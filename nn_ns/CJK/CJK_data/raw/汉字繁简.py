
r"""

py -m nn_ns.CJK.CJK_data.raw.汉字繁简
e ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字繁简.py
view ../../python3_src/nn_ns/CJK/CJK_data/output/parse_繁简.py.out/简繁.txt

#"""



__all__ = '''
    简繁字对集
        繁体字到简体字串
        简体字到繁体字串
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
    简繁_TSV_path = Path(raw_path) / r"../output/parse_繁简.py.out/简繁.txt"
    r"""
    #"""

def _read(简繁_TSV_path):
    return set(_iter_read(简繁_TSV_path))
def _iter_read(简繁_TSV_path):
    it = iter_TSV__path(简繁_TSV_path, encoding='utf8')
    for _, parts in it:
        [简繁] = parts
        [简, 繁] = 简繁
        yield 简繁

def _mk_繁体字到简体字串(简繁字对集):
    it = ((繁, 简) for 简, 繁 in 简繁字对集)
    return _mk_x2ys(it)
def _mk_简体字到繁体字串(简繁字对集):
    it = ((简, 繁) for 简, 繁 in 简繁字对集)
    return _mk_x2ys(it)
def _mk_x2ys(xy_iter):
    x2ys = {}
    for x, y in xy_iter:
        ys = x2ys.setdefault(x, [])
        ys.append(y)
    x2ys = {x:"".join(sorted(ys)) for x, ys in x2ys.items()}
    return x2ys

简繁字对集 = frozenset(_read(Globals.简繁_TSV_path))
繁体字到简体字串 = MappingProxyType(_mk_繁体字到简体字串(简繁字对集))
简体字到繁体字串 = MappingProxyType(_mk_简体字到繁体字串(简繁字对集))








