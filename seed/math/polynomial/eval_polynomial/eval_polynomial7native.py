#__all__:goto
r'''[[[
e ../../python3_src/seed/math/polynomial/eval_polynomial/eval_polynomial7native.py

seed.math.polynomial.eval_polynomial.eval_polynomial7native
py -m nn_ns.app.debug_cmd   seed.math.polynomial.eval_polynomial.eval_polynomial7native -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.polynomial.eval_polynomial.eval_polynomial7native:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.polynomial.eval_polynomial.eval_polynomial7native   @f

]]]'''#'''
__all__ = r'''
poly_eval_
    iter_poly_evals__7native_
    poly_evals__7native_
iter_poly_evals__on_geometric_progression__7native_
    iter_geometric_progression_
    poly_evals__on_geometric_progression__7native_



'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from itertools import islice
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

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



__all__
from seed.math.polynomial.eval_polynomial.eval_polynomial7native import poly_eval_, iter_poly_evals__7native_, poly_evals__7native_
#def poly_eval_(add_, mul_, zero, coeffs8poly, x, /):
from seed.math.polynomial.eval_polynomial.eval_polynomial7native import iter_poly_evals__on_geometric_progression__7native_, iter_geometric_progression_, poly_evals__on_geometric_progression__7native_
from seed.math.polynomial.eval_polynomial.eval_polynomial7native import iter_geometric_progression_
    #def iter_geometric_progression_(mul_, B, T, /):
from seed.math.polynomial.eval_polynomial.eval_polynomial7native import *
