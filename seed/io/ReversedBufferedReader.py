#__all__:goto
view ../../python3_src/seed/tiny_/null_dev.py
    可以 反过来，readable()调用_check_readable()，这样就没毛病了
[IOBase => IBaseIO] is ok, but:
    RawIOBase required 『at most only one system call is ever made』
        hard to impl ReversedRawIO
r'''[[[
e ../../python3_src/seed/io/ReversedBufferedReader.py


seed.io.ReversedBufferedReader
py -m seed.io.ReversedBufferedReader
py -m nn_ns.app.debug_cmd   seed.io.ReversedBufferedReader -x
py -m nn_ns.app.doctest_cmd seed.io.ReversedBufferedReader:__doc__ -v
py -m nn_ns.app.doctest_cmd seed.io.ReversedBufferedReader!
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.io.ReversedBufferedReader   @print_methods_of_IBaseIO
from seed.io.ReversedBufferedReader import *



[[
ABC <: Inherits
  Stub Methods
  Mixin Methods and Properties

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


]]

[[
BufferedReader <: BufferedIOBase
BufferedReader(raw, buffer_size=DEFAULT_BUFFER_SIZE)
  public constructor
  raw :: readable-sequential-RawIOBase
    #不需要writable,seekable

peek([size]) -> bytes
  [at most one single read on the raw stream is done]
  [without advancing the position]

  [len(result) <???> size]arbitrary
    [The number of bytes returned may be less or more than requested]
    size有什么用？



read([size]) -> bytes{.len<=size}|^UnsupportedOperation-not-readable|^ValueError-closed
  [pseudo_EOF4nonblocking_mode =[def]= the read call would block in non-blocking mode]
  [EOF_ex =[def]= EOF or pseudo_EOF4nonblocking_mode]

  default => read until EOF_ex
  nondefault => [not[len(result)==size]] -> [len(result) < size][EOF_ex]
    #没了:^BlockingIOError



read1([size]) -> ?may? bytes|???^BlockingIOError???|^UnsupportedOperation-not-readable|^ValueError-closed
  [len(cached)>0] => [result:=cached[:size]]
  [len(cached)==0] => [result:=.raw.read(size)]



]]
[[
RawIOBase <: IOBase
no public constructor
except readall: read/readinto/write => at most only one system call is ever made

read(size=-1) -> None|bytes{.len<=size}
  default => read all
  nondefault => only one system call is ever made
    ???why???since『raw』???
      yes!BufferedIOBase.read uses multiple system calls
  [result==b''][not size==0] => EOF
  [non-blocking mode][no bytes available] <==> [result is None]
  <<== readall+readinto


readall() -> bytes
  multiple system calls until EOF


readinto(b) -> may num_bytes
  b :: pre-allocated-writable-bytearray
  [non-blocking mode][no bytes available] <==> [result is None]
  only one system call is ever made


write(b) -> may num_bytes
  [non-blocking mode][no single byte could be readily written] <==> [result is None]
  [num_bytes <= len(b)]
  only one system call is ever made


]]
[[
IOBase <: ()
no public constructor

close()¶
  allow called more than once
closed :: bool
  True => [read()... will undefined/raise ValueError]
fileno() -> file_descriptor|^OSError-not-file|^ValueError-closed
flush() -> None|^BlockingIOError-raw-stream-block|^UnsupportedOperation-not-writable|^ValueError-closed
isatty() -> bool|^ValueError-closed
  [the stream is interactive (i.e., connected to a terminal/tty device)]
  TTY???interactive terminal
  TTY - teletypewriter
    1 电传打字电报机
    2 印刷电信机
    n. 电传打字机

readable() -> bool|^ValueError
  False => [read*() will raise OSError]

readline(size=-1) -> xstring|^UnsupportedOperation-not-readable|^ValueError-closed
  at most size (in bytes/characters) will be read
    xxx at most size bytes will be read #???not-(in bytes/characters)
    见下面:TextIOBase.readline，计数单位是字符，非字节
  binary file line_sep===b'\n'
  text file line_sep <<== open(newline=...)

readlines(hint=-1) -> [xstring]|^UnsupportedOperation-not-readable|^ValueError-closed
  no more lines will be read if the total size (in bytes/characters) of all lines so far exceeds hint.
  #see: __iter__

seek(offset, whence=SEEK_SET) -> new absolute position|^UnsupportedOperation-not-seekable|^ValueError-closed
  #os.***
  SEEK_SET or 0 – start of the stream (the default);
    offset :: uint
  SEEK_CUR or 1 – current stream position;
    offset :: int
  SEEK_END or 2 – end of the stream;
  offset :: nint

seekable() -> bool|^ValueError
  [stream supports random access]
  False => [seek(), tell(), truncate() will raise OSError]

tell() -> current stream position|^UnsupportedOperation-not-seekable|^ValueError-closed

truncate(size=None)-> new file size|^UnsupportedOperation-not-seekable&writable|^ValueError-closed
  size=None => size=current position
  extend or reduce the current file size
    padding <<== platform specified


writable() -> bool|^ValueError
  False => [write*(), truncate() will raise OSError]



writelines(lines) -> ?|^UnsupportedOperation-not-writable|^ValueError-closed
  #writelines() doesnot add line_sep



__del__()¶
  call .close()
]]


测试先后:_check_not_closed vs _check_writable

>>> import seed.io.ReversedBufferedReader
>>> with open(seed.io.ReversedBufferedReader.__file__, 'rb') as ibfile:
...     pass


#!!!_check_writable before _check_not_closed!!!
>>> ibfile.write(b'')
Traceback (most recent call last):
    ...
io.UnsupportedOperation: write
>>> ibfile.fileno()
Traceback (most recent call last):
    ...
ValueError: I/O operation on closed file




>>> from io import BytesIO

>>> bs = b'0123456789abcdef'
>>> ibfile = BytesIO(bs)



>>> ibfile.seek(0, 3)
Traceback (most recent call last):
    ...
ValueError: invalid whence (3, should be 0, 1 or 2)
>>> ibfile.seek(None, SEEK_SET)
Traceback (most recent call last):
    ...
TypeError: 'NoneType' object cannot be interpreted as an integer
>>> ibfile.seek(0, None)
Traceback (most recent call last):
    ...
TypeError: 'NoneType' object cannot be interpreted as an integer
>>> __index__(None)
Traceback (most recent call last):
    ...
TypeError: 'NoneType' object cannot be interpreted as an integer
>>> as_uint_('seek', -1)
Traceback (most recent call last):
    ...
ValueError: negative seek value -1
>>> ibfile.seek(-1, SEEK_SET) #[new_location4tell<0]@SEEK_SET ==>> ^ValueError
Traceback (most recent call last):
    ...
ValueError: negative seek value -1
>>> ibfile.seek(-999, SEEK_CUR) #[new_location4tell<0]@SEEK_CUR <==> [new_location4tell==0]
0
>>> ibfile.seek(-999, SEEK_END) #[new_location4tell<0]@SEEK_END <==> [new_location4tell==0]
0
>>> ibfile.seek(999) #[new_location4tell>sz4file] is ok
999
>>> ibfile.tell()
999
>>> len(ibfile.getvalue())
16

from above:
#seek:[new_location4tell>sz4file] is ok
#seek:[seek:new_location4tell<0]@SEEK_SET ==>> ^ValueError
#seek:[new_location4tell<0]@SEEK_CUR/SEEK_END <==> [new_location4tell==0]
#seek:using operator.__index__ to convert 2 input: `offset` & `whence`

>>> ibfile.seek(999)
999
>>> ibfile.truncate()
999
>>> len(ibfile.getvalue())
16
>>> ibfile.tell()
999
>>> ibfile.truncate(999)
999

truncate(None) <==> truncate(tell())
>>> ibfile.truncate(None)
999
>>> len(ibfile.getvalue())
16
>>> ibfile.write(b'1')
1
>>> len(ibfile.getvalue())
1000
>>> ibfile.tell()
1000
>>> ibfile.seek(1009)
1009
>>> len(ibfile.getvalue())
1000
>>> ibfile.tell()
1009
>>> ibfile.write(b'1')
1
>>> len(ibfile.getvalue())
1010
>>> ibfile.tell()
1010
>>> ibfile.seek(1019)
1019
>>> ibfile.seek(1010)
1010
>>> ibfile.write(b'1')
1
>>> len(ibfile.getvalue())
1011
>>> ibfile.tell()
1011


truncate(>=sz4file) ==>> not change seek(0, SEEK_END)result
truncate(>=sz4file) ==>> not change tell()result
truncate(>=sz4file) ==>> not padding
truncate(>=sz4file) <==> no-op echo
>>> ibfile.truncate(1029)
1029
>>> len(ibfile.getvalue()) #not padding
1011
>>> ibfile.tell() #not change tell()result
1011
>>> ibfile.seek(0, SEEK_END) #not change seek(0, SEEK_END)result
1011
>>> ibfile.write(b'1')
1
>>> len(ibfile.getvalue())
1012
>>> ibfile.tell()
1012


>>> ibfile.seek(0, SEEK_END)
1012

truncate(<0) --> ^ValueError
>>> ibfile.truncate(-1)
Traceback (most recent call last):
    ...
ValueError: negative size value -1

truncate() not change tell()result
>>> ibfile.truncate(0)
0
>>> len(ibfile.getvalue())
0
>>> ibfile.tell()
1012
>>> ibfile.seek(0, SEEK_END)
0
>>> ibfile.truncate(999)
999
>>> ibfile.seek(0, SEEK_END)
0

from above:
truncate(None) <==> truncate(tell())
truncate(>=sz4file) <==> no-op echo
truncate(<0) --> ^ValueError
truncate() not change tell()result



readline()@>=eof not change tell()result
>>> ibfile.seek(1012)
1012
>>> len(ibfile.getvalue())
0
>>> ibfile.readline()
b''
>>> ibfile.tell()
1012

readline(0) not change tell()result
>>> ibfile.readline(0)
b''
>>> ibfile.tell()
1012
>>> ibfile.seek(0)
0
>>> ibfile.write(b'0123456789abcdef')
16
>>> ibfile.tell()
16
>>> ibfile.seek(0)
0

readline(<0) <==> readline(None) <==> readline()
>>> ibfile.readline(-999)
b'0123456789abcdef'
>>> ibfile.seek(0)
0
>>> ibfile.readline(None)
b'0123456789abcdef'
>>> ibfile.seek(0)
0
>>> ibfile.readline()
b'0123456789abcdef'
>>> ibfile.seek(0)
0
>>> ibfile.readline(0)
b''
>>> ibfile.seek(0)
0

readline(1)@<eof change tell()result
>>> ibfile.readline(1)
b'0'
>>> ibfile.tell()
1
>>> ibfile.readline('')
Traceback (most recent call last):
    ...
TypeError: argument should be integer or None, not 'str'


from above:
readline(1)@<eof change tell()result
readline()@>=eof not change tell()result
readline(0) not change tell()result
readline(<0) <==> readline(None) <==> readline()


>>> ibfile.seek(0)
0
>>> ibfile.readlines(0)
[b'0123456789abcdef']
>>> ibfile.seek(0)
0
>>> ibfile.readlines(1)
[b'0123456789abcdef']
>>> ibfile.seek(0)
0
>>> ibfile.readlines(-999)
[b'0123456789abcdef']
>>> ibfile.seek(0)
0
>>> ibfile.readlines(None)
[b'0123456789abcdef']

>>> bs = b'\n12345\n789abcdef'
>>> ibfile = BytesIO(bs)


readlines(>0) ==>> readline(-1) until new_location4tell-old_location4tell>=hint
>>> ibfile.seek(0)
0
>>> ibfile.readlines(1)
[b'\n']
>>> ibfile.seek(0)
0
>>> ibfile.readlines(2)
[b'\n', b'12345\n']
>>> ibfile.seek(0)
0
>>> ibfile.readlines(7)
[b'\n', b'12345\n']
>>> ibfile.seek(0)
0
>>> ibfile.readlines(8)
[b'\n', b'12345\n', b'789abcdef']
>>> ibfile.seek(0)
0

readlines() <==> readlines(0) <==> readlines(<0) <==> readlines(None)
>>> ibfile.seek(0)
0
>>> ibfile.readlines()
[b'\n', b'12345\n', b'789abcdef']
>>> ibfile.seek(0)
0
>>> ibfile.readlines(0)
[b'\n', b'12345\n', b'789abcdef']
>>> ibfile.seek(0)
0
>>> ibfile.readlines(-999)
[b'\n', b'12345\n', b'789abcdef']
>>> ibfile.seek(0)
0
>>> ibfile.readlines(None)
[b'\n', b'12345\n', b'789abcdef']


类型错+结束
readlines()@>=eof --> []
>>> ibfile.tell()
16
>>> ibfile.readlines(None)
[]

vs:
    >>> ibfile.readline('')
    Traceback (most recent call last):
        ...
    TypeError: argument should be integer or None, not 'str'
>>> ibfile.readlines('')
Traceback (most recent call last):
    ...
TypeError: integer argument expected, got 'str'


from above:
readlines()@>=eof --> []
readlines(>0) ==>> readline(-1) until new_location4tell-old_location4tell>=hint
readlines() <==> readlines(0) <==> readlines(<0) <==> readlines(None)



    def __next__(sf, /):
        试试BytesIO

>>> ibfile.seek(0)
0
>>> next(ibfile)
b'\n'
>>> ibfile.__next__()
b'12345\n'
>>> iter(ibfile) is ibfile
True


writelines
类型错
>>> ibfile.truncate(0)
0
>>> ibfile.tell()
7
>>> ibfile.seek(5)
5
>>> ibfile.seek(0,SEEK_END)
0
>>> ibfile.seek(5)
5
>>> ibfile.tell()
5
>>> ibfile.writelines(b'')
>>> ibfile.writelines('')
>>> ibfile.writelines([])
>>> len(ibfile.getvalue())
0
>>> ibfile.tell()
5
>>> ibfile.writelines([b''])
>>> len(ibfile.getvalue()) #no padding on write empty bytes
0
>>> ibfile.tell()
5
>>> ibfile.writelines([b'=', ''])
Traceback (most recent call last):
    ...
TypeError: a bytes-like object is required, not 'str'
>>> len(ibfile.getvalue())
6
>>> ibfile.tell()
6
>>> (ibfile.getvalue()) #padding on write nonempty bytes
b'\x00\x00\x00\x00\x00='
>>> memoryview('') #not using memoryview!!!
Traceback (most recent call last):
    ...
TypeError: memoryview: a bytes-like object is required, not 'str'
>>> check_bytes_like_object('')
Traceback (most recent call last):
    ...
TypeError: a bytes-like object is required, not 'str'
>>> ibfile.writelines()
Traceback (most recent call last):
    ...
TypeError: BytesIO.writelines() takes exactly one argument (0 given)
>>> ibfile.writelines(0)
Traceback (most recent call last):
    ...
TypeError: 'int' object is not iterable
>>> iter(0)
Traceback (most recent call last):
    ...
TypeError: 'int' object is not iterable


>>> ibfile.writelines([b'\n', b'=', b'+']) #writelines(...) -> None
>>> (ibfile.getvalue()) #no extra newline inserted
b'\x00\x00\x00\x00\x00=\n=+'


from above:
writelines(Iter<bytes_like_object>) -> None
writelines(...) no extra newline inserted
writelines(...) no padding on write empty bytes
writelines(...) padding on write nonempty bytes
    #iter+check_bytes_like_object

'''
r'''
>>> bs = b'0123456789abcdef'
>>> ibfile = BytesIO(bs)

>>> r_bs = bytes(reversed(bs))
>>> r_ibfile = BytesIO(r_bs)
>>> r_ibfile.seek(999)
999

#>>> rr_ibfile = mk_ReversedBufferedReader(r_ibfile)
#    BufferedReader closed@init() ??? why??
>>> rr_ibfile = ReversedRawIO(r_ibfile)
>>> rr_ibfile.tell()
0
>>> r_ibfile.seek(0)
0
>>> rr_ibfile = ReversedRawIO(r_ibfile)
>>> rr_ibfile.tell()
16



>>> ibfile.writable()
True
>>> rr_ibfile.writable()
False

#{ibfile_test}

#{r_bfile_test}

'''#'''

_x_ibfile_test = r'''


>>> x_ibfile.closed
False
'''     
r'''
>>> x_ibfile.fileno()
Traceback (most recent call last):
    ...
io.UnsupportedOperation: fileno
>>> x_ibfile.flush()
>>> x_ibfile.isatty()
False
>>> x_ibfile.readable()
True
>>> x_ibfile.seekable()
True
>>> x_ibfile.seek(0)
0
>>> x_ibfile.tell()
0
>>> x_ibfile.seek([])
Traceback (most recent call last):
    ...
TypeError: 'list' object cannot be interpreted as an integer
>>> x_ibfile.seek(-1)
Traceback (most recent call last):
    ...
ValueError: negative seek value -1
>>> x_ibfile.seek(-1, SEEK_CUR)
0
>>> x_ibfile.seek(-1, SEEK_END)
15
>>> x_ibfile.seek(-1, SEEK_SET)
>>> x_ibfile.seek(None, SEEK_SET)
>>> x_ibfile.seek(-999, SEEK_CUR)
0
>>> x_ibfile.seek(-999, SEEK_END)
0
>>> x_ibfile.seek(17, SEEK_END)
33
>>> x_ibfile.seek(17, SEEK_CUR)
50
>>> x_ibfile.seek(17, SEEK_SET)
17

>>> x_ibfile.seek(0, 3)
Traceback (most recent call last):
    ...
ValueError: invalid whence (3, should be 0, 1 or 2)
>>> x_ibfile.seek(0, '')
Traceback (most recent call last):
    ...
TypeError: 'str' object cannot be interpreted as an integer
>>> __index__('')
Traceback (most recent call last):
    ...
TypeError: 'str' object cannot be interpreted as an integer





>>> x_ibfile.closed
False
>>> x_ibfile.close()
>>> x_ibfile.closed
True

#after-close()
>>> x_ibfile.fileno()
Traceback (most recent call last):
    ...
io.UnsupportedOperation: fileno
>>> x_ibfile.flush()
Traceback (most recent call last):
    ...
ValueError: I/O operation on closed file.
>>> x_ibfile.isatty()
Traceback (most recent call last):
    ...
ValueError: I/O operation on closed file.
>>> x_ibfile.readable()
Traceback (most recent call last):
    ...
ValueError: I/O operation on closed file.
>>> x_ibfile.seekable()
Traceback (most recent call last):
    ...
ValueError: I/O operation on closed file.
>>> x_ibfile.writable()
Traceback (most recent call last):
    ...
ValueError: I/O operation on closed file.
>>> x_ibfile.seek(0)
Traceback (most recent call last):
    ...
ValueError: I/O operation on closed file.
>>> x_ibfile.tell()
Traceback (most recent call last):
    ...
ValueError: I/O operation on closed file.

>>> x_ibfile.close()#close again



'''#'''
if 0:
    __doc__ = (__doc__.format
(r_ibfile_test = _x_ibfile_test.replace('x_ibfile', 'rr_ibfile')
,ibfile_test = _x_ibfile_test.replace('x_ibfile', 'ibfile')
))
#__doc__ = __doc__ + _x_ibfile_test.replace('x_ibfile', 'rr_ibfile') + _x_ibfile_test.replace('x_ibfile', 'ibfile')
del _x_ibfile_test
r'''end-__doc__
#]]]'''
__all__ = r'''
    IBaseIO
'''.split()#'''
__all__

from seed.mapping_tools.dict_op import set_symmetric_partition__immutable
from seed.tiny import print_err, check_uint, check_tmay, curry1, check_callable, check_is_None, check_imay, check_type_is, check_pair
from seed.tiny_.check import check_str, check_char, check_bool, check_uint_lt
from seed.tiny_.check import icheck_str, icheck_char, icheck_bool
from seed.abc.abc import ABC, abstractmethod
from seed.helper.repr_input import repr_helper
from seed.io.get_size_of_ibfile import get_size_of_ibfile, get_size_of_ibfile_ex, explain_may_negativeable_end_locations_of_ibfile_ex, explain_negativeable_location_of_ibfile_ex, explain_may_negativeable_location_rng_of_ibfile_ex #; #may have [len(ibfile) < end_location]

from os import SEEK_SET, SEEK_CUR, SEEK_END
from operator import __index__
from io import BufferedReader, RawIOBase, IOBase, DEFAULT_BUFFER_SIZE, UnsupportedOperation
dir(RawIOBase())
['__IOBase_closed'
, '__abstractmethods__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__'
, '_abc_impl', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable'
, 'close', 'closed', 'fileno', 'flush', 'isatty', 'read', 'readable', 'readall', 'readinto', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines'
]



__index__
#def __as_size__(obj, /):
def as_uint_(nm, obj, /):
    i = __index__(obj)
        # ^ValueError
    if i < 0:
        raise ValueError(f'negative {nm!s} value {i!r}')
    u = i
    check_uint(u)
    return u
def check_bytes_like_object(bytes_like_object, /):
    try:
        with memoryview(bytes_like_object):pass
    except TypeError as e:
        [err_msg] = e.args
        prefix = 'memoryview: '
        if not err_msg.startswith(prefix):raise logic-err
        err_msg = err_msg[len(prefix):]
        raise TypeError(err_msg) from e
    #TypeError: memoryview: a bytes-like object is required, not 'str'
    #TypeError: a bytes-like object is required, not 'str'
    return
def icheck_iter_bytes_like_objects(bytes_like_objects, /):
    return _icheck_iter__(check_bytes_like_object, bytes_like_objects)
def _check_str(s, /):
    check_type_is(str, s)
def _icheck_iter_strs(strs, /):
    return _icheck_iter__(_check_str, strs)
def _icheck_iter__(check_, xs, /):
    for x in xs:
        check_(x)
        yield x

def prepare4seek_(lazy_sz4file, lazy_old_location4tell, offset, whence, /):
    '(()->sz4file) -> (()->old_location4tell) -> offset/int -> whence/{os.SEEK_*} -> new-location4tell/uint #maybe [old/new-location4tell > sz4file]'
        #seek:[new_location4tell>sz4file] is ok
        #seek:[seek:new_location4tell<0]@SEEK_SET ==>> ^ValueError
        #seek:[new_location4tell<0]@SEEK_CUR/SEEK_END <==> [new_location4tell==0]
        #seek:using operator.__index__ to convert 2 input: `offset` & `whence`
    offset = __index__(offset)
            # ^ValueError
    whence = __index__(whence)
            # ^ValueError
    if not 0 <= whence < 3:
        raise ValueError(f'invalid whence ({whence!r}, should be 0, 1 or 2)')
    if whence==SEEK_SET:
        u = as_uint_('seek', offset)
            # ^ValueError
            #maybe [u > sz4file]
    elif whence==SEEK_CUR:
        old_location4tell = lazy_old_location4tell()
        check_uint(old_location4tell)
        u = max(0, old_location4tell+offset)
    elif whence==SEEK_END:
        sz4file = lazy_sz4file()
        check_uint(sz4file)
        u = max(0, sz4file + offset)
    else:
        raise logic-err
    check_uint(u)
    new_location4tell = u
    return new_location4tell

def _isize5may_isize(may_isize, /):
    if may_isize is None:
        isz = -1
    else:
        isz = may_isize
    isz
    if not type(isz) is int:
        raise TypeError("argument should be integer or None, not 'str'")
    return isz
def _imay_size5may_isize(may_isize, /):
    isz = _isize5may_isize(may_isize); del may_isize
    if isz < 0:
        imay_sz = -1
    else:
        sz = isz
        imay_sz = sz
    return imay_sz

if 1:
    #since check readable/seekable/writable ^UnsupportedOperation
    #   otherwise MUST impl the method
    Err4NotImplemented = NotImplementedError
else:
    Err4NotImplemented = UnsupportedOperation


class _GetOp:
    def __init__(sf, obj, nm4op, /):
        sf._obj = obj
        sf._nm4op = nm4op
    def __getattribute__(sf, nm4attr, /):
        obj = object.__getattribute__(sf, '_obj')
        nm4op = object.__getattribute__(sf, '_nm4op')
        return _get_method(obj, nm4op, nm4attr)
def _get_method(sf, nm4op, nm4attr, /):
    'must exist, but can be None'
    may_f = getattr(sf, nm4attr)
    if may_f is None:
        raise UnsupportedOperation(nm4op)
        raise Err4NotImplemented(nm4op)
        raise NotImplementedError(nm4op)
    f = may_f
    check_callable(f)
    return f

_line_sep_tuple_and_default_idx4binary_file = (b'\n',), 0

class IBaseIO(ABC):
    r'''
    mimic:io.IOBase

    =====now:
    ^UnsupportedOperation@_check_*able(...)/_check_readable before ^ValueError@_check_not_closed()
    =====Deprecated:
    xxx ^ValueError@_check_not_closed() before ^UnsupportedOperation@_check_*able(...)/_check_readable
        see:fileno()
        if sf is a file wrapper:
            after detach wrapped file, will donot known .readable(), is_binary_file()...
        [_check_readable() depends on readable() to determine whether ^UnsupportedOperation][readable()^ValueError@closed] ==>> [_check_readable() should ^ValueError before ^UnsupportedOperation]
        but py:!!!_check_writable before _check_not_closed!!!
            since UnsupportedOperation <: (OSError|ValueError)
            xxx none sense, IBaseIO donot follow py std io here!!! xxx
                cancelled
                NOTE:fileno
                    if UnsupportedOperation, should set sf._get_fileno_=None



all abstractmethod except _is_closed_ is called only when [not sf.closed]

all abstractmethod cannot be set None!
    but other method named regex'_\w*_' can be set None in cls or in sf to raise UnsupportedOperation (via _GetOp or fileno())
[[
this section generated by:『seed.helper.print_methods:wrapped_print_methods』
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.io.ReversedBufferedReader   @print_methods_of_IBaseIO
py -m nn_ns.app.adhoc_argparser__main__call8module  seed.helper.print_methods  @wrapped_print_methods   %seed.io.ReversedBufferedReader:IBaseIO  =IBaseIO
    TODO！！
[[===[[
new_abstract_methods:
    `_is_closed_
    `_close_
    `_isatty_
    `_is_readable_
    `_is_seekable_
    `_is_writable_
    `_get_may__line_sep_tuple_and_default_idx_
new_concrete_methods:
    _get_fileno_
    _readline_
    _tell_
    _seek_
    _truncate_
    _flush_
    _write_xstring_
    _is_debug_mode_
    _check_not_closed
    closed
    close
    __enter__
    __exit__
    __del__
    isatty
    fileno
    readable
    seekable
    writable
    _check_readable
    _check_seekable
    _check_writable
    __next__
    __iter__
    readlines
    get_line_sep_tuple_and_default_idx
    get_may__line_sep_tuple_and_default_idx
    is_binary_file
    is_text_file
    is_debug_mode
    _readline
    readline
    _check4readline
    tell
    seek
    get_file_size
    is_tell_ge_eof__tribool
    truncate
    flush
    writelines
]]===]]

]]

[[
`_is_closed_ #below abstractmethod protected by [not sf.closed]
    `_close_
    `_isatty_
    `_is_readable_
    `_is_seekable_
    `_is_writable_
    `_get_may__line_sep_tuple_and_default_idx_

new_concrete_methods that be None to ^UnsupportedOperation:
    _get_fileno_
    _readline_
    _tell_
    _seek_
    _truncate_
    _flush_
    _write_xstring_

new_concrete_methods that override with default_impl:
    _is_debug_mode_

new_concrete_methods that not intended to be override, as-if final but not final:
closed
    _check_not_closed
    close
        __enter__
        __exit__
        __del__

isatty

fileno

readable
    _check_readable
    readline
        __next__
        __iter__
            readlines
        _readline
        _check4readline
            is_debug_mode
            get_may__line_sep_tuple_and_default_idx
                get_line_sep_tuple_and_default_idx
                is_binary_file
                is_text_file
seekable
    _check_seekable
    tell
    seek
        get_file_size
        is_tell_ge_eof__tribool
    truncate #---1
writable
    _check_writable
    truncate #---2
    flush
    writelines

]]

    '''#'''
    __slots__ = ()
    assert issubclass(UnsupportedOperation, OSError)
    assert issubclass(UnsupportedOperation, ValueError)
    assert not issubclass(OSError, ValueError)
    #print(UnsupportedOperation.__mro__)
    #(<class 'io.UnsupportedOperation'>, <class 'OSError'>, <class 'ValueError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
    assert UnsupportedOperation.__mro__ == (UnsupportedOperation, OSError, ValueError, Exception, BaseException, object)
    if 0:
        def _does_unsupported_operation_raise_UnsupportedOperation_instead__ValueError_when_closed_(sf, /):
            '-> bool #True=>Python std io behavior'
            return False
            return True


    def _get_fileno_(sf, /):
        '[not sf.closed] => sf -> tmay file_descriptor'
        raise Err4NotImplemented('_get_fileno_')
    def _readline_(sf, imay_nonzero_size, /):
        '[not sf.closed][sf.readable()] => sf -> imay_nonzero_size/int{==-1 or >0} -> xstring/(bytes|str){len<=imay_nonzero_size[#-1 as +oo#]} #endby b"\n" or ...'
        raise Err4NotImplemented('_readline_')
    def _tell_(sf, /):
        '[not sf.closed][sf.seekable()] => sf -> location4tell/uint #current stream position'
        raise Err4NotImplemented('_tell_')
    def _seek_(sf, new_location4tell, /):
        '[not sf.closed][sf.seekable()] => sf -> new_location4tell/uint -> None #maybe [old/new-location4tell > sz4file]'
        raise Err4NotImplemented('_seek_')
    def _truncate_(sf, new_sz4file, /):
        '[not sf.closed][sf.seekable()][sf.writable()] => sf -> new_sz4file/uint -> None #[0 <= new_sz4file < old_sz4file] #truncate() not change tell()result'
        raise Err4NotImplemented('_truncate_')
    def _flush_(sf, /):
        '[not sf.closed][sf.writable()] => sf -> None|^BlockingIOError-raw-stream-block'
        raise Err4NotImplemented('_flush_')
    def _write_xstring_(sf, xstring, /):
        '[not sf.closed][sf.writable()] => sf -> Iter<bytes|str> -> None #no extra line_sep appended'
        raise Err4NotImplemented('_write_xstring_')

    @property
    def _get_fileno_(sf, /):
        '-> (None | ([not sf.closed] => {sf ->} -> tmay file_descriptor)) #None => ^UnsupportedOperation'
        return None #or to use non-property-method or return below example:
        def _get_fileno_(sf, /):
            ...
            return ...
        return curry1(_get_fileno_, sf)
    @property
    def _readline_(sf, /):
        '-> None | ([not sf.closed][sf.readable()] => {sf ->} imay_nonzero_size/int{==-1 or >0} -> xstring/(bytes|str){len<=imay_nonzero_size[#-1 as +oo#]}) #line endby b"\n" or ... #None => ^UnsupportedOperation'
        return None
    _get_fileno_ = None
    _readline_ = None
    _tell_ = None
    _seek_ = None
    _truncate_ = None
    _flush_ = None
    _write_xstring_ = None






    @abstractmethod
    def _is_closed_(sf, /):
        '-> bool #return True cause _check_not_closed() fail'
        raise NotImplementedError('_is_closed_')
            #not Err4NotImplemented
            #NotImplementedError <<== abstractmethod
    @abstractmethod
    def _close_(sf, /):
        '[not sf.closed] => sf -> None #allow called more than once #make _is_closed_() return True'
        raise NotImplementedError('_close_')
            #not Err4NotImplemented
            #NotImplementedError <<== abstractmethod
    @abstractmethod
    def _isatty_(sf, /):
        '[not sf.closed] => sf -> bool #return whether [the stream is interactive (i.e., connected to a terminal/tty device)]'
        raise NotImplementedError('_isatty_')
            #not Err4NotImplemented
            #NotImplementedError <<== abstractmethod
    @abstractmethod
    def _is_readable_(sf, /):
        '[not sf.closed] => sf -> bool #False => [read*() will raise OSError/io.UnsupportedOperation]'
        raise NotImplementedError('_is_readable_')
            #not Err4NotImplemented
            #NotImplementedError <<== abstractmethod
    @abstractmethod
    def _is_seekable_(sf, /):
        '[not sf.closed] => sf -> bool #whether [stream supports random access] #False => [seek(), tell(), truncate() will raise OSError/io.UnsupportedOperation]'
        raise NotImplementedError('_is_seekable_')
            #not Err4NotImplemented
            #NotImplementedError <<== abstractmethod
    @abstractmethod
    def _is_writable_(sf, /):
        '[not sf.closed] => sf -> bool #False => [write*(), truncate() will raise OSError/io.UnsupportedOperation]'
        raise NotImplementedError('_is_writable_')
            #not Err4NotImplemented
            #NotImplementedError <<== abstractmethod
    @abstractmethod
    def _get_may__line_sep_tuple_and_default_idx_(sf, /):
        '[not sf.closed] => sf -> may (line_sep_tuple/tuple<line_sep/str>, idx4default_line_sep/uint) #[default_line_sep == line_sep_tuple[idx4default_line_sep]] #binary file return None #line_sep===b"\n"'
        raise NotImplementedError('_get_may__line_sep_tuple_and_default_idx_')
            #not Err4NotImplemented
            #NotImplementedError <<== abstractmethod



    def _is_debug_mode_(sf, /):
        '[not sf.closed] => sf -> bool'
        return True

    def _check_not_closed(sf, nm=None, /):
        ##'nm is only set by _check_readable/_check_writable/_check_seekable'
        if sf.closed:
            if 0 and nm:
                #to let ^UnsupportedOperation before ^ValueError@closed
                raise UnsupportedOperation(nm)
            raise ValueError('I/O operation on closed file.')



    @property
    def closed(sf, /):
        '-> bool'
        return icheck_bool(sf._is_closed_())
            #no _GetOp <<== abstractmethod
    def close(sf, /):
        '-> None'
        if not sf.closed:
            try:
                if sf.writable():
                    sf.flush()
            finally:
                check_is_None(sf._close_())
                #no _GetOp <<== abstractmethod
        if not sf.closed:raise logic-err
        return None
    def __enter__(sf, /):
        nm = '__enter__'
        sf._check_not_closed(nm)
        return sf
    def __exit__(sf, exc_type, exc_value, traceback, /):
        #sf._check_not_closed(nm)
        sf.close()
        return None #==>> reraise
    def __del__(sf, /):
        sf.close()




    def isatty(sf, /):
        '-> bool|^ValueError-closed #return whether [the stream is interactive (i.e., connected to a terminal/tty device)]'
        nm = 'isatty'
        sf._check_not_closed(nm)
        return icheck_bool(sf._isatty_())
            #no _GetOp <<== abstractmethod
    def fileno(sf, /):
        '-> file_descriptor/uint|^OSError-not-file|^ValueError-closed'
        nm = 'fileno'
        _get_fileno_ = _GetOp(sf,nm)._get_fileno_
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)

        tmay_file_descriptor = _get_fileno_()
        check_tmay(tmay_file_descriptor)
        if tmay_file_descriptor:
            [file_descriptor] = tmay_file_descriptor
            check_uint(file_descriptor)
            return file_descriptor
        else:
            [] = tmay_file_descriptor
            raise UnsupportedOperation(nm)
                    #not Err4NotImplemented



    def readable(sf, /):
        'readable() -> bool|^ValueError #False => [read*() will raise OSError/io.UnsupportedOperation]'
        nm = 'readable'

        sf._check_not_closed(nm)
        return icheck_bool(sf._is_readable_())
            #no _GetOp <<== abstractmethod
    def seekable(sf, /):
        'seekable() -> bool|^ValueError #whether [stream supports random access] #False => [seek(), tell(), truncate() will raise OSError/io.UnsupportedOperation]'
        nm = 'seekable'
        sf._check_not_closed(nm)
        return icheck_bool(sf._is_seekable_())
            #no _GetOp <<== abstractmethod
    def writable(sf, /):
        'writable() -> bool|^ValueError #False => [write*(), truncate() will raise OSError/io.UnsupportedOperation]'
        nm = 'writable'

        sf._check_not_closed(nm)
        return icheck_bool(sf._is_writable_())
            #no _GetOp <<== abstractmethod


    def _check_readable(sf, nm, /):
        sf._check_not_closed(nm)
        if not sf.readable():
            raise UnsupportedOperation(nm)
                    #not Err4NotImplemented
    def _check_seekable(sf, nm, /):
        sf._check_not_closed(nm)
        if not sf.seekable():
            raise UnsupportedOperation(nm)
                    #not Err4NotImplemented
    def _check_writable(sf, nm, /):
        sf._check_not_closed(nm)
        if not sf.writable():
            raise UnsupportedOperation(nm)
                    #not Err4NotImplemented










    def __next__(sf, /):
        nm = '__next__'
        sf._check_not_closed(nm)
        smay_line = sf.readline(-1)
        if not smay_line:
            raise StopIteration
        line = smay_line
        return line
    def __iter__(sf, /):
        nm = '__iter__'
        sf._check_not_closed(nm)
        return sf
        #bug:readlines()->list<bytes>
        return sf.readlines()

    #def readlines(sf, hint=-1, /):
    def readlines(sf, min_positive_num_elems4read___or___may_zero_or_neg8inf=-1, /):
        '-> [xstring]|^UnsupportedOperation-not-readable|^ValueError-closed'
        nm = 'readlines'
        sf._check_readable(nm)
        sf._check_not_closed(nm)
        hint = min_positive_num_elems4read___or___may_zero_or_neg8inf
        #readlines()@>=eof --> []
        #readlines(>0) ==>> readline(-1) until new_location4tell-old_location4tell>=hint
        #readlines() <==> readlines(0) <==> readlines(<0) <==> readlines(None)
        ihint = _isize5may_isize(hint)
        if ihint <= 0:
            #min_sz = inf # +oo
            def to_stop_by_hint_(xs, /):
                return False
        else:
            min_sz = hint
            sz4acc = 0
            def to_stop_by_hint_(xs, /):
                sz4acc += len(xs)
                return sz4acc >= min_sz
        to_stop_by_hint_
        xss = []
        for xs in sf:
            xss.append(xs)
            if to_stop_by_hint_(xs):
                break
        assert type(xss) is list
        return xss




    def get_line_sep_tuple_and_default_idx(sf, /):
        '-> (line_sep_tuple/[xstring], default_idx/uint)|^ValueError-closed #[default_line_sep == line_sep_tuple[default_idx]]'
        nm = 'get_line_sep_tuple_and_default_idx'
        sf._check_not_closed(nm)
        m = sf.get_may__line_sep_tuple_and_default_idx()
        if m is None:
            return _line_sep_tuple_and_default_idx4binary_file
        line_sep_tuple_and_default_idx4text_file = m
        return line_sep_tuple_and_default_idx4text_file
    def get_may__line_sep_tuple_and_default_idx(sf, /):
        '-> may (line_sep_tuple/[str], default_idx/uint)|^ValueError-closed #None => is_binary_file #True => is_text_file && [default_line_sep == line_sep_tuple[default_idx]]'
        nm = 'get_may__line_sep_tuple_and_default_idx'
        sf._check_not_closed(nm)
        m = sf._get_may__line_sep_tuple_and_default_idx_()
            #no _GetOp <<== abstractmethod
        if not m is None:
            #is_text_file
            line_sep_tuple_and_default_idx = m
            check_pair(line_sep_tuple_and_default_idx)
            if sf.is_debug_mode():
                line_sep_tuple, default_idx = line_sep_tuple_and_default_idx
                check_type_is(tuple, line_sep_tuple)
                check_uint_lt(len(line_sep_tuple), default_idx)
                default_line_sep = line_sep_tuple[default_idx]
                check_type_is(str, default_line_sep)
                for line_sep in line_sep_tuple:
                    check_type_is(str, line_sep)
                    if not line_sep: raise TypeError
        return m


    def is_binary_file(sf, /):
        '-> bool|^ValueError-closed '
        nm = 'is_binary_file'
        sf._check_not_closed(nm)
        return None is sf.get_may__line_sep_tuple_and_default_idx()
    def is_text_file(sf, /):
        '-> bool|^ValueError-closed '
        nm = 'is_text_file'
        sf._check_not_closed(nm)
        return not sf.is_binary_file()

    def is_debug_mode(sf, /):
        '-> bool|^ValueError-closed '
        nm = 'is_debug_mode'
        sf._check_not_closed(nm)
        return icheck_bool(sf._is_debug_mode_())
            # no _GetOp <<== default method
    def _readline(sf, _readline_, imay_nonzero_size, /):
        '[not sf.closed] => sf -> imay_nonzero_size/int{==-1 or >0} -> xstring/(bytes|str){len<=imay_nonzero_size[#-1 as +oo#]} #endby b"\n" or ...'
        _binary_seekable = sf.is_binary_file() and sf.seekable()
        if _binary_seekable:
            old_location4tell = sf.tell()
        xs = _readline_(imay_nonzero_size)
        if _binary_seekable:
            new_location4tell = sf.tell()
        line_sep_tuple, default_idx = sf.get_line_sep_tuple_and_default_idx()
        default_line_sep = line_sep_tuple[default_idx]
        T = type(default_line_sep)
        check_type_is(T, xs) #bytes|str
        if not (imay_nonzero_size == -1 or len(xs) <= imay_nonzero_size):raise logic-err
        if _binary_seekable:
            #is_binary_file
            #   excluded text_file: location4tell is opaque_number
            if not T is bytes:raise logic-err
            if not new_location4tell-old_location4tell==len(xs):raise logic-err
        return xs, line_sep_tuple, T


    def readline(sf, may_isize=-1, /):
        '-> xstring/(bytes|str)|^UnsupportedOperation-not-readable|^ValueError-closed'
        nm = 'readline'
        _readline_ = _GetOp(sf,nm)._readline_
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_readable(nm)
        sf._check_not_closed(nm)

        #readline(1)@<eof change tell()result
        #readline()@>=eof not change tell()result
        #readline(0) not change tell()result
        #readline(<0) <==> readline(None) <==> readline()
        #binary file line_sep===b'\n'
        #text file line_sep <<== open(newline=...)
        imay_sz = _imay_size5may_isize(may_isize); del may_isize
            #check input type
        if sf.is_tell_ge_eof__tribool() is True:
            #no-op if tell()>=eof
            return b'' if sf.is_binary_file() else ''
        if imay_sz == 0:
            #no-op if sz==0
            return b'' if sf.is_binary_file() else ''
        imay_nonzero_size = imay_sz; del imay_sz
        check_imay(imay_nonzero_size)
        assert not imay_nonzero_size == 0
        xs, line_sep_tuple, T = sf._readline(_readline_, imay_nonzero_size)
            # no _GetOp <<== private method
        if sf.is_debug_mode():
            sf._check4readline(imay_nonzero_size, xs, line_sep_tuple, T)
            # no _GetOp <<== private method
        return xs
    def _check4readline(sf, imay_nonzero_size, xs, line_sep_tuple, T, /):
        assert not sf.is_tell_ge_eof__tribool() is True
        check_imay(imay_nonzero_size)
        assert not imay_nonzero_size == 0

        tmay__line_sep_and_idx5find = []
        for line_sep in line_sep_tuple:
            #imay_idx5find = xs.find(b'\n')
            imay_idx5find = xs.find(line_sep)
            if not imay_idx5find == -1:
                idx5find = imay_idx5find
                if tmay__line_sep_and_idx5find:
                    [(line_sep_, idx5find_)] = tmay__line_sep_and_idx5find
                    if not idx5find == idx5find_: raise logic-err
                    line_sep = max(line_sep, line_sep_)
                    tmay__line_sep_and_idx5find.pop()
                tmay__line_sep_and_idx5find.append((line_sep, idx5find))
        assert len(tmay__line_sep_and_idx5find) < 2

        #if imay_idx5find == -1:
        if not tmay__line_sep_and_idx5find:
            #no newline
            if not len(xs) == imay_nonzero_size:
                #SHOULD BE eof
                t = sf.is_tell_ge_eof__tribool()
                if t is False:
                    raise logic-err #not-eof
                elif t is ...:
                    _xs, _line_sep_tuple, _T = sf._readline(_readline_, 1)
                        # no _GetOp <<== private method
                    if _xs:raise logic-err #not-eof
                    if not _T is T:raise logic-err
                    if not _line_sep_tuple is line_sep_tuple:raise logic-err
                elif t is True:
                    pass#ok
                else:
                    raise logic-err #not-tribool
        else:
            #idx5find = imay_idx5find
            [(line_sep, idx5find)] = tmay__line_sep_and_idx5find
            #newline SHOULD BE last, only one
            if not idx5find == len(xs)-len(line_sep):raise logic-err
        return
    #end-def _check4readline(sf, imay_nonzero_size, xs, line_sep_tuple, T, /):





    def tell(sf, /):
        'tell() -> current stream position|^UnsupportedOperation-not-seekable|^ValueError-closed'
        nm = 'tell'
        _tell_ = _GetOp(sf,nm)._tell_
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_seekable(nm)
        sf._check_not_closed(nm)

        location4tell = _tell_()
        check_uint(location4tell)
        return location4tell

    def seek(sf, offset, whence=SEEK_SET, /):
        'offset/int -> whence/[0,1,2] -> new absolute position|^UnsupportedOperation-not-seekable|^ValueError-closed   #maybe [old/new-location4tell > sz4file]'
        nm = 'seek'
        _seek_ = _GetOp(sf,nm)._seek_
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_seekable(nm)
        sf._check_not_closed(nm)

        #seek:[new_location4tell>sz4file] is ok
        #seek:[seek:new_location4tell<0]@SEEK_SET ==>> ^ValueError
        #seek:[new_location4tell<0]@SEEK_CUR/SEEK_END <==> [new_location4tell==0]
        #seek:using operator.__index__ to convert 2 input: `offset` & `whence`

        lazy_sz4file = sf.get_file_size
        lazy_old_location4tell = sf.tell
        new_location4tell = prepare4seek_(lazy_sz4file, lazy_old_location4tell, offset, whence)
        check_is_None(_seek_(new_location4tell))
            #allow [new_location4tell > sz4file]
        if not sf.tell() == new_location4tell: raise logic-err
        return new_location4tell




    def get_file_size(sf, /):
        '-> sz4file|^ValueError-closed'
        nm = 'get_file_size'
        sf._check_not_closed(nm)
        return get_size_of_ibfile(sf)
    def is_tell_ge_eof__tribool(sf, /):
        '-> tribool|^ValueError-closed #unknown | (sf.get_file_size() <= sf.tell())'
        nm = 'is_tell_ge_eof__tribool'
        sf._check_not_closed(nm)
        try:
            sz4file = sf.get_file_size()
            location4tell = sf.tell()
        except UnsupportedOperation:
            return ...
        else:
            return sz4file <= location4tell


    def truncate(sf, may_size=None, /):
        'may size/uint{allow>=sz4file} -> new file size|^UnsupportedOperation-not-seekable&writable|^ValueError-closed'
        #truncate(None) <==> truncate(tell())
        #truncate(>=sz4file) <==> no-op echo
        #truncate(<0) --> ^ValueError
        #truncate() not change tell()result
        nm = 'truncate'
        _truncate_ = _GetOp(sf,nm)._truncate_
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_seekable(nm)
        sf._check_writable(nm)
        sf._check_not_closed(nm)

        if may_size is None:
            new_sz4file = sf.tell()
        else:
            obj = may_size
            new_sz4file = as_uint_('size', obj)
                # ^ValueError
        check_uint(new_sz4file)
        old_sz4file = sf.get_file_size()

        if not new_sz4file < old_sz4file:
            #no-op echo
            pass
        else:
            old_location4tell = sf.tell()
            check_is_None(_truncate_(new_sz4file))
            if not sf.tell() == old_location4tell: raise logic-err
                #truncate() not change tell()result
        return new_sz4file





    def flush(sf, /):
        'flush() -> None|^BlockingIOError-raw-stream-block|^UnsupportedOperation-not-writable|^ValueError-closed'
        nm = 'flush'
        _flush_ = _GetOp(sf,nm)._flush_
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_writable(nm)
        sf._check_not_closed(nm)

        check_is_None(_flush_())
        return None


    def writelines(sf, lines, /):
        '-> None|^UnsupportedOperation-not-writable|^ValueError-closed'
        nm = 'writelines'
        _write_xstring_ = _GetOp(sf,nm)._write_xstring_
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_writable(nm)
        sf._check_not_closed(nm)

        #writelines(Iter<bytes_like_object>) -> None
        #writelines(...) no extra newline inserted
        #writelines(...) no padding on write empty bytes
        #writelines(...) padding on write nonempty bytes
        #iter+check_bytes_like_object
        lines = iter(lines)
            #check type now

        _icheck_lines = icheck_iter_bytes_like_objects if sf.is_binary_file() else _icheck_iter_strs
        lines = _icheck_lines(lines)
                #check type later

        _binary_seekable = sf.is_binary_file() and sf.seekable()
        if _binary_seekable:
            old_location4tell = sf.tell()
        for xs in lines:
            #xs :: bytes | str
            check_is_None(_write_xstring_(xs)) #no extra line_sep appended
            if _binary_seekable:
                #is_binary_file
                #   excluded text_file: location4tell is opaque_number
                new_location4tell = sf.tell()
                if not new_location4tell-old_location4tell==len(xs):raise logic-err

                old_location4tell = new_location4tell
        return None



    'fileno seek truncate     close closed __enter__ __exit__ flush isatty __iter__ __next__ readable readline readlines seekable tell writable writelines'
    _GetOp



def __(T, /):
    nms = 'fileno seek truncate     close closed __enter__ __exit__ flush isatty __iter__ __next__ __del__ readable readline readlines seekable tell writable writelines'.split()
    nms = {*nms} - T.__dict__.keys()
    assert not nms, nms
    #print(IOBase.__mro__)
    #(<class 'io.IOBase'>, <class '_io._IOBase'>, <class 'object'>)
    bases = IOBase.__mro__
    if len(bases) == 3:
        _X, X, _ = bases
    elif len(bases) == 2:
        X, _ = bases
    else:
        assert 0, bases
    #bug:more, same, less = set_symmetric_partition__immutable(IBaseIO.__dict__.keys(), IOBase.__dict__.keys())
    more, same, less = set_symmetric_partition__immutable(IBaseIO.__dict__.keys(), X.__dict__.keys())
    more, same, less = set_symmetric_partition__immutable(IBaseIO.__dict__.keys(), set(dir(IOBase)))
    if 0:
        assert not less, less
        #AssertionError: frozenset({'__dir__', '__setattr__', '__delattr__', '__init__', '__lt__', '__init_subclass__', '_checkReadable', '__ge__', '__le__', '__repr__', '__hash__', '__eq__', '__reduce_ex__', '__class__', '_checkSeekable', '__dict__', '__ne__', '_checkWritable', '__gt__', '__new__', '__format__', '_checkClosed', '__reduce__', '__sizeof__', '__subclasshook__', '__getattribute__', '__str__'})
    assert all(nm.startswith('_') for nm in less)
    if 0:print((more, same, less))
__(IBaseIO)
#end-class IBaseIO(ABC):


def print_methods_of_IBaseIO():
    print_methods_of_(IBaseIO)
def print_methods_of_(XXX, /):
    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)
#if __name__ == '__main__':print_methods_of_IBaseIO()




































































































class ReversedRawIO(IBaseIO):
    #__slots__ = ()
    ___no_slots_ok___ = True
    def __init__(sf, seekable_ibfile, /):
        ibfile = sf._ibfile = seekable_ibfile
        if not (ibfile.readable() and ibfile.seekable()):raise TypeError
        if not ibfile.read(0)==b'':raise TypeError#str??
        sf._sz = get_size_of_ibfile(ibfile)
        #sf._i = sf._neg_tell()
            #int not uint
        sf._u = max(0, sf._neg_tell())
        super().__init__()
    def __repr__(sf, /):
        return repr_helper(sf, sf._ibfile)
    def __getattribute__(sf, nm, /):
        if nm in '_u _sz _ibfile      __IOBase_closed       _dealloc_warn name' or nm in __class__.__dict__:

            return super().__getattribute__(nm)
        print_err(nm)
        print(nm)
        def _xxx(*args, **kwargs):
            print_err(Exception(nm, args, kwargs))
            print(Exception(nm, args, kwargs))
            raise Exception(nm, args, kwargs)
        return _xxx


    @property
    def closed(sf, /):
        return sf._ibfile.closed
    def close(sf, /):
        sf._ibfile.close()
        return super().close()
    def _check_not_closed(sf, /):
        if sf.closed:
            raise ValueError('I/O operation on closed file.')
    def fileno(sf, /):
        #sf._check_not_closed(nm)
        raise UnsupportedOperation('fileno')
    def flush(sf, /):
        sf._check_not_closed(nm)
        return sf._ibfile.flush()
    def get_file_size(sf, /):
        sf._check_not_closed(nm)
        return sf._sz
    def tell(sf, /):
        sf._check_not_closed(nm)
        return sf._u
        return max(0, sf._i)
    def _neg_tell(sf, /):
        '-> int #not uint #since maybe [ibfile.tell() > eof==sf._sz]'
        ibfile = sf._ibfile
        sz = sf._sz
        return sz - ibfile.tell()
    def seek(sf, offset, /, whence=SEEK_SET):
        'seek(offset, whence=SEEK_SET) -> new absolute position|^UnsupportedOperation-not-seekable|^ValueError-closed'
        sf._check_not_closed(nm)
        sz = sf.get_file_size()
        u = prepare4seek_(sz, sf.tell(), offset, whence)
            #allow [u > sf._sz]
        sf._u = u
        return u

    def seekable(sf, /):
        sf._check_not_closed(nm)
        return True
    def readable(sf, /):
        sf._check_not_closed(nm)
        return True
    def writable(sf, /):
        sf._check_not_closed(nm)
        return False
    def isatty(sf, /):
        sf._check_not_closed(nm)
        return False


RawIOBase.register(ReversedRawIO)
def __(T, /):
    nms = {'close', 'closed', 'fileno', 'flush', 'isatty', 'read', 'readable', 'readall', 'readinto', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines'} - T.__dict__.keys()
    assert not nms, nms
#__(ReversedRawIO)

#def mk_ReversedBufferedReader(seekable_ibfile, /):
def mk_ReversedBufferedReader(seekable_ibfile, buffer_size=DEFAULT_BUFFER_SIZE, /):
    r = BufferedReader(ReversedRawIO(seekable_ibfile), buffer_size)
    assert seekable_ibfile.closed is r.closed
    return r




from seed.io.ReversedBufferedReader import *
