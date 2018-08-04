
from sympy import *
var('L R GG', positive=True)
var('v v_2', postive=True, integer=True)
x = (0.5 + 1/(v_2 + 2))*(2*v_2 + 4)
from nn_ns.sympy_util.my_sympify import my_sympify
from Archimedean_solid.Archimedean_solid__L_div_R_using_sympy__classify_ASRP \
     import main

from Archimedean_solid.Archimedean_solid__which_using_sympy import v


g44v = 2*sin(pi/v)/sqrt(sin(pi/v)**2 + 1)
f44v = -8*v*asin(sqrt(2)/sqrt(-GG + 4)) - 4*v*asin(2*cos(pi/v)/sqrt(-GG + 4)) + 4*pi*v

4,4,3
Rc=2
L=2*sqrt(3)
RR = 3+4
g = 2*sqrt(3)/sqrt(7)
f = f44v

z = f.subs(v,3).subs(GG, g*g)
z = nsimplify(z)
assert z == 0
x = g44v.subs(v,3)
assert nsimplify(x-g) == 0



f = my_sympify(f44v.subs(GG, g44v**2))
#print(f)

h = 4*v*(-2*asin(sqrt(2)*sqrt(sin(pi/v)**2 + 1)/2) - asin(sqrt(sin(pi/v)**2 + 1)*cos(pi/v)) + pi)

for i in range(3,10):
    x = h.subs(v, i)
    x = nsimplify(x)
    assert 0 == x


from Archimedean_solid.Archimedean_solid__L_div_R_using_sympy__calc_g333v_g44v \
     import *


z = v*(-4*asin(sqrt(sin(pi/v)**2 + 1)*cos(pi/v)) - 6*asin(sqrt(sin(pi/v)**2 + 1)/2) + 3*pi)

for i in range(3,6):
    x = z.subs(v, i)
    x = nsimplify(x)
    assert 0 == x
from Archimedean_solid.Archimedean_solid__L_div_R_using_sympy__calc_g333v_g44v import *
