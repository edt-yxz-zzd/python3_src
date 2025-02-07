#__all__:goto
# see: types.DynamicClassAttribute
r'''
e ../../python3_src/seed/lang/class_property.py

py -m seed.lang.class_property
from seed.lang.class_property import class_property, static_property

py -m seed.types.attr.class_property
from seed.types.attr.class_property import class_property, static_property

[[
help(types.DynamicClassAttribute)
py_help types:DynamicClassAttribute
===
class DynamicClassAttribute(builtins.object)
 |  DynamicClassAttribute(fget=None, fset=None, fdel=None, doc=None)
 |
 |  Route attribute access on a class to __getattr__.
 |
 |  This is a descriptor, used to define attributes that act differently when
 |  accessed through an instance and through a class.  Instance access remains
 |  normal, but access to an attribute through a class will be routed to the
 |  class's __getattr__ method; this is done by raising AttributeError.
 |
 |  This allows one to have properties active on an instance, and have virtual
 |  attributes on the class with the same name.  (Enum used this between Python
 |  versions 3.4 - 3.9 .)
 |
 |  Subclass from this to use a different method of accessing virtual attributes
 |  and still be treated properly by the inspect module. (Enum uses this since
 |  Python 3.10 .)
 |
 |  Methods defined here:
 |
 |  __delete__(self, instance)
 |
 |  __get__(self, instance, ownerclass=None)
 |
 |  __init__(self, fget=None, fset=None, fdel=None, doc=None)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __set__(self, instance, value)
 |
 |  deleter(self, fdel)
 |
 |  getter(self, fget)
 |
 |  setter(self, fset)
===
]]


[[
usage:
    from seed.types.ABC import ABC, not_implemented

    class C(ABC):
        @class_property
        @not_implemented
        def RED(cls):...

    try:
        C()
        # TypeError: Can't instantiate abstract class C with abstract methods RED
    except TypeError:pass
    else: raise ...

    try:
        C.RED
    except NotImplementedError:pass
    else: raise ...


    class D(C):pass
    try:
        D()
    except TypeError:pass
    else: raise ... # D() success!!
    try:
        D.RED
    except NotImplementedError:pass
    else: raise ...


    class D(C):
        RED = 'RED'
        @class_property
        def RED(cls):
            return 'RED'
    assert D.RED == 'RED'
]]


'''#'''

__all__ = r'''
    class_property
        cached_class_property
            cached_class_property4non_ABC
    static_property

'''.split()#'''


from functools import wraps, cached_property
#from seed.types.ABC import ABC, not_implemented
from seed.meta.ABC import ABC, not_implemented
#from abc import ABC, abstractmethod as not_implemented


def t1():
    class T(ABC):
        @property
        @not_implemented
        def f(self):
            pass
    #print(T.f)
    #print('\n'.join(dir(T.f)))
    try:
        T()
    except TypeError:pass
    else: raise ...

def t2():
    class T(ABC):
        @classmethod
        @not_implemented
        def f(self):
            pass
    #print(T.f)
    #print('\n'.join(dir(T.f)))
    try:
        T()
    except TypeError:pass
    else: raise ...
t1()
t2()


__isabstractmethod__ = '__isabstractmethod__'
class class_property:
    r'''
class C:
    RED = 'RED'
    @class_property
    def RED(cls):
        return 'RED'
'''#'''
    def __init__(self, func):
        self.func = func
        wraps(func)(self)
        assert hasattr(func, __isabstractmethod__) == hasattr(self, __isabstractmethod__)
        self.__isabstractmethod__ = getattr(func, __isabstractmethod__, False)

    def __get__(self, instance_or_None, owner_class):
        # type(instance) is owner_class
        if self.__isabstractmethod__: return self # <<== ABCMeta collect __abstractmethods__
        return self.func(owner_class)
    #def __call__(self): raise NotImplementedError
__0initialized0__ = '__0initialized0__'
class cached_class_property(class_property):
    name = None
    _non_ABC_only_ = False
    @cached_property
    def _required_attrs_(sf, /):
        from seed.for_libs.for_inspect import namess5api
        [[_nm4cls_], nms] = namess5api(sf.func, 1,1,0,0,0)
        return nms #exclude "self|cls" by '/' in "def f(cls, /, ...)"
    #.def __set__(self, instance, value):
    #.    raise AttributeError(self.name)
    def __set_name__(self, owner_class, name):
        self.name = name
        return
        vars(self)['name'] = name
    def __get__(self, instance_or_None, owner_class):
        #if 0b0001:print(self.name)
        #if 0b0001:print(self.name, sorted(vars(owner_class)), owner_class.__qualname__)
        #if 0b0001:return self
        if self.__isabstractmethod__: return self # <<== ABCMeta collect __abstractmethods__
        #if not getattr(owner_class, __0initialized0__, None): return self # <<== not __0initialized0__
        if not vars(owner_class).get(__0initialized0__, False): return self # <<== not __0initialized0__
        name = self.name
        if name is None:
            name = self.func.__name__

        #if not all(hasattr(owner_class, nm) for nm in self._required_attrs_):raise AttributeError(name)
        args = [getattr(owner_class, nm) for nm in self._required_attrs_]
            # ^AttributeError
            # fail: get abstractmethod
            #   cannot predicate whether the class initialized: ABC has not yet set ".__abstractmethods__"
        if self._non_ABC_only_ and (nms:=getattr(owner_class, '__abstractmethods__', None)):
            raise TypeError('ABC:', owner_class, name, nms)
        v = self.func(owner_class, *args)
        setattr(owner_class, name, v)
        _v = getattr(owner_class, name)
        assert _v is v
        return v
class cached_class_property4non_ABC(cached_class_property):
    _non_ABC_only_ = True

class static_property:
    r'''
class C:
    RED = 'RED'
    @static_property
    def RED():
        return 'RED'
'''#'''
    def __init__(self, func):
        self.func = func
        wraps(func)(self)
        assert hasattr(func, __isabstractmethod__) == hasattr(self, __isabstractmethod__)
        self.__isabstractmethod__ = getattr(func, __isabstractmethod__, False)
    def __get__(self, instance_or_None, owner_class):
        # type(instance) is owner_class
        if self.__isabstractmethod__: return self
        return self.func()
    #def __call__(self): raise NotImplementedError

def _test():
    #from seed.types.ABC import ABC, not_implemented


    class C(ABC):
        @static_property
        @not_implemented
        def RED():
            return 'RED'

    try:
        C()
        # TypeError: Can't instantiate abstract class C with abstract methods RED
    except TypeError:pass
    else:raise ...

    if 0:
        # skip this test
        try:
            C.RED
            # NotImplementedError
        except NotImplementedError:pass
        else: raise ...

    class D(C):pass
    try:
        D()
    except TypeError:pass
    else: raise ... # D() success!!

    if 0:
        # skip this test
        try:
            D.RED
        except NotImplementedError:pass
        else: raise ...


    class D(C):
        RED = 'RED'
        @static_property
        def RED():
            return 'RED'
    assert D.RED == 'RED'



_test()


def _test2():
    #from seed.types.ABC import ABC, not_implemented

    class C(ABC):
        @class_property
        @not_implemented
        def RED(cls):...

    try:
        C()
        # TypeError: Can't instantiate abstract class C with abstract methods RED
    except TypeError:pass
    else: raise ...

    if 0:
        # skip this test
        try:
            C.RED
        except NotImplementedError:pass
        else: raise ...


    class D(C):pass
    try:
        D()
    except TypeError:pass
    else: raise ... # D() success!!

    if 0:
        # skip this test
        try:
            D.RED
        except NotImplementedError:pass
        else: raise ...


    class D(C):
        RED = 'RED'
        @class_property
        def RED(cls):
            return 'RED'
    assert D.RED == 'RED'


_test2()


def _test3():
    class B(ABC):
        i = 0
        @cached_class_property
        def j(cls, /):
            cls.i += 1
            return cls.i
    assert type(B.j) is cached_class_property
    B.__0initialized0__ = True
    assert B.i == 0

    assert B.j == 1
    assert B.i == 1
    assert not type(B.j) is cached_class_property
    assert type(B.j) is int

    assert B.j == 1
    assert B.i == 1



def _test4():
    class A(ABC):
        i = 0
        @cached_class_property4non_ABC
        def j(cls, /):
            cls.i += 1
            return cls.i
        #@abstractmethod
        @not_implemented
        def g():0
    assert type(A.j) is cached_class_property4non_ABC
    A.__0initialized0__ = True
    try:
        A.j
    except TypeError:pass
    else: raise ... # A.j success!!

    class C(A):
        pass
    assert type(C.j) is cached_class_property4non_ABC
    C.__0initialized0__ = True
    try:
        C.j
    except TypeError:pass
    else: raise ... # C.j success!!

    class B(A):
        g = 0
    assert type(B.j) is cached_class_property4non_ABC
    B.__0initialized0__ = True

    assert B.i == 0

    assert B.j == 1
    assert B.i == 1

    assert B.j == 1
    assert B.i == 1

    class D:#(ABC):
        #no .__abstractmethods__
        i = 0
        @cached_class_property4non_ABC
        def j(cls, /):
            cls.i += 1
            return cls.i
    assert type(D.j) is cached_class_property4non_ABC
    D.__0initialized0__ = True

    assert D.i == 0

    assert D.j == 1
    assert D.i == 1

    assert D.j == 1
    assert D.i == 1

if 0b0001:
    _test3()
    _test4()








from seed.lang.class_property import class_property, static_property
from seed.lang.class_property import __0initialized0__, cached_class_property, cached_class_property4non_ABC, static_property, class_property
from seed.lang.class_property import *
