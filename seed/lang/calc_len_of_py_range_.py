r'''[[[
e ../../python3_src/seed/lang/calc_len_of_py_range_.py

py -m nn_ns.app.debug_cmd   seed.lang.calc_len_of_py_range_  -x
py -m nn_ns.app.doctest_cmd seed.lang.calc_len_of_py_range_!

#]]]'''#'''

__all__ = r'''
calc_len_of_py_range_
    Range
'''.split()#'''
__all__


def calc_len_of_py_range_(array, /):
    r'''see:seed.seq_tools.bisearch

# e ../lots/NOTE/Python/python-bug/len-bug.txt
# bug:py.range.__len__()
>>> len(range(2**80))
Traceback (most recent call last):
    ...
OverflowError: Python int too large to convert to C ssize_t
>>> range(2**80).__len__()
Traceback (most recent call last):
    ...
OverflowError: Python int too large to convert to C ssize_t

>>> calc_len_of_py_range_(range(2**80)) == 2**80
True

'''#'''

    (start, stop, step) = (array.start, array.stop, array.step)

    if step < 0:
        (start, stop, step) = (-start, -stop, -step)

    return max(0, 1+ (stop -start -1) // step)



assert calc_len_of_py_range_(__ := range(6)) == len(__)
assert calc_len_of_py_range_(__ := range(0)) == len(__)
assert calc_len_of_py_range_(__ := range(-1)) == len(__)
assert calc_len_of_py_range_(__ := range(3, 7, -1)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, 1)) == len(__)

assert calc_len_of_py_range_(__ := range(3, 7, 1)) == len(__)
assert calc_len_of_py_range_(__ := range(3, 7, 2)) == len(__)
assert calc_len_of_py_range_(__ := range(3, 7, 3)) == len(__)
assert calc_len_of_py_range_(__ := range(3, 7, 4)) == len(__)
assert calc_len_of_py_range_(__ := range(3, 7, 5)) == len(__)
assert calc_len_of_py_range_(__ := range(3, 7, 6)) == len(__)
assert calc_len_of_py_range_(__ := range(3, 7, 7)) == len(__)
assert calc_len_of_py_range_(__ := range(3, 7, 8)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, -1)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, -2)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, -3)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, -4)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, -5)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, -6)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, -7)) == len(__)
assert calc_len_of_py_range_(__ := range(-3, -7, -8)) == len(__)


def __():
    class Range(range):
        #TypeError: type 'range' is not an acceptable base type
        __len__ = calc_len_of_py_range_

class Range:
    r'''

>>> ls = Range(10**200+1)
>>> ls
Range(0, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)

# e ../lots/NOTE/Python/python-bug/len-bug.txt
# bug:py.len()
>>> ls = Range(10**200+1)
>>> type(ls).__len__(ls) == 10**200+1
True
>>> len(ls) == 10**200+1
Traceback (most recent call last):
    ...
OverflowError: cannot fit 'int' into an index-sized integer
>>> ls._ls.__len__() == 10**200+1
Traceback (most recent call last):
    ...
OverflowError: Python int too large to convert to C ssize_t
>>> ls.__len__() == 10**200+1
True
>>> ls.len_() == 10**200+1
True
>>> ls.len == 10**200+1
True
>>> ls[10**200]
Range(0, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
>>> ls[10**100:10**200]
Range(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

'''#'''
    def __init__(sf, /, *args4range):
        try:
            ls = range(*args4range)
        except TypeError:
            if not len(args4range)==1:
                raise
            [x] = args4range
            T = type(x)
            if T is range:
                ls = x
            elif isinstance(T, __class__):
                ls = x._ls
            else:
                raise
            ls
        ls
        sf._ls = ls
    def __len__(sf, /):
        return calc_len_of_py_range_(sf._ls)
    len_ = __len__
    @property
    def len(sf, /):
        return sf.len_()
    def __getitem__(sf, k, /):
        return type(sf)(sf._ls[k])
    def __bool__(sf, /):
        return bool(sf._ls)
    def __contains__(sf, x, /):
        return x in sf._ls
    def _cmp_(sf, ot, op, /):
        while 1:
            #if not isinstance(ot, __class__):
            if not type(ot) is __class__:
                if type(ot) is range:
                    ls4ot = ot
                    break
                return NotImplemented
            ls4ot = ot._ls
            break
        ls4sf = sf._ls
        return op(ls4sf, ls4ot)
    def __hash__(sf, /):
        return hash(sf._ls)
    def __eq__(sf, ot, /):
        return sf._cmp_(ot, range.__eq__)
    def __ne__(sf, ot, /):
        return sf._cmp_(ot, range.__ne__)
    def __lt__(sf, ot, /):
        return sf._cmp_(ot, range.__lt__)
    def __le__(sf, ot, /):
        return sf._cmp_(ot, range.__le__)
    def __gt__(sf, ot, /):
        return sf._cmp_(ot, range.__gt__)
    def __ge__(sf, ot, /):
        return sf._cmp_(ot, range.__ge__)
    def __repr__(sf, /):
        return repr(sf._ls).replace('r', 'R', 1)
    def __str__(sf, /):
        return str(sf._ls).replace('r', 'R', 1)
    def __iter__(sf, /):
        return iter(sf._ls)
    def __reversed__(sf, /):
        return reversed(sf._ls)
    def __reduce__(sf, /, *args, **kwds):
        return range.__reduce__(sf._ls, *args, **kwds)
    def __reduce_ex__(sf, /, *args, **kwds):
        return range.__reduce_ex__(sf._ls, *args, **kwds)
    def index(sf, /, *args, **kwds):
        return range.index(sf._ls, *args, **kwds)
    def count(sf, /, *args, **kwds):
        return range.count(sf._ls, *args, **kwds)
    @property
    def start(sf, /):
        return (sf._ls).start
    @property
    def stop(sf, /):
        return (sf._ls).stop
    @property
    def step(sf, /):
        return (sf._ls).step

__all__
from seed.lang.calc_len_of_py_range_ import calc_len_of_py_range_
from seed.lang.calc_len_of_py_range_ import Range
from seed.lang.calc_len_of_py_range_ import *
