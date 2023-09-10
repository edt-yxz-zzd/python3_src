
r'''
from seed.math.gcd import gcd, gcd_many, are_coprime

[deprecated]:
from fractions import gcd
ImportError: cannot import name 'gcd' from 'fractions' (/data/data/com.termux/files/usr/lib/python3.10/fractions.py)

#'''


__all__ = '''
    gcd_many
    gcd
    are_coprime
    '''.split()


from math import gcd
import functools # reduce
def gcd_many(iterable):
    #only for int
    return gcd(*iterable)
    return functools.reduce(gcd, iterable, 0)

def are_coprime(a, b, /):
    return 1 == gcd(a, b)

from seed.math.gcd import gcd, gcd_many, are_coprime
from seed.math.gcd import *
