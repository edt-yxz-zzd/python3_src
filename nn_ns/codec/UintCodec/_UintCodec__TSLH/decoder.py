
from .common import *
from ..skip_byte import skip_byte
from ..uint2ms0b_idx import uint2ms0b_idx


def read_bytes_from_blocking_binary_file(file, n):
    assert n >= 0
    bs = file.read(n)
    if bs is None:
        raise TypeError('file should not be in non-blocking mode')
    if type(bs) is not bytes:
        raise TypeError('file should not be text mode')
    return bs
def peek_bytes_from_blocking_binary_file(file, n):
    begin = file.tell()
    try:
        return read_bytes_from_blocking_binary_file(file, n)
    finally:
        file.seek(begin)

class UintCase_DecoderBase:
    def first_byte2uint_case(self, first_byte):
        u = byte_to_uint8(first_byte)
        return which_uint_case(u)

    def read_bytes(self, file, n):
        bs = read_bytes_from_blocking_binary_file(file, n)
        if len(bs) != n:
            raise DecodeError('EOF')
        return bs
    def peek_bytes(self, file, n):
        bs = peek_bytes_from_blocking_binary_file(file, n)
        if len(bs) != n:
            raise DecodeError('EOF')
        return bs
    def detect_uint_case(self, file):
        b = self.peek_bytes(file, 1)
        return self.first_byte2uint_case(b)


    def read_header(self, file):
        '''read header from file

header = (pure_prefix_bytes, mixing_byte), idx_of_last_prefix_bit_in_mixing_byte
len(pure_prefix_bytes) >= 0
len(mixing_byte) == 1
let idx = idx_of_last_prefix_bit_in_mixing_byte
0 <= idx <= 8
if idx == 0:
    ==>> no payload bits (bits of first layer uint) in mixing_byte
    ==>> mixing_byte is a pure_prefix_byte

if idx == 8:
    mixing_byte is a pure payload byte
'''
        (pure_prefix_bytes, mixing_byte), idx = self._read_header(file)
        return (pure_prefix_bytes, mixing_byte), idx

    def split_mixing_byte(self, mixing_byte, idx):
        '''split byte into prefix mask bits and payload bits

return (prefix_tail::uint, len_of_prefix_tail_bits), (payload::uint, len_of_payload_bits)

param idx
    idx = idx_of_last_prefix_bit_in_mixing_byte
param mixing_byte, idx_of_last_prefix_bit_in_mixing_byte
    see read_header
'''

        assert 0 <= idx <= 8
        len_of_prefix_tail_bits = 8 - idx
        len_of_payload_bits = idx

        u = byte_to_uint8(mixing_byte)
        prefix_tail = u >> idx
        payload = u & ((1<<idx) - 1)

        return (prefix_tail, len_of_prefix_tail_bits), (payload, len_of_payload_bits)

    def calc_num_layers(self, pure_prefix_bytes,
                              prefix_tail, len_of_prefix_tail_bits):
        'return None or uint; None - 0x00 terminated'
        return self._calc_num_layers(
            pure_prefix_bytes, prefix_tail, len_of_prefix_tail_bits)
    
    def calc_first_layer_size(self,
                              pure_prefix_bytes,
                              prefix_tail, len_of_prefix_tail_bits):
        'unit byte; include the mixing byte; so result >= 1'
        assert 0 <= len_of_prefix_tail_bits <= 8
        r = self._calc_first_layer_size(
            pure_prefix_bytes, prefix_tail, len_of_prefix_tail_bits)
        assert r >= 1
        return r

    def calc_nth_layer_bitsize(self, nth_layer_bytes):
        'bytes in big-endian'

        bs = nth_layer_bytes
        for i, uint8 in enumerate(bs):
            if uint8:
                break
        else:
            return 0

        return uint8.bit_length() + 8*(len(bs) - (i+1))

    def to_word(self, bitsize_per_word, nth_layer_bytes):
        bitsize = self.calc_nth_layer_bitsize(nth_layer_bytes)
        if bitsize > bitsize_per_word:
            raise TypeError('word too small')

        return self.to_uint(nth_layer_bytes)
    def to_uint(self, nth_layer_bytes):
        return bigEndianUintBytesCodec.bytes2uint(nth_layer_bytes)

    def decode(self, bs):
        
        file = io.BytesIO(bs)
        begin = file.tell()
        
        u = self.decode_from_file(file)
        end = file.tell()
        used_size = end - begin
        if used_size < len(bs):
            # not EOF
            raise DecodeError('remain some unused bytes after decoding; '
                              'total:{} = used:{} + unused{}'.format(len(bs), used_size, len(bs)-used_size))
        return u
    def decode_from_file(self, file):
        assert self.uint_case == self.detect_uint_case(file)
        
        (pure_prefix_bytes, mixing_byte), idx = self.read_header(file)
        (prefix_tail, len_of_prefix_tail_bits), \
            (payload, len_of_payload_bits) = \
                self.split_mixing_byte(mixing_byte, idx)
        n = self.calc_num_layers(
            pure_prefix_bytes, prefix_tail, len_of_prefix_tail_bits)
        if n is not None and n < 1:
            raise unknown-case

        first_layer_size = self.calc_first_layer_size(
            pure_prefix_bytes, prefix_tail, len_of_prefix_tail_bits)

        assert first_layer_size >= 1
        first_layer_remain_bytes = file.read(first_layer_size - 1)
        first_byte_in_first_layer = uint8_to_byte(payload)
        first_layer_bytes = first_byte_in_first_layer + first_layer_remain_bytes
        first_layer_uint = self.to_uint(first_layer_bytes)

        if n is None and first_layer_uint == 0:
            'begin_byte end_byte'
            return 0
            
        if n is None:
            def is_finish(file, num_layers, i_th):
                return self.peek_bytes(file, 1) == b'\x00'
            def skip_end_tag(file):
                end_tag = self.read_bytes(file, 1)
                assert end_tag == b'\x00'
        else:
            def is_finish(file, num_layers, i_th):
                return i_th > num_layers
            def skip_end_tag(file):
                pass

        prev_uint = first_layer_uint
        i_th = 2
        while not is_finish(file, n, i_th):
            len_of_ith_layer_bytes = prev_uint
            ith_layer_bytes = self.read_bytes(file, len_of_ith_layer_bytes)
            ith_layer_uint = self.to_uint(ith_layer_bytes)

            # prepare for next round
            prev_uint = ith_layer_uint
            i_th += 1
        else:
            skip_end_tag(file)
            last_layer_uint = prev_uint

        return last_layer_uint
            
            
    @property
    def uint_case(self):
        raise NotImplementedError
    def _calc_first_layer_size(self,
                              pure_prefix_bytes,
                              prefix_tail, len_of_prefix_tail_bits):
        raise NotImplementedError
    def _read_header(self, file):
        raise NotImplementedError
        return (pure_prefix_bytes, mixing_byte), idx
    def _calc_num_layers(self,
                         pure_prefix_bytes,
                         prefix_tail, len_of_prefix_tail_bits):
        raise NotImplementedError
            

# all without checking
# should use detect uint_case first and then choice one to decode

class TinyCaseDecoder(UintCase_DecoderBase):
    @property
    def uint_case(self):
        return TINY_CASE
    def _calc_first_layer_size(self,
                              pure_prefix_bytes,
                              prefix_tail, len_of_prefix_tail_bits):
        return 1
    def _read_header(self, file):
        pure_prefix_bytes = b''
        mixing_byte = self.read_bytes(file, 1)
        idx = 7
        assert byte_to_uint8(mixing_byte) < 0x80
        return (pure_prefix_bytes, mixing_byte), idx
    def _calc_num_layers(self,
                         pure_prefix_bytes,
                         prefix_tail, len_of_prefix_tail_bits):
        return 1

class SmallCaseDecoder(UintCase_DecoderBase):
    @property
    def uint_case(self):
        return SMALL_CASE
    def _calc_first_layer_size(self,
                              pure_prefix_bytes,
                              prefix_tail, len_of_prefix_tail_bits):
        num_prefix_bits = 8*len(pure_prefix_bytes) + len_of_prefix_tail_bits
        num_0s = 1
        num_1s = num_prefix_bits - num_0s
        total_size = num_1s # num_1s in prefix
        return total_size - len(pure_prefix_bytes)
    def _read_header(self, file):
        maybe_last_byte, skip_size = skip_byte(file, b'\xff')
        assert len(maybe_last_byte) <= 1
        if not maybe_last_byte:
            raise DecodeError('EOF while small_case.read_header')

        last_byte = maybe_last_byte
        
        pure_prefix_bytes = b'\xff' * skip_size
        mixing_byte = last_byte
        mixing_uint8 = byte_to_uint8(mixing_byte)
        idx = uint2ms0b_idx(mixing_uint8, 8)
        if idx == 0:
            assert mixing_byte == b'\xfe'
            pure_prefix_bytes += mixing_byte
            mixing_byte = self.read_bytes(file, 1)
            idx = 8
        else:
            assert idx < 8
            
        
        return (pure_prefix_bytes, mixing_byte), idx
    def _calc_num_layers(self,
                         pure_prefix_bytes,
                         prefix_tail, len_of_prefix_tail_bits):
        return 1
    

class LargeCaseDecoder(UintCase_DecoderBase):
    @property
    def uint_case(self):
        return LARGE_CASE
    def _calc_first_layer_size(self,
                              pure_prefix_bytes,
                              prefix_tail, len_of_prefix_tail_bits):
        return 1
    def _read_header(self, file):
        first_byte = self.read_bytes(file, 1)
        if first_byte == b'\x80':
            maybe_last_byte, skip_size = skip_byte(file, b'\x00')
            if not maybe_last_byte:
                raise DecodeError('EOF while large_case.read_header')

            last_byte = maybe_last_byte

            pure_prefix_bytes = first_byte + b'\x00'*skip_size
            mixing_byte = last_byte

            # first 1 idx
            mixing_uint8 = byte_to_uint8(mixing_byte)
            idx = mixing_uint8.bit_length() - 1
        else:
            pure_prefix_bytes = b''
            mixing_byte = first_byte

            # second 1 idx
            mixing_uint8 = byte_to_uint8(mixing_byte)
            mixing_uint8 -= 0x80
            idx = mixing_uint8.bit_length() - 1
            
        assert idx >= 0

        if idx == 0:
            pure_prefix_bytes += mixing_byte
            mixing_byte = self.read_bytes(file, 1)
            idx = 8

        return (pure_prefix_bytes, mixing_byte), idx
    def _calc_num_layers(self,
                         pure_prefix_bytes,
                         prefix_tail, len_of_prefix_tail_bits):

        num_prefix_bits = 8*len(pure_prefix_bytes) + len_of_prefix_tail_bits
        num_1s = 2
        num_0s = num_prefix_bits - num_1s
        num_layers = num_0s
        assert num_layers >= 2
        return num_layers
    

class HugeCaseDecoder(UintCase_DecoderBase):
    @property
    def uint_case(self):
        return HUGE_CASE
    def _calc_first_layer_size(self,
                              pure_prefix_bytes,
                              prefix_tail, len_of_prefix_tail_bits):
        return 1
    def _read_header(self, file):
        pure_prefix_bytes = first_byte = self.read_bytes(file, 1)
        mixing_byte = second_byte = self.read_bytes(file, 1)
        idx = 8
        return (pure_prefix_bytes, mixing_byte), idx
    def _calc_num_layers(self,
                         pure_prefix_bytes,
                         prefix_tail, len_of_prefix_tail_bits):
        return None
    
TinyCaseDecoder
SmallCaseDecoder
LargeCaseDecoder
HugeCaseDecoder

_uint_case2decoder_class = {
    TINY_CASE : TinyCaseDecoder,
    SMALL_CASE : SmallCaseDecoder,
    LARGE_CASE : LargeCaseDecoder,
    HUGE_CASE : HugeCaseDecoder,
    }
_uint_case2decode_func = {case: T().decode_from_file
                          for case, T in _uint_case2decoder_class.items()}

detect_uint_case = UintCase_DecoderBase().detect_uint_case
def decode_from_file(file):
    case = detect_uint_case(file)
    decode_func = _uint_case2decode_func[case]
    return decode_func(file)



