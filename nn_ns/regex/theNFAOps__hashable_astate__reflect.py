
__all__ = '''
    theNFAOps__hashable_astate__reflect

    NFAOps__hashable_astate__reflect
    '''.split()


from .abc import abstractmethod, not_implemented, override
from .IFAOps__hashable_astate import IFAOps__hashable_astate
from .INFAOps__with_astate_dict import INFAOps__with_astate_dict
class NFAOps__hashable_astate__reflect(
        INFAOps__with_astate_dict
        , IFAOps__hashable_astate):
    __slots__ = ()

    @override
    def get_args_for_eq_hash(ops):
        return ()
    @override
    def _feed_astate2nstate_(ops, self, astate, terminal):
        return self._feed_astate2nstate_(astate, terminal)
    @override
    def _null_transition_of_astate_(ops, self, astate):
        return self._null_transition_of_astate_(astate)
    @override
    def is_a_local_dead_astate(ops, self, astate):
        return self.is_a_local_dead_astate(astate)

    @override
    def is_a_global_dead_astate__relax(ops, self, astate):
        return self.is_a_global_dead_astate__relax(astate)
    @override
    def get_the_initial_cstate(ops, self):
        return self.get_the_initial_cstate()
    @override
    def is_a_global_final_astate__relax(ops, self, astate):
        return self.is_a_global_final_astate__relax(astate)
    @override
    def is_a_local_final_astate(ops, self, astate):
        return self.is_a_local_final_astate(astate)
    @override
    def make_nstate_from_astates(ops, self, astates):
        return self.make_nstate_from_astates(astates)
    @override
    def nstate2iter_astates(ops, self, nstate):
        return self.nstate2iter_astates(nstate)
theNFAOps__hashable_astate__reflect = NFAOps__hashable_astate__reflect()


