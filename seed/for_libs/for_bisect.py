#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_bisect.py

seed.for_libs.for_bisect
py -m nn_ns.app.debug_cmd   seed.for_libs.for_bisect -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.for_libs.for_bisect:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> contains7bisect_(range(999), 999)
False
>>> contains7bisect_(range(999), 998)
True
>>> contains7bisect_(range(999), 666)
True
>>> contains7bisect_(range(999), 0)
True
>>> contains7bisect_(range(999), -1)
False
>>> contains7bisect_(range(999), 666, 666, 777)
True
>>> contains7bisect_(range(999), 665, 666, 777)
False
>>> contains7bisect_(range(999), 777, 666, 777)
False
>>> contains7bisect_(range(999), 776, 666, 777)
True
>>> contains7bisect_(range(999), 666, 666, 667)
True
>>> contains7bisect_(range(999), 666, 666, 666)
False
>>> contains7bisect_(range(999), 10, 666, 777, key=int.bit_length)
True
>>> contains7bisect_(range(999), 9, 666, 777, key=int.bit_length)
False
>>> contains7bisect_(range(999), 11, 666, 777, key=int.bit_length)
False



py_adhoc_call   seed.for_libs.for_bisect   @f
from seed.for_libs.for_bisect import *
]]]'''#'''
__all__ = r'''
contains7bisect_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from bisect import bisect_right
___end_mark_of_excluded_global_names__0___ = ...

def contains7bisect_(xs, k, begin=0, end=None, /, *, key=None):
    assert begin >= 0
    j = bisect_right(xs, k, begin, end, key=key)
    if begin < j:
        x = xs[j-1]
        k4x = x if None is key else key(x)
        return k == k4x
    return False

__all__
from seed.for_libs.for_bisect import contains7bisect_
from seed.for_libs.for_bisect import *
