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
py -m nn_ns.app.doctest_cmd seed.helper.lazy_import__func7context:_FAIL____mk_ctx4lazy_import8lazy_objs_.__doc__ -ht # -ff -df
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.helper.lazy_import__func7context:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
先有了 func成功方案:mk_ctx4lazy_import4funcs_
但是 lazy_obj方案失败:_FAIL____mk_ctx4lazy_import8lazy_objs_
    失败原因:original_sys_modules 被直接导入某个标准库中，而非通过『sys.modules』间接访问
        #但 mk_ctx4lazy_import4funcs_ 没毛病，因为 导入 原函数 更佳
A:考虑另一方案:
    from seed.vmdl.LAZY_OBJ.seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset
    感觉麻烦，还不如直接:『lazy_xxx = lazy_import8lazy_obj_(qnm4mdl8src, smay_qnm4obj8src, may_either_mdl_obj:=None)』
B:考虑另一方案:
    with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
        from __.seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset
]]

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



>>> mapping4alias5or_decl_str_('') is _empty__mapping4alias
True
>>> mapping4alias5or_decl_str_('   ') is _empty__mapping4alias
True
>>> mapping4alias5or_decl_str_('k:v')
{'k': 'v'}
>>> mapping4alias5or_decl_str_(' k : v ')
{'k': 'v'}
>>> mapping4alias5or_decl_str_('k:v,a:b,ccc:ddd') == {'k': 'v', 'a': 'b', 'ccc': 'ddd'}
True
>>> mapping4alias5or_decl_str_('  k  :  v  ,  a  :  b  ,  ccc  :  ddd  ') == {'k': 'v', 'a': 'b', 'ccc': 'ddd'}
True





######################
######################
_FAIL____mk_ctx4lazy_import8lazy_objs_.__doc__
######################
######################





######################
######################
######################

#.#################################
>>> with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
...     from __.seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset
>>> lazy_null_tuple()
()
>>> lazy_null_iter() #doctest: +ELLIPSIS
<str_ascii_iterator object at 0x...>
>>> _lazy_null_frozenset_()
frozenset()

#.#################################

>>> with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
...     from __.seed.tiny import lazy_null_tuple as lazy_null_tuple_
>>> lazy_null_tuple_
_LazyImport8LazyObj('seed.tiny', 'null_tuple', None)
>>> lazy_null_tuple_()
()


#.#################################
>>> with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
...     type(sys.modules)
...     type(sys.modules['__.seed'])
...     type(sys.modules['__.seed.tiny'])
<class 'seed.helper.lazy_import__func7context.Wrapper4the_sys_modules_dict4lazy_import8lazy_obj__ver2'>
<class 'seed.helper.lazy_import__func7context.PseudoModule4lazy_import8lazy_obj__ver2'>
<class 'seed.helper.lazy_import__func7context.PseudoModule4lazy_import8lazy_obj__ver2'>
>>> with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
...     (sys.modules['__']) #doctest: +ELLIPSIS
...     (sys.modules['__.seed']) #doctest: +ELLIPSIS
...     (sys.modules['__.seed.tiny']) #doctest: +ELLIPSIS
...     lazy_null_tuple_ = sys.modules['__.seed.tiny'].lazy_null_tuple
<seed.helper.lazy_import__func7context.PseudoModule4lazy_import8lazy_obj__ver2 object at 0x...>
<seed.helper.lazy_import__func7context.PseudoModule4lazy_import8lazy_obj__ver2 object at 0x...>
<seed.helper.lazy_import__func7context.PseudoModule4lazy_import8lazy_obj__ver2 object at 0x...>
>>> lazy_null_tuple_ #doctest: +ELLIPSIS
_LazyImport8LazyObj('seed.tiny', 'null_tuple', (False, <module 'seed.tiny' from '.../seed/tiny.py'>))
>>> lazy_null_tuple_()
()
>>> (sys.modules['seed']) #doctest: +ELLIPSIS
<module 'seed' from '.../seed/__init__.py'>
>>> (sys.modules['seed.tiny']) #doctest: +ELLIPSIS
<module 'seed.tiny' from '.../seed/tiny.py'>
>>> sys.modules['seed.tiny'].lazy_null_tuple
Traceback (most recent call last):
    ...
AttributeError: module 'seed.tiny' has no attribute 'lazy_null_tuple'
>>> sys.modules['seed.tiny'].null_tuple
()

#.#################################
>>> original_sys_modules = sys.modules
>>> with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
...     assert not original_sys_modules is sys.modules
...     from __.seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset
>>> original_sys_modules is sys.modules
True
>>> lazy_null_tuple()
()
>>> lazy_null_iter() #doctest: +ELLIPSIS
<str_ascii_iterator object at 0x...>
>>> _lazy_null_frozenset_()
frozenset()



#.#################################
>>> with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
...     lazy_null_tuple_ = sys.modules['__.seed.tiny'].lazy_null_tuple
...     from __.seed.tiny import lazy_null_tuple as lazy_null_tuple_

##_LazyImport8LazyObj('seed.tiny', 'null_tuple', None)
>>> lazy_null_tuple_ #doctest: +ELLIPSIS
_LazyImport8LazyObj('seed.tiny', 'null_tuple', (False, <module 'seed.tiny' from '.../seed/tiny.py'>))
>>> lazy_null_tuple_()
()



>>> with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy__', suffix4attr='_xx_'):
...     from __.seed.tiny import lazy__null_tuple_xx_ as lazy_null_tuple_
>>> lazy_null_tuple_ #doctest: +ELLIPSIS
_LazyImport8LazyObj('seed.tiny', 'null_tuple', (False, <module 'seed.tiny' from '.../seed/tiny.py'>))
>>> lazy_null_tuple_()
()


######################
######################
######################




py_adhoc_call   seed.helper.lazy_import__func7context   @f
]]]'''#'''
__all__ = r'''
mk_ctx4lazy_import4funcs_
    Context4LazyImport4Func
    Wrapper4the_sys_modules_dict4lazy_import4func
    PseudoModule4lazy_import4func

mk_ctx4lazy_import8lazy_objs__ver2_
    Context4LazyImport8LazyObj__ver2
    Wrapper4the_sys_modules_dict4lazy_import8lazy_obj__ver2
    PseudoModule4lazy_import8lazy_obj__ver2



mapping4alias5or_decl_str_
    mapping4alias5decl_str_
'''.split()#'''
#   _FAIL____mk_ctx4lazy_import8lazy_objs_
#       _FAIL____Context4LazyImport8LazyObj
#       _FAIL____Wrapper4the_sys_modules_dict4lazy_import8lazy_obj
#       _FAIL____PseudoModule4lazy_import8lazy_obj
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import sys
from collections.abc import Mapping
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
#.
#.:s/\v^from +([_[:alnum:].]+) +import +([^# ]( *[^# ])*).*/lazy_import4funcs_('\1', '\2', __name__)\rif 0:\0
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_, force_lazy_imported_obj_, lazy_import8lazy_obj_
#.repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
#.
#.if 0b0001:from seed.debug.print_err import print_err
if 0b0000:from seed.debug.print_err import _fail__print_err
#.
#.
___end_mark_of_excluded_global_names__0___ = ...


__all__
#####################################






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
        #.m = d.get(nm)
        #.if not m is None:
        m = d.get(nm, Nothing:=object())
        if not m is Nothing:
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
class Wrapper4the_sys_modules_dict4lazy_import4func(Mapping):
    #def __init__(sf, qnm4mdl8dst, d, depth, /):
    #def __init__(sf, qnm4mdl8dst, mapping4alias, d, /):
    def __new__(cls, qnm4mdl8dst, mapping4alias, d, /):
        if type(d) is Wrapper4the_sys_modules_dict4lazy_import4func and qnm4mdl8dst in [d._qnm4mdl8dst] and mapping4alias in [d._d4alias]:
            sf = d
        else:
            sf = super(__class__, cls).__new__(cls)
            sf._qnm4mdl8dst = qnm4mdl8dst
            sf._d4alias = mapping4alias
            #.sf._original_d = d
            #.while type(d) is Wrapper4the_sys_modules_dict4lazy_import4func and qnm4mdl8dst in [d._qnm4mdl8dst] and mapping4alias in [d._d4alias]:
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
    #TypeError: Can't instantiate abstract class Wrapper4the_sys_modules_dict4lazy_import4func with abstract methods __getitem__, __iter__, __len__
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


_on4ctx4func = False
class Context4LazyImport4Func:
    'globally there is at most one ctx on working'
    def __init__(sf, qnm4mdl8dst, decl_str_or_mapping4alias, /):
        sf._qnm4mdl8dst = qnm4mdl8dst
        sf._d4alias = mapping4alias5or_decl_str_(decl_str_or_mapping4alias)
        sf._st = 0
        sf._saved_sys_modules = None
    #@override
    def __enter__(sf, /):
        global _on4ctx4func
        if not sf._st == 0:raise Exception
        if _on4ctx4func:raise Exception
        d = sys.modules
        if type(d) is Wrapper4the_sys_modules_dict4lazy_import4func:raise Exception
        new_d = Wrapper4the_sys_modules_dict4lazy_import4func(sf._qnm4mdl8dst, sf._d4alias, d)
        try:
            _on4ctx4func = True
            sf._saved_sys_modules = d
            sys.modules = new_d
            sf._st = 1
            return None
        except:
            _on4ctx4func = False
            sys.modules = d
            sf._saved_sys_modules = None
            sf._st = 0
            raise
    #@override
    def __exit__(sf, /, *excinfo):
        #sf.close()
        global _on4ctx4func
        if not sf._st == 1:raise Exception
        if not _on4ctx4func:raise Exception
        _on4ctx4func = False
        sys.modules = sf._saved_sys_modules
        sf._saved_sys_modules = None
        sf._st = 0
        return False

def mk_ctx4lazy_import4funcs_(qnm4mdl8dst, decl_str_or_mapping4alias='', /):
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
    return Context4LazyImport4Func(qnm4mdl8dst, decl_str_or_mapping4alias)


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
def mapping4alias5decl_str_(decl_str4alias, /):
    'decl_str4alias/str -> mapping4alias/{nm:alias}'
    s = decl_str4alias.strip()
    if not s:
        return _empty__mapping4alias
    mapping4alias = dict(map(_parse_item, s.split(',')))
    if not mapping4alias:
        mapping4alias = _empty__mapping4alias
    return mapping4alias
def mapping4alias5or_decl_str_(decl_str_or_mapping4alias, /):
    '(decl_str4alias/str|mapping4alias) -> mapping4alias/{nm:alias}'
    #if isinstance(decl_str_or_mapping4alias, str)
    if type(decl_str_or_mapping4alias) is str:
        decl_str4alias = decl_str_or_mapping4alias
        return mapping4alias5decl_str_(decl_str4alias)
    mapping4alias = decl_str_or_mapping4alias
    return mapping4alias








#####################################
__all__
######################
class _FAIL____PseudoModule4lazy_import8lazy_obj:
    'pseudo_mdl{lazy_import8lazy_obj}'
    def __init__(sf, prefix4attr, suffix4attr, qnm4mdl8src, may_mdl8src, /):
        _set(sf, '__name__', qnm4mdl8src)
        _set(sf, '_prefix4attr', prefix4attr)
        _set(sf, '_suffix4attr', suffix4attr)
        _set(sf, '_qnm4mdl8src', qnm4mdl8src)
        _set(sf, '_may_mdl8src', may_mdl8src)
        _set(sf, '_d', {})
    def __setattr__(sf, nm, x, /):
        if 0b0001:_fail__print_err(__class__, '__setattr__', nm, x)
        d = _get(sf, '_d')
        d[nm] = x
    def __getattribute__(sf, nm, /):
        if 0b0001:_fail__print_err(__class__, '__getattribute__', nm)
        if 1:
            if nm[-2:] == '__' == nm[:2] and nm in _special_nms:
                return _get(sf, nm)
                    # ^AttributeError:'_FAIL____PseudoModule4lazy_import8lazy_obj' object has no attribute '__spec__'
        try:
            d = _get(sf, '_d')
            m = d.get(nm, Nothing:=object())
            if not m is Nothing:
                return m
            prefix4attr = _get(sf, '_prefix4attr')
            suffix4attr = _get(sf, '_suffix4attr')
            #.#########
            #.if 0:
            #.    _nm_ = nm[len(prefix4attr):len(nm) -len(suffix4attr)]
            #.    if 0b0001: assert 0, (prefix4attr, suffix4attr, nm, _nm_)
            #.    if 0b0001: assert (prefix4attr, suffix4attr) in [('lazy__', '_xx_'), ('lazy_', '')], (prefix4attr, suffix4attr)
            #.    if 0b0001: assert not suffix4attr, (prefix4attr, suffix4attr, nm)
            #.#########
            if not len(nm) >= len(prefix4attr) + len(suffix4attr):raise AttributeError(nm)
                # empty _nm_ is ok
            if not nm.startswith(prefix4attr):raise AttributeError(nm)
            if not nm.endswith(suffix4attr):raise AttributeError(nm)
            #########
            _nm_ = nm[len(prefix4attr):len(nm) -len(suffix4attr)]
            qnm4src = _get(sf, '_qnm4mdl8src')
            may_mdl8src = _get(sf, '_may_mdl8src')
            if not may_mdl8src is None:
                mdl8src = may_mdl8src
                may_either_mdl_obj = (False, mdl8src)
                if 0b0000:
                    obj = getattr(mdl8src, _nm_)
                    may_either_mdl_obj = (True, obj)
            else:
                may_either_mdl_obj = None
            may_either_mdl_obj
            x = lazy_import8lazy_obj_(qnm4src, _nm_, may_either_mdl_obj)
                # empty _nm_ is ok
                    #def lazy_import8lazy_obj_(qnm4mdl8src, smay_qnm4obj8src, may_either_mdl_obj=None, /):

            #if 0b0001: assert not suffix4attr, (prefix4attr, suffix4attr, nm, qnm4src, _nm_, x)

            #########
            #d[nm] = x
            setattr(sf, nm, x)
            #return x
            return getattr(sf, nm)
        except AttributeError as e:
            raise BaseException(e)
class _FAIL____Wrapper4the_sys_modules_dict4lazy_import8lazy_obj(Mapping):
    def __new__(cls, prefix4attr, suffix4attr, prefixes4qnm4mdl8src, d, /):
        len(prefixes4qnm4mdl8src)
        if type(d) is _FAIL____Wrapper4the_sys_modules_dict4lazy_import8lazy_obj and d._prefix4attr == prefix4attr and d._suffix4attr == suffix4attr and d._prefixes4qnm4mdl8src == prefixes4qnm4mdl8src:
            sf = d
        else:
            sf = super(__class__, cls).__new__(cls)
            #.sf._original_d = d
            sf._d = d
            #xxx:sf._d4overrided = {}
            sf._d4missing = {}
            sf._prefix4attr = prefix4attr
            sf._suffix4attr = suffix4attr
            sf._prefixes4qnm4mdl8src = prefixes4qnm4mdl8src
        sf
        return sf
    #.if 0:
    #.    def the_wrapped_dict(sf, /):
    #.        return sf._original_d
    def _mk_pseudo_mdl4lazy_import8lazy_obj_(sf, qnm4mdl8src, may_mdl8src, /):
        'qnm4mdl -> pseudo_mdl{lazy_import8lazy_obj}'
        return _FAIL____PseudoModule4lazy_import8lazy_obj(sf._prefix4attr, sf._suffix4attr, qnm4mdl8src, may_mdl8src)
    #TypeError: Can't instantiate abstract class _FAIL____Wrapper4the_sys_modules_dict4lazy_import8lazy_obj with abstract methods __getitem__, __iter__, __len__
    def _is_qnm4mdl_ok(sf, qnm4mdl, /):
        ok = any(qnm4mdl.startswith(prefix) for prefix in sf._prefixes4qnm4mdl8src)
        return ok
    def __setitem__(sf, qnm4mdl, mdl, /):
        if 0b0001:_fail__print_err(__class__, '__setitem__', qnm4mdl, mdl)
        ok = sf._is_qnm4mdl_ok(qnm4mdl)
        assert not ok
        sf._d[qnm4mdl] = mdl
    def __getitem__(sf, qnm4mdl, /):
        'NEVER_RETURN_ORIGINAL_MDL, since original_mdl{attr->obj} but wrapper_mdl{qualified_attr->lazy_obj}'
        if 0b0001:_fail__print_err(__class__, '__getitem__', qnm4mdl)
        d = sf._d4missing
        m = d.get(qnm4mdl)
        if not m is None:
            return m
        ok = sf._is_qnm4mdl_ok(qnm4mdl)
        m = sf._d.get(qnm4mdl)
        if not m is None:
            mdl = sf._mk_pseudo_mdl4lazy_import8lazy_obj_(qnm4mdl, m) if ok else m
            d[qnm4mdl] = mdl
            return sf[qnm4mdl]
        if not ok:
            raise KeyError(qnm4mdl)
        mdl = sf._mk_pseudo_mdl4lazy_import8lazy_obj_(qnm4mdl, None)
        d[qnm4mdl] = mdl
        return sf[qnm4mdl]
        #.raise 000
        #.if not any(qnm4mdl.startswith(prefix) for prefix in sf._prefixes4qnm4mdl8src):
        #.    return sf._d[qnm4mdl]
        #.d = sf._d4missing
        #.if 0:
        #.    if qnm4mdl in sf._d4missing:
        #.        d = sf._d4missing
        #.    elif qnm4mdl in sf._d or qnm4mdl in sf._d4overrided:
        #.        d = sf._d4overrided
        #.    else:
        #.        d = sf._d4missing
        #.d
        #.m = d.get(qnm4mdl)
        #.if not m is None:
        #.    return m
        #.mdl = sf._mk_pseudo_mdl4lazy_import8lazy_obj_(qnm4mdl, None)
        #.d[qnm4mdl] = mdl
        #.return sf[qnm4mdl]
        #.return mdl
    def __len__(sf, /):
        return len(sf._d4missing)+len(sf._d) # ALTHOUGH NOT CORRECT
        return len(sf._d4missing)
        return len(sf._d4missing)+len(sf._d)#here => sf._d4overrided
    def __iter__(sf, /):
        yield from iter(sf._d4missing)
        yield from iter(sf._d)
    if 1:
        def __contains__(sf, qnm4mdl, /):
            if 0b0001:_fail__print_err(__class__, '__contains__', qnm4mdl)
            return qnm4mdl in sf._d4missing or qnm4mdl in sf._d or (ok := sf._is_qnm4mdl_ok(qnm4mdl))
            #sf[qnm4mdl]
            return True
        def get(sf, qnm4mdl, default=None, /):
            if 0b0001:_fail__print_err(__class__, 'get', (qnm4mdl, default))
            try:
                return sf[qnm4mdl]
            except KeyError:
                return default


_on4ctx4lazy_obj = False
class _FAIL____Context4LazyImport8LazyObj:
    'globally there is at most one ctx on working'
    def __init__(sf, prefix4attr, suffix4attr, prefixes4qnm4mdl8src, /):
        len(prefixes4qnm4mdl8src)
        sf._prefix4attr = prefix4attr
        sf._suffix4attr = suffix4attr
        sf._prefixes4qnm4mdl8src = prefixes4qnm4mdl8src
        sf._st = 0
        sf._saved_sys_modules = None
    #@override
    def __enter__(sf, /):
        global _on4ctx4lazy_obj
        if not sf._st == 0:raise Exception
        if _on4ctx4lazy_obj:raise Exception
        d = sys.modules
        if type(d) is _FAIL____Wrapper4the_sys_modules_dict4lazy_import8lazy_obj:raise Exception
        new_d = _FAIL____Wrapper4the_sys_modules_dict4lazy_import8lazy_obj(sf._prefix4attr, sf._suffix4attr, sf._prefixes4qnm4mdl8src, d)
        try:
            _on4ctx4lazy_obj = True
            sf._saved_sys_modules = d
            sys.modules = new_d
            sf._st = 1
            return None
        except:
            _on4ctx4lazy_obj = False
            sys.modules = d
            sf._saved_sys_modules = None
            sf._st = 0
            raise
    #@override
    def __exit__(sf, /, *excinfo):
        #sf.close()
        global _on4ctx4lazy_obj
        if not sf._st == 1:raise Exception
        if not _on4ctx4lazy_obj:raise Exception
        _on4ctx4lazy_obj = False
        sys.modules = sf._saved_sys_modules
        sf._saved_sys_modules = None
        sf._st = 0
        return False

def _FAIL____mk_ctx4lazy_import8lazy_objs_(*, prefix4attr, suffix4attr, prefixes4qnm4mdl8src):
    r'''
此方案失败:
    失败原因:original_sys_modules 被直接导入某个标准库中，而非通过『sys.modules』间接访问
        #但 mk_ctx4lazy_import4funcs_ 没毛病，因为 导入 原函数 更佳


usage:
    with _FAIL____mk_ctx4lazy_import8lazy_objs_(prefix4attr='lazy_', suffix4attr='', prefixes4qnm4mdl8src='seed. nn_ns.'.split()):
        from seed.tiny import lazy_null_tuple as lazy_null_tuple_

    '''#'''
    len(prefixes4qnm4mdl8src)
    return _FAIL____Context4LazyImport8LazyObj(prefix4attr, suffix4attr, prefixes4qnm4mdl8src)
#[[[[[[[[[
_FAIL____mk_ctx4lazy_import8lazy_objs_.__doc__ += r'''


######################
######################
######################

#.#################################
>>> with _FAIL____mk_ctx4lazy_import8lazy_objs_(prefix4attr='lazy_', suffix4attr='', prefixes4qnm4mdl8src='seed. nn_ns.'.split()):
...     from seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset
>>> lazy_null_tuple()
()
>>> lazy_null_iter() #doctest: +ELLIPSIS
<str_ascii_iterator object at 0x...>
>>> _lazy_null_frozenset_()
frozenset()

#.#################################

>>> with _FAIL____mk_ctx4lazy_import8lazy_objs_(prefix4attr='lazy_', suffix4attr='', prefixes4qnm4mdl8src='seed. nn_ns.'.split()):
...     from seed.tiny import lazy_null_tuple as lazy_null_tuple_
>>> lazy_null_tuple_
_LazyImport8LazyObj('seed.tiny', 'null_tuple', None)
>>> lazy_null_tuple_()
()


#.#################################
>>> with _FAIL____mk_ctx4lazy_import8lazy_objs_(prefix4attr='lazy_', suffix4attr='', prefixes4qnm4mdl8src='seed. nn_ns.'.split()):
...     type(sys.modules)
...     type(sys.modules['seed'])
...     type(sys.modules['seed.tiny'])
<class 'seed.helper.lazy_import__func7context._FAIL____Wrapper4the_sys_modules_dict4lazy_import8lazy_obj'>
<class 'module'>
<class 'seed.helper.lazy_import__func7context._FAIL____PseudoModule4lazy_import8lazy_obj'>
>>> with _FAIL____mk_ctx4lazy_import8lazy_objs_(prefix4attr='lazy_', suffix4attr='', prefixes4qnm4mdl8src='seed. nn_ns.'.split()):
...     (sys.modules['seed']) #doctest: +ELLIPSIS
...     (sys.modules['seed.tiny']) #doctest: +ELLIPSIS
...     lazy_null_tuple_ = sys.modules['seed.tiny'].lazy_null_tuple
<module 'seed' from '.../seed/__init__.py'>
<seed.helper.lazy_import__func7context._FAIL____PseudoModule4lazy_import8lazy_obj object at 0x...>
>>> lazy_null_tuple_ #doctest: +ELLIPSIS
_LazyImport8LazyObj('seed.tiny', 'null_tuple', (False, <module 'seed.tiny' from '.../seed/tiny.py'>))
>>> lazy_null_tuple_()
()
>>> (sys.modules['seed']) #doctest: +ELLIPSIS
<module 'seed' from '.../seed/__init__.py'>
>>> (sys.modules['seed.tiny']) #doctest: +ELLIPSIS
<module 'seed.tiny' from '.../seed/tiny.py'>
>>> sys.modules['seed.tiny'].lazy_null_tuple
Traceback (most recent call last):
    ...
AttributeError: module 'seed.tiny' has no attribute 'lazy_null_tuple'
>>> sys.modules['seed.tiny'].null_tuple
()

#.#################################
>>> del sys.modules['seed.tiny_.containers']
>>> original_sys_modules = sys.modules
>>> _fail__print_err('W'*333)
>>> with _FAIL____mk_ctx4lazy_import8lazy_objs_(prefix4attr='lazy_', suffix4attr='', prefixes4qnm4mdl8src='seed. nn_ns.'.split()):
...     assert not original_sys_modules is sys.modules
...     _fail__print_err('+*'*33)
...     from seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset
>>> _fail__print_err('M'*333)
>>> original_sys_modules is sys.modules
True
>>> lazy_null_tuple()
()
>>> lazy_null_iter() #doctest: +ELLIPSIS
<str_ascii_iterator object at 0x...>
>>> _lazy_null_frozenset_()
frozenset()

#.#################################

#重复一次，因为此前此情形曾失败过
#   ??? invalidate_caches() ???
#       并不影响
#无济于事:
>>> for x in sys.meta_path:  #doctest: +SKIP
...     if hasattr(x, 'invalidate_caches'):x.invalidate_caches()

#无济于事:
>>> sys.path_importer_cache.clear()  #doctest: +SKIP

#无济于事:
>>> sys.modules = sys.modules.copy(); del sys.modules['seed.tiny']  #doctest: +SKIP

#有用: #why? ==>> original_sys_modules 被直接导入某个标准库中，而非通过『sys.modules』间接访问
>>> del sys.modules['seed.tiny']  #doctest: +SKIP

>>> _fail__print_err('x'*333)
>>> with _FAIL____mk_ctx4lazy_import8lazy_objs_(prefix4attr='lazy_', suffix4attr='', prefixes4qnm4mdl8src='seed. nn_ns.'.split()):
...     lazy_null_tuple_ = sys.modules['seed.tiny'].lazy_null_tuple
...     _fail__print_err('y'*33)
...     from seed.tiny import lazy_null_tuple as lazy_null_tuple_
...         # why: ^ImportError: cannot import name 'lazy_null_tuple' from 'seed.tiny' (/sdcard/0my_files/git_repos/python3_src/seed/tiny.py)
>>> lazy_null_tuple_
_LazyImport8LazyObj('seed.tiny', 'null_tuple', None)
>>> lazy_null_tuple_()
()



>>> with _FAIL____mk_ctx4lazy_import8lazy_objs_(prefix4attr='lazy__', suffix4attr='_xx_', prefixes4qnm4mdl8src='seed. nn_ns.'.split()):
...     from seed.tiny import lazy__null_tuple_xx_ as lazy_null_tuple_
>>> lazy_null_tuple_
_LazyImport8LazyObj('seed.tiny', 'null_tuple', None)
>>> lazy_null_tuple_()
()


######################
######################
######################

'''#'''
#]]]]]]]]]












#####################################
__all__
######################
class PseudoModule4lazy_import8lazy_obj__ver2:
    'pseudo_mdl{lazy_import8lazy_obj}'
    def __init__(sf, prefix4attr, suffix4attr, qnm4mdl8src, may_mdl8src, /):
        _set(sf, '__name__', qnm4mdl8src)
        _set(sf, '_prefix4attr', prefix4attr)
        _set(sf, '_suffix4attr', suffix4attr)
        _set(sf, '_qnm4mdl8src', qnm4mdl8src)
        _set(sf, '_may_mdl8src', may_mdl8src)
        _set(sf, '_d', {})
    def __setattr__(sf, nm, x, /):
        #.if 0b0001:print_err(__class__, '__setattr__', nm, x)
        d = _get(sf, '_d')
        d[nm] = x
    def __getattribute__(sf, nm, /):
        #.if 0b0001:print_err(__class__, '__getattribute__', nm)
        ###############
        if nm[-2:] == '__' == nm[:2] and nm in _special_nms:
            return _get(sf, nm)
                # ^AttributeError:'PseudoModule4lazy_import8lazy_obj__ver2' object has no attribute '__spec__'
        ###############
        d = _get(sf, '_d')
        m = d.get(nm, Nothing:=object())
        if not m is Nothing:
            return m
        prefix4attr = _get(sf, '_prefix4attr')
        suffix4attr = _get(sf, '_suffix4attr')
        #.#########
        if not len(nm) >= len(prefix4attr) + len(suffix4attr):raise AttributeError(nm)
            # empty _nm_ is ok
        if not nm.startswith(prefix4attr):raise AttributeError(nm)
        if not nm.endswith(suffix4attr):raise AttributeError(nm)
        #########
        _nm_ = nm[len(prefix4attr):len(nm) -len(suffix4attr)]
        qnm4src = _get(sf, '_qnm4mdl8src')
        may_mdl8src = _get(sf, '_may_mdl8src')
        if not may_mdl8src is None:
            mdl8src = may_mdl8src
            may_either_mdl_obj = (False, mdl8src)
            if 0b0000:
                obj = getattr(mdl8src, _nm_)
                may_either_mdl_obj = (True, obj)
        else:
            may_either_mdl_obj = None
        may_either_mdl_obj
        x = lazy_import8lazy_obj_(qnm4src, _nm_, may_either_mdl_obj)
            # empty _nm_ is ok
                #def lazy_import8lazy_obj_(qnm4mdl8src, smay_qnm4obj8src, may_either_mdl_obj=None, /):

        #########
        #d[nm] = x
        setattr(sf, nm, x)
        #return x
        return getattr(sf, nm)
        ###############
def _check_nonexistent_prefix4qnm4mdl8src(nonexistent_prefix4qnm4mdl8src, /):
    assert nonexistent_prefix4qnm4mdl8src
    assert not nonexistent_prefix4qnm4mdl8src[0] == '.'
    assert nonexistent_prefix4qnm4mdl8src[-1] == '.'
    vroot_pkg = nonexistent_prefix4qnm4mdl8src[:-1]
    if vroot_pkg in sys.modules:
        raise ValueError('not nonexistent:', vroot_pkg)
class Wrapper4the_sys_modules_dict4lazy_import8lazy_obj__ver2(Mapping):
    def __new__(cls, nonexistent_prefix4qnm4mdl8src, prefix4attr, suffix4attr, d, /):
        _check_nonexistent_prefix4qnm4mdl8src(nonexistent_prefix4qnm4mdl8src)
        if type(d) is Wrapper4the_sys_modules_dict4lazy_import8lazy_obj__ver2 and d._nonexistent_prefix4qnm4mdl8src == nonexistent_prefix4qnm4mdl8src and d._prefix4attr == prefix4attr and d._suffix4attr == suffix4attr:
            sf = d
        else:
            sf = super(__class__, cls).__new__(cls)
            #.sf._original_d = d
            sf._d = d
            #xxx:sf._d4overrided = {}
            sf._d4missing = {}
            sf._nonexistent_prefix4qnm4mdl8src = nonexistent_prefix4qnm4mdl8src
            sf._vroot_pkg = nonexistent_prefix4qnm4mdl8src[:-1]
            sf._prefix4attr = prefix4attr
            sf._suffix4attr = suffix4attr
        sf
        return sf
    #.if 0:
    #.    def the_wrapped_dict(sf, /):
    #.        return sf._original_d
    def _mk_pseudo_mdl4lazy_import8lazy_obj_(sf, qnm4mdl8src, may_mdl8src, /):
        'qnm4mdl -> pseudo_mdl{lazy_import8lazy_obj}'
        return PseudoModule4lazy_import8lazy_obj__ver2(sf._prefix4attr, sf._suffix4attr, qnm4mdl8src, may_mdl8src)
    #TypeError: Can't instantiate abstract class Wrapper4the_sys_modules_dict4lazy_import8lazy_obj__ver2 with abstract methods __getitem__, __iter__, __len__
    def _is_qnm4mdl_ok(sf, qnm4mdl, /):
        pkg_ = sf._nonexistent_prefix4qnm4mdl8src
        ok = qnm4mdl.startswith(pkg_) if len(qnm4mdl) > len(pkg_) else qnm4mdl == sf._vroot_pkg
        return ok
    def __setitem__(sf, qnm4mdl, mdl, /):
        #.if 0b0001:print_err(__class__, '__setitem__', qnm4mdl, mdl)
        ok = sf._is_qnm4mdl_ok(qnm4mdl)
        assert not ok
        sf._d[qnm4mdl] = mdl
    def __getitem__(sf, qnm4mdl, /):
        'NEVER_RETURN_ORIGINAL_MDL, since original_mdl{attr->obj} but wrapper_mdl{qualified_attr->lazy_obj}'
        #.if 0b0001:print_err(__class__, '__getitem__', qnm4mdl)
        d = sf._d4missing
        m = d.get(qnm4mdl)
        if not m is None:
            return m
        ok = sf._is_qnm4mdl_ok(qnm4mdl)
        pkg_ = sf._nonexistent_prefix4qnm4mdl8src
        _qnm4mdl = qnm4mdl[len(pkg_):] if ok else qnm4mdl
        m = sf._d.get(_qnm4mdl)
        if not m is None:
            #xxx:if ok:raise ValueError('not nonexistent:', pkg_, qnm4mdl)
            mdl = sf._mk_pseudo_mdl4lazy_import8lazy_obj_(_qnm4mdl, m) if ok else m
            d[qnm4mdl] = mdl
            return sf[qnm4mdl]
        if not ok:
            raise KeyError(qnm4mdl)
        mdl = sf._mk_pseudo_mdl4lazy_import8lazy_obj_(_qnm4mdl, None)
        d[qnm4mdl] = mdl
        return sf[qnm4mdl]
    def __len__(sf, /):
        return len(sf._d4missing)+len(sf._d) # ALTHOUGH NOT CORRECT
        return len(sf._d4missing)
        return len(sf._d4missing)+len(sf._d)#here => sf._d4overrided
    def __iter__(sf, /):
        yield from iter(sf._d4missing)
        yield from iter(sf._d)
    if 1:
        def __contains__(sf, qnm4mdl, /):
            #.if 0b0001:print_err(__class__, '__contains__', qnm4mdl)
            return qnm4mdl in sf._d4missing or (ok := sf._is_qnm4mdl_ok(qnm4mdl)) or (_qnm4mdl:=qnm4mdl) in sf._d
                #<<==:
            #.if qnm4mdl in sf._d4missing:
            #.    return True
            #.ok = sf._is_qnm4mdl_ok(qnm4mdl)
            #.if ok:
            #.    return True
            #.return (_qnm4mdl:=qnm4mdl) in sf._d
                #<<==:
                #.pkg_ = sf._nonexistent_prefix4qnm4mdl8src
                #._qnm4mdl = qnm4mdl[len(pkg_):] if ok else qnm4mdl
                #.return _qnm4mdl in sf._d or ok
        def get(sf, qnm4mdl, default=None, /):
            #.if 0b0001:print_err(__class__, 'get', (qnm4mdl, default))
            try:
                return sf[qnm4mdl]
            except KeyError:
                return default


_on4ctx4lazy_obj = False
class Context4LazyImport8LazyObj__ver2:
    'globally there is at most one ctx on working'
    def __init__(sf, nonexistent_prefix4qnm4mdl8src, prefix4attr, suffix4attr, /):
        _check_nonexistent_prefix4qnm4mdl8src(nonexistent_prefix4qnm4mdl8src)
        sf._nonexistent_prefix4qnm4mdl8src = nonexistent_prefix4qnm4mdl8src
        sf._prefix4attr = prefix4attr
        sf._suffix4attr = suffix4attr
        sf._st = 0
        sf._saved_sys_modules = None
    #@override
    def __enter__(sf, /):
        global _on4ctx4lazy_obj
        if not sf._st == 0:raise Exception
        if _on4ctx4lazy_obj:raise Exception
        d = sys.modules
        if type(d) is Wrapper4the_sys_modules_dict4lazy_import8lazy_obj__ver2:raise Exception
        new_d = Wrapper4the_sys_modules_dict4lazy_import8lazy_obj__ver2(sf._nonexistent_prefix4qnm4mdl8src, sf._prefix4attr, sf._suffix4attr, d)
        try:
            _on4ctx4lazy_obj = True
            sf._saved_sys_modules = d
            sys.modules = new_d
            sf._st = 1
            return None
        except:
            _on4ctx4lazy_obj = False
            sys.modules = d
            sf._saved_sys_modules = None
            sf._st = 0
            raise
    #@override
    def __exit__(sf, /, *excinfo):
        #sf.close()
        global _on4ctx4lazy_obj
        if not sf._st == 1:raise Exception
        if not _on4ctx4lazy_obj:raise Exception
        _on4ctx4lazy_obj = False
        sys.modules = sf._saved_sys_modules
        sf._saved_sys_modules = None
        sf._st = 0
        return False

def mk_ctx4lazy_import8lazy_objs__ver2_(*, nonexistent_prefix4qnm4mdl8src, prefix4attr, suffix4attr):
    r'''
usage:
    with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
        from __.seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset

    '''#'''
    return Context4LazyImport8LazyObj__ver2(nonexistent_prefix4qnm4mdl8src, prefix4attr, suffix4attr)


#####################################
__all__
#lazy_import4funcs_('seed.helper.lazy_import__func7context', 'mk_ctx4lazy_import8lazy_objs__ver2_,mk_ctx4lazy_import4funcs_', __name__)
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import8lazy_objs__ver2_,mk_ctx4lazy_import4funcs_ #NOTE:mk_ctx4lazy_import4funcs_ not support "as"
from seed.helper.lazy_import__func7context import *
