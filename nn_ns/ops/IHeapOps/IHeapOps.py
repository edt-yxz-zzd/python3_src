


__all__ = '''
    IHeapOps
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from ..IOps import IOps



class IHeapOps(IOps):
    '''

    `wrap
    `unwrap
    `wrapped_obj2key
    `can_be_parent_key_of

    `is_empty
    `get_size
    `verify_heap
    `check_heap

    `xobj2wrapped_obj
    `wrapped_obj2xobj
    `peek

    `pop_then_push
    `push_then_pop
    `pop
    `push

'''
    __slots__ = ()
    #################
    @not_implemented
    def wrap(ops, unwrapped_obj, maybe_inner_pointer):
        # unwrapped_obj -> Maybe InnerPointer -> wrapped_obj
        # echo
        raise NotImplementedError
        wrapped_obj = unwrapped_obj
        return wrapped_obj
    @not_implemented
    def unwrap(ops, wrapped_obj):
        # wrapped_obj -> unwrapped_obj
        # echo
        raise NotImplementedError
        unwrapped_obj = wrapped_obj
        return unwrapped_obj
    @not_implemented
    def wrapped_obj2key(ops, wrapped_obj):
        # wrapped_obj -> key
        # echo
        raise NotImplementedError
        key = wrapped_obj
        return key
    @not_implemented
    def can_be_parent_key_of(ops, parent_wrapped_key, child_wrapped_key):
        # key -> key -> Bool
        # __le__
        raise NotImplementedError
        return parent_wrapped_key <= child_wrapped_key


    #################
    @not_implemented
    def is_empty(ops, heap):
        # -> bool
        raise NotImplementedError
    @not_implemented
    def get_size(ops, heap):
        # -> UInt
        raise NotImplementedError

    @not_implemented
    def verify_heap(ops, heap):
        # -> bool
        # True if OK
        raise NotImplementedError
    @not_implemented
    def check_heap(ops, heap):
        # -> (None|raise ValueError)
        raise NotImplementedError

    ################

    @not_implemented
    def xobj2wrapped_obj(ops, xobj, maybe_inner_pointer, *, wrapped):
        # -> wrapped_obj
        raise NotImplementedError

    @not_implemented
    def wrapped_obj2xobj(ops, wrapped_obj, *, wrapped):
        # -> xobj
        raise NotImplementedError

    @not_implemented
    def peek(ops, heap, *, wrapped):
        # -> xobj
        raise NotImplementedError

    ####################

    @not_implemented
    def pop_then_push(ops, heap, xobj, *, wrapped):
        # -> xobj
        raise NotImplementedError

    @not_implemented
    def push_then_pop(ops, heap, xobj, *, wrapped):
        # -> xobj
        raise NotImplementedError

    #################

    @not_implemented
    def pop(ops, heap, *, wrapped):
        # -> xobj
        raise NotImplementedError

    @not_implemented
    def push(ops, heap, xobj, *, wrapped):
        # -> new_inner_pointer
        raise NotImplementedError

if __name__ == '__main__':
    XXX = IHeapOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)


