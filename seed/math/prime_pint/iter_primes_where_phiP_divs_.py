#__all__:goto
r'''[[[
e ../../python3_src/seed/math/prime_pint/iter_primes_where_phiP_divs_.py

seed.math.prime_pint.iter_primes_where_phiP_divs_
py -m nn_ns.app.debug_cmd   seed.math.prime_pint.iter_primes_where_phiP_divs_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.prime_pint.iter_primes_where_phiP_divs_:__doc__ -ht # -ff -df

grep phi -r ../../python3_src/seed/math/ -l | grep '\.py$'
[[
[L:<-[0..]][ps::[prime]{len=L}][es::[int{>0}]{len=L}][N:=II[ps[i]**es[i] | [i:<-[0..<L]]]]:
    [max_order_mod_(N) == lcm[(ps[i]-1)*ps[i]**(es[i]-(if ps[i]==2 and es[i]>=3 then 2 else 1)) | [i:<-[0..<L]]]]
to find out possible primes divs N.
]]


>>> from seed.math.is_prime__le_pow2_81 import is_prime__le_pow2_81
>>> def f(p2e4N):
...     N = II__p2e_(p2e4N)
...     ls0 = [*unsorted_iter_primes_where_phiP_divs_(p2e4N)]
...     ls1 = [k for k in range(2, N+2) if N%(k-1) == 0 and is_prime__le_pow2_81(k)]
...     print(N)
...     print(ls0)
...     print(ls1)
...     print(ls1 == sorted(ls0))
>>> f({2:3,3:2,5:1})
360
[2, 3, 11, 7, 31, 19, 5, 13, 61, 37, 181, 41, 73]
[2, 3, 5, 7, 11, 13, 19, 31, 37, 41, 61, 73, 181]
True
>>> f({2:8})
256
[2, 3, 5, 17, 257]
[2, 3, 5, 17, 257]
True

>>> p2e4N = {2:3,3:2,5:1}
>>> N = II__p2e_(p2e4N)
>>> N
360
>>> [*unsorted_iter_primes_where_phiP_divs_(p2e4N)]
[2, 3, 11, 7, 31, 19, 5, 13, 61, 37, 181, 41, 73]
>>> [k for k in range(2, N+2) if N%(k-1) == 0 and is_prime__le_pow2_81(k)]
[2, 3, 5, 7, 11, 13, 19, 31, 37, 41, 61, 73, 181]
>>> [k for k in range(2, N+2) if N%(k-1) == 0 and is_prime__le_pow2_81(k)] == sorted(unsorted_iter_primes_where_phiP_divs_(p2e4N))
True

py_adhoc_call   seed.math.prime_pint.iter_primes_where_phiP_divs_   ,unsorted_iter_primes_where_phiP_divs_
]]]'''#'''
__all__ = r'''
unsorted_iter_primes_where_phiP_divs_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.math.is_prime__via_complete_factorization_Nmm_ import is_prime__via_complete_factorization_Nmm_
#def is_prime__via_complete_factorization_Nmm_(p2e4Nmm_or_ps4Nmm, N, /):
from seed.math.II import II__p2e_
from seed.tiny_.check import check_type_is, check_int_ge
from seed.tiny import fst, snd
from itertools import product
___end_mark_of_excluded_global_names__0___ = ...



def unsorted_iter_primes_where_phiP_divs_(p2e4N, /):
    for p, e in p2e4N.items():
        check_int_ge(2, p)
        check_int_ge(1, e)
    yield 2
    ez = p2e4N.get(2, 0)
    #if not 2 in p2e4N:
    if not ez:
        return
    pe_ls = sorted(p2e4N.items())
    ps = [*map(fst, pe_ls)]
    es = [*map(snd, pe_ls)]
    assert ps[0] == 2
    for _es in product(*(range(int(j==0), e+1) for j, e in enumerate(es))):
        # [_ez >= 1]
        assert _es[0] > 0
        #bug:_p2e4Kmm = dict(zip(ps, _es))
        _p2e4Kmm = {p:e for p, e in zip(ps, _es) if e}
        Kmm = II__p2e_(_p2e4Kmm)
        # [even Kmm]
        K = 1+Kmm
        # [odd K]
        if is_prime__via_complete_factorization_Nmm_(_p2e4Kmm, K):
            yield K


__all__
from seed.math.prime_pint.iter_primes_where_phiP_divs_ import unsorted_iter_primes_where_phiP_divs_
from seed.math.prime_pint.iter_primes_where_phiP_divs_ import *
