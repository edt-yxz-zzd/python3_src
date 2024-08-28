#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedGeneralCategory_txt.py
[format{DerivedGeneralCategory} === format{DerivedEastAsianWidth} except to_patch_missing]
    [Cn==Unassigned] ==>> [cover whole code pt set]
    [to_patch_missing==False] -> [no UserWarning]
    <<==:
    reuse:
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__DerivedEastAsianWidth_txt.py



%s/east_asian_width/general_category/g
%s/DerivedEastAsianWidth/DerivedGeneralCategory/g
======================
parse unicode::UCD::DerivedGeneralCategory.txt


======================
[[[
view /sdcard/0my_files/unzip/unicode14_0/UCD/extracted/DerivedGeneralCategory.txt
===
# DerivedGeneralCategory-14.0.0.txt
# Date: 2021-07-10, 00:35:08 GMT
... ...
# ================================================

# Property:	General_Category

# ================================================

# General_Category=Unassigned

0378..0379    ; Cn #   [2] <reserved-0378>..<reserved-0379>
0380..0383    ; Cn #   [4] <reserved-0380>..<reserved-0383>
038B          ; Cn #       <reserved-038B>
... ...
E01F0..EFFFF  ; Cn # [65040] <reserved-E01F0>..<noncharacter-EFFFF>
FFFFE..FFFFF  ; Cn #   [2] <noncharacter-FFFFE>..<noncharacter-FFFFF>
10FFFE..10FFFF; Cn #   [2] <noncharacter-10FFFE>..<noncharacter-10FFFF>

# Total code points: 829834

# ================================================

# General_Category=Uppercase_Letter

0041..005A    ; Lu #  [26] LATIN CAPITAL LETTER A..LATIN CAPITAL LETTER Z
00C0..00D6    ; Lu #  [23] LATIN CAPITAL LETTER A WITH GRAVE..LATIN CAPITAL LETTER O WITH DIAERESIS
00D8..00DE    ; Lu #   [7] LATIN CAPITAL LETTER O WITH STROKE..LATIN CAPITAL LETTER THORN
0100          ; Lu #       LATIN CAPITAL LETTER A WITH MACRON
0102          ; Lu #       LATIN CAPITAL LETTER A WITH BREVE
... ...
... ...
... ...
# ================================================

# General_Category=Control

0000..001F    ; Cc #  [32] <control-0000>..<control-001F>
007F..009F    ; Cc #  [33] <control-007F>..<control-009F>

# Total code points: 65

# ================================================

# General_Category=Format

00AD          ; Cf #       SOFT HYPHEN
0600..0605    ; Cf #   [6] ARABIC NUMBER SIGN..ARABIC NUMBER MARK ABOVE
... ...
... ...
... ...
# ================================================

# General_Category=Private_Use

E000..F8FF    ; Co # [6400] <private-use-E000>..<private-use-F8FF>
F0000..FFFFD  ; Co # [65534] <private-use-F0000>..<private-use-FFFFD>
100000..10FFFD; Co # [65534] <private-use-100000>..<private-use-10FFFD>

# Total code points: 137468

# ================================================

# General_Category=Surrogate

D800..DFFF    ; Cs # [2048] <surrogate-D800>..<surrogate-DFFF>

# Total code points: 2048

# ================================================
... ...
... ...
... ...
]]]




======================
nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedGeneralCategory_txt
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedGeneralCategory_txt -x

#]]]'''
__all__ = r'''
parse__DerivedGeneralCategory_txt
    helper4parse__UCD_DerivedGeneralCategory_txt

Helper4parse__UCD_DerivedGeneralCategory_txt
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedEastAsianWidth_txt import parse__DerivedEastAsianWidth_txt
from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedEastAsianWidth_txt import Helper4parse__UCD_DerivedEastAsianWidth_txt
from seed.abc.abc__ver0 import override
___end_mark_of_excluded_global_names__0___ = ...

def parse__DerivedGeneralCategory_txt(lines, /):
    '-> readonly-parsed_result::char_pt2general_category'
    return parse__DerivedEastAsianWidth_txt(lines, to_patch_missing=False)

class Helper4parse__UCD_DerivedGeneralCategory_txt(Helper4parse__UCD_DerivedEastAsianWidth_txt):
    @override
    def _parse__fin_(sf, fin, /):
        '-> parsed_result'
        lines = iter(fin)
        return parse__DerivedGeneralCategory_txt(lines)
helper4parse__UCD_DerivedGeneralCategory_txt = Helper4parse__UCD_DerivedGeneralCategory_txt()


__all__
from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedGeneralCategory_txt import parse__DerivedGeneralCategory_txt, helper4parse__UCD_DerivedGeneralCategory_txt

from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedGeneralCategory_txt import Helper4parse__UCD_DerivedGeneralCategory_txt
from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__DerivedGeneralCategory_txt import *
