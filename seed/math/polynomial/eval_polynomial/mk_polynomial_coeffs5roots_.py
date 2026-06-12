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




def mk_polynomial_coeffs5roots_on_geometric_progression_(opsX, may_B, T, invT, sz, /):
>>> _257_opsN = mk_ops4convolution7symbolic_FFT__5modulus_(257)
>>> inv_2 = pow(2, -1, 257)
>>> mk_polynomial_coeffs5roots_on_geometric_progression_(_257_opsN, 1, 2, inv_2, 5)
[4, -72, 45, 53, -31, 1]
>>> mk_polynomial_coeffs5roots_on_geometric_progression_(_257_opsN, 3, 2, inv_2, 5)
[-56, 79, -70, -37, -93, 1]
>>> mk_polynomial_coeffs5roots_on_geometric_progression__7native_(_257_opsN, 3, 2, 5)
[-56, 79, -70, -37, -93, 1]
>>> args = (_257_opsN.add_, _257_opsN.mul_, _257_opsN.zero)
>>> poly_evals__7native_(*args, [-56, 79, -70, -37, -93, 1], [3, 6, 12, 24, 48, 96])
[0, 0, 0, 0, 0, -56]
>>> poly_evals__7native_(*args, [4, -72, 45, 53, -31, 1], [1, 2, 4, 8, 16, 32])
[0, 0, 0, 0, 0, 4]







>>> mk_polynomial_coeffs5roots_on_geometric_progression_(_257_opsN, 1, 2, inv_2, 20)
[-64, 120, -70, 15, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, -120, 70, -15, 1]

# (opsX, may_B, T, invT, sz):=(..., 16777216, 2, 73786976294838206464, 512)
>>> M67 = -1+2**67
>>> _M67_opsN = mk_ops4convolution7symbolic_FFT__5modulus_(M67)
>>> 2*73786976294838206464 %M67
1

>>> mk_polynomial_coeffs5roots_on_geometric_progression_(_M67_opsN, 16777216, 2, 73786976294838206464, 512)  #doctest: +ELLIPSIS +SKIP
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
    from seed.math.floor_ceil_tools.fc_log import ceil_log2
    from seed.tiny_.check import check_type_is, check_int_ge, check_uint_lt
    from seed.math.power.power_ import power_
    #def power_(mul_, may_inv_, may_is_zero_, is_one_, one, imay_group_order, e, x0, /):
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
def mk_polynomial_coeffs5roots_(opsX, roots, /, *, min_len4recur=8):
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
def mk_polynomial_coeffs5roots_on_geometric_progression_(opsX, may_B, T, invT, sz, /):
    r'''[[[
    #########
    # [opsX == (opsG|opsN)]
    # [opsX :: (Ops4convolution7FFT|Ops4convolution7symbolic_FFT)]
    #########
    [roots := [T**j | [j:<-[0..<sz]]]]
    [[ver1:
    [polynomial_geo{sz;T,X} := II[(X -T**j) | [j:<-[0..<sz]]]]
    [polynomial_geo{1+2*h;T,X} == (X-T**(2*h))*polynomial_geo{2*h;T,X}]

    [polynomial_geo{2*h;T,X}
    == II[(X -T**j) | [j:<-[0..<2*h]]]
    == II[(X -T**j) | [j:<-[0..<h]]]
    *  II[(X -T**j) | [j:<-[h..<2*h]]]
    == polynomial_geo{h;T,X}
    *  II[(X -T**(h+j)) | [j:<-[0..<h]]]
    == polynomial_geo{h;T,X}
    *  II[T**h*(X*T**-h -T**j) | [j:<-[0..<h]]]
    == polynomial_geo{h;T,X}
    *  T**(h**2) * II[(X*T**-h -T**j) | [j:<-[0..<h]]]
    == polynomial_geo{h;T,X}
    *  T**(h**2) * polynomial_geo{h;T,X*T**-h}
    == T**(h**2) * polynomial_geo{h;T,X*T**-h} * polynomial_geo{h;T,X}
    ]
    [cs0 := polynomial_geo{h;T,X}.coeffs]
    [cs1 := polynomial_geo{h;T,X*T**-h}.coeffs]
    [sum[cs1[j]*X**j | [j:<-[0..=h]]]
    == polynomial_geo{h;T,X*T**-h}
    == sum[cs0[j]*(X*T**-h)**j | [j:<-[0..=h]]]
    == sum[cs0[j]*(T**-h)**j * X**j | [j:<-[0..=h]]]
    ]
    [cs1 == [cs0[j]*(T**-h)**j | [j:<-[0..=h]]]]

    ]]
    [[ver2:biased
    [roots := [B*T**j | [j:<-[0..<sz]]]]
    [polynomial_geoB{sz;B,T,X} := II[(X -B*T**j) | [j:<-[0..<sz]]]]

    [polynomial_geoB{1+d;B,T,X}
    == II[(X -B*T**j) | [j:<-[0..<1+d]]]
    == (X-B)*II[(X -B*T**j) | [j:<-[1..<1+d]]]
    == (X-B)*II[(X -(B*T)*T**j) | [j:<-[0..<d]]]
    == (X-B)*polynomial_geoB{d;B*T,T,X}
    ]
    [polynomial_geoB{1+d;B,T,X} == (X-B)*polynomial_geoB{d;B*T,T,X}]
    # [d:=2*h]
    [polynomial_geoB{1+2*h;B,T,X} == (X-B)*polynomial_geoB{2*h;B*T,T,X}]
    [polynomial_geoB{2*h;B,T,X}
    == II[(X -B*T**j) | [j:<-[0..<2*h]]]
    == II[(X -B*T**j) | [j:<-[0..<h]]]
    *  II[(X -B*T**j) | [j:<-[h..<2*h]]]
    == II[((X*T**h) -(B*T**h)*T**j)*T**-h | [j:<-[0..<h]]]
    *  II[(X -(B*T**h)*T**j) | [j:<-[0..<h]]]
    == invT**(h**2)*polynomial_geoB{h;(B*T**h),T,(X*T**h)}
    *  polynomial_geoB{h;(B*T**h),T,X}
    ]
    [polynomial_geoB{2*h;B,T,X} == invT**(h**2)*polynomial_geoB{h;(B*T**h),T,(X*T**h)} * polynomial_geoB{h;(B*T**h),T,X}]

    [csA := polynomial_geoB{h;(B*T**h),T,X}.coeffs]
    [csB := polynomial_geoB{h;(B*T**h),T,(X*T**h)}.coeffs]
    [j:<-[0..=h]]:
        [csB[j]*X**j == csA[j]*(X*T**h)**j]
        [csB[j] == csA[j]*(T**h)**j]
    [csB == [csA[j]*(T**h)**j | [j:<-[0..=h]]]]
    [csB == (csA .*. ((T**h) **. [0..=h]))]
    [polynomial_geoB{2*h;B,T,X}
    == invT**(h**2) * poly{csA} * poly{(csA .*. ((T**h) **. [0..=h]))}
    == Repr{(h**2), acyclic_convolution_(csA, (csA .*. ((T**h) **. [0..=h])))}
    ]


    ]]

    #]]]'''#'''
    _saved_args = (opsX, may_B, T, invT, sz)
    check_int_ge(0, sz)
    neg_ = opsX.neg_
    add_ = opsX.add_
    mul_ = opsX.mul_
    one = opsX.one
    neg_one = opsX.neg_one
    B = one if may_B is None else may_B

    def _mk_pows_(x, sz, /, *, mul_=mul_):
        if not sz:return []
        ls = [one]
        for _ in range(1, sz):
            ls.append(mul_(ls[-1], x))
        return ls
    def _pow7invT_(e, /):
        return power_(mul_, may_inv_:=None, may_is_zero_:=None, is_one_:=lambda x:False, one, imay_group_order:=-1, e, x0:=invT)
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
    # [sz >= 3]
    sz0 = sz
    j2Tj = _mk_pows_(T, 1+sz//2)
    stk = []
    while not sz < 3:
        # [sz >= 3]
        h = sz//2
        # [h >= 1]
        odd = bool(sz&1)
        frame = (odd, sz, h, B)
        stk.append(frame)
        if odd:
            sz = sz-1
            B = mul_(B,T)
        else:
            sz = h
            Th = j2Tj[h]
            B = mul_(B,Th)
        # [sz >= 1]
    # [sz >= 1]
    assert sz
    sz7halt = sz
    csA = _4sz_lt3(sz, B)
    e4T8LC = 0
    (e4T8LC, csA)
    # [csA[-1] == T**e4T8LC]
    while stk:
        assert -1+len(csA) == sz
        # Repr:(e4T8LC, csA)
        #   == invT**e4T8LC * poly{csA}
        # [csA[-1] == T**e4T8LC]
        frame = (odd, sz, h, B) = stk.pop()
        if odd:
            # [sz%2 == 1]
            # [-1+len(csA) == sz-1 == 2*h]
            #
            # !! [polynomial_geoB{1+2*h;B,T,X} == (X-B)*polynomial_geoB{2*h;B*T,T,X}]
            #
            assert -1+len(csA) == sz-1
            csA = mul7polynomial_(opsX, [neg_(B), one], csA)
                #=> _school_book_mul
            pass;e4T8LC
            assert -1+len(csA) == sz
        else:
            # [sz%2 == 0]
            # [len(csA) == sz/2 == h]
            #
            # !! [csA := polynomial_geoB{h;(B*T**h),T,X}.coeffs]
            # !! [polynomial_geoB{2*h;B,T,X} == Repr{(h**2), acyclic_convolution_(csA, (csA .*. ((T**h) **. [0..=h])))}]
            #
            Th = j2Tj[h]
            j2Thj = _mk_pows_(Th, 1+h)
            assert -1+len(csA) == h
            assert -1+len(j2Thj) == h
            csB = [*map(mul_, csA, j2Thj)]
            # [csB[-1] == csA[-1] * j2Thj[-1]]
            # [csB[-1] == csA[-1] * T**(h**2)]
            # !! [csA[-1] == T**e4T8LC]
            # [csB[-1] == T**(h**2+e4T8LC)]
            csA = mul7polynomial_(opsX, csA, csB)
            # [csA[-1] == T**(h+2*e4T8LC)]
            #bug:e4T8LC += h**2
            e4T8LC = h**2 +(e4T8LC<<1)
            assert -1+len(csA) == sz
    (e4T8LC, csA)
    # Repr:(e4T8LC, csA)
    #   == invT**e4T8LC * poly{csA}
    invLC = _pow7invT_(e4T8LC)
    cs = [mul_(invLC, c) for c in csA]
    assert cs[-1] == one, (_saved_args, invLC, cs, csA)
        # (opsX, may_B, T, invT, sz):=(..., 16777216, 2, 73786976294838206464, 512)
    return cs





__all__
from seed.math.polynomial.eval_polynomial.mk_polynomial_coeffs5roots_ import mul7polynomial_, mk_polynomial_coeffs5roots_, mk_polynomial_coeffs5roots_on_geometric_progression_
#def mk_polynomial_coeffs5roots_on_geometric_progression_(opsX, may_B, T, invT, sz, /):
from seed.math.polynomial.eval_polynomial.mk_polynomial_coeffs5roots_ import *
