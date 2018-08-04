
from itertools import product
def collect_multi(iterables):
    lsls = list(map(frozenset, iterables))
    s = set()
    L = len(lsls)
    for i, ls0 in enumerate(lsls):
        for j in range(i+1, L):
            ls1 = lsls[j]
            ls = ls0 & ls1
            s |= ls

    return s

