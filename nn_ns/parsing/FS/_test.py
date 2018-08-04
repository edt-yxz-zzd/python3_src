

from .FA_transform import dfa_std_eq, ndfa2dfa
from .FA_FSM import SimpleNDFA2FSM, fsm2dfa
from .Regex import re2ndfa, test__make_re__Star_ab_b_abN, re2dfa
from .Regex import *

def test__fsm2dfa__impl(ndfa):
    dfa = ndfa2dfa(ndfa)
    assert dfa_std_eq(fsm2dfa(SimpleNDFA2FSM(ndfa)), dfa)


def iter_ndfas(rng, dot=None):
    exprs = test__make_re__Star_ab_b_abN(rng, dot=dot)
    return (re2ndfa(e) for e in exprs)



def test__fsm2dfa(rng, dot=None):
    for ndfa in iter_ndfas(rng, dot):
        test__fsm2dfa__impl(ndfa)


test__fsm2dfa(range(5), dot = 'abc')
null_re = () # ReConcat([])
dead_re = frozenset() # ReAlter([])
singleton_re0 = tuple('a')
singleton_re1 = frozenset('a')
c2_re = tuple('ab')
u2_re = frozenset('ab')
exprs = null_re, dead_re, singleton_re0, singleton_re1, c2_re, u2_re
for e in exprs:
    e = handed2re(e)
    #print(e)
    dfa = re2dfa(e)
    print(e, '\n\t', dfa)







