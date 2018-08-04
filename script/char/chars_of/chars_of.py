
import os
from seed.text.encodings import to_std_encoding as std_encoding
from seed.io.read_txt import read_or_calc_xwrite__txt
from sand import gb18030, gbk, utf8, includes_char
from sand import rw_chars_to_html, iter_chars_to_txt_f
from sand import repr_hex_rngs, rngs2lens, rngs2gaps,\
     sorted_non_overlap_rngs2len_gaps
from sand import fixed__package__
fixed__package__(__name__)
from . import output_dir
##print(output_dir)
##raise

#import html
import unicodedata
assert unicodedata.name('一') == 'CJK UNIFIED IDEOGRAPH-4E00'
assert ord('一') == 0x4E00


def chars2ords(chars):
    return map(ord, chars)
def ords2chars(ords):
    return map(chr, ords)
def all_char_ords():
    return range(0x110000)
def all_chars():
    return ords2chars(all_char_ords())
def char_ords_of(encoding):
    if encoding is None:
        return all_char_ords()
    return chars2ords(chars_of(encoding))
    
def chars_of(encoding):
    if encoding is None:
        return all_chars()
    for i in all_char_ords():
        ch = chr(i)
        if includes_char(encoding, ch):
            yield ch







    


def group_char_ords_of(encoding):
    return group_sorted_chars(chars_of(encoding))
def group_sorted_chars(sorted_chars):
    return group_sorted_char_ords(chars2ords(sorted_chars))
def group_sorted_char_ords(sorted_char_ords):
    rngs = []
    it = iter(sorted_char_ords)
    for begin in it:
        break
    else:
        return rngs

    j = begin
    for i in it:
        if i == j+1:
            j = i
        else:
            rngs.append((begin, j+1))
            begin = j = i
    else:
        rngs.append((begin, j+1))

    return rngs

def chars_of_name_startswith(prefix):
    return filter(lambda ch: unicodedata.name(ch, '').startswith(prefix),
                  all_chars())

def chars_of_CJK():
    return chars_of_name_startswith('CJK')
                  
           



    
    
    



def max_len_of_encoded_char(encoding, txt):
    return max(map(lambda ch: len(ch.encode(encoding)), txt))



def rw_chars_of(encoding, *, path=output_dir):
    encoding = std_encoding(encoding)
    fname = 'chars_of_{}.txt'.format(encoding)
    fname = os.path.join(path, fname)
    iter_chars = chars_of(encoding)
    return rw_chars(fname, iter_chars, encoding, path=output_dir)


    
def rw_chars(fname, iter_chars, encoding, *, path=output_dir):
    txt_f = iter_chars_to_txt_f(iter_chars)
    fname = os.path.join(path, fname)
    return read_or_calc_xwrite__txt(fname, txt_f, encoding)


def info_of(encoding):
    txt = rw_chars_of(encoding)
    L = len(txt)
    bL = max_len_of_encoded_char(encoding, txt)
    return txt, L, bL

def info_of_rw_chars(file_basename, iter_chars, encoding=None, *, path=output_dir):
    if encoding is None:
        encoding = utf8
    encoding = std_encoding(encoding)
    txt_fname = '.'.join([file_basename, encoding, 'txt'])
    htm_fname = '.'.join([file_basename, encoding, 'html'])

    fname_str = 'fnames == {}'.format((txt_fname, htm_fname))

    txt_fname, htm_fname = map((lambda x: os.path.join(path, x)),
                               [txt_fname, htm_fname])
    chars = rw_chars(txt_fname, iter_chars, encoding)
    htm = rw_chars_to_html(htm_fname, chars)
    L = len(chars)
    rngs = group_sorted_chars(chars)
    len_gaps = sorted_non_overlap_rngs2len_gaps(rngs)
    rngs_str = 'rngs == {} == {}'.format(rngs, repr_hex_rngs(rngs))
    len_str = 'len(chars) == {} == {}'.format(L, hex(L))
    len_gaps_str = 'len_gaps == {}'.format(len_gaps)
    return (chars, htm), \
           (L, rngs, len_gaps), \
           (fname_str, rngs_str, len_str, len_gaps_str)

    

'''
info_gbk = info_of_rw_chars('chars_of_gbk', chars_of(gbk))

fnames == ('chars_of_gbk.utf-8.txt', 'chars_of_gbk.utf-8.html')
len(chars) == 21919 == 0x559f
len_gaps == [128, -36, 1, -2, 2, -7, 2, -5, 1, -31, 1, -8, 2, -6, 3, -1, 2, -4, 2, -3, 1, -1, 2, -1, 1, -4, 1, -17, 1, -7, 1, -15, 1, -24, 1, -3, 1, -4, 1, -29, 1, -98, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -116, 1, -15, 1, -101, 1, -1, 3, -13, 1, -183, 17, -1, 7, -7, 17, -1, 7, -55, 1, -14, 64, -1, 1, -7102, 1, -2, 4, -1, 2, -2, 2, -7, 2, -9, 1, -1, 2, -1, 1, -5, 1, -199, 1, -1, 1, -3, 1, -12, 1, -10, 1, -62, 12, -4, 10, -22, 4, -2, 4, -110, 1, -6, 1, -1, 1, -3, 1, -4, 1, -2, 4, -2, 1, -1, 1, -1, 5, -2, 1, -5, 4, -5, 1, -10, 1, -3, 1, -5, 1, -13, 2, -2, 4, -6, 2, -37, 1, -3, 1, -11, 1, -25, 1, -82, 1, -333, 10, -10, 40, -100, 76, -4, 36, -13, 15, -3, 3, -10, 2, -16, 2, -8, 2, -8, 2, -3, 1, -2, 2, -18, 4, -31, 2, -2, 1, -54, 1, -1, 1, -2493, 4, -1, 19, -5, 2, -2, 9, -23, 83, -7, 4, -2, 86, -5, 3, -6, 37, -246, 10, -7, 1, -113, 1, -234, 2, -12, 3, -2, 1, -34, 1, -9, 1, -2, 2, -2, 1, -6698, 20902, -22918, 1, -76, 1, -27, 1, -81, 1, -9, 1, -26, 4, -1, 1, -1, 2, -3, 1, -6, 3, -1, 2, -2, 3, -1030, 2, -1, 18, -4, 10, -1, 4, -1, 14, -1, 4, -149, 94, -129, 6]
'''

'''
info_CJK = info_of_rw_chars('chars_of_CJK', chars_of_CJK())

fnames == ('chars_of_CJK.utf-8.txt', 'chars_of_CJK.utf-8.html')
rngs == [(11904, 11930), (11931, 12020), (12736, 12772), (13312, 19894), (19968, 40909), (63744, 64110), (64112, 64218), (131072, 173783), (173824, 177973), (177984, 178206), (194560, 195102)] == \
    [(0x2e80, 0x2e9a), (0x2e9b, 0x2ef4), (0x31c0, 0x31e4), (0x3400, 0x4db6), (0x4e00, 0x9fcd), (0xf900, 0xfa6e), (0xfa70, 0xfada), (0x20000, 0x2a6d7), (0x2a700, 0x2b735), (0x2b740, 0x2b81e), (0x2f800, 0x2fa1e)]
len(chars) == 75770 == 0x127fa
len_gaps == [26, -1, 89, -716, 36, -540, 6582, -74, 20941, -22835, 366, -2, 106, -66854, 42711, -41, 4149, -11, 222, -16354, 542]
'''














################################# discarded #####################################


if 0:
    #cs = CJK_chars = rw_chars('CJK_chars.gb18030.txt', chars_of_CJK(), gb18030)
    cs = CJK_chars = rw_chars('CJK_chars.utf8.txt', chars_of_CJK(), utf8)
    assert len(cs) == 75770 == 0x127fa

    rw_chars_to_html('CJK_chars.html', CJK_chars)
    rngs = group_sorted_chars(CJK_chars)
    assert rngs == [(11904, 11930), (11931, 12020), (12736, 12772),
                    (13312, 19894), (19968, 40909), (63744, 64110),
                    (64112, 64218), (131072, 173783), (173824, 177973),
                    (177984, 178206), (194560, 195102)
                    ] == \
            [(0x2e80, 0x2e9a), (0x2e9b, 0x2ef4), (0x31c0, 0x31e4),
             (0x3400, 0x4db6), (0x4e00, 0x9fcd), (0xf900, 0xfa6e),
             (0xfa70, 0xfada), (0x20000, 0x2a6d7), (0x2a700, 0x2b735),
             (0x2b740, 0x2b81e), (0x2f800, 0x2fa1e)]
    assert rngs2lens(rngs) == [26, 89, 36, 6582, 20941, 366, 106, 42711, 4149, 222, 542]
    assert rngs2gaps(rngs) == [1, 716, 540, 74, 22835, 2, 66854, 41, 11, 16354]
    assert sorted_non_overlap_rngs2len_gaps(rngs) == \
           [26, -1, 89, -716, 36, -540, 6582, -74, 20941, -22835,
            366, -2, 106, -66854, 42711, -41, 4149, -11, 222, -16354, 542]



if 0:
    chars_of_gb18030 = ''.join(chars_of(gb18030))
    assert len(chars_of_gb18030) == 1112064
    assert max_len_of_encoded_char(gb18030, chars_of_gb18030) == 4
if 0:
    tmp = info_of(gb18030) # == (_, 1112064, 4)
    tmp = info_of(gbk) # == (_, 21919, 2)

assert chr(0x25b2).encode(gbk) == b'\xa1\xf8'
if 0:
    rngs = group_chars_of(gb18030)
    # == [(0, 55296), (57344, 1114112)]
    # == [(0x0, 0xd800), (0xe000, 0x110000)]
    # == - (0xd800, 0xe000) = - '0xd[8-f]..'
    rngs = group_chars_of(gbk)
    '''
    [(0, 128), (164, 165), (167, 169), (176, 178), (183, 184),
     (215, 216), (224, 226), (232, 235), (236, 238), (242, 244),
     (247, 248), (249, 251), (252, 253), (257, 258), (275, 276),
     (283, 284), (299, 300), (324, 325), (328, 329), (333, 334),
     (363, 364), (462, 463), (464, 465), (466, 467), (468, 469),
     (470, 471), (472, 473), (474, 475), (476, 477), (593, 594),
     (609, 610), (711, 712), (713, 716), (729, 730), (913, 930),
     (931, 938), (945, 962), (963, 970), (1025, 1026), (1040, 1104),
     (1105, 1106), (8208, 8209), (8211, 8215), (8216, 8218),
     (8220, 8222), (8229, 8231), (8240, 8241), (8242, 8244),
     (8245, 8246), (8251, 8252), (8451, 8452), (8453, 8454),
     (8457, 8458), (8470, 8471), (8481, 8482), (8544, 8556),
     (8560, 8570), (8592, 8596), (8598, 8602), (8712, 8713),
     (8719, 8720), (8721, 8722), (8725, 8726), (8730, 8731),
     (8733, 8737), (8739, 8740), (8741, 8742), (8743, 8748),
     (8750, 8751), (8756, 8760), (8765, 8766), (8776, 8777),
     (8780, 8781), (8786, 8787), (8800, 8802), (8804, 8808),
     (8814, 8816), (8853, 8854), (8857, 8858), (8869, 8870),
     (8895, 8896), (8978, 8979), (9312, 9322), (9332, 9372),
     (9472, 9548), (9552, 9588), (9601, 9616), (9619, 9622),
     (9632, 9634), (9650, 9652), (9660, 9662), (9670, 9672),
     (9675, 9676), (9678, 9680), (9698, 9702), (9733, 9735),
     (9737, 9738), (9792, 9793), (9794, 9795), (12288, 12292),
     (12293, 12312), (12317, 12319), (12321, 12330),
     (12353, 12436), (12443, 12447), (12449, 12535),
     (12540, 12543), (12549, 12586), (12832, 12842),
     (12849, 12850), (12963, 12964), (13198, 13200),
     (13212, 13215), (13217, 13218), (13252, 13253),
     (13262, 13263), (13265, 13267), (13269, 13270),
     (19968, 40870), (63788, 63789), (63865, 63866),
     (63893, 63894), (63975, 63976), (63985, 63986),
     (64012, 64016), (64017, 64018), (64019, 64021),
     (64024, 64025), (64031, 64034), (64035, 64037),
     (64039, 64042), (65072, 65074), (65075, 65093),
     (65097, 65107), (65108, 65112), (65113, 65127),
     (65128, 65132), (65281, 65375), (65504, 65510)]
'''


    '''
    [(0x0, 0x80), (0xa4, 0xa5), (0xa7, 0xa9), (0xb0, 0xb2),
     (0xb7, 0xb8), (0xd7, 0xd8), (0xe0, 0xe2), (0xe8, 0xeb), (0xec,
     0xee), (0xf2, 0xf4), (0xf7, 0xf8), (0xf9, 0xfb), (0xfc, 0xfd),
     (0x101, 0x102), (0x113, 0x114), (0x11b, 0x11c), (0x12b, 0x12c),
     (0x144, 0x145), (0x148, 0x149), (0x14d, 0x14e), (0x16b, 0x16c),
     (0x1ce, 0x1cf), (0x1d0, 0x1d1), (0x1d2, 0x1d3), (0x1d4, 0x1d5),
     (0x1d6, 0x1d7), (0x1d8, 0x1d9), (0x1da, 0x1db), (0x1dc, 0x1dd),
     (0x251, 0x252), (0x261, 0x262), (0x2c7, 0x2c8), (0x2c9, 0x2cc),
     (0x2d9, 0x2da), (0x391, 0x3a2), (0x3a3, 0x3aa), (0x3b1, 0x3c2),
     (0x3c3, 0x3ca), (0x401, 0x402), (0x410, 0x450), (0x451, 0x452),
     (0x2010, 0x2011), (0x2013, 0x2017), (0x2018, 0x201a), (0x201c,
     0x201e), (0x2025, 0x2027), (0x2030, 0x2031), (0x2032, 0x2034),
     (0x2035, 0x2036), (0x203b, 0x203c), (0x2103, 0x2104), (0x2105,
     0x2106), (0x2109, 0x210a), (0x2116, 0x2117), (0x2121, 0x2122),
     (0x2160, 0x216c), (0x2170, 0x217a), (0x2190, 0x2194), (0x2196,
     0x219a), (0x2208, 0x2209), (0x220f, 0x2210), (0x2211, 0x2212),
     (0x2215, 0x2216), (0x221a, 0x221b), (0x221d, 0x2221), (0x2223,
     0x2224), (0x2225, 0x2226), (0x2227, 0x222c), (0x222e, 0x222f),
     (0x2234, 0x2238), (0x223d, 0x223e), (0x2248, 0x2249), (0x224c,
     0x224d), (0x2252, 0x2253), (0x2260, 0x2262), (0x2264, 0x2268),
     (0x226e, 0x2270), (0x2295, 0x2296), (0x2299, 0x229a), (0x22a5,
     0x22a6), (0x22bf, 0x22c0), (0x2312, 0x2313), (0x2460, 0x246a),
     (0x2474, 0x249c), (0x2500, 0x254c), (0x2550, 0x2574), (0x2581,
     0x2590), (0x2593, 0x2596), (0x25a0, 0x25a2), (0x25b2, 0x25b4),
     (0x25bc, 0x25be), (0x25c6, 0x25c8), (0x25cb, 0x25cc), (0x25ce,
     0x25d0), (0x25e2, 0x25e6), (0x2605, 0x2607), (0x2609, 0x260a),
     (0x2640, 0x2641), (0x2642, 0x2643), (0x3000, 0x3004), (0x3005,
     0x3018), (0x301d, 0x301f), (0x3021, 0x302a), (0x3041, 0x3094),
     (0x309b, 0x309f), (0x30a1, 0x30f7), (0x30fc, 0x30ff), (0x3105,
     0x312a), (0x3220, 0x322a), (0x3231, 0x3232), (0x32a3, 0x32a4),
     (0x338e, 0x3390), (0x339c, 0x339f), (0x33a1, 0x33a2), (0x33c4,
     0x33c5), (0x33ce, 0x33cf), (0x33d1, 0x33d3), (0x33d5, 0x33d6),
     (0x4e00, 0x9fa6), (0xf92c, 0xf92d), (0xf979, 0xf97a), (0xf995,
     0xf996), (0xf9e7, 0xf9e8), (0xf9f1, 0xf9f2), (0xfa0c, 0xfa10),
     (0xfa11, 0xfa12), (0xfa13, 0xfa15), (0xfa18, 0xfa19), (0xfa1f,
     0xfa22), (0xfa23, 0xfa25), (0xfa27, 0xfa2a), (0xfe30, 0xfe32),
     (0xfe33, 0xfe45), (0xfe49, 0xfe53), (0xfe54, 0xfe58), (0xfe59,
     0xfe67), (0xfe68, 0xfe6c), (0xff01, 0xff5f), (0xffe0, 0xffe6)]'''
    


if 0:
    def chars_of(encoding):
        for i in range(0x110000):
            try:
                ch = chr(i)
            except:
                while True:
                    inp = input('at ord({}) continue ? [Nothing/Y or N]:'.format(i))
                    inp = inp.strip().upper()
                    if not inp or inp == "Y":
                        break
                    elif inp == "N":
                        return
                    else:
                        continue
            if includes(encoding, ch):
                yield ch












