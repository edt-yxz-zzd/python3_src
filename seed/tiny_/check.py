#__all__:goto
r'''[[[
e ../../python3_src/seed/tiny_/check.py

py -m seed.tiny_.check
py -m nn_ns.app.debug_cmd   seed.tiny_.check -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.tiny_.check:__doc__ -ht # -ff -df

[[
!!!!! [x in container] or [x in iterable] or [x in seq_subscriptable] !!!!!

>>> 2 in 5
Traceback (most recent call last):
  ...
TypeError: argument of type 'int' is not iterable
>>> 2 in iter(())
False
>>> it=iter((2,3))
>>> 2 in it
True
>>> [*it]
[3]
>>> it.__contains__
Traceback (most recent call last):
  ...
AttributeError: 'tuple_iterator' object has no attribute '__contains__'
>>> [].__contains__  #doctest: +ELLIPSIS
<method-wrapper '__contains__' of list object at 0x...>

]]


[[
++force_lazy_imported_func_
from seed.types.LazyObj import Lazy
>>> from seed.helper.lazy_import__func import lazy_import4func_
>>> Lazy = lazy_import4func_('seed.types.LazyObj', 'Lazy')
>>> x = Lazy(999)
>>> x
Lazy(999)
>>> Lazy
_LazyImport4Func('seed.types.LazyObj', 'Lazy', '', '')


>>> Lazy = lazy_import4func_('seed.types.LazyObj', 'Lazy')
>>> Lazy
_LazyImport4Func('seed.types.LazyObj', 'Lazy', '', '')
>>> type(x)
<class 'seed.types.LazyObj.Lazy'>
>>> check_is_(Lazy, type(x))
>>> Lazy is type(x)
False
>>> check_is_(int, type(x))
Traceback (most recent call last):
    ...
TypeError: <class 'type'>

>>> Lazy = lazy_import4func_('seed.types.LazyObj', 'Lazy')
>>> check_eq_(Lazy, type(x))
>>> Lazy == type(x) # <<== _LazyImport4Func.__eq__
True
>>> type(x) == Lazy
True
>>> Lazy
_LazyImport4Func('seed.types.LazyObj', 'Lazy', '', '')
>>> check_eq_(int, type(x))
Traceback (most recent call last):
    ...
TypeError: <class 'type'>

>>> Lazy = lazy_import4func_('seed.types.LazyObj', 'Lazy')
>>> check_type_is(Lazy, x)
>>> Lazy is type(x)
False
>>> Lazy
_LazyImport4Func('seed.types.LazyObj', 'Lazy', '', '')
>>> check_type_is(int, x)
Traceback (most recent call last):
    ...
TypeError: <class 'seed.types.LazyObj.Lazy'>

>>> isinstance(999, ()) # => _tmay_force_lazy_imported_func_
False
>>> Lazy = lazy_import4func_('seed.types.LazyObj', 'Lazy')
>>> check_type_le(Lazy, x)

################
#before:++__instancecheck__@_LazyImport4Func
#.>>> isinstance(x, Lazy) #???why not raise TypeError
#.False
################
#after:++__instancecheck__@_LazyImport4Func
>>> isinstance(x, Lazy)
True
>>> Lazy
_LazyImport4Func('seed.types.LazyObj', 'Lazy', '', '')
>>> type(Lazy).__mro__
(<class 'seed.helper.lazy_import__func._LazyImport4Func'>, <class 'seed.helper.lazy_import__func._Forbid_get_set_del'>, <class 'object'>)
>>> isinstance(666, 999) #???TypeError
Traceback (most recent call last):
    ...
TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union
>>> check_type_le(int, x)
Traceback (most recent call last):
    ...
TypeError: <class 'seed.types.LazyObj.Lazy'>

]]





from seed.tiny_.check import check_or_, check_all_, check_tmay_, check_may_, check_not_, icheck_


from seed.tiny_.check import check_subscriptable, icheck_subscriptable
    from seed.tiny_.check import check_getitemable, icheck_getitemable
from seed.tiny_.check import check_callable, check_iterator, check_is_, check_is_None

from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
from seed.tiny_.check import check_str, check_char, check_bool, check_tribool
from seed.tiny_.check import icheck_str, icheck_char, icheck_bool, icheck_tribool

]]]'''#'''

__all__ = '''
    check_non_ABC
    check_ABC

    check_or_
    check_all_
    check_tmay_
    check_may_
    check_not_
    icheck_

    check_subscriptable
        check_getitemable
        is_subscriptable
    check_callable
    check_iterator

    check_type_le_in
    check_type_in
    check_type_le
    check_type_is
    check_tuple__len_le
    check_tuple__len_ge
    check_tuple__len_eq
    check_len_le
    check_len_ge
    check_len_eq
    check_tmay
    check_pair
    check_either
    check_uint
    check_imay

    check_uint_lt
    check_int_ge_lt
        check_int_between
    check_int_ge
    check_int_ge_le
    check_uint_le
    check_imay_le

    icheck_subscriptable
        icheck_getitemable
    icheck_type_le_in
    icheck_type_in
    icheck_type_le
    icheck_type_is
    icheck_tmay
    icheck_pair
    icheck_either
    icheck_uint
    icheck_imay
    icheck_int_ge
    icheck_int_ge_le
    icheck_uint_le
    icheck_imay_le

    check_pseudo_identifier
    check_smay_pseudo_identifier
    check_smay_pseudo_qual_name
    check_pseudo_qual_name

    icheck_pseudo_identifier
    icheck_smay_pseudo_identifier
    icheck_smay_pseudo_qual_name
    icheck_pseudo_qual_name

    check_eq_
    check_is_
        check_is_obj
    check_is_None

    check_str
    check_char
    check_bool
    check_tribool

    icheck_str
    icheck_char
    icheck_bool
    icheck_tribool

'''.split()#'''
    #_force_lazy_imported_func_
    #_is_class_
__all__
####################################
def _is_class_(x, /):
    global _is_class_
    from inspect import isclass as _is_class_
    return _is_class_(x)
def _force_lazy_imported_func_(f, /):
    global _force_lazy_imported_func_
    from seed.helper.lazy_import__func import force_lazy_imported_func_ as _force_lazy_imported_func_
    return _force_lazy_imported_func_(f)
def _tmay_force_lazy_imported_func_(f, /):
    g = _force_lazy_imported_func_(f)
    if g is f:
        return ()
    return (g,)
####################################
__all__










def _call_(check_, obj, /):
    'check_ :: (obj->None) | ((obj->(*args)->None), *args)'
    if callable(check_):
        check_(obj)
    else:
        check_, *args = check_
        check_(*args, obj)

def check_or_(ls4check_, obj, /):
    es = []
    for check_ in ls4check_:
        try:
            _call_(check_, obj)
            777;return#break
        except Exception as exc:
            es.append(exc)
            continue
    else:
        raise TypeError(es)
def check_all_(check_, objs, /):
    for obj in objs:
        _call_(check_, obj)
def check_tmay_(check_, tpl, /):
    check_tmay(tpl)
    match tpl:
        case [obj]:
            _call_(check_, obj)
def check_may_(check_, obj, /):
    if not obj is None:
        _call_(check_, obj)
def check_not_(check_, obj, Types=(TypeError, ValueError, AssertionError), /):
    try:
        _call_(check_, obj)
    #except Exception:
    except Types:
        pass
    else:
        raise TypeError(type(obj))
def icheck_(check_, obj, /):
    _call_(check_, obj)
    return obj

#.def check_hashable(obj, /):
#.    #bug:must use __mro__:if not getattr(type(obj), '__hash__', None) is None: raise TypeError(type(obj))
#.    #   view /sdcard/0my_files/tmp/out4py/py_src/_collections_abc.py
#.    #       Hashable:_check_methods()
#.    #.if not hasattr(type(obj), '__hash__'): raise TypeError(type(obj))
def is_subscriptable(obj, /):
    return hasattr(type(obj), '__getitem__') or (_is_class_(obj) and hasattr(obj, '__class_getitem__'))
def check_subscriptable(obj, /):
    if not is_subscriptable(obj): raise TypeError(type(obj))
check_getitemable = check_subscriptable

def check_callable(obj, /):
    if not callable(obj): raise TypeError(type(obj))
check_callable(check_callable)

def check_iterator(obj, /):
    if not iter(obj) is obj: raise TypeError(type(obj))
check_iterator(iter(''))



def check_type_le_in(clss, obj, /):
    check_type_le(clss, obj)
    return
    #.if not isinstance(obj, clss): raise TypeError(type(obj))
def check_type_le(cls, obj, /):
    # !! ++__instancecheck__@_LazyImport4Func
    if not isinstance(obj, cls): raise TypeError(type(obj))
    return
    ################
    try:
        b = isinstance(obj, cls)
    except TypeError:
        b = False
        pass
    #.if not (b or any(isinstance(obj, C) for C in _tmay_force_lazy_imported_func_(cls))): raise TypeError(type(obj))
    if not (b or isinstance(obj, _tmay_force_lazy_imported_func_(cls))): raise TypeError(type(obj))
    return
    ################
    cls = _force_lazy_imported_func_(cls)
    if not isinstance(obj, cls): raise TypeError(type(obj))
    return
    ################
def check_type_is(cls, obj, /):
    if not ((T:=type(obj)) is cls or T is _force_lazy_imported_func_(cls)): raise TypeError(T)
    return
    #.cls = _force_lazy_imported_func_(cls)
    #.if not type(obj) is cls: raise TypeError(type(obj))
def check_type_in(clss, obj, /):
    if not type(obj) in clss: raise TypeError(type(obj))
#no check_tuple
def check_tuple__len_eq(sz, tpl, /):
    check_type_is(tuple, tpl)
    if not len(tpl) == sz: raise TypeError(sz, len(tpl))
def check_tuple__len_le(sz, tpl, /):
    check_type_is(tuple, tpl)
    if not len(tpl) <= sz: raise TypeError(sz, len(tpl))
def check_tuple__len_ge(sz, tpl, /):
    check_type_is(tuple, tpl)
    if not len(tpl) >= sz: raise TypeError(sz, len(tpl))
def check_len_eq(sz, xs, /):
    if not len(xs) == sz: raise TypeError(sz, len(xs))
def check_len_le(sz, xs, /):
    if not len(xs) <= sz: raise TypeError(sz, len(xs))
def check_len_ge(sz, xs, /):
    if not len(xs) >= sz: raise TypeError(sz, len(xs))
def check_tmay(tpl, /):
    check_type_is(tuple, tpl)
    if not len(tpl) < 2: raise TypeError(len(tpl))
def check_pair(tpl, /):
    check_type_is(tuple, tpl)
    if not len(tpl) == 2: raise TypeError(len(tpl))
def check_either(tpl, /):
    check_pair(tpl)
    check_type_is(bool, tpl[0])

def check_int_ge(min, i, /):
    check_type_is(int, i)
    if not min <= i: raise TypeError(i)
def check_int_ge_le(min, max, i, /):
    check_type_is(int, i)
    if not min <= i <= max: raise TypeError(i)

def check_uint_lt(M, i, /):
    check_int_ge_lt(0, M, i)
def check_int_ge_lt(m, M, i, /):
    check_type_is(int, i)
    if not (m <= i < M): raise TypeError(i)
check_int_between = check_int_ge_lt
def check_uint(i, /):
    check_int_ge(0, i)
def check_imay(i, /):
    check_int_ge(-1, i)

def check_uint_le(max, i, /):
    check_int_ge_le(0, max, i)
def check_imay_le(max, i, /):
    check_int_ge_le(-1, max, i)

def icheck_subscriptable(obj, /):
    check_subscriptable(obj)
    return obj
icheck_getitemable = icheck_subscriptable
def icheck_type_le_in(clss, obj, /):
    check_type_le_in(clss, obj)
    return obj
def icheck_type_in(clss, obj, /):
    check_type_in(clss, obj)
    return obj
def icheck_type_le(cls, obj, /):
    check_type_le(cls, obj)
    return obj
def icheck_type_is(cls, obj, /):
    check_type_is(cls, obj)
    return obj
def icheck_tmay(tpl, /):
    check_tmay(tpl)
    return tpl
def icheck_pair(tpl, /):
    check_pair(tpl)
    return tpl
def icheck_either(tpl, /):
    check_either(tpl)
    return tpl

def icheck_int_ge(min, i, /):
    check_int_ge(min, i)
    return i
def icheck_uint(i, /):
    check_uint(i)
    return i
def icheck_imay(i, /):
    check_imay(i)
    return i

def icheck_int_ge_le(min, max, i, /):
    check_int_ge_le(min, max, i)
    return i
def icheck_uint_le(max, i, /):
    check_uint_le(max, i)
    return i
def icheck_imay_le(max, i, /):
    check_imay_le(max, i)
    return i


def check_pseudo_identifier(s, /):
    'pseudo_identifier identifier includes py-keyword'
    check_type_is(str, s)
    if not s.isidentifier(): raise TypeError(repr(s))
def check_smay_pseudo_identifier(s, /):
    check_type_is(str, s)
    if s:
        check_pseudo_identifier(s)
def check_smay_pseudo_qual_name(s, /):
    'qual_name qualified-name includes py-keyword'
    check_type_is(str, s)
    if s:
        check_pseudo_qual_name(s)
def check_pseudo_qual_name(s, /):
    #check_smay_pseudo_qual_name(s)
    check_type_is(str, s)
    if not all(x.isidentifier() for x in s.split('.')): raise TypeError(repr(s))


def icheck_pseudo_identifier(s, /):
    check_pseudo_identifier(s)
    return s
def icheck_smay_pseudo_identifier(s, /):
    check_smay_pseudo_identifier(s)
    return s
def icheck_smay_pseudo_qual_name(s, /):
    check_smay_pseudo_qual_name(s)
    return s
def icheck_pseudo_qual_name(s, /):
    check_pseudo_qual_name(s)
    return s


#move from above:<<==since force_lazy_imported_func_():ImportError: cannot import name '...' from partially initialized module 'seed.tiny_.check' (most likely due to a circular import)
check_uint(1)
check_tuple__len_eq(0, ())
check_tuple__len_eq(3, (0,1,2))
check_tuple__len_le(3, ())
check_tuple__len_le(3, (0,1,2))
check_tuple__len_ge(0, ())
check_tuple__len_ge(0, (0,1,2))
check_len_eq(0, '')
check_len_eq(3, '012')
check_len_le(3, '')
check_len_le(3, '012')
check_len_ge(0, '')
check_len_ge(0, '012')
check_tmay(())
check_tmay((0,))
check_pair((0, 0))
check_either((False, 0))
check_type_is(str, '')
check_type_le(object, '')
check_type_le_in((int, object), '')
check_type_in((int, str), '')
assert 1 == icheck_uint(1)
assert (0,) == icheck_tmay((0,))
assert (0,0) == icheck_pair((0, 0))
assert (False, 0) == icheck_either((False, 0))
assert '' == icheck_type_is(str, '')
assert '' == icheck_type_le(object, '')




assert 'class'.isidentifier()
assert 'def'.isidentifier()
assert ''.split('.') == ['']
check_pseudo_identifier('def')
check_smay_pseudo_identifier('')
check_smay_pseudo_identifier('def')
check_smay_pseudo_qual_name('')
check_smay_pseudo_qual_name('x')
check_smay_pseudo_qual_name('x.def')
check_pseudo_qual_name('x')
check_pseudo_qual_name('x.def')

def check_eq_(expected, obj, /):
    #.if not (obj == expected or any(obj == x for x in _tmay_force_lazy_imported_func_(expected))): raise TypeError(type(obj))
    if not (obj == expected or obj in _tmay_force_lazy_imported_func_(expected)): raise TypeError(type(obj))
def check_is_(expected, obj, /):
    if not (obj is expected or any(obj is x for x in _tmay_force_lazy_imported_func_(expected))): raise TypeError(type(obj))
    #.expected = _force_lazy_imported_func_(expected)
    #.if not obj is expected: raise TypeError(type(obj))
check_is_obj = check_is_
def check_is_None(obj, /):
    check_is_(None, obj)


def check_str(s, /):
    check_type_is(str, s)

def check_char(s, /):
    check_type_is(str, s)
    if not len(s) == 1: raise TypeError(repr(s))

def check_bool(b, /):
    check_type_is(bool, b)
def check_tribool(b, /):
    if not b is ...:
        check_type_is(bool, b)

def icheck_str(s, /):
    check_str(s)
    return s
def icheck_char(s, /):
    check_char(s)
    return s
def icheck_bool(b, /):
    check_bool(b)
    return b
def icheck_tribool(b, /):
    check_tribool(b)
    return b

def check_non_ABC(cls, /):
    if (nms:=getattr(cls, '__abstractmethods__', None)):
        raise TypeError((cls, sorted(nms)))
def check_ABC(cls, nms=None, /):
    if not (_nms:=getattr(cls, '__abstractmethods__', None)):
        raise TypeError(cls)
    if not nms is None:
        diff = set(nms)^set(_nms)
        if diff:
            raise TypeError(cls, diff)

check_non_ABC(int)
def __():
    from abc import ABC, abstractmethod
    class C(ABC):
        @abstractmethod
        def f():0
    check_ABC(C)
    check_non_ABC(int)

    try:
        check_non_ABC(C)
    except TypeError:
        pass
    else:
        raise 000
    try:
        check_ABC(int)
    except TypeError:
        pass
    else:
        raise 000
__()



from seed.tiny_.check import check_subscriptable, icheck_subscriptable
    #from seed.tiny_.check import check_getitemable, icheck_getitemable
from seed.tiny_.check import check_type_le_in, check_type_in, check_type_le, check_type_is, check_tuple__len_le, check_tuple__len_ge, check_tuple__len_eq, check_len_le, check_len_ge, check_len_eq, check_tmay, check_pair, check_either, check_uint, check_imay, icheck_type_le, icheck_type_is, icheck_tmay, icheck_pair, icheck_either, icheck_uint, icheck_imay
from seed.tiny_.check import check_pseudo_identifier, check_smay_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name, icheck_pseudo_identifier, icheck_smay_pseudo_identifier, icheck_smay_pseudo_qual_name, icheck_pseudo_qual_name
from seed.tiny_.check import check_callable, check_is_, check_is_None

from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
from seed.tiny_.check import check_str, check_char, check_bool, check_tribool
from seed.tiny_.check import icheck_str, icheck_char, icheck_bool, icheck_tribool


from seed.tiny_.check import *
