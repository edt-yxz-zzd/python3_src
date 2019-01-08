
r'''
locally_reindex_global_colors
    :: num_global_colors -> row2column2global_color
    -> (row2num_local_colors, row2column2local_color, row2local_color2global_color)

locally_reindex_global_colors__depth
    :: num_global_colors -> depth2row2column2global_color
    -> (depth2num_depth_local_colors, depth2row2column2depth_local_color, depth2depth_local_color2global_color)

locally_reindex_global_colors__virtual_row_layer
    :: num_global_colors -> row2column2global_color
    -> num_layers -> row2layer
    -> (layer2num_layer_local_colors, row2column2layer_local_color, layer2layer_local_color2global_color)


'''

__all__ = '''
    locally_reindex_global_colors
    locally_reindex_global_colors__depth
    locally_reindex_global_colors__virtual_row_layer
    '''.split()

from .imports__bucket_sort import bucket_sort




def locally_reindex_global_colors(*
    ,num_global_colors
    ,row2column2global_color
    ):
    '''
locally_reindex_global_colors
    :: num_global_colors -> row2column2global_color
    -> (row2num_local_colors, row2column2local_color, row2local_color2global_color)

time:
    O(num_global_colors + len(row2local_color2global_color) + sum(map(len, row2local_color2global_color)))

input:
    num_global_colors :: UInt
    row2column2global_color :: [[GlobalColor]]
        GlobalColor = UInt[0..num_global_colors-1]

output:
    row2num_local_colors :: [UInt]
    row2column2local_color :: [[LocalColor]]
        LocalColor[row] = UInt[0..row2num_local_colors[row]-1]
    row2local_color2global_color :: [[GlobalColor]]
        #row2palette == row2local_color2global_color


example:
    >>> this = lambda num_global_colors, row2column2global_color: locally_reindex_global_colors(num_global_colors=num_global_colors, row2column2global_color=row2column2global_color)
    >>> this(5, [[], [4,2], [1,2], [4,3,1], [0,1,1,0]])
    ((0, 2, 2, 3, 2), ((), (1, 0), (0, 1), (2, 1, 0), (0, 1, 1, 0)), ((), (2, 4), (1, 2), (1, 3, 4), (0, 1)))

'''
    assert all(0 <= c < num_global_colors for cs in row2column2global_color for c in cs)
    num_rows = len(row2column2global_color)

    def mk_iter():
        for row, column2global_color in enumerate(row2column2global_color):
            for column, global_color in enumerate(column2global_color):
                yield row, column, global_color

    ls = bucket_sort(num_global_colors, mk_iter(), key=lambda triple:triple[-1])
    #ls = bucket_sort(num_rows, ls, key=lambda triple:triple[0])
    #row2num_local_colors = [0]*num_rows
    row2local_color2global_color = [[] for _ in range(num_rows)]
    row2column2local_color = [[None]*num_columns for num_columns in map(len, row2column2global_color)]


    for row, column, global_color in ls:
        local_color2global_color = row2local_color2global_color[row]
        if global_color not in local_color2global_color[-1:]:
            local_color2global_color.append(global_color)
        local_color = len(local_color2global_color)-1
        row2column2local_color[row][column] = local_color
    assert all(c is not None for cs in row2column2local_color for c in cs)

    row2num_local_colors = tuple(map(len, row2local_color2global_color))
    row2column2local_color = tuple(map(tuple, row2column2local_color))
    row2local_color2global_color = tuple(map(tuple, row2local_color2global_color))
    return row2num_local_colors, row2column2local_color, row2local_color2global_color


def locally_reindex_global_colors__depth(*
    ,num_global_colors
    ,depth2row2column2global_color
    ):
    '''
locally_reindex_global_colors__depth
    :: num_global_colors -> depth2row2column2global_color
    -> (depth2num_depth_local_colors, depth2row2column2depth_local_color, depth2depth_local_color2global_color)

global_color
depth
    # depend on depth
        depth_local_color
        num_depth_local_colors
'''
    depth2idx2row_column_pair = []
    depth2idx2global_color = []
    for row2column2global_color in depth2row2column2global_color:
        idx2row_column_pair = []
        idx2global_color = []
        depth2idx2row_column_pair.append(idx2row_column_pair)
        depth2idx2global_color.append(idx2global_color)
        for row, column2global_color in enumerate(row2column2global_color):
            for column, global_color in enumerate(column2global_color):
                idx2row_column_pair.append((row, column))
                idx2global_color.append(global_color)

    #(row2num_local_colors, row2column2local_color, row2local_color2global_color)
    (depth2num_depth_local_colors
    ,depth2idx2depth_local_color
    ,depth2depth_local_color2global_color
    ) = locally_reindex_global_colors(
            num_global_colors=num_global_colors
            ,row2column2global_color=depth2idx2global_color
            )

    def mk_row2column2depth_local_color(idx2depth_local_color, idx2row_column_pair):
        row2column2depth_local_color = []
        prev_row, prev_column = -1, 0
        for depth_local_color, (row, column) in zip(idx2depth_local_color, idx2row_column_pair):
            if column == prev_column+1:
                assert row == prev_row
                prev_column = column
                column2depth_local_color.append(depth_local_color)
            elif row == prev_row+1:
                assert column == 0
                prev_column = 0
                prev_row = row
                column2depth_local_color = [depth_local_color]
                row2column2depth_local_color.append(column2depth_local_color)
        return tuple(map(tuple, row2column2depth_local_color))

    depth2row2column2depth_local_color = tuple(
        map(mk_row2column2depth_local_color
            , depth2idx2depth_local_color, depth2idx2row_column_pair)
        )
    return (depth2num_depth_local_colors, depth2row2column2depth_local_color, depth2depth_local_color2global_color)


def locally_reindex_global_colors__virtual_row_layer(*
    ,num_global_colors
    ,row2column2global_color
    ,num_layers
    ,row2layer
    ):
    '''

locally_reindex_global_colors__virtual_row_layer
    :: num_global_colors -> row2column2global_color
    -> num_layers -> row2layer
    -> (layer2num_layer_local_colors, row2column2layer_local_color, layer2layer_local_color2global_color)

global_color
layer
    # depend on layer
        layer_local_color
        num_layer_local_colors

'''
    layer2idx2column2global_color = [[] for _ in range(num_layers)]
    layer2idx2row = [[] for _ in range(num_layers)]
    for row, column2global_color in enumerate(row2column2global_color):
        layer = row2layer[row]

        idx2column2global_color = layer2idx2column2global_color[layer]
        idx2row = layer2idx2row[layer]

        idx2column2global_color.append(column2global_color)
        idx2row.append(row)

    #(depth2num_depth_local_colors, depth2row2column2depth_local_color, depth2depth_local_color2global_color)
    (layer2num_layer_local_colors
    ,layer2idx2column2layer_local_color
    ,layer2layer_local_color2global_color
    ) = locally_reindex_global_colors__depth(
        num_global_colors=num_global_colors
        ,depth2row2column2global_color=layer2idx2column2global_color
        )

    num_rows = len(row2column2global_color)
    row2column2layer_local_color = [None]*num_rows
    for idx2column2layer_local_color, idx2row in zip(layer2idx2column2layer_local_color, layer2idx2row):
        for column2layer_local_color, row in zip(idx2column2layer_local_color, idx2row):
            row2column2layer_local_color[row] = column2layer_local_color
    row2column2layer_local_color = tuple(row2column2layer_local_color)

    return (layer2num_layer_local_colors, row2column2layer_local_color, layer2layer_local_color2global_color)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):




