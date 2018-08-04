
from sympy import factor, symbols

x = symbols('x')
a = symbols('a1:10')

es = [14, 12, 10, 4, 2, 0]
cs = [1,   1,  1, -1,-1,-1]
f = sum(c*x**e for c,e in zip(cs,es))
r = factor(f)
print('{f}={r}'.format(f=f, r=r))







