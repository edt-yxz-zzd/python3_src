
'''
std abc.ABC has no "__slots__ = ()"

'''



__all__ = '''
    ABC
    not_implemented
    override
    abstractmethod
    '''.split()

from abc import ABC as __error_ABC, abstractmethod, ABCMeta
class ABC(metaclass=ABCMeta):
    __slots__ = ()



def override(f):
    return f

abstractmethod = abstractmethod
not_implemented = abstractmethod
    # diff:
    #   abstractmethod may offer default impl
    #   but not_implemented should not


