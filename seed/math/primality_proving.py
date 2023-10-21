#__all__:goto
r'''[[[
e ../../python3_src/seed/math/primality_proving.py


seed.math.primality_proving
py -m seed.math.primality_proving
py -m nn_ns.app.debug_cmd   seed.math.primality_proving -x
py -m nn_ns.app.doctest_cmd seed.math.primality_proving:__doc__ -ff -v



[[
copy from:
    view others/数学/prime/primality_test.txt
===
# using complete factorization
# without gcd
[[[m :: pint][m%2==1][m>=3]
  [e2 :: pint][L :: uint][ps :: [pint]{len=L}][es :: [pint]{len=L}]
  # ps neednot be a set /distinguish
  [@[p :<- ps] -> [is_prime_(p)]]
  [e := 2**e2 * II ps[i]**es[i] {i :<- [0..<L]}]
  [g2 :: int][g2**(e///2) %m == m-1]
  [gs :: [int]{len=L}][@[i :<- [0..<L]] -> [gs[i]**(e///2///ps[i]) %m =!= m-1]][@[i :<- [0..<L]] -> [gs[i]**(e///2) %m == m-1]]
  ] -> [
  [phi(m) %e == 0]
  [[e == m-1] -> [is_prime_(m)]]
  ]
]

# using partial factorization
# using gcd
[[[m :: pint][m%2==1][m>=3]
  [e2 :: pint][L :: uint][fts :: [pint]{len=L}][es :: [pint]{len=L}]
  # fts neednot be pairwise-coprime
  [@[ft :<- fts] -> [[ft%2==1][ft>=3]]]
  [Bs :: [pint]{len=L}][@[i :<- [0..<L]] -> @[p4ft :<- all_prime_factors_of_(fts[i])] -> [p4ft >= Bs[i]]]
  [e5ft := 2**e2 * II fts[i]**es[i] {i :<- [0..<L]}]
  [e5B := 2**e2 * II Bs[i]**es[i] {i :<- [0..<L]}]
  [g2 :: int][g2**(e5ft///2) %m == m-1]
  [gs :: [int]{len=L}][@[i :<- [0..<L]] -> [gcd(gs[i]**(e5ft///2///fts[i]) %m +1, m) == 1]][@[i :<- [0..<L]] -> [gs[i]**(e5ft///2) %m == m-1]]

  ###
  [js := [i | [i :<- [0..<L]][fts[i] == Bs[i]]]]
  [ej := 2**e2 * II fts[j]**es[j] {j :<- js}]

  ] -> [
  ###
  [@[q4m :<- all_prime_factors_of_(m)] -> [(q4m-1) >= e5B]]
  [[(e5B+1)**2 > m] -> [is_prime_(m)]]

  ###
  [[e5ft == e5B] <==> [fts == Bs] <==> [@[ft :<- fts] -> [is_prime_(ft)]]]
  [[e5ft == e5B] -> [phi(m) %e5ft == 0]]
  [[e5ft == e5B] -> @[q4m :<- all_prime_factors_of_(m)] -> [(q4m-1) %e5ft == 0]]

  ###
  [e5ft %ej == 0]
  [e5B %ej == 0]
  [@[j :<- js] -> [is_prime_(fts[j])]]
  [[phi(m) %ej == 0][phi(m) ///ej >= e5B///ej][phi(m) >= e5B]]
  [@[q4m :<- all_prime_factors_of_(m)] -> [[(q4m-1) %ej == 0][(q4m-1) ///ej >= e5B///ej][(q4m-1) >= e5B]]]

  ###
  [[[e5ft==m-1][eF := ej][eR := e5ft///ej][gcd(eF,eR)==1]
    [u := if [e5ft%3 == 1] then 3 else 1]
    [(q,r) := eR /% (2*u*eF)]
    # [kB :: pint][[q4m :<- all_prime_factors_of_(m)] -> [(q4m-1)///eF >= kB]]
      # e.g. [kB := e5B] #but select best to max rhs=(kB*eF +1) * (((2*u*eF) +r -kB)*eF +1)
    [kB := min(e5B, (((2*u*eF) +r-1)///2))]
    [m < (kB*eF +1) * (((2*u*eF) +r -kB)*eF +1)]
    ] -> [
      [[is_prime_(m)] <-> [not$ [[r >= 2*kB][q >= ceil_(kB**2 /(2*u)) >= 1][sqrt(r**2 -8*u*q) %1 == 0]]]]
      [[[r >= 2*kB][q >= ceil_(kB**2 /(2*u)) >= 1][sqrt(r**2 -8*u*q) %1 == 0]] -> [
        [(s+t) == r]
        [(s-t) == sqrt(r**2 -8*u*q)]
        [m == (1+s*eF)*(1+t*eF)]
        ]]
      ]
    ]
  ]
]
]]
[[
copy from:
    view others/数学/prime/primality_test.txt
===
Miller's Test [Miller76]: If the extended Riemann hypothesis is true, then if n is an x-SPRP for all integers x with 1 < x < 2*(log n)**2 == 2*ln(n)**2, then n is prime.
    #require ERH
    2*ln(n)**2
heuristically we should be able to replace the bound in Miller's test with a bound near: (log 2)^-1 log n log log n.
  #heuristically
  #not exact
  ln(n)*lnln(n)/ln(2)
  log2(n)*lnln(n)


===
Note that there is no finite set of bases that will work in Miller's test.  In fact, if for n composite we let W(n) denote the least witness for n (the least x which shows n is composite), then there are infinitely many composite n with:
    [W(n) > (log n)**(1/(3 log log log n))]

===
Pocklington's Theorem (1914):  Let [n-1 = q**k *R] where q is a prime which does not divide R.  If there is an integer x such that [x**(n-1) %n == 1][gcd(x**((n-1)///q) %n -1,n) = 1, then each prime factor p of n has the form q**k*r+1.
    # [:Pocklington_Theorem_1914]:here
]]
[[
move from:
    #doc4Case4is_prime__Nmm_:here
===
view ../../python3_src/nn_ns/math_nn/numbers/b002233-least_positive_prime_primitive_root_of_n_th_prime__except_0th__fst_10000.txt
    [[least_positive_prime_primitive_root_of_(PRIMES[3417-1]) == 107][107 == PRIMES[27]][31771 == PRIMES[3416]][floor_log2(31771)==14][(31771-1)==II__p2e_({2: 1, 3: 2, 5: 1, 353: 1})]]
    ==>> [prime_bases<N> |>=| PRIMES[:1+2*floor_log2(N)]]
    ==>> [num_prime_bases<N> >= (1+2*floor_log2(N))]
===
view ../../python3_src/nn_ns/math_nn/numbers/b001918-least_positive_primitive_root_of_n_th_prime__fst_10000.txt
    [least_positive_primitive_root_of_(PRIMES[43-1]) == 19]
        43 19
        80 21
        326 23
        775 31
        3894 37
        5629 38
        7103 44

]]



from seed.math.primality_proving import *


py_adhoc_call   seed.math.primality_proving   @test_many4is_prime_ex__Nmm_ =10_00
py_adhoc_call   seed.math.primality_proving   @test_many4is_prime_ex__Nmm_ =16_00_00
py_adhoc_call   seed.math.primality_proving   @test_many4is_prime_ex__Nmm_ =20_00_00
    pass test!
    setting:
        using_prime_base_as_primitive_root_candidate_only
        one_plus_2floor_log2_P
        partial_primitive_roots__vs__primitive_root=False
        [2 <= N < 20_00_00]

py_adhoc_call   seed.math.primality_proving   ,200:iter_odd_primes__one_prime_per_bit_length_
(2, 3)
(3, 5)
(4, 13)
(5, 17)
(6, 41)
(7, 97)
(8, 241)
(9, 449)
(10, 641)
(11, 1217)
(12, 2113)
(13, None)
(14, None)
(15, None)
(16, None)
(17, 114689)
(18, None)
(19, None)
(20, 974849)
(21, None)
(22, 2424833)
(23, None)
(24, 13631489)
(25, 26017793)
(26, 63766529)
(27, None)
(28, 167772161)
... #choke


py_adhoc_call   seed.math.primality_proving   ,200:iter_odd_primes__one_prime_per_bit_length_   %seed.math.primality_proving:N2num_prime_bases__heuristically@f   --case4prime_bases=f
py_adhoc_call   seed.math.primality_proving   ,200:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases=...
(2, 3)
(3, 5)
(4, 13)
(5, 17)
(6, 41)
(7, 97)
(8, 193)
(9, 257)
(10, 769)
(11, 1153)
(12, 3329)
(13, 7681)
???ERH???: 12289
(14, 13313)
???ERH???: 18433
(15, 19457)
???ERH???: 40961
???ERH???: 61441
???ERH???: 59393
(16, 37889)
???ERH???: 65537
(17, 114689)
???ERH???: 163841
???ERH???: 147457
???ERH???: 188417
???ERH???: 151553
???ERH???: 176129
???ERH???: 184321
???ERH???: 249857
(18, 133121)
???ERH???: 270337
???ERH???: 286721
???ERH???: 319489
???ERH???: 417793
???ERH???: 307201
???ERH???: 331777
???ERH???: 380929
???ERH???: 430081
???ERH???: 471041
???ERH???: 495617
???ERH???: 520193
(19, 301057)
???ERH???: 786433
???ERH???: 557057
???ERH???: 638977
???ERH???: 737281
???ERH???: 1032193
???ERH???: 778241
???ERH???: 925697
(20, 974849)
???ERH???: 1179649
???ERH???: 1376257
???ERH???: 1769473
???ERH???: 1146881
???ERH???: 1097729
???ERH???: 1130497
???ERH???: 1196033
???ERH???: 1589249
???ERH???: 1720321
???ERH???: 1785857
^CTraceback (most recent call last):
    ...
KeyboardInterrupt

[[[
py_adhoc_call   seed.math.primality_proving   ,200:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases=...  +using_nonprime_gs4detect_primality
===
(2, 3)
(3, 5)
(4, 13)
(5, 17)
(6, 41)
(7, 97)
(8, 193)
(9, 257)
(10, 769)
(11, 1153)
(12, 3329)
(13, 7681)
(14, 12289)
(15, 18433)
(16, 40961)
(17, 65537)
(18, 163841)
(19, 270337)
(20, 786433)
(21, 1179649)
(22, 2752513)
(23, 7340033)
(24, 13631489)
(25, 23068673)
(26, 36175873)
(27, 104857601)
(28, 167772161)
(29, 469762049)
(30, 754974721)
(31, 2013265921)
(32, 3221225473)
(33, 7918845953)
(34, 12348030977)
(35, 24159191041)
(36, 52613349377)
(37, 77309411329)
(38, 206158430209)
(39, 313532612609)
(40, 850403524609)
(41, 2061584302081)
(42, 2748779069441)
(43, 6597069766657)
(44, 17317308137473)
(45, 29686813949953)
(46, 39582418599937)
(47, 79164837199873)
(48, 263882790666241)
(49, 474989023199233)
(50, 1108307720798209)
(51, 1337006139375617)
(52, 4222124650659841)
(53, 7881299347898369)
(54, 12947848928690177)
(55, 31525197391593473)
(56, 38280596832649217)
(57, 112589990684262401)
(58, 180143985094819841)
(59, 459367161991790593)
(60, 882705526964617217)
(61, 1945555039024054273)
(62, 4179340454199820289)
(63, 6269010681299730433)
(64, 15564440312192434177)
(65, 35740566642812256257)
(66, 51881467707308113921)
(67, 83010348331692982273)
(68, 221360928884514619393)
(69, 332041393326771929089)
(70, 691752902764108185601)
(71, 1328165573307087716353)
(72, 2434970217729660813313)
(73, 9149585060559937601537)
(74, 13576803638250229989377)
(75, 32613843522318487257089)
(76, 46043073207979040833537)
(77, 92086146415958081667073)
(78, 188894659314785808547841)
(79, 368344585663832326668289)
(80, 1095589024025757689577473)
(81, 1265594217409064917270529)
(82, 4533471823554859405148161)
(83, 7555786372591432341913601)
(84, 10955890240257576895774721)
(85, 21760664753063325144711169)
(86, 62864142619960717084721153)
(87, 150511264542021332250918913)
(88, 193428131138340667952988161)
(89, 493241734402768703280119809)
(90, 715684085211860471426056193)
(91, 2050338190066411080301674497)
(92, 2514565704798428683388846081)
(93, 6731298963614255244763987969)
(94, 18878585599102049192211644417)
(95, 34662321099990647697175478273)
(96, 70562582239266675669250080769)
(97, 133697524242821069689105416193)
(98, 287202089114208223776596819969)
(99, 326816170371340392573368795137)
(100, 851702747028341629130597466113)
(101, 1683598453428117173862808944641)
(102, 4516005263313067242832005169153)
(103, 9586607664225984848818817990657)
(104, 13627243952453466066089559457793)
(105, 20757778578737256449508514988033)
(106, 49913742383986532683932688711681)
(107, 138807740724991119463889000988673)
(108, 294094939252949221147235143647233)
(109, 339730360861165479601116459040769)
(110, 872143612957021828229731805298689)
(111, 2149935417987077064938408636317697)
(112, 3001796621340447222744193190330369)
(113, 9370473236887071735863630094139393)
(114, 17037224067067403156115691080253441)
(115, 30180225490233685590833509913591809)
(116, 77884452878022414427957444938301441)
(117, 94759417668260604220681558008266753)
(118, 246634100780404312355198575637954561)
(119, 334903147375496382040217013234696193)
(120, 794421419355828627165165938370674689)
(121, 2388456554926020709124028311441244161)
(122, 3385377551764707613801883606651502593)
(123, 9304595970494411110326649421962412033)
(124, 10966130965225555951456408247312842753)
(125, 33895313892515354759047080037148786689)
(126, 47187593850364513488085150639952232449)
(127, 117636677626965054751986924834810494977)
(128, 215334935317156371410416743765415821313)
(129, 467888254516290387262140085218681290753)
(130, 850705917302346158658436518579420528641)
(131, 1871553018065161549048560340874725163009)
(132, 3445358965074501942566667900246653140993)
(133, 7145929705339707732730866756067132440577)
(134, 14291859410679415465461733512134264881153)
(135, 37771342728224169444434581424926271471617)
(136, 44236707699722000250238698966129867489281)
^CTraceback (most recent call last):
    ...
KeyboardInterrupt
]]]


#]]]'''
if 0:
    __all__ = r'''
Error
    ValidateFail
        ValidateFail__order_mod_
        ValidateFail__order_mod__proper_factor
        ValidateFail__order_mod__not_order
        ValidateFail__order_mod__not_corresponding_partial_primitive_root
    PrimalityFail
        PrimalityFail__is_prime_ex__Nmm_____assume_case


    validate_order_mod_
    validate_primality__Pmm_
    Case4is_prime__Nmm____how_to_find_primitive_root
    Case4is_prime__Nmm____how_many_prime_bases_to_be_test
    ResultCase4is_prime__Nmm_
    default_case4num
    default_case4root
    is_prime__Nmm_
    is_prime_ex__Nmm_
    test_many4is_prime_ex__Nmm_
    test_one4is_prime_ex__Nmm_
'''.split()#'''
__all__ = r'''
    iter_pow_IIs_except_one_
    iter_pow_II1_except_one_
    validate_primality__Nmm__complete_factorization_
    validate_primality__Nmm_
    N2num_prime_bases__ERH
    N2num_prime_bases__heuristically
    N2num_prime_bases__tiny__one_plus_2floor_log2_P
    iter_detect_primality__Nmm_
    Error
    ValidateFail
    ValidateFail__order_mod_
    ValidateFail__order_mod__proper_factor
    ValidateFail__order_mod__not_order
    ValidateFail__nonprime
    ValidateFail__nonprime__nontrivial_factor
    ValidateFail__bad_setting
    DetectPrimalityFail
    DetectPrimalityFail__bad_setting
    DetectPrimalityFail__bad_setting__cannot_conform_primality
    DetectPrimalityFail__bad_setting__too_few_num_prime_bases



    is_composite_ex__Nmm_
        is_composite__Nmm_
        validate_result5is_composite_ex__Nmm_

    test_many4is_composite_ex__Nmm_
        test_one4is_composite_ex__Nmm_
    iter_odd_primes__one_prime_per_bit_length_
        iter_odd_primes__Pocklington_Theorem_1914__factor_2s__bit_length_
'''.split()#'''
__all__

def __():
    #API
    ...

if 1:
    from seed.iters.apply_commutative_operations_except_one import iter_apply_commutative_operations_except_one_
    #def iter_apply_commutative_operations_except_one_(apply_, commutative_operation_keys, x0, /):
    from seed.math.II import II, II_mod, II__p2e_, II__ft2e_, II__ft_e_pairs_
    from seed.math.gcd import gcd
    from seed.math.floor_ceil import floor_log2
    from seed.mapping_tools.dict_op import inv__k2v_to_v2ks

    #from seed.seq_tools.split_tuples import split_tuples, unzip_pairs
    #from seed.iters.difference_of_two_sorted_iterables import difference_of_two_sorted_iterables
    from seed.seq_tools.remove_strict_sorted_indices import lsls2lsls_pair__via_idc_ #ls2ls_pair__via_idc_
    from seed.seq_tools.remove_strict_sorted_indices import iter_complement_idc_, iter_values__via_idc_
    from seed.seq_tools.remove_strict_sorted_indices import list_rngs__via_idc_, list_values__via_idc_, list_idc4reserve_, list_complement_idc_
    from seed.math.floor_ceil import floor_sqrt #perfect_div, perfect_kth_root_

    from seed.math.prime_gens import prime_gen
    from seed.tiny import print_err
    from seed.tiny import check_type_is
    from seed.tiny_.check import check_int_ge, check_uint_lt, check_int_ge_lt # check_int_ge_le
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
    from seed.math.prime_gens import tabulate_may_factorization4uint_lt_# min_prime_factor_gen, tabulate_may_min_prime_factor4uint_lt_
    #def tabulate_may_factorization4uint_lt_(sz, uint2may_min_prime_factor=None, /):
    #    '-> uint2may_factorization/[may p2e/{prime:exp}]/[None,p2e...]'

    from itertools import count as count_

def __():
    from enum import Enum, auto
    from seed.mapping_tools.dict_op import inv__k2v_to_v2k, inv__k2v_to_v2ks, inv__k2vs_to_v2k, inv__k2vs_to_v2ks
    from seed.math.prime_gens import is_strong_pseudoprime_
    #def is_strong_pseudoprime_(base, n, /, *, to_find_sqrt_neg1=False):
    #    'base/int{>=2,%n=!=0} -> n{>=3,odd} -> [n is base-SPRP]'


_int_pow_ = int.__pow__
def _int_pow(base, exp, modulus, /):
    assert modulus > 1
    if base+1 == modulus:
        return 1 if exp&1==0 else base
    return _int_pow_(base, exp, modulus)
class _pow_ne_:
    def __init__(sf, modulus, ne, Err, /):
        sf.modulus = modulus
        sf.ne = ne
        sf.Err = Err
    def __call__(sf, base, exp, /):
        x = _int_pow(base, exp, sf.modulus)
        if x == sf.ne:
            raise sf.Err
        return x

def __():
  def _pow_(modulus, base, exp, /):
    return _int_pow(base, exp, modulus)
    assert exp >= 0
    if exp >= 2:
        if not -modulus < (base<<1) < modulus:
            base %= modulus
            base -= modulus
        if abs(base) < 2:
            if base == -1 and (exp&1 == 0):
                base = 1
            return base
    return _int_pow(base, exp, modulus)

def _mk_x_(_pow_, ft_e_pairs, g, /):
    x = g
    for ft, e in ft_e_pairs:
        for _ in range(e):
            x = _pow_(x, ft)
    return x
def _mk_x1_(_pow_, fts, es, g, /):
    ft_e_pairs = zip(fts, es)
    x1 = _mk_x_(_pow_, ft_e_pairs, g)
    return x1
def _mk_x0_(_pow_, fts, es, g, /):
    ft_e_pairs = zip(fts, es)
    ft_emm_pairs = [(ft, e-1) for ft, e in ft_e_pairs if e >= 1]
    x0 = _mk_x_(_pow_, ft_emm_pairs, g)
    return x0
def iter_pow_IIs_except_one_(_pow_, fts, es, g, /):
    x0 = _mk_x0_(_pow_, fts, es, g)
    return iter_pow_II1_except_one_(_pow_, fts, x0)
def iter_pow_II1_except_one_(_pow_, fts, x0, /):
    def apply_(ft, x, /):
        x = _pow_(x, ft)
        return x
    return iter_apply_commutative_operations_except_one_(apply_, fts, x0)

def validate_primality__Nmm__complete_factorization_(e2, ps, es, g2, gs, /):
    r'''
    [@[p :<- ps] -> [is_prime_(p)]]
    '''#'''
    # not using gcd
    assert len(ps) ==  len(es) ==  len(gs)
    assert all(p&1 == 1 for p in ps)
    assert all(p >= 3 for p in ps)
    assert all(e >= 1 for e in es)
    L = len(ps)
    assert e2 >= 0
    assert e2 >= 1 or L==0

    p_e_pairs = [*zip(ps, es)]
    Nmm = II__ft_e_pairs_(p_e_pairs) << e2
    assert Nmm >= 1
    N = Nmm+1
    assert N >= 2
    if N <= 3: return
    assert e2 >= 1
    assert e2 >= 2 or L >= 1
    #_es[0] -= 1
    # if e2==0: del _es[0], ...
    #_pow_ = _pow_ne_(N, Nmm, ValidateFail__order_mod__proper_factor)
    #   Nmm: too tedious to handle [e2==1]
    #to check:xxx since too tedious to handle [e2==1]
        #[g2 :: int][g2**(e///2) %m == m-1]
        #[gs :: [int]{len=L}][@[i :<- [0..<L]] -> [gs[i]**(e///2///ps[i]) %m =!= m-1]][@[i :<- [0..<L]] -> [gs[i]**(e///2) %m == m-1]]
    #to check:
        #[g2 :: int][g2**(e///2) %m =!= 1][g2**e %m == 1]
        #[gs :: [int]{len=L}][@[i :<- [0..<L]] -> [gs[i]**(e///ps[i]) %m =!= 1]][@[i :<- [0..<L]] -> [gs[i]**e %m == 1]]

    #_pow_ = _pow_ne_(modulus, modulus-1, ValidateFail__order_mod__proper_factor)
    _main_loop4validate__Nmm_(e2, ps, es, g2, gs, N, using_gcd=False)
    return
def _main_loop4validate__Nmm_(e2, fts, es, g2, gs, N, /, *, using_gcd):
    _fts = [2, *fts]
    _es = [e2, *es]
    _gs = [g2, *gs]
    g2js = inv__k2v_to_v2ks(_gs, True, set_vs_list=True)
    _pow_ = _pow_ne_(N, 1, ValidateFail__order_mod__proper_factor)

    g_js_pairs = sorted(g2js.items(), key=lambda kv:kv[1][0])
    assert g_js_pairs[0][0] == g2
    assert g_js_pairs[0][1][0] == 0
    assert _es[0] == e2
    assert _fts[0] == 2
    for g, js in g_js_pairs:
        #ks = difference_of_two_sorted_iterables(range(L), js)
        ([selected_fts, selected_es], [unselected_fts, unselected_es]) = lsls2lsls_pair__via_idc_(js, [_fts, _es])
        g0 = _mk_x1_(_pow_, unselected_fts, unselected_es, g)
        it = iter_pow_IIs_except_one_(_pow_, selected_fts, selected_es, g0)
        for i, x in enumerate(it):
            #assert not x == 1
            #   valid via _pow_/_pow_ne_
            if i==0:
                j = js[i]
                _ft = _fts[j]
                #_e = _es[j]
                if not _int_pow(x, _ft, N) == 1:
                    raise ValidateFail__order_mod__not_order
            #####
            if using_gcd:
                if not (ft4m := gcd(x-1, N)) == 1:
                    if not 1 < ft4m < N: raise 000
                    assert N %ft4m == 0
                    raise ValidateFail__nonprime__nontrivial_factor(ft4m)
    return
def validate_primality__Nmm_(e2, fts, es, Bs, g2, gs, /):
    r'''
    [@[ft :<- fts] -> [[ft%2==1][ft>=3]]]
    [Bs :: [pint]{len=L}][@[i :<- [0..<L]] -> @[p4ft :<- all_prime_factors_of_(fts[i])] -> [p4ft >= Bs[i]]]
    '''#'''
    assert len(fts) ==  len(es) ==  len(Bs) ==  len(gs)
    L = len(fts)
    assert all(ft&1 == 1 for ft in fts)
    assert all(ft >= 3 for ft in fts)
    assert all(B >= 3 for B in Bs)
    assert all(ft >= B for ft, B in zip(fts, Bs))
    assert e2 >= 0
    assert e2 >= 1 or L==0
    if e2 == 0:
        if not L == 0:
            raise ValidateFail__nonprime__nontrivial_factor(2)
        N = 2
        if not g2&1 == 1: raise ValidateFail__bad_setting
        return

    assert e2 >= 1

    js = [i for i in range(L) if fts[i] == Bs[i]]
    if len(js) == L:
        ps = fts
        validate_primality__Nmm__complete_factorization_(e2, ps, es, g2, gs)
    else:
        _validate_primality__Nmm__partial_factorization_(e2, fts, es, Bs, g2, gs, js)
    return

def _ex_check_setting4validate_primality__Nmm__partial_factorization_(e2, fts, es, Bs, js, /):
    r'''
    -> (may_ft4m, N) | ^ValidateFail__bad_setting | ^ValidateFail__nonprime__nontrivial_factor

    [@[ft :<- fts] -> [[ft%2==1][ft>=3]]]
    [Bs :: [pint]{len=L}][@[i :<- [0..<L]] -> @[p4ft :<- all_prime_factors_of_(fts[i])] -> [p4ft >= Bs[i]]]
    '''#'''

    # using gcd
    assert e2 >= 1
    L = len(fts)
    assert L >= 1

    js
    cs = list_complement_idc_(L, js)

    #js:
    ps = list_values__via_idc_(js, fts)
    es4p = list_values__via_idc_(js, es)

    #cs:
    fts4np = list_values__via_idc_(cs, fts)
    Bs4np = list_values__via_idc_(cs, Bs)
    es4np = list_values__via_idc_(cs, es)

    ej = II__ft_e_pairs_(zip(ps, es4p)) << e2
    eR = II__ft_e_pairs_(zip(fts4np, es4np))
    e5ft = ej * eR
    e5B = ej * II__ft_e_pairs_(zip(Bs4np, es4np))
    # [e5ft := 2**e2 * II fts[i]**es[i] {i :<- [0..<L]}]
    # [e5B := 2**e2 * II Bs[i]**es[i] {i :<- [0..<L]}]
    # [ej := 2**e2 * II fts[j]**es[j] {j :<- js}]
    111; js=None # del js

    Nmm = e5ft
    N = Nmm+1
    assert N >= 7

    may_ft4m = None
    if N < (e5B+1)**2:
        pass
    else:
        m = N
        eF = ej
        eR
        #assert m == 1+eF*eR
        if not gcd(eF,eR)==1: raise ValidateFail__bad_setting

        #u = if e5ft%3 == 1 then 3 else 1
        u = 3 if m%3 == 2 else 1
        _2_u_eF = (2*u*eF)
        (q, r) = divmod(eR, _2_u_eF)
        assert eR&1 == 1
        assert r&1 == 1

        kB = min(e5B, ((_2_u_eF +r-1)>>1))
        assert kB >= 1
        if not m < (kB*eF +1) * ((_2_u_eF +r -kB)*eF +1): raise ValidateFail__bad_setting
        # [gcd...to check ] => [[is_prime_(m)] <-> [not$ [[r >= 2*kB][q >= ceil_(kB**2 /(2*u)) >= 1][sqrt(r**2 -8*u*q) %1 == 0]]]]
        if r >= 2*kB and 2*u*q >= kB**2 and (sq := r**2 -8*u*q) >= 0 and (sqrt := floor_sqrt(sq))**2 == sq:
            # [(s+t) == r]
            # [(s-t) == sqrt(r**2 -8*u*q)]
            # [m == (1+s*eF)*(1+t*eF)]
            assert q > 0
            r, sqrt
            assert r&1 == 1
            assert sqrt&1 == 1
            assert 0 <= sqrt < r
            s = (r+sqrt)//2
            t = (r-sqrt)//2
            assert 0 < t < s

            may_ft4m = ft4m = (1+t*eF)
            #not check gcd yet:
                #assert m == (1+s*eF)*(1+t*eF)

                #assert 1 < ft4m < m
                #assert m %ft4m == 0
            if 1 < ft4m < m and m %ft4m == 0:
                raise ValidateFail__nonprime__nontrivial_factor(ft4m)
            # [may_ft4m is not None]
                # below should raise ValidateFail
    return (may_ft4m, N)

def _validate_primality__Nmm__partial_factorization_(e2, fts, es, Bs, g2, gs, js, /):
    # [@[ft :<- fts] -> [[ft%2==1][ft>=3]]]
    # [Bs :: [pint]{len=L}][@[i :<- [0..<L]] -> @[p4ft :<- all_prime_factors_of_(fts[i])] -> [p4ft >= Bs[i]]]
    (may_ft4m, N) = _ex_check_setting4validate_primality__Nmm__partial_factorization_(e2, fts, es, Bs, js)


    ######################
    ######################
    ######################
    # check ... gcd
    #to check:
        # [g2 :: int][g2**(e5ft///2) %m == m-1]
        # [gs :: [int]{len=L}][@[i :<- [0..<L]] -> [gcd(gs[i]**(e5ft///2///fts[i]) %m +1, m) == 1]][@[i :<- [0..<L]] -> [gs[i]**(e5ft///2) %m == m-1]]
    #to check:
        # [g2 :: int][gcd(g2**(e5ft///2) %m -1, m) == 1][g2**e5ft %m == 1]
        # [gs :: [int]{len=L}][@[i :<- [0..<L]] -> [gcd(gs[i]**(e5ft///fts[i]) %m -1, m) == 1]][@[i :<- [0..<L]] -> [gs[i]**e5ft %m == 1]]
    _main_loop4validate__Nmm_(e2, fts, es, g2, gs, N, using_gcd=True)
    #return



    ######################
    ######################
    ######################
    if not may_ft4m is None:
        #above should raise ValidateFail
        raise 000
    return






class _detect_compositeness__Nmm:
    def __init__(sf, e2, fts, es, N, max1_len_rootss, /):
        assert e2 >= 1
        assert N >= 3
        assert N&1 == 1
        max1_len_rootss = max(2, min(1+e2, max1_len_rootss))
        assert 2 <= max1_len_rootss <= 1+e2
        sf.args = (e2, fts, es, N, max1_len_rootss)
        sf.rootss = [[1], [N-1]] # ++[set<root>]
            # [len(rootss[i]) == 2**max(0,i-1)]
            # [0 <= i < max(2, min(1+e2, max1_len_rootss))]
    #def __call__(sf, gs, /):
    def iter_call_gs(sf, gs, /):
        'gs/[int{abs<-[1..<N]}] -> Iter ((unknown/..., (x0__but2, g_is_g2)) | (is_composite/True, <0:witness4composite|1:nontrivial_factor>)) # primality_test_of_Miller_Rabin'
        for g in gs:
            r = sf.call_g(g)
            yield r
            (case, payload) = r
            if not case is ...:
                break
        return
    def call_g(sf, g, /):
        'g/int{abs<-[1..<N]} -> ((unknown/..., (x0__but2, g_is_g2)) | (is_composite/True, <0:witness4composite|1:nontrivial_factor>)) # primality_test_of_Miller_Rabin'
        try:
            r = sf._call_g_(g)
        except _ToReturn as exc:
            [r] = exc.args
        return r
    def _call_g_(sf, g, /):
        (e2, fts, es, N, max1_len_rootss) = sf.args
        rootss = sf.rootss
        assert 0 < abs(g) < N

        L = len(fts)
        Nmm = rootss[1][0]

        _pow_ = _pow_ne_(N, 1, _ToReturn((..., (1,False))))
            # (x0__but2, g_is_g2)
        x0__but2 = _mk_x0_(_pow_, fts, es, g)
        _pow_ = _pow_ne_(N, 1, _ToReturn((..., (x0__but2,False))))
        x1__but2 = _mk_x1_(_pow_, fts, [1]*L, x0__but2)
        _pow_ = None

        xs = []
        x = x1__but2
        if x == 1:
            pass
        #to simplify witness4composite____validate_result5is_composite_ex__Nmm_
            # ==>> sqrt_mod_(N; +1) besides {+1,-1} will be used to find out nontrivial_factor
        #elif x == Nmm:
        #    xs.append(Nmm)
        #    pass
        else:
            #to simplify witness4composite____validate_result5is_composite_ex__Nmm_
                #for _ in range(e2-1):
            for _ in range(e2):
                xs.append(x)
                x = _int_pow(x, 2, N)
                #to simplify witness4composite____validate_result5is_composite_ex__Nmm_
                #if x == Nmm:
                #    xs.append(Nmm)
                    # [xs[-1] == Nmm]
                #    break
                if x == 1:
                    # [xs[-1] =!= Nmm]
                    break
            else:
                if 0:
                    #to simplify witness4composite____validate_result5is_composite_ex__Nmm_
                    assert not x == Nmm
                    # [1 =!= x =!= Nmm][0 <= x < N]
                    # [1 =!= x < Nmm]
                #####
                # [x =!= 1][0 <= x < N]

                # [1 =!= x < N]
                if x == 0:
                    ft4m = gcd(g, N)
                    if ft4m == N: raise ValueError
                    assert 1 < ft4m < N
                    assert N %ft4m == 0
                    return (True, (1,ft4m))
                # [1 < x < N]
                assert 2 <= x < N
                #assert 2 <= abs(g) < N
                assert 1 <= abs(g) < N
                witness4composite = g
                return (True, (0,witness4composite))
            pass
        #
        xs.append(1)
        xs.reverse() # [1,...]
        del xs[max1_len_rootss:]
        r = sf._update_roots(xs)
        if not r is ...:
            return r
        if 0:
            #bug:
            g_is_g2 = len(xs) > 1 and (xs[1]==Nmm)
            if not len(xs) == 1:
                assert g_is_g2
        else:
            g_is_g2 = len(xs) == 1+e2 and (xs[1]==Nmm)

        return (..., (x0__but2, g_is_g2))
    def _update_roots(sf, xs, /):
        '-> emay result'
        def f(N, xx, x, rts, /):
            assert x not in rts
            for y in rts:
                yy = _int_pow(y, 2, N)
                if yy == xx:
                    break
            else:
                raise 000
            ft4m = gcd(x+y, N)
            assert 1 < ft4m < N
            assert N %ft4m == 0
            return (True, (1,ft4m))

        (e2, fts, es, N, max1_len_rootss) = sf.args
        rootss = sf.rootss
        assert xs, xs
        assert xs[0] == 1
        begin = min(len(xs), len(rootss))
        end = min(len(xs), max1_len_rootss)
        for i in reversed(range(0, begin)):
            if xs[i] in rootss[i]:
                if not i == begin-1:
                    assert not xs[i+1] in rootss[i+1]
                    return f(N, xs[i], xs[i+1], rootss[i+1])

                break

        # extend rootss
        for i in range(begin, end):
            x = xs[i]
            rs = {rt*x %N for rs_ in rootss for rt in rs_}
            rootss.append(rs)
        return ...

class _detect_primality__Nmm:
    def __init__(sf, e2, fts, es, N, using_gcd, /):
        '[using_gcd is True] <==> [fts are all prime]'
        assert e2 >= 1
        assert N >= 3
        assert N&1 == 1
        _fts = [2, *fts]
        _es = [e2, *es]
        L = len(_fts)
        j2g = [None]*L
        js = [*range(L)]
        sf.args = (e2, fts, es, N, using_gcd, _fts, _es)
        sf._set_new_state(js, j2g)
    def _set_new_state(sf, js, j2g, /):
        sf.state = js, j2g
        (e2, fts, es, N, using_gcd, _fts, _es) = sf.args

        L = len(_fts)
        cs = list_complement_idc_(L, js)
        fts4known_g = list_values__via_idc_(cs, _fts)
        es4known_g = list_values__via_idc_(cs, _es)

        fts4unknown_g = list_values__via_idc_(js, _fts)
        es4unknown_g = list_values__via_idc_(js, _es)

        sf.state_ex = (cs, fts4known_g, es4known_g, fts4unknown_g, es4unknown_g)

    #def __call__(sf, gs, /):
    def iter_call_gs(sf, gs, may_exss, /):
        'gs/[int{abs<-[1..<N]}] -> Iter ((is_prime/False, (delta_js, j2g)) | (unknown/..., (delta_js, j2may_g)) | (is_composite/True, <0:witness4composite|1:nontrivial_factor>))'
        for g, may_exs in zip(gs, may_exss):
            r = sf.call_g(g, may_exs)
            yield r
            (case, payload) = r
            if not case is ...:
                break
        return

    def call_g(sf, g, may_exs, /):
        'g/int{abs<-[1..<N]} -> ((is_prime/False, (delta_js, j2g)) | (unknown/..., (delta_js, j2may_g)) | (is_composite/True, <0:witness4composite|1:nontrivial_factor>))'
        try:
            r = sf._call_g_(g, may_exs)
        except _ToReturn as exc:
            [r] = exc.args
        (case, payload) = r
        if case is ...:
            (delta_js, j2g) = payload
            js, j2g = sf.state
            if delta_js:
                for j in delta_js:
                    j2g[j] = g
                js = [j for j in js if j2g[j] is None]
                sf._set_new_state(js, j2g)
            if not js:
                case = False
                r = case, (delta_js, j2g)
                # [N is prime]
            pass
        return r

    def _call_g_(sf, g, may_exs, /):
        'g/int{abs<-[1..<N]} -> ((unknown/..., (delta_js, j2may_g)) | (is_composite/True, <0:witness4composite|1:nontrivial_factor>))'
        (e2, fts, es, N, using_gcd, _fts, _es) = sf.args
        js, j2g = sf.state
        assert 0 < abs(g) < N

        delta_js = []
        if not js:
            return (..., (delta_js, j2g))

        (cs, fts4known_g, es4known_g, fts4unknown_g, es4unknown_g) = sf.state_ex
        _pow_ = _pow_ne_(N, 1, _ToReturn((..., (delta_js, j2g))))
        if not may_exs is None:
            (x0__but2, g_is_g2) = may_exs
            #if x0__but2 == 1:
            if fts4unknown_g == [2]:
                if g_is_g2:
                    assert not x0__but2 == 1
                    assert js == [0]
                    #bug:delta_js.append(2)
                    delta_js.append(0)
                    pass
                return (..., (delta_js, j2g))
        else:
            x0__but2 = _mk_x0_(_pow_, fts, es, g)
        x0__but2
        x0 = _mk_x0_(_pow_, [2], [e2], x0__but2)

        x04unknown_g = _mk_x1_(_pow_, fts4known_g, [1]*len(fts4known_g), x0)

        _pow_ = _pow_ne_(N, None, None)
        it = iter_pow_II1_except_one_(_pow_, fts4unknown_g, x04unknown_g)
        for i, x in enumerate(it):
            #may have [x == 1]
            if x == 1:
                continue

            if i==0:
                j = js[i]
                _ft = _fts[j]
                #_e = _es[j]
                if not _int_pow(x, _ft, N) == 1:
                    # [1 =!= x < N]
                    if x == 0:
                        ft4m = gcd(g, N)
                        if ft4m == N: raise ValueError
                        assert 1 < ft4m < N
                        assert N %ft4m == 0
                        return (True, (1,ft4m))
                    # [1 < x < N]
                    assert 2 <= x < N
                    #assert 2 <= abs(g) < N
                    assert 1 <= abs(g) < N
                    witness4composite = g
                    return (True, (0,witness4composite))
                pass
            #####
            if using_gcd:
                if not (ft4m := gcd(x-1, N)) == 1:
                    if not 1 < ft4m < N: raise 000
                    assert N %ft4m == 0
                    return (True, (1,ft4m))
            #####
            j = js[i]
            delta_js.append(j)
        return (..., (delta_js, j2g))

#_detect_compositeness__Nmm(e2, fts, es, N, max1_len_rootss)
#_detect_primality__Nmm(e2, fts, es, N, using_gcd)
validate_primality__Nmm_
def N2num_prime_bases__ERH(N, /):
    '-> 2*floor_log2(N)**2 # >= # ERH => 2*ln(n)**2'
    #NOTE:原文上限用于 [2..<2*ln(n)**2] 并非 素数；这里 用作 PRIMES[:num_prime_bases]
    return 2*floor_log2(N)**2
def N2num_prime_bases__heuristically(N, /):
    '-> floor_log2(N)*max(1, floor_log2(floor_log2(N))) # ~= log2(n)*lnln(n)'
    #NOTE:原文上限用于 [2..<log2(n)*lnln(n)] 并非 素数；这里 用作 PRIMES[:num_prime_bases]
    flbN = floor_log2(N)
    flb_flbN = floor_log2(flbN)
    return flbN*max(1, flb_flbN)
def N2num_prime_bases__tiny__one_plus_2floor_log2_P(N, /):
    '-> (1+2*floor_log2(N)) #one_plus_2floor_log2_P'
    flbN = floor_log2(N)
    return 1+2*flbN
assert floor_log2(3) == 1
assert floor_log2(1) == 0
assert N2num_prime_bases__ERH(3) == 2
assert N2num_prime_bases__heuristically(3) == 1
assert N2num_prime_bases__tiny__one_plus_2floor_log2_P(3) == 3

assert floor_log2(5) == 2
assert floor_log2(2) == 1
assert N2num_prime_bases__ERH(5) == 8
assert N2num_prime_bases__heuristically(5) == 2
assert N2num_prime_bases__tiny__one_plus_2floor_log2_P(5) == 5

assert N2num_prime_bases__heuristically(7) == 2

assert floor_log2(16) == 4
assert floor_log2(4) == 2
assert floor_log2(256-1) == 7
assert floor_log2(8-1) == 2
assert floor_log2(256) == 8
assert floor_log2(8) == 3
assert N2num_prime_bases__ERH(256) == 128
assert N2num_prime_bases__heuristically(256) == 24
assert N2num_prime_bases__tiny__one_plus_2floor_log2_P(256) == 17

def iter_detect_primality__Nmm_(e2, fts, es, Bs, case4prime_bases, N2max1_len_rootss=None, /, *, using_nonprime_gs4detect_primality):
    r'''
    -> Iter ((is_prime/False, (delta_js, j2g)) | (unknown/..., (delta_js, j2may_g)) | (is_composite/True, <0:witness4composite|1:nontrivial_factor>))

    [@[ft :<- fts] -> [[ft%2==1][ft>=3]]]
    [Bs :: [pint]{len=L}][@[i :<- [0..<L]] -> @[p4ft :<- all_prime_factors_of_(fts[i])] -> [p4ft >= Bs[i]]]


    '''#'''
    assert len(fts) ==  len(es) ==  len(Bs)
    L = len(fts)
    assert all(ft&1 == 1 for ft in fts)
    assert all(ft >= 3 for ft in fts)
    assert all(B >= 3 for B in Bs)
    assert all(ft >= B for ft, B in zip(fts, Bs))
    assert e2 >= 0
    assert e2 >= 1 or L==0
    if e2 == 0:
        if not L == 0:
            is_composite = True
            ft4m = 2
            yield (is_composite, (1,ft4m))
            return
        N = 2
        is_composite = False
        #j2g = [1]
        j2g = [] #e2==0
        yield (is_composite, ([], j2g))
        return

    assert e2 >= 1


    js = [i for i in range(L) if fts[i] == Bs[i]]
    using_gcd = len(js) < L

    if using_gcd:
        assert L > 0
        try:
            (may_ft4m, N) = _ex_check_setting4validate_primality__Nmm__partial_factorization_(e2, fts, es, Bs, js)
        except ValidateFail__bad_setting:
            raise DetectPrimalityFail__bad_setting
        except ValidateFail__nonprime__nontrivial_factor as exc:
            [ft4m] = exc.args
            is_composite = True
            yield (is_composite, (1,ft4m))
            return
    else:
        may_ft4m = None
        N = 1 +(II__ft_e_pairs_(zip(fts, es)) << e2)

    assert N >= 3
    num_prime_bases = _calc_num_prime_bases(case4prime_bases, N)
    if N2max1_len_rootss is None:
        # total num roots <= 2**(max1_len_rootss-1)
        max1_len_rootss = 3+floor_log2(num_prime_bases)
    else:
        max1_len_rootss = N2max1_len_rootss(N)
    max1_len_rootss = max(3, max1_len_rootss)

    gs = _list_prime_bases4N(num_prime_bases, N)

    N, max1_len_rootss, using_gcd
    dc = _detect_compositeness__Nmm(e2, fts, es, N, max1_len_rootss)
    if not may_ft4m is None:
        # _detect_compositeness__Nmm only
        #   since cannot conform primality
        for r in dc.iter_call_gs(gs):
            is_composite = r[0]
            if is_composite is ...:
                pass
            elif is_composite is True:
                yield r
                return
            else:
                raise 000
        raise DetectPrimalityFail__bad_setting__cannot_conform_primality
        pass
    else:
        dc
        dp = _detect_primality__Nmm(e2, fts, es, N, using_gcd)
        gs
        if not using_nonprime_gs4detect_primality:
            gaps = ''
        else:
            gaps = iter_complement_idc_(gs[-1]+1, gs)
            if not next(gaps) == 0: raise 000
            if not next(gaps) == 1: raise 000
        #####
        #sfs = dc, dp
        for g in gs:
            r = dc.call_g(g)
            (case, payload) = r
            if not case is ...:
                assert case is True
                yield r
                return
            may_exs = (x0__but2, g_is_g2) = payload

            # dc MUST BE before dp
            r = dp.call_g(g, may_exs)
            yield r
            (case, payload) = r
            if not case is ...:
                return
        for g in gaps:
            r = dp.call_g(g, None)
            yield r
            (case, payload) = r
            if not case is ...:
                return

        raise DetectPrimalityFail__bad_setting__too_few_num_prime_bases
        pass
    raise 000


    ######################
    if not may_ft4m is None:
        #above should raise ValidateFail
        raise 000
    return

#end-def iter_detect_primality__Nmm_(e2, fts, es, Bs, case4prime_bases, N2max1_len_rootss=None, /, *, using_nonprime_gs4detect_primality):

#def _calc_num_prime_bases(N2num_prime_bases, N, /):
def _calc_num_prime_bases(case4prime_bases, N, /):
    assert N >= 3
    if callable(case4prime_bases):
        N2num_prime_bases = case4prime_bases
    elif type(case4prime_bases) is int:
        N2num_prime_bases = lambda N:case4prime_bases
    else:
        raise 000
        N2num_prime_bases = ...
    num_prime_bases = N2num_prime_bases(N)
    num_prime_bases = max(1, num_prime_bases)
    return num_prime_bases
def _list_prime_bases4N(num_prime_bases, N, /):
    assert N >= 3
    halfN = N // 2
    prime_bases = [*prime_gen[:num_prime_bases]]
    for i, g in enumerate(prime_bases):
        if g > halfN:
            #Note: [N==3][g==2]
            del prime_bases[i+1:]
            assert prime_bases[-1] is g
            break
    assert prime_bases
    assert prime_bases[0] == 2
    return prime_bases
def validate_result5is_composite_ex__Nmm_(N, r, /):
    check_int_ge(2, N)

    case, payload = r
    if case is ...:
        (e2, fts, es, Bs, prime_bases, may__j2may_g) = payload
        cannot_conform_primality = may__j2may_g is None
        pass
    elif case is False:
        if not (N==2) is (payload is None): raise ValidateFail
        if (payload is None):
            return
        (e2, fts, es, Bs, g2, gs) = payload
        try:
            validate_primality__Nmm_(e2, fts, es, Bs, g2, gs)
        except ValidateFail as exc:
            if exc.args:
                raise
            raise type(exc)(N, r)
    elif case is True:
        _01, _x = payload
        check_uint_lt(2, _01)
        if not (N&1 == 1): raise ValidateFail(N, r)
        if _01 == 0:
            witness4composite = _x
            check_int_ge_lt(1, N, abs(witness4composite))
            if not (pw := _int_pow(witness4composite, N-1, N)) > 1: raise ValidateFail(N, r, pw)
                #goto:simplify:witness4composite____validate_result5is_composite_ex__Nmm_
                    # sqrt_mod_(N; +1) besides {+1,-1} will be used to find out nontrivial_factor
        elif _01 == 1:
            nontrivial_factor = _x
            check_int_ge_lt(2, N, nontrivial_factor)
            if not N %nontrivial_factor == 0: raise ValidateFail(N, r)
        else:
            raise 000
        return r
    else:
        raise 000
    pass



assert (1, 1) == factor_pint_out_power_of_base_(2, 2)
_all_cases4prime_bases = [N2num_prime_bases__tiny__one_plus_2floor_log2_P, N2num_prime_bases__heuristically, N2num_prime_bases__ERH]
def is_composite_ex__Nmm_(N, /, *, case4prime_bases=N2num_prime_bases__tiny__one_plus_2floor_log2_P, using_nonprime_gs4detect_primality=False, tribool=False, validate=True):
    r'''[[[
    -> ((True, ((1,nontrivial_factor<N>) | (0,witness4composite))) | (False, may (e2, fts, es, Bs, g2, gs)) | ((..., (e2, fts, es, Bs, prime_bases, may__j2may_g)) if tribool else ^DetectPrimalityFail))
    #]]]'''#'''
    original_case4prime_bases = case4prime_bases
    original_tribool = tribool
    original_using_nonprime_gs4detect_primality = using_nonprime_gs4detect_primality

    if original_case4prime_bases is ...:
        all_cases4prime_bases = _all_cases4prime_bases
    else:
        all_cases4prime_bases = [original_case4prime_bases]

    for case4prime_bases in _all_cases4prime_bases:
        is_last = case4prime_bases is all_cases4prime_bases[-1]
        tribool = original_tribool if is_last else True
        using_nonprime_gs4detect_primality = original_using_nonprime_gs4detect_primality if is_last else False
        r = _is_composite_ex__Nmm_(N, case4prime_bases=case4prime_bases, using_nonprime_gs4detect_primality=using_nonprime_gs4detect_primality, tribool=tribool)
        case, payload = r
        if not case is ...:
            break
        (e2, fts, es, Bs, prime_bases, may__j2may_g) = payload
        cannot_conform_primality = may__j2may_g is None
        if cannot_conform_primality:
            if original_tribool:
                break
            raise DetectPrimalityFail__bad_setting__cannot_conform_primality
        if (case4prime_bases is N2num_prime_bases__ERH) and (using_nonprime_gs4detect_primality is True):
            print_err(f'???ERH???: {N}')
        pass

    r
    if validate:
        validate_result5is_composite_ex__Nmm_(N, r)
    return r
def _is_composite_ex__Nmm_(N, /, *, case4prime_bases, using_nonprime_gs4detect_primality, tribool):
    check_int_ge(2, N)
    if N == 2:
        return (False, None)

    assert N >= 3
    if N&1 == 0:
        ft4m = 2
        return (True, (1,ft4m))
    assert N&1 == 1
    # [N >= 1][N&1 == 1]

    num_prime_bases = _calc_num_prime_bases(case4prime_bases, N)
    prime_bases = _list_prime_bases4N(num_prime_bases, N)
    for p in prime_bases:
        if p**2 > N:
            #return (False, None)
            break
        if N%p == 0:
            assert 1 < p < N
            return (True, (1,p))
    else:
        pass


    Nmm = N-1
    eR = Nmm
    eF = 1
    fts = []
    es = []
    p = ...
    assert prime_bases
    assert prime_bases[0] == 2
    for p in prime_bases:
        (e4p, eR) = factor_pint_out_power_of_base_(p, eR)
        B4eR = 3 if p==2 else p+2
        if e4p:
            eF *= p**e4p
            fts.append(p)
            es.append(e4p)
            if eF > eR:
                e5B = eF*B4eR
                # [if below check pass] => [[(e5B+1)**2 > m] -> [is_prime_(m)]]
                if (sq := (e5B+1)**2) > N:
                    break
                elif sq == N:
                    return (True, (1,(e5B+1)))
    B4eR
    eF, eR
    fts, es
    assert eR == 1 or eR >= B4eR, ((eR, B4eR), (N, Nmm, eR, eF, fts, es))
    assert B4eR&1 == 1
    assert fts
    assert fts[0] == 2
    e2 = es[0]
    del fts[0]
    del es[0]
    Bs = [*fts]
    if eR == 1:
        pass
    else:
        fts.append(eR)
        es.append(1)
        Bs.append(B4eR)
    e2, fts, es, Bs
    #if 0b01:print((N, prime_bases, eR, eF, e2, fts, es, Bs))

    #validate_primality__Nmm_(e2, fts, es, Bs, g2, gs)
    #iter_detect_primality__Nmm_(e2, fts, es, Bs, case4prime_bases, N2max1_len_rootss=None, /, *, using_nonprime_gs4detect_primality):
    it = iter_detect_primality__Nmm_(e2, fts, es, Bs, num_prime_bases, using_nonprime_gs4detect_primality=using_nonprime_gs4detect_primality)
    if tribool:
        tmay_cannot_conform_primality = []
        tmay_exc_type = []
        def f(it, /):
            try:
                yield from it
            except DetectPrimalityFail__bad_setting__cannot_conform_primality:
                T = DetectPrimalityFail__bad_setting__cannot_conform_primality
                r = True
            except DetectPrimalityFail__bad_setting__too_few_num_prime_bases:
                T = DetectPrimalityFail__bad_setting__too_few_num_prime_bases
                r = False
            except DetectPrimalityFail__bad_setting:
                raise 000
            else:
                return
            tmay_cannot_conform_primality.append(r)
            tmay_exc_type.append(T)
            return
            #
        it = f(it)
    r = None
    for r in it:
        pass
    assert (r is None) is (tribool and tmay_cannot_conform_primality == [True])
    if r is None:
        assert tribool
        [cannot_conform_primality] = tmay_cannot_conform_primality
        assert cannot_conform_primality
        may__j2may_g = None
        return (..., (e2, fts, es, Bs, prime_bases, may__j2may_g))

    case, payload = r
    if case is ...:
        (delta_js, j2may_g) = payload
        assert tribool
        [cannot_conform_primality] = tmay_cannot_conform_primality
        assert not cannot_conform_primality
        may__j2may_g = j2may_g
        return (..., (e2, fts, es, Bs, prime_bases, may__j2may_g))
        raise DetectPrimalityFail__bad_setting
    elif case is False:
        (delta_js, j2g) = payload
        [g2, *gs] = j2g
        return (False, (e2, fts, es, Bs, g2, gs))
    elif case is True:
        return r
    else:
        raise 000
    pass
#end-def is_composite_ex__Nmm_(N, /, *, case4prime_bases=N2num_prime_bases__tiny__one_plus_2floor_log2_P, using_nonprime_gs4detect_primality=False, tribool=False, validate=True):
def is_composite__Nmm_(N, /, *, case4prime_bases=N2num_prime_bases__tiny__one_plus_2floor_log2_P, using_nonprime_gs4detect_primality=False, tribool=False, quadbool=False, validate=True):
    '-> ((is_composite/bool | ^DetectPrimalityFail) if not tribool else (emay bool) if not quadbool else (bool|type-DetectPrimalityFail__bad_setting__cannot_conform_primality|type-DetectPrimalityFail__bad_setting__too_few_num_prime_bases))'
    if quadbool:
        tribool = quadbool = True

    r = is_composite_ex__Nmm_(N, case4prime_bases=case4prime_bases, using_nonprime_gs4detect_primality=using_nonprime_gs4detect_primality, tribool=tribool, validate=validate)
    case, payload = r
    if quadbool:
        if case is ...:
            (e2, fts, es, Bs, prime_bases, may__j2may_g) = payload
            case = DetectPrimalityFail__bad_setting__cannot_conform_primality if may__j2may_g is None else DetectPrimalityFail__bad_setting__too_few_num_prime_bases
    return case


def test_many4is_composite_ex__Nmm_(max1, /, **kwds4is_composite_ex__Nmm_):
    u2p2e4N = tabulate_may_factorization4uint_lt_(max1)
    for u, p2e4N in enumerate(u2p2e4N):
        if u < 2:
            pass
        else:
            N = u
            factorization4Nmm = prev_p2e4N
            is_prime = len(p2e4N) == 1 and [*p2e4N.values()] == [1] # == N in p2e4N
            is_composite = not is_prime
            test_one4is_composite_ex__Nmm_(N, is_composite, factorization4Nmm, **kwds4is_composite_ex__Nmm_)
        prev_p2e4N = p2e4N

def test_one4is_composite_ex__Nmm_(N, is_composite, factorization4Nmm, /, **kwds4is_composite_ex__Nmm_):
    r = is_composite_ex__Nmm_(N, tribool=True, validate=True, **kwds4is_composite_ex__Nmm_)
    case, payload = r
    if case is ...:
        pass
    else:
        assert case is is_composite_ex__Nmm_

def iter_odd_primes__one_prime_per_bit_length_(begin=2, /, **kwds4is_composite_ex__Nmm_):
    begin = max(2, begin)
    for num_bits in count_(begin):
        for p in iter_odd_primes__Pocklington_Theorem_1914__factor_2s__bit_length_(num_bits, **kwds4is_composite_ex__Nmm_):
            assert p.bit_length() == num_bits, (num_bits, p.bit_length())
            yield (num_bits, p)
            break
        else:
            yield (num_bits, None)

def iter_odd_primes__Pocklington_Theorem_1914__factor_2s__bit_length_(num_bits, /, **kwds4is_composite_ex__Nmm_):
    half = num_bits//2
    prev_end = 0
    for k in range(1, half+1):
        begin = prev_end ^ 1
        end = 1<<k
        prev_end = end
        t = num_bits -k
        for i in range(begin, end, 2):
            Nmm = i << t
            N = Nmm ^ 1
            if False is (case := is_composite__Nmm_(N, quadbool=True, **kwds4is_composite_ex__Nmm_)):
                yield N



class _ToReturn(BaseException):pass
class Error(Exception):pass
class ValidateFail(Error):pass
class ValidateFail__order_mod_(ValidateFail):pass
class ValidateFail__order_mod__proper_factor(ValidateFail__order_mod_):pass
class ValidateFail__order_mod__not_order(ValidateFail__order_mod_):pass

class ValidateFail__nonprime(ValidateFail):pass
class ValidateFail__nonprime__nontrivial_factor(ValidateFail__nonprime):pass
class ValidateFail__bad_setting(ValidateFail):pass

class DetectPrimalityFail(Error):pass
class DetectPrimalityFail__bad_setting(DetectPrimalityFail):pass
class DetectPrimalityFail__bad_setting__cannot_conform_primality(DetectPrimalityFail__bad_setting):pass
class DetectPrimalityFail__bad_setting__too_few_num_prime_bases(DetectPrimalityFail__bad_setting):pass

is_composite_ex__Nmm_(5)




r"""[[[
class ValidateFail__order_mod__not_corresponding_partial_primitive_root(ValidateFail__order_mod_):pass
class PrimalityFail(Error):pass
class PrimalityFail__is_prime_ex__Nmm_____assume_case(PrimalityFail):pass


def _eval_x0_(base, pe_pairs, M, /):
    '-> x0 | ^ValidateFail__order_mod__proper_factor'
    x = base
    for p, e in pe_pairs:
        for _ in range(e-1):
            x = pow(x, p, M)
            #if x in bads:
            if x == 1:
                raise ValidateFail__order_mod__proper_factor
            #if x > halfM: x -= M
    x0 = x
    return x0

def _II__factorization_(factorization, /, *, factorization_is_pe_pairs):
    if factorization_is_pe_pairs:
        pe_pairs = (factorization)
        m = II(p**e for p, e in pe_pairs)
    else:
        p2e = (factorization)
        m = II__p2e_(p2e)
    return m
def _mk_sorted_pe_pairs_(factorization, /, *, factorization_is_pe_pairs):
    if factorization_is_pe_pairs:
        pe_pairs = (factorization)
    else:
        p2e = (factorization)
        pe_pairs = (p2e.items())
    pe_pairs = sorted(pe_pairs)
    return pe_pairs

#def validate_order_mod_(M, factorization4phiM, primitive_root_mod_M, /):
def validate_order_mod_(modulus, factorization4order4base, base, /, *, factorization_is_pe_pairs=False, to_collect_info=False):
    '-> (None if not to_collect_info else xs4good) | ^ValidateFail__order_mod__proper_factor | ^ValidateFail__order_mod__not_order'
    assert not modulus == 0
    M = abs(modulus)
    B = base
    #Mmm = M-1
    #halfM = M//2
    #bads = (1, Mmm)
    pe_pairs = _mk_sorted_pe_pairs_(factorization4order4base, factorization_is_pe_pairs=factorization_is_pe_pairs)
    x0 = _eval_x0_(base, pe_pairs, M)
        # ^ValidateFail__order_mod__proper_factor
    def apply_(pe, x, /):
        p, e = pe
        x = pow(x, p, M)
        if x == 1:
            if not to_collect_info:
                raise ValidateFail__order_mod__proper_factor
        return x


    if to_collect_info:
        bad_idc = []
        good_idc = []
        xs4good = []

    for i, x in enumerate(iter_apply_commutative_operations_except_one_(apply_, pe_pairs, x0)):
        if i == 0:
            p0, e0 = pe_pairs[0]
            if not 1==pow(x, p0, M):
                raise ValidateFail__order_mod__not_order
        if not to_collect_info:
            if x == 1:
                raise ValidateFail__order_mod__proper_factor
        else:
            if x == 1:
                bad_idc.append(i)
            else:
                good_idc.append(i)
                xs4good.append(x)

    if to_collect_info:
        if bad_idc:
            raise ValidateFail__order_mod__proper_factor((bad_idc, good_idc, xs4good))

    if not pe_pairs:
        #if not base == 1:
        if not (base%M == 1):
            raise ValidateFail__order_mod__not_order

    if to_collect_info:
        return xs4good

#end-def validate_order_mod_(modulus, factorization4order4base, base, /):


def validate_primality__Pmm_(factorization4Pmm, primitive_root_mod_P, /, *, factorization_is_pe_pairs=False, using_p2partial_primitive_root=False):
    Pmm = _II__factorization_(factorization4Pmm, factorization_is_pe_pairs=factorization_is_pe_pairs)
    P = Pmm +1
    if not using_p2partial_primitive_root:
        modulus = P
        order4base = Pmm
        factorization4order4base = factorization4Pmm
        base = primitive_root_mod_P
        validate_order_mod_(modulus, factorization4order4base, base, factorization_is_pe_pairs=factorization_is_pe_pairs)
    else:
        p2partial_primitive_root = primitive_root_mod_P
        pe_pairs = _mk_sorted_pe_pairs_(factorization4Pmm, factorization_is_pe_pairs=factorization_is_pe_pairs)
        if not len(p2partial_primitive_root) == len(pe_pairs): raise ValueError

        if not p2partial_primitive_root.keys() == dict(pe_pairs).keys(): raise ValueError
        p2i = {p:i for i, (p,e) in enumerate(pe_pairs)}

        partial_primitive_root2ps = inv__k2v_to_v2ks(p2partial_primitive_root)
        for base, ps in partial_primitive_root2ps.items():
            js = [p2i[p] for p in ps]
            try:
                xs4good = validate_order_mod_(P, pe_pairs, base, factorization_is_pe_pairs=True, to_collect_info=True)
            except ValidateFail__order_mod__proper_factor as exc:
                [(bad_idc, good_idc, xs4good)] = exc.args
                if not {*js} <= {*good_idc}: raise ValidateFail__order_mod__not_corresponding_partial_primitive_root


class Case4is_prime__Nmm_(Enum):
    '#doc4Case4is_prime__Nmm_:goto'
    #assume__exists_prime_primitive_root_mod_P_lt_log2_P = auto()
    #assume__exist_prime_primitive_roots_of_P__and__prime_index_of_the_min_one_le_2floor_log2_P = auto()
del Case4is_prime__Nmm_
class Case4is_prime__Nmm____how_to_find_primitive_root(Enum):
    using_prime_base_as_primitive_root_candidate_only = auto()
    using_arbitrary_int_ge2_as_primitive_root_candidate = auto()
class Case4is_prime__Nmm____how_many_prime_bases_to_be_test(Enum):
    #using_1plus_2floor_log2_P_as_num_bases_to_be_test = auto()
    one_plus_2floor_log2_P = auto()
    one_plus_square_floor_log2_P = auto()
class ResultCase4is_prime__Nmm_(Enum):
    # is_prime =:
    # True:
    two = auto()
    primitive_root = auto()
    p2partial_primitive_root = auto()
    # True & [unfactored_part4Nmm > 1]:
    factored_part4Nmm_ge_sqrtN = auto()
    factored_part4Nmm_ge_cubic_rootN = auto()
    # False:
    factors = auto()
    witness4composite = auto()


default_case4num=Case4is_prime__Nmm____how_many_prime_bases_to_be_test.one_plus_2floor_log2_P
default_case4root=Case4is_prime__Nmm____how_to_find_primitive_root.using_prime_base_as_primitive_root_candidate_only
def is_prime__Nmm_(factorization4Nmm, /, *, tribool=False, **kwds4is_prime_ex__Nmm_):
    r = is_prime_ex__Nmm_(factorization4Nmm, raise__vs__emay=tribool, **kwds4is_prime_ex__Nmm_)
    if r is ...:
        return ...
    (is_prime, result_case, payload4result_case) = r
    return is_prime

def is_prime_ex__Nmm_(factorization4Nmm, /, *, factorization_is_pe_pairs=False, partial_primitive_roots__vs__primitive_root=False, case4num=default_case4num, case4root=default_case4root, raise__vs__emay=False, odd_coprime_nonprime_factor2prime_factor_lowbound4Nmm=None):
    '-> (is_prime/bool, result_case/ResultCase4is_prime__Nmm_, payload4result_case) | (... if raise__vs__emay else ^PrimalityFail__is_prime_ex__Nmm_____assume_case)'
    # view others/数学/整数分解/factorint.txt
    #       F1,R1,B1 ==>> odd_coprime_nonprime_factor2prime_factor_lowbound4Nmm
    #
    check_type_is(bool, partial_primitive_roots__vs__primitive_root)
    check_type_is(bool, raise__vs__emay)

    to_collect_partials = partial_primitive_roots__vs__primitive_root is False

    pe_pairs = _mk_sorted_pe_pairs_(factorization4Nmm, factorization_is_pe_pairs=factorization_is_pe_pairs)
    if not all(e >= 1 for p, e in pe_pairs): raise ValueError
    if not all(p >= 2 for p, e in pe_pairs): raise ValueError

    js4unfactored = set()
    if odd_coprime_nonprime_factor2prime_factor_lowbound4Nmm:
        if 2 in odd_coprime_nonprime_factor2prime_factor_lowbound4Nmm: raise ValueError
        p2i = {p:i for i, (p,e) in enumerate(pe_pairs)}
        for unfactored, min_p4unfactored in odd_coprime_nonprime_factor2prime_factor_lowbound4Nmm.items():
            if not unfactored in p2i: raise ValueError
            if not (unfactored&1 == 1): raise ValueError
            js4unfactored.add(p2i[unfactored])
        R1_2_B1 = odd_coprime_nonprime_factor2prime_factor_lowbound4Nmm
    else:
        js4unfactored
        pass
    true_pe_pairs = []
    false_pe_pairs = []
    for i, pe in enumerate(pe_pairs):
        if i in js4unfactored:
            false_pe_pairs.append(pe)
        else:
            true_pe_pairs.append(pe)

    #Nmm = _II__factorization_(factorization4Nmm, factorization_is_pe_pairs=factorization_is_pe_pairs)
    if 1:
        factored_part4Nmm = _II__factorization_(true_pe_pairs, factorization_is_pe_pairs=True)
            # F1
        unfactored_part4Nmm = _II__factorization_(false_pe_pairs, factorization_is_pe_pairs=True)
            # R1
        assert unfactored_part4Nmm&1 == 1
    Nmm = factored_part4Nmm * unfactored_part4Nmm
    assert Nmm >= 1
    N = Nmm +1
    assert N >= 2
    #if not factorization4Nmm.get(2,1-len(factorization4Nmm)) >= 1: raise ValueError
    if N == 2:
        return (True, ResultCase4is_prime__Nmm_.two, None)
    if not (N&1 == 1):
        return (False, ResultCase4is_prime__Nmm_.factors, [2])
    if not factorization4Nmm.get(2,-1) >= 1: raise 000


    if case4num is Case4is_prime__Nmm____how_many_prime_bases_to_be_test.one_plus_2floor_log2_P:
        max1_prime_index4base = 1+ 2*floor_log2(N)
    elif case4num is Case4is_prime__Nmm____how_many_prime_bases_to_be_test.one_plus_square_floor_log2_P:
        max1_prime_index4base = 1+ floor_log2(N)**2
    else:
        raise 000
    if case4root is Case4is_prime__Nmm____how_to_find_primitive_root.using_prime_base_as_primitive_root_candidate_only:
        def iter_candidate_primitive_root_between_(a, b, /):
            return;yield
    elif case4root is Case4is_prime__Nmm____how_to_find_primitive_root.using_arbitrary_int_ge2_as_primitive_root_candidate:
        def iter_candidate_primitive_root_between_(a, b, /):
            return iter(range(max(2,a), b))
    else:
        raise 000

    M = modulus = N

    PRIMES = prime_gen.get_or_mk_lazy_prime_seq_()
    primes = PRIMES[:max1_prime_index4base]
    halfN = N//2
    for i, base in enumerate(primes):
        if base > halfN:
            max1_prime_index4base = max(1,i)
            #max1_prime_index4base = i+1
                # 『+1』<<== [N=3][base == 2 > 3//2]
            primes = primes[:max1_prime_index4base]
            break
    for i, base in enumerate(primes):
        if base**2 > N:
            # [is_prime_(N)]
            break
        if N%base == 0:
            if N == base:
                raise 000
            assert 1 < base < N
            factors = [base]
            return (False, ResultCase4is_prime__Nmm_.factors, factors)




    assert unfactored_part4Nmm&1 == 1
    assert factored_part4Nmm&1 == 0
    if unfactored_part4Nmm == 1:
        #ok
        # [factorization4Nmm is complete]
        pass
    elif factored_part4Nmm > unfactored_part4Nmm:
        #ok
        # [1+F1 > sqrt_(N)]
        result_case = ResultCase4is_prime__Nmm_.factored_part4Nmm_ge_sqrtN
        pass
    elif factored_part4Nmm**2 > unfactored_part4Nmm:
        #ok
        # [1+F1 > cubic_root_(N)]
        result_case = ResultCase4is_prime__Nmm_.factored_part4Nmm_ge_cubic_rootN
        pass
    else:
        raise PrimalityFail__is_prime_ex__Nmm_____unfactored_part4Nmm_too_big







    odd_pe_pairs = pe_pairs[1:]
    #odd_p1_pairs = [(odd_p, 1) for odd_p, e in odd_pe_pairs]
    p1_pairs = [(p, 1) for p, e in pe_pairs]
    p2, e2 = pe_pairs[0]
    assert p2 == 2
    assert e2 >= 1
    if to_collect_partials:
        p2rt = {}

    def _test_order_mod_(pe_pairs4B, B, base, /):
        '-> ... | result'
        #assert (B is base) is (pe_pairs4B is pe_pairs)
        assert (B == base) is (pe_pairs4B == pe_pairs)
        try:
            may_xs4good = validate_order_mod_(M, pe_pairs4B, B, factorization_is_pe_pairs=True, to_collect_info=to_collect_partials ....)
        except ValidateFail__order_mod__proper_factor as exc:
            if to_collect_partials ....:
                [(bad_idc, good_idc, xs4good)] = exc.args
                assert bad_idc
                assert 0 < len(bad_idc) < len(pe_pairs4B)
                # [len(bad_idc) < len(pe_pairs4B)] <<== [not$ [x0==1]]
                # [0 < len(bad_idc)] <<== [raise ValidateFail__order_mod__proper_factor]
                assert len(bad_idc) +len(good_idc) == len(pe_pairs4B)
                if js4unfactored:
                    ds = []
                for good_i, x4i in zip(good_idc, xs4good):
                    if good_i in js4unfactored:
                        d = gcd(x4i-1, M)
                        if not d == 1:
                            assert 1 < d < M
                            ds.append(d)
                    p, e = pe_pairs4B[good_i]
                    p2rt.setdefault(p, base)
                        # base not B
                if js4unfactored:
                    if ds:
                        return (False, ResultCase4is_prime__Nmm_.factors, ds)
                if len(p2rt) == len(pe_pairs):
                    # pe_pairs not pe_pairs4B
                    if js4unfactored:
                        return (True, result_case, (ResultCase4is_prime__Nmm_.p2partial_primitive_root, p2rt))
                    return (True, ResultCase4is_prime__Nmm_.p2partial_primitive_root, p2rt)
            return ...
        except ValidateFail__order_mod__not_order:
            raise 000 # since pass primality_test_of_Miller_Rabin
            return (False, ResultCase4is_prime__Nmm_.witness4composite, base)
        if to_collect_partials ....:
            xs4good = may_xs4good
            if js4unfactored:
        return (True, ResultCase4is_prime__Nmm_.primitive_root, base)

    k = min(e2, 1+floor_log2(len(primes)))
    xss = [set() for _ in range(k)]
        # for primitive (2**k)-th-root of 1 mod N
    #xss[0] = {1,Nmm}
    xss[0] = {1,-1}
    def _add_xs_(xs, /):
        for i, x in enumerate(reversed(xs), 1):
            if i == len(xss):
                break
            s = xss[i]
            if s:
                if not x in s:
                    break
            else:
                for s_ in xss[:i]:
                    assert s_
                    for y in s_:
                        xy = x*y%M
                        s.add(xy)
                assert len(s) == (1<<i), (len(s), i, 1<<i, x, xs, xss, M)
        else:
            i = len(xss)
        if i == len(xss):
            return ...

        i, x, s
        x2 = pow(x, 2, M)
        for y in s:
            y2 = pow(y, 2, M)
            if y2 == x2:
                break
        else:
            raise 000
        x,y,x2
        # [x**2 =[%N]= y**2]
        # [(x**2-y**2)%N == 0]
        ds = [x+y, x-y]
        ds = [gcd(d, M) for d in ds]
        ds = [d for d in ds if 1 < d < M]
        if not ds:
            raise 000
        return (False, ResultCase4is_prime__Nmm_.factors, ds)




    for base in primes:
        ######################
        # is N composite?
        #   using primality_test_of_Miller_Rabin
        ######################
        try:
            x0__but2 = _eval_x0_(base, odd_pe_pairs, M)
                # ^ValidateFail__order_mod__proper_factor
        except ValidateFail__order_mod__proper_factor:
            x0__but2 = 1
        x = x0__but2
        if not x == 1:
            for odd_p, _ in odd_pe_pairs:
                x = pow(x, odd_p, M)
                if x == Nmm:
                    break
        # [is_prime_(N)] -> [2**e2 %order_mod_(N;x) == 0]

        xs = [] # for primitive (2**k)-th-root of 1 mod N
        if x == 1:
            #ok
            pass
        elif x == Nmm:
            #ok
            pass
        else:
            for _ in range(e2-1):
                xs.append(x)
                x = pow(x, 2, M)
                if x == Nmm:
                    #ok
                    break
            else:
                return (False, ResultCase4is_prime__Nmm_.witness4composite, base)
        xs
        x
        r = _add_xs_(xs)
        if not r is ...:
            return r
        if x == 1:
            if not to_collect_partials:
                continue

        ######################
        # is "base" a primitive_root_mod_N
        ######################
        x0 = pow(x0__but2, 1<<(e2-1), M)
        if not x0 == 1:
            p1_pairs
            r = _test_order_mod_(p1_pairs, x0, base)
            if r is ...:
                continue
            return r


    ######################
    ######################
    ######################
    prev = 2
    for base in primes:
        ######################
        # try:non-prime primitive_root_candidate
        ######################
        for b in iter_candidate_primitive_root_between_(prev+1, base):
            r = _test_order_mod_(pe_pairs, b, b)
            if r is ...:
                continue
            return r
        prev = base

    if raise__vs__emay is True:
        return ...
    raise PrimalityFail__is_prime_ex__Nmm_____assume_case((case4num, case4root, partial_primitive_roots__vs__primitive_root), tuple(pe_pairs))

#end-def is_prime_ex__Nmm_(factorization4Nmm, /, *, factorization_is_pe_pairs=False, partial_primitive_roots__vs__primitive_root=False, case4num=default_case4num, case4root=default_case4root, raise__vs__emay=False):

def test_many4is_prime_ex__Nmm_(max1, /, **kwds4is_prime_ex__Nmm_):
    u2m = tabulate_may_factorization4uint_lt_(max1)
    for u, m in enumerate(u2m):
        if u < 2:
            pass
        else:
            N = u
            factorization4Nmm = prev_m
            is_prime = N in m
            test_one4is_prime_ex__Nmm_(is_prime, factorization4Nmm, factorization_is_pe_pairs=False, **kwds4is_prime_ex__Nmm_)
        prev_m = m
def test_one4is_prime_ex__Nmm_(result, factorization4Nmm, /, *, factorization_is_pe_pairs=False, **kwds4is_prime_ex__Nmm_):
    N = 1+ II__p2e_(factorization4Nmm)
    r = is_prime_ex__Nmm_(factorization4Nmm, factorization_is_pe_pairs=factorization_is_pe_pairs, **kwds4is_prime_ex__Nmm_)
    if r is ...:
        assert kwds4is_prime_ex__Nmm_['raise__vs__emay'] is True
        pass
    else:
        (is_prime, result_case, payload4result_case) = r
        RC = ResultCase4is_prime__Nmm_
        if result_case is RC.two:
            assert is_prime is True
            assert payload4result_case is None
        elif result_case is RC.primitive_root:
            assert is_prime is True
            primitive_root = payload4result_case
            validate_primality__Pmm_(factorization4Nmm, primitive_root, factorization_is_pe_pairs=factorization_is_pe_pairs, using_p2partial_primitive_root=False)
        elif result_case is RC.p2partial_primitive_root:
            assert is_prime is True
            p2partial_primitive_root = payload4result_case
            validate_primality__Pmm_(factorization4Nmm, p2partial_primitive_root, factorization_is_pe_pairs=factorization_is_pe_pairs, using_p2partial_primitive_root=True)
        elif result_case is RC.factors:
            assert is_prime is False
            factors = payload4result_case
            assert factors
            for ft in factors:
                assert 1 < ft < N
                assert N%ft == 0
        elif result_case is RC.witness4composite:
            assert is_prime is False
            witness4composite = payload4result_case
            assert 2 <= witness4composite < N
            assert N&1 == 1
            assert not is_strong_pseudoprime_(witness4composite, N)
        else:
            raise 000
        pass
    if r is ...:
        assert result is None or result is ...
    else:
        assert result is None or result is is_prime
    return
#]]]"""



r"""[[[
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
class IPrimalityProver4SpecialFormPrime(ABC):
    r'''[[[
    prime in special form:
        e.g. [[(n-1) == F*R][F has been completely factorized]]
    args:
        e.g. provide some witnesses (assume enough to determine primality/compositeness)
        e.g. the factorization of F
    state:
        e.g. 

    #]]]'''#'''
    __slots__ = ()
    #raise NotImplementedError
    #___no_slots_ok___ = True
    def is_prime_(sf, /, *args):
        ...
    def iter_states4is_prime_(sf, /, *args):
        ...
    @abstractmethod
    def __repr__(sf, /):
        #return repr_helper(sf, *args, **kwargs)
        #return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
        ...
#]]]"""

def __():
    from seed.tiny import ifNonef, ifNone, echo
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.helper.repr_input import repr_helper

if __name__ == "__main__":
    pass
__all__


from seed.math.primality_proving import *

