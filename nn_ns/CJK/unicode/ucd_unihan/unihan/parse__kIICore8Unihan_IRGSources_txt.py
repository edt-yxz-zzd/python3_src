#__all__:goto
r'''
parse unicode::Unihan::kIICore8Unihan_IRGSources.txt

nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kIICore8Unihan_IRGSources_txt
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kIICore8Unihan_IRGSources_txt

.+1,$s/Blocks/kIICore8Unihan_IRGSources/g
.+1,$s/UCD\C/Unihan/g
.+1,$s/\<ucd\>\C/unihan/g
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kIICore8Unihan_IRGSources_txt.py



from nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kIICore8Unihan_IRGSources_txt import parse__kIICore8Unihan_IRGSources_txt, helper4parse__Unihan_kIICore8Unihan_IRGSources_txt

======================
view /sdcard/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_IRGSources.txt
======================
view ../../python3_src/seed/data_funcs/rngs.py
    # [ABC][GHJKMPT]{1,7}
    level_char2char_pt_rngs
    sourceIRG_char2char_pt_rngs
        :: Map<char, NonTouchRanges>
        :: Map<char, StackStyleSimpleIntSet>

======================

[
view ../lots/NOTE/unicode/note4UnicodeStandard_14_0_annex/unicode_ver14_0_UAX31_UAX38摘要.txt
  ===
  kIICore
  Syntax 	[ABC][GHJKMPT]{1,7}
  Description 	Used for characters which are in IICore, the IRG-produced minimal set of required ideographs for East Asian use. A character is in IICore if and only if it has a value for the kIICore field.
  Each value consists of a letter (A, B, or C), indicating priority value, and one or more letters (G, H, J, K, M, P, or T), indicating source. The source letters are the same as used for IRG sources, except that "P" is used instead of "KP".
  ===
  cjkIICore                ; kIICore
  # cjkIICore (cjkIICore)
  # @missing: 0000..10FFFF; cjkIICore; <none>
  U+34E4	kIICore	CH
    #㓤
  U+3577	kIICore	CT
    #㕷
  U+35CE	kIICore	BHM
    #㗎
  U+3960	kIICore	CK
    #㥠
  U+39DF	kIICore	CG
  U+3ED0	kIICore	CP
  ...
  U+4E00	kIICore	AGTJHKMP
    #一
  #最核心字集，搜索:『\t\<A[GHJKMPT]\{7}\>』
  ===
]



======================
.dataobj
    :: (parsed_result, extra_derived_result)
    mutable
.state
    = compact_result
    mutable

======================
.parsed_result
    :: (level_char2char_pt_rngs, sourceIRG_char2char_pt_rngs)
    mutable
.extra_derived_result
    :: levelA_common_char_pt_rngs
    immutable
.compact_result
    ===ver5:
    :: cased_char2char_pt_rngs__len_rng2begin_chars
    ===ver4:
    :: cased_char2char_pt_rngs__len_rng2hexbegins_str
    ===ver3:
    :: cased_char2char_pt_rngs__len_rng2hexbegins
    ===ver2:
    :: cased_char2char_pt_rngs__hexXhexszpair_list
        mutable
    ===ver1:发现存储文件500多K，进一步缩减！
    :: cased_char2char_pt_rngs__HexReprInt
        mutable


======================
.level_char2char_pt_rngs/.sourceIRG_char2char_pt_rngs
    :: {char:NonTouchRanges}
        mutable
    :: (tmp) {char:StackStyleSimpleIntSet}
        mutable
    ###conceptual:
    :: {char: [(int, int)]}
    :: {char: [(HexReprInt, HexReprInt)]}
.levelA_common_char_pt_rngs
    :: NonTouchRanges
        immutable
.cased_char2char_pt_rngs__len_rng2begin_chars
    #ver5
    :: (literal_store) {f'{case}={key_char}': {len_rng/int: "".join(map(chr,begins))}}
.cased_char2char_pt_rngs__len_rng2hexbegins_str
    #ver4
    :: (literal_store) {f'{case}={key_char}': {len_rng/int: ",".join(f"{begin:X}"...)}}
.cased_char2char_pt_rngs__len_rng2hexbegins
    #ver3
    :: (literal_store) {f'{case}={key_char}': {len_rng/int: [begin/HexReprInt]}}
.cased_char2char_pt_rngs__hexXhexszpair_list
    #ver2
    :: (literal_store) {f'{case}={key_char}': [(HexReprInt|(HexReprInt, len_rng/int{>=2}))]}
.cased_char2char_pt_rngs
.cased_char2char_pt_rngs__HexReprInt
    #ver1
    # st 4 store
    :: (literal_store) {f'{case}={key_char}': [(HexReprInt, HexReprInt)]}
        mutable
    case = "lvl" | "src"
    ###conceptual:
    :: {str: [(int, int)]}
======================




#'''


__all__ = '''
    parse__kIICore8Unihan_IRGSources_txt
    helper4parse__Unihan_kIICore8Unihan_IRGSources_txt

    '''.split()



___begin_mark_of_excluded_global_names__0___ = ...
from seed.data_funcs.rngs import make_Ranges, StackStyleSimpleIntSet, NonTouchRanges


from seed.io.fielded_line_utils import fielded_lines_parserT__tuple#, lines_handler2txt_handler, fielded_lines_preprocesserT, lines_preprocesserT
from seed.io.fielded_line_utils import line_splitT, hex2int, line_remove_prefixT

#from seed.tiny_.HexReprInt import HexReprInt
#from seed.func_tools.fmapT.fmapT__tiny import fmapT__dict, fmap_rngs2hex_repr, fmapT__pairs#, fmapT__list, fmapT__iter, fmapT__tuple, fmapT__tpls
#from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__tuple, fmapT__list
from seed.func_tools.fmapT.predT__tiny import (dot, eqT)
from seed.func_tools.fmapT.filterT__tiny import (filterT)

from collections import defaultdict
from seed.tiny import fmap4dict_value, dict_add__is#, filter4dict_value, dict_add__eq
#from seed.data_funcs.rngs import ranges2hex_repr_pair_list, ranges5hex_repr_pair_list
#>>> IRanges.from_hex_repr_pair_list(hex_repr_pair_list)
#>>> ranges.to_hex_repr_pair_list()
#>>> IRanges.from_hexXhexszpair_list(xs)
#>>> ranges.to_hexXhexszpair_list()
#>>> IRanges.from_len_rng2hexbegins(d)
#>>> ranges.to_len_rng2hexbegins()

from seed.tiny import MapView, echo, at, check_type_is, print_err
from seed.helper.IHelper4parse__xxx_txt import IHelper4parse__xxx_txt
from seed.abc.abc__ver0 import override


___end_mark_of_excluded_global_names__0___ = ...








_basic_lines_parser4Unihan_IRGSources_txt = fielded_lines_parserT__tuple('\t', '#', [dot[hex2int, line_remove_prefixT('U+')], echo, echo], keep_space_lines=False, keep_bifix_spaces4field=False)

_lines_parser4kIICore8Unihan_IRGSources_txt = dot[filterT(dot[eqT('kIICore'), at[1]]), _basic_lines_parser4Unihan_IRGSources_txt]






def parse__kIICore8Unihan_IRGSources_txt(lines, /):
    '-> parsed_result::(level_char2char_pt_rngs, sourceIRG_char2char_pt_rngs)'

    fieldss = _lines_parser4kIICore8Unihan_IRGSources_txt(lines)
    pt_kIICore_lvlsrcs_triples = fieldss

    level_char2char_pt_rngs = defaultdict(StackStyleSimpleIntSet)
    sourceIRG_char2char_pt_rngs = defaultdict(StackStyleSimpleIntSet)

    def mk_err_msg(s, /):
        return (f'{s!s}: {hex(char_pt)}-{chr(char_pt)}-{lvlsrcs!r}')
    for char_pt, kIICore, lvlsrcs in pt_kIICore_lvlsrcs_triples:
        assert kIICore == 'kIICore'
        level_char = lvlsrcs[0]
        sourceIRG_chars = lvlsrcs[1:]
        if not sourceIRG_chars:raise TypeError(mk_err_msg('bad format'))
        if 1:
            if not len(sourceIRG_chars)==len({*sourceIRG_chars}):raise TypeError(mk_err_msg('bad format: duplicated sourceIRG_chars'))
        else:
            if not len(sourceIRG_chars)==len({*sourceIRG_chars}):
                print_err(mk_err_msg('error:warning: duplicated sourceIRG_chars'))
                sourceIRG_chars = set(sourceIRG_chars)

        for sourceIRG_char in sourceIRG_chars:
            sourceIRG_char2char_pt_rngs[sourceIRG_char].add(char_pt)
        level_char2char_pt_rngs[level_char].add(char_pt)

    level_char2char_pt_rngs = fmap4dict_value(StackStyleSimpleIntSet.to_NonTouchRanges, level_char2char_pt_rngs)
    sourceIRG_char2char_pt_rngs = fmap4dict_value(StackStyleSimpleIntSet.to_NonTouchRanges, sourceIRG_char2char_pt_rngs)

    parsed_result = (level_char2char_pt_rngs, sourceIRG_char2char_pt_rngs)
    return parsed_result


#[[[
class Helper4parse__Unihan_kIICore8Unihan_IRGSources_txt(IHelper4parse__xxx_txt):
    @override
    def _parse__fin_(sf, fin, /):
        '-> parsed_result'
        lines = iter(fin)
        return parse__kIICore8Unihan_IRGSources_txt(lines)

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
            #bug:return fmapT__tuple(MapView)(parsed_result)
            #       should be fmapT__tuple(MapView, MapView)...
            return tuple(map(MapView, parsed_result))
        def _parsed_result5readonly_(sf, readonly__parsed_result, /):
            'readonly__parsed_result -> parsed_result'
            #bug:return fmapT__tuple(dict)(parsed_result)
            return tuple(map(dict, readonly__parsed_result))
helper4parse__Unihan_kIICore8Unihan_IRGSources_txt = Helper4parse__Unihan_kIICore8Unihan_IRGSources_txt()

#]]]


class Cases:
    case4level_char = 'lvl'
    case4sourceIRG_char = 'src'
    sep = '-'

def _parsed_result2extra(parsed_result, /):
    (level_char2char_pt_rngs, sourceIRG_char2char_pt_rngs) = parsed_result
    levelA_char_pt_rngs = level_char2char_pt_rngs['A']

    # /-\~
    common = levelA_char_pt_rngs
    for char_pt_rngs in sourceIRG_char2char_pt_rngs.values():
        common &= char_pt_rngs
    levelA_common_char_pt_rngs = common

    if 0:
        sz = levelA_common_char_pt_rngs.len_ints()
        extra_derived_result = (sz, levelA_common_char_pt_rngs)

    check_type_is(NonTouchRanges, levelA_common_char_pt_rngs)
    extra_derived_result = levelA_common_char_pt_rngs
    return extra_derived_result









def _parsed_result2compact(parsed_result, /):
    #_parsed_result5compact
    (level_char2char_pt_rngs, sourceIRG_char2char_pt_rngs) = parsed_result
    ps = [
    (Cases.case4level_char, level_char2char_pt_rngs)
    ,(Cases.case4sourceIRG_char, sourceIRG_char2char_pt_rngs)
    ]

    sep = Cases.sep
    cased_char2char_pt_rngs = {
        #bug:f'{case}{sep}{char}': char2char_pt_rngs
        f'{case}{sep}{char}': char_pt_rngs
        for case, char2char_pt_rngs in ps
        for char, char_pt_rngs in char2char_pt_rngs.items()
        }
    assert len(cased_char2char_pt_rngs) == sum(map(len, parsed_result))

    if 0:
        #ver1
        cased_char2char_pt_rngs__HexReprInt = fmap4dict_value(NonTouchRanges.to_hex_repr_pair_list, cased_char2char_pt_rngs)
        compact_result = cased_char2char_pt_rngs__HexReprInt
    elif 0:
        #ver2
        cased_char2char_pt_rngs__hexXhexszpair_list = fmap4dict_value(NonTouchRanges.to_hexXhexszpair_list, cased_char2char_pt_rngs)
        compact_result = cased_char2char_pt_rngs__hexXhexszpair_list
    elif 0:
        #ver3
        cased_char2char_pt_rngs__len_rng2hexbegins = fmap4dict_value(NonTouchRanges.to_len_rng2hexbegins, cased_char2char_pt_rngs)
        compact_result = cased_char2char_pt_rngs__len_rng2hexbegins
    elif 0:
        #ver4
        cased_char2char_pt_rngs__len_rng2hexbegins_str = fmap4dict_value(NonTouchRanges.to_len_rng2hexbegins_str, cased_char2char_pt_rngs)
        compact_result = cased_char2char_pt_rngs__len_rng2hexbegins_str
    else:
        #ver5
        cased_char2char_pt_rngs__len_rng2begin_chars = fmap4dict_value(NonTouchRanges.to_len_rng2begin_chars, cased_char2char_pt_rngs)
        compact_result = cased_char2char_pt_rngs__len_rng2begin_chars
    return compact_result

    #if not _parsed_result5compact(compact_result) == parsed_result: raise logic-err
    #   verify via IHelper4parse__xxx_txt
    return compact_result



def _parsed_result5compact(compact_result, /):
    #_parsed_result2compact
    #take care! using HexReprInt
    #should covert to int
    if 0:
        #ver1
        cased_char2char_pt_rngs__HexReprInt = compact_result
        cased_char2char_pt_rngs = fmap4dict_value(NonTouchRanges.from_hex_repr_pair_list, cased_char2char_pt_rngs__HexReprInt)
    elif 0:
        #ver2
        cased_char2char_pt_rngs__hexXhexszpair_list = compact_result
        cased_char2char_pt_rngs = fmap4dict_value(NonTouchRanges.from_hexXhexszpair_list, cased_char2char_pt_rngs__hexXhexszpair_list)
    elif 0:
        #ver3
        cased_char2char_pt_rngs__len_rng2hexbegins = compact_result
        cased_char2char_pt_rngs = fmap4dict_value(NonTouchRanges.from_len_rng2hexbegins, cased_char2char_pt_rngs__len_rng2hexbegins)
    elif 0:
        #ver4
        cased_char2char_pt_rngs__len_rng2hexbegins_str = compact_result
        cased_char2char_pt_rngs = fmap4dict_value(NonTouchRanges.from_len_rng2hexbegins_str, cased_char2char_pt_rngs__len_rng2hexbegins_str)
    else:
        #ver5
        cased_char2char_pt_rngs__len_rng2begin_chars = compact_result
        cased_char2char_pt_rngs = fmap4dict_value(NonTouchRanges.from_len_rng2begin_chars, cased_char2char_pt_rngs__len_rng2begin_chars)

    level_char2char_pt_rngs = {}
    sourceIRG_char2char_pt_rngs = {}

    sep = Cases.sep
    case_sep2d = {
        Cases.case4level_char+sep:level_char2char_pt_rngs
        ,Cases.case4sourceIRG_char+sep:sourceIRG_char2char_pt_rngs
        }

    for cased_char, char_pt_rngs in cased_char2char_pt_rngs.items():
        char = cased_char[-1]
        case_sep = cased_char[:-1]
        d = case_sep2d[case_sep]
        dict_add__is(d, char, char_pt_rngs)


    parsed_result = (level_char2char_pt_rngs, sourceIRG_char2char_pt_rngs)
    return parsed_result














from nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kIICore8Unihan_IRGSources_txt import parse__kIICore8Unihan_IRGSources_txt, helper4parse__Unihan_kIICore8Unihan_IRGSources_txt
