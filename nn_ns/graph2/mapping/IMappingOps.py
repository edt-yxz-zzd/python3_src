


# TODO: __slots__ = ()

'''
see: "def - mapping.txt"


position in big-picture
    # finest dfs, datatype are offered by user
    def dfs_3color__oriented(
        graph_ops__without_mapping_ops_collection, oriented_graph
        , vtx2tricolor_ops, vtx2tricolor # offer mapping_ops directly
        , ancestor_stack
        ):pass
    def dfs_3color__unoriented(
        graph_ops__without_mapping_ops_collection, graph
        , vtx2tricolor_ops, vtx2tricolor # offer mapping_ops directly
        , ancestor_stack
        , iterator_stack
        ):pass

    # coarser
    # dfs depended on IGraphOps interface
    #   implictly offer graph_mapping_ops via graph_ops
    def dfs(graph_ops:IGraphOpsWithMappingOps, graph):pass
    # dfs depended on concrete ops class
    def dfs(graph_ops:XXX_GraphOps, graph):pass

    # coarsest
    # dfs depended on IGraph interface
    def dfs(graph:IGraph):pass
    # dfs depended on concrete graph class
    def dfs(graph:XXX_Graph):pass

    # dfs with special requirement
    def preordering_dfs(...):pass

    # using dfs instead of graph!
    #   depended on IXXX_DFS interface
    #   DFS are classified by its output format
    #       e.g. dfs_obj :: Iter<(Case, Payload)>
    #       what are the cases?? which case to which payload??
    #       which content will uniquely appear in Payload?
    def is_connected(dfs:IXXX_DFS):pass
    def is_connected(dfs_output_explain_ops, dfs_iter):pass

'''




__all__ = '''
IMappingOpsRelated
    IMappingOps
        IKnownFullKeys
            ICommonMappingOps

        ICommonMappingOps
            IFullMappingOps
            IPartialMappingOps
                IKnownPartialSize
                IKnownPartialKeys
    '''.split()

from abc import abstractmethod, ABC

class IMappingOpsRelated(ABC):pass
class IMappingOps(IMappingOpsRelated):pass
'''
class IOptionalMappingOps(IMappingOps):
    # optional
    weakref_dict_of(self, key): # -> WeakKeyDictionary<Key, ...>
'''

class IKnownFullKeys(IMappingOps):
    @abstractmethod
    def iter_full_keys(self): # -> Iter Key
        raise NotImplementedError
    @abstractmethod
    def full_size(self): # -> UInt
        raise NotImplementedError

class ICommonMappingOps(IKnownFullKeys):
    # common of IFullMappingOps and IPartialMappingOps
    pass
class IFullMappingOps(ICommonMappingOps):
    @abstractmethod
    def new_full_mapping(self, key2value):
        raise NotImplementedError
    @abstractmethod
    def new_full_mapping_from_factory(self, value_factory):
        raise NotImplementedError

    @abstractmethod
    def at(self, fm, key): # -> Value
        raise NotImplementedError
    @abstractmethod
    def overwrite_at(self, fm, key, value):
        raise NotImplementedError
    @abstractmethod
    def iter_full_items(self, fm): # -> Iter (Key, Value)
        raise NotImplementedError

class IPartialMappingOps(ICommonMappingOps):
    @abstractmethod
    def new_partial_mapping(self, key2value=None):
        raise NotImplementedError
    @abstractmethod
    def new_partial__mapping_from_factory(self, value_factory):
        raise NotImplementedError

    @abstractmethod
    def get(self, pm, key): # -> Maybe Value
        raise NotImplementedError
    @abstractmethod
    def get_Nothing(self, pm): # -> Nothing
        raise NotImplementedError

    @abstractmethod
    def iter_partial_items_filterout_all_Nothing(self, pm): # -> Iter (Key, Value)
        raise NotImplementedError
    @abstractmethod
    def iter_partial_items_filterout_some_Nothing(self, pm): # -> Iter (Key, Maybe Value)
        raise NotImplementedError
    @abstractmethod
    def iter_partial_values_filterout_all_Nothing(self, pm): # -> Iter Value
        raise NotImplementedError
    @abstractmethod
    def iter_partial_values_filterout_some_Nothing(self, pm): # -> Iter (Maybe Value)
        raise NotImplementedError
    @abstractmethod
    def iter_partial_keys_filterout_all_Nothing(self, pm): # -> Iter Key
        raise NotImplementedError
        # O(full_size)
    @abstractmethod
    def iter_partial_keys_filterout_some_Nothing(self, pm): # -> Iter Key
        raise NotImplementedError
        # O(full_size)
    @abstractmethod
    def iter_full_may_items(self, pm): # -> Iter (Key, Maybe Value)
        # O(full_size)
        raise NotImplementedError

    @abstractmethod
    def partial_size_filterout_all_Nothing(self, pm): # -> UInt
        # O(full_size)
        raise NotImplementedError
    @abstractmethod
    def unstable_partial_size_upper_bound(self, pm): # -> UInt
        # O(1)
        # default to full_size(pm)
        # not the same as len(iter_partial_keys_filterout_some_Nothing(pm))
        raise NotImplementedError

    @abstractmethod
    def modify_item(self, pm, key, maybe_val):
        raise NotImplementedError
    @abstractmethod
    def clear(self, pm):
        raise NotImplementedError

class IKnownPartialSize(IPartialMappingOps):
    @abstractmethod
    def exact_partial_size(self, pm): # <==> partial_size_filterout_all_Nothing(pm)
        # O(1)
        raise NotImplementedError
class IKnownPartialKeys(IPartialMappingOps):
    @abstractmethod
    def iter_partial_items(self, pm):
        raise NotImplementedError
    @abstractmethod
    def iter_partial_values(self, pm):
        raise NotImplementedError
    @abstractmethod
    def iter_partial_keys(self, pm): # <==> iter_partial_keys_filterout_all_Nothing(pm)
        # O(exact_partial_size)
        # maynot know partial_size; e.g. double_linked_list
        raise NotImplementedError


###################
class PartialMappingOps2FullMappingOps(IFullMappingOps):
    # PartialMapping<Key, Val> -> FullMapping<Key, Value = Maybe Val>

    def __init__(self, partial_mapping_ops):
        self.partial_mapping_ops = partial_mapping_ops
    def iter_full_keys(self): # -> Iter Key
        return self.partial_mapping_ops.iter_full_keys()
    def full_size(self): # -> UInt
        return self.partial_mapping_ops.full_size()

    ### pm is fm now
    def new_full_mapping(self, key2value):
        return self.partial_mapping_ops.new_partial_mapping(key2value)
    def new_full_mapping_from_factory(self, value_factory):
        return self.partial_mapping_ops.new_partial__mapping_from_factory(value_factory)

    def at(self, fm, key): # -> Value
        # pm = fm
        return self.partial_mapping_ops.get(fm, key)
    def overwrite_at(self, fm, key, value):
        return self.partial_mapping_ops.modify_item(fm, key, value)
    def iter_full_items(self, fm): # -> Iter (Key, Value)
        return self.partial_mapping_ops.iter_full_may_items(fm)

PartialMappingOps2FullMappingOps(object())

