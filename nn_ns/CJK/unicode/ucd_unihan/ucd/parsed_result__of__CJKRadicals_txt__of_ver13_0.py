r'''
py -m nn_ns.CJK.unicode.ucd_unihan.ucd.parsed_result__of__CJKRadicals_txt__of_ver13_0

from nn_ns.CJK.unicode.ucd_unihan.ucd.parsed_result__of__CJKRadicals_txt__of_ver13_0 import readonly_parsed_result4ver13_0, readonly_compact_result4ver13_0, readonly_radical_char2unified_ideograph4ver13_0, readonly_simplified_radical2traditional_radical4ver13_0


#'''

__all__ = '''
    readonly_parsed_result4ver13_0
    readonly_compact_result4ver13_0
    readonly_radical_char2unified_ideograph4ver13_0
    readonly_simplified_radical2traditional_radical4ver13_0
    '''.split()

from nn_ns.CJK.unicode.ucd_unihan.ucd.dump_load___parsed_result__of__CJKRadicals_txt import findout_available_version_strs, load_readonly_parsed_result_from_compact_result_file__ver, load_readonly_compact_result_from_compact_result_file__ver, load_readonly_radical_char2unified_ideograph_from_compact_result_file__ver, load_readonly_simplified_radical2traditional_radical_from_compact_result_file__ver

readonly_parsed_result4ver13_0 = load_readonly_parsed_result_from_compact_result_file__ver('ver13_0')
readonly_compact_result4ver13_0 = load_readonly_compact_result_from_compact_result_file__ver('ver13_0')
readonly_radical_char2unified_ideograph4ver13_0 = load_readonly_radical_char2unified_ideograph_from_compact_result_file__ver('ver13_0')
readonly_simplified_radical2traditional_radical4ver13_0 = load_readonly_simplified_radical2traditional_radical_from_compact_result_file__ver('ver13_0')

if __name__ == "__main__":
    from seed.types.view.RecurView import RecurView4Mapping, RecurView4Seq
    from seed.tiny import at, check_type_is
    check_type_is(RecurView4Seq, readonly_parsed_result4ver13_0)
    check_type_is(str, readonly_compact_result4ver13_0)
    check_type_is(RecurView4Mapping, readonly_radical_char2unified_ideograph4ver13_0)
    check_type_is(RecurView4Mapping, readonly_simplified_radical2traditional_radical4ver13_0)

    for k in readonly_simplified_radical2traditional_radical4ver13_0:
        break
    try:
        del readonly_simplified_radical2traditional_radical4ver13_0[k]
    except TypeError:
        #TypeError: 'RecurView4Mapping' object does not support item deletion
        pass
    else:
        raise logic-err

    print(readonly_parsed_result4ver13_0)
    print(readonly_compact_result4ver13_0)
    print(readonly_radical_char2unified_ideograph4ver13_0)
    print(readonly_simplified_radical2traditional_radical4ver13_0)

from nn_ns.CJK.unicode.ucd_unihan.ucd.parsed_result__of__CJKRadicals_txt__of_ver13_0 import readonly_parsed_result4ver13_0, readonly_compact_result4ver13_0, readonly_radical_char2unified_ideograph4ver13_0, readonly_simplified_radical2traditional_radical4ver13_0

