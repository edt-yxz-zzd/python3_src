#__all__:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint_as_pefect_power_.py
view others/数学/整数分解/整数幂方分解.txt

[[
CRT-ver-factor_pint_as_pefect_power_:
    O(lbN**3/lblbN)
        lbN**3 come from:
            apply_raw_CRT__inc::num_ps4rt<k>**3

    CRT-ver little better than floor_kth_root_-ver which gives:O(lbN**3)
        CRT-ver:
            [total k == O(lbN/lb_max_p/lblbN) == O(lbN/lblbN**2)]
                #since trial_division enlarge min prime factor(k-th root) of n

        floor_kth_root_-ver:
            [total k == O(lbN/lblbN)]
                # since k is prime
            per k:O(lbN**2 *lblbN)
            total:O(lbN**3)

CRT-ver-detect_pefect_kth_root_:
    O(lbN**3 *(k///odd4k)/k**3 +lbN**2)
    CRT-ver worse than floor_kth_root_-ver which gives: O(lbN**2 *lblbN)

]]




seed.math.factor_pint_as_pefect_power_
py -m nn_ns.app.debug_cmd   seed.math.factor_pint_as_pefect_power_ -x
py -m nn_ns.app.doctest_cmd seed.math.factor_pint_as_pefect_power_:__doc__ -ff -v

py_adhoc_call   seed.math.factor_pint_as_pefect_power_   @factor_pint_as_pefect_power_  ='257**99'
py_adhoc_call   seed.math.factor_pint_as_pefect_power_   @factor_pint_as_pefect_power_  ='(2**19-1)**99' +verbose

py_adhoc_call   seed.math.factor_pint_as_pefect_power_   @factor_pint_as_pefect_power_  ='257**7' +verbose
py_adhoc_call   seed.math.factor_pint_as_pefect_power_   @factor_pint_as_pefect_power_  ='(257*53)**7' +verbose
...  ...
iter_prime_bases4pefect_kth_root_(3) yield 47
_find_enough_prime_bases_(3, 86988722019525492386235967741) : n:86988722019525492386235967741**II({}) : new prime base 47
iter_prime_bases4pefect_kth_root_(3) yield 53
_find_enough_prime_bases_(3, 86988722019525492386235967741) : n:86988722019525492386235967741///53**7-->74051159531521793
main():loop _k=3: _n:86988722019525492386235967741///II(_p2e4n)-->74051159531521793
main():loop _k=3: _n:74051159531521793
main():loop k_=1
main():loop may_p2e4gcd4e5n={7: 1}
main():loop p2e4n_={53: 7}
main():loop _k=7
main():loop k_=1
main():loop may_p2e4gcd4e5n={7: 1}
main():loop p2e4n_={53: 7}
_detect_pefect_kth_root_(7, 74051159531521793)
_detect_pefect_kth_root_(7, 74051159531521793):odd prime k
...  ...

py_adhoc_call   seed.math.factor_pint_as_pefect_power_   @factor_pint_as_pefect_power_  ='(257*101)**7' +verbose


py_adhoc_call   seed.math.factor_pint_as_pefect_power_   @factor_pint_as_pefect_power_  ='(257*71)**7' +verbose
...  ...
_detect_pefect_kth_root_(7, 673504193807371699307428315063):odd prime k: n:673504193807371699307428315063: rt=?=18247: new prime base to confirm result: 71: found new prime factor
...  ...

py_adhoc_call   seed.math.factor_pint_as_pefect_power_   @factor_pint_as_pefect_power_  ='257*53**2' +verbose

py_adhoc_call   seed.math.factor_pint_as_pefect_power_   @factor_pint_as_pefect_power_  ='257*3**23' +verbose


>>> factor_pint_as_pefect_power_(257*3**23)
(24194796958539, 1)
>>> factor_pint_as_pefect_power_(257*53**2)
(721913, 1)
>>> factor_pint_as_pefect_power_((257*71)**7)
(18247, 7)
>>> factor_pint_as_pefect_power_((257*101)**7)
(25957, 7)
>>> factor_pint_as_pefect_power_((257*53)**7)
(13621, 7)
>>> factor_pint_as_pefect_power_(257**7)
(257, 7)
>>> factor_pint_as_pefect_power_((2**19-1)**99)
(524287, 99)
>>> factor_pint_as_pefect_power_(257**99)
(257, 99)
>>> factor_pint_as_pefect_power_(1)
Traceback (most recent call last):
    ...
ValueError: 1
>>> factor_pint_as_pefect_power_(2)
(2, 1)
>>> factor_pint_as_pefect_power_(3)
(3, 1)
>>> factor_pint_as_pefect_power_(4)
(2, 2)
>>> factor_pint_as_pefect_power_(5)
(5, 1)
>>> factor_pint_as_pefect_power_(6)
(6, 1)
>>> factor_pint_as_pefect_power_(7)
(7, 1)
>>> factor_pint_as_pefect_power_(8)
(2, 3)
>>> factor_pint_as_pefect_power_(9)
(3, 2)
>>> factor_pint_as_pefect_power_(10)
(10, 1)
>>> factor_pint_as_pefect_power_(11)
(11, 1)
>>> factor_pint_as_pefect_power_(11**2)
(11, 2)
>>> factor_pint_as_pefect_power_(101)
(101, 1)
>>> factor_pint_as_pefect_power_(101*103)
(10403, 1)


#]]]'''
__all__ = r'''
    factor_pint_as_pefect_power_
'''.split()#'''
__all__

from itertools import count as count_
from seed.tiny import check_type_is
from seed.math.floor_ceil import floor_log2, ceil_log2
from seed.math.floor_ceil import floor_log2_kth_root_, ceil_log2_kth_root_
from seed.math.floor_ceil import floor_sqrt, ceil_sqrt

from seed.math.sqrts_mod_ import is_square_residual_mod_prime_power_, is_square_residual_mod_prime_
from seed.math.sqrts_mod_ import iter_sqrts_mod_prime_power_, iter_sqrts_mod_prime_power__coprime__5one_sqrt_
from seed.math.inv_mod_ex import inv_mod_power__coprime_
from seed.math.inv_mod_ex import ginv_mod_
    #(inv_x_g, k4M, k4x, gcd_of_Mx, M_g, x_g) = ginv_mod_(M, x)

from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_2_powers, factor_pint_out_power_of_base_
from seed.math.factor_pint_by_trial_division_ import factor_pint_by_trial_division_ex_, default4upperbound4probably_prime, check_result5factor_pint_
from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
from seed.math.II import II, II__p2e_#, II_mod
from seed.math.prime_gens import prime_gen
from seed.math.gcd import gcd, gcd_many#, are_coprime
from seed.math.Chinese_Remainder_Theorem import apply_raw_CRT__inc, mk_coeff_pairs4apply_raw_CRT__inc
def __():
    # API:
    def apply_raw_CRT__inc(us, vs, coeff_pairs, rs, /, *, partial_ok=False):
        r'''[[[
        'moduli/[pint] -> accumulated_partial_moduli/[pint] -> coeff_pairs/[(uint%moduli[i], uint%accumulated_partial_moduli[i])] -> remainders/[uint%moduli[i]] -> whole_remainder/uint%whole_modulus'

        'us/[pint] -> vs/[pint]{.len==1+len(us);.[i]==II(us[:i])} -> coeff_pairs/[(uint%us[i], uint%vs[i])]{.[i]==(vs[i]*inv_mod_(us[i];vs[i]), us[i]*inv_mod_(vs[i];us[i])))} -> remainders/[uint%us[i]]{len==len(us)} -> whole_remainder/uint%vs[-1]'
        #]]]'''#'''
    def mk_coeff_pair4apply_raw_CRT__inc(u, v, /):
        'u -> v -> (coeff4u, coeff4v){coeff4x == inv_mod_(x;y)*y %(x*y)} |^CRT_Error__moduli_not_coprime if [gcd(u,v) =!= 1]'
    def mk_coeff_pairs4apply_raw_CRT__inc(us, vs, /):
        'us/[pint] -> vs/{.len=1+len(us)}{vs[i]==II(us[:i])} -> coeff_pairs/[(coeff4u, coeff4v)]{coeff4x == inv_mod_(x;y)*y %(x*y)} |^CRT_Error__moduli_not_coprime if [gcd(u[i],v[i]) =!= 1]'
    def mk_accumulated_partial_moduli4apply_raw_CRT__inc(us, /):
        'us/[pint] -> vs/{.len=1+len(us)}{vs[i]==II(us[:i])}'
    def prepare4apply_raw_CRT__inc(us, /):
        'us/[pint] -> (vs/{.len=1+len(us)}{vs[i]==II(us[:i])}, coeff_pairs/[(coeff4u, coeff4v)]{coeff4x == inv_mod_(x;y)*y %(x*y)}) |^CRT_Error__moduli_not_coprime if [gcd(u[i],v[i]) =!= 1]'



def __():
    def detect_pefect_quotient_(n, d, /):
        'n/uint -> d/pint -> may q/uint # [[result is None] =!= [n%d==0]][q == n///d]'
        r'''[[[
        if d is small near 0, then divmod(n,d) is fast enough
            since to apply Chinese_Remainder_Theorem, we need to call n%p
        if d is large near n, then divmod(n,d) is fast, too
        if d,q near sqrt(n):
            is Chinese_Remainder_Theorem useful?
            [II(ps) > n]
                [O(len(ps)) ~= log2(n)]
            [ns := {n%p | [p :<- ps]}]
                O(log2(n))*time4mod
                O(log2(n)**2)
            not better than divmod(n,d)
        #]]]'''#'''


def factor_pint_as_pefect_power_(n, /, *, verbose=False):
    r'''[[[
    'n/int{>=2} -> (base/int{>=2}, exp/int{>=1}){n==base**exp}'

    O(lbN**3/lblbN)
        lbN**3 come from:
            apply_raw_CRT__inc::num_ps4rt<k>**3

    CRT-ver little better than floor_kth_root_-ver which gives:O(lbN**3)
        CRT-ver:
            [total k == O(lbN/lb_max_p/lblbN) == O(lbN/lblbN**2)]
                #since trial_division enlarge min prime factor(k-th root) of n

        floor_kth_root_-ver:
            [total k == O(lbN/lblbN)]
                # since k is prime
            per k:O(lbN**2 *lblbN)
            total:O(lbN**3)

######################
######################vs:
O(bisearch-ver:floor_kth_root_) ~ O(log2(n)**3/k)
O(floor_sqrt) ~ O(log2(n)**2)
O(floor_kth_root_) ~:
    ######################
    let [mmm:=min{k*log2(k), log2(n)}]
    let [lbN:=log2(n)][lblbN:=log2(log2(n))]
    let [lbK:=log2(k)]
    ######################
    ~ O(mmm**3 /k + (lbN -mmm)**2)
    ######################
    ~ [0 <= lbN < k]:O(1)
    ~ [k <= lbN < k*lbK]:O(lbN**3 /k)
    ~ worst[lbN == k*lbK][k==lbN/lblbN]:O(lbN**2 *lblbN)
    ~ [k*lbK < lbN < k*lbK**(3/2)]:O(k**2 *lbK**3)
    ~ [lbN > k*lbK**(3/2)]:O(lbN**2)
    ######################



    #]]]'''#'''
    #cache:_get_ginv_mod_<{p-1:{_k:(gcd, may_inv_k)}}>
    #cache:_get_mod_<{p:(n,r4n)}>
    u2v2res4ginv = {}
    def _get5cache_(lazy_, d, /, *ks, **kwds):
        [*ks_, kl] = ks
        for k_ in ks_:
            d = d.setdefault(k_, {})
        if kl not in d:
            d[kl] = lazy_(*ks, **kwds)
        r = d[kl]
        return r
    p2b2e2pow = {}
    def lazy4pow_(p, base, exp, /):
        return pow(base, exp, p)
    def _pow_(base, exp, p, /):
        # [p :: prime]
        exp %= p-1
        base %= p
        return _get5cache_(lazy4pow_, p2b2e2pow, p, base, exp)
    def lazy4get_ginv_mod_(u, v, /):
        (inv_v_g, k4u, k4v, gcd_of_uv, u_g, v_g) = ginv_mod_(u, v)
        if gcd_of_uv == 1:
            may_inv_v_g = inv_v_g
        else:
            may_inv_v_g = None
        return gcd_of_uv, may_inv_v_g
    def _get_ginv_mod_(u, v, /):
        v = v%u
        return _get5cache_(lazy4get_ginv_mod_, u2v2res4ginv, u, v)
    def lazy4get_mod_(p, /, *, n):
        e4n, coprime4p = factor_pint_out_power_of_base_(p, n)
        r4n = coprime4p%p
        assert r4n
        if e4n==0:
            may_e4n = None
            may_n = None
        else:
            may_e4n = e4n
            may_n = coprime4p
        #
        _drop_prime_factor4n_(p)
        return n, may_n, may_e4n, r4n
    p2n_n_e_r = {}
    def _get_mod_(p, n, /):
        '-> (may_n, may_e4n, r4n)'
        n_, may_n, may_e4n, r4n = _get5cache_(lazy4get_mod_, p2n_n_e_r, p, n=n)
        if n is not n_:
            if not n < n_:
                raise 000
            del p2n_n_e_r[p]
            n_, may_n, may_e4n, r4n = _get5cache_(lazy4get_mod_, p2n_n_e_r, p, n=n)
        if n is not n_:
            raise 000
        return may_n, may_e4n, r4n
    lazy_prime_seq = prime_gen.get_or_mk_lazy_prime_seq_() # keep weakref
    _i4next_p4n = 0
    _lb_next_p4n = 1
    _handled_ps4n = set()
    def _drop_prime_factor4n_(p, /):
        nonlocal _i4next_p4n
        nonlocal _lb_next_p4n
        ls = lazy_prime_seq
        s = _handled_ps4n
        s.add(p)
        i = _i4next_p4n
        if p == ls[i]:
            #find next
            for i in count_(i+1):
                q = ls[i]
                if q not in s:
                    _i4next_p4n = i
                    _lb_next_p4n = floor_log2(q)
                    break

    def _get_floor_log2_possible_next_prime_factor4n_():
        return _lb_next_p4n


    def iter_prime_bases4pefect_kth_root_(k, /):
        if verbose:print(f'iter_prime_bases4pefect_kth_root_({k})')
        assert k&1
        # [k >= 3]
        # [k %2 == 1]
        # [k :: prime]
        for p in prime_gen:
            (gcd, may_inv_k) = _get_ginv_mod_(p-1, k)
            # ~O(lb_max_k*lb_max_p +lb_max_p**3)
            if not gcd == 1:
                assert may_inv_k is None
                continue
            if verbose:print(f'iter_prime_bases4pefect_kth_root_({k}) yield {p}')
            yield p
        # total ~O((lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n) #only output num_ps4rt < num_ps4n
    def _find_enough_prime_bases_(_k, _n, /):
        '-> (may_n, p2e4n, may (ps, Ms))'
        r'''[[[
        ######################
            '...+O((lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n)' #loop-total iter_prime_bases4pefect_kth_root_
            '...+O((lbN*lb_max_p)*num_ps4n)' #global-total _get_mod_
            '...+O(lb_max_p**2 *num_ps4rt<k>**2)' #loop-total build CRT moduli
        ######################
        '...+O((lbN*lb_max_p)*num_ps4n)' #global-total _get_mod_
        '...+O((lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n +(lb_max_p**2 *num_ps4rt<k>**2))'
            #per-call: _find_enough_prime_bases_:iter_prime_bases4pefect_kth_root_
            #per-call: _find_enough_prime_bases_:build CRT moduli

        #]]]'''#'''
        if verbose:n0 = _n
        if verbose:print(f'_find_enough_prime_bases_({_k}, {n0})')
        assert _k&1
        # [_k >= 3]
        # [_k %2 == 1]
        # [_k :: prime]
        # [lb_rt >= 1]
        # [_n >= 2]
        M = 1
        Ms = [M]
        ps = []
        p2e4n = {}
        lb_rt = floor_log2_kth_root_(_k, _n)
        if not lb_rt >= 1:
            return (None, p2e4n, None)
        # [lb_rt >= 1]
        for p in iter_prime_bases4pefect_kth_root_(_k):
            # [lb_rt >= 1]
            '...+O((lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n)' #loop-total iter_prime_bases4pefect_kth_root_
            may_n, may_e4n, r4n = _get_mod_(p, _n)
            '...+O((lbN*lb_max_p)*num_ps4n)' #global-total _get_mod_
            assert not r4n == 0
            if not may_n is None:
                assert may_n < _n
                # [new _n == old _n ///p**e4n]
                if verbose:print(f'_find_enough_prime_bases_({_k}, {n0}) : n:{_n}///{p}**{may_e4n}-->{may_n}')
                _n = may_n
                e4n = may_e4n
                p2e4n[p] = e4n
                assert e4n >= 1
                if not e4n % _k == 0:
                    return (may_n, p2e4n, None)
                lb_rt = floor_log2_kth_root_(_k, _n)
                if not lb_rt >= 1:
                    return (may_n, p2e4n, None)
                # [lb_rt >= 1]
                if floor_log2(M) > lb_rt:
                    # [floor_log2(Ms[-1]) > lb_rt]
                    break
            # [lb_rt >= 1]
            M *= p
            '...+O(lb_max_p**2 *num_ps4rt<k>**2)' #loop-total build CRT moduli
            Ms.append(M)
            ps.append(p)
            if verbose:print(f'_find_enough_prime_bases_({_k}, {n0}) : n:{_n}**II({p2e4n}) : new prime base {p}')
            if floor_log2(M) > lb_rt:
                # [floor_log2(Ms[-1]) > lb_rt]
                break
        # [lb_rt >= 1]
        # [floor_log2(Ms[-1]) > lb_rt]

        # !! [Ms[0] == 1]
        # [floor_log2(Ms[0]) == 0]
        # [floor_log2(Ms[0]) < lb_rt]
        # !! [floor_log2(Ms[-1]) > lb_rt]
        # [len(Ms) >= 2]
        while floor_log2(Ms[-2]) > lb_rt:
            # [floor_log2(Ms[-2]) > lb_rt]
            Ms.pop() #why? see:p2e4n
            # [floor_log2(Ms[-1]) > lb_rt]
        # [floor_log2(Ms[-1]) > lb_rt]
        # [floor_log2(Ms[-2]) <= lb_rt]
        # [len(Ms) >= 2]
        M = Ms[-1]
        del ps[len(Ms):]
        if verbose:print(f'_find_enough_prime_bases_({_k}, {n0}) : n:{_n}**II({p2e4n}) : prime bases {ps}')

        # postcondition:
            # [Ms[0] == 1]
            # [floor_log2(Ms[-2]) <= lb_rt]
            # [floor_log2(Ms[-1]) > lb_rt]
            # [II(ps[:i]) == Ms[i]]
            # [ps[i] :: prime]
            # [ps[i] < ps[i+1]]
            # [_n %ps[i] =!= 0]
            # [gcd(_k, ps[i]-1) == 1]
        return (may_n, p2e4n, (ps, Ms))
    def _detect_pefect_kth_root_(_k, _n, /):
        '-> (may_n, p2e4n, may rt)'
        r'''[[[
        ######################
        '...+O((lbN*lb_max_p)*num_ps4n)' #global-total _get_mod_
        '...+O((lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n +(lb_max_p**2 *num_ps4rt<k>**2))'
        '...+O(lb_max_p**2 *num_ps4rt<k>**2 + lb_max_p**3 *num_ps4rt<k>)'
        '...+O((lb_max_k*lb_max_p + lb_max_p**3)*num_ps4rt<k>)'
        '...+O(lb_max_p**2 *num_ps4rt<k>**3)'
        '...+O((lbN/k*lb_max_p + lb_max_k*lb_max_p + lb_max_p**3)*(num_ps4n-num_ps4rt<k>))'
        ######################
        '...+O((lbN*lb_max_p)*num_ps4n)' #global-total _get_mod_
        '...+O((lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n +((lbN/k*lb_max_p)*(num_ps4n-num_ps4rt<k>)) +(lb_max_p**2 *num_ps4rt<k>**3))'
            #per-call: _detect_pefect_kth_root_
        ######################
        #]]]'''#'''
        if verbose:n0 = _n
        if verbose:print(f'_detect_pefect_kth_root_({_k}, {n0})')
        # [_k >= 2]
        # [_k :: prime]
        # [n >= 2**_k >= 4]
        # [lb_rt >= 1]
        if _k == 2:
            _rt = floor_sqrt(_n)
            if _rt**2 == _n:
                return (None, {}, _rt)
            return (None, {}, None)
        if verbose:print(f'_detect_pefect_kth_root_({_k}, {n0}):odd prime k')
        # [_k >= 3]
        # [_k %2 == 1]
        may_n, p2e4n, m = _find_enough_prime_bases_(_k, _n)
        '...+O((lbN*lb_max_p)*num_ps4n)' #global-total _get_mod_
        '...+O((lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n +(lb_max_p**2 *num_ps4rt<k>**2))'
            #per-call: _find_enough_prime_bases_:iter_prime_bases4pefect_kth_root_
            #per-call: _find_enough_prime_bases_:build CRT moduli
        if m is None:
            return may_n, p2e4n, None
        if not may_n is None:
            assert may_n < _n
            # [n >= 2**_k >= 4]
            # [lb_rt >= 1]
            if verbose:print(f'_detect_pefect_kth_root_({_k}, {n0}):odd prime k: n:{_n}-->{may_n}')
            _n = may_n
        # [_k >= 2]
        # [n >= 2**_k >= 4]
        # [lb_rt >= 1]
        lb_rt = floor_log2_kth_root_(_k, _n)
        assert lb_rt >= 1
        assert _n >= 4
        assert _k >= 2

        (ps, Ms) = m
        coeff_pairs = mk_coeff_pairs4apply_raw_CRT__inc(ps, Ms)
        # ~O(sum (i*lb_max_p*lb_max_p +lb_max_p**3) {i :<- [0..<len ps]})
        # ~O(lb_max_p**2 *num_ps4rt**2 + lb_max_p**3 *num_ps4rt)
        '...+O(lb_max_p**2 *num_ps4rt<k>**2 + lb_max_p**3 *num_ps4rt<k>)'

        rs = []
        for p in ps:
            (may_n, may_e4n, r4n) = _get_mod_(p, _n) # %p
            '...+O(...)' #see:global total _get_mod_
            if not may_n is None:
                raise 000
            if not may_e4n is None:
                raise 000
            if r4n == 0:
                raise 000
            # [gcd(n, p) == 1]

            (gcd, may_inv_k) = _get_ginv_mod_(p-1, _k)
            '...+O(lb_max_k*lb_max_p)' #omit O(eval:inv(),gcd()) since cache exactly by iter_prime_bases4pefect_kth_root_; only EVAL(_k%(p-1))
            if not gcd == 1:
                raise 000
            # [gcd(k, p-1) == 1]
            if may_inv_k is None:
                raise 000
            inv_k = may_inv_k # %(p-1)
            r4n # == n %p
            inv_k # (1/k) %(p-1)
            # [rt**k == n]
            # [rt**k =[%p]= n]
            # [rt =[%p]= n**inv_k]
            # [rt =[%p]= (n%p)**inv_k]
            rt6p = _pow_(r4n, inv_k, p)
            '...+O(lb_max_p**3)'
            rs.append(rt6p)
        '...+O((lb_max_k*lb_max_p + lb_max_p**3)*num_ps4rt<k>)'
        _rt = apply_raw_CRT__inc(ps, Ms, coeff_pairs, rs)
        # ~O(sum (i*lb_max_p*i*lb_max_p) {i :<- [0..<len ps]})
        # ~O(lb_max_p**2 *num_ps4rt**3)
        '...+O(lb_max_p**2 *num_ps4rt<k>**3)'
        if verbose:print(f'_detect_pefect_kth_root_({_k}, {n0}):odd prime k: n:{_n}: rt=?={_rt}')
        if not floor_log2(_rt) == lb_rt:
            return may_n, p2e4n, None
        # !! [lb_rt >= 1]
        # [_rt >= 2]
        p_set = {*ps}
        remain_bits = ceil_log2(_n) -floor_log2(Ms[-1])
        extras = []
        ok = False
        for p in prime_gen:
            if p in p_set:
                continue
            if verbose:print(f'_detect_pefect_kth_root_({_k}, {n0}):odd prime k: n:{_n}: rt=?={_rt}: new prime base to confirm result: {p}')
            (may_n, may_e4n, r4n) = _get_mod_(p, _n) # %p
            '...+O(...)' #see:global total _get_mod_
            if not may_n is None:
                if verbose:print(f'_detect_pefect_kth_root_({_k}, {n0}):odd prime k: n:{_n}: rt=?={_rt}: new prime base to confirm result: {p}: found new prime factor')
                extras.append((p, may_n, may_e4n, r4n))
                r4n = 0
                pow_rt_k = _rt%p #not really the pow, but should be 0 if pass test
            else:
                r4n # %p
                pow_rt_k = _pow_(_rt%p, _k, p)
                '...+O(lbN/k*lb_max_p + lb_max_k*lb_max_p + lb_max_p**3)' # will eval (_k%(p-1))
            # eval (_rt%p) SHOULD NOT use _get_mod_() which cache for dec n's, not for arbitrary value _rt
            if not pow_rt_k == r4n:
                # [_rt**_k =!= _n]
                break #to handle "extras"
                return may_n, p2e4n, None
            remain_bits -= floor_log2(p)
            if remain_bits <= 0:
                # [_rt**_k == _n]
                ok = True
                break
        '...+O((lbN/k*lb_max_p + lb_max_k*lb_max_p + lb_max_p**3)*(num_ps4n-num_ps4rt<k>))'
        for (p, _may_n, _may_e4n, _r4n) in extras:
                # _may_e4n <<== since 『not ok』return may_n
            (may_n, may_e4n, r4n) = _get_mod_(p, _n) # %p
                # may_e4n <<== since 『not ok』return may_n
            if may_n is None:
                raise 000
            _n = may_n
            e4n = may_e4n
            p2e4n[p] = e4n
            assert e4n >= 1
            assert may_e4n == _may_e4n
            if not e4n % _k == 0:
                raise 000
        if ok:
            for (p, _may_n, _may_e4n, _r4n) in extras:
                # _may_e4n <<== since 『not ok』return may_n
                e4n = _may_e4n
                _rt //= p**(e4n//_k)
            # [_rt**_k == _n]




        if not ok:
            return may_n, p2e4n, None
        # [_rt**_k == _n]
        # [_rt >= 2]
        return (may_n, p2e4n, _rt)

    def main():
        # mainmain():goto
        check_type_is(int, n)
        if not n >= 2:raise ValueError(n)
        # [n >= 2]
        if not n >= 4:
            return (n, 1)
        # [n >= 4]
        ######################


        if 0:
            _n = n
            # [_n >= 4]
            # [_n >= 2]
            p2e4n_ = {}
            may_p2e4gcd4e5n = None
        else:
            # [_n >= 4]
            _2357 = (2,3,5,7)
            if 0:
                p2e4n_, _n = semi_factor_pint_via_trial_division(_2357, n)
                # [_n >= 1]
                for p in _2357:
                    _drop_prime_factor4n_(p)
            else:
                p2e4n_ = {}
                _n = n
                for p in _2357:
                    (may_n, may_e4n, r4n) = _get_mod_(p, _n) # %p
                    if may_n is not None:
                        _n = may_n
                        p2e4n_[p] = may_e4n
            # [_n >= 1]
            may_p2e4gcd4e5n = None
            if p2e4n_:
                may_p2e4gcd4e5n = p2e4gcd4e5n = _update_p2e4gcd4e5n_(may_p2e4gcd4e5n, p2e4n_)
                iter_sorted_keys_of_p2e4gcd4e5n = iter(sorted(p2e4gcd4e5n))
            #if _n == 1
        # [_n >= 1]
        k_ = 1
        # [n0 == (II__p2e_(p2e4n_)*_n)**k_]
        it = iter(prime_gen)
        while 1:
            if may_p2e4gcd4e5n is None:
                _k = next(it)
            else:
                p2e4gcd4e5n
                if not p2e4gcd4e5n:
                    break
                _k = next(iter_sorted_keys_of_p2e4gcd4e5n)
                #may_max_e4k = p2e4gcd4e5n[_k]
            _k

            # [n0 == (II__p2e_(p2e4n_)*_n)**k_]
            # [_n >= 1]
            lb_rt = floor_log2_kth_root_(_k, _n)
            # [lb_rt >= 0]
            if verbose:print(f'main():loop _k={_k}')
            if verbose:print(f'main():loop k_={k_}')
            if verbose:print(f'main():loop may_p2e4gcd4e5n={may_p2e4gcd4e5n}')
            if verbose:print(f'main():loop p2e4n_={p2e4n_}')

            while lb_rt >= _get_floor_log2_possible_next_prime_factor4n_() and (may_p2e4gcd4e5n is None or _k in p2e4gcd4e5n):
                # [lb_rt >= 1]
                # [_n >= 2]
                # [n0 == (II__p2e_(p2e4n_)*_n)**k_]
                (may_n, _p2e4n, may_rt) = _detect_pefect_kth_root_(_k, _n)
                '...+O((lbN*lb_max_p)*num_ps4n)' #global-total _get_mod_
                '...+O((lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n +((lbN/k*lb_max_p)*(num_ps4n-num_ps4rt<k>)) +(lb_max_p**2 *num_ps4rt<k>**3))'
                    #per-call: _detect_pefect_kth_root_
                ###################
                # global-total _get_mod_ ~O(lbN**2)
                # total loop except _get_mod_ ~O(lbN**3/lblbN)
                #   <<==:
                ###################
                # total loop except _get_mod_ ~O(sum (lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n +((lbN/k*lb_max_p)*(num_ps4n-num_ps4rt<k>)) +(lb_max_p**2 *num_ps4rt<k>**3) {prime k :<- [3..=max_k]})
                # ~O(sum {<= ?})
                # ??? [num_ps4rt<k> == O(lbN/k)] #lb_max_p???
                # [sum log2(i) {i :<- [2..=num_ps4rt<k>]} <= lbN/k]
                # [sum i*2**i {i :<- [1..=log2 num_ps4rt<k>]} <= (lbN/k)]
                # [D<x>(x*e**x -e**x) == x*e**x]
                # [log2(num_ps4rt<k>)*num_ps4rt<k> <= (lbN/k)]
                # [num_ps4rt<k> == O((lbN/k) /log2(lbN/k)) == O(lbN/k/lblbN)]
                # [num_ps4rt<k> == O(lbN/k/lblbN)]
                # [zzz := O(lbN/k/lblbN)]
                # ~O(sum (lb_max_k*lb_max_p +lb_max_p**3)*num_ps4n +((lbN/k*lb_max_p)*(num_ps4n-zzz)) +(lb_max_p**2 *zzz**3) {prime k :<- [3..=max_k]})
                # ~O(sum (lb_max_k +lb_max_p**2 +lbN/k)*lb_max_p*num_ps4n +(lb_max_p**2 *(lbN/k/lblbN)**3) {prime k :<- [3..=max_k]})
                # [total k == O(max_k/lb_max_k)]
                # ~O((max_k +lb_max_p**2 *max_k/lb_max_k +lbN*lb_max_k)*lb_max_p*num_ps4n +(lb_max_p**2 *(lbN/lblbN)**3))
                # [lb_max_p == lbN/max_k]  #assume trial_division until max_p, i.e. [next_prime_factor4n > max_p]
                # [max_k == lbN/lb_max_p]
                # [lb_max_k == O(lblbN -lblb_max_p) == O(lblbN)]
                # [total k == O(max_k/lb_max_k) == O(lbN/lb_max_p/lblbN)]
                # ~O((lbN/lb_max_p +lb_max_p**2 *lbN/lb_max_p/lblbN +lbN*lblbN)*lb_max_p*num_ps4n +(lb_max_p**2 *(lbN/lblbN)**3))
                # !! [num_ps4rt<k> == O(lbN/k/lblbN)]
                # [num_ps4n == num_ps4rt<1> == O(lbN/lblbN)]
                # ~O((lbN/lb_max_p +lb_max_p**2 *lbN/lb_max_p/lblbN +lbN*lblbN)*lb_max_p*lbN/lblbN +(lb_max_p**2 *(lbN/lblbN)**3))
                # ~O((lb_max_p +lblbN**2)*lb_max_p*lbN**2/lblbN**2 +(lb_max_p**2 *(lbN/lblbN)**3))
                # !! [num_ps4n == O(lbN/lblbN)]
                # [max_p == O(num_ps4n*log2(num_ps4n)) == O(lbN/lblbN*log2(lbN/lblbN)) == O(lbN)]
                # [max_p == O(lbN)]
                # [lb_max_p == O(lblbN)]
                # [total k == O(lbN/lb_max_p/lblbN) == O(lbN/lblbN**2)]
                # ~O((lblbN +lblbN**2)*lblbN*lbN**2/lblbN**2 +(lblbN**2 *(lbN/lblbN)**3))
                # ~O(lbN**2*lblbN +lbN**3/lblbN)
                # ~O(lbN**2/lblbN*(lblbN**2 +lbN))
                # [log2(16)**2 == 16]
                # ~O(lbN**3/lblbN)
                ###################
                ###################
                #
                # global-total _get_mod_ ~O((lbN*lb_max_p)*num_ps4n)
                # !! [num_ps4n == O(lbN/lblbN)]
                # !! [lb_max_p == O(lblbN)]
                # ~O((lbN*lblbN)*(lbN/lblbN))
                # ~O(lbN**2)
                ###################
                # [may_rt is None]or[_rt >= 2]
                if not may_n is None:
                    assert may_n < _n
                    # [_n == II__p2e_(_p2e4n)*may_n]
                    if verbose:print(f'main():loop _k={_k}: _n:{_n}///II(_p2e4n)-->{may_n}')
                    _n = may_n
                    # [_n >= 1]
                    #if _n == 1: break
                    # [n0 == (II__p2e_(p2e4n_)*II__p2e_(_p2e4n)*_n)**k_]
                    may_p2e4gcd4e5n = p2e4gcd4e5n = _update_p2e4gcd4e5n_(may_p2e4gcd4e5n, _p2e4n)
                    iter_sorted_keys_of_p2e4gcd4e5n = iter(sorted(p2e4gcd4e5n))
                    _iadd_p2e4n_(p2e4n_, _p2e4n)
                    _p2e4n = None
                    # [n0 == (II__p2e_(p2e4n_)*_n)**k_]
                    if verbose:print(f'main():loop _k={_k}: _n:{_n}')
                    if verbose:print(f'main():loop k_={k_}')
                    if verbose:print(f'main():loop may_p2e4gcd4e5n={may_p2e4gcd4e5n}')
                    if verbose:print(f'main():loop p2e4n_={p2e4n_}')
                    lb_rt = floor_log2_kth_root_(_k, _n)
                    # [lb_rt >= 0]
                # [n0 == (II__p2e_(p2e4n_)*_n)**k_]
                # [lb_rt >= 0]
                if may_rt is None:
                    # [may_rt is None]
                    # [lb_rt >= 0]
                    break
                else:
                    # [_rt**_k == _n]
                    # [_rt >= 2]
                    _rt = may_rt
                # [_rt**_k == _n]
                # [_rt >= 2]
                _rt
                # !! [n0 == (II__p2e_(p2e4n_)*_n)**k_]
                # [n0 == (II__p2e_(p2e4n_)*_rt**_k)**k_]
                k_ *= _k
                p2e4n_ = _perfect_kth_root__p2e_(p2e4n_, _k)
                # [n0 == (II__p2e_(p2e4n_)*_rt)**k_]
                if not may_p2e4gcd4e5n is None:
                    p2e4gcd4e5n[_k] -= 1
                    if p2e4gcd4e5n[_k] == 0:
                        del p2e4gcd4e5n[_k]
                ######next round:
                _n = _rt
                # !! [n0 == (II__p2e_(p2e4n_)*_rt)**k_]
                # [n0 == (II__p2e_(p2e4n_)*_n)**k_]
                # !! [_rt >= 2]
                # [_n >= 2]
                lb_rt = floor_log2_kth_root_(_k, _n)
                # [lb_rt >= 0]
            else:
                # [[lb_rt < _get_floor_log2_possible_next_prime_factor4n_()] or not _k in may_p2e4gcd4e5n]
                pass
            lb_next_p = _get_floor_log2_possible_next_prime_factor4n_()
            if not lb_rt >= lb_next_p:
                break
        # [n0 == (II__p2e_(p2e4n_)*_n)**k_]
        # [_n >= 1]
        if 0:
            if n == 9:
                print((k_, p2e4n_, may_p2e4gcd4e5n, _n))
        if _n == 1:
            # !! [n0 >= 4]
            # [perfect kth root include all prime factors of n0:n0**(1/k) >= 2]
            # now be 1, all prime factors must be found and put into p2e4n_
            # [not$ may_p2e4gcd4e5n is None]
            if may_p2e4gcd4e5n is None:
                raise 000
            assert _update_p2e4gcd4e5n_(None, p2e4n_) == p2e4gcd4e5n
            if p2e4gcd4e5n:
                gcd4e5n = II__p2e_(p2e4gcd4e5n)
                k_ *= gcd4e5n
                p2e4n_ = _perfect_kth_root__p2e_(p2e4n_, gcd4e5n)
                p2e4gcd4e5n.clear()
                gcd4e5n = 1
        if 0:
            #bug:n0=257*3**23:
            assert not may_p2e4gcd4e5n, (k_, p2e4n_, may_p2e4gcd4e5n, _n)
                #AssertionError: (1, {3: 23}, {23: 1}, 257)
        assert (p2e4n_ and may_p2e4gcd4e5n is not None and not p2e4gcd4e5n) or (not floor_log2_kth_root_(_k, _n) >= _get_floor_log2_possible_next_prime_factor4n_())
        if k_ == 1:
            rt = n
            k = 1
        else:
            rt = II__p2e_(p2e4n_)*_n
            k = k_
        #assert rt**k == n
        return (rt, k)
    #end-def main():
    def _update_p2e4gcd4e5n_(may_p2e4gcd4e5n, _p2e4n, /):
        if may_p2e4gcd4e5n is None:
            if not _p2e4n:
                raise 000
            gcd4e5n = gcd_many(_p2e4n.values())
            p2e4gcd4e5n = _factor_small_pint_(gcd4e5n)
        else:
            p2e4gcd4e5n = may_p2e4gcd4e5n
            new = p2e4gcd4e5n
            for _, e in _p2e4n.items():
                (p2e4gcd, _) = semi_factor_pint_via_trial_division(new.keys(), e)
                new = {p:min(e, new[p]) for p, e in p2e4gcd.items()}
            p2e4gcd4e5n = new
        return p2e4gcd4e5n

    def _iadd_p2e4n_(p2e4n_, _p2e4n, /):
        for p, e in _p2e4n.items():
            p2e4n_.setdefault(p, 0)
            p2e4n_[p] += e

    def mainmain():
        rt, k = main()
        assert rt**k == n
        return (rt, k)
    return mainmain()

def _factor_small_pint_(n, /):
    (p2e4n, unfactored_part, may_next_prime_factor) = factor_pint_by_trial_division_ex_(n, may_upperbound4prime_factor=n+1)
    if not unfactored_part == 1:raise 000
    return p2e4n

def _perfect_kth_root__p2e_(p2e, k, /):
    d = {}
    for p, e in p2e.items():
        q, r = divmod(e, k)
        if r: raise 000
        d[p] = q
    return d









def __():
    #too slow, discard
    #begin-detect_pefect_kth_root_
    #_2357 = (2,3,5,7)
    _3_5_7 = (3,5,7)
    _II_3_5_7 = II(_3_5_7)

    #_2_3_5 = (2,3,5)
    _2_5_17 = (2,5,17)
    r'''[[[
    3, 5, 17 is Fermat_prime
        p-1 is 2**e
        [gcd(phi(p**2), odd_q) == gcd(p, odd_q) == p if [p==odd_q] else 1]
        [[not$ is_square_residual_mod_prime_(p;xx)] <-> [is_primitive_root_mod_(p;xx)]]
        [2**e =[%p]= -1]
        [order_mod_(p;2) == e+1]
    [is_least_primitive_root_mod_(17;3)]
    [not$ is_square_residual_mod_prime_(17;3)]
        easy to find
    >>> pow(2,4,17)
    16
    >>> pow(3,8,17)
    16

    why use 17 but not use 3?
    [ceil_log_(17; n**(1/k)) <= ceil_log_(16; n**(1/k)) == ceil_log2_kth_root_(4*k;n)]

    xxx [ceil_log_(3; n**(1/k)) <= ceil_log_(2; n**(1/k)) == ceil_log2_kth_root_(k;n)]
    [ceil_log_(3; n**(1/k)) == ceil_log_(9; n**(2/k)) <= ceil_log_(8; n**(2/k)) == ceil_log2_kth_root_(3*k;n**2) == ceil_div(ceil_log2(n**2), 3*k) <= ceil_div(2*ceil_log2(n), 3*k)]
    cf_log2_(3) = [1;1,1,2,2,3,1,5,2,23,2,2,1,1,...]
        view ../../python3_src/nn_ns/math_nn/numbers/A028507-continued_fraction_expansion_for_log_2_3__fst_10000.txt
    1,2/1,3/2,
    from seed.math.continued_fraction.continued_fraction_fold import *
    f,g = iter_continued_fraction_digits5ND_, iter_approximate_fractions5continued_fraction_
    g = iter_approximate_fraction_NDs5continued_fraction_
    for N,D in g([1,1,1,2,2,3,1,5,2,23,2,2,1,1]):print(f'{N}/{D}')
    1/1
    2/1
    3/2
    8/5
    19/12
    65/41
    84/53
    485/306
    1054/665
    24727/15601
    50508/31867
    125743/79335
    176251/111202
    301994/190537
    >>> 3**5
    243
    >>> 2**8
    256
    >>> 2**19
    524288
    >>> 3**12
    531441

    #]]]'''#'''
    def detect_pefect_kth_root_(k, n, /, *, verbose):
        r'''[[[
        'k/int{>=1} -> n/int{>=2} -> may base/int{>=2}{n==base**k}'

        O(lbN**3 *(k///odd4k)/k**3 +lbN**2)
            too slow!!!
            worse than floor_kth_root_
                O(lbN**2 *lblbN)
        ######################
        '...+O(e2*(log2(n)/2**e2)**3 + log2(n)**2)'
        '...+O(log2(n)**3 /k**3 +log2(n)**2)'
        '...+O(log2(n)**2 /k**2)'
        ######################
        O(log2(n)**3 *(k///odd4k)/k**3 +log2(n)**2)
        #]]]'''#'''
        check_type_is(int, k)
        if not k > 0:raise ValueError(k)
        check_type_is(int, n)
        if not n >= 0:raise ValueError(n)
        # [k >= 1]
        # [n >= 0]

        if n < 2:
            return n
        # [n >= 2]

        if k == 1:
            return n
        # [k >= 2]
        n0 = n
        n = None


        lb_rt = floor_log2_kth_root_(n)
        # [lb_rt >= 0]
        if lb_rt == 0:
            return None
        # [lb_rt >= 1]

        if 1:
            (p2e, _n) = semi_factor_pint_via_trial_division(_2_5_17, n0)
            # [n%2 == 1]
            # [n%17 =!= 0]
            # [n%5 =!= 0]
            #   2,5,17 are required below
            #   3,7 is unimportant
            if not all(e%k == 0 for e in p2e.values()):
                return None
            #rt_ = II(p**(e//k) for p,e in p2e.items())
            r'''[[[
        else:
            (e4n, odd4n) = factor_pint_out_2_powers(n0)
            _n = odd4n
            # [n%2 == 1]
            if not e4n%k == 0:
                return None
            rt_ = 1 << (e4n//k)
            #]]]'''#'''
        #rt_
        _n
        # [rt_**k * _n == n0]
        # [n%2 == 1]
        # [n%17 =!= 0]
        # [n%5 =!= 0]



        if 0:
            (p2e, unfactored_part, may_next_prime_factor) = factor_pint_by_trial_division_ex_(k, may_upperbound4prime_factor=k+1)
            if not unfactored_part == 1:raise 000
            #II__p2e_(p2e)
        else:
            (e4k, odd4k) = factor_pint_out_2_powers(k)
        # [e4k >= 0]
        # [odd4k >= 1]
        # [odd4k%2 == 1]




        # [n >= 2]
        # [n%2 == 1]
        if e4k:
            # [e4k =!= 0]
            # !! [e4k >= 0]
            # [e4k >= 1]
            e2 = e4k
            # [e2 >= 1]
            # !! [n >= 2]
            # !! [n%2 == 1]
            m = _detect_pefect_kth_root__k_eq_2_power_(e2, _n, verbose=verbose)
            '...+O(e2*(log2(n)/2**e2)**3 + log2(n)**2)'
            if m is None:
                return None
            _n = m
            # [n >= 2]
            # [n%2 == 1]
        # [n >= 2]
        # [n%2 == 1]


        # [odd4k >= 1]
        if not odd4k == 1:
            # [odd4k >= 2]
            # !! [odd4k%2 == 1]
            # !! [n >= 2]
            # !! [n%17 =!= 0]
            # !! [n%5 =!= 0]

            m = _detect_pefect_kth_root__k_is_odd_(odd4k, _n, verbose=verbose)
            '...+O(log2(n)**3 /k**3  +log2(n)**2)'
            if m is None:
                return None
            _n = m
        _rt = _n

        '...+O(log2(n)**2 /k**2)'
        rt_ = II(p**(e//k) for p,e in p2e.items())
        rt = rt_ * _rt
        assert rt**k == n
        return rt
    def _detect_pefect_kth_root__k_is_odd_(k, n, /, *, verbose):
        'O(log2(n)**3 /k**3  +log2(n)**2)'
        assert k >= 2
        assert k&1 == 1
        assert n >= 2
        assert n %17
        assert n %5
        # [k >= 2]
        # [k%2 == 1]
        # [n >= 2]
        # [n%17 =!= 0]
        # [n%5 =!= 0]


        # !! [k%2 == 1]
        # [?p. [p is odd prime][gcd(p-1,k)==1]]
        # [?p. [p is odd prime][gcd((p-1)*p,k)==1]]
        # [?p. [p is odd prime][gcd(phi(p**j),k)==1]]

        e17, _17coprime = factor_pint_out_power_of_base_(17, k)
        # [_17coprime**e17 * _17coprime == k]
        # [e17 >= 0]
        # [_17coprime %17 =!= 0]

        # !! [k%2 == 1]
        # [_17coprime %2 =!= 0]
        # [gcd(_17coprime, 2*17) == 1]
        _17pows = 17**e17
        # [_17pows * _17coprime == k]
        # [gcd(_17pows, phi(5**2)) == 1]
        # [gcd(_17coprime, phi(17**2)) == 1]

        if 0:
            assert _17pows * _17coprime == k
            p = 17
            assert gcd((p-1)*p, _17coprime) == 1
            p = 5
            assert gcd((p-1)*p, _17pows) == 1

        _n = n
        k_p_e_pairs = [(_17pows, 5, 2), (_17coprime, 17, 4)]
        for _k, p, e in k_p_e_pairs:
            # !! [n%17 =!= 0]
            # !! [n%5 =!= 0]
            # !! [p <- [17,5]]
            # [n%p =!= 0]

            if _k == 1:
                continue
            # [_k >= 2]
            # [ceil_log_(5; n**(1/k)) <= ceil_log_(4; n**(1/k)) == ceil_log2_kth_root_(2*k;n)]
            # [ceil_log_(17; n**(1/k)) <= ceil_log_(16; n**(1/k)) == ceil_log2_kth_root_(4*k;n)]

            lb_rt = floor_log2_kth_root_(_k, _n)
            kk = ceil_log2_kth_root_(e*_k, _n)
            # [kk >= 1]
            if 1:
            #with _timer(prefix=f'kth_root_mod_({p}**{kk}, {_k}, {_n})', _show_hint_on_enter_=True, _to_show_=verbose):
                # !! [gcd(_17pows, phi(5**2)) == 1]
                # !! [gcd(_17coprime, phi(17**2)) == 1]
                # !! [p <- [17,5]]
                # !! [k <- [_17coprime,_17pows]]
                # [gcd(_k, phi(p**2)) == 1]
                # [_rt**_k == _n]
                # [_rt**_k =[%p**kk]= _n]
                # [_rt**(_k%((p-1)*p**(kk-1))) =[%p**kk]= _n]
                # [_rt =[%p**kk]= _n**inv_mod_(((p-1)*p**(kk-1));_k)]
                p_kkmm = p**(kk-1)
                phi_p_kk = (p-1)*p_kkmm
                p_kk = p_kkmm*p

                _inv_k = inv_mod_power__coprime_(phi_p_kk, _k)
                _rt = pow(_n, _inv_k, p_kk)
                    # ???is this fast???
                    # cmp: n**(1/k) vs _n**_inv_k%p**kk
                    # [O(EVAL(_n**_inv_k%p**kk)) == O(log2(p**kk)**3) == O(log2(_n**(1/_k))**3) == O(log2(_n)**3 /_k**3)]
                '...+O(log2(n)**3 /k**3)'
                if not floor_log2(_rt) == lb_rt:
                    return None
            #next round:
            _n = _rt
        _rt = _n
        n, k


        # [O(EVAL(_rt**k)) == O(sum (2**i *log2(_rt))**2 {i :<- [1..=log2(k)]}) == O(k**2 *log2(_rt)**2) == O(k**2 *log2(n**(1/k))**2) == log2(n)**2]
        '...+O(log2(n)**2)'
        if not _rt**k == n:
            # [_rt =!= rt]
            return None
        rt = _rt
        # [rt**k == n]
        # !! [n >= 2]
        # [rt >= 2]
        return rt
    def _detect_pefect_kth_root__k_eq_2_power_(e2, n, /, *, verbose):
        'O(e2*(log2(n)/2**e2)**3 + log2(n)**2)'
        assert e2 >= 1
        assert n >= 2
        assert n&1 == 1
        # [n%2 == 1]
        if n < 9:
            # !! [n%2 == 1]
            # !! [2 <= n < 9]
            # [n <- {3,5,7}]
            # [k == 2**e2 >= 2]
            # !! [rt**2 == n][rt %1 ==0]
            # [rt <- {}]
            #
            #xxx if (e2,n) == (1,4): return 2
            return None
        # [n >= 9]
        n__357 = n%_II_3_5_7
        for p in _3_5_7:
            if not is_square_residual_mod_prime_(p, n__357):
                return None

        lb_n = floor_log2(n)
        k = 1<<e2
        lb_rt = lb_n//k
        if lb_rt == 0:
            return None
        assert lb_rt >= 1
        # [lb_rt >= 1]

        p = 2
        kk = lb_rt+2
        # !! [lb_rt >= 1]
        # [kk >= 3]
        # [is_square_residual_mod_prime_power_(p, kk, xx) === [xx%8 == 1]]
        #
        if 1:
        #with _timer(prefix=f'sqrts_mod_(2**{kk};{n})', _show_hint_on_enter_=True, _to_show_=verbose):
            # !! [n%2 == 1]
            p_kk = 1<<kk
            _n__p_kk = n&(p_kk-1)
            ls = [_n__p_kk]
            for _ in range(e2):
                #if not ls: return None
                [_n__p_kk] = ls
                [_rt, neg_rt] = [*iter_sqrts_mod_prime_power_(p, kk, _n__p_kk)]
                # !! [_n %2 == 1]
                # [num_sqrts == O(1)]
                # !! [p == 2]
                # [neednot search sqrt%2]
                # !! iter_sqrts_mod_prime_power_ ~ O((k**3 + log2(p) + log2(p///odd4p)**(3/2))*log2(p)**2 +find_arbitrary_one_square_nonresidual_mod_odd_prime_ + num_sqrts)
                # ~O(kk**3)
                # ~O((log2(n)/2**e2)**3)
                '...+O((log2(n)/2**e2)**3)'
                assert floor_log2(neg_rt) == kk-1
                # [floor_log2(neg_rt) == kk-1 == lb_rt+1]
                # !! [is_square_residual_mod_prime_power_(p, kk, xx) === [xx%8 == 1]]
                ls = [x for x in [_rt, neg_rt] if (_rt&7) == 1]
                if not len(ls) == 1: raise 000
            #end-for _ in range(e2):
            '...+O(e2*(log2(n)/2**e2)**3)'
                #total4loop

            # !! [floor_log2(neg_rt) == kk-1 == lb_rt+1]
            # [neg_rt =!= rt]
            if not floor_log2(_rt) == lb_rt:
                # [_rt =!= rt]
                return None

            # [O(EVAL(_rt**k)) == O(sum (2**i *log2(_rt))**2 {i :<- [1..=log2(k)]}) == O(k**2 *log2(_rt)**2) == O(k**2 *log2(n**(1/k))**2) == log2(n)**2]
            '...+O(log2(n)**2)'
            if not _rt**k == n:
                # [_rt =!= rt]
                return None
            rt = _rt
        # [rt**2 == n]
        # !! [n >= 2]
        # [rt >= 2]
        return rt
    #end-detect_pefect_kth_root_

def __():
    # floor_kth_root_-ver
    from seed.for_libs.for_time import (
    Timer__print_err
        ,timer__print_err__thread_wide
        ,timer__print_err__process_wide
        ,timer__print_err__system_wide__highest_resolution
        ,timer__print_err__system_wide__monotonic
    )
    if 1:
        _timer = timer__print_err__thread_wide
        #with _timer(prefix=, _fmt_=, _show_hint_on_enter_=True, _to_show_=verbose):

    from math import sqrt as sqrt_, isqrt as isqrt_
    from seed.math.Jacobi_symbol import Jacobi_symbol
    from seed.math.prime_gens import prime_gen

    from seed.tiny import print_err
    from seed.tiny import check_type_is
    from seed.math.II import II, II_mod
    from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division


    from seed.math.gcd import gcd#, gcd_many, are_coprime
    from seed.math.floor_ceil import floor_sqrt, ceil_sqrt
    from seed.math.floor_ceil import floor_kth_root_, ceil_kth_root_
    from seed.math.floor_ceil import floor_log_, floor_log2



    def factor_pint_as_pefect_power_(n, /, *, verbose):
        'n/int{>=2} -> (base/int{>=2}, exp/int{>=1}){n==base**exp}'
        check_type_is(int, n)
        if not n > 1:raise ValueError(n)
        n0 = n
        L = n.bit_length()
        e = 1
        assert 1 < n < (1<<L)
        # [1 < n < (1<<L)]
        for p in prime_gen:
            # [1 < n < (1<<L)]
            if p >= L:
                # [2**p >= 2**L > n]
                break
            # [2**p < 2**L]
            while 1:
                # [1 < n < (1<<L)]
                may_kth_root = detect_pefect_kth_root_(p, n, verbose=verbose)
                if may_kth_root is None:
                    break
                kth_root = may_kth_root
                assert 1 < kth_root < n
                e *= p
                n = kth_root
                L = n.bit_length()
                assert 1 < n < (1<<L)
                # [1 < n < (1<<L)]
        base = n
        exp = e
        n = n0
        assert n == base**exp
        return (base, exp)


    def detect_pefect_kth_root_(k, n, /, *, verbose):
        'k/int{>=1} -> n/int{>=2} -> may base/int{>=2}{n==base**k}'
        check_type_is(int, n)
        if not n > 1:raise ValueError(k)
        check_type_is(int, k)
        if not k > 0:raise ValueError(n)
        if k == 1:
            _kth_root = n
        elif k == 2:
            # now: math.isqrt
            with _timer(prefix=f'floor_sqrt({n})', _show_hint_on_enter_=True, _to_show_=verbose):
                sqrt_ = floor_sqrt(n)
            _kth_root = sqrt_
        else:
            #if 1:
            with _timer(prefix=f'floor_kth_root_({k}, {n})', _show_hint_on_enter_=True, _to_show_=verbose):
                _kth_root = floor_kth_root_(k, n)
        if _kth_root**k == n:
            return _kth_root
        return None


if __name__ == "__main__":
    pass
__all__


from seed.math.factor_pint_as_pefect_power_ import factor_pint_as_pefect_power_
from seed.math.factor_pint_as_pefect_power_ import *
