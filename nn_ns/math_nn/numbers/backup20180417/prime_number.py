
from .numberss import NumberList
from ..floor_sqrt import floor_sqrt
from ..prime2 import primes as _primes
import bisect
import math


_data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

def _delta_fill_primes(primes, upper_I, upper_N):
    N0 = primes[-1] + 1
    N = upper_N
    assert upper_I <= len(primes)
    assert N <= N0*N0
    
    ls = bytearray(b'\1')*(N-N0)
    for i in range(upper_I):
        p = primes[i]
        for n in range((N0+p-1)//p*p - N0, N-N0, p):
            ls[n] = 0

    primes.extend(p for p, b in enumerate(ls, N0) if b)
    return

def delta_fill_primes(primes, upper_N):
    if upper_N < 0:
        return
    if not primes:
        primes.append(2)

    
    while True:
        N0 = primes[-1] + 1
        Nt = N0*N0
        if Nt > upper_N:
            break
        _delta_fill_primes(primes, len(primes), Nt)

    
    upper_divisor = floor_sqrt(upper_N)
    upper_I = bisect.bisect(primes, upper_divisor)
    _delta_fill_primes(primes, upper_I, upper_N)
    return
    
    
            
    
class PrimeNumber(NumberList):
    def fill_len(self, L):
        'PRIME[n] = n-th prime ~ n ln n'
        
        n = len(self.nums)
        if n < L:
            L2 = 2*L
            N = L2 * L2.bit_length()
            delta_fill_primes(self.nums, N)
        assert len(self.nums) >= L
        return

    def fill_until_exceed(self, N):
        delta_fill_primes(self.nums, 2*N)
        assert self.nums[-1] >= N
        

    def __getitem__(self, i):
        return self(i)
    
    def __init__(self):
        super().__init__([2])

    def get_least(self, N):
        self.fill_until_exceed(N)
        return self.nums
    def get_primes_not_exceed(self, N):
        L = self.pi(N)
        return self.get_first(L)
    get_le = get_primes_not_exceed
    
    def pi(self, x):
        'prime_pi(x) = sum [p <= x] {prime p} ~ x/ln x'

        x = math.floor(x)
        nums = self.get_least(x)
        n = bisect.bisect(nums, x)
        assert len(nums) > n
        assert nums[n] > x
        assert n == 0 or nums[n-1] <= x
        return n

        

PRIMES = prime_number = PrimeNumber()
#print(PRIMES.get_first(20))
assert PRIMES.get_first(len(_data)) == _data
assert all(list(_primes(n)) == PRIMES.get_le(n-1) for n in range(20))
assert all(list(_primes(n)) == PRIMES.get_le(n-1) for n in range(203,204))
##n = 203; ps1 = _primes(n); ps2 = PRIMES.get_le(n-1);
##print(len(ps1), len(ps2), ps1[-1], ps2[-1])







