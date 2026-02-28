#__all__:goto
r'''[[[
e ../../python3_src/seed/types/view/SeqCatView.py

seed.types.view.SeqCatView
py -m nn_ns.app.debug_cmd   seed.types.view.SeqCatView -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.view.SeqCatView:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'

>>> SeqCatView()
SeqCatView()
>>> SeqCatView([])
SeqCatView()
>>> ls = SeqCatView([(0, 1+39363, range(1+39363)), (1+39363-38039, 70070-39363, range(38039, 1+70070))])
>>> ls
SeqCatView(((0, 39364, range(0, 39364)), (1325, 30707, range(38039, 70071))))
>>> len(ls)
70071
>>> ls[0]
0
>>> ls[39363]
39363
>>> ls[39364]
39364
>>> ls[39365]
39365
>>> ls[39360:39367] == tuple(range(39360, 39367))
True
>>> ls[-1]
70070
>>> it = iter(ls)
>>> next(it)
0
>>> next(it)
1
>>> it = reversed(ls)
>>> next(it)
70070
>>> next(it)
70069


>>> from seed.types.Symbol import P
>>> __name__
'seed.types.view.SeqCatView'
>>> ls = SeqCatView(smay_repr='P.seed.types.view.SeqCatView().ls')
>>> ls
P.seed.types.view.SeqCatView().ls
>>> ls is eval(repr(ls))
Traceback (most recent call last):
    ...
AttributeError: module 'seed.types.view.SeqCatView' has no attribute 'ls'

py_adhoc_call   seed.types.view.SeqCatView   @f
]]]'''#'''
__all__ = r'''
SeqCatView
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from collections.abc import Sequence
from seed.helper.repr_input import repr_helper
#
from bisect import bisect_right
from itertools import accumulate
from seed.tiny_.check import check_type_le, check_type_is, check_int_ge, check_int_ge_le, check_int_ge_lt
___end_mark_of_excluded_global_names__0___ = ...

class SeqCatView(Sequence):
    def __init__(sf, triples7begin_size_seq=(), /, *, smay_repr=''):
        check_type_is(str, smay_repr)
        triples7begin_size_seq = tuple((begin, size, seq) for (begin, size, seq) in triples7begin_size_seq)
        for (begin, size, seq) in triples7begin_size_seq:
            check_type_le(Sequence, seq)
            check_int_ge_le(0, len(seq), begin)
            check_int_ge_le(0, len(seq)-begin, size)
        j2end = tuple(accumulate(size for (begin, size, seq) in triples7begin_size_seq))
        sf._sz = 0 if not j2end else j2end[-1]
        sf._j2end = j2end
        sf._ts = triples7begin_size_seq
        sf._smay_repr = smay_repr
    def at(sf, k, /):
        check_int_ge_lt(0, len(sf), k)
        j2end = sf._j2end
        j = bisect_right(j2end, k)
        (begin, size, seq) = sf._ts[j]
        #bug:_k = k -begin
        #assert 0 <= _k < size, (k, j2end, j, (begin, size, seq), _k)
        _end = j2end[j-1] if j else 0
        _k = k -_end +begin
        #assert begin <= _k < begin+size, (k, j2end, j, (begin, size, seq), _k)
        return seq[_k]

    def __getitem__(sf, j_or_slice, /):
        j_or_js = range(len(sf))[j_or_slice]
        if type(j_or_js) is range:
            js = j_or_js
            return tuple(map(sf.at, js))
        j = j_or_js
        return sf.at(j)



    def __repr__(sf, /):
        smay_repr = sf._smay_repr
        if smay_repr:
            return smay_repr
        if not sf:
            return repr_helper(sf)
        return repr_helper(sf, sf._ts)
    def __len__(sf, /):
        return sf._sz




__all__
from seed.types.view.SeqCatView import SeqCatView
    #SeqCatView(triples7begin_size_seq)
    #   :: [(begin, size, seq)] -> SeqCatView
from seed.types.view.SeqCatView import *
