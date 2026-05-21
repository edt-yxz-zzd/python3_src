r'''[[[
seed.iters.is_subset_of_sorted_iterable
py -m seed.iters.is_subset_of_sorted_iterable
py -m nn_ns.app.debug_cmd   seed.iters.is_subset_of_sorted_iterable -x
py -m nn_ns.app.doctest_cmd seed.iters.is_subset_of_sorted_iterable:__doc__ -ht #  -ff -v -df
#]]]'''#'''

__all__ = '''
    is_subset_of_sorted_iterable
    '''.split()

___begin_mark_of_excluded_global_names__0___ = ...
import operator

from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.funcs import echo, snd, with_key
    from .PeekableIterator import PeekableIterator
___end_mark_of_excluded_global_names__0___ = ...


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



from seed.iters.is_subset_of_sorted_iterable import *
if __name__ == "__main__":
    import doctest
    doctest.testmod()

from seed.iters.is_subset_of_sorted_iterable import is_subset_of_sorted_iterable
