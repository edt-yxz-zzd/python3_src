#__all__:goto
r'''[[[
e ../../python3_src/seed/abc/IEqTmpVal.py

seed.abc.IEqTmpVal
py -m nn_ns.app.debug_cmd   seed.abc.IEqTmpVal -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.abc.IEqTmpVal:__doc__ -ht # -ff -df
py_adhoc_call   seed.abc.IEqTmpVal   @f
#]]]'''
__all__ = r'''
IEqTmpVal
    eq8obj
    eq8tmp_val
    whether_obj_vs_val_
        lookup_ops8IEqTmpVal4cls_
        register_ops8IEqTmpVal4cls_
IEqTmpVal
    IEqTmpVal__via_iter_sized_args_kwds
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.lang.class_property import class_property# static_property
from seed.tiny_.check import check_type_is, check_type_le, check_callable
___end_mark_of_excluded_global_names__0___ = ...

class IEqTmpVal(ABC):
    __slots__ = ()
    @class_property
    @abstractmethod
    def __immutable__(cls, /):
        '-> obj_vs_val/bool'
    #.@class_property
    #.def obj_vs_val(cls, /):
    #.    '-> obj_vs_val/bool'
    #.    return cls.__immutable__
    @abstractmethod
    def __eq8tmp_val__(sf, ot, /):
        '[[not sf is ot][type(sf) is type(ot)]] => sf -> ot -> bool'
        # ? [not __immutable__]
    def __eq__(sf, ot, /):
        return eq8tmp_val(sf, ot)
def whether_obj_vs_val_(x, /):
    cls = type(x)
    ops = lookup_ops8IEqTmpVal4cls_(cls)
    obj_vs_val = ops.__immutable__
    check_type_is(bool, obj_vs_val)
    return obj_vs_val
def eq8obj(lhs, rhs, /):
    return _eq8xxx(lhs, rhs, obj_vs_tmp_val=False)
def eq8tmp_val(lhs, rhs, /):
    return _eq8xxx(lhs, rhs, obj_vs_tmp_val=True)
def _eq8xxx(lhs, rhs, /, *, obj_vs_tmp_val):
    if lhs is rhs:
        return True
    if not type(lhs) is type(rhs):
        return False
    cls = type(lhs)
    ops = lookup_ops8IEqTmpVal4cls_(cls)
    if not obj_vs_tmp_val:
        #eq8obj
        if not ops.__immutable__:
            # obj
            return False
        # val
    else:
        #eq8tmp_val
        # (obj|val)
        pass
    # (obj|val)
    b = ops.__eq8tmp_val__(lhs, rhs)
    check_type_is(bool, b)
    return b
_cls2ops8IEqTmpVal = {}
def lookup_ops8IEqTmpVal4cls_(cls, /):
    ops = _cls2ops8IEqTmpVal.get(cls, cls)
    return ops
def register_ops8IEqTmpVal4cls_(cls, ops, /):
    check_type_le(type, cls)
    check_type_is(bool, ops.__immutable__)
    check_callable(ops.__eq8tmp_val__)
    if not _cls2ops8IEqTmpVal.setdefault(cls, ops) is ops:raise KeyError(cls)
    return
    if cls in _cls2ops8IEqTmpVal:
        if not ops == _cls2ops8IEqTmpVal[cls]:raise KeyError(cls)
    else:
        _cls2ops8IEqTmpVal[cls] = ops
    return


class IEqTmpVal__via_iter_sized_args_kwds(IEqTmpVal):
    __slots__ = ()
    @abstractmethod
    def __iter_sized_args_kwds4tmp_val__(sf, /):
        'sf -> Iter(len(args), len(kwds), *args, *sorted(kwds.items()))'
    @override
    def __eq8tmp_val__(sf, ot, /):
        '[[not sf is ot][type(sf) is type(ot)]] => sf -> ot -> bool'
        cls = type(sf)
        f = cls.__iter_sized_args_kwds4tmp_val__
        return _eq4sized_iter(f(sf), f(ot))
def _eq4sized_iter(lhs, rhs, /):
    #lhs = iter(lhs)
    #rhs = iter(rhs)
    #for a, b in zip(lhs, rhs)
    return all(map(eq8tmp_val, lhs, rhs))



__all__
from seed.abc.IEqTmpVal import IEqTmpVal, IEqTmpVal__via_iter_sized_args_kwds
from seed.abc.IEqTmpVal import eq8obj, eq8tmp_val, whether_obj_vs_val_
from seed.abc.IEqTmpVal import lookup_ops8IEqTmpVal4cls_, register_ops8IEqTmpVal4cls_
from seed.abc.IEqTmpVal import *
