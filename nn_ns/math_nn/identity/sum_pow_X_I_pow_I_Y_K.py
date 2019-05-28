
r'''
sum_pow_X_I_pow_I_Y_K
Sum[x^i (i+y)^k, {i, m, n-1}]

see:
    "NOTE/wolframalpha.com/sum2_3.txt"

[x,y<-CC][k,m,n<-ZZ][k>=0][[x!=0] or [x==1] or [m==n] or [m,n>=0]]:
    sum2_3(x,y,k,m,n)
        = sum x^i*(i+y)^k {i=m->n}
        = [m<n]sum x^i*(i+y)^k {i=m..n-1} - [m>n]sum x^i*(i+y)^k {i=n..m-1}
        = C3(x,y,k,n) - C3(x,y,k,m)

        = [x==1]1/(k+1) * sum C(k+1,j)*B[j]* (n+y)^(k+1-j) {j=0..k}
        + [x!=1](x^n (-1)^0 C(k,0) (n+y)^(k-0) (x - 1)^(k-0) S(x,0)
                + x^(n+1) sum (-1)^j C(k,j) (n+y)^(k-j) (x - 1)^(k-j) S(x,j) {j=1..k}
                )/(x - 1)^(k + 1)
        - C3(x,y,k,m)
        # C/B/S = ... # see below
        S(x,j) = (sum x^e * Eulerian_1st(j,e) {e=0..j})
        Eulerian_1st(n,k)
            = Eulerian<n,k> = Eulerian<n-1,k-1>*(n-k) + Eulerian<n-1,k>*(k+1)
            Eulerian<0,k> = [k==0]
        # B = Bernoulli numbers
        B[d] = [d=0] - 1/(d+1) * sum C(d+1,k) B[k] {k=0..d-1}
        C(n,k) = binomial(n,k) = n!/(k!*(n-k)!)
=======================================


'''

__all__ = '''
    sum_pow_X_I_pow_I_Y_K
    sum_pow_X_I_pow_I_Y_K__def
    '''.split()

from nn_ns.math_nn.numbers.Bernoulli_number import bernoulli
from nn_ns.math_nn.numbers.choose import choose
from nn_ns.math_nn.numbers.Eulerian_number import eulerian_1st
from fractions import Fraction
import itertools

B = bernoulli
C = choose
E = eulerian_1st
one = Fraction(1)
zero = Fraction(0)

def sum_pow_X_I_pow_I_Y_K__def(x,y,k,m,n):
    '''
[x,y<-CC][k,m,n<-ZZ][k>=0][[x!=0] or [m==n] or [m,n>=0]]:
    sum_pow_X_I_pow_I_Y_K(x,y,k,m,n)
        = [m<n]Sum[x^i (i+y)^k, {i, m, n-1}]
        - [m>n]Sum[x^i (i+y)^k, {i, n, m-1}]
'''
    assert x != 0 or m==n or (m>=0 and n>=0)
    assert k >= 0
    x *= one
    y *= one

    if m < n:
        return __half_sum(x,y,k,m,n)
    elif m > n:
        return -__half_sum(x,y,k,n,m)
    else:
        return 0
def __half_sum(x,y,k,m,n):
    'Sum[x^i (i+y)^k, {i, m, n-1}]'
    assert x != 0 or m==n or (m>=0 and n>=0)
    assert k >= 0
    assert m < n
    return sum(x**i * (i+y)**k for i in range(m,n))


def __half__indefinite_integral(x,y,k,n):
    '''
[x,y<-CC][k,n<-ZZ][k>=0][[x!=0] or [n>=0]]:
    C3(x,y,k,n)
        = [x==1]1/(k+1) * sum C(k+1,j)*B[j]* (n+y)^(k+1-j) {j=0..k}
        + [x!=1](x^n (-1)^0 C(k,0) (n+y)^(k-0) (x - 1)^(k-0) S(x,0)
                + x^(n+1) sum (-1)^j C(k,j) (n+y)^(k-j) (x - 1)^(k-j) S(x,j) {j=1..k}
                )/(x - 1)^(k + 1)
'''
    assert x != 0 or n>=0
    assert k >= 0
    if x == 1:
        return __half__indefinite_integral__x_eq_1(y,k,n)
    else:
        return __half__indefinite_integral__x_ne_1(x,y,k,n)
def __half__indefinite_integral__x_ne_1(x,y,k,n):
    '''
[x,y<-CC][k,n<-ZZ][k>=0][[x!=0] or [n>=0]][x!=1]:
    C3(x,y,k,n)
        = (x^n (-1)^0 C(k,0) (n+y)^(k-0) (x - 1)^(k-0) S(x,0)
          + x^(n+1) sum (-1)^j C(k,j) (n+y)^(k-j) (x - 1)^(k-j) S(x,j) {j=1..k}
          )/(x - 1)^(k + 1)
'''
    assert x != 0 or n>=0
    assert k >= 0
    assert x != 1
    s1 = x**n * (n+y)**k * (x - 1)**k
    s2 = x**(n+1) * sum(
            (-1)**j * C(k,j) * (n+y)**(k-j) * (x - 1)**(k-j) * __S(x,j)
            for j in range(1, k+1)
            )
    return (s1 + s2)*one/(x - 1)**(k + 1)

def __S(x,j):
    '''
S(x,j) = (sum x^e * Eulerian_1st(j,e) {e=0..j})
'''
    return sum(x**e * eulerian_1st(j,e) for e in range(0,j+1))

def __half__indefinite_integral__x_eq_1(y,k,n):
    '''
[x,y<-CC][k,n<-ZZ][k>=0][x==1]:
    C3(x,y,k,n)
        = 1/(k+1) * sum C(k+1,j)*B[j]* (n+y)^(k+1-j) {j=0..k}
'''
    assert k >= 0
    s = sum(C(k+1,j)*B(j)*(n+y)**(k+1-j) for j in range(0,k+1))
    return s*one/(k+1)

def sum_pow_X_I_pow_I_Y_K(x,y,k,m,n):
    '''
[x,y<-CC][k,m,n<-ZZ][k>=0][[x!=0] or [m==n] or [m,n>=0]]:
    sum_pow_X_I_pow_I_Y_K(x,y,k,m,n)
        = [m<n]Sum[x^i (i+y)^k, {i, m, n-1}]
        - [m>n]Sum[x^i (i+y)^k, {i, n, m-1}]
        = C3(x,y,k,n) - C3(x,y,k,m)
'''
    assert x != 0 or m==n or (m>=0 and n>=0)
    assert k >= 0
    x *= one
    y *= one

    if m == n:
        return 0
    else:
        return (__half__indefinite_integral(x,y,k,n)
                -__half__indefinite_integral(x,y,k,m)
                )

def _test():
    #[x,y<-CC][k,m,n<-ZZ][k>=0][[x!=0] or [m==n] or [m,n>=0]]:
    for k in range(0, 6):
     for x in [-1, 0, 1, 2, one/2, -one/3]:
      for y in [-1, 0, 1, 2, 3*one/4, -5*one/3]:
       for m in range(-6, 6):
        for n in range(-6, 6):
            if not (x!=0 or m==n or (m>=0 and n>=0)): continue
            print(f'(x,y,k,m,n)=({x},{y},{k},{m},{n})')
            s = sum_pow_X_I_pow_I_Y_K(x,y,k,m,n)
            s_def = sum_pow_X_I_pow_I_Y_K__def(x,y,k,m,n)
            try:
                assert s == s_def
            except:
                print(f's={s}')
                print(f's_def={s_def}')
                raise


if __name__ == '__main__':
    _test()


