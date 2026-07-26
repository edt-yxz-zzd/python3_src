#__all__:goto
r'''[[[
e ../../python3_src/seed/math/prime_sieve/primes_ge_lt.py

seed.math.prime_sieve.primes_ge_lt
py -m nn_ns.app.debug_cmd   seed.math.prime_sieve.primes_ge_lt -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.prime_sieve.primes_ge_lt:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> list_primes__ge_lt_(2**100, 50+2**100)
Traceback (most recent call last):
    ...
ValueError: 1267650600228229401496703205426
>>> list_primes__ge_lt_(2**79, 50+2**79) # iter_filter4primes_ge_lt_
(604462909807314587353111, 604462909807314587353117)
>>> list_primes__ge_lt_(480, 500) # iter_filter4primes_ge_lt_
(487, 491, 499)
>>> list_primes__ge_lt_(40, 50) # iter_sieve4primes_ge_lt_
(41, 43, 47)
>>> list_primes__ge_lt_(2, 50) # list_primes__lt_
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
>>> list_primes__ge_lt_(-999, -666) # none
()



>>> [*iter_sieve4primes_ge_lt_(480, 500)]
Traceback (most recent call last):
    ...
TypeError: (480, 500)
>>> [*iter_sieve4primes_ge_lt_(40, 50)]
[41, 43, 47]
>>> [*iter_sieve4primes_ge_lt_(2, 4)]
[2, 3]
>>> [*iter_sieve4primes_ge_lt_(2, 3)]
[2]

Traceback (most recent call last):
    ...
TypeError: (2, 3)
>>> [*iter_sieve4primes_ge_lt_(2, 2)]
[]






py_adhoc_call   seed.math.prime_sieve.primes_ge_lt   @f
]]]'''#'''
__all__ = r'''
list_primes__ge_lt_
    iter_primes__ge_lt_
        iter_filter4primes_ge_lt_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
    from seed.math.primality_test.strong_probable_prime import is_prime__le_pow2_81_#.upperbound
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.math.prime_sieve.sieve_lt import list_primes__lt_
    from seed.math.prime_sieve.sieve_ge_le import iter_sieve4primes_ge_lt_ # ^(TypeError|ValueError) if [(min_u,max1_u) too near] # iter_best_interval5big_interval6args4sieve_interval_
    from seed.math.primality_test.strong_probable_prime import iter_probable_primes__ge_lt_#iter_primes__ge_lt_{#not check max at start#}
    from seed.math.prime_sieve.sieve_ge_le import sieve_interval4primes__ge_lt, check_args4sieve_interval__ge_lt

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def iter_filter4primes_ge_lt_(min_u, max1_u, /, *, reverse=False):
    '-> Iter prime | ^ValueError if [max1_u too big]'
    check_type_is(int, min_u)
    check_type_is(int, max1_u)
    min_u = max(2, min_u)
    max1_u = max(min_u, max1_u)
    if not min_u < max1_u:
        it = iter('')
    else:
        if not max1_u <= is_prime__le_pow2_81_.upperbound:raise ValueError(max1_u)
            # ^ValueError if [max1_u too big]
        it = iter_probable_primes__ge_lt_(min_u, max1_u, reverse=reverse)
    it
    return it
def iter_primes__ge_lt_(min_u, max1_u, /, *, reverse=False):
    '-> Iter prime | ^ValueError if [max1_u too big]'
    #'-> Iter prime | ^ValueError if [[(min_u,max1_u) too near][max1_u too big]]'
    (ok, min_u, max1_u) = _prepare7rng_(min_u, max1_u)
    # [2 <= min_u <= max1_u]
    # [not ok] => [min_u > 2][(min_u,max1_u) too near]
    if not min_u < max1_u or max1_u <= 2:
        it = iter('')
    elif ok:
        it = iter_sieve4primes_ge_lt_(min_u, max1_u, reverse=reverse)
            # no:Exception
    else:
        # [min_u > 2][(min_u,max1_u) too near]
        it = iter_filter4primes_ge_lt_(min_u, max1_u, reverse=reverse)
            # ^ValueError if [max1_u too big]
    it
    return it
def _prepare7rng_(min_u, max1_u, /):
    check_type_is(int, min_u)
    check_type_is(int, max1_u)
    min_u = max(2, min_u)
    max1_u = max(min_u, max1_u)
    # [2 <= min_u <= max1_u]
    if not min_u < max1_u or max1_u <= 2:
        ok = True
    else:
        ok = min_u == 2 or _is_good_rng_(min_u, max1_u)
    # [not ok] => [min_u > 2][(min_u,max1_u) too near]
    return (ok, min_u, max1_u)
def _is_good_rng_(min_u, max1_u, /):
    # precondition:[2 <= min_u <= max1_u]
    try:
        check_args4sieve_interval__ge_lt(min_u, max1_u)
            #^TypeError if not (max1_u-min_u)**2 >= -1+max1_u >= min_u
    except (TypeError, ValueError):
        # [not [(max1_u-min_u)**2 >= -1+max1_u >= min_u]]
        # !! [2 <= min_u <= max1_u]
        # [not [(max1_u-min_u)**2 >= -1+max1_u]]
        # [(min_u,max1_u) too near]
        ok = False
    else:
        ok = True
    # [not ok] => [(min_u,max1_u) too near]
    return ok
def list_primes__ge_lt_(min_u, max1_u, /, *, _mk=tuple):
    '-> [prime] | ^ValueError if [max1_u too big]'
    #'-> [prime] | ^ValueError if [[(min_u,max1_u) too near][max1_u too big]]'
    (ok, min_u, max1_u) = _prepare7rng_(min_u, max1_u)
    # [2 <= min_u <= max1_u]
    # [not ok] => [min_u > 2][(min_u,max1_u) too near]
    if not min_u < max1_u or max1_u <= 2:
        ps = _mk('')
    elif min_u <= 2:
        ps = list_primes__lt_(max1_u, _mk=_mk)
    elif ok:
        ps = sieve_interval4primes__ge_lt(min_u, max1_u)
        if not _mk is type(ps):
            ps = _mk(ps)
        ps
    else:
        # [min_u > 2][(min_u,max1_u) too near]
        #f = iter_primes__ge_lt_
        f = iter_filter4primes_ge_lt_
        ps = _mk(f(min_u, max1_u, reverse=False))
    ps
    return ps



__all__
from seed.math.prime_sieve.primes_ge_lt import list_primes__ge_lt_, iter_primes__ge_lt_, iter_filter4primes_ge_lt_
from seed.math.prime_sieve.primes_ge_lt import *
