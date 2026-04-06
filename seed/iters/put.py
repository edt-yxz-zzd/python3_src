__all__ = 'put'.split()

def put(start, iterable):
    yield start
    yield from iterable

from seed.iters.put import put
