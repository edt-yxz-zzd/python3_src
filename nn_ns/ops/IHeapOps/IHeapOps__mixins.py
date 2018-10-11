
__all__ = '''
    IHeapOps__mixins
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from .IHeapOps import IHeapOps

class IHeapOps__mixins(IHeapOps):
    '''

    is_empty
    verify_heap
    xobj2wrapped_obj
    wrapped_obj2xobj
    push_then_pop
'''
    __slots__ = ()
    #################
    @override
    def is_empty(ops, heap):
        # -> bool
        return not ops.get_size(heap)
    @override
    def verify_heap(ops, heap):
        # -> Bool
        # True if OK
        try:
            ops.check_heap(heap)
        except ValueError:
            return False
        return True


    @override
    def xobj2wrapped_obj(ops, xobj, maybe_inner_pointer, *, wrapped):
        # -> wrapped_obj
        if wrapped:
            wrapped_obj = xobj
        else:
            unwrapped_obj = xobj
            wrapped_obj = ops.wrap(unwrapped_obj, maybe_inner_pointer)
        return wrapped_obj
    @override
    def wrapped_obj2xobj(ops, wrapped_obj, *, wrapped):
        # -> xobj
        if wrapped:
            xobj = wrapped_obj
        else:
            unwrapped_obj = ops.unwrap(wrapped_obj)
            xobj = unwrapped_obj
        return xobj

    @override
    def push_then_pop(ops, heap, xobj, *, wrapped):
        # -> xobj
        input_xobj = xobj; del xobj
        if ops.is_empty(heap):
            return input_xobj

        head_wrapped_obj = ops.peek(heap, wrapped=True)
        input_wrapped_obj = ops.xobj2wrapped_obj(input_xobj, 0, wrapped=wrapped)

        head_key = ops.wrapped_obj2key(head_wrapped_obj)
        input_key = ops.wrapped_obj2key(input_wrapped_obj)
        if ops.can_be_parent_key_of(input_key, head_key):
            return input_xobj

        head_xobj = ops.pop_then_push(heap, input_xobj, wrapped=wrapped)
        return head_xobj


if __name__ == '__main__':
    XXX = IHeapOps__mixins

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)


