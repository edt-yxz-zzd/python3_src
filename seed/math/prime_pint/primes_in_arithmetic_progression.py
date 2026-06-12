#__all__:goto
r'''[[[
e ../../python3_src/seed/math/prime_pint/primes_in_arithmetic_progression.py

seed.math.prime_pint.primes_in_arithmetic_progression
py -m nn_ns.app.debug_cmd   seed.math.prime_pint.primes_in_arithmetic_progression -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.prime_pint.primes_in_arithmetic_progression:__doc__ -ht # -ff -df
#######

[[
page265[290/567]
Primes in Arithmetic Progression
[@[b,d::int] -> [b =!= 0] -> [d >= 1] -> [gcd(b,d) == 1] -> [+oo == len{p | [[p::prime][(p-b)%d == 0]]}]]
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.prime_pint.primes_in_arithmetic_progression   @list.9:iter_primes_in_arithmetic_progression__using_primality_test7strong_probable_prime_  =8  =3
    [11, 17, 23, 29, 41, 47, 53, 59, 71]

py_adhoc_call   seed.math.prime_pint.primes_in_arithmetic_progression   @list.9:iter_primes_in_arithmetic_progression__using_primality_test7strong_probable_prime_  =3  =6
    ValueError: ('not coprime', 3, 6)
py_adhoc_call   seed.math.prime_pint.primes_in_arithmetic_progression   @list.9:iter_primes_in_arithmetic_progression__using_primality_test7strong_probable_prime_  =3  =5
    [3, 13, 23, 43, 53, 73, 83, 103, 113]
py_adhoc_call   seed.math.prime_pint.primes_in_arithmetic_progression   @list.9:iter_primes_in_arithmetic_progression__using_primality_test7strong_probable_prime_  =3  =4
    [3, 7, 11, 19, 23, 31, 43, 47, 59]

py_adhoc_call   seed.math.prime_pint.primes_in_arithmetic_progression   @list.9:iter_primes_in_arithmetic_progression__using_primality_test7strong_probable_prime_  =1  =1
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
py_adhoc_call   seed.math.prime_pint.primes_in_arithmetic_progression   @list.9:iter_primes_where_step_divs_phiP__using_primality_test7factorization4Pmm_  =1  =1 =None
    [2, 3, 5, 7, 11, 13, 17, 19, 23]
py_adhoc_call   seed.math.prime_pint.primes_in_arithmetic_progression   @list.9:iter_primes_where_step_divs_phiP__using_primality_test7factorization4Pmm_  =1  =2 =None
    [3, 5, 7, 11, 13, 17, 19, 23, 29]
py_adhoc_call   seed.math.prime_pint.primes_in_arithmetic_progression   @list.9:iter_primes_where_step_divs_phiP__using_primality_test7factorization4Pmm_  =1  =4 =None
    [5, 13, 17, 29, 37, 41, 53, 61, 73]
py_adhoc_call   seed.math.prime_pint.primes_in_arithmetic_progression   @list.9:iter_primes_where_step_divs_phiP__using_primality_test7factorization4Pmm_  =1  =4 =None +with_factorization4Pmm
    [(5, {2: 2}), (13, {2: 2, 3: 1}), (17, {2: 4}), (29, {2: 2, 7: 1}), (37, {2: 2, 3: 2}), (41, {2: 3, 5: 1}), (53, {2: 2, 13: 1}), (61, {2: 2, 3: 1, 5: 1}), (73, {2: 3, 3: 2})]

]]]'''#'''
__all__ = r'''
iter_primes_in_arithmetic_progression__using_primality_test7strong_probable_prime_
iter_primes_where_step_divs_phiP__using_primality_test7factorization4Pmm_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
#.from seed.helper.lazy_import__func7dict import lazy_import__funcs7dict_
#.(check_type_is, check_int_ge, _ifNone) = lazy_import__funcs7dict_(__name__ or globals() or locals(), 'seed.tiny_.check',  'check_type_is, check_int_ge      ifNone:_ifNone')
#.#################################
#.def mk_context4lazy_import_registered_names_(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject={}, may_bifix4lazy_name7import=None, lazy_name7importZoriginal_name7import={}):
#.from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
#.with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
#.    from seed._lazy_ import print_err, fst, echo, ifNone
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.prime_sieve.sieve_ge_le import iter_sieve4primes_ge_lt_, iter_sieve4prime_factorizations_ge_lt_
    from seed.math.is_prime__via_complete_factorization_Nmm_ import is_prime__via_complete_factorization_Nmm_
    #def is_prime__via_complete_factorization_Nmm_(p2e4Nmm_or_ps4Nmm, N, /):
    from seed.math.prepare_p2e4N import prepare_p2e4N_, mul7p2e_
    from seed.math.primality_test.strong_probable_prime import prime_filter__using_primality_test_
    from seed.math.floor_ceil_tools.fc_div import ceil_div_
    from seed.tiny_.check import check_type_is, check_int_ge
    from itertools import count, chain
    from math import gcd
#.    from functools import cached_property
#.    from seed.for_libs.for_functools.cached_property import cached_property
#.    from seed.types.CachedProperty import CachedProperty, mk_cached_propertyT_
#.    from seed.func_tools.dot2 import dot
#.with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
#.    from seed.data_funcs.lnkls import rglnkls_ops# empty_rglnkls, mk_empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def _prepare_(begin, step, /):
    check_type_is(int, begin)
    check_int_ge(1, step)
    # [step >= 1]
    if begin < 2:
        begin += step*ceil_div_(step, 2-begin)
        assert begin -step < 2 <= begin
    assert begin >= 2
    # [begin >= 2]

    # [step >= 1]
    # [begin >= 2]
    if not gcd(begin, step) == 1:raise ValueError('not coprime', begin, step)

    hs = []
    if begin&1 == 0:
        # [begin%2 == 0]
        # [step%2 == 1]
        if begin == 2:
            hs = [begin]
        begin += step
        # [begin%2 == 1]
    else:
        # [begin%2 == 1]
        pass
    # [begin%2 == 1]
    # [begin >= 3]
    assert begin&1

    if step&1:
        # [step%2 == 1]
        # [begin%2 == 1]
        # [begin >= 3]
        # [step >= 1]
        step <<= 1
        # [step%2 == 0]
    else:
        # [step%2 == 0]
        pass
    # [step%2 == 0]
    # [step >= 2]


    # [step%2 == 0]
    # [begin%2 == 1]
    # [step >= 2]
    # [begin >= 3]
    # [hs == [2]or[]]
    return (hs, begin, step)

def iter_primes_in_arithmetic_progression__using_primality_test7strong_probable_prime_(begin, step, /):
    #if step == 1:
    #    ps = iter_sieve4primes_ge_lt_(begin, None)
    (hs, begin, step) = _prepare_(begin, step)
    # [step%2 == 0]
    # [begin%2 == 1]
    # [step >= 2]
    # [begin >= 3]
    # [hs == [2]or[]]

    us = count(begin, step)
    if hs:
        us = chain(hs, us)
    del hs
    ps = prime_filter__using_primality_test_(us)

    return ps

def iter_primes_where_step_divs_phiP__using_primality_test7factorization4Pmm_(begin, step, may_p2e4step_or_ps4step_or_factor_pint_func, /, *, with_factorization4Pmm=False):
    # view ../../python3_src/seed/math/prime_pint/iter_primes_where_phiP_divs_.py
    old_step = step
    (hs, begin, step) = _prepare_(begin, step)
    # [step%2 == 0]
    # [begin%2 == 1]
    # [step >= 2]
    # [begin >= 3]
    # [hs == [2]or[]]
    if not begin%step == 1:raise ValueError('step not divs (P-1)')
    p2e4step = prepare_p2e4N_(old_step, may_p2e4step_or_ps4step_or_factor_pint_func)
    if not step == old_step:
        assert step == old_step<<1
        assert old_step&1
        p2e4step[2] = 1

    if hs:
        assert old_step == 1
        assert hs == [2]
        yield 2 if not with_factorization4Pmm else (2, {})
        del hs
    if step == 2:
        if not with_factorization4Pmm:
            it = iter_sieve4prime_factorizations_ge_lt_(begin, None, Pmm_only=True)
            yield from ((1+Nmm, p2e4Nmm) for (Nmm, p2e4Nmm) in it)
        else:
            yield from iter_sieve4primes_ge_lt_(begin, None)
    else:
        k = begin//step
        Nmm = begin-1 -step
        for (k, p2e4k) in iter_sieve4prime_factorizations_ge_lt_(k, None, with_uint=True):
            Nmm += step
            # [Nmm == k*step >= begin-1]
            #bug:p2e4Nmm = {**p2e4k, **p2e4step}
            p2e4Nmm = mul7p2e_(p2e4k, p2e4step)
            N = 1+Nmm
            if is_prime__via_complete_factorization_Nmm_(p2e4Nmm, N):
                yield N if not with_factorization4Pmm else (N, p2e4Nmm)


__all__
from seed.math.prime_pint.primes_in_arithmetic_progression import iter_primes_in_arithmetic_progression__using_primality_test7strong_probable_prime_
from seed.math.prime_pint.primes_in_arithmetic_progression import iter_primes_where_step_divs_phiP__using_primality_test7factorization4Pmm_
from seed.math.prime_pint.primes_in_arithmetic_progression import *
