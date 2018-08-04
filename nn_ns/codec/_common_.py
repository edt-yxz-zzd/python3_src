
__all__ = '''
    NUM_BITS_OF_BYTE
    FormatError
    
    byte
    uint2bytes_len
    uint2bytes
    bytes2uint
'''.split()

from .. import FormatError
NUM_BITS_OF_BYTE = 8
byteorder = 'big' # NOT IN __all__, but public


def byte(i):
    return bytes([i])
def uint2bytes_len(i):
    assert i >= 0
    return (i.bit_length() + NUM_BITS_OF_BYTE-1) // NUM_BITS_OF_BYTE
def uint2bytes(i, byteorder=byteorder, *, signed=False):
    L = uint2bytes_len(i)
    return i.to_bytes(L, byteorder, signed=signed)
def bytes2uint(bs, byteorder=byteorder, *, signed=False):
    if not bs:
        return 0
    if not bs[0]:
        raise FormatError('bytes2uint: bytes[0] == 0')
    return int.from_bytes(bs, byteorder, signed=signed)
