#__all__:goto
r'''[[[
e ../../python3_src/seed/algo/partial_cmp.py

(+1|-1|0|...)
weak:(>0|<0|0|...)

seed.algo.partial_cmp
py -m nn_ns.app.debug_cmd   seed.algo.partial_cmp -x
py -m nn_ns.app.doctest_cmd seed.algo.partial_cmp:__doc__ -ff -v
py_adhoc_call   seed.algo.partial_cmp   @f
#]]]'''
__all__ = r'''
    partial_cmp4py
    mk_partial_cmp4array_
        partial_cmp4array__py_ord
    mk_partial_cmp4tuple_

    mk_partial_cmp_result5subresults_
'''.split()#'''
__all__

from itertools import chain

#def total_cmp4py(lhs, rhs, /):
def partial_cmp4py(lhs, rhs, /):
    if lhs < rhs:
        return -1
    if lhs > rhs:
        return +1
    if lhs == rhs:
        return 0
    return ...
def mk_partial_cmp4array_(sub_partial_cmp, /):
    def partial_cmp(lhs, rhs, /):
        return mk_partial_cmp_result5subresults_(chain(map(sub_partial_cmp, lhs, rhs), [len(lhs)-len(rhs)]))
    return partial_cmp
partial_cmp4array__py_ord = mk_partial_cmp4array_(partial_cmp4py)
def mk_partial_cmp4tuple_(*sub_partial_cmps):
    def partial_cmp(lhs, rhs, /):
        if not len(lhs) == len(rhs) == len(sub_partial_cmps): raise TypeError(len(lhs), len(rhs), len(sub_partial_cmps))
        return mk_partial_cmp_result5subresults_(f(a,b) for f,a,b in zip(sub_partial_cmps, lhs, rhs))
    return partial_cmp
def mk_partial_cmp_result5subresults_(iter_sub_partial_cmp_results, /):
    acc = 0
    for r in iter_sub_partial_cmp_results:
        if r is ...:
            return ...
        elif r == 0:
            pass
        elif r < 0:
            if acc > 0:
                return ...
            acc = -1
        elif r > 0:
            if acc < 0:
                return ...
            acc = +1
        else:
            raise 000
    return acc



__all__


from seed.algo.partial_cmp import partial_cmp4py, partial_cmp4array__py_ord
from seed.algo.partial_cmp import mk_partial_cmp4array_, mk_partial_cmp4tuple_
from seed.algo.partial_cmp import mk_partial_cmp_result5subresults_
from seed.algo.partial_cmp import *
