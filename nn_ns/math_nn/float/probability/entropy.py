

'''
assume:
    0*log2(?) = -0
        P=0 <==> "never happen"
        information_of "never happen" == information_of "must happen" == 0

        0**0 == 1
        0*log2(0) == -0
        0*log2(inf) = 0*log2(?/0) = -0 == 1*log2(1)

'''

__all__ = '''
    calc_entropy_from_probability_distribution
    calc_entropy_from_numbers
    '''.split()

from math import isclose, log2
from .probability_distribution import \
    (is_probability_distribution
    ,make_probability_distribution
    )
def calc_entropy_from_probability_distribution(probability_distribution):
    # (probability_distribution::[probability]) -> (num_bits::float)
    assert is_probability_distribution(probability_distribution)
    return -sum(p*log2(p) for p in probability_distribution if 0 < p < 1)
def calc_entropy_from_numbers(nums):
    pd = make_probability_distribution(nums)
    return calc_entropy_from_probability_distribution(pd)

assert isclose(0, calc_entropy_from_numbers([1]*2**0))
assert isclose(1, calc_entropy_from_numbers([1]*2**1))
assert isclose(2, calc_entropy_from_numbers([1]*2**2))
assert isclose(3, calc_entropy_from_numbers([1]*2**3))
assert isclose(4, calc_entropy_from_numbers([1]*2**4))
assert isclose(0, calc_entropy_from_numbers([1,0,0,0]))

