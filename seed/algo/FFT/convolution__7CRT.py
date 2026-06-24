#__all__:goto
fail
    raise bug-dead-loop-since-sz-not-decrease

view others/数学/polynomial/polynomial_evaluation.txt
[若只使用 素阶分圆多项式 则大约需要用到的最大素数约为O(sqrt(degO*ln(degO)))]
  => 只需 lnln(degO)层，数据最终倍增ln(degO)
    这就雷同于symbolic版
分解容易，如何重建？
r'''[[[
e ../../python3_src/seed/algo/FFT/convolution__7CRT.py

seed.algo.FFT.convolution__7CRT
py -m nn_ns.app.debug_cmd   seed.algo.FFT.convolution__7CRT -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.algo.FFT.convolution__7CRT:__doc__ -ht # -ff -df
#######

# linear_convolution == acyclic_convolution <==> __mul__{RR[X]%(0+X**M)}
[[
@20260619
其实FFT就是CRT，而且成功拆分到(X-g**j)
如何找到一批容易拆分重建的多项式？
[(1-X**2**ez) == (1-X)*II[(1+X**2**j) | [j:<-[0..<ez]]]]
拆分后:
    [sum degI >= deg wholeO]
    [sum degO ~= 2 * sum degI]
    这意味着每一层数据翻倍，最好一次拆分到底
    FFT就是成功典范，symbolic版则是半途

]]
[[
@20260619
fail
[M:=len(signal7output)][Ns::[uint{>=2}]][sum(Ns) >= M][are_pairwise_coprime_(Ns)]:
    RR[X]%(0+X**M) --> [RR[X]%(0+X**N) | [N:<-Ns]]
[M:=len(signal7output)][Ns::[uint{>=2}]][II(Ns) >= M][are_pairwise_coprime_(Ns)]:
    RR[X]%(0+X**M) --> [RR[X]%(0+X**N) | [N:<-Ns]]
]]

[[
view others/数学/polynomial/polynomial_evaluation.txt
@20260619
fail:
    raise bug-dead-loop-since-sz-not-decrease
考虑:CRT:拆成三部分:一大两小
    %(0+X**(2*k))
    %(-1+X**(2*k))
        %(-1+X**k)
        %(+1+X**k)
    [O(f(4*k)) == O(10*k + f(2*k)+2*f(k))]
    感觉可以！！
    [1*(0+X**(2*k)) -1*(-1+X**(2*k)) == 1]
    [(-1+X**(2*k))**-1 %(0+X**(2*k)) == -1]
    [(0+X**(2*k))**-1 %(-1+X**(2*k)) == 1]

    [h:=2**-1]
    [h*(+1+X**k) -h*(-1+X**k) == 1]
    [(+1+X**k)**-1 %(-1+X**k) == +h]
    [(-1+X**k)**-1 %(+1+X**k) == -h]
    ==>>:
    [ff(X)%(0+X**(2*k)) == ff0]
    [ff(X)%(-1+X**(2*k)) == ff1]
    [ff(X)%(+1+X**k) == ff1p]
    [ff(X)%(-1+X**k) == ff1n]
    [ff == ff0*-(-1+X**(2*k)) + ff1*(0+X**(2*k))]
    [ff1 == ff1p*-h*(-1+X**k) + ff1n*+h*(+1+X**k)]
    ==>>:
    [ff1 == h*((-ff1p+ff1n)*X**k +(+ff1p+ff1n))]
    [ff == ((-ff0+ff1)*X**(2*k) +ff0)]
    [ff0 == ff[:2*k]]
    [ff1 == ff[:2*k] .+. ff[2*k:]]
    [ff1n == ff1[:k] .+. ff1[k:]]
    [ff1p == ff1[:k] .-. ff1[k:]]
    mx==mx2*mx1
    mx1 = [
    [I; O]
    [I; I]
    ]
    mx2 = [
    [I; O]
    [O; mx3]
    ]
    mx3 = [
    [I; I]
    [I; -I]
    ]
    mx = [
    [I; O]
    [mx3; mx3]
    ]
    mx = [
    [I;O; O;O]
    [O;I; O;O]
    [I;I; I;I]
    [I;-I; I;-I]
    ]


]]
[[
bug:只能保证[0=!=1]，而可能有[-1==1]
===
考虑使用: %((1-X**p)///(1-X)), %((1+X**p)///(1+X)) [即: %(((1-X**(2*p))///(1-X))///(((1-X**2)///(1-X)) * ((1-X**p)///(1-X))))]
view ../../python3_src/seed/math/polynomial/eval_polynomial/cyclotomic_polynomial.py
3:(1, 1, 1)
6:(1, -1, 1)

5:(1, 1, 1, 1, 1)
10:(1, -1, 1, -1, 1)

]]



'#'; __doc__ = r'#'


!! [a,b>0][gcd(a,b)==1][gcd((1-X**a), (1-X**b)) == (1-X)]
=> fail...
>>> _fail__mk_fwd_mx4linear_convolution6coprimes_(1, ver=1)
[[Fraction(1, 1), Fraction(0, 1)], [Fraction(0, 1), Fraction(1, 1)]]
>>> _fail__mk_bwd_mx4linear_convolution6coprimes_(1, ver=1)
[[Fraction(1, 1), Fraction(0, 1)], [Fraction(0, 1), Fraction(1, 1)]]
>>> _fail__mk_fwd_mx4linear_convolution6coprimes_(2, ver=1, val5int_=int)
[[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 0, 1, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 0]]
>>> _fail__mk_fwd_mx4linear_convolution6coprimes_(2, ver=1, val5int_=int) == (
... [[1,0  ,1,0  ,1]
... ,[0,1  ,0,1  ,0]
... ,[1,0,0  ,1,0]
... ,[0,1,0  ,0,1]
... ,[0,0,1  ,0,0]
... ]
... )
True
>>> _fail__mk_bwd_mx4linear_convolution6coprimes_(2, ver=1)
Traceback (most recent call last):
    ...
ValueError: not enough values to unpack (expected 1, got 0)

>>> _fail__mk_fwd_mx4linear_convolution6coprimes_([4,3], ver=1, val5int_=int)
[[1, 0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1], [0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0]]
>>> _fail__mk_bwd_mx4linear_convolution6coprimes_([4,3], ver=1)
Traceback (most recent call last):
    ...
ValueError: not enough values to unpack (expected 1, got 0)
>>> _fail__mk_bwd_mx4linear_convolution6coprimes_([8,5], ver=1)
Traceback (most recent call last):
    ...
ValueError: not enough values to unpack (expected 1, got 0)
>>> _fail__mk_bwd_mx4linear_convolution6coprimes_([3,5], ver=1)
Traceback (most recent call last):
    ...
ValueError: not enough values to unpack (expected 1, got 0)
>>> _fail__mk_bwd_mx4linear_convolution6coprimes_([7,5], ver=1)
Traceback (most recent call last):
    ...
ValueError: not enough values to unpack (expected 1, got 0)
>>> _fail__mk_both_tmay_bwd_mxLR4linear_convolution6coprimes_([13,5], ver=1)
((), ())




[[1,0  ,1,0  ,1]
,[0,1  ,0,1  ,0]
,[1,0,0  ,1,0]
,[0,1,0  ,0,1]
,[0,0,1  ,0,0]
]
[[1,0  ,1,0  ,1]
,[0,1  ,0,1  ,0]
,[0,0,-1  ,1,-1]
,[0,0,0  ,-1,1]
,[0,0,1  ,0,0]
]
[[1,0  ,1,0  ,1]
,[0,1  ,0,1  ,0]
,[0,0,0  ,1,-1]
,[0,0,0  ,-1,1]
,[0,0,1  ,0,0]
]

>>> mk_fwd_mx4linear_convolution7three_parts_(val5int_=int)
[[1, 0, 0, 0], [0, 1, 0, 0], [1, 1, 1, 1], [1, -1, 1, -1]]
>>> mk_bwd_mx4linear_convolution7three_parts_()
[[Fraction(1, 1), Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)], [Fraction(0, 1), Fraction(1, 1), Fraction(0, 1), Fraction(0, 1)], [Fraction(-1, 1), Fraction(0, 1), Fraction(1, 2), Fraction(1, 2)], [Fraction(0, 1), Fraction(-1, 1), Fraction(1, 2), Fraction(-1, 2)]]
>>> h = Fraction(1, 2)
>>> mk_bwd_mx4linear_convolution7three_parts_() == (
... [[1,0  ,0,0]
... ,[0,1  ,0,0]
... ,[-1,0 ,h,h]
... ,[0,-1 ,h,-h]
... ]
... )
True





py_adhoc_call   seed.algo.FFT.convolution__7CRT   @f
from seed.algo.FFT.convolution__7CRT import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
#.from seed.helper.lazy_import__func7dict import lazy_import__funcs7dict_
#.(check_type_is, check_int_ge, _ifNone) = lazy_import__funcs7dict_(__name__ or globals() or locals(), 'seed.tiny_.check',  'check_type_is, check_int_ge      ifNone:_ifNone')
#.#################################
#.def mk_context4lazy_import_registered_names_(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject={}, may_bifix4lazy_name7import=None, lazy_name7importZoriginal_name7import={}):
from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
    from seed._lazy_ import mk_tuple#print_err, fst, echo, ifNone
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
    from seed.math.matrix.solve_matrix import linear_solver, ring_ex_ops__Fraction #NoRowMatrix
#.    from seed.data_funcs.lnkls import rglnkls_ops# empty_rglnkls, mk_empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge, check_all_
    from functools import partial
    from fractions import Fraction
    from seed.math.prime_sieve.PrimeList import PrimeList
    from seed.math.II import II
    from seed.math.are_pairwise_coprime import are_pairwise_coprime, check_pairwise_coprime
    #from seed.math.matrix.solve_matrix import NoRowMatrix, linear_solver, ring_ex_ops__Fraction
    r'''[[[
    solve = partial(linear_solver.solve_equations__matrix__to_representative_solutions, ring_ex_ops__Fraction, validate=True)
    invL_tm = partial(linear_solver.invL__matrix__tmay_arbitrary, ring_ex_ops__Fraction, validate=True)
    invR_tm = partial(linear_solver.invR__matrix__tmay_arbitrary, ring_ex_ops__Fraction, validate=True)
    inv_tm = partial(linear_solver.inv__matrix__tmay, ring_ex_ops__Fraction, validate=True)
    fr = Fraction
    #]]]'''#'''


#.    from itertools import islice
#.    from functools import cached_property
#.    from seed.for_libs.for_functools.cached_property import cached_property
#.    from seed.types.CachedProperty import CachedProperty, mk_cached_propertyT_
#.    from seed.func_tools.dot2 import dot
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def _fail__mk_both_tmay_bwd_mxLR4linear_convolution6coprimes_(coprimes_or_num_primes, /, *, ver, validate=False):
    mx7fwd = _fail__mk_fwd_mx4linear_convolution6coprimes_(coprimes_or_num_primes, ver=ver)
    invL_tm = partial(linear_solver.invL__matrix__tmay_arbitrary, ring_ex_ops__Fraction, validate=True)
    invR_tm = partial(linear_solver.invR__matrix__tmay_arbitrary, ring_ex_ops__Fraction, validate=True)
    tm_mxL7bwd = invL_tm(mx7fwd)
    tm_mxR7bwd = invR_tm(mx7fwd)
    return (tm_mxL7bwd, tm_mxR7bwd)
def _fail__mk_bwd_mx4linear_convolution6coprimes_(coprimes_or_num_primes, /, *, ver, validate=False):
    mx7fwd = _fail__mk_fwd_mx4linear_convolution6coprimes_(coprimes_or_num_primes, ver=ver)
    inv_tm = partial(linear_solver.inv__matrix__tmay, ring_ex_ops__Fraction, validate=validate)
    [mx7bwd] = inv_tm(mx7fwd)
    return mx7bwd
def _fail__mk_fwd_mx4linear_convolution6coprimes_(coprimes_or_num_primes, /, *, ver, val5int_=None):
    if type(coprimes_or_num_primes) is int:
        num_primes = coprimes_or_num_primes
        check_int_ge(1, num_primes)
        coprimes = PrimeList()[:num_primes]
    else:
        coprimes = coprimes_or_num_primes
        coprimes = mk_tuple(coprimes)
        check_all_([check_int_ge, 2], coprimes)
        check_pairwise_coprime(coprimes)
    coprimes
    if val5int_ is None:
        val5int_ = Fraction
    if ver == 1:
        M = sum(coprimes)
        #js = range(M)
        irow2Nr = [(N, r) for N in coprimes for r in range(N)]
        assert len(irow2Nr) == M
        def ij2v_(i, j, /):
            (N, r) = irow2Nr[i]
            return val5int_(j%N == r)
    elif ver == 2:
        M = II(coprimes)
        raise 000
    else:
        raise 000
    mx7fwd = linear_solver.mk_matrix__ij2v(M, M, ij2v_)
    return mx7fwd

def mk_bwd_mx4linear_convolution7three_parts_(*, validate=False):
    mx7fwd = mk_fwd_mx4linear_convolution7three_parts_()
    inv_tm = partial(linear_solver.inv__matrix__tmay, ring_ex_ops__Fraction, validate=validate)
    [mx7bwd] = inv_tm(mx7fwd)
    return mx7bwd
def mk_fwd_mx4linear_convolution7three_parts_(*, val5int_=None):
    if val5int_ is None:
        val5int_ = Fraction
    mx = (
    [[1, 0, 0, 0]
    ,[0, 1, 0, 0]
    ,[1, 1, 1, 1]
    ,[1, -1, 1, -1]
    ])
    M = 4
    def ij2v_(i, j, /):
        return val5int_(mx[i][j])
    mx7fwd = linear_solver.mk_matrix__ij2v(M, M, ij2v_)
    return mx7fwd

def dyadic_operator_(ops, op, /, *argss):
    '(*args/[arg]{len=i} -> result) -> (*argss/[[arg]{len=i}]{len=k}) -> [result]{len=k}'
    return ops.mk_list_(map(op, *argss))
def add7polynomial_(ops, us, vs, /):
    us = drop_zero_pad_(ops, us)
    vs = drop_zero_pad_(ops, vs)
    ws = dyadic_operator_(ops, ops.add_, us, vs)
    if len(ws) < len(us):
        ws = ws + us[len(ws):]
    elif len(ws) < len(vs):
        ws = ws + vs[len(ws):]
    ws = drop_zero_pad_(ops, ws)
    return ws
def sub7polynomial_(ops, us, vs, /):
    us = drop_zero_pad_(ops, us)
    vs = drop_zero_pad_(ops, vs)
    ws = dyadic_operator_(ops, ops.sub_, us, vs)
    if len(ws) < len(us):
        ws = ws + us[len(ws):]
    elif len(ws) < len(vs):
        ws = ops.mk_list_(chain(ws, map(ops.neg_, vs[len(ws):])))
    ws = drop_zero_pad_(ops, ws)
    return ws
def dyadic_half_(ops, us, vs, /):
    return dyadic_operator_(ops, ops.half_, us, vs)
def zero_pad_(ops, sz, us, /):
    if len(us) < sz:
        us = ops.mk_list_(chain(us, repeat(ops.zero, (sz-len(us)))))
    return us
def trunc_(sz, us, /):
    'RR[X]%(0+X**sz)'
    if len(us) > sz:
        us = us[:sz]
    return us
def wrap_around_(ops, sz, us, /, to_neg=False):
    'RR[X]%(-1+X**sz) if not to_neg else RR[X]%(+1+X**sz)'
    raise
def split_at_(j, us, /):
    if len(us) > j:
        usL = us[:j]
        usR = us[j:]
    else:
        usL = us
        usR = us[:0]
    return (usL, usR)
def drop_zero_pad_(ops, us, /):
    if not us:
        return us
    is_zero_ = ops.is_zero_
    for j in reversed(range(len(us))):
        if not is_zero_(us[j]):
            if 1+j < len(us):
                return us[:1+j]
            return us
    return us[:0]

#def acyclic_convolution_(ops, us, vs, /):
def mul7polynomial_(ops, us, vs, /):
    '__mul__{RR[X]}'
    raise bug-dead-loop-since-sz-not-decrease
    us = drop_zero_pad_(ops, us)
    vs = drop_zero_pad_(ops, vs)
    sz = -1 + len(us) + len(vs)
    ce4half = -(sz//-2)
    (usL, usR) = split_at_(ce4half, us)
    (vsL, vsR) = split_at_(ce4half, vs)
    usL = drop_zero_pad_(ops, usL)
    vsL = drop_zero_pad_(ops, vsL)

    usH = add7polynomial_(ops, usL, usR)
    vsH = add7polynomial_(ops, vsL, vsR)

    wsL = mul7polynomial_(ops, usL, vsL)
    wsH = mul7polynomial_(ops, usH, vsH)

    wsL = trunc_(ce4half, wsL)
    wsH = wrap_around_(ops, ce4half, wsH)

    wsR = sub7polynomial_(ops, wsH, wsL)
    if wsR:
        wsL = zero_pad_(ce4half, wsL)
        ws = wsL + wsR
    else:
        wsL = drop_zero_pad_(ops, wsL)
        ws = wsL
    ws = drop_zero_pad_(ops, ws)
    return ws

__all__
from seed.algo.FFT.convolution__7CRT import *
