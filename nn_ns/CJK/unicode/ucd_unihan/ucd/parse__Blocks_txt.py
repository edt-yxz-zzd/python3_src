#__all__:goto
r'''
parse unicode::UCD::Blocks.txt

nn_ns.CJK.unicode.ucd_unihan.ucd.parse__Blocks_txt
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.ucd.parse__Blocks_txt

e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__Blocks_txt.py



from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__Blocks_txt import parse__Blocks_txt, helper4parse__UCD_Blocks_txt

======================
view /sdcard/0my_files/unzip/e_book/unicode_13__UCD/Blocks.txt
    2FF0..2FFF; Ideographic Description Characters
======================
view ../../python3_src/seed/data_funcs/rngs.py
======================





======================
.dataobj
    :: (char_pt2code_block_name, code_block_name2char_pt_rngs)
    :: (parsed_result, extra_derived_result)
    mutable
.state
    :: char_pt_rng2code_block_name
    = compact_result
    mutable

======================
.parsed_result
    :: char_pt2code_block_name
    = readonly__parsed_result
    immutable
.extra_derived_result
    :: code_block_name2char_pt_rngs
    mutable
.compact_result
    :: char_pt_rng2code_block_name
    mutable


======================
.char_pt2code_block_name
    :: TouchRangeBasedIntMapping<str>
        immutable
    :: (tmp) StackStyleSimpleIntMapping<str>
        mutable
.char_pt_rng2code_block_name
    # st 4 store
    :: (literal_store) {(HexReprInt, HexReprInt): str}
    ###conceptual:
    :: {(int, int): str}
.code_block_name2char_pt_rngs
    :: {str, NonTouchRanges}
        mutable
    :: (tmp) {str: StackStyleSimpleIntSet}
    ###conceptual:
    :: {str: [(int, int)]}
    :: {str: [(HexReprInt, HexReprInt)]}
======================




#'''


__all__ = '''
    parse__Blocks_txt
    helper4parse__UCD_Blocks_txt

    '''.split()



___begin_mark_of_excluded_global_names__0___ = ...
from seed.data_funcs.rngs import StackStyleSimpleIntSet, StackStyleSimpleIntMapping, TouchRangeBasedIntMapping
    #make_Ranges, sorted_ints_to_iter_nontouch_ranges, detect_iter_ranges

from seed.io.fielded_line_utils import lines_handler2txt_handler, fielded_lines_parserT__tuple, fielded_lines_preprocesserT, lines_preprocesserT
from seed.io.fielded_line_utils import line_splitT, hex2int

from seed.tiny_.HexReprInt import HexReprInt
from seed.func_tools.fmapT.fmapT__tiny import fmapT__dict, fmap_rngs2hex_repr#, fmapT__list, fmapT__iter, fmapT__tuple, fmapT__tpls, fmapT__pairs
from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__tuple, fmapT__list

from collections import defaultdict
from seed.tiny import fmap4dict_value#, filter4dict_value, dict_add__is, dict_add__eq
from seed.tiny import MapView, echo
#from nn_ns.CJK.unicode.ucd_unihan.ucd.IHelper4parse__xxx_txt import IHelper4parse__xxx_txt
from seed.helper.IHelper4parse__xxx_txt import IHelper4parse__xxx_txt
from seed.abc.abc__ver0 import override


___end_mark_of_excluded_global_names__0___ = ...








_example4lines_parser4UCD_Blocks_txt = fielded_lines_parserT__tuple(';', '#', [dot[fmapT__tuple(hex2int, dot[[int.__add__, 1], hex2int]), line_splitT('..')], echo], keep_space_lines=False, keep_bifix_spaces4field=False)
_example4txt_parser4UCD_Blocks_txt = lines_handler2txt_handler(_example4lines_parser4UCD_Blocks_txt)






def parse__Blocks_txt(lines, /):
    '-> parsed_result::(char_pt2code_block_name, code_block_name2char_pt_rngs)'

    fieldss = _example4lines_parser4UCD_Blocks_txt(lines)
    rng_name_pairs = fieldss
    #for char_pt_rng, code_block_name in rng_name_pairs:

    char_pt2code_block_name = TouchRangeBasedIntMapping.from_rng_value_pairs(rng_name_pairs)

    parsed_result = char_pt2code_block_name
    readonly__parsed_result = parsed_result
    return readonly__parsed_result


#[[[
class Helper4parse__UCD_Blocks_txt(IHelper4parse__xxx_txt):
    @override
    def _parse__fin_(sf, fin, /):
        '-> parsed_result'
        lines = iter(fin)
        return parse__Blocks_txt(lines)

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
        _parsed_result__is__readonly_ = True
        _extra_derived_result__is__readonly_ = False
        def _extra_derived_result2readonly_(sf, extra_derived_result, /):
            'extra_derived_result -> readonly__extra_derived_result'
            return MapView(extra_derived_result)
        def _extra_derived_result5readonly_(sf, readonly__extra_derived_result, /):
            'readonly__extra_derived_result -> extra_derived_result'
            return {**readonly__extra_derived_result}
helper4parse__UCD_Blocks_txt = Helper4parse__UCD_Blocks_txt()

#]]]



def _parsed_result2extra(parsed_result, /):
    char_pt2code_block_name = parsed_result
    d = defaultdict(StackStyleSimpleIntSet)
    for rng, name in char_pt2code_block_name.iter_rng_value_pairs_(reverse=False):
        #bug:d[name].push(rng)
        d[name].push_rng(rng)
    code_block_name2char_pt_rngs = fmap4dict_value(StackStyleSimpleIntSet.to_NonTouchRanges, d)

    #code_block_name2char_pt_rngs = MapView(code_block_name2char_pt_rngs)
    extra_derived_result = code_block_name2char_pt_rngs
    return extra_derived_result



def _parsed_result2compact(parsed_result, /):
    #_parsed_result5compact

    char_pt2code_block_name = parsed_result

    char_pt_rng2code_block_name = {(*map(HexReprInt, rng),):name for rng, name in char_pt2code_block_name.iter_rng_value_pairs_(reverse=False)}
    compact_result = char_pt_rng2code_block_name

    #if not _parsed_result5compact(compact_result) == parsed_result: raise logic-err
    #   verify via IHelper4parse__xxx_txt
    return compact_result



def _parsed_result5compact(compact_result, /):
    #_parsed_result2compact
    char_pt_rng2code_block_name = compact_result
        #take care! using HexReprInt
        #should covert to int

    rng_name_pairs___HexReprInt = sorted(char_pt_rng2code_block_name.items())
    rng_name_pairs = [((*map(int, rng),), name) for rng, name in rng_name_pairs___HexReprInt]


    char_pt2code_block_name = TouchRangeBasedIntMapping.from_rng_value_pairs(rng_name_pairs)

    parsed_result = char_pt2code_block_name

    return parsed_result














from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__Blocks_txt import parse__Blocks_txt, helper4parse__UCD_Blocks_txt
