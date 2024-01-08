raise NotImplementedError-too-complicate
#__all__:goto
r'''[[[
e ../../python3_src/seed/math/primality_proving.py
view others/数学/prime/primality_test.txt
view ../../python3_src/seed/math/primality_proving-202310.py
view ../../python3_src/seed/types/CachedProperty.py
e ../../python3_src/seed/math/primality_proving__plain.py


seed.math.primality_proving
py -m nn_ns.app.debug_cmd   seed.math.primality_proving -x
py -m nn_ns.app.doctest_cmd seed.math.primality_proving:__doc__ -ff -v
py_adhoc_call   seed.math.primality_proving   @f
from seed.math.primality_proving import *
#]]]'''
__all__ = r'''
'''.split()#'''
__all__
from itertools import chain
from enum import Enum, auto
from itertools import accumulate, takewhile
#accumulate(iterable, func=None, *, initial=None)




from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
from seed.tiny import mk_tuple
from seed.tiny import check_type_is
from seed.tiny_.check import check_int_ge, check_int_ge_lt
from seed.math.II import II, II__ft_e_pairs_
#from seed.math.II import II, II_mod, II__p2e_, II__ft2e_
from seed.types.CachedProperty import CachedProperty
from seed.math.are_pairwise_coprime import are_pairwise_coprime
from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
from seed.seq_tools.split_tuples import split_tuples, unzip_pairs
#from seed.iters.duplicate_elements import find_maybe_duplicate_element1
from seed.math.divs import is_odd
from seed.math.gcd import gcd
from seed.iters.apply_commutative_operations_except_one import iter_apply_commutative_operations_except_one_
#def iter_apply_commutative_operations_except_one_(apply_, commutative_operation_keys, x0, /):
from seed.math.floor_ceil import floor_sqrt #perfect_div, perfect_kth_root_
from seed.seq_tools.remove_strict_sorted_indices import list_values__via_idc_, list_complement_idc_




def _iter_pow_II1_except_one_(_pow_, fts, x0, /):
    '-> (_pow_(x0, II(fts)///ft) for ft in fts)'
    def apply_(ft, x, /):
        x = _pow_(x, ft)
        return x
    return iter_apply_commutative_operations_except_one_(apply_, fts, x0)




def check_ints_ge_lt(m, M, xs, /):
    for x in xs:
        check_int_ge_lt(m, M, x)
def check_ints_ge(m, xs, /):
    for x in xs:
        check_int_ge(m, x)
class _Immutable:
    #def __getattr__(sf, nm, /):
    #def __getattribute__(sf, nm, /):
    def __delattr__(sf, nm, /):
        raise AttributeError(nm)
    def __setattr__(sf, nm, x, /):
        if hasattr(sf, nm):
            raise AttributeError(nm)
        super().__setattr__(nm, x)

class PartialFactorization(_Immutable):
    #PartialFactorization(j2factor, j2exp, j2prime_factor_lowbound, remain_factor, N=None)
    # def-nickname:[2pow == 2**e2 == 2**ez == zpow]
    def __init__(sf, j2factor, j2exp, j2prime_factor_lowbound, remain_factor, N=None, /):
        j2factor = mk_tuple(j2factor)
        j2exp = mk_tuple(j2exp)
        j2prime_factor_lowbound = mk_tuple(j2prime_factor_lowbound)
        ######################
        check_ints_ge(2, j2factor)
        check_ints_ge(1, j2exp)
        check_ints_ge(2, j2prime_factor_lowbound)
        check_int_ge(1, remain_factor)
        N is None or check_int_ge(1, N)
        ######################
        if not len(j2factor) == len(j2exp): raise TypeError
        if not len(j2factor) == len(j2prime_factor_lowbound): raise TypeError
        for ft, B in zip(j2factor, j2prime_factor_lowbound):
            #check_int_ge(B, ft)
            #check_int_ge_le(2, ft,  B)
            if not (2 <= B == ft or 2 <= B < B**2 <= ft): raise TypeError
            # [2 <= B == ft or 2 <= B < B**2 <= ft]
                # update from: [2 <= B < ft]
                #   to match primality_criterion [m < (e5B+1)**2] from: may_selected_js4CASE_factored_part_lowbound4Nmm_gt_sqrtN/may_selected_js_ex4CASE_factored_part_lowbound4Nmm_gt_cubic_rootN
        ######################
        if 0:
            L = len(j2factor)
            _N = II(ft**e for ft, e in zip(j2factor, j2exp)) *remain_factor
            if N is None:
                N = _N
            if not N == _N: raise TypeError
        ######################
        sf.j2factor = j2factor
        sf.j2exp = j2exp
        sf.j2prime_factor_lowbound = j2prime_factor_lowbound
        sf.remain_factor = remain_factor
        #sf.N = N
        #sf.L = L
        ######################
        if not N is None:
            if not N == sf.N: raise TypeError
        ######################
        return

    @CachedProperty
    def j2ft_is_prime(sf, /):
        #except remain_factor!
        # !! [2 <= B == ft or 2 <= B < B**2 <= ft]
        return tuple(ft == B for ft, B in zip(sf.j2factor, sf.j2prime_factor_lowbound))
        return tuple(ft == B or ft < B**2 for ft, B in zip(sf.j2factor, sf.j2prime_factor_lowbound))
    @CachedProperty
    def factors_are_all_prime(sf, /):
        #except remain_factor!
        return all(sf.j2ft_is_prime)
    @CachedProperty
    def factorization_is_complete(sf, /):
        return sf.remain_factor == 1 and sf.factors_are_all_prime
    @CachedProperty
    def factors_are_pairwise_coprime(sf, /):
        return are_pairwise_coprime(chain(sf.j2factor, [sf.remain_factor]))
    @CachedProperty
    def j2pow_factor_exp(sf, /):
        j2factor = sf.j2factor
        j2exp = sf.j2exp
        j2pow_factor_exp= tuple(ft**e for ft, e in zip(j2factor, j2exp))
        return j2pow_factor_exp

    @CachedProperty
    def j2pow_lowbound_exp(sf, /):
        j2prime_factor_lowbound = sf.j2prime_factor_lowbound
        j2exp = sf.j2exp
        j2pow_lowbound_exp= tuple(B**e for B, e in zip(j2prime_factor_lowbound, j2exp))
        return j2pow_lowbound_exp
    @CachedProperty
    def N(sf, /):
        N = II(sf.j2pow_factor_exp) *sf.remain_factor
        return N
    @CachedProperty
    def L(sf, /):
        return len(sf.j2factor)

    @CachedProperty
    def Nmm(sf, /):
        return sf.N -1
    @CachedProperty
    def Npp(sf, /):
        return sf.N +1

    @CachedProperty
    def ez_odd_pair(sf, /):
        (ez, odd) = factor_pint_out_power_of_base_(2, sf.N)
        return (ez, odd)

    def get_args(sf, /):
        '-> (fts, es, Bs, ft_ex, N)'
        j2factor = sf.j2factor
        j2exp = sf.j2exp
        j2prime_factor_lowbound = sf.j2prime_factor_lowbound
        remain_factor = sf.remain_factor
        N = sf.N
        return (j2factor, j2exp, j2prime_factor_lowbound, remain_factor, N)
        (j2factor, j2exp, j2prime_factor_lowbound, remain_factor, N) = sf.get_args()

    if 0:
        @CachedProperty
        def reversed_sorted_js__via_j2pow_factor_exp(sf, /):
            js = sorted(range(sf.L), sf.j2pow_factor_exp.__getitem__, reverse=True)
            return js

    @CachedProperty
    def reversed_sorted_js__via_j2pow_lowbound_exp(sf, /):
        js = sorted(range(sf.L), sf.j2pow_lowbound_exp.__getitem__, reverse=True)
        return js
    @CachedProperty
    def acc5desc_pow_lowbound_exp(sf, /):
        DESC__BEs = map(sf.j2pow_lowbound_exp.__getitem__, sf.reversed_sorted_js__via_j2pow_lowbound_exp)
        return tuple(accumulate(DESC__BEs, int.__mul__))
    @CachedProperty
    def floor_sqrt_Npp(sf, /):
        return floor_sqrt(sf.Npp)

    @CachedProperty
    def may_selected_js4CASE_factored_part_lowbound4Nmm_gt_sqrtN(sf, /):
        #CASE:factored_part_lowbound4Nmm_gt_sqrtN{N:=sf.Npp}
        floor_sqrt_Npp = sf.floor_sqrt_Npp
        ls = sf.acc5desc_pow_lowbound_exp
        may_i = _may_find__asc_seq__gt(floor_sqrt_Npp-1, ls)
        if may_i is None:
            return None
        i = may_i
        assert ls[0] is sf.reversed_sorted_js__via_j2pow_lowbound_exp[0]
        js = sf.reversed_sorted_js__via_j2pow_lowbound_exp[:i+1]
        return js
    @CachedProperty
    def _FR_decompose(sf, /):
        L = sf.L
        selected_js = range(L)
        js = sf.prime_factor_js
        j2pow_factor_exp = sf.j2pow_factor_exp
        j2pow_lowbound_exp = sf.j2pow_lowbound_exp
        #_mk_unselected_js
        js
        cs = list_complement_idc_(L, js)
        eF = II(list_values__via_idc_(js, j2pow_factor_exp))
        eR = II(list_values__via_idc_(cs, j2pow_factor_exp)) *remain_ez

        e5ft = eF * eR
        e5B = eF * II(list_values__via_idc_(cs, j2pow_lowbound_exp)) * 1 # "1" for remain_factor
        # [e5ft := II fts[i]**es[i] {i :<- [0..<L]}]
        # [e5B := II Bs[i]**es[i] {i :<- [0..<L]}]
        # [eF := II fts[j]**es[j] {j :<- js}]

        assert sf.N == e5ft >= e5B >= eF
        gcdFR = gcd(eF, eR)
        return (selected_js, eF, eR, e5ft, e5B, gcdFR)

    @CachedProperty
    def may_selected_js_ex4CASE_factored_part_lowbound4Nmm_gt_cubic_rootN(sf, /):
        '-> may (must_be_composite, selected_js) | ^IsComposite__nontrivial_factor'
        #CASE:factored_part_lowbound4Nmm_gt_cubic_rootN{N:=sf.Npp}
        N = sf.Npp
        Nmm = sf.N
        ######################
        (selected_js, eF, eR, e5ft, e5B, gcdFR) = sf._FR_decompose
        # [sf.N == Nmm == e5ft >= e5B >= eF]
        if is_odd(eF):
            return None
        if not is_odd(eR):
            return None
        if not 1 == gcdFR:
            return None
        # [gcd(eF,eR) == 1]
        # [eF%2 == 0]
        # [eR%2 == 1]

        must_be_composite = False
        #if N < (e5B+1)**2:
        #   NOTE: [N := sf.Npp]
        if sf.floor_sqrt_Npp <= e5B:
            return None
        # [sf.Npp == N >= (e5B+1)**2]
        m = N
        eR
        # [m >= (e5B+1)**2]
        # !! [e5B >= eF]
        # [m >= (eF+1)**2]
        # !! [m == 1+eF*eR]
        # [1+eF*eR >= (eF+1)**2]
        # [eR >= eF+2]

        # !! [eF%2 == 0]
        # !! [eR%2 == 1]
        #  [eR =!= eF+2]
        # !! [eR >= eF+2]
        # [eR >= eF+3]

        #assert m == 1+eF*eR
        #assert eR >= eF+3

        #u = if e5ft%3 == 1 then 3 else 1
        u = 3 if m%3 == 2 else 1
        _2_u_eF = (2*u*eF)
        (q, r) = divmod(eR, _2_u_eF)
        assert eR&1 == 1
        assert r&1 == 1
        # [1 <= r <= eR]
        # [r %2 == 1]

        #bug:e5B//eF:kB = min(e5B, ((_2_u_eF +r-1)>>1))
        kB = min(e5B//eF, ((_2_u_eF +r-1)>>1))
            # select kB to max rhs => [m < rhs]
            #   => (2*u*eF+r)/2 but r is odd
        assert kB >= 1
        if not m < (kB*eF +1) * ((_2_u_eF +r -kB)*eF +1):
            return None
        # [m < (kB*eF +1) * ((_2_u_eF +r -kB)*eF +1)]

        # [gcd...to check:ok] => [[is_prime_(m)] <-> [not$ [[r >= 2*kB][q >= ceil_(kB**2 /(2*u)) >= 1][sqrt(r**2 -8*u*q) %1 == 0]]]]
        # [gcd...to check:ok] => [[is_composite_(m)] <-> [[r >= 2*kB][q >= ceil_(kB**2 /(2*u)) >= 1][sqrt(r**2 -8*u*q) %1 == 0]]]
        # [[r >= 2*kB][q >= ceil_(kB**2 /(2*u)) >= 1][sqrt(r**2 -8*u*q) %1 == 0]] => [gcd...to check:ok] => [is_composite_(m)]
        # [[r >= 2*kB][q >= ceil_(kB**2 /(2*u)) >= 1][sqrt(r**2 -8*u*q) %1 == 0]] => [[gcd...to check:fail]or[is_composite_(m)]]
        #
        #
        # [gcd...to check:fail] => [[found nontrivial_factor or witness4composite]or[g is not partial pseudo "primitive" root of 1%m]]
        #
        if r >= 2*kB and 2*u*q >= kB**2 and (sq := r**2 -8*u*q) >= 0 and (sqrt := floor_sqrt(sq))**2 == sq:
            # [gcd...to check:ok] => [is_composite_(m)]
            # [[gcd...to check:fail]or[is_composite_(m)]]
            # [[gcd...to check:fail]or[m%ft4m == 0]]
            #
            # [(s+t) == r]
            # [(s-t) == sqrt(r**2 -8*u*q)]
            # [m == (1+s*eF)*(1+t*eF)]
            assert q > 0
            r, sqrt
            assert r&1 == 1
            assert sqrt&1 == 1
            assert 0 <= sqrt < r
            s = (r+sqrt)//2
            t = (r-sqrt)//2
            assert 0 < t <= s < t+s == r < _2_u_eF
            assert 0 < t <= (r-1)//2 <= (_2_u_eF-2)//2 == u*eF -1
            assert kB <= (r-1)//2

            ft4m = (1+t*eF)
            # !! [r <= eR]
            assert 0 < t < r <= eR
            assert 3 <= 1+t*eF < 1+eR*eF == m
            assert 3 <= ftm < m
            #not check gcd yet:
                ###assert m == (1+s*eF)*(1+t*eF)
                ###assert 1 < ft4m < m
                ###assert m %ft4m == 0
            #if 1 < ft4m < m and m %ft4m == 0:
            assert 1 < ft4m < m
            if m %ft4m == 0:
                raise IsComposite__nontrivial_factor(ft4m)
            # [m%ft4m =!= 0]
            #
            #
            # !! [[gcd...to check:fail]or[m%ft4m == 0]]
            # !! [m%ft4m =!= 0]
            # [gcd...to check:fail]
            # @j2g. [gcd...to check:fail]
            # @j2g. [gcd...to check:fail] => [[found nontrivial_factor or witness4composite]or[?j. order_mod_(m;j2g[j]) %j2factor[j]**j2exp[j] =!= 0]]
            ###
            # [gcd ... to check:must fail]
            # [any j2g must cause failure]
            # [is_composite_(m)]
            must_be_composite = True
        else:
            # [gcd...to check:ok] => [is_prime_(m)]
            pass

        return (must_be_composite, selected_js)


    @CachedProperty
    def prime_factor_js(sf, /):
        return tuple(j for j, ft_is_prime in enumerate(sf.j2ft_is_prime) if ft_is_prime)

    @CachedProperty
    def _prepare4primality_test(sf, /):
        j2factor = sf.j2factor
        remain_factor = sf.remain_factor
        (remain_ez, remain_odd) = factor_pint_out_power_of_base_(2, remain_factor)
        (j2ft_ez, j2ft_odd) = unzip_pairs(factor_pint_out_power_of_base_(2, ft) for ft in j2factor)
        return (j2ft_ez, remain_ez, j2ft_odd, remain_odd)

def _may_find__asc_seq__gt(u, asc_seq, /):
    if not (asc_seq and u < asc_seq[-1]):
        return None
    may_idx = _may_find_if(u.__lt__, asc_seq)
    if may_idx is None: raise 000
    i = may_idx
    return i

def _may_find_if(f, it, /):
    for i, x in enumerate(it):
        if f(x):
            return i
    return None
######################
######################
#def plain_validate_discrete_logarithm(N, complete_factorization4order, j2partial_pseudo_primitive_root, /):
def plain_validate_partial_primitive_roots_(N, complete_factorization4order, j2partial_primitive_root, /):
    # not using gcd
    check_int_ge(2, N)
    check_type_is(PartialFactorization, complete_factorization4order)
    if not complete_factorization4order.factorization_is_complete: raise TypeError
    order = complete_factorization4order.N
    check_int_ge_lt(1, N,   order)

    L = complete_factorization4order.L
    if not len(j2partial_primitive_root) == L: raise TypeError
    j2partial_primitive_root[:0]

    j2g = j2partial_primitive_root
    j2prime = complete_factorization4order.j2factor
    j2exp = complete_factorization4order.j2exp
    for j in range(L):
        g = j2g[j]
        p = j2prime[j]
        e = j2exp[j]
        r = pow(g, order//p, N)
        if r == 1: raise ValidateFail
        if j == 0:
            if not 1 == pow(r, p, N): raise ValidateFail
    if L == 0:
        assert order == 1
        # [g%N==1] if any
    return
######################
######################
#def plain_validate_discrete_logarithm__via_Nmm(partial_factorization4Nmm, j2partial_pseudo_primitive_root, /):
def plain_validate_partial_pseudo_primitive_roots__via_Nmm_(partial_factorization4Nmm, j2partial_pseudo_primitive_root, /):
    # using gcd
    check_type_is(PartialFactorization, partial_factorization4Nmm)
    Nmm = partial_factorization4Nmm.N
    # [Nmm >= 1]
    N = partial_factorization4Nmm.Npp
    # [N >= 2]
    assert 1 <= Nmm == N-1
    order = Nmm

    L = partial_factorization4Nmm.L
    if not len(j2partial_pseudo_primitive_root) == L: raise TypeError
    j2partial_pseudo_primitive_root[:0]

    j2g = j2partial_pseudo_primitive_root
    j2factor = partial_factorization4Nmm.j2factor
    j2exp = partial_factorization4Nmm.j2exp
    for j in range(L):
        g = j2g[j]
        ft = j2factor[j]
        e = j2exp[j]
        r = pow(g, order//ft, N)
        if not gcd(r-1, N) == 1: raise ValidateFail
        if j == 0:
            if not 1 == pow(r, ft, N): raise ValidateFail
    if L == 0:
        assert order == 1
        assert N == 2
        # [g%N==1] if any
    return
######################
######################
class PartialFactorization__with_selected_indices(_Immutable):
    #PartialFactorization__with_selected_indices(partial_factorization, selected_js)
    #PartialFactorization(j2factor, j2exp, j2prime_factor_lowbound, remain_factor, N=None)
    # def-nickname:[2pow == 2**e2 == 2**ez == zpow]
    def __init__(sf, partial_factorization, selected_js, /):
        ######################
        check_type_is(PartialFactorization, partial_factorization)
        ######################
        L = partial_factorization.L
        ######################
        if selected_js is True:
            selected_js = range(L)
        else:
            selected_js = mk_tuple(selected_js)
            check_ints_ge_lt(0, L, selected_js)
        selected_js
        ######################
        #if find_maybe_duplicate_element1(selected_js): raise TypeError
        #selected_js__set = set(selected_js)
        #if find_maybe_duplicate_element1(selected_js): raise TypeError

        ######################
        #unselected_js = tuple(i for i in range(L) if i not in selected_js__set)
        ######################
        (j2selected, unselected_js) = _mk_unselected_js(L, selected_js)
        if not len(selected_js) + len(unselected_js) == L: raise TypeError #duplicate j in selected_js
        ######################
        sf.partial_factorization = partial_factorization
        sf.j2selected = j2selected
        sf.selected_js = selected_js
        sf.unselected_js = unselected_js
        ######################
        return
    def get_core_vars(sf, /):
        partial_factorization = sf.partial_factorization
        unselected_js = sf.unselected_js
        selected_js = sf.selected_js
        return (partial_factorization, selected_js, unselected_js)
    @CachedProperty
    def _prepare4primality_test(sf, /):
        (partial_factorization, selected_js, unselected_js) = sf.get_core_vars()
        ######################
        (j2ft_ez, remain_ez, j2ft_odd, remain_odd) = partial_factorization._prepare4primality_test
        j2factor = partial_factorization.j2factor
        j2exp = partial_factorization.j2exp
        ######################
        common_odd_exp_pairs = [
            *((j2ft_odd[j], j2exp[j]) for j in unselected_js)
            ,(remain_odd, 1)
            ,*((j2ft_odd[j], j2exp[j]-1) for j in selected_js)
            ]
        common_odd_exp_pairs = tuple((odd, e) for odd, e in common_odd_exp_pairs if not (odd==1 or e==0))
        assert tuple((odd>=3 and e>=1) for odd, e in common_odd_exp_pairs)

        ######################
        common_ez_exp_pairs = [
            *((j2ft_ez[j], j2exp[j]) for j in unselected_js)
            ,(remain_ez, 1)
            ,*((j2ft_ez[j], j2exp[j]-1) for j in selected_js)
            ]
        common_ez_exp_pairs = tuple((ez, e) for ez, e in common_ez_exp_pairs if not (ez==0 or e==0))
        assert tuple((ez>=1 and e>=1) for ez, e in common_ez_exp_pairs)
        common_ez = sum(ez*e for ez, e in common_ez_exp_pairs)
        common_ez_exp_pairs = None
        ######################
        #list_values__via_idc_
        selected_ezs = tuple(j2ft_ez[j] for j in selected_js)
            # NOTE:ft_ez may be 0
        selected_odds = tuple(j2ft_odd[j] for j in selected_js)
            # NOTE:ft_odd may be 1
        selected_factors = tuple(j2factor[j] for j in selected_js)
        ######################
        common_odd_exp_pairs
        common_ez
        selected_ezs
        selected_odds
        selected_factors
        ######################
        (total_ez, total_odd) = partial_factorization.ez_odd_pair
        total_common_odd = II__ft_e_pairs_(common_odd_exp_pairs)

        assert common_ez + sum(selected_ezs) == total_ez
        assert total_common_odd * II(selected_odds) == total_odd
        assert (total_common_odd << common_ez) * II(selected_factors) == partial_factorization.N
        ######################
        selected_ezs
        selected_odds
        selected_js4ft_odd_eq1 = tuple(j for j, ft_odd in zip(selected_js, selected_odds) if ft_odd==1)
            # 2pow:zpow: [ft == 2**e2 == 2**ez]
        selected_js4ft_ez_eq0 = tuple(j for j, ft_ez in zip(selected_js, selected_ezs) if ft_ez==0)
            # odd: [ft == ft_odd]
        selected_nonzpow_ft_odds = tuple(ft_odd for ft_odd in selected_odds if not ft_odd==1)
        assert II(selected_odds) == II(selected_nonzpow_ft_odds)
        total_selected_ez = sum(selected_ezs)
        selected_ezs = None
        selected_odds = None
        ######################
        may_j4min_zpow_ft_ez = min(selected_js4ft_odd_eq1, default=None, key=j2ft_ez.__getitem__)
        may_min_zpow_ft_ez = None if may_j4min_zpow_ft_ez is None else j2ft_ez[may_j4min_zpow_ft_ez]
        assert may_min_zpow_ft_ez is None or 1 <= may_min_zpow_ft_ez <= total_ez
        ######################
        j2tribool_selected = [*sf.j2selected]
        for j in selected_js4ft_odd_eq1:
            j2tribool_selected[j] = ...
        j2tribool_selected = tuple(j2tribool_selected)
            # False: unselected_js
            # ...: selected_js && [ft_odd == 1]
            # True: selected_js && [ft_odd >= 3]
        selected_js4ft_odd_ge3 = tuple(j for j, x in enumerate(j2tribool_selected) if x is True)
        #list_values__via_idc_
        selected_zpow_factors = tuple(j2factor[j] for j in selected_js4ft_odd_eq1)
        selected_nonzpow_factors = tuple(j2factor[j] for j in selected_js4ft_odd_ge3)
        total_selected_zpow_ft_ez = sum(j2ft_ez[j] for j in selected_js4ft_odd_eq1)
        #bug:total_selected_zpow_ft_ez = sum(j2ft_ez[j]*j2exp[j] for j in selected_js4ft_odd_eq1)
        ######################
        selected_js4ft_odd_eq1
        selected_js4ft_odd_ge3
        selected_zpow_factors
        selected_nonzpow_factors
        total_selected_zpow_ft_ez
        ######################
        #
        common_odd_exp_pairs
        common_ez
        selected_factors
        ######################
        # [(total_common_odd*II(selected_nonzpow_ft_odds)) << total_ez == partial_factorization.N]
        #   for composite
        # [(total_common_odd << common_ez) * II(selected_factors) == partial_factorization.N]
        #   for prime
        # 2 path:
        #   * primality_test_of_Miller_Rabin:
        #       [g**(Nmm///2**total_ez) %N == g**total_odd %N == g**(total_common_odd*II(selected_nonzpow_ft_odds)) %N]
        #   * validate_discrete_logarithm:
        #       [g**(Nmm///ft) %N %N == (g**((total_common_odd*2**common_ez) *(II(selected_factors) ///ft)) %N]
        #   * validate_discrete_logarithm after pass primality_test_of_Miller_Rabin:
        #       [g**(Nmm///ft) %N %N == (g**((total_common_odd*2**common_ez) *2**total_selected_zpow_ft_ez *(II(selected_nonzpow_factors) ///ft)) %N]
        # total_common_odd <-- common_odd_exp_pairs
        # total_common_odd --> (total_common_odd*II(selected_nonzpow_ft_odds)) --> (total_common_odd*II(selected_nonzpow_ft_odds)) *2**(total_ez -j2ft_ez[selected_js4ft_odd_eq1[?]]) #may_min_zpow_ft_ez
        # total_common_odd --> (total_common_odd*2**common_ez) --> ((total_common_odd*2**common_ez) *(II(selected_factors) ///ft))
        # total_common_odd --> (total_common_odd*2**common_ez) --> ((total_common_odd*2**common_ez) *2**total_selected_zpow_ft_ez *(II(selected_nonzpow_factors) ///ft))
        return (common_odd_exp_pairs, (selected_nonzpow_ft_odds, total_ez, may_min_zpow_ft_ez, selected_js4ft_odd_eq1), (common_ez, selected_factors, selected_js), (total_selected_zpow_ft_ez, selected_nonzpow_factors, selected_js4ft_odd_ge3))
        return (common_odd_exp_pairs, (selected_nonzpow_ft_odds, total_ez, j2ft_ez, selected_js4ft_odd_eq1), (common_ez, selected_factors))
        return (common_odd_exp_pairs, common_ez, selected_factors)

def _mk_unselected_js(L, selected_js, /):
    j2selected = [False]*L
    for j in selected_js:
        j2selected[j] = True
    j2selected = tuple(j2selected)
    unselected_js = tuple(j for j, selected in enumerate(j2selected) if not selected)
    return (j2selected, unselected_js)
#PartialFactorization__with_selected_indices(partial_factorization, selected_js)
#PartialFactorization(j2factor, j2exp, j2prime_factor_lowbound, remain_factor, N=None)
def __():
    partial_factorization = PartialFactorization([2, 3, 6, 10, 14, 4], [4, 3, 2, 1, 2, 3], [2, 3, 2, 2, 2, 2], 44, 2**4 * 3**3 * 6**2 * 10**1 * 14**2 * 4**3   *44)
    sf = PartialFactorization__with_selected_indices(partial_factorization, [0,2,3,4,5])
    #(common_odd_exp_pairs, common_ez, selected_factors) = sf._prepare4primality_test
    (common_odd_exp_pairs, (selected_nonzpow_ft_odds, total_ez, may_min_zpow_ft_ez, selected_js4ft_odd_eq1), (common_ez, selected_factors, selected_js), (total_selected_zpow_ft_ez, selected_nonzpow_factors, selected_js4ft_odd_ge3)) = sf._prepare4primality_test
    if 0b00:print(sf._prepare4primality_test)
        #(((3, 3), (11, 1), (3, 1), (7, 1)), ((3, 5, 7), 17, 1), (11, (2, 6, 10, 14, 4)), (3, (6, 10, 14)))
    assert common_odd_exp_pairs == ((3, 3), (11, 1), (3, 1), (7, 1))

    assert selected_nonzpow_ft_odds == (3, 5, 7)
    assert total_ez == 17
    assert may_min_zpow_ft_ez == 1
    assert selected_js4ft_odd_eq1 == (0, 5)

    assert common_ez == 11
    assert selected_factors == (2, 6, 10, 14, 4)
    assert selected_js == (0, 2, 3, 4, 5)
    assert total_selected_zpow_ft_ez == 3 == 1+2 # 2*4 # not (2**4 * 4**3)
    assert selected_nonzpow_factors == (6, 10, 14)
    assert selected_js4ft_odd_ge3 == (2, 3, 4)
    assert ((II__ft_e_pairs_(common_odd_exp_pairs) * II(selected_nonzpow_ft_odds)) << total_ez) == partial_factorization.N
        #for primality_test_of_Miller_Rabin
    assert ((II__ft_e_pairs_(common_odd_exp_pairs) << common_ez) * II(selected_factors)) == partial_factorization.N
        #for validate_discrete_logarithm
    assert ((II__ft_e_pairs_(common_odd_exp_pairs) << common_ez) *2**total_selected_zpow_ft_ez * II(selected_nonzpow_factors)) == partial_factorization.N
        #for validate_discrete_logarithm if pass primality_test_of_Miller_Rabin
__()

######################
######################
class PrimalityTester__via_even_Nmm(_Immutable):
    'to detect partial_pseudo_primitive_root/witness4composite/nontrivial_factor'
    def __init__(sf, js_partial_factorization4Nmm, /):
        check_type_is(PartialFactorization__with_selected_indices, js_partial_factorization4Nmm)
        sf.js_partial_factorization4Nmm = js_partial_factorization4Nmm

        ######################
        N = sf.N
        check_int_ge(2, N)
        # [N >= 2]
        if not is_odd(N):
            # [N%2 == 0][N >= 2]
            if N == 2:
                raise IsPrime__Two
            # [N%2 == 0][N >= 4]
            raise IsComposite__nontrivial_factor(2)
        # [N%2 == 1][N >= 3]

        ######################
        return

    @CachedProperty
    def partial_factorization4Nmm(sf, /):
        return sf.js_partial_factorization4Nmm.partial_factorization
    @CachedProperty
    def selected_js(sf, /):
        return sf.js_partial_factorization4Nmm.selected_js

    @CachedProperty
    def Nmm(sf, /):
        Nmm = sf.partial_factorization4Nmm.N
        return Nmm
    @CachedProperty
    def N(sf, /):
        N = sf.partial_factorization4Nmm.Npp
        return N

    def _test(sf, g, /, *, _4prime, _4composite, using_gcd):
        '-> (may_result4composite, may_result4prime)/(may (zg_ls, dlog2_g4total_odd), may (js4g, may__g0_is_g4zpow)) | ^IsPrime__Two | ^IsComposite__nontrivial_factor | ^IsComposite__Nmm__witness4composite'
        # [N%2 == 1][N >= 3]

        N = sf.N
        Nmm = sf.Nmm

        if not using_gcd:
            if not sf.partial_factorization4Nmm.factorization_is_complete: raise TypeError

        g0 = g
        g = None
        g_N = g0 %N
        if not 2 <= g_N < N: raise TypeError
        # [g_N <- [2..<N]]
        if is_odd(g_N) and N %g_N == 0:
            raise IsComposite__nontrivial_factor(g_N)
        # [g_N <- [2..<N]][N %g_N =!= 0]


        ######################
        # [N%2 == 1][N >= 3]
        # [g_N <- [2..<N]][N %g_N =!= 0]
        #(common_odd_exp_pairs, common_ez, selected_factors) = sf._prepare4primality_test
        (common_odd_exp_pairs, (selected_nonzpow_ft_odds, total_ez, may_min_zpow_ft_ez, selected_js4ft_odd_eq1), (common_ez, selected_factors, selected_js), (total_selected_zpow_ft_ez, selected_nonzpow_factors, selected_js4ft_odd_ge3)) = sf.js_partial_factorization4Nmm._prepare4primality_test


        p1_n1 = (1, Nmm)
        def _pow(gg, e, /):
            if gg == Nmm:
                # [gg =[%N]= -1]
                if is_odd(e):
                    # [gg**e =[%N]= -1]
                    return Nmm
                else:
                    # [gg**e =[%N]= 1]
                    return 1
            else:
                return pow(gg, e, N)
        if 0:
            def _pow(gg, e, /):
                if gg in p1_n1:
                    raise _P1N1 #bug: depends on e
                else:
                    return pow(gg, e, N)
        def _pow__fts(gg, fts, /):
            '-> gg**II(fts) %N'
            for ft in fts:
                gg = _pow(gg, ft)
            return gg
        def _iter_fts(ft_e_pairs, /):
            for ft, e in ft_e_pairs:
                for _ in range(e):
                    yield ft
        def _pow__ft_e_pairs(gg, ft_e_pairs, /):
            '-> gg**II__ft_e_pairs_(ft_e_pairs) %N'
            return _pow__fts(gg, _iter_fts(ft_e_pairs))




        ######################
        assert _4composite or _4prime
        assert total_ez >= 1
        # [total_ez >= 1]

        g4common_odd = _pow__ft_e_pairs(g_N, common_odd_exp_pairs)
        # [g4common_odd == g**total_common_odd %N == g**(total_odd///II(selected_nonzpow_ft_odds)) %N]
        if 0:
            if g4common_odd in p1_n1:
                # pass primality_test_of_Miller_Rabin
                # but g is not partial_pseudo_primitive_root for any selected j
                # !!! 不同g，找出 部分伪本原根，不断缩减selected_js
                pass

        g4common_odd
        ######################
        g4common_odd
        if _4composite:
            #primality_test_of_Miller_Rabin
            # g**(Nmm///2**total_ez) %N == g**total_odd %N == g**(total_common_odd*II(selected_nonzpow_ft_odds)) %N]
            #
            g4total_odd = _pow__fts(g4common_odd, selected_nonzpow_ft_odds)
            # [g4total_odd == g**total_odd %N == g4common_odd**II(selected_nonzpow_ft_odds) %N]

            # [total_ez >= 1]
            gg = g4total_odd
            zg_ls = [gg]
            if gg in p1_n1:
                pass
            else:
                for _ in range(total_ez-1):
                    gg = pow(gg, 2, N)
                    zg_ls.append(gg)
                    if gg == Nmm:
                        break
                else:
                    raise _raise_witness4composite(N, g0, g_N)
            zg_ls = tuple(zg_ls)
            if zg_ls[-1] == Nmm:
                zg_ls.append(1)
            assert zg_ls
            assert zg_ls[-1] == 1
            assert len(zg_ls)==1 or zg_ls[-2] == Nmm
            assert (len(zg_ls)==1) is (g4total_odd==1)

            zg_ls
            dlog2_g4total_odd = len(zg_ls)-1
            # [1+dlog2_g4total_odd = len(zg_ls)]
            # [dlog2_g4total_odd >= 0]
            # [g4total_odd**(1<<dlog2_g4total_odd) %N == 1]
            #
            # [g4total_odd == 1] <==> [dlog2_g4total_odd == 0]
            # [[dlog2_g4total_odd > 0] -> [g4total_odd**(1<<(dlog2_g4total_odd-1)) %N == Nmm]]
            #
            g4total_odd
            zg_ls
            dlog2_g4total_odd
            may_result4composite = (zg_ls, dlog2_g4total_odd)
        else:
            may_result4composite = None
        may_result4composite

        ######################
        g4common_odd
        js4g = []
        pass_M_R_test = _4composite
        known__g0_order_divs_Nmm = _4composite
        if _4prime:
            if pass_M_R_test:# and not may_min_zpow_ft_ez is None:
                # validate_discrete_logarithm after pass primality_test_of_Miller_Rabin
                g4total_odd
                zg_ls
                dlog2_g4total_odd
                (selected_nonzpow_ft_odds, total_ez, may_min_zpow_ft_ez, selected_js4ft_odd_eq1)
                if not may_min_zpow_ft_ez is None:
                    min_zpow_ft_ez = may_min_zpow_ft_ez
                    assert 1 <= min_zpow_ft_ez <= total_ez
                    # [1 <= min_zpow_ft_ez <= total_ez]
                    #
                    # 3 eqv:
                    #   gg = pow(g0, Nmm>>min_zpow_ft_ez, N)
                    #   gg = pow(g4total_odd, 2**(total_ez-min_zpow_ft_ez), N)
                    #   gg = zg_ls[(total_ez-min_zpow_ft_ez)] if not overflow
                    #
                    #g0_is_g4zpow = (total_ez-min_zpow_ft_ez) < dlog2_g4total_odd
                        # g0_is_g4zpow = g0_is_g2
                    if (total_ez-min_zpow_ft_ez) < dlog2_g4total_odd:
                        # !! [1+dlog2_g4total_odd = len(zg_ls)]
                        # !! [(total_ez-min_zpow_ft_ez) < dlog2_g4total_odd]
                        # !! [1 <= min_zpow_ft_ez <= total_ez]
                        # [0 <= (total_ez-min_zpow_ft_ez) < len(zg_ls)-1]
                        gg = zg_ls[(total_ez-min_zpow_ft_ez)]
                        # [gg =!= 1]
                        if using_gcd:
                            g0_is_g4zpow = (gcd(gg-1, N) == 1)
                        else:
                            g0_is_g4zpow = True
                        g0_is_g4zpow
                    else:
                        g0_is_g4zpow = False
                    g0_is_g4zpow
                    assert selected_js4ft_odd_eq1
                    js4g.extend(selected_js4ft_odd_eq1)
                    may__g0_is_g4zpow = g0_is_g4zpow
                else:
                    may__g0_is_g4zpow = None
                may__g0_is_g4zpow
            else:
                may__g0_is_g4zpow = None
            may__g0_is_g4zpow
            ######################
            g4common_odd
            common_ez
            g4common_part = _pow__ft_e_pairs(g4common_odd, [(2, common_ez)])
            if pass_M_R_test:# and not may_min_zpow_ft_ez is None:
                # validate_discrete_logarithm after pass primality_test_of_Miller_Rabin
                # [g**(Nmm///ft) %N %N == (g**((total_common_odd*2**common_ez) *2**total_selected_zpow_ft_ez *(II(selected_nonzpow_factors) ///ft)) %N]
                #
                (total_selected_zpow_ft_ez, selected_nonzpow_factors, selected_js4ft_odd_ge3)
                g_ = _pow__ft_e_pairs(g4common_part, [(2, total_selected_zpow_ft_ez)])
                fts_ = selected_nonzpow_factors
                js_ = selected_js4ft_odd_ge3
            else:
                #validate_discrete_logarithm
                # [g**(Nmm///ft) %N %N == (g**((total_common_odd*2**common_ez) *(II(selected_factors) ///ft)) %N]
                #
                (common_ez, selected_factors, selected_js)
                g_ = g4common_part
                fts_ = selected_factors
                js_ = selected_js
            g_, js_, fts_
            known__g0_order_divs_Nmm
            it = _iter_pow_II1_except_one_(_pow, fts_, g_)
            _js = []
            i = -1
            for (j, ft, r) in zip(js_, fts_, it):
                # [ft == j2factor[j]]
                # [r == g0**(Nmm///ft) %N]
                if not known__g0_order_divs_Nmm:
                    if not 1 == _pow(r, ft):
                        raise _raise_witness4composite(N, g0, g_N)
                    known__g0_order_divs_Nmm = True
                ok = (not r == 1) if not using_gcd else (gcd(r-1, N) == 1)
                if ok:
                    _js.append(j)
            else:
                i += 1
                assert i == len(js_) == len(fts_)
            js4g.extend(_js)
            js4g.sort()
            js4g = tuple(js4g)
            may__g0_is_g4zpow
            js4g
            may_result4prime = (js4g, may__g0_is_g4zpow)
        else:
            may_result4prime = None
        may_result4prime
        ######################
        may_result4composite
        may_result4prime
        ######################
        return (may_result4composite, may_result4prime)



    def test4prime(sf, g, /, *, using_gcd):
        sf._test(g, _4prime=True, _4composite=False, using_gcd=using_gcd)
    def test4composite(sf, g, /, *, using_gcd):
        sf._test(g, _4prime=False, _4composite=True, using_gcd=using_gcd)
    def test4prime_and_composite(sf, g, /, *, using_gcd):
        sf._test(g, _4prime=True, _4composite=True, using_gcd=using_gcd)

def _raise_witness4composite(N, g0, g_N, /):
    t = gcd(g_N, N)
    if not t == 1:
        raise IsComposite__nontrivial_factor(t)
    raise IsComposite__Nmm__witness4composite(g0)
#end-class PrimalityTester__via_even_Nmm(_Immutable):

class PrimalityCriterion(Enum):
    N_eq_2 = auto()
    complete_factorization4Nmm = auto()
    #square_case__len_reduced = auto()
    #square_case__basic = auto()
    #cubic_case = auto()
    factored_part_lowbound4Nmm_gt_sqrtN = auto()
        # [N < (e5B+1)**2]
    factored_part_lowbound4Nmm_gt_cubic_rootN = auto()
        # [(e5B+1)**2 <= N < (kB*eF +1) * ((_2_u_eF +r -kB)*eF +1)]

def may_find_suitable_primality_criterion4even_Nmm_(partial_factorization4Nmm, /, *, turnoff__detect_complete_factorization=False):
    '-> may (case/PrimalityCriterion, payload) | ^IsPrime__Two | ^IsComposite__nontrivial_factor'
    check_type_is(PartialFactorization, partial_factorization4Nmm)
    Nmm = partial_factorization4Nmm.N
    N = partial_factorization4Nmm.Npp
    C = PrimalityCriterion
    if is_odd(Nmm):
        assert 2 <= N == Nmm+1
        if N == 2:
            raise IsPrime__Two
            return (C.N_eq_2, None)
        raise IsComposite__nontrivial_factor(2)
        raise TypeError

    assert 2 <= Nmm < N == Nmm+1
    ######################
    L = partial_factorization4Nmm.L
    if not turnoff__detect_complete_factorization:
        if partial_factorization4Nmm.factorization_is_complete:
            selected_js = range(L)
            return (C.complete_factorization4Nmm, selected_js)

    ######################
    m = partial_factorization4Nmm.may_selected_js4CASE_factored_part_lowbound4Nmm_gt_sqrtN
    if not m is None:
        selected_js = m
        return (C.factored_part_lowbound4Nmm_gt_sqrtN, selected_js)

    ######################
    m = partial_factorization4Nmm.may_selected_js_ex4CASE_factored_part_lowbound4Nmm_gt_cubic_rootN
        # ^IsComposite__nontrivial_factor
    if not m is None:
        (must_be_composite, selected_js) = m
        return (C.factored_part_lowbound4Nmm_gt_cubic_rootN, (must_be_composite, selected_js))

    ######################
    return None


def mk_ex____PrimalityTester__via_even_Nmm(partial_factorization4Nmm, /):
    '-> (must_be_composite, PrimalityTester__via_even_Nmm) | ^IsPrime__Two | ^IsComposite__nontrivial_factor'
    case, payload = may_find_suitable_primality_criterion4even_Nmm_(partial_factorization4Nmm)
        # ^IsPrime__Two
        # ^IsComposite__nontrivial_factor
    C = PrimalityCriterion
    must_be_composite = False
    if case is C.complete_factorization4Nmm:
        selected_js = payload
    elif case is C.factored_part_lowbound4Nmm_gt_sqrtN:
        selected_js = payload
    elif case is C.factored_part_lowbound4Nmm_gt_cubic_rootN:
        (must_be_composite, selected_js) = payload
    else:
        raise 000
    must_be_composite
    selected_js
    js_partial_factorization4Nmm = PartialFactorization__with_selected_indices(partial_factorization4Nmm, selected_js)
    tester = PrimalityTester__via_even_Nmm(js_partial_factorization4Nmm)
    return (must_be_composite, tester)


r'''[[[
def _validate_primality__Nmm_(js_partial_factorization4Nmm, g, /):
    check_type_is(PartialFactorization__with_selected_indices, js_partial_factorization4Nmm)
    check_type_is(int, g)

    sf4Nmm = js_partial_factorization4Nmm
    partial_factorization4Nmm = sf4Nmm.partial_factorization
    ######################
    Nmm = partial_factorization4Nmm.N
    N = partial_factorization4Nmm.Npp
    ######################
    check_int_ge(2, N)
    # [N >= 2]
    if not is_odd(N):
        # [N%2 == 0][N >= 2]
        if N == 2:
            raise IsPrime__Two
        # [N%2 == 0][N >= 4]
        raise IsComposite__nontrivial_factor(2)
    # [N%2 == 1][N >= 3]

    ######################
    if 0:
        if not -Nmm < g < N: raise TypeError
        if 0 <= g < 2: raise TypeError
    g_N = g %N
    if not 2 <= g_N < N: raise TypeError
    # [g_N <- [2..<N]]
    if is_odd(g_N) and N %g_N == 0:
        raise IsComposite__nontrivial_factor(g_N)
    # [g_N <- [2..<N]][N %g_N =!= 0]


    ######################
    # [N%2 == 1][N >= 3]
    # [g_N <- [2..<N]][N %g_N =!= 0]
    (common_odd_exp_pairs, common_ez, selected_factors) = sf4Nmm._prepare4primality_test
    (total_ez, total_odd) = partial_factorization4Nmm.ez_odd_pair
    assert total_ez >= 1

    def _pow(gg, e, /):
        if gg == Nmm:
            # [gg =[%N]= -1]
            if is_odd(e):
                # [gg**e =[%N]= -1]
                return Nmm
            else:
                # [gg**e =[%N]= 1]
                return 1
        else:
            return pow(gg, e, N)

    gg = g_N
    for odd, e in common_odd_exp_pairs:
        for _ in range(e):
            gg = _pow(gg, odd)
    gg
    if gg == 1:
    if gg == Nmm:


import





class IResult(ABC, BaseException):
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        pass
    @abstractmethod
    def is_prime__tribool_(sf, /):
        pass
    @abstractmethod
    def get_N(sf, /):
        pass
    @abstractmethod
    def validate(sf, /):
        pass
class IResult__is_prime(IResult):
    @abstractmethod
    def is_prime__tribool_(sf, /):
        return True
class IResult__is_composite(IResult):
    @abstractmethod
    def is_prime__tribool_(sf, /):
        return False
class IResult__unclear_yet(IResult):
    @abstractmethod
    def is_prime__tribool_(sf, /):
        return ...
class IsPrime__Two(IResult__is_prime):
    @override
    def validate(sf, /):
        assert sf.get_N() == 2
class IsComposite__nontrivial_factor(IResult__is_composite):
    'nontrivial_factor'
class IsComposite__Nmm__witness4composite(IResult__is_composite):
    'witness4composite'
    # [[gcd(g, N) == 1][g**(N-1) %N =!= 1]]
    #       otherwise:
    #           [not$ [gcd(g, N) == 1]] may lead to nontrivial_factor
    #           [g**(N-1) %N == 1][@e. (g**(N-1)///2**e) %N =!= -1 %N] may lead to nontrivial_factor
    #

class IsPrime__Nmm__complete_factorization__prime_factor2partial_primitive_root(IResult__is_prime):
    'complete_factorization #prime_factor2partial_primitive_root'
class IsPrime__Nmm__complete_factorization__prime_factors_and_primitive_root(IResult__is_prime):
    'complete_factorization #(prime_factors, partial_primitive_root)'
class IsPrime__Nmm__factored_part_ge_sqrtN(IResult__is_prime):
too_few_num_prime_bases
cannot_conform_primality

  ???primality test???
  ???primality categorize???
  ???primality criterion???
  may_find_suitable_primality_criterion4even_Nmm_
from enum import Enum, auto
class PrimalityCriterion(Enum):
    N_eq_2 = auto()
    complete_factorization = auto()
    square_case__len_reduced = auto()
    square_case__basic = auto()
    cubic_case = auto()
    # True & [unfactored_part4Nmm > 1]:
    factored_part4Nmm_ge_sqrtN = auto()
    factored_part4Nmm_ge_cubic_rootN = auto()
#]]]'''#'''

def __():
    from seed.tiny import ifNonef, ifNone, echo
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.helper.repr_input import repr_helper

def __():
    from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
    from seed.helper.repr_input import repr_helper
    class _(ABC):
        __slots__ = ()
        raise NotImplementedError
        ___no_slots_ok___ = True
        def __repr__(sf, /):
            #return repr_helper(sf, *args, **kwargs)
            #return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
            ...
if __name__ == "__main__":
    pass
__all__


from seed.math.primality_proving import *
