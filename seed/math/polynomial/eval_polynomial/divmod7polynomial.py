#__all__:goto
r'''[[[
e ../../python3_src/seed/math/polynomial/eval_polynomial/divmod7polynomial.py

seed.math.polynomial.eval_polynomial.divmod7polynomial
py -m nn_ns.app.debug_cmd   seed.math.polynomial.eval_polynomial.divmod7polynomial -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.polynomial.eval_polynomial.divmod7polynomial:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> from seed.algo.FFT.convolution import mk_ops4convolution7symbolic_FFT__5modulus_
>>> _0_opsN = mk_ops4convolution7symbolic_FFT__5modulus_(modulus:=0)


>>> inv7polynomial7trunc_(_0_opsN, 1+8, [1,1,1,4])
[1, -1, 0, -3, 7, -4, 9, -33, 40]
>>> divmod7polynomial_(_0_opsN, [1,1,1,4], [1,1], validate=True)
([4, -3, 4], [-3])
>>> mul7polynomial_(_0_opsN, [4, -3, 4], [1,1])
[4, 1, 1, 4]
>>> add7polynomial_(_0_opsN, [4,1,1,4], [-3])
[1, 1, 1, 4]



why __bug__zmay_min_nonzero_index7polynomial__ge_ default 0???
>>> divmod7polynomial_(_0_opsN, [1,1,1,4], [1], validate=True)
([1, 1, 1, 4], [])
>>> divmod7polynomial_(_0_opsN, [1,1,1,4], [0,0,0,0,1], validate=True)
([], [1, 1, 1, 4])
>>> divmod7polynomial_(_0_opsN, [1,1,1,4], [0,0,0,1], validate=True)
([4], [1, 1, 1])
>>> divmod7polynomial_(_0_opsN, [0,1,1,1,4], [0,1], validate=True)
([1, 1, 1, 4], [])
>>> divmod7polynomial_(_0_opsN, [0,0,0,1], [0,1], validate=True)
([0, 0, 1], [])



>>> mod7polynomial_(_0_opsN, [1,1,1,4], [1], validate=True)
[]
>>> mod7polynomial_(_0_opsN, [1,1,1,4], [0,0,0,0,1], validate=True)
[1, 1, 1, 4]
>>> mod7polynomial_(_0_opsN, [1,1,1,4], [0,0,0,1], validate=True)
[1, 1, 1]
>>> mod7polynomial_(_0_opsN, [0,1,1,1,4], [0,1], validate=True)
[]
>>> mod7polynomial_(_0_opsN, [0,0,0,1], [0,1], validate=True)
[]



>>> ex_gcd7polynomial7native7through_monic_(_0_opsN, [], [], validate=True)
(((1,), ()), ((1,), ()), [])
>>> ex_gcd7polynomial7native7through_monic_(_0_opsN, [9,1], [], validate=True)
(((1,), ()), ((1,), ()), [9, 1])
>>> ex_gcd7polynomial7native7through_monic_(_0_opsN, [], [9,1], validate=True)
(((), (1,)), ((), (1,)), [9, 1])
>>> ex_gcd7polynomial7native7through_monic_(_0_opsN, [1], [9,1], validate=True)
(([1], [9, 1]), ((1,), ()), [1])
>>> ex_gcd7polynomial7native7through_monic_(_0_opsN, [1,9], [9,1], validate=True)
Traceback (most recent call last):
    ...
ValueError: ('not "7through_monic"', ([1, 9], [9, 1]), ([9, 1], [-80]), -80)
>>> ex_gcd7polynomial7native7through_monic_(_0_opsN, [1]*3, [1]*2, validate=True)
(([1, 1, 1], [1, 1]), ((1,), [0, -1]), [1])
>>> ex_gcd7polynomial7native7through_monic_(_0_opsN, [1]*3, [1]*5, validate=True)
(([1, 1, 1], [1, 1, 1, 1, 1]), ([1, 0, 0, 1], [0, -1]), [1])
>>> ex_gcd7polynomial7native7through_monic_(_0_opsN, [1]*3, [1]*6, validate=True)
(([1], [1, 0, 0, 1]), ((1,), ()), [1, 1, 1])
>>> ex_gcd7polynomial7native7through_monic_(_0_opsN, [1]*9, [1]*6, validate=True)
(([1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1]), ((1,), [0, 0, 0, -1]), [1, 1, 1])








>>> ex_gcd7polynomial7native7through_monic_(_0_opsN, [-1], [9,-1], validate=True)
(([-1], [9, -1]), ([-1], []), [1])
>>> ex_gcd7polynomial7native7through_monic_(_0_opsN, [0,-1], [-1,0,-1], validate=True)
(([0, -1], [-1, 0, -1]), ([0, 1], [-1]), [1])



>>> mul7polynomial_(_0_opsN, [1]*5, [1,2,3])
[1, 3, 6, 6, 6, 5, 3]
>>> mul7polynomial7all_ones_(_0_opsN, 5, [1,2,3])
[1, 3, 6, 6, 6, 5, 3]
>>> mul7polynomial7all_ones_(_0_opsN, 5, [1,2,3,4])
[1, 3, 6, 10, 10, 9, 7, 4]
>>> mul7polynomial7all_ones_(_0_opsN, 5, [1,2,3,4,5])
[1, 3, 6, 10, 15, 14, 12, 9, 5]
>>> mul7polynomial7all_ones_(_0_opsN, 5, [1,2,3,4,5,6])
[1, 3, 6, 10, 15, 20, 18, 15, 11, 6]
>>> mul7polynomial_(_0_opsN, [1]*5, [1,2,3,4,5,6])
[1, 3, 6, 10, 15, 20, 18, 15, 11, 6]
>>> mul7polynomial7all_ones_(_0_opsN, 5, [1,0,0,0,0,1])
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]



>>> mul7polynomial7unity_roots6order_(_0_opsN, 5, [0,1])
[0, -1, 0, 0, 0, 0, 1]
>>> mul7polynomial7unity_roots6order_(_0_opsN, 5, [0,0,0,0,0,1])
[0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1]
>>> mul7polynomial7unity_roots6order_(_0_opsN, 5, [1,0,0,0,0,1])
[-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
>>> mul7polynomial7unity_roots6order_(_0_opsN, 5, [1,2,3,4,5,6])
[-1, -2, -3, -4, -5, -5, 2, 3, 4, 5, 6]
>>> mul7polynomial7unity_roots6order_(_0_opsN, 5, [1,2,3,4,5])
[-1, -2, -3, -4, -5, 1, 2, 3, 4, 5]
>>> mul7polynomial7unity_roots6order_(_0_opsN, 5, [1,2,3,4])
[-1, -2, -3, -4, 0, 1, 2, 3, 4]
>>> mul7polynomial7unity_roots6order_(_0_opsN, 5, [1,2,3])
[-1, -2, -3, 0, 0, 1, 2, 3]
>>> mul7polynomial_(_0_opsN, [-1,0,0,0,0,1], [1,2,3])
[-1, -2, -3, 0, 0, 1, 2, 3]







_iter_count_nonzero_terms6II_cyclotomic_polynomial_mod4_eq_1or3_
>>> _v3at11 = perfect_inv_mod7polynomial7native7through_monic_(_0_opsN, [1]*3, [1]*11)
>>> _v7at11 = perfect_inv_mod7polynomial7native7through_monic_(_0_opsN, [1]*7, [1]*11)
>>> _v3x7at11 = rmod7polynomial_(_0_opsN, [1]*11, mul7polynomial_(_0_opsN, _v3at11, _v7at11))
>>> _3x7 = mul7polynomial_(_0_opsN, [1]*3, [1]*7)
>>> one_at11 = mul7polynomial_(_0_opsN, _v3x7at11, _3x7)
>>> cs8one = rmod7polynomial_(_0_opsN, [1]*11, one_at11)
>>> _v3at11
[1, 0, 0, 1, 0, 0, 1, 0, 0, 1]
>>> _v7at11
[0, -1, 0, 0, -1, 0, 0, 0, -1]
>>> _v3x7at11
[1, 1, 1, 1, 0, 2, 1, 0, 1, 2]
>>> _3x7
[1, 2, 3, 3, 3, 3, 3, 2, 1]
>>> one_at11
[1, 3, 6, 9, 11, 14, 17, 19, 19, 19, 19, 19, 16, 13, 10, 8, 5, 2]
>>> cs8one
[1]
>>> perfect_inv_mod7polynomial7native7through_monic_(_0_opsN, _3x7, [1]*11)  #why ??????????????????????
Traceback (most recent call last):
    ...
ValueError: ('not "7through_monic"', ([1, 2, 3, 3, 3, 3, 3, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), ([-1, 0, 0, 1, 1], [2, 3, 3, 2]), 2)
>>> perfect_inv_mod7polynomial7native7through_monic_(_0_opsN, _3x7, [1]*11, _debug=True)
Traceback (most recent call last):
    ...
ValueError: ('not "7through_monic"', ([1, 2, 3, 3, 3, 3, 3, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), ([-1, 1, 0, -1, 1, -1], [0, 1, 0, 1]), ([1, 0, -1, 1, -1, 0, 1], [1, 0, 0, -1, -1]), [[0, -1, 1], [1, 1], [0, 1], [-1, 1], [1, 1]], ([-1, 0, 0, 1, 1], [2, 3, 3, 2]), 2)






>>> from fractions import Fraction
>>> def mk_perfect_div_(D, /):
...     D = Fraction(D)
...     def perfect_div_(N, /):
...         return N/D
...     return perfect_div_
>>> _fr0_opsN = mk_ops4convolution7symbolic_FFT__5modulus_(modulus:=0, mk_perfect_div_=mk_perfect_div_)
>>> (_v3x7at11__7fr, _v11at3x7__7fr) = perfect_both_invs_mod7polynomial7native7through_monic_(_fr0_opsN, _3x7, [1]*11, neg_only=False) #证明中间过程确实不止整数
>>> _v11at3x7__7fr
[Fraction(0, 1), Fraction(-3, 1), Fraction(-3, 1), Fraction(-3, 1), Fraction(-2, 1), Fraction(-3, 1), Fraction(-3, 1), Fraction(-2, 1)]
>>> _v3x7at11__7fr
[Fraction(1, 1), Fraction(1, 1), Fraction(1, 1), Fraction(1, 1), Fraction(0, 1), Fraction(2, 1), Fraction(1, 1), Fraction(0, 1), Fraction(1, 1), Fraction(2, 1)]
>>> all(x.denominator == 1 for x in _v11at3x7__7fr)
True
>>> all(x.denominator == 1 for x in _v3x7at11__7fr)
True
>>> _v11at3x7__7N6fr = [x.numerator for x in _v11at3x7__7fr]
>>> _v3x7at11__7N6fr = [x.numerator for x in _v3x7at11__7fr]
>>> _v11at3x7__7N6fr
[0, -3, -3, -3, -2, -3, -3, -2]
>>> _v3x7at11__7N6fr
[1, 1, 1, 1, 0, 2, 1, 0, 1, 2]
>>> _v3x7at11__7fr == _v3x7at11
True















[[
py_adhoc_call   seed.math.polynomial.eval_polynomial.divmod7polynomial   @_test
]]

[[
py_adhoc_call   seed.math.polynomial.eval_polynomial.divmod7polynomial   ,_iter_count_nonzero_terms6II_cyclotomic_polynomial_mod4_eq_1or3_ =30
    (3, (1, 1), (3, 0))
    (5, (5, 1), (3, 2))
    (7, (5, 4), (9, 3))
    Traceback (most recent call last):
        ...
    ValueError: ('not "7through_monic"', ([1, 2, 3, 3, 3, 3, 3, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), ([-1, 0, 0, 1, 1], [2, 3, 3, 2]), 2)
        不该出错的...bug?
        #见上面:证明中间过程确实不止整数

]]

py_adhoc_call   seed.math.polynomial.eval_polynomial.divmod7polynomial   @f
]]]'''#'''
__all__ = r'''
    divmod7polynomial_
        perfect_div7polynomial_
        mod7polynomial_
            rmod7polynomial_
        inv7polynomial7trunc_
    mul7polynomial7trunc_
        mul7polynomial_


    add7polynomial_
    sub7polynomial_
        neg7polynomial_
    eq7polynomial_
        eq_zero7polynomial_
        eq_one7polynomial_
    trunc7polynomial_
    drop_zero_pad7polynomial7inplace_
    drop_zero_pad7polynomial_
        zero_pad7polynomial_

    to_monic_polynomial_
    is_monic_polynomial_
    is_reversal_monic_polynomial_
    check_monic_polynomial_
    check_reversal_monic_polynomial_


    imay_deg7polynomial_
    reversal7polynomial7trunc_
    min_nonzero_index7polynomial__ge_
    max1_nonzero_index7polynomial__lt_
    ex_gcd7polynomial7native7through_monic_
        perfect_both_invs_mod7polynomial7native7through_monic_
            perfect_inv_mod7polynomial7native7through_monic_

    mul7polynomial7cyclotomic6prime_
        mul7polynomial7unity_roots6order_
        mul7polynomial7all_ones_
        perfect_div7polynomial7Xmm_


    wrap_around7polynomial_
        rmod7polynomial7unity_roots6order_
            rmod7polynomial7all_ones_

    num_nonzero_coeffs_of_
        num_zero_coeffs_of_

'''.split()#'''
    #__bug__zmay_min_nonzero_index7polynomial__ge_
    #_iter_count_nonzero_terms6II_cyclotomic_polynomial_mod4_eq_1or3_
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.math.polynomial.eval_polynomial.mul7polynomial import mul7polynomial_
    #def mul7polynomial_(opsX, coeffs8lhs, coeffs8rhs, /, *, auto_vs_native_vs_fancy=0):
    from seed.debug.show_name_value_pairs_ import errshow_name_value_pairs_, show_name_value_pairs_, iter_name_value_pairs_, parse_xnms_
    from functools import reduce
    from itertools import repeat, cycle
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def trunc7polynomial_(opsX, sz, coeffs8poly, /):
    if len(coeffs8poly) > sz:
        jpp = max1_nonzero_index7polynomial__lt_(opsX, sz, coeffs8poly)
        coeffs8poly = coeffs8poly[:jpp]
    return coeffs8poly
def inv7polynomial7trunc_(opsX, sz, coeffs8poly, /):
    #原文:R[X;degree]
    '[cs[0] == 1][sz == 1+degree >= 1] # truncated reciprocal'
    check_int_ge(1, sz)
    one = opsX.one
    two = opsX.add_(one, one)
    if 0:
        eq_one_ = opsX.eq_one_
        if not (coeffs8poly and eq_one_(coeffs8poly[0])):raise ValueError(coeffs8poly[:1]) #is_reversal_monic_polynomial_
    check_reversal_monic_polynomial_(opsX, coeffs8poly)

    stk = []
    M = sz
    while not M == 1:
        # [M >= 2]
        stk.append(M)
        M = -(M//-2) # ceil(M/2)
        # [M >= 1]
    # [M == 1]
    cs = coeffs8poly
    cs7inv = [1]
    # [len(cs7inv) == M]
    for M in reversed(stk):
        # [old_M < M <= min(2*old_M,sz)]
        # [len(cs7inv) <= old_M]
        # non_degenerative_case=>[len(cs7inv) == old_M]
        cs7M = trunc7polynomial_(opsX, M, cs)
            #drop_zero_pad7polynomial_
        p_one7M = mul7polynomial7trunc_(opsX, M, cs7M, cs7inv)
        n_one7M = sub7polynomial_(opsX, [two], p_one7M)
        cs7inv = mul7polynomial7trunc_(opsX, M, n_one7M, cs7inv)
        # [len(cs7inv) <= M]
        # non_degenerative_case=>[len(cs7inv) == M]
    # [len(cs7inv) <= M == sz]
    # non_degenerative_case=>[len(cs7inv) == M == sz]
    assert len(cs7inv) <= sz
    return cs7inv

def mul7polynomial7trunc_(opsX, sz, coeffs8lhs, coeffs8rhs, /, **kwds):
    # half-cyclic convolutions
    return trunc7polynomial_(opsX, sz, mul7polynomial_(opsX, coeffs8lhs, coeffs8rhs, **kwds))
def add7polynomial_(opsX, coeffs8lhs, coeffs8rhs, /):
    if not coeffs8rhs:
        return coeffs8lhs
    if not coeffs8lhs:
        return coeffs8rhs
    ws = list(map(opsX.add_, coeffs8lhs, coeffs8rhs))
    if len(ws) < len(coeffs8lhs):
        ws += coeffs8lhs[len(ws):]
    elif len(ws) < len(coeffs8rhs):
        ws += coeffs8rhs[len(ws):]
    else:
        drop_zero_pad7polynomial7inplace_(opsX, ws)
    return ws
def zero_pad7polynomial_(opsX, sz, ws, /):
    sz4pad = sz-len(ws)
    if sz4pad > 0:
        ws = [*ws, *repeat(opsX.zero, sz4pad)]
        assert len(ws) == sz
    assert len(ws) >= sz
    return ws
def drop_zero_pad7polynomial_(opsX, ws, /):
    end = len(ws)
    jpp = max1_nonzero_index7polynomial__lt_(opsX, end, ws)
    if not jpp == end:
        ws = ws[:jpp]
    return ws
def drop_zero_pad7polynomial7inplace_(opsX, ws, /):
    jpp = max1_nonzero_index7polynomial__lt_(opsX, len(ws), ws)
    del ws[jpp:]
    return ws
    #eq_zero_ = opsX.eq_zero_
    #while ws and eq_zero_(ws[-1]): ws.pop()
def neg7polynomial_(opsX, cs, /):
    cs = drop_zero_pad7polynomial_(opsX, cs)
    ws = list(map(opsX.neg_, cs))
    return ws
def sub7polynomial_(opsX, coeffs8lhs, coeffs8rhs, /):
    cs6R = neg7polynomial_(opsX, coeffs8rhs)
    return add7polynomial_(opsX, coeffs8lhs, cs6R)
    ws = list(map(opsX.sub_, coeffs8lhs, coeffs8rhs))
    if len(ws) < len(coeffs8lhs):
        ws += coeffs8lhs[len(ws):]
    elif len(ws) < len(coeffs8rhs):
        ws.extend(map(opsX.neg_, coeffs8rhs[len(ws):]))
    return ws
def eq_zero7polynomial_(opsX, cs, /):
    return all(map(opsX.eq_zero_, reversed(cs)))
def eq_one7polynomial_(opsX, cs, /):
    return eq7polynomial_(opsX, [opsX.one], cs)
def eq7polynomial_(opsX, coeffs8lhs, coeffs8rhs, /):
    if not len(coeffs8lhs) == len(coeffs8rhs):
        sz = min(len(coeffs8lhs), len(coeffs8rhs))
        if not all(all(map(opsX.eq_zero_, (cs[j] for j in reversed(range(sz, len(cs)))))) for cs in [coeffs8lhs, coeffs8rhs]):
            return False
    if not all(map(opsX.eq7ring_, coeffs8lhs, coeffs8rhs)):
        return False
    return True



def imay_deg7polynomial_(opsX, cs, /):
    return -1+len(cs)
def is_monic_polynomial_(opsX, cs, /):
    return cs and opsX.eq_one_(cs[-1])
def is_reversal_monic_polynomial_(opsX, cs, /):
    return cs and opsX.eq_one_(cs[0])
def check_monic_polynomial_(opsX, cs, /):
    if not is_monic_polynomial_(opsX, cs):raise ValueError(cs[-1:])
def check_reversal_monic_polynomial_(opsX, cs, /):
    if not is_reversal_monic_polynomial_(opsX, cs):raise ValueError(cs[:1])

def reversal7polynomial7trunc_(opsX, may_sz, cs, /):
    #原文:rev[X;degree]
    #reversal
    sz = len(cs) if may_sz is None else may_sz
    check_int_ge(1, sz) # [sz==1+degree >= 1]
    if not cs:
        return cs
    j = min_nonzero_index7polynomial__ge_(opsX, 0, cs, end=sz)
    #SHOULD BE{zero_pad}:cs7rev = cs[sz-1:j-1:-1]
    sz4zero_pad = (sz -len(cs))
    cs7rev = cs[min(sz, len(cs))-1:(None if j==0 else j-1):-1]
    if cs7rev and sz4zero_pad > 0:
        cs7rev7H = cs7rev
        cs7rev = [opsX.zero]*sz4zero_pad
        cs7rev.extend(cs7rev7H)
    cs7rev
    assert not cs7rev or len(cs7rev) == sz-j, (sz, cs, cs7rev)
    #drop_zero_pad7polynomial7inplace_(cs7rev)
    return cs7rev

def __bug__zmay_min_nonzero_index7polynomial__ge_(opsX, begin, cs, /):
    #ind(X;d)
    # 应当不是bug， 许是因为 [cs==0]
    j = min_nonzero_index7polynomial__ge_(opsX, begin, cs)
    if j == len(cs):
        j = 0 # if empty then default 0
    return j
def min_nonzero_index7polynomial__ge_(opsX, begin, cs, /, *, end=None):
    #almost:ind(X;d)
    if end is None:
        end = len(cs)
    else:
        check_int_ge(0, end)
        end = min(end, len(cs))
    check_int_ge(0, begin)
    check_int_ge(0, end)
    eq_zero_ = opsX.eq_zero_
    for j in range(begin, end):
        if not eq_zero_(cs[j]):
            break
    else:
        j = end # if empty then default end
        #原文:j = 0 # if empty then default 0
    return j
def max1_nonzero_index7polynomial__lt_(opsX, end, cs, /, *, begin=None):
    if begin is None:
        begin = 0
    else:
        check_int_ge(0, begin)
        begin = min(begin, len(cs))
    check_int_ge(0, begin)
    check_int_ge(0, end)
    eq_zero_ = opsX.eq_zero_
    for j in reversed(range(begin, end)):
        if not eq_zero_(cs[j]):
            jpp = 1+j
            break
    else:
        jpp = begin # if empty then default begin
    return jpp

def perfect_div7polynomial_(opsX, cs8N, cs8D, /, *, validate=False):
    (cs8Q, cs8R) = divmod7polynomial_(opsX, cs8N, cs8D, validate=validate)
    if not eq_zero7polynomial_(opsX, cs8R):raise ValueError((cs8N, cs8D), (cs8Q, cs8R))
    return cs8Q
def divmod7polynomial_(opsX, cs8N, cs8D, /, *, validate=False):
    return _divmod7polynomial_(opsX, cs8N, cs8D, _with_quotient:=True, validate)
def rmod7polynomial_(opsX, cs8D, cs8N, /, **kwds):
    return mod7polynomial_(opsX, cs8N, cs8D, **kwds)
def mod7polynomial_(opsX, cs8N, cs8D, /, *, validate=False):
    return _divmod7polynomial_(opsX, cs8N, cs8D, _with_quotient:=False, validate)
def _divmod7polynomial_(opsX, cs8N, cs8D, _with_quotient, validate, /):
    #remaindering
    # -> remainder | (quotient, remainder)
    check_monic_polynomial_(opsX, cs8D)
    # [degD >= 0]
    degD = imay_deg7polynomial_(opsX, cs8D)
    if degD == 0:
        cs8R = [] # zero
        if _with_quotient:
            cs8N = drop_zero_pad7polynomial_(opsX, cs8N)
            cs8Q = cs8N
            return (cs8Q, cs8R)
        return cs8R
    # [degD >= 1]
    cs8N = drop_zero_pad7polynomial_(opsX, cs8N)
    degN = imay_deg7polynomial_(opsX, cs8N)
    d = degN -degD
    if d < 0:
        cs8R = cs8N
        if _with_quotient:
            cs8Q = [] # zero
            return (cs8Q, cs8R)
        return cs8R
    # [d >= 0]
    sz = 1+d
    # [sz >= 1]
    cs8N7rev = reversal7polynomial7trunc_(opsX, None, cs8N)
    cs8D7rev = reversal7polynomial7trunc_(opsX, None, cs8D)
    cs8D7rev7inv = inv7polynomial7trunc_(opsX, sz, cs8D7rev)
    # [len(cs8D7rev7inv) == sz >= 1]
    cs8Q7rev = mul7polynomial7trunc_(opsX, sz, cs8D7rev7inv, cs8N7rev)
    cs8N7rev7approx = mul7polynomial_(opsX, cs8D7rev, cs8Q7rev)
    cs8R7rev7zpad = sub7polynomial_(opsX, cs8N7rev, cs8N7rev7approx)
    #bug:j = __bug__zmay_min_nonzero_index7polynomial__ge_(opsX, sz, cs8R7rev7zpad)
        # ???why default 0???
    j = min_nonzero_index7polynomial__ge_(opsX, sz, cs8R7rev7zpad)
    cs8R7rev = cs8R7rev7zpad[j:]
    cs8R = reversal7polynomial7trunc_(opsX, 1+degN-j, cs8R7rev)
    if _with_quotient or validate:
        #bug:cs8Q = reversal7polynomial7trunc_(opsX, None, cs8Q7rev)
        cs8Q = reversal7polynomial7trunc_(opsX, sz, cs8Q7rev)
    if validate:
        if not eq7polynomial_(opsX, cs8N, add7polynomial_(opsX, cs8R, mul7polynomial_(opsX, cs8Q, cs8D))):
            dat = ((cs8N, cs8D), (degN, degD, d, sz), (cs8N7rev, cs8D7rev), (cs8D7rev7inv, cs8Q7rev, cs8N7rev7approx), (cs8R7rev7zpad, j, cs8R7rev), (cs8Q, cs8R))
            xnms = parse_xnms_('((cs8N, cs8D), (degN, degD, d, sz), (cs8N7rev, cs8D7rev), (cs8D7rev7inv, cs8Q7rev, cs8N7rev7approx), (cs8R7rev7zpad, j, cs8R7rev), (cs8Q, cs8R))')
            errshow_name_value_pairs_(xnms, dat)
            raise Exception((cs8N, cs8D), (cs8Q, cs8R))
    if _with_quotient:
        return (cs8Q, cs8R)
    return cs8R

def _test():
    from seed.algo.FFT.convolution import mk_ops4convolution7symbolic_FFT__5modulus_
    _0_opsN = mk_ops4convolution7symbolic_FFT__5modulus_(modulus:=0)
    divmod7polynomial_(_0_opsN, [0,0,0,1], [0,1], validate=True)




def perfect_inv_mod7polynomial7native7through_monic_(opsX, cs8N, cs8D, /, **kwds):
    (cs8N7inv6D, cs8D7inv6N) = perfect_both_invs_mod7polynomial7native7through_monic_(opsX, cs8N, cs8D, **kwds)
    return cs8N7inv6D
def perfect_both_invs_mod7polynomial7native7through_monic_(opsX, cs8N, cs8D, /, **kwds):
    ((cs8q4lhs, cs8q4rhs), (cs8lhs2gcd, cs8rhs2gcd), cs8gcd) = ex_gcd7polynomial7native7through_monic_(opsX, cs8N, cs8D, **kwds)
    if not eq_one7polynomial_(opsX, cs8gcd): raise ValueError('not coprime or not "7through_monic" inside gcd')
    cs8N7inv6D = cs8lhs2gcd
    cs8D7inv6N = cs8rhs2gcd
    return (cs8N7inv6D, cs8D7inv6N)

def ex_gcd7polynomial7native7through_monic_(opsX, coeffs8lhs, coeffs8rhs, /, *, neg_only=True, validate=False, cs2exc_=None, _debug=False):
    r'''[[[
    -> ((cs8q4lhs, cs8q4rhs), (cs8lhs2gcd, cs8rhs2gcd), cs8gcd)

    [polynomial{cs8gcd} == polynomial{cs8lhs2gcd} * polynomial{coeffs8lhs} + polynomial{cs8rhs2gcd} * polynomial{coeffs8rhs}]
    <<==:
    [polynomial{coeffs8lhs} == polynomial{cs8q4lhs} * polynomial{cs8gcd}]
    [polynomial{coeffs8rhs} == polynomial{cs8q4rhs} * polynomial{cs8gcd}]
    [1 == polynomial{cs8lhs2gcd} * polynomial{cs8q4lhs} + polynomial{cs8rhs2gcd} * polynomial{cs8q4rhs}]
    #]]]'''#'''
    cs8N = original_cs8N = drop_zero_pad7polynomial_(opsX, coeffs8lhs)
    cs8D = original_cs8D = drop_zero_pad7polynomial_(opsX, coeffs8rhs)
    cs8one = (opsX.one,)
    cs8zero = ()
    if validate:
        ((cs8q4lhs, cs8q4rhs), (cs8lhs2gcd, cs8rhs2gcd), cs8gcd) = ex_gcd7polynomial7native7through_monic_(opsX, cs8N, cs8D, validate=False, neg_only=neg_only, cs2exc_=cs2exc_, _debug=_debug)
        #bug:assert not eq_zero7polynomial_(opsX, cs8lhs2gcd)
        #bug:assert not eq_zero7polynomial_(opsX, cs8rhs2gcd)
        assert eq7polynomial_(opsX, original_cs8N, mul7polynomial_(opsX, cs8gcd, cs8q4lhs))
        assert eq7polynomial_(opsX, original_cs8D, mul7polynomial_(opsX, cs8gcd, cs8q4rhs))
        assert eq7polynomial_(opsX, cs8one, add7polynomial_(opsX, mul7polynomial_(opsX, cs8lhs2gcd, cs8q4lhs), mul7polynomial_(opsX, cs8rhs2gcd, cs8q4rhs)))
        assert eq7polynomial_(opsX, cs8gcd, add7polynomial_(opsX, mul7polynomial_(opsX, cs8lhs2gcd, cs8N), mul7polynomial_(opsX, cs8rhs2gcd, cs8D)))
        #.return (cs8lhs2gcd, cs8rhs2gcd, cs8gcd)
        return ((cs8q4lhs, cs8q4rhs), (cs8lhs2gcd, cs8rhs2gcd), cs8gcd)
    ######################
    ######################
    ######################
    ######################
    if not (cs8N and cs8D):
        # [len(cs8N) == 0]or[len(cs8D) == 0]
        b_swap = bool(cs8D)
        if b_swap:
            # [len(cs8D) > 0]
            # [len(cs8N) == 0]
            (cs8N, cs8D) = (cs8D, cs8N)
            # [len(cs8D) == 0]
        else:
            # [len(cs8D) == 0]
            pass
        # [len(cs8D) == 0]
        if 0:
            if cs8N:check_monic_polynomial_(opsX, cs8N)

        #.return (cs8one, cs8one, cs8N)
        cs8gcd = cs8N
        (cs8lhs2gcd, cs8rhs2gcd) = (cs8one, cs8zero)
        (cs8q4lhs, cs8q4rhs) = (cs8one, cs8zero)
        if b_swap:
            (cs8lhs2gcd, cs8rhs2gcd) = (cs8rhs2gcd, cs8lhs2gcd)
            (cs8q4lhs, cs8q4rhs) = (cs8q4rhs, cs8q4lhs)
        return ((cs8q4lhs, cs8q4rhs), (cs8lhs2gcd, cs8rhs2gcd), cs8gcd)
    # [len(cs8N) > 0][len(cs8D) > 0]

    degN = -1+len(cs8N)
    degD = -1+len(cs8D)
    # [degN >= 0]
    # [degD >= 0]
    if (degN == degD and not is_monic_polynomial_(opsX, cs8D)) or (degN < degD):
        # [degN <= degD]
        (cs8N, cs8D) = (cs8D, cs8N)
        (degN, degD) = (degD, degN)
        # [degN >= degD]
        (N2N, D2N) = (cs8zero, cs8one)
        (N2D, D2D) = (cs8one, cs8zero)
    else:
        # [degN >= degD]
        (N2N, D2N) = (cs8one, cs8zero)
        (N2D, D2D) = (cs8zero, cs8one)
        pass
    # [degN >= degD]
    # [degN >= degD >= 0]
    if _debug:
        def _check_(N2X, D2X, cs8X, /):
            X6N = mul7polynomial_(opsX, original_cs8N, N2X)
            X6D = mul7polynomial_(opsX, original_cs8D, D2X)
            _cs8X = add7polynomial_(opsX, X6N, X6D)
            if not eq7polynomial_(opsX, _cs8X, cs8X):raise AssertionError(N2X, D2X, cs8X, _cs8X)
    if cs2exc_ is None:
        def cs2exc_(cs8D, /):
            if _debug:
                _check_(N2N, D2N, cs8N)
                _check_(N2D, D2D, cs8D)
                raise ValueError('not "7through_monic"', (original_cs8N, original_cs8D), (N2N, D2N), (N2D, D2D), qs, (cs8N, cs8D), cs8D[-1])# <<== 『7through_monic』
            raise ValueError('not "7through_monic"', (original_cs8N, original_cs8D), (cs8N, cs8D), cs8D[-1])# <<== 『7through_monic』
    if _debug:
        qs = []
    while 1:
        # [degN >= degD >= 0]
        #########
        (cs8D, may_div_LC) = to_monic_polynomial_(opsX, cs8D, neg_only=neg_only, with_may_div_LC=True, cs2exc_=cs2exc_)
        # [cs8D :: monic]
        if not None is may_div_LC:
            div_LC_ = may_div_LC
            N2D = list(map(div_LC_, N2D))
            D2D = list(map(div_LC_, D2D))
            (N2D, D2D)
        #check_monic_polynomial_(opsX, cs8D)
        # [cs8D :: monic]
        # [degN >= degD >= 0]
        (cs8Q, cs8R) = divmod7polynomial_(opsX, cs8N, cs8D)
        # [imay_deg(cs8R) < degD]
        # [cs8R == cs8N -cs8D*cs8Q]
        if _debug:
            qs.append(cs8Q)
        #########
        if not cs8R:
            cs8gcd = cs8D
            (cs8lhs2gcd, cs8rhs2gcd) = (N2D, D2D)
            cs8q4lhs = perfect_div7polynomial_(opsX, original_cs8N, cs8gcd)
            cs8q4rhs = perfect_div7polynomial_(opsX, original_cs8D, cs8gcd)
            (cs8q4lhs, cs8q4rhs)
            #.return (cs8lhs2gcd, cs8rhs2gcd, cs8gcd)
            #.return (N2D, D2D, cs8D)
            return ((cs8q4lhs, cs8q4rhs), (cs8lhs2gcd, cs8rhs2gcd), cs8gcd)
        # [len(cs8R) > 0]
        degR = -1+len(cs8R)
        # [0 <= degR < degD]
        #########
        # !! [cs8R == cs8N -cs8D*cs8Q]
        N2R = sub7polynomial_(opsX, N2N, mul7polynomial_(opsX, N2D, cs8Q))
        D2R = sub7polynomial_(opsX, D2N, mul7polynomial_(opsX, D2D, cs8Q))
        (N2R, D2R)
        #########
        # [0 <= degR < degD]
        (cs8N, cs8D) = (cs8D, cs8R)
        (degN, degD) = (degD, degR)
        (N2N, D2N) = (N2D, D2D)
        (N2D, D2D) = (N2R, D2R)
        # [0 <= degD < degN]
        #########

def to_monic_polynomial_(opsX, cs, /, *, neg_only=False, with_may_div_LC=False, cs2exc_=None):
    cs = drop_zero_pad7polynomial_(opsX, cs)
    if not is_monic_polynomial_(opsX, cs):
        if cs2exc_ is None:
            cs2exc_ = ValueError
        if not cs: raise cs2exc_(cs)
        LC = cs[-1]
        if opsX.eq_neg_one_(LC):
            div_LC_ = opsX.neg_
        elif not neg_only:
            div_LC_ = opsX.mk_perfect_div_(LC)
        else:
            raise cs2exc_(cs)
        div_LC_
        cs = list(map(div_LC_, cs))
        may_div_LC = div_LC_
    else:
        may_div_LC = None
    cs, may_div_LC
    check_monic_polynomial_(opsX, cs)
    return cs if not with_may_div_LC else (cs, may_div_LC)






def wrap_around7polynomial_(opsX, sz, cs, /):
    'sz -> cs -> (polynomial{cs} %(X**sz-1)).coeffs'
    if len(cs) <= sz:
        return cs
    #csL = cs[:sz]
    #csH = cs[sz:]
    ws = cs[:sz]
    add_ = opsX.add_
    for i, j in zip(cycle(range(sz)), range(sz, len(cs))):
        ws[i] = add_(ws[i], cs[j])
    return ws

def rmod7polynomial7unity_roots6order_(opsX, order8rhs, cs8lhs, /):
    'order -> cs -> (polynomial{cs} %(X**order-1)).coeffs'
    check_int_ge(1, order8rhs)
    return wrap_around7polynomial_(opsX, order8rhs, cs8lhs)

def rmod7polynomial7all_ones_(opsX, sz8rhs, cs8lhs, /):
    'sz -> cs -> (polynomial{cs} %((X**sz-1)///(X-1))).coeffs'
    check_int_ge(1, sz8rhs)
    ws = rmod7polynomial7unity_roots6order_(opsX, sz8rhs, cs8lhs)
    # [len(ws) <= sz8rhs]
    if len(ws) < sz8rhs:
        return ws
    assert len(ws) == sz8rhs
    # [len(ws) == sz8rhs]
    ws = list(ws)
    LC = ws.pop()
    neg_LC = opsX.neg_(LC)
    # [len(ws) == -1+sz8rhs]
    return add7polynomial_(opsX, ws, [neg_LC]*(-1+sz8rhs))

def mul7polynomial7cyclotomic6prime_(opsX, p8lhs, cs8rhs, /):
    'p -> cs -> (((X**p-1)///(X-1))*polynomial{cs}).coeffs # [p::prime]'
    return mul7polynomial7all_ones_(opsX, p8lhs, cs8rhs)
def mul7polynomial7all_ones_(opsX, sz8lhs, cs8rhs, /):
    'sz -> cs -> (((X**sz-1)///(X-1))*polynomial{cs}).coeffs'
    if 0:
        r'''[[[
        cs8lhs = [1]*sz8lhs
            # == ((X**sz8lhs-1)///(X-1))
        cs8rhs_mul_XpowP = [*repeat(zero, sz8lhs), *cs8rhs]
            # == rhs*(X**sz8lhs)
        cs8rhs_mul_lhs_mul_Xmm = sub7polynomial_(opsX, cs8rhs_mul_XpowP, cs8rhs)
            # == rhs*(X**sz8lhs-1)
            # == rhs*lhs*(X-1)
        cs8Xmm = [opsX.neg_one, opsX.one]
            # == (X-1)
        cs8rhs_mul_lhs = perfect_div7polynomial_(cs8rhs_mul_lhs_mul_Xmm, Xmm)
            # == rhs*lhs
        #]]]'''#'''

    cs8rhs_mul_lhs_mul_Xmm = mul7polynomial7unity_roots6order_(opsX, sz8lhs, cs8rhs)
        # == rhs*(X**sz8lhs-1)
        # == rhs*lhs*(X-1)
    cs8rhs_mul_lhs = perfect_div7polynomial7Xmm_(opsX, cs8rhs_mul_lhs_mul_Xmm)
        # == rhs*lhs*(X-1)///(X-1)
        # == rhs*lhs
    return cs8rhs_mul_lhs
def perfect_div7polynomial7Xmm_(opsX, cs8lhs, /):
    'cs -> (polynomial{cs}///(X-1)).coeffs'
    zero = opsX.zero
    add_ = opsX.add_
    #neg_ = opsX.neg_
    #if not opsX.eq_zero_(reduce(add_, cs8lhs, zero)):raise ValueError('not perfect')
        # == poly_eval_(cs8lhs, X:=1)
    ls = []
    r = zero
    for c in reversed(cs8lhs):
        q = add_(c, r)
        r = q
        ls.append(q)
    if not opsX.eq_zero_(r):raise ValueError('not perfect')
        # == poly_eval_(cs8lhs, X:=1)
    #bug:missing:ls.pop()
    ls.pop()
    ls.reverse()
    cs8lhs_div_Xmm = ls
        # == lhs///(X-1)
    return cs8lhs_div_Xmm
def mul7polynomial7unity_roots6order_(opsX, order8lhs, cs8rhs, /):
    'order -> cs -> ((X**order-1)*polynomial{cs}).coeffs'
    check_int_ge(1, order8lhs)
    cs8rhs7neg = neg7polynomial_(opsX, cs8rhs)
    L = min(order8lhs,len(cs8rhs7neg))
    #cs8rhs7neg_OL = trunc7polynomial_(opsX, L, cs8rhs7neg)
    cs8rhs7neg_OL = cs8rhs7neg[:L]
    cs8rhs7neg_pE = cs8rhs7neg[L:]
    cs8rhs7neg_Op = zero_pad7polynomial_(opsX, order8lhs, cs8rhs7neg_OL)
    cs8rhs_mul_lhs = [*cs8rhs7neg_Op, *add7polynomial_(opsX, cs8rhs7neg_pE, cs8rhs)]
        # == rhs*(X**order8lhs-1)
        # == rhs*lhs
    return cs8rhs_mul_lhs


def _iter_count_nonzero_terms6II_cyclotomic_polynomial_mod4_eq_1or3_(max1_p, /):
    #view others/数学/polynomial/polynomial_evaluation.txt
    #view ../../python3_src/seed/algo/FFT/convolution__7CRT.py
    #view ../../python3_src/seed/math/polynomial/eval_polynomial/cyclotomic_polynomial.py
    check_int_ge(6, max1_p)
    if not max1_p.bit_length() <= 11: raise ValueError('too big', max1_p)
    from seed.algo.FFT.convolution import mk_ops4convolution7symbolic_FFT__5modulus_
    _0_opsN = mk_ops4convolution7symbolic_FFT__5modulus_(modulus:=0)
    opsX = _0_opsN
    from seed.math.prime_sieve.sieve_ge_le import iter_sieve4primes_ge_lt_
    it = iter_sieve4primes_ge_lt_(3, max1_p)
    cs8one = (opsX.one,)
    cs8zero = ()
    cs8IIps41 = cs8one
    cs8IIps43 = cs8one
    b2cs8IIpsX = [cs8IIps41, cs8IIps43]
    b2cs8IIpsX7inv = [cs8one, cs8one]
    for p in it:
        #########
        b = p&3 == 3
        #########
        cs8IIpsX = b2cs8IIpsX[b]
        cs8IIpsY = b2cs8IIpsX[1-b]
        cs8p1s = [1]*p
        (cs8p1s7inv6IIpsY, cs8IIpsY7inv6p) = perfect_both_invs_mod7polynomial7native7through_monic_(opsX, cs8p1s, cs8IIpsY)
            # [poly{cs8p1s7inv6IIpsY}*poly{cs8p1s} =[%poly{cs8IIpsY}]= 1]
            # [poly{cs8IIpsY7inv6p}*poly{cs8IIpsY} =[%poly{cs8p1s}]= 1]
        cs8IIpsX7inv6IIpsY = b2cs8IIpsX7inv[b]
            # [poly{cs8IIpsX7inv6IIpsY}*poly{cs8IIpsX} =[%poly{cs8IIpsY}]= 1]
        cs8IIpsY7inv6IIpsX = b2cs8IIpsX7inv[1-b]
            # [poly{cs8IIpsY7inv6IIpsX}*poly{cs8IIpsY} =[%poly{cs8IIpsX}]= 1]



        #########
        b2cs8IIpsX[b] = new_cs8IIpsX = mul7polynomial7cyclotomic6prime_(opsX, p, b2cs8IIpsX[b])
        #########
        cs8IIpsX7inv6p = perfect_inv_mod7polynomial7native7through_monic_(opsX, cs8IIpsX, cs8p1s)
        b2cs8IIpsX7inv[1-b] = add7polynomial_(opsX
            , cs8IIpsY7inv6IIpsX
            , mul7polynomial_(opsX, cs8IIpsX
                #, rmod7polynomial_(opsX, cs8p1s ...)
                , rmod7polynomial7all_ones_(opsX, p
                    , mul7polynomial_(opsX, cs8IIpsX7inv6p
                        , sub7polynomial_(opsX, cs8IIpsY7inv6p
                            #, rmod7polynomial_(opsX, cs8p1s ...)
                            , rmod7polynomial7all_ones_(opsX, p
                                , cs8IIpsY7inv6IIpsX))))))
        #.cs8p1s7inv6IIpsX = perfect_inv_mod7polynomial7native7through_monic_(opsX, cs8p1s, cs8IIpsX)
        #.b2cs8IIpsX7inv[1-b] = cs8IIpsY7inv6p + mul7polynomial_(opsX, cs8p1s, mul7polynomial_(opsX, cs8p1s7inv6IIpsX, sub7polynomial_(opsX, cs8IIpsY7inv6IIpsX, cs8IIpsY7inv6p)))

        #########
        b2cs8IIpsX7inv[b] = mod7polynomial_(opsX, mul7polynomial_(opsX, cs8p1s7inv6IIpsY, cs8IIpsX7inv6IIpsY), cs8IIpsY)
        #########
        rs = [p]
        for _b in range(2):
            cn0 = num_nonzero_coeffs_of_(opsX, b2cs8IIpsX[_b])
            cn1 = num_nonzero_coeffs_of_(opsX, b2cs8IIpsX7inv[_b])
            rs.append((cn0, cn1))
        yield tuple(rs)

def num_zero_coeffs_of_(opsX, cs, /):
    return sum(map(opsX.eq_zero_, cs))
def num_nonzero_coeffs_of_(opsX, cs, /):
    return len(cs) -num_zero_coeffs_of_(opsX, cs)


__all__
from seed.math.polynomial.eval_polynomial.divmod7polynomial import divmod7polynomial_, mod7polynomial_, inv7polynomial7trunc_, perfect_div7polynomial_
from seed.math.polynomial.eval_polynomial.divmod7polynomial import mul7polynomial7trunc_, mul7polynomial_


from seed.math.polynomial.eval_polynomial.divmod7polynomial import add7polynomial_, sub7polynomial_, eq7polynomial_, trunc7polynomial_, drop_zero_pad7polynomial7inplace_, drop_zero_pad7polynomial_
from seed.math.polynomial.eval_polynomial.divmod7polynomial import eq_zero7polynomial_, eq_one7polynomial_, neg7polynomial_, zero_pad7polynomial_

from seed.math.polynomial.eval_polynomial.divmod7polynomial import to_monic_polynomial_, is_monic_polynomial_, is_reversal_monic_polynomial_, check_monic_polynomial_, check_reversal_monic_polynomial_


from seed.math.polynomial.eval_polynomial.divmod7polynomial import imay_deg7polynomial_, reversal7polynomial7trunc_, min_nonzero_index7polynomial__ge_, max1_nonzero_index7polynomial__lt_

from seed.math.polynomial.eval_polynomial.divmod7polynomial import ex_gcd7polynomial7native7through_monic_

from seed.math.polynomial.eval_polynomial.divmod7polynomial import *
