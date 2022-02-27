#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
seed.abc.IDescriptor
py -m seed.abc.IDescriptor
py -m nn_ns.app.debug_cmd   seed.abc.IDescriptor


seed.lang.basic_descriptors
seed.lang.apply_descriptor_protocol
seed.abc.IDescriptor
seed.types.attr.CachedLazyProperty
e ../../python3_src/seed/lang/basic_descriptors.py
e ../../python3_src/seed/lang/apply_descriptor_protocol.py
e ../../python3_src/seed/abc/IDescriptor.py
from seed.types.attr.CachedLazyProperty import CachedLazyProperty




from seed.abc.IDescriptor import IDescriptor, INonDataDescriptor, IDataDescriptor
from seed.abc.IDescriptor import IDescriptor__default_mixin, INonDataDescriptor__default_mixin, IDataDescriptor__default_mixin
from seed.abc.IDescriptor import IDescriptor__wrap_func, IDescriptor4InstanceMethod, IDescriptor4ClassMethod, IDescriptor4StaticMethod, IDescriptor4Echo, IDescriptor__using_update_wrapper, IDescriptor4Property

from seed.abc.IDescriptor import NonDataDescriptor4InstanceMethod, NonDataDescriptor4ClassMethod, NonDataDescriptor4StaticMethod, NonDataDescriptor4Echo, NonDataDescriptor4Property
from seed.abc.IDescriptor import descriptor4instance_method, descriptor4class_method, descriptor4static_method, descriptor4echo, descriptor4property
from seed.abc.IDescriptor import DataDescriptor4InstanceMethod, DataDescriptor4ClassMethod, DataDescriptor4StaticMethod, DataDescriptor4Echo, DataDescriptor4Property
from seed.abc.IDescriptor import data_descriptor4instance_method, data_descriptor4class_method, data_descriptor4static_method, data_descriptor4echo, data_descriptor4property





#[[[doc_sections:begin
#py38_doc__Descriptor_HowTo_Guide:goto
#py38_doc__Implementing_Descriptors:goto
#doctest_examples:goto
#wwwzzz:goto


#[[[py38_doc__Descriptor_HowTo_Guide:begin

Descriptor Protocol

[is descriptor] iff has any one of:
    descr.__get__(self, obj, type=None) -> value
    descr.__set__(self, obj, value) -> None
    descr.__delete__(self, obj) -> None
[is data-descriptor] iff has any one of:
    __set__
    __delete__
[is non-data-descriptor] iff has __get__ but no __set__,__delete__

object.__getattribute__()
    b.x
    may_u_or_descriptor = type(b).__dict__['x'] or super...
    if u_or_descriptor not exist or u_or_descriptor is not descriptor or u_or_descriptor is INonDataDescriptor:
        may_v = b.__dict__['x']
        if v exists: return v
        pass
    if u_or_descriptor not exists:
        __getattr__...
    if u:
        return u
    return descriptor.__get__(b, type(b))

type.__getattribute__()
    B.x
    u_or_descriptor = B.__dict__['x'] or super...
    return:
        u
        descriptor.__get__(None, B)
super.__getattribute__()
    super(B, obj).x
    super(B, type(obj)).x
    type(b).__mro__ = [type(b),...0*, B, ...-1*, object]]
        B may be object
    if find A:type(b).__mro__ = [type(b),...0*, B,...0*, A, ...-1*, object]]
        A may be object
    search A iff nearest to B && A.__dict__['x']
        py_doc:return  A.__dict__['m'].__get__(obj, B)
            ## B!!! not None/type(obj)/A!!!!
        py_impl:return  A.__dict__['m'].__get__(obj, type(obj))
            !!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!
            ????classmethod receive B????
                see below: test_super_in_classmethod/NonDataDescriptor4Echo
                @classmethod
                def f(cls, /):
                    super(__class__, cls).f()
                doc say ==>> A.f(__class__) instead of A.f(cls)!!
                error!!! actually A.f(cls)!!!
            !!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!
            !!!!!!!!!!!!!!!!!!!!!!
    else no A found:
        object.__getattribute__ for what??
            ???(type(obj), 'x')???
            ???(obj, 'x')???
            ???(super(B, obj), 'x')???
                !!!!!!
                super.__self__/.__self_class__/.__thisclass__
                help(super)
                |  __self__
                |      the instance invoking super(); may be None
                |  __self_class__
                |      the type of the instance invoking super(); may be None
                |  __thisclass__
                |      the class invoking super()




5:
    descriptors are invoked by the __getattribute__() method

    overriding __getattribute__() prevents automatic descriptor calls

    object.__getattribute__() and type.__getattribute__() make different calls to __get__().

    data descriptors always override instance dictionaries.

    non-data descriptors may be overridden by instance dictionaries.

The object returned by super() also has a custom __getattribute__() method for invoking descriptors. The attribute lookup super(B, obj).m searches obj.__class__.__mro__ for the base class A immediately following B and then returns A.__dict__['m'].__get__(obj, B). If not a descriptor, m is returned unchanged. If not in the dictionary, m reverts to a search using object.__getattribute__().

The implementation


#]]]py38_doc__Descriptor_HowTo_Guide:end

#[[[py38_doc__Implementing_Descriptors:begin
3.3.2.2. Implementing Descriptors

The following methods only apply when an instance of the class containing the method (a so-called descriptor class) appears in an owner class (the descriptor must be in either the owner’s class dictionary or in the class dictionary for one of its parents). In the examples below, “the attribute” refers to the attribute whose name is the key of the property in the owner class’ __dict__.

object.__get__(self, instance, owner=None)

    Called to get the attribute of the owner class (class attribute access) or of an instance of that class (instance attribute access). The optional owner argument is the owner class, while instance is the instance that the attribute was accessed through, or None when the attribute is accessed through the owner.

    This method should return the computed attribute value or raise an AttributeError exception.

    PEP 252 specifies that __get__() is callable with one or two arguments. Python’s own built-in descriptors support this specification; however, it is likely that some third-party tools have descriptors that require both arguments. Python’s own __getattribute__() implementation always passes in both arguments whether they are required or not.

object.__set__(self, instance, value)

    Called to set the attribute on an instance instance of the owner class to a new value, value.

    Note, adding __set__() or __delete__() changes the kind of descriptor to a “data descriptor”. See Invoking Descriptors for more details.

object.__delete__(self, instance)

    Called to delete the attribute on an instance instance of the owner class.

object.__set_name__(self, owner, name)

    Called at the time the owning class owner is created. The descriptor has been assigned to name.

    Note

    __set_name__() is only called implicitly as part of the type constructor, so it will need to be called explicitly with the appropriate parameters when a descriptor is added to a class after initial creation:

    class A:
       pass
    descr = custom_descriptor()
    A.attr = descr
    descr.__set_name__(A, 'attr')

    See Creating the class object for more details.

    New in version 3.6.

The attribute __objclass__ is interpreted by the inspect module as specifying the class where this object was defined (setting this appropriately can assist in runtime introspection of dynamic class attributes). For callables, it may indicate that an instance of the given type (or a subclass) is expected or required as the first positional argument (for example, CPython sets this attribute for unbound methods that are implemented in C).
3.3.2.3. Invoking Descriptors

In general, a descriptor is an object attribute with “binding behavior”, one whose attribute access has been overridden by methods in the descriptor protocol: __get__(), __set__(), and __delete__(). If any of those methods are defined for an object, it is said to be a descriptor.

The default behavior for attribute access is to get, set, or delete the attribute from an object’s dictionary. For instance, a.x has a lookup chain starting with a.__dict__['x'], then type(a).__dict__['x'], and continuing through the base classes of type(a) excluding metaclasses.

However, if the looked-up value is an object defining one of the descriptor methods, then Python may override the default behavior and invoke the descriptor method instead. Where this occurs in the precedence chain depends on which descriptor methods were defined and how they were called.

The starting point for descriptor invocation is a binding, a.x. How the arguments are assembled depends on a:

Direct Call

    The simplest and least common call is when user code directly invokes a descriptor method: x.__get__(a).
Instance Binding

    If binding to an object instance, a.x is transformed into the call: type(a).__dict__['x'].__get__(a, type(a)).
Class Binding

    If binding to a class, A.x is transformed into the call: A.__dict__['x'].__get__(None, A).
Super Binding

    If a is an instance of super, then the binding super(B, obj).m() searches obj.__class__.__mro__ for the base class A immediately preceding B and then invokes the descriptor with the call: A.__dict__['m'].__get__(obj, obj.__class__).

For instance bindings, the precedence of descriptor invocation depends on the which descriptor methods are defined. A descriptor can define any combination of __get__(), __set__() and __delete__(). If it does not define __get__(), then accessing the attribute will return the descriptor object itself unless there is a value in the object’s instance dictionary. If the descriptor defines __set__() and/or __delete__(), it is a data descriptor; if it defines neither, it is a non-data descriptor. Normally, data descriptors define both __get__() and __set__(), while non-data descriptors have just the __get__() method. Data descriptors with __set__() and __get__() defined always override a redefinition in an instance dictionary. In contrast, non-data descriptors can be overridden by instances.

Python methods (including staticmethod() and classmethod()) are implemented as non-data descriptors. Accordingly, instances can redefine and override methods. This allows individual instances to acquire behaviors that differ from other instances of the same class.

The property() function is implemented as a data descriptor. Accordingly, instances cannot override the behavior of a property.
#]]]py38_doc__Implementing_Descriptors:end


#[[[doctest_examples:begin

test_super_in_classmethod/NonDataDescriptor4Echo
    ... ... xxxxxxx
test abstractmethod+NonDataDescriptor4InstanceMethod
test C.f is INonDataDescriptor

>>> class A:
...     @classmethod
...     def f(cls, /):return cls
>>> class B(A):
...     @classmethod
...     def f(cls, /):return super(__class__, cls).f()
>>> class C(B):pass
>>> C.f() is C
True
>>> super(B, C).f() is C
True
>>> super(B, C()).f() is C
True
>>> del A, B, C

>>> class A:
...     @NonDataDescriptor4Echo
...     def f(cls, /):return cls
>>> class B(A):
...     @NonDataDescriptor4Echo
...     def f(sf_or_cls, /):return super(__class__, sf_or_cls).f()
>>> class C(B):pass
>>> c = C()
>>> A_f = A.__dict__['f']
>>> B_f = B.__dict__['f']
>>> type(A_f) is NonDataDescriptor4Echo
True
>>> type(B_f) is NonDataDescriptor4Echo
True
>>> C.f == (B_f, None, C)
True
>>> c.f == (B_f, c, C)
True
>>> super(B,C).f == (A_f, None, C)
True
>>> super(B,c).f == (A_f, c, C)
True
>>> del A, B, C


>>> def g():pass
>>> is_descriptor(g)
True
>>> is_descriptor(classmethod(g))
True
>>> is_descriptor(staticmethod(g))
True
>>> is_descriptor(property(g))
True
>>> is_descriptor(B_f)
True

>>> is_non_data_descriptor(g)
True
>>> is_non_data_descriptor(classmethod(g))
True
>>> is_non_data_descriptor(staticmethod(g))
True
>>> is_non_data_descriptor(property(g))
False
>>> is_non_data_descriptor(B_f)
True

>>> is_data_descriptor(g)
False
>>> is_data_descriptor(classmethod(g))
False
>>> is_data_descriptor(staticmethod(g))
False
>>> is_data_descriptor(property(g))
True
>>> is_data_descriptor(B_f)
False





#>>> from seed.abc.abc import abstractmethod, override, ABC, ABC__no_slots
#>>> class B(ABC__no_slots):
>>> class B(ABC):
...     __slots__ = ()
...     @NonDataDescriptor4InstanceMethod
...     @abstractmethod
...     def f(sf, /):pass
>>> B()
Traceback (most recent call last):
    ...
TypeError: Can't instantiate abstract class B with abstract methods f

#'






#>>> from types import MethodDescriptorType, ClassMethodDescriptorType, MethodWrapperType, WrapperDescriptorType, MethodType
>>> from types import FunctionType, LambdaType, MethodType, BuiltinFunctionType, BuiltinMethodType
>>> class C:
...     def f(sf, /):pass

>>> type(lambda:()) is LambdaType
True
>>> type(C.f) is FunctionType
True
>>> type(C().f) is MethodType
True
>>> type(id) is BuiltinFunctionType
True


# C.f is INonDataDescriptor

>>> hasattr(type(lambda:()), '__get__')
True
>>> hasattr(type(C.f), '__get__')
True
>>> hasattr(type(C().f), '__get__')
True
>>> hasattr(type(id), '__get__')
False


>>> hasattr(LambdaType, '__get__')
True
>>> hasattr(FunctionType, '__get__')
True
>>> hasattr(MethodType, '__get__')
True
>>> hasattr(BuiltinFunctionType, '__get__')
False
>>> hasattr(BuiltinMethodType, '__get__')
False


>>> BuiltinFunctionType.__get__
Traceback (most recent call last):
    ...
AttributeError: type object 'builtin_function_or_method' has no attribute '__get__'
>>> IDescriptor.__subclasshook__(BuiltinFunctionType)
NotImplemented

>>> bool(NotImplemented)
True

>>> issubclass(type, IDescriptor)
False
>>> issubclass(object, IDescriptor)
False
>>> issubclass(BuiltinFunctionType, IDescriptor)
False
>>> issubclass(BuiltinMethodType, IDescriptor)
False


>>> issubclass(LambdaType, INonDataDescriptor)
True
>>> issubclass(FunctionType, INonDataDescriptor)
True
>>> issubclass(MethodType, INonDataDescriptor)
True

>>> issubclass(LambdaType, IDataDescriptor)
False
>>> issubclass(FunctionType, IDataDescriptor)
False
>>> issubclass(MethodType, IDataDescriptor)
False




...
#]]]doctest_examples:end

#[[[wwwzzz:begin
#]]]wwwzzz:end
#]]]doc_sections:end



#'''
#]]]__doc__:end






__all__ = '''
    is_descriptor
        is_data_descriptor
        is_non_data_descriptor

    IDescriptor
        INonDataDescriptor
        IDataDescriptor

    IDescriptor__default_mixin
        INonDataDescriptor__default_mixin
        IDataDescriptor__default_mixin

    IDescriptor__wrap_func
        IDescriptor4InstanceMethod
        IDescriptor4ClassMethod
        IDescriptor4StaticMethod
        IDescriptor4Echo
        IDescriptor__using_update_wrapper
        IDescriptor4Property

    NonDataDescriptor4InstanceMethod
    NonDataDescriptor4ClassMethod
    NonDataDescriptor4StaticMethod
    NonDataDescriptor4Echo
    NonDataDescriptor4Property
        descriptor4instance_method
        descriptor4class_method
        descriptor4static_method
        descriptor4echo
        descriptor4property
    DataDescriptor4InstanceMethod
    DataDescriptor4ClassMethod
    DataDescriptor4StaticMethod
    DataDescriptor4Echo
    DataDescriptor4Property
        data_descriptor4instance_method
        data_descriptor4class_method
        data_descriptor4static_method
        data_descriptor4echo
        data_descriptor4property


    '''.split()

#from seed.abc.abc import abstractmethod, override, ABC
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from types import MethodDescriptorType, ClassMethodDescriptorType, MethodWrapperType, WrapperDescriptorType, MethodType
from types import FunctionType, LambdaType, MethodType, BuiltinFunctionType, BuiltinMethodType
from functools import partial, update_wrapper
#import functools
from seed.abc.wrapper.IWrapper4Func import IWrapper4Func, Wrapper4Func__using_slots, Wrapper4Func__no_slots
from seed.debug.expectError import expectError
from seed.lang.apply_descriptor_protocol import is_descriptor, is_data_descriptor, is_non_data_descriptor

#HHHHH
#[[[main_body_src_code:begin
#zzzwww:goto

class IDescriptor(ABC):
    r'''
    howto remove __get__?
        "return self" work!
    def __set__ or __delete__ ==>> override instance.__dict__
        data-descriptor
        property
    not def __set__ & __delete__ ==>> be overridden by instance.__dict__
        non-data-descriptor
        staticmethod
        classmethod
        def user_defined_func()
            #C.f is INonDataDescriptor
    #'''

    __slots__ = ()

    @abstractmethod
    def __get__(sf, may_instance, may_owner=None, /):
        r'''
        #'''
        assert may_owner is None or isinstance(may_owner, type)
        #bug:assert may_instance is not None or may_owner is not None
        #   super(B, obj) ==>> __get__(obj, B)
        #bug:assert (may_instance is None or may_owner is None) or type(may_instance) is may_owner
        assert (may_instance is None or may_owner is None) or isinstance(may_instance, may_owner)
        return sf
        if 0:
            r'''
            why "return sf"?
                since deine any one of __get__, __set__, __delete__ ==>> IDescriptor
                but ABC cannot express that
                by "return sf", INonDataDescriptor work-as-if not-a-descriptor
            #'''
        raise AttributeError
    @abstractmethod
    def __set_name__(sf, owner, name, /):
        raise AttributeError

    @property
    @abstractmethod
    def __isabstractmethod__(sf, /):
        'play with @abc.abstractmethod'
        return True

    @classmethod
    @override
    def __subclasshook__(cls, C, /):
        # ABCMeta::__subclasshook__
        if cls is __class__:
            #assert isinstance(C, type)
            if any('__get__' in B.__dict__ for B in C.__mro__):
                return True
            #return False#bug??missing??
        return NotImplemented



class ____0:
    __slots__ = ()
class ____1:
    __slots__ = ()
class INonDataDescriptor(____0, ____1, IDescriptor):
    __slots__ = ()
    def __init_subclass__(cls, /,*args, **kwargs):
        if hasattr(cls, '__set__'):raise logic-err
        if hasattr(cls, '__delete__'):raise logic-err
        super().__init_subclass__(*args, **kwargs)
    @classmethod
    @override
    def __subclasshook__(cls, C, /):
        # ABCMeta::__subclasshook__
        if cls is __class__:
            #assert isinstance(C, type)
            #bug:recur:if issubclass(C, IDescriptor):
            #bug:if IDescriptor.__subclasshook__ (C):
            if True is IDescriptor.__subclasshook__ (C):
                if not any('__set__' in B.__dict__ or '__delete__' in B.__dict__ for B in C.__mro__):
                    return True
            #return False#bug??missing??
        return NotImplemented

class IDataDescriptor(____1, ____0, IDescriptor):
    '__set__ or __delete__'
    __slots__ = ()

    @abstractmethod
    def __set__(sf, instance, value, /):
        raise AttributeError
    @abstractmethod
    def __delete__(sf, instance, /):
        raise AttributeError
    @classmethod
    @override
    def __subclasshook__(cls, C, /):
        # ABCMeta::__subclasshook__
        if cls is __class__:
            #assert isinstance(C, type)
            #bug:recur:if issubclass(C, IDescriptor):
            #bug:if IDescriptor.__subclasshook__ (C):
            if True is IDescriptor.__subclasshook__ (C):
                if any('__set__' in B.__dict__ or '__delete__' in B.__dict__ for B in C.__mro__):
                    return True
            #return False#bug??missing??
        return NotImplemented
assert issubclass(INonDataDescriptor, IDescriptor)
assert issubclass(IDescriptor, INonDataDescriptor)
assert issubclass(IDataDescriptor, IDescriptor)
assert not issubclass(IDescriptor, IDataDescriptor)
assert not issubclass(INonDataDescriptor, IDataDescriptor)
assert not issubclass(IDataDescriptor, INonDataDescriptor)


assert issubclass(LambdaType, INonDataDescriptor)
assert issubclass(FunctionType, INonDataDescriptor)
assert issubclass(MethodType, INonDataDescriptor)

assert not issubclass(LambdaType, IDataDescriptor)
assert not issubclass(FunctionType, IDataDescriptor)
assert not issubclass(MethodType, IDataDescriptor)

assert not issubclass(BuiltinFunctionType, IDescriptor)
assert not issubclass(BuiltinMethodType, IDescriptor)


class IDescriptor__default_mixin(IDescriptor):
    __slots__ = ()

    @override
    def __set_name__(sf, owner, name, /):
        pass
class INonDataDescriptor__default_mixin(IDescriptor__default_mixin, INonDataDescriptor):
    __slots__ = ()
class IDataDescriptor__default_mixin(IDescriptor__default_mixin, IDataDescriptor):
    __slots__ = ()

    @override
    def __set__(sf, instance, value, /):
        raise AttributeError
    @override
    def __delete__(sf, instance, /):
        raise AttributeError

class IDescriptor__wrap_func(IDescriptor, IWrapper4Func):
    __slots__ = ()

    @property
    @override
    def __isabstractmethod__(sf, /):
        'play with @abc.abstractmethod'
        return bool(getattr(sf.__func__, '__isabstractmethod__', False))


#class NonDataDescriptor4builtin_function_or_method(INonDataDescriptor):
#NonDataDescriptor4builtin_function_or_method = staticmethod
if 1:
    pass
if 0:
    help(WrapperDescriptorType)
    r'''
        no: constructor
        __objclass__
        __text_signature__
    #'''
    help(MethodType)
    r'''
        constructor:method(function, instance)
        __func__
        __self__
    #'''
    help(MethodDescriptorType)
    r'''
        no: constructor
        __objclass__
        __text_signature__
    #'''
    help(MethodWrapperType)
    r'''
        no: constructor
        __objclass__
        __self__
        __text_signature__
    #'''
if 0:
    MethodDescriptorType(repr)
        #TypeError: cannot create 'method_descriptor' instances
    MethodWrapperType(repr, '')
        #TypeError: cannot create 'method-wrapper' instances
    NonDataDescriptor4InstanceMethod = MethodDescriptorType
    assert MethodWrapperType(repr, '') == "''"

r'''
class _IBaseDescriptor4XxxMethod(IDescriptor):
    __slots__ = ('__func',)
    #__slots__ = ('__func',)
    #   since using functools.update_wrapper()
    def __init__(sf, __func__, /):
        sf.__func = __func__
        #update_wrapper(sf, __func__)
            #to work with @abc.abstractmethod(
        super(__class__, type(sf)).__init__(sf)
    @property
    def __func__(sf, /):
        return sf.__func
    @property
    @override
    def __isabstractmethod__(sf, /):
        'play with @abc.abstractmethod'
        return bool(getattr(sf.__func__, '__isabstractmethod__', False))
#'''

class IDescriptor4InstanceMethod(IDescriptor__wrap_func):
    #class IDescriptor4InstanceMethod(_IBaseDescriptor4XxxMethod):
    __slots__ = ()
    @override
    def __get__(sf, may_instance, may_owner=None, /):
        if may_instance is None:
            return sf.__func__
        else:
            instance = may_instance
            return MethodType(sf.__func__, instance)
            return partial(sf.__func__, instance)
            #fail: no_constructor:return MethodWrapperType(sf.__func__, instance)


class IDescriptor4ClassMethod(IDescriptor__wrap_func):
    #class IDescriptor4ClassMethod(_IBaseDescriptor4XxxMethod):
    __slots__ = ()
    @override
    def __get__(sf, may_instance, may_owner=None, /):
        if may_instance is None:
            if may_owner is None: raise TypeError
            owner = may_owner
        else:
            instance = may_instance
            owner = type(instance)
        return MethodType(sf.__func__, owner)
class IDescriptor4StaticMethod(IDescriptor__wrap_func):
    #class IDescriptor4StaticMethod(_IBaseDescriptor4XxxMethod):
    __slots__ = ()
    @override
    def __get__(sf, may_instance, may_owner=None, /):
        return sf.__func__

class IDescriptor4Echo(IDescriptor__wrap_func):
    __slots__ = ()
    @override
    def __get__(sf, may_instance, may_owner=None, /):
        return (sf.__func__, (sf, may_instance, may_owner))
class IDescriptor__using_update_wrapper(IDescriptor__wrap_func, ABC__no_slots):
    #__slots__ = ()
    def __init__(sf, __func__, /):
        _ = update_wrapper(sf, __func__)
        assert _ is sf
        #assert _ is None
        super(__class__, type(sf)).__init__(sf, __func__)
class IDescriptor4Property(IDescriptor__using_update_wrapper):
    #no IDataDescriptor!!!
    #   to allow NonDataDescriptor4Property
    #
    #__slots__ = ()
    #
    @override
    def __get__(sf, may_instance, may_owner=None, /):
        if may_instance is None:
            return sf
            return sf.__func__
        else:
            instance = may_instance
        return sf.__func__(instance)
    r'''
    def __getattribute__(sf, attr, /):
        #_ = functools.update_wrapper(sf, instance2value)
        #assert _ is sf
        #   copy: __doc__, ...
        #
        #bug:__func__ = super().__getattribute__('__func__')
        __func__ = super().__getattribute__('_???__func')
        if attr == '__func__':
            return __func__
        return type(__func__).__getattribute__(attr)
    #'''




class NonDataDescriptor4InstanceMethod(INonDataDescriptor__default_mixin, IDescriptor4InstanceMethod, Wrapper4Func__using_slots):
    r'''
    ~~~-->FunctionType.__get__
    NonDataDescriptor4InstanceMethod vs classmethod vs staticmethod
    why?
        diff:
            user_defined_func :: FunctionType <: INonDataDescriptor
            id/operator.is_not :: BuiltinFunctionType !<: IDescriptor
        ----
        to wrap BuiltinFunctionType as IDescriptor like FunctionType
        ----
        used in seed.abc.eq_by_id.AddrAsHash
        where:
            __hash__ = id
            __eq__ = operator.is_
            __ne__ = operator.is_not
            ==>>
            __hash__ = NonDataDescriptor4InstanceMethod(id)
            __eq__ = NonDataDescriptor4InstanceMethod(operator.is_)
            __ne__ = NonDataDescriptor4InstanceMethod(operator.is_not)
    #'''
    __slots__ = ()
class NonDataDescriptor4ClassMethod(INonDataDescriptor__default_mixin, IDescriptor4ClassMethod, Wrapper4Func__using_slots):
    '~~~classmethod'
    __slots__ = ()
class NonDataDescriptor4StaticMethod(INonDataDescriptor__default_mixin, IDescriptor4StaticMethod, Wrapper4Func__using_slots):
    '~~~staticmethod'
    __slots__ = ()
class NonDataDescriptor4Echo(INonDataDescriptor__default_mixin, IDescriptor4Echo, Wrapper4Func__using_slots):
    __slots__ = ()
class NonDataDescriptor4Property(INonDataDescriptor__default_mixin, IDescriptor4Property, Wrapper4Func__no_slots):
    #__slots__ = ()
    pass




class DataDescriptor4InstanceMethod(IDataDescriptor__default_mixin, IDescriptor4InstanceMethod, Wrapper4Func__using_slots):
    __slots__ = ()
class DataDescriptor4ClassMethod(IDataDescriptor__default_mixin, IDescriptor4ClassMethod, Wrapper4Func__using_slots):
    __slots__ = ()
class DataDescriptor4StaticMethod(IDataDescriptor__default_mixin, IDescriptor4StaticMethod, Wrapper4Func__using_slots):
    __slots__ = ()
class DataDescriptor4Echo(IDataDescriptor__default_mixin, IDescriptor4Echo, Wrapper4Func__using_slots):
    __slots__ = ()
class DataDescriptor4Property(IDataDescriptor__default_mixin, IDescriptor4Property, Wrapper4Func__no_slots):
    '~~~property'
    #__slots__ = ()
    pass
NonDataDescriptor4InstanceMethod(id)
DataDescriptor4InstanceMethod(id)

_Descriptors = (
    (NonDataDescriptor4InstanceMethod
    ,NonDataDescriptor4ClassMethod
    ,NonDataDescriptor4StaticMethod
    ,DataDescriptor4InstanceMethod
    ,DataDescriptor4ClassMethod
    ,DataDescriptor4StaticMethod
    ))

def _test__Descriptors(Descriptors, /):
    Descriptors = (*Descriptors,)
    for Descriptor in Descriptors:
        _test__using_slots(Descriptor)

    for Descriptor in Descriptors:
        nm = Descriptor.__name__
        if not 'DataDescriptor' in nm: raise logic-err
        if 'NonDataDescriptor' in nm:
            _test__NonDataDescriptor(Descriptor)
        else:
            _test__DataDescriptor(Descriptor)
    for Descriptor in Descriptors:
        nm = Descriptor.__name__
        if not nm.endswith('Method'): raise logic-err
        if nm.endswith('DataDescriptor4InstanceMethod'):
            _test__Descriptor4InstanceMethod(Descriptor)
        elif nm.endswith('DataDescriptor4ClassMethod'):
            _test__Descriptor4ClassMethod(Descriptor)
        elif nm.endswith('DataDescriptor4StaticMethod'):
            _test__Descriptor4StaticMethod(Descriptor)
        else:
            raise logic-err
def _test__using_slots(Descriptor, /):
    descriptor = Descriptor(id)
    assert expectError(AttributeError, lambda:setattr(descriptor, 'x', 1))
    try:
        descriptor.x = 1
    except AttributeError as e:
        assert repr(e) == fr'''AttributeError("'{Descriptor.__name__!s}' object has no attribute 'x'")'''

    else:
        raise logic-err
def _test__DataDescriptor(Descriptor, /):
    class C:
        @Descriptor
        def echo(*args):
            return args
    c = C()
    assert expectError(AttributeError, lambda:setattr(c, 'echo', 1))
    c.__dict__['echo'] = ...
    if c.echo is ...: raise logic-err

def _test__NonDataDescriptor(Descriptor, /):
    class C:
        @Descriptor
        def echo(*args):
            return args
    c = C()
    c.echo = ...
    if not c.echo is ...: raise logic-err


def _test__Descriptor4InstanceMethod(Descriptor, /):
    class C:
        @Descriptor
        def echo(*args):
            return args
    c = C()
    if not c.echo() == (c,): raise logic-err
    if not C.echo() == (): raise logic-err
def _test__Descriptor4ClassMethod(Descriptor, /):
    class C:
        @Descriptor
        def echo(*args):
            return args
    c = C()
    if not c.echo() == (C,): raise logic-err
    if not C.echo() == (C,): raise logic-err
def _test__Descriptor4StaticMethod(Descriptor, /):
    class C:
        @Descriptor
        def echo(*args):
            return args
    c = C()
    if not c.echo() == (): raise logic-err
    if not C.echo() == (): raise logic-err

_test__Descriptors(_Descriptors)
r'''
class DataDescriptor4InstanceMethod(_BaseDescriptor4InstanceMethod, IDataDescriptor__default_mixin, IDataDescriptor):
    __slots__ = ()
class DataDescriptor4ClassMethod(classmethod, IDataDescriptor__default_mixin, IDataDescriptor):
    __slots__ = ()
class DataDescriptor4StaticMethod(staticmethod, IDataDescriptor__default_mixin, IDataDescriptor):
    __slots__ = ()
#'''


#NonDataDescriptor4InstanceMethod = MethodType
#NonDataDescriptor4InstanceMethod = MethodDescriptorType
#NonDataDescriptor4InstanceMethod = NonDataDescriptor4InstanceMethod
#NonDataDescriptor4ClassMethod = classmethod
#NonDataDescriptor4StaticMethod = staticmethod

if 1:
    NonDataDescriptor4InstanceMethod(id)
    NonDataDescriptor4ClassMethod(id)
    NonDataDescriptor4StaticMethod(id)
    DataDescriptor4InstanceMethod(id)
    DataDescriptor4ClassMethod(id)
    DataDescriptor4StaticMethod(id)


descriptor4instance_method = NonDataDescriptor4InstanceMethod
descriptor4class_method = NonDataDescriptor4ClassMethod
descriptor4static_method = NonDataDescriptor4StaticMethod
descriptor4echo = NonDataDescriptor4Echo
descriptor4property = NonDataDescriptor4Property

data_descriptor4instance_method = DataDescriptor4InstanceMethod
data_descriptor4class_method = DataDescriptor4ClassMethod
data_descriptor4static_method = DataDescriptor4StaticMethod
data_descriptor4echo = DataDescriptor4Echo
data_descriptor4property = DataDescriptor4Property


IDescriptor
INonDataDescriptor
IDataDescriptor

IDescriptor__default_mixin
IDataDescriptor__default_mixin

IDescriptor4InstanceMethod
IDescriptor4ClassMethod
IDescriptor4StaticMethod
IDescriptor4Echo
IDescriptor__using_update_wrapper
IDescriptor4Property

NonDataDescriptor4InstanceMethod
NonDataDescriptor4ClassMethod
NonDataDescriptor4StaticMethod
NonDataDescriptor4Echo
NonDataDescriptor4Property

DataDescriptor4InstanceMethod
DataDescriptor4ClassMethod
DataDescriptor4StaticMethod
DataDescriptor4Echo
DataDescriptor4Property

descriptor4instance_method
descriptor4class_method
descriptor4static_method
descriptor4echo
descriptor4property

data_descriptor4instance_method
data_descriptor4class_method
data_descriptor4static_method
data_descriptor4echo
data_descriptor4property


#[[[zzzwww:begin
#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):



