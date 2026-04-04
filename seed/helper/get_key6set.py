#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/get_key6set.py
e ../../python3_src/seed/mapping_tools/get_key6set.py
from seed.mapping_tools.get_key6set import get_keys6set_, get_key6set_

seed.helper.get_key6set
py -m nn_ns.app.debug_cmd   seed.helper.get_key6set -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.get_key6set:__doc__ -ht # -ff -df
#######

[[
which key in set/mapping/WeakSet/WeakKeyDictionary?

]]

[[
see:Pair4hash_fst__fetch
view ../../python3_src/seed/types/mapping/CustomizableWeakKeyDict.py
from seed.types.mapping.CustomizableWeakKeyDict import Pair4hash_fst, Pair4hash_fst__fetch
]]


'#'; __doc__ = r'#'
>>> get_keys6set_({True, False}, 0)
(False,)
>>> get_keys6set_({True, False}, 1)
(True,)
>>> get_keys6set_({True, False}, 2)
()

>>> get_tmay_key6set_({True, False}, 0)
(False,)
>>> get_tmay_key6set_({True, False}, 1)
(True,)
>>> get_tmay_key6set_({True, False}, 2)
()

>>> get_key6set_({True, False}, 0)
False
>>> get_key6set_({True, False}, 1)
True
>>> get_key6set_({True, False}, 2)
Traceback (most recent call last):
    ...
KeyError: 2


py_adhoc_call   seed.helper.get_key6set   @f
]]]'''#'''
__all__ = r'''
get_keys6set_
    get_tmay_key6set_
        get_key6set_
TooManyEqvKeysError


Key7fetch_another_eqv_key
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.types.CachedProperty import CachedProperty
from seed.tiny_.types5py import mk_MapView
___end_mark_of_excluded_global_names__0___ = ...

_ordinal = 0
def _mk_new_ordinal():
    global _ordinal
    _ordinal += 1
    return _ordinal
class Key7fetch_another_eqv_key:
    def __init__(sf, k, id2k=None, /):
        if None is id2k:
            id2k = {}

        sf._id2k = id2k
        sf._k = k
        sf._h = hash(k)
        sf._j = _mk_new_ordinal()
        sf._vw = mk_MapView(id2k)
    @CachedProperty
    def id2eqv_key(sf, /):
        return sf._vw
    def __hash__(sf, /):
        return sf._h
    def __eq__(sf, ot, /):
        if id(ot) in sf._id2k:
            return True
        if sf is ot:
            #sf._id2k[id(ot)] = ot
            return True
        b = isinstance(ot, __class__)
        if b:
            if id(sf) in ot._id2k:
                return True
        try:
            h = hash(ot)
        except TypeError:
            return NotImplemented
        if not h == hash(sf):
            return False

        if b:
            assert not sf._j == ot._j
            if not sf._k in [ot._k]:
                return False
            if sf._j > ot._j:
                sf._id2k[id(ot)] = ot
            else:
                ot._id2k[id(sf)] = sf
            return True

        if not sf._k in [ot]:
            return False
        sf._id2k[id(ot)] = ot
        return True

class TooManyEqvKeysError(Exception):pass
def get_tmay_key6set_(set_or_mapping, k, /):
    '{k} -> k -> (tmay k)|^TooManyEqvKeysError'
    ks = get_keys6set_(set_or_mapping, k)
    if not len(ks) <= 1:raise TooManyEqvKeysError(set_or_mapping, k, ks)
    tmay_k = ks
    return tmay_k
def get_key6set_(set_or_mapping, k, /):
    '{k} -> k -> k|^KeyError|^TooManyEqvKeysError'
    tmay_k = get_tmay_key6set_(set_or_mapping, k)
        # ^TooManyEqvKeysError
    match tmay_k:
        case [k]:
            return k
        case []:
            raise KeyError(k)
    raise 000
def get_keys6set_(set_or_mapping, k, /):
    '{k} -> k -> [k]'
    k7get = Key7fetch_another_eqv_key(k)
    b = k7get in set_or_mapping
    777;ks = tuple(k7get.id2eqv_key.values())
    if b:
        if not ks:raise Exception(set_or_mapping, k)
    else:
        if ks:raise Exception(set_or_mapping, k, ks)
    assert b is bool(ks)
    return ks

__all__
from seed.helper.get_key6set import get_keys6set_, get_tmay_key6set_, get_key6set_, TooManyEqvKeysError
from seed.helper.get_key6set import *
