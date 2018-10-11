

__all__ = '''
    PlainNamedMinHeapOps
    thePlainNamedMinHeapOps
    '''.split()

from ..abc import abstractmethod, override, not_implemented
from .INamedHeapOps_ABC__more2 import INamedHeapOps_ABC__more2



class PlainNamedMinHeapOps(INamedHeapOps_ABC__more2):
    '''
'''
    __slots__ = ()
    #################
    @override
    def can_be_parent_key_of(ops, parent_wrapped_key, child_wrapped_key):
        # key -> key -> Bool
        # __le__
        return parent_wrapped_key <= child_wrapped_key
    @override
    def make_new_name_dict(ops):
        # -> Map name v
        return {}
    @override
    def __eq__(ops, other):
        return type(ops) is type(other)
    @override
    def __hash__(ops):
        return (type(ops),)

thePlainNamedMinHeapOps = PlainNamedMinHeapOps()


if __name__ == '__main__':
    XXX = PlainNamedMinHeapOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)



