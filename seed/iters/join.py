
__all__ = 'join iter_join chain_iters concat'.split()

from collections.abc import Container 
from itertools import chain

def chain_iters(iters):
    return chain.from_iterable(iters)

concat = chain_iters

def join(mid_container, iterables, builder=None):
    'builder :: iterable -> result'
    it = iter_join(mid_container, iterables)
    builder = builder if builder is not None else type(mid_container)
    return builder(it)

def iter_join(mid_container, iterables):
    if not isinstance(mid_container, Container):
        raise TypeError('not isinstance(mid_container, Container)')
    iterables = iter(iterables)
    for it in iterables:
        yield from it
        break
    else:
        return
    
    for it in iterables:
        yield from iter(mid_container)
        yield from it

    



    
