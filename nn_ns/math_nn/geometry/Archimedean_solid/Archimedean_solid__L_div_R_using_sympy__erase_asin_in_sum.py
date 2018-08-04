

'''
SUM = sum N[i]/2**(-P[i]) * asin Q[i] {i} for [ZZ N[i],P[i]]

see Archimedean_solid__L_div_R.py::spherical triangle::n-spherical_polygon:
    ::[calc arcsin+arcsin]:
    find y: arcsin(x)/2 = arcsin(y)
        yy = (1-sqrt(1-xx))/2
    find y: arcsin(u) + arcsin(v) = arcsin(y)
        y = u sqrt(1-vv) + sqrt(1-uu) v
'''


from sympy import pi, sin, asin, sqrt, sympify, nsimplify, \
     symbols, var, Wild, fraction

from nn_ns.sympy_util.my_sympify import my_sympify
from nn_ns.sympy_util.constant import zero, one
from nn_ns.sympy_util.geometry import add_arcsin_with_coeffs

def fraction2N_negP(x):
    '''N*2**P -> (N,-P) where P<=0'''
    N, D = fraction(x)
    negP = int(D).bit_length() - one
    if not D == 2**negP:
        raise ValueError('x != N*2**P where P<=0')
    assert x == N/2**negP
    return N, negP

def sum_asin2one_asin(Cs, Ks, w):
    '''sum C[i] asin (K[i]*w) {i} = asin ALL'''

    assert len(Cs) == len(Ks)
    NnPs = list(map(fraction2N_negP, Cs))
    
    ALL = zero # 1*asin ALL == 0
    C_ALL = (1,0) # 1/2**0 == 1
    for NnP, K in zip(NnPs, Ks):
        ALL = add_arcsin_with_coeffs(C_ALL, NnP, ALL, K*w)
    return ALL

    
    
def two_asin2no_asin(sorted_Cs):
    '''pi/2 == sum C[i] asin (K[i]*w) {i=0..1} = asin ALL
==>> ALL - 1 == 0
return ALL-1

where w = 1/sqrt(-g**2 + 4)'''
    
    assert len(sorted_Cs) == 2

    KsW = symbols('K0 K1 W', positive=True)
    K = KsW[:-1]
    W = KsW[-1]

    ALL = sum_asin2one_asin(sorted_Cs, K, W)
    zero_expr = ALL - 1

    return my_sympify(zero_expr)
    '''
# solid2sorted_C_Ks:
    ## (3, 3, 3, 3, 4): ((1/2, sqrt(2)), (2, 1)),
    Cs = (1/2, 2)
    pi/2 == 1/2 * asin(K0*W) + 2*asin(K1*W)
    y = add_arcsin_with_coeffs((1,1), (2,0), K0*W, K1*W) == 1
'''


def sum_asin2zero_radical_expr(sorted_Cs):
    '''pi/2 == sum C[i] asin (K[i]*w) {i=0..n-1} = asin ALL
==>> ALL - 1 == 0
return ALL-1

where w = 1/sqrt(-g**2 + 4)'''
    
    n = len(sorted_Cs)
    assert n > 0

    Ks = symbols(' '.join('K'+str(i) for i in range(n)), positive=True)
    W = symbols('W', positive=True)

    ALL = sum_asin2one_asin(sorted_Cs, Ks, W)
    zero_expr = ALL - 1

    return my_sympify(zero_expr)





