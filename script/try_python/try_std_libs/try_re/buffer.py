'''
pattern - str / memoryview
file.buffer?? NO
fail ............. only bytes..............


18.6. mmap — Memory-mapped file support
Memory-mapped file objects behave like both bytearray and like file objects.
You can use mmap objects in most places where bytearray are expected;
for example, you can use the re module to search through a memory-mapped file.

'''

import re, io


rex = re.compile(b'^ab*a')

def try_meomoryview():
    bs = b'abbbba'
    assert rex.match(memoryview(bs))
    help(memoryview(bs))
def try_RawIO():
    # fail
    #file = io.BytesIO(bs)
    #assert rex.match(file.buffer) # BytesIO' object has no attribute 'buffer'
    with open('aba.txt', 'rb').detach() as raw:
        print(type(raw)) # <class '_io.FileIO'>
        #rex.match(memoryview(raw)) # _io.FileIO object does not have the buffer interface
        rex.match(raw) # TypeError: expected string or buffer
        

def try_mmap():
    import mmap, os.path
    with open('aba.txt', 'rb') as fin:
        if not os.path.getsize(fin.name):
            # empty file handle
            raise empty-file
        else:
            mp = mmap.mmap(fin.fileno(), 0, access=mmap.ACCESS_READ)
            m = rex.search(mp)
            assert m
            print(m.group())

try_mmap()

if 0:
    # ValueError: cannot mmap an empty file
    import mmap
    with open('empty.txt', 'rb') as fin:
        mp = mmap.mmap(fin.fileno(), 0, access=mmap.ACCESS_READ)

import mmap, os.path, contextlib
def file2buffer(file, assess=mmap.ACCESS_READ):
    'return mmap/bytes/bytearray/memoryview of 1D unsigned bytes'
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
def path2buffer(path, assess=mmap.ACCESS_READ):
    mode = 'rb' if assess != mmap.ACCESS_WRITE else 'r+b'
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    with open(path, mode) as fin:
        yield file2buffer(fin, assess=assess)
    return


for fname in ['aba.txt', 'empty.txt']:
    with path2buffer(fname) as bf:
        print(memoryview(bf))




