#__all__:goto
r'''
e ../../python3_src/nn_ns/codec/DecodeUtils.py
view ../../python3_src/seed/io/with4seekback.py
view ../../python3_src/seed/helper/with4cleanup.py

nn_ns.codec.DecodeUtils

assume file opened in 'rb' mode
assume using uint32le as integer in file

py -m nn_ns.app.debug_cmd   nn_ns.codec.DecodeUtils
py -m nn_ns.app.debug_cmd   nn_ns.codec.DecodeUtils -x
py -m nn_ns.app.doctest_cmd nn_ns.codec.DecodeUtils:__doc__ -v
py -m nn_ns.app.doctest_cmd nn_ns.codec.DecodeUtils!

py -m nn_ns.app.adhoc_argparser__main__call8module   nn_ns.codec.DecodeUtils @_test_warn_in__is_read_result_ignoreable



from nn_ns.codec.DecodeUtils import CheckError, StreamError, StreamEOFError, SeekError, ReadError, ReadError__NamedDependentTupleReader, ReadError__SeekAddrReader
from nn_ns.codec.DecodeUtils import IDecoder, IReader

from nn_ns.codec.DecodeUtils import apply_decoder, apply_reader, try_apply_decoder, try_apply_reader


from nn_ns.codec.DecodeUtils import read_bytes, skip_bytes, checked_seek, get_size_of_ibfile, size5or_size_reader__, uint5or_uint_reader__, uint_or2uint_reader_

from nn_ns.codec.DecodeUtils import check__int_or_int_reader, int5or_int_reader__, int_or2int_reader_, offset5or_offset_reader__, offset_or2offset_reader_

from nn_ns.codec.DecodeUtils import echo_decoder, uintLE_decoder, uintBE_decoder

from nn_ns.codec.DecodeUtils import StrDecoder, ascii_decoder, u8_decoder, gb_decoder

from nn_ns.codec.DecodeUtils import uint32LE_reader, uint64LE_reader

from nn_ns.codec.DecodeUtils import BytesReader, ConstantInOutReader, mk_ConstantTargetReader, mk_ConstantBytesMatcher, UntilEndValueBytesReader

from nn_ns.codec.DecodeUtils import tell_addr_reader, mk_AddrAssertionReader, eof_addr_reader
from nn_ns.codec.DecodeUtils import OffsetReader, AddrReader, SeekAddrReader

from nn_ns.codec.DecodeUtils import ArrayReader, TupleReader, DependentPairReader, NamedTupleReader, NamedDependentTupleReader, ipop_and_drop4list, UntilEndValueArrayReader, UntilReadEndValueArrayReader #!!! NOTE:NamedTupleReader/NamedDependentTupleReader read result NamedTuple, using 『NamedTuple.as_getter4named_tuple()』to access attr !!!

from nn_ns.codec.DecodeUtils import FallbackReader, SkipReader, FurtherTransformReader, AssertionReader

from nn_ns.codec.DecodeUtils import AddrDereferenceReader, AddrSizedParamReader, AddrSizedParamArrayReader, ArrayTranformReader



from nn_ns.codec.DecodeUtils import *

[[DONE:reader:array/bytes,until...
    * by: end value
    * by: end reader
    ++to_drop_end_bytes
    ++to_drop_end_obj
UntilEndValueBytesReader

try_apply_decoder
try_apply_reader
ipop_and_drop4list
    UntilEndValueArrayReader
    UntilReadEndValueArrayReader
]]
[[DONE:test:export:
    TellAddrReader
        tell_addr_reader
        mk_AddrAssertionReader
    EOFAddrReader
        eof_addr_reader
        file_size_reader
    OffsetReader
    AddrReader
    SeekAddrReader
        ++to_read_bytes
        ++allowed_to_read_bytes_on_seekback
]]




>>> from nn_ns.codec.DecodeUtils import *


>>> from seed.func_tools.dot2 import dot
>>> from seed.tiny import lazy_raise

>>> from seed.types.NamedTuple__split_table import NamedTuple, Descriptor4NamedTuple, gmk_Descriptor4NamedTuple
>>> gmk_Descriptor4NamedTuple('aa')
Traceback (most recent call last):
    ...
KeyError: "duplicate_names: ['a']"
>>> abc123 = NamedTuple([('a', 111), ('b', 222), ('c', 333)])
>>> ns = abc123.as_getter4named_tuple()
>>> ns
_Getter4NamedTuple(NamedTuple([('a', 111), ('b', 222), ('c', 333)]))
>>> abc123.a
Traceback (most recent call last):
    ...
AttributeError: 'NamedTuple' object has no attribute 'a'
>>> ns.a
111

!!! NOTE:NamedTupleReader/NamedDependentTupleReader read result NamedTuple, using 『NamedTuple.as_getter4named_tuple()』to access attr !!!


'''  r'''
>>> from io import BytesIO
>>> ibfile = BytesIO(b'0123456789')



#checked_seek
>>> ibfile.tell()
0
>>> ibfile.seek(11) #!!!
11
>>> ibfile.tell()
11
>>> ibfile.seek(999) #!!!
999
>>> ibfile.tell()
999
>>> get_size_of_ibfile(ibfile)
10
>>> ibfile.tell()
999
>>> ibfile.read(1)
b''
>>> ibfile.tell()
999
>>> get_size_of_ibfile(ibfile)
10

>>> ibfile.seek(-1) #!!!
Traceback (most recent call last):
    ...
ValueError: negative seek value -1
>>> ibfile.tell()
999
>>> checked_seek(ibfile, 5)
>>> ibfile.tell()
5
>>> checked_seek(ibfile, -1)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.SeekError__pass_BOF
>>> ibfile.tell()
5
>>> checked_seek(ibfile, 0)
>>> ibfile.tell()
0
>>> checked_seek(ibfile, 10)
>>> ibfile.tell()
10
>>> checked_seek(ibfile, 11) #!!!
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.SeekError__pass_EOF



#get_size_of_ibfile
#skip_bytes
>>> get_size_of_ibfile(ibfile)
10
>>> checked_seek(ibfile, 5)
>>> ibfile.tell()
5
>>> skip_bytes(ibfile, 6)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.SeekError__pass_EOF
>>> ibfile.tell()
5
>>> skip_bytes(ibfile, 5)
>>> ibfile.tell()
10


#apply_decoder
>>> echo_decoder is EchoDecoder()
True
>>> echo_decoder
EchoDecoder()
>>> ascii_decoder
StrDecoder('ascii')
>>> gb_decoder
StrDecoder('gb18030')
>>> u8_decoder
StrDecoder('utf8')
>>> zlib_decoder
PyDecoder('zlib')
>>> u8_zlib_decoder
ComposeDecoder(StrDecoder('utf8'), PyDecoder('zlib'))

>>> sa = 'abcd'
>>> s = '甲乙丙丁'
>>> ba = sa.encode('ascii')
>>> gb = s.encode('gb18030')
>>> u8 = s.encode('utf8')
>>> zu8 = codecs.encode(u8, 'zlib')
>>> ba
b'abcd'
>>> gb
b'\xbc\xd7\xd2\xd2\xb1\xfb\xb6\xa1'
>>> u8
b'\xe7\x94\xb2\xe4\xb9\x99\xe4\xb8\x99\xe4\xb8\x81'
>>> zu8
b'x\x9c{>e\xd3\x93\x9d3\x9f\xec\x00\xa2F\x00:\x1c\x08\xb6'
>>> apply_decoder(echo_decoder, ba) == ba
True
>>> apply_decoder(echo_decoder, u8) == u8
True
>>> apply_decoder(ascii_decoder, ba) == sa
True
>>> apply_decoder(gb_decoder, gb) == s
True
>>> apply_decoder(u8_decoder, u8) == s
True
>>> apply_decoder(zlib_decoder, zu8) == u8
True
>>> apply_decoder(u8_zlib_decoder, zu8) == s
True


>>> uintBE_decoder
IntDecoder(False, 'big')
>>> bs = bytes.fromhex('81 02 03 84')
>>> apply_decoder(uintBE_decoder, bs) == 0x81_02_03_84
True
>>> apply_decoder(uintLE_decoder, bs) == 0x84_03_02_81
True

>>> apply_decoder(sintBE_decoder, bs) == -0x7efdfc7c
True
>>> apply_decoder(sintLE_decoder, bs) == -0x7bfcfd7f
True




'''  r'''

#apply_reader
>>> bs = bytes.fromhex('81 02 03 84 05 06')
>>> ibfile = BytesIO(bs)
>>> size5or_size_reader__(ibfile, 555)
555
>>> size5or_size_reader__(ibfile, -1)
Traceback (most recent call last):
    ...
TypeError
>>> size5or_size_reader__(ibfile, uint32BE_reader) == 0x81_02_03_84
True
>>> ibfile.tell()
4
>>> size5or_size_reader__(ibfile, uint32LE_reader)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.StreamEOFError: too few bytes
>>> ibfile.seek(0)
0
>>> size5or_size_reader__(ibfile, uint32LE_reader) == 0x84_03_02_81
True


>>> uintBE_decoder
IntDecoder(False, 'big')
>>> uint32BE_reader
BytesReader(4, IntDecoder(False, 'big'))
>>> uint32BE_reader.is_read_result_ignoreable()
False
>>> uint32BE_reader.get_may_static_num_bytes4skip()
4

>>> ibfile.seek(0)
0
>>> apply_reader(uint32BE_reader, ibfile) == 0x81_02_03_84
True
>>> ibfile.seek(0)
0
>>> apply_reader(uint32LE_reader, ibfile) == 0x84_03_02_81
True
>>> ibfile.seek(0)
0
>>> apply_reader(sint32BE_reader, ibfile) == -0x7efdfc7c
True
>>> ibfile.seek(0)
0
>>> apply_reader(sint32LE_reader, ibfile) == -0x7bfcfd7f
True
>>> ibfile.seek(0)
0
>>> apply_reader(uint16BE_reader, ibfile) == 0x81_02
True
>>> ibfile.tell()
2
>>> ibfile.seek(0)
0
>>> apply_reader(uint64LE_reader, ibfile)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.StreamEOFError: too few bytes


>>> ibfile.seek(0)
0
>>> apply_reader(sint32BE_reader, ibfile, skip_only=True)
>>> ibfile.tell()
4


'''  r'''

# 『\o』八进制
>>> [*b'\\']
[92]
>>> [*b'\9']
[92, 57]
>>> [*b'\8']
[92, 56]
>>> [*b'\7']
[7]
>>> ibfile = BytesIO(b'\5\7\4\3\2\1xyz')
>>> reader = BytesReader(uint8LE_reader)
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
b'\x07\x04\x03\x02\x01'
>>> ibfile.tell()
6
>>> ibfile.seek(0)
0
>>> reader = BytesReader(uint8LE_reader, uintBE_decoder)
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile) == 0x0704030201
True
>>> ibfile.tell()
6



'''  r'''
    ConstantInOutReader
        mk_ConstantTargetReader
        mk_ConstantBytesMatcher

>>> bs = b'233,233,223,223'
>>> ibfile = BytesIO(bs)
>>> an_ignoreable_reader = reader = ConstantInOutReader(b'233,', 777)
>>> reader
ConstantInOutReader(b'233,', 777)
>>> reader.get_may_static_num_bytes4skip()
4
>>> an_ignoreable_reader.is_read_result_ignoreable()
True
>>> apply_reader(reader, ibfile)
777
>>> apply_reader(reader, ibfile)
777
>>> apply_reader(reader, ibfile)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.CheckError: not the given bytes in file : b'223,' != b'233,'
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> apply_reader(reader, ibfile, skip_only=True)
>>> apply_reader(reader, ibfile, skip_only=True)
>>> apply_reader(reader, ibfile, skip_only=True)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.SeekError__pass_EOF



>>> ibfile.seek(0)
0
>>> reader = mk_ConstantTargetReader(777)
>>> reader
ConstantInOutReader(b'', 777)
>>> reader.get_may_static_num_bytes4skip()
0
>>> apply_reader(reader, ibfile)
777
>>> ibfile.tell()
0
>>> reader = mk_ConstantBytesMatcher(b'233,')
>>> reader
ConstantInOutReader(b'233,', None)
>>> reader.get_may_static_num_bytes4skip()
4
>>> apply_reader(reader, ibfile)
>>> apply_reader(reader, ibfile)
>>> ibfile.tell()
8
>>> apply_reader(reader, ibfile)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.CheckError: not the given bytes in file : b'223,' != b'233,'
>>> ibfile.tell()
12


'''  r'''
    FallbackReader
        IgnoreableReader
            SkipReader
    FurtherTransformReader
    AssertionReader
>>> PostprocessReader is FurtherTransformReader
True


>>> bs = b'0123456789'
>>> ibfile = BytesIO(bs)
>>> the_wrapped_reader = BytesReader(3)
>>> reader = FallbackReader(the_wrapped_reader)
>>> reader
FallbackReader(BytesReader(3))
>>> reader.the_wrapped_reader is the_wrapped_reader
True
>>> reader.get_may_static_num_bytes4skip()
3
>>> apply_reader(reader, ibfile)
b'012'
>>> apply_reader(reader, ibfile)
b'345'
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
9
>>> reader.is_read_result_ignoreable()
False
>>> FallbackReader(an_ignoreable_reader).is_read_result_ignoreable()
True


>>> ibfile.seek(0)
0
>>> reader = IgnoreableReader(the_wrapped_reader)
>>> reader
IgnoreableReader(BytesReader(3))
>>> reader.the_wrapped_reader is the_wrapped_reader
True
>>> reader.get_may_static_num_bytes4skip()
3
>>> apply_reader(reader, ibfile)
b'012'
>>> apply_reader(reader, ibfile)
b'345'
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
9
>>> reader.is_read_result_ignoreable()
True


>>> ibfile.seek(0)
0
>>> reader = SkipReader(the_wrapped_reader)
>>> reader
SkipReader(BytesReader(3))
>>> reader.the_wrapped_reader is the_wrapped_reader
True
>>> reader.get_may_static_num_bytes4skip()
3
>>> apply_reader(reader, ibfile)
>>> apply_reader(reader, ibfile)
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
9
>>> reader.is_read_result_ignoreable()
True


>>> ibfile.seek(0)
0
>>> reader = FurtherTransformReader(list, the_wrapped_reader)
>>> reader
FurtherTransformReader(<class 'list'>, BytesReader(3))
>>> reader.get_may_static_num_bytes4skip()
3
>>> apply_reader(reader, ibfile) #-> [0x30,0x31,0x32] #b'012'
[48, 49, 50]
>>> apply_reader(reader, ibfile)
[51, 52, 53]
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
9
>>> reader.is_read_result_ignoreable()
False
>>> FurtherTransformReader(list, an_ignoreable_reader).is_read_result_ignoreable() #!!! since added postprocess, the result will be used
False


>>> ibfile.seek(0)
0
>>> reader = AssertionReader(b'012', the_wrapped_reader)
>>> reader
AssertionReader(b'012', BytesReader(3))
>>> reader.get_may_static_num_bytes4skip()
3
>>> apply_reader(reader, ibfile)
>>> ibfile.tell()
3
>>> apply_reader(reader, ibfile)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.CheckError: (b'012', b'345')
>>> ibfile.tell()
6
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
9
>>> reader.is_read_result_ignoreable()
True



'''  r'''
    ArrayReader
    TupleReader
    DependentPairReader
    NamedTupleReader
    NamedDependentTupleReader
        ++to_read_ex
            #result4ex :: (result/NamedTuple, _result4ex/((begin_addr4whole, end_addr4whole), ls4ex/[((begin_addr,end_addr), (is_xname_exported, is_xname_refered), (xname, idx4xname), may_obj)]))

IReader.get_may_static_num_bytes4skip(), `xname` ==>>:
ArrayReader(sz, uint16BE_reader)
ArrayReader(sz, BytesReader(sz_reader))
ArrayReader(sz_reader, uint16BE_reader)
TupleReader(uint16BE_reader, uint32LE_reader)
TupleReader(uint16BE_reader, BytesReader(sz_reader))
DependentPairReader(sz_reader, BytesReader)
NamedTupleReader([('a', uint16BE_reader), ('b', uint32LE_reader)])
NamedTupleReader([('a', uint16BE_reader), ('b', BytesReader(sz_reader))])
NamedTupleReader([('', uint16BE_reader), ('#b', uint32LE_reader)])
NamedDependentTupleReader([('a', uint16BE_reader, None), ('b', uint32LE_reader, None)])
NamedDependentTupleReader([('a', sz_reader, None), ('b', BytesReader, ['a'])])
NamedDependentTupleReader([('', uint16BE_reader, None), ('', uint32LE_reader, None)])
NamedDependentTupleReader([('a', sz_reader, None), ('#b', BytesReader, ['a'])])
NamedDependentTupleReader([('a', sz_reader, None), ('#b', BytesReader, ['a']), ('c', sz_reader, None), ('', lambda:BytesReader(2), [])], to_read_ex=True)



>>> hex(ord('a'))
'0x61'
>>> hex(ord('A'))
'0x41'
>>> hex(ord('0'))
'0x30'
>>> chr(0x51)
'Q'
>>> elem_reader = uint16BE_reader
>>> sz_reader = uint8LE_reader
>>> sz = 2
>>> bs = b'\2\1\3\4\5abcdef'
>>> ibfile = BytesIO(bs)





ArrayReader(sz, uint16BE_reader)
ArrayReader(sz, BytesReader(sz_reader))
ArrayReader(sz_reader, uint16BE_reader)

>>> reader = ArrayReader(sz, uint16BE_reader)
>>> reader
ArrayReader(2, BytesReader(2, IntDecoder(False, 'big')))
>>> reader.get_may_static_num_bytes4skip()
4
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(1)
1
>>> apply_reader(reader, ibfile) == [0x0103, 0x0405]
True
>>> ibfile.tell()
5
>>> ibfile.seek(1)
1
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
5


>>> reader = ArrayReader(sz, BytesReader(sz_reader))
>>> reader
ArrayReader(2, BytesReader(BytesReader(1, IntDecoder(False, 'little'))))
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(1)
1
>>> apply_reader(reader, ibfile) == [b'\3', b'\5abc']
True
>>> ibfile.tell()
8
>>> ibfile.seek(1)
1
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
8


>>> reader = ArrayReader(sz_reader, uint16BE_reader)
>>> reader
ArrayReader(BytesReader(1, IntDecoder(False, 'little')), BytesReader(2, IntDecoder(False, 'big')))
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile) == [0x0103, 0x0405]
True
>>> ibfile.tell()
5
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
5



TupleReader(uint16BE_reader, uint32LE_reader)
TupleReader(uint16BE_reader, BytesReader(sz_reader))

>>> reader = TupleReader(uint16BE_reader, uint32LE_reader)
>>> reader
TupleReader(BytesReader(2, IntDecoder(False, 'big')), BytesReader(4, IntDecoder(False, 'little')))
>>> reader.get_may_static_num_bytes4skip()
6
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile) == (0x0201, 0x61050403)
True
>>> ibfile.tell()
6
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6


>>> reader = TupleReader(uint16BE_reader, BytesReader(sz_reader))
>>> reader
TupleReader(BytesReader(2, IntDecoder(False, 'big')), BytesReader(BytesReader(1, IntDecoder(False, 'little'))))
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile) == (0x0201, b'\4\5a')
True
>>> ibfile.tell()
6
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6



DependentPairReader(sz_reader, BytesReader)
>>> reader = DependentPairReader(sz_reader, BytesReader)
>>> reader
DependentPairReader(BytesReader(1, IntDecoder(False, 'little')), <class 'nn_ns.codec.DecodeUtils.BytesReader'>)
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile) == (0x02, b'\1\3')
True
>>> ibfile.tell()
3
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
3





NamedTupleReader([('a', uint16BE_reader), ('b', uint32LE_reader)])
NamedTupleReader([('a', uint16BE_reader), ('b', BytesReader(sz_reader))])
NamedTupleReader([('', uint16BE_reader), ('#b', uint32LE_reader)])

>>> reader = NamedTupleReader([('a', uint16BE_reader), ('b', uint32LE_reader)])
>>> reader
NamedTupleReader([('a', BytesReader(2, IntDecoder(False, 'big'))), ('b', BytesReader(4, IntDecoder(False, 'little')))])
>>> reader.get_may_static_num_bytes4skip()
6
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile) # as-if == (0x0201, 0x61050403)
NamedTuple([('a', 513), ('b', 1627718659)])
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile) == NamedTuple([('a', 0x0201), ('b', 0x61050403)]) != (0x0201, 0x61050403)
True
>>> ibfile.tell()
6
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6


>>> reader = NamedTupleReader([('a', uint16BE_reader), ('b', BytesReader(sz_reader))])
>>> reader
NamedTupleReader([('a', BytesReader(2, IntDecoder(False, 'big'))), ('b', BytesReader(BytesReader(1, IntDecoder(False, 'little'))))])
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile) == NamedTuple([('a', 0x0201), ('b', b'\4\5a')]) != (0x0201, b'\4\5a')
True
>>> ibfile.tell()
6
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6


>>> reader = NamedTupleReader([('', uint16BE_reader), ('#b', uint32LE_reader)])
>>> reader
NamedTupleReader([('', BytesReader(2, IntDecoder(False, 'big'))), ('#b', BytesReader(4, IntDecoder(False, 'little')))])
>>> reader.get_may_static_num_bytes4skip()
6
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
NamedTuple([])
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile) == NamedTuple([]) != ()
True
>>> ibfile.tell()
6
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6






NamedDependentTupleReader([('a', uint16BE_reader, None), ('b', uint32LE_reader, None)])
NamedDependentTupleReader([('a', sz_reader, None), ('b', BytesReader, ['a'])])
NamedDependentTupleReader([('', uint16BE_reader, None), ('', uint32LE_reader, None)])
NamedDependentTupleReader([('a', sz_reader, None), ('#b', BytesReader, ['a'])])
NamedDependentTupleReader([('a', sz_reader, None), ('#b', BytesReader, ['a']), ('c', sz_reader, None), ('', lambda:BytesReader(2), [])], to_read_ex=True)


>>> reader = NamedDependentTupleReader([('a', uint16BE_reader, None), ('b', uint32LE_reader, None)])
>>> reader
NamedDependentTupleReader([('a', BytesReader(2, IntDecoder(False, 'big')), None), ('b', BytesReader(4, IntDecoder(False, 'little')), None)])
>>> reader.get_may_static_num_bytes4skip()
6
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile) # as-if == (0x0201, 0x61050403)
NamedTuple([('a', 513), ('b', 1627718659)])
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile) == NamedTuple([('a', 0x0201), ('b', 0x61050403)]) != (0x0201, 0x61050403)
True
>>> ibfile.tell()
6
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6



>>> reader = NamedDependentTupleReader([('a', sz_reader, None), ('b', BytesReader, ['a'])])
>>> reader
NamedDependentTupleReader([('a', BytesReader(1, IntDecoder(False, 'little')), None), ('b', <class 'nn_ns.codec.DecodeUtils.BytesReader'>, ['a'])])
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
NamedTuple([('a', 2), ('b', b'\x01\x03')])
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile) == NamedTuple([('a', 0x02), ('b', b'\1\3')]) != (0x02, b'\1\3')
True
>>> ibfile.tell()
3
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
3



>>> reader = NamedDependentTupleReader([('', uint16BE_reader, None), ('', uint32LE_reader, None)])
>>> reader
NamedDependentTupleReader([('', BytesReader(2, IntDecoder(False, 'big')), None), ('', BytesReader(4, IntDecoder(False, 'little')), None)])
>>> reader.get_may_static_num_bytes4skip()
6
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
NamedTuple([])
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile) == NamedTuple([]) != ()
True
>>> ibfile.tell()
6
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6


>>> reader = NamedDependentTupleReader([('a', sz_reader, None), ('#b', BytesReader, ['a'])])
>>> reader
NamedDependentTupleReader([('a', BytesReader(1, IntDecoder(False, 'little')), None), ('#b', <class 'nn_ns.codec.DecodeUtils.BytesReader'>, ['a'])])
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
NamedTuple([('a', 2)])
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile) == NamedTuple([('a', 0x02)]) != (0x02,)
True
>>> ibfile.tell()
3
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
3



>>> reader = NamedDependentTupleReader([('a', sz_reader, None), ('#b', BytesReader, ['a']), ('c', sz_reader, None), ('', lambda:BytesReader(2), [])], to_read_ex=True)
>>> reader #doctest: +ELLIPSIS
NamedDependentTupleReader([('a', BytesReader(1, IntDecoder(False, 'little')), None), ('#b', <class 'nn_ns.codec.DecodeUtils.BytesReader'>, ['a']), ('c', BytesReader(1, IntDecoder(False, 'little')), None), ('', <function <lambda> at 0x...>, [])], to_read_ex = True)
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
(NamedTuple([('a', 2), ('c', 4)]), ((0, 6), [((0, 1), (True, True), ('a', 0), 2), ((1, 3), (False, False), ('#b', 1), b'\x01\x03'), ((3, 4), (True, False), ('c', 2), 4), ((4, 6), (False, False), ('', 3), b'\x05a')]))
>>> ibfile.tell()
6
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6





'''  r'''
    AddrDereferenceReader
    AddrSizedParamReader
    AddrSizedParamArrayReader
    ArrayTranformReader

AddrDereferenceReader(addr_param_reader, obj_reader5param_)
AddrDereferenceReader(varaddr_param_reader, obj_reader5param_)
AddrDereferenceReader(addr_varparam_reader, obj_reader5param_)

    #addr_param_reader --> addr_or_addr_param_pair_or_reader
    #obj_reader5param_ --> obj_reader_or5Mparam
AddrDereferenceReader(addr_param_pair, obj_reader)
AddrDereferenceReader(addr, obj_reader)



AddrSizedParamReader
    def __init__(sf, addr_or_addr_reader, param_reader, may_end_addr4target, /):

#for .get_may_static_num_bytes4skip()
AddrSizedParamReader(11, sz_reader, None)
AddrSizedParamReader(11, a_varsz_reader, None)
AddrSizedParamReader(addr_reader, sz_reader, None)
AddrSizedParamReader(a_varaddr_reader, sz_reader, None)

seek(5)end=13
AddrSizedParamReader(11, sz_reader, None) #buggy
AddrSizedParamReader(11, sz_reader, addr_reader) #fix above bug
AddrSizedParamReader(11, sz_reader, 13)
seek(3)end=13
AddrSizedParamReader(addr_reader, sz_reader, None)
AddrSizedParamReader(addr_reader, sz_reader, 13)

AddrDereferenceReader+AddrSizedParamReader
def obj_reader5param_(sized_param, /):
    (size4target, param) = sized_param
    return BytesReader(sized_param)
AddrDereferenceReader(AddrSizedParamReader(addr_reader, sz_reader, None), obj_reader5param_)
obj_reader5param_ = dot[BytesReader, fst_]
AddrDereferenceReader(AddrSizedParamReader(addr_reader, sz_reader, None), obj_reader5param_)


AddrSizedParamArrayReader
    def __init__(sf, len_array, may_end_addr4last_target, addr_reader, may_param_reader, may_obj_reader5sized_param_=None, /):
#for .get_may_static_num_bytes4skip()
AddrSizedParamArrayReader(0, None, a_varaddr_reader, a_varsz_reader, lazy_raise)
AddrSizedParamArrayReader(1, None, a_varaddr_reader, a_varsz_reader, lazy_raise)
AddrSizedParamArrayReader(2, None, addr_reader, sz_reader, obj_reader5sized_param_)
AddrSizedParamArrayReader(2, None, addr_reader, a_varsz_reader, obj_reader5sized_param_)
AddrSizedParamArrayReader(2, None, a_varaddr_reader, sz_reader, obj_reader5sized_param_)
AddrSizedParamArrayReader(3, None, addr_reader, sz_reader, obj_reader5sized_param_)
AddrSizedParamArrayReader(4, None, addr_reader, sz_reader, obj_reader5sized_param_)

#seek(0)end=10,11,13,16
AddrSizedParamArrayReader(0, 10, a_varaddr_reader, a_varsz_reader, lazy_raise)
AddrSizedParamArrayReader(1, 11, addr_reader, sz_reader, obj_reader5sized_param_)
AddrSizedParamArrayReader(1, 11, addr_reader, a_varsz_reader, obj_reader5sized_param_)
AddrSizedParamArrayReader(1, 11, a_varaddr_reader, sz_reader, obj_reader5sized_param_)
AddrSizedParamArrayReader(2, 13, addr_reader, sz_reader, obj_reader5sized_param_)
AddrSizedParamArrayReader(3, 16, addr_reader, sz_reader, obj_reader5sized_param_)

AddrSizedParamArrayReader(3, 16, addr_reader, sz_reader)
AddrSizedParamArrayReader(3, 16, addr_reader, None)


    #ArrayTranformReader(param_array_or_reader, obj_reader_or5param, /)
ArrayTranformReader(param_array, obj_reader, /)
ArrayTranformReader(param_array_reader, obj_reader, /)
ArrayTranformReader(param_array, obj_reader5param_, /)
ArrayTranformReader(param_array_reader, obj_reader5param_, /)








#>>> obj_reader5param_ = BytesReader
#>>> param_reader = sz_reader = uint8LE_reader
>>> a_varaddr_reader = a_varsz_reader = BytesReader(sz_reader, uintLE_decoder)
>>> addr_reader = uint16BE_reader
>>> addr_param_reader = TupleReader(addr_reader, sz_reader)
>>> varaddr_param_reader = TupleReader(a_varaddr_reader, sz_reader)
>>> addr_varparam_reader = TupleReader(addr_reader, a_varsz_reader)

# [(0x000a,1)@0, (0x000b,2)@3, (0x000d,3)@6]@[0:9]
# b':'@9 #sep#skip
# b'9'@10 # <- array[0].addr=0x000a
# b'xy'@11 # <- array[1].addr=0x000b
# b'ABC'@13 # <- array[2].addr=0x000d
>>> bs = b'\0\x0a\1\0\x0b\2\0\x0d\3:9xyABC---'
>>> ibfile = BytesIO(bs)




>>> reader = AddrDereferenceReader(addr_param_reader, BytesReader)
>>> reader
AddrDereferenceReader(TupleReader(BytesReader(2, IntDecoder(False, 'big')), BytesReader(1, IntDecoder(False, 'little'))), <class 'nn_ns.codec.DecodeUtils.BytesReader'>)
>>> reader.get_may_static_num_bytes4skip()
3
>>> AddrDereferenceReader(varaddr_param_reader, BytesReader).get_may_static_num_bytes4skip() is None
True
>>> AddrDereferenceReader(addr_varparam_reader, BytesReader).get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
b'9'
>>> ibfile.tell()
3
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
3

    #addr_param_reader --> addr_or_addr_param_pair_or_reader
    #obj_reader5param_ --> obj_reader_or5Mparam
AddrDereferenceReader(addr_param_pair, obj_reader)
AddrDereferenceReader(addr, obj_reader)
>>> reader = AddrDereferenceReader((10,1), BytesReader)
>>> reader
AddrDereferenceReader((10, 1), <class 'nn_ns.codec.DecodeUtils.BytesReader'>)
>>> reader.get_may_static_num_bytes4skip()
0
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
b'9'
>>> ibfile.tell()
0
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
0


>>> reader = AddrDereferenceReader(10, BytesReader(1))
>>> reader
AddrDereferenceReader(10, BytesReader(1))
>>> reader.get_may_static_num_bytes4skip()
0
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
b'9'
>>> ibfile.tell()
0
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
0







#for .get_may_static_num_bytes4skip()
>>> AddrSizedParamReader(11, sz_reader, None).get_may_static_num_bytes4skip()
1
>>> AddrSizedParamReader(11, a_varsz_reader, None).get_may_static_num_bytes4skip() is None
True
>>> AddrSizedParamReader(addr_reader, sz_reader, None).get_may_static_num_bytes4skip()
3
>>> AddrSizedParamReader(a_varaddr_reader, sz_reader, None).get_may_static_num_bytes4skip() is None
True

#seek(5)end=13
AddrSizedParamReader(11, sz_reader, None) #buggy
>>> reader = AddrSizedParamReader(11, sz_reader, None)
>>> reader
AddrSizedParamReader(11, BytesReader(1, IntDecoder(False, 'little')), None)
>>> reader.get_may_static_num_bytes4skip()
1
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(5)
5
>>> apply_reader(reader, ibfile) #(begin_addr4target, sized_param/(size4target, param)) #--> b'xy' #buggy!!! ==>> require end_addr_reader4target ==>> may_end_addr4target-->may_end_addr4target_or_reader
(11, (0, 2))
>>> ibfile.tell()
6
>>> ibfile.seek(5)
5
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6


#seek(5)end=13
AddrSizedParamReader(11, sz_reader, addr_reader) #fix above bug
>>> reader = AddrSizedParamReader(11, sz_reader, addr_reader)
>>> reader
AddrSizedParamReader(11, BytesReader(1, IntDecoder(False, 'little')), BytesReader(2, IntDecoder(False, 'big')))
>>> reader.get_may_static_num_bytes4skip()
1
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(5)
5
>>> apply_reader(reader, ibfile) #(begin_addr4target, sized_param/(size4target, param)) #--> b'xy' #fix above bug
(11, (2, 2))
>>> ibfile.tell()
6
>>> ibfile.seek(5)
5
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6


#seek(5)end=13
>>> reader = AddrSizedParamReader(11, sz_reader, 13)
>>> reader
AddrSizedParamReader(11, BytesReader(1, IntDecoder(False, 'little')), 13)
>>> reader.get_may_static_num_bytes4skip()
1
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(5)
5
>>> apply_reader(reader, ibfile) #(begin_addr4target, sized_param/(size4target, param)) #--> b'xy'
(11, (2, 2))
>>> ibfile.tell()
6
>>> ibfile.seek(5)
5
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6


#seek(3)end=13
>>> reader = AddrSizedParamReader(addr_reader, sz_reader, None)
>>> reader
AddrSizedParamReader(BytesReader(2, IntDecoder(False, 'big')), BytesReader(1, IntDecoder(False, 'little')), None)
>>> reader.get_may_static_num_bytes4skip()
3
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(3)
3
>>> apply_reader(reader, ibfile) #(begin_addr4target, sized_param/(size4target, param)) #--> b'xy'
(11, (2, 2))
>>> ibfile.tell()
6
>>> ibfile.seek(3)
3
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6


#seek(3)end=13
>>> reader = AddrSizedParamReader(addr_reader, sz_reader, 13)
>>> reader
AddrSizedParamReader(BytesReader(2, IntDecoder(False, 'big')), BytesReader(1, IntDecoder(False, 'little')), 13)
>>> reader.get_may_static_num_bytes4skip()
3
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(3)
3
>>> apply_reader(reader, ibfile) #(begin_addr4target, sized_param/(size4target, param)) #--> b'xy'
(11, (2, 2))
>>> ibfile.tell()
6
>>> ibfile.seek(3)
3
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6


AddrDereferenceReader+AddrSizedParamReader
>>> def obj_reader5param_(sized_param, /):
...     (size4target, param) = sized_param
...     return BytesReader(size4target)
>>> reader = AddrDereferenceReader(AddrSizedParamReader(addr_reader, sz_reader, None), obj_reader5param_)
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
b'9'
>>> ibfile.tell()
3
>>> apply_reader(reader, ibfile)
b'xy'
>>> ibfile.tell()
6
>>> apply_reader(reader, ibfile) # b'ABC' but fail since this is last array elem, no follow addr
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.StreamEOFError: too few bytes
>>> ibfile.tell() == get_size_of_ibfile(ibfile)
True
>>> ibfile.seek(6)
6
>>> reader = AddrDereferenceReader(AddrSizedParamReader(addr_reader, sz_reader, 16), obj_reader5param_) #manually fix end_addr4target of last array elem
>>> apply_reader(reader, ibfile)
b'ABC'
>>> ibfile.tell()
9



>>> obj_reader5param_ = dot[BytesReader, fst_]
>>> reader = AddrDereferenceReader(AddrSizedParamReader(addr_reader, sz_reader, None), obj_reader5param_)
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
b'9'
>>> ibfile.tell()
3
>>> apply_reader(reader, ibfile)
b'xy'
>>> ibfile.tell()
6
>>> apply_reader(reader, ibfile) # b'ABC' but fail since this is last array elem, no follow addr
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.StreamEOFError: too few bytes
>>> ibfile.tell() == get_size_of_ibfile(ibfile)
True
>>> ibfile.seek(6)
6
>>> reader = AddrDereferenceReader(AddrSizedParamReader(addr_reader, sz_reader, 16), obj_reader5param_) #manually fix end_addr4target of last array elem
>>> apply_reader(reader, ibfile)
b'ABC'
>>> ibfile.tell()
9



AddrSizedParamArrayReader
    def __init__(sf, len_array, may_end_addr4last_target, addr_reader, may_param_reader, may_obj_reader5sized_param_, /):
#for .get_may_static_num_bytes4skip()
>>> obj_reader5sized_param_ = dot[BytesReader, fst_]
>>> AddrSizedParamArrayReader(0, None, a_varaddr_reader, a_varsz_reader, lazy_raise).get_may_static_num_bytes4skip()
0
>>> AddrSizedParamArrayReader(1, None, a_varaddr_reader, a_varsz_reader, lazy_raise).get_may_static_num_bytes4skip()
0
>>> AddrSizedParamArrayReader(2, None, addr_reader, sz_reader, obj_reader5sized_param_).get_may_static_num_bytes4skip()
3
>>> AddrSizedParamArrayReader(2, None, addr_reader, a_varsz_reader, obj_reader5sized_param_).get_may_static_num_bytes4skip() is None
True
>>> AddrSizedParamArrayReader(2, None, a_varaddr_reader, sz_reader, obj_reader5sized_param_).get_may_static_num_bytes4skip() is None
True
>>> AddrSizedParamArrayReader(3, None, addr_reader, sz_reader, obj_reader5sized_param_).get_may_static_num_bytes4skip()
6
>>> AddrSizedParamArrayReader(4, None, addr_reader, sz_reader, obj_reader5sized_param_).get_may_static_num_bytes4skip() #L-1; exclude last elem
9


#seek(0)end=10,11,13,16
>>> AddrSizedParamArrayReader(0, 10, a_varaddr_reader, a_varsz_reader, lazy_raise).get_may_static_num_bytes4skip()
0
>>> AddrSizedParamArrayReader(1, 11, addr_reader, sz_reader, obj_reader5sized_param_).get_may_static_num_bytes4skip()
3
>>> AddrSizedParamArrayReader(1, 11, addr_reader, a_varsz_reader, obj_reader5sized_param_).get_may_static_num_bytes4skip() is None
True
>>> AddrSizedParamArrayReader(1, 11, a_varaddr_reader, sz_reader, obj_reader5sized_param_).get_may_static_num_bytes4skip() is None
True
>>> AddrSizedParamArrayReader(2, 13, addr_reader, sz_reader, obj_reader5sized_param_).get_may_static_num_bytes4skip()
6
>>> AddrSizedParamArrayReader(3, 16, addr_reader, sz_reader, obj_reader5sized_param_).get_may_static_num_bytes4skip()
9



>>> reader = AddrSizedParamArrayReader(0, None, addr_reader, sz_reader, obj_reader5sized_param_)
>>> reader.is_read_result_ignoreable()
False
>>> reader = AddrSizedParamArrayReader(3, 16, addr_reader, sz_reader, obj_reader5sized_param_) ##manually fix end_addr4last_target to read whole array
>>> reader #doctest: +ELLIPSIS
AddrSizedParamArrayReader(3, 16, BytesReader(2, IntDecoder(False, 'big')), BytesReader(1, IntDecoder(False, 'little')), <seed.func_tools.dot2.Dot object at 0x...>)
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
[b'9', b'xy', b'ABC']
>>> ibfile.tell()
9
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
9
>>> reader = AddrSizedParamArrayReader(3, None, addr_reader, sz_reader, obj_reader5sized_param_) ##neednot end_addr4last_target to read partial array
>>> reader #doctest: +ELLIPSIS
AddrSizedParamArrayReader(3, None, BytesReader(2, IntDecoder(False, 'big')), BytesReader(1, IntDecoder(False, 'little')), <seed.func_tools.dot2.Dot object at 0x...>)
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
[b'9', b'xy']
>>> ibfile.tell()
6
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6


AddrSizedParamArrayReader(3, 16, addr_reader, sz_reader)
>>> reader = AddrSizedParamArrayReader(3, 16, addr_reader, sz_reader) ##manually fix end_addr4last_target to read whole array #with [obj_reader5sized_param_ := None]
>>> reader
AddrSizedParamArrayReader(3, 16, BytesReader(2, IntDecoder(False, 'big')), BytesReader(1, IntDecoder(False, 'little')))
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
[(10, (1, 1)), (11, (2, 2)), (13, (3, 3))]
>>> ibfile.tell()
9
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
9


'''  r'''
AddrSizedParamArrayReader(3, 16, addr_reader, None)
>>> bs = b'\0\1\2\3\4\5\6\7:'
>>> ibfile = BytesIO(bs)
>>> reader = AddrSizedParamArrayReader(4, 9999, addr_reader, None)
>>> reader
AddrSizedParamArrayReader(4, 9999, BytesReader(2, IntDecoder(False, 'big')), None)
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
[(1, 514), (515, 514), (1029, 514), (1543, 8456)]
>>> _ == [(0x00_01, 0x0202), (0x02_03, 0x0202), (0x04_05, 0x0202), (0x06_07, 9999-0x06_07)]
True
>>> ibfile.tell()
8
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
8
>>> 0x0203 - 0x0001 == 0x0202 == 514
True
>>> 9999 - 0x0607
8456





'''  r'''


    #ArrayTranformReader(param_array_or_reader, obj_reader_or5param, /)
>>> param_array = [(10,1), (11,2), (13,3)]
>>> param_array_reader = ArrayReader(3, TupleReader(addr_reader, sz_reader))
>>> def obj_reader5param_(addr_sz_pair,/):
...     dot[BytesReader, snd_]
...     addr, sz = addr_sz_pair
...     return AddrDereferenceReader(addr, BytesReader(sz))
>>> obj_reader = addr_reader
>>> ibfile.getvalue()
b'\x00\x01\x02\x03\x04\x05\x06\x07:'
>>> bs = b'\0\x0a\1\0\x0b\2\0\x0d\3:9xyABC---'
>>> ibfile = BytesIO(bs)
>>> bs.hex(' ', -2)
'000a 0100 0b02 000d 033a 3978 7941 4243 2d2d 2d'
>>> bs[9:].hex(' ', -2)
'3a39 7879 4142 432d 2d2d'


>>> reader = ArrayTranformReader(param_array, obj_reader)
>>> reader
ArrayTranformReader([(10, 1), (11, 2), (13, 3)], BytesReader(2, IntDecoder(False, 'big')))
>>> reader.get_may_static_num_bytes4skip()
6
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
[10, 256, 2818]
>>> _ == [0x00_0a, 0x01_00, 0x0b02]
True
>>> ibfile.tell() #3*2 == 6
6
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
6


>>> reader = ArrayTranformReader(param_array_reader, obj_reader)
>>> reader
ArrayTranformReader(ArrayReader(3, TupleReader(BytesReader(2, IntDecoder(False, 'big')), BytesReader(1, IntDecoder(False, 'little')))), BytesReader(2, IntDecoder(False, 'big')))
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
[14905, 30841, 16706]
>>> _ == [0x3a39, 0x7879, 0x4142]
True
>>> ibfile.tell() #3*(2+1)  +  3*2 == 9+6
15
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
15


>>> reader = ArrayTranformReader(param_array, obj_reader5param_)
>>> reader #doctest: +ELLIPSIS
ArrayTranformReader([(10, 1), (11, 2), (13, 3)], <function obj_reader5param_ at 0x...>)
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
[b'9', b'xy', b'ABC']
>>> ibfile.tell()
0
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
0


>>> reader = ArrayTranformReader(param_array_reader, obj_reader5param_)
>>> reader #doctest: +ELLIPSIS
ArrayTranformReader(ArrayReader(3, TupleReader(BytesReader(2, IntDecoder(False, 'big')), BytesReader(1, IntDecoder(False, 'little')))), <function obj_reader5param_ at 0x...>)
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
[b'9', b'xy', b'ABC']
>>> ibfile.tell()
9
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
9




'''  r'''
    ipop_and_drop4list

    try_apply_decoder
    try_apply_reader

    UntilEndValueBytesReader

    UntilEndValueArrayReader
    UntilReadEndValueArrayReader

++to_drop_end_bytes
++to_drop_end_obj

UntilEndValueBytesReader
    def __init__(sf, end_bytes, /, *, to_drop_end_bytes=False):
UntilEndValueArrayReader
    def __init__(sf, elem_reader, end_value, may_postprocess=None, /, *, may_op:'==,is,in,is_not,not_in,_(),._()'='==', to_drop_end_obj=False):
UntilReadEndValueArrayReader
    def __init__(sf, elem_reader, end_value_reader, may_postprocess=None, /, *, to_drop_end_obj=False):

UntilEndValueBytesReader(b'')
UntilEndValueBytesReader(b'67')
UntilEndValueBytesReader(b'', to_drop_end_bytes=True)
UntilEndValueBytesReader(b'67', to_drop_end_bytes=True)
UntilEndValueBytesReader(b'z')

elem_reader = BytesReader(2)
UntilEndValueArrayReader(elem_reader, b'67')
UntilEndValueArrayReader(elem_reader, b'678')
UntilEndValueArrayReader(elem_reader, b'67', ipop_and_drop4list)
UntilEndValueArrayReader(elem_reader, b'67', to_drop_end_obj=True)
UntilEndValueArrayReader(elem_reader, b'678', may_op='in')

end_value_reader = mk_ConstantBytesMatcher(b'678')
UntilReadEndValueArrayReader(elem_reader, end_value_reader)
UntilReadEndValueArrayReader(elem_reader, end_value_reader, ipop_and_drop4list)
UntilReadEndValueArrayReader(elem_reader, end_value_reader, to_drop_end_obj=True)
end_value_reader = mk_ConstantBytesMatcher(b'z')
UntilReadEndValueArrayReader(elem_reader, end_value_reader)



>>> ls = [111,222]
>>> ls is ipop_and_drop4list(ls)
True
>>> ls
[111]

>>> try_apply_decoder(ascii_decoder, b'\0\x7f')
('\x00\x7f',)
>>> try_apply_decoder(ascii_decoder, b'\x80')
()

>>> bs = b'0123456789'
>>> ibfile = BytesIO(bs)
>>> reader = BytesReader(10)
>>> try_apply_reader(reader, ibfile)
(b'0123456789',)
>>> ibfile.tell()
10
>>> ibfile.seek(0)
0
>>> try_apply_reader(reader, ibfile, skip_only=True)
(None,)
>>> ibfile.tell()
10

>>> reader = BytesReader(11)
>>> ibfile.seek(0)
0
>>> try_apply_reader(reader, ibfile)
()
>>> ibfile.tell() #seekback
0
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.StreamEOFError: too few bytes
>>> ibfile.tell() #not seekback
10

>>> ibfile.seek(0)
0
>>> try_apply_reader(reader, ibfile, skip_only=True)
()
>>> ibfile.tell()
0
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.SeekError__pass_EOF
>>> ibfile.tell() #checked_seek() seekback
0




>>> reader = UntilEndValueBytesReader(b'')
>>> reader
UntilEndValueBytesReader(b'')
>>> reader.get_may_static_num_bytes4skip()
0
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
b''
>>> ibfile.tell()
0
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
0


>>> reader = UntilEndValueBytesReader(b'67')
>>> reader
UntilEndValueBytesReader(b'67')
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
b'01234567'
>>> ibfile.tell()
8
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
8


>>> reader = UntilEndValueBytesReader(b'', to_drop_end_bytes=True)
Traceback (most recent call last):
    ...
TypeError

>>> reader = UntilEndValueBytesReader(b'67', to_drop_end_bytes=True)
>>> reader
UntilEndValueBytesReader(b'67', to_drop_end_bytes = True)
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
b'012345'
>>> ibfile.tell()
8
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
8


>>> reader = UntilEndValueBytesReader(b'z')
>>> reader
UntilEndValueBytesReader(b'z')
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.StreamEOFError: too few bytes
>>> ibfile.tell()
10
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.StreamEOFError: too few bytes
>>> ibfile.tell()
10



>>> elem_reader = BytesReader(2)

>>> reader = UntilEndValueArrayReader(elem_reader, b'67')
>>> reader
UntilEndValueArrayReader(BytesReader(2), b'67')
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
[b'01', b'23', b'45', b'67']
>>> ibfile.tell()
8
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
8


>>> reader = UntilEndValueArrayReader(elem_reader, b'678')
>>> reader
UntilEndValueArrayReader(BytesReader(2), b'678')
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.StreamEOFError: too few bytes
>>> ibfile.tell()
10
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.StreamEOFError: too few bytes
>>> ibfile.tell()
10


>>> reader = UntilEndValueArrayReader(elem_reader, b'67', ipop_and_drop4list)
>>> reader #doctest: +ELLIPSIS
UntilEndValueArrayReader(BytesReader(2), b'67', <function ipop_and_drop4list at 0x...>)
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
[b'01', b'23', b'45']
>>> ibfile.tell()
8
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
8


>>> reader = UntilEndValueArrayReader(elem_reader, b'67', to_drop_end_obj=True)
>>> reader
UntilEndValueArrayReader(BytesReader(2), b'67', to_drop_end_obj = True)
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
[b'01', b'23', b'45']
>>> ibfile.tell()
8
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
8



>>> reader = UntilEndValueArrayReader(elem_reader, b'678', may_op='in')
>>> reader
UntilEndValueArrayReader(BytesReader(2), b'678', may_op = 'in')
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
[b'01', b'23', b'45', b'67']
>>> ibfile.tell()
8
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
8






>>> end_value_reader = mk_ConstantBytesMatcher(b'678')

>>> reader = UntilReadEndValueArrayReader(elem_reader, end_value_reader)
>>> reader
UntilReadEndValueArrayReader(BytesReader(2), ConstantInOutReader(b'678', None))
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
[b'01', b'23', b'45', None]
>>> ibfile.tell()
9
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
9


>>> reader = UntilReadEndValueArrayReader(elem_reader, end_value_reader, ipop_and_drop4list)
>>> reader #doctest: +ELLIPSIS
UntilReadEndValueArrayReader(BytesReader(2), ConstantInOutReader(b'678', None), <function ipop_and_drop4list at 0x...>)
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
[b'01', b'23', b'45']
>>> ibfile.tell()
9
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
9


>>> reader = UntilReadEndValueArrayReader(elem_reader, end_value_reader, to_drop_end_obj=True)
>>> reader
UntilReadEndValueArrayReader(BytesReader(2), ConstantInOutReader(b'678', None), to_drop_end_obj = True)
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
[b'01', b'23', b'45']
>>> ibfile.tell()
9
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
9



>>> end_value_reader = mk_ConstantBytesMatcher(b'z')

>>> reader = UntilReadEndValueArrayReader(elem_reader, end_value_reader)
>>> reader
UntilReadEndValueArrayReader(BytesReader(2), ConstantInOutReader(b'z', None))
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.StreamEOFError: too few bytes
>>> ibfile.tell()
10
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.SeekError__pass_EOF
>>> ibfile.tell()
10






    TellAddrReader
        tell_addr_reader
        mk_AddrAssertionReader
    EOFAddrReader
        eof_addr_reader
        file_size_reader
    OffsetReader
    AddrReader
    SeekAddrReader
        ++to_read_bytes
        ++allowed_to_read_bytes_on_seekback

OffsetReader
    def __init__(sf, /, *offset_or_reader__seq, to_neg=False):
AddrReader
    def __init__(sf, base_addr_or_reader_or_name:'eof,tell', offset_or_reader, /):
SeekAddrReader
    def __init__(sf, base_addr_or_reader_or_name:'eof,tell', offset_or_reader=0, /):
    def __init__(sf, base_addr_or_reader_or_name:'eof,tell', offset_or_reader=0, /, *, to_read_bytes=False, allowed_to_read_bytes_on_seekback=False):

OffsetReader()
OffsetReader(-0x30, uint8LE_reader)
OffsetReader(-0x30, a_varsz_reader)
OffsetReader(-0x30, uint8LE_reader, to_neg=True)

AddrReader(4, 1)
AddrReader('tell', 1)
AddrReader('eof', -1)
AddrReader(eof_addr_reader, a_varsz_reader)

SeekAddrReader('eof')
SeekAddrReader(tell_addr_reader, 9)
SeekAddrReader(9, a_varsz_reader)

SeekAddrReader('eof', allowed_to_read_bytes_on_seekback=True)
SeekAddrReader('eof', to_read_bytes=True)
SeekAddrReader(tell_addr_reader, -3, to_read_bytes=True)
SeekAddrReader(tell_addr_reader, -3, to_read_bytes=True, allowed_to_read_bytes_on_seekback=True)

>>> tell_addr_reader
TellAddrReader()
>>> tell_addr_reader is TellAddrReader()
True

>>> eof_addr_reader
EOFAddrReader()
>>> eof_addr_reader is EOFAddrReader()
True
>>> FileSizeReader is EOFAddrReader
True
>>> file_size_reader is eof_addr_reader
True
>>> SumReader is OffsetReader
True
>>> CasedUnionReader is DependentPairReader
True
>>> UserReader is FallbackReader
True

>>> reader = tell_addr_reader
>>> reader
TellAddrReader()
>>> reader.get_may_static_num_bytes4skip()
0
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
0
>>> ibfile.tell()
0
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
0
>>> ibfile.seek(5)
5
>>> apply_reader(reader, ibfile)
5
>>> ibfile.tell()
5
>>> ibfile.seek(5)
5
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
5


>>> reader = eof_addr_reader
>>> reader
EOFAddrReader()
>>> reader.get_may_static_num_bytes4skip()
0
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile)
10
>>> ibfile.tell()
0
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
0




>>> reader = OffsetReader()
>>> reader
OffsetReader()
>>> reader.get_may_static_num_bytes4skip()
0
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(4)
4
>>> apply_reader(reader, ibfile)
0
>>> ibfile.tell()
4
>>> ibfile.seek(7)
7
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
7


>>> reader = OffsetReader(-0x30, uint8LE_reader)
>>> reader
OffsetReader(-48, BytesReader(1, IntDecoder(False, 'little')))
>>> reader.get_may_static_num_bytes4skip()
1
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(4)
4
>>> apply_reader(reader, ibfile)
4
>>> ibfile.tell()
5
>>> apply_reader(reader, ibfile)
5
>>> ibfile.tell()
6
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
7

>>> reader = OffsetReader(-0x30, a_varsz_reader)
>>> reader
OffsetReader(-48, BytesReader(BytesReader(1, IntDecoder(False, 'little')), IntDecoder(False, 'little')))
>>> reader.get_may_static_num_bytes4skip() is None
True


>>> reader = OffsetReader(-0x30, uint8LE_reader, to_neg=True)
>>> reader
OffsetReader(-48, BytesReader(1, IntDecoder(False, 'little')), to_neg = True)
>>> ibfile.seek(4)
4
>>> apply_reader(reader, ibfile)
-4
>>> ibfile.tell()
5



>>> reader = AddrReader(4, 1)
>>> reader
AddrReader(4, 1)
>>> reader.get_may_static_num_bytes4skip()
0
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(9)
9
>>> apply_reader(reader, ibfile)
5
>>> ibfile.tell()
9
>>> ibfile.seek(7)
7
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
7



>>> reader = AddrReader('tell', 1)
>>> reader
AddrReader('tell', 1)
>>> reader.get_may_static_num_bytes4skip()
0
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(6)
6
>>> apply_reader(reader, ibfile)
7
>>> ibfile.tell()
6
>>> ibfile.seek(7)
7
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
7


>>> reader = AddrReader('eof', -1)
>>> reader
AddrReader('eof', -1)
>>> reader.get_may_static_num_bytes4skip()
0
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(6)
6
>>> apply_reader(reader, ibfile)
9
>>> ibfile.tell()
6


>>> reader = AddrReader(eof_addr_reader, a_varsz_reader)
>>> reader
AddrReader(EOFAddrReader(), BytesReader(BytesReader(1, IntDecoder(False, 'little')), IntDecoder(False, 'little')))
>>> reader.get_may_static_num_bytes4skip() is None
True




>>> reader = SeekAddrReader('eof')
>>> reader
SeekAddrReader('eof')
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(6)
6
>>> apply_reader(reader, ibfile)
10
>>> ibfile.tell()
10
>>> ibfile.seek(7)
7
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
10


>>> reader = SeekAddrReader(tell_addr_reader, 9)
>>> reader
SeekAddrReader(TellAddrReader(), 9)
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(1)
1
>>> apply_reader(reader, ibfile)
10
>>> ibfile.tell()
10
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
9

'''  r'''
>>> ibfile = BytesIO(b'\0\1\2\7\x0056789abcdef')
>>> reader = SeekAddrReader(9, a_varsz_reader)
>>> reader
SeekAddrReader(9, BytesReader(BytesReader(1, IntDecoder(False, 'little')), IntDecoder(False, 'little')))
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(2)
2
>>> apply_reader(reader, ibfile)
16
>>> ibfile.tell()
16
>>> ibfile.seek(1)
1
>>> apply_reader(reader, ibfile)
11
>>> ibfile.tell()
11
>>> ibfile.seek(0)
0
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
9



>>> SeekAddrReader('eof', allowed_to_read_bytes_on_seekback=True)
Traceback (most recent call last):
    ...
TypeError
>>> reader = SeekAddrReader('eof', to_read_bytes=True)
>>> reader
SeekAddrReader('eof', to_read_bytes = True)
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(10)
10
>>> apply_reader(reader, ibfile)
b'abcdef'
>>> ibfile.tell()
16
>>> ibfile.seek(10)
10
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
16


>>> reader = SeekAddrReader(tell_addr_reader, -3, to_read_bytes=True)
>>> reader
SeekAddrReader(TellAddrReader(), -3, to_read_bytes = True)
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(10)
10
>>> apply_reader(reader, ibfile)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.ReadError__SeekAddrReader
>>> ibfile.tell()
10
>>> ibfile.seek(10)
10
>>> apply_reader(reader, ibfile, skip_only=True)
Traceback (most recent call last):
    ...
nn_ns.codec.DecodeUtils.ReadError__SeekAddrReader
>>> ibfile.tell()
10


>>> reader = SeekAddrReader(tell_addr_reader, -3, to_read_bytes=True, allowed_to_read_bytes_on_seekback=True)
>>> reader
SeekAddrReader(TellAddrReader(), -3, allowed_to_read_bytes_on_seekback = True, to_read_bytes = True)
>>> reader.get_may_static_num_bytes4skip() is None
True
>>> reader.is_read_result_ignoreable()
False
>>> ibfile.seek(10)
10
>>> apply_reader(reader, ibfile)
b'789'
>>> ibfile.tell()
7
>>> ibfile.seek(10)
10
>>> apply_reader(reader, ibfile, skip_only=True)
>>> ibfile.tell()
7









from seed.io.with4seekback import with4seekback__on_exit, with4seekback__on_err, with4seekback__on_no_err
test include:
    IReader.get_may_static_num_bytes4skip()
    IReader.is_read_result_ignoreable()

'''#'''

__all__ = '''
    CheckError

    read_bytes
    read_uint32le
    check_bytes

    DecodeUtils
    DecodeUtils_32le
'''  r'''



ReadError
    ReadError__NamedDependentTupleReader
    ReadError__SeekAddrReader
StreamError
    StreamEOFError
    SeekError
        SeekError__pass_BOF
        SeekError__pass_EOF

read_bytes
checked_seek
    skip_bytes
get_size_of_ibfile
    get_size_of_ibfile_ex



apply_decoder
    try_apply_decoder
IDecoder
    EchoDecoder
        echo_decoder

    PyDecoder
            zlib_decoder
        StrDecoder
            ascii_decoder
            u8_decoder
            gb_decoder

    ComposeDecoder
            u8_zlib_decoder

    IntDecoder
        uintLE_decoder
        uintBE_decoder
        sintLE_decoder
        sintBE_decoder

apply_reader
    try_apply_reader
IReader
    check__uint_or_uint_reader
        uint5or_uint_reader__
            size5or_size_reader__
            addr5or_addr_reader__
        uint_or2uint_reader_
            size_or2size_reader_
            addr_or2addr_reader_

    check__int_or_int_reader
        int5or_int_reader__
            offset5or_offset_reader__
        int_or2int_reader_
            offset_or2offset_reader_

    BytesReader
        mk_UIntLEReader
        mk_UIntBEReader
        mk_SIntLEReader
        mk_SIntBEReader
            uint8BE_reader
            uint16BE_reader
            uint32BE_reader
            uint64BE_reader
            uint128BE_reader
            uint256BE_reader
            uint512BE_reader
            uint1024BE_reader
            uint8LE_reader
            uint16LE_reader
            uint32LE_reader
            uint64LE_reader
            uint128LE_reader
            uint256LE_reader
            uint512LE_reader
            uint1024LE_reader
            sint8BE_reader
            sint16BE_reader
            sint32BE_reader
            sint64BE_reader
            sint128BE_reader
            sint256BE_reader
            sint512BE_reader
            sint1024BE_reader
            sint8LE_reader
            sint16LE_reader
            sint32LE_reader
            sint64LE_reader
            sint128LE_reader
            sint256LE_reader
            sint512LE_reader
            sint1024LE_reader

    ConstantInOutReader
        mk_ConstantTargetReader
        mk_ConstantBytesMatcher
    FallbackReader      UserReader
        IgnoreableReader
            SkipReader
    FurtherTransformReader  PostprocessReader
    AssertionReader

    ArrayReader
    TupleReader
    DependentPairReader CasedUnionReader
    NamedTupleReader
    NamedDependentTupleReader
        is_xname_ignoreable_
        check_xname
    UntilEndValueBytesReader
    UntilEndValueArrayReader
    UntilReadEndValueArrayReader
        ipop_and_drop4list

    AddrDereferenceReader
        check_addrXparam
        check_addrXparam_or_reader
        addrXparam_or2reader_
        addrXparam_as_args_
    AddrSizedParamReader
    AddrSizedParamArrayReader
    ArrayTranformReader





    TellAddrReader
        tell_addr_reader
        mk_AddrAssertionReader

    EOFAddrReader       FileSizeReader
        eof_addr_reader file_size_reader

    OffsetReader        SumReader
    AddrReader
    SeekAddrReader
        addr_or_name_or2reader_


'''.split()#'''
__all__


#################################
#旧版:
#from .. import CheckError
class CheckError(Exception):pass



def read_bytes(file, size, /):
    bs = file.read(size)
    if len(bs) != size:
        raise EOFError('too few bytes')
    return bs

def read_uint32le(file, /):
    bs = read_bytes(file, 4)
    u = int.from_bytes(bs, 'little')
    assert u >= 0
    return u

def check_bytes(file, bs, pos=None, /):
    if pos is not None:
        file.seek(pos)

    size = len(bs)
    try:
        new_bs = read_bytes(file, size)
    except EOFError:
        raise CheckError('not the given bytes in file : EOF')
    if not new_bs == bs:
        raise CheckError('not the given bytes in file : {!r} != {!r}'
                             .format(new_bs, bs))
##
##def read_sized_bytes(file):
##    size = read_uint32le(file)
##    bs = read_bytes(file, size)
##    return bs
##
##def read_sized_array(file, elem_reader):
##    size = read_uint32le(file)
##    ls = [elem_reader(file) for _ in range(size)]
##    return ls
##

class DecodeUtils:
    r'''utilities to use in decoding process or parsing binary file

file should be opened in "rb" mode

default parameters:
    offset_size = position_size = sint_size = uint_size = 4
    byte_order = 'little'

    subclasses can override these parameters.

DecodeUtils serves as baseclass while DecodeUtils_32le for concrete usage
though DecodeUtils_32le is DecodeUtils
'''
    offset_size = position_size = sint_size = uint_size = 4
    byte_order = 'little'

    def __init__(self, file, /):
        'file should be opened in "rb" mode'
        self.file = file
    def read_uint(self, /):
        u = self.read_xint(self.uint_size, signed=False)
        assert u >= 0
        return u
    def read_sint(self, /):
        i = self.read_xint(self.sint_size, signed=True)
        return i
    def read_xint(self, size, /, *, signed=False):
        bs = read_bytes(self.file, size)
        i = int.from_bytes(bs, self.byte_order, signed=signed)
        return i

    def read_bytes(self, size, /):
        return read_bytes(self.file, size)

    def check_bytes(self, bs, pos=None, /):
        return check_bytes(self.file, bs, pos)

    ########## sized xxx ########
    # sized_xxx = struct{uint size; elem_t array[size];};

    def read_sized_bytes(self, /):
        size = self.read_uint()
        bs = self.read_bytes(size)
        return bs

    def read_sized_array(self, elem_factory, /):
        size = self.read_uint()
        ls = [elem_factory() for _ in range(size)]
        return ls

DecodeUtils_32le = DecodeUtils


#################################
#################################
#################################
#################################
#################################
#新版:
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
from seed.tiny import check_type_is, fmap4may, check_callable, check_pseudo_identifier, mk_tuple, check_type_le, ifNone, curry1
from seed.tiny_.check import check_uint, check_pair
from seed.tiny import echo, fst as fst_, snd as snd_
from seed.types.Tester import is_good, mk_tester_, view_registered_ops4mk_tester_
from seed.tiny_.try_ import try_


from os import SEEK_CUR, SEEK_END
import codecs
from itertools import filterfalse
import warnings
#from operator import __eq__,__contains__#no:__call__
    #from seed.for_libs.for_operator.__call__ import caller, __call__, call
    #from seed.tiny import boolexpr_wrapper

__all__
from seed.io.with4seekback import with4seekback__on_exit, with4seekback__on_err, with4seekback__on_no_err
from seed.types.NamedTuple__split_table import NamedTuple, Descriptor4NamedTuple, gmk_Descriptor4NamedTuple

#class DeprecationError(Exception):pass
class ReadError(Exception):pass
class ReadError__NamedDependentTupleReader(ReadError):pass
class ReadError__SeekAddrReader(ReadError):pass
class StreamError(Exception):pass
class StreamEOFError(StreamError, EOFError):pass
class SeekError(StreamError):pass
class SeekError__pass_BOF(SeekError, EOFError):pass
class SeekError__pass_EOF(SeekError):pass

def __():
    def read_bytes_(sz, ibfile, /):
        return read_bytes(ibfile, sz)
del read_bytes
def read_bytes(file, size, /):
    bs = file.read(size)
    if len(bs) != size:
        raise StreamEOFError('too few bytes')
    return bs
_read_bytes = read_bytes

#def check_bytes(file, bs, pos=None, /):
#-->def check_bytes(ibfile, bs, /):
#def read_bytes(file, size, /):
#-->def read_bytes(ibfile, sz, /):
def skip_bytes(ibfile, sz, /):
    #ibfile.seek(sz, SEEK_CUR)
    checked_seek(ibfile, ibfile.tell()+sz)

def checked_seek(ibfile, position, /):
    if position < 0:raise SeekError__pass_BOF
    old = ibfile.tell()
    with with4seekback__on_err(ibfile):
        ibfile.seek(position)
        if not position == ibfile.tell() or position > get_size_of_ibfile(ibfile):
            raise SeekError__pass_EOF
    return

def get_size_of_ibfile_ex(ibfile_or_sz, /):
    if type(ibfile_or_sz) is int:
        sz = ibfile_or_sz
        check_uint(sz)
    else:
        ibfile = ibfile_or_sz
        sz = get_size_of_ibfile(ibfile)
    return sz
def get_size_of_ibfile(ibfile, /):
    with with4seekback__on_no_err(ibfile):
        ibfile.seek(0, SEEK_END)
        end_pos = ibfile.tell()
    sz = end_pos
    check_uint(sz)
    return sz

#apply_decoder
#apply_reader
def apply_decoder(sf, bs, /):
    'IDecoder -> bytes -> obj'
    return sf._apply_decoder(bs)
class IDecoder(ABC__no_slots):
    __slots__ = ()
    @abstractmethod
    def __repr__(sf, /):
        #return repr_helper(sf, *args, **kwargs)
        raise NotImplementedError
    @abstractmethod
    def _decode_(sf, bs, /):
        'bytes -> obj'
        raise NotImplementedError
    #def __call__(sf, bs, /):
    def _apply_decoder(sf, bs, /):
        'bytes -> obj #see:apply_decoder'
        check_type_is(bytes, bs)
        obj = sf._decode_(bs)
        return obj

class EchoDecoder(IDecoder):
    def __new__(cls, /):
        global echo_decoder
        if not cls is __class__: raise TypeError(cls)
        try:
            sf = echo_decoder
        except NameError:
            sf = object.__new__(__class__)
            echo_decoder = sf
        assert sf is echo_decoder
        return sf

    @override
    def __repr__(sf, /):
        return repr_helper(sf)
    @override
    def _decode_(sf, bs, /):
        'bytes -> bytes'
        return bs
        return echo(bs)
echo_decoder = EchoDecoder()
assert echo_decoder is EchoDecoder()

class PyDecoder(IDecoder):
    def __init__(sf, encoding, /):
        check_type_is(str, encoding)
        if not encoding:raise TypeError
        sf._e = encoding
    @override
    def __repr__(sf, /):
        return repr_helper(sf, sf._e)
    @override
    def _decode_(sf, bs, /):
        'bytes -> obj'
        encoding = sf._e
        x = codecs.decode(bs, encoding)
            # bytes -> str
            # bytes -> bytes
            # ...
        return x
class StrDecoder(PyDecoder):
    @override
    def _decode_(sf, bs, /):
        'bytes -> obj'
        encoding = sf._e
        s = bs.decode(encoding)
            # only: bytes -> str
        return s
class ComposeDecoder(IDecoder):
    def __init__(sf, /, *outer_toinner_decoders):
        for decoder in outer_toinner_decoders:
            check_type_le(IDecoder, decoder)
        sf._ls = outer_toinner_decoders
    @override
    def __repr__(sf, /):
        return repr_helper(sf, *sf._ls)
    @override
    def _decode_(sf, bs, /):
        'bytes -> obj'
        decoders = sf._ls
        x = bs
        for decoder in reversed(decoders):
            x = apply_decoder(decoder, x)
        return x


ascii_decoder = StrDecoder('ascii')
u8_decoder = StrDecoder('utf8')
gb_decoder = StrDecoder('gb18030')

zlib_decoder = PyDecoder('zlib')
    # bytes -> bytes
u8_zlib_decoder = ComposeDecoder(u8_decoder, zlib_decoder)
    # bytes -> str


r'''[[[
class UIntLEDecoder(IDecoder):
    'little_endian'
    __slots__ = ()
    @override
    def __repr__(sf, /):
        return repr_helper(sf)
    @override
    def _decode_(sf, bs, /):
        'bytes -> uint'
        u = int.from_bytes(bs, 'little')
        return u
class UIntBEDecoder(IDecoder):
    'big_endian'
    __slots__ = ()
    @override
    def __repr__(sf, /):
        return repr_helper(sf)
    @override
    def _decode_(sf, bs, /):
        'bytes -> uint'
        u = int.from_bytes(bs, 'big')
        return u
uintLE_decoder = UIntLEDecoder()
uintBE_decoder = UIntBEDecoder()
]]]'''#'''
class IntDecoder(IDecoder):
    __slots__ = ()
    @override
    def __repr__(sf, /):
        return repr_helper(sf, sf.signed, sf.byteorder)
    def __init__(sf, signed, byteorder, /):
        check_type_is(bool, signed)
        check_type_is(str, byteorder)
        sf._sgd = signed
        sf._bo = byteorder
    @override
    def _decode_(sf, bs, /):
        'bytes -> int'
        i = int.from_bytes(bs, sf.byteorder, signed=sf.signed)
        return i
    @property
    def signed(sf, /):
        return sf._sgd
    @property
    def byteorder(sf, /):
        return sf._bo

uintLE_decoder = IntDecoder(False, 'little')
uintBE_decoder = IntDecoder(False, 'big')
sintLE_decoder = IntDecoder(True, 'little')
sintBE_decoder = IntDecoder(True, 'big')



#apply_decoder
#apply_reader
def apply_reader(sf, ibfile, position=None, offset=None, /, *, skip_only=False):
    r'''
    :: IReader -> ibfile -> obj #read at curr_position, ibfile.position move forward
    :: IReader -> ibfile -> position -> obj #read at `position`, ibfile.position seek back
    :: IReader -> ibfile -> position -> offset -> obj #read at `position+offset`, ibfile.position seek back
    :: IReader -> ibfile -> (skip_only=True) -> None #skip-read at curr_position, ibfile.position move forward
    '''#'''
    return sf._apply_reader(ibfile, position, offset, skip_only=skip_only)


def _test_warn_in__is_read_result_ignoreable():
    uint16BE_reader.is_read_result_ignoreable()
    uint16BE_reader.is_read_result_ignoreable()
    uint16BE_reader.is_read_result_ignoreable()
    assert False is uint16BE_reader.is_read_result_ignoreable()
class IReader(ABC__no_slots):
    'reader for ibfile(input-binary-stream)'
    __slots__ = ()

    @abstractmethod
    def __repr__(sf, /):
        #return repr_helper(sf, *args, **kwargs)
        raise NotImplementedError
    #xxx @abstractmethod
    def _is_read_result_ignoreable_(sf, /):
        '[Deprecated]:[deprecated by xname]: -> bool #see:NamedTupleReader,IgnoreableReader'
        #is_read_result_ignoreable
        return False
    @abstractmethod
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        #get_may_static_num_bytes4skip
        return None

    @abstractmethod
    def _read_(sf, ibfile, /):
        'ibfile -> obj #ibfile.position move forward'
        raise NotImplementedError
    def _skip_(sf, ibfile, /):
        'ibfile -> None #ibfile.position move forward'
        obj = sf._read_(ibfile)
        return None
    def is_read_result_ignoreable(sf, /):
        '[Deprecated]:[deprecated by xname]: -> bool #see:NamedTupleReader,IgnoreableReader'
        #raise DeprecationError('[IReader::is_read_result_ignoreable()/_is_read_result_ignoreable_()  are deprecated by   NamedTupleReader/NamedDependentTupleReader::arg@`xname`]')
        #raise DeprecationWarning
        message = '[IReader::is_read_result_ignoreable()/_is_read_result_ignoreable_()  are deprecated by   NamedTupleReader/NamedDependentTupleReader::arg@`xname`]'
        warnings.warn(message, UserWarning)
            #default to print once
            #<==> warnings.warn(message)
        warnings.warn(message, DeprecationWarning)
            #default not to print
            #tested by:_test_warn_in__is_read_result_ignoreable()

        b = sf._is_read_result_ignoreable_()
        check_type_is(bool, b)
        return b
    def get_may_static_num_bytes4skip(sf, /):
        '-> may uint #see:_skip_()'
        may_sz = sf._get_may_static_num_bytes4skip_()
        if not may_sz is None:
            sz = may_sz
            check_uint(sz)
        return may_sz

    #def __call__(sf, ibfile, position=None, offset=None, /, *, skip_only=False):
    def _apply_reader(sf, ibfile, position=None, offset=None, /, *, skip_only=False):
        r'''see:apply_reader
        :: ibfile -> obj #read at curr_position, ibfile.position move forward
        :: ibfile -> position -> obj #read at `position`, ibfile.position seek back
        :: ibfile -> position -> offset -> obj #read at `position+offset`, ibfile.position seek back
        :: ibfile -> (skip_only=True) -> None #skip-read at curr_position, ibfile.position move forward
        '''#'''
        if not (offset is None or position is not None): raise TypeError
        #skip_only = bool(skip_only)
        check_type_is(bool, skip_only)

        may_position = position
        if not may_position is None:
            check_uint(position)
            #check_type_is(int, position)
            position4target = position
            saved_position = ibfile.tell()
        else:
            del position
            position4target = ibfile.tell()
        to_seek_back = not may_position is None
        if skip_only and to_seek_back: raise TypeError

        may_offset = offset
        if not may_offset is None:
            #check_int_ge(-position, offset)
            check_type_is(int, offset)
            position4target += position
        else:
            del offset
        position4target
        if 1:
            #xxx assert position4target >= 0
            checked_seek(ibfile, position4target)


        if skip_only:
            sf._skip_(ibfile)
            may_obj = None
        else:
            obj = sf._read_(ibfile)
            if to_seek_back:
                ibfile.seek(saved_position)
            may_obj = obj
        return may_obj
#end-class IReader(ABC__no_slots):
def check__uint_or_uint_reader(uint_or_uint_reader, /):
    if type(uint_or_uint_reader) is int:
        u = uint_or_uint_reader
        check_uint(u)
    else:
        uint_reader = uint_or_uint_reader
        check_type_le(IReader, uint_reader)
def uint5or_uint_reader__(ibfile, uint_or_uint_reader, /):
    'ibfile -> (uint|uint_reader) -> uint'
    if type(uint_or_uint_reader) is int:
        u = uint_or_uint_reader
    else:
        uint_reader = uint_or_uint_reader
        u = apply_reader(uint_reader, ibfile)
    check_uint(u)
    return u

def uint_or2uint_reader_(uint_or_uint_reader, /):
    '(uint|uint_reader) -> uint_reader'
    if type(uint_or_uint_reader) is int:
        u = uint_or_uint_reader
        check_uint(u)
        uint_reader = mk_ConstantTargetReader(u)
    else:
        uint_reader = uint_or_uint_reader
    check_type_le(IReader, uint_reader)
    return uint_reader
def size5or_size_reader__(ibfile, sz_or_sz_reader, /):
    '-> sz'
def addr5or_addr_reader__(ibfile, addr_or_addr_reader, /):
    '-> addr'
def size_or2size_reader_(uint_or_uint_reader, /):
    '-> size_reader'
def addr_or2addr_reader_(uint_or_uint_reader, /):
    '-> size_reader'
size5or_size_reader__ = uint5or_uint_reader__
addr5or_addr_reader__ = uint5or_uint_reader__
size_or2size_reader_ = uint_or2uint_reader_
addr_or2addr_reader_ = uint_or2uint_reader_




def check__int_or_int_reader(int_or_int_reader, /):
    if type(int_or_int_reader) is int:
        i = int_or_int_reader
    else:
        int_reader = int_or_int_reader
        check_type_le(IReader, int_reader)
def int5or_int_reader__(ibfile, int_or_int_reader, /):
    'ibfile -> (int|int_reader) -> int'
    if type(int_or_int_reader) is int:
        i = int_or_int_reader
    else:
        int_reader = int_or_int_reader
        i = apply_reader(int_reader, ibfile)
    check_type_is(int, i)
    return i

def int_or2int_reader_(int_or_int_reader, /):
    '(int|int_reader) -> int_reader'
    if type(int_or_int_reader) is int:
        i = int_or_int_reader
        int_reader = mk_ConstantTargetReader(i)
    else:
        int_reader = int_or_int_reader
    check_type_le(IReader, int_reader)
    return int_reader
def offset5or_offset_reader__(ibfile, offset_or_offset_reader, /):
    '-> offset'
def offset_or2offset_reader_(int_or_int_reader, /):
    '-> offset_reader'
offset5or_offset_reader__ = int5or_int_reader__
offset_or2offset_reader_ = int_or2int_reader_



class BytesReader(IReader):
    'see:FurtherTransformReader, IDecoder # see:ArrayReader,DependentPairReader'
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        sz_or_sz_reader = sf._xsz
        if type(sz_or_sz_reader) is int:
            sz = sz_or_sz_reader
            may_sz = sz
        else:
            sz_reader = sz_or_sz_reader
            may_sz = None
        return may_sz
    @override
    def __repr__(sf, /):
        sz_or_sz_reader = sf._xsz
        may_decoder = sf._mf
        args = [sz_or_sz_reader, may_decoder]
        if may_decoder is None:
            args.pop()
        return repr_helper(sf, *args)
    def __init__(sf, sz_or_sz_reader, may_decoder=None, /):
        'vs: AddrSizedParamReader:`addr_or_addr_reader`: here donot use uint_or2uint_reader_/mk_ConstantTargetReader, to make BytesReader prime'
        sf._xsz = sz_or_sz_reader
        sf._mf = may_decoder
    @override
    def _read_(sf, ibfile, /):
        sz = size5or_size_reader__(ibfile, sf._xsz)
        bs = _read_bytes(ibfile, sz)
        may_decoder = sf._mf
        if may_decoder is None:
            decoder = echo_decoder
        else:
            decoder = may_decoder
        obj = apply_decoder(decoder, bs)
        return obj
    @override
    def _skip_(sf, ibfile, /):
        sz = size5or_size_reader__(ibfile, sf._xsz)
        skip_bytes(ibfile, sz)
        return
def _sz_in_bytes5sz_in_bits(sz_in_bits, /):
    if 0b0111&sz_in_bits:raise ValueError
    sz_in_bytes = sz_in_bits >> 3
    #if not (sz_in_bytes << 3) == sz_in_bits:raise ValueError
    assert (sz_in_bytes << 3) == sz_in_bits
    return sz_in_bytes
def mk_UIntLEReader(sz_in_bits, /):
    sz_in_bytes = _sz_in_bytes5sz_in_bits(sz_in_bits)
    return BytesReader(sz_in_bytes, uintLE_decoder)
def mk_UIntBEReader(sz_in_bits, /):
    sz_in_bytes = _sz_in_bytes5sz_in_bits(sz_in_bits)
    return BytesReader(sz_in_bytes, uintBE_decoder)

def mk_SIntLEReader(sz_in_bits, /):
    sz_in_bytes = _sz_in_bytes5sz_in_bits(sz_in_bits)
    return BytesReader(sz_in_bytes, sintLE_decoder)
def mk_SIntBEReader(sz_in_bits, /):
    sz_in_bytes = _sz_in_bytes5sz_in_bits(sz_in_bits)
    return BytesReader(sz_in_bytes, sintBE_decoder)


uint8BE_reader = mk_UIntBEReader(8)
uint16BE_reader = mk_UIntBEReader(16)
uint32BE_reader = mk_UIntBEReader(32)
uint64BE_reader = mk_UIntBEReader(64)
uint128BE_reader = mk_UIntBEReader(128)
uint256BE_reader = mk_UIntBEReader(256)
uint512BE_reader = mk_UIntBEReader(512)
uint1024BE_reader = mk_UIntBEReader(1024)

uint8LE_reader = mk_UIntLEReader(8)
uint16LE_reader = mk_UIntLEReader(16)
uint32LE_reader = mk_UIntLEReader(32)
uint64LE_reader = mk_UIntLEReader(64)
uint128LE_reader = mk_UIntLEReader(128)
uint256LE_reader = mk_UIntLEReader(256)
uint512LE_reader = mk_UIntLEReader(512)
uint1024LE_reader = mk_UIntLEReader(1024)



sint8BE_reader = mk_SIntBEReader(8)
sint16BE_reader = mk_SIntBEReader(16)
sint32BE_reader = mk_SIntBEReader(32)
sint64BE_reader = mk_SIntBEReader(64)
sint128BE_reader = mk_SIntBEReader(128)
sint256BE_reader = mk_SIntBEReader(256)
sint512BE_reader = mk_SIntBEReader(512)
sint1024BE_reader = mk_SIntBEReader(1024)

sint8LE_reader = mk_SIntLEReader(8)
sint16LE_reader = mk_SIntLEReader(16)
sint32LE_reader = mk_SIntLEReader(32)
sint64LE_reader = mk_SIntLEReader(64)
sint128LE_reader = mk_SIntLEReader(128)
sint256LE_reader = mk_SIntLEReader(256)
sint512LE_reader = mk_SIntLEReader(512)
sint1024LE_reader = mk_SIntLEReader(1024)

def __():
    #see:ConstantInOutReader, mk_ConstantTargetReader, mk_ConstantBytesMatcher
  class ConstantTargetReader(IReader):
    'read no bytes'
    def __init__(sf, v, /):
        sf._v = v
    @override
    def _read_(sf, ibfile, /):
        return sf._v
  class ConstantBytesMatcher(IReader):
      'read return None'
      ...
class ConstantInOutReader(IReader):
    'see:AssertionReader'
    @override
    def _is_read_result_ignoreable_(sf, /):
        '-> bool #see:NamedTupleReader,IgnoreableReader'
        return True
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        bs = sf._bs
        return len(bs)
    @override
    def __repr__(sf, /):
        return repr_helper(sf, sf._bs, sf._v)
    def __init__(sf, bs, obj, /):
        check_type_is(bytes, bs)
        sf._bs = bs
        sf._v = obj
    @override
    def _read_(sf, ibfile, /):
        '???_skip_ check???'
        bs = sf._bs
        if 0:
            sz = len(bs)
            bs_ = _read_bytes(ibfile, sz)
            if not bs==bs_: raise AssertionError
        else:
            check_bytes(ibfile, bs)
        return sf._v
        return None
    @override
    def _skip_(sf, ibfile, /):
        '!!!not check!!!'
        bs = sf._bs
        skip_bytes(ibfile, len(bs))
        return
def mk_ConstantTargetReader(obj, /):
    #ConstantTargetReader
    return ConstantInOutReader(b'', obj)
def mk_ConstantBytesMatcher(bs, /):
    #ConstantBytesMatcher
    #check_bytes(...)
    return ConstantInOutReader(bs, None)

class FallbackReader(IReader):
    @override
    def _is_read_result_ignoreable_(sf, /):
        '-> bool #see:NamedTupleReader,IgnoreableReader'
        reader = sf._rdr
        return reader.is_read_result_ignoreable()
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        reader = sf._rdr
        return reader.get_may_static_num_bytes4skip()
    @override
    def __repr__(sf, /):
        reader = sf._rdr
        return repr_helper(sf, reader)
    @property
    def the_wrapped_reader(sf, /):
        return sf._rdr
    def __init__(sf, reader, /):
        check_type_le(IReader, reader)
        sf._rdr = reader
    @override
    def _read_(sf, ibfile, /):
        reader = sf._rdr
        obj = apply_reader(reader, ibfile)
        return obj
    @override
    def _skip_(sf, ibfile, /):
        reader = sf._rdr
        apply_reader(reader, ibfile, skip_only=True)
        return
UserReader = FallbackReader

class IgnoreableReader(FallbackReader):
    '[Deprecated]:[deprecated by xname]: to support NamedTupleReader, via turnoff _is_read_result_ignoreable_()'
    @override
    def _is_read_result_ignoreable_(sf, /):
        '-> bool #see:NamedTupleReader,IgnoreableReader'
        return True
class SkipReader(IgnoreableReader):
    @override
    def _read_(sf, ibfile, /):
        #FallbackReader._skip_(sf, ibfile)
        #sf._skip_(ibfile)
        apply_reader(sf.the_wrapped_reader, ibfile, skip_only=True)
        return

class FurtherTransformReader(IReader):
#class FurtherTransformReader(FallbackReader):
    @override
    def _is_read_result_ignoreable_(sf, /):
        '-> bool #see:NamedTupleReader,IgnoreableReader'  r'''
        #-> False !!! since added postprocess, the result will be used
        '''#'''
        return False
        reader = sf._rdr
        return reader.is_read_result_ignoreable()
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        reader = sf._rdr
        return reader.get_may_static_num_bytes4skip()
    @override
    def __repr__(sf, /):
        f = sf._f
        reader = sf._rdr
        return repr_helper(sf, f, reader)
    def __init__(sf, func, reader, /):
        check_callable(func)
        #check_type_le(IDecoder, func)
        check_type_le(IReader, reader)
        sf._f = func
        sf._rdr = reader
    @override
    def _read_(sf, ibfile, /):
        f = sf._f
        reader = sf._rdr
        obj_ = apply_reader(reader, ibfile)
        _obj = f(obj_)
        return _obj
    @override
    def _skip_(sf, ibfile, /):
        reader = sf._rdr
        apply_reader(reader, ibfile, skip_only=True)
        return
PostprocessReader = FurtherTransformReader

class AssertionReader(IReader):
    'see:SkipReader,FurtherTransformReader,ConstantInOutReader'
    @override
    def _is_read_result_ignoreable_(sf, /):
        '-> bool #see:NamedTupleReader,IgnoreableReader'
        return True
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        reader = sf._rdr
        return reader.get_may_static_num_bytes4skip()
    @override
    def __repr__(sf, /):
        expected_obj = sf._v
        reader = sf._rdr
        return repr_helper(sf, expected_obj, reader)
    def __init__(sf, expected_obj, reader, /):
        sf._v = expected_obj
        sf._rdr = reader
    @override
    def _read_(sf, ibfile, /):
        '!!!return None!!!'
        expected_obj = sf._v
        reader = sf._rdr
        obj = apply_reader(reader, ibfile)
        if not expected_obj == obj: raise CheckError((expected_obj, obj))
        return None
        return obj
    @override
    def _skip_(sf, ibfile, /):
        '!!!not check!!!'
        reader = sf._rdr
        apply_reader(reader, ibfile, skip_only=True)
        return









class ArrayReader(IReader):
    'vs C++.vector # see:BytesReader,DependentPairReader'
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        sz_or_sz_reader = sf._xsz
        elem_reader = sf._rdr
        if not type(sz_or_sz_reader) is int:
            sz_reader = sz_or_sz_reader
            may_sz = None
        else:
            sz_ = sz_or_sz_reader
            len_array = sz_
            may_sz4elem = elem_reader.get_may_static_num_bytes4skip()
            if may_sz4elem is None:
                may_sz = None
            else:
                sz4elem = may_sz4elem
                sz = len_array*sz4elem
                may_sz = sz
        return may_sz
    @override
    def __repr__(sf, /):
        sz_or_sz_reader = sf._xsz
        elem_reader = sf._rdr
        return repr_helper(sf, sz_or_sz_reader, elem_reader)
    def __init__(sf, sz_or_sz_reader, elem_reader, /):
        sz_reader = size_or2size_reader_(sz_or_sz_reader); del sz_reader
            #check
        check_type_le(IReader, elem_reader)
        sf._xsz = sz_or_sz_reader
        sf._rdr = elem_reader
    @override
    def _read_(sf, ibfile, /):
        '-> py.list #not py.tuple'
        sz = size5or_size_reader__(ibfile, sf._xsz)
        elem_reader = sf._rdr
        ls = [apply_reader(elem_reader, ibfile) for _ in range(sz)]
        return ls
    @override
    def _skip_(sf, ibfile, /):
        len_array = size5or_size_reader__(ibfile, sf._xsz)
        elem_reader = sf._rdr
        may_sz4elem = elem_reader.get_may_static_num_bytes4skip()
        if may_sz4elem is None:
            #too slow... for len_array=汉语大辞典.词汇量=348430
            for _ in range(len_array):
                apply_reader(elem_reader, ibfile, skip_only=True)
        else:
            sz4elem = may_sz4elem
            total = sz4elem*len_array
            bs_reader = BytesReader(total)
            apply_reader(bs_reader, ibfile, skip_only=True)

        return

def _get_may_static_num_bytes4skip_ls_of_readers(elem_readers, /):
    'Iter IReader -> may [static_num_bytes4skip]'
    sz_ls = []
    for elem_reader in elem_readers:
        may_sz4elem = elem_reader.get_may_static_num_bytes4skip()
        if may_sz4elem is None:
            may__sz_ls = None
            break
        else:
            sz4elem = may_sz4elem
            sz_ls.append(sz4elem)
    else:
            may__sz_ls = sz_ls
    return may__sz_ls
def _calc_sum_of_may_static_num_bytes4skip_ls_of_readers(elem_readers, /):
    'Iter IReader -> may static_num_bytes4skip-of-tuple'
    may__sz_ls = _get_may_static_num_bytes4skip_ls_of_readers(elem_readers)
    may_sz = fmap4may(sum, may__sz_ls)
    return may_sz
class TupleReader(IReader):
    'vs C++.struct'
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        elem_readers = sf._rdrs
        may_sz = _calc_sum_of_may_static_num_bytes4skip_ls_of_readers(elem_readers)
        return may_sz
    @override
    def __repr__(sf, /):
        elem_readers = sf._rdrs
        return repr_helper(sf, *elem_readers)
    def __init__(sf, /, *elem_readers):
        sf._rdrs = elem_readers
    @override
    def _read_(sf, ibfile, /):
        elem_readers = sf._rdrs
        ls = tuple(apply_reader(elem_reader, ibfile) for elem_reader in elem_readers)
        return ls
    @override
    def _skip_(sf, ibfile, /):
        elem_readers = sf._rdrs
        for elem_reader in elem_readers:
            apply_reader(elem_reader, ibfile, skip_only=True)
        return


class DependentPairReader(IReader):
    'vs C++.union #see: BytesReader,ArrayReader'
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        may_sz = None
        return may_sz
    @override
    def __repr__(sf, /):
        fst_reader = sf._rdr1
        fst2snd_reader = sf._k2rdr2
        return repr_helper(sf, fst_reader, fst2snd_reader)
    def __init__(sf, fst_reader, fst2snd_reader, /):
        sf._rdr1 = fst_reader
        sf._k2rdr2 = fst2snd_reader
    def read_or_skip_snd(sf, ibfile, /, *, skip_only):
        #skip_only = bool(skip_only)
        check_type_is(bool, skip_only)

        fst_reader = sf._rdr1
        obj0 = apply_reader(fst_reader, ibfile)

        fst2snd_reader = sf._k2rdr2
        if callable(fst2snd_reader):
            snd_reader = fst2snd_reader(obj0)
        else:
            snd_reader = fst2snd_reader[obj0]
        snd_reader
        may_obj1 = apply_reader(snd_reader, ibfile, skip_only=skip_only)
        return (obj0, may_obj1)
    @override
    def _read_(sf, ibfile, /):
        (obj0, obj1) = sf.read_or_skip_snd(ibfile, skip_only=False)
        return (obj0, obj1)
    @override
    def _skip_(sf, ibfile, /):
        (obj0, _None) = sf.read_or_skip_snd(ibfile, skip_only=True)
        return
CasedUnionReader = DependentPairReader






def is_xname_ignoreable_(xname, /):
    return (not xname) or xname.startswith('#')
def check_xname(xname, /):
    check_type_is(str, xname)
    if not is_xname_ignoreable_(xname):
        name = xname
        check_pseudo_identifier(name)
class NamedTupleReader(IReader):
    r'''[[[
    !!! NOTE:NamedTupleReader/NamedDependentTupleReader read result NamedTuple, using 『NamedTuple.as_getter4named_tuple()』to access attr !!!

    now not using IReader._is_read_result_ignoreable_()
        ## [Deprecated]:[deprecated by xname]:using IReader._is_read_result_ignoreable_()
            now:new: name --> xname/ignoreable_name
    see:IgnoreableReader,SkipReader
    see:NamedDependentTupleReader
    see:NamedTuple
    see:Descriptor4NamedTuple
    see: seed.helper.mk_pairs::bmk_pairs,pairs5api_,ListOrderedItems

    xname = ignoreable_name | pseudo_identifier
    ignoreable_name = '' | regex'#.*'
        see:check_pseudo_identifier()/py.str.isidentifier()
    ]]]'''#'''
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        xname_reader_pairs = sf._ps
        elem_readers = map(snd_, xname_reader_pairs)
        may_sz = _calc_sum_of_may_static_num_bytes4skip_ls_of_readers(elem_readers)
        return may_sz
    @override
    def __repr__(sf, /):
        xname_reader_pairs = sf._ps
        return repr_helper(sf, [*xname_reader_pairs])
    def __init__(sf, reader_named_tuple__or__xname_reader_pairs, /):
        '(NamedTuple<name,elem_reader> | [(xname,elem_reader)]) -> NamedTupleReader'
        if type(reader_named_tuple__or__xname_reader_pairs) is NamedTuple:
            reader_named_tuple = reader_named_tuple__or__xname_reader_pairs
            xname_reader_pairs = reader_named_tuple.iter_items()
        else:
            xname_reader_pairs = reader_named_tuple__or__xname_reader_pairs
        del reader_named_tuple__or__xname_reader_pairs
        xname_reader_pairs = tuple((xname, elem_reader) for xname, elem_reader in xname_reader_pairs)
        for xname, elem_reader in xname_reader_pairs:
            check_xname(xname)
            check_type_le(IReader, elem_reader)
        names4out = map(fst_, filterfalse(sf._is_item_ignoreable, xname_reader_pairs))
        descriptor4named_tuple4out = gmk_Descriptor4NamedTuple(names4out); del names4out
        sf._ps = xname_reader_pairs
        sf._odsptr = descriptor4named_tuple4out
    def _is_item_ignoreable(sf, item, /):
        xname, elem_reader = item
        if 999:#new2
            is_item_ignoreable = is_xname_ignoreable_(xname)
        elif 333:#new1
            #[Deprecated]
            is_item_ignoreable = (is_xname_ignoreable_(xname) or elem_reader.is_read_result_ignoreable())
        else:
            #[Deprecated]
            is_item_ignoreable = elem_reader.is_read_result_ignoreable()
        return is_item_ignoreable

    @override
    def _read_(sf, ibfile, /):
        xname_reader_pairs = sf._ps
        descriptor4named_tuple4out = sf._odsptr
        ls = []
        for xname, elem_reader in xname_reader_pairs:
            obj = apply_reader(elem_reader, ibfile)
            if not sf._is_item_ignoreable((xname, elem_reader)):
            #if xname in descriptor4named_tuple4out.name2idx:
                ls.append(obj)
        return NamedTuple(descriptor4named_tuple4out, ls)
    @override
    def _skip_(sf, ibfile, /):
        xname_reader_pairs = sf._ps
        elem_readers = map(snd_, xname_reader_pairs)
        for elem_reader in elem_readers:
             apply_reader(elem_reader, ibfile, skip_only=True)
        return
#end-class NamedTupleReader(IReader):


class NamedDependentTupleReader(IReader):
    r'''[[[
    !!! NOTE:NamedTupleReader/NamedDependentTupleReader read result NamedTuple, using 『NamedTuple.as_getter4named_tuple()』to access attr !!!

    extend:NamedTupleReader+DependentPairReader

    see:DependentPairReader
    see:NamedTupleReader
    see:NamedTuple
    see:Descriptor4NamedTuple
    see: seed.helper.mk_pairs::bmk_triples,triples5api_

    xname__elem_reader_or5prev_elems__may_prev_nms__triples :: [((xname, elem_reader5prev_elems_, prev_nms/[nm])|(xname, elem_reader, None))]

    ]]]'''#'''

    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        nonskippable_nms = sf._nonskippable_nms
        if nonskippable_nms:
            #exist: elem_reader5prev_elems_
            may_sz = None
        else:
            #all are elem_readers
            elem_readers = map(snd_, sf._ts)
            may_sz = _calc_sum_of_may_static_num_bytes4skip_ls_of_readers(elem_readers)
        return may_sz
    @override
    def __repr__(sf, /):
        xname__elem_reader_or5prev_elems__may_prev_nms__triples = sf._ts
        to_read_ex = sf._ex
        kwds = dict(to_read_ex=to_read_ex)
        if not to_read_ex:
            del kwds['to_read_ex']

        xname__elem_reader_or5prev_elems__may_prev_nms__triples = list((xname, elem_reader_or_elem_reader5prev_elems_, fmap4may(list, may_prev_nms)) for xname, elem_reader_or_elem_reader5prev_elems_, may_prev_nms in xname__elem_reader_or5prev_elems__may_prev_nms__triples)

        return repr_helper(sf, xname__elem_reader_or5prev_elems__may_prev_nms__triples, **kwds)

    def __init__(sf, xname__elem_reader_or5prev_elems__may_prev_nms__triples, /, *, to_read_ex=False):
        check_type_is(bool, to_read_ex)
        #xname__elem_reader_or5prev_elems__may_prev_nms__triples = (*map(mk_tuple, xname__elem_reader_or5prev_elems__may_prev_nms__triples),)
        #   ...may_prev_nms --> may tuple
        xname__elem_reader_or5prev_elems__may_prev_nms__triples = tuple((xname, elem_reader_or_elem_reader5prev_elems_, fmap4may(mk_tuple, may_prev_nms)) for xname, elem_reader_or_elem_reader5prev_elems_, may_prev_nms in xname__elem_reader_or5prev_elems__may_prev_nms__triples)

        nms = set()
        nonskippable_nms = set()
        for xname, elem_reader_or_elem_reader5prev_elems_, may_prev_nms in xname__elem_reader_or5prev_elems__may_prev_nms__triples:
            check_xname(xname)
            if may_prev_nms is None:
                elem_reader = elem_reader_or_elem_reader5prev_elems_
                check_type_le(IReader, elem_reader)
            else:
                elem_reader5prev_elems_ = elem_reader_or_elem_reader5prev_elems_
                check_callable(elem_reader5prev_elems_)
                prev_nms = may_prev_nms
                for prev_nm in prev_nms:
                    check_type_is(str, prev_nm)
                    if not prev_nm in nms: raise LookupError(f'{prev_nm!r} is not a previous attribute name')
                nonskippable_nms.update(prev_nms)
            #######################
            #######################
            #######################
            #SHOULD BE after 『if not prev_nm in nms:』 test
            if not is_xname_ignoreable_(xname):
                nm = xname
                nms.add(nm)


        names4out = filterfalse(is_xname_ignoreable_, map(fst_, xname__elem_reader_or5prev_elems__may_prev_nms__triples))
        descriptor4named_tuple4out = gmk_Descriptor4NamedTuple(names4out); del names4out
        sf._odsptr = descriptor4named_tuple4out
        sf._ts = xname__elem_reader_or5prev_elems__may_prev_nms__triples
        sf._nonskippable_nms = frozenset(nonskippable_nms)
        sf._ex = to_read_ex
        assert nonskippable_nms <= sf._odsptr.name2idx.keys()
    #def get descriptor4named_tuple4out(sf, /):
    def get_exported_names(sf, /):
        descriptor4named_tuple4out = sf._odsptr
        return (descriptor4named_tuple4out.names)
    def _is_xname_skippable(sf, xname, /):
        nonskippable_nms = sf._nonskippable_nms
        #is_xname_skippable = not (xname in nonskippable_nms)
        #is_xname_skippable = not (xname and xname in nonskippable_nms)
        #is_xname_skippable = not (not is_xname_ignoreable_(xname) and xname in nonskippable_nms)
        is_xname_skippable = is_xname_ignoreable_(xname) or not xname in nonskippable_nms
        return is_xname_skippable

    def read_or_skip(sf, ibfile, /, *, skip_only):
        #skip_only = bool(skip_only)
        check_type_is(bool, skip_only)
        #nonskippable_nms = sf._nonskippable_nms
        ls = []
        #prev_nm2obj = {}
        nonskippable_prev_nm2obj = {}
        ex = to_read_ex = sf._ex
        if ex:
            ls4ex = []
            begin_addr4whole = ibfile.tell()
        for idx4xname, (xname, elem_reader_or_elem_reader5prev_elems_, may_prev_nms) in enumerate(sf._ts):
            if may_prev_nms is None:
                elem_reader = elem_reader_or_elem_reader5prev_elems_
            else:
                elem_reader5prev_elems_ = elem_reader_or_elem_reader5prev_elems_
                prev_nms = may_prev_nms
                #prev_elems = (prev_nm2obj[prev_nm] for prev_nm in prev_nms)
                #assert 'a' in nonskippable_prev_nm2obj, (nonskippable_prev_nm2obj, sf._nonskippable_nms)
                prev_elems = (nonskippable_prev_nm2obj[prev_nm] for prev_nm in prev_nms)
                elem_reader = elem_reader5prev_elems_(*prev_elems)
            elem_reader
            ##########
            is_xname_skippable = sf._is_xname_skippable(xname)
            begin_addr = ibfile.tell()
            try:
                may_obj = apply_reader(elem_reader, ibfile, skip_only=skip_only and is_xname_skippable)
            except Exception as e:
                sz4ibfile = get_size_of_ibfile(ibfile)
                #raise ReadError__NamedDependentTupleReader((hex(sz4ibfile), hex(begin_addr4whole), hex(begin_addr), xname, idx4xname, sf._ts[idx4xname]))
                    #show『During handling of the above exception, another exception occurred:』
                raise ReadError__NamedDependentTupleReader((hex(sz4ibfile), hex(begin_addr4whole), hex(begin_addr), xname, idx4xname, sf._ts[idx4xname])) from e
                    #show『The above exception was the direct cause of the following exception:』
            is_xname_ignoreable = is_xname_ignoreable_(xname)
            if not is_xname_ignoreable:
                nm = xname
                ls.append(may_obj)
                #prev_nm2obj[nm] = may_obj
                if not is_xname_skippable:
                    obj = may_obj
                    nonskippable_prev_nm2obj[nm] = obj
            else:
                assert is_xname_skippable
            if ex:
                end_addr = ibfile.tell()
                #is_xname_dropped = is_xname_ignoreable
                is_xname_exported = not is_xname_ignoreable
                is_xname_refered = not is_xname_skippable
                ls4ex.append(((begin_addr,end_addr), (is_xname_exported, is_xname_refered), (xname, idx4xname), may_obj))

        if ex:
            end_addr4whole = ibfile.tell()
            _result4ex = (begin_addr4whole, end_addr4whole), ls4ex
            #ls4ex :: [((begin_addr,end_addr), (is_xname_exported, is_xname_refered), (xname, idx4xname), may_obj)]
        result = NamedTuple(sf._odsptr, ls)
        if ex:
            result4ex = result, _result4ex
            return result4ex
            #result4ex :: (result/NamedTuple, _result4ex/((begin_addr4whole, end_addr4whole), ls4ex/[((begin_addr,end_addr), (is_xname_exported, is_xname_refered), (xname, idx4xname), may_obj)]))
        return result
    @override
    def _read_(sf, ibfile, /):
        named_tuple4out_objs_or_ex = sf.read_or_skip(ibfile, skip_only=False)
        return named_tuple4out_objs_or_ex
    @override
    def _skip_(sf, ibfile, /):
        named_tuple4out_may_objs_or_ex = sf.read_or_skip(ibfile, skip_only=False)
        return
#end-class NamedDependentTupleReader(IReader):



class UntilEndValueBytesReader(IReader):
    'see:BytesReader,FurtherTransformReader,IDecoder;'
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        end_bytes, to_drop_end_bytes = sf._args
        may_sz = None if end_bytes else 0
        return may_sz
    @override
    def __repr__(sf, /):
        end_bytes, to_drop_end_bytes = sf._args
        kwds = dict(to_drop_end_bytes=to_drop_end_bytes)
        if not to_drop_end_bytes:
            del kwds['to_drop_end_bytes']
        return repr_helper(sf, end_bytes, **kwds)
    def __init__(sf, end_bytes, /, *, to_drop_end_bytes=False):
        sf._args = end_bytes, to_drop_end_bytes
        #####
        check_type_is(bytes, end_bytes)
        check_type_is(bool, to_drop_end_bytes)
        if to_drop_end_bytes and not end_bytes: raise TypeError

    @override
    def _read_(sf, ibfile, /):
        'include end_bytes <<== end_bytes may be empty'
        end_bytes, to_drop_end_bytes = sf._args
        sz = len(end_bytes)
        if not sz:
            assert not to_drop_end_bytes
            return b'' #include end_bytes
        bs = _read_bytes(ibfile, sz)
        bs = bytearray(bs)
        while not bs[-sz:] == end_bytes:# bs[-sz:] ok <<== [sz > 0]
            b = _read_bytes(ibfile, 1)
                # ^EOFError
            #bug: bs.append(b)
            bs.append(*b)
        if to_drop_end_bytes:
            del bs[-sz:]
        bs = bytes(bs)
        return bs
    #@override
    #def _skip_(sf, ibfile, /):
#end-class UntilEndValueBytesReader(IReader):


def ipop_and_drop4list(ls, /):
    ls.pop()
    return ls
class UntilEndValueArrayReader(IReader):
    r'''
    see:UntilReadEndValueArrayReader;ArrayReader,FurtherTransformReader,IDecoder;

    result list endswith end_obj

    `may_postprocess`:
        [UntilEndValueArrayReader(..., postprocess, ...) ~==~ FurtherTransformReader(UntilEndValueArrayReader(..., None, ...), postprocess)]
        why? since end_obj may be not required.
            postprocess = ipop_and_drop4list
    '''#'''
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        may_sz = None
            #even when [elem_reader.get_may_static_num_bytes4skip()==0]
            #   <<== may check more then seekback
        return may_sz
    @override
    def __repr__(sf, /):
        (elem_reader, end_value, may_postprocess, may_op, to_drop_end_obj) = sf._args
        args = [elem_reader, end_value, may_postprocess]
        kwds = dict(may_op=may_op, to_drop_end_obj=to_drop_end_obj)
        if not to_drop_end_obj:
            del kwds['to_drop_end_obj']
        if may_op is None or may_op == '==':
            del kwds['may_op']
        if may_postprocess is None:
            args.pop()

        return repr_helper(sf, *args, **kwds)
    def __init__(sf, elem_reader, end_value, may_postprocess=None, /, *, may_op:'==,is,in,is_not,not_in,_(),._()'='==', to_drop_end_obj=False):
        r'''
        `may_op`:see:seed.types.Tester@view_registered_ops4mk_tester_
            ==,in,_()
            __eq__,__contains__,__call__
        '''#'''
        sf._args = (elem_reader, end_value, may_postprocess, may_op, to_drop_end_obj)
        #####
        check_type_is(bool, to_drop_end_obj)
        check_type_le(IReader, elem_reader)
        postprocess = ifNone(may_postprocess, echo)
        check_callable(postprocess)
        tester = mk_tester_(may_op, end_value)
        #print(tester)

        sf._t = tester
        return
    @override
    def _read_(sf, ibfile, /):
        '-> list<obj> #not tuple #include `end_obj`'
        (elem_reader, end_value, may_postprocess, may_op, to_drop_end_obj) = sf._args
        tester = sf._t
        is_end_value_ = curry1(is_good, tester)
        ls = []
        while 1:
            obj = apply_reader(elem_reader, ibfile)
            ls.append(obj) #include `end_obj`
            if is_end_value_(obj):
                break
        if to_drop_end_obj:
            ls.pop()
        postprocess = ifNone(may_postprocess, echo)
        r = postprocess(ls)
        return r

    @override
    def _skip_(sf, ibfile, /):
        (elem_reader, end_value, may_postprocess, may_op, to_drop_end_obj) = sf._args
        tester = sf._t
        is_end_value_ = curry1(is_good, tester)
        while 1:
            obj = apply_reader(elem_reader, ibfile)
            if is_end_value_(obj):
                break
        return#without postprocess
#end-class UntilEndValueArrayReader(IReader):


def try_apply_decoder(decoder, bs, /):
    return try_(apply_decoder, decoder, bs)

def try_apply_reader(reader, ibfile, /, skip_only=False):
    saved_position = ibfile.tell()
    tmay_r = try_(apply_reader, reader, ibfile, skip_only=skip_only)
    if not tmay_r:
        #on_err:seekback
        ibfile.seek(saved_position)
    return tmay_r
    ######################
    #bug: try_() doesnot raise
    with with4seekback__on_err(ibfile):
        return try_(apply_reader, reader, ibfile, skip_only=skip_only)

class UntilReadEndValueArrayReader(IReader):
    r'''
    see:UntilEndValueArrayReader;ArrayReader,FurtherTransformReader,IDecoder;

    result list endswith end_obj
    '''#'''

    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        may_sz = None
            #even when [end_value_reader.get_may_static_num_bytes4skip()==0]
            #   <<== may check more then seekback
        return may_sz
    @override
    def __repr__(sf, /):
        (elem_reader, end_value_reader, may_postprocess, to_drop_end_obj) = sf._args
        args = [elem_reader, end_value_reader, may_postprocess]
        kwds = dict(to_drop_end_obj=to_drop_end_obj)
        if not to_drop_end_obj:
            del kwds['to_drop_end_obj']
        if may_postprocess is None:
            args.pop()

        return repr_helper(sf, *args, **kwds)
    def __init__(sf, elem_reader, end_value_reader, may_postprocess=None, /, *, to_drop_end_obj=False):
        sf._args = (elem_reader, end_value_reader, may_postprocess, to_drop_end_obj)
        #####
        check_type_is(bool, to_drop_end_obj)
        check_type_le(IReader, elem_reader)
        check_type_le(IReader, end_value_reader)
        postprocess = ifNone(may_postprocess, echo)
        check_callable(postprocess)

        return
    @override
    def _read_(sf, ibfile, /):
        '-> list<obj> #not tuple #include `end_obj`'
        (elem_reader, end_value_reader, may_postprocess, to_drop_end_obj) = sf._args
        ls = []
        while 1:
            tmay_end_obj = try_apply_reader(end_value_reader, ibfile)
            if tmay_end_obj:
                [end_obj] = tmay_end_obj
                ls.append(end_obj) #include `end_obj`
                break
            obj = apply_reader(elem_reader, ibfile)
            ls.append(obj)
        #####
        if to_drop_end_obj:
            ls.pop()
        postprocess = ifNone(may_postprocess, echo)
        r = postprocess(ls)
        return r

    @override
    def _skip_(sf, ibfile, /):
        (elem_reader, end_value_reader, may_postprocess, to_drop_end_obj) = sf._args
        while 1:
            if 1:
                tmay_end_obj = try_apply_reader(end_value_reader, ibfile)
                    #skip will without check
                    #add skip_with_check??? must be read() otherwise should distinguish pure code out
                if tmay_end_obj:
                    break
            else:
                raise 000
                tmay_None = try_apply_reader(end_value_reader, ibfile, skip_only=True)
                if tmay_None:
                    break
            #####
            apply_reader(elem_reader, ibfile, skip_only=True)
        #####
        return#without postprocess

#end-class UntilReadEndValueArrayReader(IReader):






def check_addrXparam(addrXparam, /):
    #addr_or_addr_param_pair
    if not type(addrXparam) in (int, tuple): raise TypeError(type(addrXparam))
    check_addrXparam_or_reader(addrXparam)

def check_addrXparam_or_reader(addrXparam_or_reader, /):
    addr_or_addr_param_pair_or_reader = addrXparam_or_reader
    if type(addr_or_addr_param_pair_or_reader) is int:
        addr = addr_or_addr_param_pair_or_reader
        check_uint(addr)
        addrXparam = addr
    elif type(addr_or_addr_param_pair_or_reader) is tuple:
        addr_param_pair = addr_or_addr_param_pair_or_reader
        check_pair(addr_param_pair)
        addr, param = addr_param_pair
        check_uint(addr)
        addrXparam = addr_param_pair
    else:
        addrXparam_reader = addr_or_addr_param_pair_or_reader
        check_type_le(IReader, addrXparam_reader)
def addrXparam_or2reader_(addrXparam_or_reader, /):
    check_addrXparam_or_reader(addrXparam_or_reader)
    if type(addrXparam_or_reader) in (int, tuple):
        addrXparam = addrXparam_or_reader
        addrXparam_reader = mk_ConstantTargetReader(addrXparam)
    else:
        addrXparam_reader = addrXparam_or_reader
    check_type_le(IReader, addrXparam_reader)
    return addrXparam_reader
def addrXparam_as_args_(addrXparam, /):
    check_addrXparam(addrXparam)
    if type(addrXparam) is int:
        addr = addrXparam
        args = (addr,)
    else:
        addr_param_pair = addrXparam
        addr, param = addr_param_pair
        args = addr_param_pair
    return args



def _mk_obj_reader5Mparam__reader(obj_reader, /):
    def obj_reader5Mparam_(param=None, /):
        return obj_reader
    return obj_reader5Mparam_
def _mk_obj_reader5Mparam(obj_reader_or5Mparam, /):
    if callable(obj_reader_or5Mparam):
        obj_reader5Mparam_ = obj_reader_or5Mparam
    else:
        obj_reader = obj_reader_or5Mparam
        check_type_le(IReader, obj_reader)
        obj_reader5Mparam_ = _mk_obj_reader5Mparam__reader(obj_reader)
    obj_reader5Mparam_

    check_callable(obj_reader5Mparam_)
    return obj_reader5Mparam_
class AddrDereferenceReader(IReader):
    #AddrDereferenceReader(sf, addr_or_addr_param_pair_or_reader, obj_reader_or5Mparam, /)
        #<-- AddrDereferenceReader(addr_param_reader, obj_reader5param_, /):
    #addr_param_reader --> addr_or_addr_param_pair_or_reader
    #obj_reader5param_ --> obj_reader_or5Mparam
    #addrXparam = addr|(addr,param)
    #addrMparam = (addr,*tmay_param) = (addr,)|(addr,param)
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        addrMparam_reader = sf._rdr4aMp
        #obj_reader will be applied at `heap` section ==>> seekback
        return addrMparam_reader.get_may_static_num_bytes4skip()
    @override
    def __repr__(sf, /):
        (addr_or_addr_param_pair_or_reader, obj_reader_or5Mparam) = sf._args
        return repr_helper(sf, addr_or_addr_param_pair_or_reader, obj_reader_or5Mparam)
    def __init__(sf, addr_or_addr_param_pair_or_reader, obj_reader_or5Mparam, /):
        sf._args = (addr_or_addr_param_pair_or_reader, obj_reader_or5Mparam)
        #####
        #####
        addrXparam_reader = addrXparam_or2reader_(addr_or_addr_param_pair_or_reader)
        addrMparam_reader = FurtherTransformReader(addrXparam_as_args_, addrXparam_reader)
        obj_reader5Mparam_ = _mk_obj_reader5Mparam(obj_reader_or5Mparam)
        #sf._rdr4aXp = addrXparam_reader
        sf._rdr4aMp = addrMparam_reader
        sf._rdr5Mp = obj_reader5Mparam_
    @override
    def _read_(sf, ibfile, /):
        addrMparam_reader = sf._rdr4aMp
        (addr4obj, *tmay_param) = apply_reader(addrMparam_reader, ibfile)
        obj_reader5Mparam_ = sf._rdr5Mp
        obj_reader = obj_reader5Mparam_(*tmay_param)
        check_type_le(IReader, obj_reader)
        with with4seekback__on_no_err(ibfile):
            checked_seek(ibfile, addr4obj)
            obj = apply_reader(obj_reader, ibfile)
            #goback into stack-section after read obj in heap-section at unorder addr
        return obj
    @override
    def _skip_(sf, ibfile, /):
        addrMparam_reader = sf._rdr4aMp
        apply_reader(addrMparam_reader, ibfile, skip_only=True)
        return


u8_decoder
zlib_decoder
class AddrSizedParamReader(IReader):
    r'''[[[
    'inside Array[(addr,param)], using next-addr or end-addr to yield size4target --> (begin_addr4target,sized_param/(size4target,param))'

work with AddrDereferenceReader:
AddrDereferenceReader+AddrSizedParamReader
>>> obj_reader5param_ = dot[BytesReader, fst_]
>>> reader = AddrDereferenceReader(AddrSizedParamReader(addr_reader, sz_reader, None), obj_reader5param_)
    ]]]'''#'''
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        addr_reader = sf._rdr4a
        param_reader = sf._rdr4p
        elem_readers = addr_reader, param_reader
        may_sz = _calc_sum_of_may_static_num_bytes4skip_ls_of_readers(elem_readers)
        return may_sz

    @override
    def __repr__(sf, /):
        #addr_reader = sf._rdr4a
        param_reader = sf._rdr4p
        #may_end_addr4target = sf._mend
        #return repr_helper(sf, addr_reader, param_reader, may_end_addr4target)
        addr_or_addr_reader = sf._xrdr4a
        may_end_addr4target_or_reader = sf._mxrdr4e
        return repr_helper(sf, addr_or_addr_reader, param_reader, may_end_addr4target_or_reader)
    def __init__(sf, addr_reader, param_reader, may_end_addr4target, /):
        'why not addr_or_addr_reader?? addr may not be uint??? SHOULD-BE'
        #addr_reader
        check_type_le(IReader, addr_reader)
    def __init__(sf, addr_or_addr_reader, param_reader, may_end_addr4target, /):
        'buggy:when AddrSizedParamReader(addr, param_reader, None)'
        if not may_end_addr4target is None:
            end_addr4target = may_end_addr4target
            check_uint(end_addr4target)
        sf._mend = may_end_addr4target
    def __init__(sf, addr_or_addr_reader, param_reader, may_end_addr4target_or_reader, /):
        #addr_or_addr_reader
        #mk_ConstantTargetReader(addr)
        #addr5or_addr_reader__
        #uint_or2uint_reader_
        #check__uint_or_uint_reader(addr_or_addr_reader)
        addr_reader = addr_or2addr_reader_(addr_or_addr_reader)
        end_addr4target_or_reader = ifNone(may_end_addr4target_or_reader, addr_reader)
        end_addr_reader4target = addr_or2addr_reader_(end_addr4target_or_reader)
        ######################
        ######################
        check_type_le(IReader, addr_reader)
        check_type_le(IReader, param_reader)
        check_type_le(IReader, end_addr_reader4target)
        sf._rdr4a = addr_reader
        sf._rdr4p = param_reader
        sf._rdr4e = end_addr_reader4target
        sf._xrdr4a = addr_or_addr_reader
        sf._mxrdr4e = may_end_addr4target_or_reader
    @override
    def _read_(sf, ibfile, /):
        addr_reader = sf._rdr4a
        param_reader = sf._rdr4p
        #may_end_addr4target = sf._mend
        end_addr_reader4target = sf._rdr4e

        begin_addr4target = apply_reader(addr_reader, ibfile)
        param = apply_reader(param_reader, ibfile)
        r'''[[[
        if not may_end_addr4target is None:
            end_addr4target = may_end_addr4target
        else:
            with with4seekback__on_no_err(ibfile):
                end_addr4target = apply_reader(addr_reader, ibfile)
                #peek next addr then goback
            check_uint(end_addr4target)
        end_addr4target
        ]]]'''#'''
        with with4seekback__on_no_err(ibfile):
            end_addr4target = apply_reader(end_addr_reader4target, ibfile)

        size4target = end_addr4target - begin_addr4target
        if size4target < 0:raise ValueError((size4target, end_addr4target, begin_addr4target))
        sized_param = (size4target, param)
        return begin_addr4target, sized_param
        return (begin_addr4target, sized_param/(size4target, param))
    @override
    def _skip_(sf, ibfile, /):
        addr_reader = sf._rdr4a
        param_reader = sf._rdr4p
        apply_reader(addr_reader, ibfile, skip_only=True)
        apply_reader(param_reader, ibfile, skip_only=True)
        return
#end-class AddrSizedParamReader(IReader):

def _list_append1(pair, /):
    ls, x = pair
    ls.append(x)
    return ls
def _mk_AddrSizedParamArrayReader(len_array, may_end_addr4last_target, addr_reader, param_reader, obj_reader5sized_param_, /):
    r'''[Deprecated by AddrSizedParamArrayReader]

    may_end_addr4last_target
        None -> not to read last elem, but access its begin addr as end addr of prev elem
    #'''
    check_uint(len_array)
    L = len_array
    if L == 0:
        return mk_ConstantTargetReader(())
    elem_reader = AddrSizedParamReader(addr_reader, param_reader, None)
    array_reader_except_last = ArrayReader(L-1, elem_reader)
    if may_end_addr4last_target is None:
        array_reader = array_reader_except_last
    else:
        end_addr4last_target = may_end_addr4last_target
        last_elem_reader = AddrSizedParamReader(addr_reader, param_reader, end_addr4last_target)
        array_reader = FurtherTransformReader(_list_append1, TupleReader(array_reader_except_last, last_elem_reader))
    array_reader
    return array_reader


#DONE:批量读整个地址数组先，再批量解引用，避免来回移动地址
class AddrSizedParamArrayReader(IReader):
    'see:AddrSizedParamReader(IReader)'
    #'inside Array[(addr,param)], using next-addr or end-addr to yield size4target --> (begin_addr4target,sized_param/(size4target,param))'
    #AddrSizedParamArrayReader(len_array, may_end_addr4last_target, addr_reader, param_reader, obj_reader5sized_param_, /)._read_(ibfile, /)-> [obj]
    #AddrSizedParamArrayReader(len_array, may_end_addr4last_target, addr_reader, param_reader, /)._read_(ibfile, /)-> [(begin_addr,(sz,param))]
    #AddrSizedParamArrayReader(len_array, may_end_addr4last_target, addr_reader, None, /)._read_(ibfile, /)-> [(begin_addr,sz)]
    #obj_reader5sized_param_ --> may_obj_reader5sized_param_
    #param_reader --> may_param_reader
    #? may_end_addr4last_target -->? may_end_addr_or_reader4last_target
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        (len_array, may_end_addr4last_target, addr_reader, may_param_reader, may_obj_reader5sized_param_) = sf._args
        L = len_array
        if L == 0:
            return 0
        if may_end_addr4last_target is None:
            #read/skip (L-1) elems
            #last elem remains unread
            num_elems4skip = L-1
            array_reader_ = sf._1_arr_rdr
            array_readerX = array_reader_
        else:
            #read/skip L elems
            num_elems4skip = L
            array_reader = sf._arr_rdr
            array_readerX = array_reader
        if num_elems4skip == 0:
            return 0
        return array_readerX.get_may_static_num_bytes4skip()
            #sub_readers_per_elem = addr_reader, param_reader
            #may_sz4elem = _calc_sum_of_may_static_num_bytes4skip_ls_of_readers(sub_readers_per_elem)
            #... may_sz4elem*num_elems4skip

    @override
    def __repr__(sf, /):
        [*args] = (len_array, may_end_addr4last_target, addr_reader, may_param_reader, may_obj_reader5sized_param_) = sf._args
        if may_obj_reader5sized_param_ is None:
            args.pop()
        return repr_helper(sf, *args)
        return repr_helper(sf, len_array, may_end_addr4last_target, addr_reader, may_param_reader, may_obj_reader5sized_param_)
    def __init__(sf, len_array, may_end_addr4last_target, addr_reader, may_param_reader, may_obj_reader5sized_param_=None, /):
        sf._args = (len_array, may_end_addr4last_target, addr_reader, may_param_reader, may_obj_reader5sized_param_)
        #####
        check_uint(len_array)
        if not may_end_addr4last_target is None:
            end_addr4last_target = may_end_addr4last_target
            check_uint(end_addr4last_target)
        check_type_le(IReader, addr_reader)
        if not may_param_reader is None:
            param_reader = may_param_reader
        else:
            param_reader = mk_ConstantTargetReader(None)
        check_type_le(IReader, param_reader)
        if not may_obj_reader5sized_param_ is None:
            obj_reader5sized_param_  = may_obj_reader5sized_param_
            check_callable(obj_reader5sized_param_)
        #####
        L = len_array
        if L == 0:
            return
        elem_reader = TupleReader(addr_reader, param_reader)
        if may_end_addr4last_target is None:
            array_reader_except_last = ArrayReader(L-1, elem_reader)
            sf._1_arr_rdr = array_reader_ = array_reader_except_last
        else:
            sf._arr_rdr = array_reader = ArrayReader(L, elem_reader)

    @override
    def _read_(sf, ibfile, /):
      def read_(without_param, may_obj_reader5sized_param_, pairs, end_addr4last_target, /):
        begins = [*map(fst_, pairs)]
        ends = [*begins[1:], end_addr4last_target]
        sz_ls = [*map(int.__sub__, ends, begins)]
        for sz in sz_ls:
            check_uint(sz)
        if without_param:
            begin_addr__sz___pairs = [*zip(begins, sz_ls)]
            begin_szparam_ls = begin_addr__sz___pairs
        else:
            params = [*map(snd_, pairs)]
            begin_addr__sized_param___pairs = [*zip(begins, zip(sz_ls, params))]
            begin_szparam_ls = begin_addr__sized_param___pairs
        begin_szparam_ls

        if may_obj_reader5sized_param_ is None:
            objs = begin_szparam_ls
            return objs
        obj_reader5sized_param_  = may_obj_reader5sized_param_
        objs = []
        with with4seekback__on_no_err(ibfile):
          for begin, sz_or_sized_param in begin_szparam_ls:
            #sz = end - begin
            #check_uint(sz)
            obj_reader = obj_reader5sized_param_(sz_or_sized_param)
            checked_seek(ibfile, begin)
            obj = apply_reader(obj_reader, ibfile)
            objs.append(obj)
        return objs

      def _():
        (len_array, may_end_addr4last_target, addr_reader, may_param_reader, may_obj_reader5sized_param_) = sf._args
        without_param = may_param_reader is None
        L = len_array
        if L == 0:
            return []
        if may_end_addr4last_target is None:
            array_reader_ = sf._1_arr_rdr
            pairs_ = apply_reader(array_reader_, ibfile)
            with with4seekback__on_no_err(ibfile):
                end_addr4snd_last_target = begin_addr4last_target = apply_reader(addr_reader, ibfile)
                # elem is arrary elem
                # target is remote obj that addr ref to

            objs_ = read_(without_param, may_obj_reader5sized_param_, pairs_, end_addr4snd_last_target)
            return objs_
        else:
            end_addr4last_target = may_end_addr4last_target
            array_reader = sf._arr_rdr
            pairs = apply_reader(array_reader, ibfile)
            objs = read_(without_param, may_obj_reader5sized_param_, pairs, end_addr4last_target)
            return objs
      #end-def _():
      return _()

    @override
    def _skip_(sf, ibfile, /):
        (len_array, may_end_addr4last_target, addr_reader, may_param_reader, may_obj_reader5sized_param_) = sf._args
        L = len_array
        if L == 0:
            return
        if may_end_addr4last_target is None:
            array_reader_ = sf._1_arr_rdr
            apply_reader(array_reader_, ibfile, skip_only=True)
        else:
            #end_addr4last_target = may_end_addr4last_target
            array_reader = sf._arr_rdr
            apply_reader(array_reader, ibfile, skip_only=True)
        return
#end-class AddrSizedParamArrayReader(IReader):

def _mk_obj_reader5param__reader(obj_reader, /):
    def obj_reader5param_(param=None, /):
        return obj_reader
    return obj_reader5param_
def _mk_obj_reader5param(obj_reader_or5param, /):
    if callable(obj_reader_or5param):
        obj_reader5param_ = obj_reader_or5param
    else:
        obj_reader = obj_reader_or5param
        check_type_le(IReader, obj_reader)
        obj_reader5param_ = _mk_obj_reader5param__reader(obj_reader)
    obj_reader5param_

    check_callable(obj_reader5param_)
    return obj_reader5param_

class ArrayTranformReader(IReader):
    'see:AddrDereferenceReader+AddrSizedParamArrayReader'
    #ArrayTranformReader(param_array_or_reader, obj_reader_or5param, /)
        #AddrDereferenceReader(sf, addr_or_addr_param_pair_or_reader, obj_reader_or5Mparam, /)
        #AddrSizedParamArrayReader(len_array, may_end_addr4last_target, addr_reader, may_param_reader, may_obj_reader5sized_param_=None, /)
    def __init__(sf, param_array_or_reader, obj_reader_or5param, /):
        try:
            iter(param_array_or_reader)
        except TypeError:
            param_array_reader = param_array_or_reader
        else:
            param_array = param_array_or_reader
            param_array = mk_tuple(param_array)
            param_array_or_reader = param_array
                #updated input『param_array_or_reader』
                #sf._args SHOULD BE below
            param_array_reader = mk_ConstantTargetReader(param_array)
        param_array_reader
        check_type_le(IReader, param_array_reader)
        if 1:
            #updated input『param_array_or_reader』
            sf._args = param_array_or_reader, obj_reader_or5param

        obj_reader5param_ = _mk_obj_reader5param(obj_reader_or5param)

        may_target_array_reader = None
        if obj_reader_or5param is obj_reader5param_:
            #callable(obj_reader_or5param)
            pass
        elif param_array_or_reader is param_array_reader:
            # param_array_or_reader :: IReader
            pass
        else:
            obj_reader = obj_reader_or5param
            param_array # := param_array_or_reader
            target_array_reader = ArrayReader(len(param_array), obj_reader)
            may_target_array_reader = target_array_reader
        may_target_array_reader

        sf._rdr5p = obj_reader5param_
        sf._rdr4ps = param_array_reader
        sf._mrdr4ts = may_target_array_reader


    @override
    def __repr__(sf, /):
        param_array_or_reader, obj_reader_or5param = sf._args
        if type(param_array_or_reader) is tuple:
            param_array_or_reader = [*param_array_or_reader]
        return repr_helper(sf, param_array_or_reader, obj_reader_or5param)
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        may_target_array_reader = sf._mrdr4ts
        if may_target_array_reader is None:
            return None
        target_array_reader = may_target_array_reader
        return target_array_reader.get_may_static_num_bytes4skip()

    @override
    def _read_(sf, ibfile, /):
        'ibfile -> obj #ibfile.position move forward'
        obj_reader5param_ = sf._rdr5p
        param_array_reader = sf._rdr4ps
        param_array = apply_reader(param_array_reader, ibfile)
        ls = []
        for param in param_array:
            obj_reader = obj_reader5param_(param)
            obj = apply_reader(obj_reader, ibfile)
            ls.append(obj)
        return ls
    @override
    def _skip_(sf, ibfile, /):
        obj_reader5param_ = sf._rdr5p
        param_array_reader = sf._rdr4ps
        param_array = apply_reader(param_array_reader, ibfile)
            #need:len(param_array)
        for param in param_array:
            obj_reader = obj_reader5param_(param)
            apply_reader(obj_reader, ibfile, skip_only=True)
        return None

#end-class ArrayTranformReader(IReader):



class TellAddrReader(IReader):
    __slots__ = ()

    def __new__(cls, /):
        global tell_addr_reader
        if not cls is __class__: raise TypeError(cls)
        try:
            sf = tell_addr_reader
        except NameError:
            sf = object.__new__(__class__)
            tell_addr_reader = sf
        assert sf is tell_addr_reader
        return sf


    @override
    def __repr__(sf, /):
        return repr_helper(sf)
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        return 0

    @override
    def _read_(sf, ibfile, /):
        'ibfile -> obj #ibfile.position move forward'
        return ibfile.tell()
    @override
    def _skip_(sf, ibfile, /):
        return None
tell_addr_reader = TellAddrReader()
assert tell_addr_reader is TellAddrReader()
#end-class TellAddrReader(IReader):

def mk_AddrAssertionReader(addr, /):
    return AssertionReader(addr, tell_addr_reader)

class EOFAddrReader(IReader):
    __slots__ = ()

    def __new__(cls, /):
        global eof_addr_reader
        if not cls is __class__: raise TypeError(cls)
        try:
            sf = eof_addr_reader
        except NameError:
            sf = object.__new__(__class__)
            eof_addr_reader = sf
        assert sf is eof_addr_reader
        return sf


    @override
    def __repr__(sf, /):
        return repr_helper(sf)
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        return 0

    @override
    def _read_(sf, ibfile, /):
        'ibfile -> obj #ibfile.position move forward'
        return get_size_of_ibfile(ibfile)
    @override
    def _skip_(sf, ibfile, /):
        return None
eof_addr_reader = EOFAddrReader()
assert eof_addr_reader is EOFAddrReader()
FileSizeReader = EOFAddrReader
file_size_reader = eof_addr_reader
#end-class EOFAddrReader(IReader):

check__int_or_int_reader
offset5or_offset_reader__
offset_or2offset_reader_
class OffsetReader(IReader):
    def __init__(sf, /, *offset_or_reader__seq, to_neg=False):
        check_type_is(bool, to_neg)
        offset_readers = tuple(map(offset_or2offset_reader_, offset_or_reader__seq))
        sf._rdrs = offset_readers
        sf._args = offset_or_reader__seq, to_neg

    @override
    def __repr__(sf, /):
        offset_or_reader__seq, to_neg = sf._args
        kwds = dict(to_neg=to_neg)
        if not to_neg:
            del kwds['to_neg']
        return repr_helper(sf, *offset_or_reader__seq, **kwds)
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        offset_readers = sf._rdrs
        may_sz = _calc_sum_of_may_static_num_bytes4skip_ls_of_readers(offset_readers)
        return may_sz

    @override
    def _read_(sf, ibfile, /):
        'ibfile -> obj #ibfile.position move forward'
        offset_or_reader__seq, to_neg = sf._args
        offset_readers = sf._rdrs
        acc = 0
        for offset_reader in offset_readers:
            offset = apply_reader(offset_reader, ibfile)
            check_type_is(int, offset)
            acc += offset
        if to_neg:
            acc = -acc

        return acc
    @override
    def _skip_(sf, ibfile, /):
        offset_readers = sf._rdrs
        for offset_reader in offset_readers:
            apply_reader(offset_reader, ibfile, skip_only=True)
        return None
SumReader = OffsetReader
#end-class OffsetReader(IReader):

_addr_name2reader = (
{'eof':eof_addr_reader
,'tell':tell_addr_reader
})
def addr_or_name_or2reader_(addr_or_reader_or_name:'eof,tell', /):
    if type(addr_or_reader_or_name) is str:
        addr_name = addr_or_reader_or_name
        addr_reader = _addr_name2reader[addr_name]
        addr_or_reader = addr_reader
    else:
        addr_or_reader = addr_or_reader_or_name
    addr_or_reader
    #####
    addr_reader = addr_or2addr_reader_(addr_or_reader)
    return addr_reader

class AddrReader(IReader):
    r'''[[[
    see:OffsetReader;uint64LE_reader

    base_addr_name <- {'eof', 'tell'}
        * 'eof' -> eof_addr_reader #os.SEEK_END
        * 'tell' -> tell_addr_reader #os.SEEK_CUR
    base_addr4begin == 0 #os.SEEK_SET
    ]]]'''#'''
    def __init__(sf, base_addr_or_reader_or_name:'eof,tell', offset_or_reader, /):
        sf._args = base_addr_or_reader_or_name, offset_or_reader
        #####
        base_addr_reader = addr_or_name_or2reader_(base_addr_or_reader_or_name)
        offset_reader = offset_or2offset_reader_(offset_or_reader)
        sf._rdrs = base_addr_reader, offset_reader
    @property
    def args(sf, /):
        base_addr_or_reader_or_name, offset_or_reader = sf._args
        return sf._args
    @override
    def __repr__(sf, /):
        base_addr_or_reader_or_name, offset_or_reader = sf.args
        return repr_helper(sf, base_addr_or_reader_or_name, offset_or_reader)
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        base_addr_reader, offset_reader = sf._rdrs
        may_sz = _calc_sum_of_may_static_num_bytes4skip_ls_of_readers([base_addr_reader, offset_reader])
        return may_sz

    @override
    def _read_(sf, ibfile, /):
        'ibfile -> obj #ibfile.position move forward'
        base_addr_reader, offset_reader = sf._rdrs
        base_addr = apply_reader(base_addr_reader, ibfile)
        check_uint(base_addr)

        offset = apply_reader(offset_reader, ibfile)
        check_type_is(int, offset)

        addr = base_addr + offset
        check_uint(addr)
        return addr
    @override
    def _skip_(sf, ibfile, /):
        base_addr_reader, offset_reader = sf._rdrs
        base_addr = apply_reader(base_addr_reader, ibfile, skip_only=True)
        apply_reader(offset_reader, ibfile, skip_only=True)
        return None
#end-class AddrReader(IReader):


class SeekAddrReader(IReader):
    'see:AddrReader'
    def __init__(sf, base_addr_or_reader_or_name:'eof,tell', offset_or_reader=0, /, *, to_read_bytes=False, allowed_to_read_bytes_on_seekback=False):
        check_type_is(bool, to_read_bytes)
        check_type_is(bool, allowed_to_read_bytes_on_seekback)
        if allowed_to_read_bytes_on_seekback and not to_read_bytes:raise TypeError

        addr_reader = AddrReader(base_addr_or_reader_or_name, offset_or_reader)
        sf._rdr4a = addr_reader
        sf._flgs = to_read_bytes, allowed_to_read_bytes_on_seekback
    @property
    def _args(sf, /):
        base_addr_or_reader_or_name, offset_or_reader = sf._rdr4a.args
        to_read_bytes, allowed_to_read_bytes_on_seekback = sf._flgs
        return base_addr_or_reader_or_name, offset_or_reader, to_read_bytes, allowed_to_read_bytes_on_seekback
    @override
    def __repr__(sf, /):
        base_addr_or_reader_or_name, offset_or_reader, to_read_bytes, allowed_to_read_bytes_on_seekback = sf._args
        args = [base_addr_or_reader_or_name, offset_or_reader]
        kwds = dict(to_read_bytes=to_read_bytes, allowed_to_read_bytes_on_seekback=allowed_to_read_bytes_on_seekback)
        if not allowed_to_read_bytes_on_seekback:
            del kwds['allowed_to_read_bytes_on_seekback']
        if not to_read_bytes:
            del kwds['to_read_bytes']
            assert not kwds
        if offset_or_reader in [0]:
            args.pop()
        return repr_helper(sf, *args, **kwds)
    @override
    def _get_may_static_num_bytes4skip_(sf, /):
        '-> may uint #see:_skip_()'
        return None
    def read_or_skip(sf, ibfile, /, *, skip_only):
        '-> addr|may bytes' ' # !!! check read on seekback !!!'
        check_type_is(bool, skip_only)
        to_read_bytes, allowed_to_read_bytes_on_seekback = sf._flgs
        addr_reader = sf._rdr4a
        addr4to = apply_reader(addr_reader, ibfile)
        check_uint(addr4to)
        if not to_read_bytes:
            checked_seek(ibfile, addr4to)
            return addr4to
            return ibfile.tell()
                #??? <<== since input may be addr_reader, return addr4to to save one tell_addr_reader apply.
        else:
            addr4from = ibfile.tell()
            sz = addr4to - addr4from
            if sz < 0:
                if not allowed_to_read_bytes_on_seekback: raise ReadError__SeekAddrReader
                checked_seek(ibfile, addr4to)
                sz = -sz
            check_uint(sz)
            if skip_only:
                may_bs = None
            else:
                bs = _read_bytes(ibfile, sz)
                may_bs = bs
            checked_seek(ibfile, addr4to)
            return may_bs
    @override
    def _read_(sf, ibfile, /):
        'ibfile -> obj #ibfile.position move forward'
        addr_or_bs = sf.read_or_skip(ibfile, skip_only=False)
        return addr_or_bs
    @override
    def _skip_(sf, ibfile, /):
        '!!! check read on seekback !!!'
        addr_or_None = sf.read_or_skip(ibfile, skip_only=True)
        return None
#end-class SeekAddrReader(IReader):






r'''[[[
[[[
NamedDependentTupleReader
NamedTupleReader
    see: seed.helper.mk_pairs::bmk_pairs,pairs5api_,ListOrderedItems
    see: seed.helper.mk_pairs::bmk_triples,triples5api_





from seed.helper.mk_pairs import bmk_pairs, bmk_triples, show_ordered_pairs_as_bmk_pairs, show_ordered_triples_as_bmk_triples#, bmk_OrderedDict, show_ordered_pairs_as_bmk_OrderedDict, show_ordered_dict_as_bmk_OrderedDict, cased_bmk

from seed.helper.mk_pairs import ListOrderedItems, ListOrderedItems__replace_then_move_to_end, ListSortedItems
    #__module__, __qualname__ need special treat... ==> see: seed.types.MakeDict

from seed.helper.mk_pairs import pairs5api_, pairs5api__zdefault_
from seed.helper.mk_pairs import pairs5api__raise, pairs5api__Nothing_, pairs5api__None

from seed.helper.mk_pairs import triples5api_, triples5api__zdefault_
from seed.helper.mk_pairs import triples5api__raise, triples5api__Nothing_, triples5api__None





]]]
]]]'''#'''






from nn_ns.codec.DecodeUtils import CheckError, StreamError, StreamEOFError, SeekError, ReadError, ReadError__NamedDependentTupleReader, ReadError__SeekAddrReader
from nn_ns.codec.DecodeUtils import IDecoder, IReader

from nn_ns.codec.DecodeUtils import apply_decoder, apply_reader, try_apply_decoder, try_apply_reader

from nn_ns.codec.DecodeUtils import read_bytes, skip_bytes, checked_seek, get_size_of_ibfile, size5or_size_reader__, uint5or_uint_reader__, uint_or2uint_reader_

from nn_ns.codec.DecodeUtils import check__int_or_int_reader, int5or_int_reader__, int_or2int_reader_, offset5or_offset_reader__, offset_or2offset_reader_

from nn_ns.codec.DecodeUtils import echo_decoder, uintLE_decoder, uintBE_decoder

from nn_ns.codec.DecodeUtils import StrDecoder, ascii_decoder, u8_decoder, gb_decoder

from nn_ns.codec.DecodeUtils import uint32LE_reader, uint64LE_reader

from nn_ns.codec.DecodeUtils import BytesReader, ConstantInOutReader, mk_ConstantTargetReader, mk_ConstantBytesMatcher, UntilEndValueBytesReader

from nn_ns.codec.DecodeUtils import tell_addr_reader, mk_AddrAssertionReader, eof_addr_reader
from nn_ns.codec.DecodeUtils import OffsetReader, AddrReader, SeekAddrReader

from nn_ns.codec.DecodeUtils import ArrayReader, TupleReader, DependentPairReader, NamedTupleReader, NamedDependentTupleReader, ipop_and_drop4list, UntilEndValueArrayReader, UntilReadEndValueArrayReader #!!! NOTE:NamedTupleReader/NamedDependentTupleReader read result NamedTuple, using 『NamedTuple.as_getter4named_tuple()』to access attr !!!

from nn_ns.codec.DecodeUtils import FallbackReader, SkipReader, FurtherTransformReader, AssertionReader

from nn_ns.codec.DecodeUtils import AddrDereferenceReader, AddrSizedParamReader, AddrSizedParamArrayReader, ArrayTranformReader


from nn_ns.codec.DecodeUtils import *
