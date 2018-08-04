

'''
g = L/R
W = 1/sqrt(4-g*g); WW = 1/(1-gg)

0 == zero_expr of ASPR = sum Bi asin(Ki/sqrt(4-g*g)) {i} + B*pi

==>> pi/2 = sum Bi/(-2B) asin(Ki * W) {i}
    = sum C[i] asin(K[i]*W) {i}
so, we idenitify ASRPs by {[(C[i], K[i]) for i]}
and classify ASRPs by {[C[i] for i]}

'''
from .Archimedean_solid__L_div_R_using_sympy__calc_L_div_R \
     import solid2zero_expr
#from .Archimedean_solid__which import Archimedean_solid2info
from .Archimedean_solid__which_using_sympy \
     import solid2info_using_sympy as Archimedean_solid2info, v
from sympy import pi, sin, asin, sqrt, sympify, solve, nsolve, nsimplify, \
     symbols, var, Wild, factor, expand, trigsimp, cos
from nn_ns.sympy_util.my_sympify import my_sympify
from nn_ns.sympy_util.constant import one
from nn_ns.sympy_util.add_terms import get_coeff_of
from pprint import pprint
import copy

__all__ = ('verify_G, solid2zeroexpr'
           ', solid2K2C, solid2sorted_C_Ks, sorted_Cs2solids'
           .split(', '))

def verify_G(solid, g):
    zeroexpr = solid2zeroexpr[solid]
    G, = zeroexpr.free_symbols - {v}
    z = zeroexpr.subs(G, g)
    z = trigsimp(z)
    z = my_sympify(z)
    z = nsimplify(z)
    return 0 == z

def asin_pi2coeffs(f, x):
    '''f = sum Ci asin(Ki/sqrt(4-x*x)) {i} + C*pi
f/-2/C + pi/2 = sum Ci/-2/C asin(Ki/(4-x*x)) {i}
return {Ki:Ci/-2/C for i}

'''
    w = symbols('__W', positive=True)
    f = f.subs((4-x*x), 1/w/w) # W=1/X=1/sqrt(4-gg); WW=1/(4-gg)
    f = expand(sympify(f))
    f0 = f

    C_pi = get_coeff_of(f, pi)
    
    f /= -2*C_pi
    f += pi/2
    f = expand(f)
    #print(f)
    A, B_ls = f.as_coeff_add()
    assert A == 0
    K = Wild('K')
    C = Wild('C')
    p = C*asin(K*w)
    ls = []
    for b in B_ls:
        m = p.matches(b)
        assert len(m) == 2
        ls.append((m[K], m[C]))
    _f = sum(c*asin(k*w) for k,c in ls)
    assert f == _f
    d = dict((nsimplify(k),c) for k,c in ls)
    assert len(d) == len(ls)
    return d
    


def __tmp():
    var('g', positive=True)
    solid2zeroexpr = {}
    solid2K2C = {}
    for solid in [] or Archimedean_solid2info:
        f = solid2zero_expr(solid, g)
        #print(solid, f)
        K2C = asin_pi2coeffs(f, g)
        #print('\t', K2C)
        solid2zeroexpr[solid] = f
        solid2K2C[solid] = K2C

    #pprint(solid2K2C)

    solid2sorted_C_Ks = {}
    for solid, K2C in solid2K2C.items():
        sorted_C_Ks = tuple(sorted((C,K) for K,C in K2C.items()))
        solid2sorted_C_Ks[solid] = sorted_C_Ks

    sorted_Cs2solids = {}
    for solid, sorted_C_Ks in solid2sorted_C_Ks.items():
        sorted_Cs = tuple(C for C,K in sorted_C_Ks)
        if sorted_Cs not in sorted_Cs2solids:
            sorted_Cs2solids[sorted_Cs] = []
        solids = sorted_Cs2solids[sorted_Cs]
        solids.append(solid)

    for ls in sorted_Cs2solids.values():
        ls.sort()
    return solid2zeroexpr, solid2K2C, solid2sorted_C_Ks, sorted_Cs2solids

solid2zeroexpr, solid2K2C, solid2sorted_C_Ks, sorted_Cs2solids = __tmp()

#pprint(sorted_Cs2solids)
#pprint(sorted(sorted_Cs2solids))
half = one/2
[(half, half, half),
 (half, half, 1),
 (half, 1),
 (half, 3*half),
 (half, 2),
 (1, 1),
 (3*half,),
 (2,),
 (5*half,)]

#pprint(sorted_Cs2solids)
assert sorted_Cs2solids == \
    {(half, half, half): [(4, 6, 8), (4, 6, 10)],
     (half, half, 1): [(3, 4, 5, 4)],
     (half, 1): [(3, 6, 6),
                (3, 8, 8),
                (3, 10, 10),
                (4, 4, v),
                (4, 6, 6),
                (5, 6, 6)],
     (half, 3*half): [(3, 3, 3, v), (3, 4, 4, 4)],
     (half, 2): [(3, 3, 3, 3, 4), (3, 3, 3, 3, 5)],
     (1, 1): [(3, 4, 3, 4), (3, 5, 3, 5)],
     (3*half,): [(3, 3, 3), (4, 4, 4), (5, 5, 5)],
     (2,): [(3, 3, 3, 3)],
     (5*half,): [(3, 3, 3, 3, 3)]}



#pprint(solid2zeroexpr)

# fixed:
def __fixed():
    sorted_Cs2solids__fixed = copy.deepcopy(sorted_Cs2solids)
    sorted_Cs2solids__fixed[(one/2, one/2, 1)] += \
                sorted_Cs2solids__fixed[(one/2, 3*half)]
    del sorted_Cs2solids__fixed[(one/2, 3*half)]

    solid2sorted_C_Ks__fixed = copy.deepcopy(solid2sorted_C_Ks)
    (_, k0), (_, k1) = solid2sorted_C_Ks[(3, 4, 4, 4)]
    solid2sorted_C_Ks__fixed[(3, 4, 4, 4)] = (half, k0), (half, k1), (1, k1)
    return sorted_Cs2solids__fixed, solid2sorted_C_Ks__fixed
sorted_Cs2solids__fixed, solid2sorted_C_Ks__fixed = __fixed()

def main():
    
    print('sorted_Cs2solids = \\')
    pprint(sorted_Cs2solids)
    print('solid2sorted_C_Ks = \\')
    pprint(solid2sorted_C_Ks)
    print('solid2zeroexpr = \\')
    pprint(solid2zeroexpr)


if __name__ == '__main__':
    main()


assert solid2sorted_C_Ks == \
{(3, 3, 3): ((3*half, 1),),
 (3, 3, 3, 3): ((2, 1),),
 (3, 3, 3, 3, 3): ((5*half, 1),),
 (3, 3, 3, 3, 4): ((half, sqrt(2)), (2, 1)),
 (3, 3, 3, 3, 5): ((half, half + sqrt(5)/2), (2, 1)),
 (3, 3, 3, v): ((half, 2*cos(pi/v)), (3*half, 1)),
 (3, 4, 3, 4): ((1, 1), (1, sqrt(2))),
 (3, 4, 4, 4): ((half, 1), (3*half, sqrt(2))),
 (3, 4, 5, 4): ((half, 1), (half, half + sqrt(5)/2), (1, sqrt(2))),
 (3, 5, 3, 5): ((1, 1), (1, half + sqrt(5)/2)),
 (3, 6, 6): ((half, 1), (1, sqrt(3))),
 (3, 8, 8): ((half, 1), (1, sqrt(sqrt(2) + 2))),
 (3, 10, 10): ((half, 1), (1, sqrt(sqrt(5)/2 + 5*half))),
 (4, 4, 4): ((3*half, sqrt(2)),),
 (4, 4, v): ((half, 2*cos(pi/v)), (1, sqrt(2))),
 (4, 6, 6): ((half, sqrt(2)), (1, sqrt(3))),
 (4, 6, 8): ((half, sqrt(2)), (half, sqrt(3)), (half, sqrt(sqrt(2) + 2))),
 (4, 6, 10): ((half, sqrt(2)), (half, sqrt(3)), (half, sqrt(sqrt(5)/2 + 5*half))),
 (5, 5, 5): ((3*half, half + sqrt(5)/2),),
 (5, 6, 6): ((half, half + sqrt(5)/2), (1, sqrt(3)))}


#assert solid2zeroexpr == \
_solid2zeroexpr = {(3, 3, 3): -24*asin(1/sqrt(-g**2 + 4)) + 8*pi,
 (3, 3, 3, 3): -48*asin(1/sqrt(-g**2 + 4)) + 12*pi,
 (3, 3, 3, 3, 3): -120*asin(1/sqrt(-g**2 + 4)) + 24*pi,
 (3, 3, 3, 3, 4): -48*asin(sqrt(2)/sqrt(-g**2 + 4)) - 192*asin(1/sqrt(-g**2 + 4)) + 48*pi,
 (3, 3, 3, 3, 5): -120*asin(2*sin(3*pi/10)/sqrt(-g**2 + 4)) - 480*asin(1/sqrt(-g**2 + 4)) + 120*pi,
 (3, 3, 3, v): -4*v*asin(2*cos(pi/v)/sqrt(-g**2 + 4)) - 12*v*asin(1/sqrt(-g**2 + 4)) + 4*pi*v,
 (3, 4, 3, 4): -48*asin(sqrt(2)/sqrt(-g**2 + 4)) - 48*asin(1/sqrt(-g**2 + 4)) + 24*pi,
 (3, 4, 4, 4): -144*asin(sqrt(2)/sqrt(-g**2 + 4)) - 48*asin(1/sqrt(-g**2 + 4)) + 48*pi,
 (3, 4, 5, 4): -240*asin(sqrt(2)/sqrt(-g**2 + 4)) - 120*asin(2*sin(3*pi/10)/sqrt(-g**2 + 4)) - 120*asin(1/sqrt(-g**2 + 4)) + 120*pi,
 (3, 5, 3, 5): -120*asin(2*sin(3*pi/10)/sqrt(-g**2 + 4)) - 120*asin(1/sqrt(-g**2 + 4)) + 60*pi,
 (3, 6, 6): -48*asin(sqrt(3)/sqrt(-g**2 + 4)) - 24*asin(1/sqrt(-g**2 + 4)) + 24*pi,
 (3, 8, 8): -96*asin(2*sin(3*pi/8)/sqrt(-g**2 + 4)) - 48*asin(1/sqrt(-g**2 + 4)) + 48*pi,
 (3, 10, 10): -240*asin(2*sqrt(sqrt(5)/8 + 5*one/8)/sqrt(-g**2 + 4)) - 120*asin(1/sqrt(-g**2 + 4)) + 120*pi,
 (4, 4, 4): -48*asin(sqrt(2)/sqrt(-g**2 + 4)) + 16*pi,
 (4, 4, v): -8*v*asin(sqrt(2)/sqrt(-g**2 + 4)) - 4*v*asin(2*cos(pi/v)/sqrt(-g**2 + 4)) + 4*pi*v,
 (4, 6, 6): -48*asin(sqrt(2)/sqrt(-g**2 + 4)) - 96*asin(sqrt(3)/sqrt(-g**2 + 4)) + 48*pi,
 (4, 6, 8): -96*asin(sqrt(2)/sqrt(-g**2 + 4)) - 96*asin(sqrt(3)/sqrt(-g**2 + 4)) - 96*asin(2*sin(3*pi/8)/sqrt(-g**2 + 4)) + 96*pi,
 (4, 6, 10): -240*asin(sqrt(2)/sqrt(-g**2 + 4)) - 240*asin(sqrt(3)/sqrt(-g**2 + 4)) - 240*asin(2*sqrt(sqrt(5)/8 + 5*one/8)/sqrt(-g**2 + 4)) + 240*pi,
 (5, 5, 5): -120*asin(2*sin(3*pi/10)/sqrt(-g**2 + 4)) + 40*pi,
 (5, 6, 6): -240*asin(sqrt(3)/sqrt(-g**2 + 4)) - 120*asin(2*sin(3*pi/10)/sqrt(-g**2 + 4)) + 120*pi}



if not solid2zeroexpr == _solid2zeroexpr:
    _dict2set = lambda d: set(d.items())
    _d1 = _dict2set(solid2zeroexpr)
    _d2 = _dict2set(_solid2zeroexpr)
    pprint(_d1-_d2)
    pprint(_d2-_d1)





