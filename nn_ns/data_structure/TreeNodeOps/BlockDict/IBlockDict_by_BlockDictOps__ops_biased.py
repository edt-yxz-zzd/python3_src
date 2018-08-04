
'''
IBlockDictOps to IBlockDict
    use the ops methods instead of IBlockDict methods
'''

__all__ = '''
    IBlockDict_by_BlockDictOps__ops_biased
    '''.split()

from .abc import override
from .IBlockDict_by_BlockDictOps import IBlockDict_by_BlockDictOps



class IBlockDict_by_BlockDictOps__ops_biased(IBlockDict_by_BlockDictOps):
    # use the ops methods instead of IBlockDict methods
    __slots__ = ()

    @property
    def __data(self):
        return self._get_data_for_block_dict_ops_()

    '''
    @override
    def self_make_whole_block_dict(self, dict_value):
        other = ???
        other.__data = self.block_dict_ops.make_whole_block_dict(dict_value)
        return other
    @override
    def self_make_complement_block_dict(self, block_key2dict_value):
        other = ???
        other.__data = self.block_dict_ops.make_complement_block_dict_of(
                            self.__data, block_key2dict_value)
        return other
    '''


    @override
    def index_block_item_at(self, i:'Int'):
        return self.block_dict_ops.index_block_item_at(self.__data, i)
    @override
    def get_first_or_last_block_item(self, last:bool):
        return self.block_dict_ops.get_first_or_last_block_item(self.__data, last)
    @override
    def get_first_block_item(self):
        return self.block_dict_ops.get_first_block_item(self.__data)
    @override
    def get_last_block_item(self):
        return self.block_dict_ops.get_last_block_item(self.__data)

    @override
    def __bool__(self):
        return not self.block_dict_ops.is_empty(self.__data)
    @override
    def __contains__(self, dict_key):
        return self.block_dict_ops.contains_dict_key(self.__data, dict_key)
    @override
    def __eq__(self, other):
        return (type(self) is type(other)
            and self.block_dict_ops == other.block_dict_ops
            and self.block_dict_ops.block_dict_eq(self.__data, other.__data)
            )
    @override
    def __getitem__(self, dict_key):
        return self.block_dict_ops.dict_key2dict_value(self.__data, dict_key)

    @property
    @override
    def block_dict_key_ops(self):
        return self.block_dict_ops.block_dict_key_ops
    @override
    def block_key2block_items(self, block_key, *, reverse=False):
        return self.block_dict_ops.block_key2block_items(self.__data, block_key, reverse=reverse)

    @override
    def block_key2iter_block_items(self, block_key, *, reverse=False):
        return self.block_dict_ops.block_key2iter_block_items(self.__data, block_key, reverse=reverse)
    @override
    def dict_key2block_items(self, dict_key):
        return self.block_dict_ops.dict_key2block_items(self.__data, dict_key)

    @property
    @override
    def dict_value_eq(self):
        return self.block_dict_ops.dict_value_eq
    @property
    @override
    def eq_dict_value_ops(self):
        return self.block_dict_ops.eq_dict_value_ops
    @override
    def get(self, dict_key, default=None):
        return self.block_dict_ops.getdefault(self.__data, dict_key, default)
    @override
    def get_block_dict_key_ops(self):
        return self.block_dict_ops.block_dict_key_ops
    @override
    def get_eq_dict_value_ops(self):
        return self.block_dict_ops.eq_dict_value_ops
    @override
    def get_total_dict_key_ops(self):
        return self.block_dict_ops.total_dict_key_ops

    @override
    def is_exactly_block_key(self, block_key):
        return self.block_dict_ops.is_exactly_block_key(self.__data, block_key)
    @override
    def is_one_piece_block_key(self, block_key):
        return self.block_dict_ops.is_one_piece_block_key(self.__data, block_key)

    @override
    def iter_block_keys(self, *, reverse=False):
        return self.block_dict_ops.iter_block_keys(self.__data, reverse=reverse)
    @override
    def iter_dict_values(self, *, reverse=False):
        return self.block_dict_ops.iter_dict_values(self.__data, reverse=reverse)



    @override
    def list_all_touch_or_overlap_block_items(self, block_key
            , overlap_only:bool, *, reverse=False):
        return self.block_dict_ops.list_all_touch_or_overlap_block_items(self.__data, block_key, overlap_only, reverse=reverse)
    @property
    @override
    def mkSingletonRange(self):
        return self.block_dict_ops.block_dict_key_ops.mkSingletonRange

    @property
    @override
    def total_dict_key_ops(self):
        return self.block_dict_ops.total_dict_key_ops


if __name__ == "__main__":
    XXX = IBlockDict_by_BlockDictOps__ops_biased

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)


