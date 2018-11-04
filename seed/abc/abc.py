
'''
std abc.ABC has no "__slots__ = ()"

'''



__all__ = '''
    ABC
    not_implemented
    override
    define
    final
    abstractmethod
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

abstractmethod = abstractmethod
not_implemented = abstractmethod
    # diff:
    #   abstractmethod may offer default impl
    #   but not_implemented should not


