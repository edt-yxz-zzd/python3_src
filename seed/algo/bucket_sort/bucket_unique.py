

__all__ = '''
    bucket_unique
    '''.split()



from seed.tiny import echo

'''
v.s. bucket_sort_with_table:
    no "table"/"output"
        if offer "table/output", then should offer "Nothing"
        no better than using a empty list
        hence no better than use bucket_sort_with_table or bucket_group_with_table
'''
# bucket_sort_without_duplicates
def bucket_unique(alphabet_size, iterable
        , *, key=None, unique_case=-1, onto=False):
    ''':: (a->UInt) -> Iter a -> [a]


input:
    alphabet_size :: UInt
    iterable :: Iter a
    key :: a -> UInt[0..alphabet_size-1]
    unique_case :: -1 | 0 | 1       = -1
        1 - input has no duplicates
            into
            1<->many
            unique; no duplicates
        0 - use the first duplicate
        -1 - use the last duplicate
    onto :: bool = False
        if onto=True:
            assert set(map(key, iterable)) == set(range(alphabet_size))
            hence len(result) == alphabet_size
            many<->1
        if unique_case=1 and onto=True:
            bijection
            1<->1
output:
    result :: [a]
        len(result) == len(set(map(key, iterable)))
        if onto:
            len(result) == alphabet_size
        if unique_case==1:
            #into
            len(result) == len(iterable)
why no "reverse"?
    we can simply result.reverse(),
        since each nonempty group contains one element

see also:
    inverse_uint_bijection_array
        inverse_uint_bijection_array(old2new) ==
            this(L, range(L), key=old2new.__getitem__, unique_case=1, onto=True)
        where L = len(old2new)

example:
    >>> this = bucket_unique
    >>> this(0, iter([]))
    []
    >>> this(1, [[], {}], key=len, unique_case=-1)
    [{}]
    >>> this(1, [[], {}], key=len, unique_case=0)
    [[]]
    >>> this(1, [[], {}], key=len, unique_case=1)
    Traceback (most recent call last):
        ...
    ValueError
    >>> this(3, [[], '12', b'1'], key=len, unique_case=1, onto=True)
    [[], b'1', '12']
    >>> this(3, [[], '12'], key=len, unique_case=1, onto=True)
    Traceback (most recent call last):
        ...
    ValueError
    >>> this(3, [[], '12', (), '1'], key=len, unique_case=1, onto=True)
    Traceback (most recent call last):
        ...
    ValueError
    >>> this(3, [[], '12', (), '1'], key=len, unique_case=-1, onto=True)
    [(), '1', '12']
    >>> this(3, [[], '12', (), '1'], key=len, unique_case=0, onto=True)
    [[], '1', '12']

'''

    if not alphabet_size >= 0: raise ValueError
    if unique_case not in [-1,0,1]: raise ValueError
    onto = bool(onto)
    if key is None: key = echo

    Nothing = {}
    table = [Nothing]*alphabet_size

    into = bool(unique_case == 1)
    first = unique_case == 0
    last = unique_case == -1
    bijection = into and onto
    for x in iterable:
        k = key(x)
        if not 0 <= k < alphabet_size: raise ValueError
        if into and table[k] is not Nothing: raise ValueError
        if first:
            # use first duplicate
            if table[k] is not Nothing: continue
        assert last or table[k] is Nothing
        table[k] = x

    if onto and any(x is Nothing for x in table): raise ValueError
    if bijection:
        result = table
    else:
        result = [x for x in table if x is not Nothing]

    assert not onto or len(result) == alphabet_size
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

