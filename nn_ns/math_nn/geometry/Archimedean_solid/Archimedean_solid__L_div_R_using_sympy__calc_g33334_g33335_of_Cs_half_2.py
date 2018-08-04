

from sympy import N, factor, gcd, solve, nsolve, sqrt, \
     nsimplify, expand, collect, resultant, var


from .Archimedean_solid__L_div_R_using_sympy__classify_ASRP import verify_G
from .Archimedean_solid__L_div_R_using_sympy__solid2zero_poly_GG \
     import solid2zero_poly_GG
from nn_ns.sympy_util.add_terms import *
from nn_ns.sympy_util.constant import one
from fractions import Fraction

var('GG', positive=True)

def calc_g33334():
    # solid2sorted_C_Ks:
    ## (3, 3, 3, 3, 4): ((1/2, sqrt(2)), (2, 1)),
    solid = (3, 3, 3, 3, 4)
    f = solid2zero_poly_GG(solid)
    f = factor(f)
    gg, = solve(f)
    g33334 = sqrt(gg)
    g33334 = nsimplify(g33334)
    _g33334 = sqrt(-2*(42*sqrt(33) + 566)**(one/3)
                   - 128/(42*sqrt(33) + 566)**(one/3) + 44) / sqrt(21)
    assert 0 == nsimplify(g33334 - _g33334)

    assert verify_G(solid, g33334)
    return g33334


def calc_g33335():
    # solid2sorted_C_Ks:
    ## (3, 3, 3, 3, 5): ((1/2, 1/2 + sqrt(5)/2), (2, 1)),
    # 0.463856880645439
    solid = (3, 3, 3, 3, 5)
    f = solid2zero_poly_GG(solid)
    ggs = solve(f)
##    print(ggs)
##    print(list(map(N, ggs)))
    gg, = ggs
    g33335 = nsimplify(sqrt(gg))
    _g33335 = sqrt(-(-(-188 + 12*sqrt(5))**3/(27*(-29 + sqrt(5))**3)
                     - (-192 + 64*sqrt(5))/(2*(-29 + sqrt(5)))
                     + sqrt((-(-188 + 12*sqrt(5))**2/(9*(-29 + sqrt(5))**2)
                             + (-368 + 48*sqrt(5))/(3*(-29 + sqrt(5))))**3
                            + (-2*(-188 + 12*sqrt(5))**3/(27*(-29 + sqrt(5))**3)
                               - (-192 + 64*sqrt(5))/(-29 + sqrt(5))
                               + (-368 + 48*sqrt(5))*(-188 + 12*sqrt(5))
                               /(3*(-29 + sqrt(5))**2))**2/4)
                     + (-368 + 48*sqrt(5))*(-188 + 12*sqrt(5))
                     /(6*(-29 + sqrt(5))**2))**(1/3)
                   + (-(-188 + 12*sqrt(5))**2/(9*(-29 + sqrt(5))**2)
                      + (-368 + 48*sqrt(5))/(3*(-29 + sqrt(5))))
                   /(-(-188 + 12*sqrt(5))**3/(27*(-29 + sqrt(5))**3)
                     - (-192 + 64*sqrt(5))/(2*(-29 + sqrt(5)))
                     + sqrt((-(-188 + 12*sqrt(5))**2/(9*(-29 + sqrt(5))**2)
                             + (-368 + 48*sqrt(5))/(3*(-29 + sqrt(5))))**3
                            + (-2*(-188 + 12*sqrt(5))**3/(27*(-29 + sqrt(5))**3)
                               - (-192 + 64*sqrt(5))/(-29 + sqrt(5))
                               + (-368 + 48*sqrt(5))*(-188 + 12*sqrt(5))
                               /(3*(-29 + sqrt(5))**2))**2/4)
                     + (-368 + 48*sqrt(5))*(-188 + 12*sqrt(5))
                     /(6*(-29 + sqrt(5))**2))**(1/3)
                   + (-188 + 12*sqrt(5))/(3*(-29 + sqrt(5))))
    assert verify_G(solid, g33335)


    # new form of g33335
    h = expand(f*(sqrt(5) + 29)/2)
    h = collect(h, GG)
    assert h == 209*GG**3 + GG**2*(-1348 + 40*sqrt(5)) + GG*(-256*sqrt(5) + 2608) - 1312 + 416*sqrt(5)

    fr_one = Fraction(1) # Fraction(1)
    sr_one = GG/GG # Rational(1) 
    A = 1881*sqrt(2)*sqrt(5760573 + 2813807*sqrt(5))
    B = (A + 2563547*sqrt(15) + 6192143*sqrt(3))
    D = 4**(sr_one/3)*3**(sr_one/6)/B**(sr_one/3)
    fr_D = 4**(fr_one/3)*3**(fr_one/6)/B**(fr_one/3) # NOTE: 4**Fraction(1,3) -> float
    #assert not 0 == nsimplify(D-fr_D)
    
    _GG = 2*(-6/D - 71208*D + sqrt(5)*(-19752*D - 60) + 2022)/1881
    _g33335 = sqrt(_GG)
    assert verify_G(solid, _g33335)
    assert 0 == nsimplify(g33335 - _g33335)


    # factor the below 'f' into h over QQ[sqrt(5)]
    # see below 'f'
    u = (209*GG**6 - 2696*GG**5 + 13872*GG**4 - 35776*GG**3 + 47104*GG**2 - 27648*GG + 4096)
    #assert factor(u,extension={sqrt(5)}) == 209*(GG**3 + GG**2*(-1348/209 - 40*sqrt(5)/209) + GG*(256*sqrt(5)/209 + 2608/209) - 1312/209 - 416*sqrt(5)/209)*(GG**3 + GG**2*(-1348/209 + 40*sqrt(5)/209) + GG*(-256*sqrt(5)/209 + 2608/209) - 1312/209 + 416*sqrt(5)/209)
    assert resultant(u,h) == 0 # so, they have a same root that is GG
    assert 0 == expand(gcd(u,h,extension=True)*209 - h)
    return _g33335

    
    _g = 0.463856880645439
    _gg = _g**2
    ef = lambda f, gg=_gg: N(f.subs(GG, gg))
    tf = lambda f: bool(abs(ef(f)) < 1e-7)
    assert tf(f)

    P = sqrt(5)
    f = expand(2*f)
    f = collect(f, P)
    A, B = seperate_term(f, P)
    assert f == A+B
    f = expand(A**2 - B**2)
    assert tf(f)
    
    print(f)
    f /= 4
    assert f == (209*GG**6 - 2696*GG**5 + 13872*GG**4 - 35776*GG**3 + 47104*GG**2 - 27648*GG + 4096)


    assert tf(f)
    ggs = solve(f)
    # sympy bug1:
    #   solve(f) ==>> [1.50152930508540, 2.97263618194513, 2.40355087229957, 2.97263618194513]
    #   NOTE: 2.97263618194513 appear twice but miss 0.21516320572211706
    # sympy bug2:
    #   root of f == 4*(root of h)?? since solve(f)=[4*RootOf(h)...]
    #   where h = 209*GG**6 - 674*GG**5 + 867*GG**4 - 559*GG**3 + 184*GG**2 - 27*GG + 1
    #   but solve(h) == [] !!!
    #   while GG:positive=True
    #   but var('x'), solve(h)==[6 roots (4 reals)] and two real roots be the same
    print('gg', [N((gg)) for gg in ggs])
    print('g', [N(sqrt(gg)) for gg in ggs])
    ggs = [gg for gg in ggs if (0 < N(gg) < 4)]
    print([ef(f,gg) for gg in ggs])
    ggs = [gg for gg in ggs if verify_G(solid, sqrt(gg))]
    print(ggs)
    raise
    g33335 = sqrt(gg)
    g33335 = nsimplify(g33335)
    #assert 0 == nsimplify(g33335 - _g33335)

    assert verify_G(solid, g33335)
    return g33335

def __build_g33335():

    sr_one = GG/GG # Rational(1) 
    A = 1881*sqrt(2)*sqrt(5760573 + 2813807*sqrt(5))
    B = (A + 2563547*sqrt(15) + 6192143*sqrt(3))
    D = 4**(sr_one/3)*3**(sr_one/6)/B**(sr_one/3)
    #fr_D = 4**(fr_one/3)*3**(fr_one/6)/B**(fr_one/3) # NOTE: 4**Fraction(1,3) -> float
    #assert not 0 == nsimplify(D-fr_D)
    
    _GG = 2*(-6/D - 71208*D + sqrt(5)*(-19752*D - 60) + 2022)/1881
    _g33335 = sqrt(_GG)
    return _g33335
g33335 = __build_g33335()
g33334 = sqrt(-2*(42*sqrt(33) + 566)**(one/3)
              - 128/(42*sqrt(33) + 566)**(one/3) + 44) / sqrt(21)
ASRP33334_33335_to_g = {
    (3,3,3,3,4): g33334,
    (3,3,3,3,5): g33335,
    }



if __name__ == '__main__':
    assert 0 == nsimplify(g33334 - calc_g33334())
    assert 0 == nsimplify(g33335 - calc_g33335())
    
    print('ASRP33334_33335_to_g = {}'
          .format(ASRP33334_33335_to_g))

