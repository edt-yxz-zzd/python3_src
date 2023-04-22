#__all__
r'''
e ../../python3_src/nn_ns/CJK/CJK_struct/cjk_decomp_0_4_0/read_cjk_decomp.py

def iter_read_cjk_decomp(ifile, /):
    '-> Iter (hanzi|uint|nm8bk, (case, [(hanzi|uint|nm8bk)]))'

hz = 汉字 :: char
js = 笔顺码
bk = 部件 =:
    | uint  #部件数字代号
    | hz    #汉字字符
    | nm8bk #部件人工名 :: str # f'[{nm}]'
check_bk(bk)


[[
===原文件行格式
33238:wt(中,99697)
做:a(亻,故)
冏:a([无钩冂自部首⺆],㕣)
===改变行格式再排序:之后:
wt,中!33238:wt(中,99697)
a,亻!做:a(亻,故)
a,⺆!冏:a([无钩冂自部首⺆],㕣)
]]


[[
改变行格式再排序
===
view others/app/gvim/sort_lines.txt
排序:改变 行格式，再排序
部件:字型布局(部件...)
  -> 字型布局,可选首部件!部件:字型布局(部件...)
  ==>> 更新:line_pattern:hanzi_or_num_pattern->hanzi_or_num_or_nm8bk__pattern
vim循环下列命令:
:%s/\([^:]*\):\([^(]*\)(\([^,)]*\)/\2,\3!\0
:%sort
:%s/^[^!]*!//
]]




nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp
py -m nn_ns.app.debug_cmd   nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp -x
py -m nn_ns.app.doctest_cmd nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp:__doc__ -ff -v





py -m nn_ns.app.debug_cmd   nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp

from nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp import default_iter_read_cjk_decomp

from nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp import bk5str, check_bk, check_nm8bk

from nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp import default_iter_read_cjk_decomp, iter_read_cjk_decomp

from nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp import default_iter_read_a_d, iter_read_a_d, iter_read_a_d_from_iter

from nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp import load_default, diff__bk2f_bks_, patch__bk2f_bks_














ls /sdcard/0my_files/tmp/backup_tmp/ -1
cjk-decomp-0.4.0-原版.txt
cjk-decomp-0.4.0.txt
单字_笔顺码_29685个-原版.txt
单字_笔顺码_29685个.txt

view ../../python3_src/nn_ns/CJK/CJK_struct/cjk_decomp_0_4_0/cjk-decomp-0.4.0.txt
    已将 编辑中的版本 与 原版 备份到:
        /sdcard/0my_files/tmp/backup_tmp/
    原目录下，只保留 原版 并改回原名
py_adhoc_call nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp @diff__ipath_ --encoding:u8 --ipath4old:/sdcard/0my_files/tmp/backup_tmp/cjk-decomp-0.4.0-原版.txt  --ipath4new:../../python3_src/nn_ns/CJK/CJK_struct/cjk_decomp_0_4_0/cjk-decomp-0.4.0.txt
{}
    #ok!




py_adhoc_call nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp @diff__ipath_ --encoding:u8 --ipath4old:/sdcard/0my_files/tmp/backup_tmp/cjk-decomp-0.4.0-原版.txt  --ipath4new:/sdcard/0my_files/tmp/backup_tmp/cjk-decomp-0.4.0.txt
    ...很多不同...

def main4diff_(*, ipath4old, ipath4new, may_opath4patch, encoding, force):
def main4patch_(*, ipath4old, ipath4patch, may_opath4new, encoding, force=False):

!mkdir script/hz/patchs4cjk-decomp-0.4.0.txt/
py_adhoc_call nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp @main4diff_ --encoding:u8 --ipath4old:/sdcard/0my_files/tmp/backup_tmp/cjk-decomp-0.4.0-原版.txt  --ipath4new:/sdcard/0my_files/tmp/backup_tmp/cjk-decomp-0.4.0.txt --may_opath4patch:script/hz/patchs4cjk-decomp-0.4.0.txt/patch-20230422-cjk-decomp-0.4.0.txt

py_adhoc_call nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp @main4patch_ --encoding:u8 --ipath4old:/sdcard/0my_files/tmp/backup_tmp/cjk-decomp-0.4.0-原版.txt --ipath4patch:script/hz/patchs4cjk-decomp-0.4.0.txt/patch-20230422-cjk-decomp-0.4.0.txt  --may_opath4new:/sdcard/0my_files/tmp/out4py/tmp.diff+patch-20230422.cjk-decomp-0.4.0.txt
view /sdcard/0my_files/tmp/out4py/tmp.diff+patch-20230422.cjk-decomp-0.4.0.txt
py_adhoc_call nn_ns.CJK.CJK_struct.cjk_decomp_0_4_0.read_cjk_decomp @diff__ipath_ --encoding:u8 --ipath4old:/sdcard/0my_files/tmp/out4py/tmp.diff+patch-20230422.cjk-decomp-0.4.0.txt --ipath4new:/sdcard/0my_files/tmp/backup_tmp/cjk-decomp-0.4.0.txt
{}
    #ok!


view script/hz/patchs4cjk-decomp-0.4.0.txt/patch-20230422-cjk-decomp-0.4.0.txt


'''#'''
__all__ = '''
    default_iter_read_cjk_decomp
    default_iter_read_a_d

    iter_read_cjk_decomp
    iter_read_a_d



line_rex
    line_pattern
        hanzi_or_num_or_nm8bk__pattern

bk5str
    check_bk
        check_nm8bk

default_iter_read_cjk_decomp
    iter_read_cjk_decomp

default_iter_read_a_d
    iter_read_a_d
        iter_read_a_d_from_iter

load_default
    diff__bk2f_bks_
    patch__bk2f_bks_





main4diff_
    diff__ipath_
        load_with_diff__ipaths_ex_
            load__ipath_
                load__ifile_

main4patch_
    patch__ipath_
        patch__ipath_ex_
    write_back_
        key4sort4bk

'''.split()
#__all__

import re
from seed.helper.stable_repr import stable_repr__expand_top_layer, stable_repr_print__expand_top_layer
from seed.io.may_open import open4wt, open4wt_err, open4rt
#def open4wt(may_opath, /, *, force, encoding):
#def open4rt(may_opath, /, *, encoding):
from seed.tiny import check_uint, mk_fprint
from seed.io.read_file_as_python_object import read_file_as_python_object
#def read_file_as_python_object(ipath, /, *, encoding, literal_eval_vs_safe_eval=False):
from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_
from seed.mapping_tools.dict_op import mapping_symmetric_diff4patch__immutable__default, mapping_symmetric_patch4lhs__immutable__default, mapping_symmetric_patch4rhs__immutable__default

def _():
    from pathlib import PurePath as Path
    this_file = Path(__file__)
    this_folder = this_file.parent
    this_file_name = this_file.name

class Global:
    ifname_modified = 'cjk-decomp-0.4.0.txt'
    ifname_old = 'cjk-decomp-0.4.0-原版.txt'
    #ipath = this_folder / ifname
    iencoding = 'utf8'

#hanzi_or_num_pattern = r'(?:\D|\d+)' # num is not unicode!!!!!
#line_pattern = fr'(?P<key>{hanzi_or_num_pattern}):(?P<case>[^(]+)\((?P<components>(?:{hanzi_or_num_pattern}(?:,{hanzi_or_num_pattern})*)?)\)'
hanzi_or_num_or_nm8bk__pattern = r'(?:[^\s\d\[\](),!:]|\d\d+|\[[^\s\d\[\](),!:]+\])' # num is not unicode!!!!!
line_pattern = fr'(?:[^!]*!)?(?P<key>{hanzi_or_num_or_nm8bk__pattern}):(?P<case>[^(]+)\((?P<components>(?:{hanzi_or_num_or_nm8bk__pattern}(?:,{hanzi_or_num_or_nm8bk__pattern})*)?)\)'
line_rex = re.compile(line_pattern)
def _():
  def hanzi_or_num_str2hanzi_or_num(hanzi_or_num_str, /):
    # -> (hanzi|int)
    try:
        assert len(hanzi_or_num_str) in (1,5)
    except:
        print(f'{hanzi_or_num_str!r}')
        raise
    if len(hanzi_or_num_str) == 1:
        hanzi = hanzi_or_num_str
        hanzi_or_num = hanzi
    else:
        num_str = hanzi_or_num_str
        num = int(num_str)
        #bug!: hanzi = chr(num)
        hanzi_or_num = num
    return hanzi_or_num
def bk5str(s, /):
    '-> (hanzi|uint|nm8bk)'
    assert s
    if s[0].isdigit():
        assert s.isdigit()
        bk = int(s)
    else:
        bk = s
    check_bk(bk)
    return bk
def check_bk(bk, /):
    if type(bk) is int:
        uint8bk = bk
        assert uint8bk >= 0
    else:
        nm8bk = bk
        check_nm8bk(nm8bk)
def check_nm8bk(nm8bk, /):
    部件名 = nm8bk
    if not type(部件名) is str: raise TypeError
    if not 部件名: raise TypeError
    部件名不成字 = not len(部件名) == 1
    assert 部件名不成字 is (部件名[0]=='[') is (部件名[-1]==']') is not (len(部件名)==1)

def iter_read_cjk_decomp(ifile, /):
    '-> Iter (hanzi|uint|nm8bk, (case, [(hanzi|uint|nm8bk)]))'
    #f = hanzi_or_num_str2hanzi_or_num
    f = bk5str
    for line in ifile:
        line = line.strip()
        if not line: continue
        m = line_rex.fullmatch(line)
        if m:
            key = f(m['key'])
            case = m['case']
            components_str = m['components']
            components_str = components_str.strip()
            if not components_str:
                components = []
            else:
                components = components_str.split(',')
                components = list(map(f, components))
            yield key, (case, components)
        else:
            raise Exception(f'{line!r}')

_global_iter_read_cjk_decomp = iter_read_cjk_decomp
def default_iter_read_cjk_decomp(iter_read_cjk_decomp=None, /, *, original=False):
    '-> Iter (hanzi|uint|nm8bk, (case, [(hanzi|uint|nm8bk)]))'
    if iter_read_cjk_decomp is None:
        iter_read_cjk_decomp = _global_iter_read_cjk_decomp
    if original:
        basename = Global.ifname_old
    else:
        basename = Global.ifname_modified
    #with open(Global.ipath, encoding=Global.iencoding) as fin:
    with open_under_pkg_(__package__, basename, xencoding=Global.iencoding) as fin:
        yield from iter_read_cjk_decomp(fin)

def iter_read_a_d_from_iter(iterable, /):
    'Iter (hanzi|uint|nm8bk, (case, [(hanzi|uint|nm8bk)])) -> Iter (bk, (op, bks))'
    return (x for x in iterable if x[1][0] in 'ad')
def iter_read_a_d(ifile, /):
    return iter_read_a_d_from_iter(iter_read_cjk_decomp(ifile))
def default_iter_read_a_d():
    return default_iter_read_cjk_decomp(iter_read_a_d)
    return iter_read_a_d_from_iter(default_iter_read_cjk_decomp())


def diff__bk2f_bks_(lhs, rhs, /):
    '{bk:(op,[bk])} -> {bk:(op,[bk])} -> patch<bk2f_bks>'
    patch = mapping_symmetric_diff4patch__immutable__default(lhs, rhs, validate=True)
    return patch
def patch__bk2f_bks_(patch, lhs, /):
    rhs = mapping_symmetric_patch4lhs__immutable__default(patch, lhs, validate=True)
    return rhs


def load_default():
    bk2f_bks__new = dict(default_iter_read_cjk_decomp(original=False))
    bk2f_bks__old = dict(default_iter_read_cjk_decomp(original=True))
    patch = diff__bk2f_bks_(bk2f_bks__old, bk2f_bks__new)
    assert bk2f_bks__new == patch__bk2f_bks_(patch, bk2f_bks__old)
    return (bk2f_bks__old, bk2f_bks__new, patch)

def load__ifile_(ifile, /):
    bk2f_bks = dict(iter_read_cjk_decomp(ifile))
    return bk2f_bks
def load__ipath_(ipath, /, *, encoding):
    with open(ipath, 'rt', encoding=encoding) as ifile:
        bk2f_bks = load__ifile_(ifile)
    return bk2f_bks

def load_with_diff__ipaths_ex_(*, ipath4old, ipath4new, encoding):
    bk2f_bks__old = load__ipath_(ipath4old, encoding=encoding)
    bk2f_bks__new = load__ipath_(ipath4new, encoding=encoding)
    patch = diff__bk2f_bks_(bk2f_bks__old, bk2f_bks__new)
    assert bk2f_bks__new == patch__bk2f_bks_(patch, bk2f_bks__old)
    return (bk2f_bks__old, bk2f_bks__new, patch)
def diff__ipath_(*, ipath4old, ipath4new, encoding):
    (bk2f_bks__old, bk2f_bks__new, patch) = load_with_diff__ipaths_ex_(ipath4old=ipath4old, ipath4new=ipath4new, encoding=encoding)
    return patch
def patch__ipath_ex_(*, patch, ipath4old, encoding):
    bk2f_bks__old = load__ipath_(ipath4old, encoding=encoding)
    bk2f_bks__new = patch__bk2f_bks_(patch, bk2f_bks__old)
    return (bk2f_bks__old, bk2f_bks__new)
def patch__ipath_(*, patch, ipath4old, encoding):
    (bk2f_bks__old, bk2f_bks__new) = patch__ipath_ex_(patch=patch, ipath4old=ipath4old, encoding=encoding)
    return bk2f_bks__old


def key4sort4bk(bk,/):
    if not type(bk) is str:
        check_uint(bk)
        u = bk
        if 0:
            assert 10_000 <= u < 100_000
            #k = f'{u:0>5X}'
            k = str(u)
            assert len(k) == 5
        case = 1
    elif len(bk)==1:
        hz = bk
        case = 2
    else:
        assert bk[+0] == '['
        assert bk[-1] == ']'
        nm4bk = bk
        case = 0
    return case, bk



def write_back_(ofile, bk2f_bks, /):
    #33238:wt(中,99697)
    #做:a(亻,故)
    #冏:a([无钩冂自部首⺆],㕣)
    fprint = mk_fprint(ofile)
    bks = sorted(bk2f_bks.keys(), key=key4sort4bk)
    for bk in bks:
        op, _bks = bk2f_bks[bk]
        s = ','.join(map(str, _bks))
        fprint(f'{bk!s}:{op!s}({s!s})')

def main4patch_(*, ipath4old, ipath4patch, may_opath4new, encoding, force=False):
    patch = read_file_as_python_object(ipath4patch, encoding=encoding)
    (bk2f_bks__old, bk2f_bks__new) = patch__ipath_ex_(patch=patch, ipath4old=ipath4old, encoding=encoding)
    with open4wt(may_opath4new, force=force, encoding=encoding) as ofile:
        write_back_(ofile, bk2f_bks__new)

def main4diff_(*, ipath4old, ipath4new, may_opath4patch, encoding, force=False):
    (bk2f_bks__old, bk2f_bks__new, patch) = load_with_diff__ipaths_ex_(ipath4old=ipath4old, ipath4new=ipath4new, encoding=encoding)
    with open4wt(may_opath4patch, force=force, encoding=encoding) as ofile:
        fprint = mk_fprint(ofile)
        stable_repr_print__expand_top_layer(ofile, patch)


