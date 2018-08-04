
__all__ = '''
    is_probability_distribution
    make_probability_distribution

    is_plurality_values
    expectation_of
    '''.split()

from math import isclose
from .has_positive_len import has_positive_len

def is_normalized_probability_distribution(probability_distribution):
    return (has_positive_len(probability_distribution)
        and all(0 <= p <= 1 for p in probability_distribution)
        and isclose(1, sum(probability_distribution))
        )

def is_probability_distribution(probability_distribution):
    return (has_positive_len(probability_distribution)
        and all(p >= 0 or isclose(p,0) for p in probability_distribution)
        and all(p <= 1 or isclose(p,1) for p in probability_distribution)
        and isclose(1, sum(probability_distribution))
        )
'''
def check_probability_distribution(probability_distribution):
    if not has_positive_len(probability_distribution):
        # not iterable
        raise ValueError('probability_distribution should not be empty')
    if not all(p >= 0 or isclose(p,0) for p in probability_distribution):
        raise ValueError('probability < 0')
    if not all(p <= 1 or isclose(p,1) for p in probability_distribution):
        raise ValueError('probability > 1')
    if not isclose(1, sum(probability_distribution)):
        raise ValueError('sum != 1')
'''
def make_probability_distribution(nums):
    # normalize nums
    # nums :: Num a => [a]
    #   e.g. plurality values
    if not has_positive_len(nums): raise TypeError
    if not all(n >= 0 for n in nums): raise TypeError
    SUM = sum(nums)
    if not (SUM > 0): raise TypeError

    probability_distribution = tuple(n/SUM for n in nums)
    assert is_normalized_probability_distribution(probability_distribution)
    return probability_distribution

def normalize_probability_distribution(probability_distribution):
    if not is_probability_distribution(probability_distribution): raise TypeError

    pd = tuple(0 if p < 0 else (1 if p > 1 else p)
            for p in probability_distribution)
    return make_probability_distribution(probability_distribution)

    if not is_normalized_probability_distribution(pd):
        raise ValueError('input probability_distribution is bad')
    return pd

