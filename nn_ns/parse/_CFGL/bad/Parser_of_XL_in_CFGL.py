
from collections.abc import Sequence
from Slist import Slist


def uID2unode_to_uID2case_uID2leaves_uID2child_uIDs(uID2unode_of_XL_in_CFGL):
    build = dict
    if isinstance(uID2unode_of_XL_in_CFGL, Sequence):
        build = lambda: [None] * len(uID2unode_of_XL_in_CFGL)
        
    gf_uID2leaf_uIDs, uID2child_uIDs, uID2case = [
        build() for _ in range(3)]
    
    for uID, unode in uID2unode_of_XL_in_CFGL.items():
        case = unode[0]
        uID2case[uID] = case
        
        if case == 'filter' or case == 'group':
            _case, uID, children, leaves = unode
            gf_uID2leaf_uIDs[uID] = leaves
            uID2child_uIDs[uID] = children
        elif case == 'list':
            _case, uID, children = unode
            uID2child_uIDs[uID] = children
    return uID2case, gf_uID2leaf_uIDs, uID2child_uIDs


class Parser_of_XL_in_CFGL:
    def __init__(self, main_uID, uID2unode_of_XL_in_CFGL):
        # uID is tID or iID
        self.uID2case, self.uID2leaf_uIDs, self.uID2child_uIDs = \
                       uID2unode_to_uID2case_uID2leaves_uID2child_uIDs(
                           uID2unode_of_XL_in_CFGL)
        self.uID2unode = uID2unode_of_XL_in_CFGL
        self.main_uID = main_uID

        return
    def to_leaf_node_tree(self, tokens, begin = 0, end=None, main_uID=None):
        if end is None:
            end = len(tokens)
        if main_uID is None:
            main_uID = self.main_uID
            
        p = _Parser(self, main_uID, tokens, begin, end)
        success, r = p.parse()
        if not success:
            raise 'fail'

        
        return r



r'''
mstate = (is_close, (uID, pos), parent?, end, state)
open state:
    .parent !!!!!!!!! parent mstate when opening
    case:
        filter/group:
            (i, None)
            # before ith child, that's the previous children fail at pos
        list/lchild:
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
        filter/group:
            (i, close_mstate_of_ichild)
            # the ith child match [pos:end]
        list/lchild:
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
    return case == 'filter' or case == 'group'
def _lilc(case):
    return case == 'list' or case == 'lchild'
def _li(case):
    return case == 'list'
def _lc(case):
    return case == 'lchild'
def _t(case):
    return case == 'token'
def _r(case):
    return ValueError('unknown case: {}'.format(case))


def is_close(mstate):
    close = mstate[0]
    return close
def be_close(mstate):
    assert is_close(mstate)
def be_open(mstate):
    assert not is_close(mstate)
def get_pos(mstate):
    return mstate[1][1]

def get_close_end(mstate):
    be_close(mstate)
    return mstate[2]
def get_open_end(mstate):
    be_open(mstate)
    return mstate[3]
def get_rng(mstate):
    pos = get_pos(mstate)
    end = get_close_end(mstate) if is_close(mstate) else get_open_end(mstate)
    return pos, end



class _Parser:
    def __init__(self, parser_of_XL_in_CFGL, main_uID, tokens, begin, end, meet_end=True):
        assert 0 <= begin <= end <= len(tokens)
        info = parser_of_XL_in_CFGL
        self.tokens = tokens
        self.begin = begin
        self.end = end
        self.uID2case = info.uID2case
        self.uID2leaf_uIDs = info.uID2leaf_uIDs
        self.uID2child_uIDs = info.uID2child_uIDs
        self.uID2unode = info.uID2unode
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
        return self.uID2case[uID]
    def unode(self, uID_pos):
        uID, pos = uID_pos
        return self.uID2unode[uID]
    
    def open(self, stack, uID_pos):
        
        case = self.case(uID_pos)
        if _fg(case):
            state = (0, None)
        elif _lilc(case):
            i_end_set, i_pos2first_result = set(), {}
            child_mstates = Slist()
            state = child_mstates, i_end_set, i_pos2first_result
        elif _t(case):
            state = 0
        else:
            raise _r(case)

        end = pos
        return self.__open_with(stack, uID_pos, end, state,
                                set_None_parent=set_None_parent)

    def __open_with(self, stack, uID_pos, end, state):
        if uID_pos in self.opening_uID_pos_set():
            return False
        
        self.opening_uID_pos_set.add(uID_pos)
        if not stack:
            parent = None
        else:
            parent = stack[-1]
            be_open(parent)
        
        mstate = not CLOSE, uID_pos, parent, end, state
        stack.append(mstate)

        if self.farthest_open_mstate == None or\
           get_pos(mstate) > get_pos(self.farthest_open_mstate):
            self.farthest_open_mstate = mstate
        return True
    
    def update_last(self, stack, new_end, new_state):
        old_open_mstate = stack.pop()
        be_open(old_open_mstate)
        
        close, uID_pos, parent, end, state = old_open_parent_mstate

        mstate = close, uID_pos, parent, new_end, new_state
        stack.append(mstate)
        return
    
    def close_last(self, stack):
        old_open_mstate = stack.pop()
        be_open(old_open_mstate)
        
        close, uID_pos, parent, end, state = old_open_parent_mstate

        case = self.case(uID_pos)
        if _t(case):
            uID, pos = uID_pos
            assert state == 0
            assert end == pos
            state = 1
            end += 1
            
        mstate = not close, uID_pos, end, state
        stack.append(mstate)
        self.opening_uID_pos_set.remove(uID_pos)
        return
        
    
    def reopen_last(self, stack):
        old_closed_mstate = stack.pop()
        be_close(old_closed_mstate)
        parent = stack[-1] if stack else None
        
        close, uID_pos, end, state = old_closed_mstate

        case = self.case(uID_pos)
        if _t(case):
            uID, pos = uID_pos
            assert state == 1
            assert end == pos + 1
            state = 0
            end = pos
            
        mstate = not close, uID_pos, parent, end, state
        self.open(stack, uID_pos)
        assert mstate == stack[-1]
        return
        

    def parse(self):
        if self.opening_uID_pos_set is not None:
            raise Exception('reenter this obj')
        assert self.farthest_open_mstate == \
               self.first_match_result == \
               self.opening_uID_pos_set == None
        

        self.opening_uID_pos_set = {}
        self.farthest_open_mstate = None
        self.first_match_result = {}
        
        stack = []
        self.open(stack, (self.main_uID, self.begin))


        handler = self._match
        while handler is not None:
            handler = handler(stack)


        self.farthest_open_mstate = \
            self.first_match_result =\
            self.opening_uID_pos_set = None

        
        if not stack:
            # fail
            r = False, self.farthest_open_mstate
        else:
            main_closed_mstate = stack.pop()
            clup_state = clean_up_closed_mstate(main_closed_mstate)
            r = True, clup_state
        assert not stack

        return r

    def _log(self, s):
        assert s
        #close, uID_pos, end, state = s[-1]

        
        if len(s) == 1:
            close, uID_pos, end, state = s[-1]
            if not meet_end or end == self.end:
                # finish!!
                return s, None
            return self._next

        closed_child_mstate = s.pop()
        be_close(closed_child_mstate)
        close, (c_uID, c_pos), new_end, c_state = closed_child_mstate

        
        curr_mstate = s[-1]
        be_open(curr_mstate)
        close, uID_pos, parent, old_end, state = curr_mstate
        assert c_pos == old_end
        
        case = self.case(uID_pos)
        unode = self.unode(uID_pos)
        if _fg(case):
            _, _, _, leaves = unode
            i, x = state
            assert x is None

            assert i < len(leaves)

            new_state = i, closed_child_mstate
            self.update_last(s, new_end, new_state)
            return self._match
        
            
        elif _li(case):
            _, _, lchildren = unode
            assert len(child_mstates) < len(lchildren)
            child_mstates, i_end_set, i_pos2first_result = state
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
            
                
        elif _lc(case):
            _, _, ref_id, count, _, _ = unode
            start, stop = count
            assert len(child_mstates) < stop
            child_mstates, i_end_set, i_pos2first_result = state
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
            _, _, _, leaves = unode
            i, x = state
            if x is not None:
                # success
                self.close_last(s)
                return self._log

            if i == len(leaves):
                # fail
                return self._rollback
            
            ichild_uID = leaves[i]
            if not self.open(s, ichild_uID, pos):
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
                
                s.append(closed_mstate)
                return self._log
                
            if len(child_mstates) == len(lchildren):
                # success
                self.close_last(s)
                return self._log
            
            ilchild_uID = lchildren[i]
            if not self.open(s, ilchild_uID, pos):
                return self._popped_rollback
            return self._match
            
                
        elif _lc(case):
            _, _, ref_id, count, _, _ = unode
            start, stop = count
            child_mstates, i_end_set, i_pos2first_result = state
            assert len(child_mstates) <= stop
            
            if child_mstates:
                last_child_mstate = child_mstates.data
                pos, end = get_rng(last_child_mstate)
                if pos == end:
                    if len(child_mstates) >= start:
                        # one empty production is enough
                        return self._popped_rollback
                    
                    s.append(last_child_mstate)
                    return self._log
                
            i = len(child_mstates)
            if (i, end) in i_pos2first_result:
                closed_mstate = i_pos2first_result[(i, end)]
                if closed_mstate is None:
                    # fail
                    return self._popped_rollback
                
                s.append(closed_mstate)
                return self._log

            
            if len(child_mstates) == stop:
                # success
                self.close_last(s)
                return self._log

            
            if not self.open(s, ref_id, pos):
                return self._popped_rollback
            return self._match
        elif _t(case):
            _, _, token_name = unode
            if pos < self.end and self.tokens[pos] == token_name:
                # success !!
                end = pos + 1
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
        return self._popped_rollback(s)

    def _popped_rollback(self, s):
        curr_mstate = s[-1]
        be_open(curr_mstate)
        close, uID_pos, parent, end, state = curr_mstate

        (uID, pos) = uID_pos
        case = self.case(uID_pos)
        unode = self.unode(uID_pos)
        if _fg(case):
            _, _, _, leaves = unode
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
            _close, _uID_pos, new_end, _state = closed_child_mstate
            self.update_last(s, new_end, new_state)
            s.append(closed_child_mstate)
            return self._next
            
                
        elif _lc(case):
            _, _, ref_id, count, _, _ = unode
            child_mstates, i_end_set, i_pos2first_result = state

            start, stop = count
            assert len(child_mstates) < stop
            i = len(child_mstates)
            if (i, end) not in i_pos2first_result:
                i_pos2first_result[(i, end)] = None
                
            if start <= len(child_mstates) <= stop:
                # success
                self.close_last(s)
                return self._log

            
            child_mstates, closed_child_mstate = child_mstates.pop()
            new_state = child_mstates, i_end_set, i_pos2first_result
            _close, _uID_pos, new_end, _state = closed_child_mstate
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
            _, _, _, leaves = unode
            i, x = state
            assert x is not None
            assert i < len(leaves)
            
            closed_ichild_mstate = x
            new_end = pos
            new_state = None
            self.update_last(s, new_end, new_state)
            s.append(closed_ichild_mstate)

            return self._next
        
            
        elif _li(case):
            _, _, lchildren = unode
            child_mstates = state
            assert len(child_mstates) == len(lchildren)
            if not child_mstates:
                # fail
                s.pop()
                return self._popped_rollback
                self.reopen_last(s)
                return self._rollback
            
            child_mstates, closed_child_mstate = child_mstates.pop()
            new_state = child_mstates
            _close, _uID_pos, new_end, _state = closed_child_mstate
            self.update_last(s, new_end, new_state)
            s.append(closed_child_mstate)
            return self._next
            
            
                
        elif _lc(case):
            _, _, ref_id, count, _, _ = unode
            child_mstates = state

            start, stop = count
            assert start <= len(child_mstates) <= stop
            if not child_mstates:
                # fail
                s.pop()
                return self._popped_rollback
                self.reopen_last(s)
                return self._rollback
            
            child_mstates, closed_child_mstate = child_mstates.pop()
            new_state = child_mstates
            _close, _uID_pos, new_end, _state = closed_child_mstate
            self.update_last(s, new_end, new_state)
            s.append(closed_child_mstate)
            return self._next
        elif _t(case):
            _, _, token_name = unode
            assert pos < self.end and self.tokens[pos] == token_name
            # fail
            s.pop()
            return self._popped_rollback
            self.reopen_last(s)
            return self._rollback
        else:
            raise _r(case)



        
        
        def clean_up_closed_mstate(self, mstate):
            clean_up = self.clean_up_closed_mstate(ichild_mstate)
            case = self.case(mstate)
            is_close, (uID, pos), end, state = mstate
            assert is_close

            rng = pos, end
            if _fg(case):
                i, ichild_mstate = state
                ichild_clup_state = clean_up(ichild_mstate)
                clup_state = ichild_clup_state # no f/g now!!
            elif _lilc(case):
                child_mstates, _, _ = state
                cs_clup_states = [clean_up(ms) for ms in child_mstates]
                cs_clup_states.reverse()
                clup_state = case, uID, rng, cs_clup_states
            elif _t(case):
                assert state == 1
                clup_state = case, uID, rng
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


from CFGL import CFGL_in_free_style_CFGL
from rnode_tree_to_tID2tnode import tID2tnode_of_CFGL_in_CFGL



tokens = tokenize_of_free_style_CFGL(CFGL_in_free_style_CFGL)
pr = Parser_of_XL_in_CFGL('CFGL_in_free_style_CFGL', tID2tnode_of_CFGL_in_CFGL)
pr.to_leaf_node_tree(tokens)










