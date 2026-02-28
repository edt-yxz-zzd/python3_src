#__all__:goto
r'''[[[
e ../../python3_src/seed/types/WordSeq.py

seed.types.WordSeq
py -m nn_ns.app.debug_cmd   seed.types.WordSeq -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.WordSeq:__doc__ -ht # -ff -df
#######

[[
]]
[[
int.to_bytes(self, /, length=1, byteorder='big', *, signed=False)
int.from_bytes(bytes, byteorder='big', *, signed=False)
]]
[[
Struct(fmt) --> compiled struct object
    .format
    .size
    .unpack_from(self, /, buffer, offset=0)
    .iter_unpack(self, buffer, /)
    .unpack(self, buffer, /)
    .pack_into(buffer, offset, v1, v2, ...)
    .pack(v1, v2, ...) -> bytes
]]


'#'; __doc__ = r'#'
>>> from array import array, typecodes
>>> for tc in typecodes:
...     print((tc, array(tc).itemsize))
('b', 1)
('B', 1)
('u', 4)
('h', 2)
('H', 2)
('i', 4)
('I', 4)
('l', 8)
('L', 8)
('q', 8)
('Q', 8)
('f', 4)
('d', 8)
>>> for tc in 'BHILQ':
...     print((tc, array(tc).itemsize))
('B', 1)
('H', 2)
('I', 4)
('L', 8)
('Q', 8)


>>> array('f', [0])[0]
0.0
>>> array('u', [0])[0]
Traceback (most recent call last):
    ...
TypeError: array item must be unicode character
>>> array('u', 'A')[0]
'A'
>>> array('I', [-1])[0]
Traceback (most recent call last):
    ...
OverflowError: can't convert negative value to unsigned int
>>> array('x')
Traceback (most recent call last):
    ...
ValueError: bad typecode (must be b, B, u, h, H, i, I, l, L, q, Q, f or d)
>>> sorted(_itemsize2typecode.items())
[(1, 'B'), (2, 'H'), (4, 'I'), (8, 'L')]
>>> sorted(_struct_size2struct_format_string.items())
[(1, '=B'), (2, '=H'), (4, '=I'), (8, '=Q')]
































__repr__
>>> WordSeq()
WordSeq()
>>> WordSeq([])
WordSeq()
>>> WordSeq([0]*5)
WordSeq([0, 0, 0, 0, 0], 0)
>>> WordSeq(None, 0, 5, b'')
WordSeq([0, 0, 0, 0, 0], 0)
>>> WordSeq(range(254, 260))
WordSeq([254, 255, 256, 257, 258, 259], 2)
>>> WordSeq(range(111, 120))
WordSeq([111, 112, 113, 114, 115, 116, 117, 118, 119], 1)
>>> WordSeq(range(111, 120)).repr7impl_()
"WordSeq(None, 1, 9, b'opqrstuvw')"
>>> WordSeq.from_words(range(111, 120))
WordSeq([111, 112, 113, 114, 115, 116, 117, 118, 119], 1)
>>> WordSeq.from_bytes8words(1, 9, b'opqrstuvw')
WordSeq([111, 112, 113, 114, 115, 116, 117, 118, 119], 1)
>>> WordSeq(range(111, 120), 2)
WordSeq([111, 112, 113, 114, 115, 116, 117, 118, 119], 2)
>>> WordSeq.from_words(range(111, 120), 2)
WordSeq([111, 112, 113, 114, 115, 116, 117, 118, 119], 2)
>>> WordSeq(range(111, 120), 2).repr7impl_()
"WordSeq(None, 2, 9, b'o\\x00p\\x00q\\x00r\\x00s\\x00t\\x00u\\x00v\\x00w\\x00')"

>>> WordSeq(range(254, 260), imay_max_num_bytes4word=2)
WordSeq([254, 255, 256, 257, 258, 259], 2)
>>> WordSeq(range(254, 260), imay_max_num_bytes4word=1)
range(254, 260)
>>> WordSeq(range(111, 120), imay_max_num_bytes4word=1)
WordSeq([111, 112, 113, 114, 115, 116, 117, 118, 119], 1)
>>> WordSeq(range(111, 120), imay_max_num_bytes4word=0)
range(111, 120)
>>> WordSeq([*range(111, 120)], imay_max_num_bytes4word=0)
b'opqrstuvw'









__len__
>>> len(WordSeq())
0
>>> len(WordSeq(range(111, 120)))
9


__reversed__
>>> [*reversed(WordSeq(range(111, 120)))]
[119, 118, 117, 116, 115, 114, 113, 112, 111]
>>> [*iter(WordSeq(range(111, 120)))]
[111, 112, 113, 114, 115, 116, 117, 118, 119]

__getitem__
>>> WordSeq(range(111, 120))[7]
118
>>> WordSeq(range(111, 120))[7:-1]
WordSeq([118], 1)
>>> WordSeq([0]*5)[2:4]
WordSeq([0, 0], 0)


count
>>> WordSeq(range(111, 120)).count(111)
1
>>> WordSeq(range(111, 120)).count(120)
0


__contains__
>>> 111 in WordSeq(range(111, 120))
True
>>> 120 in WordSeq(range(111, 120))
False

>>> WordSeq(range(111, 120)).index(111)
0
>>> WordSeq(range(111, 120)).index(120)
Traceback (most recent call last):
    ...
ValueError: 120


__hash__
__lt__
>>> sorted({WordSeq(), WordSeq(range(111, 120))})
[WordSeq(), WordSeq([111, 112, 113, 114, 115, 116, 117, 118, 119], 1)]


__eq__
>>> WordSeq() == WordSeq(range(111, 120))
False
>>> WordSeq() != WordSeq(range(111, 120))
True
>>> WordSeq() <= WordSeq(range(111, 120))
True
>>> WordSeq() >= WordSeq(range(111, 120))
False
>>> WordSeq() <  WordSeq(range(111, 120))
True
>>> WordSeq() >  WordSeq(range(111, 120))
False

>>> WordSeq(range(111, 120)) == WordSeq(range(111, 120))
True
>>> WordSeq(range(111, 120)) != WordSeq(range(111, 120))
False
>>> WordSeq(range(111, 120)) <= WordSeq(range(111, 120))
True
>>> WordSeq(range(111, 120)) >= WordSeq(range(111, 120))
True
>>> WordSeq(range(111, 120)) <  WordSeq(range(111, 120))
False
>>> WordSeq(range(111, 120)) >  WordSeq(range(111, 120))
False





__add__
__mul__
__rmul__
>>> WordSeq(range(111, 120)) + WordSeq(range(254, 260))
WordSeq([111, 112, 113, 114, 115, 116, 117, 118, 119, 254, 255, 256, 257, 258, 259], 2)

>>> (WordSeq(range(111, 120)) + WordSeq(range(254, 260))).repr7impl_()
"WordSeq(None, 2, 15, b'o\\x00p\\x00q\\x00r\\x00s\\x00t\\x00u\\x00v\\x00w\\x00\\xfe\\x00\\xff\\x00\\x00\\x01\\x01\\x01\\x02\\x01\\x03\\x01')"
>>> 3*WordSeq(range(254, 260))
WordSeq([254, 255, 256, 257, 258, 259, 254, 255, 256, 257, 258, 259, 254, 255, 256, 257, 258, 259], 2)
>>> WordSeq(range(254, 260))*3
WordSeq([254, 255, 256, 257, 258, 259, 254, 255, 256, 257, 258, 259, 254, 255, 256, 257, 258, 259], 2)


__reduce__
>>> from pickle import dumps, loads
>>> dumps(WordSeq(range(254, 260)))
b'\x80\x04\x95;\x00\x00\x00\x00\x00\x00\x00\x8c\x12seed.types.WordSeq\x94\x8c\x07WordSeq\x94\x93\x94(NK\x02K\x06C\x0c\xfe\x00\xff\x00\x00\x01\x01\x01\x02\x01\x03\x01\x94t\x94R\x94.'
>>> loads(dumps(WordSeq(range(254, 260))))
WordSeq([254, 255, 256, 257, 258, 259], 2)


join
>>> WordSeq([], 2).join([WordSeq(range(254, 260)), WordSeq(range(260, 263))])
WordSeq([254, 255, 256, 257, 258, 259, 260, 261, 262], 2)
>>> WordSeq().join([WordSeq(range(254, 260)), WordSeq(range(260, 263))])
Traceback (most recent call last):
    ...
TypeError: ('num_bytes4word unmatched:', 0, 2)
>>> WordSeq().join([WordSeq(range(254, 260)), WordSeq(range(260, 263))], 2)
WordSeq([254, 255, 256, 257, 258, 259, 260, 261, 262], 2)
>>> WordSeq([333]).join([WordSeq(range(254, 260)), WordSeq(range(260, 263))], 2)
Traceback (most recent call last):
    ...
TypeError: ('reset num_bytes4word but sep not empty:', 2, WordSeq([333], 2))
>>> WordSeq([333]).join([WordSeq(range(254, 260)), WordSeq(range(260, 263))])
WordSeq([254, 255, 256, 257, 258, 259, 333, 260, 261, 262], 2)




#>>> for _ in map(print, dir(WordSeq())):pass
__hash__
__eq__
__ne__
__ge__
__gt__
__le__
__lt__

join
__reduce__
copy
__copy__
__deepcopy__
__new__
from_bytes8words
from_words
__add__
__mul__
__rmul__

__repr__
repr7impl_

__len__
__getitem__

iter_
__iter__
__reversed__

iter_index_
index
rindex
find
rfind
count
contains
__contains__

_pack
_unpack
num_bytes4word
max1_word
bytes8words













py_adhoc_call   seed.types.WordSeq   @f
]]]'''#'''

#__all__:goto
r'''[[[
[[
from array import array
===
DATA
    typecodes = 'bBuhHiIlLqQfd'
===
py_help array:array >> /sdcard/0my_files/tmp/-0tmp
view /sdcard/0my_files/tmp/-0tmp

class array(builtins.object)
 |  array(typecode [, initializer]) -> array
 |
 |  Return a new array whose items are restricted by typecode, and
 |  initialized from the optional initializer value, which must be a list,
 |  string or iterable over elements of the appropriate type.
 |
 |  Arrays represent basic values and behave very much like lists, except
 |  the type of objects stored in them is constrained. The type is specified
 |  at object creation time by using a type code, which is a single character.
 |  The following type codes are defined:
 |
 |      Type code   C Type             Minimum size in bytes
 |      'b'         signed integer     1
 |      'B'         unsigned integer   1
 |      'u'         Unicode character  2 (see note)
 |      'h'         signed integer     2
 |      'H'         unsigned integer   2
 |      'i'         signed integer     2
 |      'I'         unsigned integer   2
 |      'l'         signed integer     4
 |      'L'         unsigned integer   4
 |      'q'         signed integer     8 (see note)
 |      'Q'         unsigned integer   8 (see note)
 |      'f'         floating point     4
 |      'd'         floating point     8
 |
 |  NOTE: The 'u' typecode corresponds to Python's unicode character. On
 |  narrow builds this is 2-bytes on wide builds this is 4-bytes.
 |
 |  NOTE: The 'q' and 'Q' type codes are only available if the platform
 |  C compiler used to build Python supports 'long long', or, on Windows,
 |  '__int64'.
 |
 |  Methods:
 |
 |  append() -- append a new item to the end of the array
 |  buffer_info() -- return information giving the current memory info
 |  byteswap() -- byteswap all the items of the array
 |  count() -- return number of occurrences of an object
 |  extend() -- extend array by appending multiple elements from an iterable
 |  fromfile() -- read items from a file object
 |  fromlist() -- append items from the list
 |  frombytes() -- append items from the string
 |  index() -- return index of first occurrence of an object
 |  insert() -- insert a new item into the array at a provided position
 |  pop() -- remove and return item (default last)
 |  remove() -- remove first occurrence of an object
 |  reverse() -- reverse the order of the items in the array
 |  tofile() -- write all items to a file object
 |  tolist() -- return the array converted to an ordinary list
 |  tobytes() -- return the array converted to a string
 |
 |  Attributes:
 |
 |  typecode -- the typecode character used to create the array
 |  itemsize -- the length in bytes of one array item
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return key in self.
 |
 |  __copy__(self, /)
 |      Return a copy of the array.
 |
 |  __deepcopy__(self, unused, /)
 |      Return a copy of the array.
 |
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getitem__(self, key, /)
 |      Return self[key].
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __mul__(self, value, /)
 |      Return self*value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __reduce_ex__(self, value, /)
 |      Return state information for pickling.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __rmul__(self, value, /)
 |      Return value*self.
 |
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |
 |  __sizeof__(self, /)
 |      Size of the array in memory, in bytes.
 |
 |  append(self, v, /)
 |      Append new value v to the end of the array.
 |
 |  buffer_info(self, /)
 |      Return a tuple (address, length) giving the current memory address and the length in items of the buffer used to hold array's contents.
 |
 |      The length should be multiplied by the itemsize attribute to calculate
 |      the buffer length in bytes.
 |
 |  byteswap(self, /)
 |      Byteswap all items of the array.
 |
 |      If the items in the array are not 1, 2, 4, or 8 bytes in size, RuntimeError is
 |      raised.
 |
 |  count(self, v, /)
 |      Return number of occurrences of v in the array.
 |
 |  extend(self, bb, /)
 |      Append items to the end of the array.
 |
 |  frombytes(self, buffer, /)
 |      Appends items from the string, interpreting it as an array of machine values, as if it had been read from a file using the fromfile() method.
 |
 |  fromfile(self, f, n, /)
 |      Read n objects from the file object f and append them to the end of the array.
 |
 |  fromlist(self, list, /)
 |      Append items to array from list.
 |
 |  fromunicode(self, ustr, /)
 |      Extends this array with data from the unicode string ustr.
 |
 |      The array must be a unicode type array; otherwise a ValueError is raised.
 |      Use array.frombytes(ustr.encode(...)) to append Unicode data to an array of
 |      some other type.
 |
 |  index(self, v, start=0, stop=9223372036854775807, /)
 |      Return index of first occurrence of v in the array.
 |
 |      Raise ValueError if the value is not present.
 |
 |  insert(self, i, v, /)
 |      Insert a new item v into the array before position i.
 |
 |  pop(self, i=-1, /)
 |      Return the i-th element and delete it from the array.
 |
 |      i defaults to -1.
 |
 |  remove(self, v, /)
 |      Remove the first occurrence of v in the array.
 |
 |  reverse(self, /)
 |      Reverse the order of the items in the array.
 |
 |  tobytes(self, /)
 |      Convert the array to an array of machine values and return the bytes representation.
 |
 |  tofile(self, f, /)
 |      Write all items (as machine values) to the file object f.
 |
 |  tolist(self, /)
 |      Convert array to an ordinary list with the same items.
 |
 |  tounicode(self, /)
 |      Extends this array with data from the unicode string ustr.
 |
 |      Convert the array to a unicode string.  The array must be a unicode type array;
 |      otherwise a ValueError is raised.  Use array.tobytes().decode() to obtain a
 |      unicode string from an array of some other type.
 |
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  itemsize
 |      the size, in bytes, of one array item
 |
 |  typecode
 |      the typecode character used to create the array
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __hash__ = None

]]
[[
py_help struct >> /sdcard/0my_files/tmp/-0tmp

DESCRIPTION
    Functions to convert between Python values and C structs.
    Python bytes objects are used to hold the data representing the C struct
    and also as format strings (explained below) to describe the layout of data
    in the C struct.

    The optional first format char indicates byte order, size and alignment:
      @: native order, size & alignment (default)
      =: native order, std. size & alignment
      <: little-endian, std. size & alignment
      >: big-endian, std. size & alignment
      !: same as >

    The remaining chars indicate types of args and must match exactly;
    these can be preceded by a decimal repeat count:
      x: pad byte (no data); c:char; b:signed byte; B:unsigned byte;
      ?: _Bool (requires C99; if not available, char is used instead)
      h:short; H:unsigned short; i:int; I:unsigned int;
      l:long; L:unsigned long; f:float; d:double; e:half-float.
    Special cases (preceding decimal count indicates length):
      s:string (array of char); p: pascal string (with count byte).
    Special cases (only available in native format):
      n:ssize_t; N:size_t;
      P:an integer type that is wide enough to hold a pointer.
    Special case (not in native mode unless 'long long' in platform C):
      q:long long; Q:unsigned long long
    Whitespace between formats is ignored.

    The variable struct.error is an exception raised on errors.

CLASSES
    builtins.Exception(builtins.BaseException)
        error
    builtins.object
        _struct.Struct

    class Struct(builtins.object)
     |  Struct(fmt) --> compiled struct object
     |
     |  Methods defined here:
     |
     |  iter_unpack(self, buffer, /)
     |      Return an iterator yielding tuples.
     |
     |      Tuples are unpacked from the given bytes source, like a repeated
     |      invocation of unpack_from().
     |
     |      Requires that the bytes length be a multiple of the struct size.
     |
     |  pack(...)
     |      S.pack(v1, v2, ...) -> bytes
     |
     |      Return a bytes object containing values v1, v2, ... packed according
     |      to the format string S.format.  See help(struct) for more on format
     |      strings.
     |
     |  pack_into(...)
     |      S.pack_into(buffer, offset, v1, v2, ...)
     |
     |      Pack the values v1, v2, ... according to the format string S.format
     |      and write the packed bytes into the writable buffer buf starting at
     |      offset.  Note that the offset is a required argument.  See
     |      help(struct) for more on format strings.
     |
     |  unpack(self, buffer, /)
     |      Return a tuple containing unpacked values.
     |
     |      Unpack according to the format string Struct.format. The buffer's size
     |      in bytes must be Struct.size.
     |
     |      See help(struct) for more on format strings.
     |
     |  unpack_from(self, /, buffer, offset=0)
     |      Return a tuple containing unpacked values.
     |
     |      Values are unpacked according to the format string Struct.format.
     |
     |      The buffer's size in bytes, starting at position offset, must be
     |      at least Struct.size.
     |
     |      See help(struct) for more on format strings.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  format
     |      struct format string
     |
     |  size
     |      struct size in bytes




]]


]]]'''#'''

__all__ = r'''
mk_WordSeq
WordSeq
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from array import array
#.from struct import Struct
from collections.abc import Sequence# ByteSequence
from itertools import repeat #islice
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
with mk_ctx4lazy_import4funcs_(__name__):
    #.from seed.abc.abc__ver1 import abstractmethod, override, ABC
    #.from functools import singledispatch, singledispatchmethod
    from functools import total_ordering
    from seed.tiny_.to_may_int_ import to_may_int_

    from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_int_ge_lt, check_all_, check_may_
    from seed.helper.repr_input import repr_helper
    from seed.lang.class_property import class_property
    from seed.tiny_.containers import mk_immutable_seq
___end_mark_of_excluded_global_names__0___ = ...

def _mk_itemsize2typecode():
    from array import array
    d = {}
    for typecode in 'BHILQ':
        try:
            d.setdefault(array(typecode).itemsize, typecode)
        except ValueError:
            assert typecode == 'Q', typecode
    return d
_itemsize2typecode = _mk_itemsize2typecode()

def _mk_struct_size2struct_format_string():
    from struct import Struct
    d = {}
    for typecode in 'BHILQ':
        fmt = '=' + typecode
        try:
            d.setdefault(Struct(fmt).size, fmt)
        except ValueError:
            assert typecode == 'Q', typecode
            fmt = '!' + typecode
            d.setdefault(Struct(fmt).size, fmt)
    return d
_struct_size2struct_format_string = _mk_struct_size2struct_format_string()

#.class ICellSeq(Sequence):
#.    __slots__ = ()
#.    @class_property
#.    @abstractmethod
#.    def num_bytes4cell(cls, /):
#.        '-> uint'
#.    @abstractmethod
#.    def _cell2bytes_(cls, cell, /):
#.        'cell -> bytes'
#.    @abstractmethod
#.    def _cell5bytes_(cls, bs, /):
#.        'bytes -> cell'
#.    @abstractmethod
#.    def __bytes__(sf, bs, /):
#.        'ICellSeq -> bytes'
#.    @classmethod
#.    @abstractmethod
#.    def _from_bytes_(cls, bs, /):
#.        'bytes -> ICellSeq'
#.
#.    def to_bytes(sf, bs, /):
#.        'ICellSeq -> bytes'
#.    @classmethod
#.    def from_bytes(cls, bs, /):
#.        'bytes-like -> ICellSeq'
#.    @classmethod
#.    def from_cells(cls, cells, /):
#.        'Iter cell -> ICellSeq'
#.
#.
#.#class IStructSeq(ByteSequence, bytes):
#.class IStructSeq(Sequence):
#.    __slots__ = ()
#.    @class_property
#.    @abstractmethod
#.    def struct4item(cls, /):
#.        '-> py.struct.Struct'
#.    @class_property
#.    @abstractmethod
#.    def struct_format_string(cls, /):
#.        '-> str#py.struct.Struct.format'
#.        return cls.struct4item.format
#.    @class_property
#.    @abstractmethod
#.    def struct_size(cls, /):
#.        '-> uint#py.struct.Struct.size'
#.        return cls.struct4item.size
#.class WordSeq(IStructSeq):

r'''[[[
>>> v=memoryview(a:=array('H'))
>>> v
<memory at 0x...>
>>> len(v)
0
>>> a.append(7)
Traceback (most recent call last):
  ...
BufferError: cannot resize an array that is exporting buffers

]]]'''#'''
def _unpack_(num_bytes4word, offset, bs, /):
    '-> word/uint'
    return int.from_bytes(bs[offset:offset+num_bytes4word], byteorder='little', signed=False)
def _pack_(num_bytes4word, max1_word, word, /):
    check_int_ge_lt(0, max1_word, word)
    return word.to_bytes(num_bytes4word, byteorder='little', signed=False)
def _words2bytes_ex_(num_bytes4word, max1_word, words, /):
    check_int_ge(0, num_bytes4word)
    if num_bytes4word == 1 and type(words) is bytes:
        return words
    bss = []
    for word in words:
        #check_int_ge_lt(0, max1_word, word)
        bs = _pack_(num_bytes4word, max1_word, word)
        bss.append(bs)
    bs8words = b''.join(bss)
    num_words = len(bss)
    return (num_words, bs8words)
def _words2num_bytes4word_ex_(words, /):
    words = mk_immutable_seq(words)
    check_all_([check_int_ge, 0], words)
    max_word = max(words, default=0)
    num_bits4word = max_word.bit_length()
    num_bytes4word = (1+(-1+num_bits4word)//8)
    #num_bytes4word = max(1, num_bytes4word)
    return (words, num_bytes4word)

def mk_WordSeq(may_words=None, imay_num_bytes4word=-1, imay_num_words=-1, may_bytes8words=None, /, *, imay_max_num_bytes4word=-1):
    return WordSeq(may_words, imay_num_bytes4word, imay_num_words, may_bytes8words, imay_max_num_bytes4word=imay_max_num_bytes4word)

@total_ordering
class WordSeq(Sequence):
    #@singledispatch
    #@singledispatchmethod
    #def __new__(cls, may_xs__or__sz_bs_pair, /):
    #    if is_pair_(xs__or__sz_bs_pair)
    @classmethod
    def from_words(cls, words, imay_num_bytes4word=-1, /):
        check_int_ge(-1, imay_num_bytes4word)
        iter(words)
        return cls(words, imay_num_bytes4word)
    @classmethod
    def from_bytes8words(cls, num_bytes4word, num_words, bytes8words, /):
        check_int_ge(0, num_bytes4word)
        check_int_ge(0, num_words)
        check_type_is(bytes, bytes8words)
        return cls(may_words:=None, num_bytes4word, num_words, bytes8words)
    def __new__(cls, may_words=None, imay_num_bytes4word=-1, imay_num_words=-1, may_bytes8words=None, /, *, imay_max_num_bytes4word=-1):
        '-> (sf|words/(tuple/bytes))'
        match _std_args_(may_words, imay_num_bytes4word, imay_num_words, may_bytes8words, imay_max_num_bytes4word):
            case (True, words):
                return words
            case (False, (num_bytes4word, max1_word, num_words, bs8words)):
                pass
            case bad:
                raise 000
            #case
        assert len(bs8words) == num_bytes4word*num_words
        sf = super(__class__, cls).__new__(cls)
        sf._sz4w = num_bytes4word
        sf._m1w = max1_word
        sf._sz = num_words
        sf._bs = bs8words
        return sf
    def _pack(sf, word, /):
        return _pack_(sf.num_bytes4word, sf.max1_word, word)
    def _unpack(sf, offset, bs, /):
        return _unpack_(sf.num_bytes4word, offset, bs)
    def __repr__(sf, /):
        if not sf and sf.num_bytes4word == 0:
            return repr_helper(sf)
        return repr_helper(sf, [*sf], sf.num_bytes4word)
        #.if 0:
        #.    #cancelled <<== useless
        #.    #bug:if sf and sf.num_bytes4word <= 1:
        #.    if sf and sf.num_bytes4word == 1:
        #.        return repr_helper(sf, sf.bytes8words, sf.num_bytes4word)
        #.    if sf and sf.num_bytes4word == 0:
        #.        assert not sf.bytes8words
        #.        return repr_helper(sf, None, sf.num_bytes4word, len(sf), sf.bytes8words)
        #.return repr_helper(sf, [*sf], sf.num_bytes4word)
    def repr7impl_(sf, /):
        args = sf.__args
        return repr_helper(sf, *args)
    def __reduce__(sf, /):
        args = sf.__args
        return (__class__, args)
    @property
    def __args(sf, /):
        args = (None, sf.num_bytes4word, num_words:=len(sf), sf.bytes8words)
        return args
    def join(sf, word_seqs, imay_num_bytes4word=-1, /):
        'sf/WordSeq -> Iter WordSeq{[.num_bytes4word==sf.num_bytes4word]or[len==0]} -> WordSeq'
        check_int_ge(-1, imay_num_bytes4word)
        if imay_num_bytes4word == -1:
            num_bytes4word = sf.num_bytes4word
        else:
            num_bytes4word = imay_num_bytes4word
            if sf:raise TypeError('reset num_bytes4word but sep not empty:', imay_num_bytes4word, sf)
        num_bytes4word
        sep = sf.bytes8words
        sz4sf = len(sf)
        num_words = 0
        def __():
            nonlocal num_words
            it = iter(word_seqs)
            for j, word_seq in enumerate(it):
                check_type_le(WordSeq, word_seq)
                if word_seq and not word_seq.num_bytes4word == num_bytes4word:raise TypeError('num_bytes4word unmatched:', num_bytes4word, word_seq.num_bytes4word)
                if j:
                    yield sep
                    777;num_words += sz4sf
                yield word_seq.bytes8words
                777;num_words += len(word_seq)
        bs = b''.join(__())
        return type(sf).from_bytes8words(num_bytes4word, num_words, bs)
    @property
    def num_bytes4word(sf, /):
        return sf._sz4w
    @property
    def max1_word(sf, /):
        return sf._m1w
    @property
    def bytes8words(sf, /):
        return sf._bs
    def __len__(sf, /):
        return sf._sz
    def iter_(sf, /, *, reverse):
        if not sf:
            # MAYBE:[num_bytes4word == 0]
            return _null_iter
        # MAYBE:[num_bytes4word == 0]
        if not sf.num_bytes4word:
            assert not sf.bytes8words
            return repeat(0, len(sf))
        # [num_bytes4word > 0]
        assert sf.num_bytes4word, sf.__args
        bs8words = sf.bytes8words
        offsets = range(0, len(bs8words), sf.num_bytes4word)
        if reverse:
            offsets = reversed(offsets)
        return (sf._unpack(offset, bs8words) for offset in offsets)
    def __iter__(sf, /):
        return sf.iter_(reverse=False)
    def __reversed__(sf, /):
        return sf.iter_(reverse=True)
    def __getitem__(sf, j_or_sl, /):
        j_or_js = range(len(sf))[j_or_sl]
        cls = type(sf)
        if type(j_or_js) is range:
            js = j_or_js
            if not js:
                bs = b''
            elif js.step == 1:
                begin = js[0]*sf.num_bytes4word
                end = (1+js[-1])*sf.num_bytes4word
                bs = sf.bytes8words[begin:end]
            else:
                step = sf.num_bytes4word
                bs8words = sf.bytes8words
                bs = b''.join(bs8words[j*step:(1+j)*step] for j in js)
            bs
            return cls.from_bytes8words(sf.num_bytes4word, num_words:=len(js), bs)
        else:
            j = j_or_js
            u = sf._unpack(j*sf.num_bytes4word, sf.bytes8words)
            return u
        raise 000
    def count(sf, x, begin=None, end=None, step=None, /):
        return sum(1 for j in sf.iter_index_(x, begin, end, step))
    def __contains__(sf, x, /):
        return sf.contains(x)
    def contains(sf, x, begin=None, end=None, step=None, /, *, reverse=False):
        return not -1 == sf.find(x, begin, end, step, reverse=reverse)
    def find(sf, x, begin=None, end=None, step=None, /, *, reverse=False):
        for j in sf.iter_index_(x, begin, end, step, reverse=reverse):
            return j
        else:
            return -1
    def rfind(sf, x, begin=None, end=None, step=None, /, *, reverse=False):
        return sf.find(x, begin, end, step, reverse=not reverse)
    def index(sf, x, begin=None, end=None, step=None, /, *, reverse=False):
        if not -1 == (j:=sf.find(x, begin, end, step, reverse=reverse)):
            return j
        else:
            raise ValueError(x)
    def rindex(sf, x, begin=None, end=None, step=None, /, *, reverse=False):
        return sf.index(x, begin, end, step, reverse=not reverse)
    def iter_index_(sf, x, begin=None, end=None, step=None, /, *, reverse=False):
        if not sf:
            return _null_iter
        #.(begin, end, _1) = slice(begin, end, 1).indices(L:=len(sf))
        #.if not begin < end:
        #.    return _null_iter
        #.js = range(begin, end)
        js = range(len(sf))[begin:end:step]
        if not js:
            return _null_iter
        if reverse:
            js = reversed(js)
        if not None is (i:=to_may_int_(x)) and 0 <= i < sf.max1_word:
            bs4i = sf._pack(i)
            bs8words = sf.bytes8words
            num_bytes4word = sf.num_bytes4word
            return (j for j in js if bs8words.startswith(bs4i, j*num_bytes4word))
        return _null_iter
    #end-def iter_index_
    def copy(sf, /):
        return sf
    def __copy__(sf, /):
        return sf
    def __deepcopy__(sf, unused, /):
        return sf
    def __add__(sf, ot, /):
        if not isinstance(ot, cls:=type(sf)):
            return NotImplemented
        if not ot:
            return sf
        if not sf:
            return ot
        if sf.num_bytes4word == ot.num_bytes4word:
            return cls.from_bytes8words(sf.num_bytes4word, len(sf)+len(ot), sf.bytes8words + ot.bytes8words)
        return cls.from_words((*sf, *ot))
    def __mul__(sf, times, /):
        if not None is (i:=to_may_int_(times)):
            if not sf:
                return sf
            u = max(0, i)
            return type(sf).from_bytes8words(sf.num_bytes4word, len(sf)*u, sf.bytes8words*u)
        return NotImplemented
    def __rmul__(sf, times, /):
        if not None is (i:=to_may_int_(times)):
            return sf * i
        return NotImplemented
    def __hash__(sf, /):
        try:
            return sf.__h
        except AttributeError:
            pass
        args = sf.__args
        sf.__h = hash((type(sf), args))
        return hash(sf)
    def __eq__(sf, ot, /):
        if sf is ot:
            return True
        #.if not isinstance(ot, cls:=type(sf)):
        #.    return NotImplemented
        if not type(sf) is type(ot):
            return NotImplemented
        if not len(sf) == len(ot):
            return False
        if not hash(sf) == hash(ot):
            return False
        if sf.num_bytes4word == ot.num_bytes4word:
            return sf.bytes8words == ot.bytes8words
        return all(map(int.__eq__, sf, ot))
    def __le__(sf, ot, /):
        if sf is ot:
            return True
        #.if not isinstance(ot, cls:=type(sf)):
        #.    return NotImplemented
        if not type(sf) is type(ot):
            return NotImplemented
        for a, b in zip(sf, ot):
            if a == b:
                continue
            return a < b
        return len(sf) <= len(ot)

def _std_args_(may_words, imay_num_bytes4word, imay_num_words, may_bytes8words, imay_max_num_bytes4word, /):
    check_int_ge(-1, imay_num_bytes4word)
    check_int_ge(-1, imay_num_words)
    check_int_ge(-1, imay_max_num_bytes4word)
    check_may_([check_type_is, bytes], may_bytes8words)
    check_may_(iter, may_words)

    if not may_bytes8words is None:
        bs8words = may_bytes8words
        if not may_words is None: raise TypeError
        if not imay_max_num_bytes4word == -1: raise TypeError
        if imay_num_bytes4word == -1: raise TypeError
        num_bytes4word = imay_num_bytes4word
        if imay_num_words == -1: raise TypeError
        num_words = imay_num_words
        if not len(bs8words) == num_bytes4word*num_words: raise TypeError
        max1_word = (1<<(8*num_bytes4word))
    else:
        words = may_words if not may_words is None else _null_iter
        if not imay_num_words == -1: raise TypeError
        if imay_num_bytes4word == -1:
            (words, num_bytes4word) = _words2num_bytes4word_ex_(words)
        else:
            num_bytes4word = imay_num_bytes4word
        (words, num_bytes4word)
        if not num_bytes4word >= 0:raise 000
        if not -1 == (max_num_bytes4word:=imay_max_num_bytes4word) and not num_bytes4word <= max_num_bytes4word:
            #words = mk_immutable_seq(words)
            (words, num_bytes4word) = _words2num_bytes4word_ex_(words)
            if not type(words) in (bytes, range) and num_bytes4word <= 1:
                words = bytes(words)
            return (bypass:=True, words)
        num_bytes4word
        #xxx:words = iter(words)
            #_words2bytes_ex_ will detect bytes@[num_bytes4word==1]
        max1_word = (1<<(8*num_bytes4word))
        (num_words, bs8words) = _words2bytes_ex_(num_bytes4word, max1_word, words)
        if not len(bs8words) == num_bytes4word*num_words: raise 000

    return (bypass:=False, (num_bytes4word, max1_word, num_words, bs8words))
    return (num_bytes4word, max1_word, num_words, bs8words)
#end-def _std_args_(may_words, imay_num_bytes4word, imay_num_words, may_bytes8words, /):

_null_iter =  iter('')
__all__
from seed.types.WordSeq import WordSeq
from seed.types.WordSeq import mk_WordSeq
#def mk_WordSeq(may_words=None, imay_num_bytes4word=-1, imay_num_words=-1, may_bytes8words=None, /, *, imay_max_num_bytes4word=-1):
from seed.types.WordSeq import *
