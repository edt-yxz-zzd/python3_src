#__all__:goto
r'''[[[
e ../../python3_src/seed/types/FrozenOrderedSet.py

seed.types.FrozenOrderedSet
py -m nn_ns.app.debug_cmd   seed.types.FrozenOrderedSet -x
py -m nn_ns.app.doctest_cmd seed.types.FrozenOrderedSet:__doc__ -ht


>>> s = FrozenOrderedSet(range(300, 305))
>>> s
FrozenOrderedSet((300, 301, 302, 303, 304))
>>> s.index(303)
3
>>> s.seq
(300, 301, 302, 303, 304)
>>> s.set_view
odict_keys([300, 301, 302, 303, 304])
>>> 303 in s
True
>>> [*iter(s)]
[300, 301, 302, 303, 304]
>>> [*reversed(s)]
[304, 303, 302, 301, 300]
>>> bool(s)
True
>>> len(s)
5
>>> {s, FrozenOrderedSet(range(300, 305))}
{FrozenOrderedSet((300, 301, 302, 303, 304))}
>>> s == {*range(300, 305)} #True
False
>>> s.set_view == {*range(300, 305)}
True



>>> d = FrozenOrderedDict((j+700, j+900) for j in range(5))
>>> d
FrozenOrderedDict(((700, 900), (701, 901), (702, 902), (703, 903), (704, 904)))
>>> d.index(703)
3
>>> d.seq
((700, 900), (701, 901), (702, 902), (703, 903), (704, 904))
>>> d.map_view
mappingproxy(OrderedDict([(700, 900), (701, 901), (702, 902), (703, 903), (704, 904)]))
>>> 703 in d
True
>>> [*iter(d)]
[700, 701, 702, 703, 704]
>>> [*reversed(d)]
[704, 703, 702, 701, 700]
>>> d.keys()
odict_keys([700, 701, 702, 703, 704])
>>> d.items()
odict_items([(700, 900), (701, 901), (702, 902), (703, 903), (704, 904)])
>>> d.values()
odict_values([900, 901, 902, 903, 904])
>>> bool(d)
True
>>> len(d)
5
>>> {d, FrozenOrderedDict((j+700, j+900) for j in range(5))}
{FrozenOrderedDict(((700, 900), (701, 901), (702, 902), (703, 903), (704, 904)))}
>>> d == dict((j+700, j+900) for j in range(5)) #True
False
>>> d == OrderedDict((j+700, j+900) for j in range(5)) #True
False
>>> d.map_view == OrderedDict((j+700, j+900) for j in range(5))
True
>>> d.map_view == dict((j+700, j+900) for j in range(5))
True

#]]]'''
__all__ = r'''
FrozenOrderedSet
FrozenOrderedDict
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from collections import OrderedDict
from collections.abc import Set, Mapping
from seed.tiny import MapView, mk_tuple, mk_pair #mk_frozenset
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

class FrozenOrderedSet(Set):
    def __init__(sf, xs, /):
        sf._j2x = ls = mk_tuple(xs)
        #sf._set = s = mk_frozenset(ls)
        #if not len(ls) == len(s):raise ValueError('duplicated', ls)
        #sf._x2j = d = {x:j for j, x in enumerate(ls)}
        sf._x2j = d = OrderedDict((x,j) for j, x in enumerate(ls))#see:.set_view
        if not len(ls) == len(d):raise ValueError('duplicated', ls)
    def __repr__(sf, /):
        return repr_helper(sf, sf._j2x)
    def index(sf, x, /):
        'x -> j'
        return sf._x2j[x]
    @property
    def seq(sf, /):
        '-> [x]'
        return sf._j2x
    @property
    def set_view(sf, /):
        '-> ordered-view-{x} #for:__eq__<Set>()'
        return sf._x2j.keys()
    def __contains__(sf, x, /):
        return x in sf._x2j
    def __iter__(sf, /):
        return iter(sf._j2x)
    def __reversed__(sf, /):
        return reversed(sf._j2x)
    def __len__(sf, /):
        return len(sf._j2x)
    def __bool__(sf, /):
        return bool(sf._j2x)
    def __hash__(sf, /):
        return hash((id(type(sf)), sf._j2x))
    def __eq__(sf, ot, /):
        if ot is sf:
            return True
        if not type(ot) is type(sf):
            #return sf._j2x == ot#ordered
            #see:sf.set_view
            return NotImplemented
        return sf._j2x == ot._j2x
FrozenOrderedSet([])

class FrozenOrderedDict(Mapping):
    def __init__(sf, pairs, /):
        sf._j2kv = ls = mk_tuple(map(mk_pair, pairs))
        sf._k2j = d = {k:j for j, (k,v) in enumerate(ls)}
        sf._k2v = OrderedDict(ls)
            #ordered
        if not len(ls) == len(d):raise ValueError('duplicated', ls)
    def index(sf, k, /):
        'k -> j'
        return sf._k2j[k]
    def __repr__(sf, /):
        return repr_helper(sf, sf._j2kv)
    @property
    def seq(sf, /):
        '-> [(k,v)]'
        return sf._j2kv
    @property
    def map_view(sf, /):
        '-> ordered-view-{k:v} #for:__eq__<Mapping>()'
        return MapView(sf._k2v)
    def __getitem__(sf, k, /):
        'k -> v'
        return sf._k2v[k]
    def __contains__(sf, k, /):
        return k in sf._k2v
    def __iter__(sf, /):
        return iter(sf._k2v)#ordered
    def __reversed__(sf, /):
        return reversed(sf._k2v)#ordered
    def keys(sf, /):
        return sf._k2v.keys()#ordered
    def items(sf, /):
        return sf._k2v.items()#ordered
    def values(sf, /):
        return sf._k2v.values()#ordered

    def __len__(sf, /):
        return len(sf._j2kv)
    def __bool__(sf, /):
        return bool(sf._j2kv)
    def __hash__(sf, /):
        return hash((id(type(sf)), sf._j2kv))
    def __eq__(sf, ot, /):
        if ot is sf:
            return True
        if not type(ot) is type(sf):
            #return sf._k2v == ot#ordered
            #see:sf.map_view
            return NotImplemented
        return sf._j2kv == ot._j2kv

FrozenOrderedDict([])

__all__
from seed.types.FrozenOrderedSet import FrozenOrderedSet, FrozenOrderedDict
from seed.types.FrozenOrderedSet import *
