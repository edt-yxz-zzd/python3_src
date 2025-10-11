#__all__:goto
r'''[[[
e ../../python3_src/seed/iters/generator_iterator_mock_asif_at_initial_state.py

seed.iters.generator_iterator_mock_asif_at_initial_state
py -m nn_ns.app.debug_cmd   seed.iters.generator_iterator_mock_asif_at_initial_state -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.iters.generator_iterator_mock_asif_at_initial_state:__doc__ -ht # -ff -df

[[
源起:
view ../../python3_src/seed/iters/flatten_recur.py
将一个允许中的gi伪装成启动前的状态，以捆绑在一起的值替代外部再启动时输入的None
]]


'#'; __doc__ = r'#'
>>> def f(x=999):
...     while 1:
...         x = yield x
...         print(':', x)
>>> gi = Generator__PackWithXValue(f(999), (True, 888))
>>> next(gi)
Traceback (most recent call last):
    ...
TypeError: can't send non-None value to a just-started generator
>>> next(gi)
999

>>> gi = f(999)
>>> gi.send(888) # forbid:start with non-None
Traceback (most recent call last):
    ...
TypeError: can't send non-None value to a just-started generator

>>> gi = f(999)
>>> gi.throw(Exception(555)) # ok:start with exc
Traceback (most recent call last):
    ...
Exception: 555

>>> gi = f(999)
>>> next(gi)
999
>>> gi = Generator__PackWithXValue(gi, (True, 888))
>>> next(gi)
: 888
888
>>> next(gi)
: None
>>> next(gi)
: None
>>> gi.send(666)
: 666
666
>>> gi.send(777)
: 777
777
>>> gi.throw(Exception(555))
Traceback (most recent call last):
    ...
Exception: 555


>>> gi = f(999)
>>> next(gi)
999
>>> gi = pack_generator_iterator__with_value_(gi, 888)
>>> next(gi)
: 888
888
>>> gi.throw(Exception(555))
Traceback (most recent call last):
    ...
Exception: 555


py_adhoc_call   seed.iters.generator_iterator_mock_asif_at_initial_state   @f
from seed.iters.generator_iterator_mock_asif_at_initial_state import *
]]]'''#'''
__all__ = r'''
Generator__PackWithXValue
    pack_generator_iterator__with_xvalue_
    pack_generator_iterator__with_value_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from collections.abc import Generator
from seed.tiny_.check import check_type_is, check_int_ge
#.
___end_mark_of_excluded_global_names__0___ = ...


class Generator__PackWithXValue(Generator):
    def __init__(sf, gi, either_exc_val, /):
        (is_val, exc_or_val) = either_exc_val
        check_type_is(bool, is_val)
        while type(gi) is __class__:
            if not gi._x is None: raise TypeError
            gi = gi._gi
        sf._gi = gi
        sf._x = either_exc_val
    def throw(sf, exc, /):
        if sf._x is None:
            return sf._gi.throw(exc)
        # mock asif starting
        (is_val, exc_or_val) = sf._x

        if is_val:
            val = exc_or_val
            sf._x = None
            # ok:start with exc
            return sf._gi.throw(exc)
            return sf._gi.send(val)
        else:
            _2_exc = exc_or_val
            exc
            raise TypeError('gi start with two exc')
            return sf._gi.throw(exc)


    def send(sf, val, /):
        x = sf._x
        if x is None:
            return sf._gi.send(val)
        # mock asif starting
        if not val is None:
            raise TypeError

        (is_val, exc_or_val) = x
        sf._x = None
        if is_val:
            val = exc_or_val
            return sf._gi.send(val)
        else:
            exc = exc_or_val
            return sf._gi.throw(exc)

def pack_generator_iterator__with_xvalue_(gi, either_exc_val, /):
    'generator_iterator -> xval/(Either exc val) -> generator_iterator{start with xval}'
    return Generator__PackWithXValue(gi, either_exc_val)
def pack_generator_iterator__with_value_(gi, value, /, *, is_exc=False):
    'generator_iterator -> val -> generator_iterator{start with val}'
    return pack_generator_iterator__with_xvalue_(gi, (not is_exc, value))

__all__
#[pack_generator_iterator__with_value_] = lazy_import4funcs_('seed.iters.generator_iterator_mock_asif_at_initial_state', 'pack_generator_iterator__with_value_', __name__)
from seed.iters.generator_iterator_mock_asif_at_initial_state import pack_generator_iterator__with_value_

from seed.iters.generator_iterator_mock_asif_at_initial_state import *
