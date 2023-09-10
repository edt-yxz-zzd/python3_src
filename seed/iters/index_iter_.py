
#e ../../python3_src/seed/iters/index_iter_.py
from operator import index as _to_index

def index_iter_(i, it, /):
    i = _to_index(i)
    if i < 0: raise IndexError(i)
    for j, x in enumerate(it, -i):
        if not j:
            return x
    raise IndexError(i)


from seed.iters.index_iter_ import index_iter_
