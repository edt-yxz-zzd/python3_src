#__all__:goto
r'''[[[
e ../../python3_src/seed/math/primality_test/reproduceable7probable_primes.py

seed.math.primality_test.reproduceable7probable_primes
py -m nn_ns.app.debug_cmd   seed.math.primality_test.reproduceable7probable_primes -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.primality_test.reproduceable7probable_primes:__doc__ -ht # -ff -df
#######

[[
come_from:
e ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method.py
]]


'#'; __doc__ = r'#'
>>> Reproduceable7SPRP_2357(-999, 17)
Reproduceable7SPRP_2357(2, 17)
>>> [*iter_pairs4reproduceable_(Reproduceable7SPRP_2357(-999, 17))]
[(2, Reproduceable7SPRP_2357(3, 17)), (3, Reproduceable7SPRP_2357(5, 17)), (5, Reproduceable7SPRP_2357(7, 17)), (7, Reproduceable7SPRP_2357(9, 17)), (11, Reproduceable7SPRP_2357(13, 17)), (13, Reproduceable7SPRP_2357(15, 17)), (17, Reproduceable7SPRP_2357(19, 17))]

>>> Reproduceable7probable_primes(-999, 17)
Reproduceable7probable_primes(2, 17)
>>> [*iter_pairs4reproduceable_(Reproduceable7probable_primes(-999, 17))]
[(2, Reproduceable7probable_primes(3, 17)), (3, Reproduceable7probable_primes(5, 17)), (5, Reproduceable7probable_primes(7, 17)), (7, Reproduceable7probable_primes(9, 17)), (11, Reproduceable7probable_primes(13, 17)), (13, Reproduceable7probable_primes(15, 17)), (17, Reproduceable7probable_primes(19, 17))]

>>> Reproduceable7primes(-999, 17)
Reproduceable7primes(2, 17)
>>> [*iter_pairs4reproduceable_(Reproduceable7primes(-999, 17))]
[(2, Reproduceable7primes(3, 17)), (3, Reproduceable7primes(5, 17)), (5, Reproduceable7primes(7, 17)), (7, Reproduceable7primes(9, 17)), (11, Reproduceable7primes(13, 17)), (13, Reproduceable7primes(15, 17)), (17, Reproduceable7primes(19, 17))]








>>> from itertools import islice
>>> Reproduceable7probable_primes(is_prime__le_pow2_81_.upperbound, -1)
Reproduceable7probable_primes(3317044064679887385962123, -1)
>>> [*islice(iter_pairs4reproduceable_(Reproduceable7probable_primes(is_prime__le_pow2_81_.upperbound, -1)), 0, 2)]
[(3317044064679887385962123, Reproduceable7probable_primes(3317044064679887385962125, -1)), (3317044064679887385962177, Reproduceable7probable_primes(3317044064679887385962179, -1))]



>>> Reproduceable7primes(is_prime__le_pow2_81_.upperbound, -1)
Traceback (most recent call last):
    ...
TypeError: -1
>>> Reproduceable7primes(is_prime__le_pow2_81_.upperbound-1, is_prime__le_pow2_81_.upperbound)
Traceback (most recent call last):
    ...
TypeError: 3317044064679887385962123
>>> Reproduceable7primes(is_prime__le_pow2_81_.upperbound-1, is_prime__le_pow2_81_.upperbound-1)
Reproduceable7primes(3317044064679887385962123, 3317044064679887385962122)
>>> [*iter_pairs4reproduceable_(Reproduceable7primes(is_prime__le_pow2_81_.upperbound-1, is_prime__le_pow2_81_.upperbound-1))]
[]
>>> [*iter_pairs4reproduceable_(Reproduceable7primes(is_prime__le_pow2_81_.upperbound-1-308, is_prime__le_pow2_81_.upperbound-1))]
[]
>>> [*iter_pairs4reproduceable_(Reproduceable7primes(is_prime__le_pow2_81_.upperbound-1-309, is_prime__le_pow2_81_.upperbound-1))]
[(3317044064679887385961813, Reproduceable7primes(3317044064679887385961815, 3317044064679887385962122))]





>>> sm77 = mk_Reproduceable7dup_xprimes_(7, 7)
>>> sm79 = mk_Reproduceable7dup_xprimes_(7, 9)
>>> sm77
Reproduceable7dup_xprimes(7, 7, None, Reproduceable7primes(2, 7))
>>> [*iter_fsts4reproduceable_(sm77)]
[2, 2, 3, 5, 7]
>>> sm79
Reproduceable7dup_xprimes(7, 9, None, Reproduceable7primes(2, 7))
>>> [*iter_fsts4reproduceable_(sm79)]
[2, 2, 2, 3, 3, 5, 7]







>>> mk_Reproduceable7xprimes_(10)
Reproduceable7primes(2, 10)
>>> mk_Reproduceable7xprimes_(10, case=None)
Reproduceable7primes(2, 10)
>>> mk_Reproduceable7xprimes_(10, case=1)
Reproduceable7primes(2, 10)
>>> mk_Reproduceable7xprimes_(10, case=2357)
Reproduceable7SPRP_2357(2, 10)
>>> mk_Reproduceable7xprimes_(10, case=0)
Reproduceable7probable_primes(2, 10)
>>> mk_Reproduceable7xprimes_(10, case=2)
Reproduceable5seq(PrimeList7ge_lt(0, 11), 0)

>>> mk_Reproduceable7xprimes_(10, min4xprime=4)
Reproduceable7primes(5, 10)
>>> mk_Reproduceable7xprimes_(10, min4xprime=43)
Reproduceable7primes(43, 10)
>>> mk_Reproduceable7xprimes_(44, min4xprime=43)
Reproduceable7primes(43, 44)

>>> mk_Reproduceable7xprimes_(10, case=0, min4xprime=4)
Reproduceable7probable_primes(5, 10)
>>> mk_Reproduceable7xprimes_(10, case=0, min4xprime=43)
Reproduceable7probable_primes(43, 10)
>>> mk_Reproduceable7xprimes_(44, case=0, min4xprime=43)
Reproduceable7probable_primes(43, 44)

>>> mk_Reproduceable7xprimes_(10, case=1, min4xprime=4)
Reproduceable7primes(5, 10)
>>> mk_Reproduceable7xprimes_(10, case=1, min4xprime=43)
Reproduceable7primes(43, 10)
>>> mk_Reproduceable7xprimes_(44, case=1, min4xprime=43)
Reproduceable7primes(43, 44)

>>> mk_Reproduceable7xprimes_(10, case=2, min4xprime=4)
Reproduceable5seq(PrimeList7ge_lt(4, 11), 0)
>>> mk_Reproduceable7xprimes_(10, case=2, min4xprime=43)
Reproduceable5seq(PrimeList7ge_lt(43, 11), 0)
>>> mk_Reproduceable7xprimes_(44, case=2, min4xprime=43)
Reproduceable5seq(PrimeList7ge_lt(43, 45), 0)

>>> mk_Reproduceable7xprimes_(10, case=2357, min4xprime=4)
Reproduceable7SPRP_2357(5, 10)

>>> sm99_0 = mk_Reproduceable7dup_xprimes_(9, 9, case=0)
>>> sm99_1 = mk_Reproduceable7dup_xprimes_(9, 9, case=1)
>>> sm99_2 = mk_Reproduceable7dup_xprimes_(9, 9, case=2)
>>> sm99_0
Reproduceable7dup_xprimes(9, 9, None, Reproduceable7probable_primes(2, 9))
>>> sm99_1
Reproduceable7dup_xprimes(9, 9, None, Reproduceable7primes(2, 9))
>>> sm99_2
Reproduceable7dup_xprimes(9, 9, None, Reproduceable5seq(PrimeList7ge_lt(0, 10), 0))

>>> [*iter_fsts4reproduceable_(sm99_0)]
[2, 2, 2, 3, 3, 5, 7]
>>> [*iter_fsts4reproduceable_(sm99_1)]
[2, 2, 2, 3, 3, 5, 7]
>>> [*iter_fsts4reproduceable_(sm99_2)]
[2, 2, 2, 3, 3, 5, 7]



mk_Reproduceable7dup_xprimes__ver2_
>>> sm99_0 = mk_Reproduceable7dup_xprimes__ver2_(9, 9, case=0)
>>> sm99_1 = mk_Reproduceable7dup_xprimes__ver2_(9, 9, case=1)
>>> sm99_2 = mk_Reproduceable7dup_xprimes__ver2_(9, 9, case=2)
>>> sm99_0
mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 0)
>>> sm99_1
mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 1)
>>> sm99_2
mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 2)

>>> [*iter_fsts4reproduceable_(sm99_0)]
[2, 2, 2, 3, 3, 5, 7]
>>> [*iter_fsts4reproduceable_(sm99_1)]
[2, 2, 2, 3, 3, 5, 7]
>>> [*iter_fsts4reproduceable_(sm99_2)]
[2, 2, 2, 3, 3, 5, 7]


>>> ls0 = [*iter_pairs4reproduceable_(sm99_0)]
>>> ls1 = [*iter_pairs4reproduceable_(sm99_1)]
>>> ls2 = [*iter_pairs4reproduceable_(sm99_2)]

>>> for x in ls0:print(x)
(2, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 0, mid_args = ((2, 2), (0, Reproduceable7probable_primes(3, 9)))))
(2, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 0, mid_args = ((2, 1), (0, Reproduceable7probable_primes(3, 9)))))
(2, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 0, mid_args = ((2, 0), (0, Reproduceable7probable_primes(3, 9)))))
(3, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 0, mid_args = ((3, 1), (0, Reproduceable7probable_primes(5, 9)))))
(3, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 0, mid_args = ((3, 0), (0, Reproduceable7probable_primes(5, 9)))))
(5, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 0, mid_args = ((5, 0), (0, Reproduceable7probable_primes(7, 9)))))
(7, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 0, mid_args = ((7, 0), (0, Reproduceable7probable_primes(9, 9)))))
>>> for x in ls1:print(x)
(2, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 1, mid_args = ((2, 2), (1, Reproduceable7primes(3, 9)))))
(2, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 1, mid_args = ((2, 1), (1, Reproduceable7primes(3, 9)))))
(2, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 1, mid_args = ((2, 0), (1, Reproduceable7primes(3, 9)))))
(3, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 1, mid_args = ((3, 1), (1, Reproduceable7primes(5, 9)))))
(3, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 1, mid_args = ((3, 0), (1, Reproduceable7primes(5, 9)))))
(5, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 1, mid_args = ((5, 0), (1, Reproduceable7primes(7, 9)))))
(7, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 1, mid_args = ((7, 0), (1, Reproduceable7primes(9, 9)))))
>>> for x in ls2:print(x)
(2, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 2, mid_args = ((2, 2), (2, Reproduceable5seq(PrimeList7ge_lt(0, 10), 1)))))
(2, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 2, mid_args = ((2, 1), (2, Reproduceable5seq(PrimeList7ge_lt(0, 10), 1)))))
(2, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 2, mid_args = ((2, 0), (2, Reproduceable5seq(PrimeList7ge_lt(0, 10), 1)))))
(3, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 2, mid_args = ((3, 1), (2, Reproduceable5seq(PrimeList7ge_lt(0, 10), 2)))))
(3, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 2, mid_args = ((3, 0), (2, Reproduceable5seq(PrimeList7ge_lt(0, 10), 2)))))
(5, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 2, mid_args = ((5, 0), (2, Reproduceable5seq(PrimeList7ge_lt(0, 10), 3)))))
(7, mk_Reproduceable7dup_xprimes__ver2_(9, 9, case = 2, mid_args = ((7, 0), (2, Reproduceable5seq(PrimeList7ge_lt(0, 10), 4)))))


#test:_repr7ver2:
>>> f = lambda rp:eval(repr(rp))
>>> for _, rp in ls0:print([*iter_fsts4reproduceable_(f(rp))])
[2, 2, 3, 3, 5, 7]
[2, 3, 3, 5, 7]
[3, 3, 5, 7]
[3, 5, 7]
[5, 7]
[7]
[]
>>> for _, rp in ls1:print([*iter_fsts4reproduceable_(f(rp))])
[2, 2, 3, 3, 5, 7]
[2, 3, 3, 5, 7]
[3, 3, 5, 7]
[3, 5, 7]
[5, 7]
[7]
[]
>>> for _, rp in ls2:print([*iter_fsts4reproduceable_(f(rp))])
[2, 2, 3, 3, 5, 7]
[2, 3, 3, 5, 7]
[3, 3, 5, 7]
[3, 5, 7]
[5, 7]
[7]
[]

















py_adhoc_call   seed.math.primality_test.reproduceable7probable_primes   @f
]]]'''#'''
__all__ = r'''
Reproduceable7SPRP_2357
Reproduceable7probable_primes
Reproduceable7primes


mk_Reproduceable7dup_xprimes__ver2_
mk_Reproduceable7dup_xprimes_
    mk_Reproduceable7xprimes_
    Reproduceable7dup_xprimes



'''.split()#'''
    #Reproduceable7bounded_smooth7xprimes-->Reproduceable7dup_xprimes
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.types.Reproduceable import IReproduceable
from seed.types.Reproduceable import NextEx, StopEx, ResultTypes4xnext
from seed.types.Reproduceable import iter_pairs4reproduceable_, iter_fsts4reproduceable_, iter_snds4reproduceable_
from seed.types.Reproduceable import Reproduceable5seq, Reproduceable7chain5reproduceable, Reproduceable7fmap, Reproduceable7repeat, Reproduceable7customized_repr#, Reproduceable7chain5iterable, Reproduceable7transform, Reproduceable7rdiff, Reproduceable7foldl
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
    from seed.math.primality_test.strong_probable_prime import is_prime__le_pow2_81_#.upperbound
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.primality_test.SPRP_2357 import next_SPRP_2357__ge_
    from seed.math.primality_test.strong_probable_prime import next_probable_prime__ge_, next_may_prime__le_pow2_81__ge_
    from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_int_ge_lt, check_int_ge_le, check_uint_lt, check_may_
    from seed.helper.repr_input import repr_helper, repr_helper__str
    from seed.types.CachedProperty import CachedProperty
    from seed.math.floor_ceil_tools.fc_log import floor_log_
    from seed.math.prime_sieve.PrimeList import PrimeList7ge_lt
        #PrimeList7ge_lt+Reproduceable5seq
    from seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N import KthRoots4N
#.#################################
___end_mark_of_excluded_global_names__0___ = ...
r'''[[[
[[
KthRoots4N
move_to:
view ../../python3_src/seed/math/floor_ceil_tools/fc_kth_root__7KthRoots4N.py
]]
#]]]'''#'''
class _IReproduceable7xprimes(IReproduceable):
    ___no_slots_ok___ = True
    @property
    @abstractmethod
    def _imay_upperbound_(sf, /):
        '-> imay uint'
        return -1
        return 1+2**81
        return is_prime__le_pow2_81_.upperbound
    @abstractmethod
    def _next_may_xprime_(sf, min_u, /):
        'uint -> may xprime'
        return next_probable_prime__ge_(min_u)
        return next_may_prime__le_pow2_81__ge_(min_u)

    #.@classmethod
    #.def mk5min_and_imay_max_(cls, min_u, imay_max_u, /):
    #.    return cls(min_u, imay_max_u)
    def mk5new_min_(sf, min_u, /):
        cls = type(sf)
        #.ot = cls.mk5min_and_imay_max_(min_u, sf.imay_max_u)
        ot = cls(min_u, sf.imay_max_u)
        return ot
    def __init__(sf, min_u, imay_max_u, /):
        if not -1 == (upperbound:=sf._imay_upperbound_):
            #check_int_ge_lt(-1, upperbound, imay_max_u)
            #if imay_max_u == -1:raise ValueError
            max_u = imay_max_u
            check_int_ge_lt(0, upperbound, max_u)
        else:
            check_int_ge(-1, imay_max_u)
        check_type_is(int, min_u)
        min_u = max(2, min_u)
        min_u = 2 if min_u <= 2 else (1|min_u)
        sf._im = imay_max_u
        sf._u = min_u
    def __repr__(sf, /):
        return repr_helper(sf, sf.min_u, sf.imay_max_u)
    @property
    def min_u(sf, /):
        return sf._u
    @property
    def imay_max_u(sf, /):
        return sf._im
    @CachedProperty
    def _may_xprime_(sf, /):
        #.imay_max_u = sf._im
        #.min_u = sf._u
        imay_max_u = sf.imay_max_u
        min_u = sf.min_u
        if not -1 == (max_u:=imay_max_u):
            if not min_u <= max_u:
                may_xprime = None
            else:
                may_xprime = sf._next_may_xprime_(min_u)
                if not None is (xprime:=may_xprime) and not xprime <= max_u:
                    may_xprime = None
        else:
            may_xprime = sf._next_may_xprime_(min_u)
            if None is may_xprime:raise 000
        return may_xprime
    @override
    def ___xnext4reproduceable___(sf, /):
        may_xprime = sf._may_xprime_
        if not None is (xprime:=may_xprime):
            ot = sf.mk5new_min_((1+xprime))
            return NextEx(xprime, ot)
        imay_max_u = sf.imay_max_u
        return StopEx(imay_max_u)
#end-class _IReproduceable7xprimes(IReproduceable):
class Reproduceable7SPRP_2357(_IReproduceable7xprimes):
    #@override
    _imay_upperbound_ = -1
    @override
    def _next_may_xprime_(sf, min_u, /):
        'uint -> may xprime'
        return next_SPRP_2357__ge_(min_u)

class Reproduceable7probable_primes(_IReproduceable7xprimes):
    #@override
    _imay_upperbound_ = -1
    @override
    def _next_may_xprime_(sf, min_u, /):
        'uint -> may xprime'
        return next_probable_prime__ge_(min_u)
class Reproduceable7primes(_IReproduceable7xprimes):
    def __init__(sf, min_u, max_u, /):
        super().__init__(min_u, max_u)
    @property
    @override
    def _imay_upperbound_(sf, /):
        u = is_prime__le_pow2_81_.upperbound
        __class__._imay_upperbound_ = u
        return u
    @override
    def _next_may_xprime_(sf, min_u, /):
        'uint -> may xprime'
        return next_may_prime__le_pow2_81__ge_(min_u)


class Reproduceable7dup_xprimes(IReproduceable):
    ___no_slots_ok___ = True
    #.@classmethod
    #.def mk5maxbounds_and_repeat_status_(cls, max4xprime, max4xprime_power, may___xprime__max_exp__exp, reproduceable7xprimes, /):
    #.    return cls(max4xprime, max4xprime_power, may___xprime__max_exp__exp, reproduceable7xprimes)
    def mk5new_repeat_status_(sf, may___xprime__max_exp__exp, reproduceable7xprimes, /):
        max4xprime = sf.max4xprime
        max4xprime_power = sf.max4xprime_power
        kth_roots4max4xprime_power = sf._rs4B1b
        cls = type(sf)
        #ot = cls.mk5maxbounds_and_repeat_status_(max4xprime, max4xprime_power, may___xprime__max_exp__exp, reproduceable7xprimes)
        ot = cls(max4xprime, max4xprime_power, may___xprime__max_exp__exp, reproduceable7xprimes, may_kth_roots4max4xprime_power=kth_roots4max4xprime_power)
        return ot
    def __init__(sf, max4xprime, max4xprime_power, may___xprime__max_exp__exp, reproduceable7xprimes, /, *, may_kth_roots4max4xprime_power=None):
        check_int_ge(2, max4xprime)
        check_int_ge(max4xprime, max4xprime_power)
        #check_type_le(_IReproduceable7xprimes, reproduceable7xprimes)
        check_type_le(IReproduceable, reproduceable7xprimes)
        if not None is (kth_roots4max4xprime_power:=may_kth_roots4max4xprime_power):
            check_type_is(KthRoots4N, kth_roots4max4xprime_power)
            if not kth_roots4max4xprime_power.the_N == max4xprime_power:raise ValueError(kth_roots4max4xprime_power, max4xprime_power)
        else:
            kth_roots4max4xprime_power = KthRoots4N(max4xprime_power)
        kth_roots4max4xprime_power

        if not None is may___xprime__max_exp__exp:
            xprime__max_exp__exp = may___xprime__max_exp__exp
            check_type_is(tuple, xprime__max_exp__exp)
            (xprime, max_exp, exp) = xprime__max_exp__exp
            check_int_ge_le(2, max4xprime, xprime)
            check_int_ge(1, max_exp)
            #check_int_ge_le(2, max_exp, exp)
            check_int_ge_le(1, max_exp, exp)
            # [2 <= xprime <= max4xprime <= max4xprime_power]
            # [max_exp == floor_log_(xprime; max4xprime_power)]
            # [1 <= exp <= max_exp]
            # [2 <= xprime <= xprime**exp <= xprime**max_exp <= max4xprime_power < xprime**(1+max_exp)]
        sf._B1a = max4xprime
        sf._B1b = max4xprime_power
        sf._rs4B1b = kth_roots4max4xprime_power
        sf._mt3 = may___xprime__max_exp__exp
        sf._8ps = reproduceable7xprimes
    @property
    def max4xprime(sf, /):
        return sf._B1a
    @property
    def max4xprime_power(sf, /):
        return sf._B1b
    @property
    def repeat_status(sf, /):
        mt3 = sf._mt3
        as_ps = sf._8ps
        return (mt3, as_ps)

    def __repr__(sf, /):
        max4xprime = sf.max4xprime
        max4xprime_power = sf.max4xprime_power
        (mt3, as_ps) = sf.repeat_status
        return repr_helper(sf, max4xprime, max4xprime_power, mt3, as_ps)
    @CachedProperty
    def _may_fixed_repeat_status_(sf, /):
        max4xprime = sf.max4xprime
        max4xprime_power = sf.max4xprime_power
        (mt3, as_ps) = sf.repeat_status
        match mt3:
            case None:
                ok = False
                for xprime, new_as_ps in iter_pairs4reproduceable_(as_ps):
                    ok = True
                    break
                if not (ok and xprime <= max4xprime):
                    return None
                check_int_ge_le(2, max4xprime, xprime)
                if 0:
                    max_exp = floor_log_(xprime, max4xprime_power)
                    #TODO:list_all_floor_kth_root_until_diff_lt_
                    #[kth_roots4max4xprime_power::KthRoots4N]
                else:
                    kth_roots4max4xprime_power = sf._rs4B1b
                    max_exp = kth_roots4max4xprime_power(xprime)
                max_exp
                exp = 1
            case (xprime, max_exp, exp):
                new_as_ps = as_ps
                pass
            case _:
                raise 000
        (xprime, max_exp, exp), new_as_ps
        return ((xprime, max_exp, exp), new_as_ps)
    @override
    def ___xnext4reproduceable___(sf, /):
        match sf._may_fixed_repeat_status_:
            case None:
                return StopEx(sf.max4xprime_power)
            case ((xprime, max_exp, exp), new_as_ps):
                new_mt3 = None if exp == max_exp else (xprime, max_exp, 1+exp)
                ot = sf.mk5new_repeat_status_(new_mt3, new_as_ps)
                return NextEx(xprime, ot)
        raise 000
def mk_Reproduceable7xprimes_(max4xprime, /, *, case=None, min4xprime=0):
    'max4xprime/uint -> *(kw:case/may uint%3/(0/probable_prime|1/prime|2/prime_seq)) -> IReproduceable{xprime}'
    #check_type_is(bool, probable_prime_vs_prime)
    if not case in [2357]:check_may_([check_uint_lt, 3], case)
    check_int_ge(2, max4xprime)
    check_int_ge(0, min4xprime)
    #T = Reproduceable7probable_primes if not probable_prime_vs_prime else Reproduceable7primes
    #as_ps = T(2, max4xprime)
    match case:
        case 0:
            T = Reproduceable7probable_primes
            as_ps = T(min4xprime, max4xprime)
        case 1|None:
            T = Reproduceable7primes
            as_ps = T(min4xprime, max4xprime)
        case 2:
            seq = PrimeList7ge_lt(min4xprime, 1+max4xprime)
            as_ps = Reproduceable5seq(seq, 0)
        case 2357:
            T = Reproduceable7SPRP_2357
            as_ps = T(min4xprime, max4xprime)
        case _:
            raise 000
    as_ps
    return as_ps
def mk_Reproduceable7dup_xprimes_(max4xprime, max4xprime_power, /, *, case=None):
    'max4xprime/uint -> max4xprime_power/uint -> *(kw:case/may uint%3/(0/probable_prime|1/prime|2/prime_seq)) -> Reproduceable7dup_xprimes{xprime}'
    #check_uint_lt(3, case)
    check_int_ge(2, max4xprime)
    check_int_ge(max4xprime, max4xprime_power)

    as_ps = mk_Reproduceable7xprimes_(max4xprime, case=case)
    #if not via_combine:
    mt3 = None
    as_ps7repeat = Reproduceable7dup_xprimes(max4xprime, max4xprime_power, mt3, as_ps)
    return as_ps7repeat
def mk_Reproduceable7dup_xprimes__ver2_(max4xprime, max4xprime_power, /, *, case=None, mid_args=()):
    'max4xprime/uint -> max4xprime_power/uint -> *(kw:case/may uint%3/(0/probable_prime|1/prime|2/prime_seq)) -> Reproduceable7dup_xprimes{xprime}'
    #check_uint_lt(3, case)
    check_int_ge(2, max4xprime)
    check_int_ge(max4xprime, max4xprime_power)

    match mid_args:
        case ():
            as_ps = mk_Reproduceable7xprimes_(max4xprime, case=case)
            may_head7repeat = None
        case ((xprime, exp7remain), (_case, as_ps)):
            if case is None:
                case = _case
            if not case == _case:raise ValueError(case, _case)
            as_ps
            may_head7repeat = Reproduceable7repeat(xprime, exp7remain)
        case _:
            raise TypeError(mid_args)
    may_head7repeat
    as_ps

    kth_roots4max4xprime_power = KthRoots4N(max4xprime_power)
    def xprime2repeats_(xprime, /, *, _floor_log_=kth_roots4max4xprime_power):
        # 7fmap:xprime -> Reproduceable7repeat(xprime, max_exp:=KthRoots4N(max4xprime_power)(xprime))
        return Reproduceable7repeat(xprime, _floor_log_(xprime))
    xprime2repeats_._xdata = (max4xprime, max4xprime_power, kth_roots4max4xprime_power, case)

    _as_ps7repeat = Reproduceable7chain5reproduceable(may_head7repeat, Reproduceable7fmap(xprime2repeats_, as_ps))
    as_ps7repeat = Reproduceable7customized_repr(_repr7ver2, _as_ps7repeat)
    return as_ps7repeat
def _extract_args7ver2(_as_ps7repeat, /):
    match _as_ps7repeat:
        case Reproduceable7chain5reproduceable(may_head_reproduceable=may_head_reproduceable, tail_reproduceable4reproduceable=Reproduceable7fmap(transform7fmap_=xprime2repeats_, reproduceable8input=as_ps)):
            match may_head_reproduceable:
                case None:
                    # [head be None => at beginning]
                    args4head = ()
                case Reproduceable7repeat(the_oresult=xprime, imay_size=exp7remain):
                    args4head = (xprime, exp7remain)
                case _:
                    raise 000
            #end-match may_head_reproduceable:
            args4head
            #kth_roots4max4xprime_power = xprime2repeats_.__kwdefaults__['_floor_log_']
            (max4xprime, max4xprime_power, kth_roots4max4xprime_power, case) = xprime2repeats_._xdata
            #max4xprime_power = kth_roots4max4xprime_power.the_N
            args7extract = (args4head, (max4xprime, max4xprime_power, kth_roots4max4xprime_power, xprime2repeats_), (case, as_ps))
            return args7extract
        case _:
            raise 000
    raise 000
_extract_args7ver2

def _repr7ver2(_as_ps7repeat, /):
    args7extract = _extract_args7ver2(_as_ps7repeat)
    (args4head, (max4xprime, max4xprime_power, kth_roots4max4xprime_power, xprime2repeats_), (case, as_ps)) = args7extract
    if not args4head:
        mid_args = ()
        case
    else:
        (xprime, exp7remain) = args4head
        mid_args = ((xprime, exp7remain), (case, as_ps))
        case
    mid_args
    case

    kwds = {}
    if not case is None:
        kwds['case'] = case
    if mid_args:
        kwds['mid_args'] = mid_args
    return repr_helper__str(mk_Reproduceable7dup_xprimes__ver2_.__name__, max4xprime, max4xprime_power, **kwds)
_repr7ver2





__all__
from seed.math.primality_test.reproduceable7probable_primes import Reproduceable7primes, Reproduceable7probable_primes, Reproduceable7SPRP_2357
from seed.math.primality_test.reproduceable7probable_primes import mk_Reproduceable7dup_xprimes_, mk_Reproduceable7xprimes_, Reproduceable7dup_xprimes
from seed.math.primality_test.reproduceable7probable_primes import mk_Reproduceable7dup_xprimes__ver2_
from seed.math.primality_test.reproduceable7probable_primes import *
