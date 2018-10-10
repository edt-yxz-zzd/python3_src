
INamedHeapOps

__all__ = ['INamedHeapOps']
from ..abc import abstractmethod, override, not_implemented
from .IHeapOps import IHeapOps

class WrappedObj:
    def __init__(self, unwrapped_obj, idx):
        self.__obj = unwrapped_obj
        self.idx = idx
    @property
    def unwrapped_obj(self):
        return self.__obj

class INamedHeapOps(IHeapOps):
    '''

data NamedHeap seq map name key payload =
        {idx2wrapped_obj :: seq wrapped_obj
        ,name2wrapped_obj :: map name wrapped_obj
        }
    where wrapped_obj = WrappedObj name key payload
data WrappedObj name key payload = (UnWrappedObj name key payload, mutable UInt)
data UnWrappedObj name key payload = (name, key, payload)

'''
    `wrap
        return WrappedObj(unwrapped_obj, idx)
    `unwrap
        return wrapped_obj.unwrapped_obj
    `wrapped_obj2key
        return wrapped_obj.unwrapped_obj[1]
    `can_be_parent_key_of

    ####
    `wrap_heap
        return view(heap[0], heap[1])

