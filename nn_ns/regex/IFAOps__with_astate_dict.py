
__all__ = '''
    IFAOps__with_astate_dict
    '''.split()

from .abc import abstractmethod, not_implemented, override
from .IFAOps import IFAOps, IFAOps__succ_astates


class IFAOps__with_astate_dict(IFAOps):
    __slots__ = ()


    @not_implemented
    def make_astate_dict(ops, self, other_or_astate_value_pairs=None):
        # -> Map astate value
        ...
    @not_implemented
    def make_astate_set(ops, self, astates=None):
        # -> Set astate
        ...





if __name__ == '__main__':
    XXX = IFAOps__with_astate_dict

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)
