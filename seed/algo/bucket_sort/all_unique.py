

__all__ = '''
    all_unique
    '''.split()



from seed.tiny import echo


def all_unique(alphabet_size, iterable, *, key=None):
    ''':: (a->UInt) -> UInt -> [a] -> Bool


input:
    alphabet_size :: UInt
    iterable :: Iter a
    key :: a -> UInt[0..alphabet_size-1]
output:
    are_all_unique :: Bool
        =[def]= len(set(map(key, iterable))) == len(iterable)
see:
    seed.iters.all_the_same
    bucket_unique
    inverse_uint_bijection_array
    is_uint_bijection_array
        if all_unique and len(iterable) == alphabet_size, then is a uint_bijection_array

example:
    >>> all_unique(0, [])
    True
    >>> all_unique(2, [1])
    True
    >>> all_unique(2, [1, 0])
    True
    >>> all_unique(2, [1, 1])
    False
'''
    if not alphabet_size >= 0: raise ValueError
    if key is not None:
        iterable = map(key, iterable)
    del key

    Nothing = None
    table = [Nothing]*alphabet_size

    for k in iterable:
        if not 0 <= k < alphabet_size: raise ValueError
        if table[k] is not Nothing: return False
        table[k] = ...

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()


