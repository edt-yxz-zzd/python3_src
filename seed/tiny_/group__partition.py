#__all__:goto
r'''[[[
e ../../python3_src/seed/tiny_/group__partition.py


seed.tiny_.group__partition
py -m nn_ns.app.debug_cmd   seed.tiny_.group__partition -x
py -m nn_ns.app.doctest_cmd seed.tiny_.group__partition:__doc__ -ff -v

>>> from seed.tiny_.group__partition import partition_xs_by_bool_, xs_to_vss_, xs_to_k2vs_
>>> from seed.tiny import fst, snd
>>> xs_to_k2vs_(fst, snd, [(1,2),(3,4),(1,999,5),(3,4),(5,6)]) == {1: [2, 999], 3: [4, 4], 5: [6]}
True
>>> xs_to_k2vs_(len, None, [(1,2),(3,4),(1,999,5),(3,4),(5,6)]) == {2: [(1, 2), (3, 4), (3, 4), (5, 6)], 3: [(1, 999, 5)]}
True
>>> xs_to_k2vs_(None, None, [(1,2),(3,4),(1,999,5),(3,4),(5,6)]) == {(1, 2): [(1, 2)], (3, 4): [(3, 4), (3, 4)], (1, 999, 5): [(1, 999, 5)], (5, 6): [(5, 6)]}
True
>>> xs_to_vss_(4, len, None, [(1,2),(3,4),(1,999,5),(3,4),(5,6)])
([], [], [(1, 2), (3, 4), (3, 4), (5, 6)], [(1, 999, 5)])
>>> xs_to_vss_(4, len, snd, [(1,2),(3,4),(1,999,5),(3,4),(5,6)])
([], [], [2, 4, 4, 6], [999])
>>> xs_to_vss_(4, None, None, [-1,1,2,3,2,3,3,-2, 0,False])
([0, False], [1], [2, 2, -2], [-1, 3, 3, 3])
>>> partition_xs_by_bool_(None, [0,1,-2,False, ...,True, None,[],(),[3]])
([0, False, None, [], ()], [1, -2, Ellipsis, True, [3]])


#]]]'''
__all__ = r'''
    partition_xs_by_bool_
    xs_to_vss_
    xs_to_k2vs_
'''.split()#'''
__all__

from seed.tiny_.funcs import echo, fst, snd
from seed.tiny_.check import check_callable, check_uint
from seed.helper.ifNone import ifNone, ifNonef
#from seed.helper.Echo import echo
#from seed.tiny import echo, ifNone, check_callable
#from seed.iters.group_by import group_by
from collections import defaultdict
#from operator import __index__

def partition_xs_by_bool_(may_predicator, xs, /):
    'may (x->bool) -> Iter x -> (bads/[x], goods/[x])'
    predicator = ifNone(may_predicator, echo)
    check_callable(predicator)
    def x2idx_(x,/):
        return bool(predicator(x))
    bads, goods = xs_to_vss_(2, x2idx_, None, xs)
    return bads, goods

def xs_to_vss_(sz, may_x2idx_, may_x2v_, xs, /):
    'sz/uint -> may (x->idx) -> may (x->v) -> Iter x -> tuple<[v]>{len=sz}'
    check_uint(sz)
    k2vs = xs_to_k2vs_(may_x2idx_, may_x2v_, xs, may_k2vs_or_sz=sz)
    vss = k2vs
    assert type(vss) is tuple
    assert len(vss) == sz
    return vss
def xs_to_k2vs_(may_x2k_, may_x2v_, xs, /, *, may_k2vs_or_sz=None):
    'may (x->idx) -> may (x->v) -> Iter x -> *may_k2vs_or_sz/(may (k2vs/{k:[v]} | sz/uint)) -> (k2vs | tuple<[v]>{len=sz})'
    x2k_ = ifNone(may_x2k_, echo)
    x2v_ = ifNone(may_x2v_, echo)
    check_callable(x2k_)
    check_callable(x2v_)

    if type(may_k2vs_or_sz) is int:
        sz = may_k2vs_or_sz
        check_uint(sz)
        #k2vs = [[] for _ in range(sz)]
        k2vs = tuple([] for _ in range(sz))
            #to avoid k be slice
    else:
        may_k2vs = may_k2vs_or_sz
        k2vs = ifNonef(may_k2vs, lambda:defaultdict(list))
    post = dict if may_k2vs_or_sz is None else echo

    #for k, g in groupby(iterable, key=x2k_):
    for x in xs:
        k = x2k_(x)
        v = x2v_(x)
        k2vs[k].append(v)
    k2vs = post(k2vs)
    return k2vs

assert xs_to_k2vs_(fst, snd, [(1,2),(3,4),(1,999,5),(3,4),(5,6)]) == {1: [2, 999], 3: [4, 4], 5: [6]}
assert xs_to_vss_(4, len, snd, [(1,2),(3,4),(1,999,5),(3,4),(5,6)]) == ([], [], [2, 4, 4, 6], [999])
assert partition_xs_by_bool_(None, [0,1,-2,False, ...,True, None,[],(),[3]]) == ([0, False, None, [], ()], [1, -2, Ellipsis, True, [3]])

from seed.tiny_.group__partition import partition_xs_by_bool_, xs_to_vss_, xs_to_k2vs_
from seed.tiny_.group__partition import *
