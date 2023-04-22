#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/CJK/CJK_common/化繁为简.py

'line_fmt<繁简对照表> = "" | f"{繁简同体词}:" | f"{繁体词}:{简体词}"'





nn_ns.CJK.CJK_common.化繁为简
py -m nn_ns.app.debug_cmd   nn_ns.CJK.CJK_common.化繁为简 -x
py -m nn_ns.app.doctest_cmd nn_ns.CJK.CJK_common.化繁为简:__doc__ -ff -v
from nn_ns.CJK.CJK_common.化繁为简 import 化繁为简囗囗词囗


ipath=/sdcard/0my_files/tmp/out4py/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
ipath='../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt'
ipath4table=/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-词汇繁简对照-补空.txt

py_adhoc_call   nn_ns.CJK.CJK_common.化繁为简   @化繁为简囗囗文件路径囗 --encoding:u8 +是否输出囗繁简对照表  --路径囗输入囗繁简对照表:"$ipath4table"   --路径囗输入囗繁体词:"$ipath"   --路径囗输出=None =8
nn_ns.CJK.CJK_common.化繁为简.FormatError__len_not_eq: len not eq: '背光性' : '背旋光性'

py_adhoc_call   nn_ns.CJK.CJK_common.化繁为简   @化繁为简囗囗文件路径囗 --encoding:u8 +是否输出囗繁简对照表  --路径囗输入囗繁简对照表:"$ipath4table"   --路径囗输入囗繁体词:"$ipath"   --路径囗输出=None +discard_bad_line_in_table  =8
阿那:
阿熱:阿热
阿史德:
阿史那:
哀:
敳:
藹:蔼
艾:


opath=/sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗繁简对照表..欧路词典.汉语大辞典.姓氏提取.out.txt
py_adhoc_call   nn_ns.CJK.CJK_common.化繁为简   @化繁为简囗囗文件路径囗 --encoding:u8 +是否输出囗繁简对照表  --路径囗输入囗繁简对照表:"$ipath4table"   --路径囗输入囗繁体词:"$ipath"  +discard_bad_line_in_table  --路径囗输出:"$opath"
nn_ns.CJK.CJK_common.化繁为简.TranslationError__lookup: 幺

view ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt

py_adhoc_call   nn_ns.CJK.CJK_common.化繁为简   @化繁为简囗囗文件路径囗 --encoding:u8 +是否输出囗繁简对照表  --路径囗输入囗繁简对照表:"$ipath4table"   --路径囗输入囗繁体词:"$ipath"  +discard_bad_line_in_table  --路径囗输出:"$opath" +print_instead_raise_on_translate_fail
化繁为简:失败: '幺'

view /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗繁简对照表..欧路词典.汉语大辞典.姓氏提取.out.txt
么:
:幺
枚:

py_adhoc_call   nn_ns.CJK.CJK_common.化繁为简   @化繁为简囗囗文件路径囗 --encoding:u8 +是否输出囗繁简对照表 --路径囗输入囗繁简对照表:"$ipath4table"   --路径囗输入囗繁体词:"$ipath"  +discard_bad_line_in_table  --路径囗输出:"$opath" --may_fallback_table='dict(幺="幺")' +force
    ok!
view /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗繁简对照表..欧路词典.汉语大辞典.姓氏提取.out.txt
么:
幺:
枚:



opath=/sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗简体版..欧路词典.汉语大辞典.姓氏提取.out.txt
py_adhoc_call   nn_ns.CJK.CJK_common.化繁为简   @化繁为简囗囗文件路径囗 --encoding:u8 -是否输出囗繁简对照表 --路径囗输入囗繁简对照表:"$ipath4table"   --路径囗输入囗繁体词:"$ipath"  +discard_bad_line_in_table  --路径囗输出:"$opath" --may_fallback_table='dict(幺="幺")'
view /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗简体版..欧路词典.汉语大辞典.姓氏提取.out.txt
么
幺
枚

cp -t ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/   /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗繁简对照表..欧路词典.汉语大辞典.姓氏提取.out.txt   /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗简体版..欧路词典.汉语大辞典.姓氏提取.out.txt


#]]]'''
__all__ = r'''
BaseTranslationError
    BaseTranslationError__bug_at_lookup_table
    TranslationError
        TranslationError__lookup

BaseFormatError
    FormatError
        FormatError__len_not_eq
        FormatError__contains_bad_char


check_word_
check_繁简双词囗

mk_line_content4繁简对照表
lines_parser4繁简对照表

读取囗繁简对照表囗

化繁为简囗囗词囗
    囗化繁为简囗囗词囗
化繁为简囗囗文件路径囗

'''.split()#'''
__all__


from collections import ChainMap
from itertools import islice


from seed.iters.iter_split_rngs import iter_ok_rngs_if_, iter_split_rngs_if_, iter_split_blocks5seq_if_, split_blocks5seq_if_
from nn_ns.CJK.CJK_common.is_hz import is_hz__tribool_, partition_charset_by_is_hz_
from seed.recognize.cmdline.txt_process import main, line_filter
#def main(nm4subcmd_or_subcmd, /, *args, may_ipath, encoding, may_opath=None, oencoding=..., force=False, may_smay_newline4in='', may_smay_newline4out='', **kw):
from seed.io.may_open import open4wt, open4wt_err, open4rt
from seed.io.fielded_line_utils import lines_handler2txt_handler, fielded_lines_parserT__tuple, fielded_lines_preprocesserT, lines_preprocesserT
from seed.tiny import curry1, expectError, print_err, ifNone, check_bool
from nn_ns.CJK.cjk_subsets.hanzi import 平凡繁简囗共享汉字字集
from nn_ns.CJK.CJK_data.汉字繁简 import (
    简繁字对集
        ,繁体字到简体字串
        ,简体字到繁体字串
    )

assert all(hz == 繁体字到简体字串[hz] == 简体字到繁体字串[hz] for hz in 平凡繁简囗共享汉字字集)

_us4known_trivial_hzs = frozenset(map(ord, 平凡繁简囗共享汉字字集))
def _is_known_trivial_hz(hz, /):
    r'''-> bool #True=>trivial; False=>unknown-yet
    #只考虑 平凡自反，不考虑 唯一可逆
    #只考虑 常见汉字，不考虑 所有汉字
    '''#'''
    return ord(hz) in _us4known_trivial_hzs

class BaseTranslationError(Exception):pass
class BaseTranslationError__bug_at_lookup_table(BaseTranslationError):pass
class TranslationError(BaseTranslationError):pass
class TranslationError__lookup(TranslationError):pass

class BaseFormatError(Exception):pass
class FormatError(BaseFormatError):pass
class FormatError__len_not_eq(FormatError):pass
class FormatError__contains_bad_char(FormatError):pass



def 读取囗繁简对照表囗(路径囗输入囗繁简对照表, /, *, encoding, discard_bad_line_in_table):
    'line_fmt<繁简对照表> = "" | f"{繁简同体词}:" | f"{繁体词}:{简体词}"'
    lines_parser4繁简对照表
    check_bool(discard_bad_line_in_table)
    #iter_TSV__path(path, *, encoding, case='path', **kw)
    with open4rt(路径囗输入囗繁简对照表, encoding=encoding) as ifile:
        lines = iter(ifile)
        #lines = islice(lines, 100)
        ps = lines_parser4繁简对照表(lines, discard_bad_line=discard_bad_line_in_table)
        繁简对照表 = dict(ps)
    return 繁简对照表
def lines_parser4繁简对照表(lines, /, *, discard_bad_line):
    check_bool(discard_bad_line)
    ps = _lines_parser4繁简对照表(lines)
    ps = ((繁体词, smay_简体词 if smay_简体词 else 繁体词) for 繁体词,smay_简体词 in ps)
    if discard_bad_line:
        ps = ((繁体词, 简体词) for (繁体词, 简体词) in ps if not expectError(FormatError, lambda:check_繁简双词囗(繁体词, 简体词)))
    else:
        ps = ((繁体词, 简体词) for (繁体词, 简体词) in ps if check_繁简双词囗(繁体词, 简体词) or 1)
    return ps

_lines_parser4繁简对照表 = fielded_lines_parserT__tuple(':', '#', [str, str], keep_space_lines=False, keep_bifix_spaces4field=False)

def check_word_(词, /):
    if ':' in 词: raise FormatError__contains_bad_char(f'should not contain ":": {词!r}')
    if '\n' in 词: raise FormatError__contains_bad_char(rf'should not contain "\n": {词!r}')
    if '\r' in 词: raise FormatError__contains_bad_char(rf'should not contain "\r": {词!r}')
def check_繁简双词囗(繁体词, 简体词, /):
    check_word_(繁体词)
    check_word_(简体词)
    if not len(简体词) == len(繁体词): raise FormatError__len_not_eq(f'len not eq: {繁体词!r} : {简体词!r}')

def mk_line_content4繁简对照表(繁体词, 简体词, /):
    'line_fmt<繁简对照表> = "" | f"{繁简同体词}:" | f"{繁体词}:{简体词}"'
    check_繁简双词囗(繁体词, 简体词)
    if not 繁体词:
        line_content = ''
    else:
        smay_简体词 = '' if 简体词 == 繁体词 else 简体词
        line_content = f"{繁体词}:{smay_简体词}"
    return line_content








def _to_set_if_len_ge(L, xs, /):
    if len(xs) >= L:
        xs = frozenset(xs)
    return xs
_to_set_if_len_ge16 = curry1(_to_set_if_len_ge, 16)


def 囗化繁为简囗囗词囗(繁简对照表, 繁体词, /):
    '-> 简体词 | ^TranslationError__lookup | ^BaseTranslationError__bug_at_lookup_table # [len(简体词) == len(繁体词)]'
    ###ver1:?bug?:will reduce into char tranlate
    #       not-bug if 繁简对照表 contains only bijection
    L = len(繁体词)
    ls = []
    while 繁体词:
        简体词 = ''

        for i in range(len(繁体词), 0, -1):
            assert i
            if 繁体词[:i] in 繁简对照表:
                简体词 = 繁简对照表[繁体词[:i]]
            elif i==1:
                [hz] = 繁体词[:i]
                if _is_known_trivial_hz(hz):
                    简体词 = hz
            if 简体词:
                if not len(简体词) == i: raise BaseTranslationError__bug_at_lookup_table(繁体词[:i], 简体词)
                ls.append(简体词)
                繁体词 = 繁体词[i:]
                break
        else:
            raise TranslationError__lookup(繁体词)
    assert not 繁体词
    简体词 = ''.join(ls)
    assert len(简体词) == L
    return 简体词


def 化繁为简囗囗词囗(繁简对照表, 繁体词, /):
    '-> 简体词 | ^TranslationError__lookup | ^BaseTranslationError__bug_at_lookup_table # [len(简体词) == len(繁体词)]'
    check_word_(繁体词)
    is_hz__tribool_
    (cs4unknown, cs4noncjk, cs4cjk) = partition_charset_by_is_hz_(繁体词)
    (cs4unknown, cs4noncjk, cs4cjk) = map(_to_set_if_len_ge16, (cs4unknown, cs4noncjk, cs4cjk))
    if cs4unknown: raise ValueError(cs4unknown)
    ws = split_blocks5seq_if_(cs4cjk.__contains__, 繁体词)
    繁体词列表 = ws[1::2]
    ls = []
    for 囗繁体词 in 繁体词列表:
        简体词 = 囗化繁为简囗囗词囗(繁简对照表, 囗繁体词)
        ls.append(简体词)
    ws[1::2] = ls
    简体词 = ''.join(ws)

    check_word_(简体词)
    assert len(简体词) == len(繁体词)
    return 简体词

def 化繁为简囗囗文件路径囗(*args4islice4out,  是否输出囗繁简对照表, 路径囗输入囗繁简对照表, 路径囗输入囗繁体词, 路径囗输出, encoding, oencoding=..., iencoding4table=..., force=False, may_smay_newline4in='', may_smay_newline4out='', flush4println=True, discard_bad_line_in_table=False, print_instead_raise_on_translate_fail=False, may_fallback_table=None):
    'line_fmt<繁简对照表> = "" | f"{繁简同体词}:" | f"{繁体词}:{简体词}"'
    #路径囗输入囗繁简对照表=/sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-词汇繁简对照-补空.txt
    fallback_table = ifNone(may_fallback_table, {})
    check_bool(print_instead_raise_on_translate_fail)
    check_bool(是否输出囗繁简对照表)

    def f(繁体词, /):
        简体词 = 化繁为简囗囗词囗(繁简对照表, 繁体词)
        line_content = mk_line_content4繁简对照表(繁体词, 简体词) if 是否输出囗繁简对照表 else 简体词
        return line_content
    if print_instead_raise_on_translate_fail:
        g = f
        def f(繁体词, /):
            try:
                line_content = g(繁体词)
            except TranslationError:
                print_err(f'化繁为简:失败: {繁体词!r}')
                line_content = f':{繁体词}' if 是否输出囗繁简对照表 else f':::{繁体词}:::'
            return line_content
    def row_processor(繁体词_smay_newline, /):
        '-> (smay_line_content, smay_newline)'
        繁体词, smay_newline = 繁体词_smay_newline
        line_content = f(繁体词)
        return line_content, smay_newline #end4println=''
        #...return line_content #end4println='\n'
    end4println=''

    if iencoding4table is ...:
        iencoding4table = encoding
    繁简对照表 = 读取囗繁简对照表囗(路径囗输入囗繁简对照表, encoding=iencoding4table, discard_bad_line_in_table=discard_bad_line_in_table)
    if fallback_table:
        繁简对照表 = ChainMap(繁简对照表, fallback_table)

    return main('line_filter', *args4islice4out, cased_func_or_args4islice__eithers=[(3, row_processor)], may_ipath=路径囗输入囗繁体词, may_opath=路径囗输出, encoding=encoding, oencoding=oencoding, force=force, may_smay_newline4in=may_smay_newline4in, may_smay_newline4out=may_smay_newline4out, end4println=end4println, flush4println=flush4println, without_last_line_if_empty=True, may_fmt4out=None)
#def main(nm4subcmd_or_subcmd, /, *args, may_ipath, encoding, may_opath=None, oencoding=..., force=False, may_smay_newline4in='', may_smay_newline4out='', **kw):
#def line_filter(*args4islice4out, cased_func_or_args4islice__eithers, ifile, ofile, may_smay_newline4in, end4println='', flush4println=True, without_last_line_if_empty=True, may_fmt4out=None):






from nn_ns.CJK.CJK_common.化繁为简 import 化繁为简囗囗词囗
from nn_ns.CJK.CJK_common.化繁为简 import *
