
'''
diff with collections.OrderedDict
    see: seed.types.OrderedSet
hash algo:
    see: seed.types.FrozenDict.mapping_hash

'''

from collections.abc import Mapping, MutableMapping, Hashable
from seed.types.OrderedSet import _Node, OrderedSet, FrozenOrderedSet
from seed.lang.class_property import class_property

class _Node(_Node):
    @classmethod
    def entity2key(cls, entity):
        key, value = entity
        return key

class _OrderedSet(OrderedSet):
    __RBT_Node__ = _Node
class _FrozenOrderedSet(FrozenOrderedSet):
    __RBT_Node__ = _Node


class _OrderedMap(Mapping):
    @class_property
    def PLAIN_NODE_AND_SIZE(cls):
        return cls.__underlying_OrderedSet__.PLAIN_NODE_AND_SIZE
    __underlying_OrderedSet__ = _FrozenOrderedSet
    def __init__(self, iterable = (), *, constructor_case = None):
        Set = type(self).__underlying_OrderedSet__
        Node = Set.__RBT_Node__

        it = None
        if constructor_case is None:
            # iterable or mapping
            if isinstance(iterable, __class__):
                other = iterable
                it = other.__set
            elif isinstance(iterable, Mapping):
                it = iterable.items()
            # else: it = ((a,b) for a,b in iterable)

        if it is None:
            it = iterable
        self.__set = Set(it, constructor_case = constructor_case)


    def __getitem__(self, key):
        k, v = entity = self.__set.get_entity(key)
        return v
    def __iter__(self):
        return (k for k, v in self.__set)
    def __reversed__(self):
        return (k for k, v in reversed(self.__set))
    def __len__(self):
        return len(self.__set)

    def get_states(self):
        return self.__set.get_states()
    def __set_states(self, states):
        self.__set.set_states(states)
    @classmethod
    def from_states(cls, states):
        plain_node, size = states
        return cls((plain_node, size),
                   constructor_case = __class__.PLAIN_NODE_AND_SIZE)
    @classmethod
    def from_iterable(cls, iterable):
        return cls(iterable)
    def copy(self):
        return cls(self)
    def __repr__(self):
        return repr_helper(self,
                           self.get_states(),
                           constructor_case = __class__.PLAIN_NODE_AND_SIZE)
    def __str__(self):
        return repr_helper(self, list(self.items()))

    def _hash(self):
        return hash(self.__set)


class FrozenOrderedMap(_OrderedMap, Hashable):
    def __init__(self, iterable = (), *, constructor_case = None):
        self.__set = None
        _OrderedMap.__init__(self, iterable, constructor_case = constructor_case)
        
    @property
    def _OrderedMap__set(self):
        return self.__set
    @_OrderedMap__set.setter
    def _OrderedMap__set(self, s):
        if self.__set is not None:
            raise AttributeError('not writable')
        # initial
        self.__set = s

    def __hash__(self):
        return self._hash()

class OrderedMap(_OrderedMap, MutableMapping):
    __underlying_OrderedSet__ = _OrderedSet
    # self.__set ==>> self._OrderedMap__set
    def __setitem__(self, key, value):
        self.__set.update_add((key, value))
    def __delitem__(self, key):
        self.__set.remove(key)
    def set_states(self, states):
        return self.__set_states(states)


d = OrderedMap(dict(a=1, b=2, c=3))
d['c']=4
del d['a']
assert d == {'b':2, 'c':4}
dd = d.from_states(d.get_states())
assert dd == d
dd.set_states(d.get_states())
assert dd == d










