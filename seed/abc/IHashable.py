
r'''
from seed.abc.IHashable import IHashable
#'''

__all__ = '''
    IHashable
    '''.split()


from collections.abc import Hashable
from seed.abc.abc__ver1 import abstractmethod, ABC, override

class IHashable(Hashable, ABC):
    r'''
    not [ABC is abc.ABC]
    not [Hashable <: ABC]
    ABC will check __slots__
    #'''
    __slots__ = ()

    @abstractmethod
    def __hash__(ops, /):
        '-> int'
    @abstractmethod
    def __eq__(lhs_ops, rhs_ops, /):
        '-> bool'
    @override
    def __ne__(lhs_ops, rhs_ops, /):
        '-> bool'
        return not lhs_ops==rhs_ops

