
class fake_face:
    def __init__(self, G):
        self.graph = G
        face2dedges, dedge2face, dedge2face_idx, face2circle_vtc = fake_face2dedges(G)
        self.face2dedges, self.dedge2face, \
            self.dedge2face_idx, self.face2circle_vtc = \
            face2dedges, dedge2face, dedge2face_idx, face2circle_vtc
    def next_dedge(self, dedge):
        return fake_face_next_dedge(dedge, self.graph)
    def prev_dedge(self, dedge):
        return fake_face_prev_dedge(dedge, self.graph)
    def nf(self): return len(self.face2dedges)

def fake_face_next_dedge(dedge, G):
    _, v = G.dedge2edge(dedge)
    _, v_loc = G.where_dedge(dedge)
    v_loc += 1
    v_loc -= G.degree(v)
    dedge = G.dedges(v)[v_loc]
    return dedge
    
def fake_face_prev_dedge(dedge, G):
    v, _ = G.dedge2edge(dedge)
    v_loc, _ = G.where_dedge(dedge)
    v_loc -= 1
    dedge = G.dedges(v)[v_loc]
    dedge = G.flip_dedge(dedge)
    return dedge
    
def fake_face2dedges(G):
    dedge2face_idx = [None]*(G.ne()*2)
    dedge2face = [None]*(G.ne()*2)
    face2dedges = []
    face2circle_vtc = []
    for dedge, face in enumerate(dedge2face):
        if face != None: continue
        assert G.is_uedge(dedge)
        face = len(face2dedges)
        ds = []
        vs = []
        while dedge2face[dedge] == None:
            face_idx = len(ds)
            u, _ = G.dedge2edge(dedge)
            vs.append(u)
            ds.append(dedge)
            dedge2face[dedge] = face
            dedge2face_idx[dedge] = face_idx
            dedge = fake_face_next_dedge(dedge, G)
        assert len(ds) >= 2
        assert ds[0] == dedge
        face2dedges.append(tuple(ds))
        face2circle_vtc.append(tuple(vs))

    #for face in dedge2face: assert face != None except isolated vtx
    
    face2dedges, dedge2face, dedge2face_idx, face2circle_vtc = \
                 tuple(face2dedges), tuple(dedge2face), \
                 tuple(dedge2face_idx), tuple(face2circle_vtc)
    return face2dedges, dedge2face, dedge2face_idx, face2circle_vtc

