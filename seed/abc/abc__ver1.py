
'''
std abc.ABC has no "__slots__ = ()"


py -m seed.abc.abc__ver1
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.abc.abc__ver1 import override, def_new_method, overridable_default_method, collaboration_method_chain, final_method
from seed.abc.abc__ver1 import verify_slots_setting, check_slots_setting, Base4check_slots_setting, MetaMeta4check_slots_setting, Meta4check_slots_setting, ABCMeta4check_slots_setting, ABC4check_slots_setting, ABC4check_slots_setting__no_slots


py -m seed.abc.abc
from seed.abc.abc import abstractmethod, override, ABC, ABC__no_slots
from seed.abc.abc import override, def_new_method, overridable_default_method, collaboration_method_chain, final_method
    view python3_src/my_convention/overridable_method__to_auto_generate_wrapper_class_forward_call_src_code.txt
'''



__all__ = '''
    ABCMeta
    ABC
    ABC__no_slots
    not_implemented
    override
    define
    final
    abstractmethod

    def_new_method
    overridable_default_method
    collaboration_method_chain
    final_method


    verify_slots_setting
    check_slots_setting
    Base4check_slots_setting
    MetaMeta4check_slots_setting
    Meta4check_slots_setting
    ABCMeta4check_slots_setting
    ABC4check_slots_setting
    ABC4check_slots_setting__no_slots
    '''.split()

from abc import ABC as __error_ABC, abstractmethod, ABCMeta as _ABCMeta
from seed.debug.expectError import expectError

def verify_slots_setting(cls, /):
    return ('__slots__' in cls.__dict__ or any(B.__dict__.get('___no_slots_ok___', False) or '__dict__' in B.__dict__.get('__slots__', ()) for B in cls.__mro__))
def check_slots_setting(cls, /):
    r'''
    to remove slots by: __slots__ = ('__dict__',)
    #'''
    if not verify_slots_setting(cls): raise TypeError


class Base4check_slots_setting:
    __slots__ = ()
    ___no_slots_ok___ = False
    def __init_subclass__(cls, /, *args, **kwargs):
        #print(f'Base4check_slots_setting-__init_subclass__-check_slots_setting<{cls!r}>')
        #__init_subclass__(__class__, cls, *args, **kwargs)
#def __init_subclass__(__class__, cls, /, *args, **kwargs):
        assert '__slots__' in __class__.__dict__
        check_slots_setting(cls)
        #   cls.__dict__.setdefault('__slots__', ('__dict__',))
        #       AttributeError: 'mappingproxy' object has no attribute 'setdefault'
        #if '__slots__' not in cls.__dict__:
        if '___no_slots_ok___' not in cls.__dict__ and '__slots__' not in cls.__dict__:
            try:
                #cls.__slots__ = ('__dict__',)
                cls.___no_slots_ok___ = True
            except AttributeError:
                #meta may not allow setattr
                pass
        super(__class__, cls).__init_subclass__(*args, **kwargs)


class MetaMeta4check_slots_setting(Base4check_slots_setting, type):
    __slots__ = ()
    def __call__(meta, /, *args, **kwargs):
        assert issubclass(meta, type)
        metameta = type(meta)
        assert issubclass(metameta, __class__)
        cls = super(__class__, type(meta)).__call__(meta, *args, **kwargs)
        if not isinstance(cls, type): raise TypeError
        if type(cls) is meta:
            #print(f'MetaMeta4check_slots_setting-__call__-check_slots_setting<{cls!r}>')
            check_slots_setting(cls)
        return cls

class Meta4check_slots_setting(Base4check_slots_setting, metaclass=MetaMeta4check_slots_setting):
    __slots__ = ()
class ABCMeta4check_slots_setting(_ABCMeta, Meta4check_slots_setting, metaclass=MetaMeta4check_slots_setting):
    __slots__ = ()

class ABC4check_slots_setting(Base4check_slots_setting, metaclass=ABCMeta4check_slots_setting):
    __slots__ = ()

#print('ABC__no_slots')
class ABC4check_slots_setting__no_slots(ABC4check_slots_setting):
    #__slots__ = ('__dict__',)
    ___no_slots_ok___ = True

class _(ABC4check_slots_setting__no_slots):pass
assert _.___no_slots_ok___
def _t():
    class _(ABC4check_slots_setting):pass
#_t()
assert expectError(TypeError, _t)


ABCMeta = ABCMeta4check_slots_setting
ABC = ABC4check_slots_setting
ABC__no_slots = ABC4check_slots_setting__no_slots


def override(f):
    return f
def define(f):
    return f
def final(f):
    return f

def final_method(f):
    return f
def overridable_default_method(f):
    return f
def collaboration_method_chain(f):
    return f
def def_new_method(f):
    return f

abstractmethod = abstractmethod
not_implemented = abstractmethod
    # diff:
    #   abstractmethod may offer default impl
    #   but not_implemented should not





