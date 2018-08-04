

'S k z n = sum i**k z**i {i=0->n} = ??'

'''
S k 1 n = sum i**k {i=0->n} = 1/(k+1) (sum C(k+1, i) B[i] n**(k+1-i) {i} - B[k+1])
'''

import sympy
from sympy.abc import k, n, z, j, i
import sympy.abc


# ff = sympy.functions.combinatorial.factorials.FallingFactorial
# rf = RisingFactorial
from sympy import Sum, ff, rf, roots, binomial as C, \
     symbols, factor, factorial, Product, floor, gcd_terms, gcdex

a, b, k, n = symbols('a b k n', positive=True, integer=True)
s = Sum(i**k * z**i, (i, 0, n-1))
ans = s.doit()
q = Sum(i**k * (1-z)**i, (i, 0, n-1))
u = s * (z-1)**(k+1) - n**k*z**n*(z-1)**k

'''
t = ans.euler_maclaurin()
(0**k/2 + z**(n - 1)*(n - 1)**k/2 + Integral(_x**k*z**_x, (_x, 0, n - 1)),
 Abs(-oo*0**k*k - 0**k*log(z)/12 + k*z**(n - 1)*(n - 1)**k/(12*(n - 1)) + z**(n - 1)*(n - 1)**k*log(z)/12))
'''

if 0:
    t = lambda _k = 0: ans.subs(k, _k).doit()
    print(ans)
    for i in range(5):
        print('S(k={k}, z, n) = {s}'.format(k=i, s=t(i)))
elif 0:
    t = lambda _k = 0: q.subs(k, _k).doit()
    print(q)
    for i in range(5):
        print('S(k={k}, 1-z, n) = {s}'.format(k=i, s=t(i)))
elif 0:
    #T d z = sum z**i C(i,d) {~i}
##    test = k
##    ans = test.subs(k,k-1)
##    print(ans)
##    assert ans == k-1
    T = Sum(ff(i,k) * z**i, (i,0,n))
    K = T - ff(n,k)*z**n + k*z* T.subs(k,k-1)
    #ans = K.doit() fail
    for i in range(1,5):
        a = K.subs(n,i).doit().expand(force=True)
        print(a)
elif 0:
    print(Sum(1,(i,0,n-1)).doit())
    T = Sum((-1)**(n-j) * C(j,k), (j,0,n-1))
    T2 = T.subs(n, 2*n)
    T3 = T.subs(n,2*n+1)
    print(T2)
    print(T3)
    for i in range(0,5):
        D = -2*factorial(i)
        a2 = T2.subs(k,i).doit().simplify() #.expand(force=True)
        #print(factor(a))
        b2 = a2.subs(n, n/2)
        print('[even n]: {} = ({})/{}'.format(factor(b2), (b2*D).expand(), D))

        a3 = T3.subs(k,i).doit().simplify()
        b3 = a3.subs(n, (n-1)/2)
        print('[odd n]: {} = {}'.format(factor(b3), gcd_terms(b3.expand())))


    raise
    f = T - (1-(-1)**n)/(-2)**(k+1)
    f *= -2*factorial(k) / Product(n-2*i, (i, 0, floor(k/2)))
    print(f)
    for i in range(0,8):
        a = f.subs(k,i).doit().simplify() #.expand(force=True)
        print(factor(a))

    '''
-2*(-(-2)**(-k - 1)*(-(-1)**n + 1) + Sum((-1)**(-j + n)*binomial(j, k), (j, 0, n - 1)))*k!/Product(-2*i + n, (i, 0, floor(k/2)))
0
1
1
(2*n - 5)/2
n - 2
(2*n**2 - 13*n + 16)/2
(2*n**2 - 12*n + 13)/2
(4*n**3 - 50*n**2 + 176*n - 151)/4
'''

elif 1:
    ''
    def IIe(n, k):
        i = sympy.abc.i
        if k < 1:
            return Product(1, (i,0,0))
        
        return Product(n-2*i, (i,0,k-1))
    def IIo(n, k):
        i = sympy.abc.i
        if k < 1:
            return Product(1, (i,0,0))
        return Product(n-2*i-1, (i,0,k-1))

    for k in range(5):
        fe = IIe(n,k).doit()
        fo = IIo(n,k).doit()
        print('IIe(n,{k})= {f} = {ef}'.format(k=k, f=fe, ef=fe.expand()))
        print('IIo(n,{k})= {f} = {ef}'.format(k=k, f=fo, ef=fo.expand()))
        s,t, g = gcdex(fe, fo)
        assert (s*fe + t*fo).expand() == g.expand() == 1

        s = gcd_terms(s)
        _t = gcd_terms(-t)
        print('({s})*IIe(n,{k}) - ({_t})*IIo(n,{k}) = {g}\n'.format(s=s,_t=_t,g=g,k=k))
        c = (-2 d!/(-2)**d)




    
'''
T d z = sum z**i C(i,d) {~i} for [NN d]
u = z/(1-z)
T d z / u**d = \i:(C - z**i/(1-z) sum C(i, k) / u**k {k=0..d})
assume C=K(z,n) ==>> DD C {d} === 0
T d z / u**d |: 0->n for [NN d,n]
    = 1/(1-z) sum C(0, k) / u**k {k=0..d} - z**i/(1-z) sum C(i, k) / u**k {k=0..d}
    = 1/(1-z) - z**n/(1-z) sum C(n, k) / u**k {k=0..d}
T d z n = (T d z / u**d |: 0->n) * u**d, for [NN d,n]
    = u**d/(1-z) - z**n/(1-z) sum C(n,k) u**(d-k) {k=0..d}
=?= sum z**i C(i,d) {~i=0->n} for [NN d,n]
0 =?= T d z 0 = u**d/(1-z) - 1/(1-z) sum C(0,k) u**(d-k) {k=0..d} = 0; yes
z**n C(n,d) =?= T d z (n+1) - T d z n
    = z**n/(1-z) sum (C(n,k)-C(n+1,k)z) u**(d-k) {k=0..d}
    = z**n/(1-z) sum (C(n,k)-C(n,k-1)z-C(n,k)z) u**(d-k) {k=0..d}
    = z**n/(1-z) sum C(n,k)(1-z) u**(d-k) {k=0..d}
        - z**n/(1-z) sum C(n,k-1)z u**(d-k) {k=0..d}
    = z**n sum C(n,k) u**(d-k) {k=0..d}
        - z**n sum C(n,k-1) u**(d+1-k) {k=0..d}
    = z**n sum C(n,k) u**(d-k) {k=0..d}
        - z**n sum C(n,k) u**(d-k) {k=-1..d-1}
    = z**n C(n,d) - z**n C(n,-1) u**(d+1)
        [NN n] ==>> C(n,-1) = 0
    = z**n C(n,d); yes

'''

'''
s = Sum(i**k * z**i, (i, 0, n-1))
(z**n     - 1)/(z - 1)
(n*z*z**n - n*z**n      - z*z**n + z)/(z - 1)**2 = ((z-1)n*z**n - z(z**n-1))/()**2
    z=1: (n*z**n + (z-1)n*n*z**(n-1) - (z**n-1) - n*z**n)/()/2
    = n*n*z**(n-1)/2 - n*z**(n-1)/2 = n*n/2 - n/2

    n*z*z**n - n*z**n = n*z**n(z-1)
    -z(z**n-1)
(n**2*z**2*z**n - 2*n**2*z*z**n + n**2*z**n
 - 2*n*z**2*z**n + 2*n*z*z**n
 + z**2*z**n - z**2 + z*z**n - z)/(z - 1)**3
    n**2*z**n(z**2 - 2*z + 1) = n**2*z**n (z-1)**2
    -2*n*z**n(z - 1)*z
    z**2*z**n - z**2 + z*z**n - z = z(z+1)(z**n - 1)
    
(n**3*z**3*z**n - 3*n**3*z**2*z**n + 3*n**3*z*z**n - n**3*z**n
 - 3*n**2*z**3*z**n + 6*n**2*z**2*z**n - 3*n**2*z*z**n
 + 3*n*z**3*z**n - 3*n*z*z**n
 - z**3*z**n + z**3 - 4*z**2*z**n + 4*z**2 - z*z**n + z)/(z - 1)**4
    n**3*z**n(z-1)**3 = n**3*z**n(z-1)**3*sum Eulerian<0,i>z**(0-i){i}
    - 3*n**2*z**n(z-1)**2*z
        = - 3*n**2*z**n(z-1)**2*sum Eulerian<1,i>z**(1-i){i}
    + 3*n*z**n(z**2-1)*z ?????
        = 3*n*z**n(z-1)*sum Eulerian<2,i>z**(2-i){i}
    -(z**3+4*z**2+z)(z**n - 1) = -sum Eulerian<3,i>z**(3-i){i}(z**n - 1)

(n**4*z**4*z**n - 4*n**4*z**3*z**n + 6*n**4*z**2*z**n - 4*n**4*z*z**n + n**4*z**n
 - 4*n**3*z**4*z**n + 12*n**3*z**3*z**n - 12*n**3*z**2*z**n + 4*n**3*z*z**n
 + 6*n**2*z**4*z**n - 6*n**2*z**3*z**n - 6*n**2*z**2*z**n + 6*n**2*z*z**n
 - 4*n*z**4*z**n - 12*n*z**3*z**n + 12*n*z**2*z**n + 4*n*z*z**n
 + z**4*z**n - z**4 + 11*z**3*z**n - 11*z**3 + 11*z**2*z**n - 11*z**2 + z*z**n - z)/(z - 1)**5
    n**4*z**n(z-1)**4
    -4*n**3*z*z**n(z-1)**3
    6*n**2*z**n(z**4-z**3-z**2+z) = 6*n**2*z**n(z**3(z-1)-z(z-1))
        = 6*n**2*z**n(z**2-1)z(z-1)
        = 6*n**2*z**n(z-1)**2(z**2+z)
        = 6*n**2*z**n(z-1)**2*sum Eulerian<2,i>z**(2-i){i}
    -4*n*z**n(z**4+3z**3-3z**2-z) = -4*n*z**n(z**3+3z**2-3z-1)z
        = -4*n*z**n(z - 1)*(z**2 + 4*z + 1)z
        = -4*n*z**n(z - 1)*sum Eulerian<3,i>z**(3-i){i}
    (z**n - 1)(z**4+11*z**3+11*z**2+z) = (z**n - 1)sum Eulerian<4,i>z**(4-i){i}


(z-1)**k * Sum(i**k * z**i, (i, 0, n-1)) =
    z**n*sum C(k,j)*(-1)**(k-j) * n**j * (z-1)**j * sum Eulerian<k-j,v>z**(k-j-v){v}{j}
    -(-1)**k * sum Eulerian<k,v>z**(k-v){v}
(1-z)**k * Sum(i**k * z**i, (i, 0, n-1)) =
    z**n*sum C(k,j) * n**j * (1-z)**j * sum Eulerian<k-j,v>z**(k-j-v){v}{j}
    - sum Eulerian<k,v>z**(k-v){v}
'''

if __name__ == '__main__':pass
