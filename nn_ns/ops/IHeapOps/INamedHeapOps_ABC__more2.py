

__all__ = '''
    INamedHeapOps_ABC__more2
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from .INamedHeapOps_ABC__more1 import INamedHeapOps_ABC__more1





class INamedHeapOps_ABC__more2(INamedHeapOps_ABC__more1):
    '''

heap = (idx2wrapped_obj, name2wrapped_obj)
'''
    __slots__ = ()
    ####################
    @override
    def make_heap_from_parts(ops, idx2wrapped_obj, name2wrapped_obj):
        # -> heap
        #idx2wrapped_obj is wrapped_obj_seq
        assert len(name2wrapped_obj) == len(idx2wrapped_obj)
        heap = (idx2wrapped_obj, name2wrapped_obj)
        return heap
    @override
    def get_idx2wrapped_obj(ops, heap):
        # heap -> wrapped_obj_seq
        return heap[0]
    @override
    def get_name2wrapped_obj(ops, heap):
        # heap -> Map name wrapped_obj
        return heap[1]


if __name__ == '__main__':
    XXX = INamedHeapOps_ABC__more2

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)


