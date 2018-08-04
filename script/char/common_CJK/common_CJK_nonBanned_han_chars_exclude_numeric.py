

def _make():
    from common_CJK_noVariant_han_chars_exclude_banned import \
        common_CJK_noVariant_han_chars_exclude_banned as src
    from all_numeric_han_chars import all_numeric_han_chars as num_chars
    from exclude_chars import exclude_chars__str
    return exclude_chars__str(src, num_chars)


common_CJK_nonBanned_han_chars_exclude_numeric = _make()
assert 342 == len(common_CJK_nonBanned_han_chars_exclude_numeric)



