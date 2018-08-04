
from common_CJK_han_chars_exclude_multiST import common_CJK_han_chars_exclude_multiST
from all_similar_chars import all_similar_chars
from seed.io.read_txt import read_or_calc_xwrite__txt


def exclude_sub(org_str, other_str):
    cs = set(org_str)
    ss = set(other_str)
    r = cs - ss
    r = ''.join(sorted(r))
    return r
def _make():
    return exclude_sub(common_CJK_han_chars_exclude_multiST, all_similar_chars)

ofname = 'common_CJK_uniqueST_han_chars_exclude_similars.u8'
oencoding = 'utf-8'
common_CJK_uniqueST_han_chars_exclude_similars = read_or_calc_xwrite__txt(
    ofname, _make, oencoding)

L = 2259
assert L == len(common_CJK_uniqueST_han_chars_exclude_similars)

if __name__ == '__main__':
    print(len(common_CJK_uniqueST_han_chars_exclude_similars))
    print(common_CJK_uniqueST_han_chars_exclude_similars)





