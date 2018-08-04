

'''
BlockDict2 == BlockDict__ops_biased
    imple all methods using ops version instead of inherit from IBlockDict
        to test the ops class

###################################


'''
__all__ = '''
    BlockDict__ops_biased
    '''.split()

from ..BlockDict.IBlockDict_by_BlockDictOps__imodify__ops_biased import \
    IBlockDict_by_BlockDictOps__imodify__ops_biased
from .BlockDict import __doc__ as _doc, BlockDict as BlockDict1


#__doc__ = '\n\n'.join([__doc__, BlockDict1.__doc__, _doc]
__doc__ = '\n\n'.join([__doc__, BlockDict1.__doc__, _doc])
    # now BlockDict1.__doc__ contains no examples

#print('\n'*10)
#__doc__ = '\n'.join(__doc__.split('\n')[:600])




class BlockDict(
    IBlockDict_by_BlockDictOps__imodify__ops_biased, BlockDict1):
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
        discard_block_key
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
        @ discard_block_key
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
    __slots__ = ()

    '''
    @property
    def __tree(self):
        return self._BlockDict__tree
    @__tree.setter
    def __tree(self, tree):
        self._BlockDict__tree = tree
    '''
BlockDict__ops_biased = BlockDict2 = BlockDict


if __name__ == "__main__":
    XXX = BlockDict__ops_biased

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

