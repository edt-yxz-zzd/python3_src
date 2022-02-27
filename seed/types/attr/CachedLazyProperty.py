#################################
#[[[__doc__-begin
r'''
see: @functools.cached_property

seed.types.attr.CachedLazyProperty
py -m seed.types.attr.CachedLazyProperty
py -m nn_ns.app.debug_cmd   seed.types.attr.CachedLazyProperty
from seed.types.attr.CachedLazyProperty import CachedLazyProperty

e ../../python3_src/seed/types/attr/CachedLazyProperty.py
e ../../python3_src/seed/abc/IContextManager.py
e ../../python3_src/seed/abc/IDescriptor.py
from seed.abc.IDescriptor import IDescriptor, IDataDescriptor


#[[[doctest_examples-begin
>>> exc = OSError()
>>> OSError() == OSError()
False
>>> class C:
...     @CachedLazyProperty
...     def vvv(sf, /):
...         'vvv()'
...         print('call vvv()')
...         return 1
...     @CachedLazyProperty
...     def eee(sf, /):
...         'eee()'
...         print('call eee()')
...         raise exc
...         raise OSError
>>> c = C()
>>> c.__dict__
{}
>>> c.vvv
call vvv()
1
>>> c.vvv
1
>>> c.__dict__ == {C.vvv:(True, 1)}
True
>>> c.eee
Traceback (most recent call last):
    ...
OSError
>>> saved_exc = exc; del exc
>>> c.eee
Traceback (most recent call last):
    ...
OSError


>>> c.__dict__ == {C.vvv:(True, 1), C.eee:(False, saved_exc)}
True

>>> help(C) #doctest: +NORMALIZE_WHITESPACE
Help on class C in module __main__:
<BLANKLINE>
class C(builtins.object)
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  eee
 |      eee()
 |
 |  vvv
 |      vvv()
<BLANKLINE>


>>> from seed.abc.abc import ABC__no_slots, abstractmethod
>>> class A(ABC__no_slots):
...     @CachedLazyProperty
...     @abstractmethod
...     def vvv(sf, /):
...         'vvv()'
>>> A()
Traceback (most recent call last):
    ...
TypeError: Can't instantiate abstract class A with abstract methods vvv


#]]]doctest_examples-end
#'''
#]]]__doc__-end

#################################
__all__ = '''
    CachedLazyProperty
    '''.split()
#################################

from seed.abc.IDescriptor import DataDescriptor4Property #IDataDescriptor__default_mixin, IDescriptor__wrap_func, IDescriptor4Property
#from seed.abc.IDescriptor import DataDescriptor4Property
from seed.abc.abc import override, ABC__no_slots
from seed.abc.eq_by_id.AddrAsHash import AddrAsHash as EqById
import functools
from operator import __setitem__
import operator

from seed.tiny import check_type_is, catched_call__either

from seed.tiny import catched_call__either, cached_catched_call__either, get_or_cached_catched_call__either

#e ../../python3_src/seed/types/OpaqueInstanceStorage.py
#e ../../python3_src/seed/abc/storage/IStorage.py
#e ../../python3_src/seed/types/attr/CachedLazyProperty.py

#class CachedLazyProperty(EqById, DataDescriptor4Property, ABC__no_slots):
class CachedLazyProperty(EqById, DataDescriptor4Property):# IDataDescriptor__default_mixin, IDescriptor4Property, ABC__no_slots
    'see: @functools.cached_property'
    __slots__ = ()
    r'''
    #__slots__ = ('_instance2value',)
    def __init__(sf, instance2value, /):
        if not callable(instance2value): raise TypeError
        sf._instance2value = instance2value
        _ = functools.update_wrapper(sf, instance2value)
        #assert _ is None
        assert _ is sf
    #'''
    def ___get_instance_storage4cache___(sf, instance, intend, /):
        if intend is __class__:
            return instance.__dict__
        raise Exception(f'unknown intend: {intend!r}')

    @override
    def __get__(sf, may_instance, may_owner=None, /):
        if may_instance is None:
            return super(__class__, sf).__get__(None, may_owner)
            return sf
            raise AttributeError
        del may_owner
        instance = may_instance
        #d = instance.__dict__
        intend = __class__
        key = sf
        d = type(sf).___get_instance_storage4cache___(sf, instance, intend)
        #may_either = d.get(key)
        fget = lambda:d.get(key)
        calc = lambda:super(__class__, sf).__get__(instance)
        fset = lambda v, /:operator.__setitem__(d, key, v)
        either = get_or_cached_catched_call__either(fget, Exception, calc, fset)

        (is_value, exc_vs_value) = either
        if is_value:
            value = exc_vs_value
            return value
        else:
            exc = exc_vs_value
            raise exc

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):

