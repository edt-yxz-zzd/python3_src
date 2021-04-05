r'''
seed.iters.cmp4iterable
from seed.iters.cmp4iterable import eq4iterable

TODO:
    lt4iterable
    le4iterable
#'''

__all__ = '''
    eq4iterable
    '''.split()

from seed.tiny import echo
import operator

def eq4iterable(lhs_iterable, rhs_iterable, /, *, key=None, __eq__=None):
    lhs_iterable = iter(lhs_iterable)
    rhs_iterable = iter(rhs_iterable)
    if key is None:
        key = echo
    if __eq__ is None:
        __eq__ = operator.__eq__
    for x in lhs_iterable:
        try:
            y = next(rhs_iterable)
        except StopIteration:
            return False
        if not __eq__(x, y):
            return False
    else:
        try:
            next(rhs_iterable)
        except StopIteration:
            return True
        else:
            return False


