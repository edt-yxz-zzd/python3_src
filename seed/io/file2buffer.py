
'''
for re.search


18.6. mmap — Memory-mapped file support
Memory-mapped file objects behave like both bytearray and like file objects.
You can use mmap objects in most places where bytearray are expected;
for example, you can use the re module to search through a memory-mapped file.

'''
__all__ = ['file2buffer', 'path2buffer']
import mmap, os.path, contextlib, io
from sand import UnknownCaseError

if 0:
    class ReadOnlyMemoryView(memoryview):
        # TypeError: type 'memoryview' is not an acceptable base type
        __slots__ = ()
        readonly = True
        __delitem__ = __setitem__ = None
        
    memoryview(bytearray())[0]=1
    ReadOnlyMemoryView(bytearray())[0]=1

def file2buffer(file, assess=None):
    '''return mmap/bytes/bytearray/memoryview of 1D unsigned bytes

assess :
    default to mmap.ACCESS_READ if not BytesIO else mmap.ACCESS_WRITE
'''

    if isinstance(file, io.BytesIO):
        buffer = file.getbuffer()
        if assess is None or assess == mmap.ACCESS_WRITE:
            pass
        elif assess == mmap.ACCESS_READ:
            # buffer.readonly = True # fail!
            raise ValueError('not support ACCESS_READ for BytesIO')
        elif assess == mmap.ACCESS_COPY:
            raise ValueError('not support ACCESS_COPY for BytesIO')
        else:
            raise UnknownCaseError('unknown "assess" case : {!r}'.format(assess))
        return buffer
    
    if assess is None:
        assess = mmap.ACCESS_READ
    f = mmap.mmap
    fn = file.fileno()
    try:
        return f(fn, 0, access=assess)
    except ValueError as e:
        err_str = 'cannot mmap an empty file' # for Windows
        if (type(e) is ValueError and e.args == (err_str,)) or \
           (hasattr(file, 'name') and not os.path.getsize(file.name)):
            # e == ValueError(err_str) or empty file
            if assess == mmap.ACCESS_READ:
                return b''
        raise e

@contextlib.contextmanager
def path2buffer(path, assess=None):
    '''assess : default to mmap.ACCESS_READ

usage:
    import re
    with path2buffer('xxx.bin') as buffer:
        m = re.search(b'http://', buffer)
        if m:
            ...
'''
    if assess is None:
        assess = mmap.ACCESS_READ
    mode = 'rb' if assess != mmap.ACCESS_WRITE else 'r+b'
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    with open(path, mode) as fin:
        yield file2buffer(fin, assess=assess)
    return

#memoryview(io.BytesIO(b''))
# TypeError: memoryview: _io.BytesIO object does not have the buffer interface

file2buffer(io.BytesIO())
