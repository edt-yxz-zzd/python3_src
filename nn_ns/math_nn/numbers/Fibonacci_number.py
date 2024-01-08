

r'''
F[n] = 0, 1, ... = F[n-2] + F[n-1] = F[-n] * (-1)**(n+1)

G = golden_ratio = (1+sqrt(5))/2 = 1.61803...
F[n] = (G**n - (-1/G)**n)/sqrt(5)
    = floor(G**n/sqrt(5) + 1/2)
    = round(G**n/sqrt(5)) for [int n>=0]
F[n+1] = G*F[n] + (-1/G)**n



>>> import nn_ns.math_nn.numbers.Fibonacci_number as x
>>> x.fibonacci_number.get_first(9)
[0, 1, 1, 2, 3, 5, 8, 13, 21]
>>> x.fibonacci_number.get_first(20)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

'''#'''

from nn_ns.math_nn.mx.fibonacci import nth_FibonacciPair
from .INumberList import INumberList, INumberList__nums__concrete_mixins



_data = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def F(n):
    if n < 0:
        return F(-n) * (-1)**(1-n)
    Pn = nth_FibonacciPair(n)
    return Pn.toFn()

assert F(-1) == 1

if 0b000:
    from nn_ns.math_nn import nth_FibonacciPair
    from .numberss import NumberList
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

class FibonacciNumber(INumberList__nums__concrete_mixins):
    __slots__ = ("nums",)
    __please_add_nums_to_slots__ = ...
    def _calc_pos(self, n, nums):
        assert 0 <= n <= len(nums)
        if n < len(nums):
            return nums[n]
        # [n == len(nums)]
        elif n < 2:
            # [0, 1]
            return n
        else:
            return nums[-2] + nums[-1]

    def _lookup_neg(self, n, nums):
        assert n < 0
        m = -n
        neg = not (m&1)
        r = nums[m]
        if neg:
            r = -r
        return r
    def _fill_when_neg(self, n):
        assert n < 0
        self.fill_len(1-n)
    def _calc_neg(self, n, nums):
        assert n < 0
        r = self._calc_pos(-n, nums)
        m = -n
        neg = not (m&1)
        if neg:
            r = -r
        return r
    def direct_calc(self, n):
        return F(n)


fibonacci = fibonacci_number = FibonacciNumber()

assert fibonacci_number.get_first(len(_data)) == _data
assert all(F(n) == fibonacci_number(n) for n in range(-3, 5))

assert fibonacci_number(-1) == 1
assert fibonacci_number(-2) == -1
assert fibonacci_number(-3) == 2










