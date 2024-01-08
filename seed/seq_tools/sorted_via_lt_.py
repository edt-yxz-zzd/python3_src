#__all__:goto
r'''[[[
e ../../python3_src/seed/seq_tools/sorted_via_lt_.py


seed.seq_tools.sorted_via_lt_
py -m nn_ns.app.debug_cmd   seed.seq_tools.sorted_via_lt_ -x
py -m nn_ns.app.doctest_cmd seed.seq_tools.sorted_via_lt_:__doc__ -ff -v
py_adhoc_call   seed.seq_tools.sorted_via_lt_   @f

>>> sorted_via_lt_([3, 1, 2])
[1, 2, 3]
>>> sorted_via_lt_([3, 1, 2], key=int.__neg__)
[3, 2, 1]
>>> sorted_via_lt_([3, 1, 2], key=int.__neg__, __lt__=int.__gt__)
[1, 2, 3]
>>> sorted_via_lt_([3, 1, 2], __lt__=int.__gt__)
[3, 2, 1]

#]]]'''
__all__ = r'''
    KeyMkr5lt
    Key4sorted_via_lt_
    key_mkr5lt_
    sorted_via_lt_
'''.split()#'''
__all__
from seed.tiny import echo
import operator #__lt__

class KeyMkr5lt:
    def __init__(sf, key, lt, /):
        if key is None:
            key = echo
        if lt is None:
            lt = operator.__lt__
        sf.key = key
        sf.lt = lt
    def __call__(sf, x, /):
        return Key4sorted_via_lt_(sf, x)
class Key4sorted_via_lt_:
    def __init__(sf, key_mkr, x, /):
        assert type(key_mkr) is KeyMkr5lt
        y = key_mkr.key(x)
        sf.key_mkr = key_mkr
        sf.y = y
    @classmethod
    def _1_lt_1_(cls, sf, ot, /):
        if not type(ot) is type(sf): raise TypeError
        if not ot.key_mkr is sf.key_mkr: raise TypeError
        lt = sf.key_mkr.lt
        return lt(sf.y, ot.y)
    def __lt__(sf, ot, /):
        return type(sf)._1_lt_1_(sf, ot)
    def __gt__(sf, ot, /):
        return type(sf)._1_lt_1_(ot, sf)
        return ot < sf
    def __le__(sf, ot, /):
        return not (sf > ot)
    def __ge__(sf, ot, /):
        return not (sf < ot)

def key_mkr5lt_(*, key=None, __lt__=None):
    key_mkr = KeyMkr5lt(key, __lt__)
    return key_mkr
def sorted_via_lt_(xs, /, *, key=None, __lt__=None):
    key_mkr = key_mkr5lt_(key=key, __lt__=__lt__)
    sorted_xs = sorted(xs, key=key_mkr)
    return sorted_xs
__all__


from seed.seq_tools.sorted_via_lt_ import sorted_via_lt_
from seed.seq_tools.sorted_via_lt_ import KeyMkr5lt, Key4sorted_via_lt_, key_mkr5lt_, sorted_via_lt_
from seed.seq_tools.sorted_via_lt_ import *
