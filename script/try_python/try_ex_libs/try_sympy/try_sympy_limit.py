
import sympy as s

from sympy.abc import x, y

help(s.limit)
e = (1-x)**(1/x)
s.limit(e,x, 0)
