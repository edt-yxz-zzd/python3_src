
'''
TSLH uint encoding


uint::unsigned int # integer >= 0

functions:
    1) encode uint into bytes
    2) decode from file without knowing the length of encoded bytes

encoding:
    encoded_bytes = encode_uint_to_bytes(uint)
    encoded_bytes <==> encoded_bits
    assert len(encoded_bits) % 8 == 0
    assert len(encoded_bits) >= 8

    encoded_bits ::= prefix_bits + leading_0bits + first_layer_uint_bits
                    + (nth_layer_uint_bytes for n in range(2, num_layers+1)) + end_bytes
    prefix_bits ::= const_prefix_bits + dynamic_prefix_bits
    dynamic_prefix_bits = bits_0s1 | bits_1s0 | ''
    bits_0s1 = bits'0*1'
    bits_1s0 = bits'1*0'
    assert len(leading_0bits) >= 0
    assert len(uint_bits) == uint.bit_length() >= 0
    assert len(nth_layer_uint_bits) == (n-1)th_layer_uint for n in range(2, M)
    len(leading_0bits + first_layer_uint_bits) determined by prefix_bits
    num_layers determined by prefix_bits or the occurrence of end_bytes
    assert len(prefix_bits + leading_0bits + first_layer_uint_bits) % 8 == 0

    
    
    size ::= len(encoded_bytes)
    uint = last_layer_uint
    1) tiny case : 0...
        size = 1
        size_of_layers = 1
        bits"0(?P<bits-of-uint>[01]{7})"
        uint.bit_length() <= 7
    2) small case : 11...
        size >= 2
        size_of_layers = 1
        bits"1{size}0(?P<bits-of-uint>[01]{8*size-(size+1)})"
        len_of_prefix_mask_bits = size+1 < 8
        ==>> size < 7
        uint.bit_length() <= (7-1)*8 = 48
    3) large case : 100...
        size >= 7
        size_of_layers >= 2
        1 <= first_layer_uint <= 0xff
        bits"10{size_of_layers}1"\
            "(?P<bits-of-first-layer-uint>[01]{((1+size_of_layers+1)-1)%8 + 1})"\
            "(?P<bits-of-second-layer-uint>[01]{first_layer_uint*8})"\
            "(?P<bits-of-(n)th-layer-uint>[01]{(n-1)th_layer_uint*8}){size_of_layers-2}"
        len_of_prefix_mask_bits = 1+size_of_layers+1 < 2*8 = 16
        size_of_layers <= 13
            and if size_of_layers == 13 ==>> first_layer_uint <= 1
        max_uint when size_of_layers==13
            ==>> first_layer_uint.bit_length() == 16 - (1+13+1) = 1
            ==>> max_first_layer_uint = 1
            ==>> max_second_layer_uint = 0xff = 2**(8*max_first_layer_uint) - 1
            ==>> max_(n)th_layer_uint = 2**(8*max_(n-1)th_layer_uint) - 1
            ==>> uint < ?? # it seems very large
    4) huge case : 1010_0000 ... 0000_0000
        size_of_layers >= 14
        byte_pattern = begin_byte \
                           one_byte_for_first_layer_uint
                           (?<bytes_of_(n)th_layer_uint> byte{(n-1)th_layer_uint}){13,}
                        end_byte
        begin_byte = 0b10100000
        end_byte = 0x00
        
        first byte of bytes_of_(n)th_layer_uint != end_byte
            ==>> bytes in big-endian order
        
    5) reserved case : bits"1010(?!0000)([01]{8})*"
        reserved for future versions
    6) user case : 1011...
        Private Use Area

    NOTE:
        any non-tiny-case can be used to encode any uint
        so, there exists bytes in non-standard forms
            that can be decoded into uint
        # to ease huge-case testing
        
how to encode integer (signed integer)?
    1) encoding abs:
        abs(sint).to_bytes(min_len, 'big')
    2) encoding sign:
        to fasten integer-sign detecting, the sign encoded in first byte of last_layer_uint
            this may increase the first byte into two leading bytes
            using SintUintCodec__Neg2Odd_but1_of_1stByte to encode first byte
'''




from .cases import *
from .common import DecodeError, EncodeError
from ..CodecBase import CodecBase



    
    
class UintCodecBase(CodecBase):
    
    def encode_to_file(self, file, u, uint_case=None):
        'return None'
        assert type(u) is int and u >= 0
        
        r = self._encode_to_file(file, u, uint_case=uint_case)
        assert r is None
        return
    def decode_from_file(self, file):
        u = self._decode_from_file(file)
        assert type(u) is int and u >= 0
        return u
    
##    def decode_from_file(self, file):
##        u = self.try_decode_from_file(file)
##        if u is None:
##            raise DecodeError
##        return u
        
    def _encode_to_file(self, file, u, uint_case):
        raise NotImplementedError
    def _decode_from_file(self, file):
        raise NotImplementedError

BITS_1S0 = 'BITS_1S0'
BITS_0S1 = 'BITS_0S1'
BITS_EMPTY = 'BITS_EMPTY'
class UintCaseCodecBase(CodecBase):
    def get_uint_case(self):
        raise NotImplementedError
        
    def get_const_prefix_bits(self):
        'return rex"[01]*" # ::str'
        raise NotImplementedError
    
    def get_dynamic_prefix_bits_case(self):
        'return BITS_1S0 | BITS_0S1 | BITS_EMPTY'
        raise NotImplementedError
    def get_end_bytes(self):
        raise NotImplementedError

    def prefix_bits2prefix_bytes(self, prefix_bits):
        'return prefix_bytes and idx # idx is len of padding 0bits'
        L = len(prefix_bits)
        len_of_prefix_bytes = (L+7) // 8
        len_of_padding_bits = 8 * len_of_prefix_bytes - L
        prefix_bits += '0' * len_of_padding_bits
        u = int(prefix_bits, 2)
        bs = u.to_bytes(len_of_prefix_bytes, 'big')
        idx = len_of_padding_bits
        return bs, idx


    # decode
    
    def read_prefix_bytes(self, file):
        'return prefix_bytes, idx_of_last_prefix_bit_in_last_byte # 0 <= idx <= 8'
        
        _const_prefix_bits = self.get_const_prefix_bits()
        if _const_prefix_bits:
            _const_prefix_bytes, _idx = self.prefix_bits2prefix_bytes(const_prefix_bits)
        else:
            _const_prefix_bytes, _idx = b'\x00', 8
        const_prefix_bytes = self.read_bytes(len(_const_prefix_bytes))
        high, low = self.split_byte(const_prefix_bytes[-1:])
        const_prefix_bytes_ = const_prefix_bytes[:-1] + high
        if const_prefix_bytes_ != _const_prefix_bytes:
            raise DecodeError('not begin with bits : {!r}'.format(const_prefix_bits))

        low_uint8 = byte_to_uint8(low)
        low_bits = '{:0>8b}'.format(low_uint8)
        low_bits = low_bits[len(low_bits)-_idx:]

        case = self.get_dynamic_prefix_bits_case()
        if case == BITS_EMPTY:
            prefix_bytes = const_prefix_bytes
            idx = _idx
        else:
            if case == BITS_1S0:
                NT = '1' # non-terminate bit
                T = '0'
                nt_byte = '\xff'
                
            elif case == BITS_0S1:
                NT = '0' # non-terminate bit
                T = '1'
                nt_byte = '\x00'
            if not all(bit == NT for bit in low_bits):
                prefix_bytes = const_prefix_bytes
                idx = _idx - low_bits.index(T) - 1
            else:
                maybe_last_byte, skip_size = self.skip_byte(file, nt_byte)
                if not maybe_last_byte:
                    raise DecodeError('EOF')
                else:
                    last_byte = maybe_last_byte
                prefix_bytes = const_prefix_bytes + nt_byte * skip_size + last_byte
                u = byte_to_uint8(last_byte)
                bits = '{:0>8b}'.format(u)
                idx = 8 - bits.index(T) - 1
                
                
        return prefix_bytes, idx
            
        

    def calc_len_of_dynamic_prefix_bits(self, prefix_bytes, idx):
        len_of_prefix_bits = 8*len(prefix_bytes) - idx
        return len_of_prefix_bits - len(self.get_const_prefix_bits())
    

    def calc_len_of_first_layer_bytes(self, len_of_dynamic_prefix_bits):
        raise NotImplementedError
    def calc_num_layers(self, len_of_dynamic_prefix_bits):
        'return None for end_bytes terminated or uint'
        raise NotImplementedError


    def split_byte(self, byte, idx):
        uint8 = byte_to_uint8(byte)
        low_mask = (1<<idx) - 1
        high_mask = 0xff - low_mask
        low_part = uint8 & low_mask
        high_part = uint8 & high_mask
        return tuple(map(uint8_to_byte, [high_part, low_part]))
    
    def read_last_layer_uint(self, file, num_layers, len_of_first_layer_bytes, idx):
        
        def calc_next_size__first(nth_size):
            # only for first layer
            if idx == 0:
                nth_bytes = self.read_bytes(file, nth_size)
            else:
                file.seek(file.tell() - 1)
                nth_bytes = self.read_bytes(file, nth_size)
                high, low = split_byte(nth_bytes[:1])
                nth_bytes = low + nth_bytes[1:]
            nth_layer_uint = self.bytes2uint(nth_bytes)
            next_size = nth_layer_uint
            nonlocal calc_next_size
            calc_next_size = calc_next_size__nonfirst
        def calc_next_size__nonfirst(nth_size):
            nth_bytes = self.read_bytes(file, nth_size)
            nth_layer_uint = self.bytes2uint(nth_bytes)
            next_size = nth_layer_uint
            return next_size
        
        calc_next_size = calc_next_size__first
        
        if num_layers is None:
            end_bytes = self.get_end_bytes()
            is_end = lambda: self.peek_bytes(file, len(end_bytes)) == end_bytes
            if is_end():
                nth_size = 0
            else:
                nth_size = len_of_first_layer_bytes

            while not is_end():
                next_size = calc_next_size(nth_size)

                # prepare for next round
                # n += 1
                nth_size = next_size

        else:
            assert num_layers >= 0
            if num_layers == 0:
                nth_size = 0
            else:
                nth_size = len_of_first_layer_bytes
                
            for _ in range(num_layers):
                next_size = calc_next_size(nth_size)

                # prepare for next round
                # n += 1
                nth_size = next_size
        #self.read_bytes(file, len(end_bytes))
        last_layer_uint = nth_size
        return last_layer_uint

    def _decode_from_file(self, file):
        prefix_bytes, idx = self.read_prefix_bytes(file)
        len_of_dynamic_prefix_bits = self.calc_len_of_dynamic_prefix_bits(prefix_bytes, idx)
        len_of_first_layer_bytes = self.calc_len_of_first_layer_bytes(len_of_dynamic_prefix_bits)
        num_layers = self.calc_num_layers(len_of_dynamic_prefix_bits)
        u = read_last_layer_uint(self, file, num_layers, len_of_first_layer_bytes, idx)
        return u
        

class XxxxUintCaseCodec(UintCaseCodecBase):
    def get_uint_case(self):
        raise NotImplementedError
        
    def get_const_prefix_bits(self):
        'return rex"[01]*" # ::str'
        raise NotImplementedError
    
    def get_dynamic_prefix_bits_case(self):
        'return BITS_1S0 | BITS_0S1 | BITS_EMPTY'
        raise NotImplementedError
    def get_end_bytes(self):
        raise NotImplementedError

    # decode

    
    def calc_len_of_first_layer_bytes(self, len_of_dynamic_prefix_bits):
        raise NotImplementedError
    def calc_num_layers(self, len_of_dynamic_prefix_bits):
        'return None for end_bytes terminated or uint'
        raise NotImplementedError
    
class TinyUintCaseCodec(UintCaseCodecBase):
    def get_uint_case(self):
        return TINY_CASE
        
    def get_const_prefix_bits(self):
        'return rex"[01]*" # ::str'
        return ''
    
    def get_dynamic_prefix_bits_case(self):
        'return BITS_1S0 | BITS_0S1 | BITS_EMPTY'
        return BITS_1S0
    def get_end_bytes(self):
        return b''

    # decode

    
    def calc_len_of_first_layer_bytes(self, len_of_dynamic_prefix_bits):
        total_bytes = len_of_dynamic_prefix_bits
        total_bits = 8 * total_bytes
        len_of_first_layer_bits = total_bits - len_of_dynamic_prefix_bits
        len_of_first_layer_bytes = (len_of_first_layer_bits + 7) // 8
        return len_of_first_layer_bytes
    def calc_num_layers(self, len_of_dynamic_prefix_bits):
        'return None for end_bytes terminated or uint'
        return 1
    
    
    
aUintCodec__TSLH = UintCodec__TSLH()
aSintCodec__TSLH = SintCodec__TSLH()



