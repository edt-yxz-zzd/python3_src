

__all__ = '''
    IGraphOps
    IGraphOps_HasMappingOpsCollection
    '''.split()

from abc import abstractmethod, ABC
from .IGraphRelated import IGraphRelated
#from ???.IGraphMappingOpsCollection import IGraphMappingOpsCollection



class IGraphOps(IGraphRelated):pass
class IGraphOps_HasMappingOpsCollection(IGraphOps):
    @abstractmethod
    def get_graph_mapping_ops_collection(g):# -> IGraphMappingOpsCollection
        raise NotImplementedError


