
'''
std abc.ABC has no "__slots__ = ()"

from seed.abc.abc import override, def_new_method, overridable_default_method, collaboration_method_chain, final_method
    view python3_src/my_convention/overridable_method__to_auto_generate_wrapper_class_forward_call_src_code.txt
'''



__all__ = '''
    ABC
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

from abc import ABC as __error_ABC, abstractmethod, ABCMeta as _ABCMeta
class ABC(metaclass=_ABCMeta):
    __slots__ = ()



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


