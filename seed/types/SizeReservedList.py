#__all__:goto
r'''[[[
e ../../python3_src/seed/types/SizeReservedList.py

seed.types.SizeReservedList
py -m nn_ns.app.debug_cmd   seed.types.SizeReservedList -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.SizeReservedList:__doc__ -ht # -ff -df




>>> dir(list)     #doctest: +SKIP
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']



>>> [1,2] + [1,2]
[1, 2, 1, 2]
>>> [1,2]*3
[1, 2, 1, 2, 1, 2]
>>> 3*[1,2]
[1, 2, 1, 2, 1, 2]


>>> SizeReservedList(0)
SizeReservedList(0)
>>> SizeReservedList(99, range(700, 710))
SizeReservedList(99, [700, 701, 702, 703, 704, 705, 706, 707, 708, 709])
>>> ls = SizeReservedList(6)
>>> ls.reserved_size
6
>>> len(ls)
0
>>> ls.extend(range(1,3))
>>> ls.reserved_size
6
>>> len(ls)
2
>>> ls.append(555)
>>> len(ls)
3
>>> ls.pop(-2)
Traceback (most recent call last):
    ...
NotImplementedError: deletion may move too many items
>>> ls.pop(0)
Traceback (most recent call last):
    ...
NotImplementedError: deletion may move too many items
>>> ls.pop()
555
>>> len(ls)
2
>>> ls
SizeReservedList(6, [1, 2])
>>> ls[0]
1
>>> ls[1]
2
>>> ls[2] = 999
Traceback (most recent call last):
    ...
IndexError: range object index out of range
>>> ls[2]
Traceback (most recent call last):
    ...
IndexError: range object index out of range
>>> del ls[-1]
Traceback (most recent call last):
    ...
NotImplementedError: slice may cause size changing of sf._ls; deletion may move too many items
>>> ls.remove(2)
Traceback (most recent call last):
    ...
NotImplementedError: deletion may move too many items
>>> ls.insert(len(ls), 999)
Traceback (most recent call last):
    ...
NotImplementedError: insertion may move too many items
>>> ls.insert(-1, 999)
Traceback (most recent call last):
    ...
NotImplementedError: insertion may move too many items
>>> [*iter(ls)]
[1, 2]
>>> [*reversed(ls)]
[2, 1]
>>> ls
SizeReservedList(6, [1, 2])
>>> ls.reverse()
>>> ls
SizeReservedList(6, [2, 1])
>>> ls.sort()
>>> ls
SizeReservedList(6, [1, 2])
>>> ls[1] = 999
>>> ls[1]
999
>>> ls
SizeReservedList(6, [1, 999])
>>> ls+ls
SizeReservedList(6, [1, 999, 1, 999])
>>> ls*3
SizeReservedList(6, [1, 999, 1, 999, 1, 999])
>>> 3*ls
SizeReservedList(6, [1, 999, 1, 999, 1, 999])
>>> 999 in ls
True
>>> ls.index(999)
1
>>> ls.count(999)
1
>>> ls
SizeReservedList(6, [1, 999])
>>> ls += ls
>>> ls
SizeReservedList(6, [1, 999, 1, 999])
>>> del ls[-2:]
>>> ls
SizeReservedList(6, [1, 999])
>>> ls *= 4
Traceback (most recent call last):
    ...
seed.types.SizeReservedList.OverflowError4SizeReservedList
>>> ls
SizeReservedList(6, [1, 999])
>>> ls *= 3
>>> ls
SizeReservedList(6, [1, 999, 1, 999, 1, 999])
>>> ls.count(999)
3
>>> ls.clear()
>>> ls.index(999)
Traceback (most recent call last):
    ...
ValueError
>>> ls.count(999)
0
>>> len(ls)
0
>>> ls
SizeReservedList(6)










py_adhoc_call   seed.types.SizeReservedList   @f

]]]'''#'''
__all__ = r'''
SizeReservedList
OverflowError4SizeReservedList
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from collections.abc import MutableSequence
from collections import UserList
from itertools import repeat, islice, cycle
from seed.tiny_.check import check_type_is, check_int_ge, check_non_ABC
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

ValueError
OverflowError
class OverflowError4SizeReservedList(Exception):pass
#class SizeReservedList(UserList):
class SizeReservedList(MutableSequence):
    def __init__(sf, reserved_size, it=(), /):
        sf._ls = [None]*reserved_size
        sf._sz = 0
        sf.extend(it)
    def clear(sf, /):
        sz = sf._sz
        sf._ls[:sz] = repeat(None, sz)
        sf._sz = 0
    def copy(sf, /):
        ot = type(sf)(sf.reserved_size)
        ot._sz = sf._sz #bug:once miss this line
        ot._ls = sf._ls.copy()
        return ot
        return type(sf)(sf.reserved_size, sf)
        #bug:return type(sf)(sf._sz, sf._ls.copy())
    def as_list(sf, /):
        sz = len(sf)
        return sf._ls[:sz]
    def as_reversed_list(sf, /):
        sz = len(sf)
        return sf._ls[sz-1::-1]
    @property
    def reserved_size(sf, /):
        return len(sf._ls)
    def __repr__(sf, /):
        #bug:return repr_helper(sf, len(sf), [*sf])
        reserved_size = sf.reserved_size
        args = (reserved_size, [*sf])
        if not sf:
            args = args[:-1]
        return repr_helper(sf, *args)
    def __reversed__(sf, /):
        return map(sf._ls.__getitem__, reversed(range(len(sf))))
    def __iter__(sf, /):
        return islice(iter(sf._ls), len(sf))
        return map(sf._ls.__getitem__, range(len(sf)))
    def __len__(sf, /):
        return sf._sz
    def __getitem__(sf, k, /):
        '(idx|slice)-> (item|py.list) # [not return SizeReservedList]'
        k = _std_key(sf, k)
        return sf._ls[k]
    def __setitem__(sf, k, v, /):
        k = _std_key(sf, k)
        if not type(k) is int:
            raise NotImplementedError('slice may cause size changing of sf._ls')
        #check_int_ge(0, k) #slice may cause size changing of sf._ls
        sf._ls[k] = v
    def __delitem__(sf, k, /):
        k = _std_key(sf, k)
        if not (type(k) is slice and k.stop == len(sf) and k.step == 1):
            raise NotImplementedError('slice may cause size changing of sf._ls; deletion may move too many items')
        sl = k
        sz = len(sf)
        js = range(sz)[sl]
        n = len(js)
        sf._ls[sz-n:sz] = [None]*n
        sf._sz -= n

    #remove(self, value, /)
    #pop(self, index=-1, /)
    #insert(self, index, object, /)
    #extend(self, iterable, /)
    #append(self, object, /)
    #reverse(self, /)
    #sort(self, /, *, key=None, reverse=False)
    #__iadd__(self, value, /)
    #__imul__(self, value, /)
    #__add__(self, value, /)
    #   no:__radd__
    #__mul__(self, value, /)
    #__rmul__(self, value, /)

    def remove(self, value, /):
        raise NotImplementedError('deletion may move too many items')
    def insert(self, index, object, /):
        raise NotImplementedError('insertion may move too many items')
    def pop(sf, idx=-1, /):
        j = len(sf) -1
        if j == -1: raise IndexError
        if not (idx == -1 or idx == j):
            raise NotImplementedError('deletion may move too many items')
        v = sf._ls[j]
        sf._ls[j] = None
        sf._sz -= 1
        return v

    def append(sf, x, /):
        j = len(sf)
        try:
            sf._ls[j] = x
        except IndexError:
            raise OverflowError4SizeReservedList
        sf._sz += 1
    def extend(sf, iterable, /):
        #.if 0:
        #.    for _ in map(sf.append, iterable):pass
        #.    return None

        #if 0b0001:print('extend', sf, iterable)

        reserved_size = sf.reserved_size
        sz = len(sf)
        #.try:
        #.    len(iterable)
        #.except TypeError:
        # !! when [iterable is generator-based{sf/sf._ls}]
        if not type(iterable) in _ok_Ts:
            ls = [*islice(iterable, reserved_size -sz +1)]
            #n = len(ls)
            iterable = ls
        n = len(iterable)
        if not sz+n <= reserved_size:raise OverflowError4SizeReservedList
        sf._ls[sz:sz+n] = iterable
        sf._sz += n
        if not sf.reserved_size == reserved_size:
            del sf._ls
            del sf._sz
            raise BaseException(f'len(iterable) is wrong:{type(iterable)}')
        #if 0b0001:print('extend', sf, iterable)
        return None
    def reverse(sf, /):
        sz = len(sf)
        #bug:sf._ls[:sz] = sf._ls[sz::-1]
        sf._ls[:sz] = sf.as_reversed_list() # sf._ls[sz-1::-1]
    def sort(sf, /, *, key=None, reverse=False):
        sz = len(sf)
        ls = sf.as_list()
        ls.sort(key=key, reverse=reverse)
        sf._ls[:sz] = ls
    def __iadd__(sf, ot, /):
        if not len(sf)+len(ot) <= sf.reserved_size:raise OverflowError4SizeReservedList
        sf.extend(ot)
        return sf
    def __imul__(sf, multiplicity, /):
        check_type_is(int, multiplicity)
        multiplicity = max(0, multiplicity)
        if not len(sf)*multiplicity <= sf.reserved_size:raise OverflowError4SizeReservedList
        match multiplicity:
            case 1:
                pass
            case 0:
                sf.clear()
            case n:
                sz = len(sf)
                sf._ls[sz:sz*n] = sf.as_list()*(n-1)
                #sf._ls[sz:sz*n] = islice(cycle(sf.as_list()), sz*(n-1))
                sf._sz *= n
        return sf
    def __add__(sf, ot, /):
        if not len(sf)+len(ot) <= sf.reserved_size:raise OverflowError4SizeReservedList
        #if 0b0001:print('__iadd__', sf, ot)
        sf = sf.copy()
        #if 0b0001:print('__iadd__', sf, ot)
        sf += ot
        #if 0b0001:print('__iadd__', sf, ot)
        return sf
    def __mul__(sf, multiplicity, /):
        check_type_is(int, multiplicity)
        multiplicity = max(0, multiplicity)
        if not len(sf)*multiplicity <= sf.reserved_size:raise OverflowError4SizeReservedList
        if multiplicity == 0:
            return type(sf)(sf.reserved_size)
        sf = sf.copy()
        sf *= multiplicity
        return sf
    def __rmul__(sf, multiplicity, /):
        return sf*multiplicity
#mid-class SizeReservedList(MutableSequence):
_ok_Ts = (list, tuple, str, bytes)
def _std_key(sf, k, /):
    sz = len(sf)
    if not isinstance(k, slice):
        k = range(sz)[k]
    else:
        #(start, stop, stride)
        (start, stop, step) = k.indices(sz)
        k = slice(start, stop, step)
    k
    return k
#end-class SizeReservedList(MutableSequence):
check_non_ABC(SizeReservedList)

__all__
from seed.types.SizeReservedList import SizeReservedList, OverflowError4SizeReservedList
from seed.types.SizeReservedList import *
