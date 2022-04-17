#__all__:goto
#doctest:goto
r'''[[[[[
b64_cfg_case <- {std, urlsafe} | may bytes{len>=2}#may altchars
byteorder <- {big, little}
bigendian :: bool


seed.text.base64
py -m seed.text.base64
from seed.text.base64 import uint__to__radix64_digits_, uint__from__radix64_digits_, uint__to__radix64_digits__b64__str_, uint__from__radix64_digits__b64__str_

e ../../python3_src/seed/text/base64.py

本模块 主要 是 利用 base64 将 自然数 表达为 16进制数(任意radix 见其他模块，下面有提及)
    uint__to__radix64_digits_
    uint__from__radix64_digits_
        编码为16进制数
    uint__to__radix64_digits__b64__str_
    uint__from__radix64_digits__b64__str_
        紧凑表达，用于存储，比base64短！
            #使用 utf8 编码
            [1..63] 只用 1字节
            [64..4095] 只用 2字节
            [4096..2**18-1] 只用 3字节
        但 以上这些，base64 均 4字节

[[[
see:
    seed.int_tools.repr_uint
    seed.int_tools.uint_bits_utils
    seed.int_tools.digits.uint2radix_repr
    seed.int_tools.digits.radix_repr2uint
    py::base64
        字母表 次序:
            std:        A-Za-z0-9+/   =
            urlsafe:    A-Za-z0-9-_   =
        最后填充『==』 ==>>  最后4bit 为填充0
            最后尾数是:
            A   Q   g   w A ...
            0  16  32  48
        最后填充『=』 ==>>  最后2bit 为填充0
            最后尾数是:
            A   E   I   M   Q ...
            0   4   8   12  14
        最后无填充『』 ==>>  最后无为填充比特
            最后尾数是:
            A   B   C   D ...
            0   1   2   4

######################
from seed.int_tools.uint_bits_utils import uint2bytes, uint2iter_bits
def uint2bytes(u, byteorder, bit_length=None):
def uint2iter_bits(u, bitorder, min_len=None, bit_length=None):

######################
from seed.int_tools.repr_uint import uint2reprdigits, uint2iter_reprdigits_LE, iter_reprdigits2uint
######################
from seed.int_tools.digits.uint2radix_repr import uint2radix_repr
from seed.int_tools.digits.radix_repr2uint import radix_repr2uint

######################
base64.b64encode(s, altchars=None)

    Encode the bytes-like object s using Base64 and return the encoded bytes.

    Optional altchars must be a bytes-like object of at least length 2 (additional characters are ignored) which specifies an alternative alphabet for the + and / characters. This allows an application to e.g. generate URL or filesystem safe Base64 strings. The default is None, for which the standard Base64 alphabet is used.

base64.b64decode(s, altchars=None, validate=False)

    Decode the Base64 encoded bytes-like object or ASCII string s and return the decoded bytes.

    Optional altchars must be a bytes-like object or ASCII string of at least length 2 (additional characters are ignored) which specifies the alternative alphabet used instead of the + and / characters.

    A binascii.Error exception is raised if s is incorrectly padded.

    If validate is False (the default), characters that are neither in the normal base-64 alphabet nor the alternative alphabet are discarded prior to the padding check. If validate is True, these non-alphabet characters in the input result in a binascii.Error.


base64.standard_b64encode(s)

    Encode bytes-like object s using the standard Base64 alphabet and return the encoded bytes.

base64.standard_b64decode(s)

    Decode bytes-like object or ASCII string s using the standard Base64 alphabet and return the decoded bytes.

base64.urlsafe_b64encode(s)

    Encode bytes-like object s using the URL- and filesystem-safe alphabet, which substitutes - instead of + and _ instead of / in the standard Base64 alphabet, and return the encoded bytes. The result can still contain =.

base64.urlsafe_b64decode(s)

    Decode bytes-like object or ASCII string s using the URL- and filesystem-safe alphabet, which substitutes - instead of + and _ instead of / in the standard Base64 alphabet, and return the decoded bytes.
######################
######################
######################

bytes.translate(table, /, delete=b'')
bytearray.translate(table, /, delete=b'')¶

    Return a copy of the bytes or bytearray object where all bytes occurring in the optional argument delete are removed, and the remaining bytes have been mapped through the given translation table, which must be a bytes object of length 256.

    You can use the bytes.maketrans() method to create a translation table.

    Set the table argument to None for translations that only delete characters:
    >>>

    >>> b'read this short text'.translate(None, b'aeiou')
    b'rd ths shrt txt'

    Changed in version 3.6: delete is now supported as a keyword argument.


static bytes.maketrans(from, to)
static bytearray.maketrans(from, to)

    This static method returns a translation table usable for bytes.translate() that will map each character in from into the character at the same position in to; from and to must both be bytes-like objects and have the same length.

######################
######################
str.translate(table)

    Return a copy of the string in which each character has been mapped through the given translation table. The table must be an object that implements indexing via __getitem__(), typically a mapping or sequence. When indexed by a Unicode ordinal (an integer), the table object can do any of the following: return a Unicode ordinal or a string, to map the character to one or more other characters; return None, to delete the character from the return string; or raise a LookupError exception, to map the character to itself.

    You can use str.maketrans() to create a translation map from character-to-character mappings in different formats.

    See also the codecs module for a more flexible approach to custom character mappings.


static str.maketrans(x[, y[, z]])

    This static method returns a translation table usable for str.translate().

    If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters (strings of length 1) to Unicode ordinals, strings (of arbitrary lengths) or None. Character keys will then be converted to ordinals.

    If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

######################
######################

int.to_bytes(length, byteorder, *, signed=False)

    Return an array of bytes representing an integer.

    >>> (1024).to_bytes(2, byteorder='big')
    b'\x04\x00'
    >>> (1024).to_bytes(10, byteorder='big')
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'
    >>> (-1024).to_bytes(10, byteorder='big', signed=True)
    b'\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00'
    >>> x = 1000
    >>> x.to_bytes((x.bit_length() + 7) // 8, byteorder='little')
    b'\xe8\x03'

    The integer is represented using length bytes. An OverflowError is raised if the integer is not representable with the given number of bytes.

    The byteorder argument determines the byte order used to represent the integer. If byteorder is "big", the most significant byte is at the beginning of the byte array. If byteorder is "little", the most significant byte is at the end of the byte array. To request the native byte order of the host system, use sys.byteorder as the byte order value.

    The signed argument determines whether two’s complement is used to represent the integer. If signed is False and a negative integer is given, an OverflowError is raised. The default value for signed is False.

    New in version 3.2.

classmethod int.from_bytes(bytes, byteorder, *, signed=False)

    Return the integer represented by the given array of bytes.

    >>> int.from_bytes(b'\x00\x10', byteorder='big')
    16
    >>> int.from_bytes(b'\x00\x10', byteorder='little')
    4096
    >>> int.from_bytes(b'\xfc\x00', byteorder='big', signed=True)
    -1024
    >>> int.from_bytes(b'\xfc\x00', byteorder='big', signed=False)
    64512
    >>> int.from_bytes([255, 0, 0], byteorder='big')
    16711680

    The argument bytes must either be a bytes-like object or an iterable producing bytes.

    The byteorder argument determines the byte order used to represent the integer. If byteorder is "big", the most significant byte is at the beginning of the byte array. If byteorder is "little", the most significant byte is at the end of the byte array. To request the native byte order of the host system, use sys.byteorder as the byte order value.

    The signed argument indicates whether two’s complement is used to represent the integer.

    New in version 3.2.

######################
######################
]]]





[[[doctest
#b64_cfg_case, byteorder
b64encode__uint2str_
b64decode__uint5str_

#b64_cfg_case, bigendian
uint__to__radix64_digits__b64__str_
uint__from__radix64_digits__b64__str_

#bigendian, may_digit5uint6
uint__to__radix64_digits_
#bigendian, may_digit2uint6
uint__from__radix64_digits_




>>> sorted(b64_cfg_case2b64_alphabet_and_pad_byte.items())
[('std', b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='), ('urlsafe', b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_=')]

#>>> sorted(b64_cfg_case2table_pair.items())





#b64_cfg_case, byteorder
b64encode__uint2str_
b64decode__uint5str_
>>> b64encode__uint2str_(0, b64_cfg_case='std', byteorder='big')
''
>>> b64encode__uint2str_(0, b64_cfg_case='urlsafe', byteorder='little')
''
>>> b64encode__uint2str_(63*64+62, b64_cfg_case='std', byteorder='big')
'D/4='
>>> b64encode__uint2str_(63*64+62, b64_cfg_case='urlsafe', byteorder='little')
'_g8='

#>>> b64encode__bs2bs_(b'\63\62', b64_cfg_case='std') b'MzI='中间多了2个比特0！
>>> b2 = bytes([63>>2, ((63&0b11)<<6)+62])
>>> b64encode__bs2bs_(b2, b64_cfg_case='std')
b'D/4='
>>> b64encode__bs2bs_(b2[::-1], b64_cfg_case='urlsafe')
b'_g8='

b64xxx 命名的函数 不可用作16进制数，因为 大端序，从 大端/头部 开始 切成 6比特每块，，在 小端/尾部 填充
    可与 uint__to__radix64_digits_xxx 命名的函数 的输出 相比



#b64_cfg_case, bigendian
uint__to__radix64_digits__b64__str_
uint__from__radix64_digits__b64__str_
>>> uint__to__radix64_digits__b64__str_(0, b64_cfg_case='std', bigendian=False)
''
>>> uint__to__radix64_digits__b64__str_(0, b64_cfg_case='urlsafe', bigendian=True)
''
>>> uint__to__radix64_digits__b64__str_(63*64+62, b64_cfg_case='std', bigendian=True)
'/+'
>>> uint__to__radix64_digits__b64__str_(63*64+62, b64_cfg_case='urlsafe', bigendian=False)
'-_'
>>> uint__to__radix64_digits__b64__str_(63*64+62, b64_cfg_case=None, bigendian=False)
'+/'
>>> uint__to__radix64_digits__b64__str_(63*64+62, b64_cfg_case=b'=!', bigendian=False)
'=!'


#bigendian, may_digit5uint6
uint__to__radix64_digits_
#bigendian, may_digit2uint6
uint__from__radix64_digits_
>>> idx4d5u = 1 #table_pair #not 0!!!
>>> idx4d2u = 1 - idx4d5u
>>> uint__to__radix64_digits_(0, bigendian=False, may_digit5uint6=None)
b''
>>> uint__to__radix64_digits_(0, bigendian=True, may_digit5uint6=b64_cfg_case2table_pair['std'][idx4d5u])
()
>>> uint__to__radix64_digits_(63*64+62, bigendian=False, may_digit5uint6=None)
b'>?'
>>> [*b'>?']
[62, 63]
>>> uint__from__radix64_digits_([62, 63], bigendian=False, may_digit2uint6=None)
4094
>>> 63*64+62
4094
>>> uint__to__radix64_digits_(63*64+62, bigendian=True, may_digit5uint6=b64_cfg_case2table_pair['std'][idx4d5u])
(47, 43)
>>> bytes((47, 43))
b'/+'
>>> uint__from__radix64_digits_(b'/+', bigendian=True, may_digit2uint6=b64_cfg_case2table_pair['std'][idx4d2u]) == 63*64+62
True




]]]


#]]]]]'''



#__all__:goto
__all__ = '''

uint__to__radix64_digits_
uint__from__radix64_digits_
    uint__to__radix64_digits__b64__bytes_
    uint__from__radix64_digits__b64__bytes_

    uint__to__radix64_digits__b64__str_
    uint__from__radix64_digits__b64__str_










b64_cfg_case2b64_alphabet_and_pad_byte
b64_cfg_case2table_pair

b64encode__bs2bs__altchars
b64decode__bs2bs__altchars
    b64encode__bs2bs__std
    b64decode__bs2bs__std
    b64encode__bs2bs__urlsafe
    b64decode__bs2bs__urlsafe
        b64encode__bs2bs_
        b64decode__bs2bs_
            b64encode__uint2bs_
            b64decode__uint5bs_
                b64encode__uint2str_
                b64decode__uint5str_

            uint__to__radix64_digits__b64__bytes_
            uint__from__radix64_digits__b64__bytes_
                uint__to__radix64_digits__b64__str_
                uint__from__radix64_digits__b64__str_

                uint__to__radix64_digits_
                uint__from__radix64_digits_


    #'''.split()


from base64 import standard_b64encode as b64encode__bs2bs__std, standard_b64decode as b64decode__bs2bs__std
from base64 import urlsafe_b64encode as b64encode__bs2bs__urlsafe, urlsafe_b64decode as b64decode__bs2bs__urlsafe
from base64 import b64encode as _b64encode__bs2bs__altchars, b64decode as _b64decode__bs2bs__altchars

from seed.int_tools.uint_bits_utils import uint2bytes, uint2iter_bits
from seed.tiny import expectError, check_uint, MapView
from seed.int_tools.int_tools import uint2bytes_, align_length#, byte_length_of#, bit_length_of, unit_length2block_length, bit_length2byte_length

if 0:
    r'''
def convert__3_uint8__to__4_uint6__LE(
    uint6 = uint-6bit = uint%64
    8bit*3 == 6bit*4
    #'''

r'''
from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
class Info4DigitNbit:
    def __init__(sf, N, /):
        check_int_ge(1, N)
        N = sf._N = N
        n = sf._n_low_bytes = N >> 3
        m = sf._m_high_bits = N & 7
        high_mask = sf._high_mask = (1<<m) - 1
        offset_pairs = sf._offset_pairs = []
        for i in range(0, N*(8+1), N):
            (offset4bytes, offset4bits) = divmid(i, 8)
            offset_pairs.append((offset4bytes, offset4bits))
        end = offset_pairs.index(offset_pairs[0], 1)
        assert end in [1, 2, 4, 8]
        calc delta offset4bytes
        #del offset_pairs[end:]
        del offset_pairs[8:] #to support offset_pairs[-1]
    def uint2radix_digitsLE(sf, u, /):
        check_int_ge(0, u)
        N = sf._N
        n = sf._n_low_bytes
        m = sf._m_high_bits
        high_mask = sf._high_mask
        offset_pairs = sf._offset_pairs

        i = u
        L = 8
        bss = [None]*L
        for j in range(L):
            bs = uint2bytes(i, byteorder='little')
            bss[-j] = bs
            i >>= 1
        def get_bs(offset4bits, /)
        M = len(get(0))
        for j, _ in enumerate(range(0, M*L, N)):
            j &= 7
            (offset4bytes, offset4bits) = offset_pairs[j]
            bs = get_bs(offset4bits)
            low_bytes = bs[offset4bytes:offset4bytes+n]
            bs = get_mask(n)
    @classmethod
    def get_mask(cls, offset4bits, /):
#'''

def b64encode__bs2bs__altchars(may_altchars, bs, /):
    return _b64encode__bs2bs__altchars(bs, may_altchars)
def b64decode__bs2bs__altchars(may_altchars, bs, /):
    return _b64decode__bs2bs__altchars(bs, may_altchars)

_case2codec_pair = dict(
    std=(b64encode__bs2bs__std, b64decode__bs2bs__std)
    ,urlsafe=(b64encode__bs2bs__urlsafe, b64decode__bs2bs__urlsafe)
    )
_codec_pair4alt = (b64encode__bs2bs__altchars, b64decode__bs2bs__altchars)
def _case__to__codec_pair__args(b64_cfg_case, /):
    m = _case2codec_pair.get(b64_cfg_case)
    if m is None:
        #altchars = memoryview(b64_cfg_case)
        #args = (altchars,)
        may_altchars = b64_cfg_case
        args = (may_altchars,)
        codec_pair = _codec_pair4alt
    else:
        codec_pair = m
        args = ()
    return codec_pair, args
def b64encode__bs2bs_(bs, /,*, b64_cfg_case):
    codec_pair, args = _case__to__codec_pair__args(b64_cfg_case)
    _b64encode__bs2bs, _ = codec_pair
    bs = _b64encode__bs2bs(*args, bs)
    return bs
def b64decode__bs2bs_(bs, /,*, b64_cfg_case):
    codec_pair, args = _case__to__codec_pair__args(b64_cfg_case)
    _, _b64decode__bs2bs = codec_pair
    bs = _b64decode__bs2bs(*args, bs)
    return bs


def b64encode__uint2bs_(u, /,*, b64_cfg_case, byteorder):
    #if not u >= 0: raise ValueError
        #since to_bytes(): signed=False
    bs = uint2bytes(u, byteorder=byteorder)
    bs = b64encode__bs2bs_(bs, b64_cfg_case=b64_cfg_case)
    return bs
def b64decode__uint5bs_(bs, /,*, b64_cfg_case, byteorder):
    bs = b64decode__bs2bs_(bs, b64_cfg_case=b64_cfg_case)
    u = int.from_bytes(bs, byteorder=byteorder)
    #if not u >= 0: raise ValueError
        #since from_bytes(): signed=False
    return u

#b64encode__uint2bs_(-1, b64_cfg_case='std', byteorder='little')
#assert expectError(OverflowError, lambda:b64encode__uint2bs_(-1, 'std'))

def b64encode__uint2str_(u, /,*, b64_cfg_case, byteorder):
    bs = b64encode__uint2bs_(u, b64_cfg_case=b64_cfg_case, byteorder=byteorder)
    s = bs.decode('ascii')
    return s
def b64decode__uint5str_(s, /,*, b64_cfg_case, byteorder):
    bs = s.encode('ascii')
    u = b64decode__uint5bs_(bs, b64_cfg_case=b64_cfg_case, byteorder=byteorder)
    return u

def _mk_part4table(first_char, last_char, /):
    return bytes(range(ord(first_char), ord(last_char)+1))
def _mk_half_table(char_pairs, /):
    if not len(char_pairs)&1 == 0: raise TypeError
    return b''.join(map(_mk_part4table, char_pairs[0::2], char_pairs[1::2]))
def _mk_table(from__char_pairs, to__char_pairs, /):
    from_ = _mk_half_table(from__char_pairs)
    to_ = _mk_half_table(to__char_pairs)
    table = bytes.maketrans(from_, to_)
    return table
def _mk_table_pair(from__char_pairs, to__char_pairs, /):
    table = _mk_table(from__char_pairs, to__char_pairs)
    inv_table = _mk_table(to__char_pairs, from__char_pairs)
    return table, inv_table
def _mk_table_pair4radix(radix, from__char_pairs, /):
    assert 0 < radix < 2**8
    to__char_pairs = '\0' + chr(radix-1)
    table_pair = _mk_table_pair(from__char_pairs, to__char_pairs)
    return table_pair #(digit2uint_modN, digit5uint_modN=uint_modN2digit)

_cases = sorted(_case2codec_pair)
_case_set = frozenset(_cases)
_case2char_pairs4b64_alphabet_and_pad_byte = dict(
    std=('AZaz09++//==')
    ,urlsafe=('AZaz09--__==')
    )
_case2b64_alphabet_and_pad_byte = {b64_cfg_case:_mk_half_table(char_pairs4alphabet_pad) for b64_cfg_case, char_pairs4alphabet_pad in _case2char_pairs4b64_alphabet_and_pad_byte.items()}
_case2table_pair = {b64_cfg_case:_mk_table_pair4radix(64, char_pairs4alphabet_pad[:-2]) for b64_cfg_case, char_pairs4alphabet_pad in _case2char_pairs4b64_alphabet_and_pad_byte.items()}
    #{b64_cfg_case: (digit2uint6/bytes{len=256}, digit5uint6/bytes{len=256})}
    #{case: (digit2uint6, digit5uint6)}
    #{case: (d2u, u2d)}
b64_cfg_case2table_pair = MapView(_case2table_pair)
b64_cfg_case2b64_alphabet_and_pad_byte = MapView(_case2b64_alphabet_and_pad_byte)
    #{b64_cfg_case: bytes{len=65}}

_2_case2b64_alphabet_and_pad_byte = dict(
    std=_mk_half_table('AZaz09++//==')
    ,urlsafe=_mk_half_table('AZaz09--__==')
    )
_2_case2table_pair = dict(
    std=_mk_table_pair4radix(64, 'AZaz09++//')
    ,urlsafe=_mk_table_pair4radix(64, 'AZaz09--__')
    )
assert _case_set == _case2b64_alphabet_and_pad_byte.keys()
assert _2_case2b64_alphabet_and_pad_byte == _case2b64_alphabet_and_pad_byte
assert _2_case2table_pair == _case2table_pair

def uint__to__radix64_digits_(u, /, *, bigendian, may_digit5uint6):
    '-> [uint%64]&bytes'
    b64_cfg_case = 'std'
    #table, inv_table = _case2table_pair[b64_cfg_case]
    digit2uint6, digit5uint6 = _case2table_pair[b64_cfg_case]
    ds = uint__to__radix64_digits__b64__bytes_(u, b64_cfg_case=b64_cfg_case, bigendian=bigendian)
    bs = ds.translate(digit2uint6)
    if may_digit5uint6 is not None:
        u2d = digit5uint6 = may_digit5uint6
        return tuple(u2d[i] for i in bs)
    return bs
def uint__from__radix64_digits_(bs, /, *, bigendian, may_digit2uint6):
    if may_digit2uint6 is not None:
        d2u = digit2uint6 = may_digit2uint6
        digits = bs
        bs = bytes(d2u[d] for d in digits)
    elif (type(bs) is bytes or type(bs) is bytearray):
        bs = bs
    else:
        bs = bytes(bs)
    bs = digits = bs
    b64_cfg_case = 'std'
    #table, inv_table = _case2table_pair[b64_cfg_case]
    digit2uint6, digit5uint6 = _case2table_pair[b64_cfg_case]
    ds = bs.translate(digit5uint6)
    u = uint__from__radix64_digits__b64__bytes_(ds, b64_cfg_case=b64_cfg_case, bigendian=bigendian)
    return u
def uint__to__radix64_digits__b64__bytes_(u, /, *, b64_cfg_case, bigendian):
    '-> b64_digit_bytes<b64_cfg_case>'
    bs = uint2bytes_(u, byteorder='big', alignment=3)
    bs = b64encode__bs2bs_(bs, b64_cfg_case=b64_cfg_case)
    if 1:
        # aligned ==>> no pad at tail
        # only need to skip leading 0s
        if 1:
            #ord4zero = _case2b64_alphabet_and_pad_byte[b64_cfg_case][0]
            #   now, b64_cfg_case can be may_altchars
            ord4zero = b'A'[0]

        for idx, x in enumerate(bs):
            if not x == ord4zero: break
        else:
            idx = len(bs)
        bs = bs[idx:]
    if not bigendian:
        bs = bs[::-1]
    return bs

    ######################
    #bug: bs =  b64encode__uint2bs_(u, b64_cfg_case=b64_cfg_case, byteorder='little')
    #   SHOULD BE u.to_bytes(align_length(3, byte_length_of(u)), byteorder='big')
    #   since b64 concat bits inter-neighbor-byte as-if bigendian ==>> bytes must be bigendian too!!!
    #
    bs =  b64encode__uint2bs_(u, b64_cfg_case=b64_cfg_case, byteorder='little')
    ord4pad = _case2b64_alphabet_and_pad_byte[b64_cfg_case][-1]
    ord4zero = _case2b64_alphabet_and_pad_byte[b64_cfg_case][0]
    end = len(bs)
    for x in [ord4pad, ord4zero]:
        while end:
            end -= 1
            if not bs[end] == x:
                end += 1
                break
    bs = bs[:end]
    if bigendian:
        bs = bs[::-1]
    return bs

def uint__from__radix64_digits__b64__bytes_(bs, /, *, b64_cfg_case, bigendian):
    if not bigendian:
        bs = bs[::-1]
    L = align_length(4, len(bs))
    num_leading_0s = L - len(bs)
    if 1:
        #byte4zero = _case2b64_alphabet_and_pad_byte[b64_cfg_case][:1]
        #   now, b64_cfg_case can be may_altchars
        byte4zero = b'A'
    bs = byte4zero * num_leading_0s + bs
    bs =  b64decode__bs2bs_(bs, b64_cfg_case=b64_cfg_case)
    u = int.from_bytes(bs, byteorder='big')
        #from_bytes(): signed=False
    return u

    ######################buggy version paired above
    if bigendian:
        bs = bs[::-1]
    L = len(bs)
    R = L&3 # L%4
    if R == 0:
        #if (L*6)%8 == 0:
        #if L%4 == 0:
        pass
    else:
        bs += b'A'*(4-R)
    u =  b64decode__uint5bs_(bs, b64_cfg_case=b64_cfg_case, byteorder='little')
    return u

def uint__to__radix64_digits__b64__str_(u, /, *, b64_cfg_case, bigendian):
    '-> b64_digit_str<b64_cfg_case>'
    bs = uint__to__radix64_digits__b64__bytes_(u, b64_cfg_case=b64_cfg_case, bigendian=bigendian)
    s = bs.decode('ascii')
    return s
def uint__from__radix64_digits__b64__str_(s, /, *, b64_cfg_case, bigendian):
    bs = s.encode('ascii')
    u = uint__from__radix64_digits__b64__bytes_(bs, b64_cfg_case=b64_cfg_case, bigendian=bigendian)
    return u


#std:       A-Za-z0-9+/   =
#urlsafe:   A-Za-z0-9-_   =
#A  Q   g   w
#0  16  32  48
def _show_alphabet__b64(b64_cfg_case, /):
    print(b64_cfg_case)
    print(f'=====[0..255]')
    for i in range(2**8):
        bs = bytes([i])
        bs = b64encode__bs2bs_(bs, b64_cfg_case=b64_cfg_case)
        print(bs)
        r'''
b'AA=='
b'AQ=='
b'Ag=='
b'Aw=='
b'BA=='
b'BQ=='
b'Bg=='
b'Bw=='
b'CA=='
b'CQ=='
b'Cg=='
b'Cw=='
b'DA=='
b'DQ=='
    big-endian?
    #std:       A-Za-z0-9+/   =
    #urlsafe:   A-Za-z0-9-_   =
    #A  Q   g   w
    #0  16  32  48
    最后4bit不用???
    6*2/%8=1,4
    6*3/%8=2,2
    6*4/%8=3,0
        #'''
    print(f'=====[0..0][0..255]')
    for i in range(2**8):
        bs = bytes([0,i])
        bs = b64encode__bs2bs_(bs, b64_cfg_case=b64_cfg_case)
        print(bs)
        r'''
b'AAA='
b'AAE='
b'AAI='
b'AAM='
b'AAQ='
b'AAU='
b'AAY='
b'AAc='
b'AAg='
b'AAk='
b'AAo='
b'AAs='
b'AAw='
b'AA0='
b'AA4='
b'AA8='
b'ABA='
b'ABE='
b'ABI='
    A   E   I   M   Q
    0   4   8   12  14
    最后填充『==』 ==>>  最后4bit 为填充0
    最后填充『=』 ==>>  最后2bit 为填充0
    最后无填充『』 ==>>  最后无为填充比特
        #'''
    print(f'=====[0..0][0..0][0..255]')
    for i in range(2**8):
        bs = bytes([0,0,i])
        bs = b64encode__bs2bs_(bs, b64_cfg_case=b64_cfg_case)
        print(bs)
        r'''
b'AAAA'
b'AAAB'
b'AAAC'
b'AAAD'
b'AAAE'
b'AAAF'
        #'''
    print(f'=====[0..0]*n')
    for i in range(8):
        bs = b'\0'*i
        bs = b64encode__bs2bs_(bs, b64_cfg_case=b64_cfg_case)
        print(bs)
        r'''
b''
b'AA=='     『==』最后4bit 为填充0
b'AAA='     『==』最后2bit 为填充0
b'AAAA'
b'AAAAAA=='
b'AAAAAAA='
b'AAAAAAAA'
b'AAAAAAAAAA=='
    看来确实是 64进制？
    使用了65个字符 『=』填充
    每次 增加 4字符，太糟糕！
        #'''
def _x_show_alphabet__b64(b64_cfg_case, /):
    print(b64_cfg_case)
    ords = []
    for i in range(2**8):
        bs = bytes([i])
        bs = b64encode__bs2bs_(bs, b64_cfg_case=b64_cfg_case)
        print(bs)
        ords.append(bs[0])
    assert len(ords) == 64
    assert len({*ords}) == 64, (len({*ords}), bytes(ords))
    assert sorted(ords) == ords
    alphabet = bytes(ords)
    ords = {*ords}
    for i in range(8):
        bs = b'\0'*i
        bs = b64encode__bs2bs_(bs, b64_cfg_case=b64_cfg_case)
        print(bs)

        if bs[-1] not in ords:
            pad = bs[:-1]
            break
    else:
        raise logic-err
    print(b64_cfg_case, alphabet, pad)

if 0:
    if __name__ == "__main__":
        _show_alphabet__b64('std')
        _show_alphabet__b64('urlsafe')

def _t():
    r'''
b64encode__uint2str_
b64decode__uint5str_
    b64encode__uint2bs_
    b64decode__uint5bs_
        b64encode__bs2bs_
        b64decode__bs2bs_

uint__to__radix64_digits_
uint__from__radix64_digits_
    uint__to__radix64_digits__b64__bytes_
    uint__from__radix64_digits__b64__bytes_
    uint__to__radix64_digits__b64__str_
    uint__from__radix64_digits__b64__str_
    #'''
    lcm_6_8 = 24
    max_bit_len = lcm_6_8 * 2
    def iter_uints_of_bit_len_(bit_len, /):
        i = (1 >> bit_len)
        yield i
        if i-1 >= 0: yield i-1
        if i-2 >= 0: yield i-2
        j = (63 >> bit_len)
        yield j
        yield j ^ 62
        yield j ^ 61
    def iter_uints():
        yield from range(2**10+1)
        for n in range(max_bit_len+1):
            yield from iter_uints_of_bit_len_(n)
    cs = _cases
    _byteorders = 'big little'.split()
    _bigendians = [False, True]
    _mm_pairs = [(None, None), *_case2table_pair.values()]
        #[(may_digit2uint6, may_digit5uint6)]
        #   NOTE: not reverse! is (2,5) not (5,2)
    def test_uints(us, /):
        for u in us:
            check_uint(u)
            test_uint(u)
    def test_uint(u, /):
        #b64_cfg_case, byteorder
        b64encode__uint2str_
        b64decode__uint5str_

        #b64_cfg_case, bigendian
        uint__to__radix64_digits__b64__str_
        uint__from__radix64_digits__b64__str_

        #bigendian, may_digit5uint6
        uint__to__radix64_digits_
        #bigendian, may_digit2uint6
        uint__from__radix64_digits_

        #b64_cfg_case, byteorder
        for b64_cfg_case in cs:
            for byteorder in _byteorders:
                d = dict(b64_cfg_case=b64_cfg_case, byteorder=byteorder)
                ds = b64encode__uint2str_(u, **d)
                _u = b64decode__uint5str_(ds, **d)
                assert _u == u
            # above two ds not reversed

        #b64_cfg_case, bigendian
        uint__to__radix64_digits__b64__str_
        uint__from__radix64_digits__b64__str_
        for b64_cfg_case in cs:
            dss = []
            for bigendian in _bigendians:
                d = dict(b64_cfg_case=b64_cfg_case, bigendian=bigendian)
                ds = uint__to__radix64_digits__b64__str_(u, **d)
                _u = uint__from__radix64_digits__b64__str_(ds, **d)
                assert _u == u
                dss.append(ds)
            ds0, ds1 = dss
            assert [*ds0] == [*reversed(ds1)]

        #bigendian, may_digit5uint6
        uint__to__radix64_digits_
        #bigendian, may_digit2uint6
        uint__from__radix64_digits_
        for (may_digit2uint6, may_digit5uint6) in _mm_pairs:
            dss = []
            for bigendian in _bigendians:
                d5 = dict(may_digit5uint6=may_digit5uint6, bigendian=bigendian)
                d2 = dict(may_digit2uint6=may_digit2uint6, bigendian=bigendian)
                ds = uint__to__radix64_digits_(u, **d5)
                _u = uint__from__radix64_digits_(ds, **d2)
                assert _u == u
                dss.append(ds)
            ds0, ds1 = dss
            assert [*ds0] == [*reversed(ds1)]

    def main():
        us = [*iter_uints()]
        test_uints(us)
    return main()




if __name__ == "__main__":
    _t()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):


