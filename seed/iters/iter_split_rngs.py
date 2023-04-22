#__all__:goto
r'''[[[
e ../../python3_src/seed/iters/iter_split_rngs.py


seed.iters.iter_split_rngs
py -m nn_ns.app.debug_cmd   seed.iters.iter_split_rngs -x
py -m nn_ns.app.doctest_cmd seed.iters.iter_split_rngs:__doc__ -ff -v

>>> from seed.iters.iter_split_rngs import iter_ok_rngs_if_, iter_split_rngs_if_, iter_split_blocks5seq_if_, split_blocks5seq_if_
>>> split_blocks5seq_if_(bool, [])
[[]]
>>> split_blocks5seq_if_(bool, [0])
[[0]]
>>> split_blocks5seq_if_(bool, [1])
[[], [1], []]
>>> split_blocks5seq_if_(bool, [0,0])
[[0, 0]]
>>> split_blocks5seq_if_(bool, [1,1])
[[], [1, 1], []]


>>> split_blocks5seq_if_(bool, [0,0,1,1])
[[0, 0], [1, 1], []]
>>> split_blocks5seq_if_(bool, [1,1,0,0])
[[], [1, 1], [0, 0]]





#]]]'''
__all__ = r'''
iter_ok_rngs_if_
    iter_split_rngs_if_
        iter_split_blocks5seq_if_
            split_blocks5seq_if_

'''.split()#'''
__all__

from seed.data_funcs.rngs import sorted_ints_to_iter_nontouch_ranges

def iter_ok_rngs_if_(f, it, /):
    '(a->bool) -> Iter a -> Iter (i,j) # result are ok rngs'
    rngs4ok = sorted_ints_to_iter_nontouch_ranges(i for i, x in enumerate(it) if f(x))
    return rngs4ok

def iter_split_rngs_if_(end, f, it, /):
    '(a->bool) -> Iter a -> Iter (i,j) # islice(result, 1,None,2) are ok rngs'
    i = 0
    for j, k in iter_ok_rngs_if_(f, it):
        yield i, j
        yield j, k
        i = k
    yield i, end

def iter_split_blocks5seq_if_(f, ls, /):
    '(a->bool) -> [a] -> Iter [a] # result[1::2] are ok blocks'
    ls[:0]
    for i, j in iter_split_rngs_if_(len(ls), f, ls):
        yield ls[i:j]

def split_blocks5seq_if_(f, ls, /):
    '(a->bool) -> [a] -> [[a]] # result[1::2] are ok blocks'
    lsls = [*iter_split_blocks5seq_if_(f, ls)]
    assert len(lsls) & 1
    return lsls



from seed.iters.iter_split_rngs import iter_ok_rngs_if_, iter_split_rngs_if_, iter_split_blocks5seq_if_, split_blocks5seq_if_
from seed.iters.iter_split_rngs import *
