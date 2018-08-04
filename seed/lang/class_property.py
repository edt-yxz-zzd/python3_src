
# see: types.DynamicClassAttribute
'''
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

'''

__all__ = '''
    class_property
    static_property
'''.split()


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
    '''
class C:
    RED = 'RED'
    @class_property
    def RED(cls):
        return 'RED'
'''
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
    '''
class C:
    RED = 'RED'
    @static_property
    def RED():
        return 'RED'
'''
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











