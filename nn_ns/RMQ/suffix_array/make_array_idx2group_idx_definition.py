
__all__ = '''
    make_array_idx2group_idx_definition
    '''.split()



from itertools import groupby
from seed.tiny import snd

def make_array_idx2group_idx_definition(array, key=None):
    ''':: Ord a => [a] -> [GroupIdx]

len(array_idx2group_idx<array>) == len(array)
make_array_idx2group_idx_definition array = map snd sorted([
        (array_idx, group_idx)
        for group_idx, (group_key__array_element, group__array_indices) in
            enumerate(groupby(sorted(range(L), key=key), key=key))
        for array_idx in group__array_indices
    ])
    where
        L = len(array)
        key=\i->array[i]


an slow impl
O(n*log(n)*(ArrayIdx.'<' + a.'<'))

example:
    >>> this = make_array_idx2group_idx_definition
    >>> this('')
    []
    >>> this('0')
    [0]
    >>> this('0123210456420')
    [0, 1, 2, 3, 2, 1, 0, 4, 5, 6, 4, 2, 0]
'''

    L = len(array)
    old_key = key
    if old_key is None:
        key = lambda i: array[i]
    else:
        key = lambda i: old_key(array[i])

    [*array_idx2group_idx] = map(snd, sorted([
        (array_idx, group_idx)
        for group_idx, (group_key__array_element, group__array_indices) in
            enumerate(groupby(sorted(range(L), key=key), key=key))
        for array_idx in group__array_indices
        ]))
    assert len(array_idx2group_idx) == len(array)
    return array_idx2group_idx

if __name__ == "__main__":
    import doctest
    doctest.testmod()


