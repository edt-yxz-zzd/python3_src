

__all__ = '''
    ensure
    '''.split()

from itertools import islice

def ensure(iterable, pred, ensure_length = None, *, on_error=None):
    ''':: Iter a -> (a -> bool) -> Iter a
input:
    iterable :: Iter a
    pred      :: None | (a -> Bool)
    ensure_length :: None | UInt
        apply to iterable[:ensure_length]
    on_error :: None | a -> _
        call when iterable is not sorted
        if on_error donot raise, then raise ValueError
output:
    iterableO :: Iter a
        same elements as input iterable


example:
    >>> [*ensure([1,2,4], None)]
    [1, 2, 4]
    >>> [*ensure([1,2,4], lambda x: x<5)]
    [1, 2, 4]
    >>> it = ensure([1,2,4], lambda x: x<2)
    >>> next(it)
    1
    >>> next(it)
    Traceback (most recent call last):
      ...
    ValueError
    >>> [*ensure([1,2,4], lambda x: x<2, 1)]
    [1, 2, 4]
'''
    it = iter(iterable); del iterable
    if ensure_length is not None:
        yield from ensure(islice(it, ensure_length), pred)
        yield from it
        return
    if pred is None:
        pred = bool

    for x in it:
        if not pred(x):
            if on_error is not None:
                on_error(x) # may raise
            raise ValueError
        yield x


if __name__ == "__main__":
    import doctest
    doctest.testmod()


