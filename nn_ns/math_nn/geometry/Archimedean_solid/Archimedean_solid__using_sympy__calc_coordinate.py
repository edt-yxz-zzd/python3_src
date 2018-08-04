


'''
assume:
    vtcs on unit sphere
    v0 = (1,0,0) except 44v, 333v
    v1 = (x1, y1, 0) where y1 > 0



edge(A,B), angle(BAC), isedge(A,C), next_clockwise_edge(A,(A,B))=(A,B) -> C:
    ==>> (OB cross OA) dot OC > 0

R - radius of sphere
L - length of edge
    
'''
#from sympy import *
from sympy import nsimplify, sympify, cos, sin, pi
from nn_ns.sympy_util.my_sympify import my_sympify
from nn_ns.sympy_util.constant import one, zero
from nn_ns.sympy_util.geometry import dot_product, cross_product, distance, \
     rotate_clockwise, opposite_tri_angle, vec_len,\
    opposite_tri_edge, tri_area, angle_of_regular_polygon
from .Archimedean_solid__faces import solid2faces
from nn_ns.graph.planar_embedding import polyhedra_embedding2faces, \
     polyhedra_faces2embedding
from .Archimedean_solid__which import get_Archimedean_solid_info, solids
from .Archimedean_solid__L_div_R_using_sympy__solid2g import solid2g

from nn_ns.graph.show_v2neighbors import show_v2neighbors
from collections import deque


solid2g, solid2faces, solids

def next_clockwise_edge_endpoint(A, B, angle_BAC):
    assert 0 <= angle_BAC <= pi
    O = (0,0,0)
    #print(list(map(type, [A,B])))
    #print(list(map(tuple, (B, A))))
    #OB, OA = B, A = map(tuple, (B, A))
    # add list. why?????????
    #
    # sympy bug: Tuple.__new__ not like tuple's!!!
    OB, OA = B, A = list(map(tuple, (B, A)))
    R = len_OA = len_OB = distance(O,A)
    L = len_AB = len_AC = distance(B,A)
    len_BC = opposite_tri_edge(len_AB, angle_BAC, len_AC)
    len_BC = my_sympify(len_BC)
    
    # Q on OA, BQ _L OA
    S_ABO = tri_area(len_OA, len_OB, len_AB)
    assert nsimplify(S_ABO) > 0
    len_CQ = len_BQ = one*2*S_ABO/len_OA
    len_CQ = len_BQ = my_sympify(len_BQ)
    
    angle_BQC = opposite_tri_angle(len_BQ, len_BC, len_CQ)
    angle_BQC = my_sympify(angle_BQC)
    assert nsimplify(angle_BQC) > 0
    assert nsimplify(angle_BQC - pi) < 0
    C = OC = rotate_clockwise(O, A, B, angle_BQC)
    C = OC = tuple(map(my_sympify, OC))

##    print(next_clockwise_edge_endpoint)
##    print(distance(B,C))
##    print(len_BC)
    try:
        assert nsimplify(distance(O,C) - R) == 0
        assert nsimplify(distance(A,C) - L) == 0
        assert nsimplify(distance(B,C) - len_BC) == 0
        assert dot_product(cross_product(OB, OA), OC) > 0
    except:
        print(locals())
        assert nsimplify(distance(O,C) - R, tolerance=0) == 0
        raise
    return tuple(C)


def __verify_C(A, B, angle_BAC, C):
    O = (0,0,0)
    OC, OB, OA = C, B, A = list(map(tuple, (C, B, A)))
    R = len_OA = len_OB = distance(O,A)
    L = len_AB = len_AC = distance(B,A)
    len_BC = opposite_tri_edge(len_AB, angle_BAC, len_AC)
    len_BC = my_sympify(len_BC)
    assert nsimplify(distance(B,C) - len_BC) == 0
    assert nsimplify(distance(A,C) - L) == 0
    assert dot_product(cross_product(OB, OA), OC) > 0

def get_v0v1(L, R):
    assert 0 < L < 2*R
    v0 = (R, 0, 0)

    len_Ov0 = len_Ov1 = R
    len_v0v1 = L
    angle_v0Ov1 = opposite_tri_angle(len_Ov0, len_v0v1, len_Ov1)
    x = len_Ov1 * cos(angle_v0Ov1)
    y = len_Ov1 * sin(angle_v0Ov1)
    v1 = (x, y, 0)

    assert nsimplify(vec_len(v1) - R) == 0
    assert nsimplify(y) > 0
    return v0, v1




def ASRP_solid2coordinates(solid, L_div_R):
    info = get_Archimedean_solid_info(solid)
    faces = solid2faces[solid]
    g = L_div_R
    L = g
    R = 1

    dedge2next_vtx = {} # (u,v)->w where (u,w) is edge, (u,v)->(u,w) in clockwise
    for face in faces:
        face_plus2 = face + face[:2]
        for i in range(len(face)):
            u,v,w = v3 = face_plus2[i:i+3]
            dedge = (v,w)
            assert dedge not in dedge2next_vtx
            dedge2next_vtx[dedge] = u
    
    v3_to_face_idx = {}
    def set_v3(v3, face_idx):
        v3 = frozenset(v3)
        if v3 in v3_to_face_idx:
            print(v3, face)
        assert v3 not in v3_to_face_idx
        v3_to_face_idx[v3] = face_idx
    for face_idx, face in enumerate(faces):
        if len(face) == 3:
            v3 = face
            set_v3(v3, face_idx)
            continue
        
        face_plus2 = face + face[:2]
        for i in range(len(face)):
            u,v,w = v3 = face_plus2[i:i+3]
            set_v3(v3, face_idx)

    assert (0,1) in dedge2next_vtx

    V = info['V']
    assert set(v for face in faces for v in face) == set(range(V))
    
    v2coor = [None]*V
    v2coor[:2] = get_v0v1(L, R)

    unprocessed_vtc = set(range(V))
    vtx_which_no_dedges_in_deque = set(range(2,V))
    to_process = deque([(0,1), (1,0)])
    for i in range(len(dedge2next_vtx)):
        assert i < len(to_process)
        u, v = to_process[i]

        # each vtx processed once
        if u not in unprocessed_vtc:
            continue
        unprocessed_vtc.remove(u)
        
        v0 = v
        ws = set()
        while True:
            w = dedge2next_vtx[(u,v)]
            if w == v0:
                break
            to_process.append((u,w))
            ws.add(w)
            v = w
        to_process.extend((w,u) for w in ws & vtx_which_no_dedges_in_deque)
        vtx_which_no_dedges_in_deque -= ws
    assert i+1 == len(to_process) == len(dedge2next_vtx)

    while to_process:
        u, v = to_process.popleft()
        assert v2coor[u] is not None
        assert v2coor[v] is not None

        w = dedge2next_vtx[(u,v)]
        v3 = frozenset([u,v,w])
        face_idx = v3_to_face_idx[v3]
        n = len(faces[face_idx])

        angle_vuw = angle_of_regular_polygon(n)
        if v2coor[w] is not None:
            A, B, angle_BAC, C = v2coor[u], v2coor[v], angle_vuw, v2coor[w]
            __verify_C(A, B, angle_BAC, C)
            continue

        # calc w
##        print('w =', w)
##        print('[u,v,w] =', [u,v,w])
##        print('v2coor[u], v2coor[v] =', v2coor[u], v2coor[v])
        #print('to_process =', to_process)
        #print(next_clockwise_edge_endpoint)
        v2coor[w] = next_clockwise_edge_endpoint(
            v2coor[u], v2coor[v], angle_vuw)
        v2coor[w] = tuple(map(my_sympify, v2coor[w]))

    try:
        assert all(c is not None for c in v2coor)
    except:
        print(solid)
        print(faces)
        raise
    return v2coor



    









