r'''

e ../../python3_src/seed/math/max_power_of_base_as_factor_of_.py

from seed.math.max_power_of_base_as_factor_of_ import max_power_of_base_as_factor_of_, count_num_low_0bits_of_pint, count_num_low_1bits_of_uint, factor_pint_out_2_powers, factor_nonzero_int_out_sign_and_2_powers


view ../../python3_src/nn_ns/math_nn/uint_map.py
!!![max_power_of_base_as_factor_of_ is not floor_log]!!!
    max_power_of_base_as_factor_of_(2,12)==2
    floor_log(2,12)==3
#'''

__all__ = '''
    max_power_of_base_as_factor_of_

    count_num_low_0bits_of_pint
    count_num_low_1bits_of_uint
    factor_pint_out_2_powers
    factor_nonzero_int_out_sign_and_2_powers
    '''.split()


#from nn_ns.math_nn.uint_map import floor_log
from seed.math.sign_of import sign_of


def max_power_of_base_as_factor_of_(base, n, /):
    'base/int{>=2} -> n/pint -> exp/uint #[n%base**exp==0][n%base**(exp+1)=!=0]'
    if not base >= 2: raise ValueError
    if not n >= 0: raise ValueError
    if n == 0:
        return float('inf')
    if not n >= 1: raise ValueError
    exp = -1
    r = 0
    while not r:
        exp += 1
        n, r = divmod(n, base)
    return exp
assert max_power_of_base_as_factor_of_(2, 12) == 2
assert max_power_of_base_as_factor_of_(3, 12) == 1
assert max_power_of_base_as_factor_of_(4, 12) == 1
assert max_power_of_base_as_factor_of_(6, 12) == 1
assert max_power_of_base_as_factor_of_(12, 12) == 1
assert max_power_of_base_as_factor_of_(5, 12) == 0




def count_num_low_0bits_of_pint(u, /):
    if not u > 0: raise ValueError
    low_1s = (u-1)^u
    return low_1s.bit_length()-1


def count_num_low_1bits_of_uint(u, /):
    return count_num_low_0bits_of_pint(u+1)

assert count_num_low_0bits_of_pint(1) == 0
assert count_num_low_0bits_of_pint(3) == 0
assert count_num_low_0bits_of_pint(2) == 1
assert count_num_low_0bits_of_pint(6) == 1
assert count_num_low_0bits_of_pint(4) == 2
assert count_num_low_0bits_of_pint(12) == 2


assert count_num_low_1bits_of_uint(0) == 0
assert count_num_low_1bits_of_uint(2) == 0
assert count_num_low_1bits_of_uint(4) == 0
assert count_num_low_1bits_of_uint(6) == 0
assert count_num_low_1bits_of_uint(1) == 1
assert count_num_low_1bits_of_uint(3) == 2
assert count_num_low_1bits_of_uint(5) == 1
assert count_num_low_1bits_of_uint(7) == 3
assert count_num_low_1bits_of_uint(9) == 1


def factor_pint_out_2_powers(u, /):
    'u/pint -> (e/uint, odd/pint) # [odd%2 == 1][2**e * odd == u]'
    if not u > 0: raise ValueError
    e = count_num_low_0bits_of_pint(u)
    odd = u >> e
    assert odd%2 == 1
    assert 2**e * odd == u
    return (e, odd)

assert factor_pint_out_2_powers(1) == (0, 1)
assert factor_pint_out_2_powers(2) == (1, 1)
assert factor_pint_out_2_powers(3) == (0, 3)
assert factor_pint_out_2_powers(4) == (2, 1)
assert factor_pint_out_2_powers(5) == (0, 5)
assert factor_pint_out_2_powers(6) == (1, 3)


def factor_nonzero_int_out_sign_and_2_powers(i, /):
    'i/int -> (sign/{+1,-1}, e/uint, odd/pint) # [odd%2 == 1][sign * 2**e * odd == u]'
    if i == 0: raise ValueError
    sign = sign_of(i)
    e, odd = factor_pint_out_2_powers(abs(i))
    return (sign, e, odd)
assert factor_nonzero_int_out_sign_and_2_powers(+12) == (+1, 2, 3)
assert factor_nonzero_int_out_sign_and_2_powers(-12) == (-1, 2, 3)

