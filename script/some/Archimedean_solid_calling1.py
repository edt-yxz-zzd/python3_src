
from Archimedean_solid.Archimedean_solid__L_div_R_using_sympy__erase_asin_in_sum \
     import sum_asin2zero_radical_expr
from Archimedean_solid.Archimedean_solid__L_div_R_using_sympy__classify_ASRP import verify_G
from sympy import pi, sin, asin, sqrt, sympify, solve, nsolve, nsimplify, \
     symbols, var, Wild, expand, N, factor, collect
from nn_ns.sympy_util.add_terms import *
from nn_ns.sympy_util.constant import one
from nn_ns.sympy_util.my_sympify import my_sympify
sum_asin2zero_radical_expr

var('K0 K1 K2 W V X Y Z T WW VV XX YY ZZ TT U UU G GG K0W K1W K2W K0K1WW', positive=True)

zero_poly_K0K1K2W_of_Cs_half_half_half = (K0W**4 + 4*K0W**2*K1W**2*K2W**2 - 2*K0W**2*K1W**2 - 2*K0W**2*K2W**2 + K1W**4 - 2*K1W**2*K2W**2 + K2W**4)
zero_poly_GG_of_Cs_half_half_half = (-GG*K0**4 + 2*GG*K0**2*K1**2 + 2*GG*K0**2*K2**2 - GG*K1**4 + 2*GG*K1**2*K2**2 - GG*K2**4 + 4*K0**4 + 4*K0**2*K1**2*K2**2 - 8*K0**2*K1**2 - 8*K0**2*K2**2 + 4*K1**4 - 8*K1**2*K2**2 + 4*K2**4)

zero_poly_K0K1WVYX = (
    2*K0W**4*K1W**4 + 4*K0W**4*K1W**2*Z - 5*K0W**4*K1W**2 - 2*K0W**4*Z +
    2*K0W**4 - 2*K0W**3*K1W**3*V - 2*K0W**3*K1W**3*Y*Z + 4*K0W**3*K1W**3*Y
    - 4*K0W**3*K1W**3*Z + 8*K0W**3*K1W**3 - 4*K0W**3*K1W*V*Z +
    4*K0W**3*K1W*V + 4*K0W**3*K1W*Y*Z - 4*K0W**3*K1W*Y + 8*K0W**3*K1W*Z -
    8*K0W**3*K1W - 4*K0W**2*K1W**4*Y - 5*K0W**2*K1W**4 -
    K0W**2*K1W**2*K2W**2 + 2*K0W**2*K1W**2*V*Y*Z - 4*K0W**2*K1W**2*V*Y +
    4*K0W**2*K1W**2*V*Z - 8*K0W**2*K1W**2*V - 8*K0W**2*K1W**2*Y*Z +
    10*K0W**2*K1W**2*Y - 10*K0W**2*K1W**2*Z + 14*K0W**2*K1W**2 -
    2*K0W**2*K2W**2*Z + 2*K0W**2*K2W**2 - 4*K0W**2*V*Y*Z + 4*K0W**2*V*Y -
    8*K0W**2*V*Z + 8*K0W**2*V + 4*K0W**2*Y*Z - 4*K0W**2*Y + 8*K0W**2*Z -
    8*K0W**2 + 4*K0W*K1W**3*V*Y + 4*K0W*K1W**3*V + 4*K0W*K1W**3*Y*Z -
    8*K0W*K1W**3*Y + 4*K0W*K1W**3*Z - 8*K0W*K1W**3 + 8*K0W*K1W*V*Y*Z -
    8*K0W*K1W*V*Y + 8*K0W*K1W*V*Z - 8*K0W*K1W*V - 8*K0W*K1W*Y*Z +
    8*K0W*K1W*Y - 8*K0W*K1W*Z + 8*K0W*K1W + 2*K1W**4*Y + 2*K1W**4 +
    2*K1W**2*K2W**2*Y + 2*K1W**2*K2W**2 - 4*K1W**2*V*Y*Z + 8*K1W**2*V*Y -
    4*K1W**2*V*Z + 8*K1W**2*V + 4*K1W**2*Y*Z - 8*K1W**2*Y + 4*K1W**2*Z -
    8*K1W**2 + 4*K2W**2*Y*Z - 4*K2W**2*Y + 4*K2W**2*Z - 4*K2W**2 + 8*V*Y*Z
    - 8*V*Y + 8*V*Z - 8*V - 8*Y*Z + 8*Y - 8*Z + 8
    )



def __reduce_power(f):
    t = f
    t = sub_square_for_polynomial_only(t, V, 1-K2W**2)
    t = sub_square_for_polynomial_only(t, Z, 1-K1W**2)
    t = sub_square_for_polynomial_only(t, Y, 1-K0W**2)
    return t


def calc_zero_poly_K0K1K2W_of_Cs_half_half_half():
    # sorted_Cs2solids[(1/2, 1/2, 1/2)] == [(4, 6, 8), (4, 6, 10)]
    # solid2sorted_C_Ks:
    ## (4, 6, 8): ((1/2, sqrt(2)), (1/2, sqrt(3)), (1/2, sqrt(sqrt(2) + 2))),
    ## (4, 6, 10): ((1/2, sqrt(2)), (1/2, sqrt(3)), (1/2, sqrt(sqrt(5)/2 + 5/2))),


    solid2g_k0k1k2 = {
        (4, 6, 8): (0.431478810544531, (sqrt(2), sqrt(3), sqrt(sqrt(2) + 2))),
        (4, 6, 10): (0.2629921750726, (sqrt(2), sqrt(3), sqrt(sqrt(5)/2 + 5/2))),
        }

    
    # calc g, x, w, y, z, v, k0w, k1w, k2w
    solid2info = {}
    for solid, (g, (k0,k1,k2)) in solid2g_k0k1k2.items():
        gg = g*g;
        xx = 4-gg; x = sqrt(xx);
        ww = 1/xx; w = sqrt(ww);
        yy = 1-k0**2*ww; y = sqrt(yy);
        zz = 1-k1**2*ww; z = sqrt(zz);
        vv = 1-k2**2*ww; v = sqrt(vv);
        solid2info[solid] = {
            G:g, K0:k0, K1:k1, K2:k2, GG:gg,
            WW:ww, W:w, XX:xx, X:x, YY:yy, Y:y, ZZ:zz, Z:z,
            VV:vv, V:v, K0W:k0*w, K1W:k1*w, K2W:k2*w, K0K1WW:k0*w*k1*w
            }

    
    info = solid2info[(4, 6, 8)]
    def ef(f):
        assert f.subs(info).is_number
        return N(abs(f.subs(info)))
        if not f.subs(info).is_number:
            print('not f.subs(info).is_number:', f, info)
            pass
        return N(abs(f.subs(info).subs(K1,info[K1])))
    tf = lambda f: ef(f) < 1e-7


    zero_angle_of_Cs_half_half_half = sum_asin2zero_radical_expr((one/2,)*3)
    
    assert zero_angle_of_Cs_half_half_half == sqrt(2)*sqrt(-sqrt(-K0**2*W**2 + 1) + 1)*sqrt(sqrt(-K1**2*W**2 + 1) + 1)*sqrt(sqrt(-K2**2*W**2 + 1) + 1)/4 + sqrt(2)*sqrt(sqrt(-K0**2*W**2 + 1) + 1)*sqrt(-sqrt(-K1**2*W**2 + 1) + 1)*sqrt(sqrt(-K2**2*W**2 + 1) + 1)/4 + sqrt(-sqrt(-K2**2*W**2 + 1) + 1)*sqrt(sqrt(-K0**2*W**2 + 1)*sqrt(-K1**2*W**2 + 1) - sqrt(-sqrt(-K0**2*W**2 + 1) + 1)*sqrt(sqrt(-K0**2*W**2 + 1) + 1)*sqrt(-sqrt(-K1**2*W**2 + 1) + 1)*sqrt(sqrt(-K1**2*W**2 + 1) + 1) + 1)/2 - 1
    f = zero_angle_of_Cs_half_half_half
    assert tf(f)

    h = (f.subs(sqrt(1-K0**2*W**2), Y)
         .subs(sqrt(1-K1**2*W**2), Z)
         .subs(sqrt(1-K2**2*W**2), V))
    assert tf(h)
    assert h.free_symbols == {Z, Y, V}
    assert h == sqrt(-V + 1)*sqrt(Y*Z - sqrt(-Y + 1)*sqrt(Y + 1)*sqrt(-Z + 1)*sqrt(Z + 1) + 1)/2 + sqrt(2)*sqrt(V + 1)*sqrt(-Y + 1)*sqrt(Z + 1)/4 + sqrt(2)*sqrt(V + 1)*sqrt(Y + 1)*sqrt(-Z + 1)/4 - 1
    h *= 4*sqrt(V + 1)*sqrt(Y + 1)*sqrt(-Z + 1); h = expand(h)
    h = h.subs(sqrt(1-Z)*sqrt(1+Z), K1*W).subs(sqrt(1-Y)*sqrt(1+Y), K0*W)
    assert tf(h)

    h1 = sqrt(2)*K0*K1*V*W**2 + sqrt(2)*K0*K1*W**2 - sqrt(2)*V*Y*Z + sqrt(2)*V*Y - sqrt(2)*V*Z + sqrt(2)*V - sqrt(2)*Y*Z + sqrt(2)*Y - sqrt(2)*Z - 4*sqrt(V + 1)*sqrt(Y + 1)*sqrt(-Z + 1) + sqrt(2)
    h2 = 2*sqrt(-V + 1)*sqrt(V + 1)*sqrt(Y + 1)*sqrt(-Z + 1)*sqrt(-K0*K1*W**2 + Y*Z + 1)
    assert h == h1 + h2
    f = expand(h1**2 - h2**2)
    f = f.subs(K0*W, K0W).subs(K1*W, K1W)
    assert tf(f)

    P = sqrt(V + 1)*sqrt(Y + 1)*sqrt(-Z + 1)
    f = collect(f, P)
    A, B = seperate_term(f, P)
    h = expand(A**2 - B**2)
    assert tf(h)
    
    f = factor(h)/(V + 1)**2/4
    assert tf(f)

    assert f.free_symbols == {Z, V, Y, K0W, K1W}
    f = Poly(f, Z, V, Y, K0W, K1W)
    f = __reduce_power(f)
    f = factor(f/16)

    assert f == zero_poly_K0K1WVYX

    #print(f)
    #print(len(str(f)))
    f = expand(even_square_sub_odd_square(f, V, 1-K2W**2))
    assert V not in f.free_symbols
    f = sub_square_for_polynomial_only(f, Z, 1-K1W**2)
    f = sub_square_for_polynomial_only(f, Y, 1-K0W**2)
    #print(len(str(f)))
    f = expand(even_square_sub_odd_square(f, Z, 1-K1W**2))
    assert Z not in f.free_symbols
    f = sub_square_for_polynomial_only(f, Y, 1-K0W**2)
    #print(len(str(f)))
    f = expand(even_square_sub_odd_square(f, Y, 1-K0W**2))
    assert Y not in f.free_symbols
    #print(len(str(f)))

    h = zero_poly_K0K1K2W_of_Cs_half_half_half
    assert factor(f) == (K0W**16*K1W**16*h**4)
    assert tf(h)

    return h

def get_zero_poly_GG_of_Cs_half_half_half():
    f = zero_poly_K0K1K2W_of_Cs_half_half_half.subs({K0W: K0*W, K1W: K1*W, K2W: K2*W})
    f = expand(f/W**4)
    h = f.subs(W*W, 1/(4-GG))
    h *= (4-GG)
    h = expand(factor(h))
    assert h == zero_poly_GG_of_Cs_half_half_half
    return h













