#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/bin/find_zlib_objs_in_file.py
view ../../python3_src/py_stdlib_api.txt
  zlib_66_headers:goto
e ../../python3_src/nn_ns/fileformat/some-file-headers.txt


nn_ns.bin.find_zlib_objs_in_file
py -m   nn_ns.bin.find_zlib_objs_in_file
py -m nn_ns.app.debug_cmd   nn_ns.bin.find_zlib_objs_in_file -x
py -m nn_ns.app.doctest_cmd nn_ns.bin.find_zlib_objs_in_file:__doc__ -ff
py -m nn_ns.app.doctest_cmd nn_ns.bin.find_zlib_objs_in_file!



计算机词汇
py_adhoc_call   nn_ns.bin.find_zlib_objs_in_file   ,hex.iter_find_zlib_objs_in_file__ipath_   :/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1922908499.eudb
0x560
0x27ef
0x4acf
0x6e2c


汉语辞海
search_bytes_in_file -i '/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf' --format4show_address $'{0}=0x{0:X}\n'    '78 9C'
  [[
213603=0x34263
319065=0x4DE59
337347=0x525C3
339356=0x52D9C
... 许多
  ]]
py_adhoc_call   nn_ns.bin.find_zlib_objs_in_file   ,hex.iter_find_zlib_objs_in_file__ipath_   :'/sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai/assets/fonts/scihai.ttf'
    无






>>> from nn_ns.bin.find_zlib_objs_in_file import iter_find_zlib_objs_in_file__ipath_, iter_find_zlib_objs_in_file_, buggy_header4zlib
>>> from nn_ns.bin.find_zlib_objs_in_file import zlib_66_headers, zlib_66_headers__str, uints5fst_bytes5zlib_headers
>>> import io
>>> import zlib
>>> kw = dict(using_789C_header_only=True, detect_header_only=False, output_addr_only=True, overlap=False)
>>> ok1 = zlib.compress(b'')
>>> ok1[:2] == buggy_header4zlib
True
>>> len(ok1)
8
>>> bs = buggy_header4zlib+buggy_header4zlib+ok1+ok1+buggy_header4zlib+buggy_header4zlib+ok1
>>> len(bs)
32
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), **kw)]
[4, 12, 24]
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), may_negativeable_end_location=25, **kw)]
[4, 12, 24]
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), may_negativeable_end_location=24, **kw)]
[4, 12]
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), may_negativeable_end_location=-7, **kw)]
[4, 12, 24]
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), may_negativeable_end_location=-8, **kw)]
[4, 12]


>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), may_negativeable_begin_location=25, **kw)]
[]
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), may_negativeable_begin_location=24, **kw)]
[24]
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), may_negativeable_begin_location=-7, **kw)]
[]
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), may_negativeable_begin_location=-8, **kw)]
[24]



>>> ok2 = zlib.compress(b'', 2)
>>> ok2[:2] == buggy_header4zlib
False
>>> len(ok2)
8
>>> bs = buggy_header4zlib+buggy_header4zlib+ok2+ok2+buggy_header4zlib+buggy_header4zlib+ok2
>>> len(bs)
32
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), **kw)]
[]
>>> kw['using_789C_header_only'] = False
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), **kw)]
[4, 12, 24]
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), may_negativeable_end_location=25, **kw)]
[4, 12, 24]
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), may_negativeable_end_location=24, **kw)]
[4, 12]
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), may_negativeable_end_location=-7, **kw)]
[4, 12, 24]
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), may_negativeable_end_location=-8, **kw)]
[4, 12]


>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), may_negativeable_begin_location=25, **kw)]
[]
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), may_negativeable_begin_location=24, **kw)]
[24]
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), may_negativeable_begin_location=-7, **kw)]
[]
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), may_negativeable_begin_location=-8, **kw)]
[24]

>>> kw['output_addr_only'] = False
>>> [*iter_find_zlib_objs_in_file_(io.BytesIO(bs), **kw)]
[(4, 60, b'x^', 8), (12, 60, b'x^', 8), (24, 60, b'x^', 8)]
>>> len(ok2) #imay_sz==8
8
>>> ok2[:2] #header
b'x^'
>>> zlib_66_headers.index(ok2[:2]) #header_idx
60

>>> import bz2
>>> ok3 = bz2.compress(b'')
>>> len(ok3)
14
>>> len(header4bz2)
3
>>> bs = header4bz2+header4bz2+ok3+ok3+header4bz2+header4bz2+ok3
>>> kw = dict(detect_header_only=True, output_addr_only=True, overlap=False)
>>> [*iter_find_bz2_objs_in_file_(io.BytesIO(bs), **kw)]
[0, 3, 6, 20, 34, 37, 40]
>>> kw['detect_header_only'] = False
>>> [*iter_find_bz2_objs_in_file_(io.BytesIO(bs), **kw)]
[6, 20, 40]
>>> kw['output_addr_only'] = False
>>> [*iter_find_bz2_objs_in_file_(io.BytesIO(bs), **kw)]
[(6, 0, b'BZh', 14), (20, 0, b'BZh', 14), (40, 0, b'BZh', 14)]
>>> import lzma

#]]]'''
__all__ = r'''
    iter_find_xxx_objs_in_file_
        iter_find_xxx_obj_headers_in_file_
        xxx_obj_recognizer_5incremental_decompressor_factory
            zlib_obj_recognizer_
            bz2_obj_recognizer_
            lzma_obj_recognizer_
                Error4zlib
                Error4bz2
                Error4lzma
                Error4gzip

    iter_find_zlib_objs_in_file__ipath_
        iter_find_zlib_objs_in_file_
            buggy_header4zlib
            zlib_66_headers
                zlib_66_headers__str
                uints5fst_bytes5zlib_headers

    iter_find_bz2_objs_in_file__ipath_
            iter_find_bz2_objs_in_file_
                header4bz2
                bz2_obj_headers

    header4SQLite
        header4sqlite3
    header4zip
        header4zipfile
    is_zipfile
        is_tarfile
    header4gzip
    header4bz2
    buggy_header4lzma


    mk__xxx_obj_headers__sz_eq
    mk__xxx_obj_headers__one_more_byte















    max4bk_sz
        init4bk_sz


    zlib_66_header_hex_ls
    uints5snd_bytes5zlib_headers
    common_uints5fst_bytes_snd_bytes5zlib_headers
    zlib_66_headers__pattern
    zlib_66_headers__regex
'''.split()#'''
__all__

import re
from seed.tiny import curry1, check_imay, fst, print_err
from seed.io.find__naive import iter_find_bytes__naive_, list_find_bytes__naive_
from seed.io.get_size_of_ibfile import get_size_of_ibfile, get_size_of_ibfile_ex, explain_may_negativeable_end_locations_of_ibfile_ex, explain_negativeable_location_of_ibfile_ex, explain_may_negativeable_location_rng_of_ibfile_ex#; #may have [len(ibfile) < end_location]
from seed.io.with4seekback import with4seekback__on_exit, with4seekback__on_err, with4seekback__on_no_err








import zlib
import bz2
import lzma
import gzip
from tarfile import is_tarfile
from zipfile import is_zipfile

_mk4zlib = zlib.decompressobj().copy
Error4zlib = zlib.error
if 0:_mk4bz2 = bz2.BZ2Decompressor().copy
    #AttributeError: '_bz2.BZ2Decompressor' object has no attribute 'copy'
_mk4bz2 = bz2.BZ2Decompressor
Error4bz2 = (OSError,ValueError)#bz2.error
    #OSError: Invalid data stream
    #ValueError: Compressed data ended before the end-of-stream marker was reached
if 0:_mk4lzma = lzma.LZMADecompressor().copy
    #AttributeError: '_lzma.LZMADecompressor' object has no attribute 'copy'
_mk4lzma = lzma.LZMADecompressor
Error4lzma = lzma.LZMAError
#_mk4gzip = gzip.GzipFile(...).copy
Error4gzip = gzip.BadGzipFile



#hexdump  /sdcard/0my_files/unzip/apk/dictionary/han_yu_ci_hai-scihai-ttf/cihai.dat   -C  -n 0x200 -s 0x0
header4SQLite = b'SQLite'
header4sqlite3 = b'SQLite format 3\0'
#00000000  53 51 4c 69 74 65 20 66  6f 72 6d 61 74 20 33 00  |SQLite format 3.|
#00000010  04 00 01 01 00 40 20 20  00 05 fd 97 00 00 00 00  |.....@  ........|
header4zip = b'PK' # ??? ++ b'\x03\x04'
#00000000  50 4b 03 04 14 00 00 00  08 00 74 bd f7 42 ef d3  |PK........t..B..|
header4zipfile = b'PK\3\4'
    #from py-src:zipfile.py:
    #  stringFileHeader = b"PK\003\004"
is_zipfile
is_tarfile

header4gzip = b'\x1F\x8B' # <<== src code:gzip.py
header4bz2 = b'BZh' # ++ [1-9]
buggy_header4lzma = b'\xFD7zXZ\x00'
    #FORMAT_XZ=1
    #buggy but useful
    #
buggy_header4zlib = b'\x78\x9C'
    #level=-1|+6
    #buggy but useful
    #
max4bk_sz = 0x4000 #16K
init4bk_sz = 0x10 #16
if 1:
    may_negativeable_begin_location=None
    may_negativeable_end_location=None
    overlap=True
    output_addr_only=False
    detect_header_only=False
    using_789C_header_only=False
def iter_find_zlib_objs_in_file__ipath_(ipath, /, *, using_789C_header_only=using_789C_header_only, detect_header_only=detect_header_only, output_addr_only=output_addr_only, overlap=overlap, may_negativeable_begin_location=may_negativeable_begin_location, may_negativeable_end_location=may_negativeable_end_location):
    with open(ipath, 'rb') as ibfile:
        yield from iter_find_zlib_objs_in_file_(ibfile, using_789C_header_only=using_789C_header_only, detect_header_only=detect_header_only, output_addr_only=output_addr_only, overlap=overlap, may_negativeable_begin_location=may_negativeable_begin_location, may_negativeable_end_location=may_negativeable_end_location)




def iter_find_bz2_objs_in_file__ipath_(ipath, /, *, detect_header_only=detect_header_only, output_addr_only=output_addr_only, overlap=overlap, may_negativeable_begin_location=may_negativeable_begin_location, may_negativeable_end_location=may_negativeable_end_location):
    with open(ipath, 'rb') as ibfile:
        yield from iter_find_bz2_objs_in_file_(ibfile, detect_header_only=detect_header_only, output_addr_only=output_addr_only, overlap=overlap, may_negativeable_begin_location=may_negativeable_begin_location, may_negativeable_end_location=may_negativeable_end_location)


def iter_find_bz2_objs_in_file_(ibfile, /, *, detect_header_only=detect_header_only, output_addr_only=output_addr_only, overlap=overlap, may_negativeable_begin_location=may_negativeable_begin_location, may_negativeable_end_location=may_negativeable_end_location):
    '-> Iter (addr, header_idx, header) if detect_header_only else Iter (addr, header_idx, header, sz)'
    if detect_header_only:
        iter_find_ = iter_find_xxx_obj_headers_in_file_
    else:
        iter_find_ = curry1(iter_find_xxx_objs_in_file_, bz2_obj_recognizer_)
    iter_find_

    headers = [header4bz2]

    it = iter_find_(headers, ibfile, overlap=overlap, may_negativeable_begin_location=may_negativeable_begin_location, may_negativeable_end_location=may_negativeable_end_location)
    if output_addr_only:
        it = map(fst, it)
    return it



def iter_find_zlib_objs_in_file_(ibfile, /, *, using_789C_header_only=using_789C_header_only, detect_header_only=detect_header_only, output_addr_only=output_addr_only, overlap=overlap, may_negativeable_begin_location=may_negativeable_begin_location, may_negativeable_end_location=may_negativeable_end_location):
    '-> Iter (addr, header_idx, header) if detect_header_only else Iter (addr, header_idx, header, sz)'
    if detect_header_only:
        iter_find_ = iter_find_xxx_obj_headers_in_file_
    else:
        iter_find_ = curry1(iter_find_xxx_objs_in_file_, zlib_obj_recognizer_)
    iter_find_

    if using_789C_header_only:
        headers = [buggy_header4zlib]
    else:
        headers = zlib_66_headers
    headers

    it = iter_find_(headers, ibfile, overlap=overlap, may_negativeable_begin_location=may_negativeable_begin_location, may_negativeable_end_location=may_negativeable_end_location)
    if output_addr_only:
        it = map(fst, it)
    return it
    #len(buggy_header4zlib)
            #to_continue = addr == addr0 and len(bs5peek)==2 and bs5peek[1] in (40,50)
                    #see below:assert {40, 56} == ({*uints5fst_bytes5zlib_headers} & {*uints5snd_bytes5zlib_headers})
def xxx_obj_recognizer_5incremental_decompressor_factory(DecompressErrorType, decompressor_copy, /):
    r''' DecompressErrorType -> decompressor.copy/(()->incremental_decompressor) -> xxx_obj_recognizer_/(ibfile@addr -> imay_sz)

LZMADecompressor/BZ2Decompressor
    .decompress(sf, data)
    .eof :: bool
    .needs_input :: bool
    .unused_data :: bytes
GzipFile-whole file

zlib.decompressobj()
    .decompress(sf, data)
    .flush(sf)
    .eof :: bool
    .unconsumed_tail :: bytes
    .unused_data :: bytes
'''#'''
    def xxx_obj_recognizer_(ibfile, /):
        '-> imay_sz'
        dc = decompressor_copy()
        begin = ibfile.tell()
        bk_sz = init4bk_sz
        sz = 0
        while not dc.eof:
            bs = ibfile.read(bk_sz)
            if bk_sz < max4bk_sz:
                bk_sz <<= 1
            if not bs:
                #eof
                imay_sz = -1
                break
            try:
                dc.decompress(bs)
            except DecompressErrorType as e:
                #print_err(begin)
                #print_err(e)
                imay_sz = -1
                break
            sz += len(bs)
        else:
            _end = ibfile.tell()
            assert sz == _end-begin
            sz -= len(dc.unused_data)
            assert sz > 0
            imay_sz = sz
            #xxx:when zlib:assert len(dc.unused_data) == len(dc.unconsumed_tail), (dc.unused_data, dc.unconsumed_tail)
            #   AssertionError: (b'x\x9c\x03\x00\x00\x00\x00\x01', b'')
            #   what is .unconsumed_tail?
        return imay_sz
    return xxx_obj_recognizer_
zlib_obj_recognizer_ = xxx_obj_recognizer_5incremental_decompressor_factory(Error4zlib, _mk4zlib)
bz2_obj_recognizer_ = xxx_obj_recognizer_5incremental_decompressor_factory(Error4bz2, _mk4bz2)
lzma_obj_recognizer_ = xxx_obj_recognizer_5incremental_decompressor_factory(Error4lzma, _mk4lzma)

def iter_find_xxx_objs_in_file_(xxx_obj_recognizer_, xxx_headers, ibfile, /, *, overlap=overlap, may_negativeable_begin_location=may_negativeable_begin_location, may_negativeable_end_location=may_negativeable_end_location):
    '(ibfile@addr -> imay_sz) -> [bytes] -> ibfile -> Iter (addr, header_idx, header, sz);  ##end_location for begin_addr<zlib_obj> not end_addr<zlib_obj> : satisfy [begin_location <= begin_addr<zlib_obj> < end_location]'
    it = iter_find_xxx_obj_headers_in_file_(xxx_headers, ibfile, overlap=overlap, may_negativeable_begin_location=may_negativeable_begin_location, may_negativeable_end_location=may_negativeable_end_location)
    for (addr, header_idx, header) in it:
        with with4seekback__on_no_err(ibfile):
            ibfile.seek(addr)
            imay_sz = xxx_obj_recognizer_(ibfile)
        check_imay(imay_sz)
        if imay_sz >= 0:
            sz = imay_sz
            if sz < len(header):raise logic-err
            yield (addr, header_idx, header, sz)










def iter_find_xxx_obj_headers_in_file_(xxx_headers, ibfile, /, *, overlap=overlap, may_negativeable_begin_location=may_negativeable_begin_location, may_negativeable_end_location=may_negativeable_end_location):
    '-> Iter (addr, header_idx, header);  ##end_location for begin_addr<zlib_obj> not end_addr<zlib_obj> : satisfy [begin_location <= begin_addr<zlib_obj> < end_location]'
    the_curr_tell_location = ibfile.tell()
    (ibfile_or_sz, (begin_location, end_location)) = explain_may_negativeable_location_rng_of_ibfile_ex(ibfile, the_curr_tell_location, may_negativeable_begin_location, may_negativeable_end_location)
    if 0:
        #end_location += len(buggy_header4zlib)-1
            #all headers' len is 2!!
            #end_location := end of begin, not last of end
        #for addr in iter_find_bytes__naive_(buggy_header4zlib, ibfile, may_negativeable_begin_location=may_negativeable_begin_location, may_negativeable_end_location=end_location):
            #to_continue = addr == addr0 and len(bs5peek)==2 and bs5peek[1] in (40,50)
                    #see below:assert {40, 56} == ({*uints5fst_bytes5zlib_headers} & {*uints5snd_bytes5zlib_headers})
        000
    xxx_headers[:0] #check for xxx_headers[target_idx]
    assert len(xxx_headers)
    assert all(xxx_headers)
    max_sz = max(map(len, xxx_headers))
    assert max_sz >= 1
    last4begin = end_location-1; del end_location
    last4end = last4begin+max_sz

    #now, support overlap
    kwds = dict(overlap=overlap, target_is_bytess=True, with_target_idx=True
        #line too long for py.parser?
        , may_negativeable_begin_location=may_negativeable_begin_location, may_negativeable_end_location=last4end
        )
    it = iter_find_bytes__naive_(xxx_headers, ibfile, **kwds)
    for addr, target_idx in it:
        if last4begin < addr:break
        header_idx = target_idx
        header = xxx_headers[header_idx]
        yield (addr, header_idx, header)


def _peek(ibfile, sz4peek, /):
    with with4seekback__on_no_err(ibfile):
        return ibfile.read(sz4peek)

def _loop_body(ibfile, addr, sz4peek, /):
    dc = _mk4zlib()
    with with4seekback__on_no_err(ibfile):
        ibfile.seek(addr)
        #bs5peek = ibfile.peek(sz4peek)
            #AttributeError: '_io.BytesIO' object has no attribute 'peek'
        bs5peek = _peek(ibfile, sz4peek)
        assert ibfile.tell() == addr
        sz = init4bk_sz
        assert sz
        while 1:
            bs = ibfile.read(sz)
            if not bs:
                #eof
                #fail
                #break
                return False, bs5peek
            try:
                dc.decompress(bs)
            except Error4zlib:
                #fail
                #break
                return False, bs5peek
            if dc.eof:
                #found
                #yield addr
                #break
                return True, bs5peek
            #####
            sz = min(max4bk_sz, 2*sz)

if 1:
    del may_negativeable_begin_location
    del may_negativeable_end_location
    del overlap
    del output_addr_only
    del detect_header_only
    del using_789C_header_only


zlib_66_header_hex_ls = r"""'
'08 1d'
'08 3c'
'08 5b'
'08 7a'
'08 99'
'08 b8'
'08 d7'
'08 f6'
'18 19'
'18 38'
'18 57'
'18 76'
'18 95'
'18 b4'
'18 d3'
'18 f2'
'28 15'
'28 34'
'28 53'
'28 72'
'28 91'
'28 b0'
'28 cf'
'28 ee'
'38 11'
'38 30'
'38 4f'
'38 6e'
'38 8d'
'38 ac'
'38 cb'
'38 ea'
'48 0d'
'48 2c'
'48 4b'
'48 6a'
'48 89'
'48 a8'
'48 c7'
'48 e6'
'58 09'
'58 28'
'58 47'
'58 66'
'58 85'
'58 a4'
'58 c3'
'58 e2'
'68 05'
'68 24'
'68 43'
'68 62'
'68 81'
'68 a0'
'68 bf'
'68 de'
'68 fd'
'78 01'
'78 20'
'78 3f'
'78 5e'
'78 7d'
'78 9c'
'78 bb'
'78 da'
'78 f9'
'""".split("'\n'")#"""
del zlib_66_header_hex_ls[0]
del zlib_66_header_hex_ls[-1]
assert len(zlib_66_header_hex_ls) == 66
zlib_66_headers = [*map(bytes.fromhex, zlib_66_header_hex_ls)]
assert zlib_66_headers == \
[b'\x08\x1d', b'\x08<', b'\x08[', b'\x08z', b'\x08\x99', b'\x08\xb8', b'\x08\xd7', b'\x08\xf6', b'\x18\x19', b'\x188', b'\x18W', b'\x18v', b'\x18\x95', b'\x18\xb4', b'\x18\xd3', b'\x18\xf2', b'(\x15', b'(4', b'(S', b'(r', b'(\x91', b'(\xb0', b'(\xcf', b'(\xee', b'8\x11', b'80', b'8O', b'8n', b'8\x8d', b'8\xac', b'8\xcb', b'8\xea', b'H\r', b'H,', b'HK', b'Hj', b'H\x89', b'H\xa8', b'H\xc7', b'H\xe6', b'X\t', b'X(', b'XG', b'Xf', b'X\x85', b'X\xa4', b'X\xc3', b'X\xe2', b'h\x05', b'h$', b'hC', b'hb', b'h\x81', b'h\xa0', b'h\xbf', b'h\xde', b'h\xfd', b'x\x01', b'x ', b'x?', b'x^', b'x}', b'x\x9c', b'x\xbb', b'x\xda', b'x\xf9']
assert len(zlib_66_headers) == 66

zlib_66_headers__str = b''.join(zlib_66_headers).hex(' ', -2).upper()
#print(zlib_66_headers__str)
assert zlib_66_headers__str == '081D 083C 085B 087A 0899 08B8 08D7 08F6 1819 1838 1857 1876 1895 18B4 18D3 18F2 2815 2834 2853 2872 2891 28B0 28CF 28EE 3811 3830 384F 386E 388D 38AC 38CB 38EA 480D 482C 484B 486A 4889 48A8 48C7 48E6 5809 5828 5847 5866 5885 58A4 58C3 58E2 6805 6824 6843 6862 6881 68A0 68BF 68DE 68FD 7801 7820 783F 785E 787D 789C 78BB 78DA 78F9', zlib_66_headers__str
def __():
    ls = []
    for h in zlib_66_headers:
        u = int.from_bytes(h, 'big')
        #print(f'{u:0>16b}={u:0>4X}')
        v = int.from_bytes(h, 'little')
        s = f'{v:0>16b}'[::-1]
        line = f'{s}<--{v:0>4X}<--{u:0>4X}'
        #print(line)
        ls.append(line)
    ls.sort()
    for line in ls:
        print(line)
if 0b0:
    __();raise
    r'''
0001000000011101<--B808<--08B8
0001000000111100<--3C08<--083C
0001000001011110<--7A08<--087A
0001000001101111<--F608<--08F6
0001000010011001<--9908<--0899
0001000010111000<--1D08<--081D
0001000011011010<--5B08<--085B
0001000011101011<--D708<--08D7
0001001000010101<--A848<--48A8
0001001000110100<--2C48<--482C
0001001001010110<--6A48<--486A
0001001001100111<--E648<--48E6
0001001010010001<--8948<--4889
0001001010110000<--0D48<--480D
0001001011010010<--4B48<--484B
0001001011100011<--C748<--48C7
0001010000001101<--B028<--28B0
0001010000101100<--3428<--2834
0001010001001110<--7228<--2872
0001010001110111<--EE28<--28EE
0001010010001001<--9128<--2891
0001010010101000<--1528<--2815
0001010011001010<--5328<--2853
0001010011110011<--CF28<--28CF
0001011000000101<--A068<--68A0
0001011000100100<--2468<--6824
0001011001000110<--6268<--6862
0001011001111011<--DE68<--68DE
0001011010000001<--8168<--6881
0001011010100000<--0568<--6805
0001011010111111<--FD68<--68FD
0001011011000010<--4368<--6843
0001011011111101<--BF68<--68BF
0001100000011100<--3818<--1838
0001100000101101<--B418<--18B4
0001100001001111<--F218<--18F2
0001100001101110<--7618<--1876
0001100010011000<--1918<--1819
0001100010101001<--9518<--1895
0001100011001011<--D318<--18D3
0001100011101010<--5718<--1857
0001101000010100<--2858<--5828
0001101000100101<--A458<--58A4
0001101001000111<--E258<--58E2
0001101001100110<--6658<--5866
0001101010010000<--0958<--5809
0001101010100001<--8558<--5885
0001101011000011<--C358<--58C3
0001101011100010<--4758<--5847
0001110000001100<--3038<--3830
0001110000110101<--AC38<--38AC
0001110001010111<--EA38<--38EA
0001110001110110<--6E38<--386E
0001110010001000<--1138<--3811
0001110010110001<--8D38<--388D
0001110011010011<--CB38<--38CB
0001110011110010<--4F38<--384F
0001111000000100<--2078<--7820
0001111000111001<--9C78<--789C
0001111001011011<--DA78<--78DA
0001111001111010<--5E78<--785E
0001111010000000<--0178<--7801
0001111010011111<--F978<--78F9
0001111010111110<--7D78<--787D
0001111011011101<--BB78<--78BB
0001111011111100<--3F78<--783F
'''#'''

zlib_66_headers
uints5snd_bytes5zlib_headers = sorted({h[1] for h in zlib_66_headers})
assert uints5snd_bytes5zlib_headers == [1, 5, 9, 13, 17, 21, 25, 29, 32, 36, 40, 44, 48, 52, 56, 60, 63, 67, 71, 75, 79, 83, 87, 91, 94, 98, 102, 106, 110, 114, 118, 122, 125, 129, 133, 137, 141, 145, 149, 153, 156, 160, 164, 168, 172, 176, 180, 184, 187, 191, 195, 199, 203, 207, 211, 215, 218, 222, 226, 230, 234, 238, 242, 246, 249, 253], uints5snd_bytes5zlib_headers
assert len(uints5snd_bytes5zlib_headers) == 66, len(uints5snd_bytes5zlib_headers)
assert uints5snd_bytes5zlib_headers == [*range(1,29+1,4), *range(32,60+1,4), *range(63,91+1,4), *range(94,122+1,4), *range(125,153+1,4), *range(156,184+1,4), *range(187,215+1,4), *range(218,246+1,4), *range(249,253+1,4)]


uints5fst_bytes5zlib_headers = sorted({h[0] for h in zlib_66_headers})
assert uints5fst_bytes5zlib_headers == [8, 24, 40, 56, 72, 88, 104, 120], uints5fst_bytes5zlib_headers

assert uints5fst_bytes5zlib_headers == [*range(8,128,16)]
assert len(uints5fst_bytes5zlib_headers) == 0x80//16 == 8

uints5fst_bytes5zlib_headers = range(8,128,16)
assert [*uints5fst_bytes5zlib_headers] == [8, 24, 40, 56, 72, 88, 104, 120]
assert uints5fst_bytes5zlib_headers == range(8,128,16)
assert len(uints5fst_bytes5zlib_headers) == 0x80//16 == 8


assert {40, 56} == ({*uints5fst_bytes5zlib_headers} & {*uints5snd_bytes5zlib_headers})
uints5snd_bytes5zlib_headers = (*uints5snd_bytes5zlib_headers,)
common_uints5fst_bytes_snd_bytes5zlib_headers = frozenset({*uints5fst_bytes5zlib_headers} & {*uints5snd_bytes5zlib_headers})
def mk__xxx_obj_headers__sz_eq(DecompressErrorType, decompressor_copy, sz, /):
    headers4sz0 = [b'']
    headers4sz_ = headers4sz0
    for sz_ in range(sz):
        headers4sz_plus1 = mk__xxx_obj_headers__one_more_byte(DecompressErrorType, decompressor_copy,    sz_, headers4sz_)
        headers4sz_ = headers4sz_plus1
    headers4sz = headers4sz_
    return headers4sz
def mk__xxx_obj_headers__one_more_byte(DecompressErrorType, decompressor_copy,    sz, headers4sz, /):
    mk = decompressor_copy
    rngs = range(0x100)
    bs = [bytes([j]) for j in rngs]
    ls = []
    for h_ in headers4sz:
      assert len(h_) == sz
      #for j in rngs: header = h_ + bytes([j])
      for _b in bs:
        header = h_ + _b
        try:
          __ = mk().decompress(header)
        except DecompressErrorType:
          pass
        else:
          ls.append(header)
    return ls
    hs=[h.hex(' ') for h in ls]
    return ls, hs

if 0:
    #...header too long...
    def _mk__lzma_obj_headers(sz, /):
        return mk__xxx_obj_headers__sz_eq(Error4lzma, _mk4lzma, sz)
    lzma_obj_headers = ()
    if __name__ == "__main__":
        if 1:
            _ls = _mk__lzma_obj_headers(3)
            assert [*lzma_obj_headers] == _ls, ([*lzma_obj_headers], _ls, len(_ls))
def _mk__bz2_obj_headers():
    headers4sz4 = mk__xxx_obj_headers__sz_eq(Error4bz2, _mk4bz2, 4)
    return headers4sz4
bz2_obj_headers = (b'BZh1', b'BZh2', b'BZh3', b'BZh4', b'BZh5', b'BZh6', b'BZh7', b'BZh8', b'BZh9')
if __name__ == "__main__":
    if 0:assert [*bz2_obj_headers] == _mk__bz2_obj_headers(), ([*bz2_obj_headers], _mk__bz2_obj_headers())

def _mk__zlib_66_headers():
    headers4sz2 = mk__xxx_obj_headers__sz_eq(Error4zlib, _mk4zlib, 2)
    assert headers4sz2 == zlib_66_headers
    return headers4sz2
    ######old version@interact-mode:
    import zlib
    mk = zlib.decompressobj().copy
    rngs = range(0x100)
    ls = []
    for i in rngs:
      for j in rngs:
        header = bytes([i,j])
        try:
          __ = mk().decompress(header)
        except zlib.error:
          pass
        else:
          ls.append(header)
    hs=[h.hex(' ') for h in ls]
    assert ls == zlib_66_headers
    assert hs == zlib_66_header_hex_ls
    return ls
if __name__ == "__main__":
    if 0:assert _mk__zlib_66_headers() == zlib_66_headers

def _mk__zlib_xx_3byte_headers():
    ######old version@interact-mode:
    import zlib
    mk = zlib.decompressobj().copy
    rngs = range(0x100)
    ls = []
    for h2 in zlib_66_headers:
      for j in rngs:
        header = bytes([*h2,j])
        try:
          __ = mk().decompress(header)
        except zlib.error:
          pass
        else:
          ls.append(header)
    hs=[h.hex(' ') for h in ls]
    return ls
if 0:
    ls = _mk__zlib_xx_3byte_headers()
    print(ls)
    print(len(ls))
    assert len(ls) == 14848
    14848
assert 66*128 == 8448
assert 66*0x100 == 16896
assert str(14848/66) == '224.96969696969697'

zlib_66_headers__pattern = b'(?:' + b'|'.join(map(re.escape, zlib_66_headers)) + b')'
#print(zlib_66_headers__pattern)
assert zlib_66_headers__pattern == \
b'(?:\x08\x1d|\x08<|\x08\\[|\x08z|\x08\x99|\x08\xb8|\x08\xd7|\x08\xf6|\x18\x19|\x188|\x18W|\x18v|\x18\x95|\x18\xb4|\x18\xd3|\x18\xf2|\\(\x15|\\(4|\\(S|\\(r|\\(\x91|\\(\xb0|\\(\xcf|\\(\xee|8\x11|80|8O|8n|8\x8d|8\xac|8\xcb|8\xea|H\\\r|H,|HK|Hj|H\x89|H\xa8|H\xc7|H\xe6|X\\\t|X\\(|XG|Xf|X\x85|X\xa4|X\xc3|X\xe2|h\x05|h\\$|hC|hb|h\x81|h\xa0|h\xbf|h\xde|h\xfd|x\x01|x\\ |x\\?|x\\^|x\\}|x\x9c|x\xbb|x\xda|x\xf9)'

zlib_66_headers__pattern = \
rb'(?:\x08\x1d|\x08<|\x08\[|\x08z|\x08\x99|\x08\xb8|\x08\xd7|\x08\xf6|\x18\x19|\x188|\x18W|\x18v|\x18\x95|\x18\xb4|\x18\xd3|\x18\xf2|\(\x15|\(4|\(S|\(r|\(\x91|\(\xb0|\(\xcf|\(\xee|8\x11|80|8O|8n|8\x8d|8\xac|8\xcb|8\xea|H\r|H,|HK|Hj|H\x89|H\xa8|H\xc7|H\xe6|X\t|X\(|XG|Xf|X\x85|X\xa4|X\xc3|X\xe2|h\x05|h\$|hC|hb|h\x81|h\xa0|h\xbf|h\xde|h\xfd|x\x01|x\ |x\?|x\^|x\}|x\x9c|x\xbb|x\xda|x\xf9)'

zlib_66_headers__regex = re.compile(zlib_66_headers__pattern)
assert all(map(zlib_66_headers__regex.fullmatch, zlib_66_headers))

zlib_66_headers = (*zlib_66_headers,)
    #exported@__all__
from nn_ns.bin.find_zlib_objs_in_file import iter_find_zlib_objs_in_file__ipath_, iter_find_zlib_objs_in_file_, buggy_header4zlib
from nn_ns.bin.find_zlib_objs_in_file import zlib_66_headers, zlib_66_headers__str, uints5fst_bytes5zlib_headers

from nn_ns.bin.find_zlib_objs_in_file import (zlib_66_headers
,   iter_find_xxx_objs_in_file_
,       iter_find_xxx_obj_headers_in_file_
,       xxx_obj_recognizer_5incremental_decompressor_factory
,           zlib_obj_recognizer_
,           bz2_obj_recognizer_
,           lzma_obj_recognizer_
,               Error4zlib
,               Error4bz2
,               Error4lzma
,               Error4gzip
#
,   iter_find_zlib_objs_in_file__ipath_
,       iter_find_zlib_objs_in_file_
,           buggy_header4zlib
,           zlib_66_headers
,               zlib_66_headers__str
,               uints5fst_bytes5zlib_headers
#
,   iter_find_bz2_objs_in_file__ipath_
,           iter_find_bz2_objs_in_file_
,               header4bz2
,               bz2_obj_headers
#
,   header4SQLite
,       header4sqlite3
,   header4zip
,       header4zipfile
,   is_zipfile
,       is_tarfile
,   header4gzip
,   header4bz2
,   buggy_header4lzma
#
,   mk__xxx_obj_headers__sz_eq
,   mk__xxx_obj_headers__one_more_byte
    )



from nn_ns.bin.find_zlib_objs_in_file import *
