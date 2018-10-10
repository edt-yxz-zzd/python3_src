
__all__ = ['IKnownFullKeysMappingOps']
from .abc import abstractmethod, ABC
from .IMappingOps import IMappingOps

class IKnownFullKeysMappingOps(IMappingOps):
    @abstractmethod
    def iter_full_keys(self): # -> Iter Key
        raise NotImplementedError
    @abstractmethod
    def full_size(self): # -> UInt
        raise NotImplementedError

