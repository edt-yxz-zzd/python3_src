#__all__:goto
r'''[[[
e ../../python3_src/seed/math/polynomial/eval_polynomial/eval_polynomial_on_geometric_progression.py
view ../../python3_src/seed/algo/FFT/FFT.py
view ../../python3_src/seed/algo/FFT/index_scramble4FFT.py
view ../../python3_src/seed/algo/FFT/convolution.py


seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression
py -m nn_ns.app.debug_cmd   seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression:__doc__ -ht # -ff -df
py -m nn_ns.app.doctest_cmd seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression:__doc__ -ht # -ff -df
#######

[[
源起:
分解整数:idea:
===
@20260607
多驻点:x0*(1+a*fff(zs;x0))
  [fff(zs;x) == II[(x-z) | [z:<-zs]]]
大面积覆盖:
采用:
  [hhh(N;x) == II[(x-z) | [z:<-[0..<N]]]]
  [ggg(N;x) == II[(x-z) | [z:<-[0..<N**2]]]]
  [ggg(N;x) == II[hhh(N;x+z*N) | [z:<-[0..<N**2]]]]
  相当于:
    先:多项式hhh(N;x)求值于range(x,x+N**2,N)
    再:累积所有输出
===
@20260611
批量差积:计算冫积纟整个集合的任意俩不同元素的差:(*-*)
  [f(xs) := II[(a-b) | [a,b:<-xs][a=!=b]] %M]
  [ff(xs,ys) := II[(a-b) | [a:<-xs][b:<-ys][a=!=b]] %M]
  可以通过 多项式求值 实现快速算法！
    f(xs):分治:f(xsL),f(xsR)，再结合:ff(xsL,xsR)
    ff(xs,ys): 多项式 II[(X-b) | [b:<-ys]] 在 xs 上 求值
  * 随机生成集合
    生日悖论=>O(p**/2)
  * {B**j}
    不同层次的j
    [xs := {c**i | [i:<-[0..<K0]]}]
    [ys := {c**Kb*(c**Ke)**j | [j:<-[0..<K1]]}]
    [(ys *-* xs) %M
    == II[(c**Kb*(c**Ke)**j -c**i) | [i:<-[0..<K0]][j:<-[0..<K1]]] %M
    == II[(c**(Kb+Ke*j-i) -1)*c**i | [i:<-[0..<K0]][j:<-[0..<K1]]] %M
    ]
    [K == Ke == K0 == K1][Kb==0]:
        [M%p==0][order_mod_(p;c) < K**2] => [gcd(M,(ys *-* xs) %M) %p == 0]
          但若[p==1+2*q]则要求[K==O(p**/2)]
    [K == Ke == K0 == K1][Kb==Ku*K**2]:
        [M%p==0][Ku*K**2 <= order_mod_(p;c) < (1+Ku)*K**2] => [gcd(M,(ys *-* xs) %M) %p == 0]
          #增量搜索...内存限制
          #随机搜索...内存限制
  * {A**i} - {B**j}
    [(A**i-B**j) %p == 0]概率多大？
  * {h(b,c;i)} - {B**j}
    [h(b,c,0) := c]
    [h(b,c,1+i) := (b+h(b,c;i)**2)]
===
polynomial_evaluation
view others/数学/polynomial/polynomial_evaluation.txt
    Algorithm__9_6_6
    evaluation of polynomial on geometric progression
]]
[[
@20260608
zpow.g:行不通！
    见下面:_ws8 == [75391]*256

@20260611
但现在使用opsN，不再需要g！
e ../../python3_src/seed/math/factor_pint/factor_pint__7batch_gcd_IIdiffs.py
]]



'#'; __doc__ = r'#'
>>> from seed.algo.FFT.FFT import FFT__ping_pong

    #def FFT__ping_pong(neg_, add_, mul_, g, xs, /, *, may_radixes=None, scramble_=None, may_gs=None, may_ys=None):
>>> from seed.algo.FFT.index_scramble4FFT import IFFT_, FFT__idx_digit_reverse

    #def IFFT_(FFT_, neg_, add_, mul_, inv_g, inv4sz, xs, /, *, extra_args=(), may_gs=None, may_inv_gs=None, **kwds):
>>> from seed.algo.FFT.index_scramble4FFT import _prepare4mod_zpow_

    #def _prepare4mod_zpow_(ez4modulus, ez4sz, /):
    #    -> (neg_, add_, mul_, g, inv_g, sz, div_len_, may_radixes)
>>> from seed.algo.FFT.index_scramble4FFT import _prepare4mod_prime_

    #def _prepare4mod_prime_(modulus, g, sz=None, /):
    #    -> (neg_, add_, mul_, g, inv_g, sz, inv4sz, may_radixes)
>>> from seed.algo.FFT.convolution import dyadic_operator_




>>> from seed.algo.FFT.convolution import cyclic_convolution__len_eq__7FFT_, cyclic_convolution__len_eq__7native_

>>> (neg_, add_, mul_, g, inv_g, sz, div_sz_, may_radixes) = _prepare4mod_zpow_(16, 8) # (ez4modulus, ez4sz)
>>> xs = [*range(2, 2+5*sz, 5)]
>>> DFT4xs = FFT__ping_pong(neg_, add_, mul_, g, xs)
>>> _xs = IFFT_(FFT__ping_pong, neg_, add_, mul_, inv_g, div_sz_, DFT4xs)
>>> len(_xs) == len(DFT4xs) == len(xs) == sz == 256
True
>>> _xs == xs  # fail!!!
False


>>> ys = [*range(7, 7+3*sz, 3)]
>>> DFT4ys = FFT__ping_pong(neg_, add_, mul_, g, xs)
>>> DFT4ws = dyadic_operator_(mul_, DFT4xs, DFT4ys)
>>> ws = IFFT_(FFT__ping_pong, neg_, add_, mul_, inv_g, div_sz_, DFT4ws)
>>> _ws = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, div_sz_, sz, xs, ys)
>>> len(_ws) == len(DFT4ws) == len(ws) == 256
True
>>> _ws == ws
True


>>> (neg_, add_, mul_, g, inv_g, sz, inv4sz, may_radixes) = _prepare4mod_prime_(modulus:=1+2**16, pow(3, 256, modulus), 256)
>>> _ws_ = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, inv4sz, sz, xs, ys)
>>> _ws_ == ws
False

>>> not any(ws)
True
>>> _ws_    #doctest: +ELLIPSIS
[29804, 56805, 14429, ..., 14429, 56805, 29804, 64500]


>>> N = -1+2**17
>>> G = +1+2**16
>>> (neg_, add_, mul_, g, inv_g, sz, inv4sz, may_radixes) = _prepare4mod_prime_(modulus:=1+2**256, 4, 256) #not prime
>>> _ws2 = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, inv4sz, sz, xs, ys)
>>> _ws_ == _ws2
False
>>> _ws2  #doctest: +ELLIPSIS
[43284224, 43769984, 44251904, ..., 44729984, 44251904, 43769984, 43284224, 42794624]
>>> _ws0 = cyclic_convolution__len_eq__7native_(add_, mul_, sz, xs, ys)
>>> _ws0 == _ws2
True
>>> _ws_ == [u%G for u in _ws0]
True

>>> (neg_, add_, mul_, g, inv_g, sz, inv4sz, may_radixes) = _prepare4mod_prime_(modulus:=1+2**128, 2, 256) #not prime
>>> _ws3 = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, inv4sz, sz, xs, ys)
>>> _ws3 == _ws2
True

>>> (neg_, add_, mul_, g, inv_g, sz, inv4sz, may_radixes) = _prepare4mod_prime_(modulus:=1+2**512, 16, 256) #not prime
>>> _ws6 = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, inv4sz, sz, xs, ys)
>>> _ws6 == _ws2
True


不一致，应当是由于FFT算法内部使用了neg_()，而其结果与pow(g, sz//2, modulus)不一致
>>> (neg_, add_, mul_, g, inv_g, sz, inv4sz, may_radixes) = _prepare4mod_prime_(modulus:=-1+2**256, 2, 256, no_neg_one_ok=True) #not prime
>>> _ws4 = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, inv4sz, sz, xs, ys)
>>> _ws4 == _ws2
False
>>> _ws4  #doctest: +ELLIPSIS
[86992881756140888128335894554634538561511692025502639676866878352288124610536, ..., 86992881756140888128335894554634538561511692025502639676866878352288124610536, 61443909234216866497967250522169146222841596362783601331525665895751215350316]

>>> (neg_, add_, mul_, g, inv_g, sz, inv4sz, may_radixes) = _prepare4mod_prime_(modulus:=-1+2**512, 4, 256, no_neg_one_ok=True) #not prime
>>> _ws5 = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, inv4sz, sz, xs, ys)
>>> _ws5 == _ws2
False
>>> _ws5 == _ws4
False
>>> _ws5  #doctest: +ELLIPSIS
[7755338182400458254418796474185736358029576516492572510441301930614423689061968064662695534018270552914273711203084746854191980998322124557360555947734827, ..., 4796969276220092534672858992081142653683472059939805745146128008574805855273407047861609711364445205580496879909300272699447261091523094962949902477333807]





#>>> from seed.math.Chinese_Remainder_Theorem import apply_CRT__pairs
>>> N = -1+2**17
>>> G = +1+2**16
>>> NG = N*G
>>> g6G = pow(3, 256, G)
>>> g6N = 1

#>>> g6NG = apply_CRT__pairs([(N,g6N), (G,g6G)], extended=False)
>>> g6NG = 2851056393
>>> g6NG%NG == g6NG
True
>>> g6NG%N == g6N
True
>>> g6NG%G == g6G
True
>>> (neg_, add_, mul_, g, inv_g, sz, inv4sz, may_radixes) = _prepare4mod_prime_(modulus:=NG, g6NG, 256, no_neg_one_ok=True)
>>> _ws7 = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, inv4sz, sz, xs, ys)
>>> _ws_ == _ws7
False
>>> _ws7  #doctest: +ELLIPSIS
[7718453368, 3675437302, 8390192243, 4682717937, ..., 8390192243, 3675437302, 7718453368, 3339240187]
>>> _ws9 = [u%G for u in _ws7]
>>> _ws_ == _ws9
True

>>> _ws8 = [u%N for u in _ws7]
>>> _ws_ == _ws8
False
>>> _ws8 == [75391]*256
True
>>> sum([u%N for u in _ws0])%N
75391
>>> sum([u%N for u in _ws0])%N*pow(sz,-1,N)%N
65318
>>> sum([u%N for u in _ws0])%N*sz%N
32659





def poly_evals__on_geometric_progression__7native_(add_, mul_, zero, one, coeffs8poly, T, sz=None, /):
xxx:def eval_polynomial_on_geometric_progression__7FFT_(neg_, add_, mul_, zero, one, div_gM_, gM, g, inv_g, coeffs8poly, T, invT, /):
def eval_polynomial_on_geometric_progression__7opsX_(opsX, coeffs8poly, T, invT, /):

>>> (neg_, add_, mul_, g, inv_g, sz, inv4sz, may_radixes) = _prepare4mod_prime_(modulus:=1+2**128, 2, 256) #not prime
>>> zero, one = 0, 1
>>> T = 999
>>> invT = pow(T, -1, modulus)
>>> D = sz//2
>>> coeffs8poly = range(-56, -56+D)
>>> rs0 = poly_evals__on_geometric_progression__7native_(add_, mul_, zero, one, coeffs8poly, T, D)
>>> #rs1 = eval_polynomial_on_geometric_progression__7FFT_(neg_, add_, mul_, zero, one, inv4sz, gM:=sz, g, inv_g, coeffs8poly, T, invT)
>>> opsN = mk_ops4convolution7symbolic_FFT__5modulus_(modulus)
>>> rs3 = eval_polynomial_on_geometric_progression__7opsX_(opsN, coeffs8poly, T, invT)
>>> rs1 = [u%modulus for u in rs3]
>>> rs1 == rs0
True
>>> rs1  #doctest: +ELLIPSIS
[960, 222127915846752330184403282032556711149, ..., 287181346753101126459978715807575435981, 291707318287887882537969425177217818321, 339571985052737931669852608330042583264]
>>> opsG = mk_ops4convolution7FFT__5modulus_and_ground_root_(modulus, g, gM:=sz)
>>> rs5 = eval_polynomial_on_geometric_progression__7opsX_(opsG, coeffs8poly, T, invT)
>>> _rs1 = [u%modulus for u in rs5]
>>> _rs1 == rs1
True



>>> rs7 = eval_polynomial_on_geometric_progression__7modulus_(modulus, coeffs8poly, T, hrem_vs_mod=True)
>>> rs7 == rs0
True



>>> eval_polynomial_on_geometric_progression__7modulus_(0, [1,0,0,3], 2)
Traceback (most recent call last):
    ...
TypeError: 0

[4, 25, 193, 1537]
>>> eval_polynomial_on_geometric_progression__7modulus_(257, [1,0,0,3], 2)
[4, 25, -64, -5]
>>> eval_polynomial_on_geometric_progression__7modulus_(257, [1,0,0,3], 2, hrem_vs_mod=True)
[4, 25, 193, 252]
>>> eval_polynomial_on_geometric_progression__7modulus_(1+2*1537, [1,0,0,3], 2)
[4, 25, 193, 1537]
>>> eval_polynomial_on_geometric_progression__7modulus_(1539, [1,0,0,3], 2, hrem_vs_mod=True)
[4, 25, 193, 1537]





py_adhoc_call   seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression   ,iter_geometric_progression_ =int.__mul__ =1 =2 | more
    1
    2
    4
    8
    ...

py_adhoc_call   seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression   @eval_polynomial_on_geometric_progression__7modulus_ ='257' ='[1,0,0,3]' =2
    [4, 25, -64, -5]
py_adhoc_call   seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression   @eval_polynomial_on_geometric_progression__7modulus_ ='257' ='[1,0,0,3]' =2 +hrem_vs_mod
    [4, 25, 193, 252]
py_adhoc_call   seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression   @poly_evals__on_geometric_progression__7native_ =int.__add__ =int.__mul__ =0 =1 ='[1,0,0,3]' =2
    [4, 25, 193, 1537]
    [1+0+0+3*(2**0)**3 == 4]
    [1+0+0+3*(2**1)**3 == 1+3*8 == 25]
    [1+0+0+3*(2**2)**3 == 1+3*4**3 == 1+3*64 == 1+192 == 193]
    [1+0+0+3*(2**3)**3 == 1+3*8**3 == 1+3*512 == 1537]
py_adhoc_call   seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression   @poly_eval_ =int.__add__ =int.__mul__ =0 ='[1,0,0,3]' =2
    25


py_adhoc_call   seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression   ,eval_polynomial_on_geometric_progression__7modulus_

]]]'''#'''
__all__ = r'''
Eval_polynomial_on_geometric_progression__7modulus
eval_polynomial_on_geometric_progression__7modulus_
    eval_polynomial_on_geometric_progression__7opsX_
        triangular_number_
            tab_pows_
            tab_tri_pows_


poly_eval_
    iter_poly_evals__7native_
    poly_evals__7native_
iter_poly_evals__on_geometric_progression__7native_
    iter_geometric_progression_
    poly_evals__on_geometric_progression__7native_


'''.split()#'''
    #eval_polynomial_on_geometric_progression__7FFT_
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.floor_ceil_tools.fc_log import floor_log2, ceil_log2
    from seed.tiny_.check import check_type_is, check_int_ge

    #from seed.algo.FFT.convolution import cyclic_convolution__len_eq__7FFT_, cyclic_convolution__len_eq__7native_
    from seed.algo.FFT.convolution import mk_ops4convolution7symbolic_FFT__5modulus_
    from seed.algo.FFT.convolution import mk_ops4convolution7FFT__5modulus_and_ground_root_
    from seed.algo.FFT.convolution import dyadic_operator_

    from itertools import islice
    from functools import reduce

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def triangular_number_(i, /):
    # [triangular_number_(i) == i*(i+1)///2]
    return i*(i+1)//2
def tab_pows_(sz, mul_, one, T, /):
    pw = one # == pow_(T, 0)
    j2Tpw = [pw]
        # j:pow_(T, j)
    for j in range(1, sz):
        pw = mul_(pw, T)
        j2Tpw.append(pw)
    assert len(j2Tpw) == sz
    return j2Tpw
def tab_tri_pows_(sz, mul_, one, T, /, *, ex=False):
    j2Tpw = tab_pows_(sz, mul_, one, T)
        # j:pow_(T, j)

    trpw = one # == pow_(T, triangular_number_(0))
    j2Ttrpw = [trpw]
        # j:pow_(T, triangular_number_(j))
    for j in range(1, sz):
        # !! [(j*(j+1) -(j-1)*j)/2 == j]
        delta_exp = j # == triangular_number_(j) -triangular_number_(j-1)
        delta_trpw = j2Tpw[delta_exp]
        trpw = mul_(trpw, delta_trpw)
        j2Ttrpw.append(trpw)
    return j2Ttrpw if not ex else (j2Ttrpw, j2Tpw)


def poly_eval_(add_, mul_, zero, coeffs8poly, x, /):
    y = zero
    for c in reversed(coeffs8poly):
        y = add_(mul_(y, x), c)
    return y
def iter_poly_evals__7native_(add_, mul_, zero, coeffs8poly, xs, /):
    for x in xs:
        y = poly_eval_(add_, mul_, zero, coeffs8poly, x)
        yield y
def poly_evals__7native_(add_, mul_, zero, coeffs8poly, xs, /):
    return [*iter_poly_evals__7native_(add_, mul_, zero, coeffs8poly, xs)]

def iter_geometric_progression_(mul_, B, T, /):
    x = B
    while 1:
        yield x
        x = mul_(x, T)
def iter_poly_evals__on_geometric_progression__7native_(add_, mul_, zero, B, coeffs8poly, T, /):
    xs = iter_geometric_progression_(mul_, B, T)
    return iter_poly_evals__7native_(add_, mul_, zero, coeffs8poly, xs)
def poly_evals__on_geometric_progression__7native_(add_, mul_, zero, B, coeffs8poly, T, sz=None, /):
    if sz is None:
        sz = len(coeffs8poly)
    ys = iter_poly_evals__on_geometric_progression__7native_(add_, mul_, zero, B, coeffs8poly, T)
    ys = islice(ys, 0, sz)
    return [*ys]

#:def eval_polynomial_on_geometric_progression__7FFT_(neg_, add_, mul_, zero, one, div_gM_, gM, g, inv_g, coeffs8poly, T, invT, /):
#:    'neg_/(x->x) -> add_/(x->x->x) -> mul_/(x->x->x) -> zero/x -> one/x -> div_gM_/(x|(x->x)) -> gM/uint -> g/x -> inv_g/x -> cs/[x] -> T/x -> invT/x -> ys/[x]{len==len(cs)}  # [mul_order_(mul_;g) == gM == 2**(1 +ceil_log2(len(cs)))][T*invT==one] # [ys[k] == poly_eval_(cs;(T**k)) == sum[cs[j]*(T**k)**j | [j :<- [0..<len(cs)]]]]'
#:    # -> pow_/(x->uint->x)
#:    check_int_ge(1, gM)
#:    cs = coeffs8poly
#:    D = len(cs)
#:    (M, H) = _mk_M_H(D)
#:    if not gM == M:raise ValueError(gM, M, len(coeffs8poly))
#:    opsG = Ops4convolution7FFT(neg_, add_, mul_, pow4g_, mk_div_sz5sz_, mk5int_, zero, ground_root, mul_order4ground_root)
#:    return eval_polynomial_on_geometric_progression__7opsX_(opsG, coeffs8poly, T, invT)
def _mk_M_H(D, /):
    # n = D
    m = 1 +ceil_log2(D)
    M = 1 << m
    H = 1 << (m-1)
    assert D <= H < 2*D <= 2*H == M < 4*D, (D, H, 2*D, M, 4*D)
    return (M, H)


class _Readonly:
    def __delattr__(sf, nm, /):
        raise AttributeError(nm)
    def __setattr__(sf, nm, x, /):
        if hasattr(sf, nm):
            raise AttributeError(nm)
        super(__class__, sf).__setattr__(nm, x)
class Eval_polynomial_on_geometric_progression__7modulus(_Readonly):
    def __init__(sf, modulus, /, *, hrem_vs_mod, optimized6zpowpp):
        check_type_is(bool, hrem_vs_mod)
        check_int_ge(1, modulus)
            # !! invT
        opsN = mk_ops4convolution7symbolic_FFT__5modulus_(modulus)
        sf.modulus = modulus
        sf.opsN = opsN
        sf.hrem_vs_mod = hrem_vs_mod
        sf.optimized6zpowpp = optimized6zpowpp
    def evals_(sf, coeffs8poly, T, invT=None, /, *, hrem_vs_mod=None, optimized6zpowpp=None):
        if hrem_vs_mod is None:
            hrem_vs_mod = sf.hrem_vs_mod
        if optimized6zpowpp is None:
            optimized6zpowpp = sf.optimized6zpowpp

        opsN = sf.opsN
        modulus = sf.modulus
        if invT is None:
            invT = pow(T, -1, modulus)
        rs = eval_polynomial_on_geometric_progression__7opsX_(opsN, coeffs8poly, T, invT, optimized6zpowpp=optimized6zpowpp)
        if hrem_vs_mod and modulus:
            #rs = [u%modulus for u in rs]
            rs = [u+modulus if u < 0 else u for u in rs]
        return rs
def eval_polynomial_on_geometric_progression__7modulus_(modulus, coeffs8poly, T, invT=None, /, *, hrem_vs_mod=False):
    return Eval_polynomial_on_geometric_progression__7modulus(modulus, hrem_vs_mod=hrem_vs_mod).evals_(coeffs8poly, T, invT)

    #.check_int_ge(1, modulus)
    #.    # !! invT
    #.if invT is None:
    #.    invT = pow(T, -1, modulus)
    #.opsN = mk_ops4convolution7symbolic_FFT__5modulus_(modulus)
    #.rs = eval_polynomial_on_geometric_progression__7opsX_(opsN, coeffs8poly, T, invT)
    #.if hrem_vs_mod and modulus:
    #.    #rs = [u%modulus for u in rs]
    #.    rs = [u+modulus if u < 0 else u for u in rs]
    #.return rs
def eval_polynomial_on_geometric_progression__7opsX_(opsX, coeffs8poly, T, invT, /, *, optimized6zpowpp=False):
    r'''[[[
    #########
    # [opsX == (opsG|opsN)]
    # [opsX :: (Ops4convolution7FFT|Ops4convolution7symbolic_FFT)]
    #########
    [optimized6zpowpp:=True][len(cs) == 1+2**ez]:
        [Ts := T **. [0..<1+2**ez]]
        [this_func(cs,T)
        == poly_evals_(cs,Ts)
        == cs[0] +. (Ts .*. poly_evals_(cs[1:],Ts))
        == [poly_eval_(cs,T**0)] ++ (cs[0] +. (Ts .*. poly_evals_(cs[1:],Ts)))[1:]
        == [sum(cs)] ++ (cs[0] +. (Ts[1:] .*. poly_evals_(cs[1:],Ts[1:])))
        == [sum(cs)] ++ (cs[0] +. (T*Ts[:-1] .*. poly_evals_(cs[1:],T*Ts[:-1])))
        == [sum(cs)] ++ (cs[0] +. (T*Ts[:-1] .*. poly_evals_(Ts[:-1] .*. cs[1:],Ts[:-1])))
        == [sum(cs)] ++ (cs[0] +. (Ts[:-1] .*. poly_evals_(Ts[1:] .*. cs[1:],Ts[:-1])))
        == [sum(cs)] ++ (cs[0] +. (Ts[:-1] .*. this_func((Ts .*. cs)[1:],T)))
        ]
        [this_func(cs,T) == [sum(cs)] ++ (cs[0] +. (Ts[:-1] .*. this_func((Ts .*. cs)[1:],T)))]

    #]]]'''#'''
    mul_ = opsX.mul_
    zero = opsX.zero
    one = opsX.one
    #########
    cs = coeffs8poly
    D = len(cs)
    #########
    ex = False
    if optimized6zpowpp and D.bit_length():
        optimized6zpowpp = False
        lbD = floor_log2(D)
        if D - 1 == 1 << lbD:
            optimized6zpowpp = True
            # [len(cs) == D == 1+2**lbD]
            # apply:[this_func(cs,T) == [sum(cs)] ++ (cs[0] +. (Ts[:-1] .*. this_func((Ts .*. cs)[1:],T)))]
            c0 = cs[0]
            add_ = opsX.add_
            sum_cs = reduce(add_, cs, zero)
            ex=True
            (j2Ttrpw, j2Tpw) = tab_tri_pows_(D, mul_, one, T, ex=ex)
            Ts = j2Tpw
            cs = dyadic_operator_(mul_, Ts, cs)[1:]
            D = len(cs)
            assert D == 1 << lbD
    #########
    ex, optimized6zpowpp, cs
    (M, H) = _mk_M_H(D)
    #########
    if not ex:
        j2Ttrpw = tab_tri_pows_(D, mul_, one, T)
        # j:pow_(T, triangular_number_(j))
    # [us := [(cj*T**triangular_number_(j)) | [(j,cj):<-enumerate(cs)]] ++ [0]*(M-D)]
    us = [mul_(cs[j], j2Ttrpw[j]) for j in range(D)]
    777;us += [zero]*(M-D)
    assert len(us) == M


    # [vs := [((T**-1)**triangular_number_(M///2-j-1)) | [j:<-[0..<M]]]]
    # vs对称:
    # [triangular_number_(M///2-0-1) == (M/2-1)*(M/2)/2 == (M-2)*M/8]
    # [triangular_number_(M///2-(M-1)-1) == (-M/2)*(-M/2+1)/2 == (M-2)*M/8 == triangular_number_(M///2-0-1)]
    # [triangular_number_(M///2-(M/2-1)-1) == (0)*(0+1)/2 == 0]
    # [triangular_number_(M///2-(M/2)-1) == (-1)*(-1+1)/2 == 0]
    j2vTtrpw = tab_tri_pows_(H, mul_, one, invT)
        # j:pow_(invT, triangular_number_(j))
    vs = j2vTtrpw[::-1]
    777;vs += j2vTtrpw
    assert len(vs) == M



    us, vs
    #ws = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, inv_g, div_gM_, M, us, vs)
    ws = opsX.cyclic_convolution__7commonAPI_(us, vs)
    # [j2y[:D] := [(T**triangular_number_(-1+k) * ws[M///2+k-1]) | [k:<-[0..<D]]]]
    ys = j2y = [mul_(ws[H+kmm], j2Ttrpw[max(0,kmm)]) for kmm in range(-1, -1+D)]
    assert len(ys) == D
    #########
    if optimized6zpowpp:
        # apply:[this_func(cs,T) == [sum(cs)] ++ (cs[0] +. (Ts[:-1] .*. this_func((Ts .*. cs)[1:],T)))]
        c0
        sum_cs
        Ts.pop()
        assert len(Ts) == D
        _ys = [sum_cs]
        _ys.extend(add_(c0, y) for y in map(mul_, Ts, ys))
        ys = _ys
        assert len(ys) == 1+D
    #########
    return ys


__all__
from seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression import Eval_polynomial_on_geometric_progression__7modulus, eval_polynomial_on_geometric_progression__7modulus_, eval_polynomial_on_geometric_progression__7opsX_
    # Eval_polynomial_on_geometric_progression__7modulus(modulus, hrem_vs_mod=hrem_vs_mod).evals_(coeffs8poly, T, invT)
from seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression import iter_geometric_progression_
    #def iter_geometric_progression_(mul_, B, T, /):
from seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression import *
