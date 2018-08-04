

__all__ = '''
    RegexCompileResult
    '''.split()


from collections import namedtuple
from .IFAOps import IFAOps


RegexCompileResultBase = namedtuple('RegexCompileResultBase', '''
    pattern
    regex
    simplified_regex
    fa
    fa_ops
    '''.split()
    )
class RegexCompileResult(RegexCompileResultBase):
    '''regex -> nfa/dfa

methods:
    does_accept
    does_accept_ex
    search_prefix
    search_prefix_ex
    search_leftmost_substring
    search_leftmost_substring_ex
    search_leftmost_substring_ex_ex
'''

    __slots__ = ()
    def __init__(self, pattern, regex, simplified_regex, fa, fa_ops):
        assert isinstance(fa_ops, IFAOps)


    def does_accept(self, terminals):
        # -> does_accept:bool
        return self.fa_ops.does_accept(self.fa, terminals)

    def does_accept_ex(self
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
        return self.fa_ops.does_accept_ex(self.fa
                    , begin_low_level_reference
                    , terminal_end_low_level_reference_pairs
                    )
    def search_prefix(self, terminals, greedy:bool):
        # -> None | ... | high_level_position_of_prefix_end
        #   position after last terminal
        #   not position of last terminal
        #
        return self.fa_ops.search_prefix(self.fa, terminals, greedy)
    def search_prefix_ex(self
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
        return self.fa_ops.search_prefix_ex(self.fa
                    , begin_low_level_reference
                    , terminal_end_low_level_reference_pairs
                    , greedy
                    )

    def search_leftmost_substring(self, terminals
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
        return self.fa_ops.search_leftmost_substring(self.fa
                    , terminals
                    , greedy
                    , leftmost_end_first
                    )
    def search_leftmost_substring_ex(self
            , begin_low_level_reference
            , terminal_end_low_level_reference_pairs
            , greedy:bool
            , leftmost_end_first:bool):
        # -> (may_result_ex, actual_access_end)
        # see: search_leftmost_substring_ex_ex for:
        #   may_result_ex, actual_access_end
        #
        return self.fa_ops.search_leftmost_substring_ex(self.fa
                    , begin_low_level_reference
                    , terminal_end_low_level_reference_pairs
                    , greedy
                    , leftmost_end_first
                    )

    def search_leftmost_substring_ex_ex(self
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
        return self.fa_ops.search_leftmost_substring_ex_ex(self.fa
                    , begin_low_level_reference
                    , terminal_end_low_level_reference_pairs
                    , greedy
                    , leftmost_end_first
                    )


