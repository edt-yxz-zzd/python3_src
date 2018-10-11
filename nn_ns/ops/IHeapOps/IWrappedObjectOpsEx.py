

__all__ = '''
    IWrappedObjectOpsEx
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from .IWrappedObjectOps import IWrappedObjectOps


class IWrappedObjectOpsEx(IWrappedObjectOps):
    '''

provide below methods for INamedHeapOps_ABC.InnerArrayHeapOps:
    `wrap
    `unwrap
    `wrapped_obj2key
    `get_inner_pointer_of_wrapped_obj
    `set_inner_pointer_of_wrapped_obj
    `can_be_parent_key_of
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
    def set_inner_pointer_of_wrapped_obj(ops, wrapped_obj, inner_pointer):
        # -> None
        raise NotImplementedError
    @not_implemented
    def get_inner_pointer_of_wrapped_obj(ops, wrapped_obj):
        # -> inner_pointer
        raise NotImplementedError

    @not_implemented
    def can_be_parent_key_of(ops, parent_wrapped_key, child_wrapped_key):
        # key -> key -> Bool
        # __le__
        raise NotImplementedError
        return parent_wrapped_key <= child_wrapped_key

if __name__ == '__main__':
    XXX = IWrappedObjectOpsEx

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)


