r'''
e ../../python3_src/seed/tiny_/fmap4may.py

seed.tiny_.fmap4may
from seed.tiny_.fmap4may import fmap4may

'''#'''

def fmap4may(f, may_x, /):
    '(x->y) -> may x -> may y'
    if may_x is None:
        may_y = None
    else:
        x = may_x
        y = f(x)
        if y is None: raise TypeError
        may_y = y
    return may_y

