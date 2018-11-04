
__all__ = '''
    ISetOps
    '''.split()

from .abc import ABC, not_implemented, define

class ISetOps(ABC):
    __slots__ = ()

    @define
    @not_implemented
    def contains(ops, elem):
        # raise TypeError | return bool
        pass

