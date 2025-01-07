#__all__:goto
r'''[[[
e ../../python3_src/seed/math/log__bijective_numeration.py
view ../../python3_src/nn_ns/Bijection/BijectiveNumeration.py
used in:
    view ../../python3_src/seed/int_tools/digits/uint25bijective_numeration.py

seed.math.log__bijective_numeration
py -m nn_ns.app.debug_cmd   seed.math.log__bijective_numeration -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.log__bijective_numeration:__doc__ -ht # -ff -df


[[
[b,e :: uint][b >= 2][e >= 0]:
    [pow_(b; e) =[def]= (b**e)]
    [pow__bijective_numeration_(b; e) =[def]= = sum[b**k | [k :<- [0..<e]]] = ((b**e-1)/(b-1))]
[b :: uint][b >= 2][x :: float][x > 0]:
    [log_(b; x) =[def]= e where [x == (b**e)]]
    [log__bijective_numeration_(b; x) =[def]= e where [x == ((b**e-1)/(b-1))]]
    [x == ((b**e-1)/(b-1))]:
        [x*(b-1) == (b**e-1)]
        [(1+x*(b-1)) == (b**e)]
        [log_(b; (1+x*(b-1))) == e]
        [e == log_(b; (1+x*(b-1)))]
        [e == log_(b; x) +log_(b; (1/x+(b-1)))]
        [x > 1]:
            [1/x < 1]
            [(1/x+(b-1)) < b]
            [log_(b; (1/x+(b-1))/b) < log_(b; 1) == 0]
            [e < log_(b; x)]
]]




>>> [floor_log__bijective_numeration_(2, u) for u in range(20)]
[0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]
>>> [ceil_log__bijective_numeration_(2, u) for u in range(20)]
[0, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5]

>>> [floor_log__bijective_numeration_(3, u) for u in range(20)]
[0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]
>>> [ceil_log__bijective_numeration_(3, u) for u in range(20)]
[0, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4]

>>> [uint2len_bijective_numeration_(2, u) for u in range(20)]
[0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4]
>>> [uint2len_bijective_numeration_(3, u) for u in range(20)]
[0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]


>>> def _radix_pow__bijective_numeration__via_sum_(b, e, /):
...     if e < 1: return 0
...     r = 1
...     for _ in range(e-1):
...         r *= b
...         r += 1
...     return r
>>> [radix_pow__bijective_numeration_(2, u) for u in range(5)]
[0, 1, 3, 7, 15]
>>> [radix_pow__bijective_numeration_(3, u) for u in range(5)]
[0, 1, 4, 13, 40]

>>> [radix_pow__bijective_numeration_(2, u) for u in range(5)] == [_radix_pow__bijective_numeration__via_sum_(2, u) for u in range(5)]
True
>>> [radix_pow__bijective_numeration_(3, u) for u in range(5)] == [_radix_pow__bijective_numeration__via_sum_(3, u) for u in range(5)]
True



py_adhoc_call   seed.math.log__bijective_numeration   @f

]]]'''#'''
__all__ = r'''
log__bijective_numeration_
floor_log__bijective_numeration_
ceil_log__bijective_numeration_

uint2len_bijective_numeration_
radix_pow__bijective_numeration_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.math.log import log_
from seed.math.floor_ceil import floor_log_, ceil_log_
from seed.tiny import curry1
from seed.tiny_.check import check_type_is, check_int_ge

___end_mark_of_excluded_global_names__0___ = ...

def radix_pow__bijective_numeration_(b, e, /):
    'b/uint{>=2} -> e/uint -> ((b**e -1) /(b -1))'
    check_int_ge(2, b)
    check_int_ge(0, e)
    return (b**e -1) //(b -1)
def _xlog__bijective_numeration_(xlog_, b, x, /):
    'xlog_/(log_|floor_log_|ceil_log_) -> b -> e -> (xlog_(b, (1+x*(b-1))))'
    return xlog_(b, (1+x*(b-1)))
#def log__bijective_numeration_(b, x, /):
log__bijective_numeration_ = curry1(_xlog__bijective_numeration_, log_)
ceil_log__bijective_numeration_ = curry1(_xlog__bijective_numeration_, ceil_log_)
floor_log__bijective_numeration_ = curry1(_xlog__bijective_numeration_, floor_log_)

def uint2len_bijective_numeration_(b, u, /):
    check_int_ge(2, b)
    check_int_ge(0, u)
    return floor_log__bijective_numeration_(b, u)
    #bug:return 1+floor_log__bijective_numeration_(b, u)
    #   since [((b**(e+1) -1)/(b-1)) --> ((b**e -1)/(b-1))]



__all__
from seed.math.log__bijective_numeration import log__bijective_numeration_, floor_log__bijective_numeration_, ceil_log__bijective_numeration_
from seed.math.log__bijective_numeration import uint2len_bijective_numeration_, radix_pow__bijective_numeration_
from seed.math.log__bijective_numeration import *
