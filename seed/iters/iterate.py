r'''[[[
e ../../python3_src/seed/iters/iterate.py
seed.iters.iterate
from seed.iters.iterate import iterate

#]]]'''
__all__ = '''
    iterate
    '''.split()
from itertools import islice

def iterate(f, x, /, *args4islice):
    'f -> x -> iter([x, f(x), f(f(x)), ...])'
    if not callable(f): raise TypeError
    it = _iterate(f, x)
    if args4islice:
        it = islice(it, *args4islice)
    return it

def _iterate(f, x, /):
    while 1:
        yield x
        x = f(x)

