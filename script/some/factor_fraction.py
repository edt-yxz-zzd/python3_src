

import sympy
from sympy import factorint
import numbers # numbers.Rational


__all__ = ('factor_fraction', 'to_numerator_denominator_pair')

def to_numerator_denominator_pair(fraction):
    if isinstance(fraction, numbers.Rational):
        return fraction.numerator, fraction.denominator

    return sympy.fraction(fraction)

def factor_fraction(fraction):
    N, D = to_numerator_denominator_pair(fraction)
    
    ps = factorint(N)
    qs = factorint(D)
    L = len(ps) + len(qs)

    ps.update((q, -exp) for q, exp in qs.items())
    assert len(ps) == L
    return ps



