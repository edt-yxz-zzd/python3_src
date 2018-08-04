

def is_uint_bijection_array(old2new, *, key=None, alphabet_size=None):
    ''':: [ArrayIdx] -> Bool
    :: UInt -> (a->ArrayIdx) -> Iter a -> Bool


input:
    old2new :: [ArrayIdx] | Iter a
        # Map ArrayIdx ArrayIdx # bijection
        ArrayIdx = [UInt[0..L-1]]
        L = len(old2new) or alphabet_size
    alphabet_size :: None | UInt
    key :: None | (a -> ArrayIdx)
output:
    is_uint_bijection_array :: Bool
        =[def]= sorted(map(key, old2new)) == list(range(L))
see:
    seed.iters.all_the_same
    all_unique
    bucket_unique
    inverse_uint_bijection_array


example:
    >>> this = is_uint_bijection_array
    >>> this([])
    True
    >>> this([1])
    False
    >>> this([1,0])
    True
    >>> this([0,1])
    True
'''
    old_vtx2new_vtx = old2new; del old2new
    # old_vtx2new_vtx -> new_vtx2old_vtx
    if hasattr(old_vtx2new_vtx, '__len__'):
        V = len(old_vtx2new_vtx)
        if alphabet_size is not None:
            if V != alphabet_size: return False
    elif alphabet_size is None: raise ValueError
    else:
        V = alphabet_size

    if key is not None:
        old_vtx2new_vtx = map(key, old_vtx2new_vtx)
    del key

    Nothing = None
    new_vtx2old_vtx = [Nothing]*V
    old_vtx = -1
    for old_vtx, new_vtx in enumerate(old_vtx2new_vtx):
        if not 0 <= new_vtx < V: return False
        if not old_vtx < V: return False
        if new_vtx2old_vtx[new_vtx] is not Nothing: return False
        new_vtx2old_vtx[new_vtx] = ...
    if Nothing in new_vtx2old_vtx: return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()

