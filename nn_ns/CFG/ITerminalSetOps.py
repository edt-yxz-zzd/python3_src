__all__ = '''
    ITerminalSetOps
    '''.split()

from .abc import ABC, abstractmethod

class ITerminalSetOps(ABC):
    '''for CFG.terminal_set_ops

all objects satisfied this interface is a terminal_set_ops
    i.e. ITerminalSetOps ducktype
'''
    __slots__ = ()
    @abstractmethod
    def is_empty(ops, self):
        '-> bool'
        raise NotImplementedError
    @abstractmethod
    def is_disjoint(ops, self, other):
        '-> bool'
        raise NotImplementedError
    @abstractmethod
    def contains(ops, self, element):
        '-> bool'
        raise NotImplementedError
    @abstractmethod
    def intersection(ops, self, other):
        '-> set_obj'
        raise NotImplementedError
    @abstractmethod
    def union(ops, self, other):
        '-> set_obj'
        raise NotImplementedError



