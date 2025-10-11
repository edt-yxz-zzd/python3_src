#__all__:goto
#TODO:double_ended_inf_len_seq idx/int 双端无穷+偏移
r'''[[[
e ../../python3_src/seed/seq_tools/InfLenSeqWithRecurringPeriod.py

seed.seq_tools.InfLenSeqWithRecurringPeriod
py -m nn_ns.app.debug_cmd   seed.seq_tools.InfLenSeqWithRecurringPeriod -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.seq_tools.InfLenSeqWithRecurringPeriod:__doc__ -ht # -ff -df
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.seq_tools.InfLenSeqWithRecurringPeriod:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
]]


'#'; __doc__ = r'#'

######################
>>> from itertools import islice
>>> ls = InfLenSeqWithRecurringPeriod('abc', '0123456')
>>> ls
InfLenSeqWithRecurringPeriod('abc', '0123456')

>>> ls = mk_inf_len_seq_('abc', '0123456')
>>> ls
InfLenSeqWithRecurringPeriod('abc', '0123456')

__iter__
>>> [*islice(iter(ls), 0, 14)]
['a', 'b', 'c', '0', '1', '2', '3', '4', '5', '6', '0', '1', '2', '3']

__getitem__ slice ascending
>>> ls[0:14]
'abc01234560123'
>>> ls[:14]
'abc01234560123'
>>> ls[0:]
Traceback (most recent call last):
    ...
TypeError: <class 'NoneType'>
>>> ls[:34:5]
'a205316'

__getitem__ slice descending
>>> ls[:34:-5]
Traceback (most recent call last):
    ...
TypeError: <class 'NoneType'>
>>> ls[0:34:-5]
''
>>> ls[33::-5]
'2461350'
>>> ls[33:-1:-5]
Traceback (most recent call last):
    ...
TypeError: -1


__getitem__ index
>>> [ls[j] for j in range(0,34,5)]
['a', '2', '0', '5', '3', '1', '6']


__call__ ~=~ __getitem__
>>> [ls(j) for j in range(0,34,5)]
['a', '2', '0', '5', '3', '1', '6']
>>> ls(slice(0,14))
'abc01234560123'




######################
>>> deooseq = mk_double_ended_inf_len_seq_(5, ('abc', '0123456'), ('wxyz', '789'))
>>> deooseq
DoubleEndedInfLenSeqWithRecurringPeriod(5, InfLenSeqWithRecurringPeriod('abc', '0123456'), InfLenSeqWithRecurringPeriod('wxyz', '789'))
>>> [deooseq[j] for j in range(-20, 20)]
['0', '6', '5', '4', '3', '2', '1', '0', '6', '5', '4', '3', '2', '1', '0', '6', '5', '4', '3', '2', '1', '0', 'c', 'b', 'a', 'w', 'x', 'y', 'z', '7', '8', '9', '7', '8', '9', '7', '8', '9', '7', '8']
>>> deooseq[-20:20]
'0654321065432106543210cbawxyz78978978978'
>>> deooseq[19:-21:-1]
'87987987987zyxwabc0123456012345601234560'










######################

py_adhoc_call   seed.seq_tools.InfLenSeqWithRecurringPeriod   @f
]]]'''#'''
__all__ = r'''
mk_inf_len_seq_
    InfLenSeqWithRecurringPeriod
    mk_inf_len_seq5args8ooseq_
mk_double_ended_inf_len_seq_
    DoubleEndedInfLenSeqWithRecurringPeriod


iter_
    reversed_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge, check_may_
#.
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_
repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
lazy_import4funcs_('seed.tiny_.containers', 'mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_', __name__)
if 0:from seed.tiny_.containers import mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_
#.lazy_import4funcs_('seed.debug.print_err', 'print_err', __name__)
#.if 0:from seed.debug.print_err import print_err
lazy_import4funcs_('seed.helper.ifNone', 'ifNone,ifNonef', __name__)
if 0:from seed.helper.ifNone import ifNone,ifNonef
#.lazy_import4funcs_('seed.tiny_.funcs', 'echo,fst,snd', __name__)
#.if 0:from seed.tiny_.funcs import echo,fst,snd
lazy_import4funcs_('seed.types.Either', 'mk_Left,mk_Right', __name__)
if 0:from seed.types.Either import mk_Left,mk_Right

lazy_import4funcs_('seed.iters.count_', 'count_', __name__)
if 0:from seed.iters.count_ import count_
#.
#.
___end_mark_of_excluded_global_names__0___ = ...

if 1:
    def iter_(sf, begin, end=None, /, step=1):
        check_type_is(int, begin)
        check_may_([check_type_is, int], end)
        check_int_ge(1, step)
        for j in count_(begin, end, step):
            yield sf.at(j)
    def reversed_(sf, last, firstmm=None, /, step=-1):
        check_type_is(int, last)
        check_may_([check_type_is, int], firstmm)
        #no:check_int_lt(0, step)
        for j in map(int.__neg__, count_(-last, -firstmm, -step)):
            yield sf.at(j)

#inf_len_seq_with_recurring_period
class InfLenSeqWithRecurringPeriod:
    'inf_len_seq/ooseq'
    def __repr__(sf, /):
        return repr_helper(sf, sf.leading_seq, sf.recurring_period)
    def __init__(sf, leading_seq, recurring_period, /):
        leading_seq = mk_immutable_seq(leading_seq)
        recurring_period = mk_immutable_seq(recurring_period)
        if not recurring_period:raise TypeError

        sf._hs = leading_seq
        sf._ts = recurring_period
        sf._szs = (m:=len(leading_seq), n:=len(recurring_period), m+n)
        sf._xss = (leading_seq, recurring_period)
        T0 = type(leading_seq)
        T1 = type(recurring_period)
        sf._T = T0 if T0 is T1 else tuple

    @property
    def leading_seq(sf, /):
        return sf._hs
    @property
    def recurring_period(sf, /):
        return sf._ts
    @property
    def _type4slice_(sf, /):
        return sf._T
    def wrap_index__1_(sf, j, /):
        'uint -> uint%(len(leading_seq)+len(recurring_period))'
        check_int_ge(0, j)
        (m, n, L) = sf._szs
        return (j if j < L else m + (j-L)%n)
    def wrap_index__2_(sf, j, /):
        'uint -> (Either uint%len(leading_seq) uint%len(recurring_period))'
        check_int_ge(0, j)
        (m, n, L) = sf._szs
        return (mk_Left(j) if j < m else mk_Right((j-m)%n))
    def __iter__(sf, /):
        yield from sf.leading_seq
        while 1:
            yield from sf.recurring_period
    iter_ = iter_
    reversed_ = reversed_
    def at(sf, j, /):
        (b, i) = sf.wrap_index__2_(j)
        return sf._xss[b][i]
    def __call__(sf, j_or_sl, /):
        return sf[j_or_sl]
    def __getitem__(sf, j_or_sl, /):
        T = type(j_or_sl)
        if T is int:
            j = j_or_sl
            return sf.at(j)
        if T is slice:
            sl = j_or_sl
            step = ifNone(sl.step, 1)
            check_type_is(int, step)
            if not step:raise TypeError
            if step > 0:
                start = ifNone(sl.start, 0)
                check_int_ge(0, start)
                stop = sl.stop
                check_int_ge(0, stop)
                L = stop
                # [step >= 1][start >= 0][stop >= 0][L >= 0]
            else:
                assert step <= -1
                start = sl.start
                check_int_ge(0, start)
                if 0:
                    #bug:since 『s='abc' => s[:-1:-1]=='';s[0::-2]=='a'』
                    stop = ifNone(sl.stop, -1)
                    check_int_ge(-1, stop)
                else:
                    stop = sl.stop
                    if not None is stop:
                        check_int_ge(0, stop)
                    stop
                    # [stop :: may uint]
                L = 1+start
                # [step <= -1][start >= 0][stop :: may uint][L >= 1]
            L
            # [step <= -1][start >= 0][stop :: may uint][L >= 1]or[step >= 1][start >= 0][stop >= 0][L >= 0]
            # [step =!= 0][start >= 0][stop :: may uint][L >= 0]
            if 0:
                js = range(L)[start:stop:step]
            else:
                if stop is None:
                    stop = -1
                js = range(start, stop, step)
            js
            xs = map(sf.at, js) #(sf[i] for i in js)
            return mk_immutable_seq5iter__(sf._T, xs)
        raise TypeError(T)
#end-class InfLenSeqWithRecurringPeriod:

#def mk_inf_len_seq_with_recurring_period_
def mk_inf_len_seq_(leading_seq, recurring_period, /):
    '[x] -> nonempty[x] -> ooseq/InfLenSeqWithRecurringPeriod'
    return InfLenSeqWithRecurringPeriod(leading_seq, recurring_period)

def mk_inf_len_seq5args8ooseq_(args8ooseq, /):
    'args8ooseq/(tuple|InfLenSeqWithRecurringPeriod) -> ooseq/InfLenSeqWithRecurringPeriod'
    if type(args8ooseq) is InfLenSeqWithRecurringPeriod:
        ooseq = args8ooseq
    else:
        (leading_seq, recurring_period) = args8ooseq
        ooseq = mk_inf_len_seq_(leading_seq, recurring_period)
    ooseq
    return ooseq

def mk_double_ended_inf_len_seq_(offset, args8ooseq4L, args8ooseq4R, /):
    'int -> args8ooseq/(tuple|InfLenSeqWithRecurringPeriod) -> args8ooseq/(tuple|InfLenSeqWithRecurringPeriod) -> deooseq/DoubleEndedInfLenSeqWithRecurringPeriod'
    return DoubleEndedInfLenSeqWithRecurringPeriod(offset, args8ooseq4L, args8ooseq4R)

class DoubleEndedInfLenSeqWithRecurringPeriod:
    'double_ended_inf_len_seq/deooseq'
    def __repr__(sf, /):
        return repr_helper(sf, sf.offset, sf.ooseq4L, sf.ooseq4R)
    def __init__(sf, offset, args8ooseq4L, args8ooseq4R, /):
        check_type_is(int, offset)

        ooseq4L = mk_inf_len_seq5args8ooseq_(args8ooseq4L)
        ooseq4R = mk_inf_len_seq5args8ooseq_(args8ooseq4R)

        check_type_is(InfLenSeqWithRecurringPeriod, ooseq4L)
        check_type_is(InfLenSeqWithRecurringPeriod, ooseq4R)

        sf._org = offset
        sf._xsL = ooseq4L
        sf._xsR = ooseq4R
        sf._xss = (ooseq4L, ooseq4R)

        T0 = ooseq4L._type4slice_
        T1 = ooseq4R._type4slice_
        sf._T = T0 if T0 is T1 else tuple

    @property
    def offset(sf, /):
        return sf._org
    @property
    def ooseq4L(sf, /):
        return sf._xsL
    @property
    def ooseq4R(sf, /):
        return sf._xsR
    @property
    def _type4slice_(sf, /):
        return sf._T
    def wrap_index__2_(sf, j, /):
        'int -> Either result{ooseq4L.wrap_index__1_()} result{ooseq4R.wrap_index__1_()}'
        check_type_is(int, j)
        i = j - sf.offset
        return mk_Left(sf.ooseq4L.wrap_index__1_(-1-i)) if i < 0 else mk_Right(sf.ooseq4R.wrap_index__1_(i))
    def wrap_index__3_(sf, j, /):
        'int -> Either result{ooseq4L.wrap_index__2_()} result{ooseq4R.wrap_index__2_()}'
        check_type_is(int, j)
        i = j - sf.offset
        return mk_Left(sf.ooseq4L.wrap_index__2_(-1-i)) if i < 0 else mk_Right(sf.ooseq4R.wrap_index__2_(i))
    #def __iter__(sf, /):
    iter_ = iter_
    reversed_ = reversed_
    def at(sf, j, /):
        (b, i) = sf.wrap_index__2_(j)
        return sf._xss[b][i]
    def __call__(sf, j_or_sl, /):
        return sf[j_or_sl]
    def __getitem__(sf, j_or_sl, /):
        T = type(j_or_sl)
        if T is int:
            j = j_or_sl
            return sf.at(j)
        if T is slice:
            sl = j_or_sl
            step = ifNone(sl.step, 1)
            check_type_is(int, step)
            if not step:raise TypeError
            start = sl.start
            stop = sl.stop
            check_type_is(int, start)
            check_type_is(int, stop)
            js = range(start, stop, step)
            xs = map(sf.at, js) #(sf[i] for i in js)
            return mk_immutable_seq5iter__(sf._T, xs)
        raise TypeError(T)
#end-class DoubleEndedInfLenSeqWithRecurringPeriod:

__all__
#[mk_inf_len_seq_,mk_double_ended_inf_len_seq_] = lazy_import4funcs_('seed.seq_tools.InfLenSeqWithRecurringPeriod', 'mk_inf_len_seq_,mk_double_ended_inf_len_seq_', __name__)
from seed.seq_tools.InfLenSeqWithRecurringPeriod import mk_inf_len_seq_,mk_double_ended_inf_len_seq_

from seed.seq_tools.InfLenSeqWithRecurringPeriod import InfLenSeqWithRecurringPeriod, DoubleEndedInfLenSeqWithRecurringPeriod

from seed.seq_tools.InfLenSeqWithRecurringPeriod import *
