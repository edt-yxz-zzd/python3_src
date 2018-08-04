

'''
    .__isabstractmethod__
cls.__abstractmethods__ :: frozenset<name>
'''



__all__ = '''
    AND_OR_NOT_Meta
    AND_OR_NOT_Object

    AND
    OR
    NOT_OR
    Just_And

    AND_OR_NOT_T
    AND_OR_NOT_Just_T
    is_AND_OR_NOT
    bool_AND_OR_NOT_obj

    __require_AND_OR_NOT_methods__
    __require_AND_OR_NOT_bases__

    '''.split()
from abc import ABCMeta, abstractmethod, ABC
#from collections import ChainMap

class AND(tuple):pass
class OR(tuple):pass
class NOT_OR(tuple):pass
class Just_And(tuple):pass
AND_OR_NOT_T = (AND, OR, NOT_OR)
AND_OR_NOT_Just_T = (AND, OR, NOT_OR, Just_And)
def is_AND_OR_NOT(f, obj):
    if type(obj) in AND_OR_NOT_T:
        return all(is_AND_OR_NOT0(f, x) for x in obj)
    return False
def is_AND_OR_NOT(f, obj):
    def this_func(obj):
        if type(obj) in AND_OR_NOT_T:
            return all(map(this_func, obj))
        return type(obj) is Just_And and all(map(f, obj))
    return this_func(obj)
def is_type(cls):
    return isinstance(cls, type)
def bool_AND_OR_NOT_obj(f, AND_OR_NOT_obj):
    # AND_OR_NOT_obj :: AND_OR_NOT<T>
    # f :: T -> Bool

    def this_func(AND_OR_NOT_obj):
        T = type(AND_OR_NOT_obj)
        if T is AND:
            return all(map(this_func, AND_OR_NOT_obj))
        elif T is OR:
            return any(map(this_func, AND_OR_NOT_obj))
        elif T is NOT_OR:
            return not any(map(this_func, AND_OR_NOT_obj))
        elif T is Just_And:
            return all(map(f, AND_OR_NOT_obj))
        raise TypeError
    return this_func(AND_OR_NOT_obj)

def does_cls_st_AND_OR_NOT_bases(cls, AND_OR_NOT_bases):
    # assert is_AND_OR_NOT(is_type, AND_OR_NOT_bases)
    mro = cls.mro()
    mro = frozenset(mro)
    return bool_AND_OR_NOT_obj(mro.__contains__, AND_OR_NOT_bases)
def does_cls_st_AND_OR_NOT_methods(cls, AND_OR_NOT_methods):
    # assert is_AND_OR_NOT(callable, AND_OR_NOT_methods)
    mro = cls.mro()
    it = filter(None, (cls.__dict__ for cls in mro))
    # d = ChainMap(*it)
    d = {}
    for _ in map(d.update, it):pass
    return bool_AND_OR_NOT_obj(d.__contains__, AND_OR_NOT_methods)

_attr = '@AND_OR_NOT_Meta@'
__require_AND_OR_NOT_methods__ = '__require_AND_OR_NOT_methods__'
__require_AND_OR_NOT_bases__ = '__require_AND_OR_NOT_bases__'
class AND_OR_NOT_Meta(ABCMeta):
    # AND_OR_NOT<T> = (AND|OR|NOT_OR)<AND_OR_NOT<T>> | Just_And<T>
    # __require_AND_OR_NOT_bases__ :: AND_OR_NOT<type>
    # __require_AND_OR_NOT_methods__ :: AND_OR_NOT<Callable>
    def __new__(meta_cls, name, bases, namespace, **kwargs):
        self = super(__class__, meta_cls).__new__(meta_cls, name, bases, namespace, **kwargs)
        AND_OR_NOT_bases = self.collect_AND_OR_NOT_bases()
        AND_OR_NOT_methods = self.collect_AND_OR_NOT_methods()
        if (does_cls_st_AND_OR_NOT_bases(self, AND_OR_NOT_bases)
            and does_cls_st_AND_OR_NOT_methods(self, AND_OR_NOT_methods)):
            pass
        else:
            s = getattr(self, '__abstractmethods__', ())
            s = set(s)
            s.add(_attr)
            self.__abstractmethods__ = frozenset(s)
        return self

    def collect_AND_OR_NOT_methods(self):
        _attr = __require_AND_OR_NOT_methods__
        return self.collect_AND_OR_NOT_objs(_attr)
    def collect_AND_OR_NOT_bases(self):
        _attr = __require_AND_OR_NOT_bases__
        return self.collect_AND_OR_NOT_objs(_attr)
    def collect_AND_OR_NOT_objs(self, attr):
        mro = self.mro()
        nothing = []
        objs = []
        for cls in mro:
            obj = cls.__dict__.get(attr, nothing)
            if obj is not nothing:
                if type(obj) not in AND_OR_NOT_Just_T: raise TypeError
                objs.append(obj)
        return AND(objs)


class AND_OR_NOT_Object(metaclass=AND_OR_NOT_Meta):pass


def _test():
    AND_OR_NOT_Object()
    class A(AND_OR_NOT_Object):
        __require_AND_OR_NOT_methods__ = Just_And(['f'])
    try:
        A()
        #TypeError: Can't instantiate abstract class A with abstract methods @AND_OR_NOT_Meta@
    except TypeError:pass
    else:raise logic-error
    class B(A):
        def f(self):pass
    B()
    class C(AND_OR_NOT_Object):
        __require_AND_OR_NOT_bases__ = Just_And([tuple])
    class D(C, tuple):pass
    try:
        C()
    except TypeError:pass
    else:raise logic-error
    D()

if __name__ == "__main__":
    _test()
    print('\n'.join(globals()))

