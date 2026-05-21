
#e ../../python3_src/seed/tiny_/constants.py
__all__ = 'pos_inf  neg_inf'.split()

pos_inf = inf = float('inf')
neg_inf = float('-inf')

def get_inf_():
    return inf
def get_pos_inf_():
    return pos_inf
def get_neg_inf_():
    return neg_inf

from seed.tiny_.constants import inf, pos_inf, neg_inf
from seed.tiny_.constants import get_inf_, get_pos_inf_, get_neg_inf_

