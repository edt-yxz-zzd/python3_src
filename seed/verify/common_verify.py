
r'''
>>> is_UInt(0)
True
>>> is_UInt(-1)
False
>>> is_UInt([])
False

>>> is_UInt(0, TypeError)
True

#doctest: +IGNORE_EXCEPTION_DETAIL
>>> is_UInt([], TypeError)
Traceback (most recent call last):
    ...
TypeError: <class 'list'> is not <class 'int'>

>>> is_pair(())
False
>>> is_pair((1, 2))
True


>>> is_Sequence([1, ''], TypeError)
True
>>> is_Sequence({})
False
>>> is_Sequence.of([1, ''], is_UInt)
False
>>> is_Sequence.of([1, 0], is_UInt)
True


>>> is_sorted_sequence([])
True
>>> is_sorted_sequence([None])
True
>>> is_sorted_sequence([1,2])
True
>>> is_sorted_sequence([1,1])
True
>>> is_sorted_sequence([1,2,3])
True
>>> is_sorted_sequence([2,1])
False


>>> is_sorted_sequence.of([1, 2], is_UInt)
True
>>> is_sorted_sequence(['', 'a'])
True
>>> is_sorted_sequence.of(['', 'a'], is_UInt)
False
>>> is_sorted_sequence.of([0, 'a'], is_UInt)
False
>>> is_sorted_sequence([0, 'a'])
Traceback (most recent call last):
    ...
TypeError: '<=' not supported between instances of 'int' and 'str'


>>> is_strict_sorted_sequence([2,2])
False
>>> is_strict_sorted_sequence([1,2])
True


>>> has_attrs([], attrs='__getitem__ index'.split())
True
>>> has_attrs([], attrs=[])
True
>>> has_attrs([], attrs=['xxxxxx'])
False
'''


__all__ = '''
    is_int
    is_UInt
    is_tuple
    is_pair
    is_str

    is_Sequence
    is_Set
    is_Mapping
    is_sorted_sequence
    is_strict_sorted_sequence

    has_attrs
    '''.split()

from .Verify import Verify
from .VerifyType import VerifyType, VerifyType__static
from .VerifyContainer import VerifyContainerType
from collections.abc import Sequence, Set, Mapping

class is_int(VerifyType__static):
    types = int
class is_UInt(is_int):
    def _iter_verify_object_(self, obj):
        yield obj >= 0, lambda:'i < 0: {}'.format(obj)
        yield from super()._iter_verify_object_(obj)
class is_tuple(VerifyType__static):
    types = tuple
class is_pair(is_tuple):
    def _iter_verify_object_(self, obj):
        yield len(obj) == 2, lambda: 'len != 2: {}'.format(len(obj))
        yield from super()._iter_verify_object_(obj)
class is_str(VerifyType__static):
    types = str


class is_Sequence(VerifyContainerType):
    types = Sequence
class is_Set(VerifyContainerType):
    types = Set
class is_Mapping(VerifyContainerType):
    types = Mapping


class is_sorted_sequence(is_Sequence):
    def _iter_verify_object_(self, obj):
        ls = obj
        prevs = iter(ls)
        succs = iter(ls)
        for _ in succs: break
        for i, prev, succ in zip(range(len(ls)), prevs, succs):
            yield (prev <= succ, lambda: 'not sorted sequence at {idx}: '
                'not ls[{idx}] <= ls[{idx1}]; '
                'ls[{idx}]={lsI!r}; ls[{idx1}]={lsI1!r}; ls={ls!r}'
                .format(idx=i, idx1=i+1, lsI=ls[i], lsI1=ls[i+1], ls=ls)
                )
        yield from super()._iter_verify_object_(obj)

class is_strict_sorted_sequence(is_Sequence):
    def _iter_verify_object_(self, obj):
        ls = obj
        prevs = iter(ls)
        succs = iter(ls)
        for _ in succs: break
        for i, prev, succ in zip(range(len(ls)), prevs, succs):
            yield (prev < succ, lambda: 'not sorted sequence at {idx}: '
                'not ls[{idx}] < ls[{idx1}]; '
                'ls[{idx}]={lsI!r}; ls[{idx1}]={lsI1!r}; ls={ls!r}'
                .format(idx=i, idx1=i+1, lsI=ls[i], lsI1=ls[i+1], ls=ls)
                )
        yield from super()._iter_verify_object_(obj)



class has_attrs(Verify):
    def __init__(self, *, attrs, **kwargs):
        attrs = self.attrs = tuple(sorted(set(attrs)))
        assert is_Sequence.of(attrs, is_str, TypeError)
        if not all(attr.isidentifier() for attr in attrs): raise ValueError

        super().__init__(**kwargs)
    def _iter_verify_object_(self, obj):
        for attr in self.attrs:
            yield (hasattr(obj, attr), lambda:
                'has not attr {!r}: {!r}'.format(attr, obj)
                )
        yield from super()._iter_verify_object_(obj)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):
