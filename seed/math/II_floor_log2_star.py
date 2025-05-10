#__all__:goto
r'''[[[
e ../../python3_src/seed/math/II_floor_log2_star.py

seed.math.II_floor_log2_star
py -m nn_ns.app.debug_cmd   seed.math.II_floor_log2_star -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.II_floor_log2_star:__doc__ -ht # -ff -df

[[
]]

>>> [*map(II_floor_log2_star, range(1, 66))]
[0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 12, 12]


py_adhoc_call   seed.math.II_floor_log2_star   ,_iter_boundaries4II_floor_log2_star ='2**16+3'
(0, 1)
(1, 2)
(2, 4)
(3, 8)
(8, 16)
(10, 32)
(12, 64)
(14, 128)
(24, 256)
(27, 512)
(30, 1024)
(33, 2048)
(36, 4096)
(39, 8192)
(42, 16384)
(45, 32768)
(128, 65536)

py_adhoc_call   seed.math.II_floor_log2_star   @II_floor_log2_star ='2**16'
128

py_adhoc_call   seed.math.II_floor_log2_star   ,_iter_batch_II_floor_log2_star ='range(2**16-1,2**16+1)'
(65535, 45)
(65536, 128)

py_adhoc_call   seed.math.II_floor_log2_star   ,_iter_batch_II_floor_log2_star ='[2**ez for ez in range(9)]'
(1, 0)
(2, 1)
(4, 2)
(8, 3)
(16, 8)
(32, 10)
(64, 12)
(128, 14)
(256, 24)

py_adhoc_call   seed.math.II_floor_log2_star   ,_iter_batch_II_floor_log2_star ='[2**2**ez for ez in range(9)]'
(2, 1)
(4, 2)
(16, 8)
(256, 24)
(65536, 128)
(4294967296, 320)
(18446744073709551616, 768)
(340282366920938463463374607431768211456, 1792)
(115792089237316195423570985008687907853269984665640564039457584007913129639936, 6144)

]]]'''#'''
__all__ = r'''
II_floor_log2_star
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.math.floor_ceil import floor_log2
___end_mark_of_excluded_global_names__0___ = ...


def II_floor_log2_star(u, /):
    k = floor_log2(u)
    if k == 0:
        return 0
    assert k >= 1
    c = k
    while not k == 1:
        k = floor_log2(k)
        c *= k
    return c

def _iter_batch_II_floor_log2_star(us, /):
    for u in us:
        c = II_floor_log2_star(u)
        yield (u, c)
def _iter_boundaries4II_floor_log2_star(max1, /):
    b = -1
    for u in range(1, max1):
        c = II_floor_log2_star(u)
        if not c == b:
            b = c
            yield (c, u)
__all__
from seed.math.II_floor_log2_star import II_floor_log2_star
from seed.math.II_floor_log2_star import *
