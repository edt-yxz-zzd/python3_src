
import sympy as s
from sympy.abc import x, y
from sympy import I, Poly, log, evalf


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
ip = [((b-a)*f.subs(x, b)).evalf() for a,b in path]
print(ip, sum(ip))

'''A->B : sum(f*dz) = sum(f*dx) = F|(-2->2)


'''
find k, x**k <= ln(1+x) for x in (0, 1/3)
==>> 1/3**k <= ln(1+1/3)
k >= -log(3,(ln(1+1/3)))
'''

import math


assert math.log(1+1/3) < 1/3
mink = -math.log(math.log(1+1/3), 3)
# mink = 1.1340664368661764

print(mink)


