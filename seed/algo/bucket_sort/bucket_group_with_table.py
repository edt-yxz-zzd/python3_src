__all__ = '''
    bucket_group_with_table
    bucket_group
    '''.split()
from seed.tiny import echo
from seed.iters.ensure_sorted import ensure_sorted, ensure_strict_sorted
from seed.iters.ensure import ensure
from seed.types.DefaultList import DefaultList



old_print = print
def new_print(*args, **kwargs):
    pass

print = new_print







def get_global_table(*, __=[]):
    #may use a lock for multi-thread
    return __
def get_global_table_ex(min_length):
    table = get_global_table()
    L = len(table)
    if L < min_length:
        table.extend([] for _ in range(min_length-L))
    return table
def bucket_group(alphabet_size, iterable, sorted_wheres=None
        , *, key=None, reverse=False
        , with_key=True
        , output=None
        , return_output=False
        , table=None
        , extend_table=False
        ):
    ''':: UInt -> Iter a -> (a->Key) -> [(Key, [a])]
    where Key = UInt

see: bucket_group_with_table
vs bucket_group_with_table:
    avoid using global table
'''
    f = lambda: bucket_group_with_table(
                    alphabet_size, iterable, sorted_wheres, table
                    , key=key, reverse=reverse
                    , with_key=with_key
                    , extend_table=extend_table
                    , output=output
                    , return_output=return_output
                    , using_global_table=False
                    )
    return f()

def bucket_group_with_table(
        alphabet_size, iterable, sorted_wheres, table
        , *, key=None, reverse=False
        , with_key=True
        , extend_table=False
        , output=None
        , return_output=False
        , using_global_table=True
        ):
    ''':: UInt -> Iter a -> Iter Key -> [[a]] -> (a->Key) -> [(Key, [a])]
    where Key = UInt


input:
    alphabet_size :: None | UInt
        assert not (alphabet_size is None is sorted_wheres)
        assert alphabet_size >= 0
    iterable :: Iter a
        to be sorted
    sorted_wheres :: None | Iter Key
        # where to collect keys?
        #   so, we need not iter whole table
        #   algorithm that use this feature:
        #       * bucket sort vary-length seqences
        #           1) find out sorted_wheres per possible seq idx
        #           2) radix sort ...
        sorted_wheres should include all possibles keys in sorted order
            or reverse order(see "reverse" keyword below)
        assert is_strict_sorted(sorted_wheres, reverse=reverse)
        assert len(sorted_wheres) <= alphabet_size
        assert all(0 <= key < alphabet_size for key in sorted_wheres)
        assert all(k in sorted_wheres for k in map(key, iterable))

    table :: None | [[a]]
        assert all(not table[where] for where in sorted_wheres)
        we can save the time to construct the table
        requires:
            table.__setitem__

    key :: None | a -> Key
    with_key :: bool = True
        affect output
    reverse :: bool = False
        affect output
        output whether in reverse order
        elements with same key keep the input order like the "sorted"
            >>> sorted([(),[]], key=len, reverse=True)
            [(), []]

        if we want to reverse them:
            "reverse=False" and result.reverse()

    extend_table :: bool = False
        can extend table on need?
        assert (len(table) >= alphabet_size) or (extend_table and table is mutable)
        requires
            table.'append extend'
    output :: None | [Item]
        if not None, then output to it
        requires:
            output.'append extend'
    return_output :: bool
        affect result
        if 'output' is not None and return_output=False, then result is None
    using_global_table :: bool = True
        if table is None:
            using_global_table or create a new table
        why?
            use global_table may save the init time
                usually, sorted_wheres is not None to save the collect time
        why not?
            use global_table may cause bugs if it is not clean

  where
    Key = TableIdx = UInt[0..alphabet_size-1]

output:
    result :: None | [Item]
        if reverse=True then in reverse order
        [output is not None and not return_output] <==> [result is None]
  where
    Item = (Key, Group) if with_key else Group
    Group = [a] # nonempty
postconditon:
    assert not any(table[where] for where in sorted_wheres)
    # as the precondition
debug:
    get_global_table().clear()
        since raise inside will leave the global table contains not empty list



time:
    let n = len(iterable)
    = time O(len(sorted_wheres))*alphabet_size.'<'
    + time O(alphabet_size - len(table))* list.'__init__ append' if table is None or extend_table
    + time O(n)*('key' + table[i].'append')
    # time O(len(sorted_wheres))*(table[i].'__setitem__ __getitem__' + output.'append')

    = time O(n)*'key'
    + time O(len(sorted_wheres))*(alphabet_size.'<' + output.'append')
    + time O(alphabet_size - len(table))*ops if table is None or extend_table





example:
    >>> this = bucket_group_with_table
    >>> input = '4213255'
    >>> this(6, iter(input), None, None, key=int)
    [(1, ['1']), (2, ['2', '2']), (3, ['3']), (4, ['4']), (5, ['5', '5'])]
    >>> this(6, input, b'\1\2\3\4\5', None, key=int)
    [(1, ['1']), (2, ['2', '2']), (3, ['3']), (4, ['4']), (5, ['5', '5'])]
    >>> this(6, input, reversed(range(1,6)), None, key=int, reverse=True)
    [(5, ['5', '5']), (4, ['4']), (3, ['3']), (2, ['2', '2']), (1, ['1'])]
    >>> this(1, [(), []], None, None, key=len, reverse=True)
    [(0, [(), []])]
    >>> this(0, [], None, None)
    []
    >>> this(1, [(), []], None, None, key=len, with_key=False)
    [[(), []]]
    >>> output = [None, 'bottom']
    >>> this(None, [(), {1}, []], [0, 1], [[], []], key=len, output=output)
    >>> output
    [None, 'bottom', (0, [(), []]), (1, [{1}])]
    >>> this(None, [(), {1}, []], [0, 1], [[], []], key=len, output=output, return_output=True)
    [None, 'bottom', (0, [(), []]), (1, [{1}]), (0, [(), []]), (1, [{1}])]



    #>>> # doctest: +IGNORE_EXCEPTION_DETAIL
    # ERROR: table
    >>> table = []
    >>> this(5, [1,3], None, table)
    Traceback (most recent call last):
        ...
    ValueError: table
    >>> table
    []

    # ERROR: alphabet_size
    >>> this(None, [], None, table)
    Traceback (most recent call last):
        ...
    ValueError: alphabet_size is None is sorted_wheres
    >>> table
    []


    # ERROR: key
    >>> table = []
    >>> this(0, [1,3], None, table)
    Traceback (most recent call last):
        ...
    ValueError: key
    >>> table
    []

    # too large
    >>> table = [[], []]
    >>> this(2, [1,2], None, table)
    Traceback (most recent call last):
        ...
    ValueError: key
    >>> table
    [[], []]

    # too small
    >>> this(2, [-1, 1], None, table)
    Traceback (most recent call last):
        ...
    ValueError: key
    >>> table
    [[], []]

    # table extend until len >= alphabet_size
    >>> table = []
    >>> this(2, [0,3], None, table, extend_table=True)
    Traceback (most recent call last):
        ...
    ValueError: key
    >>> table
    [[]]

    ### success case
    >>> table = []
    >>> this(None, [0,3], [0,3], table, extend_table=True)
    [(0, [0]), (3, [3])]
    >>> table
    [[], [], [], []]

    # key too large
    #   table append until len > 0
    >>> table = []
    >>> this(2, [0,3], None, table, extend_table=True)
    Traceback (most recent call last):
        ...
    ValueError: key
    >>> table
    [[]]

    # key too large, and found sorted_wheres error
    #   table clear
    >>> table = []
    >>> this(2, [0,3], [0,3], table, extend_table=True)
    Traceback (most recent call last):
        ...
    ValueError: sorted_wheres
    >>> table
    []





    # ERROR: sorted_wheres
    # too large
    >>> table = []
    >>> this(3, [1,1,0], [0,1,2,3], table, extend_table=True)
    Traceback (most recent call last):
        ...
    ValueError: sorted_wheres
    >>> table
    []

    # too large
    >>> this(3, [1,1,0], [0,1,3], table, extend_table=True)
    Traceback (most recent call last):
        ...
    ValueError: sorted_wheres
    >>> table
    []

    # too large
    >>> this(3, [1,1,0], [0,3], table, extend_table=True)
    Traceback (most recent call last):
        ...
    ValueError: sorted_wheres
    >>> table
    []


    ### success case
    # table append until len > 1
    >>> table = []
    >>> this(3, [1,1,0], [0, 1], table, extend_table=True)
    [(0, [0]), (1, [1, 1])]
    >>> table
    [[], []]

    >>> table = []
    >>> this(None, [1,1,0], [0, 1], table, extend_table=True)
    [(0, [0]), (1, [1, 1])]
    >>> table
    [[], []]

    # not strict sorted
    >>> table = []
    >>> this(3, [1,1,0], [1, 0], table, extend_table=True)
    Traceback (most recent call last):
        ...
    ValueError: sorted_wheres
    >>> table
    []

    # not strict sorted
    >>> this(3, [1,1,0], [0,0,1], table, extend_table=True)
    Traceback (most recent call last):
        ...
    ValueError: sorted_wheres
    >>> table
    []


    # mismatch
    >>> this(3, [1,1,0], [0,2], table, extend_table=True)
    Traceback (most recent call last):
        ...
    ValueError: sorted_wheres
    >>> table
    []
'''
    f = lambda: _bucket_group_with_table(
                    alphabet_size, iterable, sorted_wheres, table
                    , key=key, reverse=reverse
                    , with_key=with_key
                    , extend_table=extend_table
                    , output=output
                    , return_output=return_output
                    , using_global_table=using_global_table
                    )
    return f()


def on_key_error1(key):
    raise ValueError('key') # out-of-range
def on_where_error1(where):
    raise ValueError('sorted_wheres') # out-of-range
def on_where_error2(where0, where1):
    raise ValueError('sorted_wheres') # not-strict-sorted
def _bucket_group_with_table(
        alphabet_size, iterable, sorted_wheres, table
        , *, key=None, reverse=False
        , with_key=True
        , extend_table=False
        , output=None
        , return_output=False
        , using_global_table=True
        ):
    if (alphabet_size is None is sorted_wheres):
        raise ValueError('alphabet_size is None is sorted_wheres')
    reverse = bool(reverse)
    with_key = bool(with_key)
    extend_table = bool(extend_table)
    return_output = bool(return_output)
    using_global_table = bool(using_global_table)


    # time O(len(sorted_wheres))*alphabet_size.'<'
    if sorted_wheres is None:
        wheres = range(alphabet_size)
        if reverse:
            wheres = reversed(wheres)
    else:
        # time O(len(sorted_wheres))*alphabet_size.'<'
        wheres = ensure_strict_sorted(sorted_wheres
                , reverse=reverse, on_error=on_where_error2)
        sorted_wheres = ...
    #del reverse , sorted_wheres

    if key is None:
        key = echo
    if with_key:
        keyed = lambda k, x: (k,x)
    else:
        keyed = lambda k, x: x
    del with_key



    # time O(alphabet_size - len(table))* list.'__init__ append' if table is None or extend_table
    table_is_None = table is None
    if table_is_None:
        # O(alphabet_size)* list.'__init__ append'
        if using_global_table:
            iget_global_table_ex = get_global_table_ex
        else:
            def iget_global_table_ex(size):
                return [[] for _ in range(size)]

        if alphabet_size is None:
            table = iget_global_table_ex(0)
            extend_table = True
            # extend_table_True 1
            # alphabet_size_None 1
        else:
            table = iget_global_table_ex(alphabet_size)
            extend_table = False
            # extend_table_False 1
            # alphabet_size_notNone 1
    elif not extend_table:
        if alphabet_size is None:
            alphabet_size = len(table)
        elif not len(table) >= alphabet_size: raise ValueError('table')
        # extend_table_False 2
        # alphabet_size_notNone 2
    else:
        # O(alphabet_size)* list.'__init__ append' if extend_table_True
        # extend_table_True 2
        # alphabet_size_None 2 or alphabet_size_notNone 3
        pass
    # alphabet_size_None ==>> extend_table_True
    assert table is not None
    assert alphabet_size is not None or extend_table
    assert alphabet_size is None or extend_table or len(table) >= alphabet_size


    # test_key: apply for key() only
    #   wheres are tested by ensure
    if alphabet_size is None:
        def test_key(k):
            return k >= 0
    else:
        def test_key(k):
            return 0 <= k < alphabet_size

    if sorted_wheres is not None:
        wheres = ensure(wheres, test_key, on_error=on_where_error1)
    del reverse , sorted_wheres


    #may_sz = alphabet_size; del alphabet_size
    if extend_table:
        table = DefaultList(list, table, copy=False)




    try:
        # time O(n)*('key' + table[i].'append')
        num_keys = 0
        num_elements = 0
        ls = None
        for x in iterable:
            print(table)
            k = key(x)
            if not test_key(k): raise ValueError('key') # on_key_error1(k)
            ls = table[k]
            is_new_key = not ls
            ls.append(x)

            if is_new_key:
                # new key
                num_keys += 1
            num_elements += 1
        del ls
    except:
        print(table)
        #table.clear()
        try:
            len_table = len(table)
            for k in wheres: # wheres => ValueError('sorted_wheres')
                ##if not test_key(k): raise ValueError('sorted_wheres')
                ##  tested in wheres
                print(k)
                if extend_table and not k < len_table: continue
                group = table[k]
                if group:
                    num_keys -= 1
                    num_elements -= len(group)
                    group.clear()
            if num_keys: raise ValueError('sorted_wheres')
            if num_elements: raise ValueError('sorted_wheres')
        except:
            table.clear()
            raise
        print(table)
        raise

    try:
        ls = [] if output is None else output
        output_old_length = len(ls)
        # time O(len(sorted_wheres))*(table[i].'__setitem__ __getitem__' + output.'append')
        len_table = len(table)
        for k in wheres: # wheres => ValueError('sorted_wheres')
            ##if not test_key(k): raise ValueError('sorted_wheres')
            ##  tested in wheres
            if extend_table and not k < len_table: continue
            group = table[k] # DONOT reverse table[k]!!!
            if group: # bug: once without "if group:"
                num_keys -= 1
                num_elements -= len(group)
                table[k] = []
                ls.append(keyed(k, group))
        if num_keys: raise ValueError('sorted_wheres')
        if num_elements: raise ValueError('sorted_wheres')
    except:
        table.clear()
        if output is not None:
            del output[output_old_length:]
        raise
        #if table_is_None and using_global_table:
            # using global table
    return ls if output is None or return_output else None


if __name__ == "__main__":
    print = old_print

if True:
    table = []
    try:
        bucket_group_with_table(2, [0,3], None, table, extend_table=True)
    except:
        assert table == [[]]
    else:
        raise logic-error


if True:
    table = []
    try:
        bucket_group_with_table(2, [1,3], None, table, extend_table=True)
    except:
        assert table == [[], []]
    else:
        raise logic-error


if __name__ == "__main__":
    print = new_print
    import doctest
    doctest.testmod()

