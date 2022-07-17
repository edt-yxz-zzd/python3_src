
r'''
e ../../python3_src/nn_ns/math_nn/Mobius.py
e ../../python3_src/nn_ns/math_nn/factor_int.py
e ../../python3_src/nn_ns/math_nn/mk_coprimes.py

from nn_ns.math_nn.Mobius import Mobius, Mu, Euler_totient_function, phi, II, iter_divisor, iter_Mu, phi
from nn_ns.math_nn.factor_int import factor_int


Euler's totient phi function
    φ(n) or Φ(n)
    Euler_totient_phi_function
Mobius mu function
    Möbius function μ(n)
    Mobius_mu_function
#'''

__all__ = '''
    Mobius_mu_function
        Mobius
        Mu
    II
    iter_Mu

    Euler_totient_phi_function
        Euler_totient_function
        phi
    '''.split()
    #iter_divisor


from itertools import product

from nn_ns.math_nn.factor_pint_into_prime2exp__using_hints import II#, iter_divisors_of, iter_divisor
from nn_ns.math_nn.factor_pint_into_prime2exp__using_hints import factor_pint_into_prime2exp__using_hints



def Mobius_mu_function(n, /, *, hints=()):
    assert n > 0

    d = factor_pint_into_prime2exp__using_hints(n, hints=hints)
    for p, exp in d.items():
        if exp > 1:
            return 0

    return (-1)**len(d)

Mu = Mobius = Mobius_mu_function
assert [Mu(n) for n in [1,2,4,6,8,14,28]] == [1,-1,0,1,0,1,0]



def iter_Mu(n, /, *, hints=()):
    r'iter_Mu n = seq of (Mu d, d) if [d\n][Mu d]'

    assert n > 0

    ##########
    ps = tuple(factor_pint_into_prime2exp__using_hints(n, hints=hints))
    for es in product(*(range(2) for _ in ps)):
        ls = [p for p,e in zip(ps, es) if e]
        yield (-1)**len(ls), II(ls)
    return

    ##########
    ps = tuple(factor_pint_into_prime2exp__using_hints(n, hints=hints))
    for i in range(2**len(ps)):
        bs = [b == '1' for b in reversed(bin(i)[2:])]
        ls = [p for p,b in zip(ps, bs) if b]
        yield (-1)**len(ls), II(ls)
    return



    ##########
    #old-version
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
    return







def Euler_totient_phi_function(n, /, *, hints=()):
    assert n > 0
    d = factor_pint_into_prime2exp__using_hints(n, hints=hints)
    a = II(p-1 for p in d.keys())
    b = II(p for p in d.keys())
    return n//b *a
phi = Euler_totient_function = Euler_totient_phi_function

