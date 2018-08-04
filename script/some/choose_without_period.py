
r'''

NT n k = n choose k with min period n
    001001 is not counted in (NT 6 2), since it has a period 3
    [n>=0] ==>> NT n k = NT n (n-k)
    [k<0] ==>> NT n k = 0
    [n>0] ==>> [n\(NT n k)], since 10000 -> 01000 -> 00100 -> ... are diff with each other
    
    NT n 0 = [n=0] + [n=1]
    NT n 1 = [n>=0]n
    NT n 2 = C(n,2) - [2\n](NT n/2 1) = C(n,2) - [2\n][n>=0]n/2
        = [n>=0]((n-1) - [2\n])n/2
        = [n>=0](n - (3+(-1)**n)/2)n/2

    [period\n][(n/period)\k] ==>> [(n/period)\n] ==>> [(n/period)\gcd(n,k)]
        [(n/gcd(n,k))\period]
        ==>> min period = n/gcd(k,n)
    
    C(n, k) = sum NT (n/d) (k/d) {d\gcd(n,k)}
    [k _L n] ==>> 
        NT n k = C(n,k)
        C(n*g, k*g) = sum NT (n*d) (k*d) {d\g}
    
        let CN n k g = C(n*g,k*g), NTN n k g = NT (n*g) (k*g)
        CN n k = DS (NTN n k)
        ==>> NTN n k = DSM (CN n k) = \x:sum Mu d * CN n k (x/d) {d\x}
        NT (n*g) (k*g) = NTN n k g = sum Mu d * CN n k (g/d) {d\g}
            = sum Mu d * C(n*g/d, k*g/d) {d\g}
    NT n k = sum Mu d * C(n/d, k/d) {d\gcd(n,k)}    for [(n,k)!=(0,0)]
        NT 1 0 =?= Mu 1 * C(1/1, 0) = 1; True
        [n>0] ==>> NT n 0 =?= sum Mu d * C(n/d, 0) {d\n} = sum Mu d {d\n} = [n=1]; True
        [n<0] ==>> now define...
        [k != 0] ==>> NT 0 k =?= sum Mu d * C(0, k/d) {d\k} = 0; True
        leave NT 0 0 undefined


    it seems [CMath page363]7.70 is right but deduce is wrong.
    let n=m=L=2, that is n (1-m)'s = (2 * -1) and (m*n+L-n) +1's = (4 * +1)
    NT 6 2 = sum Mu d * C(6/d, 2/d) {d\2} = Mu 1 * C(6,2) + Mu 2 * C(3,1)
        = 15 - 3 = 12
    NT 3 1 = 3
    (NT 6 2)/6 * 2/(6/6) + (NT 3 1)/3 * 2/(6/3)= 5 =?= C(6,2)*2/6; True

    
    num of circles of "01" of len (m*n+L) with n 1's without period: 
        (NT (m*n+L) n)/(m*n+L)

    num of circles of "01" of len (m*n+L) with n 1's:
        sum (NT ((m*n+L)/d) (n/d))/((m*n+L)/d) * L/d {d\gcd(m*n+L,n)} =?= C(m*n+L, n)*L/(m*n+L)
        left = L/(m*n+L) sum (NT ((m*n+L)/d) (n/d)) {d\gcd(L,n)} = right




'''

from Mobius import iter_Mu, iter_divisor
from fractions import gcd as _gcd
from sympy import binomial as C, gcd as gcds
from nn_ns.math_nn import primes
from sympy.abc import n

gcd = lambda x,y: abs(_gcd(x,y))

def choose_without_period(n,k):
    r'''NT n k = sum Mu d * C(n/d, k/d) {d\gcd(n,k)}    for [(n,k)!=(0,0)]
NT 0 0 = 1
'''
    if (n,k) == (0,0):
        return 1
    
    return sum(Mu_d * C(n//d, k//d) for Mu_d, d in iter_Mu(gcd(n,k)))

NT = choose_without_period

assert NT(6,2) == 12



def _DS_d_NT(n,k):
    r'sum d * NT (n/d) (k/d) {d\gcd(n,k)}'
    assert (n,k) != (0,0)
    return sum(d * NT(n//d, k//d) for d in iter_divisor(gcd(n,k)))

def _call_DS_d_NT(N):
    print(_DS_d_NT.__doc__)
    for n in range(1, N):
        print('n = {}'.format(n))
        ls=[_DS_d_NT(n,k) for k in range(n+1)]
        g = gcds(ls)
        ls = [x//g for x in ls]
        print('{ls}*{gcd}'.format(ls=ls, gcd=g))

        ls2 = [NT(n,k) for k in range(n+1)]
        g2 = gcds(ls2)
        ls2 = [x//g for x in ls2]
        assert g == g2
        ds = [x-y for x,y in zip(ls, ls2)]
        print(r'...-[NT(n,\k)] = {ls}*{gcd}'.format(ls=ds, gcd=g2))
        continue
        if ls2 == ls:
            print(r'==[NT(n,\k)]')
        else:
            print(r'[NT(n,\k)] = {ls}*{gcd}'.format(ls=ls2, gcd=g2))
               

def _call_NT(N):
    for n in range(N):
        ls = [NT(n,k) for k in range(n+1)]
        g = gcds(ls)
        ls = [x//g for x in ls]
        print(r'[NT({n},\k)] = {ls}*{gcd}'.format(n=n, ls=ls, gcd=g))

#_call_NT(20)


def _show_NT_np_p2(max_p):
    '''[n>=p**2]: NT(n,p**2) = C(n,p**2) - [p\n]C(n/p,p)

[n>=p]: NT(n*p,p**2) = C(n*p,p**2) - C(n,p)
'''

    for p in primes(max_p):
        f = C(n*p,p**2) - C(n,p)
        g = f.factor()
        print('NT(n*p, {p}**2) = {f}'.format(p=p, f=g))


_show_NT_np_p2(6)










