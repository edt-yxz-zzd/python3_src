#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/import_stmt_context7collect.py
view ../../python3_src/seed/helper/import_stmt_context7collect.py

view ../../python3_src/seed/helper/import_stmt_context.py
view ../../python3_src/seed/helper/lazy_import__func7context7register7data.py

seed.helper.import_stmt_context7collect
py -m nn_ns.app.debug_cmd   seed.helper.import_stmt_context7collect -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.import_stmt_context7collect:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/helper/import_stmt_context.py
view ../../python3_src/seed/helper/lazy_import__func7context7register7data.py
]]


'#'; __doc__ = r'#'
>>>




[[
test:
py_adhoc_call   seed.helper.import_stmt_context7collect   ,iter_collect_import_stmts_  :../../python3_src/   :../../python3_src/seed/helper/
py_adhoc_call   seed.helper.import_stmt_context7collect   ,iter_collect_import_stmts_  :../../python3_src/   :../../python3_src/seed/helper/  1>/sdcard/0my_files/tmp/-0tmp 2>/sdcard/0my_files/tmp/-1tmp
]]
[[
test:
py_adhoc_call   seed.helper.import_stmt_context7collect   @collect_import_stmts_  :../../python3_src/   :../../python3_src/seed/helper/  1>/sdcard/0my_files/tmp/-0tmp 2>/sdcard/0my_files/tmp/-1tmp

#no_dup:
py_adhoc_call   seed.helper.import_stmt_context7collect   ,iter_collect_import_stmts_  -dup_ok  :../../python3_src/   :../../python3_src/seed/helper/  1>/sdcard/0my_files/tmp/-0tmp 2>/sdcard/0my_files/tmp/-1tmp

#dup:
py_adhoc_call   seed.helper.import_stmt_context7collect   ,iter_collect_import_stmts_  +dup_ok  :../../python3_src/   :../../python3_src/seed/helper/  1>/sdcard/0my_files/tmp/-0tmp 2>/sdcard/0my_files/tmp/-1tmp

py_adhoc_call   seed.helper.import_stmt_context7collect   ,str.list_format_collect_import_stmts_  +dup_ok  :../../python3_src/   :../../python3_src/seed/helper/  1>/sdcard/0my_files/tmp/-0tmp 2>/sdcard/0my_files/tmp/-1tmp

py_adhoc_call   seed.helper.import_stmt_context7collect   ,str.list_format_collect_import_stmts_  --excludes='...' +dup_ok  :../../python3_src/   :../../python3_src/seed/helper/  1>/sdcard/0my_files/tmp/-0tmp 2>/sdcard/0my_files/tmp/-1tmp
]]
[[
main_target:
py_adhoc_call   seed.helper.import_stmt_context7collect   @collect_import_stmts_  :../../python3_src/   :../../python3_src/seed/  1>/sdcard/0my_files/tmp/-0tmp 2>/sdcard/0my_files/tmp/-1tmp


#no_dup:
py_adhoc_call   seed.helper.import_stmt_context7collect   ,iter_collect_import_stmts_  -dup_ok  :../../python3_src/   :../../python3_src/seed/  1>/sdcard/0my_files/tmp/-0tmp 2>/sdcard/0my_files/tmp/-1tmp

#dup:
py_adhoc_call   seed.helper.import_stmt_context7collect   ,iter_collect_import_stmts_  +dup_ok  :../../python3_src/   :../../python3_src/seed/  1>/sdcard/0my_files/tmp/-0tmp 2>/sdcard/0my_files/tmp/-1tmp

@20260406凌晨
py_adhoc_call   seed.helper.import_stmt_context7collect   ,str.list_format_collect_import_stmts_  +dup_ok  :../../python3_src/   :../../python3_src/seed/  1>/sdcard/0my_files/tmp/-0tmp 2>/sdcard/0my_files/tmp/-1tmp
du -bh /sdcard/0my_files/tmp/-0tmp
    316K @20260406凌晨
view /sdcard/0my_files/tmp/-0tmp
    2592 lines
view /sdcard/0my_files/tmp/-1tmp
    246 lines


@20260406中午
    ++修改代码:打补丁:++__all__ = ''.split(); ___delta_all___; ___this_is_forwarding_module___ = True;from  import 
    ++kw:excludes
py_adhoc_call   seed.helper.import_stmt_context7collect   ,str.list_format_collect_import_stmts_  --excludes='...' +dup_ok  :../../python3_src/   :../../python3_src/seed/  1>/sdcard/0my_files/tmp/-0tmp 2>/sdcard/0my_files/tmp/-1tmp
du -bh /sdcard/0my_files/tmp/-0tmp
    322K @20260406中午
view /sdcard/0my_files/tmp/-0tmp
    2717 lines
view /sdcard/0my_files/tmp/-1tmp
    0 lines
mkdir ../../python3_src/seed/helper/_ignore__tmp/
cp -iv /sdcard/0my_files/tmp/-0tmp ../../python3_src/seed/helper/_ignore__tmp/list_format_collect_import_stmts_.20260406-noon.stdout.txt
view ../../python3_src/seed/helper/_ignore__tmp/list_format_collect_import_stmts_.20260406-noon.stdout.txt
]]

view /sdcard/0my_files/tmp/-0tmp
view /sdcard/0my_files/tmp/-1tmp




]]]'''#'''
__all__ = r'''
list_format_collect_import_stmts_
collect_import_stmts_
    iter_collect_import_stmts_
        iter_collect_import_stmts5py_source_path_
            extract_may_all_export_names5py_source_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from pathlib import Path

import ast
from seed.lang.read_py_source import read_py_source5path_
from seed.filesys.relative_to import relative_to

from seed.pkg_tools.iter_py_source_paths_ import iter_py_source_paths_
#def iter_py_source_paths_(dir8py_pkg, /, *, ex=False, leading_underscore_ok=False, excludes=()):

from seed.debug.print_err import print_err
from seed.tiny_.funcs import fst, unbox
from seed.tiny_.check import check_type_is
from seed.helper.str2__all__ import str2__all__
_locals = dict(str2__all__=str2__all__)

from itertools import groupby
___end_mark_of_excluded_global_names__0___ = ...

if 0:
    _default_excluded_paths_under_seed = None
def _gmk_default_excluded_paths_under_seed_():
    try:
        return _default_excluded_paths_under_seed
    except NameError:
        pass
    _load_default_excluded_paths_under_seed_()
    return _gmk_default_excluded_paths_under_seed_()
def _load_default_excluded_paths_under_seed_():
    global _default_excluded_paths_under_seed
    ipath = Path(__file__).parent / 'import_stmt_context7collect.py.excluded_paths.txt'
    txt = ipath.read_text('utf8')
    iter_rpaths = filter(bool, txt.split('\n'))
    root_dir8py = Path(*Path(__file__).parent.parts[:-(1+__package__.count('.'))])
    #raise Exception(root_dir8py)
    _default_excluded_paths_under_seed = tuple(root_dir8py/rpath for rpath in iter_rpaths)
    return

def _iter_collect_import_stmts_(root_dir8py, dir8py_pkg, excludes, /):
    '-> Iter (nm4tgt, qnm4mdl)'
    #xxx:meaningless:if dir8py_pkg is ...: dir8py_pkg = root_dir8py
    gap_path = relative_to(root_dir8py, dir8py_pkg)
    if excludes is ...:
        excludes = _gmk_default_excluded_paths_under_seed_()
        #print_err(excludes)
    if not all(map(str.isidentifier, gap_path.parts)):raise Exception(root_dir8py, dir8py_pkg)
    #for (rpath, py_source_path) in iter_py_source_paths_(dir8py_pkg, ex=True, leading_underscore_ok=False):
    for py_source_path in iter_py_source_paths_(dir8py_pkg, leading_underscore_ok=False, excludes=excludes):
        yield from iter_collect_import_stmts5py_source_path_(root_dir8py, py_source_path)
def _iter_collect_import_stmts__no_dup_(output_dict, root_dir8py, dir8py_pkg, excludes, /):
    '-> Iter (nm4tgt, qnm4mdl) # [output_dict :: {nm4tgt:qnm4mdl}]'
    d = output_dict
    for (nm4tgt, qnm4mdl) in _iter_collect_import_stmts_(root_dir8py, dir8py_pkg, excludes):
        sz = len(d)
        _qnm4mdl = d.setdefault(nm4tgt, qnm4mdl)
        if not _qnm4mdl == qnm4mdl:
            #raise Exception(nm4tgt, (_qnm4mdl, qnm4mdl))
            print_err('conflict:', (nm4tgt, (_qnm4mdl, qnm4mdl)))
        if not sz == len(d):
            yield (nm4tgt, qnm4mdl)
    return d
def _iter_collect_import_stmts__ok_dup_(output_dict, root_dir8py, dir8py_pkg, excludes, /):
    '-> Iter (nm4tgt, qnm4mdl) # [output_dict :: {nm4tgt:{qnm4mdl}}]'
    d = output_dict
    for (nm4tgt, qnm4mdl) in _iter_collect_import_stmts_(root_dir8py, dir8py_pkg, excludes):
        s = d.setdefault(nm4tgt, set())
        sz = len(s)
        s.add(qnm4mdl)
        if not sz == len(s):
            yield (nm4tgt, qnm4mdl)
    return d

def iter_collect_import_stmts_(root_dir8py, dir8py_pkg, /, *, output_dict=None, dup_ok=..., excludes=()):
    '-> Iter (nm4tgt, qnm4mdl)'
    no_dict = output_dict is None
    if dup_ok is ...:
        dup_ok = no_dict
    if no_dict:
        output_dict = {}
    if not dup_ok:
        return _iter_collect_import_stmts__no_dup_(output_dict, root_dir8py, dir8py_pkg, excludes)
    else:
        #dup_ok
        return _iter_collect_import_stmts__ok_dup_(output_dict, root_dir8py, dir8py_pkg, excludes)
def collect_import_stmts_(root_dir8py, dir8py_pkg, /, *, dup_ok=False, excludes=()):
    '-> {nm4tgt: qnm4mdl} if not dup_ok else {nm4tgt:{qnm4mdl}}'
    check_type_is(bool, dup_ok)
    d = {}
    for (nm4tgt, qnm4mdl) in iter_collect_import_stmts_(root_dir8py, dir8py_pkg, output_dict=d, dup_ok=dup_ok, excludes=excludes):
        pass
    return d
def _format_import_stmt_(qnm_nms_pair, /):
    '(qnm4mdl, [nm4tgt]) -> str'
    (qnm4mdl, nms4tgt) = qnm_nms_pair
    if type(nms4tgt) is str:
        nms4tgt = nms4tgt.split()
    s = ', '.join(nms4tgt)
    if not s:raise Exception(qnm_nms_pair)
    return f'from {qnm4mdl} import {s}'
def list_format_collect_import_stmts_(root_dir8py, dir8py_pkg, /, *, dup_ok=False, excludes=()):
    d = collect_import_stmts_(root_dir8py, dir8py_pkg, dup_ok=dup_ok, excludes=excludes)
    if not dup_ok:
        it = _iter_format_collect_import_stmts__no_dup_(d)
    else:
        it = _iter_format_collect_import_stmts__ok_dup_(d)
    it
    return list(it)
def _iter_format_collect_import_stmts__no_dup_(d, /):
    ps = sorted((qnm, nm) for nm, qnm in d.items())
    for qnm, g in groupby(ps, key=fst):
        nms = [nm for qnm, nm in g]
        yield _format_import_stmt_((qnm, nms))
def _iter_format_collect_import_stmts__ok_dup_(d, /):
    d1 = {nm:unbox(qnms) for nm, qnms in d.items() if len(qnms) == 1}
    d2 = {nm:qnms for nm, qnms in d.items() if not len(qnms) == 1}
    yield from _iter_format_collect_import_stmts__no_dup_(d1)
    for (nm, qnms) in sorted(d2.items()):
        yield '####'
        for qnm in sorted(qnms):
            s = _format_import_stmt_((qnm, [nm]))
            yield f'#:{s}'

def _debugging__extract_may_all_export_names5py_source_path_(py_source_path, /):
    py_source = read_py_source5path_(py_source_path)
    return extract_may_all_export_names5py_source_(py_source, py_source_path)

def extract_may_all_export_names5py_source_(py_source, idnt8py_source, /):
    'py_source/str -> idnt8py_source/(str|path) -> may __all__/[str]'
    try:
        tree = ast.parse(py_source, idnt8py_source, 'exec')
    except Exception as exc:
        print_err('fail-parse:', (idnt8py_source, exc))
        #raise ExceptionGroup('fail:', [exc, Exception(idnt8py_source)])
        return None
    for stmt in tree.body:
        match stmt:
            case ast.Assign(targets=[ast.Name(id='___this_is_forwarding_module___')], value=ast.Constant(value=True)):
                #___this_is_forwarding_module___ = True
                return ()
                return None

    for stmt in reversed(tree.body):
        match stmt:
            case ast.Assign(targets=[ast.Name(id='___delta_all___')], value=rhs):
                break
    else:
        for stmt in reversed(tree.body):
            match stmt:
                case ast.Assign(targets=[ast.Name(id='__all__')], value=rhs):
                    break
        else:
            return None
        rhs
    rhs
    s4rhs = ast.get_source_segment(py_source, rhs)

    try:
        __all__ = eval(s4rhs, {}, _locals)
    except Exception as exc:
        print_err('fail-eval:', (idnt8py_source, s4rhs, exc))
        #raise ExceptionGroup('fail:', [exc, Exception(idnt8py_source, s4rhs)])
        return None
    if type(__all__) is str:
        print_err('bad-__all__:', (idnt8py_source, __all__))
        #raise Exception(idnt8py_source, __all__)
        return None
    __all__ = tuple(__all__)
    if not all(map(str.isidentifier, __all__)):
        print_err('bad-__all__:', (idnt8py_source, __all__))
        #raise Exception(idnt8py_source, __all__)
        return None
    return __all__

def iter_collect_import_stmts5py_source_path_(root_dir8py, py_source_path, /):
    '-> Iter (nm4tgt, qnm4mdl)'
    short_path = relative_to(root_dir8py, py_source_path)
    qnm4mdl = '.'.join(short_path.with_suffix('').parts)
    if not qnm4mdl or '..' in qnm4mdl or qnm4mdl[0] == '.' or qnm4mdl[-1] == '.':raise Exception(short_path, qnm4mdl)

    py_source = read_py_source5path_(py_source_path)
    m = extract_may_all_export_names5py_source_(py_source, short_path)
    match m:
        case None:
            print_err('missing __all__:', qnm4mdl, py_source_path)
            return
        case __all__:
            for nm4tgt in __all__:
                yield (nm4tgt, qnm4mdl)



__all__
from seed.helper.import_stmt_context7collect import list_format_collect_import_stmts_, collect_import_stmts_
from seed.helper.import_stmt_context7collect import iter_collect_import_stmts_, iter_collect_import_stmts5py_source_path_
from seed.helper.import_stmt_context7collect import extract_may_all_export_names5py_source_
if 0:
    from seed.helper.import_stmt_context7collect import _debugging__extract_may_all_export_names5py_source_path_
    #def _debugging__extract_may_all_export_names5py_source_path_(py_source_path, /):
from seed.helper.import_stmt_context7collect import *
