

__all__ = '''
    ABC
    ABCMeta
    optional_method
    abstract_method
    override
    define
    '''.split()

from abc import ABC, ABCMeta, abstractmethod

ABC = ABC
ABCMeta = ABCMeta
abstract_method = abstractmethod
def optional_method(__f):
    return __f
def override(__f):
    return __f
def define(__f):
    return __f











