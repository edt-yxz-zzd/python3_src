
from seed.excepts.sand_excepts import CheckError, CheckTypeError, CheckValueError


UINT32_UP_BOUND = 1 << 32
UINT8_UP_BOUND = 1 << 8
def is_uint(u):
    return type(u) is int and 0 <= u
def is_pint(u):
    'is positive int'
    return type(u) is int and 0 < u
def is_uint32(u):
    return type(u) is int and 0 <= u < UINT32_UP_BOUND
def is_uint8(u):
    return type(u) is int and 0 <= u < UINT8_UP_BOUND
def is_type(obj, T):
    return type(obj) is T

   
def check_uint(u, name):
    if not is_uint(u):
        raise CheckTypeError('not is_uint({})'.format(name))   
def check_pint(u, name):
    if not is_pint(u):
        raise CheckTypeError('not is_pint({}) # not positive int'.format(name))
    
def check_uint32(u, name):
    if not is_uint32(u):
        raise CheckTypeError('not is_uint32({})'.format(name))
def check_uint8(u, name):
    if not is_uint8(u):
        raise CheckTypeError('not is_uint8({})'.format(name))
    
def check_type(obj, T, name):
    if not is_type(obj, T):
        raise CheckTypeError('not is_type({}, {})'.format(name, T.__name__))
def check_value(obj, value, err_str):
    if not obj == value:
        raise CheckValueError(err_str)

def check_type_value(obj, value, obj_name, value_str):
    check_type(obj, type(value), obj_name)
    if not obj == value:
        err_str = '{} != {}'.format(obj_name, value_str)
        raise CheckValueError(err_str)



def to_uint(u, name):
    u = int(u)
    check_uint(u, name)
    return u
def to_pint(u, name):
    u = int(u)
    check_pint(u, name)
    return u







