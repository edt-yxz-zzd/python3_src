
'''
neighbor_unique
    if work on sorted iterable: then is normal unique
'''

__all__ = '''
    neighbor_unique
    '''.split()

import operator
from seed.tiny import echo, with_key, snd

def neighbor_unique(iterable, *, key=None, __eq__=None):
    '''first-biased
:: Eq k => Iter a -> (a->k) -> Iterator a

example:
    >>> this = neighbor_unique
    >>> list_this = lambda *args, **kwargs: [*this(*args, **kwargs)]
    >>> list_this([1,0,0,1,1,3,3,1,1])
    [1, 0, 1, 3, 1]

    # first-biased
    >>> list_this([(), [], {}, (1,), [1], {1}], key=len)
    [(), (1,)]

'''
    if key is None:
        key = echo
    if __eq__ is None:
        __eq__ = operator.eq

    #it = iter(iterable); del iterable
    it = with_key(key, iterable); del iterable

    for kx, x in it:
        break
    else:
        return
    yield x
    del x

    while True:
        for ky, y in it:
            if not __eq__(kx, ky):
                break
        else:
            break
        yield y
        kx = ky
        #x = y


if __name__ == "__main__":
    import doctest
    doctest.testmod()




