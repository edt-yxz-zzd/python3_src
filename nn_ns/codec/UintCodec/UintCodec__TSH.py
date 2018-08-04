
'''
TSH uint encoding - deprecated


two dynamic length encoding of uint : aUintHcodeCodec and aUintScodeCodec
    why?
        to support all uint instead of just a uint subset limited by 'word'
    where?
        # for each file-object
        # little bytes are required for encoding small uint
        #   UintHcodeCodec:
        #     0~127      ==>> 1 bytes # waste 1 bits /  8 bits
        #   128~8191     ==>> 2 bytes # waste 3 bits / 16 bits
        #  8192~1048575  ==>> 3 bytes # waste 4 bits / 24 bits
        uint # which may contain hundreds of bits
        
        #   UintScodeCodec:
        #     0~127      ==>> 1 bytes # waste 1 bits /  8 bits
        #   128~16383    ==>> 2 bytes # waste 2 bits / 16 bits
        # 16384~2097151  ==>> 3 bytes # waste 3 bits / 24 bits
        type/case/enum
            # but sometimes, string names are more useful
            # we can build an association list alist<name::string, id::uint> at header
            
        size-field of varlength file-container
        string
            # save few more space than utf8/utf32
            # but utf8/utf32 are non-overlap-encoding
            # and utf32 is fixed-length-encoding
        
    not where?
        file-singleton
            # since each file contains only one declaration
            version - xx.yy.zzzz ==>> (xx, yy, zzzz) or [0; xx, yy, zzzz]==A/B
                # ascii-string is good enough
            length of file-word/ptr/offset/position
                # rex'\d+ ' is good enough
                # fixed-length-elements are building block of fixed-length-struct
        fixed-length-struct
            # makes array random-accessable
            


# L = uint.bit_length()
# MAX_LS = max_bit_length_of_small_case

# tiny uint 0~2**7-1 encoded in scode
# uint2scode(tiny_uint)
scode : byte[size] ; size > 0 ; big-endian-bitorder for each byte
    bit pattern : 1{size-1}0(?P<big-endian-bits-of-small-uint>[01]{7*size})

# small uint 2**7~2**(MAX_LS+1)-1
# uint2scode(sint2uint(small_uint))
# efficience = L/(((L+1)+6)//7) / 8

# big uint 2**(MAX_LS+1)~+oo
# data = uint2bytes(big_uint)
# uint2scode(sint2uint(len(data)), min_length=2) + data
# efficience when len(size::bytes)==min_length==2 = L/(2+(L+7)//8)/8
# let efficience-small-case < efficience-big-case-with-len_size-2
#     L/(((L+1)+6)//7) / 8 < L/(2+(L+7)//8)/8
#     2+(L+7)//8 < ((L+1)+6)//7
#     1 + ceil(L/8) < ceil(L/7)
#         where L > 7 (not tiny case) and (L+7)//8 < 2**(7*2-1) (big-case len_size==2)
#             # 7 < L < 2**(7*2-1)*8 = 2**16
#     <<== L >= 106
#     let MAX_LS = 105



'''

# file::BinaryIO

__all__ = '''
    DecodeError
    EncodeError
    
    aUintScodeCodec
    aUintHcodeCodec
'''.split()


import io, os
from sand import DecodeError, EncodeError
from .UintBytesCodec import bigEndianUintBytesCodec
from .SintUintCodec import SintUintCodec__msb_2nd
from .uint8_to_byte import uint8_to_byte
from .uint2ms0b_idx import uint2ms0b_idx


def _find_ans():
    # 1 + ceil(L/8) < ceil(L/7) where 7 < L < 2**16
    import math
    pred = lambda L: 1 + math.ceil(L/8) < math.ceil(L/7)
    for L in range(8, 2**16):
        if pred(L):
            if all(pred(L_) for L_ in range(L, L+17)):
                return L
    raise logic-error
#print('1 + ceil(L/8) < ceil(L/7) where 7 < L < 2**16 ==>> L = {}'.format(_find_ans()))

##def uint8_to_byte(uint8):
##    return bytes([uint8])


aSintUintCodec = SintUintCodec__msb_2nd()
aUintBytesCodec = bigEndianUintBytesCodec


class UintScodeCodec:
    # 's' in 'scode' - stands for 'small uint' or 'size of array'
    def __init__(self):
        self.__aUintBytesCodec = bigEndianUintBytesCodec # must be 'big'!
    def bytes2uint(self, bs):
        return self.__aUintBytesCodec.bytes2uint(bs)
    def uint2bytes(self, u):
        return self.__aUintBytesCodec.uint2bytes(u)

    def _calc_min_code_size(self, bit_length_of_uint):
        L = bit_length_of_uint
        code_size = (L+6)//7
        return code_size
    def _calc_code_size_ex(self, bit_length_of_uint, min_length):
        code_size = self._calc_min_code_size(bit_length_of_uint)
        if code_size < min_length:
            code_size = min_length
        num_1s = code_size-1
        num_0s = 1
        return code_size, num_1s, num_0s
    def encode(self, u, min_length=None):
        # encode_uint_to_scode
        assert type(u) is int
        assert u >= 0
        if min_length is None or min_length < 1:
            min_length = 1

        L = u.bit_length()
        code_size, num_1s, num_0s = self._calc_code_size_ex(L, min_length)


        prefix_mask = b'\xff'*(num_1s//8)
        num_1s_tail = num_1s % 8
        weight_of_0 = 1 << (8-num_1s_tail-1)
        
        bs = self.uint2bytes(u)
        if not bs:
            bs = b'\x00'
        assert bs

        if len(prefix_mask) + len(bs) < code_size:
            bs = b'\x00' * (code_size - len(prefix_mask) - len(bs)) + bs
            
        try:
            assert bs[0] < weight_of_0
        except:
            print(locals())
            raise

        prefix_1s_tail = (1 << num_1s_tail) - 1
        prefix_1s_tail <<= (8-num_1s_tail)
        # prefix_1s_tail = uint8_to_byte(prefix_1s_tail)
        mixing = prefix_1s_tail | bs[0]
        mixing = uint8_to_byte(mixing)
        return b''.join([prefix_mask, mixing, bs[1:]])



    def decode_from_file(self, file):
        # decode_uint_from_scode_in_file
        begin = file.tell()
        try:
            return self._decode_from_file(file)
        except DecodeError as e:
            e.args += ('begins in file at 0x{:X}'.format(begin), begin)
            raise
    def skip_255s_1B(self, file):
        n = 0 # num_255s
        while True:
            b = file.read(1)
            if not b:
                raise DecodeError('EOF but scode is incomplete while reading prefix 1\'s')
            assert len(b) == 1
            if b == b'\xff':
                n += 1
            else:
                break

        num_255s = n
        mixing_byte = b # prefix_mask_bits + data_bits
        return num_255s, mixing_byte

        
    def mixing2data_byte(self, mixing, ms0b_idx):
        idx = ms0b_idx
        if idx is None:
            # where is the first 0bit in byte??
            idx = (0xff - mixing).bit_length() - 1
            assert (1 << idx) & mixing == 0
            assert idx == 7 or (1 << (idx+1)) & mixing
            assert idx == uint2ms0b_idx(mixing, 8)

        first_data_byte = ((1 << idx) - 1) & mixing
        first_data_byte = uint8_to_byte(first_data_byte)
        return first_data_byte
    def _decode_from_file(self, file):
        num_255s, (mixing_byte, first_data_byte), data_tail = \
                  self.read_scode_from_file_ex(file)
        data = first_data_byte + data_tail
        return self.bytes2uint(data)

    def _calc_num_bytes(self, num_1s, num_0s):
        assert num_0s == 1
        assert num_1s >= 0
        return num_1s + num_0s
    def read_scode_from_file_ex(self, file):
        num_255s, mixing_byte = self.skip_255s_1B(file)
        mixing, = mixing_byte
        ms0b_idx = uint2ms0b_idx(mixing, 8)
        first_data_byte = self.mixing2data_byte(mixing, ms0b_idx)
        
        num_1s_tail = 8-1 - ms0b_idx
        num_1s = num_255s * 8 + num_1s_tail
        num_0s = 1
        num_bytes = self._calc_num_bytes(num_1s, num_0s)
        data_tail_len = num_bytes - num_255s - 1 # -1 for mixing byte
        data_tail = file.read(data_tail_len)
        if len(data_tail) != data_tail_len:
            raise DecodeError('EOF but scode is incomplete while reading payload')
        
        return num_255s, (mixing_byte, first_data_byte), data_tail
        

aUintScodeCodec = UintScodeCodec()

class UintHcodeCodec:
    # 'h' in 'hcode' - stands for 'huge uint' or 'hundreds of bits'

    def __init__(self, max_bit_length_of_small_uint,
                 aUintXcodeCodec, aUintBytesCodec, aSintUintCodec):
        # xcode ::= pcode | scode

        # dependency inject
        
        self.__aUintXcodeCodec = aUintXcodeCodec
        self.__aUintBytesCodec = aUintBytesCodec # for BIG case payload
        self.__aSintUintCodec = aSintUintCodec
        self.__MAX_LS = max_bit_length_of_small_uint
    def sint2uint(self, i):
        return self.__aSintUintCodec.sint2uint(i)
    def uint2sint(self, u):
        return self.__aSintUintCodec.uint2sint(u)
    def bytes2uint(self, bs):
        return self.__aUintBytesCodec.bytes2uint(bs)
    def uint2bytes(self, u):
        return self.__aUintBytesCodec.uint2bytes(u)
    
    def try_decode_tiny_from_file(self, file):
        # cannot use decode_small_uint_from_file
        # since size of BIG case encoded in non-std form (min_length==2)
        #    maybe 0 <= size < 128
        
        begin = file.tell()
        
        bs = file.read(1)
        if bs:
            assert len(bs) == 1
            
            tiny, = bs
            if 0 <= tiny < 128:
                # TINY case
                return tiny
            else:
                # not TINY case
                pass
        else:
            # EOF
            # fail to decode
            pass

        # fail
        file.seek(begin)
        return None


        
    def decode(self, bs, more=False):
        file = io.BytesIO(bs)
        begin = file.tell()
        
        u = self.decode_from_file(file)
        end = file.tell()
        used_size = end - begin
        if more:
            end = file.tell()
            return u, end - begin
        elif used_size < len(bs):
            # not EOF
            raise DecodeError('remain some unused bytes after decoding; '
                              'total:{} = used:{} + unused{}'.format(len(bs), used_size, len(bs)-used_size))
        return u

    def decode_from_file(self, file):
        begin = file.tell()
        
        tiny = self.try_decode_tiny_from_file(file)
        if tiny is not None:
            return tiny

        try:
            usize = self.decode_small_uint_from_file(file)
            # NOTE : usize of BIG case in non-std form!
            # so, maybe 0 <= usize < 128
        except DecodeError as e:
            raise DecodeError('decoding non-TINY-case, reading ssize', e)
        
        ssize = self.uint2sint(usize)
        if ssize < 0:
            # BIG case
            payload_len = -ssize-1
            payload = file.read(payload_len)
            if len(payload) != payload_len:
                raise DecodeError(
                    'EOF while decoding BIG-case, payload incomplete',
                    'begins in file at 0x{:X}'.format(begin), begin)
            
            u = self.bytes2uint(payload)
        else:
            # SMALL case
            u = ssize
        return u


    def encode_tiny(self, u):
        # TINY case
        return uint8_to_byte(u)

    def encode_nontiny(self, ssize, payload, min_length):
        usize = self.sint2uint(ssize)
        usize_code = self.encode_small_uint(usize, min_length)
        
        assert usize_code
        assert usize_code[0] >= 128 # not TINY case
        return usize_code + payload
        
    def encode_small(self, u):
        # SMALL case
        payload = b''
        ssize = u
        assert ssize >= 0
        min_len = 0 # in fact, >=2
        return self.encode_nontiny(ssize, payload, min_len)
        
    def encode_big(self, u):
        # BIG case
        payload = self.uint2bytes(u)
        ssize = -len(payload)-1 # != 0
        assert ssize < 0
        min_len = 2
        return self.encode_nontiny(ssize, payload, min_len)
        
    def encode(self, u):
        assert type(u) is int
        assert u >= 0

        if self.is_tiny_uint(u):
            return self.encode_tiny(u)
        elif self.is_big_uint(u):
            return self.encode_big(u)
        else:
            return self.encode_small(u)
        
    def _encode__ver1(self, u):
        assert type(u) is int
        assert u >= 0

        if 0 <= u < 128:
            # TINY case
            return uint8_to_byte(u)
        
        # build (ssize, payload, min_len)
        if u.bit_length() > self.max_bit_length_of_small_uint():
            # BIG case
            payload = self.uint2bytes(u)
            ssize = -len(payload)-1 # != 0
            assert ssize < 0 # so will not confuse with small case
            min_len = 2
        else:
            # SMALL case
            payload = b''
            ssize = u
            assert ssize >= 0
            min_len = 0 # in fact, >=2
            
        usize = self.sint2uint(ssize)
        usize_code = self.encode_small_uint(usize, min_len)
        
        assert usize_code
        assert usize_code[0] >= 128 # not TINY case
        return usize_code + payload

    def is_tiny_uint(self, u):
        return 0 <= u <= self.max_tiny_case()
    def is_big_uint(self, u):
        return u.bit_length() > self.max_bit_length_of_small_uint()
    def max_tiny_case(self):
        return 127
    def max_bit_length_of_small_uint(self):
        # for pcode or scode
        return self.__MAX_LS # 105


    def encode_small_uint(self, u, min_length=None):
        # to pcode or scode
        return self.__aUintXcodeCodec.encode(u, min_length)
        
    def decode_small_uint_from_file(self, file):
        # from pcode or scode
        return self.__aUintXcodeCodec.decode_from_file(file)

aUintHcodeCodec = UintHcodeCodec(105, aUintScodeCodec, aUintBytesCodec, aSintUintCodec)


def test_UintHcodeCodec(aUintHcodeCodec):
    _test_UintCodec(aUintHcodeCodec, range(300))
    MAX_LS = aUintHcodeCodec.max_bit_length_of_small_uint()
    _test_UintCodec(aUintHcodeCodec,
                    [i for j in range(0, MAX_LS+300)
                         for i in [1<<j, (1<<j)+1]])
def _test_UintCodec(aUintHcodeCodec, rng):
    c = aUintHcodeCodec
    for i in rng:

        try:
            assert i == c.decode(c.encode(i))
        except:
            print(i)
            bs = c.uint2bytes(i)
            print(bs[0], len(bs), i.bit_length())
            raise

test_UintHcodeCodec(aUintHcodeCodec)



