
'''
repeat_FA_0_1_to_DFA

repeat_NFA_1_inf_to_NFA

repeat_NFA_ge2_inf_to_DFA
repeat_NFA_ge1_ge2_to_DFA
repeat_NFA_ge1_ge2inf_to_DFA
repeat_NFA_min_ge2inf_to_DFA

repeat_DFA_min_lt2_to_DFA
repeat_DFA_min_max_to_DFA
'''

from .DFA import DFA
from .NFA import NFA
from .ParallelFAs2DFA import OR_FAs
from .SerialNFAs2DFA import CONCAT_NFAs_FinalLast, CONCAT_NFAs_FinalFromIdx

def repeat_FA_0_1_to_DFA(fa):
    dfa = OR_FAs([DFA.regex_null(), fa])

    assert isinstance(dfa, DFA)
    return dfa

##def repeat_FA_0_1_to_NFA(fa):
##    dfa = repeat_FA_0_1_to_DFA(fa)
##    nfa = NFA.from_DFA(dfa)
##    return nfa

    # wrong implement:
    '''we "have to" add a new initial state.
'''
    gotos, fail, q0, is_final, _not_ = nfa.get_args()
    N = nfa.nstate()
    nosymbol_moves = {N:q0}
    for xq0 in q0: break
    else: raise ValueError('q0 cannot be empty')

    gotos += type(gotos)([gotos[xq0]])
    fail += type(fail)([fail[xq0]])
    q0 = frozenset({N})
    is_final += type(is_final)([True ^ _not_])
    # bug: if _not_ == True,
    #      once q == {N, x}, is_final(q) may not be True!!

    nfa = NFA(gotos, fail, q0, is_final, _not_)
    nfa = nfa.add_nosymbol_moves(nosymbol_moves)
    return nfa






def repeat_NFA_1_inf_to_NFA(nfa):
    assert isinstance(nfa, NFA)
    fs = nfa.get_finals()
    q0 = nfa.get_initial()
    nosymbol_moves = {s:q0 for s in fs}
    nfa = nfa.add_nosymbol_moves(nosymbol_moves)

    assert isinstance(nfa, NFA)
    return nfa



def repeat_NFA_ge2_inf_to_DFA(nfa, n):
    assert isinstance(nfa, NFA)
    assert n >= 2
    nfas = [nfa] * (n-1)
    tail = repeat_NFA_1_inf_to_NFA(nfa)
    nfas.append(tail)

    assert len(nfas) >= 2
    dfa = CONCAT_NFAs_FinalLast(nfas)

    assert isinstance(dfa, DFA)
    return dfa

def repeat_NFA_ge1_ge2_to_DFA(nfa, min, max):
    assert isinstance(nfa, NFA)
    assert min >= 1
    assert max >= 2
    assert max >= min
    
    nfas = [nfa] * max
    dfa = CONCAT_NFAs_FinalFromIdx(nfas, min-1)

    assert isinstance(dfa, DFA)
    return dfa



def repeat_NFA_ge1_ge2inf_to_DFA(nfa, min, max = None):
    assert isinstance(nfa, NFA)
    assert min >= 1
    assert max == None or (max >= min and max >= 2)
    
    # max == inf
    if max == None: 
        if min == 1:
            nfa = repeat_NFA_1_inf_to_NFA(nfa)
            dfa = nfa.to_DFA()
        else:
            dfa = repeat_NFA_ge2_inf_to_DFA(nfa, min)

    # max >= 2
    else:
        assert max >= 2
        dfa = repeat_NFA_ge1_ge2_to_DFA(nfa, min, max)


    assert isinstance(dfa, DFA)
    return dfa

def repeat_NFA_min_ge2inf_to_DFA(nfa, min, max = None):
    assert isinstance(nfa, NFA)
    assert min >= 0
    assert max == None or (max >= min and max >= 2)

    
    n = min
    if n == 0: n = 1
    dfa = repeat_NFA_ge1_ge2inf_to_DFA(nfa, n, max)

    if min == 0:
        dfa = repeat_FA_0_1_to_DFA(dfa)

    assert isinstance(dfa, DFA)
    return dfa





def repeat_DFA_min_lt2_to_DFA(dfa, min, max):
    assert isinstance(dfa, DFA)
    assert 0 <= min <= max < 2
    if max == 0:
        return DFA.regex_null()

    assert max == 1
    if min == 1:
        dfa = dfa
    else:
        assert min == 0
        dfa = repeat_FA_0_1_to_DFA(dfa)

    assert isinstance(dfa, DFA)
    return dfa



def repeat_DFA_min_max_to_DFA(dfa, min, max = None):
    assert isinstance(dfa, DFA)
    assert min >= 0
    assert max == None or max >= min

    if max != None and max < 2:
        dfa = repeat_DFA_min_lt2_to_DFA(dfa, min, max)
    else:
        nfa = NFA.from_DFA(dfa)
        dfa = repeat_NFA_min_ge2inf_to_DFA(nfa, min, max)

    assert isinstance(dfa, DFA)
    return dfa


