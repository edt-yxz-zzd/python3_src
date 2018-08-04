

'''
IOverwritableFactory/OverwritableFactory__seq
    used in xgraph vtx2data/aedge2data

if key was BoundedUint, then we use array
if key was Hashable, then we use dict
if key was Node, then
    # Node instead of Vertex
    # Vertex contains no data
    # Node is more complicate
    assume:
        Node.get_buffer() -> list[a]
        Node.alloc() -> idx # idx of buffer
        Node.free(idx)
    each mapping alloc an same idx for all nodes of a graph
    when this mapping __del__, free the idx
'''


__all__ = '''
    IMappingOps
        IIterKeys
            IStaticKeys
        IFullMapping
            IStaticKeys
                IFromKey2Value
                    IOverwritableFactory

        IMutableMappingOps
            IInsertNewItem
                ISetItem
            IOverwriteItem
                ISetItem
                IOverwritableFactory
                    OverwritableFactory__seq
                    OverwritableFactory__mapping

    '''.split()



from typing import (
    TypeVar, Generic, Sequence, Mapping, MutableMapping, MutableSequence
    , Callable, Iterable as Iter, Union, Tuple, Type)
from abc import abstractmethod
#from numbers import Integral
# mapping_ops.py:156: error: No overload variant of "__getitem__" of "Sequence" matches argument types [numbers.Integral]
Integral = int


K = TypeVar('K')
V = TypeVar('V')
M = TypeVar('M')
N = TypeVar('N')
T = TypeVar('T')
R = TypeVar('R')

snd = lambda x:x[1]
# Maybe V = Tuple[] | Tuple[V]
#)->Union[Tuple[()], Tuple[V]]:
#)->Sequence[V]
Maybe = Sequence
def Just(x:T)->Tuple[T]:
    return (x,)
#Nothing : "Tuple[]" = ()
#Nothing : Type[()] = ()
Nothing : Tuple[()] = ()


'''
class IGetItem(Generic[K, V]):
    # no: __iter__, __contain__, __len__, __bool__
    # has: __getitem__
    @abstractmethod
    def __getitem__(self, __key:K) -> V:
        # raise LookupError if no found
        raise NotImplementedError
'''

class IMappingOps(Generic[M, K, V]):
    @abstractmethod
    def get_or_raise(self, __map:M, __key:K) -> V:
        # raise LookupError if no found
        raise NotImplementedError
    def get_or_default(self, __map:M, __key:K, __default:V) -> V:
        return self.get_or_fdefault(__map, __key, lambda: __default)
    def fget_or_default(self, __map:M, __key:K
            , __fthen:Callable[[V], R]
            , __default:R) -> R:
        return self.get_then_else(__map, __key, __fthen, lambda: __default)
    def get_or_fdefault(self, __map:M, __key:K, __fdefault:Callable[[], V]) -> V:
        return self.get_then_else(__map, __key, lambda v:v, __fdefault)

    def get_then_else(self, __map:M, __key:K
            , __fthen:Callable[[V], R]
            , __felse:Callable[[], R]) -> R:
        return self.get_thenKV_elseK(__map, __key
                    , lambda k,v: __fthen(v), lambda k: __felse())
    def get_thenKV_elseK(self, __map:M, __key:K
            , __fthen:Callable[[K,V], R]
            , __felse:Callable[[K], R]) -> R:
        try:
            v = self.get_or_raise(__map, __key)
        except LookupError:
            return __felse(__key)
        else:
            return __fthen(__key, v)
        pass



class IIterKeys(IMappingOps[M,K,V]):
    @abstractmethod
    def iter_keys(self, __map:M) -> Iter[K]:
        raise NotImplementedError
    def iter_values(self, __map:M) -> Iter[V]:
        return map(snd, self.iter_items(__map))
    def iter_items(self, __map:M) -> Iter[Tuple[K,V]]:
        for k in self.iter_keys(__map):
            yield k, self.get_or_raise(__map, k)
class IFullMapping(IMappingOps[M,K,V]):
    # the only possible mutable method is overwrite existed key
    # cannot delete key or insert new key
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if issubclass(cls, (IDelItem, IInsertNewItem)):
            raise TypeError('overwrite is the only mutable method')
    pass
class IStaticKeys(IFullMapping[M,K,V], IIterKeys[M,K,V]):
    # keys are known static
    @abstractmethod
    def static_iter_keys(self) -> Iter[K]:
        raise NotImplementedError
    @abstractmethod
    def static_size(self)->Integral:
        raise NotImplementedError
    def iter_keys(self, __map:M) -> Iter[K]:
        return self.static_iter_keys()
class IFromKey2Value(IStaticKeys[M,K,V]):
    # constructor
    @abstractmethod
    def from_key2value(self, __key2value:Callable[[K], V]) -> M:
        raise NotImplementedError


class IMutableMappingOps(IMappingOps[M, K, V]):pass
class IDelItem(IMutableMappingOps[M, K, V]):
    @abstractmethod
    def del_item(self, __map:M, __key:K)->None:
        # raise LookupError if no found
        raise NotImplementedError
    def discard_item(self, __map:M, __key:K)->None:
        try:
            self.del_item(__map, __key)
        except LookupError: pass
        return
    def pop_value(self, __map:M, __key:K)->V:
        # raise LookupError if no found
        v = self.get_or_raise(__map, __key)
        self.del_item(__map, __key)
        return v
    def pop_may_value(self, __map:M, __key:K
            # Maybe V = Tuple[] | Tuple[V]
            #)->Union[Tuple[()], Tuple[V]]:
            )->Maybe[V]:
        return self.fget_or_default(__map, __key, Just, ())


class IOverwriteItem(IMutableMappingOps[M, K, V]):
    @abstractmethod
    def overwrite_item(self, __map:M, __key:K, __val:V)->None:
        # raise LookupError if no found
        raise NotImplementedError
    def imodify(self, __map:M, __key:K
        , __transform : Callable[..., V] # Callable[[V,...], V]
        , *args:object, **kwargs:object) -> V:
        val = self.get_or_raise(__map, __key)
        val = __transform(val, *args, **kwargs)
        self.overwrite_item(__map, __key, val)
        return val

class IInsertNewItem(IMutableMappingOps[M, K, V]):
    @abstractmethod
    def insert_new_item(self, __map:M, __key:K, __val:V)->None:
        # raise LookupError if found
        raise NotImplementedError

class ISetItem(IInsertNewItem[M,K,V], IOverwriteItem[M,K,V]):
    def set_item(self, __map:M, __key:K, __val:V)->None:
        try:
            self.overwrite_item(__map, __key, __val)
        except LookupError:
            self.insert_new_item(__map, __key, __val)
        return



################
# IFromKey2Value + IOverwriteItem
class IOverwritableFactory(IOverwriteItem[M,K,V], IFromKey2Value[M,K,V]):
    pass


#Seq = TypeVar('Seq', MutableSequence, MutableSequence)
Seq = MutableSequence[V]
class OverwritableFactory__seq(
        IOverwritableFactory[Seq, Integral,V]):
    def __init__(self
            , __length:Integral
            , __seq_constructor : Callable[[Iter[V]], Seq]=list
        ) ->None:
        if __length < 0: raise ValueError
        self.__length = __length
        self.__seq_constructor = __seq_constructor
    def get_or_raise(self, __map:Seq, __key:Integral) -> V:
        if __key < 0: raise IndexError
        return __map[__key]
    def static_iter_keys(self) -> Iter[Integral]:
        return range(self.__length)
    def static_size(self)->Integral:
        return self.__length
    def from_key2value(self, __key2value:Callable[[Integral], V]
            ) -> Seq:
        return self.__seq_constructor(
            map(__key2value, self.static_iter_keys()))

    def overwrite_item(self, __map:Seq
            , __key:Integral, __val:V)->None:
        if __key < 0: raise IndexError
        __map[__key] = __val


#Map = TypeVar('Map', MutableMapping[K,V], MutableMapping[K,V])
#Map = TypeVar('Map', MutableMapping, MutableMapping)
Map = MutableMapping[K,V]
class OverwritableFactory__mapping(
        IOverwritableFactory[Map, K,V]):
    def __init__(self, __keys:Iter[K]
            , __mapping_constructor
                : Callable[[Iter[Tuple[K,V]]], Map] =dict
        ) ->None:
        self.__keys = tuple(__keys)
        self.__mapping_constructor = __mapping_constructor
    def get_or_raise(self, __map:Map, __key:K) -> V:
        return __map[__key]
    def static_iter_keys(self) -> Iter[K]:
        return iter(self.__keys)
    def static_size(self)->Integral:
        return len(self.__keys)
    def from_key2value(self, __key2value:Callable[[K], V]
            ) -> Map:
        return self.__mapping_constructor(
            (k, __key2value(k)) for k in self.static_iter_keys())

    def overwrite_item(self, __map:Map
            , __key:K, __val:V)->None:
        if __key in __map: raise KeyError('already existed')
        __map[__key] = __val


