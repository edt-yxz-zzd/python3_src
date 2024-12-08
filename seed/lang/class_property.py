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
    static_property
'''.split()#'''


from functools import wraps
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
        if self.__isabstractmethod__: return self
        return self.func(owner_class)
    #def __call__(self): raise NotImplementedError

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










from seed.lang.class_property import class_property, static_property
from seed.lang.class_property import *
