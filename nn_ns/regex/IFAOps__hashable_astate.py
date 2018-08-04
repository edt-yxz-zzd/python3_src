
__all__ = '''
    IFAOps__hashable_astate
    '''.split()

from .abc import abstractmethod, not_implemented, override
from .OtherOps.EqOps import python_eq_key_ops
from .IFAOps__with_astate_dict import IFAOps__with_astate_dict

class IFAOps__hashable_astate(IFAOps__with_astate_dict):
    __slots__ = ()

    @override
    def get_eq_astate_ops(ops, self):
        # -> IEqOps
        return python_eq_key_ops

    @override
    def astate_eq(ops, self, lhs_astate, rhs_astate):
        return lhs_astate == rhs_astate

    @override
    def make_astate_dict(ops, self, other_or_astate_value_pairs=None):
        if other_or_astate_value_pairs is None:
            return {}
        return dict(other_or_astate_value_pairs)
    @override
    def make_astate_set(ops, self, astates=None):
        if astates is None:
            return set()
        return set(astates)

if __name__ == '__main__':
    XXX = IFAOps__hashable_astate

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)
