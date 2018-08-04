
from vary_charss import vary_chars, all_chars_with_variant
from common_CJK_uniqueST_han_chars_exclude_similars import \
    common_CJK_uniqueST_han_chars_exclude_similars as org_str, exclude_sub
from seed.io.RCXW import make_rcxw__text

ofname = 'common_CJK_noSimilar_han_chars_exclude_vary_chars.gb'
oencoding = 'gb2312'

def _make():
    common_CJK_noSimilar_han_chars_exclude_vary_chars =\
        exclude_sub(org_str, vary_chars)

    common_CJK_noSimilar_han_chars_exclude_all_chars_with_variant =\
        exclude_sub(org_str, all_chars_with_variant)

    assert len(common_CJK_noSimilar_han_chars_exclude_vary_chars) == 1520
    assert len(common_CJK_noSimilar_han_chars_exclude_all_chars_with_variant) == 1518

    return common_CJK_noSimilar_han_chars_exclude_all_chars_with_variant


common_CJK_noSimilar_han_chars_exclude_all_chars_with_variant =\
    make_rcxw__text(_make, ofname, encoding=oencoding)()





