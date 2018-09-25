
__all__ = ['u2vtc_to_std_u2vtc_ex']

from .incomplete_u2vtc_to_vertice_set import incomplete_u2vtc_to_vertice_set
from types import MappingProxyType
from .StdVertexEchoMap import StdVertexEchoMap

def u2vtc_to_std_u2vtc_ex(u2vtc, *, using_std_vertex:bool):
    # u2vtc -> bool -> (std_u2vtc, {uint:vertex}, {vertex:uint})
    if using_std_vertex:
        num_vertices = len(u2vtc)
        if not all(type(v) is int and 0 <= v < num_vertices for v in incomplete_u2vtc_to_vertice_set(u2vtc)): raise TypeError('not std_u2vtc: {u2vtc}')
        std_u2vtc = {v:list(vtc) for v, vtc in u2vtc.items()}

        uint2uint = StdVertexEchoMap(num_vertices)
        vertex2uint = uint2vertex = uint2uint
            # MappingProxyType(uint2uint)
    else:
        std_u2vtc = {}
        vertex2uint = {v:i for i, v in enumerate(u2vtc)} # {Vertex:UInt}
        for u, vtc in u2vtc.items():
            std_u2vtc[vertex2uint[u]] = [vertex2uint[v] for v in vtc]

        uint2vertex = {i:v for i, v in enumerate(u2vtc)} # {UInt:Vertex}

        vertex2uint = MappingProxyType(vertex2uint)
        uint2vertex = MappingProxyType(uint2vertex)
    return std_u2vtc, uint2vertex, vertex2uint


