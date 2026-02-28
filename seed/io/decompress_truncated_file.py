#__all__:goto
#zipfile可能无效:???zip.table at tail???
r'''[[[
e ../../python3_src/seed/io/decompress_truncated_file.py

seed.io.decompress_truncated_file
py -m nn_ns.app.debug_cmd   seed.io.decompress_truncated_file -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.io.decompress_truncated_file:__doc__ -ht # -ff -df
#######

[[
  +Data Compression and Archiving
    zlib — Compression compatible with gzip
    gzip — Support for gzip files
    bz2 — Support for bzip2 compression
    lzma — Compression using the LZMA algorithm
    zipfile — Work with ZIP archives
    tarfile — Read and write tar archive files

]]


[[
prepare4doctest:
===
cd /sdcard/0my_files/tmp/for-doctest
echo -n 123999 >> 123999.txt

===
tar -cJvf 123999.txt.txz 123999.txt
hexdump -C 123999.txt
hexdump -C 123999.txt.txz

bs8tarfile_123999 = Path('/sdcard/0my_files/tmp/for-doctest/123999.txt.txz').read_bytes()
hexstr8tarfile_123999 = bs8tarfile_123999.hex(':', 4).upper()


===
文件管理器:手动压缩:
    142B
bs8zipfile_123999 = Path('/sdcard/0my_files/tmp/for-doctest/123999.zip').read_bytes()
hexstr8zipfile_123999 = bs8zipfile_123999.hex(':', 4).upper()

===
7z a -tzip  123999.txt.-7z-.zip 123999.txt
    160B
bs8_7z_zipfile_123999 = Path('/sdcard/0my_files/tmp/for-doctest/123999.txt.-7z-.zip').read_bytes()
hexstr8_7z_zipfile_123999 = bs8_7z_zipfile_123999.hex(':', 4).upper()



===
lzma -k -z -c 123999.txt > 123999.txt.lzma
    28B
bs8lzma_123999 = Path('/sdcard/0my_files/tmp/for-doctest/123999.txt.lzma').read_bytes()
hexstr8lzma_123999 = bs8lzma_123999.hex(':', 4).upper()


===
bzip2 -k -z -c 123999.txt > 123999.txt.bz2
    40B
bs8bz2_123999 = Path('/sdcard/0my_files/tmp/for-doctest/123999.txt.bz2').read_bytes()
hexstr8bz2_123999 = bs8bz2_123999.hex(':', 4).upper()

===
gzip -k -c 123999.txt > 123999.txt.gz
    37B
bs8gzip_123999 = Path('/sdcard/0my_files/tmp/for-doctest/123999.txt.gz').read_bytes()
hexstr8gzip_123999 = bs8gzip_123999.hex(':', 4).upper()


===
bs8zlib_123999 = zlib.compress(b'123999')
    14B
hexstr8zlib_123999 = bs8zlib_123999.hex(':', 4).upper()




===
>>> hexstr8tarfile_123999 = 'FD377A58:5A000004:E6D6B446:04C08401:80502101:16000000:00000000:ADC3F6EE:E027FF00:7C5D0018:8C82B74B:FC22F870:C154AB60:29B2A5B3:D8763AC0:81741E3D:5C6BE654:12C333A9:BCFC7DCA:6AC479A6:E5DAE694:D8B1A881:9A14841F:9E65301F:9602C5CA:F2ABA775:76226517:B4064127:DD763779:02E86AC7:14CE21E2:10DDA602:5984E064:B7146290:44545835:84B702EC:8D6A0B00:769DF877:F1E32DCB:5476C49C:FEF70000:701B02BF:14E4BB52:0001A001:80500000:0874CC66:B1C467FB:02000000:0004595A'
>>> hexstr8zipfile_123999 = '504B:03041400:08080800:8F65345C:00000000:00000000:00000000:0A000000:31323339:39392E74:78743334:32B6B4B4:0400504B:0708AF12:A03D0800:00000600:0000504B:01021400:14000808:08008F65:345CAF12:A03D0800:00000600:00000A00:00000000:00000000:00000000:00000000:31323339:39392E74:7874504B:05060000:00000100:01003800:00004000:00000000'
>>> hexstr8_7z_zipfile_123999 = '504B0304:0A030000:0000D260:345CAF12:A03D0600:00000600:00000A00:00003132:33393939:2E747874:31323339:3939504B:01023F03:0A030000:0000D260:345CAF12:A03D0600:00000600:00000A00:24000000:00000000:2080B081:00000000:31323339:39392E74:78740A00:20000000:00000100:180000AE:742BC289:DC0100AE:742BC289:DC0100AE:742BC289:DC01504B:05060000:00000100:01005C00:00002E00:00000000'
>>> hexstr8lzma_123999 = '5D000080:00FFFFFF:FFFFFFFF:FF00188C:82B74C05:9345FFFF:FA73A000'
>>> hexstr8bz2_123999 = '425A6839:31415926:5359D853:36950000:00080038:20200030:CD3418C8:E08F1772:45385090:D8533695'
>>> hexstr8gzip_123999 = '1F:8B08084C:FF6E6900:03313233:3939392E:74787400:333432B6:B4B40400:AF12A03D:06000000'
>>> hexstr8zlib_123999 = '789C:333432B6:B4B40400:04480142'


===
>>> bs8tarfile_123999 = bytes.fromhex(hexstr8tarfile_123999.replace(':', ''))
>>> bs8zipfile_123999 = bytes.fromhex(hexstr8zipfile_123999.replace(':', ''))
>>> bs8_7z_zipfile_123999 = bytes.fromhex(hexstr8_7z_zipfile_123999.replace(':', ''))
>>> bs8lzma_123999 = bytes.fromhex(hexstr8lzma_123999.replace(':', ''))
>>> bs8bz2_123999 = bytes.fromhex(hexstr8bz2_123999.replace(':', ''))
>>> bs8gzip_123999 = bytes.fromhex(hexstr8gzip_123999.replace(':', ''))
>>> bs8zlib_123999 = bytes.fromhex(hexstr8zlib_123999.replace(':', ''))

>>> len(bs8tarfile_123999)
196
>>> len(bs8zipfile_123999)
142
>>> len(bs8_7z_zipfile_123999)
160
>>> len(bs8lzma_123999)
28
>>> len(bs8bz2_123999)
40
>>> len(bs8gzip_123999)
37
>>> len(bs8zlib_123999)
14



===
补偿:[[
>>> bs8tarfile_123999
b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x04\xc0\x84\x01\x80P!\x01\x16\x00\x00\x00\x00\x00\x00\x00\xad\xc3\xf6\xee\xe0\'\xff\x00|]\x00\x18\x8c\x82\xb7K\xfc"\xf8p\xc1T\xab`)\xb2\xa5\xb3\xd8v:\xc0\x81t\x1e=\\k\xe6T\x12\xc33\xa9\xbc\xfc}\xcaj\xc4y\xa6\xe5\xda\xe6\x94\xd8\xb1\xa8\x81\x9a\x14\x84\x1f\x9ee0\x1f\x96\x02\xc5\xca\xf2\xab\xa7uv"e\x17\xb4\x06A\'\xddv7y\x02\xe8j\xc7\x14\xce!\xe2\x10\xdd\xa6\x02Y\x84\xe0d\xb7\x14b\x90DTX5\x84\xb7\x02\xec\x8dj\x0b\x00v\x9d\xf8w\xf1\xe3-\xcbTv\xc4\x9c\xfe\xf7\x00\x00p\x1b\x02\xbf\x14\xe4\xbbR\x00\x01\xa0\x01\x80P\x00\x00\x08t\xccf\xb1\xc4g\xfb\x02\x00\x00\x00\x00\x04YZ'


>>> bs8zipfile_123999
b'PK\x03\x04\x14\x00\x08\x08\x08\x00\x8fe4\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00123999.txt342\xb6\xb4\xb4\x04\x00PK\x07\x08\xaf\x12\xa0=\x08\x00\x00\x00\x06\x00\x00\x00PK\x01\x02\x14\x00\x14\x00\x08\x08\x08\x00\x8fe4\\\xaf\x12\xa0=\x08\x00\x00\x00\x06\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00123999.txtPK\x05\x06\x00\x00\x00\x00\x01\x00\x01\x008\x00\x00\x00@\x00\x00\x00\x00\x00'



>>> bs8_7z_zipfile_123999
b'PK\x03\x04\n\x03\x00\x00\x00\x00\xd2`4\\\xaf\x12\xa0=\x06\x00\x00\x00\x06\x00\x00\x00\n\x00\x00\x00123999.txt123999PK\x01\x02?\x03\n\x03\x00\x00\x00\x00\xd2`4\\\xaf\x12\xa0=\x06\x00\x00\x00\x06\x00\x00\x00\n\x00$\x00\x00\x00\x00\x00\x00\x00 \x80\xb0\x81\x00\x00\x00\x00123999.txt\n\x00 \x00\x00\x00\x00\x00\x01\x00\x18\x00\x00\xaet+\xc2\x89\xdc\x01\x00\xaet+\xc2\x89\xdc\x01\x00\xaet+\xc2\x89\xdc\x01PK\x05\x06\x00\x00\x00\x00\x01\x00\x01\x00\\\x00\x00\x00.\x00\x00\x00\x00\x00'




>>> bs8lzma_123999
b']\x00\x00\x80\x00\xff\xff\xff\xff\xff\xff\xff\xff\x00\x18\x8c\x82\xb7L\x05\x93E\xff\xff\xfas\xa0\x00'

>>> bs8bz2_123999
b'BZh91AY&SY\xd8S6\x95\x00\x00\x00\x08\x008  \x000\xcd4\x18\xc8\xe0\x8f\x17rE8P\x90\xd8S6\x95'

>>> bs8gzip_123999
b'\x1f\x8b\x08\x08L\xffni\x00\x03123999.txt\x00342\xb6\xb4\xb4\x04\x00\xaf\x12\xa0=\x06\x00\x00\x00'

>>> bs8zlib_123999
b'x\x9c342\xb6\xb4\xb4\x04\x00\x04H\x01B'


]]


'#'; __doc__ = r'#'

#########
>>> import os, sys
>>> from seed.for_libs.for_tempfile import Path, mk_temp_dir_ctx_
>>> with mk_temp_dir_ctx_() as tmpdir:    #doctest: +SKIP
...     assert type(tmpdir) is str
...     tmpdir = Path(tmpdir)
...     assert tmpdir.exists()
...     p0 = tmpdir/'0tmp0.txt'
...     p1 = tmpdir/'0tmp0.txt.txz'
...     p0.write_bytes(b'123999')
...     assert 0 == (__:=os.system('tar -cJvf {p1!s} {p0!s}')), __#fail???why???
...     print(p1.read_bytes())





#########
>>> len(bs8tarfile_123999)
196
>>> decompress_truncated_file_('tarfile', 'bytes', bs8tarfile_123999)
b'123999'
>>> decompress_truncated_file_('tarfile', 'bytes', bs8tarfile_123999[:120])
Traceback (most recent call last):
    ...
tarfile.ReadError: file could not be opened successfully:
- method gz: ReadError('not a gzip file')
- method bz2: ReadError('not a bzip2 file')
- method xz: ReadError('not an lzma file')
- method tar: ReadError('truncated header')
>>> decompress_truncated_file_('tarfile', 'bytes', bs8tarfile_123999[:121])
b''
>>> decompress_truncated_file_('tarfile', 'bytes', bs8tarfile_123999[:122])
b''
>>> decompress_truncated_file_('tarfile', 'bytes', bs8tarfile_123999[:123])
b'123999'



#########
>>> len(bs8zipfile_123999)
142
>>> decompress_truncated_file_('zipfile', 'bytes', bs8zipfile_123999)
b'123999'
>>> decompress_truncated_file_('zipfile', 'bytes', bs8zipfile_123999[:142])
b'123999'
>>> decompress_truncated_file_('zipfile', 'bytes', bs8zipfile_123999[:141]) #zf = zipfile.ZipFile(ipath_or_ibfile) # ???zip.table at tail???
Traceback (most recent call last):
    ...
zipfile.BadZipFile: File is not a zip file



#########
>>> len(bs8_7z_zipfile_123999)
160
>>> decompress_truncated_file_('zipfile', 'bytes', bs8_7z_zipfile_123999)
b'123999'
>>> decompress_truncated_file_('zipfile', 'bytes', bs8_7z_zipfile_123999[:160])
b'123999'
>>> decompress_truncated_file_('zipfile', 'bytes', bs8_7z_zipfile_123999[:159])
Traceback (most recent call last):
    ...
zipfile.BadZipFile: File is not a zip file



#########
>>> len(bs8lzma_123999)
28
>>> decompress_truncated_file_('lzma', 'bytes', bs8lzma_123999)
b'123999'
>>> decompress_truncated_file_('lzma', 'bytes', bs8lzma_123999[:17])
b''
>>> decompress_truncated_file_('lzma', 'bytes', bs8lzma_123999[:18])
b'1'
>>> decompress_truncated_file_('lzma', 'bytes', bs8lzma_123999[:19])
b'1'
>>> decompress_truncated_file_('lzma', 'bytes', bs8lzma_123999[:20])
b'12'
>>> decompress_truncated_file_('lzma', 'bytes', bs8lzma_123999[:21])
b'123'
>>> decompress_truncated_file_('lzma', 'bytes', bs8lzma_123999[:22])
b'1239'
>>> decompress_truncated_file_('lzma', 'bytes', bs8lzma_123999[:23])
b'123999'

#########
>>> len(bs8bz2_123999)
40
>>> decompress_truncated_file_('bz2', 'bytes', bs8bz2_123999)
b'123999'
>>> decompress_truncated_file_('bz2', 'bytes', bs8bz2_123999[:29])
b''
>>> decompress_truncated_file_('bz2', 'bytes', bs8bz2_123999[:30])
b'123999'

#########
>>> len(bs8gzip_123999)
37
>>> decompress_truncated_file_('gzip', 'bytes', bs8gzip_123999)
b'123999'
>>> decompress_truncated_file_('gzip', 'bytes', bs8gzip_123999[:22])
b''
>>> decompress_truncated_file_('gzip', 'bytes', bs8gzip_123999[:23])
b'1'
>>> decompress_truncated_file_('gzip', 'bytes', bs8gzip_123999[:24])
b'12'
>>> decompress_truncated_file_('gzip', 'bytes', bs8gzip_123999[:25])
b'123'
>>> decompress_truncated_file_('gzip', 'bytes', bs8gzip_123999[:26])
b'1239'
>>> decompress_truncated_file_('gzip', 'bytes', bs8gzip_123999[:27])
b'12399'
>>> decompress_truncated_file_('gzip', 'bytes', bs8gzip_123999[:28])
b'123999'

#########
>>> len(bs8zlib_123999)
14
>>> decompress_truncated_file_('zlib', 'bytes', bs8zlib_123999)
b'123999'
>>> decompress_truncated_file_('zlib', 'bytes', bs8zlib_123999[:3])
b''
>>> decompress_truncated_file_('zlib', 'bytes', bs8zlib_123999[:4])
b'1'
>>> decompress_truncated_file_('zlib', 'bytes', bs8zlib_123999[:5])
b'12'
>>> decompress_truncated_file_('zlib', 'bytes', bs8zlib_123999[:6])
b'123'
>>> decompress_truncated_file_('zlib', 'bytes', bs8zlib_123999[:7])
b'1239'
>>> decompress_truncated_file_('zlib', 'bytes', bs8zlib_123999[:8])
b'12399'
>>> decompress_truncated_file_('zlib', 'bytes', bs8zlib_123999[:9])
b'123999'


#########
>>> decompress_truncated_file_('zlib', 'bytes', bs8zlib_123999[:9], max_length=3)
b'123'



>>>



py_adhoc_call   seed.io.decompress_truncated_file   @count_uncompression_bytes4truncated_compression_file_ :bz2 :ipath :'../../python3_src/nn_ns/math_nn/numbers/偏移值二爻冃靶值讠最小显链长.le7320000.le7322932[add31.bits-中断].bz2'
    =>:1830733


]]]'''#'''
__all__ = r'''
semi_open4truncated_compression_file_
    iter_uncompression_bytess4truncated_compression_file_
        count_uncompression_bytes4truncated_compression_file_
        decompress_truncated_file_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge
import zlib#gzip
import gzip
import bz2
import lzma#xz
import zipfile
import tarfile
from seed.io.open8ibfile__3to1_ import open8ibfile__3to1_, open8ibfile__3to2_, open8ibfile__2to1_

#.from seed.tiny_.null_dev import null_context, null_context5result_
#.from seed.for_libs.for_contextlib import null_context, MovableContextManager, GroupContextManager
from seed.types.ctx.IGroupContextManager import InnermostContext
from contextlib import nullcontext as mk_null_context5result_
___end_mark_of_excluded_global_names__0___ = ...
assert OSError is IOError
_all_ErrorTypes = (IOError, zlib.error, gzip.BadGzipFile, EOFError, lzma.LZMAError, zipfile.BadZipFile, tarfile.TarError)
    #bz2:no error? EOFError


def semi_open4truncated_compression_file_(file_type, input_case, ipath_or_ibfile_or_bytes, /):
    '-> (Either ctxed_ibfile8uncompression_bytes (decompressor, ibfile8compression_bytes))'
    (input_case, ipath_or_ibfile) = open8ibfile__3to2_(input_case, ipath_or_ibfile_or_bytes)
    ibfile_vs_decompressor = False
    match file_type:
        case 'gzip':
            ibfile8uncompression_bytes = gzip.open(ipath_or_ibfile)
            ctx = mk_null_context5result_(None)
        case 'zipfile':
            (zf, ibfile8uncompression_bytes) = _open4zipfile__singleton_(ipath_or_ibfile)
            ctx = zf
        case 'tarfile':
            (tf, ibfile8uncompression_bytes) = _open4tarfile__singleton_(input_case, ipath_or_ibfile)
            ctx = tf
        case 'zlib' | 'bz2' | 'lzma':
            ibfile_vs_decompressor = True
        case _:
            raise Exception('unknown file_type:', file_type)
    if not ibfile_vs_decompressor:
        ctxed_ibfile8uncompression_bytes = InnermostContext([ctx, ibfile8uncompression_bytes])
        return (ibfile_vs_decompressor, ctxed_ibfile8uncompression_bytes)

    ibfile8compression_bytes = open8ibfile__2to1_(input_case, ipath_or_ibfile)
    match file_type:
        case 'zlib':
            decompressor = zlib.decompressobj()
        case 'bz2':
            #ibfile8uncompression_bytes = bz2.open(ipath_or_ibfile)
            decompressor = bz2.BZ2Decompressor()
        case 'lzma':
            #ibfile8uncompression_bytes = lzma.open(ipath_or_ibfile)
            decompressor = lzma.LZMADecompressor()
        case _:
            raise 000
            raise Exception('unknown file_type:', file_type)
        #case
    decompressor
    return (ibfile_vs_decompressor, (decompressor, ibfile8compression_bytes))
def _open4zipfile__singleton_(ipath_or_ibfile, /):
    zf = zipfile.ZipFile(ipath_or_ibfile)
        # ^zipfile.BadZipFile: File is not a zip file
        # ???zip.table at tail???
    root = zipfile.Path(zf)
    it = root.iterdir()
    for ipath4fst_child in it:
        break
    else:
        raise Exception('no file in zipfile')
    if 0:
        for _ in it:
            raise Exception('more than one file in zipfile')
    try:
        m = next(it, None)
    except _all_ErrorTypes:
        pass#ok:truncated
    else:
        if not m is None:
            raise Exception('more than one file in zipfile')
        pass

    if not ipath4fst_child.is_file(): raise Exception('not single file in zipfile')
    ipath4the_only_child = ipath4fst_child
    ibfile8uncompression_bytes = ipath4the_only_child.open('rb')
    return (zf, ibfile8uncompression_bytes)
def _open4tarfile__singleton_(input_case, ipath_or_ibfile, /):
    #tarfile.is_tarfile(ipath_or_ibfile)
    ibfile8compression_bytes = open8ibfile__2to1_(input_case, ipath_or_ibfile)
    tf = tarfile.open(fileobj=ibfile8compression_bytes)
        # ^tarfile.ReadError: file could not be opened successfully:
    #may_fst_tarinfo8member = tf.next()
    it = iter(tf) #__iter__():tarinfo = self.next()
        # Iter member/TarInfo
        #
    for fst_child in it:
        break
    else:
        raise Exception('no file in tarfile')
    if 0:
        for _ in it:
            raise Exception('more than one file in tarfile')
    try:
        m = next(it, None)
    except _all_ErrorTypes:
        # J/bz2 => ^EOFError: Compressed file ended before the end-of-stream marker was reached
        pass#ok:truncated
    else:
        if not m is None:
            raise Exception('more than one file in tarfile')
        pass
    if not fst_child.isfile(): raise Exception('not single file in tarfile')
    the_only_child = fst_child
    ibfile8uncompression_bytes = tf.extractfile(the_only_child)
    return (tf, ibfile8uncompression_bytes)





def iter_uncompression_bytess4truncated_compression_file_(file_type, input_case, ipath_or_ibfile_or_bytes, /):
    '-> Iter bytes{decompressed}'
    either = semi_open4truncated_compression_file_(file_type, input_case, ipath_or_ibfile_or_bytes)
    match either:
        case (False, ctxed_ibfile8uncompression_bytes):
            it = _1__iter_uncompression_bytess4truncated_compression_file_(ctxed_ibfile8uncompression_bytes)
        case (True, (decompressor, ibfile8compression_bytes)):
            it = _2__iter_uncompression_bytess4truncated_compression_file_(decompressor, ibfile8compression_bytes)
        case _:
            raise 000
        #case
    it
    return it

def _1__iter_uncompression_bytess4truncated_compression_file_(ctxed_ibfile8uncompression_bytes, /):
    with ctxed_ibfile8uncompression_bytes as ibfile:
        ibfile.seek(0)
        done = False
        sz = 0
        for sz4blk in (2**15, 2**10, 2**5, 1):
            if done:break#for_loop
            while 1:
                addr = ibfile.tell()
                try:
                    bs = ibfile.read(sz4blk)
                except _all_ErrorTypes:
                    ibfile.seek(addr)
                    break#while_loop
                if not bs:
                    done = True
                    break#while_loop
                sz += len(bs)
                777;yield bs
            #end-while_loop
            pass
        #end-for_loop
        sz
    sz
    return sz

def _2__iter_uncompression_bytess4truncated_compression_file_(decompressor, ibfile8compression_bytes, /):
    ibfile = ibfile8compression_bytes
    ibfile.seek(0)
    sz4blk = 2**20
    sz = 0
    while 1:
        bs = ibfile.read(sz4blk)
        if not bs:
            break
        bs = decompressor.decompress(bs)
        sz += len(bs)
        777;yield bs
    #end-while_loop
    sz
    if hasattr(decompressor, 'flush'):
        bs = decompressor.flush()
        if bs:
            sz += len(bs)
            777;yield bs
    sz
    return sz



def count_uncompression_bytes4truncated_compression_file_(file_type, input_case, ipath_or_ibfile_or_bytes, /):
    '-> num_bytes'
    bss = iter_uncompression_bytess4truncated_compression_file_(file_type, input_case, ipath_or_ibfile_or_bytes)
    num_bytes = sum(map(len, bss))
    return num_bytes
def decompress_truncated_file_(file_type, input_case, ipath_or_ibfile_or_bytes, /, *, max_length=-1):
    '-> bytes'
    check_int_ge(-1, max_length)
    if max_length == 0:
        return b''
    if max_length > 0:
        def iter_bss_(bss, /):
            sz = max_length
            for bs in bss:
                if sz <= len(bs):
                    yield bs[:sz]
                    break
                sz -= len(bs)
                yield bs
    bss = iter_uncompression_bytess4truncated_compression_file_(file_type, input_case, ipath_or_ibfile_or_bytes)
    if max_length > 0:
        bss = iter_bss_(bss)
    bss
    bs = b''.join(bss)
    return bs

__all__
from seed.io.decompress_truncated_file import semi_open4truncated_compression_file_, iter_uncompression_bytess4truncated_compression_file_
from seed.io.decompress_truncated_file import count_uncompression_bytes4truncated_compression_file_, decompress_truncated_file_
from seed.io.decompress_truncated_file import *
