

__all__ = '''
    bucket_count
    '''.split()





def bucket_count(alphabet_size, iterable, *, key=None):
    ''':: (a->UInt) -> UInt -> [a] -> [UInt]
    ### (a->Key) -> UInt -> [a] -> Map Key UInt
    ###     where Key = UInt; May is list


input:
    alphabet_size :: UInt
    iterable :: Iter a
    key :: a -> UInt[0..alphabet_size-1]
output:
    bucket_count :: [UInt]
        =[def]= [map(key, iterable).count(k) for k in range(alphabet_size)]
        len(bucket_count) == alphabet_size


example:
    >>> this = bucket_count
    >>> this(0, [])
    []
    >>> this(2, [1])
    [0, 1]
    >>> this(2, [1, 0])
    [1, 1]
    >>> this(2, [1, 1])
    [0, 2]
    >>> this(2, [1, 0, 1])
    [1, 2]
'''
    if not alphabet_size >= 0: raise ValueError
    if key is not None:
        iterable = map(key, iterable)
    del key

    table = [0]*alphabet_size

    for k in iterable:
        if not 0 <= k < alphabet_size: raise ValueError
        table[k] += 1

    return table


if __name__ == "__main__":
    import doctest
    doctest.testmod()


