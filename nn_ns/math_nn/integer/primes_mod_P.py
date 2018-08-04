

import itertools

from root.prime2 import primes as sorted_primes_lt_N
from sand import is_main
from .error import NotPrimeError
from .mod import mulmod, all_powers_mod_N as list_all_powers_mod_N




def primes_mod_P_define(P):
    ps = sorted_primes_lt_N(P+1)
    if ps[-1] != P:
        raise NotPrimeError('P')



    remains = frozenset(range(2, P-1)) # skip -1, 0, 1
    primes_mod_P = []
    n_covered = set()
    while remains:
        p = min(remains)
        primes_mod_P.append(p)

        powers = list_all_powers_mod_N(p, P)
        powers = set(powers)
        
        powers_ = powers - n_covered
        n_covered_ = n_covered - powers
        new_covered = set()
        for power, n in itertools.product(powers_, n_covered_):
            new_covered.add(mulmod(power, n, P))

        new_covered -= n_covered
        new_covered |= powers_
        new_covered.update([-n for n in new_covered])
        assert not (new_covered & n_covered)
        
        n_covered |= new_covered # == {-1**x * product(p**e for p in primes_mod_P) mod P}
        remains -= new_covered
        pass

    if P > 3:
        assert primes_mod_P

    assert set(primes_mod_P) < set(ps)
    return primes_mod_P


def _try_primes_mod_P_define(N):
    ls = []
    for p in sorted_primes_lt_N(N):
        primes_mod = primes_mod_P_define(p)
        ls.append((p, primes_mod))
    return ls

def _show_primes_mod_P_define(N):
    for p, primes_mod in _try_primes_mod_P_define(N):
        _show_p_primes_mod(p, primes_mod)
    return
def _show_p_primes_mod(p, primes_mod):
    print(p)
    print(primes_mod)
    return

def main_for_primes_mod_P_define(args = None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='show result of primes_mod_P_define(P)')
    parser.add_argument('N', type = int, nargs='?',
                        default = 100, 
                        help='try all prime P less than N')
    
    parser.add_argument('-p', '--prime', type = int, \
                        default = None,
                        help='try prime p')


    if args == None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

        

    p = args.prime
    N = args.N
    if p == None:
        _show_primes_mod_P_define(N)
    else:
        primes_mod = primes_mod_P_define(p)
        _show_p_primes_mod(p, primes_mod)

    return 0
    


if is_main(__name__):
    main_for_primes_mod_P_define()
    
        

    
    
