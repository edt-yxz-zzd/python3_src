#__all__:goto
r'''[[[
e ../../python3_src/seed/tiny_/map_.py

seed.tiny_.map_
py -m nn_ns.app.debug_cmd   seed.tiny_.map_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.tiny_.map_:__doc__ -ht # -ff -df
#######

[[
源起:
view ../../python3_src/seed/tiny_/check.py

def _call_(check_, obj, /):
    'check_ :: (obj->None) | ((obj->(*args)->None), *args)'
    if callable(check_):
        check_(obj)
    else:
        check_, *args = check_
        check_(*args, obj)

def check_all_(check_, objs, /):
    for obj in objs:
        _call_(check_, obj)

]]


'#'; __doc__ = r'#'
>>> cmap_(tuple, [cmap_, tuple, int], '123')
((1,), (2,), (3,))
>>> cmap_(tuple, [cmap_, list, int], '123')
([1], [2], [3])
>>> cmap_(tuple, [cmap_, list, str], [[], [1, 2], [999]])
([], ['1', '2'], ['999'])

>>> tuple(map_([cmap_, list, str], [[], [1, 2], [999]]))
([], ['1', '2'], ['999'])
>>> tuple(map_(dots_(list, [map_, str]), [[], [1, 2], [999]]))
([], ['1', '2'], ['999'])
>>> dots_(tuple, map_)(dots_(list, [map_, str]), [[], [1, 2], [999]])
([], ['1', '2'], ['999'])



py_adhoc_call   seed.tiny_.map_   @f
]]]'''#'''
__all__ = r'''
map_
    cmap_
    call_
        prepare4call_
    dots_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...

#.class TypeError_or_NotImplementedError(Exception):pass


def call_(f_, /, *xs):
    'f_ :: (x->out) | ((x->(*args)->out), *args)'
    if callable(f_):
        return f_(*xs)
    else:
        f_args = f_
        (f_, args, _args, kwds) = _params5f_args_(f_args)
        return f_(*args, *xs, *_args, **kwds)
    return prepare4call_(f_)(*xs)

def dots_(*fs):
    #fs = tuple(fs)
    if not fs:raise TypeError
    if len(fs) == 1:
        f_ = prepare4call_(*fs)
    else:
        f_ = _Dots(fs)
    return f_
def prepare4call_(f_, /):
    return f_ if callable(f_) else _F_ARGS(f_)
class _Dots:
    def __init__(sf, fs, /):
        fs = cmap_(tuple, prepare4call_, fs)
        assert fs
        sf._fs = fs[:-1]
        sf._inner_f = fs[-1]
    def __call__(sf, /, *xs, **_kwds):
        r = sf._inner_f(*xs, **_kwds)
        for f in reversed(sf._fs):
            r = f(r)
        return r
class _F_ARGS:
    def __init__(sf, f_args, /):
        sf._args = _params5f_args_(f_args)
    def __call__(sf, /, *xs, **_kwds):
        (f_, args, _args, kwds) = sf._args
        return f_(*args, *xs, *_args, **kwds, **_kwds)

def cmap_(T, f_, /, *xss):
    return call_(T, map_(f_, *xss))

def map_(f_, /, *xss):
    #for x in xs: yield call_(f_, x)
    if callable(f_):
        return map(f_, *xss)
    return _map2_(f_, xss)
def _params5f_(f_, /):
    if callable(f_):
        args = ''
        _args = ''
        kwds = {}
    else:
        f_args = f_
        (f_, args, _args, kwds) = _params5f_args_(f_args)
    return (f_, args, _args, kwds)
def _params5f_args_(f_args, /):
    if callable(f_args[0]):
        [f_, *args] = f_args
        _args = ''
        kwds = {}
    elif callable(f_args[1]):
        [kwds_or_args, f_, *args] = f_args
        if hasattr(kwds_or_args, 'items'):
            kwds = kwds_or_args
            _args = ''
        else:
            _args = kwds_or_args
            kwds = {}
    elif callable(f_args[2]):
        [_args, kwds, f_, *args] = f_args
    else:
        raise TypeError(f_args)
    return (f_, args, _args, kwds)
def _map2_(f_args, xss, /):
    (f_, args, _args, kwds) = _params5f_args_(f_args)

    #.if not xss: return iter('')
    return (f_(*args, *xs, *_args, **kwds) for xs in zip(*xss))
    raise 000
assert cmap_(tuple, [cmap_, tuple, int], '123') == ((1,), (2,), (3,))
assert cmap_(tuple, [cmap_, list, int], '123') == ([1], [2], [3])
assert cmap_(tuple, [cmap_, list, str], [[], [1, 2], [999]]) == ([], ['1', '2'], ['999'])

assert tuple(map_([cmap_, list, str], [[], [1, 2], [999]])) == ([], ['1', '2'], ['999'])
assert tuple(map_(dots_(list, [map_, str]), [[], [1, 2], [999]])) == ([], ['1', '2'], ['999'])
assert dots_(tuple, map_)(dots_(list, [map_, str]), [[], [1, 2], [999]]) == ([], ['1', '2'], ['999'])

__all__
from seed.tiny_.map_ import map_, cmap_, call_, prepare4call_, dots_
from seed.tiny_.map_ import *
