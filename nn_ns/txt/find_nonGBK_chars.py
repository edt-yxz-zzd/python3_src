

__all__ = '''
    iter_nonGBK_chars
    iter_nonGBK_chars_ex
    find_nonGBK_chars
    find_nonGBK_chars_ex
    '''.split()

from collections import defaultdict
import codecs
gbk_codec = codecs.lookup('gbk')
gbk_encoder = codecs.getencoder('gbk')

def is_nongbk(ch):
    return not is_gbk(ch)
def is_gbk(ch):
    try:
        gbk_encoder(ch)
    except UnicodeError:
        return False
    return True
def iter_nonGBK_chars(chars):
    return filter(is_nongbk, chars)
def find_nonGBK_chars(chars):
    return set(iter_nonGBK_chars(chars))

def iter_nonGBK_chars_ex(chars, offset=0):
    # -> Iter (idx, char)
    for idx, ch in enumerate(chars, offset):
        if not is_gbk(ch):
            yield idx, ch
    return
def find_nonGBK_chars_ex(chars, offset=0):
    # -> Map ch [idx]
    char2idc = defaultdict(list)
    for idx, ch in iter_nonGBK_chars_ex(chars, offset):
        char2idc[ch].append(idx)

    return dict(char2idc)

