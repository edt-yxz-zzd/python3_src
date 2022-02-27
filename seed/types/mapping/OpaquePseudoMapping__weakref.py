#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
seed.types.mapping.OpaquePseudoMapping__weakref
py -m    seed.types.mapping.OpaquePseudoMapping__weakref
py -m nn_ns.app.debug_cmd   seed.types.mapping.OpaquePseudoMapping__weakref

used in seed.types.OpaqueInstanceStorage::IProtocol4OpaqueStorage
    view ../../python3_src/seed/types/OpaqueInstanceStorage.py

##################################
##################################
##################################
from seed.types.mapping.Mapping__permanent__weakref import WeakableDict, mk_callback4auto_discard_WeakableDict_key

from seed.types.mapping.Mapping__permanent__weakref import PermanentKeyRefDict, WeakKeyRefDict, PermanentKeyRefSet, WeakKeyRefSet

from seed.types.mapping.Mapping__permanent__weakref import PRefDict, WRefDict, PRefSet, WRefSet, PermanentKeyRefDict, WeakKeyRefDict, PermanentKeyRefSet, WeakKeyRefSet

from seed.types.mapping.Mapping__permanent__weakref import PValDict, WValDict, PValSet, WValSet, PermanentKeyValueDict, WeakKeyValueDict, PermanentKeyValueSet, WeakKeyValueSet


from seed.types.mapping.Mapping__permanent__weakref import WeakKeyDictionary4AddrAsHash
##################################
##################################
##################################


##################################
##################################
##################################
from seed.types.mapping.OpaquePseudoMapping__weakref import MutableOpaquePseudoMapping__init_new_key_only__WeakKeyDictionary4AddrAsHash

from seed.types.mapping.OpaquePseudoMapping__weakref import IMutableOpaquePseudoMapping__init_new_key_only__WeakKeyPathDictionary, IMutableOpaquePseudoMapping__init_new_key_only__WeakKeyPathDictionary__init, MutableOpaquePseudoMapping__init_new_key_only__WeakRefDictionary, MutableOpaquePseudoMapping__init_new_key_only__Value_Ref_Weak_KeysTripleDictionary
##################################
##################################
##################################


#[[[doc_sections:begin
#doctest_examples:goto
#wwwzzz:goto

#[[[doctest_examples:begin
>>> pd = PermanentKeyRefDict()
>>> ls1 = []
>>> ls2 = []
>>> ls1 in pd
False
>>> len(pd)
0
>>> bool(pd)
False
>>> pd[ls1] = 1
>>> len(pd)
1
>>> bool(pd)
True
>>> ls1 in pd
True
>>> ls2 in pd
False
>>> pd[ls1] = 2
>>> [*pd.items()]
[([], 2)]
>>> 1 # nonlocal "_" hold ls1
1
>>> len(pd)
1
>>> pd[ls2] = 3
>>> len(pd)
2
>>> pd[ls2]
3
>>> pd[ls1]
2
>>> del pd[ls1]
>>> [*pd.items()]
[([], 3)]
>>> 1 # nonlocal "_" hold ls2
1
>>> ls1.append(4)
>>> ls2.append(5)
>>> [*pd.items()]
[([5], 3)]
>>> 1 # nonlocal "_" hold ls2
1
>>> del ls1
>>> [*pd.items()]
[([5], 3)]
>>> 1 # nonlocal "_" hold ls2
1
>>> del ls2
>>> [*pd.items()]
[([5], 3)]
>>> 1 # nonlocal "_" hold ls2
1
>>> del pd




>>> wd = WeakKeyRefDict()
>>> [] in wd
Traceback (most recent call last):
    ...
TypeError: cannot create weak reference to 'list' object
>>> s1 = set()
>>> s2 = set()
>>> s1 in wd
False
>>> len(wd)
0
>>> bool(wd)
False
>>> wd[s1] = 1
>>> len(wd)
1
>>> bool(wd)
True
>>> s1 in wd
True
>>> s2 in wd
False
>>> wd[s1] = 2
>>> [*wd.items()]
[(set(), 2)]
>>> 1 # nonlocal "_" hold s1
1
>>> len(wd)
1
>>> wd[s2] = 3
>>> len(wd)
2
>>> wd[s2]
3
>>> wd[s1]
2
>>> del s2
>>> len(wd)
1
>>> s2 = set()
>>> wd[s2] = 3
>>> len(wd)
2
>>> del wd[s1]
>>> [*wd.items()]
[(set(), 3)]
>>> 1 # nonlocal "_" hold s2
1
>>> s1.add(4)
>>> s2.add(5)
>>> [*wd.items()]
[({5}, 3)]
>>> 1 # nonlocal "_" hold s2
1
>>> del s1
>>> [*wd.items()]
[({5}, 3)]
>>> 1 # nonlocal "_" hold s2
1
>>> del s2
>>> [*wd.items()]
[]
>>> del wd




#]]]doctest_examples:end

#[[[wwwzzz:begin
#]]]wwwzzz:end
#]]]doc_sections:end


#'''
#]]]__doc__:end

#################################
#HHHHH
__all__ = '''
    WeakableDict
        mk_callback4auto_discard_WeakableDict_key

    PRefDict
    WRefDict
    PRefSet
    WRefSet
        PermanentKeyRefDict
        WeakKeyRefDict
        PermanentKeyRefSet
        WeakKeyRefSet
    PValDict
    WValDict
    PValSet
    WValSet
        PermanentKeyValueDict
        WeakKeyValueDict
        PermanentKeyValueSet
        WeakKeyValueSet

    WeakKeyDictionary4AddrAsHash
        MutableOpaquePseudoMapping__init_new_key_only__WeakKeyDictionary4AddrAsHash

    IMutableOpaquePseudoMapping__init_new_key_only__WeakKeyPathDictionary
        IMutableOpaquePseudoMapping__init_new_key_only__WeakKeyPathDictionary__init
            MutableOpaquePseudoMapping__init_new_key_only__WeakRefDictionary
            MutableOpaquePseudoMapping__init_new_key_only__Value_Ref_Weak_KeysTripleDictionary
    '''.split()
#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.abc import ABC, abstractmethod, override#, not_implemented, ABCMeta
from seed.debug.expectError import expectError
from seed.tiny import fst, check_type_le
from seed.helper.check.checkers import check_type_is, check_tuple
import weakref
from weakref import WeakKeyDictionary as _
from weakref import WeakSet as _
from seed.abc.eq_by_id.BaseAddrAsHash import le_AddrAsHash#, BaseAddrAsHash
#from seed.abc.eq_by_id.AddrAsHash import AddrAsHash
from seed.abc.eq_by_id.AddrAsHashWrapper import AddrAsHashWrapper
from seed.types.mapping.OpaquePseudoMapping import IMutableOpaquePseudoMapping__init_new_key_only
from collections.abc import Mapping, MutableMapping, MutableSet, Hashable
from seed.tiny import check_Weakable, is_Weakable
from seed.tiny_.Hashable import check_Hashable__shallow#, is_Hashable__shallow, check_Hashable__deep, is_Hashable__deep


___end_mark_of_excluded_global_names__0___ = ...

#HHHHH
#[[[main_body_src_code:begin
#zzzwww:goto

#[[[zzzwww:begin


#print(dir(weakref.WeakKeyDictionary))
['_MutableMapping__marker', '__abstractmethods__', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', '_commit_removals', '_scrub_removals', 'clear', 'copy', 'get', 'items', 'keyrefs', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']





class WeakableDict(dict):
    __slots__ = '__weakref__'
check_Weakable(WeakableDict())
def mk_callback4auto_discard_WeakableDict_key(wd, k, /):
    check_type_is(WeakableDict, wd)
    wd = weakref.ref(wd)
    def callback(_, /):
        nonlocal wd
        #print('callback')
        #bug:wd = wd()
        #   wd become local var
        if wd is None:
            return
        d = wd()
        wd = None
            #prevent other weakref.callback()
        if d is not None:
            #print('callback: discard d[k]')
            d.pop(k, None)
                #may be removed
    return callback


class PermanentKeyRefDict(MutableMapping):
    r'''
    PermanentKeyRefDict<key, value>
        via dict<id(key), (key, value)>
        alternative impl:
            via dict<AddrAsHashWrapper(key), value>
    #'''
    __slots__ = '_d'
    __slots__ = ('_d', '__weakref__')
    @classmethod
    def check_key(cls, k, /):
        #no:check_Hashable__shallow(k)
        return
    def __init__(sf, /, *tmay_d):
        sf._d = {}
        sf.update(*tmay_d)
    @override
    def __getitem__(sf, k, /):
        sf.check_key(k)
        (_k, v) = sf._d[id(k)]
        assert k is _k
        return v
    @override
    def __delitem__(sf, k, /):
        sf.check_key(k)
        del sf._d[id(k)]
    @override
    def __setitem__(sf, k, v, /):
        sf.check_key(k)
        sf._d[id(k)] = (k, v)
    @override
    def __contains__(sf, k, /):
        sf.check_key(k)
        return id(k) in sf._d
    @override
    def __iter__(sf, /):
        return map(fst, sf._d.values())
    @override
    def __len__(sf, /):
        return len(sf._d)
    @override
    def __bool__(sf, /):
        return bool(sf._d)
    #'clear', 'copy', 'get', 'items', 'keyrefs', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
    @override
    def __ne__(sf, ot, /):
        return not (sf == ot)
    @override
    def __eq__(sf, ot, /):
        return mapping_eq4key_eq_by_id(sf, ot)
PermanentKeyRefDict()

def mapping_to_key_id2value(mapping, /):
    return {id(k):v for k, v in mapping.items()}
def mapping_eq4key_eq_by_id(sf, ot, /):
    #Mapping.__eq__: return dict(self.items()) == dict(other.items())
    #return len(ot) == len(sf) and Mapping.__eq__(sf, ot)
    f = mapping_to_key_id2value
    return len(ot) == len(sf) and f(ot) == f(sf)
def set_to_key_id_set(s, /):
    return {*map(id, s)}
def set_eq4key_eq_by_id(sf, ot, /):
    f = set_to_key_id_set
    return len(ot) == len(sf) and f(ot) == f(sf)

assert expectError(AttributeError, lambda:setattr(PermanentKeyRefDict(), 'x', 1))
    # view ~/../usr/lib/python3.8/abc.py
    # view ~/../usr/lib/python3.8/_collections_abc.py
    #Mapping ok: has '__slots__ = ()'
    #ABC ok: has '__slots__ = ()'
class PermanentKeyRefSet(MutableSet):
    r'''
    PermanentKeyRefSet<key>
        via dict<id(key), key>
        alternative impl:
            via set<AddrAsHashWrapper(key)>
    #'''
    __slots__ = '_s'
    __slots__ = ('_s', '__weakref__')
    @classmethod
    def check_key(cls, k, /):
        #no:check_Hashable__shallow(k)
        return
    def __init__(sf, ks=None, /):
        if ks is None:
            ks = ''
        sf._s = set(map(AddrAsHashWrapper, ks))

    @override
    def __contains__(sf, k, /):
        return AddrAsHashWrapper(k) in sf._s
    @override
    def __iter__(sf, /):
        return (wk.the_value_obj for wk in sf._s)
    @override
    def __len__(sf, /):
        return len(sf._s)
    @override
    def add(sf, k, /):
        sf._s.add(AddrAsHashWrapper(k))
    @override
    def discard(sf, k, /):
        sf._s.discard(AddrAsHashWrapper(k))
    @override
    def __ne__(sf, ot, /):
        return not (sf == ot)
    @override
    def __eq__(sf, ot, /):
        return set_eq4key_eq_by_id(sf, ot)



class WeakKeyRefSet(MutableSet):
    r'''
    WeakKeyRefSet<key>
        via dict<id(key), weakref.ref(key,callback)>
    #'''
    __slots__ = '_d'
    __slots__ = ('_d', '__weakref__')
    @classmethod
    def check_key(cls, k, /):
        check_Weakable(k)
        #no:check_Hashable__shallow(k)
        return
    def __init__(sf, ks=None, /):
        if ks is None:
            ks = ''
        sf._d = WeakableDict()
        #help(MutableSet)
        #sf.update(ks)
        for _ in map(sf.add, ks): pass

    @override
    def __contains__(sf, k, /):
        return id(k) in sf._d
    @override
    def __iter__(sf, /):
        return (wk() for wk in sf._d.values())
    @override
    def __len__(sf, /):
        return len(sf._d)
    @override
    def add(sf, k, /):
        if k not in sf:
            callback = mk_callback4auto_discard_WeakableDict_key(sf._d, id(k))
            wk = weakref.ref(k, callback)
            sf._d[id(k)] = wk
    @override
    def discard(sf, k, /):
        sf._d.pop(id(k))

    @override
    def __ne__(sf, ot, /):
        return not (sf == ot)
    @override
    def __eq__(sf, ot, /):
        return set_eq4key_eq_by_id(sf, ot)

class WeakKeyRefDict(MutableMapping):
    r'''
    WeakKeyRefDict<key, value>
        via dict<id(key), (weakref.ref(key, callback-to-discard-id(key)), value)>
    #'''
    __slots__ = '_d'
    __slots__ = ('_d', '__weakref__')
    @classmethod
    def check_key(cls, k, /):
        check_Weakable(k)
        return
    def __init__(sf, /, *tmay_d):
        sf._d = WeakableDict()
        sf.update(*tmay_d)
    @override
    def __getitem__(sf, k, /):
        sf.check_key(k)
        (w, v) = sf._d[id(k)]
        assert k is w()
        return v
    @override
    def __delitem__(sf, k, /):
        sf.check_key(k)
        del sf._d[id(k)]
    @override
    def __setitem__(sf, k, v, /):
        sf.check_key(k)
        m = sf._d.get(id(k))
        if m is None:
            callback = mk_callback4auto_discard_WeakableDict_key(sf._d, id(k))
            w = weakref.ref(k, callback)
        else:
            (w, _v) = m
        sf._d[id(k)] = (w, v)

    @override
    def __contains__(sf, k, /):
        sf.check_key(k)
        return id(k) in sf._d
    @override
    def __iter__(sf, /):
        return (w() for w, v in sf._d.values())
    @override
    def __len__(sf, /):
        return len(sf._d)
    @override
    def __bool__(sf, /):
        return bool(sf._d)
    #'clear', 'copy', 'get', 'items', 'keyrefs', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
    @override
    def __ne__(sf, ot, /):
        return not (sf == ot)
    @override
    def __eq__(sf, ot, /):
        return mapping_eq4key_eq_by_id(sf, ot)
WeakKeyRefDict()
def _t_WeakKeyRefDict():
    wd = WeakKeyRefDict()
    s = set()
    wd[s] = 1
    assert s in wd
    assert wd[s] == 1
    assert wd
    del s
    assert not wd
_t_WeakKeyRefDict()

PermanentKeyValueDict = WeakableDict #dict
PermanentKeyValueSet = WeakableSet = set
WeakKeyValueSet = weakref.WeakSet
WeakKeyValueDict = weakref.WeakKeyDictionary

PRefDict = PermanentKeyRefDict
PRefSet = PermanentKeyRefSet
WRefDict = WeakKeyRefDict
WRefSet = WeakKeyRefSet

PRefDict()
PRefSet() | PRefSet()
WRefDict()
WRefSet() | WRefSet()

PValDict = PermanentKeyValueDict
PValSet = PermanentKeyValueSet
WValDict = WeakKeyValueDict
WValSet = WeakKeyValueSet

PValDict()
PValSet() | PValSet()
WValDict()
WValSet() | WValSet()



check_Weakable(PermanentKeyRefDict())
check_Weakable(PermanentKeyRefSet())
check_Weakable(WeakKeyRefDict())
check_Weakable(WeakKeyRefSet())

check_Weakable(PermanentKeyValueDict())
check_Weakable(PermanentKeyValueSet())
check_Weakable(WeakKeyValueDict())
check_Weakable(WeakKeyValueSet())





#class WeakKeyDictionary4AddrAsHash(MutableMapping):
#class WeakKeyDictionary4AddrAsHash(weakref.WeakKeyDictionary):
#class WeakKeyDictionary4AddrAsHash(ABC):
class WeakKeyDictionary4AddrAsHash(MutableMapping):
    r'''
    key :: AddrAsHash&Weakable
    #'''
    __slots__ = '_d'
    __slots__ = ('_d', '__weakref__')
    @classmethod
    def check_key(cls, k, /):
        check_Weakable(k)
        if not le_AddrAsHash(type(k)):raise TypeError
    def __init__(sf, /):
        sf._d = weakref.WeakKeyDictionary()
    @override
    def __getitem__(sf, k, /):
        sf.check_key(k)
        return sf._d[k]
    @override
    def __delitem__(sf, k, /):
        sf.check_key(k)
        del sf._d[k]
    @override
    def __setitem__(sf, k, v, /):
        sf.check_key(k)
        sf._d[k] = v
    @override
    def __contains__(sf, k, /):
        sf.check_key(k)
        return k in sf._d
    @override
    def __iter__(sf, /):
        return iter(sf._d)
    @override
    def __len__(sf, /):
        return len(sf._d)
    @override
    def __bool__(sf, /):
        return bool(sf._d)
    #'clear', 'copy', 'get', 'items', 'keyrefs', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

#Mapping.register(WeakKeyDictionary4AddrAsHash)
#MutableMapping.register(WeakKeyDictionary4AddrAsHash)
WeakKeyDictionary4AddrAsHash()
#ABC=>assert expectError(AttributeError, lambda:WeakKeyDictionary4AddrAsHash.pop)
WeakKeyDictionary4AddrAsHash.pop

class MutableOpaquePseudoMapping__init_new_key_only__WeakKeyDictionary4AddrAsHash(IMutableOpaquePseudoMapping__init_new_key_only):
    r'''
    key :: AddrAsHash&Weakable
    #'''
    __slots__ = '_d'
    __slots__ = ('_d', '__weakref__')
    @classmethod
    def check_key(cls, k, /):
        check_Weakable(k)
        if not le_AddrAsHash(type(k)):raise TypeError
    def __init__(sf, /):
        sf._d = weakref.WeakKeyDictionary()
    @override
    def __getitem__(sf, k, /):
        sf.check_key(k)
        return sf._d[k]
    @override
    def __contains__(sf, k, /):
        sf.check_key(k)
        return k in sf._d
    @override
    def ___set_new_item___(sf, k, v, /):
        #sf.check_key(k)
        #   __setitem__ using __contains__ ==>> .check_key(k) called
        sf._d[k] = v

MutableOpaquePseudoMapping__init_new_key_only__WeakKeyDictionary4AddrAsHash()

class IMutableOpaquePseudoMapping__init_new_key_only__WeakKeyPathDictionary(IMutableOpaquePseudoMapping__init_new_key_only):
    r'''
    mapping<key_path4get, value>:
        __this_impl_mapping__ = valued_key_path -> (key_path4store, weakable_id2weak_ref_with_callback, value)
        # not: weakable_set :: WeakSet
        # not: id2weakable :: WeakValueDictionary
        # now: weakable_id2weak_ref_with_callback :: dict<id(weakable), weakref.ref(weakable, lambda _:__this_impl_mapping__.__delitem__(valued_key_path))>


    key_path4init/key_path4get -> valued_key_path <: Hashable
        #actual key
    key_path4get -> valued_key_path <: Hashable

    key_path4init -> Iter Weakable
        #auto remove if any weakable dead
    key_path4init -> key_path4store

    key_path4store -> unordered_iter_weakables__no_duplicates -> key_path4get -> bool
        #eqv for detect logic-error
        #   SHOULD_HOLD: eqv<key_path4store+(w() for w in weakable_id2weak_ref_with_callback.values()), key_path4get> <==> eq<valued_key_path, valued_key_path>

    init_vs_mix_vs_get:
        init:False
        mix:None
        get:True
    #'''
    __slots__ = ()
    @classmethod
    @abstractmethod
    def check_key_path(cls, key_path, /, init_vs_mix_vs_get):
        'key_path4init/key_path4get -> None'
        #def check_key_path(cls, key_path, /, init_vs_get:bool):
        #def check_key_path(cls, key_path, /):
        check_Weakable(key_path)
        return
    @classmethod
    @abstractmethod
    def key_path2valued_key_path(cls, key_path, /, init_vs_mix_vs_get):
        'key_path4init/key_path4get -> valued_key_path <: Hashable'
        #cls.check_key_path(key_path4get, init_vs_mix_vs_get=init_vs_mix_vs_get)
        return id(key_path)

    @classmethod
    @abstractmethod
    def key_path4init2key_path4get(cls, key_path4init, /):
        'key_path4init -> key_path4get'
        key_path4get = key_path4init
        return key_path4get
    @classmethod
    @abstractmethod
    def key_path4init2iter_weakables__duplicates_ok(cls, key_path4init, /):
        'key_path4init -> Iter Weakable'
        #check_Weakable(key_path4init)
        #cls.check_key_path(key_path4init, init_vs_mix_vs_get=False)
        yield key_path4init
        return
    @classmethod
    @abstractmethod
    def key_path4init2key_path4store(cls, key_path4init, /):
        'key_path4init -> key_path4store'
        #cls.check_key_path(key_path4init, init_vs_mix_vs_get=False)
        return None
        key_path4store = key_path4init
        return key_path4store
    @classmethod
    @abstractmethod
    def eqv_ex__key_path(cls, key_path4store, unordered_iter_weakables__no_duplicates, key_path4get, /):
        'key_path4store -> unordered_iter_weakables__no_duplicates -> key_path4get -> bool'
        #cls.check_key_path(key_path4get, init_vs_mix_vs_get=True)
        [key_path4init] = unordered_iter_weakables__no_duplicates
        return key_path4init is key_path4get
        return key_path4store is key_path4get



class IMutableOpaquePseudoMapping__init_new_key_only__WeakKeyPathDictionary__init(IMutableOpaquePseudoMapping__init_new_key_only__WeakKeyPathDictionary):
    __slots__ = '_d'
    __slots__ = ('_d', '__weakref__')


    def __init__(sf, /):
        #sf._d = {}
        sf._d = WeakableDict()#Weakable
    @override
    def __getitem__(sf, k, /):
        key_path4get = k
        sf.check_key_path(key_path4get, init_vs_mix_vs_get=True)
        valued_key_path = sf.key_path2valued_key_path(key_path4get, init_vs_mix_vs_get=True)
        (key_path4store, weakable_id2weak_ref_with_callback, v) = sf._d[valued_key_path]
            #KeyError
        unordered_iter_weakables__no_duplicates = (w() for w in weakable_id2weak_ref_with_callback.values())
        if True is not sf.eqv_ex__key_path(key_path4store, unordered_iter_weakables__no_duplicates, key_path4get): raise logic-err#TypeError
        return v
    @override
    def __contains__(sf, k, /):
        sf.check_key_path(k, init_vs_mix_vs_get=None)
        valued_key_path = sf.key_path2valued_key_path(k, init_vs_mix_vs_get=None)
        return valued_key_path in sf._d
    @override
    def ___set_new_item___(sf, k, v, /):
        #sf.check_key_path(k)
        #   __setitem__ using __contains__ ==>> .check_key_path(k) called
        key_path4init = k
        valued_key_path = sf.key_path2valued_key_path(key_path4init, init_vs_mix_vs_get=False)
        key_path4store = sf.key_path4init2key_path4store(key_path4init)
        iter_weakables = sf.key_path4init2iter_weakables__duplicates_ok(key_path4init)
        id2wf = weakable_id2weak_ref_with_callback = {}
        callback = _mk_callback4IWeakKeyPathDictionary__init(sf._d, valued_key_path)
        for weakable in iter_weakables:
            i = id(weakable)
            if i not in id2wf:
                id2wf[i] = weakref.ref(weakable, callback)
        sf._d[valued_key_path] = (key_path4store, weakable_id2weak_ref_with_callback, v)
def _mk_callback4IWeakKeyPathDictionary__init(wd, valued_key_path, /):
    #see:def mk_callback4auto_discard_WeakableDict_key(wd, k, /):
    check_type_is(WeakableDict, wd)
    wd = weakref.ref(wd)
    def callback(_, /):
        #print('callback')
        #bug:wd = wd()
        #   wd become local var
        d = wd()
        if d is not None:
            # not (None or empty)
            m = d.pop(valued_key_path, None)
                #may be removed
            if m is not None:
                (key_path4store, weakable_id2weak_ref_with_callback, v) = m
                weakable_id2weak_ref_with_callback.clear()
                    #prevent other weakref.callback()
    return callback
class MutableOpaquePseudoMapping__init_new_key_only__WeakRefDictionary(IMutableOpaquePseudoMapping__init_new_key_only__WeakKeyPathDictionary__init):
    __slots__ = ()
    @classmethod
    @override
    def check_key_path(cls, key_path, /, init_vs_mix_vs_get):
        'key_path4init/key_path4get -> None'
        check_Weakable(key_path)
        return
    @classmethod
    @override
    def key_path2valued_key_path(cls, key_path, /, init_vs_mix_vs_get):
        'key_path4init/key_path4get -> valued_key_path <: Hashable'
        return id(key_path)

    @classmethod
    @override
    def key_path4init2key_path4get(cls, key_path4init, /):
        'key_path4init -> key_path4get'
        key_path4get = key_path4init
        return key_path4get
    @classmethod
    @override
    def key_path4init2iter_weakables__duplicates_ok(cls, key_path4init, /):
        'key_path4init -> Iter Weakable'
        yield key_path4init
        return
    @classmethod
    @override
    def key_path4init2key_path4store(cls, key_path4init, /):
        'key_path4init -> key_path4store'
        return None
        key_path4store = key_path4init
        return key_path4store
    @classmethod
    @override
    def eqv_ex__key_path(cls, key_path4store, unordered_iter_weakables__no_duplicates, key_path4get, /):
        'key_path4store -> unordered_iter_weakables__no_duplicates -> key_path4get -> bool'
        [key_path4init] = unordered_iter_weakables__no_duplicates
        return key_path4init is key_path4get
        return key_path4store is key_path4get



MutableOpaquePseudoMapping__init_new_key_only__WeakRefDictionary()
def _t():
    from seed.debug.expectError import expectError
    d = MutableOpaquePseudoMapping__init_new_key_only__WeakRefDictionary()
    class X:
        __slots__ = '__weakref__'
        __eq__ = None
        __ne__ = None
        __hash__ = None
    x = X()
    assert not x in d
    def f0():
        d[x]
    assert expectError(KeyError, f0)
    d[x] = 1
    assert x in d
    assert d[x] == 1
    def f1():
        d[x] = 2
    def f2():
        del d[x]
    assert expectError(KeyError, f1)
    assert expectError(AttributeError, f2)
        #AttributeError: __delitem__
    assert d._d
    del x
    assert not d._d

_t()


def _tuple_map_id(xs, /):
    check_tuple(xs)
    return tuple(map(id, xs))

class MutableOpaquePseudoMapping__init_new_key_only__Value_Ref_Weak_KeysTripleDictionary(IMutableOpaquePseudoMapping__init_new_key_only__WeakKeyPathDictionary__init):
    r'''
    key_path = (keys_via_valued_eq, keys_via_id_eq, keys_via_weakref)
    #'''
    __slots__ = ()
    @classmethod
    @override
    def check_key_path(cls, key_path, /, init_vs_mix_vs_get):
        'key_path4init/key_path4get -> None'
        check_tuple(key_path, sz=3)
        (keys_via_valued_eq, keys_via_id_eq, keys_via_weakref) = key_path
        check_tuple(keys_via_valued_eq)
        check_tuple(keys_via_id_eq)
        check_tuple(keys_via_weakref)
        #for key_via_valued_eq in keys_via_valued_eq: check_type_le(Hashable, key_via_valued_eq)
        for key_via_valued_eq in keys_via_valued_eq: check_Hashable__shallow(key_via_valued_eq)
        del key_via_valued_eq
        for key_via_weakref in keys_via_weakref: check_Weakable(key_via_weakref)
        del key_via_weakref
        return
    @classmethod
    @override
    def key_path2valued_key_path(cls, key_path, /, init_vs_mix_vs_get):
        'key_path4init/key_path4get -> valued_key_path <: Hashable'
        (keys_via_valued_eq, keys_via_id_eq, keys_via_weakref) = key_path
        valued_key_path = (keys_via_valued_eq, _tuple_map_id(keys_via_id_eq), _tuple_map_id(keys_via_weakref))
        return valued_key_path

    @classmethod
    @override
    def key_path4init2key_path4get(cls, key_path4init, /):
        'key_path4init -> key_path4get'
        key_path4get = key_path4init
        return key_path4get
    @classmethod
    @override
    def key_path4init2iter_weakables__duplicates_ok(cls, key_path4init, /):
        'key_path4init -> Iter Weakable'
        (keys_via_valued_eq, keys_via_id_eq, keys_via_weakref) = key_path4init
        return iter(keys_via_weakref)
    @classmethod
    @override
    def key_path4init2key_path4store(cls, key_path4init, /):
        'key_path4init -> key_path4store'
        (keys_via_valued_eq, keys_via_id_eq, keys_via_weakref) = key_path4init
        key_path4store = keys_via_id_eq
            #keys_via_valued_eq are saved in valued_key_path
            #but valued_key_path save only id of keys_via_id_eq, keys_via_weakref
            #keys_via_weakref are stored in unordered_iter_weakables__no_duplicates via weakref, callback auto-drop ==>> valued_key_path in __this_impl_mapping__ <-> all weakref alive <-> all id of keys_via_weakref valid
            #remain id of keys_via_id_eq may not valid ==>> should store strong-ref if keys_via_id_eq
        return key_path4store
    @classmethod
    @override
    def eqv_ex__key_path(cls, key_path4store, unordered_iter_weakables__no_duplicates, key_path4get, /):
        'key_path4store -> unordered_iter_weakables__no_duplicates -> key_path4get -> bool'
        #keys_via_id_eq = key_path4store
        (keys_via_valued_eq, keys_via_id_eq, keys_via_weakref) = key_path4get
        return _tuple_map_id(key_path4store) == _tuple_map_id(keys_via_id_eq) and set(_tuple_map_id(unordered_iter_weakables__no_duplicates))==set(_tuple_map_id(keys_via_weakref))



MutableOpaquePseudoMapping__init_new_key_only__Value_Ref_Weak_KeysTripleDictionary()



#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):


if __name__ == "__main__":
#################################
#################################
#################################
#################################
#################################
#################################
    from seed.types.mapping.Mapping__permanent__weakref import WeakableDict, mk_callback4auto_discard_WeakableDict_key

    from seed.types.mapping.Mapping__permanent__weakref import PermanentKeyRefDict, WeakKeyRefDict, PermanentKeyRefSet, WeakKeyRefSet

    from seed.types.mapping.Mapping__permanent__weakref import PRefDict, WRefDict, PRefSet, WRefSet, PermanentKeyRefDict, WeakKeyRefDict, PermanentKeyRefSet, WeakKeyRefSet

    from seed.types.mapping.Mapping__permanent__weakref import PValDict, WValDict, PValSet, WValSet, PermanentKeyValueDict, WeakKeyValueDict, PermanentKeyValueSet, WeakKeyValueSet



    from seed.types.mapping.Mapping__permanent__weakref import WeakKeyDictionary4AddrAsHash



