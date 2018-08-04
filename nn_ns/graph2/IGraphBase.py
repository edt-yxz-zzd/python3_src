

@compute_and_cached
def f(self, ...):
    'docstring'
    pass
will insert __f__, f:
    @cached
    def {f}(self, ...):
        'docstring'
        return type(self).__{f}__(self, ...)
    @abstractmethod
    def __{f}__(self, ...):
        'docstring'
        raise NotImplementedError

ReorderBases_and_CollectSlots_Meta
class IGraphBase(metaclass=ReorderBases_and_CollectSlots_Meta):pass

class IXGraphBase(IGraphBase, meaningful=True):pass
class IUGraphBase(IXGraphBase, meaningful=True):pass
class IDGraphBase(IXGraphBase, meaningful=True):pass
    # meaningful means this class is not a transparent base classes collection
    # issubclass will indeed test this class
    #   if meaningful is False, then skip test on this class and class body should be empty

'''
since use "meaningful", we now need not these:
class IUGraphImmutableBase(IXGraphImmutableBase, IUGraphBase):pass
class IDGraphImmutableBase(IXGraphImmutableBase, IDGraphBase):pass
'''

class IXGraphImmutableBase(IXGraphBase, meaningful=True):
    # compute and cache
    def is_empty(self):pass
    def num_vertices():pass
    def num_aedges():pass

    # dgraph should not be ugraph
    #   i.e. not "class DGraph(UGraph)"
    #   why?
    #       simple dgraph's underlying ugraph may have multiedge
    def is_directed():pass
    def get_may_edge_relationship():
        '''-> None | (xgraph, explain_new_vtc)
    e.g. planar embedding

    explain_new_vtc :: Map new_vtx explain
    explain = (OLD_Vtx_tag, old_vtx)
            | (OLD_AEdge_tag, aedge)
            | (OLD_HEdge_tag, hedge)
    '''
        pass


    def has_multiedges():pass
    def has_self_loops():pass
    def is_simple():pass


    def has_cycles():pass # not "is forest"
    def has_isolated_vertices():pass
    def is_weak_connected():pass
    def is_weak_biconnected():pass
    def is_weak_triconnected():pass









class IXGraphImmutable(IXGraphImmutableBase, meaningful=True):
    # () -> None | IBucketSortableTV
    #   if not None, then detect whether BoundedUInt
    def get_may_vertexTV():pass
    def get_may_aedgeTV():pass
    def get_may_hedgeTV():pass
    def is_vertex_bounded_uint():pass
    def is_aedge_bounded_uint():pass
    def is_hedge_bounded_uint():pass

    def get_may_vertex_upper_bound():
        # -> None | uint
        pass
    def get_may_aedge_upper_bound():pass
    def get_may_hedge_upper_bound():pass







class IUGraphImmutableBase(IXGraphImmutableBase, IUGraphBase, meaningful=True):
    def to_sym...():pass -> dgraph
    def is_free_forest():pass
        == not is_directed() and not has_cycles()
    def is_free_tree():pass
        == is_free_forest() and is_weak_connected()



class IDGraphImmutableBase(IXGraphImmutableBase, IDGraphBase, meaningful=True):
    # compute and cache
    def erase_direction():pass -> ugraph
    def reverse_direction():pass -> dgraph

    def is_strong_connected():pass
    def is_strong_biconnected():pass
    def is_strong_triconnected():pass



    def has_one_parent_per_nonroot():pass
    def has_exactly_one_root():pass
    def is_DAG():pass                 # DAG= multi-srcs; multi-parents
        == is_directed() and not has_cycles()
        == is_rooted_compact_forest()
    def is_rooted_compact_tree():pass # DAG; single src; multi-parents
        == is_DAG() and has_exactly_one_root()
    def is_rooted_forest():pass       # DAG; multi-srcs; all maybe parent
        == is_DAG() and has_one_parent_per_nonroot()
    def is_rooted_tree():pass         # DAG; single src; all maybe parent
        == is_DAG() and has_exactly_one_root() and has_one_parent_per_nonroot()

class IDAG_ImmutableBase(IDGraphImmutableBase, meaningful=True):
    # compute and cache
    def DAG_sources():pass
    def DAG_sinks():pass
    def DAG_topological_sort():
        # -> [vtx]
        pass
class IDForest_ImmutableBase(IDAG_ImmutableBase, meaningful=True):
    # compute and cache
    def roots():
        return DAG_sources()
class IDTree_ImmutableBase(IDAG_ImmutableBase, meaningful=True):
    # compute and cache
    def root():pass






