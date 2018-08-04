

from fractions import Fraction as __fr
import functools
from .numberss import NumberList


_k2_data = [0, 1, 4, 9, 16, 25]
_i2_data = [1, 2, 4, 8, 16, 32]

class _Pow_i_const_k(NumberList):
    def _calc_neg(self, n, nums):
        return self.direct_calc(n)
        raise NotImplementedError()
    def _calc_pos(self, n, nums):
        return self.direct_calc(n)
        raise NotImplementedError()
    def direct_calc(self, n):
        return n**self.__k
        raise NotImplementedError()

    
    def __init__(self, k):
        self.__k = k
        super().__init__([])
class _Pow_const_i_k(NumberList):
    def _calc_neg(self, n, nums):
        return self.direct_calc(n)
        raise NotImplementedError()
    def _calc_pos(self, n, nums):
        return self.direct_calc(n)
        raise NotImplementedError()
    def direct_calc(self, n):
        if n > 0:
            return self.__i ** n
        elif n < 0:
            return __fr(1, self.__i ** -n)
        else:
            assert n == 0
            return 1 # so, 0**0 == 1
        raise NotImplementedError()

    
    def __init__(self, i):
        self.__i = i
        super().__init__([])


@functools.lru_cache(maxsize=None, typed=False)
def __Pow_i_const_k(k):
    return _Pow_i_const_k(k)

def Pow_i_const_k(k):
    assert isinstance(k, int)
    k = int(k)
    assert k >= 0
    return __Pow_i_const_k(k)
    

@functools.lru_cache(maxsize=None, typed=False)
def __Pow_const_i_k(k):
    return _Pow_const_i_k(k)

def Pow_const_i_k(k):
    assert isinstance(k, int)
    k = int(k)
    assert k >= 0
    return __Pow_const_i_k(k)




pow_i_2 = Pow_i_const_k(2)
#print(pow_i_2.get_first(6))
assert pow_i_2.get_first(len(_k2_data)) == _k2_data

pow_2_k = Pow_const_i_k(2)
#print(pow_2_k.get_first(6))
assert pow_2_k.get_first(len(_i2_data)) == _i2_data




    
