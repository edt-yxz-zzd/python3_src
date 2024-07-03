
#e ../../python3_src/seed/iters/group_by.py
#view ../../python3_src/seed/seq_tools/sorted_via_lt_.py
__all__ = '''
    group_by
    group_by_eq

    xs_to_k2vs_
        xs_to_vss_
            partition_xs_by_bool_

    KeyMkr5eq
    Key4group_by
    '''.split()

from itertools import groupby
from operator import __eq__ as _eq
from seed.tiny import echo, ifNone
from seed.iters.group_by_eq import group_by_eq

class KeyMkr5eq:
    def __init__(sf, key, eq, /):
        sf.key = ifNone(key, echo)
        sf.eq = ifNone(eq, _eq)
    def __call__(sf, x, /):
        return Key4group_by(sf, x)
class Key4group_by:
    def __init__(sf, key_mkr, x, /):
        assert type(key_mkr) is KeyMkr5eq
        y = key_mkr.key(x)
        sf.key_mkr = key_mkr
        sf.y = y
    def __eq__(sf, ot, /):
        if not type(ot) is type(sf): raise TypeError
        if not ot.key_mkr is sf.key_mkr: raise TypeError
        eq = sf.key_mkr.eq
        return eq(sf.y, ot.y)
    def __ne__(sf, ot, /):
        return not sf == ot

def key_mkr5eq_(*, key=None, __eq__=None):
    key_mkr = KeyMkr5eq(key, __eq__)
    return key_mkr

def group_by(iterable, /, *, key=None, container=tuple, __eq__=None):
    '!!!seed.iters.group_by_eq!!!'
    if not (__eq__ is None or __eq__ is _eq):
        key = key_mkr5eq_(key=key, __eq__=__eq__)
    for k, g in groupby(iterable, key=key):
        yield k, container(g)

from seed.tiny_.group__partition import partition_xs_by_bool_, xs_to_vss_, xs_to_k2vs_

from seed.iters.group_by import group_by
from seed.iters.group_by import group_by_eq
from seed.iters.group_by import xs_to_k2vs_, xs_to_vss_, partition_xs_by_bool_
from seed.iters.group_by import *

