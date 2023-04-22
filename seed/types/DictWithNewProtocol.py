#__all__:goto
r'''[[[
e ../../python3_src/seed/types/DictWithNewProtocol.py
see:
    view ../../python3_src/seed/mapping_tools/determine_num_slots4hash_map.py
    view ../../python3_src/seed/types/DictWithNewProtocol__ver2.py
see:
    view ../../python3_src/seed/types/DictWithNewProtocol.py
    view ../../python3_src/seed/types/FrozenDict.py
[[
e ../../python3_src/seed/types/DictWithNewProtocol.py
  vs view ../../python3_src/seed/types/FrozenDict.py
  主要意图:
    * 用tuple实现 dict，真FrozenDict，满足 seed.lang.is_immutable_pure_value
    * 避开type(key).__hash__/__eq__，用户定制:type(DictWithNewProtocol).__get_hash_protocol__()->HashProtocol.key_hash/key_eq/storage_key2query_key
    * 实现get_item(outer_key)->(inner_key,value)
  DONE:e ../../python3_src/seed/math/search_smallest_prime_ge_.py
  DONE:e ../../python3_src/seed/math/primes4hash_mapping.py
    e script/primes4hash_mapping.py
]]



py -m nn_ns.app.debug_cmd    seed.types.DictWithNewProtocol
py -m seed.types.DictWithNewProtocol
py -m nn_ns.app.adhoc_argparser__main__call8module    seed.types.DictWithNewProtocol

from seed.types.DictWithNewProtocol import IDictWithNewProtocol, IHashProtocol
from seed.types.DictWithNewProtocol import hash_protocol__default, FrozenDictWithNewProtocol__default


from seed.types.DictWithNewProtocol import IHashProtocol, query_key_eq, query_key_hash, storage_key2query_key, get_bCACHED_QUERY_KEY, get_bCACHED_HASH_VALUE
from seed.types.DictWithNewProtocol import DuplicatedKeyHandler
from seed.types.DictWithNewProtocol import KeyError__duplicates, KeyError__not_found



FrozenDictWithNewProtocol__default

>>> from seed.types.DictWithNewProtocol import IDictWithNewProtocol, IHashProtocol
>>> from seed.types.DictWithNewProtocol import hash_protocol__default, FrozenDictWithNewProtocol__default


>>> from seed.types.DictWithNewProtocol import IHashProtocol, query_key_eq, query_key_hash, storage_key2query_key, get_bCACHED_QUERY_KEY, get_bCACHED_HASH_VALUE
>>> from seed.types.DictWithNewProtocol import DuplicatedKeyHandler
>>> from seed.types.DictWithNewProtocol import KeyError__duplicates, KeyError__not_found


>>> from seed.types.DictWithNewProtocol import HashProtocol__default
>>> from seed.types.DictWithNewProtocol import iter_items_from_may_mapping_or_items



>>> FrozenDictWithNewProtocol__default()
FrozenDictWithNewProtocol__default()
>>> FrozenDictWithNewProtocol__default([])
FrozenDictWithNewProtocol__default()
>>> FrozenDictWithNewProtocol__default([(1, 2)])
FrozenDictWithNewProtocol__default([(1, 2)])
>>> FrozenDictWithNewProtocol__default({1:2})
FrozenDictWithNewProtocol__default([(1, 2)])
>>> {FrozenDictWithNewProtocol__default({1:2}), FrozenDictWithNewProtocol__default({1:2}), FrozenDictWithNewProtocol__default([]), FrozenDictWithNewProtocol__default([])} == {FrozenDictWithNewProtocol__default([(1, 2)]), FrozenDictWithNewProtocol__default()}
True

>>> len(FrozenDictWithNewProtocol__default({1:2}))
1
>>> [*FrozenDictWithNewProtocol__default({1:2})]
[1]
>>> 1 in FrozenDictWithNewProtocol__default({1:2})
True
>>> 2 in FrozenDictWithNewProtocol__default({1:2})
False
>>> FrozenDictWithNewProtocol__default({1:2})[1]
2
>>> FrozenDictWithNewProtocol__default({1:2})[2]
Traceback (most recent call last):
    ...
seed.types.DictWithNewProtocol.KeyError__not_found: 2
>>> FrozenDictWithNewProtocol__default([(1, 2), (1, 3)])
Traceback (most recent call last):
    ...
seed.types.DictWithNewProtocol.KeyError__duplicates: 1
>>> FrozenDictWithNewProtocol__default([(1, 2), (1, 3)], DuplicatedKeyHandler.preserve_last)
FrozenDictWithNewProtocol__default([(1, 3)])
>>> FrozenDictWithNewProtocol__default([(1, 2), (1, 3)], DuplicatedKeyHandler.preserve_first)
FrozenDictWithNewProtocol__default([(1, 2)])
>>> FrozenDictWithNewProtocol__default(((i,-i) for i in range(60)))
FrozenDictWithNewProtocol__default([(0, 0), (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7), (8, -8), (9, -9), (10, -10), (11, -11), (12, -12), (13, -13), (14, -14), (15, -15), (16, -16), (17, -17), (18, -18), (19, -19), (20, -20), (21, -21), (22, -22), (23, -23), (24, -24), (25, -25), (26, -26), (27, -27), (28, -28), (29, -29), (30, -30), (31, -31), (32, -32), (33, -33), (34, -34), (35, -35), (36, -36), (37, -37), (38, -38), (39, -39), (40, -40), (41, -41), (42, -42), (43, -43), (44, -44), (45, -45), (46, -46), (47, -47), (48, -48), (49, -49), (50, -50), (51, -51), (52, -52), (53, -53), (54, -54), (55, -55), (56, -56), (57, -57), (58, -58), (59, -59)])
>>> FrozenDictWithNewProtocol__default([(111111111, 22222222222222), (333333333333333333333, 444444444444444444444444444444444)])
FrozenDictWithNewProtocol__default([(111111111, 22222222222222), (333333333333333333333, 444444444444444444444444444444444)])
>>> type(tuple.__hash__(FrozenDictWithNewProtocol__default([(111111111, 22222222222222), (333333333333333333333, 444444444444444444444444444444444)]))) is int
True

>>> __get_hash_protocol__(FrozenDictWithNewProtocol__default)
HashProtocol__default()
>>> __get_max_num_accidental_collisions_per_slot__(FrozenDictWithNewProtocol__default)
3
>>> [*tuple.__iter__(FrozenDictWithNewProtocol__default([(2, 1), (4, 3)]))]
[2, 1, 2, 2, 1, 4, 1, 4, 4, 3, ((0, 5), None), 2]
>>> [*tuple.__iter__(FrozenDictWithNewProtocol__default([(2, 1), (4, 3), (6, 5)]))]
[6, 1, 6, 6, 5, 4, 1, 4, 4, 3, 2, 1, 2, 2, 1, (0, 5, 10), 3]
>>> [*tuple.__iter__(FrozenDictWithNewProtocol__default([(3, 1), (6, 4), (9, 7)]))]
[3, 1, 3, 3, 1, 6, 1, 6, 6, 4, 9, 1, 9, 9, 7, ((0, 5, 10), None, None), 3]

>>> [*tuple.__iter__(FrozenDictWithNewProtocol__default([(2, 1), (4, 3), (6, 5), (8, 7)]))]
[6, 1, 6, 6, 5, 2, 1, 2, 2, 1, 8, 1, 8, 8, 7, 4, 1, 4, 4, 3, (None, 0, 5, 10, 15), 4]
>>> [*tuple.__iter__(FrozenDictWithNewProtocol__default([(5, 1), (10, 6), (15, 11), (20, 16)]))]
[15, 1, 15, 15, 11, 10, 1, 10, 10, 6, 5, 1, 5, 5, 1, 20, 1, 20, 20, 16, (None, 0, None, 5, None, 10, 15), 4]

_attr_seq4dir
>>> dir(FrozenDictWithNewProtocol__default())
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__getattribute__', '__getitem__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__len__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'get', 'get_storage_item', 'items', 'iter__query_key__storage_key__target_value__triples', 'iter_query_items', 'iter_query_keys', 'iter_storage_items', 'iter_storage_keys', 'iter_target_values', 'keys', 'values']


view '/data/data/com.termux/files/usr/lib/python3.10/pickle.py'
        self._instantiate(klass, args)
__reduce__(self, /)
__reduce_ex__(self, protocol, /)
#>>> {}.__reduce_ex__(2)
(<function __newobj__ at 0x718f54a0e0>, (<class 'dict'>,), None, None, <dict_itemiterator object at 0x718f7c1580>)
#>>> [].__reduce_ex__(2)
(<function __newobj__ at 0x718f54a0e0>, (<class 'list'>,), None, <list_iterator object at 0x718f787b20>, None)
#>>> 1 .__reduce_ex__(2)
(<function __newobj__ at 0x718f54a0e0>, (<class 'int'>, 1), None, None, None)
#>>> '' .__reduce_ex__(2)
(<function __newobj__ at 0x718f54a0e0>, (<class 'str'>, ''), None, None, None)
#>>> None .__reduce_ex__(2)
(<function __newobj__ at 0x718f54a0e0>, (<class 'NoneType'>,), None, None, None)
>>> ... .__reduce_ex__(2)
'Ellipsis'

>>> import pickle
>>> pickle.dumps(FrozenDictWithNewProtocol__default())
b'\x80\x04\x95N\x00\x00\x00\x00\x00\x00\x00\x8c\x1eseed.types.DictWithNewProtocol\x94\x8c"FrozenDictWithNewProtocol__default\x94\x93\x94)\x85\x94\x81\x94.'

b'\x80\x04\x95\x8c\x00\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\x8c\x07getattr\x94\x93\x94\x8c\x08builtins\x94\x8c\x05tuple\x94\x93\x94\x8c\x07__new__\x94\x86\x94R\x94\x8c\x1eseed.types.DictWithNewProtocol\x94\x8c"FrozenDictWithNewProtocol__default\x94\x93\x94)K\x00\x86\x94\x86\x94R\x94.'

b'\x80\x04\x95R\x00\x00\x00\x00\x00\x00\x00\x8c\x1eseed.types.DictWithNewProtocol\x94\x8c"FrozenDictWithNewProtocol__default\x94\x93\x94)K\x00\x86\x94\x85\x94\x81\x94.'
>>> pickle.loads(pickle.dumps(FrozenDictWithNewProtocol__default()))
FrozenDictWithNewProtocol__default()
>>> pickle.loads(pickle.dumps(FrozenDictWithNewProtocol__default({i:-i for i in range(12)})))
FrozenDictWithNewProtocol__default([(0, 0), (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7), (8, -8), (9, -9), (10, -10), (11, -11)])

>>> pickle.dumps(FrozenDictWithNewProtocol__default({i:-i for i in range(12)}))
b'\x80\x04\x95\xb9\x00\x00\x00\x00\x00\x00\x00\x8c\x1eseed.types.DictWithNewProtocol\x94\x8c"FrozenDictWithNewProtocol__default\x94\x93\x94(K\x00K\x00\x86\x94K\x01J\xff\xff\xff\xff\x86\x94K\x02J\xfe\xff\xff\xff\x86\x94K\x03J\xfd\xff\xff\xff\x86\x94K\x04J\xfc\xff\xff\xff\x86\x94K\x05J\xfb\xff\xff\xff\x86\x94K\x06J\xfa\xff\xff\xff\x86\x94K\x07J\xf9\xff\xff\xff\x86\x94K\x08J\xf8\xff\xff\xff\x86\x94K\tJ\xf7\xff\xff\xff\x86\x94K\nJ\xf6\xff\xff\xff\x86\x94K\x0bJ\xf5\xff\xff\xff\x86\x94t\x94\x85\x94\x81\x94.'






>>> hash_protocol__default
HashProtocol__default()
>>> hash_protocol__default is HashProtocol__default()
True


#]]]'''
__all__ = r'''
IHashProtocol
    query_key_eq
    query_key_hash
    storage_key2query_key
    get_bCACHED_QUERY_KEY
    get_bCACHED_HASH_VALUE

IDictWithNewProtocol
    __get_hash_protocol__
    __get_max_num_accidental_collisions_per_slot__

    DuplicatedKeyHandler

    KeyError__duplicates
    KeyError__not_found

    iter_items_from_may_mapping_or_items

HashProtocol__default
    hash_protocol__default
IDictWithNewProtocol
    FrozenDictWithNewProtocol__default

'''.split()#'''
__all__

#from seed.mapping_tools.determine_num_slots4hash_map import IDetermineNumSlots4HashMap, determine_num_slots4hash_map
from enum import Enum, auto
from itertools import pairwise, groupby, combinations
from collections.abc import Mapping

#from seed.abc.abc import ABC, abstractmethod, override, not_implemented, ABCMeta
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.tiny import check_type_is, check_type_le, null_tuple, fst, snd, at, curry1, MapView, print_err
from seed.algo.bucket_sort.bucket_sort_per_row import bucket_sort_per_row
from seed.math.primes4hash_mapping import find_suitable_seq_size4hash_mapping__tabular
from seed.math.search_smallest_prime_ge_ import find_suitable_seq_size4hash_mapping__search, search_smallest_prime_ge_, search_smallest_prime_gt_, search_largest_prime_le_, search_largest_prime_lt_
from seed.seq_tools.bisearch import bisearch
#from bisect import bisect_left, bisect_right
from seed.helper.repr_input import repr_helper

at2 = at(2)
at1_ = at[1:]
at0_E_2 = at[::2]

# print(dir(()))
# print(dir({}))
_attrs4tuple = {*dir(())}
_attrs4dict = {*dir({})}
_attrs4Mapping = {*dir(Mapping)}
_attrs4MapView = {*dir(MapView({}))}
_attrs_ok = _attrs4MapView & _attrs4Mapping & _attrs4dict
_attrs_bad = _attrs4tuple - _attrs_ok

if 0:
    print(sorted(_attrs_ok))
    ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'get', 'items', 'keys', 'values']
    print(sorted(_attrs_bad))
    ['__add__', '__getnewargs__', '__mul__', '__rmul__', 'count', 'index']


AttributeError

class IHashProtocol(ABC):
    __slots__ = ()
    #def storage_key_hash(sf, storage_key, /):
    #def storage_key_eq(sf, storage_key, /):
    @abstractmethod
    def query_key_eq(sf, lhs_query_key, rhs_query_key, /):
        'lhs_query_key -> rhs_query_key -> bool'
    @abstractmethod
    def query_key_hash(sf, query_key, /):
        'query_key -> hash_value<query_key>'
    @abstractmethod
    def storage_key2query_key(sf, storage_key, /):
        'storage_key -> query_key'
    @abstractmethod
    def get_bCACHED_QUERY_KEY(sf, /):
        '-> bool #storage_key2query_key is hard'
    @abstractmethod
    def get_bCACHED_HASH_VALUE(sf, /):
        '-> bool #query_key_hash is hard'

    @abstractmethod
    def target_value_eq(sf, lhs_target_value, rhs_target_value, /):
        'lhs_target_value -> rhs_target_value -> bool'
    @abstractmethod
    def target_value_hash(sf, target_value, /):
        'target_value -> hash_value<target_value>'

def query_key_eq(sf, lhs_query_key, rhs_query_key, /):
    'lhs_query_key -> rhs_query_key -> bool'
    b = sf.query_key_eq(lhs_query_key, rhs_query_key)
    check_type_is(bool, b)
    return b
def query_key_hash(sf, query_key, /):
    'query_key -> hash_value<query_key>'
    h = sf.query_key_hash(query_key)
    check_type_is(int, h)
    return h
def storage_key2query_key(sf, storage_key, /):
    'storage_key -> query_key'
    query_key = sf.storage_key2query_key(storage_key)
    return query_key

def get_bCACHED_QUERY_KEY(sf, /):
    '-> bool #storage_key2query_key is hard'
    b = sf.get_bCACHED_QUERY_KEY()
    check_type_is(bool, b)
    return b
def get_bCACHED_HASH_VALUE(sf, /):
    '-> bool #query_key_hash is hard'
    b = sf.get_bCACHED_HASH_VALUE()
    check_type_is(bool, b)
    return b
def target_value_eq(sf, lhs_target_value, rhs_target_value, /):
    'lhs_target_value -> rhs_target_value -> bool'
    b = sf.target_value_eq(lhs_target_value, rhs_target_value)
    check_type_is(bool, b)
    return b
def target_value_hash(sf, target_value, /):
    'target_value -> hash_value<target_value>'
    h = sf.target_value_hash(target_value)
    check_type_is(int, h)
    return h


class DuplicatedKeyHandler(Enum):
    'duplicated_key_handler'
    forbid_duplicates = auto()
    preserve_last = auto()
    preserve_first = auto()
class KeyError__duplicates(KeyError):pass
class KeyError__not_found(KeyError):pass
def _():
    def forbid_duplicates(mapping_cls, hash_protocol, lhs_5ple, rhs_5ple, /):
        (idx, hash_value, query_key, storage_key, target_value) = lhs_5ple
        raise KeyError__duplicates(storage_key)
    def preserve_last(mapping_cls, hash_protocol, lhs_5ple, rhs_5ple, /):
        #yield rhs_5ple
        yield max(lhs_5ple, rhs_5ple, key=fst)
    def preserve_first(mapping_cls, hash_protocol, lhs_5ple, rhs_5ple, /):
        #yield lhs_5ple
        yield min(lhs_5ple, rhs_5ple, key=fst)
    return (
    {DuplicatedKeyHandler.forbid_duplicates:forbid_duplicates
    ,DuplicatedKeyHandler.preserve_last:preserve_last
    ,DuplicatedKeyHandler.preserve_first:preserve_first
    })
_symbol2handler = _(); del _

try:
    class _(Mapping):
        __slots__ = ()
    #assert tuple.__new__(_), _.__abstractmethods__
    assert object.__new__(_), _.__abstractmethods__
except TypeError:
    #TypeError: tuple.__new__(_): _ is not a subtype of tuple
    #TypeError: Can't instantiate abstract class _ with abstract methods __getitem__, __iter__, __len__
    pass
try:
    class _(Mapping, tuple):
        __slots__ = ()
    assert tuple.__new__(_), _.__abstractmethods__
except AssertionError:
    #AssertionError: frozenset({'__len__', '__getitem__', '__iter__'})
    pass

r'''[[[
class _NewArgs4IDictWithNewProtocol:
    __slots__ = 'arg'
    def __init__(sf, arg, /):
        sf.arg = arg
#]]]'''

__newobj__ = None.__reduce_ex__(2)[0]
def _raise(*args, **kwargs):
    print_err((args, kwargs))
    raise Exception((args, kwargs))
class IDictWithNewProtocol(Mapping, ABC, tuple):
    __slots__ = ()
    def __dir__(sf, /):
        return _attr_seq4dir
    def __getattribute__(sf, nm, /):
        if nm in _attrs_bad: raise AttributeError(nm)
        return super(__class__, type(sf)).__getattribute__(sf, nm)
    def __reduce__(sf, /):
        #pickle
        cls = type(sf)
        arg = (*sf.iter_storage_items(),)
        return (__newobj__, (cls, arg))
        cls = type(sf)
        arg = (*sf.iter_storage_items(),)
        #return (__newobj__, (cls, arg), {}, None, None, None)
        #   AttributeError: 'FrozenDictWithNewProtocol__default' object has no attribute '__dict__'
        #return (__newobj__, (cls, arg), 1, iter([1]), None, _raise)
        #   AttributeError: 'FrozenDictWithNewProtocol__default' object has no attribute 'append'
        #return (__newobj__, (cls, arg), 1, iter([]), None, _raise)
        #   _raise(sf, 1)
        #return (__newobj__, (cls, arg), 1, None, None, _raise)
        #   _raise(sf, 1)
        #return (__newobj__, (cls, arg), 1, None, 3, _raise)
        #   _pickle.PicklingError: fifth element of the tuple returned by __reduce__ must be an iterator, not int
        #return (__newobj__, (cls, arg), 1, 2, None, _raise)
        #   _pickle.PicklingError: fourth element of the tuple returned by __reduce__ must be an iterator, not int
        return (__newobj__, (cls, arg), None, None, None, _raise) #ok!!!
            #not call _raise
        cls = type(sf)
        #return (__newobj__, (cls,), sf)
        #   _pickle.UnpicklingError: state is not a dictionary
        cls = type(sf)
        arg = sf.iter_storage_items()
        #return (__newobj__, (cls,), None, None, arg)
        #   TypeError: 'FrozenDictWithNewProtocol__default' object does not support item assignment
        #   _pickle.PicklingError: fifth element of the tuple returned by __reduce__ must be an iterator, not tuple
        #return (__newobj__, (cls,), None, arg)
        #   AttributeError: 'FrozenDictWithNewProtocol__default' object has no attribute 'append'
        cls = type(sf)
        arg = (*sf.iter_storage_items(),)
        #return (__newobj__, (cls,), None, None, None, None, arg)
        #   _pickle.PicklingError: tuple returned by __reduce__ must contain 2 through 6 elements
        #return (__newobj__, (cls,), None, None, None, arg)
        #   _pickle.PicklingError: sixth element of the tuple returned by __reduce__ must be a function, not tuple
        #return (__newobj__, (cls,), None, None, arg)
        #   _pickle.PicklingError: fifth element of the tuple returned by __reduce__ must be an iterator, not tuple
        #return (__newobj__, (cls,), None, arg)
        #   _pickle.PicklingError: fourth element of the tuple returned by __reduce__ must be an iterator, not tuple
        #return (__newobj__, (cls,), arg)
        #   _pickle.UnpicklingError: state is not a dictionary
        return (__newobj__, (cls, arg))
        cls = type(sf)
        arg = tuple(tuple.__iter__(sf))
        return (tuple.__new__, (cls, arg))
        #return (__newobj__, (cls, arg))
        #return (None, (cls, arg))
        #   _pickle.PicklingError: first item of the tuple returned by __reduce__ must be callable
        #err: return (_NewArgs4IDictWithNewProtocol(arg),)
        #   _pickle.PicklingError: tuple returned by __reduce__ must contain 2 through 6 elements

    #@classmethod
    @abstractmethod
    def __get_max_num_accidental_collisions_per_slot__(cls, /):
        '-> pint #max_num_accidental_collisions_per_slot'
    #@classmethod
    @abstractmethod
    def __get_hash_protocol__(cls, /):
        '-> IHashProtocol'
    def __new__(cls, may_mapping_or_items=None, may_duplicated_key_handler=None, /):
        sf = __new4DictWithNewProtocol__(__class__, cls, may_mapping_or_items, may_duplicated_key_handler)
        check_type_is(cls, sf)
        return sf
    #_unbox4DictWithNewProtocol_
    #_attrs_ok
    #IDictWithNewProtocol.__abstractmethods__
    '__len__', '__iter__', '__get_max_num_accidental_collisions_per_slot__', '__getitem__', '__get_hash_protocol__'
    #def __get_hash_protocol__(sf, /):
    #def __get_max_num_accidental_collisions_per_slot__(sf, /):
    @override
    def __len__(sf, /):
        (ls_, jss, sz) = _unbox4DictWithNewProtocol_(sf)
        return sz
    @override
    def __iter__(sf, /):
        '-> Iter query_key #since __contains__<<==__iter__+__getitem__'
        return sf.iter_query_keys()
    @override
    def keys(sf, /):
        'since KeydView <<== __eq__'
        return sf.iter_query_keys()
    @override
    def items(sf, /):
        'since ItemsView <<==? __eq__'
        return sf.iter_query_items()
    @override
    def values(sf, /):
        'since ValuesView <<==? __eq__'
        return sf.iter_target_values()
    def iter_query_keys(sf, /):
        '-> Iter query_key'
        return map(fst, sf.iter__query_key__storage_key__target_value__triples())
    def iter_storage_keys(sf, /):
        '-> Iter storage_key'
        return map(snd, sf.iter__query_key__storage_key__target_value__triples())
    def iter_target_values(sf, /):
        '-> Iter target_value'
        return map(at2, sf.iter__query_key__storage_key__target_value__triples())
    def iter_storage_items(sf, /):
        '-> Iter (storage_key, target_value)'
        return map(at1_, sf.iter__query_key__storage_key__target_value__triples())
    def iter_query_items(sf, /):
        '-> Iter (query_key, target_value)'
        return map(at0_E_2, sf.iter__query_key__storage_key__target_value__triples())

    def iter__query_key__storage_key__target_value__triples(sf, /):
        return _iter_2(sf)
        return _iter_1(sf)
    def get_storage_item(sf, query_key, /):
        tmay_triple = _get_tmay_triple(sf, query_key)
        if not tmay_triple:
            raise KeyError__not_found(query_key)
        [(_query_key, storage_key, target_value)] = tmay_triple
        return (storage_key, target_value)
    @override
    def __getitem__(sf, query_key, /):
        (storage_key, target_value) = sf.get_storage_item(query_key)
        return target_value

    @override
    def __eq__(sf, ot, /):
        if sf is ot:
            return True
        if not type(sf) is type(ot):
            return False
        if not len(sf) == len(ot):
            return False
        if not all(query_key in ot for query_key in sf):
            return False
        cls = type(sf)
        hash_protocol = __get_hash_protocol__(cls)
        veq = curry1(target_value_eq, hash_protocol)
        if not all(veq(target_value, ot[query_key]) for query_key, target_value in sf.iter_query_items()):
        #if not all(target_value == ot[query_key] for query_key, target_value in sf.iter_query_items()):
            return False
        return True

    @override
    def __hash__(sf, /):
        cls = type(sf)
        hash_protocol = __get_hash_protocol__(cls)
        vhash = curry1(target_value_hash, hash_protocol)
        h = 0
        for (h1, query_key, storage_key, target_value) in _iter_2_with_h(sf):
            h2 = vhash(target_value)
            h ^= hash((h1, h2))
        cls = type(sf)
        hh = hash((id(cls), len(sf), h))
        return hh

    @override
    def __repr__(sf, /):
        arg = [*sf.iter_storage_items()]
        if arg:
            args = (arg,)
        else:
            args = ()
        return repr_helper(sf, *args)
    pass
#end-class IDictWithNewProtocol(tuple, ABC):
_attr_seq4dir = tuple(sorted(
    {*_attrs_ok
    , *[nm for nm in IDictWithNewProtocol.__dict__ if type(nm) is str and nm and not nm[:1]=='_']
    }
    - {'__ge__', '__gt__', '__le__', '__lt__', '__reversed__'}
    #, '__reduce__', '__reduce_ex__'
    ))


#assert IDictWithNewProtocol.__abstractmethods__ == frozenset({'__len__', '__iter__', '__get_max_num_accidental_collisions_per_slot__', '__getitem__', '__get_hash_protocol__'})
assert IDictWithNewProtocol.__abstractmethods__ == frozenset({'__get_max_num_accidental_collisions_per_slot__', '__get_hash_protocol__'})
#assert tuple.__new__(IDictWithNewProtocol), IDictWithNewProtocol.__abstractmethods__
def _get_tmay_triple(sf, query_key, /):
    '-> tmay (_query_key, storage_key, target_value)'
    hash_protocol = __get_hash_protocol__(type(sf))
    hash_value = query_key_hash(hash_protocol, query_key)
    (ls_, jss, sz) = _unbox4DictWithNewProtocol_(sf)
    MM = len(jss)
    js = jss[hash_value%MM]
    js = _correct_js(js)
    (iA,iB) = bisearch(hash_value, js, key=ls_)
    if not iA==iB:
        assert iB==iA+1
        j = js[iA]
        (h, n, it, j_next) = _iter_at_j_ex(ls_, j)
        assert h==hash_value
        for (_query_key, storage_key, target_value) in it:
            if query_key_eq(hash_protocol, query_key, _query_key):
                return ((_query_key, storage_key, target_value),)
    return ()


def _iter_2_with_h(sf, /):
    for h, it in _iter_2_ex(sf):
        for (query_key, storage_key, target_value) in it:
            yield (h, query_key, storage_key, target_value)
def _iter_2(sf, /):
    for h, it in _iter_2_ex(sf):
        yield from it
def _iter_2_ex(sf, /):
    (ls_, jss, sz) = _unbox4DictWithNewProtocol_(sf)
    j = 0
    while sz > 0:
        (h, n, it, j_next) = _iter_at_j_ex(ls_, j)
        yield (h, it)
        assert n >= 1
        sz -= n
        j = j_next
    assert sz == 0
def _correct_js(js, /):
    if js is None:
        js = null_tuple
    elif type(js) is int:
        j = js
        js = (j,)
    else:
        pass
    check_type_is(tuple, js)
    return js
def _iter_1(sf, /):
    (ls_, jss, sz) = _unbox4DictWithNewProtocol_(sf)
    for js in jss:
        js = _correct_js(js)
        for j in js:
            yield from _iter_at_j(ls_, j)

def _iter_at_j(ls_, j, /):
    (h, n, it, j_next) = _iter_at_j_ex(ls_, j)
    return it
def _iter_at_j_ex(ls_, j, /):
    h = hash_value = ls_(j)
    n = num_diff_query_keys_with_same_hash_values = ls_(j+1)
    j_next = j+2+n*3
    it = _iter_at_j__impl(ls_, j, j_next)
    return (h, n, it, j_next)

def _iter_at_j__impl(ls_, j, j_next, /):
    for k in range(j+2, j_next, 3):
        query_key = ls_(k)
        storage_key = ls_(k+1)
        target_value = ls_(k+2)
        yield (query_key, storage_key, target_value)

def _cls5cls_or_sf(cls_or_sf, /):
    if isinstance(cls_or_sf, type):
        cls = cls_or_sf
    else:
        sf = cls_or_sf
        cls = type(sf)
    cls
    return cls
def __get_max_num_accidental_collisions_per_slot__(cls_or_sf, /):
    cls = _cls5cls_or_sf(cls_or_sf)
    max_num_accidental_collisions_per_slot = cls.__get_max_num_accidental_collisions_per_slot__(cls)
    check_type_is(int, max_num_accidental_collisions_per_slot)
    if not max_num_accidental_collisions_per_slot > 0: raise TypeError
    return max_num_accidental_collisions_per_slot
def __get_hash_protocol__(cls_or_sf, /):
    cls = _cls5cls_or_sf(cls_or_sf)
    hash_protocol = cls.__get_hash_protocol__(cls)
    check_type_le(IHashProtocol, hash_protocol)
    return hash_protocol

def iter_items_from_may_mapping_or_items(may_mapping_or_items, /):
    if may_mapping_or_items is None:
        items = null_tuple
    elif hasattr(may_mapping_or_items, 'items'):
        mapping = may_mapping_or_items
        items = getattr(mapping, 'items')()
    else:
        items = may_mapping_or_items
    items
    items = iter(items)
    return items

def _handler5may_symbol(may_duplicated_key_handler, /):
    if may_duplicated_key_handler is None:
        duplicated_key_handler = DuplicatedKeyHandler.forbid_duplicates
    else:
        duplicated_key_handler = may_duplicated_key_handler
    duplicated_key_handler
    check_type_is(DuplicatedKeyHandler, duplicated_key_handler)
    duplicated_key_handler = _symbol2handler[duplicated_key_handler]
    return duplicated_key_handler

def _():
    #__new4DictWithNewProtocol__
    def _main(__class__, cls, may_mapping_or_items, may_duplicated_key_handler, /):
        duplicated_key_handler = _handler5may_symbol(may_duplicated_key_handler)

        items = iter_items_from_may_mapping_or_items(may_mapping_or_items)
        hash_protocol = __get_hash_protocol__(cls)
        try:
            _5ples = mk_5ples(hash_protocol, items)
        except:
            raise TypeError((type(may_mapping_or_items), may_mapping_or_items))

        sz_count_duplicates = len(_5ples)
        yss = hash_then_group(_5ples)
        assert sum(map(len, yss)) == sz_count_duplicates
        del _5ples
        xss = remove_duplicated_query_keys(cls, hash_protocol, duplicated_key_handler, sz_count_duplicates, yss)
        del yss

        max_num_accidental_collisions_per_slot = __get_max_num_accidental_collisions_per_slot__(cls)
        (hash_values, sz, LL, MM) = determine_size(max_num_accidental_collisions_per_slot, xss)
        h_zs_pairss = pack1(max_num_accidental_collisions_per_slot, MM, hash_values, xss)
        del xss

        ls = pack2(sz, MM, h_zs_pairss)
        #####
        sf = super(__class__, cls).__new__(cls, ls)
        del ls

        check_type_is(cls, sf)
        return sf
    #end-def _main():

    def mk_5ples(hash_protocol, items, /):
        _5ples = []
        for idx, (storage_key, target_value) in enumerate(items):
            query_key = storage_key2query_key(hash_protocol, storage_key)
            hash_value = query_key_hash(hash_protocol, query_key)
            _5ple = (idx, hash_value, query_key, storage_key, target_value)
            _5ples.append(_5ple)
        return _5ples
    def hash_then_group(_5ples, /):
        xss = _hash(_5ples)
        yss = _group(xss); del xss
        return yss

    def _hash(_5ples, /):
        sz_count_duplicates = len(_5ples)
        #M = find_suitable_seq_size4hash_mapping__search
        M = find_suitable_seq_size4hash_mapping__tabular(sz_count_duplicates)
        xss = [[] for _ in range(M)]
        for _5ple in _5ples:
            hash_value = snd(_5ple)
            j = hash_value%M
            xss[j].append(_5ple)
        return xss
    def _group(xss, /):
        yss = [] #collect/group same hash_value
        for xs in xss:
            if len(xs) >= 2:
                xs.sort(key=snd)
                yss.extend([*it] for h, it in groupby(xs, snd))
            elif xs:
                yss.append(xs)
        del xss
        return yss

    def remove_duplicated_query_keys(cls, hash_protocol, duplicated_key_handler, sz_count_duplicates, yss, /):
        xss = []
        for ys in yss:
            #for x,y in combinations(ys, 2):
            #    if query_key_eq(hash_protocol, at2(x), at2(y)):
            xs = []
            zs = []
            while ys:
                y = ys.pop()
                while xs:
                    x = xs.pop()
                    if query_key_eq(hash_protocol, at2(x), at2(y)):
                        [z] = duplicated_key_handler(cls, hash_protocol, x, y)
                        if z is x:
                            pass
                        elif z is y:
                            pass
                        else:
                            raise logic-err
                        zs.append(z)
                        zs.extend(xs)
                        xs.clear()
                        break#!!
                    else:
                        zs.append(x)
                else:
                        zs.append(y)
                assert not xs
                assert zs
                zs, xs = xs, zs
            assert xs
            assert not ys
            assert not zs
            #ys.extend(xs)
            xss.append(xs)
        del yss
        xss = bucket_sort_per_row(sz_count_duplicates, xss, None, key=fst)
        #xss = [*map(tuple, xss)]
        return xss
    #end-def remove_duplicated_query_keys(cls, hash_protocol, duplicated_key_handler, yss, /):
    def determine_size(max_num_accidental_collisions_per_slot, xss, /):
        hash_values = [snd(xs[0]) for xs in xss]
        #no duplicate query_keys now
        #but has accidental collisions of diff hash_values

        sz = sum(map(len, xss))
            #num nonduplicate query_keys
        LL = len(xss)
            #num hash_values
        MM = find_suitable_seq_size4hash_mapping__tabular(LL)
            #num hash table slots


        def is_ok(hash_values, MM, /):
            counts = [0]*MM
            for h in hash_values:
                counts[h%MM] += 1
            return max(counts, default=0) <= max_num_accidental_collisions_per_slot
        if not is_ok(hash_values, MM):
            MM = search_smallest_prime_ge_(LL)
            while not is_ok(hash_values, MM):
                MM = search_smallest_prime_gt_(MM)
        MM
        return (hash_values, sz, LL, MM)
    #end-def determine_size(max_num_accidental_collisions_per_slot, xss, /):

    def pack1(max_num_accidental_collisions_per_slot, MM, hash_values, xss, /):
        h_zs_pairss = [[] for _ in range(MM)]
        for h, xs in zip(hash_values, xss):
            j = h%MM
            zs = tuple((query_key, storage_key, target_value) for (idx, hash_value, query_key, storage_key, target_value) in xs)
            h_zs_pair = (h, zs)
            h_zs_pairss[j].append(h_zs_pair)
        assert max(map(len, h_zs_pairss), default=0) <= max_num_accidental_collisions_per_slot
        for h_zs_pairs in h_zs_pairss:
            h_zs_pairs.sort(key=fst)
        #h_zs_pairss = [*map(tuple, h_zs_pairss)]
        return h_zs_pairss
    #end-def pack1(MM, hash_values, xss, /):
    def pack2(sz, MM, h_zs_pairss, /):
        ls = []
        jss = []
        for h_zs_pairs in h_zs_pairss:
            js = []
            for h,zs in h_zs_pairs:
                j = len(ls)
                ls.append(h)
                ls.append(len(zs))
                for (query_key, storage_key, target_value) in zs:
                    ls.append(query_key)
                    ls.append(storage_key)
                    ls.append(target_value)
                assert len(ls) == j+2+3*ls[j+1]
                js.append(j)
            #jss.append(js)
            if not js:
                jss.append(None)
            elif len(js)==1:
                [j] = js
                jss.append(j)
            else:
                js = (*js,)
                jss.append(js)
        assert len(jss) == MM

        jss = (*jss,)
        ls.append(jss)
        sz
        ls.append(sz)
        ls = (*ls,)
        return ls
    #end-def pack2(sz, MM, h_zs_pairss, /):
    return _main
_main = _(); del _
def __new4DictWithNewProtocol__(__class__, cls, may_mapping_or_items, may_duplicated_key_handler, /):
    if cls.__abstractmethods__: raise TypeError(f'{cls!r}.__abstractmethods__ == {cls.__abstractmethods__!r}')
    return _main(__class__, cls, may_mapping_or_items, may_duplicated_key_handler)
try:
    assert IDictWithNewProtocol(), IDictWithNewProtocol.__abstractmethods__
except TypeError:
    #TypeError: <class '__main__.IDictWithNewProtocol'>.__abstractmethods__ == frozenset({'__get_hash_protocol__', '__get_max_num_accidental_collisions_per_slot__', '__getitem__', '__iter__', '__len__'})
    pass

def _unbox4DictWithNewProtocol_(sf, /):
    ls_ = curry1(tuple.__getitem__, sf)
    jss = ls_(-2)
    sz = ls_(-1)
    #MM = len(jss)
    return (ls_, jss, sz)



class HashProtocol__default(IHashProtocol):
    __slots__ = ()
    @override
    def query_key_eq(sf, lhs_query_key, rhs_query_key, /):
        'lhs_query_key -> rhs_query_key -> bool'
        #operator.__eq__
        return lhs_query_key==rhs_query_key
    @override
    def query_key_hash(sf, query_key, /):
        'query_key -> hash_value<query_key>'
        #__builtins__.hash
        return hash(query_key)
    @override
    def storage_key2query_key(sf, storage_key, /):
        'storage_key -> query_key'
        #echo
        query_key = storage_key
        return query_key
    @override
    def get_bCACHED_QUERY_KEY(sf, /):
        '-> bool #storage_key2query_key is hard'
        return False#echo
    @override
    def get_bCACHED_HASH_VALUE(sf, /):
        '-> bool #query_key_hash is hard'
        return True #__builtins__.hash#unless query_key is int or use id as hash
    @override
    def __repr__(sf, /):
        return repr_helper(sf)

    @override
    def target_value_eq(sf, lhs_target_value, rhs_target_value, /):
        'lhs_target_value -> rhs_target_value -> bool'
        #operator.__eq__
        return lhs_target_value==rhs_target_value
    @override
    def target_value_hash(sf, target_value, /):
        'target_value -> hash_value<target_value>'
        #__builtins__.hash
        return hash(target_value)

hash_protocol__default = HashProtocol__default()
HashProtocol__default.__abstractmethods__ = frozenset(['singleton-class'])
HashProtocol__default.__new__ = lambda cls: hash_protocol__default
assert HashProtocol__default() is hash_protocol__default

class FrozenDictWithNewProtocol__default(IDictWithNewProtocol):
    __slots__ = ()

    @override
    def __get_hash_protocol__(sf, /):
        return hash_protocol__default
    @override
    def __get_max_num_accidental_collisions_per_slot__(sf, /):
        return 3


from seed.types.DictWithNewProtocol import IDictWithNewProtocol, IHashProtocol
from seed.types.DictWithNewProtocol import hash_protocol__default, FrozenDictWithNewProtocol__default


from seed.types.DictWithNewProtocol import IHashProtocol, query_key_eq, query_key_hash, storage_key2query_key, get_bCACHED_QUERY_KEY, get_bCACHED_HASH_VALUE
from seed.types.DictWithNewProtocol import DuplicatedKeyHandler
from seed.types.DictWithNewProtocol import KeyError__duplicates, KeyError__not_found
from seed.types.DictWithNewProtocol import HashProtocol__default
from seed.types.DictWithNewProtocol import iter_items_from_may_mapping_or_items

from seed.types.DictWithNewProtocol import *




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL

