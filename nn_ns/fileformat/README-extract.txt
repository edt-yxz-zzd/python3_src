
e ../../python3_src/nn_ns/fileformat/README-extract.txt


sqlite3:see:
    view ../../python3_src/seed/for_libs/for_sqlite3.py
    view ../../python3_src/nn_ns/fileformat/sqlite3_dump_cmd.py
    view script/英语词霸囗.py
    view script/汉语字典囗.py
    view script/汉语辞海囗.py
    #view ../../python3_src/nn_ns/app/sqlite3_dump_.py


欧路词典:*.eudb:
  view script/欧路词典囗.py
      试读囗囗假设简介字节数地址固定囗
          _mk_reader5addr4introduction
      试读囗囗定位关键位置全过程囗自动化囗
          _mk_reader5many_addr

  view script/欧路词典囗现代汉语词典.py
  view script/欧路词典囗计算机词汇.py
  view script/欧路词典囗清理超文本标记.py
  view script/欧路词典囗.py.尝试修复-汉语大辞典.txt
  view script/欧路词典囗*.py

[[[
工具:
header:
  view ../../python3_src/nn_ns/bin/find_zlib_objs_in_file.py
  view ../../python3_src/nn_ns/fileformat/some-file-headers.txt

py-std-library:
  import zlib, gzip, bz2, lzma
  import zipfile, tarfile
  zipfile.is_zipfile
  tarfile.is_tarfile

hexdump
  du -h /xxx/...
  dddM

  du -b /xxx/...
  ddddddd

  printf '0x%X\n' $[0x10000+16*5]
  0x10050

  hexdump <ipath> -C -n <size> -s <addr>
  hexdump /xxx/...  -C -n 0x100 -s 0x0

search_bytes_in_file
  search_bytes_in_file -i '/xxx/...'  --format4show_address $'{0}=0x{0:X}\n'    '78 9C'


sqlite3:
  py_adhoc_call   seed.for_libs.for_sqlite3   @sqlite3_dump_meta_ :/sdcard/hugh.android/GHY.DAT


py-decoder/reader:
from seed.io.with4seekback import with4seekback__on_exit, with4seekback__on_err, with4seekback__on_no_err
#[
from nn_ns.codec.DecodeUtils import CheckError, StreamError, StreamEOFError, SeekError
from nn_ns.codec.DecodeUtils import IDecoder, IReader

from nn_ns.codec.DecodeUtils import apply_decoder, apply_reader, try_apply_decoder, try_apply_reader


from nn_ns.codec.DecodeUtils import read_bytes, skip_bytes, checked_seek, get_size_of_ibfile, size5or_size_reader__, uint5or_uint_reader__, uint_or2uint_reader_

from nn_ns.codec.DecodeUtils import echo_decoder, uintLE_decoder, uintBE_decoder

from nn_ns.codec.DecodeUtils import StrDecoder, ascii_decoder, u8_decoder, gb_decoder

from nn_ns.codec.DecodeUtils import uint32LE_reader, uint64LE_reader

from nn_ns.codec.DecodeUtils import BytesReader, ConstantInOutReader, mk_ConstantTargetReader, mk_ConstantBytesMatcher, UntilEndValueBytesReader

from nn_ns.codec.DecodeUtils import tell_addr_reader, mk_AddrAssertionReader, eof_addr_reader
from nn_ns.codec.DecodeUtils import OffsetReader, AddrReader, SeekAddrReader

from nn_ns.codec.DecodeUtils import ArrayReader, TupleReader, DependentPairReader, NamedTupleReader, NamedDependentTupleReader, ipop_and_drop4list, UntilEndValueArrayReader, UntilReadEndValueArrayReader #!!! NOTE:NamedTupleReader/NamedDependentTupleReader read result NamedTuple, using 『NamedTuple.as_getter4named_tuple()』to access attr !!!

from nn_ns.codec.DecodeUtils import FallbackReader, SkipReader, FurtherTransformReader, AssertionReader

from nn_ns.codec.DecodeUtils import AddrDereferenceReader, AddrSizedParamReader, AddrSizedParamArrayReader, ArrayTranformReader
#]


]]]
