#__all__:goto
#from seed.math.factor_pint_as_pefect_power_ import is_kth_power_, is_square_, is_cube_
r'''[[[
e ../../python3_src/seed/math/floor_ceil_tools/fc_perfect.py

seed.math.floor_ceil_tools.fc_perfect
py -m nn_ns.app.debug_cmd   seed.math.floor_ceil_tools.fc_perfect -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.floor_ceil_tools.fc_perfect:__doc__ -ht # -ff -df
#######

[[
move_from:
e ../../python3_src/seed/math/floor_ceil.py
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.floor_ceil_tools.fc_perfect   @f
]]]'''#'''
__all__ = r'''
BaseError
    NotPerfectError
        NotPerfectError__div
        NotPerfectError__kth_root
perfect_div
perfect_kth_root_
    may_perfect_div
    tmay_perfect_div


is_kth_power_
    is_square_
    is_cube_
factor_pint_as_pefect_power_
    may_perfect_kth_root_
    may_perfect_sqrt_
    may_perfect_cbrt_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_2_powers
    from seed.math.floor_ceil_tools.fc_kth_root import floor_kth_root_
___end_mark_of_excluded_global_names__0___ = ...

with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.factor_pint_as_pefect_power_ import factor_pint_as_pefect_power_
    from seed.math.factor_pint_as_pefect_power_ import is_kth_power_, is_square_, is_cube_
    from seed.math.factor_pint_as_pefect_power_ import may_perfect_kth_root_, may_perfect_sqrt_, may_perfect_cbrt_




class BaseError(Exception):pass
class NotPerfectError(BaseError):pass
class NotPerfectError__div(NotPerfectError):pass
class NotPerfectError__kth_root(NotPerfectError):pass
def perfect_div(n, d, lazy_err_=None, /):
    'n -> d -> (q:=n///d)/int |^NotPerfectError__div # [q*d == n]'
    q, r = divmod(n,d)
    if not r==0:
        if lazy_err_ is None:
            lazy_err_ = NotPerfectError__div
        raise lazy_err_()
    return q
def perfect_kth_root_(k, n, lazy_err_=None, /):
    'k/{>=1} -> n/{>=0} -> (rt:=n**(1/k))/int |^NotPerfectError__kth_root # [rt**k == n]'
    #########new:
    if not None is (rt:=may_perfect_kth_root_(k, n)):
        return rt
    else:
        if lazy_err_ is None:
            lazy_err_ = NotPerfectError__kth_root
        raise lazy_err_()

    raise 000
    #########old:
    if lazy_err_ is None:
        lazy_err_ = NotPerfectError__kth_root
    #check_type_is(int, n)
    if not n >= 0: raise TypeError
    if n < 2: return n

    (e, odd) = factor_pint_out_2_powers(n)
    e4rt = perfect_div(e, k, lazy_err_)
    rt4odd = floor_kth_root_(k, odd)
    if not rt4odd**k == odd:
        raise lazy_err_()
    rt = rt4odd << e4rt
    return rt


def may_perfect_div(n, d, /):
    'n/int -> d/int{=!=0} -> may q/int{[q*d == n]}'
    (q, r) = divmod(n, d)
    return q if r == 0 else None
def tmay_perfect_div(n, d, /):
    'n/int -> d/int{=!=0} -> tmay q/int{[q*d == n]}'
    if not None is (q:=may_perfect_div(n, d)):
        return (q,)
    return ()





__all__
from seed.math.floor_ceil_tools.fc_perfect import BaseError, NotPerfectError, NotPerfectError__div, NotPerfectError__kth_root
from seed.math.floor_ceil_tools.fc_perfect import perfect_div, perfect_kth_root_, may_perfect_div, tmay_perfect_div
def __():
    from seed.math.factor_pint_as_pefect_power_ import factor_pint_as_pefect_power_
    from seed.math.factor_pint_as_pefect_power_ import is_kth_power_, is_square_, is_cube_
    from seed.math.factor_pint_as_pefect_power_ import may_perfect_kth_root_, may_perfect_sqrt_, may_perfect_cbrt_

from seed.math.floor_ceil_tools.fc_perfect import *
