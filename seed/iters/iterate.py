r'''[[[
e ../../python3_src/seed/iters/iterate.py
seed.iters.iterate

view ../../python3_src/seed/math/mk_pows_.py

#]]]'''
__all__ = '''
    iterate
    iterate2_
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

def iterate2_(f, x, y, /, *args4islice, with_fst, with_snd):
    'f -> x -> y -> iter([?x?, ?y?, f(x,y), f(f(x,y),y), ...])'
    it = _iterate2_(f, x, y, with_fst, with_snd)
    if args4islice:
        it = islice(it, *args4islice)
    return it
def _iterate2_(f, x, y, with_fst, with_snd):
    if with_fst:
        yield x
    if with_snd:
        yield y
    while 1:
        x = f(x, y)
        yield x


from seed.iters.iterate import iterate, iterate2_
from seed.iters.iterate import *
