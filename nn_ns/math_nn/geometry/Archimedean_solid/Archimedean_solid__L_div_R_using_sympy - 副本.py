


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

debug = False


def calc_L_div_R__z(n):
    return pi - 2*pi/n

def calc_L_div_R__alpah(n, g):
    z = calc_L_div_R__z(n)
    x = 2*sin(z/2)/sqrt(4-g*g)
    alpha = arcsin(x)*2
    return alpha

def calc_L_div_R__AA(n, g):
    alpha = calc_L_div_R__alpah(n, g)
    return n*alpha - (n-2)*pi


def solid2zero_expr(solid, g):
    solid = tuple(map(int, solid))
    info = Archimedean_solid2info[solid]
    shape2count = info['shape2count']

    AA = calc_L_div_R__AA
    
    f = 4*pi-sum(AA(n,g)*f for n, f in shape2count.items())
    f = sympify(f)
    return f


def calc_L_div_R(solid, g = symbols('g', positive=True)):
    '''see Archimedean_solid.py::spherical polygon::n-spherical_polygon

z = angle of n-gon = pi - 2*pi/n
sin(alpha/2) = sin(z/2)/2 * 4/sqrt(4-gg)
    = 2*sin(z/2)/sqrt(4-gg) where g=L/R


AA(n,g) = n*alpha - (n-2)*pi
[given ASRP to calc g]:
    0 == 4*pi-sum(AA(n,g)*f for n, f in ASRP.shape2count.items()) ==>> g=??

'''
    f = solid2zero_expr(solid, g)
    eq = '0 == {}'.format(f)
    
    try:
        ans = solve(f)
    except NotImplementedError:
        #print('using nsolve')
        ans = nsolve(f, g, 1)
        #print('after nsolve')
##        ff = lambda x: f.evalf(subs={g:x})
##        ff = lambda x: f.subs(g,x).evalf()
##        print(ff(1))
##        ans = findroot(ff, 1)

        assert ans.imag < 1e-20
        ans = ans.real
        
##        print(sympy.mpmath.mp.dps)
##        print(ans)
##        sympy.mpmath.mp.dps = 1
##        print(ans) # yield it changes!
        
    else:
        ans = list(x for x in ans if x>0)
        assert len(ans) == 1
        ans, = ans
        ans = nsimplify(ans)
        ans = sympify(ans)
##    ans = powsimp(ans)
##    ans = trigsimp(ans)
##    ans = expand(ans)
    
    return ans, eq
    
def calc_g():
    indent = 4
    for solid in [] or Archimedean_solid2info:
        print(solid)
        try:
            ans, eq = x = calc_L_div_R(solid)
            print('\t', ans)
            print('\t', eq)
            #print('\t', x)
            #print(' '*indent, end='')
            #pprint(x, indent=indent)
        except Exception as e:
            print('\t', type(e))
            
    '''
(3, 3, 3)
	 2*sqrt(6)/3
	 0 == -24*asin(1/sqrt(-g**2 + 4)) + 8*pi
(4, 6, 6)
	 0.632455532033675
	 0 == -48*asin(sqrt(2)/sqrt(-g**2 + 4)) - 96*asin(sqrt(3)/sqrt(-g**2 + 4)) + 48*pi
(3, 3, 3, 3, 3)
	 sqrt(-2*sqrt(5)/5 + 2)
	 0 == -120*asin(1/sqrt(-g**2 + 4)) + 24*pi
(3, 4, 3, 4)
	 0.999999999999999
	 0 == -48*asin(sqrt(2)/sqrt(-g**2 + 4)) - 48*asin(1/sqrt(-g**2 + 4)) + 24*pi
(3, 3, 3, 3, 5)
	 0.463856880645439
	 0 == -120*asin(2*sin(3*pi/10)/sqrt(-g**2 + 4)) - 480*asin(1/sqrt(-g**2 + 4)) + 120*pi
(3, 4, 4, 4)
	 0.714813488673185
	 0 == -144*asin(sqrt(2)/sqrt(-g**2 + 4)) - 48*asin(1/sqrt(-g**2 + 4)) + 48*pi
(3, 10, 10)
	 0.336762811773427
	 0 == -240*asin(2*sqrt(sqrt(5)/8 + 5/8)/sqrt(-g**2 + 4)) - 120*asin(1/sqrt(-g**2 + 4)) + 120*pi
(3, 6, 6)
	 0.852802865422441
	 0 == -48*asin(sqrt(3)/sqrt(-g**2 + 4)) - 24*asin(1/sqrt(-g**2 + 4)) + 24*pi
(5, 5, 5)
	 sqrt(-2*sqrt(5)/3 + 2)
	 0 == -120*asin(2*sin(3*pi/10)/sqrt(-g**2 + 4)) + 40*pi
(4, 4, 4)
	 2*sqrt(3)/3
	 0 == -48*asin(sqrt(2)/sqrt(-g**2 + 4)) + 16*pi
(4, 6, 8)
	 0.431478810544531
	 0 == -96*asin(sqrt(2)/sqrt(-g**2 + 4)) - 96*asin(sqrt(3)/sqrt(-g**2 + 4)) - 96*asin(2*sin(3*pi/8)/sqrt(-g**2 + 4)) + 96*pi
(3, 8, 8)
	 0.562169275429639
	 0 == -96*asin(2*sin(3*pi/8)/sqrt(-g**2 + 4)) - 48*asin(1/sqrt(-g**2 + 4)) + 48*pi
(3, 4, 5, 4)
	 0.447837959589023
	 0 == -240*asin(sqrt(2)/sqrt(-g**2 + 4)) - 120*asin(2*sin(3*pi/10)/sqrt(-g**2 + 4)) - 120*asin(1/sqrt(-g**2 + 4)) + 120*pi
(3, 3, 3, 3, 4)
	 0.744206331156206
	 0 == -48*asin(sqrt(2)/sqrt(-g**2 + 4)) - 192*asin(1/sqrt(-g**2 + 4)) + 48*pi
(3, 5, 3, 5)
	 0.618033988749904
	 0 == -120*asin(2*sin(3*pi/10)/sqrt(-g**2 + 4)) - 120*asin(1/sqrt(-g**2 + 4)) + 60*pi
(5, 6, 6)
	 0.403548212335194
	 0 == -240*asin(sqrt(3)/sqrt(-g**2 + 4)) - 120*asin(2*sin(3*pi/10)/sqrt(-g**2 + 4)) + 120*pi
(3, 3, 3, 3)
	 sqrt(2)
	 0 == -48*asin(1/sqrt(-g**2 + 4)) + 12*pi
(4, 6, 10)
	 0.2629921750726
	 0 == -240*asin(sqrt(2)/sqrt(-g**2 + 4)) - 240*asin(sqrt(3)/sqrt(-g**2 + 4)) - 240*asin(2*sqrt(sqrt(5)/8 + 5/8)/sqrt(-g**2 + 4)) + 240*pi

'''

#print(help(pprint))
#sympy.mpmath.mp.dps = 100
#calc_g()


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



def asin_pi2coeffs(f, x):
    '''f = sum Ci asin(Ki/sqrt(4-x*x)) {i} + C*pi
f/-2/C + pi/2 = sum Ci/-2/C asin(Ki/(4-x*x)) {i}
return {Ki:Ci/-2/C for i}

'''
    w = symbols('__W', positive=True)
    f = f.subs((4-x*x), 1/w/w) # W=1/X=1/sqrt(4-gg); WW=1/(4-gg)
    f = sympify(f)
    d = f.as_coefficients_dict()
    C_pi = d[pi]
    f /= -2*C_pi
    f += pi/2
    #print(f)
    
    d = f.as_coefficients_dict()
    ls = []
    K = Wild('K')
    p = asin(K*w)
    for asin_t, c in d.items():
        m = p.matches(asin_t)
        assert m
        assert len(m) == 1
        
        ls.append((c, nsimplify(m[K])))

    d = dict((K,c) for c, K in ls)
    assert len(d) == len(ls)
    return d



var('g')
solid2zeroexpr = {}
solid2K2C = {}
for solid in [] or Archimedean_solid2info:
    f = solid2zero_expr(solid, g)
    #print(f)
    K2C = asin_pi2coeffs(f, g)
    #print('\t', cs)
    solid2zeroexpr[solid] = f
    solid2K2C[solid] = K2C

#pprint(solid2K2C)

solid2sorted_C_Ks = {}
for solid, K2C in solid2K2C.items():
    sorted_C_Ks = tuple(sorted((C,K) for K,C in K2C.items()))
    solid2sorted_C_Ks[solid] = sorted_C_Ks

sorted_Cs2solids = {}
for solid, sorted_C_Ks in solid2sorted_C_Ks.items():
    sorted_Cs = tuple(C for C,K in sorted_C_Ks)
    if sorted_Cs not in sorted_Cs2solids:
        sorted_Cs2solids[sorted_Cs] = []
    solids = sorted_Cs2solids[sorted_Cs]
    solids.append(solid)

#pprint(sorted_Cs2solids)
#pprint(sorted(sorted_Cs2solids))
[(1/2, 1/2, 1/2),
 (1/2, 1/2, 1),
 (1/2, 1),
 (1/2, 3/2),
 (1/2, 2),
 (1, 1),
 (3/2,),
 (2,),
 (5/2,)]


def fraction2N_negP(x):
    '''N*2**P -> (N,-P) where P<=0'''
    N, D = fraction(x)
    negP = int(D).bit_length() - one
    if not D == 2**negP:
        raise ValueError('x != N*2**P where P<=0')
    assert x == N/2**negP
    return N, negP

def sum_asin2one_asin(Cs, Ks, w):
    '''sum C[i] asin (K[i]*w) {i} = asin ALL'''

    assert len(Cs) == len(Ks)
    NnPs = list(map(fraction2N_negP, Cs))
    
    ALL = one-one # 1*asin ALL == 0
    C_ALL = (1,0) # 1/2**0 == 1
    for NnP, K in zip(NnPs, Ks):
        ALL = add_arcsin_with_coeffs(C_ALL, NnP, ALL, K*w)
    return ALL

    
    
def two_asin2no_asin(sorted_Cs):
    '''pi/2 == sum C[i] asin (K[i]*w) {i=0..1} = asin ALL
==>> ALL - 1 == 0
return ALL-1

where w = 1/sqrt(-g**2 + 4)'''
    
    assert len(sorted_Cs) == 2

    KsW = symbols('K0 K1 W', positive=True)
    K = KsW[:-1]
    W = KsW[-1]

    ALL = sum_asin2one_asin(sorted_Cs, K, W)
    zero_expr = ALL - 1

    return my_sympify(zero_expr)
    '''
# solid2sorted_C_Ks:
    ## (3, 3, 3, 3, 4): ((1/2, sqrt(2)), (2, 1)),
    Cs = (1/2, 2)
    pi/2 == 1/2 * asin(K0*W) + 2*asin(K1*W)
    y = add_arcsin_with_coeffs((1,1), (2,0), K0*W, K1*W) == 1
'''



var('K0 K1 K2 W X Y Z T XX YY ZZ TT WW U UU G GG', positive=True)

# sympy bug:
#    hash(2) != hash(Integer(2))
sorted_Cs2zero_expr_K0_K1_W = {
    (half, two): (GG**3*(-K0**2 + 16*K1**2) + GG**2*(12*K0**2 + 80*K1**4 - 192*K1**2) + GG*(-48*K0**2 + 128*K1**6 - 640*K1**4 + 768*K1**2) + 64*K0**2 + 64*K1**8 - 512*K1**6 + 1280*K1**4 - 1024*K1**2),
    }
solid2L_div_R = {
    (3,3,3,3,4): sqrt(-2*(42*sqrt(33) + 566)**(one/3)
                      - 128/(42*sqrt(33) + 566)**(one/3) + 44) / sqrt(21),
    }

def calc_zero_expr_K0_K1_W_of_Cs_half_2():
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


def solid2sorted_Cs_Kdict(solid):
    C_Ks = solid2sorted_C_Ks[solid]
    assert 1 <= len(C_Ks) <= 3
    
    sorted_Cs = tuple(c for c,k in C_Ks)
    ks = tuple(k for c,k in C_Ks)
    Ks = [K0, K1, K2]
    Kdict = dict(zip(Ks, ks))
    return sorted_Cs, Kdict
    
def solid2zero_GGexpr(solid):
    sorted_Cs, Kdict = solid2sorted_Cs_Kdict(solid)
    zero_expr = sorted_Cs2zero_expr_K0_K1_W[sorted_Cs]
    f = zero_expr.subs(Kdict)
    assert f.free_symbols == {GG}
    f = sympify(f)
    return f

def verify_G(solid, g):
    zeroexpr = solid2zeroexpr[solid]
    _g, = zeroexpr.free_symbols
    return 0 == nsimplify(zeroexpr.subs(_g, g))
    return
def calc_g33334():
    # solid2sorted_C_Ks:
    ## (3, 3, 3, 3, 4): ((1/2, sqrt(2)), (2, 1)),
    solid = (3, 3, 3, 3, 4)
    f = solid2zero_GGexpr(solid)
    f = factor(f)
    gg, = solve(f)
    g33334 = sqrt(gg)
    g33334 = nsimplify(g33334)
    _g33334 = sqrt(-2*(42*sqrt(33) + 566)**(one/3)
                   - 128/(42*sqrt(33) + 566)**(one/3) + 44) / sqrt(21)
    assert 0 == nsimplify(g33334 - _g33334)

    assert verify_G(solid, g33334)
    return g33334


def calc_g33335():
    # solid2sorted_C_Ks:
    ## (3, 3, 3, 3, 5): ((1/2, 1/2 + sqrt(5)/2), (2, 1)),
    # 0.463856880645439
    solid = (3, 3, 3, 3, 5)
    f = solid2zero_GGexpr(solid)
    ggs = solve(f)
##    print(ggs)
##    print(list(map(N, ggs)))
    gg, = ggs
    g33335 = nsimplify(sqrt(gg))
    _g33335 = sqrt(-(-(-188 + 12*sqrt(5))**3/(27*(-29 + sqrt(5))**3)
                     - (-192 + 64*sqrt(5))/(2*(-29 + sqrt(5)))
                     + sqrt((-(-188 + 12*sqrt(5))**2/(9*(-29 + sqrt(5))**2)
                             + (-368 + 48*sqrt(5))/(3*(-29 + sqrt(5))))**3
                            + (-2*(-188 + 12*sqrt(5))**3/(27*(-29 + sqrt(5))**3)
                               - (-192 + 64*sqrt(5))/(-29 + sqrt(5))
                               + (-368 + 48*sqrt(5))*(-188 + 12*sqrt(5))
                               /(3*(-29 + sqrt(5))**2))**2/4)
                     + (-368 + 48*sqrt(5))*(-188 + 12*sqrt(5))
                     /(6*(-29 + sqrt(5))**2))**(1/3)
                   + (-(-188 + 12*sqrt(5))**2/(9*(-29 + sqrt(5))**2)
                      + (-368 + 48*sqrt(5))/(3*(-29 + sqrt(5))))
                   /(-(-188 + 12*sqrt(5))**3/(27*(-29 + sqrt(5))**3)
                     - (-192 + 64*sqrt(5))/(2*(-29 + sqrt(5)))
                     + sqrt((-(-188 + 12*sqrt(5))**2/(9*(-29 + sqrt(5))**2)
                             + (-368 + 48*sqrt(5))/(3*(-29 + sqrt(5))))**3
                            + (-2*(-188 + 12*sqrt(5))**3/(27*(-29 + sqrt(5))**3)
                               - (-192 + 64*sqrt(5))/(-29 + sqrt(5))
                               + (-368 + 48*sqrt(5))*(-188 + 12*sqrt(5))
                               /(3*(-29 + sqrt(5))**2))**2/4)
                     + (-368 + 48*sqrt(5))*(-188 + 12*sqrt(5))
                     /(6*(-29 + sqrt(5))**2))**(1/3)
                   + (-188 + 12*sqrt(5))/(3*(-29 + sqrt(5))))
    assert verify_G(solid, g33335)


    # new form of g33335
    h = expand(f*(sqrt(5) + 29)/2)
    h = collect(h, GG)
    assert h == 209*GG**3 + GG**2*(-1348 + 40*sqrt(5)) + GG*(-256*sqrt(5) + 2608) - 1312 + 416*sqrt(5)
    A = 1881*sqrt(2)*sqrt(5760573 + 2813807*sqrt(5))
    B = (A + 2563547*sqrt(15) + 6192143*sqrt(3))
    D = 4**(one/3)*3**(one/6)/B**(one/3)
    _GG = 2*(-6/D - 71208*D + sqrt(5)*(-19752*D - 60) + 2022)/1881
    _g33335 = sqrt(_GG)
    assert 0 == nsimplify(g33335 - _g33335)


    # factor the below 'f' into h over QQ[sqrt(5)]
    # see below 'f'
    u = (209*GG**6 - 2696*GG**5 + 13872*GG**4 - 35776*GG**3 + 47104*GG**2 - 27648*GG + 4096)
    #assert factor(u,extension={sqrt(5)}) == 209*(GG**3 + GG**2*(-1348/209 - 40*sqrt(5)/209) + GG*(256*sqrt(5)/209 + 2608/209) - 1312/209 - 416*sqrt(5)/209)*(GG**3 + GG**2*(-1348/209 + 40*sqrt(5)/209) + GG*(-256*sqrt(5)/209 + 2608/209) - 1312/209 + 416*sqrt(5)/209)
    assert resultant(u,h) == 0 # so, they have a same root that is GG
    assert 0 == expand(gcd(u,h,extension=True)*209 - h)
    return _g33335

    
    _g = 0.463856880645439
    _gg = _g**2
    ef = lambda f, gg=_gg: N(f.subs(GG, gg))
    tf = lambda f: bool(abs(ef(f)) < 1e-7)
    assert tf(f)

    P = sqrt(5)
    f = expand(2*f)
    f = collect(f, P)
    A, B = seperate_term(f, P)
    assert f == A+B
    f = expand(A**2 - B**2)
    assert tf(f)
    
    print(f)
    f /= 4
    assert f == (209*GG**6 - 2696*GG**5 + 13872*GG**4 - 35776*GG**3 + 47104*GG**2 - 27648*GG + 4096)


    assert tf(f)
    ggs = solve(f)
    # sympy bug1:
    #   solve(f) ==>> [1.50152930508540, 2.97263618194513, 2.40355087229957, 2.97263618194513]
    #   NOTE: 2.97263618194513 appear twice but miss 0.21516320572211706
    # sympy bug2:
    #   root of f == 4*(root of h)?? since solve(f)=[4*RootOf(h)...]
    #   where h = 209*GG**6 - 674*GG**5 + 867*GG**4 - 559*GG**3 + 184*GG**2 - 27*GG + 1
    #   but solve(h) == [] !!!
    #   while GG:positive=True
    #   but var('x'), solve(h)==[6 roots (4 reals)] and two real roots be the same
    print('gg', [N((gg)) for gg in ggs])
    print('g', [N(sqrt(gg)) for gg in ggs])
    ggs = [gg for gg in ggs if (0 < N(gg) < 4)]
    print([ef(f,gg) for gg in ggs])
    ggs = [gg for gg in ggs if verify_G(solid, sqrt(gg))]
    print(ggs)
    raise
    g33335 = sqrt(gg)
    g33335 = nsimplify(g33335)
    #assert 0 == nsimplify(g33335 - _g33335)

    assert verify_G(solid, g33335)
    return g33335

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
    



    









    




    



























