
#e ../../python3_src/seed/iters/are_all_the_same.py

from itertools import pairwise, starmap
import operator

def are_all_the_same(iterable, /, *, __eq__=None):
    if __eq__ is None:
        __eq__ = operator.__eq__
    return all(starmap(__eq__, pairwise(iterable)))


from seed.iters.are_all_the_same import are_all_the_same

