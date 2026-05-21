#__all__:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/factor_pint5or_emay_prime_factors4target_pint_.py
view ../../python3_src/seed/math/prepare_p2e4N.py

seed.math.factor_pint.factor_pint5or_emay_prime_factors4target_pint_
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.factor_pint5or_emay_prime_factors4target_pint_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.factor_pint5or_emay_prime_factors4target_pint_:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.factor_pint.factor_pint5or_emay_prime_factors4target_pint_   @f
]]]'''#'''
__all__ = r'''
factor_pint5or_emay_prime_factors4target_pint_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.factor_pint.factor_pint__naive_brute_force import factor_pint__naive_brute_force_
    from seed.math.semi_factor_pint_via_trial_division import complete_factor_pint_via_trial_division
    from seed.tiny_.types5py import curry1
    from seed.tiny_.containers import mk_tuple
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def factor_pint5or_emay_prime_factors4target_pint_(emay_prime_factors4target_pint_or_factor_pint, /):
    'emay (prime_factors4target_pint/{prime}|factor_pint_/(uint{>=1} -> {prime:exp})) -> factor_pint_'
    x = emay_prime_factors4target_pint_or_factor_pint
    if ... is x:
        factor_pint_ = factor_pint__naive_brute_force_
    elif callable(x):
        factor_pint_ = x
    else:
        ps4O = mk_tuple(x)
        factor_pint_ = curry1(complete_factor_pint_via_trial_division, ps4O)
    factor_pint_
    return factor_pint_

__all__
from seed.math.factor_pint.factor_pint5or_emay_prime_factors4target_pint_ import factor_pint5or_emay_prime_factors4target_pint_
from seed.math.factor_pint.factor_pint5or_emay_prime_factors4target_pint_ import *
