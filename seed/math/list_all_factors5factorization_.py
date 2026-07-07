#__all__:goto
r'''[[[
e ../../python3_src/seed/math/list_all_factors5factorization_.py
see:
    view ../../python3_src/seed/math/all_factors_of_.py
        flatten recur
        fancy
        fast
    view ../../python3_src/seed/math/list_all_factors5factorization_.py
        using:II__ft_e_pairs_
        native
        slow


seed.math.list_all_factors5factorization_
py -m nn_ns.app.debug_cmd   seed.math.list_all_factors5factorization_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.list_all_factors5factorization_:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> list_all_factors5factorization_({})
(1,)
>>> list_all_factors5factorization_({3:0})
(1,)
>>> list_all_factors5factorization_({3:1})
(1, 3)
>>> list_all_factors5factorization_({3:2})
(1, 3, 9)
>>> list_all_factors5factorization_({3:3})
(1, 3, 9, 27)
>>> list_all_factors5factorization_({3:3, 5:0})
(1, 3, 9, 27)
>>> list_all_factors5factorization_({3:3, 5:1})
(1, 3, 5, 9, 15, 27, 45, 135)
>>> list_all_factors5factorization_({3:3, 5:2})
(1, 3, 5, 9, 15, 25, 27, 45, 75, 135, 225, 675)
>>> list_all_factors5factorization_({3:3, 5:2, 7:1})
(1, 3, 5, 7, 9, 15, 21, 25, 27, 35, 45, 63, 75, 105, 135, 175, 189, 225, 315, 525, 675, 945, 1575, 4725)
>>> list_all_factors5factorization_(1)
(1,)
>>> list_all_factors5factorization_(2)
(1, 2)
>>> list_all_factors5factorization_(4)
(1, 2, 4)
>>> list_all_factors5factorization_(6)
(1, 2, 3, 6)
>>> list_all_factors5factorization_(12)
(1, 2, 3, 4, 6, 12)
>>> list_all_factors5factorization_(30)
(1, 2, 3, 5, 6, 10, 15, 30)
>>> list_all_factors5factorization_(60)
(1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60)



py_adhoc_call   seed.math.list_all_factors5factorization_   @f
]]]'''#'''
__all__ = r'''
iter_all_factors5factorization_
    list_all_factors5factorization_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from itertools import product #islice
    from seed.math.II import II__ft_e_pairs_#, II, II_mod, II__p2e_, II__ft2e_, factorial_mod_
    from seed.math.factor_pint.factor_pint__naive_brute_force import factor_pint__naive_brute_force_
#.    from functools import cached_property
___end_mark_of_excluded_global_names__0___ = ...


def iter_all_factors5factorization_(u_or_p2e, /, *, with_factorization=False):
    'u_or_p2e/(u/uint{>=1}|p2e/{p/prime:e/uint}) -> unsorted-Iter (factor/uint{>0} if not with_factorization else (factor, p2e4factor))'
    match u_or_p2e:
        case int(u):
            p2e = factor_pint__naive_brute_force_(u)
        case p2e:
            pass
    p2e
    pe_pairs = sorted(p2e.items())
    ps = [p for p, e in pe_pairs]
    es = [e for p, e in pe_pairs]
    for _es in product(*(range(1+e) for e in es)):
        factor = II__ft_e_pairs_(zip(ps, _es))
        yield factor if not with_factorization else (factor, dict((p,e) for p,e in zip(ps, _es) if e))

def list_all_factors5factorization_(u_or_p2e, /):
    'u_or_p2e/(u/uint{>=1}|p2e/{p/prime:e/uint}) -> factors/sorted[uint{>0}]'
    return tuple(sorted(iter_all_factors5factorization_(u_or_p2e)))

__all__
from seed.math.list_all_factors5factorization_ import iter_all_factors5factorization_, list_all_factors5factorization_
from seed.math.list_all_factors5factorization_ import *
