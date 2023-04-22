
r"""

py -m nn_ns.CJK.CJK_data.raw.汉字繁简
e ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字繁简.py
view ../../python3_src/nn_ns/CJK/CJK_data/output/parse_繁简.py.out/简繁.txt



bug:
'bug:包含:  ․˙‥¨′＇═〓「“」”『‘』’〞″䊷䌶'
bug:包含:\u25A1
    'name': 'WHITE SQUARE'
    9633 == 0x25A1

grep $'\u25A1' -r '../../python3_src/nn_ns/CJK/CJK_data/raw/繁简转换[20200913]/' -l
../../python3_src/nn_ns/CJK/CJK_data/raw/繁简转换[20200913]/funNLP-master/fanjian_suoyin.txt
    只有一个文件

view ../../python3_src/nn_ns/CJK/CJK_data/raw/繁简转换[20200913]/funNLP-master/fanjian_suoyin.txt
搜索:
/\%u25a1

xxx并非gbk view ++enc=gbk ../../python3_src/nn_ns/CJK/CJK_data/raw/繁简转换[20200913]/funNLP-master/fanjian_suoyin.txt


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

from nn_ns.CJK.CJK_common.is_hz import is_hz__tribool_, partition_charset_by_is_hz_
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

#简繁字对集 = frozenset(_read(Globals.简繁_TSV_path))
#   'bug:包含:  ․˙‥¨′＇═〓「“」”『‘』’〞″䊷䌶'
_简繁字对集 = frozenset(_read(Globals.简繁_TSV_path))

简繁字对集 = frozenset(TS for TS in _简繁字对集 if all(is_hz__tribool_(ch) is True for ch in TS))
_unknown_pairs = frozenset(TS for TS in _简繁字对集 if not all(type(is_hz__tribool_(ch)) is bool for ch in TS))
_nonhz_pairs = _简繁字对集 -简繁字对集 -_unknown_pairs
if 0b0:
    print(_unknown_pairs)
    print(_nonhz_pairs)
    print(len(_unknown_pairs))
    print(len(_nonhz_pairs))
assert len(_unknown_pairs) == 1
assert len(_nonhz_pairs) == 2912
assert _unknown_pairs == frozenset({'□\ue5f1'})
assert frozenset({'□鴹', '□騹', '□餹', '□鐹', '□錹', '□輹', '□鵸', '□齸'}) < _nonhz_pairs
_nonhz_pairs_1 = {ab for ab in _nonhz_pairs if ab[0]=='\u25A1'}
_nonhz_pairs_2 = {ab for ab in _nonhz_pairs if not ab[0]=='\u25A1'}
if 0b0:
    print(_nonhz_pairs_1)
    print(_nonhz_pairs_2)
    print(len(_nonhz_pairs_1))
    print(len(_nonhz_pairs_2))

assert len(_nonhz_pairs_1) == 2893
assert len(_nonhz_pairs_2) == 19
assert _nonhz_pairs_2 == {'眺※', '”」', '．•', '″〞', '’』', '鹮□', '翻※', '刾□', '鳚□', '菱※', '＇′', '鲃□', '“「', '〓═', '¨‥', '‘『', '．‧', '˙․', '鳤□'}
assert _nonhz_pairs_2 > {'”」', '．•', '″〞', '’』', '＇′', '“「', '〓═', '¨‥', '‘『', '．‧', '˙․'}
assert not '․˙‥¨′＇═〓「“」”『‘』’〞″' == ''.join(sorted(ab[::-1] for ab in {'”」', '．•', '″〞', '’』', '＇′', '“「', '〓═', '¨‥', '‘『', '．‧', '˙․'}))
assert  '•．․˙‥¨‧．′＇═〓「“」”『‘』’〞″' == ''.join(sorted(ab[::-1] for ab in {'”」', '．•', '″〞', '’』', '＇′', '“「', '〓═', '¨‥', '‘『', '．‧', '˙․'}))

繁体字到简体字串 = MappingProxyType(_mk_繁体字到简体字串(简繁字对集))
简体字到繁体字串 = MappingProxyType(_mk_简体字到繁体字串(简繁字对集))








