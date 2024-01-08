#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_re___split.py

why?
    since re.split() result depends on capturing parentheses, hard to control when regexobj is given externally.
def split(pattern, string, maxsplit=0, flags=0):
    """Split the source string by the occurrences of the pattern,
    returning a list containing the resulting substrings.  If
    capturing parentheses are used in pattern, then the text of all
    groups in the pattern are also returned as part of the resulting
    list.  If maxsplit is nonzero, at most maxsplit splits occur,
    and the remainder of the string is returned as the final element
    of the list."""
def finditer(pattern, string, flags=0):
    """Return an iterator over all non-overlapping matches in the
    string.  For each match, the iterator returns a Match object.

    Empty matches are included in the result."""
finditer(string, pos=0, endpos=9223372036854775807) method of re.Pattern instance



[[maxsplit==0]or[len(gaps_tail) -1 == len(seps) == num_matches <= maxsplit]]

seed.for_libs.for_re___split
py -m nn_ns.app.debug_cmd   seed.for_libs.for_re___split -x
py -m nn_ns.app.doctest_cmd seed.for_libs.for_re___split:__doc__ -ff -v
py_adhoc_call   seed.for_libs.for_re___split   @f
from seed.for_libs.for_re___split import *





>>> import re
>>> regexobj = re.compile(r'(?P<As>a+)(b)*')
>>> s = 'abaabbaaabbb'
>>> regexobj.split(s) # capture (b) many time; save (b) instead of (b*)
['', 'a', 'b', '', 'aa', 'b', '', 'aaa', 'b', '']
>>> split(regexobj, s)
['', '', '', '']
>>> s = 'abcaabbccaaabbbccc'
>>> regexobj.split(s)
['', 'a', 'b', 'c', 'aa', 'b', 'cc', 'aaa', 'b', 'ccc']
>>> split(regexobj, s)
['', 'c', 'cc', 'ccc']
>>> split(regexobj, s, case4sep=True)
['', 'ab', 'c', 'aabb', 'cc', 'aaabbb', 'ccc']
>>> split(regexobj, s, case4sep=True, case4gap=False)
['ab', 'aabb', 'aaabbb']
>>> split(regexobj, s, case4gap=False)
[]
>>> split(regexobj, s, case4tail=False)
['', 'c', 'cc', 'ccc']
>>> split(regexobj, s, case4tail=False, maxsplit=4)
['', 'c', 'cc', 'ccc']
>>> split(regexobj, s, case4tail=False, maxsplit=3)
['', 'c', 'cc']
>>> split(regexobj, s, case4sep=True, case4tail=False, maxsplit=3)
['', 'ab', 'c', 'aabb', 'cc', 'aaabbb']
>>> split(regexobj, s, case4sep=True, case4tail=T.span, maxsplit=3)
['', 'ab', 'c', 'aabb', 'cc', 'aaabbb', (15, 18)]
>>> split(regexobj, s, case4sep=True, case4tail=T.span, maxsplit=4)
['', 'ab', 'c', 'aabb', 'cc', 'aaabbb', 'ccc']
>>> split(regexobj, s, case4sep=S.groups, case4gap=G.size, case4tail=T.span, maxsplit=3)
[0, ('a', 'b'), 1, ('aa', 'b'), 2, ('aaa', 'b'), (15, 18)]
>>> split(regexobj, s, case4sep=S.group0s, case4gap=G.size, case4tail=T.span, maxsplit=3)
[0, ('ab', 'a', 'b'), 1, ('aabb', 'aa', 'b'), 2, ('aaabbb', 'aaa', 'b'), (15, 18)]
>>> split(regexobj, s, case4sep=S.group0s, case4gap=G.size, case4tail=T.span, maxsplit=3, begin=1, end=-8)
[2, ('aabb', 'aa', 'b'), 2, ('a', 'a', None), 0]
>>> split(regexobj, s, case4sep=S.group0s_with_smay_name, case4gap=G.size, case4tail=T.span, maxsplit=3, end=-9)
[0, (('', 'ab'), ('As', 'a'), ('', 'b')), 1, (('', 'aabb'), ('As', 'aa'), ('', 'b')), 2]
>>> split(regexobj, s, case4sep=S.groups, case4gap=G.size, case4tail=T.span, maxsplit=3, output_with_case=True)
[(<OutputCase4gap4re_split.size: 4>, 0), (<OutputCase4sep4re_split.groups: 6>, ('a', 'b')), (<OutputCase4gap4re_split.size: 4>, 1), (<OutputCase4sep4re_split.groups: 6>, ('aa', 'b')), (<OutputCase4gap4re_split.size: 4>, 2), (<OutputCase4sep4re_split.groups: 6>, ('aaa', 'b')), (<OutputCase4tail4re_split.span: 3>, (15, 18))]


>>> 



#]]]'''
__all__ = r'''
split               asif_re__split_
    iter_split      iter_asif_re__split_
        output_case5or_bool_
        OutputCase4tail4re_split
        OutputCase4gap4re_split
        OutputCase4sep4re_split
            S
            G
            T
extract_group0s_with_smay_name5matchobj_
    extract_smay_group_name0s5regexobj_
    extract_group0s5matchobj_


'''.split()#'''
__all__

#from re import finditer
from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
from seed.tiny import check_type_is
from seed.tiny import print_err

from seed.seq_tools.mk_seq_rng import mk_seq_rng, mk_seq_rng__len
from enum import Enum, auto
from itertools import islice

class OutputCase4tail4re_split(Enum):
    'kw:case4tail'
    off = auto()
    group = auto()
        # tail/str if only maxsplit > 0 and len(sep) hit maxsplit
    span = auto()
        # rng<tail>
    size = auto()
        # len(tail)
class OutputCase4gap4re_split(Enum):
    'kw:case4gap'
    off = auto()
    group = auto()
        # gap/str
    span = auto()
        # rng<gap>
    size = auto()
        # len(gap)
class OutputCase4sep4re_split(Enum):
    'kw:case4sep'
    off = auto()
    group = auto()
        # matchobj.group(0) -> sep/str
    span = auto()
        # matchobj.span(0) -> rng<sep>
    size = auto()
        # len(sep)
    matchobj = auto()
        # re.matchobj
    #captured_groups = auto()
    groups = auto()
        # matchobj.groups() -> tuple<may str>
        #    # not include 『0』
    groupdict = auto()
        # matchobj.groupdict() -> {nm:may str}
        # nm@groupdict -> idx@groups
        # idx@groups -> may nm@groupdict
        #   matchobj.re/regexobj.groupindex :: mappingproxy{nm:idx}
        #       mapping group names to group numbers
        #   regexobj.groups :: uint == max idx # (-1+len [0..=max idx])
        #       number of capturing groups # not include 『0』
        #
    group0s = auto()
        #    # include 『0』
    group0s_with_smay_name = auto()
        #    # include 『0』, paired with name
        #

S = OutputCase4sep4re_split
G = OutputCase4gap4re_split
T = OutputCase4tail4re_split

def extract_group0s5matchobj_(matchobj, /):
    '-> group0s/tuple<group<idx>/may str>'
    return (matchobj.group(0), *matchobj.groups())

def extract_group0s_with_smay_name5matchobj_(matchobj, /):
    '-> group0s_with_smay_name/tuple<(smay nm<idx>, group<idx>/may str)>'
    regexobj = matchobj.re
    smay_name0s = extract_smay_group_name0s5regexobj_(regexobj)
    group0s = extract_group0s5matchobj_(matchobj)
    assert len(smay_name0s) == len(group0s)
    return (*zip(smay_name0s, group0s),)
def extract_smay_group_name0s5regexobj_(regexobj, /):
    '-> smay_group_name0s/tuple<smay nm<idx> >'
    num_groups = regexobj.groups
    num_group0s = 1+num_groups
    smay_name0s = ['']*num_group0s
    for nm, idx in regexobj.groupindex.items():
        assert not smay_name0s[idx]
        smay_name0s[idx] = nm
        assert smay_name0s[idx]
    smay_name0s = (*smay_name0s,)
    return smay_name0s

def _mk_tmay_out5xxx_(cls, case4xxx, s, begin4xxx, end4xxx, may_matchobj4xxx, /, *, output_with_case):
    check_type_is(cls, case4xxx)
    assert 0 <= begin4xxx <= end4xxx <= len(s)
    if case4xxx is cls.off:
        return ()
    elif case4xxx is cls.group:
        r = s[begin4xxx:end4xxx]
    elif case4xxx is cls.span:
        r = (begin4xxx, end4xxx)
    elif case4xxx is cls.size:
        r = (end4xxx -begin4xxx)
    else:
        if not cls is S:
            raise 000
        matchobj4xxx = may_matchobj4xxx
        if case4xxx is cls.matchobj:
            r = matchobj4xxx
        elif case4xxx is cls.groups:
            r = matchobj4xxx.groups()
        elif case4xxx is cls.groupdict:
            r = matchobj4xxx.groupdict()
        elif case4xxx is cls.group0s:
            r = extract_group0s5matchobj_(matchobj4xxx)
        elif case4xxx is cls.group0s_with_smay_name:
            r = extract_group0s_with_smay_name5matchobj_(matchobj4xxx)
        else:
            raise 000
        r
    r
    if output_with_case:
        r = (case4xxx, r)
    return (r,)



def _mk_tmay_out5sep_(case4sep, s, begin4sep, end4sep, matchobj4sep, /, **kwds):
    return _mk_tmay_out5xxx_(S, case4sep, s, begin4sep, end4sep, matchobj4sep, **kwds)
def _mk_tmay_out5gap_(case4gap, s, begin4gap, end4gap, /, **kwds):
    return _mk_tmay_out5xxx_(G, case4gap, s, begin4gap, end4gap, None, **kwds)
def _mk_tmay_out5tail_(case4tail, s, begin4tail, end4tail, /, **kwds):
    return _mk_tmay_out5xxx_(T, case4tail, s, begin4tail, end4tail, None, **kwds)
def output_case5or_bool_(cls, case_or_bool, /):
    if type(case_or_bool) is bool:
        off_vs_group = case_or_bool
        if off_vs_group:
            case = cls.group
        else:
            case = cls.off
        case
    else:
        case = case_or_bool
    case
    check_type_is(cls, case)
    return case

def iter_split(regexobj, s, /, *, begin=None, end=None, maxsplit=0, case4sep=S.off, case4gap=G.group, case4tail=None, output_with_case=False):
    check_type_is(bool, output_with_case)

    begin, end = mk_seq_rng(s, begin, end)
    check_int_ge_le(0, len(s), end)
    check_int_ge_le(0, end, begin)
    check_int_ge(0, maxsplit)

    if case4sep is None:
        case4sep = S.off
    else:
        case4sep = output_case5or_bool_(S, case4sep)
    check_type_is(S, case4sep)

    if case4gap is None:
        case4gap = G.group
    else:
        case4gap = output_case5or_bool_(G, case4gap)
    check_type_is(G, case4gap)

    if case4tail is None:
        case4tail = getattr(T, case4gap.name)
    else:
        case4tail = output_case5or_bool_(T, case4tail)
    check_type_is(T, case4tail)


    ######################
    it = regexobj.finditer(s, begin, end)
    if maxsplit > 0:
        it = islice(it, maxsplit)

    kwds = dict(output_with_case=output_with_case)
    pre_end4sep = begin
    i = 0
    for i, matchobj4sep in enumerate(it, 1):
        (begin4sep, end4sep) = matchobj4sep.span(0)
        #if 0b0001:print_err(begin4sep, end4sep)
        begin4gap = pre_end4sep
        end4gap = begin4sep
        yield from _mk_tmay_out5gap_(case4gap, s, begin4gap, end4gap, **kwds)
        yield from _mk_tmay_out5sep_(case4sep, s, begin4sep, end4sep, matchobj4sep, **kwds)
        ######################
        pre_end4sep = end4sep
        ######################
    begin4tail_gap = pre_end4sep
    end4tail_gap = end
    if i == maxsplit > 0:
        #tail
        yield from _mk_tmay_out5tail_(case4tail, s, begin4tail_gap, end4tail_gap, **kwds)
    else:
        #gap
        yield from _mk_tmay_out5gap_(case4gap, s, begin4tail_gap, end4tail_gap, **kwds)
    return
#end-def iter_split(regexobj, s, /, *, begin=None, end=None, maxsplit=0, case4sep=S.off, case4gap=G.group, case4tail=None, output_with_case=False):
def split(regexobj, s, /, *, begin=None, end=None, maxsplit=0, case4sep=S.off, case4gap=G.group, case4tail=None, output_with_case=False):
    kwds = {**locals()}
    del kwds['regexobj']
    del kwds['s']
    return [*iter_split(regexobj, s, **kwds)]







__all__


from seed.for_libs.for_re___split import extract_group0s_with_smay_name5matchobj_, extract_smay_group_name0s5regexobj_, extract_group0s5matchobj_
from seed.for_libs.for_re___split import split, iter_split
from seed.for_libs.for_re___split import split as asif_re__split_, iter_split as iter_asif_re__split_
from seed.for_libs.for_re___split import *
