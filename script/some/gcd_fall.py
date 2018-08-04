



'''
def ffx degree step z

ffx d s z = II z-s*k {~k=0->d}
    = II z-s*k {k=0..d-1}/II z-s*k {k=d..-1}
ffx(d,s,z)/s**d = II z/s-k {~k=0->d}
    = fall(z/s,d)
ffx(d,s,z) = s**d fall(z/s,d)

gcd(ffx(d,s,z), ffx(d,s,z-r)) = 1 for mod s: r =!= 0
find g,h, s.t.
    g(z)ffx(d,s,z) - h(z)ffx(d,s,z-r) = 1
    degree(g) < d

'''



# ff = sympy.functions.combinatorial.factorials.FallingFactorial
# rf = RisingFactorial
from sympy import Sum, ff, rf, roots, binomial as C, \
     symbols, factor, factorial, Product, floor, gcd_terms, gcdex,\
     LC, degree, primitive, Poly, fraction




from sympy.abc import k, n, z, j, i
a, b, d, k, n = symbols('a b d k n', positive=True, integer=True)

def ffx(degree, step, z):
    return step**degree * ff(z/step, degree)

def find_gh(d, s, r, z):
    f0 = ffx(d,s,z)
    fr = f0.subs(z, z-r)
    g, _h, one = gcdex(f0, fr)
    h = - _h
    assert one == 1
    
    if not g.is_number:
        assert LC(g) > 0
        assert LC(h) > 0
    else:
        assert g > 0
    
    return g, h

#g, h = find_gh(3, 2, 1, z)

def int_cs_gh(d,s,r):
    g, h = find_gh(d, s, r, z)
    g = gcd_terms(g)
    h = gcd_terms(h)
    
    return g,h


def to_coeffs_and_gcd(poly):
    g = poly
    if g.is_number:
        g_gcd, g_primitive = g, 1
        g_coeffs = [1]
    else:
        g_gcd, g_primitive = primitive(g)
        #g_coeffs = coeffs(gp)
        g_coeffs = Poly(g_primitive).coeffs()
    return g_coeffs, g_gcd

def to_coeffs_and_denominator(poly):
    g = poly
    g_coeffs, g_gcd = to_coeffs_and_gcd(g)
    g_numerator, g_denominator = fraction(g_gcd)
    assert g_gcd > 0
    assert g_numerator == 1

    r = (g_coeffs, g_denominator)
    return r

def to_str(g):
    g_coeffs, g_denominator = to_coeffs_and_denominator(g)
    return '{}/{}'.format(g_coeffs, g_denominator)
    

for s in range(2, 5):
    for r in range(1, s):
        for d in range(1, 6):
            g, h = find_gh(d,s,r,z)
            print('d={d};s={s};r={r}; g={g}; h={h};'
                  .format(d=d, s=s, r=r, g=to_str(g), h=to_str(h)))
    print()


''' 
d=1;s=2;r=1; g=[1]/1; h=[1]/1;
d=2;s=2;r=1; g=[2, -5]/3; h=[2, -1]/3;
d=3;s=2;r=1; g=[2, -13, 16]/15; h=[2, -7, 1]/15;
d=4;s=2;r=1; g=[4, -50, 176, -151]/315; h=[4, -34, 64, -3]/315;
d=5;s=2;r=1; g=[2, -41, 280, -712, 498]/2835; h=[2, -31, 145, -197, 3]/2835;

d=1;s=3;r=1; g=[1]/1; h=[1]/1;
d=2;s=3;r=1; g=[1, -3]/4; h=[1, -1]/4;
d=3;s=3;r=1; g=[6, -51, 73]/280; h=[6, -33, 10]/280;
d=4;s=3;r=1; g=[1, -17, 78, -76]/1120; h=[1, -13, 38, -4]/1120;
d=5;s=3;r=1; g=[14, -399, 3708, -12261, 9666]/640640; h=[14, -329, 2343, -4886, 176]/640640;
d=1;s=3;r=2; g=[1]/2; h=[1]/2;
d=2;s=3;r=2; g=[2, -9]/10; h=[2, -1]/10;
d=3;s=3;r=2; g=[3, -33, 74]/160; h=[3, -15, 2]/160;
d=4;s=3;r=2; g=[10, -205, 1221, -1922]/12320; h=[10, -125, 341, -14]/12320;
d=5;s=3;r=2; g=[1, -33, 369, -1587, 2034]/49280; h=[1, -23, 159, -317, 4]/49280;

d=1;s=4;r=1; g=[1]/1; h=[1]/1;
d=2;s=4;r=1; g=[2, -7]/15; h=[2, -3]/15;
d=3;s=4;r=1; g=[2, -21, 34]/315; h=[2, -15, 7]/315;
d=4;s=4;r=1; g=[20, -430, 2428, -2603]/135135; h=[20, -350, 1388, -231]/135135;
d=5;s=4;r=1; g=[14, -511, 6004, -24356, 20838]/6891885; h=[14, -441, 4219, -11871, 693]/6891885;
d=1;s=4;r=2; g=[1]/2; h=[1]/2;
d=2;s=4;r=2; g=[1, -5]/12; h=[1, -1]/12;
d=3;s=4;r=2; g=[1, -13, 32]/240; h=[1, -7, 2]/240;
d=4;s=4;r=2; g=[1, -25, 176, -302]/10080; h=[1, -17, 64, -6]/10080;
d=5;s=4;r=2; g=[1, -41, 560, -2848, 3984]/725760; h=[1, -31, 290, -788, 24]/725760;
d=1;s=4;r=3; g=[1]/3; h=[1]/3;
d=2;s=4;r=3; g=[2, -13]/21; h=[2, -1]/21;
d=3;s=4;r=3; g=[6, -93, 302]/1155; h=[6, -39, 5]/1155;
d=4;s=4;r=3; g=[4, -114, 956, -2181]/31185; h=[4, -66, 236, -9]/31185;
d=5;s=4;r=3; g=[14, -637, 9892, -59852, 110982]/7702695; h=[14, -427, 3907, -10277, 117]/7702695;


'''

            
            
    















