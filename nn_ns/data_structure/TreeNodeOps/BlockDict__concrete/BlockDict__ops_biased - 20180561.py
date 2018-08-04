

'''
BlockDict2
    imple all methods using ops version instead of inherit from IBlockDict
        to test the ops class

###################################


'''

from .BlockDict import __doc__ as _doc, BlockDict as BlockDict1
__doc__ = '\n\n'.join([__doc__, BlockDict1.__doc__, _doc])
#print('\n'*10)
#__doc__ = '\n'.join(__doc__.split('\n')[:600])




class BlockDict(BlockDict1):
    '''

BlockDict:
        __slots__
        __init__
        swap
        __repr__
        self_make_empty_block_dict
        make_empty_block_dict
        copy
        block_dict_ops
        _get_block_dict_key_ops_
        _get_eq_dict_value_ops_
        get_num_block_keys
        iter_block_items
        pop_left_or_right_block_item
        clear
        iter_all_touch_or_overlap_block_items
        set_block_item
        discard_block_items_of_block_key
        pop_block_items_of_block_key
        _BlockDict__ops
        _BlockDict__tree

all_methods:
        x _BlockDict__ops
        x _BlockDict__tree
        x _IBlockDict__block_key2iter_block_items__handle_left_or_right_end
        __bool__
        __contains__
        __delitem__
        __eq__
        __getitem__
        __hash__
        @ __init__
        __ne__
        @ __repr__
        __setitem__
        @ __slots__
        @ _get_block_dict_key_ops_
        @ _get_eq_dict_value_ops_
        assign
        block_dict_key_ops
        @ block_dict_ops
        block_key2block_items
        block_key2iter_block_items
        @ clear
        @ copy
        dict_key2block_items
        dict_value_eq
        @ discard_block_items_of_block_key
        eq_dict_value_ops
        get
        get_block_dict_key_ops
        get_eq_dict_value_ops
        @ get_num_block_keys
        get_total_dict_key_ops
        is_exactly_block_key
        is_one_piece_block_key
        @ iter_all_touch_or_overlap_block_items
        @ iter_block_items
        iter_block_keys
        iter_dict_values
        list_all_touch_or_overlap_block_items
        @ make_empty_block_dict
        mkSingletonRange
        pop
        pop_block_item
        pop_block_item_of_dict_key
        @ pop_block_items_of_block_key
        pop_block_items_of_dict_key
        pop_left_block_item
        @ pop_left_or_right_block_item
        pop_right_block_item
        self_make_block_dict_from_block_items
        self_make_block_dict_from_items
        @ self_make_empty_block_dict
        @ set_block_item
        set_dict_key2default
        set_fdefault
        setdefault
        @ swap
        total_dict_key_ops
        update
        update_from_block_items
        update_from_items

old_methods:
        __bool__
        __contains__
        __delitem__
        __eq__
        __getitem__
        __hash__
        __ne__
        __setitem__
        assign
        block_dict_key_ops
        block_key2block_items
        block_key2iter_block_items
        dict_key2block_items
        dict_value_eq
        eq_dict_value_ops
        get
        get_block_dict_key_ops
        get_eq_dict_value_ops
        get_total_dict_key_ops
        is_exactly_block_key
        is_one_piece_block_key
        iter_block_keys
        iter_dict_values
        list_all_touch_or_overlap_block_items
        mkSingletonRange
        pop
        pop_block_item
        pop_block_item_of_dict_key
        pop_block_items_of_dict_key
        pop_left_block_item
        pop_right_block_item
        self_make_block_dict_from_block_items
        self_make_block_dict_from_items
        set_dict_key2default
        set_fdefault
        setdefault
        total_dict_key_ops
        update
        update_from_block_items
        update_from_items



'''

    '''
    @property
    def __tree(self):
        return self._BlockDict__tree
    @__tree.setter
    def __tree(self, tree):
        self._BlockDict__tree = tree
    '''

    def __bool__(self):
        return not self.block_dict_ops.is_empty(self.__tree)
    def __contains__(self, dict_key):
        return self.block_dict_ops.contains_dict_key(self.__tree, dict_key)
    def __delitem__(self, dict_key):
        self.__tree = self.block_dict_ops.idel_item(self.__tree, dict_key)
    def __eq__(self, other):
        return (type(self) is type(other)
            and self.block_dict_ops == other.block_dict_ops
            and self.block_dict_ops.block_dict_eq(self.__tree, other.__tree)
            )
    def __getitem__(self, dict_key):
        return self.block_dict_ops.dict_key2dict_value(self.__tree, dict_key)
    def __setitem__(self, dict_key, dict_value):
        self.__tree = self.block_dict_ops.iset_item(self.__tree, dict_key, dict_value)
    def assign(self, other):
        if type(self) is not type(other): raise TypeError
        if self.block_dict_ops != other.block_dict_ops: raise TypeError
        self.__tree = self.block_dict_ops.copy_block_dict(other.__tree)

    @property
    def block_dict_key_ops(self):
        return self.block_dict_ops.block_dict_key_ops
    def block_key2block_items(self, block_key, *, reverse=False):
        return self.block_dict_ops.block_key2block_items(self.__tree, block_key, reverse=reverse)

    def block_key2iter_block_items(self, block_key, *, reverse=False):
        return self.block_dict_ops.block_key2iter_block_items(self.__tree, block_key, reverse=reverse)
    def dict_key2block_items(self, dict_key):
        return self.block_dict_ops.dict_key2block_items(self.__tree, dict_key)

    @property
    def dict_value_eq(self):
        return self.block_dict_ops.dict_value_eq
    @property
    def eq_dict_value_ops(self):
        return self.block_dict_ops.eq_dict_value_ops
    def get(self, dict_key, default=None):
        return self.block_dict_ops.getdefault(self.__tree, dict_key, default)
    def get_block_dict_key_ops(self):
        return self.block_dict_ops.block_dict_key_ops
    def get_eq_dict_value_ops(self):
        return self.block_dict_ops.eq_dict_value_ops
    def get_total_dict_key_ops(self):
        return self.block_dict_ops.total_dict_key_ops

    def is_exactly_block_key(self, block_key):
        return self.block_dict_ops.is_exactly_block_key(self.__tree, block_key)
    def is_one_piece_block_key(self, block_key):
        return self.block_dict_ops.is_one_piece_block_key(self.__tree, block_key)

    def iter_block_keys(self, *, reverse=False):
        return self.block_dict_ops.iter_block_keys(self.__tree, reverse=reverse)
    def iter_dict_values(self, *, reverse=False):
        return self.block_dict_ops.iter_dict_values(self.__tree, reverse=reverse)



    def list_all_touch_or_overlap_block_items(self, block_key
            , overlap_only:bool, *, reverse=False):
        return self.block_dict_ops.list_all_touch_or_overlap_block_items(self.__tree, block_key, overlap_only, reverse=reverse)
    @property
    def mkSingletonRange(self):
        return self.block_dict_ops.block_dict_key_ops.mkSingletonRange
    def pop(self, *args):
        e, self.__tree = self.block_dict_ops.ipop(self.__tree, *args)
        return e
    def pop_block_item(self):
        e, self.__tree = self.block_dict_ops.ipop_block_item(self.__tree)
        return e
    def pop_block_item_of_dict_key(self, dict_key):
        e, self.__tree = self.block_dict_ops.ipop_block_item_of_dict_key(self.__tree, dict_key)
        return e
    def pop_block_items_of_dict_key(self, dict_key):
        e, self.__tree = self.block_dict_ops.ipop_block_items_of_dict_key(self.__tree, dict_key)
        return e
    def pop_left_block_item(self):
        e, self.__tree = self.block_dict_ops.ipop_left_block_item(self.__tree)
        return e
    def pop_right_block_item(self):
        e, self.__tree = self.block_dict_ops.ipop_right_block_item(self.__tree)
        return e
    def self_make_block_dict_from_block_items(self, block_items):
        other = self.self_make_empty_block_dict()
        other.__tree = self.block_dict_ops.make_block_dict_from_block_items(block_items)
        return other
    def self_make_block_dict_from_items(self, items):
        other = self.self_make_empty_block_dict()
        other.__tree = self.block_dict_ops.make_block_dict_from_items(items)
        return other
    def set_dict_key2default(self, dict_key, dict_key2default):
        v, self.__tree = self.block_dict_ops.iset_dict_key2default(self.__tree, dict_key, dict_key2default)
        return v
    def set_fdefault(self, dict_key, fdefault):
        v, self.__tree = self.block_dict_ops.iset_fdefault(self.__tree, dict_key, fdefault)
        return v
    def setdefault(self, dict_key, default):
        # default must be dict_value; so no(default=None)
        v, self.__tree = self.block_dict_ops.isetdefault(self.__tree, dict_key, default)
        return v

    @property
    def total_dict_key_ops(self):
        return self.block_dict_ops.total_dict_key_ops
    #def update(self, other_or_items):
    def update_from_block_items(self, block_items):
        self.__tree = self.block_dict_ops.iupdate_from_block_items(self.__tree, block_items)
    def update_from_items(self, items):
        self.__tree = self.block_dict_ops.iupdate_from_items(self.__tree, items)




if __name__ == "__main__":
    import doctest
    doctest.testmod()
