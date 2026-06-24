#__all__:goto
r'''[[[
e ../../python3_src/seed/algo/FFT/convolution.py


seed.algo.FFT.convolution
py -m nn_ns.app.debug_cmd   seed.algo.FFT.convolution -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.algo.FFT.convolution:__doc__ -ht # -ff -df
py -m nn_ns.app.doctest_cmd seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/polynomial/eval_polynomial/eval_polynomial_on_geometric_progression.py
view others/数学/polynomial/polynomial_evaluation.txt
]]
[[
TODO:
    std params
===
cache[ez4M]...
cache[M]...
    M:
        radixes:
            reversed_radixes
            scramble_
        tmps
        may ez4M
cache[ring_ops][M]...
    ring_ops:
        M2config_
            ez4M2config_
        mk_div_zpow5ez_
            div_2_
        mk__inv_M_or_div_M_
        M:
            config6M
                config6ez4M
            inv_M_or_div_M_
            as_g6IFFT:
                g:
                    gs
                    inv_g
                    inv_gs

def newAPI:func:
    .mk_mk_config5sz_ :: (params{ring_ops}) -> mk_config5sz_/(params{M}) -> config6sz
def newAPI:FFT_(M, radixes, reversed_radixes, scramble_, ring_ops, as_g6IFFT, g, inv_g, gs, inv_gs, ys7tmp, xs7IO, /):
    #_ping_pong__inplace
def newAPI:IFFT_(FFT_, M, radixes, reversed_radixes, scramble_, ring_ops, as_g6IFFT, g, inv_g, gs, inv_gs, ys7tmp, xs7IO, /):


def newAPI:negacyclic_convolution__len_is_zpow__num_bits4len_eq_(ez4M2config_{ring_ops, args4IFFT}, ez4M, us, vs, /, *, min_ez4M4recur=_default4min_ez4M4recur, validate=False, verbose=False):
    #_7symbolic_FFT_
===
<<==:
===
mk:ring_ops:
    Rational
    ZZ
    ZZ%modulus
    [R::ring]:
        R[X]
        R[X]%f(X)
        R(X) # fractional_ring
ring_ops:
    mk5int_
        zero
        one
        neg_one

    neg_
    add_
    sub_
    mul_
    ....
        pow_
        inv_ # perfect_inv_
        div_ # perfect_div_ # eg:ZZ
        mk_div_zpow5ez_{ring_ops}
            div_2_{ring_ops}
        mk__inv_M_or_div_M_{ring_ops}
M{len4signal}
    radixes{M}
    reversed_radixes{radixes{M}}
    scramble_{reversed_radixes{radixes{M}}}#scramble signal inplace
    ys{M} # tmp-storage#ping_pong
        => tmps: one or two:large enough
        => xs-->tmp[i:j][begin:cyc:step]
            scramble_ inplace
    ez4M{M} #zpow-only
++kw:as_g6IFFT@FFT_:to switch g,inv_g
g{ring_ops,M,as_g6IFFT}
    inv_g{g{ring_ops,M,as_g6IFFT}}
    gs{g{ring_ops,M,as_g6IFFT}}
    inv_gs{inv_g{ring_ops,M,as_g6IFFT}}
inv_M_or_div_M_{ring_ops,M}
ez4M2config_{mk_div_zpow5ez_{ring_ops}, args4IFFT}
config6ez4M{ez4M{M},ez4M2config_{mk_div_zpow5ez_{ring_ops}, args4IFFT}}

neg_, add_, mul_, zero
, g, inv_g
, gs, inv_gs
, M
, radixes, reversed_radixes
, scramble_, ys
, inv_M_or_div_M_
, modulus
<<==:
def IFFT_(FFT_, neg, add, mul, inv_g, inv4sz_or_div_sz_, xs, /, *, extra_args=(), may_gs=None, may_inv_gs=None, kwds4FFT={}):


def FFT__ping_pong(neg, add, mul, g, xs, /, **kwds):
def FFT__ping_pong__inplace(neg, add, mul, g, xs, /, *, may_radixes=None, scramble_=None, may_gs=None, may_ys=None):
def FFT__native(neg, add, mul, g, xs, /, *, may_gs=None):
def FFT__original__len_is_zpow(neg, add, mul, g, xs, /, *, may_gs=None):
def FFT__bit_scramble__len_is_zpow__inplace(neg, add, mul, g, xs, /, *, may_gs=None):
def FFT__bit_scramble__len_is_zpow(neg, add, mul, g, xs, /, **kwds):
def FFT__idx_digit_reverse(neg, add, mul, g, xs, /, **kwds):
def FFT__idx_digit_reverse__inplace(neg, add, mul, g, xs, /, *, may_radixes=None, scramble_=None, may_gs=None):
def FFT__idx_digit_reverse__inplace__mod_(modulus, g, xs, /, **kwds):
def FFT__idx_digit_reverse__mod_(modulus, g, xs, /, **kwds):




def acyclic_convolution__lenO_eq__7FFT_(neg_, add_, mul_, zero, g, inv_g, div_M_, M, us, vs, /, *, FFT_=None, kwds4FFT={}, IFFT_=None, kwds4IFFT={}, validate=False):
def acyclic_convolution__lenO_eq__7native_(add_, mul_, zero, M, us, vs, /):
def acyclic_convolution__len_is_zpow__num_bits4lenO_eq__7symbolic_FFT__7config__7zero_pad_(opsN, zero, ez4M, us, vs, /):

def negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, ez4M, us, vs, /, *, FFT_=None, kwds4FFT={}, IFFT_=None, kwds4IFFT={}, min_ez4M4recur=_default4min_ez4M4recur, validate=False, verbose=False):
def negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_(opsN, config6ez4M, us, vs, /):
def negacyclic_convolution__len_eq__7native_(neg_, add_, mul_, M, us, vs, /):

def cyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7recur_(opsN, div_2_, neg_, add_, mul_, zero, ez4M, us, vs, /, *, ver=1):
def cyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7zero_pad_(opsN, neg_, add_, mul_, zero, ez4M, us, vs, /):
def cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, div_M_, M, us, vs, /, *, FFT_=None, kwds4FFT={}, IFFT_=None, kwds4IFFT={}, validate=False):
def cyclic_convolution__len_eq__7native_(add_, mul_, M, us, vs, /):

def bothcyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7zero_pad_(opsN, neg_, add_, mul_, zero, ez4M, us, vs, /, *, case=0b0011):
===

]]


'#'; __doc__ = r'#'
>>> from seed.algo.FFT.index_scramble4FFT import _prepare4mod_zpow_

    #def _prepare4mod_zpow_(ez4modulus, ez4sz, /):
    #    -> (neg_, add_, mul_, g, inv_g, sz, div_sz_, may_radixes)
>>> from seed.algo.FFT.index_scramble4FFT import _prepare4mod_prime_

    #def _prepare4mod_prime_(modulus, g, sz=None, /):
    #    -> (neg_, add_, mul_, g, inv_g, sz, inv4sz, may_radixes)



>>> xs = [1, 2, 3, 4]
>>> ys = [1, 5, 7, 3]
>>> M = len(xs)
>>> (neg_, add_, mul_, g, inv_g, sz, inv4sz, may_radixes) = _prepare4mod_prime_(modulus:=1+2**16, pow(3, (modulus-1)//M, modulus), M)
>>> cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, inv4sz, sz, xs, ys, validate=True)
[48, 44, 32, 36]

>>> sz
4
>>> len(xs[:4])
4
>>> len(ys[:0])
0
>>> acyclic_convolution__lenO_eq__7FFT_(neg_, add_, mul_, zero:=0, g, inv_g, inv4sz, sz, xs[:4], ys[:0], validate=True)
[0, 0, 0, 0]
>>> acyclic_convolution__lenO_eq__7FFT_(neg_, add_, mul_, zero:=0, g, inv_g, inv4sz, sz, xs[:3], ys[:1], validate=True)
[1, 2, 3, 0]
>>> acyclic_convolution__lenO_eq__7FFT_(neg_, add_, mul_, zero:=0, g, inv_g, inv4sz, sz, xs[:2], ys[:2], validate=True)
[1, 7, 10, 0]
>>> acyclic_convolution__lenO_eq__7FFT_(neg_, add_, mul_, zero:=0, g, inv_g, inv4sz, sz, xs[:1], ys[:3], validate=True)
[1, 5, 7, 0]
>>> acyclic_convolution__lenO_eq__7FFT_(neg_, add_, mul_, zero:=0, g, inv_g, inv4sz, sz, xs[:0], ys[:4], validate=True)
[0, 0, 0, 0]


def acyclic_convolution__lenH_eq__7FFT__7even_lenO_(neg_, add_, mul_, zero, hg, inv_hg, div_2_, div_H_, H, us, vs, /, *, FFT_=None, kwds4FFT={}, IFFT_=None, kwds4IFFT={}, validate=False):
>>> H = sz>>1
>>> inv4H = pow(H, -1, modulus)
>>> def div_2_(x):
...     if x&1:
...         x += modulus
...     x >>= 1
...     x = add_(0,x)
...     return x
>>> acyclic_convolution__lenH_eq__7FFT__7even_lenO_(neg_, add_, mul_, zero:=0, g, inv_g, div_2_, inv4H, H, xs[:0], ys[:4], validate=True)
[0, 0, 0, 0]
>>> acyclic_convolution__lenH_eq__7FFT__7even_lenO_(neg_, add_, mul_, zero:=0, g, inv_g, div_2_, inv4H, H, xs[:1], ys[:3], validate=True)
[1, 5, 7, 0]
>>> acyclic_convolution__lenH_eq__7FFT__7even_lenO_(neg_, add_, mul_, zero:=0, g, inv_g, div_2_, inv4H, H, xs[:2], ys[:2], validate=True)
[1, 7, 10, 0]
>>> acyclic_convolution__lenH_eq__7FFT__7even_lenO_(neg_, add_, mul_, zero:=0, g, inv_g, div_2_, inv4H, H, xs[:3], ys[:1], validate=True)
[1, 2, 3, 0]
>>> acyclic_convolution__lenH_eq__7FFT__7even_lenO_(neg_, add_, mul_, zero:=0, g, inv_g, div_2_, inv4H, H, xs[:4], ys[:0], validate=True)
[0, 0, 0, 0]




考虑:自行设计gs:
    %16:
        1+15
        1+x+15+y
        不行,15不是 平方剩余%16,%32,%8

modulus be zpow:证明 二幂 不行！
    g=3%16 => 3,9,11,1
        3+9+11+1 == 24 =[%16]= 8
        g**(2*j) sum: 9+1 %16 == 10 == 8+2 # 更糟糕！无法绕过...
    g=3%32 => 3,9,27,17,19,25,11,1
        3+9+27+17+19+25+11+1 == 112 =[%32]= 16
        3,9,27,17,19,25,11,1 %16 -->:
        3,9,11, 1, 3, 9,11,1
        得加两遍才成为零
        g**(2*j) sum: 9+17+25+1 == 52 =[%32] == 20 == 16+4
    也许应当特化FFT(mod_zpow)
        但是:
            g**(2*j) sum => 得加四遍
            g**(4*j) sum => 得加八遍?四遍?
            注意:使用(g**2**k)作'g' => 得加2**(1+k)遍
    g=7%16 => 7,1  # g**j sum == 8
    g=7%32 => 7,17,23,1
        # g**j sum == 16
        # g**(2*j) sum == 18 == 16+2

>>> def f(e, /):
...     M = 1 << e
...     g = 3
...     gs = [g]
...     while not gs[-1] == 1:
...         gs.append(gs[-1]*g%M)
...     for _e in range(e):
...         ze = 1<<_e
...         _gs = gs[ze-1::ze]
...         s = sum(_gs)%M
...         print(_e, s, (s<<_e)%M, sep=':')
...     return gs

>>> f(5)
0:16:16
1:20:8
2:18:8
3:1:8
4:0:0
[3, 9, 27, 17, 19, 25, 11, 1]
>>> f(6)
0:32:32
1:40:16
2:36:16
3:34:16
4:1:16
5:0:0
[3, 9, 27, 17, 51, 25, 11, 33, 35, 41, 59, 49, 19, 57, 43, 1]
>>> f(7)
0:64:64
1:80:32
2:72:32
3:68:32
4:66:32
5:1:32
6:0:0
[3, 9, 27, 81, 115, 89, 11, 33, 99, 41, 123, 113, 83, 121, 107, 65, 67, 73, 91, 17, 51, 25, 75, 97, 35, 105, 59, 49, 19, 57, 43, 1]



>>> sz = 256
>>> xs = [*range(2, 2+5*sz, 5)]
>>> ys = [*range(7, 7+3*sz, 3)]
>>> (neg_, add_, mul_, g, inv_g, sz, div_sz_, may_radixes) = _prepare4mod_zpow_(128, 8, to_replace_neg=False) # (ez4modulus, ez4sz)
>>> ws = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, div_sz_, sz, xs, ys, validate=False)
>>> _ws = cyclic_convolution__len_eq__7native_(add_, mul_, sz, xs, ys)
>>> ws == _ws
False
>>> ws == [16324050944]*256
True
>>> _ws     #doctest: +ELLIPSIS
[43284224, 43769984, 44251904, 44729984, 45204224, 45674624, ..., 44251904, 43769984, 43284224, 42794624]
>>> sum(_ws)
16324050944
>>> (16324050944).bit_length()
34
>>> (neg_, add_, mul_, g, inv_g, sz, div_sz_, may_radixes) = _prepare4mod_zpow_(128, 8, to_replace_neg=True) # to_replace_neg:无效，因为没用到 有些FFT算法 不用 neg_
>>> ws = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, div_sz_, sz, xs, ys, validate=False)
>>> ws == [16324050944]*256
True

#bug:『加四遍:零填充至四倍』
#   得加2**(128-8)倍！
#   这就表示 没啥 数据空间
>>> (_, _, _, g, inv_g, _, _, _, gs) = _prepare4mod_zpow_(128, 8, with_gs=True)
>>> sum(gs)%2**128 -2**127
256
>>> sum(gs)%2**127
256
>>> sum(gs)*2%2**128
512
>>> sum(gs)*2**(128-9)%2**128 -2**127
0
>>> sum(gs)*2**(128-8)%2**128 # => 得加2**(128-8)倍！
0
>>> sum(gs[::2])%2**128 -2**127
128
>>> sum(gs[::2])*2%2**128
256
>>> sum(gs[::2])*2 *2**(128-9)%2**128 -2**127
0
>>> sum(gs[::2])*2 *2**(128-8)%2**128 # => 得加2**(128-8)倍！
0

#bug:加四遍:零填充至四倍:
>>> (_, _, _, _, _, sz, div_sz_, _) = _prepare4mod_zpow_(128, 10, to_replace_neg=False)
>>> ws = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, div_sz_, sz, xs*4, ys*4, validate=False, kwds4FFT=dict(may_gs=gs*4))
>>> ws[:4]
[261184815104, 261184815104, 261184815104, 261184815104]
>>> ws == [16324050944*16]*(256*4)
True
>>> ws = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, div_sz_, sz, xs+[0]*(sz*3//4), ys+[0]*(sz*3//4), validate=False, kwds4FFT=dict(may_gs=gs*4))
>>> ws == [16324050944]*(256*4)
True













view ../../python3_src/seed/math/prime_pint/primes_in_arithmetic_progression.py
py_adhoc_call   seed.math.prime_pint.primes_in_arithmetic_progression   @list.9:iter_primes_where_step_divs_phiP__using_primality_test7factorization4Pmm_  =1  =256 =None
    [257, 769, 3329, 7681, 7937, 9473, 10753, 11777, 12289]
py_adhoc_call   seed.math.prime_pint.primes_in_arithmetic_progression   @list.9:iter_primes_where_step_divs_phiP__using_primality_test7factorization4Pmm_  ='1+2**32'  =256 =None
    [4294968833, 4294973953, 4294977793, 4294979329, 4294983937, 4294986497, 4294988801, 4294989313, 4294991873]
py_adhoc_call   seed.math.prime_pint.primes_in_arithmetic_progression   @list.9:iter_primes_where_step_divs_phiP__using_primality_test7factorization4Pmm_  ='1+2**32'  =256 =None +with_factorization4Pmm
    [(4294968833, {2: 9, 7: 1, 11: 1, 108943: 1}), (4294973953, {2: 9, 3: 2, 521: 1, 1789: 1}), (4294977793, {2: 8, 3: 1, 7: 2, 61: 1, 1871: 1}), (4294979329, {2: 8, 3: 1, 439: 1, 12739: 1}), (4294983937, {2: 8, 3: 1, 23: 1, 243149: 1}), (4294986497, {2: 8, 16777291: 1}), (4294988801, {2: 10, 5: 2, 17: 1, 71: 1, 139: 1}), (4294989313, {2: 9, 3: 1, 829: 1, 3373: 1}), (4294991873, {2: 13, 29: 1, 101: 1, 179: 1})]

(4294991873, {2: 13, 29: 1, 101: 1, 179: 1})
py_adhoc_call   seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_   @find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_ '={2: 13, 29: 1, 101: 1, 179: 1}'  =4294991873
    3
>>> sz = 256
>>> (neg_, add_, mul_, g, inv_g, sz, inv4sz, may_radixes) = _prepare4mod_prime_(modulus:=4294991873, pow(3, (modulus-1)//sz, modulus), sz)
>>> ws = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, inv4sz, sz, xs, ys, validate=True)
>>> ws      #doctest: +ELLIPSIS
[43284224, 43769984, 44251904, 44729984, 45204224, 45674624, ..., 44251904, 43769984, 43284224, 42794624]
>>> _ws == ws
True
>>> _ws2 = cyclic_convolution__len_eq__7native_(add_, mul_, sz, xs, ys)
>>> _ws2 == ws
True








next_probable_prime ='2**34'
    17179869209
py_adhoc_call   seed.math.factor_pint.factor_pint__naive_brute_force   ,iter_factor_pint__naive_brute_force_ =17179869209-1  --max1_num_bits=35
    (2, 3)
    (83, 1)
    (1277, 1)
    (20261, 1)
py_adhoc_call   seed.math.factor_pint.factor_pint__naive_brute_force   @factor_pint__naive_brute_force_ =17179869209-1  --max1_num_bits=35
    {2: 3, 83: 1, 1277: 1, 20261: 1}

py_adhoc_call   seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_   @find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_ '={2: 3, 83: 1, 1277: 1, 20261: 1}'  =17179869209
    3
>>> 17179869209 == 25 +2**34
True


def negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, ez4M, us, vs, /, *, FFT_=None, validate=False, min_ez4M4recur=_default4min_ez4M4recur, kwds4FFT={}):
>>> kwds4ng = dict(min_ez4M4recur=2)

>>> (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero) = _prepare4mod_odd4symbolic_DFT_(odd_modulus:=17179869209)



>>> (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero) = _prepare4ring_ZZ4symbolic_DFT_()
>>> ez4M = 0
>>> xs = [2]
>>> ys = [5]
>>> negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, ez4M, xs, ys, validate=True, **kwds4ng)
[10]

>>> ez4M = 1
>>> xs = [1, 2]
>>> ys = [1, 5]
>>> negacyclic_convolution__len_eq__7native_(neg_, add_, mul_, 1<<ez4M, xs, ys)
[-9, 7]
>>> negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, ez4M, xs, ys, validate=True, **kwds4ng)
[-9, 7]

>>> ez4M = 2
>>> xs = [1, 2, 3, 4]
>>> ys = [1, 5, 7, 3]
>>> _ws_n0 = negacyclic_convolution__len_eq__7native_(neg_, add_, mul_, 1<<ez4M, xs, ys)
>>> #_ws_n1 = negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, ez4M, xs, ys, validate=False, verbose=True, min_ez4M4recur=2)
>>> _ws_n1 = negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, ez4M, xs, ys, validate=True, **kwds4ng)
>>> _ws_n0
[-46, -30, 8, 36]
>>> _ws_n1 == _ws_n0
True





>>> (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero) = _prepare4mod_odd4symbolic_DFT_(odd_modulus:=257)
>>> ez4M = 2
>>> xs = [1, 2, 3, 4]
>>> ys = [1, 5, 7, 3]
>>> _ws_n2 = negacyclic_convolution__len_eq__7native_(neg_, add_, mul_, 1<<ez4M, xs, ys)
>>> _ws_n3 = negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, ez4M, xs, ys, validate=True, **kwds4ng)
>>> _ws_n2
[-46, -30, 8, 36]

[211, 227, 8, 36]
>>> _ws_n3 == _ws_n2
True





>>> ez4M = 8
>>> sz = 1<<ez4M
>>> xs = [*range(2, 2+5*sz, 5)]
>>> ys = [*range(7, 7+3*sz, 3)]

>>> (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero) = _prepare4ring_ZZ4symbolic_DFT_()
>>> _ws_n6 = negacyclic_convolution__len_eq__7native_(neg_, add_, mul_, 1<<ez4M, xs, ys)
>>> _ws_n7 = negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, ez4M, xs, ys, validate=True, **kwds4ng)
>>> _ws_n6[:4]
[-43284196, -43769846, -44251544, -44729260]
>>> _ws_n6[-4:]
[38382956, 39841990, 41312536, 42794624]
>>> _ws_n7 == _ws_n6
True
>>> max(_ws_n6)
42794624
>>> min(_ws_n6)
-67653524
>>> max(_ws_n6).bit_length()
26
>>> abs(min(_ws_n6)).bit_length()
27
>>> max_num_bits_ = lambda xs:max(abs(min(xs)), abs(max(xs))).bit_length()
>>> max_num_bits_(_ws_n6)
27
>>> max_num_bits_(xs)
11
>>> max_num_bits_(ys)
10


>>> (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero) = _prepare4mod_odd4symbolic_DFT_(odd_modulus:=17179869209)
>>> _ws_n8 = negacyclic_convolution__len_eq__7native_(neg_, add_, mul_, 1<<ez4M, xs, ys)
>>> _ws_n9 = negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, ez4M, xs, ys, validate=True, **kwds4ng)
>>> _ws_n8[:4]
[-43284196, -43769846, -44251544, -44729260]

[17136585013, 17136099363, 17135617665, 17135139949]
>>> _ws_n8[-4:]
[38382956, 39841990, 41312536, 42794624]

[38382956, 39841990, 41312536, 42794624]
>>> _ws_n9 == _ws_n8
True
>>> _ws_n8 == [u%odd_modulus for u in _ws_n6]
False

True
>>> _ws_n8 == [hrem_(odd_modulus, u) for u in _ws_n6]
True
>>> _ws_n9 == _ws_n8 == _ws_n6
True




_prepare4mod_uint4symbolic_DFT_(modulus)
>>> (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero) = _prepare4mod_uint4symbolic_DFT_(modulus:=2**63)
>>> _ws_n10 = negacyclic_convolution__len_eq__7native_(neg_, add_, mul_, 1<<ez4M, xs, ys)
>>> _ws_n11 = negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, ez4M, xs, ys, validate=False, **kwds4ng)
>>> _ws_n10[:4]
[-43284196, -43769846, -44251544, -44729260]

[9223372036811491612, 9223372036811005962, 9223372036810524264, 9223372036810046548]
>>> _ws_n10[-4:]
[38382956, 39841990, 41312536, 42794624]
>>> _ws_n10 == [u%modulus for u in _ws_n6]
False

True
>>> _ws_n10 == [hrem_(modulus, u) for u in _ws_n6]
True
>>> _ws_n10 == _ws_n6
True

#before{using:hrem_}>>> _ws_n11 == _ws_n10  # fail!!!!!!!!!!
False
>>> _ws_n11 == _ws_n10  # ok!!!!!!!!!!why
True
>>> _ws_n11[:4]
[-43284196, -43769846, -44251544, -44729260]

[9187343239792527644, 9178336040537301002, 45035996229453416, 18014398464752724]
>>> _ws_n11[-4:]
[38382956, 39841990, 41312536, 42794624]

[369295169482763628, 171136785879920838, 306244774702506264, 333266372468211328]


>>> (-43284196)%2**63
9223372036811491612
>>> 9187343239792527644 -2**63
-36028797062248164




>>> (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero) = _prepare4mod_uint4symbolic_DFT_(modulus:=2**30)
>>> _ws_n12 = negacyclic_convolution__len_eq__7native_(neg_, add_, mul_, 1<<ez4M, xs, ys)
>>> _ws_n13 = negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, ez4M, xs, ys, validate=False, **kwds4ng)
>>> _ws_n12[:4]
[-43284196, -43769846, -44251544, -44729260]
>>> _ws_n12[-4:]
[38382956, 39841990, 41312536, 42794624]
>>> _ws_n13 == _ws_n12  # fail!!!!!!!!!!why overflow inside since div_M_()?????
False
>>> _ws_n12 == _ws_n6
True


>>> (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero) = _prepare4mod_uint4symbolic_DFT_(modulus:=2**34)
>>> _ws_n15 = negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, ez4M, xs, ys, validate=False, **kwds4ng)
>>> _ws_n15 == _ws_n6 #old_ver7zero_padding=>False #new_ver7DWT=>True
True
>>> (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero) = _prepare4mod_uint4symbolic_DFT_(modulus:=2**35)
>>> _ws_n17 = negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, ez4M, xs, ys, validate=False, **kwds4ng)
>>> _ws_n17 == _ws_n6
True
>>> max_num_bits_(_ws_n6)
27
>>> max_num_bits_(xs)
11
>>> max_num_bits_(ys)
10
>>> (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero) = _prepare4mod_uint4symbolic_DFT_(modulus:=2**27)
>>> _ws_n18 = negacyclic_convolution__len_eq__7native_(neg_, add_, mul_, 1<<ez4M, xs, ys)
>>> _ws_n18 == _ws_n6
False
>>> (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero) = _prepare4mod_uint4symbolic_DFT_(modulus:=2**28)
>>> _ws_n20 = negacyclic_convolution__len_eq__7native_(neg_, add_, mul_, 1<<ez4M, xs, ys)
>>> _ws_n20 == _ws_n6
True






cyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7recur_
cyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7zero_pad_
    bothcyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7zero_pad_
        acyclic_convolution__len_is_zpow__num_bits4lenO_eq__7symbolic_FFT__7config__7zero_pad_

def cyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7recur_(opsN, div_2_, neg_, add_, mul_, zero, ez4M, us, vs, /, *, ver=1):
def cyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7zero_pad_(opsN, neg_, add_, mul_, zero, ez4M, us, vs, /):
def bothcyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7zero_pad_(opsN, neg_, add_, mul_, zero, ez4M, us, vs, /, *, case=0b0011):
def acyclic_convolution__len_is_zpow__num_bits4lenO_eq__7symbolic_FFT__7config__7zero_pad_(opsN, zero, ez4M, us, vs, /):
def cyclic_convolution__len_eq__7native_(add_, mul_, M, us, vs, /):
>>> (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero) = _prepare4mod_uint4symbolic_DFT_(modulus:=2**35)
>>> opsN = Ops4convolution7symbolic_FFT(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, **kwds4ng)
>>> div_2_ = mk_div_zpow5ez_(1)
>>> ws_p61 = cyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7recur_(opsN, div_2_, neg_, add_, mul_, zero, ez4M, xs, ys)
>>> ws_p60 = cyclic_convolution__len_eq__7native_(add_, mul_, 1<<ez4M, xs, ys)
>>> ws_p60[:4]
[43284224, 43769984, 44251904, 44729984]
>>> ws_p60[-4:]
[44251904, 43769984, 43284224, 42794624]
>>> ws_p61 == ws_p60
True



>>> (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero) = _prepare4mod_uint4symbolic_DFT_(modulus:=2**36)
>>> opsN = Ops4convolution7symbolic_FFT(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, **kwds4ng)
>>> (ws_p65, ws_n65) = bothcyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7zero_pad_(opsN, neg_, add_, mul_, zero, ez4M, xs, ys)
>>> ws_p65 == ws_p60 #old_ver7zero_padding=>False #new_ver7DWT=>True
True
>>> ws_n65 == _ws_n6 #old_ver7zero_padding=>False #new_ver7DWT=>True
True


>>> (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero) = _prepare4mod_uint4symbolic_DFT_(modulus:=2**37)
>>> opsN = Ops4convolution7symbolic_FFT(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, **kwds4ng)
>>> (ws_p65, ws_n65) = bothcyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7zero_pad_(opsN, neg_, add_, mul_, zero, ez4M, xs, ys)
>>> ws_p65 == ws_p60
True
>>> ws_n65 == _ws_n6
True



>>> 17179869209 == 25 +2**34
True
>>> _0__8opsN = mk_ops4convolution7symbolic_FFT__5modulus_(0)
>>> _zpow40__8opsN = mk_ops4convolution7symbolic_FFT__5modulus_(2**40)
>>> _25_add_zpow34__8opsN = mk_ops4convolution7symbolic_FFT__5modulus_(17179869209)


>>> ez4M = 2
>>> xs = [1, 2, 3, 4]
>>> ys = [1, 5, 7, 3]
>>> _0__8opsN.negacyclic_convolution__num_bits4len_eq__7recur_(ez4M, xs, ys)
[-46, -30, 8, 36]
>>> _0__8opsN.cyclic_convolution__num_bits4len_eq__7recur_(ez4M, xs, ys)
[48, 44, 32, 36]

>>> _0__8opsN.cyclic_convolution__num_bits4len_eq__7zero_pad_(ez4M, xs, ys)
[48, 44, 32, 36]
>>> _0__8opsN.bothcyclic_convolution__num_bits4len_eq__7zero_pad_(ez4M, xs, ys)
([48, 44, 32, 36], [-46, -30, 8, 36])
>>> _0__8opsN.acyclic_convolution__num_bits4lenO_eq__7zero_pad_(1+ez4M, xs, ys)
[1, 7, 20, 36, 47, 37, 12, 0]

>>> _0__8opsN.negacyclic_convolution__len_eq__7native_(1<<ez4M, xs, ys)
[-46, -30, 8, 36]
>>> _0__8opsN.cyclic_convolution__len_eq__7native_(1<<ez4M, xs, ys)
[48, 44, 32, 36]
>>> _0__8opsN.acyclic_convolution__lenO_eq__7native_(1<<(1+ez4M), xs, ys)
[1, 7, 20, 36, 47, 37, 12, 0]


>>> _0__8opsN.bothcyclic_convolution__num_bits4len_eq__7zero_pad_(ez4M, xs, ys, case=0b111)
([48, 44, 32, 36], [-46, -30, 8, 36], [1, 7, 20, 36, 47, 37, 12, 0])
>>> _0__8opsN.bothcyclic_convolution__num_bits4len_eq__7zero_pad_(ez4M, xs, ys, case=0b110)
([-46, -30, 8, 36], [1, 7, 20, 36, 47, 37, 12, 0])
>>> _0__8opsN.bothcyclic_convolution__num_bits4len_eq__7zero_pad_(ez4M, xs, ys, case=0b101)
([48, 44, 32, 36], [1, 7, 20, 36, 47, 37, 12, 0])
>>> _0__8opsN.bothcyclic_convolution__num_bits4len_eq__7zero_pad_(ez4M, xs, ys, case=0b011)
([48, 44, 32, 36], [-46, -30, 8, 36])
>>> _0__8opsN.bothcyclic_convolution__num_bits4len_eq__7zero_pad_(ez4M, xs, ys, case=0b010)
[-46, -30, 8, 36]
>>> _0__8opsN.bothcyclic_convolution__num_bits4len_eq__7zero_pad_(ez4M, xs, ys, case=0b001)
[48, 44, 32, 36]
>>> _0__8opsN.bothcyclic_convolution__num_bits4len_eq__7zero_pad_(ez4M, xs, ys, case=0b100)
[1, 7, 20, 36, 47, 37, 12, 0]
>>> _0__8opsN.bothcyclic_convolution__num_bits4len_eq__7zero_pad_(ez4M, xs, ys, case=0b000)
Traceback (most recent call last):
    ...
TypeError: 0


>>> _0__8opsN.cyclic_convolution__7commonAPI_(xs, ys)
[48, 44, 32, 36]
>>> _0__8opsN.acyclic_convolution__7commonAPI_(xs, ys)
[1, 7, 20, 36, 47, 37, 12, 0]
>>> _0__8opsN.negacyclic_convolution__7commonAPI_(xs, ys)
[-46, -30, 8, 36]





>>> _0__8opsG = mk_ops4convolution7FFT__5modulus_and_ground_root_(0, -1, 2)
>>> _zpow40__8opsG = mk_ops4convolution7FFT__5modulus_and_ground_root_(2**40, 3, 2**(40-2))
>>> _25_add_zpow34__8opsG = mk_ops4convolution7FFT__5modulus_and_ground_root_(17179869209, 3, 17179869209-1)
>>> _25_add_zpow34__8opsG.cyclic_convolution__7commonAPI_(xs, ys)
[48, 44, 32, 36]
>>> _25_add_zpow34__8opsG.acyclic_convolution__7commonAPI_(xs, ys)
[1, 7, 20, 36, 47, 37, 12, 0]






py_adhoc_call   seed.algo.FFT.convolution   @f
from seed.algo.FFT.convolution import *
]]]'''#'''
__all__ = r'''
mk_ops4convolution7symbolic_FFT__5modulus_
mk_ops4convolution7FFT__5modulus_and_ground_root_


Ops4convolution7FFT
    mk_ops4convolution7FFT__5modulus_and_ground_root_
cyclic_convolution__len_eq__7FFT_
    cyclic_convolution__len_eq__7native_

acyclic_convolution__lenH_eq__7FFT__7even_lenO_
acyclic_convolution__lenO_eq__7FFT_
    acyclic_convolution__lenI_eq__7FFT_
    acyclic_convolution__lenO_eq__7native_
        acyclic_convolution__lenI_eq__7native_



Ops4convolution7symbolic_FFT
    mk_ops4convolution7symbolic_FFT__5modulus_
negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_
    negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_
    negacyclic_convolution__len_eq__7native_


cyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7recur_
cyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7zero_pad_
    bothcyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7zero_pad_
        acyclic_convolution__len_is_zpow__num_bits4lenO_eq__7symbolic_FFT__7config__7zero_pad_



dyadic_operator_
sum0_
sum1_
weighted__inplace_
div5or_inv_
'''.split()#'''
        #mk_cached_prepare4negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_
        #Ops4convolution7symbolic_FFT
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__, 'FFT__ping_pong:_default_FFT,IFFT_:_default_IFFT_'):
    from seed.tiny_.check import check_type_is, check_int_ge, check_int_ge_lt
    from seed.algo.FFT.FFT import FFT__ping_pong as _default_FFT
    #def FFT__ping_pong(neg_, add_, mul_, g, xs, /, *, may_radixes=None, scramble_=None, may_gs=None, may_ys=None):
    #from seed.algo.FFT.index_scramble4FFT import FFT__idx_digit_reverse
    from seed.algo.FFT.index_scramble4FFT import IFFT_ as _default_IFFT_
    #def IFFT_(FFT_, neg_, add_, mul_, inv_g, inv4sz, xs, /, *, extra_args=(), may_gs=None, may_inv_gs=None, **kwds):
    from functools import reduce
    #reduce(function, iterable[, initializer])
    from itertools import chain
    from operator import __eq__
    from seed.debug.show_name_value_pairs_ import errshow_name_value_pairs_, show_name_value_pairs_, parse_xnms_
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
    from seed.math.hrem_ import hrem_, mk_hrem_
    from math import gcd
    from seed.debug.print_err import print_err, print_ferr
    from seed.types.FrozenDict import mk_FrozenDict
    from seed.tiny_.funcs import echo

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

#def dyadic_product_(mul_, us, vs, /):
def dyadic_operator_(op_, us, vs, /):
    assert len(us) == len(vs)
    return [*map(op_, us, vs)]
def sum0_(add_, zero, xs, /):
    return reduce(add_, xs, zero)
def sum1_(add_, xs, /):
    return reduce(add_, xs)
#cyclic_convolution__len_eq_
def cyclic_convolution__len_eq__7native_(add_, mul_, M, us, vs, /):
    #old:def cyclic_convolution__len_eq__7native_(add_, mul_, zero, M, us, vs, /):
    # for validate
    '[M == len(us) == len(vs)]'
    # [zero is useless]
    #del zero
    #ws = [sum0_(add_, zero, (mul_(us[j], vs[(k-j)%M]) for j in range(M))) for k in range(M)]
    #return ws
    if not M == len(us) == len(vs):raise TypeError
    ws = [sum1_(add_, (mul_(us[j], vs[(k-j)%M]) for j in range(M))) for k in range(M)]
    return ws
def negacyclic_convolution__len_eq__7native_(neg_, add_, mul_, M, us, vs, /):
    if not M == len(us) == len(vs):raise TypeError
    ws = [sum1_(add_, chain((mul_(us[j], vs[k-j]) for j in range(1+k)), map(neg_, (mul_(us[j], vs[(k-j)+M]) for j in range(1+k, M))))) for k in range(M)]
    return ws
def acyclic_convolution__lenI_eq__7native_(add_, mul_, zero, M, us, vs, /):
    # for validate
    '[M == len(us) == len(vs)][2*M == len(output)]'
    if not M == len(us) == len(vs):raise TypeError
    return acyclic_convolution__lenO_eq__7native_(add_, mul_, zero, M<<1, us, vs)
def acyclic_convolution__lenO_eq__7native_(add_, mul_, zero, M, us, vs, /):
    # for testing
    '[M == len(us) + len(vs)]'
    if not M == len(us) + len(vs):raise TypeError
    # sum0_ not sum1_: zero must occur
    ws = [sum0_(add_, zero, (mul_(us[j], vs[(k-j)]) for j in range(max(0, 1+k-len(vs)), min(1+k, len(us))))) for k in range(M)]
        # [0 <= k-j < len(vs)] <==> [k-len(vs) < j <= k]
    return ws

def acyclic_convolution__lenI_eq__7FFT_(neg_, add_, mul_, zero, hg, inv_hg, div_2M_, M, us, vs, /, *, FFT_=None, validate=False):
    # for validate
    '[M == len(us) == len(vs) == 1/2 * mul_order_(hg)][hg**M == -1]'
    if not M == len(us) == len(vs):raise TypeError
    return acyclic_convolution__lenO_eq__7FFT_(neg_, add_, mul_, zero, hg, inv_hg, div_2M_, M<<1, us, vs, FFT_=FFT_, validate=validate)
def acyclic_convolution__lenO_eq__7FFT_(neg_, add_, mul_, zero, g, inv_g, div_M_, M, us, vs, /, *, FFT_=None, kwds4FFT={}, IFFT_=None, kwds4IFFT={}, validate=False):
    # eg:polynomial multiplication
    '[M == len(us) + len(vs) == mul_order_(g)][g**M == 1] # [[M%2==0] => [1+g**(M///2) == 0]] #eg:bad usage:[g:=CRT([3,5], [1,-1])][g%15 == 4][order_mod_(15;g) == 2]but[(g+1)%15 =!= 0]'
    if not M == len(us) + len(vs):raise TypeError(M, len(us) + len(vs))
    #########old:
    #zero_padding
    us_zz = [*us, *[zero]*len(vs)]
    vs_zz = [*vs, *[zero]*len(us)]
        # (us, vs) used below@[validate=True]
    if not M == len(us_zz) == len(vs_zz):raise 000
    ws = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, div_M_, M, us_zz, vs_zz, FFT_=FFT_, kwds4FFT=kwds4FFT, IFFT_=IFFT_, kwds4IFFT=kwds4IFFT)
    if validate:
        assert ws == acyclic_convolution__lenO_eq__7native_(add_, mul_, zero, M, us, vs)
    return ws
def weighted__inplace_(mul_, w, xs, /):
    w1 = w
    for j in range(1, len(xs)):
        if j > 1:
            w = mul_(w, w1)
        xs[j] = mul_(w, xs[j])
def acyclic_convolution__lenH_eq__7FFT__7even_lenO_(neg_, add_, mul_, zero, hg, inv_hg, div_2_, div_H_, H, us, vs, /, *, FFT_=None, kwds4FFT={}, IFFT_=None, kwds4IFFT={}, validate=False):
    '[len(us) + len(vs) == 2**H][hg**H == -1]'
    if not 2*H == len(us) + len(vs):raise TypeError(H, len(us), len(vs))
    #########new:
    #DWT:
    def weighted_(xs, /):
        (xsP, [*xsN]) = wrap_(xs)
        assert len(xsP) == len(xsN) == H
        weighted__inplace_(mul_, hg, xsN)
        return (xsP, xsN)
    def wrap_(xs, /):
        dsz = len(xs) -H
        if not dsz:
            return (xs, xs)
        if dsz < 0:
            xs_zz = [*xs, *[zero]*(-dsz)]
            return (xs_zz, xs_zz)
        xsP = []
        xsN = []
        for j in range(dsz):
            a = xs[j]
            b = xs[H+j]
            xsP.append(add_(a, b))
            xsN.append(add_(a, neg_(b)))
        for j in range(dsz, H):
            a = xs[j]
            xsP.append(a)
            xsN.append(a)
        return (xsP, xsN)
    #########
    (usP, usN) = weighted_(us)
    assert len(usP) == len(usN) == H
    (vsP, vsN) = weighted_(vs)
    assert len(vsP) == len(vsN) == H

    # [hg**H == -1]
    g = mul_(hg,hg)
    # [g**H == 1]
    inv_g = mul_(inv_hg,inv_hg)
    wsP = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, div_H_, H, usP, vsP, FFT_=FFT_, kwds4FFT=kwds4FFT, IFFT_=IFFT_, kwds4IFFT=kwds4IFFT)
    _wsN = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, div_H_, H, usN, vsN, FFT_=FFT_, kwds4FFT=kwds4FFT, IFFT_=IFFT_, kwds4IFFT=kwds4IFFT)
    weighted__inplace_(mul_, inv_hg, _wsN)
    wsN = _wsN
    wsL = [*map(div_2_, dyadic_operator_(add_, wsP, wsN))]
    wsR = [*map(div_2_, dyadic_operator_(add_, wsP, [*map(neg_, wsN)]))]
    ws = wsL + wsR
    if validate:
        assert ws == (_ws:=acyclic_convolution__lenO_eq__7native_(add_, mul_, zero, 2*H, us, vs)), ((us, vs), (usP, usN), (vsP, vsN), (zero, hg, inv_hg), (wsP, wsN), (ws, _ws))
        # AssertionError: (([1, 65025], [1, 64257]), ([1, 65025], [1, 65025]), ([1, 64257], [1, 64257]), (0, 65281, 256), ([65528, 63745], [65528, 7]), ([65528, 31876, 0, 31869], [1, 63745, 65527, 0]))

    return ws
    return (wsL, wsR)

def _fix_FFTs(FFT_, IFFT_, /):
    if IFFT_ is None:
        IFFT_ = _default_IFFT_
    if FFT_ is None:
        FFT_ = _default_FFT
        #FFT_ = FFT__ping_pong
        #FFT_ = FFT__idx_digit_reverse
    return (FFT_, IFFT_)
def cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, div_M_, M, us, vs, /, *, FFT_=None, kwds4FFT={}, IFFT_=None, kwds4IFFT={}, validate=False):
    # using FFT:O(M*lnM)*field_mul
    '[M == len(us) == len(vs) == mul_order_(g)][g**M == 1] # [[M%2==0] => [1+g**(M///2) == 0]] #eg:bad usage:[g:=CRT([3,5], [1,-1])][g%15 == 4][order_mod_(15;g) == 2]but[(g+1)%15 =!= 0]'
    # [cyclic_convolution__len_eq_(M; us, vs) == IDFT(g; DFT(g;us) .*. DFT(g;vs))]
    (FFT_, IFFT_) = _fix_FFTs(FFT_, IFFT_)
    DFT4us = FFT_(neg_, add_, mul_, g, us, **kwds4FFT)
    DFT4vs = FFT_(neg_, add_, mul_, g, vs, **kwds4FFT)
    DFT4ws = dyadic_operator_(mul_, DFT4us, DFT4vs)
    ws = IFFT_(FFT_, neg_, add_, mul_, inv_g, div_M_, DFT4ws, kwds4FFT=kwds4FFT, **kwds4IFFT)
    if validate:
        # !! [zero is useless]
        #assert ws == (_ws:=cyclic_convolution__len_eq__7native_(add_, mul_, zero:=None, M, us, vs)), (ws, _ws)
        assert ws == (_ws:=cyclic_convolution__len_eq__7native_(add_, mul_, M, us, vs)), (ws, _ws)
    return ws


class _Readonly:
    def __delattr__(sf, nm, /):
        raise AttributeError(nm)
    def __setattr__(sf, nm, x, /):
        if hasattr(sf, nm):
            raise AttributeError(nm)
        super(__class__, sf).__setattr__(nm, x)
    #:####################
    #:###common:opsG&&opsN
    #:opsX.neg_,add_,mul_,mk5int_,zero,one,neg_one,eq_zero_,eq_one_,eq_neg_one_, eq7ring_,sub_,mk_perfect_div_
    #:opsX.cyclic_convolution__7commonAPI_(xs, ys)
    #:opsX.acyclic_convolution__7commonAPI_(xs, ys)
    #:opsX.negacyclic_convolution__7commonAPI_(xs, ys)
    ######################
    if 0:
        def eq7ring_(sf, x, y, /):
            return x == y
    def eq_zero_(sf, x, /):
        return sf.eq7ring_(x, sf.zero)
    def eq_one_(sf, x, /):
        return sf.eq7ring_(x, sf.one)
    def eq_neg_one_(sf, x, /):
        return sf.eq7ring_(x, sf.neg_one)
    def sub_(sf, x, y, /):
        return sf.add_(x, sf.neg_(y))
    def mk_perfect_div_(sf, x, /):
        if sf.eq_neg_one_(x):
            return sf.neg_
        if sf.eq_one_(x):
            return echo
        if not None is (mk_perfect_div_:=vars(sf).get('mk_perfect_div_')):
            return mk_perfect_div_(x)
        raise NotImplementedError('mk_perfect_div_', sf, x)
def mk_ops4convolution7FFT__5modulus_and_ground_root_(modulus, ground_root, mul_order4ground_root, /, **kwds):
    opsG = Ops4convolution7FFT.mk5modulus_and_ground_root_(modulus, ground_root, mul_order4ground_root, **kwds)
    return opsG
class Ops4convolution7FFT(_Readonly):
    'opsG'
    ######################
    #vs:Ops4convolution7symbolic_FFT
    ######################
    ######################
    ######################
    def FFT_(sf, sz, us, /, **kwds4FFT):
        if not sz == len(us):raise TypeError
        if not sz:return []
        config6sz = sf.sz2config_(sz)
        (_True, st, st_ex) = config6sz
        (g, inv_g, gs, inv_gs, inv_sz_or_div_sz_, sz) = st_ex
        DFT4us = sf._FFT_(sf.neg_, sf.add_, sf.mul_, g, us, may_gs=gs, **sf._kwds4FFT, **kwds4FFT)
        return DFT4us
    def IFFT_(sf, sz, DFT4us, /, **kwds4FFT):
        if not sz == len(DFT4us):raise TypeError
        if not sz:return []
        config6sz = sf.sz2config_(sz)
        (_True, st, st_ex) = config6sz
        (g, inv_g, gs, inv_gs, inv_sz_or_div_sz_, sz) = st_ex
        us = sf._IFFT_(sf._FFT_, sf.neg_, sf.add_, sf.mul_, inv_g, inv_sz_or_div_sz_, DFT4us, may_gs=gs, may_inv_gs=inv_gs, kwds4FFT=sf._kwds4FFT, **sf._kwds4IFFT)
        return us
    ######################
    def cyclic_convolution__len_eq_(sf, sz, us, vs, /, **kwds):
        if not sz == len(us) == len(vs):raise TypeError
        if not sz:return []
        config6sz = sf.sz2config_(sz)
        (_True, st, st_ex) = config6sz
        (g, inv_g, gs, inv_gs, inv_sz_or_div_sz_, sz) = st_ex
        return cyclic_convolution__len_eq__7FFT_(sf.neg_, sf.add_, sf.mul_, g, inv_g, inv_sz_or_div_sz_, sz, us, vs, FFT_=sf._FFT_, kwds4FFT=sf._kwds4FFT, IFFT_=sf._IFFT_, kwds4IFFT=sf._kwds4IFFT, **kwds)
    def acyclic_convolution__lenO_eq_(sf, sz, us, vs, /, **kwds):
        if not sz == len(us) + len(vs):raise TypeError
        if not sz:return []
        config6sz = sf.sz2config_(sz)
        (_True, st, st_ex) = config6sz
        (g, inv_g, gs, inv_gs, inv_sz_or_div_sz_, sz) = st_ex
        return acyclic_convolution__lenO_eq__7FFT_(sf.neg_, sf.add_, sf.mul_, sf.zero, g, inv_g, inv_sz_or_div_sz_, sz, us, vs, FFT_=sf._FFT_, kwds4FFT=sf._kwds4FFT, IFFT_=sf._IFFT_, kwds4IFFT=sf._kwds4IFFT, **kwds)

    ######################
    # common:Ops4convolution7FFT&&Ops4convolution7symbolic_FFT
    def cyclic_convolution__7commonAPI_(sf, us, vs, /):
        return sf.cyclic_convolution__len_eq_(len(us), us, vs)
    def acyclic_convolution__7commonAPI_(sf, us, vs, /):
        return sf.acyclic_convolution__lenO_eq_(len(us)+len(vs), us, vs)
    def negacyclic_convolution__7commonAPI_(sf, us, vs, /):
        raise NotImplementedError
        return sf.negacyclic_convolution__len_eq_(len(us), us, vs)


    def cyclic_convolution__len_eq__7native_(sf, sz, us, vs, /):
        return cyclic_convolution__len_eq__7native_(sf.add_, sf.mul_, sz, us, vs)
    def negacyclic_convolution__len_eq__7native_(sf, sz, us, vs, /):
        return negacyclic_convolution__len_eq__7native_(sf.neg_, sf.add_, sf.mul_, sz, us, vs)
    def acyclic_convolution__lenO_eq__7native_(sf, sz, us, vs, /):
        return acyclic_convolution__lenO_eq__7native_(sf.add_, sf.mul_, sf.zero, sz, us, vs)
    ######################
    ######################
    ######################
    @classmethod
    def mk5modulus_and_ground_root_(cls, modulus, ground_root, mul_order4ground_root, /, **kwds):
        #vs:mk5modulus_
        (neg_, add_, mul_, pow4g_, mk_div_sz5sz_, mk5int_, zero, ground_root) = _prepare4mod_uint4FFT_(modulus, ground_root, mul_order4ground_root)
        pow4g_
        mk_div_sz5sz_
        return cls(neg_, add_, mul_, pow4g_, mk_div_sz5sz_, mk5int_, zero, ground_root, mul_order4ground_root)
    def __init__(sf, neg_, add_, mul_, pow4g_, mk_div_sz5sz_, mk5int_, zero, ground_root, mul_order4ground_root, /, *, eq7ring_=None, mk_perfect_div_=None, FFT_=None, kwds4FFT={}, IFFT_=None, kwds4IFFT={}):
        #see:mk_div_zpow5ez_/_4ez2div_zpow_,mk__inv_M_or_div_M_
        mk_div_sz5sz_ = _4sz2div_sz_(mk_div_sz5sz_)
        sf._st = (neg_, add_, mul_, pow4g_, mk_div_sz5sz_, mk5int_, zero, ground_root, mul_order4ground_root)
        sf.neg_ = neg_
        sf.add_ = add_
        sf.mul_ = mul_
        sf.pow4g_= pow4g_
        sf.mk_div_sz5sz_= mk_div_sz5sz_
        if not None is mk_perfect_div_:vars(sf)['mk_perfect_div_'] = mk_perfect_div_
        sf.mk5int_ = mk5int_
        sf.zero = zero
        sf.one = mk5int_(1)
        sf.neg_one = mk5int_(-1)
        sf.eq7ring_ = __eq__ if eq7ring_ is None else eq7ring_
        sf.ground_root = ground_root
        sf.mul_order4ground_root = mul_order4ground_root
        sf._d = sz2config = {}
        (FFT_, IFFT_) = _fix_FFTs(FFT_, IFFT_)
        sf._FFT_ = FFT_
        sf._kwds4FFT = kwds4FFT
        sf._IFFT_ = IFFT_
        sf._kwds4IFFT = kwds4IFFT
    def sz2config_(sf, sz, /):
        sz2config = sf._d
        try:
            return sz2config[sz]
        except KeyError:
            pass
        config6sz = sf._prepare(sz)
        sz2config[sz] = config6sz
        return sf.sz2config_(sz)
    def _prepare(sf, sz, /):
        check_int_ge(0, sz)
        st = sf._st
        if sz == 0:
            config6sz = (False, st, may_st_ex:=None)
            return config6sz
        (neg_, add_, mul_, pow4g_, mk_div_sz5sz_, mk5int_, zero, ground_root, mul_order4ground_root) = st
        if not mul_order4ground_root%sz == 0:raise ValueError(sz, mul_order4ground_root)
        g = pow4g_(ground_root, mul_order4ground_root//sz)
        #inv_g = pow4g_(ground_root, -1+sz)
        (gs, inv_gs) = _mk_pows(mul_, g, sz)
        inv_g = gs[-1]
        inv_sz_or_div_sz_ = mk_div_sz5sz_(sz)
        st_ex = (g, inv_g, gs, inv_gs, inv_sz_or_div_sz_, sz)
        config6sz = (True, st, may_st_ex:=st_ex)
        return config6sz

        r'''[[[
        neg_, add_, mul_, zero
        , g, inv_g
        , gs, inv_gs
        , M
        , radixes, reversed_radixes
        , scramble_, ys
        , inv_M_or_div_M_
        , modulus
        #]]]'''#'''
def _mk_pows(mul_, g, sz, /):
    assert sz > 0
    gs = [None, g]
    h = g
    for _ in range(-1+sz):
        gs.append(h:=mul_(g, h))
    one = gs.pop()
    gs[0] = one
    gs = tuple(gs)
    inv_gs = (gs[0], *gs[:0:-1])
    assert len(gs) == sz
    assert len(inv_gs) == sz
    return (gs, inv_gs)
class _4sz2div_sz_(dict):
    'mk_div_sz5sz_ -> sz2div_sz_/{sz:(div_sz_|inv_sz)}'
    def __init__(sf, mk_div_sz5sz_, /):
        #skip dict.__init__
        pass

    def __new__(cls, mk_div_sz5sz_, /):
        if type(mk_div_sz5sz_) is cls:
            sf = mk_div_sz5sz_
        elif callable(mk_div_sz5sz_):
            sf = super(__class__, cls).__new__(cls)
            super(__class__, cls).__init__(sf)
            sf._mk = mk_div_sz5sz_
        elif hasattr(mk_div_sz5sz_, '__getitem__'):
            sf = mk_div_sz5sz_
        else:
            raise TypeError(type(mk_div_sz5sz_))
        return sf
    def __call__(sf, sz, /):
        return sf[sz]
    def __missing__(sf, sz, /):
        sf[sz] = sf._mk(sz)
        return sf[sz]






























class _bad_int(int):
    def __repr__(sf, /):
        i = int.__repr__(sf)
        cls = type(sf)
        nm = cls.__name__
        return f'{nm}({i})'

    __abs__             = None
    __add__             = None
    __and__             = None
    __bool__            = None
    __ceil__            = None
    __divmod__          = None
    __float__           = None
    __floor__           = None
    __floordiv__        = None
    __ge__              = None
    __gt__              = None
    __index__           = None
    #__int__             = None
    __invert__          = None
    __le__              = None
    __lshift__          = None
    __lt__              = None
    __mod__             = None
    __mul__             = None
    __neg__             = None
    __or__              = None
    __pos__             = None
    __pow__             = None
    __radd__            = None
    __rand__            = None
    __rdivmod__         = None
    __rfloordiv__       = None
    __rlshift__         = None
    __rmod__            = None
    __rmul__            = None
    __ror__             = None
    __round__           = None
    __rpow__            = None
    __rrshift__         = None
    __rshift__          = None
    __rsub__            = None
    __rtruediv__        = None
    __rxor__            = None
    __sub__             = None
    __truediv__         = None
    __trunc__           = None
    __xor__             = None
    as_integer_ratio    = None
    bit_count           = None
    bit_length          = None
    conjugate           = None
    denominator         = None
    numerator           = None
    imag                = None
    real                = None
    pass
    def __rmul__(sf, ot, /):
        return NotImplemented
    def __mul__(sf, ot, /):
        return NotImplemented
class _4z(_bad_int):
    def ___get__funcname__args__ordered_kwdxxxs___(sf):
        return (None, (int(sf),), [])
    pass
#class _4t(_bad_int): pass
_z = _4z(1)
#_t = _4t(1)
class _Rx(tuple):
    def __radd__(sf, ot, /):
        return NotImplemented
    def __add__(sf, ot, /):
        return NotImplemented
    def __rmul__(sf, ot, /):
        return NotImplemented
    def __mul__(sf, ot, /):
        return NotImplemented
class _Rz(_Rx):
    def ___get__funcname__args__ordered_kwdxxxs___(sf):
        return (None, ([*sf],), [])
    pass
class _Rzt(_Rx):
    def ___get__funcname__args__ordered_kwdxxxs___(sf):
        return (None, ([*sf],), [])
    pass
def mk_ops4convolution7symbolic_FFT__5modulus_(modulus, /, **kwds):
    opsN = Ops4convolution7symbolic_FFT.mk5modulus_(modulus, **kwds)
    return opsN
def _ez5M_(M, /):
    ez4M = -1+M.bit_length()
    if not 1<<ez4M == M:raise ValueError(M)
    return ez4M
#min_ez4M4recur
_default4min_ez4M4recur = 5
    # <<== view ../../python3_src/seed/math/factor_pint/factor_pint__7batch_gcd_IIdiffs.py
    # _3_negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_:goto
class Ops4convolution7symbolic_FFT(_Readonly):
    'opsN # O(MlnMlnlnM) # see:negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_'
    #.def __delattr__(sf, nm, /):
    #.    raise AttributeError(nm)
    #.def __setattr__(sf, nm, x, /):
    #.    if hasattr(sf, nm):
    #.        raise AttributeError(nm)
    #.    super(__class__, sf).__setattr__(nm, x)
    ########################
    def negacyclic_convolution__num_bits4len_eq__7recur_(sf, ez4M, us, vs, /):
        config6ez4M = sf.ez4M2config_(ez4M)
        return negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_(sf, config6ez4M, us, vs)
    def cyclic_convolution__num_bits4len_eq__7recur_(sf, ez4M, us, vs, /):
        return cyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7recur_(sf, sf.div_2_, sf.neg_, sf.add_, sf.mul_, sf.zero, ez4M, us, vs)
    def cyclic_convolution__num_bits4len_eq__7zero_pad_(sf, ez4M, us, vs, /):
        return cyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7zero_pad_(sf, sf.neg_, sf.add_, sf.mul_, sf.zero, ez4M, us, vs)
    def bothcyclic_convolution__num_bits4len_eq__7zero_pad_(sf, ez4M, us, vs, /, **kwds):
        return bothcyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7zero_pad_(sf, sf.neg_, sf.add_, sf.mul_, sf.zero, ez4M, us, vs, **kwds)
    def acyclic_convolution__num_bits4lenO_eq__7zero_pad_(sf, ez4M, us, vs, /):
        return acyclic_convolution__len_is_zpow__num_bits4lenO_eq__7symbolic_FFT__7config__7zero_pad_(sf, sf.zero, ez4M, us, vs)
    def cyclic_convolution__num_bits4len_eq__7native_(sf, ez4M, us, vs, /):
        return cyclic_convolution__len_eq__7native_(sf.add_, sf.mul_, 1<<ez4M, us, vs)
    ######################
    # common:Ops4convolution7FFT&&Ops4convolution7symbolic_FFT
    def cyclic_convolution__7commonAPI_(sf, us, vs, /):
        return sf.cyclic_convolution__num_bits4len_eq__7recur_(_ez5M_(len(us)), us, vs)
    def acyclic_convolution__7commonAPI_(sf, us, vs, /):
        return sf.acyclic_convolution__num_bits4lenO_eq__7zero_pad_(_ez5M_(len(us)+len(vs)), us, vs)
    def negacyclic_convolution__7commonAPI_(sf, us, vs, /):
        return sf.negacyclic_convolution__num_bits4len_eq__7recur_(_ez5M_(len(us)), us, vs)

    def cyclic_convolution__len_eq__7native_(sf, M, us, vs, /):
        return cyclic_convolution__len_eq__7native_(sf.add_, sf.mul_, M, us, vs)
    def negacyclic_convolution__len_eq__7native_(sf, M, us, vs, /):
        return negacyclic_convolution__len_eq__7native_(sf.neg_, sf.add_, sf.mul_, M, us, vs)
    def acyclic_convolution__lenO_eq__7native_(sf, M, us, vs, /):
        return acyclic_convolution__lenO_eq__7native_(sf.add_, sf.mul_, sf.zero, M, us, vs)
    ########################
    @classmethod
    def mk5modulus_(cls, modulus, /, **kwds):
        (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero) = _prepare4mod_uint4symbolic_DFT_(modulus)
        opsN = cls(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, **kwds)
        return opsN
    ########################
    def __init__(sf, mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, /, *, eq7ring_=None, mk_perfect_div_=None, FFT_=None, kwds4FFT={}, IFFT_=None, kwds4IFFT={}, min_ez4M4recur=_default4min_ez4M4recur, validate=False, verbose=False):
        check_int_ge(2, min_ez4M4recur)
        (FFT_, IFFT_) = _fix_FFTs(FFT_, IFFT_)
        ez2div_zpow_ = _4ez2div_zpow_(mk_div_zpow5ez_)
        mk_div_zpow5ez_ = ez2div_zpow_
        ez4M2config = {}
        old_kwds4FFT = kwds4FFT
        old_kwds4IFFT = kwds4IFFT
        del kwds4FFT, kwds4IFFT
        sf._st0 = ((validate, verbose, min_ez4M4recur), (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero), (FFT_, old_kwds4FFT, IFFT_, old_kwds4IFFT)) # st1 -ez4M2config_ -ez4M2config
        sf._d = ez4M2config
        sf.validate = validate
        sf.verbose = verbose
        sf.min_ez4M4recur = min_ez4M4recur
        sf.mk_div_zpow5ez_ = mk_div_zpow5ez_
        if not None is mk_perfect_div_:vars(sf)['mk_perfect_div_'] = mk_perfect_div_
        sf.neg_ = neg_
        sf.add_ = add_
        sf.mul_ = mul_
        sf.mk5int_ = mk5int_
        sf.zero = zero
        sf.one = mk5int_(1)
        sf.neg_one = mk5int_(-1)
        sf.eq7ring_ = __eq__ if eq7ring_ is None else eq7ring_
        sf.FFT_ = FFT_
        sf.old_kwds4FFT = old_kwds4FFT
        sf.IFFT_ = IFFT_
        sf.old_kwds4IFFT = old_kwds4IFFT
        sf.div_2_ = mk_div_zpow5ez_(1)
    def ez4M2config_(sf, ez4M, /):
        ez4M2config = sf._d
        try:
            return ez4M2config[ez4M]
        except KeyError:
            pass
        config6ez4M = sf._prepare(ez4M)
        ez4M2config[ez4M] = config6ez4M
        return sf.ez4M2config_(ez4M)
    def _prepare(sf, ez4M, /):
        check_int_ge(0, ez4M)
        #if ez4M < min_ez4M4recur:
        st0 = sf._st0
        payload0 = (ez4M, st0)
        if ez4M == 0:
            # !! cyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7recur_
            return (False, to_recur:=False, payload0, may_payload1:=None)
        ######################
        ((validate, verbose, min_ez4M4recur), (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero), (FFT_, old_kwds4FFT, IFFT_, old_kwds4IFFT)) = st0
        ######################
        to_recur = not ez4M < min_ez4M4recur

        em = ez4M
        ew = em//2
        en = em -ew
        #assert 1 <= ew <= en <= 1+ew <= em
        assert 0 <= ew <= en <= 1+ew <= em
        #if ew == 0: min_ez4M4recur = max(2, min_ez4M4recur)
                # to avoid RecursionError
                # [min_ez4M4recur:=1] for debug

        M = 1 << em # 高层规模
        N = 1 << en # 低层规模
        W = 1 << ew # 介层规模
        (neg7Rz_, add7Rz_, mul7Rz_, pow_g7Rz_, sub7Rz_, zero7Rz, mk_g5e_) = _prepare4symbolic_DFT_(mk_div_zpow5ez_, neg_, add_, mul_, zero, M, N, W, min_ez4M4recur, en, FFT_, old_kwds4FFT, IFFT_, old_kwds4IFFT, validate, verbose, sf)

        z = _z
        # [z**N == -1]
        #t = _t
        # [t**M == -1]
        hg = pow_g7Rz_(z, 2) if en > ew else z
        e4hg = int(hg)
        # [hg == z**e4hg]
        e4g = int(pow_g7Rz_(hg, 2))
        _2W = W<<1
        (div_2_7Rz_, div_W_7Rz_, div_2W_7Rz_) = _mk4div_2W_7Rz_(mk_div_zpow5ez_, mul_, ew, _2W, N)
        # [hg**W == -1]
        # [hg**(2*W) == 1]
        # [hg**(2*W-1) == hg**-1 == inv_hg]
        inv_hg = pow_g7Rz_(hg, _2W-1)
        assert mul7Rz_(hg, inv_hg) == _4z(0)
        if 0:
            #old_ver7zero_padding:
            sz = _2W
            e4the_g = e4hg
        else:
            #new_ver7DWT:
            sz = W
            e4the_g = e4g
        #bug:gs = (*map(mk_g5e_, range(_2W)),)
        gs = (*map(mk_g5e_, map(e4the_g.__mul__, range(sz))),)
        inv_gs = (gs[0], *gs[:0:-1])
        assert len(gs) == sz
        assert len(inv_gs) == sz
        new_kwds4FFT = dict(old_kwds4FFT, may_gs=gs) #mk_FrozenDict
        new_kwds4IFFT = dict(old_kwds4IFFT, may_inv_gs=inv_gs)
        #print_err('new_kwds4FFT=', new_kwds4FFT)
        assert new_kwds4FFT['may_gs'] is gs
        assert new_kwds4IFFT['may_inv_gs'] is inv_gs
        payload1 = ((em, ew, en), (M, W, N), (neg7Rz_, add7Rz_, mul7Rz_, pow_g7Rz_, sub7Rz_, zero7Rz, mk_g5e_), (z, hg, inv_hg, _2W, div_2_7Rz_, div_W_7Rz_, div_2W_7Rz_), (new_kwds4FFT, new_kwds4IFFT)) # == st2
        return (True, to_recur, payload0, may_payload1:=payload1)




def negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, ez4M, us, vs, /, *, FFT_=None, kwds4FFT={}, IFFT_=None, kwds4IFFT={}, min_ez4M4recur=_default4min_ez4M4recur, validate=False, verbose=False):
    opsN = Ops4convolution7symbolic_FFT(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, FFT_=FFT_, kwds4FFT=kwds4FFT, IFFT_=IFFT_, kwds4IFFT=kwds4IFFT, min_ez4M4recur=min_ez4M4recur, validate=validate, verbose=verbose)
    config6ez4M = opsN.ez4M2config_(ez4M)
    return negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_(opsN, config6ez4M, us, vs)
def cyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7zero_pad_(opsN, neg_, add_, mul_, zero, ez4M, us, vs, /):
    return bothcyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7zero_pad_(opsN, neg_, add_, mul_, zero, ez4M, us, vs, case=0b01)
def bothcyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7zero_pad_(opsN, neg_, add_, mul_, zero, ez4M, us, vs, /, *, case=0b0011):
    check_int_ge(0, ez4M)
    check_int_ge_lt(1, 8, case)
    M = 1 << ez4M
    if not M == len(us) == len(vs):raise TypeError(M, len(us) + len(vs))
    # !! [cyclic_convolution__len_eq_(M; us, vs) == acyclic_convolution__lenI_eq_(M; us, vs)[:M] .+. acyclic_convolution__lenI_eq_(M; us, vs)[M:]] # 对半折叠
    # !! [negacyclic_convolution__len_eq_(M; us, vs) == acyclic_convolution__lenI_eq_(M; us, vs)[:M] .-. acyclic_convolution__lenI_eq_(M; us, vs)[M:]] # 对半折叠
    ws_ws = acyclic_convolution__len_is_zpow__num_bits4lenO_eq__7symbolic_FFT__7config__7zero_pad_(opsN, zero, 1+ez4M, us, vs)
    if case&0b011:
        ws_wsL = ws_ws[:M]
        ws_wsR = ws_ws[M:]
    if case&0b001:
        wsP = dyadic_operator_(add_, ws_wsL, ws_wsR)
    if case&0b010:
        wsN = dyadic_operator_(add_, ws_wsL, [*map(neg_, ws_wsR)])
    match case:
        case 0b011:
            # both
            return (wsP, wsN)
        case 0b001:
            #cyclic_convolution__len_eq_
            return (wsP)
        case 0b010:
            #negacyclic_convolution__len_eq_
            return (wsN)
        case 0b100:
            #acyclic_convolution__lenO_eq_
            return (ws_ws)
        case 0b111:
            return (wsP, wsN, ws_ws)
        case 0b101:
            return (wsP,      ws_ws)
        case 0b110:
            return (     wsN, ws_ws)
        case _:
            raise Exception(case)
def acyclic_convolution__len_is_zpow__num_bits4lenO_eq__7symbolic_FFT__7config__7zero_pad_(opsN, zero, ez4M, us, vs, /):
    check_int_ge(0, ez4M)
    M = 1 << ez4M
    if not M == len(us) + len(vs):raise TypeError(M, len(us) + len(vs))
    #zero_padding
    us_zz = [*us, *[zero]*len(vs)]
    vs_zz = [*vs, *[zero]*len(us)]
        # (us, vs) used below@[validate=True]
    if not M == len(us_zz) == len(vs_zz):raise 000
    # !! [acyclic_convolution__lenI_eq_(M; us, vs)[M:] == cyclic_convolution__len_eq_(2*M; us++[0]*M, vs++[0]*M) == negacyclic_convolution__len_eq_(2*M; us++[0]*M, vs++[0]*M)] # 零填充统一
    config6ez4M = opsN.ez4M2config_(ez4M)
    ws = negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_(opsN, config6ez4M, us_zz, vs_zz)
    return ws

def cyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7recur_(opsN, div_2_, neg_, add_, mul_, zero, ez4M, us, vs, /, *, ver=1):
    check_int_ge_lt(1, 3, ver)
    if ver == 2:
        return cyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7zero_pad_(opsN, neg_, add_, mul_, zero, ez4M, us, vs)

    assert ver == 1
    check_int_ge(0, ez4M)
    if ez4M == 0:
        if not 1 == len(us) == len(vs):raise TypeError
        [a] = us
        [b] = vs
        return [mul_(a, b)]
    M = 1<<ez4M
    if not M == len(us) == len(vs):raise TypeError
    ez4H = -1+ez4M
    H = 1<<ez4H
    def f(us, /):
        (usL, usR) = (us[:H], us[H:])
        return g(usL, usR)
    def g(usL, usR, /):
        usP = dyadic_operator_(add_, usL, usR)
        usN = dyadic_operator_(add_, usL, [*map(neg_, usR)])
        return (usP, usN)
    (usP, usN) = f(us)
    (vsP, vsN) = f(vs)
    wsP =     cyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config__7recur_(opsN, div_2_, neg_, add_, mul_, zero, ez4H, usP, vsP, ver=ver)
    #wsN = negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_(ez4M2config_(ez4H), usN, vsN)
    config6ez4H = opsN.ez4M2config_(ez4H)
    wsN = negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_(opsN, config6ez4H, usN, vsN) #, validate=False
    (wsDL, wsDR) = g(wsP, wsN)
    wsD = wsDL + wsDR
    if not callable(div_2_):
        inv_2 = div_2_
        def div_2_(x, /):
            return mul_(inv_2, x)
    ws = [*map(div_2_, wsD)]
    return ws
    r'''[[[
    [(usL,usR) := (us[:M///2],us[M///2:])]
    [(vsL,vsR) := (vs[:M///2],vs[M///2:])]
    [(usP,usN) := (usL .+. usR,usL .-. usR)]
    [(vsP,vsN) := (vsL .+. vsR,vsL .-. vsR)]
    [wsP := cyclic_convolution__len_eq_(M///2; usP, vsP)]
    [wsN := negacyclic_convolution__len_eq_(M///2; usN, vsN)]
    [ws := cyclic_convolution__len_eq_(M; us, vs)]
    [2 *. ws == (wsP .+. wsN) ++ (wsP .-. wsN)]
    #]]]'''#'''


def negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_(opsN, config6ez4M, us, vs, /):
    #symbolic_g
    #symbolic_DFT
    match config6ez4M:
        case (_, False as to_recur, payload0, may_payload1):
            return _3_negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_(opsN, payload0, us, vs)
        case (_, True as to_recur, payload0, payload1):
            return _4_negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_(opsN, payload0, payload1, us, vs)
        case _:
            raise Exception(config6ez4M)
    r'''[[[
    match config6ez4M:
        case (False, payload4base):
            return _1_negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_(payload4base, us, vs)
        case (True, (False as to_recur, payload4base, st2)):
            return _1_negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_(payload4base, us, vs)
        case (True, payload4recur):
            return _2_negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_(payload4recur, us, vs)
            pass
        case _:
            raise Exception(config6ez4M)
    #]]]'''#'''

r'''[[[
def _1_negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_(payload4base, us, vs, /):
    #########
    (ez4M, st1) = payload4base
    ((validate, verbose), (min_ez4M4recur, ez4M2config, ez4M2config_), (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero), (FFT_, old_kwds4FFT, IFFT_, old_kwds4IFFT)) = st1
    #########
#]]]'''#'''
def _3_negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_(opsN, payload0, us, vs, /):
    #########
    (ez4M, st0) = payload0
    ((validate, verbose, min_ez4M4recur), (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero), _) = st0
    #########
    assert ez4M < min_ez4M4recur
    # min_ez4M4recur default 2:Tune this small-negacyclic breakover length to taste.
        #_default4min_ez4M4recur
    ws = negacyclic_convolution__len_eq__7native_(neg_, add_, mul_, 1<<ez4M, us, vs)
    if verbose:
        ttt = (ez4M, us, vs, ws)
        xnms = parse_xnms_('(ez4M, us, vs, ws)')
        errshow_name_value_pairs_(xnms, ttt)
    return ws
r'''[[[
def _2_negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_(payload4recur, us, vs, /):
    #########
    (to_recur, payload4base, st2) = payload4recur
    assert to_recur
    (ez4M, st1) = payload4base
    #########
    ((validate, verbose), (min_ez4M4recur, ez4M2config, ez4M2config_), (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero), (FFT_, old_kwds4FFT, IFFT_, old_kwds4IFFT)) = st1
    ((em, ew, en), (M, W, N), (neg7Rz_, add7Rz_, mul7Rz_, pow_g7Rz_, sub7Rz_, zero7Rz, mk_g5e_), (z, hg, inv_hg, _2W, div_2_7Rz_, div_W_7Rz_, div_2W_7Rz_), (new_kwds4FFT, new_kwds4IFFT)) = st2
    #########
#]]]'''#'''
def _4_negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_(opsN, payload0, payload1, us, vs, /):
    #########
    (ez4M, st0) = payload0
    ((validate, verbose, min_ez4M4recur), (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero), (FFT_, old_kwds4FFT, IFFT_, old_kwds4IFFT)) = st0
    ((em, ew, en), (M, W, N), (neg7Rz_, add7Rz_, mul7Rz_, pow_g7Rz_, sub7Rz_, zero7Rz, mk_g5e_), (z, hg, inv_hg, _2W, div_2_7Rz_, div_W_7Rz_, div_2W_7Rz_), (new_kwds4FFT, new_kwds4IFFT)) = payload1
    #########
    assert ez4M >= min_ez4M4recur
    if not M == len(us) == len(vs):raise TypeError
    # 数组转置:(N,W)-transpositions of us,vs
    poly7Rzt4us = _mk_poly7Rzt_(M, N, W, us)
    poly7Rzt4vs = _mk_poly7Rzt_(M, N, W, vs)


    # [hg**W == -1]
    # [hg**(2*W) == 1]
    # TODO:using: acyclic_convolution__lenH_eq__7FFT__7even_lenO_
    #print_err('new_kwds4FFT=', new_kwds4FFT)
    if 1:
        #new_ver7DWT:
        #   fixed:new_kwds4FFT.may_gs
        ws_ws7Rzt_ex = acyclic_convolution__lenH_eq__7FFT__7even_lenO_(neg7Rz_, add7Rz_, mul7Rz_, zero7Rz, hg, inv_hg, div_2_7Rz_, div_W_7Rz_, W, poly7Rzt4us, poly7Rzt4vs, FFT_=FFT_, kwds4FFT=new_kwds4FFT, IFFT_=IFFT_, kwds4IFFT=new_kwds4IFFT, validate=False)
    else:
        #old_ver7zero_padding:
        ws_ws7Rzt_ex = acyclic_convolution__lenO_eq__7FFT_(neg7Rz_, add7Rz_, mul7Rz_, zero7Rz, g:=hg, inv_g:=inv_hg, div_2W_7Rz_, _2W, poly7Rzt4us, poly7Rzt4vs, FFT_=FFT_, kwds4FFT=new_kwds4FFT, IFFT_=IFFT_, kwds4IFFT=new_kwds4IFFT, validate=False)
    assert len(ws_ws7Rzt_ex) == _2W
    if 0:
        ######################
        # !!!![ws_ws7Rzt_ex is coeffs for variable "t" not "hg"]!!!!
        #
        ######################
        #bug:
        # [ws7Rz := ws_ws7Rzt_ex[:M] .-. ws_ws7Rzt_ex[M:]]
        #bug:ws7Rz = dyadic_operator_(sub7Rz_, ws_ws7Rzt_ex[:M], ws_ws7Rzt_ex[M:])
        ws7Rz = dyadic_operator_(sub7Rz_, ws_ws7Rzt_ex[:W], ws_ws7Rzt_ex[W:])
        assert len(ws7Rz) == W
        # [ws := [ws7Rz[j%W].coeffs[j//W] | [j:<-[0..<M]]]]
        # ws = [ws7Rz[j%W][j//W] for j in range(M)]
        ws = [ws7Rz[k][i] for i in range(N) for k in range(W)]
        ######################
    # !! [z == t**W]
    # [ws7Rzt := ws_ws7Rzt_ex[:W] .+. z*ws_ws7Rzt_ex[W:]]
    ws7Rzt = [add7Rz_(a, mul7Rz_(z, b)) for (a, b) in zip(ws_ws7Rzt_ex[:W], ws_ws7Rzt_ex[W:])]
    assert len(ws7Rzt) == W

    ws = ws7Rt = [ws7Rzt[k][i] for i in range(N) for k in range(W)]
    assert len(ws) == M

    if verbose:
        _ws_ws7Rzt_ex = acyclic_convolution__lenO_eq__7native_(add7Rz_, mul7Rz_, zero7Rz, _2W, poly7Rzt4us, poly7Rzt4vs)
        #no more:_ws7Rz = negacyclic_convolution__len_eq__7native_(neg7Rz_, add7Rz_, mul7Rz_, W, poly7Rzt4us, poly7Rzt4vs)
        _ws = negacyclic_convolution__len_eq__7native_(neg_, add_, mul_, M, us, vs)
        ttt = (ez4M, ew, us, vs, poly7Rzt4us, poly7Rzt4vs, hg, inv_hg, ws_ws7Rzt_ex, _ws_ws7Rzt_ex, ws7Rzt, ws, _ws)
        xnms = parse_xnms_('(ez4M, ew, us, vs, poly7Rzt4us, poly7Rzt4vs, hg, inv_hg, ws_ws7Rzt_ex, _ws_ws7Rzt_ex, ws7Rzt, ws, _ws)')
        errshow_name_value_pairs_(xnms, ttt)
    if validate:
        assert ws == negacyclic_convolution__len_eq__7native_(neg_, add_, mul_, M, us, vs)
    return ws

def div5or_inv_(mul_, inv_sz_or_div_sz_, /):
    if callable(inv_sz_or_div_sz_):
        div_sz_ = inv_sz_or_div_sz_
    else:
        inv_sz = inv_sz_or_div_sz_
        def div_sz_(x, /):
            return mul_(inv_sz, x)
    return div_sz_
def _mk4div_2W_7Rz_(mk_div_zpow5ez_, mul_, ew, _2W, N, /):
    inv_2_or_div_2_7R_ = mk_div_zpow5ez_(1)
    inv_W_or_div_W_7R_ = mk_div_zpow5ez_(ew)
    inv_2W_or_div_2W_7R_ = mk_div_zpow5ez_(1+ew)

    div_2_7R_ = div5or_inv_(mul_, inv_2_or_div_2_7R_)
    div_W_7R_ = div5or_inv_(mul_, inv_W_or_div_W_7R_)
    div_2W_7R_ = div5or_inv_(mul_, inv_2W_or_div_2W_7R_)
    def div_2_7Rz_(xs, /):
        check_type_is(_Rz, xs)
        return _Rz(map(div_2_7R_, xs))
    def div_W_7Rz_(xs, /):
        check_type_is(_Rz, xs)
        return _Rz(map(div_W_7R_, xs))
    def div_2W_7Rz_(xs, /):
        check_type_is(_Rz, xs)
        #bug:assert len(xs) == _2W, (len(xs), _2W)
        assert len(xs) == N, (len(xs), N)
        return _Rz(map(div_2W_7R_, xs))
    return (div_2_7Rz_, div_W_7Rz_, div_2W_7Rz_)
def _prepare4symbolic_DFT_(mk_div_zpow5ez_, neg_, add_, mul_, zero, M, N, W, min_ez4M4recur, en, FFT_, kwds4FFT, IFFT_, kwds4IFFT, validate, verbose, opsN, /):
    _2N = N<<1
    zero7Rz = _mk_poly7Rz_(N, [zero]*N)
    if 0:config6en = ...
    def neg7Rz_(cs, /):
        return _Rz(map(neg_, cs))
    def add7Rz_(xs, ys, /):
        return _Rz(map(add_, xs, ys))
    def mul7Rz_(xs, ys, /):
        #bug:return _Rz(map(mul_, xs, ys))
        if type(xs) is _4z:
            g = xs
            return mul_g_xs7Rz_(g, ys)
        if type(ys) is _4z:
            g = ys
            return mul_g_xs7Rz_(g, xs)
        return poly_mul7Rz_(xs, ys)
    def sub7Rz_(xs, ys, /):
        return add7Rz_(xs, neg7Rz_(ys))
        return _Rz(map(lambda x,y:add_(x,neg_(y)), xs, ys))
    def pow_g7Rz_(g, e, /):
        check_type_is(_4z, g)
        e4g = int(g)
        # [z**e4g == g]
        # [z**new_e4g == new_g == g**e == z**(e4g*e)]
        # !! [z**N == -1]
        # [z**new_e4g == z**(e4g*e%(2*N))]
        # [new_e4g == e4g*e%(2*N)]
        new_e4g = e4g*e#% _2N
        return mk_g5e_(new_e4g)
    def mk_g5e_(new_e4g, /):
        new_e4g = new_e4g % _2N
        # [0 <= new_e4g < 2*N]
        if new_e4g > N:
            # [N < new_e4g < 2*N]
            new_e4g -= _2N
            # [-N < new_e4g < 0]
        else:
            # [0 <= new_e4g <= N]
            pass
        # [-N < new_e4g <= N]
        assert -N < new_e4g <= N
        new_e4g
        new_g = _4z(new_e4g)
        return new_g
    def mul_g_g7Rz_(g, h, /):
        check_type_is(_4z, g)
        check_type_is(_4z, h)
        e4g = int(g)
        e4h = int(h)
        #bug:new_e4g = e4g*e4h
        new_e4g = e4g+e4h
        return mk_g5e_(new_e4g)
    def mul_g_xs7Rz_(g, xs, /):
        if type(xs) is _4z:
            h = xs
            return mul_g_g7Rz_(g, h)
        assert len(xs) == N
        check_type_is(_4z, g)
        e4g = int(g)
        assert -N < e4g <= N
        # [-N < e4g <= N]
        if e4g == 0:
            # !! [z**0 == +1]
            return xs
        elif e4g == N:
            # !! [z**N == -1]
            return neg7Rz_(xs)
        elif e4g > 0:
            # [0 < e4g < N]
            xsL = xs[:-e4g]
            xsH = xs[-e4g:]
            ysL = map(neg_, xsH)
            ysH = xsL
        elif e4g < 0:
            # [-N < e4g < 0]
            xsL = xs[:-e4g]
            xsH = xs[-e4g:]
            ysL = xsH
            ysH = map(neg_, xsL)
        else:
            raise 000
        ys = _Rz(chain(ysL, ysH))
        return ys

    def poly_mul7Rz_(xs, ys, /):
        nonlocal config6en, poly_mul7Rz_
        config6en = opsN.ez4M2config_(en)
        poly_mul7Rz_ = _poly_mul7Rz_
        return poly_mul7Rz_(xs, ys)
        try:
            config6en
        except NameError:
            config6en = opsN.ez4M2config_(en)
    def _poly_mul7Rz_(xs, ys, /):
        check_type_is(_Rz, xs)
        check_type_is(_Rz, ys)
        assert len(xs) == N
        assert len(ys) == N
        # !! [z**N == -1]
        #ws = negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT_(mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero, en, xs, ys, min_ez4M4recur=min_ez4M4recur, FFT_=FFT_, kwds4FFT=kwds4FFT, IFFT_, kwds4IFFT, validate=False, verbose=verbose)
        ws = negacyclic_convolution__len_is_zpow__num_bits4len_eq__7symbolic_FFT__7config_(opsN, config6en, xs, ys) #, validate=False
        #if verbose:
        if validate:
            assert ws == negacyclic_convolution__len_eq__7native_(neg_, add_, mul_, N, xs, ys)
        return _Rz(ws)
    return (neg7Rz_, add7Rz_, mul7Rz_, pow_g7Rz_, sub7Rz_, zero7Rz, mk_g5e_)
def _mk_poly7Rz_(N, xs, /):
    # [mk_poly7Rz_ :: [R]{len==N} -> Rz]
    # [mk_poly7Rz_(xs) := sum[xs[i] * z**i | [i:<-[0..<N]]]]
    assert len(xs) == N
    return _Rz(xs)
def _mk_poly7Rzt_(M, N, W, xs, /):
    # [mk_poly7Rzt_ :: [R]{len==M} -> Rzt]
    # [mk_poly7Rzt_(xs) := sum[mk_poly7Rz_([xs[j] | [j:<-[0..<M]][j%W==k]]) * t**k | [k:<-[0..<W]]]]
    #
    # [@[xs ::[R]{len==M}] -> [mk_poly7Rzt_(xs) == sum[mk_poly7Rz_(xs[k::W]) * t**k | [k:<-[0..<W]]]]]
    # [@[xs ::[R]{len==M}] -> @[k:<-[0..<W]] -> [mk_poly7Rzt_(xs).coeffs[k] == mk_poly7Rz_(xs[k::W])]]
    assert len(xs) == M == N*W
    assert W <= N <= 2*W
    return _Rzt(_mk_poly7Rz_(N, xs[k::W]) for k in range(W))
class _4ez2div_zpow_(dict):
    'mk_div_zpow5ez_ -> ez2div_zpow_/{ez:(div_zpow_|inv_zpow)}'
    def __init__(sf, mk_div_zpow5ez_, /):
        #skip dict.__init__
        pass

    def __new__(cls, mk_div_zpow5ez_, /):
        if type(mk_div_zpow5ez_) is cls:
            sf = mk_div_zpow5ez_
        elif callable(mk_div_zpow5ez_):
            sf = super(__class__, cls).__new__(cls)
            super(__class__, cls).__init__(sf)
            sf._mk = mk_div_zpow5ez_
        elif hasattr(mk_div_zpow5ez_, '__getitem__'):
            sf = mk_div_zpow5ez_
        else:
            raise TypeError(type(mk_div_zpow5ez_))
        return sf
    def __call__(sf, ez, /):
        return sf[ez]
    def __missing__(sf, ez, /):
        sf[ez] = sf._mk(ez)
        return sf[ez]
def _prepare4mod_odd4symbolic_DFT_(odd_modulus, /):
    if not odd_modulus&1:raise TypeError(odd_modulus)
    return _prepare4mod_uint4symbolic_DFT_(odd_modulus)
def _prepare4mod_uint4symbolic_DFT_(modulus, /):
    check_int_ge(0, modulus)
    if modulus == 0:
        return _prepare4ring_ZZ4symbolic_DFT_()
    (ez, odd) = factor_pint_out_power_of_base_(2, modulus)
    hremR_ = mk_hrem_(modulus)
    @_4ez2div_zpow_
    def mk_div_zpow5ez_(em, /):
        if ez == 0:
            M = 1<<em
            invM = pow(M, -1, odd)
            return hremR_(invM)
            return invM
        e = min(ez, em)
        H = odd<<(ez-e)
        hremH_ = mk_hrem_(H)
        vz = pow(1<<(em-e), -1, H)
        vz = hremH_(vz)
        def div_M_(x, /):
            # [x =[%(odd*2**ez)]= y*2**em]
            # !! [e := min(ez, em)]
            # [x =[%(2**e)]= y*2**em =[%(2**e)]= 0]
            v = x >> e
            if not x == v<<e:raise ValueError(x, v, em)
            # [v*2**e =[%(odd*2**ez)]= y*2**em]
            # [v =[%(odd*2**(ez-e))]= y*2**(em-e)]
            # [v*inv_(2**(em-e)) =[%(odd*2**(ez-e))]= y]
            #y = v*vz %modulus
            #y = v*vz%H
            #y = hremR_(v*vz)
            y = hremH_(v*vz)
            return y
        return div_M_

    def neg_(x, /):
        return hremR_(-x)
        return (-x)%modulus
    def add_(x, y, /):
        return hremR_(x+y)
        return (x+y)%modulus
    def mul_(x, y, /):
        return hremR_(x*y)
        return (x*y)%modulus
    mk5int_ = hremR_
    zero = 0
    return (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero)

def _prepare4ring_ZZ4symbolic_DFT_():
    @_4ez2div_zpow_
    def mk_div_zpow5ez_(em, /):
        def div_M_(i, /):
            j = i >> em
            if not i == j<<em:raise ValueError(i, j, em)
            return j
        return div_M_
    def neg_(x, /):
        return (-x)
    def add_(x, y, /):
        return (x+y)
    def mul_(x, y, /):
        return (x*y)
    mk5int_ = int
    zero = 0
    return (mk_div_zpow5ez_, neg_, add_, mul_, mk5int_, zero)

def _prepare4mod_uint4FFT_(modulus, ground_root, mul_order4ground_root,/):
    #mk5modulus_and_ground_root_
    check_int_ge(0, modulus)
    check_type_is(int, ground_root)
    check_int_ge(1, mul_order4ground_root)
    if modulus == 0:
        assert abs(ground_root) == 1
        assert 1 <= mul_order4ground_root <= 2
        assert ground_root+2*mul_order4ground_root == 3
        (_, neg_, add_, mul_, mk5int_, zero) = _prepare4ring_ZZ4symbolic_DFT_()
        @_4sz2div_sz_
        def mk_div_sz5sz_(sz, /):
            def div_sz_(x, /):
                y = x//sz
                if not x == y*sz:raise ValueError(x, y, sz)
                return y
            return div_sz_
        def pow4g_(g, e, /):
            if not g == ground_root:raise ValueError(g, ground_root)
            return g if e&1 else 1
        mk_div_sz5sz_
        return (neg_, add_, mul_, pow4g_, mk_div_sz5sz_, mk5int_, zero, ground_root)
    hremR_ = mk_hrem_(modulus)
    ground_root = hremR_(ground_root)
    @_4sz2div_sz_
    def mk_div_sz5sz_(sz, /):
        #TODO:from seed.math.mk_perfect_div_mod_ import mk_perfect_div_mod_
        GCD = gcd(modulus, sz)
        if GCD == 1:
            inv4sz = pow(sz, -1, modulus)
            return hremR_(inv4sz)
            return inv4sz
        H = modulus//GCD
        hremH_ = mk_hrem_(H)
        vz = pow(sz//GCD, -1, H)
        vz = hremH_(vz)
        def div_sz_(x, /):
            # [x =[%modulus]= y*sz]
            # [x =[%(H*GCD)]= y*sz]
            # [x =[%GCD]= y*sz =[%GCD]= 0]
            v = x //GCD
            if not x == v*GCD:raise ValueError(x, v, sz)
            # [v*GCD =[%(H*GCD)]= y*sz]
            # [v =[%H]= y*(sz//GCD)]
            # [v*inv_(sz//GCD) =[%H]= y]
            y = hremH_(v*vz)
            return y
        return div_sz_

    def neg_(x, /):
        return hremR_(-x)
        return (-x)%modulus
    def add_(x, y, /):
        return hremR_(x+y)
        return (x+y)%modulus
    def mul_(x, y, /):
        return hremR_(x*y)
        return (x*y)%modulus
    inv_ground_root = pow(ground_root, -1, modulus)
    hremE_ = mk_hrem_(mul_order4ground_root)
    def pow4g_(g, e, /):
        if not g == ground_root:raise ValueError(g, ground_root)
        # [g == ground_root]
        e = hremE_(e)
        if e < 0:
            # !! [g == ground_root]
            inv_g = inv_ground_root
            r = pow(inv_g, -e, modulus)
        else:
            r = pow(g, e, modulus)
        return hremR_(r)
    pow4g_
    mk5int_ = hremR_
    zero = 0
    return (neg_, add_, mul_, pow4g_, mk_div_sz5sz_, mk5int_, zero, ground_root)




__all__
from seed.algo.FFT.convolution import cyclic_convolution__len_eq__7FFT_, cyclic_convolution__len_eq__7native_
from seed.algo.FFT.convolution import dyadic_operator_, sum0_, sum1_

from seed.algo.FFT.convolution import mk_ops4convolution7symbolic_FFT__5modulus_
    ######################
    #:####################
    #:###recur:
    #:opsN.negacyclic_convolution__num_bits4len_eq__7recur_(ez4M, xs, ys)
    #:opsN.cyclic_convolution__num_bits4len_eq__7recur_(ez4M, xs, ys)
    #:
    #:####################
    #:###zero_padding:
    #:opsN.cyclic_convolution__num_bits4len_eq__7zero_pad_(ez4M, xs, ys)
    #:opsN.bothcyclic_convolution__num_bits4len_eq__7zero_pad_(ez4M, xs, ys)
    #:opsN.acyclic_convolution__num_bits4lenO_eq__7zero_pad_(1+ez4M, xs, ys)
    #:
    #:####################
    #:###native:
    #:opsN.negacyclic_convolution__len_eq__7native_(1<<ez4M, xs, ys)
    #:opsN.cyclic_convolution__len_eq__7native_(1<<ez4M, xs, ys)
    #:opsN.acyclic_convolution__lenO_eq__7native_(1<<(1+ez4M), xs, ys)
    #:####################
    #:###common:
    #:opsN.neg_,add_,mul_,mk5int_,zero,one,neg_one
    #:opsN.cyclic_convolution__7commonAPI_(xs, ys)
    #:opsN.acyclic_convolution__7commonAPI_(xs, ys)
    #:opsN.negacyclic_convolution__7commonAPI_(xs, ys)
    ######################
from seed.algo.FFT.convolution import mk_ops4convolution7FFT__5modulus_and_ground_root_
    #:opsG.neg_,add_,mul_,mk5int_,zero,one,neg_one
    #:opsG.cyclic_convolution__7commonAPI_(xs, ys)
    #:opsG.acyclic_convolution__7commonAPI_(xs, ys)



from seed.algo.FFT.convolution import *
