#__all__:goto
#API:goto
r'''[[[
e ../../python3_src/seed/math/inv_mod_.py
py -m seed.math.inv_mod_
from seed.math.inv_mod_ import inv_mod_
from seed.math.inv_mod_ex import inv_mod_power__coprime_
from seed.math.inv_mod_ex import upgrade__inv_mod_power__coprime_
from seed.math.inv_mod_ex import inv_mod_


view ../../python3_src/nn_ns/math_nn/integer/inv_mod_.py
from nn_ns.math_nn.integer.inv_mod_ import inv_mod_

view ../../python3_src/seed/math/continued_fraction/continued_fraction_fold.py
from seed.math.continued_fraction.continued_fraction_fold import inv_mod_


#]]]'''
__all__ = '''
    inv_mod_
    ginv_mod_respectively_
    ginv_mod_
    '''.split()

#from nn_ns.math_nn.integer.inv_mod_ import inv_mod_
from seed.math.continued_fraction.continued_fraction_fold import inv_mod_, ginv_mod_respectively_, ginv_mod_

assert inv_mod_(1, 0) == 0
assert inv_mod_(1, 4) == 0
assert inv_mod_(3, 2) == 2
assert inv_mod_(-3, 2) == 2
assert inv_mod_(3, -2) == 1
assert inv_mod_(-3, -2) == 1

def __():
    # API:here
    __all__
    def inv_mod_(M, x, /):
        '[M=!=0] ==>> [0 <= inv_mod_(M, x) < abs(M)][(inv_mod_(M, x)*x-1)%M == 0]'
        # !! gcd ~ log2(M) steps
        # O(log2(M)**3)
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


from seed.math.inv_mod_ import inv_mod_, ginv_mod_respectively_, ginv_mod_
from seed.math.inv_mod_ import *
