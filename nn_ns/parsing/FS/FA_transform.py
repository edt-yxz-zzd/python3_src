
__all__ = '''
    ndfa2dfa
    
    clean_dfa
    std_named_dfa
    minimize_dfa
'''.split()


from sand.types.ToProcess import FILOOnce
from .Set_Dict_Pair import set_union, empty_set, flip_dict
from .Maybe import *
from .FA_prime import SimpleDFA, SimpleNDFA, \
    collect_maybe_symbols_from_ndfa_transition, \
    collect_symbols_from_dfa_transition
from .FA_Dgraph import dfa2unoriented_dgraph, \
     dgraph2reversed_unoriented_dgraph, \
     dfs_ordering, \
     order_states_by_symbol
from .Dgraph import find_mini_depth




def ndfa2dfa(ndfa):
    ndstate2maybe_symbols = collect_maybe_symbols_from_ndfa_transition(ndfa.transition)
    def nd_to_maybe_symbols(ndstate):
        return ndstate2maybe_symbols.get(ndstate, empty_set)
    
    dinitial = ndstates = ndfa.calc_initials() # ndfa states

    #dstates = {} # dfa states -->> all states
    dtransition = {} # dfa transition
    #dfinals = set() 
    to_process = FILOOnce([dinitial])
    def dstate2dstates(dstate):
        ndstates = dstate
        maybe_symbols = set_union(map(nd_to_maybe_symbols, ndstates))
        for maybe_symbol in maybe_symbols:
            if maybe_symbol != nothing:
                next_dstate = ndfa.completed_goto(ndstates, maybe_symbol)
                dtransition[(dstate, unjust(maybe_symbol))] = next_dstate
                # bug: missing dinitial if final
##                if ndfa.is_final(next_dstate):
##                    dfinals.add(next_dstate)
                yield next_dstate
                
    
    to_process.apply(dstate2dstates)
    dall_states = to_process.known_inputs
    dfinals = frozenset(filter(ndfa.is_final, dall_states))
    dfa = SimpleDFA(ndfa.alphabet,
                    dall_states, (dinitial,), dfinals,
                    dtransition)


    #fsm = SimpleNDFA2FSM(ndfa)
    
    #assert dfa_std_eq(fsm2dfa(SimpleNDFA2FSM(ndfa)), dfa) # delete me
    return dfa




def dfa_args_eq(lhs, rhs):
    assert type(lhs) == type(rhs) == SimpleDFA
    return lhs._get_args() == rhs._get_args()

def dfa_std_eq(lhs, rhs):
    assert type(lhs) == type(rhs) == SimpleDFA
    return dfa_args_eq(clean_dfa(lhs), clean_dfa(rhs))



def clean_dfa(dfa):
    return std_named_dfa(minimize_dfa(dfa))



def std_named_dfa(dfa):
    ':: Ord Symbol => DFA -> DFA; new_state :: integer'
    states = order_states_by_symbol(dfa)
    state2int = {state : i for i, state in enumerate(states)}
    return rename_dfa_states(dfa, state2int)
    
def minimize_dfa(dfa):
    ':: DFA -> DFA ; new_state = nondistinguishable_old_states'
    unreachable_states = find_unreachable_states(dfa)
    dfa = remove_dfa_states(dfa, unreachable_states)
    
    dead_states = find_dead_states(dfa)
    dfa = remove_dfa_states(dfa, dead_states)
    dfa = merge_nondistinguishable_states(dfa)
    return dfa


def merge_nondistinguishable_states(dfa):
    ':: DFA -> DFA ; new_state = nondistinguishable_old_states'
    nondistinguishables_set = classify_nondistinguishable_states(dfa)
    state2nondistinguishables = {s: ss
                                 for ss in nondistinguishables_set
                                 for s in ss}
    dfa = rename_dfa_states(dfa, state2nondistinguishables)

    return dfa

def remove_dfa_states(dfa, states):
    ':: DFA -> Set State -> DFA'

    new_maybe_initial = nothing if (dfa.maybe_initial != nothing and
                                    unjust(dfa.maybe_initial) in states) else\
                        dfa.maybe_initial
    new_finals = dfa.finals - states
    new_all_states = dfa.all_states - states
    new_alphabet = dfa.alphabet
    new_transition = {(q0, symbol): qt
                      for (q0, symbol), qt in dfa.transition.items()
                      if q0 not in states and qt not in states}
    return SimpleDFA(new_alphabet,
                     new_all_states, new_maybe_initial, new_finals,
                     new_transition)
                        

    
def rename_dfa_states(dfa, old_state2new_state):
    ':: DFA -> Map OldState NewState -> DFA'

    f = old_state2new_state.__getitem__
    
    new_alphabet = dfa.alphabet
    new_maybe_initial = nothing if dfa.maybe_initial == nothing else \
                        just(f(unjust(dfa.maybe_initial))) # bug: forgot "just"
    new_finals = frozenset(map(f, dfa.finals))
    all_states = (dfa.all_states & set(old_state2new_state))
    new_all_states = frozenset(map(f, all_states))

    new_transition = {(f(q0), symbol) : f(qt)
                      for (q0, symbol), qt in dfa.transition.items()}

    return SimpleDFA(new_alphabet,
                     new_all_states, new_maybe_initial, new_finals,
                     new_transition)
def rename_dfa_states_with_prefix(dfa, prefix):
    old2new = {state : (prefix, state) for state in dfa.all_states}
    return rename_dfa_states(dfa, old2new)

    
        
def find_unreachable_states(dfa):
    ':: DFA -> Set State'
    g = dfa2unoriented_dgraph(dfa)
    reachable_states = dfs_ordering(g, dfa.maybe_initial)
    unreachable_states = dfa.all_states - set(reachable_states)
    return unreachable_states
def find_dead_states(dfa):
    ':: DFA -> Set State'
    g = dfa2unoriented_dgraph(dfa)
    g = dgraph2reversed_unoriented_dgraph(g)
    productive_states = dfs_ordering(g, dfa.finals)
    dead_states = dfa.all_states - set(productive_states)
    return dead_states



def classify_nondistinguishable_states(dfa):
    ':: DFA -> Set (Set State)'
    g = dgraph2reversed_unoriented_dgraph(dfa2unoriented_dgraph(dfa))
    state2mini_length = find_mini_depth(g, dfa.finals)
    # NOTE: all lengthes are finite, i.e. there are no dead states
    # let error state be a distinguishable state from state2mini_length.keys()
    # then nondead states with different transition symbols are distinguishable
    #      since goto(nondead_state, alphabet - transition_symbols(nondead_state))
    #            -> nothing, i.e. error_state
    state2symbols = collect_symbols_from_dfa_transition(dfa.transition)
    # if state is final without jumps then state not in state2symbols
    to_symbols = lambda state: state2symbols.get(state, empty_set)
    
    state2color = {state: (L, to_symbols(state))
                   for state, L in state2mini_length.items()}


    # color2states.values() are the initial distinguishable states
    color2states = flip_dict(state2color)
    new_classes = list(color2states.values())
    assert all(new_classes)
    state2class = {state: states for states in new_classes for state in states}

    def to_rules(state):
        # assume rule ::= "A = a B ;". no "A = ;" since finals have been seperated
        rules = ((symbol, state2class[dfa.transition[(state, symbol)]])
                 for symbol in to_symbols(state))
        return frozenset(rules)

    prev_num_classes = 0
    while len(new_classes) != prev_num_classes:
        prev_num_classes = len(new_classes)
        to_process = new_classes
        new_classes = []

        while to_process:
            states = to_process.pop()
            assert states
            
            state2rules = {state: to_rules(state) for state in states}
            rules2states = flip_dict(state2rules)

            new_classes.extend(rules2states.values())
            if len(rules2states) == 1:
                continue
            
            assert len(rules2states) > 1
            for new_class in rules2states.values():
                for state in new_class:
                    state2class[state] = new_class
        
        
    return new_classes







    

def test_ndfa(s):
    rex = "[ab]*b[ab][ab]"
    
    transition_data = [
                  (0, ''), 3,
                  (0, ''), 1,
                  (1, 'a'), 2,
                  (1, 'b'), 2,
                  (2, ''), 1,
                  (2, ''), 3,
                  
                  (3, 'b'), 4,
                  (4, 'a'), 5,
                  (4, 'b'), 5,
                  (5, 'a'), 6,
                  (5, 'b'), 6,
                  ]
    transition = {key: [] for key in transition_data[::2]}
    for key, val in zip(transition_data[::2], transition_data[1::2]):
        transition[key].append(val)
    transition = {(q, tuple(maybe)): frozenset(to) for (q, maybe), to in transition.items()}
    
    initials = {0}
    finals = {6}
    alphabet = set('ab')
    all_states = set(range(7))
    ndfa = SimpleNDFA(alphabet, all_states, initials, finals, transition)
    dfa = ndfa2dfa(ndfa)
    
    def str2is_final(ndfa, s):
        states = ndfa.calc_initials()
        yield ndfa.is_final(states)
        for ch in s:
            states = ndfa.completed_goto(states, (ch,))
            yield ndfa.is_final(states)
    return list(str2is_final(ndfa, s))
assert test_ndfa('abb') == [False, False, False, False]
assert test_ndfa('abbaabbbabab') == [False, False, False, False, True, True, False, False, True, True, True, False, True]





