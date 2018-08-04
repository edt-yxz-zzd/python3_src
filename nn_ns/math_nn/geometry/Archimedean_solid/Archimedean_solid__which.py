

from fractions import Fraction
import copy
from numbers import Integral, Rational

__all__ = tuple('name2solid, solid2name, solids, solid_list, solid_set'
                ', name2Archimedean_solid, Archimedean_solid2name'
                ', Archimedean_solids, Archimedean_solid_list'
                ', Archimedean_solid_set'
                ', Archimedean_solid2info'
                ', test_another_requirement, get_Archimedean_solid_info'
                .split(', '))

one = Fraction(1)

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

===============================================================
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
for _key, _v in name2solid.items():
    name2solid[_key] = tuple(_v)

solid2name = dict(map(reversed, name2solid.items()))

solids = solid_list = tuple(sorted(sorted(solid2name), key=len))
solid_set = frozenset(solid_list)


name2Archimedean_solid = name2solid
Archimedean_solid2name = solid2name
Archimedean_solids = solids
Archimedean_solid_list = solid_list
Archimedean_solid_set = solid_set

assert solids == \
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




############################################################
############################################################
############################################################
############################################################
#####################  get_info  ###########################
############################################################
############################################################
############################################################
############################################################


## NOTE: test_another_requirement is used in get_info
def __sympy_simp(x):
    r = hasattr(x, 'is_integer')
    if r:
        x = x.simplify().ratsimp()
    return r, x
    
def is_int(x):
    if isinstance(x, Integral):
        return True
    r, x = __sympy_simp(x)
    if r:
        return x.is_integer
    if isinstance(x, Rational):
        return x.denominator == 1
    return False
def to_int(x):
    assert is_int(x)
    if isinstance(x, Integral):
        return int(x)
    r, x = __sympy_simp(x)
    if r:
        return x # may contains free symbols
    if isinstance(x, Rational):
        return x.numerator
    raise logic-error

def test_another_requirement(ASRP):
    
    #print('test_another_requirement', ASRP)
    a = ASRP
    t = len(a)
    if not 6 > t >= 3:
        return False
    if not all(shape >= 3 for shape in a):
        return False
    ASRP = a = tuple(a)
    assert all(isinstance(x, Integral) or x.is_integer for x in a)
    #a = tuple(map(int, a))
    #assert ASRP == a
    ASRP = a


    c = shape2count_per_vtx = {shape: a.count(shape) for shape in set(a)}
    #is_int = lambda x: x.denominator == 1
    #to_int = lambda x: x.numerator
    
    S = sum(one/x for x in a)
    V = 2/(1+S-one*t/2)
    E = V*t/2
    F = S*V
    if not all(map(is_int, [V,E,F])):
        return False
    V=one*to_int(V)
    E=one*to_int(E)
    F=one*to_int(F)
    
    if not (V >= 4 and E>=6 and F>=4):
        return False
    
    assert to_int(V+F-E) == 2
    

    shape2count = {}
    for shape, count_per_vtx in c.items():
        F_shape = V*count_per_vtx/shape
        shape2count[shape] = F_shape
    if not all(is_int(F_) and F_ >= 2 for F_ in shape2count.values()):
        return False

    _F = one*to_int(sum(shape2count.values()))
    assert F == _F
    V=to_int(V)
    E=to_int(E)
    F=to_int(F)
    for shape, count in shape2count.items():
        shape2count[shape] = to_int(count)
    return dict(ASRP=ASRP, S=S, V=V, E=E, F=F,
                shape2count=shape2count,
                shape2count_per_vtx=shape2count_per_vtx,)

assert all(map(test_another_requirement, solids))
assert not test_another_requirement([3,5,5,5])





## NOTE: get_Archimedean_solid_info is useful for [4,4,v] and [3,3,3,v]
##       which solid2info cannot offer

def get_Archimedean_solid_info(ASRP):
    r = test_another_requirement(ASRP)
    if not r:
        return None
    return r



def __get_infos(solids, solid2name):
    for solid in solids:
        info = get_Archimedean_solid_info(solid)
        info['name'] = solid2name[solid]
        yield info
    return

Archimedean_solid2info = {info['ASRP']: info
                          for info in __get_infos(solids, solid2name)}


assert Archimedean_solid2info == {
 (3, 3, 3): {'ASRP': (3, 3, 3),
             'E': 6,
             'F': 4,
             'S': Fraction(1, 1),
             'V': 4,
             'name': 'tetrahedron',
             'shape2count': {3: 4},
             'shape2count_per_vtx': {3: 3}},
 (3, 3, 3, 3): {'ASRP': (3, 3, 3, 3),
                'E': 12,
                'F': 8,
                'S': Fraction(4, 3),
                'V': 6,
                'name': 'octahedron',
                'shape2count': {3: 8},
                'shape2count_per_vtx': {3: 4}},
 (3, 3, 3, 3, 3): {'ASRP': (3, 3, 3, 3, 3),
                   'E': 30,
                   'F': 20,
                   'S': Fraction(5, 3),
                   'V': 12,
                   'name': 'icosahedron',
                   'shape2count': {3: 20},
                   'shape2count_per_vtx': {3: 5}},
 (3, 3, 3, 3, 4): {'ASRP': (3, 3, 3, 3, 4),
                   'E': 60,
                   'F': 38,
                   'S': Fraction(19, 12),
                   'V': 24,
                   'name': 'snub_cube',
                   'shape2count': {3: 32, 4: 6},
                   'shape2count_per_vtx': {3: 4, 4: 1}},
 (3, 3, 3, 3, 5): {'ASRP': (3, 3, 3, 3, 5),
                   'E': 150,
                   'F': 92,
                   'S': Fraction(23, 15),
                   'V': 60,
                   'name': 'snub_dodecahedron',
                   'shape2count': {3: 80, 5: 12},
                   'shape2count_per_vtx': {3: 4, 5: 1}},
 (3, 4, 3, 4): {'ASRP': (3, 4, 3, 4),
                'E': 24,
                'F': 14,
                'S': Fraction(7, 6),
                'V': 12,
                'name': 'cuboctahedron',
                'shape2count': {3: 8, 4: 6},
                'shape2count_per_vtx': {3: 2, 4: 2}},
 (3, 4, 4, 4): {'ASRP': (3, 4, 4, 4),
                'E': 48,
                'F': 26,
                'S': Fraction(13, 12),
                'V': 24,
                'name': 'rhombicuboctahedron',
                'shape2count': {3: 8, 4: 18},
                'shape2count_per_vtx': {3: 1, 4: 3}},
 (3, 4, 5, 4): {'ASRP': (3, 4, 5, 4),
                'E': 120,
                'F': 62,
                'S': Fraction(31, 30),
                'V': 60,
                'name': 'rhombicosidodecahedron',
                'shape2count': {3: 20, 4: 30, 5: 12},
                'shape2count_per_vtx': {3: 1, 4: 2, 5: 1}},
 (3, 5, 3, 5): {'ASRP': (3, 5, 3, 5),
                'E': 60,
                'F': 32,
                'S': Fraction(16, 15),
                'V': 30,
                'name': 'icosidodecahedron',
                'shape2count': {3: 20, 5: 12},
                'shape2count_per_vtx': {3: 2, 5: 2}},
 (3, 6, 6): {'ASRP': (3, 6, 6),
             'E': 18,
             'F': 8,
             'S': Fraction(2, 3),
             'V': 12,
             'name': 'truncated_tetrahedron',
             'shape2count': {3: 4, 6: 4},
             'shape2count_per_vtx': {3: 1, 6: 2}},
 (3, 8, 8): {'ASRP': (3, 8, 8),
             'E': 36,
             'F': 14,
             'S': Fraction(7, 12),
             'V': 24,
             'name': 'truncated_cube',
             'shape2count': {3: 8, 8: 6},
             'shape2count_per_vtx': {3: 1, 8: 2}},
 (3, 10, 10): {'ASRP': (3, 10, 10),
               'E': 90,
               'F': 32,
               'S': Fraction(8, 15),
               'V': 60,
               'name': 'truncated_dodecahedron',
               'shape2count': {3: 20, 10: 12},
               'shape2count_per_vtx': {3: 1, 10: 2}},
 (4, 4, 4): {'ASRP': (4, 4, 4),
             'E': 12,
             'F': 6,
             'S': Fraction(3, 4),
             'V': 8,
             'name': 'cube',
             'shape2count': {4: 6},
             'shape2count_per_vtx': {4: 3}},
 (4, 6, 6): {'ASRP': (4, 6, 6),
             'E': 36,
             'F': 14,
             'S': Fraction(7, 12),
             'V': 24,
             'name': 'truncated_octahedron',
             'shape2count': {4: 6, 6: 8},
             'shape2count_per_vtx': {4: 1, 6: 2}},
 (4, 6, 8): {'ASRP': (4, 6, 8),
             'E': 72,
             'F': 26,
             'S': Fraction(13, 24),
             'V': 48,
             'name': 'truncated_cuboctahedron',
             'shape2count': {4: 12, 6: 8, 8: 6},
             'shape2count_per_vtx': {4: 1, 6: 1, 8: 1}},
 (4, 6, 10): {'ASRP': (4, 6, 10),
              'E': 180,
              'F': 62,
              'S': Fraction(31, 60),
              'V': 120,
              'name': 'truncated_icosidodecahedron',
              'shape2count': {4: 30, 6: 20, 10: 12},
              'shape2count_per_vtx': {4: 1, 6: 1, 10: 1}},
 (5, 5, 5): {'ASRP': (5, 5, 5),
             'E': 30,
             'F': 12,
             'S': Fraction(3, 5),
             'V': 20,
             'name': 'dodecahedron',
             'shape2count': {5: 12},
             'shape2count_per_vtx': {5: 3}},
 (5, 6, 6): {'ASRP': (5, 6, 6),
             'E': 90,
             'F': 32,
             'S': Fraction(8, 15),
             'V': 60,
             'name': 'truncated_icosahedron',
             'shape2count': {5: 12, 6: 20},
             'shape2count_per_vtx': {5: 1, 6: 2}}}


def __Archimedean_solid2info__extended():
    __extended = copy.deepcopy(Archimedean_solid2info)
    __extended[(3,3,3,'v')] = {
        'ASRP': (3,3,3,'v'),
        'E': '4*v',
        'F': '2*v+2',
        'S': '1+1/v',
        'V': '2*v',
        'name': 'ASRP_333v',
        'shape2count': {'v': 2, 3: '2*v'},
        'shape2count_per_vtx': {'v': 1, 3: 3}}
    __extended[(4,4,'v')] = {
        'ASRP': (4,4,'v'),
        'E': '3*v',
        'F': 'v+2',
        'S': '(2+v)/(2*v)', #'1/2+1/v',
        'V': '2*v',
        'name': 'ASRP_44v',
        'shape2count': {'v': 2, 4: 'v'},
        'shape2count_per_vtx': {'v': 1, 4: 2}}
    return __extended
Archimedean_solid2info__extended = __Archimedean_solid2info__extended()


if __name__ == '__main__':
    from pprint import pprint
    print('solids = \\')
    pprint(solids)
    print('Archimedean_solid2info = \\')
    pprint(Archimedean_solid2info)





