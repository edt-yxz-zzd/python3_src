'''
simple_undirected_graph
    no multiedges
    no self loops
    undirected
    may not connected
    adjacency list, so planar graph can be handled in O(n)
    immutable
    no extra data, so use vertices(G) and edge_index(e, G) to ref...

make_graph(adjacency_list)
make_graph(n, edges)
|E| = num_edges(G) = ne(G)
n = |V| = order(G) = nv(G) = num_vtc(G)
adjacency_list(G)
adjacency_list_to_uedge(G)
adjacency_list_to_dedge(G)
vertices(G)=vtc(G), v is in range(n) for v in vertices(G) // for vertex_value array
edges(G)=uedge2edge(G), edge is in form (u, v) // u < v // uedge is edge_idx
dedge2edge(G), dedge2edge[dedge] == is_uedge(dedge)? uedge2edge(dedge) : reversed(uedge2edge(to_uedge(dedge)))
uedges(G), uedge is in range(num_edges) for uedge in uedges(G)
dedges(G), range(2*num_edges)
is_uedge(dedge, G)
to_uedge(dedge, G)
to_dedges(dedge, G)
neighbors(v, G)=vtc(v, G)
incident_edge_indices(v, G)=uedges(v, G) -> list of index of edge from v
dedges(v, G)
where_edge_idx(v, [u,] idx, G)=where_uedge(v, [u,] uedge, G)
where_dedge([v, [u,]] dedge, G)
degree(v, G)
is_adjacent(u, v, G)
edge_index(e, G)=edge2uedge(e,G) -> edges(G)[edge_index(e)] is e or reverse(e) // for edge_value array
edge2dedge(e,G)
flip_dedge(dedge,G)
next_out(dedge,G)
prev_out(dedge,G)
next_in(dedge,G)
prev_in(dedge,G)

flip_next_out(dedge,G)
flip_prev_out(dedge,G)
flip_next_in(dedge,G)
flip_prev_in(dedge,G)

relabel
relabel_back

############### class graph
edges_list2vtc_list(gph_order, edges_list)
reindex_edges_list(gph_order, list_of_sorted_vtc, list_of_sorted_edges)
subgraphs_from_uedges_list(list_of_unsorted_uedges, G)


class graph
= (adjacency_list, edges, edge_index_aux, idx2loc, adjacent_edge_indices)
    adjacency_list
        u -> [v...]
        if (u,v) in G then v in adjacency_list[u]
    edges
        idx -> (u,v)
        u,v = edges[idx]
    edge_index_aux
        used to guess idx from (u,v)
    idx2loc
        u, idx -> loc
        assert adjacency_list[u][loc] == edges[idx] \ {u}
    adjacent_edge_indices == loc2idx
        u, loc -> idx
        assert loc2idx[u][loc] == edge_index(u, ad_ls[u][loc], G)
'''

### error import .bucket_sort as debug_lib
##from .bucket_sort import inner_sort_ints_list
##print(dir(debug_lib))


from bisect import bisect_left as search
from .bucket_sort import group, group_to_list, bucket_sorts, \
     bucket_sort, group_unify, \
     inner_sort_ints_list, inner_sorts_ints_list, is_sorted


def _sort_edges(edges, n):
    key_with_round = lambda i, e: e[i]
    return bucket_sorts(edges, key_with_round = key_with_round, rng = (1,0), Ns = (n,n))



def _assert(b):
    if not b: raise 'bad graph data'
def _check_adjacency_list(adjacency_list):
    ls = adjacency_list
    n = len(ls)
    count = [0]*n
    to = [n]*n
    for i, e in enumerate(ls):
        count[i] += len(e)  #outgoing
        for j in e:
            _assert(0 <= j < n)
            _assert(j != i) # no i->i
            _assert(to[j] != i)
            to[j] = i       #no multi i->j
            count[j] -= 1   #income
    for c in count: _assert(c == 0)
    # leave to check: if v->u, has u->v??????????????

def make_graph(adjacency_list, edges = None):
    'make_graph(adjacency_list) or make_graph(graph_order, edges)'

    if edges != None:
        n = adjacency_list
        return _make_graph_from_edges(n, edges)

    return _make_graph_from_adjacency_list(adjacency_list)
    

#ORIENTATION-PRESERVING
def _make_graph_from_adjacency_list(adjacency_list):
    ls = tuple(tuple(e) for e in adjacency_list)
    _check_adjacency_list(ls)
    adjacency_list = ls
    n = len(ls)

    # check v->u ===> u->v
    #build idx2loc
    edge_u_loc_ls = tuple((tuple(sorted((u,v))), (u, u2v_loc)) \
                          for u,e in enumerate(ls) for u2v_loc, v in enumerate(e))
    #edge_u_loc_ls = bucket_sort(n, edge_u_loc_ls, lambda e:e[-1][0])
    edge_u_loc_ls = bucket_sorts(edge_u_loc_ls, lambda i,e:e[0][i], (1,0), (n,n))
    for i in range(0, len(edge_u_loc_ls), 2):
        e0 = edge_u_loc_ls[i]
        e1 = edge_u_loc_ls[i+1]
        assert e0[0] == e1[0] == (e0[1][0], e1[1][0]) # check v->u ===> u->v
    for i in range(1, len(edge_u_loc_ls)-1, 2):
        e0 = edge_u_loc_ls[i]
        e1 = edge_u_loc_ls[i+1]
        assert e0[0] != e1[0]  # multiedge
    
    idx2loc = tuple(tuple(u2v for (_,_), (u,u2v) in edge_u_loc_ls[i:i+2]) \
                    for i in range(0, len(edge_u_loc_ls), 2))

    #build edges
    edges = tuple(e for e, _ in edge_u_loc_ls[::2])
    m = len(edges)
    assert m == len(idx2loc)
    del edge_u_loc_ls
    
    '''
    edges2 = tuple(sorted((u,v)) for u,e in enumerate(ls) for v in e)
    edges2 = bucket_sorts(edges2, lambda i,e:e[i], (1,0), (n,n))
    for i in range(0, len(edges2), 2):
        assert edges2[i] == edges2[i+1]

    # build edges
    edges = tuple(tuple(e) for e in edges2[::2])
    m = len(edges)
    del edges2

    #build tmp for idx2loc
    tmp = []
    for u,e in enumerate(ls):
        for loc, v in enumerate(e):
            uuu = u
            if v < u: uuu,v = v,u
            tmp.append((uuu,v,loc))
    _assert(len(tmp) == 2*m) # incomplete ad_ls
    tmp = _sort_edges(tmp, n)

    #build idx2loc
    # if u<v, then loc of (v,u) is after that of (u,v)
    # u,v = edges[idx] => u < v and ad_ls[u][idx2loc[idx][0]] == v
    pre_e = (0,0)
    idx2loc = [None]*m
    for idx, i in enumerate(range(0, len(tmp), 2)):
        idx2loc[idx] = (tmp[i][2], tmp[i+1][2])
        e = edges[idx]
        _assert(e != pre_e)
        _assert(e == tmp[i][:2] == tmp[i+1][:2])
        pre_e = e
        
    idx2loc = tuple(idx2loc)
    del tmp

    '''

    #build loc2idx
    loc2idx = list([None]*len(e) for e in ls)
    for i, (u,v) in enumerate(edges):
        u2v, v2u = idx2loc[i]
        _assert(loc2idx[u][u2v] == None)  # multiedges or loop
        _assert(loc2idx[v][v2u] == None)  # or incomplete
        loc2idx[u][u2v] = i
        loc2idx[v][v2u] = i
    loc2idx = tuple(tuple(e) for e in loc2idx)
    adjacent_edge_indices = loc2idx


    #build edge_index_aux
    es_idx = []
    degree = lambda v: len(adjacency_list[v])
    for idx, (u,v) in enumerate(edges):
        if degree(u) > degree(v):
            u,v = v,u
        es_idx.append((u,v,idx)) # degree(u) <= degree(v), but may u > v
    es_idx = _sort_edges(es_idx, n)
    edge_index_aux = tuple(\
        group_to_list(n, es_idx, lambda e:e[0], lambda e:e[1:]))

    dedge2edge = tuple((v,u) for u,v in edges)
    dedge2edge = edges + dedge2edge
    def select(b, f, s):
        if b:
            return f
        else:
            return s
    calc_dedge = lambda u, uedge: select(edges[uedge][0] == u, uedge, uedge+m)
    vtx2dedges = tuple(tuple(calc_dedge(u, uedge) for uedge in uedges) \
                       for u, uedges in enumerate(adjacent_edge_indices))
        
    return adjacency_list, adjacent_edge_indices,\
           edges, edge_index_aux, idx2loc, dedge2edge, vtx2dedges


#NO ORIENTATION
def _make_graph_from_edges(graph_order, edges):
    n = graph_order
    edges = list(edges)
    edges2 = list((v,u) for u, v in edges) + edges
    edges2 = bucket_sorts(edges2, lambda i,e:e[i], (1,0), (n,n))
    ad_ls = group_to_list(n, edges2, lambda e:e[0], lambda e:e[1])
    return _make_graph_from_adjacency_list(ad_ls)
    
    '''
    edges = list(edges)
    size = len(edges)

    #check input
    for i in range(size):
        u, v = edges[i]
        _assert(u != v)
        _assert(0 <= u < n and 0 <= v < n)

    #double edges: (u,v) and (v,u)
    edges2 = list((v,u) for u, v in edges)
    edges2 += edges
    edges2 = _sort_edges(edges2, n)
    del edges

    #build adjacency_list
    adjacency_list = tuple(\
        group_to_list(n, edges2, lambda e:e[0], lambda e:e[1]))
    del edges2

    return _make_graph_from_adjacency_list(adjacency_list)'''





edge_index_aux_target_idx = 0
edge_index_aux_data_idx = 1


adjacency_list_idx = 0
adjacent_edge_indices_idx = 1
edges_idx = 2
edge_index_aux_idx = 3
idx2loc_idx = 4
dedge2edge_idx = 5
vtx2dedges_idx = 6



def num_edges(G): return len(G[edges_idx])
def order(G): return len(G[adjacency_list_idx])
def adjacency_list(G): return G[adjacency_list_idx]
def adjacency_list_to_uedge(G): return G[adjacent_edge_indices_idx]
def adjacency_list_to_dedge(G): return G[vtx2dedges_idx]
def vertices(G): return range(order(G))
def edges(G): return G[edges_idx]
def neighbors(v, G): return G[adjacency_list_idx][v]
def degree(v, G): return len(neighbors(v, G))
def _loc(u, v, G):
    if u > v: v,u = u,v
    if degree(u,G) > degree(v,G): u,v = v,u
    ls = G[edge_index_aux_idx][u]
    loc = search(ls, (v,0))
    idx = -1
    
    if loc < len(ls) and \
       ls[loc][edge_index_aux_target_idx] == v:
        idx = ls[loc][edge_index_aux_data_idx]
    else:
        assert loc >= 0
        loc = -loc-1
        
    return (loc, u, v, idx)

def is_adjacent(u, v, G): return _loc(u, v, G)[-1] > 0

def edge_index(e, G):
    u, v = e
    loc, u, v, idx = _loc(u, v, G)
    if idx < 0: raise 'not adjacent'
    return idx


def incident_edge_indices(v, G):
    return G[adjacent_edge_indices_idx][v]

def where_edge_idx(v, u, idx, G = None):
    if G == None:
        v, idx, G = v, u, idx
        loc2 = G[idx2loc_idx][idx]
        for i, u in enumerate(edges(G)[idx]):
            if v == u:
                return loc2[i]
        raise 'not match'

    
    vl, ul = G[idx2loc_idx][idx]
    if v > u:
        vl, ul = ul, vl
        v, u = u, v
    if (v, u) != edges(G)[idx]:
        raise 'not match'
    return vl, ul
        

def relabel(adjacency_list, label):#new = label[old]
    old_ls = adjacency_list
    assert len(old_ls) == len(label)
    old2new = label
    
    n = len(old_ls)
    old2new_ns = [tuple(old2new[old_v] for old_v in ns) for ns in old_ls]
    new_ls = [None]*n
    for old_v, new_v in enumerate(old2new):
        new_ls[new_v] = new_neighbors = old2new_ns[old_v]
    return tuple(new_ls)

def relabel_back(adjacency_list, label):
    new_ls = adjacency_list
    assert len(new_ls) == len(label)
    old2new = label
    n = len(new_ls)
    
    new2old = [None]*n
    for old_v, new_v in enumerate(old2new):
        new2old[new_v] = old_v
    return relabel(new_ls, new2old)



ne = num_edges 
nv = num_vtc = order
_all_vtc = vertices
uedge2edge = edges
def _assert_dedge(dedge, G):assert 0 <= dedge < 2*ne(G)
def _all_dedge2edge(G): return G[dedge2edge_idx]
def _all_uedges(G): return range(ne(G))
def _all_dedges(G): return range(2*ne(G))
def is_uedge(dedge, G):
    _assert_dedge(dedge, G)
    return 0 <= dedge < ne(G)
def to_uedge(dedge, G):
    if not is_uedge(dedge, G):
        dedge -= ne(G)
    return dedge
def to_dedges(dedge, G):
    uedge = dedge
    if not is_uedge(uedge, G):
        uedge -= ne(G)
    else:
        dedge += ne(G)
    return uedge, dedge


_v_vtc = neighbors
_v_uedges = incident_edge_indices
def _v_dedges(v, G): return G[vtx2dedges_idx][v]
def _v_dedge2edge(v, G): return G[dedge2edge_idx][v]

def _v_all_f(_v_f, _all_f, v, G):
    if G == None:
        G = v
        return _all_f(G)
    return _v_f(v, G)

def dedge2edge(v, G = None):
    return _v_all_f(_v_dedge2edge, _all_dedge2edge, v, G)
def vtc(v, G = None):
    return _v_all_f(_v_vtc, _all_vtc, v, G)
def uedges(v, G = None):
    return _v_all_f(_v_uedges, _all_uedges, v, G)
def dedges(v, G = None):
    return _v_all_f(_v_dedges, _all_dedges, v, G)

where_uedge = where_edge_idx
#where_dedge([v, [u,]] dedge, G)
def where_dedge(v, u, dedge = None, G = None):
    if G == None:
        if dedge == None:
            dedge, G = v, u
            uedge = to_uedge(dedge, G)
            vl, ul = G[idx2loc_idx][uedge]
            if not is_uedge(dedge, G):
                vl, ul = ul, vl
            return vl, ul
        v, dedge, G = v, u, dedge
        uedge = to_uedge(dedge, G)
        return where_uedge(v, uedge, G)
    uedge = to_uedge(dedge, G)
    return where_uedge(v, u, uedge, G)


edge2uedge = edge_index
def edge2dedge(e,G):
    dedge = edge2uedge(e,G)
    u, v = e
    if u > v:
        dedge += ne(G)
    return dedge

def flip_dedge(dedge,G):
    m = ne(G)
    if dedge < m:
        dedge += m
    else:
        dedge -= m
    return dedge


def next_out(dedge,G):
    s, _ = dedge2edge(dedge, G)
    s_loc, _ = where_dedge(dedge, G)
    s_loc += 1
    s_loc -= degree(s, G)
    return dedges(s, G)[s_loc]
def prev_out(dedge,G):
    s, _ = dedge2edge(dedge, G)
    s_loc, _ = where_dedge(dedge, G)
    s_loc -= 1
    return dedges(s, G)[s_loc]
def next_in(dedge,G):
    _, t = dedge2edge(dedge, G)
    _, t_loc = where_dedge(dedge, G)
    t_loc += 1
    t_loc -= degree(t, G)
    dedge = dedges(t, G)[t_loc]
    dedge = flip_dedge(dedge, G)
    return dedge
def prev_in(dedge,G):
    _, t = dedge2edge(dedge, G)
    _, t_loc = where_dedge(dedge, G)
    t_loc -= 1
    dedge = dedges(t, G)[t_loc]
    dedge = flip_dedge(dedge, G)
    return dedge


def flip_next_out(dedge,G): return flip_dedge(next_out(dedge,G), G)
def flip_prev_out(dedge,G): return flip_dedge(prev_out(dedge,G), G)
def flip_next_in(dedge,G): return flip_dedge(next_in(dedge,G), G)
def flip_prev_in(dedge,G): return flip_dedge(prev_in(dedge,G), G)
#############################################
'''
def subgraphs_from_vtc_list(vtc_list, G):
    ls = inner_sort_ints_list(G.nv(), vtc_list)
'''

def edges_list2vtc_list(gph_order, edges_list):
    vtc_ls = tuple(tuple(v for e in es for v in e) for es in edges_list)
    vtc_ls = inner_sort_ints_list(gph_order, vtc_ls)
    vtc_ls = tuple(group_unify(vtc) for vtc in vtc_ls)
    return vtc_ls


def reindex_edges_list(gph_order, node2vtc, node2edges):
    for vtc in node2vtc:
        assert is_sorted(vtc)
    for edges in node2edges:
        assert is_sorted(edges)

    node2new_edges = []
    buf = [None]*gph_order
    for vtc, edges in zip(node2vtc, node2edges):
        for new_vtx, old_vtx in enumerate(vtc):
            buf[old_vtx] = new_vtx

        new_edges = []
        for u, v in edges:
            u, v = buf[u], buf[v]
            new_edges.append((u,v))

        node2new_edges.append(tuple(new_edges))

    return tuple(node2new_edges)
        
def subgraphs_from_uedges_list(list_of_unsorted_uedges, G):
    n = G.nv()
    es = G.edges()
    uedges_list = inner_sort_ints_list(G.ne(), list_of_unsorted_uedges)
    edges_list = tuple(tuple(es[uedge] for uedge in uedges) for uedges in uedges_list)
    vtc_ls = edges_list2vtc_list(n, edges_list)
    new_edges_ls = reindex_edges_list(n, vtc_ls, edges_list)
    subgraphs = tuple(graph(len(vtc), new_edges) for vtc, new_edges in zip(vtc_ls, new_edges_ls))
    original_vtc_list, original_uedges_list = vtc_ls, uedges_list
    return subgraphs, original_vtc_list, original_uedges_list



    
    
################################################

_num_edges = num_edges
_order = order
_adjacency_list = adjacency_list
_vertices = vertices
_edges = edges
_neighbors = neighbors
_degree = degree
_is_adjacent = is_adjacent
_edge_index = edge_index
_incident_edge_indices = incident_edge_indices
_where_edge_idx = where_edge_idx
_relabel = relabel
_relabel_back = relabel_back



_dedge2edge = dedge2edge
_is_uedge = is_uedge
_to_uedge = to_uedge
_to_dedges = to_dedges
_vtc = vtc
_uedges = uedges
_dedges = dedges
_where_dedge = where_dedge
_edge2dedge = edge2dedge
_flip_dedge = flip_dedge

_next_out = next_out
_prev_out = prev_out
_next_in = next_in
_prev_in = prev_in

_flip_next_out = flip_next_out
_flip_prev_out = flip_prev_out
_flip_next_in = flip_next_in
_flip_prev_in = flip_prev_in



class graph:
    def __init__(self, graph_order, edges=None):
        self._G = make_graph(graph_order, edges)
        self._hash = hash(self._ad_ls())
    def _ad_ls(self): return self._G[adjacency_list_idx]
    def num_edges(self): return _num_edges(self._G)
    def order(self): return _order(self._G)
    def adjacency_list(self): return _adjacency_list(self._G)
    def vertices(self): return _vertices(self._G)
    def edges(self): return _edges(self._G)
    def neighbors(self, v): return _neighbors(v, self._G)
    def degree(self, v): return _degree(v, self._G)
    def is_adjacent(self, u, v): return _is_adjacent(u, v, self._G)
    def edge_index(self, e): return _edge_index(e, self._G)
    def incident_edge_indices(self, v): return _incident_edge_indices(v, self._G)
    def where_edge_idx(self, v, u, idx = None):
        ls = [v, u, idx, None]
        ls[ls.index(None)] = self._G
        return _where_edge_idx(*ls)
    def __repr__(self): return 'graph({})'.format(self._ad_ls())
    def relabel(self, label):
        # label = old_vtx2new_vtx and self is old
        return graph(_relabel(self._ad_ls(), label))
    def relabel_back(self, label):
        # label = old_vtx2new_vtx and self is new
        return graph(_relabel_back(self._ad_ls(), label))
    def __hash__(self): return self._hash

    ne = num_edges 
    nv = num_vtc = order
    uedge2edge = edges
    def is_uedge(self, dedge): return _is_uedge(dedge, self._G)
    def to_uedge(self, dedge): return _to_uedge(dedge, self._G)
    def to_dedges(self, dedge): return _to_dedges(dedge, self._G)
    
    def dedge2edge(self, v = None):
        ls = [v, None]
        ls[ls.index(None)] = self._G
        return _dedge2edge(*ls)
    def vtc(self, v = None):
        ls = [v, None]
        ls[ls.index(None)] = self._G
        return _vtc(*ls)
    def uedges(self, v = None):
        ls = [v, None]
        ls[ls.index(None)] = self._G
        return _uedges(*ls)
    def dedges(self, v = None):
        ls = [v, None]
        ls[ls.index(None)] = self._G
        return _dedges(*ls)
    where_uedge = where_edge_idx
    def where_dedge(self, v, u = None, dedge = None):
        ls = [v, u, dedge, None]
        ls[ls.index(None)] = self._G
        return _where_dedge(*ls)
    edge2uedge = edge_index
    def edge2dedge(self, e): return _edge2dedge(e, self._G)
    def flip_dedge(self, dedge): return _flip_dedge(dedge, self._G)

    def __eq__(self, other): return self.adjacency_list() == other.adjacency_list()
    def __ne__(self, other): return not (self == other)
    def next_out(self, dedge): return _next_out(dedge, self._G)
    def prev_out(self, dedge): return _prev_out(dedge, self._G)
    def next_in(self, dedge): return _next_in(dedge, self._G)
    def prev_in(self, dedge): return _prev_in(dedge, self._G)

    def flip_next_out(self, dedge): return _flip_next_out(dedge, self._G)
    def flip_prev_out(dedge,G): return _flip_prev_out(dedge, self._G)
    def flip_next_in(dedge,G): return _flip_next_in(dedge, self._G)
    def flip_prev_in(dedge,G): return _flip_prev_in(dedge, self._G)
# union, K_n, K_n_m, G_0, G_1, linear_graph, cycle_graph, star_graph, full_k_ary_tree, complete_k_ary_tree
def union(iterable):
    es = []
    n = 0
    for g in iterable:
        for u,v in g.edges():
            es.append((u+n, v+n))
        n += g.order()
    return graph(n, es)



def K_n(n): #complete graph
    t = ((i for i in range(n) if i != j) for j in range(n))
    return graph(t)

def K_n_m(n,m): #complete bipartite graph / star_graph == K_1_n
    t = ((i for i in range(n+m) if (i < n) ^ (j < n)) for j in range(n+m))
    return graph(t)

def G_0():
    return graph(())

def G_1():
    return graph((()))

def linear_graph(n):
    t = ((i, i+1) for i in range(n-1))
    return graph(n, t)

def cycle_graph(n):
    assert n > 2
    t = [(i, i+1) for i in range(n-1)]
    t.append((n-1,0))
    return graph(n, t)

def star_graph(n):
    assert n > 0
    return K_n_m(1, n-1)

def full_k_ary_tree(k, depth):
    if depth == 0:
        return G_1()
    es = []
    j = 0
    for d in range(depth):
        i = j
        j = len(es) + 1
        for _i in range(i,j):
            es += [(_i, len(es)+1 + m) for m in range(k)]

    return graph(len(es) + 1, es)

def complete_k_ary_tree(k, n):
    assert n > 0
    es = []
    j = 0
    while j < n:
        i = j
        j = len(es) + 1
        for _i in range(i,j):
            es += [(_i, len(es)+1 + m) for m in range(k)]
    del es[n-1:] 
    return graph(n, es)

    
