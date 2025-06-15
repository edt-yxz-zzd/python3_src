#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/lazy_import__func7multilines.py

seed.helper.lazy_import__func7multilines
py -m nn_ns.app.debug_cmd   seed.helper.lazy_import__func7multilines -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.lazy_import__func7multilines:__doc__ -ht # -ff -df

[[
from seed.helper.lazy_import__func7multilines import lazy_import4funcss__AbbrStmt_, lazy_import4funcss__PyStmt_

===
usage:
lazy_import4funcss__AbbrStmt_(r"""
seed.tiny{fst,snd:_snd_}
seed.tiny{echo}
"""#"""
, __name__
#, to_show_nmss4func8dst=True
)
===
usage:
lazy_import4funcss__PyStmt_(r"""
from seed.tiny import fst, snd as_snd_
from seed.tiny import echo
"""#"""
, __name__
#, to_show_nmss4func8dst=True
)
===
#, **kwds4worker
#   === , *, to_show_nmss4func8dst=False, to_return_nmss4func8dst=False
]]




>>> import seed.helper.lazy_import__func7multilines as this_mdl

>>> s4py_stmt = r"""
... from seed import xxx
... from seed import yyy as bbb
... from seed import zzz,kkk
... """#"""
>>> s4abbr_stmt = r"""
... seed{xxx}
... seed{yyy:bbb}
... seed{zzz,kkk}
... """#"""



######################
>>> ks0 = {*globals()}
>>> _ks0 = {*vars(this_mdl)}
>>> lazy_import4funcss__PyStmt_(s4py_stmt, __name__)
[[_LazyImport4Func('seed', 'xxx', 'seed.helper.lazy_import__func7multilines', '')], [_LazyImport4Func('seed', 'yyy', 'seed.helper.lazy_import__func7multilines', 'bbb')], [_LazyImport4Func('seed', 'zzz', 'seed.helper.lazy_import__func7multilines', ''), _LazyImport4Func('seed', 'kkk', 'seed.helper.lazy_import__func7multilines', '')]]
>>> _ks1 = {*vars(this_mdl)}
>>> ','.join(sorted(_ks1 -_ks0))
'bbb,kkk,xxx,zzz'
>>> ks1 = {*globals()}
>>> ','.join(sorted(ks1 -ks0))
'_ks0,_ks1,ks0'
>>> this_mdl.xxx
_LazyImport4Func('seed', 'xxx', 'seed.helper.lazy_import__func7multilines', '')
>>> this_mdl.bbb
_LazyImport4Func('seed', 'yyy', 'seed.helper.lazy_import__func7multilines', 'bbb')
>>> this_mdl.zzz
_LazyImport4Func('seed', 'zzz', 'seed.helper.lazy_import__func7multilines', '')
>>> this_mdl.kkk
_LazyImport4Func('seed', 'kkk', 'seed.helper.lazy_import__func7multilines', '')

>>> lazy_import4funcss__PyStmt_(s4py_stmt, __name__, to_return_nmss4func8dst=True)
Traceback (most recent call last):
    ...
Exception: ('dst exist:', (<module 'seed.helper.lazy_import__func7multilines' from '/sdcard/0my_files/git_repos/python3_src/seed/helper/lazy_import__func7multilines.py'>, 'xxx'), _LazyImport4Func('seed', 'xxx', 'seed.helper.lazy_import__func7multilines', ''))
>>> for k in (_ks1 -_ks0):delattr(this_mdl, k)
>>> (tpl:=lazy_import4funcss__PyStmt_(s4py_stmt, __name__, to_return_nmss4func8dst=True))
([[_LazyImport4Func('seed', 'xxx', 'seed.helper.lazy_import__func7multilines', '')], [_LazyImport4Func('seed', 'yyy', 'seed.helper.lazy_import__func7multilines', 'bbb')], [_LazyImport4Func('seed', 'zzz', 'seed.helper.lazy_import__func7multilines', ''), _LazyImport4Func('seed', 'kkk', 'seed.helper.lazy_import__func7multilines', '')]], [['xxx'], ['bbb'], ['zzz', 'kkk']], '[[xxx], [bbb], [zzz, kkk]]')
>>> tpl[-1] #output:nmss4func8dst__str
'[[xxx], [bbb], [zzz, kkk]]'

>>> for k in (_ks1 -_ks0):delattr(this_mdl, k)
>>> [[xxx], [bbb], [zzz, kkk]] = lazy_import4funcss__PyStmt_(s4py_stmt, __name__) #using:nmss4func8dst__str
>>> for k in (_ks1 -_ks0):delattr(this_mdl, k)




######################
>>> ks0 = {*globals()}
>>> _ks0 = {*vars(this_mdl)}
>>> lazy_import4funcss__AbbrStmt_(s4abbr_stmt, __name__)
[[_LazyImport4Func('seed', 'xxx', 'seed.helper.lazy_import__func7multilines', '')], [_LazyImport4Func('seed', 'yyy', 'seed.helper.lazy_import__func7multilines', 'bbb')], [_LazyImport4Func('seed', 'zzz', 'seed.helper.lazy_import__func7multilines', ''), _LazyImport4Func('seed', 'kkk', 'seed.helper.lazy_import__func7multilines', '')]]
>>> _ks1 = {*vars(this_mdl)}
>>> ','.join(sorted(_ks1 -_ks0))
'bbb,kkk,xxx,zzz'
>>> ks1 = {*globals()}
>>> ','.join(sorted(ks1 -ks0)) # '_ks0,_ks1,ks0'
''
>>> this_mdl.xxx
_LazyImport4Func('seed', 'xxx', 'seed.helper.lazy_import__func7multilines', '')
>>> this_mdl.bbb
_LazyImport4Func('seed', 'yyy', 'seed.helper.lazy_import__func7multilines', 'bbb')
>>> this_mdl.zzz
_LazyImport4Func('seed', 'zzz', 'seed.helper.lazy_import__func7multilines', '')
>>> this_mdl.kkk
_LazyImport4Func('seed', 'kkk', 'seed.helper.lazy_import__func7multilines', '')

>>> lazy_import4funcss__AbbrStmt_(s4abbr_stmt, __name__, to_return_nmss4func8dst=True)
Traceback (most recent call last):
    ...
Exception: ('dst exist:', (<module 'seed.helper.lazy_import__func7multilines' from '/sdcard/0my_files/git_repos/python3_src/seed/helper/lazy_import__func7multilines.py'>, 'xxx'), _LazyImport4Func('seed', 'xxx', 'seed.helper.lazy_import__func7multilines', ''))
>>> for k in (_ks1 -_ks0):delattr(this_mdl, k)
>>> (tpl:=lazy_import4funcss__AbbrStmt_(s4abbr_stmt, __name__, to_return_nmss4func8dst=True))
([[_LazyImport4Func('seed', 'xxx', 'seed.helper.lazy_import__func7multilines', '')], [_LazyImport4Func('seed', 'yyy', 'seed.helper.lazy_import__func7multilines', 'bbb')], [_LazyImport4Func('seed', 'zzz', 'seed.helper.lazy_import__func7multilines', ''), _LazyImport4Func('seed', 'kkk', 'seed.helper.lazy_import__func7multilines', '')]], [['xxx'], ['bbb'], ['zzz', 'kkk']], '[[xxx], [bbb], [zzz, kkk]]')
>>> tpl[-1] #output:nmss4func8dst__str
'[[xxx], [bbb], [zzz, kkk]]'

>>> for k in (_ks1 -_ks0):delattr(this_mdl, k)
>>> [[xxx], [bbb], [zzz, kkk]] = lazy_import4funcss__AbbrStmt_(s4abbr_stmt, __name__) #using:nmss4func8dst__str
>>> for k in (_ks1 -_ks0):delattr(this_mdl, k)




py_adhoc_call   seed.helper.lazy_import__func7multilines   @f
]]]'''#'''
__all__ = r'''
lazy_import4funcss_
    lazy_import4funcss__AbbrStmt_
        iter_parse__AbbrStmt_
    lazy_import4funcss__PyStmt_
        iter_parse__PyStmt_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func7worker4funcss import worker4lazy_import4funcss_

#.from itertools import islice
import re
from seed.text.useful_regex_patterns import nm__pattern, qnm__pattern, space__regex
from seed.tiny_.check import check_type_is, check_int_ge
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.repr_input import repr_helper
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError



def __():
    nm, qnm = nm__pattern, qnm__pattern
    ######################
    qnmZnm = fr'(?:{qnm}(?:\s*:\s*{nm})?)'
    abbr_stmt = fr'(?:\s*(?P<qnm4mdl8src>{qnm})\s*[{{]\s*(?P<as_ls>{qnmZnm}(?:\s*,\s*{qnmZnm})*)\s*[}}]\s*)'
    _rex4abbr_stmt = re.compile(abbr_stmt)

    ######################
    nm_as_nm = fr'(?:{nm}(?:\s+as\s+{nm})?)'
    tailbody4py_stmt = fr'(?P<as_ls>{nm_as_nm}(?:\s*,\s*{nm_as_nm})*)'

    #tail4py_stmt__bare = fr'(?:\s+{tailbody4py_stmt}\s*)'
    #tail4py_stmt__paren = fr'(?:\s*[(]\s*{tailbody4py_stmt}\s*[)]\s*)'
    tail4py_stmt = fr'(?:(?:\s*(?P<lparen>[(])\s*|\s+){tailbody4py_stmt}\s*(?(lparen)[)]|)\s*)'
    header4py_stmt = fr'(?:\s*from\s+(?P<qnm4mdl8src>{qnm})\s+import)'
    py_stmt = fr'(?:{header4py_stmt}{tail4py_stmt}\s*)'
    _rex4py_stmt = re.compile(py_stmt)
    ######################
    return (_rex4py_stmt, _rex4abbr_stmt)
(_rex4py_stmt, _rex4abbr_stmt) = __()
_rex4as = re.compile(r'\s+as\s+')
assert _rex4py_stmt.fullmatch('from x import y  ')
assert _rex4abbr_stmt.fullmatch('x{y}  ')
def _parse__as_ls__AbbrStmt_(as_ls, /, *, halfway:bool):
    as_ls = space__regex.sub('', as_ls)
    if not halfway:
        as_ls = [(qnm4func8src, smay_nm4func8dst) for qnmZnm in as_ls.split(',') for qnm4func8src, _, smay_nm4func8dst in [qnmZnm.partition(':')]]
    return as_ls
def iter_parse__AbbrStmt_(import_stmts4func8src, /, *, halfway:bool):
    check_type_is(str, import_stmts4func8src)
    prev_end = 0
    for m in _rex4abbr_stmt.finditer(import_stmts4func8src):
        begin, end = m.span()
        if not begin == prev_end:raise ValueError((prev_end, begin), import_stmts4func8src[prev_end:])
        prev_end = end
        qnm4mdl8src = m['qnm4mdl8src']
        as_ls = m['as_ls']
        as_ls = _parse__as_ls__AbbrStmt_(as_ls, halfway=halfway)
        yield (qnm4mdl8src, as_ls)
    begin = len(import_stmts4func8src)
    if not begin == prev_end:raise ValueError((prev_end, begin), import_stmts4func8src[prev_end:])
    return
def iter_parse__PyStmt_(import_stmts4func8src, /, *, halfway:bool):
    check_type_is(str, import_stmts4func8src)
    prev_end = 0
    for m in _rex4py_stmt.finditer(import_stmts4func8src):
        begin, end = m.span()
        if not begin == prev_end:raise ValueError((prev_end, begin), import_stmts4func8src[prev_end:])
        prev_end = end
        qnm4mdl8src = m['qnm4mdl8src']
        as_ls = m['as_ls']
        as_ls = _rex4as.sub(':', as_ls)
        as_ls = _parse__as_ls__AbbrStmt_(as_ls, halfway=halfway)
        yield (qnm4mdl8src, as_ls)
    begin = len(import_stmts4func8src)
    if not begin == prev_end:raise ValueError((prev_end, begin), import_stmts4func8src[prev_end:])
    return

def lazy_import4funcss__AbbrStmt_(import_stmts4func8src, smay_qnm4mdl8dst='', /, **kwds4worker):
    'line-fmt-regex"{qnm4mdl8src}{{{nm}(:{nm})?(,{nm}(:{nm})?)*}}"'
    #, **kwds4worker
    #   === , *, to_show_nmss4func8dst=False, to_return_nmss4func8dst=False
    mdl__nm_pairs__pairs = iter_parse__AbbrStmt_(import_stmts4func8src, halfway=False)
    return worker4lazy_import4funcss_(mdl__nm_pairs__pairs, smay_qnm4mdl8dst, **kwds4worker)
def lazy_import4funcss__PyStmt_(import_stmts4func8src, smay_qnm4mdl8dst='', /, **kwds4worker):
    'line-fmt-regex"from {qnm4mdl8src} import {nm}( as {nm})?(, {nm}( as {nm})?)*}}"'
    #, **kwds4worker
    #   === , *, to_show_nmss4func8dst=False, to_return_nmss4func8dst=False
    mdl__nm_pairs__pairs = iter_parse__PyStmt_(import_stmts4func8src, halfway=False)
    return worker4lazy_import4funcss_(mdl__nm_pairs__pairs, smay_qnm4mdl8dst, **kwds4worker)

_case2f = dict(PyStmt=lazy_import4funcss__PyStmt_, AbbrStmt=lazy_import4funcss__AbbrStmt_)
def lazy_import4funcss_(import_stmts4func8src, smay_qnm4mdl8dst='', /, *, case4fmt:'PyStmt|AbbrStmt'):
    check_type_is(str, case4fmt)
    return _case2f[case4fmt](import_stmts4func8src, smay_qnm4mdl8dst)



__all__
from seed.helper.lazy_import__func7multilines import lazy_import4funcss__AbbrStmt_, lazy_import4funcss__PyStmt_
from seed.helper.lazy_import__func7multilines import lazy_import4funcss_
from seed.helper.lazy_import__func7multilines import iter_parse__AbbrStmt_, iter_parse__PyStmt_
from seed.helper.lazy_import__func7multilines import *
