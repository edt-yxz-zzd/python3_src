

__all__ = '''
    INamedHeapOps__from_iterable
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from .INamedHeapOps import INamedHeapOps



class INamedHeapOps__from_iterable(INamedHeapOps):
    '''
'''
    __slots__ = ()
    #################

    @not_implemented
    def make_heap_from_iterable(ops, iter_unwrapped_objs):
        # Iter (name, key, payload) -> Heap
        raise NotImplementedError


if __name__ == '__main__':
    XXX = INamedHeapOps__from_iterable

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)



