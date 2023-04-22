#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/CJK/CJK_common/is_hz.py
see:
    view ../../python3_src/nn_ns/CJK/CJK_common/is_hz.py
    view script/字词典囗用字统计囗.py
    view ../../python3_src/nn_ns/CJK/CJK_data/raw/拼音用字.py
        #注意:PUA/私用区汉字！！

=====

nn_ns.CJK.CJK_common.is_hz
py -m nn_ns.app.debug_cmd   nn_ns.CJK.CJK_common.is_hz -x
py -m nn_ns.app.doctest_cmd nn_ns.CJK.CJK_common.is_hz:__doc__ -ff -v
py -m nn_ns.app.doctest_cmd nn_ns.CJK.CJK_common.is_hz!

from nn_ns.CJK.CJK_common.is_hz import is_hz__tribool_, partition_charset_by_is_hz_

from nn_ns.CJK.CJK_common.is_hz import *


=====
py_adhoc_call   nn_ns.CJK.CJK_common.is_hz   @partition_charset_by_is_hz__5path_  --encoding:u8  :/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词典.txt
py_adhoc_call   nn_ns.CJK.CJK_common.is_hz   @not_show.show_partition_charset_by_is_hz__5path_  --encoding:u8  --may_ipath:/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.计算机词汇.out.词典.txt  --may_opath=None



=====
Private:
Private_Use_Area
,(0xd800, 0xdb80)
: 'High Surrogates'
,(0xdb80, 0xdc00)
: 'High Private Use Surrogates'
,(0xdc00, 0xe000)
: 'Low Surrogates'
,(0xe000, 0xf900)
: 'Private Use Area'
,(0xf0000, 0x100000)
: 'Supplementary Private Use Area-A'
,(0x100000, 0x110000)
: 'Supplementary Private Use Area-B'


=====
>>> ch = '\ue001'
>>> ch.encode('gbk')
Traceback (most recent call last):
    ...
UnicodeEncodeError: 'gbk' codec can't encode character '\ue001' in position 0: illegal multibyte sequence
>>> ch.encode('gb18030')
b'\xaa\xa2'
>>> b'\xaa\xa2'.decode('gbk')
Traceback (most recent call last):
    ...
UnicodeDecodeError: 'gbk' codec can't decode byte 0xaa in position 0: illegal multibyte sequence
>>> b'\xaa\xa2'.decode('gb18030')
'\ue001'



=====
echo $'\ue001'


echo $'\ue31a'


>>> '' == '\ue001'
True
>>> '' == '\ue31a'
True

view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.中华成语大词典.out.词汇.txt
    to find '' == '\ue31a'
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.中华成语大词典.out.词典.txt
/[\ue001\ue003\ue23f\ue248\ue29e\ue2c3\ue31a\ue325\ue33e\ue34b\ue3a5\ue3fe\ue434\ue4b4\ue4be\ue4c1\ue4c6\ue5c5\ue81b\ue825\ue844]


=====




#]]]'''
__all__ = r'''

tribool_to_012_
is_hz__tribool_
    is_hz__012_

    range2block_name4Private_Use_Area__5__ucd__Blocks_txt__ver13_0
    pua__Ranges__ver13_0
    cjk_block_Ranges__ver13_0
    cjk_Ranges__ver13_0
    readonly__char_pt2code_block_name4ver13_0


    partition_charset_by_is_hz_

read_charset__uint_set5path_
    partition_charset_by_is_hz__5path_
        show_partition_charset_by_is_hz__5path_


'''.split()#'''
__all__


#from pathlib import Path
from seed.io.may_open import open4w, open4w_err, open4r
from seed.tiny import mk_fprint, expectError
from seed.tiny import check_type_is

from seed.tiny import xs_to_k2vs_, xs_to_vss_, partition_xs_by_bool_
from seed.data_funcs.rngs import (
    sorted_unique_ints_to_iter_nontouch_ranges
    ,make_NonTouchRanges
    ,make_Ranges
    )
from nn_ns.CJK.CJK_data.raw.汉字相关字符范围 import union_ranges, union_ranges__exclude_Private_Use_Area
from nn_ns.CJK.CJK_data.raw.汉字相关字符范围 import union_Ranges, union_Ranges__exclude_Private_Use_Area
from nn_ns.CJK.CJK_data.raw.汉字相关字符范围 import range2block_name__5__ucd__Blocks_txt__ver13_0 as range2block_name4CJK__5__ucd__Blocks_txt__ver13_0
from nn_ns.CJK.CJK_data.raw.汉字相关字符范围 import diff___ranges5ucd__Blocks_txt__ver13_0___union_Ranges
from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__Blocks_txt import findout_available_version_strs, load_readonly_char_pt2code_block_name_from_compact_result_file__ver, load_readonly_code_block_name2char_pt_rngs_from_compact_result_file__ver

import unicodedata

def _t():
    for i,j in diff___ranges5ucd__Blocks_txt__ver13_0___union_Ranges:
        s = ''.join(map(chr, range(i,j)))
        print(hex(i), hex(j), s)
        for u in range(i,j):
            may_nm = unicodedata.name(chr(u), None)
            if not may_nm is None:
                print(f'0x{u:X}:{may_nm}')
if __name__ == "__main__":
    _t()


range2block_name4Surrogate__5__ucd__Blocks_txt__ver13_0 = (
{(0xd800, 0xdb80)
: 'High Surrogates'
,(0xdb80, 0xdc00)
: 'High Private Use Surrogates'
,(0xdc00, 0xe000)
: 'Low Surrogates'
}
)

chr(0x11_00_00-1)
#chr(0x11_00_00)
    #ValueError: chr() arg not in range(0x110000)
assert expectError(ValueError, lambda:chr(0x11_00_00))

range2block_name4Private_Use_Area__5__ucd__Blocks_txt__ver13_0 = (
{(0xe000, 0xf900)
: 'Private Use Area'
,(0xf0000, 0x100000)
: 'Supplementary Private Use Area-A'
,(0x100000, 0x110000)
: 'Supplementary Private Use Area-B'
}
)


surrogate__Ranges__ver13_0 = make_Ranges(range2block_name4Surrogate__5__ucd__Blocks_txt__ver13_0.keys())
pua__Ranges__ver13_0 = make_Ranges(range2block_name4Private_Use_Area__5__ucd__Blocks_txt__ver13_0.keys())
cjk_block_Ranges__ver13_0 = make_Ranges(range2block_name4CJK__5__ucd__Blocks_txt__ver13_0.keys())
cjk_Ranges__ver13_0 = union_Ranges__exclude_Private_Use_Area
assert chr(0x3007) == '〇'
assert [*(cjk_Ranges__ver13_0 -cjk_block_Ranges__ver13_0)] == [0x3007]
    # <<== 区末尾 包含 非字符(非赋值的点)
    #

readonly__char_pt2code_block_name4ver13_0 = load_readonly_char_pt2code_block_name_from_compact_result_file__ver('ver13_0')

def is_hz__tribool_(ch, /):
    u = ord(ch)
    return _is_hz__tribool_(u)
def _is_hz__tribool_(u, /):
    if u in cjk_Ranges__ver13_0:
        # is hz
        return True
    if u in cjk_block_Ranges__ver13_0:
        # maybe hz
        # <<== 区末尾 包含 非字符(非赋值的点)
        return ...
    if u in pua__Ranges__ver13_0:
        # maybe hz
        return ...
    if not (0 <= u < 0x11_00_00) or u in surrogate__Ranges__ver13_0:
        raise ValueError(f'not unicode char pt: 0x{u:X}')
    if u in readonly__char_pt2code_block_name4ver13_0:
        # non-cjk-char block
        return False
    #未赋值@unicode-ver13_0
    return ...
def tribool_to_012_(t, /):
    if t is ...:
        return 0
    if t is False:
        return 1
    if t is True:
        return 2
    raise TypeError(type(t))

def is_hz__012_(ch, /):
    return tribool_to_012_(is_hz__tribool_(ch))
def _is_hz__012_(u, /):
    return tribool_to_012_(_is_hz__tribool_(u))




def partition_charset_by_is_hz_(s, /):
    us = sorted({*map(ord, s)})
    return _partition_charset_by_is_hz__uints_(us)
def _partition_charset_by_is_hz__uints_(us, /):
    #is_hz__tribool_
    uss = us4unknown, us4noncjk, us4cjk = xs_to_vss_(3, _is_hz__012_, None, us)
    ss = (''.join(map(chr, us)) for us in uss)
    cs4unknown, cs4noncjk, cs4cjk = ss
    return (cs4unknown, cs4noncjk, cs4cjk)
assert partition_charset_by_is_hz_('111,。aQ 〇ㄅ阿') == ('', ' ,1Qa。', '〇ㄅ阿')

_sz4bk = 0x4000
def read_charset__uint_set5path_(may_ipath, /, *, encoding):
    check_type_is(str, encoding)
    if not encoding: raise ValueError
    us = set()
    #with open(ipath, 'rt', encoding=encoding) as ifile:
    with open4r(may_ipath, xencoding=encoding) as ifile:
        while 1:
            s = ifile.read(_sz4bk)
            if not s:
                break
            us.update(map(ord, s))
    return us
def partition_charset_by_is_hz__5path_(may_ipath, /, *, encoding):
    us = read_charset__uint_set5path_(may_ipath, encoding=encoding)
    assert type(us) is set
    us = sorted(us)
    return _partition_charset_by_is_hz__uints_(us)
def show_partition_charset_by_is_hz__5path_(*, may_ipath, may_opath, encoding, oencoding=..., force=False):
    if not encoding: raise TypeError
    if not oencoding: raise TypeError
    (cs4unknown, cs4noncjk, cs4cjk) = partition_charset_by_is_hz__5path_(may_ipath, encoding=encoding)

    if oencoding is ...:
        oencoding = encoding

    with open4w(may_opath, xencoding=oencoding, force=force) as ofile:
        fprint = mk_fprint(ofile)
        fprint(repr(cs4unknown))
            #almost: \uXXXX \U00XXXXXX
        fprint(repr(cs4noncjk))
            #contains "\r\n"
        fprint(cs4cjk)
            #without repr




from nn_ns.CJK.CJK_common.is_hz import is_hz__tribool_, partition_charset_by_is_hz_
from nn_ns.CJK.CJK_common.is_hz import *
