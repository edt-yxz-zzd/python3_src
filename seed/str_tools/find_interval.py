#__all__:goto
r'''[[[
e ../../python3_src/seed/str_tools/find_interval.py

seed.str_tools.find_interval
py -m nn_ns.app.debug_cmd   seed.str_tools.find_interval -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.str_tools.find_interval:__doc__ -ht # -ff -df
#######

[[
used in:
    view script/clean_w3schools_pages.py
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.str_tools.find_interval   @f

]]]'''#'''
__all__ = r'''

indexs_
    index_trials_

find_interval4the_containing_html_element_at__
    search_first_word_
    find_interval4the_containing_scope_at___
        profile_check_idx_inside_scope__
        find_begin4the_containing_scope_at___
        find_end4the_containing_scope_at___

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge_le, check_int_ge_lt
from seed.str_tools.Errors import BaseError, Fail, ParamError
___end_mark_of_excluded_global_names__0___ = ...


def indexs_(s, begin, end, substrs, /):
    rngs = []
    j = begin
    for t in substrs:
        try:
            i = s.index(t, j, end)
        except ValueError as e:
            raise Fail('index():', t) from e
        j = i + len(t)
        rngs.append((i,j))
    return rngs
def index_trials_(s, begin, end, substrs7alternation, /):
    s.index('', begin, end)
    for k, t in enumerate(substrs7alternation):
        try:
            i = s.index(t, begin, end)
        except ValueError:
            continue
        j = i + len(t)
        return (i,j)
    raise Fail("index_trials_()", substrs7alternation)


def search_first_word_(s, begin, end, /):
    for j in range(begin, end):
        ch = s[j]
        if ch.isalnum():
            iword = j
            break
    else:
        raise Fail('fail:search_first_word_()')
    iword
    for j in range(iword+1, end):
        ch = s[j]
        if not ch.isalnum():
            jword = j
            break
    else:
        jword = end
    jword
    word = s[iword:jword]
    return (word, (iword, jword))
def profile_check_idx_inside_scope__(may_prefix4scope, may_suffix4scope, idx7inside_scope, whole_text, begin4txt, end4txt, /, *, without_prefix4scope=False, without_suffix4scope=False):
    check_type_is(str, whole_text)

    if without_prefix4scope:
        if not None is may_prefix4scope:raise ParamError('[without_prefix4scope][may_prefix4scope is not None]')
        sz4prefix = 0
    else:
        prefix4scope = may_prefix4scope
        check_type_is(str, prefix4scope)
        sz4prefix = len(prefix4scope)
        if 0 == sz4prefix:raise ParamError('prefix4scope empty')
    sz4prefix

    if without_suffix4scope:
        if not None is may_suffix4scope:raise ParamError('[without_suffix4scope][may_suffix4scope is not None]')
        sz4suffix = 0
    else:
        suffix4scope = may_suffix4scope
        check_type_is(str, suffix4scope)
        sz4suffix = len(suffix4scope)
        if 0 == sz4suffix:raise ParamError('suffix4scope empty')
    sz4suffix

    if sz4prefix and sz4suffix:
        if prefix4scope in suffix4scope:raise ParamError((prefix4scope, suffix4scope))
        if suffix4scope in prefix4scope:raise ParamError((prefix4scope, suffix4scope))


    check_int_ge_le(0, len(whole_text), begin4txt)
    check_int_ge_le(begin4txt+sz4prefix+sz4suffix, len(whole_text), end4txt)
    check_int_ge_lt(begin4txt, end4txt, idx7inside_scope)
        # 『lt』
def find_interval4the_containing_scope_at___(prefix4scope, suffix4scope, idx7inside_scope, whole_text, begin4txt, end4txt, /):
    profile_check_idx_inside_scope__(prefix4scope, suffix4scope, idx7inside_scope, whole_text, begin4txt, end4txt)
    begin4scope = find_begin4the_containing_scope_at___(prefix4scope, suffix4scope, idx7inside_scope, whole_text, begin4txt, end4txt, whether_profile_checked_idx_inside_scope=True)
    end4scope = find_end4the_containing_scope_at___(prefix4scope, suffix4scope, idx7inside_scope, whole_text, begin4txt, end4txt, whether_profile_checked_idx_inside_scope=True)
    interval4scope = (begin4scope, end4scope)
    return interval4scope

def find_begin4the_containing_scope_at___(prefix4scope, suffix4scope, idx7inside_scope, whole_text, begin4txt, end4txt, /, *, whether_profile_checked_idx_inside_scope=False):
    if not whether_profile_checked_idx_inside_scope:
        profile_check_idx_inside_scope__(prefix4scope, suffix4scope, idx7inside_scope, whole_text, begin4txt, end4txt)
    sz4prefix = len(prefix4scope)
    sz4suffix = len(suffix4scope)
    # !! [begin4txt <= idx7inside_scope < end4txt]
    # !! [begin4txt + sz4prefix + sz4suffix <= end4txt]
    # !! [sz4prefix >= 1]
    #idx7inside_scope = min(idx7inside_scope, end4txt -sz4prefix -sz4suffix)
    # [begin4txt <= idx7inside_scope < end4txt]
    num_CLOSEs = 0
    #for j in reversed(range(begin4txt, 1+idx7inside_scope)):
    (min_j8end4prefix, max_j8end4prefix) = (begin4txt+sz4prefix, min(idx7inside_scope+sz4prefix, end4txt-sz4suffix))
    j8end4prefix = max_j8end4prefix
    while j8end4prefix >= min_j8end4prefix:
        if whole_text.endswith(prefix4scope, begin4txt, j8end4prefix):
            # OPEN
            if num_CLOSEs == 0:
                begin4scope = j8end4prefix -sz4prefix
                break
            num_CLOSEs -= 1
            sz4step = sz4prefix
        elif whole_text.endswith(suffix4scope, begin4txt, j8end4prefix):
            # CLOSE
            num_CLOSEs += 1
            sz4step = sz4suffix
        else:
            sz4step = 1
        sz4step
        j8end4prefix -= sz4step

    else:
        raise Fail('fail:find_begin4the_containing_scope_at___()')
    begin4scope
    return begin4scope

def find_end4the_containing_scope_at___(prefix4scope, suffix4scope, idx7inside_scope, whole_text, begin4txt, end4txt, /, *, whether_profile_checked_idx_inside_scope=False):
    if not whether_profile_checked_idx_inside_scope:
        profile_check_idx_inside_scope__(prefix4scope, suffix4scope, idx7inside_scope, whole_text, begin4txt, end4txt)
    sz4prefix = len(prefix4scope)
    sz4suffix = len(suffix4scope)
    # !! [begin4txt <= idx7inside_scope < end4txt]
    # !! [begin4txt + sz4prefix + sz4suffix <= end4txt]
    # !! [sz4prefix >= 1]
    #idx7inside_scope = max(idx7inside_scope, begin4txt +sz4prefix)
    # [begin4txt <= idx7inside_scope < end4txt]
    num_OPENs = 0
    (min_j8begin4suffix, max_j8begin4suffix) = (max(begin4txt+sz4prefix, 1+idx7inside_scope-sz4suffix), end4txt-sz4suffix)
    #for j in range(idx7inside_scope, 1+ end4txt -sz4suffix):
    j8begin4suffix = min_j8begin4suffix
    while j8begin4suffix <= max_j8begin4suffix:
        if whole_text.startswith(prefix4scope, j8begin4suffix, end4txt):
            # OPEN
            num_OPENs += 1
            sz4step = sz4prefix
        elif whole_text.startswith(suffix4scope, j8begin4suffix, end4txt):
            # CLOSE
            if num_OPENs == 0:
                #bug:end4scope = j8begin4suffix
                end4scope = j8begin4suffix + sz4suffix
                break
            num_OPENs -= 1
            sz4step = sz4suffix
        else:
            sz4step = 1
        j8begin4suffix += sz4step

    else:
        raise Fail('fail:find_end4the_containing_scope_at___()')
    end4scope
    return end4scope



#bug: result start_element only
#.def find_name_and_interval4the_containing_html_element_at_(idx7inside_scope, page, begin, end, /):
#.    (ielement, jelement) = find_interval4the_containing_scope_at___('<', '>', idx7inside_scope, page, begin, end)
#.    (tag, _) = search_first_word_(page, ielement, jelement)
#.    return (tag, (ielement, jelement))
def find_interval4the_containing_html_element_at__(tag, idx7inside_html_element, page, begin, end, /):
    (ielement, _jelement) = find_interval4the_containing_scope_at___(f'<{tag}', f'</{tag}', idx7inside_html_element, page, begin, end)
    jelement = 1+page.index('>', _jelement, end)
    interval4element = (ielement, jelement)
    return interval4element

__all__
#.from seed.str_tools.find_interval import BaseError, Fail, ParamError
from seed.str_tools.find_interval import indexs_, index_trials_
from seed.str_tools.find_interval import search_first_word_, find_interval4the_containing_scope_at___, profile_check_idx_inside_scope__, find_begin4the_containing_scope_at___, find_end4the_containing_scope_at___
from seed.str_tools.find_interval import find_interval4the_containing_html_element_at__

from seed.str_tools.find_interval import *
