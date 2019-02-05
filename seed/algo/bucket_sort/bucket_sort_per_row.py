
r'''
bucket_sort_per_row
    :: [unsorted[UInt]] -> [sorted[UInt]]
    :: row2unsorted_uints -> row2sorted_uints
    :: row2unsorted_objects -> row2sorted_objects

seed.algo.bucket_sort.bucket_sort_per_row
    vs nn_ns.graph2.bucket_sort.inplace_bucket_sort
    non-inplace vs inplace


'''


__all__ = '''
    bucket_sort_per_row
    '''.split()

from .bucket_sort_with_table import bucket_sort_with_table__easy
from seed.tiny import echo, snd

def bucket_sort_per_row(
    alphabet_size
    ,row2unsorted_objects
    ,maybe_table
    , *, key=None, reverse=False
    ):
    r'''
input:
    alphabet_size :: UInt
    row2unsorted_objects :: [unsorted[a]]
    maybe_table :: None | [empty_mutable[?]]
    key :: None | (a -> UInt)
        default = None
        if key is None:
            a is UInt
    reverse :: bool
        default = False
'''
    if maybe_table is None:
        table = [[] for _ in range(alphabet_size)]
    else:
        table = maybe_table
        if len(table) < alphabet_size:
            table.extend([] for _ in range(alphabet_size - len(table)))

    assert len(table) >= alphabet_size
    assert not any(table[:alphabet_size])
        # all empty

    iter_pairs = ((row, obj)
        for row, unsorted_objects in enumerate(row2unsorted_objects)
        for obj in unsorted_objects
        )
    if key is None:
        key = echo

    may_wheres = None
    ordered_pairs = bucket_sort_with_table__easy(
        alphabet_size, iter_pairs, may_wheres, table
        ,key=lambda pair: key(snd(pair))
        ,reverse=reverse
        )

    num_rows = len(row2unsorted_objects)
    row2sorted_objects = [[] for _ in range(num_rows)]
    for row, obj in ordered_pairs:
        row2sorted_objects[row].append(obj)
    row2sorted_objects = tuple(map(tuple, row2sorted_objects))
    return row2sorted_objects



