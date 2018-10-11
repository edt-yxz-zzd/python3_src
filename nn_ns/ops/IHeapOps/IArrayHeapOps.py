
__all__ = '''
    IArrayHeapOps
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from .IHeapOps import IHeapOps

class IArrayHeapOps(IHeapOps):
    '''
    `wrap
    `unwrap
    `wrapped_obj2key
    `can_be_parent_key_of

    is_empty
    `get_size
    `verify_heap

    peek
    pop_then_push
    push_then_pop
    pop
    `push

    `make_unwrapped_obj_list
    `check_and_make_unwrapped_obj_list
    `make_array_heap_inplace
    `peek_at
    `delete_at
    `replace_at
'''
    __slots__ = ()
    #################
    @not_implemented
    def make_unwrapped_obj_list(ops, heap):
        # -> [unwrapped_obj]
        raise NotImplementedError
    @not_implemented
    def check_and_make_unwrapped_obj_list(ops, heap):
        # -> ([unwrapped_obj]|raise ValueError)
        raise NotImplementedError
    #################

    @not_implemented
    def make_array_heap_inplace(ops, heap):
        '''heapify'''
        raise NotImplementedError


    @not_implemented
    def peek_at(ops, heap, idx, *, wrapped):
        # -> xobj
        raise NotImplementedError

    ##############

    @not_implemented
    def delete_at(ops, heap, idx, *, wrapped):
        # -> xobj
        raise NotImplementedError

    @not_implemented
    def replace_at(ops, heap, idx, xobj, *, wrapped:bool):
        # xobj = unwrapped_obj|wrapped_obj
        # -> new_idx
        raise NotImplementedError




if __name__ == '__main__':
    XXX = IArrayHeapOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)


