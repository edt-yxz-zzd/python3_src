

__all__ = '''
    is_uint_onto_array
    '''.split()





def is_uint_onto_array(alphabet_size, iterable, *, key=None):
    ''':: (a->UInt) -> UInt -> [a] -> Bool


input:
    alphabet_size :: UInt
    iterable :: Iter a
    key :: a -> UInt[0..alphabet_size-1]
output:
    is_uint_onto_array :: Bool
        =[def]= set(map(key, iterable)) == set(range(alphabet_size))
see:
    seed.iters.all_the_same
    bucket_unique
    all_unique
    inverse_uint_bijection_array
    is_uint_bijection_array
    compress

example:
    >>> this = is_uint_onto_array
    >>> this(0, [])
    True
    >>> this(2, [1])
    False
    >>> this(2, [1, 0])
    True
    >>> this(2, [1, 1])
    False
    >>> this(2, [1, 0, 1])
    True
'''
    if not alphabet_size >= 0: raise ValueError
    if key is not None:
        iterable = map(key, iterable)
    del key

    Nothing = None
    table = [Nothing]*alphabet_size

    for k in iterable:
        if not 0 <= k < alphabet_size: raise ValueError
        table[k] = ...

    return not any(x is Nothing for x in table)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


