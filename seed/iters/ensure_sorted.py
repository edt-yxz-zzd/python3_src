r'''[[[
py -m seed.iters.ensure_sorted


from seed.iters.ensure_sorted import ensure_sorted, ensure_strict_sorted, ensure_neighbor_relationship
#def ensure_strict_sorted(iterable, /, *, key=None, __lt__=None, reverse=False, on_error=None, __le__=None, with_key=False):
#def ensure_sorted(iterable, /, *, key=None, before=None, reverse=False, to_not=False, on_error=None, with_key=False):
#def ensure_neighbor_relationship(iterable, bin_pred, /, *, key=None, reverse=False, to_not=False, on_error=None, with_key=False):

#]]]'''#'''



__all__ = '''
    ensure_sorted
    ensure_strict_sorted
    ensure_neighbor_relationship
    '''.split()#'''

import operator
from seed.tiny import echo
#from seed.iters.map_if import map_if
#from seed.iters.zip_me import zip_me2
#from itertools import starmap
#from itertools import pairwise

def ensure_strict_sorted(iterable, /, *, key=None, __lt__=None, reverse=False, on_error=None, __le__=None, with_key=False):
    '''ensure_strict_sorted :: Iter a -> Iter a

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

    >>> [*ensure_strict_sorted([3,1,0], key=int.__neg__, with_key=True)]
    [(-3, 3), (-1, 1), (0, 0)]
    >>> [*ensure_strict_sorted([3,1,0], reverse=True, with_key=True)]
    [(3, 3), (1, 1), (0, 0)]

    >>> [*ensure_strict_sorted([1,1])]
    Traceback (most recent call last):
        ...
    ValueError
    >>> [*ensure_strict_sorted([1,1], __lt__=int.__lt__)]
    Traceback (most recent call last):
        ...
    ValueError
    >>> [*ensure_strict_sorted([1,1], __le__=int.__le__)]
    Traceback (most recent call last):
        ...
    ValueError
    >>> [*ensure_strict_sorted([1,1], __lt__=int.__lt__, __le__=int.__le__)]
    Traceback (most recent call last):
        ...
    TypeError: err:set both __le__,__lt__

'''#'''


    if __le__ is None:
        if __lt__ is None:
            __lt__ = operator.lt
        return ensure_neighbor_relationship(
            iterable, __lt__, key=key, reverse=reverse, on_error=on_error, with_key=with_key)
    ######################
    #xxx:__le__ = operator.le
    if __lt__ is None:
        # [__lt__(a,b) == not __le__(b,a)]
        # [(a < b) == (b > a) == (not b <= a)]
        to_not = False
        return ensure_neighbor_relationship(
            iterable, __le__, key=key, reverse=not reverse, to_not=not to_not, on_error=on_error, with_key=with_key)

    raise TypeError('err:set both __le__,__lt__')


def ensure_sorted(iterable, /, *, key=None, before=None, reverse=False, to_not=False, on_error=None, with_key=False):
    '''ensure_sorted :: Iter a -> Iter a

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

    >>> [*ensure_sorted([3,1,0], key=int.__neg__, reverse=True, to_not=True, with_key=True)]
    [(-3, 3), (-1, 1), (0, 0)]
    >>> [*ensure_sorted([3,1,0], key=int.__neg__, with_key=True)]
    [(-3, 3), (-1, 1), (0, 0)]
    >>> [*ensure_sorted([3,1,0], to_not=True, with_key=True)]
    [(3, 3), (1, 1), (0, 0)]
    >>> [*ensure_sorted([3,1,0], reverse=True, with_key=True)]
    [(3, 3), (1, 1), (0, 0)]



'''#'''


    if before is None:
        before = operator.le
    return ensure_neighbor_relationship(
        iterable, before, key=key, reverse=reverse, to_not=to_not, on_error=on_error, with_key=with_key)


def ensure_neighbor_relationship(iterable, bin_pred, /, *, key=None, reverse=False, to_not=False, on_error=None, with_key=False):
    '''ensure_neighbor_relationship :: Iter a -> (a->a->Bool) -> Iter a

output are the same as input
    but ensure the neighbors in input st bin_pred on fly

input:
    iterable :: Iter a
    bin_pred :: (k -> k -> Bool)
    key      :: None | (a -> k)
    reverse  :: Bool
        if reverse:
            [bin_pred := flip bin_pred]
    to_not  :: Bool
        if to_not:
            [bin_pred := not_ . bin_pred]
    on_error :: None | a -> a -> _
        call when bad neighbor relationship occur
        if on_error donot raise, then raise ValueError
output:
    iterableO :: Iter a
        same elements as input iterable

example:
    see: ensure_sorted
'''#'''


    if key is None:
        key = echo
    if with_key:
        def mk_r_(k, x, /):
            return (k, x)
    else:
        def mk_r_(k, x, /):
            return x

    it = ((key(x), x) for x in iterable); del iterable
    for fst_key, fst in it:
        break
    else:
        return
    yield mk_r_(fst_key, fst)

    if reverse:
        _f = bin_pred
        def bin_pred(x, y, /):
            return _f(y, x)
    if to_not:
        _g = bin_pred
        def bin_pred(x, y, /):
            return not _g(x, y)

    for snd_key, snd in it:
        if bin_pred(fst_key, snd_key):
            fst_key, fst = snd_key, snd
            yield mk_r_(fst_key, fst)
        else:
            if on_error is not None:
                on_error(fst, snd)
            raise ValueError

    pass



from seed.iters.ensure_sorted import ensure_sorted, ensure_strict_sorted, ensure_neighbor_relationship
if __name__ == "__main__":
    import doctest
    import seed.iters.ensure_sorted as M
    doctest.testmod(M)

from seed.iters.ensure_sorted import *
