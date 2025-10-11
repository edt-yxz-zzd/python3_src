#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/lazy_import__func7context.py
[[

e script/trial_impl___lazy_import__with.py
mv -iv script/trial_impl___lazy_import__with.py ../../python3_src/seed/helper/lazy_import__func7context.py
%s/script[.]trial_impl___lazy_import__with/seed.helper.lazy_import__func7context/g
]]


seed.helper.lazy_import__func7context
py -m nn_ns.app.debug_cmd   seed.helper.lazy_import__func7context -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.lazy_import__func7context:__doc__ -ht # -ff -df
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.helper.lazy_import__func7context:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
copy from:mk_ctx4lazy_import4funcs_.__doc__
===
usage:
    with mk_ctx4lazy_import4funcs_(__name__):
        from seed.tiny_.types5py import mk_MapView,curry1,kwargs2Attrs
        from seed.helper.ifNone import ifNone,ifNonef
    with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
        from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef

NOTE:not support 『as』:
    from seed.helper.ifNone import ifNone as _ifNone
        ==>> 『_ifNone』 always be _LazyImport4Func object
        ==>> 『ifNone』 will be injected unexpectedly

]]
[[
源起:
try to convert:
    lazy_import4funcs_('seed.tiny_.types5py', 'mk_MapView,curry1,kwargs2Attrs', __name__)
    if 0:from seed.tiny_.types5py import mk_MapView,curry1,kwargs2Attrs #,MapView
into:
    #with ctx4lazy_import4funcs:
    with mk_ctx4lazy_import4funcs_(__name__):
        from seed.tiny_.types5py import mk_MapView,curry1,kwargs2Attrs #,MapView
怎么实现？
    开启语境:插入IMetaPathFinder:
        若seed.tiny_.types5py已存在，则无为
        否则:需得提供一个伪模块
            入栈:退出动作:.invalidate_caches();删除sys.modules['seed.tiny_.types5py']
    退出语境:执行退出动作;删除IMetaPathFinder
上面的方案太复杂
考虑容易点的方案，直接替换sys.module:
    开启语境:
        sys.module = wrap_(sys.module)
            # 或:depth+=1
    退出语境:
        sys.module = unwrap_(sys.module)
            # 或:depth-=1
    NOTE:not support 『as』
]]
[[
xxx:不使用第一种方案
view ../../python3_src/seed/for_libs/for_importlib.py

class IMetaPathFinder(MetaPathFinder, ABC):
    @abstractmethod
    def invalidate_caches(self, /):
        :: -> None

    @abstractmethod
    def find_spec(self, fullname, may_paths6parent, target=None, /):
        :: qnm4mdl -> may [path6parenth]/parent.__path__ -> may mdl_obj -> may spec | ^ImportError


]]



'#'; __doc__ = r'#'
>>> with mk_ctx4lazy_import4funcs_(__name__):
...     from seed.tiny_.types5py import mk_MapView,curry1,kwargs2Attrs #,MapView
>>> import seed.helper.lazy_import__func7context as M
>>> type(M.mk_MapView)
<class 'seed.helper.lazy_import__func._LazyImport4Func'>
>>> (M.mk_MapView)
_LazyImport4Func('seed.tiny_.types5py', 'mk_MapView', 'seed.helper.lazy_import__func7context', '')
>>> M.mk_MapView({})
mappingproxy({})
>>> type(M.mk_MapView)
<class 'function'>
>>> (M.mk_MapView)  #doctest: +ELLIPSIS
<function mk_MapView at 0x...>



>>> with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef : _ifNonef '):
...     from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
>>> import seed.helper.lazy_import__func7context as M


>>> M.ifNone
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func7context' has no attribute 'ifNone'
>>> M.ifNonef
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func7context' has no attribute 'ifNonef'


>>> type(M._ifNone)
<class 'seed.helper.lazy_import__func._LazyImport4Func'>
>>> (M._ifNone)
_LazyImport4Func('seed.helper.ifNone', 'ifNone', 'seed.helper.lazy_import__func7context', '_ifNone')
>>> M._ifNone(None, 333)
333
>>> type(M._ifNone)
<class 'function'>
>>> (M._ifNone)  #doctest: +ELLIPSIS
<function ifNone at 0x...>


>>> type(M._ifNonef)
<class 'seed.helper.lazy_import__func._LazyImport4Func'>
>>> (M._ifNonef)
_LazyImport4Func('seed.helper.ifNone', 'ifNonef', 'seed.helper.lazy_import__func7context', '_ifNonef')
>>> M._ifNonef(None, lambda:333)
333
>>> type(M._ifNonef)
<class 'function'>
>>> (M._ifNonef)  #doctest: +ELLIPSIS
<function ifNonef at 0x...>


>>> M.ifNone
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func7context' has no attribute 'ifNone'
>>> M.ifNonef
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func7context' has no attribute 'ifNonef'



>>> mapping4alias5or_str_('') is _empty__mapping4alias
True
>>> mapping4alias5or_str_('   ') is _empty__mapping4alias
True
>>> mapping4alias5or_str_('k:v')
{'k': 'v'}
>>> mapping4alias5or_str_(' k : v ')
{'k': 'v'}
>>> mapping4alias5or_str_('k:v,a:b,ccc:ddd') == {'k': 'v', 'a': 'b', 'ccc': 'ddd'}
True
>>> mapping4alias5or_str_('  k  :  v  ,  a  :  b  ,  ccc  :  ddd  ') == {'k': 'v', 'a': 'b', 'ccc': 'ddd'}
True


py_adhoc_call   seed.helper.lazy_import__func7context   @f
]]]'''#'''
__all__ = r'''
mk_ctx4lazy_import4funcs_
    Context4LazyImport4Func
    Wrapper4the_sys_modules_dict
    PseudoModule4lazy_import4func






mapping4alias5or_str_
    mapping4alias5str_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import sys
from collections.abc import Mapping
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
#.
#.:s/\v^from +([_[:alnum:].]+) +import +([^# ]( *[^# ])*).*/lazy_import4funcs_('\1', '\2', __name__)\rif 0:\0
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_
#.repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
#.
#.lazy_import4funcs_('seed.debug.print_err', 'print_err', __name__)
#.if 0:from seed.debug.print_err import print_err
#.
#.
___end_mark_of_excluded_global_names__0___ = ...


__all__






#_depth, _sys_modules
sys.modules
dict.__contains__
_get = object.__getattribute__
_set = object.__setattr__
_special_nms = '__spec__ __path__'.split()
    # ??? sys directly update mdl.__dict__ ???
_special_nms = frozenset(
r'''
__builtins__
__cached__
__doc__
__file__
__loader__
__name__
__package__
__path__
__spec__

__class__
__dict__
__all__
'''.split()#'''
)

class PseudoModule4lazy_import4func:
    'pseudo_mdl{lazy_import4func}  # role relations:[mdl{dst}.attr{nm} := mdl{src}.attr{nm}]'
    def __init__(sf, qnm4mdl8src, qnm4mdl8dst, mapping4alias, /):
        #.sf._qnm4mdl8src = qnm4mdl8src
        #.sf._qnm4mdl8dst = qnm4mdl8dst
        #.sf._d4alias = mapping4alias
        #.sf._d = {}
        _set(sf, '__name__', qnm4mdl8src)
        _set(sf, '_qnm4mdl8src', qnm4mdl8src)
        _set(sf, '_qnm4mdl8dst', qnm4mdl8dst)
        _set(sf, '_d4alias', mapping4alias)
        _set(sf, '_d', {})
    def __setattr__(sf, nm, x, /):
        d = _get(sf, '_d')
        d[nm] = x
    def __getattribute__(sf, nm, /):
        if nm[-2:] == '__' == nm[:2] and nm in _special_nms:
            return _get(sf, nm)
        d = _get(sf, '_d')
        m = d.get(nm)
        if not m is None:
            return m
        qnm4src = _get(sf, '_qnm4mdl8src')
        qnm4dst = _get(sf, '_qnm4mdl8dst')
        mapping4alias = _get(sf, '_d4alias')
        # role relations:[mdl{dst}.attr{nm} := mdl{src}.attr{nm}]
        smay_alias = mapping4alias.get(nm, '')
        x = lazy_import4func_(qnm4src, nm, qnm4dst, smay_alias)
            #def lazy_import4func_(qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst='', smay_nm4func8dst='', /):
        #d[nm] = x
        setattr(sf, nm, x)
        #return x
        return getattr(sf, nm)
class Wrapper4the_sys_modules_dict(Mapping):
    #def __init__(sf, qnm4mdl8dst, d, depth, /):
    #def __init__(sf, qnm4mdl8dst, mapping4alias, d, /):
    def __new__(cls, qnm4mdl8dst, mapping4alias, d, /):
        if type(d) is Wrapper4the_sys_modules_dict and qnm4mdl8dst in [d._qnm4mdl8dst] and mapping4alias in [d._d4alias]:
            sf = d
        else:
            sf = super(__class__, cls).__new__(cls)
            sf._qnm4mdl8dst = qnm4mdl8dst
            sf._d4alias = mapping4alias
            #.sf._original_d = d
            #.while type(d) is Wrapper4the_sys_modules_dict and qnm4mdl8dst in [d._qnm4mdl8dst] and mapping4alias in [d._d4alias]:
            #.    d = d._d
            sf._d = d
            sf._d4missing = {}
            #sf._depth = depth
        sf
        return sf
    #.if 0:
    #.    def the_wrapped_dict(sf, /):
    #.        return sf._original_d
    def _mk_pseudo_mdl4lazy_import4func_(sf, qnm4mdl8src, /):
        'qnm4mdl -> pseudo_mdl{lazy_import4func}'
        return PseudoModule4lazy_import4func(qnm4mdl8src, sf._qnm4mdl8dst, sf._d4alias)
    #TypeError: Can't instantiate abstract class Wrapper4the_sys_modules_dict with abstract methods __getitem__, __iter__, __len__
    def __getitem__(sf, qnm4mdl, /):
        m = sf._d.get(qnm4mdl)
        if not m is None:
            return m
        m = sf._d4missing.get(qnm4mdl)
        if not m is None:
            return m
        mdl = sf._mk_pseudo_mdl4lazy_import4func_(qnm4mdl)
        sf._d4missing[qnm4mdl] = mdl
        return sf[qnm4mdl]
        return mdl
    def __len__(sf, /):
        return len(sf._d4missing)+len(sf._d)
    def __iter__(sf, /):
        yield from iter(sf._d4missing)
        yield from iter(sf._d)
    if 1:
        def __contains__(sf, qnm4mdl, /):
            #sf[qnm4mdl]
            return True
        def get(sf, qnm4mdl, default=None, /):
            return sf[qnm4mdl]


class Context4LazyImport4Func:
    def __init__(sf, qnm4mdl8dst, str_or_mapping4alias, /):
        sf._qnm4mdl8dst = qnm4mdl8dst
        sf._d4alias = mapping4alias5or_str_(str_or_mapping4alias)
        sf._st = 0
        sf._saved_sys_modules = None
    #@override
    def __enter__(sf, /):
        if not sf._st == 0:raise Exception
        sf._saved_sys_modules = d = sys.modules
        sys.modules = Wrapper4the_sys_modules_dict(sf._qnm4mdl8dst, sf._d4alias, d)
        sf._st = 1
        return None
    #@override
    def __exit__(sf, /, *excinfo):
        #sf.close()
        if not sf._st == 1:raise Exception
        sys.modules = sf._saved_sys_modules
        sf._saved_sys_modules = None
        sf._st = 0
        return False

def mk_ctx4lazy_import4funcs_(qnm4mdl8dst, str_or_mapping4alias='', /):
    r'''
usage:
    with mk_ctx4lazy_import4funcs_(__name__):
        from seed.tiny_.types5py import mk_MapView,curry1,kwargs2Attrs
        from seed.helper.ifNone import ifNone,ifNonef
    with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
        from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef

NOTE:not support 『as』:
    from seed.helper.ifNone import ifNone as _ifNone
        ==>> 『_ifNone』 always be _LazyImport4Func object
        ==>> 『ifNone』 will be injected unexpectedly
    '''#'''
    return Context4LazyImport4Func(qnm4mdl8dst, str_or_mapping4alias)


class _Empty__mapping4alias:
    def get(sf, k, v=None, /):
        return v
_empty__mapping4alias = _Empty__mapping4alias()
def _parse_item(s, /):
    match s.split(':'):
        case (nm, alias):
            pass
        case _:
            raise ValueError(s)
    nm = nm.strip()
    alias = alias.strip()
    if not nm.isidentifier():raise ValueError(nm)
    if not alias.isidentifier():raise ValueError(alias)
    return (nm, alias)
def mapping4alias5str_(s, /):
    'str -> mapping4alias/{nm:alias}'
    s = s.strip()
    if not s:
        return _empty__mapping4alias
    mapping4alias = dict(map(_parse_item, s.split(',')))
    if not mapping4alias:
        mapping4alias = _empty__mapping4alias
    return mapping4alias
def mapping4alias5or_str_(str_or_mapping4alias, /):
    '(str|mapping4alias) -> mapping4alias/{nm:alias}'
    #if isinstance(str_or_mapping4alias, str)
    if type(str_or_mapping4alias) is str:
        s = str_or_mapping4alias
        return mapping4alias5str_(s)
    mapping4alias = str_or_mapping4alias
    return mapping4alias







__all__
#lazy_import4funcs_('seed.helper.lazy_import__func7context', 'mk_ctx4lazy_import4funcs_', __name__)
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
from seed.helper.lazy_import__func7context import *
