
from sympy import factorint as factor_int, sympify

def factor_frac(f):
    'this version using sympy'
    N, D = fraction(sympify(f))
    ns = factor_int(N)
    ds = factor_int(D)
    assert not (set(ns) & set(ds))
    ns.update((k,-v) for k,v in ds.items())
    return ns
