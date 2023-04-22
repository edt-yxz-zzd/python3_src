#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_re.py

xstring :: str|bytes-like

seed.for_libs.for_re
py -m nn_ns.app.debug_cmd   seed.for_libs.for_re -x
py -m nn_ns.app.doctest_cmd seed.for_libs.for_re:__doc__ -ff -v
py -m nn_ns.app.doctest_cmd seed.for_libs.for_re!
py_adhoc_call   seed.for_libs.for_re   @f


def iter_find_matchobjs_(regex, may_minlen4match, may_maxlen4match, xstring, may_first4both, may_last4begin, may_last4end, /, *, overlap:bool):
>>> from seed.for_libs.for_re import iter_find_matchobjs_, iter_find_spans_, list_find_spans_
>>> import re
>>> regex = re.compile(r'aaa|aba|bb')
>>> xstring = 'aaaaabababbbb'
>>> regex.match(xstring)
<re.Match object; span=(0, 3), match='aaa'>

#>>> list_find_spans_(regex, may_minlen4match, may_maxlen4match, xstring, may_first4both, may_last4begin, may_last4end, overlap=overlap)
>>> list_find_spans_(regex, None, None, xstring, None, None, None, overlap=False)
[(0, 3), (4, 7), (9, 11), (11, 13)]
>>> list_find_spans_(regex, None, None, xstring, None, None, None, overlap=True)
[(0, 3), (1, 4), (2, 5), (4, 7), (6, 9), (9, 11), (10, 12), (11, 13)]





>>> list_find_spans_(regex, None, None, xstring, None, None, None, overlap=False)
[(0, 3), (4, 7), (9, 11), (11, 13)]
>>> list_find_spans_(regex, 2, None, xstring, None, None, None, overlap=False)
[(0, 3), (4, 7), (9, 11), (11, 13)]
>>> list_find_spans_(regex, 3, None, xstring, None, None, None, overlap=False)
Traceback (most recent call last):
    ...
ValueError: logic-err: len(matched sub-xstring) not in expected range: 2 not between [3..=13]
>>> list_find_spans_(regex, None, 3, xstring, None, None, None, overlap=False)
[(0, 3), (4, 7), (9, 11), (11, 13)]
>>> list_find_spans_(regex, None, 2, xstring, None, None, None, overlap=False)
Traceback (most recent call last):
    ...
ValueError: logic-err: len(matched sub-xstring) not in expected range: 3 not between [0..=2]
>>> list_find_spans_(regex, None, None, xstring, 1, None, None, overlap=False)
[(1, 4), (4, 7), (9, 11), (11, 13)]
>>> list_find_spans_(regex, None, None, xstring, 2, None, None, overlap=False)
[(2, 5), (6, 9), (9, 11), (11, 13)]
>>> list_find_spans_(regex, None, None, xstring, 3, None, None, overlap=False)
[(4, 7), (9, 11), (11, 13)]
>>> list_find_spans_(regex, None, None, xstring, 4, None, None, overlap=False)
[(4, 7), (9, 11), (11, 13)]
>>> list_find_spans_(regex, None, None, xstring, 5, None, None, overlap=False)
[(6, 9), (9, 11), (11, 13)]
>>> list_find_spans_(regex, None, None, xstring, None, 0, None, overlap=False)
[(0, 3)]
>>> list_find_spans_(regex, None, None, xstring, None, 3, None, overlap=False)
[(0, 3)]
>>> list_find_spans_(regex, None, None, xstring, None, 4, None, overlap=False)
[(0, 3), (4, 7)]
>>> list_find_spans_(regex, None, None, xstring, None, 8, None, overlap=False)
[(0, 3), (4, 7)]
>>> list_find_spans_(regex, None, None, xstring, None, 9, None, overlap=False)
[(0, 3), (4, 7), (9, 11)]
>>> list_find_spans_(regex, None, None, xstring, None, 10, None, overlap=False)
[(0, 3), (4, 7), (9, 11)]
>>> list_find_spans_(regex, None, None, xstring, None, 11, None, overlap=False)
[(0, 3), (4, 7), (9, 11), (11, 13)]
>>> list_find_spans_(regex, None, None, xstring, None, None, 2, overlap=False)
[]
>>> list_find_spans_(regex, None, None, xstring, None, None, 3, overlap=False)
[(0, 3)]
>>> list_find_spans_(regex, None, None, xstring, None, None, 6, overlap=False)
[(0, 3)]
>>> list_find_spans_(regex, None, None, xstring, None, None, 7, overlap=False)
[(0, 3), (4, 7)]
>>> list_find_spans_(regex, None, None, xstring, None, None, None, overlap=False)
[(0, 3), (4, 7), (9, 11), (11, 13)]






>>> list_find_spans_(regex, None, None, xstring, None, None, None, overlap=True)
[(0, 3), (1, 4), (2, 5), (4, 7), (6, 9), (9, 11), (10, 12), (11, 13)]
>>> list_find_spans_(regex, 2, None, xstring, None, None, None, overlap=True)
[(0, 3), (1, 4), (2, 5), (4, 7), (6, 9), (9, 11), (10, 12), (11, 13)]
>>> list_find_spans_(regex, 3, None, xstring, None, None, None, overlap=True)
Traceback (most recent call last):
    ...
ValueError: logic-err: len(matched sub-xstring) not in expected range: 2 not between [3..=13]
>>> list_find_spans_(regex, None, 3, xstring, None, None, None, overlap=True)
[(0, 3), (1, 4), (2, 5), (4, 7), (6, 9), (9, 11), (10, 12), (11, 13)]
>>> list_find_spans_(regex, None, 2, xstring, None, None, None, overlap=True)
Traceback (most recent call last):
    ...
ValueError: logic-err: len(matched sub-xstring) not in expected range: 3 not between [0..=2]
>>> list_find_spans_(regex, None, None, xstring, 1, None, None, overlap=True)
[(1, 4), (2, 5), (4, 7), (6, 9), (9, 11), (10, 12), (11, 13)]
>>> list_find_spans_(regex, None, None, xstring, 11, None, None, overlap=True)
[(11, 13)]
>>> list_find_spans_(regex, None, None, xstring, 12, None, None, overlap=True)
[]
>>> list_find_spans_(regex, None, None, xstring, None, 0, None, overlap=True)
[(0, 3)]
>>> list_find_spans_(regex, None, None, xstring, None, 1, None, overlap=True)
[(0, 3), (1, 4)]
>>> list_find_spans_(regex, None, None, xstring, None, 10, None, overlap=True)
[(0, 3), (1, 4), (2, 5), (4, 7), (6, 9), (9, 11), (10, 12)]
>>> list_find_spans_(regex, None, None, xstring, None, 11, None, overlap=True)
[(0, 3), (1, 4), (2, 5), (4, 7), (6, 9), (9, 11), (10, 12), (11, 13)]
>>> list_find_spans_(regex, None, None, xstring, None, None, -1, overlap=True)
[(0, 3), (1, 4), (2, 5), (4, 7), (6, 9), (9, 11), (10, 12)]
>>> list_find_spans_(regex, None, None, xstring, None, None, -2, overlap=True)
[(0, 3), (1, 4), (2, 5), (4, 7), (6, 9), (9, 11)]
>>> list_find_spans_(regex, None, None, xstring, None, None, 4, overlap=True)
[(0, 3), (1, 4)]
>>> list_find_spans_(regex, None, None, xstring, None, None, 3, overlap=True)
[(0, 3)]
>>> list_find_spans_(regex, None, None, xstring, None, None, 2, overlap=True)
[]
>>> list_find_spans_(regex, None, None, xstring, None, None, None, overlap=True)
[(0, 3), (1, 4), (2, 5), (4, 7), (6, 9), (9, 11), (10, 12), (11, 13)]


#]]]'''
__all__ = r'''
iter_find_matchobjs_
    iter_find_spans_
    list_find_spans_

    prepare4finditer1
    prepare4finditer2
    check_may_int
'''.split()#'''
__all__


from seed.seq_tools.mk_seq_rng import mk_seq_rng, mk_seq_rng__len
import re
from seed.tiny import check_type_is, check_uint, null_iter, ifNone


def check_may_int(mi, /):
    if not mi is None:
        check_type_is(int, mi)
def prepare4finditer1(may_minlen4match, may_maxlen4match, len_xstring, may_first4both, may_last4begin, may_last4end, /):
    check_may_int(may_minlen4match)
    check_may_int(may_maxlen4match)
    (first4both, last4begin) = mk_seq_rng__len(len_xstring, may_first4both, may_last4begin)
    1;   del may_first4both, may_last4begin
    (first4both, last4end) = mk_seq_rng__len(len_xstring, first4both, may_last4end)
    1;   del may_last4end

    min_min = 0
    minlen4match = max(min_min, ifNone(may_minlen4match, min_min))
    1;   del may_minlen4match
    max_max = last4end-first4both
    maxlen4match = max(-1, min(max_max, ifNone(may_maxlen4match, max_max)))
    1;   del may_maxlen4match
    assert maxlen4match >= -1
    assert minlen4match >= 0
    return (minlen4match, maxlen4match, first4both, last4begin, last4end)
def prepare4finditer2(minlen4match, maxlen4match, len_xstring, first4both, last4begin, last4end, /, *, overlap:bool):
    check_type_is(bool, overlap)
    check_type_is(int, maxlen4match)
        #allow [maxlen4match < 0]
    check_uint(minlen4match)
    check_uint(first4both)
    check_uint(last4begin)
    check_uint(last4end)
    check_uint(len_xstring)

    if not (minlen4match <= maxlen4match and first4both <= last4begin and first4both <= last4end):
        return False
    if maxlen4match == 0:
        overlap = False
    last4end = min(last4end, last4begin+maxlen4match)
    #xxx: last4begin = min(last4begin, last4end-maxlen4match)
    #   len4match may be 0
    last4begin = min(last4begin, last4end-minlen4match)
    if not (first4both <= last4begin):
        return False
    assert 0 <= minlen4match <= maxlen4match
    assert maxlen4match > 0 or not overlap
    assert 0 <= first4both <= last4begin <= len_xstring
    assert 0 <= first4both <= last4end <= len_xstring
    assert last4begin+minlen4match <= last4end <= last4begin+maxlen4match
    return (minlen4match, maxlen4match, first4both, last4begin, last4end, overlap)

def list_find_spans_(regex, may_minlen4match, may_maxlen4match, xstring, may_first4both, may_last4begin, may_last4end, /, *, overlap:bool):
    it = iter_find_spans_(regex, may_minlen4match, may_maxlen4match, xstring, may_first4both, may_last4begin, may_last4end, overlap=overlap)
    return [*it]
def iter_find_spans_(regex, may_minlen4match, may_maxlen4match, xstring, may_first4both, may_last4begin, may_last4end, /, *, overlap:bool):
    it = iter_find_matchobjs_(regex, may_minlen4match, may_maxlen4match, xstring, may_first4both, may_last4begin, may_last4end, overlap=overlap)
    return (m.span(0) for m in it)

re.finditer
def iter_find_matchobjs_(regex, may_minlen4match, may_maxlen4match, xstring, may_first4both, may_last4begin, may_last4end, /, *, overlap:bool):
    '-> re.matchobj  #extend re.finditer with `overlap`'
    (minlen4match, maxlen4match, first4both, last4begin, last4end) = prepare4finditer1(may_minlen4match, may_maxlen4match, len(xstring), may_first4both, may_last4begin, may_last4end)

    it = _find_iter(regex, minlen4match, maxlen4match, xstring, first4both, last4begin, last4end, overlap=overlap)
    assert iter(it) is it
    return it
def _find_iter(regex, minlen4match, maxlen4match, xstring, first4both, last4begin, last4end, /, *, overlap:bool):
    regex.fullmatch #check
    xstring.find #check
    xstring[:0] #check
    x = prepare4finditer2(minlen4match, maxlen4match, len(xstring), first4both, last4begin, last4end, overlap=overlap)
    if x is False:
        return null_iter
    (minlen4match, maxlen4match, first4both, last4begin, last4end, overlap) = x
    #print(x)
    f = _find_iter__overlap if overlap else _find_iter__nonoverlap
    return f(regex, minlen4match, maxlen4match, xstring, first4both, last4begin, last4end)

def _m2out(minlen4match, maxlen4match, m, /):
    begin, end = m.span(0)
    len4match = end-begin
    if not minlen4match <= len4match <= maxlen4match:raise ValueError(f'logic-err: len(matched sub-xstring) not in expected range: {len4match} not between [{minlen4match}..={maxlen4match}]')
    return (len4match, begin, end)

def _find_iter__nonoverlap(regex, minlen4match, maxlen4match, xstring, first4both, last4begin, last4end, /):
    assert maxlen4match >= 0
    for m in regex.finditer(xstring, first4both, last4end):
        (len4match, begin, end) = _m2out(minlen4match, maxlen4match, m)
        if not begin <= last4begin:break
        yield m
        if begin == last4begin:break

def _find_iter__overlap(regex, minlen4match, maxlen4match, xstring, first4both, last4begin, last4end, /):
    assert maxlen4match > 0
    begin = first4both
    while begin <= last4begin:
        if begin == last4begin:
            m = regex.match(xstring, begin, last4end)
        else:
            m = regex.search(xstring, begin, last4end)
        if m is None:break
        (len4match, begin, end) = _m2out(minlen4match, maxlen4match, m)
        if not begin <= last4begin:break
        yield m
        begin += 1


__all__


from seed.for_libs.for_re import iter_find_matchobjs_, iter_find_spans_, list_find_spans_
from seed.for_libs.for_re import *
