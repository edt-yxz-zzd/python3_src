
r'''
from seed.math.gcd import gcd, gcd_many, are_coprime

[deprecated]:
from fractions import gcd
ImportError: cannot import name 'gcd' from 'fractions' (/data/data/com.termux/files/usr/lib/python3.10/fractions.py)

#'''


__all__ = '''
    gcd_many
    gcd
    gcd_ex
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
def gcd_ex(a, b, /):
    g = gcd(a, b)
    a_g = a//g
    b_g = b//g
    return a_g, g, b_g

from seed.math.gcd import gcd, gcd_many, are_coprime
from seed.math.gcd import gcd_ex
from seed.math.gcd import *
