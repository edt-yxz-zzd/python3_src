#__all__:goto
r'''[[[
e ../../python3_src/seed/math/iter_unsorted_squarefree_uints.py
view ../../python3_src/seed/math/Gray_code.py

seed.math.iter_unsorted_squarefree_uints
py -m nn_ns.app.debug_cmd   seed.math.iter_unsorted_squarefree_uints -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.iter_unsorted_squarefree_uints:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/BinaryQuadraticForm.py
view ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method.py
]]


'#'; __doc__ = r'#'
>>> [*islice(iter_unsorted_squarefree_uints_(), 0, 18)]
[1, 2, 6, 3, 15, 30, 10, 5, 35, 70, 210, 105, 21, 42, 14, 7, 77, 154]
>>> for (u, rv_js, rv_ps, imay_new_prime) in islice(iter_unsorted_squarefree_uints_(to_view_primes=True), 0, 18):
...     print((u, tuple(reversed(rv_js)), tuple(reversed(rv_ps)), imay_new_prime))
(1, (), (), -1)
(2, (0,), (2,), 2)
(6, (0, 1), (2, 3), 3)
(3, (1,), (3,), -1)
(15, (1, 2), (3, 5), 5)
(30, (0, 1, 2), (2, 3, 5), -1)
(10, (0, 2), (2, 5), -1)
(5, (2,), (5,), -1)
(35, (2, 3), (5, 7), 7)
(70, (0, 2, 3), (2, 5, 7), -1)
(210, (0, 1, 2, 3), (2, 3, 5, 7), -1)
(105, (1, 2, 3), (3, 5, 7), -1)
(21, (1, 3), (3, 7), -1)
(42, (0, 1, 3), (2, 3, 7), -1)
(14, (0, 3), (2, 7), -1)
(7, (3,), (7,), -1)
(77, (3, 4), (7, 11), 11)
(154, (0, 3, 4), (2, 7, 11), -1)



py_adhoc_call   seed.math.iter_unsorted_squarefree_uints   @f
]]]'''#'''
__all__ = r'''
iter_unsorted_squarefree_uints_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.prime_sieve.primes_ge_lt import iter_filter4primes_ge_lt_
    from seed.math.Gray_code import 步退冫爻位栈冃孤变码扌, 步进冫爻位栈冃孤变码扌, 趃步退冫爻位栈冃孤变码扌, 趃步进冫爻位栈冃孤变码扌
    from itertools import islice
    from seed.types.view.View import SeqView
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def iter_unsorted_squarefree_uints_(*, to_view_primes=False):
    '-> (unsorted-Iter u/uint{>=1}{squarefree}) if not to_view_primes else (unsorted-Iter (u/uint{>=1}{squarefree}, rv_js/[uint]{reversed}{[u==II(PRIMES[j] for j in rv_js)]}, rv_ps/[prime]{reversed}{[u==II(rv_ps)]}, imay prime{new}))'
    def j2using_(j, /):
        nonlocal imay_new_prime
        try:
            return _j2using[j]
        except IndexError:
            pass
        assert j == len(_j2using)
        assert j == len(j2p)
        _j2using.append(False)
        777;j2p.append(next(it8ps))
        if to_view_primes:
            imay_new_prime = j2p[-1]
        return _j2using[j]

    it8ps = iter_filter4primes_ge_lt_(0, 1<<81)
    _j2using = []
    j2p = []
    stk = [] # reversed js
    if to_view_primes:
        rv_js = stk # reversed js
        rv_ps = [] # reversed primes
        vw4rv_js = SeqView(rv_js)
        vw4rv_ps = SeqView(rv_ps)
        imay_new_prime = -1

    u = 1
    777; yield u if not to_view_primes else (u, vw4rv_js, vw4rv_ps, imay_new_prime)
    for j in 趃步进冫爻位栈冃孤变码扌(stk):
        b = j2using_(j) #update imay_new_prime
        777;_j2using[j] = not b
        777;p6j = j2p[j]
        #########
        if b:
            u //= p6j
        else:
            u *= p6j
        #u
        #########
        if to_view_primes:
            if b:
                if rv_ps[-1] == p6j:
                    rv_ps.pop()
                elif rv_ps[-2] == p6j:
                    del rv_ps[-2]
                else:
                    raise Exception(stk, rv_ps, p6j)
            else:
                if not rv_ps or rv_ps[-1] > p6j:
                    rv_ps.append(p6j)
                else:
                    rv_ps.insert(-1, p6j)
            #rv_ps
        #########
        yield u if not to_view_primes else (u, vw4rv_js, vw4rv_ps, imay_new_prime)
        #########
        if to_view_primes and not imay_new_prime == -1:
            imay_new_prime = -1
        #########


__all__
from seed.math.iter_unsorted_squarefree_uints import iter_unsorted_squarefree_uints_ # kw:to_view_primes => Iter (u, vw4rv_js, vw4rv_ps, imay_new_prime)
from seed.math.iter_unsorted_squarefree_uints import *
