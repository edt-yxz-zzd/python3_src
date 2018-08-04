
from collections.abc import Sequence
from Slist import Slist


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

newlines0 = newline newlines
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

from split_tokenize import word_tokenize, word_newline_pattern

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
    lnode_tree = BasicParser_of_CFG('main', uID2info).to_leaf_node_tree(token_names)
    print(lnode_tree)


##
##
##sw = 'switch'
##cn = 'concat'
##tk = 'token'
##
##(sw, define, [swd, cnd, tkd]),
##(cn, main, [define, main]),





class BasicParser_of_CFG:
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
            is_close, (uID, pos), parent, end, state = r
            print(uID, end, token_names[pos:end], token_names[end:end+10])
            print(len(token_names))
            raise 'fail'

        
        return r



r'''
mstate = (is_close, (uID, pos), parent?, end, state)
open state:
    .parent !!!!!!!!! parent mstate when opening
    case:
        group:
            (i, None)
            # before ith child, that's the previous children fail at pos
        list:
            child_mstates[0:i] # a Slist stack
            # before ith child, that's the previous children match [pos:end]
            # keep close mstate of the first i children

            i_end_set: {(i, end)} # the ith child had end at 'end'
            i_pos2first_result: {(i, pos): None or closed_ichild_mstate}
            # to result of the ith child first match at pos. None - fail
            # different with '_next' match
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
            i_pos2first_result
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


def is_close(mstate):
    assert len(mstate) == 4 or  len(mstate) == 5
    close = mstate[0]
    return close
def be_close(mstate):
    assert len(mstate) == 4
    assert is_close(mstate)
def be_open(mstate):
    assert len(mstate) == 5
    assert not is_close(mstate)
def get_pos(mstate):
    return mstate[1][1]

def get_close_end(mstate):
    be_close(mstate)
    return mstate[2]
def get_open_end(mstate):
    be_open(mstate)
    return mstate[3]
def get_end(mstate):
    return get_close_end(mstate) if is_close(mstate) else get_open_end(mstate)
def get_rng(mstate):
    pos = get_pos(mstate)
    end = get_end(mstate)
    return pos, end



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
        self.opening_uID_pos_set = None
        self.farthest_open_mstate = None

        ########## error !!!!!
        self.first_match_result = None # (uID, pos) to None(fail) or end 

        return

    def case(self, uID_pos):
        uID, pos = uID_pos
        return self.uID2unode[uID][0]
    def unode(self, uID_pos):
        uID, pos = uID_pos
        return self.uID2unode[uID]
    
    def open(self, stack, uID_pos):
        #print('open', uID_pos)
        
        case = self.case(uID_pos)
        if _fg(case):
            state = (0, None)
        elif _li(case):
            i_end_set, i_pos2first_result = set(), {}
            child_mstates = Slist()
            state = child_mstates, i_end_set, i_pos2first_result
        elif _t(case):
            state = 0
        else:
            raise _r(case)

        _, pos = uID_pos
        end = pos
        return self.__open_with(stack, uID_pos, end, state)

    def __open_with(self, stack, uID_pos, end, state):
        if uID_pos in self.opening_uID_pos_set:
            return False
        
        self.opening_uID_pos_set.add(uID_pos)
        if not stack:
            parent = None
        else:
            parent = stack[-1]
            be_open(parent)
            p_end = get_end(parent)
            _, c_pos = uID_pos
            if not c_pos == p_end:
                print(uID_pos, parent[1], p_end)
            assert c_pos == p_end
                
            
        
        mstate = not CLOSE, uID_pos, parent, end, state
        stack.append(mstate)

        if self.farthest_open_mstate == None or\
           get_pos(mstate) > get_pos(self.farthest_open_mstate):
            self.farthest_open_mstate = mstate
        return True

    def back_update_last(self, stack, new_end, new_state):
        old_close_mstate = stack.pop()
        be_close(old_close_mstate)

        close, uID_pos, end, state = old_close_mstate
        #print('back_update_last', uID_pos, end, new_end)

        self.__open_with(stack, uID_pos, new_end, new_state)
        return
    def update_last(self, stack, new_end, new_state):
        old_open_mstate = stack.pop()
        be_open(old_open_mstate)
        
        close, uID_pos, parent, end, state = old_open_mstate
        #print('update_last', uID_pos, end, new_end)

        mstate = close, uID_pos, parent, new_end, new_state
        stack.append(mstate)
        return
    
    def close_last(self, stack):
        old_open_mstate = stack.pop()
        be_open(old_open_mstate)
        
        close, uID_pos, parent, end, state = old_open_mstate
        #print('close_last', uID_pos)

        case = self.case(uID_pos)
        if _t(case):
            uID, pos = uID_pos
            assert state == 1
            assert end == pos + 1
##            assert state == 0
##            assert end == pos
##            state = 1
##            end += 1
            
        mstate = not close, uID_pos, end, state
        stack.append(mstate)
        self.__remove_uID_pos(uID_pos)
        return
        
    def __remove_uID_pos(self, uID_pos):
        self.opening_uID_pos_set.remove(uID_pos)


    def parse(self):
        if self.opening_uID_pos_set is not None:
            raise Exception('reenter this obj')
        assert self.farthest_open_mstate == \
               self.first_match_result == \
               self.opening_uID_pos_set == None
        

        self.opening_uID_pos_set = set()
        self.farthest_open_mstate = None
        #self.first_match_result = {}
        
        stack = []
        self.open(stack, (self.main_uID, self.begin))


        handler = self._match
        while handler is not None:
            handler = handler(stack)



        
        if not stack:
            # fail
            r = False, self.farthest_open_mstate
        else:
            main_closed_mstate = stack.pop()
            clup_state = self.clean_up_closed_mstate(main_closed_mstate)
            r = True, clup_state
        assert not stack

        self.farthest_open_mstate = \
            self.first_match_result =\
            self.opening_uID_pos_set = None
        
        return r

    def _log(self, s):
        assert s

        
        if len(s) == 1:
            close, uID_pos, end, state = s[-1]
            if not self.meet_end or end == self.end:
                # finish!!
                return None
            return self._next

        closed_child_mstate = s.pop()
        be_close(closed_child_mstate)
        close, (c_uID, c_pos), new_end, c_state = closed_child_mstate
        #print('_log', c_uID, c_pos, new_end)

        
        curr_mstate = s[-1]
        be_open(curr_mstate)
        close, uID_pos, parent, old_end, state = curr_mstate
        assert c_pos == old_end
        
        case = self.case(uID_pos)
        unode = self.unode(uID_pos)
        if _fg(case):
            _, _, leaves = unode
            i, x = state
            assert x is None

            assert i < len(leaves)

            new_state = i, closed_child_mstate
            self.update_last(s, new_end, new_state)
            return self._match
        
            
        elif _li(case):
            _, _, lchildren = unode
            child_mstates, i_end_set, i_pos2first_result = state
            assert len(child_mstates) < len(lchildren)
            i = len(child_mstates)
            if (i, new_end) in i_end_set:
                return self._popped_rollback
            else:
                i_end_set.add((i, new_end))
                
            if (i, c_pos) not in i_pos2first_result:
                i_pos2first_result[(i, c_pos)] = closed_child_mstate
            
            child_mstates <<= closed_child_mstate
            new_state = child_mstates, i_end_set, i_pos2first_result
            self.update_last(s, new_end, new_state)
            return self._match
            
        elif _t(case):
            raise logic-error
        
        else:
            raise _r(case)
        
        
        
    def _match(self, s):
        curr_mstate = s[-1]
        be_open(curr_mstate)

        
        close, uID_pos, parent, end, state = curr_mstate

        (uID, pos) = uID_pos
        case = self.case(uID_pos)
        unode = self.unode(uID_pos)
        if _fg(case):
            _, _, leaves = unode
            i, x = state
            if x is not None:
                # success
                self.close_last(s)
                return self._log

            if i == len(leaves):
                # fail
                return self._rollback
            
            ichild_uID = leaves[i]
            assert pos == end
            if not self.open(s, (ichild_uID, end)):
                # left-recur
                # fail
                return self._popped_rollback
                return self._rollback

            return self._match
        
            
        elif _li(case):
            _, _, lchildren = unode
            child_mstates, i_end_set, i_pos2first_result = state
            i = len(child_mstates)

            if (i, end) in i_pos2first_result:
                closed_mstate = i_pos2first_result[(i, end)]
                if closed_mstate is None:
                    # fail
                    return self._popped_rollback

                assert len(closed_mstate) == 4
                s.append(closed_mstate)
                return self._log
                
            if len(child_mstates) == len(lchildren):
                # success
                self.close_last(s)
                return self._log
            
            ilchild_uID = lchildren[i]
            if not self.open(s, (ilchild_uID, end)):
                return self._popped_rollback
            return self._match
            

        elif _t(case):
            _, _, token_name = unode
            if pos < self.end and self.tokens[pos] == token_name:
                # success !!
                new_end = pos + 1
                new_state = 1
                self.update_last(s, new_end, 1)
                self.close_last(s)
                return self._log
            return self._rollback
        else:
            raise _r(case)
        
        
    def _rollback(self, s):
        if not s:
            # exit parse with fail
            return None
        
        failed_child_mstate = s.pop()
        be_open(failed_child_mstate)

        close, uID_pos, parent, end, state = failed_child_mstate
        self.__remove_uID_pos(uID_pos)
        
        if not s:
            # exit parse with fail
            return None
        return self._popped_rollback(s)

    def _popped_rollback(self, s):
        curr_mstate = s[-1]
        be_open(curr_mstate)
        close, uID_pos, parent, end, state = curr_mstate

        (uID, pos) = uID_pos
        case = self.case(uID_pos)
        unode = self.unode(uID_pos)
        if _fg(case):
            _, _, leaves = unode
            i, x = state
            assert x is None

            assert i < len(leaves)
            assert end == pos

            new_state = i + 1, x
            self.update_last(s, end, new_state)
            return self._match
        
            
        elif _li(case):
            _, _, lchildren = unode
            child_mstates, i_end_set, i_pos2first_result = state
            assert len(child_mstates) < len(lchildren)
            i = len(child_mstates)
            if (i, end) not in i_pos2first_result:
                i_pos2first_result[(i, end)] = None

                
            if not child_mstates:
                # fail
                return self._rollback
            
            child_mstates, closed_child_mstate = child_mstates.pop()
            new_state = child_mstates, i_end_set, i_pos2first_result
            _close, (_uID, _pos), old_end, _state = closed_child_mstate
            assert end == old_end
            new_end = _pos
            self.update_last(s, new_end, new_state)
            s.append(closed_child_mstate)
            return self._next
            
        elif _t(case):
            raise logic-error
        
        else:
            raise _r(case)

    def _next(self, s):
        curr_mstate = s[-1]
        be_close(curr_mstate)

        
        close, uID_pos, end, state = curr_mstate

        (uID, pos) = uID_pos
        case = self.case(uID_pos)
        unode = self.unode(uID_pos)
        if _fg(case):
            _, _, leaves = unode
            i, x = state
            assert x is not None
            assert i < len(leaves)
            
            closed_ichild_mstate = x
            new_end = pos
            new_state = i, None
            self.back_update_last(s, new_end, new_state)

            assert len(closed_ichild_mstate) == 4
            s.append(closed_ichild_mstate)

            return self._next
        
            
        elif _li(case):
            _, _, lchildren = unode
            child_mstates, i_end_set, i_pos2first_result = state
            assert len(child_mstates) == len(lchildren)
            if not child_mstates:
                # fail
                s.pop()
                return self._popped_rollback
            
            child_mstates, closed_child_mstate = child_mstates.pop()
            new_state = child_mstates, i_end_set, i_pos2first_result
            _close, (_uID, _pos), old_end, _state = closed_child_mstate
            assert end == old_end
            new_end = _pos
            self.back_update_last(s, new_end, new_state)
            s.append(closed_child_mstate)
            return self._next
            
        elif _t(case):
            _, _, token_name = unode
            assert pos < self.end and self.tokens[pos] == token_name
            # fail
            s.pop()
            return self._popped_rollback
        else:
            raise _r(case)



    
    
    def clean_up_closed_mstate(self, mstate):
        assert len(mstate) == 4
        clean_up = self.clean_up_closed_mstate
        be_close(mstate)
        
        is_close, uID_pos, end, state = mstate
        case = self.case(uID_pos)
        (uID, pos) = uID_pos

        rng = pos, end
        if _fg(case):
            i, ichild_mstate = state
            assert len(ichild_mstate) == 4
            ichild_clup_state = clean_up(ichild_mstate)
            clup_state = ichild_clup_state # no f/g now!!
        elif _li(case):
            child_mstates, _, _ = state
            cs_clup_states = [clean_up(ms) for ms in child_mstates]
            cs_clup_states.reverse()
            clup_state = uID, rng, cs_clup_states
        elif _t(case):
            assert state == 1
            clup_state = uID, rng
        else:
            raise _r(case)

        return clup_state



















from split_tokenize import split_tokenize

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




