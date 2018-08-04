

from .prime1 import factor_power_pairs_of_positive_integer as _factor
from numbers import Rational
from fractions import Fraction


__all__ = ('factor_int', 'factor_fraction')


def factor_int(n):
    if n == 0:
        return [(0,1)]

    if n < 0:
        return [(-1,1)] + factor_int(-n)

    return _factor(n)


assert factor_int(0) == [(0,1)]
assert factor_int(-18) == [(-1,1), (2,1), (3,2)]



def factor_fraction(x):
    N, D = x.numerator, x.denominator
    
    ps = factor_int(N)
    qs = factor_int(D)
    L = len(ps) + len(qs)

    ps.extend((q, -exp) for q, exp in qs)

    if not len(ps) == L == len(dict(ps)):
        print(ps, L)
        assert len(ps) == L == len(dict(ps))

    ps.sort()
    return ps
    
assert factor_fraction(0) == [(0,1)]
assert factor_fraction(-14) == [(-1,1), (2,1), (7,1)]
assert factor_fraction(Fraction(99,-14)) == [(-1,1), (2,-1), (3,2), (7,-1), (11,1)]

