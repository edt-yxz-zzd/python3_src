r'''

from seed.types.empty_containers import empty_mapping
seed.types.empty_containers
    <--- seed.types.EmptyMapping
py -m seed.types.empty_containers
py -m nn_ns.app.debug_cmd   seed.types.empty_containers

from seed.types.empty_containers import EmptyMapping, EmptySet, EmptySequence, empty_mapping, empty_set, empty_sequence, empty_tuple, empty_iterator

from seed.types.empty_containers import IndexError_KeyError
from seed.types.empty_containers import EmptyHashableBase, EmptyIterable, EmptyReversible, EmptySized, EmptyContainer, EmptyCollection

from seed.types.empty_containers import EmptyMapping, EmptySet, EmptySequence, EmptyThree

from seed.types.empty_containers import theEmptyHashableBase, theEmptyIterable, theEmptySized, theEmptyContainer, theEmptyCollection, theEmptyReversible, theEmptyMapping, theEmptySet, theEmptySequence, theEmptyThree, empty_mapping, empty_set, empty_sequence, empty_three, empty_tuple, empty_iterator





>>> empty_mapping
EmptyMapping()

>>> vars(empty_mapping) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
TypeError
>>> empty_mapping.__dict__ #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
AttributeError
>>> empty_mapping['a']
Traceback (most recent call last):
    ...
KeyError: 'a'
>>> len(empty_mapping)
0
>>> list(empty_mapping)
[]
>>> list(empty_mapping.keys())
[]
>>> list(empty_mapping.values())
[]
>>> list(empty_mapping.items())
[]


>>> 1 in empty_mapping
False
>>> bool(empty_mapping)
False



>>> 1 in empty_set
False
>>> bool(empty_set)
False
>>> 1 in empty_sequence
False
>>> bool(empty_sequence)
False



>>> empty_set < empty_set
False
>>> empty_set > empty_set
False
>>> empty_set <= empty_set
True
>>> empty_set >= empty_set
True
>>> empty_set < set()
Traceback (most recent call last):
    ...
TypeError
>>> set() < empty_set
Traceback (most recent call last):
    ...
TypeError

>>> empty_set & empty_set
EmptySet()
>>> empty_set | empty_set
EmptySet()
>>> empty_set ^ empty_set
EmptySet()
>>> empty_set - empty_set
EmptySet()
>>> set() - empty_set
Traceback (most recent call last):
    ...
TypeError: unsupported operand type(s) for -: 'set' and 'EmptySet'
>>> empty_set - set()
Traceback (most recent call last):
    ...
TypeError
>>> empty_set.isdisjoint(empty_set)
True
>>> empty_set.isdisjoint(set())
True
>>> set().isdisjoint(empty_set)
True

>>> empty_mapping['a']
Traceback (most recent call last):
    ...
KeyError: 'a'
>>> empty_sequence['a']
Traceback (most recent call last):
    ...
TypeError: tuple indices must be integers or slices, not str
>>> empty_three['a']
Traceback (most recent call last):
    ...
TypeError: tuple indices must be integers or slices, not str

>>> empty_mapping[0]
Traceback (most recent call last):
    ...
KeyError: 0
>>> empty_sequence[0]
Traceback (most recent call last):
    ...
IndexError: tuple index out of range
>>> empty_three[0]
Traceback (most recent call last):
    ...
IndexError_KeyError: 0

>>> empty_mapping[:]
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'
>>> empty_sequence[:]
EmptySequence()
>>> empty_three[:]
EmptyThree()


>>> bool(theEmptyThree)
False
>>> len(theEmptyThree)
0
>>> [*theEmptyThree]
[]
>>> [] in theEmptyThree
False
>>> hash(theEmptyThree) in [hash(id(theEmptyThree)), object.__hash__(theEmptyThree)]
True
>>> theEmptyThree == theEmptyThree
True
>>> theEmptyThree != theEmptyThree
False
>>> theEmptyThree == []
False
>>> theEmptyThree != []
True


>>> theEmptyThree.keys()
EmptySet()
>>> theEmptyThree.items()
EmptySet()
>>> theEmptyThree.values()
EmptyCollection()
>>> theEmptyThree.get([], 6)
6

>>> [*reversed(theEmptyThree)]
[]
>>> theEmptyThree.index(6)
Traceback (most recent call last):
    ...
ValueError: tuple.index(x): x not in tuple
>>> theEmptyThree.index(6, 0, 8)
Traceback (most recent call last):
    ...
ValueError: tuple.index(x): x not in tuple
>>> theEmptyThree.index(6, [])
Traceback (most recent call last):
    ...
TypeError: slice indices must be integers or have an __index__ method
>>> theEmptyThree.count(6)
0

>>> theEmptyThree['a']
Traceback (most recent call last):
    ...
TypeError: tuple indices must be integers or slices, not str
>>> theEmptyThree[0]
Traceback (most recent call last):
    ...
IndexError_KeyError: 0
>>> theEmptyThree[:]
EmptyThree()




>>> issubclass(EmptyHashableBase, Hashable)
True
>>> issubclass(EmptyIterable, Iterable)
True
>>> issubclass(EmptySized, Sized)
True
>>> issubclass(EmptyContainer, Container)
True
>>> issubclass(EmptyCollection, Collection)
True
>>> not issubclass(EmptyCollection, Reversible)
True
>>> issubclass(EmptyReversible, Reversible)
True


>>> issubclass(EmptySet, KeysView)
True
>>> issubclass(EmptySet, ItemsView)
True
>>> issubclass(EmptySet, Set)
True
>>> issubclass(EmptySet, MappingView)
True
>>> issubclass(EmptyCollection, ValuesView)
True
>>> issubclass(EmptyCollection, Collection)
True
>>> issubclass(EmptyCollection, MappingView)
True


>>> issubclass(EmptyMapping, Mapping)
True
>>> issubclass(EmptySet, Set)
True
>>> issubclass(EmptySequence, Sequence)
True

>>> issubclass(EmptyThree, Mapping)
True
>>> issubclass(EmptyThree, Set)
True
>>> issubclass(EmptyThree, Sequence)
True






>>> type(theEmptyHashableBase) is EmptyHashableBase
True
>>> type(theEmptyIterable) is EmptyIterable
True
>>> type(theEmptySized) is EmptySized
True
>>> type(theEmptyContainer) is EmptyContainer
True
>>> type(theEmptyCollection) is EmptyCollection
True
>>> type(theEmptyReversible) is EmptyReversible
True

>>> type(theEmptyMapping) is EmptyMapping
True
>>> type(theEmptySet) is EmptySet
True
>>> type(theEmptySequence) is EmptySequence
True
>>> type(theEmptyThree) is EmptyThree
True


>>> theEmptyHashableBase is EmptyHashableBase()
True
>>> theEmptyIterable is EmptyIterable()
True
>>> theEmptySized is EmptySized()
True
>>> theEmptyContainer is EmptyContainer()
True
>>> theEmptyCollection is EmptyCollection()
True
>>> theEmptyReversible is EmptyReversible()
True
>>> theEmptyMapping is EmptyMapping()
True
>>> theEmptySet is EmptySet()
True
>>> theEmptySequence is EmptySequence()
True
>>> theEmptyThree is EmptyThree()
True

>>> theEmptyHashableBase
EmptyHashableBase()
>>> theEmptyIterable
EmptyIterable()
>>> theEmptySized
EmptySized()
>>> theEmptyContainer
EmptyContainer()
>>> theEmptyCollection
EmptyCollection()
>>> theEmptyReversible
EmptyReversible()
>>> theEmptyMapping
EmptyMapping()
>>> theEmptySet
EmptySet()
>>> theEmptySequence
EmptySequence()
>>> theEmptyThree
EmptyThree()




>>> isinstance(empty_mapping, Mapping)
True
>>> isinstance(empty_set, Set)
True
>>> isinstance(empty_sequence, Sequence)
True


>>> isinstance(empty_three, Mapping)
True
>>> isinstance(empty_three, Set)
True
>>> isinstance(empty_three, Sequence)
True

>>> empty_mapping is theEmptyMapping
True
>>> empty_set is theEmptySet
True
>>> empty_sequence is theEmptySequence
True
>>> empty_three is theEmptyThree
True


#'''

__all__ = '''
    EmptyMapping
    EmptySet
    EmptySequence
        empty_mapping
        empty_set
        empty_sequence
    empty_tuple
    empty_iterator





    EmptyHashableBase
        EmptyIterable
            EmptyReversible
        EmptySized
        EmptyContainer
            EmptyCollection

    EmptyMapping
    EmptySet
    EmptySequence
        EmptyThree
            IndexError_KeyError

    theEmptyHashableBase
    theEmptyIterable
    theEmptySized
    theEmptyContainer
    theEmptyCollection
    theEmptyReversible
    theEmptyMapping
    theEmptySet
    theEmptySequence
    theEmptyThree

    empty_mapping
    empty_set
    empty_sequence
    empty_three
    empty_tuple
    empty_iterator
    '''.split()

from collections.abc import Mapping, Sequence, Set, Hashable, Collection, Reversible, Sized, Iterable, Container, MappingView, KeysView, ItemsView, ValuesView
from types import MappingProxyType
#import operator
#import builtins
from seed.tiny import null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter  #,    null_sequence, null_set, null_mapping
#
#from seed.abc.ISingleton import ISingleton
#   why not use ISingleton?
#       EmptyMapping is used in tiny
#           but now remove from seed.tiny!!
#
#from seed.types.AddrAsHash import AddrAsHash as EqById
#   why not use AddrAsHash?
#       let EmptyMapping be simple without ABC
#
#

#from seed.types.AddrAsHash import BaseAddrAsHash
from seed.abc.eq_by_id.BaseAddrAsHash import BaseAddrAsHash
from seed.helper.repr_input import repr_helper

class EmptyHashableBase(BaseAddrAsHash):
    r'''
EmptyBase:
    __repr__, __hash__, __eq__, __ne__, __bool__
    ~~~~~~~
    __iter__
    __len__
    __contains__
Container
    __contains__
Hashable
    __hash__
Iterable
    __iter__
Reversible
    Iterable
    __reversed__
Sized
    __len__
Collection
    #Sized, Iterable, Container
    __contains__, __iter__, __len__
Mapping:
    __getitem__, __iter__, __len__
    =======
    __contains__, keys, items, values, get, __eq__, and __ne__
    ==>> required:
    keys, items, values, get
Set:
    __contains__, __iter__, __len__
    =======
    __le__, __lt__, __eq__, __ne__, __gt__, __ge__, __and__, __or__, __sub__, __xor__, and isdisjoint
    ==>> required:
    __le__, __lt__, __gt__, __ge__, __and__, __or__, __sub__, __xor__, isdisjoint
Sequence:
    __getitem__, __len__
    =======
    __contains__, __iter__, __reversed__, index, and count
    ==>> required:
    __getitem__, __reversed__, index, count


.register:
MappingView
    Sized
    __len__

ItemsView
    MappingView, Set
    __contains__, __iter__

KeysView
    MappingView, Set
    __contains__, __iter__

ValuesView
    MappingView, Collection
    __contains__, __iter__
    #'''
    __slots__ = ()
    if 0:
        _as_type = None
        def __new__(cls, /, *args, **kwargs):
            #if cls is not __class__:raise TypeError
            #if kwargs: raise TypeError
            if args or kwargs:
                empty_container = __class__._as_type(*args, **kwargs)
                if len(empty_container): raise TypeError

    def __new__(cls, /, *tmay_iterable):
        if tmay_iterable:
            if len(tmay_iterable) >= 2: raise logic-err
            [iterable] = tmay_iterable
            for _ in iterable: raise TypeError
            del iterable
        try:
            #cls tower!!! bug: sf = cls.the_instance
            #
            #sf = cls.__dict__[cls]
            sf = cls.__dict__['the_instance']
        #except AttributeError:
        except KeyError:
            #cls.the_instance = super(__class__, cls).__new__(cls)
            cls.the_instance = object.__new__(cls)
            #cls.__dict__[cls] = object.__new__(cls)
            #    #TypeError: 'mappingproxy' object does not support item assignment
            sf = cls()
        assert sf is cls.the_instance
        #assert sf is cls.__dict__[cls]
        if not type(sf) is cls:raise TypeError
        return sf

    r'''
    if 0:
      def __new__(cls, /, *args, **kwargs):
        global empty_mapping
        if cls is not __class__:raise TypeError
        if kwargs: raise TypeError
        d = dict(*args, **kwargs)
        if d: raise TypeError
        try:
            return empty_mapping
        except NameError:
            empty_mapping = super(cls, __class__).__new__(cls)
        return empty_mapping
    #'''

    def __setattr__(sf, attr, obj, /):
        raise AttributeError
    def __delattr__(sf, attr, /):
        raise AttributeError
    r'''
    if 0:
      def __getattribute__(sf, attr, /):
        if attr == '__dict__':
            return empty_mapping
        return super().__getattribute__(attr)
    #'''

    r'''
    def __eq__(sf, other, /):
        return type(sf) is type(other)
    def __hash__(sf, /):
        return id(sf)
    cmp with other mapping??? hashable???

    now use BaseAddrAsHash
    #'''
    def __repr__(sf, /):
        return repr_helper(sf)
    __bool__ = None

class EmptyIterable(EmptyHashableBase):
    __slots__ = ()
    def __iter__(sf, /):
        return empty_iterator
class EmptySized(EmptyHashableBase):
    __slots__ = ()
    def __len__(sf, /):
        return 0
    def __bool__(sf, /):
        return False
class EmptyContainer(EmptyHashableBase):
    __slots__ = ()
    def __contains__(sf, key, /):
        return False
class EmptyCollection(EmptyIterable, EmptySized, EmptyContainer):
    __slots__ = ()
class EmptyReversible(EmptyIterable):
    __slots__ = ()
    def __reversed__(sf, /):
        return empty_iterator
    EmptyIterable.__iter__, __reversed__
assert issubclass(EmptyHashableBase, Hashable)
assert issubclass(EmptyIterable, Iterable)
assert issubclass(EmptySized, Sized)
assert issubclass(EmptyContainer, Container)
assert issubclass(EmptyCollection, Collection)
assert not issubclass(EmptyCollection, Reversible)
assert issubclass(EmptyReversible, Reversible)


#class EmptyMapping(Mapping):
class EmptyMapping(EmptyCollection):
    __slots__ = ()
    #_as_type = dict
    def __getitem__(sf, key, /):
        return null_mapping_view[key]
        raise KeyError(key)
    def keys(sf, /):
        return empty_set
    def items(sf, /):
        return empty_set
    def values(sf, /):
        return theEmptyCollection
        return empty_set
    def get(sf, key, /, default=None):
        return default
    keys, items, values, get

def _op(sf, ot, result, /):
    if ot is not sf: raise TypeError
    return result
class EmptySet(EmptyCollection):
    __slots__ = ()
    #_as_type = set
    def __le__(sf, ot, /):
        return _op(sf, ot, True)
    def __lt__(sf, ot, /):
        return _op(sf, ot, False)
    __ge__ = __le__
    __gt__ = __lt__
    #isdisjoint = __le__
    def isdisjoint(sf, ot, /):
        return null_frozenset.isdisjoint(ot)

    def __and__(sf, ot, /):
        return _op(sf, ot, sf)
    __or__ = __and__
    __sub__ = __and__
    __xor__ = __and__

    __le__, __lt__, __gt__, __ge__, __and__, __or__, __sub__, __xor__, isdisjoint


class EmptySequence(EmptyReversible, EmptyCollection):
    __slots__ = ()
    #_as_type = tuple
    #def __reversed__(sf, /):
    def __getitem__(sf, i_or_slice, /):
        empty_tuple[i_or_slice]
        return sf
        raise IndexError
    def index(sf, /, *args, **kwargs):
        return empty_tuple.index(*args, **kwargs)
        raise IndexError
    def count(sf, /, *args, **kwargs):
        return empty_tuple.count(*args, **kwargs)
    __getitem__, EmptyReversible.__reversed__, index, count

class IndexError_KeyError(IndexError, KeyError, LookupError):pass
class EmptyThree(EmptySequence, EmptySet, EmptyMapping):
    def __getitem__(sf, i_or_slice, /):
        try:
            empty_tuple[i_or_slice]
        except LookupError:
            raise IndexError_KeyError(i_or_slice)
        return sf


theEmptyHashableBase = EmptyHashableBase()
theEmptyIterable = EmptyIterable()
theEmptySized = EmptySized()
theEmptyContainer = EmptyContainer()
theEmptyCollection = EmptyCollection()
theEmptyReversible = EmptyReversible()

theEmptyMapping = EmptyMapping()
theEmptySet = EmptySet()
theEmptySequence = EmptySequence()
theEmptyThree = EmptyThree()



assert type(theEmptyHashableBase) is EmptyHashableBase
assert type(theEmptyIterable) is EmptyIterable
assert type(theEmptySized) is EmptySized
assert type(theEmptyContainer) is EmptyContainer
assert type(theEmptyCollection) is EmptyCollection
assert type(theEmptyReversible) is EmptyReversible

assert type(theEmptyMapping) is EmptyMapping
assert type(theEmptySet) is EmptySet
assert type(theEmptySequence) is EmptySequence
assert type(theEmptyThree) is EmptyThree


assert theEmptyHashableBase is EmptyHashableBase()
assert theEmptyIterable is EmptyIterable()
assert theEmptySized is EmptySized()
assert theEmptyContainer is EmptyContainer()
assert theEmptyCollection is EmptyCollection()
assert theEmptyReversible is EmptyReversible()
assert theEmptyMapping is EmptyMapping()
assert theEmptySet is EmptySet()
assert theEmptySequence is EmptySequence()
assert theEmptyThree is EmptyThree()





if 1:
    #tmp
    assert not issubclass(EmptyMapping, Mapping)


#MappingView.register(EmptyMapping)
KeysView.register(EmptySet)
ItemsView.register(EmptySet)
ValuesView.register(EmptyCollection)
assert issubclass(EmptySet, KeysView)
assert issubclass(EmptySet, ItemsView)
assert issubclass(EmptySet, Set)
assert issubclass(EmptySet, MappingView)
assert issubclass(EmptyCollection, ValuesView)
assert issubclass(EmptyCollection, Collection)
assert issubclass(EmptyCollection, MappingView)



Mapping.register(EmptyMapping)
Set.register(EmptySet)
Sequence.register(EmptySequence)
assert issubclass(EmptyMapping, Mapping)
assert issubclass(EmptySet, Set)
assert issubclass(EmptySequence, Sequence)

if 0:
    Mapping.register(EmptyThree)
    Set.register(EmptyThree)
    Sequence.register(EmptyThree)
assert issubclass(EmptyThree, Mapping)
assert issubclass(EmptyThree, Set)
assert issubclass(EmptyThree, Sequence)




empty_mapping = EmptyMapping()
empty_set = EmptySet()
empty_sequence = EmptySequence()
assert isinstance(empty_mapping, Mapping)
assert isinstance(empty_set, Set)
assert isinstance(empty_sequence, Sequence)

empty_three = EmptyThree()
assert isinstance(empty_three, Mapping)
assert isinstance(empty_three, Set)
assert isinstance(empty_three, Sequence)

assert empty_mapping is theEmptyMapping
assert empty_set is theEmptySet
assert empty_sequence is theEmptySequence
assert empty_three is theEmptyThree





empty_tuple = null_tuple
empty_iterator = null_iter  #iter(empty_tuple) #iter('')


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


