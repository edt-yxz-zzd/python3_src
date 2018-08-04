from .InfoID_MyLL1L import *
import re


def _toCount(min=None, max=None):
    inf = float('inf')
    if max == None:
        if min == None:
            return (1, 1)
        elif isinstance(min, str):
            assert min in '?*+'
            d = {'?': (0, 1), '*': (0, inf), '+': (1, inf), }
            return d[min]
        max = inf

    
    assert 0 <= min
    assert isinstance(min, int)
    
    return (min, max)

def toCount(min = None, max = None):
    if isinstance(min, tuple):
        assert max == None
        return _toCount(*min)
    else:
        return _toCount(min, max)
    
def toInfoIDItem(ID, refID, min = (), max = None, *, name = None):
    min, max = toCount(min, max)
    return InfoIDItem(ID, refID, min, max, key = name)
def toInfoIDList(ID, idcount_name_ls):
    #print(idcount_name_ls)
    items = [toInfoIDItem(i, *idcount, name=name) for i, (idcount, name) in enumerate(idcount_name_ls)]
    return InfoIDList(ID, children = items)

def toInfoIDBlock(ID, children):
    return InfoIDBlock(ID, children = children)

def toIDList(ID, *idcount_name_ls):return toInfoIDList(ID, idcount_name_ls)
def toIDBlock(ID, *children):return toInfoIDBlock(ID, children)
def toIDToken(ID, token_type):
    assert re.match('t["\']', token_type)
    token_type = eval(token_type[1:])
    assert isinstance(token_type, str)
    
    return InfoIDToken(token_type, ID)
