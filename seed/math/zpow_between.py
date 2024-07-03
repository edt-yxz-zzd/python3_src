#__all__:goto
r'''[[[
e ../../python3_src/seed/math/zpow_between.py


seed.math.zpow_between
py -m nn_ns.app.debug_cmd   seed.math.zpow_between -x
py -m nn_ns.app.doctest_cmd seed.math.zpow_between:__doc__ -ht
py_adhoc_call   seed.math.zpow_between   @f



#]]]'''
__all__ = r'''
计算冫偏心二幂扌
计算冫居中二幂扌
计算冫最小二幂扌
计算冫最大二幂扌

'''.split()#'''
__all__
from seed.tiny_.check import check_int_ge, check_int_ge_le

def _ceil_log2_ex(u, /):
    check_int_ge(2, u)
    L = (u-1).bit_length()
    assert L >= 1
    max0 = (1<<L)
    if not (max0>>1) < u <= max0: raise 000
    return (L, max0)
def _floor_log2_ex(u, /):
    check_int_ge(2, u)
    L = u.bit_length() -1
    assert L >= 1
    min0 = (1<<L)
    if not min0 <= u < (min0<<1): raise 000
    return (L, min0)

def 计算冫偏心二幂扌(偏心, 最小值, 最大值, /):
    '-> 偏心二幂{尽量}'
    check_int_ge(2, 最小值)
    check_int_ge(最小值, 最大值)
    check_int_ge_le(最小值, 最大值, 偏心)
    if 最小值 == 最大值:
        return 最小值
    (L1, max1) = _ceil_log2_ex(偏心)
    if max1 == 偏心:
        return max1
    L0 = L1-1
    min0 = max1 >> 1
    assert min0 < 偏心 < max1
    if not (最小值 <= min0 and max1 <= 最大值):
        if 最小值 <= min0:
            return min0
        if max1 <= 最大值:
            return max1
        return 偏心
    if not (偏心<<1) < min0+max1:
        return max1
    return min0

def 计算冫居中二幂扌(最小值, 最大值, /):
    '-> 居中二幂{尽量}'
    check_int_ge(2, 最小值)
    check_int_ge(最小值, 最大值)
    if 最小值 == 最大值:
        return 最小值
    sum2 = (最小值+最大值)
    中点 = sum2//2
    return 计算冫偏心二幂扌(偏心:=中点, 最小值, 最大值)

def 计算冫最小二幂扌(最小值, 最大值, /):
    '-> 最小二幂{尽量}'
    check_int_ge(2, 最小值)
    check_int_ge(最小值, 最大值)
    if 最小值 == 最大值:
        return 最小值
    (L, max0) = _ceil_log2_ex(最小值)
    if max0 <= 最大值:
        return max0
    return (最小值+最大值)//2

def 计算冫最大二幂扌(最小值, 最大值, /):
    '-> 最大二幂{尽量}'
    check_int_ge(2, 最小值)
    check_int_ge(最小值, 最大值)
    if 最小值 == 最大值:
        return 最小值
    (L, min0) = _floor_log2_ex(最大值)
    if 最小值 <= min0:
        return min0
    return (最小值+最大值)//2






__all__
from seed.math.zpow_between import 计算冫偏心二幂扌,计算冫居中二幂扌,计算冫最小二幂扌,计算冫最大二幂扌
from seed.math.zpow_between import *
