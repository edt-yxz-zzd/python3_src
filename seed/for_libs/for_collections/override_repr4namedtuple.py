#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_collections/override_repr4namedtuple.py

seed.for_libs.for_collections.override_repr4namedtuple
py -m nn_ns.app.debug_cmd   seed.for_libs.for_collections.override_repr4namedtuple -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.for_libs.for_collections.override_repr4namedtuple:__doc__ -ht # -ff -df

[[
override namedtuple.__repr__:
    T(a=111, b=...) --> T(111, ...)
]]


>>> C = mk_namedtuple_('C', 'x y')
>>> C(111, 999)
C(111, 999)
>>> B = namedtuple('B', 'x y')
>>> B(111, 999)
B(x=111, y=999)

]]]'''#'''
__all__ = r'''
mk_namedtuple_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from functools import wraps
#.from collections import namedtuple
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
namedtuple = lazy_import4func_('collections', 'namedtuple', __name__)
___end_mark_of_excluded_global_names__0___ = ...


#def __repr__(sf, /):
def _repr4namedtuple_(sf, /):
    # T(a=111, b=...) --> T(111, ...)
    return repr_helper(sf, *sf)
def mk_namedtuple_(__module__, nm, nms_or_str, /, *args, **kwds):
    #.if type(nms_or_str) is str:
    #.    nms_str = nms_or_str
    #.    nms = nms_str.split()
    #.else:
    #.    nms = nms_or_str
    #.nms
    T = namedtuple(nm, nms_or_str, *args, module=__module__, **kwds)
    T.__repr__ = _repr4namedtuple_
    return T
def mk_namedtuple__check6make_(__module__, nm, nms_or_str, /, *args, **kwds):
    T = mk_namedtuple_(__module__, nm, nms_or_str, *args, **kwds)
    return _4check6make_(T)
def _4check6make_(T, /):
    old_new_ = T.__new__
    @wraps(old_new_)
    def __new__(cls, /, *args, **kwds):
        sf = old_new_(cls, *args, **kwds)
        cls._check6make_(sf)
        return sf
    #old_make_ = T._make
    old_make_ = vars(T)['_make'].__func__
    @classmethod
    def _make(cls, iterable, /):
        sf = old_make_(iterable)
        cls._check6make_(sf)
        return sf
    T.__new__ = __new__
    T._make = _make
    T._check6make_ = _check6make_
    return T
def _check6make_(sf, /):
    '-> None # called by cls._make()'

__all__
from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple_, mk_namedtuple__check6make_
#[mk_namedtuple_,mk_namedtuple__check6make_] = lazy_import4funcs_('seed.for_libs.for_collections.override_repr4namedtuple', 'mk_namedtuple_,mk_namedtuple__check6make_', __name__)
#def mk_namedtuple_(__module__, nm, nms_or_str, /, *args, **kwds):
#def mk_namedtuple__check6make_(__module__, nm, nms_or_str, /, *args, **kwds):
#    def _check6make_(sf, /):
from seed.for_libs.for_collections.override_repr4namedtuple import *
