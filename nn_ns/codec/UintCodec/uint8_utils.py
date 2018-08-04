
'''
bits in byte:
    when iterate bits in big-endian bytes:
        msb first!
        for u in bytes:
            yield from uint2bits__big_endian(u, 8)
    when index bit in byte:
        lsb first!
        the ith bit of byte is bool((u>>i) & 1)


byte:
    iter from left/msb/7th to right/lsb/0th
    msb                                lsb
    7th  6th  5th  4th  3th  2nd  1st  0th
     0    0    1    0    0    0    0    1    == b'\x21'







'''

assert int.from_bytes(b'\x01\x02', 'big') == int.from_bytes(b'\x02\x01', 'little')


NUM_BITS_PER_BYTE = 8


def floor_div(dividend, divisor):
    '''floor(a/b) for [INT a,b]'''
    return dividend // divisor

def ceil_div(dividend, divisor):
    '''ceil(a/b) for [INT a,b]

a // b ::= floor(a/b)
ceil(-a) == -floor(a)

if b > 0:
    ceil(a/b) = (a+(b-1)) // b
if b < 0:
    ceil(a/b) = ceil(- (a/-b)) = -floor(a/-b) = -(a//-b)
'''
    if divisor > 0:
        return (dividend + (divisor-1)) // divisor
    else:
        return -(dividend // -divisor)


def num_bits2num_bytes(num_bits):
    return ceil_div(num_bits, NUM_BITS_PER_BYTE)
    
def uint2bits__plain__little_endian(u, size):
    'list<bool>'
    bits = []
    for _ in range(size):
        bits.append(bool(u & 1))
        u >>= 1
    return bits

def uint2bits__little_endian(u, size):
    if u < 256:
        return uint2bits__plain__little_endian(u, size)
    u.to_bytes()




def uint2bits__big_endian(u, size):
    bits = uint2bits__little_endian(u, size)
    bits.reverse()
    return bits

def uint2bits(u, size, bitorder):
    if bitorder == 'big':
        uint2bits = uint2bits__big_endian
    elif bitorder == 'little':
        uint2bits = uint2bits__little_endian
    else:
        raise UnknownCaseError
    return uint2bits(u, size)
