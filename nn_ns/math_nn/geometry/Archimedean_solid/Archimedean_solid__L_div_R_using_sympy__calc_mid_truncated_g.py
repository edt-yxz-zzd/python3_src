

from sympy import pi, cos, sqrt, tan, nsimplify, var, symbols
from nn_ns.sympy_util.constant import zero, one
from nn_ns.sympy_util.my_sympify import my_sympify
from nn_ns.sympy_util.geometry import opposite_tri_edge, \
     angle_of_regular_polygon, outer_radius_of_regular_polygon, \
     inner_radius_of_regular_polygon

from .Archimedean_solid__transform import mid_truncate_to
from .Archimedean_solid__L_div_R_using_sympy__calc_Platonic_g \
     import Platonic_solid2g
from .Archimedean_solid__L_div_R_using_sympy__classify_ASRP import verify_G


mid_truncated_solid2org_solid = {new:org
                                 for org, new in mid_truncate_to.items()}


def calc_mid_truncated_g(org_solid):
    #org = mid_truncated_solid2org_solid[solid]
    org_g = Platonic_solid2g[org_solid]

    n = org_solid[0] # n-gon face of org_solid
    angle = angle_of_regular_polygon(n)
    
    # assume org_L = 2; 1 = org_L/2
    org_L = 2*one
    org_L = symbols('org_L', positive=True)
    new_L = opposite_tri_edge(org_L, angle, org_L)/2

    org_R = org_L/org_g
    org_Rc = outer_radius_of_regular_polygon(n, org_L)
    org_rc = inner_radius_of_regular_polygon(n, org_L)
    org_HH = org_R**2 - org_Rc**2
    new_RR = org_HH + org_rc**2
    new_R = sqrt(new_RR)

    new_g = new_L/new_R
    g = my_sympify(new_g)

    if not g.is_number:
        print(locals())
    assert g.is_number
    return g


##calc_mid_truncated_g((3,3,3))
##raise

def __calc_mid_truncated_solid2g():
    mid_truncated_solid2g = {
        solid: calc_mid_truncated_g(org_solid)
        for solid, org_solid in mid_truncated_solid2org_solid.items()}

    if not all(verify_G(solid, g) for solid, g in mid_truncated_solid2g.items()):
        for solid, g in mid_truncated_solid2g.items():
            if not verify_G(solid, g):
                print(solid, g)
                print(mid_truncated_solid2org_solid[solid])
    assert all(verify_G(solid, g) for solid, g in mid_truncated_solid2g.items())
    return mid_truncated_solid2g


#mid_truncated_solid2g = __calc_mid_truncated_solid2g()
mid_truncated_solid2g = {
    (3, 4, 3, 4): 1,
    (3, 3, 3, 3): sqrt(2),
    (3, 5, 3, 5): sqrt(2)/sqrt(sqrt(5) + 3)}

if __name__ == '__main__':
    assert mid_truncated_solid2g == __calc_mid_truncated_solid2g()
    print('mid_truncated_solid2g = {}'.format(mid_truncated_solid2g))


    

    
    
    


