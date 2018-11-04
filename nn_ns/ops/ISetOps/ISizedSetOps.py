
__all__ = '''
    ISizedSetOps
    '''.split()

from .abc import not_implemented, define
from .ISetOps__is_empty import ISetOps__is_empty

class ISizedSetOps(ISetOps__is_empty):
    'finite set and know its size'
    __slots__ = ()

    @define
    @not_implemented
    def size_of(ops, self):
        # -> UInt
        pass


