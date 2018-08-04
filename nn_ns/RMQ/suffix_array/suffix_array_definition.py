


def suffix_array_definition(array):
    ''':: Ord a => [a] -> [ArrayIdx]

an slow implement
time O(n^2 * log(n)) * a.'<'
    <<== O(n*log(n)) * [a].'<'

input:
    array :: Ord a => [a]
        let L = len(array)
output:
    suffix_array :: [ArrayIdx]
        # sorted_suffix_position2suffix_begin_idx
        # Map SortedPosition ArrayIdx
        # suffix_array is an uint_bijection_array
        ArrayIdx = UInt[0..L-1]
        SortedPosition = UInt[0..L-1]
        len(suffix_array) == L
        suffix_array = sorted(range(L), key=lambda i: array[i:])

see:
    seed.seq_tools.inverse_uint_bijection_array
        # the inverse of suffix_array is useful

example:
    >>> this = suffix_array_definition
    >>> this('')
    []
    >>> this('1')
    [0]
    >>> this('12')
    [0, 1]
    >>> this('21')
    [1, 0]
    >>> this('123')
    [0, 1, 2]
    >>> this('132')
    [0, 2, 1]
    >>> this('312')
    [1, 2, 0]
    >>> this('213')
    [1, 0, 2]
    >>> this('231')
    [2, 0, 1]
    >>> this('321')
    [2, 1, 0]
    >>> this('112233112233')
    [6, 0, 7, 1, 8, 2, 9, 3, 11, 5, 10, 4]
'''
    suffix_array = sorted(range(len(array)), key=lambda i: array[i:])
    return suffix_array

if __name__ == "__main__":
    import doctest
    doctest.testmod()


