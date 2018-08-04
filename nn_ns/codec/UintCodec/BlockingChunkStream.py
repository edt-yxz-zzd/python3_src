
import os

class SeekError(Exception):pass
class SeekPassEOFError(EOFError, SeekError):pass
class SeekPassBeginningError(SeekError):pass
class ReadPassEOFError(EOFError):pass

class SkipError(Exception):pass
class SkipNotMatchedError(SkipError):pass



class TryToDo:
    def _tell_state(self):
        raise NotImplementedError
    def _restore_state(self, state):
        'state was a result of self._tell_state()'
        raise NotImplementedError

    
    def try_to_do_if(self, func, pred = lambda r: bool(r)):
        state = self._tell_state()
        try:
            r = func()
            if not pred(r):
                self._restore_state(state)
            return r
        except:
            self._restore_state(state)
            raise
        raise logic-error

    def try_to_do(self, func):
        return self.try_to_do_if(func, lambda r:True)
    def try_and_restore(self, func):
        return self.try_to_do_if(func, lambda r:False)
    

class ChunkStream_WriteOnlyBase:
    def tell(self):
        raise NotImplementedError
    def write(self, chunks):
        'return None'
        raise NotImplementedError
        
        
    
class BlockingChunkStream_ReadOnlyBase(TryToDo):
    '''view file as stream<chunk> or array<chunk> for random-access

unit : chunk; i.e. bit/byte/uint32/...
chunk is a fixed-length-struct
chunks : tuple<chunk> or bytes ...
'''
    def __init__(self, size):
        self.__size = size
    def __len__(self):
        '''return num_chunks_in_stream'''
        return self.__size
    def _seek(self, pos):
        raise NotImplementedError
    def seek(self, offset, whence=os.SEEK_SET):
        '''cannot seek pass EOF even writable;
otherwise throw SeekPassEOFError'''
        size = len(self)
        new_position = calc_new_position(offset, whence,
                                         size, self.tell())
        if new_position < 0:
            raise SeekPassBeginningError
        elif new_position > size:
            raise SeekPassEOFError
        return self._seek(new_position)
    def tell(self):
        '''return idx of current chunk'''
        raise NotImplementedError

    def read_le(self, max_size):
        'return chunks of length at most MAX_SIZE; increase current position'
        raise NotImplementedError


    # methods with default implement

    # read_** methods
        
    def read_eq(self, size):
        'return chunks of length SIZE or throw ReadPassEOFError; increase current position if success'
        bs = self.safe_read_eq(size)
        if bs is None:
            raise ReadPassEOFError
        
        assert len(bs) == size
        return bs
    def safe_read_eq(self, size):
        'return chunks of length SIZE or None'
        return self.try_to_do_if(lambda:self.__safe_read_eq(size),
                                 lambda r: r is not None)
    def __safe_read_eq(self, size):
        'called by safe_read_eq'
        bs = self.read_le(size)
        if len(bs) != size:
            return None
        return bs

    def skip_const(self, chunks):
        chunks_ = self.read_eq(len(chunks))
        if chunks_ != chunks:
            end = self.tell()
            begin = end - len(chunks)
            raise SkipNotMatchedError('skip [{} : {}], not matched input chunks'
                                      .format(begin, end))
        return None



    # peek_** methods
    
    def peek_le(self, max_size):
        'like read_le but not increase current position'
        return self.try_and_restore(lambda:self.read_le(max_size))
    def peek_eq(self, size):
        'like read_eq but not increase current position'
        return self.try_and_restore(lambda:self.read_eq(size))
    def safe_peek_eq(self, size):
        'like safe_read_eq but not increase current position'
        return self.try_and_restore(lambda:self.safe_read_eq(size))



    # methods from TryToDo
    
    def _tell_state(self):
        return self.tell()
    def _restore_state(self, state):
        'state was a result of self._tell_state()'
        self.seek(state)

    



class BlockingBitStream_ReadOnlyBase(BlockingChunkStream_ReadOnlyBase):
    '''unit: bit; bits = tuple<int(0) or int(1)>

triple_bits ::= (head_bits, middle_bytes, tail_bits)
assert 0 <= len(head_bits) < NUM_BITS_PER_BYTE
assert 0 <= len(tail_bits) < NUM_BITS_PER_BYTE
'''
    def __init__(self, size):
        super().__init__(size)
    def seek_bytepos(self, bytepos):
        pos = self.bytepos_bitpos2pos(bytepos, 0)
        self.seek(pos)
    def _seek(self, pos):
        raise NotImplementedError

    @staticmethod
    def bytepos_bitpos2pos(bytepos, bitpos):
        assert bytepos >= 0
        assert 0 <= bitpos < NUM_BITS_PER_BYTE
        assert bitpos.bit_length <= NUM_BITS_FOR_BIT_IDX_IN_BYTE
        return (bytepos << NUM_BITS_FOR_BIT_IDX_IN_BYTE) | bitpos

    @staticmethod
    def pos2bytepos_bitpos(pos):
        assert pos >= 0
        bytepos, bitpos = divmod(pos, NUM_BITS_PER_BYTE)
        return bytepos, bitpos
        bitpos = pos & MASK_FOR_BIT_IDX_IN_BYTE
        bytepos = pos >> NUM_BITS_FOR_BIT_IDX_IN_BYTE

    def tell(self):
        bitpos = self.tell_bitpos()
        bytepos = self.tell_bytepos()
##        if bitpos:
##            bytepos -= 1
        return self.bytepos_bitpos2pos(bytepos, bitpos)
        
    def tell_bitpos(self):
        '[0, 8); 0 for msb, 7 for lsb'
        raise NotImplementedError
    def tell_bytepos(self):
        raise NotImplementedError
        

    # read_** methods
    
    def read_le(self, max_size):
        'return bits of length at most MAX_SIZE; increase current position'
        return self.triple_bits2bits(self.triread_le(max_size))
    def read_eq(self, size):
        'return bits of length SIZE or throw ReadPassEOFError; increase current position if success'
        return self.triple_bits2bits(self.triread_eq(size))
    def safe_read_eq(self, size):
        'return bits of length SIZE or None'
        r = self.triread_le(size)
        return None if r is None else self.triple_bits2bits(r)


    # triple_bits_** methods
    
    @staticmethod
    def calc_bit_length_of_triple_bits(triple_bits):
        head_bits, middle_bytes, tail_bits = triple_bits
        return len(head_bits) + \
               NUM_BITS_PER_BYTE*len(middle_bytes) + \
               len(tail_bits)
    
    @staticmethod
    def triple_bits2iter_bits(triple_bits):
        head_bits, middle_bytes, tail_bits = triple_bits
        return chain(head_bits, iter_vbytes2iter_bits(middle_bytes), tail_bits)
    
    @staticmethod
    def iter_bits2bits(iter_bits):
        return tuple(iter_bits)
    @staticmethod
    def triple_bits2bits(triple_bits):
        return __class__.iter_bits2bits(
            __class__.triple_bits2iter_bits(triple_bits))
    
        
    # triread_** methods

    def num_remain_bits_in_incomplete_byte(self):
        bitpos = self.tell_bitpos()
        return NUM_BITS_PER_BYTE - bitpos if bitpos else 0


    def triread_le(self, max_size):
        '''like read_le but return (head_bits, middle_bytes, tail_bits)'''
        raise NotImplementedError
    
    def triread_eq(self, size):
        '''like read_eq but return (head_bits, middle_bytes, tail_bits)'''
        triple_bits = self.safe_read_eq(size)
        if triple_bits is None:
            raise ReadPassEOFError
        
        assert self.calc_bit_length_of_triple_bits(triple_bits) == size
        return triple_bits
    def safe_triread_eq(self, size):
        'like safe_read_eq but return (head_bits, middle_bytes, tail_bits) or None'
        return self.try_to_do_if(lambda:self.__safe_triread_eq(size),
                                 lambda r: r is not None)
    def __safe_triread_eq(self, size):
        'called by safe_read_eq'
        triple_bits = self.triread_le(size)
        if self.calc_bit_length_of_triple_bits(triple_bits) != size:
            return None
        return triple_bits





    # tripeek_** methods
    
    def tripeek_le(self, max_size):
        'like triread_le but not increase current position'
        return self.try_and_restore(lambda:self.triread_le(max_size))
    def tripeek_eq(self, size):
        'like triread_eq but not increase current position'
        return self.try_and_restore(lambda:self.triread_eq(size))
    def trisafe_peek_eq(self, size):
        'like safe_triread_eq but not increase current position'
        return self.try_and_restore(lambda:self.safe_triread_eq(size))


    
class BinaryFile2BinaryFile_WriteOnly(ChunkStream_WriteOnlyBase):
    def __init__(self, file):
        self.file = file
    def tell(self):
        return self.file.tell()
    def write(self, bs):
        'return None'
        return self.file.write(bs)



def calc_binary_file_size(file):
    begin = file.tell()
    try:
        file.seek(0, os.SEEK_END)
        return file.tell()
    finally:
        file.seek(begin)
def calc_new_position(offset, whence, total_size, position):
    if whence == os.SEEK_SET:
        begin = 0
    elif whence == os.SEEK_CUR:
        begin = position
    elif whence == os.SEEK_END:
        begin = total_size
    else:
        raise ValueError('whence should be os.SEEK_***')
    return begin + offset


class BinaryFile2BlockingBinaryFile_ReadOnly(BlockingChunkStream_ReadOnlyBase):
    def __init__(self, file):
        self.file = file
        size = calc_binary_file_size(file)
        super().__init__(size)

    def _seek(self, pos):
        self.file.seek(pos)
        
    def tell(self):
        return self.file.tell()

    def read_le(self, max_size):
        'return bytes of length at most MAX_SIZE'
        if max_size < 0:
            raise ValueError('max_size should >= 0')
        return self.file.read(max_size)


class BinaryFile2BlockingBitFile_ReadOnly(BlockingBitFile_ReadOnlyBase):
    def __init__(self, file):
        self.file = file
        bytesize = calc_binary_file_size(file)
        bitsize = bytesize * NUM_BITS_PER_BYTE
        self.__bitpos = 0
        super().__init__(bitsize)

        self.bytepos_and_maybe_bits = (0, None) # (a_bytepos, bits of a_bytepos)

##    def seek_bytepos(self, bytepos):
##        self.__seek(bytepos, 0)
    def _seek(self, pos):
##        bitpos = pos & MASK_FOR_BIT_IDX_IN_BYTE
##        bytepos = pos >> NUM_BITS_FOR_BIT_IDX_IN_BYTE
##        if bitpos:
##            bytepos += 1
        bytepos, bitpos = self.pos2bytepos_bitpos(pos)
        self.__seek(bytepos, bitpos)

    def __seek(self, bytepos, bitpos):
        self.file.seek(bytepos)
        self.__bitpos = bitpos
        
        
    def tell_bytepos(self):
        return self.file.tell()
    def tell_bitpos(self):
        return self.__bitpos

    def read_curr_byte_into_bits(self):
        'return None or bits of len 8'
        begin = self.tell_bytepos()
        end = begin + 1
        
        bytepos, maybe_bits = self.__bytepos_and_maybe_bits
        if bytepos == self.tell_bytepos() and maybe_bits:
            bits = maybe_bits
            self.seek_bytepos(end)
            return bits

        self.seek_bytepos(begin)
        maybe_curr_byte = self.file.read(1)
        if maybe_curr_byte:
            curr_byte = maybe_curr_byte
            vbyte = byte2vbyte(curr_byte)
            
            bits = tuple(vbyte2iter_bits(vbyte))
            self.__bytepos_and_maybe_bits = (begin, bits) # update/cache
            return bits
        return None



    def triread_le(self, max_size):
        '''like read_le but return (head_bits, middle_bytes, tail_bits)'''

        max_size = max(0, max_size)
        begin = self.tell()
        end = max(len(self), begin + max_size)
        
        num_remain = self.num_remain_bits_in_incomplete_byte()
        if num_remain >= max_size:
            num_head_bits = max_size
            max_num_middle_bytes = 0
            max_num_tail_bits = 0
            max_num_non_head_bytes = 0
        else:
            num_head_bits = num_remain
            max_num_non_head_bits = max_size - num_head_bits
            max_num_non_head_bytes = num_bits2num_bytes(max_num_non_head_bits)
            max_num_middle_bytes, max_num_tail_bits = \
                divmod(max_num_non_head_bits, NUM_BITS_PER_BYTE)

        if num_remain:
            bitpos = self.tell_bitpos()
            head_bits = self.read_curr_byte_into_bits()[bitpos:]
        else:
            head_bits = ()

        assert not self.tell_bitpos()
        middle_bytes = self.file.read(max_num_middle_bytes)
        
        tail_bits = ()
        if max_num_tail_bits and len(middle_bytes) == max_num_middle_bytes:
            maybe_last_byte_bits = self.read_curr_byte_into_bits()
            if maybe_last_byte_bits is not None:
                last_byte_bits = maybe_last_byte_bits
                tail_bits = last_byte_bits[:max_num_tail_bits]
                assert len(tail_bits) == max_num_tail_bits

        self.seek(end)
        return (head_bits, middle_bytes, tail_bits)






