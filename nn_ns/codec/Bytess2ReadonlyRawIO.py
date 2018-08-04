
'''
mapping a bytes producer into a RawReader
'''

__all__ = ['Bytess2ReadonlyRawIO']

import io, os

class Bytess2ReadonlyRawIO(io.RawIOBase):
    def __init__(self, iter_bytess=()):
        # iter_bytess is a bytes producer
        self.__it = iter(iter_bytess) # bug: forgot call iter(...)
        self.__io = io.BytesIO()

    def get_incomplete_memoryview(self):
        return self.__buf
    def get_complete_memoryview(self):
        self.__iter_all()
        return self.__buf
    
    # ---------------------------------------------
    # private
    
    @property
    def __buf(self):
        return self.__io.getbuffer()

    def __seek_to_end(self):
        write = self.__get_writer()
        for bs in self.__it:
            write(bs)
    def __try_seek(self, pos):
        if pos < 0:
            raise ValueError('seekpos = {} < 0'.format(pos))
        remain = len(self.__buf) - pos
        if remain < 0:
            write = self.__get_writer()
            for bs in self.__it:
                write(bs)
                remain += len(bs)
                if remain >= 0:
                    break
            else:
                # not enough bytes to read
                pass
        if remain < 0:
            self.__seek_to_end()
        else:
            self.__io.seek(pos)
            
        
    def __get_writer(self):
        file = self.__io
        file.seek(0, os.SEEK_END)
        return file.write
    def __iter_all(self):
        begin = self.tell()
        self.__seek_to_end()
        end = self.tell()
        self.seek(begin)
        return end - begin # remain

        

    def __remain(self):
        # >= 0
        # although seek beyond buf will yield negative value
        # I forbid seek beyond buf!!
        return len(self.__buf) - self.__io.tell() # not < 0

    def __on_modify(self):
        raise io.UnsupportedOperation('Bytess2ReadonlyRawIO is readonly stream')


    # ---------------------------------------------
    # RawIOBase
    
    
    def read(self, n=-1):
        if n == -1:
            return self.readall()
        if n < 0:
            raise ValueError('n < -1')

        begin = self.tell()
        self.__try_seek(begin + n)
        self.seek(begin)
        return self.__io.read(n)

    def readall(self):
        n = self.__iter_all()
        bs = self.__io.read(n)
        assert len(bs) == n
        return bs
    
    def readinto(self, b):
        # blocking mode
        
        n = len(b)
        #if n < 0: raise ValueError('n < 0')
        begin = self.tell()
        self.__try_seek(begin + n)
        end = self.tell()
        size = end - begin
        b[:size] = self.__buf[begin:end]
        
        assert len(b) == n
        return size
    
    def write(self, b):
        self.__on_modify()

    # ---------------------------------------------
    # IOBase
    
    def close(self):
        return self.__io.close()
    @property
    def closed(self):
        return self.__io.closed
    
    def fileno(self):
        try:
            return self.__io.fileno()
        except OSError as e:
            raise OSError(__class__.__name__ + ' is not a regular file', e)
    def flush(self):
        return self.__io.flush()
    def isatty(self):
        return self.__io.isatty()
    def readable(self):
        return self.__io.readable()
    def readline(self, limit=-1):
        begin = self.tell()
        EOF = False
        if limit >= 0:
            remain = self.__remain()
            if remain < limit and b'\n' not in self.__buf[begin:]:
                write = self.__get_writer()
                for bs in self.__it:
                    write(bs)
                    remain += len(bs)
                    if remain >= limit:
                        break
                    if b'\n' in bs:
                        break
                else:
                    EOF = True
                self.seek(begin)
            assert EOF or self.__remain() >= limit or b'\n' in self.__buf[begin:]
            
        elif limit == -1:
            if b'\n' not in self.__buf[begin:]:
                write = self.__get_writer()
                for bs in self.__it:
                    write(bs)
                    if b'\n' in bs:
                        break
                else:
                    EOF = True
                self.seek(begin)
            assert EOF or b'\n' in self.__buf[begin:]
        else:
            raise ValueError('limit < -1')
            
        return self.__io.readline(limit)
    
    def readlines(self, hint=-1):
        if hint <= 0:
            self.__iter_all()
            
            readline = self.__io.readline
            lines = []
            while True:
                line = readline()
                if not line:
                    break
                lines.append(line)
        else:
            begin = self.tell()
            self.__try_seek(begin + hint)
            end = self.tell()
            self.seek(begin)

            readline = self.readline # NOTE: diff with above one
            lines = []
            while self.tell() < end:
                line = readline()
                #if not line: break
                lines.append(line)
                
        return lines

    def seek(self, offset, whence=os.SEEK_SET):
        if whence == os.SEEK_SET:
            pos = offset
        elif whence == os.SEEK_CUR:
            pos = offset + self.tell()
        elif whence == os.SEEK_END:
            self.__seek_to_end()
            end = self.tell()
            pos = end + offset
        self.__try_seek(pos)
        if self.tell() != pos:
            assert self.tell() < pos
            assert self.__size() < pos
            raise OSError('seek beyond EOF : total:{} < seekpos:{}'
                          .format(self.__size(), pos))
        return pos
    def seekable(self):
        return True
    def tell(self):
        return self.__io.tell()
    def truncate(self, size=None):
        # The current stream position isn’t changed.
        self.__on_modify()
    def writable(self):
        # If False, write() and truncate() will raise OSError.
        # UnsupportedOperation inheriting OSError and ValueError
        # so, I raise UnsupportedOperation
        return False
    def writelines(self, lines):
        self.__on_modify()

    
def test_Bytess2ReadonlyRawIO():
    for bss in [(b'a', b'', b'adfs'), (), (b'',), (b'', b'3s')]:
        file_bytes = b''.join(bss)
        file = Bytess2ReadonlyRawIO(bss)
        first_byte = file.read(1)
        assert (not first_byte) == (not file_bytes)
        assert len(file.get_incomplete_memoryview()) == (
            0 if not file_bytes
            else [L for L in map(len, bss) if L][0])
        assert bytes(file.get_incomplete_memoryview()) == (
            b'' if not file_bytes
            else [bs for bs in bss if bs][0])
        assert file.tell() == 1 or not file_bytes
        
        file.seek(0)
        r = file.readall()
        #print(bss, file.tell(), file_bytes, r)
        assert r == file_bytes
        assert file.tell() == len(file_bytes)

        file.seek(0)
        assert file.tell() == 0
test_Bytess2ReadonlyRawIO()


