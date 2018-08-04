
__all__ = '''
    Stream_OpUncons
    Stream_OpTell
    Stream_OpSeek
    Stream_Ops
    OffsetedArray
    ArrayStream
    '''.split()

from .Utils import handle_seq_begin_end
from abc import abstractmethod, ABCMeta

class ImmutableStream(metaclass=ABCMeta):pass
class Stream_OpUncons(ImmutableStream):
    '''\
uncons :: self -> (None | (token, other))
'''
    @abstractmethod
    def uncons(self):pass

class Stream_OpTell(ImmutableStream):
    '''\
tell :: self -> pos
'''
    @abstractmethod
    def tell(self):pass

class Stream_OpSeek(ImmutableStream):
    '''\
seek :: (self, pos) -> other
'''
    @abstractmethod
    def seek(self):pass

class OffsetedArray:
    # may not begin index from 0
    def __init__(self, seq, begin=None, end=None):
        seq, begin, end = handle_seq_begin_end(seq, begin, end)
        assert 0 <= begin <= end <= len(seq)
        self.__stream = (seq, begin, end)
    def __getitem__(self, i):
        seq, begin, end = self.__stream
        if begin <= i < end:
            return seq[i]
        raise IndexError(i)
    def get_args(self):
        return self.__stream
    def get_range(self):
        seq, begin, end = self.__stream
        return begin, end
    def get_end(self):
        return self.__stream[2]
    def get_begin(self):
        return self.__stream[1]
class Stream_Ops(Stream_OpUncons, Stream_OpTell, Stream_OpSeek):
    pass
class ArrayStream(Stream_Ops):
    def __init__(self, array, pos=None):
        assert isinstance(array, OffsetedArray)
        if pos is None:
            pos = array.get_begin()
        self.__stream = array
        self.__pos = pos
    def get_args(self):
        return self.__stream, self.__pos
    def seek(self, pos):
        return type(self)(self.__stream, pos)
    def tell(self):
        return self.__pos
    def uncons(self):
        array, pos = self.get_args()
        try:
            val = array[pos]
        except IndexError:
            return None
        return val, self.seek(pos+1)



