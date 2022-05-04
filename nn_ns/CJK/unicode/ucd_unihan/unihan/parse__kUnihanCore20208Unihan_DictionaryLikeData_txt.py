#__all__:goto
r'''
parse unicode::Unihan::kUnihanCore20208Unihan_DictionaryLikeData.txt

nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kUnihanCore20208Unihan_DictionaryLikeData_txt
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kUnihanCore20208Unihan_DictionaryLikeData_txt

e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kUnihanCore20208Unihan_DictionaryLikeData_txt.py
copy from:
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kIICore8Unihan_IRGSources_txt.py
.+1,$s/kIICore\C/kUnihanCore2020/g
.+1,$s/Unihan_IRGSources\C/Unihan_DictionaryLikeData/g




from nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kUnihanCore20208Unihan_DictionaryLikeData_txt import parse__kUnihanCore20208Unihan_DictionaryLikeData_txt, helper4parse__Unihan_kUnihanCore20208Unihan_DictionaryLikeData_txt

======================
view /sdcard/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_DictionaryLikeData.txt
======================
view ../../python3_src/seed/data_funcs/rngs.py
    # [GHJKMPT]{1,7}
    sourceIRG_char2char_pt_rngs
        :: Map<char, NonTouchRanges>
        :: Map<char, StackStyleSimpleIntSet>

======================


[[kUnihanCore2020
  Unihan_DictionaryLikeData.txt 	kCangjie, kCheungBauer, kCihaiT, kFenn, kFourCornerCode, kFrequency, kGradeLevel, kHDZRadBreak, kHKGlyph, kPhonetic, kStrange, kUnihanCore2020
view ../lots/NOTE/unicode/note4UnicodeStandard_14_0_annex/unicode_ver14_0_UAX31_UAX38摘要.txt
[
Property 	kUnihanCore2020
Status 	Informative
Category 	Dictionary-like Data
Introduced 	13.0
Delimiter 	N/A
Syntax 	[GHJKMPT]{1,7}
Description 	Used for characters which are in the UnihanCore2020 set, the minimal set of required ideographs for East Asia. A character is in the UnihanCore2020 set if and only if it has a value for the kUnihanCore2020 property.

The property value consists of one or more letters (G, H, J, K, M, P, or T), indicating source. The source letters are the same as used for IRG sources, except that P is used instead of the two-letter sequence KP.
]
view /sdcard/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_DictionaryLikeData.txt
# Unihan_DictionaryLikeData.txt
# Date: 2020-02-18 18:27:33 GMT [JHJ]
# Unicode version: 13.0.0
grep kUnihanCore2020 /sdcard/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_DictionaryLikeData.txt > /sdcard/0my_files/tmp/_.txt
view /sdcard/0my_files/tmp/_.txt
  20720个！！！
!du -h /sdcard/0my_files/tmp/_.txt
  556K
!du -h ../../python3_src/nn_ns/CJK/cjk_subsets/hanzi.py
  164K
grep 'kUnihanCore2020\s\+\S\{7\}' /sdcard/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_DictionaryLikeData.txt > /sdcard/0my_files/tmp/_.txt
view /sdcard/0my_files/tmp/_.txt
  2573个

]]


======================
.dataobj
    :: (parsed_result, extra_derived_result)
    mutable
.state
    = compact_result
    mutable

======================
.parsed_result
    :: sourceIRG_char2char_pt_rngs
    mutable
.extra_derived_result
    :: common_char_pt_rngs
    immutable
.compact_result
    ===ver5:
    :: sourceIRG_char2char_pt_rngs__len_rng2begin_chars
        mutable

#ver5 come from:
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kIICore8Unihan_IRGSources_txt.py
======================
.sourceIRG_char2char_pt_rngs
    :: {char:NonTouchRanges}
        mutable
    :: (tmp) {char:StackStyleSimpleIntSet}
        mutable
    ###conceptual:
    :: {char: [(int, int)]}
    :: {char: [(HexReprInt, HexReprInt)]}
.common_char_pt_rngs
    :: NonTouchRanges
        immutable
.sourceIRG_char2char_pt_rngs__len_rng2begin_chars
    #ver5
    :: (literal_store) {char: {len_rng/int: "".join(map(chr,begins))}}
        mutable
    ###conceptual:
    :: {str: [(int, int)]}
======================




#'''


__all__ = '''
    parse__kUnihanCore20208Unihan_DictionaryLikeData_txt
    helper4parse__Unihan_kUnihanCore20208Unihan_DictionaryLikeData_txt

    '''.split()



___begin_mark_of_excluded_global_names__0___ = ...
from seed.data_funcs.rngs import make_Ranges, StackStyleSimpleIntSet, NonTouchRanges


from seed.io.fielded_line_utils import fielded_lines_parserT__tuple
from seed.io.fielded_line_utils import line_splitT, hex2int, line_remove_prefixT

#from seed.tiny_.HexReprInt import HexReprInt
from seed.func_tools.fmapT.predT__tiny import (dot, eqT)
from seed.func_tools.fmapT.filterT__tiny import (filterT)

from collections import defaultdict
from seed.tiny import fmap4dict_value#, dict_add__is, filter4dict_value, dict_add__eq

from seed.tiny import MapView, echo, at, check_type_is, print_err
from seed.helper.IHelper4parse__xxx_txt import IHelper4parse__xxx_txt
from seed.abc.abc__ver0 import override


___end_mark_of_excluded_global_names__0___ = ...








_basic_lines_parser4Unihan_DictionaryLikeData_txt = fielded_lines_parserT__tuple('\t', '#', [dot[hex2int, line_remove_prefixT('U+')], echo, echo], keep_space_lines=False, keep_bifix_spaces4field=False)

_lines_parser4kUnihanCore20208Unihan_DictionaryLikeData_txt = dot[filterT(dot[eqT('kUnihanCore2020'), at[1]]), _basic_lines_parser4Unihan_DictionaryLikeData_txt]






def parse__kUnihanCore20208Unihan_DictionaryLikeData_txt(lines, /):
    '-> parsed_result::sourceIRG_char2char_pt_rngs'

    fieldss = _lines_parser4kUnihanCore20208Unihan_DictionaryLikeData_txt(lines)
    pt_kUnihanCore2020_lvlsrcs_triples = fieldss

    sourceIRG_char2char_pt_rngs = defaultdict(StackStyleSimpleIntSet)

    def mk_err_msg(s, /):
        return (f'{s!s}: {hex(char_pt)}-{chr(char_pt)}-{srcs!r}')
    for char_pt, kUnihanCore2020, srcs in pt_kUnihanCore2020_lvlsrcs_triples:
        assert kUnihanCore2020 == 'kUnihanCore2020'
        sourceIRG_chars = srcs
        if not sourceIRG_chars:raise TypeError(mk_err_msg('bad format'))
        if 1:
            if not len(sourceIRG_chars)==len({*sourceIRG_chars}):raise TypeError(mk_err_msg('bad format: duplicated sourceIRG_chars'))
        else:
            if not len(sourceIRG_chars)==len({*sourceIRG_chars}):
                print_err(mk_err_msg('error:warning: duplicated sourceIRG_chars'))
                sourceIRG_chars = set(sourceIRG_chars)

        for sourceIRG_char in sourceIRG_chars:
            sourceIRG_char2char_pt_rngs[sourceIRG_char].add(char_pt)

    sourceIRG_char2char_pt_rngs = fmap4dict_value(StackStyleSimpleIntSet.to_NonTouchRanges, sourceIRG_char2char_pt_rngs)

    parsed_result = sourceIRG_char2char_pt_rngs
    return parsed_result


#[[[
class Helper4parse__Unihan_kUnihanCore20208Unihan_DictionaryLikeData_txt(IHelper4parse__xxx_txt):
    @override
    def _parse__fin_(sf, fin, /):
        '-> parsed_result'
        lines = iter(fin)
        return parse__kUnihanCore20208Unihan_DictionaryLikeData_txt(lines)

    #def parse__lines(sf, lines, /):
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
        _parsed_result__is__readonly_ = False
        _extra_derived_result__is__readonly_ = True
        def _parsed_result2readonly_(sf, parsed_result, /):
            'parsed_result -> readonly__parsed_result'
            return MapView(parsed_result)
        def _parsed_result5readonly_(sf, readonly__parsed_result, /):
            'readonly__parsed_result -> parsed_result'
            return dict(readonly__parsed_result)
helper4parse__Unihan_kUnihanCore20208Unihan_DictionaryLikeData_txt = Helper4parse__Unihan_kUnihanCore20208Unihan_DictionaryLikeData_txt()

#]]]



def _parsed_result2extra(parsed_result, /):
    sourceIRG_char2char_pt_rngs = parsed_result

    # /-\~
    it = iter(sourceIRG_char2char_pt_rngs.values())
    for common in it:
        break
    else:
        common = NonTouchRanges()
    for char_pt_rngs in it:
        common &= char_pt_rngs
    common_char_pt_rngs = common


    check_type_is(NonTouchRanges, common_char_pt_rngs)
    extra_derived_result = common_char_pt_rngs
    return extra_derived_result









def _parsed_result2compact(parsed_result, /):
    #_parsed_result5compact
    sourceIRG_char2char_pt_rngs = parsed_result

    if 1:
        #ver5
        sourceIRG_char2char_pt_rngs__len_rng2begin_chars = fmap4dict_value(NonTouchRanges.to_len_rng2begin_chars, sourceIRG_char2char_pt_rngs)
        compact_result = sourceIRG_char2char_pt_rngs__len_rng2begin_chars
    return compact_result

    #if not _parsed_result5compact(compact_result) == parsed_result: raise logic-err
    #   verify via IHelper4parse__xxx_txt
    return compact_result



def _parsed_result5compact(compact_result, /):
    #_parsed_result2compact
    #take care! using HexReprInt
    #should covert to int
    if 1:
        #ver5
        sourceIRG_char2char_pt_rngs__len_rng2begin_chars = compact_result
        sourceIRG_char2char_pt_rngs = fmap4dict_value(NonTouchRanges.from_len_rng2begin_chars, sourceIRG_char2char_pt_rngs__len_rng2begin_chars)


    parsed_result = sourceIRG_char2char_pt_rngs
    return parsed_result














from nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kUnihanCore20208Unihan_DictionaryLikeData_txt import parse__kUnihanCore20208Unihan_DictionaryLikeData_txt, helper4parse__Unihan_kUnihanCore20208Unihan_DictionaryLikeData_txt

