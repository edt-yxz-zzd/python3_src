
r"""

py -m nn_ns.CJK.CJK_data.raw.汉字笔顺
e ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺.py
view ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺表[20200913]/stroke-seq_MB-master[汉字笔顺表][20200827]/单字_笔顺码_29685个.txt
#"""



__all__ = '''
    汉字到笔顺码
    '''.split()






##section##
r"""
import io
import re
from seed.tiny import print_err
#"""

from seed.io.iter_row_based_Z_delimited_text_file import iter_TSV__path
from types import MappingProxyType #frozenset




##section##
class Globals:
    import nn_ns.CJK.CJK_data.raw as raw
    from pathlib import Path
    [raw_path] = raw.__path__
    笔顺_TSV_path = Path(raw_path) / r"汉字笔顺表[20200913]/stroke-seq_MB-master[汉字笔顺表][20200827]/单字_笔顺码_29685个.txt"
    r"""
    #"""
    # /sdcard/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺表[20200913]/stroke-seq_MB-master[汉字笔顺表][20200827]/单字_笔顺码_29685个.txt

def _read(笔顺_TSV_path):
    return dict(_iter_read(笔顺_TSV_path))
def _iter_read(笔顺_TSV_path):
    it = iter_TSV__path(笔顺_TSV_path, encoding='utf8')
    for _, parts in it:
        [汉字, 笔顺码, _] = parts
        assert len(汉字) == 1
        assert ord(汉字) > 0x3000
        assert len(笔顺码)
        assert all('1' <= d <= '5' for d in 笔顺码)
        yield 汉字, 笔顺码

汉字到笔顺码 = MappingProxyType(_read(Globals.笔顺_TSV_path))
assert len(汉字到笔顺码) == 29685




