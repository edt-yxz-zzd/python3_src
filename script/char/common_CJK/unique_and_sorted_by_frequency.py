
from exclude_chars import exclude_chars__str, intersection
from seed.io.RCXW import make_rcxw__text


def unique_and_sorted_by_frequency(chars, freq_sorted_chars):
    # return (sorted_chars, infreq_chars)
    # set(sorted_chars) + set(infreq_chars) == set(chars)
    # set(sorted_chars) == set(chars) & set(freq_sorted_chars)
    # set(infreq_chars) == set(chars) - set(freq_sorted_chars)
    infreq_chars = exclude_chars__str(chars, freq_sorted_chars)
    freq_chars = intersection(chars, freq_sorted_chars)
    d = {ch:i for i,ch in enumerate(freq_sorted_chars)}
    i_ch_pairs = sorted((d[ch], ch) for ch in freq_chars)
    sorted_chars = ''.join(ch for i,ch in i_ch_pairs)
    return sorted_chars, infreq_chars

assert unique_and_sorted_by_frequency('122345', '354') == ('354', '12')







def _make():
    from common_CJK_nonBanned_han_chars_exclude_numeric import \
        common_CJK_nonBanned_han_chars_exclude_numeric as src
    ofname = 'freq_sorted_nonBanned_nonNum_han_chars.gb'
    oencoding = 'gb2312'
    sorted_chars = __make(src, ofname, oencoding)
    return sorted_chars
def __make(src_chars, ofname, oencoding):
    calc = lambda: _f(src_chars)[0]
    return make_rcxw__text(calc, ofname, encoding=oencoding)()
def _f(src):
    from han_chars_sorted_by_frequency import han_chars_sorted_by_frequency
    sorted_chars, infreq_chars = unique_and_sorted_by_frequency(
                    src, han_chars_sorted_by_frequency)
    assert infreq_chars == ''
    assert len(sorted_chars) == len(src)
    #print(repr(sorted_chars))
    #print(repr(infreq_chars))
    return sorted_chars, infreq_chars


#sorted_chars, infreq_chars = _f()
sorted_chars = _make()
N = 2**8
init, tail = sorted_chars[:-N], sorted_chars[-N:]
assert init + tail == sorted_chars
assert len(tail) == N
print(len(init), init)
print(len(tail), tail)






