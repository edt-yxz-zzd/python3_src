#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/lazy_import.py
see-example:
    view ../../python3_src/seed/helper/_test__lazy_import_/__init__.py
    view ../../python3_src/seed/helper/_test__lazy_import_/_lazy_child__aaa.py
see-tools:
    view ../../python3_src/seed/for_libs/for_importlib.py
    view ../../python3_src/seed/for_libs/for_importlib__finder6parent.py
    view ../../python3_src/seed/types/attr/BatchCachedProperty.py
see:
    from functools import cached_property
    view ../../python3_src/seed/types/LazyValueDict.py


view ../../python3_src/seed/for_libs/for_importlib__finder6parent.py
    MetaPathFinder__parent_defined
        framework:import register root/toplvl.pacgkage provide loader for children/descendant... inherit/stop/manally offer
cp -iv -r /data/data/com.termux/files/usr/lib/python3.11/importlib/ /sdcard/0my_files/tmp/py_lib_src/

e ../../python3_src/seed/abc/IStated.py
e ../../python3_src/seed/helper/lazy_import.py
e ../../python3_src/seed/for_libs/for_importlib.py
e ../../python3_src/seed/for_libs/for_importlib__finder6parent.py




seed.helper.lazy_import
py -m nn_ns.app.debug_cmd   seed.helper.lazy_import -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.lazy_import:__doc__ -ht # -ff -df
py -m nn_ns.app.doctest_cmd seed.helper.lazy_import! -ht # -ff -df


>>> d = Dict4lazy_attr_mdl()
>>> d
Dict4lazy_attr_mdl({})
>>> d[996]
Traceback (most recent call last):
    ...
KeyError: 996
>>> d['_may_on_missing_'] = on_missing = lambda d, k:k+1
>>> d   #doctest: +ELLIPSIS
Dict4lazy_attr_mdl({'_may_on_missing_': <function <lambda> at 0x...>})
>>> d[996]
997
>>> d == {'_may_on_missing_':on_missing, 996:997}
True
>>> d   #doctest: +ELLIPSIS
Dict4lazy_attr_mdl({'_may_on_missing_': <function <lambda> at 0x...>, 996: 997})


>>> import seed.helper._test__lazy_import_._lazy_child__aaa as M
>>> name4on_missing4lazy_attr_mdl in vars(M)
True
>>> vars(M)['_may_on_missing_'] is getattr(M, '_may_on_missing_')
True
>>> type(vars(M)) is Dict4lazy_attr_mdl
True

#>>> vars(M)['a']      #doctest: +SKIP
calling:_mk_a_b()
666
>>> M.a
calling:_mk_a_b()
666
>>> M.b
999
>>> M.c
calling:c()
777
>>> M.a
666
>>> M.b
999
>>> M.c
777


######################
>>> #from seed.helper.lazy_import import BaseCachedPropertyGroup, ImmediateProperty, ImportProperty, FunctionalBatchProperty
>>> class B(BaseCachedPropertyGroup):
...     def bxx(sf, /):
...         from seed.helper.lazy_import import BaseCachedPropertyGroup
...         return BaseCachedPropertyGroup
...     vxx = ImmediateProperty(999)
...     ixx = ImportProperty('seed.helper.lazy_import', 'ImportProperty')
...     @FunctionalBatchProperty
...     def fxx(sf, /):
...         from seed.helper.lazy_import import FunctionalBatchProperty
...         return FunctionalBatchProperty, {'exx':666}
>>> x = B()
>>> x.bxx
<class 'seed.helper.lazy_import.BaseCachedPropertyGroup'>
>>> x.vxx
999
>>> x.ixx
<class 'seed.helper.lazy_import.ImportProperty'>
>>> x.fxx
<class 'seed.helper.lazy_import.FunctionalBatchProperty'>
>>> x.exx
666



######################
py_adhoc_call   seed.helper.lazy_import   @f
#]]]'''
__all__ = r'''
BaseCachedPropertyGroup
_IProperty4BaseCachedPropertyGroup
    ImmediateProperty
    ImportProperty
    FunctionalBatchProperty

CachedProperty
BatchCachedProperty
    mk_batch_cached_properties_
    mk_decorator8injector4batch_cached_property_
CommonState4BatchCachedProperty
    mk_common_state4batch_cached_property_





Dict4lazy_attr_mdl
    name4on_missing4lazy_attr_mdl
    LazyAttrModule

Loader4lazy_attr_mdl
    update_spec__using_Loader4lazy_attr_mdl_


symbol4finder6parent
    MetaPathFinder__parent_defined
    IFinder6parent
        IFinder6parent__4lazy_attr_mdl__via_meta_path_finders
            Finder6parent__4lazy_attr_mdl__via_meta_path_finders
                RegisteredError
                finder6parent__4lazy_attr_mdl__via_PathFinder









Finder4lazy_attr_mdl
    is_nonlazy_qnm4mdl__default_
    mk_path_hook4lazy_attr_mdl__5path_hook_
'''.split()#'''
#deprecated:Finder4lazy_attr_mdl
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.repr_input import repr_helper
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
    #__slots__ = ()
    #___no_slots_ok___ = True
from seed.tiny_.check import check_type_is, check_type_le, check_callable
from seed.tiny import mk_tuple, ifNone



from seed.for_libs.for_importlib import ILoader, IPathEntryFinder
    #sys.path_hooks
from importlib.machinery import FileFinder

from seed.for_libs.for_importlib__finder6parent import symbol4finder6parent, IFinder6parent
from seed.for_libs.for_importlib__finder6parent import MetaPathFinder__parent_defined
from importlib.machinery import PathFinder



from seed.pkg_tools.import_object import import_object, import4qobject
#def import4qobject(may_qname4module, may_qname4obj, /):

___end_mark_of_excluded_global_names__0___ = ...



#from collections import defaultdict
name4on_missing4lazy_attr_mdl = _0nm = '_may_on_missing_'
class Dict4lazy_attr_mdl(dict):
    @override
    def __repr__(sf, /):
        nm4ty = type(sf).__name__
        s = dict.__repr__(sf)
        return f'{nm4ty}({s})'
    @override
    def __missing__(sf, k, /):
        nm = _0nm
        #_may_on_missing_
        m = sf.get(nm)
        if m is None:
            #raise KeyError(k, 77777777)
            raise KeyError(k)
        on_missing = m
        v = on_missing(sf, k)
        if 1:
            sf[k] = v
        return v

#_readonly_names = ('__dict__', '__class__')
class LazyAttrModule:
    'lazy_attr_mdl # [vars(sf) :: Dict4lazy_attr_mdl][_may_on_missing_@vars(sf) :: may (sf -> k/nm -> v|^KeyError)]'
    #def __init__(sf, /, *args4globals4mdl, **kwds):
    def __init__(sf, args4globals4mdl, /, *, not_copy=False):
        if not not_copy:
            # copy
            d = Dict4lazy_attr_mdl(args4globals4mdl)
        else:
            d = (args4globals4mdl)
            check_type_le(dict, d)
                # !! [exec.globals :: dict]
        #check_type_is(Dict4lazy_attr_mdl, d)
        sf.__dict__ = d
    #.   super().__setattr__('__dict__', d)
    #.@override
    #.def __setattr__(sf, nm, v, /):
    #.    #avoid: __class__,__dict__
    #.    #if nm == '__dict__':
    #.    if nm in type(sf).__get_readonly_names__(sf)
    #.        raise AttributeError(nm)
    #.    #vars(sf)[nm] = v
    #.    super().__setattr__(nm, v)
    #.def __get_readonly_names__(sf, /):
    #.    '-> {nm} #see:__setattr__'
    #.    return _readonly_names
    #.@override
    #.def __getattr__(sf, nm, /):
    #.#def __getattribute__(sf, nm, /):
    #.    try:
    #.        return vars(sf)[nm]
    #.    except KeyError:
    #.        pass
    #.    raise AttributeError(nm)
    def __getattr__(sf, nm, /):
        try:
            return super().__getattr__(nm)
        except AttributeError:
            pass
        try:
            return vars(sf)[nm]
                # __missing__()-->on_missing()
        except KeyError:
            raise AttributeError(nm)

assert type(vars(LazyAttrModule({}))) is Dict4lazy_attr_mdl

#.class LazyAttrModule(dict):
#.    'lazy_attr_mdl # [_may_on_missing_@(vars(sf)|sf) :: may (sf -> k/nm -> v|^KeyError)]'
#.    __slots__ = '__dict__ __weakref__'.split()
#.    def __init__(sf, params, dict8globals, /):
#.        vars(sf).update(params)
#.        dict.update(sf, dict8globals)
#.    @override
#.    def __missing__(sf, k, /):
#.        nm = '_may_on_missing_'
#.        m = vars(sf).get(nm)
#.        if m is None:
#.            m = dict.get(sf, nm)
#.        if m is None:
#.            raise KeyError(k)
#.        on_missing = m
#.        return on_missing(sf, k)
#.    #def __getattr__(sf, nm, /):
#.    @override
#.    def __getattribute__(sf, nm, /):
#.        try:
#.            return vars(sf)[nm]
#.        except KeyError:
#.            pass
#.
#.        try:
#.            return sf[nm]
#.        except KeyError:
#.            pass
#.        raise AttributeError(nm)



class Loader4lazy_attr_mdl(ILoader):
    ___no_slots_ok___ = True
    def __new__(cls, loader, /):
        'ILoader -> Loader4lazy_attr_mdl # eg:[(SourceLoader|?ExtensionFileLoader?|SourcelessFileLoader) <: IFileLoader <: ILoader]'
        if isinstance(loader, __class__):
            sf = loader
        else:
            sf = super(__class__, cls).__new__(cls)
            sf._loader = loader
        sf
        return sf
    @override
    def __getattr__(sf, nm, /):
        'for:subclass of ILoader'
        return getattr(sf._loader, nm)
    #.@override
    #.#@optional
    #.def get_resource_reader(sf, fullname, /):
    #.    'qnm4mdl -> may (ITraversableResources|IResourceReader){fullname not package => None}[#ResourceReader is deprecated by TraversableResources#]'
    #.    m = getattr(sf._loader, 'get_resource_reader', None)
    #.    if m is None:
    #.        raise NotImplementedError('@optional')
    #.    get_resource_reader = m
    #.    return get_resource_reader(fullname)
    #.    return None
    @property
    #@optional
    #def get_resource_reader(sf, fullname, /):
    def get_resource_reader(sf, /):
        return sf._loader.get_resource_reader

    @override
    def create_module(sf, spec, /):
        'spec -> may empty-mdl_obj[#neednot set attrs4mdl#] | ^ImportError'
        m = sf._loader.create_module(spec)
            # ^ImportError
        if m is None:
            return LazyAttrModule({})
        mdl_obj = m
        #.if not isinstance(mdl_obj, LazyAttrModule):
        #.    mdl_obj = LazyAttrModule(vars(mdl_obj))
        d = vars(mdl_obj)
        if not isinstance(d, Dict4lazy_attr_mdl):
            mdl_obj = LazyAttrModule(vars(mdl_obj))
        return mdl_obj
        return None
        raise ImportError

    @property
    @override
    #def exec_module(sf, module, /):
    def exec_module(sf, /):
        return sf._loader.exec_module
def update_spec__using_Loader4lazy_attr_mdl_(spec, /):
    'spec -> spec{Loader4lazy_attr_mdl}'
    loader = spec.loader
    if not isinstance(loader, Loader4lazy_attr_mdl):
        loader4lazy_attr_mdl = Loader4lazy_attr_mdl(loader)
        spec.loader = loader4lazy_attr_mdl
    spec
    return spec

def is_nonlazy_qnm4mdl__default_(qnm4mdl, /):
    'qnm4mdl -> bool'
    return False
class Finder4lazy_attr_mdl(IPathEntryFinder):
    '???deprecated???'
    ___no_slots_ok___ = True
    def __new__(cls, finder, is_nonlazy_qnm4mdl_, /):
        'IPathEntryFinder -> (qnm4mdl->bool) -> Finder4lazy_attr_mdl # eg:[FileFinder <- IPathEntryFinder] #and not required:[FileFinder <: IPathEntryFinder]'
        check_callable(is_nonlazy_qnm4mdl_)
        if isinstance(finder, __class__):
            sf = finder
        else:
            sf = super(__class__, cls).__new__(cls)
            sf._finder = finder
            sf._is_nonlazy_qnm4mdl = is_nonlazy_qnm4mdl_
        sf
        return sf
    @override
    def __getattr__(sf, nm, /):
        'for:subclass of IPathEntryFinder'
        return getattr(sf._finder, nm)
    @override
    def invalidate_caches(sf, /):
        sf._finder.invalidate_caches()
        return None
    @override
    def find_spec(sf, fullname, target=None, /):
        'qnm4mdl -> may mdl_obj -> may spec |  ^ImportError'
        may_spec = sf._finder.find_spec(fullname, target)
            # ^ImportError
        if not (may_spec is None or sf._is_nonlazy_qnm4mdl(fullname)):
            spec = may_spec
            spec = update_spec__using_Loader4lazy_attr_mdl_(spec)
            may_spec = spec
            may_spec
        may_spec
        return may_spec

def mk_path_hook4lazy_attr_mdl__5path_hook_(path_hook, may__is_nonlazy_qnm4mdl_, /):
    'path_hook -> may is_nonlazy_qnm4mdl_ -> path_hook4lazy_attr_mdl/path_hook{Finder4lazy_attr_mdl} # [path_hook :: (path -> may? IPathEntryFinder|^ImportError)][is_nonlazy_qnm4mdl_ :: (qnm4mdl -> bool)] #see:is_nonlazy_qnm4mdl__default_'
    is_nonlazy_qnm4mdl_ = ifNone(may__is_nonlazy_qnm4mdl_, is_nonlazy_qnm4mdl__default_)
    check_callable(is_nonlazy_qnm4mdl_)
    check_callable(path_hook)
    def path_hook4lazy_attr_mdl(path, /):
        'path -> may? Finder4lazy_attr_mdl|^ImportError'
        may_finder = path_hook(path)
            # ^ImportError
        if not may_finder is None:
            finder = may_finder
            finder4lazy_attr_mdl = Finder4lazy_attr_mdl(finder, is_nonlazy_qnm4mdl_)
            may_finder = finder4lazy_attr_mdl
        return may_finder
    return path_hook4lazy_attr_mdl






























IFinder6parent
#xxx:class Finder6parent__using_Finder4lazy_attr_mdl(IFinder6parent):
    #'see:MetaPathFinder__parent_defined,Finder4lazy_attr_mdl'
class IFinder6parent__4lazy_attr_mdl__via_meta_path_finders(IFinder6parent):
    ___no_slots_ok___ = True
    @abstractmethod
    def is_lazy_qnm4child_ex_(sf, qnm4parent, bnm4child, paths6parent, obj8parent, /):
        'qualname4package/qnm4pkg/qnm4parent -> basename4module/bnm4mdl/bnm4child -> [path6parenth]/parent.__path__ -> pkg_obj/obj8parent -> bool'
    def __init__(sf, meta_path_finders, /):
        '[meta_path_finders :: [IMetaPathFinder]]'
        meta_path_finders = mk_tuple(meta_path_finders)

        assert not MetaPathFinder__parent_defined in meta_path_finders
        assert not iter(meta_path_finders) is meta_path_finders
        len(meta_path_finders)
        meta_path_finders[:0]
        sf._ls = meta_path_finders
        sf._qnm4child2may_spec = {}

    @override
    def invalidate_caches(sf, /):
        '-> None #[vivi:(IMetaPathFinder|IPathEntryFinder).invalidate_caches()]'
        sf._qnm4child2may_spec.clear()
        for meta_path_finder in sf._ls:
            meta_path_finder.invalidate_caches()
    @override
    def find_may_spec_or_raise(sf, qnm4parent, bnm4child, paths6parent, obj8parent, may_obj8child, /):
        'qualname4package/qnm4pkg/qnm4parent -> basename4module/bnm4mdl/bnm4child -> [path6parenth]/parent.__path__ -> pkg_obj/obj8parent -> may mdl_obj/obj8child -> may spec | ^ImportError #[vivi:(IMetaPathFinder|IPathEntryFinder).find_spec()]'
        ######################
        qnm4child = f'{qnm4parent}.{bnm4child}'
        d = sf._qnm4child2may_spec
        if qnm4child in d:
            may_spec = d[qnm4child]
            return may_spec
        ######################
        if not sf.is_lazy_qnm4child_ex_(qnm4parent, bnm4child, paths6parent, obj8parent):
            meta_path_finders = []
                # => may_spec = None
        else:
            meta_path_finders = sf._ls
        meta_path_finders
        ######################
        fullname = qnm4child
        may_paths6parent = paths6parent
        target = may_obj8child
        for meta_path_finder in meta_path_finders:
            may_spec = meta_path_finder.find_spec(fullname, may_paths6parent, target)
                # ^ImportError
            if not may_spec is None:
                break
        else:
            may_spec = None
        may_spec
        ######################
        if not may_spec is None:
            spec = may_spec
            spec = update_spec__using_Loader4lazy_attr_mdl_(spec)
            may_spec = spec
        may_spec
        d[qnm4child] = may_spec
        ######################
        return sf.find_may_spec_or_raise(qnm4parent, bnm4child, paths6parent, obj8parent, may_obj8child)
        return may_spec
class Finder6parent__4lazy_attr_mdl__via_meta_path_finders(IFinder6parent__4lazy_attr_mdl__via_meta_path_finders):
    def __init__(sf, meta_path_finders, /):
        super().__init__(meta_path_finders)
        sf._qnm4parent2bnm_set4lazy_children = {}
            # {qnm4parent:{registered-lazy-bnm4child}}
        sf._qnm4parent2is_lazy_bnm4child = {}
            # {qnm4parent:{registered-(bnm4child->is_lazy/bool)}}
        sf._seq4is_lazy_qnm4child = []
            # [registered-(qnm4child->is_lazy/bool)]
    def register__add_more_lazy_children_(sf, qnm4parent, bnms4lazy_children, /):
        'qnm4parent -> Iter bnm4child -> None'
        sf._qnm4parent2bnm_set4lazy_children.setdefault(qnm4parent, set()).update(bnms4lazy_children)
    def register__lazy_child_basename_predicator6parent_(sf, qnm4parent, is_lazy_bnm4child_, /):
        'qnm4parent -> (bnm4child->is_lazy/bool) -> None|^RegisteredError'
        check_callable(is_lazy_bnm4child_)
        if not is_lazy_bnm4child_ is sf._qnm4parent2is_lazy_bnm4child.setdefault(qnm4parent, is_lazy_bnm4child_): raise RegisteredError
    def register__add_lazy_child_qualname_predicator6global_(sf, is_lazy_qnm4child_, /):
        '(qnm4child->is_lazy/bool) -> None'
        check_callable(is_lazy_qnm4child_)
        sf._seq4is_lazy_qnm4child.append(is_lazy_qnm4child_)
    @override
    def is_lazy_qnm4child_ex_(sf, qnm4parent, bnm4child, paths6parent, obj8parent, /):
        'qualname4package/qnm4pkg/qnm4parent -> basename4module/bnm4mdl/bnm4child -> [path6parenth]/parent.__path__ -> pkg_obj/obj8parent -> bool'
        if bnm4child in sf._qnm4parent2bnm_set4lazy_children.get(qnm4parent, []):
            return True
        if not None is (is_lazy_bnm4child_ := sf._qnm4parent2is_lazy_bnm4child.get(qnm4parent)) and is_lazy_bnm4child_(bnm4child):
            #, is_lazy_bnm4child__default_
            return True
        qnm4child = f'{qnm4parent}.{bnm4child}'
        if any(is_lazy_qnm4child_(qnm4child) for is_lazy_qnm4child_ in sf._seq4is_lazy_qnm4child):
            return True
        return False
class RegisteredError(Exception):pass
finder6parent__4lazy_attr_mdl__via_PathFinder = Finder6parent__4lazy_attr_mdl__via_meta_path_finders([PathFinder])
#is_nonlazy_qnm4mdl__default_
#is_lazy_qnm4mdl__default_
#is_lazy_qnm4mdl_
#is_lazy_qnm4child_
#.def is_lazy_bnm4child__default_(bnm4child, /):
#.    return False



######################
#@20241229
_spec_nms = ('__dict__', '__class__')
class BaseCachedPropertyGroup:
    #__slots__ = ('__dict__', '__weakref__')
    def __getattribute__(sf, nm, /):
        if nm in _spec_nms:
            return super().__getattribute__(nm)
        d = object.__getattribute__(sf, '__dict__')
        #d = vars(sf)
            # RecursionError: maximum recursion depth exceeded
        try:
            return d[nm]
        except KeyError:
            pass
        cls = type(sf)
        f = getattr(cls, nm)
        d[nm] = f(sf)
        return getattr(sf, nm)
BaseCachedPropertyGroup

class _IProperty4BaseCachedPropertyGroup(ABC):
    __slots__ = ()
    @abstractmethod
    def __repr__(sf, /):
        return super().__repr__()
    @abstractmethod
    def __call__(sf, instance, /):
        '-> property_value'
    def __get__(sf, may_instance, owner, /):
        if may_instance is None:
            return sf
        instance = may_instance
        return sf(instance)

class ImmediateProperty(_IProperty4BaseCachedPropertyGroup):
    ___no_slots_ok___ = True
    def __init__(sf, v, /):
        sf._v = v
    @override
    def __repr__(sf, /):
        return repr_helper(sf, sf._v)
    @override
    def __call__(sf, instance, /):
        return sf._v

class ImportProperty(_IProperty4BaseCachedPropertyGroup):
    ___no_slots_ok___ = True
    def __init__(sf, qnm4mdl, qnm4obj, /):
        sf._qnm4mdl = qnm4mdl
        sf._qnm4obj = qnm4obj
    @override
    def __repr__(sf, /):
        return repr_helper(sf, sf._qnm4mdl, sf._qnm4obj)
    @override
    def __call__(sf, instance, /):
        return import4qobject(sf._qnm4mdl, sf._qnm4obj)

class FunctionalBatchProperty(_IProperty4BaseCachedPropertyGroup):
    ___no_slots_ok___ = True
    def __init__(sf, f, /):
        '[f :: instance -> (property_value, dict4batch_property)]'
        sf._f = f
    @override
    def __repr__(sf, /):
        return repr_helper(sf, sf._f)
    @override
    def __call__(sf, instance, /):
        (v, d) = sf._f(instance)
        vars(instance).update(d)
        return v


######################





__all__
from seed.for_libs.for_importlib__finder6parent import symbol4finder6parent, IFinder6parent
from seed.for_libs.for_importlib__finder6parent import MetaPathFinder__parent_defined
__all__
from seed.types.attr.BatchCachedProperty import CachedProperty, BatchCachedProperty, mk_batch_cached_properties_, mk_decorator8injector4batch_cached_property_
from seed.types.attr.BatchCachedProperty import CommonState4BatchCachedProperty, mk_common_state4batch_cached_property_
__all__



from seed.helper.lazy_import import name4on_missing4lazy_attr_mdl
    #def _may_on_missing_(Dict4lazy_attr_mdl, k, /) -> 'v':
from seed.helper.lazy_import import symbol4finder6parent, finder6parent__4lazy_attr_mdl__via_PathFinder
    #globals()[symbol4finder6parent] = finder6parent__4lazy_attr_mdl__via_PathFinder
    #finder6parent__4lazy_attr_mdl__via_PathFinder.register__add_more_lazy_children_(__name__, ['lazy_child__aaa'])

from seed.helper.lazy_import import BaseCachedPropertyGroup, ImmediateProperty, ImportProperty, FunctionalBatchProperty

from seed.helper.lazy_import import *
