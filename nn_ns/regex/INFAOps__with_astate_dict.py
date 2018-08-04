
__all__ = '''
    INFAOps__with_astate_dict
    '''.split()

from .abc import abstractmethod, not_implemented, override
from .INFAOps import INFAOps
from .IFAOps__with_astate_dict import IFAOps__with_astate_dict
from .imports.Pair import Pair
from seed.tiny import fst #, snd

#class SearchLeftmostSubstring(Enum):
FailUntilEnd                        = 'FailUntilEnd'
FailOnGlobalDead                    = 'FailOnGlobalDead'
LeftMostEnd_GreedyBegin             = 'LeftMostEnd_GreedyBegin'
LeftMostEnd_NonGreedyBegin          = 'LeftMostEnd_NonGreedyBegin'
LeftMostBegin_NonGreedyEnd          = 'LeftMostBegin_NonGreedyEnd'
LeftMostBegin_ToWholeEnd            = 'LeftMostBegin_ToWholeEnd'
LeftMostBegin_SuccessUntilEnd       = 'LeftMostBegin_SuccessUntilEnd'
LeftMostBegin_SuccessOnGlobalDead   = 'LeftMostBegin_SuccessOnGlobalDead'

if False and __debug__:
    def eprint(*args):
        from sys import stderr
        print(*args, file=stderr)
else:
    def eprint(*args):
        pass

class INFAOps__with_astate_dict(INFAOps, IFAOps__with_astate_dict):
    '''
override
    _nstate2cnstate_
    search_leftmost_substring_ex_ex
'''
    __slots__ = ()

    @override
    def _nstate2cnstate_(ops, self, nstate):
        # -> new_cnstate
        nstate2iter_astates = ops.nstate2iter_astates
        complete_astates = ops.complete_astates
        make_nstate_from_astates = ops.make_nstate_from_astates

        astates = nstate2iter_astates(self, nstate)
        c_astates = complete_astates(self, astates)
        c_nstate = make_nstate_from_astates(self, c_astates)
        cnstate = c_nstate
        return cnstate

    def complete_astates(ops, self, astates):
        # -> Set astate # null_transition closure
        # -> c_astates
        make_astate_set = ops.make_astate_set
        nstate2iter_astates = ops.nstate2iter_astates
        _null_transition_of_astate_ = ops._null_transition_of_astate_

        astates_to_handled = make_astate_set(self, astates)
        handled_astates = make_astate_set(self)

        while astates_to_handled:
            astate = astates_to_handled.pop()
            assert astate not in handled_astates
            #if astate in handled_astates: continue
            handled_astates.add(astate)

            nstate = _null_transition_of_astate_(self, astate)
            astates_to_handled.update(
                    astate
                    for astate in nstate2iter_astates(self, nstate)
                    if astate not in handled_astates
                    )
        return handled_astates


    @override
    def search_leftmost_substring_ex_ex(ops, self
            , begin_low_level_reference
            , terminal_end_low_level_reference_pairs
            , greedy:bool
            , leftmost_end_first:bool):
        # -> (reason, may_result_ex, actual_access_end)
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
        # reason
        #   FailUntilEnd
        #   FailOnGlobalDead
        #   LeftMostEnd_GreedyBegin
        #   LeftMostEnd_NonGreedyBegin
        #   LeftMostBegin_NonGreedyEnd
        #   LeftMostBegin_ToWholeEnd
        #   LeftMostBegin_SuccessUntilEnd
        #   LeftMostBegin_SuccessOnGlobalDead

        greedy = bool(greedy)
        leftmost_end_first = bool(leftmost_end_first)

        initial_cstate = ops.get_the_initial_cstate(self)
        #feed = ops.feed
        #is_local_dead = ops.is_a_local_dead_astate
        is_global_dead = ops.is_a_global_dead_astate__relax
        is_local_final = ops.is_a_local_final_astate
        is_global_final = ops.is_a_global_final_astate__relax
        _feed_astate2nstate_ = ops._feed_astate2nstate_
        #_null_transition_of_astate_ = ops._null_transition_of_astate_
        complete_astates = ops.complete_astates
        nstate2iter_astates = ops.nstate2iter_astates
        make_astate_set = ops.make_astate_set
        make_astate_dict = ops.make_astate_dict

        def may_lt(may_highlowL, may_highlowR):
            # None = +inf
            L = may_highlowL
            R = may_highlowR
            if L is None: return False
            if R is None: return True
            return lt(L, R)
        def lt(lhs_highlow, rhs_highlow):
            return lhs_highlow[0] < rhs_highlow[0]
        NoneResult = None

        def Result(begin, end):
            return begin, end


        # tagged cstate
        # astate2begin_end :: Map cstate Pair(begin, may_end)
        #   begin :: (high, low)
        #   end :: (high, low)

        #actual_access_end = None
        def main():
            #nonlocal actual_access_end
            astate2begin_end = make_astate_dict(self)
            high_end = 0 # high_level_position
            low_end = begin_low_level_reference
            actual_access_end = high_end, low_end # initial

            # restore before remove
            #   later remove before restore
            #   since disable_restore
            to_restore = True
            restore_initial_cstate(astate2begin_end, actual_access_end)
            may_main_result, to_restore = remove_and_handle(
                            astate2begin_end, to_restore, actual_access_end)
            if may_main_result is not None:
                main_result = may_main_result
                return main_result
            elif not astate2begin_end:
                # global_dead
                return handle_global_dead(actual_access_end)

            if True and __debug__: eprint('<start>' + '-'*70)
            for terminal, low_end in terminal_end_low_level_reference_pairs:
                assert astate2begin_end
                if True and __debug__: eprint(astate2begin_end)
                if True and __debug__: eprint(high_end, terminal)

                # feed
                # high_end++
                # update astate2begin_end
                high_end += 1
                actual_access_end = high_end, low_end



                astate2begin_end = step_astate2begin_end(
                                        astate2begin_end, terminal)
                # now, keys of astate2begin_end make up a cstate



                # before remove, should perform null_transition
                #   fix_new_astate2begin_end__null_transition
                may_main_result, to_restore = remove_and_handle(
                            astate2begin_end, to_restore, actual_access_end)
                if True and __debug__: eprint('\tremove:', astate2begin_end)
                # may disable_restore now
                if may_main_result is not None:
                    main_result = may_main_result
                    return main_result
                if to_restore:
                    restore_initial_cstate(astate2begin_end, actual_access_end)
                if True and __debug__: eprint('\trestore:', astate2begin_end)

                if not astate2begin_end:
                    # global_dead
                    return handle_global_dead(actual_access_end)

            assert astate2begin_end
            if saved_may_best_result is None:
                # not found_one
                reason = FailUntilEnd
                return reason, NoneResult, actual_access_end
            best_result = saved_may_best_result
            begin, end = best_result

            assert not leftmost_end_first
            assert begin is not None
            assert end is not None

            reason = LeftMostBegin_SuccessUntilEnd
            return reason, Result(begin, end), actual_access_end

        def step_astate2begin_end(astate2begin_end, terminal):
            # -> new_astate2begin_end
            new_astate2begin_end = make_astate_dict(self)
            #bug: to_end = high_end # to_end should be pair/highlow_end
            #to_end = actual_access_end
            for from_astate, from_pair in astate2begin_end.items():
                to_nstate = _feed_astate2nstate_(self, from_astate, terminal)
                #bug:??from_begin = astate2begin_end[from_astate].fst
                #new_pair = Pair(from_begin, to_end)
                #   bug: new_pair = from_begin, to_end
                #update_new_astate2begin_end(new_astate2begin_end
                #        , from_astate, new_pair, to_nstate)
                update_new_astate2begin_end(new_astate2begin_end
                        , from_astate, from_pair, to_nstate)
            if True and __debug__: eprint('\tstep:', new_astate2begin_end)

            fix_new_astate2begin_end__null_transition(new_astate2begin_end)
            if True and __debug__: eprint('\tfix:', new_astate2begin_end)
            # now, keys of new_astate2begin_end make up a cstate

            return new_astate2begin_end



        # clean initial_cstate
        clean_initial_astates = tuple(astate
                        for astate in nstate2iter_astates(self, initial_cstate)
                        if not is_global_dead(self, astate))
        del initial_cstate

        def disable_restore_initial_cstate(astate2begin_end, actual_access_end):
            return
        def restore_initial_cstate(astate2begin_end, actual_access_end):
            # since (.*) ++ self
            # initial_cstate appear everywhere
            setdefault = astate2begin_end.setdefault
            pair = Pair(actual_access_end, None)
            for initial_astate in clean_initial_astates:
                # bug: setdefault(initial_astate, pair)
                _update(astate2begin_end, initial_astate, pair)
            return


        def del_keys(d, keys):
            for k in keys:
                del d[k]

        def handle_global_dead(actual_access_end):
            if saved_may_best_result is not None:
                begin, end = saved_may_best_result
                assert greedy and not leftmost_end_first
                    # non-greedy will return directly, not here
                    #   # it will detect (not astate2begin_end)
                assert begin is not None
                assert end is not None
                reason = LeftMostBegin_SuccessOnGlobalDead
                return reason, Result(begin, end), actual_access_end

            assert not clean_initial_astates
            reason = FailOnGlobalDead
            return reason, NoneResult, actual_access_end

        def remove_and_handle(astate2begin_end
                    , to_restore:bool, actual_access_end):
            # -> ((None | main_result), to_restore:bool)
            found_one, found_to_end = remove_local_dead_astates(
                                astate2begin_end, actual_access_end)
            if found_one:
                may_main_result = handle_found_one(
                                found_one, found_to_end
                                , astate2begin_end, actual_access_end)
                return may_main_result, False
            else:
                may_main_result = None
                return may_main_result, to_restore
            pass
            return may_main_result, (to_restore and not found_one)
        # None | Pair(high, low)
        #saved_may_min_begin = None
        #saved_may_max_end = None

        # None | Pair(high, low)
        saved_may_best_result = None
        saved_may_best_result_to_end = None
        def update_best_result(pair):
            nonlocal saved_may_best_result
            if saved_may_best_result is None \
                or should_update_pair(saved_may_best_result, pair):
                saved_may_best_result = pair # output
            return
        def update_best_result_to_end(pair):
            nonlocal saved_may_best_result_to_end
            if saved_may_best_result_to_end is None \
                or lt(pair.fst, saved_may_best_result_to_end.fst):
                saved_may_best_result_to_end = pair # output
            return
        def remove_local_dead_astates(astate2begin_end, actual_access_end):
            # -> (None | main_result)

            found_one = False # one complete substring
            found_to_end = False # success until end
            #for astate, pair in astate2begin_end.items():
            for astate in list(astate2begin_end):
                pair = astate2begin_end[astate]

                if is_local_final(self, astate):
                    #pair.snd = actual_access_end
                    pair = pair._replace(snd=actual_access_end)
                    astate2begin_end[astate] = pair
                        # Pair
                        # maybe one possible matched substring
                        # assume pair = Pair((5, _), (7, _))
                        #   now, we are at high_end 7
                        #   but there may be a Pair((1,_), None)
                        #       which may finally matched as Pair((1,_), (8,_))
                        #           when greedy=True, leftmost_end_first=False
                        #

                    update_best_result(pair)
                    found_one = True

                    #if not found_to_end and is_global_final(self, astate):
                    if is_global_final(self, astate):
                        found_to_end = True
                        update_best_result_to_end(pair)
                        del astate2begin_end[astate]

                #elif is_local_dead(self, astate):
                elif is_global_dead(self, astate):
                    del astate2begin_end[astate]
            return found_one, found_to_end

        prev_saved_may_best_result = None
        def handle_found_one(
                found_one, found_to_end, astate2begin_end, actual_access_end):
            # -> (None | main_result)
            #nonlocal restore_initial_cstate # to disable it
            nonlocal prev_saved_may_best_result # output here only
            assert not leftmost_end_first
            #restore_initial_cstate = disable_restore_initial_cstate

            # leftmost_begin_first
            # find leftmost_begin if it has end
            #
            best_result = saved_may_best_result
            assert best_result is not None

            old_may_best_result = prev_saved_may_best_result
            prev_saved_may_best_result = best_result # output
            return remove_using_saved_best_result(
                    astate2begin_end
                    , best_result, old_may_best_result
                    , found_one, found_to_end
                    , actual_access_end)
            return None

        if leftmost_end_first:
            # overwrite prev handle_found_one
            def handle_found_one(
                found_one, found_to_end, astate2begin_end, actual_access_end):
                # -> (None | main_result)
                # execute at most once
                # all first found substrings
                # they has same "end"
                #   i.e. pair.snd == None | found_one.snd
                if __debug__:
                    eprint('leftmost_end_first, handle_found_one, astate2begin_end:\n', astate2begin_end)
                return handle_leftmost_end_first_and_found_one(
                        astate2begin_end, found_one, actual_access_end)

        def remove_using_saved_best_result(
                    astate2begin_end
                    , best_result, old_may_best_result
                    , found_one, found_to_end
                    , actual_access_end):
            assert best_result is not None
            assert not leftmost_end_first
            assert greedy

            new_min_begin__maxbound = best_result.fst
            if old_may_best_result is None:
                to_del = True
            else:
                old_min_begin__maxbound = old_may_best_result.fst
                    # Pair
                to_del = lt(new_min_begin__maxbound, old_min_begin__maxbound)
            if to_del:
                for astate, pair in list(astate2begin_end.items()):
                    if lt(new_min_begin__maxbound, pair.fst):
                        del astate2begin_end[astate]

            if not found_to_end: return
            best_result_to_end = saved_may_best_result_to_end # input

            if lt(new_min_begin__maxbound, best_result_to_end.fst):
                return
            m = best_result_to_end.fst
            if not any(lt(pair.fst, m) for pair in astate2begin_end.values()):
                leftmost_best_result = best_result_to_end
                begin, __end = leftmost_best_result; end = ...
                reason = LeftMostBegin_ToWholeEnd
                return reason, Result(begin, ...), actual_access_end
            return

        if not greedy:
            # overwrite prev remove_using_saved_best_result
            def remove_using_saved_best_result(
                        astate2begin_end
                        , best_result, old_may_best_result
                        , found_one, found_to_end
                        , actual_access_end):
                assert best_result is not None
                assert not leftmost_end_first
                assert not greedy
                del found_to_end

                new_min_begin__maxbound = best_result[0]
                for astate, pair in list(astate2begin_end.items()):
                    # new_min_begin__maxbound <= pair.fst
                    # not (pair.fst < new_min_begin__maxbound)
                    if not lt(pair.fst, new_min_begin__maxbound):
                        del astate2begin_end[astate]
                if astate2begin_end: return

                begin, end = best_result
                reason = LeftMostBegin_NonGreedyEnd
                return reason, Result(begin, end), actual_access_end
        def handle_leftmost_end_first_and_found_one(
                astate2begin_end, found_one, actual_access_end):
            # -> main_result
            # execute at most once
            #
            assert leftmost_end_first
            assert found_one
            begin, end = best_result = saved_may_best_result
            if greedy:
                reason = LeftMostEnd_GreedyBegin
            else:
                reason = LeftMostEnd_NonGreedyBegin
            return reason, Result(begin, end), actual_access_end

        def update_new_astate2begin_end(new_astate2begin_end
                    , from_astate, from_pair, to_nstate):
                    #, from_astate, new_pair, to_nstate):
                    #, from_astate, from_begin, to_end, to_nstate):
            #new_pair = Pair(from_begin, to_end)
            for succ_astate in nstate2iter_astates(self, to_nstate):
                _update(new_astate2begin_end, succ_astate, from_pair)
        def _update(astate2begin_end, astate, pair):
            # return whether overwrite
            #   if return True:
            #       astate must exist in old astate2begin_end
            #       and pair "<" astate2begin_end[astate]
            may_pair = astate2begin_end.setdefault(astate, pair)
            if may_pair is pair:
                # not exist; not overwrite
                return False
            old_pair = may_pair
            if should_update_pair(old_pair, pair):
                astate2begin_end[astate] = pair
                return True
            return False

        def fix_new_astate2begin_end__null_transition(new_astate2begin_end):
            keys = make_astate_set(self, new_astate2begin_end)
            while keys:
                astate = keys.pop()
                pair = new_astate2begin_end[astate]

                #bug: nstate = _null_transition_of_astate_(self, astate)
                c_astates = complete_astates(self, [astate])
                for succ_astate in c_astates:
                    if _update(new_astate2begin_end, succ_astate, pair):
                        # if updated
                        keys.discard(succ_astate)

        #def merge_pairs(lhs_pair, rhs_pair):
            # lhs_pair, rhs_pair :: Pair(begin, may_end)
            # depends on greedy and leftmost_end_first
        #def should_update_pair(old_pair, new_pair):
            # return old_pair ">" new_pair
            # return new_pair "<" old_pair
            # "<" depends on leftmost_end_first and greedy
            # pair :: Pair((high, low), ((high, low)|None))
            #

        '''
        def merge_pairs(lhs_pair, rhs_pair):
            if should_update_pair(lhs_pair, rhs_pair):
                return rhs_pair
            return lhs_pair
        '''
        if leftmost_end_first:
            # snd then fst
            def should_update_pair(old_pair, new_pair):
                # return old_pair ">" new_pair
                # return new_pair "<" old_pair
                if may_lt(new_pair.snd, old_pair.snd):
                    return True
                if may_lt(old_pair.snd, new_pair.snd):
                    return False
                if greedy:
                    return lt(new_pair.fst, old_pair.fst)
                else:
                    return lt(old_pair.fst, new_pair.fst)
        else:
            # leftmost_begin_first
            # fst then snd
            def should_update_pair(old_pair, new_pair):
                # return old_pair ">" new_pair
                # return new_pair "<" old_pair
                if lt(new_pair.fst, old_pair.fst):
                    return True
                if lt(old_pair.fst, new_pair.fst):
                    return False

                if new_pair.snd is None: return False
                if old_pair.snd is None: return True
                if greedy:
                    return lt(old_pair.snd, new_pair.snd)
                else:
                    return lt(new_pair.snd, old_pair.snd)
        return main()




if __name__ == '__main__':
    XXX = INFAOps__with_astate_dict

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)

    from seed.helper.detect_method_conflict import \
        wrapped_print_detect_method_conflict
    wrapped_print_detect_method_conflict(XXX)

    from seed.helper.find_bases_without_slots import print_bases_without_slots
    print_bases_without_slots(XXX)
