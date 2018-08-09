
r'''
MM = II(M...)
M = B**P
N = MM/M

x%M = a
x%N = b

let M_%M = 1
    M_%N = 0
    N_%M = 0
    N_%N = 1
x = a*M_ + b*N_

M_ = k1*N = k2*M+1
k1 = (N**-1)%M = (N**-1)%(B**P)
M_ = (N**-1)%(B**P) *N
x = sum(a*M_...) = sum(a*(N**-1)%(B**P) *N...)

'''

__all__ = ['calc_chinese_remainder']

from collections.abc import Sequence
from math import gcd
from numbers import Integral
from seed.iters.product import py_product

from .inv_mod_pow import InvModPow
from .all_pairwise_coprime_are_1 import all_pairwise_coprime_are_1



def _check_input(triples):
    if not isinstance(triples, Sequence): raise TypeError
    if not len(triples) >= 1: raise TypeError
    for remainder, base, power in triples:
        if not base >= 2: raise TypeError
        if not power >= 1: raise TypeError
    bases = (base for remainder, base, power in triples)
    if not all_pairwise_coprime_are_1(bases): raise TypeError

def calc_chinese_remainder(triples):
    '''[(Integer, IntGe2, PInt)] -> Integer
[(remainder, base, power)] -> result


preconditions:
    len(input) >= 1
    base >= 2
    power >= 1
    all_pairwise_coprime_are_1(base...)

postconditions:
    (result-remainder)%base**power == 0
    0 <= result < II(base**power...)

example:
    >>> this = calc_chinese_remainder
    >>> calc_chinese_remainder([(0,2,1)])
    0
    >>> calc_chinese_remainder([(-3,2,1)])
    1

    >>> calc_chinese_remainder([(-3,2,1), (2,3,4), (1,5,2)])
    2351
    >>> 2351%3**4
    2
    >>> 2351%5**2
    1
    >>> 2 * 3**4 * 5**2
    4050

    >>> calc_chinese_remainder([(1,14,1), (2,15,1)]) == (-13)%(14*15)
    True

'''
    _check_input(triples)
    Ms = tuple(base**power for _, base, power in triples)
    MM = py_product(Ms)

    def eval_M_(base, power, M):
        N = MM//M
        #M_ = (N**-1)%(B**P) *N
        inv_N = InvModPow(base)(N, power)
        M_ = inv_N*N
        return M_
    def avoid_huge(remainder, M):
        # to avoid huge remainder
        if abs(remainder) >= M:
            remainder %= M
        return remainder

    result = sum(avoid_huge(remainder, M) * eval_M_(base, power, M)
                for M, (remainder, base, power) in zip(Ms, triples)
                ) % MM

    # check output
    assert 0 <= result < MM
    assert all((result-remainder)%M == 0
                for M, (remainder, base, power) in zip(Ms, triples))
    return result





if __name__ == "__main__":
    import doctest
    doctest.testmod()



