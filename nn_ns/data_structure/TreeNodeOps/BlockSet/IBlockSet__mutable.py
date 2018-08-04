
__all__ = '''
    IBlockSet__mutable
    '''.split()

from ..OtherOps.IEqOps import IEqOps
from ..OtherOps.ITotalOrderingOps import ITotalOrderingOps
from ..BlockDictOps.IBlockDictKeyOps import IBlockDictKeyOps
from .IBlockSet import IBlockSet

from .abc import not_implemented, override
'''
from seed.tiny import echo


set_entity2block_key = echo
set_ireplace_block_key_of_entity = lambda entity, block_key: block_key
'''



class IBlockSet__mutable(IBlockSet):
    '''
not (MutableMapping):
    since no __len__/__iter__
        # hence no pop

dict_key :: ITotalOrderingOps
    # to using KeyOrderedTree
dict_value :: IEqOps
    # to merge two touch/overlap blocks with same dict_value

dict_key = basic_key = key :: Key in IBlockDictKeyOps
    # BlockSet implement details:
    # tree_key = lkey_ex = left_key_ex = left_bound :: KeyEx in IBlockDictKeyOps

block_key = (lkey_ex, rkey_ex) = range :: Range


'''
    __slots__ = ()


    @not_implemented
    def add_block_key(self, block_key):
        # if block_key overlap or touch input_block_key
        #   then merge the two ranges/block_keys
        ...

    @not_implemented
    def pop_block_keys_of_block_key(self, block_key, *, reverse=False):
        # -> [block_key]
        #   not Iter block_key
        ...
    @not_implemented
    def discard_block_key(self, block_key):
        ...
    @not_implemented
    def pop_left_or_right_block_key(self, right:bool):
        ...

    @not_implemented
    def clear(self):
        ...
    @not_implemented
    def swap(self, other):
        if self is other: return
        ...
    def assign(self, other):
        if self is other: return
        other = other.copy()
        self.swap(other)

    @override
    def self_make_block_set_from_dict_keys(self, dict_keys):
        other = self.self_make_empty_block_set()
        other.update_from_dict_keys(dict_keys)
        return other
    @override
    def self_make_block_set_from_block_keys(self, block_keys):
        other = self.self_make_empty_block_set()
        other.update_from_block_keys(block_keys)
        return other








    def pop_block_keys_of_dict_key(self, dict_key):
        block_key = self.mkSingletonRange(dict_key)
        block_keys = self.pop_block_keys_of_block_key(block_key)
        return block_keys
    def pop_block_key_of_dict_key(self, dict_key):
        block_keys = self.pop_block_keys_of_dict_key(dict_key)
        if not block_keys:
            raise KeyError(dict_key)
        [block_key] = block_keys
        return block_key

    def pop_left_block_key(self):
        return self.pop_left_or_right_block_key(False)
    def pop_right_block_key(self):
        return self.pop_left_or_right_block_key(True)
    def pop_block_key(self):
        # no pop
        return self.pop_right_block_key()

    def update_from_dict_keys(self, dict_keys):
        for dict_key in dict_keys:
            self.add_dict_key(dict_key)
    def update_from_block_keys(self, block_keys):
        for block_key in block_keys:
            self.add_block_key(block_key)


    def add_dict_key(self, dict_key):
        block_key = self.mkSingletonRange(dict_key)
        self.add_block_key(block_key)

    def del_dict_key(self, dict_key):
        self.pop_block_key_of_dict_key(dict_key)

    def discard_dict_key(self, dict_key):
        block_key = self.mkSingletonRange(dict_key)
        self.discard_block_key(block_key)


    def __check_other(self, other):
        if not isinstance(other, __class__): raise TypeError
        if self.block_dict_key_ops != other.block_dict_key_ops : raise TypeError
    def update(self, block_set_or_dict_keys):
        if not isinstance(block_set_or_dict_keys, __class__):
            dict_keys = block_set_or_dict_keys
            self.update_from_dict_keys(dict_keys)
            return

        other = block_set_or_dict_keys
        self.__check_other(other)

        block_keys = other.iter_block_keys()
        self.update_from_block_keys(block_keys)

    add = add_dict_key
    remove = del_dict_key
    discard = discard_dict_key
    # no pop
    def __ior__(self, other):
        self.__check_other(other)
        self.swap(self | other)
        #bug: forgor return self
        return self
    def __iand__(self, other):
        self.__check_other(other)
        self.swap(self & other)
        return self
    def __ixor__(self, other):
        self.__check_other(other)
        self.swap(self ^ other)
        return self
    def __isub__(self, other):
        self.__check_other(other)
        self.swap(self - other)
        return self


if __name__ == '__main__':
    XXX = IBlockSet__mutable

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)


