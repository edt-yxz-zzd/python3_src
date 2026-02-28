#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/lazy_import__func7context7register.py

seed.helper.lazy_import__func7context7register
py -m nn_ns.app.debug_cmd   seed.helper.lazy_import__func7context7register -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.lazy_import__func7context7register:__doc__ -ht # -ff -df
###py -m doctest  ../../python3_src/seed/helper/lazy_import__func7context7register.py
#######

[[
expected:
with mk_context4lazy_import_registered_names_(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject, may_bifix4lazy_name7import, lazy_name7importZoriginal_name7import):
with mk_context4lazy_import_registered_names_(qnm4mdl7inject:=__name__, qnm4pseudo_mdl7import:='seed._lazy_', name7importZqnm4mdl):
    from seed._lazy_ import print_err, fst, echo, ...
]]


'#'; __doc__ = r'#'
>>> import seed.helper.lazy_import__func7context7register as mdl
>>> from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
>>> with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
...     from seed._lazy_ import print_err, fst, echo, ifNone

>>> __name__
'seed.helper.lazy_import__func7context7register'
>>> print_err
_LazyImport4Func('seed.debug.print_err', 'print_err', 'seed.helper.lazy_import__func7context7register', 'print_err')
>>> fst
_LazyImport4Func('seed.tiny_.funcs', 'fst', 'seed.helper.lazy_import__func7context7register', 'fst')
>>> hasattr(mdl, 'echo')
True
>>> mdl.echo is echo
True
>>> echo
_LazyImport4Func('seed.tiny_.funcs', 'echo', 'seed.helper.lazy_import__func7context7register', 'echo')
>>> echo(fst) is fst
True
>>> echo
_LazyImport4Func('seed.tiny_.funcs', 'echo', 'seed.helper.lazy_import__func7context7register', 'echo')
>>> hasattr(mdl, 'echo')
True
>>> mdl.echo is echo
False
>>> mdl.echo   #doctest: +ELLIPSIS
<function <lambda> at 0x...>




def mk_context4lazy_import_registered_names_(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject={}, may_bifix4lazy_name7import=None, lazy_name7importZoriginal_name7import={}):
>>> with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny, name7importZalias7inject={'echo':'echo_'}):
...     from seed._lazy_ import echo as echo_
>>> hasattr(mdl, 'echo_')
True
>>> mdl.echo_ is echo_
True
>>> echo_
_LazyImport4Func('seed.tiny_.funcs', 'echo', 'seed.helper.lazy_import__func7context7register', 'echo_')
>>> echo_(fst) is fst
True
>>> echo_
_LazyImport4Func('seed.tiny_.funcs', 'echo', 'seed.helper.lazy_import__func7context7register', 'echo_')
>>> hasattr(mdl, 'echo_')
True
>>> mdl.echo_ is echo_
False
>>> mdl.echo_   #doctest: +ELLIPSIS
<function <lambda> at 0x...>





>>> with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny, lazy_name7importZoriginal_name7import={'lazy_null_tuple':'null_tuple'}):
...     from seed._lazy_ import lazy_null_tuple
>>> lazy_null_tuple
_LazyImport8LazyObj('seed.tiny_.containers', 'null_tuple', None)
>>> lazy_null_tuple() is lazy_null_tuple()
True
>>> lazy_null_tuple()
()
>>> lazy_null_tuple
_LazyImport8LazyObj('seed.tiny_.containers', 'null_tuple', None)
>>> hasattr(mdl, 'lazy_null_tuple')
False



>>> with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny, may_bifix4lazy_name7import=('lazy_','_')):
...     from seed._lazy_ import lazy_null_tuple_
>>> lazy_null_tuple_
_LazyImport8LazyObj('seed.tiny_.containers', 'null_tuple', None)
>>> lazy_null_tuple_() is lazy_null_tuple_()
True
>>> lazy_null_tuple_()
()
>>> lazy_null_tuple_
_LazyImport8LazyObj('seed.tiny_.containers', 'null_tuple', None)
>>> hasattr(mdl, 'lazy_null_tuple_')
False

#>>> dir(mdl)








py_adhoc_call   seed.helper.lazy_import__func7context7register   @f
]]]'''#'''
__all__ = r'''
mk_context4lazy_import_registered_names_
    name7importZqnm4mdl_7tiny

BadUsage
remove_may_bifix4lazy_name7import_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
import sys
777;sys.modules
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import8lazy_obj_
#.def lazy_import4func_(qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst='', smay_nm4func8dst='', /):
#.def lazy_import8lazy_obj_(qnm4mdl8src, smay_qnm4obj8src, may_either_mdl_obj=None, /):
___end_mark_of_excluded_global_names__0___ = ...


class BadUsage(BaseException):pass
class _Args4lazy_import_registered_names(tuple):
    def __new__(cls, qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject, may_bifix4lazy_name7import, lazy_name7importZoriginal_name7import, /):
        #qnm4mdl7inject:0, qnm4pseudo_mdl7import:1, name7importZqnm4mdl:2, name7importZalias7inject:3, may_bifix4lazy_name7import:4, lazy_name7importZoriginal_name7import:5
        sf = tuple.__new__(cls, [qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject, may_bifix4lazy_name7import, lazy_name7importZoriginal_name7import])
        return sf
    @property
    def qnm4mdl7inject(sf, /):
        return sf[0]
    @property
    def qnm4pseudo_mdl7import(sf, /):
        return sf[1]
    @property
    def name7importZqnm4mdl(sf, /):
        return sf[2]
    @property
    def name7importZalias7inject(sf, /):
        return sf[3]
    @property
    def may_bifix4lazy_name7import(sf, /):
        return sf[4]
    @property
    def lazy_name7importZoriginal_name7import(sf, /):
        return sf[5]
_get = object.__getattribute__
_nms7bypass = ('__spec__', '__path__', )
class _Module4lazy_import_registered_names:
    #def __init__(sf, args4import, qnm4mdl, /):
    def __init__(sf, args4import, /):
        sf._args4import = args4import
        sf._d = {}
    def __getattribute__(sf, _nm4obj_, /):
        if _nm4obj_ in _nms7bypass:
            return None

        args4import = _get(sf, '_args4import')
        d = _get(sf, '_d')
        (qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject, may_bifix4lazy_name7import, lazy_name7importZoriginal_name7import) = args4import
        nm4obj = remove_may_bifix4lazy_name7import_(may_bifix4lazy_name7import, _nm4obj_)
        nm4obj7import = lazy_name7importZoriginal_name7import.get(nm4obj, nm4obj)
        if nm4obj7import in d:
            return d[nm4obj7import]
        try:
            qnm4mdl7import = name7importZqnm4mdl[nm4obj7import]
        except KeyError:
            raise BadUsage('no qnm4mdl7import@name7importZqnm4mdl:', _nm4obj_, nm4obj7import)
        qnm4mdl7import
        nm4obj7inject = name7importZalias7inject.get(nm4obj7import, nm4obj7import)
        qnm4mdl7inject
        b_lazy_obj = not (nm4obj7import == _nm4obj_)
        if b_lazy_obj:
            x = lazy_obj = lazy_import8lazy_obj_(qnm4mdl8src:=qnm4mdl7import, smay_qnm4obj8src:=nm4obj7import)
        else:
            x = lazy_func = lazy_import4func_(qnm4mdl8src:=qnm4mdl7import, qnm4func8src:=nm4obj7import, smay_qnm4mdl8dst:=qnm4mdl7inject, smay_nm4func8dst:=nm4obj7inject)
        x
        777;d[nm4obj7import] = x
        return x
def remove_may_bifix4lazy_name7import_(may_bifix4lazy_name7import, _nm4obj_, /):
    match may_bifix4lazy_name7import:
        case None:
            nm4obj = _nm4obj_
        case (prefix, suffix):
            if len(_nm4obj_) > len(prefix)+len(suffix) and _nm4obj_.startswith(prefix) and _nm4obj_.endswith(suffix):
                nm4obj = _nm4obj_[len(prefix):len(_nm4obj_)-len(suffix)]
            else:
                nm4obj = _nm4obj_
        case _:
            raise TypeError(may_bifix4lazy_name7import)
        #case _:
    nm4obj
    return nm4obj
class _Dict4lazy_import_registered_names:
    def __init__(sf, sys_modules, args4import, /):
        sf._pseudo_mdl = _Module4lazy_import_registered_names(args4import)
        sf._args4import = args4import
        sf._qnm4pseudo_mdl7import = args4import.qnm4pseudo_mdl7import
        sf._qnm4mdl7inject = args4import.qnm4mdl7inject
        sf._qnm2mdl = sys_modules
        if sf._qnm4pseudo_mdl7import in sys_modules:raise BadUsage('exist:', sf._qnm4pseudo_mdl7import)
    def __getitem__(sf, qnm4mdl, /):
        #if qnm4mdl == sf._qnm4mdl7inject:
        if not None is (mdl:=sf._qnm2mdl.get(qnm4mdl)):
            return mdl
        if not qnm4mdl == sf._qnm4pseudo_mdl7import: raise BadUsage(sf._qnm4pseudo_mdl7import, qnm4mdl)
        return sf._pseudo_mdl
    def __contains__(sf, qnm4mdl, /):
        return True
    def get(sf, qnm4mdl, default=None, /):
        return sf[qnm4mdl]
class _Ctx4lazy_import_registered_names:
    def __init__(sf, args4import, /):
        sf._args4import = args4import
        sf._d = None
        #sf._d = _Dict4lazy_import_registered_names(args4import)
        sf._m = None
    def __enter__(sf, /):
        if not sf._m is None:raise BadUsage('reenter')
        if not sf._d is None:raise BadUsage('reenter')
        sf._d = _Dict4lazy_import_registered_names(sys.modules, sf._args4import)
        sf._m = sys.modules
        if sf._m is None:raise BadUsage('unknown err')
        sys.modules = sf._d
    def __exit__(sf, /, *exc_info):
        if sf._m is None:raise BadUsage('unknown err')
        if sf._d is None:raise BadUsage('unknown err')
        if not sf._d is sys.modules:raise BadUsage('unknown err')
        sys.modules = sf._m
        sf._m = None
        sf._d = None
        return False

def mk_context4lazy_import_registered_names_(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject={}, may_bifix4lazy_name7import=None, lazy_name7importZoriginal_name7import={}):
    args4import = _Args4lazy_import_registered_names(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject, may_bifix4lazy_name7import, lazy_name7importZoriginal_name7import)
    ctx = _Ctx4lazy_import_registered_names(args4import)
    return ctx

if 1:from seed.helper.lazy_import__func7context7register7data import name7importZqnm4mdl as name7importZqnm4mdl_7tiny
__all__
from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
#.def mk_context4lazy_import_registered_names_(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject={}, may_bifix4lazy_name7import=None, lazy_name7importZoriginal_name7import={}):
from seed.helper.lazy_import__func7context7register import *
