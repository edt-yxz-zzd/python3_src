#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/CJK/cjk_subsets/cjk_subsets__TS.py

[[
繁简汉字对vivi大小写字母
    因为大部分基础编码:全部简体|全部繁体
        ，所以只要求:繁简汉字对 其一汉字 可被编码就行。
    因为unicode编码持续更新
        ，所以只考虑已稳定的部分编码:『[一..=龥]』
        龥yu4
        由于[gb2312 < [一..=龥]]，可以说是个好的起点
>>> hex(ord('龥'))
'0x9fa5'
>>> hex(ord('一'))
'0x4e00'
>>> j=1+ord('龥')
>>> i=ord('一')
>>> j-i
20902
>>> hex(20902)
'0x51a6'
>>> chr(0x51A6)
'冦'
>>> ord('冦')
20902
>>> ord('寇')
23495


基础编码-汉字相关:
    (big5,cp949,gb2312,iso2022_jp)
        view ../../python3_src/nn_ns/CJK/cjk_subsets/hanzi.py
]]


nn_ns.CJK.cjk_subsets.cjk_subsets__TS
py -m nn_ns.app.debug_cmd   nn_ns.CJK.cjk_subsets.cjk_subsets__TS -x
py -m nn_ns.app.doctest_cmd nn_ns.CJK.cjk_subsets.cjk_subsets__TS:__doc__ -ht
from nn_ns.CJK.cjk_subsets.cjk_subsets__TS import *


py_adhoc_call   nn_ns.CJK.cjk_subsets.cjk_subsets__TS   @str._main4TS_ +show_sz --sz4cut=16
    ==>>:
    943
    文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥牜过滤冫汉字相关基础编码
py_adhoc_call   nn_ns.CJK.cjk_subsets.cjk_subsets__TS   @str._main4TS_ +show_sz --sz4cut=16 --encodings='[]'
    ==>>:
    1959
    文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥


py_adhoc_call   nn_ns.CJK.cjk_subsets.cjk_subsets__TS   @str._main4hz_ +show_sz --sz4cut=16
    ==>>:
    2230
    文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥牜过滤冫汉字相关基础编码
        cjk_common_subset_2513_trivial_TS_2230
py_adhoc_call   nn_ns.CJK.cjk_subsets.cjk_subsets__TS   @str._main4hz_ +show_sz --sz4cut=16 --encodings='[]'
    ==>>:
    14428
    文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥

py_adhoc_call   nn_ns.CJK.cjk_subsets.cjk_subsets__TS   @str._main4hz_ +show_sz --sz4cut=16 +to_output_rngs
    ==>>:
    2230 hzs
    1780 rngs
    Counter({1: 1437, 2: 267, 3: 54, 4: 16, 5: 3, 6: 3})
py_adhoc_call   nn_ns.CJK.cjk_subsets.cjk_subsets__TS   @str._main4hz_ +show_sz --sz4cut=16 --encodings='[]' +to_output_rngs
    ==>>:
    14428 hzs
    3396 rngs
    Counter({1: 1011, 2: 592, 3: 430, 4: 311, 5: 223, 6: 172, 7: 146, 8: 111, 9: 74, 10: 60, 11: 44, 12: 42, 13: 25, 14: 21, 17: 20, 15: 16, 19: 15, 18: 15, 16: 11, 21: 10, 22: 7, 20: 6, 24: 6, 27: 4, 28: 3, 25: 3, 23: 3, 29: 3, 34: 2, 36: 2, 26: 2, 32: 1, 48: 1, 35: 1, 39: 1, 31: 1, 30: 1})

py_adhoc_call   nn_ns.CJK.cjk_subsets.cjk_subsets__TS   @generate_output_py_data_script
view ../../python3_src/nn_ns/CJK/cjk_subsets/cjk_subsets__TS____output.py


#]]]'''
__all__ = r'''

文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥
文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥牜过滤冫汉字相关基础编码

文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥牜过滤冫汉字相关基础编码
文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥

    列表纟基础编码牜汉字相关
    所选用的稳定汉字区
    繁简字对列表囗繁简囗唯一可逆
    汉字列表囗繁简囗平凡自反


generate_output_py_data_script
    default_oname4generate_output_py_data_script











文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥牜过滤冫汉字相关基础编码
    文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥牜过滤冫汉字相关基础编码_943繁简字对_1886
    hzTSpairs__hit_encodings_big5_cp949_gb2312_iso2022_jp__1886
文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥
    文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥_1959繁简字对_3918
    hzTSpairs__hit_region_ge4E00_le9FA5_20902__3918
文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥牜过滤冫汉字相关基础编码
    文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥牜过滤冫汉字相关基础编码_2230
    cjk_common_region_of_encodings_big5_cp949_gb2312_iso2022_jp__trivial_TS__2230
文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥
    文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥_14428
    cjk_region_ge4E00_le9FA5_20902__trivial_TS__14428

'''.split()#'''
r'''[[[
class _CachedLazy:
def _iter_TSs5str_(TSs__str, /):
def _str5TSs_(TSs, /, *, sep=''):
def _mk_hz2TS__5__TSs_(TSs, /):

def _filter_TSs__hit_rngs_(rngs, hz2TS, /):
def _filter_TSs__hit_encoding_(encoding, hz2TS, /):
def _filter_TSs__hit_rngs__hit_encodings_(encodings, rngs, TSs__str, /):
def _main4TS_(*, sz4cut, show_sz, encodings=...):

def _filter_hzs__hit_rngs_(rngs, hzs__str, /):
def _filter_hzs__hit_encoding_(encoding, hzs__str, /):
def _filter_hzs__hit_rngs__hit_encodings_(encodings, rngs, hzs__str, /):
def _main4hz_(*, sz4cut, show_sz, to_output_rngs=False, encodings=...):

#]]]'''#'''
__all__
from collections import Counter
from pathlib import Path

from seed.iters.icut_to import icut_seq_to
from seed.data_funcs.rngs import make_Ranges, sorted_ints_to_iter_nontouch_ranges# detect_iter_ranges, StackStyleSimpleIntSet, StackStyleSimpleIntMapping, TouchRangeBasedIntMapping
from seed.text.charset_filter import (
EncodingCharFilter
#,CharsetCharFilter
#,CharNameRegexCharFilter
#,CharPredicatorCharFilter
)
from nn_ns.CJK.CJK_data.汉字繁简囗囗平凡自反囗唯一可逆囗囗打完补丁囗简繁字对囗补丁囗㝉宁相关 import \
(汉字列表囗繁简囗平凡自反#14513
,繁简字对列表囗繁简囗唯一可逆#1965*2
)

#全局变量:
列表纟基础编码牜汉字相关 = tuple(r'big5,cp949,gb2312,iso2022_jp'.split(','))
所选用的稳定汉字区 = '一龥'

assert 14513 == len(汉字列表囗繁简囗平凡自反)
assert 1965*2 == len(繁简字对列表囗繁简囗唯一可逆)



















class _CachedLazy:
    def __init__(sf, f, /, *args):
        sf._f = f
        sf._args = args
        sf._tm = ()
    def __call__(sf, /):
        if not sf._tm:
            r = sf._f(*sf._args)
            sf._tm = (r,)
            return sf()
        [r] = sf._tm
        return r











def _rng2hzhz_(rng, /):
    (i, j) = rng
    c0 = chr(i)
    c1 = chr(j-1)
    hzhz = c0 + c1
    return hzhz
def _rng5hzhz_(hzhz, /):
    (c0, c1) = hzhz
    i = ord(c0)
    j = 1+ord(c1)
    rng = (i, j)
    return rng
def _mk_rngs5hzhzs_(hzhzs__str, /):
    #hzhzs__str = 所选用的稳定汉字区
    #bug:rngs = sorted((*map(ord, hzhz),) for hzhz in _iter_hzhzs5str_(hzhzs__str))
    rngs = sorted(map(_rng5hzhz_, _iter_hzhzs5str_(hzhzs__str)))
    return tuple(rngs)
def _iter_hzhzs5str_(hzhzs__str, /):
    'hzhzs__str -> Iter hzhz'
    assert len(hzhzs__str)&1 == 0
    ss = hzhzs__str
    for j in range(len(ss))[::2]:
        hzhz = ss[j:j+2]
        yield hzhz

def _iter_TSs5str_(TSs__str, /):
    'TSs__str -> Iter TS'
    #ss = TSs__str = 繁简字对列表囗繁简囗唯一可逆
    return _iter_hzhzs5str_(TSs__str)
def _str5TSs_(TSs, /, *, sep=''):
    'TSs__str -> Iter TS'
    return sep.join(TSs)
def _mk_hz2TS__5__TSs_(TSs, /):
    'Iter TS -> hz2TS/{(简|繁):繁简字对}'
    hz2TS = {}
    for TS in TSs:
        (hz__T, hz__S) = TS
        hz2TS[hz__T] = TS
        hz2TS[hz__S] = TS
    return hz2TS


def _filter_TSs__hit_rngs_(rngs, hz2TS, /):
    '-> sorted-unique-[TS]  #[繁简字对{[繁<-rngs]or[简<-rngs]}]'
    rsP = make_Ranges(rngs)
    rsK = make_Ranges(sorted_ints_to_iter_nontouch_ranges(sorted(map(ord, hz2TS))))
    rs = (rsP & rsK)
    s = {hz2TS[hz] for hz in map(chr, rs)}
    TSs = sorted(s)
    return TSs
def _filter_TSs__hit_encoding_(encoding, hz2TS, /):
    '-> sorted-unique-[TS]  #[繁简字对{[繁<-encoding]or[简<-encoding]}]'
    efr = EncodingCharFilter(encoding)
    s = set()
    for hz in hz2TS:
        k = ord(hz)
        #if k in efr:
        if efr.is_good_char_ord(k):
            TS = hz2TS[hz]
            s.add(TS)
    TSs = sorted(s)
    return TSs

def _filter_TSs__hit_rngs__hit_encodings_(encodings, rngs, TSs__str, /):
    '-> sorted-unique-[TS]  #[繁简字对{[繁<-(rngs/-\encodings)]or[简<-(rngs/-\encodings)]}]'
    TSs = _iter_TSs5str_(TSs__str)
    hz2TS = _mk_hz2TS__5__TSs_(TSs)
    TSs = _filter_TSs__hit_rngs_(rngs, hz2TS)
    for encoding in encodings:
        hz2TS = _mk_hz2TS__5__TSs_(TSs)
        TSs = _filter_TSs__hit_encoding_(encoding, hz2TS)
    TSs
    #hz2TS = _mk_hz2TS__5__TSs_(TSs)
    return TSs


def _main4TS_(*, sz4cut, show_sz, encodings=...):
    r'''[[[
全局变量:
    列表纟基础编码牜汉字相关
    所选用的稳定汉字区
    繁简字对列表囗繁简囗唯一可逆

    #]]]'''#'''
    ######################
    #全局变量:
    encodings = 列表纟基础编码牜汉字相关 if encodings is ... else encodings
    rngs = _mk_rngs5hzhzs_(所选用的稳定汉字区)
    TSs__str = 繁简字对列表囗繁简囗唯一可逆
    ######################
    TSs = _filter_TSs__hit_rngs__hit_encodings_(encodings, rngs, TSs__str)
        #if not encodings:文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥
        #if encodings is ...:文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥牜过滤冫汉字相关基础编码
    if show_sz:
        print(len(TSs))
            #943@[encodings is ...]
            #   文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥牜过滤冫汉字相关基础编码
            #
            #1959@[encodings == []]
            #   文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥
            #
    TSs__str = _str5TSs_(TSs)
    if sz4cut > 0:
        TSs__str = '\n'.join(icut_seq_to(TSs__str, sz4cut))
    TSs__str
    文本纟繁简字对列表牜繁简唯一可逆牜过滤后 = TSs__str
    return 文本纟繁简字对列表牜繁简唯一可逆牜过滤后




def _filter_hzs__hit_rngs_(rngs, hzs__str, /):
    '-> sorted-unique-hzs__str  #[平凡自反{[hz<-rngs]}]'
    rsP = make_Ranges(rngs)
    rsK = make_Ranges(sorted_ints_to_iter_nontouch_ranges(sorted(map(ord, hzs__str))))
    rs = (rsP & rsK)
    hzs__str = ''.join(map(chr, rs))

    return hzs__str
def _filter_hzs__hit_encoding_(encoding, hzs__str, /):
    '-> sorted-unique-hzs__str  #[平凡自反{[hz<-encoding]}]'
    efr = EncodingCharFilter(encoding)
    hzs = []
    for hz in hzs__str:
        k = ord(hz)
        #if k in efr:
        if efr.is_good_char_ord(k):
            hzs.append(hz)
    hzs.sort()
    hzs__str = ''.join(hzs)
    return hzs__str

def _filter_hzs__hit_rngs__hit_encodings_(encodings, rngs, hzs__str, /):
    '-> sorted-unique-hzs__str  #[平凡自反{[hz<-(rngs/-\encodings)]}]'
    hzs__str = _filter_hzs__hit_rngs_(rngs, hzs__str)
    for encoding in encodings:
        hzs__str = _filter_hzs__hit_encoding_(encoding, hzs__str)
    hzs__str
    return hzs__str


def _main4hz_(*, sz4cut, show_sz, to_output_rngs=False, encodings=...):
    r'''[[[
全局变量:
    列表纟基础编码牜汉字相关
    所选用的稳定汉字区
    汉字列表囗繁简囗平凡自反

    #]]]'''#'''
    ######################
    #全局变量:
    encodings = 列表纟基础编码牜汉字相关 if encodings is ... else encodings
    rngs = _mk_rngs5hzhzs_(所选用的稳定汉字区)
    hzs__str = 汉字列表囗繁简囗平凡自反
    ######################
    hzs__str = _filter_hzs__hit_rngs__hit_encodings_(encodings, rngs, hzs__str)
        #if not encodings:文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥
        #if encodings is ...:文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥牜过滤冫汉字相关基础编码
    if to_output_rngs:
        rngs = make_Ranges(sorted_ints_to_iter_nontouch_ranges(map(ord, hzs__str))).ranges

    if show_sz:
        print(len(hzs__str), 'hzs')
            #2230@[encodings is ...]
            #   文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥牜过滤冫汉字相关基础编码
            #
            #14428@[encodings == []]
            #   文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥
            #
        if to_output_rngs:
            rngs
            print(len(rngs), 'rngs')
            sz2c = Counter()
            for rng in rngs:
                (i, j) = rng
                sz = j-i
                sz2c[sz] += 1
            #print(sz2c.most_common())
            print(sz2c)

    if to_output_rngs:
        rngs
        ls = []
        for rng in rngs:
            (i, j) = rng
            sz = j-i
            hzhz = _rng2hzhz_(rng)
            s = f'{hzhz}#{sz}'
            ls.append(s)
        return '\n'.join(ls)
        r'''[[[
        if sz4cut > 0:
            rngss = [*icut_seq_to(rngs, sz4cut)]
        else:
            rngss = [rngs]
        rngss
        ls = []
        for _rngs in rngss:
            ...
        #]]]'''#'''

    if sz4cut > 0:
        hzs__str = '\n'.join(icut_seq_to(hzs__str, sz4cut))
    hzs__str
    文本纟汉字列表牜繁简平凡自反牜过滤后 = hzs__str
    return 文本纟汉字列表牜繁简平凡自反牜过滤后




#generate_output_py_data_script:begin
_fmt = r"""
{sz1}
{nm4var} = (
r'''
{txt4var}
'''#'''
)
assert {sz2} == len({nm4var}.replace('\n', ''))

"""#"""

_this_file = Path(__file__)
_this_dir = _this_file.parent
default_oname4generate_output_py_data_script = f'{_this_file.stem}____output'
    #cjk_subsets__TS____output.py
def generate_output_py_data_script(*, oname=default_oname4generate_output_py_data_script):
    if not oname.isidentifier():raise ValueError(oname)
    opath = _this_dir / f'{oname}.py'
    with open(opath, 'xt', encoding='utf8') as ofile:
        for s in _generate_output_py_data_script_(oname):
            print(s, file=ofile)

def _generate_output_py_data_script_(oname, /):
    _fmt

    文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥牜过滤冫汉字相关基础编码 = _main4TS_(sz4cut=16, show_sz=False, encodings=...)
    文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥 = _main4TS_(sz4cut=16, show_sz=False, encodings=[])



    文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥牜过滤冫汉字相关基础编码 = _main4hz_(sz4cut=16, show_sz=False, encodings=...)
    文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥 = _main4hz_(sz4cut=16, show_sz=False, encodings=[])

    full_szs = [943*2, 1959*2, 2230, 14428]
    assert full_szs == [1886, 3918, 2230, 14428]

    nms = (
    ['文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥牜过滤冫汉字相关基础编码'
    ,'文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥'
    ,'文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥牜过滤冫汉字相关基础编码'
    ,'文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥'
    ])
    brief_nms = nms
    english_nms = (
    # !! [gb2312 < [0x4E00..=0x9FA5]]
    # => omit "region_ge4E00_le9FA5_20902" if using gb2312
    ['hzTSpairs__hit_encodings_big5_cp949_gb2312_iso2022_jp__'
    ,'hzTSpairs__hit_region_ge4E00_le9FA5_20902__'
    ,'cjk_common_region_of_encodings_big5_cp949_gb2312_iso2022_jp__trivial_TS__'
        #,'cjk_common_subset_2513_trivial_TS_2230:文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥牜过滤冫汉字相关基础编码'
    ,'cjk_region_ge4E00_le9FA5_20902__trivial_TS__'
    ]) #待附加full_sz...
    verbose_nms = [] #待填充...
    _full_szs = []


    this_mdl = f'{__package__}.{oname}'

    header = f'#\n#\n#generated by {__name__}::generate_output_py_data_script\n#\n#\n\n'

    yield header
    for nm4var in nms[:2]:
        txt4var = locals()[nm4var]
        full_sz = len(''.join(txt4var.split()))
        assert full_sz%2 == 0
        half_sz = full_sz//2
        sz1 = f'#{half_sz}对 #{full_sz}'
        sz2 = f'{half_sz}*2 == {full_sz}'
        s = _fmt.format(sz1=sz1, sz2=sz2, nm4var=nm4var, txt4var=txt4var)
        yield s
        _full_szs.append(full_sz)
        verbose_nm = f'{nm4var}_{half_sz}繁简字对_{full_sz}'
        verbose_nms.append(verbose_nm)
        i = nms.index(nm4var)
        english_nms[i] += str(full_sz)
    half_sz = None

    for nm4var in nms[2:]:
        txt4var = locals()[nm4var]
        full_sz = len(''.join(txt4var.split()))
        sz1 = f'#{full_sz}'
        sz2 = f'{full_sz}'
        s = _fmt.format(sz1=sz1, sz2=sz2, nm4var=nm4var, txt4var=txt4var)
        yield s
        _full_szs.append(full_sz)
        verbose_nm = f'{nm4var}_{full_sz}'
        verbose_nms.append(verbose_nm)
        i = nms.index(nm4var)
        english_nms[i] += str(full_sz)
    assert _full_szs == full_szs

    for nm0, nm1, nm2 in zip(brief_nms, verbose_nms, english_nms):
        yield f'{nm2} = {nm1} = {nm0}'

    yield ''
    yield r"assert '' == ''.join(c for c in 文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥 if not ('一' <= c <= '龥' or c == '\n'))"
    yield ''

    brief_nms4vars__str = ', '.join(brief_nms)
    verbose_nms4vars__str = ', '.join(verbose_nms)
    english_nms4vars__str = ', '.join(english_nms)

    footer1 = '\n\n' f'from {this_mdl} import {brief_nms4vars__str}'
    footer2 = '\n\n' f'from {this_mdl} import {verbose_nms4vars__str}'
    footer3 = '\n\n' f'from {this_mdl} import {english_nms4vars__str}'

    yield footer1
    yield footer2
    yield footer3
    return
#generate_output_py_data_script:end




from nn_ns.CJK.cjk_subsets.cjk_subsets__TS____output import 文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥牜过滤冫汉字相关基础编码, 文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥, 文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥牜过滤冫汉字相关基础编码, 文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥

943
assert 943*2 == len(文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥牜过滤冫汉字相关基础编码.replace('\n', ''))

1959
assert 1959*2 == len(文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥.replace('\n', ''))

2230
assert 2230 == len(文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥牜过滤冫汉字相关基础编码.replace('\n', ''))

14428
assert 14428 == len(文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥.replace('\n', ''))



assert '' == ''.join(c for c in 文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥 if not ('一' <= c <= '龥' or c == '\n'))









from nn_ns.CJK.cjk_subsets.cjk_subsets__TS____output import 文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥牜过滤冫汉字相关基础编码, 文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥, 文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥牜过滤冫汉字相关基础编码, 文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥

from nn_ns.CJK.cjk_subsets.cjk_subsets__TS____output import 文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥牜过滤冫汉字相关基础编码_943繁简字对_1886, 文本纟繁简字对列表牜繁简唯一可逆牜基位面冫一臸龥_1959繁简字对_3918, 文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥牜过滤冫汉字相关基础编码_2230, 文本纟汉字列表牜繁简平凡自反牜基位面冫一臸龥_14428


from nn_ns.CJK.cjk_subsets.cjk_subsets__TS____output import hzTSpairs__hit_encodings_big5_cp949_gb2312_iso2022_jp__1886, hzTSpairs__hit_region_ge4E00_le9FA5_20902__3918, cjk_common_region_of_encodings_big5_cp949_gb2312_iso2022_jp__trivial_TS__2230, cjk_region_ge4E00_le9FA5_20902__trivial_TS__14428
__all__
from nn_ns.CJK.cjk_subsets.cjk_subsets__TS import *
