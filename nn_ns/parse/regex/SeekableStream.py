


from abc import ABCMeta, abstractmethod
from contextlib import contextmanager



class ReadableStreamABC(metaclass=ABCMeta):
    @abstractmethod
    def _iter_read(self):
        'iter read all remain tokens'
        raise NotImplementedError



    ############## auto ####################
    
    def _read_le1(self):
        'return empty|singleton seq'
        for e in self.iter_read():
            return [e]
        return []
    def read_le1(self):
        return self._read_le1()
    
    def iter_read(self):
        'iter read all remain tokens'
        return self._iter_read()

    
    def iter_read_le(self, n):
        'iter(read at most n tokens)'
        if n < 0:
            raise ValueError('n < 0')
        return islice(self.iter_read(), n)


    

    def read_le(self, n):
        'read at most n tokens; return type could be any seq'
        return tuple(self.iter_read_le(n))
    def skip_le(self, n):
        'skip at most n(n>=0) tokens; return the actual skipped num'
        if n < 0:
            raise ValueError('n < 0')
        ls = self.read_le(n)
        return len(ls)


class SeekableStreamABC(metaclass=ABCMeta):
    '''seekable stream: bytes, chars, tokens, supertokens...

to use regex upon file:
    each char was encoded by var-length bytes.
    seekable but not random_accessable
pos - position; not element index
    to seek to ith element,
    we need the pos returned by tell()
    when stream was at index i
pos : __hash__; __eq__
    may not a integer
    i.e. a tuple : (byte_index, char_index, token_index)

each time pos changes, should call on_pos_change()
'''
    @abstractmethod
    def tell(self):
        'return current pos'
        raise NotImplementedError
    @abstractmethod
    def _seek(self, pos):
        raise NotImplementedError

##    def on_pos_change(self):
##        pass

        
    def seek(self, pos):
        if not self.tell() == pos:
            self._seek(pos)
            #self.on_pos_change()
        return
    @contextmanager
    def hold_pos(self):
        '''hold position; return self

usage:
    pos = x.tell()
    with x.hold_pos() as x:
        f(x)
    assert x.tell() == pos
'''
        pos = self.tell()
        try:
            yield self
        finally:
            self.seek(pos)
        return
##    @contextmanager
##    def _autocall_on_pos_change(self):
##        '''if position changes then call on_pos_change; return self
##
##usage:
##    pos = x.tell()
##    with x._autocall_on_pos_change() as x:
##        f(x)
##    # auto call on_pos_change if x.tell() != pos
##'''
##        pos = self.tell()
##        try:
##            yield self
##        finally:
##            if x.tell() != pos:
##                self.on_pos_change()
##        return


class SeekRead_StreamMixin:
    'SeekRead_StreamABC = SeekRead_StreamMixin + ReadableStreamABC + SeekableStreamABC'
    def peek_le(self, n):
        with self.hold_pos():
            return read_le(n)
    def is_end(self):
        with self.hold_pos():
            return bool(self._read_le1()) # not self.read_le1()


class SeekReadback_StreamMixin:
    def peekback_le(self, n):
        with self.hold_pos():
            return readback_le(n)
    def is_begin(self):
        with self.hold_pos():
            return bool(self._readback_le1()) # not self.readback_le1()


class ReadbackableStreamABC(metaclass=ABCMeta):
    '''for regex like '(?<=xxx)

all tokens are in reverse order
'''
    @abstractmethod
    def _iter_readback(self):
        'iter readback all prev tokens'
        raise NotImplementedError


    ############## auto ####################
    
    def _readback_le1(self):
        'return empty|singleton seq'
        for e in self.iter_readback():
            return [e]
        return []
    def readback_le1(self):
        return self._readback_le1()
    
    def iter_readback(self):
        'iter readback all prev tokens'
        return self._iter_readback()

    
    def iter_readback_le(self, n):
        'iter(readback at most n tokens)'
        if n < 0:
            raise ValueError('n < 0')
        return islice(self.iter_readback(), n)


    

    def readback_le(self, n):
        'readback at most n tokens; return type could be any seq'
        return tuple(self.iter_readback_le(n))
    def skipback_le(self, n):
        'skipback at most n(n>=0) tokens; return the actual skipped num'
        if n < 0:
            raise ValueError('n < 0')
        ls = self.readback_le(n)
        return len(ls)


    
class ForkSeekableStream(SeekableStreamABC):
    '''copy stream...

usage:
    streamA
    A, B = map(ForkSeekableStream, streamA)
    C = A.fork()
    
    B.seek(posB)
    C.seek(posC)
    for a, b, c in zip(A.iter_read(), B.iter_read(), C.iter_read()):...
    
'''
    def __init__(self, seekable_stream_obj):
        self.__pos = seekable_stream_obj.tell() # not obj.__s.pos
        if __class__ is type(seekable_stream_obj):
            self.__s = seekable_stream_obj.__s
        else:
            self.__s = seekable_stream_obj

    def fork(self):
        return __class__(self)
    def tell(self):
        'return current pos'
        raise self.__pos # instead of self.__s.tell() !!!!!!!!!
    
    def _seek(self, pos):
        self.__pos = pos # instead of self.__s._seek(pos) !!!!!

class ForkReadableStreamMixin(ReadableStreamABC):
    def _iter_read(self):
        'iter read all remain tokens'
        while True:
            seq = self._read_le1()
            if not seq:
                break
            yield from seq
        return
    
    def _read_le1(self):
        'return empty|singleton seq'
        self.__s.seek(self.tell())   # not need to seek back
        seq = self.__s.read_le1()
        self.seek(self.__s.tell())
        return seq
    

class ForkReadbackableStreamMixin(ReadbackableStreamABC):
    def _iter_readback(self):
        'iter readback all prev tokens'
        while True:
            seq = self._readback_le1()
            if not seq:
                break
            yield from seq
        return
    
    def _readback_le1(self):
        'return empty|singleton seq'
        self.__s.seek(self.tell())   # not need to seek back
        seq = self.__s.readback_le1()
        self.seek(self.__s.tell())
        return seq
    

