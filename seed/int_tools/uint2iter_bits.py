r'''[[[
e ../../python3_src/seed/int_tools/uint2iter_bits.py

seed.int_tools.uint2iter_bits
py -m nn_ns.app.debug_cmd   seed.int_tools.uint2iter_bits -x
py -m nn_ns.app.doctest_cmd seed.int_tools.uint2iter_bits:__doc__ -ht #  -ff -v -df
]]]'''#'''
__all__ = '''
    uint2iter_bits
    uint2bytes

    uint2bit_length
    uint2byte_length


    '''.split()
    #bytes2iter_bits
    #
    #byte_MSB
    #byte_LSB
    #byte_bits_from_LSB_to_MSB
    #byte_bits_from_MSB_to_LSB

___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from itertools import dropwhile, islice
    from seed.tiny_.containers import get_null_iter_#null_iter
    from seed.math.floor_ceil_tools.fc_div import ceil_div
___end_mark_of_excluded_global_names__0___ = ...


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
        if not bs: return get_null_iter_()
        #num_lead0s = 8 - bs[0].bit_length()
        it = bytes2iter_bits(is_big_endian, bs)
        return dropwhile(lambda b: not b, it)
    byte_length = ceil_div(length, 8)
    bs = uint2bytes(is_big_endian, u, length=byte_length)
    if not bs: return get_null_iter_()
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


from seed.int_tools.uint2iter_bits import uint2iter_bits, uint2bytes
from seed.int_tools.uint2iter_bits import *
