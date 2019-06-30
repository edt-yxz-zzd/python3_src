
__all__ = '''
    gcd_many
    gcd
    '''.split()


from math import gcd
import functools # reduce
def gcd_many(iterable):
    #only for int
    return functools.reduce(gcd, iterable, 0)

