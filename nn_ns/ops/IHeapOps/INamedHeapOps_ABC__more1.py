

__all__ = '''
    INamedHeapOps_ABC__more1
    WrappedObj
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from .INamedHeapOps_ABC import INamedHeapOps_ABC




class WrappedObj:
    def __init__(self, unwrapped_obj, idx):
        self.__obj = unwrapped_obj
        self.idx = idx
    @property
    def unwrapped_obj(self):
        return self.__obj


class INamedHeapOps_ABC__more1(INamedHeapOps_ABC):
    '''

wrapped_obj :: WrappedObj
'''
    __slots__ = ()
    ####################

    @override
    def wrap(ops, unwrapped_obj, idx):
        return WrappedObj(unwrapped_obj, idx)
    @override
    def unwrap(ops, wrapped_obj:WrappedObj):
        return wrapped_obj.unwrapped_obj
    @override
    def set_idx_of_wrapped_obj(ops, wrapped_obj, idx):
        wrapped_obj.idx = idx
    @override
    def get_idx_of_wrapped_obj(ops, wrapped_obj, idx):
        return wrapped_obj.idx



if __name__ == '__main__':
    XXX = INamedHeapOps_ABC__more1

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)


