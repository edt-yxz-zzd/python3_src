r'''
py -m nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__kUnihanCore20208Unihan_DictionaryLikeData_txt__of_ver13_0

from nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__kUnihanCore20208Unihan_DictionaryLikeData_txt__of_ver13_0 import readonly__sourceIRG_char2char_pt_rngs4ver13_0, readonly__common_char_pt_rngs4ver13_0

e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parsed_result__of__kUnihanCore20208Unihan_DictionaryLikeData_txt__of_ver13_0.py
copy from:
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parsed_result__of__kIICore8Unihan_IRGSources_txt__of_ver13_0.py

.+1,$s/kIICore\C/kUnihanCore2020/g
.+1,$s/Unihan_IRGSources\C/Unihan_DictionaryLikeData/g


view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kUnihanCore20208Unihan_DictionaryLikeData_txt.py.out.ver13_0.txt

#'''

__all__ = '''
    readonly__sourceIRG_char2char_pt_rngs4ver13_0
    readonly__common_char_pt_rngs4ver13_0
    '''.split()


from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kUnihanCore20208Unihan_DictionaryLikeData_txt import findout_available_version_strs, load_readonly_sourceIRG_char2char_pt_rngs_from_compact_result_file__ver, load_readonly_common_char_pt_rngs_from_compact_result_file__ver
readonly__sourceIRG_char2char_pt_rngs4ver13_0 = load_readonly_sourceIRG_char2char_pt_rngs_from_compact_result_file__ver('ver13_0')
readonly__common_char_pt_rngs4ver13_0 = load_readonly_common_char_pt_rngs_from_compact_result_file__ver('ver13_0')


_sz = readonly__common_char_pt_rngs4ver13_0.len_ints()
assert _sz == 2573







from nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__kUnihanCore20208Unihan_DictionaryLikeData_txt__of_ver13_0 import readonly__sourceIRG_char2char_pt_rngs4ver13_0, readonly__common_char_pt_rngs4ver13_0
