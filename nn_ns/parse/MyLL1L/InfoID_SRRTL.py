
import re
from .RawToken import RawToken, RawTokenizeFail
from .str_op import join_children

class InfoID_SRRTL:
    def __repr__(self):
        return self.get_raw_init_repr()
    
class InfoContainsInfoDefineTypeIDs(InfoID_SRRTL):
    def __init__(self, infoDefineTypeID_ls):
        self.set_children(infoDefineTypeID_ls)
        return
    
    def set_children(self, infoDefineTypeID_ls):
        if infoDefineTypeID_ls:
            self.children = infoDefineTypeID_ls
            for c in self.children:
                if not isinstance(c, InfoDefineTypeID):
                    print(type(c), c)
                assert isinstance(c, InfoDefineTypeID)
        else:
            self.children = []
        return
    pass
    def get_children_raw_init_repr(self):
        s = ', '.join(c.get_raw_init_repr() for c in self.children)
        
        return '[{!r}]'.format(s)
class InfoDefineStateID(InfoContainsInfoDefineTypeIDs):
    def __init__(self, ID, infoDefineTypeID_ls):
        assert isinstance(ID, str)
        
        self.ID = ID
        super().__init__(infoDefineTypeID_ls)
        assert infoDefineTypeID_ls
        return
    
    def fix_subresult(self, subresult):
        if subresult == None:
            return subresult
        (raw_token, state_op) = subresult
        if raw_token.type == None:
            raw_token.type = ''
            
        assert raw_token.state == None # to be set
        raw_token.state = self.ID
        return subresult


    def match(self, string, begin, end): # -> None or (raw_token, state_op) # state_op :: ns -> void
        #print(self.ID, 'match')
        for c in self.children:
            r = c.startswith(string, begin, end)
            if None != r:
                return self.fix_subresult(r)
        return None

    def get_define(self):
        s = join_children(self.ID, (c.get_define() for c in self.children))
        return s

    def get_raw_init_repr(self):
        return 'InfoDefineStateID({!r}, {})'\
               .format(self.ID, self.get_children_raw_init_repr())
class InfoDefineTypeID(InfoID_SRRTL):
    def __init__(self, ID, infoDefineBody):
        self.ID = ID

        assert isinstance(infoDefineBody, InfoDefineBody)
        self.infoDefineBody = infoDefineBody
        return
    def fix_subresult(self, subresult):
        if subresult == None:
            return subresult
        (raw_token, state_op) = subresult
        if raw_token.type == None:
            raw_token.type = self.ID
        #state_id = None # to be set
        return subresult
    
    def complete_match(self, string, begin, end, trueend):
        #print(self.ID, 'complete_match')
        r = self.infoDefineBody.complete_match(string, begin, end, trueend)
        return self.fix_subresult(r)
    def startswith(self, string, begin, end):
        #print(self.ID, 'startswith')
        r = self.infoDefineBody.startswith(string, begin, end)
        return self.fix_subresult(r)
    def get_define(self):
        head = ''
        if self.ID != None:
            head = '{!r} = '.format(self.ID)
        return '{}{}'.format(head, self.infoDefineBody.get_define())
    def get_raw_init_repr(self):
        return 'InfoDefineTypeID({!r}, {})'\
               .format(self.ID, self.infoDefineBody.get_raw_init_repr())



class InfoDefineBody(InfoID_SRRTL): 
    def make_result(self, begin, end):
        state_id = None # to be set
        type_id = None # to be set
        raw_token = RawToken(state_id, type_id, begin, end)
        state_op = self.state_op
        return (raw_token, state_op)
    
class InfoDefineIfClause(InfoDefineBody):
    def __init__(self, state_op, rex=None):
        # rex == None means no if-test that is 'otherwise'
        self.str_rex = rex
        if rex != None:
            assert isinstance(rex, str)
            rex = re.compile(rex)
        self.rex = rex
        self.state_op = state_op
        assert isinstance(state_op, InfoStateOp)
        return

    #def state_op(self, ns):raise # to be overwrite
    def _test(self, string, begin, end, trueend):
        if self.rex != None:
            m = self.rex.match(string, end, trueend)
            if not m:
                return None
        
        return self.make_result(begin, end)
    

    def complete_match(self, string, begin, end, trueend):
        #print('if', 'complete_match')
        return self._test(string, begin, end, trueend)

    def startswith(self, string, begin, end):
        #print('if', 'startswith')
        trueend = end
        end = begin
        return self._test(string, begin, end, trueend)
    def get_define(self):
        head = ''
        if self.str_rex != None:
            head = 'if {!r} '.format(self.str_rex)
        return '{}{}'.format(head, self.state_op.get_define())
    def get_raw_init_repr(self):
        return 'InfoDefineIfClause({}, rex = {!r})'\
               .format(self.state_op.get_raw_init_repr(), self.str_rex)


class InfoStateOp(InfoID_SRRTL):pass

class InfoGoto(InfoStateOp):
    def __init__(self, state_id):
        self.state_id = state_id
        #print('init', self.state_id, id(self))
    def __call__(self, ns):
        #print(self.state_id, id(self))
        ns.call_stack[-1] = self.state_id
        return
    def get_define(self):
        return 'goto {}'.format(self.state_id)
    def get_raw_init_repr(self):
        return 'InfoGoto({!r})'.format(self.state_id)
class InfoCall(InfoStateOp):
    def __init__(self, state_id):
        self.state_id = state_id
    def __call__(self, ns):
        ns.call_stack.append(self.state_id)
        return
    def get_define(self):
        return 'call {}'.format(self.state_id)
    def get_raw_init_repr(self):
        return 'InfoCall({!r})'.format(self.state_id)
class InfoReturn(InfoStateOp):
    def __init__(self):pass
    def __call__(self, ns):
        ns.call_stack.pop()
        return
    def get_define(self):
        return 'return'
    def get_raw_init_repr(self):
        return 'InfoReturn()'
class InfoError(InfoStateOp):
    def __init__(self, error_string):
        self.error_string = error_string
    def __call__(self, ns):
        err = 'call_stack: {!r}  error: {}'.format(ns.call_stack, self.error_string)
        pos = ns.pos
        raise RawTokenizeFail(err, pos=pos)
    
    def get_define(self):
        return 'error {!r}'.format(self.error_string)
    def get_raw_init_repr(self):
        return 'InfoError({!r})'.format(self.error_string)
    

class InfoNormalDefine(InfoContainsInfoDefineTypeIDs, InfoDefineBody):
    def __init__(self, rex=None, infoDefineTypeID_ls=None):
        # rex == None means 'otherwise'
        self.rex_str = rex
        if rex != None:
            assert isinstance(rex, str)
            rex = re.compile(rex)
        self.rex = rex
        super().__init__(infoDefineTypeID_ls)
        return

    def state_op(self, ns):pass
    def _complete_match(self, string, begin, end):
        if self.rex == None:
            return True
        m = self.rex.match(string, begin, end)
        if m:
            assert m.start() == begin
            return m.end() == end
        return False
    def _startswith(self, string, begin, end):
        if self.rex == None:
            return end
        m = self.rex.match(string, begin, end)
        if m:
            assert m.start() == begin
            return m.end()
        return None
    
    def try_children(self, string, begin, end, trueend):
        for c in self.children:
            r = c.complete_match(string, begin, end, trueend)
            if None != r:
                return r

        return self.make_result(begin, end)
    def complete_match(self, string, begin, end, trueend):
        #print('=', 'complete_match')
        if not self._complete_match(string, begin, end):
            return None
        return self.try_children(string, begin, end, trueend)

    def startswith(self, string, begin, end):
        #print('=', 'startswith')
        trueend = end
        end = self._startswith(string, begin, end)
        if end == None:
            return None
        return self.try_children(string, begin, end, trueend)

    def get_define(self):
        head = 'otherwise'
        if self.rex_str != None:
            head = repr(self.rex_str)

        if self.children:
            head = join_children(head, (c.get_define() for c in self.children))
        return head
    def get_raw_init_repr(self):
        return 'InfoNormalDefine({!r}, {})'\
               .format(self.rex_str, self.get_children_raw_init_repr())
                    

