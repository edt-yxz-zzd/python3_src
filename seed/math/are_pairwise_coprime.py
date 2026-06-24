r'''[[[
e ../../python3_src/seed/math/are_pairwise_coprime.py



#]]]'''
__all__ = '''
    are_pairwise_coprime
    check_pairwise_coprime
'''.split()

from seed.math.gcd import gcd

def __():
  from seed.math.II import II
  def are_pairwise_coprime(us, M=None, /):
    if M is None:
        us = [*us]
        M = II(us)
    return all(u and gcd(u, M//u) ==1 for u in us)
def are_pairwise_coprime(us, M=None, /, *, to_return_product=False, to_raise=False):
    m = 1
    for j, u in enumerate(us):
        if not (g:=gcd(m, u))==1:
            if to_raise:
                mk_exc = to_raise if callable(to_raise) else ValueError
                raise mk_exc((us, j, u, g))
            return False
        m *= u
    m
    if not M is None:
        if not M == m: raise ValueError(us, m, M)
    if to_return_product:
        return m
    return True
def check_pairwise_coprime(us, M=None, /, *, to_return_product=False):
    m = are_pairwise_coprime(us, M, to_return_product=to_return_product, to_raise=True)
    if to_return_product:
        return m
    return None



from seed.math.are_pairwise_coprime import are_pairwise_coprime, check_pairwise_coprime
from seed.math.are_pairwise_coprime import *
