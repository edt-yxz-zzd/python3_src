
__all__ = '''
    calc_common_prefix_length
    '''.split()
import operator
import itertools

def calc_common_prefix_length(lhs_iterable, rhs_iterable, /, *, __eq__=None):
    if __eq__ is None:
        __eq__ = operator.__eq__

    idx = -1
    for a, b, idx in zip(lhs_iterable, rhs_iterable, itertools.count(0)):
        if not __eq__(a, b):
            return idx
    else:
        return idx+1

assert calc_common_prefix_length([], []) == 0
assert calc_common_prefix_length([], [1]) == 0
assert calc_common_prefix_length([1], [1]) == 1
assert calc_common_prefix_length([1,3], [1,2]) == 1

