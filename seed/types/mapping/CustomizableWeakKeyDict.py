#__all__:goto
r'''[[[
e ../../python3_src/seed/types/mapping/CustomizableWeakKeyDict.py

seed.types.mapping.CustomizableWeakKeyDict
py -m nn_ns.app.debug_cmd   seed.types.mapping.CustomizableWeakKeyDict -x
py -m nn_ns.app.doctest_cmd seed.types.mapping.CustomizableWeakKeyDict:__doc__ -ht


[[
impl WeakKeyDict by WeakValueDict
]]


>>> d = CustomizableWeakKeyDict(id)
>>> d
CustomizableWeakKeyDict(<built-in function id>, {})
>>> bool(d)
False
>>> len(d)
0
>>> [*d]
[]


>>> wk = set()
>>> v = []
>>> d[wk] = v
>>> d #doctest: +ELLIPSIS
CustomizableWeakKeyDict(<built-in function id>, {Pair4hash_fst(..., []): set()})
>>> bool(d)
True
>>> len(d)
1
>>> [*d]
[set()]
>>> [*d][0] is wk
True

>>> wk in d
True
>>> d[wk] is v
True
>>> hk = id(wk)
>>> slice(None, hk, None) in d
True
>>> d[:hk] is v
True
>>> del wk
>>> d[:hk] #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
KeyError: Pair4hash_fst__fetch(..., None)
>>> d
CustomizableWeakKeyDict(<built-in function id>, {})
>>> bool(d)
False
>>> len(d)
0
>>> [*d]
[]



#]]]'''
__all__ = r'''
Pair4hash_fst
    Pair4hash_fst__fetch
ICustomizableWeakKeyDict
    CustomizableWeakKeyDict
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from weakref import ref as wref_, WeakKeyDictionary as WkeyD, WeakValueDictionary as WvalD

from collections.abc import MutableMapping

from seed.tiny_.check import check_type_is, check_type_le, check_non_ABC, check_callable
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
from seed.tiny_._Base4repr import _Base4repr
___end_mark_of_excluded_global_names__0___ = ...

class Pair4hash_fst:
    '(hk, v)/(hashable, hash_irrelevant)'
    _to_fetch_ = False
    def __init__(sf, hk, v, /):
        sf._hk = hk
        sf._h = hash(hk)
        sf._v = v #hash_irrelevant
    def __repr__(sf, /):
        return repr_helper(sf, sf._hk, sf._v)
    @property
    def key(sf, /):
        return sf._hk
    @property
    def value(sf, /):
        return sf._v
    def __hash__(sf, /):
        return sf._h
    def __eq__(sf, ot, /):
        if sf is ot:
            #_to_fetch_ take no effect
            return True
        if not type(ot) in _Ts4eq:
            return NotImplemented
        #if not isinstance(ot, Pair4hash_fst):
        #    raise TypeError(type(sf), type(ot))
        #if not type(sf) is type(ot):
        #    return NotImplemented
        #    raise TypeError(type(sf), type(ot))
        b = sf._hk is ot._hk or (sf._h == ot._h and sf._hk == ot._hk)
        x, y = sf._to_fetch_, ot._to_fetch_
        if x is y:
            #_to_fetch_ take no effect
            pass
        elif x:
            #fetch
            sf._v = ot._v
        elif y:
            #fetch
            ot._v = sf._v
        return b
class Pair4hash_fst__fetch(Pair4hash_fst):
    'fetch-value of Pair4hash_fst via __eq__'
    #@override
    _to_fetch_ = True
_Ts4eq = (Pair4hash_fst, Pair4hash_fst__fetch)


def _hk5sf_wk_or_sl_hk(sf, wk_or_sl_hk, /):
    if type(wk_or_sl_hk) is slice:
        sl_hk = wk_or_sl_hk
        match sl_hk:
            case slice(start=None, stop=hk, step=None):
                return hk
            case _:
                raise KeyError(sl_hk)
    wk = wk_or_sl_hk
    w = wref_(wk)
    hk = sf._weakable_key2hashable_key_(wk)
    return hk
def _ex_wk2pk__to_get(sf, wk_or_sl_hk, /):
    hk = _hk5sf_wk_or_sl_hk(sf, wk_or_sl_hk)
    return Pair4hash_fst__fetch(hk, None)
def _wk2pk__to_set(sf, wk, v, /):
    #hk = _hk5sf_wk_or_sl_hk(sf, wk)
    w = wref_(wk)
    hk = sf._weakable_key2hashable_key_(wk)
    return Pair4hash_fst(hk, v)
class ICustomizableWeakKeyDict(MutableMapping, ABC):
    '[d[wk] === d[:d._weakable_key2hashable_key_(wk)]]'
    __slots__ = ()
    @abstractmethod
    def _weakable_key2hashable_key_(sf, wk, /):
        'wk/weakable -> hk/hashable'
    @property
    @abstractmethod
    def _weak_value_dict_(sf, /):
        '-> weak_value_dict/WeakValueDictionary{pk/Pair4hash_fst<hk<wk>,v>:wk}'
    def _key2hashable_key_(sf, wk_or_sl_hk, /):
        'wk_or_sl_hk/(wk/weakable|slice(-,hk,-)) -> hk/hashable'
        hk = _hk5sf_wk_or_sl_hk(sf, wk_or_sl_hk)
        return hk
    @override
    def __len__(sf, /):
        d = sf._weak_value_dict_
        return len(d)
    @override
    def __iter__(sf, /):
        d = sf._weak_value_dict_
        return iter(d.values())
    @override
    def __contains__(sf, wk_or_sl_hk, /):
        'wk_or_sl_hk/(wk/weakable|slice(-,hk,-)) -> v|^KeyError'
        gk = _ex_wk2pk__to_get(sf, wk_or_sl_hk)
        d = sf._weak_value_dict_
        return gk in d


    @override
    def __getitem__(sf, wk_or_sl_hk, /):
        'wk_or_sl_hk/(wk/weakable|slice(-,hk,-)) -> v|^KeyError'
        gk = _ex_wk2pk__to_get(sf, wk_or_sl_hk)
        d = sf._weak_value_dict_
        d[gk]
        return gk.value

    @override
    def __setitem__(sf, wk, v, /):
        'wk/weakable -> v -> None'
        sk = _wk2pk__to_set(sf, wk, v)
        d = sf._weak_value_dict_
        d[sk] = wk
    @override
    def __delitem__(sf, wk_or_sl_hk, /):
        'wk_or_sl_hk/(wk/weakable|slice(-,hk,-)) -> None|^KeyError'
        gk = _ex_wk2pk__to_get(sf, wk_or_sl_hk)
        d = sf._weak_value_dict_
        del d[gk]
class CustomizableWeakKeyDict(ICustomizableWeakKeyDict):
    ___no_slots_ok___ = True
    def __init__(sf, _weakable_key2hashable_key_, /, *args4dict):
        check_callable(_weakable_key2hashable_key_)
        sf._f = _weakable_key2hashable_key_
        sf._d = WvalD(*args4dict)
    def __repr__(sf, /):
        return repr_helper(sf, sf._f, {**sf._d})
    @property
    @override
    def _weakable_key2hashable_key_(sf, /):
        '-> (wk/weakable -> hk/hashable)'
        'wk/weakable -> hk/hashable'
        return sf._f
    @property
    @override
    def _weak_value_dict_(sf, /):
        '-> weak_value_dict/WeakValueDictionary{pk/Pair4hash_fst<hk<wk>,v>:wk}'
        return sf._d
check_non_ABC(CustomizableWeakKeyDict)
CustomizableWeakKeyDict(id)














__all__
from seed.types.mapping.CustomizableWeakKeyDict import Pair4hash_fst, Pair4hash_fst__fetch
from seed.types.mapping.CustomizableWeakKeyDict import ICustomizableWeakKeyDict

from seed.types.mapping.CustomizableWeakKeyDict import CustomizableWeakKeyDict
from seed.types.mapping.CustomizableWeakKeyDict import *
