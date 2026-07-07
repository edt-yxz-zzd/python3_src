#__all__:goto
r'''[[[
e ../../python3_src/seed/math/polynomial/eval_polynomial/repr_polynomial8dict.py

seed.math.polynomial.eval_polynomial.repr_polynomial8dict
py -m nn_ns.app.debug_cmd   seed.math.polynomial.eval_polynomial.repr_polynomial8dict -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.polynomial.eval_polynomial.repr_polynomial8dict:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> exp2coeff_to_exp2nonzero_coeff_(None, [1,2,3,4,5])
{0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
>>> exp2coeff_to_exp2nonzero_coeff_(None, [0,2,3,4,0])
{1: 2, 2: 3, 3: 4}
>>> exp2coeff_to_exp2nonzero_coeff_(None, [0,2,0,4,0])
{1: 2, 3: 4}



py_adhoc_call   seed.math.polynomial.eval_polynomial.repr_polynomial8dict   @f
]]]'''#'''
__all__ = r'''
exp2coeff_to_exp2nonzero_coeff_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def exp2coeff_to_exp2nonzero_coeff_(may_opsX_or_eq_zero_, cs, /):
    'exp2coeff/[RR]/sequence -> exp2nonzero_coeff_/{exp:RR{=!=0}}/mapping'
    cs[:0] #seq --> dict
    if may_opsX_or_eq_zero_ is None:
        from operator import not_
        eq_zero_ = not_
    elif hasattr(may_opsX_or_eq_zero_, 'eq_zero_'):
        opsX = may_opsX_or_eq_zero_
        eq_zero_ = opsX.eq_zero_
    elif callable(may_opsX_or_eq_zero_):
        eq_zero_ = may_opsX_or_eq_zero_
    else:
        raise TypeError(may_opsX_or_eq_zero_)
    eq_zero_
    return {j:c for j, c in enumerate(cs) if not eq_zero_(c)}

__all__
from seed.math.polynomial.eval_polynomial.repr_polynomial8dict import exp2coeff_to_exp2nonzero_coeff_
from seed.math.polynomial.eval_polynomial.repr_polynomial8dict import *
