#from seed.tiny_.check import check_getitemable, icheck_getitemable
#from seed.tiny_.check import check_type_le, check_type_is, check_tmay, check_pair, check_uint, check_imay, icheck_type_le, icheck_type_is, icheck_tmay, icheck_pair, icheck_uint, icheck_imay
#from seed.tiny_.check import check_pseudo_identifier, check_smay_pseudo_qual_name, check_pseudo_qual_name, icheck_pseudo_identifier, icheck_smay_pseudo_qual_name, icheck_pseudo_qual_name
#from seed.tiny_.check import check_callable, check_is_obj, check_is_None

#from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
#from seed.tiny_.check import check_str, check_char

__all__ = '''
    check_getitemable

    check_type_le
    check_type_is
    check_tmay
    check_pair
    check_uint
    check_imay

    check_uint_lt
    check_int_ge_lt
    check_int_ge
    check_int_ge_le

    icheck_getitemable
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
    '''.split()


def check_getitemable(x, /):
    if not hasattr(type(x), '__getitem__'): raise TypeError

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

def icheck_getitemable(obj, /):
    check_getitemable(obj)
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
check_type_is(str, '')
check_type_le(object, '')
assert 1 == icheck_uint(1)
assert (0,) == icheck_tmay((0,))
assert (0,0) == icheck_pair((0, 0))
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

