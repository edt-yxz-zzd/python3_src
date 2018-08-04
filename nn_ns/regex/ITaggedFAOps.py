
__all__ = '''
    ITaggedFAOps
    '''.split()

from .abc import abstractmethod, not_implemented, override
from .IFAOps import IFAOps


class ITaggedFAOps(IFAOps):
    '''
tagged_cstate
    NFA.tagged_cstate = Map astate tag
    DFA.tagged_cstate = tagged_astate
tagged_astate = (astate, tag)
'''
    __slots__ = ()

    @not_implemented
    def _tagged_feed_(ops, self, tagged_cstate, terminal
            , high_level_position:'UInt'
            , low_level_reference:'opaque data'):
        # -> new_tagged_cstate
        # low_level_reference can be anything
        #   ops may store it into the result tagged_cstate
        #       , but do not check type or read it or modify it
        ...
    def tagged_feed(ops, self, tagged_cstate, terminal
            , high_level_position:'UInt'
            , low_level_reference:'opaque data'):
        # -> (high_level_position+1, new_tagged_cstate)
        assert high_level_position >= 0
        new_tagged_cstate = ops._tagged_feed_(self, tagged_cstate, terminal
                    , high_level_position, low_level_reference)
        return high_level_position+1, new_tagged_cstate

if __name__ == '__main__':
    XXX = ITaggedFAOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)
