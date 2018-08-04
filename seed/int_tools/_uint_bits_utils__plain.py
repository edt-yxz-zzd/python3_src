
'''
slow version for initialization at setup stage
'''

__all__ = '''
    uint8_to_bitsBE
    uint8_to_bitsLE
    byte_MSB_first_to_uint8XE2uint8BE
    uint8_to_reversed_uint8
    uint8_to_reversed_byte
    byte2reversed_byte_table
'''
from seed.helper.check_utils import to_uint, to_pint

def uint2expsLE(u):
    '''list exps in LSB first order

>>> uint2expsLE(5)
[0, 2]
'''
    u = to_uint(u, 'u')
    ls = []
    exp = 0
    while u:
        if u & 1:
            ls.append(exp)
        exp += 1
        u >>= 1
    return ls

def uint2bitsLE(i, min_len=None):
    '''list bits in LSB first order

>>> uint2bitsLE(4)
[False, False, True]
>>> uint2bitsLE(4, 1)
[False, False, True]
>>> uint2bitsLE(4, 4)
[False, False, True, False]
'''
    bits = uint2bitsBE(i, min_len)
    bits.reverse()
    return bits


def uint2bitsBE(u, min_len=None):
    '''list bits in MSB first order

>>> uint2bitsBE(4)
[True, False, False]
>>> uint2bitsBE(4, 1)
[True, False, False]
>>> uint2bitsBE(4, 4)
[False, True, False, False]
'''
    'big-endian'
    i = to_uint(u, 'u')
    s = bin(i)[2:]
    bits = [ch == '1' for ch in s]
    if not bits[0]:
        assert i == 0
        bits.pop()
        if bits:
            raise logic-error

    assert not bits or bits[0]
    if min_len is not None:
        bits = [False]*(min_len - len(bits)) + bits
        assert len(bits) >= min_len
    return bits


def bitsBE2uint(bits):
    '''calc uint from bits in MSB first order

>>> bitsBE2uint([False, True, False, False])
4
'''
    u = 0
    for bit in bits:
        u <<= 1
        if bit:
            u |= 1
    return u



def reverse_uint(L, u):
    '''reverse the bits of a L-bit unsigned int

>>> reverse_uint(4, 1)
8
>>> reverse_uint(4, 1) == 1 << (4-1)
True
'''
    bits = uint2bitsLE(u, L)
    if not len(bits) == L:
        assert u.bit_length() > L
        raise ValueError('u.bit_length() > L; u is not uint<{}>'.format(L))
    return bitsBE2uint(bits)


uint8_to_bitsBE = tuple(tuple(uint2bitsBE(u, 8)) for u in range(0x100))
uint8_to_bitsLE = tuple(tuple(uint2bitsLE(u, 8)) for u in range(0x100))


byte_MSB_first_to_uint8XE2uint8BE = (
    tuple(reverse_uint(8, u) for u in range(0x100)), # LE2BE
    tuple(range(0x100)) # BE2BE
    )

uint8_to_reversed_uint8 = byte_MSB_first_to_uint8XE2uint8BE[False]
assert uint8_to_reversed_uint8[1] == 0x80
uint8_to_reversed_byte = tuple(bytes([u]) for u in uint8_to_reversed_uint8)

byte2reversed_byte_table = bytes.maketrans(bytes(range(0x100)), bytes(uint8_to_reversed_uint8))
assert type(byte2reversed_byte_table) is bytes
assert len(byte2reversed_byte_table) == 0x100


if __name__ == "__main__":
    import doctest
    doctest.testmod()
