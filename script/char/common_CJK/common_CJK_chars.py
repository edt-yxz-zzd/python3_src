
r'''
find out characters that occur in GBK, Shift-JIS, Big5...
'''


from seed.text.encodings import all_encodings


#def common_CJK_chars():pass

def able_encode(encoding, txt):
    try:
        txt.encode(encoding)
    except:
        return False
    return True
def iter_encodings_contains(s, encodings=all_encodings):
    return (e for e in encodings if able_encode(e, s))

def encodings_contains(s, encodings=all_encodings):
    return list(iter_encodings_contains(s, encodings=encodings))




# encodings_CJK
if 0:
    ls = encodings_contains('一')
    ls_ = ['big5', 'big5hkscs', 'cp932', 'cp949', 'cp950', 'cp65001', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213', 'euc_kr', 'gb2312', 'gbk', 'gb18030', 'hz', 'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_2004', 'iso2022_jp_3', 'iso2022_jp_ext', 'iso2022_kr', 'johab', 'shift_jis', 'shift_jis_2004', 'shift_jisx0213', 'utf_32', 'utf_32_be', 'utf_32_le', 'utf_16', 'utf_16_be', 'utf_16_le', 'utf_7', 'utf_8', 'utf_8_sig', 'idna', 'mbcs', 'punycode', 'raw_unicode_escape', 'unicode_escape']

    assert set(ls) == set(ls_)
    print(ls)

encodings_CJK = ['big5', 'big5hkscs', 'cp932', 'cp949', 'cp950', 'cp65001', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213', 'euc_kr', 'gb2312', 'gbk', 'hz', 'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_2004', 'iso2022_jp_3', 'iso2022_jp_ext', 'iso2022_kr', 'johab', 'shift_jis', 'shift_jis_2004', 'shift_jisx0213', 'idna', 'mbcs', 'punycode']




# common_CJK_ranges, total_common_CJK_chars
if 0:
    from encoding2ranges import encoding2ranges, gb2312_ranges, common_char_ord_ranges

    common_CJK_ranges = common_char_ord_ranges(encodings_CJK, gb2312_ranges)
    print(common_CJK_ranges)
from common_CJK_ranges import common_CJK_ranges

def count_int_ranges(ranges):
    return sum(end - begin for begin, end in ranges)
assert count_int_ranges([(0,0), (1,2)]) == 1

if 0:
    total_common_CJK_chars = count_int_ranges(common_CJK_ranges)
    print(total_common_CJK_chars)
    assert total_common_CJK_chars == 3065
    from encoding2ranges import encoding2ranges, gb2312_ranges, common_char_ord_ranges
    total_gb2312_chars = count_int_ranges(gb2312_ranges)
    print(total_gb2312_chars)
    assert total_gb2312_chars == 7573
total_common_CJK_chars = 3065
total_gb2312_chars = 7573











# common_CJK_chars_exclude_nonHanzi

def ranges2string(ranges):
    ords = iter_char_ords(ranges)
    return ''.join(map(chr, ords))

if 0:
    from encoding2ranges import iter_char_ords
    common_CJK_chars = ranges2string(common_CJK_ranges)
    #rint(common_CJK_chars)
    begin = common_CJK_chars.index('一')
    end = common_CJK_chars.index('！')
    common_CJK_chars_exclude_nonHanzi = common_CJK_chars[begin:end]
    print(repr(common_CJK_chars_exclude_nonHanzi))
from common_CJK_chars_exclude_nonHanzi import common_CJK_chars_exclude_nonHanzi
total_common_CJK_chars_exclude_nonHanzi = len(common_CJK_chars_exclude_nonHanzi)
#rint(total_common_CJK_chars_exclude_nonHanzi)
assert total_common_CJK_chars_exclude_nonHanzi == 2513






