
from .Dgraph import *
from .FA_prime import collect_symbols_from_dfa_transition
from itertools import chain


def dfa2unoriented_dgraph(dfa):
    ':: DFA -> Map State (Set State)'
    state2symbols = collect_symbols_from_dfa_transition(dfa.transition)
    def to_states(state, symbols):
        return (dfa.transition[(state, symbol)] for symbol in symbols)

    dedges = ((state, next_state)
              for state, symbols in state2symbols.items()
              for next_state in to_states(state, symbols))

    # bug: what if finals/initial not in g??
    maybe_missing_vtcs = chain(dfa.maybe_initial, dfa.finals)

    return dedges2unoriented_dgraph(dedges, maybe_missing_vtcs)

    state2states = {state : frozenset(to_states(state, symbols))
                    for state, symbols in state2symbols.items()}
    # bug: state2states is a incomplete dgraph

    vtcs = set_union(state2states.values())
    missing_vtcs = vtcs - set(state2states)
    state2states.update(dict.fromkeys(missing_vtcs, emptyset))
    return state2states



def dfa2oriented_dgraph(dfa):
    ':: Ord Symbol => DFA -> Map State [State] ; children by ord of symbols'
    state2symbols = collect_symbols_from_dfa_transition(dfa.transition)
    def to_states(state, symbols):
        s = set()
        for symbol in sorted(symbols):
            vtx = next_state = dfa.transition[(state, symbol)]
            yield vtx

    dedges = ((state, next_state)
              for state, symbols in state2symbols.items()
              for next_state in to_states(state, symbols))
    maybe_missing_vtcs = chain(dfa.maybe_initial, dfa.finals)
    return dedges2oriented_dgraph(dedges, maybe_missing_vtcs)
    # bug: state2states is a incomplete dgraph
    state2states = {state : tuple(to_states(state, symbols))
                    for state, symbols in state2symbols.items()}
    return state2states

def order_states_by_symbol(dfa, initials = None):
    ':: Ord Symbol => DFA -> [State] ; dfs ; children by ord of symbols'
    if initials is None:
        initials = dfa.maybe_initial
    g = dfa2oriented_dgraph(dfa)
    roots = initials
    return dfs_ordering(g, roots)
