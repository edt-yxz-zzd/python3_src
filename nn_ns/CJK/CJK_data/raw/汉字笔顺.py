r"""

py -m nn_ns.CJK.CJK_data.raw.汉字笔顺
e ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺.py
view ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺表[20200913]/stroke-seq_MB-master[汉字笔顺表][20200827]/单字_笔顺码_29685个.txt
#"""



__all__ = '''
    汉字到笔顺码
    汉字到笔顺码囗囗未打补丁囗囗包含已知错误
    '''.split()






##section##
r"""
import io
import re
from seed.tiny import print_err
#"""

from seed.io.iter_row_based_Z_delimited_text_file import iter_TSV__path
from types import MappingProxyType #frozenset
#xxx:from seed.mapping_tools.SandBoxDict import SandBoxDict

def __():
    def iter_TSV__path(path, *, encoding, case='path', **kw):
        r"-> Iter ((line_number, raw_line, line_content), parts)"
    def iter_row_based_Z_delimited_text_file_(input, *, sep, case:'stream|path|data', encoding, skip_empty_lines=False, skip_space_lines=False, line_number_offset=0, smay_comment_prefix='', turnon__tail_comment=False):
        ...



##section##
class Globals:
    import nn_ns.CJK.CJK_data.raw as raw
    from pathlib import Path
    [raw_path] = raw.__path__
    data_dir_path = Path(raw_path) / r"汉字笔顺表[20200913]/stroke-seq_MB-master[汉字笔顺表][20200827]/"
    笔顺_TSV_path = data_dir_path / r"单字_笔顺码_29685个.txt"
    sz_before_patch = 29685
        #tab
    错误_SSV_path = data_dir_path / r"my_found_bugs.txt"
    补丁_SSV_path = data_dir_path / r"my_patch.py.out.txt"
        #space
    手动补丁_SSV_path = data_dir_path / r"my_patch_ex.txt"
        #『:』
    r"""
    #"""
    # /sdcard/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺表[20200913]/stroke-seq_MB-master[汉字笔顺表][20200827]/单字_笔顺码_29685个.txt
    # /storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺表[20200913]/stroke-seq_MB-master[汉字笔顺表][20200827]/my_patch.py.out.txt

_s=set("𠂇𠂉𠃌𡗗𢦏𤇾")
#def _read_ex(笔顺_TSV_path, sz_before_patch, 错误_SSV_path, 补丁_SSV_path, 手动补丁_SSV_path):
def _read(笔顺_TSV_path, sz_before_patch, 错误_SSV_path, 补丁_SSV_path, 手动补丁_SSV_path):
    it2 = _iter_read_2(错误_SSV_path)
    it1 = _iter_read_1(补丁_SSV_path)
    it3 = _iter_read_3(手动补丁_SSV_path)

    ########
    d0 = dict(_iter_read_0(笔顺_TSV_path))
    assert len(d0) == sz_before_patch
    #xxx:d = SandBoxDict(d0)
    d = {**d0}
    #d = d0


    ########
    for ch, bug_ds, true_ds in it2:
        if ch in d:
            if d[ch] != bug_ds: raise ValueError
            assert true_ds != bug_ds
            d[ch] = true_ds
    ########
    def f(a,b):
        if a in d:
            x = d[a]
            if b not in d:
                d[b] = x
            y = d[b]
            if x != y:
                raise ValueError(f"d[{a!r}]=={x!r}!={y!r}==d[{b!r}]")

    ########
    s=set()
    for pua_ch, std_ch in it1:
        #if std_ch in d: print(std_ch)
        if std_ch in d: s.add(std_ch)
        f(pua_ch, std_ch)
        f(std_ch, pua_ch)
    assert s == _s

    ########
    assert len(d) == 80-len(_s)+Globals.sz_before_patch
    ########
    for 部件名, 笔顺码 in it3:
        js = d.setdefault(部件名, 笔顺码)
        if not js == 笔顺码:
            raise ValueError((部件名, js, 笔顺码))

    return d0, d
    ########
    #xxx:(dels, updates) = d.summary__dels__updates_()
    ########
    #xxx:d = {**d}
    #xxx:return (d, (dels, updates))
#end-def _read(笔顺_TSV_path, sz_before_patch, 错误_SSV_path, 补丁_SSV_path, 手动补丁_SSV_path):

def _iter_read_3(手动补丁_SSV_path):
    it = iter_TSV__path(手动补丁_SSV_path, sep=':', encoding='utf8', smay_comment_prefix='#')
    for _, parts in it:
        [bks, js] = parts
        bks = bks.split('=')
        for bk in bks:
            yield bk, js

def _iter_read_2(错误_SSV_path):
    it = iter_TSV__path(错误_SSV_path, sep=' ', encoding='utf8')
    for _, parts in it:
        [ch_pt, bug_ds, true_ds] = parts
        ch = ch_pt[0]
        assert bug_ds[0] == '!'
        assert true_ds[0] == '='
        yield ch, bug_ds[1:], true_ds[1:]

def _iter_read_1(补丁_SSV_path):
    it = iter_TSV__path(补丁_SSV_path, sep=' ', encoding='utf8')
    for _, parts in it:
        [pua, std, gb] = parts
        pua_ch = pua[0]
        std_ch = std[0]
        yield pua_ch, std_ch
def _iter_read_0(笔顺_TSV_path):
    it = iter_TSV__path(笔顺_TSV_path, encoding='utf8')
    for _, parts in it:
        [汉字, 笔顺码, _] = parts
        assert len(汉字) == 1
        assert ord(汉字) > 0x3000
        assert len(笔顺码)
        assert all('1' <= d <= '5' for d in 笔顺码)
        yield 汉字, 笔顺码


def _main():
    #(d, (dels, updates)) = _read_ex(Globals.笔顺_TSV_path, Globals.sz_before_patch, Globals.错误_SSV_path, Globals.补丁_SSV_path, Globals.手动补丁_SSV_path)
    #assert not dels, dels
    #TODO:save to file....auto gen...
    d0, d = _read(Globals.笔顺_TSV_path, Globals.sz_before_patch, Globals.错误_SSV_path, Globals.补丁_SSV_path, Globals.手动补丁_SSV_path)
    return MappingProxyType(d0), MappingProxyType(d)
[汉字到笔顺码囗囗未打补丁囗囗包含已知错误
,汉字到笔顺码
] = _main()
assert len(汉字到笔顺码囗囗未打补丁囗囗包含已知错误) == Globals.sz_before_patch
assert len(汉字到笔顺码) >= Globals.sz_before_patch
#print(len(汉字到笔顺码) - Globals.sz_before_patch)
#:assert len(汉字到笔顺码) == 80-len(_s)+Globals.sz_before_patch
assert len(汉字到笔顺码) >= 80-len(_s)+Globals.sz_before_patch




from nn_ns.CJK.CJK_data.raw.汉字笔顺 import 汉字到笔顺码
from nn_ns.CJK.CJK_data.raw.汉字笔顺 import 汉字到笔顺码囗囗未打补丁囗囗包含已知错误
from nn_ns.CJK.CJK_data.raw.汉字笔顺 import *

if 0:
    from nn_ns.CJK.CJK_data.汉字笔顺 import 汉字到笔顺码
