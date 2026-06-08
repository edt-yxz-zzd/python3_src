#__all__:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/perfect_power/detect_perfect_power.py

seed.math.factor_pint.perfect_power.detect_perfect_power
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.perfect_power.detect_perfect_power -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.perfect_power.detect_perfect_power:__doc__ -ht # -ff -df
#######

[[
kwds4detect:using_floor_kth_root,vprime_list
kwds4CRT:vprime_list
kwds4pKrt:using_floor_kth_root,**kwds4CRT
kwds4pKrtEx:p2e4k, **kwds4pKrt
]]


'#'; __doc__ = r'#'
>>> from seed.math.factor_pint.perfect_power.lift_neg_kth_root_mod_coprime_power_ import sqrt_of_odd_mod_zpow_

>>> k = 2
>>> y = 465871**k
>>> sqrt_of_odd_mod_zpow_(y.bit_length()//2, y)
320561
>>> sqrt_of_odd_mod_zpow_(1+y.bit_length()//2, y)
58417
>>> sqrts_of_odd_mod_zpow_(y.bit_length()//2, y, validate=True)
(58417, 203727, 320561, 465871)
>>> sqrts_of_odd_mod_zpow_(1+y.bit_length()//2, y, validate=True)
(58417, 465871, 582705, 990159)
>>> sqrts_of_odd_mod_zpow_(2+y.bit_length()//2, y, validate=True)
(465871, 582705, 1514447, 1631281)
>>> sqrts_of_odd_mod_zpow_(3+y.bit_length()//2, y, validate=True)
(465871, 1631281, 2563023, 3728433)
>>> (1+y.bit_length()//2) -(5+y.bit_length())//2
-1
>>> (2+y.bit_length()//2) -(5+y.bit_length())//2
0
>>> (3+y.bit_length()//2) -(5+y.bit_length())//2
1



>>> may_perfect_sqrt_of_(y)
465871
>>> may_perfect_sqrt_of_(1+y)
>>> may_perfect_sqrt_of_(-1+y)


>>> is_perfect_square_(y)
True
>>> is_perfect_kth_power_(2, y)
True
>>> is_perfect_kth_power_(3, y)
False
>>> may_perfect_kth_root_of_(2, y)
465871
>>> may_perfect_kth_root_of_(12, 35**12)
35

>>> detect_perfect_power_(35**12)
(35, 12)
>>> detect_perfect_power_(35**12, arbitrary_exp_ok=True)
(1838265625, 2)
>>> detect_perfect_power_(2**9*35**12)
(12005000, 3)
>>> detect_perfect_power_(2*35**12)


>>> factor_pint_as_perfect_power_(9)
(3, 2)
>>> may_perfect_sqrt_of_(9)
3






[[
py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @_run_lt_ -using_floor_kth_root -validate ='1+2**16'
    total::duration: 19.682154564999998 *(unit: 0:00:01)
        #pre-trial_division__reduce_max_k

py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @_run_lt_ -using_floor_kth_root +validate ='1+2**16'
    total::duration: 19.536151727 *(unit: 0:00:01)
        #pre-trial_division__reduce_max_k

py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @factor_pint_as_perfect_power_ ='7**(1+2**8)'
    (7, 257)
    total::duration: 0.3831588399999999 *(unit: 0:00:01)

py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @factor_pint_as_perfect_power_ ='7**(1+2**16)'
    (7, 65537)
    total::duration: 37.093264041999994 *(unit: 0:00:01)
        #pre-trial_division__reduce_max_k
# [:trial_division__reduce_max_k]:goto
py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @factor_pint_as_perfect_power_ ='7**(1+2**16)'
    (7, 65537)
    total::duration: 0.3423573919999999 *(unit: 0:00:01)
        #post-trial_division__reduce_max_k

py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @_run_lt_ -using_floor_kth_root -validate ='1+2**16'
    total::duration: 3.30401724 *(unit: 0:00:01)
        #post-trial_division__reduce_max_k

py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @_run_lt_ -using_floor_kth_root +validate ='1+2**16'
    total::duration: 3.4169894010000004 *(unit: 0:00:01)
        #post-trial_division__reduce_max_k

py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @_run_lt_ +using_floor_kth_root -validate ='1+2**16'
    total::duration: 2.067181853 *(unit: 0:00:01)
py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @_run_lt_ +using_floor_kth_root +validate ='1+2**16'
    total::duration: 2.281000315 *(unit: 0:00:01)
CRT版更慢更花哨，大写的尴尬
    #此后CRT采用新算法@20260608，重新测时

===以下:更新:检测提取，构根靠后
py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @_run_lt_ -using_floor_kth_root -validate ='1+2**16'
    total::duration: 3.424905765 *(unit: 0:00:01)
py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @_run_lt_ -using_floor_kth_root +validate ='1+2**16'
    total::duration: 3.5588912550000003 *(unit: 0:00:01)
py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @_run_lt_ +using_floor_kth_root -validate ='1+2**16'
    total::duration: 2.416809166 *(unit: 0:00:01)
py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @_run_lt_ +using_floor_kth_root +validate ='1+2**16'
    total::duration: 2.660633857 *(unit: 0:00:01)


===
@20260608CRT采用新算法，重新测时
py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @_run_lt_ -using_floor_kth_root -validate ='1+2**16'
    total::duration: 2.906208317 *(unit: 0:00:01)
py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @_run_lt_ -using_floor_kth_root +validate ='1+2**16'
    total::duration: 3.170212776 *(unit: 0:00:01)
py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @_run_lt_ +using_floor_kth_root -validate ='1+2**16'
    total::duration: 2.7720433879999997 *(unit: 0:00:01)
py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   @_run_lt_ +using_floor_kth_root +validate ='1+2**16'
    total::duration: 2.86120063 *(unit: 0:00:01)
]]
[[
py_adhoc_call  { +to_show_total_timedelta }  seed.math.factor_pint.perfect_power.detect_perfect_power   ,_asc_us2iter_dqr_triples_ ='-1+2**3456' ='range(2, 2**16, 3)' +validate | more
]]



from seed.math.factor_pint.perfect_power.detect_perfect_power import *
]]]'''#'''
__all__ = r'''
detect_perfect_power_
    is_perfect_power_
    factor_pint_as_perfect_power_



is_cube_        is_perfect_cube_
    may_perfect_cbrt_of_    may_perfect_cbrt_
is_square_      is_perfect_square_
    may_perfect_sqrt_of_    may_perfect_sqrt_
        may_perfect_sqrt_of__via_CRT_
        may_perfect_sqrt_of__via_floor_kth_root_

is_kth_power_   is_perfect_kth_power_
    may_perfect_kth_root_of_    may_perfect_kth_root_
        may_perfect_kth_root_of__factorization4k_
            may_perfect_kth_root_of__factorization4k__via_CRT_
            may_perfect_kth_root_of__via_floor_kth_root_
                may_perfect_kth_root_of__k_is_prime_
                    may_perfect_kth_root_of__k_is_prime__via_CRT_
                        may_perfect_kth_root_of__k_is_odd_prime__via_CRT_




'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from itertools import chain, repeat, islice# takewhile
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.math.prime_sieve.sieve_ge_le import iter_primes_, iter_sieve4primes_ge_
    from seed.math.Jacobi_symbol import Jacobi_symbol
    #from seed.math.Chinese_Remainder_Theorem import apply_CRT__pairs
        #def apply_CRT__pairs(u_r_pairs, /, *, extended:bool):
    from seed.math.Chinese_Remainder_Theorem__ver2 import apply_CRT__pairs
        # @20260608
    from seed.math.factor_pint.factor_pint__naive_brute_force import iter_factor_pint__naive_brute_force_
    from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
    from seed.math.factor_pint.perfect_power.lift_neg_kth_root_mod_coprime_power_ import sqrts_of_odd_mod_zpow_, kth_root_of_odd_mod_zpow__k_is_odd_
    from seed.debug.print_err import print_err
    from seed.math.floor_ceil_tools.fc_kth_root import floor_sqrt, floor_kth_root_
    from seed.math.floor_ceil_tools.fc_log import floor_log2, ceil_log2
from seed.math.prime_sieve.PrimeList import PrimeList, ModOverPrimeList #, DivmodOverPrimeList
#.#################################
___end_mark_of_excluded_global_names__0___ = ...



#.#################################
#using_floor_kth_root
_default4using_floor_kth_root = False
#@20260608:found CRT.precomputation slow
_default4using_floor_kth_root = True
#.#################################



def _asc_us2iter_dqr_triples_(n, ds, /, *, validate=False):
    'n -> sorted-Iter d -> Iter (d, q, r) # [n == d*q+r]'
    ds = iter(ds)
    for d in ds:
        (q, r) = divmod(n, d)
        yield (d, q, r)
        break
    for _d in ds:
        # [n == d*q+r]
        dd = _d -d
        #dq = _q -q
        #dr = _r -r
        # [n == _d*_q+_r]
        # [n == (d+dd)*(q+dq)+(r+dr)]
        # [n == (d+dd)*q +(d+dd)*dq +(r+dr)]
        # !! [n == d*q+r]
        # [0 == dd*q +_d*dq +dr]
        # [-dd*q == _d*dq +dr]
        # [dr <= _r < _d]
        # [dr >= -r > -d > -_d]
        dq, dr = divmod(-dd*q, _d)
        # [0 <= r < d < _d]
        # [-_d < r+dr < 2*_d]
        _r = r+dr
        # [-_d < _r < 2*_d]
        if _r < 0:
            # [-_d < _r < 0]
            _r += _d
            777; dq -= 1
            # [0 < _r < _d]
        elif _r >= _d:
            # [_d <= _r < 2*_d]
            _r -= _d
            777; dq += 1
            # [0 <= _r < _d]
        else:
            # [0 <= _r < _d]
            pass
        # [0 <= _r < _d]
        _q = q+dq
        # [n == _d*_q+_r]
        (d, q, r) = (_d, _q, _r)
        # [n == d*q+r]
        yield (d, q, r)
        if validate:
            assert n == d*q+r

def is_perfect_power_(m, /, **kwds4detect):
    'm/uint{>1} -> bool/{==[?[rt,exp::uint{>1}] -> [rt**exp==m]]}'
    return not None is detect_perfect_power_(m, arbitrary_exp_ok=True, **kwds4detect)
def factor_pint_as_perfect_power_(m, /, **kwds4detect):
    'm/uint{>1} -> (rt/uint{>1}, exp/uint{>=1}) # [rt**exp==m]'
    x = detect_perfect_power_(m, arbitrary_exp_ok=False, **kwds4detect)
    if x is None:
        x = (m, 1)
    x
    #if 0b00001:print_err('factor_pint_as_perfect_power_', m, x, )
    return x
def _1_detect_perfect_power_(using_floor_kth_root, arbitrary_exp_ok, vprime_list, m, q, eq, odd, /):
    '[m == q**eq *odd][eq >= 1]'
    assert eq > 0
    if eq == 1:
        return None
    # [eq >= 2]
    if odd == 1:
        # [eq >= 2]
        return (q, eq)
    pes = iter_factor_pint__naive_brute_force_(eq)
    e4odd = floor_log2(odd)
    return _2_detect_perfect_power_(using_floor_kth_root, arbitrary_exp_ok, vprime_list, m, q, eq, odd, e4odd, pes)

def detect_perfect_power_(m, /, *, arbitrary_exp_ok=False, vprime_list=None, using_floor_kth_root=_default4using_floor_kth_root):
    #, **kwds4detect:vprime_list,using_floor_kth_root
    'm/uint{>1} -> may (rt/uint{>1}, exp/uint{>1}) # [rt**exp==m] # kw:arbitrary_exp_ok affect whether "exp" should be maximal'
    check_int_ge(2, m)
    # [m >= 2]
    (ez, odd) = factor_pint_out_power_of_base_(2, m)
    # [odd%2 == 1]
    if ez:
        # [m == 2**ez*odd]
        return _1_detect_perfect_power_(using_floor_kth_root, arbitrary_exp_ok, vprime_list, m, 2, ez, odd)
    # [ez == 0]
    # [odd == m >= 2]
    # [odd%2 == 1]
    # [odd == m >= 3]
    # [odd >= 3]

    e4odd = floor_log2(odd)
    # !! [odd >= 3]
    # [e4odd >= 1]
    e4e4odd = floor_log2(e4odd)
    #max1_p = e4odd
    #max1_p = e4odd*(1+e4e4odd)
    max1_p = e4odd+e4e4odd
    dr_ls = vprime_list = _5vprime_list(odd, vprime_list, strict=False, max1_6init=0)
    #(p2e, odd) = semi_factor_pint_via_trial_division(prime_list[:e4odd], odd)
    it = iter(dr_ls)
    for p, r4odd in islice(it, 0, max1_p):
        # [p::prime]
        # [r4odd == odd%p]
        if r4odd == 0:
            (ep, _odd) = factor_pint_out_power_of_base_(p, odd)
            # [m == odd == p**ep*_odd]
            dr_ls = vprime_list = _5vprime_list(_odd, vprime_list:=dr_ls, strict=False, max1_6init=0)
            return _1_detect_perfect_power_(using_floor_kth_root, arbitrary_exp_ok, vprime_list:=dr_ls, m, p, ep, _odd)
    # [odd == m >= 3]
    next_p, _ = next(it)
    # [@[q::prime][q < next_p] -> [odd%q =!= 0]]
    if odd < next_p**2:
        # !! [odd >= 3]
        # [is_prime_(odd)]
        # !! [odd == m]
        # [is_prime_(m)]
        return None
    # [exp <= log_(next_p;m) == log2(m)/log2(next_p) < m.bit_length()/floor_log2(next_p) == (1+floor_log2(odd))/floor_log2(next_p)]
    # [exp < (1+floor_log2(odd))/floor_log2(next_p)]
    # [exp <= (1+floor_log2(odd))//floor_log2(next_p)]
    max_exp = (1+e4odd)//floor_log2(next_p)
        # (next_p, max_exp) => [m == next_p**max_exp]
        # trial_division => reduce max_k=max_exp from e4odd
        # [:trial_division__reduce_max_k]:here

    #pes = zip(iter_primes_(), repeat(e4odd))
    pes = zip(dr_ls.the_prime_list.iter__lt_(1+max_exp), repeat(max_exp.bit_length()))
    pes
    # !! [ez == 0]
    return _2_detect_perfect_power_(using_floor_kth_root, arbitrary_exp_ok, vprime_list:=dr_ls, m, q:=2, eq:=0, odd, e4odd, pes)

def _5vprime_list(m, vprime_list, /, *, strict, max1_6init):
    match vprime_list:
        case ModOverPrimeList(the_numerator=_m, the_prime_list=prime_list) as dr_ls:
            dr_ls
            if not _m == m:
                if strict:raise ValueError(_m, m)
                dr_ls = ModOverPrimeList(m, prime_list)
            dr_ls
        case PrimeList() as prime_list:
            dr_ls = ModOverPrimeList(m, prime_list)
        case None:
            prime_list = PrimeList(max1_6init)
            dr_ls = ModOverPrimeList(m, prime_list)
        #case
    return dr_ls
def _2_detect_perfect_power_(using_floor_kth_root, arbitrary_exp_ok, vprime_list, m, q, eq, odd, e4odd, pes, /):
    '[m == q**eq *odd][eq >= 0]'
    dr_ls = vprime_list = _5vprime_list(odd, vprime_list, strict=False, max1_6init=0)

    exp = 1
    # [m == q**eq*odd**exp]
    for p, max_ep in pes:
        #if p > e4odd:raise 000
        # !! [m == q**eq*odd**exp]
        # => odd decreasing
        # => MAYBE:[p > e4odd]
        if p > e4odd:break
        for _ in range(max_ep):
            x = may_perfect_kth_root_of__k_is_prime_(p, odd, vprime_list=dr_ls, using_floor_kth_root=using_floor_kth_root)
            if x is None: break
            rt = x
            # [odd == rt**p]
            if arbitrary_exp_ok:
                if q == 2:
                    return (rt<<(eq//p), p)
                return (rt*q**(eq//p), p)
            # !! [m == q**eq*odd**exp]
            # !! [odd == rt**p]
            # [m == q**eq*rt**(p*exp)]
            exp *= p
            777;odd = rt
            777;e4odd = floor_log2(odd)
            # [m == q**eq*odd**exp]
            dr_ls = vprime_list = _5vprime_list(odd, vprime_list:=dr_ls, strict=False, max1_6init=0)
    # [m == q**eq*odd**exp]
    if exp > 1:
        if q == 2:
            return (odd<<(eq//exp), exp)
        return (odd*q**(eq//exp), exp)
    return None
def may_perfect_kth_root_of__k_is_prime_(k, m, /, *, using_floor_kth_root=_default4using_floor_kth_root, **kwds4CRT):
    'k/prime -> m/uint -> may n/uint # [n**k == m]'
    if using_floor_kth_root:
        return may_perfect_kth_root_of__via_floor_kth_root_(k, m)
    return may_perfect_kth_root_of__k_is_prime__via_CRT_(k, m, **kwds4CRT)
def may_perfect_kth_root_of__via_floor_kth_root_(k, m, /):
    check_int_ge(1, k)
    check_int_ge(0, m)
    if k == 1 or m <= 1:
        return m
    # [k >= 2]
    # [m >= 2]
    rt = floor_kth_root_(k, m)
    if rt**k == m:
        return rt
    return None
def may_perfect_kth_root_of_(k, m, /, *, p2e4k=None, **kwds4pKrt):
    #, **kwds4pKrtEx:p2e4k, **kwds4pKrt
    'k/uint -> m/uint -> may n/uint # [n**k == m]'
    return may_perfect_kth_root_of__factorization4k_(k, p2e4k, m, **kwds4pKrt)
may_perfect_kth_root_ = may_perfect_kth_root_of_
def may_perfect_cbrt_of_(m, /, **kwds4pKrt):
    'm/uint -> may n/uint # [n**3 == m]'
    return may_perfect_kth_root_of__k_is_prime_(3, m, **kwds4pKrt)
may_perfect_cbrt_ = may_perfect_cbrt_of_
def may_perfect_kth_root_of__factorization4k_(k, may_p2e4k, m, /, *, using_floor_kth_root=_default4using_floor_kth_root, **kwds4CRT):
    #, **kwds4pKrt:using_floor_kth_root, **kwds4CRT
    'k/uint -> may factorization{k}/p2e4k/{prime:exp{>=1}} -> m/uint -> may n/uint # [n**k == m]'
    if using_floor_kth_root:
        return may_perfect_kth_root_of__via_floor_kth_root_(k, m)
    return may_perfect_kth_root_of__factorization4k__via_CRT_(k, may_p2e4k, m, **kwds4CRT)
def may_perfect_kth_root_of__factorization4k__via_CRT_(k, may_p2e4k, m, /, *, vprime_list=None):
    check_int_ge(1, k)
    check_int_ge(0, m)
    if k == 1 or m <= 1:
        return m
    using_floor_kth_root = False
    # [k >= 2]
    # [m >= 2]
    # [m**/k > 1]
    e4m = floor_log2(m)
    # [2**e4m <= m < 2**(e4m+1)]
    if e4m < k:
        # [2**e4m <= m < 2**(e4m+1) <= 2**k]
        # [m**/k < 2]
        # !! [m**/k > 1]
        # [1 < m**/k < 2]
        return None
    rt = m
    if may_p2e4k is None:
        pes = iter_factor_pint__naive_brute_force_(k)
    else:
        p2e4k = may_p2e4k
        pes = sorted(p2e4k.items())
    pes

    vprime_list
    kwds4pKrt = dict(vprime_list=vprime_list, using_floor_kth_root=using_floor_kth_root)
    for p, ep in pes:
        for _ in range(ep):
            x = may_perfect_kth_root_of__k_is_prime_(p, rt, **kwds4pKrt)
            if x is None:
                return None
            rt = x
    rt
    return rt
def is_perfect_kth_power_(k, m, /, **kwds4pKrtEx):
    return not None is may_perfect_kth_root_of_(k, m, **kwds4pKrtEx)
is_kth_power_ = is_perfect_kth_power_

def is_perfect_square_(m, /, **kwds4pKrt):
    return not None is may_perfect_sqrt_of_(m, **kwds4pKrt)
is_square_ = is_perfect_square_
def is_perfect_cube_(m, /, **kwds4pKrt):
    return not None is may_perfect_kth_root_of__k_is_prime_(3, m, **kwds4pKrt)
is_cube_ = is_perfect_cube_

def may_perfect_sqrt_of__via_floor_kth_root_(m, /):
    check_int_ge(0, m)
    rt = floor_sqrt(m)
    if rt**2 == m:
        return rt
    return None
def may_perfect_sqrt_of_(m, /, *, using_floor_kth_root=_default4using_floor_kth_root, **kwds4CRT):
    'm/uint -> may n/uint # [n**2 == m]'
    if using_floor_kth_root:
        return may_perfect_sqrt_of__via_floor_kth_root_(m)
    return may_perfect_sqrt_of__via_CRT_(m, **kwds4CRT)
def may_perfect_sqrt_of__via_CRT_(m, /, *, vprime_list=None):
    using_floor_kth_root = False
    check_int_ge(0, m)
    # [m >= 0]
    if m <= 1:
        return m
    # [m >= 2]
    r8 = m&7
    if not r8 < 2:
        if m == 4:
            return 2
        return None
    # [m%8 <- {0,1}]
    if r8 == 0:
        # [m%8 == 0]
        (ez, odd) = factor_pint_out_power_of_base_(2, m)
        # [odd %2 == 1]
        if ez&1:
            return None
        # [ez%2 == 0]
        if not odd&7 == 1:
            return None
        # [odd %8 == 1]
    else:
        # [m%8 == 1]
        ez = 0
        odd = m
        # [odd %8 == 1]
    ez, odd
    # [ez%2 == 0]
    # [odd %8 == 1]
    # [odd >= 1]
    # [m == 2**ez*odd]


    ###########################
    # [m == 2**ez*odd]
    # [odd %8 == 1]
    # [odd >= 1]
    if odd < 25:
        match odd:
            case 1:
                rt = 1
            case 9:
                rt = 3
            case _:
                return None
        n = rt << (ez>>1)
        return n
    # [odd >= 25]
    ###########################


    e4odd = floor_log2(odd)
    e4e4odd = floor_log2(e4odd)
    dr_ls = vprime_list = _5vprime_list(odd, vprime_list, strict=False, max1_6init=0 and 2*e4odd*e4e4odd)

    pe_pairs = []
    #if ez: pe_pairs.append((2, ez))

    e4rt = e4odd//2
    tmp = 2+e4rt//e4e4odd
    _odd = odd
    for p, r4odd in dr_ls:
        # [p::prime]
        # [r4odd == odd%p]
        if p == 2:
            # !! Jacobi_symbol(oddD;N)
            continue
        if r4odd == 0:
            (ep, _odd) = factor_pint_out_power_of_base_(p, _odd)
            if ep&1:
                return None
            pe_pairs.append((p, ep))
        elif -1 == Jacobi_symbol(p, r4odd):
            return None
        tmp -= floor_log2(p)
        if tmp <= 0:
            break
    else:
        raise 000
    pe_pairs
    _odd
    if not _odd == odd:
        odd = _odd
        # [odd >= 1]
        e4odd = floor_log2(odd)
        dr_ls = vprime_list = _5vprime_list(odd, dr_ls, strict=False, max1_6init=0)
        e4rt = e4odd//2
    # [odd >= 1]
    odd
    pe_pairs
    e4odd
    dr_ls
    e4rt




    r'''[[[
[k>=2][n**k == m]:
    [em := floor_log2(m)]
    [en := em//k]
    [k*en <= em < 1+k*en]
    [k*en <= em < 1+em < 2+k*en <= k+k*en]
    [en <= em/k < (1+em)/k < (1+en)]
    [em <= log2(m) < (1+em)]
    [en <= em/k <= log2(n)==log2(m)///k < (1+em)/k < (1+en)]
    [en <= log2(n) < (1+en)]
    [en == floor_log2(n)]
    [k==2]:
        [n < Mj/4 == 2**(j-2)]:
            [1+en <= j-2]
            [j
            >= 3+en
            == 3+em//2
            == 3+floor_log2(m)//2
            == 3+(-1+m.bit_length())//2
            == 2+(1+m.bit_length())//2
            == (5+m.bit_length())//2
            ]
            [j >= (5+m.bit_length())//2]
        [[n < Mj/4 == 2**(j-2)] <-> [j >= (5+m.bit_length())//2]]
        [[n < Mj/4 == 2**(j-2)] <-> [j >= (6+floor_log2(m))//2]]

    #]]]'''#'''
    #########
    # [odd >= 1]
    #e4odd = -1+odd.bit_length()
    #e4rt = e4odd//2
    #########
    #j = (6+e4odd)//2
    j = 3 +e4rt
    # !! [odd >= 1]
    # [odd.bit_length() >= 1]
    # [j >= 3]
    # [[(5+odd.bit_length())//2 >= 3] <-> [odd >= 1]]
    # [j >= 3] <-> 4 roots
    (rt, _, _, _) = sqrts_of_odd_mod_zpow_(j, odd)
    # [rt**2 %2**j == odd %2**j]
    # [rt < 2**(j-2)]
    # !! [sqrt(odd) < 2**(1+e4rt) == 2**(j-2)]
    # [max(rt, sqrt(odd)) < 2**(j-2)]
    # [[is_square_(m)] <-> [rt == sqrt(odd)]]
    if not e4rt == floor_log2(rt):
        return None
    # [e4rt == floor_log2(rt)]
    # [2**e4rt <= rt < 2**(1+e4rt) == 2**(j-2)]
    # [max(rt, sqrt(odd)) < 2**(j-2)]

    it = iter(dr_ls)
    if not (2, 1) == next(it):raise 000
    it

    e4sq = (1+e4rt)*2
    assert e4sq >= 1+e4odd
    # !! [2**e4rt <= rt < 2**(1+e4rt)]
    # [2**e4sq > rt**2]
    # !! [2*e4rt <= e4odd < 1+2*e4rt]
    # [e4sq > 1+e4odd]
    # [2**e4sq > 2**(1+e4odd) > odd]
    # [2**e4sq > max(odd, rt**2)]
    tmp = e4sq -j
    sz = 0
    for sz, (p, r4odd) in enumerate(it, 1):
        # [sz >= 1]
        # [M:=2**j*II(prime_list[1:sz-1])]
        #   [M >= 2**(e4sq -tmp)]
        #   [odd%M == rt**2 %M]
        #
        # [p == prime_list[sz-1]]
        # [r4odd == odd%p]
        if not r4odd == pow(rt, 2, p):
            return None
        tmp -= floor_log2(p)
        # [M:=2**j*II(prime_list[1:sz])]
        #   [M >= 2**(e4sq -tmp)]
        #   [odd%M == rt**2 %M]
        if tmp <= 0:
            # [tmp <= 0]
            # [M >= 2**(e4sq -tmp) >= 2**e4sq > max(odd, rt**2)]
            break
    else:
        raise 000
    # [M:=2**j*II(prime_list[1:sz])]
    # [M > max(odd, rt**2)]
    # [odd%M == rt**2 %M]
    # ==>>:
    # [odd == odd%M == rt**2 %M == rt**2]
    # [rt == sqrt(odd)]
    # [is_square_(m)]
    n = rt
    for p, ep in pe_pairs:
        # [ep%2 == 0]
        n *= p**(ep>>1)
    n <<= (ez>>1)
    n
    return n
may_perfect_sqrt_ = may_perfect_sqrt_of_

def may_perfect_kth_root_of__k_is_prime__via_CRT_(k, m, /, **kwds4CRT):
    using_floor_kth_root = False
    # [k::prime]
    check_int_ge(2, k)
    if k == 2:
        return may_perfect_sqrt_of_(m, using_floor_kth_root=using_floor_kth_root, **kwds4CRT)
    # [k >= 3]
    return may_perfect_kth_root_of__k_is_odd_prime__via_CRT_(k, m, **kwds4CRT)

r'''[[[
e4rt足够小，即[2**e4rt..<2**(1+e4rt)]足够小，直接搜索根
    必然 [m%rt == 0]
    [[m%a == 0][m%b == 0]]
        必须是lcm(a,b) => 超界 即 不存在
e4rt足够大，即e4odd//k足够大，则 可以在[..<e4odd]间找到(1+k*d)型素数，用于提前检测是否k次幂方
#]]]'''#'''
def may_perfect_kth_root_of__k_is_odd_prime__via_CRT_(k, m, /, *, vprime_list=None):
    #, **kwds4CRT:vprime_list
    using_floor_kth_root = False
    # [k::prime]
    # [k%2 == 1]
    # [k >= 3]
    check_int_ge(3, k)
    check_int_ge(0, m)
    # [m >= 0]
    # [k >= 3]
    if not (k&1):raise ValueError(k)
    # [k %2 == 1]

    if m <= 1:
        return m
    # [m >= 2]

    (ez, odd) = factor_pint_out_power_of_base_(2, m)
    # [m == 2**ez*odd]
    if not ez%k == 0:
        return None
    # [ez%k == 0]
    # [odd >= 1]
    if odd == 1:
        return 1<<(ez//k)
    # [odd >= 2]
    # !! [k >= 3]
    # [odd**/k > 1]
    e4odd = floor_log2(odd)
    # [2**e4odd <= odd < 2**(e4odd+1)]
    if e4odd < k:
        # [2**e4odd <= odd < 2**(e4odd+1) <= 2**k]
        # [odd**/k < 2]
        # !! [odd**/k > 1]
        # [1 < odd**/k < 2]
        return None
    e4rt = e4odd//k
    # [e4rt == floor_log2(odd**/k)]

    max1_q = e4odd*k.bit_length()
    dr_ls = vprime_list = _5vprime_list(odd, vprime_list, strict=False, max1_6init=max1_q)
    ps = dr_ls.the_prime_list
    e4e4odd = floor_log2(e4odd)
    tmp = 2+e4rt//e4e4odd
    for q in ps.iter_find_primes_if_be_1addKmulX__lt_(max1_q, k):
        # [q::prime]
        # [q%k == 1]
        d = q//k
        _, r4odd = dr_ls(q) # == odd%q
        if not pow(r4odd, d, q) < 2:
            return None
        tmp -= floor_log2(q)
        if tmp <= 0:
            break

    ##############################
    # CRT or kth_root_of_odd_mod_zpow__k_is_odd_
    ##############################
        #
    it = iter(dr_ls)
    qr_ls = []
    p_rt_pairs = []
    #IIps = 1
    _e = 1+e4rt
    for p, r4odd in it:
        # [p::prime]
        # [r4odd == odd%p]
        if p%k == 1:
            qr_ls.append((p, r4odd))
            continue
        # [(p-1)%k =!= 0]
        # !! [k::prime]
        # [gcd(k, p-1) == 1]
        vk = pow(k, -1, p-1)
        # [vk*k %(p-1) == 0]
        rt6p = pow(r4odd, vk, p)
        # !! [p::prime]
        # !! [r4odd == odd%p]
        # [rt6p == odd**vk%p == (rt**k)**vk%p == rt%p]
        p_rt_pairs.append((p,rt6p))
        #IIps *= p
        #if IIps > 2**(1+e4rt): break
        _e -= floor_log2(p)
        if _e <= 0:break
    p_rt_pairs
    #IIps
    _e
    qr_ls
    rt = apply_CRT__pairs(p_rt_pairs, extended=False)
    # [[is_kth_power_(k;m)] <-> [rt == (odd**/k)]]
    if not e4rt == floor_log2(rt):
        return None
    # [e4rt == floor_log2(rt)]
    ##############################

    ##############################
    _e
    e4pw_rt = (1+e4rt)*k
    # !! [e4rt == floor_log2(rt)]
    # [2**e4rt <= rt < 2**(1+e4rt)]
    # [rt**k < (2**(1+e4rt))**k == 2**e4pw_rt]
    # [rt**k < 2**e4pw_rt]
    # !! [e4rt := e4odd//k]
    # [k*e4rt <= e4odd < k*(1+e4rt) == e4pw_rt]
    # [e4odd < e4pw_rt]
    # [1+e4odd <= e4pw_rt]
    # !! [e4odd == floor_log2(odd)]
    # [2**e4odd <= odd < 2**(1+e4odd)]
    # [odd < 2**(1+e4odd) <= 2**e4pw_rt]
    # [odd < 2**e4pw_rt]
    # [max(odd,rt**k) < 2**e4pw_rt]
    #
    lowb4e4IIps = (1+e4rt) -_e
    tmp = e4pw_rt -lowb4e4IIps
    for q, r4odd in chain(qr_ls, it):
        # [q::prime]
        # [r4odd == odd%q]
        if not r4odd == pow(rt, k%(q-1), q):
            return None
        tmp -= floor_log2(q)
        # [tmp == e4pw_rt -lowb4e4IIps -lowb4e4IIqs]
        if tmp <= 0:
            # [e4M >= lowb4e4IIps +lowb4e4IIqs == e4pw_rt -tmp >= e4pw_rt]
        # [max(odd,rt**k) < 2**e4pw_rt <= 2**e4M <= M]
            # [odd == odd%M == rt**k%M == rt**k]
            # [odd == rt**k]
            break
    else:
        raise 000
    # [odd == rt**k]
    # [rt == odd**/k]
    # [is_kth_power_(k;m)]
    # !! [m == 2**ez*odd]
    # [m == 2**ez*rt**k]
    # !! [ez%k == 0]
    # [(m**/k) == 2**(ez///k)*rt]
    n = rt << (ez//k)
    return n




def _run_lt_(m, /, *, validate, using_floor_kth_root:'not _default4using_floor_kth_root;once be False'):
    if validate:
        from math import gcd
        from seed.math.prime_sieve.sieve_lt import tabulate_may_prime_factorization4uint_lt_
        u2p2e = tabulate_may_prime_factorization4uint_lt_(m)
    for u in range(2, m):
        (rt, e) = factor_pint_as_perfect_power_(u, using_floor_kth_root=using_floor_kth_root)
        if validate:
            p2e = u2p2e[u]
            _e = gcd(*p2e.values())
            if not e == _e:raise Exception((u, p2e, _e, (rt, e)))
            if not rt**e == u:raise Exception((u, p2e, _e, (rt, e)))




__all__
from seed.math.factor_pint.perfect_power.detect_perfect_power import detect_perfect_power_, is_perfect_power_, factor_pint_as_perfect_power_
from seed.math.factor_pint.perfect_power.detect_perfect_power import is_kth_power_, is_square_, is_cube_

from seed.math.factor_pint.perfect_power.detect_perfect_power import may_perfect_kth_root_of_, may_perfect_sqrt_of_, may_perfect_cbrt_of_
333;from seed.math.factor_pint.perfect_power.detect_perfect_power import may_perfect_kth_root_, may_perfect_sqrt_, may_perfect_cbrt_

from seed.math.factor_pint.perfect_power.detect_perfect_power import may_perfect_kth_root_of__k_is_prime_, may_perfect_kth_root_of__factorization4k_, may_perfect_kth_root_of_



from seed.math.factor_pint.perfect_power.detect_perfect_power import (
detect_perfect_power_
,   is_perfect_power_
,   factor_pint_as_perfect_power_
#
,is_cube_,      is_perfect_cube_
,   may_perfect_cbrt_of_,  may_perfect_cbrt_
,is_square_,    is_perfect_square_
,   may_perfect_sqrt_of_,  may_perfect_sqrt_
#
,is_kth_power_, is_perfect_kth_power_
,   may_perfect_kth_root_of_,  may_perfect_kth_root_
,       may_perfect_kth_root_of__factorization4k_
,           may_perfect_kth_root_of__k_is_prime_
#
,may_perfect_sqrt_of__via_floor_kth_root_
,may_perfect_kth_root_of__via_floor_kth_root_
#
,may_perfect_sqrt_of__via_CRT_
,may_perfect_kth_root_of__factorization4k__via_CRT_
,may_perfect_kth_root_of__k_is_prime__via_CRT_
,may_perfect_kth_root_of__k_is_odd_prime__via_CRT_
)

from seed.math.factor_pint.perfect_power.detect_perfect_power import *
