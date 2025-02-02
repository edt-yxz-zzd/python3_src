#__all__:goto

r'''[[[[[
命名有误，应当是:exponents4Mersenne_prime
    Mersenne_prime |<| Mersenne_number

e ../../python3_src/nn_ns/math_nn/numbers/exponents4Mersenne_prime.py

e ../../python3_src/nn_ns/math_nn/numbers/Mersenne_exponents.py
py -m nn_ns.math_nn.numbers.Mersenne_exponents
py -m nn_ns.app.debug_cmd   nn_ns.math_nn.numbers.Mersenne_exponents -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.math_nn.numbers.Mersenne_exponents:__doc__ -ht # -ff -df

from nn_ns.math_nn.numbers.Mersenne_exponents import is_Mersenne_number_
from nn_ns.math_nn.numbers.Mersenne_exponents import is_Mersenne_prime_

from nn_ns.math_nn.numbers.Mersenne_exponents import Mersenne_exponents, Mersenne_exponents__stable, Mersenne_exponents__unstable
from nn_ns.math_nn.numbers.Mersenne_exponents import known_Mersenne_exponent_set, is_known_Mersenne_exponent, is_Mersenne_exponent__Lucas_Lehmer_test
from nn_ns.math_nn.numbers.Mersenne_exponents import is_known_not_Mersenne_exponent
from nn_ns.math_nn.numbers.Mersenne_exponents import is_known_Mersenne_prime, is_Mersenne_prime__Lucas_Lehmer_test, int2imay_pseudo_Mersenne_exponent
from nn_ns.math_nn.numbers.Mersenne_exponents import Mersenne_exponents__stable_48, Mersenne_exponents__unstable_48_51


Mersenne exponent <-> even perfect number
    let p be a Mersenne exponent
    then even perfect number = (2^p-1)*2^(p-1)

A000043
    Mersenne exponents: primes p such that 2^p - 1 is prime. Then 2^p - 1 is called a Mersenne prime.
    (Formerly M0672 N0248)
    2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457, 32582657, 37156667

A000396
    Perfect numbers n: n is equal to the sum of the proper divisors of n.
    (Formerly M4186 N1744)
    6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128, 2658455991569831744654692615953842176, 191561942608236107294793378084303638130997321548169216




[[20220704
[2,3,5,7,13,17,19,31,61,89,107,127,521,607,1279,2203,2281,3217,4253,4423,9689,9941,11213,19937,21701,23209,44497,86243,110503,132049,216091,756839,859433,1257787,1398269,2976221,3021377,6972593,13466917,20996011,24036583,25964951,30402457,32582657,37156667,42643801,43112609,57885161        ,74207281,77232917,82589933]
  #前48个位置固定，此后 可能有 新增的
https://primes.utm.edu/mersenne/
https://www.mersenne.org/primes/
List of Known Mersenne Prime Numbers
#只保留了 指数:P --> 2^p-1
[
1:2
2:3
3:5
4:7
5:13
6:17
7:19
8:31
9:61
10:89
11:107
12:127
13:521
14:607
15:1279
16:2203
17:2281
18:3217
19:4253
20:4423
21:9689
22:9941
23:11213
24:19937
25:21701
26:23209
27:44497
28:86243
29:110503
30:132049
31:216091
32:756839
33:859433
34:1257787
35:1398269
36:2976221
37:3021377
38:6972593
39:13466917
40:20996011
41:24036583
42:25964951
43:30402457
44:32582657
45:37156667
46:42643801
47:43112609
48:57885161
* Provisional ranking, not all candidates between M[57885161] and M[82589933] have been eliminated
-49*:74207281
-50*:77232917
-51*:82589933
]

These sites may provide additional details on the list of known Mersenne Prime Numbers:
  http://primes.utm.edu/mersenne/#known
  http://www.isthe.com/chongo/tech/math/prime/mersenne.html
  http://en.wikipedia.org/wiki/Mersenne_prime#List_of_known_Mersenne_primes
]]

>>> sorted(common__known_Mersenne_exponent_set__known_Mersenne_prime_set)
[3, 7, 31, 127]

[[
copy from:
    view others/数学/不可约多项式/找冫超长本原不可约多项式.txt
===
view /storage/emulated/0/0my_files/book/math/fxtbook[Matters Computational][Algorithms for Programmers].pdf

[f(x) :: binary_polynomial]:
  [Q(f;x) =[def]= sum [c*x**(2**k-1) | [c*x**k :<- all_terms_of(f(x))]]]
[[p(x) :: irreducible_binary_polynomial] -> [q(x) :<- all_irreducible_factors_of(Q(p;x))] -> [deg(q(x)) == order_mod(p(x);x)]]
!! [[p(x) :: primitive_irreducible_binary_polynomial] -> [(2**deg(p(x))-1) == order_mod(p(x);x)]]
!! [[p(x) :: binary_polynomial] -> [deg(Q(p;x)) == (2**deg(p(x))-1)]]
[[p(x) :: primitive_irreducible_binary_polynomial] -> [is_irreducible_binary_polynomial_(Q(p;x))]]

[[p(x) :: irreducible_binary_polynomial] -> [[is_primitive_irreducible_binary_polynomial_(p(x))] <-> [(2**deg(p(x))-1) == order_mod(p(x);x)]]]
[[q(x) :: irreducible_binary_polynomial] -> [is_prime_(2**deg(q(x))-1)] -> [is_primitive_irreducible_binary_polynomial_(q(x))]]

!! [[is_Mersenne_exponent_(d)] <-> [is_Mersenne_prime_(2**d-1)] <-> [is_prime_(2**d-1)]]
[[p(x) :: primitive_irreducible_binary_polynomial] -> [is_Mersenne_exponent_(deg(p(x)))] -> [is_primitive_irreducible_binary_polynomial_(Q(p;x))]]
  也就是 要找出一个 次数为梅森素数的本原不可约多项式，可以先 找出一个 次数为梅森指数的本原不可约多项式
  比如:
    要:找出一个 次数为梅森素数(2**127-1)的本原不可约多项式
    转化为:找出一个 次数为梅森指数127的本原不可约多项式
        等价于:找出一个 次数为梅森素数(2**7-1)的本原不可约多项式
    转化为:找出一个 次数为梅森指数7的本原不可约多项式
        等价于:找出一个 次数为梅森素数(2**3-1)的本原不可约多项式
    转化为:找出一个 次数为梅森指数3的本原不可约多项式
    (x**3+x**1+x**0)
    --> (x**(2**3-1)+x**(2**1-1)+x**(2**0-1))
    == (x**7+x**1+x**0)
    --> (x**(2**7-1)+x**(2**1-1)+x**(2**0-1))
    == (x**127+x**1+x**0)
    --> (x**(2**127-1)+x**(2**1-1)+x**(2**0-1))
    == (x**170141183460469231731687303715884105727+x**1+x**0)
]]

>>> for e in Mersenne_exponents__unstable: print(e, e.bit_length(), sep=':')
2:2
3:2
5:3
7:3
13:4
17:5
19:5
31:5
61:6
89:7
107:7
127:7
521:10
607:10
1279:11
2203:12
2281:12
3217:12
4253:13
4423:13
9689:14
9941:14
11213:14
19937:15
21701:15
23209:15
44497:16
86243:17
110503:17
132049:18
216091:18
756839:20
859433:20
1257787:21
1398269:21
2976221:22
3021377:22
6972593:23
13466917:24
20996011:25
24036583:25
25964951:25
30402457:25
32582657:25
37156667:26
42643801:26
43112609:26
57885161:26
74207281:27
77232917:27
82589933:27



>>> (_1__is_Mersenne_number_ is not _2__is_Mersenne_number_ is is_Mersenne_number_)
True
>>> all(_1__is_Mersenne_number_(i) is _2__is_Mersenne_number_(i) for i in range(-3, 300))
True

#]]]]]'''

__all__ = '''
is_known_Mersenne_prime_
    common__known_Mersenne_exponent_set__known_Mersenne_prime_set
is_Mersenne_number_

Mersenne_exponents
    Mersenne_exponents__stable
    Mersenne_exponents__unstable

    Mersenne_exponents__stable_48
    Mersenne_exponents__unstable_48_51

    known_Mersenne_exponent_set
    is_known_Mersenne_exponent
    is_Mersenne_exponent__Lucas_Lehmer_test

    is_known_not_Mersenne_exponent

    is_known_Mersenne_prime
    is_Mersenne_prime__Lucas_Lehmer_test

    int2imay_pseudo_Mersenne_exponent

    '''.split()

if 0:
    Mersenne_exponents = (
        2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457, 32582657, 37156667
        )

    #rint(len(Mersenne_exponents))
    assert len(Mersenne_exponents) == 45

Mersenne_exponents__unstable_48_51 = \
(2,3,5,7,13,17,19,31,61,89,107,127,521,607,1279,2203,2281,3217,4253,4423,9689,9941,11213,19937,21701,23209,44497,86243,110503,132049,216091,756839,859433,1257787,1398269,2976221,3021377,6972593,13466917,20996011,24036583,25964951,30402457,32582657,37156667,42643801,43112609,57885161        ,74207281,77232917,82589933)
assert len(Mersenne_exponents__unstable_48_51) == 51


Mersenne_exponents__stable_48 = Mersenne_exponents__unstable_48_51[:48]
assert len(Mersenne_exponents__stable_48) == 48
assert Mersenne_exponents__stable_48[-1] == Mersenne_exponents__stable_48[47] == 57885161

Mersenne_exponents__stable = Mersenne_exponents__stable_48
Mersenne_exponents__unstable = Mersenne_exponents__unstable_48_51

Mersenne_exponents = Mersenne_exponents__stable

#known_Mersenne_exponent_set = {*Mersenne_exponents__unstable}
known_Mersenne_exponent_set = frozenset(Mersenne_exponents__unstable)
def is_known_Mersenne_exponent(n, /):
    return n in known_Mersenne_exponent_set
def is_known_not_Mersenne_exponent(n, /):
    if n in known_Mersenne_exponent_set:
        # known Mersenne_exponents
        return False
    if not n <= Mersenne_exponents__stable[-1]:
        # unknown yet
        return False
    return  True


def is_known_Mersenne_prime(m, /):
    return _is_Mersenne_prime(is_known_Mersenne_exponent, m)
def is_Mersenne_prime__Lucas_Lehmer_test(m, /):
    return _is_Mersenne_prime(is_Mersenne_exponent__Lucas_Lehmer_test, m)

def is_Mersenne_number_(u, /):
    # @20250130
    return u > 0 and u.bit_length() == u.bit_count()
_2__is_Mersenne_number_ = is_Mersenne_number_
def _1__is_Mersenne_number_(u, /):
    # @20250119
    return u > 0 and (u&(u+1)) == 0
def is_known_Mersenne_prime_(u, /):
    # @20250130
    return u > 0 and (L:=u.bit_length()) == u.bit_count() and L in known_Mersenne_exponent_set
    # @20250119
    return u > 0 and (u&(u+1)) == 0 and u.bit_length() in known_Mersenne_exponent_set
    return int2imay_pseudo_Mersenne_exponent(u) in known_Mersenne_exponent_set
common__known_Mersenne_exponent_set__known_Mersenne_prime_set = set(filter(is_known_Mersenne_prime_, known_Mersenne_exponent_set))
#if __name__ == "__main__": print(sorted(common__known_Mersenne_exponent_set__known_Mersenne_prime_set))
assert [3, 7, 31, 127] == (__:=sorted(common__known_Mersenne_exponent_set__known_Mersenne_prime_set)), __

def int2imay_pseudo_Mersenne_exponent(u, /):
    return u.bit_length() if u > 0 and (u&(u+1)) == 0 else -1
def __old_int2imay_pseudo_Mersenne_exponent(i, /):
    if i < 1: return -1
    assert i >= 1
    k1 = i.bit_length()
    assert k1 >= 1 # == k+1 ==>> k>=0
    pow_2_k1 = 1 << k1
    pow_2_k = pow_2_k1 >> 1
    assert 1 <= pow_2_k <= i < pow_2_k1
    imay_pseudo_Mersenne_exponent = k1 if (i == pow_2_k1 - 1) else -1
    return imay_pseudo_Mersenne_exponent

def _is_Mersenne_prime(_is_Mersenne_exponent, m, /):
    if not m >= 1: raise ValueError
    imay = int2imay_pseudo_Mersenne_exponent(m)
    if imay == -1:
        return False

    e = imay
    return  _is_Mersenne_exponent(e)


#[[[
#https://rosettacode.org/wiki/Lucas-Lehmer_test#Python
def _():
  def isqrt(n, /):
    if n < 0:
        raise ValueError
    elif n < 2:
        return n
    else:
        a = 1 << ((1 + n.bit_length()) >> 1)
        while True:
            b = (a + n // a) >> 1
                #牛顿迭代？
            if b >= a:
                return a
            a = b

  def isprime(n, /):
    if n < 5:
        return n == 2 or n == 3
    elif n%2 == 0:
        return False
    else:
        r = isqrt(n)
        k = 3
        while k <= r:
            if n%k == 0:
                return False
            k += 2
        return True

  def lucas_lehmer_fast(n, /):
    if n == 2:
        return True
    elif not isprime(n):
        return False
    else:
        m = 2**n - 1
        s = 4
        for i in range(2, n):
            # s := (s*s-2)%m
            # s == s%m < m < 2**n
            # ss = s*s < m**2 < 2**(2n)
            # ss == q*(2**n -1) + r == q*2**n + (r-q) = (q-1)*2**n +(2**n -(q-r))
            # 0 <= q = ss//m <= ss/m < s < m
            # 0 <= r < m
            # -m < r-q < m
            # [r >= q]: [q==ss//2**n][r==ss%2**n +q==ss%2**n +ss//2**n]
            # [r < q]:  [q==ss//2**n +1][r==ss%2**n+q -2**n==ss%2**n+(ss//2**n +1) -2**n==ss%2**n +ss//2**n -m]
            # ss&m == ss%2**n
            # ss>>n == ss//2**n
            # r_ = ss%2**n +ss//2**n
            # r = r_ -m if r_ > m else r_
            #
            sqr = s*s
            s = (sqr & m) + (sqr >> n)
            if s >= m:
                s -= m
            s -= 2
            #但实际实现却是 s := s*s%m -2
            # s <- [-2..=m-3] not [0..=m-1]
            # 反正 最后 检查 s==0 而 中间 模m >= 2**3-1 == 7 > 4 == |-2|**2，无伤大雅
        return s == 0
  def is_Mersenne_exponent__Lucas_Lehmer_test(n, /):
      #if n < 0 # lucas_lehmer_fast--isprime --> False
      return lucas_lehmer_fast(n)
  return is_Mersenne_exponent__Lucas_Lehmer_test
  return lucas_lehmer_fast
is_Mersenne_exponent__Lucas_Lehmer_test = _()
#]]]
