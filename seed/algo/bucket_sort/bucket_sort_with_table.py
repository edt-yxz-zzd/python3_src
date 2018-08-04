
__all__ = '''
    bucket_sort_with_table
    bucket_sort_with_table__easy
    '''.split()
from seed.tiny import echo
from seed.iters.ensure_sorted import ensure_sorted, ensure_strict_sorted


def bucket_sort_with_table__easy(
        may_alphabet_size, iterable, may_sorted_wheres, table
        , *, key=None, reverse=False):
    '''

bucket_sort_with_table__easy v.s. bucket_sort_with_table
    table is mutable_seq, growing

    if len(table) <= key(iterable[i]): table.extend(...)
    if may_sorted_wheres is None: iter table # bad ideas
    if may_alphabet_size is None: ...
postconditon:
    len(table) > max(iterable)

see: bucket_sort_with_table.__doc__

time and space:
    let n = len(iterable)
    space = O(n)*reference
        both working space and space(output)
        but donot consider space(table) and space(sorted_wheres)
    time = time O(n)*('key') + O(n+alphabet_size) * uint[..alphabet_size].'<' + O(alphabet_size-len(table))*table.'append'
        ###### eval
        = time O(n)*('key' + table[i].'append' + alphabet_size.'<') + O(max(iterable)+1-len(table))*table.'append'
        + time O(len(sorted_wheres))*(table[i].'clear' + alphabet_size.'<') + O(n)*(list.'append')
        = time O(n)*('key' + uint[..alphabet_size].'<') + O(len(sorted_wheres))*(alphabet_size.'<') + O(max(iterable)+1-len(table))*table.'append'
        ##### since len(sorted_wheres) <= alphabet_size > max(iterable)
        = time O(n)*('key') + O(n+alphabet_size) * uint[..alphabet_size].'<' + O(alphabet_size-len(table))*table.'append'

        ##### if len(sorted_wheres) <= alphabet_size <= n
        = time O(n)*('key' + uint[..n].'<') + O(alphabet_size-len(table))*table.'append'



example:
    >>> this = bucket_sort_with_table__easy
    >>> input = '4213255'
    >>> this(6, iter(input), range(6), [[] for _ in range(6)], key=int)
    ['1', '2', '2', '3', '4', '5', '5']
    >>> this(6, iter(input), range(1,6), [[] for _ in range(6)], key=int)
    ['1', '2', '2', '3', '4', '5', '5']
    >>> this(6, iter(input), range(6-1,0,-1), [[] for _ in range(6)], key=int, reverse=True)
    ['5', '5', '4', '3', '2', '2', '1']
    >>> this(None, iter(input), range(6-1,0,-1), [[] for _ in range(6)], key=int, reverse=True)
    ['5', '5', '4', '3', '2', '2', '1']
    >>> this(None, iter(input), range(6-1,0,-1), tuple([] for _ in range(6)), key=int, reverse=True)
    ['5', '5', '4', '3', '2', '2', '1']
    >>> this(None, iter(input), None, tuple([] for _ in range(6)), key=int, reverse=True)
    ['5', '5', '4', '3', '2', '2', '1']
    >>> this(6, iter(input), None, [[] for _ in range(6)], key=int)
    ['1', '2', '2', '3', '4', '5', '5']
    >>> ls = []
    >>> this(6, iter(input), None, ls, key=int)
    ['1', '2', '2', '3', '4', '5', '5']
    >>> ls
    [[], [], [], [], [], []]

'''
    if key is None:
        key = echo
    sz = may_alphabet_size

    # time O(n)*('key' + table[i].'append' + alphabet_size.'<') + O(max(iterable)+1-len(table))*table.'append'
    for x in iterable:
        k = key(x)
        if not (sz is None or 0 <= k < sz): raise ValueError
        if k >= len(table):
            table.extend([] for _ in range(k-len(table)+1))
        table[k].append(x)


    # wheres
    if may_sorted_wheres is None:
        L = len(table)
        wheres = range(L-1, -1, -1) if reverse else range(L)
    else:
        sorted_wheres = may_sorted_wheres
        wheres = ensure_strict_sorted(sorted_wheres, reverse=reverse)
        del sorted_wheres
    del may_sorted_wheres



    ls = []
    # time O(len(sorted_wheres))*(table[i].'clear' + alphabet_size.'<') + O(n)*(list.'append')
    for k in wheres:
        if not (sz is None or 0 <= k < sz): raise ValueError
        seq = table[k]
        ls.extend(seq) # DONOT reverse table[k]!!!
        seq.clear()
    return ls



def bucket_sort_with_table(
        may_alphabet_size, iterable, sorted_wheres, table
        , *, key=None, reverse=False):
    '''

why with table?
    so we can save the time to construct the table
    we need only init table once O(1)*table<L>.'init'
        and perform many bucket_sort_with_table

input:
    may_alphabet_size   :: None | UInt
    iterable            :: Iter a
    sorted_wheres       :: Iter TableIdx
        TableIdx is UInt[0..alphabet_size-1]
        is_strict_sorted(sorted_wheres, reverse=reverse)
            ==>> len(sorted_wheres) <= alphabet_size
    table               :: [[a]]
        :: [mutable_seq<a>]
        :: immutable_array<mutable_seq<a> >{max(sorted_wheres)+1..}
        assert len(table) >= max(sorted_wheres)+1
        assert not any(table[i] for i in sorted_wheres)
    key                 :: (a -> where) | None
        assert all(k in sorted_wheres for k in map(key, iterable))
    reverse             :: bool
output:
    sorted_list         :: [a]
        if reverse:
            then in reverse order
            but elements with same key will keep the input order.
postconditon:
    assert not any(table[i] for i in sorted_wheres)


why not return iterable?
    since using "table"
    see: iter_bucket_sort


time and space:
    let n = len(iterable)
    space = O(n)*reference
        both working space and space(output)
        but donot consider space(table) and space(sorted_wheres)
    time
        =[finest]= time O(n)*('key' + uint[..alphabet_size].'<') + O(len(sorted_wheres))*(alphabet_size.'<')
        <= time O(n)*('key') + O(n+alphabet_size) * uint[..alphabet_size].'<'
        ###### eval
        = time O(n)*('key' + table[i].'append' + alphabet_size.'<')
        + time O(len(sorted_wheres))*(table[i].'clear' + alphabet_size.'<') + O(n)*(list.'append')
        = time O(n)*('key' + uint[..alphabet_size].'<') + O(len(sorted_wheres))*(alphabet_size.'<')
        ##### since len(sorted_wheres) <= alphabet_size
        = time O(n)*('key') + O(n+alphabet_size) * uint[..alphabet_size].'<'

        ##### if len(sorted_wheres) <= alphabet_size <= n
        = time O(n)*('key' + uint[..n].'<')



example:
    >>> this = bucket_sort_with_table
    >>> input = '4213255'
    >>> this(6, iter(input), range(6), [[] for _ in range(6)], key=int)
    ['1', '2', '2', '3', '4', '5', '5']
    >>> this(6, iter(input), range(1,6), [[] for _ in range(6)], key=int)
    ['1', '2', '2', '3', '4', '5', '5']
    >>> this(6, iter(input), range(6-1,0,-1), [[] for _ in range(6)], key=int, reverse=True)
    ['5', '5', '4', '3', '2', '2', '1']
    >>> this(None, iter(input), range(6-1,0,-1), [[] for _ in range(6)], key=int, reverse=True)
    ['5', '5', '4', '3', '2', '2', '1']
    >>> this(None, iter(input), range(6-1,0,-1), tuple([] for _ in range(6)), key=int, reverse=True)
    ['5', '5', '4', '3', '2', '2', '1']
    >>> this(None, [(), {1}, []], [0, 1], [[], []], key=len)
    [(), [], {1}]

'''
    if key is None:
        key = echo
    wheres = ensure_strict_sorted(sorted_wheres, reverse=reverse)
    del sorted_wheres
    sz = may_alphabet_size

    # time O(n)*('key' + table[i].'append' + alphabet_size.'<')
    for x in iterable:
        k = key(x)
        if not (sz is None or 0 <= k < sz): raise ValueError
        table[k].append(x)

    ls = []
    # time O(len(sorted_wheres))*(table[i].'clear' + alphabet_size.'<') + O(n)*(list.'append')
    for k in wheres:
        if not (sz is None or 0 <= k < sz): raise ValueError
        seq = table[k]
        ls.extend(seq) # DONOT reverse table[k]!!!
        seq.clear()
    return ls



if __name__ == "__main__":
    import doctest
    doctest.testmod()

