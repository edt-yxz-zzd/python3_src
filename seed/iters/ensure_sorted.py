



__all__ = '''
    ensure_sorted
    ensure_strict_sorted
    ensure_neighbor_relationship
    '''.split()

import operator
from seed.tiny import echo
#from seed.iters.map_if import map_if
#from seed.iters.zip_me import zip_me2
#from itertools import starmap

def ensure_strict_sorted(iterable
        , *, key=None, __lt__ = None, reverse=False, on_error=None):
    ''' ensure_strict_sorted :: Iter a -> Iter a

output are the same as input
    but ensure the input are sorted dynamic
    to test directly, see: is_sorted

input:
    iterable :: Iter a
    key      :: None | (a -> k)
    __lt__   :: None | (k -> k -> Bool)
    on_error :: None | a -> a -> _
        call when iterable is not sorted
        if on_error donot raise, then raise ValueError
output:
    iterableO :: Iter a
        same elements as input iterable

example:
    >>> [*ensure_strict_sorted([1,2,3])]
    [1, 2, 3]
    >>> [*ensure_strict_sorted([3,1,0], key=lambda a:-a)]
    [3, 1, 0]

    >>> ls = []
    >>> on_error = lambda a, b: ls.extend([a,b])
    >>> it = ensure_strict_sorted([1,1], on_error=on_error)
    >>> next(it);
    1
    >>> next(it)
    Traceback (most recent call last):
        ...
    ValueError
    >>> ls
    [1, 1]
'''


    if __lt__ is None:
        __lt__ = operator.lt
    return ensure_neighbor_relationship(
                iterable, __lt__, key=key, reverse=reverse, on_error=on_error)


def ensure_sorted(iterable
        , *, key=None, before = None, reverse=False, on_error=None):
    ''' ensure_sorted :: Iter a -> Iter a

output are the same as input
    but ensure the input are sorted dynamic
    to test directly, see: is_sorted

input:
    iterable :: Iter a
    key      :: None | (a -> k)
    before   :: None | (k -> k -> Bool)
        before = __le__ or __lt__ (strict)
    on_error :: None | a -> a -> _
        call when iterable is not sorted
        if on_error donot raise, then raise ValueError
output:
    iterableO :: Iter a
        same elements as input iterable

example:
    >>> [*ensure_sorted([1,2,3,3])]
    [1, 2, 3, 3]
    >>> [*ensure_sorted([3,1,0], key=lambda a:-a)]
    [3, 1, 0]

    >>> ls = []
    >>> on_error = lambda a, b: ls.extend([a,b])
    >>> it = ensure_sorted([1,0], on_error=on_error)
    >>> next(it);
    1
    >>> next(it)
    Traceback (most recent call last):
        ...
    ValueError
    >>> ls
    [1, 0]
'''


    if before is None:
        before = operator.le
    return ensure_neighbor_relationship(
                iterable, before, key=key, reverse=reverse, on_error=on_error)


def ensure_neighbor_relationship(iterable, bin_pred
        , *, key=None, reverse=False, on_error=None):
    ''' ensure_neighbor_relationship :: Iter a -> (a->a->Bool) -> Iter a

output are the same as input
    but ensure the neighbors in input st bin_pred on fly

input:
    iterable :: Iter a
    bin_pred :: (k -> k -> Bool)
    key      :: None | (a -> k)
    reverse  :: Bool
        flip bin_pred
    on_error :: None | a -> a -> _
        call when bad neighbor relationship occur
        if on_error donot raise, then raise ValueError
output:
    iterableO :: Iter a
        same elements as input iterable

example:
    see: ensure_sorted
'''


    if key is None:
        key = echo

    it = ((key(x), x) for x in iterable); del iterable
    for fst_key, fst in it:
        break
    else:
        return
    yield fst

    if reverse:
        _f = bin_pred
        def bin_pred(x, y):
            return _f(y, x)

    for snd_key, snd in it:
        if bin_pred(fst_key, snd_key):
            fst_key, fst = snd_key, snd
            yield fst
        else:
            if on_error is not None:
                on_error(fst, snd)
            raise ValueError

    pass



if __name__ == "__main__":
    import doctest
    doctest.testmod()

