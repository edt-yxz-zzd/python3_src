#__all__:goto
r'''[[[
e ../../python3_src/seed/tiny_/std_mk_hashable_.py

seed.tiny_.std_mk_hashable_
py -m nn_ns.app.debug_cmd   seed.tiny_.std_mk_hashable_ -x
py -m nn_ns.app.doctest_cmd seed.tiny_.std_mk_hashable_:__doc__ -ht
py_adhoc_call   seed.tiny_.std_mk_hashable_   @f

>>> std_mk_hashable_([])
()
>>> std_mk_hashable_([{1:[]}])
(FrozenDict({1: ()}),)
>>> std_mk_hashable_([{1:[set()]}])
(FrozenDict({1: (frozenset(),)}),)
>>> std_mk_hashable_([bytearray(), '', b'', True, 1, ..., None, NotImplemented])
(b'', '', b'', True, 1, Ellipsis, None, NotImplemented)
>>> std_mk_hashable_([object, object()]) #doctest: +ELLIPSIS
(<class 'object'>, <object object at 0x...>)

#]]]'''
__all__ = r'''
std_mk_hashable_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from collections.abc import Mapping, Set, Sequence
#from collections import OrderedDict
from seed.types.FrozenDict import FrozenDict, mk_FrozenDict
from seed.tiny import mk_frozenset, mk_tuple
from seed.tiny_.check import check_type_is
___end_mark_of_excluded_global_names__0___ = ...

def std_mk_hashable_(x, /):
    return _recur_std(x)
_solid_types = (
{int
,float
,complex
,str
,bytes
,bool
,type(...)
,type(None)
,type(NotImplemented)
,frozenset
})
hash(NotImplemented)
_known_container_types = (
{list
,tuple
,set
,dict
,FrozenDict
})

def _recur_std(x, /):
    T = type(x)
    if T in _solid_types:
        return x
    if isinstance(x, Sequence):
        if T is bytearray:
            return bytes(x)
        return _recur_std__seq(x)
    if isinstance(x, Mapping):
        return _recur_std__mapping(x)
    if isinstance(x, Set):
        return mk_frozenset(x)
    hash(x)
        # ^TypeError
    return x
    raise TypeError(T)

def _recur_std__mapping(d, /):
    T = type(d)
    changed = not T is FrozenDict
    _d = {}
    for k, v in d.items():
        if k in _d:raise TypeError(T, k)
        _v = _recur_std(v)
        _d[k] = _v
        if not changed and not _v is v:
            changed = True
    r = mk_FrozenDict(_d) if changed else d
    check_type_is(FrozenDict, r)
    return r


def _recur_std__seq(ls, /):
    T = type(ls)
    changed = not T is tuple
    _ls = []
    for v in ls:
        _v = _recur_std(v)
        _ls.append(_v)
        if not changed and not _v is v:
            changed = True
    r = mk_tuple(_ls) if changed else ls
    check_type_is(tuple, r)
    return r










__all__
from seed.tiny_.std_mk_hashable_ import std_mk_hashable_
from seed.tiny_.std_mk_hashable_ import *
