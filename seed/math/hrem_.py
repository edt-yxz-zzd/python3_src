#__all__:goto
r'''[[[
e ../../python3_src/seed/math/hrem_.py

seed.math.hrem_
py -m nn_ns.app.debug_cmd   seed.math.hrem_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.hrem_:__doc__ -ht # -ff -df
#######

[[
move_from:
view ../../python3_src/seed/math/Chinese_Remainder_Theorem__ver2.py
]]


'#'; __doc__ = r'#'
>>> for M in range(1, 10):
...     for x in range(-20, 20):
...         y = hrem_(M, x)
...         assert (y-x)%M == 0
...         assert -M < 2*y <= M



py_adhoc_call   seed.math.hrem_   @f
]]]'''#'''
__all__ = r'''
hrem_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...


def mk_hrem_(M, /):
    H = M >> 1
    even = not M&1
    def _hrem(x, /):
        return _hrem_(M, H, even, x)
    return _hrem
def hrem_(M, x, /):
    'M/uint{>0} -> x/int -> y/int # [y =[%M]= x][-M/2 < y <= M/2]'
    H = M >> 1
    even = not M&1
    return _hrem_(M, H, even, x)
def _hrem_(M, H, even, x, /):
    # [H == floor(M/2)]
    # [H == M//2]
    # [H <= M/2 < 1+H]
    # [-1+M/2 < H <= M/2]
    # [M/2 < 1+H <= 1+M/2]
    if not abs(x) <= H:
        x %= M
        # [0 <= x < M]
        if x > H:
            # [1+H <= x < M]
            x -= M
            # [-M+(1+H) <= x < 0]
            # !! [M/2 < 1+H <= 1+M/2]
            # [-M/2 < x < 0]
            # [ceil(-M/2) <= x < 0]
            # !! [H == floor(M/2)]
            # [-H == ceil(-M/2)]
            # [-H <= x < 0]
        else:
            # [0 <= x <= H]
            pass
        # [-H <= x < H]
    else:
        # [-H <= x <= H]
        pass
    # [-H <= x <= H]
    assert abs(x) <= H
    if even and x == -H:
        # [M%2 == 0]
        # [x == -H]

        # [H == M//2 == M/2]
        # [M == 2*H]
        # !! [x == -H]
        # [x =[%M]= H]
        x = H
        # [x == H == M/2]
        # [-M/2 < x <= M/2]
    else:
        # [M%2 == 1]or[x =!= H]
        # * [M%2 == 1]:
        #   [H == M//2 == (1+M)/2]
        #   [H =!= M/2]
        #   !! [-1+M/2 < H <= M/2]
        #   [-1+M/2 < H < M/2]
        #   !! [-H <= x <= H]
        #   [-M/2 < x < M/2]
        #   [-M/2 < x <= M/2]
        # * [x =!= H]:
        #   !! [-H <= x <= H]
        #   [-H < x <= H]
        #   !! [-1+M/2 < H <= M/2]
        #   [-M/2 < x <= M/2]
        #==>>:
        # [-M/2 < x <= M/2]
        pass
    # [-M/2 < x <= M/2]
    return x


__all__
from seed.math.hrem_ import hrem_, mk_hrem_
from seed.math.hrem_ import *
