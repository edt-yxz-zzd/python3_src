
r'''

using bytes.translate to speed up reversing bits
using icut_to to chop iterable into std-size-seq to perform more concrete operations




min_len and bit_length:
    if bit_length is None:
        bit_length = u.bit_length()
    if min_len is None:
        min_len = bit_length
    min_len = bit_length = max(bit_length, min_len)
    del min_len
    size = (bit_length+7)//8
    u.to_bytes(size, byteorder)
'''

__all__ = '''
    memoryview_B1D
    uint2bytes
    uint2iter_bytess

    uint2iter_bitsLE
    uint2iter_bitsBE
    uint2iter_bits

    uint2bitsLE
    uint2bitsBE
    uint2iter_expsLE
    uint2expsLE




    uint8s2bitsBE
    uint8s2bitsLE

    reverse_uint8
    reverse_bytes
    reverse_bytes_and_bits_per_byte
    reverse_bitorder_per_byte
    std_data_bitorder

    reverse_uint32
    uint8_to_reversed_byte
    uint8_to_reversed_uint8
    byte2reversed_byte_table
    uint8_to_bitsBE
    uint8_to_bitsLE
    byte_MSB_first_to_uint8XE2uint8BE



    bitseq8sBE2bytes
    bitseqBE2bytes_padlen
    bitseqBE2uint_padlen
    bitseqBE2uint
    bitsBE2bytes_padlen
    bitsBE2uint_padlen
    bitsBE2uint

    bitseqLE2bytes
    bitsLE2bytes
    bitseqLE2uint
    bitsLE2uint



    reverse_uint
    reverse_uint32


'''.split()

##
##import operator
##import functools
import itertools
from collections import Sequence

from seed.iters.icut_to import icut_to, icut_seq_to
from seed.helper.check_utils import to_uint, to_pint
from ._uint_bits_utils__plain import \
    uint8_to_bitsBE,\
    uint8_to_bitsLE,\
    byte_MSB_first_to_uint8XE2uint8BE,\
    uint8_to_reversed_uint8,\
    uint8_to_reversed_byte,\
    byte2reversed_byte_table

#from ._uint_bits_utils__plain import *



def memoryview_B1D(data):
    'unsigned byte array (1 dim)'
    return memoryview(data).cast('B')


def fix_uint_bit_length(u, bit_length):
    u = to_uint(u, 'u')
    if bit_length is None:
        L = u.bit_length()
    else:
        L = to_uint(bit_length, 'bit_length')
    return u, L
def fix_uint_bit_length_min_len(u, min_len, bit_length):
    u, bit_length = fix_uint_bit_length(u, bit_length)
    if min_len is not None:
        bit_length = max(bit_length, int(min_len))
    min_len = bit_length
    return u, min_len, bit_length
    min_len = bit_length if min_len is None else int(min_len)
    min_len = bit_length = max(bit_length, min_len)

def uint2bytes(u, byteorder, bit_length=None):
    u, L = fix_uint_bit_length(u, bit_length)
    size = (L+7) >> 3 # (L+7)//8
    bs = u.to_bytes(size, byteorder)
    if bit_length is None:
        assert not bs or bs[0 if byteorder == 'big' else -1]
    return bs

#default_bytes_size = 8 << 20
def uint2iter_bytess(u, item_size, byteorder, bit_length=None):
    #item_size = to_pint(item_size, 'item_size')
    bs = uint2bytes(u, byteorder, bit_length)
    return icut_seq_to(bs, item_size)
##
##    for i in range(0, size, item_size):
##        yield bs[i:i+item_size]


def uint2iter_bitsLE(u, min_len=None, bit_length=None):
    return uint2iter_bits(u, 'little', min_len, bit_length)
def uint2iter_bitsBE(u, min_len=None, bit_length=None):
    return uint2iter_bits(u, 'big', min_len, bit_length)
def uint2iter_bits(u, bitorder, min_len=None, bit_length=None):
    'byteorder == bitorder; recommand "big"'
    u, min_len, bit_length = fix_uint_bit_length_min_len(u, min_len, bit_length)
    del min_len

    bs = uint2bytes(u, bitorder, bit_length)
    if bitorder == 'big':
        f = uint8s2bitsBE
        # drop leading 0s
        it = iter(f(bs))
        ls = list(itertools.islice(it, (len(bs)<<3) - bit_length))
        assert not any(ls)
        return it
    elif bitorder == 'little':
        f = uint8s2bitsLE
        # drop leading 0s which are at tail
        return itertools.islice(f(bs), bit_length)
    raise logic-error


def uint2expsLE(u):
    '''list exps in LSB first order

>>> uint2expsLE(5)
[0, 2]
'''
    return list(uint2iter_expsLE(u))
def uint2iter_expsLE(u):
    return itertools.compress(itertools.count(), uint2iter_bitsLE(u))
def uint2bitsLE(u, min_len=None, bit_length=None):
    '''list bits in LSB first order

>>> uint2bitsLE(4)
[False, False, True]
>>> uint2bitsLE(4, 1)
[False, False, True]
>>> uint2bitsLE(4, 4)
[False, False, True, False]
'''
    return list(uint2iter_bitsLE(u, min_len, bit_length))
def uint2bitsBE(u, min_len=None, bit_length=None):
    '''list bits in MSB first order

>>> uint2bitsBE(4)
[True, False, False]
>>> uint2bitsBE(4, 1)
[True, False, False]
>>> uint2bitsBE(4, 4)
[False, True, False, False]
'''
    return list(uint2iter_bitsBE(u, min_len, bit_length))



















def uint8s2bitsBE(uint8s):
    '''big-endian per byte

>>> ls = list(uint8s2bitsBE([0x80, 0x01])) # [True, False..., True]
>>> len(ls) == 16
True
>>> ls[0] == ls[-1] == True
True
>>> not any(ls[1:-1])
True
'''
    for uint8 in uint8s:
        bits = uint8_to_bitsBE[uint8]
        yield from bits
def uint8s2bitsLE(uint8s):
    '''little-endian per byte

>>> ls = list(uint8s2bitsLE([0x01, 0x80])) # [True, False..., True]
>>> len(ls) == 16
True
>>> ls[0] == ls[-1] == True
True
>>> not any(ls[1:-1])
True
'''
    for uint8 in uint8s:
        bits = uint8_to_bitsLE[uint8]
        yield from bits



def reverse_uint8(u):
    '''reverse the bits of a 32-bit unsigned int

>>> reverse_uint8(1) == 1 << (8-1)
True
'''
    return uint8_to_reversed_uint8[u]
    return reverse_uint(8, u)

if 1: # reverse_bitorder_per_byte
    # bytes(uint8s) slower than b''.join(iter_bytes)!!!

    def reverse_bitorder_per_byte(data):
        r'''reverse_bitorder_per_byte(buffer)->bytes or bytearray # or buffer??

>>> reverse_bitorder_per_byte(b'\x80\xF0')
b'\x01\x0f'
'''
        return _ver3_reverse_bitorder_per_byte(data)
    def _ver1_reverse_bitorder_per_byte(data):
        data = memoryview_B1D(data)
        reverse = uint8_to_reversed_uint8
        return bytes(reverse[u] for u in data)
    def _ver2_reverse_bitorder_per_byte(data):
        # slower if not using reverse = uint8_to_reversed_byte!!
        # get nonlocal/global variable showing down...
        data = memoryview_B1D(data)
        reverse = uint8_to_reversed_byte
        return b''.join(reverse[u] for u in data)
    def _ver3_reverse_bitorder_per_byte(data):
        if not isinstance(data, (bytes, bytearray)):
            data = bytes(data)
        return data.translate(byte2reversed_byte_table)
    assert type(_ver3_reverse_bitorder_per_byte(bytearray(b'aafs'))) is bytearray


def std_data_bitorder(data, byte_MSB_first):
    'std_byte is with [byte_MSB_first==True]'
    if not byte_MSB_first:
        data = reverse_bitorder_per_byte(data)
    data = memoryview_B1D(data)
    return data


def reverse_bytes(bs):
    return bs[::-1]

def reverse_bytes_and_bits_per_byte(bs):
    bs = reverse_bitorder_per_byte(bs)
    return reverse_bytes(bs)














class _bitsXE2uint8_T:
    compress = staticmethod(itertools.compress)
##    reduce = staticmethod(functools.reduce)
##    or_ = staticmethod(operator.or_)
    _2powsLE = [1<<i for i in range(8)]
    _2powsBE = list(reversed(_2powsLE))

    def __init__(self, bitorder):
        self._2pows = self._2powsBE if bitorder == 'big' else self._2powsLE
    def __call__(self, bits):
        return sum(self.compress(self._2pows, bits))
        return self.reduce(self.or_, self.compress(self._2pows, bits), 0)
_bitsLE2uint8 = _bitsXE2uint8_T('little')
_bitsBE2uint8 = _bitsXE2uint8_T('big')



def bitseq8sBE2bytes(bitseq):
    r'''calc uint from bits in MSB first order; len(bits) == 8

>>> bitseq8sBE2bytes([False, False, False, False,   False, True, False, False])
b'\x04'
'''
    bs, pad_len = bitseqBE2bytes_padlen(bitseq)
    if pad_len:
        raise ValueError('len(bitseq) % 8 != 0')
    return bs

    if len(bitseq) & 7:
        raise ValueError('len(bitseq) % 8 != 0')
    to_uint8 = _bitsBE2uint8
    bs = bytes(to_uint8(bits) for bits in icut_seq_to(bitseq, 8))
    return bs


def bitseqBE2bytes_padlen(bitseq):
    r'''calc uint from bits in MSB first order; len(bits) == 8

>>> bitseqBE2bytes_padlen([False, False, True]) == (b'\x20', 5)
True
'''
    r = len(bitseq) & 7
    pad_len = 0 if not r else 8-r
    to_uint8 = _bitsBE2uint8
    bs = bytes(to_uint8(bits) for bits in icut_seq_to(bitseq, 8))
    return bs, pad_len




def bitseqBE2uint_padlen(bits):
    r'''calc uint from bits in MSB first order

>>> bitseqBE2uint_padlen([False, False, True])
(32, 5)
'''
    bs, pad_len = bitseqBE2bytes_padlen(bits)
    return int.from_bytes(bs, 'big'), pad_len

def bitseqBE2uint(bits):
    r'''calc uint from bits in MSB first order

>>> bitseqBE2uint([False, False, True])
1
'''
    u, pad_len = bitseqBE2uint_padlen(bits)
    return u >> pad_len


def bitsBE2bytes_padlen(bits):
    r'''calc uint from bits in MSB first order

>>> bitsBE2bytes_padlen(iter([False, False, True])) == (b'\x20', 5)
True
'''
    if isinstance(bits, Sequence):
        return bitseqBE2bytes_padlen(bits)
    ls = []
    pad_len = 0
    for bitseq in icut_to(bits, 8 << 20): # 1MB
        assert bitseq
        bs, pad_len = bitseqBE2bytes_padlen(bitseq)
        ls.append(bs)
    return b''.join(ls), pad_len



def bitsBE2uint_padlen(bits):
    r'''calc uint from bits in MSB first order

>>> bitsBE2uint_padlen(iter([False, False, True]))
(32, 5)
'''
    bs, pad_len = bitsBE2bytes_padlen(bits)
    return int.from_bytes(bs, 'big'), pad_len
def bitsBE2uint(bits):
    r'''calc uint from bits in MSB first order

>>> bitsBE2uint(iter([False, False, True]))
1
'''
    u, pad_len = bitsBE2uint_padlen(bits)
    return u >> pad_len












def bitseqLE2bytes(bitseq):
    r'''calc uint from bits in LSB first order

>>> bitseqLE2bytes([False, True, False, False])
b'\x02'
'''
    to_uint8 = _bitsLE2uint8
    bs = bytes(to_uint8(bits) for bits in icut_seq_to(bitseq, 8))
    return bs


def bitseqLE2uint(bits):
    r'''calc uint from bits in LSB first order

>>> bitseqLE2uint([False, True, False, False])
2
'''
    return int.from_bytes(bitseqLE2bytes(bits), 'little')


def bitsLE2bytes(bits):
    r'''calc uint from bits in LSB first order

>>> bitsLE2bytes(iter([False, True, False, False]))
b'\x02'
'''
    if isinstance(bits, Sequence):
        return bitseqLE2bytes(bits)
    ls = []
    for bitseq in icut_to(bits, 8 << 20): # 1MB
        ls.append(bitseqLE2bytes(bitseq))
    return b''.join(ls)

def bitsLE2uint(bits):
    r'''calc uint from bits in LSB first order

>>> bitsLE2uint(iter([False, True, False, False]))
2
'''
    return int.from_bytes(bitsLE2bytes(bits), 'little')

    ##### old version #######
    it = iter(bits)
    to_uint8 = _bitsLE2uint8
    islice = itertools.islice
    ls = bytearray()
    while True:
        bits = list(islice(it, 8))
        if not bits:
            break
        ls.append(to_uint8(bits))
    return int.from_bytes(ls, 'little')








def _reverse_uint_8x(bytesize, u):
##    u = to_uint(u, 'u')
##    size = to_uint(size, 'bytesize')
##    if (size<<3) < u.bit_length():
##        raise
    bs = reverse_bitorder_per_byte(u.to_bytes(bytesize, 'big'))
    return int.from_bytes(bs, 'little')

def _reverse_uint_not8x(bitsize, u):
    L = bitsize
    size = (L+7) >> 3 # (L+7)//8
    u = _reverse_uint_8x(size, u)

    pad_len = (size << 3) - L # size*8 - L
    #print(bs, u, pad_len)
    return u >> pad_len

def reverse_uint(bitsize, u):
    '''reverse the bits of a L-bit unsigned int

>>> reverse_uint(4, 1)
8
>>> reverse_uint(4, 1) == 1 << (4-1)
True
>>> reverse_uint(4, 0)
0
>>> reverse_uint(0, 0)
0
'''
    u = to_uint(u, 'u')
    L = to_uint(bitsize, 'bitsize')

    # 0 .bit_length() == 0
    if L < u.bit_length():
        raise ValueError('u.bit_length() > bitsize; u is not a {}-bit uint'
                         .format(L))
    if not L & 7: # L % 8 == 0
        return _reverse_uint_8x(L>>3, u)
    return _reverse_uint_not8x(L, u)


def reverse_uint32(u):
    '''reverse the bits of a 32-bit unsigned int

>>> reverse_uint32(1) == 1 << (32-1)
True
'''
    return reverse_uint(32, u)





def _t():
    import timeit
    bs = b'2343535' * 10000
    tests = [_ver1_reverse_bitorder_per_byte,
             _ver2_reverse_bitorder_per_byte,
             _ver3_reverse_bitorder_per_byte]
    fs = [(lambda *, f=f: f(bs)) for f in tests]
    N = 100
    ts = [timeit.timeit(f, number=N) for f in fs]
    try:
        t = ts
        assert t[0] > t[1] > t[2]
        #print('times:', ts)
        # times: [1.2314897851167614, 1.1803496367134678, 0.010453131956557282]
    except:
        print('times:', ts)
        raise

    # bytes(uint8s) slower than b''.join(iter_bytes) which slower than translate!!!

if 0:
    from sand import testmod
    testmod(__name__)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    _t()

