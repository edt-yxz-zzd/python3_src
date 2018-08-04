
'''

isDAG/find_a_circle
to_super_tree/to_super_DAG

reversed_topological_ordering
'''
from .bucket_sort import bucket_sort, is_sorted, group_unify
from .dgraph_DFS import dgraph_DFS, EXIT, HEXIT, BACK, LOOP
from .directed_graph import strong_connected_components, \
     reverse_u2vtc, u2vtc2dedges, dedges2u2vtc

class NotDAGError(ValueError):pass





def reversed_topological_ordering(u2vtc):
    r = _reversed_topological_ordering(u2vtc)
    if r == None:
        raise NotDAGError('not a DAG @reversed_topological_ordering')
    return r

def _reversed_topological_ordering(u2vtc):
    ls = []
    for case, path, node in dgraph_DFS(u2vtc):
        if case == EXIT or case == HEXIT:
            ls.append(node)
        elif case == BACK or case == LOOP:
            return None

    return ls






def isDAG(u2vtc):
    return None != _reversed_topological_ordering(u2vtc)

def find_a_circle(u2vtc):
    for case, path, node in dgraph_DFS(u2vtc):
        if case == BACK or case == LOOP:
            r = tuple(path[:-1])
            assert r
            return r
    return None

def _to_super_v(u2vtc):
    vtc_ls, edges_ls, discarded_edges = strong_connected_components(u2vtc)
    assert is_sorted(vtc_ls)
    assert all(is_sorted(vtc) for vtc in vtc_ls)

    N = len(u2vtc)
    super_N = len(vtc_ls)

    v2super_v = [None] * N
    for i, vtc in enumerate(vtc_ls):
        for v in vtc:
            assert v2super_v[v] == None
            v2super_v[v] = i

    assert not any((super_v == None) for super_v in v2super_v)
    super_v2vtc = vtc_ls
    return v2super_v, super_v2vtc, edges_ls

def dedges2super_dedges(dedges, v2super_v, super_N):
    super_dedges = ((v2super_v[u], v2super_v[v]) for u, v in dedges)
    super_dedges = tuple((u,v) for u, v in super_dedges if u != v)
    
    super_dedges = bucket_sort(super_dedges, key=lambda e:e[1], N=super_N)
    super_dedges = bucket_sort(super_dedges, key=lambda e:e[0], N=super_N)
    super_dedges = group_unify(super_dedges)
    return super_dedges

##def to_super_tree(u2vtc):
##    v2super_v, super_v2vtc, edges_ls = _to_super_v(u2vtc)
##    super_N = len(super_v2vtc)
##    super_dedges = dedges2super_dedges(u2vtc2dedges(u2vtc), v2super_v, super_N)
##    super_tree = dedges2u2vtc(super_N, super_dedges)
##    return v2super_v, super_v2vtc, super_tree

def to_super_DAG(u2vtc):
    v2super_v, super_v2vtc, edges_ls = _to_super_v(u2vtc)
    super_N = len(super_v2vtc)
    super_dedges = dedges2super_dedges(u2vtc2dedges(u2vtc), v2super_v, super_N)
    super_DAG = dedges2u2vtc(super_N, super_dedges)
    return v2super_v, super_v2vtc, super_DAG



def u2vtc_to_heights(u2vtc):
    '''see DAG_to_heights; using strong_connected_components as super DAG
'''
    v2super_v, super_v2vtc, super_DAG = to_super_DAG(u2vtc)
    super_u2height = DAG_to_heights(super_DAG)

    u2height = [super_u2height[v2super_v[v]] for v in range(len(u2vtc))]
    return u2height
    
def DAG_to_heights(dag_u2vtc):
    '''height[u] = max(map(height, u2vtc[u]))+1 if u2vtc[u] else 0
'''
    u2vtc = dag_u2vtc

    u2height = [None]*len(u2vtc)
    u2num_no_height_vtc = list(map(len, u2vtc))
    r_u2vtc = reverse_u2vtc(u2vtc)
    to_process = [v for v, num in enumerate(u2num_no_height_vtc) if num == 0]
    while to_process:
        v = to_process.pop()
        assert u2num_no_height_vtc[v] == 0
        assert u2height[v] is None
        
        ls = [-1]
        ls.extend(u2height[u] for u in u2vtc[v])
        u2height[v] = max(ls) + 1

        for u in r_u2vtc[v]:
            u2num_no_height_vtc[u] -= 1
            assert u2num_no_height_vtc[u] >= 0

            if u2num_no_height_vtc[u] == 0:
                to_process.append(u)
    if any(h is None for h in u2height):
        circle = find_a_circle(u2vtc)
        if not circle:
            raise logic-error
        raise NotDAGError(circle)

    return u2height


        
    





