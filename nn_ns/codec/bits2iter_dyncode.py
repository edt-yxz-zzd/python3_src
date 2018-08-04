
'''
bytes = seq of uint8
bits = seq of 0 or 1

# iseq is a iterable
# dyncode is a seq of uint8
# iter_dyncode is a iseq of uint8

dyncode = Single | Combine   
Combine = Start Middle* End
Single = 00B{6}
Start  = 011B{5}
Middle = 1B{7}
End    = 010B{5}
B = [01]

bit_len of payload of dyncode = 6 | 5 + 7x + 5 // easy to reverse bits
padded_bits = payload_bits = data_bits + pad
pad = 10{0,6} | (?<!10{0,6})''


encode : uint | int | bits | bytes
bits:
    L = len(data_bits)
    min_x = lambda L: 0 if L <= 10 else (L-10 + 7-1)//7
    min_L = lambda L: 10+7*min_x(L)
    if L == 6 or L == 10+7x:
        tail = data_bits[-7:]
        if tail == '0' * len(tail):
            # padded_bits = data_bits
            len_padded_bits = L
        else:
            len_padded_bits = min_L(L+1)
    else:
        len_padded_bits = 6 if L < 6 else min_L(L)
    len_pad = len_padded_bits - L
    pad = '1' + '0'*(len_pad-1) if len_pad else ''
    padded_bits = data_bits + pad


possible1:
    pint2bits: #positive_int2bits
        p = 1B* ==>> B*
        bits = reversed(bin(p)[3:]) # so, sign of int2bits will be the first bit
        1: ''
        2: '0'
        3: '1'
        4: '00'
        5: '10'
        6: '01'
    uint2bits:
        p = u+1
        bits = pint2bits(p)
        0: ''
        1: '0'
        2: '1'
        3: '00'
        4: '10'
        5: '01'
    int2bits:
        u = abs(i)*2 - int(i<0)
        bits = uint2bits(u)
        +0: ''
        -1: '0'
        +1: '1'
        -2: '00'
        +2: '10'
        -3: '01'

    good:
        reuse bits2iter_padded_bits
    bad:
        uint2bits: 0:'' ==>> '00' + '100000' : not all 0
possible2:
    s.t.: 0 ==>> '0'*8
    uint2bits: pad leading 0s instead of default padding
    

'''

__all__ = '''
    uint2iter_padded_bits
    padded_bits2uint
    uint2dyncode
    dyncode2uint
    first_byte_in_dyncode_of_int_to_sign
    
    dyncode2iter_bits
    first_dyncode2iter_bits
    bits2iter_dyncode
    first_dyncode2iter_padded_bits
    padded_bits2iter_dyncode
    bytes2iter_dyncodes
    
    bytes2iter_bits
    bits2iter_bytes
    bits2iter_bytes_zfill
    
    is_dyncode_single, is_dyncode_start, is_dyncode_end, is_dyncode_middle
    encode_dyncode_single, encode_dyncode_start,
    encode_dyncode_end, encode_dyncode_middle
    dyncode_single2iter_bits, dyncode_start2iter_bits,
    dyncode_end2iter_bits, dyncode_middle2iter_bits
'''.replace(',', ' ').split()
#print(__all__)
#from .. import take_ex

import itertools
from collections import deque
from itertools import chain, islice, compress

NUM_BITS_OF_BYTE = 8
BYTE_LIM = 2**NUM_BITS_OF_BYTE
BYTE_MASK = BYTE_LIM -1
BYTE_RBITS = tuple(2**i for i in range(NUM_BITS_OF_BYTE))
BYTE_BITS = tuple(reversed(BYTE_RBITS))
# IS_MIDDLE, IS_MULTI,    IS_START
BYTE_BIT_H0, BYTE_BIT_H1, BYTE_BIT_H2 = BYTE_BITS[:3]

DYNCODE_SINGLE_PAYLOAD_LEN = 6
DYNCODE_START_PAYLOAD_LEN = 5
DYNCODE_END_PAYLOAD_LEN = 5
DYNCODE_MIDDLE_PAYLOAD_LEN = 7

DYNCODE_SINGLE_PAYLOAD_MASK = BYTE_BIT_H1 -1
DYNCODE_START_PAYLOAD_MASK = BYTE_BIT_H2 -1
DYNCODE_END_PAYLOAD_MASK = BYTE_BIT_H2 -1
DYNCODE_MIDDLE_PAYLOAD_MASK = BYTE_BIT_H0 -1

DYNCODE_SINGLE_FLAG = 0
DYNCODE_START_FLAG = BYTE_BIT_H1 | BYTE_BIT_H2
DYNCODE_END_FLAG = BYTE_BIT_H1
DYNCODE_MIDDLE_FLAG = BYTE_BIT_H0
dyncode_flag_fmt = 'DYNCODE_{}_FLAG'
dyncode_payloadmask_fmt = 'DYNCODE_{}_PAYLOAD_MASK'
dyncode_payloadlen_fmt = 'DYNCODE_{}_PAYLOAD_LEN'


    


class LenError(ValueError):pass
class NotDyncodeError(ValueError):pass
class NotDyncode_EmptyError(NotDyncodeError):pass


def is_uint8(x):
    return type(x) is int and 0 <= x < BYTE_LIM
def byte2iter_rbits(uint8):
    return byte2iter_bits(uint8, BYTE_RBITS)
def byte2iter_bits(uint8, bits=BYTE_BITS):
    assert is_uint8(uint8)
    for i in bits:
        yield int(bool(uint8 & i))
    return
def rbits2byte(bits, EmptyError=None):
    return bits2byte(bits, EmptyError, BYTE_RBITS)
def bits2byte(bits, EmptyError=None, weights = BYTE_BITS):
    bits = slice_le(bits, NUM_BITS_OF_BYTE+1)
    if len(bits) != NUM_BITS_OF_BYTE:
        if not bits and EmptyError is not None:
            raise EmptyError
        raise LenError('len(bits) == {} != NUM_BITS_OF_BYTE'.format(len(bits)))
    
    #uint8 = int(bits2bin_str(bits), 2)
    uint8 = sum(compress(weights, bits))
    return uint8
def bytes2iter_bits(uint8s):
    for u in uint8s:
        yield from byte2iter_bits(u)
    return

def bits2iter_bytes(bits):
    it = iter(bits)
    islice = itertools.islice
    while True:
        bits_ = islice(it, NUM_BITS_OF_BYTE)
        yield bits2byte(bits_, StopIteration)

    return
def bits2iter_bytes_zfill(uint8s, fill=0):
    for bits in bits2iter_bitss_zfill(uint8s, NUM_BITS_OF_BYTE, fill):
        # 'little-endian'
        yield rbits2byte(bits)
def bits2iter_bitss_zfill(uint8s, length, fill=0):
    'fill == None ==>> raise if error'
    if length < 1:
        raise ValueError('length < 1')
    it = iter(uint8s)
    while True:
        bits = slice_le(it, length)
        if len(bits) != length:
            break
        yield bits
    assert len(bits) < length
    if bits:
        if fill is None:
            raise LenError('length not divide len(bits)')
        bits += (0,)*(length - len(bits))
        assert len(bits) == length
        yield bits
    return



_min_x = lambda L: 0 if L <= 10 else (L-10 + 7-1)//7
_min_575_L = lambda L: 10+7*_min_x(L)
def bits_len2min_padded_len(L):
    return 6 if L <= 6 else _min_575_L(L)
    
def slice_le(iterable, n):
    return tuple(itertools.islice(iterable, n))
    return first_le_n

def bits2iter_dyncode(bits):
    # yield seq of uint8
    padded_bits = bits2iter_padded_bits(bits)
    return padded_bits2iter_dyncode(padded_bits)
def padded_bits2iter_dyncode(padded_bits):
    it = iter(padded_bits)
    le_7 = slice_le(it, 7)
    L = len(le_7)
    if L < 7:
        if L == 6:
            return padded_bits2iter_dyncode__eq6(le_7)
        assert L < 6
        raise LenError('len(padded_bits) < 6')
    return padded_bits2iter_dyncode__gt6(itertools.chain(le_7, it))
def padded_bits2iter_dyncode__eq6(bits):
    # [00B{6}]
    yield encode_dyncode_single(tuple(bits))
    return


def padded_bits2iter_dyncode__gt6(bits):
    it = padded_bits2iter_bitchunks__gt6(bits)
    start = next(it)
    yield encode_dyncode_start(start)

    mid = ()
    for mid in it:
        if len(mid) != 7:
            break
        yield encode_dyncode_middle(mid)

    end = mid
    if len(end) != 5:
        raise logic-error
    yield encode_dyncode_end(end)




def padded_bits2iter_bitchunks__gt6(bits):
    it = iter(bits)
    
    start = slice_le(it, 5)
    if len(start) != 5:
        raise LenError('length is not 5+7x+5: len(START)=={} != 5'.format(len(start)))
    yield start

    while True:
        le_7 = slice_le(it, 7)
        if len(le_7) != 7:
            end = le_7
            break
        yield le_7

    
    if len(end) != 5:
        raise LenError('length is not 5+7x+5: len(END)=={} != 5'.format(len(end)))
    yield end
    
    

def bits2iter_padded_bits(bits):
    d = deque([], 7)
    i = -1
    for i, b in enumerate(bits):
        yield b
        d.append(b)
    i += 1
    assert i >= 0
    ###########

    L = i           # L = len(data_bits)
    tail = tuple(d) # tail = data_bits[-7:]
    min_L = _min_575_L
    if L == 6 or L == min_L(L):
        if not any(tail):
            # padded_bits = data_bits
            len_padded_bits = L
        else:
            len_padded_bits = min_L(L+1)
    else:
        len_padded_bits = 6 if L < 6 else min_L(L)
    len_pad = len_padded_bits - L
    
    pad = [1] + [0]*(len_pad-1) if len_pad else []
    yield from pad
    return


    
    

__names = 'SINGLE START END MIDDLE'.split()
def _get_global_values(name, fmts):
    return [globals()[fmt.format(name)] for fmt in fmts]
def __check_payloadmask():
    fmts = dyncode_payloadlen_fmt, dyncode_payloadmask_fmt
    for name in __names:
        L, mask = _get_global_values(name, fmts)
        assert 2**L - 1 == mask
    return True
assert __check_payloadmask()

class _is_dyncode_XXX:
    def __init__(self, flag, payloadmask):
        self.flag = flag
        self.mask = payloadmask
    def __call__(self, uint8):
        return uint8 & ~self.mask == self.flag
    @classmethod
    def from_name(cls, name):
        fmts = dyncode_flag_fmt, dyncode_payloadmask_fmt
        args = _get_global_values(name, fmts)
        return cls(*args)
class _encode_dyncode_XXX:
    def __init__(self, name, flag, payloadlen):
        self.name, self.flag, self.len = name, flag, payloadlen
        self.is_XXX = _is_dyncode_XXX.from_name(name)
    def __call__(self, bits):
        if len(bits) != self.len:
            raise ValueError('dyncode {}: len(bits) != {}'
                             .format(self.name, self.len))
        s = ''.join('1' if b else '0' for b in bits)
        payload = int(s, 2)
        i = payload + self.flag
        assert self.is_XXX(i)
        return i
    @classmethod
    def from_name(cls, name):
        fmts = dyncode_flag_fmt, dyncode_payloadlen_fmt
        args = _get_global_values(name, fmts)
        return cls(name, *args)

class _dyncode_XXX2iter_bits(_encode_dyncode_XXX):
    def __call__(self, uint8):
        if not self.is_XXX(uint8):
            raise ValueError('not dyncode {}'.format(self.name))

        for i in BYTE_BITS[-self.len:]:
            yield int(bool(i & uint8))
        return
        
is_dyncode_single, is_dyncode_start, is_dyncode_end, is_dyncode_middle = \
                   map(_is_dyncode_XXX.from_name, __names)
encode_dyncode_single, encode_dyncode_start, \
                       encode_dyncode_end, encode_dyncode_middle = \
                   map(_encode_dyncode_XXX.from_name, __names)
dyncode_single2iter_bits, dyncode_start2iter_bits, \
                       dyncode_end2iter_bits, dyncode_middle2iter_bits = \
                   map(_dyncode_XXX2iter_bits.from_name, __names)


#def is_dyncode_single(uint8):
#def dyncode_end2iter_bits(uint8):
        
        
def _bytes2iter_iter_dyncodes(uint8s):
    'iseq of iseq of uint8; should iter the prev one and then next'
    it = iter(uint8s)
    for first in it:
        yield bytes2iter_first_dyncode(chain([first], it))
    return
def bytes2iter_dyncodes(uint8s):
    'iseq of bytes'

    it = iter(uint8s)
    while True:
        code = bytes2iter_first_dyncode(it, False)
        code = bytes(code)
        if not code:
            break
        yield code
    return

    for it in _bytes2iter_iter_dyncodes(uint8s):
        yield bytes(it)
    return

        
def bytes2iter_first_dyncode(uint8s, raise_if_empty=True, EmptyError=None):
    '''raise_if_empty=False ==>> this_f([]) yield nothing'''
    it = iter(uint8s)
    for start in it:
        break
    else:
        if raise_if_empty:
            if EmptyError is not None:
                raise EmptyError
            raise NotDyncode_EmptyError('empty uint8s')
        else:
            return

    if not is_dyncode_start(start):
        single = start
        if not is_dyncode_single(single):
            raise NotDyncodeError('not start with dyncode_start/dyncode_single')
        yield single
        return
    yield start

    
    for mid in it:
        if not is_dyncode_middle(mid):
            end = mid
            break
        yield mid
    else:
        raise NotDyncodeError('no dyncode_end')

    if not is_dyncode_end(end):
        raise NotDyncodeError('not end with dyncode_end')
    yield end
    return
def first_dyncode2iter_bits(uint8s):
    'NotDyncode_EmptyError | NotDyncodeError'
    it = first_dyncode2iter_padded_bits(uint8s)
    return padded_bits2iter_bits(it)


def dyncode2iter_bits(uint8s):
    it = dyncode2iter_padded_bits(uint8s)
    return padded_bits2iter_bits(it)

def dyncode2iter_padded_bits(uint8s):
    it = iter(uint8s)
    yield from first_dyncode2iter_padded_bits(it)
    for _ in it:
        raise NotDyncodeError('not exactly : more than one dyncode')
    return



def padded_bits2iter_bits(padded_bits):
    L = 7
    it = iter(padded_bits)
    d = deque(slice_le(it, L), L)
    if len(d) < L:
        assert len(d) == 6
    else:
        for b in it:
            yield d.popleft()
            d.append(b)
        assert len(d) == L
        
    if any(d):
        while not d.pop():pass
    else:
        # no pad
        pass
        
    yield from d
    return
    
def first_dyncode2iter_padded_bits(uint8s, raise_if_empty=True, EmptyError=None):
    '''raise_if_empty=False ==>> this_f([]) yield nothing'''
    it = bytes2iter_first_dyncode(uint8s, raise_if_empty, EmptyError)
    for start in it:
        break
    else:
        assert not raise_if_empty
        return
    
    for end in it:
        break
    else:
        single = start
        yield from dyncode_single2iter_bits(single)
        return

    yield from dyncode_start2iter_bits(start)
    mid = end
    for end in it:
        yield from dyncode_middle2iter_bits(mid)
        mid = end
    yield from dyncode_end2iter_bits(end)
    return


def _test_bits2iter_dyncode():
    chain = itertools.chain
    e = bits2iter_dyncode
    d = dyncode2iter_bits
    c = list

    def L2rng(L):
        return range(2**L-0x100, 2**L+0x100)
    def L2rng_ex(L):
        return chain(L2rng(L-1), L2rng(L), L2rng(L+1))
    def Ls2rng(*Ls):
        return chain.from_iterable(map(L2rng_ex, Ls))
        
    for i in itertools.chain(range(0x100), Ls2rng(6, 10, 17)):
        bits = bin(i)[3:]
        bits = c(int(b == '1') for b in bits)
        #bits = c(bits)
        assert c(d(e(bits))) == bits
    return

########################## encode int ####################
def bin_str2iter_bits(bin_str):
    'bin_str = rex"[01]*"'
    return (int(ch == '1') for ch in bin_str)
def bits2iter_bin_str(bits):
    return map(str, bits)
def bits2bin_str(bits):
    return ''.join(bits2iter_bin_str(bits))

def check_int(i):
    if type(i) is not int:
        raise TypeError('type(i) is not int')
def check_pint(i):
    check_int(i)
    if i <= 0:
        raise ValueError('i <= 0')
def check_uint(i):
    check_int(i)
    if i < 0:
        raise ValueError('i < 0')

def int2uint(i):
    return abs(i)*2 - int(i<0)
def uint2pint(i):
    return i + 1
def pint2uint(i):
    return i - 1
def uint2int(i):
    check_uint(i)
    neg = i & 1
    if neg:
        return -((i+1) >> 1)
    return i >> 1

def int2pint(i):
    return uint2pint(int2uint(i))
def pint2int(i):
    return uint2int(pint2uint(i))

def _test_int2pint():
    for i in range(-10, 10):
        assert pint2int(int2pint(i)) == i
def int2dyncode(i):
    return uint2dyncode(int2uint(i))
def dyncode2int(uint8s):
    return uint2int(dyncode2uint(uint8s))


########################## possible2 #####################
def uint2iter_padded_bits(i):
    'little-endian; fill with leading 0s'
    check_uint(i)

    L = i.bit_length()
    LL = bits_len2min_padded_len(L)
    bytes_len = (L+8-1)//8
    bs = i.to_bytes(bytes_len, 'little')
    bits = chain.from_iterable(map(byte2iter_rbits, bs))

    pad_len = LL - bytes_len * 8
    if pad_len < 0:
        it = islice(bits, LL)
    elif pad_len == 0:
        it = bits
    else:
        it = chain(bits, [0]*pad_len)

    it = list(it); assert len(it) == LL; it = iter(it)
    return it

def padded_bits2uint(bits):
    bs = bytes(bits2iter_bytes_zfill(bits))
    return int.from_bytes(bs, 'little')

def _test_uint2iter_padded_bits():
    for i in range(300):
        it = uint2iter_padded_bits(i)
        u = padded_bits2uint(it)
        assert i == u
    return


def uint2iter_dyncode(i):
    return padded_bits2iter_dyncode(uint2iter_padded_bits(i))
def first_dyncode2uint(uint8s, raise_if_empty=True, EmptyError=None):
    return padded_bits2uint(first_dyncode2iter_padded_bits(
        uint8s, raise_if_empty, EmptyError))
def uint2dyncode(i):
    icode = uint2iter_dyncode(i)
    code = bytes(icode)
    return code
def dyncode2uint(uint8s):
    bits = dyncode2iter_padded_bits(uint8s)
    return padded_bits2uint(bits)
def _test_uint2dyncode():
    for i in range(300):
        it = uint2dyncode(i)
        u = dyncode2uint(it)
        assert i == u
    return

assert uint2dyncode(0) == b'\0'
assert int2dyncode(0) == b'\0'
__fbyte_int0 = int2dyncode(0)[0]
_test_uint2dyncode()
_test_uint2iter_padded_bits()
def first_byte_in_dyncode_of_int_to_sign(uint8):
    if is_dyncode_single(uint8):
        single = uint8
        if single == __fbyte_int0:
            return 0
        sign_bit = BYTE_BITS[2]
    elif is_dyncode_start(uint8):
        start = uint8
        sign_bit = BYTE_BITS[3]
    else:
        for _ in bytes2iter_first_dyncode([uint8]):
            break
        raise logic-error

    # int -> uint # neg -> odd
    return -1 if uint8 & sign_bit else +1
########################## possible1 #####################
if 0:
    def pint2iter_bits(i):
        check_pint(i)
        return bin_str2iter_bits(reversed(bin(i)[3:]))

    def bits2pint(bits):
        iter_bin_str = itertools.chain(bits2iter_bin_str(bits), '1')
        s = ''.join(reversed(''.join(iter_bin_str)))
        i = int(s, 2)
        check_pint(i)
        return i

    def _test_bits2pint():
        for i in range(1, 10):
            assert bits2pint(pint2iter_bits(i))
        return

    def uint2dyncode(i):
        return pint2dyncode(uint2pint(i))
    def dyncode2uint(uint8s):
        return pint2uint(dyncode2pint(uint8s))

    def pint2dyncode(i):
        bits = pint2iter_bits(i)
        icode = bits2iter_dyncode(bits)
        code = bytes(icode)
        return code
    def dyncode2pint(uint8s):
        bits = dyncode2iter_bits(uint8s)
        return bits2pint(bits)

    def __max_uint_with_dyncode_len_1():
        for u in range(100):
            code = uint2dyncode(u)
            assert dyncode2uint(code) == u
            if len(code) != 1:
                assert u == 64
                break
        print(u)

    assert int2dyncode(0) == b' ' == bytes([0b00100000])
    assert dyncode2int(b'\0') == -32
    __fbyte_int0 = int2dyncode(0)[0]
    def first_byte_in_dyncode_of_int_to_sign(uint8):
        if is_dyncode_single(uint8):
            single = uint8
            if single == __fbyte_int0:
                return 0
            sign_bit = BYTE_BITS[2]
        elif is_dyncode_start(uint8):
            start = uint8
            sign_bit = BYTE_BITS[3]
        else:
            for _ in bytes2iter_first_dyncode([uint8]):
                break
            raise logic-error

        # int -> uint # neg -> odd
        # uint -> pint # neg -> even
        return +1 if uint8 & sign_bit else -1
        

    if 0:
        _test_int2pint()
        _test_bits2pint()
        _test_bits2iter_dyncode()
        _test_first_byte_in_dyncode_of_int_to_sign()


def _test_first_byte_in_dyncode_of_int_to_sign():
    for i in range(-300, 300):
        code = int2dyncode(i)
        b = code[0]
        s = first_byte_in_dyncode_of_int_to_sign(b)
        #print(i, code, s, bin(b))
        assert i*s == abs(i)
    return
_test_first_byte_in_dyncode_of_int_to_sign()
if __name__ == '__main__':
    from __main__ import *

    
