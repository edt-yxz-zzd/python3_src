
__all__ = 'not_ not_dot'.split()
from operator import not_

def not_dot(pred):
    return lambda x: not pred(x)


