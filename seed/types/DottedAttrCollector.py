#__all__:goto
r'''[[[
e ../../python3_src/seed/types/DottedAttrCollector.py
used in:
    view ../../python3_src/seed/types/Symbol.py
    view ../../python3_src/seed/pkg_tools/load_module5attr.py
    view ../../python3_src/seed/types/LazyModule.py


seed.types.DottedAttrCollector
py -m nn_ns.app.debug_cmd   seed.types.DottedAttrCollector -x
py -m nn_ns.app.doctest_cmd seed.types.DottedAttrCollector:__doc__ -ht

>>> obj = ReDefRepr(lambda:'obj')
>>> obj
obj
>>> def call(sf, /, *args, **kwds):
...     return (sf, args, kwds)
>>> aaa = DottedAttrCollector(call, obj, (), 'aaa')
>>> aaa
aaa
>>> aaa.x.y.z
aaa.x.y.z
>>> aaa.x.y.z()
(aaa.x.y.z, (), {})
>>> aaa.x.y.z(333, 666, kkk=999)
(aaa.x.y.z, (333, 666), {'kkk': 999})


>>> bbb = DottedAttrCollector___autocall_at_max_depth(aaa, -1)
>>> DottedAttrCollector___autocall_at_max_depth(aaa, 0)
>>> ccc = DottedAttrCollector___autocall_at_max_depth(aaa, 1)
Traceback (most recent call last):
    ...
ValueError: imay_max_depth==0
>>> ddd = DottedAttrCollector___autocall_at_max_depth(aaa, 3)

>>> bbb.x.y.z.a.b.c
aaa.x.y.z.a.b.c
>>> bbb.x.y.z.a.b.c()
(aaa.x.y.z.a.b.c, (), {})
>>> ccc.x
(aaa.x, (), {})
>>> ddd.x
aaa.x
>>> ddd.x()
(aaa.x, (), {})
>>> ddd.x.y
aaa.x.y
>>> ddd.x.y()
(aaa.x.y, (), {})
>>> ddd.x.y.z
(aaa.x.y.z, (), {})




#]]]'''
__all__ = r'''
DottedAttrCollector
    DottedAttrCollector___autocall_at_max_depth

ReDefRepr

'''.split()#'''
__all__
from seed.tiny_.check import check_type_is, check_int_ge
from seed.tiny_.check import check_callable
from seed.tiny_.check import check_pseudo_identifier
from seed.data_funcs.lnkls import rglnkls2list


class ReDefRepr:
    def __init__(sf, f, /, *args):
        check_callable(f)
        sf._f = f
        sf._xs = args
        sf._m = None
    def __repr__(sf, /):
        if sf._m is None:
            s = sf._m = sf._f(*sf._xs)
            check_type_is(str, s)
        return sf._m
    @property
    def func(sf, /):
        return sf._f
    @property
    def args4func(sf, /):
        return sf._xs



class DottedAttrCollector(tuple):
    def __new__(cls, f, obj, lnkls8nms, may_repr4obj, /):
        check_callable(f)
        check_type_is(tuple, lnkls8nms)
        sf = tuple.__new__(cls, [f, obj, lnkls8nms, may_repr4obj])
        return sf
    if 0:
        #useless since __getattribute__
        @property
        def func(sf, /):
            return sf[0]
        @property
        def obj(sf, /):
            return sf[1]
        @property
        def lnkls8nms(sf, /):
            return sf[2]
        @property
        def may_repr4obj(sf, /):
            return sf[3]

    def __get_func__(sf, /):
        return sf[0]
    def __get_obj__(sf, /):
        return sf[1]
    def __get_lnkls8nms__(sf, /):
        return sf[2]
    def __get_may_repr4obj__(sf, /):
        return sf[3]



    def __list_names__(sf, /):
        [f, obj, lnkls8nms, may_repr4obj] = sf
        nms = rglnkls2list(lnkls8nms)
        return nms
    def __mk_qname4attr__(sf, /):
        ss = __class__.__list_names__(sf)
        return '.'.join(ss)
    def __getattribute__(sf, nm, /):
        check_pseudo_identifier(nm)
        [f, obj, lnkls8nms, may_repr4obj] = sf
        return type(sf)(f, obj, (lnkls8nms, nm), may_repr4obj)
    def __repr__(sf, /):
        [f, obj, lnkls8nms, may_repr4obj] = sf
        if may_repr4obj is None:
            s = repr(obj)
        elif type(may_repr4obj) is str:
            s = may_repr4obj
        else:
            repr4obj = may_repr4obj
            check_callable(repr4obj)
            s = repr4obj(obj)
        s
        ss = __class__.__list_names__(sf)
        ss.insert(0, s)
        return '.'.join(ss)
    def __call__(sf, /, *args, **kwds):
        [f, obj, lnkls8nms, may_repr4obj] = sf
        return f(sf, *args, **kwds)




class DottedAttrCollector___autocall_at_max_depth(tuple):
    def __new__(cls, qattr_clltr:DottedAttrCollector, imay_max_depth, /):
        check_type_is(DottedAttrCollector, qattr_clltr)
        if 1:
            check_int_ge(-1, imay_max_depth)
            if imay_max_depth == 0:raise ValueError(f'imay_max_depth==0')# Exception
        else:
            check_int_ge(1, imay_max_depth)
        sf = super(__class__, cls).__new__(cls, [qattr_clltr, imay_max_depth])
        return sf
        if 0:
            #bug: since __getattribute__
            sf._x = qattr_clltr
            sf._md = imay_max_depth
    def __call__(sf, /):
        x, i = sf
        return x()
    def __repr__(sf, /):
        x, i = sf
        return repr(x)
    def __getattribute__(sf, nm, /):
        x, i = sf
        y = getattr(x, nm)
        if i == 1:
            return y()
        if i > 0:
            i -= 1
        return type(sf)(y, i)
#end-class DottedAttrCollector___autocall_at_max_depth:



#def __():
#    #bug:__getattribute__==>>
#    #   ^RecursionError: maximum recursion depth exceeded
#  class WrappedCallable:
#    def __init__(sf, f, /):
#        check_callable(f)
#        sf.__f = f
#    @property
#    def func(sf, /):
#        return sf.__f
#    def __call__(sf, /, *args, **kwds):
#        return sf.__f(sf, *args, **kwds)
#
#
#  class DottedAttrCollector(WrappedCallable):
#    def __init__(sf, f, obj, lnkls8nms, /):
#        check_type_is(tuple, lnkls8nms)
#        sf.__obj = obj
#        sf.__nms = lnkls8nms
#        super().__init__(f)
#    @property
#    def obj(sf, /):
#        return sf.__obj
#    @property
#    def lnkls8names(sf, /):
#        return sf.__nms
#    def list_names(sf, /):
#        nms = rglnkls2list(sf.__nms)
#        return nms
#    def mk_qname4attr(sf, /):
#        ss = sf.list_names()
#        return '.'.join(ss)
#    def __getattribute__(sf, nm, /):
#        check_pseudo_identifier(nm)
#        return type(sf)(sf.func, sf.obj, (sf.lnkls8names, nm))
#    def __repr__(sf, /):
#        s = repr(sf.__obj)
#        ss = sf.list_names()
#        ss.insert(0, s)
#        return '.'.join(ss)
#
#    @property
#    def func(sf, /):
#        return sf.__f
#



__all__
from seed.types.DottedAttrCollector import DottedAttrCollector, ReDefRepr
from seed.types.DottedAttrCollector import DottedAttrCollector___autocall_at_max_depth
from seed.types.DottedAttrCollector import *
