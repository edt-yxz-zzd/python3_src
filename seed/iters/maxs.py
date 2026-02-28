#__all__:goto
r'''[[[
e ../../python3_src/seed/iters/maxs.py

seed.iters.maxs
py -m nn_ns.app.debug_cmd   seed.iters.maxs -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.iters.maxs:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> maxs_(len, str, [{}, '0', '', [1,2], 'ab', (), b'34'])
(2, ['[1, 2]', 'ab', "b'34'"])
>>> mins_(len, str, [{}, '0', '', [1,2], 'ab', (), b'34'])
(0, ['{}', '', '()'])

>>> (maxs7continue_(len, str, 1, outs:=[999], [{}, '0', '', [1,2], 'ab', (), b'34']), outs)
(2, ['[1, 2]', 'ab', "b'34'"])
>>> (maxs7continue_(len, str, 2, outs:=[999], [{}, '0', '', [1,2], 'ab', (), b'34']), outs)
(2, [999, '[1, 2]', 'ab', "b'34'"])
>>> (maxs7continue_(len, str, 3, outs:=[999], [{}, '0', '', [1,2], 'ab', (), b'34']), outs)
(3, [999])

>>> (mins7continue_(len, str, 1, outs:=[999], [{}, '0', '', [1,2], 'ab', (), b'34']), outs)
(0, ['{}', '', '()'])
>>> (mins7continue_(len, str, 0, outs:=[999], [{}, '0', '', [1,2], 'ab', (), b'34']), outs)
(0, [999, '{}', '', '()'])
>>> (mins7continue_(len, str, -1, outs:=[999], [{}, '0', '', [1,2], 'ab', (), b'34']), outs)
(-1, [999])


py_adhoc_call   seed.iters.maxs   @f
]]]'''#'''
__all__ = r'''
maxs_
    maxs7continue_
mins_
    mins7continue_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from operator import lt, gt
from seed.tiny_.funcs import echo
from seed.helper.ifNone import ifNone
___end_mark_of_excluded_global_names__0___ = ...

def maxs_(may_x2k_, may_x2y_, xs, /, *, __lt__=None):
    'may (x->k) -> may (x->y) -> Iter x -> (k, [y])'
    x2k_ = ifNone(may_x2k_, echo)
    x2y_ = ifNone(may_x2y_, echo)
    xs = iter(xs)
    for x0 in xs:
        break
    else:
        max(xs)
        raise 000
    k0 = x2k_(x0)
    max_ys = [x2y_(x0)]
    max_k = maxs7continue_(x2k_, x2y_, k0, max_ys, xs, __lt__=__lt__)
    return (max_k, max_ys)
def maxs7continue_(may_x2k_, may_x2y_, max_k, max_ys, xs, /, *, __lt__=None):
    'may (x->k) -> may (x->y) -> k -> [y]/list@INOUT-> Iter x -> k'
    x2k_ = ifNone(may_x2k_, echo)
    x2y_ = ifNone(may_x2y_, echo)
    __lt__ = ifNone(__lt__, lt)
    for x in xs:
        k = x2k_(x)
        if __lt__(k, max_k):
            # [k < max_k]
            continue
        if __lt__(max_k, k):
            # [k > max_k]
            max_k = k
            del max_ys[:]
        y = x2y_(x)
        max_ys.append(y)
    return max_k

def mins_(may_x2k_, may_x2y_, xs, /, *, __lt__=None):
    'may (x->k) -> may (x->y) -> Iter x -> (k, [y])'
    return maxs_(may_x2k_, may_x2y_, xs, __lt__=gt)
def mins7continue_(may_x2k_, may_x2y_, max_k, max_ys, xs, /, *, __lt__=None):
    'may (x->k) -> may (x->y) -> k -> [y]/list@INOUT-> Iter x -> k'
    return maxs7continue_(may_x2k_, may_x2y_, max_k, max_ys, xs, __lt__=gt)

__all__
from seed.iters.maxs import maxs_, maxs7continue_, mins_, mins7continue_
from seed.iters.maxs import *
