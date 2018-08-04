


'''
IBlockDictOps__imodify to IBlockDict__mutable

'''

__all__ = '''
    IBlockDict_by_BlockDictOps__imodify
    '''.split()


from .abc import not_implemented, override
from .IBlockDict_by_BlockDictOps import IBlockDict_by_BlockDictOps
from .IBlockDict__mutable import IBlockDict__mutable
from ..BlockDictOps.IBlockDictOps__imodify import IBlockDictOps__imodify



class IBlockDict_by_BlockDictOps__imodify(
        IBlockDict_by_BlockDictOps, IBlockDict__mutable):
    __slots__ = ()

    @not_implemented
    def _set_data_for_block_dict_ops_(self, data):
        ...

    @override
    def get_block_dict_ops(self):
        ops = super().get_block_dict_ops()
        assert isinstance(ops, IBlockDictOps__imodify)
        return ops
    @property
    def __data(self):
        return self._get_data_for_block_dict_ops_()
    @__data.setter
    def __data(self, data):
        self._set_data_for_block_dict_ops_(data)


    ##################


    @override
    def copy(self):
        other = self.self_make_empty_block_dict()
        other.__data = self.block_dict_ops.copy_block_dict(self.__data)
        return other



    @override
    def swap(self, other):
        if self is other: return

        if type(other) is not type(self): return TypeError
        if other.block_dict_key_ops != self.block_dict_key_ops: raise TypeError
        if other.eq_dict_value_ops != self.eq_dict_value_ops: raise TypeError
        if self.__data is other.__data: return

        other.__data, self.__data = self.__data, other.__data
    '''
    def assign(self, other):
        if self is other: return
        other = other.copy()
        self.swap(other)
    '''

    @override
    def pop_left_or_right_block_item(self, right:bool):
        old_entity, new_data = self.block_dict_ops.ipop_left_or_right_block_item(self.__data, right)
        self.__data = new_data
        return old_entity

    @override
    def clear(self):
        self.__data = self.block_dict_ops.iclear(self.__data)
        return
    @override
    def set_block_item(self, block_key, dict_value):
        # if block_key overlap or touch input_block_key
        #   and block_dict_value_eq(self[block_key], dict_value):
        #   then merge the two ranges/block_keys
        self.__data = self.block_dict_ops.iset_block_item(self.__data, block_key, dict_value)


    @override
    def discard_block_key(self, block_key):
        #self.pop_block_items_of_block_key(block_key)
        new_data = self.block_dict_ops.idiscard_block_key(
                    self.__data, block_key)
        self.__data = new_data
        return

    @override
    def pop_block_items_of_block_key(self, block_key, *, reverse=False):
        # -> [block_item]
        #   not Iter block_item
        block_items, new_data = \
            self.block_dict_ops.ipop_block_items_of_block_key(
                    self.__data, block_key, reverse=reverse)
        self.__data = new_data
        return block_items




if __name__ == "__main__":
    XXX = IBlockDict_by_BlockDictOps__imodify

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)


