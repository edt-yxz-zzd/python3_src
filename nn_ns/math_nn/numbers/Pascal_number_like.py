

import warnings, sys
DeprecationWarning
warnings.warn("deprecated, use IPascalNumberLike instead"
        , DeprecationWarning)
print("deprecated, use IPascalNumberLike instead", file=sys.stderr)

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


