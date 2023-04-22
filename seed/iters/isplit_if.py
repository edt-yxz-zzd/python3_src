#__all__:goto
r'''[[[
e ../../python3_src/seed/iters/isplit_if.py


seed.iters.isplit_if
py -m nn_ns.app.debug_cmd   seed.iters.isplit_if -x
py -m nn_ns.app.doctest_cmd seed.iters.isplit_if:__doc__ -ff -v
py_adhoc_call   seed.iters.isplit_if   @f


>>> from seed.iters.isplit_if import iter_split_if__
>>> from seed.iters.isplit_if import iter_split_if_starts_, iter_split_if_ends_, iter_split_with_sep_if_, iter_split_without_sep_if_

>>> from seed.tiny import not_

>>> f = iter_split_without_sep_if_
>>> [*f(not_, '111 111 000 111 000 000 111'.split())]
[['111', '111', '000', '111', '000', '000', '111']]
>>> [*f(not_, '111 111 000 111 000 000 111'.split(), key=None)]
[['111', '111', '000', '111', '000', '000', '111']]
>>> [*f(int, '111 111 000 111 000 000 111'.split())]
[[], [], ['000'], ['000', '000'], []]
>>> [*f(None, '111 111 000 111 000 000 111'.split(), key=int)]
[[], [], ['000'], ['000', '000'], []]
>>> [*f(not_, '111 111 000 111 000 000 111'.split(), key=int)]
[['111', '111'], ['111'], [], ['111']]

>>> f = iter_split_with_sep_if_
>>> [*f(not_, '111 111 000 111 000 000 111'.split())]
[['111', '111', '000', '111', '000', '000', '111']]
>>> [*f(not_, '111 111 000 111 000 000 111'.split(), key=None)]
[['111', '111', '000', '111', '000', '000', '111']]
>>> [*f(int, '111 111 000 111 000 000 111'.split())]
[[], ['111'], [], ['111'], ['000'], ['111'], ['000', '000'], ['111'], []]
>>> [*f(None, '111 111 000 111 000 000 111'.split(), key=int)]
[[], ['111'], [], ['111'], ['000'], ['111'], ['000', '000'], ['111'], []]
>>> [*f(not_, '111 111 000 111 000 000 111'.split(), key=int)]
[['111', '111'], ['000'], ['111'], ['000'], [], ['000'], ['111']]

>>> f = iter_split_if_starts_
>>> [*f(not_, '111 111 000 111 000 000 111'.split())]
[['111', '111', '000', '111', '000', '000', '111']]
>>> [*f(not_, '111 111 000 111 000 000 111'.split(), key=None)]
[['111', '111', '000', '111', '000', '000', '111']]
>>> [*f(int, '111 111 000 111 000 000 111'.split())]
[[], ['111'], ['111', '000'], ['111', '000', '000'], ['111']]
>>> [*f(None, '111 111 000 111 000 000 111'.split(), key=int)]
[[], ['111'], ['111', '000'], ['111', '000', '000'], ['111']]
>>> [*f(not_, '111 111 000 111 000 000 111'.split(), key=int)]
[['111', '111'], ['000', '111'], ['000'], ['000', '111']]


>>> f = iter_split_if_ends_
>>> [*f(not_, '111 111 000 111 000 000 111'.split())]
[['111', '111', '000', '111', '000', '000', '111']]
>>> [*f(not_, '111 111 000 111 000 000 111'.split(), key=None)]
[['111', '111', '000', '111', '000', '000', '111']]
>>> [*f(int, '111 111 000 111 000 000 111'.split())]
[['111'], ['111'], ['000', '111'], ['000', '000', '111'], []]
>>> [*f(None, '111 111 000 111 000 000 111'.split(), key=int)]
[['111'], ['111'], ['000', '111'], ['000', '000', '111'], []]
>>> [*f(not_, '111 111 000 111 000 000 111'.split(), key=int)]
[['111', '111', '000'], ['111', '000'], ['000'], ['111']]



>>> [*iter_split_without_sep_if_(None, [])]
[[]]
>>> [*iter_split_with_sep_if_(None, [])]
[[]]
>>> [*iter_split_if_starts_(None, [])]
[[]]
>>> [*iter_split_if_ends_(None, [])]
[[]]



#]]]'''
__all__ = r'''
iter_split_if__
    iter_split_if_starts_
    iter_split_if_ends_
    iter_split_with_sep_if_
    iter_split_without_sep_if_
'''.split()#'''
__all__


#from seed.iters.iter_with import iter_with_
from seed.tiny import ifNonef, ifNone, echo
from seed.tiny_.check import check_uint_lt
#from itertools import groupby

def iter_split_if__(_0123_, may_predicator, iterable, /, *, key):
    r'''_0123_/uint%4 -> may (k->bool) -> Iter x -> (*key::may (x->k)) -> Iter [x]

    case _0123_ of:
        0 -> [bads...]+
                #iter_split_without_sep_if_
        1 -> [bads..., ok]*, [bads...]
                #iter_split_if_ends_
        2 -> [bads...], [ok, bads...]*
                #iter_split_if_starts_
        3 -> [bads...], ([ok], [bads...])*
                #iter_split_with_sep_if_

    '''#'''

    check_uint_lt(4, _0123_)
    key = ifNone(key, echo)
    predicator = ifNone(may_predicator, bool)

    if _0123_ == 0:
        def f(ls, b_ok, x, /):
            '-> new_lsls'
            if b_ok:
                #discard x
                return ([],)
            ls.append(x)
            return ()
    elif _0123_ == 1:
        def f(ls, b_ok, x, /):
            '-> new_lsls'
            ls.append(x)
            if b_ok:
                return ([],)
            return ()
    elif _0123_ == 2:
        def f(ls, b_ok, x, /):
            '-> new_lsls'
            if b_ok:
                return ([x],)
            ls.append(x)
            return ()
    elif _0123_ == 3:
        def f(ls, b_ok, x, /):
            '-> new_lsls'
            if b_ok:
                return ([x], [])
            ls.append(x)
            return ()
    else:
        raise 000
    f

    ls = []
    #for k, g in groupby(iterable, key=key):
    for x in iterable:
        k = key(x)
        b_ok = bool(predicator(k))
        new_lsls = f(ls, b_ok, x)
        if new_lsls:
            [*lsls, new_ls] = new_lsls
            yield ls
            yield from lsls
            ls = new_ls
    yield ls
    return

iter_split_if__
def iter_split_if_starts_(may_predicator, iterable, /, *, key=None):
    r'may (k->bool) -> Iter x -> (*key::may (x->k)) -> Iter [x] # [bads...], [ok, bads...]*'
    return iter_split_if__(2, may_predicator, iterable, key=key)
def iter_split_if_ends_(may_predicator, iterable, /, *, key=None):
    r'may (k->bool) -> Iter x -> (*key::may (x->k)) -> Iter [x] # [bads..., ok]*, [bads...]'
    return iter_split_if__(1, may_predicator, iterable, key=key)
def iter_split_with_sep_if_(may_predicator, iterable, /, *, key=None):
    r'may (k->bool) -> Iter x -> (*key::may (x->k)) -> Iter [x] # [bads...], ([ok], [bads...])*'
    return iter_split_if__(3, may_predicator, iterable, key=key)
def iter_split_without_sep_if_(may_predicator, iterable, /, *, key=None):
    r'may (k->bool) -> Iter x -> (*key::may (x->k)) -> Iter [x] # [bads...]+'
    return iter_split_if__(0, may_predicator, iterable, key=key)





from seed.iters.isplit_if import iter_split_if__
from seed.iters.isplit_if import iter_split_if_starts_, iter_split_if_ends_, iter_split_with_sep_if_, iter_split_without_sep_if_
from seed.iters.isplit_if import *
