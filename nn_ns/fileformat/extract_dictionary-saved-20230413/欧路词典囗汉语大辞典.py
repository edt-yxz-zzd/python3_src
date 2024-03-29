#__all__:goto
r'''[[[
e script/欧路词典囗汉语大辞典.py
      codecs.register_error()
e ../lots/NOTE/Python/python-bug/codec-bug.txt
    bug:utf8-decoder reuse exc obj, update (.start, .end) but not (.args)
view ../../python3_src/seed/text/decode_on_err_bytes_.py

script.欧路词典囗汉语大辞典
py -m nn_ns.app.debug_cmd   script.欧路词典囗汉语大辞典
py -m nn_ns.app.doctest_cmd script.欧路词典囗汉语大辞典:f -v
from script.欧路词典囗汉语大辞典 import f

py -m nn_ns.app.adhoc_argparser__main__call8module   script.欧路词典囗汉语大辞典   @_test__replace_by_newline
py -m nn_ns.app.adhoc_argparser__main__call8module   script.欧路词典囗汉语大辞典   @看看有哪些直接存储的字符串 --iencoding:utf8 --ipath:/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb --opath:/sdcard/0my_files/tmp/out4py/script.欧路词典囗汉语大辞典.看看有哪些直接存储的字符串.out.txt
du -bh /sdcard/0my_files/tmp/out4py/script.欧路词典囗汉语大辞典.看看有哪些直接存储的字符串.out.txt
140M
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗汉语大辞典.看看有哪些直接存储的字符串.out.txt
[[
+  汉语大辞典@可查成语48700条、汉字20973个、词语377590条、诗词93535首、歇后语16648条、灯谜40790条、对联5390幅、妙言警句13752条、俗语1929条、谚语1200条、同义词2036组、反义词3282组、别名近1000组、古文词语近1000组，内设【辞海成语词典】、【常用成语词典】、【新华字典】、【中华辞海】、【中华诗词】、【拼音专家】、【歇后语大全】、【灯谜大全】、【对联欣赏】、【同义反义别名词典】、【名言词典】、【古文词典】及【成语故事】等内容，其拼音、解释、出处、示例等等都一目了然。
+
+作者：Eudic


+     @  r   <?xml version="1.0" encoding="UTF-8"?><EuDic><DicCategory><![CDATA[汉语⇒汉语,推荐]]></DicCategory></EuDic>                     <&  `9     DW     Ut     

]]

[[
汉语大辞典
/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb

py script/欧路词典.py search -t '昔者莊周夢為胡蝶' -i  /sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb   -v 2
  无结果

/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb

du -bh /sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb
79M

du -b /sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb
82724782

hex 82724782
'0x4ee47ae'

文件最后:
阿阿Ｑ阿阿阿八阿爸阿傍阿謗阿保阿
... ...
座中銘座主做做嗄做伴做保做弊做病
... ...
做住做莊做樁做嘴做嘴臉做作葄 
... ...空白大约2800字符... ...

49162*16-2=786590 汉字

欧路词典，搜索框:
    『做』:做、做爱、做伴、做东、做法、...
    『葄』只有2项:
        汉语大辞典
        葄
        中华成语大词典
        葄枕图史




定位『葄』:
hex $[82724782-2800]
'0x4ee3cbe'

hexdump /sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb -n 0x100 -s 0x4ee4700 -C
[[
04ee4700  00 00 02 00 00 00 02 00  00 00 02 00 00 00 02 00  |................|
*
04ee47a0  00 00 02 00 00 00 02 00  00 00 02 00 00 00        |..............|
04ee47ae
]]

hexdump /sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb -n 0x100 -s 0x4ee3ca0 -C
[[
04ee3ca0  9a e5 98 b4 e5 81 9a e5  98 b4 e8 87 89 e5 81 9a  |................|
04ee3cb0  e4 bd 9c e8 91 84 02 00  00 00 02 00 00 00 02 00  |................|
04ee3cc0  00 00 02 00 00 00 02 00  00 00 02 00 00 00 02 00  |................|
*
04ee3da0
]]
py_eval "'做住做莊做樁做嘴做嘴臉做作葄\2\0'.encode('u8').hex(':',2)"
'e581:9ae4:bd8f:e581:9ae8:8e8a:e581:9ae6:a881:e581:9ae5:98b4:e581:9ae5:98b4:e887:89e5:819a:e4bd:9ce8:9184:0200'
py_eval "'葄'.encode('u8').hex(':',2)"
'e8:9184'
py_eval "'葄'.encode('u8')"
b'\xe8\x91\x84'




hexdump /sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb -n 3 -s 0x4ee3cb3 -C
[[
04ee3cb3  e8 91 84                                          |...|
04ee3cb6
]]

在文件内搜索『葄』地址『0x4ee3cb3』

定位『阿』:
hex $[0x4ee3cb3-3*786590]
'0x4ca3ad9'

hexdump /sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb -n 0x50 -s 0x4ca3f30 -C
[[
04ca3f30  00 00 00 00 73 01 00 00  4d fd 23 00 20 10 a8 00  |....s...M.#. ...|
04ca3f40  00 00 00 00 a8 06 00 00  53 fd 23 00 d5 ee c2 06  |........S.#.....|
04ca3f50  00 00 00 00 e9 01 00 00  56 fd 23 00 00 00 00 00  |........V.#.....|
04ca3f60  e9 98 bf e9 98 bf ef bc  b1 e9 98 bf e9 98 bf e9  |................|
04ca3f70  98 bf e5 85 ab e9 98 bf  e7 88 b8 e9 98 bf e5 82  |................|
04ca3f80
]]

py_eval "'阿阿Ｑ阿阿阿八阿爸阿傍阿謗阿保阿'.encode('u8').hex(':',2)"
'e998:bfe9:98bf:efbc:b1e9:98bf:e998:bfe9:98bf:e585:abe9:98bf:e788:b8e9:98bf:e582:8de9:98bf:e8ac:97e9:98bf:e4bf:9de9:98bf'

py_eval "'阿'.encode('u8')"
b'\xe9\x98\xbf'


在文件内搜索『阿』地址『0x4ca3f60』

高频模式:周期16 BYTE:『fd 23 00』

0x_00_23_fd_4d
0x_00_23_fd_53
hexdump /sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb -n 0x100 -s 0x0023fd00 -C
[[
...
0023fd40  c2 8b 23 71 33 37 39 6c  8c e6 1d 0f ef 11 76 22  |..#q379l......v"|
0023fd50  f3 1c 73 9f 2c 3f 0c 88  76 5f 14 57 72 e4 16 3e  |..s.,?..v_.Wr..>|
...
]]


#py -m nn_ns.app.search_bytes_in_file -i '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb'    -e4bs 'utf8'   '葄'
5757838
29749355
31138882
42284739
82592113
82721971

hex 5757838 29749355 31138882 42284739 82592113 82721971
'0x57db8e'
'0x1c5f06b'
'0x1db2442'
'0x28536c3'
'0x4ec4171'
'0x4ee3cb3'

py -m nn_ns.app.search_bytes_in_file -i '/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb' --format4show_address $'{0}=0x{0:X}\n'    -e4bs 'utf8'   '葄'
5757838=0x57DB8E
29749355=0x1C5F06B
31138882=0x1DB2442
42284739=0x28536C3
82592113=0x4EC4171
82721971=0x4EE3CB3

hexdump /sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb -n 0x100 -s 0x57db00 -C




======================
======================
======================
======================试用-第一#上面后来
xxx view ++enc=utf-8 /sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb
with open('/sdcard/0my_files/tmp/out4py/script.欧路词典囗汉语大辞典.as-utf8.errors=replace.out.txt', 'xt', encoding='u8') as fout:
open('/sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb', 'rt', encoding='u8', errors='replace')
hexdump /sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb -n 1280 -s 0x420 -C
  出现 大量 数字 #见上面，都是词组数目
  出现 xml

!mkdir /sdcard/0my_files/tmp/out4hexdump/
hexdump /sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb -n 0x380 -s 0x420 -C > /sdcard/0my_files/tmp/out4hexdump/eudb_en-汉语大辞典-1317108648.eudb.0x420+0x380.out.txt
view  /sdcard/0my_files/tmp/out4hexdump/eudb_en-汉语大辞典-1317108648.eudb.0x420+0x380.out.txt
  [
00000420  be 9e e5 85 b8 40 e5 8f  af e6 9f a5 e6 88 90 e8  |.....@..........|
00000430  af ad 34 38 37 30 30 e6  9d a1 e3 80 81 e6 b1 89  |..48700.........|
00000440  e5 ad 97 32 30 39 37 33  e4 b8 aa e3 80 81 e8 af  |...20973........|
00000450  8d e8 af ad 33 37 37 35  39 30 e6 9d a1 e3 80 81  |....377590......|
00000460  e8 af 97 e8 af 8d 39 33  35 33 35 e9 a6 96 e3 80  |......93535.....|
00000470  81 e6 ad 87 e5 90 8e e8  af ad 31 36 36 34 38 e6  |..........16648.|
00000480  9d a1 e3 80 81 e7 81 af  e8 b0 9c 34 30 37 39 30  |...........40790|
00000490  e6 9d a1 e3 80 81 e5 af  b9 e8 81 94 35 33 39 30  |............5390|
000004a0  e5 b9 85 e3 80 81 e5 a6  99 e8 a8 80 e8 ad a6 e5  |................|
000004b0  8f a5 31 33 37 35 32 e6  9d a1 e3 80 81 e4 bf 97  |..13752.........|
000004c0  e8 af ad 31 39 32 39 e6  9d a1 e3 80 81 e8 b0 9a  |...1929.........|
000004d0  e8 af ad 31 32 30 30 e6  9d a1 e3 80 81 e5 90 8c  |...1200.........|
000004e0  e4 b9 89 e8 af 8d 32 30  33 36 e7 bb 84 e3 80 81  |......2036......|
000004f0  e5 8f 8d e4 b9 89 e8 af  8d 33 32 38 32 e7 bb 84  |.........3282...|
00000500  e3 80 81 e5 88 ab e5 90  8d e8 bf 91 31 30 30 30  |............1000|
00000510  e7 bb 84 e3 80 81 e5 8f  a4 e6 96 87 e8 af 8d e8  |................|
00000520  af ad e8 bf 91 31 30 30  30 e7 bb 84 ef bc 8c e5  |.....1000.......|
00000530  86 85 e8 ae be e3 80 90  e8 be 9e e6 b5 b7 e6 88  |................|

... ...
000006b0  ef bc 9a 45 75 64 69 63  fd b7 32 01 00 00 00 00  |...Eudic..2.....|
000006c0  00 00 00 00 e7 15 00 00  78 2e 75 04 00 00 00 00  |........x.u.....|
000006d0  60 3f ca 04 00 00 00 00  56 fd 23 00 0e 51 05 00  |`?......V.#..Q..|
000006e0  10 00 00 00 b6 3c ee 04  00 00 00 00 00 40 00 00  |.....<.......@..|
000006f0  72 00 00 00 3c 3f 78 6d  6c 20 76 65 72 73 69 6f  |r...<?xml versio|
00000700  6e 3d 22 31 2e 30 22 20  65 6e 63 6f 64 69 6e 67  |n="1.0" encoding|
00000710  3d 22 55 54 46 2d 38 22  3f 3e 3c 45 75 44 69 63  |="UTF-8"?><EuDic|
00000720  3e 3c 44 69 63 43 61 74  65 67 6f 72 79 3e 3c 21  |><DicCategory><!|
00000730  5b 43 44 41 54 41 5b e6  b1 89 e8 af ad e2 87 92  |[CDATA[.........|
00000740  e6 b1 89 e8 af ad 2c e6  8e a8 e8 8d 90 5d 5d 3e  |......,......]]>|
00000750  3c 2f 44 69 63 43 61 74  65 67 6f 72 79 3e 3c 2f  |</DicCategory></|
00000760  45 75 44 69 63 3e 00 00  00 00 00 00 00 00 00 00  |EuDic>..........|
00000770  00 00 00 00 00 00 00 00  00 00 00 3c 26 00 00 60  |...........<&..`|
00000780  39 01 00 00 00 00 00 44  57 01 00 00 00 00 00 55  |9......DW......U|
00000790  74 01 00 00 00 00 00 9e  91 01 00 00 00 00 00 81  |t...............|
000007a0
==>> 『60 39 01 00』=0x13960@0x77f
  ]


[
$ hexdump --help

Usage:
 hexdump [options] <file>...

Display file contents in hexadecimal, decimal, octal, or ascii.

Options:
 -b, --one-byte-octal      one-byte octal display
 -c, --one-byte-char       one-byte character display
 -C, --canonical           canonical hex+ASCII display
 -d, --two-bytes-decimal   two-byte decimal display
 -o, --two-bytes-octal     two-byte octal display
 -x, --two-bytes-hex       two-byte hexadecimal display
 -L, --color[=<mode>]      interpret color formatting specifiers
                             colors are enabled by default
 -e, --format <format>     format string to be used for displaying data
 -f, --format-file <file>  file that contains format strings
 -n, --length <length>     interpret only length bytes of input
 -s, --skip <offset>       skip offset bytes from the beginning
 -v, --no-squeezing        output identical lines

 -h, --help                display this help
 -V, --version             display version

Arguments:
 <length> and <offset> arguments may be followed by the suffixes for
   GiB, TiB, PiB, EiB, ZiB, and YiB (the "iB" is optional)

For more details see hexdump(1).
]


snippet -h
usage: get_file_chunks.py [-h] [-c CHUNK_SIZE]
                          [-n NUM_CHUNKS]
                          [-b BEGIN]
                          fname
snippet /sdcard/20220614_copy5sd__0my_files/unzip/eudb_en/1317108648.eudb -c 16 -n 8 -b 0
[b'V\x11m\x03\x00\x00`9\x01\x00\x02\x00\x00\x004\x0c',
 b'\x03\x00\x00\x00\xb6KRE>x\xb3mP\xd2^\xfe',
 b'Y\xa1\x88\x96*\x14\xafw\xf0\x96T\xa1\xf8\xaa\xaat',
 b'\xa46&\x946\x8f1\xa3`@p\xa9\x90\xd0R>',
 b"[\tsh'\xf1c\xf33\x17\xc4 \xf7\xb1L\x93",
 b'\xcd?\xc9\x19\xab\xca\xc7\xcao\xe55\xea\xa4\x05\xe6 ',
 b'C\x15E\xef7BL\xb2\xd33`\x1f\xca\x11\xab\xaf',
 b'\xf3\xdc\xdbQ\x079\x92\x91A\xa9\xf9B\xbbyN-']

]]
[[
py_help @UnicodeDecodeError
    #UnicodeDecodeError((encoding, object, start, end, reason))
    [
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  encoding
 |      exception encoding
 |
 |  end
 |      exception end
 |
 |  object
 |      exception object
 |
 |  reason
 |      exception reason
 |
 |  start
 |      exception start
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from BaseException:
 |
 |  __cause__
 |      exception cause
 |
 |  __context__
 |      exception context
 |
 |  __dict__
 |
 |  __suppress_context__
 |
 |  __traceback__
 |
 |  args
    ]

py_help codecs@register_error
    [
register_error(errors, handler, /)
    Register the specified error handler under the name errors.

    handler must be a callable object, that will be called with an exception instance containing information about the location of the encoding/decoding error and must return a (replacement, new position) tuple.
    ]
py_help codecs@lookup_error
    [
lookup_error(name, /)
    lookup_error(errors) -> handler

    Return the error handler for the specified error handling name or raise a LookupError, if no handler exists under this name.
    ]

ch2nm �
    'name': 'REPLACEMENT CHARACTER'
    'unicode': 65533,
    'unicode_hex': '0xfffd'
py_eval 'chr(0xFFFD).encode("u8")'
b'\xef\xbf\xbd'


>>> import codecs

>>> for s in dir(codecs):print(s)
BOM
BOM32_BE
BOM32_LE
BOM64_BE
BOM64_LE
BOM_BE
BOM_LE
BOM_UTF16
BOM_UTF16_BE
BOM_UTF16_LE
BOM_UTF32
BOM_UTF32_BE
BOM_UTF32_LE
BOM_UTF8
BufferedIncrementalDecoder
BufferedIncrementalEncoder
Codec
CodecInfo
EncodedFile
IncrementalDecoder
IncrementalEncoder
StreamReader
StreamReaderWriter
StreamRecoder
StreamWriter
__all__
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__spec__
_false
ascii_decode
ascii_encode
backslashreplace_errors
builtins
charmap_build
charmap_decode
charmap_encode
decode
encode
escape_decode
escape_encode
getdecoder
getencoder
getincrementaldecoder
getincrementalencoder
getreader
getwriter
ignore_errors
iterdecode
iterencode
latin_1_decode
latin_1_encode
lookup
lookup_error
make_encoding_map
make_identity_dict
namereplace_errors
open
raw_unicode_escape_decode
raw_unicode_escape_encode
readbuffer_encode
register
register_error
replace_errors
strict_errors
sys
unicode_escape_decode
unicode_escape_encode
unregister
utf_16_be_decode
utf_16_be_encode
utf_16_decode
utf_16_encode
utf_16_ex_decode
utf_16_le_decode
utf_16_le_encode
utf_32_be_decode
utf_32_be_encode
utf_32_decode
utf_32_encode
utf_32_ex_decode
utf_32_le_decode
utf_32_le_encode
utf_7_decode
utf_7_encode
utf_8_decode
utf_8_encode
xmlcharrefreplace_errors






#这些大概是codecs.register_error(errors, handler, /)的handler
    backslashreplace_errors
    ignore_errors
    namereplace_errors
    replace_errors
    strict_errors
    xmlcharrefreplace_errors

lookup_error
register_error

>>> for s in (codecs.__all__):print(s)
register
lookup
open
EncodedFile
BOM
BOM_BE
BOM_LE
BOM32_BE
BOM32_LE
BOM64_BE
BOM64_LE
BOM_UTF8
BOM_UTF16
BOM_UTF16_LE
BOM_UTF16_BE
BOM_UTF32
BOM_UTF32_LE
BOM_UTF32_BE
CodecInfo
Codec
IncrementalEncoder
IncrementalDecoder
StreamReader
StreamWriter
StreamReaderWriter
StreamRecoder
getencoder
getdecoder
getincrementalencoder
getincrementaldecoder
getreader
getwriter
encode
decode
iterencode
iterdecode
strict_errors
ignore_errors
replace_errors
xmlcharrefreplace_errors
backslashreplace_errors
namereplace_errors
register_error
lookup_error



]]

#]]]'''
__all__ = r'''
'''.split()#'''
__all__

def _():
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import echo, print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
    from seed.helper.repr_input import repr_helper

def _():
  class _(ABC):
    __slots__ = ()
    raise NotImplementedError
    def __repr__(sf, /):
        return repr_helper(sf, *args, **kwargs)
        return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
    from seed.helper.repr_input import repr_helper_ex
    from seed.helper.repr_input import repr_helper

#from seed.seq_tools.find_all import find_all_, iter_all_
#from seed.seq_tools.mk_nonsubseq_of import check_antisubseq_, mk_a_nonsub_uint_seq_of_uint_seq_, mk_a_nonsubseq_of_
#def mk_a_nonsub_uint_seq_of_uint_seq_(bad_uint, uint_seq, /)->antisubseq:
#def mk_a_nonsubseq_of_(key_seq, /, *, is_key_ok, extra_keys)->antisubseq:

from codecs import lookup_error, register_error
_handler4replace8errors_ = lookup_error('replace')
    #codecs.replace_errors
#help(_handler4replace8errors_)

def mk_handler4replace8errors_(from_replacement, /):
    #handler must be a callable object, that will be called with an exception instance containing information about the location of the encoding/decoding error and must return a (replacement, new position) tuple.
    def _handler4replace8errors(exc, /):
        args = (
        (exc.encoding
        ,exc.object
        ,exc.start
        ,exc.end
        ,exc.reason
        ))
        (encoding, object, start, end, reason) = exc.args
        if 0:
            for x, y in zip(exc.args, args):
                assert x is y, ((x,y), (start,end), (exc.start,exc.end))
                    #AssertionError: ((20, 26), (20, 21), (26, 27))
        if 1:
            print(((start,end), (exc.start,exc.end)))
            print(hex(id(exc)))
            r'''
            ((20, 21), (20, 21))
            0x70c2ce1ec0
            ((20, 21), (26, 27))
            0x70c2ce1ec0
            ... ...
            ((20, 21), (122, 123))
            0x70c2ce1ec0
            ((20, 21), (124, 125))
            0x70c2ce1ec0
            ---
            我猜可能是 重用 第一个exc
                exc.start = ...
                exc.end = ...
                但没有:
                    exc.args = ...
                ==>>以 (exc.start,exc.end) 为准，不使用 exc.args
            #'''
        (_replacement, new_position) = _handler4replace8errors_(exc)
        assert exc.end == new_position, (exc.end, new_position)
        #raise ValueError((_replacement, new_position, exc)) from exc
        replacement = from_replacement(_replacement)
        return (replacement, new_position)
    return _handler4replace8errors

if 1:
    register_error('replace_by_newline', mk_handler4replace8errors_(lambda s:'\n'))
    _1 = lookup_error('replace_by_newline')
    register_error('replace_by_newline', mk_handler4replace8errors_(lambda s:s+'\n'))
    _2 = lookup_error('replace_by_newline')
    assert _1 is not _2
if 1:
    register_error('replace_by_newline', mk_handler4replace8errors_(lambda s:s+'\n'))
else:
    register_error('replace_by_newline', mk_handler4replace8errors_(lambda s:'\n'))

def _handler4raise_from_replace(exc, /):
    (_replacement, new_position) = _handler4replace8errors_(exc)
    raise ValueError((_replacement, new_position, exc)) from exc
register_error('raise_from_replace', _handler4raise_from_replace)

def _test__replace_by_newline():
    bs = (
b'V\x11m\x03\x00\x00`9\x01\x00\x02\x00\x00\x004\x0c'
b'\x03\x00\x00\x00\xb6KRE>x\xb3mP\xd2^\xfe'
b'Y\xa1\x88\x96*\x14\xafw\xf0\x96T\xa1\xf8\xaa\xaat'
b'\xa46&\x946\x8f1\xa3`@p\xa9\x90\xd0R>'
b"[\tsh'\xf1c\xf33\x17\xc4 \xf7\xb1L\x93"
b'\xcd?\xc9\x19\xab\xca\xc7\xcao\xe55\xea\xa4\x05\xe6 '
b'C\x15E\xef7BL\xb2\xd33`\x1f\xca\x11\xab\xaf'
b'\xf3\xdc\xdbQ\x079\x92\x91A\xa9\xf9B\xbbyN-'
    )
    #bs.decode(encoding='u8', errors='raise_from_replace')
        #UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb6 in position 20: invalid start byte
        #ValueError: ('�', 21, UnicodeDecodeError('utf-8', bs, 20, 21, 'invalid start byte'))
            #UnicodeDecodeError((encoding, object, start, end, reason))

    s = bs.decode(encoding='u8', errors='replace_by_newline')
    print(s)
    print(repr(s))
    if 0:
        print(repr(bs[20:21]))
        print(repr(bs[26:27]))
    assert bs[20:21] == b'\xb6'
    assert bs[26:27] == b'\xb3'
REPLACEMENT_CHARACTER = '\uFFFD'
u8_bytes4REPLACEMENT_CHARACTER = b'\xef\xbf\xbd'
assert ord('�') == 0xFFFD
assert REPLACEMENT_CHARACTER == '\uFFFD' == chr(0xFFFD) == '�' == u8_bytes4REPLACEMENT_CHARACTER.decode('u8') == b'\x80'.decode(encoding='ascii', errors='replace')
assert chr(0xFFFD).encode("u8") == b'\xef\xbf\xbd' == u8_bytes4REPLACEMENT_CHARACTER

from seed.text.decode_on_err_bytes_ import decode_on_err_bytes_
    #def decode_on_err_bytes_(encoding, bs, /):
    #   :: encoding -> bytes -> (ok_strs/[str], bad_bss/[bytes]{.len=1+len(ok_strs)})
from pathlib import Path
from seed.tiny import mk_fprint
from seed.io.may_open import open4w, open4w_err, open4r
def 看看有哪些直接存储的字符串(*, iencoding, ipath, opath=None, oencoding='utf8', force=False):
    ipath = Path(ipath)
    bs = ipath.read_bytes()
    (ok_strs, bad_bss) = decode_on_err_bytes_(iencoding, bs)
    with open4w(opath, force=force, xencoding=oencoding) as fout:
        fprint = mk_fprint(fout)
        for bad_bs, ok_str in zip(bad_bss, ok_strs):
            fprint(f'-{len(bad_bs)}')
            #fprint(f'+{ok_str!r}')
            #   \uXXXX 不行！
            for s in ok_str.split('\n'):
                fprint(f'+{s!s}')
        else:
            bad_bs = bad_bss[-1]
            fprint(f'-{len(bad_bs)}')




if __name__ == "__main__":
    pass
