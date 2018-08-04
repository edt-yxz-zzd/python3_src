


r'''
sympy bugs from Archimedean_solid__L_div_R_using_sympy
bug1 from calc_L_div_R:
    # calc g3434
    [3,4,3,4]:
        L/R should be 1
        but yields 0.999999999999999076021
        it seems sympy only have 15 precision
        even I set sympy.mpmath.mp.dps = 100 gets this wrong result
        it is far from real ans
    that is:
    var('g', positive=True)
    f = -48*asin(sqrt(2)/sqrt(-g**2 + 4)) - 48*asin(1/sqrt(-g**2 + 4)) + 24*pi
    assert 0 == nsimplify(f.subs(g,1))
    sympy.mpmath.mp.dps = 100
    x = nsolve(f, g, 1)
    assert str(x)[6:][:21] == '0.9999999999999990760'
    assert '0.9999999999999990760' in str(x)
    

bug2 from sorted_Cs2solids:
    assert hash(2) != hash(Integer(2))
    assert hash(Fraction(1,2)) != hash(Rational(1,2))
    fixed by:
        import nn_ns.sympy_util.bug_fix__rational_hash
bug3 from calc_g33335:
    var('GG', positive=True)
    u = (209*GG**6 - 2696*GG**5 + 13872*GG**4 - 35776*GG**3 + 47104*GG**2 - 27648*GG + 4096)
    h = (209*GG**3 + GG**2*(-1348 + 40*sqrt(5)) + GG*(-256*sqrt(5) + 2608) - 1312 + 416*sqrt(5))
    assert 0 == expand(gcd(u,h,extension=True)*209 - h)
    gg, = solve(h)
    assert 0 == nsimplify(u.subs(GG, gg))
    assert all(0 != nsimplify(gg - _gg) for _gg in solve(u))
    
'''


from sympy import *
import sympy.mpmath
from sympy.mpmath import findroot, mpf
from pprint import pprint

from nn_ns.sympy_util.constant import *
from nn_ns.sympy_util.add_terms import *
from nn_ns.sympy_util.geometry import *
from nn_ns.sympy_util.my_sympify import *

from .Archimedean_solid__which import Archimedean_solid2info

##from Archimedean_solid__using_sympy__zero_expr_K0_K1_W_of_Cs_half_2 import \
##     zero_expr_K0_K1_W_of_Cs_half_2

arcsin = asin
#help(findroot)
#sympy.core.evalf
#help(evalf)





#print(help(pprint))
#sympy.mpmath.mp.dps = 100
#calc_g()


if False:
    var('g', positive=True)
    __g = g
    f366 = -48*asin(sqrt(3)/sqrt(-g**2 + 4)) - 24*asin(1/sqrt(-g**2 + 4)) + 24*pi
    f3434 = -48*asin(sqrt(2)/sqrt(-g**2 + 4)) - 48*asin(1/sqrt(-g**2 + 4)) + 24*pi
    f3444 = -144*asin(sqrt(2)/sqrt(-g**2 + 4)) - 48*asin(1/sqrt(-g**2 + 4)) + 48*pi
    eval_fxxx = lambda f, x, dps=100: N(f, dps, subs={__g:x})

    fxxx_root_pairs = [(f366, sqrt(22)*2/11), (f3434, 1)]
    one = g/g
    err = one/10**60
    for fxxx, root in fxxx_root_pairs:
        _zero = eval_fxxx(fxxx, root, 100)
        assert abs(_zero) < err 

def calc_g3434():
    solid=(3,4,3,4)
    var('g', positive=True)
    g3434 = 1
    assert verify_G(solid, g3434)

    # sympy bug:
    dps = sympy.mpmath.mp.dps = 100
    x = calc_L_div_R(solid)

    ss = "mpf('0.9999999999999990760')"
    str_x = str(x)[6:][:21]
    print(str_x)
    assert str_x == '0.9999999999999990760'
    
    return g3434






def calc_4gon_diagonal():
    var('a b c d x y S')
    # S = tri_area(a,b,x) + tri_area(c,d,x)
    Y1 = tri_area(b,c,y)
    Y2 = tri_area(d,a,y)
    '''
    S = Y1+Y2
    S**2 = Y1**2+Y2**2 +2*Y1*Y2
    2*Y1*Y2 = S**2 - Y1**2+Y2**2
    (2*Y1*Y2)**2 - (S**2 - Y1**2+Y2**2)**2 == 0

    '''
    f = 256* ( (2*Y1*Y2)**2 - (S**2 - Y1**2+Y2**2)**2 )
    f = factor(sympify(expand(f)))



using = False
if using:
    var('X')
    #[3,4,4,4]
    #y = add_arcsin_with_coeffs((3,1), (1,1), sqrt(2)/X, 1/X)

    #[3,4,5,4]
    y = add_arcsin_with_coeffs((1,1), (1,1), 2*sin(3*pi/10)/X, 1/X)
    y = add_arcsin(sqrt(2)/X,y)
    print(y)
    ans = solve(y-1)

var('X Y Z XX YY ZZ g gg t tt T TT')
cf = collect




def calc_g3454():
    frr = 4*Y*(T + Z*t - t - 1)
    fzz = (T**2*(Y**2*Z + Y**2 - 4*Z**3 + 4*Z)
                           + T*(2*Y**2*Z**2*t - 2*Y**2*Z - 2*Y**2*t - 2*Y**2 + 4*Z**3 - 4*Z**2*ZZ*t + 4*Z**2*t - 4*Z**2 - 4*Z + 4*ZZ*t - 4*t)
                           + Y**2*(Z**3*t**2 - Z**2*t**2 - 2*Z**2*t - Z*t**2 + Z + t**2 + 2*t + 1)
                           + 4*Z**2*ZZ*t - 4*Z**2*t + 4*Z**2 - 4*ZZ*t + 4*t)
    f=(frr*sqrt(1-T)*sqrt(1+Z))**2 - fzz**2
    f=expand(f)
    f=collect_square_recur(f, T, t*t*Z*Z-t)
    f=collect_square_recur(f, Y, 2*Z*Z-1)
    h = collect_square_recur(f, t, t+1)
    h = h.subs(ZZ, Z*Z)
    f = even_square_sub_odd_square(h, T, t*t*Z*Z-t)
    f = collect_square_recur(f, t, t+1)
    h = f.subs(t, (sqrt(5)+1)/2)
    h = collect(expand(h), sqrt(5))
    var('r_5');
    h = h.subs(sqrt(5), r_5)
    f = even_square_sub_odd_square(h, r_5)
    f = f.subs(r_5, sqrt(5))
    f = expand(f)
    h = factor(f)
    h = 320*Z**4 - 400*Z**2 + 121
    f = collect_square_recur(h, Z, 1-1/(4-gg))
    f *= (4-gg)**2
    f = factor(simplify(f))
    ans, = [x for x in solve(f) if x < 1]
    g3454 = ans = nsimplify(sqrt(ans))
    return 






'''
def get_zero_expr_K0_K1_W_of_Cs_half_2():
    fname = '_Archimedean_solid__using_sympy__zero_expr_K0_K1_W_of_Cs_half_2'
    try:
        fin = open(fname)
    except FileNotFoundError:
        #raise logic-error
        _zero_expr_K0_K1_W_of_Cs_half_2 = calc_zero_expr_K0_K1_W_of_Cs_half_2()
        with open(fname, 'x') as fout:
            fout.write(str(_zero_expr_K0_K1_W_of_Cs_half_2))
    else:
        with fin:
            _zero_expr_K0_K1_W_of_Cs_half_2 = eval(fin.read())
    return _zero_expr_K0_K1_W_of_Cs_half_2
    
##_zero_expr_K0_K1_W_of_Cs_half_2 = get_zero_expr_K0_K1_W_of_Cs_half_2()
##_g = gcd(zero_expr_K0_K1_W_of_Cs_half_2, _zero_expr_K0_K1_W_of_Cs_half_2)
##print(len(str(_g)))'''


#calc_zero_expr_K0_K1_W_of_Cs_half_2()



'''
if False:
    for sorted_Cs in [(one/2, 2)] or sorted_Cs2solids:
        if len(sorted_Cs) == 2:
            print(sorted_Cs)
            f = two_asin2no_asin(sorted_Cs)
            print(f)

    '''


# sympy bug:
#    hash(2) != hash(Integer(2))
solid2L_div_R = {
    (3,3,3,3,4): sqrt(-2*(42*sqrt(33) + 566)**(one/3)
                      - 128/(42*sqrt(33) + 566)**(one/3) + 44) / sqrt(21),
    }

    return
#g33334 = calc_g33334()
#print(g33334)
##g33335 = calc_g33335()
##print(g33335)
#calc_zero_expr_K0_K1_W_of_Cs_half_2()

'''
raise


if False: # deprecated
    from sand import write_txt
    f = calc_g33334()
    write_txt('afsafsf', str(f), 'ascii')
    if True:
        g33334 = 0.744206331156206
        _gg = g33334 **2
        xx = 4-_gg
        w = 1/sqrt(xx)
        print(N(f.subs(W,w)))


    p = Poly(f, W)
    print(p.degree())
    root_rngs = intervals(p, inf=0,sup=2)
    
'''



calc_g3434()
    



    









    




    



























