#__all__:goto
r'''[[[
e ../../python3_src/seed/io/line_index_file.py
    行索引文件
    构造冫行索引文件扌

seed.io.line_index_file
py -m nn_ns.app.debug_cmd   seed.io.line_index_file -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.io.line_index_file:__doc__ -ht # -ff -df
#######

[[
源起:
view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__six_lists.py
]]

[[
[line_index_file =[def]= (header, body)]
[header =[def]= (NUM_BYTES4WORD{==4}/u32LE, num_lines/u32LE)]
[body =[def]= line_gap_addrs/[u32LE]{len==1+num_lines}]
[line_gap_addrs == [0]++line_end_addrs == line_begin_addrs++[num_bytes4ibfile]]

]]
cat /data/data/com.termux/files/usr/lib/python3.11/tarfile.py

[[
echo -n $'999\n666\n' >  $my_tmp/test/tar/b.txt
tar -cvf $my_tmp/test/b.txt.tar.lzma --lzma   -C $my_tmp/test/tar/  b.txt
tar -tf $my_tmp/test/b.txt.tar.lzma
tar -xf $my_tmp/test/b.txt.tar.lzma -O
    999
    666

du -b $my_tmp/test/b.txt.tar.lzma
    143
hexdump $my_tmp/test/b.txt.tar.lzma

rm -iv $my_tmp/test/b.txt.tar.lzma

#>>> from pathlib import Path
#>>> p = Path('/sdcard/0my_files/tmp/test/b.txt.tar.lzma')
#>>> bs = p.read_bytes()
#>>> len(bs)
#143
#>>> bs.hex(':', -4).upper()
>>> hex_str = ('5D000080:00FFFFFF:FFFFFFFF:FF00310B:8A87C40E:F297A4F8:7540BA02:ABBB6CD9:CFB7DC2F:8BB9066C:C0C3BFEC:303844BC:57AF4E4C:8CC88F57:5ACB05A6:67B34A86:57D32584:6D7F1C11:E646C48C:F3E85800:71DF0D9E:33D04AEC:1E8D7A21:0B83A02E:FA77C561:64920A32:0E8834C3:1315A0A4:68EB2C23:EA93068B:FB463CEE:76EFA7A9:11E9E0CB:0A32BC85:84EAFFEF:8DD240')
>>> bs = bytes.fromhex(hex_str.replace(':', ''))
>>> import tarfile
>>> from io import BytesIO, TextIOWrapper
>>> ibfile = BytesIO(bs)
>>> len(ibfile.getvalue())
143
>>> ifile4tar = tarfile.open(fileobj=ibfile)
>>> for tarinfo8member in ifile4tar:
...     print(tarinfo8member)  #doctest: +ELLIPSIS
<TarInfo 'b.txt' at 0x...>
>>> for tarinfo8member in ifile4tar:
...     print(tarinfo8member)  #doctest: +ELLIPSIS
<TarInfo 'b.txt' at 0x...>
>>> ifile4tar is iter(ifile4tar)
False

>>> for tarinfo8member in ifile4tar:
...     print(f'@{tarinfo8member.name!r}')
...     with ifile4tar.extractfile(tarinfo8member) as ifile4data, TextIOWrapper(ifile4data, encoding='ascii') as ifile:
...         for line in ifile:
...             print(repr(line))
@'b.txt'
'999\n'
'666\n'


>>> len(ibfile.getvalue())
143
>>> ibfile.seek(0)
0





>>> ibfile = BytesIO(b'999\n666\n')
>>> obfile = BytesIO()
>>> mk_line_index_file__bfile_(ibfile, obfile)
>>> obfile.getvalue().hex(':', -4).upper()
'04000000:02000000:00000000:04000000:08000000'
>>> obfile.seek(0)
0
>>> ls = LineIndexArray__utf8__eval(cache:={0:None}, offset4lineno:=1, ibfile7line_index:=obfile, ibfile7data:=ibfile, smay_repr='ls')
>>> ls
ls
>>> obfile.seek(0)
0
>>> ls = LineIndexArray__utf8__eval(cache:={0:None}, offset4lineno:=1, ibfile7line_index:=obfile, ibfile7data:=ibfile, smay_repr='')
>>> ls  #doctest: +ELLIPSIS
LineIndexArray__utf8__eval({0: None}, 1, <_io.BytesIO object at 0x...>, <_io.BytesIO object at 0x...>)
>>> len(ls)
3
>>> ls[0]
>>> cache
{0: None}
>>> ls[1]
999
>>> cache
{0: None, 1: 999}
>>> ls[2]
666
>>> cache
{0: None, 1: 999, 2: 666}
>>> obfile.close()
>>> ibfile.close()
>>> ls[:]
(None, 999, 666)
>>> cache.clear()
>>> ls[0]
Traceback (most recent call last):
    ...
LookupError: 0
>>> cache
{}
>>> ls[1]
Traceback (most recent call last):
    ...
ValueError: I/O operation on closed file.




def double_open_solo_tarfile_(may_ipath_or_ifile, may_fmt4compression4read=None, /, xencoding4data=None, *, kwds4open_tarfile={}, group=False):
>>> from seed.for_libs.for_tarfile import double_open_solo_tarfile_
>>> ibfile = BytesIO(bs)

#>>> ifile4tar = tarfile.open(fileobj=ibfile)
>>> (ifile4tar, ibfile4data) = double_open_solo_tarfile_(ibfile)
>>> obfile = BytesIO()
>>> mk_line_index_file__bfile_(ibfile4data, obfile)
>>> obfile.getvalue().hex(':', -4).upper()
'04000000:02000000:00000000:04000000:08000000'
>>> obfile.seek(0)
0
>>> ls = LineIndexArray__utf8__eval(cache:={0:None}, offset4lineno:=1, ibfile7line_index:=obfile, ibfile7data:=ibfile4data, smay_repr='')
>>> ls  #doctest: +ELLIPSIS
LineIndexArray__utf8__eval({0: None}, 1, <_io.BytesIO object at 0x...>, <ExFileObject name=None>)
>>> ls[2]
666
>>> ls[:]
(None, 999, 666)


du -bh ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__six_lists.py..尾六表纟简并记录纟递归婪溟链.ver2.le35035.txt.tar.lzma
    1.5M
du -bh ../../python3_src/nn_ns/math_nn/numbers/_ignore__tmp/shortest_addition_chain__six_lists.py..尾六表纟简并记录纟递归婪溟链.ver2.le35035.txt.idx
    137K

solo_tarfile
LineIndexArray__tiny_solo_tarfile__utf8__eval(may_cache, offset4lineno, iopath7line_index, ipath7data6tiny_solo_tarfile, /, *, smay_repr='')
see:
    view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__six_lists.py
#.>>> ipath7data6tiny_solo_tarfile = '../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__six_lists.py..尾六表纟简并记录纟递归婪溟链.ver2.le35035.txt.tar.lzma'
#.>>> iopath7line_index = '../../python3_src/nn_ns/math_nn/numbers/_ignore__tmp/shortest_addition_chain__six_lists.py..尾六表纟简并记录纟递归婪溟链.ver2.le35035.txt.idx'
#.>>> ls = LineIndexArray__tiny_solo_tarfile__utf8__eval(cache:={0:None}, offset4lineno:=1, iopath7line_index, ipath7data6tiny_solo_tarfile, smay_repr='')
#.>>> ls
#.LineIndexArray__tiny_solo_tarfile__utf8__eval({0: None}, 1, PosixPath('../../python3_src/nn_ns/math_nn/numbers/_ignore__tmp/shortest_addition_chain__six_lists.py..尾六表纟简并记录纟递归婪溟链.ver2.le35035.txt.idx'), PosixPath('../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__six_lists.py..尾六表纟简并记录纟递归婪溟链.ver2.le35035.txt.tar.lzma'))
#.>>> ls[35035]
#.(35035, [1, 2, 3, 4, 6, 11, 19, 31, 47, 91, 182, 271, 539, 1078, 2156, 4095, 7315, 11739, 17519, 35035], [1, 2, 4, 8, 16, 32, 64, 128, 256, 384, 544, 1088, 2176, 4352, 8704, 9240, 16640, 30800, 35032, 35035], [1, 2, 3, 4, 7, 11, 22, 44, 47, 91, 182, 364, 728, 1456, 2912, 5824, 11648, 11739, 23296, 35035], [1, 2, 4, 8, 16, 32, 64, 128, 256, 384, 385, 770, 1540, 3080, 6160, 9240, 9625, 19250, 28875, 35035], [1, 2, 3, 4, 8, 16, 32, 64, 128, 256, 259, 515, 1030, 2060, 2319, 4379, 8758, 17516, 17519, 35035], [1, 2, 3, 4, 8, 16, 32, 64, 128, 256, 259, 515, 1030, 2060, 4120, 4379, 8758, 17516, 35032, 35035])
#.
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.io.line_index_file   @f
]]]'''#'''
__all__ = r'''
ILineIndexArray
    LineIndexArray__raw_bytes
    LineIndexArray__utf8__eval
    LineIndexArray

    ILineIndexArray__tiny_solo_tarfile
        LineIndexArray__tiny_solo_tarfile__utf8__eval

mk_line_index_file__bfile_
mk_line_index_file__ibfile_opath_
mk_line_index_file__path_

NUM_BYTES4WORD
write_uint32_LE_
write_uint_LE_
read_bytes__len_eq_
read_uint_LE_
read_uint32_LE_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
from io import SEEK_END
from seed.tiny_.check import check_type_is, check_int_ge
from collections.abc import Sequence
from abc import abstractmethod
#.#################################
#.def mk_context4lazy_import_registered_names_(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject={}, may_bifix4lazy_name7import=None, lazy_name7importZoriginal_name7import={}):
#.from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
#.with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
#.    from seed._lazy_ import print_err, fst, echo, ifNone
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

NUM_BYTES4WORD = 4
def mk_line_index_file__bfile_(ibfile, obfile):
    if not 0 == ibfile.tell():raise Exception
    if not 0 == obfile.tell():raise Exception

    #header:
    write_uint32_LE_(obfile, NUM_BYTES4WORD)
    777;oaddr = obfile.tell()
    777;write_uint32_LE_(obfile, num_lines:=0)

    #body:
    begin = ibfile.tell()
    777;write_uint32_LE_(obfile, begin)
    for num_lines, line in enumerate(ibfile, 1):
        if not line[-1:] == b'\n':raise Exception(num_lines, line)
        end = ibfile.tell()
        write_uint32_LE_(obfile, end)
            #^OverflowError
        #begin = end
    #patch:header:
    777;oend = obfile.tell()
    777;obfile.seek(oaddr)
    777;write_uint32_LE_(obfile, num_lines)
    777;obfile.seek(oend)
    assert oaddr == NUM_BYTES4WORD
    assert oend == NUM_BYTES4WORD*(2  +  1+num_lines)
    assert oend == 8 + 4*(1+num_lines)
    return


def mk_line_index_file__ibfile_opath_(ibfile, opath, *, exist_ok):
    try:
        obfile = open(opath, 'xb')
    except FileExistsError:
        if exist_ok:
            return
        raise
    with obfile:
        mk_line_index_file__bfile_(ibfile, obfile)
def mk_line_index_file__path_(ipath, opath, *, exist_ok):
    #.with open(ipath, 'rb') as ibfile, open(opath, 'xb') as obfile:
    #.    mk_line_index_file__bfile_(ibfile, obfile)
    with open(ipath, 'rb') as ibfile:
        mk_line_index_file__ibfile_opath_(ibfile, opath, exist_ok=exist_ok)


def write_uint32_LE_(obfile, u32, /):
    write_uint_LE_(4, obfile, u32)
        #^OverflowError
    return
def write_uint_LE_(num_bytes4uint, obfile, u, /):
    bs = u.to_bytes(num_bytes4uint, 'little')
        #^OverflowError
    obfile.write(bs)
    return
def read_bytes__len_eq_(num_bytes, ibfile, /):
    bs = ibfile.read(num_bytes)
    if not len(bs) == num_bytes:raise EOFError
    return bs
def read_uint_LE_(num_bytes4uint, ibfile, /):
    bs = read_bytes__len_eq_(num_bytes4uint, ibfile)
    u = int.from_bytes(bs, 'little')
    return u
def read_uint32_LE_(ibfile, /):
    return read_uint_LE_(4, ibfile)


#.from seed.types.LazyDict8Array import mk_LazyDict8Array_ex_ex_, mk_LazyDict_ex_ex_, Dict8Array
#.def mk_LazyDict8Array_ex_ex_(sz, may_mapping, ncall, value_mkr, /, *ex_args, smay_repr=''):
#.    'sz/uint -> may d/{k:v} -> ncall/(imay uint%3) -> (case ncall of {-1=>v; 0=>((*ex_args)->v); 1=>(k -> (*ex_args) -> v); 2=>(LazyDict{k:v} -> k -> (*ex_args) -> v);}) -> (*ex_args) -> LazyDict8Array{j:v}'
class ILineIndexArray(Sequence):
    def __init__(sf, may_cache, offset4lineno, ibfile7line_index, ibfile7data, /, *, smay_repr=''):
        check_type_is(str, smay_repr)
        if not (may_cache is None or hasattr(may_cache, '__setitem__') and hasattr(may_cache, 'keys')):raise TypeError
        check_int_ge(0, offset4lineno)
        if not (offset4lineno == 0 or not None is (cache:=may_cache) and len(cache) >= offset4lineno):raise TypeError
        if not 0 == ibfile7line_index.tell():raise Exception
        _NUM_BYTES4WORD = read_uint32_LE_(ibfile7line_index)
        if not _NUM_BYTES4WORD == NUM_BYTES4WORD:raise Exception
        num_lines = read_uint32_LE_(ibfile7line_index)
        iaddr4body = ibfile7line_index.tell()
        ibfile7line_index.seek(0, SEEK_END)
        777;iaddr4end = ibfile7line_index.tell()
        if not iaddr4end == iaddr4body + NUM_BYTES4WORD*(1+num_lines) == 8+4*(1+num_lines):raise Exception
        sf._ibfile7line_index = ibfile7line_index
        sf._ibfile7data = ibfile7data
        sf._offset = iaddr4body
        sf._num_lines = num_lines
        sf._may_cache = may_cache
        sf._offset4lineno = offset4lineno
        sf._sz = offset4lineno+num_lines
        sf._smay_repr = smay_repr
        sf._args4repr = (may_cache, offset4lineno, ibfile7line_index, ibfile7data)
    def __repr__(sf, /):
        if sf._smay_repr:
            return sf._smay_repr
        nm = type(sf).__name__
        args = sf._args4repr
        return f'{nm}{args}'
    def __len__(sf, /):
        return sf._sz
    def __getitem__(sf, lineno_or_linenos, /):
        lineno_or_linenos = range(len(sf))[lineno_or_linenos]
        if type(lineno_or_linenos) is range:
            linenos = lineno_or_linenos
            return tuple(map(sf.at, linenos))
        lineno = lineno_or_linenos
        return sf.at(lineno)
    def at(sf, lineno, /):
        check_int_ge(0, lineno)
        may_cache = sf._may_cache
        if not None is (cache:=may_cache) and lineno in cache.keys():
            return cache[lineno]

        j = lineno - sf._offset4lineno
        if not j >= 0:raise LookupError(lineno)
        ibfile7line_index = sf._ibfile7line_index
        ibfile7data = sf._ibfile7data
        iaddr = sf._offset + j*NUM_BYTES4WORD
        ibfile7line_index.seek(iaddr)
        777;begin = read_uint32_LE_(ibfile7line_index)
        777;end = read_uint32_LE_(ibfile7line_index)
        num_bytes4line = end - begin
        777;ibfile7data.seek(begin)
        777;bs8line = read_bytes__len_eq_(num_bytes4line, ibfile7data)
        value = sf._eval_bytes8line_(lineno, bs8line)
        if not None is (cache:=may_cache):
            cache[lineno] = value
        return value
    @abstractmethod
    def _eval_bytes8line_(sf, lineno, bs8line, /):
        'lineno{>=0} -> bytes{endswith(b"\n")} -> value'
        raise NotImplementedError
class LineIndexArray__raw_bytes(ILineIndexArray):
    #@override
    def _eval_bytes8line_(sf, lineno, bs8line, /):
        return bs8line
class LineIndexArray__utf8__eval(ILineIndexArray):
    #@property
    _locals_ = None#{}
    #@override
    def _eval_bytes8line_(sf, lineno, bs8line, /):
        return eval(bs8line.decode('u8'), None, sf._locals_)
class LineIndexArray(ILineIndexArray):
    def __init__(sf, _eval_bytes8line_, may_cache, offset4lineno, ibfile7line_index, ibfile7data, /, *, smay_repr=''):
        super().__init__(may_cache, offset4lineno, ibfile7line_index, ibfile7data, smay_repr=smay_repr)
        sf._args4repr = (_eval_bytes8line_, may_cache, offset4lineno, ibfile7line_index, ibfile7data)
        sf._eval = _eval_bytes8line_
    #@override
    def _eval_bytes8line_(sf, lineno, bs8line, /):
        return sf._eval(lineno, bs8line)

class ILineIndexArray__tiny_solo_tarfile(ILineIndexArray):
    def __init__(sf, may_cache, offset4lineno, iopath7line_index, ipath7data6tiny_solo_tarfile, /, *, smay_repr=''):
        from io import BytesIO
        from pathlib import Path
        from seed.for_libs.for_tarfile import double_open_solo_tarfile_
        ipath7data6tiny_solo_tarfile = Path(ipath7data6tiny_solo_tarfile)
        iopath7line_index = Path(iopath7line_index)
        ibfile7tar = BytesIO(ipath7data6tiny_solo_tarfile.read_bytes())
        (ifile4tar, ibfile7data) = double_open_solo_tarfile_(ibfile7tar)
        if not iopath7line_index.exists():
            mk_line_index_file__ibfile_opath_(ibfile7data, iopath7line_index, exist_ok=False)
        ibfile7line_index = BytesIO(iopath7line_index.read_bytes())
        super().__init__(may_cache, offset4lineno, ibfile7line_index, ibfile7data, smay_repr=smay_repr)
        sf._args4repr = (may_cache, offset4lineno, iopath7line_index, ipath7data6tiny_solo_tarfile)
class LineIndexArray__tiny_solo_tarfile__utf8__eval(LineIndexArray__utf8__eval, ILineIndexArray__tiny_solo_tarfile):pass


__all__
from seed.io.line_index_file import mk_line_index_file__bfile_, mk_line_index_file__ibfile_opath_, mk_line_index_file__path_
    #mk_line_index_file__bfile_(ibfile, obfile)

from seed.io.line_index_file import ILineIndexArray, LineIndexArray__raw_bytes, LineIndexArray__utf8__eval, LineIndexArray
    #LineIndexArray(_eval_bytes8line_, may_cache, offset4lineno, ibfile7line_index, ibfile7data, /, *, smay_repr='')
from seed.io.line_index_file import ILineIndexArray__tiny_solo_tarfile, LineIndexArray__tiny_solo_tarfile__utf8__eval
    #LineIndexArray__tiny_solo_tarfile__utf8__eval(may_cache, offset4lineno, iopath7line_index, ipath7data6tiny_solo_tarfile, /, *, smay_repr='')
from seed.io.line_index_file import *
