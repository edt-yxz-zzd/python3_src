
'''see Archimedean_solid__L_div_R.py::spherical polygon::n-spherical_polygon

z = angle of n-gon = pi - 2*pi/n
sin(alpha/2) = sin(z/2)/2 * 4/sqrt(4-gg)
    = 2*sin(z/2)/sqrt(4-gg) where g=L/R


AA(n,g) = n*alpha - (n-2)*pi
[given ASRP to calc g]:
    0 == 4*pi-sum(AA(n,g)*f for n, f in ASRP.shape2count.items()) ==>> g=??

'''


from sympy import pi, sin, asin, sqrt, sympify, solve, nsolve, nsimplify, \
     symbols, var, expand

import sympy.mpmath
from sympy.mpmath import findroot, mpf
from pprint import pprint
#from .Archimedean_solid__which import Archimedean_solid2info
from .Archimedean_solid__which_using_sympy \
     import solid2info_using_sympy as Archimedean_solid2info

__all__ = tuple('solid2zero_expr, calc_L_div_R'.split(', '))

def calc_L_div_R__z(n):
    return pi - 2*pi/n

def calc_L_div_R__alpah(n, g):
    z = calc_L_div_R__z(n)
    x = 2*sin(z/2)/sqrt(4-g*g)
    alpha = asin(x)*2
    return alpha

def calc_L_div_R__AA(n, g):
    alpha = calc_L_div_R__alpah(n, g)
    return n*alpha - (n-2)*pi

def solid2zero_expr(solid, g):
    #solid = tuple(map(int, solid))
    solid = tuple(solid)
    info = Archimedean_solid2info[solid]
    shape2count = info['shape2count']

    AA = calc_L_div_R__AA
    
    f = 4*pi-sum(AA(n,g)*f for n, f in shape2count.items())
    f = sympify(expand(f))
    return f


def calc_L_div_R(solid, g = symbols('g', positive=True)):
    '''see Archimedean_solid__L_div_R.py::spherical polygon::n-spherical_polygon

z = angle of n-gon = pi - 2*pi/n
sin(alpha/2) = sin(z/2)/2 * 4/sqrt(4-gg)
    = 2*sin(z/2)/sqrt(4-gg) where g=L/R


AA(n,g) = n*alpha - (n-2)*pi
[given ASRP to calc g]:
    0 == 4*pi-sum(AA(n,g)*f for n, f in ASRP.shape2count.items()) ==>> g=??

'''
    f = solid2zero_expr(solid, g)
    eq = '0 == {}'.format(f)
    
    try:
        ans = solve(f)
    except NotImplementedError:
        #print('using nsolve')
        ans = nsolve(f, g, 1)
        #print('after nsolve')
##        ff = lambda x: f.evalf(subs={g:x})
##        ff = lambda x: f.subs(g,x).evalf()
##        print(ff(1))
##        ans = findroot(ff, 1)

        assert ans.imag < 1e-20
        ans = ans.real
        
##        print(sympy.mpmath.mp.dps)
##        print(ans)
##        sympy.mpmath.mp.dps = 1
##        print(ans) # yield it changes!
        
    else:
        ans = list(x for x in ans if x>0)
        assert len(ans) == 1
        ans, = ans
        ans = nsimplify(ans)
        ans = sympify(ans)
##    ans = powsimp(ans)
##    ans = trigsimp(ans)
##    ans = expand(ans)
    
    return ans, eq
    
def calc_g():
    indent = 4
    for solid in [] or Archimedean_solid2info:
        print(solid)
        try:
            ans, eq = x = calc_L_div_R(solid)
            print('\t', ans)
            print('\t', eq)
            #print('\t', x)
            #print(' '*indent, end='')
            #pprint(x, indent=indent)
        except Exception as e:
            print('\t', type(e))
            
    '''
calc_g()

(3, 3, 3)
	 2*sqrt(6)/3
	 0 == -24*asin(1/sqrt(-g**2 + 4)) + 8*pi
(4, 6, 6)
	 0.632455532033675
	 0 == -48*asin(sqrt(2)/sqrt(-g**2 + 4)) - 96*asin(sqrt(3)/sqrt(-g**2 + 4)) + 48*pi
(3, 3, 3, 3, 3)
	 sqrt(-2*sqrt(5)/5 + 2)
	 0 == -120*asin(1/sqrt(-g**2 + 4)) + 24*pi
(3, 4, 3, 4)
	 0.999999999999999
	 0 == -48*asin(sqrt(2)/sqrt(-g**2 + 4)) - 48*asin(1/sqrt(-g**2 + 4)) + 24*pi
(3, 3, 3, 3, 5)
	 0.463856880645439
	 0 == -120*asin(2*sin(3*pi/10)/sqrt(-g**2 + 4)) - 480*asin(1/sqrt(-g**2 + 4)) + 120*pi
(3, 4, 4, 4)
	 0.714813488673185
	 0 == -144*asin(sqrt(2)/sqrt(-g**2 + 4)) - 48*asin(1/sqrt(-g**2 + 4)) + 48*pi
(3, 10, 10)
	 0.336762811773427
	 0 == -240*asin(2*sqrt(sqrt(5)/8 + 5/8)/sqrt(-g**2 + 4)) - 120*asin(1/sqrt(-g**2 + 4)) + 120*pi
(3, 6, 6)
	 0.852802865422441
	 0 == -48*asin(sqrt(3)/sqrt(-g**2 + 4)) - 24*asin(1/sqrt(-g**2 + 4)) + 24*pi
(5, 5, 5)
	 sqrt(-2*sqrt(5)/3 + 2)
	 0 == -120*asin(2*sin(3*pi/10)/sqrt(-g**2 + 4)) + 40*pi
(4, 4, 4)
	 2*sqrt(3)/3
	 0 == -48*asin(sqrt(2)/sqrt(-g**2 + 4)) + 16*pi
(4, 6, 8)
	 0.431478810544531
	 0 == -96*asin(sqrt(2)/sqrt(-g**2 + 4)) - 96*asin(sqrt(3)/sqrt(-g**2 + 4)) - 96*asin(2*sin(3*pi/8)/sqrt(-g**2 + 4)) + 96*pi
(3, 8, 8)
	 0.562169275429639
	 0 == -96*asin(2*sin(3*pi/8)/sqrt(-g**2 + 4)) - 48*asin(1/sqrt(-g**2 + 4)) + 48*pi
(3, 4, 5, 4)
	 0.447837959589023
	 0 == -240*asin(sqrt(2)/sqrt(-g**2 + 4)) - 120*asin(2*sin(3*pi/10)/sqrt(-g**2 + 4)) - 120*asin(1/sqrt(-g**2 + 4)) + 120*pi
(3, 3, 3, 3, 4)
	 0.744206331156206
	 0 == -48*asin(sqrt(2)/sqrt(-g**2 + 4)) - 192*asin(1/sqrt(-g**2 + 4)) + 48*pi
(3, 5, 3, 5)
	 0.618033988749904
	 0 == -120*asin(2*sin(3*pi/10)/sqrt(-g**2 + 4)) - 120*asin(1/sqrt(-g**2 + 4)) + 60*pi
(5, 6, 6)
	 0.403548212335194
	 0 == -240*asin(sqrt(3)/sqrt(-g**2 + 4)) - 120*asin(2*sin(3*pi/10)/sqrt(-g**2 + 4)) + 120*pi
(3, 3, 3, 3)
	 sqrt(2)
	 0 == -48*asin(1/sqrt(-g**2 + 4)) + 12*pi
(4, 6, 10)
	 0.2629921750726
	 0 == -240*asin(sqrt(2)/sqrt(-g**2 + 4)) - 240*asin(sqrt(3)/sqrt(-g**2 + 4)) - 240*asin(2*sqrt(sqrt(5)/8 + 5/8)/sqrt(-g**2 + 4)) + 240*pi

'''

if __name__ == '__main__':
    calc_g()






    
