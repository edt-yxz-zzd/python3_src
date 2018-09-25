

__all__ = ['u2vtc_to_maybe_circle']

from nn_ns.graph.directed_acyclic_graph import \
    find_a_circle as _find_a_circle
from .ma_u2vtc_to_array_u2vtc_ex import ma_u2vtc_to_array_u2vtc_ex

def u2vtc_to_maybe_circle(u2vtc, *, using_std_vertex:bool):
    # u2vtc -> (None|nonempty_tuple<vertex>)
    array_u2vtc, uint2vertex, vertex2uint = \
        ma_u2vtc_to_array_u2vtc_ex(u2vtc, using_std_vertex=using_std_vertex)
    return _find_a_circle(array_u2vtc)
'''
def u2vtc_to_maybe_circle(u2vtc):
    # u2vtc -> (None|nonempty_tuple<vertex>)
    return _find_a_circle(u2vtc)
'''

