

'''
inverse_uint_bijection_array
'''
__all__ = '''
    inverse_uint_bijection_array
    '''.split()

#from seed.tiny import echo
def inverse_uint_bijection_array(old2new, *, key=None, alphabet_size=None):
    ''':: [ArrayIdx] -> [ArrayIdx]
    :: (a->ArrayIdx) -> Iter a -> UInt -> [ArrayIdx]

used in graph algorithm, suffix tree/array algorithm

input:
    old2new :: [ArrayIdx] | Iter a
        # Map ArrayIdx ArrayIdx # bijection
        ArrayIdx = [UInt[0..L-1]]
        L = len(old2new) or alphabet_size
        # bijection
        set(old2new) == set(range(L))
        sorted(old2new) == list(range(L))
    alphabet_size :: None | UInt
    key :: None | (a -> ArrayIdx)
output:
    new2old :: [ArrayIdx]
        # Map ArrayIdx ArrayIdx # bijection
        len(new2old) == L
        # bijection
        set(new2old) == set(range(L))
        sorted(new2old) == list(range(L))

        # reversed
        # new2old is inverse_uint_bijection_array of old2new
        old2new[new2old[i]] == i
        new2old[old2new[i]] == i

see:
    seed.algo.bucket_sort::
        is_uint_bijection_array
        all_unique
        bucket_unique
example:
    >>> this = inverse_uint_bijection_array
    >>> this([])
    []
    >>> this([0])
    [0]
    >>> this([0,1])
    [0, 1]
    >>> this([1,0])
    [1, 0]
    >>> this([0,1,2])
    [0, 1, 2]
    >>> this([0,2,1])
    [0, 2, 1]
    >>> this([2,0,1])
    [1, 2, 0]
    >>> this([1,0,2])
    [1, 0, 2]
    >>> this([1,2,0])
    [2, 0, 1]
    >>> this([2,1,0])
    [2, 1, 0]




used alias:
    reverse_uint_bijection_array
    reversed_uint_bijection_array
    inverse_uint_bijection_array
    inv_uint_bijection_array
    inv_automap
    reverse_map
    inverse_map
    inverse_automap
    old2new_to_new2old
'''
    old_vtx2new_vtx = old2new
    # old_vtx2new_vtx -> new_vtx2old_vtx
    if hasattr(old_vtx2new_vtx, '__len__'):
        V = len(old_vtx2new_vtx)
        if alphabet_size is not None:
            if V != alphabet_size: raise ValueError
    elif alphabet_size is None: raise ValueError
    else:
        V = alphabet_size

    if key is not None:
        old_vtx2new_vtx = map(key, old_vtx2new_vtx)

    Nothing = {}
    new_vtx2old_vtx = [Nothing]*V
    old_vtx = -1
    for old_vtx, new_vtx in enumerate(old_vtx2new_vtx):
        if not 0 <= new_vtx < V: raise ValueError
        if new_vtx2old_vtx[new_vtx] is not Nothing: raise ValueError
        new_vtx2old_vtx[new_vtx] = old_vtx
    if old_vtx >= V: raise ValueError('not a uint_bijection_array')
    if Nothing in new_vtx2old_vtx: raise ValueError('not a uint_bijection_array')
    return new_vtx2old_vtx

if __name__ == "__main__":
    import doctest
    doctest.testmod()

