#__all__:goto
r'''[[[
e ../../python3_src/seed/math/mk_perfect_div_mod_.py

seed.math.mk_perfect_div_mod_
py -m nn_ns.app.debug_cmd   seed.math.mk_perfect_div_mod_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.mk_perfect_div_mod_:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/algo/FFT/convolution.py
_prepare4mod_uint4symbolic_DFT_
_prepare4ring_ZZ4symbolic_DFT_
]]


'#'; __doc__ = r'#'
>>> mk_perfect_div_mod_(0, 7)
mk_perfect_div_mod_(0, 7)
>>> mk_perfect_div_mod_(0, 7)(4)
Traceback (most recent call last):
    ...
ValueError: (4, 7, 0, 4)
>>> mk_perfect_div_mod_(0, 7)(4*7)
4

>>> mk_perfect_div_mod_(17, 7)
mk_perfect_div_mod_(17, 7)
>>> mk_perfect_div_mod_(17, 7)(4)
3
>>> mk_perfect_div_mod_(17, 7)(4)*7%17
4

>>> mk_perfect_div_mod_(40, 10)(20)
2
>>> mk_perfect_div_mod_(40, 10)(30)
-1
>>> mk_perfect_div_mod_(40, 10)(30)*30%40
10

>>> mk_perfect_div_mod_(40, 10)(15)
Traceback (most recent call last):
    ...
ValueError: (15, 10, 1, 5)
>>> mk_perfect_div_mod_(40, 30)(15)
Traceback (most recent call last):
    ...
ValueError: (15, -10, 1, 5)
>>> mk_perfect_div_mod_(40, 30)(20)
2
>>> mk_perfect_div_mod_(40, 30)(20)*30%40
20





py_adhoc_call   seed.math.mk_perfect_div_mod_   @f
]]]'''#'''
__all__ = r'''
mk_perfect_div_mod_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.hrem_ import hrem_, mk_hrem_
    from math import gcd
    from seed.tiny_.check import check_type_is, check_int_ge
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def mk_perfect_div_mod_(modulus, denominator, /):
    return _mk_perfect_div_mod_(modulus, denominator)
class _mk_perfect_div_mod_:
    def __hash__(sf, /):
        return hash((__class__, sf._m, sf._d))
    def __eq__(sf, ot, /):
        if not type(ot) is __class__:
            return NotImplemented
        return sf._m == ot._m and sf._d == ot._d
    def __new__(cls, modulus, denominator, /):
        check_int_ge(0, modulus)
        if modulus == 0:
            return _mk_perfect_div_7ZZ_(denominator)

        check_type_is(int, denominator)
        hremR_ = mk_hrem_(modulus)
            # R - ring
        denominator = hremR_(denominator)
        if denominator == 0:raise ValueError
        sf = super(__class__, cls).__new__(cls)
        sf._m = modulus
        sf._d = denominator
        try:
            inv4D = pow(denominator, -1, modulus)
        except ValueError:
            ok = False
        else:
            ok = True
            GCD = 1
            H = modulus
            hremH_ = hremR_
            vD = hremH_(inv4D)
        if not ok:
            GCD = gcd(modulus, denominator)
            H = modulus//GCD
            hremH_ = mk_hrem_(H)
            vD = pow(denominator//GCD, -1, H)
            vD = hremH_(vD)
        sf._dat = (GCD, H, hremH_, vD)
        return sf
    def __call__(sf, numerator, /):
        (GCD, H, hremH_, vD) = sf._dat
        # [numerator =[%modulus]= y*denominator]
        # [numerator =[%(H*GCD)]= y*denominator]
        # [numerator =[%GCD]= y*denominator =[%GCD]= 0]
        (q, r) = divmod(numerator, GCD)
        if not r==0:raise ValueError(numerator, sf._d, q, r)
        # [q*GCD =[%(H*GCD)]= y*denominator]
        # [q =[%H]= y*(denominator//GCD)]
        # [q*inv_(denominator//GCD) =[%H]= y]
        # [q*vD =[%H]= y]
        y = hremH_(q*vD)
        return y
    def __repr__(sf, /):
        modulus = sf._m
        denominator = sf._d
        return f'mk_perfect_div_mod_({modulus}, {denominator})'


class _mk_perfect_div_7ZZ_:
    def __hash__(sf, /):
        return hash((__class__, sf._d))
    def __eq__(sf, ot, /):
        if not type(ot) is __class__:
            return NotImplemented
        return sf._d == ot._d
    def __init__(sf, denominator, /):
        check_type_is(int, denominator)
        if denominator == 0:raise ValueError
        sf._d = denominator
    def __call__(sf, numerator, /):
        (q, r) = divmod(numerator, sf._d)
        if not r==0:raise ValueError(numerator, sf._d, q, r)
        return q
    def __repr__(sf, /):
        modulus = 0
        denominator = sf._d
        return f'mk_perfect_div_mod_({modulus}, {denominator})'




__all__
from seed.math.mk_perfect_div_mod_ import mk_perfect_div_mod_
from seed.math.mk_perfect_div_mod_ import *
