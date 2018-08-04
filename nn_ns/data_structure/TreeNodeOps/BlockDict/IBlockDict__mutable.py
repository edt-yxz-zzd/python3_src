


__all__ = '''
    IBlockDict__mutable
    '''.split()

from ..OtherOps.IEqOps import IEqOps
from ..OtherOps.ITotalOrderingOps import ITotalOrderingOps
from ..BlockDictOps.IBlockDictKeyOps import IBlockDictKeyOps
from .IBlockDict import IBlockDict

from .abc import not_implemented, override



#from collections.abc import MutableMapping
def make_pop():
    Nothing = object()
    def pop(self, dict_key, default=Nothing):
        block_items = self.pop_block_items_of_dict_key(dict_key)
        if not block_items:
            if default is Nothing:
                raise KeyError(dict_key)
            return default

        [block_item] = block_items
        block_key, dict_value = block_item
        return dict_value


        # old version
        if default is Nothing:
            dict_value = self[dict_key] # may KeyError
            del self[dict_key]
        else:
            dict_value = self.get(dict_key, Nothing)
            if dict_value is Nothing:
                # not exist
                dict_value = default
            else:
                # exist
                del self[dict_key]
        return dict_value
    return pop




class IBlockDict__mutable(IBlockDict):
    '''
not (MutableMapping):
    since no __len__/__iter__
        # hence no keys/items/values/popitem

dict_key :: ITotalOrderingOps
    # to using KeyOrderedTree
dict_value :: IEqOps
    # to merge two touch/overlap blocks with same dict_value

dict_key = basic_key = key :: Key in IBlockDictKeyOps
    # BlockDict implement details:
    # tree_key = lkey_ex = left_key_ex = left_bound :: KeyEx in IBlockDictKeyOps

item = (dict_key, dict_value)

block_key = (lkey_ex, rkey_ex) = range :: Range
block_item = (block_key, dict_value) = entity


why not m[begin:end] for get/set/del?
    # block_key2iter_block_items
    # set_block_item
    # pop_block_items_of_block_key/discard_block_key
    since we donot know what Key is.
    Key may be slice, so confuse...

'''
    __slots__ = ()


    @not_implemented
    def set_block_item(self, block_key, dict_value):
        # if block_key overlap or touch input_block_key
        #   and dict_value_eq(self[block_key], dict_value):
        #   then merge the two ranges/block_keys
        ...

    @not_implemented
    def pop_block_items_of_block_key(self, block_key, *, reverse=False):
        # -> [block_item]
        #   not Iter block_item
        ...
    @not_implemented
    def discard_block_key(self, block_key):
        ...
    @not_implemented
    def pop_left_or_right_block_item(self, right:bool):
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
    def self_make_block_dict_from_items(self, items):
        other = self.self_make_empty_block_dict()
        other.update_from_items(items)
        return other
    @override
    def self_make_block_dict_from_block_items(self, block_items):
        other = self.self_make_empty_block_dict()
        other.update_from_block_items(block_items)
        return other

    def pop_block_items_of_dict_key(self, dict_key):
        block_key = self.mkSingletonRange(dict_key)
        block_items = self.pop_block_items_of_block_key(block_key)
        return block_items
    def pop_block_item_of_dict_key(self, dict_key):
        block_items = self.pop_block_items_of_dict_key(dict_key)
        if not block_items:
            raise KeyError(dict_key)
        [block_item] = block_items
        return block_item

    def pop_left_block_item(self):
        return self.pop_left_or_right_block_item(False)
    def pop_right_block_item(self):
        return self.pop_left_or_right_block_item(True)
    def pop_block_item(self):
        # no popitem
        return self.pop_right_block_item()

    def update_from_items(self, items):
        for dict_key, dict_value in items:
            self[dict_key] = dict_value
    def update_from_block_items(self, block_items):
        for block_key, dict_value in block_items:
            self.set_block_item(block_key, dict_value)
    def set_dict_key2default(self, dict_key, dict_key2default):
        Nothing = []
        may_dict_value = self.get(dict_key, Nothing)
        if may_dict_value is not Nothing:
            dict_value = may_dict_value
            return dict_value

        dict_value = self[dict_key] = dict_key2default(dict_key)
        return dict_value
    def set_fdefault(self, dict_key, fdefault):
        def dict_key2default(dict_key):
            return fdefault()
        return self.set_dict_key2default(dict_key, dict_key2default)


    def __setitem__(self, dict_key, dict_value):
        block_key = self.mkSingletonRange(dict_key)
        self.set_block_item(block_key, dict_value)
    def __delitem__(self, dict_key):
        self.pop_block_item_of_dict_key(dict_key)


    pop = make_pop()

    def update(self, block_dict_or_items):
        if not isinstance(block_dict_or_items, __class__):
            items = block_dict_or_items
            self.update_from_items(items)
            return

        other = block_dict_or_items
        if self.block_dict_key_ops != other.block_dict_key_ops: raise TypeError
        if other.eq_dict_value_ops != self.eq_dict_value_ops: return TypeError

        block_items = other.iter_block_items()
        self.update_from_block_items(block_items)
    #bug:
    #   1) default must be dict_value, not None
    #   2) should return dict_value
    #def setdefault(self, dict_key, default=None):
    #   self.set_fdefault(dict_key, lambda:default)
    def setdefault(self, dict_key, default):
        return self.set_fdefault(dict_key, lambda:default)




if __name__ == '__main__':
    XXX = IBlockDict__mutable

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)


