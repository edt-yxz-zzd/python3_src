#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/rename_module6py_stmts.py

py -m nn_ns.app.rename_module6py_stmts
py -m nn_ns.app.debug_cmd   nn_ns.app.rename_module6py_stmts -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.app.rename_module6py_stmts:__doc__ -ht # -ff -df
#######

[[
translation:
    from xxx import aaa
    from yyy import bbb
original:
    from zzz import aaa, bbb

]]


'#'; __doc__ = r'#'
>>>


[[
view ../../python3_src/seed/helper/lazy_import__func7context7register7data.py
py -m nn_ns.app.rename_module6py_stmts -new ../../python3_src/seed/helper/lazy_import__func7context7register7data.py -old ../../python3_src/seed/func_tools/[20220405]fmapT.py ../../python3_src/seed/data_funcs/finger_tree-obsolete-20240423/finger_tree3/bases.py
    ok
]]




py_adhoc_call   nn_ns.app.rename_module6py_stmts   @f
from nn_ns.app.rename_module6py_stmts import *
]]]'''#'''
__all__ = r'''
main
regex4py_import_stmt
    collect_nm2mdl5py_src_
        collect_nm2mdl5py_srcs_
    translate_py_import_stmts6lines_
        translate_py_import_stmts6ipath_
        iter_translate_py_import_stmts6ipaths_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.funcs import mk_fprint
    from seed.iters.chains import chains
    from seed.pkg_tools.read_python_source import read_python_source, read_python_source_from_module_qname

import re
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

#re.compile(r' *from ([._0-9a-zA-Z]+) import ([, \n\r\t0-9a-zA-Z]+)(#.*)?')
regex4py_import_stmt = re.compile(r' *from (\S+) import ([^#;]+)(#.*)?')
def collect_nm2mdl5py_src_(may_nm2mdl7new, ipath7new_stmts, /):
    nm2mdl7new = {} if None is may_nm2mdl7new else may_nm2mdl7new
    txt7new_stmts = read_python_source(ipath7new_stmts)
    lines7new_stmts = txt7new_stmts.split('\n')
    for line in lines7new_stmts:
        m = regex4py_import_stmt.fullmatch(line)
        if not m: continue
        (nm4mdl7new, xnms) = m.group(1, 2)
        xnms = xnms.split(',')
        xnms = _strips(xnms)
        for xnm in xnms:
            (nm, alias) = _split_alias(xnm)
            nm2mdl7new[nm] = nm4mdl7new
    return nm2mdl7new
def collect_nm2mdl5py_srcs_(may_nm2mdl7new, ipaths7new_stmts, /):
    nm2mdl7new = {} if None is may_nm2mdl7new else may_nm2mdl7new
    for ipath7new_stmts in ipaths7new_stmts:
        collect_nm2mdl5py_src_(nm2mdl7new, ipath7new_stmts)
    return nm2mdl7new

def translate_py_import_stmts6lines_(nm2mdl7new, lines_or_txt7original, /):
    '-> txt7translation/str'
    if isinstance(lines_or_txt7original, str):
        txt7original = lines_or_txt7original
        lines7original = txt7original.split('\n')
    else:
        lines7original = lines_or_txt7original
    lines7original
    nm4mdl7newZxnms = {}
    for line in lines7original:
        m = regex4py_import_stmt.fullmatch(line)
        if not m: continue
        (nm4mdl7old, xnms) = m.group(1, 2)
        xnms = xnms.split(',')
        xnms = _strips(xnms)
        for xnm in xnms:
            (nm, alias) = _split_alias(xnm)
            nm4mdl7new = nm2mdl7new.get(nm)
            if not nm4mdl7new: continue
            if nm4mdl7new == nm4mdl7old: continue
            nm4mdl7newZxnms.setdefault(nm4mdl7new, []).append(xnm)
    nm4mdl7newZxnms
    def __():
        for (nm4mdl7new, xnms) in sorted(nm4mdl7newZxnms.items()):
            xnms.sort()
            t = ', '.join(xnms)
            yield f'from {nm4mdl7new} import {t}'
    txt7translation = '\n'.join(__())
    return txt7translation


def _split_alias(xnm, /):
    if ' as ' in xnm:
        znms = xnm.split(' as ')
        znms = _strips(znms)
        (nm, alias) = znms
    else:
        nm = xnm
        alias = ''
    return (nm, alias)
def _strips(ss, /):
    return [*map(str.strip, ss)]

def translate_py_import_stmts6ipath_(nm2mdl7new, ipath7original, /):
    '-> txt7translation/str'
    txt7original = read_python_source(ipath7original)
    txt7translation = translate_py_import_stmts6lines_(nm2mdl7new, txt7original)
    return txt7translation





def iter_translate_py_import_stmts6ipaths_(nm2mdl7new, ipaths7original, /):
    '-> Iter (ipath, txt7translation/str)'
    for ipath7original in ipaths7original:
        txt7translation = translate_py_import_stmts6ipath_(nm2mdl7new, ipath7original)
        yield (ipath7original, txt7translation)


def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout
    from seed.io.may_open import open4w, open4w_err, open4r

    parser = argparse.ArgumentParser(
        description='translate py_import_stmts to alter module names'
        )
    parser.add_argument('-new', '--input7new'
        , type=str, default=[], action='append', nargs='+', required=True
        , help='input py source path which contains new import stmts')

    parser.add_argument('-old', '--input7old'
        , type=str, default=[], action='append', nargs='+', required=True
        , help='input py source path which contains old import stmts')

    parser.add_argument('-o', '--output'
        , type=str, default=None
        , help='output file path')
    parser.add_argument('-oe', '--oencoding', type=str, default='utf8'
        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true', default = False
        , help='open mode for output file')

    args = parser.parse_args(args)
    ipathss7new_stmts = args.input7new
    ipathss7original = args.input7old
    #print(ipaths7new_stmts)
    #print(ipaths7original)
    ipaths7new_stmts = chains(ipathss7new_stmts)
    ipaths7original = chains(ipathss7original)

    force = args.force
    oencoding = args.oencoding
    oencoding = 'utf8' if not oencoding else oencoding

    nm2mdl7new = collect_nm2mdl5py_srcs_({}, ipaths7new_stmts)
    may_ofname = args.output
    if 0b00000:
        #bug: 『-force』 --> 『-f -o rce』
        print(may_ofname)
        return
    with open4w(may_ofname, force=force, xencoding=oencoding) as ofile:
        #print(ofile)
        fprint = mk_fprint(ofile)
        #print(fprint)
        #fprint('xxx')
        for (ipath7original, txt7translation) in iter_translate_py_import_stmts6ipaths_(nm2mdl7new, ipaths7original):
            fprint('#########')
            fprint('#', ipath7original)
            fprint(txt7translation)
            fprint('\n')
if __name__ == "__main__":
    main()



__all__
from nn_ns.app.rename_module6py_stmts import *
