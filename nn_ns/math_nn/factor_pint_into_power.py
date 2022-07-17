
r'''
e ../../python3_src/nn_ns/math_nn/factor_pint_into_power.py

from nn_ns.math_nn.factor_pint_into_power import factor_pint_into_power

#'''

__all__ = '''
    factor_pint_into_power
    '''.split()




from nn_ns.math_nn.floor_sqrt import floor_kth_root
from nn_ns.math_nn.prime2 import sorted_primes_lt_N

assert 2** (2 .bit_length()-1) == 2
assert 1<< (2 .bit_length()-1) == 2
def factor_pint_into_power(n, /):
    'n/pint -> (base/pint, exp/pint){n==base**exp}'
    if not n >= 1: raise ValueError
    primes = []
    def recur(n, /):
        if n < 4:
            assert 0 < n < 4
            return (n, 1)
            return (1, 1)
        max_power = n.bit_length()-1
        assert max_power >= 2

        if n == (1<<max_power):
            return (2, max_power)
        max_power -= 1
        assert max_power >= 1

        if max_power == 1:
            assert 4 < n < 8
            return (n, 1)
        assert max_power >= 2

        if not primes:
            primes.extend(sorted_primes_lt_N(max_power +1))
            assert primes

        for p in primes:
            if p > max_power:
                return (n, 1)
            r = floor_kth_root(n, p)
            if r**p == n:
                break
        else:
            return (n, 1)
        (base, exp) = recur(r)
        exp *= p
        return (base, exp)
    (base, exp) = recur(n)
    assert base**exp == n
    return (base, exp)

assert factor_pint_into_power(1) == (1,1)
assert factor_pint_into_power(2) == (2,1)
assert factor_pint_into_power(3) == (3,1)
assert factor_pint_into_power(4) == (2,2)
assert factor_pint_into_power(5) == (5,1)
assert factor_pint_into_power(6) == (6,1)
assert factor_pint_into_power(7) == (7,1)
assert factor_pint_into_power(8) == (2,3)
assert factor_pint_into_power(9) == (3,2)
assert factor_pint_into_power(10) == (10,1)
assert factor_pint_into_power(11) == (11,1)
assert factor_pint_into_power(12) == (12,1)
assert factor_pint_into_power(25) == (5,2)
assert factor_pint_into_power(27) == (3,3)
assert factor_pint_into_power(36) == (6,2)


