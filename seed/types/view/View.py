
r'''

from seed.types.view.View import MapView

#'''

__all__ = '''
    MapView
    MapViewBase
    SetView
    SeqView
    '''.split()

from collections.abc import Set, Sequence, Mapping
from seed.helper.repr_input import repr_helper
from types import MappingProxyType as MapView
from seed.abc.IReprHelper import IReprHelper

class MapViewBase(Mapping):
    # MappingProxyType can not be base type
    # 'immutable; .__d should not be assigned again!'
    __slots__ = ('__d',)
    def __init__(self, mapping):
        if not isinstance(mapping, Mapping):
            raise TypeError('not a mapping')
        if isinstance(mapping, __class__):
            # since immutable, we can use the underly object directly
            mapping = mapping.__d
            assert not isinstance(mapping, __class__)
        self.__d = mapping
    @classmethod
    def _from_iterable(cls, it):
        return cls(dict(it))
    def __contains__(self, x):
        return x in self.__d
    def __eq__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        if isinstance(other, __class__):
            other = other.__d
            assert not isinstance(other, __class__)
        try:
            return self.__d == other
        except:
            return super().__eq__(other)

    def __repr__(self):
        return repr_helper(self, self.__d)
    def __getitem__(self, key):
        return self.__d[key]
    def __iter__(self):
        return iter(self.__d)
    def __len__(self):
        return len(self.__d)
    def keys(self):
        return self.__d.keys()
    def values(self):
        return self.__d.values()
    def items(self):
        return self.__d.items()
    def get(self, key, default=None):
        return self.__d.get(key, default)

class SetView(Set):
    'immutable; .__s should not be assigned again!'
    __slots__ = ('__s',)
    def __init__(self, set_obj):
        if not isinstance(set_obj, Set):
            raise TypeError('not a set')
        if isinstance(set_obj, __class__):
            # since immutable, we can use the underly object directly
            set_obj = set_obj.__s
            assert not isinstance(set_obj, __class__)
        self.__s = set_obj
    @classmethod
    def _from_iterable(cls, it):
        # since nobody can access the underly set
        # we use frozenset instead
        return frozenset(it) 
    def __contains__(self, x):
        return x in self.__s
    def __iter__(self):
        return iter(self.__s)
    def __len__(self):
        return len(self.__s)
    def __le__(self, other):
        if not isinstance(other, Set):
            return NotImplemented
        if isinstance(other, __class__):
            other = other.__s
            assert not isinstance(other, __class__)
        try:
            return self.__s <= other
        except:
            return super().__le__(other)

    def __repr__(self):
        return repr_helper(self, self.__s) # ? set(self.__s)

#class SeqView(IReprHelper, Sequence):
class SeqView(Sequence):
    'immutable; .__s should not be assigned again!'
    __slots__ = ('__s',)
    '''
    def ___get_args_kwargs___(self):
        # for repr
        return (self.__s,), {}
    '''

    def __init__(self, seq):
        if not isinstance(seq, Sequence):
            raise TypeError('not a seq')
        if isinstance(seq, __class__):
            seq = seq.__s
            assert not isinstance(seq, __class__)
        self.__s = seq

    #def __getitem__(self, i): return self.__s.__getitem__(i)
    def __repr__(self):
        return repr_helper(self, self.__s) # ? list(self.__s)

    @classmethod
    def from_sequence(cls, seq): return cls(seq)
    def __getitem__(self, i):
        r = self.__s[i]
        t = type(i)
        if t is slice or isinstance(i, Sequence):
            if isinstance(r, Sequence):
                return type(self).from_sequence(r)
        return r


    def __len__(self):
        return len(self.__s)
    def __contains__(self, x):
        return x in self.__s
    def __iter__(self):
        return iter(self.__s)
    def __reversed__(self):
        return reversed(self.__s)
    def index(self, *args):
        return self.__s.index(*args)
    def count(self, *args):
        return self.__s.count(*args)





