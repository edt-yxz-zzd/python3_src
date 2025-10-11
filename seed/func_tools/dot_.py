#__all__:goto
r'''[[[
e ../../python3_src/seed/func_tools/dot_.py

seed.func_tools.dot_
py -m nn_ns.app.debug_cmd   seed.func_tools.dot_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.func_tools.dot_:__doc__ -ht # -ff -df
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.func_tools.dot_:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
源起:
    协同:lazy_import4func_
==>>:
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_
dot_ = lazy_import4func_('seed.func_tools.dot_', 'dot_', __name__)
]]


'#'; __doc__ = r'#'
>>> def f(a, b, c, d):
...     return ('f', a, b, c, d)
>>> def g(w, x, y, z):
...     return ('g', w, x, y, z)
>>> def h(a, /):
...     return ('h', a)
>>> fhg = dot_([f, [666], dict(d=999), [888]], h, [g, [000], {}, [222]])
>>> fhg #doctest: +ELLIPSIS
DotCall([[<function f at 0x...>, (666,), {'d': 999}, (888,)], <function h at 0x...>, [<function g at 0x...>, (0,), {}, (222,)]])
>>> fhg(111, z=333)
('f', 666, ('h', ('g', 0, 111, 222, 333)), 888, 999)


py_adhoc_call   seed.func_tools.dot_   @f

]]]'''#'''
__all__ = r'''
dot_
    DotCall
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from seed.tiny_.check import check_type_is, check_int_ge
#.
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_
repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
lazy_import4funcs_('seed.tiny', 'mk_tuple,echo', __name__)
if 0:from seed.tiny import mk_tuple,echo#print_err,ifNone as ifNone_ #xxx:null_tuple #xxx:echo,fst,snd
___end_mark_of_excluded_global_names__0___ = ...


def _frozen_fxx(f, pre_args=(), kwargs={}, post_args=(), /):
    assert callable(f)
    pre_args = mk_tuple(pre_args)
    post_args = mk_tuple(post_args)
    kwargs = dict(kwargs)
    fxx = (f, pre_args, kwargs, post_args)
    return fxx

def _simplify_fxx(fxx, /):
    fxx = [*fxx]
    for _ in range(len(fxx)-1):
        if fxx[-1]:
            break
        fxx.pop()
    fxx
    f_or_fxx = fxx[0] if len(fxx) == 1 else fxx
    return f_or_fxx

def _std_fxx(f_or_fxx, /):
    '(callable|fxx) ->  fxx # [fxx == ((callable,pre_args)|(callable,pre_args,kwargs)|(callable,pre_args,kwargs,post_args))]'
    if callable(f_or_fxx):
        f = f_or_fxx
        fxx = (f,)
    else:
        fxx = f_or_fxx
    fxx
    fxx = _frozen_fxx(*fxx)
    if not (fxx and callable(fxx[0])):raise TypeError(fxx)
    if not 1 <= len(fxx) <= 4:raise TypeError(fxx)
    fxx
    return fxx
_fxx0 = (echo, (), {}, ())
class DotCall:
    def __init__(sf, iter4f_or_fxx, /):
        'Iter (callable|(callable,pre_args)|(callable,pre_args,kwargs)|(callable,pre_args,kwargs,post_args)) -> None'
        fxxs = []
        for f_or_fxx in iter4f_or_fxx:
            fxx = _std_fxx(f_or_fxx)
            fxxs.append(fxx)
        sf._fxxs = tuple(fxxs)
    def __repr__(sf, /):
        ls4f_or_fxx = [*map(_simplify_fxx, sf._fxxs)]
        return repr_helper(sf, ls4f_or_fxx)
    def __call__(sf, /, *args, **kwds):
        fxxs = sf._fxxs
        if not fxxs:
            fxxs = [_fxx0]
        fxxs
        it = reversed(fxxs)
        fxx = next(it)
        [f, xs, d, ys] = fxx
        r = f(*xs, *args, *ys, **d, **kwds)
        777; del args, kwds
        for fxx in it:
            [f, xs, d, ys] = fxx
            r = f(*xs, r, *ys, **d)
        r
        return r
#end-class DotCall:
def dot_(*ls4f_or_fxx):
    '(*ls4f_or_fxx/[f_or_fxx]) -> DotCall/callable # [f_or_fxx == (callable|(callable,pre_args)|(callable,pre_args,kwargs)|(callable,pre_args,kwargs,post_args))]'
    return DotCall(ls4f_or_fxx)



__all__
#[dot_] = lazy_import4funcs_('seed.func_tools.dot_', 'dot_', __name__)
from seed.func_tools.dot_ import dot_
from seed.func_tools.dot_ import *
