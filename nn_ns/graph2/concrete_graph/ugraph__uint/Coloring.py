
r'''
CompactRecoloring vs RowColoring vs Serialization
    CompactRecoloring(num_old_colors, compact_new_color2old_color)
    RowColoring(num_colors, column2color)
    Serialization(upper_bound, serialization)
    diff:
        * 1
            compact_new_color2old_color is injection
            column2color may not
            serialization may not
        * 2
            num_new_colors <= num_old_colors
            num_colors <= num_columns
            no requirements between upper_bound and len(serialization)

>>> Serialization(upper_bound=6, serialization=[5])
Serialization(upper_bound=6, serialization=[5])
>>> Serialization(upper_bound=1, serialization=[0, 0])
Serialization(upper_bound=1, serialization=[0, 0])
>>> CompactRecoloring(num_old_colors=6, compact_new_color2old_color=[5])
CompactRecoloring(num_old_colors=6, compact_new_color2old_color=[5])
>>> RowColoring(num_colors=1, column2color=[0, 0])
RowColoring(num_colors=1, column2color=[0, 0])
>>> TableColoring(num_colors=1, row2column2color=[[], [0, 0]])
TableColoring(num_colors=1, row2column2color=[[], [0, 0]])


>>> make_rowcoloring_from_color2columns(num_columns=5, color2columns=[[], [1,2], [0,3,4]])
RowColoring(num_colors=3, column2color=(2, 1, 1, 2, 2))

'''


__all__ = '''
    Serialization
    CompactRecoloring
    RowColoring
    TableColoring

    make_rowcoloring_from_color2columns
    make_column2color_from_color2columns
    '''.split()

from seed.types.ImmutableNamespaceBase import ImmutableNamespaceBase
from seed.verify.common_verify import is_UInt, is_Sequence
from seed.iters.is_sorted import is_strict_sorted
from .is_uint_sequence import is_uint_sequence

from itertools import chain

def is_strictly_increasing(iterable):
    return is_strict_sorted(iterable)

class Serialization(ImmutableNamespaceBase
    , ordered_attr_name_seq = '''
        upper_bound
        serialization
        '''.split()
    ):
    def __init__(self, *, upper_bound, serialization):
        if not is_UInt(upper_bound): raise TypeError
        if not is_uint_sequence(serialization): raise TypeError
        if not max(serialization, default=-1) < upper_bound: raise ValueError
        super().__init__(upper_bound = upper_bound, serialization = serialization)


class CompactRecoloring(ImmutableNamespaceBase
    , ordered_attr_name_seq = '''
        num_old_colors
        compact_new_color2old_color
        '''.split()
    ):
    '''compact_new_color2old_color # injection, strictly_increasing
num_new_colors <= num_old_colors

'''
    def __init__(self, *, num_old_colors, compact_new_color2old_color):
        if not is_UInt(num_old_colors): raise TypeError
        if not is_uint_sequence(compact_new_color2old_color): raise TypeError
        if not max(compact_new_color2old_color, default=-1) < num_old_colors: raise ValueError
        if not is_strictly_increasing(compact_new_color2old_color):raise ValueError
        num_new_colors = len(compact_new_color2old_color)
        if not num_new_colors <= num_old_colors: raise ValueError
        super().__init__(num_old_colors = num_old_colors, compact_new_color2old_color = compact_new_color2old_color)



class RowColoring(ImmutableNamespaceBase
    , ordered_attr_name_seq = '''
        num_colors
        column2color
        '''.split()
    ):
    '''
column2color
num_colors <= num_columns
'''
    def __init__(self, *, num_colors, column2color):
        if not is_UInt(num_colors): raise TypeError
        if not is_uint_sequence(column2color): raise TypeError
        if not max(column2color, default=-1) < num_colors: raise ValueError
        num_columns = len(column2color)
        if not num_colors <= num_columns: raise ValueError
        super().__init__(num_colors = num_colors, column2color = column2color)


class TableColoring(ImmutableNamespaceBase
    , ordered_attr_name_seq = '''
        num_colors
        row2column2color
        '''.split()
    ):
    '''
row2column2color
num_colors <= sum(map(len, row2column2color))
'''
    def __init__(self, *, num_colors, row2column2color):
        if not is_UInt(num_colors): raise TypeError
        if not is_Sequence.of(row2column2color, is_uint_sequence): raise TypeError
        if not max(chain.from_iterable(row2column2color), default=-1) < num_colors: raise ValueError
        num_elements = sum(map(len, row2column2color))
        if not num_colors <= num_elements: raise ValueError
        super().__init__(num_colors = num_colors, row2column2color = row2column2color)


def make_rowcoloring_from_color2columns(num_columns, color2columns):
    column2color = make_column2color_from_color2columns(num_columns, color2columns)
    num_colors = len(color2columns)
    rowcoloring = RowColoring(num_colors=num_colors, column2color=column2color)
    return rowcoloring

def make_column2color_from_color2columns(num_columns, color2columns):
    # color2columns -> column2color
    # [[column]] -> [color]
    # [[UInt]] -> [UInt]
    column2color = [None]*num_columns
    for color, columns in enumerate(color2columns):
        for column in columns:
            if column2color[column] is not None: raise ValueError('duplicated column')
            column2color[column] = color
    if any(c is None for c in column2color): raise ValueError('missing column')
    return tuple(column2color)




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):



