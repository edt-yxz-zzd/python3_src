
import operator
from functools import reduce
from itertools import product
import fractions # for gcd


def inner_product(u, v):
    return sum(a*b for a, b in zip(u,v))

def numv_product(n, v):
    return [n*b for b in v]
'''
def vsub(u, v):
    return [a-b for a, b in zip(u,v)]

def vadd(u, v):
    return [a+b for a, b in zip(u,v)]
'''

def op_start(op, start, vs):
    return reduce(op, vs, start)
def sub_start(start, *vs):
    return op_start(operator.sub, start, vs)

def add_start(start, *vs):
    return op_start(operator.add, start, vs)
def gcd(vs, start=0):
    return op_start(fractions.gcd, start, vs)

def vmap(f, *vs):
    return tuple(map(f, *vs))

def element_op(op, vs):
    return tuple(map(op, *vs))

def vadd(*vs):
    return element_op(add_start, vs)
def vsub(*vs):
    return element_op(sub_start, vs)


def rproduct(*iterable):
    f = lambda t: tuple(reversed(t))
    return map(f, product(*reversed(iterable)))


