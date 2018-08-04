
__all__ = '''
    difference_of_two_sorted_iterables
    '''.split()

import operator
from seed.tiny import echo, with_key, snd
from .PeekableIterator import PeekableIterator


def difference_of_two_sorted_iterables(lefts, rights
        , *, left_key=None, right_key=None, __lt__=None):
    ''':: Ord k => (a->k) -> (b->k) -> [a] -> [b] -> [a]
    # all Iter not []

left_key :: a->k
right_key :: b->k
lefts :: Iter a
    lefts should be sorted
    assert is_sorted(lefts, key=left_key)
rights :: Iter b
    rights should be sorted
    assert is_sorted(rights, key=right_key)
__lt__ :: k -> k -> Bool

example:
    >>> list_this = lambda *args, **kwargs: list(difference_of_two_sorted_iterables(*args, **kwargs))
    >>> list_this(iter([]), iter([]))
    []
    >>> list_this([], [1])
    []
    >>> list_this([1], [])
    [1]
    >>> list_this([1], [1])
    []
    >>> list_this([1,1], [1])
    [1]
    >>> list_this([1,1,1], [1])
    [1, 1]
    >>> list_this([1,1,1], [1,1])
    [1]
    >>> list_this([0,3], [1,2])
    [0, 3]
    >>> list_this([-1,0,1,1,3,4,4,5,6], [-1,1,1,2,4])
    [0, 3, 4, 5, 6]

'''
    if left_key is None:
        left_key = echo
    if right_key is None:
        right_key = echo
    if __lt__ is None:
        __lt__ = operator.lt

    lefts = PeekableIterator(with_key(left_key, lefts))
    rights = PeekableIterator(with_key(right_key, rights))

    try:
        while True:
            lkey, lhs = lefts.head
                # may raise but fine since we will catch
            rkey, rhs = rights.head

            if __lt__(lkey, rkey):
                yield lhs
                next(lefts)
            elif __lt__(rkey, lkey):
                next(rights)
            else:
                # lkey == rkey:
                next(lefts)
                next(rights)
    except StopIteration:
        yield from map(snd, lefts.chain_detach())

if __name__ == "__main__":
    import doctest
    doctest.testmod()

