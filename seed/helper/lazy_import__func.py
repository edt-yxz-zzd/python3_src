#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/lazy_import__func.py

py -m seed.helper.lazy_import__func
    main4convert_FromImportStmt()
py -m nn_ns.app.debug_cmd   seed.helper.lazy_import__func -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.lazy_import__func:__doc__ -ht # -ff -df

[[
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
from seed.helper.lazy_import__func7ast import mk_decorator4lazy_import__funcs_, decorator4lazy_import__funcs_

===
usage:
from seed.helper.lazy_import__func import lazy_import4func_
lazy_import4func_('seed.tiny', 'echo', __name__)
    ##if toplevel then almost eqv:
echo = lazy_import4func_('seed.tiny', 'echo')
    ##not overwrite global.echo
best:
echo = lazy_import4func_('seed.tiny', 'echo', __name__)

lazy_import4func_('seed.tiny', 'ifNone', __name__, '_ifNone_')
    ##if toplevel then almost eqv:
_ifNone_ = lazy_import4func_('seed.tiny', 'ifNone')
    ##not overwrite global._ifNone_
best:
_ifNone_ = lazy_import4func_('seed.tiny', 'ifNone', __name__, '_ifNone_')

===
usage:
from seed.helper.lazy_import__func import lazy_import4funcs_
lazy_import4funcs_('seed.tiny', 'fst,snd:_snd_', __name__)
    ##if toplevel then almost eqv:
[fst,_snd_] = lazy_import4funcs_('seed.tiny', 'fst,snd')
    ##not overwrite global.fst/_snd_
best:
[fst,_snd_] = lazy_import4funcs_('seed.tiny', 'fst,snd:_snd_', __name__)

===
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
[[
force_lazy_imported_func_:
old:
    (echo(0) or echo)
now:
    force_lazy_imported_func_(echo)
]]
[[
from seed.helper.lazy_import__func import lazy_import8lazy_obj_, force_lazy_imported_obj_

usage:
lazy_null_tuple = lazy_import8lazy_obj_('seed.tiny', 'null_tuple')
assert () == lazy_null_tuple()
assert () == force_lazy_imported_obj_(lazy_null_tuple)
assert () == force_lazy_imported_obj_(())


]]



######################
>>> import seed.helper.lazy_import__func as this_mdl
>>> this_mdl.check_int_ge # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute 'check_int_ge'
>>> this_mdl._check_int_ge # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute '_check_int_ge'
>>> x = lazy_import4func_('seed.tiny_.check', 'check_int_ge')
>>> this_mdl.check_int_ge # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute 'check_int_ge'
>>> this_mdl._check_int_ge # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute '_check_int_ge'
>>> x = lazy_import4func_('seed.tiny_.check', 'check_int_ge', __name__, '_check_int_ge')
>>> this_mdl.check_int_ge # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute 'check_int_ge'
>>> this_mdl._check_int_ge # yes:sf
_LazyImport4Func('seed.tiny_.check', 'check_int_ge', 'seed.helper.lazy_import__func', '_check_int_ge')
>>> this_mdl._check_int_ge(0, 1)
>>> this_mdl._check_int_ge # yes:f #doctest: +ELLIPSIS
<function check_int_ge at 0x...>
>>> x = lazy_import4func_('seed.tiny_.check', 'check_int_ge', __name__)
>>> this_mdl.check_int_ge # yes:sf
_LazyImport4Func('seed.tiny_.check', 'check_int_ge', 'seed.helper.lazy_import__func', '')
>>> this_mdl.check_int_ge(0, 1)
>>> this_mdl.check_int_ge # yes:f #doctest: +ELLIPSIS
<function check_int_ge at 0x...>




######################
>>> import seed.helper.lazy_import__func as this_mdl
>>> this_mdl.echo # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute 'echo'
>>> this_mdl._echo_ # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute '_echo_'
>>> x = lazy_import4func_('seed.tiny', 'echo', __name__)
>>> y = lazy_import4func_('seed.tiny', 'echo', __name__, '_echo_')
>>> this_mdl.echo # yes:sf
_LazyImport4Func('seed.tiny', 'echo', 'seed.helper.lazy_import__func', '')
>>> this_mdl._echo_ # yes:sf
_LazyImport4Func('seed.tiny', 'echo', 'seed.helper.lazy_import__func', '_echo_')
>>> this_mdl.echo(666)
666
>>> this_mdl._echo_(999)
999
>>> this_mdl.echo # yes:f #doctest: +ELLIPSIS
<function <lambda> at 0x...>
>>> this_mdl._echo_ # yes:f #doctest: +ELLIPSIS
<function <lambda> at 0x...>
>>> x
_LazyImport4Func('seed.tiny', 'echo', 'seed.helper.lazy_import__func', '')
>>> y
_LazyImport4Func('seed.tiny', 'echo', 'seed.helper.lazy_import__func', '_echo_')


######################
>>> import seed.helper.lazy_import__func as this_mdl
>>> this_mdl.fst # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute 'fst'
>>> this_mdl._snd_ # no
Traceback (most recent call last):
    ...
AttributeError: module 'seed.helper.lazy_import__func' has no attribute '_snd_'
>>> xs = lazy_import4funcs_('seed.tiny', 'fst,snd:_snd_', __name__)
>>> this_mdl.fst # yes:sf
_LazyImport4Func('seed.tiny', 'fst', 'seed.helper.lazy_import__func', '')
>>> this_mdl._snd_ # yes:sf
_LazyImport4Func('seed.tiny', 'snd', 'seed.helper.lazy_import__func', '_snd_')
>>> this_mdl.fst([666,999])
666
>>> this_mdl._snd_([666,999])
999
>>> this_mdl.fst # yes:f #doctest: +ELLIPSIS
<function fst at 0x...>
>>> this_mdl._snd_ # yes:f #doctest: +ELLIPSIS
<function snd at 0x...>
>>> xs
[_LazyImport4Func('seed.tiny', 'fst', 'seed.helper.lazy_import__func', ''), _LazyImport4Func('seed.tiny', 'snd', 'seed.helper.lazy_import__func', '_snd_')]

######################
######################
######################
>>> lazy_null_tuple = lazy_import8lazy_obj_('seed.tiny', 'null_tuple')
>>> lazy_null_tuple
_LazyImport8LazyObj('seed.tiny', 'null_tuple', None)
>>> lazy_null_tuple()
()
>>> force_lazy_imported_obj_(lazy_null_tuple)
()
>>> force_lazy_imported_obj_(())
()

######################
++__getitem__
>>> x = lazy_import4func_('seed.tiny_.bmk_pairs', 'bmk_pairs')
>>> x[666:999, -5:-2]
((666, 999), (-5, -2))

######################
++__getattribute__
++kw:arbitrary_ok
>>> rglnkls_ops = lazy_import4func_('seed.data_funcs.lnkls', 'rglnkls_ops', arbitrary_ok=True)
>>> rglnkls_ops.empty_rglnkls
()
>>> IRanges = lazy_import4func_('seed.data_funcs.rngs', 'IRanges')
>>> ranges = IRanges.from_unsorted_ints([9,8,7,1,2,4])
>>> ranges
NonTouchRanges(((1, 3), (4, 5), (7, 10)))

######################
++updated:check_type_is,check_type_le,check_is_obj
>>> from seed.tiny_.check import check_type_le, check_type_is
>>> IRanges = lazy_import4func_('seed.data_funcs.rngs', 'IRanges')
>>> IRanges
_LazyImport4Func('seed.data_funcs.rngs', 'IRanges', '', '')
>>> check_type_le(IRanges, ranges)
>>> NonTouchRanges = lazy_import4func_('seed.data_funcs.rngs', 'NonTouchRanges')
>>> NonTouchRanges
_LazyImport4Func('seed.data_funcs.rngs', 'NonTouchRanges', '', '')
>>> check_type_is(NonTouchRanges, ranges)

######################
++__pos__
#from seed.tiny_.oo8inf import oo
>>> oo = lazy_import4func_('seed.tiny_.oo8inf', 'oo')
>>> +oo
(+oo)

######################




[[
py_adhoc_call   seed.helper.lazy_import__func   ,str.filter_FromImportStmt6seed_tiny :'mk_tuple,echo'
===
from seed.helper.Echo import echo, theEcho
from seed.tiny_.containers import null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter, mk_frozenset, mk_tuple, mk_Just, mk_Left, mk_Right
from seed.tiny_.funcs import no_op, echo_args_kwargs, echo_kwargs, echo_args, echo, unbox_, unbox, fst, snd, const, lazy, lazy_raise_v, lazy_raise_f, eq, not_eq, is_, not_is, in_, not_in, flip, neg_flip, xor, xnor, not_, with_key, mk_fprint, fprint, py_cmp, int2cmp, set_doc_

]]
[[
py_adhoc_call   seed.helper.lazy_import__func   ,str.filter_FromImportStmt6seed_tiny :'mk_tuple,echo' | py -m seed.helper.lazy_import__func
===
lazy_import4funcs_('seed.helper.Echo', 'echo,theEcho', __name__)
if 0:from seed.helper.Echo import echo, theEcho

lazy_import4funcs_('seed.tiny_.containers', 'null_str,null_bytes,null_int,null_tuple,null_frozenset,null_mapping_view,null_iter,mk_frozenset,mk_tuple,mk_Just,mk_Left,mk_Right', __name__)
if 0:from seed.tiny_.containers import null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter, mk_frozenset, mk_tuple, mk_Just, mk_Left, mk_Right

lazy_import4funcs_('seed.tiny_.funcs', 'no_op,echo_args_kwargs,echo_kwargs,echo_args,echo,unbox_,unbox,fst,snd,const,lazy,lazy_raise_v,lazy_raise_f,eq,not_eq,is_,not_is,in_,not_in,flip,neg_flip,xor,xnor,not_,with_key,mk_fprint,fprint,py_cmp,int2cmp,set_doc_', __name__)
if 0:from seed.tiny_.funcs import no_op, echo_args_kwargs, echo_kwargs, echo_args, echo, unbox_, unbox, fst, snd, const, lazy, lazy_raise_v, lazy_raise_f, eq, not_eq, is_, not_is, in_, not_in, flip, neg_flip, xor, xnor, not_, with_key, mk_fprint, fprint, py_cmp, int2cmp, set_doc_
]]
[[
come_from:check_type_le
    view ../../python3_src/seed/tiny_/check.py

py_adhoc_call   seed.helper.lazy_import__func   @_test4isinstance_
    before:++__instancecheck__:
        =>『__getattribute__ {'nm': '__bases__'}』
    after:++__instancecheck__:
        =>『__instancecheck__ {'x': 999}』
py_adhoc_call   seed.helper.lazy_import__func   @_test4issubclass_
    before:++__subclasscheck__:
        =>『__getattribute__ {'nm': '__bases__'}』
    after:++__subclasscheck__:
        =>『__subclasscheck__ {'x': <class 'int'>}』


e ../lots/NOTE/Python/python-bug/isinstance-bug.txt

>>> (999).__bases__
Traceback (most recent call last):
    ...
AttributeError: 'int' object has no attribute '__bases__'
>>> int.__bases__
(<class 'object'>,)
>>> bool.__bases__
(<class 'int'>,)
>>> class C:
...     def __init__(sf, /):
...         sf.__bases__ = bool.__bases__
>>> x = C()
>>> x.__bases__
(<class 'int'>,)
>>> isinstance(999, C)
False
>>> isinstance(999, x) # not ^TypeError
False
>>> isinstance(999, 666) # ^TypeError
Traceback (most recent call last):
    ...
TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union

>>> class B:
...     def __getattribute__(sf, nm, /):
...         print('__getattribute__', nm)
...         if nm == '__bases__':return bool.__bases__
...         return super().__getattribute__(nm)
>>> y = B()
>>> y.__bases__
__getattribute__ __bases__
(<class 'int'>,)
>>> isinstance(999, y)
__getattribute__ __bases__
False

>>> from typing import Union
>>> Union[int,str].__bases__
Traceback (most recent call last):
    ...
AttributeError: __bases__
>>> Union[int,str]()
Traceback (most recent call last):
    ...
TypeError: Cannot instantiate typing.Union
>>> isinstance(Union[int,str], type)
False
>>> issubclass(Union[int,str], type)
Traceback (most recent call last):
    ...
TypeError: issubclass() arg 1 must be a class
>>> isinstance(999, Union[int,str])
True
>>> issubclass(int, Union[int,str])
True


dir(type(Union[int,str]))
    __instancecheck__
    __subclasscheck__
    __subclasshook__
dir(Union[int,str])
    __instancecheck__
    __subclasscheck__
    __subclasshook__
>>> Union[int,str].__instancecheck__
<bound method _UnionGenericAlias.__instancecheck__ of typing.Union[int, str]>
>>> type(Union[int,str]).__instancecheck__  #doctest: +ELLIPSIS
<function _UnionGenericAlias.__instancecheck__ at 0x...>

]]



]]]'''#'''
__all__ = r'''
lazy_import4func_
    lazy_import4funcs_
force_lazy_imported_func_

lazy_import8lazy_obj_
force_lazy_imported_obj_


filter_FromImportStmt6seed_tiny
    main4convert_FromImportStmt
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import operator as opss
from operator import attrgetter, __index__
from functools import cached_property

from seed.pkg_tools.import_object import import_object, import4qobject
#def import4qobject(may_qname4module, may_qname4obj, /):

####################################
#bug:
#xx:from seed.helper.lazy_import__func7dict import lazy_import__funcs7dict_
#xx:    #bug:check_type_is(bool, arbitrary_ok)@_LazyImport4Func.__init__()
#xx:    #   !! _LazyImport4Func.__init__() UNDER: with mk_ctx4lazy_import4funcs_(__name__):...
#xx:    #   !! lazy_import__func7dict import under lazy-context => cause deadloop
#xx:#lazy_import__funcs7dict_(globals(), ...)
#xx:(check_pseudo_identifier, check_smay_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name) = lazy_import__funcs7dict_(__name__, 'seed.tiny_.check',  'check_pseudo_identifier, check_smay_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name')
#xx:(check_callable, check_or_, check_subscriptable, check_type_is) = lazy_import__funcs7dict_(__name__, 'seed.tiny_.check',  'check_callable, check_or_, check_subscriptable, check_type_is')
####################################

#.from itertools import islice
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
__all__

def _inject_(sf, smay_qnm4mdl8dst, smay_nm4func8dst, may_func8dst, /):
    if 0b0000:
        from seed.debug.print_err import print_err, print_ferr
        print_err((sf, smay_qnm4mdl8dst, smay_nm4func8dst, may_func8dst))
    f = sf if may_func8dst is None else may_func8dst
    if smay_qnm4mdl8dst:
        #inject...
        qnm4mdl8dst = smay_qnm4mdl8dst
        nm4func8dst = smay_nm4func8dst
        mdl8dst = import4qobject(qnm4mdl8dst, None)
        ########
        try:
            #x = import4qobject(mdl8dst, nm4func8dst)
            x = getattr(mdl8dst, nm4func8dst)
        except AttributeError:
            #ok
            pass
        else:
            if not x is sf:
                raise Exception('dst exist:', (mdl8dst, nm4func8dst), (sf, x), (id(sf), id(x)))
        ########
        setattr(mdl8dst, nm4func8dst, f)
        x = getattr(mdl8dst, nm4func8dst)
        if not x is f:raise Exception('setattr fail?:', (mdl8dst, nm4func8dst), x, f)
        ########

_get = object.__getattribute__
_set = object.__setattr__
_del = object.__delattr__

class _Forbid_get_set_del:
    def __getattribute__(sf, nm, /):
        raise AttributeError(nm)
    def __setattr__(sf, nm, v, /):
        raise AttributeError(nm)
    def __delattr__(sf, nm, /):
        raise AttributeError(nm)

def _get_func(sf, /):
    #check_type_is(_LazyImport4Func, sf)
    try:
        return _get(sf, '__f')
    except AttributeError:
        pass
    f = type(sf)._fetch_func(sf)
    _set(sf, '__f', f)
    return _get_func(sf)
_debug_ = __name__ == "__main__"
def _4locals(d, /):
    d = dict(d)
    del d['sf']
    return d
class _LazyImport4Func(_Forbid_get_set_del):
    #.@cached_property
    #.def _func_(sf, /):
    def _fetch_func(sf, /):
        (qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst) = _get(sf, '_args7ssdd')
        f = import4qobject(qnm4mdl8src, qnm4func8src)
        f = force_lazy_imported_func_(f)
        #######
        #original:
        #.check_callable(f)
        #######
        # !! ++__getitem__
        #.check_or_([check_callable, check_subscriptable], f)
        #######
        # !! ++__getattribute__
        # !! ++__pos__
        arbitrary_ok = _get(sf, '_arbitrary_ok')
        if not arbitrary_ok:
            check_or_([check_callable, check_subscriptable], f)
        #######
        _inject_(sf, smay_qnm4mdl8dst, smay_nm4func8dst, may_func8dst:=f)
        return f
    def __init__(sf, qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst, /, *, arbitrary_ok=False):
        check_type_is(bool, arbitrary_ok)
            #now:static_import
        #bug:check_type_is(bool, arbitrary_ok)
        #   !! _LazyImport4Func.__init__() UNDER: with mk_ctx4lazy_import4funcs_(__name__):...
        #   !! lazy_import__func7dict import under lazy-context => cause deadloop
        #if not type(arbitrary_ok) is bool:raise TypeError(type(arbitrary_ok))
        _set(sf, '_args4repr', (qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst))
        _set(sf, '_arbitrary_ok', arbitrary_ok)
        check_pseudo_qual_name(qnm4mdl8src)
        check_pseudo_qual_name(qnm4func8src)
        check_smay_pseudo_qual_name(smay_qnm4mdl8dst)
        check_smay_pseudo_identifier(smay_nm4func8dst)
        if smay_nm4func8dst and not smay_qnm4mdl8dst:raise TypeError
        if smay_qnm4mdl8dst and not smay_nm4func8dst:
            check_pseudo_identifier(smay_nm4func8dst:=qnm4func8src)
            #updated:smay_nm4func8dst
        assert bool(smay_qnm4mdl8dst) is bool(smay_nm4func8dst)
        #updated:smay_nm4func8dst
        _set(sf, '_args7ssdd', (qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst))

    def __repr__(sf, /):
        from seed.helper.repr_input import repr_helper
        arbitrary_ok = _get(sf, '_arbitrary_ok')
        kwds = {} if not arbitrary_ok else dict(arbitrary_ok=arbitrary_ok)
        args = _get(sf, '_args4repr')
        return repr_helper(sf, *args, **kwds)
    #:.+1,.+200s/^    def \(\w\+\)(.*):$/\0\r        if _debug_:print('\1', _4locals(locals()))
    def __call__(sf, /, *args, **kwds):
        if _debug_:print('__call__', _4locals(locals()))
        #.return sf._func_(*args, **kwds)
        return _get_func(sf)(*args, **kwds)
    ################
    #@20260313:
    ################
    def __getitem__(sf, k, /):
        if _debug_:print('__getitem__', _4locals(locals()))
        # ++@20260313:<<== from seed.tiny_.bmk_pairs import bmk_pairs
        return _get_func(sf)[k]
        #++?:def __getattribute__(sf, nm, /):
        #   cancelled by:_Forbid_get_set_del
    def __getattribute__(sf, nm, /):
        if _debug_:print('__getattribute__', _4locals(locals()))
        #++kw:arbitrary_ok
        #updated:check_type_is,check_type_le,check_is_obj:e ../../python3_src/seed/tiny_/check.py
        return getattr(_get_func(sf), nm)
    def __contains__(sf, k, /):
        if _debug_:print('__contains__', _4locals(locals()))
        return k in _get_func(sf)
    def __delitem__(sf, k, /):
        if _debug_:print('__delitem__', _4locals(locals()))
        del _get_func(sf)[k]
    def __setitem__(sf, k, v, /):
        if _debug_:print('__setitem__', _4locals(locals()))
        _get_func(sf)[k] = v
    def __bool__(sf, /):
        if _debug_:print('__bool__', _4locals(locals()))
        return bool(_get_func(sf))
    def __len__(sf, /):
        if _debug_:print('__len__', _4locals(locals()))
        return len(_get_func(sf))
    def __reversed__(sf, /):
        if _debug_:print('__reversed__', _4locals(locals()))
        return reversed(_get_func(sf))
    def __iter__(sf, /):
        if _debug_:print('__iter__', _4locals(locals()))
        return iter(_get_func(sf))
    def __aiter__(sf, /):
        if _debug_:print('__aiter__', _4locals(locals()))
        return aiter(_get_func(sf))
    def __dir__(sf, /):
        if _debug_:print('__dir__', _4locals(locals()))
        return dir(_get_func(sf))
    def __abs__(sf, /):
        if _debug_:print('__abs__', _4locals(locals()))
        return abs(_get_func(sf))
    def __pos__(sf, /):
        if _debug_:print('__pos__', _4locals(locals()))
        return +(_get_func(sf))
    def __neg__(sf, /):
        if _debug_:print('__neg__', _4locals(locals()))
        return -(_get_func(sf))
    def __invert__(sf, /):
        if _debug_:print('__invert__', _4locals(locals()))
        return ~(_get_func(sf))
    def __index__(sf, /):
        if _debug_:print('__index__', _4locals(locals()))
        return __index__(_get_func(sf))


    #metaclass-type.__instancecheck__
    #metaclass-type.__subclasscheck__
    #class-object.__subclasshook__

    def __instancecheck__(sf, x, /):
        if _debug_:print('__instancecheck__', _4locals(locals()))
        #@20260323
        #see:_test4isinstance_
        return isinstance(x, _get_func(sf))
    def __subclasscheck__(sf, x, /):
        if _debug_:print('__subclasscheck__', _4locals(locals()))
        #@20260323
        #see:_test4issubclass_
        return issubclass(x, _get_func(sf))


    def __hash__(sf, /):
        if _debug_:print('__hash__', _4locals(locals()))
        return hash(_get_func(sf))
    def __eq__(sf, ot, /):
        if _debug_:print('__eq__', _4locals(locals()))
        return _call(opss.__eq__, sf, ot)
    def __ne__(sf, ot, /):
        if _debug_:print('__ne__', _4locals(locals()))
        return _call(opss.__ne__, sf, ot)
    def __lt__(sf, ot, /):
        if _debug_:print('__lt__', _4locals(locals()))
        return _call(opss.__lt__, sf, ot)
    def __le__(sf, ot, /):
        if _debug_:print('__le__', _4locals(locals()))
        return _call(opss.__le__, sf, ot)
    def __ge__(sf, ot, /):
        if _debug_:print('__ge__', _4locals(locals()))
        return _call(opss.__ge__, sf, ot)
    def __gt__(sf, ot, /):
        if _debug_:print('__gt__', _4locals(locals()))
        return _call(opss.__gt__, sf, ot)

    def __divmod__(sf, ot, /):
        if _debug_:print('__divmod__', _4locals(locals()))
        return _call(divmod, sf, ot)
    def __rdivmod__(sf, ot, /):
        if _debug_:print('__rdivmod__', _4locals(locals()))
        return _rcall(divmod, ot, sf)



    # :s/ *\(\w\+\)/def \1(sf, ot, \/):\r    return _call(opss.\1, sf, ot)\r/g
    # __sub__ __add__ __pow__ __matmul__ __mul__ __mod__ __floordiv__ __truediv__ __rshift__ __lshift__ __or__ __and__ __xor__
    #
    # :s/ *__r\(\w\+\)/def __r\1(sf, ot, \/):\r    return _rcall(opss.__\1, ot, sf)\r/g
    # __rsub__ __radd__ __rpow__ __rmatmul__ __rmul__ __rmod__ __rfloordiv__ __rtruediv__ __rrshift__ __rlshift__ __ror__ __rand__ __rxor__
    #
    # :s/ *\(\w\+\)/def \1(sf, ot, \/):\r    return _call(opss.\1, sf, ot)\r/g
    # __isub__ __iadd__ __ipow__ __imatmul__ __imul__ __imod__ __ifloordiv__ __itruediv__ __irshift__ __ilshift__ __ior__ __iand__ __ixor__
    #
    #pow:++args
    def __sub__(sf, ot, /):
        if _debug_:print('__sub__', _4locals(locals()))
        return _call(opss.__sub__, sf, ot)
    def __add__(sf, ot, /):
        if _debug_:print('__add__', _4locals(locals()))
        return _call(opss.__add__, sf, ot)
    def __pow__(sf, ot, /, *args):
        if _debug_:print('__pow__', _4locals(locals()))
        return _call(opss.__pow__, sf, ot, *args)
    def __matmul__(sf, ot, /):
        if _debug_:print('__matmul__', _4locals(locals()))
        return _call(opss.__matmul__, sf, ot)
    def __mul__(sf, ot, /):
        if _debug_:print('__mul__', _4locals(locals()))
        return _call(opss.__mul__, sf, ot)
    def __mod__(sf, ot, /):
        if _debug_:print('__mod__', _4locals(locals()))
        return _call(opss.__mod__, sf, ot)
    def __floordiv__(sf, ot, /):
        if _debug_:print('__floordiv__', _4locals(locals()))
        return _call(opss.__floordiv__, sf, ot)
    def __truediv__(sf, ot, /):
        if _debug_:print('__truediv__', _4locals(locals()))
        return _call(opss.__truediv__, sf, ot)
    def __rshift__(sf, ot, /):
        if _debug_:print('__rshift__', _4locals(locals()))
        return _call(opss.__rshift__, sf, ot)
    def __lshift__(sf, ot, /):
        if _debug_:print('__lshift__', _4locals(locals()))
        return _call(opss.__lshift__, sf, ot)
    def __or__(sf, ot, /):
        if _debug_:print('__or__', _4locals(locals()))
        return _call(opss.__or__, sf, ot)
    def __and__(sf, ot, /):
        if _debug_:print('__and__', _4locals(locals()))
        return _call(opss.__and__, sf, ot)
    def __xor__(sf, ot, /):
        if _debug_:print('__xor__', _4locals(locals()))
        return _call(opss.__xor__, sf, ot)


    def __isub__(sf, ot, /):
        if _debug_:print('__isub__', _4locals(locals()))
        return _call(opss.__isub__, sf, ot)
    def __iadd__(sf, ot, /):
        if _debug_:print('__iadd__', _4locals(locals()))
        return _call(opss.__iadd__, sf, ot)
    def __ipow__(sf, ot, /, *args):
        if _debug_:print('__ipow__', _4locals(locals()))
        return _call(opss.__ipow__, sf, ot, *args)
    def __imatmul__(sf, ot, /):
        if _debug_:print('__imatmul__', _4locals(locals()))
        return _call(opss.__imatmul__, sf, ot)
    def __imul__(sf, ot, /):
        if _debug_:print('__imul__', _4locals(locals()))
        return _call(opss.__imul__, sf, ot)
    def __imod__(sf, ot, /):
        if _debug_:print('__imod__', _4locals(locals()))
        return _call(opss.__imod__, sf, ot)
    def __ifloordiv__(sf, ot, /):
        if _debug_:print('__ifloordiv__', _4locals(locals()))
        return _call(opss.__ifloordiv__, sf, ot)
    def __itruediv__(sf, ot, /):
        if _debug_:print('__itruediv__', _4locals(locals()))
        return _call(opss.__itruediv__, sf, ot)
    def __irshift__(sf, ot, /):
        if _debug_:print('__irshift__', _4locals(locals()))
        return _call(opss.__irshift__, sf, ot)
    def __ilshift__(sf, ot, /):
        if _debug_:print('__ilshift__', _4locals(locals()))
        return _call(opss.__ilshift__, sf, ot)
    def __ior__(sf, ot, /):
        if _debug_:print('__ior__', _4locals(locals()))
        return _call(opss.__ior__, sf, ot)
    def __iand__(sf, ot, /):
        if _debug_:print('__iand__', _4locals(locals()))
        return _call(opss.__iand__, sf, ot)
    def __ixor__(sf, ot, /):
        if _debug_:print('__ixor__', _4locals(locals()))
        return _call(opss.__ixor__, sf, ot)


    def __rsub__(sf, ot, /):
        if _debug_:print('__rsub__', _4locals(locals()))
        return _rcall(opss.__sub__, ot, sf)
    def __radd__(sf, ot, /):
        if _debug_:print('__radd__', _4locals(locals()))
        return _rcall(opss.__add__, ot, sf)
    def __rpow__(sf, ot, /):
        if _debug_:print('__rpow__', _4locals(locals()))
        return _rcall(opss.__pow__, ot, sf)
    def __rmatmul__(sf, ot, /):
        if _debug_:print('__rmatmul__', _4locals(locals()))
        return _rcall(opss.__matmul__, ot, sf)
    def __rmul__(sf, ot, /):
        if _debug_:print('__rmul__', _4locals(locals()))
        return _rcall(opss.__mul__, ot, sf)
    def __rmod__(sf, ot, /):
        if _debug_:print('__rmod__', _4locals(locals()))
        return _rcall(opss.__mod__, ot, sf)
    def __rfloordiv__(sf, ot, /):
        if _debug_:print('__rfloordiv__', _4locals(locals()))
        return _rcall(opss.__floordiv__, ot, sf)
    def __rtruediv__(sf, ot, /):
        if _debug_:print('__rtruediv__', _4locals(locals()))
        return _rcall(opss.__truediv__, ot, sf)
    def __rrshift__(sf, ot, /):
        if _debug_:print('__rrshift__', _4locals(locals()))
        return _rcall(opss.__rshift__, ot, sf)
    def __rlshift__(sf, ot, /):
        if _debug_:print('__rlshift__', _4locals(locals()))
        return _rcall(opss.__lshift__, ot, sf)
    def __ror__(sf, ot, /):
        if _debug_:print('__ror__', _4locals(locals()))
        return _rcall(opss.__or__, ot, sf)
    def __rand__(sf, ot, /):
        if _debug_:print('__rand__', _4locals(locals()))
        return _rcall(opss.__and__, ot, sf)
    def __rxor__(sf, ot, /):
        if _debug_:print('__rxor__', _4locals(locals()))
        return _rcall(opss.__xor__, ot, sf)


def _call(f, sf, /, *args):
    sf = _get_func(sf)
    return f(sf, *map(force_lazy_imported_func_, args))
def _rcall(f, ot, sf, /, *args):
    sf = _get_func(sf)
    ot = force_lazy_imported_func_(ot)
    return f(ot, sf, *map(force_lazy_imported_func_, args))
#import operator as s
#dir(s)
'__abs__'
'__neg__'
'__pos__'
'__invert__'

'__contains__'
'__call__'
'__getitem__'
'__setitem__'
'__delitem__'

'__eq__'
'__ge__'
'__gt__'
'__le__'
'__lt__'
'__ne__'

'__sub__'
'__add__'
'__pow__'
'__matmul__'
'__mul__'
'__mod__'
'__floordiv__'
'__truediv__'
'__rshift__'
'__lshift__'

'__or__'
'__and__'
'__xor__'

'__isub__'
'__iadd__'
'__ipow__'
'__imatmul__'
'__imul__'
'__imod__'
'__ifloordiv__'
'__itruediv__'
'__irshift__'
'__ilshift__'

'__ior__'
'__iand__'
'__ixor__'

#__divmod__
#dir(__builtins__)
'abs'
'aiter'
'anext'
'ascii'
'bool'
'delattr'
'dir'
'divmod'
'getattr'
'hasattr'
'hash'
'id'
'isinstance'
'issubclass'
'iter'
'len'
'next'
'pow'
'repr'
'reversed'
'round'
'setattr'
'sorted'
'str'
'type'
'vars'
def _test4isinstance_():
    global _debug_
    saved_debug = _debug_
    _debug_ = True
    try:
        #from seed.types.LazyObj import Lazy, LazyX, LazyAttrs
        assert not 'Lazy' in globals()
        Lazy = lazy_import4func_('seed.types.LazyObj', 'Lazy', __name__)
        isinstance(999, Lazy)
            # not ^TypeError???
            #before:++__instancecheck__:
            #   =>『__getattribute__ {'nm': '__bases__'}』
            #after:++__instancecheck__:
            #   =>『__instancecheck__ {'x': 999}』
        assert 'Lazy' in globals()
        #assert not isinstance(999, Lazy)
    finally:
        _debug_ = saved_debug

def _test4issubclass_():
    global _debug_
    saved_debug = _debug_
    _debug_ = True
    try:
        #from seed.types.LazyObj import Lazy, LazyX, LazyAttrs
        assert not 'Lazy' in globals()
        Lazy = lazy_import4func_('seed.types.LazyObj', 'Lazy', __name__)
        issubclass(int, Lazy)
            # not ^TypeError???
            #before:++__subclasscheck__:
            #   =>『__getattribute__ {'nm': '__bases__'}』
            #after:++__subclasscheck__:
            #   =>『__subclasscheck__ {'x': <class 'int'>}』
        assert 'Lazy' in globals()
        #assert not issubclass(int, Lazy)
    finally:
        _debug_ = saved_debug



def lazy_import4func_(qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst='', smay_nm4func8dst='', /, *, arbitrary_ok=False):
    sf = _LazyImport4Func(qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst, arbitrary_ok=arbitrary_ok)
    (qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst) = _get(sf, '_args7ssdd')
        # updated:smay_nm4func8dst
    _inject_(sf, smay_qnm4mdl8dst, smay_nm4func8dst, may_func8dst:=None)
    return sf
def lazy_import4funcs_(qnm4mdl8src, xqnms4func8src, smay_qnm4mdl8dst='', /):
    r'''[[[
    [xqnms4func8src :: (Iter xqnm4func8src) | xqnms4func8src__str]
    [xqnms4func8src__str <- regex"{xqnm4func8src}(,{xqnm4func8src})*"]
    [xqnm4func8src <- regex"{qnm4func8src}(:{nm4func8dst})?"]
    #]]]'''#'''
    if type(xqnms4func8src) is str:
        xqnms4func8src = xqnms4func8src.split(',')
    xs = []
    for xqnm4func8src in xqnms4func8src:
        qnm4func8src, _, smay_nm4func8dst = xqnm4func8src.partition(':')
        x = lazy_import4func_(qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst, smay_nm4func8dst)
        xs.append(x)
    return xs


def force_lazy_imported_func_(f, /):
    #updated:check_type_is,check_type_le,check_is_obj:e ../../python3_src/seed/tiny_/check.py
    if type(f) is _LazyImport4Func:
        #.f = f._func_
        f = _get_func(f)
        assert not type(f) is _LazyImport4Func
    return f


def force_lazy_imported_obj_(obj, /):
    ids = set()
    while 1:
        ids.add(id(obj))
        if type(obj) is _LazyImport8LazyObj:
            obj = _get_obj(obj)
            assert not type(obj) is _LazyImport8LazyObj
            if id(obj) in ids:raise 000
            ids.add(id(obj))
        _obj = force_lazy_imported_func_(obj)
        if _obj is obj:
            break
        if id(_obj) in ids:raise 000
        obj = _obj
    return obj


def _get_obj(sf, /):
    #check_type_is(_LazyImport8LazyObj, sf)
    try:
        return _get(sf, '__x')
    except AttributeError:
        pass
    x = type(sf)._fetch_obj(sf)
    _set(sf, '__x', x)
    return _get_obj(sf)
class _LazyImport8LazyObj(_Forbid_get_set_del):
    #.@cached_property
    #.def _obj_(sf, /):
    def _fetch_obj(sf, /):
        (qnm4mdl8src, may_qnm4obj8src, may_either_mdl_obj) = _get(sf, '_args4import4qobject')
        if not may_either_mdl_obj is None:
            either_mdl_obj = may_either_mdl_obj
            (mdl_vs_obj, mdl_or_obj) = either_mdl_obj
            if mdl_vs_obj:
                obj = mdl_or_obj
            else:
                mdl8src = mdl_or_obj
                if may_qnm4obj8src is None:
                    obj = mdl8src
                else:
                    qnm4obj8src = may_qnm4obj8src
                    #???buggy???:from operator import attrgetter
                    #   e ../../python3_src/seed/helper/lazy_import__func7context.py
                    obj = attrgetter(qnm4obj8src)(mdl8src)
                obj
            obj
        else:
            obj = import4qobject(qnm4mdl8src, may_qnm4obj8src)
        obj
        obj = force_lazy_imported_obj_(obj)
        return obj
    def __init__(sf, qnm4mdl8src, smay_qnm4obj8src, may_either_mdl_obj, /):
        _set(sf, '_args4repr', (qnm4mdl8src, smay_qnm4obj8src, may_either_mdl_obj))
        check_pseudo_qual_name(qnm4mdl8src)
        check_smay_pseudo_qual_name(smay_qnm4obj8src)
        may_qnm4obj8src = None if not smay_qnm4obj8src else smay_qnm4obj8src
        _set(sf, '_args4import4qobject', (qnm4mdl8src, may_qnm4obj8src, may_either_mdl_obj))

    def __call__(sf, /):
        #.return sf._obj_
        return _get_obj(sf)
    def __repr__(sf, /):
        from seed.helper.repr_input import repr_helper
        return repr_helper(sf, *_get(sf, '_args4repr'))

def lazy_import8lazy_obj_(qnm4mdl8src, smay_qnm4obj8src, may_either_mdl_obj=None, /):
    sf = _LazyImport8LazyObj(qnm4mdl8src, smay_qnm4obj8src, may_either_mdl_obj)
    return sf








class _LazyData:
    @cached_property
    def regex4FromImportStmt(sf, /):
        import re
        regex4FromImportStmt = re.compile(r'^(\s*)from\s+(\S+)\s+import\s+([^()#]+|[(][^()#]+[)]\s+)((?:#.*)?)$')
        return regex4FromImportStmt
    def parse4regex4FromImportStmt(sf, match_obj, /):
        (indent, qnm4mdl, import_list, smay_comment) = match_obj.groups()
        import_list = import_list.replace('(', ' ').replace(')', ' ').strip()
        import_list = ' '.join(import_list.split())
        _import_list = import_list.replace(' as ', ':').replace(' ', '')
        line = match_obj.group(0)
        content = line.strip()
        s = f"{indent}lazy_import4funcs_('{qnm4mdl}', '{_import_list}', __name__)\n{indent}if 0:{content}"
        return (s, (indent, qnm4mdl, _import_list, smay_comment, content))
_lazy_data = _LazyData()

#.def main4convert_FromImportStmt6seed_tiny(nms4funcs, /):
#.    'deeper and lazy version of "from seed.tiny import ..."'
def filter_FromImportStmt6seed_tiny(nms4funcs, /):
    'deeper version of "from seed.tiny import ..."'
    import re
    from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_
    from seed.tiny_.containers import mk_tuple__split_first_if_str
    from seed.tiny_.check import check_pseudo_identifier, check_all_

    nms4funcs = mk_tuple__split_first_if_str(nms4funcs, ',')
    check_all_(check_pseudo_identifier, nms4funcs)
    s = '|'.join(nms4funcs)
    s = fr'\b(?:{s})\b'
    regex8nms = re.compile(s)
    txt = read_under_pkg_('seed', 'tiny.py', xencoding='u8')
    for line in txt.split('\n'):
        if not line.startswith('from '):
            continue
        if line.startswith('from seed.tiny import '):
            continue
        j = line.find(mid:=' import ')
        if j == -1:
            continue
        m = regex8nms.search(line[j+len(mid):])
        if not m:
            continue
        yield line

def main4convert_FromImportStmt(args=None, /):
    regex4FromImportStmt = _lazy_data.regex4FromImportStmt
    parse4regex4FromImportStmt = _lazy_data.parse4regex4FromImportStmt
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description=r'''convert "from xxx.yyy import aaa, bbb as ccc" to "lazy_import4funcs_('xxx.yyy', 'aaa,bbb:ccc', __name__);\nif 0:from xxx.yyy import aaa, bbb as ccc"'''
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-ie', '--iencoding', type=str
                        , default='utf8'
                        , help='input file encoding')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    force = args.force
    omode = 'wt' if args.force else 'xt'
    iencoding = args.iencoding
    oencoding = args.oencoding
    iencoding = 'utf8' if not iencoding else iencoding
    oencoding = 'utf8' if not oencoding else oencoding

    may_ifname = args.input
    may_ofname = args.output
    with may_open_stdin(may_ifname, 'rt', encoding=iencoding) as fin, may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        for line in fin:
            m = regex4FromImportStmt.fullmatch(line)
            if m:
                (s, _) = parse4regex4FromImportStmt(m)
                print(s, end='\n\n', file=fout)

from seed.helper.lazy_import__func import *
if __name__ == "__main__":
    main4convert_FromImportStmt()
#.if __name__ == "__main__":
#.    from seed.helper.lazy_import__func import _test4isinstance_
#.    _debug_ = True
#.    _test4isinstance_()


__all__
####################################
#static_import
___begin_mark_of_excluded_global_names__1___ = ...
from seed.tiny_.check import check_pseudo_identifier, check_smay_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name
from seed.tiny_.check import check_callable, check_or_, check_subscriptable
from seed.tiny_.check import check_type_is
___end_mark_of_excluded_global_names__1___ = ...
####################################

__all__
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_, force_lazy_imported_obj_, lazy_import8lazy_obj_
#.def lazy_import4func_(qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst='', smay_nm4func8dst='', /):
#.def lazy_import8lazy_obj_(qnm4mdl8src, smay_qnm4obj8src, may_either_mdl_obj=None, /):
if 1:from seed.helper.lazy_import__func import filter_FromImportStmt6seed_tiny, main4convert_FromImportStmt
from seed.helper.lazy_import__func import *
