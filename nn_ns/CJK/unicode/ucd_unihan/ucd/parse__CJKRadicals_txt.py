#__all__:goto
r'''
parse unicode::UCD::CJKRadicals.txt

nn_ns.CJK.unicode.ucd_unihan.ucd.parse__CJKRadicals_txt
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__CJKRadicals_txt.py

from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__CJKRadicals_txt import parse__CJKRadicals_txt, parsed_result2compact, parsed_result5compact, compact_result2dicts

======================
view /sdcard/0my_files/unzip/e_book/unicode_13__UCD/CJKRadicals.txt
# There is one line per CJK radical number. Each line contains three
# fields, separated by a semicolon (';'). The first field is the
# CJK radical number. The second field is the CJK radical character.
# The third field is the CJK unified ideograph.
1; 2F00; 4E00
214; 2FD5; 9FA0
======================



.parsed_result
    :: [((pint, str), char, hz)]
    :: [((cjk_radical_number, smay4ST), cjk_radical_character, cjk_unified_ideograph)]
    = readonly__parsed_result
    = idxZ_radical_unified_triples
.compact_result
    :: str
    <- (";".join0s(",".join1s([f"{radical}{unified}"])))
    = radical_char_unified_ideograph_pairss__str

.radical_char2unified_ideograph
    :: {radical:unified}

.simplified_radical2traditional_radical
    :: {simplified_radical:traditional_radical}

#'''


__all__ = '''
    parse__CJKRadicals_txt
    parsed_result2compact
    parsed_result5compact
    compact_result2dicts
    '''.split()
    #compact_result5dict

___begin_mark_of_excluded_global_names__0___ = ...

from seed.io.fielded_line_utils import example4lines_parser4UCD_CJKRadicals_txt, example4txt_parser4UCD_CJKRadicals_txt
from seed.tiny import at, check_type_is
import re

from seed.io.fielded_line_utils import line_splitT
from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__tuple, fmapT__list

___end_mark_of_excluded_global_names__0___ = ...


def check_char(ch, /):
    check_type_is(str, ch)
    if not len(ch) == 1:raise TypeError

_regex4_01s = re.compile(r'(?:(?:0+1?)*)')
def parse__CJKRadicals_txt(lines, /):
    '-> idxZ_radical_unified_triples::((cjk_radical_number, smay4ST), cjk_radical_character, cjk_unified_ideograph)'

    fieldss = example4lines_parser4UCD_CJKRadicals_txt(lines)
    fieldss = (*fieldss,)

    idxZ_radical_unified_triples = fieldss
        # :: ((cjk_radical_number, smay4ST), cjk_radical_character, cjk_unified_ideograph)
        # smay4ST = "" | "'"

    check_idxZ_radical_unified_triples(idxZ_radical_unified_triples)

    parsed_result = idxZ_radical_unified_triples
    readonly__parsed_result = parsed_result
    return readonly__parsed_result

def check_idxZ_radical_unified_triples(idxZ_radical_unified_triples, /):
    hash(idxZ_radical_unified_triples)

    idc = [idx for (idx, _), _, _ in idxZ_radical_unified_triples]
    if not sorted(idc) == idc: raise logic-err
    if not set(idc) == set(range(1, 1+max(idc, default=0))): raise logic-err

    def f(smay4ST, /):
        if smay4ST == "":
            return '0'
        elif smay4ST == "'":
            return '1'
        else:
            return 'x'

    _01x__str = ''.join(f(smay4ST) for (_, smay4ST), _, _ in idxZ_radical_unified_triples)
    if not _regex4_01s.fullmatch(_01x__str): raise logic-err
    _chars = [ch for _, a, b in idxZ_radical_unified_triples for ch in (a, b)]
    [*map(check_char, _chars)]
    if not len(set(_chars)) == len(_chars): raise logic-err
    return



def parsed_result2compact(parsed_result, /):
    #parsed_result5compact
    '[((idx, smay4ST), radical, unified)] -> (compact_result/str/";".join0s(",".join1s([f"{radical}{unified}"])))'

    idxZ_radical_unified_triples = parsed_result
    check_idxZ_radical_unified_triples(idxZ_radical_unified_triples)


    pairss = []
        # [[f"{radical}{unified}"]]

    prev_cjk_radical_number = -1
    for ((cjk_radical_number, smay4ST), cjk_radical_character, cjk_unified_ideograph) in idxZ_radical_unified_triples:
        if cjk_radical_number != prev_cjk_radical_number:
            pairs = []
            pairss.append(pairs)
            prev_cjk_radical_number = cjk_radical_number
        pair = cjk_radical_character + cjk_unified_ideograph
        pairs.append(pair)

    radical_char_unified_ideograph_pairss__str = ';'.join(','.join(pairs) for pairs in pairss)
    compact_result = radical_char_unified_ideograph_pairss__str

    if not parsed_result5compact(compact_result) == parsed_result: raise logic-err
    return compact_result



_pattern4non_sep = '(?:[^,;])'
_pattern4pair = f'(?:{_pattern4non_sep}{{2}})'
_pattern4pair1s = f'(?:{_pattern4pair}(?:,{_pattern4pair})*)'
_pattern4pair1s1s = f'(?:{_pattern4pair1s}(?:;{_pattern4pair1s})*)'
_pattern4pair1s0s = f'(?:{_pattern4pair1s1s}?)'
_regex4pair1s0s = re.compile(_pattern4pair1s0s)

def check_radical_char_unified_ideograph_pairss__str(radical_char_unified_ideograph_pairss__str, /):
    check_type_is(str, radical_char_unified_ideograph_pairss__str)
    if not _regex4pair1s0s.fullmatch(radical_char_unified_ideograph_pairss__str): raise TypeError
def parsed_result5compact(compact_result, /):
    #parsed_result2compact
    '(compact_result/str/";".join0s(",".join1s([f"{radical}{unified}"]))) -> [((idx, smay4ST), radical, unified)]'
    radical_char_unified_ideograph_pairss__str = compact_result
    check_radical_char_unified_ideograph_pairss__str(radical_char_unified_ideograph_pairss__str)



    idxZ_radical_unified_triples = tuple(
        ((idx, "'"*time), radical_char, unified_ideograph)
        for idx, pairs__str in enumerate(radical_char_unified_ideograph_pairss__str.split(';'), 1)
        for time, (radical_char, unified_ideograph) in enumerate(pairs__str.split(','))
        )

    check_idxZ_radical_unified_triples(idxZ_radical_unified_triples)

    parsed_result = idxZ_radical_unified_triples
    return parsed_result




def compact_result2dicts(compact_result, /):
    #compact_result5dict
    '(compact_result/str/";".join0s(",".join1s([f"{radical}{unified}"]))) -> ({radical:unified}, {simplified_radical:traditional_radical})'
    radical_char_unified_ideograph_pairss__str = compact_result
    check_radical_char_unified_ideograph_pairss__str(radical_char_unified_ideograph_pairss__str)

    radical_char2unified_ideograph = {
        radical_char:unified_ideograph
        for pairs__str in radical_char_unified_ideograph_pairss__str.split(';')
        for (radical_char, unified_ideograph) in pairs__str.split(',')
        }

    simplified_radical2traditional_radical = {
        simplified_radical: traditional_radical
        for pairs in map(line_splitT(','), radical_char_unified_ideograph_pairss__str.split(';'))
        if not len(pairs) == 1
            #assert len(pairs) == 2
        for (traditional_radical, _), (simplified_radical, _) in [pairs]
        }
    return (radical_char2unified_ideograph, simplified_radical2traditional_radical)

r'''
def compact_result5dict(radical_char2unified_ideograph, /):
    #compact_result2dict
    '{radical:unified} -> (compact_result/str/";".join0s(",".join1s([f"{radical}{unified}"])))'
    radical_char_unified_ideograph_pairs = sorted(radical_char2unified_ideograph.items())
    ls = []
    [*map(ls.extend, radical_char_unified_ideograph_pairs)]
    radical_char_unified_ideograph_pairss__str = ''.join(ls)
    compact_result = radical_char_unified_ideograph_pairss__str

    return compact_result

#'''







from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__CJKRadicals_txt import parse__CJKRadicals_txt, parsed_result2compact, parsed_result5compact, compact_result2dicts

