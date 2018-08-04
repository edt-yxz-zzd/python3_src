

'''
H[p-1] mod p**2 == ?
(p-1)! mod p**2 == ?
Stirling[p>2,2] = (p-1)! H[p-1]

'''


from nn_ns.math_nn import primes, invmod, power
from factorial import factorial
from Stirling_numbers import Stirling_circle


def list_inv_pairs(p, k):
    p2 = p**2
    ls = []
    base = p*k
    E = p**2 - p - 1
    for i in range(base+1, base+p):
        r = invmod(i, p2)
        r2 = pow(i, E, p2)
        assert r == r2
        ls.append(divmod(r, p))
    return ls


for p in primes(100):
    ls = (list_inv_pairs(p, 3))
    assert len(set(pair[1] for pair in ls)) == p-1
    ls = list(pair[0] for pair in ls)
    s = sum(ls) + (p-1)//2
    print(s%p==0, s%p**2!=0)
    #print(sorted(ls))
raise


def H_mod_powE(p, E):
    s = 0
    M = p**E
    for i in range(1, p):
        s += invmod(i, M)
    s %= M
    return s

def t(N):
    for p in primes(N):
        if H_mod_powE(p,2):
            print(p)
        elif H_mod_powE(p,3)==0:
            print(p)
            
    
def t1(N):
    for n in primes(N):
        if Stirling_circle(n,2)%n**2:
            print(n)

t(1000)


            
raise
for p in primes(100):
    r = factorial(p-1) % p**2
    nr = r-p**2
    assert r % p == p-1
    print(p, r, nr)

    s = Stirling_circle(p,2)
    inv_r = invmod(r, p**2)
    Hp_1 = (s*inv_r) % p**2
    print(p, s, s%p**2, inv_r, Hp_1)
