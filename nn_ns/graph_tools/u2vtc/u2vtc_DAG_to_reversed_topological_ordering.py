

__all__ = '''
    NotDAGError
    u2vtc_DAG_to_reversed_topological_ordering
    '''.split()


from nn_ns.graph.directed_acyclic_graph import (
    NotDAGError
    , reversed_topological_ordering as _to_rtopo_ordering
    )
from .ma_u2vtc_to_array_u2vtc_ex import ma_u2vtc_to_array_u2vtc_ex
def u2vtc_DAG_to_reversed_topological_ordering(
    u2vtc_DAG, *, using_std_vertex:bool):
    # u2vtc_DAG -> bool -> [vertex]
    # dedge direction: left_vertex <-[dedge]- right_vertex
    using_std_vertex = bool(using_std_vertex)
    array_u2vtc, uint2vertex, vertex2uint = \
        ma_u2vtc_to_array_u2vtc_ex(u2vtc, using_std_vertex=using_std_vertex)

    uints = _to_rtopo_ordering(array_u2vtc)
    if using_std_vertex:
        r_ordering = uints
    else:
        r_ordering = [uint2vertex[i] for i in uints]
    return r_ordering

'''
def u2vtc_DAG_to_reversed_topological_ordering(u2vtc_DAG):
    # u2vtc_DAG -> ([vertex]|raise NotDAGError)
    # dedge direction: left_vertex <-[dedge]- right_vertex
    r_ordering = vertices = _to_rtopo_ordering(u2vtc_DAG)
    return r_ordering
'''



