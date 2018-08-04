'''
TS uint encoding
    # TS from TSLH

size = len(encoded_bytes)
bits"(?P<prefix-bits>1{size-1}0)(?P<bits-of-uint>[01]{8*size - size})"
efficiency = 7bits/8bits

'''

from .CodecBase import CodecBase, DecodeError, EncodeError
from .UintBytesCodec import bigEndianUintBytesCodec
from .skip_byte import skip_byte
from .uint8_to_byte import uint8_to_byte, byte_to_uint8
from .uint2ms0b_idx import uint2ms0b_idx

uint2bytes = bigEndianUintBytesCodec.uint2bytes
class UintCodec__TS(CodecBase):
    def calc_total_size(self, u):
        if u == 0:
            return 1
        L = u.bit_length()
        return (L+6)//7
    def make_prefix_bytes(self, total_size):
        # prefix_bits + padding_bits == prefix_bytes
        num_prefix_bits = total_size
        num_0s = 1
        num_1s = num_prefix_bits - num_0s
        
        num_padding_bits = 8 - num_prefix_bits % 8 # (0, 8]
        u = 1 << num_1s # 10{num_1s}
        u -= 1 # 1{num_1s}
        u <<= num_0s + num_padding_bits # 1{num_1s}00{num_padding_bits}
        len_of_prefix_bytes = (num_prefix_bits + num_padding_bits) // 8
        return u.to_bytes(len_of_prefix_bytes, 'big')


    def read_bytes(self, file, n):
        bs = file.read(n)
        if len(bs) != n:
            raise DecodeError('EOF')
        return bs

    def make_payload_bytes(self, u, size):
        payload_bytes = uint2bytes(u)
        if len(payload_bytes) < size:
            payload_bytes = b'\x00' * (size - len(payload_bytes)) + payload_bytes

        assert size == len(payload_bytes)
        return payload_bytes
        
    def _encode_to_file(self, file, u):
        total_size = self.calc_total_size(u)
        prefix_bytes = self.make_prefix_bytes(total_size)
        len_of_payload_bytes = 1 + (total_size - len(prefix_bytes))
        payload_bytes = self.make_payload_bytes(u, len_of_payload_bytes)
        assert len(payload_bytes) == len_of_payload_bytes

        mixing_uint8 = prefix_bytes[-1] | payload_bytes[0]
        mixing_byte = uint8_to_byte(mixing_uint8)
        ls = [prefix_bytes[:-1], mixing_byte, payload_bytes[1:]]
        for bs in ls:
            file.write(bs)
        return
    def _decode_from_file(self, file):
        maybe_last_byte, skip_size = skip_byte(file, b'\xff')
        if not maybe_last_byte:
            raise DecodeError('EOF')
        else:
            last_byte = maybe_last_byte
        last_uint8 = byte_to_uint8(last_byte)
        idx = uint2ms0b_idx(last_uint8, 8) # first 0bit
        num_payload_bits_in_last_byte = idx

        prefix_0xff_bytes = b'\xff'*skip_size
        if idx == 0:
            # last_byte is prefix_bytes[-2]
            pure_prefix_bytes = prefix_0xff_bytes + last_byte
            mixing_byte = self.read_bytes(file, 1)
            idx = 8
        else:
            # last_byte is prefix_bytes[-1] that is the mixing_byte
            pure_prefix_bytes = prefix_0xff_bytes
            mixing_byte = last_byte
            idx = idx

        total_size = self._prefix2total_size(pure_prefix_bytes, mixing_byte, idx)
        remain_size = total_size - (len(pure_prefix_bytes) + len(mixing_byte))
        remain_bytes = self.read_bytes(file, remain_size)
        return self.calc_uint(idx, mixing_byte, remain_bytes)
    def calc_uint(self, idx, mixing_byte, remain_bytes):
        mixing_uint8 = byte_to_uint8(mixing_byte)
        mask = (1<<idx)-1
        first_uint8 = mask & mixing_uint8
        first_byte = uint8_to_byte(first_uint8)
        payload_bytes = first_byte + remain_bytes
        return int.from_bytes(payload_bytes, 'big')
        
        

    def _prefix2total_size(self, pure_prefix_bytes, mixing_byte, idx):
        L = 8* (len(pure_prefix_bytes) + len(mixing_byte))
        return L - idx
    

aUintCodec__TS = UintCodec__TS()
def test_UintCodec__TS():
    _test_UintCodec__TS(range(1000),
                        [1<<i for i in range(1000)])
def _test_UintCodec__TS(*rngs):
    a = aUintCodec__TS
    d = a.decode
    e = a.encode
    for rng in rngs:
        for i in rng:
            try:
                assert i == d(e(i))
            except:
                print(i)
                print(e(i))
                print(d(e(i)))
                raise

test_UintCodec__TS()





