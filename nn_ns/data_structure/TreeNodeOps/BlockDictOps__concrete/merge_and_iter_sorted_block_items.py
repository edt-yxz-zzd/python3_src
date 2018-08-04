
__all__ = '''
    merge_and_iter_sorted_block_items
    '''.split()

from .BlockDictOps__for_KeyOrderedRedBlackTreeNodeOps__sized_immutable import \
    BlockDictOps__for_KeyOrderedRedBlackTreeNodeOps__sized_immutable as BD_Ops



def merge_and_iter_sorted_block_items(
        block_dict_key_ops, eq_dict_value_ops
        , iterable, is_block_items:bool
        , *, reverse=False):
    '''
input:
        default = echo
    iterable :: Iter item | Iter block_item
        if is_block_items:
            iterable :: Iter block_item
        else:
            iterable :: Iter item
    is_block_items :: bool
    reverse :: bool = False
        whether the result is reversed
output:
    result :: (Iterator block_item) # sorted if not reverse else reversed

'''
    reverse = bool(reverse)
    ops = BD_Ops(block_dict_key_ops, eq_dict_value_ops)
    block_dict = ops.make_block_dict_from_iterable(iterable, is_block_items)
    return ops.iter_block_items(block_dict, reverse=reverse)
