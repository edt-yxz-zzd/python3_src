
__all__ = '''
    IHeapOps__with_IWrappedObjectOps
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from .IHeapOps import IHeapOps
from .IWrappedObjectOps import IWrappedObjectOps

class IHeapOps__with_IWrappedObjectOps(IHeapOps):
    '''

provide below methods for IHeapOps:
    wrap
    unwrap
    wrapped_obj2key
'''
    __slots__ = ()
    #################
    @not_implemented
    def get_wrapped_obj_ops(ops):
        # -> IWrappedObjectOps
        raise NotImplementedError

    #################
    @override
    def wrap(ops, unwrapped_obj, maybe_inner_pointer):
        # unwrapped_obj -> Maybe InnerPointer -> wrapped_obj
        return ops.get_wrapped_obj_ops().wrap(unwrapped_obj, maybe_inner_pointer)
    @override
    def unwrap(ops, wrapped_obj):
        # wrapped_obj -> unwrapped_obj
        return ops.get_wrapped_obj_ops().unwrap(wrapped_obj)
    @override
    def wrapped_obj2key(ops, wrapped_obj):
        # wrapped_obj -> key
        return ops.get_wrapped_obj_ops().wrapped_obj2key(wrapped_obj)





if __name__ == '__main__':
    XXX = IHeapOps__with_IWrappedObjectOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)


