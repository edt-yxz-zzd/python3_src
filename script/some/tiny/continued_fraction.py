

'''
circle period
pure x = [bn; b[n-1]...b[0], x] > 1
x = (A[n+1]x + B[n+1]) / (C[n+1]x + D[n+1])
M[i] = [A[i], B[i]; C[i], D[i]] = [A[i], B[i]; A[i-1], B[i-1]]
M[i+1] = [b[i], 1; 1, 0] * M[i]
M[0] = eye(2)
let T[i] = [b[i], 1; 1, 0]
? product(T[i] for i in range(n+1))
'''


'''
sympy.physics.quantum.shor.continued_fraction(x, y)
This applies the continued fraction expansion to two numbers x/y
x is the numerator and y is the denominator
'''

from sympy import Product, symbols, Matrix, eye, ones, zeros, simplify
from sympy.abc import x, y, z
bs = symbols('b0 b1 b2 b3 b4')
##print(bs[0])
##i2b = lambda i: bs[i]
##Product(i2b, (x, 1, 2))

#Product(ones(2,2)[x], (x, 1, 2))

mc = [ones(2, 2) for _ in bs]
for mx, b in zip(mc, bs):
    mx[1,1] = 0
    mx[0,0] = b

r = eye(2)
for mx in mc:
    r = mx*r

for i in range(2):
    for j in range(2):
        r[i,j] = simplify(r[i,j])
print(r)









