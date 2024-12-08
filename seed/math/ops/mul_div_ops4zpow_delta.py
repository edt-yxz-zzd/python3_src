#__all__:goto
r'''[[[
e ../../python3_src/seed/math/ops/mul_div_ops4zpow_delta.py
view ../../python3_src/nn_ns/math_nn/numbers/Mersenne_exponents.py
view script/is_prime_zpow_plus1_div3.py



seed.math.ops.mul_div_ops4zpow_delta
py -m nn_ns.app.debug_cmd   seed.math.ops.mul_div_ops4zpow_delta -x
py -m nn_ns.app.doctest_cmd seed.math.ops.mul_div_ops4zpow_delta:__doc__ -ht

py -m nn_ns.app.doctest_cmd seed.math.ops.mul_div_ops4zpow_delta:__doc__ -ht     >  /sdcard/0my_files/tmp/0tmp      2>&1
view /sdcard/0my_files/tmp/0tmp


view ../lots/NOTE/char/数学符号.txt
    远小于？翻译:much less than

[[
cases:
    case__zpow
    case__delta
    case__coeff
    case__factor

    #case__zpow: [(?, ?) == N /% (2**e)]
    #case__delta: [(?, ?) == N /% (D + dD)]
    #case__coeff: [(?, ?) == N /% (k*D)]
    #case__factor: [(?, ?) == N /% (D///k)]
]]
[[
#case__zpow: [(?, ?) == N /% (2**e)]
    # eg. (2**127)
let [(q, r) := N /% (2**e)]
[q == N >> e]
[r == N & (2**e-1)]
]]
# below maybe [[D==2**e][dD<~<D]]  #??[k<~<D]
#   (<~<):much less than#远小于
[[
#case__delta: [(?, ?) == N /% (D + dD)]
    # eg. (2**127-1)
    view ../../python3_src/nn_ns/math_nn/numbers/Mersenne_exponents.py

let [(q, r) := N /% (D + dD)]
let [(q_, r_) := N /% D]
let [dq := q -q_]
[q == q_+dq]
[q*(D + dD) +r == N == q_*D +r_]
[(q_+dq)*(D + dD) +r == q_*D +r_]
[dq*(D + dD) +r == -q_*dD +r_]
[(dq, r) == (-q_*dD +r_)/%(D + dD)]
# (q, r) ~ (dq, r) ~ (q_, r_)
[fast_enough]:
    [abs(-q_*dD +r_) ~< D]
    [abs(q_*dD) ~< D]
    [abs(N/D*dD) ~< D]
    [abs(N*dD) ~< D*D]
    [abs(N) ~< D*D]
    [pN ~< sqD]
        assume cut L into pairwise...
        Otherwise cause O(L**2)

]]
[[
#case__coeff: [(?, ?) == N /% (k*D)]
    # eg. (3*2**127)
let [(q, r) := N /% (k*D)]
let [(_N, _R) := N /% D]
let [(_q, _r) := _N /% k]
[q*k*D +r == N]
[_N*D +_R == N]
[_q*k +_r == _N]
[(_q*k +_r)*D +_R == N == q*k*D +r]
[_q*k*D +(_r*D +_R) == q*k*D +r]

[q == _q]
[r == _r*D +_R]
# (q, r) ~ (_q, _r, _R)
]]
[[
#case__factor: [(?, ?) == N /% (D///k)]
    # eg. (2**127+1)///3
    view script/is_prime_zpow_plus1_div3.py

let [(q, r) := N /% (D///k)]
let [(_q, _r) := (k*N) /% D]
[q*D///k +r == N]
[_q*D +_r == k*N]
[q*D +r*k == k*N == _q*D +_r]
[q == (k*N //D) == _q]
[q == _q]
[r == _r///k]
# (q, r) ~ (_q, _r)

]]



==>>:
[[
[zpow_delta == (2**e+delta)]
[e >= 1]
[delta %2 == 1]
[1 <= delta <~< 2**e]

[mul<zpow_delta>(n) =[def]= n*zpow_delta]
[floor_div<zpow_delta>(n) =[def]= n//zpow_delta]
[divmod<zpow_delta>(n) =[def]= n/%zpow_delta = (n//zpow_delta, n%zpow_delta)]

case__zpow&case__delta

]]
[[
generalized:
[g_zpow_delta == ((k*2**e+delta)*2**c)]
[k >= 1]
[e >= 1]
[c >= 0]
[delta %2 == 1]
[1 <= delta <~< 2**e]

[mul<g_zpow_delta>(n) =[def]= n*g_zpow_delta]
[floor_div<g_zpow_delta>(n) =[def]= n//g_zpow_delta]
[divmod<g_zpow_delta>(n) =[def]= n/%g_zpow_delta]


case__coeff&case__zpow&case__delta&case__coeff

]]



[[
useless:it seems cache result...
    1000_vs_1000:goto
        only little improve
<<==:
repeat(stmt='pass', setup='pass', timer=<built-in function perf_counter>, repeat=5, number=1000000, globals=None)
timeit(stmt='pass', setup='pass', timer=<built-in function perf_counter>, number=1000000, globals=None)

>>> import timeit

>>> m4 = MulDivOps4case__zpow.from_exponent(100_00) # 2**10000
>>> m47 = MulDivOps4case__delta.from_offset_delta(m4, 7) # 2**10000 +7
>>> m34 = MulDivOps4case__coeff.from_coeff_base(3, m4) # 3*2**10000
>>> m347 = MulDivOps4case__delta.from_offset_delta(m34, 7) # 3*2**10000 +7

#bug:>>> m413 = MulDivOps4case__factor.from_base_factor(m4+5, 3) # (2**10000+5)///3
>>> m413 = MulDivOps4case__factor.from_base_factor(MulDivOps4case__delta.from_offset_delta(m4, 5), 3) # (2**10000+5)///3

>>> N = (1<<180_00) -99999
>>> N < m4*m4
True
>>> N < m47*m47
True

>>> divmod(N,m4) == divmod(N,int(m4))
True
>>> divmod(N,m47) == divmod(N,int(m47))
True
>>> divmod(N,m34) == divmod(N,int(m34))
True
>>> divmod(N,m347) == divmod(N,int(m347))
True
>>> divmod(N,m413) == divmod(N,int(m413))
True

>>> divmod(N,m4)    #doctest: +SKIP
Traceback (most recent call last):
    ...
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit


>>> def g(N, mX, number, /):
...     return timeit.timeit(stmt='divmod(N,mX)', number=number, globals=locals())

>>> g(N, m413, 10000) #why slower than others?? #doctest: +SKIP
0.26335815377533436
>>> g(N, m413, 10000) #doctest: +SKIP
0.08959722984582186
>>> g(N, MulDivOps4case__factor.from_base_factor(MulDivOps4case__delta.from_offset_delta(m4, 5), 3), 10000) #doctest: +SKIP
0.07331576943397522
>>> g(N, x:=int(m413), 1_000) #doctest: +SKIP
0.336280538700521
>>> g(N, x, 1_000) #doctest: +SKIP
0.3360267700627446

>>> 2*g(N, m413, 10000) < g(N, int(m413), 1_000) #first time slower, cache???
False
>>> 2*g(N, m413, 10000) < g(N, int(m413), 1_000)
True




>>> def gg(mX, /):
...     print(g(N, mX, 10000))
...     print(g(N, int(mX), 1_000))

#>>> gg(m4)
#>>> gg(m47)
#>>> gg(m34)
#>>> gg(m347)
#>>> gg(m413)

>>> gg(m4) #doctest: +SKIP
0.008270847611129284
0.2078399993479252
>>> gg(m47) #doctest: +SKIP
0.030422153882682323
0.20824123080819845
>>> gg(m34) #doctest: +SKIP
0.04014992341399193
0.208550076931715
>>> gg(m347) #doctest: +SKIP
0.06245084572583437
0.20819538366049528
>>> gg(m413) #doctest: +SKIP
0.07312523107975721
0.3363763075321913


>>> def f(mX, /):
...     t0 = g(N, mX, 10000)
...     t1 = g(N, int(mX), 1_000)
...     assert 2*t0 < t1, (t0, t1)
>>> f(m4)
>>> f(m47)
>>> f(m34)
>>> f(m347)
>>> f(m413)










######################
######################
#to avoid cache:create mX each time,use .repeat() instead of .timeit()
######################
######################

>>> m4_ = lambda:MulDivOps4case__zpow.from_exponent(100_00) # 2**10000
>>> m47_ = lambda:MulDivOps4case__delta.from_offset_delta(m4_(), 7) # 2**10000 +7
>>> m34_ = lambda:MulDivOps4case__coeff.from_coeff_base(3, m4_()) # 3*2**10000
>>> m347_ = lambda:MulDivOps4case__delta.from_offset_delta(m34_(), 7) # 3*2**10000 +7
>>> m413_ = lambda:MulDivOps4case__factor.from_base_factor(MulDivOps4case__delta.from_offset_delta(m4_(), 5), 3) # (2**10000+5)///3

>>> def g_(N, mX_, number, /):
...     return sum(timeit.repeat(stmt='divmod(N,mX_())', repeat=number, number=1, globals=locals()))
>>> def gg_(mX_, /):
...     print(g_(N, mX_, 1_000))
...     print(g_(N, lambda:int(mX_()), 1_000))

1_000 vs 1_000
1000_vs_1000:here
#>>> gg_(m4_)
#>>> gg_(m47_)
#>>> gg_(m34_)
#>>> gg_(m347_)
#>>> gg_(m413_)

>>> gg_(m4_) #doctest: +SKIP
0.004240994341671467
0.21141723170876503
>>> gg_(m47_) #doctest: +SKIP
0.09765331167727709
0.3021826855838299
>>> gg_(m34_) #doctest: +SKIP
0.009597760625183582
0.21434276271611452
>>> gg_(m347_) #doctest: +SKIP
0.017711793072521687
0.21918522845953703
>>> gg_(m413_) #doctest: +SKIP
0.023098227567970753
0.3527623862028122



]]


py_adhoc_call   seed.math.ops.mul_div_ops4zpow_delta   @f
#]]]'''
__all__ = r'''
MulDivOps4case__zpow
MulDivOps4case__delta
MulDivOps4case__coeff
MulDivOps4case__factor
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from numbers import Integral
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_non_ABC
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

def _API_Integral():
    def __ceil__(sf, /):
        'ceil(sf)'
    def __floor__(sf, /):
        'floor(sf)'
    def __trunc__(sf, /):
        'trunc(sf)'
    def __round__(sf, /):
        'round(sf)'
    def __int__(sf, /):
        'int(sf)'

    def __abs__(sf, /):
        'abs(sf)'
    def __neg__(sf, /):
        '-sf'
    def __pos__(sf, /):
        '+sf'
    def __invert__(sf, /):
        '~sf'

    def __eq__(sf, ot, /):
        'sf == ot'
    def __le__(sf, ot, /):
        'sf <= ot'
    def __lt__(sf, ot, /):
        'sf < ot'

    def __and__(sf, ot, /):
        'sf & ot'
    def __or__(sf, ot, /):
        'sf | ot'
    def __xor__(sf, ot, /):
        'sf ^ ot'
    def __lshift__(sf, ot, /):
        'sf << ot'
    def __rshift__(sf, ot, /):
        'sf >> ot'

    def __truediv__(sf, ot, /):
        'sf / ot'
    def __floordiv__(sf, ot, /):
        'sf // ot'
    def __mod__(sf, ot, /):
        'sf % ot'
    def __add__(sf, ot, /):
        'sf + ot'
    def __mul__(sf, ot, /):
        'sf * ot'
    def __pow__(sf, exponent, modulus=None, /):
        'sf ** exponent % modulus'
        """self ** exponent % modulus, but maybe faster.

        Accept the modulus argument if you want to support the
        3-argument version of pow(). Raise a TypeError if exponent < 0
        or any argument isn't Integral. Otherwise, just implement the
        2-argument version described in Complex.
        """



    def __rand__(sf, ot, /):
        'ot & sf'
    def __ror__(sf, ot, /):
        'ot | sf'
    def __rxor__(sf, ot, /):
        'ot ^ sf'
    def __rlshift__(sf, ot, /):
        'ot << sf'
    def __rrshift__(sf, ot, /):
        'ot >> sf'

    def __rtruediv__(sf, ot, /):
        'ot / sf'
    def __rfloordiv__(sf, ot, /):
        'ot // sf'
    def __rmod__(sf, ot, /):
        'ot % sf'
    def __radd__(sf, ot, /):
        'ot + sf'
    def __rmul__(sf, ot, /):
        'ot * sf'
    def __rpow__(sf, base, /):
        'base ** sf'

class _Base4m:
    'required:[sf._m :: semi-Integral]'
    def __int__(sf, /):
        'int(sf)'
        return int(sf._m)
    def __hash__(sf, /):
        'hash(sf)'
        return hash(sf._m)
    def __eq__(sf, ot, /):
        'sf == ot'
        return sf._m == ot
    def __le__(sf, ot, /):
        'sf <= ot'
        return sf._m <= ot
    def __lt__(sf, ot, /):
        'sf < ot'
        return sf._m < ot

    def __radd__(sf, ot, /):
        'ot + sf'
        return ot + sf._m
    def __rsub__(sf, ot, /):
        'ot - sf'
        return ot - sf._m #......

    def __add__(sf, ot, /):
        'sf + ot'
        return ot + sf._m
    def __sub__(sf, ot, /):
        'sf - ot'
        return sf._m - ot #......

    def __lshift__(sf, ot, /):
        'sf << ot'
        return sf._m << ot
    def __rshift__(sf, ot, /):
        'sf >> ot'
        return sf._m >> ot
    def __rlshift__(sf, ot, /):
        'ot << sf'
        return ot << sf._m
    def __rrshift__(sf, ot, /):
        'ot >> sf'
        return ot >> sf._m


    def __divmod__(sf, ot, /):
        'divmod(sf, ot)'
        return divmod(sf._m, ot)
    def __pow__(sf, exponent, modulus=None, /):
        'sf ** exponent % modulus'
        return pow(sf._m, exponent, modulus)

#end-class _Base4m:
class _Base4m__rdivmod__mul(_Base4m):
    'required:__mul__,__rdivmod__'
    def __rfloordiv__(sf, ot, /):
        'ot // sf'
        return divmod(ot, sf)[0]
    def __rmod__(sf, ot, /):
        'ot % sf'
        return divmod(ot, sf)[1]
    def __rmul__(sf, ot, /):
        'ot * sf'
        return sf * ot

#class MulDivOps4case__zpow(Integral):
#check_non_ABC(MulDivOps4case__zpow)
class MulDivOps4case__zpow(_Base4m):
    'see:case__zpow'
    @classmethod
    def from_exponent(cls, e, /):
        m = 1 << e
        mm1 = m-1
        return cls(m, e, mm1)
    def __new__(cls, m, e, mm1, /):
        if 0:
            #pseudo-Integral
            #semi-Integral
            check_type_le(Integral, m)
            check_type_le(Integral, e)
            check_type_le(Integral, mm1)
        #xxx:m = int(m)
        assert e >= 0
        assert m == (1<<e) # == 2**e
        assert m-1 == mm1 # == 0b11...1
        sf = super(__class__, cls).__new__(cls)
        sf._m = m
        sf._e = e
        sf._mm1 = mm1
        return sf
    def __repr__(sf, /):
        return repr_helper(sf, sf._m, sf._e, sf._mm1)

    def __rfloordiv__(sf, ot, /):
        'ot // sf'
        return ot >> sf._e
    def __rmod__(sf, ot, /):
        'ot % sf'
        return ot & sf._mm1
    def __rdivmod__(sf, ot, /):
        'divmod(ot, sf) # ot /% sf'
        return (ot >> sf._e, ot & sf._mm1)
    def __rmul__(sf, ot, /):
        'ot * sf'
        return ot << sf._e
    def __mul__(sf, ot, /):
        'sf * ot'
        return ot << sf._e

#end-class MulDivOps4case__zpow(_Base4m):

class MulDivOps4case__delta(_Base4m__rdivmod__mul):
    'see:case__delta'
    @classmethod
    def from_offset_delta(cls, D, dD, /):
        m = D +dD
        sqD = D*D
        return cls(m, D, dD, sqD)
    def __new__(cls, m, D, dD, sqD, /):
        if 0:check_type_le(_Base4m, D)
        assert m == D +dD
        assert m > 0
        assert D*D == sqD
        sf = super(__class__, cls).__new__(cls)
        sf._m = m
        sf._D = D
        sf._dD = dD
        sf._sqD = sqD
        return sf
    def __repr__(sf, /):
        return repr_helper(sf, sf._m, sf._D, sf._dD)

    def __rdivmod__(sf, ot, /):
        'divmod(ot, sf) # ot /% sf'
        N = ot
        M = sf._m
        sqD = sf._sqD
        pN = abs(N)
        if pN < M:
            if N < 0:
                return (-1, N+M)
            return (0, N)
        if not pN < sqD:
            raise ValueError('cause O(L**2)')
        D = sf._D
        dD = sf._dD
        (q_, r_) = divmod(N, D)
        if 0:
            (dq, r) = divmod(-q_*dD +r_, M)#vs:sf
        else:
            # !! [using sf] => O(L**2)
            # => using sqD to limit L
            #it seems faster when using sf instead M
            (dq, r) = divmod(-q_*dD +r_, sf)#vs:M
        q = q_ + dq
        return (q, r)
    def __mul__(sf, ot, /):
        'sf * ot'
        return sf._D * ot + sf._dD * ot

#end-class MulDivOps4case__delta(_Base4m__rdivmod__mul):

class MulDivOps4case__coeff(_Base4m__rdivmod__mul):
    'see:case__coeff'
    @classmethod
    def from_coeff_base(cls, k, D, /):
        m = k*D
        return cls(m, k, D)
    def __new__(cls, m, k, D, /):
        if 0:check_type_le(_Base4m, D)
        assert m == k*D
        sf = super(__class__, cls).__new__(cls)
        sf._m = m
        sf._k = k
        sf._D = D
        return sf
    def __repr__(sf, /):
        return repr_helper(sf, sf._m, sf._k, sf._D)

    def __rfloordiv__(sf, ot, /):
        'ot // sf'
        return ot // sf._D // sf._k
    def __rdivmod__(sf, ot, /):
        'divmod(ot, sf) # ot /% sf'
        N = ot
        M = sf._m
        pN = abs(N)
        if pN < M:
            if N < 0:
                return (-1, N+M)
            return (0, N)
        k = sf._k
        D = sf._D
        (_N, _R) = divmod(N, D)
        (_q, _r) = divmod(_N, k)
        q = _q
        r = _r*D +_R
        return (q, r)

    def __mul__(sf, ot, /):
        'sf * ot'
        return sf._D * (ot*sf._k)

#end-class MulDivOps4case__coeff(_Base4m__rdivmod__mul):

class MulDivOps4case__factor(_Base4m__rdivmod__mul):
    'see:case__factor'
    @classmethod
    def from_base_factor(cls, D, k, /):
        m, _0 = divmod(D, k)
        assert _0 == 0
        return cls(m, D, k)
    def __new__(cls, m, D, k, /):
        if 0:check_type_le(_Base4m, D)
        assert (m, 0) == divmod(D, k)
        sf = super(__class__, cls).__new__(cls)
        sf._m = m
        sf._D = D
        sf._k = k
        return sf
    def __repr__(sf, /):
        return repr_helper(sf, sf._m, sf._D, sf._k)

    def __rfloordiv__(sf, ot, /):
        'ot // sf'
        return ot * sf._k // sf._D
    def __rdivmod__(sf, ot, /):
        'divmod(ot, sf) # ot /% sf'
        N = ot
        M = sf._m
        pN = abs(N)
        if pN < M:
            if N < 0:
                return (-1, N+M)
            return (0, N)
        D = sf._D
        k = sf._k
        (_q, _r) = divmod(N*k, D)
        q = _q
        r = _r//k
        return (q, r)

    def __mul__(sf, ot, /):
        'sf * ot'
        return (sf._D * ot) //sf._k

#end-class MulDivOps4case__factor(_Base4m__rdivmod__mul):


__all__
from seed.math.ops.mul_div_ops4zpow_delta import MulDivOps4case__zpow, MulDivOps4case__delta, MulDivOps4case__coeff, MulDivOps4case__factor
from seed.math.ops.mul_div_ops4zpow_delta import *
