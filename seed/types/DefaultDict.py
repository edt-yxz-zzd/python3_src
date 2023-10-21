
__all__ = '''
    DefaultDict2

    DefaultDict
    curryDefaultDict
'''.split()

from collections.abc import MutableMapping

curryDefaultDict = lambda mapping: lambda default_factory:\
                     DefaultDict(mapping, default_factory)
class DefaultDict(MutableMapping):
    def __init__(self, mapping, default_factory):
        self.mapping = mapping
        self.default_factory = type(None) if default_factory is None \
                               else default_factory

    def __missing__(self, key):
        self[key] = self.default_factory()
        return self.mapping[key]
        raise KeyError(key)
    def __getitem__(self, key):
        try:
            return self.mapping[key]
        except KeyError:
            return type(self).__missing__(self, key)
    def __setitem__(self, key, value):
        self.mapping[key] = value
    def __delitem__(self, key):
        del self.mapping[key]

    def __iter__(self):
        return iter(self.mapping)
    def __len__(self):
        return len(self.mapping)


del MutableMapping

class DefaultDict2(DefaultDict):
    def __init__(self, mapping, ncall, value_mkr, /, *ex_args):
        assert type(ncall) is int
        assert -1 <= ncall <= 2
        #assert (not ncall == -1) or (not ex_args)
        assert not (ncall == -1 and ex_args)
        self.mapping = mapping
        self.ncall = ncall
        self.value_mkr = value_mkr
        self.ex_args = ex_args


    def _key2value_(self, key):
        ncall = self.ncall
        value_mkr = self.value_mkr
        ex_args = self.ex_args
        if ncall == -1:
            v = value_mkr
        else:
            args = [self, key][2-ncall:]
            v = value_mkr(*args, *ex_args)
        return v

    def __missing__(self, key):
        self[key] = self._key2value_(key)
        return self.mapping[key]
        raise KeyError(key)

    def __getitem__(self, key):
        try:
            return self.mapping[key]
        except KeyError:
            return type(self).__missing__(self, key)
    def __setitem__(self, key, value):
        self.mapping[key] = value
    def __delitem__(self, key):
        del self.mapping[key]

    def __iter__(self):
        return iter(self.mapping)
    def __len__(self):
        return len(self.mapping)

    def __contains__(self, key):
        return key in self.mapping
    def __eq__(self, other):
        if not isinstance(other, __class__):
            return NotImplemented
        return self.mapping == other.mapping
        return self.default_factory == other.default_factory and self.mapping == other.mapping
    def __reversed__(self):
        return reversed(self.mapping)
    #def __repr__(self):

    def clear(sf, /):
        sf.mapping.clear()
    #def copy(sf, /):
    #def default_factory(sf, /):
    #def fromkeys(sf, /):
    def get(sf, k, default=None, /):
        return sf.mapping.get(k, default)
    def items(sf, /):
        return sf.mapping.items()
    def keys(sf, /):
        return sf.mapping.keys()
    def pop(sf, k, /, *tmay_default):
        return sf.mapping.pop(k, *tmay_default)
    def popitem(sf, /):
        return sf.mapping.popitem()
    def setdefault(sf, k, default=None, /):
        return sf.mapping.setdefault(k, default)
    def update(sf, /, *tmay_other, **kwds):
        sf.mapping.update(*tmay_other, **kwds)
    def values(sf, /):
        return sf.mapping.values()



r'''
>>> from collections import defaultdict as d
>>> d(int).__missing__(99)
0
>>> dir(d)
['__class__', '__class_getitem__', '__contains__', '__copy__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__missing__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'default_factory', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
#'''


from seed.types.DefaultDict import DefaultDict, curryDefaultDict
from seed.types.DefaultDict import DefaultDict2
from seed.types.DefaultDict import *
