#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/lazy_import__func7ast.py

seed.helper.lazy_import__func7ast
py -m nn_ns.app.debug_cmd   seed.helper.lazy_import__func7ast -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.lazy_import__func7ast:__doc__ -ht # -ff -df

[[
usage:
from seed.helper.lazy_import__func7ast import mk_decorator4lazy_import__funcs_, decorator4lazy_import__funcs_
@decorator4lazy_import__funcs_
def __():
    from seed.tiny import fst, snd as _snd_
    ##if toplevel then eqv:
@mk_decorator4lazy_import__funcs_(__name__)
def __():
    from seed.tiny import fst, snd as _snd_

]]



>>> import seed.helper.lazy_import__func7ast as this_mdl

>>> ks0 = {*globals()}
>>> _ks0 = {*vars(this_mdl)}
>>> decorator4lazy_import__funcs_(_f)
[[_LazyImport4Func('seed', 'xxx', 'seed.helper.lazy_import__func7ast', '')], [_LazyImport4Func('seed', 'yyy', 'seed.helper.lazy_import__func7ast', 'bbb')], [_LazyImport4Func('seed', 'zzz', 'seed.helper.lazy_import__func7ast', ''), _LazyImport4Func('seed', 'kkk', 'seed.helper.lazy_import__func7ast', '')]]
>>> _ks1 = {*vars(this_mdl)}
>>> ','.join(sorted(_ks1 -_ks0))
'bbb,kkk,xxx,zzz'
>>> ks1 = {*globals()}
>>> ','.join(sorted(ks1 -ks0))
'_ks0,_ks1,ks0'
>>> this_mdl.xxx
_LazyImport4Func('seed', 'xxx', 'seed.helper.lazy_import__func7ast', '')
>>> this_mdl.bbb
_LazyImport4Func('seed', 'yyy', 'seed.helper.lazy_import__func7ast', 'bbb')
>>> this_mdl.zzz
_LazyImport4Func('seed', 'zzz', 'seed.helper.lazy_import__func7ast', '')
>>> this_mdl.kkk
_LazyImport4Func('seed', 'kkk', 'seed.helper.lazy_import__func7ast', '')

>>> decorator4lazy_import__funcs_(_f, to_return_nmss4func8dst=True)
Traceback (most recent call last):
    ...
Exception: ('dst exist:', (<module 'seed.helper.lazy_import__func7ast' from '/sdcard/0my_files/git_repos/python3_src/seed/helper/lazy_import__func7ast.py'>, 'xxx'), _LazyImport4Func('seed', 'xxx', 'seed.helper.lazy_import__func7ast', ''))
>>> for k in (_ks1 -_ks0):delattr(this_mdl, k)
>>> (tpl:=decorator4lazy_import__funcs_(_f, to_return_nmss4func8dst=True))
([[_LazyImport4Func('seed', 'xxx', 'seed.helper.lazy_import__func7ast', '')], [_LazyImport4Func('seed', 'yyy', 'seed.helper.lazy_import__func7ast', 'bbb')], [_LazyImport4Func('seed', 'zzz', 'seed.helper.lazy_import__func7ast', ''), _LazyImport4Func('seed', 'kkk', 'seed.helper.lazy_import__func7ast', '')]], [['xxx'], ['bbb'], ['zzz', 'kkk']], '[[xxx], [bbb], [zzz, kkk]]')
>>> tpl[-1] #output:nmss4func8dst__str
'[[xxx], [bbb], [zzz, kkk]]'

>>> for k in (_ks1 -_ks0):delattr(this_mdl, k)
>>> [[xxx], [bbb], [zzz, kkk]] = decorator4lazy_import__funcs_(_f) #using:nmss4func8dst__str




py_adhoc_call   seed.helper.lazy_import__func7ast   ,_test
]]]'''#'''
__all__ = r'''
decorator4lazy_import__funcs_
mk_decorator4lazy_import__funcs_


helper4decorator4lazy_import__funcs_
    worker4decorator4lazy_import__funcs_
        check_kwds4worker
        mk_decorator4lazy_import__funcs_
            decorator4lazy_import__funcs_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from types import FunctionType
import ast
from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge
#from seed.tiny_.types5py import curry1
from seed.helper.lazy_import__func7worker4funcss import worker4lazy_import4funcss_, check_kwds4worker
from seed.helper.lazy_import__func import lazy_import4funcs_
#def lazy_import4funcs_(qnm4mdl8src, xqnms4func8src, smay_qnm4mdl8dst='', /):
lazy_import4funcs_('seed.debug.print_err', 'print_err', __name__)
if 0:from seed.debug.print_err import print_err, print_ferr
lazy_import4funcs_('seed.helper.repr_input', 'repr_helper', __name__)
if 0:from seed.helper.repr_input import repr_helper
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
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


def _f():
    from seed import xxx
    from seed import yyy as bbb
    from seed import zzz,kkk
#end-def _f():
def _test(f=_f, /):
    #from types import FunctionType
    #assert callable(f)
    check_type_is(FunctionType, f)

    ts = list(f.__code__.co_lines())
        # guess: [(begin_idx6code, end_idx6code, lineno)]
    path = f.__code__.co_filename
    j4f = f.__code__.co_firstlineno
    j0 = ts[0][2]
    j4end = ts[-1][2]
    assert j0 >= 1, j0
    assert j4f == j0 >= 1, j4f
    assert j4end >= j4f == j0 >= 1, (j4end, j0)
    with open(path, 'rt', encoding='utf8') as ifile:
        #txt = ''.join(islice(iter(ifile), j0-1, j4end-1))
        #txt = ''.join(islice(iter(ifile), j0, j4end))
        txt = ''.join(islice(iter(ifile), j0-1, j4end+0))
    #print(__name__)
    #print(txt)
    if f is _f:
        assert 1 == txt.count('def')
        assert 0 == txt.rindex('def')
        assert 'kkk' in txt
        assert len(txt)-4 == txt.rindex('kkk')

    #import ast
    ast_tree = ast.parse(txt)
    #return (txt, ast_tree)
    check_type_is(ast.Module, ast_tree)
    assert [] == ast_tree.type_ignores
    assert 1 == len(ast_tree.body)
    node4f = ast_tree.body[0]
    check_type_is(ast.FunctionDef, node4f)
    #return (path, j0, j4end, txt, ast_tree, node4f)
    assert node4f.decorator_list == []
    assert node4f.returns is None
    assert node4f.type_comment is None
    args4f = node4f.args
    assert all(getattr(args4f, nm) in ([], None) for nm in args4f._fields), [(nm, getattr(args4f, nm)) for nm in args4f._fields]
    stmts = node4f.body
    assert all(typ is ast.ImportFrom for typ in map(type, stmts))
    stmts4import_from = stmts
    assert all(stmt.level == 0 for stmt in stmts4import_from)
    mdl__nm_pairs__pairs = [(stmt.module, [(alias.name, alias.asname) for alias in stmt.names]) for stmt in stmts4import_from]
    ######################
    return (path, j0, j4end, txt, ast_tree, node4f, mdl__nm_pairs__pairs)
    ######################
    g = node4f
        # g._fields # 个性#特色属性
        #   ('name', 'args', 'body', 'decorator_list', 'returns', 'type_comment')
        # g._attributes # 共性#共通基础属性
        #   ('lineno', 'col_offset', 'end_lineno', 'end_col_offset')
    g.name
        # == '_f'
    g.args
        # :: ast.arguments
    g.body
        # :: [ast.ImportFrom]
    g.decorator_list
        # == []
    g.returns
        # == None
    g.type_comment
        # == None
    g.end_col_offset
        # == 28
    g.col_offset
        # == 0
    g.end_lineno
        # == 4
    g.lineno
        # == 1
    ######################
    g.args
        # :: ast.arguments
        #   ('posonlyargs', 'args', 'vararg', 'kwonlyargs', 'kw_defaults', 'kwarg', 'defaults')
        #   all be [], except kwarg/vararg be None
    ######################
    g.body
        # :: [ast.ImportFrom]
        #   ('module', 'names', 'level')
        #       #level==0
        #       #names :: [ast.alias] # ~ [('name', 'asname')]
    ######################
#_test()

def helper4decorator4lazy_import__funcs_(f, smay_qnm4mdl8dst, /):
    check_type_is(FunctionType, f)
    check_type_is(str, smay_qnm4mdl8dst)
    qnm4mdl8dst = f.__module__ if not smay_qnm4mdl8dst else smay_qnm4mdl8dst
    assert qnm4mdl8dst

    (path, j0, j4end, txt, ast_tree, node4f, mdl__nm_pairs__pairs) = _test(f)
    return (qnm4mdl8dst, mdl__nm_pairs__pairs)

def worker4decorator4lazy_import__funcs_(f, smay_qnm4mdl8dst, /, **kwds4worker):
    #, **kwds4worker
    #   === , *, to_show_nmss4func8dst=False, to_return_nmss4func8dst=False
    (qnm4mdl8dst, mdl__nm_pairs__pairs) = helper4decorator4lazy_import__funcs_(f, smay_qnm4mdl8dst)
    return worker4lazy_import4funcss_(mdl__nm_pairs__pairs, smay_qnm4mdl8dst:=qnm4mdl8dst, **kwds4worker)

#.def worker4decorator4lazy_import__funcs_(f, smay_qnm4mdl8dst, /, *, to_show_nmss4func8dst=False, to_return_nmss4func8dst=False):
#.    #, **kwds4worker
#.    check_type_is(bool, to_show_nmss4func8dst)
#.    check_type_is(bool, to_return_nmss4func8dst)
#.    (qnm4mdl8dst, mdl__nm_pairs__pairs) = helper4decorator4lazy_import__funcs_(f, smay_qnm4mdl8dst)
#.    nmss4func8dst = []
#.    rss = []
#.    for (qnm4mdl8src, nm_pairs) in mdl__nm_pairs__pairs:
#.        xqnms4func8src = ','.join((f'{nm}:{smay_nm}' if smay_nm else nm) for nm, smay_nm in nm_pairs)
#.        nms4func8dst = [(smay_nm if smay_nm else nm) for nm, smay_nm in nm_pairs]
#.        rs = lazy_import4funcs_(qnm4mdl8src, xqnms4func8src, smay_qnm4mdl8dst:=qnm4mdl8dst)
#.        rss.append(rs)
#.        nmss4func8dst.append(nms4func8dst)
#.    rss
#.    nmss4func8dst
#.    nmss4func8dst__str = _str8list_(map(_str8list_, nmss4func8dst))
#.    if to_show_nmss4func8dst:
#.        print_err(nmss4func8dst__str)
#.    if to_return_nmss4func8dst:
#.        return (rss, nmss4func8dst, nmss4func8dst__str)
#.    return rss
#.def _str8list_(ss, /):
#.    r'[str] -> str # fmt=regex"\[({s}(, {s})*)?\]"'
#.    s = ', '.join(ss)
#.    return f'[{s!s}]'
class _Decorator4lazy_import__funcs:
    def __init__(sf, smay_qnm4mdl8dst='', /, **kwds4worker):
        check_type_is(str, smay_qnm4mdl8dst)
        check_kwds4worker(kwds4worker)
        sf._sm = smay_qnm4mdl8dst
        sf._kw = kwds4worker
    def __repr__(sf, /):
        args = [sf._sm]
        if not args[0]:
            args.pop()
        kwds = {k:v for k,v in sf._kw.items() if v}
        return repr_helper(sf, *args, **kwds)
    def __call__(sf, f_or_may_smay_qnm4mdl8dst=None, may_smay_qnm4mdl8dst=None, /, **kwds4worker):
        may_f = None
        if f_or_may_smay_qnm4mdl8dst is None:
            if not may_smay_qnm4mdl8dst is None:raise TypeError
            smay_qnm4mdl8dst = sf._sm
        elif type(f_or_may_smay_qnm4mdl8dst) is str:
            smay_qnm4mdl8dst = f_or_may_smay_qnm4mdl8dst
            if not may_smay_qnm4mdl8dst is None:raise TypeError
        else:
            f = f_or_may_smay_qnm4mdl8dst
            check_type_is(FunctionType, f)
            may_f = f
            if not may_smay_qnm4mdl8dst is None:
                smay_qnm4mdl8dst = may_smay_qnm4mdl8dst
                check_type_is(str, smay_qnm4mdl8dst)
            else:
                smay_qnm4mdl8dst = sf._sm
            smay_qnm4mdl8dst
        may_f
        smay_qnm4mdl8dst

        kw0 = sf._kw
        if kwds4worker:
            if kw0:
                kw1 = kwds4worker
                kwds4worker = {**kw0, **kw1}
            kwds4worker
        else:
            kwds4worker = kw0
        kwds4worker


        may_f
        smay_qnm4mdl8dst
        kwds4worker
        if may_f is None:
            ot = __class__(smay_qnm4mdl8dst, **kwds4worker)
            return ot
        #f = may_f
        f
        return worker4decorator4lazy_import__funcs_(f, smay_qnm4mdl8dst, **kwds4worker)
#end-class _Decorator4lazy_import__funcs:

def mk_decorator4lazy_import__funcs_(smay_qnm4mdl8dst='', /, **kwds4worker):
    return _Decorator4lazy_import__funcs(smay_qnm4mdl8dst, **kwds4worker)
    ######################
    #.check_type_is(str, smay_qnm4mdl8dst)
    #._kwds4worker = kwds4worker
    #.def decorator4lazy_import__funcs_(f=None, /, **kwds4worker):
    #.    if _kwds4worker:
    #.        ks = kwds4worker.keys() & _kwds4worker.keys()
    #.        if not ks:
    #.            kwds4worker.update(_kwds4worker)
    #.        else:
    #.            #kwds4worker = {**_kwds4worker, **kwds4worker}
    #.            for k, v in _kwds4worker.items():
    #.                if not k in ks:
    #.                    kwds4worker[k] = v
    #.            kwds4worker
    #.        kwds4worker
    #.    kwds4worker
    #.    if f is None:
    #.    return worker4decorator4lazy_import__funcs_(f, smay_qnm4mdl8dst, **kwds4worker)
    #.return _decorator4lazy_import__funcs_
    ######################
decorator4lazy_import__funcs_ = mk_decorator4lazy_import__funcs_()
#.def decorator4lazy_import__funcs_(f__or__smay_qnm4mdl8dst, may_f=None, /):
#.    if type(f__or__smay_qnm4mdl8dst) is str:
#.        smay_qnm4mdl8dst = f__or__smay_qnm4mdl8dst
#.        if not may_f is None:
#.            f = may_f
#.            check_type_is(FunctionType, f)
#.    else:
#.        f = f__or__smay_qnm4mdl8dst
#.        check_type_is(FunctionType, f)
#.        if not may_f is None:raise TypeError
#.        may_f = f
#.        smay_qnm4mdl8dst = ''
#.    may_f, smay_qnm4mdl8dst
#.
#.    if may_f is None:
#.        smay_qnm4mdl8dst
#.        return curry1(decorator4lazy_import__funcs_, smay_qnm4mdl8dst)
#.            #def _decorator4lazy_import__funcs_(f, /):
#.    #f = may_f
#.    f
#.    return worker4decorator4lazy_import__funcs_(f, smay_qnm4mdl8dst)

__all__
from seed.helper.lazy_import__func7ast import helper4decorator4lazy_import__funcs_, worker4decorator4lazy_import__funcs_, mk_decorator4lazy_import__funcs_, decorator4lazy_import__funcs_
from seed.helper.lazy_import__func7ast import mk_decorator4lazy_import__funcs_, decorator4lazy_import__funcs_
from seed.helper.lazy_import__func7ast import *
