#__all__:goto
r'''[[[
e ../../python3_src/seed/types/attr/special_method6class_and_class_only_property.py
view ../../python3_src/seed/abc/IDescriptor.py

seed.types.attr.special_method6class_and_class_only_property
py -m nn_ns.app.debug_cmd   seed.types.attr.special_method6class_and_class_only_property -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.attr.special_method6class_and_class_only_property:__doc__ -ht # -ff -df




>>> object.__getattr__  # @py3_11_9
Traceback (most recent call last):
    ...
AttributeError: type object 'object' has no attribute '__getattr__'


######################
######################
>>> class T:
...     aaa = ClassOnlySpecialData(999)
...     @ClassOnlySpecialMethod
...     def f(sf, /):
...         return type(sf)
...     def g(cls, nm, /):
...         return (cls, nm)
...     g = mk_class_only_named_property__based_default_('', imay_xdefault_rank=2, xdefault=g)
...     ddd = ClassOnlySpecialData(666, _forbid_delattr_=True, _forbid_setattr_=True)

>>> T.aaa
999
>>> T().aaa
Traceback (most recent call last):
    ...
AttributeError: aaa

AttributeError: type object 'T' has no attribute '__getattr__'

>>> T.f()
Traceback (most recent call last):
    ...
TypeError: T.f() missing 1 required positional argument: 'sf'
>>> T.f(T()) is T
True
>>> T().f
Traceback (most recent call last):
    ...
AttributeError: f

AttributeError: type object 'T' has no attribute '__getattr__'

>>> T.g == (T, 'g')
True
>>> T().g
Traceback (most recent call last):
    ...
AttributeError: g

AttributeError: type object 'T' has no attribute '__getattr__'


>>> def getattr4T(sf, nm, /):
...     raise AttributeError(nm)
>>> T.__getattr__ = getattr4T
>>> T().aaa
Traceback (most recent call last):
    ...
AttributeError: aaa
>>> T().f
Traceback (most recent call last):
    ...
AttributeError: f
>>> T().g
Traceback (most recent call last):
    ...
AttributeError: g

>>> t = T()
>>> t.aaa
Traceback (most recent call last):
    ...
AttributeError: aaa
>>> t.f
Traceback (most recent call last):
    ...
AttributeError: f
>>> t.g
Traceback (most recent call last):
    ...
AttributeError: g


>>> t.aaa = 111
>>> t.f = 222
>>> t.g = 333

>>> t.aaa
111
>>> t.f
222
>>> t.g
333

>>> T.aaa
999
>>> T.f(T()) is T
True
>>> T.g == (T, 'g')
True

>>> del t.aaa
>>> del t.f
>>> del t.g


>>> T.aaa
999
>>> T.f(T()) is T
True
>>> T.g == (T, 'g')
True

>>> t.aaa
Traceback (most recent call last):
    ...
AttributeError: aaa
>>> t.f
Traceback (most recent call last):
    ...
AttributeError: f
>>> t.g
Traceback (most recent call last):
    ...
AttributeError: g



>>> T.ddd
666
>>> t.ddd
Traceback (most recent call last):
    ...
AttributeError: ddd
>>> t.ddd = 444
Traceback (most recent call last):
    ...
AttributeError: ddd
>>> del t.ddd
Traceback (most recent call last):
    ...
AttributeError: ddd
>>> t.ddd
Traceback (most recent call last):
    ...
AttributeError: ddd
>>> T.ddd
666
>>> vars(t)['ddd'] = 555
>>> t.ddd
555
>>> T.ddd
666
>>> t.ddd = 444
Traceback (most recent call last):
    ...
AttributeError: ddd
>>> del t.ddd
Traceback (most recent call last):
    ...
AttributeError: ddd
>>> t.ddd
555
>>> T.ddd
666





######################
######################
######################
######################
special_method6class
>>> class C:
...     @special_method6class
...     def f(sf, /):
...         return type(sf)
...     @special_method6class
...     @classmethod
...     def g(cls, /):
...         return cls
...     @special_method6class
...     @staticmethod
...     def h():
...         return 777
>>> C.f(C()) is C
True
>>> C.g() is C
True
>>> C.h() == 777
True
>>> c = C()
>>> c.f
Traceback (most recent call last):
    ...
AttributeError: f
>>> c.g
Traceback (most recent call last):
    ...
AttributeError: g
>>> c.h
Traceback (most recent call last):
    ...
AttributeError: h
>>> c.f = 123
>>> c.g = 456
>>> c.h = 789
>>> c.f
123
>>> c.g
456
>>> c.h
789
>>> C.f(C()) is C
True
>>> C.g() is C
True
>>> C.h() == 777
True




>>> class I(ABC):
...     __slots__ = ()
...     @special_method6class
...     @abstractmethod
...     def f(sf, /):
...         return type(sf)
...     @special_method6class
...     @classmethod
...     @abstractmethod
...     def g(cls, /):
...         return cls
...     @special_method6class
...     @staticmethod
...     @abstractmethod
...     def h():
...         return 777
>>> I.__abstractmethods__ == frozenset({'h', 'f', 'g'})
True


######################
######################
py_adhoc_call   seed.types.attr.special_method6class_and_class_only_property   @f
]]]'''#'''
__all__ = r'''
ClassOnlyNamedProperty
    mk_class_only_named_property__based_default_
    ClassOnlySpecialData
        ClassOnlySpecialMethod
    ClassOnlyNamedProperty__5descriptor
        get_via_descriptor6class_
        ClassOnlyClassMethod
        ClassOnlyStaticMethod

special_method6class
    ClassOnlySpecialMethod
    ClassOnlyClassMethod
    ClassOnlyStaticMethod


IClassOnlyDataDescriptor
    IClassOnlyDataDescriptor__named
        IClassOnlyDataDescriptor__named__init
            ClassOnlyNamedProperty



getattr_via_vars_
    getattr_via_vars__fallback_
delattr_via_vars_
setattr_via_vars_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.abc.IDescriptor import IDescriptor, INonDataDescriptor, IDataDescriptor
from seed.tiny_.check import check_pseudo_identifier, check_smay_pseudo_identifier, check_type_is, check_type_le, check_int_ge, check_may_, check_callable, check_non_ABC
from seed.tiny_.mk_fdefault import mk_default
    #def mk_default(imay_xdefault_rank, xdefault, /,*args4xdefault):
#from seed.for_libs.for_inspect__isolated import check_num_args_ok_, is_num_args_ok_
from seed.tiny_.mk_fdefault import check4mk_default_, check4mk_default__len_
    #def check4mk_default_(imay_xdefault_rank, xdefault, /, *args4xdefault):
    #def check4mk_default__len_(imay_xdefault_rank, xdefault, len_args4xdefault, /):
___end_mark_of_excluded_global_names__0___ = ...

class IClassOnlyDataDescriptor(IDataDescriptor):
    __slots__ = ()
    @abstractmethod
    def _get5owner_(sf, owner, /):
        'owner -> dat|^AttributeError'
    @abstractmethod
    def _get5instance_(sf, instance, /):
        'instance -> dat|^AttributeError'

    @property
    @abstractmethod
    def __isabstractmethod__(sf, /):
        '-> bool #play with @abc.abstractmethod'


    @abstractmethod
    def __set_name__(sf, owner, name, /):
        pass

    @abstractmethod
    def __set__(sf, instance, value, /):
        raise AttributeError
    @abstractmethod
    def __delete__(sf, instance, /):
        raise AttributeError


    @override
    def __get__(sf, may_instance, may_owner=None, /):
        if not may_instance is None:
            #6instance
            instance = may_instance
            try:
                return sf._get5instance_(instance)
            except AttributeError:
                #fallback
                owner = type(instance) if may_owner is None else may_owner
                #g = owner.__getattr__
                    # AttributeError: type object 'T' has no attribute '__getattr__'
                if not None is (g := getattr(owner, '__getattr__', None)):
                    return g(instance, sf._name_)
                raise
        if not may_owner is None:
            #6class
            owner = may_owner
            return sf._get5owner_(owner)
        return sf

class IClassOnlyDataDescriptor__named(IClassOnlyDataDescriptor):
    __slots__ = ()
    @property
    @abstractmethod
    def _forbid_delattr_(sf, /):
        '-> bool # see:__delete__'

    @property
    @abstractmethod
    def _forbid_setattr_(sf, /):
        '-> bool # see:__set__'

    @property
    @abstractmethod
    def _smay_name_(sf, /):
        '-> smay name/str # see: ._name_'
    @property
    def _name_(sf, /):
        '-> name/str|^AttributeError # for:getattr_via_vars_()'
        smay_name = sf._smay_name_
        if not smay_name:raise AttributeError
        name = smay_name
        return name

    @override
    def _get5instance_(sf, instance, /):
        'instance -> dat|^AttributeError'
        #fallback
        return getattr_via_vars_(instance, sf._name_, fallback=False)

    @override
    def __set__(sf, instance, value, /):
        if sf._forbid_setattr_:raise AttributeError(sf._name_)
        setattr_via_vars_(instance, sf._name_, value)
        return
        super(type(instance), instance).__setattr__(sf._name_, value)
            # RecursionError: maximum recursion depth exceeded
        return
        setattr(instance, sf._name_, value)
            # RecursionError: maximum recursion depth exceeded
        return
    @override
    def __delete__(sf, instance, /):
        if sf._forbid_delattr_:raise AttributeError(sf._name_)
        delattr_via_vars_(instance, sf._name_)
        return
        delattr(instance, sf._name_)



class IClassOnlyDataDescriptor__named__init(IClassOnlyDataDescriptor__named):
    ___no_slots_ok___ = True
    def __init__(sf, smay_name, /):
        check_smay_pseudo_identifier(smay_name)
        sf._snm = smay_name
    @property
    @override
    def _smay_name_(sf, /):
        '-> smay name/str # see: ._name_'
        smay_name = sf._snm
        return smay_name

    @override
    def __set_name__(sf, owner, name, /):
        check_pseudo_identifier(name)
        smay_name = sf._snm
        if not smay_name:
            sf._snm = name
        elif not smay_name == name:
            raise AttributeError(smay_name, name)
        assert sf._name_ == name

class ClassOnlyNamedProperty(IClassOnlyDataDescriptor__named__init):
    def __init__(sf, _forbid_delattr_, _forbid_setattr_, __isabstractmethod__, smay_name, imay_xdefault_rank, xdefault, /):
        # [args4xdefault == (sf, owner, name)]
        super().__init__(smay_name)
            # => check_smay_pseudo_identifier(smay_name)
        check_type_is(bool, _forbid_setattr_)
        check_type_is(bool, _forbid_delattr_)
        check_type_is(bool, __isabstractmethod__)
        #check4mk_default_(imay_xdefault_rank, xdefault, *(args4xdefault:=(sf, owner:=..., name:=...)))
        check4mk_default__len_(imay_xdefault_rank, xdefault, 3)
        #check_int_ge_le(-1, 3, imay_xdefault_rank)
        sf._x_d = _forbid_delattr_
        sf._x_s = _forbid_setattr_
        sf._abs = __isabstractmethod__
        sf._imay_num_args = imay_xdefault_rank
        sf._xf = xdefault
    @property
    @override
    def _forbid_delattr_(sf, /):
        '-> bool # see:__delete__'
        return sf._x_d

    @property
    @override
    def _forbid_setattr_(sf, /):
        '-> bool # see:__set__'
        return sf._x_s

    @property
    @override
    def __isabstractmethod__(sf, /):
        '-> bool #play with @abc.abstractmethod'
        return sf._abs

    @override
    def _get5owner_(sf, owner, /):
        'owner -> dat|^AttributeError'
        imay_xdefault_rank = sf._imay_num_args
        xdefault = sf._xf
        dat = mk_default(imay_xdefault_rank, xdefault, sf, owner, sf._name_)
        return dat
    def as_kwds_(sf, /):
        return dict(_forbid_delattr_=sf._forbid_delattr_, _forbid_setattr_=sf._forbid_setattr_, __isabstractmethod__=sf.__isabstractmethod__, smay_name=sf._smay_name_, imay_xdefault_rank=sf._imay_num_args, xdefault=sf._xf)
    @classmethod
    def from_kwds_(cls, /, *, _forbid_delattr_, _forbid_setattr_, __isabstractmethod__, smay_name, imay_xdefault_rank, xdefault):
        return cls(_forbid_delattr_, _forbid_setattr_, __isabstractmethod__, smay_name, imay_xdefault_rank, xdefault)
    def copy_then_replace_(sf, /, **kwds):
        d = sf.as_kwds_()
        d.update(kwds)
        cls = type(sf)
        ot = cls.from_kwds_(**d)
        return ot
def delattr_via_vars_(x, name, /):
    del vars(x)[name]
def setattr_via_vars_(x, name, value, /):
    vars(x)[name] = value
def getattr_via_vars_(x, name, /, *, fallback=False):
    'obj -> name -> (kw:fallback/(bool|(obj->name->value|^AttributeError))) -> value|^AttributeError # [[fallback is True] => using __getattr__]'
    try:
        return vars(x)[name]
    except KeyError:
        pass
    if type(fallback) is bool:
        if fallback is False:
            raise AttributeError(name)
        #fallback = type(x).__getattr__
            #AttributeError: type object 'T' has no attribute '__getattr__'
        fallback = getattr(type(x), '__getattr__', False)
        if fallback is False:
            raise AttributeError(name)
    return fallback(x, name)
def getattr_via_vars__fallback_(x, name, /):
    'obj -> name -> value|^AttributeError # [using __getattr__]'
    return getattr_via_vars_(x, name, fallback=True)
#_anonymous_default_class_only_named_property = ClassOnlyNamedProperty(False, False, False, '', 2, getattr_via_vars__fallback_)
_anonymous_default_class_only_named_property = ClassOnlyNamedProperty(False, False, False, '', 2, getattr_via_vars_)
def mk_class_only_named_property__based_default_(smay_name, **kwds):
    'smay_name -> ClassOnlyNamedProperty'
    return _anonymous_default_class_only_named_property.copy_then_replace_(smay_name=smay_name, **kwds)


class ClassOnlySpecialData(ClassOnlyNamedProperty):
    '__special_data6class__'
    def __init__(sf, data, /, smay_name='', __isabstractmethod__=False, _forbid_setattr_=False, _forbid_delattr_=False):
        #if not smay_name: smay_name = data.__name__
        super().__init__(_forbid_delattr_, _forbid_setattr_, __isabstractmethod__, smay_name, imay_xdefault_rank:=-1, xdefault:=data)
    @property
    def data(sf, /):
        return sf._xf


def special_method6class(func, /):
    'decorator'
    if isinstance(func, classmethod):
        T = ClassOnlyClassMethod
    elif isinstance(func, staticmethod):
        T = ClassOnlyStaticMethod
    else:
        T = ClassOnlySpecialMethod
    return T(func, __isabstractmethod__ = getattr(func, '__isabstractmethod__', False))
def _getattr_via_descriptor6class_(sf, owner, name, /):
    return get_via_descriptor6class_(sf.descriptor, owner)
def get_via_descriptor6class_(descriptor, owner, /):
    'descriptor -> owner -> value|^AttributeError # [using __get__]'
    return type(descriptor).__get__(descriptor, None, owner)
class ClassOnlyNamedProperty__5descriptor(ClassOnlyNamedProperty):
    def _check_descriptor_(sf, descriptor, /):
        check_type_le(IDescriptor, descriptor)
    def __init__(sf, descriptor, /, smay_name='', __isabstractmethod__=False, _forbid_setattr_=False, _forbid_delattr_=False):
        sf._check_descriptor_(descriptor)
        super().__init__(_forbid_delattr_, _forbid_setattr_, __isabstractmethod__, smay_name, imay_xdefault_rank:=3, xdefault:=_getattr_via_descriptor6class_)
        sf._dsc = descriptor
    @property
    def descriptor(sf, /):
        return sf._dsc

class ClassOnlyClassMethod(ClassOnlyNamedProperty__5descriptor):
    'classmethod'
    def _check_descriptor_(sf, descriptor, /):
        check_type_is(classmethod, descriptor)
class ClassOnlyStaticMethod(ClassOnlyNamedProperty__5descriptor):
    'staticmethod'
    def _check_descriptor_(sf, descriptor, /):
        check_type_is(staticmethod, descriptor)
class ClassOnlySpecialMethod(ClassOnlySpecialData):
    '__special_method6class__'
    def __init__(sf, func, /, smay_name='', __isabstractmethod__=False, _forbid_setattr_=False, _forbid_delattr_=False):
        check_callable(func)
        #if not smay_name: smay_name = func.__name__
        super().__init__(func, smay_name=smay_name, __isabstractmethod__=__isabstractmethod__, _forbid_setattr_=_forbid_setattr_, _forbid_delattr_=_forbid_delattr_)
    @property
    def func(sf, /):
        return sf.data

check_non_ABC(ClassOnlySpecialMethod)
check_non_ABC(ClassOnlySpecialData)
check_non_ABC(ClassOnlyNamedProperty)
r'''[[[
class ClassOnlyProperty(IClassOnlyDataDescriptor):
    def __init__(sf, __isabstractmethod__, smay_name, dat, may_fget, may_fset, may_fdel, may_doc, /):
|  deleter(...)
|      Descriptor to obtain a copy of the property with a different deleter.
 |
 |  getter(...)
 |      Descriptor to obtain a copy of the property with a different getter.
 |
 |  setter(...)
 |      Descriptor to obtain a copy of the property with a different setter.
|
 |    fget
 |      function to be used for getting an attribute value
 |    fset
 |      function to be used for setting an attribute value
 |    fdel
 |      function to be used for delelting an attribute
 |    doc
 |      docstring

#]]]'''#'''
__all__
from seed.types.attr.special_method6class_and_class_only_property import ClassOnlyNamedProperty, mk_class_only_named_property__based_default_
from seed.types.attr.special_method6class_and_class_only_property import ClassOnlySpecialData, ClassOnlySpecialMethod
from seed.types.attr.special_method6class_and_class_only_property import special_method6class, ClassOnlySpecialMethod, ClassOnlyClassMethod, ClassOnlyStaticMethod
from seed.types.attr.special_method6class_and_class_only_property import *
