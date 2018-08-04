

'''
F[n] = 0, 1, ... = F[n-2] + F[n-1] = F[-n] * (-1)**(n+1)

G = golden_ratio = (1+sqrt(5))/2 = 1.61803...
F[n] = (G**n - (-1/G)**n)/sqrt(5)
    = floor(G**n/sqrt(5) + 1/2)
    = round(G**n/sqrt(5)) for [int n>=0]
F[n+1] = G*F[n] + (-1/G)**n
'''

from nn_ns.math_nn import nth_FibonacciPair
from .numberss import NumberList



_data = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def F(n):
    if n < 0:
        return F(-n) * (-1)**(1-n)
    Pn = nth_FibonacciPair(n)
    return Pn.toFn()

assert F(-1) == 1

class FibonacciNumber(NumberList):
    def _calc_neg(self, n, nums):
        return nums[-n] * (-1)**(1-n)
        raise NotImplementedError()
    def _calc_pos(self, n, nums):
        return nums[-2] + nums[-1]
        raise NotImplementedError()
    def direct_calc(self, n):
        return F(n)
        raise NotImplementedError()

    
    def __init__(self):
        super().__init__([0, 1])

fibonacci = fibonacci_number = FibonacciNumber()

assert fibonacci_number.get_first(len(_data)) == _data
assert all(F(n) == fibonacci_number(n) for n in range(-3, 5))

assert fibonacci_number(-1) == 1
assert fibonacci_number(-2) == -1
assert fibonacci_number(-3) == 2










