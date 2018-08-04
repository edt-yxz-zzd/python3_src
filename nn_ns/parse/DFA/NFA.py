
from sand import is_main
from .FA import FA
from .FA2DFA import FA2DFA

# NOTE:
#   NFA's _not_ attribute has strong effect on finals.
#   it classifies NFA into two case: and-NFA and or-NFA
#   if we want to modify the 'is_final' list,
#   then the '_not_' should be False.

class NFA(FA):
    # state is {int}
    # others are the same as those of FA

    
    @staticmethod
    def from_DFA(dfa):
        assert isinstance(dfa, DFA)
        args = dfa.get_args()
        transitions, defaults, initial_state, is_final_states, not_ = args

        to_nfa_state = lambda state_idx: frozenset([state_idx])
        transitions = tuple({sym : to_nfa_state(state_idx)
                             for sym, state_idx in goto.items()}
                            for goto in transitions)
        defaults = tuple(to_nfa_state(state_idx) for state_idx in defaults)
        initial_state = to_nfa_state(initial_state)
        return NFA(transitions, defaults, initial_state, is_final_states, not_)
    
    def shift_state(self, state, offset):
        self.check_state(self.M, state)
        _shift = self._shift_state_idx
        return frozenset(_shift(state_idx, offset) for state_idx in state)
    
    def shift_back_state(self, shifted_state, offset):
        _shift = self._shift_back_state_idx
        state = frozenset(_shift(state_idx, offset) for state_idx in shifted_state)
        self.check_state(self.M, state)
    
        return state

    def next(self, state, symbol):
        self.check_state(self.M, state)
        
        _idx_next = super()._idx_next
        state = frozenset().union(*tuple(_idx_next(idx, symbol) for idx in state))
        self.check_state(self.M, state)
        return state

    
    def check_state(self, M, state):
        assert len(state)
        assert isinstance(state, frozenset)
        for s in state:
            super().check_state(M, s)

    def check_default(self, M, default):
        #assert len(default) == 1
        self.check_state(M, default)

    def _is_final(self, state):
        final = super()._is_final
        return any(final(s) for s in state)

##    def get_transition(self, state=None):
##        state = self._default_state(state)
##        assert len(state) == 1
##        state = next(iter(state))
##        
##        return super().get_transition(state)
    def get_default(self, state=None):
        self.check_state(self.M, state)
        
        _get_idx_default = super()._get_idx_default
        state = frozenset().union(*tuple(_get_idx_default(s) for s in state))
        self.check_state(self.M, state)
        return state


    
    def state_key(self, state):
        self.check_state(self.M, state)
        ls = list(state)
        ls.sort()
        return tuple(ls)

    def _get_transition_symbols(self, state):
        return self._get_transition_symbols_from_indices(state)
    
##    def to_DFA(self):
##        typ = type(self)
##        transitions, defaults, state0, state, dfa_state2nfa_state, nfa_state2dfa_state = \
##                     union_states(self, typ.get_initial, typ.get_default, \
##                                  typ._get_transition_symbols, typ.next, typ.get_state, \
##                                  state_key = self.state_key)
##        
##        final = tuple(self.is_final(nfa_state) for nfa_state in dfa_state2nfa_state)
##        dfa = DFA(transitions, defaults, state0, final)
##        dfa.set_state(state)
##        return dfa, dfa_state2nfa_state, nfa_state2dfa_state

    def to_DFA(self):
        return FA2DFA(self)

    @staticmethod
    def make_new_goto(goto, idx2idx_set):
        return {k: self.extend_to_new_idx_set(idx_set, idx2idx_set)
                for k, idx_set in goto.items()}
    @staticmethod
    def extend_to_new_idx_set(idx_set, idx2idx_set):
        return frozenset().union(idx2idx_set[i] for i in idx_set)
        
    def add_nosymbol_moves(self, nosymbol_moves):
        state_idx2idx_set = self.fill_nosymbol_moves(nosymbol_moves)

        make_new_goto = lambda goto: self.make_new_goto(goto, state_idx2idx_set)
        extend_to_new_idx_set = lambda idx_set: self.extend_to_new_idx_set(idx_set, state_idx2idx_set)
        gotos = [make_new_goto(goto) for goto in self.gotos]
        fail = [extend_to_new_idx_set(idx_set) for idx_set in self.get_defaults()]
        q0 = extend_to_new_idx_set(self.get_initial())

        # bug:
##        is_final = [self._is_final_idx(i) for i in range(self.M)]
##        return NFA(gotos, fail, q0, is_final)

        _, _, _, is_final, _not_ = self.get_args()
        return NFA(gotos, fail, q0, is_final, _not_)
    
            

    def fill_nosymbol_moves(self, nosymbol_moves):
        state_idx2indices = nosymbol_moves
        state_idx2idx_set = [None] * self.M
        
        vtc_ls, edges_ls, discarded_edges = strong_connected_components(state_idx2indices)
        for vtc in vtc_ls:
            s = set()
            for v in vtc:
                state_idx2idx_set[v] = s
                
        exit_cases = {EXIT, HEXIT, HCROSS, CROSS}
        for case, path, v in dgraph_DFS(state_idx2indices):
            if case == ENTER:
                state_idx2idx_set[v].add(v)
            elif case in exit_cases:
                if len(path) > 1:
                    p = path[-2]
                    assert v == path[-1]
                    state_idx2idx_set[p] |= state_idx2idx_set[v]
        return state_idx2idx_set


    pass



def test_NFA():
    s0 = frozenset([0])
    s01 = frozenset([0,1])
    s1 = frozenset([1])
    s2 = frozenset([2])
    gotos = [{'a':s1, 'b':s01}, {}, {}]
    fail = [s2]*3
    q0 = s0
    final = [False, True, False]
    nfa = NFA(gotos, fail, q0, final)

    assert not nfa
    nfa.gos('bbbbbb')

    assert nfa
    nfa.gos('bbbbbba')
    assert nfa
    nfa.go('a')
    assert not nfa
    assert nfa.get_state() == s2
    nfa.gos('aaaafb')
    assert not nfa
    assert nfa.get_state() == s2

    nfa.reset()
    assert not nfa
    assert nfa.get_state() == s0
    nfa.go('c')
    assert not nfa
    assert nfa.get_state() == s2

    dfa = nfa.to_DFA()
    assert dfa.get_nstate() == 6

    return


if is_main(__name__):
    test_NFA()
    pass












