
'''
multi_directed_or_undirected_with_loops_graph
for case, es, v in DFS
case in {enter_root, new_edge ...}
'''

'''
multi_undirected_with_loops_graph
baisc output
c1:
    component = ([v...], [e...])
c2:
    component = ('B'/'L'/'O', [e...]) # loops not seperated
    # ('L', edges_of_same_bridge) or ('X', cut_vtx) or \
    # ('O', loops_of_same_vtx) or ('B', [e...])
    # 
c3:
    componet = ('S'/'P'/'Q'/'R', virtual_edges)
    virtual_edge2vtx_pair = [(u,v)...]
    assert old_edge2virtual_edge == range(ne)
    # a virtual edge is contained by excatly 2 components
    # form a super-tree
    assert num_virtual_edges == len(components) - 1
    assert sum(map(len, components)) == ne + 2*num_virtual_edges
    # one real edge in one Q
    # multi-edges in same Q
    # Q contains at least one real edge
    # Q contains 0/1 virtual edge
    # if Q contain no vitual edge, then it is the only component
    # one virtual edge in 2 different components
    # virtual_edge > real_edge == old_edge

extended output
c1:
    vtx2component
    edge2componet
c2:
    # merge L
    # super-tree
    # add super vtcs, each B/L/X/O one super vtx
    # one real vtx in one O
    # loops in same O
    # O contains one real vtx, O's super vtx number eq this real vtx
    # O incidents 0/1 super edge
    # if O incidents no super edge, then it is the only component
    # one virtual vtx in 2 different components
    # virtual_vtx > real_vtx == old_vtx
    # possible connected (via one virtual-vtx) components are:
    # B/L/O-X
    # X contains at least 2 vtcs.
c3:
    # merge S
    # merge P
    # possible connected (via one virtual-edge) components are:
    # R/S/Q-P
    # P contains at least 2 edges
    
    
    
'''

from .SPQR import basic_SPQR
from .bucket_sort import group_unify, group, bucket_sorts, split

def connect1_basic(g, DFS):
    # multi_undirected_with_loops_graph
    # DFS needn't go through all g
    component2vertics = []
    component2edges = []
    
    new_edge_cases = frozenset([enter_edge, back_edge, loop_edge, dead_edge])
    for case, es, v in DFS:
        if case == enter_root:
            component2vertics.append([v])
            component2edges.append([])
            
        elif case in new_edge_cases:
            e = es[-1]
            component2edges[-1].append(e)
            component2vertics[-1].append(v)

    return component2vertics, component2edges

def weak_connect1_basic(g, DFS):
    # multi_undirected/directed_with_loops_graph
    # undirect g, call connect1_basic
    # but DFS may only examine partial g
    # so, we can't undirect g, and use another DFS.
    
    component2vertics = []
    component2edges = []
    v2component = [None]*g.nv()
    components_to_be_merged = []
    component = -1
    
    new_edge_cases = frozenset([enter_edge, back_edge, loop_edge, dead_edge])
    for case, es, v in DFS:
        if case == enter_root:
            component += 1
            v2component[v] = component
            
            component2vertics.append([v])
            component2edges.append([])
            
        elif case in new_edge_cases:
            e = es[-1]
            component2edges[-1].append(e)
            component2vertics[-1].append(v)
            
            if case == dead_edge:
                pre_component = v2component[v]
                components_to_be_merged.append((pre_component, component))
            elif case == enter_edge:
                assert v2component[v] == None
                v2component[v] = component
                
            
        
    cg = make_mgraph_from_pairs(components_to_be_merged)
    components_to_be_merged, _super_edges = connect1_basic(cg, cg.DFS())
    for cs in components_to_be_merged:
        assert is_sorted(cs)
        cs.reverse()
        min_c = cs.pop()
        target_vs = component2vertics[min_c]
        target_es = component2edges[min_c]
        for target_ls, from_lsls in zip(
            [target_vs, target_es], [component2vertics, component2edges]):
            for c in cs:
                from_ls = from_lsls[c]
                target_ls.extend(from_ls)
                from_ls.clear()
            
        
    component2vertics = list(filter(component2vertics))
    component2edges = list(filter(component2edges))
    assert len(component2vertics) == len(component2edges)
    return component2vertics, component2edges

def connect2_basic(g, DFS):
    # connected multi_undirected_with_loops_graph
    nroot = 0
    component2edges = []
    v2lowpt = [None] * g.nv()
    lowpt2v = []
    edge_stack = []
    def new_lowpt(v):
        lowpt = len(lowpt2v)
        lowpt2v.append(v)
        v2lowpt[v] = lowpt
    for case, es, v in DFS:
        if case == enter_root:
            if nroot:
                raise ValueError('not connected graph')
            nroot += 1
            new_lowpt(v)
        elif case == enter_edge:
            new_lowpt(v)
            edge_stack.append()
        elif case == back_edge:
            descendant = g.edge2src(es[-1])
            v2lowpt[descendant] = v2lowpt[v]
        elif case == loop_edge:
            # at last
            pass
        elif case == exit_edge:
            if edge_stack and lowpt2v[v2lowpt[v]] == v:
                # lowpt not changed
                # cut vtx
                component2edges.append(edge_stack)
                edge_stack = []
            e = es[-1]
            edge_stack.append(e)
            parent = g.edge2src(e)
            v2lowpt[parent] = min(v2lowpt[parent], v2lowpt[v])
        elif case == exit_root:
            assert not edge_stack
        elif case == dead_edge:
            raise ValueError('not undirected graph')
        else:
            raise logic-error

    return component2edges

def connect3_basic(g, DFS):
    r = component2type, virtual_edge2vtx_pair, \
        component2virtual_edges, old_edge2virtual_edge = basic_SPQR(g, DFS)
    
    return r

def is_connect3(g, DFS):
    component2type, *others = connect3_basic(g, DFS)
    L = len(component2type)
    if L <= 1:
        return bool(L)
    
    d = dict.fromkeys('SPQR', 0)
    for typ in component2type:
        d[typ] += 1
    del d['Q']
    N = sum(d.values())
    assert N
    if N > 1 or d['S']:
        return False

    return True

def connect2_extend__get_loops(g, component2edges):
    loops_ls = [[] for _ in g.vertices()]
    new_component2edges = []
    for edges in component2edges:
        es = []
        for e in edges:
            if g.is_loop():
                v = g.edge2end(e)
                loops_ls[v].append(e)
            else:
                es.append(e)
        if es:
            new_component2edges.append(es)
    loops_ls = [es for es in loops_ls if es]

    assert all(loops_ls)
    assert all(new_component2edges)
    return loops_ls, new_component2edges


def connect2_extend__calc_component2vtcs(g, component2edges):
    c_v_ls = [[(c,v) for e in es for v in g.edge2ends()]
              for c,es in enumerate(component2edges)]

    # sorted as by (v,c)
    c_v_ls = bucket_sort(c_v_ls, lambda e:e[1], g.ne())
    c_v_ls = group_unify(c_v_ls)
    blocks = group(c_v_ls, lambda e:e[1])
    cs = [c for c,v in c_v_ls]
    v2components = split(cs, blocks)
    assert len(v2components) == g.nv()
    
    # sorted as by (c,v)
    c_v_ls = bucket_sort(c_v_ls, lambda e:e[0], g.ne())
    blocks = group(c_v_ls, lambda e:e[0])
    vs = [v for c,v in c_v_ls]
    component2vtcs = split(vs, blocks)
    assert len(component2vtcs) == len(component2edges)

    assert all(v2components)
    assert all(len(vs) > 1 for vs in component2vtcs)
    return v2components, component2vtcs

def connect2_extend__find_out_cut_vtcs(g, v2components):
    return [v for v, cs in enumerate(v2components) if len(cs) > 1]
def connect2_extend__find_out_bridge_components(g, component2vtcs):
    return [c for c, vs in enumerate(component2vtcs) if len(vs) == 2]

def connect2_extend__merge_bridges_to_L(g, cut_vtcs, v2components):
    raise
    def is_bridge(component):
        return len(component2vtcs[component]) == 2

    component2merge_idx = []
    for v in cut_vtcs:
        cs = v2components[v]
        if len(cs) == 2:
            if all(is_bridge(c) for c in cs):
                xxxxxxxxxxxxxxxxxxxxxxxxx
    
                
    

def connect2_extend(g, component2edges):
    loops_ls, component2edges = connect2_extend__get_loops(g, component2edges)
    v2components, component2vtcs = \
                  connect2_extend__calc_component2vtcs(g, component2edges)
    # super-tree
    # each vtx hold its vertex number in O node
    # 
    cut_vtcs = connect2_extend__find_out_cut_vtcs(g, v2components)
    bridge_components = connect2_extend__find_out_bridge_components(
        g, component2vtcs)
    raise
    





