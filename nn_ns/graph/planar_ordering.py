from .simple_undirected_graph import graph
from .bucket_sort import bucket_sort, group, group_to_list, bucket_sorts
from .fake_face import fake_face
from .BC_tree import connected_components

__all__ = ('left_most_canonical_ordering, drawing_planar_graphs_on_a_grid, '
           'make_connected'.split(', '))

#planar_ordering
#make_maximal_planar

#make_biconnected
#make_triconnected

def _next(v, v_loc, g):
    v_loc += 1
    if v_loc == g.degree(v): v_loc = 0
    idx = g.incident_edge_indices(v)[v_loc]
    u, v = v, g.neighbors(v)[v_loc]
    u_loc, v_loc = v_loc, g.where_edge_idx(v, idx)
    return u, u_loc, idx, v, v_loc

def _make_connected(G):
    g = G
    if g.nv() < 2: return g
    
    root = 0
    cs = connected_components(g)
    vtcs = cs.sub_vtx2gph_vtx
    #if not vtcs or not vtcs[0]: print(g)
    assert vtcs[0][0] == root
    vs = tuple(vtc[0] for vtc in vtcs)
    if len(vs) > 1:
        ad_ls = list(g.adjacency_list())
        ad_ls[root] = list(ad_ls[root])
        for v in vs[1:]:
            ad_ls[v] = list(ad_ls[v])
            ad_ls[v].append(root)
            ad_ls[root].append(v)
        g = graph(ad_ls)
    return g

def make_connected(embedding):
    '1-connected component -> single or get an edge -> link them'
    g = graph(embedding)
    g = _make_connected(g)
    return g.adjacency_list()

def make_biconnected(connected_embedding):pass
#xxxxxxxxxxxxxxxxxxxxxxxx bug xxxxxxxxxxxxxxxxxxxxxx
#   wrong!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11
'BC-tree -> each component(single but not Q) a virtual node'
'ignore nodes of degree 2'
'find a nonleaf node such that each subtree rooted at it has no more than half leaves.'
'let it be root(NOTE, at least three subtrees, so max num_leaves can be <= N//2)'
'make a rooted tree, calc leftmost and rightmost leaf (L,R) of each subtree,'
'we have a ground and forest on it, trees are ordered'
'the first ground is the root'
'list all leaves by order LS, cut into four part, A B C D, number to be a, b, c, d'
'such that B, C are empty or B U C = all leaves of same tree, a+b+c+d=N, c+d=N//2, b+c<=N//2'
'let b1+c1 = b+c, a-b1 = d-c1[+1] => b1 = (a+b+c-d)//2, c1=...'
'cut LS into 6 part L1~L6 with cardinal a-b1, b1, b1, c1, c1, d-c1'
'handle (L2,L3), (L4,L5) and then (L1,L6)'
'when handle (Li,Lj): '
'each round get the rightmost leaf of Li, Li.R and leftmost of Lj, Lj.L, link Li.R - Lj.L'
'if only one leaf remains, link the only leaf to its sibling'
'we get one new edge, and update the forest'
'total no. of new edges = (1+no. of leaves) // 2, lowest bound'


def make_triconnected(biconnected_embedding):pass
'SPQR-tree -> if any P is pure virtual, then we add an new edge(they will be removed)'
'embeding the new edge, this approach make it possible to '
'determind which nodes are contained for a given face'
'choose a node B to begin'
'each face F of B contain a SPQR-forest'
'SPQR-forest has two type of node: E nodes that have edges in F, D those not'
'E nodes just form a forest, and F ground like in make_biconnected'
'Now we add B to E to make a tree T'
'each vertex of degree 2 in a outer S, let it be a leaf of the forest as outer R/S leaf'
'leaf vertices that chain together form a subtree to offer L/R leaf'
'process like in make_biconnected'
'if only one leaf remain, then link it to a non-neighbor'
'else '
'the final ground be a new root'
'loop until SPQR-tree has only one node'
'if the only node is S'
'S 3 - pass; S 4/5 - ....; S n = 4k+i > 5, i = 0/1/2/3, (4j,4j+3), (4j+2,4j+5)'
'i=1, no (4k-2,4k+1) but(4k-2,4k), (4k,1)'
'i=2, no (4k-2,4k+1) but(4k-2,4k), (4k+1,1)'
'i=3, (4k,4k+2), (4k+2,1)'
'else not S, there are some S in the original SPQR-tree'


def make_biconnected(connected_embedding):
    '''add new edges to connected_embedding to be biconnected and planar holds.

for each cut vertex v:
    if v->y follows v->x in the embedding and
        x,y belongs to different biconnected-components:
        add a new edge (x,y)
        v -> [...x, y,...]  x before y   #  needn't handle (tail, head)
        x -> [...`y', v,...] insert y before v
        y -> [...v, `x',...] insert x after v

        but if v->[x,y] deg(v) == 2, troubles, we have to take care of
        new edges to avoid breaking planarity.
        

'''
    n = len(connected_embedding)
    v2loc2new_edges = [[[] for u in neighbors] for neighbors in connected_embedding]
    raise

    
def make_maximal_planar(biconnected_embedding):
    g = graph(biconnected_embedding)
    if g.order() < 3: return biconnected_embedding
    new_edge = [[[] for i in range(g.degree(x))] for x in g.vertices()]
    #print(g._G)
    #idx = g.edge_index((u,v))
    err_msg = 'either not biconnected_embedding or not planar embedding'
    idx = 0
    assert g.num_edges() > 0
    u, v = g.edges()[idx]
    visited = [0]*g.num_edges()
    v_loc = g.where_edge_idx(v, idx)
    stack = [(u, idx, v, v_loc)]
    def color(u, u_loc, idx, v, g):
        visited[idx] += 1
        if visited[idx] > 2: raise err_msg
        if visited[idx] < 2: stack.append((v, idx, u, u_loc))
    def move(v, v_loc, g):
        u, u_loc, idx, v, v_loc = _next(v, v_loc, g)
        color(u, u_loc, idx, v, g)
        return u, u_loc, idx, v, v_loc
    
    while stack:
        u, idx, v, v_loc = stack.pop()
        visited[idx] += 1
        if visited[idx] > 3: raise err_msg
        elif visited[idx] == 3: continue
        v0_new_edge = new_edge[v][v_loc]
        v0 = v
        u0 = u
        u, u_loc, idx, v, v_loc = move(v, v_loc, g)
        u, u_loc, idx, v, v_loc = move(v, v_loc, g)
        while v != u0:
            v0_new_edge.append(v)
            new_edge[v][v_loc].append(v0)
            u, u_loc, idx, v, v_loc = move(v, v_loc, g)

    for c in visited: assert c == 2 or c == 3
    new_g = []
    for u in g.vertices():
        u_ns = []
        #for v, ls in zip(g.neighbors(u), new_edge[u]):
        for i, v in enumerate(g.neighbors(u)):
            ls = new_edge[u][i]
            ls.reverse() ##  ooooo
            u_ns.append(v)
            u_ns += ls
        new_g.append(tuple(u_ns))

    new_g = tuple(new_g)

    # remove multiedge
    n = len(new_g)
    edges = tuple((u, v_loc, v) for u, ns in enumerate(new_g) for v_loc, v in enumerate(ns))
    edges = bucket_sort(edges, lambda e:e[-1], n)
    block = group(edges, lambda e:e[::2])
    single_edges = tuple(edges[i] for i, j in block if j == i + 1)
    single_edges = bucket_sorts(single_edges, lambda i,e:e[i], [1,0], [n,n])
    new_g_ = group_to_list(n, single_edges, lambda e:e[0], lambda e:e[-1])
    
    reserved_multiedges = (edges[i] for i, j in block if j > i + 1)
    reserved_multiedges = tuple((u, new_g[u][v_loc-1], v, new_g[u][v_loc+1]) for u, v_loc, v in reserved_multiedges)
    block = ((i+1, j) for i,j in block if j > i + 1)
    changed_multiedges = tuple((new_g[u][v_loc-1], v, new_g[u][v_loc+1-len(new_g[u])], u) for i, j in block for u, v_loc, v  in edges[i:j])
    new_edges = reserved_multiedges + changed_multiedges
    new_edges = bucket_sorts(new_edges, lambda i, e:e[i], [-1, 0], [n, n])
    new_edges = group_to_list(n, new_edges, lambda e:e[0], lambda e:e[1:])
    for u, new_es in enumerate(new_edges):
        i = 0
        u_ns = new_g_[u]
        u_ns_ = []
        for x, v, y in new_es:
            j = u_ns.index(y, i)
            assert u_ns[j-1] == x
            u_ns_ += u_ns[i:j]
            u_ns_.append(v)
            i = j
        else:
            u_ns_ += u_ns[i:]
        new_g_[u] = tuple(u_ns_)
    new_g_ = tuple(new_g_)
        
    return new_g_
        


        
    
    
    
def planar_ordering(u, v, maximal_planar_embedding):
    g = graph(maximal_planar_embedding)
    n = g.order()
    assert n > 1
    if n == 2: return (u, v)
    assert n > 2

    
    #out_face = [False] * n
    idx = g.edge_index((u,v))
    #u, v = g.edges()[idx]????????????
    v_loc = g.where_edge_idx(v, idx)
    u0, v0 = u, v
    contour = [None] * n
    m = 0
    while v != u0:
        u, u_loc, idx, v, v_loc = _next(v, v_loc, g)
        contour[u] = u_loc, v
        m += 1
    assert m == 2
    u, u_loc, idx, v, v_loc = _next(v, v_loc, g)
    contour[u] = u_loc, v
    del m


    def num_contour_neighbors(contour, v, g):
        c = 1
        v_loc, x = contour[v]
        lowest_contour_neighbor = None
        while contour[x] == None or contour[x][contour_next_idx] != v:
            if contour[x] != None:
                c += 1
                lowest_contour_neighbor = x
            v, v_loc, idx, x, x_loc = _next(v, v_loc, g)
        return c, lowest_contour_neighbor

    contour_next_idx = 1
    contour_loc_idx = 0
    v = contour[v0][contour_next_idx]
    lowest_contour_neighbors = [None]*n
    stack = []
    while v != u0:
        m, lowest = num_contour_neighbors(contour, v, g)
        assert m > 1
        if m > 2:
            lowest_contour_neighbors[v] = lowest
            v = contour[v][contour_next_idx]
            continue
        stack.append(v)
        v_loc = contour[v][contour_loc_idx]
        contour[v] = None
        t = None # just for the first round test in 'while'
        while t == None:
            v, v_loc, idx, x, x_loc = _next(v, v_loc, g)
            x, x_loc, idx, y, y_loc = _next(x, x_loc, g)
            t = contour[x]
            contour[x] = x_loc, y

        v = x
        if v == v0: v = contour[v0][contour_next_idx]
        elif lowest_contour_neighbors[v] != None:
            if y != lowest_contour_neighbors[v]:
                v = y

    stack += [v0, u0]
    stack.reverse()
    assert len(stack) == n
    return tuple(stack)
    



#[CP89] A linear-time algorithm for drawing planar graphs on a grid
# (0,0), (2n-4,0), (n-2,n-2)
def drawing_planar_graphs_on_a_grid(maximal_planar_embedding, planar_ordering):
    V = planar_ordering
    g = graph(maximal_planar_embedding)
    n = g.order()
    if n < 3: return ((0,0), (1, 0))[:n]
    assert n > 2

    T = [None]*n
    # (under_vertex(left_child in tree), next_contour_vertex(right_child in tree), \
    #  x_offset(from tree parent), y)
    under_vertex = left_child = 0
    next_contour_vertex = right_child = 1
    x_offset = 2
    y = 3


    def neighbors_on_contour(v, T, g):
        is_on = lambda u: T[u] != None
        us = g.neighbors(v)
        L = len(us)
        for i in range(L):
            if not is_on(us[i]): break
        else:
            i = us.index(V[0])
            assert 0 <= i < L
            ls = us[i:] + us[:i]
            assert ls[-1] == V[1]
            return ls
        
        k = i  #[:k]
        for i in range(k+1, L):
            if is_on(us[i]): break
        else:
            return us[:k]

        j = i #[j:?]
        for i in range(j+1,L):
            if not is_on(us[i]): break
        else:
            ls = us[j:] + us[:k]
            return ls

        assert k == 0
        k = i
        for i in range(k+1,L):
            assert not is_on(us[i])
        return us[j:k]
    
    T[V[0]] = [None, V[2], 0, 0]
    T[V[1]] = [None, None, 1, 0]
    T[V[2]] = [None, V[1], 1, 1]
    for k, v in zip(range(3, n), V[3:]):
        w = neighbors_on_contour(v, T, g)
        T[v] = [None] * len(T[V[0]])

        wp = w[0]
        wq = w[-1]
        T[w[1]][x_offset] += 1
        T[wq][x_offset] += 1
        delta_wx = sum(T[u][x_offset] for u in w[1:])
        T[v][x_offset] = (-T[wp][y] + delta_wx + T[wq][y])//2
        T[v][y] = (T[wp][y] + delta_wx + T[wq][y])//2
        T[wq][x_offset] = delta_wx - T[v][x_offset] # parent changing
        if w[1] != wq:
            T[w[1]][x_offset] -= T[v][x_offset]
            
        T[wp][next_contour_vertex] = v
        T[v][next_contour_vertex] = wq
        if w[1] != wq:
            T[v][under_vertex] = w[1]
            T[w[-2]][next_contour_vertex] = None
        else:
            T[v][under_vertex] = None



    stack = [(V[0], 0)] # (v, x_base)
    while stack:
        v, x_base = stack.pop()
        if v == None: continue
        T[v][x_offset] += x_base
        x = T[v][x_offset]
        stack.append((T[v][left_child], x))
        stack.append((T[v][right_child], x))

    return tuple((x, y) for _a, _b, x, y in T)







'''
def _prev(u, u_loc, g):
    u_loc -= 1
    if u_loc == -1: u_loc += g.degree(u)
    idx = g.incident_edge_indices(u)[u_loc]
    u, v = g.neighbors(u)[u_loc], u
    u_loc, v_loc = g.where_edge_idx(u, idx), u_loc
    return u, u_loc, idx, v, v_loc


def left_most_canonical_ordering(u, v, triconnected_embedding):
    lmc = _left_most_canonical_ordering(u, v, triconnected_embedding)
    return lmc.calc()
'''

#def left_most_canonical_ordering(u, v, triconnected_embedding):
def left_most_canonical_ordering(u, v, biconnected_embedding):
    lmc = _left_most_canonical_ordering(u, v, biconnected_embedding)
    return lmc.calc()

class _left_most_canonical_ordering:
    #def __init__(self, u, v, triconnected_embedding):
    def __init__(self, u, v, biconnected_embedding):
        self.u0 = u
        self.v0 = v
        self.g = g = graph(biconnected_embedding)
        self.n = n = g.order()
        assert n > 1

        u0, v0 = u, v
        faces = self.faces = fake_face(g)
        u2v = g.edge2dedge((u,v))
        idx = faces.dedge2face_idx[u2v]
        outer_face = faces.dedge2face[u2v]
        outer_dedges = faces.face2dedges[outer_face]
        self.contour = [None] * n
        d = outer_dedges[0]
        v, u = g.dedge2edge(d)
        for d in outer_dedges[::-1]:
            d = g.flip_dedge(d)
            p, x = u, v
            u, v = g.dedge2edge(d)
            assert x == u
            self.contour[u] = p, d, v
            
        self.has_neighbor_removed = [False] * n
        
        self.face_searched = [False]*faces.nf()
        self.face2co_cut_pair = [None]*faces.nf()
        self.to_lowest_t_cut = [None]*n

        # init u0 last face
        face = self.first_face(v0)
        self.face_searched[face] = True
        self.face2co_cut_pair[face] = (u0, v0)
        for v in faces.face2circle_vtc[face]:
            self.to_lowest_t_cut[v] = v0
        self.to_lowest_t_cut[v0] = None

        
        class _a:pass
        self.contour_data_of_vk = _a
        return

    def contour_next(self, u): return self.contour[u][-1]
    def contour_prev(self, u): return self.contour[u][0]
    def contour_dedge(self, u): return self.contour[u][1]
    def is_on_contour(self, u):
        assert self.contour[u] is not self.contour_data_of_vk
        return self.contour[u] != None
    def search_face(self, face, v2u):
        assert not self.face_searched[face]
        assert self.face2co_cut_pair[face] == None
        self.face_searched[face] = True
        
        ds = self.faces.face2dedges[face]
        idx = self.faces.dedge2face_idx[v2u]
        ds = ds[idx:] + ds[:idx]
        vs = tuple(self.g.dedge2edge(d)[0] for d in ds[::-1]) # reverse
        for i, v in enumerate(vs[:-2]): # except the first two vtc
            if self.is_on_contour(v):
                break
        else:
            return
        t = v
        
        for v in vs[i+1:]:
            if self.to_lowest_t_cut[v] == None:
                self.to_lowest_t_cut[v] = t
        s, _ = self.g.dedge2edge(v2u)
        self.face2co_cut_pair[face] = (s, t)

    def first_face(self, v):
        v2u = self.contour_dedge(v)
        face = self.faces.dedge2face[v2u]
        return face
    def st_cut_for_first_face(self, v):
        face = self.first_face(v)
        assert self.face_searched[face]
        st = self.face2co_cut_pair[face]
        return st
    def st_cut_for_last_face(self, v):
        u = self.contour_prev(v)
        return self.st_cut_for_first_face(u)
    def is_t_cut(self, v):
        st = self.st_cut_for_last_face(v)
        if st == None:
            return False
        return st[-1] == v
    def down_outgo(self, v):
        p, v2u, u = self.contour[v]
        ds = []
        while u != p:
            ds.append((v2u, u))
            v2u = self.g.prev_out(v2u)
            _v, u = self.g.dedge2edge(v2u)
            assert _v == v
        assert self.contour[u] != None and self.contour_next(u) == v
        ds.append((v2u, u))
        return ds
    

    def is_s_cut(self, v):
        face = self.first_face(v)
        if not self.face_searched[face]:
            # search v
            down = self.down_outgo(v)
            assert len(down) >= 3
            for v2u, u in down[-3::-1]:
                face = self.faces.dedge2face[v2u]
                if self.face_searched[face]:
                    break
                self.search_face(face, v2u)
        return (not self.is_t_cut(v)) and self.to_lowest_t_cut[v] != None
        
    def calc(self):
        u0, v0 = self.u0, self.v0
        vn = self.contour_next(u0)
        self.has_neighbor_removed[vn] = True
        v = u0
        vs = []
        vk2neighbors = []
        while v != v0:
            vk, neighbors_on_new_contour = self.find_from(v)
            vs.append(vk)
            assert len(neighbors_on_new_contour) >= 2
            # [(vk2nb_dedge, nb)]
            vk2neighbors.append(neighbors_on_new_contour)
            
            for v in vk:
                self.contour[v] = self.contour_data_of_vk
            for vk2v, v in neighbors_on_new_contour:
                self.has_neighbor_removed[v] = True

            # fix contour
            u_L = neighbors_on_new_contour[0]
            for v_L in neighbors_on_new_contour[1:]:
                self.build_contour(u_L, v_L)
                u_L = v_L
            #self.check_contour()

            vk2v, v = neighbors_on_new_contour[0]
            if v == u0 and self.contour_next(u0) == v0: break

        vs.append((u0, v0))
        vs.reverse()
        vk2neighbors.append(())
        vk2neighbors.reverse()
        return tuple(vs), tuple(vk2neighbors)

    def find_from(self, v):
        u0, v0 = self.u0, self.v0
        
        while v != v0 or self.is_t_cut(v0):
            u = self.contour_next(v)
            
            if self.is_t_cut(v):
                return self.go_back_to_remove_list(v)
            elif self.is_s_cut(v):
                v = u
                continue

            elif not self.has_neighbor_removed[v]:
                v = u
                continue
            elif self.is_contour_degree2(v):
                v = u
                continue


            return self.remove_v(v)

        raise 'error: bad data'

    def remove_v(self, v):
        assert not self.is_contour_degree2(v)

        vk = (v,)  # remove only one vtx
        ns = self.down_outgo(v) #[(v2u, u)]
        ns.reverse()
        assert len(ns) >= 3

        return vk, tuple(ns)

        
        
    def go_back_to_remove_list(self, v):
        u0, v0 = self.u0, self.v0
        
        s,t = self.st_cut_for_last_face(v)
        assert t == v
        assert (not self.is_contour_degree2(s)) or s == u0
        if self.to_lowest_t_cut[s] == t:
            self.to_lowest_t_cut[s] = None
        
        vk = []
        u = self.contour_next(s)
        while u != t:
            vk.append(u)
            u = self.contour_next(u)

        assert vk
        s2vk = self.contour_dedge(s)
        vk2s = self.g.flip_dedge(s2vk)
        vk2t = self.contour_dedge(vk[-1])
        
        return tuple(vk), ((vk2s, s), (vk2t, t))
    
    def is_contour_degree2(self, u):
        assert self.contour[u] != None
        u2x = self.contour_dedge(u)
        u2x = self.g.prev_out(u2x)
        _, x = self.g.dedge2edge(u2x)
        return x == self.contour_prev(u)

    
    def build_contour(self, u_L, v_L):
        contour = self.contour
        g = self.g
        u2x, x = u_L
        vk2y, y = v_L
        p = self.contour_prev(x)
        curr = x
        while x != y:
            u2x = g.prev_in(u2x)
            u2x = g.flip_dedge(u2x)
            u, x = g.dedge2edge(u2x)
            assert u == curr
            self.contour[u] = p, u2x, x
            p, curr = u, x

        # p -> y -> ?
        assert self.contour_next(p) == y
        if self.is_on_contour(y):
            _, y2z, z = self.contour[y]
        else:
            z2y = g.prev_in(vk2y)  #no edges in z2y and vk2y
            y2z = g.flip_dedge(z2y)
            _y, z = g.dedge2edge(y2z)
            assert curr == y == _y
        
        self.contour[y] = p, y2z, z
        return

    def check_contour(self):
        u0, v0 = self.u0, self.v0
        v = u0
        p = v0
        while v != v0:
            _p, v2x, x = self.contour[v]
            assert p == _p
            assert (v,x) == self.g.dedge2edge(v2x)
            p, v = v, x
        _p, v2x, x = self.contour[v]
        assert p == _p
        assert (v,x) == self.g.dedge2edge(v2x)
        assert x == u0
    
'''
class _left_most_canonical_ordering:
    def __init__(self, u, v, triconnected_embedding):
        self.u0 = u
        self.v0 = v
        self.g = g = graph(triconnected_embedding)
        self.n = n = g.order()
        assert n > 1

    
        idx = g.edge_index((u,v))
        u_loc = g.where_edge_idx(u, idx)
        u0, v0 = u, v
        contour = [None] * n
        while u != v0:
            u, u_loc, idx, v, v_loc = _prev(u, u_loc, g)
            contour[v] = v_loc, u
        u, u_loc, idx, v, v_loc = _prev(u, u_loc, g)
        contour[v] = v_loc, u
        self.contour = contour
    
        self.has_neighbor_removed = [False] * n
        
        self.co_cut_pt = [None] * n
        self.co_cut_pt_back = list([] for i in range(n))
        return

    def calc(self):
        contour = self.contour
        has_neighbor_removed = self.has_neighbor_removed
        u0, v0 = self.u0, self.v0
        find_from, build_contour = self.find_from, self.build_contour
        
        u0_loc, vn = contour[u0]
        has_neighbor_removed[vn] = True
        v = vn
        vs = []
        while v != v0:
            vk, neighbors_on_new_contour = find_from(v)
            vs.append(vk)
            for v in vk:
                contour[v] = None
            for v, _ in neighbors_on_new_contour:
                has_neighbor_removed[v] = True
            u_L = neighbors_on_new_contour[0]
            for v_L in neighbors_on_new_contour[1:]:
                build_contour(u_L, v_L)
                u_L = v_L

            v = neighbors_on_new_contour[0][0]
            if v == u0:
                v = neighbors_on_new_contour[1][0]

        vs.append((u0, v0))
        vs.reverse()
        return tuple(vs)

    def find_from(self, v):
        contour = self.contour
        has_neighbor_removed = self.has_neighbor_removed
        u0, v0 = self.u0, self.v0
        is_contour_degree2 = self.is_contour_degree2
        co_cut_pt = self.co_cut_pt
        go_back_to_remove_list, find_co_cut_pt, remove_v =\
                                self.go_back_to_remove_list, self.find_co_cut_pt, self.remove_v
        while v != v0 or co_cut_pt[v0] == v0:
            v_loc, u = contour[v]
            if v == v0:
                pass
            elif (not is_contour_degree2(v)) and is_contour_degree2(u):
                v = u
                continue
            if co_cut_pt[v] != None:
                if co_cut_pt[v] == v:
                    return go_back_to_remove_list(v)
                else:
                    v = u
                    continue

            if not has_neighbor_removed[v]:
                v = u
                continue


            find_co_cut_pt(v, v_loc)

            if co_cut_pt[v] != None:
                v = u
                continue

            return remove_v(v)

        raise 'error: bad data'

    def remove_v(self, v):
        contour = self.contour
        u0, v0 = self.u0, self.v0
        is_contour_degree2 = self.is_contour_degree2
        g = self.g
        
        vk = []
        u = v
        while v != v0 and is_contour_degree2(v):
            vk.append(v)
            _, v = contour[v]

        if len(vk):
            u, u_loc, idx, _, _ = _prev(u, contour[u][0], g)
            return tuple(vk), ((u, u_loc), (v, None))

        vk = (v,)
        v_loc, u = contour[v]
        ns = [(u, None)]
        u, u_loc, idx, v, v_loc = _prev(v, v_loc, g)
        while contour[u] == None:
            ns.append((u, u_loc))
            u, u_loc, idx, v, v_loc = _prev(v, v_loc, g)
        ns.append((u, u_loc))
        ns.reverse()
        assert contour[u][-1] == v

        return vk, tuple(ns)

    def anticlockwise_circle(self, u, u_loc):
        g = self.g
        
        vs = []
        u0 = u
        u, u_loc, idx, v, v_loc = _prev(u, u_loc, g)
        while u != u0:
            vs.append(u)
            u, u_loc, idx, v, v_loc = _prev(u, u_loc, g)
        vs.append(u0)
        return vs
        
    def find_co_cut_pt(self, v, v_loc):
        contour = self.contour
        u0, v0 = self.u0, self.v0
        g = self.g
        co_cut_pt, co_cut_pt_back = self.co_cut_pt, self.co_cut_pt_back
        anticlockwise_circle = self.anticlockwise_circle
        
        vd = [(v, v_loc)]
        u, u_loc, idx, _, v_loc = _prev(v, v_loc, g)
        while contour[u] == None or contour[u][-1] != v:
            vd.append((v, v_loc))
            u, u_loc, idx, _, v_loc = _prev(v, v_loc, g)

        for _, v_loc in vd[:-1]:
            vs = anticlockwise_circle(v, v_loc)
            v_head = [vs.pop()]
            while vs:
                if contour[v_head[-1]][-1] != vs[-1]:
                    break
                v_head.append(vs.pop())

            assert vs # if degree2 then len(vd) == 1 
            for i, u in enumerate(vs):
                if contour[u] != None:
                    break
            else:
                continue

            for x in vs[i:] + v_head:
                if co_cut_pt[x] == None:
                    co_cut_pt[x] = u
            co_cut_pt_back[u].append(v)

        for _, v_loc in vd[-1:]:
            vs = anticlockwise_circle(v, v_loc)
            v_head = [vs.pop()]
            while vs:
                if contour[v_head[-1]][-1] != vs[-1]:
                    break
                v_head.append(vs.pop())

            assert vs or v_head[-1] == u0 # vs[0] == prev(v) or ...
            if len(vs) == 0:
                assert len(vd) == 1 # last circle
                return
            
            for i, u in enumerate(vs[1:]):
                if contour[u] != None:
                    break
            else:
                continue

            for x in vs[i:] + v_head:
                if co_cut_pt[x] == None:
                    co_cut_pt[x] = u
            co_cut_pt_back[u].append(v)

                
        
        
    def go_back_to_remove_list(self, v):
        contour = self.contour
        u0, v0 = self.u0, self.v0
        is_contour_degree2 = self.is_contour_degree2
        g = self.g
        co_cut_pt, co_cut_pt_back = self.co_cut_pt, self.co_cut_pt_back
        
        u = co_cut_pt_back[v].pop()
        vk = []
        if is_contour_degree2(u):
            vk.append(u)
        u_loc, v = contour[u]
        while v != v0 and is_contour_degree2(v):
            vk.append(v)
            _, v = contour[v]

        assert vk
        u = vk[0]
        u_loc, _ = contour[u]
        u, u_loc, idx, _, _ = _prev(u, u_loc, g)
        return tuple(vk), ((u, u_loc), (v, None))
    
    def is_contour_degree2(self, u):
        contour = self.contour
        g = self.g
        
        assert contour[u] != None
        u_loc, _ = contour[u]
        u, u_loc, idx, v, v_loc = _prev(u, u_loc, g)
        return contour[u] != None and contour[u] == (u_loc, v)
        
        
    def build_contour(self, u_L, v_L):
        contour = self.contour
        g = self.g

        x, x_loc = u_L
        v, _ = v_L
        while x != v:
            x, x_loc, idx, u, u_loc = _prev(x, x_loc, g)
            contour[u] = u_loc, x

        return

'''





def _test_left_most_canonical_ordering():
    ad_ls = [\
        (1, 9, 8),\
        (0, 2, 9),\
        (1, 3, 10),\
        (2, 4, 11, 10),\
        (3, 5, 14, 13, 12),\

        (4, 6, 14),\
        (5, 7, 14),\
        (6, 8, 14),\
        (0, 9, 7),\
        (0, 1, 10, 11, 8),\

        (2, 3, 11, 9),\
        (9, 10, 3, 12),\
        (11, 4, 13),\
        (12, 4, 14),\
        (13, 4, 5, 6, 7),\
        ]
    ans = (\
            ((0, 1), (9,), (10, 2), (3,), (11,), (12, 4), \
             (13,), (14,), (5,), (6,), (7,), (8,)), \
            ((), ((29, 0), (31, 1)), \
             ((48, 9), (30, 1)), \
             ((8, 10), (32, 2)), \
             ((49, 9), (50, 10), (36, 3)), \
             ((51, 11), (34, 3)), \
             ((52, 12), (39, 4)), \
             ((53, 13), (40, 4)), \
             ((15, 14), (37, 4)), \
             ((17, 14), (41, 5)), \
             ((19, 14), (43, 6)), \
             ((28, 0), (20, 9), (45, 7))),\
        )
    t = left_most_canonical_ordering(0, 1, ad_ls)
    if ans != t: print(t)
    assert ans == t

    


def _test_make_maximal_planar():
    from . import graph_format_ascii_embedding
    from . import Boyer_Myrvold_planarity_test
    from .some_triconnected_cubic_planar_graphs import show_graph_format_ascii_embedding_by_networkx
    str2embedding = graph_format_ascii_embedding.str2embedding
    planarity_test = Boyer_Myrvold_planarity_test.Boyer_Myrvold_planarity_test
    data = [\
        '4 bcd,adc,abd,acb',\
        '6 bcd,aef,afd,ace,bdf,bec',\
        '8 bcd,aef,afg,agh,bhf,bec,chd,dge',\
        '8 bcd,aef,afg,age,bdh,bhc,chd,egf',\
        '10 bcd,aef,afg,ahi,bjf,bec,cjh,dgi,dhj,eig',\
        '10 bcd,aef,afd,acg,bhi,bic,djh,egj,ejf,gih',\
        '10 bcd,aef,agd,ach,bif,beg,cfj,dji,ehj,gih',\
        '10 bcd,aef,afg,agh,bhi,bic,cjd,dje,ejf,gih',\
        '10 bcd,aef,agh,ahe,bdi,bjg,cfj,cid,ehj,fig',\
        '12 bcd,aef,afd,acg,bhi,bjc,djk,ekl,elj,fig,glh,hki',\
        '12 bcd,aef,agh,aij,bkl,blg,cfl,cki,dhj,dik,ejh,egf',\
        '12 bcd,aef,afg,ahi,bjf,bec,ckl,dli,dhj,eik,gjl,gkh',\
        '12 bcd,aef,afg,agh,bij,bjc,chd,dgk,ekl,elf,hli,ikj',\
        '12 bcd,aef,afg,agh,bij,bjc,ckd,dki,ehl,elf,glh,ikj',\
        '12 bcd,aef,agd,ach,bif,bej,cjk,dli,ehl,fkg,gjl,hki',\
        '12 bcd,aef,agd,ach,bij,bjg,cfk,dki,ehl,elf,glh,ikj',\
        '12 bcd,aef,agh,ahe,bdi,bjk,ckl,cid,ehj,fil,flg,gkj',\
        '12 bcd,aef,agh,ahe,bdi,bjg,cfj,ckd,ekl,flg,hli,ikj',\
        '12 bcd,aef,agh,aie,bdj,bkg,cfk,cli,dhl,elk,fjg,hji',\
        '12 bcd,aef,agh,aij,bjk,blg,cfl,cki,dhj,die,ehl,fkg',\
        '12 bcd,aef,agh,aie,bdj,bjg,cfk,cki,dhl,elf,glh,ikj',\
        '14 bcd,aef,agd,ach,bij,bjk,ckh,dgl,emn,enf,flg,hkm,iln,imj',\
        '14 bcd,aef,agd,ach,bij,bjg,cfh,dgk,ekl,emf,hni,inm,jln,kml',\
        '14 bcd,aef,agd,ach,bij,bjg,cfh,dgk,elm,enf,hnl,ikm,iln,jmk',\
        '14 bcd,aef,agd,ach,bij,bkg,cfh,dgl,emn,enk,fjl,hkm,iln,imj',\
        '14 bcd,aef,agd,ach,bif,bej,cjk,dlm,enj,fig,gnl,hkm,hln,imk',\
        '14 bcd,aef,agh,aij,bkl,bmn,cnl,cki,dhj,dik,ejh,egm,fln,fmg',\
        '14 bcd,aef,agd,ach,bif,bej,cjk,dkl,emn,fng,glh,hkm,iln,imj',\
        '14 bcd,aef,agd,ach,bij,bjg,cfk,dkl,emj,eif,gnh,hnm,iln,kml',\
        '14 bcd,aef,afg,ahi,bjf,bec,ckl,dli,dhj,eim,gmn,gnh,jnk,kml',\
        '14 bcd,aef,agh,aij,bkf,beg,cfh,cgl,dmj,dik,ejn,hnm,iln,kml',\
        '14 bcd,aef,afg,ahi,bjk,bkc,clm,dmi,dhn,enk,ejf,gnm,glh,ilj',\
        '14 bcd,aec,abf,afg,bhi,cjd,dkl,eli,ehm,fmn,gnl,gkh,inj,jmk',\
        '14 bcd,aef,afg,agh,bij,bjc,ckd,dkl,emn,enf,glh,hkm,iln,imj',\
        '14 bcd,aef,afg,agh,bij,bjc,ckd,dkl,elm,emf,gnh,hni,inj,kml',\
        '14 bcd,aef,agd,ach,bij,bjg,cfk,dkl,elm,emf,gnh,hni,inj,kml',\
        '14 bcd,aef,afg,ahi,bjk,bgc,cfl,dlm,dmj,ein,enl,gkh,hni,jmk',\
        '14 bcd,aec,abf,agh,bij,cjk,dkh,dgl,elm,emf,fng,hni,inj,kml',\
        '14 bcd,aef,agh,aij,bkf,beg,cfl,cmi,dhj,din,enl,gkm,hln,jmk',\
        '14 bcd,aef,afg,agh,bij,bkc,cld,dmi,ehj,eik,fjn,gnm,hln,kml',\
        '14 bcd,aef,afg,agh,bij,bkc,cld,dli,ehj,eim,fmn,gnh,jnk,kml',\
        '14 bcd,aef,agh,aij,bkl,bmg,cfh,cgi,dhn,dnk,ejl,ekm,fln,imj',\
        '14 bcd,aef,afg,agh,bij,bkc,cld,dmi,ehn,enk,fjl,gkm,hln,imj',\
        '14 bcd,aef,agh,ahe,bdi,bjk,clm,cid,ehj,fin,fnl,gkm,gln,jmk',\
        '14 bcd,aef,agh,aie,bdj,bkl,cmh,cgi,dhj,eik,fjn,fnm,gln,kml',\
        '14 bcd,aef,agh,ahe,bdi,bjk,clm,cid,ehn,fnk,fjl,gkm,gln,imj',\
        '14 bcd,aef,agh,ahe,bdi,bjk,ckl,cid,ehm,fmn,fng,gnm,ilj,jlk',\
        '14 bcd,aef,agh,ahe,bdi,bjg,cfk,cld,elm,fmk,gjn,hni,inj,kml',\
        '14 bcd,aef,agh,aie,bdj,bkg,cfk,clm,dmn,elk,fjg,hjn,hni,iml',\
        '14 bcd,aef,agh,aie,bdj,bkl,clh,cgm,dmn,enk,fjl,fkg,hni,imj',\
        '14 bcd,aef,agh,aij,bjk,blg,cfl,cmi,dhm,dke,ejn,fng,hni,kml',\
        '14 bcd,aef,agh,aij,bkl,bmg,cfh,cgi,dhm,dnk,ejl,ekn,fni,jml',\
        '14 bcd,aef,agh,aij,bjf,bek,ckl,cmi,dhm,dne,flg,gkn,hni,jml',\
        '14 bcd,aef,agh,aie,bdj,bjg,cfk,cli,dhm,emf,gnl,hkn,inj,kml',\
        '14 bcd,aef,agh,aie,bdj,bkg,cfl,cmi,dhn,enk,fjl,gkm,hln,imj',\
        '20 bcd,aef,agh,aij,bjk,blg,cfm,cni,dho,dpe,eql,fkr,grn,hms,isp,joq,kpt,ltm,nto,qsr',
        ]

    res = []
    for s in data[:]:
        e = str2embedding(s)
        G = graph(e)
        e = planarity_test(G)
        for i, ls in enumerate(e):
            if len(ls): break
        else:
            raise 'empty graph?'
        
        me = make_maximal_planar(e)
        o = planar_ordering(0, me[0][0], me)
        d = drawing_planar_graphs_on_a_grid(me, o)
        res.append((me,o,d))

    #return res
    list(map(show_graph_format_ascii_embedding_by_networkx, data))

    import matplotlib.pyplot as plt
    import networkx as nx
    gx = nx.Graph
    g = graph(e)
    n = g.order()
    edges = g.edges()
    g = gx()
    g.add_nodes_from(range(n))
    g.add_edges_from(edges)
    pos = {i:p for i, p in enumerate(d)}
    nx.draw(g, pos)
    plt.show()
    nx.draw(g)
    plt.show()
    for layout in [nx.spring_layout, nx.spectral_layout]:#, nx.pydot_layout]:
        pos=layout(g)
        nx.draw(g, pos)
        plt.show()


if __name__ == "__main__":
    _test_left_most_canonical_ordering()
    _test_make_maximal_planar()



