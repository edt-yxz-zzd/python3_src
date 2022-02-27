
'''
std abc.ABC has no "__slots__ = ()"

py -m seed.abc.abc__ver2
from seed.abc.abc__ver2 import abstractmethod, override, ABC, ABC__no_slots
from seed.abc.abc__ver2 import override, def_new_method, overridable_default_method, collaboration_method_chain, final_method


py -m seed.abc.abc
from seed.abc.abc import abstractmethod, override, ABC, ABC__no_slots
from seed.abc.abc import override, def_new_method, overridable_default_method, collaboration_method_chain, final_method
    view python3_src/my_convention/overridable_method__to_auto_generate_wrapper_class_forward_call_src_code.txt
'''



__all__ = '''
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
    '''.split()

#from abc import ABC as __error_ABC, abstractmethod, ABCMeta as _ABCMeta
from seed.debug.expectError import expectError
import inspect #.isabstract
from seed.abc.abc__ver1 import verify_slots_setting, check_slots_setting, Base4check_slots_setting, MetaMeta4check_slots_setting, Meta4check_slots_setting, ABCMeta4check_slots_setting, ABC4check_slots_setting, ABC4check_slots_setting__no_slots
from abc import abstractmethod


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





def _t_impl_of_ABCMeta():
    class C(__error_ABC):
        @abstractmethod
        def f(sf, /):pass
    assert inspect.isabstract(C)
    assert {'f'} == getattr(C, '__abstractmethods__', ())
    assert True is getattr(C.__dict__['f'], '__isabstractmethod__', False)
    assert expectError(TypeError, C)
    del C.__abstractmethods__
    assert not expectError(TypeError, C)
    C()
    assert inspect.isabstract(C)
        #!!!!!!!!!!!!!!!!!!!!!!
        #!!!!!!!!!!!!!!!!!!!!!!
        #!!!!!!!!!!!!!!!!!!!!!!
        #!!!!!!!!!!!!!!!!!!!!!!
        #!!!!!!!!!!!!!!!!!!!!!!
_t_impl_of_ABCMeta()


def collect_reasons_to_be_ABC(cls, /):
    meta = type(cls)
    reasons = frozenset(meta.___iter_reasons_to_be_ABC___(cls))
    return reasons
class IMeta4check_ABC(type, ABC):
    __slots__ = ()
    @abstractmethod
    def ___iter_reasons_to_be_ABC___(cls, /):
        'collect_reasons_to_be_ABC'
        inspect.isabstract(cls)
        for B in cls.__mro__:
            getattr(B, '__abstractmethods__', ())
            for attr, x in B.__dict__.items():
                getattr(x, '__isabstractmethod__', False)
    def __call__(cls, /, *args, **kwargs):
        #meta = type(cls)
        #assert issubclass(meta, __class__)
        #if __is_abstract_class__(cls): raise TypeError(cls)
        reasons = collect_reasons_to_be_ABC(cls)
        if reasons:
            s = ', '.join(sorted(map(repr, reasons)))
            raise TypeError(fr'{cls!r} is ABC: {s!s}')
        sf = super(__class__, type(cls)).__call__(cls, *args, **kwargs)
        return sf

class MetaMeta4delta_init(type):
    __slots__ = ()
    def __call__(meta, /, *args, **kwargs):
        assert issubclass(meta, type)
        metameta = type(meta)
        assert issubclass(metameta, __class__)
        cls = super(__class__, type(meta)).__call__(meta, *args, **kwargs)
        if not isinstance(cls, type): raise TypeError
        if type(cls) is meta:
            cls.___3meta3__delta_collects__3meta3___ = None
                #override super... proof from exception
            d = {}
            attrs = '___3meta3__delta_init__preorder__3meta3___  ___3meta3__delta_init__postorder__3meta3___  ___3meta3__delta_check__preorder__3meta3___  ___3meta3__delta_check__postorder__3meta3___'.split()
            collects_deltas_at_to(cls, attrs, d)
            cls.___3meta3__delta_collects__3meta3___ = d
        return cls
def collects_deltas_at_to(cls, attrs, output_dict, /):
    for attr in {*attr}:
        collect1_deltas_at_to(cls, attr, output_dict)
def collect1_deltas_at_to(cls, attr, output_dict, /):
    #output_dict.setdefault(attr, tuple(ls))
    ls = []
    Nothing = object()
    for B in cls.__mro__:
        delta = B.__dict__.get(attr, Nothing)
        if delta is not Nothing:
            ls.append(delta)
    output_dict[attr] = tuple(ls)

class Meta4delta_init(type, metaclass=MetaMeta4delta_init):
    __slots__ = ()
    def __call__(cls, /, *args, **kwargs):
        #meta = type(cls)
        #assert issubclass(meta, __class__)
        sf = super(__class__, type(cls)).__call__(cls, *args, **kwargs)
        if type(sf) is cls:
            on_new_sf__ver2(sf, *args, **kwargs)
            return sf
        return sf

def on_new_sf__ver2(sf, /, *args, **kwargs):
        cls = type(sf)
        d = cls.__dict__['___3meta3__delta_collects__3meta3___']
        .. ..
def on_new_sf__ver1(sf, /, *args, **kwargs):
        cls = type(sf)
        #################################
        #################################
        for B in cls.__mro__:
            delta_init_pre = B.__dict__.get('___3meta3__delta_init__preorder__3meta3___')
            if delta_init_pre is not None:
                delta_init_pre(sf, *args, **kwargs)
        #################################
        for B in reversed(cls.__mro__):
            delta_init_post = B.__dict__.get('___3meta3__delta_init__postorder__3meta3___')
            if delta_init_post is not None:
                delta_init_post(sf, *args, **kwargs)
        #################################
        #################################
        for B in cls.__mro__:
            delta_check_pre = B.__dict__.get('___3meta3__delta_check__preorder__3meta3___')
            if delta_check_pre is not None:
                delta_check_pre(sf)
        #################################
        for B in reversed(cls.__mro__):
            delta_check_post = B.__dict__.get('___3meta3__delta_check__postorder__3meta3___')
            if delta_check_post is not None:
                delta_check_post(sf)
        #################################
        #################################

#class ABCMeta2(_ABCMeta, IMeta4check_ABC, metaclass=Meta4check_ABC):
#class ABCMeta4delta(_ABCMeta, Meta4check_ABC, metaclass=Meta4check_ABC):
    __slots__ = ()

