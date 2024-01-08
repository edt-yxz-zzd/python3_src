r'''[[[
e ../../python3_src/seed/graph/DAG.py
    view ../../python3_src/seed/graph/DigraphABC.py
        view ../../python3_src/seed/graph/U2Vtc_To_DigraphABC.py


#]]]'''#'''

__all__ = '''
    is_DAG
        find_one_cycle

    iter_reversed_topological_ordering
        list_a_cycle_or_reversed_topological_ordering

    iter_local_sorted_topological_ordering
        list_a_cycle_or_local_sorted_topological_ordering

    validate_topological_ordering_
        NotTopologicalOrdering
    validate_local_sorted_topological_ordering__local_neighbor_pair_only_
        NotLocalSortedTopologicalOrdering

'''.split()


#from .dfs import *
from seed.graph.dfs import dfs, ENTER, EXIT, BACK, CROSS_OR_FORWARD
from seed.types.pair_based_leftward_list import iter_leftward_list

class NotDAG(ValueError):pass

def is_DAG(g, roots=None):
    return not _find_one_cycle(g, roots) # bug : forgot "not"



def iter_reversed_topological_ordering(g, roots=None):
    'O(N)'
    for case, path in dfs(g, roots):
        if case == EXIT:
            yield path[0]
        elif case == BACK:
            raise NotDAG(find_one_cycle(g, roots))
            raise ValueError('Not a DAG : {}'.format(find_one_cycle(g, roots)))
def list_a_cycle_or_reversed_topological_ordering(g, roots=None):
    'O(N): -> (is_DAG/bool, [vtx])/((False, cycle)|(True, reversed_topological_ordering))'
    try:
        reversed_topological_ordering = tuple(iter_reversed_topological_ordering(g, roots))
    except NotDAG as e:
        [cycle] = e.args
        assert cycle
        return (False, tuple(cycle))
    return (True, reversed_topological_ordering)


def find_one_cycle(g, roots=None):
    'return [] or [v1, v2, ...vn] where v1->v2->...->vn->v1'
    path = _find_one_cycle(g, roots)
    ls = []
    if path:
        u, path = path
        for v in iter_leftward_list(path): # bug : forgot "iter_leftward_list"
            ls.append(v)
            if v == u:
                break
        else:
            raise logic-error
        ls.reverse()
        assert ls
    return ls

def _find_one_cycle(g, roots):
    for case, path in dfs(g, roots):
        if case == BACK:
            return path

from seed.graph.DAG import iter_reversed_topological_ordering, is_DAG, find_one_cycle




#################################
#################################
#################################
from seed.tiny import echo
from seed.seq_tools.sorted_via_lt_ import sorted_via_lt_
from seed.seq_tools.inverse_uint_bijection_array import inverse_uint_bijection_array
from heapq import heapify, heappush, heappop


def mk_vtx2sorted_idx(g, /, *, key=None, __lt__=None, extra=False):
    nv = g.num_vertices()
    if key is None:
        key = echo
    j2vtx = tuple(g.iter_vertices())

    sorted_idx2j = new_j2old_j = sorted_js = sorted_via_lt_(range(nv), key=lambda j:key(j2vtx[j]), __lt__=__lt__)

    j2sorted_idx = inverse_uint_bijection_array(sorted_idx2j)
    vtx2sorted_idx = g.make_vertex_mapping()
    #for j, vtx in enumerate(j2vtx):
    #    sorted_idx = j2sorted_idx
    for vtx, sorted_idx in zip(j2vtx, j2sorted_idx):
        vtx2sorted_idx[vtx] = sorted_idx
    if not extra:
        return vtx2sorted_idx
    else:
        return (j2vtx, sorted_idx2j, j2sorted_idx, vtx2sorted_idx)
    raise NotImplementedError

def mk_dst_vtx2num_src_vtc(g, /):
    dst_vtx2num_src_vtc = g.make_vertex_mapping__default_(0)

    for src_vtx in g.iter_vertices():
        for dst_vtx in g.iter_neighbors(src_vtx):
            dst_vtx2num_src_vtc[dst_vtx] += 1
    return dst_vtx2num_src_vtc

def list_a_cycle_or_local_sorted_topological_ordering(g, /, *, key=None, __lt__=None, vtx2sorted_idx=None):
    'O(N*log(N)): -> (is_DAG/bool, [vtx])/((False, cycle)|(True, local_sorted_topological_ordering))'
    try:
        local_sorted_topological_ordering = tuple(iter_local_sorted_topological_ordering(g, key=key, __lt__=__lt__, vtx2sorted_idx=vtx2sorted_idx))
    except NotDAG as e:
        [cycle] = e.args
        assert cycle
        return (False, tuple(cycle))
    return (True, local_sorted_topological_ordering)

def iter_local_sorted_topological_ordering(g, /, *, key=None, __lt__=None, vtx2sorted_idx=None):
    'O(N*log(N)): used to sort attribute names of multi-inheritance class bases'
    if vtx2sorted_idx is None:
        vtx2sorted_idx = mk_vtx2sorted_idx(g, key=key, __lt__=__lt__)
    return iter_local_sorted_topological_ordering__vtx2sorted_idx_(vtx2sorted_idx, g)

def iter_local_sorted_topological_ordering__vtx2sorted_idx_(vtx2sorted_idx, g, /):
    'O(N*log(N)): used to sort attribute names of multi-inheritance class bases'
    #local_sorted_topological_ordering:这个概念有点小毛病:不能保障全局有序:[[u before v in local_sorted_topological_ordering] -> [(topo_ord[u], lt_ord[u]) < (topo_ord[v], lt_ord[v])]]
    #   # 『<!>』===『拓扑次序无关』
    #   比如: [topo_ord[u] <!> topo_ord[v] < topo_ord[w] <!> topo_ord[u]][lt_ord[w] < lt_ord[u] < lt_ord[v]]
    #       sort([u,v,w]) => [u, v, w]
    #       sort([u,w]) => [w, u]
    #   见下面:validate_local_sorted_topological_ordering__local_neighbor_pair_only_

    #if 0 == g.num_vertices(): return
    dst_vtx2num_src_vtc = mk_dst_vtx2num_src_vtc(g)
    srcs = [v for v, n in enumerate(dst_vtx2num_src_vtc) if n==0]


    def mk_item(v, /):
        return (vtx2sorted_idx[v], v)
    def push(v, /):
        heappush(hp, mk_item(v))
    def pop():
        _, v = heappop(hp)
        return v
    hp = [*map(mk_item, srcs)]
    heapify(hp)

    num_output_vtc = 0
    while hp:
        src_vtx = pop()
        yield src_vtx
        num_output_vtc += 1
        for dst_vtx in g.iter_neighbors(src_vtx):
            dst_vtx2num_src_vtc[dst_vtx] -= 1

        for dst_vtx in g.iter_neighbors(src_vtx):
            if dst_vtx2num_src_vtc[src_vtx] == 0:
                push(dst_vtx)
    if not num_output_vtc == g.num_vertices():
        cycle = find_one_cycle(g)
        assert cycle
        raise NotDAG(cycle)
    return


#################################
#################################
#################################
from seed.tiny import mk_tuple, ifNone

class NotTopologicalOrdering(ValueError):pass
class NotLocalSortedTopologicalOrdering(ValueError):pass
def validate_topological_ordering_(g, topological_ordering, /):
    topo_idx2vtx = mk_tuple(topological_ordering)
    #bug:vtx2topo_idx = inverse_uint_bijection_array(topo_idx2vtx)
    vtx2topo_idx = g.make_vertex_mapping()
    for topo_idx, vtx in enumerate(topo_idx2vtx):
        vtx2topo_idx[vtx] = topo_idx

    for src_vtx in g.iter_vertices():
        src_topo_idx = vtx2topo_idx[src_vtx]
        for dst_vtx in g.iter_neighbors(src_vtx):
            dst_topo_idx = vtx2topo_idx[dst_vtx]
            if not src_topo_idx < dst_topo_idx:
                raise NotTopologicalOrdering(((src_vtx, dst_vtx), (src_topo_idx, dst_topo_idx)))
    return (topo_idx2vtx, vtx2topo_idx)
def validate_local_sorted_topological_ordering__local_neighbor_pair_only_(g, local_sorted_topological_ordering, /, *, key=None, __lt__=None, vtx2sorted_idx=None):
    'validate only local-neighbor: (u,v) :<- pairwise(input) => [(topo_ord[u], lt_ord[u]) < (topo_ord[v], lt_ord[v])]'
    #见上面:iter_local_sorted_topological_ordering__vtx2sorted_idx_:
    (topo_idx2vtx, vtx2topo_idx) = validate_topological_ordering_(local_sorted_topological_ordering)

    if vtx2sorted_idx is None:
        vtx2sorted_idx = mk_vtx2sorted_idx(g, key=key, __lt__=__lt__)
    key = None
    __lt__ = None
    vtx2sorted_idx


    nv = len(topo_idx2vtx)
    src_topo_idx2may_min_dst_topo_idx = [None]*nv
    for src_vtx in g.iter_vertices():
        src_topo_idx = vtx2topo_idx[src_vtx]
        nv_or_min_dst_topo_idx = nv
        for dst_vtx in g.iter_neighbors(src_vtx):
            dst_topo_idx = vtx2topo_idx[dst_vtx]
            nv_or_min_dst_topo_idx = min(nv_or_min_dst_topo_idx, dst_topo_idx)
        may_min_dst_topo_idx = None if nv_or_min_dst_topo_idx == nv else nv_or_min_dst_topo_idx
        src_topo_idx2may_min_dst_topo_idx[src_topo_idx] = may_min_dst_topo_idx
    src_topo_idx2may_min_dst_topo_idx


    for src_topo_idx, src_vtx in enumerate(topo_idx2vtx):
        may_min_dst_topo_idx = src_topo_idx2may_min_dst_topo_idx[src_topo_idx]
        nv_or_min_dst_topo_idx = ifNone(may_min_dst_topo_idx, nv)
        next_topo_idx = src_topo_idx + 1
        # to validate:[next_topo_idx==nv]or[(topo_ord[u], lt_ord[u]) < (topo_ord[v], lt_ord[v])]
        if next_topo_idx < nv_or_min_dst_topo_idx:
            # [next_topo_idx < nv]
            # [next_topo_idx < min_dst_topo_idx]
            # [topo_ord[u] <!> topo_ord[v]]
            # to validate:[lt_ord[u] < lt_ord[v]]
            u = src_vtx
            v = topo_idx2vtx[next_topo_idx]
            if not vtx2sorted_idx[u] < vtx2sorted_idx[v]:
                raise NotLocalSortedTopologicalOrdering(((u, v), (src_topo_idx, next_topo_idx), (vtx2sorted_idx[u], vtx2sorted_idx[v])))
            # [lt_ord[u] < lt_ord[v]]
        else:
            if not next_topo_idx == nv_or_min_dst_topo_idx: raise 000
            # [next_topo_idx == nv_or_min_dst_topo_idx]
            # [next_topo_idx==nv]or[next_topo_idx==min_dst_topo_idx]
            # [next_topo_idx==nv]or[(u,v) is a dedge of g]
            # [next_topo_idx==nv]or[topo_ord[u] < topo_ord[v]]
    return (topo_idx2vtx, vtx2topo_idx, vtx2sorted_idx, src_topo_idx2may_min_dst_topo_idx)



from seed.graph.DAG import is_DAG, find_one_cycle
from seed.graph.DAG import iter_reversed_topological_ordering, list_a_cycle_or_reversed_topological_ordering

from seed.graph.DAG import iter_local_sorted_topological_ordering, list_a_cycle_or_local_sorted_topological_ordering

from seed.graph.DAG import NotTopologicalOrdering, NotLocalSortedTopologicalOrdering
from seed.graph.DAG import validate_topological_ordering_, validate_local_sorted_topological_ordering__local_neighbor_pair_only_

from seed.graph.DAG import *
