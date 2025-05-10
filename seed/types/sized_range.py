#__all__:goto
#fail:since py.len() => OverflowError: cannot fit 'int' into an index-sized integer
#   #beside range.__len__() => OverflowError: Python int too large to convert to C ssize_t
r'''[[[
e ../../python3_src/seed/types/sized_range.py

seed.types.sized_range
py -m nn_ns.app.debug_cmd   seed.types.sized_range -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.sized_range:__doc__ -ht # -ff -df

[[
since:
view ../../python3_src/seed/seq_tools/bisearch.py
# e ../lots/NOTE/Python/python-bug/len-bug.txt
>>> len(range(2**80))
Traceback (most recent call last):
    ...
OverflowError: Python int too large to convert to C ssize_t
>>> range(2**80).__len__()
Traceback (most recent call last):
    ...
OverflowError: Python int too large to convert to C ssize_t

]]


>>> class T(range):...
Traceback (most recent call last):
    ...
TypeError: type 'range' is not an acceptable base type

>>> SizedSeq(range(2**80)).__len__() == 2**80
True

fail...
>>> len(SizedSeq(range(2**80))) == 2**80
Traceback (most recent call last):
    ...
OverflowError: cannot fit 'int' into an index-sized integer


py_adhoc_call   seed.types.sized_range   @f
from seed.types.sized_range import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.lang.calc_len_of_py_range_ import calc_len_of_py_range_
from collections.abc import Sequence
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

class SizedSeq(Sequence):
    def __init__(sf, ls, sz=None, /):
        if sz is None:
            try:
                sz = len(ls)
            except OverflowError:
                if isinstance(ls, range):
                    sz = calc_len_of_py_range_(ls)
                else:
                    raise
                sz
            sz
        sz
        sf._sz = sz
        sf._ls = ls
    def __repr__(sf, /):
        return repr_helper(sf, sf._ls, sf._sz)
    def __len__(sf, /):
        return (sf._sz)
    def __bool__(sf, /):
        return bool(sf._sz)
    def __getitem__(sf, k, /):
        return sf._ls[k]



__all__
from seed.types.sized_range import *
