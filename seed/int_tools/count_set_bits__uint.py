
r'''
py -m nn_ns.app.debug_cmd    seed.int_tools.count_set_bits__uint
py -m seed.int_tools.count_set_bits__uint
from seed.int_tools.count_set_bits__uint import tabulate4count_set_bits__uint__Brian_Kernighan_Algorithm, itabulate4count_set_bits__uint__Brian_Kernighan_Algorithm
from seed.int_tools.count_set_bits__uint import  count_set_bits__uint__Brian_Kernighan_Algorithm, count_set_bits__uint__via_binary_repr, count_set_bits__uint__via_hex_repr, count_set_bits__uint__via_bytes_repr

e ../../python3_src/seed/int_tools/count_set_bits__uint.py

[[
how to count 1 bits of integer
https://www.geeksforgeeks.org/count-set-bits-in-an-integer/
Brian Kernighan’s Algorithm
  (n & (n-1)), we unset the rightmost set bit. If we do n & (n-1) in a loop and count the number of times the loop executes, we get the set bit count.

]]


>>> verify_ = lambda f,/:all(f(u)==num_set_bits for u, num_set_bits in enumerate(uint8_to_num_set_bits))
>>> verify_(count_set_bits__uint__Brian_Kernighan_Algorithm)
True
>>> verify_(count_set_bits__uint__via_binary_repr)
True
>>> verify_(count_set_bits__uint__via_hex_repr)
True
>>> verify_(count_set_bits__uint__via_bytes_repr)
True

#'''

__all__ = '''
    tabulate4count_set_bits__uint__Brian_Kernighan_Algorithm
        itabulate4count_set_bits__uint__Brian_Kernighan_Algorithm

    count_set_bits__uint__Brian_Kernighan_Algorithm
    count_set_bits__uint__via_binary_repr
    count_set_bits__uint__via_hex_repr
        mk_hex2num_set_bits
            hex2num_set_bits
    count_set_bits__uint__via_bytes_repr
        mk_uint8_to_num_set_bits
            uint8_to_num_set_bits

    '''.split()


from seed.tiny import check_uint, MapView
from seed.int_tools.int_tools import uint2bytes__littleendian

def itabulate4count_set_bits__uint__Brian_Kernighan_Algorithm(may_uint2num_set_bits, uint_lt, /):
    if may_uint2num_set_bits is None:
        uint2num_set_bits = []
    else:
        uint2num_set_bits = may_uint2num_set_bits
    tabulate4count_set_bits__uint__Brian_Kernighan_Algorithm(uint2num_set_bits, uint_lt)
    return uint2num_set_bits
def tabulate4count_set_bits__uint__Brian_Kernighan_Algorithm(uint2num_set_bits, uint_lt, /):
    check_uint(uint_lt)
    if len(uint2num_set_bits) == 0 < uint_lt:
        uint2num_set_bits.append(0)

    for u in range(len(uint2num_set_bits), uint_lt):
        u &= u-1
        num_set_bits = 1+uint2num_set_bits[u]
        uint2num_set_bits.append(num_set_bits)
    assert len(uint2num_set_bits) >= uint_lt
    return

def count_set_bits__uint__Brian_Kernighan_Algorithm(u, /):
    check_uint(u)
    num_set_bits = 0
    while u:
        num_set_bits += 1
        u &= u-1

    return num_set_bits

def count_set_bits__uint__via_binary_repr(u, /):
    check_uint(u)
    num_set_bits = bin(u).count('1')
    return num_set_bits

def mk_uint8_to_num_set_bits():
    uint2num_set_bits = bytearray()
    uint_lt = (1<<8)
    tabulate4count_set_bits__uint__Brian_Kernighan_Algorithm(uint2num_set_bits, uint_lt)
    uint8_to_num_set_bits = bytes(uint2num_set_bits)
    return uint8_to_num_set_bits
uint8_to_num_set_bits = mk_uint8_to_num_set_bits()
def mk_hex2num_set_bits():
    hex2num_set_bits = MapView({hex(u)[-1]: count_set_bits__uint__via_binary_repr(u) for u in range(16)})
    return hex2num_set_bits
hex2num_set_bits = mk_hex2num_set_bits()

def count_set_bits__uint__via_hex_repr(u, /, *, may_hex2num_set_bits=None):
    check_uint(u)
    _hex2num_set_bits = hex2num_set_bits if may_hex2num_set_bits is None else may_hex2num_set_bits
    num_set_bits = sum(map(_hex2num_set_bits.__getitem__, hex(u)[2:]))
    return num_set_bits
def count_set_bits__uint__via_bytes_repr(u, /, *, may_uint8_to_num_set_bits=None):
    check_uint(u)
    _uint8_to_num_set_bits = uint8_to_num_set_bits if may_uint8_to_num_set_bits is None else may_uint8_to_num_set_bits
    num_set_bits = sum(map(_uint8_to_num_set_bits.__getitem__, uint2bytes__littleendian(u)))
    return num_set_bits





if __name__ == "__main__":
    import doctest
    doctest.testmod()


