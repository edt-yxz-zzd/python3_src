#__all__:goto
#DONE:merge into ../../python3_src/seed/data_funcs/rngs.py
r'''[[[
e ../../python3_src/seed/text/compack_repr_char_set.py
    #字符范围:fmt==regex"({孤符}|{尾符}{首符})*" #局部降序，总体升序

view ../../python3_src/seed/text/pack_char_set.py
    #无关:
        #to chain strs to be a single str
view ../../python3_src/seed/text/mk_char_pt_ranges5predicator.py
    #字符集合<==>字符范围
view ../../python3_src/seed/data_funcs/rngs.py
    #字符范围:fmt==regex"({首符}{尾符})*" #升序
        ranges2char_pairs__str
        ranges5char_pairs__str
    #自然数范围:而非字符范围:
        #ranges2compact_txt_
        #ranges5compact_txt_


seed.text.compack_repr_char_set
py -m nn_ns.app.debug_cmd   seed.text.compack_repr_char_set -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.text.compack_repr_char_set:__doc__ -ht # -ff -df

[[
]]

:%s/compack_reprtxt/wave_rngtxt/g
    #局部降序，总体升序 => wave#波动,涨落,起伏

wave_rngtxt2nontouch_ranges_
wave_rngtxt5nontouch_ranges_

# [(strict_sorted_chars, wave_rngtxt)]
>>> cs_ct_pairs = (
... [('', '')
... ,('0', '0')
... ,('01', '10')
... ,('012', '20')
... ,('02', '02')
... ,('0245', '0254')
... ,('02456', '0264')
... ,('024568', '02648')
... ,('0245689', '026498')
... ,('0245689a', '026498a')
... ])


>>> for (strict_sorted_chars, wave_rngtxt) in cs_ct_pairs:
...     assert wave_rngtxt5strict_sorted_chars_(strict_sorted_chars) == wave_rngtxt
...     assert wave_rngtxt2strict_sorted_chars_(wave_rngtxt) == strict_sorted_chars




py_adhoc_call   seed.text.compack_repr_char_set   @f
]]]'''#'''
__all__ = r'''
wave_rngtxt2nontouch_ranges_
wave_rngtxt5nontouch_ranges_
    wave_rngtxt2IRanges_
    wave_rngtxt5IRanges_
    wave_rngtxt2strict_sorted_chars_
    wave_rngtxt5strict_sorted_chars_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func import lazy_import4funcs_
lazy_import4funcs_('seed.data_funcs.rngs', 'make_Ranges,sorted_rngs_to_iter_nontouch_ranges,sorted_ints_to_iter_nontouch_ranges', __name__)
if 0:from seed.data_funcs.rngs import make_Ranges, sorted_rngs_to_iter_nontouch_ranges, sorted_ints_to_iter_nontouch_ranges
#from seed.data_funcs.rngs import IRanges


#from itertools import pairwise
from seed.iters.pairwise_ import pairwise__tail_
from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...



def wave_rngtxt2nontouch_ranges_(wave_rngtxt, /):
    check_type_is(str, wave_rngtxt)
    ######################
    #ver1:
    #.c_ = -2
    #.end = -1
    #.b_drop = False
    #.for c, _c in pairwise(map(ord, wave_rngtxt)):
    #.    if b_drop:
    #.        #drop c since (c_,c)~rng
    #.        # [c_ > c]
    #.        b_drop = False
    #.        if not c+1 <= c_ <= _c-2:raise 000
    #.            # !! nontouch_ranges
    #.        continue
    #.    if not c_ < c:raise 000
    #.    if c == _c:raise 000
    #.    c_ = c
    #.    b_drop = c > _c
    #.    if b_drop:
    #.        #局部降序
    #.        #(c,_c)~rng
    #.        #{尾符}{首符}
    #.        # [c > _c]
    #.        first = _c
    #.    else:
    #.        #{孤符}
    #.        if not c <= _c-2:raise 000
    #.        first = c
    #.    first
    #.    last = c
    #.    if not end < first:raise 000
    #.    begin = first
    #.    end = last+1
    #.    yield(begin, end)
    #.if wave_rngtxt and not b_drop:
    #.    # [_c == ord(wave_rngtxt[-1])]
    #.    if len(wave_rngtxt) == 1:
    #.        _c = ord(wave_rngtxt[-1])
    #.    else:
    #.        _c
    #.    assert _c == ord(wave_rngtxt[-1])
    #.    #{孤符}
    #.    first = last = _c
    #.    if not end < first:raise 000
    #.    begin = first
    #.    end = last+1
    #.    yield(begin, end)
    #.#return nontouch_ranges
    #.return
    ######################
    #ver2:通过添加末尾哨兵，省略最后尾符处理
    c_ = -2
    end = -1
    b_drop = False
    for c, _c in pairwise__tail_(float('inf'), map(ord, wave_rngtxt)):
        if b_drop:
            #drop c since (c_,c)~局部降序~rng
            # [c_ > c]
            # [c_ > c < _c]
            # [c < c_ < _c]
            # [c+1 <= c_ <= _c-2]
                # !! nontouch_ranges => "-2"
                # !! 局部降序 => "+1"
            if not c+1 <= c_ <= _c-2:raise 000
            b_drop = False
            continue
        if not c_ <= c-2:raise 000
        if c == _c:raise 000
        c_ = c #for next round
        b_drop = c > _c
        if b_drop:
            #局部降序
            #(c,_c)~rng
            #{尾符}{首符}
            # [c > _c]
            first = _c
        else:
            #{孤符}
            if not c <= _c-2:raise 000
            first = c
        first
        last = c
        if not end < first:raise 000
        begin = first
        end = last+1
        yield(begin, end)
    #return nontouch_ranges
    return
def wave_rngtxt5nontouch_ranges_(nontouch_ranges, /):
    #字符范围:fmt==regex"({孤符}|{尾符}{首符})*" #局部降序，总体升序
    def __():
        last = -2
        for begin, end in nontouch_ranges:
            if not last+2 <= begin <= end-1: raise 000
            #总体升序
            first = begin
            last = end-1
            if first == last:
                #{孤符}
                ch = chr(first)
                yield ch
            else:
                #{尾符}{首符}
                head_ch = chr(first)
                tail_ch = chr(last)
                yield tail_ch+head_ch #局部降序
    #end-def __():
    wave_rngtxt = ''.join(__())
    return wave_rngtxt
def wave_rngtxt5IRanges_(ranges, /):
    ranges = ranges.to_NonTouchRanges()
    nontouch_ranges = ranges.ranges
    return wave_rngtxt5nontouch_ranges_(nontouch_ranges)
def wave_rngtxt5strict_sorted_chars_(strict_sorted_chars, /):
    nontouch_ranges = sorted_ints_to_iter_nontouch_ranges(map(ord, strict_sorted_chars))
    #it = ensure_strict_sorted(strict_sorted_chars)
    return wave_rngtxt5nontouch_ranges_(nontouch_ranges)
def wave_rngtxt2strict_sorted_chars_(wave_rngtxt, /):
    ranges = wave_rngtxt2IRanges_(wave_rngtxt)
    strict_sorted_chars = ''.join(map(chr, ranges.iter_ints()))
    return strict_sorted_chars
def wave_rngtxt2IRanges_(wave_rngtxt, /):
    nontouch_ranges = wave_rngtxt2nontouch_ranges_(wave_rngtxt)
    ranges = make_Ranges(nontouch_ranges)
    return ranges

__all__
from seed.text.compack_repr_char_set import wave_rngtxt2nontouch_ranges_, wave_rngtxt5nontouch_ranges_
from seed.text.compack_repr_char_set import wave_rngtxt2IRanges_, wave_rngtxt5IRanges_
from seed.text.compack_repr_char_set import wave_rngtxt2strict_sorted_chars_, wave_rngtxt5strict_sorted_chars_
from seed.text.compack_repr_char_set import *
