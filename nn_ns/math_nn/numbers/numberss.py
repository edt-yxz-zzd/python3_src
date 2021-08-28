import warnings, sys
DeprecationWarning
warnings.warn("deprecated, use INumberList/INumberTable instead"
        , DeprecationWarning)
print("deprecated, use INumberList/INumberTable instead", file=sys.stderr)

__all__ = '''
    NumberList
    NumberTable
    '''.split()

from .INumberList import \
    ( INumberList
    , INumberList__neg2zero
    , INumberList__nums__concrete_mixins
    )
from .INumberTable import \
    ( INumberTable
    , INumberTable__table__concrete_mixins
    )
from .numbers_common import abstract_method, optional_method, override, define

class NumberList(INumberList__nums__concrete_mixins):
    __slots__ = 'nums'
    @override
    def __please_add_nums_to_slots__(self):pass
    @override
    def _calc_pos(self, n, nums):
        #calc for positive n
        return super()._calc_pos(n, nums)
class NumberTable(INumberTable__table__concrete_mixins):
    __slots__ = 'table'
    @override
    def __please_add_table_to_slots__(self):pass



