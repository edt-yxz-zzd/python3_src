'''
neighbor_unique
    if work on sorted iterable: then is normal unique
seed.iters.neighbor_unique
py -m seed.iters.neighbor_unique
py -m nn_ns.app.debug_cmd   seed.iters.neighbor_unique -x
py -m nn_ns.app.doctest_cmd seed.iters.neighbor_unique:__doc__ -ht #  -ff -v -df
'''

__all__ = '''
    neighbor_unique
    '''.split()

___begin_mark_of_excluded_global_names__0___ = ...
import operator

from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.funcs import echo, snd, with_key
___end_mark_of_excluded_global_names__0___ = ...


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






from seed.iters.neighbor_unique import *
if __name__ == "__main__":
    import doctest
    doctest.testmod()
from seed.iters.neighbor_unique import neighbor_unique
