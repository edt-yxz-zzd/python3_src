#__all__:goto
r'''[[[
e ../../python3_src/seed/iters/IteratorResultGettor.py

seed.iters.IteratorResultGettor
py -m nn_ns.app.debug_cmd   seed.iters.IteratorResultGettor -x
py -m nn_ns.app.doctest_cmd seed.iters.IteratorResultGettor:__doc__ -ht

>>> def f(it, r, /):
...     yield from it
...     return r
>>> def h(it, e, /):
...     yield from it
...     raise e


>>> g = IteratorResultGettor(f(range(9), 999))
>>> g.tmay_result_or_raise
()
>>> g.may_either_result
>>> g.stopped
False
>>> for _ in g:pass
>>> g.tmay_result_or_raise
(999,)
>>> g.may_either_result
(True, 999)
>>> g.stopped
True
>>> [*g]
[]
>>> g.tmay_result_or_raise
(999,)
>>> g.may_either_result
(True, 999)
>>> g.stopped
True


>>> g = IteratorResultGettor(h(range(9), Exception(999)))
>>> g.tmay_result_or_raise
()
>>> g.may_either_result
>>> g.stopped
False
>>> for _ in g:pass
Traceback (most recent call last):
    ...
Exception: 999
>>> g.tmay_result_or_raise
Traceback (most recent call last):
    ...
Exception: 999
>>> g.may_either_result
(False, Exception(999))
>>> g.stopped
True
>>> for _ in g:pass
Traceback (most recent call last):
    ...
Exception: 999




>>> c = IterableResultCollector(f(range(9), 999))
>>> bool(c)
False
>>> len(c)
0
>>> c[:]
[]
>>> for _ in c:pass
>>> bool(c)
True
>>> len(c)
1
>>> c[:]
[999]
>>> for _ in c:pass
>>> c[:]
[999, None]
>>> for _ in c:pass
>>> bool(c)
True
>>> len(c)
3
>>> c[:]
[999, None, None]
>>> c.clear()
>>> bool(c)
False
>>> len(c)
0
>>> c[:]
[]


>>> c = IterableResultCollector(h(range(9), Exception(999)))
>>> bool(c)
False
>>> len(c)
0
>>> c[:]
[]
>>> for _ in c:pass
Traceback (most recent call last):
    ...
Exception: 999
>>> bool(c)
False
>>> len(c)
0
>>> c[:]
[]
>>> for _ in c:pass
>>> bool(c)
True
>>> len(c)
1
>>> c[:]
[None]
>>> for _ in c:pass
>>> c[:]
[None, None]
>>> for _ in c:pass
>>> bool(c)
True
>>> len(c)
3
>>> c[:]
[None, None, None]
>>> c.clear()
>>> bool(c)
False
>>> len(c)
0
>>> c[:]
[]




#]]]'''
__all__ = r'''
IteratorResultGettor
IterableResultCollector
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...

class IterableResultCollector:
    'iterable#no:exc'
    def __init__(sf, xs, /):
        sf._xs = xs
        sf._rs = []
    def __iter__(sf, /):
        r = yield from sf._xs
        sf._rs.append(r)
        return r
    def __bool__(sf, /):
        return bool(sf._rs)
    def __len__(sf, /):
        return len(sf._rs)
    def __getitem__(sf, k, /):
        return sf._rs[k]
    def clear(sf, /):
        return sf._rs.clear()
    def _get_results_(sf, /):
        'mutable'
        return sf._rs


class IteratorResultGettor:
    'iterator#catch:exc'
    def __init__(sf, xs, /):
        sf._r = None
        sf._it = iter(xs)
    @property
    def tmay_result_or_raise(sf, /):
        '-> tmay result | ^exc'
        if sf._r:
            (ok, x) = sf._r
            if ok:
                return (x,)
            raise x
        return ()
    @property
    def may_either_result(sf, /):
        '-> may (exc_vs_result, exc_or_result)'
        return sf._r
    @property
    def stopped(sf, /):
        '-> bool'
        return bool(sf._r)
    def __iter__(sf, /):
        return sf
    def __next__(sf, /):
        if sf._r:
            (ok, x) = sf._r
            if ok:
                raise StopIteration(x)
            raise x
        try:
            return next(sf._it)
        except StopIteration as e:
            sf._r = (True, e.value)
            sf._it = None
            raise
        except Exception as e:
            sf._r = (False, e)
            sf._it = None
            raise


__all__
from seed.iters.IteratorResultGettor import IteratorResultGettor, IterableResultCollector
from seed.iters.IteratorResultGettor import *
