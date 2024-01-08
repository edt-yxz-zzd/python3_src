#__all__:goto
r'''[[[
e ../../python3_src/seed/text/avoid_py_str_literal.py
src-code:move from:
    view ../../python3_src/nn_ns/app/line_selector.py

why?
    to handle pseudo-py-like language/mini-language, such as split/replace/find, almost required to skip py_str_literal


seed.text.avoid_py_str_literal
py -m nn_ns.app.debug_cmd   seed.text.avoid_py_str_literal -x
py -m nn_ns.app.doctest_cmd seed.text.avoid_py_str_literal:__doc__ -ff -v
py -m nn_ns.app.doctest_cmd nn_ns.app.line_selector:__doc__ -ff -v

py_adhoc_call   seed.text.avoid_py_str_literal   @f

#]]]'''
__all__ = r'''
StrOps4avoid_selected_substr
    str_ops4avoid_py_str_literal

        replace___avoid_py_str_literal_
            split___avoid_py_str_literal_
                split_out__py_str_literals_


replace_ex___avoid_py_str_literal_
    extract_old5new_idx__re_matchobj_groupdict_


erase_spaces_
    regex4erase_spaces
'''.split()#'''
            #regex4split_out__py_str_literal

__all__
import re
from seed.for_libs.for_re___split import split as asif_re__split_, iter_split as iter_asif_re__split_
from seed.text.useful_regex_patterns import py_str__pattern, py_str__regex
#from seed.tiny import check_type_is, echo, mk_fprint, print_err


regex4erase_spaces = re.compile(r'\s+')
def erase_spaces_(s, /):
    r'''[[[
    may cause bug:
        concat keyword and identifier: 『lambda u:(s if x or y is z in c else t)』
        may distroy py_str_literal
    #]]]'''#'''
    return regex4erase_spaces.sub('', s)

class StrOps4avoid_selected_substr:
    def __init__(sf, regexobj4selected_substr, /):
        sf.regexobj4selected_substr = regexobj4selected_substr
    def replace___avoid_selected_substr_(sf, old_sep, new_sep, s, /):
        ls = sf.split___avoid_selected_substr_(old_sep, s)
        return new_sep.join(ls)
    def split___avoid_selected_substr_(sf, sep, s, /):
        ls4gap_and_selected_substr = sf.split_out__selected_substrs_(s)
        assert len(ls4gap_and_selected_substr)&1 == 1
        ls4gap_and_selected_substr.append('')
        ls4out = []
        ls4last = []
        for i4gap in range(len(ls4gap_and_selected_substr))[::2]:
            gap = ls4gap_and_selected_substr[i4gap]
            ss = gap.split(sep)
            assert ss
            if len(ss) == 1:
                assert ss == [gap]
                ls4last.append(gap)
            else:
                tail4prev, *ls4mid, init4next = ss
                ls4last.append(tail4prev)
                last4prev = ''.join(ls4last)
                ls4out.append(last4prev)
                ls4out.extend(ls4mid)
                ls4last = [init4next]
            smay_selected_substr = ls4gap_and_selected_substr[1+i4gap]
            ls4last.append(smay_selected_substr)
        else:
                last = ''.join(ls4last)
                ls4out.append(last)
        return ls4out


    def split_out__selected_substrs_(sf, s, /):
        #ls4gap_and_selected_substr = sf.regexobj4selected_substr.split(s)
            # bug: output depends capturing groups
        #bug:ls4gap_and_selected_substr = asif_re__split_(sf.regexobj4selected_substr, s)
        ls4gap_and_selected_substr = asif_re__split_(sf.regexobj4selected_substr, s, case4sep=True)
        assert len(ls4gap_and_selected_substr)&1 == 1
            #selected_substr @odd idx
        return ls4gap_and_selected_substr

if 1:
    str_ops4avoid_py_str_literal = StrOps4avoid_selected_substr(py_str__regex)
    replace___avoid_py_str_literal_ = str_ops4avoid_py_str_literal.replace___avoid_selected_substr_
    split___avoid_py_str_literal_ = str_ops4avoid_py_str_literal.split___avoid_selected_substr_
    split_out__py_str_literals_ = str_ops4avoid_py_str_literal.split_out__selected_substrs_
    ##no:regex4split_out__py_str_literal



def __():
    def replace___avoid_py_str_literal_(old_sep, new_sep, s, /):
        ls = split___avoid_py_str_literal_(old_sep, s)
        return new_sep.join(ls)
    def split___avoid_py_str_literal_(sep, s, /):
        ls4gap_and_py_str_literal = split_out__py_str_literals_(s)
        assert len(ls4gap_and_py_str_literal)&1 == 1
        ls4gap_and_py_str_literal.append('')
        ls4out = []
        ls4last = []
        for i4gap in range(len(ls4gap_and_py_str_literal))[::2]:
            gap = ls4gap_and_py_str_literal[i4gap]
            ss = gap.split(sep)
            assert ss
            if len(ss) == 1:
                assert ss == [gap]
                ls4last.append(gap)
            else:
                tail4prev, *ls4mid, init4next = ss
                ls4last.append(tail4prev)
                last4prev = ''.join(ls4last)
                ls4out.append(last4prev)
                ls4out.extend(ls4mid)
                ls4last = [init4next]
            smay_py_str_literal = ls4gap_and_py_str_literal[1+i4gap]
            ls4last.append(smay_py_str_literal)
        else:
                last = ''.join(ls4last)
                ls4out.append(last)
        return ls4out


    regex4split_out__py_str_literal = re.compile(fr'({py_str__pattern})')
    def split_out__py_str_literals_(s, /):
        ls4gap_and_py_str_literal = regex4split_out__py_str_literal.split(s)
            #py_str_literal @odd idx
        assert len(ls4gap_and_py_str_literal)&1 == 1
        return ls4gap_and_py_str_literal



def extract_old5new_idx__re_matchobj_groupdict_(old_s, new_idx2old_idx, m, /):
    #d = m.groupdict()
    #print_err(m.groupdict())
    #print_err(m.groups())
    d = {}
    for k, may in m.groupdict().items():
        #print_err(k)
        if may is None:
            d[k] = None
            continue
        new_i,new_j = m.span(k)
        old_i = new_idx2old_idx[new_i]
        old_j = new_idx2old_idx[new_j]
        d[k] = old_s[old_i:old_j]
    d
    return d
def replace_ex___avoid_py_str_literal_(old_s, /):
    # new_sep = _find_unused_nm_(s)
    new_sep = '""'
    ls4gap_and_py_str_literal = split_out__py_str_literals_(old_s)
    gaps = ls4gap_and_py_str_literal[0::2]
    ls4py_str_literal = ls4gap_and_py_str_literal[1::2]
    new_s = new_sep.join(gaps)
    new_idx2old_idx = []
    old_i = 0
    def put_old_idx_(old_i, /):
        new_idx2old_idx.append(old_i)
        return old_i + 1
    for gap, smay in zip(gaps, [*ls4py_str_literal, '']):
        for _ in gap:
            old_i = put_old_idx_(old_i)
        if smay:
            assert len(smay) >= 2
            old_i = put_old_idx_(old_i)
                # open "
            old_i += len(smay)-2
            old_i = put_old_idx_(old_i)
                # close "
    new_idx2old_idx
    assert len(new_idx2old_idx) == len(new_s)
    assert old_i == len(old_s)
    old_end = len(old_s)
    put_old_idx_(old_end)

    return (new_idx2old_idx, new_s)










__all__





from seed.text.avoid_py_str_literal import StrOps4avoid_selected_substr
from seed.text.avoid_py_str_literal import (
str_ops4avoid_py_str_literal
,replace___avoid_py_str_literal_
,    split___avoid_py_str_literal_
,        split_out__py_str_literals_
,replace_ex___avoid_py_str_literal_
,    extract_old5new_idx__re_matchobj_groupdict_
)
#,            regex4split_out__py_str_literal
from seed.text.avoid_py_str_literal import erase_spaces_, regex4erase_spaces
from seed.text.avoid_py_str_literal import *

