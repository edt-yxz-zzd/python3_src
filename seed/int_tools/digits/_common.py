
r'''
py -m seed.int_tools.digits.radix_repr2uint
from seed.int_tools.digits._common import _Int, _pow_ge1
e ../../python3_src/seed/int_tools/digits/_common.py
    _Int, _pow_ge1
#'''
__all__ = '''
    _Int
    _pow_ge1
    '''.split()

class _Int:
    def __init__(sf, i, /):
        if type(i) is not int: raise TypeError(f'{type(i)}:{i!r}')
        sf.i = i
    def __eq__(sf, rhs, /):
        return sf.i==rhs.i
    def __hash__(sf, /):
        return hash(sf.i)
    def __repr__(sf, /):
        return f'_Int({sf.i})'

import functools


assert bin(1) =='0b1'
def _pow_ge1(mul, pows, exp):
    r'''
    input:
        mul
        pows = [base**2**i for i in range(len(pows))]
        exp >= 0
    output:
        base**exp
    #'''
    if not exp >= 1: raise ValueError
    bits = bin(exp)[2:]
    assert bits
    assert bits[0]=='1'
    if not len(bits) <= len(pows):raise ValueError
    ls = [weight for bit, weight in zip(reversed(bits), pows) if bit=='1']
    assert ls
    return functools.reduce(mul, ls)


