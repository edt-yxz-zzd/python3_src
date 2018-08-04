
'''
sint:
    signed integer
    integer
uint:
    unsigned integer
    integer >= 0
pint:
    positive integer
    integer > 0
'''

'''
uint_bits:
    uint_bits == bits'(1[01]*)?' # big-endian
    len(uint_bits) == uint.bit_length()
uint_0sbits:
    uint_0sbits == bits'0*' + uint_bits
    uint_0sbits<num_bits> == bits'0{num_bits-len(uint_bits)}' + uint_bits

uint_bytes:
    uint.byte_length() ::= (uint.bit_length()+7)//8
    uint_bytes == uint.to_bytes(uint.byte_length(), 'big')
               == uint_0sbits<8*uint.byte_length()>
uint_0sbytes:
    uint_0sbytes == bytes'\x00*' + uint_bytes
    uint_0sbytes<num_bytes> == bytes'\x00{num_bytes-len(uint_bytes)}' + uint_bytes



pint_omit_leading1_bits:
    pint_omit_leading1_bits == bits'[01]*'
    pint_omit_leading1_bits ::= uint_bits(pint)[1:]

'''

'''
total_bits = prefix_bits + payload_bits
payload_bits = uint_0sbits = leading_0s + uint_bits
assume len(payload_bits) > 0
assume len(total_bits)%8 == 0

prefix_bytes = prefix_bits + bits'0' * (8 - len(prefix_bits)%8)
             = pure_prefix_bytes + mixing_byte__high_part
pure_prefix_bytes = prefix_bits[:len(prefix_bits)//8*8]
payload_bytes = bits'0' * (7 - (len(payload_bits)-1)%8) + payload_bits
              = mixing_byte__low_part + pure_payload_bytes
pure_payload_bytes = payload_bits[-(len(payload_bits)//8*8):]
total_bytes = total_bits
            = pure_prefix_bytes + mixing_byte + pure_payload_bytes
        where mixing_byte = mixing_byte__high_part | mixing_byte__low_part
'''

'''
Uint2BitsPrefixCodeCodec:
    EnumUintBits:
        bits"1{uint}0"
        EnumUintBits0:
            bits"1{uint}00"
        EnumBitBlocks<block_size>:
            bits"(?P<block>1[01]{block_size-1}){num_blocks-1}\
                \(?P<end_block>0[01]{block_size-1})"
        SizedArray<EnumBits, BitBlock<block_size> >:
            bits"(?P<array_size>1{num_blocks-1}0)\
                \(?P<block>[01]{block_size}){num_blocks}"
Pint2BitsPrefixCodeCodec:
    EnumPintBits:
        bits"1{pint-1}0"
        EnumPintBits0:
            bits"1{pint-1}00"
    BitsLayers:
        bits"(?P<0th_bits_layer>1)\
            \(?P<nth_bits_layer>1[01]{(n-1)th_bits_layer_pint}){0,}\
            \0"
        SizedBitsLayers == SizedList<EnumPintBits, OmitLeading1_BitsLayer>:
            bits_layer2pint ::= lambda input_bits: big_endian_bits2pint(bits'1'+input_bits)
            bits"(?P<list_size>1{num_bits_layers-1}0)\
                \(?P<0th_bits_layer>)\
                \(?P<nth_bits_layer>[01]{bits_layer2pint((n-1)th_bits_layer)}){num_layers-1}"
            # num_layers include 0th_bits_layer
    
Uint2BytesPrefixCodeCodec:
    RadixNull:
        bytes'[^\xff]*\xff'
    DynamicBytes == EnumBitBlocks<8>:
        bytes'[\x80-\xff]*[\x00-\x7f]'
        SizedDynamicBytes == SizedArray<EnumPintBits, BitBlock<7> >
            == SizedTotalBytes<EnumPintBits, uint_0sbytes>
            bits'(1{total_bytes-1}0)\
                \([01]{8*total_bytes - total_bytes})'
            SizedDynamicBytes0 == SizedArray<EnumPintBits0, BitBlock<7> >
                == SizedTotalBytes<EnumPintBits0, uint_0sbytes>
                bits'(1{total_bytes-1}00)\
                    \([01]{8*total_bytes - (total_bytes+1)})'
    BytesLayers_Null:
        bytes"((?P<first_bytes_layer>[^\x00])\
              \(?P<nth_bytes_layer>(?!\x00).{(n-1)th_bytes_layer_uint}){0,}\
              \)?\
              \(\x00)"
    SizedBitsLayers_BytesLayer == SizedTotalBytes<SizedBitsLayers, uint_0sbytes>
        bits"(?P<prefix_bits>\
              \(?P<list_size>1{num_bits_layers-1}0)\
              \(?P<0th_bits_layer>)\
              \(?P<nth_bits_layer>[01]{bits_layer2pint((n-1)th_bits_layer)}){num_layers-1}\
            \)\
            \(?P<uint_0sbits>[01]{\
                \   8*bits_layer2pint((num_bits_layers-1)th_bits_layer)\
                \ - len(prefix_bits)})"
        # num_layers include 0th_bits_layer but uint_0sbits
    TriLayers == SizedTotalBytes<SizedArray<EnumUintBits, bit>, uint_0sbytes>
        bits'(1{num_second_layer_bits}0)\
            \(?P<second_layer_bits>[01]{num_second_layer_bits})\
            \(?P<uint_0sbits>[01]{\
                \   8*bits_layer2pint(second_layer_bits) \
                \ - (num_second_layer_bits+1) \
                \ - num_second_layer_bits})'
        TriLayers0 == SizedTotalBytes<SizedArray<EnumUintBits0, bit>, uint_0sbytes>
        bits'(1{num_second_layer_bits}00)\
            \(?P<second_layer_bits>[01]{num_second_layer_bits})\
            \(?P<uint_0sbits>[01]{\
                \   8*bits_layer2pint(second_layer_bits) \
                \ - (num_second_layer_bits+2) \
                \ - num_second_layer_bits})'
            
    

'''

'''
dynamic length encoding of uint
    # uint::unsigned integer # integer >= 0
    # sint::signed integer # integer
functions:
    1) encode uint into file # unit::byte
        1-1) encode uint into file by the specified case
        1-2) find a recommend case for a given uint_bit_length
        1-3) calc total bytes by the specified case for a given uint_bit_length
    2) decode from file without knowing the length of encoded bytes
        # prefix coding scheme
        # self-determined length
        2-1) detect encoding case # maybe unknown case
        2-2) skip the uint-object@file
        2-3) detect isZero/isOne
        2-4) decode from file into a word of given bit_length
            throw or truncate when overflow
    3) encode/decode sint
        3-1) detect sign : +1/0/-1
        3-2) detect isNegOne

    why?
        to support all uint instead of just a uint subset limited by 'word'
    where?
        # "xxx@file" means a object in file
        
        # for many object@file
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
            
        size-field of varlength container@file
        string
            # save few more space than utf8/utf32
            # but utf8/utf32 are non-overlap-encoding
            # and utf32 is fixed-length-encoding
        
    not where?
        singleton@file
            # since each file contains only one declaration
            version - xx.yy.zzzz ==>> (xx, yy, zzzz) or [0; xx, yy, zzzz]==A/B
                # ascii-string is good enough
            length of file-word/ptr/offset/position
                # rex'\d+ ' is good enough
                # fixed-length-elements are building block of fixed-length-struct
        fixed-length-struct
            # makes array random-accessable
            # although varlength object can be refered to by a pointer in fixed-length-struct
            #     that will not be efficient


how to encode integer (signed integer)?
    1) encoding abs:
        abs(sint).to_bytes(min_len, 'big')
    2) encoding sign:
        to fasten integer-sign detecting, the sign encoded in first byte of last_layer_uint
            this may increase the first byte into two leading bytes
            using SintUintCodec__Neg2Odd_but1_of_1stByte to encode first byte
            # SintUintCodec__msb_2nd will be more elegant but a little slower.


# big-endian
'''


'''
history
    S:
        # SMALL
        # <<== dynamic bytes + time efficiency
        # case_prefix_bits + time efficiency + prefix coding ==>> big-endian
    H:
        # HUGE
        # <<== sized array + fixed length struct
        # nth_layer_bytes[:1] != b'\x00' ==>> big-endian
    TSH:
        # TINY SMALL1 (>>8)HUGE
        # TINY <<== ascii
        # case_prefix_bits + time efficiency + prefix coding ==>> big-endian
        
    # big-endian everywhere
    
    TSLH:
        # TINY SMALL1 ~0LARGE (>>8)HUGE
    SSLLH:
        # SMALL SMALL1 1110(<<2)LARGE 1110(<<2)LARGE1 (>>8)HUGE
        # <<== unicode
    SSFH:
        # SMALL SMALL0 FIXED_LENGTH (>>8)HUGE
        # <<== word<8*2**K>
    TTFH:
        # TRILAYERS TRILAYERS0 FIXED_LENGTH (>>8)HUGE
        # TRILAYERS <<== SMALL0 + space efficiency
    BBF:
        # SIZEDBITSLAYERS_BYTESLAYER SIZEDBITSLAYERS0_BYTESLAYER FIXED_LENGTH
        # SIZEDBITSLAYERS_BYTESLAYER <<== HUGE
'''


'''
prefix_code = self_known_length_block

list_of_prefix_code_and_end_by_end_values:
    radix_null_codec:
        [:value_digit:]* null
        example:
            rex_bytes:
                '[0-9A-F]+H' # hex
                '[0-9]+ ' # dec
                '[\x00-\xfe]*\xff'
            rex_bits:
                '1*0'

    endbit_codec:
        (1(?P<payload_bits>[01]{L}))* (0(?P<payload_bits>[01]{L}))
        example:
            rex_bytes:
                '[\x00-\x7F]*[\x80-\xFF]' # dynamic bytes
            rex_bits:
                '(1[01])*(0[01])'
                '1*0'
        


length_encoded_prefix_and_list_of_prefix_code:
    SMALL:
        '1{size-1}0(?P<uint_bits>[01]{8*size-size})' # <==> '[\x00-\x7F]*[\x80-\xFF]'
        SMALL0:
            '1{size-1}00(?P<uint_bits>[01]{8*size-size-1})'
        SMALL1:
            '1{size-1}10(?P<uint_bits>[01]{8*size-size-1})'

    LARGE:
        '1{num_layers-1}0(?P<first_layer_bits>[01]{8-num_layers%8})(?P<nth_layer_bytes>([01]{8}){(n-1)th_layer_uint}){num_layers-1}'
    trilayers:
        '1{num_delta_bits}0(?P<delta_bits>[01]{num_delta_bits})(?P<uint_bits>[01]{8*(2**num_delta_bits+delta_uint)-2*num_delta_bits-1})'
        trilayers0:
            '1{num_delta_bits}00(?P<delta_bits>[01]{num_delta_bits})(?P<uint_bits>[01]{8*(2**num_delta_bits+delta_uint)-2*num_delta_bits-2})'
    

hybrid_codec:
    layers_null_codec:
        end_byte = 0x00
        last_layer_uint ::= uint
        nth_layer_bytes ::= nth_layer_uint.to_bytes(min_size, 'big')
        uint ==>> (?<nth_layer_bytes>.{(n-1)th_layer_uint})* end_byte
        if len(nth_layer_bytes) > 0:
            nth_layer_bytes[0] != 0x00
        if exists first_layer:
            len(first_layer_bytes) == 1
        
        uint == 0:
            ==>> end_byte



'''

from sand.codec.CodecBase import CodecBase
from sand.codec.UintCodec.BlockingChunkStream import \
     BinaryFile2BlockingBitFile_ReadOnly, \
     BinaryFile2BlockingBinaryFile_ReadOnly
from sand.codec.UintCodec.UintBytesCodec import bigEndianUintBytesCodec
import types # for MappingProxyType



def iter_bytes_from_file(begin, end):
    file.seek(begin)
    while file.tell() != end:
        yield file.read_eq(1)
    
def reversed_bytes_from_file(begin, end):
    file.seek(end)
    while file.tell() != begin:
        file.seek(-1, os.SEEK_CUR)
        yield file.peek_eq(1)
    
    


class UintCodecBase(CodecBase):
    '''

file::BlockingBinaryFile_ReadOnlyBase
'''
##    def wrap_file(self, file):
##        return BinaryFile2BlockingBinaryFile_ReadOnly(file)
##    def unwrap_file(self, file):
##        return file.file

    
    def iter_cases(self):
        raise NotImplementedError

    
    def _encode_to_file(self, file, u):
        num_uint_bits = u.bit_length()
        case = self.recommend_case(num_uint_bits)
        self.encode_to_file_by(file, u, case)
        
    def encode_to_file_by(self, file, u, case):
        raise NotImplementedError
    def recommend_case(self, num_uint_bits):
        raise NotImplementedError
    def calc_total_bytes(self, num_uint_bits):
        case = self.recommend_case(num_uint_bits)
        return self.calc_total_bytes_by(num_uint_bits, case)
    def calc_total_bytes_by(self, num_uint_bits, case):
        raise NotImplementedError





    def _decode_from_file(self, file):
        case = self.detect_case(file)
        return self.decode_from_file_by(file, case)

    def peek_from_file(self, file):
        return file.try_and_restore(lambda:self.decode_from_file(file))
    def decode_uint_bytes_from_file_by(self, file, case):
        begin_bytes, (begin_pos, end_pos), end_bytes = \
                     self._get_uint_bytes_info_by(file, case)
        file.seek(begin_pos)
        middle_bytes = file.read_eq(end_pos - begin_pos)
        return b''.join(begin_bytes, middle_bytes, end_bytes)
    
    def decode_from_file_by(self, file, case):
        bs = decode_uint_bytes_from_file_by(file, case)
        return bigEndianUintBytesCodec.bytes2uint(bs)
    
    def detect_case(self, file):
        raise NotImplementedError
    def skip_one_object(self, file):
        self.decode_from_file(file)
    def detect__is_zero(self, file):
        return self.peek_from_file(file) == 0
    def detect__is_one(self, file):
        return self.peek_from_file(file) == 1
    def decode_from_file_into__truncate(self, file, max_num_output_bits):
        'return (was_truncated, uint)'
        u = self.decode_from_file(file)
        
        was_truncated = False
        if u.bit_length() > max_num_output_bits:
            u &= (1 << max_num_output_bits) - 1
            was_truncated = True

        assert u.bit_length() <= max_num_output_bits
        return was_truncated, u
    def decode_from_file_into__overflow(self, file, max_num_output_bits):
        'return uint or raise OverflowError'
        was_truncated, u = self.decode_from_file_into__truncate(file)
        if was_truncated:
            raise OverflowError('u.bit_length() > max_num_output_bits')

        return u

    def iter_uint_bytes_from_file(self, file, case):
        case = self.detect_case(file)
        return self.iter_uint_bytes_from_file_by(file, case)
    def reversed_uint_bytes_from_file(self, file, case):
        case = self.detect_case(file)
        return self.reversed_uint_bytes_from_file_by(file, case)

    def _get_uint_bytes_info_by(self, file, case):
        '''return begin_bytes, (begin_pos, end_pos), end_bytes
and move current_position of file to the end of uint_object@file

uint_bytes = begin_bytes + file[begin_pos : end_pos] + end_bytes
'''
        raise NotImplementedError
    def iter_uint_bytes_from_file_by(self, file, case):
        begin_bytes, (begin_pos, end_pos), end_bytes = \
                     self._get_uint_bytes_info_by(file, case)
        yield from begin_bytes
        yield from iter_bytes_from_file(begin_pos, end_pos)
        yield from end_bytes
            
    def reversed_uint_bytes_from_file_by(self, file, case):
        begin_bytes, (begin_pos, end_pos), end_bytes = \
                     self._get_uint_bytes_info_by(file, case)
        yield from reversed(end_bytes)
        yield from reversed_bytes_from_file(begin_pos, end_pos)
        yield from reversed(begin_bytes)
        
    
    


class UintCodec__HelperBase(UintCodecBase):
    def __init__(self, cases):
        self.__cases = tuple(cases)
        
        case2encode_to_file = self._build_case2encode_to_file(self.__cases)
        self.__case2encode_to_file = types.MappingProxyType(case2encode_to_file)
        
        case2get_uint_bytes_info = self._build_case2get_uint_bytes_info(self.__cases)
        self.__case2get_uint_bytes_info = types.MappingProxyType(case2get_uint_bytes_info)
    def _build_case2encode_to_file(self, cases):
        'return dict<case, encode_to_file or None>'
        raise NotImplementedError
    def _build_case2get_uint_bytes_info(self, cases):
        'return dict<case, get_uint_bytes_info or None>'
        raise NotImplementedError
    def _build_case2calc_total_bytes(self, cases):
        'return dict<case, calc_total_bytes or None>'
        raise NotImplementedError
    
    def iter_cases(self):
        return iter(self.__cases)
    
    def encode_to_file_by(self, file, u, case):
        return self.__case2encode_to_file[case](file, u)
    def recommend_case(self, num_uint_bits):
        raise NotImplementedError
    def calc_total_bytes_by(self, num_uint_bits, case):
        return self.__case2calc_total_bytes[case](num_uint_bits)

    


    def detect_case(self, file):
        raise NotImplementedError
    def _get_uint_bytes_info_by(self, file, case):
        '''return begin_bytes, (begin_pos, end_pos), end_bytes
and move current_position of file to the end of uint_object@file

uint_bytes = begin_bytes + file[begin_pos : end_pos] + end_bytes
'''
        return self.__case2get_uint_bytes_info[case](file)




class UintCodec__SingleCaseBase(UintCodec__HelperBase):
    def __init__(self, case, prime_codec):
        super().__init__([case])
        self.__case = case
        self.__prime_codec = prime_codec
        

    def _build_case2encode_to_file(self, cases):
        'return dict<case, encode_to_file or None>'
        return {self.__case : self.__prime_codec.encode_to_file}
    def _build_case2get_uint_bytes_info(self, cases):
        'return dict<case, get_uint_bytes_info or None>'
        return {self.__case : self.__prime_codec.get_uint_bytes_info}
    def _build_case2calc_total_bytes(self, cases):
        'return dict<case, calc_total_bytes or None>'
        return {self.__case : self.__prime_codec.calc_total_bytes}
    

    def recommend_case(self, num_uint_bits):
        return self.__case
    
    def detect_case(self, file):
        return self.__case


class UintCodecPrimeBase:
    def encode_to_file(self, file, u):
        raise NotImplementedError
    def get_uint_bytes_info(self, file):
        raise NotImplementedError
    def calc_total_bytes(self, num_uint_bits):
        raise NotImplementedError
        



class UintCodecPrime__SizedDynamicBytes(UintCodecPrimeBase):
    '''


prefix = const_prefix1 + bits"1{num_dynamic_1s}0" + const_prefix2

prefix_and_mixing_bytes
    i.e.  bits"0000 1111", bits"1000 0010", bits"1111 1110 0000 0000" '''
    @property
    def const_prefix1(self):
        'return tuple<0|1>'
        raise NotImplementedError
    @property
    def const_prefix2(self):
        'return tuple<0|1>'
        raise NotImplementedError
    def encode_to_file(self, file, u):
        num_uint_bits = u.bit_length()
        total = self.calc_total_bytes(num_uint_bits)
        assert total > 0

        # prefix_and_mixing_vbytes
        num_prefix_1s = total-1
        num_prefix_0s = self.num_prefix_0s
        num_prefix_bits = num_prefix_1s + num_prefix_0s

        # num_prefix_and_mixing_bytes*8 = num_prefix_bits + num_non_prefix_bits
        # 0 < num_non_prefix_bits <= NUM_BITS_PER_BYTE
        num_prefix_and_mixing_bytes = ceil_div(num_prefix_bits+1, NUM_BITS_PER_BYTE)
        num_0s_till_mixing_byte = NUM_BITS_PER_BYTE*num_prefix_and_mixing_bytes - num_prefix_1s
        
        bits = chain(repeat(1, num_prefix_1s), [0]*num_0s_till_mixing_byte)
        prefix_and_mixing_vbytes = list(iter_bits2iter_vbytes(bits))


        # mixing_and_uint_0sbytes
        #   +1 for the mixing byte
        num_mixing_and_uint_0sbytes = total - len(prefix_and_mixing_vbytes) + 1
        uint_bytes = uint2bytes(u)
        num_zero_bytes = num_mixing_and_uint_0sbytes - len(uint_bytes)

        mixing_and_uint_0sbytes = b'\x00' * num_zero_bytes + uint_bytes


        # mixing_vbyte
        mixing_vbyte = prefix_and_mixing_vbytes[-1] | mixing_and_uint_0sbytes[0]
        prefix_and_mixing_vbytes[-1] = mixing_vbyte # update
        prefix_and_mixing_bytes = bytes(prefix_and_mixing_vbytes)
        bytes_after_mixing_byte = mixing_and_uint_0sbytes[1:]

        # write out
        file.write(prefix_and_mixing_bytes)
        file.write(bytes_after_mixing_byte)
        
    def get_uint_bytes_info(self, file):
        maybe_last_byte, skip_size = skip_byte(file, b'\xff')
        if not maybe_last_byte:
            raise DecodeError('EOF')
        last_byte = maybe_last_byte

        if last_byte != self.non_mixing_byte:
            mixing_byte = last_byte
            vbyte = byte2vbyte(last_byte)
            first_0bit_idx = NUM_BITS_PER_BYTE-1 - list(vbyte2iter_bits(vbyte)).index(0)
            assert 0 < first_0bit_idx <= NUM_BITS_PER_BYTE-1
        else:
            skip_size += 1
            mixing_byte = file.read_eq(1)
            first_0bit_idx = NUM_BITS_PER_BYTE
        assert 0 < first_0bit_idx <= NUM_BITS_PER_BYTE

        num_prefix_1s = skip_size * 
            
    def calc_total_bytes(self, num_uint_bits):
        return ceil_div(num_uint_bits, NUM_BITS_PER_BYTE-1)
    
    

