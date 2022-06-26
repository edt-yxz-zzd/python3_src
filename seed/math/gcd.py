
r'''
from seed.math.gcd import gcd, gcd_many

[deprecated]:
from fractions import gcd
ImportError: cannot import name 'gcd' from 'fractions' (/data/data/com.termux/files/usr/lib/python3.10/fractions.py)

#'''


__all__ = '''
    gcd_many
    gcd
    '''.split()


from math import gcd
import functools # reduce
def gcd_many(iterable):
    #only for int
    return gcd(*iterable)
    return functools.reduce(gcd, iterable, 0)

