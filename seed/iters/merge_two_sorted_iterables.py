r'''[[[
seed.iters.merge_two_sorted_iterables
py -m nn_ns.app.debug_cmd   seed.iters.merge_two_sorted_iterables -x
py -m nn_ns.app.doctest_cmd seed.iters.merge_two_sorted_iterables:__doc__ -ht #  -ff -v -df
#]]]'''#'''

__all__ = '''
    merge_two_sorted_iterables
    '''.split()

___begin_mark_of_excluded_global_names__0___ = ...
import operator

from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.funcs import echo, snd, with_key
    from .PeekableIterator import PeekableIterator

___end_mark_of_excluded_global_names__0___ = ...



def merge_two_sorted_iterables(lefts, rights
        #, *, __le__=None, Left=None, Right=None):
        , *, left_key=None, right_key=None, before=None
        , Left=None, Right=None):
    ''':: (a->b->Bool) -> [a] -> [b] -> [Either a b] # all Iter not []

before :: KeyA -> KeyB -> Bool
lefts :: Iter a
    lefts should be sorted
rights :: Iter b
    rights should be sorted
Left :: a -> Either a b
Right :: b -> Either a b
left_key :: a -> KeyA
right_key :: b -> KeyB


example:
    >>> list_this = lambda *args, **kwargs: list(merge_two_sorted_iterables(*args, **kwargs))
    >>> list_this(iter([]), iter([]))
    []
    >>> list_this([], [1])
    [1]
    >>> list_this([1], [])
    [1]
    >>> list_this([1], [1])
    [1, 1]
    >>> list_this([0,3], [1,2])
    [0, 1, 2, 3]
    >>> list_this([3,0], [2,1], before = lambda a, b: b <= a)
    [3, 2, 1, 0]
    >>> list_this([0,3], [1,2], Left=lambda a: None)
    [None, 1, 2, None]
    >>> list_this([0,3], [1,2], Right=lambda a: None)
    [0, None, None, 3]
'''
    if Left is None:
        Left = echo
    if Right is None:
        Right = echo
    if left_key is None:
        left_key = echo
    if right_key is None:
        right_key = echo
    if before is None:
        before = operator.le


    lefts = PeekableIterator(with_key(left_key, lefts))
    rights = PeekableIterator(with_key(right_key, rights))
    #lefts = PeekableIterator(lefts)
    #rights = PeekableIterator(rights)
    try:
        while True:
            lkey, lhs = lefts.head
                # may raise but fine since we donot catch
            rkey, rhs = rights.head

            if before(lkey, rkey):
                yield Left(lhs)
                next(lefts)
            else:
                yield Right(rhs)
                next(rights)
    except StopIteration:
        yield from map(Left, map(snd, lefts.chain_detach()))
        yield from map(Right, map(snd, rights.chain_detach()))




from seed.iters.merge_two_sorted_iterables import *
if __name__ == "__main__":
    import doctest
    doctest.testmod()

from seed.iters.merge_two_sorted_iterables import merge_two_sorted_iterables
