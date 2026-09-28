#__all__:goto
r'''[[[
e ../../python3_src/seed/math/prime_pint/primes_with_specified_primitive_roots.py

seed.math.prime_pint.primes_with_specified_primitive_roots
py -m nn_ns.app.debug_cmd   seed.math.prime_pint.primes_with_specified_primitive_roots -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.prime_pint.primes_with_specified_primitive_roots:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/pseudo_random.py
===
fxtbook:
    41.7 Feedback carry shift registers (FCSR)
        [p::prime][order_mod_(p;2) == -1+p]:
            [SRS{FCSR{p}} := [1&(2^j%p) | [j:<-[1..=-1+p]]]]
            # A001122:primes with primitive root 2
]]


'#'; __doc__ = r'#'
>>> from itertools import islice
>>> from seed.helper.stable_repr import stable_repr

>>> [*iter_primes_with_specified_primitive_roots__ge_le_([2], 0, 100, more=False, reverse=True)]
[83, 67, 61, 59, 53, 37, 29, 19, 13, 11, 5, 3]
>>> [*iter_primes_with_specified_primitive_roots__ge_le_([2], 0, 100, more=False)]
[3, 5, 11, 13, 19, 29, 37, 53, 59, 61, 67, 83]
>>> [*iter_primes_with_specified_primitive_roots__ge_le_([2,3], 0, 100, more=False)]
[5, 19, 29, 53]
>>> [*iter_primes_with_specified_primitive_roots__ge_le_([2,3,5], 0, 100, more=False)]
[53]
>>> stable_repr([*iter_primes_with_specified_primitive_roots__ge_le_([2,3,5], 0, 100, more=True)])
'[(53, {2: 2, 13: 1})]'

>>> stable_repr([*islice(iter_primes_with_specified_primitive_roots__ge_le_([2], 2**64, 2**65, more=True), 3)])
'[(18446744073709551629, {2: 2, 7: 1, 658812288346769701: 1}), (18446744073709551709, {2: 2, 3: 2, 29: 1, 38652541: 1, 457131527: 1}), (18446744073709551757, {2: 2, 3: 1, 13: 1, 3859151: 1, 30641029451: 1})]'
>>> stable_repr([*islice(iter_primes_with_specified_primitive_roots__ge_le_([2], 2**63, 2**64, more=True, reverse=True), 3)])
'[(18446744073709551557, {2: 2, 11: 1, 137: 1, 547: 1, 5594472617641: 1}), (18446744073709551533, {2: 2, 43: 1, 67: 1, 193: 1, 809383: 1, 10247197: 1}), (18446744073709551437, {2: 2, 41: 1, 101: 1, 4051: 1, 6199: 1, 44347651: 1})]'
>>> 18446744073709551629-2**64
13
>>> 18446744073709551709-2**64
93
>>> 18446744073709551757-2**64
141

>>> 18446744073709551557-2**64
-59
>>> 18446744073709551533-2**64
-83
>>> 18446744073709551437-2**64
-179


[[
znorder(Mod(2,18446744073709551437))
    18446744073709551436

ds=[-179,-83,-59,13,93,141];
ps=[d+2^64 | d <- ds];
isprime(ps)
    [1,1,1,1,1,1]
[p-1 == znorder(Mod(2,p)) | p <- ps]
    [1,1,1,1,1,1]

e ../../python3_src/pari_gp_script/primes_with_specified_primitive_roots.gp
]]




py_adhoc_call   seed.math.prime_pint.primes_with_specified_primitive_roots   @f
from seed.math.prime_pint.primes_with_specified_primitive_roots import *
]]]'''#'''
#__all__:goto
#py_adhoc_call
r'''[[[

[[
===
py_adhoc_call   seed.math.prime_pint.primes_with_specified_primitive_roots   ,iter_primes_with_specified_primitive_roots__ge_le_ +more ='[2]' =2 =1000
    (3, {2: 1})
    (5, {2: 2})
    (11, {2: 1, 5: 1})
    (13, {2: 2, 3: 1})
    (19, {2: 1, 3: 2})
    (29, {2: 2, 7: 1})
    (37, {2: 2, 3: 2})
    (53, {2: 2, 13: 1})
    (59, {2: 1, 29: 1})
    (61, {2: 2, 3: 1, 5: 1})
    (67, {2: 1, 3: 1, 11: 1})
    (83, {2: 1, 41: 1})
    (101, {2: 2, 5: 2})
    (107, {2: 1, 53: 1})
    (131, {2: 1, 5: 1, 13: 1})
    (139, {2: 1, 3: 1, 23: 1})
    (149, {2: 2, 37: 1})
    (163, {2: 1, 3: 4})
    (173, {2: 2, 43: 1})
    (179, {2: 1, 89: 1})
    (181, {2: 2, 3: 2, 5: 1})
    (197, {2: 2, 7: 2})
    (211, {2: 1, 3: 1, 5: 1, 7: 1})
    (227, {2: 1, 113: 1})
    (269, {2: 2, 67: 1})
    (293, {2: 2, 73: 1})
    (317, {2: 2, 79: 1})
    (347, {2: 1, 173: 1})
    (349, {2: 2, 3: 1, 29: 1})
    (373, {2: 2, 3: 1, 31: 1})
    (379, {2: 1, 3: 3, 7: 1})
    (389, {2: 2, 97: 1})
    (419, {2: 1, 11: 1, 19: 1})
    (421, {2: 2, 3: 1, 5: 1, 7: 1})
    (443, {2: 1, 13: 1, 17: 1})
    (461, {2: 2, 5: 1, 23: 1})
    (467, {2: 1, 233: 1})
    (491, {2: 1, 5: 1, 7: 2})
    (509, {2: 2, 127: 1})
    (523, {2: 1, 3: 2, 29: 1})
    (541, {2: 2, 3: 3, 5: 1})
    (547, {2: 1, 3: 1, 7: 1, 13: 1})
    (557, {2: 2, 139: 1})
    (563, {2: 1, 281: 1})
    (587, {2: 1, 293: 1})
    (613, {2: 2, 3: 2, 17: 1})
    (619, {2: 1, 3: 1, 103: 1})
    (653, {2: 2, 163: 1})
    (659, {2: 1, 7: 1, 47: 1})
    (661, {2: 2, 3: 1, 5: 1, 11: 1})
    (677, {2: 2, 13: 2})
    (701, {2: 2, 5: 2, 7: 1})
    (709, {2: 2, 3: 1, 59: 1})
    (757, {2: 2, 3: 3, 7: 1})
    (773, {2: 2, 193: 1})
    (787, {2: 1, 3: 1, 131: 1})
    (797, {2: 2, 199: 1})
    (821, {2: 2, 5: 1, 41: 1})
    (827, {2: 1, 7: 1, 59: 1})
    (829, {2: 2, 3: 2, 23: 1})
    (853, {2: 2, 3: 1, 71: 1})
    (859, {2: 1, 3: 1, 11: 1, 13: 1})
    (877, {2: 2, 3: 1, 73: 1})
    (883, {2: 1, 3: 2, 7: 2})
    (907, {2: 1, 3: 1, 151: 1})
    (941, {2: 2, 5: 1, 47: 1})
    (947, {2: 1, 11: 1, 43: 1})



===
py_adhoc_call   seed.math.prime_pint.primes_with_specified_primitive_roots   @list.iter_primes_with_specified_primitive_roots__ge_le_ -more ='[2]' =2 =1000
    [3, 5, 11, 13, 19, 29, 37, 53, 59, 61, 67, 83, 101, 107, 131, 139, 149, 163, 173, 179, 181, 197, 211, 227, 269, 293, 317, 347, 349, 373, 379, 389, 419, 421, 443, 461, 467, 491, 509, 523, 541, 547, 557, 563, 587, 613, 619, 653, 659, 661, 677, 701, 709, 757, 773, 787, 797, 821, 827, 829, 853, 859, 877, 883, 907, 941, 947]
===
py_adhoc_call   seed.math.prime_pint.primes_with_specified_primitive_roots   @list.iter_primes_with_specified_primitive_roots__ge_le_ -more ='[2,3]' =2 =1000
    [5, 19, 29, 53, 101, 139, 149, 163, 173, 197, 211, 269, 293, 317, 379, 389, 461, 509, 557, 653, 677, 701, 773, 797, 821, 859, 907, 941]
===
py_adhoc_call   seed.math.prime_pint.primes_with_specified_primitive_roots   @list.iter_primes_with_specified_primitive_roots__ge_le_ -more ='[2,3,5]' =2 =1000
    [53, 173, 197, 293, 317, 557, 653, 677, 773, 797, 907]


===
py_adhoc_call   seed.math.prime_pint.primes_with_specified_primitive_roots   ,10:iter_primes_with_specified_primitive_roots__ge_le_ +more ='[2]' ='2**64' ='2**65'
    (18446744073709551629, {2: 2, 7: 1, 658812288346769701: 1})
    (18446744073709551709, {2: 2, 3: 2, 29: 1, 38652541: 1, 457131527: 1})
    (18446744073709551757, {2: 2, 3: 1, 13: 1, 3859151: 1, 30641029451: 1})
    (18446744073709551923, {2: 1, 7: 1, 19: 1, 456167: 1, 152024723251: 1})
    (18446744073709551947, {2: 1, 35960443: 1, 256486607711: 1})
    (18446744073709552109, {2: 2, 17: 1, 47: 1, 17467: 1, 330441535519: 1})
    (18446744073709552157, {2: 2, 4611686018427388039: 1})
    (18446744073709552213, {2: 2, 3: 5, 18978131763075671: 1})
    (18446744073709552253, {2: 2, 527099: 1, 2089273: 1, 4187669: 1})
    (18446744073709552267, {2: 1, 3: 3, 341606371735362079: 1})

===
]]
#]]]'''#'''
__all__ = r'''
iter_primes_with_specified_primitive_roots__ge_le_
    filter_primes_with_specified_primitive_roots_
    test4prime_with_specified_primitive_roots_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.containers import mk_tuple
    from seed.math.is_kth_primitive_root_mod_N__via_complete_factorization_k_ import is_kth_primitive_root_mod_N__via_complete_factorization_k_
    #def is_kth_primitive_root_mod_N__via_complete_factorization_k_(may_k, factorization_of_k, N, r, /, *, _ver=2):
    #   'may k/int{>=1} -> factorization{k} -> N/int{>=2} -> r/uint%N -> bool/[k==min_order_mod_(N;r)]'

    from seed.math.primality_test.SPRP_2357 import is_SPRP_2357_, filter_SPRP_2357_, iter_xprimes7SPRP_2357__ge_lt_
        # sieve coprime to [2,3,5,7]
        # maybe sieve coprime to [2..<2**16] chunk by chunk
    from seed.math.factor_pint.factor_pint__le_pow2_81 import factor_pint__le_pow2_81_, factor_pint__le_pow2_81__7ECM_7rho_first_
    #def factor_pint__le_pow2_81_(n, /, *, using_ECM:bool, **kwds):

def __():
    from seed.math.primality_test.strong_probable_prime import is_strong_probable_prime__basis_

    from seed.math.prime_sieve.sieve_ge_le import iter_sieve4prime_factorizations_ge_lt_
        #but cannot handle >2**60

    from seed.math.prime_sieve.primes_ge_lt import iter_primes__ge_lt_
    from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
    #def semi_factor_pint_via_trial_division(candidate_factors, pint, /):
    #    'Iter factor{>=2} -> pint -> (factor2exp/{factor:exp{>=1}}, unfactored_part{>=1})'

    from seed.math.search_smooth_around_interval import sorted_search_smooth_integer_inside_interval_, disordered_search_smooth_integer_inside_interval_, disordered_iter_search_smooth_integer_inside_interval_
    #def sorted_search_smooth_integer_inside_interval_(min4interval, max4interval, us, /, *, tuple_vs_dict=False, smooth_bases_checked=False):
#end:def __():


#.#################################
___end_mark_of_excluded_global_names__0___ = ...


__all__


def iter_primes_with_specified_primitive_roots__ge_le_(primitive_roots, min4prime, max4prime, /, *, more:bool, reverse=False):
    'primitive_roots/[int] -> min4prime/int -> max4prime/int -> Iter (u, ?[more]p2e4umm?){[min4prime<=u<=max4prime][is_prime_(u)][@[g:<-primitive_roots] -> [u-1 == order_mod_(u;g)]]}'
    min4prime = max(2, min4prime)
    us = range(min4prime, 1+max4prime)
    if reverse:
        us = us[::-1]
    return filter_primes_with_specified_primitive_roots_(primitive_roots, us, more=more)
def filter_primes_with_specified_primitive_roots_(primitive_roots, us, /, *, more:bool):
    'primitive_roots/[int] -> Iter u/int -> Iter (u, ?[more]p2e4umm?){[is_prime_(u)][@[g:<-primitive_roots] -> [u-1 == order_mod_(u;g)]]}'
    primitive_roots = mk_tuple(primitive_roots)
    if not primitive_roots:raise TypeError
    us = filter_SPRP_2357_(us)
    for u in us:
        m = test4prime_with_specified_primitive_roots_(primitive_roots, u)
        match m:
            case bool(False):
                pass
            case tuple([_u, dict() as p2e4umm]) if _u == u:
                yield u if not more else m
            case _:
                raise 000

_zpow81 = 1 << 81
def test4prime_with_specified_primitive_roots_(primitive_roots, u, /):
    'primitive_roots/[int] -> u/int -> (False|(u, p2e4umm){[is_prime_(u)][@[g:<-primitive_roots] -> [u-1 == order_mod_(u;g)]]})'
    assert len(primitive_roots)
    if u > _zpow81:raise NotImplementedError('[u > 2**81]', u)
    if u < 2:
        return False
    # [2 <= u]
    if 0 == u&1:
        if u == 2 and all(1==g&1 for g in primitive_roots):
            return (2, {})
        return False
    # [1 == u%2]
    # !! [2 <= u]
    # [3 <= u]
    gs = sorted(set(g%u for g in primitive_roots))
    # [0 <= gs[j] < u]
    match gs[0]:
        case (0|1):
            return False
    # [2 <= gs[j] < u]
    if u == 3:
        if gs == [2]:
            return (3, {2:1})
        return False
    # [4 <= u]
    # !! [1 == u%2]
    # [5 <= u]
    umm = u-1
    if gs[-1] == umm:
        return False
    # [2 <= gs[j] <= u-2]

    ###########################
    # !! [2 <= gs[j] <= u-2]
    # !! [5 <= u]
    # !! [1 == u%2]
    #if not is_strong_probable_prime__basis_(gs, u): return False
    half = umm>>1
    if not all(umm == pow(g, half, u) for g in gs): return False
    ###########################

    p2e4umm = factor_pint__le_pow2_81__7ECM_7rho_first_(umm)
    if not all(is_kth_primitive_root_mod_N__via_complete_factorization_k_(umm, p2e4umm, u, g) for g in gs):
        return False
    return (u, p2e4umm)


__all__
from seed.math.prime_pint.primes_with_specified_primitive_roots import iter_primes_with_specified_primitive_roots__ge_le_, filter_primes_with_specified_primitive_roots_, test4prime_with_specified_primitive_roots_
#def iter_primes_with_specified_primitive_roots__ge_le_(primitive_roots, min4prime, max4prime, /, *, more:bool, reverse=False):
from seed.math.prime_pint.primes_with_specified_primitive_roots import *
