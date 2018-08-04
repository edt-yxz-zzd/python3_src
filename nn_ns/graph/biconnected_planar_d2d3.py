
'''
simple
biconnected
planar
degree == 2 or 3  (so  n > 2)

    we have:::::::::
    SPQR-tree: (no R - P - R pattern)
    (1) only one R
    (2) select an S as root
        S -> P(pure) -> R   ===> S -> R
        S -> P(pure) -> S   ===> S -> RS
                    \-> S
        S -> P(real) -> S   ===> S -> RS
        R -> P(pure) -> S   ===> R -> S

        that is:
        [R]S -> R[S]
        R -> S
    an S has at least 2 real edges, no 2 virtual edges are incident


let degree == 3:::::
an S has at least 2 real(virtual) edges, no 2 real(virtual) edges are incident

'''


from .bucket_sort import bucket_sorts, group
from .simple_undirected_graph import graph
from .BC_tree import bc_tree, spqr_tree, \
     connected_component2vtc_in_dfs_preordering, _SRcomponents2spqr, \
     _spqr_component_edges2components
from .DFS import *
from .rooted_tree import DFS_tree, up_from, down_to
from .fake_face import fake_face
from .Boyer_Myrvold_planarity_test import Boyer_Myrvold_planarity_test
from .planar_ordering import left_most_canonical_ordering


def label_faces(G_biconnected_embedding):
    g = G_biconnected_embedding
    faces = fake_face(g)
    faces, dedge2face = faces.face2dedges, faces.dedge2face
    return len(faces), dedge2face, faces

def SPQR_tree_for_c2d2d3_planar(G_biconnected_embedding):
    return _SPQR_tree_for_c2d2d3_planar(G_biconnected_embedding).calc()

def is_c2d2d3_planar(G):
    from Boyer_Myrvold_planarity_test import is_planar
    return is_c2d2d3_graph(G) and is_planar(G)
def is_c2d2d3_graph(G):
    for u in G.vertices():
        if not 2 <= G.degree(u) <= 3:
            return False
    return is_biconnected(G)

class _SPQR_tree_for_c2d2d3_planar:
    def __init__(self, G_c2d2d3):
        assert is_c2d2d3_graph(G_c2d2d3)
        G_biconnected_embedding = Boyer_Myrvold_planarity_test(G_c2d2d3)
        G = self.G = graph(G_biconnected_embedding)
        n = self.n = G.order()
        num_faces, dedge2face, face2circle \
                   = self.num_faces, self.dedge2face, self.face2circle \
                   = label_faces(G)
        multi_adjacency_faces = self.multi_adjacency_faces \
                                = _builde_multi_adjacency_faces(num_faces, dedge2face)

        is_outer_face = self.is_outer_face = [False]*num_faces
        face_state_buffer = self.face_state_buffer = [-1]*num_faces
        S_circles = self.S_circles = []
        get_dedge = self.get_dedge = lambda e:e
        get_edge = self.get_edge = lambda e:self.G.dedge2edge(e)


    def calc(self):
        G = self.G
        n = self.n
        num_faces = self.num_faces
        is_outer_face = self.is_outer_face
        S_circles = self.S_circles
        
        for face in range(num_faces):
            if is_outer_face[face]:
                mfaces = self.multiedges_adjacency_outerfaces(face)
                if mfaces:
                    S_circles += self.gen_S(face, mfaces)
            else:
                mfaces = self.multiedges_adjacency_faces(face)
                if mfaces:
                    S_circles += self.gen_S(face, mfaces)
                for mf in mfaces:
                    is_outer_face[mf] = True
                    
        edges = [(u, v, -1) for u, v in G.edges()]
        for s, S in enumerate(S_circles):
            edges += [(min(u,v), max(u,v), s) for u, v in S]


        edges = bucket_sorts(edges, lambda i,e:e[i], (1,0), (n,n))
        block = group(edges, lambda e:e[:2])
        R_edges = []
        P_edges = []
        P_real_edges = []
        #1:R, 1virtual/2/3:S, 1virtual/3:P
        for i, j in block:
            L = j - i
            if L == 1:
                e = edges[i]
                R_edges.append(e[:2])
                if e[-1] != -1:
                    P_edges.append((e,))
            elif L == 3:
                if edges[j][-1] == -1:
                    P_real_edges.append(edges[i:j])
                else:
                    P_edges.append(edges[i:j])
        num_P_with_real_edge = len(P_real_edges)
        num_P = len(P_edges) + len(P_real_edges)

        R_component_edges = _R_edges2R_component_edges(n, R_edges)
        SR_component_edges = S_circles + R_component_edges
        SRcomponents = _spqr_component_edges2components(n, SR_component_edges)

        return _SRcomponents2spqr(G, SRcomponents)
    


    def multiedges_adjacency_outerfaces(self, face):
        multi_adjacency_faces = self.multi_adjacency_faces
        is_outer_face = self.is_outer_face
        assert is_outer_face[face]
        mf = []
        for f in multi_adjacency_faces[face]:
            if f > face: break
            if is_outer_face[f]:
                mf.append(f)

        return mf

    def multiedges_adjacency_faces(self, face):
        multi_adjacency_faces = self.multi_adjacency_faces
        is_outer_face = self.is_outer_face
        
        assert not is_outer_face[face]
        for f in multi_adjacency_faces[face]:
            assert f > face or is_outer_face[f]

        return multi_adjacency_faces[face]

    def gen_S(self, face, mfaces):
        G = self.G
        n = self.n
        num_faces, dedge2face, face2circle \
                   = self.num_faces, self.dedge2face, self.face2circle
        multi_adjacency_faces = self.multi_adjacency_faces
        is_outer_face = self.is_outer_face
        face_state_buffer = self.face_state_buffer
        S_circles = self.S_circles
        get_dedge = self.get_dedge
        get_edge = self.get_edge

        if G.order() == G.num_edges():
            assert face == 0 and mfaces == (1,)
            assert num_faces == 2
            return [G.edges()]
        
        for f in mfaces: face_state_buffer[f] = 0
        
        face_circle = face2circle[face]
        color = []
        for e in face_circle:
            dedge = get_dedge(e)
            mf = dedge2face[G.flip_dedge(dedge)]
            assert mf != face
            if face_state_buffer[mf] == -1:
                color.append(-1)
            else:
                color.append(mf)

        assert len(color) == len(face_circle)
        block = group(color)
        assert len(block) > 1

        if color[0] == color[-1]:
            j = block[0][1]
            face_circle = face_circle[j:] + face_circle[:j]
            color = color[j:] + color[:j]
            block = group(color)
        assert color[0] != color[-1]


        
        def pass_colorful_path():
            S = S_part_stack[-1]
            for k in range(i, j):
                S.append(get_edge(face_circle[k]))

        def closing_last_S():
            nonlocal pre
            closing_mf = color_stack.pop()
            assert face_state_buffer[closing_mf] == 1
            face_state_buffer[closing_mf] = 2
            S = S_part_stack.pop()
            assert len(S) >= 1
            u, v = S[-1][-1], S[0][0]
            S.append((u, v))
            if len(S) > 2:
                Ss.append(S)
            if u != pre:
                middle_S.append((u,pre))
            middle_S.append((v,u))
            pre = v

        def finish_middle_S():
            u = S_part_stack[-1][-1][-1]
            if u != pre:
                middle_S.append((u,pre))
            finish_middle_S_2()
        def finish_middle_S_2():
            u = middle_S[-1][0]
            v = middle_S[0][-1] # == get_edge(face_circle[i])[0]
            if v != u:
                middle_S.append((v, u))
            assert len(middle_S) >= 2
            if len(middle_S) > 2:
                middle_S.reverse()
                Ss.append(middle_S)
        Ss = []
        S_part_stack = []
        color_stack = []
        for i, j in block:
            mf = color[i]
            if mf == -1: continue
            state = face_state_buffer[mf]
            assert state == 0 or state == 1
            if state == 0:
                face_state_buffer[mf] = 1 # open
                S_part_stack.append([])
                color_stack.append(mf)
                pass_colorful_path()
                continue

            middle_S = []
            pre = get_edge(face_circle[i])[0]
            while color_stack[-1] != mf:
                closing_last_S()
            finish_middle_S()

            S_part = S_part_stack[-1]
            u = S_part[-1][-1]
            v = get_edge(face_circle[i])[0]
            S_part.append((u,v))
            pass_colorful_path()
        else:
            middle_S = []
            pre = get_edge(face_circle[0])[0]
            while color_stack:
                closing_last_S()
            finish_middle_S_2()


        for f in mfaces:
            assert face_state_buffer[f] == 2
            face_state_buffer[f] = -1

        return Ss
        


def _R_edges2R_component_edges(n, R_edges):
    gR = graph(n, R_edges)
    vtc_ls, uedges_ls = connected_component2vtc_in_dfs_preordering(gR)
    for vtc in vtc_ls:
        assert len(vtc) == 1 or len(vtc) > 3

    R_node2vertices = tuple(vtc for vtc in vtc_ls if len(vtc) > 3)
    num_R = len(R_node2vertices)
    R_component_edges = list(tuple((u, v) for u in vertices for v in gR.neighbors(u) if u < v) \
                              for R, vertices in enumerate(R_node2vertices))
    return R_component_edges

def _builde_multi_adjacency_faces(num_faces, dedge2face):
    m = len(dedge2face)//2
    assert m*2 == len(dedge2face)
    to_co_edge = lambda uedge:tuple(sorted((dedge2face[uedge], dedge2face[uedge+m])))
    
    co_multiedge_graph_edges = tuple(to_co_edge(uedge) for uedge in range(m))
    co_multiedge_graph_edges = bucket_sorts(\
        co_multiedge_graph_edges, lambda i,e:e[i], (1,0), (num_faces,)*2)
    block = group(co_multiedge_graph_edges)
    representative_of_proper_multiedge = []
    for i, j in block:
        if j > i + 1:
            representative_of_proper_multiedge.append(co_multiedge_graph_edges[i])
    h = graph(num_faces, representative_of_proper_multiedge)
    return h.adjacency_list()
    '''
    edge_idx2faces = bucket_sorts(edge_idx2faces, lambda i,e:e[i], (1,0), (num_faces,)*2)
    block = group(edge_idx2faces)
    multi_adjacency_faces = []
    for i, j in block:
        if j > i + 1:
            multi_adjacency_faces.append(edge_idx2faces[i])

    h = graph(num_faces, multi_adjacency_faces)
    return h.adjacency_list()'''








def _test_SPQR_tree_for_c2d2d3_planar():
    from BC_tree import _test_spqr_tree_data
    from Boyer_Myrvold_planarity_test import Boyer_Myrvold_planarity_test
    
    gs, ans = _test_spqr_tree_data()
    for g, a in zip(gs, ans):
        if not is_c2d2d3_planar(g): continue
        g = graph(Boyer_Myrvold_planarity_test(g))
        x = SPQR_tree_for_c2d2d3_planar(g)
        if not a == x:
            print(a)
            print(x)
        assert a == x




##############################################################
'''
class _R_rect:
    def __init__(self, rect_type, xL, xR, yT, yH, rotation, shift, bends, data)
class _S_rect:
    def __init__(self, rect_type, xL, xR, yL, yH, rotation, shift, data)
class _rect:
    def __init__(self, rect_type, xL, yH, rotation, shift, data)

def _bc_node_order(node): pass
def orthogonal_drawing_of_sub_bc_tree(node):
    n = _bc_node_order(node)
    while n < 3 and _num_bc_tree_son(node) == 1:
        node, = _bc_tree_son(node)
    assert n != 2
    if n == 1:
        rect = []
        for son in _bc_tree_son(node):
            rect.append[orthogonal_drawing_of_sub_bc_tree(node)]
        assert len(rect) == 2
        r0, r1 = rect
        rect_type = 'bc_cut'
        xL = sum(-1 + r[_rect_xL_idx] for r in rect) + 1
        yH = max(r0[_rect_xL_idx], r1[_rect_xL_idx]+1)
        rotation = 0
        shift = (0,0)
        r0.shift = (r1.xL - 1, 0)
        r1.shift = (0, 1)
        data = [_bc_tree_cut_node2vertex(node), r0, r1]
        return _rect(rect_type, xL, xH, rotation, shift, data)
    else:
        spqr_tree = _spqr_tree(node)
        income_vertex = _bc_tree_cut_node2vertex(_bc_tree_parent(node))
        return orthogonal_drawing_of_spqr_tree(spqr_tree, income_vertex)
        
'''




def RS_tree_for_c2d2d3_planar(G_c2d2d3, spqr, rooted_spqr_tree):
    g = G_c2d2d3
    node2type
    node2planar_subgraph
    node2parent_node_uedge
    node_dedge2child_node_st
    root
    #node_vtx2gph_vtx
class rs_tree:
    def is_virtual(self, node, dedge):
        return self.node_dedge2child_node_st[node][dedge] != None





'''
V for vertex
O for bend pt
. for exteranl edge
# for non-virtual edge
~ for omited items
B for possible bend pt of ---t


f for 'flip'
+n for anticlockwise rotate n*pi/2
<> ^ for s->t direction

R
  ______
 |  _   |
 |_|R|__|
...s-t..B...
   .|__|.
   .    .
   .    .



S
   ______
  |  _   |
  |_|S|__|
s###V-V##B###t
    #|__|#
    #    #
    s    t

RS
  _______
 |  __   |
 |_|RS|__|
...s--t..B...
   .|___|.
   .     .
   .     .

R
   
    V
   /|\      O---V---O
  / | \     |   |   |
 /  |  \    |   |   |
s---V---t   s---V---t


O---V-------O
|   |       |
|   V---O   |
|   |   |   |
|   V---V   |
|   |   |   |
|   V---V   |
|   |   |   |
|   V---V   |
|   |   |   |
s---V---V---t



O---V-------------------O
|   |                   |
|   V---------------O   |
|   |               |   |
|   V-----------O   |   |
|   |           |   |   |
|   V-------O   |   |   |
|   |       |   |   |   |
|   V---O   |   |   |   |
|   |   |   |   |   |   |
s---V---V---V---V---V---t



O---V---O
|   |   |


 f+2<
  -V-----V-----V- +3>
 |S|     |     |S|
  -V    -V     V- 
   |   |S|     |
   |    -V +1^ |
   |     |     |
   |     ~     |
   |           |
   |           |
   |           t...
   |           |
   |     V~~~V-V
   |     |   |S|
...s---V-V    -
       |S|   +2<
        -



   V---O
   |   |
~~~V~~~V~~~


   ~~~~V-V---V
   ~   |S|   | `
   ~    -    |  `
   ~         |   ` 
~~~V~~~~~~~~~V~~~ `
                   `   if no this S then lookup
                   V---V-
                   |   |S| +3>
             V~~~V-V   V-
f+2<         |   |S|   |
  -V---V---V-V    -    |
 |S|       |S|  +2<    |
  -V        -          |
   |                   |
~~~V~~~~~~~~~~~~~~~~~~~V~~~



S


n(S) == 3
s###V###t
    #
    s

n(S) == 4
     _ +0>
    |R|
s###V-V###t
    #
    s

n(S) == 5
s###V###V
    #   #
    s   V###t


     _ +0>
    |R| 
s###V-V###V###t
    #
    s


     _ +0>
    |R|
    V-V###t
    #
s###V
    #
    s

n(S) > 5

     _ +0>
    |R|
    V-V~~~###V- +3>
    #        |R|
    ~        V-
    ~        ~
    V- f+0^  ~
    |R|      ~
s###V-       O###t
    #
    s

RS
(1,2) :: n(RS) == 3
   V###O
   #   #
...s###t...
   .
   .

(2,2) :: n(RS) == 4
   V###t...
   #   #
...s###V
   .
   .

(1,3) :: n(RS) == 4

   V###V
   #   #
...s###t...
   .
   .
    _
   |R|
   V-V###O
   #     #
...s#####t...
   .
   .

(2,3) :: n(RS) == 5
    _
   |R|
   V-V###t...
   #     #
...s#####V
   .
   .

(1,4) :: n(RS) == 5
    _
   |R|
   V-V###V
   #     #
...s#####t...
   .
   .

   V###V-
   #   |R|
   #   V-
   #   #
...s###t...
   .
   .

(3,3) :: n(RS) == 6
    _
   |R|
   V-V###t...
   #     #
...s###V-V
   .   |R|
   .    -
   
(1,2) a bend
(1,3) may a bend
(2,2) or (2,3) or (3,3), put t on the upright corner
n(RS,up_half) >= 4

        _ +0>
 f+2<  |R|
  -V~~~V-V~~~~~~###V-
 |R|               |R| +3>
  -V               V-
   ~               ~
   #               #
...s###~~~V-V~~~###t...
   .      |R|
   .       - +2<

'''


def orthogonal_drawing_of_c1d1d2d3_planar(G_c1d1d2d3):
    # G to BC_tree, rooted by block_node bcr with n == 2
    # otherwise G is a R since d <= 3

    g = G_c1d1d2d3
    assert is_c1d1d2d3(g)
    
    bc = bc_tree(g)
    for node, subgph in enumerate(bc.bc_node2subgraph):
        if subgph.nv() > 2:
            break
    else:
        return orthogonal_drawing_of_c1d1d2d3_tree(g, bc)

    b2_root = node
    rooted_bc_tree = DFS_tree(b2_root, bc.bc_tree)
    
    sub_bc_tree_drawings = [None]*rooted_bc_tree.nv()
    bc_env = (g, bc, rooted_bc_tree, sub_bc_tree_drawings)
    for updown, bc_node in rooted_bc_tree:
        if updown == up_from:
            orthogonal_drawing_of_sub_bc_tree(bc_env, bc_node)
    orthogonal_drawing_of_bc_tree(bc_env)
    
    
    return calc_xy(bc_env, sub_bc_tree_drawings)

def orthogonal_drawing_of_c1d1d2d3_tree(g, bc):
    for node, subgph in enumerate(bc.bc_node2subgraph):
        # find a leaf
        if subgph.nv() == 1 and len(bc.bc_tree.neighbors(node)) == 1:
            break
    else:
        assert g.nv() == 1
        return ((0,0))

    cut_leaf_root = node
    rooted_bc_tree = DFS_tree(cut_leaf_root, bc.bc_tree)
    
    sub_bc_tree_drawings = [None]*rooted_bc_tree.nv()
    bc_env = (g, bc, rooted_bc_tree, sub_bc_tree_drawings)
    for updown, bc_node in rooted_bc_tree:
        if updown == up_from:
            orthogonal_drawing_of_sub_bc_tree(bc_env, bc_node)
    orthogonal_drawing_of_sub_bc_tree(bc_env, cut_leaf_root)
    
    return calc_xy(bc_env, sub_bc_tree_drawings)
def orthogonal_drawing_of_sub_bc_tree(bc_env, bc_node):
    (g, bc, rooted_bc_tree, sub_bc_tree_drawings) = bc_env
    if bc.is_cut_node(bc_node):
        c_node = bc_node
        cs = rooted_bc_tree.children(c_node)
        if len(cs) == 2:
            # c ->[b2, b2]
            for a in cs: assert bc.is_nv2_block_node(a)
            a, b = cs
            ar = sub_bc_tree_drawings[a].rect
            ar.shift = (0, -ar.yH-1)
            xL = ar.xL
            br = sub_bc_tree_drawings[b].rect
            br.shift = (ar.xR+1, 0)
            yH = br.yH
            xR = br.xR + br.shift[0]
            yL = min(ar.yL + ar.shift[1], br.yL)
            sub_bc_tree_drawings[c_node] = c_node_data(c_node, (a,b), (xL, xR, yL, yH))
            return
        
        assert len(cs) == 1
        a, = cs
        assert bc.is_block_node(a)
        ar = sub_bc_tree_drawings[a].rect
        xL, xR, yL, yH = ar.xL, ar.xR, ar.yL, ar.yH
        
        if not bc.is_nv2_block_node(a): # do nothing
            # c -> [b3]
            ar.shift = (0, 0)
            sub_bc_tree_drawings[c_node] = c_node_data(c_node, (a,), (xL, xR, yL, yH))
            return

        # c -> [b2]
        if ar.xL < 0:
            ar.shift = (1, 0)
            xL += 1
            xR += 1
        elif ar.yH > 0:
            ar.shift = (0, -1)
            yH -= 1
            yL -= 1
        elif ar.xR < -ar.yL:
            ar.shift = (1, 0)
            xR += 1
        else:
            ar.shift = (0, -1)
            yL -= 1
        sub_bc_tree_drawings[c_node] = c_node_data(c_node, (a,), (xL, xR, yL, yH))
        return

    # b2 or b3
    assert bc.is_block_node(bc_node)
    b_node = bc_node
    b_g = bc.bc_node2subgraph[b_node]
    if bc.is_nv2_block_node(b_node): # nothing happen
        # b2 -> [c]
        cs = rooted_bc_tree.children(b_node)
        assert len(cs) == 1
        a, = cs
        ar = sub_bc_tree_drawings[a].rect
        ar.shift = (0,0) 
        xL, xR, yL, yH = ar.xL, ar.xR, ar.yL, ar.yH
        sub_bc_tree_drawings[b_node] = b2_node_data(b_node, (a,), (xL, xR, yL, yH))
        return
    

    # b3 (all cs in internal)

    # calc incoming vtx
    p = rooted_bc_tree.parent(b_node)
    assert bc.is_cut_node(p)
    p_vtx, = bc.bc_node2gph_vtc[p]
    for node, sub_vtx in bc.gph_vtx2bc_node_vtc[p_vtx]:
        if node == b_node: break
    else:
        raise 'logic error'
    root_bc_vtx_of_spqr = sub_vtx

    
    children, data = orthogonal_drawing_of_block_node(bc_env, b_node, root_bc_vtx_of_spqr)
    assert sorted(children) == rooted_bc_tree.children(b_node)

    
    dr = data.rect
    (xL, xR, yL, yH) = dr.xL, dr.xR, dr.yL, dr.yH
    sub_bc_tree_drawings[b_node] = b3_node_data(b_node, children, (xL, xR, yL, yH), data)
    return


def _place_S(s_nv):
    '''     nb
         |-------|
         |       |nc 
       na|       |_______nd
         |
         |
         na + nb + nc + nd + 1 == nv
         nd == 1
         nc + 1 >= na >= nb >= nc
         nc = (nv-2)//3
         na = nv//3
         nb = (nv-1)//3
    '''

    nv = s_nv
    na, nb, nc, nd = num_edges_list = (nv//3, (nv-1)//3, (nv-2)//3, 1)
    assert sum(num_edges_list) == nv - 1
    corner_vtc = (0, na, na+nb, na+nb+nc, nv-1)
    return num_edges_list, corner_vtc


def S_node2dedge_vtx_ls(spqr, begin_b_vtx):
    (s_node, begin_s_node_vtx), = spqr.gph_vtx2spqr_node_vtc[begin_b_vtx]
    s_g = spqr.spqr_node2subgraph[s_node]
    dedge2edge = s_g.dedge2edge()
    
    u = begin_s_node_vtx
    u2v_dedge, _ = s_g.dedges(u)
    v = dedge2edge[u2v_dedge][1]
    dedge_vtx_ls = [(u2v_dedge, v)]
    while v != upleft_s_node_vtx:
        x2v = s_g.next_in(u2v_dedge)
        v2x = s_g.flip_dedge(x2v)
        x = dedge2edge[v2x][1]
        u, u2v_dedge, v = v, v2x, x
        dedge_vtx_ls.append((u2v_dedge, v))
    return dedge_vtx_ls


def _build_rs(bc_env, b_node, b_upleft_vtx):
    (_, bc, rooted_bc_tree, _) = bc_env
    b_g = bc.bc_node2subgraph[b_node]

    spqr = spqr_tree(b_g, SPQR_tree_for_c2d2d3_planar)
    (s_root, s_upleft_vtx), = spqr.gph_vtx2spqr_node_vtc[b_upleft_vtx]
    assert spqr.is_S_node(s_root)
    
    rooted_spqr_tree = rooted_tree(s_root, spqr.spqr_tree)
    rs = rs_tree(b_g, spqr, rooted_spqr_tree)
    return rs
def orthogonal_drawing_of_block_node(bc_env, b_node, b_upleft_vtx):
    rs = _build_rs(bc_env, b_node, b_upleft_vtx) # a rooted tree

    n = rs.tree.nv()
    subgph_st = [None]*n
    subgph_ordering = [None]*n
    subgph_drawing = [None]*n
    rs_env = bc_env, (rs, subgph_st, subgph_ordering, subgph_drawing)

    # calc_children_st
    (root, rs_upleft_vtx), = rs.gph_vtx2node_vtc(b_upleft_vtx)
    assert root == rs.tree.root()
    subgph_st[root] = calc_root_st(rs, root, rs_upleft_vtx)
    
    calc_children_st(rs_env, root)
    for updown, node in rs.tree:
        if updown == down_to:
            calc_children_st(rs_env, node)

    c_children = []
    for updown, node in rs.tree:
        if updown == up_from:
            c_children += orthogonal_drawing_of_sub_rs_tree(rs_env, node)
    c_children += orthogonal_drawing_of_sub_rs_tree(rs_env, root)

    (x, y) = _calc_xy_of_upleft_corner(rs_env, root, rs_upleft_vtx)
    assert x == 0 and y >= 0
    
    sr = subgph_drawing[root].rect
    sr.shift = (-x, -y)

    (xL, xR, yL, yH) = (sr.xL, sr.xR, sr.yL, sr.yH)
    yL -= y
    yH -= y
    assert yL < 0 <= yH
    
    data = rs_node_data((xL, xR, yL, yH), subgph_drawing)
    return c_children, data

    '''
    s_g = spqr.spqr_node2subgraph[s_root]

    # build s_root_dedge_vtx_ls
    s_root_dedge_vtx_ls = S_node2dedge_vtx_ls(spqr, upleft_b_node_vtx)

    # calc s,t of s_root,  st_P_node
    num_edges_list, corner_vtc = _place_S(s_g.nv())
    upleft_corner = corner_vtc[1]
    t2s_loc = -1-upleft_corner-1 + len(s_root_dedge_vtx_ls)
    t2s_dedge, s = s_root_dedge_vtx_ls[t2s_loc]
    _,         t = s_root_dedge_vtx_ls[t2s_loc-1]
    st_uedge = s_g.to_uedge(t2s_dedge)
    if spqr.is_virtual_edge(s_root, st_uedge):
        st_P_node = spqr.spqr_node_uedge2spqr_node_uedges[s_root][0]
    else:
        st_P_node = None
    
    
    


    #######
    spqr_node_st = [None]*spqr.spqr_order
    spqr_node_vtc_ordering = [None]*spqr.spqr_order
    sub_spqr_tree_drawings = [None]*spqr.spqr_order
    spqr_env = bc_env, (spqr, rooted_spqr_tree, \
                        spqr_node_st, spqr_node_vtc_ordering, sub_spqr_tree_drawings)

    # calc_spqr_child_node_st
    spqr_node_st[s_root] = (s,t)
    if st_P_node != None: spqr_node_st[st_P_node] = (t,s)
    calc_spqr_child_node_st(spqr_env, s_root)
    for updown, spqr_node in rooted_spqr_tree:
        if updown == down_to:
            calc_spqr_child_node_st(spqr_env, spqr_node)

    c_children = []
    for updown, spqr_node in rooted_spqr_tree:
        if updown == up_from:
            c_children += orthogonal_drawing_of_sub_spqr_tree(spqr_env, spqr_node)
    c_children += orthogonal_drawing_of_sub_spqr_tree(spqr_env, s_root)
    if st_P_node != None: _concat(spqr_env, s_root, st_P_node)

    (x, y) = _calc_xy_of_upleft_corner(spqr_env, s_root, upleft_s_node_vtx)
    sr = sub_spqr_tree_drawings[s_root].rect
    sr.shift = (-x, -y)
    assert x == 0 and y >= 0

    (xL, xR, yL, yH) = (sr.xL, sr.xR, sr.yL, sr.yH)
    yL -= y
    yH -= y
    assert yL < 0 <= yH
    
    data = spqr_node_data((xL, xR, yL, yH), sub_spqr_tree_drawings)
    return c_children, data
    

def is_P(spqr_env, spqr_node)
def is_S(spqr_env, spqr_node)
def is_R(spqr_env, spqr_node)
def is_P2S(spqr_env, spqr_P_node)
def is_P2R(spqr_env, spqr_P_node)
def is_P2RS(spqr_env, spqr_P_node)
def is_P2RSS(spqr_env, spqr_P_node)
def is_S_root(spqr_env, spqr_node)
def P2children(spqr_env, spqr_P_node)
def get_st(spqr_env, spqr_node)
def calc_spqr_child_node_st(spqr_env, spqr_node):
    bc_env, (spqr, rooted_spqr_tree, spqr_node_st, \
             spqr_node_vtc_ordering, sub_spqr_tree_drawings)\
             = spqr_env
    if not is_P(spqr_env, spqr_node):
        if not is_S_root(spqr_env, spqr_node): return
        s_root = spqr_node
        calc_S_spqr_child_node_st(spqr_env, spqr_node)
        return

    st = get_st(spqr_env, spqr_node)
    children = P2children(spqr_env, spqr_node)
    if is_P2S(spqr_env, spqr_node):
        S, = children
        put_st(spqr_env, S, st)
        calc_S_spqr_child_node_st(spqr_env, S)
        return
    elif is_P2R(spqr_env, spqr_node):
        R, = children
        put_st(spqr_env, R, st)
        calc_R_spqr_child_node_st(spqr_env, S)
        return
        
        
    s,t = 
    
'''

class _st:
    def __init__(self, child_st, fr, parent_dedge_st_flip):
        self.st = child_st # s, t
        self.fr = fr # child_flip, child_rotation
        self.parent_dedge_st_flip = parent_dedge_st_flip # parent_dedge, parent_dedge_flip
        
def calc_children_st(rs_env, node):
    bc_env, (rs, subgph_st, subgph_ordering, subgph_drawing) = rs_env
    
    if rs.is_R(node):
        calc_children_st_of_R(rs_env, node)
    elif rs.is_S(node):
        calc_children_st_of_S(rs_env, node)
    elif rs.is_RS(node):
        calc_children_st_of_RS(rs_env, node)
    else:
        raise 'logic error'

def new_dedges_for_v0(R_g, v0, v02cs):#(u0,u02u1,u1),
    assert len(v02cs) == 0
    u0, u1 = v0
    u02u1 = R_g.edge2dedge(u0, u1)
    return (u0,u02u1,u1),
def new_dedges_for_vk(R_g, vk, vk2cs):#(cL,cL2vk[0],vk[0]), ..., (vk[-1],vk[-1]2cR,cR)
    assert len(vk2cs) == 2
    vL = vk[0]
    vR = vk[-1]
    vL2cL, cL = vk2cs[0]
    vR2cR, cR = vk2cs[-1]
    cL2vL = R_g.flip_dedge(vL2cL)
    
    ls = [(cL, cL2vL, vL)]
    v2u = cL2vL
    while v2u != vR2cR:
        v2u = R_g.flip_next_in(v2u)
        v, u = R_g.dedge2edge(v2u)
        ls.append((v, v2u, u))

    assert len(ls) == len(vk)+1
    assert ls[0][-1] == vL
    assert ls[-1][0] == vR
    return ls
def new_dedges_for_vn(R_g, vn, vn2cs):#(s,s2vn,vn), (vn,vn2?,?), (vn,vn2t,t)
    assert len(vn2cs) == 3

    vn, = vn
    vn2s, s = vn2cs[0]
    s2vn = R_g.flip_dedge(vn2s)
    res = ((s,s2vn,vn),) + tuple((vn,vn2x,x) for vn2x,x in vn2cs[1:])
    return res
    
def calc_new_dedges_vk_ls(R_g, vk_ls, vk2cs_ls):
    new_dedges = [new_dedges_for_v0(R_g, vk_ls[0], vk2cs_ls[0])]
    for vk, vk2cs in zip(vk[1:-1], vk2cs_ls[1:-1]):
        assert len(vk2cs) == 2
        new_dedges.append(new_dedges_for_vk(R_g, vk, vk2cs))
    new_dedges.append(new_dedges_for_vn(R_g, vk_ls[-1], vk2cs_ls[-1]))
    return new_dedges

def color(rs, subgph_st, node, fr, parent_dedge_st_flip):
    st_flip, parent_dedge = parent_dedge_st_flip
    if rs.is_virtual(node, parent_dedge) != None:
        s2t = parent_dedge
        if st_flip:
            s2t = rs.node2planar_subgraph[node].flip_dedge(parent_dedge)
        child, sub_st = rs.node_dedge2child_node_st[node][s2t]
        subgph_st[child] = _st(sub_st, fr, parent_dedge_st_flip)
def calc_children_st_of_R(rs_env, node):
    bc_env, (rs, subgph_st, subgph_ordering, subgph_drawing) = rs_env
    R = node

    R_g = rs.node2planar_subgraph[R]
    s, t = subgph_st[R]
    vk_ls, vk2cs_ls = left_most_canonical_ordering(s, t, R_g)

    new_dedges_ls = calc_new_dedges_vk_ls(R_g, vk_ls, vk2cs_ls)
    subgph_ordering[R] = vk_ls, vk2cs_ls, new_dedges_ls
    
    # st_flip, (child_flip, child_rotaion)
    ts2 = True, (False, 2)
    tsf2 = True, (True, 2)
    st3 = False, (False, 3)
    ts1 = True, (False, 1)


    st_flip, fr = ts2
    for dedges in new_dedges_ls[1:]:
        for t, t2s, s in dedges: #reverse
            color(rs, subgph_st, R, fr, (t2s,st_flip))

    st_flip, fr = tsf2
    for dedges in new_dedges_ls[2:]:
        t, t2s, s = dedges[0]
        color(rs, subgph_st, R, fr, (t2s,st_flip))

    st_flip, fr = st3
    for dedges in new_dedges_ls[2:]:
        s, s2t, t = dedges[-1]
        color(rs, subgph_st, R, fr, (s2t,st_flip))

    st_flip, fr = ts1
    dedges = new_dedges_ls[-1]
    t, t2s, s = dedges[1]
    color(rs, subgph_st, R, st_flip, t2s, fr)


        
def S_node_ordering(s, t, S_g):#[(s,s2s',s')], [(s',s'2?,?)...(..upleft)],[...], [...], [(t',t'2t,t)],[(t,t2s,s)]
    num_edges_list, corner_vtc = _place_S(S_g.nv())
    assert len(corner_vtc) == 5
    
    L0, L1 = _circle_st(s, t, S_g)
    assert len(L0) == 1
    
    n = len(L1)
    cuts = list(corner_vtc)
    assert cuts[-1] == n == S_g.nv() - 1
    for i in range(1, len(cuts)):
        cuts[i-1] = (cuts[i-1], cuts[i])
    cuts.pop()
    
    L1 = tuple(L1[i:j] for i,j in cuts)

    (s,s2t,t), = L0
    t2s = S_g.flip_dedge(s2t)
    L0 = (t,t2s,s),
    res = (L0,) + L1
    assert len(res) == 5
    return res

def fix_S_node_ordering(rs, S, new_dedges_ls):
    ls = list(new_dedges_ls)
    assert not rs.is_virtual(S, ls[0][0][1])
    assert not rs.is_virtual(S, ls[-2][0][1])

    def inc(i):
        assert len(ls[i+1])
        ls[i] += ls[i+1][0:1]
        ls[i+1] = ls[i+1][1:]
    if rs.is_virtual(S, ls[0][-1][1]):
        inc(0)
    assert not rs.is_virtual(S, ls[0][-1][1])

    if (not len(ls[1])) and len(ls[2]):
        inc(1)
    
    if len(ls[2]) and rs.is_virtual(S, ls[1][-1][1]):
        inc(1)
    assert len(ls[1]) == 0 or len(ls[2]) == 0 or not rs.is_virtual(S, ls[1][-1][1])

    if rs.node2planar_subgraph[S].nv() == 5:
        if len(ls[2]) and rs.is_virtual(S, ls[2][-1][1]):
            assert len(ls[0]) == len(ls[1]) == len(ls[2]) == 1
            if S != rs.root():
                inc(0)
                inc(1)

    assert not rs.is_virtual(S, ls[0][-1][1])
    assert len(ls[1]) or len(ls[2]) == 0
    assert len(ls[2]) == 0 or not rs.is_virtual(S, ls[1][-1][1])
    
    return tuple(ls)
        
    
def calc_children_st_of_S(rs_env, node):
    bc_env, (rs, subgph_st, subgph_ordering, subgph_drawing) = rs_env
    S = node
    S_g = rs.node2planar_subgraph[S]
    s, t = subgph_st[S]
    new_dedges_ls = S_node_ordering(s, t, S_g)
    new_dedges_ls = fix_S_node_ordering(rs, S, new_dedges_ls)            
    subgph_ordering[R] = new_dedges_ls

    # st_flip, (child_flip, child_rotaion)
    stf0 = False, (True, 0)
    st0 = False, (False, 0)
    st3 = False, (False, 3)
    state = [stf0, st0, st3]

    for (st_flip, fr), dedges in zip(state, new_dedges_ls):
        for s, s2t, t in dedges:
            color(rs, subgph_st, R, fr, (s2t,st_flip))


def _circle_st(s, t, RS_g):
    faces = fake_face(RS_g)
    circle, = faces.face2circle_vtc
    s_idx = circle.index(s)
    t_idx = circle.index(t)

    L = len(circle)
    dedges, = faces.face2dedges
    dedges += dedges
    if s_idx < t_idx:
        s0_idx, t0_idx = s_idx, t_idx    # <
        s1_idx, t1_idx = s_idx+L, t_idx  # > > 0
    else:
        s0_idx, t0_idx = s_idx, t_idx+L   # <
        s1_idx, t1_idx = s_idx+L, t_idx+L # > > 0
        
    st0 = dedges[s0_idx:t0_idx]
    st1 = dedges[s1_idx-1:t1_idx-1:-1]
    st1 = tuple(RS_g.flip_dedge(d) for d in st1)

    if len(st0) > len(st1):
        st0, st1 = st1, st0

    f = lambda dedge:(RS_g.dedge2edge[0], dedge, RS_g.dedge2edge[1])
    res = tuple(tuple(f(d) for d in sti) for sti in (st0, st1))
    assert res[0][0][0] == s == res[1][0][0]
    assert res[0][-1][-1] == t == res[1][-1][-1]

    return res
        
    
    
def RS_node_ordering(s, t, RS_g):#[(s...)...(...t)], [(s...)...], [...], [...(...t)], 
    L0, L1 = _circle_st(s, t, RS_g)
    n = len(L1)
    cuts = [0, (n+1)//3, n//3, (n+2)//3]
    assert sum(cuts) == n
    for i in range(1, len(cuts)):
        cuts[i] += cuts[i-1]
        cuts[i-1] = (cuts[i-1], cuts[i])
    cuts.pop()
    L1 = tuple(L1[i:j] for i,j in cuts)
    res = (L0,) + L1
    assert len(res) == 4
    return res
    

def fix_RS_node_ordering(rs, RS, new_dedges_ls):
    ls = list(new_dedges_ls)
    assert not rs.is_virtual(RS, ls[0][0][1])
    assert not rs.is_virtual(RS, ls[0][-1][1])
    assert not rs.is_virtual(RS, ls[1][0][1])
    assert not rs.is_virtual(RS, ls[-1][-1][1])

    def inc(i):
        assert len(ls[i+1])
        ls[i] += ls[i+1][0:1]
        ls[i+1] = ls[i+1][1:]

    L0 = len(ls[0])
    L1 = sum(len(es) for es in ls[1:])
    assert L0 <= L1
    if 2 <= L0 and L1 <= 3:
        inc(2)
        assert len(ls[-1]) == 0
        #inc(-1)
        ls[-1] += ls[0][-1:]
        ls[0] = ls[0][:-1]
    elif 1 == L0 and L1 <= 3:
        pass
    else:
        assert L1 >= 4
        if len(ls[2]) and rs.is_virtual(RS, ls[2][-1][1]):
            inc(2)
        assert not rs.is_virtual(RS, ls[2][-1][1])


    assert len(ls[2]) == 0 or not rs.is_virtual(S, ls[2][-1][1])
    
    return tuple(ls)

def calc_children_st_of_RS(rs_env, node):
    bc_env, (rs, subgph_st, subgph_ordering, subgph_drawing) = rs_env
    RS = node
    RS_g = rs.node2planar_subgraph[RS]
    s, t = subgph_st[RS]
    new_dedges_ls = RS_node_ordering(s, t, RS_g)
    subgph_ordering[RS] = new_dedges_ls

    # st_flip, (child_flip, child_rotaion)
    ts0 = True, (False, 0)
    tsf2 = True, (True, 2)
    st0 = False, (False, 0)
    st3 = False, (False, 3)
    state = [ts0, tsf2, st0, st3]

    for (st_flip, fr), dedges in zip(state, new_dedges_ls):
        for _, d, _ in dedges:
            color(rs, subgph_st, R, fr, (d,st_flip))


def orthogonal_drawing_of_sub_rs_tree(rs_env, node):
    bc_env, (rs, subgph_st, subgph_ordering, subgph_drawing) = rs_env
    
    if rs.is_R(node):
        orthogonal_drawing_of_sub_rs_tree_rooted_by_R(rs_env, node)
    elif rs.is_S(node):
        orthogonal_drawing_of_sub_rs_tree_rooted_by_S(rs_env, node)
    elif rs.is_RS(node):
        orthogonal_drawing_of_sub_rs_tree_rooted_by_RS(rs_env, node)
    else:
        raise 'logic error'


class _pt:
    def __init__(self, x,y):
        self.x, self.y = x,y
        
    @staticmethod
    def f(x,y):return y,x
    @staticmethod
    def r(x,y):return -y,x
    @staticmethod
    def rn(x,y,n):
        n %= 4
        if n < 0: n += 4
        for _ in range(n):
            x, y = r(x, y)
        return x,y
    @staticmethod
    def fs(xy_ls):return tuple(f(x,y) for x,y in xy_ls)
    @staticmethod
    def rns(xy_ls,n):return tuple(rn(x,y,n) for x,y in xy_ls)
    def flip(self):
        self.x, self.y = f(self.x, self.y)
    def rotate(self, n):
        return rn(self.x, self.y, n)
    def __iadd__(self, shift):
        dx, dy = shift
        self.x += dx
        self.y += dy
        

class _rect:
    def __init__(self, xLRyLH = None):
        if xLRyLH == None:
            xLRyLH = None, None, None, None
        self.xL, self.xR, self.yL, self.yH = xLRyLH
    def bound(self):
        return self.xL, self.xR, self.yL, self.yH
    def __iadd__(self, shift):
        dx, dy = shift
        self.xL += dx
        self.xR += dx
        self.yL += dy
        self.yH += dy
    def flip(self):
        ps = (self.xL, self.yL), (self.xR, self.yH)
        ps = list(_pt.f(p) for p in ps)
        (self.xL, self.yL), (self.xR, self.yH) = ps
    def rotate(self,n):
        ps = (self.xL, self.yL), (self.xR, self.yH)
        ps = list(_pt.rn(p,n) for p in ps)
        (self.xL, self.yL), (self.xR, self.yH) = ps
            

        


class _vtx_info(_rect):
    def __init__(self, xLRyLH = None, \
                 xLxRdx_based_vtx = None, \
                 dxyx = None):
        _rect.__init__(self, xLRyLH)
        if xLxRdx_based_vtx == None:
            xLxRdx_based_vtx = None, None, None
        if dxyx == None:
            dxyx = None, None, None
        self.xL_based_vtx, self.xR_based_vtx, self.dx_based_vtx = xLxRdx_based_vtx
        self.dx, self.y, self.x = dxyx

        assert self.xL <= 0 <= self.xR and self.yL <= 0 <= self.yH

        
    def __iadd__(self, dshift):
        _rect.__init__(self, dshift)
        '''
        if self.xL > 0: self.xL = 0
        if self.xR < 0: self.xR = 0
        if self.yL > 0: self.yL = 0
        if self.yH < 0: self.yH = 0
        #'''
    def based_vtx(self):
        return self.xL_based_vtx, self.xR_based_vtx, self.dx_based
    def dxyx(self):
        return self.dx, self.y, self.x

class _rect_view(_rect):
    def __init__(self, xLRyLH, tb_xy):
        _rect.__init__(self, xLRyLH)
        self.xLRyLH, self.tb_xy = xLRyLH, tb_xy
        self.xL, self.xR, self.yL, self.yH = xLRyLH
        self.t_xy, self.b_xy = tb_xy # b is a possible bend for t
        (self.tx, self.ty), (self.bx, self.by) = tb_xy

class _rect_data(_rect_view): # s or s' = (0,0) ===> flip => rotation => shift
    def __init__(self, xLRyLH, tb_xy, st_fr, dshift = None):
        if dshift == None: dshift = (0,0)
        _rect_view.__init__(self, xLRyLH, tb_xy)
        self.st_fr, self.dshift = st_fr, dshift
        # b is a possible bend for t
        (self.s,self.t), (self.flip, self.rotation) \
                         = (s,t), (flip, rotation) = st_fr

        xL, xR, yL, yH = xLRyLH
        (tx, ty), (bx, by) = tb_xy
        ps = (xL, yL), (xH, yH), (tx, ty), (bx, by)
        r = _rect.(xLRyLH)
        if flip:
            ps = _pt.fs(ps)
        ps = _pt.rns(ps,n)

        (xL, yL), (xH, yH), (tx, ty), (bx, by) = ps
        self.parent_view = _rect_view((xL, xR, yL, yH), ((tx, ty), (bx, by)))

def _vn_mid_down_line_of_R(subgph_drawing, rs, node, info, dedges):
    _child = lambda dedge: rs.node_dedge2child_node_st[node][dedge]
    assert len(dedges) == 3

    s, s2v, _ = dedges[0]
    v, v2u, u = dedges[1]
    iu = info[u]

    iv = info[v]
    _y = iu.y + iu.yH + 1
    child_st = _child(v2u)
    if child_st == None:
        #_iv = _vtx_info((0,0,0,0), base, (dx_to_u + dx_u2xL, u_y, None))
        _v_y = _y
        dx = 0
    else:
        child, _ = child_st
        cr = subgph_drawing[child].rect
        view = cr.parent_view
        
        dy = max(0, -view.yL) + max(0, view.yH) + 1
        _v_y = _y + dy
        _fix_xL_xR(info, u, view.xL, view.xR)
        dx = -view.tx
        

    h_yL = info[v].y
    su_width, su_yH = _cut_and_dx_yH_of(info, s, u)
    shift_y1 = su_yH - h_yL + 1
    shift_y2 = _v_y - info[v].y
    shift_y = max(shift_y1, shift_y2, 0)
    iv.y += shift_y

    assert iu.dx_base_vtx == s
    ddx_of_v = su_width - dx - iv.dx
    assert ddx_of_v >= 0
    iv += (-ddx_of_v, 0)
    iv.dx += -ddx_of_v

    xR_root = iu.xR_base_vtx
    base = (v, xR_root, v)
    iu = info[u] = _vtx_info(iu.bound(), base, (dx, iu.y, None))
    assert iu.dx_base_vtx == iu.xL_base_vtx
    if xR_root != u:
        ixR = info[xR_root]
        assert ixR.dx_base_vtx == u == ixR.xL_base_vtx
        ixR.dx += iu.dx
        ixR.xL_base_vtx = ixR.dx_base_vtx = iu.dx_base_vtx





def _vn_last_down_line_of_R(subgph_drawing, rs, node, info, dedges):
    _child = lambda dedge: rs.node_dedge2child_node_st[node][dedge]
    assert len(dedges) == 3

    #s, s2v, _ = dedges[0]
    v, v2u, u = dedges[1]
    _, v2t, t = dedges[2]
    it = info[t]
    xL_root = it.xL_base_vtx
    xR_root = it.xR_base_vtx
    base = (v, xR_root, v)

    iv = info[v]
    _y = it.y + it.yH + 1
    child_st = _child(v2t)
    if child_st == None:
        _v_y = _y
    else:
        child, _ = child_st
        cr = subgph_drawing[child].rect
        view = cr.parent_view
        
        dy = max(0, -view.yL)
        _v_y = _y + dy
        _fix_xL_xR(info, t, view.xL - view.tx, view.xR - view.tx)
        iv.yH = max(iv.yH, view.yH)
        

    h_yL = info[v].y
    h_width = -iu.dx
    ut_width, ut_yH = _cut_and_dx_yH_of(info, u, t)
    shift_y1 = ut_yH - h_yL + 1
    shift_y2 = _v_y - iv.y
    shift_y = max(shift_y1, shift_y2, 0)
    iv.y += shift_y



def _fix_xL_xR(info, v, up_xL, up_xR):
    iv = info[v]
    
    xL_root = iv.xL_base_vtx
    ixL = info[xL_root]
    if v != xL_root:
        assert iv.dx_base_vtx == xL_root
        up_xL += iv.dx
    ixL.xL = min(ixL.xL, up_xL)

    xR_root = iv.xR_base_vtx
    ixR = info[xR_root]
    if v != xR_root:
        assert ixR.dx_base_vtx == v
        up_xR -= ixR.dx
    ixR.xR = max(ixR.xR, up_xR)

def _dx_v2xL(info, v):
    iv = info[v]
    
    xL_root = iv.xL_base_vtx
    if v != xL_root:
        assert iv.dx_base_vtx == xL_root
        dx = iv.dx
    else:
        dx = 0
    return dx

def _cL_up_line_of_R(subgph_drawing, rs, node, info, dedges):
    _child = lambda dedge: rs.node_dedge2child_node_st[node][dedge]
    u, u2v, v = dedges[0] # u is cL

    iu = info[u]
    xL_root = iu.xL_base_vtx
    base = (xL_root, v, xL_root)
    dx_to_u = 0
    dx_u2xL = _dx_v2xL(info, u)

    u_y = iu.y + iu.yH + 1
    child_st = _child(u2v)
    if child_st == None:
        info[v] = _vtx_info((0,0,0,0), base, (dx_to_u + dx_u2xL, u_y, None))
    else:
        child, _ = child_st
        cr = subgph_drawing[child].rect
        view = cr.parent_view
        #cr.dshift = (-1,0)
        dshift = (-1,0)
        
        dy = max(0, -view.yL)
        y = u_y + dy
        
        dx_to_u = 1 - view.tx
        dx = dx_to_u + dx_u2xL
        
        info[v] = _vtx_info(view.bound(), base, (dx, y, None))
        info[v] += dshift

        _fix_xL_xR(info, u, view.xL - view.tx, view.xR - view.tx)

        

    is_real = child_st == None
    return is_real, info[v].y, dx_to_u


def _cut_and_dx_yH_of(info, begin, end):
    vtc = [end]
    while vtc.top() != begin:
        vtc.append(info[vtc.top()].dx_base_vtx)

    dx = 0
    yH_ls = []
    i = info[vtc.pop()]
    #y_base = i.y
    while vtc:
        v = vtc.pop()
        p, i = i, info[v]
        
        yH_ls.append(i.yH + i.y)# - y_base)

        if i.xL_base_vtx != v:
            _dx = i.dx
        else:
            _dx = max(0, p.xR) + 1 - min(i.xL, 0)
            _dx = max(_dx, i.dx)
        i.dx = dx = dx + _dx
        i.dx_base_vtx = begin
    return dx, max(yH_ls)


def _h_min_width(info, begin, end):
    vtc = [end]
    while vtc.top() != begin:
        vtc.append(info[vtc.top()].dx_base_vtx)

    h_width = 0
    i = info[vtc.pop()]
    while vtc:
        v = vtc.pop()
        p, i = i, info[v]
                
        _dx = max(0, p.xR) + 1 - min(i.xL, 0)
        _dx = max(_dx, i.dx)
        h_width += _dx
    return h_width


def _h_shift_y(info, begin, end, shift_y):
    assert 0 <= shift_y
    vtc = [end]
    while vtc.top() != begin:
        vtc.append(info[vtc.top()].dx_base_vtx)

    for v in vtc:
        info[v].y += shift_y
def _cR_down_line_of_R(subgph_drawing, rs, node, info, dedges, h_width, h_yL):
    _child = lambda dedge: rs.node_dedge2child_node_st[node][dedge]
    
    
    #vkLR_weight = _dx_of(info, dedges[0][-1], dedges[-1][0])
    #vkn_y = info[dedges[-1][0]].y
    cL, cL2vk0, vk0 = dedges[0]
    vkn, vkn2cR, cR = dedges[-1]
    ivkn, icR = info[vkn], info[cR]
    
    info[vkn].xR_base_vtx = info[cR].xR_base_vtx
    child_st = _child(vkn2cR)
    ycR_H = max(0, icR.yH)
    if child_st == None:
        width, height = 0, 1 + ycR_H
        bound = (0,0,0,0)
        #dshift = (-width, height)
        dshift = (0,0) # to vkn
        dx = max(0, ivkn.xR) + 1
    else:
        child, _ = child_st
        cr = subgph_drawing[child].rect
        view = cr.parent_view
        
        width = view.tx
        height = -view.yL + 1 + ycR_H
        #dshift = (-width, height)
        dshift = (1, 0)  # to vkn
        
        bound = view.bound()
        #cr.dshift = dshift
        #icR.xL = min(icR.xL, bound.xL - bound.tx)
        dx = max(0, ivkn.xR) + 1 + width
        ivkn.yH = max(ivkn.yH, bound.yH)
        _fix_xL_xR(info, cR, view.xL - view.tx, view.xR - view.tx)

        

    cLR_width, cLR_yH = _cut_and_dx_yH_of(info, cL, cR)
    shift_y1 = cLR_yH - h_yL + 1
    shift_y2 = icR.y + height - ivkn.y
    shift_y = max(shift_y1, shift_y2, 0)
    _h_shift_y(info, vk0, vkn, shift_y)


    base = (vkn, icR.xR_base_vtx, vkn)
    #dx = 1 + width
    icR = info[cR] = _vtx_info(icR.bound(), base, (dx, icR.y, None))
    dw = h_width + icR.dx - cLR_width
    vx, vx2vkn, _ = dedges[-2]
    if dw >= 0:
        pass
        #icR += dshift
    elif _child(vkn2cR) != None:
        #cr.dshift = (1-dw,0)
        #icR += cr.dshift
        icR.dx += -dw
    elif len(dedges) == 2:
        if _child(cL2vk0) == None:
            # a bend
            bend = (vkn, +0, cR) # rotate +n * pi/2
            icR.dx = -dw
        else:
            #child, _ = _child(cL2vk0)
            #cr = subgph_drawing[child].rect
            #cr.dshift = (-1 + dw,0)
            info[vk0] += (dw, 0)
            info[vk0].dx += -dw    
    elif _child(vx2vkn) == None:
        info[vx].xL += dw
    else:
        #child, _ = _child(vx2vkn)
        #cr = subgph_drawing[child].rect
        #cr.dshift = (dw, 0)
        info[vx] += (dw, 1)
        #info[vx].dx += -dw

    assert icR.dx_base_vtx == icR.xL_base_vtx
    xR_root = icR.xR_base_vtx
    if xR_root != cR:
        ixR = info[xR_root]
        assert ixR.dx_base_vtx == cR == ixR.xL_base_vtx
        ixR.dx += icR.dx
        ixR.xL_base_vtx = ixR.dx_base_vtx = icR.dx_base_vtx
    
def _horizontal_line_of_R(subgph_drawing, rs, node, info, dedges):
    _child = lambda dedge: rs.node_dedge2child_node_st[node][dedge]
    
    yL_ls = [0]
    for u, u2v, v in dedges:
        child_st = _child(u2v)
        base = (v,v,u)
        dx = 1
        if child_st == None:
            info[v] = _vtx_info((0,0,0,0), base, (dx, info[u].y, None))
        else:
            child, _ = child_st
            cr = subgph_drawing[child].rect
            view = cr.parent_view
            #cr.dshift = (0,-1)
            dshift = (0,-1)
            dy = 1 - view.ty
            y = info[u].y + dy
            info[v] = _vtx_info(view.bound(), base, (dx, y, None))
            info[v] += dshift
            yL = info[v].y + info[v].yL
            yL_ls.append(yL)

    last_seg_is_real = True
    if dedges:
        last_seg_is_real = _child(dedges[-1]) == None
    return last_seg_is_real, min(yL_ls)

def _calc_dshift_of_children_of_R(subgph_drawing, rs, node, info, new_dedges_ls)
    _child = lambda dedge: rs.node_dedge2child_node_st[node][dedge]
    bends = []
    def _h_dshift(u2v):
        if _child[u2v]:
            child, _ = _child[u2v]
            cr = subgph_drawing[child].rect
            cr.dshift = (0, -1)
    def _first_up_dshift(u, u2v, v):
        if _child[u2v]:
            child, _ = _child[u2v]
            cr = subgph_drawing[child].rect
            view = cr.parent_view
            dx = info[v].x - info[u].x + view.tx
            cr.dshift = (-dx, 0)
        elif info[v].x != info[u].x:
            bends.append((info[u].x, info[v].y))
        
    def _middle_down_dshift(u, u2v, v):
        if _child[u2v]:
            child, _ = _child[u2v]
            cr = subgph_drawing[child].rect
            view = cr.parent_view
            sy = info[u].y - 1 - view.yH
            dy = info[v].y - sy
            cr.dshift = (0, -dy)
    def _last_down_dshift(u, u2v, v):
        if _child[u2v]:
            child, _ = _child[u2v]
            cr = subgph_drawing[child].rect
            view = cr.parent_view
            dx = info[u].x - info[v].x + view.tx
            cr.dshift = (-dx, 0)
        elif info[v].x != info[u].x:
            bends.append((info[v].x, info[u].y))
    for dedges in new_dedges_ls[1:2]:
        for u, u2v, v in dedges:
            _h_dshift(u2v)
                
    for dedges in new_dedges_ls[2:-1]:
        for u, u2v, v in dedges[0:1]:
            _first_up_dshift(u, u2v, v)
        for u, u2v, v in dedges[1:-1]:
            _h_dshift(u2v)
        for u, u2v, v in dedges[-1:]:
            _last_down_dshift(u, u2v, v)

    for dedges in new_dedges_ls[-1:]:
        for u, u2v, v in dedges[0:1]:
            _first_up_dshift(u, u2v, v)
        for u, u2v, v in dedges[1:-1]:
            _middle_down_dshift(u, u2v, v)
        for u, u2v, v in dedges[-1:]:
            _last_down_dshift(u, u2v, v)

    return bends
def _calc_x_of_R(vtc_info):
    info = vtc_info
    for v in range(len(vtc_info)):
        ls = []
        while info[v].x == None:
            ls.append(v)
            v = info[v].dx_base_vtx
        while ls:
            x_base = info[v].x
            v = ls.pop()
            info[v].x += x_base
class _rs_subgph_drawing_data:
    def __init__(self, rect, vtc_info, bends, others):
        self.rect, self.vtc_info, self.bends, self.others = rect, vtc_info, bends, others
def orthogonal_drawing_of_sub_rs_tree_rooted_by_R(rs_env, node):
    bc_env, (rs, subgph_st, subgph_ordering, subgph_drawing) = rs_env

    st = subgph_st[node]
    s,t = st.st
    R_g = rs.node2planar_subgraph[node]
    vk_ls, vk2cs_ls, new_dedges_ls = subgph_ordering[node]
    info = vtc_info = [None]*R_g.nv()
    
    _h_env = subgph_drawing, rs, node, vtc_info
    
    # embed s -> t
    vtx_info[s] = _vtx_info((0,0,0,0), (s,s,s), (0,0,0))
    h_vk1 = new_dedges_ls[1]
    bend_is_t, R_yL = _horizontal_line_of_R(*_h_env, h_vk1)

    
    ####
    for dedges in new_dedges_ls[2:-1]:
        vk0_y, head_dx = _cL_up_line_of_R(*_h_env, dedges)
        h_last_real, h_yL = _horizontal_line_of_R(*_h_env, dedges[1:-1])
        h_width = head_dx + _h_min_width(info, dedges[0][-1], dedges[-1][0])
        _cR_down_line_of_R(*_h_env, dedges, h_width, h_yL)
        
    # embed vn
    vn0_y, head_dx = _cL_up_line_of_R(*_h_env, dedges[-1])
    _vn_mid_down_line_of_R(*_h_env, dedges)
    _vn_last_down_line_of_R(*_h_env, dedges)

    

    # calc x
    _calc_x_of_R(vtc_info)


    # calc bound of R
    R_xL = info[s].xL
    vn, = vk_ls[-1]
    R_yH = info[vn].y + info[vn].yH
    R_xR = info[t].x + info[t].xR
    R_tx = info[t].x
    R_ty = R_by = info[t].y
    if bend_is_t:
        R_bx = R_tx
    else:
        _, x2t, _ = new_dedges_ls[1][-1]
        child, _ = _child[u2v]
        cr = subgph_drawing[child].rect
        R_bx = R_tx + cr.xR + 1

    R_xLRyLH = (R_xL, R_xR, R_yL, R_yH)
    R_tb_xy = (R_tx, R_ty), (R_bx, R_by)
    R_st_fr = st.st, st.fr
    R_rect = _rect_data(R_xLRyLH, R_tb_xy, R_st_fr)
    

    # calc dshift of child  and   bends
    bends = _calc_dshift_of_children_of_R(*_h_env, new_dedges_ls)
    
    assert subgph_drawing[node] == None
    subgph_drawing[node] = _rs_subgph_drawing_data(R_rect, vtc_info, bends, others = None)


def orthogonal_drawing_of_sub_rs_tree_rooted_by_RS(rs_env, node):
    bc_env, (rs, subgph_st, subgph_ordering, subgph_drawing) = rs_env

    st = subgph_st[node]
    s,t = st.st
    RS_g = rs.node2planar_subgraph[node]
    new_dedges_ls = subgph_ordering[node]
    assert len(new_dedges_ls) == 4
    info = vtc_info = [None]*RS_g.nv()
    
    _h_env = subgph_drawing, rs, node, vtc_info

    # embed s -> buttomright
    vtx_info[s] = _vtx_info((0,0,0,0), (s,s,s), (0,0,0))
    h_buttom = new_dedges_ls[0]
    bend_is_t_if_t_not_upright, RS_yL = _horizontal_line_of_R(*_h_env, h_buttom)
    v_first_up = new_dedges_ls[1]
    _vertical_of_RS(*_h_env, v_first_up)
    for 

if __name__ == "__main__":
    _test_SPQR_tree_for_c2d2d3_planar()

    


