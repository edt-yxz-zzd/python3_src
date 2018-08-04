

'''
each face is recorded in clockwise order
clockwise from outside into center
'''




from itertools import groupby
from nn_ns.graph.planar_embedding import polyhedra_embedding2faces, \
     truncated_polyhedra, polyhedra_faces2embedding, snub3_polyhedra, \
     mid_truncated_polyhedra
from nn_ns.graph.show_v2neighbors import show_v2neighbors
from .Archimedean_solid__which import get_Archimedean_solid_info

__all__ = tuple('solid2faces, calc_faces_44v, calc_faces_333v'
                .split(', '))

def show_faces(faces):
    embedding = polyhedra_faces2embedding(faces)
    show_v2neighbors(embedding)


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
    
    info = get_Archimedean_solid_info(solid)
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
    solid = (4,4,v)
    
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

    check_faces(solid, faces)
    return tuple(faces)
    

def calc_faces_333v(v):
    '''[3,3,3,v] for v>=3 '''

    assert v >= 3
    solid = (3,3,3,v)
    
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

    check_faces(solid, faces)
    return tuple(faces)
    

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






for __solid, __faces in solid2faces.items():
    try:
        check_faces(__solid, __faces)
        #print('checed:', solid)
    except:
        print(__solid, __faces)
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

if __name__ == '__main__':
    for solid, faces in solid2faces.items():
        show_faces(faces)



