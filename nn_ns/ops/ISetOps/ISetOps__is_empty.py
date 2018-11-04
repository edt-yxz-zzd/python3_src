__all__ = '''
    ISetOps__is_empty
    '''.split()

from .abc import not_implemented, define
from .ISetOps import ISetOps


class ISetOps__is_empty(ISetOps):
    __slots__ = ()

    @define
    @not_implemented
    def is_empty(ops, self):
        # -> bool
        pass

