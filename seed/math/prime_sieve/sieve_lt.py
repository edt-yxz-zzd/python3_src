#__all__:goto
#@20260510:++优化冫复用小对象
r'''[[[
e ../../python3_src/seed/math/prime_sieve/sieve_lt.py

seed.math.prime_sieve.sieve_lt
py -m nn_ns.app.debug_cmd   seed.math.prime_sieve.sieve_lt -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.prime_sieve.sieve_lt:__doc__ -ht # -ff -df
#######

[[
move_from:
e ../../python3_src/seed/math/prime_gens.py
]]


'#'; __doc__ = r'#'

py_adhoc_call   seed.math.prime_sieve.sieve_lt   @f
]]]'''#'''
__all__ = r'''
list_primes__len_ge_
list_primes__lt_    list_all_strict_sorted_primes__lt_
    sieve4uint2is_prime__lt_
iter_all_strict_sorted_primes_
raw_list_all_strict_sorted_primes__lt_
    raw_iter_all_strict_sorted_primes__lt_
        raw_iter_all_strict_sorted_primes_
            raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_
                raw_list_all_strict_sorted_ints__ge2__with_min_prime_factor__sized_







check_offsetted_uint2may_prime_factors_
    check_offsetted_uint2prime_factors_
    check_uint2may_prime_factors_

check_offsetted_uint2may_pairs8prime_factorization_
    check_offsetted_uint2pairs8prime_factorization_
    check_uint2may_pairs8prime_factorization_

check_offsetted_uint2may_prime_factorization_
    check_offsetted_uint2prime_factorization_
    check_uint2may_prime_factorization_




tabulate_may_min_prime_factor4uint_lt_
TabulateMinPrimeFactor
    iter_find_best_wheel_paramss4sieve_lt_
    find_best_wheel_params4sieve_lt_



tabulate_may_all_prime_factors4uint_lt_
    tabulate_may_all_prime_factor_lflnkls4uint_lt_
    extract_prime_factorization5uint2may_all_prime_factor_lflnkls_


tabulate_may_pairs8prime_factorization4uint_lt_
    tabulate_may_prime_factorization4uint_lt_
                                                tabulate_may_factorization4uint_lt_
'''.split()#'''
    #deprecated:tabulate_may_factorization4uint_lt_
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__, 'count:_count,repeat:_repeat'):
    from itertools import count as _count, repeat as _repeat
    from itertools import islice, pairwise
    from math import isqrt as floor_sqrt
    from bisect import bisect_left


    from seed.tiny_.funcs import echo
    from seed.helper.ifNone import ifNonef
    from seed.tiny_.check import check_type_is, check_int_ge, check_uint_lt, check_int_ge_lt, check_callable
    from seed.iters.apply_may_args4islice_ import list_islice_
    from seed.iters.is_sorted import is_strict_sorted
    from seed.math.II import II
    from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
    from seed.math.semi_factor_pint_via_trial_division import complete_factor_pint_via_trial_division__lflnkls_
    from seed.math.semi_factor_pint_via_trial_division import complete_factor_pint_via_trial_division
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_


    from seed.math.prime_pint.bounds4kth_prime import estimate_upper_bound4Kth_prime_
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def list_primes__len_ge_(min_sz, /, *, _mk=tuple):
    check_int_ge(0, min_sz)
    min_n = min_sz
    min_k = max(0, -1+min_n)
    max_pk = estimate_upper_bound4Kth_prime_(min_k)
    ps = list_primes__lt_(1+max_pk, _mk=_mk)
    assert len(ps) >= min_sz
    return ps


#def _iter_all_strict_sorted_primes():
def iter_all_strict_sorted_primes_(*, size=None, end=None, may_primes=None):
    'using Eratosthenes_sieve: -> Iter prime'
    #to_replace:iter(prime_gen)
    #vs:raw_iter_all_strict_sorted_primes_
    #vs:list_all_strict_sorted_primes__lt_
    it = raw_iter_all_strict_sorted_primes_(to_cache_only_busy_primes_plus_next=may_primes is None, may_primes=may_primes)
    if not None is end:
        it = _iter__lt_(end, it)
    if not None is size:
        it = islice(it, 0, size)
    return it

def raw_iter_all_strict_sorted_primes__lt_(end, /, *, to_cache_only_busy_primes_plus_next, may_primes):
    'using Eratosthenes_sieve: end -> (Iter prime){[[last prime < end][next prime >= end]]} #see:raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_'
    '-> (Iter prime){[[last prime < end][next prime >= end]]}'
    it = raw_iter_all_strict_sorted_primes_(to_cache_only_busy_primes_plus_next=to_cache_only_busy_primes_plus_next, may_primes=may_primes)
    return _iter__lt_(end, it)
def _iter__lt_(end, xs, /):
    xs = iter(xs) #hold iterator only #eg drop LazySeq, hold LazyList tail
    for p in xs:
        if not p < end:
            break
        yield p
def raw_list_all_strict_sorted_primes__lt_(end, /, *, to_cache_only_busy_primes_plus_next, may_primes):
    'using Eratosthenes_sieve: -> [prime]{[[last prime < end][next prime >= end]]} #see:raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_ #see:list_all_strict_sorted_primes__lt_'
    return [*raw_iter_all_strict_sorted_primes__lt_(end, to_cache_only_busy_primes_plus_next=to_cache_only_busy_primes_plus_next, may_primes=may_primes)]
def list_all_strict_sorted_primes__lt_(end, /, *, _mk=tuple):
    'using Eratosthenes_sieve: -> [prime]{[[last prime < end][next prime >= end]]} #see:raw_list_all_strict_sorted_primes__lt_'
    u2b = sieve4uint2is_prime__lt_(end, _mk=list)
    return _mk(u for u, b in enumerate(u2b) if b)
    #if _mk is list: _mk = echo
    #it = _iter_all_strict_sorted_primes__lt_(end)
    #return _mk(it)
list_primes__lt_ = list_all_strict_sorted_primes__lt_
def sieve4uint2is_prime__lt_(end, /, *, _mk=tuple):
    'end/uint -> uint2is_prime/[is_prime/bool]{len==end} # [uint2is_prime == [is_prime_(u) | [u:<-[0..<end]]]]'
    #core_sieve4offsetted_uint2is_prime__ge_le
    #def _iter_all_strict_sorted_primes__lt_(end, may_output_u2b_=None, /):
    #end = __index__(end)
    check_int_ge(0, end)
    if _mk is list: _mk = echo
    u2b = [True]*end
    for u in range(0, min(2, end)):
        u2b[u] = False
    #big = False
    for u in range(2, end):
        if u2b[u]:
            p = u
            #yield p
            #if big:continue
            uu = u**2
            if uu >= end:
                #big = True
                #continue
                break
            for v in range(uu, end, p):
                u2b[v] = False
    u2b
    #.if not None is may_output_u2b_:
    #.    output_u2b_ = may_output_u2b_
    #.    output_u2b_(u2b)
    #.    #tmay_u2b.append(u2b)
    return _mk(u2b)


def raw_iter_all_strict_sorted_primes_(*, to_cache_only_busy_primes_plus_next, may_primes):
    'using Eratosthenes_sieve: -> Iter prime'
    ps = raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_(to_cache_only_busy_primes_plus_next=to_cache_only_busy_primes_plus_next, may_primes=may_primes)
    for n, m in ps:
        if n == m:
            p = n
            yield p
def raw_list_all_strict_sorted_ints__ge2__with_min_prime_factor__sized_(sz, /, *, to_cache_only_busy_primes_plus_next, may_primes):
    'using Eratosthenes_sieve: sz -> [(n, min_prime_factor<n>)]{len=sz} # [n >= 2]'
    return list_islice_(sz, raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_(to_cache_only_busy_primes_plus_next=to_cache_only_busy_primes_plus_next, may_primes=may_primes))
def raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_(*, to_cache_only_busy_primes_plus_next, may_primes, ihead2may_itail=None, offsetted_sieve=None, lmay_offset=None, to_export_all_prime_factors=False, may_uint2all_prime_factors_=None):
    'using Eratosthenes_sieve: -> Iter (n, min_prime_factor<n>) if not to_export_all_prime_factors else (n, all_strict_sorted_prime_factors<n>) # [n >= 2]'
    #no max_prime_factor, since use square limit, donot detect p for [i*p | [i :<- [2..<p]]] inside [p..=p**2]
    #       ...can have max_prime_factor, since miss at most one prime that is a prime <- [next_busy_prime..<next_busy_prime**2]
    #
    #the input `may_primes` used as view to outside
    #
    primes = ifNonef(may_primes, list)
    has_u2ps = not None is may_uint2all_prime_factors_
    if has_u2ps:
        u2ps_ = may_uint2all_prime_factors_
        check_callable(u2ps_)


    if len(primes): raise ValueError

    check_type_is(bool, to_cache_only_busy_primes_plus_next)
        # `primes` cache all future busy_primes, that occupies too much memory
        #
    if to_cache_only_busy_primes_plus_next:
        #recur call:
        iter_busy_primes = raw_iter_all_strict_sorted_primes_(may_primes=primes, to_cache_only_busy_primes_plus_next=False)
        #next_busy_prime = next(iter_busy_primes)
        _2 = next(iter_busy_primes)
            # extract&drop 2
        only_busy_primes_plus_next = primes
    else:
        cached_primes = primes

    # [singly_list<idx8prime> === may idx8prime]
    #idx2may_idx = []
    ihead2may_itail = ifNonef(ihead2may_itail, list)
    if len(ihead2may_itail): raise ValueError
        # :: [may idx8prime]
        # [singly_list<idx8prime>]
        # ihead of busy_prime
        # [len_busy_primes == len(ihead2may_itail)]

    lmay_offset = ifNonef(lmay_offset, list)
    if len(lmay_offset): raise ValueError
    #offset = 2 = first_prime
    lmay_offset.append(2)

    offsetted_sieve = ifNonef(offsetted_sieve, list)
    if len(offsetted_sieve): raise ValueError
        # :: [may idx8prime]
        # :: [may ihead]
        # :: [singly_list<idx8prime>]
        # :: [singly_list<idx8prime_factor>]
    def main():
        # ihead =[def]= idx8prime__singly_list
        # iheads =[def]= idx8prime__list
        # busy_primes =[def]= primes[:len(ihead2may_itail)] that curr used to do trial_division


        #len_busy_primes = ?
        #   deleted since [len_busy_primes == len(ihead2may_itail)]


        next_busy_prime = first_prime = 2
        # square4next_busy_prime = next_busy_prime**2
        square4next_busy_prime = 4
        # prev____square4next_busy_prime = 1

        # for n in _count(first_prime):
        for n in _count(2):
            # [prev____square4next_busy_prime < n <= square4next_busy_prime]
            may_ihead = get_(n)
            drop_(n)
            #advance_ should be after drop_!!! since extend offsetted_sieve
            if may_ihead is None and n == square4next_busy_prime:
                #not prime # next_busy_prime**2
                ihead4next_busy_prime = len(ihead2may_itail)
                may_ihead = ihead4next_busy_prime
                #prev____square4next_busy_prime = square4next_busy_prime
                (next_busy_prime, square4next_busy_prime) = add_new_busy_prime()
            iheads = (*iter_(may_ihead),)
            if not iheads:
                #prime
                #m = p = n
                on_prime(n)
                    #before yield: put into primes
                yield mk4prime(n)
            else:
                #not prime
                #m = primes[iheads[0]]
                on_composite(n, iheads)
                yield mk4composite(n, iheads, next_busy_prime, square4next_busy_prime)
                advance_(n, iheads)
        return
    def advance_(n, iheads, /):
        #put_ vs get_
        assert iheads
        offset = lmay_offset[0]
        k4n = n - offset
        k2h = offsetted_sieve
        h2m = ihead2may_itail
        prs = primes

        max_k = k4n+prs[iheads[-1]]
        if not max_k < len(k2h):
            sz4pad = max_k+1 -len(k2h)
            k2h.extend(_repeat(None, sz4pad))

        for ihead in iheads:
            p = prs[ihead]
            k = k4n+p
            h2m[ihead] = k2h[k]
            k2h[k] = ihead
    def get_(n, /):
        offset = lmay_offset[0]
        k4n = n - offset
        if not k4n >= 0:raise logic-err
        k2h = offsetted_sieve
        may_ihead = None if not k4n < len(k2h) else k2h[k4n]
        return may_ihead
    def drop_(n, /):
        #nonlocal offset
        k2h = offsetted_sieve
        offset = lmay_offset[0]
        k4n = n - offset
        if k4n < len(k2h):
            k2h[k4n] = -1
        num_nil_slots = k4n+1
        L = len(k2h)
        if not num_nil_slots*3 < L*2:
            del k2h[:num_nil_slots]
            #offset += num_nil_slots
            lmay_offset[0] += num_nil_slots
    #def add_new_busy_prime(len_busy_primes, /):
    #    '-> (len_busy_primes, square4next_busy_prime)'
    def add_new_busy_prime():
        '-> (next_busy_prime, square4next_busy_prime)'
        # in first round: [old-next_busy_prime == 2]
        # in first round: [old-ihead2may_itail<2> == 0]
        # in first round: [old-square4next_busy_prime<2> == 4]

        # in first round: [new-next_busy_prime == 3]
        ihead2may_itail.append(None)
            # len_busy_primes += 1
        ihead4next_busy_prime = len(ihead2may_itail)
        # in first round: [new-ihead2may_itail<3> == 1]
        if to_cache_only_busy_primes_plus_next:
            next_busy_prime = next(iter_busy_primes)
            assert len(only_busy_primes_plus_next) == 1+len(ihead2may_itail)
        else:
            next_busy_prime = primes[ihead4next_busy_prime]

        square4next_busy_prime = next_busy_prime**2
        # in first round: [new-square4next_busy_prime<3> == 9]
        return (next_busy_prime, square4next_busy_prime)
    def iter_(may_ihead, /):
        h2m = ihead2may_itail
        while not may_ihead is None:
            ihead = may_ihead
            yield ihead
            #may_itail = h2m[ihead]
            may_ihead = h2m[ihead]
    if to_export_all_prime_factors:
        def mk4prime(n, /):
            p = n
            m = p
            fs = (p,)
            return (n, fs)
        def mk4composite(n, iheads, next_busy_prime, square4next_busy_prime, /):
            #OK@[n==old-square4next_busy_prime]
            #   even call mk4composite() after next_busy_prime,square4next_busy_prime updated
            #       since fs=[old-next_busy_prime] is complete, [_1_or_p==1]
            fs = [primes[ihead] for ihead in iheads]
            (p2e, _1_or_p) = semi_factor_pint_via_trial_division(fs, n)
            if not _1_or_p == 1:
                p = _1_or_p
                assert next_busy_prime <= p < square4next_busy_prime
                fs.append(p)
            fs = (*fs,)
            if has_u2ps:
                if not (_n:=II(fs)) == n:
                    # [n :: non_squarefree]
                    # [_n :: squarefree]
                    #assert 4 <= _n < n, (n, fs, _n)
                        # ^AssertionError: (4, (2,), 2)
                    assert 2 <= _n < n, (n, fs, _n)
                    _fs = u2ps_(_n) #优化冫复用小对象
                    assert _fs == fs, (n, fs, _n, _fs)
                        # ^AssertionError: (20, (2, 5), 10, (3,))
                        #   bug:all_prime_factors_gen[:20] --> (None, (), (2,), (3,), (2,), (5,), (2, 3), None, (), (2,), (3,), (2,), (5,), (2, 3), (7,), (2,), (3,), (2, 5), (11,), (2, 3))
                    fs = _fs
                else:
                    # [n :: squarefree]
                    fs
                    pass
                fs
            fs
            return (n, fs)
    else:
        def mk4prime(n, /):
            p = n
            m = p
            return (n, m)
        def mk4composite(n, iheads, next_busy_prime, square4next_busy_prime, /):
            m = primes[iheads[0]]
            return (n, m)
    if to_cache_only_busy_primes_plus_next:
        def on_prime(n, /):
            pass
    else:
        def on_prime(n, /):
            p = n
            primes.append(p)
    def on_composite(n, iheads, /):
        pass
    return main()








def tabulate_may_min_prime_factor4uint_lt_(sz, /, *, _mk=tuple):
    '-> uint2may_min_prime_factor/[may prime]/[None,None,prime...]'
    if _mk is list: _mk = echo
    #########
    #new:
    check_int_ge(0, sz)
    u2p = [None]*sz
    #floor_sqrt4sz = floor_sqrt(sz)
    #end4stage1 = min(1+floor_sqrt4sz, sz)
    #for u in range(2, end4stage1):
    big = False
    for u in range(2, sz):
        if u2p[u] is None:
            p = u
            u2p[u] = p
            if big:continue
            uu = u**2
            if not uu < sz:
                big = True
                continue
            for v in range(uu, sz, p):
                if u2p[v] is None:
                    u2p[v] = p
    return _mk(u2p)
    return tuple(u2p)
    #########
    #old:
    #.return min_prime_factor_gen[:sz]
    #########
r'''[[[
>>> 1/2*2/3
0.3333333333333333
>>> 1/2*2/3*4/5
0.26666666666666666
>>> 1/2*2/3*4/5*6/7
0.2285714285714286
>>> 1/2*2/3*4/5*6/7*10/11
0.20779220779220783
>>> 1/2*2/3*4/5*6/7*10/11*12/13
0.19180819180819184
>>> 1/2*2/3*4/5*6/7*10/11*12/13*16/17
0.18052535699594527
>>> 2*3*5*7*11
2310
>>> 2*3*5*7*11*13
30030
>>> 2*3*5*7*11*13*17
510510

#]]]'''#'''
def iter_find_best_wheel_paramss4sieve_lt_(szs, /):
    for sz in szs:
        (num_ps, sz4wheel, result_sz, ps) = find_best_wheel_params4sieve_lt_(sz)
        yield (sz, (num_ps, sz4wheel, result_sz, ps))
def find_best_wheel_params4sieve_lt_(sz, /):
    'sz -> (num_ps, sz4wheel, result_sz, ps)'
    check_int_ge(0, sz)
    from fractions import Fraction
    from math import ceil
    fr_sz = Fraction(sz)

    primes = []
    def iter_():
        num_ps = 0
        sz4wheel = 1
        num_coprimes4wheel = 1
        result_sz = sz
        yield (num_ps, sz4wheel, result_sz)
        #.for p in iter(prime_gen):
        #for p in raw_iter_all_strict_sorted_primes_(may_primes=primes, to_cache_only_busy_primes_plus_next=False):
        for p in iter_all_strict_sorted_primes_(may_primes=primes):
            num_ps += 1
            sz4wheel *= p
            num_coprimes4wheel *= (p-1)
            # (q, r) = divmod(sz, num_coprimes4wheel)
            result_sz = sz4wheel +num_coprimes4wheel +ceil(fr_sz*num_coprimes4wheel/sz4wheel)
                # (wheel, j2coprime, sieve)
            yield (num_ps, sz4wheel, result_sz)
    it = iter_()
    for (num_ps, sz4wheel, result_sz), (_num_ps, _sz4wheel, _result_sz) in pairwise(it):
        if result_sz < _result_sz:
            break
    #.ps4wheel = prime_gen[:num_ps]
    ps4wheel = tuple(primes[:num_ps])
    assert len(ps4wheel) == num_ps
    return (num_ps, sz4wheel, result_sz, ps4wheel)
def _init_wheel(sz4wheel, ps4wheel, /):
    assert ps4wheel
    wheel = [None]*sz4wheel
    for p in reversed(ps4wheel):
        #bug:for u in range(p, sz4wheel, p):
        for u in range(0, sz4wheel, p):
            wheel[u] = p
    wheel
    j2coprime = []
    for u in range(0, sz4wheel):
        if wheel[u] is None:
            # coprime
            # [gcd(u, sz4wheel) == 1]
            coprime = u
            wheel[coprime] = -len(j2coprime) # -j
            j2coprime.append(coprime)
    j2coprime
    wheel # == u2p_or_neg_j :: [(p|-j)]
    return (wheel, j2coprime)
def _sieve_wheel(wheel, j2coprime, sz, /):
    sz4wheel = len(wheel)
    assert sz4wheel > 1
    num_coprimes = len(j2coprime)
    (num_wheels, sz4tail) = divmod(sz, sz4wheel)
    end4j6tail = bisect_left(j2coprime, sz4tail)
    if end4j6tail < num_coprimes:
        assert sz4tail <= j2coprime[end4j6tail]
    if 0 < end4j6tail:
        assert j2coprime[end4j6tail-1] < sz4tail

    #bug:sz4tbl = num_wheels*sz4wheel +end4j6tail
    sz4tbl = num_wheels*num_coprimes +end4j6tail
    j2p = [None]*sz4tbl
    #def __(j2coprime, num_wheels, sz4tbl, ):
    def __():
        u0 = 0
        j0 = 0
        done = False
        for j4wheel in range(1+num_wheels):
            for j4u, coprime in enumerate(j2coprime, j0):
                if j4u == sz4tbl:
                    done = True
                    break
                if j2p[j4u] is None:
                    u = u0 +coprime
                    if u == 1:continue
                    assert u >= 2, (j4u, u, u0, coprime, sz4wheel, j2coprime)
                    yield (j4u, coprime, u)
            if done:break
            #########next round:
            u0 += sz4wheel
            j0 += num_coprimes
        else:
            raise Exception(j0, j4u, sz4tbl)
            raise 000
    #end-def __():

    big = False
    for (j4u, coprime, u) in __():
        p = u
        j2p[j4u] = p
        if big:continue
        uu = u**2
        if not uu < sz:
            big = True
            continue
        for v in range(uu, sz, p):
            (q4v, r4v) = divmod(v, sz4wheel)
            x = wheel[r4v]
            if x > 0:
                # [x <- ps4wheel]
                continue
            j4r4v = -x
            j4v = (j4r4v+q4v*num_coprimes)
            if None is j2p[j4v]:
                j2p[j4v] = p
    j2p
    return j2p
class TabulateMinPrimeFactor:
    #tabulate_may_min_prime_factor4uint_lt_
    #########
    # TODO:改版:TabulateMinPrimeFactor --> TabulatePrimes
    #   Algorithm__3_2_2(Fancy Eratosthenes sieve)
    #########
    def __init__(sf, sz, /):
        (num_ps, sz4wheel, result_sz, ps4wheel) = find_best_wheel_params4sieve_lt_(sz)
        no_wheel = not ps4wheel
        if no_wheel:
            # no wheel
            u2p = tabulate_may_min_prime_factor4uint_lt_(sz)
            sf._u2p = u2p
        else:
            (wheel, j2coprime) = _init_wheel(sz4wheel, ps4wheel)
            j2p = _sieve_wheel(wheel, j2coprime, sz)
            sf._4wjje = (wheel, j2coprime, j2p)
        sf._no_wheel = no_wheel
        sf._sz = sz
    def __len__(sf, /):
        sz = sf._sz
        return sz
    def __iter__(sf, /):
        return sf.iter7fancy_()
        return sf.iter7naive_()
    def iter7naive_(sf, /):
        '-> Iter (may min_p)'
        for u in range(len(sf)):
            yield sf[u]
    def iter7fancy_(sf, /):
        '-> Iter (may min_p)'
        if sf._no_wheel:
            u2p = sf._u2p
            yield from u2p
            return
        (wheel, j2coprime, j2p) = sf._4wjje
        sz4wheel = len(wheel)
        sz = sf._sz
        num_coprimes = len(j2coprime)

        u0 = 0
        j0 = 0
        done = False
        for j4wheel in _count(0):
            prev_coprime = -1
            for j4u, coprime in enumerate(j2coprime, j0):
                for _u in range(1+prev_coprime, coprime):
                    u = u0 +_u
                    if u == sz:
                        done = True
                        break
                    #if _u == 0 and u0 == 0:
                    if u == 0:
                        yield None
                    else:
                        yield wheel[_u]
                prev_coprime = coprime
                    # last coprime is (-1)%sz4wheel, no gap after it
                if done: break
                u = u0 +coprime
                if u == sz:
                    done = True
                    break
                #if u == 1:yield None
                may_p = j2p[j4u]
                yield may_p
            if done: break
            #########next round:
            u0 += sz4wheel
            j0 += num_coprimes
        else:
            raise 000


    def __getitem__(sf, u, /):
        'u -> may min_p'
        sz = sf._sz
        check_uint_lt(sz, u)
        if sf._no_wheel:
            u2p = sf._u2p
            return u2p[u]
        if u < 2:
            return None
        #check_int_ge_lt(2, sz, u)
        (wheel, j2coprime, j2p) = sf._4wjje
        sz4wheel = len(wheel)
        (q4u, r4u) = divmod(u, sz4wheel)
        x = wheel[r4u]
        if x > 0:
            p = x
            return p
        j4r4u = -x
        num_coprimes = len(j2coprime)
        j4u = (j4r4u +q4u*num_coprimes)
        p = j2p[j4u]
        return p
    def iter_prime_factors_at_(sf, u, /):
        'u -> Iter p'
        check_int_ge_lt(1, len(sf), u)
        while not u == 1:
            p = sf[u]
            yield p
            (ep, u) = factor_pint_out_power_of_base_(p, u)
            assert ep > 0
    def extract_prime_factors_at_(sf, u, /):
        'u -> [p]'
        ps4u = tuple(sf.iter_prime_factors_at_(u))
        return ps4u
    def extract_prime_factorization_at_(sf, u, /):
        'u -> {p:e}'
        check_int_ge_lt(1, len(sf), u)
        p2e4u = {}
        while not u == 1:
            p = sf[u]
            (ep, u) = factor_pint_out_power_of_base_(p, u)
            assert ep > 0
            p2e4u[p] = ep
        return p2e4u
#end-class TabulateMinPrimeFactor:

def _old__tabulate_may_factorization4uint_lt_(sz, uint2may_min_prime_factor=None, /, *, _mk=tuple):
    #old_ver:tabulate_may_factorization4uint_lt_
    '-> uint2may_factorization/[may p2e/{prime:exp}]/[None,p2e...]'
    check_int_ge(0, sz)
    if _mk is list: _mk = echo
    if uint2may_min_prime_factor is None:
        uint2may_min_prime_factor = tabulate_may_min_prime_factor4uint_lt_(sz)
    u2p = uint2may_min_prime_factor

    u2f = uint2may_factorization = [None, {}]
    del u2f[sz:]
    for u in range(2, sz):
        assert u == len(u2f)
        p = u2p[u]
        v = u//p
        p2e = u2f[v].copy()
        p2e.setdefault(p, 0)
        p2e[p] += 1
        u2f.append(p2e)
    assert len(u2f) == sz
    return _mk(u2f)
def tabulate_may_factorization4uint_lt_(sz, uint2may_min_prime_factor=None, /, *, _mk=tuple):
    #new_ver:tabulate_may_factorization4uint_lt_
    #deprecated by:tabulate_may_prime_factorization4uint_lt_
    #   old-API:kw:uint2may_factorization
    '-> uint2may_factorization/[may p2e/{prime:exp}]/[None,p2e...]'
    del uint2may_min_prime_factor
    return tabulate_may_prime_factorization4uint_lt_(sz, _mk=_mk)
def tabulate_may_pairs8prime_factorization4uint_lt_(sz, /, *, _mk=tuple, dict_vs_pairs=True, _validate=False):
    '-> uint2may_pairs8factorization/[may p_e_pairs/[(prime,exp)]]/[None,p_e_pairs...]'
    return tabulate_may_prime_factorization4uint_lt_(sz, _mk=_mk, dict_vs_pairs=dict_vs_pairs, _validate=_validate)
def tabulate_may_prime_factorization4uint_lt_(sz, /, *, _mk=tuple, dict_vs_pairs=False, _validate=False):
    '-> uint2may_factorization/[may p2e/{prime:exp}]/[None,p2e...]'
    check_int_ge(0, sz)
    if _mk is list: _mk = echo

    #########
    if dict_vs_pairs:
        u2m = u2may_pes = [[] for _ in range(sz)]
    else:
        u2m = u2may_p2e = [{} for _ in range(sz)]
    u2m
    if sz:
        u2m[0] = None
    else:
        return _mk(u2m)
    u2m

    #########
    if dict_vs_pairs:
        def on_prime_power_(u, pe, /):
            if u == 0: return
            (p, e) = pe
            if e == 1:
                u2may_pes[u].append(None)
            u2may_pes[u][-1] = pe
        on_prime_power_
    else:
        def on_prime_power_(u, pe, /):
            if u == 0: return
            (p, e) = pe
            u2may_p2e[u][p] = e
        on_prime_power_
    on_prime_power_
    #########
    max_u = -1+sz
    max1_e = max_u.bit_length()
    flsqrtL = floor_sqrt(-1+sz)
    big = False
    for u in range(2, sz):
        if not u2m[u]:
            p = u
            # [p <?> sqrt(max_u)]
            if not big and p > flsqrtL:
                # [p > sqrt(max_u)]
                # [p**2 > max_u]
                max1_e = 2
                big = True
            _sieve_p_0_(sz, on_prime_power_, p, max1_e)
    #########
    #u2may_p2e or u2may_pes
    #########
    if dict_vs_pairs:
        for u in range(1, sz):
            u2may_pes[u] = tuple(u2may_pes[u])
    #########
    assert len(u2m) == sz
    if _validate:
        if dict_vs_pairs:
            check_uint2may_pairs8prime_factorization_(u2may_pes)
        else:
            check_uint2may_prime_factorization_(u2may_p2e)
    #########
    return _mk(u2m)
if 1:
    def _sieve_p_0_(sz, on_prime_power_, p, max1_e, /):
        'unoffsetted#vs:_sieve_p_'

        pw = 1 # p powers
        for e in range(1, max1_e):
            pe = (p, e)
            pw *= p
            # [pw == p**e]

            u0 = pw
            if not u0 < sz:
                break
            # [u0%pw == 0]
            for u in range(u0, sz, pw):
                # [u >= u0]
                # [u%pw == u0%pw == 0]
                on_prime_power_(u, pe)
                #########
    #end-def _sieve_p_0_(p, max1_e, /):








def tabulate_may_all_prime_factors4uint_lt_(sz, /, *, _mk=tuple):
    '-> uint2may_all_prime_factors/[may [prime]]/[None,[prime]...]'
    # core_sieve4prime_factors__ge_le
    # tabulate_may_all_prime_factor_lflnkls4uint_lt_
    if _mk is list: _mk = echo
    #########
    #new:
    u2ps = tabulate_may_all_prime_factor_lflnkls4uint_lt_(sz, _mk=echo)
    for u in range(2, sz):
        # [u2ps[:u] :: [[prime]]]
        # [u2ps[u:] :: [[lflnkls prime]]]
        lflnkls8ps4u = u2ps[u]
        # [lflnkls8ps4u :: lflnkls prime]
        p = lflnkls8ps4u[0]
        v = u//p
        ps4v = u2ps[v]
        # [ps4v :: [prime]]
        #ps4u = ps4v if ps4v and ps4v[0] == p else (p, *ps4v)
        if ps4v and ps4v[0] == p:
            # [v%p == 0]
            # [u%p**2 == 0]
            ps4u = ps4v #优化冫复用小对象
        elif not (_w:=II(ps4v)) == v:
            # [u,v :: non_squarefree]
            w = p*_w
            # [w :: squarefree]
            assert w < v < u
            ps4u = u2ps[w] #优化冫复用小对象
        else:
            # [u,v :: squarefree]
            ps4u = (p, *ps4v)
        ps4u
        u2ps[u] = ps4u
        # [ps4u :: [prime]]
    u2ps
    return _mk(u2ps)


    #########
    #old:
    #.return all_prime_factors_gen[:sz]
    #########
#def tabulate_may_reversed_prime_factor_rglnkls4uint_lt_(sz, /):
#    '-> uint2may_reversed_prime_factor_rglnkls/[may (rglnkls prime)]/[None, (), ((),2), ((),3), ((),2), ((),5), (((),3),2), ...]'
def tabulate_may_all_prime_factor_lflnkls4uint_lt_(sz, /, *, _mk=tuple):
    '-> uint2may_all_prime_factor_lflnkls/[may (lflnkls prime)]/[None, (), (2,()), (3,()), (2,()), (5,()), (2,(3,())), ...] #see:extract_prime_factorization5uint2may_all_prime_factor_lflnkls_,complete_factor_pint_via_trial_division__lflnkls_'
    from seed.data_funcs.lnkls import lflnkls2iterable
    if _mk is list: _mk = echo
    u2p = tabulate_may_min_prime_factor4uint_lt_(sz, _mk=echo)
    assert len(u2p) == sz
    u2ps = u2p
    if sz >= 2:
        u2ps[1] = ()
    for u in range(2, sz):
        p = u2p[u]
        v = u//p
        ps4v = u2ps[v]
        #ps4u = ps4v if ps4v and ps4v[0] == p else (p, ps4v)
        if ps4v and ps4v[0] == p:
            # [v%p == 0]
            # [u%p**2 == 0]
            ps4u = ps4v #优化冫复用小对象
        elif not (_w:=II(lflnkls2iterable(ps4v))) == v:
            # [u,v :: non_squarefree]
            w = p*_w
            # [w :: squarefree]
            assert w < v < u
            ps4u = u2ps[w] #优化冫复用小对象
        else:
            # [u,v :: squarefree]
            ps4u = (p, ps4v)
        ps4u
        u2ps[u] = ps4u
    u2ps
    return _mk(u2ps)



def extract_prime_factorization5uint2may_all_prime_factor_lflnkls_(uint2may_all_prime_factor_lflnkls, u, /):
    '[lflnkls prime] -> pint -> {prime:pint} #see:tabulate_may_all_prime_factor_lflnkls4uint_lt_'
    check_int_ge(1, u)
    lflnkls8ps4u = uint2may_all_prime_factor_lflnkls[u]
    p2e4u = complete_factor_pint_via_trial_division__lflnkls_(lflnkls8ps4u, u)
    return p2e4u















def check_offsetted_uint2prime_factors_(min_u, offsetted_u2ps, /):
    check_int_ge(1, min_u)
    check_offsetted_uint2may_prime_factors_(min_u, offsetted_u2ps)
def check_uint2may_prime_factors_(u2may_ps, /):
    check_offsetted_uint2may_prime_factors_(min_u:=0, u2may_ps)
def check_offsetted_uint2may_prime_factors_(min_u, offsetted_u2may_ps, /):
    check_int_ge(0, min_u)
    for u, may_ps in enumerate(offsetted_u2may_ps, min_u):
        if u == 0:
            assert may_ps is None
            continue
        ps = may_ps
        assert is_strict_sorted(ps), (u, ps)
        p2e = complete_factor_pint_via_trial_division(ps, u)
        assert len(p2e) == len(ps), (u, ps)




def check_offsetted_uint2pairs8prime_factorization_(min_u, offsetted_u2pes, /):
    check_int_ge(1, min_u)
    check_offsetted_uint2may_pairs8prime_factorization_(min_u, offsetted_u2pes)
def check_uint2may_pairs8prime_factorization_(u2may_pes, /):
    check_offsetted_uint2may_pairs8prime_factorization_(min_u:=0, u2may_pes)
def check_offsetted_uint2may_pairs8prime_factorization_(min_u, offsetted_u2may_pes, /):
    check_int_ge(0, min_u)
    for u, may_pes in enumerate(offsetted_u2may_pes, min_u):
        if u == 0:
            assert may_pes is None
            continue
        pes = may_pes
        assert all(e > 0 for p, e in pes), (u, pes)
        assert is_strict_sorted(pes), (u, pes)
        assert u == II(p**e for p, e in pes), (u, pes)



def check_offsetted_uint2prime_factorization_(min_u, offsetted_u2p2e, /):
    check_int_ge(1, min_u)
    check_offsetted_uint2may_prime_factorization_(min_u, offsetted_u2p2e)
def check_uint2may_prime_factorization_(u2may_p2e, /):
    check_offsetted_uint2may_prime_factorization_(min_u:=0, u2may_p2e)
def check_offsetted_uint2may_prime_factorization_(min_u, offsetted_u2may_p2e, /):
    check_int_ge(0, min_u)
    for u, may_p2e in enumerate(offsetted_u2may_p2e, min_u):
        if u == 0:
            assert may_p2e is None
            continue
        p2e = may_p2e
        assert all(e > 0 for p, e in p2e.items()), (u, p2e)
        assert u == II(p**e for p, e in p2e.items()), (u, p2e)







__all__
from seed.math.prime_sieve.sieve_lt import list_all_strict_sorted_primes__lt_, sieve4uint2is_prime__lt_
from seed.math.prime_sieve.sieve_lt import list_primes__lt_, list_primes__len_ge_

#from seed.math.prime_sieve.sieve_lt import iter_all_strict_sorted_primes_, PrimeList #to_replace:prime_gen
from seed.math.prime_sieve.sieve_lt import iter_all_strict_sorted_primes_ #to_replace:prime_gen
from seed.math.prime_sieve.sieve_lt import raw_list_all_strict_sorted_primes__lt_, raw_iter_all_strict_sorted_primes__lt_, raw_iter_all_strict_sorted_primes_, raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_, raw_list_all_strict_sorted_ints__ge2__with_min_prime_factor__sized_

from seed.math.prime_sieve.sieve_lt import tabulate_may_min_prime_factor4uint_lt_
from seed.math.prime_sieve.sieve_lt import TabulateMinPrimeFactor, iter_find_best_wheel_paramss4sieve_lt_, find_best_wheel_params4sieve_lt_

from seed.math.prime_sieve.sieve_lt import tabulate_may_all_prime_factors4uint_lt_, tabulate_may_all_prime_factor_lflnkls4uint_lt_, extract_prime_factorization5uint2may_all_prime_factor_lflnkls_


from seed.math.prime_sieve.sieve_lt import tabulate_may_pairs8prime_factorization4uint_lt_, tabulate_may_prime_factorization4uint_lt_#deprecated: tabulate_may_factorization4uint_lt_




from seed.math.prime_sieve.sieve_lt import check_offsetted_uint2may_prime_factors_, check_offsetted_uint2prime_factors_, check_uint2may_prime_factors_

from seed.math.prime_sieve.sieve_lt import check_offsetted_uint2may_pairs8prime_factorization_, check_offsetted_uint2pairs8prime_factorization_, check_uint2may_pairs8prime_factorization_

from seed.math.prime_sieve.sieve_lt import check_offsetted_uint2may_prime_factorization_, check_offsetted_uint2prime_factorization_, check_uint2may_prime_factorization_

if 1:from seed.math.prime_sieve.sieve_lt import _iter__lt_


from seed.math.prime_sieve.sieve_lt import *
