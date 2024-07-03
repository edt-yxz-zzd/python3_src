r'''[[[

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
>>> [].__contains__
<method-wrapper '__contains__' of list object at 0x...>

]]

from seed.tiny_.check import check_may_, check_not_

from seed.tiny_.check import check_subscriptable, icheck_subscriptable
    from seed.tiny_.check import check_getitemable, icheck_getitemable
from seed.tiny_.check import check_type_le, check_type_is, check_tmay, check_pair check_either, check_uint, check_imay, icheck_type_le, icheck_type_is, icheck_tmay, icheck_pair, icheck_either, icheck_uint, icheck_imay
from seed.tiny_.check import check_pseudo_identifier, check_smay_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name, icheck_pseudo_identifier, icheck_smay_pseudo_identifier, icheck_smay_pseudo_qual_name, icheck_pseudo_qual_name
from seed.tiny_.check import check_callable, check_is_obj, check_is_None

from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
from seed.tiny_.check import check_str, check_char, check_bool
from seed.tiny_.check import icheck_str, icheck_char, icheck_bool

]]]'''#'''

__all__ = '''
    check_may_
    check_not_

    check_subscriptable
        check_getitemable

    check_type_in
    check_type_le
    check_type_is
    check_tmay
    check_pair
    check_either
    check_uint
    check_imay

    check_uint_lt
    check_int_ge_lt
    check_int_ge
    check_int_ge_le

    icheck_subscriptable
        icheck_getitemable
    icheck_type_in
    icheck_type_le
    icheck_type_is
    icheck_tmay
    icheck_pair
    icheck_uint
    icheck_imay

    check_pseudo_identifier
    check_smay_pseudo_identifier
    check_smay_pseudo_qual_name
    check_pseudo_qual_name

    icheck_pseudo_identifier
    icheck_smay_pseudo_identifier
    icheck_smay_pseudo_qual_name
    icheck_pseudo_qual_name

    check_callable
    check_is_obj
    check_is_None

    check_str
    check_char
    check_bool

    icheck_str
    icheck_char
    icheck_bool
    '''.split()

def _call_(check_, obj, /):
    'check_ :: (obj->None) | ((obj->None), *args)'
    if callable(check_):
        check_(obj)
    else:
        check_, *args = check_
        check_(*args, obj)

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

def check_subscriptable(obj, /):
    if not hasattr(type(obj), '__getitem__'): raise TypeError(type(obj))
check_getitemable = check_subscriptable

def check_type_in(clss, obj, /):
    if not type(obj) in clss: raise TypeError(type(obj))
def check_type_le(cls, obj, /):
    if not isinstance(obj, cls): raise TypeError(type(obj))
def check_type_is(cls, obj, /):
    if not type(obj) is cls: raise TypeError(type(obj))
#no check_tuple
def check_tmay(tpl, /):
    check_type_is(tuple, tpl)
    if not len(tpl) < 2: raise TypeError(len(tpl))
def check_pair(tpl, /):
    check_type_is(tuple, tpl)
    if not len(tpl) == 2: raise TypeError(len(tpl))
def check_either(tpl, /):
    check_pair(tpl); check_type_is(bool, tpl[0])

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

check_uint(1)
check_tmay(())
check_tmay((0,))
check_pair((0, 0))
check_either((False, 0))
check_type_is(str, '')
check_type_le(object, '')
assert 1 == icheck_uint(1)
assert (0,) == icheck_tmay((0,))
assert (0,0) == icheck_pair((0, 0))
assert (False, 0) == icheck_either((False, 0))
assert '' == icheck_type_is(str, '')
assert '' == icheck_type_le(object, '')


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

def check_callable(obj, /):
    if not callable(obj): raise TypeError(type(obj))

check_callable(check_callable)

def check_is_obj(expected, obj, /):
    if not obj is expected: raise TypeError(type(obj))
def check_is_None(obj, /):
    check_is_obj(None, obj)


def check_str(s, /):
    check_type_is(str, s)

def check_char(s, /):
    check_type_is(str, s)
    if not len(s) == 1: raise TypeError(repr(s))

def check_bool(b, /):
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




from seed.tiny_.check import check_subscriptable, icheck_subscriptable
    #from seed.tiny_.check import check_getitemable, icheck_getitemable
from seed.tiny_.check import check_type_le, check_type_is, check_tmay, check_pair, check_either, check_uint, check_imay, icheck_type_le, icheck_type_is, icheck_tmay, icheck_pair, icheck_either, icheck_uint, icheck_imay
from seed.tiny_.check import check_pseudo_identifier, check_smay_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name, icheck_pseudo_identifier, icheck_smay_pseudo_identifier, icheck_smay_pseudo_qual_name, icheck_pseudo_qual_name
from seed.tiny_.check import check_callable, check_is_obj, check_is_None

from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
from seed.tiny_.check import check_str, check_char, check_bool
from seed.tiny_.check import icheck_str, icheck_char, icheck_bool


from seed.tiny_.check import *
