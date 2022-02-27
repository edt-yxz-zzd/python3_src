#HHHHH
r"""
py -m seed.abc.ISingleton
from seed.abc.ISingleton import ISingleton


>>> ISingleton() #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
TypeError: Can't instantiate abstract class ...

#to pair above'

>>> inspect.isabstract(ISingleton)
True
>>> is_final_type(ISingleton)
False

>>> class C(ISingleton):pass
>>> inspect.isabstract(C)
False
>>> is_final_type(C)
True
>>> class C(ISingleton, final=None):pass
>>> inspect.isabstract(C)
False
>>> is_final_type(C)
True
>>> class C(ISingleton, final=False):pass
Traceback (most recent call last):
    ...
TypeError: not (final is None or final is True): final=False
>>> class C(ISingleton, final=True):pass
>>> inspect.isabstract(C)
False
>>> is_final_type(C)
True

>>> class C(ISingleton):
...     @abstractmethod
...     def f(sf):pass
...
>>> is_final_type(C)
False
>>> inspect.isabstract(C)
True
>>> class C(ISingleton, final=None):
...     @abstractmethod
...     def f(sf):pass
...
>>> is_final_type(C)
False
>>> inspect.isabstract(C)
True
>>> class C(ISingleton, final=False):
...     @abstractmethod
...     def f(sf):pass
...
Traceback (most recent call last):
    ...
TypeError: not (final is None or final is True): final=False

#weird case: final abc!!
>>> class C(ISingleton, final=True):
...     @abstractmethod
...     def f(sf):pass
...
>>> is_final_type(C)
True
>>> inspect.isabstract(C)
True










>>> class C(ISingleton):
...     def __new__(sf):pass
...
Traceback (most recent call last):
    ...
TypeError: __new__ been overrided: <class '__main__.C'>
>>> class C(ISingleton):
...     def __init__(sf):pass
...
Traceback (most recent call last):
    ...
TypeError: __init__ been overrided: <class '__main__.C'>










>>> class C(ISingleton):pass
>>> i = id(C()) #WeakKeyDictionary vs WeakValueDictionary
>>> a = C()

#bug: >>> id(a) is i
>>> id(a) == i
True
>>> C() is a
True
>>> C() is C()
True


#"""
#HHHHH

__all__ = '''
    ISingleton
    '''.split()

from seed.abc.IFinalType import is_final_type, BaseFinalType, FinalTypeFalse, FinalType, FinalTypeNotFalse

from seed.abc.abc import ABC, abstractmethod, override
from seed.abc.IReprImmutableHelper import IReprImmutableHelper
import inspect

from weakref import WeakKeyDictionary
#import operator
from seed.abc.eq_by_id.BaseAddrAsHash import BaseAddrAsHash
from seed.abc.eq_by_id.AddrAsHash import AddrAsHash



#HHHHH

class ISingleton(AddrAsHash, FinalTypeNotFalse, IReprImmutableHelper):
#class ISingleton(BaseAddrAsHash, FinalTypeNotFalse, IReprImmutableHelper):
    __slots__ = ()
    def ___init___(sf):
        'donot override __init__'
        super().__init__()

    @override
    def ___get_args_kwargs___(sf):
        return [], {}
        #for repr()

    r'''
    def __eq__(sf, ot):
        return sf is ot
    def __hash__(sf):
        return id(sf)
    __eq__ = operator.is_
    __ne__ = operator.is_not
    __hash__ = id
    now use BaseAddrAsHash
    #'''

    __cache = WeakKeyDictionary()
    r'''
        why not __cache = WeakValueDictionary()?
            cls2sf
            since only one per cls
                if cls exists, WeakKeyDictionary ==>> atmost O(1) spaces
            WeakValueDictionary ==>> observed diff id()
    #'''
    def __new__(cls, /):
        d = __class__.__cache
        m = d.get(cls)
        if m is not None:
            sf = m
        else:
            sf = super().__new__(cls)
            d[cls] = sf
            cls() # test for repr()
            if sf is not cls():raise Exception('logic-err')
        return sf
    __new = __new__

    def __init__(sf, /):
        while 1:
            cls = type(sf)
            d = __class__.__cache
            m = d.get(cls)
            if m is None:
                break
            else:
                cached_sf = m
                if sf is not cached_sf:
                    break
            cls.___init___(sf)
            return

        raise Exception(f'logic-err: call __new__ passby ISingleton.__new__: super().__new__(cls): {cls!r}')
    __init = __init__


    @abstractmethod
    def __mk_this_class_abstract_only(sf):
        pass
    def __init_subclass__(cls, /, **kwargs):
        if cls.__mk_this_class_abstract_only is not None:
            cls.__mk_this_class_abstract_only = None
        if cls.__new__ is not __class__.__new: raise TypeError(f'__new__ been overrided: {cls!r}')
        if cls.__init__ is not __class__.__init: raise TypeError(f'__init__ been overrided: {cls!r}')

        if 1:
            super().__init_subclass__(**kwargs)

        if not (inspect.isabstract(cls) or is_final_type(cls)):raise TypeError(f'not (inspect.isabstract(cls) or is_final_type(cls): {cls!r})')



#HHHHH
if __name__ == "__main__":
    import doctest
    doctest.testmod()



