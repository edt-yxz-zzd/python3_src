#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/import_stmt_context.py

py -m seed.helper.import_stmt_context
py -m nn_ns.app.debug_cmd   seed.helper.import_stmt_context -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.import_stmt_context:__doc__ -ht # -ff -df
py -m nn_ns.app.doctest_cmd seed.helper.import_stmt_context:_test.doc4ver1 -ht # -ff -df
py -m nn_ns.app.doctest_cmd seed.helper.import_stmt_context:_test.doc4ver2 -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/helper/lazy_import__func7context7register7data.py
==>>:
expected usage:
with mk_context4import_stmts_(name7importZqnm4mdl:={}):
    from xxx.yyy import zzz, www

]]
[[
importlib.__import__(name, globals=None, locals=None, fromlist=(), level=0)
__builtis__
builtins.__import__(name, globals=None, locals=None, fromlist=(), level=0)

spam = __import__('spam.ham', globals(), locals(), [], 0)
    #spam not spam_ham

_temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
eggs = _temp.eggs
saus = _temp.sausage
    Here, the spam.ham module is returned from __import__().


class _new_builtins:
    def __init__(sf, __builtins__, /, **kwds):
        sf._bt = __builtins__
        vars(sf).update(kwds)
    def __getattr__(sf, nm, /):
        return getattr(sf._bt)
def _new_import(*args, **kwds):
    print('_new_import', (args, kwds))
    m = _old_import(*args, **kwds)
    print('_new_import', (args, kwds), m)
    return m
_old_import = __builtins__.__import__
#有效:__builtins__.__import__ = _new_import
#无效:__builtins__ = _new_builtins(__builtins__, __import__=_new_import)

import seed
from collections.abc import Mapping
raise ...
]]



'#'; __doc__ = r'#'
>>> 'mk_context4import_stmts_' # to see which ver: _test.doc4ver2

######################
>>> with mk_context4import_stmts_():
...     from _000_xxx import yyy
...     from _999_xxx import z
...     from _999.xww import xy
>>> yyy
ImportStmt('yyy', '_000_xxx', None)
>>> z
ImportStmt('z', '_999_xxx', None)
>>> xy
ImportStmt('xy', '_999.xww', None)
>>> del yyy, z






######################
>>> with mk_context4import_stmts_():
...     from _000_xxx import z
...     from _999_xxx import z
Traceback (most recent call last):
    ...
seed.helper.import_stmt_context.Conflict: ('z', ('_999_xxx', '_000_xxx'))
>>> z
ImportStmt('z', '_000_xxx', None)
>>> del z

>>> with mk_context4import_stmts_(overwrite_ok=True):
...     from _000_xxx import z
...     from _999_xxx import z
>>> z
ImportStmt('z', '_999_xxx', None)
>>> del z





######################
>>> d = {}
>>> with mk_context4import_stmts_(d):
...     from _000_xxx import yyy
...     from _999_xxx import z
>>> yyy
ImportStmt('yyy', '_000_xxx', None)
>>> z
ImportStmt('z', '_999_xxx', None)
>>> d == {'yyy': '_000_xxx', 'z': '_999_xxx'}
True
>>> del yyy, z, d




######################
>>> with mk_context4import_stmts_(extra=999):
...     from _000_xxx import yyy
>>> yyy
ImportStmt('yyy', '_000_xxx', 999)
>>> del yyy




######################
fail:unknown why:may be stdlib ref to 『sys.modules』 directly via local var name instead via 『sys』
######################
#:::>>> import sys
#:::>>> with mk_context4import_stmts_():
#:::...     from sys import yyy
#:::Traceback (most recent call last):
#:::    ...
#:::ImportError: cannot import name 'yyy' from 'sys' (unknown location)
#:::>>> with mk_context4import_stmts_(None, 'sys os'):
#:::...     from sys import yyy
#:::...     from os.path import z
#:::Traceback (most recent call last):
#:::    ...
#:::ImportError: cannot import name 'yyy' from 'sys' (unknown location)
expect:
#.>>> yyy
#.ImportStmt('yyy', 'sys', None)
#.>>> z
#.ImportStmt('z', 'os', None)
#.>>> del yyy, z
######################
==>>:
######################
now:MOVE_SYS_MODULES
######################
>>> import sys
>>> import os.path
>>> with mk_context4import_stmts_():
...     from sys import yyy
...     from os.path import z
>>> yyy
ImportStmt('yyy', 'sys', None)
>>> z
ImportStmt('z', 'os.path', None)
>>> del yyy, z


######################
#.>>> import seed as xx1
#.>>> with mk_context4import_stmts_(): #doctest: +ELLIPSIS
#....     from seed import yyy
#.Traceback (most recent call last):
#.    ...
#.ImportError: cannot import name 'yyy' from 'seed' (.../seed/__init__.py)
#.>>> with mk_context4import_stmts_():
#....     import seed as xx2
#.>>> xx1 #doctest: +ELLIPSIS
#.<module 'seed' from '.../seed/__init__.py'>
#.>>> xx2 is xx1
#.True
#.>>> with mk_context4import_stmts_(None, 'seed k9d99'):
#....     import seed as xx3
#.>>> xx3
#.
#.>>> with mk_context4import_stmts_(None, 'seed k9d99'):
#....     from seed import yyy
#....     from seed.u09uxxx import z
#.>>> yyy
#.ImportStmt('yyy', 'seed', None)
#.>>> z
#.ImportStmt('z', 'seed.u09uxxx', None)
#.>>> del yyy, z



######################






py_adhoc_call   seed.helper.import_stmt_context   @f
]]]'''#'''
__all__ = r'''
mk_context4import_stmts_
    ImportStmt

mk_context4import_stmts_
    mk_context4import_stmts__ver1_
    mk_context4import_stmts__ver2_

Conflict
BadUsage
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
#.from seed.helper.lazy_import__func7dict import lazy_import__funcs7dict_
#.(check_type_is, check_int_ge, _ifNone) = lazy_import__funcs7dict_(__name__ or globals() or locals(), 'seed.tiny_.check',  'check_type_is, check_int_ge      ifNone:_ifNone')
#.#################################
#.def mk_context4lazy_import_registered_names_(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject={}, may_bifix4lazy_name7import=None, lazy_name7importZoriginal_name7import={}):
#.from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
#.with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
#.    from seed._lazy_ import print_err, fst, echo, ifNone
#.#################################
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__):
#.    from itertools import islice
#.    from functools import cached_property
#.    from seed.for_libs.for_functools.cached_property import cached_property
#.    from seed.types.CachedProperty import CachedProperty, mk_cached_propertyT_
#.    from seed.func_tools.dot2 import dot
#.    from seed.tiny_.check import check_type_is, check_int_ge
#.with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
#.    from seed.data_funcs.lnkls import rglnkls_ops# empty_rglnkls, mk_empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
import sys
from collections.abc import Mapping
from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple_, mk_namedtuple__check6make_
#def mk_namedtuple_(__module__, nm, nms_or_str, /, *args, **kwds):
#def mk_namedtuple__check6make_(__module__, nm, nms_or_str, /, *args, **kwds):
#    def _check6make_(sf, /):


from types import SimpleNamespace
import builtins#__import__
#.from seed.debug.print_err import print_err
def print_err(*args, file=sys.stderr, **kwds):
    print(*args, file=file, **kwds)

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

class Conflict(Exception):pass
class BadUsage(Exception):pass

_ImportStmt = mk_namedtuple__check6make_(__name__, '_ImportStmt', 'name4target  qname4module  extra')
class ImportStmt(_ImportStmt):
    def _check6make_(sf, /):
        assert sf.name4target.isidentifier()
        assert all(nm.isidentifier() for nm in sf.qname4module.split('.'))

def _import_from(mk_ImportStmt, nm4tgt, qnm4mdl, nm4tgtZqnm4mdl, extra, overwrite_ok, /):
    0b000 and print_err(444, qnm4mdl, nm4tgt)
    if not (overwrite_ok or (_qnm4mdl:=nm4tgtZqnm4mdl.get(nm4tgt, qnm4mdl)) == qnm4mdl): raise Conflict(nm4tgt, (qnm4mdl, _qnm4mdl))
    nm4tgtZqnm4mdl[nm4tgt] = qnm4mdl
    return mk_ImportStmt(name4target=nm4tgt, qname4module=qnm4mdl, extra=extra)






_get = object.__getattribute__
_set = object.__setattr__
_nms4bypass = '__spec__ __path__'.split()
class _Mdl4import_stmts:
    def __init__(sf, mk_ImportStmt, qnm4mdl, nm4tgtZqnm4mdl, extra, /, *, overwrite_ok):
        args = (mk_ImportStmt, qnm4mdl, nm4tgtZqnm4mdl, extra, overwrite_ok)
        _set(sf, '_args', args)
        if 0x000_000:
            sf._qnm = qnm4mdl
            sf._nm2qnm = nm4tgtZqnm4mdl
            sf._b = bool(overwrite_ok)
            sf._x = extra
    if 0x000_000:
        @property
        def qnm4mdl(sf, /):
            return sf._qnm
        @property
        def nm4tgtZqnm4mdl(sf, /):
            return sf._nm2qnm
        @property
        def overwrite_ok(sf, /):
            return sf._b
        @property
        def extra(sf, /):
            return sf._x
    def __getattribute__(sf, nm4tgt, /):
        if nm4tgt in _nms4bypass:
            #if nm4tgt == '__path__':
            raise AttributeError(nm4tgt)
            return None
        (mk_ImportStmt, qnm4mdl, nm4tgtZqnm4mdl, extra, overwrite_ok) = _get(sf, '_args')
        return _import_from(mk_ImportStmt, nm4tgt, qnm4mdl, nm4tgtZqnm4mdl, extra, overwrite_ok)
    def __setattr__(sf, nm, v, /):
        raise AttributeError(nm, v)
class _Dict4import_stmts(Mapping):
    def __init__(sf, sys_modules, mk_ImportStmt, nm4tgtZqnm4mdl, qnms4pkg7tgt, extra, /, *, overwrite_ok):
        sf._sd = sys_modules
        sf._mk = mk_ImportStmt
        sf._nm2qnm = nm4tgtZqnm4mdl
        sf._b = bool(overwrite_ok)
        sf._x = extra
        sf._qps = qnms4pkg7tgt
    @property
    def sys_modules(sf, /):
        return sf._sd
    @property
    def mk_ImportStmt(sf, /):
        return sf._mk
    @property
    def nm4tgtZqnm4mdl(sf, /):
        return sf._nm2qnm
    @property
    def overwrite_ok(sf, /):
        return sf._b
    @property
    def extra(sf, /):
        return sf._x
    @property
    def qnms4pkg7tgt(sf, /):
        return sf._qps
    def __len__(sf, /):
        return len(sf.sys_modules)
    def __iter__(sf, /):
        return iter(sf.sys_modules)
    def __getitem__(sf, qnm4mdl, /):
        0b000 and print_err(111, qnm4mdl, sf.qnms4pkg7tgt, qnm4mdl in sf.sys_modules)
        if 0x0_00000:
          000
            #MOVE_SYS_MODULES
          if not (mdl:=sf.sys_modules.get(qnm4mdl, Nothing:=[])) is Nothing:
            0b000 and print_err(222, qnm4mdl)
            under_tgt_pkg = False
            for qnm4pkg7tgt in sf.qnms4pkg7tgt:
                0b000 and print_err(333, qnm4mdl, qnm4pkg7tgt)
                if qnm4mdl.startswith(qnm4pkg7tgt) and (len(qnm4mdl) == len(qnm4pkg7tgt) or qnm4mdl[len(qnm4pkg7tgt)] == '.'):
                    under_tgt_pkg = True
                    break
            under_tgt_pkg
            if not under_tgt_pkg:
                return mdl
        return _Mdl4import_stmts(sf.mk_ImportStmt, qnm4mdl, sf.nm4tgtZqnm4mdl, sf.extra, overwrite_ok=sf.overwrite_ok)
class _Ctx4import_stmts__ver1:
    def __init__(sf, mk_ImportStmt, nm4tgtZqnm4mdl, qnms4pkg7tgt, extra, /, *, overwrite_ok):
        nm4tgtZqnm4mdl.items()
        sf._mk = mk_ImportStmt
        sf._nm2qnm = nm4tgtZqnm4mdl
        sf._b = bool(overwrite_ok)
        sf._x = extra
        sf._qps = qnms4pkg7tgt
        sf._d = None
        sf._m = None
        sf._mc = None
    @property
    def mk_ImportStmt(sf, /):
        return sf._mk
    @property
    def nm4tgtZqnm4mdl(sf, /):
        return sf._nm2qnm
    @property
    def overwrite_ok(sf, /):
        return sf._b
    @property
    def extra(sf, /):
        return sf._x
    @property
    def qnms4pkg7tgt(sf, /):
        return sf._qps
    def __enter__(sf, /):
        if not sf._mc is None:raise BadUsage('reenter')
        if not sf._m is None:raise BadUsage('reenter')
        if not sf._d is None:raise BadUsage('reenter')
        sf._d = _Dict4import_stmts(sys.modules, sf.mk_ImportStmt, sf.nm4tgtZqnm4mdl, sf.qnms4pkg7tgt, sf.extra, overwrite_ok=sf.overwrite_ok)
        sf._m = sys.modules
        sf._mc = sys.modules.copy()#MOVE_SYS_MODULES
        if sf._m is None:raise BadUsage('unknown err')
        sys.modules = sf._d
        sf._m.clear()#MOVE_SYS_MODULES
    def __exit__(sf, /, *exc_info):
        if sf._mc is None:raise BadUsage('unknown err')
        if sf._m is None:raise BadUsage('unknown err')
        if sf._d is None:raise BadUsage('unknown err')
        if not sf._d is sys.modules:raise BadUsage('unknown err')
        ks = sorted(sf._m)
        sf._m.update(sf._mc)#MOVE_SYS_MODULES
        sys.modules = sf._m
        sf._mc = None
        sf._m = None
        sf._d = None
        if ks:raise BadUsage(ks)
        return False

class _NewImport:
    '_new_import'
    def __init__(sf, mk_ImportStmt, nm4tgtZqnm4mdl, extra, /, *, overwrite_ok):
        sf._args = (mk_ImportStmt, nm4tgtZqnm4mdl, extra, overwrite_ok)
    builtins.__import__
    def __call__(sf, /, name, globals=None, locals=None, fromlist=(), level=0):
        qnm4mdl = name
        if not 0 == level:raise BadUsage(qnm4mdl, level)
        if qnm4mdl[0] == '.':raise BadUsage(qnm4mdl)
        if not fromlist:raise BadUsage(qnm4mdl)

        (mk_ImportStmt, nm4tgtZqnm4mdl, extra, overwrite_ok) = sf._args
        ns = SimpleNamespace()
        for nm4tgt in fromlist:
            tgt = _import_from(mk_ImportStmt, nm4tgt, qnm4mdl, nm4tgtZqnm4mdl, extra, overwrite_ok)
            setattr(ns, nm4tgt, tgt)
        return ns
class _Ctx4import_stmts__ver2:
    def __init__(sf, mk_ImportStmt, nm4tgtZqnm4mdl, qnms4pkg7tgt, extra, /, *, overwrite_ok):
        _new_import = _NewImport(mk_ImportStmt, nm4tgtZqnm4mdl, extra, overwrite_ok=overwrite_ok)
        nm4tgtZqnm4mdl.items()
        sf._mk = mk_ImportStmt
        sf._nm2qnm = nm4tgtZqnm4mdl
        sf._b = bool(overwrite_ok)
        sf._x = extra
        sf._qps = qnms4pkg7tgt
        sf._new_import = _new_import
        sf._old_import = None
    @property
    def mk_ImportStmt(sf, /):
        return sf._mk
    @property
    def nm4tgtZqnm4mdl(sf, /):
        return sf._nm2qnm
    @property
    def overwrite_ok(sf, /):
        return sf._b
    @property
    def extra(sf, /):
        return sf._x
    @property
    def qnms4pkg7tgt(sf, /):
        return sf._qps
    @property
    def new_import(sf, /):
        return sf._new_import
    @property
    def old_import(sf, /):
        return sf._old_import
    def __enter__(sf, /):
        if not sf._old_import is None:raise BadUsage('reenter')
        sf._old_import = builtins.__import__
        if sf._old_import is None:raise BadUsage('unknown err')
        builtins.__import__ = sf._new_import
    def __exit__(sf, /, *exc_info):
        if sf._old_import is None:raise BadUsage('unknown err')
        builtins.__import__ = sf._old_import
        sf._old_import = None
        return False



def mk_context4import_stmts__ver1_(nm4tgtZqnm4mdl=None, /, *, mk_ImportStmt=None, extra=None, overwrite_ok=False, ver=1):
    return mk_context4import_stmts_(nm4tgtZqnm4mdl, mk_ImportStmt=mk_ImportStmt, extra=extra, overwrite_ok=overwrite_ok, ver=ver)
def mk_context4import_stmts__ver2_(nm4tgtZqnm4mdl=None, /, *, mk_ImportStmt=None, extra=None, overwrite_ok=False, ver=2):
    return mk_context4import_stmts_(nm4tgtZqnm4mdl, mk_ImportStmt=mk_ImportStmt, extra=extra, overwrite_ok=overwrite_ok, ver=ver)
def mk_context4import_stmts_(nm4tgtZqnm4mdl=None, /, *, mk_ImportStmt=None, extra=None, overwrite_ok=False, ver=2):
    777;qnms4pkg7tgt=()
    #def mk_context4import_stmts_(nm4tgtZqnm4mdl=None, qnms4pkg7tgt=(), /, *, extra=None, overwrite_ok=False):
    if not type(overwrite_ok) is bool:raise TypeError
    if qnms4pkg7tgt:raise TypeError#MOVE_SYS_MODULES

    mk_ImportStmt = ImportStmt if mk_ImportStmt is None else mk_ImportStmt
    assert callable(mk_ImportStmt)


    nm4tgtZqnm4mdl = {} if nm4tgtZqnm4mdl is None else nm4tgtZqnm4mdl
    777;nm4tgtZqnm4mdl.items()



    if type(qnms4pkg7tgt) is str:
        qnms4pkg7tgt = qnms4pkg7tgt.split()
    if not type(qnms4pkg7tgt) is tuple:
        qnms4pkg7tgt = tuple(qnms4pkg7tgt)

    #_Ctx4import_stmts__ver2
    Ctx = _ver2Ctx[ver]
    return Ctx(mk_ImportStmt, nm4tgtZqnm4mdl, qnms4pkg7tgt, extra, overwrite_ok=overwrite_ok)
_ver2Ctx = {1:_Ctx4import_stmts__ver1, 2:_Ctx4import_stmts__ver2}

class _Test:
    def mk_doc4verX(sf, /, ver):
        nmX = f'mk_context4import_stmts__ver{ver}_'
        nmO = 'mk_context4import_stmts_'
        return __doc__.replace(nmO, nmX)
    @property
    def doc4ver1(sf, /):
        return sf.mk_doc4verX(1)
    @property
    def doc4ver2(sf, /):
        return sf.mk_doc4verX(2)
_test = _Test()

def __():
    with mk_context4import_stmts_(None, 'sys os'):
        from os.path import z
        from sys import yyy
if __name__ == '__main__':
    __()






__all__
from seed.helper.import_stmt_context import Conflict, BadUsage
from seed.helper.import_stmt_context import mk_context4import_stmts__ver1_, mk_context4import_stmts__ver2_
from seed.helper.import_stmt_context import mk_context4import_stmts_, ImportStmt
#ImportStmt(name4target, qname4module, extra)
#def mk_context4import_stmts_(nm4tgtZqnm4mdl=None, /, *, extra=None, overwrite_ok=False):
#with mk_context4import_stmts_(name7importZqnm4mdl:={}):
#    from xxx.yyy import zzz, www
from seed.helper.import_stmt_context import *
