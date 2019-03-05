

__all__ = '''
    lcm_many
    lcm
    '''.split()

import math # gcd
import functools # reduce
#bad: import functools # reduce
#   since reduce is not foldl!!!!!!!!!!!!!
#   not bug: if lcm/gcd work only for int
#from seed.iters.binary_op import foldl


def lcm_many(iterable):
    #only for int
    #not bug: return functools.reduce(lcm, iterable, 1)
    return functools.reduce(lcm, iterable, 1)
    #return foldl(lcm, iterable, one)
def lcm(a, b):
    #only for int
    if not a or not b: raise ValueError
        # return a*b # may not int
        # return 0
    return a*b//math.gcd(a,b)

