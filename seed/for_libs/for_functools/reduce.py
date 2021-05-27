
r'''
py -m seed.for_libs.for_functools.reduce
from seed.for_libs.for_functools.reduce import reduce_with_tmay

functools.reduce(function, iterable[, initializer])
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
#'''

__all__ = '''
    reduce_with_tmay

    fold_with_tmay
    '''.split()
import functools

def _t():
    if None is not functools.reduce(functools.reduce, (), None): raise TypeError

    try:
        functools.reduce(functools.reduce, ())
            #TypeError: reduce() of empty sequence with no initial value
    except TypeError:
        pass
    else:
        raise TypeError

_t()

def reduce_with_tmay(op, tmay_init, iterable, /,*, flip:bool=False):
    if flip:
        f = op
        def op(lhs, rhs, /):
            return f(rhs, lhs)
    #bug:if not tmay_init:
    if tmay_init:
        [init] = tmay_init
        return functools.reduce(op, iterable, init)
    else:
        return functools.reduce(op, iterable)
fold_with_tmay = reduce_with_tmay

