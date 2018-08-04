
from .chars_of import info_of_rw_chars, chars_of, rw_chars, rw_chars_to_html, utf8
import io

iter_chars_of_utf8 = chars_of(utf8)
cs = utf8_chars = rw_chars('utf8_chars.utf8.txt', iter_chars_of_utf8, utf8)
if 0:
    info_utf8 = info_of_rw_chars('chars_of_utf8', iter_chars_of_utf8)
    print(info_utf8)
if 0:
    rw_chars_to_html('utf8_chars.html', utf8_chars)


def index_if(pred, array, begin=0, end=None):
    L = len(array)
    if end is None:
        end = len(array)
    if end < 0:
        end += L
    if begin < 0:
        begin += L
    if end < 0 or begin < 0:
        raise ValueError

    for i in range(begin, end):
        ch = array[i]
        if pred(ch):
            return i
    return None

def iter_split_while_mod(chars, mod=16, pad='-'):
    yield from split_while_mod(chars, mod=mod, pad=pad)
def split_while_mod(chars, mod=16, pad='-'):
    # patched with '-'
    assert len(pad) <= 1
    assert mod >= 1

    out = io.StringIO()
    pred_i = -1
    pred_r = pred_i % mod
    assert pred_r == mod - 1
    for ch in chars:
        i = ord(ch)
        try:
            assert pred_i < i # chars asc
        except:
            print(pred_i, i, ch)
            raise
        r = i % mod
        row_begin = i - r
        if row_begin <= pred_i:
            # in same row
            pads = pad * (i - pred_i - 1)
        else:
            # in different row
            pads = ( pad * (mod - 1 - pred_r)
                   + '\n'
                   + pad * r)
        out.write(pads)
        out.write(ch)
        pred_i = i
        pred_r = r
    pads = pad * (mod - 1 - pred_r) + '\n'
    out.write(pads)
    out.write('\n')
    s = out.getvalue()
    assert s[0] == '\n'
    return s[1:]


#rint(split_while_mod('3a'))

iter_shaped_chars_of_utf8 = iter_split_while_mod(utf8_chars)
shaped_chars_of_utf8 = rw_chars('shaped_chars_of_utf8.utf8.txt'
                                , iter_shaped_chars_of_utf8, utf8)



'''
def split_while_mod(chars, mod=16):
    raise
    lss = [[]]
    ls = lss[-1]
    begin = 0

    for ch in chars:
        base = ord(ch)
        if base % mod == 0:
            lss.append([])
            ls = lss[-1]
        end = base + 16
'''
