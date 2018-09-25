
__all__ = ['u2vtc_to_reversed_topological_ordered_strong_connected_components']

from nn_ns.graph.directed_graph import (
    to_reversed_topological_ordered_strong_connected_components
    as _to_rtopo_components
    )
from .ma_u2vtc_to_array_u2vtc_ex import ma_u2vtc_to_array_u2vtc_ex
def u2vtc_to_reversed_topological_ordered_strong_connected_components(
    u2vtc, *, using_std_vertex:bool):
    # u2vtc -> bool -> [nonempty[vertex]]
    using_std_vertex = bool(using_std_vertex)
    array_u2vtc, uint2vertex, vertex2uint = \
        ma_u2vtc_to_array_u2vtc_ex(u2vtc, using_std_vertex=using_std_vertex)

    uints_ls = _to_rtopo_components(array_u2vtc)
    if using_std_vertex:
        components = uints_ls
    else:
        components = [[uint2vertex[i] for i in uints] for uints in uints_ls]
    return components
'''
def u2vtc_to_reversed_topological_ordered_strong_connected_components(
    u2vtc):
    # u2vtc -> [nonempty[vertex]]
    components = _to_rtopo_components(u2vtc)
    return components

'''

if __name__ == '__main__':
    u2vtc = {0: [2, 1, 3], 1: [4], 2: [], 3: [5], 4: [], 5: []}
    u2vtc_to_reversed_topological_ordered_strong_connected_components(u2vtc, using_std_vertex=True)

