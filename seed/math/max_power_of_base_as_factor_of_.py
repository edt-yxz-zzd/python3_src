r'''

e ../../python3_src/seed/math/max_power_of_base_as_factor_of_.py

from seed.math.max_power_of_base_as_factor_of_ import max_power_of_base_as_factor_of_

view ../../python3_src/nn_ns/math_nn/uint_map.py
!!![max_power_of_base_as_factor_of_ is not floor_log]!!!
    max_power_of_base_as_factor_of_(2,12)==2
    floor_log(2,12)==3
#'''

__all__ = '''
    max_power_of_base_as_factor_of_
    '''.split()


#from nn_ns.math_nn.uint_map import floor_log


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






