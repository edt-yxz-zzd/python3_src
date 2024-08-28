#__all__:goto
r'''[[[
e ../../python3_src/seed/lang/generator_iterator_ops.py

[gi :: is_gi__builtin <: is_gi__ABC]


seed.lang.generator_iterator_ops
py -m nn_ns.app.debug_cmd   seed.lang.generator_iterator_ops -x
py -m nn_ns.app.doctest_cmd seed.lang.generator_iterator_ops:__doc__ -ht
py_adhoc_call   seed.lang.generator_iterator_ops   @f

#]]]'''
__all__ = r'''
is_gi_maker

is_gi__builtin
is_gi__ABC

get_gi_locals
get_gi_state
    GEN_CLOSED
    GEN_CREATED
    GEN_RUNNING
    GEN_SUSPENDED


    is_gi_closed
    is_gi_beginning
    is_gi_running
    is_gi_waiting


OccasionError
gi_next__catch
    gi_next
        gi_start
        gi_send

'''.split()#'''
__all__
from seed.types.Either import Cased, Either
#from seed.tiny_.catched_call__either import catched_call__either, cached_catched_call__either, get_or_cached_catched_call__either
import operator
_get_v = operator.attrgetter('value')

from collections.abc import Generator
import inspect
from inspect import \
(getframeinfo as _get_frame_info

,isgeneratorfunction as is_gi_maker
,isgenerator as is_gi__builtin

,getgeneratorlocals as get_gi_locals
,getgeneratorstate as get_gi_state
    ,GEN_CLOSED
    ,GEN_CREATED
    ,GEN_RUNNING
    ,GEN_SUSPENDED
)

is_gi__builtin
def is_gi__ABC(x, /):
    return isinstance(x, Generator)

def __():
    class C(Generator):
        def send():pass
        def throw():pass
    x = C()
    assert is_gi__ABC(x)
    assert not is_gi__builtin(x)
__()

def __():
    def f():yield
    assert is_gi_maker(f)
    y = f()
    assert is_gi__ABC(y)
    assert is_gi__builtin(y)
__()

def __():
  def getgeneratorstate(generator):
    if generator.gi_running:
        return GEN_RUNNING
    if generator.gi_suspended:
        return GEN_SUSPENDED
    if generator.gi_frame is None:
        return GEN_CLOSED
    return GEN_CREATED

def _dir_gi(gi, /):
    gi.close
    gi.send
    gi.throw
    gi.gi_code
    gi.gi_frame
    gi.gi_running
    gi.gi_suspended
    gi.gi_yieldfrom
    ######################
    gi.gi_frame

def is_gi_closed(gi, /):
    return get_gi_state(gi) == GEN_CLOSED
    return gi.gi_frame is None
def is_gi_beginning(gi, /):
    return get_gi_state(gi) == GEN_CREATED
def is_gi_running(gi, /):
    return get_gi_state(gi) == GEN_RUNNING
def is_gi_waiting(gi, /):
    return get_gi_state(gi) == GEN_SUSPENDED

class OccasionError(Exception):pass
def gi_start(gi, /):
    if not is_gi_beginning(gi):raise OccasionError
    return gi.send(None)
def gi_send(gi, val, /):
    if not is_gi_waiting(gi):raise OccasionError
    return gi.send(val)
def gi_next(gi, /, *tmay_val):
    if tmay_val:
        [val] = tmay_val
        return gi_send(gi, val)
    return gi_start(gi)
def gi_next__catch(gi, /, *tmay_val):
    lazy = lambda:gi_next(gi, *tmay_val)
    return Either.from_catched_lazy_value(StopIteration, lazy).fmap_if_left(_get_v)

def __():
    def f():
        r = yield 666
        assert not is_gi_beginning(y)
        assert is_gi_running(y)
        assert not is_gi_waiting(y)
        assert not is_gi_closed(y)

        r = yield r
        assert not is_gi_beginning(y)
        assert is_gi_running(y)
        assert not is_gi_waiting(y)
        assert not is_gi_closed(y)

        return r
    assert is_gi_maker(f)
    y = f()
    assert is_gi__ABC(y)
    assert is_gi__builtin(y)

    assert is_gi_beginning(y)
    assert not is_gi_running(y)
    assert not is_gi_waiting(y)
    assert not is_gi_closed(y)

    assert 666 == gi_next(y)
    assert not is_gi_beginning(y)
    assert not is_gi_running(y)
    assert is_gi_waiting(y)
    assert not is_gi_closed(y)

    assert (True, 777) == gi_next__catch(y, 777)
    assert not is_gi_beginning(y)
    assert not is_gi_running(y)
    assert is_gi_waiting(y)
    assert not is_gi_closed(y)

    assert (False, 999) == gi_next__catch(y, 999)
    assert not is_gi_beginning(y)
    assert not is_gi_running(y)
    assert not is_gi_waiting(y)
    assert is_gi_closed(y)

__()




__all__
from seed.lang.generator_iterator_ops import gi_next__catch, gi_next, gi_start, gi_send, OccasionError
from seed.lang.generator_iterator_ops import  is_gi__builtin, is_gi__ABC, is_gi_maker
from seed.lang.generator_iterator_ops import is_gi_closed, is_gi_beginning, is_gi_running, is_gi_waiting

from seed.lang.generator_iterator_ops import get_gi_state, GEN_CLOSED, GEN_CREATED, GEN_RUNNING, GEN_SUSPENDED
from seed.lang.generator_iterator_ops import get_gi_locals



from seed.lang.generator_iterator_ops import *
