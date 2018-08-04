

'''
try to use general 'solver' to find a suitable 3D draw
fail, cannot converge

'''
from itertools import chain
from math import tanh
import math
import numpy as np
from numpy.dual import lstsq
from scipy.optimize import *


from graph.simple_undirected_graph import graph

from graph.fake_face import fake_face
from graph.some_triconnected_cubic_planar_graphs import get_planar_embeddings

#print(lstsq([(1,2), (2,3), (2,1)], [0, 0, 0])) = x,_,_,_

def on_same_plane(xyz_ls):
    #print(xyz_ls)
    r,_,_,_ = lstsq(xyz_ls, [0]*len(xyz_ls))
    #print(len(r))
    ABC = A,B,C = r
    return [inner(ABC, xyz) for xyz in xyz_ls]

def inner(a, b):
    return sum(A*x for A,x in zip(a, b))
def on_surface(xyz_ls, R):
    return [elen(xyz)-R*R for xyz in xyz_ls]

def elen(xyz):
    return sum(x*x for x in xyz)

def be_polygon(xyz_ls):
    xyz_ls2 = xyz_ls + xyz_ls[:2]
    cos_outer_angles = []
    for a, b, c in zip(xyz_ls, xyz_ls2[1:], xyz_ls2[2:]):
        ab = b - a
        bc = c - b
        L = elen(ab)*elen(bc)
        cos_outer_angle = inner(ab, bc)/math.sqrt(L)
        if not math.isfinite(cos_outer_angle):
            cos_outer_angle = -1
        if abs(cos_outer_angle) > 1:
            cos_outer_angle /= abs(cos_outer_angle)
        assert abs(cos_outer_angle) <= 1
        cos_outer_angles.append(cos_outer_angle)
    assert all(math.isfinite(x) for x in cos_outer_angles)
    outer_angles = np.arccos(cos_outer_angles)
    if not all(math.isfinite(x) for x in outer_angles):
        print(cos_outer_angles, outer_angles)
        pass
    return sum(outer_angles) - 2*np.pi

def not_too_small(edge_vec_ls, R, nv):
    th = 4*R/nv
    h = (tanh(th)+1)/2
    lens = [elen(e)-th if elen(e) < th else 0 for e in edge_vec_ls]
    return [tanh(L) - h for L in lens]

    

def draw_polyhedron(planar_embedding):
    g = graph(planar_embedding)
    ff = fake_face(g)
    f2vtc = ff.face2circle_vtc
    R = 1
    n = g.nv()
    M = n + sum(len(vs) for vs in f2vtc) + len(f2vtc) + g.ne()
    assert M >= 3*n

    def f(xyzarray):
        assert len(xyzarray) == M
        xyz_ls = [xyzarray[i:i+3] for i in range(0, 3*n, 3)]
        assert len(xyz_ls) == n
        r = on_surface(xyz_ls, R)
        for vs in f2vtc:
            face_xyz_ls = [xyz_ls[v] for v in vs]
            r.extend(on_same_plane(face_xyz_ls))
            r.append(be_polygon(face_xyz_ls))

        edge_vec_ls = []
        for u,v in g.edges():
            vec = [x1-x2 for x1,x2 in zip(*(xyz_ls[x] for x in (u,v)))]
            edge_vec_ls.append(vec)
        r.extend(not_too_small(edge_vec_ls, R, n))
        return r

    #newton_krylov, anderson, broyden2
    ans = broyden1(f, np.random.random_sample((M,)))
    return ans

for embedding in get_planar_embeddings():
    print(draw_polyhedron(embedding))
    break

    









    
