

'''
Archimedean solid ::= Archimedean semi-regular polyhedra (ASRP)
    convex
    each face is a regular polygon
    each vertex is arounded by same polygon sequence
    notation ::= seq of number of edges of polygon
    i.e. ASRP[3,3,3]; ASRP[3,4,5,4]

problems:
    how many? which?
    faces and graph?
    L/R? get one coordinate configure?




@The Math Book.djvu::Platonic Solids::page50
    tetrahedron [3, 3, 3]
    cube [4, 4, 4]
    octahedron [3, 3, 3, 3]
    dodecahedron [5, 5, 5]
    icosahedron [3, 3, 3, 3, 3]
    total: 5

@The Math Book.djvu::Archimedean Semi-Regular Polyhedra::page64
    3,4,3,4     (a cuboctahedron);
    3,5,3,5     (an icosidodecahedron);
    3,6,6       (a truncated tetrahedron);          # [3, 3, 3]
    4,6,6       (a truncated octahedron);           # [3, 3, 3, 3]
    3,8,8       (a truncated cube);                 # [4, 4, 4]
    5,6,6       (a truncated icosahedron, or soccer ball); # [3, 3, 3, 3, 3]
    3,10,10     (a truncated dodecahedron);         # [5, 5, 5]
    3,4,4,4     (a rhombicuboctahedron);
    4,6,8       (a truncated cuboctahedron);        # [3,4,3,4]
    3,4,5,4     (a rhombicosidodecahedron);
    4,6,10      (a truncated icosidodecahedron);    # [3,5,3,5]
    3,3,3,3,4   (a snub cube, or snub cuboctahedron);
    3,3,3,3,5   (a snub dodecahedron, or snub icosidodecahedron).
    total: 13
    total(Platonic Solids + Archimedean Solids) = 5+13 = 18

#'''
'''
basic requirement:
    ASRP[a[0],...,a[t-1]]
    (1) t >= 3
    (2) a[i] >= 3
    (3) [odd a[i]] ==>>
        [a[i+1 mod t] == a[i-1 mod t]]
        or [exist j: [j!=i][a[j]=a[i]]
                [{a[j-1],a[j+1]}!={a[i-1],a[i+1]}]
                [Card({a[j-1],a[j+1]}/\{a[i-1],a[i+1]})=1]
            ]
    def angle(n) = (n*pi-2*pi)/n = pi - pi*2/n
    def angle_ASRP(a) = sum angle(a[i]) {i=0..t-1}
    (4) 2*pi > angle_ASRP(a)
    angle(a[i]) < angle_ASRP(a) - angle(a[i])
        ==>> angle(a[i]) < angle_ASRP(a)/2
        ==>> angle(max(a)) < angle_ASRP(a)/2
    [a[i] >= 3] ==>> [angle(a[i])>=angle(3)=pi/3]
        ==>> [angle_ASRP(a) >= t*angle(3) = t*pi/3]
        [2*pi > angle_ASRP(a)] ==>> [2*pi > t*pi/3] ==>> [t < 6]
    [ASRP[3]*6 is plane] ==>> [t<6]
    (1') 3 <= t < 6
    
    let b = sorted(a)
    // find upper bound of b[0] = min(a)
    2*pi > angle_ASRP(a) >= sum angle(b[0]) {i=0..t-1} = (pi - pi*2/b[0])t
        ==>> b[0] < 2/(1 - 2/t) = 2*t/(t-2)
        ==>> t=3..5, b[0]<=5|3|3
    (5) t=3..5, b[0]<=5|3|3

    // find upper bound of b[-1] = max(a)
    angle(b[-1]) = pi - pi*2 / b[-1]
        < angle_ASRP(a) - angle(b[-1])
        = (t-1)*pi - pi*2 * sum 1/b[i] {i=0..t-2}
        < 2*pi - angle(b[-1]) = pi + pi*2 / b[-1]
        ==>> 1 / b[-1] > -(t-2)/2 + sum 1/b[i] {i=0..t-2} > -1 / b[-1]
        ==>> abs(sum 1/b[i] {i=0..t-2} - (t-2)/2) < 1/b[-1]
        let f = sum 1/b[i] {i=0..t-2} - (t-2)/2
        (6) abs(f) < 1/b[-1]
        
        [t=3]:
            b[0] <= 5
            [t=3][odd a[i]] ==>> [a[i+1 mod t] == a[i-1 mod t]]
            
            2/b[-1] - 1/2 <= f <= 1/6
            f = 1/b[0] + 1/b[1] - 1/2
            [b[-1]->inf]:
                // s.t. abs(f)<1/b[-1]
                [b = [3,6,b[-1]]] ==>> f=0 
                [b = [4,4,b[-1]]] ==>> f=0 // yeah!!!!!!!!!!!!!!
            but [b[0]=3] ==>> [odd b[0]] ==>> [b[1]=b[2]][even b[1] or b[1]=3]
            [b=[3]*3]:pass
            [w>=2][b=[3,2*w,2*w]]
                f = 1/3 + 1/2/w - 1/2 = 1/2/w - 1/6
                [abs(f)<1/b[-1] = 1/2/w] ==>> -1/2/w < 1/2/w - 1/6 < 1/2/w
                    ==>> 1/6 < 1/w ==>> w < 6 ==>> b[-1] = 2*w <= 10
            [b=[4,4,>=4]]:pass
            [b[0]=4][b[1]>=5]
                #f <= 1/4 + 1/5 - 1/2 = -1/20 # invalid // if b[1]==5 ==>> b=[5,5,5]
                [even b[1]]
                f <= 1/4 + 1/6 - 1/2 = -1/12
                1/b[-1] > abs(f) >= 1/12 ==>> b[-1] < 12 ==>> b[-1] <= 10
                b = [4,2*w, 2*v] for [w>=3]
                f <= 1/4 + 1/2/w - 1/2 = 1/2/w - 1/4 < 0
                1/b[-1] > abs(f) >= 1/4 - 1/2/w
                2*v = b[-1] < 1/(1/4 - 1/2/w) = 4*w/(w-2) <= 4*3/(3-2) = 12
                w <= v < 2*w/(w-2) <= 2*3/(3-2) = 6
                w < 4 ==>> w = 3
                b=[4,6, 2*v] for [v=3..5]
            [b=[5]*3]:pass
            [w>=3][b=[5,2*w,2*w]]:
                f = 1/5 + 1/2/w - 1/2 = 1/2/w - 3/10
                -1/2/w < f < 1/2/w ==>> 3/10 < 1/w ==>> w < 10/3 ==>> w=3
                ==>> b[-1] = 6
                b=[5,6,6]

        [t=4]:
            b[0] = 3
            [t=4][odd a[i]] ==>>
                [a[i+1 mod t] == a[i-1 mod t]]
                or [a[i-1]!=a[i+1]]([s=1]or[s=-1])[a[i]=a[i+s]][{a[i-s],a[i+2s]}={a[i-s],a[i+s]} or {a[i],a[i+2s]}]
                    // == [a[i-1]!=a[i+1]]([s=1]or[s=-1])[a[i]=a[i+s]]([a[i+2s]=a[i+s]] or [a[i-s]=a[i]])
                    // ==>> b= [v,u,u,u] or [u,u,u,v] where [u!=v]
            b=[3,u,u,v] or [3,u,v,v]
            
            [3<=u<=v][b=[3,u,u,v]]:
                f = 1/3 + 1/u + 1/u - 1 = 2/u - 2/3 <= 0
                [u=3]:
                    f = 0
                    b=[3,3,3,v] for [v>=3]
                [u>=4]:
                    f <= 2/4 - 2/3 = -1/6
                    -1/v < f < 1/v ==>> 1/v > 1/6 ==>> b[-1] = v < 6
                    [4<=u<=v<6] ==>> [4<=u<=5]
                    b = [3,u,u,v] for [4<=u<=v<=5]
                    b = [3,4,4,4] or [3,4,4,5] or [3,5,5,5]
            [3<=u<v][b=[3,u,v,v]]:
                f = 1/3 + 1/u + 1/v - 1 = 1/u+1/v - 2/3 <= 0
                -1/v < f < 1/v ==>> 2/3-1/u < 2/v
                    ==>> b[-1] = v < 2/(2/3-1/u) = 6*u / (2*u-3) <= 6
                [3<=u<=v<6*u/(2*u-3)] ==>> [3<=u<9/2]
                    ==>> u=3..4 ==>> v<=5|4
                [u<v] ==>> u = 3
                b=[3,3,v,v] for [v=4..5]
                b=[3,3,4,4] or [3,3,5,5]

        [t=5]:
            b[0] = 3
            [plane ASRP[3,3,3,4,4], ASRP[3,3,3,3,6]]
            b=[3,3,3,3,v] for [v=3..5]
            
                

        ------------------
        b=[3]*3
        b=[3,2*w,2*w] for [w=2..5]
        b=[4,4,w] for [w>=4]
        b=[4,6, 2*v] for [v=3..5]
        b=[5]*3
        b=[5,6,6]
        b=[3,3,3,v] for [v>=3]
            a = b
        b=[3,u,u,v] for [4<=u<=v<=5]
            a = [3,u,v,u]
        b=[3,3,v,v] for [v=4..5]
            a = [3,v,3,v]
        b=[3,3,3,3,v] for [v=3..5]
            a = b
        total: 1 + 4 + inf + 3 + 1 + 1 + inf + 3 + 2 + 3 = 18 + 2*inf
        // [3,5,5,5] is not
        
((3, 3, 3),
 # no 3,4,4, but it is
 (3, 6, 6),
 (3, 8, 8),
 (3, 10, 10),
 (4, 4, 4), # (4,4,v) family
 # no 4,4,>=5, but they are
 (4, 6, 6),
 (4, 6, 8),
 (4, 6, 10),
 (5, 5, 5),
 (5, 6, 6),
 (3, 3, 3, 3), # (3, 3, 3, v) family
 # no 3,3,3,>=4, but they are
 (3, 4, 3, 4),
 (3, 4, 4, 4),
 (3, 4, 5, 4),
 (3, 5, 3, 5),
 # no 3,5,5,5??, yeah, it is not; see below
 (3, 3, 3, 3, 3),
 (3, 3, 3, 3, 4),
 (3, 3, 3, 3, 5),)

another requirement:
    V = num_vertices
    F = num_faces
    E = num_edges
    c = shape2count_per_vtx = num_one_face_edges2num_faces_per_vtx
        = {shape: a.count(shape) for shape in set(a)}
    let S = sum 1/a[i] {i=0..t-1}
    (1) F_(shape) = num_faces_of_shape = c.get(shape, 0)/shape *V
    (2) F = sum F_(s) {s in c} = S*V
    (3) E = len(a)/2 *V = t/2 *V
    (4) 2 = V+F-E = (1+S-t/2)*V
        V = 2/(1+S-t/2)
    (5) [NN F_(s)>=2 for s in c][NN V,F,E][V>=4][F>=4][E>=6]
    test:
        ASRP[3,5,5,5]:
            S = 1/3+3/5; t=4
            V = 2/(1+S-t/2) = 2/(1+1/3+3/5-2) < 0
            fail
        [v>=3] ASRP[4,4,v]:
            S = 1/v+1/2; t=3
            V = 2/(1+S-t/2) = 2/(1+1/v+1/2-3/2) = 2*v >= 6 >= 4
            F_(4) = 2/4 *V = v >= 3 >= 2
            F_(v) = 1/v *V = 2 >= 2
            F = F_(4) + F_(v) >= 5 >= 4
            E = t/2*V = 3*v >= 9 >= 6
            pass
        [v>=3] ASRP[3,3,3,v]:
            S = 1/v+1; t=4
            V = 2/(1+S-t/2) = 2/(1+1/v+1-4/2) = 2*v >= 6 >= 4
            F_(3) = 3/3 *V = 2*v >= 6 >= 2
            F_(v) = 1/v *V = 2 >= 2
            F = F_(4) + F_(v) >= 8 >= 4
            E = t/2*V = 4*v >= 12 >= 6
            pass
            
            
    
'''


'''
relationship of R and L(n)
    r,R - radii of circumscribed circle (outer and inner)
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


'''
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
    ::3.3.3 Polyeder or Polyhedron::11 Regular Polyeder::page154
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
    
@Handbook.of.Mathematics::3 Geometry::3.4 Spherical Trigonometry
    ::3.4.1.4 Spherical Triangle::page161
    see also::page170::Table3.9 First and second basic problems for spherical oblique triangles
    
spherical triangle
spherical polygon

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


    AA(n,g) = area(spherical_tri(n-gon) in unit sphere) = ee(n,alpha)
        = n*alpha - (n-2)*pi

    [given ASRP to calc g]:
        0 == 4*pi-sum(AA(n,g)*f for n, f in ASRP.shape2count.items()) ==>> g=??

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


'''
draw:
    (3, 3, 3):
        # from outside into center: clockwise:0->1->2->0
        faces = [(0,1,2), (0,2,3), (0,3,1), (1,3,2)]
        
        xyz_tmp = [(0,0,2*sqrt(2)), (-2,0,0), (1,sqrt(3),0), (1,-sqrt(3),0), ]
        O = (0,0,c)
        r = 2*sqrt(2) - c
        r = sqrt(c*c+4)
        r*r = c*c+4 = 8 + c*c - 4*sqrt(2)c
        c = 1/sqrt(2) = sqrt(2)/2
        r = sqrt(2)*3/2
        sqrt(2)*[(0,0,2*sqrt(2)-c), (-2,0,-c), (1,sqrt(3),-c), (1,-sqrt(3),-c), ]
        xyz = [(0,0,3), (-2sqrt(2),0,-1), (sqrt(2),sqrt(6),-1), (sqrt(2),-sqrt(6),-1), ]
    (5,5,5):
        faces = [(0,1,2,3,4), (0,5,11,6,1), (1,6,12,7,2),
                 (2,7,13,8,3), (3,8,14,9,4), (0,4,9,10,5),
                 (5,10,15,16,11), (6,11,16,17,12), (7,12,17,18,13),
                 (8,13,18,19,14), (9,14,19,15,10), (15,19,18,17,16),
                 ]
        

    (3, 6, 6):
        # truncated_tetrahedron
        # truncated_[3,3,3]
        faces = [(0,1,2), (3,4,5), (6,7,8), (9,10,11),
                 (0,3,5,7,6,1), (1,6,8,10,9,2), (0,2,9,11,4,3), (4,11,10,8,7,5)]
    (3, 8, 8):
        # truncated_cube
        # truncated_[4,4,4]
        faces = [(0,1,2), (3,4,5), (6,7,8), (9,10,11),
                 (12,13,14), (15,16,17), (18,19,20), (21,22,23),
                 (0,2,12,14,22,21,5,4), (0,4,3,7,6,10,9,1), (3,5,21,23,19,18,8,7), 
                 (6,8,18,20,16,15,11,10), (1,9,11,15,17,13,12,2), (13,17,16,20,19,23,22,14)]

    (3, 10, 10):
        # truncated_dodecahedron
        # truncated_[5, 5, 5]
        faces = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11),
                 (12, 13, 14), (15, 16, 17), (18, 19, 20), (21, 22, 23),
                 (24, 25, 26), (27, 28, 29), (30, 31, 32), (33, 34, 35),
                 (36, 37, 38), (39, 40, 41), (42, 43, 44), (45, 46, 47),
                 (48, 49, 50), (51, 52, 53), (54, 55, 56), (57, 58, 59),
                 (1,5,4,8,7,  11,10,14,13,2,), (0,15,17,35,34,  19,18,3,5,1,),
                 (4,3,18,20,38,  37,22,21,6,8,), (6,21,23,41,40,  25,24,9,11,7,),
                 (9,24,26,44,43,  28,27,12,14,10,), (0,2,13,12,27,  29,32,31,16,15,),
                 
                 (16,31,30,45,47,  49,48,33,35,17,), (19,34,33,48,50,  52,51,36,38,20,),
                 (22,37,36,51,53,  55,54,39,41,23,), (25,40,39,54,56,  58,57,42,44,26,),
                 (28,43,42,57,59,  46,45,30,32,29,), (46,59,58,56,55,  53,52,50,49,47,),
                 ]
    (4, 4, >=3), # (4,4,v) family
    (4, 6, 6),
    (4, 6, 8),
    (4, 6, 10),
    (5, 5, 5),
    (5, 6, 6),
    (3, 3, 3, >=3), # (3, 3, 3, v) family
    (3, 4, 3, 4),
    (3, 4, 4, 4),
    (3, 4, 5, 4),
    (3, 5, 3, 5),
    (3, 3, 3, 3, 3),
    (3, 3, 3, 3, 4),
    (3, 3, 3, 3, 5),)
#'''


from pprint import pprint
from fractions import Fraction as __fr
from itertools import groupby
from nn_ns.graph.planar_embedding import polyhedra_embedding2faces, \
     truncated_polyhedra, polyhedra_faces2embedding, snub3_polyhedra, \
     mid_truncated_polyhedra
from nn_ns.graph.show_v2neighbors import show_v2neighbors


one = __fr(1)



def show_faces(faces):
    embedding = polyhedra_faces2embedding(faces)
    show_v2neighbors(embedding)


init_try = False
if init_try:
    from sympy.combinatorics.polyhedron import *


    ['Basic', 'FiniteSet', 'Perm', 'PermutationGroup', 'Polyhedron', 'Tuple',
    '__builtins__', '__doc__', '__file__', '__loader__', '__name__',
    '__package__', 'as_int', 'cube', 'cube_faces', 'dodecahedron',
    'dodecahedron_faces', 'flatten', 'icosahedron', 'icosahedron_faces',
    'minlex', 'octahedron', 'octahedron_faces', 'rmul', 'tetrahedron',
    'tetrahedron_faces', 'unflatten']


    platonic_solids = [tetrahedron, cube, octahedron, dodecahedron, icosahedron]
    platonic_solid_names = 'tetrahedron, cube, octahedron, dodecahedron, icosahedron'.split(', ')


    #print(dir(cube))
    ['corners', 'count', 'count_ops',
    'cyclic_form', 'edges',
    'faces', 'pgroup', 'rotate', 'size', 'vertices']


    def show_platonic_solids():
        for solid, name in zip(platonic_solids, platonic_solid_names):
            vtc = solid.vertices
            faces = solid.faces
            some_a_face = next(iter(faces))
            ne_per_face = len(some_a_face)
            nf_per_vtx = sum(0 in face for face in faces)
            print(name, [ne_per_face]*nf_per_vtx)

    show_platonic_solids()



name2solid = {
    'tetrahedron' : [3, 3, 3],
    'cube' : [4, 4, 4],
    'octahedron' : [3, 3, 3, 3],
    'dodecahedron' : [5, 5, 5],
    'icosahedron' : [3, 3, 3, 3, 3],

    'cuboctahedron' : [3,4,3,4],
    'icosidodecahedron' : [3,5,3,5],
    'truncated_tetrahedron' : [3,6,6],
    'truncated_octahedron' : [4,6,6],
    'truncated_cube' : [3,8,8],
    'truncated_icosahedron' : [5,6,6],
    'truncated_dodecahedron' : [3,10,10],
    'rhombicuboctahedron' : [3,4,4,4],
    'truncated_cuboctahedron' : [4,6,8],
    'rhombicosidodecahedron' : [3,4,5,4],
    'truncated_icosidodecahedron' : [4,6,10],
    'snub_cube' : [3,3,3,3,4],
    'snub_dodecahedron' : [3,3,3,3,5],
    }

assert len(name2solid) == 18
for key, v in name2solid.items():
    name2solid[key] = tuple(v)

solid2name = dict(map(reversed, name2solid.items()))
solids = tuple(sorted(sorted(solid2name), key=len))

'''
pprint(solids)
((3, 3, 3),
 (3, 6, 6),
 (3, 8, 8),
 (3, 10, 10),
 (4, 4, 4),
 (4, 6, 6),
 (4, 6, 8),
 (4, 6, 10),
 (5, 5, 5),
 (5, 6, 6),
 (3, 3, 3, 3),
 (3, 4, 3, 4),
 (3, 4, 4, 4),
 (3, 4, 5, 4),
 (3, 5, 3, 5),
 (3, 3, 3, 3, 3),
 (3, 3, 3, 3, 4),
 (3, 3, 3, 3, 5))
#'''


def test_another_requirement(ASRP):
    a = ASRP
    t = len(a)
    if not 6 > t >= 3:
        return False
    if not all(shape >= 3 for shape in a):
        return False
    ASRP = a = tuple(a)
    a = tuple(map(int, a))
    assert ASRP == a
    ASRP = a

    
    c = shape2count_per_vtx = {shape: a.count(shape) for shape in set(a)}
    is_int = lambda x: x.denominator == 1
    to_int = lambda x: x.numerator
    
    S = sum(one/x for x in a)
    V = 2/(1+S-one*t/2)
    E = V*t/2
    F = S*V
    if not all(map(is_int, [V,E,F])):
        return False
    if not (V >= 4 and E>=6 and F>=4):
        return False
    assert V+F-E == 2

    shape2count = {}
    for shape, count_per_vtx in c.items():
        F_shape = V*count_per_vtx/shape
        shape2count[shape] = F_shape
    if not all(is_int(F_) and F_ >= 2 for F_ in shape2count.values()):
        return False
    
    assert F == sum(shape2count.values())
    V=to_int(V)
    E=to_int(E)
    F=to_int(F)
    for shape, count in shape2count.items():
        shape2count[shape] = int(count)
    return dict(ASRP=ASRP, S=S, V=V, E=E, F=F,
                shape2count=shape2count,
                shape2count_per_vtx=shape2count_per_vtx,)

assert all(map(test_another_requirement, solids))
assert not test_another_requirement([3,5,5,5])
    
def get_info(ASRP):
    r = test_another_requirement(ASRP)
    if not r:
        return None
    return r


def get_infos(solids, solid2name):
    for solid in solids:
        info = get_info(solid)
        info['name'] = solid2name[solid]
        yield info
    return

Archimedean_solid2info = {info['ASRP']: info
                          for info in get_infos(solids, solid2name)}

'''
#list(map(pprint, map(get_info, solids)))
pprint(list(get_infos(solids, solid2name)))

[{'ASRP': (3, 3, 3),
  'E': 6,
  'F': 4,
  'S': Fraction(1, 1),
  'V': 4,
  'name': 'tetrahedron',
  'shape2count': {3: 4},
  'shape2count_per_vtx': {3: 3}},
 {'ASRP': (3, 6, 6),
  'E': 18,
  'F': 8,
  'S': Fraction(2, 3),
  'V': 12,
  'name': 'truncated_tetrahedron',
  'shape2count': {3: 4, 6: 4},
  'shape2count_per_vtx': {3: 1, 6: 2}},
 {'ASRP': (3, 8, 8),
  'E': 36,
  'F': 14,
  'S': Fraction(7, 12),
  'V': 24,
  'name': 'truncated_cube',
  'shape2count': {3: 8, 8: 6},
  'shape2count_per_vtx': {3: 1, 8: 2}},
 {'ASRP': (3, 10, 10),
  'E': 90,
  'F': 32,
  'S': Fraction(8, 15),
  'V': 60,
  'name': 'truncated_dodecahedron',
  'shape2count': {3: 20, 10: 12},
  'shape2count_per_vtx': {3: 1, 10: 2}},
 {'ASRP': (4, 4, 4),
  'E': 12,
  'F': 6,
  'S': Fraction(3, 4),
  'V': 8,
  'name': 'cube',
  'shape2count': {4: 6},
  'shape2count_per_vtx': {4: 3}},
 {'ASRP': (4, 6, 6),
  'E': 36,
  'F': 14,
  'S': Fraction(7, 12),
  'V': 24,
  'name': 'truncated_octahedron',
  'shape2count': {4: 6, 6: 8},
  'shape2count_per_vtx': {4: 1, 6: 2}},
 {'ASRP': (4, 6, 8),
  'E': 72,
  'F': 26,
  'S': Fraction(13, 24),
  'V': 48,
  'name': 'truncated_cuboctahedron',
  'shape2count': {4: 12, 6: 8, 8: 6},
  'shape2count_per_vtx': {4: 1, 6: 1, 8: 1}},
 {'ASRP': (4, 6, 10),
  'E': 180,
  'F': 62,
  'S': Fraction(31, 60),
  'V': 120,
  'name': 'truncated_icosidodecahedron',
  'shape2count': {4: 30, 6: 20, 10: 12},
  'shape2count_per_vtx': {4: 1, 6: 1, 10: 1}},
 {'ASRP': (5, 5, 5),
  'E': 30,
  'F': 12,
  'S': Fraction(3, 5),
  'V': 20,
  'name': 'dodecahedron',
  'shape2count': {5: 12},
  'shape2count_per_vtx': {5: 3}},
 {'ASRP': (5, 6, 6),
  'E': 90,
  'F': 32,
  'S': Fraction(8, 15),
  'V': 60,
  'name': 'truncated_icosahedron',
  'shape2count': {5: 12, 6: 20},
  'shape2count_per_vtx': {5: 1, 6: 2}},
 {'ASRP': (3, 3, 3, 3),
  'E': 12,
  'F': 8,
  'S': Fraction(4, 3),
  'V': 6,
  'name': 'octahedron',
  'shape2count': {3: 8},
  'shape2count_per_vtx': {3: 4}},
 {'ASRP': (3, 4, 3, 4),
  'E': 24,
  'F': 14,
  'S': Fraction(7, 6),
  'V': 12,
  'name': 'cuboctahedron',
  'shape2count': {3: 8, 4: 6},
  'shape2count_per_vtx': {3: 2, 4: 2}},
 {'ASRP': (3, 4, 4, 4),
  'E': 48,
  'F': 26,
  'S': Fraction(13, 12),
  'V': 24,
  'name': 'rhombicuboctahedron',
  'shape2count': {3: 8, 4: 18},
  'shape2count_per_vtx': {3: 1, 4: 3}},
 {'ASRP': (3, 4, 5, 4),
  'E': 120,
  'F': 62,
  'S': Fraction(31, 30),
  'V': 60,
  'name': 'rhombicosidodecahedron',
  'shape2count': {3: 20, 4: 30, 5: 12},
  'shape2count_per_vtx': {3: 1, 4: 2, 5: 1}},
 {'ASRP': (3, 5, 3, 5),
  'E': 60,
  'F': 32,
  'S': Fraction(16, 15),
  'V': 30,
  'name': 'icosidodecahedron',
  'shape2count': {3: 20, 5: 12},
  'shape2count_per_vtx': {3: 2, 5: 2}},
 {'ASRP': (3, 3, 3, 3, 3),
  'E': 30,
  'F': 20,
  'S': Fraction(5, 3),
  'V': 12,
  'name': 'icosahedron',
  'shape2count': {3: 20},
  'shape2count_per_vtx': {3: 5}},
 {'ASRP': (3, 3, 3, 3, 4),
  'E': 60,
  'F': 38,
  'S': Fraction(19, 12),
  'V': 24,
  'name': 'snub_cube',
  'shape2count': {3: 32, 4: 6},
  'shape2count_per_vtx': {3: 4, 4: 1}},
 {'ASRP': (3, 3, 3, 3, 5),
  'E': 150,
  'F': 92,
  'S': Fraction(23, 15),
  'V': 60,
  'name': 'snub_dodecahedron',
  'shape2count': {3: 80, 5: 12},
  'shape2count_per_vtx': {3: 4, 5: 1}}]
#'''


def minimal_ASRP(ASRP):
    a = tuple(ASRP)
    b = tuple(reversed(a))
    return min(_minimal_ASRP(a), _minimal_ASRP(b))
def _minimal_ASRP(a):
    a0 = min(a)
    count = a.count(a0)
    idc = [i for i in range(len(a)) if a[i] == a0]
    return min(a[i:]+a[:i] for i in idc)


def check_faces(solid, faces):
    solid = minimal_ASRP(solid)
    
    info = get_info(solid)
    F = len(faces)
    E2 = sum(map(len, faces))
    V = max(map(max, faces)) + 1
    
    assert F == info['F']
    assert E2 == info['E']*2
    assert V == info['V']
    E = E2//2

    shape2count = info['shape2count']
    shape2count_per_vtx = info['shape2count_per_vtx']
    shapes = list(map(len, faces))
    for shape, count in shape2count.items():
        assert count == shapes.count(shape)
    for v in range(V):
        faces_around_v = [face for face in faces if v in face]
        shapes_around_v = list(map(len, faces_around_v))
        for shape, count in shape2count_per_vtx.items():
            assert count == shapes_around_v.count(shape)


    assert all(len(set(face)) == len(face) for face in faces)
    
    def face2dedges(face):
        f = list(face) + [face[0]]
        return zip(f[:-1], f[1:])
    dedges = []
    dedge2face_idx = {}
    for i, face in enumerate(faces):
        new = list(face2dedges(face))
        dedges.extend(new)
        dedge2face_idx.update((d,i) for d in new)
            
    assert len(dedges) == E2 == len(dedge2face_idx)
    dedges = set(dedges) # once per dedge
    assert len(dedges) == E2
    assert {(v,u) for u,v in dedges} == dedges # (u,v) and (v,u)
    assert all(u!=v for u,v in dedges)

    v2vus = dict((k,tuple(ls)) for k,ls in groupby(sorted(dedges), lambda vu: vu[0]))
    assert len(v2vus) == V
    assert set(v2vus) == set(range(V))
    for v, vus in v2vus.items():
        face_idc_around_v = [i for i, face in enumerate(faces) if v in face]
        face_idx2next_idx = {dedge2face_idx[(u,v)]:dedge2face_idx[(v,u)] for v,u in vus}

        if not len(face_idx2next_idx) == len(face_idc_around_v):
            print(face_idc_around_v)
            print(face_idx2next_idx)
            print(faces)
            print(solid)
            print(v, vus)
        assert len(face_idx2next_idx) == len(face_idc_around_v)
        assert set(face_idx2next_idx) == set(face_idx2next_idx.values()) \
               == set(face_idc_around_v)
        f_idx = face_idc_around_v[0]
        face_idc_clockwise = []
        for _ in range(len(solid)):
            face_idc_clockwise.append(f_idx)
            f_idx = face_idx2next_idx[f_idx]

        shape_clockwise = map(len, (faces[i] for i in face_idc_clockwise))
        min_shape_seq = minimal_ASRP(shape_clockwise)
        assert min_shape_seq == solid
        
    return




def calc_faces_44v(v):
    '''[4,4,v] for v>=3 # [3,4,4]'''

    assert v >= 3
    face0 = tuple(range(0, 2*v, 2))
    face1 = tuple(range(2*v-1, 0, -2))
    face1 = face1[-1:] + face1[:-1]
    faces = [face0, face1]
    for i in face0:
        face = (i, i+1, i+3, i+2)
        faces.append(face)

    face = faces[-1]
    face = tuple(x % (2*v) for x in face)
    face = face[-1:] + face[:-1]
    faces[-1] = face
    
    assert faces[-1] == (0, 2*v-2, 2*v-1, 1)
    assert all(4 == len(face) for face in faces[2:])
    assert all(v == len(face) for face in faces[:2])
    assert all(face[0] == min(face) and len(set(face)) == len(face)
               for face in faces)
    assert len(faces) == 2+v
    
    return faces
    

def calc_faces_333v(v):
    '''[3,3,3,v] for v>=3 '''

    assert v >= 3
    face0 = tuple(range(0, 2*v, 2))
    face1 = tuple(range(2*v-1, 0, -2))
    face1 = face1[-1:] + face1[:-1]
    faces = [face0, face1]
    for i in face0:
        face2 = (i, i+1, i+2)
        face3 = (i+1, i+3, i+2)
        faces.append(face2)
        faces.append(face3)


    assert faces[-2] == (2*v-2, 2*v-1, 2*v)
    assert faces[-1] == (2*v-1, 2*v+1, 2*v)
    faces[-2] = (0, 2*v-2, 2*v-1)
    faces[-1] = (0, 2*v-1, 1)
    
    assert all(3 == len(face) for face in faces[2:])
    assert all(v == len(face) for face in faces[:2])
    assert all(face[0] == min(face) and len(set(face)) == len(face)
               for face in faces)
    assert len(faces) == 2+2*v
    
    return faces
    

solid2faces = {
    (3, 3, 3): [(0,1,2), (0,2,3), (0,3,1), (1,3,2)],
    (5, 5, 5): [(0,1,2,3,4), (0,5,11,6,1), (1,6,12,7,2),
                 (2,7,13,8,3), (3,8,14,9,4), (0,4,9,10,5),
                 (5,10,15,16,11), (6,11,16,17,12), (7,12,17,18,13),
                 (8,13,18,19,14), (9,14,19,15,10), (15,19,18,17,16),
                 ],
    }

solid2faces[(3,3,3,3)] = calc_faces_333v(3)
solid2faces[(4,4,4)] = calc_faces_44v(4)


faces2embedding = polyhedra_faces2embedding
embedding2faces = lambda embedding: sorted(map(tuple,
                                polyhedra_embedding2faces(embedding)))
transform_faces = lambda transform, faces: embedding2faces(transform(faces2embedding(faces)))

snub3 = lambda faces: transform_faces(snub3_polyhedra, faces)
solid2faces[(3,3,3,3,3)] = snub3(solid2faces[(3,3,3)])
solid2faces[(3,3,3,3,4)] = snub3(solid2faces[(4,4,4)])
solid2faces[(3,3,3,3,5)] = snub3(solid2faces[(5,5,5)])


mid_truncated = lambda faces: transform_faces(mid_truncated_polyhedra, faces)
solid2faces[(3,4,3,4)] = mid_truncated(solid2faces[(4,4,4)])
solid2faces[(3,5,3,5)] = mid_truncated(solid2faces[(5,5,5)])
solid2faces[(3,4,4,4)] = mid_truncated(solid2faces[(3,4,3,4)])
solid2faces[(3,4,5,4)] = mid_truncated(solid2faces[(3,5,3,5)])


truncated = lambda faces: transform_faces(truncated_polyhedra, faces)
solid2faces[(3,6,6)] = truncated(solid2faces[(3,3,3)])
solid2faces[(4,6,6)] = truncated(solid2faces[(3,3,3,3)])
solid2faces[(3,8,8)] = truncated(solid2faces[(4,4,4)])
solid2faces[(5,6,6)] = truncated(solid2faces[(3,3,3,3,3)])
solid2faces[(3,10,10)] = truncated(solid2faces[(5,5,5)])
solid2faces[(4,6,8)] = truncated(solid2faces[(3,4,3,4)])
solid2faces[(4,6,10)] = truncated(solid2faces[(3,5,3,5)])

assert len(solid2faces) == 18






_tmp = {
    (3, 6, 6): [(0,1,2), (3,4,5), (6,7,8), (9,10,11),
                (0,3,5,7,6,1), (1,6,8,10,9,2), (0,2,9,11,4,3), (4,11,10,8,7,5)],
    (3, 8, 8): [(0,1,2), (3,4,5), (6,7,8), (9,10,11),
                 (12,13,14), (15,16,17), (18,19,20), (21,22,23),
                 (0,2,12,14,22,21,5,4), (0,4,3,7,6,10,9,1), (3,5,21,23,19,18,8,7), 
                 (6,8,18,20,16,15,11,10), (1,9,11,15,17,13,12,2), (13,17,16,20,19,23,22,14)],
    (3,10,10): [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11),
                 (12, 13, 14), (15, 16, 17), (18, 19, 20), (21, 22, 23),
                 (24, 25, 26), (27, 28, 29), (30, 31, 32), (33, 34, 35),
                 (36, 37, 38), (39, 40, 41), (42, 43, 44), (45, 46, 47),
                 (48, 49, 50), (51, 52, 53), (54, 55, 56), (57, 58, 59),
                 (1,5,4,8,7,  11,10,14,13,2,), (0,15,17,35,34,  19,18,3,5,1,),
                 (4,3,18,20,38,  37,22,21,6,8,), (6,21,23,41,40,  25,24,9,11,7,),
                 (9,24,26,44,43,  28,27,12,14,10,), (0,2,13,12,27,  29,32,31,16,15,),
                 
                 (16,31,30,45,47,  49,48,33,35,17,), (19,34,33,48,50,  52,51,36,38,20,),
                 (22,37,36,51,53,  55,54,39,41,23,), (25,40,39,54,56,  58,57,42,44,26,),
                 (28,43,42,57,59,  46,45,30,32,29,), (46,59,58,56,55,  53,52,50,49,47,),
                 ],
    }
for solid, faces in solid2faces.items():
    try:
        check_faces(solid, faces)
        #print('checed:', solid)
    except:
        print(solid, faces)
        raise

def check_transform_faces(faces, ans, transform):
    embedding = polyhedra_faces2embedding(faces)
    new_embedding = transform(embedding)
    new_faces = polyhedra_embedding2faces(new_embedding)
    new_faces = sorted(map(tuple, new_faces))
    ans = sorted(map(tuple, ans))
    assert ans == new_faces
    return new_faces
##faces = solid2faces[(3,3,3)]
##ans = solid2faces[(3,6,6)]
##check_transform_faces(faces, ans, truncated_polyhedra)


for solid, faces in solid2faces.items():
    show_faces(faces)













































