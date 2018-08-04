# finite automata
# (states, symbols, transitions, initial_state, final_states)

import itertools # for chain


class FA:
    # state is int
    # transitions :: [{symbol:state}]
    # defaults :: [state]
    # initial_state :: state or frozenset{state}
    # final_states :: [bool]
    # not_ :: bool # means "not_ xor final_states[state]"
    # let M = len(transitions)
    # states = {0..M-1}
    # assume there are infinite symbols, so there is a default state to goto.
    # assert len(defaults) == M == len(final_states)
    # let dict = transitions[state]
    # next_state = dict[symbol] if symbol in dict
    #              else defaults[state]
    def __init__(self, transitions, defaults, initial_state, is_final_states, not_ = False):
        assert not_ in {0, 1} # so I can use ^ as xor.

        M = len(transitions)
        assert M == len(defaults) == len(is_final_states)
        
        self.check_transitions(transitions)
        self.check_defaults(defaults)
        self.check_initial_state(M, initial_state)
        self.check_final_states(is_final_states)
        assert isinstance(not_, bool)
        self.M = M
        self.gotos = transitions
        self._fail = defaults
        self._q0 = initial_state
        self._final = is_final_states
        self._not_ = not_
        self.reset()
        return




    
    # check ...
    def check_transitions(self, transitions):
        assert len(transitions)
        M = len(transitions)
        for goto in transitions:
            for state in goto.values():
                self.check_state(M, state)
    def check_defaults(self, defaults):
        assert len(defaults)
        M = len(defaults)
        for state in defaults:
            self.check_default(M, state)
    def check_default(self, M, default):
        self.check_state(M, default)
    def check_initial_state(self, M, initial_state):
        self.check_state(M, initial_state)
        
    def check_final_states(self, final_states):
        assert len(final_states)
        M = len(final_states)
        for b in final_states:
            assert isinstance(b, bool)
    
    def check_state(self, M, state):
        self.check_idx(M, state)
    def check_idx(self, M, idx):
        assert 0 <= idx < M




    # ...
    def get_nstate(self):
        return self.M
    def get_args(self):
        return (self.gotos, self.get_defaults(),
                self.get_initial(), self._final,
                self._not_)

    def copy(self):
        args = self.get_args()
        return type(self)(*args)
    
    def not_(self):
        args = list(self.get_args())
        args[-1] = not args[-1]
        return type(self)(*args)

    def _get_transition(self, idx):
        return self.gotos[idx]


    
    # next go
    def _idx_next(self, idx, symbol):
        self.check_idx(self.M, idx)
        d = self._get_transition(idx)
        if symbol in d:
            return d[symbol]
        else:
            return self._get_idx_default(idx)

    def get_next(self, state, symbol): # == next()
        return self.next(state, symbol)
    def next(self, state, symbol):
        return self._idx_next(state, symbol)
    def nexts(self, state, symbols):
        for s in symbols:
            state = self.next(state, s)
        return s
    def gos(self, symbols):
        for s in symbols:
            self.go(s)
        
    def go(self, symbol):
        state = self.next(self.get_state(), symbol)
        self.set_state(state)





    # state
    def _shift_state_idx(self, state_idx, offset):
        self.check_idx(self.M, state_idx)
        shifted_state_idx = state_idx + offset
        return shifted_state_idx
    def _shift_back_state_idx(self, shifted_state_idx, offset):
        state_idx = shifted_state_idx - offset
        self.check_idx(self.M, state_idx)
        return state_idx
    
    def shift_state(self, state, offset):
        return self._shift_state_idx(state, offset)
    def shift_back_state(self, shifted_state, offset):
        return self._shift_back_state_idx(shifted_state, offset)
        
    def get_initial(self):
        return self._q0
    def reset(self):
        self.set_state(self.get_initial())
    def set_state(self, state):
        self.check_state(self.M, state)
        self.state = state
        
    def get_state(self):
        return self.state

    def state_key(self, state):
        self.check_state(self.M, state)
        return state

    def _default_state(self, state):
        return self.get_state() if state == None else state
    def get_defaults(self):
        return self._fail
    def get_default(self, state=None):
        state = self._default_state(state)
        return self._get_idx_default(state)
    def _get_idx_default(self, idx):
        self.check_idx(self.M, idx)
        return self.get_defaults()[idx]



    # final
    def __bool__(self):
        return self.is_final() # accept

    
    def is_final(self, state=None):
        state = self._default_state(state)
        return self._not_ ^ self._is_final(state)

    def _is_final(self, state):
        return self._is_final_idx(state)
    def _is_final_idx(self, idx):
        return self._final[idx]

# wrong: a NFA with _not_ == False is a NFA of or-finals
#        a NFA with _not_ == True is a NFA of and-finals,
#        in the second case, we can't build is_final to discard the _not_
##    def xxx build_is_final_ls(self):
##        return list(self.for i in range(self.M))

        
    def get_finals(self):
        return tuple(i for i in range(self.M) if self._is_final_idx(i))
    def get_nonfinals(self):
        return tuple(i for i in range(self.M) if not self._is_final_idx(i))



    # symbol
    def get_transition_symbols(self, state = None):
        state = self._default_state(state)
        return self._get_transition_symbols(state)
        
    def _get_transition_symbols(self, state):
        return self._get_transition_symbols_from_indices([state])
        
    def _get_transition_symbols_from_indices(self, indices):
        return set(itertools.chain.from_iterable(self._get_transition(i).keys() for i in indices))
    def _get_set_of_all_known_symbols(self):
        return self._get_transition_symbols_from_indices(range(self.M))
    def _get_list_of_all_known_symbols(self):
        ls = self._get_set_of_all_known_symbols()
        ls = list(ls)
        ls.sort()
        return ls
    def _get_all_symbols_and_xsymbol(self):
        syms = self._get_list_of_all_known_symbols()
        xsym = tuple(syms)
        assert xsym not in syms
        syms.append(xsym)
        return syms
    
    def to_goto_table(self):
        table = []
        syms = self._get_all_symbols_and_xsymbol()
        
        for q in range(self.M):
            ls = []
            table.append(ls)
            for sym in syms:
                to = self.next(q, sym)
                ls.append(to)
                
        return syms, table
    pass













