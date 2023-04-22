#__all__:goto
#[[[__doc__-begin
r'''

seed.tiny_.mk_fdefault
    used in:
        seed.mapping_tools.fdefault
py -m seed.tiny_.mk_fdefault
py -m nn_ns.app.debug_cmd   seed.tiny_.mk_fdefault

xdefault # imay, xdefault, ...
    see: mk_default
xedefault # -3- ?, ..., mirror=?
    see: mk_default_or_raise===mk_default_or_raise__ver2
zdefault # ... # handle all cases
    see: mk_default__easy===mk_default5zdefault



from seed.tiny_.mk_fdefault import mk_default__easy, mk_default, mk_default_or_raise
    #def mk_default__easy(*tmay_Nothing___or___args4mk_default_or_raise, mirror=False):
    #def mk_default(imay_xdefault_rank, xdefault, /, *args4xdefault):
    #def mk_default_or_raise(mirror_imay_xedefault_rank, xedefault, /, *args4xedefault, mirror:bool):
    #   imay_xdefault_ranks = (-3)-mirror_imay_xedefault_rank if mirror_imay_xedefault_rank < -1 else mirror_imay_xedefault_rank
    #   mirrored = (mirror_imay_xedefault_rank < -1) ^ bool(mirror)
    #

from seed.tiny_.mk_fdefault import mk_fdefault, mk_default, eliminate_tmay__mix, eliminate_tmay_or_raise__simple, BasePermissionMappingOps, SimplePermissionMappingOps, XDefaultDict, ops4XDefaultMapping

from seed.tiny_.mk_fdefault import mk_fdefaultP, mk_fdefault, mk_fdefaultP_from_default, mk_fdefault_from_default, Mk_fdefaultP, Mk_fdefault, Mk_fdefault1__caller_args_at_last, Mk_fdefault1__caller_args_at_first, Mk_fdefaultP_from_default, Mk_fdefault_from_default, mk_default2value__default_at_last, mk_default2value__default_at_first, mk_tmay_from_default2value, mk_fvalue, mk_tmay_from_is_safe_fvalue, mk_tmay_from_try_fvalue, mk_tmay_from_try_fvalue_KeyError


from seed.tiny_.mk_fdefault import mk_default_or_raise, mirror_rank2imay_rank, mk_default_or_raise__ver1, mk_edefault__cased, eliminate_cased_edefault__raise, mk_default_or_raise__ver2, reform_args_from_mk_default_or_raise, raise4mk_default_or_raise, mk_default

from seed.tiny_.mk_fdefault import eliminate_tmay, eliminate_tmay__cased, eliminate_tmay__mix, eliminate_tmay_or_raise, eliminate_tmay_or_raise__simple

from seed.tiny_.mk_fdefault import BasePermissionMappingOps, MappingOpsPermission, SimplePermissionMappingOps, LazyValueCachedTransitionalObj, XDefaultMappingOps, ops4XDefaultMapping, WeakableXDefaultDict, XDefaultDict, XDefaultHashMappingMixin, XDefaultMappingMixin, MappingMixin__auto_setdefault_via_slice4HashMap




#[[[doctest_examples:BEGIN
>>> echo_args_kwargs = lambda *args, **kwargs:(args, kwargs)


#doctest_examples:mk_fdefault
>>> fdefault = mk_fdefault(echo_args_kwargs, 1, 2, a=3, b=4)
>>> fdefault() == ((1,2), dict(a=3, b=4))
True
>>> fdefault(0)
Traceback (most recent call last):
    ...
TypeError
>>> fdefault(z=5)
Traceback (most recent call last):
    ...
TypeError



#doctest_examples:mk_fdefaultP
>>> fdefault = mk_fdefaultP(False, 1, {'z'}, echo_args_kwargs, 1, 2, a=3, b=4)
>>> fdefault()
Traceback (most recent call last):
    ...
TypeError
>>> fdefault(0) == ((0,1,2), dict(a=3, b=4))
True
>>> fdefault(0,0)
Traceback (most recent call last):
    ...
TypeError
>>> fdefault(z=5)
Traceback (most recent call last):
    ...
TypeError
>>> fdefault(0,z=5) == ((0,1,2), dict(a=3, b=4,z=5))
True
>>> fdefault(0,0,z=5)
Traceback (most recent call last):
    ...
TypeError
>>> fdefault(0,y=6,z=5)
Traceback (most recent call last):
    ...
TypeError


>>> fdefault = mk_fdefaultP(True, 1, {'z'}, echo_args_kwargs, 1, 2, a=3, b=4)
>>> fdefault(0) == ((1,2,0), dict(a=3, b=4))
True
>>> fdefault(0,z=5) == ((1,2,0), dict(a=3, b=4,z=5))
True



>>> default = "default:xxx"
>>> default = object()

#doctest_examples:mk_fdefault_from_default
>>> fdefault = mk_fdefault_from_default(default)
>>> fdefault() is default
True
>>> fdefault(0)
Traceback (most recent call last):
    ...
TypeError
>>> fdefault(z=5)
Traceback (most recent call last):
    ...
TypeError




#doctest_examples:mk_fdefaultP_from_default
>>> fdefault = mk_fdefaultP_from_default(1, {'z'}, default)
>>> fdefault()
Traceback (most recent call last):
    ...
TypeError
>>> fdefault(0) is default
True
>>> fdefault(0,0)
Traceback (most recent call last):
    ...
TypeError
>>> fdefault(z=5)
Traceback (most recent call last):
    ...
TypeError
>>> fdefault(0,z=5) is default
True
>>> fdefault(0,0,z=5)
Traceback (most recent call last):
    ...
TypeError
>>> fdefault(0,y=6,z=5)
Traceback (most recent call last):
    ...
TypeError





mk_tmay_from_try_fvalue_KeyError
mk_tmay_from_default2value
>>> import operator as opss


mk_tmay_from_try_fvalue_KeyError
>>> mk_tmay_from_try_fvalue_KeyError(mk_fvalue(opss.__getitem__, {}, 1))
()
>>> mk_tmay_from_try_fvalue_KeyError(mk_fvalue(opss.__getitem__, {1:2}, 1))
(2,)
>>> mk_tmay_from_try_fvalue_KeyError(mk_fvalue(opss.__getitem__, [3], 1))
Traceback (most recent call last):
    ...
IndexError: list index out of range
>>> mk_tmay_from_try_fvalue_KeyError(mk_fvalue(opss.__getitem__, [3,4], 1))
(4,)


mk_tmay_from_default2value
>>> mk_tmay_from_default2value(mk_default2value__default_at_last({}.pop, 1))
()
>>> mk_tmay_from_default2value(mk_default2value__default_at_last({1:2}.pop, 1))
(2,)
>>> mk_tmay_from_default2value(mk_default2value__default_at_last([3].pop, 1))
Traceback (most recent call last):
    ...
TypeError: pop expected at most 1 argument, got 2
>>> mk_tmay_from_default2value(mk_default2value__default_at_last([3,4].pop, 1))
Traceback (most recent call last):
    ...
TypeError: pop expected at most 1 argument, got 2



mk_default
>>> mk_default(-1, 999)
999
>>> mk_default(0, 999)
Traceback (most recent call last):
    ...
TypeError: 'int' object is not callable
>>> mk_default(-2, 999)
Traceback (most recent call last):
    ...
TypeError
>>> mk_default(1, 999)
Traceback (most recent call last):
    ...
TypeError


>>> from seed.tiny_.funcs import echo_args
>>> mk_default(-1, echo_args) is echo_args
True
>>> mk_default(0, echo_args)
()
>>> mk_default(1, echo_args)
Traceback (most recent call last):
    ...
TypeError

>>> mk_default(-1, echo_args, 'a') is echo_args
True
>>> mk_default(0, echo_args, 'a')
()
>>> mk_default(1, echo_args, 'a')
('a',)
>>> mk_default(2, echo_args, 'a')
Traceback (most recent call last):
    ...
TypeError

>>> mk_default(-1, echo_args, *'ab') is echo_args
True
>>> mk_default(0, echo_args, *'ab')
()
>>> mk_default(1, echo_args, *'ab')
('b',)
>>> mk_default(2, echo_args, *'ab')
('a', 'b')
>>> mk_default(3, echo_args, *'ab')
Traceback (most recent call last):
    ...
TypeError

>>> mk_default(-1, echo_args, *'abc') is echo_args
True
>>> mk_default(0, echo_args, *'abc')
()
>>> mk_default(1, echo_args, *'abc')
('c',)
>>> mk_default(2, echo_args, *'abc')
('b', 'c')
>>> mk_default(3, echo_args, *'abc')
('a', 'b', 'c')
>>> mk_default(4, echo_args, *'abc')
Traceback (most recent call last):
    ...
TypeError

>>> _mk_d_e = lambda *args, **kwargs: mk_default_or_raise(*args, mirror=False, **kwargs)
>>> _mk_d_e(-1, echo_args, *'abc') is echo_args
True
>>> _mk_d_e(0, echo_args, *'abc')
()
>>> _mk_d_e(1, echo_args, *'abc')
('c',)
>>> _mk_d_e(2, echo_args, *'abc')
('b', 'c')
>>> _mk_d_e(3, echo_args, *'abc')
('a', 'b', 'c')
>>> _mk_d_e(4, echo_args, *'abc')
Traceback (most recent call last):
    ...
TypeError

>>> _mk_d_e(-2, Exception(999), *'abc')
Traceback (most recent call last):
    ...
Exception: 999
>>> _mk_d_e(-2, Exception, *'abc')
Traceback (most recent call last):
    ...
Exception
>>> _mk_d_e(-3, Exception, *'abc')
Traceback (most recent call last):
    ...
Exception
>>> _mk_d_e(-4, Exception, *'abc')
Traceback (most recent call last):
    ...
Exception: c
>>> _mk_d_e(-5, Exception, *'abc')
Traceback (most recent call last):
    ...
Exception: ('b', 'c')
>>> _mk_d_e(-6, Exception, *'abc')
Traceback (most recent call last):
    ...
Exception: ('a', 'b', 'c')
>>> _mk_d_e(-7, Exception, *'abc')
Traceback (most recent call last):
    ...
TypeError


>>> _mk_d_e_T = lambda *args, **kwargs: mk_default_or_raise(*args, mirror=True, **kwargs)
>>> _mk_d_e_T(-2, echo_args, *'abc') is echo_args
True
>>> _mk_d_e_T(-1, Exception(999), *'abc')
Traceback (most recent call last):
    ...
Exception: 999






eliminate_tmay__cased
eliminate_tmay__mix
>>> eliminate_tmay__cased((), 2, echo_args, *'abc')
(False, ('b', 'c'))
>>> eliminate_tmay__cased((999,), 2, echo_args, *'abc')
(True, 999)

>>> eliminate_tmay__mix((), 2, echo_args, *'abc')
('b', 'c')
>>> eliminate_tmay__mix((999,), 2, echo_args, *'abc')
999



XDefaultMappingMixin
>>> {}[:]
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'



>>> d = XDefaultDict()
>>> d #not override repr/__repr__
{}
>>> d[1]
Traceback (most recent call last):
    ...
KeyError: 1
>>> d[1:list]
[]
>>> d
{1: []}
>>> d[1:list:-1]
[]
>>> d[2:list:-1]
<class 'list'>
>>> d[2]
<class 'list'>
>>> d[1]
[]
>>> d[3:type:1]
<class 'int'>
>>> d[4:str:1]
'4'
>>> d == {1: [], 2: list, 3: int, 4: '4'}
True
>>> d[5:lambda d,k,/:(type(d), k):2] == (XDefaultDict, 5)
True


>>> d = XDefaultDict({2:3})
>>> d.get__tmay(1)
()
>>> d.get__tmay(2)
(3,)
>>> d.pop__tmay(1)
()
>>> d.pop__tmay(2)
(3,)
>>> d.get__tmay(2)
()


>>> d == {}
True
>>> d.set__xdefault(1, -1, 999, mix=False)
(False, 999)
>>> d.set__xdefault(1, -1, 888, mix=False)
(True, 999)
>>> d.set__xdefault(1, -1, 888, mix=True)
999
>>> d.set__xdefault(2, -1, 888, mix=True)
888
>>> d == {1:999, 2:888}
True


>>> d.get__xdefault(3, -1, 777, mix=False)
(False, 777)
>>> d.pop__xdefault(3, -1, 777, mix=False)
(False, 777)

>>> d.get__xdefault(3, -1, 777, mix=True)
777
>>> d.pop__xdefault(3, -1, 777, mix=True)
777


>>> d.get__xdefault(1, -1, 777, mix=False)
(True, 999)
>>> d.pop__xdefault(1, -1, 777, mix=False)
(True, 999)

>>> d.get__xdefault(2, -1, 777, mix=True)
888
>>> d.pop__xdefault(2, -1, 777, mix=True)
888



>>> d == {}
True
>>> d.set__xdefault__cased(1, -1, 999)
(False, 999)
>>> d.set__xdefault__cased(1, -1, 888)
(True, 999)
>>> d.set__xdefault__mix(1, -1, 888)
999
>>> d.set__xdefault__mix(2, -1, 888)
888
>>> d == {1:999, 2:888}
True


>>> d.get__xdefault__cased(3, -1, 777)
(False, 777)
>>> d.pop__xdefault__cased(3, -1, 777)
(False, 777)

>>> d.get__xdefault__mix(3, -1, 777)
777
>>> d.pop__xdefault__mix(3, -1, 777)
777


>>> d.get__xdefault__cased(1, -1, 777)
(True, 999)
>>> d.pop__xdefault__cased(1, -1, 777)
(True, 999)

>>> d.get__xdefault__mix(2, -1, 777)
888
>>> d.pop__xdefault__mix(2, -1, 777)
888


BasePermissionMappingOps
SimplePermissionMappingOps
>>> ops = SimplePermissionMappingOps(0)
>>> d = {1:2}
>>> ops.detect(d, 2)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.get__tmay(d, 2)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.set__new_or_overwrite(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.detect_set__new_or_pass(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.detect_set__overwrite_or_pass(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.drop__delete_or_pass(d, 2)
Traceback (most recent call last):
    ...
PermissionError





>>> ops = SimplePermissionMappingOps(MappingOpsPermission.detect)
>>> d = {1:2}
>>> ops.detect(d, 1)
True
>>> ops.detect(d, 2)
False
>>> ops.get__tmay(d, 2)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.set__new_or_overwrite(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.detect_set__new_or_pass(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.detect_set__overwrite_or_pass(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.drop__delete_or_pass(d, 2)
Traceback (most recent call last):
    ...
PermissionError



>>> ops = SimplePermissionMappingOps(MappingOpsPermission.get__tmay)
>>> d = {1:2}
>>> ops.detect(d, 1)
True
>>> ops.detect(d, 2)
False
>>> ops.get__tmay(d, 1)
(2,)
>>> ops.get__tmay(d, 2)
()
>>> ops.set__new_or_overwrite(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.detect_set__new_or_pass(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.detect_set__overwrite_or_pass(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.drop__delete_or_pass(d, 2)
Traceback (most recent call last):
    ...
PermissionError
>>> d
{1: 2}




>>> ops = SimplePermissionMappingOps(MappingOpsPermission.set__new_or_overwrite)
>>> d = {1:2}
>>> ops.detect(d, 1)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.get__tmay(d, 1)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.set__new_or_overwrite(d, 1, lambda:4)
4
>>> ops.set__new_or_overwrite(d, 2, lambda:4)
4
>>> ops.detect_set__new_or_pass(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.detect_set__overwrite_or_pass(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.drop__delete_or_pass(d, 2)
Traceback (most recent call last):
    ...
PermissionError
>>> d == {1:4, 2:4}
True



>>> ops = SimplePermissionMappingOps(MappingOpsPermission.detect_set__new_or_pass)
>>> d = {1:2}
>>> ops.detect(d, 1)
True
>>> ops.detect(d, 2)
False
>>> ops.get__tmay(d, 1)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.set__new_or_overwrite(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.detect_set__new_or_pass(d, 1, lambda:4)
()
>>> ops.detect_set__new_or_pass(d, 2, lambda:4)
(4,)
>>> ops.detect_set__overwrite_or_pass(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.drop__delete_or_pass(d, 2)
Traceback (most recent call last):
    ...
PermissionError
>>> d == {1:2,2:4}
True



>>> ops = SimplePermissionMappingOps(MappingOpsPermission.detect_set__overwrite_or_pass)
>>> d = {1:2}
>>> ops.detect(d, 1)
True
>>> ops.detect(d, 2)
False
>>> ops.get__tmay(d, 1)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.set__new_or_overwrite(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.detect_set__new_or_pass(d, 1, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.detect_set__overwrite_or_pass(d, 1, lambda:4)
(4,)
>>> ops.detect_set__overwrite_or_pass(d, 2, lambda:4)
()
>>> ops.drop__delete_or_pass(d, 2)
Traceback (most recent call last):
    ...
PermissionError
>>> d
{1: 4}



>>> ops = SimplePermissionMappingOps(MappingOpsPermission.drop__delete_or_pass)
>>> d = {1:2}
>>> ops.detect(d, 2)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.get__tmay(d, 2)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.set__new_or_overwrite(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.detect_set__new_or_pass(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.detect_set__overwrite_or_pass(d, 2, lambda:4)
Traceback (most recent call last):
    ...
PermissionError
>>> ops.drop__delete_or_pass(d, 1)
>>> ops.drop__delete_or_pass(d, 2)
>>> d
{}









uniform_read_calc_update

#>>> ops.detect(d, 2)
#>>> ops.get__tmay(d, 2)
#>>> ops.set__new_or_overwrite(d, 2, lambda:4)
#>>> ops.detect_set__new_or_pass(d, 2, lambda:4)
#>>> ops.detect_set__overwrite_or_pass(d, 2, lambda:4)
#>>> ops.drop__delete_or_pass(d, 2)





>>> from seed.tiny_.mk_fdefault import mk_default__easy, mk_default5zdefault
>>> class ok(Exception):pass
>>> class bad(Exception):pass

>>> mk_default5zdefault is mk_default__easy
>>> mk_default__easy(111)
>>> mk_default__easy(111)
111
>>> mk_default__easy(-1, 111)
111
>>> mk_default__easy(0, ok)
ok()
>>> mk_default__easy(1, ok, 111)
ok(111)
>>> mk_default__easy(2, ok, 333, 222, 111)
ok(222, 111)
>>> mk_default__easy(1, ok, 333, 222, 111)
ok(111)
>>> mk_default__easy(0, ok, 333, 222, 111)
ok()

>>> mk_default__easy(-3- -1, 111, mirror=True)
111
>>> mk_default__easy(-3- 0, ok, mirror=True)
ok()
>>> mk_default__easy(-3- 1, ok, 111, mirror=True)
ok(111)



>>> mk_default__easy()
Traceback (most recent call last):
    ...
TypeError: miss default value
>>> mk_default__easy(mirror=True)
Traceback (most recent call last):
    ...
TypeError: miss default value


>>> mk_default__easy(-1, bad(111), mirror=True)
Traceback (most recent call last):
    ...
bad: 111
>>> mk_default__easy(0, bad, mirror=True)
Traceback (most recent call last):
    ...
bad
>>> mk_default__easy(1, bad, 111, mirror=True)
Traceback (most recent call last):
    ...
bad: 111


>>> mk_default__easy(-3- -1, bad(111))
Traceback (most recent call last):
    ...
bad: 111
>>> mk_default__easy(-3- 0, bad)
Traceback (most recent call last):
    ...
bad
>>> mk_default__easy(-3- 1, bad, 111)
Traceback (most recent call last):
    ...
bad: 111




#]]]doctest_examples:END

#'''
#]]]__doc__-end


__all__ = '''
    mk_fdefault
    mk_default
        eliminate_tmay__mix
        eliminate_tmay_or_raise__simple
    BasePermissionMappingOps
        SimplePermissionMappingOps
    XDefaultDict
        ops4XDefaultMapping







    mk_fdefaultP
    mk_fdefault
    mk_fdefaultP_from_default
    mk_fdefault_from_default

    Mk_fdefaultP
    Mk_fdefault
    Mk_fdefault1__caller_args_at_last
    Mk_fdefault1__caller_args_at_first
    Mk_fdefaultP_from_default
    Mk_fdefault_from_default

    mk_default2value__default_at_last
    mk_default2value__default_at_first
    mk_tmay_from_default2value
    mk_fvalue
    mk_tmay_from_is_safe_fvalue
    mk_tmay_from_try_fvalue
    mk_tmay_from_try_fvalue_KeyError



    mk_default__easy
        mk_default5zdefault
    mk_default_or_raise
        mirror_rank2imay_rank
        mk_default_or_raise__ver1
            mk_edefault__cased
            eliminate_cased_edefault__raise
        mk_default_or_raise__ver2
            reform_args_from_mk_default_or_raise
                raise4mk_default_or_raise
    mk_default

    eliminate_tmay
        eliminate_tmay__cased
        eliminate_tmay__mix
    eliminate_tmay_or_raise
        eliminate_tmay_or_raise__simple

    BasePermissionMappingOps
        MappingOpsPermission
        SimplePermissionMappingOps
        LazyValueCachedTransitionalObj

    XDefaultMappingOps
        ops4XDefaultMapping

    WeakableXDefaultDict
        XDefaultDict
            XDefaultHashMappingMixin
                XDefaultMappingMixin
                MappingMixin__auto_setdefault_via_slice4HashMap
    '''.split()#'''
__all__

from types import MappingProxyType
from seed.tiny_.check import check_type_is, check_imay, check_callable, check_pair, check_is_None
from seed.tiny_.verify import is_reiterable
from seed.tiny_.slice2triple import slice2triple
from seed.tiny_.Weakable import WeakableDict

class Mk_fdefaultP:
    r'''
    ========
    fdefault
        num_args4caller=0
    key2default
        num_args4caller=1
    mapping_key2default
        num_args4caller=2
    ========
    fvalue
        num_args4caller=0
        #see:mk_tmay_from_try_fvalue
    default2value
        num_args4caller=1
        #see:mk_tmay_from_default2value
    ========
    *args0, *args1
    vs
    *args1, *args0
    #'''
    def __init__(sf, args4caller_after_local_args:bool, num_args4caller, legal_keys4caller:'set<attr>', func, args:'seq', kwargs, /):
        if not type(args4caller_after_local_args) is bool: raise TypeError
        if not type(num_args4caller) is int: raise TypeError
        if legal_keys4caller is iter(legal_keys4caller): raise TypeError
        if not callable(func): raise TypeError
        if args is iter(args): raise TypeError
        if kwargs is iter(kwargs): raise TypeError
        #if not num_args4caller >= 0: raise ValueError
        sf.args4caller_after_local_args = args4caller_after_local_args
        sf.num_args4caller = num_args4caller
        sf.legal_keys4caller = legal_keys4caller
        sf.func = func
        sf.args = args
        sf.kwargs = kwargs
    def __call__(sf, /, *args4caller, **caller_kwargs):
        if len(args4caller) != sf.num_args4caller: raise TypeError
        if not caller_kwargs.keys() <= sf.legal_keys4caller: raise TypeError

        if sf.args4caller_after_local_args:
            return sf.func(*sf.args, *args4caller, **sf.kwargs, **caller_kwargs)
        else:
            return sf.func(*args4caller, *sf.args, **caller_kwargs, **sf.kwargs)

class Mk_fdefault(Mk_fdefaultP):
    'see: mk_fvalue, mk_tmay_from_try_fvalue, mk_tmay_from_try_fvalue_KeyError'
    args4caller_after_local_args = False
    num_args4caller = 0
    legal_keys4caller = frozenset()
    def __init__(sf, func, args, kwargs, /):
        #super().__init__(num_args4caller, legal_keys4caller, func, *args, **kwargs)
        sf.func = func
        sf.args = args
        sf.kwargs = kwargs
class Mk_fdefault1__caller_args_at_last(Mk_fdefault):
    'see: mk_default2value__default_at_last, mk_tmay_from_default2value'
    args4caller_after_local_args = True
    num_args4caller = 1
class Mk_fdefault1__caller_args_at_first(Mk_fdefault):
    'see: mk_default2value__default_at_first, mk_tmay_from_default2value'
    args4caller_after_local_args = False
    num_args4caller = 1
class Mk_fdefaultP_from_default(Mk_fdefaultP):
    args4caller_after_local_args = False
    args = ()
    kwargs = MappingProxyType({})
    def __init__(sf, num_args4caller, legal_keys4caller:'set<attr>', default, /):
        sf.num_args4caller = num_args4caller
        sf.legal_keys4caller = legal_keys4caller
        sf.default = default
    def func(sf, /, *args, **kwargs):
        return sf.default

class Mk_fdefault_from_default(Mk_fdefaultP_from_default, Mk_fdefault):
    def __init__(sf, default, /):
        sf.default = default


mk_fdefaultP_from_default = Mk_fdefaultP_from_default
mk_fdefault_from_default = Mk_fdefault_from_default



def mk_fdefaultP(args4caller_after_local_args, num_args4caller, legal_keys4caller:'set<attr>', func, /, *args, **kwargs):
    return Mk_fdefaultP(args4caller_after_local_args, num_args4caller, legal_keys4caller, func, args, kwargs)
def mk_fdefault(func, /, *args, **kwargs):
    return Mk_fdefault(func, args, kwargs)
mk_fvalue = mk_fdefault
def mk_default2value__default_at_last(func, /, *args, **kwargs):
    return Mk_fdefault1__caller_args_at_last(func, args, kwargs)
def mk_default2value__default_at_first(func, /, *args, **kwargs):
    return Mk_fdefault1__caller_args_at_first(func, args, kwargs)

def mk_tmay_from_is_safe_fvalue(is_safe, fvalue, /):
    if is_safe:
        value = fvalue()
        tmay = (value,)
    else:
        tmay = ()
    return tmay
def mk_tmay_from_try_fvalue(ErrorTree, fvalue, /):
    try:
        value = fvalue()
    except ErrorTree:
        tmay = ()
    else:
        tmay = (value,)
    return tmay
def mk_tmay_from_try_fvalue_KeyError(fvalue, /):
    return mk_tmay_from_try_fvalue(KeyError, fvalue)
def mk_tmay_from_default2value(default2value, /):
    Nothing = object()
    nmay = default2value(Nothing)
    if nmay is Nothing:
        tmay = ()
    else:
        value = nmay
        tmay = (value,)
    return tmay

def mirror_rank2imay_rank(mirror, mirror_imay_xedefault_rank, /):
    #def mirror4imay_xdefault_rank(mirror, mirror_imay_xedefault_rank, /):
    '-> (mirrored, imay_xedefault_rank)'
    check_type_is(int, mirror_imay_xedefault_rank)
    if -1 <= mirror_imay_xedefault_rank:
        imay_xedefault_rank = mirror_imay_xedefault_rank
        mirrored = bool(mirror)
    else:
        imay_xedefault_rank = -3 - mirror_imay_xedefault_rank
        mirrored = not mirror
    del mirror
    return (mirrored, imay_xedefault_rank)
def mk_edefault__cased(mirror_imay_xedefault_rank, xedefault, /, *args4xedefault, mirror:bool):
    '-> (is_exception, default_or_exception)'
    'xxx -> (is_default, default_or_exception)'
    (mirrored, imay_xedefault_rank) = mirror_rank2imay_rank(mirror, mirror_imay_xedefault_rank)
    del mirror, mirror_imay_xedefault_rank
    is_exception = mirrored
    default_or_exception = mk_default(imay_xedefault_rank, xedefault, *args4xedefault)
    return (is_exception, default_or_exception)
def eliminate_cased_edefault__raise (is_exception, default_or_exception, /):
    '-> default|raise exception'
    if not is_exception:
        default = default_or_exception
        return default
    exception = default_or_exception
    raise exception
#def mk_default_or_mk_exception_then_raise(mirror_imay_xedefault_rank, xedefault, /, *args4xedefault, mirror:bool):
def mk_default_or_raise__ver1(mirror_imay_xedefault_rank, xedefault, /, *args4xedefault, mirror:bool):
    '-> default|raise exception'
    (is_exception, default_or_exception) = mk_edefault__cased(mirror_imay_xedefault_rank, xedefault, *args4xedefault, mirror=mirror)
    default = eliminate_cased_edefault__raise(is_exception, default_or_exception)
    return default

def raise4mk_default_or_raise(imay_xedefault_rank, xedefault, /, *args4xedefault):
    exception = mk_default(imay_xedefault_rank, xedefault, *args4xedefault)
    raise exception
def reform_args_from_mk_default_or_raise(mirror_imay_xedefault_rank, xedefault, /, *args4xedefault, mirror:bool):
    '-> (imay_xdefault_rank, xdefault, args4xdefault)'
    (mirrored, imay_xedefault_rank) = mirror_rank2imay_rank(mirror, mirror_imay_xedefault_rank)
    del mirror, mirror_imay_xedefault_rank
    is_exception = mirrored
    if is_exception:
        args4xdefault = (imay_xedefault_rank, xedefault, *args4xedefault)
        imay_xdefault_rank = len(args4xdefault)
        xdefault = raise4mk_default_or_raise
    else:
        args4xdefault = args4xedefault
        imay_xdefault_rank = imay_xedefault_rank
        xdefault = xedefault
    del imay_xedefault_rank, xedefault, args4xedefault
    return (imay_xdefault_rank, xdefault, args4xdefault)


def mk_default_or_raise__ver2(mirror_imay_xedefault_rank, xedefault, /, *args4xedefault, mirror:bool):
    (imay_xdefault_rank, xdefault, args4xdefault) = reform_args_from_mk_default_or_raise(mirror_imay_xedefault_rank, xedefault, *args4xedefault, mirror=mirror)
    #del imay_xedefault_rank, xedefault, args4xedefault, mirror
    #e ../../python3_src/seed/pkg_tools/_forgot_import.py
    del mirror_imay_xedefault_rank, xedefault, args4xedefault, mirror
    default = mk_default(imay_xdefault_rank, xdefault, *args4xdefault)#may raise
    return default
if 0:
    del _222222222222222222222222222222222
    def ___x(_y,/):
        # e ../../python3_src/seed/pkg_tools/_forgot_import.py
        _000000000000000000000000000000000
        _zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
        _111111111111111111111111111111111 = 1
        def __f():
            _111111111111111111111111111111111
        del _33333333333333333333333333333333
mk_default_or_raise = mk_default_or_raise__ver1
mk_default_or_raise = mk_default_or_raise__ver2
def mk_default(imay_xdefault_rank, xdefault, /, *args4xdefault):
    r'''
    args4xdefault = [..., z, y, x]
    imay_xdefault_rank :: [-1..len(args4xdefault)]
    xdefault = [default, fdefault, x2default, y_x2default, z_y_x2defaulta, ...].__getitem__(1+imay_xdefault_rank)
    #'''
    #check_imay(imay_xdefault_rank)
    check_type_is(int, imay_xdefault_rank)
    if not -1 <= imay_xdefault_rank <= len(args4xdefault): raise TypeError#ValueError
    if imay_xdefault_rank == -1:
        default = xdefault
    else:
        args2default = xdefault
        L = xdefault_rank = imay_xdefault_rank
        args = args4xdefault[len(args4xdefault)-L:]
        assert len(args) == L
        default = args2default(*args)
    return default
def mk_default__easy(*tmay_Nothing___or___args4mk_default_or_raise, mirror=False):
    L = len(tmay_Nothing___or___args4mk_default_or_raise)

    if L == 0:
        [] = tmay_Nothing = tmay_Nothing___or___args4mk_default_or_raise
        raise TypeError('miss default value')
    elif L == 1:
        [Nothing] = tmay_Nothing = tmay_Nothing___or___args4mk_default_or_raise
        if mirror:
            exception = Nothing
            raise exception
        default = Nothing
    else:
        (mirror_imay_xedefault_rank, xedefault, *args4xedefault) = args4mk_default = tmay_Nothing___or___args4mk_default_or_raise
        default = mk_default_or_raise(mirror_imay_xedefault_rank, xedefault, *args4xedefault, mirror=mirror)
    default
    return default
mk_default5zdefault = mk_default__easy
from seed.tiny_.mk_fdefault import mk_default__easy, mk_default, raise4mk_default_or_raise, mk_default_or_raise
    #def mk_default_or_raise(mirror_imay_xedefault_rank, xedefault, /, *args4xedefault, mirror:bool):
    #   imay_xdefault_ranks = (-3)-mirror_imay_xedefault_rank if mirror_imay_xedefault_rank < -1 else mirror_imay_xedefault_rank
    #   mirrored = (mirror_imay_xedefault_rank < -1) ^ bool(mirror)
    #
    #def raise4mk_default_or_raise(imay_xedefault_rank, xedefault, /, *args4xedefault):
    #def mk_default(imay_xdefault_rank, xdefault, /, *args4xdefault):
    #def mk_default__easy(*tmay_Nothing___or___args4mk_default_or_raise, mirror=False):




# zzz-elimination-rule vs zzz-introduction-rule (above mk_tmay_from_...)
def eliminate_tmay__cased(tmay_value, imay_xdefault_rank, xdefault, /, *args4xdefault):
    'see:mk_default; -> (is_value, default_or_value)'
    (is_value, default_or_value) = eliminate_tmay(tmay_value, imay_xdefault_rank, xdefault, *args4xdefault, mix=False)
    return (is_value, default_or_value)

def eliminate_tmay__mix(tmay_value, imay_xdefault_rank, xdefault, /, *args4xdefault):
    'see:mk_default; -> default_or_value'
    default_or_value = eliminate_tmay(tmay_value, imay_xdefault_rank, xdefault, *args4xdefault, mix=True)
    return default_or_value

def eliminate_tmay(tmay_value, imay_xdefault_rank, xdefault, /, *args4xdefault, mix:bool):
    'see:mk_default; -> default_or_value if mix else (is_value, default_or_value)'
    check_type_is(tuple, tmay_value)
    if tmay_value:
        [value] = tmay_value
        default_or_value = value
    else:
        default = mk_default(imay_xdefault_rank, xdefault, *args4xdefault)
        default_or_value = default
    if mix:
        return default_or_value
    is_value = bool(tmay_value)
    return (is_value, default_or_value)




def eliminate_tmay_or_raise__simple(tmay_value, imay_xexception_rank, xexception, /, *args4xexception):
    check_imay(imay_xexception_rank)
    value = eliminate_tmay_or_raise(tmay_value, imay_xexception_rank, xexception, mix=True, mirror=True)#may raise
    return value
def eliminate_tmay_or_raise(tmay_value, mirror_imay_xedefault_rank, xedefault, /, *args4xedefault, mix:bool, mirror:bool):
    'see:mk_default_or_raise; -> (default_or_value if mix else (is_value, default_or_value)) | raise exception'
    (imay_xdefault_rank, xdefault, args4xdefault) = reform_args_from_mk_default_or_raise(mirror_imay_xedefault_rank, xedefault, *args4xedefault, mirror=mirror)
    del mirror_imay_xedefault_rank, xedefault, args4xedefault, mirror
    return eliminate_tmay(tmay_value, imay_xdefault_rank, xdefault, *args4xdefault, mix=mix)#may raise



class _helper4MappingOpsPermission:
    class _NS:pass
    @classmethod
    def init_section(cls, ns4out, offset, section, /):
        #why named bit_name?
        #   each one introduct a new bit/alloc 1 bit
        idx2bit_names = tuple(section.content.split())
        if len({*idx2bit_names}) != len(idx2bit_names): raise ValueError('duplicated')
        section._content__idx2bit_names_ = idx2bit_names

        #section2bit_names = gettattr(section, 'required', {})
        section2bit_names = section.required
        for _section, _bit_names in [*section2bit_names.items()]:
            section2bit_names[_section] = frozenset(_bit_names.split())
        section._required__section2bit_names_ = section2bit_names

        required_permission__int_flag = 0
        for _section, _bit_names in section2bit_names.items():
            _ns = _section._ns__permissions_
            for _bit_name in _bit_names:
                required_permission__int_flag |= getattr(_ns, _bit_name)
        section._required_permission__int_flag_ = required_permission__int_flag

        ns = section._ns__permissions_ = cls._NS()
        for offset, bit_name in enumerate(idx2bit_names, offset):
            permission__bit = 1 << offset
                #why named bit_name?
                #   each one introduct a new bit/alloc 1 bit
            permission__int_flag = permission__bit | required_permission__int_flag
            setattr(ns, bit_name, permission__int_flag)
            if hasattr(ns4out, bit_name): raise ValueError('duplicated')
            setattr(ns4out, bit_name, permission__int_flag)



    @classmethod
    def section2size(cls, section, /):
        return len(section._content__idx2bit_names_)

    @classmethod
    def init_ordered_sections(cls, offset, /, *sections):
        ns4out = cls._NS()
        for section in sections:
            cls.init_section(ns4out, offset, section)
            sz = cls.section2size(section)
            offset += sz
        return ns4out

    @classmethod
    def build_permission4primitive_ops(cls, /, *, _detect_, _get__value_, _set__new_, _set__overwrite_, _delete_, **kwargs):
        d0 = 1; d0 = {**locals()}
        detect = _detect_
        get__tmay = _detect_ | _get__value_
        set__new_or_overwrite = _set__new_ | _set__overwrite_
        detect_set__new_or_pass = _detect_ | _set__new_
        detect_set__overwrite_or_pass = _detect_ | _set__overwrite_
        drop__delete_or_pass = _delete_
        d1 = {**locals()}
        d = {k:v for k, v in d1.items() if k  not in d0}
        assert len(d) == 6
        return d


    @classmethod
    def build_permission4composite_ops(cls, /, *, detect, get__tmay, set__new_or_overwrite, detect_set__new_or_pass, detect_set__overwrite_or_pass, drop__delete_or_pass, **kwargs):
        d0 = 1; d0 = {**locals()}
        get__raise = get__tmay
        detect_set__new_or_raise = detect_set__new_or_pass
        detect_set__overwrite_or_raise = detect_set__overwrite_or_pass
        detect_set__new_or_overwrite = detect_set__new_or_pass | detect_set__overwrite_or_raise   |    detect | set__new_or_overwrite
        get_set__overwrite = get__raise | detect_set__overwrite_or_raise
        get_set__new_or_overwrite = get__tmay | detect_set__new_or_raise | detect_set__overwrite_or_raise    |    get__tmay | set__new_or_overwrite
        detect_drop__delete_or_pass = detect | drop__delete_or_pass
        detect_drop__delete_or_raise = detect_drop__delete_or_pass
        get_drop__delete_or_pass = get__tmay | drop__delete_or_pass
        get_drop__delete_or_raise = get_drop__delete_or_pass
        alter__drop_or_set = set__new_or_overwrite | drop__delete_or_pass
        detect_alter__drop_or_set = detect_drop__delete_or_pass | detect_set__new_or_overwrite
        get_alter__drop_or_set = get_drop__delete_or_pass | get_set__new_or_overwrite
        d1 = {**locals()}
        d = {k:v for k, v in d1.items() if k  not in d0}
        assert len(d) == 13
        return d


def _mk4MappingOpsPermission():
    d0 = 1; d0 = {**locals()}
    class _basic_section_:
        content = '_basic_read_ _basic_write_'
        required = {}
    class _read_section_:
        content = '_detect_ _get__view_ _get__value_'
        required = {_basic_section_:'_basic_read_'}
    class _write_section_:
        content = '_set__new_ _set__overwrite_ _delete_'
        required = {_basic_section_:'_basic_write_'}
    class _read_write_section_:
        content = '_emplace_modify_ _iassign_modify_'
        #??? <==> _get__value_
        # like _get__view_, only selected action can be apply to the value
        #??? required _read_section_:'_get__view_' ??? no! eg. apply inc()/succ() on integer...
        required = {_basic_section_:'_basic_read_ _basic_write_'}

    _sections_ = (_basic_section_, _read_section_, _write_section_, _read_write_section_)

    _ns__prime_bits_ = _helper4MappingOpsPermission.init_ordered_sections(0, *_sections_)

    _dict__primitive_ops_permission__int_flags_ = _helper4MappingOpsPermission.build_permission4primitive_ops(**_ns__prime_bits_.__dict__)
    _dict__composite_ops_permission__int_flags_ = _helper4MappingOpsPermission.build_permission4composite_ops(**_dict__primitive_ops_permission__int_flags_)
    class _ns__primitive_ops_permission__int_flags_:
        locals().update(_dict__primitive_ops_permission__int_flags_)
    class _ns__composite_ops_permission__int_flags_:
        locals().update(_dict__composite_ops_permission__int_flags_)
    d1 = {**locals()}
    d = {k:v for k, v in d1.items() if k  not in d0}
    assert len(d) == 10
    return d

class MappingOpsPermission:
    locals().update(_mk4MappingOpsPermission())
    if 0:
        _ns__primitive_ops_permission__int_flags_ = _ns__primitive_ops_permission__int_flags_
        _ns__composite_ops_permission__int_flags_ = _ns__composite_ops_permission__int_flags_

    if 1:
        _ = _ns__primitive_ops_permission__int_flags_
        detect = _.detect
        get__tmay = _.get__tmay
        set__new_or_overwrite = _.set__new_or_overwrite
        detect_set__new_or_pass = _.detect_set__new_or_pass
        detect_set__overwrite_or_pass = _.detect_set__overwrite_or_pass
        drop__delete_or_pass = _.drop__delete_or_pass
        del _

    if 1:
        _ = _ns__composite_ops_permission__int_flags_
        #.,.+14s/ *\(\w*\) = _.
        get__raise = _.get__raise
        detect_set__new_or_raise = _.detect_set__new_or_raise
        detect_set__overwrite_or_raise = _.detect_set__overwrite_or_raise
        detect_set__new_or_overwrite = _.detect_set__new_or_overwrite
        get_set__overwrite = _.get_set__overwrite
        get_set__new_or_overwrite = _.get_set__new_or_overwrite
        detect_drop__delete_or_pass = _.detect_drop__delete_or_pass
        detect_drop__delete_or_raise = _.detect_drop__delete_or_raise
        get_drop__delete_or_pass = _.get_drop__delete_or_pass
        get_drop__delete_or_raise = _.get_drop__delete_or_raise
        alter__drop_or_set = _.alter__drop_or_set
        detect_alter__drop_or_set = _.detect_alter__drop_or_set
        get_alter__drop_or_set = _.get_alter__drop_or_set
        del _

class BasePermissionMappingOps:
    r'''
    see:
        view ../../python3_src/seed/types/OpaqueInstanceStorage.py
        detect = 0b01
        get__tmay = 0b11
        set__new_or_overwrite = 0b11_1_00
        detect_set__new_or_pass = 0b01_1_01
        detect_set__overwrite_or_pass = 0b10_1_01
        drop__delete_or_pass = 0b100_1_00
    why lazy?
        why lazy_new_value not new_value? to check permission before eval
        why lazy_tmay_lazy_new_value not tmay_new_value? to check permission before eval

    #'''
    __slots__ = ()
    def get_permission_at(ops, d, key, /):
        '-> permission__int_flag; #see:MappingOpsPermission'
        return 0 #forbidden all ops
    def acquire_permission(ops, d, key, permission__int_flag, /):
        '-> None|raise PermissionError; #see:MappingOpsPermission'
        _permission__int_flag = ops.get_permission_at(d, key)
        if not permission__int_flag == (permission__int_flag & _permission__int_flag): raise PermissionError
        return
    def check_permission(ops, d, key, action_name__main, /, *action_names__depended):

        f = lambda action_name,/:ops.acquire_permission(d, key, getattr(MappingOpsPermission, action_name))
        f(action_name__main)
        for action_name in action_names__depended:
            f(action_name)
        return
    #primitive-public-API:
    def detect(ops, d, key, /):
        '-> old_value_exists:bool'
        ops.check_permission(d, key, 'detect')
        ops.acquire_permission(d, key, MappingOpsPermission.detect)
        return ops._detect_(d, key)
    def get__tmay(ops, d, key, /):
        '-> tmay_old_value'
        ops.check_permission(d, key, 'get__tmay', 'detect')
        ops.acquire_permission(d, key, MappingOpsPermission.get__tmay)
        return ops._get__tmay_(d, key)
    def set__new_or_overwrite(ops, d, key, lazy_new_value, /):
        'lazy_new_value -> new_value #may raise PermissionError before eval'
        ops.check_permission(d, key, 'set__new_or_overwrite')
        ops.acquire_permission(d, key, MappingOpsPermission.set__new_or_overwrite)
        return ops._set__new_or_overwrite_(d, key, lazy_new_value)
    def detect_set__new_or_pass(ops, d, key, lazy_new_value, /):
        'lazy_new_value -> tmay_new_value'
        ops.check_permission(d, key, 'detect_set__new_or_pass', 'detect')
        ops.acquire_permission(d, key, MappingOpsPermission.detect_set__new_or_pass)
        return ops._detect_set__new_or_pass_(d, key, lazy_new_value)
    def detect_set__overwrite_or_pass(ops, d, key, lazy_new_value, /):
        'lazy_new_value -> tmay_new_value'
        ops.check_permission(d, key, 'detect_set__overwrite_or_pass', 'detect')
        ops.acquire_permission(d, key, MappingOpsPermission.detect_set__overwrite_or_pass)
        return ops._detect_set__overwrite_or_pass_(d, key, lazy_new_value)
    def drop__delete_or_pass(ops, d, key, /):
        '-> None'
        ops.check_permission(d, key, 'drop__delete_or_pass')
        ops.acquire_permission(d, key, MappingOpsPermission.drop__delete_or_pass)
        return ops._drop__delete_or_pass_(d, key)

    #primitive-protected-API:#for override
    def _000___get__old_or_undefined___000_(ops, d, key, /):
        old_value = d[key]
        return old_value
    def _000___set__new_or_overwrite___000_(ops, d, key, new_value, /):
        d[key] = new_value
        return
    def _000___set__new_or_undefined___000_(ops, d, key, new_value, /):
        d[key] = new_value
        return
    def _000___set__overwrite_or_undefined___000_(ops, d, key, new_value, /):
        d[key] = new_value
        return
    def _000___drop__delete_or_undefined___000_(ops, d, key, /):
        del d[key]
        return
    def _000___detect___000_(ops, d, key, /):
        return key in d

    def _detect_(ops, d, key, /):
        old_value_exists = ops._000___detect___000_(d, key)
        check_type_is(bool, old_value_exists)
        return old_value_exists
    def _get__tmay_(ops, d, key, /):
        if not ops.detect(d, key):
            #not exist
            return ()
        #old_value = d[key]
        old_value = ops._000___get__old_or_undefined___000_(d, key)
        return (old_value,)
    def _set__new_or_overwrite_(ops, d, key, lazy_new_value, /):
        new_value = lazy_new_value()
        #d[key] = new_value
        ops._000___set__new_or_overwrite___000_(d, key, new_value)
        return new_value
    def _detect_set__new_or_pass_(ops, d, key, lazy_new_value, /):
        if ops.detect(d, key):
            #exist
            return ()
        new_value = lazy_new_value()
        #d[key] = new_value
        ops._000___set__new_or_undefined___000_(d, key, new_value)
        return (new_value,)
    def _detect_set__overwrite_or_pass_(ops, d, key, lazy_new_value, /):
        if not ops.detect(d, key):
            #not exist
            return ()
        new_value = lazy_new_value()
        #d[key] = new_value
        ops._000___set__overwrite_or_undefined___000_(d, key, new_value)
        return (new_value,)
    def _drop__delete_or_pass_(ops, d, key, /):
        # d.pop(key)
        #bug: if ops.detect(d, key):
        if ops._000___detect___000_(d, key):
        #if key in d:
            #exist
            #del d[key]
            ops._000___drop__delete_or_undefined___000_(d, key)
        return None

    #composite:TODO
    #composite-public-API:
    r'''
    ----
    ----
    ----total 13:
    get__raise
        get__tmay
    detect_set__new_or_raise
        detect_set__new_or_pass
    detect_set__overwrite_or_raise
        detect_set__overwrite_or_pass
    detect_set__new_or_overwrite
        detect_set__new_or_pass+detect_set__overwrite_or_raise
        vs detect+set__new_or_overwrite
    get_set__overwrite
        get__raise
        detect_set__overwrite_or_raise
    get_set__new_or_overwrite
        get__tmay+detect_set__new_or_raise+detect_set__overwrite_or_raise
        vs get__tmay+set__new_or_overwrite
    detect_drop__delete_or_pass
        detect
        drop__delete_or_pass
    detect_drop__delete_or_raise
        detect_drop__delete_or_pass
    get_drop__delete_or_pass
        get__tmay
        drop__delete_or_pass
    get_drop__delete_or_raise
        get_drop__delete_or_pass
    alter__drop_or_set
        set__new_or_overwrite
        drop__delete_or_pass
    detect_alter__drop_or_set
        detect_drop__delete_or_pass # ()
        detect_set__new_or_overwrite # (exist2new_value,)
    get_alter__drop_or_set
        get_drop__delete_or_pass # ()
        get_set__new_or_overwrite # (tmay_old_value2new_value,)
    uniform_read
        ---depend on read_fmt
        get__tmay
    uniform_update
        ---depend on update_fmt
        set__new_or_overwrite
        drop__delete_or_pass
    uniform_read_calc_update
        ---depend on read_fmt/update_fmt
        get__tmay
        set__new_or_overwrite
        drop__delete_or_pass
    ----
    ----
    ----
    get__raise
        'lazy_KeyNotFoundError -> old_value|KeyNotFoundError<:KeyError'
    detect_set__new_or_raise
        'lazy_new_value -> lazy_KeyExistsError -> new_value|KeyExistsError<:KeyError'
    detect_set__overwrite_or_raise
        'lazy_new_value -> lazy_KeyNotFoundError -> new_value|KeyNotFoundError<:KeyError'
    detect_set__new_or_overwrite
        'exist2new_value -> (old_value_exists, new_value)'
    get_set__overwrite
        'old_value2new_value -> lazy_KeyNotFoundError -> (old_value, new_value)|KeyNotFoundError<:KeyError'
    get_set__new_or_overwrite
        'tmay_old_value2new_value -> (tmay_old_value, new_value)'
    detect_drop__delete_or_pass
        '-> old_value_exists'
    detect_drop__delete_or_raise
        'lazy_KeyNotFoundError -> None|KeyNotFoundError<:KeyError'
    get_drop__delete_or_pass
        '-> tmay_old_value'
    get_drop__delete_or_raise
        'lazy_KeyNotFoundError -> old_value|KeyNotFoundError<:KeyError'
    alter__drop_or_set
        'lazy_tmay_lazy_new_value -> tmay_new_value'
    detect_alter__drop_or_set
        'lazy_tmay__exist2new_value -> (old_value_exists, tmay_new_value)'
    get_alter__drop_or_set
        'lazy_tmay__tmay_old_value2new_value -> (tmay_old_value, tmay_new_value)'
    uniform_read
        '{read_fmt} -> (read_fmt, read_output)'
    uniform_update
        '{update_fmt} -> (()->(update_fmt, update_input)) -> (update_fmt, update_input)'
    uniform_read_calc_update
        '{read_fmt} -> {update_fmt} -> ((read_fmt, read_output) -> (update_fmt, update_input)) -> ((read_fmt, read_output), (update_fmt, update_input))'
    ----
    ----
    ----
    -----
    read_then_update :: permission__int_flag -> mapping -> key -> (?rc:read_case, payload<rc>) -> {(?uc:update_case, payload<uc>)} -> ((?rc:read_case, payload<c>, extracted_info<rc, payload<rc> >)->(?uc:update_case, payload<uc>, evaled_info4update<uc, payload<uc> >)) -> ((?rc:read_case, payload<c>, extracted_info<rc, payload<rc> >), (?uc:update_case, payload<uc>, evaled_info4update<uc, payload<uc> >))
    read_then_update :: permission__int_flag -> mapping -> key -> read_fmt -> {update_fmt} -> ((read_fmt, extracted_info<read_fmt>)->(update_fmt, evaled_info4update<update_fmt>)) -> ((read_fmt, extracted_info<read_fmt>), (update_fmt, evaled_info4update<update_fmt>))
    read_fmt:
        False/None??/0??/()??/''??: no _basic_read_
            extracted_info<False> = None
        bool: _detect_
            extracted_info<bool> = old_value_exists :: bool
        object: _get__value_
            extracted_info<object> = tmay_old_value
        (Ellipsis, read_func, *args): _get__view_
            extracted_info<object> = tmay (read_func<args>(old_value))
    update_fmt:
        ...
    -----
    read_phase:: any one of below
        (0, None) -> None # no _basic_read_
        (1, None) -> old_value_exists # _detect_
        (2, [permitted_read_action<the_stored_obj>], args) -> [extracted_info] # _get__view_ # eg. len, further getitem<key-path>
        (3, None) -> the_stored_obj# _get__value_
        #(4, permitted_read_action<attached-control-info>) -> the_stored_obj# _get__value_
    update_phase: subset of below
        (0, None) -> None #no _basic_write_
        (1, None) -> None # _delete_
        (2, obj4new) -> None # _detect_+_set__new_
        (3, obj4overwrite) -> None # _detect_+_set__overwrite_
        (4, obj4set) -> None # _set__new_+_set__overwrite_
        (5, obj4set, [(permitted_cmp_check, args)]) -> None # _get__view_+_set__new_+_set__overwrite_
            permitted_cmp_check<args> :: tmay_old_value -> new_value -> bool
        (6, permitted_modify_action<the_stored_obj>, args) -> extracted_info # _emplace_modify_ # eg. further setitem<key-path>
    -----
    -----
    #'''
    def get__raise(ops, d, key, lazy_KeyNotFoundError, /):
        'lazy_KeyNotFoundError -> old_value|KeyNotFoundError<:KeyError'
        #neednot check
        #get__tmay
        tmay_old_value = ops.get__tmay(d, key)
        old_value = eliminate_tmay_or_raise__simple(tmay_old_value, 0, lazy_KeyNotFoundError)
        return old_value
    def detect_set__new_or_raise(ops, d, key, lazy_new_value, lazy_KeyExistsError, /):
        'lazy_new_value -> lazy_KeyExistsError -> new_value|KeyExistsError<:KeyError'
        #neednot check
        #detect_set__new_or_pass
        tmay_new_value = ops.detect_set__new_or_pass(d, key, lazy_new_value)
        new_value = eliminate_tmay_or_raise__simple(tmay_new_value, 0, lazy_KeyExistsError)
        return new_value
    def detect_set__overwrite_or_raise(ops, d, key, lazy_new_value, lazy_KeyNotFoundError, /):
        'lazy_new_value -> lazy_KeyNotFoundError -> new_value|KeyNotFoundError<:KeyError'
        #neednot check
        #detect_set__overwrite_or_pass
        tmay_new_value = ops.detect_set__overwrite_or_pass(d, key, lazy_new_value)
        new_value = eliminate_tmay_or_raise__simple(tmay_new_value, 0, lazy_KeyNotFoundError)
        return new_value
    def detect_set__new_or_overwrite(ops, d, key, exist2new_value, /):
        'exist2new_value -> (old_value_exists, new_value)'
        #check
        ops.check_permission(d, key, 'detect_set__new_or_overwrite', 'detect', 'set__new_or_overwrite')
        #detect_set__new_or_pass+detect_set__overwrite_or_raise
        #vs detect+set__new_or_overwrite
        #why lazy_new_value not new_value? to check permission before eval
        #why not detect+set__new_or_overwrite? ????since exist2new_value not lazy_new_value????
        lazy_old_value_exists = lambda:ops.detect(d, key)
        (old_value_exists, new_value) = _update_checked_before_read(lazy_old_value_exists, exist2new_value, ops.set__new_or_overwrite, d, key)
        return (old_value_exists, new_value)
        exist2new_value
        lazy_new_value = LazyValueCachedTransitionalObj(exist2new_value, lazy_old_value_exists)
        _new_value = ops.set__new_or_overwrite(d, key, lazy_new_value)
        [(old_value_exists, new_value)] = lazy_new_value.tmay_pair
        assert _new_value is new_value
        return (old_value_exists, new_value)
    def get_set__overwrite(ops, d, key, old_value2new_value, lazy_KeyNotFoundError, /):
        'old_value2new_value -> lazy_KeyNotFoundError -> (old_value, new_value)|KeyNotFoundError<:KeyError'
        #check
        ops.check_permission(d, key, 'get_set__overwrite', 'get__raise', 'detect_set__overwrite_or_raise')
        #get__raise
        #detect_set__overwrite_or_raise
        #neednot _set__new_
        #lazy_new_value = lambda:old_value2new_value(ops.get__raise(d, key, lazy_KeyNotFoundError))
        lazy_old_value = lambda:ops.get__raise(d, key, lazy_KeyNotFoundError)
        (old_value, new_value) = _update_checked_before_read(lazy_old_value, old_value2new_value, ops.detect_set__overwrite_or_raise, d, key)
        return (old_value, new_value)
    def get_set__new_or_overwrite(ops, d, key, tmay_old_value2new_value, /):
        'tmay_old_value2new_value -> (tmay_old_value, new_value)'
        #check
        ops.check_permission(d, key, 'get_set__new_or_overwrite', 'get__tmay', 'set__new_or_overwrite')
        #get__tmay+detect_set__new_or_raise+detect_set__overwrite_or_raise
        #vs get__tmay+set__new_or_overwrite
        #why not get__tmay+set__new_or_overwrite? ????since tmay_old_value2new_value not lazy_new_value????
        lazy_tmay_old_value = lambda:ops.get__tmay(d, key)
        (tmay_old_value, new_value) = _update_checked_before_read(lazy_tmay_old_value, tmay_old_value2new_value, ops.set__new_or_overwrite, d, key)
        return (tmay_old_value, new_value)
    def detect_drop__delete_or_pass(ops, d, key, /):
        '-> old_value_exists'
        #check
        ops.check_permission(d, key, 'detect_drop__delete_or_pass', 'detect', 'drop__delete_or_pass')
        #detect
        #drop__delete_or_pass
        #bug:old_value_exists = _noreturn_update_checked_before_read(ops.detect, ops.drop__delete_or_pass, d, key)
        old_value_exists = ops.detect(d, key)
        ops.drop__delete_or_pass(d, key)
        return old_value_exists
    def detect_drop__delete_or_raise(ops, d, key, lazy_KeyNotFoundError, /):
        'lazy_KeyNotFoundError -> None|KeyNotFoundError<:KeyError'
        #neednot check
        #detect_drop__delete_or_pass
        old_value_exists = ops.detect_drop__delete_or_pass(d, key)
        if not old_value_exists: raise lazy_KeyNotFoundError()
        return None
    def get_drop__delete_or_pass(ops, d, key, /):
        '-> tmay_old_value'
        #check
        ops.check_permission(d, key, 'get_drop__delete_or_pass', 'get__tmay', 'drop__delete_or_pass')
        #get__tmay
        #drop__delete_or_pass
        tmay_old_value = ops.get__tmay(d, key)
        ops.drop__delete_or_pass(d, key)
        return tmay_old_value
    def get_drop__delete_or_raise(ops, d, key, lazy_KeyNotFoundError, /):
        'lazy_KeyNotFoundError -> old_value|KeyNotFoundError<:KeyError'
        #neednot check
        #get_drop__delete_or_pass
        tmay_old_value = ops.get_drop__delete_or_pass(d, key)
        if not tmay_old_value: raise lazy_KeyNotFoundError()
        [old_value] = tmay_old_value
        return old_value
    def alter__drop_or_set(ops, d, key, lazy_tmay_lazy_new_value, /):
        'lazy_tmay_lazy_new_value -> tmay_new_value'
        #check
        ops.check_permission(d, key, 'alter__drop_or_set', 'set__new_or_overwrite', 'drop__delete_or_pass')
        #why lazy_tmay_lazy_new_value not tmay_new_value? to check permission before eval
        #set__new_or_overwrite
        #drop__delete_or_pass
        tmay_lazy_new_value = lazy_tmay_lazy_new_value()
        if tmay_lazy_new_value:
            #set
            [lazy_new_value] = tmay_lazy_new_value
            new_value = ops.set__new_or_overwrite(d, key, lazy_new_value)
            tmay_new_value = (new_value,)
        else:
            #del
            ops.drop__delete_or_pass(d, key)
            tmay_new_value = ()
        return tmay_new_value
    def detect_alter__drop_or_set(ops, d, key, lazy_tmay__exist2new_value, /):
        'lazy_tmay__exist2new_value -> (old_value_exists, tmay_new_value)'
        #check
        ops.check_permission(d, key, 'detect_alter__drop_or_set', 'detect_drop__delete_or_pass', 'detect_set__new_or_overwrite')
        #detect_drop__delete_or_pass # ()
        #detect_set__new_or_overwrite # (exist2new_value,)
        tmay__exist2new_value = lazy_tmay__exist2new_value()
        if tmay__exist2new_value:
            #set
            [exist2new_value] = tmay__exist2new_value
            (old_value_exists, new_value) = ops.detect_set__new_or_overwrite(d, key, exist2new_value)
            tmay_new_value = (new_value,)
        else:
            #del
            old_value_exists = ops.detect_drop__delete_or_pass(d, key)
            tmay_new_value = ()
        return (old_value_exists, tmay_new_value)

    def get_alter__drop_or_set(ops, d, key, lazy_tmay__tmay_old_value2new_value, /):
        'lazy_tmay__tmay_old_value2new_value -> (tmay_old_value, tmay_new_value)'
        #check
        ops.check_permission(d, key, 'get_alter__drop_or_set', 'get_drop__delete_or_pass', 'get_drop__delete_or_pass')
        #get_drop__delete_or_pass # ()
        #get_set__new_or_overwrite # (tmay_old_value2new_value,)
        tmay__tmay_old_value2new_value = lazy_tmay__tmay_old_value2new_value()
        if tmay__tmay_old_value2new_value:
            #set
            [tmay_old_value2new_value] = tmay__tmay_old_value2new_value
            (tmay_old_value, new_value) = ops.get_set__new_or_overwrite(d, key, tmay_old_value2new_value)
            tmay_new_value = (new_value,)
        else:
            #del
            tmay_old_value = ops.get_drop__delete_or_pass(d, key)
            tmay_new_value = ()
        return (tmay_old_value, tmay_new_value)

    def is_permitted_read_fmt(ops, d, key, read_fmt, /):
        raise NotImplementedError
        return False
    def is_permitted_update_fmt(ops, d, key, update_fmt, /):
        raise NotImplementedError
        return False
    def _000___uniform_read___000_(ops, d, key, read_fmt, /):
        'read_fmt -> read_output'
        raise NotImplementedError
    def _000___uniform_update___000_(ops, d, key, update_fmt, update_input, /):
        'update_fmt -> update_input -> None'
        raise NotImplementedError

    def _uniform_read_(ops, d, key, acceptable_read_fmts, /):
        for read_fmt in acceptable_read_fmts:
            if ops.is_permitted_read_fmt(d, key, read_fmt): break
        else:
            raise logic-err
            raise PermissionError
        read_output = ops._000___uniform_read___000_(d, key, read_fmt)
        return (read_fmt, read_output)
    def _uniform_update_(ops, d, key, possible_update_fmts, lazy_cased_update_input, /):
        cased_update_input = lazy_cased_update_input()
        (update_fmt, update_input) = cased_update_input
        _ = ops._000___uniform_update___000_(d, key, update_fmt, update_input)
        check_is_None(_)
        return cased_update_input


    def check_permission4uniform_read(ops, d, key, acceptable_read_fmts, /):
        if not is_reiterable(acceptable_read_fmts): raise TypeError
        len(acceptable_read_fmts)
        if not any(ops.is_permitted_read_fmt(d, key, read_fmt) for read_fmt in acceptable_read_fmts): raise PermissionError
    def check_permission4uniform_update(ops, d, key, possible_update_fmts, /):
        if not is_reiterable(possible_update_fmts): raise TypeError
        len(possible_update_fmts)
        if not (len(possible_update_fmts) and all(ops.is_permitted_update_fmt(d, key, update_fmt) for update_fmt in possible_update_fmts)): raise PermissionError
    def uniform_read(ops, d, key, acceptable_read_fmts, /):
        '{read_fmt} -> (read_fmt, read_output)'
        #check
        ops.check_permission4uniform_read(d, key, acceptable_read_fmts)
        cased_read_output = ops._uniform_read_(d, key, acceptable_read_fmts)
        check_pair(cased_read_output)
        (read_fmt, read_output) = cased_read_output
        if not id(read_fmt) in list(map(id, acceptable_read_fmts)): raise TypeError
        return cased_read_output
    def uniform_update(ops, d, key, possible_update_fmts, lazy_cased_update_input, /):
        '{update_fmt} -> (()->(update_fmt, update_input)) -> (update_fmt, update_input)'
        #check
        ops.check_permission4uniform_update(d, key, possible_update_fmts)
        def _icheck(cased_update_input, /):
            check_pair(cased_update_input)
            (update_fmt, update_input) = cased_update_input
            if not id(update_fmt) in list(map(id, possible_update_fmts)): raise TypeError
            return cased_update_input
        _lazy_cased_update_input = LazyValueCachedTransitionalObj(_icheck, lazy_cased_update_input)
        cased_update_input = ops._uniform_update_(d, key, possible_update_fmts, _lazy_cased_update_input)
        if not cased_update_input is (_lazy_cased_update_input.tmay_pair[0][0]): raise logic-err
        return cased_update_input
    def uniform_read_calc_update(ops, d, key, acceptable_read_fmts, possible_update_fmts, cased_read_output2cased_update_input, /):
        '{read_fmt} -> {update_fmt} -> ((read_fmt, read_output) -> (update_fmt, update_input)) -> ((read_fmt, read_output), (update_fmt, update_input))'
        #check
        ops.check_permission4uniform_read(d, key, acceptable_read_fmts)
        ops.check_permission4uniform_update(d, key, possible_update_fmts)
        cased_read_output = ops.uniform_read(d, key, acceptable_read_fmts)
        cased_update_input = cased_read_output2cased_update_input(cased_read_output)
        _ = ops.uniform_update(d, key, possible_update_fmts, lambda:cased_update_input)
        check_is_None(_)
        return (cased_read_output, cased_update_input)
class SimplePermissionMappingOps(BasePermissionMappingOps):
    def __init__(sf, permission__int_flag, /):
        sf._p = permission__int_flag
    def get_permission_at(ops, d, key, /):
        '-> permission__int_flag; #see:MappingOpsPermission'
        return ops._p #irrelevance with d,key

class LazyValueCachedTransitionalObj:
    def __init__(sf, transitional_obj2output, lazy_transitional_obj, /):
        check_callable(transitional_obj2output)
        check_callable(lazy_transitional_obj)
        sf._f = transitional_obj2output
        sf._fv = lazy_transitional_obj
        sf._tm = ()
    def __call__(sf, /):
        if not sf._tm:
            t = sf._fv()
            o = sf._f(t)
            sf._tm = ((t,o),)
        [(transitional_obj, output)] = sf._tm
        return output
    @property
    def tmay_pair(sf, /):
        '-> tmay (transitional_obj, output)'
        return sf._tm
    r'''
    def __iter__(sf, /):
        'tuple(sf) = tmay (transitional_obj, output)'
        yield from sf._tm
    #'''

r'''bug: read after update ==>> read info after update, not after update-check
def _noreturn_update_checked_before_read(read, update, /, *args4update)
    _ = update(*args4update)
    check_is_None(_)
    return read()
#'''

def _update_checked_before_read(read, transform, update, /, *args4update):
    lazy_new_value = LazyValueCachedTransitionalObj(transform, read)
    _new_value = update(*args4update, lazy_new_value)
    [(transitional_obj, new_value)] = lazy_new_value.tmay_pair
    assert _new_value is new_value
    return (transitional_obj, new_value)
r'''
.+1,$s/get_/get__/g
.+1,$s/pop_/pop__/g
.+1,$s/set_/set__/g
#'''
class XDefaultMappingOps:
    r'''
    get__tmay
    pop__tmay

    get__xdefault
    pop__xdefault
    set__xdefault

    xxx__xdefault__mix
    xxx__xdefault__cased

    (imay_xdefault_rank, xdefault) >--> (mirror_imay_xedefault_rank, xedefault, /, *, mirror:bool):
    #'''
    __slots__ = ()
    def _000___detect___000_(ops, d, key, /):
        return key in d
    def _000___get__old_or_undefined___000_(ops, d, key, /):
        return d[key]
    def detect(ops, d, key, /):
        old_value_exists = ops._000___detect___000_(d, key)
        check_type_is(bool, old_value_exists)
        return old_value_exists
        return key in d
    def _000___drop__delete_or_undefined___000_(ops, d, key, /):
        del d[key]
        return
    def _000___set__new_or_undefined___000_(ops, d, key, new_value, /):
        d[key] = new_value
        return

    def get__tmay(ops, d, key, /):
        if not ops.detect(d, key):
            #not exist
            return ()
        #old_value = d[key]
        old_value = ops._000___get__old_or_undefined___000_(d, key)
        return (old_value,)
        if key in d:
            return (d[key],)
        return ()
    def pop__tmay(ops, d, key, /):
        # d.pop(key)
        tm = ops.get__tmay(d, key)
        if tm:
            #exist
            #del d[key]
            ops._000___drop__delete_or_undefined___000_(d, key)
        return tm

    def get__xedefault(ops, d, key, mirror_imay_xedefault_rank, xedefault, /, *, mix:bool, mirror:bool):
        tm = ops.get__tmay(d, key)
        return eliminate_tmay_or_raise(tm, mirror_imay_xedefault_rank, xedefault, d, key, mix=mix, mirror=mirror)
    def pop__xedefault(ops, d, key, mirror_imay_xedefault_rank, xedefault, /, *, mix:bool, mirror:bool):
        tm = ops.pop__tmay(d, key)
        return eliminate_tmay_or_raise(tm, mirror_imay_xedefault_rank, xedefault, d, key, mix=mix, mirror=mirror)
    def set__xedefault(ops, d, key, mirror_imay_xedefault_rank, xedefault, /, *, mix:bool, mirror:bool):
        #nonsense:SHOULD-USE get__xedefault
        (is_old_value, default_or_value) = ops.get__xedefault(d, key, mirror_imay_xedefault_rank, xedefault, mirror=mirror, mix=False)#cased
        if not is_old_value:
            new_value = default = default_or_value
            ops._000___set__new_or_undefined___000_(d, key, new_value)
            #d[key] = default
                #d.setdefault(key, default)
        if mix:
            return default_or_value
        else:
            return (is_old_value, default_or_value)



    def get__xdefault(ops, d, key, imay_xdefault_rank, xdefault, /, *, mix:bool):
        check_imay(imay_xdefault_rank)
        return ops.get__xedefault(d, key, imay_xdefault_rank, xdefault, mirror=False, mix=mix)
    def pop__xdefault(ops, d, key, imay_xdefault_rank, xdefault, /, *, mix:bool):
        check_imay(imay_xdefault_rank)
        return ops.pop__xedefault(d, key, imay_xdefault_rank, xdefault, mirror=False, mix=mix)
    def set__xdefault(ops, d, key, imay_xdefault_rank, xdefault, /, *, mix:bool):
        check_imay(imay_xdefault_rank)
        return ops.set__xedefault(d, key, imay_xdefault_rank, xdefault, mirror=False, mix=mix)
    def get__xdefault__mix(ops, d, key, imay_xdefault_rank, xdefault, /):
        return ops.get__xdefault(d, key, imay_xdefault_rank, xdefault, mix=True)
    def get__xdefault__cased(ops, d, key, imay_xdefault_rank, xdefault, /):
        return ops.get__xdefault(d, key, imay_xdefault_rank, xdefault, mix=False)

    def pop__xdefault__mix(ops, d, key, imay_xdefault_rank, xdefault, /):
        return ops.pop__xdefault(d, key, imay_xdefault_rank, xdefault, mix=True)
    def pop__xdefault__cased(ops, d, key, imay_xdefault_rank, xdefault, /):
        return ops.pop__xdefault(d, key, imay_xdefault_rank, xdefault, mix=False)

    def set__xdefault__mix(ops, d, key, imay_xdefault_rank, xdefault, /):
        return ops.set__xdefault(d, key, imay_xdefault_rank, xdefault, mix=True)
    def set__xdefault__cased(ops, d, key, imay_xdefault_rank, xdefault, /):
        return ops.set__xdefault(d, key, imay_xdefault_rank, xdefault, mix=False)


ops4XDefaultMapping = XDefaultMappingOps()
class XDefaultMappingMixin:
    r'''
    get__tmay
    pop__tmay

    get__xdefault
    pop__xdefault
    set__xdefault

    xxx__xdefault__mix
    xxx__xdefault__cased

    (imay_xdefault_rank, xdefault) >--> (mirror_imay_xedefault_rank, xedefault, /, *, mirror:bool):

    def get__tmay(sf, key, /):
        if key in sf:
            return (sf[key],)
        return ()
    def pop__tmay(sf, key, /):
        tm = sf.get__tmay(key)
        if tm:
            del sf[key]
        return tm

    def get__xdefault(sf, key, imay_xdefault_rank, xdefault, /, *, mix:bool):
        tm = sf.get__tmay(key)
        return eliminate_tmay(tm, imay_xdefault_rank, xdefault, sf, key, mix=mix)
    def pop__xdefault(sf, key, imay_xdefault_rank, xdefault, /, *, mix:bool):
        tm = sf.pop__tmay(key)
        return eliminate_tmay(tm, imay_xdefault_rank, xdefault, sf, key, mix=mix)
    def set__xdefault(sf, key, imay_xdefault_rank, xdefault, /, *, mix:bool):
        (is_value, default_or_value) = sf.get__xdefault(key, imay_xdefault_rank, xdefault, mix=False)#cased
        if not is_value:
            default = default_or_value
            sf[key] = default
                #sf.setdefault(key, default)
        if mix:
            return default_or_value
        else:
            return (is_value, default_or_value)

    def get__xdefault__mix(sf, key, imay_xdefault_rank, xdefault, /):
        return sf.get__xdefault(key, imay_xdefault_rank, xdefault, mix=True)
    def get__xdefault__cased(sf, key, imay_xdefault_rank, xdefault, /):
        return sf.get__xdefault(key, imay_xdefault_rank, xdefault, mix=False)

    def pop__xdefault__mix(sf, key, imay_xdefault_rank, xdefault, /):
        return sf.pop__xdefault(key, imay_xdefault_rank, xdefault, mix=True)
    def pop__xdefault__cased(sf, key, imay_xdefault_rank, xdefault, /):
        return sf.pop__xdefault(key, imay_xdefault_rank, xdefault, mix=False)

    def set__xdefault__mix(sf, key, imay_xdefault_rank, xdefault, /):
        return sf.set__xdefault(key, imay_xdefault_rank, xdefault, mix=True)
    def set__xdefault__cased(sf, key, imay_xdefault_rank, xdefault, /):
        return sf.set__xdefault(key, imay_xdefault_rank, xdefault, mix=False)
    #'''
    __slots__ = ()


    def get__tmay(d, key, /):
        return ops4XDefaultMapping.get__tmay(d, key)
    def pop__tmay(d, key, /):
        return ops4XDefaultMapping.pop__tmay(d, key)

    def get__xedefault(d, key, mirror_imay_xedefault_rank, xedefault, /, *, mix:bool, mirror:bool):
        return ops4XDefaultMapping.get__xedefault(d, key, mirror_imay_xedefault_rank, xedefault, mix=mix, mirror=mirror)
    def pop__xedefault(d, key, mirror_imay_xedefault_rank, xedefault, /, *, mix:bool, mirror:bool):
        return ops4XDefaultMapping.pop__xedefault(d, key, mirror_imay_xedefault_rank, xedefault, mix=mix, mirror=mirror)
    def set__xedefault(d, key, mirror_imay_xedefault_rank, xedefault, /, *, mix:bool, mirror:bool):
        #nonsense:SHOULD-USE get__xedefault
        return ops4XDefaultMapping.set__xedefault(d, key, mirror_imay_xedefault_rank, xedefault, mix=mix, mirror=mirror)


    def get__xdefault(d, key, imay_xdefault_rank, xdefault, /, *, mix:bool):
        return ops4XDefaultMapping.get__xdefault(d, key, imay_xdefault_rank, xdefault, mix=mix)
    def pop__xdefault(d, key, imay_xdefault_rank, xdefault, /, *, mix:bool):
        return ops4XDefaultMapping.pop__xdefault(d, key, imay_xdefault_rank, xdefault, mix=mix)
    def set__xdefault(d, key, imay_xdefault_rank, xdefault, /, *, mix:bool):
        return ops4XDefaultMapping.set__xdefault(d, key, imay_xdefault_rank, xdefault, mix=mix)

    def get__xdefault__mix(d, key, imay_xdefault_rank, xdefault, /):
        return ops4XDefaultMapping.get__xdefault__mix(d, key, imay_xdefault_rank, xdefault)
    def get__xdefault__cased(d, key, imay_xdefault_rank, xdefault, /):
        return ops4XDefaultMapping.get__xdefault__cased(d, key, imay_xdefault_rank, xdefault)

    def pop__xdefault__mix(d, key, imay_xdefault_rank, xdefault, /):
        return ops4XDefaultMapping.pop__xdefault__mix(d, key, imay_xdefault_rank, xdefault)
    def pop__xdefault__cased(d, key, imay_xdefault_rank, xdefault, /):
        return ops4XDefaultMapping.pop__xdefault__cased(d, key, imay_xdefault_rank, xdefault)

    def set__xdefault__mix(d, key, imay_xdefault_rank, xdefault, /):
        return ops4XDefaultMapping.set__xdefault__mix(d, key, imay_xdefault_rank, xdefault)
    def set__xdefault__cased(d, key, imay_xdefault_rank, xdefault, /):
        return ops4XDefaultMapping.set__xdefault__cased(d, key, imay_xdefault_rank, xdefault)




class MappingMixin__auto_setdefault_via_slice4HashMap:
    r'''
    ---
    usage:
        #mimic defaultdict
            d = defaultdict(set)
            d[2].add(4)
        #vs:
            d = derived_class<MappingMixin__auto_setdefault_via_slice4HashMap>()
            d[2:set].add(4)
            d[2:set():-1].add(4)
    ---
    auto setdefault via slice
        since slice is not Hashable
    ---
    required: HashMap
        ie.  key :: Hashable
    ---
    d[key]
    d[key:fdefault] #not default
    d[key:xdefault:imay_xdefault_rank]
    ---
    #'''
    __slots__ = ()
    def __getitem__(sf, hashable_or_slice, /):
        # 0~fdefault instead of -1~default
        return ___getitem_via_hashable_or_slice___(0, __class__, sf, hashable_or_slice)
    def __contains__(sf, hashable_or_slice, /):
        return ___contains_via_hashable_or_slice___(__class__, sf, hashable_or_slice)
def ___contains_via_hashable_or_slice___(__class__, sf, hashable_or_slice, /):
    if type(hashable_or_slice) is slice: raise TypeError
    hashable_ = hashable_or_slice
    return super(__class__, sf).__contains__(hashable_)
def ___getitem_via_hashable_or_slice___(default4imay_xdefault_rank, __class__, sf, hashable_or_slice, /):
    if type(hashable_or_slice) is slice:
        slice_ = hashable_or_slice
        return ___getitem_via_slice___(default4imay_xdefault_rank, __class__, sf, slice_)
    hashable_ = hashable_or_slice
    return super(__class__, sf).__getitem__(hashable_)
def ___getitem_via_slice___(default4imay_xdefault_rank, __class__, sf, slice_, /):
    #slice2triple        # :: slice -> (.start, .stop, .step)
    #assert None is getattr(slice_, '__hash__', None)
    (key, xdefault, may_imay_xdefault_rank) = slice2triple(slice_)
    if may_imay_xdefault_rank is None:
        #imay_xdefault_rank = 0 #fdefault
        imay_xdefault_rank = default4imay_xdefault_rank
    else:
        imay_xdefault_rank = may_imay_xdefault_rank
    if key in sf:
        return sf[key]
    default = mk_default(imay_xdefault_rank, xdefault, sf, key)
    sf[key] = default # sf.setdefault
    return default
    return sf[key]

class XDefaultHashMappingMixin(MappingMixin__auto_setdefault_via_slice4HashMap, XDefaultMappingMixin):
    __slots__ = ()



class XDefaultDict(XDefaultHashMappingMixin, dict):
    __slots__ = ()

class WeakableXDefaultDict(XDefaultDict, WeakableDict):
    __slots__ = ()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):

