
from functools import reduce
import operator
from .ChildrenMixin import ChildrenMixin
from .ParseResult import MatchFail, make_match_result, getMatchResultRng
from .str_op import join_children

FIRST = 'FIRST'
FOLLOW = 'FOLLOW'



class InfoID(ChildrenMixin):
    def __init__(self, define_type, ID, *, tID = None, children = None):
        super().__init__()
        self.define_type = define_type
        self.ID, self.tID = ID, tID
        self.set_children(children)
        self.first = None
        self.id2info = None
        self.debug = False
        return



    ###################### first / follow #######################
    
    # tID is (ID,) or (...parentID, ID)
    # ftID is (f, tID) where f is 'FIRST' or 'FOLLOW' => fstID, fwtID
    # FRef is a set of ftID
    # FirstRef is FRef, indicate how to make up First
    # FollowRef is is FRef, indicate how to make up Follow
    def getDisjointRules(self):return [] # list of FRef
    def getPreKnownFirst(self):return set() # set of token_type
    def getFirstRef(self):return set()
    def exportFollowRef(self, fwtID2FollowRef):pass
    def set_FIRST(self, first):# first: set of token_type
        self.first = first
        return
    def set_id2info(self, id2info): # id2info[ID] = InfoID
        self.id2info = id2info
        return

    ###################### match #######################
    def isInFirst(self, token):
        return token.type in self.first
    def make_match_result(self, begin_end, children):
        return make_match_result(self.tID, begin_end, children)
    
    def match(self, tokens, begin, end):
        if self.debug:
            print('debug InfoID; try {} ;'.format(self.tID))
            try:
                r = self._match(tokens, begin, end)
            except:
                print('debug InfoID; fail {} ;'.format(self.tID))
                raise
            else:
                print('debug InfoID; success {} ;'.format(self.tID))
                return r
        return self._match(tokens, begin, end)
        
    def _match(self, tokens, begin, end):
        raise NotImplementedError('_match')


    ###################### basic #######################
    def getStrName(self):
        # may not ID!! ID may be number
        r = self._getStrName()
        assert r == None or isinstance(r, str)
        return r
    
    def _getStrName(self):
        return self.ID
        

    def nullable(self):
        return self._nullable()
    def _nullable(self, s):
        raise NotImplementedError('_nullable')


    def set_tID(self, tID):
        assert tID[-1] == self.ID
        assert isinstance(tID, tuple)
        self.tID = tID
        return

    def get_define(self):
        raise NotImplementedError('get_define')
    def set_debug(self, debug = True):
        self.debug = debug
    def get_raw_init_repr(self):
        raise NotImplementedError('get_raw_init_repr')


class InfoIDLeaf(InfoID):
    def _set_children(self, children):
        assert children == None
        super()._set_children(children)
        return


class InfoIDNamedChildren(InfoID):
    def __init__(self, define_type, ID, *, tID = None, children = None):
        self.name2idx = None
        super().__init__(define_type, ID, tID = tID, children = children)
        return

    def _get_name_idx_ls(self):
        return list(self.name2idx.items())

    def _get_names(self):
        return list(self.name2idx.keys())
    
    def _set_children(self, children):
        super()._set_children(children)
        if children == None:
            self.name2idx = None
        else:
            self.name2idx = {}
            for i, child in enumerate(children):
                name = child.getStrName()
                if name == None:
                    continue
                if name in self.name2idx:
                    raise Exception('duplicate name: {!r}'.format(name))
                self.name2idx[name] = i
                
        return
    
    def _getitem_str(self, s):
        i = self.name2idx[s]
        return self[i]
    def set_debug(self, debug = True):
        super().set_debug(debug)
        for c in self:
            c.set_debug(debug)


###############################################################





class InfoIDToken(InfoIDLeaf):
    def __init__(self, token_type, ID, *, tID = None, children = None):
        self.token_type = token_type
        super().__init__('Token', ID, tID = tID, children = children)
        return

    def set_FIRST(self, first):# first: set of token_type
        assert first == None or len(first) == 1
        if len(first) == 1:
            t, = first
            assert t == self.token_type
        super().set_FIRST(first)
        return
    
    def _match(self, tokens, begin, end):
        if begin >= end:
            raise MatchFail('begin >= end: {} >= {}'.format(begin, end), pos=begin)
        t = tokens[begin]
        if not self.isInFirst(t):
            raise MatchFail('not isInFirst pos:{}, token:{}'.format(begin, t), pos=begin)

        begin_end = begin, begin+1
        r = self.make_match_result(begin_end, None)
        
        return r
    
    def getPreKnownFirst(self):
        return {self.token_type}
    
    def _nullable(self):
        return False
    
    def get_define(self):
        return '{} is t{!r}'.format(self.ID, self.token_type)
    def get_raw_init_repr(self):
        return 'InfoIDToken({!r}, {!r})'.format(self.token_type, self.ID)

class InfoIDItem(InfoIDLeaf):
    def __init__(self, ID, refID, min, max, *, key = None, tID = None, children = None):
        assert isinstance(ID, int)
        
        self.refID = refID
        self.min, self.max = min, max
        self.key = key # name in list

        tIDofRefID = (self.refID,)
        self.fs_tRefID = (FIRST, tIDofRefID)
        self.fw_tRefID = (FOLLOW, tIDofRefID)
        
        super().__init__('Item', ID, tID = tID, children = children)
        return
    
    def _match(self, tokens, begin, end):
        if begin >= end:
            if not self.nullable():
                #print(self.refID, self.id2info[self.refID]) #xxxxxxxxxxxxxxxxxx
                raise MatchFail('begin >= end: {} >= {}'.format(begin, end), pos=begin)
            r = self.make_match_result((begin, begin), [])
            return r
        
        t = tokens[begin]
        old_begin = begin
        children = []
        info = self.id2info[self.refID]
        while self.isInFirst(t) and len(children) < self.max:
            r = info.match(tokens, begin, end)
            _beg, _end = getMatchResultRng(r)
            if not begin == _beg < _end <= end:
                print(begin, _beg, _end, end, tokens[begin])
            assert begin == _beg < _end <= end

            children.append(r)
            begin = _end
            if begin == end:
                break
            t = tokens[begin]
            
        if not self.min <= len(children) <= self.max:
            s = 'pos:{} count error:not min={} <= len={} <= max= {};'\
                'tID:{}; refID:{!r}'\
                .format(begin, self.min, len(children), self.max,\
                        self.tID, self.refID)

            if begin < end:
                t = tokens[begin]
            else:
                t = '<END of TOKENS>'
            s = '{}; {}'.format(t, s)
            raise MatchFail(s, pos=begin)

        begin_end = old_begin, begin
        r = self.make_match_result(begin_end, children)
        
        return r
    
    def getDisjointRules(self):# list of FRef
        s = set()
        if not self.exact():
            s.add(self.fs_tRefID)
            
            me = self.tID
            s.add((FOLLOW, me))
        return [s]
        
    #def getPreKnownFirst(self):return set() # set of token_type
    def getFirstRef(self):
        return {self.fs_tRefID}
    
    def exportFollowRef(self, fwtID2FollowRef):
        s = fwtID2FollowRef[self.fw_tRefID]
        me = self.tID
        s.add((FOLLOW, me))
        return
    
    def _getStrName(self):
        return self.key
    def _nullable(self):
        return self.min == 0
    def exact(self):
        return self.min == self.max

    def get_define(self):
        m = self.max
        if m == float('inf'):
            m = ''
        key = self.key
        if key == None:
            key = ''
            
        return '{} {{ {} , {} }} {}'.format(self.refID, self.min, m, key)

    def get_raw_init_repr(self):
        m = self.max
        if m == float('inf'):
            m = None
        return 'InfoIDItem({!r}, {!r}, {!r}, {!r}, key = {!r})'\
               .format(self.ID, self.refID, self.min, m, self.key)


###############################################################



class InfoIDList(InfoIDNamedChildren):
    def __init__(self, ID, *, tID = None, children = None):
        super().__init__('List', ID, tID = tID, children = children)
        return
    
    def _match(self, tokens, begin, end):
        if begin >= end:
            raise MatchFail('begin >= end: {} >= {}'.format(begin, end), pos=begin)
        
        t = tokens[begin]
        old_begin = begin
        children = []
        for c in self:
            r = c.match(tokens, begin, end)
            _beg, _end = getMatchResultRng(r)
            assert begin == _beg <= _end <= end
            if not c.nullable():
                assert _beg < _end

            children.append(r)
            begin = _end

        begin_end = old_begin, begin
        r = self.make_match_result(begin_end, children)
        
        return r

    
    #def getDisjointRules(self):# list of FRef
    #def getPreKnownFirst(self):return set() # set of token_type
    def getFirstRef(self):
        s = set()
        for c in self:
            first_child = (FIRST, c.tID)
            s.add(first_child)
            if not c.nullable():
                break
        else:
            raise cant-go-here
        
        return s
    
    def exportFollowRef(self, fwtID2FollowRef):
        follow_me = (FOLLOW, self.tID)
        for i, c in enumerate(self):
            follow_child = (FOLLOW, c.tID)
            s = fwtID2FollowRef[follow_child]

            if i == len(self) - 1: #last one
                s.add(follow_me)
            else:
                nextc = self[i+1]
                first_next = (FIRST, nextc.tID)
                follow_next = (FOLLOW, nextc.tID)
                s.add(first_next)
                if nextc.nullable():
                    s.add(follow_next) # because this no string ID InfoIDItem occur here only

        return


    def _nullable(self):
        if not self.children:
            return True
        nullable = reduce(operator.and_, (c.nullable() for c in self.children)) # all
        return nullable

    def get_define(self):
        body = ' , '.join(c.get_define() for c in self)
        return '{} = {}'.format(self.ID, body)

    def get_raw_init_repr(self):
        children = '[{}]'.format(', '.join(c.get_raw_init_repr() for c in self))
        return 'InfoIDList({!r}, children = {!s})'\
               .format(self.ID, children)


    
class InfoIDBlock(InfoIDNamedChildren):
    def __init__(self, ID, *, tID = None, children = None):
        super().__init__('Block', ID, tID = tID, children = children)
        return
    
    def _match(self, tokens, begin, end):
        if begin >= end:
            raise MatchFail('begin >= end: {} >= {}'.format(begin, end), pos=begin)
        
        t = tokens[begin]
        for c in self:
            if c.isInFirst(t):
                r = c.match(tokens, begin, end)
                begin_end = getMatchResultRng(r)
                r = self.make_match_result(begin_end, [r])
                return r

        
        if not self.isInFirst(t):
            raise MatchFail('not isInFirst pos:{}, token:{}'.format(begin, t), pos=begin)
        raise cant-go-here
    


    
    def getDisjointRules(self):# list of FRef
        s = self.getFirstRef()
        return [s]
        
    #def getPreKnownFirst(self):return set() # set of token_type
    def getFirstRef(self):
        s = set()
        for c in self:
            first_child = (FIRST, c.tID)
            s.add(first_child)
        return s
    
    def exportFollowRef(self, fwtID2FollowRef):
        follow_me = (FOLLOW, self.tID)
        for c in self:
            follow_child = (FOLLOW, c.tID)
            s = fwtID2FollowRef[follow_child]
            s.add(follow_me)
        return
    
    def _nullable(self):
        if not self.children:
            return True
        nullable = reduce(operator.or_, (c.nullable() for c in self.children)) # any
        return nullable


    def get_define(self):
        return join_children(self.ID, (c.get_define() for c in self))
        body = '\n'.join(c.get_define() for c in self)
        body = body.split('\n')
        define = [self.ID]
        define.extend(body)
        define = '\n    '.join(define)
        
        return define
    
    def get_raw_init_repr(self):
        children = '[{}]'.format(', '.join(c.get_raw_init_repr() for c in self))
        return 'InfoIDBlock({!r}, children = {!s})'\
               .format(self.ID, children)
##################################################





    
