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
]]


'#'; __doc__ = r'#'
>>> from seed.algo.FFT.index_scramble4FFT import _prepare4mod_zpow_

    #def _prepare4mod_zpow_(ez4modulus, ez4sz, /):
    #    -> (neg_, add_, mul_, g, inv_g, sz, div_len_, may_radixes)
>>> from seed.algo.FFT.index_scramble4FFT import _prepare4mod_prime_

    #def _prepare4mod_prime_(modulus, g, sz=None, /):
    #    -> (neg_, add_, mul_, g, inv_g, sz, inv_len, may_radixes)



>>> xs = [1, 2, 3, 4]
>>> ys = [1, 5, 7, 3]
>>> M = len(xs)
>>> (neg_, add_, mul_, g, inv_g, sz, inv_len, may_radixes) = _prepare4mod_prime_(modulus:=1+2**16, pow(3, (modulus-1)//M, modulus), M)
>>> cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, sz, inv_g, inv_len, xs, ys, validate=True)
[48, 44, 32, 36]

>>> sz
4
>>> len(xs[:4])
4
>>> len(ys[:0])
0
>>> acyclic_convolution__lenO_eq__7FFT_(neg_, add_, mul_, zero:=0, g, sz, inv_g, inv_len, xs[:4], ys[:0], validate=True)
[0, 0, 0, 0]
>>> acyclic_convolution__lenO_eq__7FFT_(neg_, add_, mul_, zero:=0, g, sz, inv_g, inv_len, xs[:3], ys[:1], validate=True)
[1, 2, 3, 0]
>>> acyclic_convolution__lenO_eq__7FFT_(neg_, add_, mul_, zero:=0, g, sz, inv_g, inv_len, xs[:2], ys[:2], validate=True)
[1, 7, 10, 0]
>>> acyclic_convolution__lenO_eq__7FFT_(neg_, add_, mul_, zero:=0, g, sz, inv_g, inv_len, xs[:1], ys[:3], validate=True)
[1, 5, 7, 0]
>>> acyclic_convolution__lenO_eq__7FFT_(neg_, add_, mul_, zero:=0, g, sz, inv_g, inv_len, xs[:0], ys[:4], validate=True)
[0, 0, 0, 0]






py_adhoc_call   seed.algo.FFT.convolution   @f
from seed.algo.FFT.convolution import *
]]]'''#'''
__all__ = r'''
cyclic_convolution__len_eq__7FFT_
    cyclic_convolution__len_eq__7native_

acyclic_convolution__lenO_eq__7FFT_
    acyclic_convolution__lenI_eq__7FFT_
    acyclic_convolution__lenO_eq__7native_
        acyclic_convolution__lenI_eq__7native_


dyadic_operator_
sum0_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.algo.FFT.FFT import FFT__ping_pong
    #def FFT__ping_pong(neg_, add_, mul_, g, xs, /, *, may_radixes=None, scramble_=None, may_gs=None, may_ys=None):
    from seed.algo.FFT.index_scramble4FFT import IFFT_, FFT__idx_digit_reverse
    #def IFFT_(FFT_, neg_, add_, mul_, inv_g, inv_len, xs, /, *, extra_args=(), may_gs=None, may_inv_gs=None, **kwds):
    from functools import reduce
    #reduce(function, iterable[, initializer])

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
def cyclic_convolution__len_eq__7native_(add_, mul_, zero, M, us, vs, /):
    # for validate
    '[M == len(us) == len(vs)] # [zero is useless]'
    #ws = [sum0_(add_, zero, (mul_(us[j], vs[(k-j)%M]) for j in range(M))) for k in range(M)]
    #return ws
    ws = [sum1_(add_, (mul_(us[j], vs[(k-j)%M]) for j in range(M))) for k in range(M)]
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

def acyclic_convolution__lenI_eq__7FFT_(neg_, add_, mul_, zero, hg, M, inv_g, div_M_, us, vs, /, *, FFT_=None, validate=False):
    # for validate
    '[M == len(us) == len(vs) == 1/2 * mul_order_(hg)][hg**M == -1]'
    if not M == len(us) == len(vs):raise TypeError
    return acyclic_convolution__lenO_eq__7FFT_(neg_, add_, mul_, zero, hg, M<<1, inv_g, div_M_, us, vs, FFT_=FFT_, validate=validate)
def acyclic_convolution__lenO_eq__7FFT_(neg_, add_, mul_, zero, g, M, inv_g, div_M_, us, vs, /, *, FFT_=None, validate=False):
    # eg:polynomial multiplication
    '[M == len(us) + len(vs) == mul_order_(g)][g**M == 1] # [[M%2==0] => [1+g**(M///2) == 0]] #eg:bad usage:[g:=CRT([3,5], [1,-1])][g%15 == 4][order_mod_(15;g) == 2]but[(g+1)%15 =!= 0]'
    if not M == len(us) + len(vs):raise TypeError(M, len(us) + len(vs))
    #zero_padding
    us_zz = [*us, *[zero]*len(vs)]
    vs_zz = [*vs, *[zero]*len(us)]
        # (us, vs) used below@[validate=True]
    if not M == len(us_zz) == len(vs_zz):raise 000
    ws = cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, M, inv_g, div_M_, us_zz, vs_zz, FFT_=FFT_)
    if validate:
        assert ws == acyclic_convolution__lenO_eq__7native_(add_, mul_, zero, M, us, vs)
    return ws

def cyclic_convolution__len_eq__7FFT_(neg_, add_, mul_, g, M, inv_g, div_M_, us, vs, /, *, FFT_=None, validate=False):
    # using FFT:O(M*lnM)*field_mul
    '[M == len(us) == len(vs) == mul_order_(g)][g**M == 1] # [[M%2==0] => [1+g**(M///2) == 0]] #eg:bad usage:[g:=CRT([3,5], [1,-1])][g%15 == 4][order_mod_(15;g) == 2]but[(g+1)%15 =!= 0]'
    # [cyclic_convolution__len_eq_(M; us, vs) == IDFT(g; DFT(g;us) .*. DFT(g;vs))]
    if FFT_ is None:
        FFT_ = FFT__ping_pong
        #FFT_ = FFT__idx_digit_reverse
    DFT4us = FFT_(neg_, add_, mul_, g, us)
    DFT4vs = FFT_(neg_, add_, mul_, g, vs)
    DFT4ws = dyadic_operator_(mul_, DFT4us, DFT4vs)
    ws = IFFT_(FFT_, neg_, add_, mul_, inv_g, div_M_, DFT4ws)
    if validate:
        # !! [zero is useless]
        assert ws == cyclic_convolution__len_eq__7native_(add_, mul_, zero:=None, M, us, vs)
    return ws




__all__
from seed.algo.FFT.convolution import cyclic_convolution__len_eq__7FFT_, cyclic_convolution__len_eq__7native_
from seed.algo.FFT.convolution import dyadic_operator_, sum0_, sum1_
from seed.algo.FFT.convolution import *
