#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/import_stmt_context7collect.py
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
]]
[[
main_target:
py_adhoc_call   seed.helper.import_stmt_context7collect   @collect_import_stmts_  :../../python3_src/   :../../python3_src/seed/  1>/sdcard/0my_files/tmp/-0tmp 2>/sdcard/0my_files/tmp/-1tmp


#no_dup:
py_adhoc_call   seed.helper.import_stmt_context7collect   ,iter_collect_import_stmts_  -dup_ok  :../../python3_src/   :../../python3_src/seed/  1>/sdcard/0my_files/tmp/-0tmp 2>/sdcard/0my_files/tmp/-1tmp

#dup:
py_adhoc_call   seed.helper.import_stmt_context7collect   ,iter_collect_import_stmts_  +dup_ok  :../../python3_src/   :../../python3_src/seed/  1>/sdcard/0my_files/tmp/-0tmp 2>/sdcard/0my_files/tmp/-1tmp
]]

view /sdcard/0my_files/tmp/-0tmp
view /sdcard/0my_files/tmp/-1tmp




]]]'''#'''
__all__ = r'''
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

from seed.debug.print_err import print_err

___end_mark_of_excluded_global_names__0___ = ...


def _iter_collect_import_stmts_(root_dir8py, dir8py_pkg, /):
    '-> Iter (nm4tgt, qnm4mdl)'
    #xxx:meaningless:if dir8py_pkg is ...: dir8py_pkg = root_dir8py
    gap_path = relative_to(root_dir8py, dir8py_pkg)
    if not all(map(str.isidentifier, gap_path.parts)):raise Exception(root_dir8py, dir8py_pkg)
    #for (rpath, py_source_path) in iter_py_source_paths_(dir8py_pkg, ex=True, leading_underscore_ok=False):
    for py_source_path in iter_py_source_paths_(dir8py_pkg, leading_underscore_ok=False):
        yield from iter_collect_import_stmts5py_source_path_(root_dir8py, py_source_path)
def _iter_collect_import_stmts__no_dup_(output_dict, root_dir8py, dir8py_pkg, /):
    '-> Iter (nm4tgt, qnm4mdl)'
    d = output_dict
    for (nm4tgt, qnm4mdl) in _iter_collect_import_stmts_(root_dir8py, dir8py_pkg):
        sz = len(d)
        _qnm4mdl = d.setdefault(nm4tgt, qnm4mdl)
        if not _qnm4mdl == qnm4mdl:
            #raise Exception(nm4tgt, (_qnm4mdl, qnm4mdl))
            print_err('conflict:', (nm4tgt, (_qnm4mdl, qnm4mdl)))
        if not sz == len(d):
            yield (nm4tgt, qnm4mdl)
    return d
def iter_collect_import_stmts_(root_dir8py, dir8py_pkg, /, *, output_dict=None, dup_ok=...):
    '-> Iter (nm4tgt, qnm4mdl)'
    no_dict = output_dict is None
    if dup_ok is ...:
        dup_ok = no_dict
    if not dup_ok:
        if no_dict:
            output_dict = {}
        return _iter_collect_import_stmts__no_dup_(output_dict, root_dir8py, dir8py_pkg)
    else:
        #dup_ok
        if not no_dict:raise TypeError
        return _iter_collect_import_stmts_(root_dir8py, dir8py_pkg)
def collect_import_stmts_(root_dir8py, dir8py_pkg, /):
    '-> {nm4tgt: qnm4mdl}'
    d = {}
    for (nm4tgt, qnm4mdl) in iter_collect_import_stmts_(root_dir8py, dir8py_pkg, output_dict=d):
        pass
    return d

def extract_may_all_export_names5py_source_(py_source, idnt8py_source, /):
    'py_source/str -> may __all__/[str]'
    try:
        tree = ast.parse(py_source, idnt8py_source, 'exec')
    except Exception as exc:
        print_err('fail-parse:', (idnt8py_source, exc))
        #raise ExceptionGroup('fail:', [exc, Exception(idnt8py_source)])
        return None
    for stmt in reversed(tree.body):
        match stmt:
            case ast.Assign(targets=[ast.Name(id='__all__')], value=rhs):
                break
    else:
        return None
    rhs
    s4rhs = ast.get_source_segment(py_source, rhs)
    try:
        __all__ = eval(s4rhs, {}, {})
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
from seed.helper.import_stmt_context7collect import collect_import_stmts_
from seed.helper.import_stmt_context7collect import iter_collect_import_stmts_, iter_collect_import_stmts5py_source_path_
from seed.helper.import_stmt_context7collect import extract_may_all_export_names5py_source_
from seed.helper.import_stmt_context7collect import *
