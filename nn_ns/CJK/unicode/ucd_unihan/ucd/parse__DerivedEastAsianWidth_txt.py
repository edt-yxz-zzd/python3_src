#__all__:goto
r'''[[[
NOTE:
    char_pt2east_asian_width.get(pt, 'N')
        !! buggy@N
    now:fixed:++kw:to_patch_missing

===
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedEastAsianWidth_txt.py
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__Blocks_txt.py
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/dump_load___parsed_result__of__DerivedEastAsianWidth_txt.py
view ../../python3_src/nn_ns/CJK/CJK_data/raw/U+FF00全角字符.txt
    保存格式:linefmt=f'{ea}@0x{i:X}+{sz}'
view ../lots/NOTE/Python/python-bug/unicodedata-bug.txt
    [py3_11_9:unicodedata.unidata_version=='14.0.0']:east_asian_width():bug!!


%s/code_block_name/east_asian_width/g
%s/Blocks/DerivedEastAsianWidth/g
======================
parse unicode::UCD::DerivedEastAsianWidth.txt

hex(0x30000+65534)
>>> hex(0x3250+7024)
'0x4dc0'
>>> hex(0x4E00+22157)
'0xa48d'
>>> hex(0xF900+512)
'0xfb00'
>>> hex(0x20000+65534)
'0x2fffe'
>>> hex(0x30000+65534)
'0x3fffe'

vs:
    view ../lots/NOTE/Python/python-bug/unicodedata-bug.txt
    [py3_11_9:unicodedata.unidata_version=='14.0.0']:east_asian_width():bug!!

parse-output is ok@W but buggy@N:
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedEastAsianWidth_txt.py.out.ver14_0.txt
buggy@N: #@ver14_0:
    #UserWarning: East_Asian_Width:has gaps:766583:[(888, 890), (896, 900), (907, 908), (909, 910), (930, 931), ..., (262142, 917505), (917506, 917536), (917632, 917760), (918000, 983040), (1048574, 1048576)]
    #UserWarning: East_Asian_Width:not cover whole code pt:766585:[(888, 890), (896, 900), (907, 908), (909, 910), (930, 931), ..., (917506, 917536), (917632, 917760), (918000, 983040), (1048574, 1048576), (1114110, 1114112)]
    766585 <<==:
        view /sdcard/0my_files/unzip/unicode14_0/UCD/extracted/DerivedEastAsianWidth.txt
            # The above property value applies to 766585 code points not listed here.
    now:fixed:++kw:to_patch_missing
ok@W: #@ver14_0:
W@0x3250+7024
    == [0x3250..<0x4dc0]
    > [U+3400..U+4DBF]
W@0x4E00+22157
    == [0x4E00..<0xa48d]
    > [U+4E00..U+9FFF]
W@0xF900+512
    == [0xF900..<0xfb00]
    == [U+F900..U+FAFF]
W@0x20000+65534
    == [0x20000..<0x2fffe]
    == [U+20000..U+2FFFD]
W@0x30000+65534
    == [0x30000..<0x3fffe]
    == [U+30000..U+3FFFD]
<<==:default:(N or W):
[[[
view /sdcard/0my_files/unzip/unicode14_0/UCD/EastAsianWidth.txt
===
# EastAsianWidth-14.0.0.txt
# Date: 2021-07-06, 09:58:53 GMT [KW, LI]
... ...
#
# The format is two fields separated by a semicolon.
# Field 0: Unicode code point value or range of code point values
# Field 1: East_Asian_Width property, consisting of one of the following values:
#         "A", "F", "H", "N", "Na", "W"
#  - All code points, assigned or unassigned, that are not listed
#      explicitly are given the value "N".
#  - The unassigned code points in the following blocks default to "W":
#         CJK Unified Ideographs Extension A: U+3400..U+4DBF
#         CJK Unified Ideographs:             U+4E00..U+9FFF
#         CJK Compatibility Ideographs:       U+F900..U+FAFF
#  - All undesignated code points in Planes 2 and 3, whether inside or
#      outside of allocated blocks, default to "W":
#         Plane 2:                            U+20000..U+2FFFD
#         Plane 3:                            U+30000..U+3FFFD
#
... ...
#
# @missing: 0000..10FFFF; N
0000..001F;N     # Cc    [32] <control-0000>..<control-001F>
... ...

]]]

======================
[[[
view /sdcard/0my_files/unzip/unicode14_0/UCD/extracted/DerivedEastAsianWidth.txt
===
# DerivedEastAsianWidth-14.0.0.txt
# Date: 2021-07-10, 00:35:07 GMT
# © 2021 Unicode®, Inc.
... ...
# @missing: 0000..10FFFF; Neutral

# ================================================

# East_Asian_Width=Neutral

0000..001F    ; N # Cc  [32] <control-0000>..<control-001F>
007F..009F    ; N # Cc  [33] <control-007F>..<control-009F>
00A0          ; N # Zs       NO-BREAK SPACE
00A9          ; N # So       COPYRIGHT SIGN
00AB          ; N # Pi       LEFT-POINTING DOUBLE ANGLE QUOTATION MARK
00B5          ; N # L&       MICRO SIGN
... ...
E0001         ; N # Cf       LANGUAGE TAG
E0020..E007F  ; N # Cf  [96] TAG SPACE..CANCEL TAG

# The above property value applies to 766585 code points not listed here.
# Total code points: 792645

# ================================================

# East_Asian_Width=Ambiguous

00A1          ; A # Po       INVERTED EXCLAMATION MARK
00A4          ; A # Sc       CURRENCY SIGN
... ...
F0000..FFFFD  ; A # Co [65534] <private-use-F0000>..<private-use-FFFFD>
100000..10FFFD; A # Co [65534] <private-use-100000>..<private-use-10FFFD>

# Total code points: 138739

# ================================================

# East_Asian_Width=Halfwidth

20A9          ; H # Sc       WON SIGN
FF61          ; H # Po       HALFWIDTH IDEOGRAPHIC FULL STOP
FF62          ; H # Ps       HALFWIDTH LEFT CORNER BRACKET
FF63          ; H # Pe       HALFWIDTH RIGHT CORNER BRACKET
FF64..FF65    ; H # Po   [2] HALFWIDTH IDEOGRAPHIC COMMA..HALFWIDTH KATAKANA MIDDLE DOT
FF66..FF6F    ; H # Lo  [10] HALFWIDTH KATAKANA LETTER WO..HALFWIDTH KATAKANA LETTER SMALL TU
... ...
FFE9..FFEC    ; H # Sm   [4] HALFWIDTH LEFTWARDS ARROW..HALFWIDTH DOWNWARDS ARROW
FFED..FFEE    ; H # So   [2] HALFWIDTH BLACK SQUARE..HALFWIDTH WHITE CIRCLE

# Total code points: 123

# ================================================

# East_Asian_Width=Wide

1100..115F    ; W # Lo  [96] HANGUL CHOSEONG KIYEOK..HANGUL CHOSEONG FILLER
231A..231B    ; W # So   [2] WATCH..HOURGLASS
2329          ; W # Ps       LEFT-POINTING ANGLE BRACKET
232A          ; W # Pe       RIGHT-POINTING ANGLE BRACKET
23E9..23EC    ; W # So   [4] BLACK RIGHT-POINTING DOUBLE TRIANGLE..BLACK DOWN-POINTING DOUBLE TRIANGLE
23F0          ; W # So       ALARM CLOCK
... ...
30000..3134A  ; W # Lo [4939] CJK UNIFIED IDEOGRAPH-30000..CJK UNIFIED IDEOGRAPH-3134A
3134B..3FFFD  ; W # Cn [60595] <reserved-3134B>..<reserved-3FFFD>

# Total code points: 182390

# ================================================

# East_Asian_Width=Fullwidth

3000          ; F # Zs       IDEOGRAPHIC SPACE
FF01..FF03    ; F # Po   [3] FULLWIDTH EXCLAMATION MARK..FULLWIDTH NUMBER SIGN
FF04          ; F # Sc       FULLWIDTH DOLLAR SIGN
FF05..FF07    ; F # Po   [3] FULLWIDTH PERCENT SIGN..FULLWIDTH APOSTROPHE
FF08          ; F # Ps       FULLWIDTH LEFT PARENTHESIS
FF09          ; F # Pe       FULLWIDTH RIGHT PARENTHESIS
... ...
FFE4          ; F # So       FULLWIDTH BROKEN BAR
FFE5..FFE6    ; F # Sc   [2] FULLWIDTH YEN SIGN..FULLWIDTH WON SIGN

# Total code points: 104

# ================================================

# East_Asian_Width=Narrow

0020          ; Na # Zs       SPACE
0021..0023    ; Na # Po   [3] EXCLAMATION MARK..NUMBER SIGN
0024          ; Na # Sc       DOLLAR SIGN
0025..0027    ; Na # Po   [3] PERCENT SIGN..APOSTROPHE
0028          ; Na # Ps       LEFT PARENTHESIS
0029          ; Na # Pe       RIGHT PARENTHESIS
... ...
27ED          ; Na # Pe       MATHEMATICAL RIGHT WHITE TORTOISE SHELL BRACKET
2985          ; Na # Ps       LEFT WHITE PARENTHESIS
2986          ; Na # Pe       RIGHT WHITE PARENTHESIS

# Total code points: 111

# EOF

]]]






======================
nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedEastAsianWidth_txt
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedEastAsianWidth_txt -x

from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedEastAsianWidth_txt import parse__DerivedEastAsianWidth_txt, helper4parse__UCD_DerivedEastAsianWidth_txt


#]]]'''
__all__ = r'''
parse__DerivedEastAsianWidth_txt
    helper4parse__UCD_DerivedEastAsianWidth_txt

Helper4parse__UCD_DerivedEastAsianWidth_txt
'''.split()#'''
__all__




___begin_mark_of_excluded_global_names__0___ = ...
import warnings

from seed.data_funcs.rngs import StackStyleSimpleIntSet, StackStyleSimpleIntMapping, TouchRangeBasedIntMapping
from seed.data_funcs.rngs import make_Ranges#, sorted_ints_to_iter_nontouch_ranges, detect_iter_ranges

from seed.io.fielded_line_utils import lines_handler2txt_handler, fielded_lines_parserT__tuple, fielded_lines_preprocesserT, lines_preprocesserT
from seed.io.fielded_line_utils import line_splitT, hex2int
from seed.io.fielded_line_utils import unicode_char_pt_rng5field

from seed.tiny_.HexReprInt import HexReprInt
from seed.func_tools.fmapT.fmapT__tiny import fmapT__dict, fmap_rngs2hex_repr#, fmapT__list, fmapT__iter, fmapT__tuple, fmapT__tpls, fmapT__pairs
from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__tuple, fmapT__list

from collections import defaultdict
from seed.tiny import fmap4dict_value
from seed.tiny import MapView, echo, fst, snd
#from nn_ns.CJK.unicode.ucd_unihan.ucd.IHelper4parse__xxx_txt import IHelper4parse__xxx_txt
from seed.helper.IHelper4parse__xxx_txt import IHelper4parse__xxx_txt
from seed.abc.abc__ver0 import override


___end_mark_of_excluded_global_names__0___ = ...








_example4lines_parser4UCD_DerivedEastAsianWidth_txt = fielded_lines_parserT__tuple(';', '#', [unicode_char_pt_rng5field, echo], keep_space_lines=False, keep_bifix_spaces4field=False)
_example4txt_parser4UCD_DerivedEastAsianWidth_txt = lines_handler2txt_handler(_example4lines_parser4UCD_DerivedEastAsianWidth_txt)



def _cut_too_many_rngs(rngs, /):
    from seed.tiny import repr_as_3dot
    if len(rngs) > 10:
        rngs = [*rngs[:5], repr_as_3dot, *rngs[-5:]]
    else:
        rngs = [*rngs]
    return rngs


def parse__DerivedEastAsianWidth_txt(lines, /, *, to_patch_missing:bool):
    '-> parsed_result::char_pt2east_asian_width'

    fieldss = _example4lines_parser4UCD_DerivedEastAsianWidth_txt(lines)
    rng_ea_pairs = fieldss
    rng_ea_pairs = sorted(rng_ea_pairs)

    _whole = make_Ranges([(0, 0x11_00_00)])
    if to_patch_missing:
        _missing = _whole -make_Ranges(map(fst, rng_ea_pairs))
        rng_ea_pairs.extend((rng, 'N') for rng in _missing.ranges)
        rng_ea_pairs.sort()


    char_pt2east_asian_width = TouchRangeBasedIntMapping.from_rng_value_pairs(rng_ea_pairs)
    gaps = char_pt2east_asian_width.gaps()
    if gaps:
        _sz = make_Ranges(gaps).len_ints()
        _gaps = _cut_too_many_rngs(gaps)
        warnings.warn(f'East_Asian_Width:has gaps:{_sz}:{_gaps}')
            #@ver14_0:
            #UserWarning: East_Asian_Width:has gaps:766583:[(888, 890), (896, 900), (907, 908), (909, 910), (930, 931), ..., (262142, 917505), (917506, 917536), (917632, 917760), (918000, 983040), (1048574, 1048576)]

    _all_ranges = char_pt2east_asian_width.to_NonTouchRanges()
    if not _all_ranges == _whole:
        rs = _whole -_all_ranges
        _sz = rs.len_ints()
        rs = rs.ranges
        _rs = _cut_too_many_rngs(rs)
        warnings.warn(f'East_Asian_Width:not cover whole code pt:{_sz}:{_rs}')
            #@ver14_0:
            #UserWarning: East_Asian_Width:not cover whole code pt:766585:[(888, 890), (896, 900), (907, 908), (909, 910), (930, 931), ..., (917506, 917536), (917632, 917760), (918000, 983040), (1048574, 1048576), (1114110, 1114112)]

    parsed_result = char_pt2east_asian_width
    readonly__parsed_result = parsed_result
    return readonly__parsed_result


#[[[
class Helper4parse__UCD_DerivedEastAsianWidth_txt(IHelper4parse__xxx_txt):
    @override
    def _parse__fin_(sf, fin, /):
        '-> parsed_result'
        lines = iter(fin)
        return parse__DerivedEastAsianWidth_txt(lines, to_patch_missing=True)

    @override
    def _parsed_result2extra_(sf, parsed_result, /):
        'parsed_result -> extra_derived_result #not bijection'
        return _parsed_result2extra(parsed_result)
    @override
    def _parsed_result5compact_(sf, compact_result, /):
        'compact_result -> parsed_result'
        return _parsed_result5compact(compact_result)
    @override
    def _parsed_result2compact_(sf, parsed_result, /):
        'parsed_result -> compact_result'
        return _parsed_result2compact(parsed_result)

    if 1:
        _parsed_result__is__readonly_ = True
        _extra_derived_result__is__readonly_ = False
        def _extra_derived_result2readonly_(sf, extra_derived_result, /):
            'extra_derived_result -> readonly__extra_derived_result'
            return MapView(extra_derived_result)
        def _extra_derived_result5readonly_(sf, readonly__extra_derived_result, /):
            'readonly__extra_derived_result -> extra_derived_result'
            return {**readonly__extra_derived_result}
helper4parse__UCD_DerivedEastAsianWidth_txt = Helper4parse__UCD_DerivedEastAsianWidth_txt()

#]]]



def _parsed_result2extra(parsed_result, /):
    char_pt2east_asian_width = parsed_result
    d = defaultdict(StackStyleSimpleIntSet)
    for rng, ea in char_pt2east_asian_width.iter_rng_value_pairs_(reverse=False):
        d[ea].push_rng(rng)
    east_asian_width2char_pt_rngs = fmap4dict_value(StackStyleSimpleIntSet.to_NonTouchRanges, d)

    #east_asian_width2char_pt_rngs = MapView(east_asian_width2char_pt_rngs)
    extra_derived_result = east_asian_width2char_pt_rngs
    return extra_derived_result

def _keyed_line5rng_nm_pair(rng_nm_pair, /):
    line = _line5rng_nm_pair(rng_nm_pair)
    (i,j), nm = rng_nm_pair
    k = (nm, i, j)
    return (k, line)
def _line5rng_nm_pair(rng_nm_pair, /):
    (i,j), nm = rng_nm_pair
    assert nm.isidentifier()
    sz = j-i
    line = f'{nm}@0x{i:X}+{sz}'
    return line
def _line2rng_nm_pair(line, /):
    nm, s = line.rsplit('@0x', 1)
    hx4i, s4sz = s.split('+')
    i = hex2int(hx4i)
    sz = int(s4sz)
    j = i+sz
    rng_nm_pair = (i,j), nm
    return rng_nm_pair
assert ((__tmp0:=((999, 7777), 'aaa')) == (__tmp2:=_line2rng_nm_pair(__tmp1:=_line5rng_nm_pair(__tmp0)))), (__tmp0, __tmp1, __tmp2)


def _parsed_result2compact(parsed_result, /):
    #_parsed_result5compact
    char_pt2east_asian_width = parsed_result
    if 0:
        lines = map(_line5rng_nm_pair, char_pt2east_asian_width.iter_rng_value_pairs_(reverse=False))
        lines = sorted(lines)
    else:
        keyed_lines = map(_keyed_line5rng_nm_pair, char_pt2east_asian_width.iter_rng_value_pairs_(reverse=False))
        keyed_lines = sorted(keyed_lines)
        lines = map(snd, keyed_lines)
    lines
    txt = '\n'.join(lines)
    compact_result = txt
    return compact_result

    # char_pt2east_asian_width = parsed_result

    # char_pt_rng2east_asian_width = {(*map(HexReprInt, rng),):ea for rng, ea in char_pt2east_asian_width.iter_rng_value_pairs_(reverse=False)}
    # compact_result = char_pt_rng2east_asian_width

    # #if not _parsed_result5compact(compact_result) == parsed_result: raise logic-err
    # #   verify via IHelper4parse__xxx_txt
    # return compact_result



def _parsed_result5compact(compact_result, /):
    #_parsed_result2compact
    txt = compact_result
    lines = txt.split()
    rng_ea_pairs = map(_line2rng_nm_pair, lines)
    rng_ea_pairs = sorted(rng_ea_pairs)
    char_pt2east_asian_width = TouchRangeBasedIntMapping.from_rng_value_pairs(rng_ea_pairs)
    parsed_result = char_pt2east_asian_width
    return parsed_result

    # char_pt_rng2east_asian_width = compact_result
    #     #take care! using HexReprInt
    #     #should covert to int

    # rng_ea_pairs___HexReprInt = sorted(char_pt_rng2east_asian_width.items())
    # rng_ea_pairs = [((*map(int, rng),), ea) for rng, ea in rng_ea_pairs___HexReprInt]


    # char_pt2east_asian_width = TouchRangeBasedIntMapping.from_rng_value_pairs(rng_ea_pairs)

    # parsed_result = char_pt2east_asian_width

    # return parsed_result














__all__
from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedEastAsianWidth_txt import parse__DerivedEastAsianWidth_txt, helper4parse__UCD_DerivedEastAsianWidth_txt
from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedEastAsianWidth_txt import Helper4parse__UCD_DerivedEastAsianWidth_txt
from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedEastAsianWidth_txt import *
