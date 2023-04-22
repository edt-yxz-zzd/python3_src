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


from seed.tiny_.check import check_subscriptable, icheck_subscriptable
    from seed.tiny_.check import check_getitemable, icheck_getitemable
from seed.tiny_.check import check_type_le, check_type_is, check_tmay, check_pair check_either, check_uint, check_imay, icheck_type_le, icheck_type_is, icheck_tmay, icheck_pair, icheck_either, icheck_uint, icheck_imay
from seed.tiny_.check import check_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name, icheck_pseudo_identifier, icheck_smay_pseudo_qual_name, icheck_pseudo_qual_name
from seed.tiny_.check import check_callable, check_is_obj, check_is_None

from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
from seed.tiny_.check import check_str, check_char, check_bool
from seed.tiny_.check import icheck_str, icheck_char, icheck_bool

]]]'''#'''

__all__ = '''
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
    check_smay_pseudo_qual_name
    check_pseudo_qual_name

    icheck_pseudo_identifier
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


def check_subscriptable(x, /):
    if not hasattr(type(x), '__getitem__'): raise TypeError(type(x))
check_getitemable = check_subscriptable

def check_type_in(clss, obj, /):
    if not type(obj) in clss: raise TypeError
def check_type_le(cls, obj, /):
    if not isinstance(obj, cls): raise TypeError
def check_type_is(cls, obj, /):
    if not type(obj) is cls: raise TypeError
#no check_tuple
def check_tmay(obj, /):
    check_type_is(tuple, obj)
    if not len(obj) < 2: raise TypeError
def check_pair(obj, /):
    check_type_is(tuple, obj)
    if not len(obj) == 2: raise TypeError
def check_either(obj, /):
    check_pair(obj); check_type_is(bool, obj[0])

def check_int_ge(min, obj, /):
    check_type_is(int, obj)
    if not min <= obj: raise TypeError
def check_int_ge_le(min, max, obj, /):
    check_type_is(int, obj)
    if not min <= obj <= max: raise TypeError

def check_uint_lt(M, i, /):
    check_int_ge_lt(0, M, i)
def check_int_ge_lt(m, M, i, /):
    check_type_is(int, i)
    if not (m <= i < M): raise TypeError
check_int_between = check_int_ge_lt
def check_uint(obj, /):
    check_int_ge(0, obj)
def check_imay(obj, /):
    check_int_ge(-1, obj)

def check_uint_le(max, obj, /):
    check_int_ge_le(0, max, obj)
def check_imay_le(max, obj, /):
    check_int_ge_le(-1, max, obj)

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
def icheck_tmay(obj, /):
    check_tmay(obj)
    return obj
def icheck_pair(obj, /):
    check_pair(obj)
    return obj
def icheck_either(obj, /):
    check_either(obj)
    return obj

def icheck_int_ge(min, obj, /):
    check_int_ge(min, obj)
    return obj
def icheck_uint(obj, /):
    check_uint(obj)
    return obj
def icheck_imay(obj, /):
    check_imay(obj)
    return obj

def icheck_int_ge_le(min, max, obj, /):
    check_int_ge_le(min, max, obj)
    return obj
def icheck_uint_le(max, obj, /):
    check_uint_le(max, obj)
    return obj
def icheck_imay_le(max, obj, /):
    check_imay_le(max, obj)
    return obj

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


def check_pseudo_identifier(obj, /):
    'pseudo_identifier identifier includes py-keyword'
    check_type_is(str, obj)
    if not obj.isidentifier(): raise TypeError
def check_smay_pseudo_qual_name(obj, /):
    'qual_name qualified-name includes py-keyword'
    check_type_is(str, obj)
    if obj:
        check_pseudo_qual_name(obj)
def check_pseudo_qual_name(obj, /):
    #check_smay_pseudo_qual_name(obj)
    check_type_is(str, obj)
    if not all(x.isidentifier() for x in obj.split('.')): raise TypeError


def icheck_pseudo_identifier(obj, /):
    check_pseudo_identifier(obj)
    return obj
def icheck_smay_pseudo_qual_name(obj, /):
    check_smay_pseudo_qual_name(obj)
    return obj
def icheck_pseudo_qual_name(obj, /):
    check_pseudo_qual_name(obj)
    return obj

assert 'class'.isidentifier()
assert 'def'.isidentifier()
assert ''.split('.') == ['']
check_pseudo_identifier('def')
check_smay_pseudo_qual_name('')
check_smay_pseudo_qual_name('x')
check_smay_pseudo_qual_name('x.def')
check_pseudo_qual_name('x')
check_pseudo_qual_name('x.def')

def check_callable(obj, /):
    if not callable(obj): raise TypeError

check_callable(check_callable)

def check_is_obj(expected, obj, /):
    if not obj is expected: raise TypeError
def check_is_None(obj, /):
    check_is_obj(None, obj)


def check_str(s, /):
    check_type_is(str, s)

def check_char(char, /):
    check_type_is(str, char)
    if not len(char) == 1: raise TypeError

def check_bool(b, /):
    check_type_is(bool, b)

def icheck_str(obj, /):
    check_str(obj)
    return obj
def icheck_char(obj, /):
    check_char(obj)
    return obj
def icheck_bool(obj, /):
    check_bool(obj)
    return obj




from seed.tiny_.check import check_subscriptable, icheck_subscriptable
    #from seed.tiny_.check import check_getitemable, icheck_getitemable
from seed.tiny_.check import check_type_le, check_type_is, check_tmay, check_pair, check_either, check_uint, check_imay, icheck_type_le, icheck_type_is, icheck_tmay, icheck_pair, icheck_either, icheck_uint, icheck_imay
from seed.tiny_.check import check_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name, icheck_pseudo_identifier, icheck_smay_pseudo_qual_name, icheck_pseudo_qual_name
from seed.tiny_.check import check_callable, check_is_obj, check_is_None

from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
from seed.tiny_.check import check_str, check_char, check_bool
from seed.tiny_.check import icheck_str, icheck_char, icheck_bool


from seed.tiny_.check import *
