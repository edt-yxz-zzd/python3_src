r'''[[[
e ../../python3_src/seed/math/are_pairwise_coprime.py

from seed.math.are_pairwise_coprime import are_pairwise_coprime


#]]]'''
__all__ = '''
    are_pairwise_coprime
    '''.split()

from seed.math.II import II
from seed.math.gcd import gcd

if 0:
  def are_pairwise_coprime(us, M=None, /):
    if M is None:
        us = [*us]
        M = II(us)
    return all(u and gcd(u, M//u) ==1 for u in us)
def are_pairwise_coprime(us, M=None, /):
    m = 1
    for u in us:
        if not gcd(m, u)==1: return False
        m *= u
    if not M is None:
        if not M == m: raise ValueError
    return True


