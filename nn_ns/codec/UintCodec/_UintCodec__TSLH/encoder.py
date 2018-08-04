
from .common import *

_uint2bytes = bigEndianUintBytesCodec.uint2bytes
_bytes2uint = bigEndianUintBytesCodec.bytes2uint
class UintCase_EncoderBase:
    def uint2bytes(self, u):
        return _uint2bytes(u)
    def bytes2uint(self, bs):
        return _bytes2uint(bs)


    def add_a_new_layer(self, reversed_layers):
        L = len(reversed_layers[-1])
        bs = self.uint2bytes(L)
        reversed_layers.append(bs)
    def calc_reversed_layers(self, u, min_num_layers=0):
        last_layer_bytes = self.uint2bytes(u)
        rlayers = [last_layer_bytes]
        while True:
            L = len(rlayers[-1])
            if L < 2 and min_num_layers <= len(rlayers):
                break
            self.add_a_new_layer(rlayers)
        return rlayers


    #def prefix_bytes_and_reversed_layers

    def encode(self, u):
        file = io.BytesIO()
        self.encode_to_file(file, u)
        return file.getvalue()
    def encode_to_file(self, file, u):
        raise NotImplementedError

aUintCase_EncoderBase = UintCase_EncoderBase()
calc_reversed_layers = aUintCase_EncoderBase.calc_reversed_layers

class HugeCaseEncoder(UintCase_EncoderBase):
    def encode_to_file(self, file, u):
        rlayers = self.calc_reversed_layers(u)
##        if not len(rlayers[-1]):
##            assert u == 0
##            rlayers[-1] = b'\x00'
        begin_byte = b'\xa0' # 0b10100000
        end_byte   = b'\x00' # 0b00000000

        file.write(begin_byte)
        for bs in reversed(rlayers):
            file.write(bs)
        file.write(end_byte)
class LargeCaseEncoder(UintCase_EncoderBase):
    def num_layers2prefix(self, num_layers):
        '0 < len_of_padding_bits <= 8'
        # 10{num_layers}1...
        assert num_layers >= 2
        prefix = 1 << (num_layers+1)
        prefix += 1
        len_of_prefix_tail_bits = (1+num_layers+1)%8
        len_of_padding_bits = 8 - len_of_prefix_tail_bits # (0, 8]
        prefix <<= len_of_padding_bits
        prefix_bytes = self.uint2bytes(prefix)
        assert 0x80 <= prefix_bytes[0] < 0x10100000

        return prefix_bytes, len_of_padding_bits

    def _reversed_layers2detail(self, reversed_layers):
        num_layers = len(reversed_layers)
        
        prefix_bytes, len_of_padding_bits = self.num_layers2prefix(num_layers)
        first_layer_bytes = reversed_layers[-1]
        first_layer_uint = self.bytes2uint(first_layer_bytes)
        assert first_layer_uint < 0x100

        len_of_payload_bits = first_layer_uint.bit_length()
        assert len_of_payload_bits <= 8
        assert len_of_padding_bits > 0
        return prefix_bytes, len_of_padding_bits, len_of_payload_bits
        
    def encode_to_file(self, file, u):
        reversed_layers = self.calc_reversed_layers(u, min_num_layers=2)
        prefix_bytes, len_of_padding_bits, len_of_payload_bits = \
                             self._reversed_layers2detail(reversed_layers)
        if len_of_padding_bits < len_of_payload_bits:
            self.add_a_new_layer(reversed_layers)
            prefix_bytes, len_of_padding_bits, len_of_payload_bits = \
                             self._reversed_layers2detail(reversed_layers)

        assert 8 >= len_of_padding_bits >= len_of_payload_bits >= 0
        first_layer_bytes = reversed_layers[-1]
        reversed_layers[-1] = first_layer_bytes[1:]
        maybe_first_byte = first_layer_bytes[:1]
        if maybe_first_byte:
            first_byte = maybe_first_byte
            fake_first_byte = first_byte
        else:
            fake_first_byte = b'\x00'
        pure_prefix_bytes = prefix_bytes[:-1]
        # bugs: once used '&' intead of '|'
        mixing_uint8 = prefix_bytes[-1] | fake_first_byte[0]
        mixing_byte = uint8_to_byte(mixing_uint8)
        reversed_layers.extend([mixing_byte, pure_prefix_bytes])

        for bs in reversed(reversed_layers):
            file.write(bs)
        
        
class SmallCaseEncoder(UintCase_EncoderBase):
    def calc_last_layer_bytes(self, u, min_length):
        bs = self.uint2bytes(u)
        if len(bs) < min_length:
            bs = b'\x00'*(min_length - len(bs)) + bs

        return bs

    def calc_total_size(self, u):
        # 1{total_size}00{len_of_padding_bits}[01]{bit_length_of_uint}

        # total_size*8 == total_size + 1 + len_of_padding_bits + bit_length_of_uint
        # where 0 <= len_of_padding_bits < 8
        # total_size*7 == 1 + len_of_padding_bits + bit_length_of_uint
        L = u.bit_length()
        total_size = (L+1 +6)//7
        min_total_size = 2
        total_size = max(min_total_size, total_size)
        return total_size
        
    def total_size2prefix(self, total_size):
        len_of_prefix_bits = total_size+1
        prefix = 1 << len_of_prefix_bits
        prefix -= 2
        len_of_padding_bits = 8 - len_of_prefix_bits%8 # (0, 8] # include the sep 0
        prefix <<= len_of_padding_bits
        prefix_bytes = self.uint2bytes(prefix)
        assert prefix_bytes[0] >= 0b11000000
        assert len(prefix_bytes) == len_of_prefix_bits//8 + 1 # +1 for mixing_byte
        return prefix_bytes

    def calc_len_of_last_layer_bytes(self, total_size):
        len_of_pure_prefix_bytes = (total_size+1)//8
        len_of_last_layer_bytes = total_size - len_of_pure_prefix_bytes
        return len_of_last_layer_bytes
        
    
    def encode_to_file(self, file, u):
        total_size = self.calc_total_size(u)
        len_of_last_layer_bytes = self.calc_len_of_last_layer_bytes(total_size)
        last_layer_bytes = self.calc_last_layer_bytes(u, len_of_last_layer_bytes)
        assert len(last_layer_bytes) == len_of_last_layer_bytes
        prefix_bytes = self.total_size2prefix(total_size)
        
        pure_prefix_bytes = prefix_bytes[:-1]
        # bugs: once used '&' intead of '|'
        mixing_uint8 = prefix_bytes[-1] | last_layer_bytes[0] 
        mixing_byte = uint8_to_byte(mixing_uint8)
        ls = [pure_prefix_bytes, mixing_byte, last_layer_bytes[1:]]
        try:
            assert sum(map(len, ls)) == total_size
        except:
            print('total_size =', total_size)
            raise
        for bs in ls:
            file.write(bs)
        
        
            
class TinyCaseEncoder(UintCase_EncoderBase):
    def encode_to_file(self, file, u):
        assert 0 <= u < 0x80
        byte = uint8_to_byte(u)
        file.write(byte)



_uint_case2encoder_class = {
    TINY_CASE : TinyCaseEncoder,
    SMALL_CASE : SmallCaseEncoder,
    LARGE_CASE : LargeCaseEncoder,
    HUGE_CASE : HugeCaseEncoder,
    }
_uint_case2encode_func = {case: T().encode_to_file
                          for case, T in _uint_case2encoder_class.items()}

def _encode_to_file(file, u, uint_case):
    return _uint_case2encode_func[uint_case](file, u)
def encode_to_file(file, u, uint_case=None):
    if uint_case is None:
        L = u.bit_length()
        if L < 8:
            uint_case = TINY_CASE
        elif L <= 48:
            uint_case = SMALL_CASE
        else:
            rlayers = calc_reversed_layers(u)
            if len(rlayers) < 13:
                uint_case = LARGE_CASE
            else:
                uint_case = HUGE_CASE
    return _encode_to_file(file, u, uint_case)




    
        
