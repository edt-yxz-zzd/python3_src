
'''
test simple graph embedding
'''

from itertools import chain, groupby, accumulate

from .Boyer_Myrvold_planarity_test import \
     planar_embedding_by_Boyer_Myrvold as \
     _planar_embedding_by_Boyer_Myrvold,\
     is_planar_embedding as _is_planar_embedding, \
     is_planar as _is_planar

from .simple_undirected_graph import graph as _graph

def __is_planar(simple_graph, embedding):
    r1 = _is_planar(simple_graph)
    r2 = _is_planar_embedding(embedding)
    if r1 != r2:
        raise Exception('bug')
    return r
def is_planar(simple_graph, embedding=None):
    if embedding == None:
        return _is_planar(simple_graph)
    return __is_planar(simple_graph, embedding)
    
def is_planar_embedding(embedding):
    simple_graph = _graph(embedding)
    return __is_planar(simple_graph, embedding)

def planar_embedding(g):
    return _planar_embedding_by_Boyer_Myrvold(g)

def reverse_embedding(embedding):
    return [list(reversed(neighbors)) for neighbors in embedding]





def circlic_lshift_to_min(seq):
    if not seq:
        return seq[:]
    
    m = min(seq)
    idc = [i for i,x in enumerate(seq) if x == m]
    return min(seq[i:]+seq[:i] for i in idc)


def face2dedges(face):
    f = list(face)
    f.append(face[0])
    
    return list(zip(f[:-1], f[1:]))

def polyhedra_faces2embedding(faces):
    '''
input faces
output embedding

data type:
    faces = [face]
    face = [vtx]
    embedding = [neighbors]
    neighbors = [vtx]
    
    assume clockwise, viewing from outside into center
    face = [v0,v1,...,vt] = v0->v1->...->vt->v0 is of clockwise
    embedding[v] = [u0,u1,...,ut] = (v->u0, v->u1,..., v->ut) is of clockwise
    
    dedge = (u,v) # u!=v
'''
    
    nde = sum(map(len, faces))
    #dedges = set(chain.from_iterable(map(face2dedges, faces)))
    dedge2face_idx = {}
    dedges = set()
    v_face_idx2uw = {} # {(v, face_idx):(u,w) where u->v->w in face}
    v_face_idx2u = {}
    v_face_idx2w = {}
    for idx, face in enumerate(faces):
        es = face2dedges(face)
        dedges.update(es)
        dedge2face_idx.update((d,idx) for d in es)

        for u,v in es:
            v_face_idx2u[(v,idx)] = u
            v_face_idx2w[(u,idx)] = v
    assert len(v_face_idx2u) == len(v_face_idx2w)
    for vf in v_face_idx2u:
        v_face_idx2uw[vf] = (v_face_idx2u[vf], v_face_idx2w[vf])
        

    
    assert nde == len(dedges) # unique

    assert {(v,u) for u,v in dedges} == dedges # (u,v) and (v,u)
    assert all(u!=v for u,v in dedges)

    v2vus = dict((k,tuple(vus))
                 for k,vus in groupby(sorted(dedges), lambda vu: vu[0]))

    n = len(v2vus)
    assert set(v2vus) == set(range(n))

    v2vus = [v2vus[v] for v in range(n)] # == v2unordered_neighbors
    v2face_idc = [[] for v in range(n)]
    for idx, face in enumerate(faces):
        for v in face:
            v2face_idc[v].append(idx)

    
    
    embedding = v2neighbors = []
    for v, vus in enumerate(v2vus):
        face_idc_around_v = v2face_idc[v]
        face_idx2next_idx = {dedge2face_idx[(u,v)]:dedge2face_idx[(v,u)]
                             for v,u in vus}
        
        assert len(face_idx2next_idx) == len(face_idc_around_v)
        assert set(face_idx2next_idx) == set(face_idx2next_idx.values()) \
               == set(face_idc_around_v)

        
        f_idx = face_idc_around_v[0]
        face_idc_clockwise = []
        for _ in range(len(face_idc_around_v)):
            face_idc_clockwise.append(f_idx)
            f_idx = face_idx2next_idx[f_idx]
        assert set(face_idx2next_idx) == set(face_idc_clockwise)

        neighbors_clockwise = [v_face_idx2w[(v,f)] for f in face_idc_clockwise]
        neighbors_clockwise = circlic_lshift_to_min(neighbors_clockwise)
        assert len(v2neighbors) == v
        v2neighbors.append(neighbors_clockwise)

    return embedding


def truncated_polyhedra(embedding):
    '''each old edge introduces two new vtc

truncated_polyhedra.nv = org_polyhedra.ne * 2
truncated_polyhedra.ne = org_polyhedra.ne * 3
truncated_polyhedra.nf = org_polyhedra.nf + org_polyhedra.nv
truncated_polyhedra:: nv+nf-ne
    = org_polyhedra:: 2 ne + nf+nv - 3 ne = nv+nf-ne = 2

org_shapes = map(len, org_polyhedra.faces)
truncated_shapes = [2*s for s in org_shapes] \
                    + [org_polyhedra.degree(v) for v in org_polyhedra.vtc]

assert all(truncated_polyhedra.degree(v) == 3 for v in truncated_polyhedra.vtc)


i.e. truncated(ASRP[3, 3, 3]) = ASRP[3, 6, 6]
'''
    old_v2new_base = [0]
    old_v2new_base.extend(accumulate(map(len, embedding)))
    old_v2new_base.pop()


    old_uv2new_vtx = {}
    new_v = -1
    for old_v, old_neighbors in enumerate(embedding):
        base = old_v2new_base[old_v]
        assert base == new_v+1
        for new_v, old_w in enumerate(old_neighbors, base):
            old_uv2new_vtx[(old_v, old_w)] = new_v
            
    new_embedding = []
    for old_v, old_neighbors in enumerate(embedding):
        L = len(old_neighbors)
        for i, old_w in enumerate(old_neighbors):
            new_v = old_uv2new_vtx[(old_v, old_w)]
            new_u = old_uv2new_vtx[(old_v, old_neighbors[i-1])]
            new_w = old_uv2new_vtx[(old_v, old_neighbors[i+1-L])]
            new_x = old_uv2new_vtx[(old_w, old_v)]
            new_neighbors = [new_w, new_u, new_x]
            new_neighbors = circlic_lshift_to_min(new_neighbors)
            assert new_v == len(new_embedding)
            new_embedding.append(new_neighbors)

    old_V = len(embedding)
    old_E2 = sum(map(len, embedding))
    old_E = old_E2//2
    assert old_E2 == old_E*2
    
    new_V = len(new_embedding)
    new_E2 = sum(map(len, new_embedding))
    new_E = new_E2//2
    assert new_E2 == new_E*2

    assert new_V == old_E*2
    assert new_E == old_E*3

    assert set(map(len, new_embedding)) == {3}
    return new_embedding


def mid_truncated_polyhedra(embedding):
    '''each old edge introduces one new vtc

mid_truncated_polyhedra.nv = org_polyhedra.ne
mid_truncated_polyhedra.ne = org_polyhedra.ne * 2
mid_truncated_polyhedra.nf = org_polyhedra.nf + org_polyhedra.nv
mid_truncated_polyhedra:: nv+nf-ne
    = org_polyhedra:: ne + nf+nv - 2 ne = nv+nf-ne = 2

org_shapes = map(len, org_polyhedra.faces)
mid_truncated_shapes = org_shapes \
                    + [org_polyhedra.degree(v) for v in org_polyhedra.vtc]

assert all(mid_truncated_polyhedra.degree(v) == 4 for v in mid_truncated_polyhedra.vtc)


i.e.
    mid_truncated(ASRP[3,3,3]) == ASRP[3,3,3,3]
        //          tetrahedron     octahedron
    mid_truncated(ASRP[3,3,3,3]) == ASRP[3,4,3,4] == mid_truncated(ASRP[4,4,4])
        //          octahedron         cuboctahedron                   cube
    mid_truncated(ASRP[3,3,3,3,3]) == ASRP[3,5,3,5] == mid_truncated(ASRP[5,5,5])
        //          icosahedron        icosidodecahedron           dodecahedron
    mid_truncated(ASRP[3,4,3,4]) ~=~ ASRP[3,4,4,4]
        //      cuboctahedron       rhombicuboctahedron
        //                       rhombi- ::== mid_truncated???
    mid_truncated(ASRP[3,5,3,5]) ~=~ ASRP[3,4,5,4]
        //      icosidodecahedron   rhombicosidodecahedron
    
    
    
'''
    old_uv2new_vtx = {} # u<v
    new_v = -1
    for old_v, old_neighbors in enumerate(embedding):
        for old_w in old_neighbors:
            if old_v < old_w:
                new_v += 1
                old_uv2new_vtx[(old_v, old_w)] = new_v
                old_uv2new_vtx[(old_w, old_v)] = new_v
            
    new_embedding = []
    for old_v, old_neighbors in enumerate(embedding):
        L = len(old_neighbors)
        for i, old_w in enumerate(old_neighbors):
            new_v = old_uv2new_vtx[(old_v, old_w)]
            new_u = old_uv2new_vtx[(old_v, old_neighbors[i-1])]
            new_w = old_uv2new_vtx[(old_v, old_neighbors[i+1-L])]
            new_neighbors = [new_w, new_u]

            if old_v < old_w:
                assert new_v == len(new_embedding)
                new_embedding.append(new_neighbors)
            else:
                assert new_v < len(new_embedding)
                new_embedding[new_v].extend(new_neighbors)
                new_embedding[new_v] = circlic_lshift_to_min(new_embedding[new_v])
                

    old_V = len(embedding)
    old_E2 = sum(map(len, embedding))
    old_E = old_E2//2
    assert old_E2 == old_E*2
    
    new_V = len(new_embedding)
    new_E2 = sum(map(len, new_embedding))
    new_E = new_E2//2
    assert new_E2 == new_E*2

    assert new_V == old_E
    assert new_E == old_E*2

    assert set(map(len, new_embedding)) == {4}
    return new_embedding


def snub3_polyhedra(embedding):
    '''degree of every old vtx is 3;
each old vtx introduces 3 new vtc;

assert all(org_polyhedra.degree(v) == 3 for v in org_polyhedra.vtc)
    org_polyhedra:: ne*2 == nv*3; ne=nv*3/2; nf = 2+ne-nv = 2+nv/2


snub3_polyhedra.nv = org_polyhedra.nv * 3
snub3_polyhedra.ne = org_polyhedra.ne + snub3_polyhedra.nv*2
    = org_polyhedra.ne + org_polyhedra.nv*6
    = org_polyhedra.nv*15/2
    = org_polyhedra.ne*5
snub3_polyhedra.nf = org_polyhedra.nf + org_polyhedra.nv*4
    = 2+org_polyhedra.nv*9/2
snub3_polyhedra:: nv+nf-ne
    = org_polyhedra:: (3+9/2-15/2)nv + 2 = 2

org_shapes = map(len, org_polyhedra.faces)
snub3_polyhedra = org_shapes + [3]*(org_polyhedra.nv*4)

assert all(snub3_polyhedra.degree(v) == 5 for v in snub3_polyhedra.vtc)


i.e.
    snub3(ASRP[3,3,3]) ~=~ ASRP[3,3,3,3,3]
        //   tetrahedron    icosahedron
    snub3(ASRP[4,4,4]) ~=~ ASRP[3,3,3,3,4]
        //   cube           snub_cube
    snub3(ASRP[5,5,5]) ~=~ ASRP[3,3,3,3,5]
        //   dodecahedron   snub_dodecahedron
'''
    assert set(map(len, embedding)) == {3}
    
    old_vw2new_v = {}
    for old_v, old_neighbors in enumerate(embedding):
        base = old_v*3
        old_w2new_v = dict(zip(old_neighbors, range(base, base+3)))
        for old_w in old_neighbors:
            old_vw = old_v, old_w
            old_vw2new_v[old_vw] = old_w2new_v[old_w]

    old_vw2new_vw = {} # partial new_vw, since new_ne > old_ne
    for old_vw in old_vw2new_v:
        old_wv = tuple(reversed(old_vw))
        new_v = old_vw2new_v[old_vw]
        new_w = old_vw2new_v[old_wv]
        old_vw2new_vw[old_vw] = new_v, new_w
    for old_vw, new_vw in old_vw2new_vw.items():
        old_wv = tuple(reversed(old_vw))
        new_wv = old_vw2new_vw[old_wv]
        assert new_vw == tuple(reversed(new_wv))

    new_v2new_w__from_old_vw = {}
    for new_v, new_w in old_vw2new_vw.values():
        assert new_v not in new_v2new_w__from_old_vw
        new_v2new_w__from_old_vw[new_v] = new_w
    for new_v, new_w in new_v2new_w__from_old_vw.items():
        assert new_v2new_w__from_old_vw[new_w] == new_v

        

    def add_in3(new_v, k):
        r = new_v % 3
        base = new_v - r
        r += k
        r %= 3
        return base + r

    new_embedding = []
    for old_v, old_neighbors in enumerate(embedding):
        for old_w in old_neighbors:
            old_vw = old_v, old_w
            new_v, new_w = old_vw2new_vw[old_vw]

            # clockwise
            new_v1 = add_in3(new_v, 1)
            new_v2 = add_in3(new_v, 2)
            new_w_of_new_v2 = new_v2new_w__from_old_vw[new_v2]
            new_w1 = add_in3(new_w, 1)
            
            new_neighbors = [new_w, new_v1, new_v2, new_w_of_new_v2, new_w1]
            new_neighbors = circlic_lshift_to_min(new_neighbors)
            assert new_v == len(new_embedding)
            new_embedding.append(new_neighbors)
            

    old_V = len(embedding)
    old_E2 = sum(map(len, embedding))
    old_E = old_E2//2
    assert old_E2 == old_E*2
    
    new_V = len(new_embedding)
    new_E2 = sum(map(len, new_embedding))
    new_E = new_E2//2
    assert new_E2 == new_E*2

    assert new_V == old_V*3
    assert new_E == old_E*5

    assert set(map(len, new_embedding)) == {5}
    return new_embedding
            
            
        
            
def polyhedra_embedding2faces(embedding):
    '''see polyhedra_faces2embedding doc :: clockwise'''

    uv2vw = {}
    for v, neighbors in enumerate(embedding):
        L = len(neighbors)
        for i, w in enumerate(neighbors):
            # (...,v->w,v->u,...) in neighbors ==>> u->v->w in face
            u = neighbors[i+1-L]
            uv2vw[(u,v)] = (v,w)

    nde = len(uv2vw)
    assert nde == sum(map(len, embedding))
    
    faces = []
    while uv2vw:
        org_uv, vw = uv2vw.popitem()
        face = [vw[0]]
        while vw != org_uv:
            face.append(vw[1])
            vw = uv2vw.pop(vw)

        face = circlic_lshift_to_min(face)
        faces.append(face)

    assert nde == sum(map(len, faces))
    return faces





        





        
    







