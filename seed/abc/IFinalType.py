#HHHHH
r'''

py -m seed.abc.IFinalType
from seed.abc.IFinalType import is_final_type, BaseFinalType, FinalTypeFalse, FinalType, FinalTypeNotFalse

why not named IFinalType?
    this class is abstract
    but the abstractmethod will remove auto for subclass
    hence FinalType is not named "IFinalType"

#HHH
##############begin##########
>>> BaseFinalType() #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
TypeError: Can't instantiate abstract class ...

#to pair above'

>>> FinalTypeFalse() #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
TypeError: Can't instantiate abstract class ...

#to pair above'

>>> FinalType() #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
TypeError: Can't instantiate abstract class ...

#to pair above'

>>> FinalTypeNotFalse() #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
TypeError: Can't instantiate abstract class ...

#to pair above'


#HHH
#################BaseFinalType#############
>>> inspect.isabstract(BaseFinalType)
True
>>> class C(BaseFinalType):pass
...
Traceback (most recent call last):
    ...
TypeError: __init_subclass__() missing 1 required keyword-only argument: 'final'

>>> class C(BaseFinalType, final=False):pass
...

>>> is_final_type(C)
False
>>> inspect.isabstract(C)
False
>>> class X(C):pass
...
Traceback (most recent call last):
    ...
TypeError: __init_subclass__() missing 1 required keyword-only argument: 'final'
>>> class X(C, final=False):pass
...
>>> is_final_type(X)
False
>>> inspect.isabstract(C)
False
>>> class X(C, final=True):pass
...
>>> is_final_type(X)
True
>>> inspect.isabstract(C)
False

>>> class C(BaseFinalType, final=True):pass
...

>>> is_final_type(C)
True
>>> inspect.isabstract(C)
False
>>> class X(C):pass
...
Traceback (most recent call last):
    ...
TypeError: __init_subclass__() missing 1 required keyword-only argument: 'final'
>>> class X(C, final=True):pass
...
Traceback (most recent call last):
    ...
TypeError: inherit final class: <class '__main__.X'> <: <class '__main__.C'>
>>> class X(C, final=False):pass
...
Traceback (most recent call last):
    ...
TypeError: inherit final class: <class '__main__.X'> <: <class '__main__.C'>





#HHH
#################FinalTypeFalse#############
>>> inspect.isabstract(FinalTypeFalse)
True
>>> class C(FinalTypeFalse):pass
...
>>> is_final_type(C)
False
>>> inspect.isabstract(C)
False
>>> class X(C):pass
...
>>> is_final_type(X)
False
>>> inspect.isabstract(C)
False
>>> class X(C, final=False):pass
...
>>> is_final_type(X)
False
>>> inspect.isabstract(C)
False
>>> class X(C, final=True):pass
...
>>> is_final_type(X)
True
>>> inspect.isabstract(C)
False


>>> class C(FinalTypeFalse, final=False):pass
...
>>> is_final_type(C)
False
>>> inspect.isabstract(C)
False
>>> class X(C):pass
...
>>> is_final_type(X)
False
>>> inspect.isabstract(C)
False
>>> class X(C, final=False):pass
...
>>> is_final_type(X)
False
>>> inspect.isabstract(C)
False
>>> class X(C, final=True):pass
...
>>> is_final_type(X)
True
>>> inspect.isabstract(C)
False

>>> class C(FinalTypeFalse, final=True):pass
...
>>> is_final_type(C)
True
>>> inspect.isabstract(C)
False
>>> class X(C):pass
...
Traceback (most recent call last):
    ...
TypeError: inherit final class: <class '__main__.X'> <: <class '__main__.C'>
>>> class X(C, final=False):pass
...
Traceback (most recent call last):
    ...
TypeError: inherit final class: <class '__main__.X'> <: <class '__main__.C'>
>>> class X(C, final=True):pass
...
Traceback (most recent call last):
    ...
TypeError: inherit final class: <class '__main__.X'> <: <class '__main__.C'>


#HHH
#################FinalType#############
>>> inspect.isabstract(FinalType)
True
>>> class C(FinalType):pass
...
>>> is_final_type(C)
True
>>> inspect.isabstract(C)
False
>>> class C(FinalType, final=False):pass
...
>>> is_final_type(C)
False
>>> inspect.isabstract(C)
False
>>> class C(FinalType, final=True):pass
...
>>> is_final_type(C)
True
>>> inspect.isabstract(C)
False


>>> class C(FinalType):
...     @abstractmethod
...     def f(sf):pass
...
>>> is_final_type(C)
False
>>> inspect.isabstract(C)
True
>>> class C(FinalType, final=False):
...     @abstractmethod
...     def f(sf):pass
...
>>> is_final_type(C)
False
>>> inspect.isabstract(C)
True
>>> class C(FinalType, final=True):
...     @abstractmethod
...     def f(sf):pass
...
>>> is_final_type(C)
True
>>> inspect.isabstract(C)
True





#HHH
##############FinalTypeNotFalse##########
>>> inspect.isabstract(FinalTypeNotFalse)
True
>>> class C(FinalTypeNotFalse):pass
...
>>> is_final_type(C)
True
>>> inspect.isabstract(C)
False
>>> class C(FinalTypeNotFalse, final=False):pass
...
Traceback (most recent call last):
    ...
TypeError: not (final is None or final is True): final=False

>>> class C(FinalTypeNotFalse, final=True):pass
...
>>> is_final_type(C)
True
>>> inspect.isabstract(C)
False


>>> class C(FinalTypeNotFalse):
...     @abstractmethod
...     def f(sf):pass
...
>>> is_final_type(C)
False
>>> inspect.isabstract(C)
True
>>> class C(FinalTypeNotFalse, final=False):
...     @abstractmethod
...     def f(sf):pass
...
Traceback (most recent call last):
    ...
TypeError: not (final is None or final is True): final=False

>>> class C(FinalTypeNotFalse, final=True):
...     @abstractmethod
...     def f(sf):pass
...
>>> is_final_type(C)
True
>>> inspect.isabstract(C)
True


#HHH
##############end##########




#'''

#HHHHH

__all__ = '''
    is_final_type
    BaseFinalType
        FinalTypeFalse
        FinalType
            FinalTypeNotFalse
    '''.split()


#from seed.lang.class_property import class_property
from seed.abc.abc import ABC, abstractmethod, override
import inspect


def _find_one_final_ancestpr(cls):
    if not is_final_type(cls): raise TypeError(f'not is_final_type({cls!r})')
    for t in type.mro(cls)[1:]:
        if is_final_type(t):
            return t
    raise Exception("logic-err: {cls!r} is_final_type, but has no final_ancestpr")
def is_final_type(cls):
    return issubclass(cls, BaseFinalType) and cls._BaseFinalType__final

#HHHHH
class BaseFinalType(ABC):
    __slots__ = ()
    __final = False
        #_BaseFinalType__final: is_final_type
    @abstractmethod
    def __mk_this_class_abstract_only(sf):
        pass
    def __init_subclass__(cls, /, *, final:bool, **kwargs):
        if cls.__mk_this_class_abstract_only is not None:
            cls.__mk_this_class_abstract_only = None
        if type(final) is not bool: raise TypeError(f'keyword "final" is not bool: {type(final)!r}')
        if is_final_type(cls): raise TypeError(f'inherit final class: {cls!r} <: {_find_one_final_ancestpr(cls)!r}')
        if final:
            cls.__final = True
        super().__init_subclass__(**kwargs)


#HHHHH
class FinalTypeFalse(BaseFinalType, final=False):
    'turn off keyword "final"'
    __slots__ = ()
    @abstractmethod
    def __mk_this_class_abstract_only(sf):
        pass
    def __init_subclass__(cls, /, *, final:bool=False, **kwargs):
        if cls.__mk_this_class_abstract_only is not None:
            cls.__mk_this_class_abstract_only = None
        super().__init_subclass__(final=final, **kwargs)
#HHHHH
class FinalType(BaseFinalType, final=False):
    r'''
why not named IFinalType?
    this class is abstract
    but the abstractmethod will remove auto for subclass
    hence FinalType is not named "IFinalType"
    #'''
    __slots__ = ()

    @abstractmethod
    def __mk_this_class_abstract_only(sf):
        pass
    def __init_subclass__(cls, /, *, final:'None|bool'=None, **kwargs):
        if cls.__mk_this_class_abstract_only is not None:
            cls.__mk_this_class_abstract_only = None
        if final is None:
            final = not inspect.isabstract(cls)
        super().__init_subclass__(final=final, **kwargs)

#HHHHH

class FinalTypeNotFalse(FinalType):
    'forbid turn off keyword "final"'
    __slots__ = ()

    @abstractmethod
    def __mk_this_class_abstract_only(sf):
        pass
    def __init_subclass__(cls, /, *, final:'None|True'=None, **kwargs):
        if cls.__mk_this_class_abstract_only is not None:
            cls.__mk_this_class_abstract_only = None
        if not (final is None or final is True):raise TypeError(f'not (final is None or final is True): final={final!r}')

        if 1:
            super().__init_subclass__(final=final, **kwargs)

        if not (inspect.isabstract(cls) or is_final_type(cls)):raise Exception(f'logic-err: not (inspect.isabstract(cls) or is_final_type(cls)): cls={cls!r})')

#HHHHH





if __name__ == "__main__":
    import doctest
    doctest.testmod()

#HHHHH
