
class UintBytesCodec:
    def __init__(self, byteorder):
        # byteorder = 'big' or 'little'
        assert byteorder in {'big', 'little'}
        self.byteorder = byteorder
    def bytes2uint(self, bs):
        return int.from_bytes(bs, byteorder=self.byteorder)
    def uint2bytes(self, u):
        L = u.bit_length()
        size = (L+7)//8
        bs = u.to_bytes(size, byteorder=self.byteorder)
        return bs
##    def uint8_to_byte(self, uint8):
##        return bytes([uint8])
##    def byte_to_uint8(self, byte):
##        uint8, = byte
##        return uint8

bigEndianUintBytesCodec = UintBytesCodec('big')
littleEndianUintBytesCodec = UintBytesCodec('little')
