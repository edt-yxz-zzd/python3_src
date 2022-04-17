#__all__:goto
r'''
to parse UCD::PropList.txt
    真值属性
    出现 即 turnon

.parsed_result
    :: {property_name:[(begin,end)]}
.readonly__parsed_result
    :: MapView {property_name:NonTouchRanges}'

py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.ucd.parse__PropList_txt

from nn_ns.CJK.unicode.ucd_unihan.ucd.parse__PropList_txt import parse__PropList_txt, parsed_result2readonly, parsed_result5readonly, parsed_result2literal_text, parsed_result5literal_text

[[genenerate data:
py -m nn_ns.CJK.unicode.ucd_unihan.ucd.parse__PropList_txt   -i /storage/emulated/0/0my_files/unzip/e_book/unicode_13__UCD/PropList.txt -o $my_tmp/out4py/cjk.parse__PropList_txt.ver13_0.decimal.txt
py -m nn_ns.CJK.unicode.ucd_unihan.ucd.parse__PropList_txt   -i /storage/emulated/0/0my_files/unzip/e_book/unicode_13__UCD/PropList.txt -o $my_tmp/out4py/cjk.parse__PropList_txt.ver13_0.hex.txt --hex
view /storage/emulated/0/0my_files/tmp/out4py/cjk.parse__PropList_txt.ver13_0.txt
view /storage/emulated/0/0my_files/tmp/out4py/cjk.parse__PropList_txt.ver13_0.hex.txt
!du -h /storage/emulated/0/0my_files/unzip/e_book/unicode_13__UCD/PropList.txt
    124K
!du -h /storage/emulated/0/0my_files/tmp/out4py/cjk.parse__PropList_txt.ver13_0.decimal.txt
    24k
        #decimal
!du -h /storage/emulated/0/0my_files/tmp/out4py/cjk.parse__PropList_txt.ver13_0.hex.txt
    28k
        #hex
!cp /storage/emulated/0/0my_files/tmp/out4py/cjk.parse__PropList_txt.ver13_0.hex.txt      ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__PropList_txt.py.out.ver13_0.hex.txt
]]




[[list property_name
py -m nn_ns.CJK.unicode.ucd_unihan.ucd.parse__PropList_txt   -i /storage/emulated/0/0my_files/unzip/e_book/unicode_13__UCD/PropList.txt  --show_property_names_only

ASCII_Hex_Digit
Bidi_Control
Dash
Deprecated
Diacritic
Extender
Hex_Digit
Hyphen
IDS_Binary_Operator
IDS_Trinary_Operator
Ideographic
Join_Control
Logical_Order_Exception
Noncharacter_Code_Point
Other_Alphabetic
Other_Default_Ignorable_Code_Point
Other_Grapheme_Extend
Other_ID_Continue
Other_ID_Start
Other_Lowercase
Other_Math
Other_Uppercase
Pattern_Syntax
Pattern_White_Space
Prepended_Concatenation_Mark
Quotation_Mark
Radical
Regional_Indicator
Sentence_Terminal
Soft_Dotted
Terminal_Punctuation
Unified_Ideograph
Variation_Selector
White_Space

]]
感兴趣的:
    IDS_Binary_Operator
    IDS_Trinary_Operator
    Ideographic
    Radical
    Sentence_Terminal
    Terminal_Punctuation
    Unified_Ideograph
    White_Space

TODO:
    加载数据
        mimic parsed_result__of__Unihan_Variants_txt__of_ver13_0.py
    parsed_result__of__PropList_txt__of_ver13_0.py
    e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parsed_result__of__PropList_txt__of_ver13_0.py

e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__PropList_txt.py
0009..000D    ; White_Space # Cc   [5] <control-0009>..<control-000D>

#'''



r'''
py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.ucd.parse__PropList_txt
    pt2ord
    parse__PropList_txt
    parsed_result2readonly
    parsed_result5readonly
    parsed_result2literal_text
    parsed_result5literal_text
    main
#'''

__all__ = '''
    parse__PropList_txt
    parsed_result2readonly
    parsed_result5readonly
    parsed_result2literal_text
    parsed_result5literal_text
    '''.split()

___begin_mark_of_excluded_global_names__0___ = ...
from seed.io.FieldedLineHandler import FieldedLineHandler, IFieldedLineHandler
from seed.tiny import mk_fprint
from seed.tiny import fmap4dict_value#, filter4dict_value, dict_add__is, dict_add__eq
from seed.tiny import MapView, echo
#from seed.data_funcs.rngs import NonTouchRanges
from seed.data_funcs.rngs import make_Ranges#, sorted_ints_to_iter_nontouch_ranges, detect_iter_ranges, StackStyleSimpleIntSet
from seed.func_tools.fmapT.fmapT__tiny import fmapT__dict, fmap_rngs2hex_repr#, fmapT__list, fmapT__iter, fmapT__tuple, fmapT__tpls, fmapT__pairs
from ast import literal_eval
from seed.helper.stable_repr import stable_repr
___end_mark_of_excluded_global_names__0___ = ...


def pt2ord(pt, /):
    if 0:
        if not pt.startswith('U+'):raise ValueError
        hex = pt[2:]
    else:
        hex = pt
    return int(hex, 16)

_fielded_line_handler__PropList_txt= FieldedLineHandler(remove_empty_lines=True, line_strip=True, field_strip=True, line_comment_prefix='#', line_tail_comment_prefix='#', field_sep=';')
def parse__PropList_txt(lines, /, *, result_readonly):
    '-> attr2rngs/{property_name:[(begin,end)]}'
    attr2rngs = {}

    fieldss = _fielded_line_handler__PropList_txt.lines2fieldss(lines)
    for pt_or_blk, property_name in fieldss:
        rngs = attr2rngs.setdefault(property_name, [])
        pt_ls = pt_or_blk.split('..')
        assert pt_ls
        assert len(pt_ls) in [1, 2]
        if len(pt_ls) == 1:
            pt_ls *= 2
        first, last = map(pt2ord, pt_ls)
        rngs.append((first, last+1))
    if 1:
        #!!!!!check!!!!!
        #!!!!!check!!!!!
        #!!!!!check!!!!!
        #check sorted and not touch/overlap
        readonly__attr2rngs = parsed_result2readonly(attr2rngs)
        #!!!!!check!!!!!
        #!!!!!check!!!!!
        #!!!!!check!!!!!
        #readonly__attr2rngs = MapView(fmap4dict_value(make_Ranges, attr2rngs))

    parsed_result = attr2rngs
    readonly__parsed_result = readonly__attr2rngs
    if result_readonly:
        return readonly__parsed_result
    else:
        return parsed_result
def parsed_result2readonly(parsed_result, /):
    #parsed_result5readonly
    '{property_name:[(begin,end)]} -> MapView {property_name:NonTouchRanges}'
    attr2rngs = parsed_result
    readonly__attr2rngs = MapView(fmap4dict_value(make_Ranges, attr2rngs))
    readonly__parsed_result = readonly__attr2rngs

    if not parsed_result == parsed_result5readonly(readonly__parsed_result):raise logic-err
    return readonly__parsed_result

def parsed_result5readonly(readonly__parsed_result, /):
    'MapView {property_name:NonTouchRanges} -> {property_name:[(begin,end)]}'
    def f(ranges, /):
        return [*ranges.ranges]

    readonly__attr2rngs = readonly__parsed_result
    attr2rngs = fmap4dict_value(f, readonly__attr2rngs)
    parsed_result = attr2rngs
    return parsed_result
def parsed_result2literal_text(parsed_result, /, *, decimal_vs_hex):
    if decimal_vs_hex:
        f = fmapT__dict(fmap_rngs2hex_repr)
    else:
        f = echo
    repr_result = stable_repr(f(parsed_result), depth=0, maybe_max_depth=1)
    if not parsed_result == parsed_result5literal_text(repr_result): raise logic-err
    return repr_result
def parsed_result5literal_text(repr_result, /):
    parsed_result = literal_eval(repr_result)
    return parsed_result


def main(args=None, /):
    from pprint import pprint
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout
    if 0:
        help(pprint)
        #pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True)
        return

    parser = argparse.ArgumentParser(
        description='parse unicode::UCD::PropList.txt'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )

    parser.add_argument('--show_property_names_only', action='store_true'
                        , default = False
                        , help='output property_names without uint-rngs')
    parser.add_argument('--hex', action='store_true'
                        , default = False
                        , help='output uint-rngs in hex/radix<16>')
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path for unicode::UCD::PropList.txt')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'


    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        #lines = [*fin]
        lines = iter(fin)
        parsed_result = parsed_result = parse__PropList_txt(lines, result_readonly=False)


    repr_result = parsed_result2literal_text(parsed_result, decimal_vs_hex=args.hex)


    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        print = mk_fprint(fout)
        if args.show_property_names_only:
            attr2rngs = parsed_result
            for property_name in sorted(attr2rngs):
                print(property_name)

        else:
            #pprint(parsed_result, stream=fout, indent='')
            stable_repr
            print(repr_result)
if __name__ == "__main__":
    main()



