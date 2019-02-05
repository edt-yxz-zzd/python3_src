
'''
group_by_eq
    vs seed.iters.group_by
    add parameter '__eq__'
'''

__all__ = '''
    group_by_eq
    '''.split()

from seed.tiny import echo
import operator

def group_by_eq(iterable, *, key=None, __eq__=None, list2group=None):
    '''Iter a -> (a -> k) -> (k -> k -> Bool) -> ([a] -> g) -> Iter (k, g)

input:
    iterable :: Iter a
        may or may not sorted
    key :: None | (a -> k)
        if key is None:
            k = a
    __eq__ :: None | (k -> k -> Bool)
    list2group :: None | ([a] -> g)
        if list2group is None:
            g = [a]
output:
    iter_keyed_group_pairs :: Iter (k, g)

example:
    >>> this = group_by_eq
    >>> ls_this = lambda *args, **kwargs: list(this(*args, **kwargs))

    >>> it = this([])
    >>> iter(it) is it
    True

    >>> ls_this([])
    []
    >>> ls_this([1])
    [(1, [1])]
    >>> ls_this([1,1])
    [(1, [1, 1])]
    >>> ls_this([1,2,1])
    [(1, [1]), (2, [2]), (1, [1])]
    >>> ls_this([1,2,2,1])
    [(1, [1]), (2, [2, 2]), (1, [1])]
    >>> ls_this([1,1,2,2,1])
    [(1, [1, 1]), (2, [2, 2]), (1, [1])]

    # key
    >>> ls_this([(),[],[1],{1},'a',{},''], key=len)
    [(0, [(), []]), (1, [[1], {1}, 'a']), (0, [{}, ''])]
    >>> ls_this([1,2,[],'','a',3], key=type)
    [(<class 'int'>, [1, 2]), (<class 'list'>, [[]]), (<class 'str'>, ['', 'a']), (<class 'int'>, [3])]

    # __eq__
    >>> ls_this([1,2,[],'','a',3], __eq__=lambda a,b:type(a) is type(b))
    [(1, [1, 2]), ([], [[]]), ('', ['', 'a']), (3, [3])]

    # list2group
    >>> ls_this([1,1,2,2,1], list2group = tuple)
    [(1, (1, 1)), (2, (2, 2)), (1, (1,))]
'''
    if key is None:
        key = echo
    if __eq__ is None:
        __eq__ = operator.__eq__
    if list2group is None:
        list2group = echo


    it = iter(iterable)
    for head in it:
        break
    else:
        return; yield

    head_key = key(head)
    ls = [head]
    for a in it:
        k = key(a)
        if __eq__(k, head_key):
            ls.append(a)
        else:
            # prev group complete
            group = list2group(ls)
            yield head_key, group

            # new group
            head = a
            head_key = k
            ls = [head]
    assert ls
    group = list2group(ls)
    yield head_key, group



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):



