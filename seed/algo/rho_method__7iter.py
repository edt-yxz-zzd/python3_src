#__all__:goto
r'''[[[
e ../../python3_src/seed/algo/rho_method__7iter.py
view ../../python3_src/seed/algo/rho_method__7iter___py_adhoc_call.py

seed.algo.rho_method__7iter
py -m nn_ns.app.debug_cmd   seed.algo.rho_method__7iter -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.algo.rho_method__7iter:__doc__ -ht # -ff -df
#######

[[
源起:
view script/整数分解牜尸方法牜吸引子.py

相关:
view script/模幂注入.py
]]


'#'; __doc__ = r'#'
[[

def try7iter_rho_method7default_(max_num_steps_per_xs, xss, /, x2key_=None, test_=None, stop_=None, *, ok_=None, more_info=False):

>>> [*islice(mk_rho_iterator_(6, 3), 0, 12)]
[-6, -5, -4, -3, -2, -1, 1, 2, 3, 1, 2, 3]
>>> calc_required_num_steps4rho_method_(6, 3)
10
>>> try7iter_rho_method7default_(10, [mk_rho_iterator_(6, 3)], more_info=True)
(True, (1, 10))
>>> try7iter_rho_method7default_(9, [mk_rho_iterator_(6, 3)], more_info=True)
(None, 1)

>>> calc_required_num_steps4rho_method_(4, 4)
11
>>> try7iter_rho_method7default_(11, [mk_rho_iterator_(4, 4)], more_info=True)
(True, (1, 11))
>>> try7iter_rho_method7default_(10, [mk_rho_iterator_(4, 4)], more_info=True)
(None, 1)

>>> calc_required_num_steps4rho_method_(7, 4)
11
>>> try7iter_rho_method7default_(11, [mk_rho_iterator_(7, 4)], more_info=True)
(True, (1, 11))
>>> try7iter_rho_method7default_(10, [mk_rho_iterator_(7, 4)], more_info=True)
(None, 1)

>>> calc_required_num_steps4rho_method_(8, 4)
19
>>> try7iter_rho_method7default_(19, [mk_rho_iterator_(8, 4)], more_info=True)
(True, (1, 19))
>>> try7iter_rho_method7default_(18, [mk_rho_iterator_(8, 4)], more_info=True)
(None, 1)


>>> calc_required_num_steps4rho_method_(4, 7)
14
>>> try7iter_rho_method7default_(14, [mk_rho_iterator_(4, 7)], more_info=True)
(True, (1, 14))
>>> try7iter_rho_method7default_(13, [mk_rho_iterator_(4, 7)], more_info=True)
(None, 1)

>>> calc_required_num_steps4rho_method_(4, 8)
15
>>> try7iter_rho_method7default_(15, [mk_rho_iterator_(4, 8)], more_info=True)
(True, (1, 15))
>>> try7iter_rho_method7default_(14, [mk_rho_iterator_(4, 8)], more_info=True)
(None, 1)

>>> calc_required_num_steps4rho_method_(4, 9)
24
>>> try7iter_rho_method7default_(24, [mk_rho_iterator_(4, 9)], more_info=True)
(True, (1, 24))
>>> try7iter_rho_method7default_(23, [mk_rho_iterator_(4, 9)], more_info=True)
(None, 1)

>>> calc_required_num_steps4rho_method_(8, 9)
24
>>> try7iter_rho_method7default_(24, [mk_rho_iterator_(8, 9)], more_info=True)
(True, (1, 24))
>>> try7iter_rho_method7default_(23, [mk_rho_iterator_(8, 9)], more_info=True)
(None, 1)

>>> calc_required_num_steps4rho_method_(15, 9)
24
>>> try7iter_rho_method7default_(24, [mk_rho_iterator_(15, 9)], more_info=True)
(True, (1, 24))
>>> try7iter_rho_method7default_(23, [mk_rho_iterator_(15, 9)], more_info=True)
(None, 1)

>>> calc_required_num_steps4rho_method_(16, 9)
40
>>> try7iter_rho_method7default_(40, [mk_rho_iterator_(16, 9)], more_info=True)
(True, (1, 40))
>>> try7iter_rho_method7default_(39, [mk_rho_iterator_(16, 9)], more_info=True)
(None, 1)

>>> def _test4calc_required_num_steps4rho_method_(max1_len4leader, max1_len4circle, /):
...     for len4leader in range(0, max1_len4leader):
...         for len4circle in range(1, max1_len4circle):
...             required_num_steps = calc_required_num_steps4rho_method_(len4leader, len4circle)
...             r7ok = try7iter_rho_method7default_(required_num_steps, [mk_rho_iterator_(len4leader, len4circle)], more_info=True)
...             assert r7ok == (True, (1, required_num_steps))
...             if required_num_steps == 1:continue
...             r7fail = try7iter_rho_method7default_(-1+required_num_steps, [mk_rho_iterator_(len4leader, len4circle)], more_info=True)
...             assert r7fail == (None, 1)
>>> _test4calc_required_num_steps4rho_method_(12, 12)


>>> calc_rho_shape5num_steps4rho_method_(12)
((0, 7), 5)
>>> calc_required_num_steps4rho_method_(0, 5)
12
>>> calc_required_num_steps4rho_method_(7, 5)
12
>>> calc_required_num_steps4rho_method_(8, 5)
20

>>> calc_rho_shape5num_steps4rho_method_(15)
((0, 7), 8)
>>> calc_required_num_steps4rho_method_(0, 8)
15
>>> calc_required_num_steps4rho_method_(7, 8)
15

>>> calc_rho_shape5num_steps4rho_method_(16)
((8, 15), 1)
>>> calc_required_num_steps4rho_method_(7, 1)
8
>>> calc_required_num_steps4rho_method_(8, 1)
16
>>> calc_required_num_steps4rho_method_(15, 1)
16
>>> calc_required_num_steps4rho_method_(16, 1)
32



>>> def _test4calc_rho_shape5num_steps4rho_method_(max1_num_steps, /):
...     for num_steps in range(1, max1_num_steps):
...         rho_shape = calc_rho_shape5num_steps4rho_method_(num_steps)
...         (minmax_len4leader, len4circle) = rho_shape
...         (min_len4leader, max_len4leader) = minmax_len4leader
...         assert num_steps == calc_required_num_steps4rho_method_(min_len4leader, len4circle)
...         assert num_steps == calc_required_num_steps4rho_method_(max_len4leader, len4circle)
...         assert min_len4leader == 0 or num_steps > calc_required_num_steps4rho_method_(-1+min_len4leader, len4circle)
...         assert num_steps < calc_required_num_steps4rho_method_(+1+max_len4leader, len4circle)
>>> _test4calc_rho_shape5num_steps4rho_method_(100)










]]
[[
===
test:kw:print6KeyboardInterrupt:
===
>>> def u2next_u_(u, /):
...     if u == 10999:raise KeyboardInterrupt(666)
...     return 1+u
>>> ls = []
>>> it = islice(iter_rho_method4factor_pint7gcd_((-1+2**34)//3, 10000, u2next_u_, print6KeyboardInterrupt=ls.append), 0, 1000)
>>> # [*it] => doctest cannot catch KeyboardInterrupt
>>> from sys import stdout
>>> from seed.debug.print_exc import print_exc
>>> try:
...     [*it]
... except KeyboardInterrupt:
...     print_exc(file=stdout) #doctest: +ELLIPSIS
Traceback (most recent call last):
...
KeyboardInterrupt: 666
<BLANKLINE>
During handling of the above exception, another exception occurred:
<BLANKLINE>
Traceback (most recent call last):
...
seed.algo.rho_method__7iter.KeyboardInterrupt__ixi_jxj: (KeyboardInterrupt(666), ((511, 10511), (999, 10999)))
>>> ls
[((511, 10511), (999, 10999))]




===
]]
[[
===
test:kw:resume:
===
>>> ls0_6 = [*islice(iter_rho_method4factor_pint7gcd_((-1+2**34)//3, 27, 'pow_u_u_'), 0, 7)]
>>> len(ls0_6)
6
>>> ls0_6[-1]
(True, 43691, (3, 1242896403, 1242896403), (6, 2055505312, 2055505312))
>>> ls0_6[2]
(False, 1, (1, 5498574605, 5498574605), (3, 1242896403, 1242896403))
>>> ls2_6 = [*islice(iter_rho_method4factor_pint7gcd_((-1+2**34)//3, ((1, 5498574605),(3, 1242896403)), 'pow_u_u_', resume=True), 0, 6)]
>>> len(ls2_6)
4
>>> ls2_6 == ls0_6[2:]
True


===
]]














e ../../python3_src/seed/algo/rho_method__7iter___py_adhoc_call.py



[[
===
test:kw:resume:
===
def iter_rho_method4factor_pint7gcd_(M, u0, u2next_u_, /, *, extra_args=(), gcd_with_more=1, print6KeyboardInterrupt=print, resume=False):
===

py_adhoc_call { --lineno=1 }  seed.algo.rho_method__7iter   ,iter_rho_method4factor_pint7gcd_  ='(-1+2**34)//3' =27 :pow_u_u_
    1:(False, 1, (0, 27, 27), (1, 5498574605, 5498574605))
    2:(False, 1, (1, 5498574605, 5498574605), (2, 1377351933, 1377351933))
    3:(False, 1, (1, 5498574605, 5498574605), (3, 1242896403, 1242896403))
    4:(False, 1, (3, 1242896403, 1242896403), (4, 1870814876, 1870814876))
    5:(False, 1, (3, 1242896403, 1242896403), (5, 5258238993, 5258238993))
    6:(True, 43691, (3, 1242896403, 1242896403), (6, 2055505312, 2055505312))

py_adhoc_call { --lineno=3 }  seed.algo.rho_method__7iter   ,iter_rho_method4factor_pint7gcd_  ='(-1+2**34)//3' +resume ='((1, 5498574605),(3, 1242896403))' :pow_u_u_
    3:(False, 1, (1, 5498574605, 5498574605), (3, 1242896403, 1242896403))
    4:(False, 1, (3, 1242896403, 1242896403), (4, 1870814876, 1870814876))
    5:(False, 1, (3, 1242896403, 1242896403), (5, 5258238993, 5258238993))
    6:(True, 43691, (3, 1242896403, 1242896403), (6, 2055505312, 2055505312))


===
]]


py_adhoc_call   seed.algo.rho_method__7iter   @f
from seed.algo.rho_method__7iter import *
]]]'''#'''
#++resume
__all__ = r'''
KeyboardInterrupt__ixi_jxj
iter_rho_method__7resume_
    iter_rho_method__5iter__7resume_
iter_rho_method_
    iter_rho_method__5iter_
        iter_rho_method__5iter__7default_
            try7iter_rho_method7default_
        calc_required_num_steps4rho_method_
            mk_rho_iterator_
        calc_rho_shape5num_steps4rho_method_

iter_rho_method4factor_pint7gcd__7resume_
iter_rho_method4factor_pint7gcd_
iter_rho_method4factor_pint7gcd7quadratic_attract_
    mk_u2next_u__7quadratic_attract_
        mk_std_ratio_
            iter_mk_std_ratios_
try_factor_pint7iter_rho_method7gcd7quadratic_attract_
    try_factor_pint7iter_rho_method7gcd7quadratic_attract__ratios_


try_factor_pint7iter_rho_method7gcd_



prepare_u2next_u_
    mk_u2next_u__5name_



check_odd_uint_
rem_mod_odd_
div2_mod_odd_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.funcs import echo
    from seed.helper.ifNone import ifNone
    from seed.tiny_.check import check_type_le, check_type_is, check_int_ge, check_callable
    from numbers import Rational
    from fractions import Fraction
    from math import gcd
    from itertools import islice, chain, cycle
    from seed.math.Jacobi_symbol import Jacobi_symbol
    from seed.math.floor_ceil_tools.fc_log import floor_log2, ceil_log2
    from seed.for_libs.next__tmay import next_
    from seed.iters.iterate import iterate
    from operator import __eq__
    from seed.math.II import II_mod
    from seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression import Eval_polynomial_on_geometric_progression__7modulus
        # Eval_polynomial_on_geometric_progression__7modulus(modulus, hrem_vs_mod=hrem_vs_mod).evals_(coeffs8poly, T, invT)
000000000 and TODO and Eval_polynomial_on_geometric_progression__7modulus
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def calc_rho_shape5num_steps4rho_method_(num_steps, /):
    check_int_ge(1, num_steps)
    len4last_round = 1 << floor_log2(num_steps)
    len4circle = num_steps -(-1 +len4last_round)
    max_len4leader = len4last_round -1
    if len4last_round == 1 << (len4circle-1).bit_length():
        min_len4leader = 0
    else:
        min_len4leader = len4last_round >> 1
    min_len4leader

    minmax_len4leader = (min_len4leader, max_len4leader)
    rho_shape = (minmax_len4leader, len4circle)
    return rho_shape

def calc_required_num_steps4rho_method_(len4leader, len4circle, /):
    check_int_ge(0, len4leader)
    check_int_ge(1, len4circle)
    #len4last_round = 1 << (1+floor_log2(max(len4leader, len4circle-1)))
    #   ^AssertionError@[len4leader==0][len4circle==1]
    len4last_round = 1 << max(len4leader, len4circle-1).bit_length()
    # [len4leader+1 <= len4last_round]
    # [len4circle+1 <= len4last_round]
    #return -1 +(len4last_round-1) + (len4circle+1)
    return -1 +len4last_round +len4circle
def mk_rho_iterator_(len4leader, len4circle, /):
    check_int_ge(0, len4leader)
    check_int_ge(1, len4circle)
    #leader = range(-1-len4leader, -1)
    leader = range(-len4leader, 0)
    assert len(leader) == len4leader
    circle = range(1, 1+len4circle)
    assert len(circle) == len4circle
    return chain(leader, cycle(circle))



def iter_rho_method_(x0, x2next_x_, x2key_, test_, stop_, /, *, print6KeyboardInterrupt=print, resume=False):
    'x -> (x->x) -> (x->k) -> (k->k->r) -> (r->whether_stop/bool) -> Iter (whether_stop[i,j]/bool, r[i,j], (i, x[i], k[i]), (j, x[j], k[j]))  # stop iff found result or detect bad seed/state'
    if resume:
        (ixi, jxj) = x0
        return iter_rho_method__7resume_(ixi, jxj, x2next_x_, x2key_, test_, stop_, print6KeyboardInterrupt=print6KeyboardInterrupt)
    #########
    xs = iterate(x2next_x_, x0)
    return iter_rho_method__5iter_(xs, x2key_, test_, stop_, print6KeyboardInterrupt=print6KeyboardInterrupt)
def iter_rho_method__7resume_(ixi, jxj, x2next_x_, x2key_, test_, stop_, /, *, print6KeyboardInterrupt=print):
    '(i, x[i]) -> (j, x[j]) -> (x->x) -> (x->k) -> (k->k->r) -> (r->whether_stop/bool) -> Iter (whether_stop[i,j]/bool, r[i,j], (i, x[i], k[i]), (j, x[j], k[j]))  # stop iff found result or detect bad seed/state'
    (i, xi) = ixi
    (j, xj) = jxj
    xs6j = iterate(x2next_x_, xj)
    return iter_rho_method__5iter__7resume_(i, xi, j, xs6j, x2key_, test_, stop_, print6KeyboardInterrupt=print6KeyboardInterrupt)
class KeyboardInterrupt__ixi_jxj(KeyboardInterrupt):
    def __init__(sf, exc, ixi_jxj, /):
        check_type_le(KeyboardInterrupt, exc)
        ((i, xi), (j, xj)) = ixi_jxj
        super().__init__(exc, ixi_jxj)
        sf.ixi_jxj = ixi_jxj
        sf.exc = exc

def _body4iter_rho_method__5iter_(ti, j, xs, x2key_, test_, stop_, print6KeyboardInterrupt, /):
    i = ti[0]
    end = (1+i) << 1
    assert end.bit_count() == 1
    assert i < j < end
    tj = xj = Nothing = object()
    try:
        while 1:
            (i, xi, ki) = ti

            for j in range(j, end):
                #xj = x2next_x_(xj)
                xj = next_(xs)
                kj = x2key_(xj)
                tj = (j, xj, kj)
                rij = test_(ki, kj)
                bij = stop_(rij)
                yield (bij, rij, ti, tj)
                if bij: return
            #...
            j
            ti = tj
            j += 1
            end = j<<1
            #assert end.bit_count() == 1
    except KeyboardInterrupt as exc:
        (i, xi, ki) = ti
        ixi = (i, xi)
        ###
        if xj is Nothing:
            j # j0
            xj = next_(xs)
        elif tj is Nothing:
            j # j0
            xj # x[j0]
        else:
            (j, xj, kj) = tj
        jxj = (j, xj)
        ###
        print6KeyboardInterrupt(dat:=(ixi, jxj))
        raise KeyboardInterrupt__ixi_jxj(exc, dat)
def iter_rho_method__5iter_(xs, x2key_, test_, stop_, /, *, print6KeyboardInterrupt=print, ixi_j4resume=None):
    #, resume=False
    'Iter x -> (x->k) -> (k->k->r) -> (r->whether_stop/bool) -> Iter (whether_stop[i,j]/bool, r[i,j], (i, x[i], k[i]), (j, x[j], k[j])) | ^KeyboardInterrupt__ixi_jxj(KeyboardInterrupt, (ixi,jxj)) # [print6KeyboardInterrupt((ixi,jxj)) -> None] # stop iff found result or detect bad seed/state'
    if not ixi_j4resume is None:
        (i, xi, j) = ixi_j4resume
        xs6j = xs
        return iter_rho_method__5iter__7resume_(i, xi, j, xs6j, x2key_, test_, stop_, print6KeyboardInterrupt=print6KeyboardInterrupt)
    #########
    xs = iter(xs)
    x0 = next_(xs)
    ti = (i, xi, ki) = 0, x0, x2key_(x0)
    j = i+1
    return _body4iter_rho_method__5iter_(ti, j, xs, x2key_, test_, stop_, print6KeyboardInterrupt)
def iter_rho_method__5iter__7resume_(i, xi, j, xs6j, x2key_, test_, stop_, /, *, print6KeyboardInterrupt=print):
    'i/uint{==2**ez-1} -> x[i] -> j/uint{>=2**ez}{<2**(1+ez)} -> Iter x[k]{k>=j} -> (x->k) -> (k->k->r) -> (r->whether_stop/bool) -> Iter (whether_stop[i,j]/bool, r[i,j], (i, x[i], k[i]), (j, x[j], k[j]))  # stop iff found result or detect bad seed/state'
    check_int_ge(0, i)
    check_int_ge(1+i, j)
    ez = i.bit_length()
    zpow = 1<<ez
    if not i+1 == zpow:raise ValueError(i)
    #if not zpow <= j < 2*zpow:raise ValueError(i, j)
    if not (j>>ez) == 1:raise ValueError(i, j)

    xs6j = iter(xs6j)
    i
    xi
    ki = x2key_(xi)
    ti = (i, xi, ki)
    j
    return _body4iter_rho_method__5iter_(ti, j, xs6j, x2key_, test_, stop_, print6KeyboardInterrupt)

def iter_rho_method__5iter__7default_(xs, /, x2key_=None, test_=None, stop_=None, max_num_steps=None, print6KeyboardInterrupt=print, ixi_j4resume=None):
    'Iter x -> Iter (whether_stop[i,j]/bool, r[i,j], (i, x[i], k[i]), (j, x[j], k[j]))'
    x2key_ = ifNone(x2key_, echo)
    test_ = ifNone(test_, __eq__)
    stop_ = ifNone(stop_, bool)
    it = iter_rho_method__5iter_(xs, x2key_, test_, stop_, print6KeyboardInterrupt=print6KeyboardInterrupt, ixi_j4resume=ixi_j4resume)
    if not max_num_steps is None:
        check_int_ge(1, max_num_steps)
        it = islice(max_num_steps, 0, max_num_steps)
    return it


#resume
def iter_rho_method4factor_pint7gcd__7resume_(M, iui, juj, u2next_u_, /, *, extra_args=(), gcd_with_more=1, print6KeyboardInterrupt=print):
    'M/uint{>0} -> (i, u[i]) -> (j, u[j]) -> ((u->u)|name/str) -> Iter (whether_stop[i,j]/bool, g[i,j], (i, u[i], u[i]), (j, u[j], u[j]))  # stop iff [g[i,j]=!=1] where [g[i,j] == gcd(u[i],u[j])]'
    (i, ui) = iui
    (j, uj) = juj
    (x2next_x_, x2key_, test_, stop_) = _prepare4iter_rho_method4factor_pint7gcd_(M, u2next_u_, extra_args, gcd_with_more)
    check_type_is(int, ui)
    check_type_is(int, uj)
    xi = ui % M
    xj = uj % M
    ixi = (i, xi)
    jxj = (j, xj)
    return iter_rho_method__7resume_(ixi, jxj, x2next_x_, x2key_, test_, stop_, print6KeyboardInterrupt=print6KeyboardInterrupt)
def iter_rho_method4factor_pint7gcd_(M, u0, u2next_u_, /, *, extra_args=(), gcd_with_more=1, print6KeyboardInterrupt=print, resume=False):
    'M/uint{>0} -> u/uint%M -> ((u->u)|name/str) -> Iter (whether_stop[i,j]/bool, g[i,j], (i, u[i], u[i]), (j, u[j], u[j]))  # stop iff [g[i,j]=!=1] where [g[i,j] == gcd(u[i],u[j])]'
    if resume:
        (iui, juj) = u0
        return iter_rho_method4factor_pint7gcd__7resume_(M, iui, juj, u2next_u_, extra_args=extra_args, gcd_with_more=gcd_with_more, print6KeyboardInterrupt=print6KeyboardInterrupt)
    #########
    (x2next_x_, x2key_, test_, stop_) = _prepare4iter_rho_method4factor_pint7gcd_(M, u2next_u_, extra_args, gcd_with_more)
    check_type_is(int, u0)
    x0 = u0 % M
    return iter_rho_method_(x0, x2next_x_, x2key_, test_, stop_, print6KeyboardInterrupt=print6KeyboardInterrupt)
def _prepare4iter_rho_method4factor_pint7gcd_(M, u2next_u_, extra_args, gcd_with_more, /):
    check_int_ge(1, M)
    u2next_u_ = prepare_u2next_u_(M, u2next_u_)

    x2key_ = echo
    def x2next_x_(u, /, *, extra_args=extra_args):
        return u2next_u_(*extra_args, u)%M
    if gcd_with_more == 1:
        def test_(ui, uj, /):
            g = gcd(uj-ui, M)
            return g
    else:
        match gcd_with_more:
            case 2:
                def mk_us_(ui, uj, /):
                    us = [(uj-ui), (uj-1)]
                    return us
            case 3:
                def mk_us_(ui, uj, /):
                    us = [(uj-ui), (uj-1), uj]
                    return us
            case _:
                raise Exception(gcd_with_more)
        mk_us_
        def test_(ui, uj, /):
            #old:g = gcd(uj-ui, M)
            #new:see:pow_u_u_
            us = mk_us_(ui, uj)
            g = gcd(M, II_mod(M, us))
            if g == M:
                gs = []
                for u in us:
                    g = gcd(u, M)
                    if 1 < g < M: break
                    gs.append(g)
                else:
                    g = gs[0] # (uj-ui)
                g
            return g
    def stop_(g, /):
        return not g == 1
    return (x2next_x_, x2key_, test_, stop_)


def iter_rho_method4factor_pint7gcd7quadratic_attract_(M, D, u0, /, *, ratio=None, exp=2, print6KeyboardInterrupt=print, resume=False):
    'M/uint{>0} -> D/uint%M -> u/uint%M -> Iter (whether_stop[i,j]/bool, g[i,j], (i, u[i], u[i]), (j, u[j], u[j]))  # stop iff [g[i,j]=!=1] where [g[i,j] == gcd(u[i],u[j])]'
    u2next_u_ = mk_u2next_u__7quadratic_attract_(M, D, ratio=ratio, exp=exp)
    return iter_rho_method4factor_pint7gcd_(M, u0, u2next_u_, print6KeyboardInterrupt=print6KeyboardInterrupt, resume=resume)
def check_odd_uint_(M, /):
    check_int_ge(1, M)
    if not M&1 == 1:raise ValueError('not odd uint') #modulus
def rem_mod_odd_(M, x, /):
    #check_odd_uint_(M)
    H = M//2
    if not abs(x) <= H:
        x %= M
        if x > H:
            x -= M
    assert abs(x) <= H
    return x


def iter_mk_std_ratios_(M, exp, ratios, /, *, _01_ok=False):
    for ratio in ratios:
        ratio = mk_std_ratio_(M, exp, ratio, _01_ok=_01_ok)
        yield ratio

def mk_std_ratio_(M, exp, ratio, /, *, _01_ok=False):
    '-> int'
    #old:'-> emay int # [... repr 1/2][None repr 1/exp]'
    check_int_ge(2, exp)
    check_odd_uint_(M)
    if ratio is None:
        ratio = Fraction(1, exp)
    elif ratio is ...:
        ratio = Fraction(1, 2)

    if not ratio is ...:
        #if not (1 < ratio < M or 1 < ratio+M < M):raise ValueError(M, ratio0)
        #check_type_le(Rational, ratio)
        #rD = ratio.denominator
        #rN = ratio.numerator

        ratio0 = ratio
        ratio = Fraction(ratio0) #eg:str:'1/3'
        (rN, rD) = ratio.as_integer_ratio()
        ratio = rN * pow(rD, -1, M) %M if not rD == 1 else rN
        ratio = rem_mod_odd_(M, ratio)
        if not _01_ok and 0 <= ratio <= 1:raise ValueError(M, ratio0, ratio)
        assert abs(ratio) <= M//2
        #.if 2*ratio %M == 1:
        #.    ratio = ...
        #.else:
        #.    assert abs(ratio) <= M//2 -(ratio < 0)
        ratio
    ratio

    #.if not ratio is ...:
    #.    check_type_is(int, ratio)
    #.    assert -(H:=M//2) < ratio <= H
    #.        # -H --> ...
    #.    assert _01_ok or not 0 <= ratio <= 1
    assert abs(ratio) <= M//2
    assert _01_ok or not 0 <= ratio <= 1
    return ratio

def mk_u2next_u__7quadratic_attract_(M, D, /, *, ratio=None, exp=2):
    check_int_ge(2, exp)
    check_odd_uint_(M)
    D = rem_mod_odd_(M, D)
    if D == 0:raise ValueError(M, D)

    ratio = mk_std_ratio_(M, exp, ratio)
    if not 2*ratio%M == 1:
        #if not ratio is ...:
        lhs_ratio = 1-ratio
        rhs_ratio = ratio
        u2next_u_ = _2_mk_u2next_u__7quadratic_attract_(M, D, exp, lhs_ratio, rhs_ratio)
    else:
        # [ratio == 1/2]
        u2next_u_ = _1_mk_u2next_u__7quadratic_attract_(M, D, exp)
    return u2next_u_
def _2_mk_u2next_u__7quadratic_attract_(M, D, exp, lhs_ratio, rhs_ratio, /):
    assert exp >= 2
    def u2next_u_(u, /):
        #调整比率
        #
        #view script/整数分解牜尸方法牜吸引子.py
        #   『逐步搜索』『Mbac2f_args_』
            #森林结构只有两种:假设[M素数]:
            #    [x1 == x0/2 +Dn/x0/2][Dn%4 < 2][Jacobi_symbol(M; Dn) == -1]
            #    [x1 == x0/2 +Dp/x0/2][Dp%4 < 2][Jacobi_symbol(M; Dp) == +1]
        try:
            v = pow(u, -1, M)
                # ^ValueError: base is not invertible for the given modulus
        except ValueError:
            g = gcd(u, M)
            return g
        v
        #z1 = (lhs_ratio*u+rhs_ratio*D*v) %M
        z1 = (lhs_ratio*u+rhs_ratio*D*pow(v, (exp-1), M)) %M
        return z1
    u2next_u_
    return u2next_u_


def _1_mk_u2next_u__7quadratic_attract_(M, D, exp, /):
    # [ratio == 1/2]
    assert exp >= 2
    def u2next_u_(u, /):
        #view script/整数分解牜尸方法牜吸引子.py
        #   『逐步搜索』『Mbac2f_args_』
            #森林结构只有两种:假设[M素数]:
            #    [x1 == x0/2 +Dn/x0/2][Dn%4 < 2][Jacobi_symbol(M; Dn) == -1]
            #    [x1 == x0/2 +Dp/x0/2][Dp%4 < 2][Jacobi_symbol(M; Dp) == +1]
        try:
            v = pow(u, -1, M)
                # ^ValueError: base is not invertible for the given modulus
        except ValueError:
            g = gcd(u, M)
            return g
        v
        #z1_z1 = (u+D*v) %M
        z1_z1 = (u+D*pow(v, (exp-1), M)) %M
        z1 = div2_mod_odd_(M, z1_z1)
        return z1
    u2next_u_
    return u2next_u_

def div2_mod_odd_(M, x, /):
    if x&1:
        x += M
    assert x&1 == 0
    x >>= 1
    x %= M
    return x

def _iter_both_neg_pos_(ratios, /):
    for ratio in ratios:
        yield ratio
        #if not (ratio is ... or ratio is None):
        yield -ratio

def try_factor_pint7iter_rho_method7gcd7quadratic_attract__ratios_(ratios, M, u0, max_num_steps_per_D, Ds, /, *, exp=2, more_info=False, neg_Jacobi_symbol_only=False, neg_ratio_too=False, print6KeyboardInterrupt=print, resume=False):
    'Iter (may ratio/Rational) -> M/uint{>0} -> u/uint%M -> max_num_steps_per_D/uint -> Iter D/uint%M -> may facfor4M/uint'
    _01_ok = True
    ratios = iter_mk_std_ratios_(M, exp, ratios, _01_ok=_01_ok)
    if neg_ratio_too:
        ratios = _iter_both_neg_pos_(ratios)

    ratio7inv_exp = mk_std_ratio_(M, exp, None) #1/exp
    ratio7inv_z = mk_std_ratio_(M, exp, ...) #1/2

    ratio_set = set()
    ls = []
    may_g = None
    for ratio in ratios:
        #ratio = mk_std_ratio_(M, exp, ratio, _01_ok=_01_ok)
        #if not ratio is ... and 0 <= ratio <= 1:continue
        if 0 <= ratio <= 1:continue
        if ratio in ratio_set:continue
        ratio_set.add(ratio)
        (may_g, info) = try_factor_pint7iter_rho_method7gcd7quadratic_attract_(M, u0, max_num_steps_per_D, Ds, more_info=True, neg_Jacobi_symbol_only=neg_Jacobi_symbol_only, ratio=ratio, exp=exp, print6KeyboardInterrupt=print6KeyboardInterrupt, resume=resume)
        if ratio == ratio7inv_exp:
            _ratio = None
        elif ratio == ratio7inv_z:
            _ratio = ...
        else:
            _ratio = ratio
        ls.append([(_ratio, info)])
        if may_g: break
    return may_g if not more_info else (may_g, ls)
def try_factor_pint7iter_rho_method7gcd7quadratic_attract_(M, u0, max_num_steps_per_D, Ds, /, *, more_info=False, neg_Jacobi_symbol_only=False, ratio=None, exp=2, print6KeyboardInterrupt=print, resume=False):
    'M/uint{>0} -> u/uint%M -> max_num_steps_per_D/uint -> Iter D/uint%M -> may facfor4M/uint'
    check_int_ge(1, max_num_steps_per_D)
    check_odd_uint_(M)
    u0 %= M
    if neg_Jacobi_symbol_only:
        def is_D_ok_(D, /):
            return Jacobi_symbol(M, D) == -1
    else:
        def is_D_ok_(D, /):
            return True
    is_D_ok_

    num_Ds = 0
    for D in Ds:
        if D == 0: continue
        if not is_D_ok_(D): continue
        num_Ds += 1
        if resume and num_Ds > 1:raise ValueError('resume and num_Ds > 1')
        it = iter_rho_method4factor_pint7gcd7quadratic_attract_(M, D, u0, ratio=ratio, exp=exp, print6KeyboardInterrupt=print6KeyboardInterrupt, resume=resume)
        it = islice(it, 0, max_num_steps_per_D)
        for (bstop, g, ti, tj) in it:
            if bstop and 1 < g < M:
                assert M%g == 0
                if more_info:
                    j = tj[0]
                    info = (M, u0, num_Ds, D, j)
                    return (g, info)
                return g
    if more_info:
        return (None, num_Ds)
    return None

class _Ops8u2next_u_:
    #u2next_u_
    def __init__(sf, M, /):
        sf._M = M
    def pow_u_u_(sf, u, /):
        #view script/模幂注入.py
        M = sf._M
        return pow(u, u, M)
    def pow_u_rru_(sf, u, /):
        M = sf._M
        if u == 0: return u
        ru = M%u
        if ru == 0: return ru
        rru = u%ru
        return pow(u, rru, M)
    def random_walk_1_(sf, u, /):
        'bad'
        M = sf._M
        match u&255:
            case 0:
                r = (pow(u, 2, M)+1)
            case 1:
                r = u ^ M
            case 2:
                r = u & M
            case 3:
                r = u | M
            case 4:
                r = 999*u
            case 5:
                r = -233*u
            case r:
                r **= 3
                r *= u
        return r%M
    def add_1_pow_u_2_(sf, u, /):
        M = sf._M
        return (1+pow(u, 2, M))%M
    def add_B_pow_u_2_(sf, B, u, /):
        M = sf._M
        return (B+pow(u, 2, M))%M
def prepare_u2next_u_(M, u2next_u_, /):
    if type(u2next_u_) is str:
        nm = u2next_u_
        u2next_u_ = mk_u2next_u__5name_(M, nm)
    check_callable(u2next_u_)
    return u2next_u_
def mk_u2next_u__5name_(M, nm, /):
    assert not nm.startswith('_')
    ops = _Ops8u2next_u_(M)
    u2next_u_ = getattr(ops, nm)
    return u2next_u_

def try_factor_pint7iter_rho_method7gcd_(u2next_u_, M, max_num_steps_per_u0, u0s, /, *, more_info=False, extra_args=(), gcd_with_more=1, print6KeyboardInterrupt=print, resume=False):
    '((u->u)|name/str) -> M/uint{>0} -> max_num_steps_per_u0/uint -> Iter u0/uint%M -> may facfor4M/uint'
    check_int_ge(1, max_num_steps_per_u0)
    check_odd_uint_(M)
    u2next_u_ = prepare_u2next_u_(M, u2next_u_)
    #def is_u0_ok_(u0, /): return True
    #is_u0_ok_

    num_u0s = 0
    #u0_set = set()
    for u0 in u0s:
        u0 %= M
        #if u0 == 0: continue
        #if not is_u0_ok_(u0): continue
        #if u0 in u0_set: continue
        #u0_set.add(u0)

        num_u0s += 1
        if resume and num_u0s > 1:raise ValueError('resume and num_u0s > 1')
        it = iter_rho_method4factor_pint7gcd_(M, u0, u2next_u_, extra_args=extra_args, gcd_with_more=gcd_with_more, print6KeyboardInterrupt=print6KeyboardInterrupt, resume=resume)
        it = islice(it, 0, max_num_steps_per_u0)
        for (bstop, g, ti, tj) in it:
            if bstop and 1 < g < M:
                assert M%g == 0
                if more_info:
                    j = tj[0]
                    info = (M, num_u0s, u0, j)
                    return (g, info)
                return g
    if more_info:
        return (None, num_u0s)
    return None

def try7iter_rho_method7default_(max_num_steps_per_xs, xss, /, x2key_=None, test_=None, stop_=None, *, ok_=None, more_info=False, print6KeyboardInterrupt=print, ixi_j4resume=None):
    check_int_ge(1, max_num_steps_per_xs)
    #ok_ = ifNone(ok_, bool)
    ok_ = ifNone(ok_, lambda r:True)

    resume = not ixi_j4resume is None
    xss

    num_xss = 0
    for xs in xss:
        num_xss += 1
        if resume and num_xss > 1:raise ValueError('[not ixi_j4resume is None][len(xss) > 1]')
        it = iter_rho_method__5iter__7default_(xs, x2key_, test_, stop_, print6KeyboardInterrupt=print6KeyboardInterrupt, ixi_j4resume=ixi_j4resume)
        it = islice(it, 0, max_num_steps_per_xs)
        for (bstop, r, ti, tj) in it:
            if bstop and ok_(r):
                if more_info:
                    j = tj[0]
                    info = (num_xss, j)
                    return (r, info)
                return r
    if more_info:
        return (None, num_xss)
    return None





__all__
from seed.algo.rho_method__7iter import *
