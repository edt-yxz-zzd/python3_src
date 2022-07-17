

r'''[[[[[
e ../../python3_src/nn_ns/math_nn/numbers/Mersenne_exponents.py
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
#]]]]]'''

__all__ = '''
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

def int2imay_pseudo_Mersenne_exponent(i, /):
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
