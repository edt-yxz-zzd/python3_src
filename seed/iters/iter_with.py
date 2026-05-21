r'''[[[
e ../../python3_src/seed/iters/iter_with.py

seed.iters.iter_with
py -m seed.iters.iter_with
py -m nn_ns.app.debug_cmd   seed.iters.iter_with -x
py -m nn_ns.app.doctest_cmd seed.iters.iter_with:__doc__ -ht #  -ff -v -df
#]]]'''#'''

__all__ = 'iter_with_'.split()

___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.helper.ifNone import ifNone, ifNonef
    from seed.tiny_.check import check_callable
    from seed.tiny_.funcs import echo


def iter_funcs5may_funcs_(may_funcs, /):
    for m in may_funcs:
        f = ifNone(m, echo)
        check_callable(f)
        yield f
___end_mark_of_excluded_global_names__0___ = ...



def iter_with_(may_funcs, iterable, /):
    'Iter (may (x->y)) -> Iter x -> Iter tuple<y>'
    funcs = iter_funcs5may_funcs_(may_funcs)
    funcs = tuple(funcs)
    for x in iterable:
        ts = tuple(f(x) for f in funcs)
        yield ts





from seed.iters.iter_with import iter_with_
from seed.iters.iter_with import *
