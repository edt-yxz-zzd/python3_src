#__all__:goto
r'''[[[
e ../../python3_src/seed/pkg_tools/load_module5attr.py

rigid --> rigid
sloppy --> sloppy
java-style:
    loader.xxx.yyy.zzz.obj
java-style+terminal-attr:
    loader.xxx.yyy.zzz._.obj

seed.pkg_tools.load_module5attr
py -m nn_ns.app.debug_cmd   seed.pkg_tools.load_module5attr -x
py -m nn_ns.app.doctest_cmd seed.pkg_tools.load_module5attr:__doc__ --ndiff -ff -v
py_adhoc_call   seed.pkg_tools.load_module5attr   @f
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.pkg_tools.load_module5attr:XXX@T    =T      ++exclude_prefixes:_
from seed.pkg_tools.load_module5attr import *

>>> sloppy_java_style_proxy_loader.math.pi
3.141592653589793
>>> import math
>>> sloppy_java_style_proxy_loader.math is math
True
>>> import collections.abc
>>> sloppy_java_style_proxy_loader.collections.abc is collections.abc
True
>>> sloppy_java_style_proxy_loader.collections is collections
False
>>> type(sloppy_java_style_proxy_loader.collections) is SloppyJavaStyleProxyLoader
True






sloppy_java_style_proxy_loader__terminated_by_underscore

>>> sloppy_java_style_proxy_loader__terminated_by_underscore.math.pi
3.141592653589793
>>> import math
>>> sloppy_java_style_proxy_loader__terminated_by_underscore.math is math
True
>>> import collections.abc
>>> sloppy_java_style_proxy_loader__terminated_by_underscore.collections.abc is collections.abc
True
>>> sloppy_java_style_proxy_loader__terminated_by_underscore.collections is collections
False
>>> sloppy_java_style_proxy_loader__terminated_by_underscore.collections._ is collections
True
>>> type(sloppy_java_style_proxy_loader__terminated_by_underscore.collections) is SloppyJavaStyleProxyLoader__terminal_attr
True












rigid_java_style_proxy_loader__terminal_attr

>>> rigid_java_style_proxy_loader__terminal_attr.math.pi
RigidJavaStyleProxyLoader__terminal_attr('_', (((), 'math'), 'pi'))
>>> rigid_java_style_proxy_loader__terminal_attr.math._.pi
Traceback (most recent call last):
    ...
ModuleNotFoundError: No module named 'math.pi'; 'math' is not a package
>>> rigid_java_style_proxy_loader__terminal_attr._.math.pi
3.141592653589793
>>> import math
>>> rigid_java_style_proxy_loader__terminal_attr._.math is math
True
>>> rigid_java_style_proxy_loader__terminal_attr.math._ is math
False
>>> import collections.abc
>>> rigid_java_style_proxy_loader__terminal_attr.collections.abc is collections.abc
False
>>> rigid_java_style_proxy_loader__terminal_attr.collections.abc._ is collections.abc
False
>>> rigid_java_style_proxy_loader__terminal_attr.collections._.abc is collections.abc
True
>>> rigid_java_style_proxy_loader__terminal_attr.collections is collections
False
>>> rigid_java_style_proxy_loader__terminal_attr.collections._ is collections
False
>>> rigid_java_style_proxy_loader__terminal_attr._.collections is collections
True

>>> type(rigid_java_style_proxy_loader__terminal_attr.collections.abc.pi) is RigidJavaStyleProxyLoader__terminal_attr
True
>>> type(rigid_java_style_proxy_loader__terminal_attr.collections.abc) is RigidJavaStyleProxyLoader__terminal_attr
True
>>> type(rigid_java_style_proxy_loader__terminal_attr.collections) is RigidJavaStyleProxyLoader__terminal_attr
True
>>> type(rigid_java_style_proxy_loader__terminal_attr.math) is RigidJavaStyleProxyLoader__terminal_attr
True

>>> sloppy_java_style_proxy_loader
SloppyJavaStyleProxyLoader('', None)
>>> sloppy_java_style_proxy_loader__terminated_by_underscore
SloppyJavaStyleProxyLoader__terminal_attr('_', '', None)
>>> rigid_java_style_proxy_loader__terminal_attr
RigidJavaStyleProxyLoader__terminal_attr('_', '')


>>> rjstplr._.math.e
2.718281828459045
>>> rjstplr().math.e
2.718281828459045
>>> Rjstplr('____end_of_pkg___', 'collections').____end_of_pkg___.abc is collections.abc
True
>>> Rjstplr(None, 'collections')().abc is collections.abc
True


#]]]'''
__all__ = r'''
IBaseJavaStyleProxyLoader
    SloppyJavaStyleProxyLoader
        get_smay_pkg_qname_
        get_may_pkg_obj_
        sloppy_java_style_proxy_loader
    IBaseJavaStyleProxyLoader__terminal_attr
        get_terminal_attr_
        SloppyJavaStyleProxyLoader__terminal_attr
            sloppy_java_style_proxy_loader__terminated_by_underscore

RigidJavaStyleProxyLoader__step1
RigidJavaStyleProxyLoader__terminal_attr            Rjstplr
    rigid_java_style_proxy_loader__terminal_attr    rjstplr

'''.split()#'''
__all__


import importlib
from seed.pkg_tools.is_pkg import is_pkg_, is_module_
from seed.tiny import check_type_is, curry1

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
from seed.data_funcs.lnkls import rglnkls_ops, empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable

from seed.data_funcs.lnkls import rglnkls2list


def _call_(nm, sf, /, *args):
    f = getattr(type(sf), nm)
    return f(sf, *args)
class _Call:
    @override
    def __getattribute__(sf, nm, /):
        return curry1(_call_, nm)
_call = _Call()
_get__ = object.__getattribute__
def _get_(nm, sf, /):
    return _get__(sf, nm)
class _Get:
    @override
    def __getattribute__(sf, nm, /):
        return curry1(_get_, nm)
_get = _Get()

def get_smay_pkg_qname_(sf, /):
    return _get.smay_pkg_qname(sf)
    return _get__(sf, 'smay_pkg_qname')

def get_may_pkg_obj_(sf, /):
    return _get.may_pkg_obj(sf)
    return _get__(sf, 'may_pkg_obj')

def _get_args4BaseJavaStyleProxyLoader_(sf, /):
    smay_pkg_qname = get_smay_pkg_qname_(sf)
    may_pkg_obj = get_may_pkg_obj_(sf)
    return (smay_pkg_qname, may_pkg_obj)
def _mk_proxy_or_echo___success_(sf, smay_pkg_qname, may_pkg_obj, nm, qname4module, module_obj, /):
    '-> (module_obj | new-proxy/sf<module_obj>)'
    return _call._mk_proxy_or_echo___success_(sf, smay_pkg_qname, may_pkg_obj, nm, qname4module, module_obj)
def _get_attr_or_reraise___failure_(sf, smay_pkg_qname, may_pkg_obj, nm, qname4module, /):
    '-> may_pkg_obj.nm | re-raise'
    return _call._get_attr_or_reraise___failure_(sf, smay_pkg_qname, may_pkg_obj, nm, qname4module)
class _Base4repr:
    def _get_args4repr_(sf, /):
        return _get_args4BaseJavaStyleProxyLoader_(sf)
    def __repr__(sf, /):
        args = _call._get_args4repr_(sf)
        return repr_helper(sf, *args)
def _mk_qname4module_(smay_pkg_qname, nm, /):
    if smay_pkg_qname:
        qname4module = f'{smay_pkg_qname}.{nm}'
    else:
        qname4module = nm
    return qname4module
class IBaseJavaStyleProxyLoader(_Base4repr, ABC__no_slots):
#class _BaseJavaStyleProxyLoader(ABC__no_slots):
    def _check_args4BaseJavaStyleProxyLoader_(sf, smay_pkg_qname, may_pkg_obj, /):
        if not (not smay_pkg_qname) is (may_pkg_obj is None): raise TypeError
        # [[may_pkg_obj is None] <-> [smay_pkg_qname == '']]
        if not may_pkg_obj is None:
            pkg_obj = may_pkg_obj
            if not is_pkg_(pkg_obj):raise TypeError(type(pkg_obj))
        # [may_pkg_obj :: None | pkg]

    #def __init__(sf, smay_pkg_qname='', may_pkg_obj=None, /):
    def __init__(sf, smay_pkg_qname, may_pkg_obj, /):
        check_type_is(str, smay_pkg_qname)
        _call._check_args4BaseJavaStyleProxyLoader_(sf, smay_pkg_qname, may_pkg_obj)
        # [[may_pkg_obj is None] <-> [smay_pkg_qname == '']]
        # [may_pkg_obj :: None | pkg]
        sf.smay_pkg_qname = smay_pkg_qname
        sf.may_pkg_obj = may_pkg_obj
    @override
    def __getattribute__(sf, nm, /):
        (smay_pkg_qname, may_pkg_obj) = _get_args4BaseJavaStyleProxyLoader_(sf)
        qname4module = _mk_qname4module_(smay_pkg_qname, nm)

        try:
            module_obj = importlib.import_module(qname4module)
        except ImportError:
            return _get_attr_or_reraise___failure_(sf, smay_pkg_qname, may_pkg_obj, nm, qname4module)
        return _mk_proxy_or_echo___success_(sf, smay_pkg_qname, may_pkg_obj, nm, qname4module, module_obj)
    @abstractmethod
    def _mk_proxy_or_echo___success_(sf, smay_pkg_qname, may_pkg_obj, nm, qname4module, module_obj, /):
        '-> (module_obj | new-proxy/sf<module_obj>)'
        raise NotImplementedError
    @abstractmethod
    def _get_attr_or_reraise___failure_(sf, smay_pkg_qname, may_pkg_obj, nm, qname4module, /):
        '-> may_pkg_obj.nm | re-raise'
        raise NotImplementedError

class SloppyJavaStyleProxyLoader(IBaseJavaStyleProxyLoader):
    def _mk_proxy_(sf, pkg_qname, pkg_obj, /):
        '-> (new-proxy/sf<module_obj>)'
        return type(sf)(pkg_qname, pkg_obj)
    @override
    def _mk_proxy_or_echo___success_(sf, smay_pkg_qname, may_pkg_obj, nm, qname4module, module_obj, /):
        '-> (module_obj | new-proxy/sf<module_obj>)'
        if not is_pkg_(module_obj):
            #non-pkg
            #module_obj
            return module_obj
        #pkg --> proxy
        pkg_obj = module_obj
        pkg_qname = qname4module
        proxy = _call._mk_proxy_(sf, pkg_qname, pkg_obj)
        return proxy
    @override
    def _get_attr_or_reraise___failure_(sf, smay_pkg_qname, may_pkg_obj, nm, qname4module, /):
        '-> may_pkg_obj.nm | re-raise'
        if not smay_pkg_qname:
            #no pkg at all
            raise #re-raise ImportError
        # [not$ [smay_pkg_qname == '']]
        if 0:
            if not is_pkg_(may_pkg_obj):
                #non-pkg
                #module_obj --> module_obj.nm
                module_obj = may_pkg_obj
                return getattr(may_pkg_obj, nm)
                    # ^AttributeError
            #pkg
            pkg_obj = may_pkg_obj
        else:
            # !! _check_args4BaseJavaStyleProxyLoader_
            # [may_pkg_obj :: None | pkg]
            # [[may_pkg_obj is None] <-> [smay_pkg_qname == '']]
            # !! [not$ [smay_pkg_qname == '']]
            # [not$ [may_pkg_obj is None]]
            # [may_pkg_obj :: pkg]
            #
            #pkg
            pkg_obj = may_pkg_obj
        pkg_obj

        try:
            #pkg
            return getattr(pkg_obj, nm)
                # ^AttributeError --> ^ImportError
        except AttributeError:
            pass
        raise #re-raise ImportError
sloppy_java_style_proxy_loader = SloppyJavaStyleProxyLoader('', None)

def get_terminal_attr_(sf, /):
    return _get.terminal_attr(sf)
    return _get__(sf, 'terminal_attr')

class IBaseJavaStyleProxyLoader__terminal_attr(IBaseJavaStyleProxyLoader):
#class _BaseJavaStyleProxyLoader__terminal_attr(IBaseJavaStyleProxyLoader):
    @override
    def _get_args4repr_(sf, /):
        terminal_attr = get_terminal_attr_(sf)
        (smay_pkg_qname, may_pkg_obj) = _get_args4BaseJavaStyleProxyLoader_(sf)
        return (terminal_attr, smay_pkg_qname, may_pkg_obj)
    #def __init__(sf, terminal_attr='_', smay_pkg_qname='', may_pkg_obj=None, /):
    def __init__(sf, terminal_attr, smay_pkg_qname, may_pkg_obj, /):
        check_type_is(str, terminal_attr)
        sf.terminal_attr = terminal_attr
        super().__init__(smay_pkg_qname, may_pkg_obj)
    @override
    def __getattribute__(sf, nm, /):
        if nm == get_terminal_attr_(sf):
            # stop proxy
            return get_may_pkg_obj_(sf)
        return super().__getattribute__(nm)
class SloppyJavaStyleProxyLoader__terminal_attr(IBaseJavaStyleProxyLoader__terminal_attr, SloppyJavaStyleProxyLoader):
    @override
    def _mk_proxy_(sf, pkg_qname, pkg_obj, /):
        '-> (new-proxy/sf<module_obj>)'
        terminal_attr = get_terminal_attr_(sf)
        return type(sf)(terminal_attr, pkg_qname, pkg_obj)
sloppy_java_style_proxy_loader__terminated_by_underscore = SloppyJavaStyleProxyLoader__terminal_attr('_', '', None)

##class RigidJavaStyleProxyLoader__terminal_attr(IBaseJavaStyleProxyLoader__terminal_attr):
##    @override
##    def _mk_proxy_or_echo___success_(sf, smay_pkg_qname, may_pkg_obj, nm, qname4module, module_obj, /):
##        '-> (module_obj | new-proxy/sf<module_obj>)'
##        # not terminal yet
##        terminal_attr = get_terminal_attr_(sf)
##        return type(sf)(terminal_attr, qname4module, module_obj)
##            # _check_args4BaseJavaStyleProxyLoader_
##                # ^TypeError if not is_pkg_(module_obj)
##    @override
##    def _get_attr_or_reraise___failure_(sf, smay_pkg_qname, may_pkg_obj, nm, qname4module, /):
##        '-> may_pkg_obj.nm | re-raise'
##        # not terminal yet
##        raise #re-raise ImportError
##rigid_java_style_proxy_loader__terminal_attr = RigidJavaStyleProxyLoader__terminal_attr('_', '', None)

class RigidJavaStyleProxyLoader__step1(_Base4repr):
    @override
    def _get_args4repr_(sf, /):
        smay_pkg_qname = get_smay_pkg_qname_(sf)
        return (smay_pkg_qname,)
    def __init__(sf, smay_pkg_qname, /):
        check_type_is(str, smay_pkg_qname)
        sf.smay_pkg_qname = smay_pkg_qname
    def __getattribute__(sf, nm, /):
        smay_pkg_qname = get_smay_pkg_qname_(sf)
        qname4module = _mk_qname4module_(smay_pkg_qname, nm)
        module_obj = importlib.import_module(qname4module)
        return module_obj

class RigidJavaStyleProxyLoader__terminal_attr(_Base4repr):
    @override
    def _get_args4repr_(sf, /):
        may_terminal_attr = _get.may_terminal_attr(sf)
        smay_pkg_qname__or__rglnkls = _get.smay_pkg_qname__or__rglnkls(sf)
        return (may_terminal_attr, smay_pkg_qname__or__rglnkls)
    def __init__(sf, may_terminal_attr, smay_pkg_qname__or__rglnkls, /):
        if not may_terminal_attr is None:
            terminal_attr = may_terminal_attr
            check_type_is(str, terminal_attr)
        if not type(smay_pkg_qname__or__rglnkls) is tuple:
            smay_pkg_qname = smay_pkg_qname__or__rglnkls
            check_type_is(str, smay_pkg_qname)
        if not type(smay_pkg_qname__or__rglnkls) is tuple:
            smay_pkg_qname = smay_pkg_qname__or__rglnkls
            if not smay_pkg_qname:
                rglnkls8smay_pkg_qname = empty_rglnkls
            else:
                rglnkls8smay_pkg_qname, _ = rglnkls_ipush_right(empty_rglnkls, smay_pkg_qname)
            rglnkls8smay_pkg_qname
        else:
            rglnkls8smay_pkg_qname = smay_pkg_qname__or__rglnkls
        rglnkls8smay_pkg_qname

        sf.may_terminal_attr = may_terminal_attr
        sf.smay_pkg_qname__or__rglnkls = smay_pkg_qname__or__rglnkls
        sf.rglnkls8smay_pkg_qname = rglnkls8smay_pkg_qname
        sf._may_step1_loader = None

    #def _setget_step1_loader_(sf, /):
    def __call__(sf, /):
        m = _get._may_step1_loader(sf)
        if m is None:
            smay_pkg_qname__or__rglnkls = _get.smay_pkg_qname__or__rglnkls(sf)
            if not type(smay_pkg_qname__or__rglnkls) is tuple:
                smay_pkg_qname = smay_pkg_qname__or__rglnkls
            else:
                rglnkls8smay_pkg_qname = smay_pkg_qname__or__rglnkls
                smay_pkg_qname = '.'.join(rglnkls2list(rglnkls8smay_pkg_qname))
            smay_pkg_qname
            sf._may_step1_loader = RigidJavaStyleProxyLoader__step1(smay_pkg_qname)
            m = _get._may_step1_loader(sf)
        assert not m is None
        step1_loader = m

        return step1_loader

    @override
    def __getattribute__(sf, nm, /):
        may_terminal_attr = _get.may_terminal_attr(sf)
        if not may_terminal_attr is None:
            terminal_attr = may_terminal_attr
            if nm == terminal_attr:
                # stop proxy
                return sf()
                return _call._setget_step1_loader_(sf)
    #    return sf[nm]
    #def __getitem__(sf, nm, /):
        # continue mk proxy
        rglnkls8smay_pkg_qname = _get.rglnkls8smay_pkg_qname(sf)
        rglnkls8pkg_qname, _ = rglnkls_ipush_right(rglnkls8smay_pkg_qname, nm)
        proxy = RigidJavaStyleProxyLoader__terminal_attr(may_terminal_attr, rglnkls8pkg_qname)
        return proxy

rjstplr = rigid_java_style_proxy_loader__terminal_attr = RigidJavaStyleProxyLoader__terminal_attr('_', '')
Rjstplr = RigidJavaStyleProxyLoader__terminal_attr


__all__

from seed.pkg_tools.load_module5attr import Rjstplr, rjstplr

from seed.pkg_tools.load_module5attr import SloppyJavaStyleProxyLoader, SloppyJavaStyleProxyLoader__terminal_attr, RigidJavaStyleProxyLoader__step1, RigidJavaStyleProxyLoader__terminal_attr, Rjstplr

from seed.pkg_tools.load_module5attr import sloppy_java_style_proxy_loader, sloppy_java_style_proxy_loader__terminated_by_underscore, rigid_java_style_proxy_loader__terminal_attr, rjstplr


from seed.pkg_tools.load_module5attr import *
