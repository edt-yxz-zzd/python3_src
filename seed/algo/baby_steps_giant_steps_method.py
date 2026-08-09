#__all__:goto
r'''[[[
e ../../python3_src/seed/algo/baby_steps_giant_steps_method.py
    DL:discrete_logarithm

view ../../python3_src/seed/math/discrete_logarithm.py


seed.algo.baby_steps_giant_steps_method
py -m nn_ns.app.debug_cmd   seed.algo.baby_steps_giant_steps_method -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.algo.baby_steps_giant_steps_method:__doc__ -ht # -ff -df
#######

[[
大小步碰撞:baby_steps_giant_steps_method#Shanks method

come_from:
view ../../python3_src/seed/math/BinaryQuadraticForm.py
    群规模计算牜大小步碰撞
    pari-gp:『?? qfbclassno』

view ../../python3_src/seed/math/factor_pint/smooth_group_order_method.py
]]


'#'; __doc__ = r'#'


view ../../python3_src/nn_ns/math_nn/numbers/_patch_prime_..b001918.b002233.out.txt
    7 19 2 2
    66 331 3 3
    9999 104729 12 23
>>> 104729 == +1+2**3 *13 *19 *53
True
>>> (19**2)
361
>>> pow(2, 18*19//19, 19**2)
58
>>> pow(2, 18*19//2, 19**2)
360
>>> pow(2, 18*19//3, 19**2)
292

[y==x**2+x-1]:
    (x,y)
    (7,55)
>>> 5*11 == 7**2+7-1
True
>>> 1+6 *55
331


def baby_steps_giant_steps_method_(offset4exp, min_num_fwd_giant_steps, max_num_fwd_giant_steps, sz4giant_step, mul_, pow_, base, target, /, *, key=None, hash_vs_sort=False):

>>> from math import isqrt
>>> M = 104729
>>> base = 12
>>> target = 23
>>> mul_ = lambda a,b,/:a*b%M
>>> pow_ = lambda a,e,/:pow(a,e,M)
>>> sz = 1+isqrt(M)
>>> baby_steps_giant_steps_method_(0, 0, sz, sz, mul_, pow_, base, target)
(68, 317, 22349)
>>> exp = 22349
>>> pow_(base, exp) == target
True
>>> sz = 1+isqrt(exp)
>>> baby_steps_giant_steps_method_(0, 0, sz, sz, mul_, pow_, base, target)
(148, 149, 22349)
>>> sz = 0+isqrt(exp)
>>> baby_steps_giant_steps_method_(0, 0, sz, sz, mul_, pow_, base, target) # ??? not is None
(149, 148, 22349)
>>> baby_steps_giant_steps_method_(0, 0, sz, -1+sz, mul_, pow_, base, target) # is None
>>> baby_steps_giant_steps_method_(0, 0, -1+sz, sz, mul_, pow_, base, target) # is None

>>> offset4exp = exp
>>> sz = 1
>>> baby_steps_giant_steps_method_(offset4exp, 0, 0, 1, mul_, pow_, base, target)
(0, 0, 22349)

>>> offset4exp = exp+4
>>> baby_steps_giant_steps_method_(offset4exp, -2, 2, 2, mul_, pow_, base, target)
(-2, 0, 22349)
>>> baby_steps_giant_steps_method_(offset4exp, -2, 0, 2, mul_, pow_, base, target)
(-2, 0, 22349)
>>> baby_steps_giant_steps_method_(offset4exp, -2, -1, 2, mul_, pow_, base, target)
(-2, 0, 22349)
>>> baby_steps_giant_steps_method_(offset4exp, -2, -2, 2, mul_, pow_, base, target)
(-2, 0, 22349)

>>> baby_steps_giant_steps_method_(offset4exp, 2, 2, 2, mul_, pow_, base, target)
>>> baby_steps_giant_steps_method_(offset4exp, 1, 2, 2, mul_, pow_, base, target)
>>> baby_steps_giant_steps_method_(offset4exp, 0, 2, 2, mul_, pow_, base, target)
>>> baby_steps_giant_steps_method_(offset4exp, -1, 2, 2, mul_, pow_, base, target)
>>> baby_steps_giant_steps_method_(offset4exp, -2, 2, 2, mul_, pow_, base, target)
(-2, 0, 22349)


>>> baby_steps_giant_steps_method_(0, 0, 0, 4, mul_, pow_, base, pow_(base, 4))
>>> baby_steps_giant_steps_method_(0, 0, 0, 4, mul_, pow_, base, pow_(base, 3))
(0, 3, 3)


>>> baby_steps_giant_steps_method_(0, 0, 0, 1, mul_, pow_, M-1, target)
>>> baby_steps_giant_steps_method_(0, 0, 0, 2, mul_, pow_, M-1, target)
>>> baby_steps_giant_steps_method_(0, 0, 0, 3, mul_, pow_, M-1, target)
Traceback (most recent call last):
    ...
seed.algo.baby_steps_giant_steps_method.SmallMulOrderException: (3, 2, 104728)




search_multiple_of_mul_order__7baby_steps_giant_steps_method_
>>> sz = 1+isqrt(M)
>>> search_multiple_of_mul_order__7baby_steps_giant_steps_method_(0, 0, sz, sz, mul_, pow_, base)
104728
>>> search_multiple_of_mul_order__7baby_steps_giant_steps_method_(0, 0, sz, sz, mul_, pow_, base, hash_vs_sort=True)
104728
>>> search_multiple_of_mul_order__7baby_steps_giant_steps_method_(0, 0, 0, 2, mul_, pow_, M-1)
>>> search_multiple_of_mul_order__7baby_steps_giant_steps_method_(0, 0, 0, 3, mul_, pow_, M-1)
2

_debug
>>> search_multiple_of_mul_order__7baby_steps_giant_steps_method_(0, 0, 0, 3, mul_, pow_, M-1, _debug=True)
2
>>> search_multiple_of_mul_order__7baby_steps_giant_steps_method_(0, 0, 1, 2, mul_, pow_, M-1, _debug=True)
2
>>> search_multiple_of_mul_order__7baby_steps_giant_steps_method_(0, 0, 2, 1, mul_, pow_, M-1, _debug=True)
2






search_mul_order__7baby_steps_giant_steps_method_
>>> sz = 1+isqrt(M)
>>> search_mul_order__7baby_steps_giant_steps_method_(sz, mul_, pow_, base)
104728












velidate:
    [0 < mul_order4base < sz4giant_step*(1+sz4giant_step)]

>>> M = 361
>>> base = 2 # [mul_order_(%361;2) == 18*(1+18)]
>>> sz = 18
>>> search_mul_order__7baby_steps_giant_steps_method_(sz, mul_, pow_, base) is None
True
>>> sz = 19
>>> search_mul_order__7baby_steps_giant_steps_method_(sz, mul_, pow_, base)
342

>>> M = 331
>>> g = 3 # [mul_order_(%331;3) == 6*55]
>>> base = pow_(3,6) # [mul_order_(%331;3**6) == 55]
>>> base # [mul_order_(%331;67) == 55 == -1+7*(1+7)]
67
>>> sz = 7
>>> search_mul_order__7baby_steps_giant_steps_method_(sz, mul_, pow_, base)
55











py_adhoc_call   seed.algo.baby_steps_giant_steps_method   @f
]]]'''#'''
__all__ = r'''
search_mul_order__7baby_steps_giant_steps_method_
    search_multiple_of_mul_order__7baby_steps_giant_steps_method_
        baby_steps_giant_steps_method_
            SmallMulOrderException
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
    from seed._lazy_ import echo, ifNone, fst# print_err
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge
    from itertools import pairwise#islice
    from bisect import bisect_left
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


class SmallMulOrderException(Exception):
    def __init__(sf, sz4giant_step, mul_order4base, base, /):
        assert mul_order4base > 0
        super().__init__(sz4giant_step, mul_order4base, base)
        sf.sz4giant_step = sz4giant_step
        sf.mul_order4base = mul_order4base
        sf.base = base
    pass

def _eq_(key, lhs, rhs, /):
    key = ifNone(key, echo)
    return key(lhs) in [key(rhs)]
def search_mul_order__7baby_steps_giant_steps_method_(sz4giant_step, mul_, pow_, base, /, *, key=None, hash_vs_sort=False, _debug=False):
    'sz4giant_step/uint{>0} -> mul_/(R->R->R) -> pow_/(R->int->R) -> base/R -> may mul_order4base/int{=!=0} # [base**mul_order4base == one][0 =!= mul_order4base][mul_order4base == mul_order_(base)][0 < mul_order4base < sz4giant_step*(1+sz4giant_step)] # DL:discrete_logarithm'
    return search_multiple_of_mul_order__7baby_steps_giant_steps_method_(offset4exp:=0, min_num_fwd_giant_steps:=0, max_num_fwd_giant_steps:=sz4giant_step, sz4giant_step, mul_, pow_, base, key=key, hash_vs_sort=hash_vs_sort, _debug=_debug)
def search_multiple_of_mul_order__7baby_steps_giant_steps_method_(offset4exp, min_num_fwd_giant_steps, max_num_fwd_giant_steps, sz4giant_step, mul_, pow_, base, /, *, key=None, hash_vs_sort=False, _debug=False):
    'offset4exp/int -> min_num_fwd_giant_steps/int -> max_num_fwd_giant_steps/int -> sz4giant_step/uint{>0} -> mul_/(R->R->R) -> pow_/(R->int->R) -> base/R -> may exp/int{=!=0} # [base**exp == one][exp%mul_order_(base) == 0][0 =!= exp][min_num_fwd_giant_steps <= (exp-offset4exp)/sz4giant_step < 1+max_num_fwd_giant_steps] # DL:discrete_logarithm'
    # no: ^SmallMulOrderException(sz4giant_step, mul_order4base, base)
    target = one = pow_(base, 0)
    m = baby_steps_giant_steps_method_(offset4exp, min_num_fwd_giant_steps, max_num_fwd_giant_steps, sz4giant_step, mul_, pow_, base, target, key=key, hash_vs_sort=hash_vs_sort, _debug=_debug, to_raise_vs_return_mul_order4base=True)
    match m:
        case None:
            return None
        case (k, j, exp):
            multiple4mul_order4base = exp
        case ('mul_order', mul_order4base):
            multiple4mul_order4base = mul_order4base
        case _:
            raise 000
    multiple4mul_order4base
    if _debug:
        assert min_num_fwd_giant_steps*sz4giant_step <= (multiple4mul_order4base -offset4exp) < (1+max_num_fwd_giant_steps)*sz4giant_step
        #assert one == pow_(base, multiple4mul_order4base)
        assert _eq_(key, one, pow_(base, multiple4mul_order4base))
    # [min_num_fwd_giant_steps <= (multiple4mul_order4base -offset4exp)/sz4giant_step < (1+max_num_fwd_giant_steps)]
    # [one == base**multiple4mul_order4base]
    return multiple4mul_order4base

def baby_steps_giant_steps_method_(offset4exp, min_num_fwd_giant_steps, max_num_fwd_giant_steps, sz4giant_step, mul_, pow_, base, target, /, *, key=None, hash_vs_sort=False, to_raise_vs_return_mul_order4base=False, _debug=False):
    'offset4exp/int -> min_num_fwd_giant_steps/int -> max_num_fwd_giant_steps/int -> sz4giant_step/uint{>0} -> mul_/(R->R->R) -> pow_/(R->int->R) -> base/R -> target/R -> may (k/int,j/uint%sz4giant_step,exp/int{=!=0})|(^SmallMulOrderException(sz4giant_step, mul_order4base, base) if not to_raise_vs_return_mul_order4base else ("mul_order", mul_order4base)) # [base**exp == target][0 =!= exp == offset4exp+k*sz4giant_step+j][0 <= j < sz4giant_step][-num_bwd_giant_steps <= k <= num_fwd_giant_steps] # [min_num_fwd_giant_steps <= (exp-offset4exp)/sz4giant_step < 1+max_num_fwd_giant_steps] # DL:discrete_logarithm'
    if to_raise_vs_return_mul_order4base:
        # to return if found mul_order4base
        try:
            return baby_steps_giant_steps_method_(offset4exp, min_num_fwd_giant_steps, max_num_fwd_giant_steps, sz4giant_step, mul_, pow_, base, target, key=key, hash_vs_sort=hash_vs_sort, _debug=_debug, to_raise_vs_return_mul_order4base=not to_raise_vs_return_mul_order4base)
        except SmallMulOrderException as exc:
            mul_order4base = exc.mul_order4base
            return ('mul_order', mul_order4base)
        raise 000
    # to raise if found mul_order4base
    ###########################
    key = ifNone(key, echo)
    hash_vs_sort = bool(hash_vs_sort)
    check_type_is(int, offset4exp)
    check_type_is(int, min_num_fwd_giant_steps)
    check_int_ge(min_num_fwd_giant_steps, max_num_fwd_giant_steps)
    # [min_num_fwd_giant_steps <= max_num_fwd_giant_steps]
    check_int_ge(1, sz4giant_step)

    ###########################
    #rename:API-changed
    ###########################
    num_bwd_giant_steps = -min_num_fwd_giant_steps
    num_fwd_giant_steps = max_num_fwd_giant_steps
    # [-num_bwd_giant_steps <= num_fwd_giant_steps]
    ###########################



    ###########################
    #virtual member function:hash_vs_sort
    ###########################
    if hash_vs_sort:
        #sort
        ts = []
            # :: [(key{g**j}, j, g**j)]
        def add7baby_step_(j, pw, /):
            ts.append((key(pw), j, pw))
        def post7baby_step_():
            ts.sort()
            mul_order4base = None
            for (_ky, _j, _), (ky, j, _) in pairwise(ts):
                if _ky == ky:
                    #bug:assert _j == 0 # => mul_order4base
                    assert _j < j, (_ky, ky, _j, j)
                    _mul_order4base = abs(j-_j)
                    if mul_order4base is None:
                        mul_order4base = _mul_order4base
                    else:
                        assert mul_order4base == _mul_order4base, (_ky, ky, _j, j, mul_order4base, _mul_order4base)
            mul_order4base
            if not mul_order4base is None:
                raise SmallMulOrderException(sz4giant_step, mul_order4base, base)
        def search7giant_step_(k, pt, /):
            ky4pt = key(pt)
            idx = bisect_left(ts, ky4pt, key=fst)
            if idx == len(ts) or not ts[idx][0] == ky4pt:
                return None
            (ky4pw, j, pw) = ts[idx]
            return (j, pw)
    else:
        #hash
        d = {}
            # :: {key{g**j}: (j, g**j)}
        def add7baby_step_(j, pw, /):
            #d[key(pw)] = (j, pw)
            match d.setdefault(key(pw), (j, pw)):
                case (_j, _pw) if not _j == j:
                    assert _j < j, (_pw, pw, _j, j)
                    assert _j == 0 # => mul_order4base
                    mul_order4base = abs(j-_j)
                    raise SmallMulOrderException(sz4giant_step, mul_order4base, base)
            pass
        def post7baby_step_():
            pass
        def search7giant_step_(k, pt, /):
            ky4pt = key(pt)
            return d.get(ky4pt)

    add7baby_step_
    post7baby_step_
    search7giant_step_
    ###########################




    ###########################
    #baby_steps
    ###########################
    one = pow_(base, 0)
    j = 0
    777;pw = one
    for j in range(0, sz4giant_step):
        # [pw == base**j]
        add7baby_step_(j, pw)
            # ^SmallMulOrderException
        pw = mul_(pw, base)
    # [pw == base**sz4giant_step]
    # !! at rhs: neg exp for fwd
    giant_step7bwd = pw
    giant_step7fwd = pow_(giant_step7bwd, -1)
    # [giant_step7bwd  == base**+sz4giant_step]
    # [giant_step7fwd  == base**-sz4giant_step]

    post7baby_step_()
        # ^SmallMulOrderException
    ###########################




    ###########################
    #navigation:giant_steps
    ###########################
    pt0 = mul_(target, pow_(base, -offset4exp))
    # [pt0 == target*base**-(offset4exp+sz4giant_step*0)]

    # !! [-num_bwd_giant_steps <= num_fwd_giant_steps]
    if -num_bwd_giant_steps <= 0 <= num_fwd_giant_steps:
        tmay_pairs6zero = [(0, pt0)]
        pt7fwd = pt0
        ks7pos = range(1, 1+num_fwd_giant_steps)
        pt7bwd = pt0
        ks7neg = range(-num_bwd_giant_steps, 0)[::-1]
    elif 0 < -num_bwd_giant_steps <= num_fwd_giant_steps:
        tmay_pairs6zero = []
        pt7fwd = mul_(pt0, pow_(giant_step7fwd, -1-num_bwd_giant_steps))
        ks7pos = range(-num_bwd_giant_steps, 1+num_fwd_giant_steps)
        pt7bwd = object()
        ks7neg = ()
    elif -num_bwd_giant_steps <= num_fwd_giant_steps < 0:
        tmay_pairs6zero = []
        pt7bwd = mul_(pt0, pow_(giant_step7bwd, -1-num_fwd_giant_steps))
        ks7neg = range(-num_bwd_giant_steps, 1+num_fwd_giant_steps)[::-1]
        pt7fwd = object()
        ks7pos = ()
    else:
        raise 000
    ks7pos = iter(ks7pos)
    ks7neg = iter(ks7neg)
    pt7fwd
    pt7bwd
    tmay_pairs6zero


    def iter_ks_(ks7neg, ks7pos, /):
        '-> sorted{key=abs}-Iter k # [[k++ for k >= 0][k-- for k <= 0]]'
        try:
            while 1:
                b = False
                yield next(ks7pos)
                b = True
                yield next(ks7neg)
        except StopIteration:
            pass
        if b:
            [] = ks7neg
            ks = ks7pos
        else:
            [] = ks7pos
            ks = ks7neg
        ks
        yield from ks
    def iter_k_pt_pairs_(tmay_pairs6zero, pt7fwd, pt7bwd, ks, /):
        '-> sorted{key=abs.fst}-Iter (k,pt) # [pt == pt0*giant_step7fwd**k] # [[k++ for k >= 0][k-- for k <= 0]]'
        yield from tmay_pairs6zero
            # [k == 0]
        for k in ks:
            # [k =!= 0]
            if k < 0:
                pt = pt7bwd = mul_(pt7bwd, giant_step7bwd)
            else:
                pt = pt7fwd = mul_(pt7fwd, giant_step7fwd)
            # [pt == pt0*giant_step7fwd**k]
            yield (k, pt)
    iter_ks_
    iter_k_pt_pairs_

    k_pt_pairs = iter_k_pt_pairs_(tmay_pairs6zero, pt7fwd, pt7bwd, iter_ks_(ks7neg, ks7pos))
    ###########################




    ###########################
    #giant_steps
    ###########################
    #_debug = True
    #_debug = False
    if _debug:
        #assert pt0 == mul_(target, pow_(base, -offset4exp))
        assert _eq_(key, pt0, mul_(target, pow_(base, -offset4exp)))
    # [pt0 == target*base**-(offset4exp+sz4giant_step*0)]
    for k, pt in k_pt_pairs:
        if _debug:
            assert -num_bwd_giant_steps <= k <= num_fwd_giant_steps
            #assert pt == mul_(pt0, pow_(giant_step7fwd, k))
            assert _eq_(key, pt, mul_(pt0, pow_(giant_step7fwd, k)))
        # [-num_bwd_giant_steps <= k <= num_fwd_giant_steps]
        # [pt == pt0*giant_step7fwd**k]
        match search7giant_step_(k, pt):
            case None:
                continue
            case (j, pw):
                if _debug:
                    assert 0 <= j < sz4giant_step
                    #assert pw == pt
                    #assert pw == pow_(base, j)
                    assert _eq_(key, pw, pt)
                    assert _eq_(key, pw, pow_(base, j))
                # [0 <= j < sz4giant_step]
                # [pt == pw]
                # !! [pw == base**j]
                # [pt == base**j]

                # !! [pt == pt0*giant_step7fwd**k]
                # !! [giant_step7fwd  == base**-sz4giant_step]
                # [pt == pt0*base**-(sz4giant_step*k)]
                # !! [pt0 == target*base**-(offset4exp+sz4giant_step*0)]
                # [pt == target*base**-(offset4exp+sz4giant_step*k)]
                # !! [pt == base**j]
                # [base**j == target*base**-(offset4exp+sz4giant_step*k)]
                # [target == base**(offset4exp+sz4giant_step*k+j)]
                exp = (offset4exp+sz4giant_step*k+j)
                if exp == 0: continue
                # [0 =!= exp == offset4exp+k*sz4giant_step+j]
                # [base**exp == target]
                return (k, j, exp)
            case _:
                raise 000
        raise 000
    return None
    ###########################











__all__
from seed.algo.baby_steps_giant_steps_method import search_mul_order__7baby_steps_giant_steps_method_, search_multiple_of_mul_order__7baby_steps_giant_steps_method_, baby_steps_giant_steps_method_, SmallMulOrderException
#def search_mul_order__7baby_steps_giant_steps_method_(sz4giant_step, mul_, pow_, base, /, *, key=None, hash_vs_sort=False, _debug=False):
#def search_multiple_of_mul_order__7baby_steps_giant_steps_method_(offset4exp, min_num_fwd_giant_steps, max_num_fwd_giant_steps, sz4giant_step, mul_, pow_, base, /, *, key=None, hash_vs_sort=False):
#def baby_steps_giant_steps_method_(offset4exp, min_num_fwd_giant_steps, max_num_fwd_giant_steps, sz4giant_step, mul_, pow_, base, target, /, *, key=None, hash_vs_sort=False, to_raise_vs_return_mul_order4base=False, _debug=False):
#SmallMulOrderException{.mul_order4base,.base,.sz4giant_step}

from seed.algo.baby_steps_giant_steps_method import *
