#__all__:goto
r'''[[[
e ../../python3_src/seed/iters/FixedSizeTailTrapIterator.py

seed.iters.FixedSizeTailTrapIterator
py -m nn_ns.app.debug_cmd   seed.iters.FixedSizeTailTrapIterator -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.iters.FixedSizeTailTrapIterator:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> it = FixedSizeTailTrapIterator(4, range(9))
>>> it.eof
False
>>> it.len_trap
4
>>> it.trap2tuple_()
(0, 1, 2, 3)
>>> [*it]
[0, 1, 2, 3, 4]
>>> it.eof
True
>>> it.len_trap
4
>>> it.trap2tuple_()
(5, 6, 7, 8)

>>> it = FixedSizeTailTrapIterator(4, range(4))
>>> it.eof
False
>>> it.len_trap
4
>>> it.trap2tuple_()
(0, 1, 2, 3)
>>> [*it]
[]
>>> it.eof
True
>>> it.len_trap
4
>>> it.trap2tuple_()
(0, 1, 2, 3)

>>> it = FixedSizeTailTrapIterator(4, range(2))
>>> it.eof
True
>>> it.len_trap
2
>>> it.trap2tuple_()
(0, 1)
>>> [*it]
[]
>>> it.eof
True
>>> it.len_trap
2
>>> it.trap2tuple_()
(0, 1)

>>> it = FixedSizeTailTrapIterator(0, range(2))
>>> it.eof
False
>>> it.len_trap
0
>>> it.trap2tuple_()
()
>>> [*it]
[0, 1]
>>> it.eof
True
>>> it.len_trap
0
>>> it.trap2tuple_()
()




py_adhoc_call   seed.iters.FixedSizeTailTrapIterator   @f
]]]'''#'''
__all__ = r'''
FixedSizeTailTrapIterator
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge
from collections import deque
#from seed.types.Deque import Deque as deque
___end_mark_of_excluded_global_names__0___ = ...

class FixedSizeTailTrapIterator:
    def __init__(sf, maxlen4trap, iterable, /):
        check_int_ge(0, maxlen4trap)
        sf._sz = maxlen4trap
        #sf._full = 0==maxlen4trap
        sf._it = it = iter(iterable)
        sf._dq = dq = deque(islice(it, 0, maxlen4trap), maxlen4trap)
        sf._eof = len(dq) < maxlen4trap
    @property
    def eof(sf, /):
        return sf._eof
    @property
    def len_trap(sf, /):
        return len(sf._dq)
    def trap2tuple_(sf, /):
        return tuple(sf._dq)
    def __iter__(sf, /):
        return sf
    def __next__(sf, /):
        sf._eof = True
        z = next(sf._it)
            # ^StopIteration
        sf._eof = False
        dq = sf._dq
        if dq:
            x = dq.popleft()
            777;dq.append(z)
        else:
            x = z
        x
        return x


__all__
from seed.iters.FixedSizeTailTrapIterator import FixedSizeTailTrapIterator
    #FixedSizeTailTrapIterator(maxlen4trap, iterable)
    #   .eof
    #   .len_trap
    #   .trap2tuple_()
from seed.iters.FixedSizeTailTrapIterator import *
