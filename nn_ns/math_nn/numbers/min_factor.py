
r'''[[[

e ../../python3_src/nn_ns/math_nn/numbers/min_factor.py
nn_ns.math_nn.numbers.min_factor
py -m nn_ns.math_nn.numbers.min_factor
from nn_ns.math_nn.numbers.min_factor import min_factor, factor_uint__via_min_factor_list

#]]]'''
__all__ = '''
    min_factor
    factor_uint__via_min_factor_list
    '''.split()

from .numberss import NumberList
from .prime_number import PRIMES
from ..floor_sqrt import floor_sqrt
from ..prime1 import min_prime_factor as _min_prime_factor
from seed.math.II import II
from collections import Counter
from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
from seed.math.floor_ceil import floor_log2
from nn_ns.math_nn.prime2 import primes_lt, floor_sqrt


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



def factor_uint__via_min_factor_list(u, /, *, turnon__try_div=False, may_upperbound4primes4try_div=None, may_primes4try_div=None, threshold4max_sz4min_factor = (1<<28)):
    if not u >= 1: raise ValueError

    u1 = u
    if turnon__try_div:
        if not (may_primes4try_div is None or may_upperbound4primes4try_div is None): raise TypeError
        if may_primes4try_div is not None:
            ps = may_primes4try_div
        else:
            if may_upperbound4primes4try_div is not None:
                U = may_upperbound4primes4try_div
                U = max(1, U)
            else:
                q = u1
                # copy from:view ../../python3_src/nn_ns/math_nn/inv_phi.py
                #####
                q_sub1 = q-1
                U = 1+min(q_sub1//2+1, 2*floor_log2(q)+2)
                #####
            if u1 < ((U-1)<<1) or u1 < (U-1)**2:
                U = floor_sqrt(u1)+1
            ps = primes_lt(U)
        ps
        (p2e_, u) = semi_factor_pint_via_trial_division(ps, u1)
    else:
        p2e_ = {}


    if u >= threshold4max_sz4min_factor and len(min_factor.get_nums()) <= u: raise ValueError('too big to factor via min_factor') #这里的u是经过『试除』不完全分解后剩下的未分解部分

    u0 = u
    ls = []
    while not u == 1:
        p = min_factor(u)
        ls.append(p)
        u //= p
    p2e = {**Counter(ls)}
    if not u0 == II(p**e for p,e in p2e.items()): raise logic-err#ValueError

    p2e.update(p2e_)
    if not u1 == II(p**e for p,e in p2e.items()): raise logic-err#ValueError
    return p2e

assert factor_uint__via_min_factor_list(630) == {2:1,3:2,5:1,7:1}
assert factor_uint__via_min_factor_list(630, turnon__try_div=True) == {2:1,3:2,5:1,7:1}
assert factor_uint__via_min_factor_list(630, turnon__try_div=True, may_upperbound4primes4try_div=4) == {2:1,3:2,5:1,7:1}
assert factor_uint__via_min_factor_list(630, turnon__try_div=True, may_upperbound4primes4try_div=666) == {2:1,3:2,5:1,7:1}
assert factor_uint__via_min_factor_list(630, turnon__try_div=True, may_primes4try_div=[3,5]) == {2:1,3:2,5:1,7:1}

