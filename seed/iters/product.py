

__all__ = '''
    py_sum          py_product
    sum             product
    sum1            product1
    sum_default     product_default
    iter_sum        iter_product
    iter_sum_chain  iter_product_chain
    '''.split()

from .head_tail import head_tail, forward1, with_default
from .binary_op import foldl, iter_accumulate, iter_accumulate_chain
from operator import __mul__, __add__

py_sum = sum
def sum(start, iterable):
    return foldl(__add__, start, iterable)
def product(start, iterable):
    return foldl(__mul__, start, iterable)
def py_product(iterable, start=1):
    return product(start, iterable)

def product1(iterable): return forward1(product, iterable)
def sum1(iterable): return forward1(sum, iterable)

assert product1([None]) is None
assert product1([3,5]) == 15
assert py_product([3,5]) == 15

def product_default(iterable, default):
    return product1(with_default(iterable, default))

def sum_default(iterable, default):
    return sum1(with_default(iterable, default))
    return forward1_default(sum, iterable, default)

assert product_default([None], []) is None
assert product_default([], None) is None
assert product_default(['2', 3], None) == '222'

def iter_product(start, iterable):
    return iter_accumulate(__mul__, start, iterable)
def iter_sum(start, iterable):
    return iter_accumulate(__add__, start, iterable)
def iter_product_chain(*iterables):
    return iter_accumulate_chain(__mul__, *iterables)
def iter_sum_chain(*iterables):
    return iter_accumulate_chain(__add__, *iterables)



