
from sympy import factorint
from itertools import product


def Mobius(n):
    assert n > 0

    d = factorint(n)
    for p, exp in d.items():
        if exp > 1:
            return 0

    return (-1)**len(d)

Mu = Mobius
assert [Mu(n) for n in [1,2,4,6,8,14,28]] == [1,-1,0,1,0,1,0]


def II(ns, one=None):
    if one is None:
        one = 1

    ns = iter(ns)
    for prod in ns:
        break
    else:
        return one

    for x in ns:
        prod *= x
    
    return prod


def iter_divisor(n):
    r'iter_divisor(n) = [d if [d\n]]'

    p_exp_ls = tuple(factorint(n).items())
    ps = tuple(p for p,e in p_exp_ls)
    for es in product(*(range(e+1) for p,e in p_exp_ls)):
        #print(es)
        yield II(p**e for p,e in zip(ps, es))
    pass

        

def iter_Mu(n):
    r'iter_Mu n = seq of (Mu d, d) if [d\n][Mu d]'
    
    assert n > 0

    ps = tuple(factorint(n))
    for es in product(*(range(2) for _ in ps)):
        ls = [p for p,e in zip(ps, es) if e]
        yield (-1)**len(ls), II(ls)
    return





    
    L = 2**len(ps)
    for i in range(L):
        s = bin(i)[2:]
        d = 1
        Mu_d = 1
        for p, b in zip(ps, reversed(s)):
            if b == '1':
                d *= p
                Mu_d = -Mu_d
        yield Mu_d, d

    pass






    
