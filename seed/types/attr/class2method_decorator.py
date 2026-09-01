#__all__:goto
r'''[[[
e ../../python3_src/seed/types/attr/class2method_decorator.py

seed.types.attr.class2method_decorator
py -m nn_ns.app.debug_cmd   seed.types.attr.class2method_decorator -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.attr.class2method_decorator:__doc__ -ht # -ff -df
#######

[[
usage:
class C:pass
@mk_instance_method_decorator_(C)
def f(sf, /, *args, **kwds):pass
@mk_class_method_decorator_(C)
def g(cls, /, *args, **kwds):pass
@mk_static_method_decorator_(C)
def h(*args, **kwds):pass

]]



'#'; __doc__ = r'#'
>>> class C:pass

>>> @mk_instance_method_decorator_(C)
... def f(sf, /):return sf
>>> @mk_class_method_decorator_(C)
... def g(cls, /):return cls
>>> @mk_static_method_decorator_(C)
... def h():pass


>>> @mk_instance_method_decorator_(C, name='fff')
... def f(sf, /):return sf
>>> @mk_class_method_decorator_(C, name='ggg')
... def g(cls, /):return cls
>>> @mk_static_method_decorator_(C, name='hhh')
... def h():pass

>>> v = C()

>>> v.f() is v
True
>>> v.g() is C
True
>>> v.h() is None
True


>>> v.fff() is v
True
>>> v.ggg() is C
True
>>> v.hhh() is None
True


py_adhoc_call   seed.types.attr.class2method_decorator   @f
]]]'''#'''
__all__ = r'''
MethodDecoratorBase
    mk_instance_method_decorator_
    mk_class_method_decorator_
    mk_static_method_decorator_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_type_le, check_callable, check_all_
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

staticmethod
classmethod
#instancemethod
class MethodDecoratorBase:
    def __init__(sf, name, klass, /, *decorators):
        check_type_is(str, name)
        check_type_le(type, klass)
        check_all_(check_callable, decorators)
        sf._nm = name
        sf._c = klass
        sf._fs = decorators
    def _decorate_(sf, func, /):
        decorators = sf._fs
        x = func
        for decorator in decorators:
            x = decorator(x)
        x
        return x
    def __call__(sf, func, /):
        check_callable(func)
        klass = sf._c
        nm = func.__name__ if not sf._nm else sf._nm
        mthd = sf._decorate_(func)
        setattr(klass, nm, mthd)
        return func
        return mthd

def mk_instance_method_decorator_(klass, /, *, name=''):
    return MethodDecoratorBase(name, klass)
def mk_class_method_decorator_(klass, /, *, name=''):
    return MethodDecoratorBase(name, klass, classmethod)
def mk_static_method_decorator_(klass, /, *, name=''):
    return MethodDecoratorBase(name, klass, staticmethod)


__all__
from seed.types.attr.class2method_decorator import MethodDecoratorBase, mk_instance_method_decorator_, mk_class_method_decorator_, mk_static_method_decorator_
#def mk_instance_method_decorator_(klass, /, *, name=''):
from seed.types.attr.class2method_decorator import *
