
import io, os
from ..UintBytesCodec import bigEndianUintBytesCodec
from ..uint8_to_byte import uint8_to_byte, byte_to_uint8
from sand import DecodeError, EncodeError

from .cases import *




def _which_uint_case(uint8_from_first_byte):
    u = uint8_from_first_byte
    assert 0 <= u < 1 << 8
    
    if not (u & (1 << 7)):
        # 0...
        return TINY_CASE

    # 1...
    if u & (1 << 6):
        # 11...
        return SMALL_CASE

    # 10...
    if not (u & (1 << 5)):
        # 100...
        return LARGE_CASE

    # 101...
    if not (u & (1 << 4)):
        # 1010...
        return HUGE_OR_RESERVED_CASE

    # 1011...
    return USER_CASE


# map uint4 to uint case
# where uint4 is the high half of uint8 from first byte
_uint4_to_uint_case = [_which_uint_case(i << 4) for i in range(1 << 4)]

def which_uint_case(uint8_from_first_byte):
    uint8 = uint8_from_first_byte
    assert 0 <= uint8 < 0x100
    
    uint4 = uint8 >> 4
    case = _uint4_to_uint_case[uint4]
    if case == HUGE_OR_RESERVED_CASE:
        case = HUGE_CASE if uint8 & 0x0f == 0 else RESERVED_CASE
    return case

def _which_uint_case__by_hand(uint8_from_first_byte):
    u = uint8_from_first_byte
    assert 0 <= u < 0x100
    if u <= 0b01111111:
        return TINY_CASE
    if u >= 0b11000000:
        return SMALL_CASE
    if u >= 0b10110000:
        return USER_CASE
    if u > 0b10100000:
        return RESERVED_CASE
    if u == 0b10100000:
        return HUGE_CASE
    return LARGE_CASE

def test_which_uint_case():
    for u in range(0x100):
        try:
            assert which_uint_case(u) == _which_uint_case__by_hand(u)
        except:
            print(u)
            print(which_uint_case(u), _which_uint_case__by_hand(u))
            raise

test_which_uint_case()


