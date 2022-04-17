r'''
py -m nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__Unihan_Variants_txt__of_ver13_0

from nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__Unihan_Variants_txt__of_ver13_0 import readonly_parsed_result4ver13_0, readonly_simplified_result4ver13_0

#'''

__all__ = '''
    readonly_parsed_result4ver13_0
    readonly_simplified_result4ver13_0
    '''.split()

from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__Unihan_Variants_txt import load_readonly_parsed_result_from_compact_result_file__ver, load_readonly_simplified_result_from_compact_result_file__ver

readonly_parsed_result4ver13_0 = load_readonly_parsed_result_from_compact_result_file__ver('ver13_0')
readonly_simplified_result4ver13_0 = load_readonly_simplified_result_from_compact_result_file__ver('ver13_0')


