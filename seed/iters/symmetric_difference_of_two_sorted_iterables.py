
__all__ = '''
    symmetric_difference_of_two_sorted_iterables
    '''.split()

import operator
from seed.tiny import echo, with_key, snd
from .PeekableIterator import PeekableIterator


def symmetric_difference_of_two_sorted_iterables(lefts, rights
        , *, left_key=None, right_key=None, __lt__=None
        , Left=None, Right=None):
    ''':: Ord k => (a->k) -> (b->k) -> [a] -> [b] -> [Either a b]
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
Left :: a -> Either a b
Right :: b -> Either a b


example:
    >>> list_this = lambda *args, **kwargs: list(symmetric_difference_of_two_sorted_iterables(*args, **kwargs))
    >>> list_this(iter([]), iter([]))
    []
    >>> list_this([], [1])
    [1]
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
    [0, 1, 2, 3]
    >>> list_this([-1,0,1,1,3,4,4,5,6], [-1,1,1,2,4])
    [0, 2, 3, 4, 5, 6]

'''
    if Left is None:
        Left = echo
    if Right is None:
        Right = echo
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
                yield Left(lhs)
                next(lefts)
            elif __lt__(rkey, lkey):
                yield Right(rhs)
                next(rights)
            else:
                # lkey == rkey:
                next(lefts)
                next(rights)
    except StopIteration:
        yield from map(Left, map(snd, lefts.chain_detach()))
        yield from map(Right, map(snd, rights.chain_detach()))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

