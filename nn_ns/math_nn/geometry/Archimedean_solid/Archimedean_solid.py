

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


if False:
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
















































