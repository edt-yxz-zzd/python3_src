
'''
ReadOnly mapping ==>> MappingProxyType
Hashable mapping ==>> FrozenDict
KeysImmutable mapping ==>> HalfFrozenDict
'''


__all__ = '''
    mapping_hash
    FrozenDict
    HalfFrozenDict

    HashableMapping
'''.split()


from types import MappingProxyType
from collections.abc import Mapping, Set, Hashable

def mapping_hash(mapping):
    'like Set._hash; to provide a std algo for all mapping'
    return hash(__Mapping2Set_for_hash(mapping))
class __Mapping2Set_for_hash(Set):
    'make a tmp obj to compute hash'
    def __init__(self, d):
        self.__d = d
    def __hash__(self):
        return self._hash()
    @classmethod
    def _from_iterable(cls, it):
        return frozenset(it) 
    def __contains__(self, x):
        if type(x) is tuple and len(x) == 2:
            k, v = x
            if k in x and v == x[k]:
                return True
        return False
    def __iter__(self):
        return ((a, b) for a, b in self.__d.items())
    def __len__(self):
        return len(self.__d)



class HashableMapping(Mapping, Hashable):
    'requires: __hash__, __getitem__, __iter__, and __len__'
    def _hash(self):
        # since __hash__ may not be inherited
        return mapping_hash(self)


class __Dict(Mapping):
    'should not reassigned .__d!'
    def __init__(self, d):
        assert type(d) is dict
        self.__d = d
    def __getitem__(self, key):
        return self.__d[key]
    def __iter__(self):
        return iter(self.__d)
    def __len__(self):
        return len(self.__d)

    def __eq__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        if isinstance(other, __class__):
            return self.__d == other.__d
        elif len(self) != len(other):
            return False
        return self.__d == dict(other)
    def __ne__(self, other):
        return self != other



class FrozenDict(__Dict, HashableMapping):
    'should not modify .__d!'
    def __init__(self, iterable_or_mapping=(), **kwargs):
        if not kwargs and isinstance(iterable_or_mapping, __class__):
            # bug: d = iterable_or_mapping.__d
            d = iterable_or_mapping._Dict__d
        else:
            d = dict(iterable_or_mapping, **kwargs)
        super().__init__(d)
        self.__hash = None
    def __hash__(self):
        if self.__hash is None:
            self.__hash = self._hash()
        return self.__hash

class HalfFrozenDict(__Dict):
    def __init__(self, iterable_or_mapping=(), **kwargs):
        d = dict(iterable_or_mapping, **kwargs)
        super().__init__(d)
    def __setitem__(self, key, value):
        if key not in self:
            raise KeyError('only existing key can be used to set item')

        self._Dict__d[key] = value
        # why _Dict__d!!
        #   getattr(self, '___Dict__d')[key] = value


{FrozenDict({1:2, 3:3})}
hd = HalfFrozenDict(a=1, b=2)
hd['a'] = 3
try:
    hd[''] = 4
except KeyError:pass
else: raise ...










if 0:

    '''
    # fail
    if use frozenset to implement frozendict
        then we need get element in set
        since that is not a std interface
        it would be an O(n) operation; e.g. next(set - (set - {elem}))
        


    '''



    class SetElemGetter:
        '''to find object in a set
    usage:
        getter = SetElemGetter(a)
        if getter in set:
            assert getter.gots
            for a in gots:
                return a
    '''
        def __init__(self, elem):
            if isinstance(elem, __class__):
                elem = elem.elem
                assert not isinstance(elem, __class__)
            self.elem = elem
            self.gots = []
        def __eq__(self, other):
            if isinstance(elem, __class__):
                other = other.elem
                assert not isinstance(other, __class__)
            if self.elem == other:
                self.gots.append(other)
                return True
            return False
        def __ne__(self, other):
            return not self == other
        def __hash__(self):
            return hash(self.elem)

    def find_object_in_set(set, key):
        # the only way is (s-(s-k))
        # fail
        raise
        getter = SetElemGetter(a)
        if getter in set:
            assert getter.gots
            # but what if set call a==a??
            # what if x.__eq__(a) raise/return False instead of NotImplemented??
            for b in gots:
                if b is not a:
                    return b
                










