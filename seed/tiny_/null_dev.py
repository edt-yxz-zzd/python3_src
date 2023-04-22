#__all__:goto
r'''
e ../../python3_src/seed/tiny_/null_dev.py

mimic:
    /dev/null

view ../../python3_src/seed/io/ReversedBufferedReader.py
  IOBase-fail?


py -m nn_ns.app.debug_cmd  seed.tiny_.null_dev  -x
py -m nn_ns.app.doctest_cmd seed.tiny_.null_dev:__doc__ -ff


from seed.tiny_.null_dev import null_dev
from seed.tiny_.null_dev import null_context, null_context5result_
from seed.tiny_.null_dev import DEVNULL4subprocess
from seed.tiny_.null_dev import NullFileBase, NullOutputFile, null_dev, ParameterizedNullFileBase


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

#'''



__all__ = r'''
DEVNULL4subprocess
null_context
    null_context5result_
NullFileBase
    NullOutputFile
        null_dev
    ParameterizedNullFileBase
'''.split()#'''
__all__



import sys, locale

from contextlib import nullcontext as mk_null_context
from subprocess import DEVNULL
import io
from io import BufferedReader, RawIOBase, IOBase, DEFAULT_BUFFER_SIZE, UnsupportedOperation
from os import SEEK_SET
from seed.debug.expectError import expectError
from seed.tiny_.check import check_is_None

DEVNULL4subprocess = DEVNULL
assert DEVNULL4subprocess == -3

def null_context5result_(result, /):
    return mk_null_context(result)

null_context = mk_null_context()

#test reusable
with null_context:pass
with null_context:pass

#test bind
with null_context5result_(null_context5result_) as __:
    assert __ is null_context5result_



def _isize5may_isize(may_isize, /):
    if may_isize is None:
        isz = -1
    else:
        isz = may_isize
    isz
    if not type(isz) is int:
        raise TypeError("argument should be integer or None, not 'str'")
    return isz


class NullFileBase:
    #[[[
    r'''
[[


closed
    _check_not_closed
    close
        __enter__
        __exit__
        __del__

isatty
fileno

readable
    _check_readable_
    readline
        __next__
        __iter__
            readlines
seekable
    _check_seekable_
    tell
    seek
    truncate #---1
writable
    _check_writable_
    truncate #---2
    flush
    writelines

]]
    '''#''']]]
    __slots__ = ()

    assert issubclass(UnsupportedOperation, OSError)
    assert issubclass(UnsupportedOperation, ValueError)
    assert not issubclass(OSError, ValueError)
    assert UnsupportedOperation.__mro__ == (UnsupportedOperation, OSError, ValueError, Exception, BaseException, object)




    def _check_readable_(sf, nm, /):
        raise UnsupportedOperation(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)
    def _check_seekable_(sf, nm, /):
        raise UnsupportedOperation
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)
    def _check_writable_(sf, nm, /):
        raise UnsupportedOperation
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)

    def _check_not_closed(sf, nm=None, /):
        ##'nm is only set by _check_readable_/_check_writable_/_check_seekable_'
        if sf.closed:
            if 0 and nm:
                #to let ^UnsupportedOperation before ^ValueError@closed
                raise UnsupportedOperation(nm)
            raise ValueError('I/O operation on closed file.')



    @property
    def closed(sf, /):
        '-> bool'
        return True # always closed
        return False # always open
    def close(sf, /):
        '-> None'
        return None
        if not sf.closed:
            try:
                if sf.writable():
                    sf.flush()
            finally:
                check_is_None(sf._close_())
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
        return False



    def fileno(sf, /):
        '-> file_descriptor/uint|^OSError-not-file|^ValueError-closed'
        nm = 'fileno'
        raise UnsupportedOperation(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)
        return




    def readable(sf, /):
        'readable() -> bool|^ValueError #False => [read*() will raise OSError/io.UnsupportedOperation]'
        nm = 'readable'
        sf._check_not_closed(nm)
        return not expectError(OSError, lambda:sf._check_readable_(nm))

    def seekable(sf, /):
        'seekable() -> bool|^ValueError #whether [stream supports random access] #False => [seek(), tell(), truncate() will raise OSError/io.UnsupportedOperation]'
        nm = 'seekable'
        sf._check_not_closed(nm)
        return not expectError(OSError, lambda:sf._check_seekable_(nm))
    def writable(sf, /):
        'writable() -> bool|^ValueError #False => [write*(), truncate() will raise OSError/io.UnsupportedOperation]'
        nm = 'writable'

        sf._check_not_closed(nm)
        return not expectError(OSError, lambda:sf._check_writable_(nm))














    def __next__(sf, /):
        nm = '__next__'
        sf._check_readable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)
        smay_line = sf.readline(-1)
        if not smay_line:
            raise StopIteration
        line = smay_line
        return line
    def __iter__(sf, /):
        nm = '__iter__'
        sf._check_readable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)
        return sf
        #bug:readlines()->list<bytes>
        return sf.readlines()

    #def readlines(sf, hint=-1, /):
    def readlines(sf, min_positive_num_elems4read___or___may_zero_or_neg8inf=-1, /):
        '-> [xstring]|^UnsupportedOperation-not-readable|^ValueError-closed'
        nm = 'readlines'
        sf._check_readable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
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




    def readline(sf, may_isize=-1, /):
        '-> xstring/(bytes|str)|^UnsupportedOperation-not-readable|^ValueError-closed'
        nm = 'readline'
        sf._check_readable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)

        #readline(1)@<eof change tell()result
        #readline()@>=eof not change tell()result
        #readline(0) not change tell()result
        #readline(<0) <==> readline(None) <==> readline()
        #binary file line_sep===b'\n'
        #text file line_sep <<== open(newline=...)
        raise NotImplementedError





    def tell(sf, /):
        'tell() -> current stream position|^UnsupportedOperation-not-seekable|^ValueError-closed'
        nm = 'tell'
        sf._check_seekable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)
        raise NotImplementedError


    def seek(sf, offset, whence=SEEK_SET, /):
        'offset/int -> whence/[0,1,2] -> new absolute position|^UnsupportedOperation-not-seekable|^ValueError-closed   #maybe [old/new-location4tell > sz4file]'
        nm = 'seek'
        sf._check_seekable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)

        #seek:[new_location4tell>sz4file] is ok
        #seek:[seek:new_location4tell<0]@SEEK_SET ==>> ^ValueError
        #seek:[new_location4tell<0]@SEEK_CUR/SEEK_END <==> [new_location4tell==0]
        #seek:using operator.__index__ to convert 2 input: `offset` & `whence`
        raise NotImplementedError


    def truncate(sf, may_size=None, /):
        'may size/uint{allow>=sz4file} -> new file size|^UnsupportedOperation-not-seekable&writable|^ValueError-closed'
        nm = 'truncate'
        sf._check_seekable_(nm)
        sf._check_writable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)

        #truncate(None) <==> truncate(tell())
        #truncate(>=sz4file) <==> no-op echo
        #truncate(<0) --> ^ValueError
        #truncate() not change tell()result
        raise NotImplementedError




    def flush(sf, /):
        'flush() -> None|^BlockingIOError-raw-stream-block|^UnsupportedOperation-not-writable|^ValueError-closed'
        nm = 'flush'
        sf._check_writable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)

        raise NotImplementedError
        return None


    def writelines(sf, lines, /):
        '-> None|^UnsupportedOperation-not-writable|^ValueError-closed'
        nm = 'writelines'
        sf._check_writable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)

        #writelines(Iter<bytes_like_object>) -> None
        #writelines(...) no extra newline inserted
        #writelines(...) no padding on write empty bytes
        #writelines(...) padding on write nonempty bytes
        #iter+check_bytes_like_object
        raise NotImplementedError
        return None

#end-class NullFileBase:

class NullOutputFile(NullFileBase):
    'add: write()/...'
    __slots__ = ()
    @property
    def closed(sf, /):
        '-> bool'
        return False # always open
        return True # always closed
    def close(sf, /):
        '-> None'
        return None

    def _check_writable_(sf, nm, /):
        #raise UnsupportedOperation
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)
        return None#ok


    def flush(sf, /):
        'flush() -> None|^BlockingIOError-raw-stream-block|^UnsupportedOperation-not-writable|^ValueError-closed'
        nm = 'flush'
        sf._check_writable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)

        #raise NotImplementedError
        return None


    def writelines(sf, lines, /):
        '-> None|^UnsupportedOperation-not-writable|^ValueError-closed'
        nm = 'writelines'
        sf._check_writable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)

        #writelines(Iter<bytes_like_object>) -> None
        #writelines(...) no extra newline inserted
        #writelines(...) no padding on write empty bytes
        #writelines(...) padding on write nonempty bytes
        #iter+check_bytes_like_object
        #raise NotImplementedError
        return None

    def write(sf, xstring, /):
        '[a] -> len(a)'   r'''

RawIOBase.write(b) -> may num_bytes
  [non-blocking mode][no single byte could be readily written] <==> [result is None]
  [num_bytes <= len(b)]
  only one system call is ever made
BufferedIOBase.write(b) -> num_bytes{===len(b)}|^OSError-not-write-all|^BlockingIOError-require-blocking|^UnsupportedOperation-not-writable|^ValueError-closed
  [non blocking-mode][couldnot accept all the data without blocking] => [raise ^BlockingIOError]
  #... [non blocking-mode][raw stream block] => [raise ^BlockingIOError]
TextIOBase.write(s) -> num_chars
        '''#'''
        nm = 'write'
        sf._check_writable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)
        #raise NotImplementedError
        return len(xstring)
    def read(sf, size=-1, /):
        r'''
RawIOBase.read(size=-1) -> None|bytes{.len<=size}
  default => read all
  nondefault => only one system call is ever made
    ???why???since『raw』???
      yes!BufferedIOBase.read uses multiple system calls
  [result==b''][not size==0] => EOF
  [non-blocking mode][no bytes available] <==> [result is None]
  <<== readall+readinto

BufferedIOBase.read(size=-1) -> bytes{.len<=size}|^BlockingIOError|^UnsupportedOperation-not-readable|^ValueError-closed
  default => read all
  EOF => [result==b'']
  [size>0][not isatty] => [multiple raw reads until size or EOF]
  [not isatty][len(result) < size)] => EOF
  [isatty] => [at most one raw read]
  [len(result) < size] => [[isatty]or[EOF]]
  [non blocking-mode][no data available] => [raise ^BlockingIOError]
  ==>>:
    [0 == len(result) < size)] => EOF
      !!!OK!!!

TextIOBase.read(size=-1) -> str{.len<=size}
  default => EOF

        '''#'''
        nm = 'read'
        sf._check_readable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)
        raise NotImplementedError
    def readinto(sf, pre_allocated_writable_bytearray, /):
        r'''
RawIOBase.readinto(b) -> may num_bytes
  b :: pre-allocated-writable-bytearray
  [non-blocking mode][no bytes available] <==> [result is None]
  only one system call is ever made

BufferedIOBase.readinto(b) -> num_bytes|^BlockingIOError|^UnsupportedOperation-not-readable|^ValueError-closed
  b :: pre-allocated-writable-bytearray
  invariants like read()

        '''#'''
        nm = 'readinto'
        sf._check_readable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)
        raise NotImplementedError
    def detach(sf, /):
        r'''
BufferedIOBase.detach() -> the underlying raw stream|^UnsupportedOperation-no-raw-stream
  postcondition:[self unusable]

BufferedIOBase.[nonstd].raw :: RawIOBase
TextIOBase.[nonstd].buffer :: BufferedIOBase
  the underlying binary buffer

TextIOBase.detach() -> buffer/BufferedIOBase|^UnsupportedOperation
  postcondition:[self unusable]


        '''#'''
        nm = 'detach'
        return sf
    @property
    def raw(sf, /):
        return sf
    @property
    def buffer(sf, /):
        return sf

    def readall(sf, /):
        r'''
RawIOBase.readall() -> bytes
  multiple system calls until EOF

        '''#'''
        nm = 'readall'
        sf._check_readable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)
        raise NotImplementedError

    def read1(sf, /):
        r'''
BufferedIOBase.read1([size]) -> ?may? bytes|???^BlockingIOError???|^UnsupportedOperation-not-readable|^ValueError-closed
  <==> .raw.read(size)
  ???奇怪！不清楚:是否可能>None，还是^BlockingIOError
    相比readinto1 明确是 ^BlockingIOError 而非>None
        '''#'''
        nm = 'read1'
        sf._check_readable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)
        raise NotImplementedError

    def readinto1(sf, /):
        r'''
BufferedIOBase.readinto1(b) -> num_bytes|^BlockingIOError|^UnsupportedOperation-not-readable|^ValueError-closed
  <==> .raw.readinto(b) 只是 >None变^BlockingIOError
        '''#'''
        nm = 'readinto1'
        sf._check_readable_(nm)
            #to let ^UnsupportedOperation before ^ValueError@closed
        sf._check_not_closed(nm)
        raise NotImplementedError


    @property
    def encoding(sf, /):
        return locale.getpreferredencoding(False)
        return sys.getdefaultencoding()
        return sys.getfilesystemencoding()
        return sys.stdout.encoding
        return 'utf8'
        return None
    @property
    def errors(sf, /):
        return 'ignore'
        return 'strict'
    @property
    def newlines(sf, /):
        r'''
encoding :: may str

errors :: ?str?
  The error setting of the decoder or encoder.

newlines :: None|str|tuple<str>
  this may not be available
        '''#'''
        return None # <<== not readable

#end-class NullOutputFile(NullFileBase):
class ParameterizedNullFileBase(NullFileBase):
    'eg:encoding/newline...'
    #__slots__ = ()
    def __new__(cls, /, *, kwargs):
        sf = super(__class__, cls).__new__(cls)
        sf.__dict__.update(kwargs)
    def __setattr__(sf, nm, obj, /):
        raise AttributeError(nm)

io.IOBase.register(NullFileBase)
io.IOBase.register(NullOutputFile)

io.RawIOBase.register(NullOutputFile)
io.BufferedIOBase.register(NullOutputFile)
io.TextIOBase.register(NullOutputFile)


null_dev = NullOutputFile()





from seed.tiny_.null_dev import null_dev
from seed.tiny_.null_dev import null_context, null_context5result_
from seed.tiny_.null_dev import DEVNULL4subprocess
from seed.tiny_.null_dev import NullFileBase, NullOutputFile, null_dev, ParameterizedNullFileBase

from seed.tiny_.null_dev import *

