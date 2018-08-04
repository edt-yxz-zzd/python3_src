
from sympy import pi, cos, sqrt, tan, nsimplify, var, symbols, \
     solve, expand, sin, sympify, Abs
from nn_ns.sympy_util.constant import zero, one
from nn_ns.sympy_util.my_sympify import my_sympify
from nn_ns.sympy_util.geometry import opposite_tri_edge, \
     angle_of_regular_polygon, outer_radius_of_regular_polygon, \
     inner_radius_of_regular_polygon

from .Archimedean_solid__transform import truncate_to
from .Archimedean_solid__L_div_R_using_sympy__calc_Platonic_g \
     import Platonic_solid2g
from .Archimedean_solid__L_div_R_using_sympy__classify_ASRP import verify_G
from .Archimedean_solid__which_using_sympy import v


#calc_g44v:

var('L R GG', positive=True)

'''
h = distance of 2 v-gon faces of 333v or 44v

Rc_v = outer_radius_of_regular_polygon(v, L)
Hc_v**2 = R**2 - Rc_v**2
h = 2*Hc_v
'''

    
def calc_zero_poly_vGG_of_ASRP333v():
    Rc_v = outer_radius_of_regular_polygon(v, L)
    Rc_2v = outer_radius_of_regular_polygon(v, L)
    Rc_2v_div_L__square = expand(Rc_2v**2/L**2)
    L_2v_of_Rc_2v_eq_Rc_v = Rc_v**2/Rc_2v_div_L__square
    hh = L**2 - L_2v_of_Rc_2v_eq_Rc_v
    hh_ = 4*(R**2 - Rc_v**2)
    f = expand(hh - hh_)
    assert f == L**2/sin(pi/v)**2 - 4*R**2
    f = f.subs(L**2, GG*R**2)
    f = expand(f/R**2*sin(pi/v)**2)
    return f
                             

def calc_zero_poly_vGG_of_ASRP44v():
    Rc_v = sqrt(R**2 - (L/2)**2)
    Rc_v_ = outer_radius_of_regular_polygon(v, L)

    f = Rc_v**2 - Rc_v_**2
    f = expand(f)
    assert f == -L**2/4 - L**2/(4*sin(pi/v)**2) + R**2
    f = f.subs(L**2, GG*R**2)
    f = expand(f/-R**2*(4*sin(pi/v)**2))
    assert f == GG*sin(pi/v)**2 + GG - 4*sin(pi/v)**2
    return f



def solve_poly_GG(f):
    gg, = solve(f, GG)
    g = sympify(sqrt(gg)).subs(Abs(sin(pi/v)), sin(pi/v))
    return g


zero_poly_vGG_of_ASRP44v = GG*sin(pi/v)**2 + GG - 4*sin(pi/v)**2
zero_poly_vGG_of_ASRP333v = GG - 4*sin(pi/v)**2
ASRP333v_44v_to_zero_poly_vGG = \
    {(4, 4, v): zero_poly_vGG_of_ASRP44v, (3, 3, 3, v): zero_poly_vGG_of_ASRP333v}

g44v = 2*sin(pi/v)/sqrt(sin(pi/v)**2 + 1)
g333v = 2*sin(pi/v)
ASRP333v_44v_to_g = {(4, 4, v): g44v, (3, 3, 3, v): g333v}



# fail to simplify:
##assert verify_G((4,4,v), g44v)
##assert verify_G((3,3,3,v), g333v)

def __verify():
    for solid in ASRP333v_44v_to_g:
        gv = ASRP333v_44v_to_g[solid]
        zero_poly_vGG = ASRP333v_44v_to_zero_poly_vGG[solid]
        zero_poly_v = zero_poly_vGG.subs(GG, gv**2)
        for i in range(3, 20):
            zero = zero_poly_v.subs(v, i)
            assert 0 == nsimplify(zero)
        
__verify()

if __name__ == '__main__':
    assert zero_poly_vGG_of_ASRP44v == calc_zero_poly_vGG_of_ASRP44v()
    assert zero_poly_vGG_of_ASRP333v == calc_zero_poly_vGG_of_ASRP333v()
    assert g44v == solve_poly_GG(zero_poly_vGG_of_ASRP44v)
    assert g333v == solve_poly_GG(zero_poly_vGG_of_ASRP333v)

    for name in ('zero_poly_vGG_of_ASRP44v, zero_poly_vGG_of_ASRP333v'
                 ', g44v, g333v'.split(', ')):
        _obj = globals()[name]
        print('{} = {}'.format(name, _obj))
        

























