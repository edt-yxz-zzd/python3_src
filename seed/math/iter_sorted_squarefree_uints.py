#__all__:goto
r'''[[[
e ../../python3_src/seed/math/iter_sorted_squarefree_uints.py
view others/数学/prime/无平方因子耂充分条件.txt

seed.math.iter_sorted_squarefree_uints
py -m nn_ns.app.debug_cmd   seed.math.iter_sorted_squarefree_uints -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.iter_sorted_squarefree_uints:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method.py
    generate k4D @iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_()
]]

[[
view ../../python3_src/seed/math/iter_sorted_squarefree_uints.py
vs:
view ../../python3_src/seed/math/iter_unsorted_squarefree_uints.py
    iter_unsorted_squarefree_uints_()
view ../../python3_src/seed/math/iter_sorted_products_of_uints.py

view ../../python3_src/seed/math/prime_sieve/sieve_ge_le.py
   kw:squarefree_only@iter_sieve4prime_factorizations_ge_lt_()

]]


'#'; __doc__ = r'#'
>>> [*islice(iter_sorted_squarefree_uints_([2,3,5]), 0, 100)]
[1, 2, 3, 5, 6, 10, 15, 30]
>>> [*islice(iter_sorted_squarefree_uints_([2,3,5], may_prime2ok_=lambda p:p>2), 0, 100)]
[1, 3, 5, 15]
>>> [*islice(iter_sorted_squarefree_uints_([2,3,5], more=True), 0, 100)]
[(1, (), (), -1), (2, ((), 0), ((), 2), 2), (3, ((), 1), ((), 3), 3), (5, ((), 2), ((), 5), 5), (6, (((), 0), 1), (((), 2), 3), -1), (10, (((), 0), 2), (((), 2), 5), -1), (15, (((), 1), 2), (((), 3), 5), -1), (30, ((((), 0), 1), 2), ((((), 2), 3), 5), -1)]
>>> [*islice(iter_sorted_squarefree_uints_([2,3,5], more=True, to_seq6more=True), 0, 100)]
[(1, (), (), -1), (2, (0,), (2,), 2), (3, (1,), (3,), 3), (5, (2,), (5,), 5), (6, (0, 1), (2, 3), -1), (10, (0, 2), (2, 5), -1), (15, (1, 2), (3, 5), -1), (30, (0, 1, 2), (2, 3, 5), -1)]
>>> [*islice(iter_sorted_squarefree_uints_([2,3,5], more=True, to_seq6more=True, may_squarefree7resume=10), 0, 100)]
[(15, (1, 2), (3, 5), -1), (30, (0, 1, 2), (2, 3, 5), -1)]
>>> [*islice(iter_sorted_squarefree_uints_([2,3,5], more=True, to_seq6more=True, may_squarefree7resume=10, new_resume=True), 0, 100)]
[(10, (0, 2), (2, 5), -1), (15, (1, 2), (3, 5), -1), (30, (0, 1, 2), (2, 3, 5), -1)]
>>> [*islice(iter_sorted_squarefree_uints_([2,3,5], more=True, to_seq6more=True, may_squarefree7resume=-10, neg_resume_ok=True), 0, 100)]
[(10, (0, 2), (2, 5), -1), (15, (1, 2), (3, 5), -1), (30, (0, 1, 2), (2, 3, 5), -1)]
>>> [*islice(iter_sorted_squarefree_uints_([2,3,5], more=True, to_seq6more=True, may_squarefree7resume=-10, neg_resume_ok=True, new_resume=True), 0, 100)]
[(15, (1, 2), (3, 5), -1), (30, (0, 1, 2), (2, 3, 5), -1)]
>>> us100 = [*islice(iter_sorted_squarefree_uints_(), 0, 100)]
>>> us100
[1, 2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30, 31, 33, 34, 35, 37, 38, 39, 41, 42, 43, 46, 47, 51, 53, 55, 57, 58, 59, 61, 62, 65, 66, 67, 69, 70, 71, 73, 74, 77, 78, 79, 82, 83, 85, 86, 87, 89, 91, 93, 94, 95, 97, 101, 102, 103, 105, 106, 107, 109, 110, 111, 113, 114, 115, 118, 119, 122, 123, 127, 129, 130, 131, 133, 134, 137, 138, 139, 141, 142, 143, 145, 146, 149, 151, 154, 155, 157, 158, 159, 161, 163]

>>> from seed.math.prime_sieve.sieve_ge_le import iter_sieve4prime_factorizations_ge_lt_
>>> _us100 = [u for u, p2e4u in islice(iter_sieve4prime_factorizations_ge_lt_(1, 1+163+40, with_uint=True, squarefree_only=True), 0, 100)]
>>> _us100 == us100
True







is_partial_squarefree6finite_basis_
>>> is_partial_squarefree6finite_basis_(False, [2, 3, 5], 15)
True
>>> is_partial_squarefree6finite_basis_(False, [2, 3, 5], 45)
False
>>> is_partial_squarefree6finite_basis_(False, [2, 3, 5], 12)
False
>>> is_partial_squarefree6finite_basis_(False, [2, 3, 5], 6)
True
>>> is_partial_squarefree6finite_basis_(False, [2, 3, 5], 6*7**2)
True
>>> is_partial_squarefree6finite_basis_(False, [2, 3, 5], 3*7**2)
True

>>> is_partial_squarefree6finite_basis_(True, [2, 3, 5], 15)
True
>>> is_partial_squarefree6finite_basis_(True, [2, 3, 5], 45)
False
>>> is_partial_squarefree6finite_basis_(True, [2, 3, 5], 12)
False
>>> is_partial_squarefree6finite_basis_(True, [2, 3, 5], 6)
False
>>> is_partial_squarefree6finite_basis_(True, [2, 3, 5], 6*7**2)
False
>>> is_partial_squarefree6finite_basis_(True, [2, 3, 5], 3*7**2)
True




IterSortedIndivisible6finite_divisors
IterSortedPartialSquarefree6finite_basis
>>> it7even_ok = IterSortedIndivisible6finite_divisors(False, [5, 3])
>>> it7even_ok
IterSortedIndivisible6finite_divisors(False, (5, 3))
>>> [*islice(it7even_ok, 0, 18)]
[1, 2, 4, 7, 8, 11, 13, 14, 16, 17, 19, 22, 23, 26, 28, 29, 31, 32]
>>> [*islice(it7even_ok.iter7resume__gt1_(16), 0, 18)]
[17, 19, 22, 23, 26, 28, 29, 31, 32, 34, 37, 38, 41, 43, 44, 46, 47, 49]
>>> [*islice(it7even_ok.iter7resume__gt1_(-16, neg_resume_ok=True), 0, 18)]
[16, 17, 19, 22, 23, 26, 28, 29, 31, 32, 34, 37, 38, 41, 43, 44, 46, 47]
>>> [*islice(it7even_ok.iter7resume__gt1_(16, new_resume=True), 0, 18)]
[16, 17, 19, 22, 23, 26, 28, 29, 31, 32, 34, 37, 38, 41, 43, 44, 46, 47]
>>> [*islice(it7even_ok.iter7resume__gt1_(-16, new_resume=True, neg_resume_ok=True), 0, 18)]
[17, 19, 22, 23, 26, 28, 29, 31, 32, 34, 37, 38, 41, 43, 44, 46, 47, 49]
>>> [*islice(it7even_ok.iter7resume__gt1_(16, _more4compatibility=True), 0, 18)]
[(17, None, None, -1), (19, None, None, -1), (22, None, None, -1), (23, None, None, -1), (26, None, None, -1), (28, None, None, -1), (29, None, None, -1), (31, None, None, -1), (32, None, None, -1), (34, None, None, -1), (37, None, None, -1), (38, None, None, -1), (41, None, None, -1), (43, None, None, -1), (44, None, None, -1), (46, None, None, -1), (47, None, None, -1), (49, None, None, -1)]

>>> it7odd_only = IterSortedIndivisible6finite_divisors(True, [5, 3])
>>> it7odd_only
IterSortedIndivisible6finite_divisors(True, (5, 3))
>>> [*islice(it7odd_only, 0, 18)]
[1, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 49, 53, 59, 61, 67]
>>> [*islice(it7odd_only.iter7resume__gt1_(41), 0, 18)]
[43, 47, 49, 53, 59, 61, 67, 71, 73, 77, 79, 83, 89, 91, 97, 101, 103, 107]
>>> [*islice(it7odd_only.iter7resume__gt1_(-41, neg_resume_ok=True), 0, 18)]
[41, 43, 47, 49, 53, 59, 61, 67, 71, 73, 77, 79, 83, 89, 91, 97, 101, 103]
>>> [*islice(it7odd_only.iter7resume__gt1_(41, new_resume=True), 0, 18)]
[41, 43, 47, 49, 53, 59, 61, 67, 71, 73, 77, 79, 83, 89, 91, 97, 101, 103]
>>> [*islice(it7odd_only.iter7resume__gt1_(-41, new_resume=True, neg_resume_ok=True), 0, 18)]
[43, 47, 49, 53, 59, 61, 67, 71, 73, 77, 79, 83, 89, 91, 97, 101, 103, 107]
>>> [*islice(it7odd_only.iter7resume__gt1_(41, _more4compatibility=True), 0, 18)]
[(43, None, None, -1), (47, None, None, -1), (49, None, None, -1), (53, None, None, -1), (59, None, None, -1), (61, None, None, -1), (67, None, None, -1), (71, None, None, -1), (73, None, None, -1), (77, None, None, -1), (79, None, None, -1), (83, None, None, -1), (89, None, None, -1), (91, None, None, -1), (97, None, None, -1), (101, None, None, -1), (103, None, None, -1), (107, None, None, -1)]










>>> it7even_ok = IterSortedPartialSquarefree6finite_basis(False, [5, 3])
>>> it7even_ok
IterSortedPartialSquarefree6finite_basis(False, (5, 3))
>>> [*islice(it7even_ok, 0, 18)]
[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20]
>>> [*islice(it7even_ok.iter7resume__gt1_(16), 0, 18)]
[17, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38]
>>> [*islice(it7even_ok.iter7resume__gt1_(-16, neg_resume_ok=True), 0, 18)]
[16, 17, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37]
>>> [*islice(it7even_ok.iter7resume__gt1_(16, new_resume=True), 0, 18)]
[16, 17, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37]
>>> [*islice(it7even_ok.iter7resume__gt1_(-16, new_resume=True, neg_resume_ok=True), 0, 18)]
[17, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38]
>>> [*islice(it7even_ok.iter7resume__gt1_(16, _more4compatibility=True), 0, 18)]
[(17, None, None, -1), (19, None, None, -1), (20, None, None, -1), (21, None, None, -1), (22, None, None, -1), (23, None, None, -1), (24, None, None, -1), (26, None, None, -1), (28, None, None, -1), (29, None, None, -1), (30, None, None, -1), (31, None, None, -1), (32, None, None, -1), (33, None, None, -1), (34, None, None, -1), (35, None, None, -1), (37, None, None, -1), (38, None, None, -1)]

>>> it7odd_only = IterSortedPartialSquarefree6finite_basis(True, [5, 3])
>>> it7odd_only
IterSortedPartialSquarefree6finite_basis(True, (5, 3))
>>> [*islice(it7odd_only, 0, 18)]
[1, 3, 5, 7, 11, 13, 15, 17, 19, 21, 23, 29, 31, 33, 35, 37, 39, 41]
>>> [*islice(it7odd_only.iter7resume__gt1_(41), 0, 18)]
[43, 47, 49, 51, 53, 55, 57, 59, 61, 65, 67, 69, 71, 73, 77, 79, 83, 85]
>>> [*islice(it7odd_only.iter7resume__gt1_(-41, neg_resume_ok=True), 0, 18)]
[41, 43, 47, 49, 51, 53, 55, 57, 59, 61, 65, 67, 69, 71, 73, 77, 79, 83]
>>> [*islice(it7odd_only.iter7resume__gt1_(41, new_resume=True), 0, 18)]
[41, 43, 47, 49, 51, 53, 55, 57, 59, 61, 65, 67, 69, 71, 73, 77, 79, 83]
>>> [*islice(it7odd_only.iter7resume__gt1_(-41, new_resume=True, neg_resume_ok=True), 0, 18)]
[43, 47, 49, 51, 53, 55, 57, 59, 61, 65, 67, 69, 71, 73, 77, 79, 83, 85]
>>> [*islice(it7odd_only.iter7resume__gt1_(41, _more4compatibility=True), 0, 18)]
[(43, None, None, -1), (47, None, None, -1), (49, None, None, -1), (51, None, None, -1), (53, None, None, -1), (55, None, None, -1), (57, None, None, -1), (59, None, None, -1), (61, None, None, -1), (65, None, None, -1), (67, None, None, -1), (69, None, None, -1), (71, None, None, -1), (73, None, None, -1), (77, None, None, -1), (79, None, None, -1), (83, None, None, -1), (85, None, None, -1)]











iter_sorted_partial_squarefree_uints_

def iter_sorted_partial_squarefree_uints_(finite_basis, /, *, may_prev_uint7resume=..., odd_only=False, new_resume=False, neg_resume_ok=False, _more4compatibility=False):
>>> [*islice(iter_sorted_partial_squarefree_uints_([5, 3]), 0, 18)]
[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20]
>>> [*islice(iter_sorted_partial_squarefree_uints_([5, 3], odd_only=True), 0, 18)]
[1, 3, 5, 7, 11, 13, 15, 17, 19, 21, 23, 29, 31, 33, 35, 37, 39, 41]
>>> [*islice(iter_sorted_partial_squarefree_uints_([5, 3], may_prev_uint7resume=16), 0, 18)]
[17, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38]
>>> [*islice(iter_sorted_partial_squarefree_uints_([5, 3], may_prev_uint7resume=16, new_resume=True), 0, 18)]
[16, 17, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37]
>>> [*islice(iter_sorted_partial_squarefree_uints_([5, 3], may_prev_uint7resume=-16, neg_resume_ok=True), 0, 18)]
[16, 17, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37]
>>> [*islice(iter_sorted_partial_squarefree_uints_([5, 3], may_prev_uint7resume=16, _more4compatibility=True), 0, 18)]
[(17, None, None, -1), (19, None, None, -1), (20, None, None, -1), (21, None, None, -1), (22, None, None, -1), (23, None, None, -1), (24, None, None, -1), (26, None, None, -1), (28, None, None, -1), (29, None, None, -1), (30, None, None, -1), (31, None, None, -1), (32, None, None, -1), (33, None, None, -1), (34, None, None, -1), (35, None, None, -1), (37, None, None, -1), (38, None, None, -1)]





mk__iter_sorted_partial_squarefree_uints7mimic_oldAPI_
>>> iter_sorted_partial_squarefree_uints7mimic_oldAPI_ = mk__iter_sorted_partial_squarefree_uints7mimic_oldAPI_(True, [5, 3])
>>> [*islice(iter_sorted_partial_squarefree_uints7mimic_oldAPI_(), 0, 18)]
[1, 3, 5, 7, 11, 13, 15, 17, 19, 21, 23, 29, 31, 33, 35, 37, 39, 41]
>>> iter_sorted_partial_squarefree_uints7mimic_oldAPI_ = mk__iter_sorted_partial_squarefree_uints7mimic_oldAPI_(False, [5, 3])
>>> [*islice(iter_sorted_partial_squarefree_uints7mimic_oldAPI_(), 0, 18)]
[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20]
>>> [*islice(iter_sorted_partial_squarefree_uints7mimic_oldAPI_(may_squarefree7resume=16), 0, 18)]
[17, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38]
>>> [*islice(iter_sorted_partial_squarefree_uints7mimic_oldAPI_(may_squarefree7resume=16, new_resume=True), 0, 18)]
[16, 17, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37]
>>> [*islice(iter_sorted_partial_squarefree_uints7mimic_oldAPI_(may_squarefree7resume=-16, neg_resume_ok=True), 0, 18)]
[16, 17, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37]
>>> [*islice(iter_sorted_partial_squarefree_uints7mimic_oldAPI_(may_squarefree7resume=16, more=True), 0, 18)]
[(17, None, None, -1), (19, None, None, -1), (20, None, None, -1), (21, None, None, -1), (22, None, None, -1), (23, None, None, -1), (24, None, None, -1), (26, None, None, -1), (28, None, None, -1), (29, None, None, -1), (30, None, None, -1), (31, None, None, -1), (32, None, None, -1), (33, None, None, -1), (34, None, None, -1), (35, None, None, -1), (37, None, None, -1), (38, None, None, -1)]





iter_sorted_partial_squarefree_uints7mimic_oldAPI__7odd_only__7basis_eq_fst_16_odd_primes_
>>> [*islice(iter_sorted_partial_squarefree_uints7mimic_oldAPI__7odd_only__7basis_eq_fst_16_odd_primes_(), 0, 18)]
[1, 3, 5, 7, 11, 13, 15, 17, 19, 21, 23, 29, 31, 33, 35, 37, 39, 41]
>>> [*islice(iter_sorted_partial_squarefree_uints7mimic_oldAPI__7odd_only__7basis_eq_fst_16_odd_primes_(may_squarefree7resume=17, new_resume=True), 0, 18)]
[17, 19, 21, 23, 29, 31, 33, 35, 37, 39, 41, 43, 47, 51, 53, 55, 57, 59]







iter_sorted_squarefree_uints7mimic_oldAPI__7builtin_data6zpow64_
    odd_only
>>> [*islice(iter_sorted_squarefree_uints7mimic_oldAPI__7builtin_data6zpow64_(), 0, 18)]
[1, 3, 5, 7, 11, 13, 15, 17, 23, 29, 31, 33, 35, 37, 47, 51, 61, 65]
>>> [*islice(iter_sorted_squarefree_uints7mimic_oldAPI__7builtin_data6zpow64_(may_squarefree7resume=17), 0, 18)]
[23, 29, 31, 33, 35, 37, 47, 51, 61, 65, 79, 83, 97, 101, 119, 123, 127, 129]
>>> [*islice(iter_sorted_squarefree_uints7mimic_oldAPI__7builtin_data6zpow64_(may_squarefree7resume=17, new_resume=True), 0, 18)]
[17, 23, 29, 31, 33, 35, 37, 47, 51, 61, 65, 79, 83, 97, 101, 119, 123, 127]
>>> [*islice(iter_sorted_squarefree_uints7mimic_oldAPI__7builtin_data6zpow64_(may_squarefree7resume=-17, neg_resume_ok=True), 0, 18)]
[17, 23, 29, 31, 33, 35, 37, 47, 51, 61, 65, 79, 83, 97, 101, 119, 123, 127]
>>> [*islice(iter_sorted_squarefree_uints7mimic_oldAPI__7builtin_data6zpow64_(may_squarefree7resume=17, more=True), 0, 18)]
[(23, None, None, -1), (29, None, None, -1), (31, None, None, -1), (33, None, None, -1), (35, None, None, -1), (37, None, None, -1), (47, None, None, -1), (51, None, None, -1), (61, None, None, -1), (65, None, None, -1), (79, None, None, -1), (83, None, None, -1), (97, None, None, -1), (101, None, None, -1), (119, None, None, -1), (123, None, None, -1), (127, None, None, -1), (129, None, None, -1)]























py_adhoc_call   seed.math.iter_sorted_squarefree_uints   @f
]]]'''#'''
__all__ = r'''
iter_sorted_squarefree_uints_
iter_sorted_partial_squarefree_uints7mimic_oldAPI__7odd_only__7basis_eq_fst_16_odd_primes_
iter_sorted_squarefree_uints7mimic_oldAPI__7builtin_data6zpow64_




mk__iter_sorted_partial_squarefree_uints7mimic_oldAPI_
    iter_sorted_partial_squarefree_uints7mimic_oldAPI__7odd_only__7basis_eq_fst_16_odd_primes_
    iter_sorted_partial_squarefree_uints_
    IterSortedIndivisible6finite_divisors
        IterSortedPartialSquarefree6finite_basis
            is_partial_squarefree6finite_basis_
'''.split()#'''
__all__
r'''[[[
gp
    issquarefree
    forsquarefree

factor(9)~[1,][1]
    3

ver1:
next_squarefree_ge_(u)={
    ;forsquarefree(
    u_pes=u,u+2*sqrtint(abs(u))+9
    ,return([u_pes[1],u_pes[2]~[1,]])
    )
}

ver2:
next_squarefree_ge_(u,odd_only=0)={
    ;for(
    v=u,u+(2*sqrtint(abs(u))+9)
    ,if(((!odd_only) || v%2==1) && issquarefree(v)
    ,return(if(v==1,[1, []],[v,factorint(v)~[1,]]))
    ,)
    )
}

next_squarefree_ge_(2^9)
    [514, [2, 257]]
next_squarefree_ge_(2^9,1)
    [515, [5, 103]]

prev_squarefree_lt_(2^9)
    [511, [7, 73]]
prev_squarefree_lt_(2^9,1)
    [511, [7, 73]]
prev_squarefree_lt_(3^7)
    [2186, [2, 1093]]
prev_squarefree_lt_(3^7,1)
    [2185, [5, 19, 23]]

    ;for(
    v=u-(2*sqrtint(abs(u))+9),u-1
    ...)
prev_squarefree_lt_(u,odd_only=0)={
    ;forstep(
    v=u-1,u-(2*sqrtint(abs(u))+9),-1
    ,if(((!odd_only) || v%2==1) && issquarefree(v)
    ,return(if(v==1,[1, []],[v,factorint(v)~[1,]]))
    ,)
    )
}


list_squarefree_ge_pow_(min4base, max4base, max4pow,odd_only=0)={
    ;local(ls,nx,u)
    ;ls=List()
    ;for(base=min4base,min(max4base,max4pow)
    ,if(base < 2 || ispower(base)
        ,
        ,u=base
        ;while(u<=max4pow
            ,nx=next_squarefree_ge_(u,odd_only)
            ;listput(ls,nx)
            ;u*=base
            )
        )
    )
    ;return(Vec(ls))
}

print7seq_(ls)={ foreach(ls,x,print(x)) }

vecsort(list_squarefree_ge_pow_(2,12,2^9),,8)
    [[2, [2]], [3, [3]], [5, [5]], [6, [2, 3]], [7, [7]], [10, [2, 5]], [11, [11]], [13, [13]], [17, [17]], [26, [2, 13]], [29, [29]], [33, [3, 11]], [37, [37]], [51, [3, 17]], [65, [5, 13]], [82, [2, 41]], [101, [101]], [122, [2, 61]], [127, [127]], [129, [3, 43]], [145, [5, 29]], [217, [7, 31]], [246, [2, 3, 41]], [257, [257]], [345, [3, 5, 23]], [514, [2, 257]]]
vecsort(list_squarefree_ge_pow_(2,12,2^9,1),,8)
    [[3, [3]], [5, [5]], [7, [7]], [11, [11]], [13, [13]], [17, [17]], [29, [29]], [33, [3, 11]], [37, [37]], [51, [3, 17]], [65, [5, 13]], [83, [83]], [101, [101]], [123, [3, 41]], [127, [127]], [129, [3, 43]], [145, [5, 29]], [217, [7, 31]], [247, [13, 19]], [257, [257]], [345, [3, 5, 23]], [515, [5, 103]]]


vecsort(list_squarefree_ge_pow_(2,12,2^64),,8)
    ver1{next_squarefree_ge_}:
    current stack size: 8000000 (7.629 Mbytes)
        [hint] set 'parisizemax' to a nonzero value in your GPRC

print7seq_(vecsort(list_squarefree_ge_pow_(2,12,2^32,1),,8))
    ver2{next_squarefree_ge_}:
    ok

print7seq_(vecsort(list_squarefree_ge_pow_(2,12,2^64,1),,8))
    ver2{next_squarefree_ge_}:
    =>:_data4next6zpow64
    224lines

[odd_only:=1]
data4next6zpow64 = vecsort(list_squarefree_ge_pow_(2,12,2^64,1),,8)
us6data4next6zpow64 = vector(length(data4next6zpow64), j, data4next6zpow64[j][1])
data4prev6zpow64 = vector(length(us6data4next6zpow64), j, prev_squarefree_lt_(us6data4next6zpow64[j],1))
us6data4prev6zpow64 = vector(length(data4prev6zpow64), j, data4prev6zpow64[j][1])
us6data4prevnext6zpow64 = vecsort(concat(us6data4prev6zpow64,us6data4next6zpow64),,8)

print7seq_(us6data4prevnext6zpow64)
    #   442lines
print7seq_(data4next6zpow64)
    #   224lines
print7seq_(data4prev6zpow64)
    #   224lines

data4prev6zpow64
_data4prev6zpow64 = (
#generated by gp:
#   224lines
([1, []]
,[3, [3]]
,[5, [5]]
,[7, [7]]
,[11, [11]]
,[15, [3, 5]]
,[23, [23]]
,[31, [31]]
,[35, [5, 7]]
,[47, [47]]
,[61, [61]]
,[79, [79]]
,[97, [97]]
,[119, [7, 17]]
,[123, [3, 41]]
,[127, [127]]
,[143, [11, 13]]
,[215, [5, 43]]
,[241, [241]]
,[255, [3, 5, 17]]
,[341, [11, 31]]
,[511, [7, 73]]
,[623, [7, 89]]
,[727, [727]]
,[997, [997]]
,[1023, [3, 11, 31]]
,[1295, [5, 7, 37]]
,[1329, [3, 443]]
,[1727, [11, 157]]
,[2047, [23, 89]]
,[2185, [5, 19, 23]]
,[2399, [2399]]
,[3121, [3121]]
,[4093, [4093]]
,[6559, [7, 937]]
,[7773, [3, 2591]]
,[8191, [8191]]
,[9997, [13, 769]]
,[14639, [14639]]
,[15623, [17, 919]]
,[16383, [3, 43, 127]]
,[16805, [5, 3361]]
,[19681, [19681]]
,[20735, [5, 11, 13, 29]]
,[32767, [7, 31, 151]]
,[46655, [5, 7, 31, 43]]
,[59047, [137, 431]]
,[65535, [3, 5, 17, 257]]
,[78123, [3, 26041]]
,[99995, [5, 7, 2857]]
,[117647, [71, 1657]]
,[131071, [131071]]
,[161049, [3, 7, 7669]]
,[177145, [5, 71, 499]]
,[248831, [11, 22621]]
,[262141, [11, 23831]]
,[279935, [5, 55987]]
,[390623, [73, 5351]]
,[524287, [524287]]
,[531439, [113, 4703]]
,[823541, [823541]]
,[999997, [757, 1321]]
,[1048573, [1048573]]
,[1594321, [197, 8093]]
,[1679615, [5, 7, 37, 1297]]
,[1771559, [1771559]]
,[1953123, [3, 653, 997]]
,[2097149, [773, 2713]]
,[2985983, [7, 11, 13, 19, 157]]
,[4194303, [3, 23, 89, 683]]
,[4782967, [7, 17, 40193]]
,[5764799, [5764799]]
,[8388607, [47, 178481]]
,[9765623, [7, 151, 9239]]
,[9999997, [7, 1428571]]
,[10077695, [5, 19, 43, 2467]]
,[14348905, [5, 2869781]]
,[16777213, [16777213]]
,[19487167, [7, 79, 131, 269]]
,[33554431, [31, 601, 1801]]
,[35831807, [11, 659, 4943]]
,[40353605, [5, 8070721]]
,[43046719, [89, 483671]]
,[48828121, [61, 709, 1129]]
,[60466173, [3, 1933, 10427]]
,[67108863, [3, 2731, 8191]]
,[99999997, [1297, 77101]]
,[129140161, [29, 47, 94747]]
,[134217727, [7, 73, 262657]]
,[214358873, [23, 9319951]]
,[244140623, [223, 1094801]]
,[268435455, [3, 5, 29, 43, 113, 127]]
,[282475245, [3, 5, 13, 431, 3361]]
,[362797055, [5, 23, 3154757]]
,[387420487, [23, 3617, 4657]]
,[429981695, [5, 11, 13, 29, 89, 233]]
,[536870911, [233, 1103, 2089]]
,[999999997, [71, 2251, 6257]]
,[1073741821, [23, 46684427]]
,[1162261465, [5, 232452293]]
,[1220703123, [3, 9587, 42443]]
,[1977326741, [13, 103, 1476719]]
,[2147483647, [2147483647]]
,[2176782335, [5, 7, 13, 31, 37, 43, 97]]
,[2357947689, [3, 29, 137, 197831]]
,[3486784399, [7, 498112057]]
,[4294967295, [3, 5, 17, 257, 65537]]
,[5159780351, [11, 37, 157, 80749]]
,[6103515623, [6103515623]]
,[8589934591, [7, 23, 89, 599479]]
,[9999999997, [13, 769230769]]
,[10460353201, [3719, 2812679]]
,[13060694015, [5, 3433, 760891]]
,[13841287199, [13841287199]]
,[17179869183, [3, 43691, 131071]]
,[25937424599, [23, 1127714113]]
,[30517578123, [3, 8831, 1151911]]
,[31381059607, [31381059607]]
,[34359738367, [31, 71, 127, 122921]]
,[61917364223, [11, 13, 19141, 22621]]
,[68719476733, [242819, 283007]]
,[78364164093, [3, 1993, 13106567]]
,[94143178823, [19031, 4946833]]
,[96889010405, [5, 11, 167, 659, 16007]]
,[99999999997, [17, 5882352941]]
,[137438953471, [223, 616318177]]
,[152587890623, [7, 239, 1433, 63647]]
,[274877906943, [3, 174763, 524287]]
,[282429536479, [31, 6679, 1364071]]
,[285311670609, [3, 7, 18541, 732769]]
,[470184984573, [3, 17, 41, 953, 235951]]
,[549755813887, [7, 79, 8191, 121369]]
,[678223072847, [23, 41, 439, 1638311]]
,[743008370685, [3, 5, 7, 59, 241, 497663]]
,[762939453121, [19, 131, 4259, 71971]]
,[847288609441, [19, 44594137339]]
,[999999999997, [5507, 181587071]]
,[1099511627773, [13, 84577817521]]
,[2199023255551, [13367, 164511353]]
,[2541865828323, [3, 19, 44594137339]]
,[2821109907455, [5, 7, 17, 37, 1297, 98801]]
,[3138428376719, [257, 8713, 1401559]]
,[3814697265623, [47, 81163771609]]
,[4398046511101, [47, 193, 4463, 108637]]
,[4747561509941, [4747561509941]]
,[7625597484985, [5, 43, 2693, 13170403]]
,[8796093022207, [431, 9719, 2099863]]
,[8916100448255, [5, 7, 11, 13, 19, 29, 157, 20593]]
,[9999999999995, [5, 3833, 521784503]]
,[16926659444735, [5, 239, 409, 1123, 30839]]
,[17592186044415, [3, 5, 23, 89, 397, 683, 2113]]
,[19073486328123, [3, 1889, 3365711369]]
,[22876792454959, [4273, 5353801183]]
,[33232930569599, [233, 249703, 571201]]
,[34522712143927, [7, 43, 114693395827]]
,[35184372088831, [7, 31, 73, 151, 631, 23311]]
,[68630377364881, [23, 101, 7103, 4159349]]
,[70368744177663, [3, 47, 178481, 2796203]]
,[95367431640623, [2087, 45695942329]]
,[99999999999997, [839, 119189511323]]
,[101559956668415, [5, 7, 19, 31, 43, 2467, 46441]]
,[106993205379071, [11, 477517, 20369233]]
,[140737488355327, [2351, 4513, 13264529]]
,[205891132094647, [17, 263, 46050353857]]
,[232630513987205, [5, 46526102797441]]
,[281474976710653, [11, 167, 239, 641110271]]
,[379749833583239, [7, 12113, 4478657329]]
,[476837158203123, [3, 158945719401041]]
,[562949953421311, [127, 4432676798593]]
,[609359740010495, [5, 191, 638073026189]]
,[617673396283945, [5, 419491, 294487079]]
,[999999999999997, [599, 2131, 3733, 209861]]
,[1125899906842623, [3, 11, 31, 251, 601, 1801, 4051]]
,[1283918464548863, [11, 13, 211, 659, 4943, 13063]]
,[1628413597910447, [31, 9473, 47521, 116689]]
,[1853020188851839, [7, 337, 29209, 26892769]]
,[2251799813685247, [7, 103, 2143, 11119, 131071]]
,[2384185791015623, [7, 17, 5881, 3406763257]]
,[3656158440062973, [3, 13, 21577, 4344795491]]
,[4177248169415649, [3, 109, 173, 31883, 2315993]]
,[4503599627370495, [3, 5, 53, 157, 1613, 2731, 8191]]
,[5559060566555521, [317, 601, 29178816413]]
,[9007199254740991, [6361, 69431, 20394401]]
,[9999999999999997, [13, 433, 39323, 45177491]]
,[11398895185373141, [157, 46093, 1575172541]]
,[11920928955078121, [11, 29, 5339189, 6999131]]
,[15407021574586367, [11, 61, 157, 661, 9781, 22621]]
,[16677181699666567, [463, 10193, 3533781113]]
,[18014398509481981, [36217, 497401731493]]
,[21936950640377855, [5, 43, 55987, 1822428931]]
,[36028797018963967, [23, 31, 89, 881, 3191, 201961]]
,[45949729863572159, [71, 359, 1559, 3943, 293263]]
,[50031545098999705, [5, 15241, 656538876701]]
,[59604644775390623, [23, 127, 51871, 393390553]]
,[72057594037927935, [3, 5, 17, 29, 43, 113, 127, 15790321]]
,[79792266297611999, [967, 82515270214697]]
,[99999999999999997, [99999999999999997]]
,[131621703842267135, [5, 7, 23, 3154757, 51828151]]
,[144115188075855871, [7, 32377, 524287, 1212847]]
,[150094635296999119, [3767, 23017, 1731094721]]
,[184884258895036415, [5, 11, 13, 17, 29, 89, 97, 233, 260753]]
,[288230376151711743, [3, 59, 233, 1103, 2089, 3033169]]
,[298023223876953123, [3, 99341074625651041]]
,[450283905890997361, [450283905890997361]]
,[505447028499293769, [3, 7, 2027, 396203, 29969869]]
,[558545864083284005, [5, 111709172816656801]]
,[576460752303423487, [179951, 3203431780337]]
,[789730223053602815, [5, 47, 139, 3221, 7505944891]]
,[999999999999999997, [47, 1283, 949261, 17469877]]
,[1152921504606846973, [1177067, 979486728119]]
,[1350851717672992087, [7, 386471, 647057, 771703]]
,[1490116119384765623, [1490116119384765623]]
,[2218611106740436991, [11, 2693651, 74876782031]]
,[2305843009213693951, [2305843009213693951]]
,[3909821048582988047, [223, 271, 2922631, 22136489]]
,[4052555153018976265, [5, 810511030603795253]]
,[4611686018427387903, [3, 715827883, 2147483647]]
,[4738381338321616895, [5, 7, 13, 31, 37, 43, 97, 1297, 1678321]]
,[5559917313492231479, [17, 31, 89, 19753, 6001152281]]
,[7450580596923828123, [3, 311, 3449, 2315342688119]]
,[9223372036854775805, [5, 23, 53301701, 1504703107]]
,[9999999999999999997, [7, 103, 9431, 155027, 9486361]]
,[12157665459056928799, [23, 47, 11246684050931479]]
,[18446744073709551615, [3, 5, 17, 257, 641, 65537, 6700417]]
))
#_data4prev6zpow64 -> _us6data4prev6zpow64


data4next6zpow64
_data4next6zpow64 = (
#generated by gp:
#   224lines
([3, [3]]
,[5, [5]]
,[7, [7]]
,[11, [11]]
,[13, [13]]
,[17, [17]]
,[29, [29]]
,[33, [3, 11]]
,[37, [37]]
,[51, [3, 17]]
,[65, [5, 13]]
,[83, [83]]
,[101, [101]]
,[123, [3, 41]]
,[127, [127]]
,[129, [3, 43]]
,[145, [5, 29]]
,[217, [7, 31]]
,[247, [13, 19]]
,[257, [257]]
,[345, [3, 5, 23]]
,[515, [5, 103]]
,[627, [3, 11, 19]]
,[731, [17, 43]]
,[1001, [7, 11, 13]]
,[1027, [13, 79]]
,[1297, [1297]]
,[1333, [31, 43]]
,[1729, [7, 13, 19]]
,[2049, [3, 683]]
,[2189, [11, 199]]
,[2405, [5, 13, 37]]
,[3127, [53, 59]]
,[4097, [17, 241]]
,[6563, [6563]]
,[7777, [7, 11, 101]]
,[8193, [3, 2731]]
,[10001, [73, 137]]
,[14645, [5, 29, 101]]
,[15627, [3, 5209]]
,[16385, [5, 29, 113]]
,[16809, [3, 13, 431]]
,[19685, [5, 31, 127]]
,[20737, [89, 233]]
,[32771, [32771]]
,[46657, [13, 37, 97]]
,[59051, [59051]]
,[65537, [65537]]
,[78127, [7, 11161]]
,[100001, [11, 9091]]
,[117651, [3, 39217]]
,[131073, [3, 43691]]
,[161053, [161053]]
,[177149, [7, 25307]]
,[248833, [13, 19141]]
,[262145, [5, 13, 37, 109]]
,[279939, [3, 11, 17, 499]]
,[390629, [577, 677]]
,[524289, [3, 174763]]
,[531443, [11, 48313]]
,[823547, [823547]]
,[1000001, [101, 9901]]
,[1048577, [17, 61681]]
,[1594327, [7, 421, 541]]
,[1679617, [17, 98801]]
,[1771563, [3, 179, 3299]]
,[1953127, [11, 277, 641]]
,[2097155, [5, 59, 7109]]
,[2985985, [5, 29, 20593]]
,[4194305, [5, 397, 2113]]
,[4782971, [4782971]]
,[5764805, [5, 41, 61, 461]]
,[8388609, [3, 2796203]]
,[9765627, [3, 3255209]]
,[10000001, [11, 909091]]
,[10077697, [7, 31, 46441]]
,[14348909, [14348909]]
,[16777217, [97, 257, 673]]
,[19487173, [89, 347, 631]]
,[33554433, [3, 11, 251, 4051]]
,[35831809, [13, 211, 13063]]
,[40353609, [3, 13451203]]
,[43046727, [3, 14348909]]
,[48828127, [331, 147517]]
,[60466177, [37, 241, 6781]]
,[67108865, [5, 53, 157, 1613]]
,[100000001, [17, 5882353]]
,[129140165, [5, 7, 11, 335429]]
,[134217731, [4057, 33083]]
,[214358883, [3, 281, 254281]]
,[244140627, [3, 43, 1892563]]
,[268435457, [17, 15790321]]
,[282475253, [113, 2499781]]
,[362797057, [7, 51828151]]
,[387420491, [59, 283, 23203]]
,[429981697, [17, 97, 260753]]
,[536870913, [3, 59, 3033169]]
,[1000000001, [7, 11, 13, 19, 52579]]
,[1073741827, [1073741827]]
,[1162261469, [97, 1129, 10613]]
,[1220703127, [7, 19, 23, 41, 9733]]
,[1977326745, [3, 5, 131821783]]
,[2147483649, [3, 715827883]]
,[2176782337, [1297, 1678321]]
,[2357947693, [2357947693]]
,[3486784403, [58027, 60089]]
,[4294967297, [641, 6700417]]
,[5159780353, [7, 13, 19, 1657, 1801]]
,[6103515629, [569, 10726741]]
,[8589934597, [251, 1979, 17293]]
,[10000000001, [101, 3541, 27961]]
,[10460353205, [5, 1709, 1224149]]
,[13060694017, [7, 53, 937, 37571]]
,[13841287203, [3, 4613762401]]
,[17179869185, [5, 137, 953, 26317]]
,[25937424605, [5, 5187484921]]
,[30517578127, [6361, 4797607]]
,[31381059611, [11, 17, 211, 795323]]
,[34359738369, [3, 11, 43, 281, 86171]]
,[61917364227, [3, 127, 162512767]]
,[68719476737, [17, 241, 433, 38737]]
,[78364164097, [37, 421, 5030761]]
,[94143178829, [7, 53, 419, 659, 919]]
,[96889010411, [29, 37, 67, 239, 5639]]
,[100000000003, [100000000003]]
,[137438953473, [3, 1777, 25781083]]
,[152587890627, [3, 523, 97251683]]
,[274877906945, [5, 229, 457, 525313]]
,[282429536483, [282429536483]]
,[285311670613, [97, 40699, 72271]]
,[470184984577, [7, 11, 31, 101, 1950271]]
,[549755813891, [63727, 8626733]]
,[678223072851, [3, 226074357617]]
,[743008370689, [13, 57154490053]]
,[762939453127, [762939453127]]
,[847288609445, [5, 107, 1583717027]]
,[1000000000001, [73, 137, 99990001]]
,[1099511627777, [257, 4278255361]]
,[2199023255553, [3, 83, 8831418697]]
,[2541865828331, [2541865828331]]
,[2821109907457, [353, 1697, 4709377]]
,[3138428376723, [3, 83, 6163, 2045129]]
,[3814697265627, [3, 1271565755209]]
,[4398046511105, [5, 13, 29, 113, 1429, 14449]]
,[4747561509945, [3, 5, 316504100663]]
,[7625597484989, [11, 693236134999]]
,[8796093022209, [3, 2932031007403]]
,[8916100448257, [89, 193, 233, 2227777]]
,[10000000000001, [11, 859, 1058313049]]
,[16926659444737, [7, 190537, 12690943]]
,[17592186044417, [17, 353, 2931542417]]
,[19073486328131, [1489, 50993, 251203]]
,[22876792454963, [131, 174632003473]]
,[33232930569605, [5, 13, 443077, 1153921]]
,[34522712143933, [13, 8369, 317313089]]
,[35184372088835, [5, 7036874417767]]
,[68630377364885, [5, 7, 1960867924711]]
,[70368744177665, [5, 277, 1013, 1657, 30269]]
,[95367431640629, [17, 97, 100741, 574081]]
,[100000000000001, [29, 101, 281, 121499449]]
,[101559956668417, [13, 37, 73, 97, 541, 55117]]
,[106993205379077, [503, 1523, 5783, 24151]]
,[140737488355329, [3, 283, 165768537521]]
,[205891132094651, [449, 343081, 1336579]]
,[232630513987209, [3, 13, 79, 75504873089]]
,[281474976710657, [193, 65537, 22253377]]
,[379749833583243, [3, 67, 1889302654643]]
,[476837158203127, [143419, 3324783733]]
,[562949953421313, [3, 43, 4363953127297]]
,[609359740010497, [7, 1787, 48713705333]]
,[617673396283953, [3, 449, 343081, 1336579]]
,[1000000000000001, [7, 11, 13, 211, 241, 2161, 9091]]
,[1125899906842627, [7, 3435997, 46811113]]
,[1283918464548865, [5, 29, 673, 13156924369]]
,[1628413597910451, [3, 11, 17, 2902698035491]]
,[1853020188851843, [11, 139, 1211916408667]]
,[2251799813685251, [967, 3967, 4547, 129097]]
,[2384185791015627, [3, 19, 251, 563, 295994147]]
,[3656158440062977, [41, 1297, 68754507401]]
,[4177248169415653, [4976161, 839451973]]
,[4503599627370497, [17, 858001, 308761441]]
,[5559060566555527, [31, 43, 4170338009419]]
,[9007199254740993, [3, 107, 28059810762433]]
,[10000000000000001, [353, 449, 641, 1409, 69857]]
,[11398895185373147, [15493, 735744864479]]
,[11920928955078127, [3527, 3379906139801]]
,[15407021574586369, [7, 13, 19, 31, 421, 19141, 35671]]
,[16677181699666571, [19, 7300529, 120230521]]
,[18014398509481985, [5, 13, 37, 109, 246241, 279073]]
,[21936950640377859, [3, 7312316880125953]]
,[36028797018963971, [36028797018963971]]
,[45949729863572165, [5, 181, 2593, 82657, 236893]]
,[50031545098999709, [7, 205537, 34774097051]]
,[59604644775390627, [3, 11, 3779, 477957490561]]
,[72057594037927937, [257, 5153, 54410972897]]
,[79792266297612003, [3, 21193, 1255009772057]]
,[100000000000000001, [11, 103, 4013, 21993833369]]
,[131621703842267137, [37, 58477, 70489, 863017]]
,[144115188075855877, [41, 641, 9397, 583550761]]
,[150094635296999123, [150094635296999123]]
,[184884258895036417, [153953, 1200913648289]]
,[288230376151711745, [5, 107367629, 536903681]]
,[298023223876953127, [7, 132329, 321734058809]]
,[450283905890997365, [5, 11, 20548183, 398428421]]
,[505447028499293773, [43, 11754582058123111]]
,[558545864083284009, [3, 59, 131, 24088750769107]]
,[576460752303423489, [3, 2833, 37171, 1824726041]]
,[789730223053602817, [7, 113958101, 990000731]]
,[1000000000000000001, [101, 9901, 999999000001]]
,[1152921504606846977, [17, 241, 61681, 4562284561]]
,[1350851717672992091, [17, 40771, 102793, 18960241]]
,[1490116119384765629, [61, 24428133104668289]]
,[2218611106740436993, [13, 2551, 66900193189411]]
,[2305843009213693953, [3, 768614336404564651]]
,[3909821048582988053, [37, 653, 456409, 354558397]]
,[4052555153018976269, [31, 5147, 117751, 215699167]]
,[4611686018427387905, [5, 5581, 8681, 49477, 384773]]
,[4738381338321616897, [17, 5953, 98801, 473896897]]
,[5559917313492231483, [3, 1853305771164077161]]
,[7450580596923828127, [1806786637, 4123663771]]
,[9223372036854775811, [11, 271, 439, 7047956753329]]
,[10000000000000000001, [11, 909090909090909091]]
,[12157665459056928803, [1170408739, 10387538177]]
,[18446744073709551617, [274177, 67280421310721]]
))
#_data4next6zpow64 -> _us6data4next6zpow64


#]]]'''#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge
    #from seed.math.prime_sieve.primes_ge_lt import iter_filter4primes_ge_lt_
    #from seed.iters.ensure_sorted import ensure_strict_sorted
    from seed.for_libs.for_heapq import merge_ex
    #def merge_ex(*sorted_iterable_exs, key4stable:[False,callable]=False, key4le=None, __le__=None, reverse=False, unique:[bool,callable]=False, obj2value_:[None,callable]=None):
    #   '# [sorted_iterable_exs :: [sorted<fst> Iter (x, may sorted_iterable_exs{all <= x})]] # [[key4stable := False] -> [unstable sort]]'

    from itertools import islice, count
    from seed.data_funcs.lnkls import rglnkls2list
    from seed.math.iter_unsorted_squarefree_uints import _iter_primes, _std
    #def _std(squarefree7resume, new_resume, neg_resume_ok, /):
    #def _iter_primes(may_primes, may_prime2ok_, /):
    from seed.tiny_.funcs import echo, fst
    from seed.tiny_.containers import mk_tuple,mk_immutable_seq
    from seed.helper.repr_input import repr_helper

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

class IterSortedIndivisible6finite_divisors:
    def __init__(sf, odd_only, finite_divisors, /):
        odd_only = bool(odd_only)
        sf._b = odd_only
        sf._ds = mk_immutable_seq(finite_divisors)
    @property
    def odd_only(sf, /):
        return sf._b
    @property
    def finite_divisors(sf, /):
        return sf._ds
    def __repr__(sf, /):
        return repr_helper(sf, sf.odd_only, sf.finite_divisors)
    def __iter__(sf, /):
        return sf.iter__ge_(1)
    def iter7resume__gt1_(sf, may_prev_u, /, *, new_resume=False, neg_resume_ok=False, _more4compatibility=False):
        match may_prev_u:
            case None:
                min_u = 1
            case int(prev_u):
                if prev_u <= 0:
                    if prev_u == 0: raise ValueError(prev_u)
                    if not neg_resume_ok: raise ValueError(prev_u)
                    prev_u = -prev_u
                    new_resume = not new_resume
                min_u = prev_u + (not new_resume)
            case _:
                raise ValueError(may_prev_u)
        min_u
        it = sf.iter__ge_(min_u)
        if _more4compatibility:
            # (u, _, _, imay_new_prime)
            it = ((u, None, None, -1) for u in it)
        return it
    def iter__ge_(sf, min_u, /):
        return filter(sf.is_ok_, count(min_u))
    def is_ok_(sf, u, /):
        if sf.odd_only and u&1 == 0:
            # even
            return False
        return not any(u%d == 0 for d in sf.finite_divisors)


class IterSortedPartialSquarefree6finite_basis(IterSortedIndivisible6finite_divisors):
    def __init__(sf, odd_only, finite_basis, /):
        finite_basis = mk_immutable_seq(finite_basis)
        sf._ps = finite_basis
        finite_divisors = (p**2 for p in finite_basis)
        super().__init__(odd_only, finite_divisors)
    @property
    def finite_basis(sf, /):
        return sf._ps
    def __repr__(sf, /):
        return repr_helper(sf, sf.odd_only, sf.finite_basis)
def is_partial_squarefree6finite_basis_(odd_only, finite_basis, u, /):
    if odd_only:
        if u&1 == 0:
            # even
            return False
    return not any(u%p**2 == 0 for p in finite_basis)

def mk__iter_sorted_partial_squarefree_uints7mimic_oldAPI_(odd_only, finite_basis, /):
    sf = IterSortedPartialSquarefree6finite_basis(odd_only, finite_basis)
    def iter_sorted_partial_squarefree_uints7mimic_oldAPI_(may_primes=None, /, *, may_prime2ok_=None, more=False, to_seq6more=False, may_squarefree7resume=None, new_resume=False, neg_resume_ok=False):
        del may_primes, may_prime2ok_, to_seq6more
        new_resume, neg_resume_ok
        more, may_squarefree7resume
        return sf.iter7resume__gt1_(may_prev_uint7resume:=may_squarefree7resume, new_resume=new_resume, neg_resume_ok=neg_resume_ok, _more4compatibility=bool(more))
    return iter_sorted_partial_squarefree_uints7mimic_oldAPI_
iter_sorted_partial_squarefree_uints7mimic_oldAPI__7odd_only__7basis_eq_fst_16_odd_primes_ = mk__iter_sorted_partial_squarefree_uints7mimic_oldAPI_(True, (3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59))
    # <<==:
    #   prime_gen 17 | tail -n +2

def iter_sorted_partial_squarefree_uints_(finite_basis, /, *, may_prev_uint7resume=None, odd_only=False, new_resume=False, neg_resume_ok=False, _more4compatibility=False):
    sf = IterSortedPartialSquarefree6finite_basis(odd_only, finite_basis)
    return sf.iter7resume__gt1_(may_prev_uint7resume, new_resume=new_resume, neg_resume_ok=neg_resume_ok, _more4compatibility=_more4compatibility)

def iter_sorted_squarefree_uints_(may_primes=None, /, *, may_prime2ok_=None, more=False, to_seq6more=False, may_squarefree7resume=None, new_resume=False, neg_resume_ok=False):
    '-> Iter (u/squarefree if not more else (u/squarefree, js4ps/rglnkls{j4p}, ps4u/rglnkls{p}, imay_new_prime/(u if ps4u==((), u) else -1))) # imay_new_prime from iter_unsorted_squarefree_uints_()'
    ######################
    if not None is (squarefree7resume:=may_squarefree7resume):
        (squarefree7resume, new_resume) = _std(squarefree7resume, new_resume, neg_resume_ok)
        x2u_ = fst if more else echo
        xs = iter_sorted_squarefree_uints_(may_primes, may_prime2ok_=may_prime2ok_, more=more, to_seq6more=to_seq6more)
        for x in xs:
            u = x2u_(x)
            if not u < squarefree7resume:
                break
        else:
            raise ValueError(squarefree7resume)
        x, u
        if not u == squarefree7resume:raise ValueError(squarefree7resume, u)
        if new_resume:
            yield x
        yield from xs
        return


    ######################
    it8ps = _iter_primes(may_primes, may_prime2ok_)
    #it8ps = ensure_strict_sorted(it8ps)
    # [it8ps :: strict_sorted-Iter prime]
    ######################
    if more:
        if to_seq6more:
            def f_(rglnkls, /):
                return tuple(rglnkls2list(rglnkls))
        else:
            def f_(rglnkls, /):
                return rglnkls
        f_#@more

    ######################
    j2p = []
    777;prev_p = 1
    def j2p_(j, /):
        'j -> p | ^StopIteration'
        nonlocal prev_p
        if j == len(j2p):
            p = next(it8ps)
                # ^StopIteration
            # !! [it8ps :: strict_sorted-Iter prime]
            if not p > prev_p: raise ValueError(prev_p, p)
            777; prev_p = p
            #j4p = len(j2p)
            777;j2p.append(p)
        return j2p[j]

    ######################
    # j2ts = []
        # :: [[(u, lflnkls{j4p}, lflnkls{prime{>=j2p[j]}})]]
        # :: j -> [(u, lflnkls{j4p}, lflnkls{prime{>=j2p[j]}})]
        # :: j -> list(iter_sorted_squarefree_uints_(it8ps[j]))
        # 占用太多空间
    # p, q..., p*q, ...

    ######################
    #sz2ts = [[(1, (), ())]]
        # :: [[(u, js, ps)]]
        # :: sz -> [(u{ps}, js{sz}, ps{js})]
    # [sz2ts[0] == [1]]
    # [map(fst, sz2ts[1]) == primes]


    ######################
    # [record :: (u, js4ps, ps4u)] #rglnkls
    record0 = (1, (), ())
    sorted_iterable_ex = [_record2term6sorted_iterable_ex_(j2p_, record0)]
    sorted_records = merge_ex(sorted_iterable_ex)
    for (u, js4ps, ps4u) in sorted_records:
        yield u if not more else (u, f_(js4ps), f_(ps4u), imay_new_prime:=u if js4ps and not js4ps[0] else -1)
    ######################
def _iter_sorted_records5record_(j2p_, record, /):
    (u, js4ps, ps4u) = record
    j4p = -1 if u == 1 else js4ps[1]
    try:
        while 1:
            j4p += 1
            777;p = j2p_(j4p)
            yield (u*p, (js4ps, j4p), (ps4u, p))
    except StopIteration:
        return

def _record2term6sorted_iterable_ex_(j2p_, record, /):
    sorted_iterable_ex = _leading_record2following_sorted_iterable_ex_(j2p_, record)
    return (record, [sorted_iterable_ex])
def _leading_record2following_sorted_iterable_ex_(j2p_, record, /):
    'record -> sorted_iterable_ex'
    #yield (record, None)
    sorted_records = _iter_sorted_records5record_(j2p_, record)
    for record in sorted_records:
        yield _record2term6sorted_iterable_ex_(j2p_, record)







def iter_sorted_squarefree_uints7mimic_oldAPI__7builtin_data6zpow64_(may_primes=None, /, *, may_prime2ok_=None, more=False, to_seq6more=False, may_squarefree7resume=None, new_resume=False, neg_resume_ok=False):
    ######################
    ls = _us6data6zpow64#us6data4prevnext6zpow64
    ######################
    del may_primes, may_prime2ok_, to_seq6more
    new_resume, neg_resume_ok
    more, may_squarefree7resume
    ######################
    if not None is (squarefree7resume:=may_squarefree7resume):
        (squarefree7resume, new_resume) = _std(squarefree7resume, new_resume, neg_resume_ok)
        j = ls.index(squarefree7resume)
        if not new_resume:
            j += 1
    else:
        j = 0
    j
    ######################
    for j in range(j, len(ls)):
        u = ls[j]
        yield u if not more else (u, None, None, -1)


    ######################
iter_sorted_squarefree_uints7mimic_oldAPI__7builtin_data6zpow64_
_us6data6zpow64 = (
    #extracted from us6data4prevnext6zpow64
    #   442lines
(1
,3
,5
,7
,11
,13
,15
,17
,23
,29
,31
,33
,35
,37
,47
,51
,61
,65
,79
,83
,97
,101
,119
,123
,127
,129
,143
,145
,215
,217
,241
,247
,255
,257
,341
,345
,511
,515
,623
,627
,727
,731
,997
,1001
,1023
,1027
,1295
,1297
,1329
,1333
,1727
,1729
,2047
,2049
,2185
,2189
,2399
,2405
,3121
,3127
,4093
,4097
,6559
,6563
,7773
,7777
,8191
,8193
,9997
,10001
,14639
,14645
,15623
,15627
,16383
,16385
,16805
,16809
,19681
,19685
,20735
,20737
,32767
,32771
,46655
,46657
,59047
,59051
,65535
,65537
,78123
,78127
,99995
,100001
,117647
,117651
,131071
,131073
,161049
,161053
,177145
,177149
,248831
,248833
,262141
,262145
,279935
,279939
,390623
,390629
,524287
,524289
,531439
,531443
,823541
,823547
,999997
,1000001
,1048573
,1048577
,1594321
,1594327
,1679615
,1679617
,1771559
,1771563
,1953123
,1953127
,2097149
,2097155
,2985983
,2985985
,4194303
,4194305
,4782967
,4782971
,5764799
,5764805
,8388607
,8388609
,9765623
,9765627
,9999997
,10000001
,10077695
,10077697
,14348905
,14348909
,16777213
,16777217
,19487167
,19487173
,33554431
,33554433
,35831807
,35831809
,40353605
,40353609
,43046719
,43046727
,48828121
,48828127
,60466173
,60466177
,67108863
,67108865
,99999997
,100000001
,129140161
,129140165
,134217727
,134217731
,214358873
,214358883
,244140623
,244140627
,268435455
,268435457
,282475245
,282475253
,362797055
,362797057
,387420487
,387420491
,429981695
,429981697
,536870911
,536870913
,999999997
,1000000001
,1073741821
,1073741827
,1162261465
,1162261469
,1220703123
,1220703127
,1977326741
,1977326745
,2147483647
,2147483649
,2176782335
,2176782337
,2357947689
,2357947693
,3486784399
,3486784403
,4294967295
,4294967297
,5159780351
,5159780353
,6103515623
,6103515629
,8589934591
,8589934597
,9999999997
,10000000001
,10460353201
,10460353205
,13060694015
,13060694017
,13841287199
,13841287203
,17179869183
,17179869185
,25937424599
,25937424605
,30517578123
,30517578127
,31381059607
,31381059611
,34359738367
,34359738369
,61917364223
,61917364227
,68719476733
,68719476737
,78364164093
,78364164097
,94143178823
,94143178829
,96889010405
,96889010411
,99999999997
,100000000003
,137438953471
,137438953473
,152587890623
,152587890627
,274877906943
,274877906945
,282429536479
,282429536483
,285311670609
,285311670613
,470184984573
,470184984577
,549755813887
,549755813891
,678223072847
,678223072851
,743008370685
,743008370689
,762939453121
,762939453127
,847288609441
,847288609445
,999999999997
,1000000000001
,1099511627773
,1099511627777
,2199023255551
,2199023255553
,2541865828323
,2541865828331
,2821109907455
,2821109907457
,3138428376719
,3138428376723
,3814697265623
,3814697265627
,4398046511101
,4398046511105
,4747561509941
,4747561509945
,7625597484985
,7625597484989
,8796093022207
,8796093022209
,8916100448255
,8916100448257
,9999999999995
,10000000000001
,16926659444735
,16926659444737
,17592186044415
,17592186044417
,19073486328123
,19073486328131
,22876792454959
,22876792454963
,33232930569599
,33232930569605
,34522712143927
,34522712143933
,35184372088831
,35184372088835
,68630377364881
,68630377364885
,70368744177663
,70368744177665
,95367431640623
,95367431640629
,99999999999997
,100000000000001
,101559956668415
,101559956668417
,106993205379071
,106993205379077
,140737488355327
,140737488355329
,205891132094647
,205891132094651
,232630513987205
,232630513987209
,281474976710653
,281474976710657
,379749833583239
,379749833583243
,476837158203123
,476837158203127
,562949953421311
,562949953421313
,609359740010495
,609359740010497
,617673396283945
,617673396283953
,999999999999997
,1000000000000001
,1125899906842623
,1125899906842627
,1283918464548863
,1283918464548865
,1628413597910447
,1628413597910451
,1853020188851839
,1853020188851843
,2251799813685247
,2251799813685251
,2384185791015623
,2384185791015627
,3656158440062973
,3656158440062977
,4177248169415649
,4177248169415653
,4503599627370495
,4503599627370497
,5559060566555521
,5559060566555527
,9007199254740991
,9007199254740993
,9999999999999997
,10000000000000001
,11398895185373141
,11398895185373147
,11920928955078121
,11920928955078127
,15407021574586367
,15407021574586369
,16677181699666567
,16677181699666571
,18014398509481981
,18014398509481985
,21936950640377855
,21936950640377859
,36028797018963967
,36028797018963971
,45949729863572159
,45949729863572165
,50031545098999705
,50031545098999709
,59604644775390623
,59604644775390627
,72057594037927935
,72057594037927937
,79792266297611999
,79792266297612003
,99999999999999997
,100000000000000001
,131621703842267135
,131621703842267137
,144115188075855871
,144115188075855877
,150094635296999119
,150094635296999123
,184884258895036415
,184884258895036417
,288230376151711743
,288230376151711745
,298023223876953123
,298023223876953127
,450283905890997361
,450283905890997365
,505447028499293769
,505447028499293773
,558545864083284005
,558545864083284009
,576460752303423487
,576460752303423489
,789730223053602815
,789730223053602817
,999999999999999997
,1000000000000000001
,1152921504606846973
,1152921504606846977
,1350851717672992087
,1350851717672992091
,1490116119384765623
,1490116119384765629
,2218611106740436991
,2218611106740436993
,2305843009213693951
,2305843009213693953
,3909821048582988047
,3909821048582988053
,4052555153018976265
,4052555153018976269
,4611686018427387903
,4611686018427387905
,4738381338321616895
,4738381338321616897
,5559917313492231479
,5559917313492231483
,7450580596923828123
,7450580596923828127
,9223372036854775805
,9223372036854775811
,9999999999999999997
,10000000000000000001
,12157665459056928799
,12157665459056928803
,18446744073709551615
,18446744073709551617
))







__all__
from seed.math.iter_sorted_squarefree_uints import iter_sorted_squarefree_uints_
#def iter_sorted_squarefree_uints_(may_primes=None, /, *, may_prime2ok_=None, more=False, to_seq6more=False, may_squarefree7resume=None, new_resume=False, neg_resume_ok=False):
#old:def iter_sorted_squarefree_uints_(may_primes=None, /, *, may_prime2ok_=None, more=False, to_seq6more=False):
from seed.math.iter_sorted_squarefree_uints import mk__iter_sorted_partial_squarefree_uints7mimic_oldAPI_, iter_sorted_partial_squarefree_uints7mimic_oldAPI__7odd_only__7basis_eq_fst_16_odd_primes_, iter_sorted_partial_squarefree_uints_, iter_sorted_squarefree_uints7mimic_oldAPI__7builtin_data6zpow64_
from seed.math.iter_sorted_squarefree_uints import IterSortedIndivisible6finite_divisors, IterSortedPartialSquarefree6finite_basis
from seed.math.iter_sorted_squarefree_uints import is_partial_squarefree6finite_basis_
from seed.math.iter_sorted_squarefree_uints import *
