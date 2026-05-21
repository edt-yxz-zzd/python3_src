#__all__:goto
r'''[[[
e ../../python3_src/seed/seq_tools/find.py

seed.seq_tools.find
py -m nn_ns.app.debug_cmd   seed.seq_tools.find -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.seq_tools.find:__doc__ -ht # -ff -df
#######

[[
list.index
has no:list.find
]]


'#'; __doc__ = r'#'
>>> find7seq_([3, 5, 6, 7], 6)
2
>>> find7seq_([3, 5, 6, 7], 6, 2)
2
>>> find7seq_([3, 5, 6, 7], 6, 2, -1)
2
>>> find7seq_([3, 5, 6, 7], 6, 3)
-1
>>> find7seq_([3, 5, 6, 7], 6, 0, -2)
-1

>>> find7iter_(iter([3, 5, 6, 7]), 6)
2
>>> find7iter_(iter([3, 5, 6, 7]), 6, offset=1000)
1002
>>> find7iter_(iter([3, 5, 6, 7]), 999)
-1


py_adhoc_call   seed.seq_tools.find   @f
]]]'''#'''
__all__ = r'''
find7seq_
find7iter_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...

def find7iter_(iterable, x, /, *, offset=0):
    'Iter x -> x -> imay_idx'
    xs = [x]
    for j, y in enumerate(iterable, offset):
        if y in xs:
            return j
    return -1

def find7seq_(seq, x, begin=None, end=None, /):
    '[x] -> x -> imay_idx'
    try:
        return seq.index(x, begin, end)
            # None => ^TypeError: slice indices must be integers or have an __index__ method
    except ValueError:
        return -1
def find7seq_(seq, x, /, *args):
    try:
        return seq.index(x, *args)
    except ValueError:
        return -1

__all__
from seed.seq_tools.find import find7seq_, find7iter_
from seed.seq_tools.find import *
