

__all__ = '''
    IArrayHeapOps__mixins
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from .IArrayHeapOps import IArrayHeapOps
from .IHeapOps__mixins import IHeapOps__mixins


class IArrayHeapOps__mixins(IHeapOps__mixins, IArrayHeapOps):
    '''

make_unwrapped_obj_list
check_and_make_unwrapped_obj_list
peek
pop_then_push
pop
'''
    __slots__ = ()
    #################
    @override
    def make_unwrapped_obj_list(ops, heap):
        # -> [unwrapped_obj]
        L = ops.get_size(heap)
        return [ops.peek_at(heap, i, wrapped=False) for i in range(L)]
    @override
    def check_and_make_unwrapped_obj_list(ops, heap):
        # -> ([unwrapped_obj]|raise ValueError)
        ops.check_heap(heap)
        return ops.make_unwrapped_obj_list(heap)
    ##############

    @override
    def peek(ops, heap, *, wrapped):
        # -> xobj
        return ops.peek_at(heap, 0, wrapped=wrapped)

    @override
    def pop_then_push(ops, heap, xobj, *, wrapped):
        # -> xobj
        result_xobj = ops.peek_at(heap, 0, wrapped=wrapped)
        ops.replace_at(heap, 0, xobj, wrapped=wrapped)
        return result_xobj

    @override
    def pop(ops, heap, *, wrapped):
        # -> xobj
        return ops.delete_at(heap, 0, wrapped=wrapped)


if __name__ == '__main__':
    XXX = IArrayHeapOps__mixins

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)



