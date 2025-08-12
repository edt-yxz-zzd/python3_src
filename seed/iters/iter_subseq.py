#__all__:goto
r'''[[[
e ../../python3_src/seed/iters/iter_subseq.py
see:
    itertools.islice
    seed.iters.iter_seq.(iter_seq,IterSeq)
view ../../python3_src/seed/iters/iter_seq.py


seed.iters.iter_subseq
py -m nn_ns.app.debug_cmd   seed.iters.iter_subseq -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.iters.iter_subseq:__doc__ -ht # -ff -df

[[
]]


######################
iter_seq
def iter_seq(seq, reversed=False, reversed_in=False):
class IterSeq(seq, reversed_out=False, reversed_in=False):
>>> from seed.iters.iter_seq import (iter_seq, IterSeq)
>>> s = '0123456789'
>>> x = iter_seq(s)
>>> iter(x) #doctest: +ELLIPSIS
<iterator object at 0x...>
>>> z = x[1:-3:2]
>>> not iter(z) is z
True
>>> x #doctest: +ELLIPSIS
<seed.iters.iter_seq.IterSeq object at 0x...>
>>> z #doctest: +ELLIPSIS
<seed.iters.iter_seq.IterSeq_Slices object at 0x...>
>>> y = iter(z)
>>> iter(y) is y
True
>>> next(y)
'1'
>>> y #doctest: +ELLIPSIS
<generator object IterSeq.iter at 0x...>
>>> list(y)
['3', '5']

######################
iter_subseq__opaque_
def iter_subseq__opaque_(seq, /, begin=None, end=None, step=None):
>>> y = iter_subseq__opaque_(s, 1,-3,2)
>>> iter(y) is y
True
>>> next(y)
'1'
>>> y #doctest: +ELLIPSIS
<map object at 0x...>
>>> list(y)
['3', '5']


>>> y = iter_subseq__opaque_(s, step=-3)
>>> iter(y) is y
True
>>> next(y)
'9'
>>> y #doctest: +ELLIPSIS
<map object at 0x...>
>>> list(y)
['6', '3', '0']

>>> y = iter_subseq__opaque_(s, step=-1)
>>> iter(y) is y
True
>>> next(y)
'9'
>>> y #doctest: +ELLIPSIS
<map object at 0x...>
>>> list(y)
['8', '7', '6', '5', '4', '3', '2', '1', '0']

>>> y = iter_subseq__opaque_(s)
>>> iter(y) is y
True
>>> next(y)
'0'
>>> y #doctest: +ELLIPSIS
<map object at 0x...>
>>> list(y)
['1', '2', '3', '4', '5', '6', '7', '8', '9']





######################
iter_subseq__transparent_
def iter_subseq__transparent_(seq, /, begin=None, end=None, step=None):
>>> y = iter_subseq__transparent_(s, 1,-3,2)
>>> y
IterSubseq__transparent('0123456789', 1, 7, 2, 1)
>>> iter(y) is y
True
>>> next(y)
'1'
>>> y
IterSubseq__transparent('0123456789', 1, 7, 2, 3)
>>> list(y)
['3', '5']
>>> y
IterSubseq__transparent('0123456789', 1, 7, 2, 7)



>>> y = iter_subseq__transparent_(s, step=-3)
>>> y
IterSubseq__transparent('0123456789', 9, -1, -3, 9)
>>> iter(y) is y
True
>>> next(y)
'9'
>>> y
IterSubseq__transparent('0123456789', 9, -1, -3, 6)
>>> list(y)
['6', '3', '0']
>>> y
IterSubseq__transparent('0123456789', 9, -1, -3, -1)



>>> y = iter_subseq__transparent_(s, step=-1)
>>> y
IterSubseq__transparent('0123456789', 9, -1, -1, 9)
>>> iter(y) is y
True
>>> next(y)
'9'
>>> y
IterSubseq__transparent('0123456789', 9, -1, -1, 8)
>>> list(y)
['8', '7', '6', '5', '4', '3', '2', '1', '0']
>>> y
IterSubseq__transparent('0123456789', 9, -1, -1, -1)



>>> y = iter_subseq__transparent_(s, _step_eq1_plain=True)
>>> y
IterSubseq__transparent('0123456789', 0, 10, 1, 0, _step_eq1_plain = True)
>>> iter(y) is y
True
>>> next(y)
'0'
>>> y
IterSubseq__transparent('0123456789', 0, 10, 1, 1, _step_eq1_plain = True)
>>> list(y)
['1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> y
IterSubseq__transparent('0123456789', 0, 10, 1, 10, _step_eq1_plain = True)




>>> y = iter_subseq__transparent_(s)
>>> y
IterSubseq__transparent__step_eq1('0123456789', 0, 10, 0)
>>> iter(y) is y
True
>>> next(y)
'0'
>>> y
IterSubseq__transparent__step_eq1('0123456789', 0, 10, 1)
>>> list(y)
['1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> y
IterSubseq__transparent__step_eq1('0123456789', 0, 10, 10)








>>> range(1, 7, 5)
range(1, 7, 5)
>>> [*range(1, 7, 5)]
[1, 6]
>>> y = iter_subseq__transparent_(s, 1,-3,5)
>>> y
IterSubseq__transparent('0123456789', 1, 7, 5, 1)
>>> next(y)
'1'
>>> y
IterSubseq__transparent('0123456789', 1, 7, 5, 6)
>>> list(y)
['6']
>>> y
IterSubseq__transparent('0123456789', 1, 7, 5, 7)


>>> y = iter_subseq__transparent_(s, end=-5, step=-7)
>>> y
IterSubseq__transparent('0123456789', 9, 5, -7, 9)
>>> y = iter_subseq__transparent_(s, step=-7)
>>> y #not:IterSubseq__transparent('0123456789', 9, -5, -7, 9)
IterSubseq__transparent('0123456789', 9, -1, -7, 9)
>>> next(y)
'9'
>>> y
IterSubseq__transparent('0123456789', 9, -1, -7, 2)
>>> next(y)
'2'
>>> y
IterSubseq__transparent('0123456789', 9, -1, -7, -1)
>>> next(y)
Traceback (most recent call last):
    ...
StopIteration
>>> y.idx = 9
>>> y
IterSubseq__transparent('0123456789', 9, -1, -7, 9)
>>> y.idx = 2
>>> y
IterSubseq__transparent('0123456789', 9, -1, -7, 2)
>>> y.idx = -1
>>> y
IterSubseq__transparent('0123456789', 9, -1, -7, -1)
>>> y.idx = -8
>>> y
IterSubseq__transparent('0123456789', 9, -1, -7, 2)
>>> y.idx = 10
Traceback (most recent call last):
    ...
IndexError: 10
>>> y.idx = 8
Traceback (most recent call last):
    ...
IndexError: 8
>>> y.idx = 7
Traceback (most recent call last):
    ...
IndexError: 7
>>> y.idx = 6
Traceback (most recent call last):
    ...
IndexError: 6
>>> y.idx = 5
Traceback (most recent call last):
    ...
IndexError: 5
>>> y.idx = 4
Traceback (most recent call last):
    ...
IndexError: 4
>>> y.idx = 3
Traceback (most recent call last):
    ...
IndexError: 3
>>> y.idx = 1
Traceback (most recent call last):
    ...
IndexError: 1
>>> y.idx = 0
Traceback (most recent call last):
    ...
IndexError: 0
>>> y.idx = -2
Traceback (most recent call last):
    ...
IndexError: -2
>>> y.idx = -3
Traceback (most recent call last):
    ...
IndexError: -3
>>> y.idx = -4
Traceback (most recent call last):
    ...
IndexError: -4
>>> y.idx = -5
Traceback (most recent call last):
    ...
IndexError: -5
>>> y.idx = -6
Traceback (most recent call last):
    ...
IndexError: -6
>>> y.idx = -7
Traceback (most recent call last):
    ...
IndexError: -7
>>> y.idx = -9
Traceback (most recent call last):
    ...
IndexError: -9
>>> y.idx = -10
Traceback (most recent call last):
    ...
IndexError: -10


######################

]]]'''#'''
__all__ = r'''
iter_subseq__opaque_
iter_subseq__transparent_
    IterSubseq__transparent
        IterSubseq__transparent__step_eq1
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from operator import __index__
from functools import cached_property
from seed.tiny_.types5py import curry1
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
#.
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
___end_mark_of_excluded_global_names__0___ = ...



def iter_subseq__opaque_(seq, /, begin=None, end=None, step=None):
    'seq/[x] -> begin -> end -> step -> iter(seq[begin:end:step])'
    #g = seq.__getitem__
    g = curry1(type(seq).__getitem__, seq)
    return map(g, range(len(seq))[begin:end:step])
def iter_subseq__transparent_(seq, /, begin=None, end=None, step=None, **kwds):
    'seq/[x] -> begin -> end -> step -> iter(seq[begin:end:step]){.idx}'
    return IterSubseq__transparent(seq, begin, end, step, **kwds)
class IterSubseq__transparent:
    def __new__(cls, seq, /, begin=None, end=None, step=None, idx=None, _step_eq1_plain=False):
        if not _step_eq1_plain and cls is __class__ and (step is None or step == 1):
            return IterSubseq__transparent__step_eq1(seq, begin, end, idx)
        return super(__class__, cls).__new__(cls)
    def __init__(sf, seq, /, begin=None, end=None, step=None, idx=None, _step_eq1_plain=False):
        #discard:_step_eq1_plain#used in __new__()

        sf._ls = seq
        sf._rg = range(len(seq))[begin:end:step]
        if idx is None:
            sf._i = sf.begin
        else:
            sf.idx = idx
            sf._i
    @property
    def seq(sf, /):
        return sf._ls
    @property
    def indices4subseq(sf, /):
        return sf._rg
    @cached_property
    def begin(sf, /):
        return sf._rg.start
    @cached_property
    def end(sf, /):
        return sf._rg.stop
    @cached_property
    def step(sf, /):
        return sf._rg.step

    @property
    def idx(sf, /):
        '-> uint%(1+len(sf.seq)) # 『transparent』'
        return sf._i
    @idx.setter
    def idx(sf, i, /):
        'int{-len(sf.seq)..=len(sf.seq)} -> None|^IndexError'
        i = __index__(i)
        if i == sf.end:
            # allow:[sf.end == -1 < 0] if [sf.step < 0]
            sf._i = i
            return
        L = len(sf._ls)
        u = i + L if i < 0 else i
        #bug:sf._rg.index(u) #^IndexError
            # !! u may be sf.end
        if not (0 <= u <= L):
            raise IndexError(i)
        if not u == sf.end:
            (q, r) = divmod(u -sf.begin, sf.step)
            if not (r==0 and 0 <= q < len(sf._rg)):
                raise IndexError(i)
        sf._i = u
        return

    def __repr__(sf, /):
        args = (sf.seq, sf.begin, sf.end, sf.step, sf.idx)
        if sf.step == 1:
            return repr_helper(sf, *args, _step_eq1_plain=True)
        return repr_helper(sf, *args)
    def __iter__(sf, /):
        return sf
    def __next__(sf, /):
        i = sf._i
        e = sf.end
        if i == e:
            raise StopIteration
        x = sf._ls[i]
        t = sf.step
        i += t
        f = min if t > 0 else max
        sf._i = f(i, e)
        return x
#end-class IterSubseq__transparent:
class IterSubseq__transparent__step_eq1(IterSubseq__transparent):
    #@override
    def __init__(sf, seq, /, begin=None, end=None, idx=None):
        super().__init__(seq, begin, end, None, idx)
    @property
    #@override
    def idx(sf, /):
        '-> uint%(1+len(sf.seq)) # 『transparent』'
        return sf._i
    @idx.setter
    #@override
    def idx(sf, i, /):
        'int{-len(sf.seq)..=len(sf.seq)} -> None|^IndexError'
        i = __index__(i)
        L = len(sf._ls)
        u = i + L if i < 0 else i
        #bug:sf._rg.index(u) #^IndexError
            # !! u may be sf.end
        if not (sf.begin <= u <= sf.end):
            raise IndexError(i)
        sf._i = u
        return

    #@override
    def __repr__(sf, /):
        return repr_helper(sf, sf.seq, sf.begin, sf.end, sf.idx)
    #@override
    def __next__(sf, /):
        i = sf._i
        e = sf.end
        if i == e:
            raise StopIteration
        x = sf._ls[i]
        sf._i = i+1
        return x
#end-class IterSubseq__transparent__step_eq1(IterSubseq__transparent):

__all__
#[iter_subseq__opaque_,iter_subseq__transparent_] = lazy_import4funcs_('seed.iters.iter_subseq', 'iter_subseq__opaque_,iter_subseq__transparent_', __name__)
from seed.iters.iter_subseq import iter_subseq__opaque_, iter_subseq__transparent_, IterSubseq__transparent
from seed.iters.iter_subseq import *
