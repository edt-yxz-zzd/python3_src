
__all__ = ['ma_u2vtc_to_array_u2vtc_ex']

from collections.abc import Sequence
from .u2vtc_to_std_u2vtc_ex import u2vtc_to_std_u2vtc_ex
from .StdVertexEchoMap import StdVertexEchoMap

def ma_u2vtc_to_array_u2vtc_ex(ma_u2vtc, *, using_std_vertex:bool):
    # ma_u2vtc -> bool -> (array_u2vtc, uint2vertex, vertex2uint)
    if using_std_vertex and isinstance(ma_u2vtc, Sequence):
        array_u2vtc = ma_u2vtc
        uint2vertex = vertex2uint = StdVertexEchoMap(len(array_u2vtc))
    else:
        std_u2vtc, uint2vertex, vertex2uint = \
            u2vtc_to_std_u2vtc_ex(ma_u2vtc, using_std_vertex=using_std_vertex)
        array_u2vtc = [std_u2vtc[v] for v in range(len(std_u2vtc))]
    return array_u2vtc, uint2vertex, vertex2uint

