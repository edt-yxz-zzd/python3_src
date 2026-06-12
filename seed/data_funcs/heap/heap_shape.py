#__all__:goto
r'''[[[
e ../../python3_src/seed/data_funcs/heap/heap_shape.py

seed.data_funcs.heap.heap_shape
py -m nn_ns.app.debug_cmd   seed.data_funcs.heap.heap_shape -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.data_funcs.heap.heap_shape:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/Chinese_Remainder_Theorem__ver2.py
]]


'#'; __doc__ = r'#'
>>> heap_shape5num_leafs_(-1)
Traceback (most recent call last):
    ...
TypeError: -1
>>> heap_shape5num_leafs_(0)
(0, 0, 0)
>>> heap_shape5num_leafs_(1)
(1, 1, 1)
>>> heap_shape5num_leafs_(2)
(3, 2, 2)
>>> for L in range(20):print(L, heap_shape5num_leafs_(L), sep=':')
0:(0, 0, 0)
1:(1, 1, 1)
2:(3, 2, 2)
3:(5, 3, 2)
4:(7, 3, 4)
5:(9, 4, 2)
6:(11, 4, 4)
7:(13, 4, 6)
8:(15, 4, 8)
9:(17, 5, 2)
10:(19, 5, 4)
11:(21, 5, 6)
12:(23, 5, 8)
13:(25, 5, 10)
14:(27, 5, 12)
15:(29, 5, 14)
16:(31, 5, 16)
17:(33, 6, 2)
18:(35, 6, 4)
19:(37, 6, 6)

>>> mk_rvheap__Nothing_(None, range(3))
[0, 1, 2, None, None]
>>> mk_rvheap__fill_(lambda x,y:f'({x}++{y})', range(3))
[0, 1, 2, '(0++1)', '(2++(0++1))']
>>> mk_rvheap__fill_(lambda x,y:f'({x}++{y})', range(4))
[0, 1, 2, 3, '(0++1)', '(2++3)', '((0++1)++(2++3))']
>>> mk_rvheap__fill_(lambda x,y:f'({x}++{y})', range(5))
[0, 1, 2, 3, 4, '(0++1)', '(2++3)', '(4++(0++1))', '((2++3)++(4++(0++1)))']


>>> mk_rvheap__fill_(lambda k,x6k,x6kpp:f'({k}:{x6k}++{x6kpp})', range(3), with_fwd_idx=True)
[0, 1, 2, '(0:0++1)', '(2:2++(0:0++1))']

>>> mk_rvheap__fill_(lambda vidc,x6k,x6kpp:f'({vidc}:{x6k}++{x6kpp})', range(3), with_bwd_idc=True)
[0, 1, 2, '((5, 4, 2):0++1)', '((3, 2, 1):2++((5, 4, 2):0++1))']
>>> mk_rvheap__fill_(lambda k,vidc,x6k,x6kpp:f'({k}:{vidc}:{x6k}++{x6kpp})', range(3), with_fwd_idx=True, with_bwd_idc=True)
[0, 1, 2, '(0:(5, 4, 2):0++1)', '(2:(3, 2, 1):2++(0:(5, 4, 2):0++1))']


>>> __=mk_rvheap__Nothing_(None, ls:=[*range(3)], inplace=True)
>>> __ is ls
True
>>> ls
[0, 1, 2, None, None]
>>> __=mk_rvheap__fill_(lambda x,y:f'({x}++{y})', ls:=[*range(3)], inplace=True)
>>> __ is ls
True
>>> ls
[0, 1, 2, '(0++1)', '(2++(0++1))']



py_adhoc_call   seed.data_funcs.heap.heap_shape   @f
]]]'''#'''
__all__ = r'''
heap_shape5num_leafs_

mk_rvheap__Nothing_
mk_rvheap__fill_


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.math.floor_ceil_tools.fc_log import floor_log2
    from itertools import repeat

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def heap_shape5num_leafs_(num_leafs, /):
    # [[len4heap == num_leafs == 0]or[len4heap +1 == 2*num_leafs]]
    # [len4heap == max(0,-1+2*num_leafs)]
    check_int_ge(0, num_leafs)
    L = num_leafs
    r'''[[[
    [num_layers >= 1]
    [L >= 2]:
        [num_layers >= 2]
        [L6bottom > 0]
        [L6higher >= 0]
        [L6higher +L6bottom == L]
        [L6higher +ceil(L6bottom/2) <= 2**(num_layers-2) < 1+L6higher +ceil((-1+L6bottom)/2)]
            #L6higher极大化
        [ceil(L6bottom/2) < 1+ceil((-1+L6bottom)/2)]
        * [L6bottom%2 == 0]:
            [(L6bottom///2) < 1+L6bottom///2]
            ok
        * [L6bottom%2 == 1]:
            [(1+L6bottom)/2 < 1+(-1+L6bottom)/2]
            _L
        [L6bottom%2 == 0]
        [L6higher +(L6bottom///2) <= 2**(num_layers-2) < 1+L6higher +(L6bottom///2)]
        [L6higher +(L6bottom///2) == 2**(num_layers-2)]
        [h := (L6bottom///2)]
        [h > 0]
        [2*h +L6higher == L]
        [L6higher == (L -2*h)]
        [(L -2*h) +h == 2**(num_layers-2)]
        [(L -h) == 2**(num_layers-2)]
        !! [h > 0]
        [(L -1) >= 2**(num_layers-2)]
        !! L6higher极大化
        => h极小化
        => num_layers极大化
        [(num_layers-2) == floor_log2(L-1)]
        [num_layers == 2+floor_log2(L-1)]
        [h == L -2**(num_layers-2)]
        [L6bottom == 2*h]
        [sz == -1+2**(-1+num_layers) +L6bottom]
        [sz == -1+2*2**(-2+num_layers) +L6bottom]
        [sz == -1+2*(L-h) +2*h]
        [sz == -1+2*L]
    #]]]'''#'''
    if L == 0:
        num_layers = 0
        L6bottom = 0
    elif L >= 2:
        num_layers = 2+floor_log2(L-1)
        h = L -2**(num_layers-2)
        L6bottom = 2*h
        h&1 #odd
    else:
        assert L == 1
        num_layers = 1
        L6bottom = 1
    #L6higher = L -L6bottom
    #sz = -1+2**max(0, -1+num_layers) +L6bottom
    sz = max(0, -1+2*L)
    #sz4pad = sz -L
    ####
    num_leafs6bottom = L6bottom
    len4heap = sz
    ####
    assert (num_leafs6bottom&1 == 0) ^ (num_leafs == 1)
    assert not num_leafs > 1 or (num_leafs6bottom//2) + (num_leafs -num_leafs6bottom) == 2**(num_layers-2)
    assert not num_leafs > 1 or num_leafs6bottom&1 == 0
    assert not num_leafs > 1 or num_leafs > 1
    assert not num_leafs == 1 or num_leafs == 1
    assert not num_leafs == 0 or num_leafs == 0
    assert len4heap == 0 or len4heap&1 == 1
    assert len4heap == 0 or len4heap == -1 +2*num_leafs
    # [[len4heap == num_leafs == 0]or[len4heap +1 == 2*num_leafs]]
    # [len4heap == max(0,-1+2*num_leafs)]
    ####
    heap_shape = (len4heap, num_layers, num_leafs6bottom)
    return heap_shape


def mk_rvheap__Nothing_(Nothing, leafs, /, *, inplace=False):
    rvheap = [*leafs] if not inplace else leafs
    num_leafs = len(rvheap)
    (len4heap, num_layers, num_leafs6bottom) = heap_shape5num_leafs_(num_leafs)
    sz4pad = len4heap -num_leafs
    #rvheap += [Nothing]*sz4pad
    rvheap.extend(repeat(Nothing, sz4pad))
    assert len4heap == len(rvheap)
    return rvheap

def mk_rvheap__fill_(parent5children_, leafs, /, *, inplace=False, with_fwd_idx=False, with_bwd_idc=False):
    r'''[[[
    [k%2 == 0][sz >= sz-k == vj == 1+vi > vi == 2*vparent > vparent >= 1]
    [node6k is node6vj is rvheap8vj2node[-vj] is rvheap8vj2node[k]]

    [not with_fwd_idx][not with_bwd_idc]:
        def parent5children_(node6vj, node6vi, /):
    [with_fwd_idx][not with_bwd_idc]:
        def parent5children_(k, node6vj, node6vi, /):
    [not with_fwd_idx][with_bwd_idc]:
        def parent5children_(bwd_idc, node6vj, node6vi, /):
    [with_fwd_idx][with_bwd_idc]:
        def parent5children_(k, bwd_idc, node6vj, node6vi, /):
            (vj, vi, vparent) = bwd_idc

    #]]]'''#'''
    rvheap8vj2node = [*leafs] if not inplace else leafs
    num_leafs = len(rvheap8vj2node)
    (len4heap, num_layers, num_leafs6bottom) = heap_shape5num_leafs_(num_leafs)
    sz4pad = len4heap -num_leafs
    # !! [[len4heap == num_leafs == 0]or[len4heap +1 == 2*num_leafs]]
    # !! [sz4pad == len4heap -num_leafs]
    # [sz4pad == max(0, -1+num_leafs)]
    sz = len4heap
    if not sz:
        return rvheap8vj2node
    assert sz&1 #odd
    # [sz%2 == 1]
    # [sz > 0]
    # [sz == (-1+2*num_leafs)]
    # [sz4pad == (-1+num_leafs)]

    def idc5k_(k, /):
        if with_fwd_idx:
            yield k
        if not with_bwd_idc:
            return
        # [k <= 2*sz4pad-2]
        # [k%2 == 0]
        # [sz%2 == 1]
        # [sz > 0]
        # [sz == (-1+2*num_leafs)]
        # [sz4pad == (-1+num_leafs)]
        # [k <= 2*sz4pad-2 == -2+2*(-1+num_leafs) == -3+sz]
        # [0 <= k <= -3+sz]

        vj = sz -k
        # [k +vj == sz]
        # !! [0 <= k <= -3+sz]
        # [sz >= vj >= 3]
        # !! [sz%2 == 1]
        # !! [k%2 == 0]
        # [vj%2 == 1]
        # [sz >= vj > 2]
        vi = vj -1
        # [sz > vi >= 2]
        vparent = vi >> 1
        # [sz > vi > vparent >= 1]
        # [sz >= sz-k == vj == 1+vi > vi == 2*vparent > vparent >= 1]
        #
        # [k%2 == 0][sz >= sz-k == vj == 1+vi > vi == 2*vparent > vparent >= 1]
        # [node6k is node6vj is rvheap8vj2node[-vj] is rvheap8vj2node[k]]
        yield (vj, vi, vparent)
        return

    if not (with_fwd_idx or with_bwd_idc):
        def idc5k_(k, /):
            return ''

    ls = rvheap8vj2node
    for k in range(0, 2*sz4pad, 2):
        # [k <= 2*sz4pad-2]
        # [k%2 == 0]
        node6vj = node6k = ls[k]
        node6vi = node6kpp = ls[1+k]
        idc = idc5k_(k)
        node6parent = parent5children_(*idc, node6vj, node6vi)
        # parent = len(ls)
        # vparent = sz -parent
        ls.append(node6parent)
    rvheap8vj2node
    assert sz == len(rvheap8vj2node)
    return rvheap8vj2node



    r'''[[[
    rvheap8vj2node = mk_rvheap__Nothing_(Nothing, leafs)
    sz = len(rvheap8vj2node)
    assert sz&1 #odd
    for vj in range(sz, 2, -2):
        # [vj%2 == 1]
        # [sz >= vj > 2]
        vi = vj -1
        # [sz > vi >= 2]
        vparent = vi >> 1
        # [sz > vi > vparent >= 1]
        node6vj = rvheap8vj2node[-vj]
        node6vi = rvheap8vj2node[-vi]
        node6vparent = parent5children_(node6vj, node6vi)
        rvheap8vj2node[-vparent] = node6vparent
    rvheap8vj2node
    #]]]'''#'''

__all__
from seed.data_funcs.heap.heap_shape import heap_shape5num_leafs_, mk_rvheap__fill_, mk_rvheap__Nothing_
from seed.data_funcs.heap.heap_shape import *
