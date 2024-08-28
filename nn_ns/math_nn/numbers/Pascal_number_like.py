

import warnings, sys
DeprecationWarning
warnings.warn(f"deprecated:{__name__}, use IPascalNumberLike instead"
        , DeprecationWarning)
print(f"deprecated:{__name__}, use IPascalNumberLike instead", file=sys.stderr)

__all__ = '''
    PascalNumberLike
    '''.split()

from .IPascalNumberLike import IPascalNumberLike
from .INumberTable import \
    ( INumberTable
    , INumberTable__table__concrete_mixins
    )
from .numbers_common import abstract_method, optional_method, override, define

class PascalNumberLike(IPascalNumberLike, INumberTable__table__concrete_mixins):
    __slots__ = 'table'
    @override
    def __please_add_table_to_slots__(self):pass
    @override
    def row_len(self, n):
        return n+1

    @override
    def __init__(self):
        super().__init__([[1]])

    @override
    def _lookup_pos_underflow(self, n, k, table):
        assert n >= 0
        assert k < 0
        return 0

    @override
    def _lookup_pos_overflow(self, n, k, table):
        assert n >= 0
        assert k >= self.row_len(n)
        return 0
