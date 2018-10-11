

__all__ = ['IUserArrayHeapOps']
from ..abc import abstractmethod, override, not_implemented
from .IArrayHeapOps import IArrayHeapOps
from .IUserHeapOps import IUserHeapOps

# though IArrayHeapOps overrides some IHeapOps methods
#   IArrayHeapOps should be after IUserHeapOps
#   since IUserHeapOps overrides all IHeapOps methods
class IUserArrayHeapOps(IUserHeapOps, IArrayHeapOps):
    '''


new_methods:
    `get_user_array_heap_ops

'''
    __slots__ = ()
    ###########################
    @not_implemented
    def get_user_array_heap_ops(ops):
        # -> IArrayHeapOps
        raise NotImplementedError

    @override
    def get_user_heap_ops(ops):
        # -> IHeapOps
        return ops.get_user_array_heap_ops()
    ###########################
    ###########################

    @override
    def make_array_heap_inplace(ops, heap):
        '''heapify'''
        return ops.get_user_array_heap_ops().make_array_heap_inplace(heap)


    @override
    def peek_at(ops, heap, idx, *, wrapped):
        # -> xobj
        return ops.get_user_array_heap_ops().peek_at(heap, idx, wrapped=wrapped)

    ##############

    @override
    def delete_at(ops, heap, idx, *, wrapped):
        # -> xobj
        return ops.get_user_array_heap_ops().delete_at(heap, idx, wrapped=wrapped)

    @override
    def replace_at(ops, heap, idx, xobj, *, wrapped:bool):
        # xobj = unwrapped_obj|wrapped_obj
        # -> new_idx
        return ops.get_user_array_heap_ops().replace_at(heap, idx, xobj, wrapped=wrapped)


    ########### redirect to IUserHeapOps

    peek = IUserHeapOps.peek
    pop_then_push = IUserHeapOps.pop_then_push
    pop = IUserHeapOps.pop


if __name__ == '__main__':
    XXX = IUserArrayHeapOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)


