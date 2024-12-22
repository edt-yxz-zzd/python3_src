#__all__:goto
r'''
from seed.math.gcd import gcd, gcd_many, are_coprime

[deprecated]:
from fractions import gcd
ImportError: cannot import name 'gcd' from 'fractions' (/data/data/com.termux/files/usr/lib/python3.10/fractions.py)


py -m nn_ns.app.debug_cmd   seed.math.gcd -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.gcd:__doc__ -ht # -ff -df


>>> from itertools import product
>>> for a, b in product(range(-50, 51), repeat=2):
...     assert py_std_gcd(a, b) == gcd_via_halve_(a, b), (a,b)
>>> for a, b in product(range(-50, 51), repeat=2):
...     assert are_coprime__using_py_std_gcd_(a, b) is are_coprime__detect_via_halve_(a, b), (a,b)

>>> gcd is py_std_gcd
True
>>> are_coprime is are_coprime__using_py_std_gcd_
True
>>> gcd_many([36, 81, 72])
9
>>> gcd_ex(36, 81)
(4, 9, 9)



'''#'''


__all__ = r'''
gcd_many
gcd_ex

gcd
are_coprime
    py_std_gcd
    are_coprime__using_py_std_gcd_

    gcd_via_halve_
    are_coprime__detect_via_halve_
    '''.split()#'''


from math import gcd as py_std_gcd
#import functools # reduce

def are_coprime__using_py_std_gcd_(a, b, /):
    return 1 == py_std_gcd(a, b)
gcd = py_std_gcd or gcd_via_halve_
are_coprime = are_coprime__using_py_std_gcd_ or are_coprime__detect_via_halve_

def gcd_many(iterable):
    #only for int
    return gcd(*iterable)
    #return functools.reduce(gcd, iterable, 0)
def gcd_ex(a, b, /):
    g = gcd(a, b)
    a_g = a//g
    b_g = b//g
    return a_g, g, b_g




def _factor_out_odd(n, /):
    assert n > 0
    e2 = 0
    while not n&1:
        n >>= 1
        e2 += 1
    odd = n
    return (odd, e2)
def gcd_via_halve_(a, b, /):
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    if a == 0 or a == b:
        return b
    (a, eA) = _factor_out_odd(a)
    (b, eB) = _factor_out_odd(b)
    e2 = min(eA, eB)
    if a > b:
        a, b = b, a
    return _gcd_odds_via_halve(a, b) << e2

def _gcd_odds_via_halve(a, b, /):
    assert 1 <= a <= b, (a, b)
    assert 1 == a&1 == b&1, (a, b)
    if a == 1:
        return 1
    # [1 < a <= b]
    # [1 == a%2 == b%2]
    while 1:
        # [1 < a <= b]
        # [1 == a%2 == b%2]
        d = b - a
        # [d >= 0]
        # [d%2 == 0]
        if not d:
            return a
        # [d >= 1]
        # [d%2 == 0]
        (b, e2) = _factor_out_odd(d)
        assert e2
        # [e2 > 0][new-b < old-b] => loop-halt
        # [b >= 1]
        # [1 == b%2]
        # [a <?> b]

        # [1 == a%2 == b%2]
        # [1 < a]
        if b < a:
            # [1 <= b < a]
            a, b = b, a
            # [1 <= a < b]
            if a == 1:
                return 1
            # [1 < a < b]
        else:
            # [a <= b]
            # [1 < a <= b]
            pass
        # [1 < a <= b]
        # [1 == a%2 == b%2]


def are_coprime__detect_via_halve_(a, b, /):
    if a&1 == 0 == b&1:
        # (even, even) # (0, 0)
        return False
    a = abs(a)
    b = abs(b)
    if a == 1 or b == 1:
        return True
    if a == 0 or b == 0:
        return False
    (a, eA) = _factor_out_odd(a)
    (b, eB) = _factor_out_odd(b)
    if a > b:
        a, b = b, a
    for p in _ps4detect:
        if a%p == 0 == b%p:
            return False
    return _gcd_odds_via_halve(a, b) == 1
_ps4detect = (3,5,7)


from seed.math.gcd import gcd, gcd_many, are_coprime
from seed.math.gcd import gcd_ex
from seed.math.gcd import *
