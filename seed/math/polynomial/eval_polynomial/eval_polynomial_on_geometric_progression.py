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
polynomial_evaluation
view others/数学/polynomial/polynomial_evaluation.txt
    Algorithm__9_6_6
    evaluation of polynomial on geometric progression
]]
[[
似乎行不通！
见下面:_ws8 == [75391]*256
]]



'#'; __doc__ = r'#'
>>> from seed.algo.FFT.FFT import FFT__ping_pong

    #def FFT__ping_pong(neg_, add_, mul_, g, xs, /, *, may_radixes=None, scramble_=None, may_gs=None, may_ys=None):
>>> from seed.algo.FFT.index_scramble4FFT import IFFT_, FFT__idx_digit_reverse

    #def IFFT_(FFT_, neg_, add_, mul_, inv_g, inv_len, xs, /, *, extra_args=(), may_gs=None, may_inv_gs=None, **kwds):
>>> from seed.algo.FFT.index_scramble4FFT import _prepare4mod_zpow_

    #def _prepare4mod_zpow_(ez4modulus, ez4sz, /):
    #    -> (neg_, add_, mul_, g, inv_g, sz, div_len_, may_radixes)
>>> from seed.algo.FFT.index_scramble4FFT import _prepare4mod_prime_

    #def _prepare4mod_prime_(modulus, g, sz=None, /):
    #    -> (neg_, add_, mul_, g, inv_g, sz, inv_len, may_radixes)
>>> from seed.algo.FFT.convolution import dyadic_operator_





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
>>> _ws = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, sz, inv_g, div_sz_, xs, ys)
>>> len(_ws) == len(DFT4ws) == len(ws) == 256
True
>>> _ws == ws
True


>>> (neg_, add_, mul_, g, inv_g, sz, inv_len, may_radixes) = _prepare4mod_prime_(modulus:=1+2**16, pow(3, 256, modulus), 256)
>>> _ws_ = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, sz, inv_g, inv_len, xs, ys)
>>> _ws_ == ws
False

>>> not any(ws)
True
>>> _ws_    #doctest: +ELLIPSIS
[29804, 56805, 14429, ..., 14429, 56805, 29804, 64500]


>>> N = -1+2**17
>>> G = +1+2**16
>>> (neg_, add_, mul_, g, inv_g, sz, inv_len, may_radixes) = _prepare4mod_prime_(modulus:=1+2**256, 4, 256) #not prime
>>> _ws2 = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, sz, inv_g, inv_len, xs, ys)
>>> _ws_ == _ws2
False
>>> _ws2  #doctest: +ELLIPSIS
[43284224, 43769984, 44251904, ..., 44729984, 44251904, 43769984, 43284224, 42794624]
>>> _ws0 = cyclic_convolution__len_eq__7native_(add_, mul_, zero:=0, sz, xs, ys)
>>> _ws0 == _ws2
True
>>> _ws_ == [u%G for u in _ws0]
True

>>> (neg_, add_, mul_, g, inv_g, sz, inv_len, may_radixes) = _prepare4mod_prime_(modulus:=1+2**128, 2, 256) #not prime
>>> _ws3 = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, sz, inv_g, inv_len, xs, ys)
>>> _ws3 == _ws2
True

>>> (neg_, add_, mul_, g, inv_g, sz, inv_len, may_radixes) = _prepare4mod_prime_(modulus:=1+2**512, 16, 256) #not prime
>>> _ws6 = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, sz, inv_g, inv_len, xs, ys)
>>> _ws6 == _ws2
True


不一致，应当是由于FFT算法内部使用了neg_()，而其结果与pow(g, sz//2, modulus)不一致
>>> (neg_, add_, mul_, g, inv_g, sz, inv_len, may_radixes) = _prepare4mod_prime_(modulus:=-1+2**256, 2, 256, no_neg_one_ok=True) #not prime
>>> _ws4 = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, sz, inv_g, inv_len, xs, ys)
>>> _ws4 == _ws2
False
>>> _ws4  #doctest: +ELLIPSIS
[86992881756140888128335894554634538561511692025502639676866878352288124610536, ..., 86992881756140888128335894554634538561511692025502639676866878352288124610536, 61443909234216866497967250522169146222841596362783601331525665895751215350316]

>>> (neg_, add_, mul_, g, inv_g, sz, inv_len, may_radixes) = _prepare4mod_prime_(modulus:=-1+2**512, 4, 256, no_neg_one_ok=True) #not prime
>>> _ws5 = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, sz, inv_g, inv_len, xs, ys)
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
>>> (neg_, add_, mul_, g, inv_g, sz, inv_len, may_radixes) = _prepare4mod_prime_(modulus:=NG, g6NG, 256, no_neg_one_ok=True)
>>> _ws7 = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, sz, inv_g, inv_len, xs, ys)
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





def poly_evals__on_geometric_progression__native_(add_, mul_, zero, one, coeffs8poly, T, sz=None, /):
def eval_polynomial_on_geometric_progression_(neg_, add_, mul_, zero, one, g, gM, inv_g, div_gM_, coeffs8poly, T, invT, /):

>>> (neg_, add_, mul_, g, inv_g, sz, inv_len, may_radixes) = _prepare4mod_prime_(modulus:=1+2**128, 2, 256) #not prime
>>> zero, one = 0, 1
>>> T = 999
>>> invT = pow(T, -1, modulus)
>>> D = sz//2
>>> coeffs8poly = range(-56, -56+D)
>>> rs0 = eval_polynomial_on_geometric_progression_(neg_, add_, mul_, zero, one, g, gM:=sz, inv_g, inv_len, coeffs8poly, T, invT)
>>> rs1 = poly_evals__on_geometric_progression__native_(add_, mul_, zero, one, coeffs8poly, T, D)
>>> rs0 == rs1
True
>>> rs0  #doctest: +ELLIPSIS
[960, 222127915846752330184403282032556711149, ..., 287181346753101126459978715807575435981, 291707318287887882537969425177217818321, 339571985052737931669852608330042583264]




py_adhoc_call   seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression   @f
from seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression import *
]]]'''#'''
__all__ = r'''
eval_polynomial_on_geometric_progression_
    triangular_number_
        tab_pows_
        tab_tri_pows_


poly_eval_
    iter_poly_evals__native_
    poly_evals__native_
iter_poly_evals__on_geometric_progression__native_
    iter_geometric_progression_
    poly_evals__on_geometric_progression__native_


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.floor_ceil_tools.fc_log import floor_log2, ceil_log2
    from seed.tiny_.check import check_type_is, check_int_ge

    from seed.algo.FFT.convolution import cyclic_convolution__len_eq__7FFT_, cyclic_convolution__len_eq__7native_

    from itertools import islice

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
def tab_tri_pows_(sz, mul_, one, T, /):
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
    return j2Ttrpw


def poly_eval_(add_, mul_, zero, coeffs8poly, x, /):
    y = zero
    for c in reversed(coeffs8poly):
        y = add_(mul_(y, x), c)
    return y
def iter_poly_evals__native_(add_, mul_, zero, coeffs8poly, xs, /):
    for x in xs:
        y = poly_eval_(add_, mul_, zero, coeffs8poly, x)
        yield y
def poly_evals__native_(add_, mul_, zero, coeffs8poly, xs, /):
    return [*iter_poly_evals__native_(add_, mul_, zero, coeffs8poly, xs)]

def iter_geometric_progression_(mul_, one, T, /):
    x = one
    while 1:
        yield x
        x = mul_(x, T)
def iter_poly_evals__on_geometric_progression__native_(add_, mul_, zero, one, coeffs8poly, T, /):
    xs = iter_geometric_progression_(mul_, one, T)
    return iter_poly_evals__native_(add_, mul_, zero, coeffs8poly, xs)
def poly_evals__on_geometric_progression__native_(add_, mul_, zero, one, coeffs8poly, T, sz=None, /):
    if sz is None:
        sz = len(coeffs8poly)
    ys = iter_poly_evals__on_geometric_progression__native_(add_, mul_, zero, one, coeffs8poly, T)
    ys = islice(ys, 0, sz)
    return [*ys]

def eval_polynomial_on_geometric_progression_(neg_, add_, mul_, zero, one, g, gM, inv_g, div_gM_, coeffs8poly, T, invT, /):
    'neg_/(x->x) -> add_/(x->x->x) -> mul_/(x->x->x) -> zero/x -> one/x -> g/x -> gM/uint -> inv_g/x -> div_gM_/(x|(x->x)) -> cs/[x] -> T/x -> invT/x -> ys/[x]{len==len(cs)}  # [mul_order_(mul_;g) == gM == 2**(1 +ceil_log2(len(cs)))][T*invT==one] # [ys[k] == poly_eval_(cs;(T**k)) == sum[cs[j]*(T**k)**j | [j :<- [0..<len(cs)]]]]'
    # -> pow_/(x->uint->x)
    check_int_ge(1, gM)
    cs = coeffs8poly
    D = len(cs)
    # n = D
    m = 1 +ceil_log2(D)
    M = 1 << m
    H = M >> 1
    assert D <= H < 2*D <= M < 4*D, (D, H, 2*D, M, 4*D)
    if not gM == M:raise ValueError(gM, M, len(cs))



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
    ws = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, M, inv_g, div_gM_, us, vs)
    # [j2y[:D] := [(T**triangular_number_(-1+k) * ws[M///2+k-1]) | [k:<-[0..<D]]]]
    ys = j2y = [mul_(ws[H+kmm], j2Ttrpw[max(0,kmm)]) for kmm in range(-1, -1+D)]
    assert len(ys) == D
    return ys


__all__
from seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression import *
