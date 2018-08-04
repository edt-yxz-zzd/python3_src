

from .Archimedean_solid__L_div_R_using_sympy__erase_asin_in_sum \
     import two_asin2no_asin
from .Archimedean_solid__L_div_R_using_sympy__classify_ASRP import verify_G
from sympy import pi, sin, asin, sqrt, sympify, solve, nsolve, nsimplify, \
     symbols, var, Wild, expand, N, factor, collect
from nn_ns.sympy_util.add_terms import *
from nn_ns.sympy_util.constant import one
from nn_ns.sympy_util.my_sympify import my_sympify
two_asin2no_asin

var('K0 K1 K2 W X Y Z T XX YY ZZ TT WW U UU G GG', positive=True)

def calc_zero_poly_K0K1W_of_Cs_half_2():
    # sorted_Cs2solids[(1/2, 2)] == [(3, 3, 3, 3, 5), (3, 3, 3, 3, 4)]
    # solid2sorted_C_Ks:
    ## (3, 3, 3, 3, 4): ((1/2, sqrt(2)), (2, 1)),
    ## (3, 3, 3, 3, 5): ((1/2, 1/2 + sqrt(5)/2), (2, 1)),


    solid2g_k0k1 = {
        (3, 3, 3, 3, 4): (0.744206331156206, (sqrt(2), 1)),
        (3, 3, 3, 3, 5): (0.463856880645439, ((1+sqrt(5))/2, 1)),
        }
    # calc x, w, y, z, t, u
    solid2info = {}
    for solid, (g, (k0,k1)) in solid2g_k0k1.items():
        gg = g*g;
        xx = 4-gg; x = sqrt(xx);
        ww = 1/xx; w = sqrt(ww);
        yy = 1-k0**2*ww; y = sqrt(yy);
        zz = 1-k1**2*ww; z = sqrt(zz);
        tt = 1+y; t = sqrt(tt);
        uu = 2-tt; u = sqrt(uu)
        solid2info[solid] = {
            G:g, K0:k0, K1:k1, GG:gg,
            WW:ww, W:w, XX:xx, X:x, YY:yy, Y:y, ZZ:zz, Z:z,
            TT:tt, T:t, UU:uu, U:u,
            }
    info = solid2info[(3, 3, 3, 3, 4)]
    def ef(f):
        assert f.subs(info).is_number
        return N(abs(f.subs(info)))
        if not f.subs(info).is_number:
            print('not f.subs(info).is_number:', f, info)
            pass
        return N(abs(f.subs(info).subs(K1,info[K1])))
    tf = lambda f: ef(f) < 1e-7

    zero_angle_of_Cs_half_2 = two_asin2no_asin((one/2, 2))
    assert zero_angle_of_Cs_half_2 == -K1**2*W**2*sqrt(-2*sqrt(-K0**2*W**2 + 1) + 2)/2 + sqrt(2)*K1*W*sqrt(-K1**2*W**2 + 1)*sqrt(sqrt(-K0**2*W**2 + 1) + 1)/2 + K1*W*sqrt(-4*K1**2*W**2*sqrt(-K0**2*W**2 + 1) - 4*K1*W*sqrt(-K1**2*W**2 + 1)*sqrt(-sqrt(-K0**2*W**2 + 1) + 1)*sqrt(sqrt(-K0**2*W**2 + 1) + 1) + 2*sqrt(-K0**2*W**2 + 1) + 2)/2 + sqrt(-2*sqrt(-K0**2*W**2 + 1) + 2)/2 - 1
    # 33334: 0 == -48*asin(sqrt(2)/sqrt(-g**2 + 4)) - 192*asin(1/sqrt(-g**2 + 4)) + 48*pi
    f = zero_angle_of_Cs_half_2
    assert tf(f)
    
    h = f.subs(sqrt(1-K0**2*W**2), Y).subs(sqrt(1-K1**2*W**2), Z)
    assert tf(h)
    assert h.free_symbols == {Z, K1, W, Y}
    h = h.subs(Y, T*T-1)
    assert tf(h)
    h = my_sympify(h)
    assert h.free_symbols == {Z, K1, W, T}
    _c, _h = h.as_content_primitive()
    assert _c.is_number
    # _c*_h != h
    h /= _c
    
    #print(h)
    h1 = -K1**2*W**2*sqrt(-2*T**2 + 4) + sqrt(2)*K1*T*W*Z + sqrt(-2*T**2 + 4) - 2
    h2 = K1*W*sqrt(-4*K1**2*T**2*W**2 + 4*K1**2*W**2 - 4*K1*T*W*Z*sqrt(-T**2 + 2) + 2*T**2)
    assert h == h1 + h2
    assert tf(h)
    f = h1**2 - h2**2; f = expand(f)
    assert tf(f)

    f = f.subs(T*T, 2-U*U); f = expand(f)
    h = expand(even_square_sub_odd_square(f, U, 2-T*T))
    assert h.free_symbols == {K1, W, T, Z}
    assert tf(h)

    # remove T
    f = expand(even_square_sub_odd_square(h, T, 1+Y))
    assert f.free_symbols == {K1, W, Y, Z}
    assert tf(f)
    h = expand(even_square_sub_odd_square(f, Y, 1-K0**2*W**2))
    assert h.free_symbols == {K1, W, K0, Z}
    assert tf(h)
    f = expand(even_square_sub_odd_square(h, Z, 1-K1**2*W**2))
    assert f.free_symbols == {K1, W, K0}
    assert tf(f)

    h = factor(f)
    assert h == 65536*K0**8*W**16*(K0**2 + 64*K1**8*W**6 - 128*K1**6*W**4 + 80*K1**4*W**2 - 16*K1**2)**4
    f = (K0**2 + 64*K1**8*W**6 - 128*K1**6*W**4 + 80*K1**4*W**2 - 16*K1**2)
    assert tf(f)
    deg = Poly(f, W).degree()
    assert deg % 2 == 0
    h = f.subs(W*W, 1/(4-GG)) * (4-GG)**(deg//2)
    h = factor(h)
    h = collect(h, GG)
    assert tf(h)
    assert h == GG**3*(-K0**2 + 16*K1**2) + GG**2*(12*K0**2 + 80*K1**4 - 192*K1**2) + GG*(-48*K0**2 + 128*K1**6 - 640*K1**4 + 768*K1**2) + 64*K0**2 + 64*K1**8 - 512*K1**6 + 1280*K1**4 - 1024*K1**2
    return h

    #############################
    P = sqrt(-sqrt(2)*U**2 + 4)
    f = collect(f, P)
    # fail:
    ##A, B = map(Wild, 'AB')
    ##d = (A + B*P).matches(f)
    ##assert d[A] + d[B]*P == f
    ##h = d[A]**2 - (d[B]*P)**2
    d = get_order2coeff_of(f,P)
    assert set(d) == {0,1}
    assert d[0] + d[1]*P == f
    h = d[0]**2 - (d[1]*P)**2; h = my_sympify(h)



if __name__ == '__main__':
    print(calc_zero_poly_K0K1W_of_Cs_half_2())












