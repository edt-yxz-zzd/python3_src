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
>>> def show_(sz, /, **kwds):
...     for (u, rv_js, rv_ps, imay_new_prime) in islice(iter_unsorted_squarefree_uints_(to_view_primes=True, **kwds), 0, sz):
...         print((u, tuple(reversed(rv_js)), tuple(reversed(rv_ps)), imay_new_prime))
>>> show_(18)
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

>>> [*islice(iter_unsorted_squarefree_uints_(may_prime2ok_=lambda p:p>2), 0, 18)]
[1, 3, 15, 5, 35, 105, 21, 7, 77, 231, 1155, 385, 55, 165, 33, 11, 143, 429]
>>> [*islice(iter_unsorted_squarefree_uints_([2,3,5]), 0, 18)]
[1, 2, 6, 3, 15, 30, 10, 5]
>>> [*islice(iter_unsorted_squarefree_uints_([5,3,2]), 0, 18)] #disorder
[1, 5, 15, 3, 6, 30, 10, 2]
>>> [*islice(iter_unsorted_squarefree_uints_([5,7,3,2]), 0, 18)] #disorder
[1, 5, 35, 7, 21, 105, 15, 3, 6, 30, 210, 42, 14, 70, 10, 2]

>>> [*islice(iter_unsorted_squarefree_uints_(may_squarefree7resume=1), 0, 18-1)]
[2, 6, 3, 15, 30, 10, 5, 35, 70, 210, 105, 21, 42, 14, 7, 77, 154]
>>> [*islice(iter_unsorted_squarefree_uints_(may_squarefree7resume=2), 0, 18-2)]
[6, 3, 15, 30, 10, 5, 35, 70, 210, 105, 21, 42, 14, 7, 77, 154]
>>> [*islice(iter_unsorted_squarefree_uints_(may_squarefree7resume=6), 0, 18-3)]
[3, 15, 30, 10, 5, 35, 70, 210, 105, 21, 42, 14, 7, 77, 154]
>>> [*islice(iter_unsorted_squarefree_uints_(may_squarefree7resume=3), 0, 18-4)]
[15, 30, 10, 5, 35, 70, 210, 105, 21, 42, 14, 7, 77, 154]
>>> [*islice(iter_unsorted_squarefree_uints_(may_squarefree7resume=15), 0, 18-5)]
[30, 10, 5, 35, 70, 210, 105, 21, 42, 14, 7, 77, 154]

>>> show_(18-11, may_squarefree7resume=210)
(105, (1, 2, 3), (3, 5, 7), -1)
(21, (1, 3), (3, 7), -1)
(42, (0, 1, 3), (2, 3, 7), -1)
(14, (0, 3), (2, 7), -1)
(7, (3,), (7,), -1)
(77, (3, 4), (7, 11), 11)
(154, (0, 3, 4), (2, 7, 11), -1)

>>> show_(1, new_resume=True, may_squarefree7resume=1)
(1, (), (), -1)
>>> show_(1, new_resume=True, may_squarefree7resume=2)
(2, (0,), (2,), 2)
>>> show_(1, new_resume=True, may_squarefree7resume=6)
(6, (0, 1), (2, 3), 3)
>>> show_(1, new_resume=True, may_squarefree7resume=3)
(3, (1,), (3,), -1)
>>> show_(1, new_resume=True, may_squarefree7resume=15)
(15, (1, 2), (3, 5), 5)
>>> show_(1, new_resume=True, may_squarefree7resume=30)
(30, (0, 1, 2), (2, 3, 5), -1)
>>> show_(1, new_resume=True, may_squarefree7resume=10)
(10, (0, 2), (2, 5), -1)
>>> show_(1, new_resume=True, may_squarefree7resume=5)
(5, (2,), (5,), -1)
>>> show_(1, new_resume=True, may_squarefree7resume=35)
(35, (2, 3), (5, 7), 7)
>>> show_(1, new_resume=True, may_squarefree7resume=70)
(70, (0, 2, 3), (2, 5, 7), -1)
>>> show_(1, new_resume=True, may_squarefree7resume=210)
(210, (0, 1, 2, 3), (2, 3, 5, 7), -1)



test:reset imay_new_prime
>>> show_(2, new_resume=True, may_squarefree7resume=1)
(1, (), (), -1)
(2, (0,), (2,), 2)
>>> show_(2, new_resume=True, may_squarefree7resume=2)
(2, (0,), (2,), 2)
(6, (0, 1), (2, 3), 3)
>>> show_(2, new_resume=True, may_squarefree7resume=6)
(6, (0, 1), (2, 3), 3)
(3, (1,), (3,), -1)




>>> show_(1, may_squarefree7resume=1)
(2, (0,), (2,), 2)
>>> show_(1, new_resume=True, may_squarefree7resume=1)
(1, (), (), -1)
>>> show_(1, neg_resume_ok=True, may_squarefree7resume=-1)
(1, (), (), -1)
>>> show_(1, neg_resume_ok=True, new_resume=True, may_squarefree7resume=-1)
(2, (0,), (2,), 2)
>>> show_(1, may_squarefree7resume=-1)
Traceback (most recent call last):
    ...
ValueError: -1
>>> show_(1, new_resume=True, may_squarefree7resume=-1)
Traceback (most recent call last):
    ...
ValueError: -1







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
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.math.prime_sieve.primes_ge_lt import iter_filter4primes_ge_lt_
    from seed.math.Gray_code import 步退冫爻位栈冃孤变码扌, 步进冫爻位栈冃孤变码扌, 趃步退冫爻位栈冃孤变码扌, 趃步进冫爻位栈冃孤变码扌
    from itertools import islice
    from seed.types.view.View import SeqView
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def _resume(it8ps, squarefree7resume, /):
    assert squarefree7resume > 0
    u = squarefree7resume
    # [u > 0]
    _j2using = []
    j2p = []
    stk = [] # reversed js
    if not u == 1:
        # [u > 1]
        for j, p in enumerate(it8ps):
            # [u > 1]
            assert u >= p
            # [u >= p]
            j2p.append(p)
            b = u%p == 0
            _j2using.append(b)
            if b:
                stk.append(j)
                u //= p
                # [u >= 1]
                if u == 1:break
                # [u > 1]
                if u%p == 0:raise Exception('non-squarefree', squarefree7resume, p)
                # [u > 1]
            # [u > 1]
            #MAYBE disorder:assert u > p # [u > p]
    assert u == 1
    stk.reverse() # reversed js
    return (_j2using, j2p, stk)
def _std(squarefree7resume, new_resume, neg_resume_ok, /):
    new_resume = bool(new_resume)
    check_type_is(int, squarefree7resume)
    if squarefree7resume == 0:raise ValueError(squarefree7resume)
    if squarefree7resume < 0:
        if not neg_resume_ok:raise ValueError(squarefree7resume)
        squarefree7resume = -squarefree7resume
        new_resume = not new_resume
    return (squarefree7resume, new_resume)
#resume,restore,snapshot,breakpoint,setup
def iter_unsorted_squarefree_uints_(may_primes=None, /, *, to_view_primes=False, may_prime2ok_=None, may_squarefree7resume=None, new_resume=False, neg_resume_ok=False):
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
            # ^StopIteration
        if to_view_primes:
            imay_new_prime = j2p[-1]
        assert 1 <= len(stk) <= 2
        assert stk[0] == j
        assert len(stk) == 1 or stk[1] == j-1
        return _j2using[j]

    it8ps = iter(may_primes) if not None is may_primes else iter_filter4primes_ge_lt_(0, 1<<81)
    if not None is may_prime2ok_:
        prime2ok_ = may_prime2ok_
        it8ps = filter(prime2ok_, it8ps)
    it8ps

    if not None is (squarefree7resume:=may_squarefree7resume):
        (squarefree7resume, new_resume) = _std(squarefree7resume, new_resume, neg_resume_ok)
        (_j2using, j2p, stk) = _resume(it8ps, squarefree7resume)
        u = squarefree7resume
        777;u0_is_new = new_resume
    else:
        _j2using = []
        j2p = []
        stk = [] # reversed js
        u = 1
        777;u0_is_new = True

    if to_view_primes:
        rv_js = stk # reversed js
        rv_ps = [j2p[j] for j in rv_js] # reversed primes
        vw4rv_js = SeqView(rv_js)
        vw4rv_ps = SeqView(rv_ps)
        # !! u0_is_new <= [u==1]
        if u0_is_new and stk and 1+stk[0] == len(j2p) and (stk == [0] or len(stk) == 2 and stk[0] == 1+stk[1]):
            imay_new_prime = j2p[-1]
        else:
            imay_new_prime = -1

    if u0_is_new:
        777; yield u if not to_view_primes else (u, vw4rv_js, vw4rv_ps, imay_new_prime)
    for j in 趃步进冫爻位栈冃孤变码扌(stk):
        #########
        if to_view_primes and not imay_new_prime == -1:
            imay_new_prime = -1
        #########
        try:
            b = j2using_(j) #update imay_new_prime
        except StopIteration:
            return
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
                if rv_js[-1] == j:
                    #MAYBE disorder:if not rv_ps or rv_ps[-1] > p6j:
                    rv_ps.append(p6j)
                elif rv_js[-2] == j:
                    rv_ps.insert(-1, p6j)
                else:
                    raise Exception(stk, rv_ps, p6j)
            #rv_ps
        #########
        yield u if not to_view_primes else (u, vw4rv_js, vw4rv_ps, imay_new_prime)
        #########


__all__
from seed.math.iter_unsorted_squarefree_uints import iter_unsorted_squarefree_uints_ # ++kw:to_view_primes => Iter (u, vw4rv_js, vw4rv_ps, imay_new_prime)  # ++kw:may_prime2ok_{filter} # ++arg:may_primes # ++kw:may_squarefree7resume,kw:new_resume,kw:neg_resume_ok
from seed.math.iter_unsorted_squarefree_uints import *
