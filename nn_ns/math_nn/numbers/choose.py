
__all__ = r'''
    choose
    choose_fraction
    '''.split()
#from .Pascal_number_like import PascalNumberLike
#from .numberss import NumberTable
#from .factorial import P
from fractions import Fraction
from .IPascalNumberLike import IPascalNumberLike
from .INumberTable import INumberTable__table__concrete_mixins
from .numbers_common import abstract_method, optional_method, override, define

def C(n, i):
    r'''II(n-k for k in [0..i-1])/i!

choose(n,i) ~ time O(n * log(n)^2)
'''

    if i < 0:
        return 0

    if n < 0:
        # n < 0 <= i
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

    """
    # factorial_formula, too slow
    # ~ time O(n^3 * log(n)^2)
    r = 1
    for x in range(n, n-i, -1):
        r *= x

    #assert r == factorial(n)//factorial(n-i)
    return r // P(i)
    """


def choose_fraction(fraction, i):
    if type(fraction) is int:
        return choose(fraction, i)

##    if fraction.denominator == 1:
##        return choose(fraction.numerator, i)


    r = Fraction(1)
    fraction_place_holder = 0
    for i, d_fr in zip(range(1, i+1)
                     , range(fraction_place_holder+1-i
                           , fraction_place_holder+1)):
        r *= fraction + d_fr
        r //= i
    return r

    ############# above avoid factorial in below
    r'''
    r = Fraction(1, 1)
    for x in range(i):
        r *= fraction - x

    return r / P(i)
    '''



_data = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
_half_data = [[1], [1], [1, 2], [1, 3], [1, 4, 6], [1, 5, 10]]

#class Choose(PascalNumberLike):
#?not bug?:class Choose(IPascalNumberLike, INumberTable__table__concrete_mixins):
class Choose(INumberTable__table__concrete_mixins, IPascalNumberLike):
    r'''choose(n,k) = choose(n-1,k-1)+choose(n-1,k) # n choose k
'''
    __slots__ = 'table'
    @override
    def __please_add_table_to_slots__(self):pass

    @override
    def _calc_pos_pascal_like(self, n, k, n1_k1, n1_k):
        return n1_k1 + n1_k
        raise NotImplementedError

    r'''[[[ #bug!
    @override
    def lookup_static(self, n,k):
        if k < 0: return 0
        # k >= 0
        if n < 0:
            # n < 0 <= k
            n = k-1-n
            assert n >= 0
        # n >= 0
        if k > n: return 0
        # 0 <= k <= n
        if k == n: return 1
        if k == 0: return 1
        if k == 1: return n
        if k == n-1: return n
        raise LookupError
    #]]]'''
    @override
    def lookup_static(self, n,k):
        if k < 0: return 0
        # k >= 0
        if n < 0:
            # n < 0 <= k
            n = k-1-n
            assert n >= 0
            assert 0 <= k <= n
            s = (-1)**k
        else:
            s = 1
        # n >= 0
        # k >= 0
        if k > n: return 0
        # 0 <= k <= n
        if k == n: return s
        if k == 0: return s
        if k == 1: return n*s
        if k == n-1: return n*s
        raise LookupError

    @override
    def _lookup_pos_overflow(self, n, k, table):
        assert n >= 0
        assert k >= 0
        if k > n: return 0
        return self._lookup(n, n-k, table)
    @override
    def _fill_when_neg(self, n, k):
        assert n < 0
        if k < 0: return
        assert (k-1)-n >= k >= 0
        self.fill_len(k-1-n+1)
        return
    @override
    def _lookup_neg(self, n, k, table):
        assert n < 0
        if k < 0: return 0
        assert (k-1)-n >= k >= 0
        return self._lookup((k-1)-n, k, table) * (-1)**k
        raise NotImplementedError
    @override
    def direct_calc(self, n, k):
        return C(n,k)
        raise NotImplementedError
    @override
    def row_len(self, n):
        # half data
        assert n >= 0
        return n//2+1 # 0 -> 1; 1 -> 1
        return n+1


    @override
    def __init__(self):
        super().__init__([[1]])





choose = Pascal_number = binomial = Choose()
#print(choose.get_first(6))
#assert choose.get_first(len(_data)) == _data
assert choose.get_first(len(_half_data)) == _half_data

assert C(8, 5) == choose(8, 5)
assert C(-1, 0) == choose(-1, 0) == 1
assert C(-1, -1) == choose(-1, -1) == 0
assert C(-1, 1) == choose(-1, 1) == -1
if __name__ == '__main__':
    #print = str
    print(choose(-30, 11))
    print(choose(-30, 12))
    print(choose.get_table())




