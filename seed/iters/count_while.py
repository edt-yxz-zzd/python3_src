__all__ = 'count_while'.split()
def count_while(pred, iterable):
    i = -1
    for i, x in enumerate(iterable):
        if not pred(x):
            return i
    return i+1
from seed.iters.count_while import count_while
