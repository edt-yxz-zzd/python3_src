#__all__:goto
r'''[[[
e ../../python3_src/seed/math/valence_of_Euler_function.py

seed.math.valence_of_Euler_function
py -m nn_ns.app.debug_cmd   seed.math.valence_of_Euler_function -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.valence_of_Euler_function:__doc__ -ht # -ff -df
#######

[[
'/sdcard/0my_files/book/math/factorint/snd/The new book of prime number records(3ed)(1996)(Ribenboim).djvu'
page41[66/567]
    [37 == len{n | [n:<-[1..]][phi(n) == 480]}]

page38[63/567]
    Valence of Euler's Function

[f :: I4f->O4f][output4f :: O4f]:
    [valence_function{f}(output4f) =[def]= len{input4f | [input4f::I4f][f(input4f) == output4f]}]
    [valence_function{f} :: O4f -> uint]

[m:<-[1..]]:
    [valence_function{phi}(m) = valence_of_Euler_function_(m) = Vφ(m) =[def]= len{n | [n:<-[1..]][phi(n) == m]}]

Vφ(m) is called the (Euler) multiplicity of m
the function Vφ is called the valence function of φ.
]]


'#'; __doc__ = r'#'
>>> from itertools import islice
>>> [*islice(iter_even_uints_with_zero_Euler_multiplicity_(), 0, 20)]
[14, 26, 34, 38, 50, 62, 68, 74, 76, 86, 90, 94, 98, 114, 118, 122, 124, 134, 142, 146]



[[
===
py_adhoc_call   seed.math.valence_of_Euler_function   ,iter_inv_phi_ =...  =1
    2
    1
===
py_adhoc_call   seed.math.valence_of_Euler_function   ,iter_inv_phi_ =...  =2
    6
    3
    4
===
py_adhoc_call   seed.math.valence_of_Euler_function   @list.iter_inv_phi_ =...  =2
    [6, 3, 4]
===
py_adhoc_call   seed.math.valence_of_Euler_function   @list.iter_inv_phi_ =...  =3
    []
===
py_adhoc_call   seed.math.valence_of_Euler_function   @list_inv_phi_ =...  =4
    [10, 5, 12, 8]
===
py_adhoc_call   seed.math.valence_of_Euler_function   @list_inv_phi_ =...  =4 +to_sort
    [5, 8, 10, 12]
===
py_adhoc_call   seed.math.valence_of_Euler_function   @list_inv_phi_ =...  =480 +to_sort
    [527, 533, 715, 723, 861, 915, 964, 975, 976, 992, 1054, 1066, 1144, 1148, 1155, 1220, 1232, 1240, 1300, 1400, 1430, 1446, 1464, 1476, 1488, 1540, 1584, 1716, 1722, 1800, 1830, 1848, 1860, 1950, 1980, 2100, 2310]
===
py_adhoc_call   seed.math.valence_of_Euler_function   ,iter_inv_phi_ =...  =480  +with_factorization
    (1446, {241: 1, 3: 1, 2: 1})
    (723, {241: 1, 3: 1})
    (964, {241: 1, 2: 2})
    (1830, {61: 1, 5: 1, 3: 1, 2: 1})
    (915, {61: 1, 5: 1, 3: 1})
    (1220, {61: 1, 5: 1, 2: 2})
    (1464, {61: 1, 3: 1, 2: 3})
    (976, {61: 1, 2: 4})
    (1066, {41: 1, 13: 1, 2: 1})
    (533, {41: 1, 13: 1})
    (1722, {41: 1, 7: 1, 3: 1, 2: 1})
    (861, {41: 1, 7: 1, 3: 1})
    (1148, {41: 1, 7: 1, 2: 2})
    (1476, {41: 1, 3: 2, 2: 2})
    (1054, {31: 1, 17: 1, 2: 1})
    (527, {31: 1, 17: 1})
    (1860, {31: 1, 5: 1, 3: 1, 2: 2})
    (1240, {31: 1, 5: 1, 2: 3})
    (1488, {31: 1, 3: 1, 2: 4})
    (992, {31: 1, 2: 5})
    (1430, {13: 1, 11: 1, 5: 1, 2: 1})
    (715, {13: 1, 11: 1, 5: 1})
    (1716, {13: 1, 11: 1, 3: 1, 2: 2})
    (1144, {13: 1, 11: 1, 2: 3})
    (1950, {13: 1, 5: 2, 3: 1, 2: 1})
    (975, {13: 1, 5: 2, 3: 1})
    (1300, {13: 1, 5: 2, 2: 2})
    (2310, {11: 1, 7: 1, 5: 1, 3: 1, 2: 1})
    (1155, {11: 1, 7: 1, 5: 1, 3: 1})
    (1540, {11: 1, 7: 1, 5: 1, 2: 2})
    (1848, {11: 1, 7: 1, 3: 1, 2: 3})
    (1232, {11: 1, 7: 1, 2: 4})
    (1980, {11: 1, 5: 1, 3: 2, 2: 2})
    (1584, {11: 1, 3: 2, 2: 4})
    (2100, {7: 1, 5: 2, 3: 1, 2: 2})
    (1400, {7: 1, 5: 2, 2: 3})
    (1800, {5: 2, 3: 2, 2: 3})

===
py_adhoc_call   seed.math.valence_of_Euler_function   ,iter_batch_list_inv_phi_ =...  ='range(1,31)'  +with_output4phi +with_factorization -to_sort
    (1, [(2, {2: 1}), (1, {})])
    (2, [(6, {3: 1, 2: 1}), (3, {3: 1}), (4, {2: 2})])
    (3, [])
    (4, [(10, {5: 1, 2: 1}), (5, {5: 1}), (12, {3: 1, 2: 2}), (8, {2: 3})])
    (5, [])
    (6, [(14, {7: 1, 2: 1}), (7, {7: 1}), (18, {3: 2, 2: 1}), (9, {3: 2})])
    (7, [])
    (8, [(30, {5: 1, 3: 1, 2: 1}), (15, {5: 1, 3: 1}), (20, {5: 1, 2: 2}), (24, {3: 1, 2: 3}), (16, {2: 4})])
    (9, [])
    (10, [(22, {11: 1, 2: 1}), (11, {11: 1})])
    (11, [])
    (12, [(26, {13: 1, 2: 1}), (13, {13: 1}), (42, {7: 1, 3: 1, 2: 1}), (21, {7: 1, 3: 1}), (28, {7: 1, 2: 2}), (36, {3: 2, 2: 2})])
    (13, [])
    (14, [])
    (15, [])
    (16, [(34, {17: 1, 2: 1}), (17, {17: 1}), (60, {5: 1, 3: 1, 2: 2}), (40, {5: 1, 2: 3}), (48, {3: 1, 2: 4}), (32, {2: 5})])
    (17, [])
    (18, [(38, {19: 1, 2: 1}), (19, {19: 1}), (54, {3: 3, 2: 1}), (27, {3: 3})])
    (19, [])
    (20, [(66, {11: 1, 3: 1, 2: 1}), (33, {11: 1, 3: 1}), (44, {11: 1, 2: 2}), (50, {5: 2, 2: 1}), (25, {5: 2})])
    (21, [])
    (22, [(46, {23: 1, 2: 1}), (23, {23: 1})])
    (23, [])
    (24, [(78, {13: 1, 3: 1, 2: 1}), (39, {13: 1, 3: 1}), (52, {13: 1, 2: 2}), (70, {7: 1, 5: 1, 2: 1}), (35, {7: 1, 5: 1}), (84, {7: 1, 3: 1, 2: 2}), (56, {7: 1, 2: 3}), (90, {5: 1, 3: 2, 2: 1}), (45, {5: 1, 3: 2}), (72, {3: 2, 2: 3})])
    (25, [])
    (26, [])
    (27, [])
    (28, [(58, {29: 1, 2: 1}), (29, {29: 1})])
    (29, [])
    (30, [(62, {31: 1, 2: 1}), (31, {31: 1})])

===
py_adhoc_call   seed.math.valence_of_Euler_function   @the_Euler_multiplicity_of_ =...  =480
    37
===
py_adhoc_call   seed.math.valence_of_Euler_function   ,iter_Euler_multiplicities_of_ =...  ='range(1,31)'  +with_output4phi
    (1, 2)      ###唯一非零乊奇
    (2, 3)
    (3, 0)
    (4, 4)
    (5, 0)
    (6, 4)
    (7, 0)
    (8, 5)
    (9, 0)
    (10, 2)
    (11, 0)
    (12, 6)
    (13, 0)
    (14, 0)     ###首零乊偶
    (15, 0)
    (16, 6)
    (17, 0)
    (18, 4)
    (19, 0)
    (20, 5)
    (21, 0)
    (22, 2)
    (23, 0)
    (24, 10)
    (25, 0)
    (26, 0)
    (27, 0)
    (28, 2)
    (29, 0)
    (30, 2)
===
py_adhoc_call   seed.math.valence_of_Euler_function   ,20:iter_even_uints_with_zero_Euler_multiplicity_
py_adhoc_call   seed.math.valence_of_Euler_function   @list.20:iter_even_uints_with_zero_Euler_multiplicity_
    [14, 26, 34, 38, 50, 62, 68, 74, 76, 86, 90, 94, 98, 114, 118, 122, 124, 134, 142, 146]
        # (14+12*k) ??? 但是 未含110
    >>> [*range(14, 147, 12)]
    [14, 26, 38, 50, 62, 74, 86, 98, 110, 122, 134, 146]

    非(14+12*k) => [34,68,76,90,94,114,118,124,142]

===
]]

py_adhoc_call   seed.math.valence_of_Euler_function   @f
from seed.math.valence_of_Euler_function import 
]]]'''#'''
__all__ = r'''
iter_inv_phi_
    list_inv_phi_
        iter_batch_list_inv_phi_
the_Euler_multiplicity_of_
    iter_Euler_multiplicities_of_

iter_even_uints_with_zero_Euler_multiplicity_
    is_zero_Euler_multiplicity_



the_Euler_multiplicity_of_    multiplicity_of_output4phi_    valence_of_Euler_function_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.perfect_div import may_perfect_div, tmay_perfect_div
    from seed.math.perfect_div import perfect_div, perfect_kth_root_
    from seed.math.list_all_factors5factorization_ import iter_all_factors5factorization_
    from seed.math.is_prime__via_complete_factorization_Nmm_ import is_prime__via_complete_factorization_Nmm_
    from seed.math.factor_pint.factor_pint5or_emay_prime_factors4target_pint_ import factor_pint5or_emay_prime_factors4target_pint_

    from seed.tiny_.check import check_type_is, check_int_ge
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def iter_even_uints_with_zero_Euler_multiplicity_():
    '-> Iter u/uint{>0}{[u%2==0][the_Euler_multiplicity_of_(u) == 0]}'
    #from seed.math.prime_[#broken#]gens import all_prime_factors_gen
    #it = enumerate(iter(all_prime_factors_gen))
    #next(it) # 0 => None
    #next(it) # 1 => ()
    from seed.math.prime_sieve.sieve_ge_le import iter_sieve4prime_factorss_ge_lt_#iter_sieve4prime_factorizations_ge_lt_
    it = iter_sieve4prime_factorss_ge_lt_(2, None, with_uint=True)
    for u, ps4u in it:
        if u&1:continue
        if is_zero_Euler_multiplicity_(ps4u, u):
            #if 0 == the_Euler_multiplicity_of_(ps4u, u):
            yield u

def iter_Euler_multiplicities_of_(emay_prime_factors4output4phi_or_factor_pint, outputs4phi, /, *, with_output4phi=False):
    'emay (prime_factors4output4phi/{prime}|factor_pint_/(uint{>=1} -> {prime:exp})) -> Iter output4phi/uint{>=1} -> Iter len({input4phi | [input4phi::uint{>=1}][output4phi == phi(input4phi)]}) # phi is the Euler Function'
    factor_pint_ = factor_pint5or_emay_prime_factors4target_pint_(emay_prime_factors4output4phi_or_factor_pint)
    for output4phi in outputs4phi:
        total = the_Euler_multiplicity_of_(factor_pint_, output4phi)
        yield total if not with_output4phi else (output4phi, total)
def is_zero_Euler_multiplicity_(emay_prime_factors4output4phi_or_factor_pint, output4phi, /):
    'emay (prime_factors4output4phi/{prime}|factor_pint_/(uint{>=1} -> {prime:exp})) -> output4phi/uint{>=1} -> bool/[0==len({input4phi | [input4phi::uint{>=1}][output4phi == phi(input4phi)]})] # phi is the Euler Function'
    it = iter_inv_phi_(emay_prime_factors4output4phi_or_factor_pint, output4phi)
    return not any(1 for _ in it)
def the_Euler_multiplicity_of_(emay_prime_factors4output4phi_or_factor_pint, output4phi, /):
    'emay (prime_factors4output4phi/{prime}|factor_pint_/(uint{>=1} -> {prime:exp})) -> output4phi/uint{>=1} -> uint/len({input4phi | [input4phi::uint{>=1}][output4phi == phi(input4phi)]}) # phi is the Euler Function'
    it = iter_inv_phi_(emay_prime_factors4output4phi_or_factor_pint, output4phi)
    return sum(1 for _ in it)
valence_of_Euler_function_ = multiplicity_of_output4phi_ = the_Euler_multiplicity_of_

def iter_batch_list_inv_phi_(emay_prime_factors4output4phi_or_factor_pint, outputs4phi, /, *, to_sort=False, with_factorization=False, with_output4phi=False):
    'emay (prime_factors4output4phi/{prime}|factor_pint_/(uint{>=1} -> {prime:exp})) -> Iter output4phi/uint{>=1} -> Iter [input4phi/uint{>=1}] # [output4phi == phi(input4phi)] # phi is the Euler Function'
    factor_pint_ = factor_pint5or_emay_prime_factors4target_pint_(emay_prime_factors4output4phi_or_factor_pint)
    for output4phi in outputs4phi:
        inputs4phi = list_inv_phi_(factor_pint_, output4phi, to_sort=to_sort, with_factorization=with_factorization)
        yield inputs4phi if not with_output4phi else (output4phi, inputs4phi)
def list_inv_phi_(emay_prime_factors4output4phi_or_factor_pint, output4phi, /, *, to_sort=False, with_factorization=False):
    'emay (prime_factors4output4phi/{prime}|factor_pint_/(uint{>=1} -> {prime:exp})) -> output4phi/uint{>=1} -> [input4phi/uint{>=1}] # [output4phi == phi(input4phi)] # phi is the Euler Function'
    it = iter_inv_phi_(emay_prime_factors4output4phi_or_factor_pint, output4phi, with_factorization=with_factorization)
    return list(it) if not to_sort else sorted(it)
def iter_inv_phi_(emay_prime_factors4output4phi_or_factor_pint, output4phi, /, *, with_factorization=False):
    'emay (prime_factors4output4phi/{prime}|factor_pint_/(uint{>=1} -> {prime:exp})) -> output4phi/uint{>=1} -> Iter input4phi/uint{>=1} # [output4phi == phi(input4phi)] # phi is the Euler Function'
    check_int_ge(1, output4phi)
    if output4phi&1:
        # odd
        if output4phi > 1:
            return iter('')
    factor_pint_ = factor_pint5or_emay_prime_factors4target_pint_(emay_prime_factors4output4phi_or_factor_pint)
    p2e4O = factor_pint_(output4phi)

    # [phi(II[p**e | [(p,e):<-p2e4I.items()]]) == II[(p-1)*p**(e-1) | [(p,e):<-p2e4I.items()]]]
    q2p2e4qmm = {}
        # :: {q:p2e4qmm}
        # where [q::prime][output4phi%(q-1) == 0]

    ft_p2e4ft4O_pairs = sorted(iter_all_factors5factorization_(p2e4O, with_factorization=True))
    ft2p2e4ft4O = dict(ft_p2e4ft4O_pairs)
    ft2imay_max_p4O = {ft4O: max(p2e4ft4O, default=-1) for ft4O, p2e4ft4O in ft_p2e4ft4O_pairs}
    for factor, p2e4factor in ft_p2e4ft4O_pairs:
        if is_prime__via_complete_factorization_Nmm_(p2e4factor, 1+factor):
            q = 1+factor
            p2e4qmm = p2e4factor
            q2p2e4qmm[q] = p2e4qmm

    q2p2e4qmm
    q_p2e4qmm_pairs = sorted(q2p2e4qmm.items())
    assert q_p2e4qmm_pairs[0][0] == 2


    #ft4O_2_fts4I = {}
    _tmp__q2e4I = {}
    def f1_(end4qs, ft4O, /):
        '-> Iter ft4I'
        if ft4O == 1:
            if end4qs:
                assert not 2 in _tmp__q2e4I
                _tmp__q2e4I[2] = 1
                yield 2
                del _tmp__q2e4I[2]
            yield 1
            return
        # [ft4O > 1]
        if end4qs:
            imay_max_p4ft4O = ft2imay_max_p4O[ft4O]
            # !! [ft4O > 1]
            assert imay_max_p4ft4O > 1
            max_p4ft4O = imay_max_p4ft4O
            p2e4ft4O = ft2p2e4ft4O[ft4O]
            assert p2e4ft4O
        for j4q in reversed(range(end4qs)):
            (q, p2e4qmm) = q_p2e4qmm_pairs[j4q]
            if q < max_p4ft4O:
                break
            if ft4O < q-1:
                continue
            if not _divs_(p2e4qmm, p2e4ft4O):continue
            # [ft4O%(q-1) == 0]
            _ft4O = perfect_div(ft4O, q-1)
            e4q4ft4O = p2e4ft4O.get(q, 0)
            if e4q4ft4O:
                assert q == max_p4ft4O
            qw4ft4O = q**e4q4ft4O
            _ft4O = perfect_div(_ft4O, qw4ft4O)
            qw4I = q*qw4ft4O # --[phi]-> (q-1)*qw4ft4O
            assert not q in _tmp__q2e4I
            _tmp__q2e4I[q] = (1+e4q4ft4O)
            for _ft4I in f1_(j4q, _ft4O):
                ft4I = qw4I*_ft4I
                yield ft4I
            del _tmp__q2e4I[q]

        return
    #end-def f1_(end4qs, ft4O, /):
    def f2_(it, /):
        for input4phi in it:
            yield (input4phi, dict(_tmp__q2e4I))
        assert not _tmp__q2e4I
    ...
    it = f1_(len(q_p2e4qmm_pairs), output4phi)
    return it if not with_factorization else f2_(it)
#end-def iter_inv_phi_(emay_prime_factors4output4phi_or_factor_pint, output4phi, /, *, with_factorization=False):
def _divs_(p2e4D, p2e4N, /):
    '-> [N%D == 0]'
    return len(p2e4D) <= len(p2e4N) and p2e4D.keys() <= p2e4N.keys() and all(eD <= p2e4N[p] for p, eD in p2e4D.items())

__all__
from seed.math.valence_of_Euler_function import iter_inv_phi_, list_inv_phi_, iter_batch_list_inv_phi_
from seed.math.valence_of_Euler_function import the_Euler_multiplicity_of_, iter_Euler_multiplicities_of_  # the_Euler_multiplicity_of_ === multiplicity_of_output4phi_ === valence_of_Euler_function_
from seed.math.valence_of_Euler_function import iter_even_uints_with_zero_Euler_multiplicity_, is_zero_Euler_multiplicity_
from seed.math.valence_of_Euler_function import *
