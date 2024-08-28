#__all__:goto
r'''[[[
nn_ns.math_nn.numbers.Stirling_number
py -m nn_ns.app.debug_cmd   nn_ns.math_nn.numbers.Stirling_number -x
py -m nn_ns.app.doctest_cmd nn_ns.math_nn.numbers.Stirling_number:__doc__ -ht

[[
view others/数学/oeis整数序列/摘要.txt
===
Bell_number(n)
  [0..<n]的划分数量
Eulerian_2nd(n,k)
  序列([0..<n]*2)的满足凹坑光滑约束(嵌套无错乱)的刚好有k个『升序对』的排列数量
Eulerian_1st(n,k)
  [0..<n]刚好有k个『升序对』的排列数量
Stirling_circle_number(n,k)
  [0..<n]的刚好k个环轨的排列的数量
Stirling_subset_number(n,k)
  [0..<n]的k个非空子集的划分的数量


]]



Pascal_number(n,k) = binomial(n,k) = C(n,k)
Stirling_circle_number(n,k) = Stirling[n,k] = Stirling number of first kind
Stirling_subset_number(n,k) = Stirling{n,k} = Stirling number of second kind
Eulerian_1st(n,k) = Eulerian<n,k> = Eulerian numbers of first order
Eulerian_2nd(n,k) = Eulerian<<n,k>> = Eulerian numbers of second order



C(n,k)          = C(n-1,k-1)                   + C(n-1,k)
Stirling[n,k]   = Stirling[n-1,k-1]            + Stirling[n-1,k]   (n-1)
Stirling{n,k}   = Stirling{n-1,k-1}            + Stirling{n-1,k}   k
Eulerian<n,k>   = Eulerian<n-1,k-1>   (n-k)    + Eulerian<n-1,k>   (k+1)
Eulerian<<n,k>> = Eulerian<<n-1,k-1>> (2n-1-k) + Eulerian<<n-1,k>> (k+1)

Stirling[n,k] = Stirling{-k,-n}




py_adhoc_call   nn_ns.math_nn.numbers.Stirling_number   @
#]]]'''
__all__ = r'''
stirling_subset
    stirling_subset_number
stirling_circle
    stirling_circle_number
'''.split()#'''
__all__





from .IPascalNumberLike import IPascalNumberLike
from .INumberTable import INumberTable__table__concrete_mixins
from .numbers_common import abstract_method, optional_method, override, define


_sc_data = [[1], [0, 1], [0, 1, 1], [0, 2, 3, 1], [0, 6, 11, 6, 1], [0, 24, 50, 35, 10, 1]]
_ss_data = [[1], [0, 1], [0, 1, 1], [0, 1, 3, 1], [0, 1, 7, 6, 1], [0, 1, 15, 25, 10, 1]]



class _IBase(IPascalNumberLike, INumberTable__table__concrete_mixins):
    __slots__ = ("table",)
    @override
    def __please_add_table_to_slots__(self):
        ''
    @define
    def __init__(self):
        super().__init__([[1]])

    @define
    def row_len(self, n):
        assert n >= 0
        return n+1
    @define
    def _lookup_pos_underflow(self, n, k, table):
        assert n >= 0
        assert k < 0
        return 0
    @optional_method
    def _lookup_pos_overflow(self, n, k, table):
        assert n >= 0
        assert k >= self.row_len(n)
        return 0


class StirlingCircleNumber(_IBase):
    __slots__ = ()
    @define
    def _calc_pos_pascal_like(self, n, k, n1_k1, n1_k):
        return n1_k1 + n1_k*(n-1)
    @define
    def _fill_when_neg(self, n, k):
        assert n < 0
        if k > 0:
            return
        stirling_subset.fill_len(-k+1)
    @define
    def _lookup_neg(self, n, k, table):
        assert n < 0
        if k > 0:
            return 0
        return stirling_subset(-k, -n)
class StirlingSubsetNumber(_IBase):
    __slots__ = ()
    @define
    def _calc_pos_pascal_like(self, n, k, n1_k1, n1_k):
        return n1_k1 + n1_k*k
    @define
    def _fill_when_neg(self, n, k):
        assert n < 0
        if k > 0:
            return
        stirling_circle.fill_len(-k+1)
    @define
    def _lookup_neg(self, n, k, table):
        assert n < 0
        if k > 0:
            return 0
        return stirling_circle(-k, -n)


def __():
  from .Pascal_number_like import PascalNumberLike
  class StirlingCircleNumber(PascalNumberLike):
    def _calc_pos_pascal_like(self, n, k, n1_k1, n1_k):
        return n1_k1 + n1_k*(n-1)
        raise NotImplementedError()
    def _calc_neg(self, n, k, table):
        if k > 0:
            return 0
        return stirling_subset(-k, -n)
        raise NotImplementedError()
    def direct_calc(self, n, k):
        raise NotImplementedError()

#def __():
  class StirlingSubsetNumber(PascalNumberLike):
    def _calc_pos_pascal_like(self, n, k, n1_k1, n1_k):
        return n1_k1 + n1_k*k
        raise NotImplementedError()
    def _calc_neg(self, n, k, table):
        if k > 0:
            return 0
        return stirling_circle(-k, -n)
        raise NotImplementedError()
    def direct_calc(self, n, k):
        raise NotImplementedError()


r'''
from .numberss import NumberTable
class StirlingCircleNumber(NumberTable):
    def _calc_neg(self, n, k, table):
        if k > 0:
            return 0
        return stirling_subset(-k, -n)
        raise NotImplementedError()
    def _calc_pos(self, n, k, table):
        if k == n:
            return 1
        if k == 0:
            return 0

        assert 0 < k < n
        return table[n-1][k-1] + table[n-1][k]*(n-1)
        raise NotImplementedError()
    def _calc_pos_beyond(self, n, k, table):
        return 0
        raise NotImplementedError()
    def direct_calc(self, n, k):
        raise NotImplementedError()
    def row_len(self, n):
        return n+1

    def __init__(self):
        super().__init__([[1]])





#############################################3


class StirlingSubsetNumber(NumberTable):
    def _calc_neg(self, n, k, table):
        if k > 0:
            return 0
        return stirling_circle(-k, -n)
        raise NotImplementedError()
    def _calc_pos(self, n, k, table):
        if k == n:
            return 1
        if k == 0:
            return 0

        assert 0 < k < n
        return table[n-1][k-1] + table[n-1][k]*k
        raise NotImplementedError()
    def _calc_pos_beyond(self, n, k, table):
        return 0
        raise NotImplementedError()
    def direct_calc(self, n, k):
        raise NotImplementedError()
    def row_len(self, n):
        return n+1

    def __init__(self):
        super().__init__([[1]])

'''#'''


####################
stirling_subset = stirling_subset_number = StirlingSubsetNumber()
stirling_circle = stirling_circle_number = StirlingCircleNumber()

#print(stirling_circle.get_first(6))
assert stirling_circle.get_first(len(_sc_data)) == _sc_data

#print(stirling_subset.get_first(6))
assert stirling_subset.get_first(len(_ss_data)) == _ss_data

assert stirling_subset(5, 3) == stirling_circle(-3, -5)
assert stirling_subset(-3, -6) == stirling_circle(6, 3)


######################
######################
######################
######################
#Bell_number
from nn_ns.math_nn.numbers.Stirling_number import stirling_subset
from .INumberList import INumberList__neg2zero, INumberList__nums__concrete_mixins
from .numbers_common import abstract_method, optional_method, override, define

_b_data = [1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975, 678570]
class BellNumber(INumberList__neg2zero, INumberList__nums__concrete_mixins):
    __slots__ = ("nums",)
    @override
    def __please_add_nums_to_slots__(self):
        '__slots__ = (..., "nums")'
    if 0:
        @define
        def __init__(self):
            super().__init__([])
    @define
    def _calc_pos(self, n, nums):
        assert 0 <= n <= len(nums)
        if n < len(nums):
            return nums[n]
        return sum(stirling_subset.get_row(n))
bell_number = BellNumber()
assert bell_number.get_first(len(_b_data)) == _b_data
from nn_ns.math_nn.numbers.Bell_number import bell_number



######################
######################
######################
######################


__all__
from nn_ns.math_nn.numbers.Stirling_number import stirling_subset, stirling_circle
from nn_ns.math_nn.numbers.Stirling_number import stirling_subset_number, stirling_circle_number
from nn_ns.math_nn.numbers.Stirling_number import *

