

from .Archimedean_solid__L_div_R_using_sympy__calc_g33334_g33335_of_Cs_half_2 \
     import ASRP33334_33335_to_g
from .Archimedean_solid__L_div_R_using_sympy__calc_g468_g4610_of_Cs_half_half_half \
     import ASRP468_4610_to_g
from .Archimedean_solid__L_div_R_using_sympy__calc_g3444_g3454_of_Cs_half_half_1 \
     import ASRP3444_3454_to_g
from .Archimedean_solid__L_div_R_using_sympy__calc_g333v_g44v \
     import ASRP333v_44v_to_g

from .Archimedean_solid__L_div_R_using_sympy__calc_Platonic_g \
     import Platonic_solid2g
from .Archimedean_solid__L_div_R_using_sympy__calc_truncated_g \
     import truncated_solid2g
from .Archimedean_solid__L_div_R_using_sympy__calc_mid_truncated_g \
     import mid_truncated_solid2g
from .Archimedean_solid__which import solids
from .Archimedean_solid__L_div_R_using_sympy__classify_ASRP \
     import solid2sorted_C_Ks__fixed as solid2sorted_C_Ks, verify_G
from pprint import pprint

def __build_solid2g():
    solid2g = {}
    for _solid2g in [ASRP33334_33335_to_g, ASRP468_4610_to_g,
                     ASRP3444_3454_to_g, ASRP333v_44v_to_g,
                     Platonic_solid2g,
                     truncated_solid2g, mid_truncated_solid2g]:
        solid2g.update(_solid2g)
    return solid2g

solid2g = __build_solid2g()

if __name__ == '__main__':

    assert all(verify_G(solid, g) for solid, g in solid2g.items()
               if all(type(x) is int for x in solid))
    for solid in (set(solids) - set(solid2g)):
        print(solid, solid2sorted_C_Ks[solid])

    if not (set(solids) - set(solid2g)):
        print('solid2g = \\', )
        pprint(solid2g)

r'''
solid2g = \
{(3, 3, 3): 2*sqrt(6)/3,
 (3, 3, 3, 3): sqrt(2),
 (3, 3, 3, 3, 3): sqrt(-2*sqrt(5)/5 + 2),
 (3, 3, 3, 3, 4): sqrt(21)*sqrt(-2*(42*sqrt(33) + 566)**(1/3) - 128/(42*sqrt(33) + 566)**(1/3) + 44)/21,
 (3, 3, 3, 3, 5): sqrt(-2*2**(1/3)*3**(5/6)*(1881*sqrt(2)*sqrt(5760573 + 2813807*sqrt(5)) + 2563547*sqrt(15) + 6192143*sqrt(3))**(1/3)/1881 - 15824*2**(2/3)*3**(1/6)/(209*(1881*sqrt(2)*sqrt(5760573 + 2813807*sqrt(5)) + 2563547*sqrt(15) + 6192143*sqrt(3))**(1/3)) + 2*sqrt(5)*(-19752*2**(2/3)*3**(1/6)/(1881*sqrt(2)*sqrt(5760573 + 2813807*sqrt(5)) + 2563547*sqrt(15) + 6192143*sqrt(3))**(1/3) - 60)/1881 + 1348/627),
 (3, 3, 3, v): 2*sin(pi/v),
 (3, 4, 3, 4): 1,
 (3, 4, 4, 4): sqrt(17)*sqrt(-8*sqrt(2) + 20)/17,
 (3, 4, 5, 4): sqrt(41)*sqrt(-16*sqrt(5) + 44)/41,
 (3, 5, 3, 5): sqrt(2)/sqrt(sqrt(5) + 3),
 (3, 6, 6): 2*sqrt(22)/11,
 (3, 8, 8): sqrt(17)*sqrt(-16*sqrt(2) + 28)/17,
 (3, 10, 10): sqrt(61)*sqrt(-30*sqrt(5) + 74)/61,
 (4, 4, 4): 2*sqrt(3)/3,
 (4, 4, v): 2*sin(pi/v)/sqrt(sin(pi/v)**2 + 1),
 (4, 6, 6): sqrt(10)/5,
 (4, 6, 8): sqrt(97)*sqrt(-24*sqrt(2) + 52)/97,
 (4, 6, 10): sqrt(241)*sqrt(-48*sqrt(5) + 124)/241,
 (5, 5, 5): sqrt(-2*sqrt(5)/3 + 2),
 (5, 6, 6): sqrt(109)*sqrt(-18*sqrt(5) + 58)/109}


'''


'''
(4, 6, 8) ((1/2, sqrt(2)), (1/2, sqrt(3)), (1/2, sqrt(sqrt(2) + 2)))
(3, 4, 4, 4) ((1/2, 1), (3/2, sqrt(2)))
(4, 6, 10) ((1/2, sqrt(2)), (1/2, sqrt(3)), (1/2, sqrt(sqrt(5)/2 + 5/2)))
(3, 4, 5, 4) ((1/2, 1), (1/2, 1/2 + sqrt(5)/2), (1, sqrt(2)))
'''






