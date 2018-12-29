
__all__ = '''
    radix_sort_with_table
    '''.split()
from seed.tiny import echo
from seed.iters.ensure_sorted import ensure_sorted, ensure_strict_sorted
from .bucket_sort_with_table import bucket_sort_with_table


def complete_key_func(num_alphabet_sizes, key):
    # extend result of key s.t. len(result of key) >= num_alphabet_sizes
    #   but need to shift old uint key (+1)
    assert num_alphabet_sizes >= 0
    def new_key(a):
        keys = key(a)
        [*keys] = map(lambda i:i+1, islice(keys, num_alphabet_sizes))
        if len(keys) < num_alphabet_sizes:
            keys += [0]*(num_alphabet_sizes-len(keys))
            assert len(keys) == num_alphabet_sizes
        return keys
    return new_key

def radix_sort_with_table(
        alphabet_sizes, iterable, table
        , *, key=None, reverse=False, incomplete=False):
    ''':: [UInt] -> Iter a -> Iter TableIdx -> [[a]] -> [a]




    alphabet_sizes      :: [UInt]
        let SZ = max(alphabet_sizes)
    iterable            :: Iter a
        let n = len(iterable)
    table               :: [[a]]
                        :: [mutable_seq<a>]
                        :: immutable_array<mutable_seq<a> >
        assert len(table) >= SZ+int(incomplete)
        assert not any(table[i+int(incomplete)] for i in range(SZ))
    key :: None | (a -> Tuple<UInt[..sz] for sz in alphabet_sizes>)
        len(result of key) can be large than len(alphabet_sizes)
            may be lesser, see incomplete
        assert all(0 <= k < sz for ks in map(key, iterable) for k,sz in zip(ks, alphabet_sizes))
    incomplete :: Bool
        if True:
            length of the result of key may be less than len(alphabet_sizes)
    reverse             :: bool
output:
    sorted_list         :: [a]
        if reverse:
            then in reverse order
            but elements with same key will keep the input order.
postconditon:
    assert not any(table[i+int(incomplete)] for i in range(SZ))


time and space
    let n = len(iterable)
    let SZ = max(alphabet_sizes)
    let SUM_SZ = sum(alphabet_sizes) <= len(alphabet_sizes)*SZ
    working space O(n)*reference + O(len(sorted_wheres)*log2(SZ)
        donot count space(table)
    time
        = time sum(O(n)*('key' + uint[..sz].'< +1') + O(sz)*(sz.'< +') for sz in alphabet_sizes)
        TODO
        = time sum(O(n)*'key' + O(sz+n)*(sz.'< +') for sz in alphabet_sizes)
        = time sum(O(n*len(alphabet_sizes))*'key' + O(sz+n)*(sz.'< +') for sz in alphabet_sizes)
        = 
'''
    if key is None:
        key = echo
    alphabet_sizes = tuple(alphabet_sizes)
    incomplete = bool(incomplete)
    if incomplete:
        key = complete_key_func(len(alphabet_sizes), key)
    if reverse:
        def make_wheres(sz):
            return reversed(range(sz))
    else:
        def make_wheres(sz):
            return range(sz)

    #O(n)*'key'
    ls = [(key(x), x) for x in iterable]; del iterable
    # O(len(alphabet_sizes))*???
    for idx, sz in zip(reversed(range(len(alphabet_sizes)))
                     , reversed(alphabet_sizes)):
        # bucket_sort_with_table:
        #   = time O(n)*('key' + uint[..alphabet_size].'< +1') + O(len(sorted_wheres))*(alphabet_size.'<')
        # make_wheres
        #   = time O(sz_)*sz.'+'
        #=time O(n)*('key' + uint[..sz].'< +1') + O(sz)*sz.'< +'
        sz_ = sz+incomplete
        ls[:] = bucket_sort_with_table(
                    sz_, ls, make_wheres(sz_), table, key=lambda x:x[0][idx])
    for i in range(len(ls)):
        _, ls[i] = ls[i]
    return ls

radix_sort = radix_sort_with_table

if __name__ == "__main__":
    import doctest
    doctest.testmod()

