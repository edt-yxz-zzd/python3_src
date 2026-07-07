#__all__:goto
r'''[[[
e ../../python3_src/seed/math/mk_pows_.py
view ../../python3_src/seed/iters/iterate.py

seed.math.mk_pows_
py -m nn_ns.app.debug_cmd   seed.math.mk_pows_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.mk_pows_:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/polynomial/eval_polynomial/eval_polynomial7native.py
    iter_geometric_progression_
view ../../python3_src/seed/algo/FFT/convolution__7symbolic_DFT.py
]]


'#'; __doc__ = r'#'
>>> mk_pows_(int.__mul__, 3, -2, 5)
(3, -6, 12, -24, 48)
>>> mk_pows_(int.__add__, 3, -2, 5, mk=list)
[3, 1, -1, -3, -5]


py_adhoc_call   seed.math.mk_pows_   @f
]]]'''#'''
__all__ = r'''
mk_pows_
    iter_geometric_progression_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from itertools import islice
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def iter_geometric_progression_(mul_, B, T, /):
    x = B
    while 1:
        yield x
        x = mul_(x, T)

def mk_pows_(mul_, B, g, sz, /, *, mk=tuple):
    return mk(islice(iter_geometric_progression_(mul_, B, g), 0, sz))

__all__
from seed.math.mk_pows_ import mk_pows_, iter_geometric_progression_
from seed.math.mk_pows_ import *
