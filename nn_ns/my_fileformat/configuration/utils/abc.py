
__all__ = '''
    abstractmethod
    ABC
    final
    override
    '''.split()

#from .abc import abstractmethod, ABC, final, override
from abc import abstractmethod, ABC

ABC = ABC
abstractmethod = abstractmethod
def final(f):
    return f
def override(f):
    return f


