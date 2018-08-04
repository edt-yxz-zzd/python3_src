
__all__ = '''
    is_subset_of_sorted_iterable
    '''.split()

import operator
from seed.tiny import echo, with_key, snd
from .PeekableIterator import PeekableIterator


def is_subset_of_sorted_iterable(lefts, rights
        , *, left_key=None, right_key=None, __lt__=None):
    ''':: Ord k => (a->k) -> (b->k) -> [a] -> [b] -> Bool
    # all Iter not []

left_key :: a->k
right_key :: b->k
lefts :: Iter a
    lefts should be sorted
    assert is_sorted(lefts, key=left_key)
rights :: Iter b
    rights should be sorted
    assert is_sorted(rights, key=right_key)


example:
    >>> this = is_subset_of_sorted_iterable
    >>> this(iter([]), iter([]))
    True
    >>> this([], [1])
    True
    >>> this([1], [])
    False
    >>> this([1], [1])
    True
    >>> this([0,3], [1,2])
    False

    # left.key < right.key
    >>> this([-1,0,1,1], [-1,1,1,2])
    False

    # left.key > right.key
    >>> this([-1,1,1], [-1,0,1,1,2])
    True
    >>> this([-1,1,1], [-1,0,1,1])
    True

    # left.key while right.none
    >>> this([-1,1,1], [-1,0,1])
    False


'''
    if left_key is None:
        left_key = echo
    if right_key is None:
        right_key = echo
    if __lt__ is None:
        __lt__ = operator.lt


    lefts = PeekableIterator(with_key(left_key, lefts))
    rights = PeekableIterator(with_key(right_key, rights))

    while True:
        try:
            lkey, lhs = lefts.head
        except StopIteration:
            return True

        try:
            rkey, rhs = rights.head
        except StopIteration:
            return False

        if __lt__(lkey, rkey):
            return False
        elif __lt__(rkey, lkey):
            next(rights)
        else:
            # lkey == rkey:
            next(lefts)
            next(rights)



if __name__ == "__main__":
    import doctest
    doctest.testmod()

