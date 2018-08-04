
'''
a has b
    b is a subobject of a
a owns b
    b is a satellite object of a
a shares b
    a has a shared_ptr to b
a points to b
    a has a raw ptr to b
a refers to b
    a has a key to b [in some a database / mapping]
a weakrefs to b
    a has a weak_ptr to b
'''

'''
fixed_length_struct
    # basic
    byte # SIZE in bytes
    word<SIZE, ENDIAN=big|little> ==>> ptr/position/enum
    // sint<SIZE, ENDIAN, REPRESENTATION=twos_complement|ones_complement|signed_magnitude> ==>> offset
        # 2's complement, 1's complement and signed magnitude representations
    // float<SIZE=4|8> # ENDIAN??
    eqsize_array<EQ_SIZE_ELEMENT_TYPE, LENGTH>
    array<FLS, LENGTH>
    // union<FLS1, FLS2 ...>
    tuple<FLS1, FLS2 ...>
    
varlength_struct
    endby_list = guarded_list = list<T> end_by a guard
    sized_list = tuple<uint, list<T> >
'''

__all__ = []

import functools
from sand import FormatError

def is_uint(u):
    return type(u) is int and u >= 0
def check_uint(u):
    assert is_uint(u)


class _T:
    def __init__(self, type, data):
        self.__type = type
        self.__data = data
    def __getattr__(self, method_name):
        return functools.partial(getattr(self.__type, '_T_'+method_name), self.__data)
    def is_of_type(self, type):
        return self.__type == type
    
class Type:
    def __init__(self, fixed_length):
        assert fixed_length is None or is_uint(fixed_length)
        self.__sz = fixed_length
    def is_fixed_length_type(self):
        return self.get_fixed_length() is not None
    
    def get_fixed_length(self):
        # return None or uint
        raise self.__sz
    def get_type_name(self):
        raise NotImplementedError
    def __repr__(self):
        return self.get_type_name()

    def create(self):
        raise NotImplementedError
    def to_bytes(self, data):
        # return bytes # of length self.get_fixed_length() if not None
        bs = self._to_bytes(data)
        if self.is_fixed_length_type():
            assert len(bs) == self.get_fixed_length()
        return bs
    
    def from_bytes(self, bs):
        if self.is_fixed_length_type():
            assert len(bs) == self.get_fixed_length()
        return self._from_bytes(bs)
    
    def _to_bytes(self, data):
        # return bytes # of length self.get_fixed_length() if not None
        raise NotImplementedError
    def _from_bytes(self, bs):
        raise NotImplementedError
    def from_bytes_ex(self, bs, begin, end):
        # from prefix of bytes
        if self.is_fixed_length_type():
            L = self.get_fixed_length()
            if end-begin < L:
                raise ValueError('too few bytes')
            return from_bytes(bs[begin:begin+L]), L
            
        raise NotImplementedError


    def to_file(self, data, file):
        file.write(self.to_bytes(data))
    def from_file(self, file):
        if self.is_fixed_length_type():
            sz = self.get_fixed_length()
            bs = file.read(sz)
            if len(bs) != sz:
                assert len(bs) < sz
                raise FormatError('EOF while reading {}'.format(self.get_type_name()))
            return self.from_bytes(bs)
        raise NotImplementedError
    
    def _T_to_bytes(self, data):
        return self.to_bytes(data)
    def _T_from_bytes(self, data, bs):
        return self.from_bytes(bs)
    def _T_from_bytes_ex(self, data, bs, begin, end):
        return self.from_bytes_ex(bs, begin, end)
    def _T_to_file(self, data, file):
        return self.to_file(data, file)
    def _T_from_file(self, data, file):
        return self.from_file(file)
    

class Byte(Type):
    def __init__(self):
        super().__init__(1)

    def get_type_name(self):
        return '{}()'.format(type(self).__name__)
    def create(self, uint8=0):
        assert 0 <= uint8 < 256
        return _T(self, uint8)
    def _to_bytes(self, data):
        return bytes([data])
    def _from_bytes(self, bs):
        bs = memoryview(bs)
        uint8, = bs
        return self.create(uint8)
    

class Word(Type):
    def __init__(self, size, endian):
        assert endian in {'big', 'little'}

        super().__init__(size)
        self.__endian = endian
        self.__up = (1 << (8*size))

    def get_type_name(self):
        return '{}({}, {!r})'.format(type(self).__name__,
                                     self.get_fixed_length(),
                                     self.__endian)

    def create(self, u=0):
        if not 0 <= u < self.__up:
            raise ValueError('not 0 <= u < {}'.format(self.__up))
        return _T(self, u)
    
    def _to_bytes(self, data):
        u = data
        return u.to_bytes(self.__size, self.__endian)
    def _from_bytes(self, bs):
        u = int.from_bytes(bs, self.__endian)
        return self.create(u)


class Pointer(Word):pass
class Position(Word):pass
class EnumFL(Word):pass # FL stands for fixed-length
class UintFL(Word):pass
##class FloatFL(Word):
##    def __init__(self, size):
##        super().__init__(size)


class Array(Type):
    def __init__(self, aTypeFL, length):
        if not isinstance(aTypeFL, Type):
            raise TypeError('not isinstance(aTypeFL, Type)')
        if not aTypeFL.is_fixed_length_type():
            raise TypeError('not {}.is_fixed_length_type()'
                            .format(aTypeFL.get_type_name()))
        check_uint(length)
        super().__init__(aTypeFL.get_fixed_length() * length)
        self.__t = aTypeFL
    def get_array_length(self):
        return self.get_fixed_length() // self.get_element_size()
    def get_element_type(self):
        return self.__t
    



    def get_element_type_name(self):
        return self.get_element_type().get_type_name()
    def get_element_size(self):
        return self.get_element_type().get_fixed_length()
    def get_type_name(self):
        return '{}({}, {})'.format(type(self).__name__,
                                   self.get_element_type_name(),
                                   self.get_array_length())

    def create(self, iterable=()):
        ls = tuple(iterable)
        L = self.get_array_length()
        
        if len(ls) > L:
            raise ValueError('too many elements')

        if not all(isinstance(e, _T) for e in ls) or \
           not all(e.is_of_type(self.get_element_type()) for e in ls):
            raise TypeError('not all {}'.format(self.get_element_type_name()))
        
        ls += (self.get_element_type().create(),) * (L - len(ls))
        return _T(self, ls)
    
    def _to_bytes(self, data):
        ls = data
        return b''.join(e.to_bytes() for e in ls)
    
    def _from_bytes(self, bs):
        L = self.get_element_size()
        from_bytes = self.get_element_type().from_bytes
        it = (from_bytes(bs[i:i+L]) for i in range(0, self.get_fixed_length(), L))
        return self.create(it)

class Tuple(Type):
    def __init__(self, iterable):
        # iterable<Type>

        types = tuple(iterable)
        if not all(isinstance(e, Type) for e in types):
            raise TypeError('not all Type')

        sz = None
        if all(e.is_fixed_length_type() for e in types):
            sz = sum(e.get_fixed_length() for e in types)
        super().__init__(sz)
        self.__ts = types
        return
    def get_element_types(self):
        return self.__ts

    def get_tuple_length(self):
        return len(self.get_element_types())
    def get_type_name(self):
        return '{}({})'.format(type(self).__name__,
                               ', '.join(e.get_type_name()
                                         for e in self.get_element_types())
                               )
    

    def create(self, iterable=()):
        ls = tuple(iterable)
        L = self.get_tuple_length()
        
        if len(ls) > L:
            raise ValueError('too many elements')

        if not all(isinstance(e, _T) for e in ls):
            raise TypeError('not all _T')
        if not all(e.is_of_type(t) for e,t in zip(ls, self.get_element_types())):
            for i, e, t in zip(range(len(ls)), ls, self.get_element_types()):
                if not e.is_of_type(t):
                    raise TypeError('{}th element is not of type {}'
                                    .format(i, t.get_type_name()))
            raise logic-error
        
        ls += tuple(t.create() for t in self.get_element_types()[len(ls):])
        return _T(self, ls)
    
    def _to_bytes(self, data):
        ls = data
        return b''.join(e.to_bytes() for e in ls)
    
    def _from_bytes(self, bs):
        obj, used_len = self.from_bytes_ex(bs, begin, end)
        if used_len != len(bs):
            assert used_len < len(bs)
            raise ValueError('too many bytes')
        return obj
    def from_bytes_ex(self, bs, begin, end):
        old_begin = begin
        ls = []
        for t in self.get_element_types():
            obj, used_len = t.from_bytes_ex(bs, begin, end)
            begin += used_len
            ls.append(obj)
        return self.create(ls), begin - old_begin
    




class List(Type):
    def __init__(self, aType):
        if not isinstance(aType, Type):
            raise TypeError('not isinstance(aType, Type)')
        super().__init__(None)
        self.__t = aType
    def get_element_type(self):
        return self.__t
    



    def get_element_type_name(self):
        return self.get_element_type().get_type_name()
    def get_element_size(self):
        return self.get_element_type().get_fixed_length()
    def get_type_name(self):
        return '{}({}, {})'.format(type(self).__name__,
                                   self.get_element_type_name())

    def create(self, iterable=()):
        ls = tuple(iterable)

        if not all(isinstance(e, _T) for e in ls) or \
           not all(e.is_of_type(self.get_element_type()) for e in ls):
            raise TypeError('not all {}'.format(self.get_element_type_name()))
        
        return _T(self, ls)
    
    def _to_bytes(self, data):
        ls = data
        return b''.join(e.to_bytes() for e in ls)
    

    def _from_bytes(self, bs,
                    *, end_pred):
        obj, used_len = self.from_bytes_ex(bs, begin, end, end_pred=end_pred)
        if used_len != len(bs):
            assert used_len < len(bs)
            raise ValueError('too many bytes')
        return obj
    def from_bytes_ex(self, bs, begin, end,
                      *, end_pred):
        # end_pred = lambda ls: return is_complete
        
        old_begin = begin
        ls = []
        t = self.get_element_type()
        while not end_pred(ls):
            obj, used_len = t.from_bytes_ex(bs, begin, end)
            begin += used_len
            ls.append(obj)
        return self.create(ls), begin - old_begin








