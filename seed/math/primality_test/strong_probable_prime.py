#__all__:goto
r'''[[[
e ../../python3_src/seed/math/primality_test/strong_probable_prime.py
[SPRP=strong_probable_prime]
[SPSP=strong_pseudoprime=strong_probable_prime\-\prime=strong_probable_prime/-\composite]

seed.math.primality_test.strong_probable_prime
py -m nn_ns.app.debug_cmd   seed.math.primality_test.strong_probable_prime -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.primality_test.strong_probable_prime:__doc__ -ht # -ff -df
#######

[[
move_from:
e ../../python3_src/seed/math/prime_gens.py
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.primality_test.strong_probable_prime   @f

]]]'''#'''
__all__ = r'''

Error
    IsPrimeError
    PrimalityUndeterminedError
        OverflowError__Miller_Rabin_primality_test__A014233







A014233     n2upperbound4Miller_Rabin_primality_test_using_first_n_plus1_primes_as_basis
    prime_basis4A014233
    prime_basis_set4A014233

is_prime__using_A014233_    is_prime__le_pow2_81_
    OverflowError__Miller_Rabin_primality_test__A014233







is_strong_probable_prime__basis__with_trial_division_
    is_strong_probable_prime__basis_
        is_strong_probable_prime_

    continuous_trial_division_
        iter_continuous_prime_bases_
        callable5xfilter4continuous_bases
        mk_initial_state4filter4continuous_bases_
        mk_filter4continuous_bases4fixed_size
        filter4continuous_bases4empty
        filter4continuous_bases4II_prime_basis_gtN







find_min_prime_witness4odd_composite_
    iter_until_found_min_prime_witness4odd_composite_
        IsPrimeError





is_prime__tribool_
    mk_tribool_delegate5PRP_test_

    detect_strong_probable_prime__not_waste_too_much_time_

    Case4is_prime__tribool_
        iter_prime_basis4II_prime_basis_gtN_
            calc_len_prime_basis4II_prime_basis_gtN_

    prev_may_probable_prime__lt_
    next_probable_prime__ge_
    iter_probable_primes__inside_
    iter_probable_primes__ge_lt_
        iter_probable_primes__between_
    iter_probable_primes__ge_
    reversed_iter_probable_primes__lt_










prime_filter__using_primality_test_
    default4is_prime_and_may_upperbound
        is_prime__le_pow2_81_
            OverflowError__Miller_Rabin_primality_test__A014233
            next_may_prime__le_pow2_81__ge_
            prev_may_prime__le_pow2_81__lt_
            iter_primes__inside_
                PrimalityUndeterminedError
            iter_primes__ge_lt_
                iter_primes__between_
            iter_primes__le_pow2_81__ge_
            reversed_iter_primes__le_pow2_81__lt_
                raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_
                raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_








pairwise_diff_
    iter_pairwise_diff_probable_primes__ge_
    iter_pairwise_diff_primes__le_pow2_81__ge_


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from enum import Enum, auto

from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__, 'count:_count'):
    from itertools import islice, chain, pairwise, filterfalse
    from itertools import count as _count
    from seed.math.gcd import gcd

    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.tiny_.dict_op__add import set_add
    from seed.tiny_.mk_reiterable import mk_reiterable
    from seed.debug.print_err import print_err

    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_2_powers
    from seed.math.prime_sieve.sieve_lt import iter_all_strict_sorted_primes_#to replace:prime_gen



#.#################################
___end_mark_of_excluded_global_names__0___ = ...

from seed.math.primality_test.errors import Error, IsPrimeError, PrimalityUndeterminedError, OverflowError__Miller_Rabin_primality_test__A014233
    # !! except OverflowError__Miller_Rabin_primality_test__A014233:
    # => not lazy import
    # => add to __all__ ok




#view others/数学/prime/primality_test.txt
# https://oeis.org/A014233
# A014233 Smallest odd number for which Miller-Rabin primality test on bases <= n-th prime does not reveal compositeness.
n2upperbound4Miller_Rabin_primality_test_using_first_n_plus1_primes_as_basis = A014233 = (2047, 1373653, 25326001, 3215031751, 2152302898747, 3474749660383, 341550071728321, 341550071728321, 3825123056546413051, 3825123056546413051, 3825123056546413051, 318665857834031151167461, 3317044064679887385961981)
#assert len(A014233) == 13
assert len(A014233) >= 13
assert A014233[10] < 2**64 < A014233[11]
assert 2**10 < A014233[0] < 2**11
assert 2**20 < A014233[1] < 2**21
assert 2**24 < A014233[2] < 2**25
assert 2**31 < A014233[3] < 2**32
assert 2**40 < A014233[4] < 2**41
assert 2**41 < A014233[5] < 2**42
assert 2**48 < A014233[6] < 2**49
assert 2**48 < A014233[7] < 2**49
assert 2**61 < A014233[8] < 2**62
assert 2**61 < A014233[9] < 2**62
assert 2**61 < A014233[10] < 2**62
assert 2**78 < A014233[11] < 2**79
assert 2**81 < A014233[12] < 2**82
        # II_prime_basis_gtN___vs___A014233:goto

assert 2**48 < A014233[6] == A014233[7] < 2**49
assert 2**61 < A014233[8] == A014233[9] == A014233[10] < 2**62
assert len({*A014233[:13]}) == 13-1-2 == 10

#.prime_basis4A014233 = prime_gen[:len(A014233)]
prime_basis4A014233 = tuple(iter_all_strict_sorted_primes_(size=len(A014233)))

assert prime_basis4A014233[11] == 37
assert len(prime_basis4A014233) == len(A014233)
check_type_is(tuple, A014233)
check_type_is(tuple, prime_basis4A014233)
prime_basis_set4A014233 = frozenset(prime_basis4A014233)
if 0:
    #move to below
    assert not any(map(is_prime__using_A014233_, A014233))







def _prepare4is_prime__tribool_(prime_basis, n, /, *, skip_check, _not_seq=False):
    r'''[[[
precondition:
    [prime_basis is strict sorted]
    [len(prime_basis) >= 1]
    [prime_basis[0] == 2]
    [set(raw_iter_all_strict_sorted_primes__lt_(1+prime_basis[-1])) |<=| set(prime_basis)]

postcondition:
    * True:
        [n is prime]
    * False:
        [n is not prime]
        [[n < 2]or[n is composite]]
    * ...:
        [n is odd][n >= 3]
        [@[b :<- prime_basis] -> [b%n =!= 0]]
        #extra:
        [n > prime_basis[-1]]
        [[not skip_check] -> [@[p :<- prime_basis] -> [n%p =!= 0]]]
        [[not skip_check] -> [n >= (1+prime_basis[-1])**2]]

    #]]]'''#'''
    assert prime_basis
    assert _not_seq or prime_basis[0] == 2
    #assert set(raw_iter_all_strict_sorted_primes__lt_(1+prime_basis[-1])) <= set(prime_basis)

    if skip_check:
        #e.g. factor_pint_by_trial_division_, n reduce...
        check_type_is(int, n)
        if not (n >= 3 and (n&1) == 1): raise ValueError(n)
        if not (_not_seq or n > prime_basis[-1]): raise ValueError(n)
        # [n is odd][n >= 3]
        # [@[b :<- prime_basis] -> [b%n =!= 0]]
        # [n > prime_basis[-1]]
        return ...

    check_type_is(int, n)
    if n < 2:
        return False
    if n & 1 == 0:
        return n == 2
    ######################
    # [n is odd][n >= 3]
    ######################
    if n < 9:
        return True
    for p in prime_basis:
        assert not n < p
        if n < p**2:
            return True
        if n%p == 0:
            return n == p
    # [@[p :<- prime_basis] -> [n%p =!= 0]]
    # [n > prime_basis[-1]]
    p_6 = p%6
    if p_6 == 5:
        d = 2
    elif p_6 == 1:
        d = 4
    elif p_6 == 3:
        d = 2
    elif p_6 == 2:
        d = 1
    else:
        raise ValueError(prime_basis)
    _prp = (p+ d)
    # [_prp <= next_prime__ge_(1+p)]
    if n < _prp**2:
        # [n < _prp**2 <= next_prime__ge_(1+p)**2]
        return True

    ######################
    # [@[b :<- prime_basis] -> [b%n =!= 0]]
    ######################
    return ...

def is_prime__using_A014233_(n, /, *, skip_check=False, to_find_sqrt_neg1=False):
    r'''[[[
n/int -> is_prime/bool | ^OverflowError__Miller_Rabin_primality_test__A014233
precondition:
    [n is int]
postcondition:
    * True:
        [n is prime]
    * False:
        [n is not prime]
        [[n < 2]or[n is composite]]
    * ^OverflowError__Miller_Rabin_primality_test__A014233:
        [[n >= is_prime__using_A014233_.upperbound > A014233[-1] > 2**81][is_strong_probable_prime__basis_(prime_basis4A014233, n) is True]]

        ######################
        [is_strong_probable_prime__basis_(prime_basis4A014233, n) is True] ==>> [@[p :<- prime_basis4A014233] -> [n%p =!= 0]]
        ######################
        #useless:
        [n is odd][n >= 3]
        [@[b :<- prime_basis4A014233] -> [b%n =!= 0]]
        #extra:
        [n > prime_basis4A014233[-1]]
        [[not skip_check] -> [@[p :<- prime_basis4A014233] -> [n%p =!= 0]]]
        [[not skip_check] -> [n >= (1+prime_basis4A014233[-1])**2]]




######################
[n,b :: int][n =!= 0][b%n =!= 0]:
    [is_strong_probable_prime_(b;n) =[def]= [[n >= 3][n%2==1][(e,t) :=> [[e,t :: pint][t%2==1][t*2**e == n-1]]][[b**t %n == +1]or[?[s :<- [0..<e]] -> [(b**t)**(2**s) %n == -1]]]]]

    [[is_strong_probable_prime_(b;n)] -> [gcd(n,b) == 1]]

primality_test_of_Miller_Rabin
  probabilistic primality test
    return probably_prime | composite
  --> deterministic algorithm

    #]]]'''#'''
    #see:is_strong_probable_prime__basis_
    #see:is_prime__tribool_
    #see:raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_
    r = _prepare4is_prime__tribool_(prime_basis4A014233, n, skip_check=skip_check)

    if not r is ...:
        return r
    # [n is odd][n >= 3]
    # [@[b :<- prime_basis4A014233] -> [b%n =!= 0]]
    #extra:
    # [n > prime_basis4A014233[-1]]
    # [[not skip_check] -> [@[p :<- prime_basis4A014233] -> [n%p =!= 0]]]
    # [[not skip_check] -> [n >= (1+prime_basis4A014233[-1])**2]]
    #
    A014233
    prime_basis4A014233
    if 0:
        for i1, max1 in enumerate(A014233, 1):
            if n <= max1:
                if n == max1:
                    return False
                basis = prime_basis4A014233[:i1]
                return _kw__is_strong_probable_prime__basis_(basis, n)
    else:
        for i1, max1 in enumerate(A014233, 1):
            if n < max1:
                basis = prime_basis4A014233[:i1]
                return _kw__is_strong_probable_prime__basis_(basis, n, to_find_sqrt_neg1=to_find_sqrt_neg1)
        if n == max1:
            if to_find_sqrt_neg1:
                bool_or_with_sqrts = _kw__is_strong_probable_prime__basis_(prime_basis4A014233, n, to_find_sqrt_neg1=to_find_sqrt_neg1)
                b, sqrts = _pair5bool_or_with_sqrts_(bool_or_with_sqrts)
                #print(sqrts)
                assert not b
                assert sqrts == [806966215798523717614900, 1560865212556530034242163]
                #if len(sqrts) == 2: return False, sqrts
                if sqrts:
                    #must return False
                    return False, sqrts
            return False
    assert n > A014233[-1]
    # [n > A014233[-1]]
    #if not _kw__is_strong_probable_prime__basis_(prime_basis4A014233, n):
        #return False
    bool_or_with_sqrts = _kw__is_strong_probable_prime__basis_(prime_basis4A014233, n, to_find_sqrt_neg1=to_find_sqrt_neg1)
    if not _bool__5bool_or_with_sqrts_(bool_or_with_sqrts):
        return bool_or_with_sqrts
    # [[n >= is_prime__using_A014233_.upperbound > A014233[-1] > 2**81][is_strong_probable_prime__basis_(prime_basis4A014233, n) is True]]
        #see:_find_upperbound4is_prime__using_A014233_()

    upperbound = is_prime__using_A014233_.upperbound #max1+2
    raise OverflowError__Miller_Rabin_primality_test__A014233(f'[{upperbound} == upperbound <= n == {n}]')
if 1:
    #see below:_find_upperbound4is_prime__using_A014233_
    is_prime__using_A014233_.upperbound = A014233[-1]+2
        #only for first raise in _find_upperbound4is_prime__using_A014233_

def is_strong_probable_prime_(base, n, /, *, to_find_sqrt_neg1=False):
    'base/int{>=2,%n=!=0} -> n{>=3,odd} -> [n is base-SPRP]'
    return _kw__is_strong_probable_prime__basis_([base], n, to_find_sqrt_neg1=to_find_sqrt_neg1)
def _bool__5bool_or_with_sqrts_(bool_or_with_sqrts, /):
    b, sqrts = _pair5bool_or_with_sqrts_(bool_or_with_sqrts)
    return b
def _sqrts__5bool_or_with_sqrts_(bool_or_with_sqrts, /):
    b, sqrts = _pair5bool_or_with_sqrts_(bool_or_with_sqrts)
    return sqrts
def _pair5bool_or_with_sqrts_(bool_or_with_sqrts, /):
    if type(bool_or_with_sqrts) is bool:
        b = bool_or_with_sqrts
        sqrts = []
    else:
        b, sqrts = bool_or_with_sqrts
        assert 1 <= len(sqrts) <= 2
    return b, sqrts

def iter_continuous_prime_bases_(xfilter4continuous_bases, n, /):
    # @20250130
    'may filter4continuous_bases/((k/uint -> st[k] -> prime_gen[k] -> tmay st[k+1])|((-1) -> None -> n/int -> st0)) -> n/int -> Iter prime_gen[k]'
    f = callable5xfilter4continuous_bases(xfilter4continuous_bases)
    st = mk_initial_state4filter4continuous_bases_(f, n)
    #.for k, p in enumerate(iter(prime_gen)):
    for k, p in enumerate(iter_all_strict_sorted_primes_()):
        tm = f(k, st, p)
        if not tm:break
        yield p
        [st] = tm
    return
def continuous_trial_division_(xfilter4continuous_bases, n, /):
    # @20250130
    'may filter4continuous_bases/((k/uint -> st[k] -> prime_gen[k] -> tmay st[k+1])|((-1) -> None -> n/int -> st0)) -> n/int -> (-1/[is_prime(n)]|0/YET|1/[n < 2]|prime_factor/{2..<n})'
    check_type_is(int, n)
    r = _continuous_trial_division_(xfilter4continuous_bases, n)
    check_int_ge(-1, r)
    assert (r&1) or (r < 3)
    return r
def _continuous_trial_division_(xfilter4continuous_bases, n, /):
    #see:_prepare4is_prime__tribool_
    bases4div = iter_continuous_prime_bases_(xfilter4continuous_bases, n)

    check_type_is(int, n)
    if n < 2:
        return 1 # [n<2]
    if n & 1 == 0:
        return -1 if n == 2 else 2
    ######################
    # [n is odd][n >= 3]
    ######################
    if n < 9:
        return -1 # [is_prime(n)]
    p = 2
    for p in bases4div:
        assert not n < p
        if n < p**2:
            return -1 # [is_prime(n)]
        if n%p == 0:
            return -1 if n == p else p
    # [@[p :<- bases4div] -> [n%p =!= 0]]
    # [n > bases4div[-1]]
    p_6 = p%6
    d = _041202[p%6]
        #_041202 = (0,4,1,2,0,2)
    if d == 0:raise ValueError(n)
    _prp = (p+d)
    # [_prp <= next_prime__ge_(1+p)]
    if n < _prp**2:
        # [n < _prp**2 <= next_prime__ge_(1+p)**2]
        return -1 # [is_prime(n)]

    ######################
    # [@[b :<- bases4div] -> [b%n =!= 0]]
    ######################
    return 0 # YET
_041202 = (0,4,1,2,0,2)


def callable5xfilter4continuous_bases(xfilter4continuous_bases, /):
    x = xfilter4continuous_bases
    if callable(x):
        f = x
        return f
    if x is None:
        #default vivi case@is_prime__tribool_
        return filter4continuous_bases4II_prime_basis_gtN
    if x is False:
        #null_iter
        return filter4continuous_bases4empty
    if type(x) is int and x >= 0:
        sz = x
        return mk_filter4continuous_bases4fixed_size(sz)
    raise ValueError(x)
def mk_initial_state4filter4continuous_bases_(filter4continuous_bases, n, /):
    'filter4continuous_bases -> n/int -> st0'
    st0 = filter4continuous_bases(-1, None, n)
    return st0
#def mk_filter4continuous_bases4iterable(bases4div, /):
def mk_filter4continuous_bases4fixed_size(sz, /):
  def filter4continuous_bases4fixed_size(k, st_k, prime_k, /):
    'imay k -> (st[k] | None) -> (prime_gen[k]|n) -> ((tmay st[k+1]) | st0) # ((k/uint -> st[k] -> prime_gen[k] -> tmay st[k+1])|((-1) -> None -> n/int -> st0))'
    if k < 0:
        st0 = 0
        return st0
    _sz = st_k
    if not _sz < sz:
        return ()
    st_k1 = _sz+1
    return (st_k1,)
  if 1:
    return filter4continuous_bases4fixed_size
def filter4continuous_bases4empty(k, st_k, prime_k, /):
    'imay k -> (st[k] | None) -> (prime_gen[k]|n) -> ((tmay st[k+1]) | st0) # ((k/uint -> st[k] -> prime_gen[k] -> tmay st[k+1])|((-1) -> None -> n/int -> st0))'
    if k < 0:
        return None
    return ()
def filter4continuous_bases4II_prime_basis_gtN(k, st_k, prime_k, /):
    'imay k -> (st[k] | None) -> (prime_gen[k]|n) -> ((tmay st[k+1]) | st0) # ((k/uint -> st[k] -> prime_gen[k] -> tmay st[k+1])|((-1) -> None -> n/int -> st0))'
    # see:II_prime_basis_gtN
    # see:iter_prime_basis4II_prime_basis_gtN_
    if k < 0:
        assert k == -1
        assert st_k is None
        n = prime_k
        st0 = (n, ii:=1)
        return st0
    (n, ii) = st_k
    if ii > n:
        return ()
    ii *= prime_k
    st_k1 = (n, ii)
    return (st_k1,)
#filter4continuous_bases4II_prime_basis_gtN.n2st0 = lambda n, /: (n, 1)
def is_strong_probable_prime__basis__with_trial_division_(xfilter4continuous_bases4div, bases4SPRP, n, /):
    # @20250130
    'may filter4continuous_bases4div/((k/uint -> st[k] -> prime_gen[k] -> tmay st[k+1])|((-1) -> None -> n/int -> st0)) -> bases4SPRP/(Iter int) -> n/int -> whether_SPRP/bool # [SPRP == strong probable-prime]'
    r = continuous_trial_division_(xfilter4continuous_bases4div, n)
    if r:
        return r == -1
        match r:
            case -1:
                # [is_prime(n)]
                return True
            case 1:
                # [n < 2]
                return False
            case prime_factor:
                assert 2 <= prime_factor < n
                assert n%prime_factor == 0
                return False
    # [r==0] YET
    is_ok, factor_or_bases = _std_finite_basis_(n, bases4SPRP)
    if not is_ok:
        return False
    bases = factor_or_bases
    return is_strong_probable_prime__basis_(bases, n)

def is_strong_probable_prime__basis_(basis, n, /, *, to_find_sqrt_neg1=False):
    'basis/[base/int{>=2,%n=!=0}] -> n{>=3,odd} -> [n is basis-SPRP] /(bool if not to_find_sqrt_neg1 or not found sqrt_neg1 else (bool, [sqrt_neg1]/[int%n <= n//2]{len=1/(False|True),2/False}))'
    #see:is_prime__using_A014233_
    return _kw__is_strong_probable_prime__basis_(basis, n, to_find_sqrt_neg1=to_find_sqrt_neg1)
def _kw__is_strong_probable_prime__basis_(basis, n, /, *, to_find_sqrt_neg1):
    check_type_is(int, n)
    if not (n >= 3 and (n&1) == 1): raise ValueError(n)
    # [n is odd][n >= 3]
    n_neg1 = n-1

    def _iter_basis(n, n_neg1, basis, /):
        s = set()
        for base in basis:
            check_type_is(int, base)
            base %= n
            if not set_add(s, base):continue
            if not 1 < base < n_neg1: raise ValueError((base, n))
            # [base%n !<- {0,1,n-1}]
            # [base%n =!= 0]
            yield base
    basis = _iter_basis(n, n_neg1, basis)
    # [@[b :<- basis] -> [b%n =!= 0]]

    ######################
    # [n is odd][n >= 3]
    # [@[b :<- basis] -> [b%n =!= 0]]
    ######################

    e, odd = factor_pint_out_2_powers(n_neg1)
    e_neg1 = e-1

    #return all(_is_strong_probable_prime_(base, n, n_neg1, e_neg1, odd) for base in basis)
    #if not to_find_sqrt_neg1:
    #    return all(_is_strong_probable_prime_(base, n, n_neg1, e_neg1, odd, False) for base in basis)
    #else:
    if 1:
        sqrts = []
        def put(bool_or_bool_sqrt_x, /):
            if type(bool_or_bool_sqrt_x) is bool:
                b = bool_or_bool_sqrt_x
            else:
                b, sqrt = bool_or_bool_sqrt_x
                neg_sqrt = n -sqrt
                if neg_sqrt < sqrt:
                    sqrt, neg_sqrt = neg_sqrt, sqrt
                assert 0 < sqrt < neg_sqrt < n
                if b:
                    sqrt_neg1 = sqrt
                    if not sqrt in sqrts:
                        sqrts.append(sqrt)
                    b = len(sqrts) == 1
                else:
                    nonplain_sqrt_1 = sqrt
                    sqrts.append((nonplain_sqrt_1,))
                    b; pass
            return b

        r = all(put(_is_strong_probable_prime_(base, n, n_neg1, e_neg1, odd, True)) for base in basis)
        #bug:return sqrts or r
        #   may be found one sqrt then found not probable_prime
        #   hence len(sqrts)==1 donot repr True
        if to_find_sqrt_neg1 and sqrts:
            if len(sqrts)==2:
                assert r is False
            return (r, sqrts)
        return r
def _is_strong_probable_prime_(base, n, n_neg1, e_neg1, odd, to_find_sqrt_neg1, /):
    '-> (bool if not to_find_sqrt_neg1 or not found sqrt_neg1 else (True, sqrt_neg1/(int%n))|(False, nonplain_sqrt_1/(int%n)))'
    ######################
    # [n is odd][n >= 3]
    # [[base%n =!= 0]]
    ######################
    d = pow(base, odd, n)
    if d == 1:
        return True
    if 1:
        if d == n_neg1:
            return True
    for _ in range(e_neg1):
        d2 = pow(d, 2, n)
        if d2 == n_neg1:
            if to_find_sqrt_neg1:
                sqrt_neg1 = d
                return (True, sqrt_neg1)
            return True
        if d2 == 1:
            if to_find_sqrt_neg1:
                nonplain_sqrt_1 = d
                return (False, nonplain_sqrt_1)
            return False
        d = d2
    return False

def __():
    from seed.for_libs.for_time import timer__print_err__thread_wide

    timer = timer__print_err__thread_wide
    _to_show_ = __name__ == "__main__"
    with timer(prefix='apply is_prime__using_A014233_ on A014233', _to_show_=_to_show_):
        assert not any(map(is_prime__using_A014233_, A014233))
        #assert not any(len(_sqrts__5bool_or_with_sqrts_(bool_or_with_sqrts)) == 2 for bool_or_with_sqrts in (ls := [is_prime__using_A014233_(n, to_find_sqrt_neg1=True) for n in A014233])), ls
        #   SyntaxError: assignment expression cannot be used in a comprehension iterable expression
        assert (__ := [is_prime__using_A014233_(n, to_find_sqrt_neg1=True) for n in A014233]) == [False, (False, [483061]), False, False, False, False, (False, [27393523843088, 36156112808384]), (False, [27393523843088, 36156112808384]), False, False, False, (False, [107889940756980366727205, 103782637039805229854323]), (False, [806966215798523717614900, 1560865212556530034242163])], __
if __name__ == "__main__":
    __()

def _find_upperbound4is_prime__using_A014233_():
    try:
        for n in _count(A014233[-1]):
            is_prime__using_A014233_(n)
    except OverflowError__Miller_Rabin_primality_test__A014233:
        pass
    assert n == 3317044064679887385962123, (n, len(A014233)) #13"
    return n
if __name__ == "__main__":
#if 0b0000:
    is_prime__using_A014233_.upperbound = _find_upperbound4is_prime__using_A014233_()
else:
    assert len(A014233) == 13
    is_prime__using_A014233_.upperbound = 3317044064679887385962123
assert is_prime__using_A014233_.upperbound - A014233[-1] == 142




def iter_until_found_min_prime_witness4odd_composite_(odd_composite, /):
    'odd_composite/int{odd,>=9} -> Iter (whether_sprp, prime_idx, prime_base){if not whether_sprp then prime_base is min_prime_witness) | ^IsPrimeError # [[whether_sprp == is_strong_probable_prime_(prime_base, odd_composite)][prime_gen[prime_idx] == prime_base][not is_strong_probable_prime_(min_prime_witness, odd_composite)]]'
    #NOTE: may have [min_witness_base < min_prime_witness]
    check_type_is(int, odd_composite)
    if not (odd_composite&1 ==1):raise ValueError(odd_composite)
    if not odd_composite >= 9:raise ValueError(odd_composite)
    # [odd_composite is odd][odd_composite >= 3**2]
    return _iter_until_found_min_prime_witness4odd_composite_(odd_composite)
def _iter_until_found_min_prime_witness4odd_composite_(n, /):
    #n = odd_composite
    # [n is composite]
    #
    # [n is odd][n >= 3]
    n_neg1 = n-1
    e, odd = factor_pint_out_2_powers(n_neg1)
    e_neg1 = e-1
    #.for i, p in enumerate(prime_gen):
    for i, p in enumerate(iter_all_strict_sorted_primes_()):
        base = p

        q, r = divmod(n, p)
        if r == 0:
            pass
        elif not q > p: raise IsPrimeError(n) #trial_division prove primality

        # [n == q*p+r >= (p+1)*p+r >= p**2+p > p]
        # [n > p]
        # [n > base == p >= 2]

        ######################
        # [n is odd][n >= 3]
        # [[base%n =!= 0]]
        ######################
        whether_sprp = _is_strong_probable_prime_(base, n, n_neg1, e_neg1, odd, False)
        yield (whether_sprp, i, p)
        if not whether_sprp:
            return
        if r == 0:raise logic-err
def find_min_prime_witness4odd_composite_(odd_composite, /, *, with_prime_idx=False):
    'odd_composite/int{odd,>=9} -> min_prime_witness/int{prime} if not with_prime_idx else (prime_idx, min_prime_witness) | ^IsPrimeError # [[not is_strong_probable_prime_(min_prime_witness, odd_composite)][prime_gen[prime_idx] == min_prime_witness]]'
    #NOTE: may have [min_witness_base < min_prime_witness]
    for (whether_sprp, i, p) in iter_until_found_min_prime_witness4odd_composite_(odd_composite):
        pass
    assert not whether_sprp
    min_prime_witness = base = p
    if with_prime_idx:
        prime_idx = i
        return (prime_idx, min_prime_witness)
    return min_prime_witness

def __():
    prime_gen = ...
    lazy_prime_seq = prime_gen()
    for i1, max1 in enumerate(A014233, 1):
        (prime_idx, min_prime_witness) = find_min_prime_witness4odd_composite_(max1, with_prime_idx=True)
        assert prime_idx >= i1, (prime_idx, i1, max1, min_prime_witness)
            # dup!! ==>> 『==』->『>=』
        assert prime_idx == i1 or A014233[i1-1]==A014233[i1], (prime_idx, i1, max1, min_prime_witness)
        assert prime_gen[prime_idx] == min_prime_witness
#if __name__ == "__main__":
if 0b0000:
    __()

class Case4is_prime__tribool_(Enum):
    '[case :: (Case4is_prime__tribool_ | [basis/uint] | None{==II_prime_basis_gtN})] #<<==kw:case@is_prime__tribool_()'
        # @20250130: ++[case :: (___ | [basis/uint] | None)] for kw:case@next_probable_prime__ge_/prev_may_probable_prime__lt_/...
    bit_length = auto()
    ERH = auto()
    II_prime_basis_gtN = auto()
        # def____II_prime_basis_gtN:here
        # impl____II_prime_basis_gtN:goto
        # II_prime_basis_gtN___vs___A014233:goto
def detect_strong_probable_prime__not_waste_too_much_time_(n, /, *, may_bases4SPRP=None):
    'n/int -> (0|1|-1) # [0=>not prime][1=>prime][-1=>strong_probable_prime] #[case:=Case4is_prime__tribool_.II_prime_basis_gtN]'
    #r = is_prime__tribool_(n, case=Case4is_prime__tribool_.II_prime_basis_gtN)
    if not may_bases4SPRP is None:
        bases4SPRP = mk_reiterable(may_bases4SPRP)
        case = bases4SPRP
    else:
        case = None
            #=> case=Case4is_prime__tribool_.II_prime_basis_gtN
    r = is_prime__tribool_(n, case=case)
    if r is ...:
        return -1
    return int(r)
def mk_tribool_delegate5PRP_test_(is_PRP_, /, *args, **kwds):
    'probable_primality_test/(*args -> int -> **kwds -> whether_PRP/bool) -> *args -> **kwds -> tribool_primality_test/(int -> tribool_whether_prime/tribool)  # [PRP == probable-prime] # [used by (kw:delegate@is_prime__tribool_)]'
    def tribool_primality_test(n, /):
        return ... if is_PRP_(*args, n, **kwds) else False
    return tribool_primality_test
def is_prime__tribool_(n, /, *, case:[Case4is_prime__tribool_,tuple], skip_check=False, skip_A014233=False):
    r'''[[[
int -> tribool/(bool|...)

[[
precondition:
    [n is int]
    [case :: (Case4is_prime__tribool_ | None{=>II_prime_basis_gtN} | bases4SPRP/[int]) | delegate/callable/(int -> tribool)]
        eg:
        [delegate := mk_tribool_delegate5PRP_test_(is_strong_probable_prime__basis__with_trial_division_, xfilter4continuous_bases4div, bases4SPRP)]
]]
[[
postcondition:
    * True:
        [n is prime]
    * False:
        [n is not prime]
        [[n < 2]or[n is composite]]
    * ...:
        * [case is CASE.II_prime_basis_gtN]or[case is None]:
            # [prime_basis <- iter_prime_basis4II_prime_basis_gtN_(n)]
            [basis <- prime_gen[:min{i | [[i :<- [0..]][II(prime_gen[:i]) > n]]}]]
        * [case is CASE.bit_length]:
            [basis <- prime_gen[:n.bit_length()]]
        * [case is CASE.ERH]:
            [basis <- range(2, 2*n.bit_length()**2)]
        * [case :: bases4SPRP/[int]]:
            [bases := case]
            [basis <- bases]
        * [case :: delegate/callable/(int -> tribool)]:
            [delegate => ignore all other kwds]

        [[n >= is_prime__using_A014233_.upperbound > A014233[-1] > 2**81][is_strong_probable_prime__basis_(prime_basis4A014233, n) is True][is_strong_probable_prime__basis_(basis, n) is True]]
]]


[[
pseudoprime
strong pseudoprime

probable-prime (PRP)
strong probable-prime (SPRP)
  b-SPRP
Extended Riemann Hypothesis (ERH)

[n,b :: int][n =!= 0][b%n =!= 0]:
    [is_strong_probable_prime_(b;n) =[def]= [[n >= 3][n%2==1][(e,t) :=> [[e,t :: pint][t%2==1][t*2**e == n-1]]][[b**t %n == +1]or[?[s :<- [0..<e]] -> [(b**t)**(2**s) %n == -1]]]]]

    [[is_strong_probable_prime_(b;n)] -> [gcd(n,b) == 1]]
[[Extended Riemann Hypothesis (ERH)] -> @[n :: int] -> [n > 0] -> [n%2==1] -> [[is_prime_(n)] <-> [@[b :<- [2..<min(n, 2*(log n)**2)]] -> [is_strong_probable_prime_(b;n)]]]]
  # what is the base of log?
==>>:
!! [2 < e ~= 2.718281828459045 < 10]
[[Extended Riemann Hypothesis (ERH)] -> @[n :: int] -> [n > 0] -> [n%2==1] -> [[is_prime_(n)] <-> [@[b :<- [2..<min(n, 2*(ceil_log2 n)**2)]] -> [is_strong_probable_prime_(b;n)]]]]
==>>:
!! [[is_strong_probable_prime_(b;n)] -> [gcd(n,b) == 1]]
[[Extended Riemann Hypothesis (ERH)] -> @[n :: int] -> [n > 0] -> [n%2==1] -> [[is_prime_(n)] <-> [@[b :<- [2..<min(1+floor_sqrt(n), 2*(ceil_log2 n)**2)]] -> [is_strong_probable_prime_(b;n)]]]]
  # switch to trial_division
]]

[[
C.bit_length:
===
# ??? [prime_gen[n.bit_length()-1] < n]
    #see:_find_minN4bit_length__not_consider_trial_division_
    # [[n >= 6] -> [prime_gen[n.bit_length()-1] < n]]
# ??? [prime_gen[n.bit_length()]**2 <= n]
    #see:_find_minN4bit_length__consider_trial_division_
    # [[n >= 1369 == 37**2 == prime_gen[11]**2] -> [prime_gen[n.bit_length()]**2 <= n]]
===
[len(prime_basis) >= 1]
    <==> [n.bit_length() > len(prime_basis4A014233)]
===
[len(prime_basis) >= 1][last := prime_gen[n.bit_length()-1]][max(prime_basis) == prime_basis[-1] == last][min(prime_basis) == prime_basis[0] >= 2]:
    [@[b :<- prime_basis] -> [b%n =!= 0]]
        <<== [max(prime_basis) < n]
        <<== [max(prime_basis) == prime_basis[-1] == last == prime_gen[n.bit_length()-1] < n]
        <<== [prime_gen[n.bit_length()-1] < n]
        <<== [n >= 6]
===
[[n >= 6] -> [prime_gen[n.bit_length()-1] < n]]
===
[n >= 6][len(prime_basis) >= 1][last := prime_gen[n.bit_length()-1]][max(prime_basis) == prime_basis[-1] == last][min(prime_basis) == prime_basis[0] >= 2]:
    !! [[n >= 6] -> [prime_gen[n.bit_length()-1] < n]]
    !! [n >= 6]
    [prime_gen[n.bit_length()-1] < n]

    !! [max(prime_basis) == prime_basis[-1] == last]
    !! [last := prime_gen[n.bit_length()-1]]
    !! [prime_gen[n.bit_length()-1] < n]
    [max(prime_basis) < n]

    !! [min(prime_basis) == prime_basis[0] >= 2]
    !! [max(prime_basis) < n]
    [@[b :<- prime_basis] -> [2 <= b < n]]
    [@[b :<- prime_basis] -> [b%n =!= 0]]
===
[[[n >= 6][len(prime_basis) >= 1][last := prime_gen[n.bit_length()-1]][max(prime_basis) == prime_basis[-1] == last][min(prime_basis) == prime_basis[0] >= 2]] -> [@[b :<- prime_basis] -> [b%n =!= 0]]]
    #condition4CASE____bit_length:here
===
===
]]
[[
C.ERH:
===
# ??? [2* n.bit_length()**2 <= n]
    #see:_find_minN4ERH__not_consider_trial_division_
    # [[n >= 98 == 2* 7**2] -> [2* n.bit_length()**2 <= n]]
# ??? [(2* n.bit_length()**2)**2 <= n]
    #see:_find_minN4ERH__consider_trial_division_
    # [[n >= 640000 == ((2* 20**2)**2)] -> [(2* n.bit_length()**2)**2 <= n]]
===
[end := 2* n.bit_length()**2][len(prime_basis) >= 1][max(prime_basis) == prime_basis[-1] < end][min(prime_basis) == prime_basis[0] >= 2]:
    [@[b :<- prime_basis] -> [b%n =!= 0]]
        <<== [max(prime_basis) < n]
        <<== [max(prime_basis) == prime_basis[-1] < end == 2* n.bit_length()**2 <= n]
        <<== [2* n.bit_length()**2 <= n]
        <<== [n >= 98]
===
[[n >= 98] -> [2* n.bit_length()**2 <= n]]
===
[n >= 98][len(prime_basis) >= 1][max(prime_basis) == prime_basis[-1] < end == 2* n.bit_length()**2][min(prime_basis) == prime_basis[0] >= 2]:
    !! [[n >= 98] -> [2* n.bit_length()**2 <= n]]
    !! [n >= 98]
    [2* n.bit_length()**2 <= n]

    !! [max(prime_basis) == prime_basis[-1] < end == 2* n.bit_length()**2]
    !! [2* n.bit_length()**2 <= n]
    [max(prime_basis) < n]

    !! [min(prime_basis) == prime_basis[0] >= 2]
    !! [max(prime_basis) < n]
    [@[b :<- prime_basis] -> [2 <= b < n]]
    [@[b :<- prime_basis] -> [b%n =!= 0]]
===
[[[n >= 98][len(prime_basis) >= 1][max(prime_basis) == prime_basis[-1] < end == 2* n.bit_length()**2][min(prime_basis) == prime_basis[0] >= 2]] -> [@[b :<- prime_basis] -> [b%n =!= 0]]]
    #condition4CASE____ERH:here
===

]]
[[
C.II_prime_basis_gtN:
===
# ??? [[*iter_prime_basis4II_prime_basis_gtN_(n)][-1] < n]
    #see:_find_minN4II_prime_basis_gtN__not_consider_trial_division_
    # [[n >= 4 < 2*3] -> [[*iter_prime_basis4II_prime_basis_gtN_(n)][-1] < n]]
# ??? [next_prime__ge_(1+[*iter_prime_basis4II_prime_basis_gtN_(n)][-1])**2 <= n]
    #see:_find_minN4II_prime_basis_gtN__consider_trial_division_
    # [[n >= 121 == (11**2) < 2*3*5*7] -> [next_prime__ge_(1+[*iter_prime_basis4II_prime_basis_gtN_(n)][-1])**2 <= n]]
===
[[n >= 4 < 2*3] -> [[*iter_prime_basis4II_prime_basis_gtN_(n)][-1] < n]]
===
[[[n >= 4][len(prime_basis) >= 1][max(prime_basis) == prime_basis[-1] == last == [*iter_prime_basis4II_prime_basis_gtN_(n)][-1]][min(prime_basis) == prime_basis[0] >= 2]] -> [@[b :<- prime_basis] -> [b%n =!= 0]]]
    #condition4CASE____II_prime_basis_gtN:here
===
]]


######################
##delegate used in:view script/搜索冫伪素数牜临近幂方.py
#   !! there are many funcs depends on is_prime__tribool_():next_probable_prime__ge_,prev_may_probable_prime__lt_,iter_probable_primes__between_,...
#   to override it by [case:=delegate]
######################
    #]]]'''#'''
    #def is_prime__tribool_(n, /, *, case=Case4is_prime__tribool_.II_prime_basis_gtN, skip_check=False):
    #def is_prime__tribool_(n, /, *, case:Case4is_prime__tribool_, skip_check=False):
    #def is_prime__tribool_(n, /, *, case:[Case4is_prime__tribool_,tuple], skip_check=False, skip_A014233=False, params4is_strong_probable_prime__basis__with_trial_division_=None):
    #def is_prime__tribool_(n, /, *, case:[Case4is_prime__tribool_,tuple], skip_check=False, skip_A014233=False, delegate=None):
    #
    # xxx is_prime__using_A014233_.upperbound
    #   since trial_division...
    if 0b0001:params = dict(locals())
    ######################
    ##delegate used in:view script/搜索冫伪素数牜临近幂方.py
    #   !! there are many funcs depends on is_prime__tribool_():next_probable_prime__ge_,prev_may_probable_prime__lt_,iter_probable_primes__between_,...
    #   to override it by [case:=delegate]
    ######################
    #if not delegate is None:
    if callable(case):
        delegate = case
        # [delegate => ignore all other kwds]
        return delegate(n)
    ######################
    ######################
    #.if params4is_strong_probable_prime__basis__with_trial_division_:
    #.    # use is_strong_probable_prime__basis__with_trial_division_ instead
    #.    #   since just required whether_SPRP
    #.    (xfilter4continuous_bases4div, bases4SPRP) = params4is_strong_probable_prime__basis__with_trial_division_
    #.    whether_SPRP = is_strong_probable_prime__basis__with_trial_division_(xfilter4continuous_bases4div, bases4SPRP, n)
    #.    return ... if whether_SPRP else False
    ######################
    check_type_is(bool, skip_A014233)
    check_type_is(bool, skip_check)
    C = Case4is_prime__tribool_
    if case is None:
        case = C.II_prime_basis_gtN

    if type(case) is C and skip_A014233:raise TypeError

    if not skip_A014233:
        try:
            return is_prime__using_A014233_(n, skip_check=skip_check)
        except OverflowError__Miller_Rabin_primality_test__A014233:
            #
            pass
        # [[n >= is_prime__using_A014233_.upperbound > A014233[-1] > 2**81][is_strong_probable_prime__basis_(prime_basis4A014233, n) is True]]
            #==>>:
            # [n is odd][n >= 3]

        # [n > 2**81 > 98]
        # [n >= 98]
        # [n is odd][n >= 3]
    else:
        assert not type(case) is C
        check_type_is(int, n)
        if n < 2:
            return False
        if n&1 == 0:
            return n==2
        # [n is odd][n >= 3]
    # [n is odd][n >= 3]
    assert n >= 3
    assert n&1

    if skip_A014233 and not skip_check:
        # trial_division_if_skip_A014233
        #prime_basis4trial_division = prime_gen[n.bit_length()-1]
        prime_basis4trial_division = iter_prime_basis4II_prime_basis_gtN_(n)
        #prime_basis4trial_division = tuple(prime_basis4trial_division)
        r = _prepare4is_prime__tribool_(prime_basis4trial_division, n, skip_check=skip_check, _not_seq=True)

        if not r is ...:
            return r

    # [n is odd][n >= 3]


    # [[not skip_A014233] -> [n >= 98]]
    # [[type(case) is C] -> [n >= 98]]

    ##################
    L = len(prime_basis4A014233)
    C = Case4is_prime__tribool_
    ############
    if case is C.bit_length:
        # ??? [prime_gen[n.bit_length()-1] < n]
            #see:_find_minN4bit_length__not_consider_trial_division_
            # [[n >= 6] -> [prime_gen[n.bit_length()-1] < n]]
        # ??? [prime_gen[n.bit_length()]**2 <= n]
            #see:_find_minN4bit_length__consider_trial_division_
            # [[n >= 1369 == 37**2 == prime_gen[11]**2] -> [prime_gen[n.bit_length()]**2 <= n]]


        assert not skip_A014233
        assert n >= 6
        assert n >= 1369
        # [[[n >= 6][len(prime_basis) >= 1][last := prime_gen[n.bit_length()-1]][max(prime_basis) == prime_basis[-1] == last][min(prime_basis) == prime_basis[0] >= 2]] -> [@[b :<- prime_basis] -> [b%n =!= 0]]]
            #condition4CASE____bit_length:goto

        sz = n.bit_length()
        if not L < sz:
            basis_ls = []
            # [@[b :<- chain(prime_basis4A014233, *basis_ls)] -> [b%n =!= 0]]
        else:
            #.prime_basis = prime_gen[L:sz]
            prime_basis = tuple(iter_all_strict_sorted_primes_(size=sz))[L:]
                # exclude prime_basis4A014233
            # [len(prime_basis) == sz-L >= 1]
            # [len(prime_basis) >= 1]
            # [min(prime_basis) == prime_gen[L] >= 2]
            # [max(prime_basis) == prime_gen[sz-1] <= prime_gen[n.bit_length()-1]]
            # !! condition4CASE____bit_length:goto
            # [@[b :<- prime_basis4A014233++prime_basis] -> [b%n =!= 0]]
            basis_ls = [prime_basis]
            # [@[b :<- chain(prime_basis4A014233, *basis_ls)] -> [b%n =!= 0]]
        basis_ls

    ############
    elif case is C.ERH:
        # ??? [2* n.bit_length()**2 <= n]
            #see:_find_minN4ERH__not_consider_trial_division_
            # [[n >= 98 == 2* 7**2] -> [2* n.bit_length()**2 <= n]]
        # ??? [(2* n.bit_length()**2)**2 <= n]
            #see:_find_minN4ERH__consider_trial_division_
            # [[n >= 640000 == ((2* 20**2)**2)] -> [(2* n.bit_length()**2)**2 <= n]]

        #bug:#assert n >= 1048577 #see:_find_min4ERH_
        #bug:assert n.bit_length() >= 21 #see:_find_min4ERH_
        assert not skip_A014233
        assert n >= 98
        assert n >= 640000
        # [[[n >= 98][len(prime_basis) >= 1][max(prime_basis) == prime_basis[-1] < end == 2* n.bit_length()**2][min(prime_basis) == prime_basis[0] >= 2]] -> [@[b :<- prime_basis] -> [b%n =!= 0]]]
            #condition4CASE____ERH:goto

        #bug:sz = 2* n.bit_length()**2
        end = 2* n.bit_length()**2
        #bug:prime_basis = (*prime_gen.iter__lt_(end),)
            #NOTE: may have [min_witness_base < min_prime_witness]

        #.ps = prime_gen.iter__lt_(end)
        ps = iter_all_strict_sorted_primes_(end=end)
        _ps = islice(ps, L, None)
            # exclude prime_basis4A014233
        # !! condition4CASE____ERH:goto
        # [@[b :<- range(2,end)] -> [b%n =!= 0]]
        s = []
        def _iter0(s, _ps, /):
            for p in _ps:
                yield p
                s.append(p)
        def _iter1(s, _ps, /):
            [] = _ps
            ps = {*prime_basis4A014233, *s}
            for b in range(2, end):
                if b not in ps:
                    yield b
        if n&3 == 3:
            # [n%4 == 3]
            basis_ls = [_ps]
        else:
            # [n%4 == 1]
            basis_ls = [_iter0(s, _ps), _iter1(s, _ps)]
        basis_ls
        # !! [@[b :<- range(2,end)] -> [b%n =!= 0]]
        # [@[b :<- chain(prime_basis4A014233, *basis_ls)] -> [b%n =!= 0]]
    ############
    elif case is C.II_prime_basis_gtN or case is None:
        # ??? [[*iter_prime_basis4II_prime_basis_gtN_(n)][-1] < n]
            #see:_find_minN4II_prime_basis_gtN__not_consider_trial_division_
            # [[n >= 4 < 2*3] -> [[*iter_prime_basis4II_prime_basis_gtN_(n)][-1] < n]]
        # ??? [next_prime__ge_(1+[*iter_prime_basis4II_prime_basis_gtN_(n)][-1])**2 <= n]
            #see:_find_minN4II_prime_basis_gtN__consider_trial_division_
            # [[n >= 121 == (11**2) < 2*3*5*7] -> [next_prime__ge_(1+[*iter_prime_basis4II_prime_basis_gtN_(n)][-1])**2 <= n]]
        assert not skip_A014233
        assert n >= 4
        assert n >= 121
        # [[[n >= 4][len(prime_basis) >= 1][max(prime_basis) == prime_basis[-1] == last == [*iter_prime_basis4II_prime_basis_gtN_(n)][-1]][min(prime_basis) == prime_basis[0] >= 2]] -> [@[b :<- prime_basis] -> [b%n =!= 0]]]
            #condition4CASE____II_prime_basis_gtN:goto

        prime_basis = islice(iter_prime_basis4II_prime_basis_gtN_(n), L, None)
            # exclude prime_basis4A014233
            #
            # impl____II_prime_basis_gtN:here
            # def____II_prime_basis_gtN:goto
        # !! condition4CASE____II_prime_basis_gtN:goto
        # [@[b :<- prime_basis4A014233++prime_basis] -> [b%n =!= 0]]
        for head in prime_basis:
            assert head > prime_basis4A014233[-1]
            prime_basis = chain([head], prime_basis)
            basis_ls = [prime_basis]
            break
        else:
            basis_ls = []
        # [@[b :<- chain(prime_basis4A014233, *basis_ls)] -> [b%n =!= 0]]
    ############
    elif isinstance(case, _int_seq_types):
        basis = case
        basis_ls = [basis]
    ############
    else:
        raise Exception(f'unknowm Case4is_prime__tribool_:{case}')
    ############
    ##################
    basis_ls
    ##################

    # [@[b :<- chain(prime_basis4A014233, *basis_ls)] -> [b%n =!= 0]]

    #if 0:
    #    if not prime_basis[-1] < n-1: raise logic-err
    #    if not prime_basis[-1]**2 < n: raise logic-err
    #    r = _prepare4is_prime__tribool_(prime_basis, n, skip_check=skip_check)
    #    if not r is ...:
    #        return r
    #    # [n is odd][n >= 3]
    #    # [@[b :<- prime_basis] -> [b%n =!= 0]]




    # [n is odd][n >= 3]
    # [@[b :<- chain(prime_basis4A014233, *basis_ls)] -> [b%n =!= 0]]

    #for basis in basis_ls:
    basis = chain.from_iterable(basis_ls)
    if not skip_A014233:
        # tested hence drop:
        basis = filterfalse(prime_basis_set4A014233.__contains__, basis)
    else:
        is_ok, factor_or_basis = _std_finite_basis_(n, basis)
        if not is_ok:
            return False
        basis = factor_or_basis
    basis
    if 0b0000:
        basis = tuple(basis)
        print_err('is_prime__tribool_', params, basis)
    basis
    if 1:
        # !! [@[b :<- chain(prime_basis4A014233, *basis_ls)] -> [b%n =!= 0]]
        # [@[b :<- basis] -> [b%n =!= 0]]
        if not _kw__is_strong_probable_prime__basis_(basis, n, to_find_sqrt_neg1=False):
            return False
        # [is_strong_probable_prime__basis_(basis, n) is True]
    # [is_strong_probable_prime__basis_(chain(*basis_ls), n) is True]
    # !! [is_strong_probable_prime__basis_(prime_basis4A014233, n) is True]
    # [is_strong_probable_prime__basis_(chain(prime_basis4A014233, *basis_ls), n) is True]
        # hence the above "exclude" prime_basis4A014233 is ok

    # postcondition:
    # [[n >= is_prime__using_A014233_.upperbound > A014233[-1] > 2**81][is_strong_probable_prime__basis_(chain(prime_basis4A014233, *basis_ls), n) is True]]
    return ...
_int_seq_types = (tuple, list, bytes, bytearray)
def _std_finite_basis_(n, basis, /):
    'n -> Iter base -> ((False,factor<n>)|(True,basis/[base/[2..=n-2]{gcd(base,n)==1}]))'
    basis = set(base%n for base in basis)
    # [0 <= base <= n-1]
    basis.discard(0)
    basis.discard(1)
    basis.discard(n-1)
    # [2 <= base <= n-2]
    #if not all(gcd(n, base) == 1 for base in basis): return False
    basis = sorted(basis)
    for base in basis:
        if not gcd(n, base) == 1:
            return (False, base)
    basis = tuple(basis)
    return (True, basis)
def calc_len_prime_basis4II_prime_basis_gtN_(n, /):
    return len([*iter_prime_basis4II_prime_basis_gtN_(n)])
def iter_prime_basis4II_prime_basis_gtN_(n, /):
    '-> Iter prime until II(all output prime) > input'
    #see: II_prime_basis_gtN
    ii = 1
    #.for p in iter(prime_gen):
    for p in iter_all_strict_sorted_primes_():
        yield p
        ii *= p
        if ii > n:
            break

def _find_minN_(_is_ok_, begin=1, /):
    from seed.seq_tools.bisearch import bisearch
    for bit_length in range(1, 500):
        n = 1<<(bit_length-1)
        assert n.bit_length() == bit_length
        if _is_ok_(n):
            break
    else:
        raise 000
    assert _is_ok_(1<<(bit_length -1))
    (eqv_begin, eqv_end) = bisearch(True, range(1<<bit_length), max(begin, 1<<max(0, bit_length-2)), key=_is_ok_)
    if eqv_begin == eqv_end:
        raise 000
    n = eqv_begin
    assert not any(__ := [*map(_is_ok_, __3 := range(__2 := max(begin,n-100), n))]), ((__2, n), __, [*filter(_is_ok_, __3)])
    assert all(__ := [*map(_is_ok_, range(n, n+100))]), (n, __, n+__.index(False), (1<<(bit_length-1), 1<<bit_length))
    return n


    #bug:
    for bit_length in range(1, 500):
        n = (1<<bit_length) -1
        assert n.bit_length() == bit_length
        if _is_ok_(n):
            break
    else:
        raise 000
    assert _is_ok_((1<<bit_length) -1)
    (eqv_begin, eqv_end) = bisearch(True, range(1<<bit_length), 1<<(bit_length-1), key=_is_ok_)
    if eqv_begin == eqv_end:
        raise 000
    n = eqv_begin
    assert not any(__ := [*map(_is_ok_, range(__2 := max(1,n-100), n))]), ((__2, n), __)
    assert all(__ := [*map(_is_ok_, range(n, n+100))]), (n, __, n+__.index(False), (1<<(bit_length-1), 1<<bit_length))
        # ^(961, ..., 1024, (512, 1024)) @_find_minN4bit_length__consider_trial_division_
            #assert [*map(_is_ok_, range(n, n+100))] == [True]*(1024-961) + [False]*(100-(1024-961))
    return n

def __hide__prime_gen():
  if 1:
    prime_gen = ...
  def _is_ok4find_minN4bit_length__not_consider_trial_division_(n, /):
    last = prime_gen[n.bit_length()-1]
    return last < n
  def _find_minN4bit_length__not_consider_trial_division_():
    # ??? [prime_gen[n.bit_length()-1] < n]
    lazy_prime_seq = prime_gen() #turnon weakref
    n = _find_minN_(_is_ok4find_minN4bit_length__not_consider_trial_division_)
    assert n == 6, n
    # [[n >= 6] -> [prime_gen[n.bit_length()-1] < n]]
    return n
  def _is_ok4find_minN4bit_length__consider_trial_division_(n, /):
    next_prime_factor = prime_gen[n.bit_length()]
    return next_prime_factor**2 <= n
  def _find_minN4bit_length__consider_trial_division_():
    # ??? [prime_gen[n.bit_length()]**2 <= n]
    #return ...
    lazy_prime_seq = prime_gen() #turnon weakref
    assert _is_ok4find_minN4bit_length__consider_trial_division_(961)
    assert _is_ok4find_minN4bit_length__consider_trial_division_(1369)
    assert not _is_ok4find_minN4bit_length__consider_trial_division_(961 -1)
    assert not _is_ok4find_minN4bit_length__consider_trial_division_(1369 -1)
    n = _find_minN_(_is_ok4find_minN4bit_length__consider_trial_division_)
    assert n == 1369 == 37**2, n
    # [[n >= 1369 == 37**2 == prime_gen[11]**2] -> [prime_gen[n.bit_length()]**2 <= n]]
    return n

    assert n == 961 == 31**2, n
    assert n == 131079601 == 11449**2, n
    assert 11449 == prime_gen[27], prime_gen[26:30]
    assert prime_gen[28]**2 < 1<<27
    return n
    r'''[[[

min is 961, but 1024...
>>> 31**2
961
>>> 961 .bit_length()
10
>>> prime_gen[10]
31
>>> 1024 .bit_length()
11
>>> prime_gen[11]
37
>>> 37**2
1369
>>> 1369 .bit_length()
11
>>> 2048 .bit_length()
12
>>> prime_gen[12]
41
>>> 41**2
1681


#err:wrong-condition: [next_prime_factor**4 <= n]
>>> 11449**2
131079601
>>> 131079601 .bit_length()
27
>>> prime_gen[27]
107
>>> 107**2
11449
>>> 107**4
131079601

    #]]]'''#'''
  if 1:
    return (_find_minN4bit_length__not_consider_trial_division_, _find_minN4bit_length__consider_trial_division_)
#end-def __hide__prime_gen():
if 1:
    (_find_minN4bit_length__not_consider_trial_division_, _find_minN4bit_length__consider_trial_division_) = __hide__prime_gen()

def _is_ok4find_minN4ERH__not_consider_trial_division_(n, /):
    end = 2* n.bit_length()**2
    return end <= n
def _find_minN4ERH__not_consider_trial_division_():
    # ??? [2* n.bit_length()**2 <= n]
    n = _find_minN_(_is_ok4find_minN4ERH__not_consider_trial_division_)
    assert n == 98, n
    # [[n >= 98 == 2* 7**2] -> [2* n.bit_length()**2 <= n]]
    return n
    r'''[[[
>>> 98 .bit_length()
7
>>> 7**2
49
>>> 2* 7**2
98

    #]]]'''#'''
    for n in range(1, 1000):
        if _is_ok4find_minN4ERH__not_consider_trial_division_(n):
            break
    else:
        raise 000
    assert all(map(_is_ok4find_minN4ERH__not_consider_trial_division_, range(n, 5*n)))
    assert n == 98, n
    return n
def _is_ok4find_minN4ERH__consider_trial_division_(n, /):
    end = 2* n.bit_length()**2
    return end**2 <= n
def _find_minN4ERH__consider_trial_division_():
    # ??? [(2* n.bit_length()**2)**2 <= n]
    assert _is_ok4find_minN4ERH__consider_trial_division_(521284)
    assert _is_ok4find_minN4ERH__consider_trial_division_(640000)
    assert not _is_ok4find_minN4ERH__consider_trial_division_(521284 -1)
    assert not _is_ok4find_minN4ERH__consider_trial_division_(640000 -1)
    n = _find_minN_(_is_ok4find_minN4ERH__consider_trial_division_)
    assert n == 640000 == ((2* 20**2)**2), n
    # [[n >= 640000 == ((2* 20**2)**2)] -> [(2* n.bit_length()**2)**2 <= n]]
    return n

    n = ((2* 20**2)**2)
    return n
    assert n == 521284, n
    assert n == 640000, n
    return n
    r'''[[[
>>> 640000 .bit_length()
20
>>> 800**2
640000
>>> 2* 20**2
800
>>> (2* 20**2)**2
640000

>>> 521284 .bit_length()
19
>>> (2* 19**2)**2
521284

>>> (2* 18**2)**2
419904
>>> ((2* 18**2)**2) .bit_length()
19
>>> ((2* 19**2)**2) .bit_length()
19
>>> ((2* 20**2)**2) .bit_length()
20
>>> ((2* 21**2)**2) .bit_length()
20
>>> ((2* 22**2)**2) .bit_length()
20
>>> ((2* 23**2)**2) .bit_length()
21

    #]]]'''#'''
    from seed.seq_tools.bisearch import bisearch
    #len(range(2**80))
        # OverflowError: Python int too large to convert to C ssize_t
        # e ../lots/NOTE/Python/python-bug/len-bug.txt
        #
    (eqv_begin, eqv_end) = bisearch(True, range(2**80), 1, key=_is_ok4find_minN4ERH__consider_trial_division_)
    if eqv_begin == eqv_end:
        raise 000
    n = eqv_begin
    assert not any(map(_is_ok4find_minN4ERH__consider_trial_division_, range(n-100, n)))
    assert all(map(_is_ok4find_minN4ERH__consider_trial_division_, range(n, n+100)))
    assert n == 640000, n
    return n

    #fail:
    n0 = 98**2
    for n in range(n0, n0+1000):
        if _is_ok4find_minN4ERH__consider_trial_division_(n):
            break
    else:
        raise 000
    assert all(map(_is_ok4find_minN4ERH__consider_trial_division_, range(n, n+100)))
    assert n == 98, n
    return n

def _is_ok4find_minN4II_prime_basis_gtN__not_consider_trial_division_(n, /):
    last = [*iter_prime_basis4II_prime_basis_gtN_(n)][-1]
    return last < n
def _find_minN4II_prime_basis_gtN__not_consider_trial_division_():
    # ??? [[*iter_prime_basis4II_prime_basis_gtN_(n)][-1] < n]
    n = _find_minN_(_is_ok4find_minN4II_prime_basis_gtN__not_consider_trial_division_)
    assert n == 4 < 2*3
    # [[n >= 4 < 2*3] -> [[*iter_prime_basis4II_prime_basis_gtN_(n)][-1] < n]]
    return n

def _is_ok4find_minN4II_prime_basis_gtN__consider_trial_division_(n, /):
    last = [*iter_prime_basis4II_prime_basis_gtN_(n)][-1]
    next_prime_factor = next_may_prime__le_pow2_81__ge_(1+last)
    return next_prime_factor**2 <= n
def _find_minN4II_prime_basis_gtN__consider_trial_division_():
    # ??? [next_prime__ge_(1+[*iter_prime_basis4II_prime_basis_gtN_(n)][-1])**2 <= n]
    n = _find_minN_(_is_ok4find_minN4II_prime_basis_gtN__consider_trial_division_, 1)
    assert n == 121 == (11**2) < 2*3*5*7, n
    # [[n >= 121 == (11**2) < 2*3*5*7] -> [next_prime__ge_(1+[*iter_prime_basis4II_prime_basis_gtN_(n)][-1])**2 <= n]]
    return n


def __():
    #bug: prime_gen.iter__lt_(end) --> range(2, end)
    _iter__lt_ = ...
    prime_gen = ...
    def _check_min4ERH_(lazy_prime_seq, e, n, /):
        assert n == 2**(e-1)+1
        assert n.bit_length() == e
            # == ceil_log2(n)
        assert 2**(e-1) < n < 2**e
        for e_ in range(e, e+100):
            assert _is_ok4ERH_(lazy_prime_seq, e_)
        for _e in range(2,e):
            assert not _is_ok4ERH_(lazy_prime_seq, _e)
    def _is_ok4ERH_(lazy_prime_seq, e, /):
        n = 2**(e-1)+1
        assert n.bit_length() == e
        #bug:
            #sz = 2* n.bit_length()**2
            #prime_basis = lazy_prime_seq[:sz]
        end = 2* n.bit_length()**2
        prime_basis = [*_iter__lt_(end, lazy_prime_seq)]
        p = prime_basis[-1]
        return p < n-1 and p**2 < n
    def _find_min4ERH_():
        lazy_prime_seq = prime_gen.get_or_mk_lazy_prime_seq_()
        for e in _count(2):
            if _is_ok4ERH_(lazy_prime_seq, e):
                break
        n = 2**(e-1)+1
        _check_min4ERH_(lazy_prime_seq, e, n)
        assert (n, e) == (1048577, 21), (n, e)
        return (n, e)
def _find_mismatch4diff_cases4is_prime__tribool_():
    # view ../../python3_src/nn_ns/math_nn/numbers/Mersenne_exponents.py
    from nn_ns.math_nn.numbers.Mersenne_exponents import Mersenne_exponents, Mersenne_exponents__stable, Mersenne_exponents__unstable
    from nn_ns.math_nn.numbers.Mersenne_exponents import known_Mersenne_exponent_set, is_known_Mersenne_exponent, is_Mersenne_exponent__Lucas_Lehmer_test
    max_p = Mersenne_exponents__stable[-1]
    print(f'max_p = {max_p}; max_p.bit_length() = {max_p.bit_length()}')
    C = Case4is_prime__tribool_
    #for p in prime_gen:
    #.for p in prime_gen.iter__lt_(max_p+1):
    for p in iter_all_strict_sorted_primes_(end=1+max_p):
        print(f'2**{p}-1')
        mn = (1<<p)-1

        r2 = is_prime__tribool_(mn, case=C.II_prime_basis_gtN)
        if not r2 is ...:
            assert r2 is is_known_Mersenne_exponent(p)
            continue
        else:
            if not is_known_Mersenne_exponent(p):
                print(f'II_prime_basis_gtN fail: 2**{p}-1')
                pass
            else:
                continue


        r0 = is_prime__tribool_(mn, case=C.bit_length)
        if not r0 is ...:
            assert r0 is is_known_Mersenne_exponent(p)
            continue
        else:
            if not is_known_Mersenne_exponent(p):
                print(f'bit_length fail: 2**{p}-1')
                pass
            else:
                continue

        r1 = is_prime__tribool_(mn, case=C.ERH)
        if not r0 is r1:
            print(f'mismatch: 2**{p}-1: {r0} vs {r1}')
        if not r1 is ...:
            assert r1 is is_known_Mersenne_exponent(p)
        else:
            if not is_known_Mersenne_exponent(p):
                print(f'ERH err: 2**{p}-1')

if 0b0000:
    assert len(A014233) == 13
    #ceil(ceil_log2(A014233[i])/(i+1)) = 11,11,9,8,9,7,7,7,7,7,6,7,7
    assert (__ := [(max1.bit_length() +i) //(i+1) for i, max1 in enumerate(A014233)]) == [11,11,9,8,9,7,7,7,7,7,6,7,7], __

    #ceil(floor_log2(A014233[i])/(i+1)) = 10,10,8,8,8,7,7,6,7,7,6,7,7
    assert (__ := [(max1.bit_length()-1 +i) //(i+1) for i, max1 in enumerate(A014233)]) == [10,10,8,8,8,7,7,6,7,7,6,7,7], __

    #floor(floor_log2(A014233[i])/(i+1)) = 10,10,8,7,8,6,6,6,6,6,5,6,6
    assert (__ := [(max1.bit_length()-1) //(i+1) for i, max1 in enumerate(A014233)]) == [10,10,8,7,8,6,6,6,6,6,5,6,6], __

    #floor(calc_len_prime_basis4II_prime_basis_gtN_(A014233[i])/(i+1)) = ?
    assert (__ := [calc_len_prime_basis4II_prime_basis_gtN_(max1) //(i+1) for i, max1 in enumerate(A014233)]) == [5, 4, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1], __
        # II_prime_basis_gtN___vs___A014233:here
        # def____II_prime_basis_gtN:goto
        # II_prime_basis_gtN
        # [:next_probable_prime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    calc_len_prime_basis4II_prime_basis_gtN_









#def raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_(end, /, *, is_prime_and_may_upperbound=(is_prime__le_pow2_64, 2**64)):
    # replaced since 2**64 < A014233[-1]
assert A014233[-1] > 2**81
is_prime__le_pow2_81_ = is_prime__using_A014233_
default4is_prime_and_may_upperbound = (is_prime__using_A014233_, is_prime__using_A014233_.upperbound)
def raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_(begin, /, *, is_prime_and_may_upperbound=default4is_prime_and_may_upperbound):
    'using Miller_Rabin_primality_test: begin -> (Iter prime){[[prev first prime < begin][fist prime >= begin]]}'
    check_type_is(int, begin)

    (is_prime_, may_upperbound) = is_prime_and_may_upperbound
    if not may_upperbound is None:
        upperbound = may_upperbound
        ints = range(begin, upperbound)
    else:
        ints = _count(begin)
    return prime_filter__using_primality_test_(ints, is_prime_and_may_upperbound=is_prime_and_may_upperbound)
def raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_(end, /, *, is_prime_and_may_upperbound=default4is_prime_and_may_upperbound, reverse=False):
    'using Miller_Rabin_primality_test: end -> (Iter prime){[[last prime < end][next prime >= end]]} #see:raw_iter_all_strict_sorted_primes__lt_<Eratosthenes_sieve>'
    check_type_is(int, end)

    (is_prime_, may_upperbound) = is_prime_and_may_upperbound
    if not may_upperbound is None:
        upperbound = may_upperbound
        if upperbound < end:
            raise OverflowError__Miller_Rabin_primality_test__A014233(f'[{upperbound} == upperbound < end == {end}]')
    ints = range(2, end)
    if reverse:
        ints = reversed(ints)
    return prime_filter__using_primality_test_(ints, is_prime_and_may_upperbound=is_prime_and_may_upperbound)
    return filter(is_prime_, range(2, end))


def prev_may_probable_prime__lt_(end, /, **kwds):
    # @20250130: ++kw:case@prev_may_probable_prime__lt_
    'using Miller_Rabin_primality_test: end -> (may probable_prime){[[probable_prime < end][next probable_prime >= end]]} #see:prev_may_prime__le_pow2_81__lt_'
    # [:next_probable_prime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    kwds.setdefault('case', None)
    for n in reversed(range(3, end|1, 2)):
        r = is_prime__tribool_(n, **kwds)
        if not r is False:
            probable_prime = n
            return probable_prime
            break
    else:
        assert end <= 3, (end, kwds)
        if 2 < end:
            return 2
    return None

def next_probable_prime__ge_(begin, /, **kwds):
    # @20250130: ++kw:case@next_probable_prime__ge_
    'using Miller_Rabin_primality_test: begin -> (probable_prime){[[prev probable_prime < begin][probable_prime >= begin]]} #see:next_may_prime__le_pow2_81__ge_' \
    r'''

!! II_prime_basis_gtN___vs___A014233:goto
=> [II_prime_basis_gtN `better_than` A014233[:13]]
=> [II_prime_basis_gtN `better_than` __le_pow2_81]
=> [next_probable_prime__ge_ `better_than` next_may_prime__le_pow2_81__ge_]
=> [[n <= 2**81] -> [next_probable_prime__ge_(n) == next_may_prime__le_pow2_81__ge_(n)]]
    [:next_probable_prime__ge___vs__next_may_prime__le_pow2_81__ge_]:here
'''#'''
    kwds.setdefault('case', None)
    begin = max(2, begin)
    if begin == 2:
        return 2
    for n in _count(begin|1, 2):
        r = is_prime__tribool_(n, **kwds)
        if not r is False:
            break
    probable_prime = n
    return probable_prime
def next_may_prime__le_pow2_81__ge_(begin, /, *, is_prime_and_may_upperbound=default4is_prime_and_may_upperbound):
    'using Miller_Rabin_primality_test: begin -> (may prime){[[prev prime < begin][prime >= begin]]} #see:next_probable_prime__ge_'
    # [:next_probable_prime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    it = raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_(begin, is_prime_and_may_upperbound=is_prime_and_may_upperbound)
    return _next__may_head_(it)
def _next__may_head_(it, /):
    for head in it:
        return head
    return None
def prev_may_prime__le_pow2_81__lt_(end, /, *, is_prime_and_may_upperbound=default4is_prime_and_may_upperbound):
    'using Miller_Rabin_primality_test: end -> (may prime){[[prime < end][next prime >= end]]} #see:prev_may_probable_prime__lt_'
    # [:next_probable_prime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    it = raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_(end, is_prime_and_may_upperbound=is_prime_and_may_upperbound, reverse=True)
    return _next__may_head_(it)
def _iter_xs_ge_(next_may_x__ge_, begin, /, **kwds):
    while 1:
        m = next_may_x__ge_(begin, **kwds)
        if m is None:break
        x = m
        yield x
        begin = x+1
def _reversed_iter_xs_lt_(prev_may_x__lt_, end, /, **kwds):
    while 1:
        m = prev_may_x__lt_(end, **kwds)
        if m is None:break
        x = m
        yield x
        #bug:end = x-1
        end = x
def iter_primes__ge_lt_(begin, may_end, /, *, reverse=False):
    #iter_primes__le_pow2_81__ge_
    #reversed_iter_primes__le_pow2_81__lt_
    #is_prime__le_pow2_81_
    delegate, max_end = default4is_prime_and_may_upperbound
    assert delegate is is_prime__le_pow2_81_
    if may_end is None:
        may_end = max_end
    else:
        end = may_end
        check_type_is(int, end)
        may_end = min(max_end, end)
    return iter_probable_primes__ge_lt_(begin, may_end, reverse=reverse, case=is_prime__le_pow2_81_)
iter_primes__between_ = iter_primes__ge_lt_
def iter_primes__inside_(ints, /, **kwds):
    it = filter(2 .__le__, ints)
    return _iter_primes__inside_(it, **kwds)
def _iter_primes__inside_(uints, /, **kwds):
    kwds.setdefault('case', None)
    for n in uints:
        r = is_prime__tribool_(n, **kwds)
        if r is True:
            prime = n
            yield prime
        elif r is False:
            composite = n
            pass
        elif r is ...:
            raise PrimalityUndeterminedError(n)
        else:
            raise 000
    return

def iter_probable_primes__ge_lt_(begin, may_end, /, *, reverse=False, **kwds):
    # @20250130: ++kw:case@next_probable_prime__ge___vs__next_may_prime__le_pow2_81__ge_&prev_may_probable_prime__lt_
    check_type_is(bool, reverse)
    check_type_is(int, begin)
    begin = max(2, begin)
    if may_end is None:
        if reverse:raise TypeError('reverse but [end := +oo]')
        _end = 3
        odds = _count(begin|1, 2)
    else:
        end = may_end
        check_type_is(int, end)
        _end = end
        odds = range(begin|1, end, 2)
        if reverse:
            odds = reversed(odds)
        odds
    odds
    _end
    _has2 = (begin == 2 < _end)
    even_primes = [2][:_has2]
    odd_primes = _iter_probable_primes__inside_(odds, **kwds)
    primess = (even_primes, odd_primes)
    if reverse:
        primess = reversed(primess)
    primess
    return chain(*primess)
def _iter_probable_primes__inside_(uints, /, **kwds):
    kwds.setdefault('case', None)
    for n in uints:
        r = is_prime__tribool_(n, **kwds)
        if not r is False:
            probable_prime = n
            yield probable_prime
    return
def iter_probable_primes__inside_(ints, /, **kwds):
    it = filter(2 .__le__, ints)
    return _iter_probable_primes__inside_(it, **kwds)
iter_probable_primes__inside_
iter_probable_primes__ge_lt_
iter_probable_primes__between_ = iter_probable_primes__ge_lt_
def iter_probable_primes__ge_(begin, /, **kwds):
    # @20250130: ++kw:case@next_probable_prime__ge___vs__next_may_prime__le_pow2_81__ge_&prev_may_probable_prime__lt_
    # [:next_probable_prime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    return _iter_xs_ge_(next_probable_prime__ge_, begin, **kwds)
def reversed_iter_probable_primes__lt_(end, /, **kwds):
    # @20250130: ++kw:case@next_probable_prime__ge___vs__next_may_prime__le_pow2_81__ge_&prev_may_probable_prime__lt_
    # [:next_probable_prime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    return _reversed_iter_xs_lt_(prev_may_probable_prime__lt_, end, **kwds)
def iter_primes__le_pow2_81__ge_(begin, /):
    # [:next_probable_prime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    return _iter_xs_ge_(next_may_prime__le_pow2_81__ge_, begin)
iter_primes__le_pow2_81__ge_ = raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_
def reversed_iter_primes__le_pow2_81__lt_(end, /):
    # [:next_probable_prime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    return raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_(end, reverse=True)
    return _reversed_iter_xs_lt_(prev_may_prime__le_pow2_81__lt_, end)
#bug:reversed_iter_primes__le_pow2_81__lt_ = raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_

def pairwise_diff_(xs, /):
    xs = iter(xs)
    for a, b in pairwise(xs):
        yield b-a
def iter_pairwise_diff_probable_primes__ge_(begin, /):
    # [:next_probable_prime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    return pairwise_diff_(iter_probable_primes__ge_(begin))
def iter_pairwise_diff_primes__le_pow2_81__ge_(begin, /):
    # [:next_probable_prime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    return pairwise_diff_(iter_primes__le_pow2_81__ge_(begin))

def prime_filter__using_primality_test_(ints, /, *, is_prime_and_may_upperbound=default4is_prime_and_may_upperbound):
    'using Miller_Rabin_primality_test: Iter int -> Iter prime'
    (is_prime_, may_upperbound) = is_prime_and_may_upperbound
    return filter(is_prime_, ints)
if 0:
    def raw_iter_primes__using_primality_test__inside_(ints, /, *, is_prime_and_may_upperbound=default4is_prime_and_may_upperbound):
        'using Miller_Rabin_primality_test: Iter int -> Iter prime'
        (is_prime_, may_upperbound) = is_prime_and_may_upperbound
        return filter(is_prime_, ints)

if 0:
    print(_find_minN4bit_length__not_consider_trial_division_())
    print(_find_minN4bit_length__consider_trial_division_())
    print(_find_minN4ERH__not_consider_trial_division_())
    print(_find_minN4ERH__consider_trial_division_())
    print(_find_minN4II_prime_basis_gtN__not_consider_trial_division_())
    print(_find_minN4II_prime_basis_gtN__consider_trial_division_())
    r'''[[[
6
1369
98
640000
4
121

    #]]]'''#'''






















r'''[[[

%s/\<is_pseudoprime\>/whether_sprp/g
%s/\<next_pseudoprime__ge___vs__next_may_prime__le_pow2_81__ge_\>/next_probable_prime__ge___vs__next_may_prime__le_pow2_81__ge_/g
%s/\<backward_compatible_for_renaming_pseudoprime_as_pseudoprime\>/backward_compatible_for_renaming_pseudoprime_as_probable_prime/g

.,$s/.* \(\w\+\) *= *\(\w\+\)\>.*/%s\/\\\<\1\\\>\/\2\/g
==>>:
%s/\<is_strong_pseudoprime_\>/is_strong_probable_prime_/g
%s/\<is_strong_pseudoprime__basis__with_trial_division_\>/is_strong_probable_prime__basis__with_trial_division_/g
%s/\<is_strong_pseudoprime__basis_\>/is_strong_probable_prime__basis_/g
%s/\<_kw__is_strong_pseudoprime__basis_\>/_kw__is_strong_probable_prime__basis_/g
%s/\<_is_strong_pseudoprime_\>/_is_strong_probable_prime_/g
%s/\<detect_strong_pseudoprime__not_waste_too_much_time_\>/detect_strong_probable_prime__not_waste_too_much_time_/g
%s/\<prev_may_pseudoprime__lt_\>/prev_may_probable_prime__lt_/g
%s/\<next_pseudoprime__ge_\>/next_probable_prime__ge_/g
%s/\<iter_pseudoprimes__ge_lt_\>/iter_probable_primes__ge_lt_/g
%s/\<_iter_pseudoprimes__inside_\>/_iter_probable_primes__inside_/g
%s/\<iter_pseudoprimes__inside_\>/iter_probable_primes__inside_/g
%s/\<iter_pseudoprimes__between_\>/iter_probable_primes__between_/g
%s/\<iter_pseudoprimes__ge_\>/iter_probable_primes__ge_/g
%s/\<reversed_iter_pseudoprimes__lt_\>/reversed_iter_probable_primes__lt_/g
%s/\<iter_pairwise_diff_pseudoprimes__ge_\>/iter_pairwise_diff_probable_primes__ge_/g


#]]]'''#'''

__all__
from seed.math.primality_test.strong_probable_prime import (
Error
,   IsPrimeError
,   PrimalityUndeterminedError
,       OverflowError__Miller_Rabin_primality_test__A014233
#
#
#
#
#
#
#
,A014233     ,n2upperbound4Miller_Rabin_primality_test_using_first_n_plus1_primes_as_basis
,   prime_basis4A014233
,   prime_basis_set4A014233
#
,is_prime__using_A014233_    ,is_prime__le_pow2_81_
,   OverflowError__Miller_Rabin_primality_test__A014233
#
#
#
#
#
#
#
,is_strong_probable_prime__basis__with_trial_division_
,   is_strong_probable_prime__basis_
,       is_strong_probable_prime_
#
,   continuous_trial_division_
,       iter_continuous_prime_bases_
,       callable5xfilter4continuous_bases
,       mk_initial_state4filter4continuous_bases_
,       mk_filter4continuous_bases4fixed_size
,       filter4continuous_bases4empty
,       filter4continuous_bases4II_prime_basis_gtN
#
#
#
#
#
#
#
,find_min_prime_witness4odd_composite_
,   iter_until_found_min_prime_witness4odd_composite_
,       IsPrimeError
#
#
#
#
#
,is_prime__tribool_
,   mk_tribool_delegate5PRP_test_
#
,   detect_strong_probable_prime__not_waste_too_much_time_
#
,   Case4is_prime__tribool_
,       iter_prime_basis4II_prime_basis_gtN_
,           calc_len_prime_basis4II_prime_basis_gtN_
#
,   prev_may_probable_prime__lt_
,   next_probable_prime__ge_
,   iter_probable_primes__inside_
,   iter_probable_primes__ge_lt_
,       iter_probable_primes__between_
,   iter_probable_primes__ge_
,   reversed_iter_probable_primes__lt_
#
#
#
#
#
#
#
#
#
#
,prime_filter__using_primality_test_
,   default4is_prime_and_may_upperbound
,       is_prime__le_pow2_81_
,           OverflowError__Miller_Rabin_primality_test__A014233
,           next_may_prime__le_pow2_81__ge_
,           prev_may_prime__le_pow2_81__lt_
,           iter_primes__inside_
,               PrimalityUndeterminedError
,           iter_primes__ge_lt_
,               iter_primes__between_
,           iter_primes__le_pow2_81__ge_
,           reversed_iter_primes__le_pow2_81__lt_
,               raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_
,               raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_
#
#
#
#
#
#
#
#
,pairwise_diff_
,   iter_pairwise_diff_probable_primes__ge_
,   iter_pairwise_diff_primes__le_pow2_81__ge_
#
)


from seed.math.primality_test.strong_probable_prime import *
