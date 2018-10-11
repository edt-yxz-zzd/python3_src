

__all__ = '''
    IWrappedObjectOps
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from ..IOps import IOps


class IWrappedObjectOps(IOps):
    '''

provide below methods for IHeapOps:
    `wrap
    `unwrap
    `wrapped_obj2key
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



if __name__ == '__main__':
    XXX = IWrappedObjectOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)


