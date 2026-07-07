#__all__:goto
r'''[[[
e ../../python3_src/seed/math/polynomial/eval_polynomial/mul7polynomial.py

seed.math.polynomial.eval_polynomial.mul7polynomial
py -m nn_ns.app.debug_cmd   seed.math.polynomial.eval_polynomial.mul7polynomial -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.polynomial.eval_polynomial.mul7polynomial:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'

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





py_adhoc_call   seed.math.polynomial.eval_polynomial.mul7polynomial   @f
]]]'''#'''
__all__ = r'''
mul7polynomial_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.floor_ceil_tools.fc_log import ceil_log2
    from seed.tiny_.check import check_uint_lt
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
            coeffs8rhs = [*coeffs8rhs, *[opsX.zero]*d]
        assert sz7zpow == len(coeffs8lhs) + len(coeffs8rhs)
        cs = opsX.acyclic_convolution__7commonAPI_(coeffs8lhs, coeffs8rhs)
        del cs[sz-1:]
    cs
    return cs
    #zero = opsX.zero
    eq_zero_ = opsX.eq_zero_
    while cs and eq_zero_(cs[-1]):
        #while cs and cs[-1] == zero:
        cs.pop()
    return cs

__all__
from seed.math.polynomial.eval_polynomial.mul7polynomial import mul7polynomial_
from seed.math.polynomial.eval_polynomial.mul7polynomial import *
