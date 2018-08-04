
__all__ = '''
    mkSimpleNFA
    mkSimpleNFA_ex
    '''.split()

def mkSimpleNFA_ex(NFAs, regex:'ISimpleRE', make_new_astate:'MakeNewAState'
        , may_initial_astate, may_final_astate):
    # -> ISimpleNFA
    # NFAs - a namespace offer constructors; see: ISimpleRE
    assert isinstance(regex, ISimpleRE)
    return regex._mkSimpleNFA_(NFAs, make_new_astate
                                , may_initial_astate, may_final_astate)

def mkSimpleNFA(regex:'ISimpleRE'):
    # -> ISimpleNFA
    return mkSimpleNFA_ex(global_NFAs, regex, MakeNewAState(), None, None)

############ function first
from .ISimpleRE import ISimpleRE
from .ISimpleNFA import ISimpleNFA, MakeNewAState
from . import SimpleNFA as global_NFAs



'''
from . import ISimpleRE as out
out.mkSimpleNFA = mkSimpleNFA
del out
'''

