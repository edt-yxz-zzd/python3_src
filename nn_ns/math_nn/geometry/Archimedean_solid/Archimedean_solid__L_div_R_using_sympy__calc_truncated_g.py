

from sympy import pi, cos, sqrt, tan, nsimplify, var, symbols, solve
from nn_ns.sympy_util.constant import zero, one
from nn_ns.sympy_util.my_sympify import my_sympify
from nn_ns.sympy_util.geometry import opposite_tri_edge, \
     angle_of_regular_polygon, outer_radius_of_regular_polygon, \
     inner_radius_of_regular_polygon

from .Archimedean_solid__transform import truncate_to
from .Archimedean_solid__L_div_R_using_sympy__calc_Platonic_g \
     import Platonic_solid2g
from .Archimedean_solid__L_div_R_using_sympy__classify_ASRP import verify_G


truncated_solid2org_solid = {new:org
                             for org, new in truncate_to.items()}


def calc_truncated_g(org_solid):
    #org = mid_truncated_solid2org_solid[solid]
    org_g = Platonic_solid2g[org_solid]

    n = org_solid[0] # n-gon face of org_solid
    angle = angle_of_regular_polygon(n)
    
    # assume org_L = 2; 1 = org_L/2
    org_L = 2*one
    org_L, X = symbols('org_L X', positive=True)
    new_L = opposite_tri_edge(org_L, angle, org_L)*X
    new_L_ = org_L*(1-2*X)
    x, = solve(new_L - new_L_, X)
    x = my_sympify(x)
    new_L = my_sympify(new_L.subs(X,x))

    org_R = org_L/org_g
    org_Rc = outer_radius_of_regular_polygon(n, org_L)
    org_rc = inner_radius_of_regular_polygon(n, org_L)
    org_HH = org_R**2 - org_Rc**2

    new_rc_rc = org_rc**2 + (new_L/2)**2
    new_RR = org_HH + new_rc_rc
    new_R = sqrt(new_RR)

    new_g = new_L/new_R
    g = my_sympify(new_g)
    g = nsimplify(g)

    if not g.is_number:
        print(locals())
    assert g.is_number
    return g


##calc_mid_truncated_g((3,3,3))
##raise

def __calc_truncated_solid2g():
    truncated_solid2g = {
        solid: calc_truncated_g(org_solid)
        for solid, org_solid in truncated_solid2org_solid.items()}

    if not all(verify_G(solid, g) for solid, g in truncated_solid2g.items()):
        for solid, g in truncated_solid2g.items():
            if not verify_G(solid, g):
                print(solid, g)
                print(truncated_solid2org_solid[solid])
    assert all(verify_G(solid, g) for solid, g in truncated_solid2g.items())
    return truncated_solid2g

#truncated_solid2g = __calc_truncated_solid2g()
truncated_solid2g = {
    (3, 8, 8): sqrt(-16*sqrt(2) + 28)/sqrt(17),
    (4, 6, 6): sqrt(10)/5,
    (5, 6, 6): sqrt(-18*sqrt(5) + 58)/sqrt(109),
    (3, 6, 6): 2*sqrt(22)/11,
    (3, 10, 10): sqrt(-30*sqrt(5) + 74)/sqrt(61)}

if __name__ == '__main__':
    _x = __calc_truncated_solid2g()
    if False and not _x == truncated_solid2g:
        print(_x)
        print(truncated_solid2g)
    assert len(_x) == len(truncated_solid2g)
    assert all(0 == nsimplify(g - _x[key]) for key, g in truncated_solid2g.items())
    print('truncated_solid2g = {}'.format(truncated_solid2g))


    

    
    
    


