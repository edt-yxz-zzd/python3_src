

__all__ = '''
    compile

    does_accept
    does_accept_ex
    search_prefix
    search_prefix_ex
    search_leftmost_substring
    search_leftmost_substring_ex
    search_leftmost_substring_ex_ex
    '''.split()

import functools
from ..RegexCompileResult import RegexCompileResult
from .string_regex_pattern import parse_string_regex_pattern
from .ISimpleNFA import ISimpleNFA
ops = ISimpleNFA.NFA_ops

def _compile(pattern:'Iter Char', *, reverse:bool):
    # used inside this module only, to avoid miss reverse
    return compile(pattern, reverse=reverse)
def compile(pattern:'Iter Char', *, reverse=False):
    if type(pattern) is not str:
        pattern = ''.join(pattern)
    return __compile(pattern, reverse)
@functools.lru_cache(maxsize=128, typed=False)
def __compile(pattern:str, reverse:bool):
    # since use cache, pattern must be str instead of (Iter Char)
    # used inside compile() only
    regex = parse_string_regex_pattern(pattern, simplify=False)
    if reverse:
        regex = regex.to_reverse_regex()
    simplified_regex = regex.simplify(None, True)
    nfa = simplified_regex.toSimpleNFA()
    nfa_ops = ops
    return RegexCompileResult(
        pattern=pattern
        ,regex=regex
        ,simplified_regex=simplified_regex
        ,fa=nfa
        ,fa_ops=nfa_ops
        )


def does_accept(pattern, iter_chars, *, reverse=False):
    '''-> bool
input:
    pattern :: Iter Char
    iter_chars :: Iter Char
output:
    does_accept :: bool
'''
    r = _compile(pattern, reverse=reverse)
    return r.does_accept(iter_chars)
def does_accept_ex(pattern
                    , begin_low_level_reference
                    , char_end_low_level_reference_pairs
                    , *, reverse=False):
    '''-> (reason:str, does_accept:bool, actual_access_end)
input:
    pattern :: Iter Char
    begin_low_level_reference :: low
    char_end_low_level_reference_pairs :: Iter (Char, low)
output:
    (reason, does_accept, actual_access_end)
        reason :: str
        does_accept :: bool
        actual_access_end :: highlow

        highlow :: (UInt, low)

'''
    r = _compile(pattern, reverse=reverse)
    return r.does_accept_ex(
                begin_low_level_reference
                , char_end_low_level_reference_pairs
                )





def search_prefix(pattern, iter_chars, greedy:bool=True, *, reverse=False):
    '''-> (None | ... | end)
        # although in current implement "..." should not appear
input:
    pattern :: Iter Char
    iter_chars :: Iter Char
output:
    may_matched_ex :: None | ... | end
        end :: UInt
'''
    r = _compile(pattern, reverse=reverse)
    return r.search_prefix(iter_chars, greedy)
def search_prefix_ex(pattern
                    , begin_low_level_reference
                    , char_end_low_level_reference_pairs
                    , greedy:bool=True
                    , *, reverse=False):
    '''-> (reason:str, may_result_ex, actual_access_end)
input:
    pattern :: Iter Char
    begin_low_level_reference :: low
    char_end_low_level_reference_pairs :: Iter (Char, low)
output:
    (reason, may_result_ex, actual_access_end)
        reason :: str
        may_result_ex = None | ...  | highlow_end
        actual_access_end :: highlow

        highlow_end :: highlow
        highlow :: (UInt, low)

'''
    r = _compile(pattern, reverse=reverse)
    return r.search_prefix_ex(
                begin_low_level_reference
                , char_end_low_level_reference_pairs
                , greedy
                )





def search_leftmost_substring(pattern, iter_chars
        , greedy:bool=True
        , leftmost_end_first:bool=False
        , *, reverse=False):
    '''-> (None | (begin, end) | (begin, ...))
        # although in current implement (begin, ...) should not appear
input:
    pattern :: Iter Char
    iter_chars :: Iter Char
output:
    may_matched_range :: None | (begin, end)
        begin, end :: UInt

see:
    INFAOps__with_astate_dict
'''
    r = _compile(pattern, reverse=reverse)
    return r.search_leftmost_substring(iter_chars, greedy, leftmost_end_first)

def search_leftmost_substring_ex(pattern
        , begin_low_level_reference
        , char_end_low_level_reference_pairs
        , greedy:bool=True
        , leftmost_end_first:bool=False
        , *, reverse=False):
    '''-> (may_result_ex, actual_access_end)
input:
    pattern :: Iter Char
    begin_low_level_reference :: low
    char_end_low_level_reference_pairs :: Iter (Char, low)
output:
    (may_result_ex, actual_access_end)
        may_result_ex
                    = None
                    | (highlow_begin, ...)
                    | (highlow_begin, highlow_end)
        actual_access_end :: highlow

        highlow_begin, highlow_end :: highlow
        highlow :: (UInt, low)

see:
    INFAOps__with_astate_dict
'''
    r = _compile(pattern, reverse=reverse)
    return r.search_leftmost_substring_ex(
                begin_low_level_reference
                , char_end_low_level_reference_pairs
                , greedy
                , leftmost_end_first
                )
def search_leftmost_substring_ex_ex(pattern
        , begin_low_level_reference
        , char_end_low_level_reference_pairs
        , greedy:bool=True
        , leftmost_end_first:bool=False
        , *, reverse=False):
    '''-> (reason:str, may_result_ex, actual_access_end)
input:
    pattern :: Iter Char
    begin_low_level_reference :: low
    char_end_low_level_reference_pairs :: Iter (Char, low)
output:
    (reason, may_result_ex, actual_access_end)
        reason :: str
        may_result_ex
                    = None
                    | (highlow_begin, ...)
                    | (highlow_begin, highlow_end)
        actual_access_end :: highlow

        highlow_begin, highlow_end :: highlow
        highlow :: (UInt, low)

see:
    INFAOps__with_astate_dict
'''
    r = _compile(pattern, reverse=reverse)
    return r.search_leftmost_substring_ex_ex(
                begin_low_level_reference
                , char_end_low_level_reference_pairs
                , greedy
                , leftmost_end_first
                )


