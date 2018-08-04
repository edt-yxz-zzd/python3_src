
__all__ = '''
    
    dedges2unoriented_dgraph
    dedges2oriented_dgraph
    dgraph2dedges
    dgraph2reversed_unoriented_dgraph
    
    find_mini_depth
    dfs_ordering

'''.split()

from collections import defaultdict
from sand.types.ToProcess import FILOOnce, FIFOOnce
from sand import nub
from .Set_Dict_Pair import swap_pairs

def dedges2unoriented_dgraph(dedges, maybe_missing_vtcs):
    ':: Iter (Vtx, Vtx) -> Iter Vtx -> Map Vtx (Set Vtx) ; differ from "group_pairs2dict"'
    d = defaultdict(set)
    for u, v in dedges:
        d[u].add(v)
        d[v] # not to missing v
    for v in maybe_missing_vtcs:
        d[v] # not to missing v
    return {v : frozenset(ns) for v, ns in d.items()}
def dedges2oriented_dgraph(dedges, maybe_missing_vtcs):
    ':: Iter (Vtx, Vtx) -> Iter Vtx -> Map Vtx [Vtx] ; differ from "group_pairs2dict_seq_nub"'
    d = defaultdict(list)
    for u, v in nub(dedges):
        d[u].append(v)
        d[v] # not to missing v
    for v in maybe_missing_vtcs:
        d[v] # not to missing v
    assert all(len(vs) == len(set(vs)) for vs in d.values())
    return {v : tuple(ns) for v, ns in d.items()}


def dgraph2dedges(g):
    ':: Map Vtx (Iter Vtx) -> Iter (Vtx, Vtx)'
    return ((v, u) for v, ns in g.items() for u in ns)

def dgraph2reversed_unoriented_dgraph(g):
    ':: Map Vtx (Iter Vtx) -> Map Vtx (Set Vtx)'
    return dedges2unoriented_dgraph(swap_pairs(dgraph2dedges(g)), g.keys())


def find_mini_depth(dgraph, roots):
    'mini depth to any root; bfs'
    vtx2neighbors = dgraph

    vtx2min = dict.fromkeys(roots, 0)
    to_process = FIFOOnce(vtx2min.keys())

    
    def to_children(vtx):
        ns = vtx2neighbors[vtx]
        depth = vtx2min[vtx] + 1
        for u in ns:
            if u not in vtx2min:
                vtx2min[u] = depth
        return ns

    to_process.apply(to_children)
    return vtx2min
    
    
def dfs_ordering(dgraph, roots):
    vtx2neighbors = dgraph
    
    to_process = FILOOnce(roots)
    ordered_vtcs = []
    def to_children(vtx):
        ordered_vtcs.append(vtx)
        return vtx2neighbors[vtx]
    
    to_process.apply(to_children)
    return ordered_vtcs


    
