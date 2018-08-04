
from sympy import N, factor, gcd, solve, nsolve, sqrt, \
     nsimplify, expand, collect, resultant, var


from .Archimedean_solid__L_div_R_using_sympy__classify_ASRP import verify_G
from .Archimedean_solid__L_div_R_using_sympy__solid2zero_poly_GG \
     import solid2zero_poly_GG
from nn_ns.sympy_util.add_terms import *
from nn_ns.sympy_util.constant import one
from fractions import Fraction

var('GG', positive=True)



def calc_g3444_g3454(solid):
    f = solid2zero_poly_GG(solid)
    gg, = solve(f)
    g = nsimplify(sqrt(gg))

    assert verify_G(solid, g)
    return g

##ASRP3444_3454_to_g = {solid:calc_g3444_g3454(solid)
##                     for solid in [(3,4,4,4), (3,4,5,4)]}
##print(ASRP3444_3454_to_g)


g3444 = sqrt(-8*sqrt(2) + 20)/sqrt(17)
g3454 = sqrt(-16*sqrt(5) + 44)/sqrt(41)
ASRP3444_3454_to_g = {(3, 4, 4, 4): g3444, (3, 4, 5, 4): g3454}


if __name__ == '__main__':
    assert 0 == nsimplify(g3444 - calc_g3444_g3454((3, 4, 4, 4)))
    assert 0 == nsimplify(g3454 - calc_g3444_g3454((3, 4, 5, 4)))
    
    print('ASRP3444_3454_to_g = {}'
          .format(ASRP3444_3454_to_g))



