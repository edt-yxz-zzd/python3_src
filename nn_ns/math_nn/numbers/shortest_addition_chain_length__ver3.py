#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length__ver3.py
    [1..=7322932]#七百万#百倍于16爻元/七万
=>:
    view ../../python3_src/seed/math/power/addition_chain/data/get_target_uint2may_len_optimal_addition_chain_.py
        from seed.math.power.addition_chain.data.get_target_uint2may_len_optimal_addition_chain_ import 取冫靶值讠最小显链长扌, 靶值讠最小显链长扌
        靶值讠最小显链长 = 取冫靶值讠最小显链长扌()
vs:
    view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length.py
        静态加载:100000
    view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length__ver2.py
        惰性完整加载:7320000
    view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length__ver3.py
        动态逐项加载:7322932


nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3
py -m nn_ns.app.debug_cmd   nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3 -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3:__doc__ -ht # -ff -df
#######
[[
copy_from:view script/解读冫二进制文件冃靶值讠最小显链长.py
===
py_adhoc_call   seed.io.decompress_truncated_file   @count_uncompression_bytes4truncated_compression_file_ :bz2 :ipath :'../../python3_src/nn_ns/math_nn/numbers/偏移值二爻冃靶值讠最小显链长.le7320000.le7322932[add31.bits-中断].bz2'
    =>:1830733
#no:cp -iv /sdcard/0my_files/unzip/addition_chain/add31.bits-靶值首爻位小于三十一牜不完整.dat '../../python3_src/nn_ns/math_nn/numbers/偏移值二爻冃靶值讠最小显链长.le7320000[add31.bits-中断].dat'
stat /sdcard/0my_files/unzip/addition_chain/add31.bits-靶值首爻位小于三十一牜不完整.dat
    =>:1830000 bytes
py.bz2解压实测:
    =>:1830733 bytes
du -h /sdcard/0my_files/tmp/wget_/wwwhomes.uni-bielefeld.de/achim/add31.bits.bz2
  820K#中断
cp -iv /sdcard/0my_files/tmp/wget_/wwwhomes.uni-bielefeld.de/achim/add31.bits.bz2  '../../python3_src/nn_ns/math_nn/numbers/偏移值二爻冃靶值讠最小显链长.le7320000.le7322932[add31.bits-中断].bz2'

e ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length__ver3.py

]]
[[
]]


'#'; __doc__ = r'#'

>>> from timeit import timeit
>>> from nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3 import 取冫靶值讠最小显链长扌
>>> timeit(取冫靶值讠最小显链长扌, number=1)      #doctest: +SKIP
0.5353498458862305
0.29044192284345627
0.37970361299812794

>>> (7322932).bit_length()
23
>>> 2**22 < 7322932 < 2**23
True
>>> 2**16
65536
>>> 7322932/65536
111.73907470703125
>>> 靶值讠最小显链长 = 取冫靶值讠最小显链长扌()
>>> len(靶值讠最小显链长)
7322933
>>> 靶值讠最小显链长[7322932]
28
>>> 靶值讠最小显链长[1+7322932]
Traceback (most recent call last):
    ...
IndexError: range object index out of range
>>> 靶值讠最小显链长[0] is None
True
>>> 靶值讠最小显链长[-1]
28

>>> 靶值讠最小显链长[:31]
(None, 0, 1, 2, 2, 3, 3, 4, 3, 4, 4, 5, 4, 5, 5, 5, 4, 5, 5, 6, 5, 6, 6, 6, 5, 6, 6, 6, 6, 7, 6)

>>> 靶值讠最小显链长扌(7322932)
28
>>> 靶值讠最小显链长扌(1+7322932)
Traceback (most recent call last):
    ...
IndexError: range object index out of range
>>> 靶值讠最小显链长扌(0)
Traceback (most recent call last):
    ...
TypeError: 0
>>> 靶值讠最小显链长扌(-1)
Traceback (most recent call last):
    ...
TypeError: -1



>>> 靶值讠最小显链长
P.nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3().取冫靶值讠最小显链长扌()
>>> from seed.types.Symbol import P
>>> 靶值讠最小显链长 is eval(repr(靶值讠最小显链长))
True

py_adhoc_call   '' @str   %%:P  ='P.nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3().取冫靶值讠最小显链长扌()[12509]'
    =>『'17'』
py_adhoc_call   '' @str   %%:P  ='P.nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3().取冫靶值讠最小显链长扌()'
    =>『'P.nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3().取冫靶值讠最小显链长扌()'』


[[
py_adhoc_call   nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3   @打印冫最小显链长灬巛靶值灬扌 =12 =13 =781 =12509
<==>:
szmm4shortest_addition_chain 12 13  781  12509
==>>:
    [ℓ(12) == 4]
    [ℓ(13) == 5]
    [ℓ(781) == 12]
    [ℓ(12509) == 17]

]]
[[
py_adhoc_call   nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3   @打印冫最小总小步数灬巛靶值灬扌 =12 =13 =781 =12509 =17010 =18030 =18146 =18180
<==>:
num_small_steps4shortest_addition_chain 12 13  781  12509  17010  18030  18146  18180
==>>:
[ℓ(12) == 4][s(12) == 1]
[ℓ(13) == 5][s(13) == 2]
[ℓ(781) == 12][s(781) == 3]
[ℓ(12509) == 17][s(12509) == 4]
[ℓ(17010) == 18][s(17010) == 4]
[ℓ(18030) == 18][s(18030) == 4]
[ℓ(18146) == 18][s(18146) == 4]
[ℓ(18180) == 18][s(18180) == 4]

]]



]]]'''#'''
__all__ = r'''
取冫靶值讠最小显链长扌
    靶值讠最小显链长扌
枚举冫最小显链长灬巛靶值灬扌
    打印冫最小显链长灬巛靶值灬扌
枚举冫最小总小步数灬巛靶值灬扌
    打印冫最小总小步数灬巛靶值灬扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge
if 1:from nn_ns.math_nn.numbers.shortest_addition_chain_length__ver2 import _解读冫编码值讠最小显链长纟靶值扌
    #def _解读冫编码值讠最小显链长纟靶值扌(靶值, 编码值, /):
___end_mark_of_excluded_global_names__0___ = ...
def 打印冫最小总小步数灬巛靶值灬扌(*列表纟靶值, ofmt=r'[ℓ({靶值}) == {最小显链长}][s({靶值}) == {最小总小步数}]'):
    for 靶值, 最小显链长, 最小总小步数 in 枚举冫最小总小步数灬巛靶值灬扌(*列表纟靶值, 欤带靶值辻最小显链长=True):
        s = ofmt.format(靶值=靶值, 最小显链长=最小显链长, 最小总小步数=最小总小步数)
        print(s)
    #e ../../python3_src/bash_script/app/num_small_steps4shortest_addition_chain
def 枚举冫最小总小步数灬巛靶值灬扌(*列表纟靶值, 欤带靶值辻最小显链长=False):
    from seed.math.power.addition_chain.common.properties import 小步数纟
    靶值讠最小显链长 = 取冫靶值讠最小显链长扌()
    for 靶值 in 列表纟靶值:
        check_int_ge(1, 靶值)
        最小显链长 = 靶值讠最小显链长[靶值]
        最小总小步数 = 小步数纟(靶值, 最小显链长)
        yield (靶值, 最小显链长, 最小总小步数) if 欤带靶值辻最小显链长 else 最小总小步数





def 打印冫最小显链长灬巛靶值灬扌(*列表纟靶值, ofmt=r'[ℓ({靶值}) == {最小显链长}]'):
    for 靶值, 最小显链长 in 枚举冫最小显链长灬巛靶值灬扌(*列表纟靶值, 欤带靶值=True):
        s = ofmt.format(靶值=靶值, 最小显链长=最小显链长)
        print(s)
    #e ../../python3_src/bash_script/app/szmm4shortest_addition_chain
def 枚举冫最小显链长灬巛靶值灬扌(*列表纟靶值, 欤带靶值=False):
    靶值讠最小显链长 = 取冫靶值讠最小显链长扌()
    for 靶值 in 列表纟靶值:
        check_int_ge(1, 靶值)
        最小显链长 = 靶值讠最小显链长[靶值]
        yield (靶值, 最小显链长) if 欤带靶值 else 最小显链长

def 靶值讠最小显链长扌(靶值, /):
    check_int_ge(1, 靶值)
    return 取冫靶值讠最小显链长扌()[靶值]

if 0:
    _靶值讠最小显链长 = ...
def 取冫靶值讠最小显链长扌():
    try:
        return _靶值讠最小显链长
    except NameError:
        pass
    _加载冫靶值讠最小显链长扌()
    return 取冫靶值讠最小显链长扌()
def _加载冫靶值讠最小显链长扌():
    global _靶值讠最小显链长
    from pathlib import Path
    path4pkg = Path(__file__).parent
    basename = '偏移值二爻冃靶值讠最小显链长.le7320000.le7322932[add31.bits-中断].bz2'
    ipath = path4pkg / basename
    sz = 1830733
    _靶值讠最小显链长 = _构造冫靶值讠最小显链长扌(sz, ipath)
    assert len(_靶值讠最小显链长) == 1+4*sz == 1+7322932 == 7322933
    return
def _构造冫靶值讠最小显链长扌(sz, ipath, /):
    from seed.types.LazyDict8Array import mk_LazyDict8Array_ex_ex_, mk_LazyDict_ex_ex_, Dict8Array
    #def mk_LazyDict8Array_ex_ex_(sz, may_mapping, ncall, value_mkr, /, *ex_args):
    bs = _读冫字节串巛断尾压缩包扌(sz, ipath)
    靶值讠最小显链长 = mk_LazyDict8Array_ex_ex_(1+4*sz, {0:None}, 1, _靶值讠最小显链长扌, bs, smay_repr='P.nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3().取冫靶值讠最小显链长扌()')
            #see:from seed.types.Symbol import P
    return 靶值讠最小显链长
def _读冫字节串巛断尾压缩包扌(sz, ipath, /):
    import bz2
    bs = bytearray(sz)
    with bz2.open(ipath) as ibfile:
        ibfile.seek(0)
        _sz = ibfile.readinto(bs)
        if not _sz == sz:raise Exception(sz, _sz)
        try:
            ibfile.read(1)
        except EOFError:
            #EOFError: Compressed file ended before the end-of-stream marker was reached
            pass
        else:
            raise Exception(f'有效字节数 多于 {sz}')
    return bytes(bs)
def _靶值讠最小显链长扌(靶值, bs, /):
    assert 靶值 >= 1
    u = 靶值 - 1
    #(offset4bytes, half_offset4bits) = divmod(u, 4)
    offset4bytes = u>>2
    #half_offset4bits = u&0b011
    offset4bits = (u&0b011) << 1
    编码值 = 0b011 & (bs[offset4bytes] >> offset4bits)
    最小显链长纟靶值 = _解读冫编码值讠最小显链长纟靶值扌(靶值, 编码值)
    return 最小显链长纟靶值


__all__
from nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3 import 取冫靶值讠最小显链长扌, 靶值讠最小显链长扌
from nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3 import *
