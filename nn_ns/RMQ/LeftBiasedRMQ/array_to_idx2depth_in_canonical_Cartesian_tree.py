
__all__ = '''
    array_to_idx2depth_in_canonical_Cartesian_tree
    '''.split()

from .canonical_Cartesian_tree.canonical_Cartesian_tree import \
    canonical_Cartesian_tree

def array_to_idx2depth_in_canonical_Cartesian_tree(array):
    '''Ord a => [a] -> [UInt]

what?
    to use array<uint> instead of the original array<a>
        # so that "<" will be faster
    output[idx] =[def]= canonical_Cartesian_tree(input).depth(input[idx])
    assert len(output) == len(input)



time and space:
    let L = len(input)
    time O(L)*(a.'<' + uint[..L].'+-')
    space O(L*log2(L))*bit
        for both space(output) and working space

why?
    RMQ<array> <==> RMQ<this(array)>

    in LeftBiasedRangeMinimumQuery__via_power_table,
        each query use "<" which maybe slow
        we can transform array to uint array, hence use uint."<"

example:
    >>> this = array_to_idx2depth_in_canonical_Cartesian_tree
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
    >>> this('213')
    [1, 0, 1]
    >>> this('231')
    [1, 2, 0]
    >>> this('312')
    [1, 0, 1]
    >>> this('321')
    [2, 1, 0]

'''
    (may_root, v2may_parent, v2may_left, v2may_right) \
        = canonical_Cartesian_tree(array)
        #time O(L)*(a.'<' + uint[..L].'+-')
        #space O(L*log2(L))*bit
    if may_root is None:
        assert not v2may_parent
        return []
    root = may_root

    # space O(L*log2(L))*bit
    idx2depth = [None]*len(v2may_parent)
    idx2depth[root] = 0
    to_process = [root]
        # any vtx in to_process, idx2depth[vtx] has been set

    # O(L)*uint[..L-1].'+'
    while to_process:
        v = to_process.pop()
        mL = v2may_left[v]
        mR = v2may_right[v]

        depth = idx2depth[v]
        child_depth = depth+1 # uint[..L-1].'+'
        for may_child in [mL, mR]:
            if may_child is not None:
                child = may_child
                idx2depth[child] = child_depth
                to_process.append(child) # append each vtx once
    return idx2depth


def array_to_idx2sorted_position(array):
    '''array_to_idx2sorted_position
    :: Ord a => [a] -> [ArrayNonEmptyRangeBeginIdx]


must be O(n*log(n))
    too slow
    use array_to_idx2depth_in_canonical_Cartesian_tree instead

input:
    array :: Ord a => [a]
output:
    idx2sorted_position :: [ArrayNonEmptyRangeBeginIdx]
        sorted_array = [None]*len(array)
        for idx, sorted_position in enumerate(idx2sorted_position):
            sorted_array[sorted_position] = array[idx]
        assert all(a is b for a,b in zip(sorted(array), sorted_array))
'''
    raise NotImplementedError-willnot-impl



if __name__ == "__main__":
    import doctest
    doctest.testmod()


