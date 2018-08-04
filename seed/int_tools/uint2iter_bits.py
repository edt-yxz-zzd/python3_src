
__all__ = '''
    uint2iter_bits
    uint2bytes

    uint2bit_length
    uint2byte_length
    '''.split()

from itertools import dropwhile, islice
from seed.math.floor_ceil import ceil_div
from seed.tiny import null_iter

def uint2bit_length(u):
    return u.bit_length()
def uint2byte_length(u):
    L = uint2bit_length(u)
    return ceil_div(L, 8)
def uint2bytes(is_big_endian, u, *, length=None):
    min_length = uint2byte_length(u)
    if length is None:
        length = min_length
    elif length < min_length:
        #mask = ~(1<<(8*length))
        #u &= mask
        #
        #bug:u %= 1 << (8*min_length)
        u %= 1 << (8*length)
    return u.to_bytes(length, byteorder='big' if is_big_endian else 'little')

byte_MSB = 1<<7
byte_LSB = 1<<0
byte_bits_from_LSB_to_MSB = [1<<i for i in range(8)]
byte_bits_from_MSB_to_LSB = list(reversed(byte_bits_from_LSB_to_MSB))
def bytes2iter_bits(is_big_endian, bs):
    masks = byte_bits_from_MSB_to_LSB if is_big_endian\
            else byte_bits_from_LSB_to_MSB
    f = iter if is_big_endian else reversed
    for byte in f(bs):
        for mask in masks:
            yield bool(byte&mask)
def uint2iter_bits(is_big_endian, u, *, length=None):
    if length is None:
        #length = u.bit_length()
        bs = uint2bytes(is_big_endian, u)
        if not bs: return null_iter
        #num_lead0s = 8 - bs[0].bit_length()
        it = bytes2iter_bits(is_big_endian, bs)
        return dropwhile(lambda b: not b, it)
    byte_length = ceil_div(length, 8)
    bs = uint2bytes(is_big_endian, u, length=byte_length)
    if not bs: return null_iter
    #num_lead0s = 8 - bs[0].bit_length()
    to_drop = byte_length*8 - length
    it = bytes2iter_bits(is_big_endian, bs)
    return islice(it, to_drop, None)

assert uint2bit_length(0) == 0
assert uint2bit_length(1) == 1
assert uint2bit_length(2) == 2
assert uint2bit_length(3) == 2
assert uint2bit_length(4) == 3

assert uint2byte_length(0) == 0
assert uint2byte_length(1) == 1
assert uint2bytes(True, 0, length=0) == b''
assert uint2bytes(True, 1, length=0) == b''
assert uint2bytes(True, 2, length=0) == b''
assert uint2bytes(True, 1, length=1) == b'\1'
assert uint2bytes(True, 2, length=1) == b'\2'
assert uint2bytes(True, 255, length=1) == b'\xFF'
assert uint2bytes(True, 255, length=2) == b'\x00\xFF'
#print(uint2bytes(True, 256, length=2))
assert uint2bytes(True, 256, length=2) == b'\x01\x00'
assert uint2bytes(True, 256, length=1) == b'\x00'


