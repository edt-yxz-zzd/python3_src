

'''
ASRP = Archimedean semi-regular polyhedra

L = length of edge
R = radius of outer circumscribed sphere of ASRP  // inner one may not exist
rc(n), Rc(n) = radii of circumscribed circle (inner and outer) of n-edge face of ASRP
H(n) = distance from the center of ASRP to the center of n-edge face of ASRP
    R**2 == H(n)**2 + Rc(n)**2
    Rc(n)**2 == (L/2)**2 + rc(n)**2

find g = L/R ??


'''


r'''
regular convex n-gons

relationship of R and L(n)
    r,R - radii of circumscribed circle (inner and outer)
    L(n) - length of edge of regular convex n-gons
    S(n) - area of regular convex n-gons


@Handbook.of.Mathematics::3 Geometry::3.1 Plane Geometry 
    ::3.1.5 Polygons in the Plane::3.1.5.2 Regular Convex Polygons::page137
    formulas of regular convex n-gons

::page139::Table3.2 Properties of some regular polygons
def r_x = sqrt(x)

shape=n \ unit  L(n)/R          S(n)/R**2           r/R
3               r_3             3/4*r_3             1/2
5               r_(10-2*r_5)/2  5/8*r_(10+2*r_5)    (1+r_5)/4
6               1               3/2*r_3             r_3/2
8               r_(2-r_2)       2*r_2               r_(2+r_2)/2
10              (r_5-1)/2       5/4*r_(10-2*r_5)    r_(10+2*r_5)/4



#'''


r'''
Archimedean semi-regular polyhedra

relationship of R and L ==========>>>>>>>> L/R = ???????
    R - radius of outer circumscribed sphere
    L - length of edge
    Area - total area
    Volume -
    
[Platonic Solids]:
    Area_per_face = Area/F
    Volume_per_face = Volume/F = Area_per_face*h/3
    ==>> h = 3*Volume/Area = 3*(Volume/L**3)/(Area/L**2)*L
    let Rc be radius of outer circumscribed circle of one face
    x = L/h = 1/(3*(Volume/L**3)/(Area/L**2)) = (Area/L**2)/(Volume/L**3)/3
    y = L/Rc = 1/(Rc/L)
    R**2 = Rc**2 + h**2 = (1/y**2+1/x**2)L**2
    L/R = 1/sqrt(1/y**2+1/x**2) = x*y/sqrt(y**2+x**2)
    
@Handbook.of.Mathematics::3 Geometry::3.3 Stereometry
    ::3.3.3 Polyeder or Polyhedron::11
 Regular Polyeder::page154
def r_x = sqrt(x)
shape\unit  Area/L**2           Volume/L**3     ==>> x              y               L/R
[3,3,3]     r_3                 r_2/12              2*r_6           r_3             2/3*r_6
[4,4,4]     6                   1                   2               r_2             2/3*r_3
[3,3,3,3]   2*r_3               r_2/3               r_6             r_3             r_2
[5,5,5]     3*sqrt(25+10*r_5)   15/4 + 7/4*r_5      r_(50-22*r_5)   r_(10-2*r_5)/2  (r_5-1)*r_3/3
[3,3,3,3,3] 5*r_3               5/4 + 5/12*r_5      r_3(3-r_5)      r_3             r_(50-10*r_5)/5

// 3*sqrt(25+10*r_5)/(15/4 + 7/4*r_5)/3
    = 4*sqrt(25+10*r_5)/(15 + 7*r_5) 
    = 4*sqrt(25+10*r_5)(15 - 7*r_5)/(225 - 49*5)
    = 4*sqrt(25+10*r_5)(7*r_5-15)/(50*5-225-5)
    = sqrt(25+10*r_5)(7*r_5-15)/5
    = sqrt(5+2*r_5)(7-3*r_5)
    = sqrt((5+2*r_5)(49-42*r_5+45))
    = sqrt((5+2*r_5)(94-42*r_5))
    = sqrt(470+188*r_5 - 210*r_5-420)
    = sqrt(50-22*r_5)
// 5*r_3/(5/4 + 5/12*r_5)/3
    = 5*r_3/(15/4 + 5/4*r_5)
    = 4*r_3/(3 + r_5)
    = 4*r_3(3 - r_5)/(9-5)
    = r_3(3-r_5)

// x=r_(50-22*r_5); y=r_(10-2*r_5)/2
    x**2 + y**2 = 50-22*r_5 + (5-r_5)/2
        = (100-44*r_5 + 5-r_5)/2
        = (105-45*r_5)/2
        = 15/2*(7-3*r_5)
        = 15/4*(14-2*3*r_5)
        = 15/4*(3-r_5)**2
    sqrt(x**2 + y**2) = sqrt(15/4*(3-r_5)**2)
        = (3-r_5)*r_15/2
    x*y = r_((50-22*r_5)(10-2*r_5))/2
        = r_(500-220*r_5 - 100*r_5+220)/2
        = r_(720-320*r_5)/2
        = r_(80(9-4*r_5))/2
        = 2*r_(5(9-4*r_5))
        = 2*r_(5(r_5-2)**2)
        = 2*r_5*(r_5-2)
        = 10-4*r_5
    x*y/sqrt(x**2 + y**2) = (10-4*r_5)/((3-r_5)*r_15/2)
        = (10-4*r_5)/(3-r_5)/r_15 *2
        = (10-4*r_5)(3+r_5)/(9-5)/r_15 *2
        = (5-2*r_5)(3+r_5)/r_15
        = (r_5-2)(3+r_5)/r_3
        = (3*r_5-6 + 5-2*r_5)/r_3
        = (r_5-1)/r_3
        = (r_5-1)*r_3/3
// x=r_3(3-r_5); y=r_3
    x=y*a
    x*y/sqrt(x**2 + y**2) = y*a*y/sqrt((y*a)**2 + y**2)
        = a*y/sqrt(a**2 + 1)
    a**2 = (3-r_5)**2 = 9+5-6*r_5 = 14-6*r_5
    sqrt(a**2 + 1) = sqrt(15-6*r_5) = r_3 * r_(5-2*r_5)
    x*y/sqrt(x**2 + y**2) = a*y/r_3 / r_(5-2*r_5)
        = a / r_(5-2*r_5)
        = (3-r_5) * r_(5-2*r_5) / (5-2*r_5)
        = r_(5-2*r_5)*(3-r_5)(5+2*r_5) / (25-20)
        = r_(5-2*r_5)*(15-5*r_5 + 6*r_5-10) / 5
        = r_(5-2*r_5)*(5+r_5) / 5
        = r_((5-2*r_5)*(5+r_5)**2) / 5
        = r_((5-2*r_5)*(25+10*r_5+5)) / 5
        = r_((5-2*r_5)*(3+r_5)*10) / 5
        = r_((15-6*r_5 + 5*r_5-10)*10) / 5
        = r_(10(5-r_5)) / 5
        = r_(50-10*r_5)/5

#'''


'''
spherical triangle
spherical polygon

g3454 = sqrt((44-16*sqrt(5))/41)
g366 = 2/11 * sqrt(22)
g3444 = sqrt((20-8*sqrt(2))/17)

@Handbook.of.Mathematics::3 Geometry::3.4 Spherical Trigonometry
    ::3.4.1.4 Spherical Triangle::page161
    see also::page170::Table3.9 First and second basic problems for spherical oblique triangles
    

area_spherical_triangle(a,b,c) = area of spherical triangle of unit sphere
    a,b,c - lengths of each arc; side angles;
        those are angles between two radius; side angles of the Trihedral Angle
        not Intersection Angles of two arcs
            which are angles between two faces of the Trihedral Angle
            call these alpha, beta, gamma; opposite angles;
    // R = 1
    0 < a+b+c < 2*pi
    a+b > c
    pi < alpha+beta+gamma < 3*pi
        spherical_excess = alpha+beta+gamma - pi
    alpha+beta < gamma+pi
    area_spherical_triangle(a,b,c) = spherical_excess * R**2  ---------------- 1
        = spherical_excess/(4*pi) * area_sphere
        = (alpha+beta+gamma - pi)* R**2
    so, we can define angle3D = spherical_excess!!!!
    L'Huilier Equations(3.201)::
        let ee = spherical_excess;
        let s = (a+b+c)/2
        (tan (ee/4))**2 = tan(s/2)tan((s-a)/2)tan((s-b)/2)tan((s-c)/2) ------- 2
area_spherical_polygon(n, L, R) = area of spherical polygon
    n - n-gon; number of edges of polygon
    L - length of chord of polygon
    R - radius of outer circumscribed sphere

    Rc = ?*L = L/(L(n)_by_R) # outer circle
    h**2 = R**2 - Rc**2


ee(n,alpha) = spherical_excess of n-spherical_polygon with angle alpha
    = n*alpha - (n-2)*pi
    
n-spherical_polygon:
    z = angle of n-gon = pi - 2*pi/n
    tri(ABO), tri(ACO)
    AO = BO = CO = R # radius of outer sphere
    AB = AC = L    # length of n-gon
    angle(BAC) = z # angle of n-gon
    calc alpha = angle(ABO, ACO)
    let H on OA and BH _L OA, so CH _L OA
    alpha = angle(BHC)
    BH = CH = area(tri(ABO))*2/R
    BC = 2*L*sin(z/2)
    sin(alpha/2) = BC/2/BH = L*sin(z/2)/(area(tri(ABO))*2/R)
        = sin(z/2)/2 * R*L/area(tri(ABO))

    s = (a+b+c)/2
    area(tri(a,b,c)) = sqrt(s(s-a)(s-b)(s-c))
        = sqrt(((b+c)**2-a**2)(a**2-(b-c)**2))/4
        = sqrt((2bc)**2-(bb+cc-aa)**2)/4
    let a,b,c = L,R,R, g=L/R
    R*L/area(tri(ABO)) = R*L/sqrt((2bb)**2-(2bb-aa)**2) *4
        = R*L/sqrt((2RR)**2-(2RR-LL)**2) *4
        = R*gR/sqrt((2RR)**2-(2RR-ggRR)**2) *4
        = 4g/sqrt(4-(2-gg)**2)
        = 4g/sqrt(4gg-(gg)**2)
        = 4/sqrt(4-gg)
    sin(alpha/2) = sin(z/2)/2 * 4/sqrt(4-gg)
        = 2*sin(z/2)/sqrt(4-gg) where g=L/R
        0<g<2
        only[3,3,3]/[4,4,4]/[3,3,3,3]/[3,4,3,4]==>>[g>=1]


    AA(n,g) = area(spherical_tri(n-gon) in unit sphere) = ee(n,alpha)
        = n*alpha - (n-2)*pi

    [given ASRP to calc g]:
        0 == 4*pi-sum(AA(n,g)*f for n, f in ASRP.shape2count.items()) ==>> g=??
        let X = sqrt(4-gg) ==>> 0<=X<=2
        the SUM contains items like Ki*arcsin(Ci/X)
        i.e. [3,6,6]:
            0 == -48*asin(sqrt(3)/sqrt(-g**2 + 4)) - 24*asin(1/sqrt(-g**2 + 4)) + 24*pi
            0 == -48*asin(sqrt(3)/X) - 24*asin(1/X) + 24*pi



    [calc arcsin+arcsin]:
        find y: arcsin(x)/2 = arcsin(y)
            let a = arcsin(x)
            [0<=a<=pi/2]:
                y = sin(a/2)
                x**2 = sin(a)**2 = 1-cos(a)**2
                cos(a) = 1-2*sin(a/2)**2 = 1-2yy
                cos(a)**2 = (1-2yy)**2 = 1-x**2
                1-2yy = sqrt(1-x**2)
                yy = (1-sqrt(1-x**2))/2
                y = sqrt(1-sqrt(1-x**2))/sqrt(2)
            i.e. [3,6,6]:
                0 == -48*asin(sqrt(3)/sqrt(-g**2 + 4)) - 24*asin(1/sqrt(-g**2 + 4)) + 24*pi
                pi/2 == asin(sqrt(3)/X) + asin(1/X)/2

                
                pi/2 == asin(K1/X) + asin(K2/X)/2
                    = asin(K1/X) + asin(sqrt(1-sqrt(1-(K2/X)**2))/sqrt(2))
                1 == (K1/X)**2 + (1-sqrt(1-(K2/X)**2))/2
                2 == 2(K1/X)**2 + 1-sqrt(1-(K2/X)**2)
                sqrt(1-(K2/X)**2) == 2(K1/X)**2 - 1
                1-(K2/X)**2 == 4(K1/X)**4 + 1 - 4(K1/X)**2
                0 == 4(K1/X)**4 - 4(K1/X)**2 + (K2/X)**2
                0 == 4*K1**4 - 4(K1*X)**2 + (K2*X)**2
                4(K1*X)**2 - (K2*X)**2 == 4*K1**4
                X**2 = 4*K1**4 / (4*K1**2 - K2**2)
                X = sqrt(4-gg) ==>> gg = 4-X**2
                [K1 = sqrt(3), K2 = 1]:
                    X**2 = 4*K1**4 / (4*K1**2 - K2**2)
                        = 4*9 / (4*3 - 1)
                        = 36 / 11
                    gg = 4-X**2 = 8/11
                    g366 = r_88/11 = 2/11 * sqrt(22)

        find y: arcsin(u) + arcsin(v) = arcsin(y)
            let a = arcsin(u); b = arcsin(v)
            [a>=0][b>=0][a+b<=pi/2]:
                y = sin(a+b) = sin(a)cos(b)+cos(a)sin(b)
                    = u cos(b) + cos(a) v
                    = u sqrt(1-vv) + sqrt(1-uu) v
            i.e. [3,4,4,4]:
                0 == -144*asin(sqrt(2)/sqrt(-g**2 + 4)) - 48*asin(1/sqrt(-g**2 + 4)) + 48*pi
                0 == -3*asin(sqrt(2)/X) - asin(1/X) + pi
                pi/2 == 3/2*asin(sqrt(2)/X) + asin(1/X)/2
                1 == (2*sqrt(1 - 2/X**2)*sqrt(-sqrt(1 - 2/X**2) + 1)*sqrt(sqrt(1 - 1/X**2) + 1) + sqrt(-sqrt(1 - 2/X**2) + 1)*sqrt(sqrt(1 - 1/X**2) + 1) + sqrt(-sqrt(1 - 1/X**2) + 1)*sqrt(sqrt(1 - 2/X**2) + 1 - 8*sqrt(1 - 2/X**2)/X**2))/2
                
                let Y = sqrt(1 - 2/X**2), Z = sqrt(1 - 1/X**2); 2*ZZ-YY=1; 2/XX=1-YY
                2 == ((2*Y+1)*sqrt(-Y + 1)*sqrt(Z + 1)
                      + sqrt(-Z + 1)*sqrt(Y + 1 - 8*Y/X**2))
                2*sqrt(-Z + 1) == ((2*Y+1)*sqrt(-Y + 1)*sqrt(1-Z**2)
                      + (-Z + 1)*sqrt(Y + 1 - 8*Y/X**2))
                    = ((2*Y+1)*sqrt(-Y + 1)*1/X
                      + (-Z + 1)*sqrt(Y + 1 - 8*Y/X**2))
                    = ((2*Y+1)*sqrt((-Y + 1)/X**2)
                      + (-Z + 1)*sqrt(Y + 1 - 8*Y/X**2))
                    = ((2*Y+1)*sqrt((-Y + 1)(1-YY)/2)
                      + (-Z + 1)*sqrt(Y + 1 - 8*Y(1-YY)/2))
                    = ((2*Y+1)*(1-Y)*sqrt(1+Y)/r_2
                      + (-Z + 1)*sqrt(1+Y)sqrt(1 - 4*Y(1-Y)))
                    = ((2*Y+1)*(1-Y)*sqrt(1+Y)/r_2
                      + (-Z + 1)*sqrt(1+Y)sqrt(1 - 4*Y+4*YY))
                    = ((2*Y+1)*(1-Y)*sqrt(1+Y)/r_2
                      + (-Z + 1)*sqrt(1+Y)abs(2Y-1))
                2*sqrt(1-Z)sqrt(1+Y) == ((2*Y+1)*(1-Y)*(1+Y)/r_2
                                         + (1-Z)*(1+Y)abs(2Y-1))
                    = ((2*Y+1)*(1-YY)/r_2 + (1-Z)*(1+Y)abs(2Y-1))
                4*(1-Z)(1+Y) == ((2*Y+1)*(1-YY)/r_2 + (1-Z)*(1+Y)abs(2Y-1))**2
                // if known g3444 < 1:
                    gg < 1; 4 > XX = 4-gg > 3;
                    1/4 < 1/XX < 1/3; 1/2 > YY=1-2/XX > 1/3;
                    1/2 = 1/r_4 < 1/r_3 < Y < 1/r_2 < 1
                    2Y-1>0
                0 == ((2*Y+1)*(1-Y*Y)/sqrt(2) + (1-Z)*(1+Y)*(2*Y-1))**2 - 4*(1-Z)*(1+Y)
                    = 2*Y**6 + Y**5*(-4*sqrt(2) + 2) + Y**4*(-8*sqrt(2) + 1)/2
                    + 5*sqrt(2)*Y**3 + Y**2*(-2 + 5*sqrt(2)) + Y*(-4 - sqrt(2))
                    - (5 + 2*sqrt(2))/2
                    + Z**2*(4*Y**4 + 4*Y**3 - 3*Y**2 - 2*Y + 1)
                    + Z*(4*sqrt(2)*Y**5 + Y**4*(-8 + 4*sqrt(2))
                         + Y**3*(-8 - 5*sqrt(2)) + Y**2*(-5*sqrt(2) + 6)
                         + Y*(sqrt(2) + 8) + sqrt(2) + 2)
                    
                    = fY0 + Z**2 * fY2 + Z*fY1
                    fY0 = (2*Y**6 + Y**5*(-4*sqrt(2) + 2) + Y**4*(-8*sqrt(2) + 1)/2
                           + 5*sqrt(2)*Y**3 + Y**2*(-2 + 5*sqrt(2)) + Y*(-4 - sqrt(2))
                           - (5 + 2*sqrt(2))/2)
                    fY2 = (4*Y**4 + 4*Y**3 - 3*Y**2 - 2*Y + 1)
                    fY1 = (4*sqrt(2)*Y**5 + Y**4*(-8 + 4*sqrt(2)) + Y**3*(-8 - 5*sqrt(2)) + Y**2*(-5*sqrt(2) + 6) + Y*(sqrt(2) + 8) + sqrt(2) + 2)
                ZZ = (1+YY)/2
                (fY0 + ZZ * fY2)**2 == (-Z*fY1)**2 = ZZ*fY1**2
                0 == (fY0 + ZZ * fY2)**2 - ZZ*fY1**2
                    = (32*Y**10
                       + 64*Y**9 + Y**8*(-48 - 8*sqrt(2))
                       + Y**7*(-160 - 16*sqrt(2)) + Y**6*(-13 + 10*sqrt(2))
                       + Y**5*(36*sqrt(2) + 134) + Y**4*(6*sqrt(2) + 45)
                       + Y**3*(-44 - 24*sqrt(2)) + Y**2*(-19 - 10*sqrt(2))
                       + Y*(4*sqrt(2) + 6) + 2*sqrt(2) + 3)
                    = (32*YY**5
                       + 64*Y*YY**4 + YY**4*(-48 - 8*sqrt(2))
                       + Y*YY**3*(-160 - 16*sqrt(2)) + YY**3*(-13 + 10*sqrt(2))
                       + Y*YY**2*(36*sqrt(2) + 134) + YY**2*(6*sqrt(2) + 45)
                       + Y*YY**1*(-44 - 24*sqrt(2)) + YY**1*(-19 - 10*sqrt(2))
                       + Y*(4*sqrt(2) + 6) + 2*sqrt(2) + 3)
                    = Y*Yodd + Yeven
                    Yodd = (64*YY**4 + YY**3*(-160 - 16*sqrt(2)) + YY**2*(36*sqrt(2) + 134) + YY*(-44 - 24*sqrt(2)) + 4*sqrt(2) + 6)
                    Yeven = (32*YY**5 + YY**4*(-48 - 8*sqrt(2)) + YY**3*(-13 + 10*sqrt(2)) + YY**2*(6*sqrt(2) + 45) + YY*(-19 - 10*sqrt(2)) + 2*sqrt(2) + 3)
                Yeven**2 == (-Y*Yodd)**2 = YY*Yodd**2
                0 == Yeven**2 - YY*Yodd**2
                    = 1024*YY**10 + YY**9*(-7168 - 512*sqrt(2)) + YY**8*(3456*sqrt(2) + 22080) + YY**7*(-39456 - 10096*sqrt(2)) + YY**6*(16684*sqrt(2) + 45457) + YY**5*(-35526 - 17112*sqrt(2)) + YY**4*(11252*sqrt(2) + 19263) + YY**3*(-7220 - 4736*sqrt(2)) + YY**2*(1236*sqrt(2) + 1791) + YY*(-262 - 184*sqrt(2)) + 12*sqrt(2) + 17
                    = fYz + sqrt(2)*fYr
                    fYz = (1024*YY**10 - 7168*YY**9 + 22080*YY**8 - 39456*YY**7 + 45457*YY**6 - 35526*YY**5 + 19263*YY**4 - 7220*YY**3 + 1791*YY**2 - 262*YY + 17)
                    fYr = (-512*YY**9 + 3456*YY**8 - 10096*YY**7 + 16684*YY**6 - 17112*YY**5 + 11252*YY**4 - 4736*YY**3 + 1236*YY**2 - 184*YY + 12)

                0 == fYz**2 - 2*fYr**2
                    = (YY - 1)**12*(32*YY**2 - 16*YY + 1)**4
                [XX<4]==>>[2/XX>1/2]==>>[YY=1-2/XX<1/2]==>>[YY!=1]
                0 == 32*YY**2 - 16*YY + 1
                [YY = 1-2/XX = 1-2/(4-gg)]==>> 0==17*gg**2 - 40*gg + 16
                g3444 = sqrt((20-8*sqrt(2))/17)

            i.e. [3,4,5,4]:
                0 == -240*asin(sqrt(2)/sqrt(-g**2 + 4)) - 120*asin(2*sin(3*pi/10)/sqrt(-g**2 + 4)) - 120*asin(1/sqrt(-g**2 + 4)) + 120*pi
                pi/2 == asin(sqrt(2)/X) + asin(2*sin(3*pi/10)/X)/2 + asin(1/X)/2
                let Y = sqrt(1 - 2/X**2), Z = sqrt(1 - 1/X**2);
                let T = sqrt(1 - 4*sin(3*pi/10)**2/X**2)
                    4*sin(3*pi/10)**2 = (sqrt(5)+3)/2 = ((sqrt(5)+1)/2)**2
                    let t = (sqrt(5)+1)/2
                    TT = 1 - tt/XX; 1-tt=-t; tt=1+t
                1 == (X*sqrt(1 - 2/X**2)*sqrt(-sqrt(1 - 1/X**2) + 1)*sqrt(sqrt(1 - 4*sin(3*pi/10)**2/X**2) + 1)/2 + X*sqrt(1 - 2/X**2)*sqrt(sqrt(1 - 1/X**2) + 1)*sqrt(-sqrt(1 - 4*sin(3*pi/10)**2/X**2) + 1)/2 + sqrt(sqrt(1 - 1/X**2)*sqrt(1 - 4*sin(3*pi/10)**2/X**2) - sqrt(-sqrt(1 - 1/X**2) + 1)*sqrt(sqrt(1 - 1/X**2) + 1)*sqrt(-sqrt(1 - 4*sin(3*pi/10)**2/X**2) + 1)*sqrt(sqrt(1 - 4*sin(3*pi/10)**2/X**2) + 1) + 1))/X
                    # var('Y'); f.subs(sqrt(1 - 2/X**2), Y)
                    = (X*Y*sqrt(-T + 1)*sqrt(Z + 1)/2 + X*Y*sqrt(T + 1)*sqrt(-Z + 1)/2 + sqrt(T*Z - sqrt(-T + 1)*sqrt(T + 1)*sqrt(-Z + 1)*sqrt(Z + 1) + 1))/X

                1/XX = 1-ZZ;
                YY = 1-2/XX=1-2(1-ZZ)=2*ZZ-1;
                TT = 1 - tt(1-ZZ) = tt*ZZ-t
                2*X == X*Y*sqrt(1-T)*sqrt(1+Z) + X*Y*sqrt(1+T)*sqrt(1-Z)
                        + 2*sqrt(T*Z - sqrt(1-T)*sqrt(1+T)*sqrt(1-Z)*sqrt(1+Z) + 1)
                    = X*Y*sqrt(1-T)*sqrt(1+Z) + X*Y*sqrt(1+T)*sqrt(1-Z)
                        + 2*sqrt(T*Z - sqrt(1-TT)*sqrt(1-ZZ) + 1)
                sqrt(1-TT)*sqrt(1-ZZ) = sqrt(tt(1-ZZ))*sqrt(1-ZZ) = t*(1-ZZ)
                2*X*sqrt(1-T)*sqrt(1+Z) == X*Y*(1-T)*(1+Z)
                        + X*Y*sqrt(1-TT)*sqrt(1-ZZ)
                        + 2*sqrt( (T*Z - sqrt(1-TT)*sqrt(1-ZZ) + 1)*(1-T)*(1+Z) )
                    = X*Y*(1-T)*(1+Z) + X*Y*t*(1-ZZ)
                        + 2*sqrt( (T*Z - t*(1-ZZ) + 1)*(1-T)*(1+Z) )
                2*sqrt(1-T)*sqrt(1+Z) == Y*( (1-T)*(1+Z) + t*(1-ZZ) )
                        + 2*sqrt( (T*Z - t*(1-ZZ) + 1)*(1-T)*(1+Z)/XX )
                    = Y*( (1-T)*(1+Z) + t*(1-ZZ) )
                        + 2*sqrt( (T*Z - t*(1-ZZ) + 1)*(1-T)*(1+Z)(1-ZZ) )
                    = Y*( (1-T) + t*(1-Z) ) *(1+Z)
                        + 2*sqrt( (T*Z - t*(1-ZZ) + 1)*(1-T)*(1-Z) ) *(1+Z)
                2*sqrt(1-T) == Y*( (1-T) + t*(1-Z) ) *sqrt(1+Z)
                        + 2*sqrt( (T*Z - t*(1-ZZ) + 1)*(1-T)*(1-Z) ) *sqrt(1+Z)
                0 == (2*sqrt(1-T) - Y*( (1-T) + t*(1-Z) ) *sqrt(1+Z))**2 
                        - 4*( (T*Z - t*(1-ZZ) + 1)*(1-T)*(1-Z) ) *(1+Z)
                    = frr*sqrt(1-T)*sqrt(1+Z) + fzz
                    frr = 4*Y*(T + Z*t - t - 1)
                    fzz = (T**2*(Y**2*Z + Y**2 - 4*Z**3 + 4*Z)
                       + T*(2*Y**2*Z**2*t - 2*Y**2*Z - 2*Y**2*t - 2*Y**2 + 4*Z**3 - 4*Z**2*ZZ*t + 4*Z**2*t - 4*Z**2 - 4*Z + 4*ZZ*t - 4*t)
                       + Y**2*(Z**3*t**2 - Z**2*t**2 - 2*Z**2*t - Z*t**2 + Z + t**2 + 2*t + 1)
                       + 4*Z**2*ZZ*t - 4*Z**2*t + 4*Z**2 - 4*ZZ*t + 4*t)
                0 == (frr*sqrt(1-T)*sqrt(1+Z))**2 - fzz**2
                    # YY=2*ZZ-1; TT=tt*ZZ-t; tt=t+1; ZZ=Z*Z
                    = T*(-48*Z**5*t - 40*Z**5 + 80*Z**4*t + 144*Z**4 + 72*Z**3*t + 8*Z**3 - 136*Z**2*t - 208*Z**2 - 24*Z*t + 16*Z + 56*t + 80)
                    + (- 152*Z**6*t - 112*Z**6 + 96*Z**5*t + 80*Z**5 + 312*Z**4*t + 140*Z**4 - 160*Z**3*t - 80*Z**3 - 200*Z**2*t - 32*Z**2 + 64*Z*t + 16*Z + 40*t - 12)
                    = ff
                ff = even_square_sub_odd_square(ff, T, t*t*Z*Z-t)
                ff = collect_square_recur(ff, t, t+1)
                    = 40960*Z**12*t + 25600*Z**12 - 224256*Z**10*t - 140032*Z**10 + 509696*Z**8*t + 317968*Z**8 - 615424*Z**6*t - 383552*Z**6 + 416256*Z**4*t + 259168*Z**4 - 149504*Z**2*t - 92992*Z**2 + 22272*t + 13840
                    = 46080*Z**12 - 252160*Z**10 + 572816*Z**8 - 691264*Z**6 + 467296*Z**4 - 167744*Z**2 + 24976
                    + sqrt(5)*(20480*Z**12 - 112128*Z**10 + 254848*Z**8 - 307712*Z**6 + 208128*Z**4 - 74752*Z**2 + 11136)
                ff = even_square_sub_odd_square(ff.subs(sqrt(5), r_5), r_5)
                    = 256*(Z - 1)**8*(Z + 1)**8*(320*Z**4 - 400*Z**2 + 121)**2
                ZZ = 1-1/XX < 1-1/4 < 1
                    0 == 320*Z**4 - 400*Z**2 + 121
                ZZ = 1-1/XX = 1-1/(4-gg)
                    0 == 41*gg**2 - 88*gg + 16
                g3454 < 1
                    gg = -16*sqrt(5)/41 + 44/41
                    g3454 = sqrt((44-16*sqrt(5))/41)
                
                    


                
        [4-gon: a,b,c,d with diagonal x,y][tri (a,b,x), (b,c,y), (c,d,x), (d,a,y)]:
            find f: y = f(a,b,c,d,x)
                area(tri(b,c,y)) = sqrt((2bc)**2-(bb+cc-yy)**2)/4
                S = area(tri(b,c,y)) + area(tri(d,a,y)) = area(tri(a,b,x)) + area(tri(c,d,x))
                (4S)**2 = ((2bc)**2-(bb+cc-yy)**2) + ((2da)**2-(dd+aa-yy)**2)
                        + 2*sqrt(((2bc)**2-(bb+cc-yy)**2)((2da)**2-(dd+aa-yy)**2))
                0 == -256*S**4 + 32*S**2*a**4 - 64*S**2*a**2*d**2 - 64*S**2*a**2*y**2 - 32*S**2*b**4 + 64*S**2*b**2*c**2 + 64*S**2*b**2*y**2 - 32*S**2*c**4 + 64*S**2*c**2*y**2 + 32*S**2*d**4 - 64*S**2*d**2*y**2 - a**8 + 4*a**6*d**2 + 4*a**6*y**2 + 6*a**4*b**4 - 12*a**4*b**2*c**2 - 12*a**4*b**2*y**2 + 6*a**4*c**4 - 12*a**4*c**2*y**2 - 6*a**4*d**4 - 4*a**4*d**2*y**2 - 12*a**2*b**4*d**2 - 12*a**2*b**4*y**2 + 24*a**2*b**2*c**2*d**2 + 24*a**2*b**2*c**2*y**2 + 24*a**2*b**2*d**2*y**2 + 24*a**2*b**2*y**4 - 12*a**2*c**4*d**2 - 12*a**2*c**4*y**2 + 24*a**2*c**2*d**2*y**2 + 24*a**2*c**2*y**4 + 4*a**2*d**6 - 4*a**2*d**4*y**2 - 16*a**2*d**2*y**4 - 8*a**2*y**6 - b**8 + 4*b**6*c**2 + 4*b**6*y**2 - 6*b**4*c**4 - 4*b**4*c**2*y**2 + 6*b**4*d**4 - 12*b**4*d**2*y**2 + 4*b**2*c**6 - 4*b**2*c**4*y**2 - 12*b**2*c**2*d**4 + 24*b**2*c**2*d**2*y**2 - 16*b**2*c**2*y**4 - 12*b**2*d**4*y**2 + 24*b**2*d**2*y**4 - 8*b**2*y**6 - c**8 + 4*c**6*y**2 + 6*c**4*d**4 - 12*c**4*d**2*y**2 - 12*c**2*d**4*y**2 + 24*c**2*d**2*y**4 - 8*c**2*y**6 - d**8 + 4*d**6*y**2 - 8*d**2*y**6 + 4*y**8
                y**8 + c6 y**6 + c4 y**4 + c2 y**2 + c0 == 0
            
            

[Platonic Solids]:
    let t = num_faces_per_vtx; for [3,3,3,3], t=4
    alpha = angle of n-spherical_polygon = 2*pi/t
    4*pi == F*ee(n,alpha) = F*(n*2*pi/t - (n-2)*pi)
        4/F == (2/t - 1)n + 2
        for [3,3,3,3]: F=8; n=3; t=4

        high dim:
            G(m,n) = n-mD-gon = n:[n-(m-1)D-gon]*num_faces_per_vtx
                n=F=num_faces
                m is dim
            num_faces_per_vtx = num_edges in the face that cut out one vtx
                face of dim m-1
                edge of dim m-2
            n-0D-gons = {1:one-point}???
            n-1D-gons = {2:[the 0D-gon]*0} ????
            n-2D-gons = {n:[G(1,2)]*2 for n>=3}
            n-3D-gons = {4:[G(2,3)]*3, 6:[G(2,4)]*3, 8:[G(2,3)]*4,
                         12:[G(2,5)]*3, 20:[G(2,3)]*5}

#'''





