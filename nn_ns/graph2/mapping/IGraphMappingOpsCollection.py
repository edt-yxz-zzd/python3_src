
# TODO: __slots__ = ()

'''
see: "def - mapping.txt"
'''




__all__ = '''
    IGraphMappingOpsCollection
        IHasFullMappingOpsVertex
        IHasPartialMappingOpsVertex
            IHasBothMappingOpsVertex

        IHasFullMappingOpsAEdge
        IHasPartialMappingOpsAEdge
            IHasBothMappingOpsAEdge

        IHasFullMappingOpsHEdge
        IHasPartialMappingOpsHEdge
            IHasBothMappingOpsHEdge
    '''.split()

from abc import abstractmethod, ABC
#from ???.IMappingOps import IFullMappingOps, IPartialMappingOps


from .IGraphRelated import IGraphRelated



class IGraphMappingOpsCollection(IGraphRelated):
    # correspond to a graph
    # e.g. graph_ops.get_graph_mapping_ops_collection(g) -> IGraphMappingOpsCollection
    pass

'''
# XXX = Vertex | AEdge | HEdge | ...
class IHasFullMappingOpsXXX(IGraphMappingOpsCollection):
    @abstractmethod
    def get_full_mapping_ops_XXX():# -> IFullMappingOps<XXX,Value>
        raise NotImplementedError
class IHasPartialMappingOpsXXX(IGraphMappingOpsCollection):
    @abstractmethod
    def get_partial_mapping_ops_XXX():# -> PartialMappingOps<XXX,Value>
        raise NotImplementedError
class IHasBothMappingOpsXXX(IHasPartialMappingOpsXXX, IHasFullMappingOpsXXX):
    pass
'''


######## Vertex #########
class IHasFullMappingOpsVertex(IGraphMappingOpsCollection):
    @abstractmethod
    def get_full_mapping_ops_Vertex():# -> IFullMappingOps<Vertex,Value>
        raise NotImplementedError
class IHasPartialMappingOpsVertex(IGraphMappingOpsCollection):
    @abstractmethod
    def get_partial_mapping_ops_Vertex():# -> PartialMappingOps<Vertex,Value>
        raise NotImplementedError
class IHasBothMappingOpsVertex(IHasPartialMappingOpsVertex, IHasFullMappingOpsVertex):
    pass

######## AEdge #########
class IHasFullMappingOpsAEdge(IGraphMappingOpsCollection):
    @abstractmethod
    def get_full_mapping_ops_AEdge():# -> IFullMappingOps<AEdge,Value>
        raise NotImplementedError
class IHasPartialMappingOpsAEdge(IGraphMappingOpsCollection):
    @abstractmethod
    def get_partial_mapping_ops_AEdge():# -> PartialMappingOps<AEdge,Value>
        raise NotImplementedError
class IHasBothMappingOpsAEdge(IHasPartialMappingOpsAEdge, IHasFullMappingOpsAEdge):
    pass

######## HEdge #########
class IHasFullMappingOpsHEdge(IGraphMappingOpsCollection):
    @abstractmethod
    def get_full_mapping_ops_HEdge():# -> IFullMappingOps<HEdge,Value>
        raise NotImplementedError
class IHasPartialMappingOpsHEdge(IGraphMappingOpsCollection):
    @abstractmethod
    def get_partial_mapping_ops_HEdge():# -> PartialMappingOps<HEdge,Value>
        raise NotImplementedError
class IHasBothMappingOpsHEdge(IHasPartialMappingOpsHEdge, IHasFullMappingOpsHEdge):
    pass




