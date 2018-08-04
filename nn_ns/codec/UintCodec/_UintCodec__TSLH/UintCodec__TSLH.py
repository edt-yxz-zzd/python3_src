
'''
TSLH uint encoding


uint::unsigned int # integer >= 0

functions:
    1) encode uint into bytes
    2) decode from file without knowing the length of encoded bytes

encoding:
    size ::= len(uint_encode(uint))
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



from ..SintUintCodec import \
     aSintUintCodec__Neg2Odd_but1_of_1stByte as _aSintUintCodec
from .codec import encode_to_file, decode_from_file
from .cases import *
from .common import DecodeError, EncodeError
from ..CodecBase import CodecBase


_sint2uint = _aSintUintCodec.sint2uint
_uint2sint = _aSintUintCodec.uint2sint
class SintCodec__TSLH(CodecBase):
    def _encode_to_file(self, file, sint):
        uint = _sint2uint(sint)
        return aUintCodec__TSLH.encode_to_file(file, uint)
    def _decode_from_file(self, file):
        uint = aUintCodec__TSLH.decode_from_file(file)
        return _uint2sint(uint)
    
    
    
class UintCodec__TSLH(CodecBase):
    
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
        return encode_to_file(file, u, uint_case)
        raise NotImplementedError
    def _decode_from_file(self, file):
        return decode_from_file(file)
        raise NotImplementedError


aUintCodec__TSLH = UintCodec__TSLH()
aSintCodec__TSLH = SintCodec__TSLH()



