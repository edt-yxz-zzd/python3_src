
'''
dynamic_bytes = rex_rb'[^\x00-\x7f]*[\x00-\x7f]'

sized_object = payload_len payload
payload = bytes of length payload_len
payload_len = rex_rb'[^\x00-\x80][^\x00-\x7f]*[\x00-\x7f]|[\x00-\x7f]'

# big-endian
binary_uint = payload_len payload
payload = rex_rb'(?s)[^\x00].*|'


why not '\d+ '?
    to slow to skip a big integer
'''

from os import SEEK_CUR, SEEK_END
from abc import ABCMeta, abstractmethod

from .common import *

class DynamicBytesFormatError(FormatError):pass
class PayloadFormatError(FormatError):pass
DynamicBytesFormatError


class FileObjectABC(ABCMeta):
    @abstractmethod
    def read(self, file):...
    @abstractmethod
    def write(self, file, obj):...

    @abstractmethod
    def skip(self, file):...
    def try_skip(self, file):
        'skip and then seek back'
        self.peek_len(file)
    def peek_len(self, file):
        pos = file.tell()
        end = self.skip(file)
        file.seek(pos)
        return end-pos
        

class SizedFileObjectABC(FileObjectABC):
    @abstractmethod
    def bytes2object(self, bs):...
    @abstractmethod
    def object2bytes(self, obj):...
    
    #@abstractmethod
    def read_payload(self, file, payload_len):
        if payload_len < 0:
            raise ValueError('payload_len < 0')
        bs = file.read(payload_len)
        if len(bs) != payload_len:
            assert len(bs) < payload_len
            raise PayloadFormatError('EOF: too few bytes')
        return self.bytes2object(bs)
    
    def read(self, file):
        return read_sized_object(file, self.read_payload)

    def write(self, file, obj):
        bs = self.payload2bytes(obj)
        return write_sized_bytes(file, bs)
        
    def skip(self, file):
        return skip_sized_object(file)

    
class SizedFileUint(SizedFileObjectABC):
    def bytes2object(self, bs):
        return bytes2uint(bs)
    def object2bytes(self, i):
        if i < 0:
            raise ValueError('uint2bytes: i<0')
        return uint2bytes(i)
    
class SizedFileArray(SizedFileObjectABC):
    '''size, num_elems, size_of_ptr, obj[num_elems], ptr[num_elems]'''
    def __init__(self, obj):
        assert isinstance(obj, FileObjectABC)
        self.obj = obj
    







    
def encode_uint_to_dynamic_bytes(i):
    if i < 0:
        raise ValueError('i < 0')
    if i < MAX:
        return byte(i)

    L = i.bit_length()
    width = (L+M-1)//M * M
    assert width >= L
    s01s = '{{:0>{width}b}}'.format(width=width).format(i)
    assert len(s01s) == width > 0
    assert s01s[0] in '01'

    ls = [int(s01s[i:i+M], 2)+MAX for i in range(0, width, M)]
    ls[-1] -= MAX
    assert len(ls) == 1 or ls[0] > MAX
    return bytes(ls)

def decode_uint_from_dynamic_bytes(bs):
    if not bs:
        raise DynamicBytesFormatError('not bs')
    if not bs[-1] < MAX:
        raise DynamicBytesFormatError('not bs[-1] < MAX')
    if len(bs) > 1 and not bs[0] > MAX:
        raise DynamicBytesFormatError('len(bs) > 1 and not bs[0] > MAX')
    if not all(i >= MAX for i in bs[:-1]):
        raise DynamicBytesFormatError('not all(i >= MAX for i in bs[:-1])')


    ls = [i - MAX for i in bs]
    ls[-1] += MAX
    assert all(0 <= i < MAX for i in ls)

    s01s = ''.join(CHUNK_FMT.format(i) for i in ls)
    assert len(s01s) == len(bs) * M
    return int(s01s, 2)

def test_encode_uint_to_dynamic_bytes():
    f = encode_uint_to_dynamic_bytes
    d = decode_uint_from_dynamic_bytes
    for i in [0, 1, 127, 128, 129, 255, 256, 257,]:
        assert i == d(f(i))
    for i in range(0, 600):
        assert i == d(f(i))
    for i in range(0x10000-600, 0x10000+600):
        assert i == d(f(i))
test_encode_uint_to_dynamic_bytes()

def read_dynamic_bytes(file):
    first = file.read(1)
    if not first:
        raise DynamicBytesFormatError('EOF: no bytes')
    #assert len(first) == 1
    i, = first

    if i == MAX:
        raise DynamicBytesFormatError('first byte == {!r}'.format(first))
    if i < MAX:
        return first

    bs = bytearray(first)
    while True:
        b = file.read(1)
        if not b:
            raise DynamicBytesFormatError('EOF: not ends with 0x0hhhh...')

        i, = b
        bs.append(i)
        if i < MAX:
            break
    return bytes(bs)

def read_uint_from_dynamic_bytes(file):
    bs = read_dynamic_bytes(file)
    try:
        return decode_uint_from_dynamic_bytes(bs)
    except:
        raise logic-error

def write_uint_to_dynamic_bytes(file, i):
    bs = encode_uint_to_dynamic_bytes(i)
    return file.write(bs)

def write_sized_bytes(file, bs):
    bs0 = encode_uint_to_dynamic_bytes(len(bs))
    #write_uint_to_dynamic_bytes(file, len(bs))
    return file.write(bs0 + bs)
    
def read_sized_object(file, read_payload):
    r'''object = read_payload(file, payload_len)
'''
    L = read_uint_from_dynamic_bytes(file)
    return read_payload(file, L)

def skip_sized_object(file):
    L = read_uint_from_dynamic_bytes(file)
    if not L:
        return file.seek(L, SEEK_CUR)
    
    # TO AVOID seek beyond the end
    # not: file.seek(L, SEEK_CUR)
    pos = file.tell()
    end = file.seek(0, SEEK_END)
    if end-pos < L:
        raise PayloadFormatError('EOF: too few bytes')
    
    return file.seek(pos + L)

#print(uint2bytes(0, signed=True))

if 0:
    import io
    s = io.BytesIO()
    s.seek(0, SEEK_END)
    s.seek(5) # seek beyond the end!!!
    s.write(b'3')
    assert s.getvalue() == b'\x00\x00\x00\x00\x003'






