
from seed.io.RCXW import make_rcxw__text

ofname = 'common_CJK_noVariant_han_chars_exclude_banned.gb'
oencoding = 'gb2312'

def _make():
    from common_CJK_noSimilar_han_chars_exclude_vary_chars import \
        common_CJK_noSimilar_han_chars_exclude_all_chars_with_variant \
        as noVariants
    from chars_in_banned_words import chars_in_banned_words
    from exclude_chars import exclude_chars__str
    common_CJK_noVariant_han_chars_exclude_banned = exclude_chars__str(
        noVariants, chars_in_banned_words)

    if 0:
        print(len(common_CJK_noVariant_han_chars_exclude_banned))
        print(common_CJK_noVariant_han_chars_exclude_banned)
    assert 342 == len(common_CJK_noVariant_han_chars_exclude_banned)
    return common_CJK_noVariant_han_chars_exclude_banned


common_CJK_noVariant_han_chars_exclude_banned =\
    make_rcxw__text(_make, ofname, encoding=oencoding)()

assert 342 == len(common_CJK_noVariant_han_chars_exclude_banned)

