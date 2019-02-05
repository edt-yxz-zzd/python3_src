
__all__ = '''
    reindex_complex_colors
    reindex_complex_colors_of_ordered_columns
    reindex_complex_colors__old_color_sequence
    reindex_complex_colors__old_color_tuple
    '''.split()

from seed.iters.group_by_eq import group_by_eq
from .imports__bucket_sort import (
    bucket_sort_per_row
    ,bucket_sort4uint_seq
    ,radix_sort
    )

def reindex_complex_colors(column2complex_color, sort, *, __eq__=None):
    '''
reindex_complex_colors
    :: [complex_color]
    -> (Iter a -> (a -> complex_color) -> [a])
    -> (complex_color -> complex_color -> Bool)
    -> (UInt, [NewColor], [complex_color])
        where Column = UInt = NewColor

input:
    column2complex_color :: [complex_color]
        seq, not func
    sort :: (Iter a -> (key :: a -> complex_color) -> [a])
    __eq__ :: None | (complex_color -> complex_color -> Bool)
output:
    (num_new_colors, column2new_color, new_color2complex_color)
        num_new_colors :: UInt
        column2new_color :: [NewColor]
        new_color2complex_color :: [complex_color]

example:
    >>> this = reindex_complex_colors
    >>> type2int = {int:0, str:1, list:2}
    >>> sort = lambda iterable, *, key: sorted(iterable, key=lambda a: type2int[type(key(a))])
    >>> this([0,1,'2',[3],4,[5]], sort, __eq__=lambda a,b:type(a) is type(b))
    (3, (0, 0, 1, 2, 0, 2), (0, '2', [3]))

'''
    num_columns = len(column2complex_color)
    key = lambda i: column2complex_color[i]
    ordered_columns = sort(range(num_columns), key=key)

    (num_new_colors, column2new_color, new_color2complex_color
    ) = reindex_complex_colors_of_ordered_columns(
        ordered_columns, key, __eq__=__eq__)
    return (num_new_colors, column2new_color, new_color2complex_color)

def reindex_complex_colors_of_ordered_columns(
    ordered_columns, column2complex_color
    , *, __eq__=None
    ):
    '''
reindex_complex_colors_of_ordered_columns
    :: [Column]
    -> (Column -> complex_color)
    -> (complex_color -> complex_color -> Bool)
    -> (UInt, [NewColor], [complex_color])
        where Column = UInt = NewColor

input:
    ordered_columns :: Iter Column
        NOTE: sorted by complex_color instead of column
    column2complex_color :: Column -> complex_color
        func, not seq
    __eq__ :: None | (complex_color -> complex_color -> Bool)
output:
    (num_new_colors, column2new_color, new_color2complex_color)
        num_new_colors :: UInt
        column2new_color :: [NewColor]
        new_color2complex_color :: [complex_color]

example:
    >>> this = reindex_complex_colors_of_ordered_columns
    >>> this(iter([0,1,4,2,3,5]), [0,1,'2',[3],4,[5]].__getitem__, __eq__=lambda a,b:type(a) is type(b))
    (3, (0, 0, 1, 2, 0, 2), (0, '2', [3]))
'''
    assert callable(column2complex_color)

    ordered_columns = iter(ordered_columns)
    [*keyed_group_pairs] = group_by_eq(
        ordered_columns, key=column2complex_color, __eq__=__eq__)

    # num_columns = len(ordered_columns)
    num_columns = sum(len(g) for k, g in keyed_group_pairs)
    column2new_color = [None]*num_columns
    new_color2complex_color = []
    for new_color, (complex_color, columns) in enumerate(keyed_group_pairs):
        new_color2complex_color.append(complex_color)
        for column in columns:
            column2new_color[column] = new_color

    if any(c is None for c in column2new_color):
        raise ValueError('ordered_columns is bad (not permutation of [0..len(ordered_columns)-1])')

    num_new_colors = len(keyed_group_pairs)
    column2new_color = tuple(column2new_color)
    new_color2complex_color = tuple(new_color2complex_color)
    return num_new_colors, column2new_color, new_color2complex_color


def reindex_complex_colors__old_color_sequence(
    num_old_colors
    ,column2old_color_sequence
    ,*
    ,ordered : bool
    ):
    '''
reindex_complex_colors__old_color_sequence
    :: UInt -> [[OldColor]] -> (ordered::Bool)
    -> (UInt, [NewColor], [ordered[OldColor]])
    # ordered is not sorted
    #   if ordered == False: ordered is sorted
    #   else: ordered means merely-keeping-input-order

complex_color :: [OldColor]
    complex_color = old_color_sequence # old_color_multiset
    OldColor = UInt

input:
    num_old_colors :: UInt
    column2old_color_sequence :: [[OldColor]]
    ordered :: Bool
        if ordered == False:
            require to sort input old_color_sequence
            i.e. treat old_color_sequence as old_color_multiset
output:
    num_new_colors :: UInt
    column2new_color :: [NewColor]
    new_color2ordered_old_color_sequence :: [ordered[OldColor]]

example:
    >>> this = reindex_complex_colors__old_color_sequence
    >>> this(3, [[2,1], [1,2], [1,2,1], [2,1,1]], ordered=True)
    (4, (2, 0, 1, 3), ([1, 2], [1, 2, 1], [2, 1], [2, 1, 1]))
    >>> this(3, [[2,1], [1,2], [1,2,1], [2,1,1]], ordered=False)
    (2, (1, 1, 0, 0), ((1, 1, 2), (1, 2)))
'''
    # ordered neednot sorted
    if ordered:
        column2ordered_old_color_sequence = column2old_color_sequence
    else:
        (column2ordered_old_color_sequence
        ) = bucket_sort_per_row(
            num_old_colors, column2old_color_sequence, None)
    del column2old_color_sequence
    del ordered

    num_columns = len(column2ordered_old_color_sequence)
    key = column2ordered_old_color_sequence.__getitem__
    (ordered_columns
    ) = bucket_sort4uint_seq(
        num_old_colors, range(num_columns), key=key)


    (num_new_colors
    ,column2new_color
    ,new_color2ordered_old_color_sequence
    ) = reindex_complex_colors_of_ordered_columns(
        ordered_columns, key)
    return (num_new_colors, column2new_color, new_color2ordered_old_color_sequence)


def reindex_complex_colors__old_color_tuple(
    old_color_sizes
    ,column2old_color_tuple
    ):
    '''
reindex_complex_colors__old_color_tuple
    :: [UInt] -> [[OldColor<i>]]
    -> (UInt, [NewColor], [[OldColor<i>]])

complex_color :: [OldColor<i>]
    complex_color = old_color_tuple
    OldColor<i> = UInt[0..old_color_sizes[i]]

input:
    old_color_sizes :: [UInt]
    column2old_color_tuple :: [[OldColor<i>]]
output:
    num_new_colors :: UInt
    column2new_color :: [NewColor]
    new_color2old_color_tuple :: [[OldColor<i>]]

example:
    >>> this = reindex_complex_colors__old_color_tuple
    >>> this([3,6], [(1,1), (2,1), (2,1), (1,1), (1,5)])
    (3, (0, 2, 2, 0, 1), ((1, 1), (1, 5), (2, 1)))
'''
    num_columns = len(column2old_color_tuple)
    key = column2old_color_tuple.__getitem__
    ordered_columns = radix_sort(old_color_sizes, range(num_columns), key=key)

    (num_new_colors, column2new_color, new_color2old_color_tuple
    ) = reindex_complex_colors_of_ordered_columns(ordered_columns, key)

    return (num_new_colors, column2new_color, new_color2old_color_tuple)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


