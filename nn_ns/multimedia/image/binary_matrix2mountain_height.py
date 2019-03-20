
'''
numpy ops:
    # image_PIL -> array
        greys = numpy.asarray(image_PIL.convert('L'))

    # array -> matrix
    # mx.reshape(num_rows, num_columns)
        greys = greys.reshape(image_PIL.height, image_PIL.width)

    # change matrix.dtype
        matrix.astype(numpy.uint8)
        matrix.astype(numpy.int_)
        matrix.astype(int)
        matrix.floor(matrix)

    # matrix -> image_PIL
        PIL.Image.fromarray(matrix.astype(numpy.uint8))


'''


__all__ = '''
    binary_matrix2mountain_height

    IBinaryMatrix2MountainHeight
        BinaryMatrix2MountainHeight
    '''.split()


'''
    iter_neighbours_of__prime
    iter_neighbours_of_ex

        BinaryMatrix2MountainHeight__8
            aBinaryMatrix2MountainHeight__8
        BinaryMatrix2MountainHeight__4
            aBinaryMatrix2MountainHeight__4
'''

from .IIterNeighboursOf import (
    IIterNeighboursOf
    , IterNeighboursOf__8, IterNeighboursOf__4
    , IterNeighboursOf
    )

def binary_matrix2mountain_height(*
    ,input_binary_matrix
    ,output_uint_matrix
    ,num_rows
    ,num_columns
    ,case:'8|4'
    ):
    '''
example:
    >>> I = input_binary_matrix = [[0,1,0,1], [1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
    >>> O = output_uint_matrix = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    >>> R = num_rows = 5
    >>> C = num_columns = 4
    >>> binary_matrix2mountain_height(input_binary_matrix=I, output_uint_matrix=O, num_rows=R, num_columns=C, case=8)
    >>> output_uint_matrix
    [[0, 1, 0, 1], [1, 1, 1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1, 1, 1]]
'''
    '''
    if case == 8:
        aBinaryMatrix2MountainHeight = aBinaryMatrix2MountainHeight__8
    elif case == 4:
        aBinaryMatrix2MountainHeight = aBinaryMatrix2MountainHeight__4
    else:
        raise Exception(f'unknown case: {case!r}')
    '''
    aBinaryMatrix2MountainHeight = BinaryMatrix2MountainHeight(case=case)

    aBinaryMatrix2MountainHeight.binary_matrix2mountain_height(
        input_binary_matrix=input_binary_matrix
        ,output_uint_matrix=output_uint_matrix
        ,num_rows=num_rows
        ,num_columns=num_columns
        )


class IBinaryMatrix2MountainHeight(IIterNeighboursOf):
    __slots__ = ()
    def binary_matrix2mountain_height(self, *
        ,input_binary_matrix
        ,output_uint_matrix
        ,num_rows
        ,num_columns
        ):
        assert not any(output_uint_matrix[i][j] for i in range(num_rows) for j in range(num_columns))

        def f(i, j):
            if not input_binary_matrix[i][j]:
                output_uint_matrix[i][j] = 0
                return
            if i == 0 or j == 0 or i == num_rows-1 or j == num_columns-1:
                m = 0
            else:
                m = min(output_uint_matrix[i_][j_]
                    for i_, j_ in self.iter_neighbours_of__prime(i, j))

            result = m+1
            if output_uint_matrix[i][j] == result:
                return

            output_uint_matrix[i][j] = result
            idx_pairs.extend(self.iter_neighbours_of_ex(i,j
                , num_rows=num_rows, num_columns=num_columns))


        idx_pairs = []
        for i in range(num_rows):
          for j in range(num_columns):
            f(i, j)

        while idx_pairs:
            tmp = idx_pairs
            idx_pairs = []
            for i, j in tmp:
                f(i, j)
# end IBinaryMatrix2MountainHeight

'''
class BinaryMatrix2MountainHeight__8(
    IterNeighboursOf__8, IBinaryMatrix2MountainHeight):
    __slots__ = ()
class BinaryMatrix2MountainHeight__4(
    IterNeighboursOf__4, IBinaryMatrix2MountainHeight):
    __slots__ = ()

aBinaryMatrix2MountainHeight__8 = BinaryMatrix2MountainHeight__8()
aBinaryMatrix2MountainHeight__4 = BinaryMatrix2MountainHeight__4()
'''


class BinaryMatrix2MountainHeight(
    IterNeighboursOf, IBinaryMatrix2MountainHeight):
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):

if __name__ == "__main__":
    pass

