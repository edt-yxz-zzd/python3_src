# finite automata
# (states, symbols, transitions, initial_state, final_states)

import itertools # for chain
from root.graph.directed_graph import dedges2u2vtc, reverse_u2vtc
from root.graph.dgraph_DFS import dgraph_DFS, ENTER
from root.graph.dgraph_ordered_partition import end_of_cell2rngs, rngs2end_of_cell, \
     refine_ordered_partition_to_coarsest_equitable


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

        
    def get_finals(self):
        return tuple(i for i in range(self.M) if self._is_final_idx(i))
    def get_nonfinals(self):
        return tuple(i for i in range(self.M) if not self._is_final_idx(i))



    # symbol
    def _get_transition_symbols(self, indices):
        return set(itertools.chain.from_iterable(self._get_transition(i).keys() for i in indices))
    def _get_set_of_all_known_symbols(self):
        return self._get_transition_symbols(range(self.M))
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
    



def union_states(fa, get_initial, get_default, get_transition_symbols, get_next, get_state, *, state_key=None):
    q0 = get_initial(fa)
    qs = {}
    to_process = {q0}

    def add_to_process(q):
        if q not in qs:
            to_process.add(q)
    while to_process:
        q = to_process.pop()
        #if q in qs: continue
        assert q not in qs
        qs[q] = None # fail and next_ can be q, too

        fail = get_default(fa, q)
        add_to_process(fail)

        goto = {}
        syms = get_transition_symbols(fa, q)
        for sym in syms:
            next_ = get_next(fa, q, sym)
            add_to_process(next_)
            
            if next_ != fail:
                goto[sym] = next_
        qs[q] = (fail, goto)


        
    q_ls = sorted(qs.keys(), key = state_key)
    q2idx = {q:i for i, q in enumerate(q_ls)}
    fail = tuple(q2idx[qs[q][0]] for q in q_ls)
    gotos = tuple(qs[q][1] for q in q_ls)
    for goto in gotos:
        for sym, q in goto.items():
            goto[sym] = q2idx[q]

    transitions = gotos
    defaults = fail
    state0 = q2idx[q0]
    state = q2idx[get_state(fa)]
    state2substates = q_ls
    substates2state = q2idx
    return transitions, defaults, state0, state, state2substates, substates2state


def unionFAs_get_initial(FA_ls):
    q0 = tuple(fa.get_initial() for fa in FA_ls)
    return q0
def unionFAs_get_default(FA_ls, q):
    fail = tuple(fa.get_default(qx) for fa, qx in zip(FA_ls, q))
    return fail
def unionFAs_get_transition_symbols(FA_ls, q):
    syms = set().union(fa.get_transition(qx).keys() for fa, qx in zip(FA_ls, q))
    return syms
def unionFAs_get_next(FA_ls, q, sym):
    next_ = tuple(fa.next(qx, sym) for fa, qx in zip(FA_ls, q))
    return next_

def unionFAs_get_state(FA_ls):
    state = tuple(fa.get_state() for fa in FA_ls)
    return state
def unionFAs(FA_ls):
    
    def state_tuple_key(state_tuple):
        assert len(FA_ls) == len(state_tuple)
        return tuple(fa.state_key(state) for fa, state in zip(FA_ls, state_tuple))
        
    return union_states(FA_ls, unionFAs_get_initial, unionFAs_get_default,
                        unionFAs_get_transition_symbols, unionFAs_get_next,
                        unionFAs_get_state, state_key = state_tuple_key)

'''

def unionFAs(FA_ls):
    assert len(FA_ls) > 1
    q0 = tuple(fa.get_initial() for fa in FA_ls)
    qs = {}
    to_process = {q0}

    def add_to_process(q):
        if q not in qs:
            to_process.add(q)
    while to_process:
        q = to_process.pop()
        #if q in qs: continue
        assert q not in qs

        fail = tuple(fa.get_default(qx) for fa, qx in zip(FA_ls, q))
        add_to_process(fail)

        goto = {}
        syms = set.union(fa.get_transition(qx).keys() for fa, qx in zip(FA_ls, q))
        for sym in syms:
            next_ = tuple(fa.next(qx, sym) for fa, qx in zip(FA_ls, q))
            add_to_process(next_)
            
            if next_ != fail:
                goto[sym] = next_
        qs[q] = (fail, goto)

    q_ls = sorted(qs.keys())
    q2idx = {q:i for i, q in enumerate(q_ls)}
    fail = tuple(q2idx[qs[q][0]] for q in q_ls)
    gotos = tuple(qs[q][1] for q in q_ls)
    for goto in gotos:
        for sym, q in goto.items():
            goto[sym] = q2idx[q]

    transitions = gotos
    defaults = fail
    state0 = q2idx[q0]
    state2substates = q_ls
    substates2state = q2idx
    return transitions, defaults, state0, state2substates, substates2state

'''

        
    
class DFA(FA):
##    def smallest(self):
##        return DFA([{}], [0], 0, [False])
    def _raw_classify_states(self):
        M = self.M
        q0 = self.get_initial()
        F = self.get_finals()
        
        reachable = [1] * M
        dg = self.to_directed_graph()
        for case, path, node in dgraph_DFS(dg, [q0]):
            if case == ENTER:
                reachable[node] *= 2 # reachable from initial state
                
        rdg = reverse_u2vtc(dg)
        for case, path, node in dgraph_DFS(rdg, F):
            if case == ENTER:
                reachable[node] *= 3 # reachable to final state

        isolated = set() # -> None
        dead = set() # -> fail
        unreachable = set() # -> None
        good = set() # -> super_node
        d = {1: isolated, 2: dead, 3: unreachable, 6: good}
        for state, x in enumerate(reachable):
            d[x].add(state)
            
        assert q0 in good or q0 in dead
        assert len(good) + len(dead)
        assert set().union(*[good, dead, unreachable, isolated]) == set(range(M))
        return good, dead, unreachable, isolated
        
    def minimize(self):
        # Unreachable States: Unreachable states of a DFA are not reachable from the initial state of DFA on any possible input sequence.
        # Dead States: A dead state is a nonfinal state of a DFA whose transitions on every input symbol terminates on itself. For example, q is a dead state if q is in Q F, and δ(q, a) = q for every a in Σ.
        # Nondistinguishable States: Nondistinguishable states are those states of a DFA for which there exist no distinguishing strings; hence, they cannot be distinguished from one another.
        
        old2new, new2old, dfa = self._raw_reduce()

        super2states, state2super, super_dfa = dfa.merge_nondistinguishable_states()

        old2super = []
        for old in range(self.M):
            new = old2new[old]
            if new == None:
                super_state = None
            else:
                super_state = state2super[new]
            old2super.append(super_state)

##        print('old2new', old2new)
##        print('state2super', state2super)
##        print('old2super', old2super)
        return old2super, super_dfa


    def merge_nondistinguishable_states(self):
        super2states, state2super = self.state2nondistinguishable_superstate()
        super2state = [states[0] for states in super2states]

        xsyms = self._get_all_symbols_and_xsymbol()
        xsym = xsyms[-1]
        syms = xsyms[:-1]

        
        defaults = []
        for state in super2state:
            defaults.append(state2super[self.next(state, xsym)])
        
        gotos = []
        for super_state, state in enumerate(super2state):
            default = defaults[super_state]
            goto = {}
            gotos.append(goto)
            for sym in syms:
                to = state2super[self.next(state, sym)]
                if to != default:
                    goto[sym] = to

        q0 = state2super[self.get_initial()]
        is_final = [self.is_final(state) for state in super2state]
        super_dfa = DFA(gotos, defaults, q0, is_final)

        # check
        def next_states(fa, state, syms):
            return [fa.next(state, sym) for sym in syms]
                
        for super_state, states in enumerate(super2states):
            super_nexts = next_states(super_dfa, super_state, xsyms)
            
            for state in states:
                nexts = next_states(self, state, xsyms)
                assert super_nexts == [state2super[state] for state in nexts]

                    
        return super2states, state2super, super_dfa
        
    def state2nondistinguishable_superstate(self):
        super2states = self.nondistinguishable_states()
        state2super = [None] * self.M
        for super_state, states in enumerate(super2states):
            for state in states:
                state2super[state] = super_state

        
        return super2states, state2super

        

    def nondistinguishable_states(self):
        syms, _rngs, u2vtc = self.to_directed_graph_with_color_vertex()

        N = len(u2vtc)
        M = self.M
        
        
        vertices = list(range(N))
        for alpha in [[(0, M), (M, N)], _rngs]:
            end_of_cell = rngs2end_of_cell(alpha)
            ordered_partition = vertices, end_of_cell
            r = refine_ordered_partition_to_coarsest_equitable(u2vtc, ordered_partition, alpha)
            assert r == ordered_partition
        
        
        F = self.get_finals()
        nF = self.get_nonfinals()
        vertices[:M] = F + nF
        assert len(vertices) == N
        end_of_cell = rngs2end_of_cell(_rngs)
        end_of_cell[len(F)-1] = True

        alpha = [(0, len(F))] + _rngs[2:] # since _rngs is a coarsest equitable ordered partition
##        print('g', u2vtc)
##        print('_rngs', _rngs)
##        print('alpha', alpha)
##        print('type(F)', type(F))
##        print('F', F)
##        print('vertices', vertices)
##        print('end_of_cell', end_of_cell)
##        

        
        ordered_partition = vertices, end_of_cell
        r = refine_ordered_partition_to_coarsest_equitable(u2vtc, ordered_partition, alpha)
        vertices, end_of_cell = r
##        rngs = end_of_cell2rngs(end_of_cell)
##        print('vertices', vertices)
##        print('end_of_cell', end_of_cell)
##        print('rngs', rngs)


        
        vertices, end_of_cell = vertices[:M], end_of_cell[:M]
        rngs = end_of_cell2rngs(end_of_cell)

        super_vertices = [vertices[begin:end] for begin, end in rngs]
        super_vertices.sort()
##        print('rngs', rngs)
##        print('super_vertices', super_vertices)
        return super_vertices
        
        
        
    def _raw_reduce(self):
        'discard unreachable states; merge dead states;'
        M = self.M
        q0 = self.get_initial()
        F = self.get_finals()

        good, dead, unreachable, isolated = self._raw_classify_states()

        # set up new2old
        new2old = list(good)
        if dead:
            old_fail = min(dead)
            new2old.append(old_fail)
        
        new2old.sort()
        if dead:
            new_fail = new2old.index(old_fail)
        new_M = len(new2old)

        # set up old2new
        old2new = [None] * M
        for new, old in enumerate(new2old):
            old2new[old] = new
        for old in dead:
            old2new[old] = new_fail

        # set up new_defaults
        new_defaults = [None] * new_M
        for new, old in enumerate(new2old):
            old_default = self.get_default(old)
            new_default = old2new[old_default]
            assert new_default != None
            new_defaults[new] = new_default
            
        # set up new_gotos
        new_gotos = []
        for new, old in enumerate(new2old):
            old_goto = self._get_transition(old)
            new_default = new_defaults[new]
            new_goto = {symbol: old2new[state]
                        for symbol, state in old_goto.items()
                        if new_default != old2new[state]}
            new_gotos.append(new_goto)


        # set up DFA
        assert len(new_gotos) == new_M
        new_q0 = old2new[q0]
        new_F = {old2new[q] for q in F}
        new_F.discard(None)
        new_is_final = [False] * new_M
        for q in new_F:
            new_is_final[q] = True
        dfa = DFA(new_gotos, new_defaults, new_q0, new_is_final)

        return old2new, new2old, dfa
        
                
    

    def to_directed_graph_with_color_vertex(self):
        syms, table = self.to_goto_table()
        assert len(syms) == len(table[0])
        M = self.M
        N = len(syms)
        
        edges = []

        for q in range(M):
            goto = table[q]
            for s in range(N):
                to = goto[s]
                v = (s+1) * M + q
                edges.append((q, v))
                edges.append((v, to))

        rngs = [(i*M, (i+1)*M) for i in range(N+1)]
        u2vtc = dedges2u2vtc((N+1)*M, edges)
        return syms, rngs, u2vtc
    
            
        

    def to_directed_graph(self):
        ls = []
        for i, goto in enumerate(self.gotos):
            fail = self.get_default(i)
            vtc = {fail}
            vtc.update(goto.values())
            vtc = list(vtc)
            ls.append(vtc)
        return ls
    pass



class FA_LINK(DFA):
    def __init__(self, FA_ls):
        assert len(FA_ls) > 1
        transitions, defaults, state0, state, state2substates, substates2state = unionFAs(FA_ls)
        final = self._calc_final_ls(FA_ls, state2substates)
        
        super().__init__(transitions, defaults, state0, final)
        
        self.FA_ls = FA_ls
        self.state2substates = state2substates
        self.substates2state = substates2state
        
    def get_substates2state(self):
        return self.substates2state
    def get_state2substates(self):
        return self.state2substates
    def _calc_final_ls(self, FA_ls, state2substates):
        final = tuple(self._calc_final_item(FA_ls, q) for q in state2substates) 
    def _calc_final_item(self, FA_ls, states):
        raise
    
class FA_OR(FA_LINK):
    def __init__(self, FA_ls):
        super().__init__(FA_ls) 
    def _calc_final_item(self, FA_ls, states):
        return any(FA_ls(idx).is_final(state) for idx, state in enumerate(states))

    pass

class FA_AND(FA_LINK):
    def __init__(self, FA_ls):
        super().__init__(FA_ls)
    def _calc_final_item(self, FA_ls, states):
        return all(FA_ls(idx).is_final(state) for idx, state in enumerate(states))

    pass


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
    def to_DFA(self):
        typ = type(self)
        transitions, defaults, state0, state, dfa_state2nfa_state, nfa_state2dfa_state = \
                     union_states(self, typ.get_initial, typ.get_default, \
                                  typ._get_transition_symbols, typ.next, typ.get_state, \
                                  state_key = self.state_key)
        
        final = tuple(self.is_final(nfa_state) for nfa_state in dfa_state2nfa_state)
        dfa = DFA(transitions, defaults, state0, final)
        dfa.set_state(state)
        return dfa, dfa_state2nfa_state, nfa_state2dfa_state

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
        is_final = [self._is_final_idx(i) for i in range(self.M)]
        return NFA(gotos, fail, q0, is_final)
            

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
                




#accumulate chain
def concatNFAs_get_initial(NFA_ls):
    q0 = tuple((NFA_ls[0].get_initial() if i == 0 else None) for i, nfa in enumerate(NFA_ls))
    return q0
def concatNFAs_get_default(NFA_ls, q):
##    ns = tuple(nfa.nstate() for nfa in NFA_ls)
##    offsets = accumulate(ns)
##    state_idx2offset = tuple(chain.from_iterable(([offset] * n) for n, offset in zip(ns, offsets)))
##    
    fail = tuple((nfa.get_default(qx) if qx != None else None) for nfa, qx in zip(NFA_ls, q))
    return fail
def concatNFAs_get_transition_symbols(NFA_ls, q):
    syms = set().union((nfa._get_transition_symbols(qx) if qx != None else []) for nfa, qx in zip(NFA_ls, q))
    return syms
def concatNFAs_get_next(NFA_ls, q, sym):
    next_ = list((nfa.next(qx, sym) if qx != None else None) for nfa, qx in zip(NFA_ls, q))
    for i in range(len(next_) - 1):
        nfa = NFA_ls[i]
        qx = next_[i]

        # i.final -> zero move to -> i+1.initial
        if nfa.is_final(qx):
            nfa_right = NFA_ls[i+1]
            q0_right = nfa_right.get_initial()
            
            q_right = next_[i+1]
            if q_right == None:
                q_right = frozenset()

            q_right = q_right | q0_right
            next_[i+1] = q_right
            
    return tuple(next_)

def concatNFAs_get_state(NFA_ls):
    state = tuple((NFA_ls[0].get_state() if i == 0 else None) for i, nfa in enumerate(NFA_ls))
    return state
def concatNFAs(NFA_ls):
    
    def state_tuple_key(state_tuple):
        assert len(NFA_ls) == len(state_tuple)
        return tuple((nfa.state_key(state) if state != None else None)
                     for nfa, state in zip(NFA_ls, state_tuple))
        
    return union_states(NFA_ls, concatNFAs_get_initial, concatNFAs_get_default,
                        concatNFAs_get_transition_symbols, concatNFAs_get_next,
                        concatNFAs_get_state, state_key = state_tuple_key)

class NFA_CONCAT(DFA):
    def __init__(self, NFA_ls, finalNFA_indices):
        assert len(NFA_ls) > 1
        transitions, defaults, state0, state, state2substates, substates2state = concatNFAs(NFA_ls)

        finalNFA_indices = tuple(finalNFA_indices)
        final = self._calc_final_ls(NFA_ls, state2substates, finalNFA_indices)
        
        super().__init__(transitions, defaults, state0, final)
        
        self.NFA_ls = NFA_ls
        self.state2substates = state2substates
        self.substates2state = substates2state
        self.finalNFA_indices = finalNFA_indices
        
    def get_substates2state(self):
        return self.substates2state
    def get_state2substates(self):
        return self.state2substates
    def _calc_final_ls(self, NFA_ls, state2substates, finalNFA_indices):
        final = tuple(self._calc_final_item(NFA_ls, q, finalNFA_indices) for q in state2substates) 
    def _calc_final_item(self, NFA_ls, states, finalNFA_indices):
        is_final = lambda nfa, state: False if state == None else nfa.is_final(state)
        return any(is_final(NFA_ls[idx], states[idx]) for idx in finalNFA_indices)
   

class NFA_CONCAT_finalFromNFAIdx(NFA_CONCAT):
    def __init__(self, NFA_ls, finalFromNFAIdx):
        N = len(NFA_ls)
        assert -N <= finalFromNFAIdx < N

        
        if finalFromNFAIdx < 0:
            finalFromNFAIdx += N
        assert 0 <= finalFromNFAIdx < N
        
        finalNFA_indices = range(finalFromNFAIdx, N)
        super().__init__(NFA_ls, finalNFA_indices)
        return
    pass

class NFA_CONCAT_finalAllNFA(NFA_CONCAT_finalFromNFAIdx):
    def __init__(self, NFA_ls):
        finalFromNFAIdx = 0
        super().__init__(NFA_ls, finalFromNFAIdx)
        return
    pass

class NFA_CONCAT_finalLastNFA(NFA_CONCAT_finalFromNFAIdx):
    def __init__(self, NFA_ls):
        finalFromNFAIdx = -1
        super().__init__(NFA_ls, finalFromNFAIdx)
        return
    pass
    
    
    




def test_DFA():
    gotos = [{'a':1, 'b':0}, {}, {}]
    fail = [2, 2, 2]
    q0 = 0
    final = [False, True, False]
    dfa = DFA(gotos, fail, q0, final)

    assert not dfa
    dfa.gos('bbbbbb')

    assert not dfa
    dfa.gos('bbbbbba')
    assert dfa
    dfa.go('a')
    assert not dfa
    assert dfa.get_state() == 2
    dfa.gos('aaaafb')
    assert not dfa
    assert dfa.get_state() == 2

    dfa.reset()
    assert not dfa
    assert dfa.get_state() == 0
    dfa.go('c')
    assert not dfa
    assert dfa.get_state() == 2

def test_DFA_minimize():
    
    gotos = [{'a':1, 'b':4}, {'a':2, 'b':5}, {'a':2, 'b':5},
             {'a':2, 'b':3}, {'a':4, 'b':4}, {'a':2, 'b':3},
             {'a':2, 'b':5}, {'a':7, 'b':7}, {'a':2, 'b':5}]

    fail = []
    for goto in gotos:
        default = goto['b']
        fail.append(default)
        for k, v in list(goto.items()):
            if v == default:
                del goto[k]
        
    
    q0 = 0
    final = [False, False, False, True, False, False, True, False, False]
    dfa = DFA(gotos, fail, q0, final)

    r = good, dead, unreachable, isolated = {0,1,2,3,5}, {4}, {6, 8}, {7}
    nondistinguishable_states = [[0], [1,2,8], [3], [4, 7], [5], [6]]

    assert dfa._raw_classify_states() == r
    assert dfa.nondistinguishable_states() == nondistinguishable_states


    
    super2states, state2super, super_dfa = dfa.merge_nondistinguishable_states()
    assert state2super == [0, 1, 1, 2, 3, 4, 5, 3, 1]
    super_gotos = [{'a':1, 'b':3}, {'a':1, 'b':4}, {'a':1, 'b':2},
                   {'a':3, 'b':3}, {'a':1, 'b':2}, {'a':1, 'b':4},]
    super_fail = []
    for goto in super_gotos:
        default = goto['b']
        super_fail.append(default)
        for k, v in list(goto.items()):
            if v == default:
                del goto[k]
        
    assert super_dfa.gotos == super_gotos
    assert super_dfa.get_defaults() == super_fail



    old2super, super_dfa = dfa.minimize()
##    print('old2super', old2super)
##    print('super_gotos', super_gotos)
##    print('super_dfa.gotos', super_dfa.gotos)
    assert old2super == [0, 1, 1, 2, 3, 4, None, None, None]
    assert super_dfa.gotos == super_gotos[:-1]
    assert super_dfa.get_defaults() == super_fail[:-1]
    

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

    dfa, dfa_state2nfa_state, nfa_state2dfa_state = nfa.to_DFA()
    assert dfa.get_nstate() == 6
    
def test():
    test_DFA()       
    test_NFA()
    test_DFA_minimize()
test()







