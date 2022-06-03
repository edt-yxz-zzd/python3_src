
r'''
from seed.tiny_.default_cmp import default_cmp

used in:
    seed.algo.merge_sort
        echo as default key()
        default_cmp as default cmp()

#'''

def default_cmp(a, b, /):
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return +1

from seed.tiny_.default_cmp import default_cmp


