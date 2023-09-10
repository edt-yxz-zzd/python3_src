#API:goto
__all__ = '''
    inv_mod_    inv_mod__coprime_
        upgrade__inv_mod_power__coprime_
            inv_mod_power__coprime_
    ginv_mod_respectively_
    ginv_mod_
    '''.split()

from seed.math.sqrts_mod_ import upgrade__inv_mod_power__coprime_
from seed.math.sqrts_mod_ import inv_mod_power__coprime_
from seed.math.sqrts_mod_ import inv_mod__coprime_
from seed.math.inv_mod_ import inv_mod_, ginv_mod_respectively_, ginv_mod_
inv_mod_ = inv_mod__coprime_

def __():
    # API:here
    __all__
    inv_mod__coprime_ = inv_mod_
    def inv_mod_(M, x, /):
        '[M=!=0] ==>> [0 <= inv_mod_(M, x) < abs(M)][(inv_mod_(M, x)*x-1)%M == 0]'
        # !! gcd ~ log2(M) steps
        # O(log2(M)**3)

    def inv_mod_power__coprime_(m, k, x, /):
        'm -> k -> x -> inv_x/uint%m**k # [[m >= 2][k >= 1][gcd(m,x)==1][x*inv_x %m**k == 1]]'
        # O((k**3 + log2(m))*log2(m)**2)



    #from seed.math.sqrts_mod_ import _upgrade__inv_mod_power__coprime_
    def upgrade__inv_mod_power__coprime_(m, i, j, x_0_i, x_i_ij, inv_x_0_i, m_i, m_j, /):
        r'''[[[
    'm -> i -> j -> x_0_i -> x_i_ij -> inv_x_0_i -> m_i -> m_j -> (inv_x_i_ij, inv_x_0_ij) # [[m >= 2][1 <= j <= i][m_i == m**i][m_j == m**j][0 < *_0_i < m**i][0 <= *_i_ij < m**j][0 <= *_0_ij < m**(i+j)]]'

    O(i**2 * log2(p)**2)

    ######################
    [inv_x_0_i =[def]= inv_mod_(m**i; x_0_i)]
    [inv_x_0_ij =[def]= inv_mod_(m**(i+j); x_0_ij)]
    ######################
    known:  i, j, x_0_i, x_i_ij, inv_x_0_i
    unknown: inv_x_i_ij
    ######################
    constraints:
    [m >= 2]
    [gcd(m, x_0_i) == 1]

    [1 <= j <= i]
    [x_0_i*inv_x_0_i %m**i == 1]
    [x_0_ij*inv_x_0_ij %m**(i+j) == 1]
    [m_i == m**i]
    [m_j == m**j]
    [0 < x_0_i < m**i]
    [0 < inv_x_0_i < m**i]
    [0 <= x_i_ij < m**j]
    [0 <= inv_x_i_ij < m**j]

    [x_0_ij == x_0_i + x_i_ij*m**i]
    [inv_x_0_ij == inv_x_0_i + inv_x_i_ij*m**i]
    [0 <= x_0_ij < m**(i+j)]
    [0 <= inv_x_0_ij < m**(i+j)]
    ######################

    #]]]'''#'''
        # O(i**2 * log2(p)**2)

    def ginv_mod_respectively_(u, v, /):
        r'''[[[
    :: u/pint -> v/pint -> (inv_u_g/uint%v_g, inv_v_g/uint%u_g, k4u, k4v, gcd_of_uv, u_g, v_g)

    (inv_u_g, inv_v_g, k4u, k4v, gcd_of_uv, u_g, v_g) = ginv_mod_respectively_(u, v)
    precondition:
    [u >= 1]
    [v >= 1]

    postcondition:
    [inv_u_g*u_g =[%v_g]= 1]
    [inv_v_g*v_g =[%u_g]= 1]

    [k4u*u +k4v*v == gcd_of_uv >= 0]
    [[u_g*gcd_of_uv == u][v_g*gcd_of_uv == v]
    [k4u*u_g +k4v*v_g == 1]

    #]]]'''#'''
        # !! gcd ~ log2(u) steps
        # O(log2(u)**3)
    def ginv_mod_(M, x, /):
        r'''[[[
    :: M/pint -> x/int -> (inv_x_g/uint%M_g, k4M, k4x, gcd_of_Mx, M_g, x_g)

    (inv_x_g, k4M, k4x, gcd_of_Mx, M_g, x_g) = ginv_mod_(M, x)
    precondition:
    [M >= 1]
    [x :: int] #while ginv_mod_respectively_ requires [v>=1]

    postcondition:
    [inv_x_g*x_g =[%M_g]= 1]

    [k4M*M +k4x*x == gcd_of_Mx >= 0]
    [[M_g*gcd_of_Mx == M][x_g*gcd_of_Mx == x]
    [k4M*M_g +k4x*x_g == 1]

    #]]]'''#'''

        # !! gcd ~ log2(M) steps
        # O(log2(M)**3)



__all__

from seed.math.inv_mod_ex import inv_mod_power__coprime_
from seed.math.inv_mod_ex import upgrade__inv_mod_power__coprime_
from seed.math.inv_mod_ex import inv_mod_
from seed.math.inv_mod_ex import inv_mod_, ginv_mod_respectively_, ginv_mod_
from seed.math.inv_mod_ex import *

