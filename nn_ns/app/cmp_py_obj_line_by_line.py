#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/cmp_py_obj_line_by_line.py
e ../../python3_src/bash_script/app/cmp_py_obj_line_by_line

nn_ns.app.cmp_py_obj_line_by_line
py -m nn_ns.app.debug_cmd   nn_ns.app.cmp_py_obj_line_by_line -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.app.cmp_py_obj_line_by_line:__doc__ -ht # -ff -df
#######

[[
to compare output files which contains set/dict but not use stable_repr
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   nn_ns.app.cmp_py_obj_line_by_line   @cmp_py_obj_line_by_line__ipaths_  --encoding:u8  :/sdcard/0my_files/tmp/-1tmp :/sdcard/0my_files/tmp/-0tmp
<==>:
cmp_py_obj_line_by_line  --encoding:u8  :/sdcard/0my_files/tmp/-1tmp :/sdcard/0my_files/tmp/-0tmp

]]]'''#'''
__all__ = r'''
cmp_py_obj_line_by_line__ipaths_
cmp_py_obj_line_by_line__ifiles_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.helper.safe_eval import safe_eval, safe_exec, data_eval
    #def safe_eval(expression, /,*, locals=None, nonlocals=None, using_extended_globals=False):

___end_mark_of_excluded_global_names__0___ = ...


def cmp_py_obj_line_by_line__ipaths_(ipath0, ipath1, /, *, encoding, **kwds4safe_eval):
    with (open(ipath0, 'rt', encoding=encoding) as ifile0, open(ipath1, 'rt', encoding=encoding) as ifile1):
        return cmp_py_obj_line_by_line__ifiles_(ifile0, ifile1, **kwds4safe_eval)
def cmp_py_obj_line_by_line__ifiles_(ifile0, ifile1, /, **kwds4safe_eval):
    it0 = iter(ifile0)
    it1 = iter(ifile1)
    Nothing = object()
    lineno = 0
    for lineno, s0 in enumerate(it0, 1):
        s1 = next(it1, Nothing)
        if s1 is Nothing:
            return ('diff:', lineno, (s0, None))
        s0 = s0.strip()
        s1 = s1.strip()
        if s0 == s1:
            continue
        v0 = safe_eval(s0, **kwds4safe_eval)
        v1 = safe_eval(s1, **kwds4safe_eval)
        if v0 == v1:
            continue
        return ('diff:', lineno, (s0, s1))
    else:
        s1 = next(it1, Nothing)
        if not s1 is Nothing:
            lineno += 1
            return ('diff:', lineno, (None, s1))
    num_lines = lineno
    return ('same:', num_lines)

__all__
from nn_ns.app.cmp_py_obj_line_by_line import cmp_py_obj_line_by_line__ipaths_, cmp_py_obj_line_by_line__ifiles_
from nn_ns.app.cmp_py_obj_line_by_line import *
