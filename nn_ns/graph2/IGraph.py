


'''
G = (V, E)
V :: Set Vertex
E :: Map NonUniqueStdEdge UInt
Vertex <: Hashable
StdEdge <: Hashable
    should not compare Edge directly
    eq(e1,e2) ::= std(e1) == std(e2)
Edge    = UInt # unique representation
        | Set Vertex of len [1..2] # nonunique representation
    directed simple graph <: undirected graph with multiple edges
    undirected graph is directed graph of which each edge has two directions
undirected multi-graph
   self-loop
   multiple edge
undirected simple graph
    no self-loops
    no multiple edges

Edge -- directed? standardized? unique?
V = [offset..offset+nv-1]?? for bucket sort
vertex color??
edge weight??


Edge implement:
    UniqueEdge(AEdge):
        # to access edge data(e.g. weight)
        # should exist in graph, has edge data
        Pointer
        Name
        UInt
        (StdEdge, UInt)
    NonUniqueEdge(QEdge):
        # to query existance, multi-edges
        # may not exist in graph, has no data
        (Vertex, Vertex)
        Set Vertex of len [1..2]

        standardized?
            NonUniqueNonStdEdge
                NonUniqueNonStdUndirectedEdge
                    (Vertex, Vertex) unsorted
                # no need: NonUniqueNonStdDirectedEdge
            NonUniqueStdEdge
                NonUniqueStdUndirectedEdge
                    (Vertex, Vertex) sorted
                    Set Vertex of len [1..2]
                NonUniqueStdDirectedEdge
                    (Vertex, Vertex)

    DirectedAEdge(PAEdge):
        PAEdge = (PEdge, AEdge)
            # PEdge gives the direction
            # AEdge tells which edge
        used in:
            unstable_iter_adjacent_paedges
            dfs underlying undirected graph of a directed graph
        if aedge is directed, then aedge's direction is as pdedge
        if aedge is undirected, then aedge's direction is as suedge

    so there are 4 data types of edges:
        AEdge: UniqueEdge
            if directed graph then directed
        PEdge: NonUniqueStdDirectedEdge == NonUniqueNonStdUndirectedEdge
            (Vertex, Vertex) unsorted
        SEdge: NonUniqueStdUndirectedEdge or NonUniqueStdDirectedEdge
            depends on whether the graph is directed
        PAEdge:
            PAEdge = (PEdge, AEdge)
            always a directed edge
    but when using the underlying undirected graph of directed graph:
        we should use a directed edge as an undirected edge
        has_pdedge(pdedge)
        has_puedge(puedge) == has_pdedge(pdedge) or has_pdedge(reversed(pdedge))
    so there are 6 purpose types of edges:
        AUEdge, PUEdge, SUEdge
        ADEdge, SDEdge(PDEdge)
        PAEdge
        # only 4 data types
        # AUEdge = ADEdge = AEdge
        # PUEdge = PDEdge = SDEdge = PEdge = DEdge
        # SUEdge
        # PAEdge


G implement:
    1) (Set Vertex, [Edge])
    1') (Set Vertex, Set Edge)
    2) (Set Vertex, Map (Vertex, Vertex) UInt)
    2') (Set Vertex, Map (Vertex, Vertex) Bool)
    3) (Set Vertex, Map Vertex [Vertex])
    3') (Set Vertex, Map Vertex (Set Vertex))
    3'') (Set Vertex, Map Vertex (Map Vertex UInt))
    4) ([0..nV-1], [[UInt]])
    4') ([0..nV-1], [[Bool]])


------------
method that have different speed:
    IMethod__O(...)
constructor:
    IConstructor:
        @classmethod
        def make_graph_from_...



'''











class IFiniteGraphOps(ABC):
    '''
infinite graph - e.g. state space of same a game
    we donot know size
    we may not know whether a state is a vertex (or maybe we should treat invalid state as an unreachable vertex from initial state)
    we are not able to iter all hedges # maybe not countable
finite graph - len(Vertex), len(Edge), len(HEdge)
'''
    __slots__ = ()
    ## s::Set ==>> len(s), iter(s), x in s
    @abstractmethod
    def get_vertex_set(self, g):
        # -> V; Vertex
        pass
    @abstractmethod
    def get_edge_set(self, g):
        # -> E; Edge
        pass
    @abstractmethod
    def get_hedge_set(self, g):
        # -> HEdge; half edge set
        # a vertex may connect to 0~many hedges
        # an edge may connect to 0~many hedges (normally, 2)
        pass
    @abstractmethod
    def explain_hedge2DVE(self, g, hedge):
        # hedge -> (direction::Bool, vertex::V, edge::E)
        # direction=True <==> vertex->edge  # vertex can see edge
        # direction=False <==> vertex<-edge # vertex cannot see edge
        pass






############### TODO: remove has_vertex by testing (v in V)
__all__ = '''
    inside
    total__ON
    GraphAlgoSpeed

    IUnstableIterVertices
    IStdPUEdge
    IUnstableIterPUEdges
    IUnstableIterSDEdges

    IGetNumVertices
    IGetNumEdges

    IHasVertex
    IHasPUEdge
    IGraph

    IHasSDEdge
    IDGraph

    IUnstableIterAEdges
    IAEdgesHashable

    IGetVertexData
    Reference_to_hash_id
    IGetAEdgeData
    '''.split()


from abc import ABCMeta, abstractmethod, ABC
from collections.abc import Hashable
from enum import Flag, Enum
from itertools import chain, product
#from operator import __or__
from seed.iters.binary_op import foldl #, iter_accumulate, iter_accumulate_chain


def inside(obj, iterable):
    for x in iterable:
        if obj == x: return True
    return False
def total__ON(iterable):
    r = 0
    for _ in iterable: r += 1
    return r



# --------

'''
class GraphAlgoSpeed(Enum):
    OE
    OV
    OD # max degree; OD <= OE; OD ?unorder? OV
    OlogE
    OlogV
    OlogD
    O1
    OVV # O(|V|^2)

    # for IHasPUEdge
    OE_OVV
    OE_OV # O(|E|+|V|)
    OV_OD
    OV_OlogD
    OlogV_OD
    OlogVD # O(log(|V|*max_degree))


    OW # assume graph is a subgraph of graph with vertices [0..W-1]
'''
GraphAlgoSpeed = Flag('GraphAlgoSpeed', '''
    OW
    OE
    OVV
    OV
    OD
    O1

    OlogE
    OlogV
    OlogD
    '''.split())
    # Oa|Ob means O(a*b)
    # {Oa, Ob} means O(a+b)
# prime_speed :: GraphAlgoSpeed             # product
# macro_speed :: frozenset<GraphAlgoSpeed>  # sum of product
macro_O1 = frozenset([GraphAlgoSpeed.O1])

def prime_graph_algo_speed_mul(prime_speedL, prime_speedR):
    return prime_speedL | prime_speedR
def prime_graph_algo_speed_product(prime_speeds):
    # prime_speeds -> prime_speed
    return foldl(prime_graph_algo_speed_mul, GraphAlgoSpeed.O1, prime_speeds)
def prime_graph_algo_speed_sum(prime_speeds):
    # prime_speeds -> macro_speed
    return frozenset(chain(macro_O1, prime_speeds))
def macro_graph_algo_speed_mul(macro_speedL, macro_speedR):
    mul = prime_graph_algo_speed_mul
    return prime_graph_algo_speed_sum(
        mul(a, b) for a, b in product(macro_speedL, macro_speedR))
def macro_graph_algo_speed_product(macro_speeds):
    # macro_speeds -> macro_speed
    return foldl(macro_graph_algo_speed_mul, macro_O1, macro_speeds)
def macro_graph_algo_speed_sum(macro_speeds):
    # macro_speeds -> macro_speed
    return prime_graph_algo_speed_sum(chain.from_iterable(macro_speeds))

















class IUnstableIterVertices(ABC):
    # if G = E, and assume no isolated vertex ==>> OE_OV
    # if G = [[Count]] and assume no isolated vertex ==>> OW > OV
    # normally: OV
    @abstractmethod
    def unstable_iter_vertices(self):pass

    @abstractmethod
    def unstable_iter_vertices__speed(self):
        return prime_graph_algo_speed_sum([GraphAlgoSpeed.OE_OV])


# --------

class IStdPUEdge(ABC):
    @abstractmethod
    # pue/sue may or may not in G.E
    # should not compare pue directly, or use pue as mapping key
    # puedge -> suedge
    # sue: to be hashable and comparable
    def standardize_puedge(self, pue):pass

class IUnstableIterPUEdges(IStdPUEdge):
    # if G = Matrix<Vertex, Vertex, Count> ==>> OE_OVV
    # if G = ([0..nV-1], [[Vertex]]) ==>> OE_OV
    # normally: OE
    @abstractmethod
    # multi-edges duplicated in the result
    # but undirected/bidirected edge has 1 occurrence
    def unstable_iter_puedges(self):pass
    @abstractmethod
    def unstable_iter_puedges__speed(self):
        return prime_graph_algo_speed_sum([GraphAlgoSpeed.OE_OVV])

    def unstable_iter_suedges(self):
        it = self.unstable_iter_puedges()
        return map(self.standardize_puedge, it)
    def unstable_iter_suedges__speed(self):
        return self.unstable_iter_puedges__speed()




# --------

class IUnstableIterSDEdges(IUnstableIterPUEdges):
    @abstractmethod
    def unstable_iter_sdedges(self):pass
    @abstractmethod
    def unstable_iter_sdedges__speed(self):
        return prime_graph_algo_speed_sum([GraphAlgoSpeed.OE_OVV])
    def unstable_iter_puedges(self):
        return self.unstable_iter_sdedges()
    def unstable_iter_puedges__speed(self):
        return self.unstable_iter_sdedges__speed()



# --------

class IGetNumVertices(IUnstableIterVertices):
    def get_num_vertices(self):
        return total__ON(self.unstable_iter_vertices())
    def get_num_vertices__speed(self):
        return self.unstable_iter_vertices__speed()
class IGetNumEdges(IUnstableIterPUEdges):
    # count multi-puedge
    def get_num_edges(self):
        return total__ON(self.unstable_iter_puedges())
    def get_num_edges__speed(self):
        return self.unstable_iter_puedges__speed()














# --------

class IHasVertex(IUnstableIterVertices):
    # OW/OE_OV/OV/OlogV/O1
    # why seperate this method from IGraph?
    #   because IHasVertex__O1/OlogV/OV to override IHasVertex__OV_OE
    def has_vertex(self, vtx):
        return inside(vtx, self.unstable_iter_vertices())
    def has_vertex__speed(self):
        return self.unstable_iter_vertices__speed()


# --------

class IHasPUEdge(IUnstableIterPUEdges):
    # inside: OE_OVV/OE_OV/OE
    # edge map: OlogE/O1
    # vertex map: OV_OD/OV_OlogD/OV/OlogV_OD/OlogVD/OlogV/OD/OlogD/O1
    #               <<== [OV/OlogV/O1]+[OD/OlogD/O1]
    #                   OD <= OE can not compare with OV
    def has_puedge(self, pue):
        sue = self.standardize_puedge(pue)
        return self.has_suedge(sue)
    def has_suedge(self, sue):
        return inside(sue, self.unstable_iter_suedges())
    def has_suedge__speed(self):
        return self.unstable_iter_suedges__speed()
    def has_puedge__speed(self):
        return self.has_suedge__speed()



# --------------------------





















# --------------------------

class PEdgeIO:
    # PEdge = PUEdge = PDEdge = SDEdge
    # O(1)
    def make_pedge(self, v, u):
        'make_pedge == pedge2vertex_pair^-1'
        return (v,u)
    # O(1)
    def pedge2vertex_pair(self, pedge):
        v,u = pedge
        return pedge
    # O(1)
    def reverse_pedge(self, pedge):
        v,u = self.pedge2vertex_pair(pedge)
        return self.make_pedge(u,v)



class IGraph(PEdgeIO, IHasPUEdge, IHasVertex, IGetNumEdges, IGetNumVertices, Hashable):
    '''see IGraphOps also

unstable means the order may be changed between different calls
directed graph is a undirected graph with direction
OV = O(len(V))
OE = O(len(E))
OD = O(max(degree(vtx) for vtx in V))
OVE = O(len(V)*len(E))
OE_OVV = O(|E|+|V|^2)

([NonUnique]|Unique)([NonStd]|Std)(Directed|Undirected)Edge
dedge - nonunique nonstandard directed edge
uedge - nonunique nonstandard undirected edge

possible implement:
    dedge - ??
    std_dedge - (v, u)
    unique_dedge - ??
    unique_std_dedge - ((v,u), idx) | edge_idx
        or (v, u) and (v,u) in G.E and every dedge is unique

    uedge - (v,u)
    std_uedge - {v} | {v,u} where v!=u
    unique_uedge - ((v,u), idx) | edge_idx
        or (v,u) and (v,u) in G.E and every uedge is unique
    unique_std_uedge - (std_uedge, idx) | edge_idx
        or std_uedge and std_uedge in G.E and every uedge is unique


no unique edge now
    since "unique" require:
        1) edge to exist in graph
        2)  *) all edges in graph are unique
         or *) index multiple edges

'''
    pass











# --------

class IHasSDEdge(IUnstableIterSDEdges):
    def has_sdedge(self, sde):
        return inside(sde, self.unstable_iter_sdedges())
    def has_sdedge__speed(self):
        return self.unstable_iter_sdedges__speed()


class IDGraph(IHasSDEdge, IGraph):
    '''directed graph has directed edges'''
    pass




class IUnstableIterAEdges(IUnstableIterPUEdges):
    # aedge should exist in graph



    ### AEdge

    @abstractmethod
    def unstable_iter_aedges(self):pass
    @abstractmethod
    def unstable_iter_aedges__speed(self):pass

    @abstractmethod
    # O(1)??
    def aedge_equal(self, aedgeL, aedgeR):pass

    @abstractmethod
    # O(1)??
    # if directed graph then pdedge else puedge
    def aedge2pedge(self, ae):pass

    ### PAEdge

    @abstractmethod
    # O(1)??
    def aedge2paedge(self, ae, reverse=False):pass
    @abstractmethod
    # O(1)
    def reverse_paedge(self, pae):pass
    @abstractmethod
    # O(1)
    def paedge2aedge(self, pae):pass
    @abstractmethod
    # O(1)
    def paedge2pedge(self, pae):pass


    def unstable_iter_puedges(self):
        return map(self.aedge2pedge, self.unstable_iter_aedges())
    def unstable_iter_puedges__speed(self):
        return self.unstable_iter_aedges__speed()





class IAEdgesHashable(IUnstableIterAEdges):
    def aedge_equal(self, aedgeL, aedgeR):
        return aedgeL == aedgeR


class IGetVertexData(IHasVertex):
    # vertex is immutable and hashable
    # but vertex data may be mutable
    @abstractmethod
    def get_vertex_data(self, vtx):pass

class Reference_to_hash_id(Hashable):
    # to use as aedge
    def __init__(self, obj):
        self.__obj == obj
    @property
    def obj(self):
        return self.__obj
    def __hash__(self):
        return id(self.__obj)
    def __eq__(self, other):
        if not isinstance(other, __class__): return NotImplemented
        return self.__obj is other.__obj
    def __ne__(self, other):
        return not (self == other)
class IGetAEdgeData(IUnstableIterAEdges):
    # aedge is hashable?? # may or may not immutable
    # aedge data may be mutable
    # when the aedge data is the aedge itself,
    #   hash should depend on id(aedge)
    #   and eq<aedge> should be "is"
    #   e.g. aedge == ((v,u), mutable_field) == aedge_data
    #   see Reference_to_hash_id
    @abstractmethod
    def get_aedge_data(self, aedge):pass

class IGetGraphData(IGraph):
    # e.g. malloc dfs color map
    @abstractmethod
    def get_graph_data(self, aedge):pass














# ----------------
class GraphError(Exception):pass
class VertexError(GraphError, KeyError):pass
class EdgeError(GraphError):pass
class AEdgeError(EdgeError):pass
class PEdgeError(EdgeError):pass
class SUEdgeError(EdgeError):pass


class IUnstableIterAdjacentPAEdges(IUnstableIterAEdges, IGraph):
    # duplicated multi-edge
    # undirected edge ==>> bidirected edge
    # result = Iter (vtx, out_vtx)
    def unstable_iter_adjacent_paedges(self, vtx):
        if not self.has_vertex(vtx): raise VertexError
        for aedge in self.unstable_iter_aedges():
            pedge = self.aedge2pedge(aedge)
            v,u = self.pedge2vertex_pair(pedge)
            if vtx == v: reverse = False
            elif vtx == u: reverse = True
            else: continue
            yield self.aedge2paedge(aedge, reverse)
    def unstable_iter_adjacent_paedges__speed(self):
        return self.unstable_iter_paedges__speed()
class IUnstableIterIncomeAdjacentAEdges(IDGraph):
    # duplicated multi-edge
    # result = Iter (in_vtx, vtx)
    def unstable_iter_income_adjacent_aedges(self, vtx):
        if not self.has_vertex(vtx): raise VertexError
        for ae in self.unstable_iter_aedges():
            pe = self.aedge2pedge(ae)
            v,u = self.pedge2vertex_pair(pe)
            if vtx == u: yield ae
    def unstable_iter_income_adjacent_aedges__speed(self):
        return self.unstable_iter_aedges__speed()

class IUnstableIterOutgoAdjacentAEdges(IDGraph):
    # duplicated multi-edge
    # result = Iter (vtx, out_vtx)
    def unstable_iter_outgo_adjacent_aedges(self, vtx):
        if not self.has_vertex(vtx): raise VertexError
        for ae in self.unstable_iter_aedges():
            pe = self.aedge2pedge(ae)
            v,u = self.pedge2vertex_pair(pe)
            if vtx == v: yield ae
    def unstable_iter_outgo_adjacent_aedges__speed(self):
        return self.unstable_iter_aedges__speed()




class IUnstableIterAdjacentVertices(IUnstableIterAdjacentPAEdges):
    # no duplicate vertices
    def unstable_iter_adjacent_vertices__speed(self):
        return self.unstable_iter_paedges__speed()
    def unstable_iter_adjacent_vertices(self, vtx, excepts=()):
        excepts = set(excepts)
        for pae in self.unstable_iter_paedges():
            pe = self.paedge2pedge(pae)
            _, u = self.pedge2vertex_pair(pe)
            if u not in excepts:
                yield u
                del excepts[u]


















# ----------------

UGraphDFS_Action = Enum('UGraphDFS_Action', 'EnterRoot ExitRoot EnterPAEdge ExitPAEdge EnterExitPAEdge')
UGraphDFS_Color = Enum('UGraphDFS_Color', 'UnVisit Enter Exit')
class IUGraphDFS_Space:
    # def clear(self, ug):pass
    @abstractmethod
    def get_color(self, ug, vtx):pass
    @abstractmethod
    def set_color(self, ug, vtx, color):pass
class IUGraphDFS(Iterator):
    '''

result:
    iter[( ((EnterRoot|ExitRoot), vtx)
         | ((EnterPAEdge|ExitPAEdge|EnterExitPAEdge), paedge)
         )
        ]

NOTE:
    if graph is a tree ==>> need not color
        space
'''
    @classmethod
    @abstractmethod
    def make_ugraph_dfs(cls, ug, roots, space):
        '''
space should be clean;
will query space with new nonparent adjacent vertices or new root
'''
        assert isinstance(ug, IUnstableIterAdjacentPAEdges)
        assert isinstance(space, IUGraphDFS_Space)
        ...

class IUGraphDFS_with_ancestors_view(IUGraphDFS):
    @abstractmethod
    def get_ancestor_seq_view(self):pass




if __name__ == '__main__':
    from seed.helper.print_global_names import print_global_names
    print_global_names(globals(), prefix='     ')
