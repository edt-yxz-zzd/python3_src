

'''
connected_components
BC_tree
SPQR_tree
'''

from .bucket_sort import bucket_sort, group, bucket_sorts, \
     group_unify, group_to_list, is_sorted, inner_sorts_ints_list
from .DFS import *
from .simple_undirected_graph import graph, subgraphs_from_uedges_list, edges_list2vtc_list, reindex_edges_list


spqr_tree_gph_node = 'spqr_gph_node'
spqr_tree_no_co_gph_uedge = 'spqr_no_co_gph_uedge'

# uedge type
spqr_tree_real_pure = 'r''eal_pure'
spqr_tree_virtual_pure = 'v''irtual_pure'
spqr_tree_both_real_virtual = 'b''oth_real_virtual'


def connected_component2vtc_in_dfs_preordering(G):
    cs = []
    uedges_ls = []
    for action, argv in DFS(G):
        if action == enter_tree:
            G, r = argv
            cs.append([r])
            uedges = []
            uedges_ls.append(uedges)
        elif action == exit_tree:
            G, r = argv
        elif action == enter_tree_edge:
            G, idx, p, v = argv
            cs[-1].append(v)
            uedges.append(idx)
        elif action == exit_tree_edge:
            G, idx, p, v = argv
        elif action == visit_back_edge:
            G, idx, p, v = argv
            uedges.append(idx)
        elif action == revisit_back_edge:
            G, idx, p, v = argv
        else:
            raise 'unknown'
    vtc_ls = tuple(tuple(c) for c in cs)
    uedges_ls = tuple(tuple(uedges) for uedges in uedges_ls)
    return vtc_ls, uedges_ls

def make_connected_components(G):
    vtc_ls, uedges_ls = connected_component2vtc_in_dfs_preordering(G)
    subgraphs, sub_vtx2gph_vtx, sub_uedge2gph_uedge = \
               subgraphs_from_uedges_list(uedges_ls, G)

    subgraphs, sub_vtx2gph_vtx = list(subgraphs), list(sub_vtx2gph_vtx)
    g0 = graph(((),))
    for i, uedges in enumerate(uedges_ls):
        if uedges: continue
        assert len(vtc_ls[i]) == 1
        v, = vtc_ls[i]
        subgraphs[i] = g0
        sub_vtx2gph_vtx[i] = (v,)
    subgraphs, sub_vtx2gph_vtx = tuple(subgraphs), tuple(sub_vtx2gph_vtx)
    
    gph_order = G.nv()
    num_components = len(subgraphs)
    return gph_order, num_components, \
           subgraphs, sub_vtx2gph_vtx, sub_uedge2gph_uedge

class connected_components:
    def __init__(self, G):
        self.gph_order, self.num_components, self.subgraphs, \
                        self.sub_vtx2gph_vtx, self.sub_uedge2gph_uedge \
                        = make_connected_components(G)


def reindex(gph_order, gph_edges, node2vtc, node2uedges):
    for vtc in node2vtc:
        assert is_sorted(vtc)
    for uedges in node2uedges:
        assert is_sorted(uedges)

    node2new_edges = []
    buf = [None]*gph_order
    es = gph_edges
    for vtc, uedges in zip(node2vtc, node2uedges):
        for new_vtx, old_vtx in enumerate(vtc):
            buf[old_vtx] = new_vtx

        edges = []
        for uedge in uedges:
            u, v = es[uedge]
            u, v = buf[u], buf[v]
            edges.append((u,v))

        node2new_edges.append(tuple(edges))

    return tuple(node2new_edges)
        
def _calc_vtx2node_vtc(gph_order, node2gph_vtc):
    n = gph_order
    vtx2node_vtc = tuple([] for _ in range(n))
    set2ints_to_int2set_locations(node2gph_vtc, vtx2node_vtc)
    vtx2node_vtc = tuple(tuple(n_v) for n_v in vtx2node_vtc)
    return vtx2node_vtc
def _calc_uedge2node_uedge(G, node2gph_uedges):
    uedge2node_uedge = [None]*G.ne()
    set2ints_to_int2set_location(node2gph_uedges, uedge2node_uedge)
    uedge2node_uedge = tuple(uedge2node_uedge)
    return uedge2node_uedge

def set2ints_to_int2set_location(set2ints, out_int2set_location):
    for set_idx, ints in enumerate(set2ints):
        for loc, i in enumerate(ints):
            out_int2set_location[i] = (set_idx, loc)
def set2ints_to_int2set_locations(set2ints, out_int2set_locations):
    for set_idx, ints in enumerate(set2ints):
        for loc, i in enumerate(ints):
            out_int2set_locations[i].append((set_idx, loc))

def set2ints_to_int2set(set2ints, out_int2set, set_idx_base = 0):
    for set_idx, ints in enumerate(set2ints, set_idx_base):
        for i in ints:
            out_int2set[i] = set_idx

def int2set_to_set2ints(int2set, out_set2ints, set_idx_base = 0):
    for i, set_idx in enumerate(int2set, set_idx_base):
        out_set2ints[set_idx].append(i)

def set2ints_to_int2sets(set2ints, out_int2sets):
    for set_idx, ints in enumerate(set2ints):
        for i in ints:
            out_int2sets[i].append(set_idx)

class bc_tree:
    def __init__(self, G):
        self.num_connected_component, self.gph_order, self.bc_order, \
            self.gph_vtx2bc_nodes, self.gph_vtx2bc_node_vtc, \
            self.gph_uedge2bc_node, self.gph_uedge2bc_node_uedge, \
            self.bc_tree, self.bc_node2gph_vtc, self.bc_node2gph_uedges, self.bc_node2subgraph, \
            self.cut_node_base, self.block_node_base \
            = BC_tree(G)

    def is_isolated_node(self, bc_node):
        return 0 <= bc_node < self.cut_node_base
    def is_cut_node(self, bc_node):
        return self.cut_node_base <= bc_node < self.block_node_base
    def is_block_node(self, bc_node):
        return self.block_node_base <= bc_node < self.bc_order
    def is_nv2_block_node(self, bc_node):
        return self.is_block_node(bc_node) and self.node_nv(bc_node) == 2
    def node_nv(self, node): return len(self.bc_node2gph_vtc[node])
        
def BC_tree(G):
    block_uedges = []
    uedges = []
    n = G.order()
    lowpt = [None]*n
    order = [None]*n
    cut_vertices = []
    curr = 0
    isolated_vertices = []
    len_uedges = []
    num_connected_component = 0
    for action, argv in DFS(G):
        if action == enter_tree:
            G, r = argv
            lowpt[r] = curr
            order[r] = curr
            curr += 1
            num_connected_component += 1
        elif action == exit_tree:
            G, r = argv
            if G.degree(r) == 0:
                isolated_vertices.append(r)
            else:
                cut_vertices.pop()
            assert len(len_uedges) == 0
            assert len(uedges) == 0
        elif action == enter_tree_edge:
            G, idx, p, v = argv
            lowpt[v] = curr
            order[v] = curr
            curr += 1
            len_uedges.append(len(uedges))
        elif action == exit_tree_edge:
            G, idx, p, v = argv
            if lowpt[p] > lowpt[v]:
                lowpt[p] = lowpt[v]
            uedges.append(idx)
            if lowpt[v] >= order[p]:
                cut_vertices.append(p)
                block_uedges.append(tuple(uedges[len_uedges[-1]:]))
                del uedges[len_uedges[-1]:]
            len_uedges.pop()
        elif action == visit_back_edge:
            G, idx, p, v = argv
            if lowpt[p] > order[v]:
                lowpt[p] = order[v]
            uedges.append(idx)
        elif action == revisit_back_edge:
            G, idx, p, v = argv
        else:
            raise 'unknown'


    isolated_vertices = tuple(isolated_vertices)
    cut_vertices = group_unify(bucket_sort(cut_vertices, lambda e:e, G.nv()))
    cut_node_base = len(isolated_vertices)
    block_node_base = cut_node_base + len(cut_vertices)
    
    
    uedge2node = [None]*G.ne()
    set2ints_to_int2set(block_uedges, uedge2node)
    block_uedges = list([] for _ in range(len(block_uedges)))
    int2set_to_set2ints(uedge2node, block_uedges)
    
    block_uedges = bucket_sort(block_uedges, lambda e:e[0], G.ne())
    block_uedges = tuple(tuple(uedges) for uedges in block_uedges)
    
    set2ints_to_int2set(block_uedges, uedge2node, block_node_base)
    uedge2node = tuple(uedge2node)
    

    vertex2nodes = list([] for _ in range(n))
    int2set_to_set2ints(isolated_vertices, vertex2nodes)
    int2set_to_set2ints(cut_vertices, vertex2nodes, cut_node_base)


    bc_edges = []
    for b_node, uedges in enumerate(block_uedges, block_node_base):
        for uedge in uedges:
            for x in G.uedge2edge()[uedge]:
                v2n = vertex2nodes[x]
                if len(v2n) and v2n[-1] == b_node:
                    continue
                v2n.append(b_node)
                if len(v2n) > 1:
                    bc_edges.append((v2n[0]-cut_node_base, b_node-block_node_base))

    vertex2nodes = tuple(tuple(v2n) for v2n in vertex2nodes)
    bc_edges = bucket_sorts(bc_edges, lambda i,e: e[i], (1,0), (len(block_uedges), len(cut_vertices)))
    bc_edges = tuple((c+cut_node_base, b+block_node_base) for c, b in bc_edges)
    
    
    N = len(isolated_vertices) + len(cut_vertices) + len(block_uedges)
    bc_tree = graph(N, bc_edges)
    
    node2vtc = tuple([] for _ in range(N))
    set2ints_to_int2sets(vertex2nodes, node2vtc)
    node2vtc = tuple(tuple(vtc) for vtc in node2vtc)

    node2uedges = ((),)*block_node_base + block_uedges
    node2new_edges = reindex(n, G.edges(), node2vtc, node2uedges)

    node2subgraph = tuple(graph(len(vtc), new_edges) \
                          for vtc, new_edges in zip(node2vtc, node2new_edges))

    gph_vtx2bc_node_vtc = _calc_vtx2node_vtc(n, node2vtc)
    gph_uedge2bc_node_uedge = _calc_uedge2node_uedge(G, node2uedges)
    assert cut_node_base <= num_connected_component <= len(isolated_vertices) + len(block_uedges) <= n
    assert cut_node_base <= block_node_base <= n

    gph_order = n
    bc_order = N
    gph_vtx2bc_nodes = vertex2nodes
    gph_uedge2bc_node = uedge2node
    bc_tree
    bc_node2gph_vtc = node2vtc
    bc_node2gph_uedges = node2uedges
    bc_node2subgraph = node2subgraph
    return num_connected_component, gph_order, bc_order, \
           gph_vtx2bc_nodes, gph_vtx2bc_node_vtc, \
           gph_uedge2bc_node, gph_uedge2bc_node_uedge, \
           bc_tree, bc_node2gph_vtc, bc_node2gph_uedges, bc_node2subgraph, \
           cut_node_base, block_node_base

def _spqr_inner_sort_components(n, components):
    components = tuple((org, tuple((min(a,b), max(a,b)) for a,b in edges)) for org, edges in components)
    components = tuple((org, tuple(bucket_sorts(edges, lambda i,e: e[i], (1,0), (len(org),)*2))) \
                 for org, edges in components)
    return components

def _spqr_edge2component(G, components):
    n = G.order()
    components = _spqr_inner_sort_components(n, components)
    
    edges = list((org[a], org[b], c, i)for c, (org, edges) in enumerate(components) \
                 for i, (a,b) in enumerate(edges))
    edges += [(a, b, -1, i) for i, (a,b) in enumerate(G.edges())]
    for a, b, _, _ in edges:
        assert a < b
    edges = bucket_sorts(edges, lambda i,e: e[i], (1,0), (n,n))
    
    block = group(edges, lambda e: e[:2])
    edge2component = tuple((edges[i][:2], \
                            list((c, idx) for a, b, c, idx in edges[i:j])) \
                           for i, j in block)
    for i in range(len(block)):
        ls = edge2component[i][-1]
        assert len(ls) > 1
        if len(ls) == 2 and ls[-1][0] == -1:
            ls.pop()

    return components, edge2component

def _spqr_component_type(G, components):
    n = G.order()
    component_type = ['R']*len(components)
    for i, (org, edges) in enumerate(components):
        assert len(org) > 1
        if len(org) == 2:
            assert n == 2
            assert len(components) == 1
            assert len(edges) == 1
            assert i == 0
            component_type[i] = 'Q'
        elif len(org) == 3:
            assert len(edges) == 3
            component_type[i] = 'S'
        elif len(edges) == len(org):
            component_type[i] = 'S'
        else:
            assert len(org)*3 <= len(edges)*2

    return component_type


def _spqr_component_edges2components(n, component_edges):
    edges_of_nodes = component_edges

    '''
    vertices_of_nodes = _calc_vertices_of_edges_of_nodes(n, edges_of_nodes)

    reorder = [None]*n
    new_edges_of_nodes = []
    for edges, vertices in zip(edges_of_nodes, vertices_of_nodes):
        for i, u in enumerate(vertices):
            reorder[u] = i
        es = tuple((reorder[a], reorder[b]) for a, b in edges)
        new_edges_of_nodes.append(es)
    '''
    
    vertices_of_nodes = edges_list2vtc_list(n, edges_of_nodes)
    edges_of_nodes = tuple(tuple((min(u,v), max(u,v)) for u,v in edges) \
                           for edges in edges_of_nodes)
    edges_of_nodes = inner_sorts_ints_list(edges_of_nodes, lambda i,e:e[i], (1,0), (n,n))
    new_edges_of_nodes = reindex_edges_list(n, vertices_of_nodes, edges_of_nodes)
    
    new_components = list(zip(vertices_of_nodes, new_edges_of_nodes))
    return new_components


def _spqr_merge(G, components, edge2component):
    n = G.order()
    component_type = _spqr_component_type(G, components)
    
    merge_to = list(range(len(components)))
    idx_del = list([] for i in range(len(components)))
    for _, ls in edge2component:
        if len(ls) == 2:
            (a,ia), (b,ib) = ls
            if component_type[a] == component_type[b] == 'S':
                assert a < b
                merge_to[b] = a
                idx_del[a].append(ia)
                idx_del[b].append(ib)

    new_components = list([] for i in range(len(merge_to)))
    old_cs = []
    for i in range(len(merge_to)):
        if len(idx_del[i]):
            j = merge_to[i] = merge_to[merge_to[i]]
            idx_del[i].sort()
            org, edges = components[i]
            pre = 0
            new_es = []
            for d in idx_del[i]:
                new_es += edges[pre : d]
                pre = d + 1
            else:
                new_es += edges[pre:]
            new_es = [(org[a], org[b]) for a, b in new_es]
            new_components[j] += new_es
        else:
            old_cs.append(components[i])

    nodes = tuple(edges for edges in new_components if len(edges))
    new_components = _spqr_component_edges2components(n, nodes)

    new_components += old_cs
    new_components = tuple(new_components)
    return new_components

def _spqr_sort_components(n, components):
    components = _spqr_inner_sort_components(n, components)
    if len(components) > 1: # no 'Q'
        components = bucket_sorts(components, lambda i, e: e[0][i], [2,1,0], [n]*3)
    Ss = []
    Rs = []
    for c in components:
        vertices, edges = c
        if len(vertices) == len(edges):#'S'
            Ss.append(c)
        else:
            Rs.append(c)
    num_S = len(Ss)
    components = Ss + Rs
    return num_S, components

def _SRcomponents2spqr(G, SRcomponents):
    n = G.order()
    num_S, SRcomponents = _spqr_sort_components(n, SRcomponents)
    components, edge2component = _spqr_edge2component(G, SRcomponents)

    P_real_components = []
    P_virtual_pure_components = []
    P_edges = ((0,1),)
    P_real_neighbors = []
    P_virtual_pure_neighbors = []
    for edge, component_idx_uedge_list in edge2component:
        if len(component_idx_uedge_list) > 1:
            original = edge
            neighbors = tuple(idx for idx, uedge in component_idx_uedge_list)
            if neighbors[-1] == -1:
                P_components = P_real_components
                P_neighbors = P_real_neighbors
                neighbors = neighbors[:-1]
            else:
                P_components = P_virtual_pure_components
                P_neighbors = P_virtual_pure_neighbors
            P_components.append((original, P_edges))
            P_neighbors.append(neighbors)
    
    num_P_real = len(P_real_components)
    P_components = tuple(P_real_components + P_virtual_pure_components)
    num_P = len(P_components)
    
    P_neighbors = P_real_neighbors + P_virtual_pure_neighbors
    spqr_edges = tuple((p_node, num_P + idx) \
                       for p_node, neighbors in enumerate(P_neighbors) for idx in neighbors)
    spqr_nodes = P_components + components
    spqr_node2gph_vtc = tuple(org for org, _ in spqr_nodes)
    spqr_node2subedges = tuple(subedges for org, subedges in spqr_nodes)
    return _SRcomponents2spqr_last_handle(n, G.edges(), \
                                          spqr_node2gph_vtc, spqr_node2subedges, spqr_edges, \
                                          num_P_real, num_P, num_S)

def _SRcomponents2spqr_last_handle(gph_order, gph_uedge2edges, \
                                   spqr_node2gph_vtc, spqr_node2subedges, spqr_edges, \
                                   num_P_real, num_P, num_S):
    n = gph_order
    gph_ne = len(gph_uedge2edges)
    spqr_order = len(spqr_node2gph_vtc)
    assert spqr_order > 0
    
    if spqr_order == 1 and len(spqr_node2gph_vtc[0]) ==  2:
        # spqr tree is a Q node
        assert num_P + num_S == 0
        assert spqr_node2gph_vtc == ((0,1),)
        assert spqr_node2subedges == (((0,1),),)
        num_Q = 1
    else:
        num_Q = 0

    num_P_virtual_pure = num_P - num_P_real
    P_node_virtual_pure_base = num_P_real
    S_node_base = num_P
    R_node_base = S_node_base + num_S
    Q_node_base = spqr_order - num_Q
    num_R = Q_node_base - R_node_base

    
    
    
    gph_vtx2spqr_nodes = tuple([] for _ in range(n))
    set2ints_to_int2sets(spqr_node2gph_vtc, gph_vtx2spqr_nodes)
    gph_vtx2spqr_nodes = tuple(tuple(nodes) for nodes in gph_vtx2spqr_nodes)
    
    gph_vtx2spqr_node_vtc = _calc_vtx2node_vtc(gph_order, spqr_node2gph_vtc)

    spqr_node2subgraph = tuple(graph(len(vtc), subedges) \
                               for vtc, subedges in zip(spqr_node2gph_vtc, spqr_node2subedges))
    u_v_node_uedge_list = tuple((org[u],org[v],(node,uedge)) for node, (org, subedges) in \
                                enumerate(zip(spqr_node2gph_vtc, spqr_node2subedges))\
                                for uedge, (u, v) in enumerate(subedges))
    u_v_node_uedge_list += tuple((u,v,(spqr_tree_gph_node,uedge)) \
                                 for uedge, (u,v) in enumerate(gph_uedge2edges))
    u_v_node_uedge_list = bucket_sorts(u_v_node_uedge_list, lambda i,e:e[i], (1,0), (n,n))
    block = group(u_v_node_uedge_list, lambda e:e[:2])
    spqr_node_uedge2spqr_gph_node_uedges = tuple(tuple([] for _ in range(len(subedges))) \
                                                 for subedges in spqr_node2subedges)
    spqr_node_uedge2spqr_uedge_type = tuple([None]*len(subedges) \
                                             for subedges in spqr_node2subedges)
    gph_uedge2spqr_node_uedges = tuple([] for _ in range(gph_ne))
    gph_uedge2spqr_uedge_type = [None]*gph_ne

    def _unpack(k):
        node_uedge = u_v_node_uedge_list[k][-1]
        node, uedge = node_uedge
        return node_uedge, node, uedge
    def _P_nonP(k):
        nonP_node_uedge, nonP_node, nonP_uedge = _unpack(k)
        assert nonP_node >= num_P
        spqr_node_uedge2spqr_gph_node_uedges[P_node][P_uedge].append(nonP_node_uedge)
        spqr_node_uedge2spqr_uedge_type[nonP_node][nonP_uedge] = uedge_type
        spqr_node_uedge2spqr_gph_node_uedges[nonP_node][nonP_uedge].append(P_node_uedge)
    def _P_gph():
        #spqr_node_uedge2spqr_uedge_types[P_node][P_uedge] = uedge_type
        #spqr_node_uedge2spqr_node_uedges[P_node][P_uedge].append(gho_n1_uedge)
        gph_uedge2spqr_uedge_type[gph_uedge] = uedge_type
        gph_uedge2spqr_node_uedges[gph_uedge].append(P_node_uedge)
    def _P_nonP_gph(k):
        nonP_node_uedge, nonP_node, nonP_uedge = _unpack(k)
        assert nonP_node >= num_P
        spqr_node_uedge2spqr_gph_node_uedges[P_node][P_uedge].append(nonP_node_uedge)
        gph_uedge2spqr_node_uedges[gph_uedge].append(nonP_node_uedge)
        spqr_node_uedge2spqr_uedge_type[nonP_node][nonP_uedge] = uedge_type
        spqr_node_uedge2spqr_gph_node_uedges[nonP_node][nonP_uedge].append(P_node_uedge)
        spqr_node_uedge2spqr_gph_node_uedges[nonP_node][nonP_uedge].append(gph_n1_uedge)
        
        
    def _nonP_gph(k):
        nonP_node_uedge, nonP_node, nonP_uedge = _unpack(k)
        assert nonP_node >= num_P
        spqr_node_uedge2spqr_uedge_type[nonP_node][nonP_uedge] = uedge_type
        spqr_node_uedge2spqr_gph_node_uedges[nonP_node][nonP_uedge].append(gph_n1_uedge)
        gph_uedge2spqr_uedge_type[gph_uedge] = uedge_type
        gph_uedge2spqr_node_uedges[gph_uedge].append(nonP_node_uedge)
        
        
    for i, j in block:
        assert j >= i+2
        if j == i+2:
            uedge_type = spqr_tree_real_pure
            # real = real_pure + both_real_virtual = non_virtual_pure
            gph_n1_uedge, _n1, gph_uedge = _unpack(j-1)
            assert _n1 == spqr_tree_gph_node
            _nonP_gph(i)
        else:
            P_node_uedge, P_node, P_uedge = _unpack(i)
            assert P_node < num_P
            assert P_uedge == 0
            _, node, _ = _unpack(j-1)
            if node == spqr_tree_gph_node:
                assert P_node < num_P_real
                uedge_type = spqr_tree_both_real_virtual
                gph_n1_uedge, _n1, gph_uedge = _unpack(j-1)
                assert _n1 == spqr_tree_gph_node
                _P_gph()
                for k in range(i+1, j-1):
                    _P_nonP_gph(k)
                spqr_node_uedge2spqr_uedge_type[P_node][P_uedge] = uedge_type
                spqr_node_uedge2spqr_gph_node_uedges[P_node][P_uedge].append(gph_n1_uedge)
            else:
                assert P_node >= num_P_real
                uedge_type = spqr_tree_virtual_pure
                # virtual = virtual_pure + both_real_virtual = non_real_pure
                for k in range(i+1, j):
                    _P_nonP(k)
                spqr_node_uedge2spqr_uedge_type[P_node][P_uedge] = uedge_type
        
    spqr_node_uedge2spqr_gph_node_uedges = \
        tuple(tuple(tuple(spqr_gph_node_uedges) \
                    for spqr_gph_node_uedges in uedge2spqr_gph_node_uedges) \
              for uedge2spqr_gph_node_uedges in spqr_node_uedge2spqr_gph_node_uedges)
    spqr_node_uedge2spqr_uedge_type = tuple(tuple(uedge2type) \
                                            for uedge2type in spqr_node_uedge2spqr_uedge_type)
    gph_uedge2spqr_node_uedges = tuple(tuple(spqr_node_uedges) \
                                       for spqr_node_uedges in gph_uedge2spqr_node_uedges)
    gph_uedge2spqr_uedge_type = tuple(gph_uedge2spqr_uedge_type)






    spqr_tree = graph(spqr_order, spqr_edges)

    spqr_node2gph_uedges_real_pure = tuple([] for _ in spqr_tree.vtc())
    spqr_node2gph_uedges_non_virtual_pure = tuple([] for _ in spqr_tree.vtc())
    spqr_node_uedge_non_virtual_pure2gph_uedge = \
        tuple([spqr_tree_no_co_gph_uedge]*subgraph.ne() for subgraph in spqr_node2subgraph)
    for node, uedge2spqr_gph_node_uedges in enumerate(spqr_node_uedge2spqr_gph_node_uedges):
        for uedge, node_uedges in enumerate(uedge2spqr_gph_node_uedges):
            assert len(node_uedges)
            uedge_type = spqr_node_uedge2spqr_uedge_type[node][uedge]
            if uedge_type == spqr_tree_virtual_pure:
                neighbor_node, co_uedge = node_uedges[-1]
                assert neighbor_node != spqr_tree_gph_node
                continue
            gph_n1, gph_uedge = node_uedges[-1]
            assert gph_n1 == spqr_tree_gph_node
            spqr_node_uedge_non_virtual_pure2gph_uedge[node][uedge] = gph_uedge
            spqr_node2gph_uedges_non_virtual_pure[node].append(gph_uedge)
            if uedge_type == spqr_tree_real_pure:
                spqr_node2gph_uedges_real_pure[node].append(gph_uedge)
            else:
                assert uedge_type == spqr_tree_both_real_virtual

    spqr_node2gph_uedges_real_pure = tuple(tuple(gph_uedges) \
        for gph_uedges in spqr_node2gph_uedges_real_pure)
    spqr_node2gph_uedges_non_virtual_pure = tuple(tuple(gph_uedges) \
        for gph_uedges in spqr_node2gph_uedges_non_virtual_pure)
    spqr_node_uedge_non_virtual_pure2gph_uedge = tuple(tuple(spqr_uedge2gph_uedge) \
        for spqr_uedge2gph_uedge in spqr_node_uedge_non_virtual_pure2gph_uedge)

    spqr_node_uedge2spqr_node_uedges = \
        tuple(tuple(tuple((node, uedge) \
                          for node, uedge in spqr_gph_node_uedges \
                          if node != spqr_tree_gph_node) \
                    for spqr_gph_node_uedges in uedge2spqr_gph_node_uedges) \
              for uedge2spqr_gph_node_uedges in spqr_node_uedge2spqr_gph_node_uedges)
    gph_uedge2spqr_nodes = tuple(tuple(node for node, uedge in spqr_node_uedges) \
                                       for spqr_node_uedges in gph_uedge2spqr_node_uedges)


    spqr_node_vtx2gph_vtx = spqr_node2gph_vtc
    return gph_order, spqr_order, \
           gph_vtx2spqr_nodes, gph_vtx2spqr_node_vtc, \
           gph_uedge2spqr_nodes, gph_uedge2spqr_node_uedges, \
           gph_uedge2spqr_uedge_type, \
           \
           spqr_tree, spqr_node2subgraph, \
           spqr_node_uedge2spqr_gph_node_uedges, spqr_node_uedge2spqr_node_uedges, \
           spqr_node2gph_uedges_real_pure, spqr_node2gph_uedges_non_virtual_pure, \
           \
           spqr_node_vtx2gph_vtx, \
           spqr_node_uedge_non_virtual_pure2gph_uedge, \
           spqr_node_uedge2spqr_uedge_type, \
           \
           P_node_virtual_pure_base, S_node_base, R_node_base, Q_node_base, \
           num_P_real, num_P_virtual_pure, num_P, num_S, num_R, num_Q



# O(n^2) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def SPQR_tree(G):
    n = G.order()
    assert is_biconnected(G)
    assert n > 1
    components = _SPQR_tree(0, tuple(range(n)), G.edges())
    components, edge2component = _spqr_edge2component(G, components)
    SRcomponents = _spqr_merge(G, components, edge2component)
    return _SRcomponents2spqr(G, SRcomponents)
    

class spqr_tree:
    def __init__(self, G, make_spqr_tree = SPQR_tree):
        self.gph_order, self.spqr_order, \
            self.gph_vtx2spqr_nodes, self.gph_vtx2spqr_node_vtc, \
            self.gph_uedge2spqr_nodes, self.gph_uedge2spqr_node_uedges, \
            self.gph_uedge2spqr_uedge_type, \
            \
            self.spqr_tree, self.spqr_node2subgraph, \
            self.spqr_node_uedge2spqr_gph_node_uedges, self.spqr_node_uedge2spqr_node_uedges, \
            self.spqr_node2gph_uedges_real_pure, self.spqr_node2gph_uedges_non_virtual_pure, \
            \
            self.spqr_node_vtx2gph_vtx, \
            self.spqr_node_uedge_non_virtual_pure2gph_uedge, \
            self.spqr_node_uedge2spqr_uedge_type, \
            \
            self.P_node_virtual_pure_base, self.S_node_base, self.R_node_base, self.Q_node_base, \
            self.num_P_real, self.num_P_virtual_pure, self.num_P, \
            self.num_S, self.num_R, self.num_Q \
            = make_spqr_tree(G)

    def is_P_node(self, node): return 0 <= node < self.S_node_base
    def is_P_real_node(self, node): return 0 <= node < self.num_P_real
    def is_S_node(self, node): return self.S_node_base <= node < self.R_node_base
    def is_R_node(self, node): return self.R_node_base <= node < self.Q_node_base
    def is_Q_node(self, node): return self.Q_node_base <= node < self.spqr_order
    def node_nv(self, node): return len(self.spqr_node_vtx2gph_vtx[node])
    def is_virtual_edge(self, node, uedge):
        return self.spqr_node_uedge2spqr_uedge_type[node][uedge] != spqr_tree_real_pure


    
def _spqr_remove_adjacency_edges(v, edges):
    edges_with_v = []
    edges_without_v = []
    for e in edges:
        if v in e:
            edges_with_v.append(e)
        else:
            edges_without_v.append(e)

    return edges_without_v, edges_with_v
'''
def _calc_vertices_of_edges_of_nodes(n, edges_of_nodes):
    nodes = edges_of_nodes
    node_vertices = tuple((i, u) for i, node in enumerate(nodes) for e in node for u in e)
    node_vertices = bucket_sorts(node_vertices, lambda i, e: e[i], [1,0], [n, len(nodes)])
    node_vertices = group_unify(node_vertices)
    vertices_of_nodes = group_to_list(len(nodes), node_vertices, lambda e:e[0], lambda e:e[1])
    return vertices_of_nodes
'''
_calc_vertices_of_edges_of_nodes = edges_list2vtc_list
def _SPQR_tree(begin, original_vertices, biconnect_edges):
    this_function = _SPQR_tree
    n = len(original_vertices)
    assert n > 1

    for v in range(begin, n):
        edges_without_v, edges_with_v = _spqr_remove_adjacency_edges(v, biconnect_edges)
        g = graph(n, edges_without_v)
        '''
        num_connected_component, _, N, \
           vertex2node, edge2node, bc_nodes, bc_edges, \
           cut_node_base, block_node_base\
           = BC_tree(g)'''
        num_connected_component, gph_order, bc_order, \
            gph_vtx2bc_nodes, gph_vtx2bc_node_vtc, \
            gph_uedge2bc_node, gph_uedge2bc_node_uedge, \
            bc_tree, bc_node2gph_vtc, bc_node2gph_uedges, bc_node2subgraph, \
            cut_node_base, block_node_base \
            = BC_tree(g)
        N = bc_order
        edge2node = gph_uedge2bc_node
        assert num_connected_component == 2
        assert cut_node_base == 1 or (n == 2 and cut_node_base == 2)
        if cut_node_base < block_node_base:
            break
        else:
            assert bc_tree.nv() == 2
    else:
        return [(original_vertices, tuple(biconnect_edges)),]
    begin = v
    #G = bc_tree
    #bug!!!!!!!!!!!!!!!
    #for cut_node in bc_nodes[cut_node_base : block_node_base]:
    #    assert G.degree(cut_node) == 2

    flag = [False]*n
    for s, u in edges_with_v:
        if u == begin: u = s
        flag[u] = True
    for cut_vtx, in bc_node2gph_vtc[cut_node_base : block_node_base]:
        assert cut_vtx > begin
        flag[cut_vtx] = True

    to_ls = tuple(u for u, b in enumerate(flag) if b)
    edges = g.edges()
    edges_of_nodes = tuple(list(edges[uedge] for uedge in uedges)\
                           for uedges in bc_node2gph_uedges[block_node_base:])
    for u in to_ls:
        node = gph_vtx2bc_nodes[u][0]
        if node < block_node_base:
            c_node = node
            cut_vertex = u
            for b_node in bc_tree.neighbors(c_node):
                edges_of_nodes[b_node - block_node_base].append((begin, cut_vertex))
        else:
            b_node = node
            edges_of_nodes[b_node - block_node_base].append((begin, u))

    vertices_of_nodes = edges_list2vtc_list(n, edges_of_nodes)
    
    reorder = [None]*n
    new_edges_of_nodes = []
    begs = []
    for edges, vertices in zip(edges_of_nodes, vertices_of_nodes):
        for new_v, old_v in enumerate(vertices):
            reorder[old_v] = new_v
        es = tuple((reorder[u], reorder[v]) for u, v in edges)
        new_edges_of_nodes.append(es)
        begs.append(reorder[begin]+1)
    org_vtc_of_nodes = tuple(tuple(original_vertices[u] for u in vertices) \
                             for vertices in vertices_of_nodes)
    
    components = []
    for beg, new_edges, org_vtc in zip(begs, new_edges_of_nodes, org_vtc_of_nodes):
        sub_components = this_function(beg, org_vtc, new_edges)
        components += sub_components

    return components















def _test_spqr_tree_data():
    from simple_undirected_graph import graph, linear_graph, cycle_graph, K_n
    
    ad_ls = [\
        (1, 2, 7),\
        (0, 2),\
        (0, 1, 3, 4),\
        (2, 4),\
        (2, 3, 5, 7),\
        
        (4, 6),\
        (5, 7),\
        (0, 4, 6),\
        ]
    g1 = graph(ad_ls)
    ad_ls = [\
        (1, 6, 12),\
        (0, 2),\
        (1, 3),\
        (2, 4, 5),\
        (3, 6),\
        
        (3, 6),\
        (0, 4, 5, 7, 9),\
        (6, 8),\
        (7, 9),\
        (6, 8, 10, 11),\
        
        (9, 11, 12),\
        (9, 10, 12),\
        (0, 10, 11),\
        ]
    g2 = graph(ad_ls)

    ad_ls = [\
        (1, 2, 3), \
        (0, 4, 7), \
        (0, 11, 12), \
        (0, 14, 15), \
        (1, 5, 8), \
        
        (4, 16, 6), \
        (5, 7, 8), \
        (1, 8, 6), \
        (4, 6, 7), \
        (10, 16, 13), \
        
        (11, 9, 12), \
        (2, 10), \
        (2, 10), \
        (9, 15, 14), \
        (3, 13, 15), \
        
        (3, 14, 13), \
        (5, 9), \
        ]
    g3 = graph(ad_ls)

        

    gs = [g1, g2, g3, linear_graph(2), \
          cycle_graph(3), cycle_graph(4), cycle_graph(5), \
          K_n(4), K_n(5), \
          ]


    ans = [\
        (8, 7, \
            (\
                (0, 3, 4), \
                (3,), \
                (0, 1, 3, 4, 5), \
                (5,), \
                (1, 2, 4, 5, 6), \
                (6,), \
                (6,), \
                (2, 4, 6)), \
            (\
                ((0, 0), (3, 0), (4, 0)), \
                ((3, 1),), \
                ((0, 1), (1, 0), (3, 2), (4, 1), (5, 0)), \
                ((5, 1),), \
                ((1, 1), (2, 0), (4, 2), (5, 2), (6, 0)), \
                ((6, 1),), \
                ((6, 2),), \
                ((2, 1), (4, 3), (6, 3))), \
            (\
                (3,), (0, 3, 4), (4,), \
                (3,), \
                (5,), (1, 4, 5), \
                (5,), \
                (6,), (2, 4, 6), \
                (6,), \
                (6,)), \
            (\
                ((3, 0),), ((0, 0), (3, 1), (4, 0)), ((4, 1),), \
                ((3, 2),), \
                ((5, 0),), ((1, 0), (4, 2), (5, 1)), \
                ((5, 2),), \
                ((6, 0),), ((2, 0), (4, 3), (6, 1)), \
                ((6, 2),), \
                ((6, 3),)), \
            (\
                spqr_tree_real_pure, spqr_tree_both_real_virtual, spqr_tree_real_pure, \
                spqr_tree_real_pure, \
                spqr_tree_real_pure, spqr_tree_both_real_virtual, \
                spqr_tree_real_pure, \
                spqr_tree_real_pure, spqr_tree_both_real_virtual, \
                spqr_tree_real_pure, \
                spqr_tree_real_pure), \
            \
            graph(((3, 4), (4, 5), (4, 6), (0,), (0, 1, 2), (1,), (2,))), \
            (\
                graph(((1,), (0,))), graph(((1,), (0,))), graph(((1,), (0,))), \
                graph(((1, 2), (0, 2), (0, 1))), \
                graph(((1, 3), (0, 2), (1, 3), (0, 2))), \
                graph(((1, 2), (0, 2), (0, 1))), \
                graph(((1, 3), (0, 2), (1, 3), (0, 2)))), 
            (\
                (((3, 1), (4, 0), (spqr_tree_gph_node, 1)),), \
                (((4, 2), (5, 1), (spqr_tree_gph_node, 5)),), \
                (((4, 3), (6, 1), (spqr_tree_gph_node, 8)),), \
                (((spqr_tree_gph_node, 0),), ((0, 0), (spqr_tree_gph_node, 1)), ((spqr_tree_gph_node, 3),)), \
                (((0, 0), (spqr_tree_gph_node, 1)), ((spqr_tree_gph_node, 2),), ((1, 0), (spqr_tree_gph_node, 5)), ((2, 0), (spqr_tree_gph_node, 8))), \
                (((spqr_tree_gph_node, 4),), ((1, 0), (spqr_tree_gph_node, 5)), ((spqr_tree_gph_node, 6),)), \
                (((spqr_tree_gph_node, 7),), ((2, 0), (spqr_tree_gph_node, 8)), ((spqr_tree_gph_node, 9),), ((spqr_tree_gph_node, 10),))), \
            (\
                (((3, 1), (4, 0)),), \
                (((4, 2), (5, 1)),), \
                (((4, 3), (6, 1)),), \
                ((), ((0, 0),), ()), \
                (((0, 0),), (), ((1, 0),), ((2, 0),)), \
                ((), ((1, 0),), ()), \
                ((), ((2, 0),), (), ())), \
            ((), (), (), (0, 3), (2,), (4, 6), (7, 9, 10)), \
            ((1,), (5,), (8,), (0, 1, 3), (1, 2, 5, 8), (4, 5, 6), (7, 8, 9, 10)), \
            \
            ((0, 2), (2, 4), (4, 7), (0, 1, 2), (0, 2, 4, 7), (2, 3, 4), (4, 5, 6, 7)), \
            ((1,), (5,), (8,), (0, 1, 3), (1, 2, 5, 8), (4, 5, 6), (7, 8, 9, 10)), \
            (\
                (spqr_tree_both_real_virtual,), (spqr_tree_both_real_virtual,), (spqr_tree_both_real_virtual,), \
                (spqr_tree_real_pure, spqr_tree_both_real_virtual, spqr_tree_real_pure), \
                (spqr_tree_both_real_virtual, spqr_tree_real_pure, spqr_tree_both_real_virtual, spqr_tree_both_real_virtual), \
                (spqr_tree_real_pure, spqr_tree_both_real_virtual, spqr_tree_real_pure), \
                (spqr_tree_real_pure, spqr_tree_both_real_virtual, spqr_tree_real_pure, spqr_tree_real_pure)), \
        3, 3, 7, 7, 3, 0, 3, 4, 0, 0), \
        (13, 10, ((0, 4, 5), (4,), (4,), (2, 4, 6, 7), (6,), (7,), (0, 1, 2, 4, 5, 6, 7, 8), (8,), (8,), (1, 3, 5, 8, 9), (9,), (9,), (3, 5, 9)), (((0, 0), (4, 0), (5, 0)), ((4, 1),), ((4, 2),), ((2, 0), (4, 3), (6, 0), (7, 0)), ((6, 1),), ((7, 1),), ((0, 1), (1, 0), (2, 1), (4, 4), (5, 1), (6, 2), (7, 2), (8, 0)), ((8, 1),), ((8, 2),), ((1, 1), (3, 0), (5, 2), (8, 3), (9, 0)), ((9, 1),), ((9, 2),), ((3, 1), (5, 3), (9, 3))), ((4,), (0, 4, 5), (5,), (4,), (4,), (6,), (7,), (6,), (7,), (8,), (1, 5, 8), (8,), (8,), (9,), (9,), (9,), (9,), (9,)), (((4, 0),), ((0, 0), (4, 1), (5, 0)), ((5, 1),), ((4, 2),), ((4, 3),), ((6, 0),), ((7, 0),), ((6, 2),), ((7, 2),), ((8, 0),), ((1, 0), (5, 2), (8, 1)), ((8, 2),), ((8, 3),), ((9, 0),), ((9, 1),), ((9, 3),), ((9, 4),), ((9, 5),)), (spqr_tree_real_pure, spqr_tree_both_real_virtual, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_both_real_virtual, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure), graph(((4, 5), (5, 8), (4, 6, 7), (5, 9), (0, 2), (0, 1, 3), (2,), (2,), (1,), (3,))), (graph(((1,), (0,))), graph(((1,), (0,))), graph(((1,), (0,))), graph(((1,), (0,))), graph(((1, 4), (0, 2), (1, 3), (2, 4), (0, 3))), graph(((1, 3), (0, 2), (1, 3), (0, 2))), graph(((1, 2), (0, 2), (0, 1))), graph(((1, 2), (0, 2), (0, 1))), graph(((1, 3), (0, 2), (1, 3), (0, 2))), graph(((1, 2, 3), (0, 2, 3), (0, 1, 3), (0, 1, 2)))), ((((4, 1), (5, 0), (spqr_tree_gph_node, 1)),), (((5, 2), (8, 1), (spqr_tree_gph_node, 10)),), (((4, 4), (6, 1), (7, 1)),), (((5, 3), (9, 2)),), (((spqr_tree_gph_node, 0),), ((0, 0), (spqr_tree_gph_node, 1)), ((spqr_tree_gph_node, 3),), ((spqr_tree_gph_node, 4),), ((2, 0),)), (((0, 0), (spqr_tree_gph_node, 1)), ((spqr_tree_gph_node, 2),), ((1, 0), (spqr_tree_gph_node, 10)), ((3, 0),)), (((spqr_tree_gph_node, 5),), ((2, 0),), ((spqr_tree_gph_node, 7),)), (((spqr_tree_gph_node, 6),), ((2, 0),), ((spqr_tree_gph_node, 8),)), (((spqr_tree_gph_node, 9),), ((1, 0), (spqr_tree_gph_node, 10)), ((spqr_tree_gph_node, 11),), ((spqr_tree_gph_node, 12),)), (((spqr_tree_gph_node, 13),), ((spqr_tree_gph_node, 14),), ((3, 0),), ((spqr_tree_gph_node, 15),), ((spqr_tree_gph_node, 16),), ((spqr_tree_gph_node, 17),))), ((((4, 1), (5, 0)),), (((5, 2), (8, 1)),), (((4, 4), (6, 1), (7, 1)),), (((5, 3), (9, 2)),), ((), ((0, 0),), (), (), ((2, 0),)), (((0, 0),), (), ((1, 0),), ((3, 0),)), ((), ((2, 0),), ()), ((), ((2, 0),), ()), ((), ((1, 0),), (), ()), ((), (), ((3, 0),), (), (), ())), ((), (), (), (), (0, 3, 4), (2,), (5, 7), (6, 8), (9, 11, 12), (13, 14, 15, 16, 17)), ((1,), (10,), (), (), (0, 1, 3, 4), (1, 2, 10), (5, 7), (6, 8), (9, 10, 11, 12), (13, 14, 15, 16, 17)), ((0, 6), (6, 9), (3, 6), (9, 12), (0, 1, 2, 3, 6), (0, 6, 9, 12), (3, 4, 6), (3, 5, 6), (6, 7, 8, 9), (9, 10, 11, 12)), ((1,), (10,), (spqr_tree_no_co_gph_uedge,), (spqr_tree_no_co_gph_uedge,), (0, 1, 3, 4, spqr_tree_no_co_gph_uedge), (1, 2, 10, spqr_tree_no_co_gph_uedge), (5, spqr_tree_no_co_gph_uedge, 7), (6, spqr_tree_no_co_gph_uedge, 8), (9, 10, 11, 12), (13, 14, spqr_tree_no_co_gph_uedge, 15, 16, 17)), ((spqr_tree_both_real_virtual,), (spqr_tree_both_real_virtual,), (spqr_tree_virtual_pure,), (spqr_tree_virtual_pure,), (spqr_tree_real_pure, spqr_tree_both_real_virtual, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_virtual_pure), (spqr_tree_both_real_virtual, spqr_tree_real_pure, spqr_tree_both_real_virtual, spqr_tree_virtual_pure), (spqr_tree_real_pure, spqr_tree_virtual_pure, spqr_tree_real_pure), (spqr_tree_real_pure, spqr_tree_virtual_pure, spqr_tree_real_pure), (spqr_tree_real_pure, spqr_tree_both_real_virtual, spqr_tree_real_pure, spqr_tree_real_pure), (spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_virtual_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure)), 2, 4, 9, 10, 2, 2, 4, 5, 1, 0),\
        (17, 11, ((0, 4, 5, 6), (1, 4, 9), (2, 5, 7, 8), (3, 6, 10), (9,), (1, 4, 9), (9,), (9,), (9,), (0, 4, 5, 6), (2, 5, 7, 8), (7,), (8,), (3, 6, 10), (10,), (10,), (4,)), (((0, 0), (4, 0), (5, 0), (6, 0)), ((1, 0), (4, 1), (9, 0)), ((2, 0), (5, 1), (7, 0), (8, 0)), ((3, 0), (6, 1), (10, 0)), ((9, 1),), ((1, 1), (4, 2), (9, 2)), ((9, 3),), ((9, 4),), ((9, 5),), ((0, 1), (4, 3), (5, 2), (6, 2)), ((2, 1), (5, 3), (7, 1), (8, 1)), ((7, 2),), ((8, 2),), ((3, 1), (6, 3), (10, 1)), ((10, 2),), ((10, 3),), ((4, 4),)), ((4,), (5,), (6,), (9,), (9,), (7,), (8,), (10,), (10,), (9,), (9,), (9,), (4,), (9,), (9,), (9,), (5,), (6,), (4,), (7,), (8,), (10,), (10,), (10,)), (((4, 0),), ((5, 0),), ((6, 0),), ((9, 0),), ((9, 2),), ((7, 1),), ((8, 1),), ((10, 1),), ((10, 2),), ((9, 3),), ((9, 4),), ((9, 5),), ((4, 3),), ((9, 6),), ((9, 7),), ((9, 8),), ((5, 3),), ((6, 3),), ((4, 4),), ((7, 2),), ((8, 2),), ((10, 3),), ((10, 4),), ((10, 5),)), (spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure), graph(((4, 5, 6), (4, 9), (5, 7, 8), (6, 10), (0, 1), (0, 2), (0, 3), (2,), (2,), (1,), (3,))), (graph(((1,), (0,))), graph(((1,), (0,))), graph(((1,), (0,))), graph(((1,), (0,))), graph(((1, 3), (0, 2), (1, 4), (0, 4), (2, 3))), graph(((1, 2), (0, 3), (0, 3), (1, 2))), graph(((1, 2), (0, 3), (0, 3), (1, 2))), graph(((1, 2), (0, 2), (0, 1))), graph(((1, 2), (0, 2), (0, 1))), graph(((1, 2, 4), (0, 2, 5), (0, 1, 3), (2, 4, 5), (0, 3, 5), (1, 3, 4))), graph(((1, 2, 3), (0, 2, 3), (0, 1, 3), (0, 1, 2)))), ((((4, 1), (5, 1), (6, 1)),), (((4, 2), (9, 1)),), (((5, 2), (7, 0), (8, 0)),), (((6, 2), (10, 0)),), (((spqr_tree_gph_node, 0),), ((0, 0),), ((1, 0),), ((spqr_tree_gph_node, 12),), ((spqr_tree_gph_node, 18),)), (((spqr_tree_gph_node, 1),), ((0, 0),), ((2, 0),), ((spqr_tree_gph_node, 16),)), (((spqr_tree_gph_node, 2),), ((0, 0),), ((3, 0),), ((spqr_tree_gph_node, 17),)), (((2, 0),), ((spqr_tree_gph_node, 5),), ((spqr_tree_gph_node, 19),)), (((2, 0),), ((spqr_tree_gph_node, 6),), ((spqr_tree_gph_node, 20),)), (((spqr_tree_gph_node, 3),), ((1, 0),), ((spqr_tree_gph_node, 4),), ((spqr_tree_gph_node, 9),), ((spqr_tree_gph_node, 10),), ((spqr_tree_gph_node, 11),), ((spqr_tree_gph_node, 13),), ((spqr_tree_gph_node, 14),), ((spqr_tree_gph_node, 15),)), (((3, 0),), ((spqr_tree_gph_node, 7),), ((spqr_tree_gph_node, 8),), ((spqr_tree_gph_node, 21),), ((spqr_tree_gph_node, 22),), ((spqr_tree_gph_node, 23),))), ((((4, 1), (5, 1), (6, 1)),), (((4, 2), (9, 1)),), (((5, 2), (7, 0), (8, 0)),), (((6, 2), (10, 0)),), ((), ((0, 0),), ((1, 0),), (), ()), ((), ((0, 0),), ((2, 0),), ()), ((), ((0, 0),), ((3, 0),), ()), (((2, 0),), (), ()), (((2, 0),), (), ()), ((), ((1, 0),), (), (), (), (), (), (), ()), (((3, 0),), (), (), (), (), ())), ((), (), (), (), (0, 12, 18), (1, 16), (2, 17), (5, 19), (6, 20), (3, 4, 9, 10, 11, 13, 14, 15), (7, 8, 21, 22, 23)), ((), (), (), (), (0, 12, 18), (1, 16), (2, 17), (5, 19), (6, 20), (3, 4, 9, 10, 11, 13, 14, 15), (7, 8, 21, 22, 23)), ((0, 9), (1, 5), (2, 10), (3, 13), (0, 1, 5, 9, 16), (0, 2, 9, 10), (0, 3, 9, 13), (2, 10, 11), (2, 10, 12), (1, 4, 5, 6, 7, 8), (3, 13, 14, 15)), ((spqr_tree_no_co_gph_uedge,), (spqr_tree_no_co_gph_uedge,), (spqr_tree_no_co_gph_uedge,), (spqr_tree_no_co_gph_uedge,), (0, spqr_tree_no_co_gph_uedge, spqr_tree_no_co_gph_uedge, 12, 18), (1, spqr_tree_no_co_gph_uedge, spqr_tree_no_co_gph_uedge, 16), (2, spqr_tree_no_co_gph_uedge, spqr_tree_no_co_gph_uedge, 17), (spqr_tree_no_co_gph_uedge, 5, 19), (spqr_tree_no_co_gph_uedge, 6, 20), (3, spqr_tree_no_co_gph_uedge, 4, 9, 10, 11, 13, 14, 15), (spqr_tree_no_co_gph_uedge, 7, 8, 21, 22, 23)), ((spqr_tree_virtual_pure,), (spqr_tree_virtual_pure,), (spqr_tree_virtual_pure,), (spqr_tree_virtual_pure,), (spqr_tree_real_pure, spqr_tree_virtual_pure, spqr_tree_virtual_pure, spqr_tree_real_pure, spqr_tree_real_pure), (spqr_tree_real_pure, spqr_tree_virtual_pure, spqr_tree_virtual_pure, spqr_tree_real_pure), (spqr_tree_real_pure, spqr_tree_virtual_pure, spqr_tree_virtual_pure, spqr_tree_real_pure), (spqr_tree_virtual_pure, spqr_tree_real_pure, spqr_tree_real_pure), (spqr_tree_virtual_pure, spqr_tree_real_pure, spqr_tree_real_pure), (spqr_tree_real_pure, spqr_tree_virtual_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure), (spqr_tree_virtual_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure)), 0, 4, 9, 11, 0, 4, 4, 5, 2, 0),\
        (2, 1, ((0,), (0,)), (((0, 0),), ((0, 1),)), ((0,),), (((0, 0),),), (spqr_tree_real_pure,), graph(((),)), (graph(((1,), (0,))),), ((((spqr_tree_gph_node, 0),),),), (((),),), ((0,),), ((0,),), ((0, 1),), ((0,),), ((spqr_tree_real_pure,),), 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),\
        (3, 1, ((0,), (0,), (0,)), (((0, 0),), ((0, 1),), ((0, 2),)), ((0,), (0,), (0,)), (((0, 0),), ((0, 1),), ((0, 2),)), (spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure), graph(((),)), (graph(((1, 2), (0, 2), (0, 1))),), ((((spqr_tree_gph_node, 0),), ((spqr_tree_gph_node, 1),), ((spqr_tree_gph_node, 2),)),), (((), (), ()),), ((0, 1, 2),), ((0, 1, 2),), ((0, 1, 2),), ((0, 1, 2),), ((spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure),), 0, 0, 1, 1, 0, 0, 0, 1, 0, 0),\
        (4, 1, ((0,), (0,), (0,), (0,)), (((0, 0),), ((0, 1),), ((0, 2),), ((0, 3),)), ((0,), (0,), (0,), (0,)), (((0, 0),), ((0, 1),), ((0, 2),), ((0, 3),)), (spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure), graph(((),)), (graph(((1, 3), (0, 2), (1, 3), (0, 2))),), ((((spqr_tree_gph_node, 0),), ((spqr_tree_gph_node, 1),), ((spqr_tree_gph_node, 2),), ((spqr_tree_gph_node, 3),)),), (((), (), (), ()),), ((0, 1, 2, 3),), ((0, 1, 2, 3),), ((0, 1, 2, 3),), ((0, 1, 2, 3),), ((spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure),), 0, 0, 1, 1, 0, 0, 0, 1, 0, 0),\
        (5, 1, ((0,), (0,), (0,), (0,), (0,)), (((0, 0),), ((0, 1),), ((0, 2),), ((0, 3),), ((0, 4),)), ((0,), (0,), (0,), (0,), (0,)), (((0, 0),), ((0, 1),), ((0, 2),), ((0, 3),), ((0, 4),)), (spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure), graph(((),)), (graph(((1, 4), (0, 2), (1, 3), (2, 4), (0, 3))),), ((((spqr_tree_gph_node, 0),), ((spqr_tree_gph_node, 1),), ((spqr_tree_gph_node, 2),), ((spqr_tree_gph_node, 3),), ((spqr_tree_gph_node, 4),)),), (((), (), (), (), ()),), ((0, 1, 2, 3, 4),), ((0, 1, 2, 3, 4),), ((0, 1, 2, 3, 4),), ((0, 1, 2, 3, 4),), ((spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure),), 0, 0, 1, 1, 0, 0, 0, 1, 0, 0),\
        (4, 1, ((0,), (0,), (0,), (0,)), (((0, 0),), ((0, 1),), ((0, 2),), ((0, 3),)), ((0,), (0,), (0,), (0,), (0,), (0,)), (((0, 0),), ((0, 1),), ((0, 2),), ((0, 3),), ((0, 4),), ((0, 5),)), (spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure), graph(((),)), (graph(((1, 2, 3), (0, 2, 3), (0, 1, 3), (0, 1, 2))),), ((((spqr_tree_gph_node, 0),), ((spqr_tree_gph_node, 1),), ((spqr_tree_gph_node, 2),), ((spqr_tree_gph_node, 3),), ((spqr_tree_gph_node, 4),), ((spqr_tree_gph_node, 5),)),), (((), (), (), (), (), ()),), ((0, 1, 2, 3, 4, 5),), ((0, 1, 2, 3, 4, 5),), ((0, 1, 2, 3),), ((0, 1, 2, 3, 4, 5),), ((spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure),), 0, 0, 0, 1, 0, 0, 0, 0, 1, 0),\
        (5, 1, ((0,), (0,), (0,), (0,), (0,)), (((0, 0),), ((0, 1),), ((0, 2),), ((0, 3),), ((0, 4),)), ((0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,)), (((0, 0),), ((0, 1),), ((0, 2),), ((0, 3),), ((0, 4),), ((0, 5),), ((0, 6),), ((0, 7),), ((0, 8),), ((0, 9),)), (spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure), graph(((),)), (graph(((1, 2, 3, 4), (0, 2, 3, 4), (0, 1, 3, 4), (0, 1, 2, 4), (0, 1, 2, 3))),), ((((spqr_tree_gph_node, 0),), ((spqr_tree_gph_node, 1),), ((spqr_tree_gph_node, 2),), ((spqr_tree_gph_node, 3),), ((spqr_tree_gph_node, 4),), ((spqr_tree_gph_node, 5),), ((spqr_tree_gph_node, 6),), ((spqr_tree_gph_node, 7),), ((spqr_tree_gph_node, 8),), ((spqr_tree_gph_node, 9),)),), (((), (), (), (), (), (), (), (), (), ()),), ((0, 1, 2, 3, 4, 5, 6, 7, 8, 9),), ((0, 1, 2, 3, 4, 5, 6, 7, 8, 9),), ((0, 1, 2, 3, 4),), ((0, 1, 2, 3, 4, 5, 6, 7, 8, 9),), ((spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure, spqr_tree_real_pure),), 0, 0, 0, 1, 0, 0, 0, 0, 1, 0),\
     ]
    return gs, ans


def _test_spqr_tree():
    gs, ans = _test_spqr_tree_data()
    for g, a in zip(gs, ans):
        if not a == SPQR_tree(g):
            print(a)
            print(SPQR_tree(g))
        assert a == SPQR_tree(g)


def _test_bc_tree():
    from simple_undirected_graph import graph
    ad_ls = [\
        (1, 2),\
        
        (0, 2),\
        (0, 1, 3),\
        (2, 4, 5),\
        (3,),\
        (3, 6, 9, 10),\
        
        (5, 7, 8),\
        (6,),\
        (6,),\
        (5, 10),\
        (5, 9, 11, 12, 13, 14, 15),\
        
        (10, 12),\
        (10, 11),\
        (10, 14, 15),\
        (10, 13, 15),\
        (10, 13, 14),\
        
        (),\
        (18,),\
        (17,),\
        (20, 21),\
        (19, 21),\
        
        (19, 20),\
        (23,),\
        (22, 24),\
        (23,),\
        ]
    ans =\
        (5, 25, 21, \
            (\
                (7,), (7,), \
                (1, 7, 8), \
                (2, 8, 9, 10), (9,), \
                (3, 10, 11, 12), \
                (4, 11, 13, 14), (13,), (14,), (12,), \
                (5, 12, 15, 16), (15,), (15,), (16,), (16,), (16,), \
                (0,), (17,), (17,), (18,), (18,), (18,), (19,), \
                (6, 19, 20), (20,)), \

            (\
                ((7, 0),), ((7, 1),), \
                ((1, 0), (7, 2), (8, 0)), \
                ((2, 0), (8, 1), (9, 0), (10, 0)), ((9, 1),), \
                ((3, 0), (10, 1), (11, 0), (12, 0)), \
                ((4, 0), (11, 1), (13, 0), (14, 0)), ((13, 1),), \
                ((14, 1),), ((12, 1),), ((5, 0), (12, 2), \
                (15, 0), (16, 0)), ((15, 1),), ((15, 2),), ((16, 1),), ((16, 2),), ((16, 3),), \
                ((0, 0),), ((17, 0),), ((17, 1),), \
                ((18, 0),), ((18, 1),), ((18, 2),), \
                ((19, 0),), \
                ((6, 0), (19, 1), (20, 0)), ((20, 1),)), \
            (\
                7, 7, 7, 8, 9, 10, \
                11, 12, 12, 13, 14, 12, \
                15, 15, 16, 16, 16, 15, 16, 16, 16, \
                17, 18, 18, 18, 19, 20), \
            (\
                (7, 0), (7, 1), (7, 2), \
                (8, 0), (9, 0), (10, 0), (11, 0), \
                (12, 0), (12, 1), (13, 0), (14, 0), (12, 2), \
                (15, 0), (15, 1), (16, 0), (16, 1), (16, 2), (15, 2), \
                (16, 3), (16, 4), (16, 5), \
                (17, 0), (18, 0), (18, 1), (18, 2), \
                (19, 0), (20, 0)), 
            graph((\
                (), (7, 8), (8, 9, 10), (10, 11, 12), \
                (11, 13, 14), (12, 15, 16), (19, 20), \
                (1,), (1, 2), (2,), (2, 3), (3, 4), (3, 5), (4,), (4,), (5,), (5,), \
                (), (), (6,), (6,))), \
            (\
                (16,), (2,), (3,), (5,), (6,), (10,), (23,), \
                (0, 1, 2), (2, 3), (3, 4), (3, 5), (5, 6), (5, 9, 10), \
                (6, 7), (6, 8), (10, 11, 12), (10, 13, 14, 15), \
                (17, 18), (19, 20, 21), (22, 23), (23, 24)), \
            (\
                (), (), (), (), (), (), (), \
                (0, 1, 2), (3,), (4,), (5,), (6,), (7, 8, 11), \
                (9,), (10,), (12, 13, 17), (14, 15, 16, 18, 19, 20), \
                (21,), (22, 23, 24), (25,), (26,)), \
            (\
                graph(((),)), graph(((),)), graph(((),)), graph(((),)), \
                graph(((),)), graph(((),)), graph(((),)), \
                graph(((1, 2), (0, 2), (0, 1))), \
                graph(((1,), (0,))), graph(((1,), (0,))), \
                graph(((1,), (0,))), graph(((1,), (0,))), \
                graph(((1, 2), (0, 2), (0, 1))), \
                graph(((1,), (0,))), graph(((1,), (0,))), \
                graph(((1, 2), (0, 2), (0, 1))), \
                graph(((1, 2, 3), (0, 2, 3), (0, 1, 3), (0, 1, 2))), \
                graph(((1,), (0,))), \
                graph(((1, 2), (0, 2), (0, 1))), \
                graph(((1,), (0,))), graph(((1,), (0,)))), \
        1, 7)
    
    G = graph(ad_ls)
    bc = BC_tree(G)
    if ans != bc:
        print(ans)
        print(G)
        print(bc)
    assert ans == bc






if __name__ == "__main__":
    _test_bc_tree()
    _test_spqr_tree()
    
