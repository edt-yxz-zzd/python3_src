

__all__ = '''
    INFAOps
    '''.split()

from .abc import override, not_implemented
from .IFAOps import IFAOps
from itertools import chain

class INFAOps(IFAOps):
    # NFA
    # see: INFAOps__with_astate_dict.search_leftmost_substring_ex_ex
    # see: INFAOps__with_astate_dict._nstate2cnstate_
    #
    __slots__ = ()


    @not_implemented
    def _feed_astate2nstate_(ops, self, astate, terminal):
        # -> new_nstate
        # not consider null transition after input astate and output astates
        ...
    @not_implemented
    def _null_transition_of_astate_(ops, self, astate):
        # -> nstate # may not include the input astate
        # result neednot be cnstate
        ...
    @not_implemented
    def nstate2iter_astates(ops, self, nstate):
        # -> Iter astate
        ...
    @not_implemented
    def make_nstate_from_astates(ops, self, astates):
        ...

    @not_implemented
    def _nstate2cnstate_(ops, self, nstate):
        # -> new_cnstate
        # see: INFAOps__with_astate_dict._nstate2cnstate_
        # nstate is subset of new_cnstate
        ...
    '''
    (astate -> cnstate) is useless

    def astate2cnstate(ops, self, nstate):
    def _feed_astate2cnstate_(ops, self, astate, terminal)
    '''

    def nstate2cnstate(ops, self, nstate):
        return ops._nstate2cnstate_(self, nstate)

    @override
    def cstate2iter_astates(ops, self, cstate):
        return ops.nstate2iter_astates(self, cstate)



    @override
    def is_a_global_final_cstate__relax(ops, self, cstate):
        return ops.is_a_global_final_nstate__relax(self, cstate)
    def is_a_global_final_nstate__relax(ops, self, nstate):
        # see: is_a_global_final_astate__relax
        # for NFA.cnstate, any astate is is_a_global_final_astate__relax ==>> True
        is_global_final = ops.is_a_global_final_astate__relax
        return any(is_global_final(self, astate)
                    for astate in ops.nstate2iter_astates(self, nstate))
    @override
    def is_a_global_dead_cstate__relax(ops, self, cstate):
        return ops.is_a_global_dead_nstate__relax(self, cstate)
    def is_a_global_dead_nstate__relax(ops, self, nstate):
        # see: is_a_global_dead_astate__relax
        # for NFA.cnstate, all astates are is_a_global_dead_astate__relax ==>> True
        is_global_dead = ops.is_a_global_dead_astate__relax
        return all(is_global_dead(self, astate)
                    for astate in ops.nstate2iter_astates(self, nstate))

    @override
    def is_a_local_final_cstate(ops, self, cstate):
        return ops.is_a_local_final_nstate(self, cstate)
    def is_a_local_final_nstate(ops, self, cstate):
        # cstate = cnstate; cstate is a nstate
        is_a_local_final_astate = ops.is_a_local_final_astate
        return any(is_a_local_final_astate(self, astate)
                    for astate in ops.nstate2iter_astates(self, cstate))
    @override
    def is_a_local_dead_cstate(ops, self, cstate):
        return ops.is_a_local_dead_nstate(self, cstate)
    def is_a_local_dead_nstate(ops, self, cstate):
        # not final and no going out
        is_a_local_dead_astate = ops.is_a_local_dead_astate
        return all(is_a_local_dead_astate(self, astate)
                    for astate in ops.nstate2iter_astates(self, cstate))
    @override
    def _feed_(ops, self, cstate, terminal):
        # -> new_cstate
        _feed_astate2nstate_ = ops._feed_astate2nstate_
        nstate2iter_astates = ops.nstate2iter_astates
        make_nstate_from_astates = ops.make_nstate_from_astates
        nstate2cnstate = ops.nstate2cnstate

        nstates = (_feed_astate2nstate_(self, astate, terminal)
                    for astate in nstate2iter_astates(self, cstate))
        astates = chain.from_iterable(
                    nstate2iter_astates(self, nstate) for nstate in nstates)
        nstate = make_nstate_from_astates(self, astates)
        cnstate = nstate2cnstate(self, nstate)
        cstate = cnstate
        return cstate




if __name__ == '__main__':
    XXX = INFAOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)

