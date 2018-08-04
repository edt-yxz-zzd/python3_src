
'''
dynamic_bytes = rex_rb'[^\x00-\x7f]*[\x00-\x7f]'
'''

__all__ = '''
    DynamicBytesFormatError
    encode_dynamic_bytes_to_bytes
    decode_dynamic_bytes_from_bytes
    
    bytes2dynamic_bytes
    dynamic_bytes2bytes
'''.split()

from ._common_ import *
from ._common_ import byteorder

M = CHUNK_LEN = NUM_BITS_OF_BYTE - 1
MAX = CHUNK_LIM = 2**M
CHUNK_FMT = '{{:0>{}b}}'.format(M)
assert MAX == 0x80
class DynamicBytesFormatError(FormatError):pass


def encode_dynamic_bytes_to_bytes(dbs):
    return dynamic_bytes2bytes(dbs)
def decode_dynamic_bytes_from_bytes(bs):
    return bytes2dynamic_bytes(bs)
    
def bytes2dynamic_bytes(bs):
    # bs may begin with \0
    if not bs:
        return b'\x00'
    
    L = len(bs) * NUM_BITS_OF_BYTE
    #L += max(1, bs[0].bit_length())
    # width is the minimum integer that ge L and divides M
    width = (L + M-1) // M * M
    assert width - L < M
    
    i = int.from_bytes(bs, byteorder)
    s01s = '{{:0>{width}b}}'.format(width=width).format(i)
    assert len(s01s) == width >= L >= i.bit_length() > 0
    assert s01s[0] in '01'
    assert width // NUM_BITS_OF_BYTE * NUM_BITS_OF_BYTE == L

    ls = [int(s01s[i:i+M], 2)+MAX for i in range(0, width, M)]
    ls[-1] -= MAX
    return bytes(ls)
    
def dynamic_bytes2bytes(dbs):
    if not dbs:
        raise DynamicBytesFormatError('len(dynamic_bytes) == 0')
    if dbs == b'\x00':
        return b''

    if not dbs[-1] < MAX:
        raise DynamicBytesFormatError('not dbs[-1] < {}'.format(MAX))
    if not all(i >= MAX for i in dbs[:-1]):
        raise DynamicBytesFormatError(
            'not all(i >= {} for i in dbs[:-1])'.format(MAX))

    ls = [i - MAX for i in dbs]
    ls[-1] += MAX
    assert all(0 <= i < MAX for i in ls)

    s01s = ''.join(CHUNK_FMT.format(i) for i in ls)
    width = len(s01s)
    assert width == len(dbs) * M
    L = width // NUM_BITS_OF_BYTE * NUM_BITS_OF_BYTE
    if width - L == M:
        assert len(bs) % 8 == 1
        raise DynamicBytesFormatError('wrong length: len(bs) % 8 == 1')
    assert L > 0
    assert 0 <= width - L < M

    if s01s[:-L] != '0'*(width-L):
        raise DynamicBytesFormatError('leading patch bits not all 0s')
    i = int(s01s, 2)
    return i.to_bytes(L // NUM_BITS_OF_BYTE, byteorder)
    return int(s01s, 2)

def test_bytes2dynamic_bytes():
    f = bytes2dynamic_bytes
    d = dynamic_bytes2bytes
    for i in [0, 1, 127, 128, 129, 255, 256, 257,]:
        i = uint2bytes(i)
        assert i == d(f(i))
    for i in range(0, 600):
        i = uint2bytes(i)
        assert i == d(f(i))
    for i in range(0x10000-600, 0x10000+600):
        i = uint2bytes(i)
        assert i == d(f(i))
test_bytes2dynamic_bytes()
    
