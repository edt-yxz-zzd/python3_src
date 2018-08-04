

'''
Stirling polynomial

[NN n]:
    Stirling{x, x-n} = sum Eulerian<<n,k>> C(x+n-1-k, 2n) {k}
    Stirling[x, x-n] = sum Eulerian<<n,k>> C(x+k, 2n) {k}

[NN n>0]:
    Stirling[x, x-n]/fall(x, n+1)
    Stirling{x, x-n}/fall(x, n+1)

    Stirling_polynomial(n, z) = Stirling[z, z-n]/fall(z, n+1)
    Stirling_subset_polynomial(n, z) = Stirling[z, z-n]/fall(z, n+1)

    Stirling{x, x-n} = Stirling[n-x, -x] = Stirling[n-x, (n-x)-n]
    Stirling_subset_polynomial(n, z) = Stirling[n-z, (n-z)-n]/fall(z, n+1)
        = Stirling_polynomial(n, n-z) fall((n-z), n+1) /fall(z, n+1)
        = Stirling_polynomial(n, n-z) (-1)**(n+1)
        
'''
import sympy
from sympy.abc import k, n, z, j, i, x, y
import sympy.abc


# ff = sympy.functions.combinatorial.factorials.FallingFactorial
# rf = RisingFactorial
from sympy import Sum, ff, rf, roots, binomial as C, \
     symbols, factor, factorial, Product, floor, gcd_terms, gcdex
from sympy import Function, sympify, cos, summation, S


from nn_ns.math_nn.numbers.Eulerian_number import eulerian_2nd



a, b, k, n = symbols('a b k n', positive=True, integer=True)

class Eulerian2nd(Function):
    nargs = 2
    @classmethod
    def eval(cls, n, k):
        n = sympify(n)
        k = sympify(k)
        if not n.is_integer:
            raise TypeError('n is not integer')
        if not k.is_integer:
            raise TypeError('k is not integer')
        
        if n < 0:
            raise ValueError('n<0')
        return eulerian_2nd(n, k)



def Stirling_circle_tail(n, x):
    '''Stirling[x, x-n] = sum Eulerian<<n,k>> C(x+k, 2n) {k}, for [NN n]'''
    #return summation(Eulerian2nd(n, k)*C(x+k, 2*n), (k, 0, n)).doit()
    return sum(Eulerian2nd(n, k)*C(x+k, 2*n) for k in range(n)).simplify()


def Stirling_subset_tail(n, x):
    '''Stirling{x, x-n} = sum Eulerian<<n,k>> C(x+n-1-k, 2n) {k}, for [NN n]'''
    return sum(Eulerian2nd(n, k)*C(x+n-1-k, 2*n) for k in range(n)).simplify()


def Stirling_polynomial(n, z):
    'Stirling_polynomial(n, z) = Stirling[z, z-n]/fall(z, n+1), for [int n>0]'

    assert n > 0
    r = Stirling_circle_tail(n, z) / ff(z, n+1)
    return gcd_terms(factor(r.simplify()))

def Stirling_subset_polynomial(n, z):
    'Stirling_polynomial(n, z) = Stirling{z, z-n}/fall(z, n+1), for [int n>0]'

    assert n > 0
    r = Stirling_subset_tail(n, z) / ff(z, n+1)
    return gcd_terms(factor(r.simplify()))


print('Stirling_polynomial')
ls = []
for n in range(1, 10):
    ls.append(Stirling_polynomial(n, z))
    print(ls[-1])

print('Stirling_subset_polynomial')
for n in range(1, 10):
    p = Stirling_subset_polynomial(n, z)
    print(p)
    assert (p - ls[n-1].subs(z, n-z) * (-1)**(n+1)).expand() == 0



'''

Stirling_polynomial
1/2
(3*z - 1)/24
z*(z - 1)/48
(15*z**3 - 30*z**2 + 5*z + 2)/5760
z*(z - 1)*(3*z**2 - 7*z - 2)/11520
(63*z**5 - 315*z**4 + 315*z**3 + 91*z**2 - 42*z - 16)/2903040
z*(z - 1)*(9*z**4 - 54*z**3 + 51*z**2 + 58*z + 16)/5806080
(135*z**7 - 1260*z**6 + 3150*z**5 - 840*z**4 - 2345*z**3 - 540*z**2 + 404*z + 144)/1393459200
z*(z - 1)*(15*z**6 - 165*z**5 + 465*z**4 + 17*z**3 - 648*z**2 - 548*z - 144)/2786918400
Stirling_subset_polynomial
1/2
(3*z - 5)/24
(z - 3)*(z - 2)/48
(15*z**3 - 150*z**2 + 485*z - 502)/5760
(z - 5)*(z - 4)*(3*z**2 - 23*z + 38)/11520
(63*z**5 - 1575*z**4 + 15435*z**3 - 73801*z**2 + 171150*z - 152696)/2903040
(z - 7)*(z - 6)*(9*z**4 - 198*z**3 + 1563*z**2 - 5182*z + 6008)/5806080
(135*z**7 - 6300*z**6 + 124110*z**5 - 1334760*z**4 + 8437975*z**3 - 31231500*z**2 + 62333204*z - 51360816)/1393459200
(z - 9)*(z - 8)*(15*z**6 - 645*z**5 + 11265*z**4 - 101807*z**3 + 499176*z**2 - 1249444*z + 1234224)/2786918400

'''







