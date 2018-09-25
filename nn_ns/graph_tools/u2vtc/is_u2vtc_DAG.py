
__all__ = ['is_u2vtc_DAG']

from nn_ns.graph.directed_acyclic_graph import isDAG as _isDAG
from .ma_u2vtc_to_array_u2vtc_ex import ma_u2vtc_to_array_u2vtc_ex
def is_u2vtc_DAG(u2vtc, *, using_std_vertex:bool):
    # u2vtc -> bool -> bool
    array_u2vtc, uint2vertex, vertex2uint = \
        ma_u2vtc_to_array_u2vtc_ex(u2vtc, using_std_vertex=using_std_vertex)
    return _isDAG(array_u2vtc)
'''
def is_u2vtc_DAG(u2vtc):
    # u2vtc -> bool
    return _isDAG(u2vtc)
'''

