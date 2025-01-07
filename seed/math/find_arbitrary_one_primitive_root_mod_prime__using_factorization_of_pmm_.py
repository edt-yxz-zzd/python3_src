#__all__:goto
r'''[[[
e ../../python3_src/seed/math/find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_.py

seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_
py -m nn_ns.app.debug_cmd   seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_:__doc__ -ht # -ff -df

>>> [*_iter_sorted_primitive_roots_mod_prime_(17, {2:4})]
[3, 5, 6, 7, 10, 11, 12, 14]
>>> _find_the_min_primitive_root_mod_prime_(17, {2:4})
3
>>> _find_arbitrary_one_primitive_root_mod_prime_(17, {2:4})
3
>>> [*_iter_sorted_primitive_roots_mod_prime_(101, {2:2, 5:2})]
[2, 3, 7, 8, 11, 12, 15, 18, 26, 27, 28, 29, 34, 35, 38, 40, 42, 46, 48, 50, 51, 53, 55, 59, 61, 63, 66, 67, 72, 73, 74, 75, 83, 86, 89, 90, 93, 94, 98, 99]
>>> _find_arbitrary_one_primitive_root_mod_prime_(101, {2:2, 5:2})
2

>>> 2**75 * 3**0 * 5**1  +1
188894659314785808547841
>>> 2**5 * 3**48 * 5**0  +1
2552526178459920315627553
>>> 2**1 * 3**1 * 5**33  +1
698491930961608886718751
>>> _find_arbitrary_one_primitive_root_mod_prime_(188894659314785808547841, {2:75, 5:1})
3
>>> _find_arbitrary_one_primitive_root_mod_prime_(2552526178459920315627553, {2:5, 3:48})
5
>>> _find_arbitrary_one_primitive_root_mod_prime_(698491930961608886718751, {2:1, 3:1, 5:33})
7




>>> find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_({2:1, 3:1, 5:33})
7
>>> find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_({2:1, 3:1, 5:33}, 698491930961608886718751)
7

py_adhoc_call   seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_   @find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_ '={2:1,3:1}'
3

]]]'''#'''
__all__ = r'''
find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_
    find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_
        iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#from seed.math.discrete_logarithm import _find_arbitrary_one_primitive_root_mod_prime_, _find_the_min_primitive_root_mod_prime_, _iter_sorted_primitive_roots_mod_prime_
#from seed.math.discrete_logarithm import find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_, find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_, iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_

from seed.math.II import II, II__p2e_
___end_mark_of_excluded_global_names__0___ = ...


def _API():
    #API:
    def find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, /):
        'factorization{p-1} -> may p -> arbitrary primitive_root%p'
    def find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, /):
        'factorization{p-1} -> may p -> min primitive_root%p'
    def iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, /):
        'factorization{p-1} -> may p -> sorted-Iter primitive_root%p'


    def _find_arbitrary_one_primitive_root_mod_prime_(p, factorization_of_pmm, /):
        'p -> factorization{p-1} -> arbitrary primitive_root%p'
    def _find_the_min_primitive_root_mod_prime_(p, factorization_of_pmm, /):
        'p -> factorization{p-1} -> min primitive_root%p'
    def _iter_sorted_primitive_roots_mod_prime_(p, factorization_of_pmm, /):
        'p -> factorization{p-1} -> sorted-Iter primitive_root%p'
_API




def _p5factorization_of_pmm_ex_(factorization_of_pmm, may_p, /):
    p = 1+II__p2e_(factorization_of_pmm) if may_p is None else may_p
    return p
#def find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, /):
    #'factorization{p-1} -> may p -> arbitrary primitive_root%p'
def find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, /):
    'factorization{p-1} -> may p -> min primitive_root%p'
    p = _p5factorization_of_pmm_ex_(factorization_of_pmm, may_p)
    return _find_arbitrary_one_primitive_root_mod_prime_(p, factorization_of_pmm)
find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ = find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_
    #'factorization{p-1} -> may p -> arbitrary primitive_root%p'
def iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, /):
    'factorization{p-1} -> may p -> sorted-Iter primitive_root%p'
    p = _p5factorization_of_pmm_ex_(factorization_of_pmm, may_p)
    return _iter_sorted_primitive_roots_mod_prime_(p, factorization_of_pmm)

#def _find_arbitrary_one_primitive_root_mod_prime_(p, factorization_of_pmm, /):
    #'p -> factorization{p-1} -> arbitrary primitive_root%p'
def _find_the_min_primitive_root_mod_prime_(p, factorization_of_pmm, /):
    'p -> factorization{p-1} -> min primitive_root%p'
    for g in _iter_sorted_primitive_roots_mod_prime_(p, factorization_of_pmm):
        break
    else:
        raise 000
    return g
_find_arbitrary_one_primitive_root_mod_prime_ = _find_the_min_primitive_root_mod_prime_
    #'p -> factorization{p-1} -> arbitrary primitive_root%p'
def _iter_sorted_primitive_roots_mod_prime_(p, factorization_of_pmm, /):
    'p -> factorization{p-1} -> sorted-Iter primitive_root%p'
    if p == 2:
        yield 1
        return
    # [p >= 3]
    # [p-1 >= 2]
    pmm = p-1
    # [pmm >= 2]
    e0 = pmm//II(factorization_of_pmm.keys())
    II_q = II(q for q in factorization_of_pmm)
    phi_p = e0 * II_q
    assert phi_p == pmm
    II_qmm = II(q-1 for q in factorization_of_pmm)
    phi_pmm = e0 * II_qmm
    #gs = []
    num_gs = 0
    ps = sorted(factorization_of_pmm.items())
    assert ps
        # !! [p-1 >= 2]
    #bug: p=2,3: for g in range(2, pmm//2 +1):
    for g in range(2, p):
        #base0 = pow(g, e0, p)
        base0 = g
        for q, e in ps:
            for _ in range(e-1):
                base0 = pow(base0, q, p)
                if base0 == 1:
                    break
            if base0 == 1:
                break
        else:
            assert not base0 == 1
        if base0 == 1:
            continue

        for i in range(len(ps)):
            #base1 = pow(g, pmm//q, p)
            base1 = base0
            for q, _ in ps[i+1:]:
                base1 = pow(base1, q, p)
                if base1 == 1:
                    break
            if base1 == 1:
                break
            q, _ = ps[i]
            base0 = pow(base0, q, p)
        else:
            assert base0 == 1, ((p, factorization_of_pmm), phi_p, ps, base0, pow(g, phi_p, p))
        if base1 == 1:
            #bug:assert not base0 == 1
            continue
        assert base0 == 1
        yield g
        #gs.append(g)
        num_gs += 1
    #assert len(gs) == phi_pmm
    assert num_gs == phi_pmm


__all__
if 1:from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import _find_arbitrary_one_primitive_root_mod_prime_, _find_the_min_primitive_root_mod_prime_, _iter_sorted_primitive_roots_mod_prime_
from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_, find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_, iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_

from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import *
