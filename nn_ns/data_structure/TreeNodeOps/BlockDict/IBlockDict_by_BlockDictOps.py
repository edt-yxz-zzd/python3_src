
'''
IBlockDictOps to IBlockDict

'''

__all__ = '''
    IBlockDict_by_BlockDictOps
    '''.split()


from .abc import not_implemented, override
from .IBlockDict import IBlockDict
from ..BlockDictOps.IBlockDictOps import IBlockDictOps

class IBlockDict_by_BlockDictOps(IBlockDict):
    __slots__ = ()

    @not_implemented
    def _get_block_dict_ops_(self):
        ...
    @not_implemented
    def _get_data_for_block_dict_ops_(self):
        ...

    def get_block_dict_ops(self):
        ops = self._get_block_dict_ops_()
        assert isinstance(ops, IBlockDictOps)
        return ops
    @property
    def block_dict_ops(self):
        return self.get_block_dict_ops()
    @property
    def __data(self):
        return self._get_data_for_block_dict_ops_()



    ##################


    @override
    def _get_block_dict_key_ops_(self):
        # -> IBlockDictKeyOps<dict_key, KeyEx<dict_key> >
        #
        # dict_key vs tree_key
        #   dict_key = basic_key = key in IBlockDictKeyOps
        #   tree_key = lkey_ex = left_key_ex = left_bound
        #       is key_ex in IBlockDictKeyOps
        return self.block_dict_ops.block_dict_key_ops
    @override
    def _get_eq_dict_value_ops_(self):
        # -> IEqOps<dict_value>
        return self.block_dict_ops.eq_dict_value_ops

    @override
    def get_num_block_keys(self):
        # no __len__
        return self.block_dict_ops.get_num_block_keys(self.__data)
    @override
    def iter_block_items(self, *, reverse=False):
        # no items
        return self.block_dict_ops.iter_block_items(self.__data, reverse=reverse)

    @override
    def iter_all_touch_or_overlap_block_items(self, block_key
            , overlap_only:bool
                # False ==>> touch_or_overlap
                # True ==>> overlap_only
            , *, reverse=False):
        return self.block_dict_ops.iter_all_touch_or_overlap_block_items(
                self.__data, block_key, overlap_only, reverse=reverse)

    @override
    def _index_block_item_at_(self, i:'UInt'):
        return self.block_dict_ops._index_block_item_at_(self.__data, i)

if __name__ == "__main__":
    XXX = IBlockDict_by_BlockDictOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)


