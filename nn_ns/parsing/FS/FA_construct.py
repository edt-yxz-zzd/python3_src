
__all__ = '''
    informal_transition_rules2ndfa
    transition_rules2ndfa

    informal_transition_rules2transition_rules
'''.split()
from .Maybe import *
from .Set_Dict_Pair import group_pairs2dict, set_union
from .FA_prime import SimpleNDFA


def informal_transition_rules2ndfa(rules, initials, alphabet=None, all_states=None):
    rules = informal_transition_rules2transition_rules(rules)
    return transition_rules2ndfa(rules, initials, alphabet=alphabet, all_states=all_states)

def informal_transition_rules2transition_rules(rules):
    '''informal rules, e.g. A = a B; A = a D; B = a b C ; C = a b ; D = ; ...
formal rules, e.g. A = a B ; A = a C ; A = D ; D = ; ...

:: Iter (Nonterminal, [Symbol], Maybe Nonterminal) -> Iter (State, Maybe (Maybe Symbol, State))
where State = (Nonterminal, Integer)
'''
    for N, symbols, maybeN in rules:
        curr_state = N, 0
        for i, symbol in enumerate(symbols, 1):
            next_state = N, i
            yield curr_state, just((just(symbol), next_state))
            curr_state = next_state

        if maybeN == nothing:
            yield curr_state, nothing

        else:
            next_state = (unjust(maybeN), 0)
            yield curr_state, just((nothing, next_state))



def transition_rules2ndfa(rules, initials, alphabet=None, all_states=None):
    '''formal rules, e.g. A = a B ; A = a C ; A = D ; D = ; ...

:: Iter (State, Maybe (Maybe Symbol, State)) -> Set State -> NDFA Symbol State
'''
    
    initials = frozenset(initials)
    transition, finals = transition_rules2ndfa_transition_finals(rules)

    if alphabet is None:
        alphabet = frozenset(unjust(maybe_symbol)
                             for _, maybe_symbol in transition.keys()
                             if maybe_symbol != nothing)
    if all_states is None:
        all_states = calc_ndfa_all_states(initials, finals, transition)

    ndfa = SimpleNDFA(alphabet, all_states, initials, finals, transition)
    return ndfa

        


def calc_ndfa_all_states(initials, finals, transition):
    all_states = frozenset(q for q, _ in transition.keys())
    all_states |= set_union(transition.values())
    all_states |= initials
    all_states |= finals
    return all_states
def calc_dfa_all_states(maybe_initial, finals, transition):
    all_states = frozenset(q for q, _ in transition.keys())
    all_states |= set(transition.values())
    all_states |= set(maybe_initial)
    all_states |= finals
    return all_states

def transition_rules2ndfa_transition_finals(rules):
    '''formal rules, e.g. A = a B ; A = a C ; A = D ; D = ; ...

:: Iter (State, Maybe (Maybe Symbol, State)) -> (Map , Set State)
'''
    finals = set()
    dedges = []
    for state, maybe_jump in rules:
        if maybe_jump == nothing:
            finals.add(state)
        else:
            maybe_symbol, next_state = unjust(maybe_jump)
            key = state, maybe_symbol
            dedges.append((key, next_state))
    transition = group_pairs2dict(dedges)
    return transition, frozenset(finals)


    

