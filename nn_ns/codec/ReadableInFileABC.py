

__all__ = ['ReadableInFileABC']
from abc import ABCMeta, abstractmethod

#sized_file = stack_rng, heap_rng_set, file

class ReadableInFileABC(ABCMeta):
    '''assume:
    1) forward reading if peek_size > 0 else backward reading;
    2) one compact stack bytes block and some heap data
'''
    @abstractmethod
    def read(self, sized_file):
        'file->data_obj'
        raise NotImplementedError
    @abstractmethod
    def read_stack(self, sized_file):
        'file->stack_struct_bytes (not include data in heap)'
        raise NotImplementedError
    @abstractmethod
    def parse_stack(self, sized_file):
        'stack_struct_bytes->stack_struct_obj (not include data in heap)'
        raise NotImplementedError
    @abstractmethod
    def skip(self, sized_file):
        raise NotImplementedError
    @abstractmethod
    def peek_size(self, sized_file):
        '''size in stack (not include size in heap)

if sized_file is None, return fixed_size or None'''
        raise NotImplementedError











