

from fractions import Fraction
from .Archimedean_solid__which import get_Archimedean_solid_info, \
     Archimedean_solid2info__extended as __ex
from sympy import var, expand, nsimplify
from pprint import pprint

# v_2 = v-2 > 0
var('v v_2', postive=True, integer=True)

def str_to_expr(s):
    return eval(s) if type(s) is str else s
def dict2expr(d):
    return {str_to_expr(__k): str_to_expr(__v) for __k, __v in d.items()}

def __build_solid2info_using_sympy():
    new = {}
    for solid, info in __ex.items():
        if 'v' in solid:
            solid = tuple(x if x != 'v' else v for x in solid)
            info = {
                'ASRP': solid,
                'E': str_to_expr(info['E']),
                'F': str_to_expr(info['F']),
                'S': str_to_expr(info['S']),
                'V': str_to_expr(info['V']),
                'name': info['name'],
                'shape2count': dict2expr(info['shape2count']),
                'shape2count_per_vtx': dict2expr(info['shape2count_per_vtx'])}
        new[solid] = info
    return new

solid2info_using_sympy = __build_solid2info_using_sympy()



    
def check_solid2info_using_sympy(solid2info):
    v_ = v_2 + 2
    zero = v-v
    v2v_ = lambda x: expand((zero+x).subs(v, v_))
    def dict_v2v_(d):
        return {v2v_(k):v2v_(v) for k, v in d.items()}
    for solid, info in solid2info.items():
        solid_ = tuple(map(v2v_, solid))
            
        info_ = get_Archimedean_solid_info(solid_)
        if not info_:
            print('check_solid2info_using_sympy', solid)
        assert info_
        for name in 'EFSV':
            z = info[name] - info_[name]
            assert 0 == (v2v_(z)).simplify().ratsimp()
        for name in ['shape2count', 'shape2count_per_vtx']:
            d = info[name]
            d = dict_v2v_(d)
            d_ = info_[name]
            assert d == d_
            
check_solid2info_using_sympy(solid2info_using_sympy)
#pprint(solid2info_using_sympy)



        
if __name__ == '__main__':
    print('solid2info_using_sympy =\\')
    pprint(solid2info_using_sympy)


assert solid2info_using_sympy == \
    {(3, 3, 3): {'ASRP': (3, 3, 3),
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
     (3, 3, 3, v): {'ASRP': (3, 3, 3, v),
                    'E': 4*v,
                    'F': 2*v + 2,
                    'S': 1 + 1/v,
                    'V': 2*v,
                    'name': 'ASRP_333v',
                    'shape2count': {3: 2*v, v: 2},
                    'shape2count_per_vtx': {3: 3, v: 1}},
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
     (4, 4, v): {'ASRP': (4, 4, v),
                 'E': 3*v,
                 'F': v + 2,
                 'S': (v + 2)/(2*v),
                 'V': 2*v,
                 'name': 'ASRP_44v',
                 'shape2count': {4: v, v: 2},
                 'shape2count_per_vtx': {4: 2, v: 1}},
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

