#__all__:goto
r'''[[[
e ../../python3_src/seed/io/InputFile.py
view ../../python3_src/seed/io/IBaseIO.py
view /sdcard/0my_files/unzip/py_doc/python-3.12.4-docs-text/library/io.txt
view ../lots/NOTE/Python/download-docs.txt
    http://127.0.0.1:3124/library/io.html
to be used in:
    view ../../python3_src/seed/types/IToken.py

seed.io.InputFile
py -m nn_ns.app.debug_cmd   seed.io.InputFile -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.io.InputFile:__doc__ -ht # -ff -df

[[
mk from:
    * str|bytes
        + to_close=False
        ifile5bytes
        ifile5str
    * open(path|fd/file_descriptor, *args, **kwds)
        + to_close=(True if path | closefd if fd)
        ifile5open
    * sys.(stdin|stdout|stderr)
        + to_close=False
        + case4src:raw_vs_buffered_vs_text/[0..<3]
        + case4dst:raw_vs_buffered_vs_text/[0..<3]
        ifile5stdxxx
    * ifile
        + to_close=???
        + case4src:raw_vs_buffered_vs_text/[0..<3]
        + case4dst:raw_vs_buffered_vs_text/[0..<3]
        ifile5ifile
]]
[[
===
IOBase
  TextIOBase<BufferedIOBase>
    TextIOWrapper
    StringIO
    open("myfile.txt", "r", encoding="utf-8")
  BufferedIOBase<RawIOBase>
    BufferedWriter
    BufferedReader
    BufferedRWPair
    BufferedRandom
      BytesIO
      open("myfile.jpg", "rb")
  RawIOBase
    FileIO
    open("myfile.jpg", "rb", buffering=0)

===
IOBase <: ()
  fileno, seek, truncate
  close, closed, __enter__, __exit__, flush, isatty, __iter__, __next__, readable, readline, readlines, seekable, tell, writable, writelines
  #__iter__/readlines <<== readline -> bytes/str
RawIOBase <: IOBase
  readinto, write
  Inherited IOBase methods, read, readall

BufferedIOBase <: IOBase
  detach, read, read1, write
  Inherited IOBase methods, readinto, readinto1

TextIOBase <: IOBase
  detach, read, readline, write
  Inherited IOBase methods, encoding, errors, newlines


===
write/read:
    RawIOBase
    BufferedIOBase
    TextIOBase

readinto:
    RawIOBase
    BufferedIOBase
detach:
    BufferedIOBase
    TextIOBase

readall:
    RawIOBase
read1/readinto1:
    BufferedIOBase
encoding/errors/newlines:
    TextIOBase


===
class io.FileIO(name, mode='r', closefd=True, opener=None)
class io.BytesIO(initial_bytes=b'')

class io.BufferedReader(raw, buffer_size=DEFAULT_BUFFER_SIZE)
    from readable_non_seekable_raw_binary_stream
class io.BufferedWriter(raw, buffer_size=DEFAULT_BUFFER_SIZE)
    from writable_non_seekable_raw_binary_stream
class io.BufferedRandom(raw, buffer_size=DEFAULT_BUFFER_SIZE)
    from (readable|writable)seekable_raw_binary_stream
class io.BufferedRWPair(reader, writer, buffer_size=DEFAULT_BUFFER_SIZE, /)
    from two (readable+writable)non_seekable_raw_binary_stream

class io.TextIOWrapper(buffer, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False)
class io.StringIO(initial_value='', newline='\n')

===
class io.IncrementalNewlineDecoder



]]


py_adhoc_call   seed.io.InputFile   @f
]]]'''#'''
__all__ = r'''
mk_ifile5params
    mk_params4ifile
        ifile5bytes
        ifile5str
        ifile5open
        ifile5stdxxx
        ifile5ifile

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#from io import IOBase, RawIOBase, BufferedIOBase, TextIOBase
from io import IOBase, TextIOWrapper, BufferedRandom
import sys

from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_uint_lt, check_non_ABC

from seed.io.IBaseIO import IBaseIO, IRawIO, IBufferedIO, ITextIO
from seed.io.IBaseIO import InputStream5Bytes, InputStream5String
from seed.io.IBaseIO import IBaseInputStream, IRawInputStream, IBufferedInputStream, ITextInputStream


___end_mark_of_excluded_global_names__0___ = ...

#######
#from seed.io.IBaseIO import InputStream5Bytes, InputStream5String

#######
#class IBaseInputStream(IOBase):
#class IRawBinaryInputStream(RawIOBase):
#class IBufferedBinaryInputStream(BufferedIOBase):
#class ITextInputStream(TextIOBase):

#######
#class IBaseInputStream(IBaseIO):
#class IRawBinaryInputStream(IRawIO):
#class IBufferedBinaryInputStream(IBufferedIO):
#class ITextInputStream(ITextIO):
#######
#from seed.io.IBaseIO import IBaseInputStream, IRawInputStream as IRawBinaryInputStream, IBufferedInputStream as IBufferedBinaryInputStream, ITextInputStream
#######
#InputStream5Bytes
#InputStream5String
#InputStream5Open
#InputStream5StdXxx
#InputStream5InputFile



def ifile5bytes(bs, /, to_close=False):
    check_type_is(bytes, bs)
    if not to_close is False:raise TypeError
    return InputStream5Bytes(bs)
def ifile5str(txt, /, to_close=False):
    check_type_is(str, txt)
    if not to_close is False:raise TypeError
    return InputStream5String(txt)
def ifile5open(*args4open, to_close=True, **kwds4open):
    check_type_is(bool, to_close)
    return open(*args4open, closefd=to_close, **kwds4open)

_nms4stdxxx = 'stdin stdout stderr'.split()
def ifile5stdxxx(nm, /, case4src:range(3), case4dst:range(3), to_close=False):
    check_type_is(str, nm)
    if not nm in _nms4stdxxx:raise FileNotFoundError('sys.{nm}')
    check_uint_lt(3, case4src)
    ifile8src = getattr(sys, nm)
    match case4src:
        case 0:
            #raw
            ifile8src = ifile8src.buffer.raw
        case 1:
            #buffered
            ifile8src = ifile8src.buffer
        case 2:
            #text
            ifile8src = ifile8src
    ifile8src
    ifile8dst = ifile5ifile(ifile8src, case4src=case4src, case4dst=case4dst, to_close=to_close)
    return ifile8dst
def ifile5ifile(ifile8src, /, case4src:range(3), case4dst:range(3), to_close=False, may_kwds4TextIOWrapper=None):
    if not to_close is False:raise TypeError
    check_uint_lt(3, case4src)
    check_uint_lt(3, case4dst)
    check_type_le(IOBase, ifile8src)
    if not ifile8src.readable():raise TypeError
    #if not bool(xencoding) is (case4src < case4dst == 2):raise TypeError
    ifile8dst = ifile8src
    _case4dst = case4src
    while _case4dst < case4dst:
        match _case4dst:
            case 0:
                # raw
                ifile8dst = BufferedRandom(ifile8dst)
                _case4dst += 1
            case 1:
                #buffered
                kwds = may_kwds4TextIOWrapper if may_kwds4TextIOWrapper else {}
                ifile8dst = TextIOWrapper(ifile8dst, **kwds)
                _case4dst += 1
            case 2:
                #text
                raise 000
            case _:
                raise 000



    while _case4dst > case4dst:
        match _case4dst:
            case 0:
                #raw
                raise 000
            case 1:
                #buffered
                ifile8dst = ifile8dst.raw
                _case4dst -= 1
            case 2:
                #text
                ifile8dst = ifile8dst.buffer
                _case4dst -= 1
            case _:
                raise 000
        assert _case4dst == case4dst
        return ifile8dst

_nm2mkr = (dict(*''
,ifile5bytes=ifile5bytes
,ifile5str=ifile5str
,ifile5open=ifile5open
,ifile5stdxxx=ifile5stdxxx
,ifile5ifile=ifile5ifile
))

def mk_params4ifile(nm4mkr, /, *args4mkr, **kwds4mkr):
    mkr = _nm2mkr[nm4mkr]
    params4ifile = ((nm4mkr, *args4mkr), kwds4mkr)
    return params4ifile
def mk_ifile5params(params4ifile, /):
    ((nm4mkr, *args4mkr), kwds4mkr) = params4ifile
    mkr = _nm2mkr[nm4mkr]
    ifile = mkr(*args4mkr, **kwds4mkr)
    return ifile




__all__
from seed.io.InputFile import mk_ifile5params, mk_params4ifile, ifile5bytes, ifile5str, ifile5open, ifile5stdxxx, ifile5ifile
from seed.io.InputFile import *
