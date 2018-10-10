

__all__ = ['IUserHeapOps']
from ..abc import abstractmethod, override, not_implemented
from .IHeapOps import IHeapOps

class IUserHeapOps(IHeapOps):
    '''


new_methods:
    `get_user_heap_ops

'''
    __slots__ = ()
    ###########################
    @not_implemented
    def get_user_heap_ops(ops):
        # -> IHeapOps
        raise NotImplementedError

    ###########################
    @override
    def wrap(ops, unwrapped_obj, idx):
        # unwrapped_obj -> UInt -> wrapped_obj
        return ops.get_user_heap_ops().wrap(unwrapped_obj, idx)
    @override
    def unwrap(ops, wrapped_obj):
        # wrapped_obj -> unwrapped_obj
        return ops.get_user_heap_ops().unwrap(wrapped_obj)
    @override
    def wrapped_obj2key(ops, wrapped_obj):
        # wrapped_obj -> key
        return ops.get_user_heap_ops().wrapped_obj2key(wrapped_obj)
    @override
    def can_be_parent_key_of(ops, parent_wrapped_key, child_wrapped_key):
        # key -> key -> Bool
        return ops.get_user_heap_ops().can_be_parent_key_of(parent_wrapped_key, child_wrapped_key)

    #################
    #################
    #################
    #################
    def is_empty(ops, heap):
        # -> bool
        return ops.get_user_heap_ops().is_empty(heap)
    def get_size(ops, heap):
        # -> UInt
        return ops.get_user_heap_ops().get_size(heap)

    ################

    def make_heap_inplace(ops, heap):
        '''heapify'''
        return ops.get_user_heap_ops().make_heap_inplace(heap)

    def replace_at(ops, heap, idx, xobj, *, wrapped:bool):
        # xobj = unwrapped_obj|wrapped_obj
        # -> new_idx
        return ops.get_user_heap_ops().replace_at(heap, idx, xobj, wrapped=wrapped)


    ##############

    def pop_then_push(ops, heap, xobj, *, wrapped):
        # -> xobj
        return ops.get_user_heap_ops().pop_then_push(heap, xobj, wrapped=wrapped)

    def push_then_pop(ops, heap, xobj, *, wrapped):
        # -> xobj
        return ops.get_user_heap_ops().push_then_pop(heap, xobj, wrapped=wrapped)

    #################

    def pop(ops, heap, *, wrapped):
        # -> xobj
        return ops.get_user_heap_ops().pop(heap, wrapped=wrapped)

    def push(ops, heap, xobj, *, wrapped):
        return ops.get_user_heap_ops().push(heap, xobj, wrapped=wrapped)

    ###############

    def delete_at(ops, heap, idx, *, wrapped):
        # -> xobj
        return ops.get_user_heap_ops().delete_at(heap, idx, wrapped=wrapped)


if __name__ == '__main__':
    XXX = IUserHeapOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)


