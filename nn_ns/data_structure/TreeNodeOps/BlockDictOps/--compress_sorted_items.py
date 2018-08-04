

ensure_sorted
fst
def compress_sorted_items(block_dict_key_ops, eq_dict_value_ops, items, *, reverse=False):
    '''(Sorted | Reversed)<Iter (dict_key, dict_value)> -> Sorted (Range, dict_value)

input:
    block_dict_key_ops :: IBlockDictKeyOps<dict_key>
    eq_dict_value_ops :: None | IEqOps<dict_value>
        default = python_eq_key_ops
'''
    if not isinstance(block_dict_key_ops, IBlockDictKeyOps): raise TypeError
    if eq_dict_value_ops is None:
        eq_dict_value_ops = python_eq_key_ops
    elif not isinstance(eq_dict_value_ops, IEqOps): raise TypeError

    total_dict_key_ops = block_dict_key_ops.total_key_ops
    items = ensure_sorted(items, key=fst, before=total_dict_key_ops.le, reverse=reverse)

    dict_value_eq = eq_dict_value_ops.eq
    if not reverse:
        return __compress_sorted_items(
                block_dict_key_ops, dict_value_eq, items)
    else:
        return __compress_reversed_sorted_items(
                block_dict_key_ops, dict_value_eq, items)
    pass

def __compress_sorted_items(block_dict_key_ops, dict_value_eq, items):
    it = iter(items); del items
    for prev_dict_key, prev_dict_value in it:
        break
    else:
        # yield nothing
        return

    mkTheKey = block_dict_key_ops.mkTheKey

    prev_left_bound = mkTheKey(prev_dict_key)
    prev_right_bound = prev_left_bound

    for dict_key, dict_value in it:
        if dict_value_eq(prev_dict_value, dict_value):
            

def __compress_reversed_sorted_items(block_dict_key_ops, dict_value_eq, items):
    it = iter(items); del items

