#__all__:goto
r'''
parse unicode::Unihan::kCompatibilityVariant8Unihan_IRGSources.txt

nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kCompatibilityVariant8Unihan_IRGSources_txt
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kCompatibilityVariant8Unihan_IRGSources_txt


e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kCompatibilityVariant8Unihan_IRGSources_txt.py
copy from:
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kIICore8Unihan_IRGSources_txt.py
.+1,$s/kIICore/kCompatibilityVariant/g



from nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kCompatibilityVariant8Unihan_IRGSources_txt import parse__kCompatibilityVariant8Unihan_IRGSources_txt, helper4parse__Unihan_kCompatibilityVariant8Unihan_IRGSources_txt

======================
view /sdcard/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_IRGSources.txt
    U+F900	kCompatibilityVariant	U+8C48
      #豈豈
    U+F901	kCompatibilityVariant	U+66F4
      #更更
    U+F91B	kCompatibilityVariant	U+4E82
      #亂亂
======================

======================




======================
.dataobj
    :: (parsed_result, extra_derived_result)
    mutable
.state
    = compact_result
    mutable

======================
.parsed_result
    :: cjk_compatibility_variant2unified
    mutable
.extra_derived_result
    :: None
    immutable
.compact_result
    :: variant_unified_packedpair_rawlines
    immutable

======================
.cjk_compatibility_variant2unified
    :: {variant_hz:unified_hz}
    mutable
.variant_unified_packedpair_rawlines
    :: '\n'.join(f'{variant_hz}{unified_hz}'...)
    immutable
======================




#'''


__all__ = '''
    parse__kCompatibilityVariant8Unihan_IRGSources_txt
    helper4parse__Unihan_kCompatibilityVariant8Unihan_IRGSources_txt

    '''.split()



___begin_mark_of_excluded_global_names__0___ = ...

from seed.io.fielded_line_utils import fielded_lines_parserT__tuple
from seed.io.fielded_line_utils import line_splitT, hex2int, line_remove_prefixT, hex2char

from seed.func_tools.fmapT.fmapT__tiny import fmapT__tpls, fmapT__iter#, fmapT__pairs#, fmapT__list, fmapT__tuple
from seed.func_tools.fmapT.fmapT__tiny import dot
from seed.func_tools.fmapT.predT__tiny import (dot, eqT)
from seed.func_tools.fmapT.filterT__tiny import (filterT)

from seed.tiny import dict_add__is#, fmap4dict_value, filter4dict_value, dict_add__eq

from seed.tiny import MapView, echo, at#, check_type_is, print_err
from seed.helper.IHelper4parse__xxx_txt import IHelper4parse__xxx_txt
from seed.abc.abc__ver0 import override


___end_mark_of_excluded_global_names__0___ = ...








_basic_lines_parser4Unihan_IRGSources_txt = fielded_lines_parserT__tuple('\t', '#', [dot[hex2int, line_remove_prefixT('U+')], echo, echo], keep_space_lines=False, keep_bifix_spaces4field=False)

char5Upt = dot[hex2char, line_remove_prefixT('U+')]
_lines_parser4kCompatibilityVariant8Unihan_IRGSources_txt = dot[fmapT__tpls(chr, echo, char5Upt), filterT(dot[eqT('kCompatibilityVariant'), at[1]]), _basic_lines_parser4Unihan_IRGSources_txt]






def parse__kCompatibilityVariant8Unihan_IRGSources_txt(lines, /):
    '-> parsed_result::cjk_compatibility_variant2unified'

    fieldss = _lines_parser4kCompatibilityVariant8Unihan_IRGSources_txt(lines)
    variant_kCompatibilityVariant_unified_triples = fieldss


    def mk_err_msg(s, /):
        return (f'{s!s}: {hex(ord(variant_hz))}-{variant_hz}-{hex(ord(unified_hz))}-{unified_hz}')

    cjk_compatibility_variant2unified = {}
    for variant_hz, kCompatibilityVariant, unified_hz in variant_kCompatibilityVariant_unified_triples:
        assert kCompatibilityVariant == 'kCompatibilityVariant'

        try:
            dict_add__is(cjk_compatibility_variant2unified, variant_hz, unified_hz)
        except:
            raise  TypeError(mk_err_msg('bad format: duplicated variant_hz'))


    parsed_result = cjk_compatibility_variant2unified
    return parsed_result


#[[[
class Helper4parse__Unihan_kCompatibilityVariant8Unihan_IRGSources_txt(IHelper4parse__xxx_txt):
    @override
    def _parse__fin_(sf, fin, /):
        '-> parsed_result'
        lines = iter(fin)
        return parse__kCompatibilityVariant8Unihan_IRGSources_txt(lines)

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
            return MapView( parsed_result)
        def _parsed_result5readonly_(sf, readonly__parsed_result, /):
            'readonly__parsed_result -> parsed_result'
            return dict(readonly__parsed_result)
helper4parse__Unihan_kCompatibilityVariant8Unihan_IRGSources_txt = Helper4parse__Unihan_kCompatibilityVariant8Unihan_IRGSources_txt()

#]]]



def _parsed_result2extra(parsed_result, /):
    extra_derived_result = None
    return extra_derived_result









def _parsed_result2compact(parsed_result, /):
    #_parsed_result5compact
    cjk_compatibility_variant2unified = parsed_result

    variant_unified_packedpair_rawlines = '\n'.join(variant_hz+unified_hz for variant_hz, unified_hz in sorted(cjk_compatibility_variant2unified.items()))


    compact_result = variant_unified_packedpair_rawlines
    return compact_result

    #if not _parsed_result5compact(compact_result) == parsed_result: raise logic-err
    #   verify via IHelper4parse__xxx_txt
    return compact_result



def _parsed_result5compact(compact_result, /):
    #_parsed_result2compact
    variant_unified_packedpair_rawlines = compact_result
    txt = variant_unified_packedpair_rawlines
    pairs = txt.split()
    cjk_compatibility_variant2unified = dict(pairs)
    parsed_result = cjk_compatibility_variant2unified
    return parsed_result













from nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kCompatibilityVariant8Unihan_IRGSources_txt import parse__kCompatibilityVariant8Unihan_IRGSources_txt, helper4parse__Unihan_kCompatibilityVariant8Unihan_IRGSources_txt

