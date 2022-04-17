r'''
seed.int_tools.int_tools
from seed.int_tools.int_tools import divs, is_even, is_odd, even, odd
from seed.int_tools.int_tools import bit_length_of, byte_length_of, align_length, unit_length2block_length, bit_length2byte_length, uint2bytes_


#'''


__all__ = '''
    divs
    is_even
    is_odd

    even
    odd

    bit_length_of
    byte_length_of
    align_length
    unit_length2block_length
    bit_length2byte_length
    uint2bytes_

    '''.split()


from seed.math.divs import divs, is_odd, is_even, odd, even





def bit_length_of(i, /):
    return i.bit_length()
def byte_length_of(i, /):
    return bit_length2byte_length(i.bit_length())

def align_length(alignment, min_length, /):
    aligned_length = alignment * unit_length2block_length(alignment, min_length)
    assert aligned_length % alignment == 0
    assert aligned_length - alignment < min_length <= aligned_length
    return aligned_length
def unit_length2block_length(num_units_per_block, unit_length, /):
    q, r = divmod(unit_length, num_units_per_block)
    block_length = q + bool(r)
    assert (unit_length==0 and block_length==0) or (unit_length > 0 and block_length > 0 and (block_length-1)*num_units_per_block < unit_length <= block_length*num_units_per_block)
    return block_length
def bit_length2byte_length(bit_length, /, *, num_bits_per_byte=8):
    r'''
    [i.bit_length() == abs(i).bit_length()]
    [0.bit_length() == 0]
    [1.bit_length() == 1]
    [2.bit_length() == 2]
    [3.bit_length() == 2]
    [4.bit_length() == 3]
    [[p > 0][n == p.bit_length()] -->> [n > 0][2**(k-1) <= p < 2**k]]
    ==>> d=efine byte_length mimic bit_length
    scenarios:
        x.to_bytes((x.bit_length() + 7) // 8, byteorder='little')
        <==> x.to_bytes(bit_length2byte_length(x.bit_length()), byteorder='little')
        <==> x.to_bytes(byte_length_of(x), byteorder='little')
        ######################
        to exploit py::base64.b64encode to product radix<64>-digits, we pad/align bytes:
            #64 == 2**6
            #6*4 == 8*3
            #alignment == 3
            #byteorder MUST BE 'big'
            #   since b64encode concat bits inter-neighbor-byte as-if bigendian
            x.to_bytes(align_length(3, byte_length_of(x)), byteorder='big')


    #'''
    #size = (L+7) >> 3 # (L+7)//8
    #size = bool(L&7) + (L >> 3) # (L+7)//8
    return unit_length2block_length(num_bits_per_byte, bit_length)

def uint2bytes_(u, /, *, byteorder, alignment):
    return u.to_bytes(align_length(alignment, byte_length_of(u)), byteorder=byteorder)
        #why uint?
        #   since to_bytes(..., signed=False) ==>> OverflowError if [u < 0]
    return u.to_bytes(byte_length_of(u), byteorder=byteorder)
