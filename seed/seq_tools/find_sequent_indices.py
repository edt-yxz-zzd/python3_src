#__all__:goto
r'''[[[
e ../../python3_src/seed/seq_tools/find_sequent_indices.py

seed.seq_tools.find_sequent_indices
py -m nn_ns.app.debug_cmd   seed.seq_tools.find_sequent_indices -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.seq_tools.find_sequent_indices:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> find_sequent_indices_('abbc', 'aabbcc')
(0, 2, 3, 4)
>>> find_sequent_indices_('abbc', 'aabbcc', 1, -1)
(1, 2, 3, 4)
>>> find_sequent_indices_('abbc', 'aabbcc', 1, -2)
Traceback (most recent call last):
    ...
ValueError: substring not found




py_adhoc_call   seed.seq_tools.find_sequent_indices   @f
]]]'''#'''
__all__ = r'''
find_sequent_indices_
    iter_find_sequent_indices_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...


def find_sequent_indices_(elems, whole_seq, begin=None, end=None, /):
    'Iter x -> seq/[x] -> strict_ascend[uint%len(seq)] | ^ValueError'
    js = tuple(iter_find_sequent_indices_(elems, whole_seq, begin, end))
    return js
def iter_find_sequent_indices_(elems, whole_seq, begin=None, end=None, /):
    'Iter x -> seq/[x] -> strict_ascend-Iter uint%len(seq) | ^ValueError'
    (begin, end, _1) = slice(begin, end, 1).indices(len(whole_seq))
    for x in elems:
        j = whole_seq.index(x, begin, end)
            # ^ValueError
        yield j
        begin = 1+j

__all__
from seed.seq_tools.find_sequent_indices import find_sequent_indices_, iter_find_sequent_indices_
from seed.seq_tools.find_sequent_indices import *
