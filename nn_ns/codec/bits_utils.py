
'''
seq is a sequence, random-access
iseq/iter_seq is a iterable # i.e. iter_bits, iter_vbytes

bytes = seq/iseq of uint8 # may not be a python::bytes, i.e. list<uint8>
byte is bytes of len 1

vbyte is the value of a byte that is a uint8
vbytes = seq/iseq of vbyte == bytes

bits = seq of 0 or 1
    # default to big-endian
rbits = seq of 0 or 1, little-endian


B = [01]

padded_bits = payload_bits = data_bits + pad
pad = 10{0,6} | (?<!10{0,6})''



'''

__all__ = '''
    iter_vbytes2iter_bits
    iter_bits2iter_vbytes
    
'''.replace(',', ' ').split()
#print(__all__)
#from .. import take_ex

import itertools
from collections import deque
from itertools import chain, islice, compress
from sand import icut_to, drop, head_ex
from sand.codec.UintCodec.UintBytesCodec import bigEndianUintBytesCodec



class LenError(ValueError):pass

NUM_BITS_PER_BYTE = 8
VBYTE_MIN = 0
VBYTE_INF = 2**NUM_BITS_PER_BYTE # vbyte < VBYTE_INF
VBYTE_MAX = VBYTE_INF -1 # vbyte <= VBYTE_MAX
VBYTE_MASK = VBYTE_INF -1 # 1{NUM_BITS_PER_BYTE}


VBYTE_MASKBITS__LITTLE_ENDIAN = tuple(2**i for i in range(NUM_BITS_PER_BYTE))
VBYTE_MASKBITS__BIG_ENDIAN = tuple(reversed(VBYTE_MASKBITS__LITTLE_ENDIAN))
VBYTE_IDX_MASKBITS = VBYTE_MASKBITS__LITTLE_ENDIAN
VBYTE_ITER_MASKBITS = VBYTE_MASKBITS__BIG_ENDIAN

VBYTE_BIT_H0, VBYTE_BIT_H1, VBYTE_BIT_H2 = VBYTE_MASKBITS__BIG_ENDIAN[:3]
BitType = int
VByteType = int

NUM_BITS_FOR_BIT_IDX_IN_BYTE = 3
MASK_FOR_BIT_IDX_IN_BYTE = (1<<NUM_BITS_FOR_BIT_IDX_IN_BYTE) - 1 # 7


def is_bit(x):
    return type(x) is BitType and 0 <= x < 2
def is_vbyte(x):
    return type(x) is VByteType and VBYTE_MIN <= x < VBYTE_INF




########################## vbyte ####################

def vbyte2iter_rbits(vbyte):
    return vbyte2iter_bits(vbyte, VBYTE_IDX_MASKBITS)
def vbyte2iter_bits(vbyte, weights=VBYTE_ITER_MASKBITS):
    assert is_vbyte(vbyte)
    for i in weights:
        yield int(bool(vbyte & i))
    return
def iter_rbits2vbyte(bits, EmptyError=None):
    return iter_bits2vbyte(bits, EmptyError, VBYTE_IDX_MASKBITS)
def iter_bits2vbyte(bits, EmptyError=None, weights = VBYTE_ITER_MASKBITS):
    bits = slice_le(bits, NUM_BITS_PER_BYTE+1)
    if len(bits) != NUM_BITS_PER_BYTE:
        if not bits and EmptyError is not None:
            raise EmptyError
        raise LenError('len(bits) == {} != NUM_BITS_PER_BYTE'.format(len(bits)))
    
    #vbyte = int(bits2bin_str(bits), 2)
    vbyte = sum(compress(weights, bits))
    return vbyte




########################## vbytes ####################

def iter_vbytes2iter_bits(vbytes):
    for u in vbytes:
        yield from vbyte2iter_bits(u)
    return



def iter_bits2iter_vbytes_ex(bits,
                             weights = VBYTE_ITER_MASKBITS,
                             container=None,
                             incomplete_tailbits_handler=None):
    '''

incomplete_tailbits_handler(bits, weights)
    assert 0 < len(bits) < NUM_BITS_PER_BYTE
    return the last vbyte or
    raise StopIteration to discared incomplete_tailbits or
    raise other Exception to indicate error

example:
    def incomplete_tailbits_handler__padding_bits(bits, weights):
        # nonlocal padding_bits where len(padding_bits) == 7
        bits = list(bits)
        bits.extend(padding_bits[:NUM_BITS_PER_BYTE-len(bits)])
        assert len(bits) == NUM_BITS_PER_BYTE
        return iter_bits2vbyte(bits, weights)
    def incomplete_tailbits_handler__discard(bits, weights):
        # discard bits
        raise StopIteration
    def incomplete_tailbits_handler__error(bits, weights):
        # error # default
        raise LenError('len(bits) % NUM_BITS_PER_BYTE != 0')
    class IncompleteTailbitsHandler__Save:
        def __init__(self, padding_bits=(0,)*(NUM_BITS_PER_BYTE-1)):
            self.incomplete_tailbits = None
            self.weights = None
            self.padding_bits = padding_bits
            if len(padding_bits) != NUM_BITS_PER_BYTE-1:
                raise LenError('len(padding_bits) != NUM_BITS_PER_BYTE-1')
        def __call__(self, bits, weights):
            # save incomplete_tailbits
            self.incomplete_tailbits = bits
            self.weights = weights

            
            full_bits = list(bits)
            full_bits.extend(self.padding_bits[:NUM_BITS_PER_BYTE-len(bits)])
            assert len(full_bits) == NUM_BITS_PER_BYTE
            return iter_bits2vbyte(full_bits, weights)
'''
    for bits in icut_to(bits, NUM_BITS_PER_BYTE, container):
        if len(bits) < NUM_BITS_PER_BYTE:
            assert len(bits)
            if incomplete_tailbits_handler is None:
                raise LenError('len(bits) % NUM_BITS_PER_BYTE != 0')
            yield incomplete_tailbits_handler(bits, weights)
            break
        yield iter_bits2vbyte(bits, weights)
def iter_bits2iter_vbytes(bits, padding_bits = None, weights = VBYTE_ITER_MASKBITS):
    assert padding_bits is None or len(padding_bits) == 7
    if padding_bits is None:
        incomplete_tailbits_handler = None
    elif len(padding_bits) != 7:
        raise ValueError('len(padding_bits) != 7')
    else:
        def incomplete_tailbits_handler(bits, weights):
            bits = list(bits)
            bits.extend(padding_bits[:NUM_BITS_PER_BYTE-len(bits)])
            assert len(bits) == NUM_BITS_PER_BYTE
            return iter_bits2vbyte(bits, weights)
            
    return iter_bits2iter_vbytes_ex(bits, weights, tuple, incomplete_tailbits_handler)



    
def slice_le(iterable, n):
    return tuple(itertools.islice(iterable, n))





########################## bin_str ####################
def iter_bin_str2iter_bits(bin_str):
    'bin_str = rex"[01]*"'
    return (int(ch == '1') for ch in bin_str)
def iter_bits2iter_bin_str(bits):
    return map(str, bits)
def iter_bits2bin_str(bits):
    return ''.join(bits2iter_bin_str(bits))




########################## uint #####################

def uint2iter_bits(u):
    L = u.bit_length()
    bs = bigEndianUintBytesCodec.uint2bytes(u)

    
    bits_with_leading_0s = iter_vbytes2iter_bits(bs)
    len_of_leading_0s = NUM_BITS_PER_BYTE*len(bs) - L
    iter_bits = drop(len_of_leading_0s, bits_with_leading_0s)
    return iter_bits

class _IncompleteTailbitsHandler__Save:
    '''to save called args and make the last byte

    if self.incomplete_tailbits is None:
        ==>> not be called
'''
    
    def __init__(self, padding_bits=(0,)*(NUM_BITS_PER_BYTE-1)):
        self.incomplete_tailbits = None
        self.weights = None
        self.padding_bits = padding_bits
        if len(padding_bits) != NUM_BITS_PER_BYTE-1:
            raise LenError('len(padding_bits) != NUM_BITS_PER_BYTE-1')
    def __call__(self, bits, weights):
        # save incomplete_tailbits
        self.incomplete_tailbits = bits
        self.weights = weights

        
        full_bits = list(bits)
        full_bits.extend(self.padding_bits[:NUM_BITS_PER_BYTE-len(bits)])
        assert len(full_bits) == NUM_BITS_PER_BYTE
        return iter_bits2vbyte(full_bits, weights)
def iter_bits2uint(bits):
    handler = _IncompleteTailbitsHandler__Save()
    bs_with_padding_0s = iter_bits2iter_vbytes_ex(bits, VBYTE_ITER_MASKBITS,
                                                  None, handler)

    u_with_padding_0s = bigEndianUintBytesCodec.bytes2uint(bytes(bs_with_padding_0s))
    tailbits = handler.incomplete_tailbits
    if tailbits is not None:
        #print(tailbits)
        assert 0 < len(tailbits) < NUM_BITS_PER_BYTE
        len_of_padding_0s = NUM_BITS_PER_BYTE - len(tailbits)
    else:
        len_of_padding_0s = 0

    u = u_with_padding_0s >> len_of_padding_0s
    return u


def test_uint2iter_bits():
    for u in range(1000):
        try:
            assert iter_bits2uint(uint2iter_bits(u)) == u
        except:
            print(u, bin(u))
            bits = list(uint2iter_bits(u))
            print(bits)
            u_ = iter_bits2uint(bits)
            print(u_, bin(u_))
            raise

def pint2iter_omit_leading1_bits(pint):
    if not pint > 0:
        raise ValueError('not pint > 0')
    head, tail = head_ex(uint2iter_bits(pint))
    assert head == 1
    return tail

def iter_omit_leading1_bits2pint(omit_leading1_bits):
    bits = chain((1,), omit_leading1_bits)
    return iter_bits2uint(bits)


def test_pint2iter_omit_leading1_bits():
    d = iter_omit_leading1_bits2pint
    e = pint2iter_omit_leading1_bits
    for u in range(1, 1000):
        try:
            assert d(e(u)) == u
        except:
            print(u, bin(u))
            bits = list(e(u))
            print(bits)
            u_ = d(bits)
            print(u_, bin(u_))
            raise

test_uint2iter_bits()
test_pint2iter_omit_leading1_bits()






if __name__ == '__main__':
    from __main__ import *

    
