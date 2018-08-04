
'''
Platonic solids = ASRP([A]*t)
'''

from .Archimedean_solid__which import solids
from .Archimedean_solid__L_div_R_using_sympy__classify_ASRP \
     import solid2zeroexpr, verify_G
from sympy import solve, nsimplify, sqrt


def __calc_Platonic_solid2g():
    Platonic_solid2g = {}
    for solid in solids:
        if len(set(solid)) != 1: continue
        # Platonic
        f = solid2zeroexpr[solid]
        gs = solve(f)
        g, = gs
        g = nsimplify(g)
        Platonic_solid2g[solid] = g
    return Platonic_solid2g

#Platonic_solid2g = __calc_Platonic_solid2g()

Platonic_solid2g = {
    (3, 3, 3): 2*sqrt(6)/3,
    (3, 3, 3, 3, 3): sqrt(-2*sqrt(5)/5 + 2),
    (3, 3, 3, 3): sqrt(2),
    (5, 5, 5): sqrt(-2*sqrt(5)/3 + 2),
    (4, 4, 4): 2*sqrt(3)/3}

if __name__ == '__main__':
    assert Platonic_solid2g == __calc_Platonic_solid2g()
    print('Platonic_solid2g = {}'.format(Platonic_solid2g))





    
    
        
