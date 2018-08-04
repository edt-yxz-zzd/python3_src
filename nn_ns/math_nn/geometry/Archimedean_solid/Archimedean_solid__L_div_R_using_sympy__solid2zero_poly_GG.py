


from nn_ns.sympy_util.constant import *
from .Archimedean_solid__L_div_R_using_sympy__classify_ASRP \
     import solid2sorted_C_Ks__fixed as solid2sorted_C_Ks
from sympy import sympify, var


__all__ = ('sorted_Cs2zero_poly_Ks_GG, solid2zero_poly_GG'.split())

var('K0 K1 K2 G GG', positive=True)

sorted_Cs2zero_poly_Ks_GG = {
    (half, two): (GG**3*(-K0**2 + 16*K1**2) + GG**2*(12*K0**2 + 80*K1**4 - 192*K1**2) + GG*(-48*K0**2 + 128*K1**6 - 640*K1**4 + 768*K1**2) + 64*K0**2 + 64*K1**8 - 512*K1**6 + 1280*K1**4 - 1024*K1**2),
    (half,)*3: (-GG*K0**4 + 2*GG*K0**2*K1**2 + 2*GG*K0**2*K2**2 - GG*K1**4 + 2*GG*K1**2*K2**2 - GG*K2**4 + 4*K0**4 + 4*K0**2*K1**2*K2**2 - 8*K0**2*K1**2 - 8*K0**2*K2**2 + 4*K1**4 - 8*K1**2*K2**2 + 4*K2**4),
    (half, half, one): (-GG*K0**2 + 2*GG*K0*K1 - GG*K1**2 + 4*GG*K2**2 + 4*K0**2 + 4*K0*K1*K2**2 - 8*K0*K1 + 4*K1**2 + 4*K2**4 - 16*K2**2)
    }


def solid2sorted_Cs_Kdict(solid):
    C_Ks = solid2sorted_C_Ks[solid]
    assert 1 <= len(C_Ks) <= 3
    
    sorted_Cs = tuple(c for c,k in C_Ks)
    ks = tuple(k for c,k in C_Ks)
    Ks = [K0, K1, K2]
    Kdict = dict(zip(Ks, ks))
    return sorted_Cs, Kdict
    
def solid2zero_poly_GG(solid):
    sorted_Cs, Kdict = solid2sorted_Cs_Kdict(solid)
    zero_expr = sorted_Cs2zero_poly_Ks_GG[sorted_Cs]
    f = zero_expr.subs(Kdict)
    assert f.free_symbols == {GG}
    f = sympify(f)
    return f







