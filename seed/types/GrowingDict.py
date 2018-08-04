

__all__ = '''
    GrowingDict
    GrowingDictView
    '''.split()

from collections.abc import MutableMapping, Mapping
#from types import MappingProxyType
from .View import MapViewBase


class GrowingDict(Mapping):
    # grow only
    # no: __delitem__, pop, popitem, clear
    # __setitem__/update: not allow override existed keys
    def __init__(self, iterable_or_mapping = {}, **kwargs):
        d = iterable_or_mapping
        if not isinstance(d, Mapping):
            d = list(d)
        L = len(d)
        d = dict(d) # copy
        d.update(kwargs) # make sure order
        if len(d) != L + len(kwargs):
            raise KeyError('key duplicated')

        self.__d = d

    def __eq__(self, other):
        if isinstance(other, __class__):
            return self.__d == other.__d
        return self.__d == other
    def __ne__(self, other):
        return not (self == other)
    def __contains__(self, key):
        return key in self.__d
    def __getitem__(self, key):
        return self.__d[key]
    def __setitem__(self, key, value):
        if key in self.__d: raise KeyError(f'{key} existed!')
        self.__d[key] = value
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
    def setdefault(self, key, default=None):
        return self.__d.setdefault(key, default)
    def update(self, other, **kwargs):
        other = __class__(other, **kwargs)
        if set(self) & set(other): raise KeyError('key duplicated')
        self.__d.update(other.__d)
        return
        ####
        if isinstance(other, Mapping):
            other = other.items()
        for key, value in other: self[key] = value
        for key, value in kwargs.items(): self[key] = value


class GrowingDictView(MapViewBase):
    # grow only; read-only
    # no: __delitem__, pop, popitem, clear
    # no: __setitem__, update
    def __init__(self, growing_dict = {}, **kwargs):
        if type(growing_dict) not in [GrowingDictView, GrowingDict]: raise TypeError
        super().__init__(growing_dict)
        return

