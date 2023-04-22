
__all__ = r'''
    boolexpr_wrapper
    '''.split()#'''

from seed.tiny_.check import check_type_is
from functools import wraps

def boolexpr_wrapper(predicator, /):
    r'''
from seed.tiny import curry1
from operator import __eq__,__contains__#no:__call__
from seed.for_libs.for_operator.__call__ import caller, __call__, call

curry1(operator.__eq__, lhs)
boolexpr_wrapper(curry1(predicator, lhs))
@boolexpr_wrapper
def predicator(...):...

    '''#'''
    @wraps(predicator)
    def f(*args, **kwargs):
        b = predicator(*args, **kwargs)
        check_type_is(bool, b)
        return b
    return f

from seed.tiny_.boolexpr_wrapper import boolexpr_wrapper
