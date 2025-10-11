#__all__:goto
r'''[[[
e ../../python3_src/seed/seq_tools/mk_seq_rng__with_step.py

seed.seq_tools.mk_seq_rng__with_step
py -m nn_ns.app.debug_cmd   seed.seq_tools.mk_seq_rng__with_step -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.seq_tools.mk_seq_rng__with_step:__doc__ -ht # -ff -df
#######

[[
源起:
view ../../python3_src/seed/types/Deque.py
]]


'#'; __doc__ = r'#'
>>> from itertools import product
>>> js = [-999, -666, -333, *range(-10,11), +333, +666, +999]
>>> steps = [j for j in js if j]
>>> szs = [j for j in js if j >= 0]
>>> for (sz, begin, end, step) in product(szs, js, js, steps):
...     rng = range(sz)[begin:end:step]
...     (b_reversed, begin, end, step, length) = mk_seq_rng__with_step__len_(sz, begin, end, step)
...     assert type(b_reversed) is bool
...     assert type(begin) is int
...     assert type(end) is int
...     assert type(step) is int
...     assert type(length) is int
...     assert 0 <= begin <= end <= sz, (rng, (begin, end, sz))
...     assert step >= 1
...     assert length >= 0
...     assert 0 <= begin + step*length - end < step, (begin, end, step, length)
...     assert length == 1+(end-begin-1)//step # ceil((end-begin)/step)
...     assert length == len(rng)
...     _rng = range(sz)[begin:end:step][::-1 if b_reversed else 1]
...     assert length == len(_rng)
...     assert rng == _rng, (rng, _rng)


py_adhoc_call   seed.seq_tools.mk_seq_rng__with_step   @f
]]]'''#'''
__all__ = r'''
mk_seq_rng__with_step__len_
    mk_seq_rng__with_step__seq_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge
#.from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_
___end_mark_of_excluded_global_names__0___ = ...



def mk_seq_rng__with_step__seq_(seq, /, begin, end, step):
    return mk_seq_rng__with_step__len_(len(seq), begin, end, step)
def mk_seq_rng__with_step__len_(sz, /, begin, end, step):
    'sz/uint -> begin/may int -> end/may int -> step/may int{=!=0} -> (b_reversed, begin, end, step, length) # [b_reversed::bool][step >= 1][0 <= begin <= end <= sz][length == ceil((end-begin)/step) == 1+(end-begin-1)//step]'
    check_int_ge(0, sz)
    _0_args = (sz, begin, end, step)
    _0_rng = range(sz)[begin:end:step]
    if step is None:
        step = 1
    ######################
    b_neg = step < 0
    rng = _0_rng[::-1] if b_neg else _0_rng
    step = rng.step
    if rng:
        last = rng[-1]
        end = min(sz, last+step)
        begin = rng[0]
    else:
        begin = min(sz, rng.start)
        end = begin
    begin, end
    ######################
    b_reversed = b_neg
    ######################
    sz
    b_reversed, (begin, end, step)
    ######################
    _9_rng = range(sz)[begin:end:step]
    assert _0_rng == _9_rng[::-1 if b_reversed else 1]
    ######################
    #.assert len(_0_rng) == len(_9_rng)
    #.assert not _9_rng or ([_0_rng[0], _0_rng[-1]] == [_9_rng[0], _9_rng[-1]][::-1 if b_reversed else 1])
    #.assert _0_rng.step == -_9_rng.step if b_reversed else _9_rng.step
    ######################
    assert step >= 1
    assert 0 <= begin <= end <= sz, (_0_args, _0_rng, rng, (begin, end, sz))
    # [step >= 1]
    # [0 <= begin <= end <= sz]
    length = len(_0_rng)
    return (b_reversed, begin, end, step, length)

#################################
#一些失败的实现:
#################################
#.def __mk_seq_rng__with_step__len_(sz, /, begin, end, step):
#.    'sz/uint -> begin/int -> end/int -> step/int{=!=0} -> (b_reversed, begin, end, step) # [b_reversed::bool][step >= 1][0 <= begin <= end <= sz]'
#.    check_int_ge(0, sz)
#.    _0_args = (sz, begin, end, step)
#.    _0_rng = range(sz)[begin:end:step]
#.    if 1:
#.        ######################
#.        b_neg = step < 0
#.        rng = _0_rng[::-1] if b_neg else _0_rng
#.        step = rng.step
#.        if 0:
#.            raise 000
#.            #bad:
#.            begin = rng.start
#.            end = rng.stop
#.        if rng:
#.            last = rng[-1]
#.            end = min(sz, last+step)
#.            begin = rng[0]
#.        else:
#.            begin = min(sz, rng.start)
#.            end = begin
#.        begin, end
#.
#.        ######################
#.    else:
#.        ######################
#.        raise 000
#.        #bad:
#.        (begin, end, step) = slice(begin, end, step).indices(sz)
#.        b_neg = step < 0
#.        if b_neg:
#.            rng = range(begin, end, step)[::-1]
#.            begin = rng.start
#.            end = rng.stop
#.            step = rng.step
#.        ######################
#.    b_reversed = b_neg
#.    ######################
#.    sz
#.    b_reversed, (begin, end, step)
#.    #.assert step >= 1
#.    #.assert 0 <= begin <= end <= sz, (_0_args, _0_rng, rng, (begin, end, sz))
#.
#.
#.    #.assert 0 <= begin <= end, (_0_args, _0_rng, rng, (begin, end, sz))
#.    #.if begin == end and not 0 <= begin <= sz:
#.    #.    begin = end = sz
#.    #.assert 0 <= begin <= sz, (_0_args, _0_rng, rng, (begin, end, sz))
#.    #.if sz < end:
#.    #.    assert end-step < sz, (_0_args, _0_rng, rng, (begin, end, sz))
#.    #.    end = sz
#.    #.assert 0 <= begin <= end <= sz, (_0_args, _0_rng, rng, (begin, end, sz))
#.
#.    _9_rng = range(sz)[begin:end:step]
#.    assert len(_0_rng) == len(_9_rng)
#.    assert not _9_rng or ([_0_rng[0], _0_rng[-1]] == [_9_rng[0], _9_rng[-1]][::-1 if b_reversed else 1])
#.    assert _0_rng.step == -_9_rng.step if b_reversed else _9_rng.step
#.    assert 0 <= begin <= end <= sz, (_0_args, _0_rng, rng, (begin, end, sz))
#.    assert step >= 1
#.    # [step >= 1]
#.    # [0 <= begin <= end <= sz]
#.    return (b_reversed, begin, end, step)




__all__
#[mk_seq_rng__with_step__len_,mk_seq_rng__with_step__seq_] = lazy_import4funcs_('seed.seq_tools.mk_seq_rng__with_step', 'mk_seq_rng__with_step__len_,mk_seq_rng__with_step__seq_', __name__)
from seed.seq_tools.mk_seq_rng__with_step import mk_seq_rng__with_step__len_, mk_seq_rng__with_step__seq_
# (b_reversed, begin, end, step, length) = mk_seq_rng__with_step__len_(sz, begin, end, step)
from seed.seq_tools.mk_seq_rng__with_step import *
