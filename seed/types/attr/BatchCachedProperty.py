#__all__:goto
r'''[[[
e ../../python3_src/seed/types/attr/BatchCachedProperty.py
moved from:
    view ../../python3_src/seed/helper/lazy_import.py
see:
    from functools import cached_property
    view ../../python3_src/seed/types/LazyValueDict.py
see-tools:
    view ../../python3_src/seed/lang/apply_descriptor_protocol.py
    view ../../python3_src/seed/abc/IDescriptor.py

seed.types.attr.BatchCachedProperty
py -m nn_ns.app.debug_cmd   seed.types.attr.BatchCachedProperty -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.attr.BatchCachedProperty:__doc__ -ht # -ff -df

######################
using:mk_decorator8injector4batch_cached_property_
######################
>>> class T:
...     #@cached_property
...     @CachedProperty
...     def c(sf, /):
...         return 777
...     ... # a, b = ..., ...
>>> @mk_decorator8injector4batch_cached_property_(T)
... def _mk_a_b(sf, /) -> '(a, b)':
...     #or:def _mk_a_b(sf, /) -> ('a', 'b'):
...     #or:def _mk_a_b(sf, /) -> '(A, B)#(a, b)':
...     print('calling:_mk_a_b')
...     assert isinstance(sf, T)
...     assert not 'a' in vars(sf)
...     assert not 'b' in vars(sf)
...     a = 666
...     b = 999
...     return (a, b)
>>> T.a #doctest: +ELLIPSIS
BatchCachedProperty(CommonState4BatchCachedProperty(<function _mk_a_b at 0x...>, ('a', 'b')), 0, 'a')
>>> T.b #doctest: +ELLIPSIS
BatchCachedProperty(CommonState4BatchCachedProperty(<function _mk_a_b at 0x...>, ('a', 'b')), 1, 'b')
>>> T.c #doctest: +ELLIPSIS
<functools.cached_property object at 0x...>
>>> T.a.common_state4batch_cached_property.func is _mk_a_b
True
>>> T.b.common_state4batch_cached_property.func is _mk_a_b
True
>>> mk_decorator8injector4batch_cached_property_(T)(_mk_a_b)
Traceback (most recent call last):
    ...
AttributeError: ('existed:', 'a')
>>> _mk_a_b #assert mk_decorator8injector4batch_cached_property_(T)(_mk_a_b) is _mk_a_b #doctest: +ELLIPSIS
<function _mk_a_b at 0x...>

#######
>>> t = T()
>>> vars(t)
{}
>>> t.b
calling:_mk_a_b
999
>>> vars(t) == {'a': 666, 'b': 999}
True
>>> t.a
666
>>> vars(t) == {'a': 666, 'b': 999}
True
>>> t.c
777
>>> vars(t) == {'a': 666, 'b': 999, 'c': 777}
True

#######
>>> t = T()
>>> vars(t)
{}
>>> t.a
calling:_mk_a_b
666
>>> vars(t) == {'a': 666, 'b': 999}
True
>>> t.b
999

#######
>>> t = T()
>>> vars(t)
{}
>>> t.b
calling:_mk_a_b
999
>>> vars(t) == {'a': 666, 'b': 999}
True
>>> t.a
666


#######
>>> t = T()
>>> vars(t)
{}
>>> t.c
777
>>> vars(t)
{'c': 777}


######################
using:mk_batch_cached_properties_
######################
>>> def _mk_a_b(sf, /) -> '(a, b)':
...     #or:def _mk_a_b(sf, /) -> ('a', 'b'):
...     #or:def _mk_a_b(sf, /) -> '(A, B)#(a, b)':
...     print('calling:_mk_a_b')
...     assert isinstance(sf, T)
...     assert not 'a' in vars(sf)
...     assert not 'b' in vars(sf)
...     a = 666
...     b = 999
...     return (a, b)
>>> class T:
...     #@cached_property
...     @CachedProperty
...     def c(sf, /):
...         return 777
...     a, b = mk_batch_cached_properties_(_mk_a_b)
>>> T.a #doctest: +ELLIPSIS
BatchCachedProperty(CommonState4BatchCachedProperty(<function _mk_a_b at 0x...>, ('a', 'b')), 0, 'a')
>>> T.b #doctest: +ELLIPSIS
BatchCachedProperty(CommonState4BatchCachedProperty(<function _mk_a_b at 0x...>, ('a', 'b')), 1, 'b')
>>> T.c #doctest: +ELLIPSIS
<functools.cached_property object at 0x...>
>>> T.a.common_state4batch_cached_property.func is _mk_a_b
True
>>> T.b.common_state4batch_cached_property.func is _mk_a_b
True



#######
>>> t = T()
>>> vars(t)
{}
>>> t.b
calling:_mk_a_b
999
>>> vars(t) == {'a': 666, 'b': 999}
True
>>> t.a
666
>>> vars(t) == {'a': 666, 'b': 999}
True
>>> t.c
777
>>> vars(t) == {'a': 666, 'b': 999, 'c': 777}
True

#######
>>> t = T()
>>> vars(t)
{}
>>> t.a
calling:_mk_a_b
666
>>> vars(t) == {'a': 666, 'b': 999}
True
>>> t.b
999

#######
>>> t = T()
>>> vars(t)
{}
>>> t.b
calling:_mk_a_b
999
>>> vars(t) == {'a': 666, 'b': 999}
True
>>> t.a
666


#######
>>> t = T()
>>> vars(t)
{}
>>> t.c
777
>>> vars(t)
{'c': 777}


######################

######################




py_adhoc_call   seed.types.attr.BatchCachedProperty   @f
]]]'''#'''
__all__ = r'''
CachedProperty
BatchCachedProperty
    mk_batch_cached_properties_
    mk_decorator8injector4batch_cached_property_
CommonState4BatchCachedProperty
    mk_common_state4batch_cached_property_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_._Base4repr import _Base4repr
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.tiny_.check import check_type_is, check_type_le, check_uint_lt, check_int_ge, check_callable, check_pseudo_identifier
from seed.tiny import mk_tuple

#from seed.abc.IDescriptor import IDataDescriptor__default_mixin
from seed.abc.IDescriptor import IDataDescriptor

import re
from functools import cached_property
#.class ILazyAttr:
#.    'see:cached_property'
___end_mark_of_excluded_global_names__0___ = ...


#begin-BatchCachedProperty
class CommonState4BatchCachedProperty(_Base4repr):
    'cst/common_state4batch_cached_property'
    def __init__(sf, f, onms, /):
        check_callable(f)
        onms = mk_tuple(onms)
        for nm in onms:
            check_pseudo_identifier(nm)
        assert len(set(onms)) == len(onms), onms
        sf._f = f
        sf._onms = onms
        sf._reset4repr(_args4repr:=(f, onms), _kwds4repr:=None)
    @property
    def func(sf, /):
        '-> (instance -> tuple{len=(sf.names4output)})'
        return sf._f
    @property
    def names4output(sf, /):
        return sf._onms
    @cached_property
    def __isabstractmethod__(sf, /):
        '-> bool'
        return getattr(sf._f, '__isabstractmethod__', False)
    def mk_batch_cached_properties_(sf, /):
        '-> [BatchCachedProperty]'
        return tuple(BatchCachedProperty(sf, idx) for idx in range(len(sf.names4output)))
    def inject_batch_cached_properties_into_type_(sf, type4obj, /):
        check_type_le(type, type4obj)
        for nm in sf.names4output:
            if hasattr(type4obj, nm):raise AttributeError('existed:', nm)

        batch_cached_properties = sf.mk_batch_cached_properties_()
        for batch_cached_property in batch_cached_properties:
            #batch_cached_property.inject_into_type_(type4obj)
            nm = batch_cached_property.name
            if hasattr(type4obj, nm):raise AttributeError('existed:', nm)
            setattr(type4obj, nm, batch_cached_property)
    def set_properties_on_instance_dict_(sf, instance, d, /):
        output = sf.func(instance)
        check_type_is(tuple, output)
        if not len(output) == len(sf.names4output):raise TypeError
        for nm in sf.names4output:
            if nm in d:raise AttributeError('existed:', nm)
        for nm, v in zip(sf.names4output, output):
            #setattr(instance, nm, v)
            d[nm] = v
#class BatchCachedProperty(IDataDescriptor__default_mixin, _Base4repr):
class BatchCachedProperty(IDataDescriptor, _Base4repr):
    'batch_cached_property'
    ___no_slots_ok___ = True
    def __init__(sf, cst, idx, may_nm=None, /):
        #, may_alias=None
        check_type_is(CommonState4BatchCachedProperty, cst)
        check_uint_lt(len(cst.names4output), idx)
        nm = cst.names4output[idx]
        if not may_nm is None:
            assert nm == may_nm
        sf._cst = cst
        sf._idx = idx
        sf._nm = nm
        sf._reset4repr(_args4repr:=(cst, idx, nm), _kwds4repr:=None)
    @property
    def common_state4batch_cached_property(sf, /):
        '-> cst/CommonState4BatchCachedProperty'
        return sf._cst
    @property
    def idx(sf, /):
        return sf._idx
    @property
    def name(sf, /):
        return sf._nm

    #.def inject_into_type_(sf, type4obj, /):
    #.    check_type_le(type, type4obj)
    #.    nm = sf._nm
    #.    if hasattr(type4obj, nm):raise AttributeError('existed:', nm)
    #.    setattr(type4obj, nm, sf)

    @cached_property
    @override
    def __isabstractmethod__(sf, /):
        '-> bool'
        return sf._cst.__isabstractmethod__
    @override
    def __get__(sf, may_instance, may_owner=None, /):
        if may_instance is None:
            return sf
            #.return sf._cst.func
            #.return sf.__func__
        else:
            instance = may_instance
            d = vars(instance) # instance.__dict__
            nm = sf._nm
            try:
                return d[nm]
            except KeyError:
                pass
            sf._cst.set_properties_on_instance_dict_(instance, d)
            return getattr(instance, nm)
            #.return MethodType(sf.__func__, instance)
    @override
    def __set__(sf, instance, value, /):
        raise AttributeError(sf._nm)
    @override
    def __delete__(sf, instance, /):
        raise AttributeError(sf._nm)
    @override
    def __set_name__(sf, owner, name, /):
        if not name == sf._nm:raise AttributeError(owner, name, sf._nm)

_rex4onms = re.compile(r'(.*#)?\s*([(])\s*\w+\s*(,\s*\w+\s*)+([)])\s*')
def _mk_onms(may_nms, f, /):
    if may_nms is None:
        onms = f.__annotations__['return']
            # ^KeyError
        if type(onms) is str:
            return_annotation = onms
            m = _rex4onms.fullmatch(return_annotation)
            if not m:raise ValueError(f'format should be "(a,b,c)": {return_annotation!r}')
            onms = (return_annotation
                .replace('(', ' ')
                .replace(')', ' ')
                .replace(',', ' ')
                .split()
                )
            onms
        else:
            onms
            iter(onms)
        onms
    else:
        onms = may_nms
        #iter(onms)
    onms
    return onms
def mk_decorator8injector4batch_cached_property_(type4obj, may_nms=None, /):
    r'''[[[
usage:
>>> class T:
...     #@cached_property
...     @CachedProperty
...     def c(sf, /):
...         return 777
...     ...
>>> @mk_decorator8injector4batch_cached_property_(T)
... def _mk_a_b(sf, /) -> '(a, b)':
...     #or:def _mk_a_b(sf, /) -> ('a', 'b'):
...     #or:def _mk_a_b(sf, /) -> '(A, B)#(a, b)':
...     print('calling:_mk_a_b')
...     assert isinstance(sf, T)
...     assert not 'a' in vars(sf)
...     assert not 'b' in vars(sf)
...     a = 666
...     b = 999
...     return (a, b)
>>> t = T()
>>> vars(t)
{}
>>> t.b
calling:_mk_a_b
999
>>> vars(t) == {'a': 666, 'b': 999}
True
>>> t.a
666
>>> vars(t) == {'a': 666, 'b': 999}
True
>>> t.c
777
>>> vars(t) == {'a': 666, 'b': 999, 'c': 777}
True



    #]]]'''#'''
    def decorator8injector4batch_cached_property(f, /):
        cst = mk_common_state4batch_cached_property_(f, may_nms)
        #batch_cached_properties = cst.mk_batch_cached_properties_()
        cst.inject_batch_cached_properties_into_type_(type4obj)
        return f
    return decorator8injector4batch_cached_property
def mk_common_state4batch_cached_property_(f, may_nms=None, /):
    onms = _mk_onms(may_nms, f)
    cst = CommonState4BatchCachedProperty(f, onms)
    return cst
def mk_batch_cached_properties_(f, may_nms=None, /):
    '-> [BatchCachedProperty]'
    cst = mk_common_state4batch_cached_property_(f, may_nms)
    batch_cached_properties = cst.mk_batch_cached_properties_()
    return batch_cached_properties
#end-BatchCachedProperty
CachedProperty = cached_property




__all__
from seed.types.attr.BatchCachedProperty import CachedProperty, BatchCachedProperty, mk_batch_cached_properties_, mk_decorator8injector4batch_cached_property_
from seed.types.attr.BatchCachedProperty import CommonState4BatchCachedProperty, mk_common_state4batch_cached_property_
from seed.types.attr.BatchCachedProperty import *
