#__all__:goto
r'''[[[
e ../../python3_src/seed/func_tools/func_pow_.py
view ../../python3_src/seed/iters/iterate.py
view ../../python3_src/seed/iters/fold.py

seed.func_tools.func_pow_
py -m nn_ns.app.debug_cmd   seed.func_tools.func_pow_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.func_tools.func_pow_:__doc__ -ht # -ff -df

[[
]]

>>> func_pow_(5, 'a'.__add__, 'b')
'aaaaab'
>>> func_powT_(5, 'a'.__add__)('b')
'aaaaab'
>>> func_powT_(5, str.__add__, (), ['a'])('b')
'baaaaa'

py_adhoc_call   seed.func_tools.func_pow_   @f
]]]'''#'''
__all__ = r'''
func_pow_
    func_powT_
partial_ex
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
from functools import partial, wraps #reduce
from seed.tiny_.check import check_type_is, check_int_ge
from seed.tiny_.funcs import echo
#.
___end_mark_of_excluded_global_names__0___ = ...


def func_pow_(e, f, x, /):
    'e -> f/(x->x) -> x -> x{==(f**e)(x)}'
    check_int_ge(0, e)
    return _func_pow_(e, f, x)
def _func_pow_(e, f, x, /):
    for _ in range(e):
        x = f(x)
    return x
def func_powT_(e, f, args4f6L=(), args4f6R=(), /, **kwds4f):
    'e -> f/(x->x) -> (x -> x{==(f**e)(x)})'
    check_int_ge(0, e)
    if e == 0:
        return echo
    f = partial_ex(f, args4f6L, args4f6R, **kwds4f)
    if e == 1:
        return f
    return partial(_func_pow_, e, f)
def partial_ex(f, args4f6L=(), args4f6R=(), /, **kwds4f):
    if args4f6L or kwds4f:
        f = partial(f, *args4f6L, **kwds4f)
    if args4f6R:
        f = _flip(f, *args4f6R)
    return f

def _flip(f, /, *args4f6R):
    @wraps(f)
    def g(x, /):
        return f(x, *args4f6R)
    return g

__all__
from seed.func_tools.func_pow_ import func_pow_, func_powT_, partial_ex
from seed.func_tools.func_pow_ import *
