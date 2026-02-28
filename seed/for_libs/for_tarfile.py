#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_tarfile.py
view ../../python3_src/seed/io/decompress_truncated_file.py
see:
    view ../../python3_src/seed/for_libs/for_tarfile.py
    view others/app/termux/tar_7zip.txt
    view others/app/termux/help/xz.txt
    view others/app/termux/help/lzma-see-xz.txt
    view /sdcard/0my_files/unzip/py_doc/python-3.12.4-docs-text/library/tarfile.txt


seed.for_libs.for_tarfile
py -m nn_ns.app.debug_cmd   seed.for_libs.for_tarfile -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.for_libs.for_tarfile:__doc__ -ht # -ff -df

copy from:view others/app/termux/tar_7zip.txt
[[
see:py::shutil,tarfile,zipfile
httpd -f /sdcard/0my_files/git_repos/txt_phone/lots/NOTE/html/httpd-confs/httpd.conf-sdcard_0my_files-unzip-py_doc-python_3_12_4_docs_html
http://127.0.0.1:3124/library/tarfile.html#module-tarfile
http://127.0.0.1:3124/library/shutil.html#archiving-operations
==>>:
High-level utilities to create and read compressed and archived files are also provided. They rely on the zipfile and tarfile modules.

shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])
shutil.unpack_archive(filename[, extract_dir[, format[, filter]]]

shutil.get_archive_formats()
  -> [(name, description)]
shutil.get_unpack_formats()
  -> [(name, extensions, description)]

default-supported-names of get_archive_formats&get_unpack_formats:
  zip: ZIP file (unpacking compressed files works only if the corresponding module is available).
  tar: uncompressed tar file.
  gztar: gzip’ed tar-file (if the zlib module is available).
  bztar: bzip2’ed tar-file (if the bz2 module is available).
  xztar: xz’ed tar-file (if the lzma module is available).


===
view others/app/termux/help/xz.txt
man lzma
  『lzma』 is equivalent to 『xz --format=lzma』.
man xz
view others/app/termux/help/xz.man.txt
view others/app/termux/help/xz.help.txt
man xz
  ==>> file suffix: .xz  .lzma  .lz  ; .txz  .tlz # .txz==.tar.xz  .tlz==.tar.lz
  ==>> format:auto,xz,lzma/alone,lzip,raw


==>>:
py -m tarfile -l script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma
  => 『script/搜索冫最短加链长度.py..statistics.out.txt』


class tarfile.TarInfo(name='')
class tarfile.TarFile(name=None, mode='r', fileobj=None, format=DEFAULT_FORMAT, tarinfo=TarInfo, dereference=False, ignore_zeros=False, encoding=ENCODING, errors='surrogateescape', pax_headers=None, debug=0, errorlevel=1)
    vs:
tarfile.open(name=None, mode='r', fileobj=None, bufsize=10240, **kwargs)
  mode has to be a string of the form 'filemode[:compression]':
  * 'r' or 'r:*'
    Open for reading with transparent compression (recommended).
  * 'r:'
    Open for reading exclusively without compression.
  * 'r:gz'
    Open for reading with gzip compression.
  * 'r:bz2'
    Open for reading with bzip2 compression.
  * 'r:xz'
    Open for reading with lzma compression.
  * 'x:xz'
    Create a tarfile with lzma compression. Raise a FileExistsError exception if it already exists.
  * 'w:xz'
    Open for lzma compressed writing.
  ===
  * 'r|xz'
    Open an lzma compressed stream for reading.
  * 'w|xz'
    Open an lzma compressed stream for writing.
tarfile.is_tarfile(name)
  :: (str|?file?|file-like object) -> bool

[tar_file ~=~ [tar-block]]
[archive_member == stored file) ~=~ [head-block; data-block...]]

TarFile Objects
The TarFile object provides an interface to a tar archive.
  A tar archive is a sequence of blocks.
  An archive member (a stored file) is made up of a header block followed by data blocks.
    It is possible to store a file in a tar archive several times.
    Each archive member is represented by a TarInfo object, see TarInfo Objects for details.


TarInfo Objects
A TarInfo object represents one member in a TarFile.
  Aside from storing all required attributes of a file (like file type, size, time, permissions, owner etc.)
    , it provides some useful methods to determine its type.
  It does not contain the file’s data itself.

TarInfo objects are returned by TarFile’s methods getmember(), getmembers() and gettarinfo().

Modifying the objects returned by getmember() or getmembers() will affect all subsequent operations on the archive.
  For cases where this is unwanted, you can use copy.copy() or call the replace() method to create a modified copy in one step.

Several attributes can be set to None to indicate that a piece of metadata is unused or unknown. Different TarInfo methods handle None differently:
  * extract() or extractall() methods will ignore the corresponding metadata, leaving it set to a default.
  * addfile() will fail.
  * list() will print a placeholder string.

class tarfile.TarInfo(name='')
  Create a TarInfo object.

classmethod TarInfo.frombuf(buf, encoding, errors)
  Create and return a TarInfo object from string buffer buf.
  Raises HeaderError if the buffer is invalid.

classmethod TarInfo.fromtarfile(tarfile)
  Read the next member from the TarFile object tarfile and return it as a TarInfo object.

TarInfo.tobuf(format=DEFAULT_FORMAT, encoding=ENCODING, errors='surrogateescape')
  Create a string buffer from a TarInfo object. For information on the arguments see the constructor of the TarFile class.


TarFile.getmember(name)
  -> TarInfo{name} | ^KeyError@non_existed
  Note If a member occurs more than once in the archive, its last occurrence is assumed to be the most up-to-date version.

TarFile.getmembers()
  -> [TarInfo]
  The list has the same order as the members in the archive.

TarFile.getnames()
  -> [TarInfo.name]
  It has the same order as the list returned by getmembers().

TarFile.next()
  [open4reading] => -> may TarInfo{next_member}

TarFile.gettarinfo(name=None, arcname=None, fileobj=None)
  -> TarInfo
  Create a TarInfo object from the result of os.stat() or equivalent on an existing file.
    The file is either named by name, or specified as a file object fileobj with a file descriptor.
    name may be a path-like object.
    If given, arcname specifies an alternative name for the file in the archive, otherwise, the name is taken from fileobj’s name attribute, or the name argument. The name should be a text string.

  You can modify some of the TarInfo’s attributes before you add it using addfile().
    If the file object is not an ordinary file object positioned at the beginning of the file, attributes such as size may need modifying. This is the case for objects such as GzipFile.
    The name may also be modified, in which case arcname could be a dummy string.




TarFile.addfile(tarinfo, fileobj=None)
TarFile.extractfile(member)
  :: member/(filename|TarInfo) -> may fileobj{regular file|link}/io.BufferedReader | ^KeyError@non_existed

TarFile.add(name, arcname=None, recursive=True, *, filter=None)
TarFile.extract(member, path='', set_attrs=True, *, numeric_owner=False, filter=None)
TarFile.extractall(path='.', members=None, *, numeric_owner=False, filter=None)

view ../../python3_src/seed/for_libs/for_tarfile.py
py_adhoc_call  { -end4print }  seed.for_libs.for_tarfile   @str.read_solo_tarfile_  :script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma  --xencoding4data:ascii
py_adhoc_call  { -end4print }  seed.for_libs.for_tarfile   ,str.iter_read_solo_tarfile_  :script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma  --xencoding4data:ascii

]]












xxx:py_adhoc_call   seed.for_libs.for_tarfile   @read_solo_tarfile_  :script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma  --kwds4open_tarfile='dict(encoding="ascii")'
py_adhoc_call  { -end4print }  seed.for_libs.for_tarfile   @str.read_solo_tarfile_  :script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma  --xencoding4data:ascii

py_adhoc_call  { -end4print }  seed.for_libs.for_tarfile   ,str.iter_read_solo_tarfile_  :script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma  --xencoding4data:ascii

[[
源起:
view script/搜索冫最短加链长度.py
===
create:lzma:
tar --create --verbose --file=script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma  --lzma script/搜索冫最短加链长度.py..statistics.out.txt
tar -cvf script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma  --lzma script/搜索冫最短加链长度.py..statistics.out.txt

===
show:lzma:
tar --extract --verbose --file=script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma --to-stdout | more
tar -xvf script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma -O | more
    -C, --directory=DIR
tar -xf script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma -O | diff - script/搜索冫最短加链长度.py..statistics.out.txt -s
    Files - and script/搜索冫最短加链长度.py..statistics.out.txt are identical
py_adhoc_call  { -end4print }  seed.for_libs.for_tarfile   ,str.iter_read_solo_tarfile_  :script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma  --xencoding4data:ascii  | diff - script/搜索冫最短加链长度.py..statistics.out.txt -s


]]
[[
@20260216
源起:打包多个文件
===
1-16016完成@20260209晚八点
tar -cvf script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.out.txt.tar.lzma --lzma   script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part00*.out.txt
tar -xf script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py..枚举生成冫文件后续简并记录纟递归婪溟链扌.ver2.part-1-2-3-4.1-16016.out.txt.tar.lzma -O | head -n 6019 | tail -n +6016 | more
===
测试:
mkdir $my_tmp/test
mkdir $my_tmp/test/tar
mkdir $my_tmp/test/tar/c-d/

echo -n $'123\nabc\n...' >  $my_tmp/test/tar/a.txt
echo -n $'999\n666\n' >  $my_tmp/test/tar/b.txt
echo -n $'\n' >  $my_tmp/test/tar/c-d/c.txt
echo -n $'' >  $my_tmp/test/tar/c-d/d.txt
tree $my_tmp/test/tar/

tar -cvf $my_tmp/test/a-b-c-d.txt.tar.lzma --lzma   -C $my_tmp/test/tar/  a.txt b.txt c-d/c.txt c-d/d.txt
tar -tf $my_tmp/test/a-b-c-d.txt.tar.lzma
tar -xf $my_tmp/test/a-b-c-d.txt.tar.lzma -O
    123
    abc
    ...999
    666
    <BLANK>

du -b $my_tmp/test/a-b-c-d.txt.tar.lzma
    191
hexdump $my_tmp/test/a-b-c-d.txt.tar.lzma

rm -iv $my_tmp/test/a-b-c-d.txt.tar.lzma

#>>> from pathlib import Path
#>>> p = Path('/sdcard/0my_files/tmp/test/a-b-c-d.txt.tar.lzma')
#>>> bs = p.read_bytes()
#>>> len(bs)
#191
#>>> bs.hex(':', -4).upper()
>>> hex_str = ('5D000080:00FFFFFF:FFFFFFFF:FF00308B:8A87C40E:F297A4F8:7540BA02:ABBB6CD9:CFB7DC2F:8BB90662:416B9C75:D9744603:5DD8B610:94FAE819:1F4CCC76:366CB468:BD7BD819:54185245:BE0C4935:C0E64277:34106ABF:46C053B9:0F8E7511:A3BAB40D:00746AAE:E7377A3E:AAB87C6D:D1F8D482:9127EB1E:67BA9F04:B58FEF3A:A2CF3260:1FE44F1F:3C1CCCD0:0627EA73:815380CF:131B12CC:A0AE2A29:AF8A89DA:156D57AD:0E9FF231:AD4BED25:6FE64D7D:97EC833C:6DB5D0EE:F2C98BD8:AC44FFE1:B6A8D6')
>>> bs = bytes.fromhex(hex_str.replace(':', ''))
>>> import tarfile
>>> from io import BytesIO, TextIOWrapper
>>> ibfile = BytesIO(bs)
>>> ifile4tar = tarfile.open(fileobj=ibfile)
>>> for tarinfo8member in ifile4tar:
...     print(tarinfo8member)  #doctest: +ELLIPSIS
<TarInfo 'a.txt' at 0x...>
<TarInfo 'b.txt' at 0x...>
<TarInfo 'c-d/c.txt' at 0x...>
<TarInfo 'c-d/d.txt' at 0x...>
>>> for tarinfo8member in ifile4tar:
...     print(tarinfo8member)  #doctest: +ELLIPSIS
<TarInfo 'a.txt' at 0x...>
<TarInfo 'b.txt' at 0x...>
<TarInfo 'c-d/c.txt' at 0x...>
<TarInfo 'c-d/d.txt' at 0x...>
>>> ifile4tar is iter(ifile4tar)
False

>>> for tarinfo8member in ifile4tar:
...     print(f'@{tarinfo8member.name!r}')
...     with ifile4tar.extractfile(tarinfo8member) as ifile4data, TextIOWrapper(ifile4data, encoding='ascii') as ifile:
...         for line in ifile:
...             print(repr(line))
@'a.txt'
'123\n'
'abc\n'
'...'
@'b.txt'
'999\n'
'666\n'
@'c-d/c.txt'
'\n'
@'c-d/d.txt'


>>> ibfile.seek(0)
0
>>> for line in iter_chain_read_multi_tarfile_(ibfile, xencoding4data='ascii', required_newline=False):
...     print(repr(line))
'123\n'
'abc\n'
'...'
'999\n'
'666\n'
'\n'
>>> for line in iter_chain_read_multi_tarfile_(ibfile, xencoding4data='', required_newline=False):
...     print(repr(line))
>>> ibfile.seek(0)
0
>>> for line in iter_chain_read_multi_tarfile_(ibfile, xencoding4data='', required_newline=False):
...     print(repr(line))
b'123\n'
b'abc\n'
b'...'
b'999\n'
b'666\n'
b'\n'
>>> ibfile.seek(0)
0
>>> for line in iter_chain_read_multi_tarfile_(ibfile, xencoding4data='ascii'):
...     print(repr(line))
Traceback (most recent call last):
    ...
seed.for_libs.for_tarfile.Error__line_not_endswith_newline
>>> for line in iter_chain_read_multi_tarfile_(ibfile, xencoding4data=''):
...     print(repr(line))
>>> ibfile.seek(0)
0
>>> for line in iter_chain_read_multi_tarfile_(ibfile, xencoding4data=''):
...     print(repr(line))
Traceback (most recent call last):
    ...
seed.for_libs.for_tarfile.Error__line_not_endswith_newline

===
>>> ibfile1 = BytesIO(bs)
>>> ibfile2 = BytesIO(bs)
>>> for line in iter_chain_read_multi_tarfiles_(ibfile1, ibfile2, xencoding4data='ascii', required_newline=False):
...     print(repr(line))
'123\n'
'abc\n'
'...'
'999\n'
'666\n'
'\n'
'123\n'
'abc\n'
'...'
'999\n'
'666\n'
'\n'
>>> ibfile1.seek(0)
0
>>> ibfile2.seek(0)
0
>>> for line in iter_chain_read_multi_tarfiles_(ibfile1, ibfile2, xencoding4data='ascii'):
...     print(repr(line))
Traceback (most recent call last):
    ...
seed.for_libs.for_tarfile.Error__line_not_endswith_newline
>>> for line in iter_chain_read_multi_tarfiles_(ibfile1, ibfile2, xencoding4data=''):
...     print(repr(line))
Traceback (most recent call last):
    ...
seed.for_libs.for_tarfile.Error__line_not_endswith_newline

===
]]
[[
ifile4tar donot auto close ibfile, no optional way to do it...
>>> ibfile = BytesIO(bs)
>>> ibfile.tell()
0
>>> ifile4tar = tarfile.open(fileobj=ibfile)
>>> ibfile.closed
False
>>> ibfile.tell()
191
>>> ifile4tar.close()
>>> ibfile.closed
False
>>> ibfile.tell()
191
>>> ibfile.close()
>>> ibfile.closed
True
>>> ibfile.tell()
Traceback (most recent call last):
    ...
ValueError: I/O operation on closed file.


>>> ibfile = BytesIO(bs)
>>> ifile4tar = tarfile.open(ibfile)
Traceback (most recent call last):
    ...
TypeError: expected str, bytes or os.PathLike object, not BytesIO

]]




]]]'''#'''
__all__ = r'''
double_open_solo_tarfile_
    group_open_solo_tarfile_
read_solo_tarfile_
    iter_read_solo_tarfile_
iter_chain_read_multi_tarfile_
    iter_chain_read_multi_tarfiles_


fmts4compression4read
mk_mode4read_tarfile_
distinguish5may_ipath_or_ifile_

mk_echo_or_wrap_

Error
    Error__not_solo_tarfile
    Error__line_not_endswith_newline
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import tarfile
import sys
from io import TextIOWrapper, BufferedReader
from seed.tiny_.check import check_type_is, check_type_le
from seed.tiny_.null_dev import null_context
from seed.for_libs.for_contextlib import GroupContextManager
___end_mark_of_excluded_global_names__0___ = ...
fmts4compression4read = ('*', '', 'gz', 'bz2', 'xz')
class Error(Exception):pass
class Error__not_solo_tarfile(Error):pass
class Error__line_not_endswith_newline(Error):pass

def distinguish5may_ipath_or_ifile_(may_ipath_or_ifile, /):
    ipath_or_ifile = sys.stdin if may_ipath_or_ifile is None else may_ipath_or_ifile

    may_ipath = None
    may_ifile = None
    if hasattr(ipath_or_ifile, 'readable'):
        ifile = ipath_or_ifile
        may_ifile = ifile
    else:
        ipath = ipath_or_ifile
        may_ipath = ipath
    return (may_ipath, may_ifile)

def mk_mode4read_tarfile_(may_fmt4compression4read, /):
    fmt4compression4read = '*' if may_fmt4compression4read is None else may_fmt4compression4read
    check_type_is(str, fmt4compression4read)
    assert fmt4compression4read in fmts4compression4read
    mode4read_tarfile = f'r:{fmt4compression4read}'
    return mode4read_tarfile

def mk_echo_or_wrap_(xencoding4data, /):
    if xencoding4data:
        # str
        encoding4data = xencoding4data
        check_type_is(str, encoding4data)
        def echo_or_wrap_(ifile4data, /):
            # [ifile4data :: BufferedReader]
            ifile4text = TextIOWrapper(ifile4data, encoding=encoding4data)
            # [ifile4text :: TextIOWrapper]
            return ifile4text
    else:
        # bytes
        def echo_or_wrap_(ifile4data, /):
            # [ifile4data :: BufferedReader]
            return ifile4data
    return echo_or_wrap_
def double_open_solo_tarfile_(may_ipath_or_ifile, may_fmt4compression4read=None, /, xencoding4data=None, *, kwds4open_tarfile={}, group=False):
    '-> ((ifile4tar, (ifile4data|ifile4text))|grp_ctx_mngr{(ifile4tar, ifile4data_or_ifile4text)})/(TarFile, (BufferedReader if not xencoding4data else TextIOWrapper) if not group else GroupContextManager)|^Error__not_solo_tarfile'
    return group_open_solo_tarfile_(may_ipath_or_ifile, may_fmt4compression4read, xencoding4data, kwds4open_tarfile=kwds4open_tarfile, not_group=not group)
def group_open_solo_tarfile_(may_ipath_or_ifile, may_fmt4compression4read=None, /, xencoding4data=None, *, kwds4open_tarfile={}, not_group=False):
    '-> ((ifile4tar, (ifile4data|ifile4text))|grp_ctx_mngr{(ifile4tar, ifile4data_or_ifile4text)})/(TarFile, (BufferedReader if not xencoding4data else TextIOWrapper) if not_group else GroupContextManager)|^Error__not_solo_tarfile'
    check_type_is(bool, not_group)
    ######################
    echo_or_wrap_ = mk_echo_or_wrap_(xencoding4data)
    (may_ipath, may_ifile) = distinguish5may_ipath_or_ifile_(may_ipath_or_ifile)
    mode4read_tarfile = mk_mode4read_tarfile_(may_fmt4compression4read)
    ######################

    ifile4tar = ifile4data = ifile4data_or_ifile4text = null_context
    try:
        ifile4tar = tarfile.open(may_ipath, mode4read_tarfile, may_ifile, **kwds4open_tarfile)
        check_type_is(tarfile.TarFile, ifile4tar)
        may_fst_tarinfo8member = ifile4tar.next()
        if may_fst_tarinfo8member is None: raise Error__not_solo_tarfile('empty tarfile')
        fst_tarinfo8member = may_fst_tarinfo8member
        if not None is (snd_member := ifile4tar.next()): raise Error__not_solo_tarfile('tarfile has more than one file')
            #snd_member

        solo_tarinfo8member = fst_tarinfo8member
        ifile4data = ifile4tar.extractfile(solo_tarinfo8member)
        check_type_le(BufferedReader, ifile4data)
        # [ifile4data :: BufferedReader]
        ifile4data_or_ifile4text = echo_or_wrap_(ifile4data)
            # [ifile4text :: TextIOWrapper]
        if not_group:
            return (ifile4tar, ifile4data_or_ifile4text)
        return GroupContextManager([ifile4tar, ifile4data_or_ifile4text])
    except:
        with ifile4tar, ifile4data, ifile4data_or_ifile4text:pass
        raise
    raise 000




def iter_read_solo_tarfile_(may_ipath_or_ifile, may_fmt4compression4read=None, /, xencoding4data=None, *, kwds4open_tarfile={}):
    '-> Iter line/(bytes if not xencoding4data else str)|^Error__not_solo_tarfile'
    grp_ctx_mngr = group_open_solo_tarfile_(may_ipath_or_ifile, may_fmt4compression4read, xencoding4data=xencoding4data, kwds4open_tarfile=kwds4open_tarfile)
    with grp_ctx_mngr as (ifile4tar, ifile4data_or_ifile4text):
        lines = iter(ifile4data_or_ifile4text)
        assert iter(lines) is lines
        #bug:return lines
        yield from lines

def read_solo_tarfile_(may_ipath_or_ifile, may_fmt4compression4read=None, /, xencoding4data=None, *, kwds4open_tarfile={}, _iter=False):
    '-> (bytes if not xencoding4data else str)|^Error__not_solo_tarfile'
    grp_ctx_mngr = group_open_solo_tarfile_(may_ipath_or_ifile, may_fmt4compression4read, xencoding4data=xencoding4data, kwds4open_tarfile=kwds4open_tarfile)
    with grp_ctx_mngr as (ifile4tar, ifile4data_or_ifile4text):
        # [ifile4data :: BufferedReader]
        # [ifile4text :: TextIOWrapper]
        bs_or_txt = ifile4data_or_ifile4text.read()
    check_type_is((bytes if not xencoding4data else str), bs_or_txt)
    return bs_or_txt

    ######################
    #.if xencoding4data:
    #.    # str
    #.    encoding4data = xencoding4data
    #.    check_type_is(str, encoding4data)
    #.    def read_(ifile4data, /):
    #.        # [ifile4data :: BufferedReader]
    #.        ifile4text = TextIOWrapper(ifile4data, encoding=encoding4data)
    #.        txt = ifile4text.read()
    #.        check_type_is(str, txt)
    #.        return txt
    #.else:
    #.    # bytes
    #.    def read_(ifile4data, /):
    #.        # [ifile4data :: BufferedReader]
    #.        bs = ifile4data.read()
    #.        check_type_is(bytes, bs)
    #.        return bs
    #.    read_
    #.read_

    #.(ifile4tar, ifile4data) = double_open_solo_tarfile_(may_ipath_or_ifile, may_fmt4compression4read, kwds4open_tarfile=kwds4open_tarfile)
    #.with ifile4tar, ifile4data:
    #.    bs_or_txt = read_(ifile4data)
    #.    #.bs = ifile4data.read()
    #.#.check_type_is(bytes, bs)
    #.#.if xencoding4data:
    #.#.    encoding4data = xencoding4data
    #.#.    txt = bs.decode(encoding4data)
    #.#.    return txt
    #.#.return bs
    #.check_type_is((bytes if not xencoding4data else str), bs_or_txt)
    #.return bs_or_txt


def iter_chain_read_multi_tarfile_(may_ipath_or_ifile, may_fmt4compression4read=None, /, xencoding4data=None, *, kwds4open_tarfile={}, required_newline=True):
    '-> Iter line/(bytes if not xencoding4data else str)|^Error__not_solo_tarfile'
    echo_or_wrap_ = mk_echo_or_wrap_(xencoding4data)
    (may_ipath, may_ifile) = distinguish5may_ipath_or_ifile_(may_ipath_or_ifile)
    mode4read_tarfile = mk_mode4read_tarfile_(may_fmt4compression4read)
    with tarfile.open(may_ipath, mode4read_tarfile, may_ifile, **kwds4open_tarfile) as ifile4tar:
        for tarinfo8member in ifile4tar:
            if not tarinfo8member.isfile():
                continue
            with ifile4tar.extractfile(tarinfo8member) as ifile4data, echo_or_wrap_(ifile4data) as ixfile:
                if not required_newline:
                    yield from ixfile
                else:
                    newline = '\n' if xencoding4data else b'\n'
                    for line in ixfile:
                        if not line[-1:] == newline:raise Error__line_not_endswith_newline
def iter_chain_read_multi_tarfiles_(*ls4may_ipath_or_ifile, may_fmt4compression4read=None, xencoding4data=None, kwds4open_tarfile={}, required_newline=True):
    '-> Iter line/(bytes if not xencoding4data else str)|^Error__not_solo_tarfile'
    for may_ipath_or_ifile in ls4may_ipath_or_ifile:
        yield from iter_chain_read_multi_tarfile_(may_ipath_or_ifile, may_fmt4compression4read, xencoding4data=xencoding4data, kwds4open_tarfile=kwds4open_tarfile, required_newline=required_newline)

__all__
from seed.for_libs.for_tarfile import double_open_solo_tarfile_, group_open_solo_tarfile_, read_solo_tarfile_, iter_read_solo_tarfile_
from seed.for_libs.for_tarfile import iter_chain_read_multi_tarfile_, iter_chain_read_multi_tarfiles_
from seed.for_libs.for_tarfile import *
