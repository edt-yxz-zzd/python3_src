
__all__ = '''
    choose
    choose_fraction
    '''.split()
from .Pascal_number_like import PascalNumberLike
from .numberss import NumberTable
from .factorial import P
from fractions import Fraction

def C(n, i):
    '''II(n-k for k in [0..i-1])/i!

choose(n,i) ~ time O(n * log(n)^2)
'''

    if i < 0:
        return 0

    if n < 0:
        return C((i-1)-n,i) * (-1)**i

    i = min(i, n-i)
    if i < 0:
        return 0

    # multiplicative_formula
    # choose(n,i) ~ time O(n * log(n)^2)
    r = 1
    for i, k in zip(range(1, i+1), range(n+1-i, n+1)):
        r *= k
        r //= i
    return r

    # factorial_formula, too slow
    # ~ time O(n^3 * log(n)^2)
    r = 1
    for x in range(n, n-i, -1):
        r *= x

    #assert r == factorial(n)//factorial(n-i)
    return r // P(i)


def choose_fraction(fraction, i):
    if type(fraction) is int:
        return choose(fraction, i)

##    if fraction.denominator == 1:
##        return choose(fraction.numerator, i)


    r = Fraction(1, 1)
    for x in range(i):
        r *= fraction - x

    return r / P(i)



_data = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

class Choose(PascalNumberLike):
    def _calc_pos_pascal_like(self, n, k, n1_k1, n1_k):
        return n1_k1 + n1_k
        raise NotImplementedError()
    def _calc_neg(self, n, k, table):
        if k < 0:
            return 0
        assert n < 0
        return self((k-1)-n, k) * (-1)**k
        raise NotImplementedError()
    def direct_calc(self, n, k):
        return C(n,k)
        raise NotImplementedError()



'''
class Choose(NumberTable):
    def _calc_neg(self, n, k, table):
        if k < 0:
            return 0
        assert n < 0
        return self((k-1)-n, k) * (-1)**k
        raise NotImplementedError()
    def _calc_pos(self, n, k, table):
        if n == 0:
            return int(k==0)
        if k == 0 or k == n:
            return 1

        assert n > 0
        assert 0 < k < n
        return table[n-1][k-1] + table[n-1][k]
        raise NotImplementedError()
    def _calc_pos_beyond(self, n, k, table):
        return 0
        raise NotImplementedError()
    def direct_calc(self, n, k):
        return C(n,k)
        raise NotImplementedError()
    def row_len(self, n):
        return n+1

    def __init__(self):
        super().__init__([[1]])
    '''


choose = Pascal_number = binomial = Choose()
#print(choose.get_first(6))
assert choose.get_first(len(_data)) == _data

assert C(8, 5) == choose(8, 5)





