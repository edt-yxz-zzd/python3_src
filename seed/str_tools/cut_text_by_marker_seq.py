#__all__:goto
r'''[[[
e ../../python3_src/seed/str_tools/cut_text_by_marker_seq.py


seed.str_tools.cut_text_by_marker_seq
py -m nn_ns.app.debug_cmd   seed.str_tools.cut_text_by_marker_seq -x
py -m nn_ns.app.doctest_cmd seed.str_tools.cut_text_by_marker_seq:__doc__ -ht


>>> _txt0 = r"""
... abc
... :mmm:begin
... 666999
... :mmm:end
... xyz
... """#"""

>>> _b_mr = ':mmm:begin'
>>> _e_mr = ':mmm:end'
>>> _ans = ['\nabc\n', '\n666999\n', '\nxyz\n', ]

>>> assert cut_text_by_marker_seq(_txt0, _b_mr, _e_mr) == _ans
>>> assert strip_text_by_marker_pair(_txt0, _b_mr, _e_mr) == _ans[1]




#]]]'''
__all__ = r'''
cut_text_by_marker_seq
    strip_text_by_marker_pair
'''.split()#'''
__all__

def strip_text_by_marker_pair(txt, begin_marker, end_marker, /):
    _, s, _ = cut_text_by_marker_seq(txt, begin_marker, end_marker)
    return s
def cut_text_by_marker_seq(txt, /, *markers):
    ss = []
    i = 0
    for marker in markers:
        j = txt.index(marker, i)
        ss.append(txt[i:j])
        i = j+len(marker)
    ss.append(txt[i:])
    assert len(ss) == len(markers)+1
    return ss
assert cut_text_by_marker_seq('abcdefg', *'bdf') == [*'aceg']
assert cut_text_by_marker_seq('abcde', *'bd') == [*'ace']
assert strip_text_by_marker_pair('abcde', *'bd') == 'c'

__all__
from seed.str_tools.cut_text_by_marker_seq import cut_text_by_marker_seq, strip_text_by_marker_pair
from seed.str_tools.cut_text_by_marker_seq import *
