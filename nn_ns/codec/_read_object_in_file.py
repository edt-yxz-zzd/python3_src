

'''
read_object_in_file
'''


from os import SEEK_CUR, SEEK_END
from abc import ABCMeta, abstractmethod
from .common import *






class ReadableInFileABC(ABCMeta):
    @abstractmethod
    def _read(self, ptr):
        raise NotImplementedError
    def read(self, sized_file):
        ptr = PtrInSizedFile(sized_file)
        return self._read(ptr)

    #@abstractmethod
    def skip(self, sized_file):
        L = self.peek_len(sized_file)

        # not allow pos+L > size_limit
        ptr = PtrInSizedFile(sized_file) + L
        ptr.prepare()
        return sized_file.file.tell()
    
    def try_skip(self, sized_file):
        'skip and then seek back'
        with fixed_pos(sized_file.file):
            self.skip(sized_file)
        return
    def peek_len(self, sized_file):
        'return the skip length (not include heap length if any)'
        L = self._known_len()
        if L is None:
            L = self._peek_len(sized_file)
        check_uint(L, 'object_size')
        return L

    
    def _skip(self, sized_file):
        self.read(sized_file)
        return sized_file.file.tell()
    def _known_len(self):
        return None
    def _peek_len(self, sized_file):
        file = sized_file.file
        pos = file.tell()
        end = self._skip(sized_file)
        file.seek(pos)
        return end-pos



class RefFile:
    __slots__ = ('__file',)
    def __init__(self, file):
        if isinstance(file, __class__):
            file = file.file
        self.__file = file
    @property
    def file(self):
        return self.__file



def check_uint(i, name=None, err_type=TypeError):
    def r(err_fmt):
        prefix = 'not unsigned int: '
        if name is None:
            name = 'i'
        err = prefix + err_fmt.format(name)
        raise err_type(err)
    if type(i) is not int:
        raise r('type({}) is not int')
    if i < 0:
        raise r('{} < 0')

def check_rng(rng, name=None, err_type=TypeError):
    if name is None:
        name = 'rng'
    def r(err_fmt):
        prefix = 'not range: '
        err = prefix + err_fmt.format(name)
        raise err_type(err)
    if type(rng) is not tuple:
        raise r('type({}) is not tuple')
    if len(rng) != 2:
        raise r('len({}) != 2')
    begin, end = rng
    check_uint(begin, name+'::begin')
    check_uint(end, name+'::end')
    

class _PtrInFileMixin:
    #__slots__ = ('__pos',)
    def __init__(self, pos):
        check_uint(pos, 'pos')
        self.__pos = pos
    @property
    def pos(self):
        return self.__pos


    def read(self, n=-1):
        self.prepare()
        return self.file.read(n)
    def __sub__(self, offset):
        return self + -offset
class _PtrInFile(RefFile, _PtrInFileMixin):
    '''unsafe if seek beyond file'''
    __slots__ = ()
    # class _PtrInFile(RefFile, _PtrInFileMixin)
    # TypeError: multiple bases have instance lay-out conflict

    def __init__(self, file, pos=None):
        if not file.seekable():
            raise TypeError('not file.seekable()')
        RefFile.__init__(self, file)

        if pos is None:
            pos = file.tell()
        _PtrInFileMixin.__init__(self, pos)
        
    def prepare(self):
        return self.file.seek(self.pos)

    def __add__(self, offset):
        return __class__(self.file, self.pos + offset)
                 


class _FixedPos:
    
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ptr.prepare()
        return self.suppress

    def __init__(self, file, pos=None, *, suppress=False):
        self.ptr = _PtrInFile(file, pos=pos)
        self.suppress = suppress
        
def fixed_pos(file):
    '''fixed file current position

usage:
    pos = file.tell()
    with fixed_pos(file):
        f(file)
    assert file.tell() == pos
'''
    return _FixedPos(file)
    

def get_size(file):
    # TO AVOID seek beyond the end
    # not: file.seek(L, SEEK_CUR)
##    pos = file.tell()
##    end = file.seek(0, SEEK_END)
##    file.seek(pos)
##    return end
    with fixed_pos(file):
        return file.seek(0, SEEK_END)
class SizedFile(RefFile):
    __slots__ = ('__size',)
    
    def __init__(self, file, size=None):
        if isinstance(file, __class__):
            other = file
            file = other.file
            max_size = min(other.size, get_size(file))
            if size is None:
                size = other.size
        else:
            max_size = get_size(file)
            
        super().__init__(file)
        if size is None:
            size = get_size(file)
        check_uint(size, 'size')
        if size > max_size:
            # even other.size < size <= get_size(file)
            raise ValueError('size > input_file.size_limit')
        self.__size = size
        
    @property
    def size(self):
        return self.__size

    def tellx(self):
        return self.file.tell()
    def eofx(self):
        return self.size == self.tellx()
    def exceeded(self):
        return self.size < self.tellx()
    def tail_size(self):
        if self.exceeded():
            raise ValueError('self.exceeded()')
        s = self.size - self.tellx()
        check_uint(s, 'tail_size')
        return s
    
class RefSizedFile:
    __slots__ = ('__sized_file',)
    
    def __init__(self, sized_file):
        if isinstance(sized_file, __class__):
            other = sized_file
            sized_file = other.sized_file
        elif not isinstance(sized_file, SizedFile):
            raise TypeError('not isinstance(sized_file, SizedFile)')
        self.__sized_file = sized_file
    @property
    def sized_file(self):
        return self.__sized_file
class ExRefSizedFile(RefSizedFile):
    __slots__ = ()
    @property
    def file(self):
        return self.sized_file.file
    @property
    def size(self):
        return self.sized_file.size
    
class PtrInSizedFile(ExRefSizedFile, _PtrInFileMixin):
    '''raise if seek beyond file'''
    __slots__ = ()
    def __init__(self, sized_file, pos=None):
        if isinstance(sized_file, __class__):
            other = sized_file
            sized_file = other.sized_file
            if pos is None:
                pos = other.pos
        RefSizedFile.__init__(self, sized_file)
        #sized_file = self.sized_file
        file = sized_file.file
        if not file.seekable():
            raise TypeError('not file.seekable()')

        if pos is None:
            pos = file.tell()
        if not 0 <= pos <= sized_file.size:
            raise ValueError('not 0 <= pos <= sized_file.size')
        _PtrInFileMixin.__init__(self, pos)
        
    def prepare(self):
        assert 0 <= pos <= self.sized_file.size
        file = self.file
        pos = self.pos
        if file.tell() == pos:
            return pos
        return file.seek(pos)

    def __add__(self, offset):
        return __class__(self.sized_file, self.pos + offset)
    def read(self, n=-1):
        self.prepare()
        if n < 0:
            assert n == -1
            n = self.size
        assert n >= 0
        n = min(n, self.max_len) # not pass limit
        return self.file.read(n)
    @property
    def max_len(self):
        return self.size - self.pos
    def enough(self, size):
        return size <= self.max_len
    def check_enough(self, size):
        if not self.enough(size):
            raise ValueError('not self.enough(size)')

    def read_ex(self, n=-1):
        bs = self.read(n)
        ptr = __class__(self.sized_file)
        return ptr, bs

class RangedFile(ExRefSizedFile):
    __slots__ = ('__rng')
    def __init__(self, sized_file, begin=None, end=None):
        super().__init__(sized_file)
        sized_file = self.sized_file
        
        if begin is None:
            begin = 0
        if end is None:
            end = self.size
        rng = begin, end
        check_rng(rng)

        if not 0 <= begin <= end <= sized_file.size:
            raise ValueError('not 0 <= begin <= end <= sized_file.size')
        self.__rng = rng

    @property
    def range(self):
        return self.__rng
    @property
    def begin(self):
        return self.__rng[0]
    @property
    def end(self):
        return self.__rng[-1]

##class ObjectInFile(ABCMeta):
##    @abstractmethod
##    def _read(self, sized_file):...
##    def read(self, sized_file):
##        assert isinstance(sized_file, SizedFile)
##        return self._read(self, sized_file)

class ObjectInFile_ReadError(ValueError):pass


class ObjectInFile_NoHeap_RequiredLength:
    def readL(self, sized_file, L):
        check_uint(L, 'object_size')
        ptr = PtrInSizedFile(sized_file)
        if L > ptr.max_len:
            raise ValueError('not enough bytes')
        return self._read(ptr, L)
    def _readL(self, ptr, L):
        raise NotImplementedError
class ObjectInFile_NoHeap_WithoutLength(ReadableInFileABC):pass
class ObjectInFile_NoHeap_FixedLength(ObjectInFile_NoHeap_WithoutLength):
    @property
    def size(self):
        raise NotImplementedError
    def _known_len(self):
        return self.size
    
class ObjectInFile_NoHeap_FixedLength__L(ObjectInFile_NoHeap_FixedLength):
    def __init__(self, obj_reader, L):
        check_uint(L, 'object size')
        self.__size = L
        if not isinstance(obj_reader, ObjectInFile_NoHeap_RequiredLength):
            raise TypeError('not isinstance(obj_reader, ObjectInFile_NoHeap_RequiredLength)')
        self.__obj_reader = obj_reader
    def _read(self, ptr):
        ptr.prepare()
        return self.__obj_reader.readL(ptr.sized_file, self.size)
    @property
    def size(self):
        return self.__size

class BytesInFile_RequiredLength(ObjectInFile_NoHeap_RequiredLength):
    def _readN(self, ptr, L):
        bs = ptr.read(L)
        assert len(bs) == L
        return bs
class BytesInFile_FixedLength__L(ObjectInFile_NoHeap_FixedLength__L):
    __obj_reader = BytesInFile_RequiredLength()
    def __init__(self, L):
        super().__init__(self.__obj_reader, L)
class BytesInFile_WithoutLength__EndBy(ObjectInFile_NoHeap_WithoutLength):
    def _read(self, ptr):
        bs = self.__read(ptr)
        return bytes(bs)
    def __read(self, ptr):
        bs = bytearray()
        while True:
            ptr_, b = ptr.read_ex(1)
            if not b:
                break
            r = self._test_bytes(bs, b)
            assert -1 <= r <= 1
            if r == -1:
                # put b back; end
                ptr.prepare() # seek backward 1
                return bs
                break
            
            bs.extend(b)
            if r == 0:
                # end
                return bs
            assert r == 1 # continue
            ptr = ptr_

        # EOF or touch size limit
        if self._test_bytes_eof(bs):
            return bs
        raise ObjectInFile_ReadError('read fail : size limit hits')

    def _test_bytes(self, bs, b):
        'return -1|0|+1'
        raise NotImplementedError
    def _test_bytes_eof(self, bs):
        'return True | False'
        raise NotImplementedError

class RawDynamicBytesInFile(BytesInFile_WithoutLength__EndBy):
    def _test_bytes(self, bs, b):
        'return -1|0|+1'
        i, = b
        assert 0 <= i < 256
        if i < 0x80:
            return 0
        return 1
        
    def _test_bytes_eof(self, bs):
        'return True | False'
        return False


class IntInFile(BytesInFile_FixedLength__L):
    def __init__(self, length, byteorder, *, signed=False):
        #self.length = length
        self.byteorder = byteorder
        self.signed=signed
        super().__init__(length)

    def _read(self, ptr):
        bs = super()._read(ptr)
        return int.from_bytes(self.size, self.byteorder, signed=self.signed)

class UintInFile(IntInFile):
    def __init__(self, length, byteorder):
        super().__init__(length, byteorder)

class UintBInFile(UintInFile):
    def __init__(self, length):
        super().__init__(length, byteorder='big')

class UintLInFile(UintInFile):
    def __init__(self, length):
        super().__init__(length, byteorder='little')



class ArrayInFile:
    '''array of fixed-length objects'''
    def __init__(self, elem_reader):
        #self.num_elems = num_elems
        #self.elem_size = elem_size
        if not isinstance(elem_reader, ObjectInFile_NoHeap_FixedLength):
            raise TypeError('not isinstance(elem_reader, ObjectInFile_NoHeap_FixedLength)')
        # self.elem_size = elem_reader.size
        self.elem_reader = elem_reader
        check_uint(self.elem_size, 'elem_size')

    @property
    def elem_size(self):
        return self.elem_reader.size
    def total_size(self, num_elems):
        check_uint(num_elems, 'num_elems')
        return num_elems * self.elem_size
    def readN(self, sized_file, num_elems):
        total_size = self.total_size(num_elems)
        ptr = PtrInSizedFile(sized_file)
        ptr.check_enough(total_size)

        ls = []
        read = self.elem_reader.read
        for _ in range(num_elems):
            obj = read(sized_file)
            ls.append(obj)
        return ls
class ListInFile:
    '''list of var-length objects'''
    def __init__(self, elem_reader):
        if not isinstance(elem_reader, ObjectInFile_NoHeap_WithoutLength):
            raise TypeError('not isinstance(elem_reader, ObjectInFile_NoHeap_WithoutLength)')

        self.elem_reader = elem_reader
    def __doN(self, sized_file, num_elems, f):
        check_uint(num_elems, 'num_elems')
        ptr = PtrInSizedFile(sized_file)
        ptr.check_enough(0) # assert not exceed
        return [f(sized_file) for _ in range(num_elems)]
    
    def readN(self, sized_file, num_elems):
        f = self.elem_reader.read
        return self.__doN(sized_file, num_elems, f)
    def skipN(self, sized_file, num_elems):
        f = self.elem_reader.skip
        ls = self.__doN(sized_file, num_elems, f)
        if not ls:
            return sized_file.tellx()
        return ls[-1]
class TupleInFile(ObjectInFile_NoHeap_WithoutLength):
    '''tuple of var-length types'''
    def __init__(self, elem_readers):
        elem_readers = tuple(elem_readers)
        if not all(isinstance(elem_reader, ObjectInFile_NoHeap_WithoutLength)
                   for elem_reader in elem_readers):
            raise TypeError('not all(isinstance(elem_reader, ObjectInFile_NoHeap_WithoutLength) '
                            'for elem_reader in elem_readers)')

        self.elem_readers = elem_readers
        
    def __doN(self, sized_file, f):
        ptr = PtrInSizedFile(sized_file)
        ptr.check_enough(0) # assert not exceed

        return (f(elem_reader, sized_file) for elem_reader in self.elem_readers)
    
    def _read(self, sized_file):
        f = lambda elem_reader, sized_file: \
            self.elem_reader.read(sized_file)
        ls = self.__doN(sized_file, f)
        return tuple(ls)
    def _peek_len(self, sized_file):
        f = lambda elem_reader, sized_file: \
            self.elem_reader.peek_len(sized_file)
        lens = self.__doN(sized_file, f)
        return sum(lens)
    

class TupleInFile_FixedLength(ObjectInFile_NoHeap_FixedLength):
    '''tuple of fixed-length types'''
    def __init__(self, elem_readers):
        elem_readers = tuple(elem_readers)
        if not all(isinstance(elem_reader, ObjectInFile_NoHeap_FixedLength)
                   for elem_reader in elem_readers):
            raise TypeError('not all(isinstance(elem_reader, ObjectInFile_NoHeap_FixedLength) '
                            'for elem_reader in elem_readers)')

        self.elem_readers = elem_readers
        self.__size = sum(e.size for e in elem_readers)
        #super().__init__(size)
        
    @property
    def size(self):
        return self.__size
    
    def __doN(self, ptr, f):
        ptr.check_enough(self.size) # assert not exceed
        return (f(elem_reader, sized_file) for elem_reader in self.elem_readers)
    def _read(self, ptr):
        f = lambda elem_reader, sized_file: \
            self.elem_reader.read(sized_file)
        it = self.__doN(ptr, f)
        return tuple(it)
    
















