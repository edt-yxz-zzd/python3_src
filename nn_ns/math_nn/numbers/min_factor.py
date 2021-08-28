


from .numberss import NumberList
from .prime_number import PRIMES
from ..floor_sqrt import floor_sqrt
from ..prime1 import min_prime_factor as _min_prime_factor


_data = [0, 1, 2, 3, 2, 5, 2, 7, 2, 3, 2, 11, 2, 13, 2, 3, 2, 17, 2, 19]

def delta_fill_minfactors(minfactors, L):
    if len(minfactors) < L:
        N = L
        N0 = len(minfactors)
        ls = [0]*(N-N0)
        max_prime = floor_sqrt(N)
        upper_I = PRIMES.pi(max_prime)

        for i in range(upper_I-1, -1, -1):
            p = PRIMES[i]
            for n in range((N0+p-1)//p*p - N0, N-N0, p):
                ls[n] = p


        minfactors.extend(p if p else n for n, p in enumerate(ls,N0))
    return




class MinFactor(NumberList):
    'min_factor(n) = abs(n) if -2<n<2 else the minimum prime factor of abs(n)'

    def _lookup_neg(self, n, nums):
        assert n < 0
        return nums[-n]

    def _calc_neg(self, n, nums):
        assert n < 0
        return self._calc_pos(-n, nums)
        raise NotImplementedError()

    def _fill_when_neg(self, n):
        self.fill_len(-n+1)

    def fill_len(self, L):
        n = len(self.nums)
        if n < L:
            L2 = 2*L
            delta_fill_minfactors(self.nums, L2)
        assert len(self.nums) >= L
        return


    def __init__(self):
        super().__init__([0,1])





min_factor = MinFactor()
#print(min_factor.get_first(20))
assert min_factor.get_first(len(_data)) == _data
assert all(list(_min_prime_factor(n)) == min_factor.get_first(n) for n in range(20))
assert all(list(_min_prime_factor(n)) == min_factor.get_first(n) for n in range(203,204))
assert all(min_factor(-n) == min_factor(n) for n in range(20))
##n = 203; ps1 = _primes(n); ps2 = PRIMES.get_le(n-1);



