
r'''
method not property!!!

>>> ls3 = [1,2,3]
>>> theSpecialMethodCaller.__len__(ls3)
3
>>> theSpecialMethodCaller.__getitem__(ls3, 1)
2
>>> the__SpecialMethodCaller__.len(ls3)
3
>>> the__SpecialMethodCaller__.getitem(ls3, 1)
2

>>> SpecialMethodGetter(ls3).__len__()
3
>>> SpecialMethodGetter(ls3).__getitem__(1)
2
>>> __SpecialMethodGetter__(ls3).len()
3
>>> __SpecialMethodGetter__(ls3).getitem(1)
2

'''

__all__ = '''
    theSpecialMethodCaller
    the__SpecialMethodCaller__
    SpecialMethodGetter
    __SpecialMethodGetter__
    '''.split()


from types import MethodType


class SpecialMethodCaller:
    # final class

    def __getattribute__(_, __attr):
        def f(__obj, *args, **kwargs):
            return getattr(type(__obj), __attr)(__obj, *args, **kwargs)
        f.__name__ = __attr
        return f

    def __hash__(self):
        return id(__class__)
    def __eq__(self, other):
        if type(self) is not __class__: raise TypeError
        return type(other) is __class__

class __SpecialMethodCaller__:
    # final class

    def __getattribute__(_, __attr):
        __attr = f'__{__attr}__'
        def f(__obj, *args, **kwargs):
            return getattr(type(__obj), __attr)(__obj, *args, **kwargs)
        f.__name__ = __attr
        return f

    def __hash__(self):
        return id(__class__)
    def __eq__(self, other):
        if type(self) is not __class__: raise TypeError
        return type(other) is __class__
theSpecialMethodCaller = SpecialMethodCaller()
the__SpecialMethodCaller__ = __SpecialMethodCaller__()

class SpecialMethodGetter:
    __slots__ = ['__self__']
    def __init__(__self, __obj):
        __self.__self__ = __obj
    def __getattribute__(__self, __attr):
        #bug: obj = __self.__self__
        obj = object.__getattribute__(__self, '__self__')
        f = getattr(type(obj), __attr)
        return MethodType(f, obj)

class __SpecialMethodGetter__:
    __slots__ = ['__self__']
    def __init__(__self, __obj):
        __self.__self__ = __obj
    def __getattribute__(__self, __attr):
        obj = object.__getattribute__(__self, '__self__')
        __attr = f'__{__attr}__'

        f = getattr(type(obj), __attr)
        return MethodType(f, obj)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #doctest: +NORMALIZE_WHITESPACE

