#__all__:goto
r'''[[[
e ../../python3_src/seed/math/is_prime__via_complete_factorization_Nmm_.py


seed.math.is_prime__via_complete_factorization_Nmm_
py -m nn_ns.app.debug_cmd   seed.math.is_prime__via_complete_factorization_Nmm_ -x
py -m nn_ns.app.doctest_cmd seed.math.is_prime__via_complete_factorization_Nmm_:__doc__ -ht
py_adhoc_call   seed.math.is_prime__via_complete_factorization_Nmm_   @f

from seed.math.is_prime__via_complete_factorization_Nmm_ import is_prime__via_complete_factorization_Nmm_



>>> is_prime__via_complete_factorization_Nmm_([], -1)
Traceback (most recent call last):
    ...
ValueError
>>> is_prime__via_complete_factorization_Nmm_([], 0)
Traceback (most recent call last):
    ...
ValueError
>>> is_prime__via_complete_factorization_Nmm_([], 1)
Traceback (most recent call last):
    ...
ValueError
>>> is_prime__via_complete_factorization_Nmm_([], 2)
True
>>> is_prime__via_complete_factorization_Nmm_([2], 3)
True
>>> is_prime__via_complete_factorization_Nmm_([3], 4)
False
>>> is_prime__via_complete_factorization_Nmm_([2], 5)
True
>>> is_prime__via_complete_factorization_Nmm_([2,3], 7)
True
>>> is_prime__via_complete_factorization_Nmm_([7], 8)
False
>>> is_prime__via_complete_factorization_Nmm_([2], 9)
False
>>> is_prime__via_complete_factorization_Nmm_([3], 10)
False
>>> is_prime__via_complete_factorization_Nmm_([2,3], 10)
False
>>> is_prime__via_complete_factorization_Nmm_([2,5], 11)
True
>>> is_prime__via_complete_factorization_Nmm_([11], 12)
False
>>> is_prime__via_complete_factorization_Nmm_([2,3], 13)
True
>>> is_prime__via_complete_factorization_Nmm_([5,2,3], 13)
True
>>> is_prime__via_complete_factorization_Nmm_({2:4}, 17)
True



fixed:7,23:
seed.math.primality_proving__plain.Fail__unknown_fine_upperbound4primitive_root: (7, (2, 3), (1, 1), False, 3)
seed.math.primality_proving__plain.Fail__unknown_fine_upperbound4primitive_root: (23, (2, 11), (1, 1), False, 5)


#ok@20240706
>>> _test_le_(2**16+3)  #doctest: +SKIP


py_adhoc_call   seed.math.is_prime__via_complete_factorization_Nmm_   @_test_le_  ='2**16+3'
py_adhoc_call   seed.math.is_prime__via_complete_factorization_Nmm_   @_test_le_  ='2**18+3'
    #ok@20240706


#]]]'''
__all__ = r'''
is_prime__via_complete_factorization_Nmm_

'''.split()#'''
__all__

from seed.math.is_complete_factorization_of__ft2e_ import is_complete_factorization_of__ft2e_, check_complete_factorization_of__ft2e_
from seed.tiny_.check_container import is_mapping, check_mapping

from seed.tiny_.check import check_type_is, check_int_ge
from seed.math.semi_factor_pint_via_trial_division import complete_factor_pint_via_trial_division
from seed.math.primality_proving__plain import return_version____primality_test__Nmm__plain__sqrt_case_
def __():
  def return_version____primality_test__Nmm__plain__sqrt_case_(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, /, *, complete_factorization__vs__using_gcd=True):
    '-> (case, payload)/((odd_prime_case/0, j2g) | (1, witness4composite) | (2, nontrivial_factor) | (even_prime_case/3, None)) | ^ERH__fail/Fail__unknown_fine_upperbound4primitive_root | ^ValueError__not_complete_factorization | ^ValueError__not_sqrt_case'






def _test_le_(max_N, /):
    from seed.math.prime_gens import min_prime_factor_gen, tabulate_may_min_prime_factor4uint_lt_, tabulate_may_factorization4uint_lt_
    n2p2e = tabulate_may_factorization4uint_lt_(1+max_N)
    for Nmm in range(1, max_N):
        N = Nmm+1
        p2e4N = n2p2e[N]
        p2e4Nmm = n2p2e[Nmm]
        ans = N in p2e4N
        r = is_prime__via_complete_factorization_Nmm_(p2e4Nmm.keys(), N)
        #assert r == ans
        if not r == ans:
            print(N, sorted(p2e4N.items()), Nmm, sorted(p2e4Nmm.items()), ans, r)

def is_prime__via_complete_factorization_Nmm_(p2e4Nmm_or_ps4Nmm, N, /):
    '-> bool | ^ERH__fail/Fail__unknown_fine_upperbound4primitive_root | ^ValueError__not_complete_factorization | ^ValueError__not_sqrt_case'
    check_type_is(int, N)

    Nmm = N-1
    if is_mapping(p2e4Nmm_or_ps4Nmm):
        p2e4Nmm = p2e4Nmm_or_ps4Nmm
    else:
        ps4Nmm = p2e4Nmm_or_ps4Nmm
        #ps4Nmm[:0]
        p2e4Nmm = complete_factor_pint_via_trial_division(ps4Nmm, Nmm)
    p2e4Nmm
    check_complete_factorization_of__ft2e_(Nmm, p2e4Nmm)

    j2p4Nmm = (*sorted(p2e4Nmm),)
    j2e4Nmm = tuple(p2e4Nmm[p] for p in j2p4Nmm)
    (case, payload) = return_version____primality_test__Nmm__plain__sqrt_case_(N, j2p4Nmm, j2e4Nmm, complete_factorization__vs__using_gcd=False)
    assert 0 <= case < 4
    return case in (0, 3)



__all__
from seed.math.is_prime__via_complete_factorization_Nmm_ import is_prime__via_complete_factorization_Nmm_
from seed.math.is_prime__via_complete_factorization_Nmm_ import *
