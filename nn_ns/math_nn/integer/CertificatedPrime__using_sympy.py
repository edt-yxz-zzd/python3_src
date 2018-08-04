

from sympy import factorint as factor_int, isprime as is_pseudoprime, \
     is_primitive_root
from .CertificatedPrime import CertificatedPrime, find_primitive_root
from functools import lru_cache

__all__ = ('make_certificated_prime',)

def make_certificated_prime(p):
    if not is_pseudoprime(p):
        raise ValueError('not is_pseudoprime({})'.format(p))
    return __make_certificated_prime(p)

@lru_cache(maxsize=None, typed=False) 
def __make_certificated_prime(p):
    q2exp = factor_int(p-1)

    q2exp = {__make_certificated_prime(q): int(exp)
             for q, exp in q2exp.items()}

    p = int(p)
    g = find_primitive_root(p, p-1, q2exp)
    return CertificatedPrime(q2exp, int(g))
    

#print(make_certificated_prime(203))




