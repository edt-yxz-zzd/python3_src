#__all__:goto
r'''[[[
e ../../python3_src/seed/iters/flatten_recur__7iter.py

seed.iters.flatten_recur__7iter
py -m nn_ns.app.debug_cmd   seed.iters.flatten_recur__7iter -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.iters.flatten_recur__7iter:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/search_smooth_around_interval.py
]]


'#'; __doc__ = r'#'
>>> def f():
...     yield (Case6halfway.yield1, 666)
...     yield (Case6halfway.yields, [777,888])
...     assert 111000 == (yield (Case6halfway.subcall, g(111)))
...     return (Case6exit.tailcall, g(222))
>>> def g(u, /):
...     yield (Case6halfway.yield1, u)
...     return (Case6exit.return1, u*1000)
>>> it = flatten_recur__7iter_(f())
>>> it is iter(it)
True
>>> type(it)
<class 'generator'>
>>> list(it)
[666, 777, 888, 111, 222]

>>> from seed.iters.generator_iterator_capturer import GeneratorIteratorCapturer
>>> it = GeneratorIteratorCapturer(flatten_recur__7iter_(f()))
>>> it.get_tmay_result()
()
>>> list(it)
[666, 777, 888, 111, 222]
>>> it.get_tmay_result()
(222000,)











py_adhoc_call   seed.iters.flatten_recur__7iter   @f
]]]'''#'''
__all__ = r'''
flatten_recur__7iter_
    Case4FlattenRecur7Iter6halfway
        Case6halfway
    Case4FlattenRecur7Iter6exit
        Case6exit

    default_explain6exit_
    default_explain6halfway_
    default_send_
    default_next6init_
    default_throw_
    default_BaseException

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from enum import Enum
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.helper.ifNone import ifNone
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def default_explain6exit_(x, /):
    return x
def default_explain6halfway_(x, /):
    return x
def default_send_(g, result, /):
    return g.send(result)
default_next6init_ = default_send_
def default_throw_(g, exc, /):
    return g.throw(exc)
default_BaseException = BaseException

class Case4FlattenRecur7Iter6halfway(Enum):
    'explain6halfway_()'
    subcall = -2
    yield1 = 1
    yields = 2
class Case4FlattenRecur7Iter6exit(Enum):
    'explain6exit_()'
    tailcall = -2
    return1 = -1
Case6halfway = Case4FlattenRecur7Iter6halfway
Case6exit = Case4FlattenRecur7Iter6exit
_H = Case4FlattenRecur7Iter6halfway
_E = Case4FlattenRecur7Iter6exit

def flatten_recur__7iter_(g, /, dat6init=None, next6init_=None, *, explain6exit_=None, explain6halfway_=None, send_=None, throw_=None, BaseException=None):
    #vs: def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):
    'Generator{yield ((-2,subcall/Generator, ?dat6init?, ?next6init_?)|(1, out)|(2,outs/Iter out));return ((-2,subcall/Generator, ?dat6init?, ?next6init_?)|(-1, result))} -> Iter out'
    #####################
    #ok:dat6init = ifNone(dat6init, None)
    next6init_ = ifNone(next6init_, default_next6init_)
    explain6exit_ = ifNone(explain6exit_, default_explain6exit_)
    explain6halfway_ = ifNone(explain6halfway_, default_explain6halfway_)
    send_ = ifNone(send_, default_send_)
    throw_ = ifNone(throw_, default_throw_)
    BaseException = ifNone(BaseException, default_BaseException)
    #####################
    _gs = []
    #########
    def replace_(g, dat6init, next6init_, /):
        dat = dat6init
        777;next_ = next6init_
        _gs[-1] = g
        return (dat, next_)
    #########
    def append_(g, dat6init, next6init_, /):
        dat = dat6init
        777;next_ = next6init_
        _gs.append(g)
        return (dat, next_)
    #########
    def pop_(dat, next_, /):
        _gs.pop()
        done = not _gs
        may_g = _gs[-1] if not done else None
        return (done, may_g, dat, next_)
    #########
    (dat, next_) = append_(g, dat6init, next6init_)
    #########
    while 1:
        # (g, dat, next_)
        try:
            x = next_(g, dat)
        except StopIteration as exc:
            x = exc.value
            match explain6exit_(x):
                case tuple((-2|_E.tailcall, g)):
                    #tailcall
                    (dat, next_) = replace_(g, None, send_)
                case tuple((-2|_E.tailcall, g, dat6init, next6init_)):
                    #tailcall
                    (dat, next_) = replace_(g, dat6init, next6init_)
                case tuple((-1|_E.return1, result)):
                    #return1
                    (done, g, dat, next_) = pop_(result, send_)
                    if done: return result
                case y:
                    raise TypeError('unknown y:=explain6exit_(x):', x, y)
            continue
        except BaseException as exc:
            (done, g, dat, next_) = pop_(exc, throw_)
            if done: raise
            continue
        else:
            match explain6halfway_(x):
                case tuple((1|_H.yield1, out)):
                    #yield1
                    yield out
                case tuple((-2|_H.subcall, g)):
                    #subcall
                    (dat, next_) = append_(g, None, send_)
                case tuple((-2|_H.subcall, g, dat6init, next6init_)):
                    #subcall
                    (dat, next_) = append_(g, dat6init, next6init_)
                case tuple((2|_H.yields, outs)):
                    #yields
                    yield from outs
                case y:
                    raise TypeError('unknown y:=explain6halfway_(x):', x, y)
            continue
    #end-while 1:
    #########
    raise 000
    #########


__all__
from seed.iters.flatten_recur__7iter import flatten_recur__7iter_
#def flatten_recur__7iter_(g, /, dat6init=None, next6init_=None, *, explain6exit_=None, explain6halfway_=None, send_=None, throw_=None, BaseException=None):
from seed.iters.flatten_recur__7iter import Case4FlattenRecur7Iter6halfway, Case4FlattenRecur7Iter6exit
#.with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
from seed.iters.flatten_recur__7iter import Case6halfway, Case6exit
    #Case6halfway:subcall, yield1, yields
    #Case6exit:tailcall, return1

from seed.iters.flatten_recur__7iter import *
