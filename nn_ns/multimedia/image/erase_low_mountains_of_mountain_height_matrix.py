
'''
mountain_height_matrix
erase_low_mountains_of_mountain_height_matrix
'''

__all__ = '''
    erase_low_mountains_of_mountain_height_matrix

    IEraseLowMountainsOfMountainHeightMatrix
        EraseLowMountainsOfMountainHeightMatrix
    '''.split()




from .iter_all_local_max_positions_of_mountain_height_matrix import (
    IFindAllLocalMaxPositionsOfMountainHeightMatrix
    ,FindAllLocalMaxPositionsOfMountainHeightMatrix
    )

def erase_low_mountains_of_mountain_height_matrix(
    *, inout_matrix, num_rows, num_columns, min_height, case:'8|4'
    ):
    '''
example:
    >>> this_func = erase_low_mountains_of_mountain_height_matrix
    >>> IO = inout_matrix = [[0, 1, 0, 1], [1, 1, 1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1, 1, 1]]
    >>> R = num_rows = 5
    >>> C = num_columns = 4
    >>> this_func(inout_matrix=IO, num_rows=R, num_columns=C, min_height=2, case=8)
    >>> IO
    [[0, 0, 0, 0], [1, 1, 1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1, 1, 1]]

'''
    (aEraseLowMountainsOfMountainHeightMatrix
    ) = EraseLowMountainsOfMountainHeightMatrix(case=case)
    return (aEraseLowMountainsOfMountainHeightMatrix
        .erase_low_mountains_of_mountain_height_matrix(
            inout_matrix=inout_matrix
            ,num_rows=num_rows
            ,num_columns=num_columns
            ,min_height=min_height
        ))
class IEraseLowMountainsOfMountainHeightMatrix(
    IFindAllLocalMaxPositionsOfMountainHeightMatrix
    ):
    __slots__ = ()
    def erase_low_mountains_of_mountain_height_matrix(
        self, *, inout_matrix, num_rows, num_columns, min_height
        ):
        it = self.iter_all_local_max_positions_of_mountain_height_matrix(
            inout_matrix, num_rows=num_rows, num_columns=num_columns)

        def delete(i, j):
            if inout_matrix[i][j] == 0: return
            inout_matrix[i][j] = 0
            it = self.iter_neighbours_of_ex(
                i, j, num_rows=num_rows, num_columns=num_columns)
            idx_pairs.extend(it)

        idx_pairs = []
        for i, j in it:
            if inout_matrix[i][j] < min_height:
                delete(i,j)

        while idx_pairs:
            tmp = idx_pairs
            idx_pairs = []
            for i, j in tmp:
                height = inout_matrix[i][j]
                if height >= min_height or height == 0: continue

                it = self.iter_neighbours_of_ex(
                    i, j, num_rows=num_rows, num_columns=num_columns)
                M = max(inout_matrix[i_][j_] for i_, j_ in it)
                if height >= M:
                    delete(i,j)
        return None

class EraseLowMountainsOfMountainHeightMatrix(
    FindAllLocalMaxPositionsOfMountainHeightMatrix
    ,IEraseLowMountainsOfMountainHeightMatrix
    ):
    pass



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


