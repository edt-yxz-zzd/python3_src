

'''
search_leftmost_substring:
    # greedy, leftmost_end_first
    are these two cases have same result?:
        greedy=True, leftmost_end_first=True
        greedy=False, leftmost_end_first=False
    NO! see below example:
        search_leftmost_substring (S+A+|B+S+A+X+) in "BBBSSSAAAXXX"
            greedy leftmost_end_first   result
            True        False           (0, 12)
            False       False           (0, 10)
            True        True            (3, 7)
            False       True            (5, 7)
'''

__all__ = '''
    IFAOps
    IFAOps__succ_astates
    '''.split()

from .abc import abstractmethod, not_implemented, override
from .OtherOps.IOps import IOps
from .OtherOps.IEqOps import IEqOps
from .OtherOps.EqOps import python_eq_key_ops


SuccessOnNonGreedy                  = 'SuccessOnNonGreedy'
SuccessOnGlobalDead                 = 'SuccessOnGlobalDead'
SuccessOnGlobalFinal                = 'SuccessOnGlobalFinal'
SuccessUntilEnd                     = 'SuccessUntilEnd'

FailUntilEnd                        = 'FailUntilEnd'
FailOnGlobalDead                    = 'FailOnGlobalDead'
LeftMostEnd_GreedyBegin             = 'LeftMostEnd_GreedyBegin'
LeftMostEnd_NonGreedyBegin          = 'LeftMostEnd_NonGreedyBegin'
LeftMostBegin_NonGreedyEnd          = 'LeftMostBegin_NonGreedyEnd'
LeftMostBegin_ToWholeEnd            = 'LeftMostBegin_ToWholeEnd'
LeftMostBegin_SuccessUntilEnd       = 'LeftMostBegin_SuccessUntilEnd'
LeftMostBegin_SuccessOnGlobalDead   = 'LeftMostBegin_SuccessOnGlobalDead'
class IFAOps(IOps):
    '''
self :: FA
    ops donot modify self

cstate
    complete_state
    cstate should be immutable
        but user should not depend on this immutable property
        user may assume nstate is mutable, and donot use mutable operation
        # assume cstate = Seq astate
        # i.e. "seq += seq" is not allow
        #   seq may be mutable
        #   "seq = seq + seq" is OK
    NFA.cstate = cnstate
    DFA.cstate = astate
cnstate
    complete nstate # special nstate
    means apply any null transition can not alter cnstate
        but implement is allowed to first eval the true cnstate
            (closure under null_transitions)
            and then remove all global_dead_astate in cnstate
            i.e. cnstate may exclude global_dead_astates
        so, user should not test the closure property
nstate
    nondeterministic_state # NFA_state
    nstate = Set astate
    nstate should be immutable
        but user should not depend on this immutable property
        user may assume nstate is mutable, and donot use mutable operation
        # assume nstate = Seq astate
        # i.e. "seq += seq" is not allow
        #   seq may be mutable
        #   "seq = seq + seq" is OK
        # why?
        #   e.g. we convert DFA to NFA
        #       where DFA with astate_set
        #       but the astate_set is mutable
        #       we may use the mutable set to repr NFA.nstate
        #
    NFA.cstate = cnstate
astate
    atomic_state
    astate should be immutable
        ??? __eq__
    NFA.state = astate
    DFA.state = astate

tagged_cstate
    NFA.tagged_cstate = Map astate tag
    DFA.tagged_cstate = tagged_astate
tagged_astate = (astate, tag)


local_dead_astate
    local dead astate
    has_no_nonnull_outgoing_transitions
    not consider null transition
    no going out

    may be final # but implement are allowed to exclude final state
    not indicate fail since itself maybe final and null_transitions

    [local_dead_cstate and not final_cstate] indicate fail
        since all astates in it are local_dead and not final
global_dead_astate
    global dead astate
    global_dead
    not consider null transition at this level
    not final and all nonnull_outgoing_transitions' cstates(not astates/nstates) are global_dead
    not indicate fail since null_transitions
        but if in cstate, we can remove global_dead_astate in cstate
    [global_dead_cstate] indicate fail
        global_dead_cstate <==> all astates in it are global_dead
local_final_astate
    local final astate
    not consider null transition
    alias of "final"
    indicate local success, i.e. itself is OK

    [local_final_cstate] indicate local success
        local_final_cstate <==> any astate in it is local_final
global_final_astate
    global final astate
    global_final
    not consider null transition at this level
    final and for any terminal: at least one nonnull_outgoing_transition at terminal whose result cstate(not astate/nstate!) is global_final
        # very hard condition
    indicate global success, since later regex is equivalence to regex".*"

    [global_final_cstate] indicate global success
        global_final_cstate <==> any astate in it is global_final

pseudo_global_final_astate
    consider null_transition at this level
    exist null_transition* to global_final_astate

terminal
    e.g. byte/char/token
high_level_position :: UInt
    per terminal ==>> high_level_position += 1
    we cannot refer to the input terminal using high_level_position
low_level_reference :: opaque_data
    outer user may use low_level_reference can refer to the input terminal
    ops donot dereference low_level_reference, just store it if needed
highlow_position_pair = (high_level_position, low_level_reference)
'''
    __slots__ = ()


    @abstractmethod
    def get_eq_astate_ops(ops, self):
        # -> IEqOps
        return python_eq_key_ops

    @abstractmethod
    def astate_eq(ops, self, lhs_astate, rhs_astate):
        ops.get_eq_astate_ops(self).eq(lhs_astate, rhs_astate)
        return lhs_astate == rhs_astate

    @abstractmethod
    def is_a_global_final_astate__relax(ops, self, astate):
        # global_final
        # relax means:
        #   when return False: the input astate may be indeed global final
        #
        return False
    @abstractmethod
    def is_a_global_dead_astate__relax(ops, self, astate):
        # global_dead
        # relax means:
        #   when return False: the input astate may be indeed global dead
        #
        # if not final and local dead, must return True
        #
        return (not ops.is_a_local_final_astate(self, astate)
            and ops.is_a_local_dead_astate(self, astate)
            )

    @not_implemented
    def is_a_local_final_astate(ops, self, astate):
        ...
    @not_implemented
    def is_a_local_dead_astate(ops, self, astate):
        # no going out, not consider null transition
        # may be final
        # so, if initial_astate -[null]-> other_astates # all nulls
        #       then initial_astate is a dead initial_astate
        #   user should use is_a_local_dead_cstate
        #   or user should test is_a_local_final_astate before is_a_local_dead_astate
        ...

    @not_implemented
    def get_the_initial_cstate(ops, self:'FA'):
        # -> cstate
        ...
    @abstractmethod
    def is_a_global_final_cstate__relax(ops, self, cstate):
        # see: is_a_global_final_astate__relax
        # global_final
        # for NFA.cnstate, any astate is is_a_global_final_astate__relax ==>> True
        cstate2iter_astates = ops.cstate2iter_astates
        is_global_final = ops.is_a_global_final_astate__relax
        return any(is_global_final(self, astate)
                for astate in cstate2iter_astates(self, cstate))
    def is_a_global_dead_cstate__relax(ops, self, cstate):
        # see: is_a_global_dead_astate__relax
        # global_dead
        # for NFA.cnstate, all astates are is_a_global_dead_astate__relax ==>> True
        cstate2iter_astates = ops.cstate2iter_astates
        is_global_dead = ops.is_a_global_dead_astate__relax
        return all(is_global_dead(self, astate)
                for astate in cstate2iter_astates(self, cstate))

    @not_implemented
    def cstate2iter_astates(ops, self, cstate):
        # -> Iter astate
        ...

    @not_implemented
    def is_a_local_final_cstate(ops, self, cstate):
        ...
    @not_implemented
    def is_a_local_dead_cstate(ops, self, cstate):
        # no going out, may be final
        # normally, user should test is_a_local_final_cstate before is_a_local_dead_cstate
        ...
    @not_implemented
    def _feed_(ops, self, cstate, terminal):
        # -> new_cstate
        ...

    @not_implemented
    def search_leftmost_substring_ex_ex(ops, self
            , begin_low_level_reference
            , terminal_end_low_level_reference_pairs
            , greedy:bool
            , leftmost_end_first:bool):
        # -> (reason:str, may_result_ex, actual_access_end)
        #   may_result_ex = None | result_ex
        #   result_ex = (begin, end_ex)
        #   end_ex = ... | end
        #   begin = (high_begin, low_begin)
        #   end = (high_end, low_end)
        #   actual_access_end = (high_level_position_of_access_end
        #                       ,low_level_reference_of_access_end)
        #
        # if leftmost_end_first:
        #   leftmost_end take priority over leftmost_begin
        #   if greedy:
        #       1) find leftmost_end
        #       2) find leftmost_begin for the fixed leftmost_end
        #   else:
        #       1) find leftmost_end
        #       2) find rightmost_begin for the fixed leftmost_end
        # else:
        #   leftmost_begin take priority over leftmost_end
        #   if greedy:
        #       1) find leftmost_begin if it has an end
        #       2) find rightmost_end for the fixed leftmost_begin
        #   else:
        #       1) find leftmost_begin if it has an end
        #       2) find leftmost_end for the fixed leftmost_begin
        #
        #
        # longest if greedy else shortest
        #
        # new FA = (.*) ++ (?P<main>self)
        #
        # a concrete implement:
        #   see: INFAOps__with_astate_dict.search_leftmost_substring_ex_ex
        ...



    def feed(ops, self, cstate, terminal, high_level_position:'UInt'):
        # -> (high_level_position+1, new_cstate)
        assert high_level_position >= 0
        new_cstate = ops._feed_(self, cstate, terminal)
        return high_level_position+1, new_cstate
    def search_leftmost_substring(ops, self, terminals
            , greedy:bool, leftmost_end_first:bool):
        # -> None | (high_begin, ...) | (high_begin, high_end)
        #   high_begin, high_end :: UInt # high_level_position
        #   None for fail
        #   ... means the end of the whole input
        #
        # longest if greedy else shortest
        #
        # new FA = (.*) ++ (?P<main>self)
        #
        # search_leftmost_substring (S+A+|B+S+A+X+) in "BBBSSSAAAXXX"
        #   greedy leftmost_end_first   result
        #   True        False           (0, 12)
        #   False       False           (0, 10)
        #   True        True            (3, 7)
        #   False       True            (5, 7)
        #
        f = ops.search_leftmost_substring_ex
        pairs = ((terminal, None) for terminal in terminals)
        r = f(self, None, pairs, greedy, leftmost_end_first)
        may_result_ex, _ = r
        if may_result_ex is None:
            return None
        [(high_begin, _), end_ex] = may_result_ex
        if end_ex is ...:
            return high_begin, ...
        (high_end, _) = end_ex
        return high_begin, high_end
    def search_leftmost_substring_ex(ops, self
            , begin_low_level_reference
            , terminal_end_low_level_reference_pairs
            , greedy:bool
            , leftmost_end_first:bool):
        # -> (may_result_ex, actual_access_end)
        # see: search_leftmost_substring_ex_ex for:
        #   may_result_ex, actual_access_end
        #
        f = ops.search_leftmost_substring_ex_ex
        r = f(self
            , begin_low_level_reference
            , terminal_end_low_level_reference_pairs
            , greedy
            , leftmost_end_first
            )
        _, may_result_ex, actual_access_end = r
        return may_result_ex, actual_access_end




    def does_accept(ops, self, terminals):
        # -> does_accept:bool
        pairs = ((terminal, None) for terminal in terminals)
        reason, does_accept, _ = ops.does_accept_ex(self, None, pairs)
        return does_accept

    def does_accept_ex(ops, self
                        , begin_low_level_reference
                        , terminal_end_low_level_reference_pairs):
        # -> (reason, does_accept:bool, actual_access_end)
        #   actual_access_end = (high_level_position_of_access_end
        #                       ,low_level_reference_of_access_end)
        #   if does_accept:
        #       high_level_position is
        #           * the len of terminal_end_low_level_reference_pairs
        #           * or where is_a_global_final_cstate__relax
        #   else:   high_level_position is the end of an error prefix
        #
        # reason:
        #   return FailOnGlobalDead, False, actual_access_end
        #   return SuccessOnGlobalFinal, True, actual_access_end
        #   return FailUntilEnd, False, actual_access_end
        #   return SuccessUntilEnd, True, actual_access_end
        #
        #   # SuccessOnGlobalFinal # is_a_global_final_cstate__relax
        #   # FailOnGlobalDead # is_a_global_dead_cstate__relax
        high_level_position = 0
        initial_cstate = ops.get_the_initial_cstate(self)
        feed = ops.feed
        #is_dead = ops.is_a_local_dead_cstate
        is_global_dead = ops.is_a_global_dead_cstate__relax
        is_final = ops.is_a_local_final_cstate
        is_global_final = ops.is_a_global_final_cstate__relax


        def handle(cstate):
            # -> None | main_result
            #if is_dead(self, cstate):
            if is_global_dead(self, cstate):
                return FailOnGlobalDead, False, actual_access_end
            elif is_global_final(self, cstate):
                return SuccessOnGlobalFinal, True, actual_access_end
            return None


        cstate = initial_cstate
        end_low = begin_low_level_reference
        actual_access_end = high_level_position, end_low

        may_main_result = handle(cstate)
        if may_main_result is not None:
            main_result = may_main_result
            return main_result

        for terminal, end_low in terminal_end_low_level_reference_pairs:
            #bug: actual_access_end = high_level_position, end_low
            #   high_level_position not increased yet
            high_level_position, cstate = feed(self, cstate, terminal
                                                , high_level_position)
            actual_access_end = high_level_position, end_low
            may_main_result = handle(cstate)
            if may_main_result is not None:
                main_result = may_main_result
                return main_result

        if is_final(self, cstate):
            return SuccessUntilEnd, True, actual_access_end
        return FailUntilEnd, False, actual_access_end

    def search_prefix(ops, self, terminals, greedy:bool):
        # -> None | ... | high_level_position_of_prefix_end
        #   position after last terminal
        #   not position of last terminal
        #
        pairs = ((terminal, None) for terminal in terminals)
        reason, may_result_ex, actual_access_end = \
            ops.search_prefix_ex(self, None, pairs, greedy)
        if may_result_ex is None:
            return None
        elif may_result_ex is ...:
            return ...
        high_level_position_of_prefix_end, _ = may_result_ex
        return high_level_position_of_prefix_end

    def search_prefix_ex(ops, self
                        , begin_low_level_reference
                        , terminal_end_low_level_reference_pairs
                        , greedy:bool):
        # -> (reason, may_result_ex, actual_access_end)
        #   may_result_ex = ... | None | result
        #   result = (high_level_position_of_prefix_end
        #           , low_level_reference_of_prefix_end))
        #           position after last terminal
        #           not position of last terminal
        #   actual_access_end = (high_level_position_of_access_end
        #                       ,low_level_reference_of_access_end)
        # when success: longest if greedy else shortest
        #
        # reason:
        #   return FailOnGlobalDead, None, actual_access_end
        #   return FailUntilEnd, None, actual_access_end
        #   return SuccessOnGlobalFinal, ..., actual_access_end
        #   return SuccessOnNonGreedy, result=, actual_access_end
        #   return SuccessOnGlobalDead, result<=, actual_access_end
        #   return SuccessUntilEnd, result<=, actual_access_end
        #       SuccessOnNonGreedy:
        #           result==actual_access_end
        #       SuccessOnGlobalDead/SuccessUntilEnd:
        #           result<=actual_access_end
        #
        #   # SuccessOnGlobalFinal # is_a_global_final_cstate__relax
        #   # FailOnGlobalDead # is_a_global_dead_cstate__relax
        #
        greedy = bool(greedy)

        high_level_position = 0
        initial_cstate = ops.get_the_initial_cstate(self)
        feed = ops.feed
        #is_dead = ops.is_a_local_dead_cstate
        is_global_dead = ops.is_a_global_dead_cstate__relax
        is_final = ops.is_a_local_final_cstate
        is_global_final = ops.is_a_global_final_cstate__relax



        # actual_access_end = high_level_position, end_low
        def handle(cstate, actual_access_end):
            # -> may_main_result
            # -> None | main_result
            # None          - no-op
            # main_result   - return directly
            #
            # reason = SuccessOnNonGreedy/SuccessOnGlobalFinal/FailOnGlobalDead/SuccessOnGlobalDead
            nonlocal saved_may_result

            if is_final(self, cstate):
                # position after last terminal
                # not position of last terminal
                # save result
                result = actual_access_end
                if not greedy:
                    return SuccessOnNonGreedy, result, actual_access_end
                elif is_global_final(self, cstate):
                    return SuccessOnGlobalFinal, ..., actual_access_end

                saved_may_result = result       # output
                return None                     # no-op
            #elif is_dead(self, cstate):
            elif is_global_dead(self, cstate):
                may_result = saved_may_result   # input
                if may_result is None:
                    # fail
                    return FailOnGlobalDead, None, actual_access_end
                result = may_result
                return SuccessOnGlobalDead, result, actual_access_end
            return None                         # no-op



        cstate = initial_cstate
        saved_may_result = None
        end_low = begin_low_level_reference

        actual_access_end = high_level_position, end_low
        may_main_result = handle(cstate, actual_access_end)
        if may_main_result is not None:
            main_result = may_main_result
            return main_result


        for terminal, end_low in terminal_end_low_level_reference_pairs:
            high_level_position, cstate = feed(self, cstate, terminal
                    , high_level_position)

            actual_access_end = high_level_position, end_low
            may_main_result = handle(cstate, actual_access_end)
            if may_main_result is not None:
                main_result = may_main_result
                return main_result

        if saved_may_result is None:
            return FailUntilEnd, None, actual_access_end
        result = saved_may_result
        return SuccessUntilEnd, result, actual_access_end

class IFAOps__succ_astates(IFAOps):
    __slots__ = ()


    @not_implemented
    def astate2iter_nonnull_succ_astates(ops, self, astate):
        # -> Iter succ_astate # via all nonnull_outgoing_transitions
        ...

    '''
    def is_a_global_final_cstate__def(ops, self, cstate):
        # global_final_cstate <==> any astate in it is global_final

    def is_a_global_dead_cstate__def(ops, self, cstate):
        # global_dead_cstate <==> all astates in it are global_dead
    '''

if __name__ == '__main__':
    XXX = IFAOps

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)
