__all__ = '''
    ISetOps__is_subset_of
    '''.split()

from .abc import not_implemented, define
from .ISetOps import ISetOps

class ISetOps__is_subset_of(ISetOps):
    __slots__ = ()

    @define
    @not_implemented
    def is_subset_of(ops, self, other):
        # -> bool
        pass

    def is_superset_of(ops, self, other):
        return ops.is_subset_of(other, self)
    def equals(ops, self, other):
        return ops.is_subset_of(self, other) and ops.is_subset_of(other, self)

