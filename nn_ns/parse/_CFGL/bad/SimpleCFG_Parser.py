


r'''
id2info: # unify id !!

# FC for Finite Choose
# ^ and $ are predefined
info type:
    'switch', ID, [ref_id]
    'concat', ID, [(ref_id, is_lookahead_assertion)], [(ref_id, is_not)]
    'token_set', ID, is_in, [token_name]

one of the source form may look like:
switch_def    = ?ID :ID *
concat_def    = =ID ( +ID | >ID ) * ( &ID | !ID ) *
token_set_def = ( `ID | ~ID ) @token_name *
comment = '/*' ... '*/'
'''



from collections.abc import Sequence
from parse.Slist import Slist
from parse.split_tokenize import word_tokenize, word_newline_pattern

r'''

parse
unode (3-case):
    'switch', uID, [ref_uID]
    'concat', uID, [ref_uID]
    'token', uID, token_name

input:
    uID2unode, main_uID, tokens
output:
    tree<{uID's}> if success




'''

r'''
'''

BasicCFG_in_self = r'''


# basic_CFG = define +
main0 = define main2
main1 = define
main2 : main0 main1
main3 = newlines main2
main : main3 main2

define : switch_def concat_def token_def
switch_def = ID ':' IDs newlines
concat_def = ID '=' IDs newlines
token_def = ID 'is' tag newlines

newlines0 = newlines newline
newlines1 = newline
newlines : newlines0 newlines1

IDs0 = ID IDs
IDs1 = 
IDs : IDs0 IDs1


ID is --word
tag is --tag
':' is --:
'=' is --=
'is' is --is
newline is --newline
'''



def basic_CFG_tokenize(src):
    tokens = word_tokenize(src, word_newline_pattern, pycomment_start=lambda w: w == '#')

    ls = []
    for w, rng in tokens:
        if w in ': = is'.split():
            c = w
        elif w == '\n':
            c = 'newline'
        elif w[:2] == '--':
            c = 'tag'
        else:
            c = 'word'
            
        ls.append((c, rng))
    return ls



def simple_parse(src):
    tokens = word_tokenize(src, word_newline_pattern, pycomment_start=lambda w: w == '#')
    cases = ': = is'.split()
    lines = ' '.join(w for w, rng in tokens).split('\n')
    uID2info = {}
    for line in lines:
        words = line.split()
        if not words:
            continue
        
        assert len(words) >= 2
        assert words[1] in cases
        case = words[1]
        if case == ':':
            case = 'switch'
            data = words[2:]
        elif case == '=':
            case = 'concat'
            data = words[2:]
        elif case == 'is':
            case = 'token'
            assert len(words) == 3
            tag = words[2]
            assert tag[:2] == '--'
            data = tag[2:]
            
        else:
            raise ValueError()
        ID = words[0]
        if ID in uID2info:
            print(ID)
        assert ID not in uID2info
        uID2info[ID] = case, ID, data
    return uID2info
            
            
            

def t():
    tokens = basic_CFG_tokenize(BasicCFG_in_self)
    uID2info = simple_parse(BasicCFG_in_self)
    token_names = [n for n, rng in tokens]
    assert set(token_names) <= set(tname for case, _, tname in uID2info.values() if case == 'token')
    lnode_tree = SimpleParser_of_CFG('main', uID2info).to_leaf_node_tree(token_names)
    print(lnode_tree)


##
##
##sw = 'switch'
##cn = 'concat'
##tk = 'token'
##
##(sw, define, [swd, cnd, tkd]),
##(cn, main, [define, main]),





class SimpleParser_of_CFG:
    def __init__(self, main_uID, uID2unode):
        # uID is tID or iID or some unique id
        self.uID2unode = uID2unode
        self.main_uID = main_uID
        return
    def to_leaf_node_tree(self, token_names, begin = 0, end=None, main_uID=None):
        if end is None:
            end = len(token_names)
        if main_uID is None:
            main_uID = self.main_uID
            
        p = _Parser(self.uID2unode, main_uID, token_names, begin, end)
        success, r = p.parse()
        if not success:
            is_close, (uID, pos), parent, end, state, lefts = r
            print(uID, end, token_names[pos:end], token_names[end:end+10])
            print(len(token_names))
            raise 'fail'

        
        return r




import collections


OpenStateBase = collections.namedtuple('OpenStateBase',
                'close id_pos parent end state left_corner_mstates'.split())
CloseStateBase = collections.namedtuple('CloseStateBase',
                'close id_pos end state left_corner_mstates'.split())

class MStateBase:
    __slots__ = ()
    def get_pos(self):
        return self.id_pos[1]
    def get_id(self):
        return self.id_pos[0]
    def get_rng(self):
        pos = self.get_pos()
        return pos, self.end

    @property
    def pos(self):
        return self.get_pos()
    @property
    def id(self):
        return self.get_id()
    
    @property
    def rng(self):
        return self.get_rng()


    
    

    
    
class _Open(MStateBase, OpenStateBase):
    pass
    
class _Close(MStateBase, CloseStateBase):
    pass


SwitchStateBase = collections.namedtuple('SwitchStateBase',
                'i imstate'.split())
class SwitchState(SwitchStateBase):
    pass


ConcatStateBase = collections.namedtuple('ConcatStateBase',
                'child_mstates i_end_set'.split())
class ConcatState(ConcatStateBase):
    pass


r'''
mstate = (is_close, (uID, pos), parent?, end, state, left_corner_mstates)
.left_corner_mstates # a Slist stack
open state:
    .parent !!!!!!!!! parent mstate when opening
    case:
        switch:
            (i, None)
            # before ith child, that's the previous children fail at pos

        concat:
            child_mstates[0:i] # a Slist stack
            # before ith child, that's the previous children match [pos:end]
            # keep close mstate of the first i children

            i_end_set: {(i, end)} # the ith child had end at 'end'

            
        token:
            0
close state:
    case:
        group:
            (i, close_mstate_of_ichild)
            # the ith child match [pos:end]
        list:
            child_mstates[0:i] # a Slist stack
            # i's children match [pos:end]
            # keep close mstate of those children

            i_end_set
        token:
            1
'''





CLOSE = True
def _fg(case):
    return case == 'switch'
def _li(case):
    return case == 'concat'
def _t(case):
    return case == 'token'
def _r(case):
    return ValueError('unknown case: {}'.format(case))




class _Parser:
    def __init__(self, uID2unode, main_uID, tokens, begin, end, meet_end=True):
        assert 0 <= begin <= end <= len(tokens)
        self.tokens = tokens
        self.begin = begin
        self.end = end
        self.uID2unode = uID2unode
        self.main_uID = main_uID
        
        self.meet_end = meet_end
        #self.stack = None
        self.opening = None
        self.farthest_open_mstate = None
        self.left_recur = None
        self.__depth_opening = None

        self.n = 0

        return


    def check(self, s):
        if s:
            assert len(s) + bool(s[-1].close) == self.n
        else:
            assert self.n == 0
    def check_mstate(self, mstate):
        case = self.case(mstate.id_pos)
        assert type(mstate.left_corner_mstates) is Slist
        assert ['token', 'switch', 'concat'].index(case) ==\
               [int, SwitchState, ConcatState].index(type(mstate.state))
        

    def make_Open(self, *args):
        mstate = _Open(not CLOSE, *args)
        assert mstate.parent is None or (
            not mstate.parent.close)
        self.check_mstate(mstate)
        return mstate
    
    def make_Close(self, *args):
        mstate = _Close(CLOSE, *args)
        self.check_mstate(mstate)
        return mstate
        
        
    def make_state(self, case, *args):
        if _fg(case):
            state = SwitchState(*args)
            assert type(state.i) is int
            assert state.imstate is None or \
                   (state.imstate.close and type(state.imstate) is _Close)
        elif _li(case):
            state = ConcatState(*args)
            #print(type(state.child_mstates))
            assert type(state.child_mstates) is Slist
            assert type(state.i_end_set) is set
            
        elif _t(case):
            state, = args
            assert state in [0, 1]
        else:
            raise _r(case)

        return state
    
    def case(self, uID_pos):
        uID, pos = uID_pos
        return self.uID2unode[uID][0]
    def unode(self, uID_pos):
        uID, pos = uID_pos
        return self.uID2unode[uID]
    
    def open(self, stack, uID_pos):
        #print('open', uID_pos)

        left_corner_mstates = Slist()
        
        case = self.case(uID_pos)
        if _fg(case):
            state = self.make_state(case, 0, None)
        elif _li(case):
            i_end_set = set()
            child_mstates = Slist()
            state = self.make_state(case, child_mstates, i_end_set)
        elif _t(case):
            state = self.make_state(case, 0)
        else:
            raise _r(case)

        _, pos = uID_pos
        end = pos
        return self.new(stack, uID_pos, end, state, left_corner_mstates)


        
    def __try_add_uID_pos(self, s, uID_pos, lefts):
        assert len(self.opening) == len(self.__depth_opening)
        
        if uID_pos not in self.opening:
            self.opening[uID_pos] = lefts
            self.__depth_opening[uID_pos] = len(s)
        else:
            i = self.__depth_opening[uID_pos]
        #print(i, len(s))
            assert type(i) is int
            assert i < len(s)
    
        
    def __try_remove_uID_pos(self, s, uID_pos):
        # self.opening.remove(uID_pos)
        i = self.__depth_opening[uID_pos]
        #print(i, len(s))
        assert type(i) is int
        assert i <= len(s)
        if i < len(s):
            assert s[i].id_pos == uID_pos
        if len(s) == i:
            del self.opening[uID_pos]
            del self.__depth_opening[uID_pos]
            
    def kill(self, stack):
        print('kill', stack[-1].id_pos)
        self.check(stack)
        self.n -= 1
        m = stack.pop()
        assert not m.close
        self.__try_remove_uID_pos(stack, m.id_pos)
        return m
    
    def new(self, stack, uID_pos, end, state, left_corner_mstates):
        print('new', uID_pos)
        if uID_pos in self.opening:
            raise logic-error
        
        self.__try_add_uID_pos(stack, uID_pos, Slist())
        self.__new(stack, uID_pos, end, state, left_corner_mstates)

    def __new(self, stack, uID_pos, end, state, left_corner_mstates):
        self.check(stack)
        self.n += 1
        
        #self.opening.add(uID_pos)
        if not stack:
            parent = None
        else:
            parent = stack[-1]
            assert not parent.close
            _, c_pos = uID_pos
            assert c_pos == parent.end
                
            
        
        tmstate = uID_pos, parent, end, state, left_corner_mstates
        mstate = self.make_Open(*tmstate)
        stack.append(mstate)

        if self.farthest_open_mstate == None or\
           mstate.pos > self.farthest_open_mstate.get_pos():
            self.farthest_open_mstate = mstate
        return True

    def close(self, stack):
        print('close', stack[-1].id_pos)
        self.check(stack)
        self.n += 1
        old_open_mstate = stack.pop()
        assert not old_open_mstate.close
        
        close, uID_pos, parent, end, state, left = old_open_mstate
        self.__try_remove_uID_pos(stack, uID_pos)
        #print('close_last', uID_pos)

        case = self.case(uID_pos)
        if _t(case):
            uID, pos = uID_pos
            assert state == 1
            assert end == pos + 1
            
        mstate = self.make_Close(uID_pos, end, state, left)
        stack.append(mstate)
        return

    def back_close(self, stack):
        print('back_close', stack[-1].id_pos)
        self.check(stack)
        #self.n -= 1
        old_close_mstate = self.achieve(stack)
        assert old_close_mstate.close

        close, uID_pos, end, state, lefts = old_close_mstate
        self.__try_add_uID_pos(stack, uID_pos, lefts)
        self.__new(stack, uID_pos, end, state, lefts)
        return

    def update_end_state(self, stack, new_end, new_state):
        self.update(stack, new_end, new_state, stack[-1].left_corner_mstates)
    def update_lefts(self, stack, left_corner_mstates):
        self.update(stack, stack[-1].end, stack[-1].state, left_corner_mstates)
    def update(self, stack, new_end, new_state, left_corner_mstates):
        self.check(stack)
        old_open_mstate = stack.pop()
        assert not old_open_mstate.close
        
        close, uID_pos, parent, _end, _state, _left = old_open_mstate
        #print('update_last', uID_pos, end, new_end)

        mstate = self.make_Open(uID_pos, parent,
                                new_end, new_state, left_corner_mstates)
        stack.append(mstate)
        return
    def ropen_with_newstate(self, stack, end, state, lefts):
        self.back_close(stack)
        self.update(stack, end, state, lefts)
    def achieve(self, stack):
        self.check(stack)
        self.n -= 2
        m = stack.pop()
        assert m.close
        return m
    def restore(self, stack, mstate):
        self.check(stack)
        self.n += 2
        assert mstate.close
        stack.append(mstate)
        
    


    def parse(self):
        if self.opening is not None:
            raise Exception('reenter this obj')
        assert self.farthest_open_mstate == \
               self.opening == None
        

        self.opening = {} # set()
        self.farthest_open_mstate = None
        self.left_recur = set()
        self.__depth_opening = {}
        
        stack = []
        self.open(stack, (self.main_uID, self.begin))


        handler = self._match
        args = ()
        while handler is not None:
            handler = handler(stack, *args)
            if type(handler) is tuple:
                handler, *args = handler
            else:
                args = ()

            for id_pos, i in self.__depth_opening.items():
                if not i < len(stack):
                    print('i < len(stack): i = {}; L = {}; id_pos'.format(i, len(stack)), id_pos)
            assert all(i < len(stack) for i in self.__depth_opening.values())
                



        
        if not stack:
            # fail
            r = False, self.farthest_open_mstate
        else:
            main_closed_mstate = self.achieve(stack)
            clup_state = self.clean_up_closed_mstate(main_closed_mstate)
            r = True, clup_state
        assert not stack

        self.farthest_open_mstate = None
        self.opening = None
        self.left_recur = None
        self.__depth_opening = None
        
        return r


    def _back_log(self, s):
        assert s
        
        curr_mstate = s[-1]
        assert not curr_mstate.close
        uID_pos, state = curr_mstate.id_pos, curr_mstate.state
        print('_back_log', uID_pos)
        
        case = self.case(uID_pos)
        unode = self.unode(uID_pos)
        if _fg(case):
            _, _, leaves = unode
            i, ichild_mstate = state
            assert ichild_mstate is not None
            
            assert i < len(leaves)

            new_state = self.make_state(case, i, None)
            new_end = curr_mstate.pos
            self.update_end_state(s, new_end, new_state)
            self.restore(s, ichild_mstate)
            return self._next
        
            
        elif _li(case):
            _, _, lchildren = unode
            child_mstates, i_end_set = state
            assert len(child_mstates) <= len(lchildren)
            assert child_mstates
            
            
            child_mstates, closed_child_mstate = child_mstates.pop()
            new_state = self.make_state(case, child_mstates, i_end_set)
            
            assert curr_mstate.end == closed_child_mstate.end
            new_end = closed_child_mstate.pos
            
            self.update_end_state(s, new_end, new_state)
            self.restore(s, closed_child_mstate)
            return self._next
            
        elif _t(case):
            raise logic-error
        
        else:
            raise _r(case)
        
    def _log(self, s):
        assert s
        print('_log', s[-1].id_pos)

        
        if len(s) == 1:
            mstate = s[-1]
            if not self.meet_end or mstate.end == self.end:
                # finish!!
                return None
            return self._next

        closed_child_mstate = self.achieve(s)
        assert closed_child_mstate.close
        new_end = closed_child_mstate.end

        
        curr_mstate = s[-1]
        assert not curr_mstate.close
        uID_pos, state = curr_mstate.id_pos, curr_mstate.state
        assert closed_child_mstate.pos == curr_mstate.end
        
        case = self.case(uID_pos)
        unode = self.unode(uID_pos)
        if _fg(case):
            _, _, leaves = unode
            i, x = state
            assert x is None

            assert i < len(leaves)

            new_state = self.make_state(case, i, closed_child_mstate)
            self.update_end_state(s, new_end, new_state)
            return self._match
        
            
        elif _li(case):
            _, _, lchildren = unode
            child_mstates, i_end_set = state
            assert len(child_mstates) < len(lchildren)
            i = len(child_mstates)
            
            child_mstates <<= closed_child_mstate
            new_state = self.make_state(case, child_mstates, i_end_set)
            self.update_end_state(s, new_end, new_state)
            
            if (i, new_end) in i_end_set:
                return self._back_log
            else:
                i_end_set.add((i, new_end))
                
            return self._match
            
        elif _t(case):
            raise logic-error
        
        else:
            raise _r(case)
        

##    def push_lefts(self, s):
##        self.close(s)
##        curr_mstate = new_left = self.achieve(s)
##        new_lefts = curr_mstate.left_corner_mstates
##        new_lefts <<= new_left
##        
##        # open same uID
##        if not self.open(s, curr_mstate.id_pos):
##            raise logic-error
##
##        self.update_lefts(s, new_lefts)
##        return
##
##    def _close_left_corner_child(self, s, child_uID_pos):
##        stack_idx = self.opening[child_uID_pos]
##        
##        ancestor_open_mstate_of_same_uID = s[stack_idx]
##        mstate_stack = ancestor_open_mstate_of_same_uID.left_corner_mstates
##        if not mstate_stack:
##            return self._popped_rollback
##        closed_mstate = mstate_stack.data
##        assert closed_mstate.id == curr_mstate.uID
##        self.restore(closed_mstate)
##        return self._log
        
    def _match(self, s):
        print('_match', s[-1].id_pos)
        curr_mstate = s[-1]
        assert not curr_mstate.close

        
        uID_pos, state = curr_mstate.id_pos, curr_mstate.state

        case = self.case(uID_pos)
        unode = self.unode(uID_pos)
        if _fg(case):
            _, _, leaves = unode
            
            i, x = state
            if x is not None:
                # success
                #self.update_last_left(s)
                return self._finish

            if i == len(leaves):
                # fail
                return self._rollback

            
            assert curr_mstate.pos == curr_mstate.end
            ichild_uID = leaves[i]

            return self._open_ref, (ichild_uID, curr_mstate.end)

        elif _li(case):
            _, _, lchildren = unode
            child_mstates, i_end_set = state
            i = len(child_mstates)
                
            if len(child_mstates) == len(lchildren):
                # success
                return self._finish
            
            ichild_uID = lchildren[i]
            return self._open_ref, (ichild_uID, curr_mstate.end)

        elif _t(case):
            _, _, token_name = unode
            assert curr_mstate.pos == curr_mstate.end
            pos = curr_mstate.end
            if pos < self.end and self.tokens[pos] == token_name:
                # success !!
                new_end = pos + 1
                new_state = 1
                self.update_end_state(s, new_end, new_state)
                return self._finish
            return self._rollback
        else:
            raise _r(case)

        
    def _open_ref(self, s, uID_pos):
        print('_open_ref', s[-1].id_pos, uID_pos)
        curr_mstate = s[-1]
        assert not curr_mstate.close
        if uID_pos in self.opening:
            # ref_id : left-recur
            ref_id, _ = uID_pos
            self.left_recur.add(ref_id)
            
            lefts = self.opening[uID_pos]
            if not lefts:
                # fail
                return self._fail_match
            
            self.restore(s, lefts.data)
            return self._log

        self.open(s, uID_pos)
        return self._match


    def _finish(self, s):
        print('_finish', s[-1].id_pos)
        curr_mstate = s[-1]
        assert not curr_mstate.close

        
        uID_pos, state = curr_mstate.id_pos, curr_mstate.state
        if curr_mstate.id in self.left_recur:
            is_top_one = len(s)-1 == self.__depth_opening[curr_mstate.id_pos]
            lefts = self.opening[curr_mstate.id_pos]
            self.close(s)
            if is_top_one:
                assert curr_mstate.id_pos not in self.opening
            # error: curr_mstate.id_pos not in self.opening
            
            lefts <<= s[-1]
            self.back_close(s)
            assert curr_mstate.id_pos in self.opening

                
            self.opening[curr_mstate.id_pos] = lefts
            
            if is_top_one:
                self.kill(s)
                assert curr_mstate.id_pos not in self.opening
                self.open(s, curr_mstate.id_pos)
                self.update_lefts(s, lefts)

                return self._match
            else:
                pass
            pass

            
        self.close(s)
        return self._log

        
        
    def _rollback(self, s):
        print('_rollback', s[-1].id_pos)
        if not s:
            # exit parse with fail
            return None
        
        failed_child_mstate = self.kill(s)
        assert not failed_child_mstate.close
        if failed_child_mstate.left_corner_mstates:
            self.restore(s, failed_child_mstate.left_corner_mstates.data)
            return self._log
        
        
        
        if not s:
            # exit parse with fail
            return None
        return self._fail_match

    def _fail_match(self, s):
        print('_fail_match', s[-1].id_pos)
        curr_mstate = s[-1]
        assert not curr_mstate.close
        close, uID_pos, parent, end, state, left = curr_mstate

        (uID, pos) = uID_pos
        case = self.case(uID_pos)
        unode = self.unode(uID_pos)
        if _fg(case):
            _, _, leaves = unode
            i, x = state
            assert x is None
            assert i < len(leaves)
            assert end == pos

            new_state = self.make_state(case, i + 1, x)
            self.update_end_state(s, end, new_state)
            return self._match
        
            
        elif _li(case):
            _, _, lchildren = unode
            child_mstates, i_end_set = state
            assert len(child_mstates) < len(lchildren)
            
            if not child_mstates:
                # fail
                return self._rollback
            else:
                return self._back_log
            
        elif _t(case):
            raise logic-error
        
        else:
            raise _r(case)

    def _next(self, s):
        print('_next', s[-1].id_pos)
        curr_mstate = s[-1]
        assert curr_mstate.close
        
        close, uID_pos, end, state, left = curr_mstate
        case = self.case(uID_pos)
        unode = self.unode(uID_pos)

        
        self.back_close(s)
        if _fg(case):
            return self._back_log
        elif _li(case):
            _, _, lchildren = unode
            child_mstates, i_end_set = state
            assert len(child_mstates) == len(lchildren)
            if not child_mstates:
                return self._rollback
            
            return self._back_log
            
        elif _t(case):
            return self._rollback
        
        else:
            raise _r(case)


    
    
    def clean_up_closed_mstate(self, mstate):
        clean_up = self.clean_up_closed_mstate
        assert mstate.close
        
        is_close, uID_pos, end, state, left = mstate
        case = self.case(uID_pos)
        (uID, pos) = uID_pos

        rng = pos, end
        if _fg(case):
            i, ichild_mstate = state
            ichild_clup_state = clean_up(ichild_mstate)
            clup_state = ichild_clup_state # no f/g now!!
        elif _li(case):
            child_mstates, _ = state
            cs_clup_states = [clean_up(ms) for ms in child_mstates]
            cs_clup_states.reverse()
            clup_state = uID, rng, cs_clup_states
        elif _t(case):
            assert state == 1
            clup_state = uID, rng
        else:
            raise _r(case)

        return clup_state




















def tokenize_of_free_style_CFGL(txt_in_free_style_CFGL):
    rtokens = split_tokenize(txt_in_free_style_CFGL)
    types = []
    rngs = []
    keywords = set('* + ? *? +? ?? is = { } [ ] ; : . :-'.split())
    
    for value, rng in rtokens:
        if value[0] == '#':
            continue
        elif value in keywords:
            token_name = value
        elif value.startswith('--'):
            token_name = '#'
        else:
            token_name = 'w'
        types.append(token_name)
        rngs.append(rng)
    return types, rngs


##from CFGL import CFGL_in_free_style_CFGL
##from rnode_tree_to_tID2tnode import tID2tnode_of_CFGL_in_CFGL
##
##
##
##tokens = tokenize_of_free_style_CFGL(CFGL_in_free_style_CFGL)
##pr = Parser_of_XL_in_CFGL('CFGL_in_free_style_CFGL', tID2tnode_of_CFGL_in_CFGL)
##pr.to_leaf_node_tree(tokens)
##
##



t()




