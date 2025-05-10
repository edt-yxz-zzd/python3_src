#__all__:goto
r'''[[[
e ../../python3_src/seed/math/prepare_p2e4N.py

seed.math.prepare_p2e4N
py -m nn_ns.app.debug_cmd   seed.math.prepare_p2e4N -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.prepare_p2e4N:__doc__ -ht # -ff -df

[[
]]


>>> prepare_p2e4N_(60, (factor_pint__naive_brute_force_, [2,3])) == {2:2,3:1,5:1}
True
>>> prepare_p2e4N_(60, (None, [2,3])) == {2:2,3:1,5:1}
True
>>> prepare_p2e4N_(60, factor_pint__naive_brute_force_) == {2:2,3:1,5:1}
True
>>> prepare_p2e4N_(60, None) == {2:2,3:1,5:1}
True
>>> prepare_p2e4N_(60, {2:2,3:1,5:1}) == {2:2,3:1,5:1}
True
>>> prepare_p2e4N_(60, [2,3,5]) == {2:2,3:1,5:1}
True
>>> prepare_p2e4N_(60, [2,3,5,7]) == {2:2,3:1,5:1}
True
>>> prepare_p2e4N_(60, [2,3,7])
Traceback (most recent call last):
    ...
ValueError: candidate_factors is incomplete

py_adhoc_call   seed.math.prepare_p2e4N   @prepare_p2e4N_
]]]'''#'''
__all__ = r'''
prepare_p2e4N_
prepare_p2e4psphiM_ex_

num_coprimes_lt_
    phi_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
#def semi_factor_pint_via_trial_division(candidate_factors, pint, /):
#    'Iter factor{>=2} -> pint -> (factor2exp/{factor:exp{>=1}}, unfactored_part{>=1})'
from seed.math.semi_factor_pint_via_trial_division import complete_factor_pint_via_trial_division
from seed.math.factor_pint.factor_pint__naive_brute_force import factor_pint__naive_brute_force_
from seed.math.II import II__p2e_, II
from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...


def prepare_p2e4N_(N, may_p2e4N_or_ps4N_or_factor_pint_func, /):
    'N/int{>=1} -> may_p2e4N_or_ps4N_or_factor_pint_func/(None{=>factor_pint__naive_brute_force_}|factor_pint_func/(N->p2e4N)|p2e4N/{prime:exp}|ps4N/(Iter prime)|(may_factor_pint_func, partial_candidate_prime_factors)/tuple{len=2})'
    check_int_ge(1, N)
    t = may_p2e4N_or_ps4N_or_factor_pint_func
    if type(t) is tuple and len(t) == 2 and (t[0] is None or callable(t[0])):
        (may_factor_pint_func, partial_candidate_prime_factors) = t
        #_ps = iter(partial_candidate_prime_factors)
        _p2e4N, unfactored_part = semi_factor_pint_via_trial_division(partial_candidate_prime_factors, N)
        #recur:
        __p2e4N = prepare_p2e4N_(unfactored_part, may_factor_pint_func)
        _p2e4N.update(__p2e4N)
        777;    p2e4N = _p2e4N
        may_p2e4N_or_ps4N_or_factor_pint_func = p2e4N
    may_p2e4N_or_ps4N_or_factor_pint_func

    if may_p2e4N_or_ps4N_or_factor_pint_func is None:
        factor_pint_func = factor_pint__naive_brute_force_
        p2e4N_or_ps4N_or_factor_pint_func = factor_pint_func
    else:
        p2e4N_or_ps4N_or_factor_pint_func = may_p2e4N_or_ps4N_or_factor_pint_func
    p2e4N_or_ps4N_or_factor_pint_func

    if callable(p2e4N_or_ps4N_or_factor_pint_func):
        factor_pint_func = p2e4N_or_ps4N_or_factor_pint_func
        p2e4N = factor_pint_func(N)
        p2e4N_or_ps4N = p2e4N
    else:
        p2e4N_or_ps4N = p2e4N_or_ps4N_or_factor_pint_func
    p2e4N_or_ps4N

    if hasattr(p2e4N_or_ps4N, 'items'):
        p2e4N = p2e4N_or_ps4N
    else:
        ps4N = p2e4N_or_ps4N
        p2e4N = complete_factor_pint_via_trial_division(ps4N, N)
    p2e4N

    assert hasattr(p2e4N, 'items')
    if not II__p2e_(p2e4N) == N:raise Exception(N, may_p2e4N_or_ps4N_or_factor_pint_func, p2e4N)

    return p2e4N

def prepare_p2e4psphiM_ex_(modulus, psphiM_or_may_p2e4M_or_ps4M_or_factor_pint_func=None, may_p2e4psphiM_or_ps4psphiM_or_factor_pint_func=None, /):
    'modulus/int{>=2} -> (psphiM|may_p2e4M_or_ps4M_or_factor_pint_func=None) -> (may_p2e4psphiM_or_ps4psphiM_or_factor_pint_func=None) -> (psphiM, p2e4psphiM) # some coprime4M => [psphiM <- [k | [[k:<-[1..]][k%order_mod_(modulus;coprime4M)==0]]]]'
    check_int_ge(2, modulus)
    ######################
    if type(psphiM_or_may_p2e4M_or_ps4M_or_factor_pint_func) is int:
        psphiM = psphiM_or_may_p2e4M_or_ps4M_or_factor_pint_func
    else:
        if not (may_p2e4psphiM_or_ps4psphiM_or_factor_pint_func is None or callable(may_p2e4psphiM_or_ps4psphiM_or_factor_pint_func)):raise TypeError
        may_p2e4M_or_ps4M_or_factor_pint_func = psphiM_or_may_p2e4M_or_ps4M_or_factor_pint_func
        phiM = num_coprimes_lt_(modulus, may_p2e4M_or_ps4M_or_factor_pint_func)
        psphiM = phiM
    psphiM

    p2e4psphiM = prepare_p2e4N_(psphiM, may_p2e4psphiM_or_ps4psphiM_or_factor_pint_func)
    ######################
    psphiM
    p2e4psphiM
    return (psphiM, p2e4psphiM)

def num_coprimes_lt_(modulus, may_p2e4M_or_ps4M_or_factor_pint_func=None, /):
    'modulus/int{>=1} -> phiM/num_coprimes_lt_(modulus)'
    check_int_ge(1, modulus)
    p2e4M = prepare_p2e4N_(modulus, may_p2e4M_or_ps4M_or_factor_pint_func)
    #phiM = II((p-1)*p**(e-1) for p, e in p2e4M.items())
        #num_coprimes_ltM
    phiM = modulus//II(p2e4M.keys()) * II((p-1) for p in p2e4M)
    return phiM
phi_ = num_coprimes_lt_



__all__
from seed.math.prepare_p2e4N import prepare_p2e4N_
from seed.math.prepare_p2e4N import prepare_p2e4psphiM_ex_
from seed.math.prepare_p2e4N import num_coprimes_lt_, phi_
from seed.math.prepare_p2e4N import *
