__all__ = '''
    ISetOps__is_disjoint
    '''.split()

from .abc import not_implemented, define
from .ISetOps import ISetOps

class ISetOps__is_disjoint(ISetOps):
    __slots__ = ()

    @define
    @not_implemented
    def is_disjoint(ops, self, other):
        # -> bool
        pass

