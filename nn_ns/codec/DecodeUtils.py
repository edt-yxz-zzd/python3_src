
r'''
assume file opened in 'rb' mode
assume using uint32le as integer in file
'''

__all__ = '''
    read_bytes
    read_uint32le
    check_bytes

    DecodeUtils
    DecodeUtils_32le
'''.split()


from .. import CheckError

    
def read_bytes(file, size):
    bs = file.read(size)
    if len(bs) != size:
        raise EOFError('too few bytes')
    return bs

def read_uint32le(file):
    bs = read_bytes(file, 4)
    u = int.from_bytes(bs, 'little')
    assert u >= 0
    return u

def check_bytes(file, bs, pos=None):
    if pos is not None:
        file.seek(pos)
        
    size = len(bs)
    try:
        new_bs = read_bytes(file, size)
    except EOFError:
        raise CheckError('not the given bytes in file : EOF')
    if not new_bs == bs:
        raise CheckError('not the given bytes in file : {!r} != {!r}'
                             .format(new_bs, bs))
##
##def read_sized_bytes(file):
##    size = read_uint32le(file)
##    bs = read_bytes(file, size)
##    return bs
##
##def read_sized_array(file, elem_reader):
##    size = read_uint32le(file)
##    ls = [elem_reader(file) for _ in range(size)]
##    return ls
##    

class DecodeUtils:
    r'''utilities to use in decoding process or parsing binary file

file should be opened in "rb" mode

default parameters:
    offset_size = position_size = sint_size = uint_size = 4
    byte_order = 'little'

    subclasses can override these parameters.

DecodeUtils serves as baseclass while DecodeUtils_32le for concrete usage
though DecodeUtils_32le is DecodeUtils
'''
    offset_size = position_size = sint_size = uint_size = 4
    byte_order = 'little'
    
    def __init__(self, file):
        'file should be opened in "rb" mode'
        self.file = file
    def read_uint(self):
        u = self.read_xint(self.uint_size, signed=False)
        assert u >= 0
        return u
    def read_sint(self):
        i = self.read_xint(self.sint_size, signed=True)
        return i
    def read_xint(self, size, *, signed=False):
        bs = read_bytes(self.file, size)
        i = int.from_bytes(bs, self.byte_order, signed=signed)
        return i

    def read_bytes(self, size):
        return read_bytes(self.file, size)
    
    def check_bytes(self, bs, pos=None):
        return check_bytes(self.file, bs, pos)

    ########## sized xxx ########
    # sized_xxx = struct{uint size; elem_t array[size];};
    
    def read_sized_bytes(self):
        size = self.read_uint()
        bs = self.read_bytes(size)
        return bs

    def read_sized_array(self, elem_factory):
        size = self.read_uint()
        ls = [elem_factory() for _ in range(size)]
        return ls
        
DecodeUtils_32le = DecodeUtils
