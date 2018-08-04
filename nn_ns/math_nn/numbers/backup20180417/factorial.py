

from .numberss import NumberList



def P(n):
    if n < 0:
        raise ValueError('n < 0')
    
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

class Factorial(NumberList):
    def _calc_neg(self, n, nums):
        raise NotImplementedError()
    def _calc_pos(self, n, nums):
        return nums[n-1]*n
        raise NotImplementedError()
    def direct_calc(self, n):
        return P(n)
        raise NotImplementedError()

    
    def __init__(self):
        super().__init__([1])
    
factorial = Factorial()
#print(factorial.get_first(6))
assert factorial.get_first(6) == [1, 1, 2, 6, 24, 120]
assert P(7) == factorial(7)






'''
old version


_factorials = [1]

def factorials_least_len(L):
    ls = _factorials
    if len(ls) < L:
        for n in range(len(ls), L):
            ls.append(ls[-1]*n)
        assert len(ls) == L

    assert len(ls) >= L
    return ls

def factorial(n):
    return factorials_least_len(n+1)[n]


assert factorials_least_len(5)[:5] == [1, 1, 2, 6, 24]

'''



