
from root.graph.directed_graph import dedges2u2vtc, reverse_u2vtc
from root.graph.dgraph_DFS import dgraph_DFS, ENTER
from root.graph.dgraph_ordered_partition import end_of_cell2rngs, rngs2end_of_cell, \
     refine_ordered_partition_to_coarsest_equitable

from sand import is_main
from .FA import FA



class DFA(FA):
    @staticmethod
    def regex_null():
        return DFA([{}, {}], [1, 1], 0, [True, False])
    @staticmethod
    def regex_accept_all():
        return DFA([{}], [0], 0, [True])
    @staticmethod
    def regex_accept_nothing():
        return DFA([{}], [0], 0, [False])
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

    return




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

    return



if is_main(__name__):
    test_DFA()
    test_DFA_minimize()
    pass


