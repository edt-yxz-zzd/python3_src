
import operator
from functools import reduce
from itertools import product
import fractions


import math


def sigmoid(x):
    if x < 0:
        return math.exp(x) / (1+math.exp(x))
                
    return 1.0 / (1+math.exp(-x))


    
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


    
def calc_power(I, T_2pow_ls, power:int):
    assert power >= 0
    s = bin(power)[-1:1:-1]

    while len(T_2pow_ls) < len(s):
        T = T_2pow_ls[-1]
        T_2pow_ls.append(T*T)
    assert len(T_2pow_ls) >= len(s)

    '''
    T = I
    for t, c in zip(T_2pow_ls, s):
        if c == '1':
            T = T*t'''
    
    i = s.find('1')
    if i == -1:
        return I
    
    T = T_2pow_ls[i]
    for t, c in zip(T_2pow_ls[i+1:], s[i+1:]):
        if c == '1':
            T = T*t 
    
    return T
