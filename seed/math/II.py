
'''

II :: [a] -> (start=1) -> a


functools
    reduce(function, iterable[, initializer])
    # bad! not foldl
seed.iters.fold
    foldl0
seed.iters.binary_op
    foldl
seed.iters.product
    py_sum          py_product
    sum             product
    sum1            product1
    sum_default     product_default
    iter_sum        iter_product
    iter_sum_chain  iter_product_chain
'''

__all__ = 'II'.split()

#from seed.iters.product import py_product as II
from seed.iters.binary_op import foldl
from operator import __mul__

def II(iterable, *, one=1, mul=None):
    if mul is None:
        mul = __mul__
    return foldl(mul, one, iterable)

