__all__ = '''
    classify
    '''.split()


def classify(alphabet_size, iterable, key
        , *, output = None, return_output=False):
    ''':: UInt -> [a] -> (a->UInt) -> [[a]]

input:
    alphabet_size :: UInt
    iterable :: Iter a
    key :: a -> UInt[0..alphabet_size-1]
    output :: None | [[a]]{alphabet_size..}
    return_output :: bool
output:
    result :: None | [[a]]
        group/class maybe empty
        [result is None] <==> [output is not None and not return_output]

example:
    >>> this = classify
    >>> this(3, [1,2,3,4], lambda x:x<3)
    [[3, 4], [1, 2], []]
    >>> output = [[], []]
    >>> this(2, [1,2,3,4], lambda x:x<3, output=output)
    >>> output
    [[3, 4], [1, 2]]
    >>> this(2, [1,2,3,4], lambda x:x<3, output=output, return_output=True)
    [[3, 4, 3, 4], [1, 2, 1, 2]]
'''
    if output is not None:
        table = output
        if len(output) < alphabet_size: raise ValueError
    else:
        table = [[] for _ in range(alphabet_size)]

    for x in iterable:
        k = key(x)
        if not 0 <= k < alphabet_size: raise ValueError
        table[k].append(x)
    return table if output is None or return_output else None


if __name__ == "__main__":
    import doctest
    doctest.testmod()

