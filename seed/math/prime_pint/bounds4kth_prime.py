#__all__:goto
r'''[[[
e ../../python3_src/seed/math/prime_pint/bounds4kth_prime.py
view ../../python3_src/seed/math/prime_pint/bounds4kth_prime__7prepare.py

seed.math.prime_pint.bounds4kth_prime
py -m nn_ns.app.debug_cmd   seed.math.prime_pint.bounds4kth_prime -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.prime_pint.bounds4kth_prime:__doc__ -ht # -ff -df
#######

[[
estimate_upper_bound4Kth_prime_
estimate_lower_bound4Kth_prime_
<<==:
#view ../../python3_src/seed/math/prime_pint/generate_primes.py
view ../../python3_src/seed/math/prime_pint/generate_primes-deprecated.py
    list_primes__len_ge_
        required:estimate_upper_bound4Kth_prime_

view ../../python3_src/seed/math/prime_sieve/PrimeList.py
    PrimeList.__call__(sf, emay_idx_or_begin, /, end=None, *, max1=None):
        required:estimate_lower_bound4Kth_prime_
]]
[[
PRIMES[k] vs PRIMES_S1[n]
[PRIMES[0] == PRIMES_S1[1] == 2]

[num_primes_le(10**8) == 5761455]

[[n>=1] -> [0.91*n*ln(n) < PRIMES_S1[n] < 1.7*n*ln(n)]]
[[n>=2] -> [-9 < PRIMES_S1[n]/n -(ln(n) +lnln(n)-1) < +9]]
我:数值公式:[[2227 <= n <= 5761455] -> [PRIMES_S1[n] <= n*(ln(n) +lnln(n) -1 +0.08673)]] #末位系数峰值@[n==2227]
我:数值公式:[[2 <= n <= 5761455] -> [PRIMES_S1[n] >= n*(ln(n) +lnln(n) -1 +0.01655)]] #末位系数谷值@[n==2688]
    #俩界限公式形式差异的原因在于:
        !! 最后一个逆向谷值位于[n:=2688]@[n:<-[2..=5761455]]
        !! 最后一个逆向峰值位于[n:=2]@[n:<-[2..=5761455]] 而非 2227
<<==:
view ../../python3_src/seed/math/prime_pint/bounds4kth_prime__7prepare.py
]]












'#'; __doc__ = r'#'

>>> from seed.math.constants.lnN import interval5lnN__via_floor_numerator4denominator_
>>> from seed.math.constants.lnN import interval5lnN__via_limit_denominator_

>>> (A_lt_ln2, A_gt_ln2) = interval5lnN__via_floor_numerator4denominator_(2**64, 2)
>>> (A_lt_ln2, A_gt_ln2)
(Fraction(12786308645202655659, 18446744073709551616), Fraction(3196577161300663915, 4611686018427387904))

>>> (B_lt_ln2, B_gt_ln2) = interval5lnN__via_limit_denominator_(2**64, 2)
>>> (B_lt_ln2, B_gt_ln2)
(Fraction(3052446177238342414, 4403748962482230453), Fraction(1385328996563313413, 1998607273341576092))

>>> (A_lt_ln2 < B_lt_ln2 < B_gt_ln2 < A_gt_ln2) # B better
True








__all__

>>> #from seed.math.prime_sieve.sieve_lt import list_all_strict_sorted_primes__lt_
>>> from seed.math.prime_sieve.sieve_ge_le import sieve_interval4primes__ge_lt
>>> from seed.math.prime_pint.num_primes_le import num_primes_le__via_the_Meissel_formula_1871_
>>> def test_(min_p, max1_p, /, *, to_show=False):
...     #ps = list_all_strict_sorted_primes__lt_(max1_p)
...     ps = sieve_interval4primes__ge_lt(min_p, max1_p)
...     k0 = num_primes_le__via_the_Meissel_formula_1871_(-1+min_p)
...     for k, pk in enumerate(ps, k0):
...         (lw4pk, up4pk) = estimate_both_bounds4Kth_prime_(k)
...         assert lw4pk <= pk <= up4pk, (k, pk, n:=1+k, lw4pk, up4pk)
...         if to_show:print(k, n:=1+k, (lw4pk, pk, up4pk), (d0:=pk-lw4pk, d1:=up4pk-pk), d1-d0, sep=':')
>>> test_(0, 10_00_00) #doctest: +SKIP


>>> test_(0, 100)
>>> test_(0, 100, to_show=True)
0:1:(2, 2, 2):(0, 0):0
1:2:(2, 3, 3):(1, 0):-1
2:3:(2, 5, 5):(3, 0):-3
3:4:(6, 7, 7):(1, 0):-1
4:5:(7, 11, 11):(4, 0):-4
5:6:(8, 13, 13):(5, 0):-5
6:7:(9, 17, 22):(8, 5):-3
7:8:(16, 19, 31):(3, 12):9
8:9:(18, 23, 35):(5, 12):7
9:10:(19, 29, 39):(10, 10):0
10:11:(21, 31, 43):(10, 12):2
11:12:(23, 37, 47):(14, 10):-4
12:13:(25, 41, 51):(16, 10):-6
13:14:(27, 43, 55):(16, 12):-4
14:15:(29, 47, 59):(18, 12):-6
15:16:(41, 53, 85):(12, 32):20
16:17:(43, 59, 91):(16, 32):16
17:18:(46, 61, 96):(15, 35):20
18:19:(48, 67, 101):(19, 34):15
19:20:(51, 71, 107):(20, 36):16
20:21:(53, 73, 112):(20, 39):19
21:22:(56, 79, 117):(23, 38):15
22:23:(59, 83, 123):(24, 40):16
23:24:(61, 89, 128):(28, 39):11
24:25:(64, 97, 125):(33, 28):-5
>>> test_(100_00, 100_00+300, to_show=True) #doctest: +ELLIPSIS
1229:1230:(9022, 10007, 11754):(985, 1747):762
1230:1231:(9029, 10009, 11764):(980, 1755):775
...
1260:1261:(9249, 10273, 12051):(1024, 1778):754
1261:1262:(9256, 10289, 12060):(1033, 1771):738

vs:
    #before:++(_data4lower_bound__snd_part,_data4upper_bound__snd_part)
1229:1230:(9001, 10007, 11754):(1006, 1747):741
1230:1231:(9009, 10009, 11764):(1000, 1755):755
...
1260:1261:(9228, 10273, 12051):(1045, 1778):733
1261:1262:(9236, 10289, 12060):(1053, 1771):718

>>> test_(100_00_00, 100_00_00+12_00, to_show=True) #doctest: +ELLIPSIS
78498:78499:(957854, 1000003, 1067959):(42149, 67956):25807
78499:78500:(957866, 1000033, 1067973):(42167, 67940):25773
...
78589:78590:(958964, 1001191, 1069197):(42227, 68006):25779
78590:78591:(958977, 1001197, 1069211):(42220, 68014):25794

vs:
    #before:++(_data4lower_bound__snd_part,_data4upper_bound__snd_part)
78498:78499:(955317, 1000003, 1070947):(44686, 70944):26258
78499:78500:(955330, 1000033, 1070961):(44703, 70928):26225
...
78589:78590:(956425, 1001191, 1072189):(44766, 70998):26232
78590:78591:(956437, 1001197, 1072202):(44760, 71005):26245
























py_adhoc_call   seed.math.prime_pint.bounds4kth_prime   @f
]]]'''#'''
__all__ = r'''
estimate_both_bounds4Kth_prime_
    estimate_lower_bound4Kth_prime_
    estimate_upper_bound4Kth_prime_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from bisect import bisect_right
    from fractions import Fraction
    from math import floor, ceil
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.math.constants.lnN import lt_ln_, gt_ln_


#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def estimate_both_bounds4Kth_prime_(k, /):
    'k/uint -> both_bounds/(lower_bound{PRIMES[k]}/uint, upper_bound{PRIMES[k]}/uint) # [lower_bound{PRIMES[k]} <= PRIMES[k] <= upper_bound{PRIMES[k]}] # [PRIMES[0] == 2]'
    lower_bound = estimate_lower_bound4Kth_prime_(k)
    upper_bound = estimate_upper_bound4Kth_prime_(k)
    assert lower_bound <= upper_bound
    both_bounds = (lower_bound, upper_bound)
    return both_bounds
def estimate_lower_bound4Kth_prime_(k, /):
    'k/uint -> lower_bound{PRIMES[k]}/uint # [lower_bound{PRIMES[k]} <= PRIMES[k]] # [PRIMES[0] == 2]'
    check_int_ge(0, k)
    # [k>=0]
    n = 1+k
    777;del k
    # [n>=1]
    if n == 1:
        return 2
    # [n>=2]


    lt_lnN = lt_ln_(n)
    lt_lnlnN = lt_ln_(lt_lnN)
    lt_center = n*(lt_lnN +lt_lnlnN -1)

    rs = []

    # !! [[n>=1] -> [0.91*n*ln(n) < PRIMES_S1[n] < 1.7*n*ln(n)]]
    r0 = n*lt_lnN*Fraction(0.91)
    check_type_is(Fraction, r0)
    rs.append(r0)

    # !! [[n>=2] -> [-9 < PRIMES_S1[n]/n -(ln(n) +lnln(n)-1) < +9]]
    r1 = lt_center -n*9
    check_type_is(Fraction, r1)
    rs.append(r1)

    if n <= 4118054813:
        # [2<=n<=4118054813]
        # !! [[2<=n<=4118054813] -> [n*ln(n) + n*(lnln(n)-1) <= PRIMES_S1[n]]]
        r2 = lt_center
    else:
        # !! [[n>=2] -> [n*ln(n) + n*(lnln(n)-1.0072629) <= PRIMES_S1[n]]]
        r2 = lt_center -n*Fraction(0.0072630)
    r2
    check_type_is(Fraction, r2)
    rs.append(r2)

    if n <= 5761455:
        # [2<=n<=5761455] #required by _data4lower_bound
        _data4lower_bound = _gmk_data4lower_bound()
        _j = -1+bisect_right(_data4lower_bound, n, key=lambda t:t[0])
        assert _j >= -1
        777;j = max(0, _j)
        assert j >= 0
        (_n, _Pn, _lt_xn, _) = _data4lower_bound[j]
        assert _n <= n or _j == -1
        # [[_n <= n <= 5761455]or[2<=n<2688==_n]]
            #与upper_bound的[7<=_n<=n<=5761455]不同:2688处最小

        #  我:数值公式:[[2 <= n <= 5761455] -> [PRIMES_S1[n] >= n*(ln(n) +lnln(n) -1 +0.01655)]] #末位系数谷值@[n==2688]
        # !! [[[_n <= n <= 5761455]or[2<=n<2688==_n]] -> [PRIMES_S1[n] >= n*(ln(n) +lnln(n) -1 +_lt_xn)]]
        r = lt_center +n*_lt_xn
        check_type_is(Fraction, r)
        rs.append(r)
    else:
        pass
    rs


    r = max(rs)
    check_type_is(Fraction, r)
    return ceil(r) # lower_bound:final:ceil!!!

def estimate_upper_bound4Kth_prime_(k, /):
    'k/uint -> upper_bound{PRIMES[k]}/uint # [upper_bound{PRIMES[k]} >= PRIMES[k]] # [PRIMES[0] == 2]'
    check_int_ge(0, k)
    # [k>=0]
    n = 1+k
    777;del k
    # [n>=1]
    if n < 7:
        # [1<=n<=6]
        if n == 1:
            # 2
            return 2
        # [2<=n<=6]
        if n <= 4:
            # [2<=n<=4]
            # 3,5,7
            return (n<<1)-1
        # [5<=n<=6]
        # 11,13
        return (n<<1)+1
    # [n>=7] #required by _data4upper_bound


    gt_lnN = gt_ln_(n)
    gt_lnlnN = gt_ln_(gt_lnN)
    gt_center = n*(gt_lnN +gt_lnlnN -1)

    # !! [[n>=1] -> [0.91*n*ln(n) < PRIMES_S1[n] < 1.7*n*ln(n)]]
    r0 = n*gt_lnN*Fraction(1.7)
    check_type_is(Fraction, r0)

    # !! [[n>=2] -> [-9 < PRIMES_S1[n]/n -(ln(n) +lnln(n)-1) < +9]]
    r1 = gt_center +n*9
    check_type_is(Fraction, r1)

    rs = [r0, r1]
    if n <= 5761455:
        # [7<=n<=5761455] #required by _data4upper_bound
        _data4upper_bound = _gmk_data4upper_bound()
        j = -1+bisect_right(_data4upper_bound, n, key=lambda t:t[0])
        assert j >= 0
        (_n, _Pn, _gt_xn, _) = _data4upper_bound[j]
        assert _n <= n
        # [_n <= n <= 5761455]

        #我:数值公式:[[2227 <= n <= 5761455] -> [PRIMES_S1[n] <= n*(ln(n) +lnln(n) -1 +0.08673)]] #末位系数峰值@[n==2227]
        # !! [[_n <= n <= 5761455] -> [PRIMES_S1[n] <= n*(ln(n) +lnln(n) -1 +_gt_xn)]]
        r = gt_center +n*_gt_xn
        check_type_is(Fraction, r)
        rs.append(r)
    else:
        pass
    rs
    r = min(rs)
    check_type_is(Fraction, r)
    return floor(r) # upper_bound:final:floor!!!

if 0:
    _data4upper_bound = ...
    _data4lower_bound = ...
def _gmk_data4upper_bound():
    try:
        return _data4upper_bound
    except NameError:
        pass
    _mk_data4upper_bound()
    return _gmk_data4upper_bound()
def _gmk_data4lower_bound():
    try:
        return _data4lower_bound
    except NameError:
        pass
    _mk_data4lower_bound()
    return _gmk_data4lower_bound()


def _mk_data4upper_bound():
    global _data4upper_bound
    # [7<=n<=5761455]
    _data4upper_bound = (*''
    #_data4upper_bound__fst_part
    #   from:命令行牜生成数据牜部分一
    ,(7, 17, Fraction(5674137815635505509, 6945671737940182595), 0.8169314689378389)
    ,(25, 97, Fraction(6026128338173015331, 12245938457487303491), 0.49209199924474334)
    ,(102, 557, Fraction(5590118234585976967, 18367942844044346429), 0.3043410077029136)
    ,(464, 3301, Fraction(1302707933219373577, 8165725309374318866), 0.15953364629151243)
    ,(1410, 11777, Fraction(325796002487799548, 2716091159943447081), 0.11995031952262718)
    ,(2227, 19681, Fraction(576798800953562899, 6650757009630375594), 0.08672678916375254)

    #_data4upper_bound__snd_part
    #   from:命令行牜生成数据牜部分二+_convert_format4halfway_data_()
    ,(4272, 40813, Fraction(934848883253278558, 13292601215173710431), 0.07032851344296209)
    ,(26966, 312209, Fraction(934929341129738590, 17664366159220989073), 0.05292742081445676)
    ,(39056, 467879, Fraction(296452379269973271, 6091830699837973268), 0.04866392286277065)
    ,(133219, 1773643, Fraction(287289411947109405, 6257522843007130076), 0.045911044858295544)
    )
    return _data4upper_bound


def _mk_data4lower_bound():
    global _data4lower_bound
    # lower_bound:[2<=n<=5761455]
    #   but:upper_bound:[7<=n<=5761455]
    #       !! 最后一个逆向谷值位于[n:=2688]@[n:<-[2..=5761455]]
    #       !! 最后一个逆向峰值位于[n:=2]@[n:<-[2..=5761455]]
    _data4lower_bound =(*''
    #_data4lower_bound__snd_part#no:fst_part
    #   from:命令行牜生成数据牜部分二+_convert_format4halfway_data_()
    ,(2688, 24137, Fraction(61940009616985749, 3740408431204872707), 0.01655969147653574)
    ,(2699, 24251, Fraction(25845891958679246, 1468538031455118409), 0.01759974301317177)
    ,(6045, 59797, Fraction(99026027251956104, 4746195079699114771), 0.02086429773515206)
    ,(6076, 60169, Fraction(24469830758211391, 944157057445231584), 0.02591711894250267)
    ,(30749, 359783, Fraction(552785476962881336, 17478850508844274795), 0.03162596285626292)
    ,(50461, 617819, Fraction(27806617729747633, 860479055057933734), 0.032315275504149824)
    ,(115647, 1520821, Fraction(36818552949582949, 1016289110306572638), 0.03622842415233231)
    ,(2085570, 33933047, Fraction(658443856207116879, 15598157929882652099), 0.04221292406237808)
    )
    return _data4lower_bound


__all__
from seed.math.prime_pint.bounds4kth_prime import estimate_both_bounds4Kth_prime_, estimate_lower_bound4Kth_prime_, estimate_upper_bound4Kth_prime_
from seed.math.prime_pint.bounds4kth_prime import *
