#__all__:goto
r'''[[[
e ../../python3_src/seed/math/power/power_.py

seed.math.power.power_
py -m nn_ns.app.debug_cmd   seed.math.power.power_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.power_:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.power.power_:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######

[[
]]


'#'; __doc__ = r'#'

def power_(mul_, may_inv_, may_eq_zero_, eq_one_, one, imay_group_order, e, x0, /):
>>> mul_ = int.__mul__
>>> may_inv_ = None
>>> may_eq_zero_ = (0).__eq__
>>> eq_one_ = (1).__eq__
>>> one = 1
>>> imay_group_order = -1
>>> args = (mul_, may_inv_, may_eq_zero_, eq_one_, one, imay_group_order)
>>> power_(*args, 3001, 3) == 3**3001
True

>>> modulus = 1+2**16
>>> mul_ = lambda x,y:x*y%modulus
>>> may_inv_ = lambda x:pow(x,-1,modulus)
>>> may_eq_zero_ = lambda x:0 == x%modulus
>>> eq_one_ = lambda x:1 == x%modulus
>>> one = 1
>>> imay_group_order = -1+modulus
>>> args = (mul_, may_inv_, may_eq_zero_, eq_one_, one, imay_group_order)
>>> power_(*args, 3001, 3) == pow(3,3001,modulus)
True
>>> power_(*args, -1+2**61, 3) == pow(3,-1+2**61,modulus)
True
>>> power_(*args, -600001, 3) == pow(3,-600001,modulus)
True



py_adhoc_call   seed.math.power.power_   @f
]]]'''#'''
__all__ = r'''
power_
    std_exp_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.math.power.addition_chain.short.target_uint2short_addition_chain import 靶值讠加链牜尽量短扌
    from seed.math.power.addition_chain.common.indices import 松序加链讠址引减一讠最大最小加数址引扌

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

__all__



def std_exp_(imay_group_order, e, /):
    check_type_is(int, imay_group_order)
    check_type_is(int, e)
    if not -1 == (group_order:=imay_group_order):
        assert group_order >= 1
        # [group_order >= 1]
        e %= group_order
        # [0 <= e < group_order]
        if group_order < 2*e:
            # [0 < e < group_order < 2*e]
            # [group_order/2 < e < group_order]
            # [-group_order/2 < e-group_order < 0]
            e -= group_order
            # [-group_order/2 < e < 0]
        else:
            # [0 <= e < 2*e <= group_order]
            # [0 <= e <= group_order/2]
            pass
        e
        # [-group_order/2 < e <= group_order/2]
        # [imay_group_order >= 1]
    else:
        # [imay_group_order == -1]
        # [e :: int]
        e
        pass
    # [[imay_group_order == -1]or[-group_order/2 < e <= group_order/2]]
    return e



def power_(mul_, may_inv_, may_eq_zero_, eq_one_, one, imay_group_order, e, x0, /):
    'mul_/(x->x->x) -> may inv_/(x->x) -> may eq_zero_/(x->bool) -> eq_one_/(x->bool) -> one/x -> imay_group_order/imay uint{>=1} -> e/int -> x0/x -> y/x # [y==x**e] # [zero**0 == 1] # [[e<0][imay_group_order==-1] => [zero**e --> ^ZeroDivisionError]]'

    e = std_exp_(imay_group_order, e)
    # [[imay_group_order == -1]or[-group_order/2 < e <= group_order/2]]

    if e == 0 or eq_one_(x0):
        # assume:[zero**0 == 1]
        return one
    # [e =!= 0]
    # [x0 =!= one]

    if not None is (eq_zero_:=may_eq_zero_):
        if eq_zero_(x0):
            if e < 0 and imay_group_order == -1:raise ZeroDivisionError
            return x0
        # [x0 =!= zero]


    # [x0 =!= one]
    # [e =!= 0]
    if e < 0:
        # [e < 0]
        if not None is (inv_:=may_inv_):
            # [e < 0]
            e = -e
            777;x0 = inv_(x0)
            # [e > 0]
        elif not -1 == (group_order:=imay_group_order):
            # !! [[imay_group_order == -1]or[-group_order/2 < e <= group_order/2]]
            # [-group_order/2 < e <= group_order/2]
            # !! [e < 0]
            # [-group_order/2 < e < 0]
            e += group_order
            # [group_order/2 < e < group_order]
            # [e > 0]
        else:
            # [e < 0]
            # [may_inv_ is None]
            # [imay_group_order == -1]
            raise Exception('[e < 0][may_inv_ is None][imay_group_order == -1]')
        # [e > 0]

    else:
        # [e > 0]
        pass
    # [e > 0]
    return _power_(mul_, e, x0)


def _power_(mul_, e, x0, /):
    # [e > 0]
    assert e > 0
    us = 靶值讠加链牜尽量短扌(e)
    assert us[-1] == e

    kmm2ji = 松序加链讠址引减一讠最大最小加数址引扌(us)
    assert 1+len(kmm2ji) == len(us)

    k2x = [x0]
    for k in range(1, len(us)):
        (j, i) = kmm2ji[k-1]
        xj = k2x[j]
        xi = k2x[i]
        xk = mul_(xj, xi)
        k2x.append(xk)
    assert len(k2x) == len(us)
    xw = k2x[-1]
    return xw











__all__
from seed.math.power.power_ import power_, std_exp_
#def power_(mul_, may_inv_, may_eq_zero_, eq_one_, one, imay_group_order, e, x0, /):
#   e = std_exp_(imay_group_order, e)
#   # [[imay_group_order == -1]or[-group_order/2 < e <= group_order/2]]
from seed.math.power.power_ import *
