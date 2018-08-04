
__all__ = '''
    IEqOps
    '''.split()

from .abc import not_implemented
from .IOps import IOps


class IEqOps(IOps):
    __slots__ = ()
    @not_implemented
    def eq(ops, lkey, rkey):
        ...
    def ne(ops, lkey, rkey):
        return not ops.eq(lkey, rkey)

