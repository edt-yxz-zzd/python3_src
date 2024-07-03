#__all__:goto
r'''[[[
e ../../python3_src/seed/math/pow__via_binomial_formula.py
    #二项式定理
    #binomial formula
    #binomial theorem
    #binomial coefficient


used in:
    view ../../python3_src/seed/math/polynomial/simple_polynomial.py

seed.math.pow__via_binomial_formula
py -m nn_ns.app.debug_cmd   seed.math.pow__via_binomial_formula -x
py -m nn_ns.app.doctest_cmd seed.math.pow__via_binomial_formula:__doc__ -ht
py_adhoc_call   seed.math.pow__via_binomial_formula   @f

#]]]'''
__all__ = r'''
iter_parts5pow__via_binomial_formula__
iter_counted_parts5pow__via_binomial_formula_

'''.split()#'''
__all__

from functools import reduce
from seed.tiny import check_type_is
from seed.math.combination import factorial, iter_partitions_of_sum_




def iter_parts5pow__via_binomial_formula__(part5int, mul4part, parts, exp, /):
    '(int->x) -> (x->x->x) -> [x]{len>=2} -> uint{>=2} -> Iter x'
    for r, part in iter_counted_parts5pow__via_binomial_formula_(mul4part, parts, exp):
        part8r = part5int(r)
        part = mul4part(part, part8r)
        yield part
def iter_counted_parts5pow__via_binomial_formula_(mul4part, parts, exp, /):
    '(x->x->x) -> [x]{len>=2} -> uint{>=2} -> Iter (uint, x)'
    check_type_is(tuple, parts)
    check_type_is(int, exp)
    if not len(parts) >= 2:raise ValueError
    if not exp >= 2:raise ValueError
    #one8part = part5int(1)
    one8part = Nothing = object()
    j2k2part = tuple([one8part, part] for part in parts)
    for part, k2part in zip(parts, j2k2part):
        part_ = part
        for _ in range(exp-1):
            part_ = mul4part(part, part_)
            k2part.append(part_)
        assert len(k2part) == 1+exp
    ...
    M = exp
    L = len(parts)
    def __(M, L, j2k2part, one8part):
      for ks in iter_partitions_of_sum_(M, L):
        assert len(ks) == L
        s = M
        r = factorial(s)
        j2part = []
        for k, k2part in zip(ks, j2k2part):
            r //= factorial(k)
            s -= k
            j2part.append(k2part[k])
        assert s == 0
        j2part
        parts = [part for part in j2part if part is not one8part]
        assert len(parts)
        part = reduce(mul4part, parts)
        yield (r, part)
    it8parts = __(M, L, j2k2part, one8part)
    return it8parts


__all__
from seed.math.pow__via_binomial_formula import iter_parts5pow__via_binomial_formula__
from seed.math.pow__via_binomial_formula import *
