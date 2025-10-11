#__all__:goto
#_doc4factor_pint_as_pefect_power__CRT_ver_:goto
#bug-fixed:@20250104..20250105
r'''[[[
e ../../python3_src/seed/math/factor_pint_as_pefect_power_.py
view others/数学/整数分解/整数幂方分解.txt
view script/辅助冫幂方判定.py
view ../../python3_src/seed/math/_data4factor_pint_as_pefect_power_.py





py -m seed.math.factor_pint_as_pefect_power_    >  /sdcard/0my_files/tmp/0tmp      2>&1
    to show _cache
py -m nn_ns.app.debug_cmd   seed.math.factor_pint_as_pefect_power_ -x
py -m nn_ns.app.doctest_cmd seed.math.factor_pint_as_pefect_power_:__doc__ -ht # -ff -v
py -m nn_ns.app.doctest_cmd seed.math.factor_pint_as_pefect_power_:_4doctest -ht # -ff -v

[[
floor_kth_root_-ver2@20250105:
[TIME(factor_pint_as_pefect_power_(n)) ~<= O(lbN**3*lblblbN) if not _to_eliminate_the_dominant_branch else O(lbN**3)]
<<==:
#DONE:eliminate the_dominant_branch&the_secondary_branch via _factor_pint_as_pefect_power__try_small_prime_factors
===
let [max4exp < lbN/lblbN] to eliminate the_dominant_branch&the_secondary_branch
let [max4exp < lbN/lblbN**(3/2)] to eliminate the_dominant_branch&the_secondary_branch
!! [max4exp := ceil_div(ceil_log2(n), exp4zpow) -1]
[max4exp ~= lbN/exp4zpow]
[max4exp <= lbN/lblbN]
    <==> [lbN/exp4zpow ~<= lbN/lblbN]
    <==> [exp4zpow ~>= lblbN]
    #config4primes4le_256
    # [exp4zpow == 8] => [n <= 2**2**8 == 2**256]
[max4exp <= lbN/lblbN**(3/2)]
    <==> [lbN/exp4zpow ~<= lbN/lblbN**(3/2)]
    <==> [exp4zpow ~>= lblbN**(3/2)]
    #config4primes4le_256
    # [exp4zpow == 8] => [n <= 2**2**8**(2/3) == 2**16]

[TIME(_factor_pint_as_pefect_power__try_small_prime_factors{config4primes4le_{2**exp4zpow}})
~= TIME(div(n,2**exp4zpow))*len(primes_le(2**exp4zpow))
~= O((lbN*exp4zpow) * (2**exp4zpow/exp4zpow))
~= O(lbN * 2**exp4zpow)
* [exp4zpow ~>= lblbN]:
    ~>= O(lbN * 2**lblbN)
        ~= O(lbN**2)
* [exp4zpow ~>= lblbN**(3/2)]:
    ~>= O(lbN * 2**lblbN**(3/2))
        ~= O(lbN * (2**lblbN)**lblbN**(1/2))
        ~= O(lbN * lbN**lblbN**(1/2))
        ~= O(lbN**lblbN**(1/2))
            too big!!
            should not eliminate the_secondary_branch
]
++kw:_to_eliminate_the_dominant_branch
[eliminate the_dominant_branch]:
    [max4exp <= lbN/lblbN]
    !! [max4exp ~= lbN/exp4zpow]
    [exp4zpow ~>= lblbN]
    [exp4zpow := lblbN]:
        # [{exp4zpow:minN} == {e:2**2**e} == {1:4, 2:16, 3:256, 4:65536, 5:4294967296, 6:18446744073709551616, 7:340282366920938463463374607431768211456, 8:115792089237316195423570985008687907853269984665640564039457584007913129639936, ..., 14:ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit, ...}]
        [TIME(_factor_pint_as_pefect_power__try_small_prime_factors{config4primes4le_{2**exp4zpow}}) ~>= O(lbN**2)]
        [TIME(factor_pint_as_pefect_power_(n)) ~<= O(lbN**3)]
===
]]
[[
floor_kth_root_-ver2@20250105:
[TIME(factor_pint_as_pefect_power_(n)) ~<= O(lbN**3*lblblbN)]
<<==:
TIME(factor_pint_as_pefect_power_(n))
    <= O(sum[TIME(floor_kth_root_(k;n)) | [k :<- primes_le(lbN)]])
    <= O(sum[TIME(floor_kth_root_(k;n)) | [k :<- [1,3,5..=lbN]]])
    <= O(sum[TIME(floor_kth_root_(k;n)) | [k :<- [1 ... lbN/lblbN**(3/2) ... lbN/lblbN ... lbN]]])
    <= O(sum[TIME(floor_kth_root_(k;n)) | [k :<- [1 ... lbN/lblbN**(3/2)]]])
      +O(sum[TIME(floor_kth_root_(k;n)) | [k :<- [lbN/lblbN**(3/2) ... lbN/lblbN]]])
      +O(sum[TIME(floor_kth_root_(k;n)) | [k :<- [lbN/lblbN ... lbN]]])
    <= O(sum[ lbN**2 | [k :<- [1 ... lbN/lblbN**(3/2)]]])
      +O(sum[ k**2 *lbK**3 | [k :<- [lbN/lblbN**(3/2) ... lbN/lblbN]]])
      +O(sum[ lbN**3 /k | [k :<- [lbN/lblbN ... lbN]]])
    <= O(lbN**3/lblbN**(3/2))
      +O(lbN**3) # the_secondary_branch
      +O(lbN**3*lblblbN) # the_dominant_branch
    <= O(lbN**3*lblblbN)
<<==:
def floor_kth_root_(k, n, /):
    ######################
    let [mmm:=min{k*log2(k), log2(n)}]
    let [lbN:=log2(n)][lblbN:=log2(log2(n))]
    let [lbK:=log2(k)]
    ######################
    ~ O(mmm**3 /k + (lbN -mmm)**2)
    ######################
    ~ [0 <= lbN < k]:O(1)
    ~ [k <= lbN < k*lbK]:O(lbN**3 /k)
    ~ worst[lbN == k*lbK][k==lbN/lblbN]:O(lbN**2 *lblbN)
    ~ [k*lbK < lbN < k*lbK**(3/2)][lbN/lblbN**(3/2) < k < lbN/lblbN]:O(k**2 *lbK**3)
    ~ [lbN > k*lbK**(3/2)]:O(lbN**2)
    ######################
    [lbN == k*lbK] => [k==lbN/lblbN]
    [lbN == k*lbK**(3/2)] => [k==lbN/lblbN**(3/2)]
    [k*lbK < lbN < k*lbK**(3/2)] => [lbN/lblbN**(3/2) < k < lbN/lblbN]
    ######################

]]

[[
CRT-ver-factor_pint_as_pefect_power_:
    O(lbN**3/lblbN)
        lbN**3 come from:
            apply_raw_CRT__inc::num_ps4rt<k>**3

    CRT-ver little better than floor_kth_root_-ver which gives:O(lbN**3)
        CRT-ver:
            [total k == O(lbN/lb_max_p/lblbN) == O(lbN/lblbN**2)]
                #since trial_division enlarge min prime factor(k-th root) of n

        floor_kth_root_-ver:
            [total k == O(lbN/lblbN)]
                # since k is prime
            per k:O(lbN**2 *lblbN)
            total:O(lbN**3)

CRT-ver-detect_pefect_kth_root_:
    O(lbN**3 *(k///odd4k)/k**3 +lbN**2)
    CRT-ver worse than floor_kth_root_-ver which gives: O(lbN**2 *lblbN)

]]
py_adhoc_call   seed.math.factor_pint_as_pefect_power_   @factor_pint_as_pefect_power_  ='257**99'
py_adhoc_call   seed.math.factor_pint_as_pefect_power_   @factor_pint_as_pefect_power_  ='(2**19-1)**99' +verbose

py_adhoc_call   seed.math.factor_pint_as_pefect_power_   @factor_pint_as_pefect_power_  ='257**7' +verbose
py_adhoc_call   seed.math.factor_pint_as_pefect_power_   @factor_pint_as_pefect_power_  ='(257*53)**7' +verbose
...  ...
iter_prime_bases4pefect_kth_root_(3) yield 47
_find_enough_prime_bases_(3, 86988722019525492386235967741) : n:86988722019525492386235967741**II({}) : new prime base 47
iter_prime_bases4pefect_kth_root_(3) yield 53
_find_enough_prime_bases_(3, 86988722019525492386235967741) : n:86988722019525492386235967741///53**7-->74051159531521793
main():loop _k=3: _n:86988722019525492386235967741///II(_p2e4n)-->74051159531521793
main():loop _k=3: _n:74051159531521793
main():loop k_=1
main():loop may_p2e4gcd4e5n={7: 1}
main():loop p2e4n_={53: 7}
main():loop _k=7
main():loop k_=1
main():loop may_p2e4gcd4e5n={7: 1}
main():loop p2e4n_={53: 7}
_detect_pefect_kth_root_(7, 74051159531521793)
_detect_pefect_kth_root_(7, 74051159531521793):odd prime k
...  ...

py_adhoc_call   seed.math.factor_pint_as_pefect_power_   @factor_pint_as_pefect_power_  ='(257*101)**7' +verbose


py_adhoc_call   seed.math.factor_pint_as_pefect_power_   @factor_pint_as_pefect_power_  ='(257*71)**7' +verbose
...  ...
_detect_pefect_kth_root_(7, 673504193807371699307428315063):odd prime k: n:673504193807371699307428315063: rt=?=18247: new prime base to confirm result: 71: found new prime factor
...  ...

py_adhoc_call   seed.math.factor_pint_as_pefect_power_   @factor_pint_as_pefect_power_  ='257*53**2' +verbose

py_adhoc_call   seed.math.factor_pint_as_pefect_power_   @factor_pint_as_pefect_power_  ='257*3**23' +verbose


>>> factor_pint_as_pefect_power_(257*3**23)
(24194796958539, 1)
>>> factor_pint_as_pefect_power_(257*53**2)
(721913, 1)
>>> factor_pint_as_pefect_power_((257*71)**7)
(18247, 7)
>>> factor_pint_as_pefect_power_((257*101)**7)
(25957, 7)
>>> factor_pint_as_pefect_power_((257*53)**7)
(13621, 7)
>>> factor_pint_as_pefect_power_(257**7)
(257, 7)
>>> factor_pint_as_pefect_power_((2**19-1)**99)
(524287, 99)
>>> factor_pint_as_pefect_power_(257**99)
(257, 99)
>>> factor_pint_as_pefect_power_(1)
Traceback (most recent call last):
    ...
ValueError: 1
>>> factor_pint_as_pefect_power_(2)
(2, 1)
>>> factor_pint_as_pefect_power_(3)
(3, 1)
>>> factor_pint_as_pefect_power_(4)
(2, 2)
>>> factor_pint_as_pefect_power_(5)
(5, 1)
>>> factor_pint_as_pefect_power_(6)
(6, 1)
>>> factor_pint_as_pefect_power_(7)
(7, 1)
>>> factor_pint_as_pefect_power_(8)
(2, 3)
>>> factor_pint_as_pefect_power_(9)
(3, 2)
>>> factor_pint_as_pefect_power_(10)
(10, 1)
>>> factor_pint_as_pefect_power_(11)
(11, 1)
>>> factor_pint_as_pefect_power_(11**2)
(11, 2)
>>> factor_pint_as_pefect_power_(101)
(101, 1)
>>> factor_pint_as_pefect_power_(101*103)
(10403, 1)



[[
@20250104
DONE:set_doc_
from seed.tiny_.funcs import set_doc_
]]

[[
@20250104
DONE:类似:平方剩余判定
    静态制表<p>: (n%p)是否是k次幂剩余
view script/辅助冫幂方判定.py
view ../../python3_src/seed/math/_data4factor_pint_as_pefect_power_.py
===
[211 == 1+2*3*5*7]
[2311 == 1+2*3*5*7*11]
[200560490131 == 1+II_primes_le(31)]
===
e script/辅助冫幂方判定.py
    枚举冫顺次奇素数辻相应最小素数牜小于二的八十一次幂牜减一被顺次奇素数整除扌
#>>> [*islice(map(at[2], 枚举冫顺次奇素数辻相应最小素数牜小于二的八十一次幂牜减一被顺次奇素数整除扌()), 100)]
[1, 1, 2, 1, 2, 3, 5, 1, 1, 5, 2, 1, 2, 3, 1, 6, 3, 2, 4, 2, 2, 1, 1, 2, 3, 3, 3, 5, 1, 2, 1, 3, 2, 4, 3, 5, 2, 7, 1, 1, 3, 1, 2, 9, 2, 5, 6, 12, 6, 1, 1, 3, 1, 3, 3, 4, 3, 2, 1, 3, 1, 2, 3, 3, 13, 3, 5, 3, 5, 7, 1, 3, 2, 6, 6, 12, 3, 4, 2, 1, 5, 1, 2, 5, 1, 4, 15, 3, 6, 3, 4, 2, 1, 2, 3, 1, 16, 5, 9, 5]

[
def _考察冫阈值间素因子纟阈值以下规模纟素模乘法群扌(min4factor, max4factor, max4modulus, /):
    'min4factor -> max4factor -> max4modulus -> Iter (p, [modulus]){[p <- [min4factor..=max4factor]][is_prime(modulus)][modulus%p==1]}'
===
py_adhoc_call   script.辅助冫幂方判定   ,_考察冫阈值间素因子纟阈值以下规模纟素模乘法群扌  =2  =7  =100
(2, [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
(3, [7, 13, 19, 31, 37, 43, 61, 67, 73, 79, 97])
(5, [11, 31, 41, 61, 71])
(7, [29, 43, 71])
===
py_adhoc_call   script.辅助冫幂方判定   ,_考察冫阈值间素因子纟阈值以下规模纟素模乘法群扌  =11  =47  =500
===
(11, [23, 67, 89, 199, 331, 353, 397, 419, 463])
(13, [53, 79, 131, 157, 313, 443])
(17, [103, 137, 239, 307, 409, 443])
(19, [191, 229, 419, 457])
(23, [47, 139, 277, 461])
(29, [59, 233, 349])
(31, [311, 373])
(37, [149, 223])
(41, [83])
(43, [173, 431])
(47, [283])
===
]
xxx[没必要重复<<==%(M0*M1)即可降低运算量]==>>: 最多挑选3个模，尽量重复...
忽略2
次序:7,5,3; => [29,31,43,61,71]
!! [modulus <= 500][2*11*13 == 286] => 超过10的素因子相应模 不太可能 重复
    只有:419,443
(2, ...[31, 43, 61])
(3, [31, 43, 61])
(5, [31, 61, 71])
(7, [29, 43, 71])
(11, [23, 67, 89, 419])
(13, [53, 79, 131, 443])
(17, [103, 137, 239, 443])
(19, [191, 229, 419])
(23, [47, 139, 277])
(29, [59, 233, 349])
(31, [311, 373])
(37, [149, 223])
(41, [83])
(43, [173, 431])
(47, [283])
++(53, [107])

==>>: 挑选几个最小模
(2, [3, 5, 7, 11, 13, 17, 19, 23, 29])
(3, [7, 13, 19])
(5, [11, 31, 41])
(7, [29, 43, 71])
(11, [23, 67, 89])
(13, [53, 79, 131])
(17, [103, 137])
(19, [191])
(23, [47, 139])
(29, [59])
(31, [311])
(37, [149])
(41, [83])
(43, [173])
(47, [283])
++(53, [107])

===
发现没必要保存整个表O(N)即O(prime_modulus)
    [N==1+d*p4Nmm]
    只有(1+d)即(1+((N-1)/p4Nmm))个 模幂方数
    当d足够小时，可直接保存 所有 模幂方数
from seed.math._data4factor_pint_as_pefect_power_ import p4Nmm_scales_pairs, p4Nmm_Ns_pairs, p4Nmm2Ns, p4Nmm2II_Ns, p4Nmm2N2modpows
]]

@20250104
found_bugs_20250104
Exception: (268, ({2: 2}, 67, {2: 1}), {2: 1})
Exception: (517, (11, 47, 1, 3), (47, 1, 3))
Exception: (639, ({3: 2}, 71, {2: 1}), {2: 1})
>>> factor_pint_as_pefect_power_(268)
(268, 1)
>>> factor_pint_as_pefect_power_(517)
(517, 1)
>>> factor_pint_as_pefect_power_(639)
(639, 1)

>>> from math import floor, ceil
>>> def _factor_pint_as_pefect_power_(n, /, *, float_type:'float|Decimal'):
...     for e in reversed(range(1, 1+n.bit_length())):
...         r = n**(1/float_type(e))
...         r1 = ceil(r)
...         r0 = floor(r)
...         n1 = r1**e
...         n0 = r0**e
...         if n0 < n < n1:continue
...         if n1 == n:return (r1, e)
...         if n0 == n:return (r0, e)
...         raise Exception((n, e), (r1, r0), (n1, n0))
...             #Exception: ((284144440414418491, 1), (284144440414418496, 284144440414418496), (284144440414418496, 284144440414418496))
...                 #==>> ++kw:float_type to use Decimal

>>> def _test_factor_pint_as_pefect_power_eq(n, /, *, float_type:'float|Decimal'):
...     r_e = factor_pint_as_pefect_power_(n)
...     _r_e = _factor_pint_as_pefect_power_(n, float_type=float_type)
...     assert r_e == _r_e, (n, r_e, _r_e)
>>> def _test_factor_pint_as_pefect_power_lt(m, /, *, float_type:'float|Decimal'):
...     for n in range(2, m):
...         _test_factor_pint_as_pefect_power_eq(n, float_type=float_type)
>>> _test_factor_pint_as_pefect_power_lt(1+2**16, float_type=float)

>>> from math import *
>>> log10((2*3*17*23)**6)
20.221968046677063
>>> log10((2*3*17*23)**12)
40.443936093354125
>>> (2*3*17*23)**12
27793042616829652326068869392049880764416
>>> ((2*3*17*23)**12).bit_length()
135
>>> from itertools import product
>>> def _test_factor_pint_as_pefect_power__comb(max4e4p=10, *, float_type:'float|Decimal'):
...     bases = [2, 3, 17, 23]
...     max1_e = 5
...     #for e2 in range(0, 11):
...     # for e3 in range(0, 11):
...     #  for e17 in range(0, 11):
...     #   for e23 in range(0, 11):
...     #    n = 2**e2 * 3**e3 * 17**e17 * 23**e23
...     for es in product(range(0, 1+max4e4p), repeat=len(bases)):
...         n = II(map(int.__pow__, bases, es))
...         if n == 1:continue
...         _test_factor_pint_as_pefect_power_eq(n, float_type=float_type)
>>> from decimal import localcontext, Decimal
>>> with localcontext(prec=50) as ctx:ctx
Context(prec=50, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
>>> with localcontext(prec=50):_test_factor_pint_as_pefect_power__comb(10, float_type=Decimal)     #doctest: +SKIP
>>> with localcontext(prec=30):_test_factor_pint_as_pefect_power__comb(4, float_type=Decimal)




is_kth_power_
    is_square_
    is_cube_
>>> is_square_(8)
False
>>> is_square_(9)
True
>>> is_cube_(8)
True
>>> is_cube_(9)
False

>>> for k in range(-3, 3+1):
...     [(k,n) for n in range(-27, 27+1) if is_kth_power_(k,n)]
[(-3, -1), (-3, 1)]
[(-2, 1)]
[(-1, -1), (-1, 1)]
[(0, 1)]
[(1, -27), (1, -26), (1, -25), (1, -24), (1, -23), (1, -22), (1, -21), (1, -20), (1, -19), (1, -18), (1, -17), (1, -16), (1, -15), (1, -14), (1, -13), (1, -12), (1, -11), (1, -10), (1, -9), (1, -8), (1, -7), (1, -6), (1, -5), (1, -4), (1, -3), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18), (1, 19), (1, 20), (1, 21), (1, 22), (1, 23), (1, 24), (1, 25), (1, 26), (1, 27)]
[(2, 0), (2, 1), (2, 4), (2, 9), (2, 16), (2, 25)]
[(3, -27), (3, -8), (3, -1), (3, 0), (3, 1), (3, 8), (3, 27)]

>>> for k in range(2, 17):     #doctest: +SKIP
...     for n in range(2, 2**16):
...         assert is_kth_power_(k, n) == _is_kth_power_(k, n), (k, n)











>>> may_perfect_kth_root_(2, 27)
>>> may_perfect_kth_root_(2, -4)
>>> may_perfect_kth_root_(-2, -4)
>>> may_perfect_kth_root_(-2, 1)
1
>>> may_perfect_kth_root_(-2, 0)
>>> may_perfect_kth_root_(2, 0)
0
>>> may_perfect_kth_root_(1, 0)
0
>>> may_perfect_kth_root_(0, 0)
>>> may_perfect_kth_root_(0, 0, default='')
''


>>> may_perfect_kth_root_(3, 27)
3
>>> may_perfect_kth_root_(9, 999**9)
999
>>> may_perfect_kth_root_(3, -27)
-3
>>> may_perfect_kth_root_(9, -999**9)
-999
>>> may_perfect_cbrt_(-27)
-3
>>> may_perfect_sqrt_(-27)
>>> may_perfect_sqrt_(4)
2








#]]]'''
_4doctest = r'''[[[


#]]]'''#'''
__all__ = r'''
factor_pint_as_pefect_power_
is_kth_power_
    is_square_
    is_cube_
may_perfect_kth_root_
    may_perfect_sqrt_
    may_perfect_cbrt_


get_or_mk_config4primes4le_zpow_
    config4primes4le_2
    config4primes4le_4
    config4primes4le_8
    config4primes4le_16
    config4primes4le_32
    config4primes4le_64
    config4primes4le_128
    config4primes4le_256

'''.split()#'''
__all__

___begin_mark_of_excluded_global_names__0___ = ...
class _G:
    from seed.math._data4factor_pint_as_pefect_power_ import p4Nmm_scales_pairs, p4Nmm_Ns_pairs, p4Nmm2Ns, p4Nmm2II_Ns, p4Nmm2N2modpows

from functools import cache
from itertools import takewhile
#from seed.tiny_.funcs import set_doc_
from seed.tiny_.check import check_int_ge, check_type_is
from seed.math.floor_ceil import floor_kth_root_, ceil_div, ceil_log2
#
from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_# factor_pint_out_2_powers
from seed.math.factor_pint_by_trial_division_ import factor_pint_by_trial_division_ex_# default4upperbound4probably_prime, check_result5factor_pint_
from seed.math.II import II, II__p2e_#, II_mod
from seed.math.gcd import gcd
from seed.math.prime_gens import prime_gen
from seed.math.factor_pint.factor_pint__naive_brute_force import factor_pint__naive_brute_force_, iter_factor_pint__naive_brute_force_

___end_mark_of_excluded_global_names__0___ = ...



__all__
def _prepare4is_kth_power_(max_k, max_n, /):
    _k2kpows = [None, None]
    for k in range(2, 1+max_k):
        s = set()
        for i in range(2, 1+max_n):
            n = i**k #kpow
            if n > max_n:break
            s.add(n)
        _k2kpows.append(s)
    return _k2kpows
_k2kpows = _prepare4is_kth_power_(10, 2**10)
assert len(_k2kpows) == 11
assert _k2kpows[-1] is _k2kpows[10]
assert _k2kpows[-1] == {1024}, _k2kpows[-1]

def _prepare4kth_root_(max_k, max_n, /):
    _k2pow2rt = [None, None]
    for k in range(2, 1+max_k):
        d = {}
        for i in range(2, 1+max_n):
            n = i**k #kpow
            if n > max_n:break
            d[n] = i
        _k2pow2rt.append(d)
    return _k2pow2rt
_k2pow2rt = _prepare4kth_root_(10, 2**10)
assert len(_k2pow2rt) == 11
assert _k2pow2rt[-1] is _k2pow2rt[10]
assert _k2pow2rt[-1] == {1024:2}, _k2pow2rt[-1]


_3_5_7_11_13 = (3,5,7,11,13)
_II_3_5_7_11_13 = II(_3_5_7_11_13)
def is_kth_power_(k, n, /):
    'k/int -> n/int -> bool/(floor_kth_root_(k;n)**k==n)'
    #def is_perfect_kth_power_(k, n, /):
    return not None is may_perfect_kth_root_(k, n)
def may_perfect_kth_root_(k, n, /, *, default=None):
    'k/int -> n/int -> may perfect_kth_root/int{perfect_kth_root**k==n}'
    check_type_is(int, k)
    check_type_is(int, n)
    m = _0_may_perfect_kth_root_(k, n)
    if m is None:
        return default
    check_type_is(int, m)
    return m
def _0_may_perfect_kth_root_(k, n, /):
    m = _1_may_perfect_kth_root_(k, n)
    if type(m) is bool:raise 000
    return m
def _1_may_perfect_kth_root_(k, n, /):
    default = None
    #_try_best_to_detect_non_pefect_power_
    if n < 0:
        # [n < 0]
        if k&1 == 0:
            # [even k]
            return default
            return False
        # [odd k]
        n = -n
        # [n > 0]
        if 0x0001:
            mr = _0_may_perfect_kth_root_(k, n)
            return default if mr is None else -mr
    # [n >= 0]
    if n < 2:
        if n == 1:
            return 1
            return True
        if n == 0:
            # 0**0 ok
            # 0**0==1 not 0
            return 0 if k >= 1 else default
            return k >= 1
        raise 000
    # [n >= 2]
    if k < 2:
        return n if k == 1 else default
        return k == 1
    # [k >= 2]
    # [n >= 2]
    if n&1 == 0:
        # [n%2 == 0]
        # [n >= 2]
        (ez, n) = factor_pint_out_power_of_base_(2, n)
        # [n >= 1]
        # [n%2 == 1]
        if not ez%k == 0:
            return default
            return False
        ez //= k
        if n == 1:
            return 1 << ez
            return True
        # [n >= 2]
        # [n%2 == 1]
        # [n >= 3]
        if 0x0001:
            mr = _0_may_perfect_kth_root_(k, n)
            return default if mr is None else (mr << ez)
    # [n%2 == 1]
    # [n >= 3]

    if n <= 1024:
        # [2 <= n <= 1024]
        if k > 10:
            return default
            return False
        return _k2pow2rt[k].get(n, default)
        return n in _k2kpows[k]
    # [n > 1024]
    # [n%2 == 1]
    L = n.bit_length()
    # [1024 < 2**L <= n < 2**L]
    # [L >= 11]
    # [k >= 2]
    if k >= L:
        return default
        return False
    # [2 <= k < L]

    # !! [2**3 < 3**2]
    # [2 < 3**(2/3)]
    # [n < 2**L < 3**(2*L/3)]
    # !! [L >= 11]
    # [2*L/3 < L-1]
    if 3*k >= 2*L:
        # [k >= 2*L/3]
        # [3**k >= 3**(2*L/3) > n]
        # [n%2 == 1]
        return default
        return False
        return k == L-1 and n == (1<<k)
    # [2 <= k < 2*L/3]
    # [1024 < 2**L <= n < 2**L]
    # [n%2 == 1]
    # !! [2**4 < 17]
    # [n < 2**L < 17**(L/4)]
    if 4*k >= L:
        # [k >= L/4]
        # [17**k >= 17**(L/4) > n]
        # [n%2 == 1]
        ds = []
        _n = n%_II_3_5_7_11_13
        for p in _3_5_7_11_13:
            if _n%p == 0:
                if ds and p > 5:
                    return default
                    return False
                ds.append(p)
        if not ds:
            return default
            return False
        assert len(ds) == 1 or ds == [3,5]
        # [9==3**2 is not useless since k const]
        if 3 in ds:
            if len(ds) == 2:
                ds.append(15)
            ds.append(9)
        if 0x0001:
            for d in ds:
                if d**k == n:
                    return d
            return default
        raise 000
        return any(d**k == n for d in ds)
    # [2 <= k < L/4]
    # [1024 < 2**L <= n < 2**L]
    # [n%2 == 1]
    #see:_try_best_to_detect_non_pefect_power_
    if _try_best_to_detect_non_pefect_power_(k, n):
        # NOTE:[k may be not prime]
        #   intended to abuse
        return default
        return False
    if L > 257 and k >= 4:
        for (p,ep) in iter_factor_pint__naive_brute_force_(k):
            if _try_best_to_detect_non_pefect_power_(p, n):
                return default
                return False
    _rt = floor_kth_root_(k, n)
    return _rt if n == _rt**k else default
    return n == floor_kth_root_(k, n)**k
def _is_kth_power_(k, n, /):
    return n == floor_kth_root_(k, n)**k

def may_perfect_sqrt_(n, /, *, default=None):
    'n/int -> may perfect_sqrt/int{perfect_sqrt**2==n}'
    return may_perfect_kth_root_(2, n, default=default)
def may_perfect_cbrt_(n, /, *, default=None):
    'n/int -> may perfect_cbrt/int{perfect_cbrt**3==n}'
    return may_perfect_kth_root_(3, n, default=default)

def is_square_(n, /):
    #def is_perfect_square_(n, /):
    'n/int -> bool/(isqrt(n)**2==n)'
    return is_kth_power_(2, n)
def is_cube_(n, /):
    #def is_perfect_cube_(n, /):
    'n/int -> bool/(floor(cbrt(n))**3==n)'
    return is_kth_power_(3, n)
#.def _try_best_to_detect_non_pefect_power_(e, n, /):
#.    'e/uint -> n/uint -> sure_non_pefect_power{True=>[not [?[rt::uint]. rt**e==n]];False=>unsure}/bool'
#.    check_int_ge(0, e)
#.    check_int_ge(0, n)
#.    if e == 0:
#.        return not n == 1
#.    if e == 1:
#.        return False
#.    # [e >= 2]
#.    if n <= 1:
#.        return False
#.    # [n >= 2]
#.    ... ...
def _try_best_to_detect_non_pefect_power_(e, n, /):
    'e/prime/uint{>=2} -> n/uint{>=2} -> sure_non_pefect_power{True=>[not [?[rt::uint]. rt**e==n]];False=>unsure}/bool'
    # [e >= 2]
    # [n >= 2]
    assert e >= 2
    assert n >= 2
    # [p4Nmm := e]
    if (II_Ns := _G.p4Nmm2II_Ns.get(e)):
        rem = n %II_Ns
        Ns = _G.p4Nmm2Ns[e]
        N2modpows = _G.p4Nmm2N2modpows[e]
        for N in Ns:
            modpows = N2modpows[N]
            if not rem%N in modpows:
                return True#non_pefect_power
    else:
        # [e is prime which larger cached ones] or abuse:[e is not prime]{it is intended not to raise at this case}
        pass
    #######
    return False#unsure
if 1:
    from seed.math._data4factor_pint_as_pefect_power_ import cache4factor_pint_as_pefect_power_ as _cache
#xxx:@set_doc_(_doc4factor_pint_as_pefect_power__CRT_ver_, force=True)
def factor_pint_as_pefect_power_(n, /, *, verbose=False, _to_eliminate_the_dominant_branch=True):
    'n/int{>=2} -> (base/int{>=2}, exp/int{>=1}){n==base**exp} #floor_kth_root_-ver2@20250105:[TIME(factor_pint_as_pefect_power_(n)) ~<= O(lbN**3*lblblbN) if not _to_eliminate_the_dominant_branch else O(lbN**3)]'
    check_int_ge(1, n)
    if not n >= 2:raise ValueError(n)
    # [n >= 2]
    if not n >= 4:
        return (n, 1)
    # [n >= 4]
    ######################
    if n < len(_cache):
        return _cache[n]
    ######################
    if _to_eliminate_the_dominant_branch:
        # [exp4zpow ~>= lblbN]
        lbN = ceil_log2(n)
        lblbN = ceil_log2(lbN)
        exp4zpow = lblbN
        # !! [n >= 4]
        # [lbN >= 2]
        # [lblbN >= 1]
        assert exp4zpow >= 1
        # [{exp4zpow:minN} == {e:2**2**e} == {1:4, 2:16, 3:256, 4:65536, 5:4294967296, 6:18446744073709551616, 7:340282366920938463463374607431768211456, 8:115792089237316195423570985008687907853269984665640564039457584007913129639936, ..., 14:ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit, ...}]
    else:
        exp4zpow = 4
        #config4primes4le_zpow = config4primes4le_16
            #config4primes4le_zpow = config4primes4le_256
    exp4zpow
    exp4zpow = max(4, exp4zpow)
    config4primes4le_zpow = get_or_mk_config4primes4le_zpow_(exp4zpow)
    ######################
    (exp4zpow, zpow, primes4le_zpow, product4primes4le_zpow) = config4primes4le_zpow
    ######################
    # !! [exp4zpow >= 1]
    # [2 in primes4le_zpow]
    assert exp4zpow >= 1
    assert primes4le_zpow and primes4le_zpow[0] == 2
    ######################
    #assert zpow == 256 #for 257==256+1
    #assert product4primes4le_zpow == 64266330917908644872330635228106713310880186591609208114244758680898150367880703152525200743234420230
        # !! product4primes4le_zpow is too big
    ######################
    if not _to_eliminate_the_dominant_branch:
        assert exp4zpow == 4
        assert zpow == 16 #for 17==16+1
        assert product4primes4le_zpow == 30030
        #assert config4primes4le_16 == (4, 16, (2, 3, 5, 7, 11, 13), 30030), config4primes4le_16
    ######################
    #if gcd(n, product4primes4le_zpow):
    (b_stop, payload) = _factor_pint_as_pefect_power__try_small_prime_factors(primes4le_zpow, n, verbose=verbose)
        #DONE:eliminate the_dominant_branch&the_secondary_branch via _factor_pint_as_pefect_power__try_small_prime_factors
        #   let [max4exp < lbN/lblbN] to eliminate the_dominant_branch&the_secondary_branch
        #   let [max4exp < lbN/lblbN**(3/2)] to eliminate the_dominant_branch&the_secondary_branch
    if b_stop:
        (base, exp) = payload
        assert (base, exp) == (n, 1)
        return (base, exp)
    (gcd4es4ps, p_e_pairs, _n) = payload
    # [[_n==1]or[min_prime_factor{_n} > zpow]]
    if gcd4es4ps == 0:
        assert not p_e_pairs
        #assert _n is n, (n, _n)
        assert _n == n, (n, _n)
        # [_n == n]
        # !! [n >= 4]
        # !! [[_n==1]or[min_prime_factor{_n} > zpow]]
        # [min_prime_factor{n} > zpow]
        # !! [n <= 2**ceil_log2(n)]
        # [n <= 2**ceil_log2(n) == zpow**(ceil_log2(n)/exp4zpow) <= zpow**ceil_div(ceil_log2(n), exp4zpow)]
        # [n <= zpow**ceil_div(ceil_log2(n), exp4zpow)]
        # !! [min_prime_factor{n} > zpow]
        # [log_(min_prime_factor{n}; n) < log_(zpow; n) <= ceil_div(ceil_log2(n), exp4zpow)]
        # [floor_log_(min_prime_factor{n}; n) <= ceil_div(ceil_log2(n), exp4zpow) -1]
        max4exp = ceil_div(ceil_log2(n), exp4zpow) -1
        assert max4exp >= 1
        result = _factor_pint_as_pefect_power__basic(max4exp, n, verbose=verbose)
    else:
        assert gcd4es4ps >= 2
        assert p_e_pairs
        assert 1 <= _n < n
        # !! [exp4zpow >= 1]
        # [2 in primes4le_zpow]
        # [odd _n]
        assert _n&1
        if _n == 1:
            _result = (1, gcd4es4ps)
        else:
            # [_n >= 2]
            p2max_e4exp = p2e4gcd4es = _factor_small_pint_(gcd4es4ps)
            assert p2max_e4exp
            _max4exp = ceil_div(ceil_log2(_n), exp4zpow) -1
            _result = _factor_pint_as_pefect_power__extend(p2max_e4exp, _max4exp, _n, verbose=verbose)
        _result
        (_base, exp) = _result
        base = _base*II(p**(e//exp) for p,e in p_e_pairs)
        result = (base, exp)
    result
    #if validate:
    if __debug__:
        (base, exp) = result
        assert n == base**exp
    return result

def _factor_pint_as_pefect_power__basic(max4exp, n, /, *, verbose):
    'max4exp{>=1} -> n/int{>=2} -> (base/int{>=2}, exp/int{>=1}){n==base**exp}'
    assert max4exp >= 1
    assert n >= 2
    ps4exp = takewhile(max4exp.__ge__, iter(prime_gen))
    #ps4exp = (p4exp for p4exp in ps4exp if not _try_best_to_detect_non_pefect_power_(p4exp, n))
        # !! [_n decreasing]
    p2max_e4exp_ = lambda _, /:max4exp
    return _factor_pint_as_pefect_power__common(ps4exp, p2max_e4exp_, max4exp, n, verbose=verbose)


def _factor_pint_as_pefect_power__extend(p2max_e4exp, max4exp, n, /, *, verbose):
    'p2max_e4exp/{p4exp:max_e4p4exp} -> max4exp{>=1} -> n/int{>=2} -> (base/int{>=2}, exp/int{>=1}){n==base**exp}{II__p2e_(p2max_e4exp)%exp==0}'
    assert p2max_e4exp
    assert max4exp >= 1
    assert n >= 2
    ps4exp = sorted(p2max_e4exp)
    # !! [_n decreasing]
        #.ps4exp = [p4exp for p4exp in ps4exp if not _try_best_to_detect_non_pefect_power_(p4exp, n)]
        #.if not ps4exp:
        #.    #non_pefect_power
        #.    return (n, 1)
    p2max_e4exp_ = p2max_e4exp.__getitem__
    return _factor_pint_as_pefect_power__common(ps4exp, p2max_e4exp_, max4exp, n, verbose=verbose)

def _factor_pint_as_pefect_power__common(ps4exp, p2max_e4exp_, max4exp, n, /, *, verbose):
    'ps4exp/sorted-Iter (candidate_prime_factor4exp/prime/pint) -> p2max_e4exp_/(p4exp->max_e4p4exp) -> max4exp{>=1} -> n/int{>=2} -> (base/int{>=2}, exp/int{>=1}){n==base**exp}{II__p2e_(p2max_e4exp)%exp==0}'
    ps4exp = iter(ps4exp)
    assert callable(p2max_e4exp_)
    assert max4exp >= 1
    assert n >= 2

    p2e4exp = {}
    _n = n
    _max4exp = max4exp
    for p4exp in ps4exp:
        if not p4exp <= _max4exp:
            # !! _max4exp updated/decreasing
            break
        if _try_best_to_detect_non_pefect_power_(p4exp, _n):
            #non_pefect_power@p4exp
            continue
        #max_e4p4exp = p2max_e4exp[p4exp]
        max_e4p4exp = p2max_e4exp_(p4exp)
        for e4p in range(1, 1+max_e4p4exp):
            rt = floor_kth_root_(p4exp, _n)
            if not rt**p4exp == _n:
                e4p -= 1
                break
            _n = rt
            _max4exp //= p4exp
                # _max4exp updated/decreasing
        e4p, _n
        if e4p:
            p2e4exp[p4exp] = e4p
        _n
    p2e4exp, _n
    exp = II__p2e_(p2e4exp)
    base = _n
    return (base, exp)

_2357 = (2,3,5,7)
#_small_primes = _2357
def _mk_config4primes4le_zpow_(exp4zpow, /):
    check_int_ge(1, exp4zpow)
    zpow = 1 << exp4zpow
    primes4le_zpow = small_continuous_primes = tuple(takewhile(zpow.__ge__, iter(prime_gen)))
    product4primes4le_zpow = II(primes4le_zpow)
    config4primes4le_zpow = (exp4zpow, zpow, primes4le_zpow, product4primes4le_zpow)
    return config4primes4le_zpow
#config4primes4le_2 = _mk_config4primes4le_zpow_(1)
#config4primes4le_4 = _mk_config4primes4le_zpow_(2)
#config4primes4le_8 = _mk_config4primes4le_zpow_(3)
#config4primes4le_16 = _mk_config4primes4le_zpow_(4)
#config4primes4le_32 = _mk_config4primes4le_zpow_(5)
#config4primes4le_64 = _mk_config4primes4le_zpow_(6)
#config4primes4le_128 = _mk_config4primes4le_zpow_(7)
#config4primes4le_256 = _mk_config4primes4le_zpow_(8)
_ls4config4primes4le_zpow = [_mk_config4primes4le_zpow_(exp4zpow) for exp4zpow in range(1, 9)]
[config4primes4le_2, config4primes4le_4, config4primes4le_8, config4primes4le_16, config4primes4le_32, config4primes4le_64, config4primes4le_128, config4primes4le_256] = _ls4config4primes4le_zpow
#print(_ls4config4primes4le_zpow)
assert _ls4config4primes4le_zpow == (
[(1, 2, (2,), 2)
,(2, 4, (2, 3), 6)
,(3, 8, (2, 3, 5, 7), 210)
,(4, 16, (2, 3, 5, 7, 11, 13), 30030)
,(5, 32, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31), 200560490130)
,(6, 64, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61), 117288381359406970983270)
,(7, 128, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127), 4014476939333036189094441199026045136645885247730)
,(8, 256, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251), 64266330917908644872330635228106713310880186591609208114244758680898150367880703152525200743234420230)
]), _ls4config4primes4le_zpow

assert config4primes4le_16 == (4, 16, (2, 3, 5, 7, 11, 13), 30030), config4primes4le_16

#++kw:_to_eliminate_the_dominant_branch
@cache
def get_or_mk_config4primes4le_zpow_(exp4zpow, /):
    check_int_ge(1, exp4zpow)
    if (i:=exp4zpow-1) < len(_ls4config4primes4le_zpow):
        return _ls4config4primes4le_zpow[i]
    return _mk_config4primes4le_zpow_(exp4zpow)

def _factor_pint_as_pefect_power__try_small_prime_factors(ps, n, /, *, verbose):
    'n/int{>=2} -> (b_stop/bool, payload)/((False, ...)|(True, (base/int{>=2}, exp/int{>=1}){n==base**exp}))'
    _n = n
    gcd4es4ps = 0
    p_e_pairs = []
    for p in ps:
        e4p, _n = factor_pint_out_power_of_base_(p, _n)
        if e4p:
            p_e_pairs.append((p, e4p))
            gcd4es4ps = gcd(gcd4es4ps, e4p)
            if gcd4es4ps == 1:
                return (True, (n, 1))
    assert not gcd4es4ps == 1
    assert (not gcd4es4ps == 0) is bool(p_e_pairs)
    return (False, (gcd4es4ps, p_e_pairs, _n))







def _factor_small_pint_(n, /):
    (p2e4n, unfactored_part, may_next_prime_factor) = factor_pint_by_trial_division_ex_(n, may_upperbound4prime_factor=n+1)
    if not unfactored_part == 1:raise 000
    return p2e4n

def _fill_cache(max_n, /):
    _cache.extend(map(factor_pint_as_pefect_power_, range(len(_cache), 1+max_n)))
if __name__ == "__main__":
    if '_cache' not in globals() or len(_cache) < 3:
        _cache = [None, None]
            #_fill_cache():goto
            #fill only once, cache no more
        _fill_cache(1 << 12)
        if 0b0001:[*map(print, _cache)]
del _fill_cache
















def _perfect_kth_root__p2e_(p2e, k, /):
    d = {}
    for p, e in p2e.items():
        q, r = divmod(e, k)
        if r: raise 000
        d[p] = q
    return d




__all__
def __():
    #cancel:TODO:
    def detect_pefect_quotient_(n, d, /):
        'n/uint -> d/pint -> may q/uint # [[result is None] =!= [n%d==0]][q == n///d]'
        r'''[[[
        if d is small near 0, then divmod(n,d) is fast enough
            since to apply Chinese_Remainder_Theorem, we need to call n%p
        if d is large near n, then divmod(n,d) is fast, too
        if d,q near sqrt(n):
            is Chinese_Remainder_Theorem useful?
            [II(ps) > n]
                [O(len(ps)) ~= log2(n)]
            [ns := {n%p | [p :<- ps]}]
                O(log2(n))*time4mod
                O(log2(n)**2)
            not better than divmod(n,d)
        #]]]'''#'''


_doc4factor_pint_as_pefect_power__CRT_ver_ = \
r'''[[[
'n/int{>=2} -> (base/int{>=2}, exp/int{>=1}){n==base**exp}'

O(lbN**3/lblbN)
    lbN**3 come from:
        apply_raw_CRT__inc::num_ps4rt<k>**3

CRT-ver little better than floor_kth_root_-ver which gives:O(lbN**3)
    CRT-ver:
        [total k == O(lbN/lb_max_p/lblbN) == O(lbN/lblbN**2)]
            #since trial_division enlarge min prime factor(k-th root) of n

    floor_kth_root_-ver:
        [total k == O(lbN/lblbN)]
            # since k is prime
        per k:O(lbN**2 *lblbN)
        total:O(lbN**3)

######################
######################vs:
O(bisearch-ver:floor_kth_root_) ~ O(log2(n)**3/k)
O(floor_sqrt) ~ O(log2(n)**2)
O(floor_kth_root_) ~:
######################
let [mmm:=min{k*log2(k), log2(n)}]
let [lbN:=log2(n)][lblbN:=log2(log2(n))]
let [lbK:=log2(k)]
######################
~ O(mmm**3 /k + (lbN -mmm)**2)
######################
~ [0 <= lbN < k]:O(1)
~ [k <= lbN < k*lbK]:O(lbN**3 /k)
~ worst[lbN == k*lbK][k==lbN/lblbN]:O(lbN**2 *lblbN)
~ [k*lbK < lbN < k*lbK**(3/2)]:O(k**2 *lbK**3)
~ [lbN > k*lbK**(3/2)]:O(lbN**2)
######################



#]]]'''#'''

__all__
def __():
  if 1:
    from itertools import count as count_
    from seed.tiny_.funcs import set_doc_
    from seed.tiny_.check import check_type_is# check_int_ge
    from seed.math.II import II__p2e_#II, II_mod
    from seed.math.floor_ceil import floor_log2, ceil_log2
    from seed.math.floor_ceil import floor_log2_kth_root_# ceil_log2_kth_root_
    from seed.math.floor_ceil import floor_sqrt# ceil_sqrt
    from seed.math.gcd import gcd_many #, gcd#, are_coprime
    #
    from seed.math.inv_mod_ex import ginv_mod_
    #    #(inv_x_g, k4M, k4x, gcd_of_Mx, M_g, x_g) = ginv_mod_(M, x)

    from seed.math.prime_gens import prime_gen
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_# factor_pint_out_2_powers
    from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
    from seed.math.Chinese_Remainder_Theorem import apply_raw_CRT__inc, mk_coeff_pairs4apply_raw_CRT__inc
    #
  def __():
    # API:
    from seed.math.Chinese_Remainder_Theorem import apply_raw_CRT__inc, mk_coeff_pairs4apply_raw_CRT__inc
    def apply_raw_CRT__inc(us, vs, coeff_pairs, rs, /, *, partial_ok=False):
        r'''[[[
        'moduli/[pint] -> accumulated_partial_moduli/[pint] -> coeff_pairs/[(uint%moduli[i], uint%accumulated_partial_moduli[i])] -> remainders/[uint%moduli[i]] -> whole_remainder/uint%whole_modulus'

        'us/[pint] -> vs/[pint]{.len==1+len(us);.[i]==II(us[:i])} -> coeff_pairs/[(uint%us[i], uint%vs[i])]{.[i]==(vs[i]*inv_mod_(us[i];vs[i]), us[i]*inv_mod_(vs[i];us[i])))} -> remainders/[uint%us[i]]{len==len(us)} -> whole_remainder/uint%vs[-1]'
        #]]]'''#'''
    def mk_coeff_pair4apply_raw_CRT__inc(u, v, /):
        'u -> v -> (coeff4u, coeff4v){coeff4x == inv_mod_(x;y)*y %(x*y)} |^CRT_Error__moduli_not_coprime if [gcd(u,v) =!= 1]'
    def mk_coeff_pairs4apply_raw_CRT__inc(us, vs, /):
        'us/[pint] -> vs/{.len=1+len(us)}{vs[i]==II(us[:i])} -> coeff_pairs/[(coeff4u, coeff4v)]{coeff4x == inv_mod_(x;y)*y %(x*y)} |^CRT_Error__moduli_not_coprime if [gcd(u[i],v[i]) =!= 1]'
    def mk_accumulated_partial_moduli4apply_raw_CRT__inc(us, /):
        'us/[pint] -> vs/{.len=1+len(us)}{vs[i]==II(us[:i])}'
    def prepare4apply_raw_CRT__inc(us, /):
        'us/[pint] -> (vs/{.len=1+len(us)}{vs[i]==II(us[:i])}, coeff_pairs/[(coeff4u, coeff4v)]{coeff4x == inv_mod_(x;y)*y %(x*y)}) |^CRT_Error__moduli_not_coprime if [gcd(u[i],v[i]) =!= 1]'


  if 0:
    #deprecated-version@20250104
    #found_bugs_20250104
    Exception: (268, ({2: 2}, 67, {2: 1}), {2: 1})
    Exception: (517, (11, 47, 1, 3), (47, 1, 3))
    Exception: (639, ({3: 2}, 71, {2: 1}), {2: 1})
  @set_doc_(_doc4factor_pint_as_pefect_power__CRT_ver_, force=True)
  def factor_pint_as_pefect_power__buggy_(n, /, *, verbose=False):
  #def factor_pint_as_pefect_power_(n, /, *, verbose=False):
    'n/int{>=2} -> (base/int{>=2}, exp/int{>=1}){n==base**exp}'
    #cache:_get_ginv_mod_<{p-1:{_k:(gcd, may_inv_k)}}>
    #cache:_get_mod_<{p:(n,r4n)}>
    u2v2res4ginv = {}
    def _get5cache_(lazy_, d, /, *ks, **kwds):
        [*ks_, kl] = ks
        for k_ in ks_:
            d = d.setdefault(k_, {})
        if kl not in d:
            d[kl] = lazy_(*ks, **kwds)
        r = d[kl]
        return r
    p2b2e2pow = {}
    def lazy4pow_(p, base, exp, /):
        return pow(base, exp, p)
    def _pow_(base, exp, p, /):
        # [p :: prime]
        exp %= p-1
        base %= p
        return _get5cache_(lazy4pow_, p2b2e2pow, p, base, exp)
    def lazy4get_ginv_mod_(u, v, /):
        (inv_v_g, k4u, k4v, gcd_of_uv, u_g, v_g) = ginv_mod_(u, v)
        if gcd_of_uv == 1:
            may_inv_v_g = inv_v_g
        else:
            may_inv_v_g = None
        return gcd_of_uv, may_inv_v_g
    def _get_ginv_mod_(u, v, /):
        v = v%u
        return _get5cache_(lazy4get_ginv_mod_, u2v2res4ginv, u, v)
    def lazy4get_mod_(p, /, *, n):
        e4n, coprime4p = factor_pint_out_power_of_base_(p, n)
        r4n = coprime4p%p
        assert r4n
        if e4n==0:
            may_e4n = None
            may_n = None
        else:
            may_e4n = e4n
            may_n = coprime4p
        #
        _drop_prime_factor4n_(p)
        return n, may_n, may_e4n, r4n
    p2n_n_e_r = {}
    def _get_mod_(p, n, /):
        '-> (may_n, may_e4n, r4n)'
        n_, may_n, may_e4n, r4n = _get5cache_(lazy4get_mod_, p2n_n_e_r, p, n=n)
        if n is not n_:
            if not n < n_:
                raise 000
            del p2n_n_e_r[p]
            n_, may_n, may_e4n, r4n = _get5cache_(lazy4get_mod_, p2n_n_e_r, p, n=n)
        if n is not n_:
            raise 000
        return may_n, may_e4n, r4n
    lazy_prime_seq = prime_gen.get_or_mk_lazy_prime_seq_() # keep weakref
    _i4next_p4n = 0
    _lb_next_p4n = 1
    _handled_ps4n = set()
    def _drop_prime_factor4n_(p, /):
        nonlocal _i4next_p4n
        nonlocal _lb_next_p4n
        ls = lazy_prime_seq
        s = _handled_ps4n
        s.add(p)
        i = _i4next_p4n
        if p == ls[i]:
            #find next
            for i in count_(i+1):
                q = ls[i]
                if q not in s:
                    _i4next_p4n = i
                    _lb_next_p4n = floor_log2(q)
                    break

    def _get_floor_log2_possible_next_prime_factor4n_():
        return _lb_next_p4n


    def iter_prime_bases4pefect_kth_root_(k, /):
        if verbose:print(f'iter_prime_bases4pefect_kth_root_({k})')
        assert k&1
        # [k >= 3]
        # [k %2 == 1]
        # [k :: prime]
        for p in prime_gen:
            (gcd, may_inv_k) = _get_ginv_mod_(p-1, k)
            # ~O(lb_max_k*lb_max_p +lb_max_p**3)
            if not gcd == 1:
                assert may_inv_k is None
                continue
            if verbose:print(f'iter_prime_bases4pefect_kth_root_({k}) yield {p}')
            yield p
        # total ~O((lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n) #only output num_ps4rt < num_ps4n
    def _find_enough_prime_bases_(_k, _n, /):
        '-> (may_n, p2e4n, may (ps, Ms))'
        r'''[[[
        ######################
            '...+O((lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n)' #loop-total iter_prime_bases4pefect_kth_root_
            '...+O((lbN*lb_max_p)*num_ps4n)' #global-total _get_mod_
            '...+O(lb_max_p**2 *num_ps4rt<k>**2)' #loop-total build CRT moduli
        ######################
        '...+O((lbN*lb_max_p)*num_ps4n)' #global-total _get_mod_
        '...+O((lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n +(lb_max_p**2 *num_ps4rt<k>**2))'
            #per-call: _find_enough_prime_bases_:iter_prime_bases4pefect_kth_root_
            #per-call: _find_enough_prime_bases_:build CRT moduli

        #]]]'''#'''
        if verbose:n0 = _n
        if verbose:print(f'_find_enough_prime_bases_({_k}, {n0})')
        assert _k&1
        # [_k >= 3]
        # [_k %2 == 1]
        # [_k :: prime]
        # [lb_rt >= 1]
        # [_n >= 2]
        M = 1
        Ms = [M]
        ps = []
        p2e4n = {}
        lb_rt = floor_log2_kth_root_(_k, _n)
        if not lb_rt >= 1:
            return (None, p2e4n, None)
        # [lb_rt >= 1]
        for p in iter_prime_bases4pefect_kth_root_(_k):
            # [lb_rt >= 1]
            '...+O((lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n)' #loop-total iter_prime_bases4pefect_kth_root_
            may_n, may_e4n, r4n = _get_mod_(p, _n)
            '...+O((lbN*lb_max_p)*num_ps4n)' #global-total _get_mod_
            assert not r4n == 0
            if not may_n is None:
                assert may_n < _n
                # [new _n == old _n ///p**e4n]
                if verbose:print(f'_find_enough_prime_bases_({_k}, {n0}) : n:{_n}///{p}**{may_e4n}-->{may_n}')
                _n = may_n
                e4n = may_e4n
                p2e4n[p] = e4n
                assert e4n >= 1
                if not e4n % _k == 0:
                    return (may_n, p2e4n, None)
                lb_rt = floor_log2_kth_root_(_k, _n)
                if not lb_rt >= 1:
                    return (may_n, p2e4n, None)
                # [lb_rt >= 1]
                if floor_log2(M) > lb_rt:
                    # [floor_log2(Ms[-1]) > lb_rt]
                    break
            # [lb_rt >= 1]
            M *= p
            '...+O(lb_max_p**2 *num_ps4rt<k>**2)' #loop-total build CRT moduli
            Ms.append(M)
            ps.append(p)
            if verbose:print(f'_find_enough_prime_bases_({_k}, {n0}) : n:{_n}**II({p2e4n}) : new prime base {p}')
            if floor_log2(M) > lb_rt:
                # [floor_log2(Ms[-1]) > lb_rt]
                break
        # [lb_rt >= 1]
        # [floor_log2(Ms[-1]) > lb_rt]

        # !! [Ms[0] == 1]
        # [floor_log2(Ms[0]) == 0]
        # [floor_log2(Ms[0]) < lb_rt]
        # !! [floor_log2(Ms[-1]) > lb_rt]
        # [len(Ms) >= 2]
        while floor_log2(Ms[-2]) > lb_rt:
            # [floor_log2(Ms[-2]) > lb_rt]
            Ms.pop() #why? see:p2e4n
            # [floor_log2(Ms[-1]) > lb_rt]
        # [floor_log2(Ms[-1]) > lb_rt]
        # [floor_log2(Ms[-2]) <= lb_rt]
        # [len(Ms) >= 2]
        M = Ms[-1]
        del ps[len(Ms):]
        if verbose:print(f'_find_enough_prime_bases_({_k}, {n0}) : n:{_n}**II({p2e4n}) : prime bases {ps}')

        # postcondition:
            # [Ms[0] == 1]
            # [floor_log2(Ms[-2]) <= lb_rt]
            # [floor_log2(Ms[-1]) > lb_rt]
            # [II(ps[:i]) == Ms[i]]
            # [ps[i] :: prime]
            # [ps[i] < ps[i+1]]
            # [_n %ps[i] =!= 0]
            # [gcd(_k, ps[i]-1) == 1]
        return (may_n, p2e4n, (ps, Ms))
    def _detect_pefect_kth_root_(_k, _n, /):
        '-> (may_n, p2e4n, may rt)'
        r'''[[[
        ######################
        '...+O((lbN*lb_max_p)*num_ps4n)' #global-total _get_mod_
        '...+O((lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n +(lb_max_p**2 *num_ps4rt<k>**2))'
        '...+O(lb_max_p**2 *num_ps4rt<k>**2 + lb_max_p**3 *num_ps4rt<k>)'
        '...+O((lb_max_k*lb_max_p + lb_max_p**3)*num_ps4rt<k>)'
        '...+O(lb_max_p**2 *num_ps4rt<k>**3)'
        '...+O((lbN/k*lb_max_p + lb_max_k*lb_max_p + lb_max_p**3)*(num_ps4n-num_ps4rt<k>))'
        ######################
        '...+O((lbN*lb_max_p)*num_ps4n)' #global-total _get_mod_
        '...+O((lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n +((lbN/k*lb_max_p)*(num_ps4n-num_ps4rt<k>)) +(lb_max_p**2 *num_ps4rt<k>**3))'
            #per-call: _detect_pefect_kth_root_
        ######################
        #]]]'''#'''
        if verbose:n0 = _n
        if verbose:print(f'_detect_pefect_kth_root_({_k}, {n0})')
        # [_k >= 2]
        # [_k :: prime]
        # [n >= 2**_k >= 4]
        # [lb_rt >= 1]
        if _k == 2:
            _rt = floor_sqrt(_n)
            if _rt**2 == _n:
                return (None, {}, _rt)
            return (None, {}, None)
        if verbose:print(f'_detect_pefect_kth_root_({_k}, {n0}):odd prime k')
        # [_k >= 3]
        # [_k %2 == 1]
        may_n, p2e4n, m = _find_enough_prime_bases_(_k, _n)
        '...+O((lbN*lb_max_p)*num_ps4n)' #global-total _get_mod_
        '...+O((lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n +(lb_max_p**2 *num_ps4rt<k>**2))'
            #per-call: _find_enough_prime_bases_:iter_prime_bases4pefect_kth_root_
            #per-call: _find_enough_prime_bases_:build CRT moduli
        if m is None:
            return may_n, p2e4n, None
        if not may_n is None:
            assert may_n < _n
            # [n >= 2**_k >= 4]
            # [lb_rt >= 1]
            if verbose:print(f'_detect_pefect_kth_root_({_k}, {n0}):odd prime k: n:{_n}-->{may_n}')
            _n = may_n
        # [_k >= 2]
        # [n >= 2**_k >= 4]
        # [lb_rt >= 1]
        lb_rt = floor_log2_kth_root_(_k, _n)
        assert lb_rt >= 1
        assert _n >= 4
        assert _k >= 2

        (ps, Ms) = m
        coeff_pairs = mk_coeff_pairs4apply_raw_CRT__inc(ps, Ms)
        # ~O(sum (i*lb_max_p*lb_max_p +lb_max_p**3) {i :<- [0..<len ps]})
        # ~O(lb_max_p**2 *num_ps4rt**2 + lb_max_p**3 *num_ps4rt)
        '...+O(lb_max_p**2 *num_ps4rt<k>**2 + lb_max_p**3 *num_ps4rt<k>)'

        rs = []
        for p in ps:
            (may_n, may_e4n, r4n) = _get_mod_(p, _n) # %p
            '...+O(...)' #see:global total _get_mod_
            if not may_n is None:
                raise 000
            if not may_e4n is None:
                raise 000
            if r4n == 0:
                raise 000
            # [gcd(n, p) == 1]

            (gcd, may_inv_k) = _get_ginv_mod_(p-1, _k)
            '...+O(lb_max_k*lb_max_p)' #omit O(eval:inv(),gcd()) since cache exactly by iter_prime_bases4pefect_kth_root_; only EVAL(_k%(p-1))
            if not gcd == 1:
                raise 000
            # [gcd(k, p-1) == 1]
            if may_inv_k is None:
                raise 000
            inv_k = may_inv_k # %(p-1)
            r4n # == n %p
            inv_k # (1/k) %(p-1)
            # [rt**k == n]
            # [rt**k =[%p]= n]
            # [rt =[%p]= n**inv_k]
            # [rt =[%p]= (n%p)**inv_k]
            rt6p = _pow_(r4n, inv_k, p)
            '...+O(lb_max_p**3)'
            rs.append(rt6p)
        '...+O((lb_max_k*lb_max_p + lb_max_p**3)*num_ps4rt<k>)'
        _rt = apply_raw_CRT__inc(ps, Ms, coeff_pairs, rs)
        # ~O(sum (i*lb_max_p*i*lb_max_p) {i :<- [0..<len ps]})
        # ~O(lb_max_p**2 *num_ps4rt**3)
        '...+O(lb_max_p**2 *num_ps4rt<k>**3)'
        if verbose:print(f'_detect_pefect_kth_root_({_k}, {n0}):odd prime k: n:{_n}: rt=?={_rt}')
        if not floor_log2(_rt) == lb_rt:
            return may_n, p2e4n, None
        # !! [lb_rt >= 1]
        # [_rt >= 2]
        p_set = {*ps}
        remain_bits = ceil_log2(_n) -floor_log2(Ms[-1])
        extras = []
        ok = False
        for p in prime_gen:
            if p in p_set:
                continue
            if verbose:print(f'_detect_pefect_kth_root_({_k}, {n0}):odd prime k: n:{_n}: rt=?={_rt}: new prime base to confirm result: {p}')
            (may_n, may_e4n, r4n) = _get_mod_(p, _n) # %p
            '...+O(...)' #see:global total _get_mod_
            if not may_n is None:
                if verbose:print(f'_detect_pefect_kth_root_({_k}, {n0}):odd prime k: n:{_n}: rt=?={_rt}: new prime base to confirm result: {p}: found new prime factor')
                extras.append((p, may_n, may_e4n, r4n))
                r4n = 0
                pow_rt_k = _rt%p #not really the pow, but should be 0 if pass test
            else:
                r4n # %p
                pow_rt_k = _pow_(_rt%p, _k, p)
                '...+O(lbN/k*lb_max_p + lb_max_k*lb_max_p + lb_max_p**3)' # will eval (_k%(p-1))
            # eval (_rt%p) SHOULD NOT use _get_mod_() which cache for dec n's, not for arbitrary value _rt
            if not pow_rt_k == r4n:
                # [_rt**_k =!= _n]
                break #to handle "extras"
                return may_n, p2e4n, None
            remain_bits -= floor_log2(p)
            if remain_bits <= 0:
                # [_rt**_k == _n]
                ok = True
                break
        '...+O((lbN/k*lb_max_p + lb_max_k*lb_max_p + lb_max_p**3)*(num_ps4n-num_ps4rt<k>))'
        for (p, _may_n, _may_e4n, _r4n) in extras:
                # _may_e4n <<== since 『not ok』return may_n
            (may_n, may_e4n, r4n) = _get_mod_(p, _n) # %p
                # may_e4n <<== since 『not ok』return may_n
            if may_n is None:
                raise 000
            _n = may_n
            e4n = may_e4n
            p2e4n[p] = e4n
            assert e4n >= 1
            assert may_e4n == _may_e4n
            if not e4n % _k == 0:
                raise Exception(n, (p, _may_n, _may_e4n, _r4n), (may_n, may_e4n, r4n))
                    #Exception: (517, (11, 47, 1, 3), (47, 1, 3))
                raise 000
        if ok:
            for (p, _may_n, _may_e4n, _r4n) in extras:
                # _may_e4n <<== since 『not ok』return may_n
                e4n = _may_e4n
                _rt //= p**(e4n//_k)
            # [_rt**_k == _n]




        if not ok:
            return may_n, p2e4n, None
        # [_rt**_k == _n]
        # [_rt >= 2]
        return (may_n, p2e4n, _rt)

    def main():
        # mainmain():goto
        check_type_is(int, n)
        if not n >= 2:raise ValueError(n)
        # [n >= 2]
        if not n >= 4:
            return (n, 1)
        # [n >= 4]
        ######################


        if 0:
            _n = n
            # [_n >= 4]
            # [_n >= 2]
            p2e4n_ = {}
            may_p2e4gcd4e5n = None
            p2e4n_, _n, may_p2e4gcd4e5n
        else:
            # [_n >= 4]
            _2357 = (2,3,5,7)
            if 0:
                p2e4n_, _n = semi_factor_pint_via_trial_division(_2357, n)
                # [_n >= 1]
                for p in _2357:
                    _drop_prime_factor4n_(p)
            else:
                p2e4n_ = {}
                _n = n
                for p in _2357:
                    (may_n, may_e4n, r4n) = _get_mod_(p, _n) # %p
                    if may_n is not None:
                        _n = may_n
                        p2e4n_[p] = may_e4n
            p2e4n_, _n
            # [_n >= 1]
            may_p2e4gcd4e5n = None
            if p2e4n_:
                may_p2e4gcd4e5n = p2e4gcd4e5n = _update_p2e4gcd4e5n_(may_p2e4gcd4e5n, p2e4n_)
                iter_sorted_keys_of_p2e4gcd4e5n = iter(sorted(p2e4gcd4e5n))
            p2e4n_, _n, may_p2e4gcd4e5n
            #if _n == 1
        p2e4n_, _n, may_p2e4gcd4e5n
        # [_n >= 1]
        k_ = 1
        # [n0 == (II__p2e_(p2e4n_)*_n)**k_]
        it = iter(prime_gen)
        while 1:
            if may_p2e4gcd4e5n is None:
                _k = next(it)
            else:
                p2e4gcd4e5n
                if not p2e4gcd4e5n:
                    break
                #_k = next(iter_sorted_keys_of_p2e4gcd4e5n)
                _k = next(iter_sorted_keys_of_p2e4gcd4e5n, None)
                    # ?StopIteration
                if _k is None:raise Exception(n, (p2e4n_, _n, may_p2e4gcd4e5n), p2e4gcd4e5n)
                    #Exception: (639, ({3: 2}, 71, {2: 1}), {2: 1})
                #may_max_e4k = p2e4gcd4e5n[_k]
            _k

            # [n0 == (II__p2e_(p2e4n_)*_n)**k_]
            # [_n >= 1]
            lb_rt = floor_log2_kth_root_(_k, _n)
            # [lb_rt >= 0]
            if verbose:print(f'main():loop _k={_k}')
            if verbose:print(f'main():loop k_={k_}')
            if verbose:print(f'main():loop may_p2e4gcd4e5n={may_p2e4gcd4e5n}')
            if verbose:print(f'main():loop p2e4n_={p2e4n_}')

            while lb_rt >= _get_floor_log2_possible_next_prime_factor4n_() and (may_p2e4gcd4e5n is None or _k in p2e4gcd4e5n):
                # [lb_rt >= 1]
                # [_n >= 2]
                # [n0 == (II__p2e_(p2e4n_)*_n)**k_]
                (may_n, _p2e4n, may_rt) = _detect_pefect_kth_root_(_k, _n)
                '...+O((lbN*lb_max_p)*num_ps4n)' #global-total _get_mod_
                '...+O((lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n +((lbN/k*lb_max_p)*(num_ps4n-num_ps4rt<k>)) +(lb_max_p**2 *num_ps4rt<k>**3))'
                    #per-call: _detect_pefect_kth_root_
                ###################
                # global-total _get_mod_ ~O(lbN**2)
                # total loop except _get_mod_ ~O(lbN**3/lblbN)
                #   <<==:
                ###################
                # total loop except _get_mod_ ~O(sum (lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n +((lbN/k*lb_max_p)*(num_ps4n-num_ps4rt<k>)) +(lb_max_p**2 *num_ps4rt<k>**3) {prime k :<- [3..=max_k]})
                # ~O(sum {<= ?})
                # ??? [num_ps4rt<k> == O(lbN/k)] #lb_max_p???
                # [sum log2(i) {i :<- [2..=num_ps4rt<k>]} <= lbN/k]
                # [sum i*2**i {i :<- [1..=log2 num_ps4rt<k>]} <= (lbN/k)]
                # [D<x>(x*e**x -e**x) == x*e**x]
                # [log2(num_ps4rt<k>)*num_ps4rt<k> <= (lbN/k)]
                # [num_ps4rt<k> == O((lbN/k) /log2(lbN/k)) == O(lbN/k/lblbN)]
                # [num_ps4rt<k> == O(lbN/k/lblbN)]
                # [zzz := O(lbN/k/lblbN)]
                # ~O(sum (lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n +((lbN/k*lb_max_p)*(num_ps4n-zzz)) +(lb_max_p**2 *zzz**3) {prime k :<- [3..=max_k]})
                # ~O(sum (lb_max_k +lb_max_p**2 +lbN/k)*lb_max_p*num_ps4n +(lb_max_p**2 *(lbN/k/lblbN)**3) {prime k :<- [3..=max_k]})
                # [total k == O(max_k/lb_max_k)]
                # ~O((max_k +lb_max_p**2 *max_k/lb_max_k +lbN*lb_max_k)*lb_max_p*num_ps4n +(lb_max_p**2 *(lbN/lblbN)**3))
                # [lb_max_p == lbN/max_k]  #assume trial_division until max_p, i.e. [next_prime_factor4n > max_p]
                # [max_k == lbN/lb_max_p]
                # [lb_max_k == O(lblbN -lblb_max_p) == O(lblbN)]
                # [total k == O(max_k/lb_max_k) == O(lbN/lb_max_p/lblbN)]
                # ~O((lbN/lb_max_p +lb_max_p**2 *lbN/lb_max_p/lblbN +lbN*lblbN)*lb_max_p*num_ps4n +(lb_max_p**2 *(lbN/lblbN)**3))
                # !! [num_ps4rt<k> == O(lbN/k/lblbN)]
                # [num_ps4n == num_ps4rt<1> == O(lbN/lblbN)]
                # ~O((lbN/lb_max_p +lb_max_p**2 *lbN/lb_max_p/lblbN +lbN*lblbN)*lb_max_p*lbN/lblbN +(lb_max_p**2 *(lbN/lblbN)**3))
                # ~O((lb_max_p +lblbN**2)*lb_max_p*lbN**2/lblbN**2 +(lb_max_p**2 *(lbN/lblbN)**3))
                # !! [num_ps4n == O(lbN/lblbN)]
                # [max_p == O(num_ps4n*log2(num_ps4n)) == O(lbN/lblbN*log2(lbN/lblbN)) == O(lbN)]
                # [max_p == O(lbN)]
                # [lb_max_p == O(lblbN)]
                # [total k == O(lbN/lb_max_p/lblbN) == O(lbN/lblbN**2)]
                # ~O((lblbN +lblbN**2)*lblbN*lbN**2/lblbN**2 +(lblbN**2 *(lbN/lblbN)**3))
                # ~O(lbN**2*lblbN +lbN**3/lblbN)
                # ~O(lbN**2/lblbN*(lblbN**2 +lbN))
                # [log2(16)**2 == 16]
                # ~O(lbN**3/lblbN)
                ###################
                ###################
                #
                # global-total _get_mod_ ~O((lbN*lb_max_p)*num_ps4n)
                # !! [num_ps4n == O(lbN/lblbN)]
                # !! [lb_max_p == O(lblbN)]
                # ~O((lbN*lblbN)*(lbN/lblbN))
                # ~O(lbN**2)
                ###################
                # [may_rt is None]or[_rt >= 2]
                if not may_n is None:
                    assert may_n < _n
                    # [_n == II__p2e_(_p2e4n)*may_n]
                    if verbose:print(f'main():loop _k={_k}: _n:{_n}///II(_p2e4n)-->{may_n}')
                    _n = may_n
                    # [_n >= 1]
                    #if _n == 1: break
                    # [n0 == (II__p2e_(p2e4n_)*II__p2e_(_p2e4n)*_n)**k_]
                    may_p2e4gcd4e5n = p2e4gcd4e5n = _update_p2e4gcd4e5n_(may_p2e4gcd4e5n, _p2e4n)
                    iter_sorted_keys_of_p2e4gcd4e5n = iter(sorted(p2e4gcd4e5n))
                    _iadd_p2e4n_(p2e4n_, _p2e4n)
                    _p2e4n = None
                    # [n0 == (II__p2e_(p2e4n_)*_n)**k_]
                    if verbose:print(f'main():loop _k={_k}: _n:{_n}')
                    if verbose:print(f'main():loop k_={k_}')
                    if verbose:print(f'main():loop may_p2e4gcd4e5n={may_p2e4gcd4e5n}')
                    if verbose:print(f'main():loop p2e4n_={p2e4n_}')
                    lb_rt = floor_log2_kth_root_(_k, _n)
                    # [lb_rt >= 0]
                # [n0 == (II__p2e_(p2e4n_)*_n)**k_]
                # [lb_rt >= 0]
                if may_rt is None:
                    # [may_rt is None]
                    # [lb_rt >= 0]
                    break
                else:
                    # [_rt**_k == _n]
                    # [_rt >= 2]
                    _rt = may_rt
                # [_rt**_k == _n]
                # [_rt >= 2]
                _rt
                # !! [n0 == (II__p2e_(p2e4n_)*_n)**k_]
                # [n0 == (II__p2e_(p2e4n_)*_rt**_k)**k_]
                k_ *= _k
                p2e4n_ = _perfect_kth_root__p2e_(p2e4n_, _k)
                # [n0 == (II__p2e_(p2e4n_)*_rt)**k_]
                if not may_p2e4gcd4e5n is None:
                    p2e4gcd4e5n[_k] -= 1
                    if p2e4gcd4e5n[_k] == 0:
                        del p2e4gcd4e5n[_k]
                ######next round:
                _n = _rt
                # !! [n0 == (II__p2e_(p2e4n_)*_rt)**k_]
                # [n0 == (II__p2e_(p2e4n_)*_n)**k_]
                # !! [_rt >= 2]
                # [_n >= 2]
                lb_rt = floor_log2_kth_root_(_k, _n)
                # [lb_rt >= 0]
            else:
                # [[lb_rt < _get_floor_log2_possible_next_prime_factor4n_()] or not _k in may_p2e4gcd4e5n]
                pass
            lb_next_p = _get_floor_log2_possible_next_prime_factor4n_()
            if not lb_rt >= lb_next_p:
                break
        # [n0 == (II__p2e_(p2e4n_)*_n)**k_]
        # [_n >= 1]
        if 0:
            if n == 9:
                print((k_, p2e4n_, may_p2e4gcd4e5n, _n))
        if _n == 1:
            # !! [n0 >= 4]
            # [perfect kth root include all prime factors of n0:n0**(1/k) >= 2]
            # now be 1, all prime factors must be found and put into p2e4n_
            # [not$ may_p2e4gcd4e5n is None]
            if may_p2e4gcd4e5n is None:
                raise 000
            assert _update_p2e4gcd4e5n_(None, p2e4n_) == p2e4gcd4e5n
            if p2e4gcd4e5n:
                gcd4e5n = II__p2e_(p2e4gcd4e5n)
                k_ *= gcd4e5n
                p2e4n_ = _perfect_kth_root__p2e_(p2e4n_, gcd4e5n)
                p2e4gcd4e5n.clear()
                gcd4e5n = 1
        if 0:
            #bug:n0=257*3**23:
            assert not may_p2e4gcd4e5n, (k_, p2e4n_, may_p2e4gcd4e5n, _n)
                #AssertionError: (1, {3: 23}, {23: 1}, 257)
        assert (p2e4n_ and may_p2e4gcd4e5n is not None and not p2e4gcd4e5n) or (not floor_log2_kth_root_(_k, _n) >= _get_floor_log2_possible_next_prime_factor4n_())
        if k_ == 1:
            rt = n
            k = 1
        else:
            rt = II__p2e_(p2e4n_)*_n
            k = k_
        #assert rt**k == n
        return (rt, k)
    #end-def main():
    def _update_p2e4gcd4e5n_(may_p2e4gcd4e5n, _p2e4n, /):
        if may_p2e4gcd4e5n is None:
            if not _p2e4n:
                raise 000
            gcd4e5n = gcd_many(_p2e4n.values())
            p2e4gcd4e5n = _factor_small_pint_(gcd4e5n)
        else:
            p2e4gcd4e5n = may_p2e4gcd4e5n
            new = p2e4gcd4e5n
            for _, e in _p2e4n.items():
                (p2e4gcd, _) = semi_factor_pint_via_trial_division(new.keys(), e)
                new = {p:min(e, new[p]) for p, e in p2e4gcd.items()}
            p2e4gcd4e5n = new
        return p2e4gcd4e5n

    def _iadd_p2e4n_(p2e4n_, _p2e4n, /):
        for p, e in _p2e4n.items():
            p2e4n_.setdefault(p, 0)
            p2e4n_[p] += e

    def mainmain():
        rt, k = main()
        assert rt**k == n
        return (rt, k)
    return mainmain()









__all__
def __():
    #too slow, discard
    #begin-detect_pefect_kth_root_
    #_2357 = (2,3,5,7)
    _3_5_7 = (3,5,7)
    _II_3_5_7 = II(_3_5_7)

    #_2_3_5 = (2,3,5)
    _2_5_17 = (2,5,17)
    r'''[[[
    3, 5, 17 is Fermat_prime
        p-1 is 2**e
        [gcd(phi(p**2), odd_q) == gcd(p, odd_q) == p if [p==odd_q] else 1]
        [[not$ is_square_residual_mod_prime_(p;xx)] <-> [is_primitive_root_mod_(p;xx)]]
        [2**e =[%p]= -1]
        [order_mod_(p;2) == e+1]
    [is_least_primitive_root_mod_(17;3)]
    [not$ is_square_residual_mod_prime_(17;3)]
        easy to find
    >>> pow(2,4,17)
    16
    >>> pow(3,8,17)
    16

    why use 17 but not use 3?
    [ceil_log_(17; n**(1/k)) <= ceil_log_(16; n**(1/k)) == ceil_log2_kth_root_(4*k;n)]

    xxx [ceil_log_(3; n**(1/k)) <= ceil_log_(2; n**(1/k)) == ceil_log2_kth_root_(k;n)]
    [ceil_log_(3; n**(1/k)) == ceil_log_(9; n**(2/k)) <= ceil_log_(8; n**(2/k)) == ceil_log2_kth_root_(3*k;n**2) == ceil_div(ceil_log2(n**2), 3*k) <= ceil_div(2*ceil_log2(n), 3*k)]
    cf_log2_(3) = [1;1,1,2,2,3,1,5,2,23,2,2,1,1,...]
        view ../../python3_src/nn_ns/math_nn/numbers/A028507-continued_fraction_expansion_for_log_2_3__fst_10000.txt
    1,2/1,3/2,
    from seed.math.continued_fraction.continued_fraction_fold import *
    f,g = iter_continued_fraction_digits5ND_, iter_approximate_fractions5continued_fraction_
    g = iter_approximate_fraction_NDs5continued_fraction_
    for N,D in g([1,1,1,2,2,3,1,5,2,23,2,2,1,1]):print(f'{N}/{D}')
    1/1
    2/1
    3/2
    8/5
    19/12
    65/41
    84/53
    485/306
    1054/665
    24727/15601
    50508/31867
    125743/79335
    176251/111202
    301994/190537
    >>> 3**5
    243
    >>> 2**8
    256
    >>> 2**19
    524288
    >>> 3**12
    531441

    #]]]'''#'''
    from seed.tiny_.check import check_type_is# check_int_ge
    from seed.math.sqrts_mod_ import is_square_residual_mod_prime_# is_square_residual_mod_prime_power_
    from seed.math.sqrts_mod_ import iter_sqrts_mod_prime_power_# iter_sqrts_mod_prime_power__coprime__5one_sqrt_
    from seed.math.floor_ceil import floor_log2_kth_root_, ceil_log2_kth_root_
    from seed.math.floor_ceil import floor_log2# ceil_log2
    from seed.math.inv_mod_ex import inv_mod_power__coprime_
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_, factor_pint_out_2_powers
    from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
    from seed.math.factor_pint_by_trial_division_ import factor_pint_by_trial_division_ex_# default4upperbound4probably_prime, check_result5factor_pint_
    from seed.math.II import II
    from seed.math.gcd import gcd
    def detect_pefect_kth_root_(k, n, /, *, verbose):
        r'''[[[
        'k/int{>=1} -> n/int{>=2} -> may base/int{>=2}{n==base**k}'

        O(lbN**3 *(k///odd4k)/k**3 +lbN**2)
            too slow!!!
            worse than floor_kth_root_
                O(lbN**2 *lblbN)
        ######################
        '...+O(e2*(log2(n)/2**e2)**3 + log2(n)**2)'
        '...+O(log2(n)**3 /k**3 +log2(n)**2)'
        '...+O(log2(n)**2 /k**2)'
        ######################
        O(log2(n)**3 *(k///odd4k)/k**3 +log2(n)**2)
        #]]]'''#'''
        check_type_is(int, k)
        if not k > 0:raise ValueError(k)
        check_type_is(int, n)
        if not n >= 0:raise ValueError(n)
        # [k >= 1]
        # [n >= 0]

        if n < 2:
            return n
        # [n >= 2]

        if k == 1:
            return n
        # [k >= 2]
        n0 = n
        n = None


        lb_rt = floor_log2_kth_root_(n)
        # [lb_rt >= 0]
        if lb_rt == 0:
            return None
        # [lb_rt >= 1]

        if 1:
            (p2e, _n) = semi_factor_pint_via_trial_division(_2_5_17, n0)
            # [n%2 == 1]
            # [n%17 =!= 0]
            # [n%5 =!= 0]
            #   2,5,17 are required below
            #   3,7 is unimportant
            if not all(e%k == 0 for e in p2e.values()):
                return None
            #rt_ = II(p**(e//k) for p,e in p2e.items())
            r'''[[[
        else:
            (e4n, odd4n) = factor_pint_out_2_powers(n0)
            _n = odd4n
            # [n%2 == 1]
            if not e4n%k == 0:
                return None
            rt_ = 1 << (e4n//k)
            #]]]'''#'''
        #rt_
        _n
        # [rt_**k * _n == n0]
        # [n%2 == 1]
        # [n%17 =!= 0]
        # [n%5 =!= 0]



        if 0:
            (p2e, unfactored_part, may_next_prime_factor) = factor_pint_by_trial_division_ex_(k, may_upperbound4prime_factor=k+1)
            if not unfactored_part == 1:raise 000
            #II__p2e_(p2e)
        else:
            (e4k, odd4k) = factor_pint_out_2_powers(k)
        # [e4k >= 0]
        # [odd4k >= 1]
        # [odd4k%2 == 1]




        # [n >= 2]
        # [n%2 == 1]
        if e4k:
            # [e4k =!= 0]
            # !! [e4k >= 0]
            # [e4k >= 1]
            e2 = e4k
            # [e2 >= 1]
            # !! [n >= 2]
            # !! [n%2 == 1]
            m = _detect_pefect_kth_root__k_eq_2_power_(e2, _n, verbose=verbose)
            '...+O(e2*(log2(n)/2**e2)**3 + log2(n)**2)'
            if m is None:
                return None
            _n = m
            # [n >= 2]
            # [n%2 == 1]
        # [n >= 2]
        # [n%2 == 1]


        # [odd4k >= 1]
        if not odd4k == 1:
            # [odd4k >= 2]
            # !! [odd4k%2 == 1]
            # !! [n >= 2]
            # !! [n%17 =!= 0]
            # !! [n%5 =!= 0]

            m = _detect_pefect_kth_root__k_is_odd_(odd4k, _n, verbose=verbose)
            '...+O(log2(n)**3 /k**3  +log2(n)**2)'
            if m is None:
                return None
            _n = m
        _rt = _n

        '...+O(log2(n)**2 /k**2)'
        rt_ = II(p**(e//k) for p,e in p2e.items())
        rt = rt_ * _rt
        assert rt**k == n
        return rt
    def _detect_pefect_kth_root__k_is_odd_(k, n, /, *, verbose):
        'O(log2(n)**3 /k**3  +log2(n)**2)'
        assert k >= 2
        assert k&1 == 1
        assert n >= 2
        assert n %17
        assert n %5
        # [k >= 2]
        # [k%2 == 1]
        # [n >= 2]
        # [n%17 =!= 0]
        # [n%5 =!= 0]


        # !! [k%2 == 1]
        # [?p. [p is odd prime][gcd(p-1,k)==1]]
        # [?p. [p is odd prime][gcd((p-1)*p,k)==1]]
        # [?p. [p is odd prime][gcd(phi(p**j),k)==1]]

        e17, _17coprime = factor_pint_out_power_of_base_(17, k)
        # [_17coprime**e17 * _17coprime == k]
        # [e17 >= 0]
        # [_17coprime %17 =!= 0]

        # !! [k%2 == 1]
        # [_17coprime %2 =!= 0]
        # [gcd(_17coprime, 2*17) == 1]
        _17pows = 17**e17
        # [_17pows * _17coprime == k]
        # [gcd(_17pows, phi(5**2)) == 1]
        # [gcd(_17coprime, phi(17**2)) == 1]

        if 0:
            assert _17pows * _17coprime == k
            p = 17
            assert gcd((p-1)*p, _17coprime) == 1
            p = 5
            assert gcd((p-1)*p, _17pows) == 1

        _n = n
        k_p_e_pairs = [(_17pows, 5, 2), (_17coprime, 17, 4)]
        for _k, p, e in k_p_e_pairs:
            # !! [n%17 =!= 0]
            # !! [n%5 =!= 0]
            # !! [p <- [17,5]]
            # [n%p =!= 0]

            if _k == 1:
                continue
            # [_k >= 2]
            # [ceil_log_(5; n**(1/k)) <= ceil_log_(4; n**(1/k)) == ceil_log2_kth_root_(2*k;n)]
            # [ceil_log_(17; n**(1/k)) <= ceil_log_(16; n**(1/k)) == ceil_log2_kth_root_(4*k;n)]

            lb_rt = floor_log2_kth_root_(_k, _n)
            kk = ceil_log2_kth_root_(e*_k, _n)
            # [kk >= 1]
            if 1:
            #with _timer(prefix=f'kth_root_mod_({p}**{kk}, {_k}, {_n})', _show_hint_on_enter_=True, _to_show_=verbose):
                # !! [gcd(_17pows, phi(5**2)) == 1]
                # !! [gcd(_17coprime, phi(17**2)) == 1]
                # !! [p <- [17,5]]
                # !! [k <- [_17coprime,_17pows]]
                # [gcd(_k, phi(p**2)) == 1]
                # [_rt**_k == _n]
                # [_rt**_k =[%p**kk]= _n]
                # [_rt**(_k%((p-1)*p**(kk-1))) =[%p**kk]= _n]
                # [_rt =[%p**kk]= _n**inv_mod_(((p-1)*p**(kk-1));_k)]
                p_kkmm = p**(kk-1)
                phi_p_kk = (p-1)*p_kkmm
                p_kk = p_kkmm*p

                _inv_k = inv_mod_power__coprime_(phi_p_kk, _k)
                _rt = pow(_n, _inv_k, p_kk)
                    # ???is this fast???
                    # cmp: n**(1/k) vs _n**_inv_k%p**kk
                    # [O(EVAL(_n**_inv_k%p**kk)) == O(log2(p**kk)**3) == O(log2(_n**(1/_k))**3) == O(log2(_n)**3 /_k**3)]
                '...+O(log2(n)**3 /k**3)'
                if not floor_log2(_rt) == lb_rt:
                    return None
            #next round:
            _n = _rt
        _rt = _n
        n, k


        # [O(EVAL(_rt**k)) == O(sum (2**i *log2(_rt))**2 {i :<- [1..=log2(k)]}) == O(k**2 *log2(_rt)**2) == O(k**2 *log2(n**(1/k))**2) == log2(n)**2]
        '...+O(log2(n)**2)'
        if not _rt**k == n:
            # [_rt =!= rt]
            return None
        rt = _rt
        # [rt**k == n]
        # !! [n >= 2]
        # [rt >= 2]
        return rt
    def _detect_pefect_kth_root__k_eq_2_power_(e2, n, /, *, verbose):
        'O(e2*(log2(n)/2**e2)**3 + log2(n)**2)'
        assert e2 >= 1
        assert n >= 2
        assert n&1 == 1
        # [n%2 == 1]
        if n < 9:
            # !! [n%2 == 1]
            # !! [2 <= n < 9]
            # [n <- {3,5,7}]
            # [k == 2**e2 >= 2]
            # !! [rt**2 == n][rt %1 ==0]
            # [rt <- {}]
            #
            #xxx if (e2,n) == (1,4): return 2
            return None
        # [n >= 9]
        n__357 = n%_II_3_5_7
        for p in _3_5_7:
            if not is_square_residual_mod_prime_(p, n__357):
                return None

        lb_n = floor_log2(n)
        k = 1<<e2
        lb_rt = lb_n//k
        if lb_rt == 0:
            return None
        assert lb_rt >= 1
        # [lb_rt >= 1]

        p = 2
        kk = lb_rt+2
        # !! [lb_rt >= 1]
        # [kk >= 3]
        # [is_square_residual_mod_prime_power_(p, kk, xx) === [xx%8 == 1]]
        #
        if 1:
        #with _timer(prefix=f'sqrts_mod_(2**{kk};{n})', _show_hint_on_enter_=True, _to_show_=verbose):
            # !! [n%2 == 1]
            p_kk = 1<<kk
            _n__p_kk = n&(p_kk-1)
            ls = [_n__p_kk]
            for _ in range(e2):
                #if not ls: return None
                [_n__p_kk] = ls
                [_rt, neg_rt] = [*iter_sqrts_mod_prime_power_(p, kk, _n__p_kk)]
                # !! [_n %2 == 1]
                # [num_sqrts == O(1)]
                # !! [p == 2]
                # [neednot search sqrt%2]
                # !! iter_sqrts_mod_prime_power_ ~ O((k**3 + log2(p) + log2(p///odd4p)**(3/2))*log2(p)**2 +find_arbitrary_one_square_nonresidual_mod_odd_prime_ + num_sqrts)
                # ~O(kk**3)
                # ~O((log2(n)/2**e2)**3)
                '...+O((log2(n)/2**e2)**3)'
                assert floor_log2(neg_rt) == kk-1
                # [floor_log2(neg_rt) == kk-1 == lb_rt+1]
                # !! [is_square_residual_mod_prime_power_(p, kk, xx) === [xx%8 == 1]]
                ls = [x for x in [_rt, neg_rt] if (_rt&7) == 1]
                if not len(ls) == 1: raise 000
            #end-for _ in range(e2):
            '...+O(e2*(log2(n)/2**e2)**3)'
                #total4loop

            # !! [floor_log2(neg_rt) == kk-1 == lb_rt+1]
            # [neg_rt =!= rt]
            if not floor_log2(_rt) == lb_rt:
                # [_rt =!= rt]
                return None

            # [O(EVAL(_rt**k)) == O(sum (2**i *log2(_rt))**2 {i :<- [1..=log2(k)]}) == O(k**2 *log2(_rt)**2) == O(k**2 *log2(n**(1/k))**2) == log2(n)**2]
            '...+O(log2(n)**2)'
            if not _rt**k == n:
                # [_rt =!= rt]
                return None
            rt = _rt
        # [rt**2 == n]
        # !! [n >= 2]
        # [rt >= 2]
        return rt
    #end-detect_pefect_kth_root_

__all__
def __():
    # floor_kth_root_-ver
    from seed.for_libs.for_time import (
    Timer__print_err
        ,timer__print_err__thread_wide
        ,timer__print_err__process_wide
        ,timer__print_err__system_wide__highest_resolution
        ,timer__print_err__system_wide__monotonic
    )
    if 1:
        _timer = timer__print_err__thread_wide
        #with _timer(prefix=, _fmt_=, _show_hint_on_enter_=True, _to_show_=verbose):

    from math import sqrt as sqrt_, isqrt as isqrt_
    from seed.math.Jacobi_symbol import Jacobi_symbol
    from seed.math.prime_gens import prime_gen

    from seed.tiny import print_err
    from seed.tiny import check_type_is
    from seed.math.II import II, II_mod
    from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division


    from seed.math.gcd import gcd#, gcd_many, are_coprime
    from seed.math.floor_ceil import floor_sqrt, ceil_sqrt
    from seed.math.floor_ceil import floor_kth_root_, ceil_kth_root_
    from seed.math.floor_ceil import floor_log_, floor_log2



    def factor_pint_as_pefect_power_(n, /, *, verbose):
        'n/int{>=2} -> (base/int{>=2}, exp/int{>=1}){n==base**exp}'
        check_type_is(int, n)
        if not n > 1:raise ValueError(n)
        n0 = n
        L = n.bit_length()
        e = 1
        assert 1 < n < (1<<L)
        # [1 < n < (1<<L)]
        for p in prime_gen:
            # [1 < n < (1<<L)]
            if p >= L:
                # [2**p >= 2**L > n]
                break
            # [2**p < 2**L]
            while 1:
                # [1 < n < (1<<L)]
                may_kth_root = detect_pefect_kth_root_(p, n, verbose=verbose)
                if may_kth_root is None:
                    break
                kth_root = may_kth_root
                assert 1 < kth_root < n
                e *= p
                n = kth_root
                L = n.bit_length()
                assert 1 < n < (1<<L)
                # [1 < n < (1<<L)]
        base = n
        exp = e
        n = n0
        assert n == base**exp
        return (base, exp)


    def detect_pefect_kth_root_(k, n, /, *, verbose):
        'k/int{>=1} -> n/int{>=2} -> may base/int{>=2}{n==base**k}'
        check_type_is(int, n)
        if not n > 1:raise ValueError(k)
        check_type_is(int, k)
        if not k > 0:raise ValueError(n)
        if k == 1:
            _kth_root = n
        elif k == 2:
            # now: math.isqrt
            with _timer(prefix=f'floor_sqrt({n})', _show_hint_on_enter_=True, _to_show_=verbose):
                sqrt_ = floor_sqrt(n)
            _kth_root = sqrt_
        else:
            #if 1:
            with _timer(prefix=f'floor_kth_root_({k}, {n})', _show_hint_on_enter_=True, _to_show_=verbose):
                _kth_root = floor_kth_root_(k, n)
        if _kth_root**k == n:
            return _kth_root
        return None


if __name__ == "__main__":
    pass
__all__


from seed.math.factor_pint_as_pefect_power_ import factor_pint_as_pefect_power_
from seed.math.factor_pint_as_pefect_power_ import is_kth_power_, is_square_, is_cube_
from seed.math.factor_pint_as_pefect_power_ import may_perfect_kth_root_, may_perfect_sqrt_, may_perfect_cbrt_
from seed.math.factor_pint_as_pefect_power_ import *
