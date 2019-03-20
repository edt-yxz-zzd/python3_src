
__all__ = '''
    iter_all_local_max_positions_of_mountain_height_matrix

    IFindAllLocalMaxPositionsOfMountainHeightMatrix
        FindAllLocalMaxPositionsOfMountainHeightMatrix
    '''.split()

'''
        FindAllLocalMaxPositionsOfMountainHeightMatrix__8
            aFindAllLocalMaxPositionsOfMountainHeightMatrix__8
        FindAllLocalMaxPositionsOfMountainHeightMatrix__4
            aFindAllLocalMaxPositionsOfMountainHeightMatrix__4
'''



from .IIterNeighboursOf import (
    IIterNeighboursOf
    , IterNeighboursOf__8, IterNeighboursOf__4
    , IterNeighboursOf
    )

class IFindAllLocalMaxPositionsOfMountainHeightMatrix(IIterNeighboursOf):
    'position of local_max of mountain_height_matrix'
    __slots__ = ()
    def is_local_max_position_of_mountain_height_matrix(
        self, matrix, i, j, *, num_rows, num_columns
        ):
        height = matrix[i][j]
        it = self.iter_neighbours_of_ex(
            i, j, num_rows=num_rows, num_columns=num_columns)
        M = max(matrix[i][j] for i, j in it)
        return height >= M

    def iter_all_local_max_positions_of_mountain_height_matrix(
        self, matrix, *, num_rows, num_columns
        ):
        '-> Iter (i,j)'
        f = self.is_local_max_position_of_mountain_height_matrix
        for i in range(num_rows):
            for j in range(num_columns):
                if f(matrix, i, j, num_rows=num_rows, num_columns=num_columns):
                    yield (i, j)

    def find_all_local_max_positions_of_mountain_height_matrix(
        self, matrix, *, num_rows, num_columns
        ):
        '-> [(i,j)]'
        it = self.iter_all_local_max_positions_of_mountain_height_matrix(
            i, j, num_rows=num_rows, num_columns=num_columns)
        return list(it)

'''
class FindAllLocalMaxPositionsOfMountainHeightMatrix__8(
    IterNeighboursOf__8
    ,IFindAllLocalMaxPositionsOfMountainHeightMatrix):
    __slots__ = ()
class FindAllLocalMaxPositionsOfMountainHeightMatrix__4(
    IterNeighboursOf__4
    ,IFindAllLocalMaxPositionsOfMountainHeightMatrix):
    __slots__ = ()

aFindAllLocalMaxPositionsOfMountainHeightMatrix__4 = FindAllLocalMaxPositionsOfMountainHeightMatrix__4()
aFindAllLocalMaxPositionsOfMountainHeightMatrix__8 = FindAllLocalMaxPositionsOfMountainHeightMatrix__8()
'''


class FindAllLocalMaxPositionsOfMountainHeightMatrix(
    IterNeighboursOf
    ,IFindAllLocalMaxPositionsOfMountainHeightMatrix):
    pass

'''
__d = {8:aFindAllLocalMaxPositionsOfMountainHeightMatrix__8
    ,4:aFindAllLocalMaxPositionsOfMountainHeightMatrix__4
    }
'''

def iter_all_local_max_positions_of_mountain_height_matrix(
    matrix, *, num_rows, num_columns, case:'8|4'
    ):
    '''
example:
    >>> this_func = iter_all_local_max_positions_of_mountain_height_matrix
    >>> list(this_func([[1,1,1,1], [1,2,1,1], [0,1,1,0]], num_rows=3, num_columns=4, case=8))
    [(0, 3), (1, 1), (1, 3)]

    >>> I = matrix = [[0, 1, 0, 1], [1, 1, 1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1, 1, 1]]
    >>> R = num_rows = 5
    >>> C = num_columns = 4
    >>> list(this_func(I, num_rows=R, num_columns=C, case=8))
    [(0, 1), (0, 3), (2, 1), (2, 2), (3, 1), (3, 2)]

'''
    #aFindAllLocalMaxPositionsOfMountainHeightMatrix = __d[case]
    (aFindAllLocalMaxPositionsOfMountainHeightMatrix
    ) = FindAllLocalMaxPositionsOfMountainHeightMatrix(case=case)
    return (aFindAllLocalMaxPositionsOfMountainHeightMatrix
            .iter_all_local_max_positions_of_mountain_height_matrix(
            matrix, num_rows=num_rows, num_columns=num_columns
            )
        )



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


