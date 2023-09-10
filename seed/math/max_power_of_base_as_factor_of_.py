r'''

e ../../python3_src/seed/math/max_power_of_base_as_factor_of_.py

from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_

from seed.math.max_power_of_base_as_factor_of_ import max_power_of_base_as_factor_of_, count_num_low_0bits_of_pint, count_num_low_1bits_of_uint, factor_pint_out_2_powers, factor_nonzero_int_out_sign_and_2_powers


view ../../python3_src/nn_ns/math_nn/uint_map.py
!!![max_power_of_base_as_factor_of_ is not floor_log]!!!
    max_power_of_base_as_factor_of_(2,12)==2
    floor_log(2,12)==3

[[[
https://mathworld.wolfram.com/GreatestCommonDivisor.html
gde(n,b) is the greatest dividing exponent of b in n (Stehlé and Zimmerman 2004).
===
https://mathworld.wolfram.com/GreatestDividingExponent.html
===
Greatest Dividing Exponent
The greatest dividing exponent gde(n,b) of a base b with respect to a number n is the largest integer value of k such that b^k|n, where b^k<=n. It is implemented as the Wolfram Language function IntegerExponent[n, b].

SEE ALSO
Divide, Even Part, Odd Part, p-adic Norm
]]]

py -m nn_ns.app.debug_cmd   seed.math.max_power_of_base_as_factor_of_ -x
py -m nn_ns.app.doctest_cmd seed.math.max_power_of_base_as_factor_of_:__doc__ -ff -v


>>> factor_pint_out_power_of_base_(2, 0b1)
(0, 1)
>>> factor_pint_out_power_of_base_(2, 0b10)
(1, 1)
>>> factor_pint_out_power_of_base_(2, 0b100)
(2, 1)

>>> factor_pint_out_power_of_base_(2, 0b11)
(0, 3)
>>> factor_pint_out_power_of_base_(2, 0b110)
(1, 3)
>>> factor_pint_out_power_of_base_(2, 0b1100)
(2, 3)

>>> factor_pint_out_power_of_base_(2, 0b101)
(0, 5)
>>> factor_pint_out_power_of_base_(2, 0b1010)
(1, 5)
>>> factor_pint_out_power_of_base_(2, 0b10100)
(2, 5)

>>> [factor_pint_out_power_of_base_(3, 1*3**e) for e in range(20)]
[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (18, 1), (19, 1)]
>>> [factor_pint_out_power_of_base_(3, 2*3**e) for e in range(20)]
[(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 2), (11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (17, 2), (18, 2), (19, 2)]
>>> [factor_pint_out_power_of_base_(3, 5*3**e) for e in range(20)]
[(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5), (13, 5), (14, 5), (15, 5), (16, 5), (17, 5), (18, 5), (19, 5)]
>>> [factor_pint_out_power_of_base_(3, 11*3**e) for e in range(20)]
[(0, 11), (1, 11), (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (12, 11), (13, 11), (14, 11), (15, 11), (16, 11), (17, 11), (18, 11), (19, 11)]
>>> [factor_pint_out_power_of_base_(3, 28*3**e) for e in range(20)]
[(0, 28), (1, 28), (2, 28), (3, 28), (4, 28), (5, 28), (6, 28), (7, 28), (8, 28), (9, 28), (10, 28), (11, 28), (12, 28), (13, 28), (14, 28), (15, 28), (16, 28), (17, 28), (18, 28), (19, 28)]
>>> [factor_pint_out_power_of_base_(3, 7777*3**e) for e in range(20)]
[(0, 7777), (1, 7777), (2, 7777), (3, 7777), (4, 7777), (5, 7777), (6, 7777), (7, 7777), (8, 7777), (9, 7777), (10, 7777), (11, 7777), (12, 7777), (13, 7777), (14, 7777), (15, 7777), (16, 7777), (17, 7777), (18, 7777), (19, 7777)]





#'''

__all__ = '''
factor_pint_out_power_of_base_
    max_power_of_base_as_factor_of_
        greatest_dividing_exponent_
            gde_

factor_pint_out_2_powers
    count_num_low_0bits_of_pint
    count_num_low_1bits_of_uint
    factor_nonzero_int_out_sign_and_2_powers

ValidateFail__factor_pint_out_power_of_base_
    verify_result5factor_pint_out_power_of_base_

    '''.split()


#from nn_ns.math_nn.uint_map import floor_log
from seed.math.sign_of import sign_of
from seed.tiny import check_type_is


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






class ValidateFail__factor_pint_out_power_of_base_(Exception):pass
def verify_result5factor_pint_out_power_of_base_(base, n, exp, unfactored_part, /):
    check_type_is(int, base)
    check_type_is(int, n)
    if not base >= 2: raise ValueError
    if not n >= 1: raise ValueError

    check_type_is(int, exp)
    check_type_is(int, unfactored_part)
    if not exp >= 0: raise ValidateFail__factor_pint_out_power_of_base_
    if not unfactored_part >= 1: raise ValidateFail__factor_pint_out_power_of_base_
    if not n == base**exp * unfactored_part: raise ValidateFail__factor_pint_out_power_of_base_
    if unfactored_part%base == 0: raise ValidateFail__factor_pint_out_power_of_base_
def factor_pint_out_power_of_base_(base, n, /):
    'base/int{>=2} -> n/pint -> (exp/uint, unfactored_part) #[n == base**exp * unfactored_part][unfactored_part%base =!= 0]'
    (exp, unfactored_part) = _factor_pint_out_power_of_base_(base, n)
    verify_result5factor_pint_out_power_of_base_(base, n, exp, unfactored_part)
    return (exp, unfactored_part)
def _factor_pint_out_power_of_base_(base, n, /):
    check_type_is(int, base)
    check_type_is(int, n)
    if not base >= 2: raise ValueError
    if not n >= 1: raise ValueError
    if n < base:
        return (0, n)
    if base == 2:
        (e, odd) = factor_pint_out_2_powers(n)
        return (e, odd)

    double_pows = []
    B = base
    #i = 0
    e4i = 1 # = 2**i
    e4acc = 0
    while 1:
        (q, r) = divmod(n, B)
        if not r == 0:
            break
        n = q
        e4acc += e4i
        double_pows.append(B)

        # next round:
        if not B < n:
            break
        B **= 2
        # i += 1
        e4i <<= 1
    if e4acc == 0:
        return (0, n)
    # [len(double_pows) > 0]
    while not n < base:
        # [len(double_pows) > 0]
        # [double_pows[0] == base >= n]
        while n < double_pows[-1]:
            # [len(double_pows) > 1]
            double_pows.pop()
            # [len(double_pows) > 0]
        # [len(double_pows) > 0]
        B = double_pows.pop()
        # [len(double_pows) >= 0]
        (q, r) = divmod(n, B)
        if r == 0:
            n = q
            e4acc += 1 << len(double_pows)
        if not double_pows:break
        # [len(double_pows) > 0]

    return (e4acc, n)

def max_power_of_base_as_factor_of_(base, n, /):
    'base/int{>=2} -> n/pint -> exp/uint #[n%base**exp==0][n%base**(exp+1)=!=0]'
    (exp, unfactored_part) = _factor_pint_out_power_of_base_(base, n)
    return exp

    #
    #old:
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
gde_ = greatest_dividing_exponent_ = max_power_of_base_as_factor_of_



from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
from seed.math.max_power_of_base_as_factor_of_ import *
