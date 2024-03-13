#__all__:goto
r'''
ReadOnly mapping ==>> MappingProxyType
    mapping view
    not hashable
Hashable mapping ==>> FrozenDict
    like tuple, hashable iff all elements hashable
KeysImmutable mapping ==>> HalfFrozenDict
    like list with fixed len
    frozen keys
    not hashable

py -m seed.types.FrozenDict

see:
    view ../../python3_src/seed/types/DictWithNewProtocol.py
    view ../../python3_src/seed/types/FrozenDict.py
'''#'''


__all__ = '''
    mapping_hash
    FrozenDict
        mk_FrozenDict
        empty_FrozenDict
    HalfFrozenDict
        mk_HalfFrozenDict
        empty_HalfFrozenDict

    HashableMapping
'''.split()


from seed.helper.repr_input import repr_helper_ex
from seed.helper.repr_input import repr_helper
from types import MappingProxyType
from collections.abc import Mapping, Set, Hashable
import itertools

def __():
    'logic-err:HalfFrozenDict is Mutable, except empty_HalfFrozenDict'
    _Types = (FrozenDict, HalfFrozenDict)
    def mk_HalfFrozenDict(mapping_or_pairs=(), /, **kwargs):
        if not kwargs and type(mapping_or_pairs) in _Types:
            d = mapping_or_pairs
        else:
            d = HalfFrozenDict(mapping_or_pairs, **kwargs)
        assert type(d) in _Types

        if not d:
            d = empty_HalfFrozenDict
        assert type(d) in _Types
        return d



def __():
    'now using __new__'
    def mk_FrozenDict(mapping_or_pairs=(), /, **kwargs):
        if not kwargs and type(mapping_or_pairs) is FrozenDict:
            d = mapping_or_pairs
        else:
            d = FrozenDict(mapping_or_pairs, **kwargs)
        assert type(d) is FrozenDict

        if not d:
            d = empty_FrozenDict
        assert type(d) is FrozenDict
        return d

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

def check_tmay(x):
    if not type(x) is tuple: raise TypeError
    if not len(x) <= 1: raise TypeError

def _set_tm(d, k, tm):
    check_tmay(tm)
    if tm:
        [d[k]] = tm
    else:
        del d[k]

def default_init(k, a, /):
    return (a,)
def default_on_left_only(k, r, /):
    return (r,)
def default_on_right_only(k, b, /):
    return (b,)
def default_on_both(k, r, b, /):
    return (b,)

class __Dict(Mapping):
    'should not reassigned .__d!'
    def __new__(cls, d, /):
        self = super(__class__, cls).__new__(cls)
        self.__init(d)
        return self
    #def __init__(self, d, /):
    def __init(self, d, /):
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
        #bug:return self != other
        return not self == other
    def __repr__(self):
        return repr_helper(self, {**self})
        #return repr_helper_ex('mk_GetArgsKwargs', self.args, [], self.kwargs, name_only=True)
    def iupdates_ex(self, mappings, /,*, init, on_left_only, on_right_only, on_both):
        r'''
        :: {k:a} -> Iter {k:b} -> (init::None|(k->a->tmay r)) -> (on_left_only::None|(k->r->tmay r)) -> on_right_only::None|(k->b->tmay r)) -> (on_both::None|(k->r->b->tmay r)) -> {k:r}
        #'''
        d = {**self}
        if init is None:
            init = default_init
        if on_left_only is None:
            on_left_only = default_on_left_only
        if on_right_only is None:
            on_right_only = default_on_right_only
        if on_both is None:
            on_both = default_on_both

        def set_tm(d, k, tm):
            L = len(d)
            _set_tm(d, k, tm)
            if not on_left_only is default_on_left_only:
                #update keys
                assert L == len(keys)
                cmp = len(keys) - len(d)
                if cmp == 0:
                    pass
                elif cmp == +1:
                    keys.remove(k)
                elif cmp == -1:
                    keys.add(k)
                else:
                    raise logic-err
        if not on_left_only is default_on_left_only:
            keys = set(d)
        if not init is default_init:
            if on_left_only is default_on_left_only:
                keys = (*d,)
            for k in keys:
                tm = init(k, d[k])
                set_tm(d, k, tm)

        for mapping in mappings:
            if not (on_right_only is default_on_right_only and on_both is default_on_both):
                for k, b in mapping.items():
                    try:
                        r = d[k]
                    except KeyError:
                        tm = on_right_only(k, b)
                    else:
                        tm = on_both(k, r, b)
                    set_tm(d, k, tm)
            else:
                d.update(mapping)

            if not on_left_only is default_on_left_only:
                lonly_keys = keys - set(mapping.keys())
                for lonly_key in lonly_keys:
                    tm = on_left_only(lonly_key, d[lonly_key])
                    set_tm(d, lonly_key, tm)
            else:
                pass

    def ireplaces_or_removes_via_tmay(self, mappings, /, **kwargs):
        d = {**self}
        for mapping in itertools.chain(mappings, [kwargs]):
            for k, tm in mapping.items():
                _set_tm(d, k, tm)
        return type(self)(d)
    def ireplaces(self, mappings, /, **kwargs):
        d = {**self}
        for mapping in mappings:
            d.update(mapping)
        d.update(kwargs)
        return type(self)(d)


    def iupdate_ex(self, /, *mappings, init, on_left_only, on_right_only, on_both):
        return self.iupdates_ex(mappings, init=init, on_left_only=on_left_only, on_right_only=on_right_only, on_both=on_both)
    def ireplace_or_remove_via_tmay(self, /, *mappings, **kwargs):
        return self.ireplaces_or_removes_via_tmay(mappings, **kwargs)
    def ireplace(self, /, *mappings, **kwargs):
        return self.ireplaces(mappings, **kwargs)
        d = {**self, **mapping, **kwargs}
        return type(self)(d)




class FrozenDict(__Dict, HashableMapping):
    'should not modify .__d!'
    def __new__(cls, mapping_or_pairs=(), /, **kwargs):
        if not kwargs:
            if type(mapping_or_pairs) is __class__:
                self = mapping_or_pairs
                return self
        if not kwargs and isinstance(mapping_or_pairs, __class__):
            d = mapping_or_pairs._Dict__d
        else:
            d = dict(mapping_or_pairs, **kwargs)
        d
        if not d and cls is __class__:
            try:
                return empty_FrozenDict
            except NameError:
                pass
        self = super(__class__, cls).__new__(cls, d)
        self.__hash = None
        return self
    #def __init__(self, mapping_or_pairs=(), /, **kwargs):
    def __init(self, mapping_or_pairs=(), /, **kwargs):
        if not kwargs and isinstance(mapping_or_pairs, __class__):
            # bug: d = mapping_or_pairs.__d
            d = mapping_or_pairs._Dict__d
        else:
            d = dict(mapping_or_pairs, **kwargs)
        super().__init__(d)
        self.__hash = None
    def __hash__(self):
        if self.__hash is None:
            self.__hash = self._hash()
        return self.__hash
    def __or__(self, mapping, /):
        return self.ireplace(mapping)
    __ior__ = __or__
empty_FrozenDict = FrozenDict()
mk_FrozenDict = FrozenDict

class HalfFrozenDict(__Dict):
    def __new__(cls, mapping_or_pairs=(), **kwargs):
        d = dict(mapping_or_pairs, **kwargs)
        if not d and cls is __class__:
            try:
                return empty_HalfFrozenDict
            except NameError:
                pass
        self = super(__class__, cls).__new__(cls, d)
        return self
    #def __init__(self, mapping_or_pairs=(), **kwargs):
    def __init(self, mapping_or_pairs=(), **kwargs):
        d = dict(mapping_or_pairs, **kwargs)
        super().__init__(d)
    def __setitem__(self, key, value):
        if key not in self:
            raise KeyError('only existing key can be used to set item')

        self._Dict__d[key] = value
        # why _Dict__d!!
        #   getattr(self, '___Dict__d')[key] = value
    def __or__(self, mapping, /):
        return self.ireplace(mapping)
    __ior__ = __or__
#empty_HalfFrozenDict = HalfFrozenDict()
empty_HalfFrozenDict = empty_FrozenDict
mk_HalfFrozenDict = HalfFrozenDict





assert empty_HalfFrozenDict is mk_HalfFrozenDict()
assert empty_FrozenDict is mk_FrozenDict()


{FrozenDict({1:2, 3:3})}
hd = HalfFrozenDict(a=1, b=2)
hd['a'] = 3
try:
    hd[''] = 4
except KeyError:pass
else: raise ...










def __():

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











from seed.types.FrozenDict import FrozenDict, mk_FrozenDict, empty_FrozenDict
from seed.types.FrozenDict import HalfFrozenDict, mk_HalfFrozenDict, empty_HalfFrozenDict

from seed.types.FrozenDict import mapping_hash
from seed.types.FrozenDict import HashableMapping
from seed.types.FrozenDict import *
