
from ? import (
    IUGraphImpl_by_PUEdges
    , IHasGetGraphMappingOpsCollection
    , IHasGraphDFSMethodBase
    , IHasGraphVtxDFS_FromVertices_3Color
    )
from ? import is_reiterable

class ByPUEdges__bare(IUGraphImpl_by_PUEdges):
    def __init__(self, reiter_puedges, vertex_eq):
        self.__puedges = reiter_puedges
        self.__vertex_eq = vertex_eq
        assert is_reiterable(reiter_puedges)
    def vertex_eq(self, v, u):
        return self.__vertex_eq(v, u)
    def unstable_iter_puedges(self):
        return iter(self.__puedges)
class ByPUEdges(ByPUEdges__bare):
    def __init__(self, reiter_all_vertices, reiter_puedges, vertex_eq
        , **kwargs):
        assert is_reiterable(reiter_all_vertices)
        self.__all_vertices = reiter_all_vertices
        super().__init__(
            reiter_puedges=reiter_puedges
            , vertex_eq=vertex_eq
            , **kwargs)
    def unstable_iter_vertices(self):
        return iter(self.__all_vertices)
class ByPUEdgesWithGraphMapping(ByPUEdges, IHasGetGraphMappingOpsCollection):
    def get_graph_mapping_ops_collection(self):
class ByPUEdgesWithDFS(ByPUEdges, IHasGraphVtxDFS_FromVertices_3Color):
    def vertex_dfs_from_vertices__3color(self, from_vertices):


