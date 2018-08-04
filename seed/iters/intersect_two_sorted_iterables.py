
__all__ = '''
    intersect_two_sorted_iterables
    '''.split()

import operator
from seed.tiny import echo, with_key, snd
from .PeekableIterator import PeekableIterator


def intersect_two_sorted_iterables(lefts, rights
        , *, left_key=None, right_key=None, combine=None, __lt__=None):
    ''':: Ord k => (a->k) -> (b->k) -> [a] -> [b] -> (a->b->c) -> [c]
    # all Iter not []

left_key :: a->k
right_key :: b->k
lefts :: Iter a
    lefts should be sorted
    assert is_sorted(lefts, key=left_key)
rights :: Iter b
    rights should be sorted
    assert is_sorted(rights, key=right_key)
combine :: a->b->c
    if combine is None, then left-biased # i.e. c is a
__lt__ :: k -> k -> Bool

example:
    >>> list_this = lambda *args, **kwargs: list(intersect_two_sorted_iterables(*args, **kwargs))
    >>> list_this(iter([]), iter([]))
    []
    >>> list_this([], [1])
    []
    >>> list_this([1], [])
    []
    >>> list_this([1], [1])
    [1]
    >>> list_this([0,3], [1,2])
    []
    >>> list_this([-1,0,1,1,3,4, 5,6], [-1,1,1,2,4])
    [-1, 1, 1, 4]

    # combine
    >>> list_this([-1,0,1,1,3,4, 5,6], [-1,1,1,2,4], combine=lambda a,b:(a,b))
    [(-1, -1), (1, 1), (1, 1), (4, 4)]
    >>> list_this([-1,0,1,1,3,4, 5,6], [-1,1,1,2,4], combine=lambda a,b:None)
    [None, None, None, None]

    >>> list_this([3,0], [2,1,-1]
    ...     , left_key=lambda a:1-a, right_key=lambda a:-a
    ...     , combine=lambda a,b:(a,b))
    [(3, 2), (0, -1)]
'''
    if left_key is None:
        left_key = echo
    if right_key is None:
        right_key = echo
    if combine is None:
        def combine(lhs, rhs):
            return lhs # left-biased
    if __lt__ is None:
        __lt__ = operator.lt

    lefts = PeekableIterator(with_key(left_key, lefts))
    rights = PeekableIterator(with_key(right_key, rights))
    # try:
    if True:
        while True:
            lkey, lhs = lefts.head
                # may raise but fine since we donot catch
            rkey, rhs = rights.head
            if __lt__(lkey, rkey):
                next(lefts)
            elif __lt__(rkey, lkey):
                next(rights)
            else:
                # lkey == rkey:
                yield combine(lhs, rhs)
                #next(lefts, None)
                next(lefts)
                next(rights)
    '''
    neednot catch
    except StopIteration:
        yield from map(snd, lefts.chain_detach())
        yield from map(snd, rights.chain_detach())
    '''

if __name__ == "__main__":
    import doctest
    doctest.testmod()

