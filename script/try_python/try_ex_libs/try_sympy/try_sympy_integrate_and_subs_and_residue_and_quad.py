
import sympy as s
from sympy.abc import x, y
from sympy import I, Poly, log, evalf, residue
import math, cmath


'''
find number of complex roots of polynomial
integrate f'/f over sqare ABCD
= logf|(A->B, B->C, C->D, D->A)
= N*2pi

replace
.subs
.evalf
>>> N(sqrt(2)*pi)
4.44288293815837
>>> (sqrt(2)*pi).evalf()
4.44288293815837

count_roots
>>> Poly(x**4 - 4, x).count_roots(0, 1 + 3*I)
1

eval
>>> Poly(x**2 + 2*x + 3, x).eval(2)
11

is_irreducible
>>> Poly(x**2 + x + 1, x, modulus=2).is_irreducible
True

is_primitive
Returns True if GCD of the coefficients of f is one.


refine_root
real_roots
sympy.polys.polytools.intervals(F, all=False, eps=None, inf=None, sup=None,
strict=False, fast=False, sqf=False)
Compute isolating intervals for roots of f
>>> intervals(x**2 - 3)
[((-2, -1), 1), ((1, 2), 1)]


Complex integrals are supported. The following computes a residue at z = 0 by integrat-ing counterclockwise along the diamond-shaped path from 1 to +i to  1 to  i to 1:
>>> from mpmath import *
>>> mp.dps = 15
>>> chop(quad(lambda z: 1/z, [1,j,-1,-j,1]))
(0.0 + 6.28318530717959j)


sympy.series.residues.residue(expr, x, x0)
Finds the residue of expr at the point x=x0.
The residue is defined as the coefficient of 1/(x-x0) in the power series expansion about
x=x0.
References
1.http://en.wikipedia.org/wiki/Residue_theorem
Examples
>>> from sympy import Symbol, residue, sin
>>> x = Symbol(”x”)
>>> residue(1/x, x, 0)
1
>>> residue(1/x**2, x, 0)
0
>>> residue(2/sin(x), x, 0)
2
This function is essential for the Residue Theorem [1].
'''

f = x*(x*x+1)
p = Poly(f, x)
A = -2+2*I
B = 2+2*I
C = 2-2*I
D = -2-2*I
ABCD = [A,B,C,D]
path = list(zip([D]+ABCD, ABCD))

print([p.eval(x, z) for z in ABCD])
logf = log(f)
print([logf.subs(x,z).evalf() for z in ABCD])
ip = [((b-a)/f.subs(x, b)).evalf() for a,b in path]
print(ip, sum(ip))
ress = [residue(1/f, x, z0) for z0 in [0, I, -I]]
print(sum(ress), ress)
'''A->B : sum(f*dz) = sum(f*dx) = F|(-2->2)


'''

def residue(f, circle, N):
    '''residue(f, A->B->.., N) == integrate(f, A->..->A, N)/2pi/1j
'''
    
    path = circle + circle[:1]

    res = (integrate(f, path, N).imag/(2*math.pi))
    return res

def poly_num_roots(f, Df, circle, N):
    '''poly_num_roots(f, f', A->B->.., N) == residue(f'/f, A->B->.., N)

bug: if circle not convex or outside roots too near


we can cut the z-plane into strikes by R+y*i for some real R.
note that each root contribute to +/-pi over such line.
sadly, log is not continue over all plane, we have to do numerial integrate.
how to trace the change of angle????????????????
'''

    Df_f = lambda z: Df(z)/f(z)

    circle = list(circle)
    i = 1
    while i < len(circle):
        if circle[i-1] != circle[i]: break
        i += 1

    circle = circle[i-1:]

    
    res = round(residue(Df_f, circle, N))
    path = circle + circle[:1]

    # watch the change of angle of f(z), that is imag of log(f(z))
    ss = []
    for a, b in zip(path, path[1:]):
        L = b-a
        dL = L/N
        s = (f(a + L*t/N) for t in range(1, N+1))
        angles = (cmath.log(v).imag for v in s)
        ss.extend(angles) # angle counts
    ss.append(ss[0])
    if ss[0] == 0 or ss[0] == 2*math.pi:
        if len(circle) > 2 or len(circle) == 2 and N > 1:
            ss.append(ss[1])
            #print('ss.append')
    #print('angles[0]=={}'.format(ss[0]))
    print('angles[:10]=={}'.format(ss[:10]))
    #print('angles[-10:]=={}'.format(ss[-10:]))
    num_roots1 = sum(a>b for a,b in zip(ss, ss[1:]))
    num_roots2 = len(ss) - num_roots1
    num_roots = min(num_roots1, num_roots2)
    #num_roots = num_roots1
    if num_roots != res:
        print('num_roots != res', num_roots, res)
    assert abs(num_roots - res) < 2
        
    
    return num_roots


def integrate(f, path, N):
    '''integrate(f, A->B, N) == sum(f(z(t))*z'(t)*dt for t in range(N))
z(t) = A + (B-A)*(t+1)/N, z'(t) = (B-A)/N, dt = 1
'''
    path = list(path)
    #path = list(zip(path[-1:]+path, path))

    ss = []
    for a, b in zip(path, path[1:]):
        L = b-a
        dL = L/N
        s = sum(f(a + L*t/N)*dL for t in range(1, N+1))
        ss.append(s)
    return sum(ss)

def test(Ns = [1, 2,10,100]):
    print('integrate f(x)=1/x countclockwise around 0, N increase, ans->2pi*j')
    for N in Ns:
        s = integrate(lambda z: 1/z, [1,1j,-1,-1j, 1], N)
        print('N={}, ans={}'.format(N, s))
        
    print('residue f(x)=g\'(x)/g(x) countclockwise around 0, g(x)=x*(xx+1)')
    for N in Ns:
        s = residue(lambda z: (3*z*z+1)/(z**3+z), [2,2j,-2,-2j], N)
        
        print('N={}, ans={}'.format(N, s))
        
    print('poly_num_roots g(x)=x*(xx+1) countclockwise around 0')
    for N in Ns:
        s = poly_num_roots(lambda z: (z**3+z), lambda z: (3*z*z+1), [2,2j,-2,-2j], N)
        
        print('N={}, ans={}'.format(N, s))

test()

        
            



