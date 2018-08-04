
import sympy as s

from sympy.abc import x, y


f = (x+1)**2 * (x+3)*(x+4)
f = s.expand(f)
# I expect: [(x**2+7x + 12), 1] ,  [(x+1), 2]
# but it factors (x+3) ,  (x+4)
print(s.sqf_list(f))
