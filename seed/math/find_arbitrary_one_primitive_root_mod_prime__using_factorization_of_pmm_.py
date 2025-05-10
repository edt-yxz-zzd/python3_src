#__all__:goto
r'''[[[
e ../../python3_src/seed/math/find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_.py

seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_
py -m nn_ns.app.debug_cmd   seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_:__doc__ -ht # -ff -df


:.+1,$s/\(pseudo_\)\@<!primitive_roots_mod_prime_power/pseudo_\0/g
    primitive_roots_mod_prime
    primitive_roots_mod_prime_square
    pseudo_primitive_roots_mod_prime_power
    pseudo_primitive_roots_mod_zpow
    primitive_roots_mod_old_prime_power


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





######################
>>> [*iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_({}, 2)]
[1]
>>> [*iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_({2:1}, 3)]
[2]
>>> [*iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_({2:1,3:1,5:1}, 31)]
[3, 11, 12, 13, 17, 21, 22, 24]
>>> [*iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_({2:2,3:1,5:1}, 61)]
[2, 6, 7, 10, 17, 18, 26, 30, 31, 35, 43, 44, 51, 54, 55, 59]
>>> [*iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_({2:3,11:1}, 89)]
[3, 6, 7, 13, 14, 15, 19, 23, 24, 26, 27, 28, 29, 30, 31, 33, 35, 38, 41, 43, 46, 48, 51, 54, 56, 58, 59, 60, 61, 62, 63, 65, 66, 70, 74, 75, 76, 82, 83, 86]






######################
>>> list_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_({}, 2)
[1]
>>> list_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_({2:1}, 3)
[2]
>>> list_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_({2:1,3:1,5:1}, 31)
[3, 11, 12, 13, 17, 21, 22, 24]
>>> list_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_({2:2,3:1,5:1}, 61)
[2, 6, 7, 10, 17, 18, 26, 30, 31, 35, 43, 44, 51, 54, 55, 59]
>>> list_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_({2:3,11:1}, 89)
[3, 6, 7, 13, 14, 15, 19, 23, 24, 26, 27, 28, 29, 30, 31, 33, 35, 38, 41, 43, 46, 48, 51, 54, 56, 58, 59, 60, 61, 62, 63, 65, 66, 70, 74, 75, 76, 82, 83, 86]






######################
>>> [*iter_unsorted_primitive_roots_mod_prime__using_factorization_of_pmm_({}, 2)]
[1]
>>> [*iter_unsorted_primitive_roots_mod_prime__using_factorization_of_pmm_({2:1}, 3)]
[2]
>>> [*iter_unsorted_primitive_roots_mod_prime__using_factorization_of_pmm_({2:1,3:1,5:1}, 31)]
[3, 17, 13, 24, 22, 12, 11, 21]
>>> [*iter_unsorted_primitive_roots_mod_prime__using_factorization_of_pmm_({2:2,3:1,5:1}, 61)]
[2, 6, 35, 18, 44, 54, 10, 30, 59, 55, 26, 43, 17, 7, 51, 31]
>>> [*iter_unsorted_primitive_roots_mod_prime__using_factorization_of_pmm_({2:3,11:1}, 89)]
[3, 27, 65, 51, 14, 66, 60, 6, 54, 41, 13, 28, 74, 43, 31, 19, 82, 26, 56, 59, 86, 62, 24, 38, 75, 23, 29, 83, 35, 48, 76, 61, 15, 46, 58, 70, 7, 63, 33, 30]

>>> sorted(iter_unsorted_primitive_roots_mod_prime__using_factorization_of_pmm_({2:1,3:1,5:1}, 31))
[3, 11, 12, 13, 17, 21, 22, 24]
>>> sorted(iter_unsorted_primitive_roots_mod_prime__using_factorization_of_pmm_({2:2,3:1,5:1}, 61))
[2, 6, 7, 10, 17, 18, 26, 30, 31, 35, 43, 44, 51, 54, 55, 59]
>>> sorted(iter_unsorted_primitive_roots_mod_prime__using_factorization_of_pmm_({2:3,11:1}, 89))
[3, 6, 7, 13, 14, 15, 19, 23, 24, 26, 27, 28, 29, 30, 31, 33, 35, 38, 41, 43, 46, 48, 51, 54, 56, 58, 59, 60, 61, 62, 63, 65, 66, 70, 74, 75, 76, 82, 83, 86]





>>> list(iter_unsorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_(6, {}, 2))
[3, 19, 35, 51, 5, 21, 37, 53, 11, 27, 43, 59, 13, 29, 45, 61]
>>> sorted(iter_unsorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_(6, {}, 2))
[3, 5, 11, 13, 19, 21, 27, 29, 35, 37, 43, 45, 51, 53, 59, 61]
>>> list(iter_unsorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_(4, {2:1}, 3))
[2, 11, 20, 29, 38, 47, 56, 65, 74, 5, 14, 23, 32, 41, 50, 59, 68, 77]
>>> sorted(iter_unsorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_(4, {2:1}, 3))
[2, 5, 11, 14, 20, 23, 29, 32, 38, 41, 47, 50, 56, 59, 65, 68, 74, 77]

>>> list(iter_unsorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_(3, {2:2}, 5))
[2, 27, 52, 77, 102, 8, 33, 58, 83, 108, 3, 28, 53, 78, 103, 12, 37, 62, 87, 112, 23, 48, 73, 98, 123, 17, 42, 67, 92, 117, 22, 47, 72, 97, 122, 13, 38, 63, 88, 113]
>>> sorted(iter_unsorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_(3, {2:2}, 5))
[2, 3, 8, 12, 13, 17, 22, 23, 27, 28, 33, 37, 38, 42, 47, 48, 52, 53, 58, 62, 63, 67, 72, 73, 77, 78, 83, 87, 88, 92, 97, 98, 102, 103, 108, 112, 113, 117, 122, 123]



py_adhoc_call   seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_   @find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_ '={2:1,3:1}'
3

]]]'''#'''
__all__ = r'''
find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_
    find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_
        iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_

list_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_
iter_unsorted_primitive_roots_mod_prime__using_factorization_of_pmm_



find_arbitrary_one_primitive_root_mod_prime_power__using_factorization_of_pmm_
iter_unsorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_
    list_sorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_


iter_unsorted_primitive_roots_mod_prime_square__using_factorization_of_pmm_
    list_sorted_primitive_roots_mod_prime_square__using_factorization_of_pmm_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#from seed.math.discrete_logarithm import _find_arbitrary_one_primitive_root_mod_prime_, _find_the_min_primitive_root_mod_prime_, _iter_sorted_primitive_roots_mod_prime_
#from seed.math.discrete_logarithm import find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_, find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_, iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_

from seed.math.II import II, II__p2e_
if 1:from seed.math.is_kth_primitive_root_mod_N__via_complete_factorization_k_ import _is_kth_primitive_root_mod_N__via_complete_factorization_k__ver2_
#def _is_kth_primitive_root_mod_N__via_complete_factorization_k__ver2_(k, q_e_pairs, N, r, /):
    # [2 <= r < N]
    # [k >= 2]
    # [len(qs) >= 1]
from seed.math.is_kth_primitive_root_mod_N__via_complete_factorization_k_ import check_kth_primitive_root_mod_N__via_complete_factorization_k_, is_kth_primitive_root_mod_N__via_complete_factorization_k_
#def check_kth_primitive_root_mod_N__via_complete_factorization_k_(may_k, factorization_of_k, N, r, /, *, _ver=2):
#    'may k/int{>=1} -> factorization{k} -> N/int{>=2} -> r/uint%N -> None if [k==min_order_mod_(N;r)] else ^ValueError'
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
def find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, /):
    'factorization{p-1} -> may p -> min primitive_root%p'
    p = _p5factorization_of_pmm_ex_(factorization_of_pmm, may_p)
    return _find_arbitrary_one_primitive_root_mod_prime_(p, factorization_of_pmm)
#old:find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ = find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_
    #'factorization{p-1} -> may p -> arbitrary primitive_root%p'
#old:def find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, /):
    #'factorization{p-1} -> may p -> arbitrary primitive_root%p'
def find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, may_arbitrary_one_primitive_root_modP=None, /):
    'factorization{p-1} -> may p -> may arbitrary_one_primitive_root%p -> arbitrary primitive_root%p'
    if may_arbitrary_one_primitive_root_modP is None:
        g = find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p)
    else:
        g = may_arbitrary_one_primitive_root_modP
        p = _p5factorization_of_pmm_ex_(factorization_of_pmm, may_p)
        if not 1 <= g < p:raise ValueError(p, g)
        pmm = p-1
        check_kth_primitive_root_mod_N__via_complete_factorization_k_(may_k:=pmm, factorization_of_pmm, p, g)
    return g

def find_arbitrary_one_primitive_root_mod_prime_power__using_factorization_of_pmm_(exp4Ppow, factorization_of_pmm, may_p=None, may_arbitrary_one_primitive_root_modP=None, may_ppow=None, may_arbitrary_one_primitive_root_modPpow=None, /):
    'exp4Ppow/int{>=1}{[[p==2]->[exp4Ppow<=2]]} -> factorization{p-1} -> may p -> may arbitrary_one_primitive_root%p -> may ppow{==p**exp4Ppow} -> may arbitrary_one_primitive_root%ppow -> arbitrary primitive_root%ppow'
    assert exp4Ppow >= 1
    assert factorization_of_pmm or exp4Ppow <= 2 #pseudo_primitive_root_modZpow{zpow>=8}
        #<==> assert not p==2 or exp4Ppow <= 2 #pseudo_primitive_root_modZpow{zpow>=8}
    ######################
    def f(exp4Ppow, p, g, /):
        if exp4Ppow == 1:
            return g
        assert exp4Ppow >= 2
        if exp4Ppow > 2:
            assert p > 2
            assert p&1
        exp4Ppow = 2
        pmm = p-1
        _pw = p**(exp4Ppow-1)
        ppow = p*_pw if may_ppow is None else may_ppow#p**exp4Ppow
        k = phi_ppow = pmm*_pw
        factorization_of_k = {p:exp4Ppow-1, **factorization_of_pmm}
        if not is_kth_primitive_root_mod_N__via_complete_factorization_k_(k, factorization_of_k, ppow, g):
            g += p
            assert is_kth_primitive_root_mod_N__via_complete_factorization_k_(k, factorization_of_k, ppow, g)
        g
        return g
    #end-def f(exp4Ppow, p, g, /):
    ######################
    if not may_arbitrary_one_primitive_root_modPpow is None:
        g = may_arbitrary_one_primitive_root_modPpow
    else:
        p = _p5factorization_of_pmm_ex_(factorization_of_pmm, may_p)
        g = find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, p, may_arbitrary_one_primitive_root_modP)
        g = f(exp4Ppow, p, g)
    g
    return g

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
def _iter_sorted_primitive_roots_mod_prime_(p, factorization_of_pmm, /, *, _ver=2):
    'p -> factorization{p-1} -> sorted-Iter primitive_root%p'
    if p == 2:
        yield 1
        return
    # [p >= 3]
    # [p-1 >= 2]
    pmm = p-1
    # [pmm >= 2]
    ######################
    if _ver==2:
        q_e_pairs = sorted(factorization_of_pmm.items())
        k = pmm
        N = p
        for g in range(2, p):
            if _is_kth_primitive_root_mod_N__via_complete_factorization_k__ver2_(k, q_e_pairs, N, g):
                yield g
        return
    assert _ver==1
    ######################
    (phi_p, phi_pmm) = _phi_phi_(pmm, factorization_of_pmm)
    #gs = []
    num_gs = 0
    q_e_pairs = sorted(factorization_of_pmm.items())
    assert q_e_pairs
        # !! [p-1 >= 2]
    #bug: p=2,3: for g in range(2, pmm//2 +1):
    for g in range(2, p):
        #base0 = pow(g, e0, p)
        base0 = g
        for q, e in q_e_pairs:
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
        # [base0 == pow(g, (p-1)///II(qs), p)]

        # [base0 == pow(g, (p-1)///II(qs[0:]), p)]
        for i in range(len(q_e_pairs)):
            # [base0 == pow(g, (p-1)///II(qs[i:]), p)]
            #base1 = pow(g, pmm//q, p)
            base1 = base0
            for q, _ in q_e_pairs[i+1:]:
                base1 = pow(base1, q, p)
                if base1 == 1:
                    break
            if base1 == 1:
                break
            # [base1 == pow(g, (p-1)///qs[i], p)]
            # [base1 =!= 1]
            q, _ = q_e_pairs[i]
            base0 = pow(base0, q, p)
            # [base0 == pow(g, (p-1)///II(qs[i+1:]), p)]
        else:
            # [base0 == pow(g, (p-1)///II([]), p)]
            # [base0 == pow(g, (p-1), p)]
            assert base0 == 1, ((p, factorization_of_pmm), phi_p, q_e_pairs, base0, pow(g, phi_p, p))
        if base1 == 1:
            #bug:assert not base0 == 1
            continue
        assert base0 == 1
        yield g
        #gs.append(g)
        num_gs += 1
    #assert len(gs) == phi_pmm
    assert num_gs == phi_pmm
    ######################
def _phi_phi_(pmm, factorization_of_pmm, /):
    II_q = II(q for q in factorization_of_pmm)
    e0 = pmm//II_q
    phi_p = e0 * II_q
    assert phi_p == pmm #check:[pmm%II_q==0]
    II_qmm = II(q-1 for q in factorization_of_pmm)
    phi_pmm = e0 * II_qmm
        # == phi_phi_p
    return (phi_p, phi_pmm) # (phi_p, phi_phi_p)


def _prepare4prs_mod_(factorization_of_pmm, may_p, may_arbitrary_one_primitive_root_modP, /):
    p = _p5factorization_of_pmm_ex_(factorization_of_pmm, may_p)
    pmm = p-1
    g = find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, p, may_arbitrary_one_primitive_root_modP)
    return (p, pmm, g)
def list_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, may_arbitrary_one_primitive_root_modP=None, /):
    'factorization{p-1} -> may p -> may arbitrary_one_primitive_root%p -> sorted[primitive_root%p]  # [list_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p) == list(iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p))]'
    from itertools import repeat, pairwise, chain
    #from seed.types.DefaultDict import DefaultDict2
    #class DefaultDict2(DefaultDict):
    #    def __init__(self, mapping, ncall, value_mkr, /, *ex_args):
    (p, pmm, g) = _prepare4prs_mod_(factorization_of_pmm, may_p, may_arbitrary_one_primitive_root_modP)
    assert p < 2**21
    j2b = j2whether_coprime4Pmm = [True]*pmm
    #qs4Pmm = sorted(factorization_of_pmm.keys())
    qs4Pmm = (factorization_of_pmm.keys())
    if 0:
        #bug:
        if p==2:
            j2b[0] = False
    for q in qs4Pmm:
        #bug:cellphone-crash:j2b[::q] = repeat(False)
        j2b[::q] = repeat(False, pmm//q)
    j2b
    777;    del qs4Pmm
    assert len(j2b) == pmm

    #coprimes4Pmm = [j for j, b in enumerate(j2b) if b]
    #iter_coprimes4Pmm_ = lambda:(j for j, b in enumerate(j2b) if b)
    #bug:iter_0_or_coprimes4Pmm_ = lambda:(j for j, b in enumerate(j2b) if b or j==0)
    #   !! [p==2][pmm==1][0 <- coprimes4Pmm]:
    iter_0_or_coprimes4Pmm_ = lambda:chain([0], (j for j, b in enumerate(j2b) if b))
    deltas = {b-a for a, b in pairwise(iter_0_or_coprimes4Pmm_())}
    assert (0 in deltas) is (p==2)
    #deltas = sorted(deltas)
    e2pw = {1:g}
    def pw5e_(e, /):
        assert (e > 0) ^ (p==2)
        try:
            return e2pw[e]
        except KeyError:
            pass
        e2pw[e] = pow(g,e,p)
        return e2pw[e]
        return pw5e_(e)
    for delta in deltas:
        pw5e_(delta)
        # [e2pw[delta] == g**delta%p]

    #e2pw = DefaultDict2({1:g}, 1, lambda e:e2pw[e-1]*g%p)
    iter_0_or_coprimes4Pmm = iter_0_or_coprimes4Pmm_()
    ls = []
    pw = 1
    # [pw == g**0%p]
    #for _j, j in pairwise(chain([0], iter_coprimes4Pmm_())):
    for _j, j in pairwise(iter_0_or_coprimes4Pmm):
        # [are_coprime(pmm, j)]
        # [pw == g**_j%p]
        delta = j-_j
        pw = pw*e2pw[delta]%p
        # !! [e2pw[delta] == g**delta%p]
        # [pw == g**(_j+delta)%p]
        # [pw == g**j%p]

        # !! [are_coprime(pmm, j)]
        # !! [g is arbitrary_one_primitive_root%p]
        # !! [pw == g**j%p]
        # [pw is arbitrary_one_primitive_root%p]
        ls.append(pw)
    ls

    if __debug__:
        (phi_p, phi_pmm) = _phi_phi_(pmm, factorization_of_pmm)
        assert len(ls) == phi_pmm, (p, pmm, factorization_of_pmm, phi_pmm, len(ls), ls)
    ls.sort()
    return ls


def _iter_coprimes4prime_bases_(ps, may_us, /):
    'sized[prime] -> Iter coprime/uint'
    assert not iter(ps) is ps
    L = len(ps)
    def is_coprime_(u, /):
        return all(u%p for p in ps)

    if may_us is None:
        from itertools import count
        us = count(0)
    else:
        us = may_us
    us = iter(us)

    if not L:
        return us
    assert L
    return filter(is_coprime_, us)


def iter_unsorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, may_arbitrary_one_primitive_root_modP=None, /):
    'factorization{p-1} -> may p -> may arbitrary_one_primitive_root%p -> unsorted (Iter primitive_root%p)  # [sorted(iter_unsorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p)) == list(iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p))]'
    (p, pmm, g) = _prepare4prs_mod_(factorization_of_pmm, may_p, may_arbitrary_one_primitive_root_modP)
    assert p >= 2
    ps4Pmm = sorted(factorization_of_pmm)
    num_gs4P = yield from _iter_unsorted_gs4same_order_mod_(M:=p, g, order4g:=pmm, ps4order4g:=ps4Pmm)
    if __debug__:
        (phi_p, phi_pmm) = _phi_phi_(pmm, factorization_of_pmm)
        assert num_gs4P == phi_pmm, (p, pmm, factorization_of_pmm, phi_pmm, num_gs4P)
    return

def _iter_unsorted_gs4same_order_mod_(M, g, order4g, ps4order4g, /):
    'M -> g -> order4g{[order_mod_(M;g) == order4g]} -> ps4order4g{[ps4order4g==all_prime_factors_of(order4g)]} -> (Iter pw){[order_mod_(M;pw) == order4g]}'
    from itertools import pairwise, chain
    assert M >= 2
    iter_coprimes4order4g = _iter_coprimes4prime_bases_(ps4order4g, range(order4g))
    iter_0_or_coprimes4order4g = chain([0], iter_coprimes4order4g)
    _e = 0
    sz = 0
    pw = 1
    # [pw == g**0%M]
    for _j, j in pairwise(iter_0_or_coprimes4order4g):
        # [are_coprime(order4g, j)]
        # [pw == g**_j%M]
        delta = j-_j
        pw = pw*pow(g,delta,M)%M
        # [pw == g**(_j+delta)%M]
        # [pw == g**j%M]

        # !! [are_coprime(order4g, j)]
        # !! [pw == g**j%M]
        # [order_mod_(M;pw) == order_mod_(M;g) == order4g]
        yield pw
        sz += 1
    return sz




iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_
list_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_
iter_unsorted_primitive_roots_mod_prime__using_factorization_of_pmm_

#prime_power
#list_sorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_
#   view ../../python3_src/seed/math/max_order_mod_.py
#, *, exp4Ppow=1
find_arbitrary_one_primitive_root_mod_prime_power__using_factorization_of_pmm_


def list_sorted_primitive_roots_mod_prime_square__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, may_arbitrary_one_primitive_root_modP=None, may_arbitrary_one_primitive_root_modPP=None, /):
    'factorization{p-1} -> may p -> may arbitrary_one_primitive_root%p -> may arbitrary_one_primitive_root%p**2 -> sorted[primitive_root%p**2]'
    gs4PP = sorted(iter_unsorted_primitive_roots_mod_prime_square__using_factorization_of_pmm_(factorization_of_pmm, may_p, may_arbitrary_one_primitive_root_modP, may_arbitrary_one_primitive_root_modPP))
    return gs4PP
def iter_unsorted_primitive_roots_mod_prime_square__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, may_arbitrary_one_primitive_root_modP=None, may_arbitrary_one_primitive_root_modPP=None, /):
    'factorization{p-1} -> may p -> may arbitrary_one_primitive_root%p -> may arbitrary_one_primitive_root%p**2 -> unsorted (Iter primitive_root%p**2)'
    exp4Ppow = 2
    p = _p5factorization_of_pmm_ex_(factorization_of_pmm, may_p)
    pp = p**exp4Ppow
    g4pp = find_arbitrary_one_primitive_root_mod_prime_power__using_factorization_of_pmm_(exp4Ppow, factorization_of_pmm, p, may_arbitrary_one_primitive_root_modP, pp, may_arbitrary_one_primitive_root_modPP)
    phi_p = pmm = p-1
    (phi_p, phi_pmm) = _phi_phi_(pmm, factorization_of_pmm)
    phi_pp = pmm*p
        # [phi_(p**2) == phi_(p)*p == pmm*p]
    777;    ps4phi_pp = sorted(factorization_of_pmm) + [p]
    phi_phi_pp = phi_pmm*pmm
        # !! [phi_(p**2) == pmm*p]
        # !! [gcd(pmm,p)==1]
        # [phi_(phi_(p**2)) == phi_(pmm*p) == phi_pmm*phi_p == phi_pmm*pmm]
        # [phi_(phi_(p**2)) == phi_pmm*pmm]
    num_gs4P = phi_phi_p = phi_pmm
    num_gs4PP = phi_phi_pp
    assert num_gs4PP == num_gs4P*pmm
    #.if 0:
    #.    g4p = g4pp%p
    #.    gs4P = list_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, p, g4p)
    #.    assert len(gs4P) == num_gs4P
    #_iter_sorted_primitive_roots_mod_prime_
    #_iter_coprimes4prime_bases_
    _num_gs4PP = yield from _iter_unsorted_gs4same_order_mod_(M:=pp, g4pp, order4g:=phi_pp, ps4order4g:=ps4phi_pp)
    assert num_gs4PP == _num_gs4PP
    return

def list_sorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_(exp4Ppow, factorization_of_pmm, may_p=None, may_arbitrary_one_primitive_root_modP=None, may_arbitrary_one_primitive_root_modPP=None, /):
    'exp4Ppow/int{>=1} -> factorization{p-1} -> may p -> may arbitrary_one_primitive_root%p -> may arbitrary_one_primitive_root%p**2{== 2 not exp4Ppow} -> sorted[Iter primitive_root%p**exp4Ppow]'
    return sorted(iter_unsorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_(exp4Ppow, factorization_of_pmm, may_p, may_arbitrary_one_primitive_root_modP, may_arbitrary_one_primitive_root_modPP))
def iter_unsorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_(exp4Ppow, factorization_of_pmm, may_p=None, may_arbitrary_one_primitive_root_modP=None, may_arbitrary_one_primitive_root_modPP=None, /):
    r'''[[[
    'exp4Ppow/int{>=1} -> factorization{p-1} -> may p -> may arbitrary_one_primitive_root%p -> may arbitrary_one_primitive_root%p**2{== 2 not exp4Ppow} -> unsorted (Iter primitive_root%p**exp4Ppow)'

[[
copy from:
  view ../../python3_src/seed/math/max_order_mod_.py
  # [:规律纟伪本原根纟模二幂]:goto
  # [:规律纟伪本原根纟模奇素幂]:goto
===

# [:规律纟伪本原根纟模二幂]:here
# [all_primitive_roots_modZpow_(2**1) == {1}]
# [all_primitive_roots_modZpow_(2**2) == {1}]
# [all_pseudo_primitive_roots_modZpow_(2**3) == {3, 5, 7}]
# [all_pseudo_primitive_roots_modZpow_(2**4) == {3, 5, 11, 13}]
# [[ez>=4] -> [all_pseudo_primitive_roots_modZpow_(2**ez) == {(g+16*k) | [[g:<-[3, 5, 11, 13]][k:<-[0..<2**(ez-4)]]]}]]
# [[ez>=4] -> [len(all_pseudo_primitive_roots_modZpow_(2**ez)) == 2**(ez-2)]]

# [:规律纟伪本原根纟模奇素幂]:here
# [[is_prime_(p)] -> [p%2==1] -> [g4p:<-all_primitive_roots_modPpow_(p**1)] -> [(p-1) == len({k | [[k:<-[0..<p]][(g4p+k*p) <- all_primitive_roots_modPpow_(p**2)]]})]]
# [[ep:<-[2..]] -> [is_prime_(p)] -> [p%2==1] -> [all_primitive_roots_modPpow_(p**ep) == {(g+k*p**2) | [[g:<-all_primitive_roots_modPpow_(p**2)][k:<-[0..<p**(ep-2)]]]}]]
# [[ep:<-[2..]] -> [is_prime_(p)] -> [p%2==1] -> [len(all_primitive_roots_modPpow_(p**ep)) == phi_(p-1)*(p-1)*p**(ep-2)]]
# [[is_prime_(p)] -> [p%2==1] -> [len(all_primitive_roots_modPpow_(p**2)) == phi_(p-1)*(p-1)]]
# [[is_prime_(p)] -> [p%2==1] -> [len(all_primitive_roots_modPpow_(p**1)) == phi_(p-1)]]
]]
    #]]]'''#'''
    assert exp4Ppow >= 1
    if exp4Ppow == 1:
        return iter_unsorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p, may_arbitrary_one_primitive_root_modP)

    p = _p5factorization_of_pmm_ex_(factorization_of_pmm, may_p)
    iter_gs4PP = iter_unsorted_primitive_roots_mod_prime_square__using_factorization_of_pmm_(factorization_of_pmm, p, may_arbitrary_one_primitive_root_modP, may_arbitrary_one_primitive_root_modPP)
    if exp4Ppow == 2:
        return iter_gs4PP
    pp = p**2
    ppow = p**exp4Ppow

    def f4odd_p(exp4Ppow, p, pp, ppow, iter_gs4PP, /):
        assert p&1
        assert exp4Ppow >= 3
        # [:规律纟伪本原根纟模奇素幂]:goto
        for g4pp in iter_gs4PP:
            yield from range(g4pp, ppow, pp)
        return
    def f4even_p(exp4Ppow, p, pp, ppow, iter_gs4PP, /):
        assert p == 2
        assert exp4Ppow >= 3
        ez = exp4Ppow
        # [:规律纟伪本原根纟模二幂]:goto
        assert ez >= 3
        if ez == 3:
            yield from [3,5,7]
            return
        assert ez >= 4
        for g4zpow4 in [3, 5, 11, 13]:
            yield from range(g4zpow4, ppow, zpow4:=16)
        return
    f = f4even_p if p==2 else f4odd_p
    return f(exp4Ppow, p, pp, ppow, iter_gs4PP)



__all__
if 1:from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import _iter_unsorted_gs4same_order_mod_
if 1:from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import _iter_coprimes4prime_bases_
if 1:from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import _find_arbitrary_one_primitive_root_mod_prime_, _find_the_min_primitive_root_mod_prime_, _iter_sorted_primitive_roots_mod_prime_
from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_, find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_, iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_
#def find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, may_arbitrary_one_primitive_root_modP=None, /):
#    'factorization{p-1} -> may p -> may arbitrary_one_primitive_root%p -> arbitrary primitive_root%p'

from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import list_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_
#def list_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, may_arbitrary_one_primitive_root_modP=None, /):
#    'factorization{p-1} -> may p -> may arbitrary_one_primitive_root%p -> sorted[primitive_root%p]  # [list_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p) == list(iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p))]'


from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import iter_unsorted_primitive_roots_mod_prime__using_factorization_of_pmm_
#def iter_unsorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, may_arbitrary_one_primitive_root_modP=None, /):
#    'factorization{p-1} -> may p -> may arbitrary_one_primitive_root%p -> unsorted (Iter primitive_root%p)  # [sorted(iter_unsorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p)) == list(iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p))]'

from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import find_arbitrary_one_primitive_root_mod_prime_power__using_factorization_of_pmm_
#def find_arbitrary_one_primitive_root_mod_prime_power__using_factorization_of_pmm_(exp4Ppow, factorization_of_pmm, may_p=None, may_arbitrary_one_primitive_root_modP=None, may_ppow=None, may_arbitrary_one_primitive_root_modPpow=None, /):
#    'exp4Ppow/int{>=1}{[[p==2]->[exp4Ppow<=2]]} -> factorization{p-1} -> may p -> may arbitrary_one_primitive_root%p -> may ppow{==p**exp4Ppow} -> may arbitrary_one_primitive_root%ppow -> arbitrary primitive_root%ppow'


from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import iter_unsorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_, list_sorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_
#def iter_unsorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_(exp4Ppow, factorization_of_pmm, may_p=None, may_arbitrary_one_primitive_root_modP=None, may_arbitrary_one_primitive_root_modPP=None, /):
#    'exp4Ppow/int{>=1} -> factorization{p-1} -> may p -> may arbitrary_one_primitive_root%p -> may arbitrary_one_primitive_root%p**2{== 2 not exp4Ppow} -> unsorted (Iter primitive_root%p**exp4Ppow)'

from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import iter_unsorted_primitive_roots_mod_prime_square__using_factorization_of_pmm_, list_sorted_primitive_roots_mod_prime_square__using_factorization_of_pmm_
#def list_sorted_primitive_roots_mod_prime_square__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, may_arbitrary_one_primitive_root_modP=None, may_arbitrary_one_primitive_root_modPP=None, /):
#    'factorization{p-1} -> may p -> may arbitrary_one_primitive_root%p -> may arbitrary_one_primitive_root%p**2 -> sorted[primitive_root%p**2]'
#def iter_unsorted_primitive_roots_mod_prime_square__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, may_arbitrary_one_primitive_root_modP=None, may_arbitrary_one_primitive_root_modPP=None, /):
#    'factorization{p-1} -> may p -> may arbitrary_one_primitive_root%p -> may arbitrary_one_primitive_root%p**2 -> unsorted (Iter primitive_root%p**2)'
from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import *
