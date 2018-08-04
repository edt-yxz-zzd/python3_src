
__all__ = '''
IGraphRelated
    IGraphOps
    IGraphBase

IGraphBase
    IGraphProxy

    IHasGraphMethod
        IHasVertexEq
            IHasAEdgeEq
                IHasHEdgeEq
        IHasGraphDFSMethodBase
        IHasGetGraphMappingOpsCollection

    IAbstractGraph
        IFiniteVertices
        IBGraph
            IXGraph
                IUGraph
                IDGraph

    IGraphImpl
        IExplicitGraph
            IExplicitUGraph
            IGraphImplDatastructure
                IUGraphImpl_by_PUEdges
    '''.split()

class IGraphRelated(ABC):
    # is not a graph
    # e.g. graph_ops/graph_mapping_ops is not a graph
    #       but it is related to this graph module
    __slots__ = ()

class IGraphOps(IGraphRelated):
    # not graph, but offer ops to handle an related object as graph
    # graph_ops.dfs(data_as_graph, ...)
    pass

class IGraphBase(IGraphRelated):
    # instance of IGraphBase must be a graph, conceptually
    pass
class IGraphProxy(IGraphBase):
    # wrap data(may be graph) into graph
    # maynot known the exactly graph type in static
    # so, we test it dynamic
    #   may override __getattr__
    is_explicit_graph()
    is_directed_graph()
    is_DAG()
    has_vertex_eq()
    pass


class IHasGraphMethod(IGraphBase):
    # concern?? which method the graph object have
    # user should call correspond free function
    #   e.g. has_vertex_eq(g)
    #       <==> g in IHasVertexEq or
    #           (g in IGraphProxy and getattr(g, 'has_vertex_eq', const False)())
    pass
class IHasVertexEq(IHasGraphMethod):
    # implicit_graph may have vertex_eq
    # explicit_graph should have vertex_eq
    vertex_eq(v, u)
class IHasAEdgeEq(IHasVertexEq):
    aedge_eq(aedge1, aedge2)
class IHasHEdgeEq(IHasAEdgeEq):
    hedge_eq(hedge1, hedge2)
class IHasGetGraphMappingOpsCollection(IHasGraphMethod):
    get_graph_mapping_ops_collection() # -> IGraphMappingOpsCollection
class IHasGraphDFSMethodBase(IHasGraphMethod):
    # there are many many dfs interface/implement
    pass
class IHasGraphVtxDFS_FromVertices_3Color(IHasGraphDFSMethodBase):
    # 3-color
    #   means the dfs implement use 3 colors for vertices
    # vertex_dfs
    #   means the output contain vertices only, no edges
    #   format: Iter (src_vtx, dst_vtx, color)
    # from_vertices
    #   means to use from_vertices as possible dfs roots
    vertex_dfs_from_vertices__3color(from_vertices)


class IAbstractGraph(IGraphBase):
    # concern?? the graph properties instead of the implement
    # e.g. the graph is finite conceptually, but we donot the size of the implement
    pass
class IFiniteVertices(IAbstractGraph):
    # but maybe too large to know the size
    # e.g. the game state
    # subclass may be: NumVertexUpperBound/NumVertex
    # sibling class may be: IFiniteEdges
    # subclass may be: IFiniteGraph(IFiniteEdges, IFiniteVertices)
    pass
class IBGraph(IAbstractGraph)
class IXGraph(IBGraph)
class IUGraph(IXGraph)
    # undirected graph with multiedge, loops
    #   maybe disconnected
class IDGraph(IXGraph)



class IGraphImpl(IGraphBase):
    # concern?? properties of the underlying data structure of graph
    # e.g. IExplicitGraph
    pass
class IExplicitGraph(IVertexEq, IGraphImpl):
    # maybe infinite
    # e.g. 0->1->2->...
    pass
class IExplicitUGraph(IExplicitGraph, IUGraph):

class IGraphImplDatastructure(IGraphImpl):
    # concern?? the underlying data structure of graph
    # e.g. IGraphImpl_by_PUEdges
    pass
class IUGraphImpl_by_PUEdges(IExplicitUGraph, IGraphImplDatastructure):
    # UnstableReIter (Vtx, Vtx)
    unstable_iter_puedges()




