
__all__ = '''
    ISimpleNFA
    MakeNewAState
    '''.split()

from .abc import ABC, abstractmethod, not_implemented, override
from ..theNFAOps__hashable_astate__reflect import \
    theNFAOps__hashable_astate__reflect as _ops

class MakeNewAState:
    __slots__ = 'new_astate'.split()
    def __init__(self):
        self.new_astate = 0
    def __call__(self):
        new_astate = self.new_astate
        self.new_astate += 1
        return new_astate

class ISimpleNFA(ABC):
    '''

see:
    mkSimpleNFA
    SimpleNFA.py
    SimpleRE.py
    example_Simple.py

terminal_set
    .__contains__
    but not require .__bool__
    why?
        terminal_set may be implement by a predicator
        we donot know whether it contains any value


ISimpleNFA terminal_set
    # Thompson's construction
    = DeadNFA initial_astate final_astate
    | NullNFA initial_astate final_astate
    | SinglePassNFA initial_astate final_astate
    | SingleNotNFA initial_astate final_astate
            terminal_set
    | SingleNFA initial_astate final_astate
            terminal_set
    | ConcatenationNFA initial_astate final_astate
            (SingleNFA terminal_set) (SingleNFA terminal_set)
    | AlternationNFA initial_astate final_astate
            (SingleNFA terminal_set) (SingleNFA terminal_set)
    | OneOrMoreNFA initial_astate final_astate
            (SingleNFA terminal_set)


assume astate is not None
assume astate is UInt
make_new_astate :: () -> new_astate


abstract_methods:
    see: theNFAOps__hashable_astate__reflect
    to s.t. IFAOps__hashable_astate, INFAOps__with_astate_dict
        `_feed_astate2nstate_
        `_null_transition_of_astate_
        `is_a_local_dead_astate

        `get_args_for_eq_hash
        `get_the_initial_cstate
        `is_a_global_dead_astate__relax
        `is_a_global_final_astate__relax
        `is_a_local_final_astate
        `make_nstate_from_astates
        `nstate2iter_astates
'''
    __slots__ = 'initial_astate final_astate _next_new_astate'.split()
    def __init__(self, make_new_astate, initial_astate, final_astate):
        '''
input:
    initial_astate :: None | astate
    final_astate :: None | astate
    make_new_astate :: MakeNewAState
        .__call__ :: () -> new_astate
        .new_astate :: UInt # next astate
'''
        if initial_astate is None:
            initial_astate = make_new_astate()
        if final_astate is None:
            final_astate = make_new_astate()
        self.initial_astate = initial_astate
        self.final_astate = final_astate

    NFA_ops = _ops
    def get_NFA_ops(self):
        # -> INFAOps
        return _ops

    def get_the_initial_cstate(self):
        return _ops.nstate2cnstate(self, frozenset([self.initial_astate]))
    def is_a_global_final_astate__relax(self, astate):
        # only one final_astate and it has not outgoing
        return False
    def is_a_local_final_astate(self, astate):
        return self.final_astate == astate
    def make_nstate_from_astates(self, astates):
        return frozenset(astates)
    def nstate2iter_astates(self, nstate):
        return iter(nstate)

    @not_implemented
    def _feed_astate2nstate_(self, astate, terminal):
        # -> new_nstate
        # not consider null transition after input astate and output astates
        ...
    @not_implemented
    def _null_transition_of_astate_(self, astate):
        # -> nstate # may not include the input astate
        # result neednot be cnstate
        ...
    @not_implemented
    def is_a_local_dead_astate(self, astate):
        # no going out, not consider null transition
        # may be final
        # so, if initial_astate -[null]-> other_astates
        #       then initial_astate is a dead initial_astate
        #   user should use is_a_local_dead_cstate
        #   or user should test is_a_local_final_astate before is_a_local_dead_astate
        ...


    def is_a_global_dead_astate__relax(self, astate):
        # global_dead
        # relax means:
        #   when return False: the input astate may be indeed global dead
        #
        # if not final and local dead, must return True
        #
        return (not self.is_a_local_final_astate(astate)
            and self.is_a_local_dead_astate(astate)
            )

    @not_implemented
    def show(self, show_terminal_set, more=None):
        # -> str
        # show_terminal_set :: terminal_set -> str
        # more :: None | (self, str) -> str
        ...
    def show_detail(self, show_terminal_set):
        def more(self, s):
            return '{{>-{}}}-> {} ->{{{}->}}'.format(
                    self.initial_astate, s, self.final_astate)
        return self.show(show_terminal_set, more)


if __name__ == '__main__':
    XXX = ISimpleNFA

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)


