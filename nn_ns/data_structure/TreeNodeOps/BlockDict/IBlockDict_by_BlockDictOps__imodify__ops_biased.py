
'''
IBlockDictOps__imodify to IBlockDict__mutable
    use the ops methods instead of IBlockDict__mutable methods
'''

__all__ = '''
    IBlockDict_by_BlockDictOps__imodify__ops_biased
    '''.split()

from .abc import override
from .IBlockDict_by_BlockDictOps__imodify import \
    IBlockDict_by_BlockDictOps__imodify


class IBlockDict_by_BlockDictOps__imodify__ops_biased(IBlockDict_by_BlockDictOps__imodify):
    # use the ops methods instead of IBlockDict__mutable methods
    __slots__ = ()


    @property
    def __data(self):
        return self._get_data_for_block_dict_ops_()
    @__data.setter
    def __data(self, data):
        self._set_data_for_block_dict_ops_(data)


    @override
    def assign(self, other):
        if self is other: return
        if type(self) is not type(other): raise TypeError
        if self.block_dict_ops != other.block_dict_ops: raise TypeError
        self.__data = self.block_dict_ops.copy_block_dict(other.__data)


    @override
    def __delitem__(self, dict_key):
        self.__data = self.block_dict_ops.idel_item(self.__data, dict_key)
    @override
    def __setitem__(self, dict_key, dict_value):
        self.__data = self.block_dict_ops.iset_item(self.__data, dict_key, dict_value)
    @override
    def pop(self, *args):
        e, self.__data = self.block_dict_ops.ipop(self.__data, *args)
        return e
    @override
    def pop_block_item(self):
        e, self.__data = self.block_dict_ops.ipop_block_item(self.__data)
        return e
    @override
    def pop_block_item_of_dict_key(self, dict_key):
        e, self.__data = self.block_dict_ops.ipop_block_item_of_dict_key(self.__data, dict_key)
        return e
    @override
    def pop_block_items_of_dict_key(self, dict_key):
        e, self.__data = self.block_dict_ops.ipop_block_items_of_dict_key(self.__data, dict_key)
        return e
    @override
    def pop_left_block_item(self):
        e, self.__data = self.block_dict_ops.ipop_left_block_item(self.__data)
        return e
    @override
    def pop_right_block_item(self):
        e, self.__data = self.block_dict_ops.ipop_right_block_item(self.__data)
        return e
    @override
    def self_make_block_dict_from_block_items(self, block_items):
        other = self.self_make_empty_block_dict()
        other.__data = self.block_dict_ops.make_block_dict_from_block_items(block_items)
        return other
    @override
    def self_make_block_dict_from_items(self, items):
        other = self.self_make_empty_block_dict()
        other.__data = self.block_dict_ops.make_block_dict_from_items(items)
        return other

    @override
    def self_make_block_dict_from_iterable(self, iterable, is_block_items:bool):
        other = self.self_make_empty_block_dict()
        other.__data = self.block_dict_ops.make_block_dict_from_iterable(
                                    iterable, is_block_items)
        return other
    @override
    def self_make_whole_block_dict(self, dict_value):
        other = self.self_make_empty_block_dict()
        other.__data = self.block_dict_ops.make_whole_block_dict(dict_value)
        return other
    @override
    def self_make_complement_block_dict(self, block_key2dict_value):
        other = self.self_make_empty_block_dict()
        other.__data = self.block_dict_ops.make_complement_block_dict_of(
                            self.__data, block_key2dict_value)
        return other






    def __check_other(self, other):
        if not isinstance(other, __class__): raise TypeError
        if self.block_dict_key_ops != other.block_dict_key_ops: raise TypeError
        if other.eq_dict_value_ops != self.eq_dict_value_ops: raise TypeError
    @override
    def make_union(self, other, combine):
        self.__check_other(other)
        r = self.self_make_empty_block_dict()
        r.__data = self.block_dict_ops.make_union(
                            self.__data, other.__data, combine)
        return r

    @override
    def make_intersection(self, other, combine):
        self.__check_other(other)
        r = self.self_make_empty_block_dict()
        r.__data = self.block_dict_ops.make_intersection(
                            self.__data, other.__data, combine)
        return r
    @override
    def make_difference(self, other):
        self.__check_other(other)
        r = self.self_make_empty_block_dict()
        r.__data = self.block_dict_ops.make_difference(
                            self.__data, other.__data)
        return r
    @override
    def make_symmetric_difference(self, other):
        self.__check_other(other)
        r = self.self_make_empty_block_dict()
        r.__data = self.block_dict_ops.make_symmetric_difference(
                            self.__data, other.__data)
        return r

    @override
    def set_dict_key2default(self, dict_key, dict_key2default):
        v, self.__data = self.block_dict_ops.iset_dict_key2default(self.__data, dict_key, dict_key2default)
        return v
    @override
    def set_fdefault(self, dict_key, fdefault):
        v, self.__data = self.block_dict_ops.iset_fdefault(self.__data, dict_key, fdefault)
        return v
    @override
    def setdefault(self, dict_key, default):
        # default must be dict_value; so no(default=None)
        v, self.__data = self.block_dict_ops.isetdefault(self.__data, dict_key, default)
        return v

    #def update(self, other_or_items):
    @override
    def update_from_block_items(self, block_items):
        self.__data = self.block_dict_ops.iupdate_from_block_items(self.__data, block_items)
    @override
    def update_from_items(self, items):
        self.__data = self.block_dict_ops.iupdate_from_items(self.__data, items)


if __name__ == "__main__":
    XXX = IBlockDict_by_BlockDictOps__imodify__ops_biased

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)


