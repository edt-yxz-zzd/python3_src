
from sympy import N, factor, gcd, solve, nsolve, sqrt, \
     nsimplify, expand, collect, resultant, var


from .Archimedean_solid__L_div_R_using_sympy__classify_ASRP import verify_G
from .Archimedean_solid__L_div_R_using_sympy__solid2zero_poly_GG \
     import solid2zero_poly_GG
from nn_ns.sympy_util.add_terms import *
from nn_ns.sympy_util.constant import one
from fractions import Fraction

var('GG', positive=True)



def calc_g468_g4610(solid):
    #solid = (4, 6, 8)
    f = solid2zero_poly_GG(solid)
    gg, = solve(f)
    g = nsimplify(sqrt(gg))
    #print(g468)
    #_g468 = sqrt(-24*sqrt(2) + 52) / sqrt(97)
    #assert 0 == nsimplify(g468 - _g468)

    assert verify_G(solid, g)
    return g

##ASRP468_4610_to_g = {solid:calc_g468_g4610(solid)
##                     for solid in [(4,6,8), (4,6,10)]}
##print(ASRP468_4610_to_g)

g468 = sqrt(-24*sqrt(2) + 52)/sqrt(97)
g4610 = sqrt(-48*sqrt(5) + 124)/sqrt(241)
ASRP468_4610_to_g = {(4, 6, 8): g468, (4, 6, 10): g4610}


if __name__ == '__main__':
    assert 0 == nsimplify(g468 - calc_g468_g4610((4, 6, 8)))
    assert 0 == nsimplify(g4610 - calc_g468_g4610((4, 6, 10)))
    
    print('ASRP468_4610_to_g = {}'
          .format(ASRP468_4610_to_g))



