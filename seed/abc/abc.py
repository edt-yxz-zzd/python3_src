
'''
std abc.ABC has no "__slots__ = ()"

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
#from abc import abstractmethod
#import inspect #.isabstract

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.abc.abc__ver1 import override, def_new_method, overridable_default_method, collaboration_method_chain, final_method
from seed.abc.abc__ver1 import not_implemented
#from seed.abc.abc__ver1 import verify_slots_setting, check_slots_setting, Base4check_slots_setting, MetaMeta4check_slots_setting, Meta4check_slots_setting, ABCMeta4check_slots_setting, ABC4check_slots_setting, ABC4check_slots_setting__no_slots


r'''
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
#'''




