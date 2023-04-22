#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏.py
see:
    view script/字词典囗姓氏提取囗.py


nn_ns.CJK.CJK_data.raw.姓氏
py -m nn_ns.app.debug_cmd   nn_ns.CJK.CJK_data.raw.姓氏 -x
py -m nn_ns.app.doctest_cmd nn_ns.CJK.CJK_data.raw.姓氏:__doc__ -ff -v
py_adhoc_call   nn_ns.CJK.CJK_data.raw.姓氏   @show_srcs
py_adhoc_call   nn_ns.CJK.CJK_data.raw.姓氏   @show  :姓氏囗囗欧路词典囗现代汉语词典  :姓氏囗囗欧路词典囗汉语大辞典囗囗繁体版 :姓氏囗囗欧路词典囗汉语大辞典囗囗简体版  :姓氏囗囗纯文本囗中文字典囗新华字典  :姓氏囗囗应用程序囗汉语字典
py_adhoc_call   nn_ns.CJK.CJK_data.raw.姓氏   @show_diff   :姓氏囗囗纯文本囗中文字典囗新华字典  :姓氏囗囗应用程序囗汉语字典
py_adhoc_call   nn_ns.CJK.CJK_data.raw.姓氏   @show_whether_contain   :裔  :赓
py_adhoc_call   nn_ns.CJK.CJK_data.raw.姓氏   @show_diff   :姓氏囗囗应用程序囗汉语辞海  :姓氏囗囗欧路词典囗汉语大辞典囗囗简体版


from nn_ns.CJK.CJK_data.raw.姓氏 import *

[[
view script/字词典囗姓氏提取囗.py
===
欧路词典.现代汉语词典:
乐:④（Lè）姓（与Yuè不同姓）。②（Yuè）姓（与Lè不同姓）。
    !!!

欧路词典.汉语大辞典:
余俞相朴那樂:多音不同姓
余:
I
 yú
5.姓。
II
 yù
姓。見“余且”。
俞:
I
 yú
 9.姓。
V
 chòu
 姓。
 漢有司徒掾俞連。見《廣韻‧去宥》

相:
I
 xiāng
 7.姓。
 晉有相龍。見《晉書‧五行志上》。
II
 xiàng
 23.姓。
 晉有相雲。見《晉書‧姚興載記上》。

朴:
V
 pú
 姓。
 三國魏有巴七姓夷王朴胡。見《三國志‧魏志‧武帝紀》。
VI
 piáo
 姓。
 明代有朴素。

那
I
 nuó
 8.姓。
 明有那嵩。見明陳士元《姓觿》卷三、《明史》本傳。
VII
 nā
 ㄋㄚ
 姓。
 《清史稿‧那桐傳》：“那桐，字琴軒，葉赫那拉氏，內務府滿洲鑲黃旗人。”

樂:
I
 yuè
 7.姓。
 戰國時有燕將樂毅
II
 lè
 9.姓(與樂yuè不同姓)。


]]
[[
view script/字词典囗姓氏提取囗.py
    view ../../python3_src/nn_ns/CJK/CJK_common/化繁为简.py
===
!mkdir ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/
cp -t ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/  script/字词典囗姓氏提取囗.py.outs/*
du -h ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/
    52K
cp -t ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/  script/字词典囗姓氏提取囗.py.mid-outs-只保留关键义项/*

src=/sdcard/0my_files/tmp/out4py
dst=../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总

show diffs:
for nm in $( ls "$dst/" ) ; do {  if [[ '' != $( diff "$src/$nm"  "$dst/$nm" -q ) ]] ; then echo "$nm" ; fi }  done

copy overwrite diffs:
for nm in $( ls "$dst/" ) ; do {  if [[ '' != $( diff "$src/$nm"  "$dst/$nm" -q ) ]] ; then cp -t "$dst/"  "$src/$nm" ; fi }  done


du -h ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/
    428K
du -h ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/*
16K     ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗简体版..欧路词典.汉语大辞典.姓氏提取.out.txt
20K     ../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗繁简对照表..欧路词典.汉语大辞典.姓氏提取.out.txt
    忽略前缀:『../../python3_src/nn_ns/CJK/CJK_data/raw/姓氏汇总/script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗』
304K    ...+人工编辑+再过滤+只保留关键义项..欧路词典.汉语大辞典.词典-初步清理.out.txt
32K     ...+人工编辑+再过滤+只保留关键义项..欧路词典.现代汉语词典.词典.out.txt
4.0K    ...+人工编辑+提取囗人工编辑过的过滤文件囗..APP.古汉语字典囗.dump.out.txt
8.0K    ...+人工编辑+提取囗人工编辑过的过滤文件囗..APP.汉语字典囗.dump.out.txt
8.0K    ...+人工编辑+提取囗人工编辑过的过滤文件囗..TXT.中文字典囗.新华字典.格式化.out.txt
16K     ...+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
4.0K    ...+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.现代汉语词典.词典.out.txt
8.0K    ...+再过滤+人工编辑+提取囗人工编辑过的过滤文件囗..APP.汉语辞海囗.dump.out.txt
]]


nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗简体版..欧路词典.汉语大辞典.姓氏提取.out.txt
script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.现代汉语词典.词典.out.txt
script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt
script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..TXT.中文字典囗.新华字典.格式化.out.txt
script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..APP.汉语字典囗.dump.out.txt



姓氏囗囗欧路词典囗现代汉语词典
姓氏囗囗欧路词典囗汉语大辞典囗囗繁体版
姓氏囗囗欧路词典囗汉语大辞典囗囗简体版
姓氏囗囗纯文本囗中文字典囗新华字典
姓氏囗囗应用程序囗汉语字典
--姓氏囗囗应用程序囗汉语辞海

#]]]'''
__all__ = r'''
姓氏囗囗欧路词典囗现代汉语词典
姓氏囗囗欧路词典囗汉语大辞典囗囗繁体版
姓氏囗囗欧路词典囗汉语大辞典囗囗简体版
姓氏囗囗纯文本囗中文字典囗新华字典
姓氏囗囗应用程序囗汉语字典



sorted_uniqued_
show_srcs
show
show_diff
show_whether_contain

姓氏囗囗应用程序囗汉语辞海
'''.split()#'''
__all__



from seed.pkg_tools.load_resource import iter_potential_basenames_under_pkg_, does_exist_under_pkg_#, list_potential_basenames_under_pkg_, sorted_potential_basenames_under_pkg_, with_path_under_pkg_
from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_
#def read_under_pkg_(pkg, basename, /, *, xencoding, **kwds):
from seed.tiny import MapView
from seed.mapping_tools.dict_op import inv__k2v_to_v2k, inv__k2v_to_v2ks, inv__k2vs_to_v2k, inv__k2vs_to_v2ks
from seed.mapping_tools.dict_op import set_symmetric_partition__immutable
from seed.tiny import fmap4dict_value
from itertools import combinations

_nms4skip = set('''
__init__.py
__main__.py
'''.split())#'''
_pkg = f'{__package__}.姓氏汇总'
def __(pkg, nms4skip, /):
    nms = iter_potential_basenames_under_pkg_(pkg)
    #family name
    nms4fmmn = set()
    nms4fmmn_with_src = set()
    for nm in nms:
        if nm in nms4skip:
            pass
        elif '+只保留关键义项..' in nm:
            nms4fmmn_with_src.add(nm)
        elif '+人工编辑+提取囗人工编辑过的过滤文件囗..' in nm:
            nms4fmmn.add(nm)
        elif nm.startswith('nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗简体版..'):
            nms4fmmn.add(nm)
        elif nm.startswith('nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗繁简对照表..'):
            pass
        else:
            raise Exception(f'unknown: {nm!r}')
    nms4fmmn = frozenset(nms4fmmn)
    nms4fmmn_with_src = frozenset(nms4fmmn_with_src)
    return (nms4fmmn, nms4fmmn_with_src)

(_nms4fmmn, _nms4fmmn_with_src) = __(_pkg, _nms4skip)

def sorted_uniqued_(xs, /):
    return sorted({*xs})
def _load_surnames(pkg, nms4fmmn, /):
    nm2surnames = {}
    for nm in sorted_uniqued_(nms4fmmn):
        if not does_exist_under_pkg_(pkg, nm):
            continue
        txt = read_under_pkg_(pkg, nm, xencoding='u8')
        surnames = txt.split()
        surnames = sorted_uniqued_(surnames)
        surnames = (*surnames,)
        nm2surnames[nm] = surnames
    nm2surnames
    nm2surname_set = fmap4dict_value(frozenset, nm2surnames)

    nm2surnames = MapView(nm2surnames)
    nm2surname_set = MapView(nm2surname_set)
    return nm2surnames, nm2surname_set
_nm2surnames, _nm2surname_set = _load_surnames(_pkg, _nms4fmmn)



_nm2nm = (dict
(姓氏囗囗欧路词典囗现代汉语词典 = 'script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.现代汉语词典.词典.out.txt'
,姓氏囗囗欧路词典囗汉语大辞典囗囗简体版 = 'nn_ns.CJK.CJK_common.化繁为简..化繁为简囗囗文件路径囗..输出囗简体版..欧路词典.汉语大辞典.姓氏提取.out.txt'
,姓氏囗囗欧路词典囗汉语大辞典囗囗繁体版 = 'script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..欧路词典.汉语大辞典.词典-初步清理.out.txt'
,姓氏囗囗纯文本囗中文字典囗新华字典 = 'script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..TXT.中文字典囗.新华字典.格式化.out.txt'
,姓氏囗囗应用程序囗汉语字典 = 'script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+人工编辑+提取囗人工编辑过的过滤文件囗..APP.汉语字典囗.dump.out.txt'
,姓氏囗囗应用程序囗汉语辞海 = 'script.字词典囗姓氏提取囗..过滤出候选姓氏囗格式化囗字词典囗+再过滤+人工编辑+提取囗人工编辑过的过滤文件囗..APP.汉语辞海囗.dump.out.txt'
))



def _get_ground_nm(nm, /):
    nm = nm
    while nm in _nm2nm:
        nm = _nm2nm[nm]
    return nm
def _get(nm, /):
    nm = _get_ground_nm(nm)
    surnames = _nm2surnames[nm]
    return surnames
def _get8set(nm, /):
    nm = _get_ground_nm(nm)
    surname_set = _nm2surname_set[nm]
    return surname_set
    return {*_get(nm)}
globals().update((nm, _get(nm)) for nm in _nm2nm)




def show_srcs():
    _nm2gnm = {nm:_get_ground_nm(nm) for nm in _nm2nm}
    gnm2gnm = {nm:nm for nm in _nm2surnames}
    xnm2gnm = {**_nm2gnm, **gnm2gnm}
    gnm2xnms = inv__k2v_to_v2ks(xnm2gnm)
    for gnm, xnms in sorted(gnm2xnms.items()):
        xnms = {*xnms}
        xnms.remove(gnm)
        xnms = sorted(xnms)
        print(f'{gnm!r}')
        for xnm in xnms:
            print(f'    {xnm!r}')



def show(*nms):
    for nm in nms:
        surnames = _get(nm)
        print(f'==={nm!r}===')
        print(f'==={len(surnames)!r}===')
        for surname in surnames:
            print(surname)

def _1_show_diff(prefix, surnames, /, *, b_show=True):
    print(f'{prefix}{len(surnames)}')
    if not b_show:
        return
    for surname in surnames:
        print(surname)

def show_diff(*nms):
    #nms = sorted_uniqued_(nms)

    for nm4lhs, nm4rhs in combinations(nms, 2):
        lhs = _get8set(nm4lhs)
        rhs = _get8set(nm4rhs)
        (lonly, common, ronly) = map(sorted, set_symmetric_partition__immutable(lhs, rhs))
        print(f'===: {nm4lhs!r} vs {nm4rhs!r} :===')
    _1_show_diff('<<<<<<:', lonly)
    _1_show_diff('>>><<<:', common, b_show=False)
    _1_show_diff('>>>>>>:', ronly)

def show_whether_contain(*surnames):
    for nm in sorted(_nm2nm):
        print(f'{nm}')
        surname_set = _get8set(nm)

        for surname in surnames:
            b = int(surname in surname_set)
            print(f'   {b} {surname}')

def __():
    from seed.tiny import ifNonef, ifNone, echo
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.helper.repr_input import repr_helper

__all__


from nn_ns.CJK.CJK_data.raw.姓氏 import *
