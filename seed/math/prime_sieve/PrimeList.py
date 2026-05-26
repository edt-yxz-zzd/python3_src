#__all__:goto
r'''[[[
e ../../python3_src/seed/math/prime_sieve/PrimeList.py

seed.math.prime_sieve.PrimeList
py -m nn_ns.app.debug_cmd   seed.math.prime_sieve.PrimeList -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.prime_sieve.PrimeList:__doc__ -ht # -ff -df
#######

[[
move_from:
view ../../python3_src/seed/math/prime_sieve/sieve_lt.py
]]


'#'; __doc__ = r'#'

__call__
>>> ps = PrimeList()
>>> ps(3)
7
>>> ps(...)
SeqView([2, 3, 5, 7])
>>> [*ps(...)]
[2, 3, 5, 7]
>>> ps(6, 9)
SeqSliceView([2, 3, 5, 7, 11, 13, 17, 19, 23], range(6, 9))
>>> ps(6, 9)[-1]
23
>>> ps(6, 9)[2:]
SeqSliceView([2, 3, 5, 7, 11, 13, 17, 19, 23], range(8, 9))
>>> [*ps(6, 9)[2:]]
[23]
>>> [*ps(6, 9)]
[17, 19, 23]
>>> [*ps(4, 9)]
[11, 13, 17, 19, 23]
>>> [*ps(4, 5)]
[11]
>>> [*ps(4, 4)]
[]
>>> [*ps(4, 3)]
[]
>>> [*ps(2, 9, max1=7)]
[5]
>>> [*ps(2, 9, max1=8)]
[5, 7]
>>> [*ps(2, 9, max1=-1)]
[]

>>> ps = PrimeList()
>>> [*ps(2, 4, max1=12)]
[5, 7]
>>> ps = PrimeList()
>>> [*ps(2, 4, max1=8)]
[5, 7]
>>> ps = PrimeList()
>>> [*ps(2, 4, max1=7)]
[5]
>>> ps = PrimeList()
>>> [*ps(2, 4, max1=6)]
[5]
>>> ps = PrimeList()
>>> [*ps(2, 4, max1=5)]
[]


>>> ps = PrimeList()
>>> [*ps(2, max1=12)]
[5, 7, 11]
>>> ps = PrimeList()
>>> [*ps(2, max1=11)]
[5, 7]
>>> ps = PrimeList()
>>> [*ps(2, max1=8)]
[5, 7]
>>> ps = PrimeList()
>>> [*ps(2, max1=7)]
[5]
>>> ps = PrimeList()
>>> [*ps(2, max1=6)]
[5]
>>> ps = PrimeList()
>>> [*ps(2, max1=5)]
[]
>>> ps = PrimeList()
>>> [*ps(2, max1=0)]
[]
>>> ps = PrimeList()
>>> [*ps(2, max1=-1)]
[]



>>> ps = PrimeList()
>>> ps(2**20, 2**21, max1=2**22) #estimate_lower_bound4Kth_prime_
SeqSliceView([], range(1048576, 0))



__getitem__
>>> ps = PrimeList()
>>> [*ps[:9:2]]
[2, 5, 11, 17, 23]
>>> ps[:9:2]
SeqSliceView([2, 3, 5, 7, 11, 13, 17, 19, 23], range(0, 9, 2))


__iter__
>>> ps = PrimeList()
>>> [*islice(ps, 0, 5)]
[2, 3, 5, 7, 11]




len7relax_
__init__.arg:max1_prime6init
>>> ps = PrimeList()
>>> ps.len7relax_()
0
>>> ps[4]
11
>>> ps.len7relax_()
5


>>> ps = PrimeList(6)
>>> ps.len7relax_()
3
>>> ps[4]
11
>>> ps.len7relax_()
5


>>> ps = PrimeList(14)
>>> ps.len7relax_()
6
>>> ps[4]
11
>>> ps.len7relax_()
6
>>> ps.find7relax_(11)
4
>>> ps.find7relax_(13)
5
>>> ps.find7relax_(17)
-1
>>> ps.find7relax_(10)
-1
>>> ps.find7relax_(1)
-1
>>> ps.find7relax_(2)
0



>>> ps = PrimeList()
>>> [*ps.iter__sz_(4)]
[2, 3, 5, 7]
>>> [*ps.iter__lt_(4)]
[2, 3]


>>> ps = PrimeList()
>>> [*ps.iter_find_primes_if_be_1addKmulX__lt_(30, 7)]
[29]
>>> [*ps.iter_find_primes_if_be_1addKmulX__lt_(30, 1)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> [*ps.iter_find_primes_if_be_1addKmulX__lt_(30, 2)]
[3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> [*ps.iter_find_primes_if_be_1addKmulX__lt_(30, 3)]
[7, 13, 19]
>>> [*ps.iter_find_primes_if_be_1addKmulX__lt_(30, 6)]
[7, 13, 19]




>>> dqr_ls = DivmodOverPrimeList(999, PrimeList())
>>> dqr_ls[4]
(11, 90, 9)
>>> dqr_ls[2:4]
SeqSliceView([(2, 499, 1), (3, 333, 0), (5, 199, 4), (7, 142, 5), (11, 90, 9)], range(2, 4))
>>> [*dqr_ls[2:4]]
[(5, 199, 4), (7, 142, 5)]
>>> dqr_ls[2:4][-1]
(7, 142, 5)
>>> [*dqr_ls[2:8:2]]
[(5, 199, 4), (11, 90, 9), (17, 58, 13)]
>>> [*islice(dqr_ls, 5)]
[(2, 499, 1), (3, 333, 0), (5, 199, 4), (7, 142, 5), (11, 90, 9)]
>>> dqr_ls(11)
(11, 90, 9)
>>> dqr_ls(4)
(4, 249, 3)




>>> dr_ls = ModOverPrimeList(999, PrimeList())
>>> dr_ls[4]
(11, 9)
>>> dr_ls[2:4]
SeqSliceView([(2, 1), (3, 0), (5, 4), (7, 5), (11, 9)], range(2, 4))
>>> [*dr_ls[2:4]]
[(5, 4), (7, 5)]
>>> dr_ls[2:4][-1]
(7, 5)
>>> [*dr_ls[2:8:2]]
[(5, 4), (11, 9), (17, 13)]
>>> [*islice(dr_ls, 5)]
[(2, 1), (3, 0), (5, 4), (7, 5), (11, 9)]
>>> dr_ls(11)
(11, 9)
>>> dr_ls(4)
(4, 3)






py_adhoc_call   seed.math.prime_sieve.PrimeList   @f
]]]'''#'''
__all__ = r'''
PrimeList
DivmodOverPrimeList
ModOverPrimeList
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from itertools import islice, count
    from bisect import bisect_left

    from seed.tiny_.check import check_int_ge, check_type_is
    from seed.helper.ifNone import ifNone

    from seed.math.prime_pint.bounds4kth_prime import estimate_lower_bound4Kth_prime_

    from seed.types.view.SeqSliceView import SeqSliceView
    from seed.types.view.View import SeqView




    from seed.math.prime_sieve.sieve_lt import list_primes__lt_
    from seed.math.prime_sieve.sieve_ge_le import iter_sieve4primes_ge_
def _iter_primes__ge_(min_u, primes, /):
    for p in iter_sieve4primes_ge_(min_u):
        primes.append(p)
        yield p

#.#################################
___end_mark_of_excluded_global_names__0___ = ...
def _explain(emay_idx_or_slice, /):
    '-> emay_idx_or_rng/(...|idx|range)'
    match emay_idx_or_slice:
        case slice(start=begin, stop=end, step=step):
            begin = ifNone(begin, 0)
            step = ifNone(step, 1)
            check_int_ge(0, begin)
            check_int_ge(0, end)
            check_int_ge(1, step)
            #check_type_is(int, step)
            rng = range(begin, end, step)
            if rng:
                _end = 1+rng[-1]
                if not _end == end:
                    assert _end < end
                    rng = range(begin, _end, step)
            else:
                rng = range(0, 0, 1)
            return rng
        case emay_j:
            if emay_j is ...:
                return ...
            j = emay_j
            check_int_ge(0, j)
            return j

    raise 000

class PrimeList:
    def __init__(sf, max1_prime6init=0, /):
        check_int_ge(0, max1_prime6init)
        sf._ps = primes = list_primes__lt_(max1_prime6init, _mk=list)
        sf._it = _iter_primes__ge_(max1_prime6init, primes)
    def len7relax_(sf, /):
        return len(sf._ps)
    def find7relax_(sf, p, /):
        'uint -> imay idx'
        ps = sf._ps
        j = bisect_left(ps, p)
        if j < len(ps) and ps[j] == p:
            return j
        return -1
    def iter_find_primes_if_be_1addKmulX__lt_(sf, max1, k, /):
        check_int_ge(1, k)
        if k == 1:
            yield from sf.iter__lt_(max1)
            return
        ps = sf._ps
        end = len(sf(0, max1=max1))
        if k&1:
            k <<= 1
        j = 0
        for n in range(1+k, max1, k):
            j = bisect_left(ps, n, j, end)
            if ps[j] == n:
                yield n
    def iter__sz_(sf, sz, /):
        return islice(sf, 0, sz)
    def iter__lt_(sf, max1, /):
        for p in sf:
            if not p < max1:break
            yield p
    def __iter__(sf, /):
        ps = sf._ps
        it = sf._it
        for j in count(0):
            if j == len(ps):
                next(it)
                #sf._fill_ge(j)
            yield ps[j]
    def __getitem__(sf, emay_idx_or_slice, /):
        emay_idx_or_rng = _explain(emay_idx_or_slice)
        match emay_idx_or_rng:
            case range(start=begin, stop=end, step=step):
                ps_view = sf(begin, end)
                if not step == 1:
                    ps_view = ps_view[::step]
                return ps_view
            case emay_j:
                return sf(emay_j)
        raise 000
    def __call__(sf, emay_idx_or_begin, /, end=None, *, max1=None):
        'emay (idx|begin) -> may end -> may (kw:max1) -> prime_gen[idx] if end is None is max1 else prime_seq # [prime_seq==frozen-SeqView(takewhile(max1.__gt__, prime_gen[begin:end])) if not emay_idx_or_begin is ... else dynamic-SeqView(prime_gen{sf})]'
        ps = sf._ps
        if emay_idx_or_begin is ...:
            return SeqView(ps)

        idx_or_begin = emay_idx_or_begin
        check_int_ge(0, idx_or_begin)
        # [idx_or_begin >= 0]
        #may_end = end
        #may_max1 = max1
        if end is None is max1:
            j = idx_or_begin
            # [j >= 0]
            if not j < len(ps):
                sf._fill_ge(j)
            return ps[j]
        # [not$[end is None is max1]]
        begin = idx_or_begin
        # [begin >= 0]
        expected_end = sf._fill_to(begin, end, max1)
        return SeqSliceView(ps, range(begin, expected_end))

    def _fill_to(sf, begin, may_end, may_max1, /):
        # [begin >= 0]
        # [not$[end is None is max1]]
        assert begin >= 0
        assert not (may_end is None is may_max1)
        #########
        if may_end is None:
            # [end == +oo]
            # [max1 < +oo]
            end = may_max1
            # [end < +oo]
        else:
            # [end < +oo]
            end = may_end
        end
        # [end < +oo]
        #end = max(begin, end)
        if not begin < end:
            return (expected_end:=0)
        # [0 <= begin < end < +oo]
        #########
        if may_max1 is None:
            # [max1 == +oo]
            def max1_le_q_(q, /):
                return False
        else:
            # [max1 < +oo]
            max1 = may_max1
            max1 = max(0, max1)
            # [0 <= max1 < +oo]
            if max1 <= 2:
                return (expected_end:=0)
            # [3 <= max1 < +oo]
            max1_le_q_ = max1.__le__
        max1_le_q_
        # [0 <= max1 <= +oo]
        #########
        # [0 <= begin < end < +oo]
        # [0 <= max1 <= +oo]
        max1_le_q_
        it = sf._it
        ps = sf._ps
        sz = len(ps)
        if begin < sz and max1_le_q_(ps[begin]):
            return (expected_end:=0)
        # [[begin >= sz]or[ps[begin] < max1]]
        q = ps[-1] if sz else 1
        # [max1 <?> q == ps[-1] if ps else 1]
        if max1_le_q_(q):
            # [max1 <= q == ps[-1] if ps else 1]
            # [0 <= expected_end <= (-1+sz if ps else 0)]
            # [0 <= expected_end <= max(0,-1+sz)]
            # !! [0 <= end < +oo]
            # !! [0 <= expected_end <= end]
            # [0 <= expected_end <= min(end, max(0,-1+sz)) < len(ps)+[sz==0]]
            if not begin < sz:
                # [begin >= sz >= expected_end]
                return (expected_end:=0)
            # [begin < sz]
            # !! [0 <= begin < end < +oo]
            # [0 <= begin < min(end, sz) < +oo]
            # [sz > 0]
            # !! [max1 <= q == ps[-1] if ps else 1]
            # [max1 <= q == ps[-1]]
            # !! [[begin >= sz]or[ps[begin] < max1]]
            # [ps[begin] < max1 <= ps[-1]]
            # [begin =!= -1+sz]
            # !! [0 <= begin < min(end, sz) < +oo]
            # [0 <= begin < min(end, -1+sz) < +oo]
            # !! [ps[begin] < max1]
            # [expected_end >= (1+begin)]
            # !! [sz > 0]
            # !! [0 <= expected_end <= min(end, max(0,-1+sz)) < len(ps)+[sz==0]]
            # [(1+begin) <= expected_end <= min(end, -1+sz) < len(ps)]
            assert sz
            #.expected_end = 0 if sz==0 else bisect_left(ps, max1, (1+begin), min(end, max(0,-1+sz)))
            expected_end = bisect_left(ps, max1, (1+begin), min(end, -1+sz))
            # !! [0 <= max1 <= +oo]
            # [max1 > ps[-1+expected_end] if expected_end else -1]
            # [[expected_end < end] -> [max1 <= ps[expected_end] if sz else 1]]
            # [0 <= expected_end <= min(end, len(ps))]
        elif end <= sz:
            # [len(ps) == sz >= end]
            # [max1 > q == ps[-1] if ps else 1]
            expected_end = end
            # !! [expected_end == end]
            # !! [0 <= max1 <= +oo]
            # [max1 > ps[-1+expected_end] if expected_end else -1]
            # [[expected_end < end] -> [max1 <= ps[expected_end] if sz else 1]]
            # [0 <= expected_end <= min(end, len(ps))]
        else:
            # [len(ps) == sz < end]
            # [max1 > q == ps[-1] if ps else 1]
            if not None is may_max1:
                max1
                if max1 <= (0 if begin == 0 else 1+(begin<<1)):
                    # [max1 <= lower_bound{PRIMES[begin]} <= PRIMES[begin]]
                    return (expected_end:=0)
                if max1 <= estimate_lower_bound4Kth_prime_(begin):
                    # [max1 <= lower_bound{PRIMES[begin]} <= PRIMES[begin]]
                    return (expected_end:=0)

            # [len(ps) == sz < end]
            # [max1 > q == ps[-1] if ps else 1]
            for sz in range(1+sz, 1+end):
                # [sz < 1+end]
                # [sz <= end]
                # !! [len(ps) == -1+sz < end]
                # [1 <= 1+len(ps) == sz <= end]
                # [max1 > q == ps[-1] if ps else 1]
                q = next(it)
                # [1 <= len(ps) == sz <= end]
                # [max1 > _q == ps[-2] if len(ps) >= 2 else 1]
                # [max1 <?> q == ps[-1]]
                if max1_le_q_(q):
                    # [max1 <= q == ps[-1]]
                    # [max1 > _q == ps[-2] if len(ps) >= 2 else 1]
                    # [1 <= len(ps) == sz <= end]
                    expected_end = -1+sz
                    # [expected_end == -1+sz <= -1+end < end]
                    # !! [sz >= 1]
                    # [0 <= expected_end < end]
                    # [max1 <= q == ps[expected_end]]
                    # [max1 > _q == ps[-1+expected_end] if expected_end else 1]
                    #==>>:
                    # !! [sz >= 1]
                    # [max1 > ps[-1+expected_end] if expected_end else -1]
                    # [[expected_end < end] -> [max1 <= ps[expected_end] if sz else 1]]
                    # [0 <= expected_end <= min(end, len(ps))]
                    break
                # [max1 > q == ps[-1]]
                # [len(ps) == sz <= end]
            else:
                # [len(ps) == sz == end]
                # [max1 > q == ps[-1]]
                expected_end = end
                # [max1 > ps[-1+expected_end] if expected_end else -1]
                # [[expected_end < end] -> [max1 <= ps[expected_end] if sz else 1]]
                # [0 <= expected_end <= min(end, len(ps))]
            expected_end
        expected_end
        #########
        # [max1 > ps[-1+expected_end] if expected_end else -1]
        # [[expected_end < end] -> [max1 <= ps[expected_end] if sz else 1]]
        # [0 <= expected_end <= min(end, len(ps))]
        #########
        # [MAYBE:[expected_end < begin]]
        return expected_end
        #########

    def _fill_ge(sf, j, /):
        # [j >= len(sf._ps)]
        sz = len(sf._ps)
        assert not j < sz
        #if not j < sz:
        it = islice(sf._it, 0, j+1-sz)
        for _ in it:pass

#end-class PrimeList:


class _OverPrimeList:
    @classmethod
    def _mk_result_tuple_(cls, n, d, /):
        raise 000
    def _gmk_result_tuple_(sf, d, /):
        d2t = sf._d2t
        if d in d2t:
            tpl = d2t[d]
        else:
            tpl = type(sf)._mk_result_tuple_(sf._n, d)
            d2t[d] = tpl
        return tpl
    def _mk_filling_iterator_(sf, /):
        for d in sf._qs:
            tpl = sf._gmk_result_tuple_(d)
            sf._ts.append(tpl)
            yield tpl
        raise 000
    def __init__(sf, n, prime_list, /):
        check_int_ge(1, n)
        check_type_is(PrimeList, prime_list)
        sf._n = n
        sf._qs = qs = prime_list
        sf._ts = ts = []
        sf._d2t = d2t = {}
        sf._it = sf._mk_filling_iterator_()
    @property
    def the_numerator(sf, /):
        return sf._n
    @property
    def the_prime_list(sf, /):
        return sf._qs
    def __iter__(sf, /):
        ts = sf._ts
        it = sf._it
        for j in count(0):
            if j == len(ts):
                next(it)
            tpl = ts[j]
            yield tpl
    def _fill_ge(sf, j, /):
        # [j >= len(sf._ts)]
        sz = len(sf._ts)
        assert not j < sz
        it = islice(sf._it, 0, j+1-sz)
        for _ in it:pass

    def __call__(sf, d, /):
        return sf._gmk_result_tuple_(d)
    def __getitem__(sf, emay_idx_or_slice, /):
        ts = sf._ts
        emay_idx_or_rng = _explain(emay_idx_or_slice)
        match emay_idx_or_rng:
            case range(start=begin, stop=end, step=step) as rng:
                if len(ts) < end:
                    sf._fill_ge(-1+end)
                ts_view = SeqSliceView(ts, rng)
                return ts_view
            case emay_j:
                if emay_j is ...:
                    return SeqView(ts)
                j = emay_j
                if not j < len(ts):
                    sf._fill_ge(j)
                return ts[j]
        raise 000

class DivmodOverPrimeList(_OverPrimeList):
    @classmethod
    def _mk_result_tuple_(cls, n, d, /):
        (q, r) = divmod(n, d)
        dqr = (d, q, r)
        return dqr
class ModOverPrimeList(_OverPrimeList):
    @classmethod
    def _mk_result_tuple_(cls, n, d, /):
        r = n%d
        dr = (d, r)
        return dr






__all__
from seed.math.prime_sieve.PrimeList import PrimeList, DivmodOverPrimeList, ModOverPrimeList
from seed.math.prime_sieve.PrimeList import *
