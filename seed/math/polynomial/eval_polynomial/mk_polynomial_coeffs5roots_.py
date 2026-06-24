#__all__:goto
r'''[[[
e ../../python3_src/seed/math/polynomial/eval_polynomial/mk_polynomial_coeffs5roots_.py

seed.math.polynomial.eval_polynomial.mk_polynomial_coeffs5roots_
py -m nn_ns.app.debug_cmd   seed.math.polynomial.eval_polynomial.mk_polynomial_coeffs5roots_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.polynomial.eval_polynomial.mk_polynomial_coeffs5roots_:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> from seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression import poly_evals__7native_
>>> from seed.algo.FFT.convolution import mk_ops4convolution7symbolic_FFT__5modulus_

>>> modulus = 0
>>> _0_opsN = mk_ops4convolution7symbolic_FFT__5modulus_(modulus)


>>> kwds = dict(auto_vs_native_vs_fancy=2) #force fancy
>>> mul7polynomial_(_0_opsN, [], [], **kwds)
[]
>>> mul7polynomial_(_0_opsN, [], [1], **kwds)
[]
>>> mul7polynomial_(_0_opsN, [3], [2], **kwds)
[6]
>>> mul7polynomial_(_0_opsN, [3, 5], [2], **kwds)
[6, 10]
>>> mul7polynomial_(_0_opsN, [3, 5], [2, 7], **kwds)
[6, 31, 35]



>>> kwds = dict(min_len4recur=0) #force fancy
>>> mk_polynomial_coeffs5roots_(_0_opsN, [], **kwds)
[1]
>>> mk_polynomial_coeffs5roots_(_0_opsN, [2], **kwds)
[-2, 1]
>>> mk_polynomial_coeffs5roots_(_0_opsN, [2, 7], **kwds)
[14, -9, 1]
>>> mk_polynomial_coeffs5roots_(_0_opsN, [2, 7, 1], **kwds)
[-14, 23, -10, 1]
>>> mk_polynomial_coeffs5roots_(_0_opsN, [2, 7, 1, 3], **kwds)
[42, -83, 53, -13, 1]
>>> mk_polynomial_coeffs5roots_(_0_opsN, [2, 7, 1, 3, 5], **kwds)
[-210, 457, -348, 118, -18, 1]
>>> mk_polynomial_coeffs5roots__7native_(_0_opsN, [2, 7, 1, 3, 5])
[-210, 457, -348, 118, -18, 1]

>>> args = (_0_opsN.add_, _0_opsN.mul_, _0_opsN.zero)
>>> poly_evals__7native_(*args, [-14, 23, -10, 1], [2, 7, 1, 3])
[0, 0, 0, -8]

>>> poly_evals__7native_(*args, [42, -83, 53, -13, 1], [2, 7, 1, 3])
[0, 0, 0, 0]




def mk_polynomial_coeffs5roots_on_geometric_progression_(opsX, may_B, T, sz, /, *, min_len4recur=_default4min_len4recur):
>>> kwds = dict(min_len4recur=0) #force fancy
>>> _257_opsN = mk_ops4convolution7symbolic_FFT__5modulus_(257)
>>> mk_polynomial_coeffs5roots_on_geometric_progression_(_257_opsN, 1, 2, 5, **kwds)
[4, -72, 45, 53, -31, 1]
>>> mk_polynomial_coeffs5roots_on_geometric_progression_(_257_opsN, 3, 2, 5, **kwds)
[-56, 79, -70, -37, -93, 1]
>>> mk_polynomial_coeffs5roots_on_geometric_progression__7native_(_257_opsN, 3, 2, 5)
[-56, 79, -70, -37, -93, 1]
>>> args = (_257_opsN.add_, _257_opsN.mul_, _257_opsN.zero)
>>> poly_evals__7native_(*args, [-56, 79, -70, -37, -93, 1], [3, 6, 12, 24, 48, 96])
[0, 0, 0, 0, 0, -56]
>>> poly_evals__7native_(*args, [4, -72, 45, 53, -31, 1], [1, 2, 4, 8, 16, 32])
[0, 0, 0, 0, 0, 4]



>>> mk_polynomial_coeffs5roots_on_geometric_progression__7native_(_257_opsN, 3, 2, 16)
[8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
>>> mk_polynomial_coeffs5roots_on_geometric_progression_(_257_opsN, 3, 2, 16, optimized6zpow=False)
[8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
>>> mk_polynomial_coeffs5roots_on_geometric_progression_(_257_opsN, 3, 2, 16, optimized6zpow=True)
[8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

>>> mk_polynomial_coeffs5roots_on_geometric_progression__7native_(_257_opsN, 3, 7, 16)
[-30, 35, -63, -113, 94, 94, 19, -56, 58, 30, -27, 59, 51, -127, -90, 65, 1]
>>> mk_polynomial_coeffs5roots_on_geometric_progression_(_257_opsN, 3, 7, 16, optimized6zpow=False)
[-30, 35, -63, -113, 94, 94, 19, -56, 58, 30, -27, 59, 51, -127, -90, 65, 1]
>>> mk_polynomial_coeffs5roots_on_geometric_progression_(_257_opsN, 3, 7, 16, optimized6zpow=True)
[-30, 35, -63, -113, 94, 94, 19, -56, 58, 30, -27, 59, 51, -127, -90, 65, 1]



>>> mk_polynomial_coeffs5roots_on_geometric_progression_(_257_opsN, 1, 2, 20, **kwds)
[-64, 120, -70, 15, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, -120, 70, -15, 1]

# (opsX, may_B, T, invT, sz):=(..., 16777216, 2, 73786976294838206464, 512)
>>> M67 = -1+2**67
>>> _M67_opsN = mk_ops4convolution7symbolic_FFT__5modulus_(M67)
>>> 2*73786976294838206464 %M67
1

>>> mk_polynomial_coeffs5roots_on_geometric_progression_(_M67_opsN, 16777216, 2, 73786976294838206464, 512, **kwds)  #doctest: +ELLIPSIS +SKIP
[576460752303423488, 1152921435887370240, 1537228535370178560, 29859294260464681740, ..., -47073627296167079618, -64529609978923588375, 45911958911335765997, 28109136652816625871, 187649967696555, 16777215, 1]


















py_adhoc_call   seed.math.polynomial.eval_polynomial.mk_polynomial_coeffs5roots_   @f

]]]'''#'''
__all__ = r'''
mul7polynomial_
mk_polynomial_coeffs5roots_
mk_polynomial_coeffs5roots_on_geometric_progression_

mk_polynomial_coeffs5roots__7native_
mk_polynomial_coeffs5roots_on_geometric_progression__7native_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.floor_ceil_tools.fc_log import ceil_log2, floor_log2
    from seed.tiny_.check import check_type_is, check_int_ge, check_uint_lt
    from seed.math.polynomial.eval_polynomial.eval_polynomial_on_geometric_progression import iter_geometric_progression_
    #def iter_geometric_progression_(mul_, B, T, /):
    from itertools import islice
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def _school_book_mul(opsX, coeffs8lhs, coeffs8rhs, /):
    cs = opsX.acyclic_convolution__lenO_eq__7native_(len(coeffs8lhs) + len(coeffs8rhs), coeffs8lhs, coeffs8rhs)
    cs.pop()
    return cs

def mul7polynomial_(opsX, coeffs8lhs, coeffs8rhs, /, *, auto_vs_native_vs_fancy=0):
    r'''[[[
    #########
    # [opsX == (opsG|opsN)]
    # [opsX :: (Ops4convolution7FFT|Ops4convolution7symbolic_FFT)]
    #########
    #]]]'''#'''
    if not (coeffs8lhs and coeffs8rhs):
        return []
    check_uint_lt(3, auto_vs_native_vs_fancy)
    zero = opsX.zero
    if len(coeffs8lhs) > len(coeffs8rhs):
        coeffs8lhs, coeffs8rhs = coeffs8rhs, coeffs8lhs
    # [len(coeffs8lhs) <= len(coeffs8rhs)]
    if auto_vs_native_vs_fancy == 0:
        #auto:
        native_vs_fancy = not len(coeffs8lhs) <= 2+len(coeffs8rhs).bit_length()
    else:
        # [auto_vs_native_vs_fancy <- {1,2}]
        native_vs_fancy = not auto_vs_native_vs_fancy == 1

    if not native_vs_fancy:
        #native:
        cs = _school_book_mul(opsX, coeffs8lhs, coeffs8rhs)
    else:
        # FFT:
        sz = len(coeffs8lhs) + len(coeffs8rhs)
        sz7zpow = 1<<ceil_log2(sz)
        d = sz7zpow -sz
        if d:
            coeffs8rhs = [*coeffs8rhs, *[zero]*d]
        assert sz7zpow == len(coeffs8lhs) + len(coeffs8rhs)
        cs = opsX.acyclic_convolution__7commonAPI_(coeffs8lhs, coeffs8rhs)
        del cs[sz-1:]
    cs
    return cs
    while cs and cs[-1] == zero:
        cs.pop()
    return cs
_default4min_len4recur = 32
    # <<== view ../../python3_src/seed/math/factor_pint/factor_pint__7batch_gcd_IIdiffs.py
def mk_polynomial_coeffs5roots_(opsX, roots, /, *, min_len4recur=_default4min_len4recur):
    r'''[[[
    #########
    # [opsX == (opsG|opsN)]
    # [opsX :: (Ops4convolution7FFT|Ops4convolution7symbolic_FFT)]
    #########
    #]]]'''#'''
    neg_ = opsX.neg_
    add_ = opsX.add_
    mul_ = opsX.mul_
    one = opsX.one
    def _4sz_lt3(roots, /):
        match roots:
            case [c, b]:
                return [mul_(c,b), neg_(add_(c,b)), one]
            case [c]:
                return [neg_(c), one]
            case []:
                return [one]
        raise Exception(roots)
    def _recur(roots, /):
        if len(roots) < 3:
            return _4sz_lt3(roots)
        if len(roots) < min_len4recur:
            return mk_polynomial_coeffs5roots__7native_(opsX, roots)
        h = len(roots)//2
        assert h > 0
        cs0 = _recur(roots[:h])
        cs1 = _recur(roots[h:])
        cs = mul7polynomial_(opsX, cs0, cs1)
        return cs
    return _recur(roots)
def mk_polynomial_coeffs5roots__7native_(opsX, roots, /):
    neg_ = opsX.neg_
    one = opsX.one
    cs = [one]
    for r in roots:
        cs = mul7polynomial_(opsX, [neg_(r), one], cs)
    return cs
def mk_polynomial_coeffs5roots_on_geometric_progression__7native_(opsX, may_B, T, sz, /):
    mul_ = opsX.mul_
    one = opsX.one

    B = one if may_B is None else may_B

    it = iter_geometric_progression_(mul_, B, T)
    roots = islice(it, 0, sz)
    return mk_polynomial_coeffs5roots__7native_(opsX, roots)
def mk_polynomial_coeffs5roots_on_geometric_progression_(opsX, may_B, T, sz, /, *, min_len4recur=_default4min_len4recur, optimized6zpow=False):
    r'''[[[
    #########
    # [opsX == (opsG|opsN)]
    # [opsX :: (Ops4convolution7FFT|Ops4convolution7symbolic_FFT)]
    #########
    update6odd:goto
    update4cs6even:goto

    [roots := [B*T**j | [j:<-[0..<sz]]]]
    [roots == B *. [T**j | [j:<-[0..<sz]]]]
    [roots == B *. (T **. [0..<sz])]

    [[
    [polynomial_geo{sz;B,T,X} := II[(X -B*T**j) | [j:<-[0..<sz]]]]
    [polynomial_geo{1+2*h;B,T,X} == (X-B*T**(2*h))*polynomial_geo{2*h;B,T,X}] # not good...
    [polynomial_geo{1+2*h;B,T,X} == (X-B)*polynomial_geo{2*h;B*T,T,X}] # update6odd:here

    [polynomial_geo{2*h;B,T,X}
    == II[(X -B*T**j) | [j:<-[0..<2*h]]]
    == II[(X -B*T**j) | [j:<-[0..<h]]]
    *  II[(X -B*T**j) | [j:<-[h..<2*h]]]
    == polynomial_geo{h;B,T,X}
    *  II[(X -B*T**(h+j)) | [j:<-[0..<h]]]
    == polynomial_geo{h;B,T,X}
    *  II[T**h*(X*T**-h -B*T**j) | [j:<-[0..<h]]]
    == polynomial_geo{h;B,T,X}
    *  T**(h**2) * II[(X*T**-h -B*T**j) | [j:<-[0..<h]]]
    == polynomial_geo{h;B,T,X}
    *  T**(h**2) * polynomial_geo{h;B,T,X*T**-h}
    ]
    [cs0 := polynomial_geo{h;B,T,X}.coeffs]
    [cs1 := T**(h**2) * polynomial_geo{h;B,T,X*T**-h}.coeffs]
    [T**(h**2) * sum[cs1[j]*X**j | [j:<-[0..=h]]]
    == T**(h**2) * polynomial_geo{h;B,T,X*T**-h}
    == T**(h**2) * sum[cs0[j]*(X*T**-h)**j | [j:<-[0..=h]]]
    == T**(h**2) * sum[cs0[j]*(T**-h)**j * X**j | [j:<-[0..=h]]]
    == sum[cs0[j]*T**(h**2-h*j) * X**j | [j:<-[0..=h]]]
    == sum[cs0[j]*(T**h)**(h-j) * X**j | [j:<-[0..=h]]]
    ]
    [cs1 == [cs0[j]*(T**h)**(h-j) | [j:<-[0..=h]]]]
    [cs1 == cs0 .*. [(T**h)**(h-j) | [j:<-[0..=h]]]]
    [cs1 == cs0 .*. (reverse [(T**h)**j | [j:<-[0..=h]]])]
    [cs1 == cs0 .*. (reverse (T**h) **. [0..=h])] # update4cs6even:here

    ]]

    @20260617:++kw:optimized6zpow
    #vs:optimized6zpowpp
    [sz > 0]:
        [polynomial_geo{sz;B,T,X}
        == II[(X -B*T**j) | [j:<-[0..<sz]]]
        == (X -B*T**0) * II[(X -B*T**j) | [j:<-[1..<sz]]]
        == (X-B) * II[(X -(B*T)*T**j) | [j:<-[0..<-1+sz]]]
        ]
    [[sz > 0] -> [polynomial_geo{sz;B,T,X} == (X-B) * II[(X -(B*T)*T**j) | [j:<-[0..<-1+sz]]]]]

    #]]]'''#'''
    _saved_args = (opsX, may_B, T, sz)
    check_int_ge(0, sz)
    neg_ = opsX.neg_
    add_ = opsX.add_
    mul_ = opsX.mul_
    one = opsX.one
    B = one if may_B is None else may_B
    min_len4recur = max(2, min_len4recur)
    # [min_len4recur >= 2]

    def _mk_pows_(x, sz, /, *, mul_=mul_):
        if not sz:return []
        ls = [one]
        for _ in range(1, sz):
            ls.append(mul_(ls[-1], x))
        return ls
    def _4sz_lt3(sz, B, /):
        match sz:
            case 2:
                # (X -B)*(X -B*T)
                # (X**2 -(B+B*T)*X +B*B*T)
                BT = mul_(B,T)
                b = neg_(add_(B,BT))
                c = mul_(B,BT)
                return [c, b, one]
            case 1:
                # (X -B)
                return [neg_(B), one]
            case 0:
                return [one]
        raise Exception(sz)
    if sz < 3:
        return _4sz_lt3(sz, B)
    if sz < min_len4recur:
        return mk_polynomial_coeffs5roots_on_geometric_progression__7native_(opsX, may_B, T, sz)
    # [sz >= 3]

    if optimized6zpow:
        #@20260617
        optimized6zpow = False
        lb_sz = floor_log2(sz)
        if 3 < sz == 1<<lb_sz:
            # [4 <= sz == 2**lb_sz]
            optimized6zpow = True
            # apply:[[sz > 0] -> [polynomial_geo{sz;B,T,X} == (X-B) * II[(X -(B*T)*T**j) | [j:<-[0..<-1+sz]]]]]
            f0 = [neg_(B), one]
            B = mul_(B, T)
            sz -= 1
            # [sz >= 3]
    # [sz >= 3]
    sz0 = sz
    j2Tj = _mk_pows_(T, 1+sz//2)
    stk = []
    # [min_len4recur >= 2]
    while not sz < min_len4recur:
        # [sz >= min_len4recur >= 2]
        h = sz//2
        # [h >= 1]
        odd = bool(sz&1)
        frame = (odd, sz, h, B)
        stk.append(frame)
        if odd:
            # update6odd:goto
            sz = sz-1
            B = mul_(B,T)
        else:
            # update4cs6even:goto
            sz = h
            Th = j2Tj[h]
            B;pass
        # [sz >= 1]
    # [sz >= 1]
    assert sz
    sz7halt = sz
    if sz < 3:
        csA = _4sz_lt3(sz, B)
    elif sz < min_len4recur:
        csA = mk_polynomial_coeffs5roots_on_geometric_progression__7native_(opsX, B, T, sz)
    else:
        raise 000
    #csA = _4sz_lt3(sz, B)
    csA
    while stk:
        assert -1+len(csA) == sz
        frame = (odd, sz, h, B) = stk.pop()
        if odd:
            # [sz%2 == 1]
            # [-1+len(csA) == sz-1 == 2*h]
            # update6odd:goto
            #
            # !! [polynomial_geo{1+2*h;B,T,X} == (X-B)*polynomial_geo{2*h;B*T,T,X}] # update6odd:here
            #
            assert -1+len(csA) == sz-1
            csA = mul7polynomial_(opsX, [neg_(B), one], csA)
                #=> _school_book_mul
            assert -1+len(csA) == sz
        else:
            # [sz%2 == 0]
            # [len(csA) == sz/2 == h]
            #
            # update4cs6even:goto
            # !! [cs1 == cs0 .*. (reverse (T**h) **. [0..=h])] # update4cs6even:goto
            #
            Th = j2Tj[h]
            j2Thj = _mk_pows_(Th, 1+h)
            assert -1+len(csA) == h
            assert -1+len(j2Thj) == h
            csB = [*map(mul_, csA, reversed(j2Thj))]
            csA = mul7polynomial_(opsX, csA, csB)
            assert -1+len(csA) == sz
    csA
    if optimized6zpow:
        sz += 1
        csA = mul7polynomial_(opsX, f0, csA)
    assert csA[-1] == one, (_saved_args, csA)
    return csA





__all__
from seed.math.polynomial.eval_polynomial.mk_polynomial_coeffs5roots_ import mul7polynomial_, mk_polynomial_coeffs5roots_, mk_polynomial_coeffs5roots_on_geometric_progression_
#def mk_polynomial_coeffs5roots_on_geometric_progression_(opsX, may_B, T, sz, /, *, min_len4recur=_default4min_len4recur):
from seed.math.polynomial.eval_polynomial.mk_polynomial_coeffs5roots_ import *
