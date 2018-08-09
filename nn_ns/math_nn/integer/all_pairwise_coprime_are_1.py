
r'''
example:
    >>> this = all_pairwise_coprime_are_1
    >>> this(iter([]))
    True
    >>> this([])
    True
    >>> this([0])
    True
    >>> this([1])
    True
    >>> this([2])
    True
    >>> this([1,2])
    True
    >>> this([1,2,3])
    True
    >>> this([1,2,3,4])
    False
    >>> this([2,3,35,11])
    True

    >>> this([0,1,1,-1])
    True
    >>> this([0,0])
    False
    >>> this([0,1,0])
    False

'''

__all__ = ['all_pairwise_coprime_are_1']
from seed.iters.product import py_product
from collections.abc import Sequence
from math import gcd
from numbers import Integral

'''
def all_pairwise_coprime_are_1(ints):
    # [Integer] -> Bool
    # return all(i==j or gcd(input[i], input[j])==1 for any i,j <- [0..len(input)])
    if not isinstance(ints, Sequence): raise TypeError
    if not all(isinstance(i, Integral) for i in ints): raise TypeError

    L = len(ints)
    if L < 2: return True
    if not all(ints):
        # 0 in ints
        if not all(abs(i) < 2 for i in ints): return False # not all (-1,0,1)
        return sum(map(abs, ints)) == L-1 # one and only one 0

    M = py_product(ints)
    return all(gcd(i, M//i)==1 for i in ints)
'''

def all_pairwise_coprime_are_1(ints):
    # Iter Integer -> Bool
    # return all(i==j or gcd(input[i], input[j])==1 for any i,j <- [0..len(input)])

    if __debug__:
        def iter_ints(ints):
            for i in ints:
                if not isinstance(i, Integral): raise TypeError
                yield i
        ints = iter_ints(ints)
    ints = iter(ints)

    for M in ints:
        break
    for i in ints:
        if gcd(i, M) != 1: return False
        M *= i
    return True




if __name__ == "__main__":
    import doctest
    doctest.testmod()




