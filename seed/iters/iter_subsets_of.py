
r"""

>>> from seed.func_tools.dot2 import dot
>>> f=dot[list, iter_subsets_of_uints_lt__dictionary_order::[list]]
>>> f(0)
[[]]
>>> f(1)
[[], [0]]
>>> f(2)
[[], [0], [0, 1], [1]]
>>> f(3)
[[], [0], [0, 1], [0, 1, 2], [0, 2], [1], [1, 2], [2]]
>>> f(4)
[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3], [0, 1, 3], [0, 2], [0, 2, 3], [0, 3], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
>>> len(_) == 2**4
True

>>> f = dot[list, iter_subsets_of__dictionary_order]
>>> f([])
[()]
>>> f([10])
[(), (10,)]
>>> f([10, 11])
[(), (10,), (10, 11), (11,)]
>>> f([10, 11, 12])
[(), (10,), (10, 11), (10, 11, 12), (10, 12), (11,), (11, 12), (12,)]
>>> f(range(10, 14))
[(), (10,), (10, 11), (10, 11, 12), (10, 11, 12, 13), (10, 11, 13), (10, 12), (10, 12, 13), (10, 13), (11,), (11, 12), (11, 12, 13), (11, 13), (12,), (12, 13), (13,)]
>>> len(_) == 2**4
True




>>> f = dot[list, iter_subsets_of__binary_order]
>>> f([])
[()]
>>> f([0])
[(), (0,)]
>>> f([0, 1])
[(), (1,), (0,), (0, 1)]
>>> f([0, 1, 2])
[(), (2,), (1,), (1, 2), (0,), (0, 2), (0, 1), (0, 1, 2)]
>>> f(range(4))
[(), (3,), (2,), (2, 3), (1,), (1, 3), (1, 2), (1, 2, 3), (0,), (0, 3), (0, 2), (0, 2, 3), (0, 1), (0, 1, 3), (0, 1, 2), (0, 1, 2, 3)]
>>> len(_) == 2**4
True

>>> f = dot[list, iter_subsets_of__sorted_by_len_first]
>>> f([])
[()]
>>> f([0])
[(), (0,)]
>>> f([0, 1])
[(), (0,), (1,), (0, 1)]
>>> f([0, 1, 2])
[(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
>>> f(range(4))
[(), (0,), (1,), (2,), (3,), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]
>>> len(_) == 2**4
True


#"""

__all__ = '''
    iter_subsets_of_uints_lt__dictionary_order
        iter_subsets_of__dictionary_order
    iter_subsets_of__sorted_by_len_first
    iter_subsets_of__binary_order
    '''.split()
        #iter_subsets_of

from itertools import (
        combinations
        , product
        , compress
        )
#from seed.types.view.SeqSliceView import SeqSliceView
from seed.types.view.SeqTransformView import SeqTransformView

def iter_subsets_of__sorted_by_len_first(iterable):
    ""
    #
    r"""
    it = iter(iterable)
    if it is iterable:
        #iterable is iterator
        s = tuple(it)
    else:
        s = iterable
    #"""

    s = tuple(iterable)
    n = len(s)
    for i in range(n+1):
        yield from combinations(s, i)
def iter_subsets_of__dictionary_order(iterable):
    s = tuple(iterable)
    def f(us):
        return tuple(s[i] for i in us)
    return iter_subsets_of_uints_lt__dictionary_order(len(s), f)

def iter_subsets_of_uints_lt__dictionary_order(n, __f=tuple):
    r"""
    n -> (), (0,), (0,1), ..., (n-2, n-1), (n-1,)
    #####
    [] => [0] if 0 < n else halt
    [n-1] => halt
    [..., x, n-1] => [..., x+1]
    [..., x] => [..., x, x+1]
    #"""
    n = max(0, n)
    if __f is None:
        __f = tuple

    def g():
        #vw = SeqSliceView(ls, None)
        return __f(vw)
    ls = []
    vw = SeqTransformView(None, ls)
    yield g()

    if n < 1:
        return
    n1 = n-1

    ls.append(0)
    while 1:
        assert ls
        yield g()

        if ls[-1] == n1:
            if len(ls) == 1:
                return
            else:
                ls.pop()
                ls[-1] += 1
        else:
            ls.append(ls[-1] +1)



def iter_subsets_of__binary_order(iterable):
    s = list(iterable)
    #s.reverse()
    n = len(s)
    #c = 0
    for _01s in product(range(2), repeat=n):
        #yield tuple(compress(s, (not x for x in _01s)))
        yield tuple(compress(s, _01s))
        #c += 1
    #assert c == 2**n

#iter_subsets_of = iter_subsets_of__dictionary_order
#iter_subsets_of = iter_subsets_of__binary_order

#print([*iter_subsets_of([0, 1])])
#assert [*iter_subsets_of([])] == [()]
#assert [*iter_subsets_of([0])] == [(), (0,)]
#assert [*iter_subsets_of([0, 1])] == [(), (1,), (0,), (0, 1)]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


