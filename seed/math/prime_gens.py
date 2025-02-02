#__all__:goto
r'''[[[
e ../../python3_src/seed/math/prime_gens.py
    view ../../python3_src/seed/math/is_prime__le_pow2_64.py
        # replaced since 2**64 < A014233[-1]

e ../../python3_src/seed/math/factor_pint_by_trial_division_.py
e ../../python3_src/seed/math/factor_pint_into_strong_pseudoprimes_by_quadratic_sieve_.py

[[
!mv ../../python3_src/seed/math/lazy_prime_seq_by_Eratosthenes_sieve.py ../../python3_src/seed/math/prime_gens.py
.+1,$s/\<lazy_prime_seq_by_Eratosthenes_sieve\>/prime_gens/g
]]
[[
rename:
    to match:
        next_may_prime__le_pow2_81__ge_
        raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_
.+1,$s/\<prev_may_prime__lt_\>/prev_may_prime__le_pow2_81__lt_/g
.+1,$s/\<raw_iter_all_strict_sorted_primes__using_primality_test__lt_\>/raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_/g
]]


seed.math.prime_gens
py -m seed.math.prime_gens
py -m nn_ns.app.debug_cmd   seed.math.prime_gens -x
py -m nn_ns.app.doctest_cmd seed.math.prime_gens:__doc__ -ht #  -ff -v -df
py -m nn_ns.app.doctest_cmd seed.math.prime_gens:__doc__ -ff
py -m nn_ns.app.doctest_cmd seed.math.prime_gens:_doc4tmp_test -ht





from seed.math.prime_gens import detect_strong_pseudoprime__not_waste_too_much_time_

from seed.math.prime_gens import all_prime_factors_gen, tabulate_may_all_prime_factors4uint_lt_

from seed.math.prime_gens import min_prime_factor_gen, tabulate_may_min_prime_factor4uint_lt_, tabulate_may_factorization4uint_lt_



from seed.math.prime_gens import prime_gen__Eratosthenes_sieve, prime_gen__Miller_Rabin_primality_test

from seed.math.prime_gens import prime_gen, prime_filter__using_primality_test_, raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_

from seed.math.prime_gens import is_strong_pseudoprime__basis_, is_prime__using_A014233_, is_prime__le_pow2_81_, is_prime__tribool_, Case4is_prime__tribool_






>>> list_islice_(9, reversed_iter_pseudoprimes__lt_(7))
[5, 3, 2]


py_adhoc_call   seed.math.prime_gens   @raw_list_all_strict_sorted_ints__ge2__with_min_prime_factor__sized_ =200 -to_cache_only_busy_primes_plus_next --may_primes=None

py_adhoc_call   seed.math.prime_gens   @_find_mismatch4diff_cases4is_prime__tribool_
... ...
2**521-1
    # choke here:
    # _find_mismatch4diff_cases4is_prime__tribool_:
    #   r1 = is_prime__tribool_(mn, case=C.ERH)
    # _is_strong_pseudoprime_:
    #   d = pow(base, odd, n)
    #
    # 2*521**2
... ...
2**607-1
    # choke here
... ...
2**1279-1
    # choke here # after add two 'continue' follow r0
... ...
2**2203-1
    # choke here # after add two 'continue' follow r0
    # r0 = is_prime__tribool_(mn, case=C.bit_length)
    #
    # choke here # after add two 'continue' follow r2
... ...
2**3217-1
    # choke here # after add two 'continue' follow r2

(2,3,5,7,13,17,19,31,61,89,107,127,521,607,1279,2203,2281,3217,4253,4423,9689,9941,11213,19937,21701,23209,44497,86243,110503,132049,216091,756839,859433,1257787,1398269,2976221,3021377,6972593,13466917,20996011,24036583,25964951,30402457,32582657,37156667,42643801,43112609,57885161       #unstable: ,74207281,77232917,82589933)
>>> 2*521**2
542882
>>> len([*iter_prime_basis4II_prime_basis_gtN_(2**2203 -1)])
248
>>> calc_len_prime_basis4II_prime_basis_gtN_(2**2203 -1)
248




#>>> from itertools import islice
>>> raw_list_all_strict_sorted_ints__ge2__with_min_prime_factor__sized_(200, to_cache_only_busy_primes_plus_next=False, may_primes=None)
[(2, 2), (3, 3), (4, 2), (5, 5), (6, 2), (7, 7), (8, 2), (9, 3), (10, 2), (11, 11), (12, 2), (13, 13), (14, 2), (15, 3), (16, 2), (17, 17), (18, 2), (19, 19), (20, 2), (21, 3), (22, 2), (23, 23), (24, 2), (25, 5), (26, 2), (27, 3), (28, 2), (29, 29), (30, 2), (31, 31), (32, 2), (33, 3), (34, 2), (35, 5), (36, 2), (37, 37), (38, 2), (39, 3), (40, 2), (41, 41), (42, 2), (43, 43), (44, 2), (45, 3), (46, 2), (47, 47), (48, 2), (49, 7), (50, 2), (51, 3), (52, 2), (53, 53), (54, 2), (55, 5), (56, 2), (57, 3), (58, 2), (59, 59), (60, 2), (61, 61), (62, 2), (63, 3), (64, 2), (65, 5), (66, 2), (67, 67), (68, 2), (69, 3), (70, 2), (71, 71), (72, 2), (73, 73), (74, 2), (75, 3), (76, 2), (77, 7), (78, 2), (79, 79), (80, 2), (81, 3), (82, 2), (83, 83), (84, 2), (85, 5), (86, 2), (87, 3), (88, 2), (89, 89), (90, 2), (91, 7), (92, 2), (93, 3), (94, 2), (95, 5), (96, 2), (97, 97), (98, 2), (99, 3), (100, 2), (101, 101), (102, 2), (103, 103), (104, 2), (105, 3), (106, 2), (107, 107), (108, 2), (109, 109), (110, 2), (111, 3), (112, 2), (113, 113), (114, 2), (115, 5), (116, 2), (117, 3), (118, 2), (119, 7), (120, 2), (121, 11), (122, 2), (123, 3), (124, 2), (125, 5), (126, 2), (127, 127), (128, 2), (129, 3), (130, 2), (131, 131), (132, 2), (133, 7), (134, 2), (135, 3), (136, 2), (137, 137), (138, 2), (139, 139), (140, 2), (141, 3), (142, 2), (143, 11), (144, 2), (145, 5), (146, 2), (147, 3), (148, 2), (149, 149), (150, 2), (151, 151), (152, 2), (153, 3), (154, 2), (155, 5), (156, 2), (157, 157), (158, 2), (159, 3), (160, 2), (161, 7), (162, 2), (163, 163), (164, 2), (165, 3), (166, 2), (167, 167), (168, 2), (169, 13), (170, 2), (171, 3), (172, 2), (173, 173), (174, 2), (175, 5), (176, 2), (177, 3), (178, 2), (179, 179), (180, 2), (181, 181), (182, 2), (183, 3), (184, 2), (185, 5), (186, 2), (187, 11), (188, 2), (189, 3), (190, 2), (191, 191), (192, 2), (193, 193), (194, 2), (195, 3), (196, 2), (197, 197), (198, 2), (199, 199), (200, 2), (201, 3)]





>>> list_islice_(200, raw_iter_all_strict_sorted_primes_(to_cache_only_busy_primes_plus_next=False, may_primes=None))
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223]




>>> raw_list_all_strict_sorted_primes__lt_(200, to_cache_only_busy_primes_plus_next=False, may_primes=None)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]






>>> def f(sz, /, *, to_cache_only_busy_primes_plus_next):
...   if 1:
...     primes = []
...     ihead2may_itail = []
...     lmay_offset = []
...     offsetted_sieve = []
...     it = raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_(may_primes=primes, ihead2may_itail=ihead2may_itail, offsetted_sieve=offsetted_sieve, lmay_offset=lmay_offset, to_cache_only_busy_primes_plus_next=to_cache_only_busy_primes_plus_next)
...     nm4primes = 'only_busy_primes_plus_next' if to_cache_only_busy_primes_plus_next else 'cached_primes'
...   def g(it, /):
...     print('(n, min_prime_factor) =', next(it))
...     print(f'{nm4primes} =', primes)
...     print('ihead2may_itail =', ihead2may_itail)
...     print('offset =', *lmay_offset)
...     print('offsetted_sieve =', offsetted_sieve)
...   if 1:
...     for _ in range(sz):g(it)
...   return






















>>> f(85, to_cache_only_busy_primes_plus_next=False)
(n, min_prime_factor) = (2, 2)
cached_primes = [2]
ihead2may_itail = []
offset = 3
offsetted_sieve = []
(n, min_prime_factor) = (3, 3)
cached_primes = [2, 3]
ihead2may_itail = []
offset = 4
offsetted_sieve = []
(n, min_prime_factor) = (4, 2)
cached_primes = [2, 3]
ihead2may_itail = [None]
offset = 5
offsetted_sieve = []
(n, min_prime_factor) = (5, 5)
cached_primes = [2, 3, 5]
ihead2may_itail = [None]
offset = 5
offsetted_sieve = [-1, 0]
(n, min_prime_factor) = (6, 2)
cached_primes = [2, 3, 5]
ihead2may_itail = [None]
offset = 7
offsetted_sieve = []
(n, min_prime_factor) = (7, 7)
cached_primes = [2, 3, 5, 7]
ihead2may_itail = [None]
offset = 7
offsetted_sieve = [-1, 0]
(n, min_prime_factor) = (8, 2)
cached_primes = [2, 3, 5, 7]
ihead2may_itail = [None]
offset = 9
offsetted_sieve = []
(n, min_prime_factor) = (9, 3)
cached_primes = [2, 3, 5, 7]
ihead2may_itail = [None, None]
offset = 9
offsetted_sieve = [-1, 0]
(n, min_prime_factor) = (10, 2)
cached_primes = [2, 3, 5, 7]
ihead2may_itail = [None, None]
offset = 9
offsetted_sieve = [-1, -1, None, 1]
(n, min_prime_factor) = (11, 11)
cached_primes = [2, 3, 5, 7, 11]
ihead2may_itail = [1, None]
offset = 12
offsetted_sieve = [0]
(n, min_prime_factor) = (12, 2)
cached_primes = [2, 3, 5, 7, 11]
ihead2may_itail = [1, None]
offset = 13
offsetted_sieve = []
(n, min_prime_factor) = (13, 13)
cached_primes = [2, 3, 5, 7, 11, 13]
ihead2may_itail = [None, None]
offset = 13
offsetted_sieve = [-1, 0, 1]
(n, min_prime_factor) = (14, 2)
cached_primes = [2, 3, 5, 7, 11, 13]
ihead2may_itail = [None, None]
offset = 15
offsetted_sieve = [1]
(n, min_prime_factor) = (15, 3)
cached_primes = [2, 3, 5, 7, 11, 13]
ihead2may_itail = [None, None]
offset = 15
offsetted_sieve = [-1, 0]
(n, min_prime_factor) = (16, 2)
cached_primes = [2, 3, 5, 7, 11, 13]
ihead2may_itail = [None, None]
offset = 15
offsetted_sieve = [-1, -1, None, 1]
(n, min_prime_factor) = (17, 17)
cached_primes = [2, 3, 5, 7, 11, 13, 17]
ihead2may_itail = [1, None]
offset = 18
offsetted_sieve = [0]
(n, min_prime_factor) = (18, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17]
ihead2may_itail = [1, None]
offset = 19
offsetted_sieve = []
(n, min_prime_factor) = (19, 19)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19]
ihead2may_itail = [None, None]
offset = 19
offsetted_sieve = [-1, 0, 1]
(n, min_prime_factor) = (20, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19]
ihead2may_itail = [None, None]
offset = 21
offsetted_sieve = [1]
(n, min_prime_factor) = (21, 3)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19]
ihead2may_itail = [None, None]
offset = 21
offsetted_sieve = [-1, 0]
(n, min_prime_factor) = (22, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19]
ihead2may_itail = [None, None]
offset = 21
offsetted_sieve = [-1, -1, None, 1]
(n, min_prime_factor) = (23, 23)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
ihead2may_itail = [1, None]
offset = 24
offsetted_sieve = [0]
(n, min_prime_factor) = (24, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
ihead2may_itail = [1, None]
offset = 25
offsetted_sieve = []
(n, min_prime_factor) = (25, 5)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
ihead2may_itail = [None, None, None]
offset = 25
offsetted_sieve = [-1, 0, 1]
(n, min_prime_factor) = (26, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
ihead2may_itail = [None, None, None]
offset = 25
offsetted_sieve = [-1, -1, 1, None, None, 2]
(n, min_prime_factor) = (27, 3)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
ihead2may_itail = [None, None, None]
offset = 25
offsetted_sieve = [-1, -1, -1, 0, None, 2]
(n, min_prime_factor) = (28, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
ihead2may_itail = [None, 2, None]
offset = 29
offsetted_sieve = [None, 1]
(n, min_prime_factor) = (29, 29)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
ihead2may_itail = [1, 2, None]
offset = 29
offsetted_sieve = [-1, 0]
(n, min_prime_factor) = (30, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
ihead2may_itail = [1, 2, None]
offset = 31
offsetted_sieve = []
(n, min_prime_factor) = (31, 31)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
ihead2may_itail = [None, None, None]
offset = 31
offsetted_sieve = [-1, 0, 1, None, 2]
(n, min_prime_factor) = (32, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
ihead2may_itail = [None, None, None]
offset = 31
offsetted_sieve = [-1, -1, 1, None, 2]
(n, min_prime_factor) = (33, 3)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
ihead2may_itail = [None, None, None]
offset = 31
offsetted_sieve = [-1, -1, -1, 0, 2]
(n, min_prime_factor) = (34, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
ihead2may_itail = [None, None, None]
offset = 35
offsetted_sieve = [2, 1]
(n, min_prime_factor) = (35, 5)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
ihead2may_itail = [1, None, None]
offset = 35
offsetted_sieve = [-1, 0]
(n, min_prime_factor) = (36, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
ihead2may_itail = [1, None, None]
offset = 35
offsetted_sieve = [-1, -1, None, None, None, 2]
(n, min_prime_factor) = (37, 37)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
ihead2may_itail = [None, None, None]
offset = 35
offsetted_sieve = [-1, -1, -1, 0, 1, 2]
(n, min_prime_factor) = (38, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
ihead2may_itail = [None, None, None]
offset = 39
offsetted_sieve = [1, 2]
(n, min_prime_factor) = (39, 3)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
ihead2may_itail = [2, None, None]
offset = 39
offsetted_sieve = [-1, 0]
(n, min_prime_factor) = (40, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
ihead2may_itail = [2, None, None]
offset = 39
offsetted_sieve = [-1, -1, None, 1]
(n, min_prime_factor) = (41, 41)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
ihead2may_itail = [1, None, None]
offset = 39
offsetted_sieve = [-1, -1, -1, 0, None, None, 2]
(n, min_prime_factor) = (42, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
ihead2may_itail = [1, None, None]
offset = 39
offsetted_sieve = [-1, -1, -1, -1, None, None, 2]
(n, min_prime_factor) = (43, 43)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
ihead2may_itail = [None, 2, None]
offset = 44
offsetted_sieve = [0, 1]
(n, min_prime_factor) = (44, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
ihead2may_itail = [None, 2, None]
offset = 44
offsetted_sieve = [-1, 1]
(n, min_prime_factor) = (45, 3)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
ihead2may_itail = [None, 2, None]
offset = 46
offsetted_sieve = [0]
(n, min_prime_factor) = (46, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
ihead2may_itail = [None, None, None]
offset = 46
offsetted_sieve = [-1, None, 1, None, 2]
(n, min_prime_factor) = (47, 47)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
ihead2may_itail = [1, None, None]
offset = 46
offsetted_sieve = [-1, -1, 0, None, 2]
(n, min_prime_factor) = (48, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
ihead2may_itail = [1, None, None]
offset = 46
offsetted_sieve = [-1, -1, -1, None, 2]
(n, min_prime_factor) = (49, 7)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
ihead2may_itail = [2, None, None, None]
offset = 50
offsetted_sieve = [0, 1]
(n, min_prime_factor) = (50, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
ihead2may_itail = [2, None, None, None]
offset = 50
offsetted_sieve = [-1, 1, None, None, None, None, 3]
(n, min_prime_factor) = (51, 3)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
ihead2may_itail = [None, None, None, None]
offset = 50
offsetted_sieve = [-1, -1, 0, None, None, 2, 3]
(n, min_prime_factor) = (52, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
ihead2may_itail = [None, None, None, None]
offset = 50
offsetted_sieve = [-1, -1, -1, None, 1, 2, 3]
(n, min_prime_factor) = (53, 53)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
ihead2may_itail = [1, None, None, None]
offset = 50
offsetted_sieve = [-1, -1, -1, -1, 0, 2, 3]
(n, min_prime_factor) = (54, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
ihead2may_itail = [1, None, None, None]
offset = 55
offsetted_sieve = [2, 3]
(n, min_prime_factor) = (55, 5)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
ihead2may_itail = [3, None, None, None]
offset = 55
offsetted_sieve = [-1, 0, 1]
(n, min_prime_factor) = (56, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
ihead2may_itail = [3, None, None, None]
offset = 55
offsetted_sieve = [-1, -1, 1, None, None, 2]
(n, min_prime_factor) = (57, 3)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
ihead2may_itail = [None, None, None, None]
offset = 55
offsetted_sieve = [-1, -1, -1, 0, None, 2, None, None, 3]
(n, min_prime_factor) = (58, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
ihead2may_itail = [None, 2, None, None]
offset = 55
offsetted_sieve = [-1, -1, -1, -1, None, 1, None, None, 3]
(n, min_prime_factor) = (59, 59)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
ihead2may_itail = [1, 2, None, None]
offset = 55
offsetted_sieve = [-1, -1, -1, -1, -1, 0, None, None, 3]
(n, min_prime_factor) = (60, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
ihead2may_itail = [1, 2, None, None]
offset = 61
offsetted_sieve = [None, None, 3]
(n, min_prime_factor) = (61, 61)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
ihead2may_itail = [None, 3, None, None]
offset = 61
offsetted_sieve = [-1, 0, 1, None, 2]
(n, min_prime_factor) = (62, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
ihead2may_itail = [None, 3, None, None]
offset = 61
offsetted_sieve = [-1, -1, 1, None, 2]
(n, min_prime_factor) = (63, 3)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
ihead2may_itail = [None, 3, None, None]
offset = 61
offsetted_sieve = [-1, -1, -1, 0, 2]
(n, min_prime_factor) = (64, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
ihead2may_itail = [None, None, None, None]
offset = 61
offsetted_sieve = [-1, -1, -1, -1, 2, 1, None, None, None, 3]
(n, min_prime_factor) = (65, 5)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
ihead2may_itail = [1, None, None, None]
offset = 61
offsetted_sieve = [-1, -1, -1, -1, -1, 0, None, None, None, 3]
(n, min_prime_factor) = (66, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
ihead2may_itail = [1, None, 3, None]
offset = 61
offsetted_sieve = [-1, -1, -1, -1, -1, -1, None, None, None, 2]
(n, min_prime_factor) = (67, 67)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
ihead2may_itail = [None, None, 3, None]
offset = 68
offsetted_sieve = [0, 1, 2]
(n, min_prime_factor) = (68, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
ihead2may_itail = [None, None, 3, None]
offset = 68
offsetted_sieve = [-1, 1, 2]
(n, min_prime_factor) = (69, 3)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
ihead2may_itail = [2, None, 3, None]
offset = 70
offsetted_sieve = [0]
(n, min_prime_factor) = (70, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
ihead2may_itail = [2, None, 3, None]
offset = 70
offsetted_sieve = [-1, None, 1]
(n, min_prime_factor) = (71, 71)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
ihead2may_itail = [1, None, None, None]
offset = 70
offsetted_sieve = [-1, -1, 0, None, None, 2, None, 3]
(n, min_prime_factor) = (72, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
ihead2may_itail = [1, None, None, None]
offset = 70
offsetted_sieve = [-1, -1, -1, None, None, 2, None, 3]
(n, min_prime_factor) = (73, 73)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
ihead2may_itail = [None, 2, None, None]
offset = 70
offsetted_sieve = [-1, -1, -1, -1, 0, 1, None, 3]
(n, min_prime_factor) = (74, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
ihead2may_itail = [None, 2, None, None]
offset = 70
offsetted_sieve = [-1, -1, -1, -1, -1, 1, None, 3]
(n, min_prime_factor) = (75, 3)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
ihead2may_itail = [None, 2, None, None]
offset = 76
offsetted_sieve = [0, 3]
(n, min_prime_factor) = (76, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
ihead2may_itail = [None, None, None, None]
offset = 76
offsetted_sieve = [-1, 3, 1, None, 2]
(n, min_prime_factor) = (77, 7)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
ihead2may_itail = [1, None, None, None]
offset = 76
offsetted_sieve = [-1, -1, 0, None, 2]
(n, min_prime_factor) = (78, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
ihead2may_itail = [1, None, None, None]
offset = 76
offsetted_sieve = [-1, -1, -1, None, 2, None, None, None, 3]
(n, min_prime_factor) = (79, 79)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]
ihead2may_itail = [2, None, None, None]
offset = 76
offsetted_sieve = [-1, -1, -1, -1, 0, 1, None, None, 3]
(n, min_prime_factor) = (80, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]
ihead2may_itail = [2, None, None, None]
offset = 76
offsetted_sieve = [-1, -1, -1, -1, -1, 1, None, None, 3]
(n, min_prime_factor) = (81, 3)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]
ihead2may_itail = [None, None, None, None]
offset = 76
offsetted_sieve = [-1, -1, -1, -1, -1, -1, 0, None, 3, 2]
(n, min_prime_factor) = (82, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]
ihead2may_itail = [None, 3, None, None]
offset = 83
offsetted_sieve = [None, 1, 2]
(n, min_prime_factor) = (83, 83)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83]
ihead2may_itail = [1, 3, None, None]
offset = 83
offsetted_sieve = [-1, 0, 2]
(n, min_prime_factor) = (84, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83]
ihead2may_itail = [1, 3, None, None]
offset = 85
offsetted_sieve = [2]
(n, min_prime_factor) = (85, 5)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83]
ihead2may_itail = [None, None, None, None]
offset = 85
offsetted_sieve = [-1, 0, 1, None, None, None, 3]
(n, min_prime_factor) = (86, 2)
cached_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83]
ihead2may_itail = [None, None, None, None]
offset = 85
offsetted_sieve = [-1, -1, 1, None, None, 2, 3]























>>> f(85, to_cache_only_busy_primes_plus_next=True)
(n, min_prime_factor) = (2, 2)
only_busy_primes_plus_next = [2]
ihead2may_itail = []
offset = 3
offsetted_sieve = []
(n, min_prime_factor) = (3, 3)
only_busy_primes_plus_next = [2]
ihead2may_itail = []
offset = 4
offsetted_sieve = []
(n, min_prime_factor) = (4, 2)
only_busy_primes_plus_next = [2, 3]
ihead2may_itail = [None]
offset = 5
offsetted_sieve = []
(n, min_prime_factor) = (5, 5)
only_busy_primes_plus_next = [2, 3]
ihead2may_itail = [None]
offset = 5
offsetted_sieve = [-1, 0]
(n, min_prime_factor) = (6, 2)
only_busy_primes_plus_next = [2, 3]
ihead2may_itail = [None]
offset = 7
offsetted_sieve = []
(n, min_prime_factor) = (7, 7)
only_busy_primes_plus_next = [2, 3]
ihead2may_itail = [None]
offset = 7
offsetted_sieve = [-1, 0]
(n, min_prime_factor) = (8, 2)
only_busy_primes_plus_next = [2, 3]
ihead2may_itail = [None]
offset = 9
offsetted_sieve = []
(n, min_prime_factor) = (9, 3)
only_busy_primes_plus_next = [2, 3, 5]
ihead2may_itail = [None, None]
offset = 9
offsetted_sieve = [-1, 0]
(n, min_prime_factor) = (10, 2)
only_busy_primes_plus_next = [2, 3, 5]
ihead2may_itail = [None, None]
offset = 9
offsetted_sieve = [-1, -1, None, 1]
(n, min_prime_factor) = (11, 11)
only_busy_primes_plus_next = [2, 3, 5]
ihead2may_itail = [1, None]
offset = 12
offsetted_sieve = [0]
(n, min_prime_factor) = (12, 2)
only_busy_primes_plus_next = [2, 3, 5]
ihead2may_itail = [1, None]
offset = 13
offsetted_sieve = []
(n, min_prime_factor) = (13, 13)
only_busy_primes_plus_next = [2, 3, 5]
ihead2may_itail = [None, None]
offset = 13
offsetted_sieve = [-1, 0, 1]
(n, min_prime_factor) = (14, 2)
only_busy_primes_plus_next = [2, 3, 5]
ihead2may_itail = [None, None]
offset = 15
offsetted_sieve = [1]
(n, min_prime_factor) = (15, 3)
only_busy_primes_plus_next = [2, 3, 5]
ihead2may_itail = [None, None]
offset = 15
offsetted_sieve = [-1, 0]
(n, min_prime_factor) = (16, 2)
only_busy_primes_plus_next = [2, 3, 5]
ihead2may_itail = [None, None]
offset = 15
offsetted_sieve = [-1, -1, None, 1]
(n, min_prime_factor) = (17, 17)
only_busy_primes_plus_next = [2, 3, 5]
ihead2may_itail = [1, None]
offset = 18
offsetted_sieve = [0]
(n, min_prime_factor) = (18, 2)
only_busy_primes_plus_next = [2, 3, 5]
ihead2may_itail = [1, None]
offset = 19
offsetted_sieve = []
(n, min_prime_factor) = (19, 19)
only_busy_primes_plus_next = [2, 3, 5]
ihead2may_itail = [None, None]
offset = 19
offsetted_sieve = [-1, 0, 1]
(n, min_prime_factor) = (20, 2)
only_busy_primes_plus_next = [2, 3, 5]
ihead2may_itail = [None, None]
offset = 21
offsetted_sieve = [1]
(n, min_prime_factor) = (21, 3)
only_busy_primes_plus_next = [2, 3, 5]
ihead2may_itail = [None, None]
offset = 21
offsetted_sieve = [-1, 0]
(n, min_prime_factor) = (22, 2)
only_busy_primes_plus_next = [2, 3, 5]
ihead2may_itail = [None, None]
offset = 21
offsetted_sieve = [-1, -1, None, 1]
(n, min_prime_factor) = (23, 23)
only_busy_primes_plus_next = [2, 3, 5]
ihead2may_itail = [1, None]
offset = 24
offsetted_sieve = [0]
(n, min_prime_factor) = (24, 2)
only_busy_primes_plus_next = [2, 3, 5]
ihead2may_itail = [1, None]
offset = 25
offsetted_sieve = []
(n, min_prime_factor) = (25, 5)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [None, None, None]
offset = 25
offsetted_sieve = [-1, 0, 1]
(n, min_prime_factor) = (26, 2)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [None, None, None]
offset = 25
offsetted_sieve = [-1, -1, 1, None, None, 2]
(n, min_prime_factor) = (27, 3)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [None, None, None]
offset = 25
offsetted_sieve = [-1, -1, -1, 0, None, 2]
(n, min_prime_factor) = (28, 2)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [None, 2, None]
offset = 29
offsetted_sieve = [None, 1]
(n, min_prime_factor) = (29, 29)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [1, 2, None]
offset = 29
offsetted_sieve = [-1, 0]
(n, min_prime_factor) = (30, 2)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [1, 2, None]
offset = 31
offsetted_sieve = []
(n, min_prime_factor) = (31, 31)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [None, None, None]
offset = 31
offsetted_sieve = [-1, 0, 1, None, 2]
(n, min_prime_factor) = (32, 2)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [None, None, None]
offset = 31
offsetted_sieve = [-1, -1, 1, None, 2]
(n, min_prime_factor) = (33, 3)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [None, None, None]
offset = 31
offsetted_sieve = [-1, -1, -1, 0, 2]
(n, min_prime_factor) = (34, 2)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [None, None, None]
offset = 35
offsetted_sieve = [2, 1]
(n, min_prime_factor) = (35, 5)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [1, None, None]
offset = 35
offsetted_sieve = [-1, 0]
(n, min_prime_factor) = (36, 2)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [1, None, None]
offset = 35
offsetted_sieve = [-1, -1, None, None, None, 2]
(n, min_prime_factor) = (37, 37)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [None, None, None]
offset = 35
offsetted_sieve = [-1, -1, -1, 0, 1, 2]
(n, min_prime_factor) = (38, 2)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [None, None, None]
offset = 39
offsetted_sieve = [1, 2]
(n, min_prime_factor) = (39, 3)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [2, None, None]
offset = 39
offsetted_sieve = [-1, 0]
(n, min_prime_factor) = (40, 2)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [2, None, None]
offset = 39
offsetted_sieve = [-1, -1, None, 1]
(n, min_prime_factor) = (41, 41)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [1, None, None]
offset = 39
offsetted_sieve = [-1, -1, -1, 0, None, None, 2]
(n, min_prime_factor) = (42, 2)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [1, None, None]
offset = 39
offsetted_sieve = [-1, -1, -1, -1, None, None, 2]
(n, min_prime_factor) = (43, 43)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [None, 2, None]
offset = 44
offsetted_sieve = [0, 1]
(n, min_prime_factor) = (44, 2)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [None, 2, None]
offset = 44
offsetted_sieve = [-1, 1]
(n, min_prime_factor) = (45, 3)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [None, 2, None]
offset = 46
offsetted_sieve = [0]
(n, min_prime_factor) = (46, 2)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [None, None, None]
offset = 46
offsetted_sieve = [-1, None, 1, None, 2]
(n, min_prime_factor) = (47, 47)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [1, None, None]
offset = 46
offsetted_sieve = [-1, -1, 0, None, 2]
(n, min_prime_factor) = (48, 2)
only_busy_primes_plus_next = [2, 3, 5, 7]
ihead2may_itail = [1, None, None]
offset = 46
offsetted_sieve = [-1, -1, -1, None, 2]
(n, min_prime_factor) = (49, 7)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [2, None, None, None]
offset = 50
offsetted_sieve = [0, 1]
(n, min_prime_factor) = (50, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [2, None, None, None]
offset = 50
offsetted_sieve = [-1, 1, None, None, None, None, 3]
(n, min_prime_factor) = (51, 3)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, None, None, None]
offset = 50
offsetted_sieve = [-1, -1, 0, None, None, 2, 3]
(n, min_prime_factor) = (52, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, None, None, None]
offset = 50
offsetted_sieve = [-1, -1, -1, None, 1, 2, 3]
(n, min_prime_factor) = (53, 53)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [1, None, None, None]
offset = 50
offsetted_sieve = [-1, -1, -1, -1, 0, 2, 3]
(n, min_prime_factor) = (54, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [1, None, None, None]
offset = 55
offsetted_sieve = [2, 3]
(n, min_prime_factor) = (55, 5)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [3, None, None, None]
offset = 55
offsetted_sieve = [-1, 0, 1]
(n, min_prime_factor) = (56, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [3, None, None, None]
offset = 55
offsetted_sieve = [-1, -1, 1, None, None, 2]
(n, min_prime_factor) = (57, 3)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, None, None, None]
offset = 55
offsetted_sieve = [-1, -1, -1, 0, None, 2, None, None, 3]
(n, min_prime_factor) = (58, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, 2, None, None]
offset = 55
offsetted_sieve = [-1, -1, -1, -1, None, 1, None, None, 3]
(n, min_prime_factor) = (59, 59)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [1, 2, None, None]
offset = 55
offsetted_sieve = [-1, -1, -1, -1, -1, 0, None, None, 3]
(n, min_prime_factor) = (60, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [1, 2, None, None]
offset = 61
offsetted_sieve = [None, None, 3]
(n, min_prime_factor) = (61, 61)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, 3, None, None]
offset = 61
offsetted_sieve = [-1, 0, 1, None, 2]
(n, min_prime_factor) = (62, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, 3, None, None]
offset = 61
offsetted_sieve = [-1, -1, 1, None, 2]
(n, min_prime_factor) = (63, 3)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, 3, None, None]
offset = 61
offsetted_sieve = [-1, -1, -1, 0, 2]
(n, min_prime_factor) = (64, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, None, None, None]
offset = 61
offsetted_sieve = [-1, -1, -1, -1, 2, 1, None, None, None, 3]
(n, min_prime_factor) = (65, 5)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [1, None, None, None]
offset = 61
offsetted_sieve = [-1, -1, -1, -1, -1, 0, None, None, None, 3]
(n, min_prime_factor) = (66, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [1, None, 3, None]
offset = 61
offsetted_sieve = [-1, -1, -1, -1, -1, -1, None, None, None, 2]
(n, min_prime_factor) = (67, 67)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, None, 3, None]
offset = 68
offsetted_sieve = [0, 1, 2]
(n, min_prime_factor) = (68, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, None, 3, None]
offset = 68
offsetted_sieve = [-1, 1, 2]
(n, min_prime_factor) = (69, 3)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [2, None, 3, None]
offset = 70
offsetted_sieve = [0]
(n, min_prime_factor) = (70, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [2, None, 3, None]
offset = 70
offsetted_sieve = [-1, None, 1]
(n, min_prime_factor) = (71, 71)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [1, None, None, None]
offset = 70
offsetted_sieve = [-1, -1, 0, None, None, 2, None, 3]
(n, min_prime_factor) = (72, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [1, None, None, None]
offset = 70
offsetted_sieve = [-1, -1, -1, None, None, 2, None, 3]
(n, min_prime_factor) = (73, 73)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, 2, None, None]
offset = 70
offsetted_sieve = [-1, -1, -1, -1, 0, 1, None, 3]
(n, min_prime_factor) = (74, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, 2, None, None]
offset = 70
offsetted_sieve = [-1, -1, -1, -1, -1, 1, None, 3]
(n, min_prime_factor) = (75, 3)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, 2, None, None]
offset = 76
offsetted_sieve = [0, 3]
(n, min_prime_factor) = (76, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, None, None, None]
offset = 76
offsetted_sieve = [-1, 3, 1, None, 2]
(n, min_prime_factor) = (77, 7)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [1, None, None, None]
offset = 76
offsetted_sieve = [-1, -1, 0, None, 2]
(n, min_prime_factor) = (78, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [1, None, None, None]
offset = 76
offsetted_sieve = [-1, -1, -1, None, 2, None, None, None, 3]
(n, min_prime_factor) = (79, 79)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [2, None, None, None]
offset = 76
offsetted_sieve = [-1, -1, -1, -1, 0, 1, None, None, 3]
(n, min_prime_factor) = (80, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [2, None, None, None]
offset = 76
offsetted_sieve = [-1, -1, -1, -1, -1, 1, None, None, 3]
(n, min_prime_factor) = (81, 3)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, None, None, None]
offset = 76
offsetted_sieve = [-1, -1, -1, -1, -1, -1, 0, None, 3, 2]
(n, min_prime_factor) = (82, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, 3, None, None]
offset = 83
offsetted_sieve = [None, 1, 2]
(n, min_prime_factor) = (83, 83)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [1, 3, None, None]
offset = 83
offsetted_sieve = [-1, 0, 2]
(n, min_prime_factor) = (84, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [1, 3, None, None]
offset = 85
offsetted_sieve = [2]
(n, min_prime_factor) = (85, 5)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, None, None, None]
offset = 85
offsetted_sieve = [-1, 0, 1, None, None, None, 3]
(n, min_prime_factor) = (86, 2)
only_busy_primes_plus_next = [2, 3, 5, 7, 11]
ihead2may_itail = [None, None, None, None]
offset = 85
offsetted_sieve = [-1, -1, 1, None, None, 2, 3]



>>> [*raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_(200)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
>>> len(_)
46

>>> prime_gen[:46]
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199)
>>> prime_gen[...]
LazyList([<...>])
>>> prime_gen()
LazySeq(LazyList([<...>]))
>>> list_islice_(13, iter(prime_gen))
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
>>> lazy_prime_seq = prime_gen.get_or_mk_lazy_prime_seq_()
>>> lazy_prime_seq is prime_gen.get_or_mk_lazy_prime_seq_()
True
>>> prime_gen.get_or_mk_global_singleton_() is lazy_prime_seq
True
>>> prime_gen.remove_global_singleton_()
>>> w = _ref(lazy_prime_seq)
>>> lazy_prime_seq is w()
True
>>> del lazy_prime_seq
>>> None is w()
True
>>> prime_gen.get_or_mk_global_singleton_()
LazySeq(LazyList([<...>]))



>>> prime_gen is prime_gen__Eratosthenes_sieve
True
>>> prime_gen is prime_gen__Miller_Rabin_primality_test
False


>>> prime_gen2 = prime_gen__Miller_Rabin_primality_test

>>> prime_gen2[:46]
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199)
>>> prime_gen2[...]
LazyList([<...>])
>>> prime_gen2()
LazySeq(LazyList([<...>]))
>>> list_islice_(13, iter(prime_gen2))
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
>>> lazy_prime_seq = prime_gen2.get_or_mk_lazy_prime_seq_()
>>> lazy_prime_seq is prime_gen2.get_or_mk_lazy_prime_seq_()
True
>>> prime_gen2.get_or_mk_global_singleton_() is lazy_prime_seq
True
>>> prime_gen2.remove_global_singleton_()
>>> w = _ref(lazy_prime_seq)
>>> lazy_prime_seq is w()
True
>>> del lazy_prime_seq
>>> None is w()
True
>>> prime_gen2.get_or_mk_global_singleton_()
LazySeq(LazyList([<...>]))
>>> prime_gen2.get_or_mk_global_singleton_() is prime_gen2.get_or_mk_global_singleton_()
True
>>> prime_gen2.get_or_mk_global_singleton_() is prime_gen.get_or_mk_global_singleton_()
False
>>> prime_gen.get_or_mk_global_singleton_() is prime_gen.get_or_mk_global_singleton_()
True




>>> len(A014233)
13
>>> 2**81 < A014233[-1] < 2**82
True
>>> is_prime__using_A014233_.upperbound - A014233[-1]
142

#bug:>>> _find_min4ERH_()
(1048577, 21)

#>>> for p in prime_gen:is_prime__tribool_(p, case=???)
    #see:_find_mismatch4diff_cases4is_prime__tribool_


>>> prime_basis4A014233[-1]
41
>>> next(prime_gen.iter__ge_(1+prime_basis4A014233[-1]))
43








>>> min_prime_factor_gen.get_or_mk_lazy_min_prime_factor_seq_()
LazySeq(LazyList([<...>]))
>>> min_prime_factor_gen.get_or_mk_lazy_min_prime_factor_seq_()[:20]
(None, None, 2, 3, 2, 5, 2, 7, 2, 3, 2, 11, 2, 13, 2, 3, 2, 17, 2, 19)
>>> tabulate_may_min_prime_factor4uint_lt_(20)
(None, None, 2, 3, 2, 5, 2, 7, 2, 3, 2, 11, 2, 13, 2, 3, 2, 17, 2, 19)
>>> stable_list_islice_(999, tabulate_may_factorization4uint_lt_(20))
[None
,{}
,{2: 1}
,{3: 1}
,{2: 2}
,{5: 1}
,{2: 1, 3: 1}
,{7: 1}
,{2: 3}
,{3: 2}
,{2: 1, 5: 1}
,{11: 1}
,{2: 2, 3: 1}
,{13: 1}
,{2: 1, 7: 1}
,{3: 1, 5: 1}
,{2: 4}
,{17: 1}
,{2: 1, 3: 2}
,{19: 1}
]



>>> tabulate_may_min_prime_factor4uint_lt_(2)
(None, None)
>>> tabulate_may_min_prime_factor4uint_lt_(1)
(None,)
>>> tabulate_may_min_prime_factor4uint_lt_(0)
()
>>> tabulate_may_min_prime_factor4uint_lt_(-1)
Traceback (most recent call last):
    ...
TypeError: -1

>>> tabulate_may_factorization4uint_lt_(2)
(None, {})
>>> tabulate_may_factorization4uint_lt_(1)
(None,)
>>> tabulate_may_factorization4uint_lt_(0)
()
>>> tabulate_may_factorization4uint_lt_(-1)
Traceback (most recent call last):
    ...
TypeError: -1





>>> all_prime_factors_gen.get_or_mk_lazy_all_prime_factors_seq_()
LazySeq(LazyList([<...>]))
>>> all_prime_factors_gen.get_or_mk_lazy_all_prime_factors_seq_()[:20]
(None, (), (2,), (3,), (2,), (5,), (2, 3), (7,), (2,), (3,), (2, 5), (11,), (2, 3), (13,), (2, 7), (3, 5), (2,), (17,), (2, 3), (19,))
>>> tabulate_may_all_prime_factors4uint_lt_(20)
(None, (), (2,), (3,), (2,), (5,), (2, 3), (7,), (2,), (3,), (2, 5), (11,), (2, 3), (13,), (2, 7), (3, 5), (2,), (17,), (2, 3), (19,))
>>> tabulate_may_all_prime_factors4uint_lt_(2)
(None, ())
>>> tabulate_may_all_prime_factors4uint_lt_(1)
(None,)
>>> tabulate_may_all_prime_factors4uint_lt_(0)
()
>>> tabulate_may_all_prime_factors4uint_lt_(-1)
Traceback (most recent call last):
    ...
TypeError: -1


    is_prime__le_pow2_81_
    raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_
    raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_
    next_pseudoprime__ge_
    prev_may_pseudoprime__lt_
    next_may_prime__le_pow2_81__ge_
    prev_may_prime__le_pow2_81__lt_
>>> is_prime__le_pow2_81_(7)
True
>>> is_prime__le_pow2_81_(9)
False
>>> is_prime__le_pow2_81_(2047)
False
>>> is_prime__le_pow2_81_(2**81-1)
False
>>> is_prime__le_pow2_81_(is_prime__le_pow2_81_.upperbound)
Traceback (most recent call last):
    ...
seed.math.prime_gens.OverflowError__Miller_Rabin_primality_test__A014233: [3317044064679887385962123 == upperbound <= n == 3317044064679887385962123]
>>> pp = next_pseudoprime__ge_(2**82) -2**82
>>> pp
9
>>> mm =  2**82 -prev_may_pseudoprime__lt_(2**82)
>>> mm
57
>>> is_prime__le_pow2_81_(2**82+pp)
Traceback (most recent call last):
    ...
seed.math.prime_gens.OverflowError__Miller_Rabin_primality_test__A014233: [3317044064679887385962123 == upperbound <= n == 4835703278458516698824713]
>>> is_prime__le_pow2_81_(2**82-mm)
Traceback (most recent call last):
    ...
seed.math.prime_gens.OverflowError__Miller_Rabin_primality_test__A014233: [3317044064679887385962123 == upperbound <= n == 4835703278458516698824647]
>>> is_prime__le_pow2_81_(2**83-1)
False

>>> next_may_prime__le_pow2_81__ge_(2**82) -2**82
Traceback (most recent call last):
    ...
TypeError: unsupported operand type(s) for -: 'NoneType' and 'int'
>>> next_may_prime__le_pow2_81__ge_(2**82) is None
True
>>> next_may_prime__le_pow2_81__ge_(2**81) -2**81
17
>>> 2**82 -prev_may_prime__le_pow2_81__lt_(2**82)
Traceback (most recent call last):
    ...
seed.math.prime_gens.OverflowError__Miller_Rabin_primality_test__A014233: [3317044064679887385962123 == upperbound < end == 4835703278458516698824704]
>>> 2**81 -prev_may_prime__le_pow2_81__lt_(2**81)
51
>>> prev_may_prime__le_pow2_81__lt_(2) is None
True
>>> prev_may_prime__le_pow2_81__lt_(1) is None
True






>>> [*map(detect_strong_pseudoprime__not_waste_too_much_time_, range(-1, 20))]
[0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1]
>>> [*map(calc_len_prime_basis4II_prime_basis_gtN_, [is_prime__le_pow2_81_.upperbound, 2**607-1, 2**1279-1])]
[19, 87, 158]
>>> detect_strong_pseudoprime__not_waste_too_much_time_(is_prime__le_pow2_81_.upperbound)
-1
>>> detect_strong_pseudoprime__not_waste_too_much_time_(2**607-1)
-1
>>> detect_strong_pseudoprime__not_waste_too_much_time_(2**1279-1)
-1




    iter_pseudoprimes__ge_
    reversed_iter_pseudoprimes__lt_
    iter_primes__le_pow2_81__ge_
    reversed_iter_primes__le_pow2_81__lt_

>>> list_islice_(9, iter_pseudoprimes__ge_(-4))
[2, 3, 5, 7, 11, 13, 17, 19, 23]
>>> list_islice_(9, iter_pseudoprimes__ge_(0))
[2, 3, 5, 7, 11, 13, 17, 19, 23]
>>> list_islice_(9, iter_pseudoprimes__ge_(7))
[7, 11, 13, 17, 19, 23, 29, 31, 37]

>>> list_islice_(9, iter_primes__le_pow2_81__ge_(-4))
[2, 3, 5, 7, 11, 13, 17, 19, 23]
>>> list_islice_(9, iter_primes__le_pow2_81__ge_(0))
[2, 3, 5, 7, 11, 13, 17, 19, 23]
>>> list_islice_(9, iter_primes__le_pow2_81__ge_(7))
[7, 11, 13, 17, 19, 23, 29, 31, 37]

>>> list_islice_(9, reversed_iter_pseudoprimes__lt_(-4))
[]
>>> list_islice_(9, reversed_iter_pseudoprimes__lt_(0))
[]
>>> list_islice_(9, reversed_iter_pseudoprimes__lt_(7))
[5, 3, 2]

>>> list_islice_(9, reversed_iter_primes__le_pow2_81__lt_(-4))
[]
>>> list_islice_(9, reversed_iter_primes__le_pow2_81__lt_(0))
[]
>>> list_islice_(9, reversed_iter_primes__le_pow2_81__lt_(7))
[5, 3, 2]

#>>> for a, b in zip(iter_pseudoprimes__ge_(0), iter_primes__le_pow2_81__ge_(0)):
#...     if not a == b:break
#>>> (a, b)
[:next_pseudoprime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
>>> A014233[12] == (3317044064679887385961981)
True
>>> next_pseudoprime__ge_(3317044064679887385961981)
3317044064679887385962123
>>> next_pseudoprime__ge_(3317044064679887385961980)
3317044064679887385962123
>>> next_pseudoprime__ge_(3317044064679887385961981) -3317044064679887385961981
142

    iter_pairwise_diff_pseudoprimes__ge_
    iter_pairwise_diff_primes__le_pow2_81__ge_
>>> list_islice_(9, iter_pairwise_diff_pseudoprimes__ge_(0))
[1, 2, 2, 4, 2, 4, 2, 4, 6]
>>> list_islice_(9, iter_pairwise_diff_primes__le_pow2_81__ge_(0))
[1, 2, 2, 4, 2, 4, 2, 4, 6]



    iter_pseudoprimes__inside_
    iter_pseudoprimes__ge_lt_   iter_pseudoprimes__between_
>>> iter_pseudoprimes__between_ is iter_pseudoprimes__ge_lt_
True
>>> [*iter_pseudoprimes__inside_(range(-5, 11))]
[2, 3, 5, 7]
>>> [*iter_pseudoprimes__between_(-5, 11)]
[2, 3, 5, 7]
>>> [*iter_pseudoprimes__between_(-5, 11, reverse=True)]
[7, 5, 3, 2]
>>> [*iter_pseudoprimes__between_(-5, 11, case=[], reverse=True)] # see:is_prime__tribool_() since < 2**81
[7, 5, 3, 2]
>>> [*iter_pseudoprimes__between_(-5, 11, case=[], reverse=True, skip_A014233=True)] # see:is_prime__tribool_() since skip_A014233 # 由于打补丁，之前相当于skip_check=True
[7, 5, 3, 2]
>>> [*iter_pseudoprimes__between_(-5, 11, case=[], reverse=True, skip_A014233=True, skip_check=True)] # see:is_prime__tribool_() since skip_A014233
[9, 7, 5, 3, 2]

>>> [*map((2**100).__rsub__, islice(iter_pseudoprimes__between_(2**100, 2**100+8000, case=[], reverse=True, skip_A014233=True), 9))] # see:is_prime__tribool_() since skip_A014233 # 由于打补丁，之前相当于skip_check=True
[7995, 7987, 7983, 7981, 7977, 7965, 7947, 7945, 7911]
>>> [*map((2**100).__rsub__, islice(iter_pseudoprimes__between_(2**100, 2**100+8000, case=[], reverse=True, skip_A014233=True, skip_check=True), 9))] # see:is_prime__tribool_() since skip_A014233
[7999, 7997, 7995, 7993, 7991, 7989, 7987, 7985, 7983]
>>> [*map((2**100).__rsub__, islice(iter_pseudoprimes__between_(2**100, 2**100+8000, case=[], reverse=True), 9))]
[7737, 7717, 7713, 7701, 7623, 7557, 7531, 7491, 7477]
>>> [*map((2**100).__rsub__, islice(iter_pseudoprimes__between_(2**100, 2**100+8000, case=None, reverse=True), 9))]
[7737, 7717, 7713, 7701, 7623, 7557, 7531, 7491, 7477]


is_strong_pseudoprime__basis__with_trial_division_
    continuous_trial_division_
        iter_continuous_prime_bases_

xfilter4continuous_bases:=None
    filter4continuous_bases4II_prime_basis_gtN
>>> [(n, [*iter_continuous_prime_bases_(None, n)]) for n in range(-2, 20)]
[(-2, []), (-1, []), (0, []), (1, [2]), (2, [2, 3]), (3, [2, 3]), (4, [2, 3]), (5, [2, 3]), (6, [2, 3, 5]), (7, [2, 3, 5]), (8, [2, 3, 5]), (9, [2, 3, 5]), (10, [2, 3, 5]), (11, [2, 3, 5]), (12, [2, 3, 5]), (13, [2, 3, 5]), (14, [2, 3, 5]), (15, [2, 3, 5]), (16, [2, 3, 5]), (17, [2, 3, 5]), (18, [2, 3, 5]), (19, [2, 3, 5])]
>>> [*iter_continuous_prime_bases_(None, 99)]
[2, 3, 5, 7]
>>> [*iter_continuous_prime_bases_(None, 2*3*5*7)]
[2, 3, 5, 7, 11]
>>> [*iter_continuous_prime_bases_(None, 2*3*5*7+1)]
[2, 3, 5, 7, 11]
>>> [*iter_continuous_prime_bases_(None, 2*3*5*7-1)]
[2, 3, 5, 7]

>>> [(n, continuous_trial_division_(None, n)) for n in range(-2, 20)]
[(-2, 1), (-1, 1), (0, 1), (1, 1), (2, -1), (3, -1), (4, 2), (5, -1), (6, 2), (7, -1), (8, 2), (9, 3), (10, 2), (11, -1), (12, 2), (13, -1), (14, 2), (15, 3), (16, 2), (17, -1), (18, 2), (19, -1)]

>>> [(n, is_strong_pseudoprime__basis__with_trial_division_(None, [], n)) for n in range(-2, 20)]
[(-2, False), (-1, False), (0, False), (1, False), (2, True), (3, True), (4, False), (5, True), (6, False), (7, True), (8, False), (9, False), (10, False), (11, True), (12, False), (13, True), (14, False), (15, False), (16, False), (17, True), (18, False), (19, True)]
>>> [(n, r) for n in range(-2, 2**16) for r in [is_strong_pseudoprime__basis__with_trial_division_(None, [2], n)] if not r is is_prime__le_pow2_81_(n)]
[(2047, True), (3277, True), (4033, True), (4681, True), (8321, True), (42799, True), (49141, True), (65281, True)]

xfilter4continuous_bases:=False
    filter4continuous_bases4empty
>>> [(n, [*iter_continuous_prime_bases_(False, n)]) for n in range(-2, 20)]
[(-2, []), (-1, []), (0, []), (1, []), (2, []), (3, []), (4, []), (5, []), (6, []), (7, []), (8, []), (9, []), (10, []), (11, []), (12, []), (13, []), (14, []), (15, []), (16, []), (17, []), (18, []), (19, [])]
>>> [(n, continuous_trial_division_(False, n)) for n in range(-2, 20)]
[(-2, 1), (-1, 1), (0, 1), (1, 1), (2, -1), (3, -1), (4, 2), (5, -1), (6, 2), (7, -1), (8, 2), (9, 0), (10, 2), (11, 0), (12, 2), (13, 0), (14, 2), (15, 0), (16, 2), (17, 0), (18, 2), (19, 0)]
>>> [(n, r) for n in range(-2, 2**12) for r in [is_strong_pseudoprime__basis__with_trial_division_(False, [2], n)] if not r is is_prime__le_pow2_81_(n)]
[(2047, True), (3277, True), (4033, True)]


xfilter4continuous_bases:=0|1|2|...
    mk_filter4continuous_bases4fixed_size
>>> [(n, [*iter_continuous_prime_bases_(0, n)]) for n in range(-2, 3)]
[(-2, []), (-1, []), (0, []), (1, []), (2, [])]
>>> [(n, [*iter_continuous_prime_bases_(1, n)]) for n in range(-2, 3)]
[(-2, [2]), (-1, [2]), (0, [2]), (1, [2]), (2, [2])]
>>> [(n, [*iter_continuous_prime_bases_(2, n)]) for n in range(-2, 3)]
[(-2, [2, 3]), (-1, [2, 3]), (0, [2, 3]), (1, [2, 3]), (2, [2, 3])]


mk_tribool_delegate5PRP_test_
    [delegate := mk_tribool_delegate5PRP_test_(is_strong_pseudoprime__basis__with_trial_division_, xfilter4continuous_bases4div, bases4SPRP)]
>>> delegate = mk_tribool_delegate5PRP_test_(is_strong_pseudoprime__basis__with_trial_division_, xfilter4continuous_bases4div:=None, bases4SPRP:=[2,3,5,7])
>>> [(n, is_prime__tribool_(n, case=delegate)) for n in range(-2, 20)]
[(-2, False), (-1, False), (0, False), (1, False), (2, Ellipsis), (3, Ellipsis), (4, False), (5, Ellipsis), (6, False), (7, Ellipsis), (8, False), (9, False), (10, False), (11, Ellipsis), (12, False), (13, Ellipsis), (14, False), (15, False), (16, False), (17, Ellipsis), (18, False), (19, Ellipsis)]
>>> bool(...)
True

#]]]'''
_doc4tmp_test = r'''
>>> 

'''#'''
__all__ = r'''

prime_gen
prime_gen__Miller_Rabin_primality_test

is_strong_pseudoprime__basis_
    is_strong_pseudoprime__basis__with_trial_division_
    is_prime__le_pow2_81_
        prime_filter__using_primality_test_
            raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_
                prev_may_prime__le_pow2_81__lt_
                    reversed_iter_primes__le_pow2_81__lt_
            raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_
                next_may_prime__le_pow2_81__ge_
                    iter_primes__le_pow2_81__ge_
                        iter_pairwise_diff_primes__le_pow2_81__ge_
        is_prime__tribool_
            Case4is_prime__tribool_
            detect_strong_pseudoprime__not_waste_too_much_time_
            next_pseudoprime__ge_
            prev_may_pseudoprime__lt_
                reversed_iter_pseudoprimes__lt_
                iter_pseudoprimes__ge_
                    iter_pairwise_diff_pseudoprimes__ge_
            iter_pseudoprimes__inside_
            iter_pseudoprimes__ge_lt_   iter_pseudoprimes__between_



min_prime_factor_gen
    tabulate_may_min_prime_factor4uint_lt_
    tabulate_may_factorization4uint_lt_

all_prime_factors_gen
    tabulate_may_all_prime_factors4uint_lt_












raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_
    raw_list_all_strict_sorted_ints__ge2__with_min_prime_factor__sized_
    raw_iter_all_strict_sorted_primes_
        raw_iter_all_strict_sorted_primes__lt_
            raw_list_all_strict_sorted_primes__lt_


    GlobalControl4PrimeGenerator__Eratosthenes_sieve
        prime_gen__Eratosthenes_sieve
            prime_gen
    GlobalControl4PrimeGenerator__Miller_Rabin_primality_test
        prime_gen__Miller_Rabin_primality_test

Error
    Bool5TriboolFail__probably_prime
    OverflowError__Miller_Rabin_primality_test__A014233
    IsPrimeError


A014233         n2upperbound4Miller_Rabin_primality_test_using_first_n_plus1_primes_as_basis
    prime_basis4A014233
        prime_basis_set4A014233


is_strong_pseudoprime__basis_
    is_strong_pseudoprime_
        iter_until_found_min_prime_witness4odd_composite_
            find_min_prime_witness4odd_composite_

    is_prime__using_A014233_        is_prime__le_pow2_81_
        default4is_prime_and_may_upperbound
            prime_filter__using_primality_test_
                raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_
                    prev_may_prime__le_pow2_81__lt_
                raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_
                    next_may_prime__le_pow2_81__ge_

        is_prime__tribool_
            mk_tribool_delegate5PRP_test_
                is_strong_pseudoprime__basis__with_trial_division_
            Case4is_prime__tribool_
            detect_strong_pseudoprime__not_waste_too_much_time_
            iter_prime_basis4II_prime_basis_gtN_
                calc_len_prime_basis4II_prime_basis_gtN_
            next_pseudoprime__ge_
            prev_may_pseudoprime__lt_



GlobalControl4MinPrimeFactorGenerator__Eratosthenes_sieve
    min_prime_factor_gen__Eratosthenes_sieve
        min_prime_factor_gen
        tabulate_may_min_prime_factor4uint_lt_
        tabulate_may_factorization4uint_lt_

GlobalControl4AllPrimeFactorsGenerator__Eratosthenes_sieve
    all_prime_factors_gen__Eratosthenes_sieve
        all_prime_factors_gen
        tabulate_may_all_prime_factors4uint_lt_



mk_tribool_delegate5PRP_test_
is_strong_pseudoprime__basis__with_trial_division_
    continuous_trial_division_
        iter_continuous_prime_bases_
    callable5xfilter4continuous_bases
    mk_initial_state4filter4continuous_bases_
        filter4continuous_bases4II_prime_basis_gtN
        filter4continuous_bases4empty
        mk_filter4continuous_bases4fixed_size



pairwise_diff_
'''.split()#'''
__all__

___begin_mark_of_excluded_global_names__0___ = ...

from seed.for_libs.for_time import (
Timer__print_err
    ,timer__print_err__thread_wide
    ,timer__print_err__process_wide
    ,timer__print_err__system_wide__highest_resolution
    ,timer__print_err__system_wide__monotonic
)

timer = timer__print_err__thread_wide
_to_show_ = __name__ == "__main__"

with timer(prefix='py:std...', _to_show_=_to_show_):
    from enum import Enum, auto
    from weakref import ref as _ref
    import itertools
    from itertools import count as _count, repeat as _repeat
    from itertools import islice, chain, pairwise, filterfalse

with timer(prefix='seed:basic...', _to_show_=_to_show_):
    from seed.iters.apply_may_args4islice_ import apply_may_args4islice_
    from seed.iters.apply_may_args4islice_ import list_islice_, show_islice_, stable_show_islice_, stable_list_islice_
    from seed.tiny import ifNonef, snd, print_err, ifNone #, echo
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.tiny_.dict_op__add import set_add# dict_add, dict_update, set_update

with timer(prefix='seed:math... pass', _to_show_=False):
    from seed.math.gcd import gcd
    pass
    #from seed.math.is_prime__le_pow2_64 import is_prime__le_pow2_64
    #from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_

    #from seed.math.II import II, II_mod

    #from seed.helper.repr_input import repr_helper
    #from seed.helper.stable_repr import stable_repr
with timer(prefix='seed.math.max_power_of_base_as_factor_of_', _to_show_=_to_show_):
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_2_powers
with timer(prefix='seed.math.semi_factor_pint_via_trial_division', _to_show_=_to_show_):
    from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
with timer(prefix='LazySeq', _to_show_=_to_show_):
    from seed.types.LazySeq import LazySeq

r'''[[[
py -m seed.math.prime_gens
py:std...:duration: 0.0002503850000000196 *(unit: 0:00:01)
seed:basic...:duration: 0.002044998999999992 *(unit: 0:00:01)
seed.math.max_power_of_base_as_factor_of_:duration: 0.001993615000000004 *(unit: 0:00:01)
seed.math.semi_factor_pint_via_trial_division:duration: 0.18622884699999998 *(unit: 0:00:01)
LazySeq:duration: 0.008693461999999985 *(unit: 0:00:01)


seed.math.semi_factor_pint_via_trial_division
e ../../python3_src/seed/math/semi_factor_pint_via_trial_division.py

py -m seed.math.semi_factor_pint_via_trial_division
py:std...:duration: 0.00015815400000002144 *(unit: 0:00:01)
seed:basic...:duration: 9.846099999999414e-05 *(unit: 0:00:01)
seed:func_tools...:duration: 0.023295232 *(unit: 0:00:01)
seed:math...:duration: 0.015590459999999973 *(unit: 0:00:01)
seed.math.floor_ceil:duration: 0.10961200099999996 *(unit: 0:00:01)

seed.math.floor_ceil
e ../../python3_src/seed/math/floor_ceil.py

move 'import unittest, doctest' into seed.math.floor_ceil:load_tests() body -->:
move seed.math.semi_factor_pint_via_trial_division:"_test1__calc_num_products_of_coprime_factors__ge1_le()" under 'if __name__ == "__main__":' -->:
    py:std...:duration: 0.0001649229999999835 *(unit: 0:00:01)
    seed:basic...:duration: 0.001496232000000014 *(unit: 0:00:01)
    seed.math.max_power_of_base_as_factor_of_:duration: 0.0014222299999999966 *(unit: 0:00:01)
    seed.math.semi_factor_pint_via_trial_division:duration: 0.032522994 *(unit: 0:00:01)
    LazySeq:duration: 0.006289921000000004 *(unit: 0:00:01)

0.03?? <-- seed.math.semi_factor_pint_via_trial_division
py -m seed.math.semi_factor_pint_via_trial_division
seed:func_tools...:duration: 0.02524277199999997 *(unit: 0:00:01)


#]]]'''#'''



___end_mark_of_excluded_global_names__0___ = ...







class Error(Exception):
    pass
    r'''[[[
    def __repr__(sf, /):
        return repr_helper(sf, *sf.args)
    #]]]'''#'''

#def _iter_all_strict_sorted_primes():
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
    'using Eratosthenes_sieve: -> [prime]{[[last prime < end][next prime >= end]]} #see:raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_'
    return [*raw_iter_all_strict_sorted_primes__lt_(end, to_cache_only_busy_primes_plus_next=to_cache_only_busy_primes_plus_next, may_primes=may_primes)]



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
def raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_(*, to_cache_only_busy_primes_plus_next, may_primes, ihead2may_itail=None, offsetted_sieve=None, lmay_offset=None, to_export_all_prime_factors=False):
    'using Eratosthenes_sieve: -> Iter (n, min_prime_factor<n>) if not to_export_all_prime_factors else (n, all_strict_sorted_prime_factors<n>) # [n >= 2]'
    #no max_prime_factor, since use sqare limit, donot detect p for [i*p | [i :<- [2..<p]]] inside [p..=p**2]
    #       ...can have max_prime_factor, since miss at most one prime that is a prime <- [next_busy_prime..<next_busy_prime**2]
    #
    #the input `may_primes` used as view to outside
    #
    primes = ifNonef(may_primes, list)

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
        # sqare4next_busy_prime = next_busy_prime**2
        sqare4next_busy_prime = 4
        # prev____sqare4next_busy_prime = 1

        # for n in _count(first_prime):
        for n in _count(2):
            # [prev____sqare4next_busy_prime < n <= sqare4next_busy_prime]
            may_ihead = get_(n)
            drop_(n)
            #advance_ should be after drop_!!! since extend offsetted_sieve
            if may_ihead is None and n == sqare4next_busy_prime:
                #not prime # next_busy_prime**2
                ihead4next_busy_prime = len(ihead2may_itail)
                may_ihead = ihead4next_busy_prime
                #prev____sqare4next_busy_prime = sqare4next_busy_prime
                (next_busy_prime, sqare4next_busy_prime) = add_new_busy_prime()
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
                yield mk4composite(n, iheads, next_busy_prime, sqare4next_busy_prime)
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
    #    '-> (len_busy_primes, sqare4next_busy_prime)'
    def add_new_busy_prime():
        '-> (next_busy_prime, sqare4next_busy_prime)'
        # in first round: [old-next_busy_prime == 2]
        # in first round: [old-ihead2may_itail<2> == 0]
        # in first round: [old-sqare4next_busy_prime<2> == 4]

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

        sqare4next_busy_prime = next_busy_prime**2
        # in first round: [new-sqare4next_busy_prime<3> == 9]
        return (next_busy_prime, sqare4next_busy_prime)
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
        def mk4composite(n, iheads, next_busy_prime, sqare4next_busy_prime, /):
            #OK@[n==old-sqare4next_busy_prime]
            #   even call mk4composite() after next_busy_prime,sqare4next_busy_prime updated
            #       since fs=[old-next_busy_prime] is complete, [_1_or_p==1]
            fs = [primes[ihead] for ihead in iheads]
            (p2e, _1_or_p) = semi_factor_pint_via_trial_division(fs, n)
            if not _1_or_p == 1:
                p = _1_or_p
                assert next_busy_prime <= p < sqare4next_busy_prime
                fs.append(p)
            fs = (*fs,)
            return (n, fs)
    else:
        def mk4prime(n, /):
            p = n
            m = p
            return (n, m)
        def mk4composite(n, iheads, next_busy_prime, sqare4next_busy_prime, /):
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




class _IBaseGlobalControl4LazySeq:
    #_may_singleton = None
    #_may_wref_singleton = None

    #@abstractmethod
    def _mk_new_lazy_seq_(sf, /):
        raise 000
    def __new__(cls, /):
        #if not cls is __class__: raise TypeError
        while 1:
            try:
                return cls._sf
            except AttributeError:
                pass
            sf = cls._sf = object.__new__(cls)
            sf._may_singleton = None
            sf._may_wref_singleton = None
    def remove_global_singleton_(sf, /):
        'del strong ref to the global lazy_seq if exist'
        sf._may_singleton = None
        #hold sf._may_wref_singleton
    def get_or_mk_global_singleton_(sf, /, *, not_set_global=False):
        '-> LazySeq<x> # get if weak ref exist else mk new lazy_seq (store as strong ref unless not_set_global=True)'
        while 1:
            m = sf._may_singleton
            if not m is None:
                lazy_seq = m
                return lazy_seq
            while 1:
                w = sf._may_wref_singleton
                if not (w is None or w() is None):
                    lazy_seq = w()
                    break
                #weak_ref = w
                #if no_make: return None
                #rebuild:
                lazy_seq = sf._mk_new_lazy_seq_()
                sf._may_wref_singleton = _ref(lazy_seq)
            #end-inner-while 1:
            assert lazy_seq is not None
            if not_set_global:
                return lazy_seq
            sf._may_singleton = lazy_seq
    def get_or_mk_lazy_seq_(sf, /):
        '-> LazySeq<x> # get if weak ref exist else mk new lazy_seq (not store as strong ref)'
        '-> LazySeq<x>'
        lazy_seq = sf.get_or_mk_global_singleton_(not_set_global=True)
        return lazy_seq
    def __call__(sf, /):
        '-> LazySeq<x> # === get_or_mk_lazy_seq_'
        return sf.get_or_mk_lazy_seq_()
    def iter__sized_(sf, sz, /):
        '-> Iter<,>{len=sz}'
        return islice(iter(sf), sz)
    def __bool__(sf, /):
        return True
    #__bool__ = ...
    __len__ = ...
    __contains__ = ...

    def __iter__(sf, /):
        '-> Iter<x>{len=+oo}'
        return iter(sf[...]) #del lazy_seq, hold LazyList tail only
        return iter(sf()) # hold lazy_seq
    def __getitem__(sf, i_or_sl_or_3dot, /):
        'i -> x; i:j -> [x]; ... -> LazyList<x>'
        if i_or_sl_or_3dot is ...:
            return sf().the_lazylist
        i_or_sl = i_or_sl_or_3dot
        return sf()[i_or_sl]
        if type(i_or_sl) is slice:
            sl = i_or_sl
            return sf()[sl]
        if type(i_or_sl) is int:
            i = i_or_sl
            return sf()[i]
        raise TypeError(type(i_or_sl))
class Bool5TriboolFail__probably_prime(Error):pass
class _IBaseGlobalControl4PrimeGenerator(_IBaseGlobalControl4LazySeq):
    #_may_singleton = None
    #_may_wref_singleton = None

    #@abstractmethod
    #def _mk_new_lazy_seq_(sf, /):
    ...

    def get_or_mk_lazy_prime_seq_(sf, /):
        '-> LazySeq<prime> # get if weak ref exist else mk new lazy_prime_seq (not store as strong ref)'
        '-> LazySeq<prime>'
        lazy_seq = sf.get_or_mk_lazy_seq_()
        return lazy_seq
    def iter__lt_(sf, end, /):
        '-> Iter<prime{<end}>'
        return _iter__lt_(end, iter(sf))
    def iter__ge_(sf, begin, /):
        '-> Iter<prime{>=begin}>'
        check_type_is(int, begin)
        if begin <= 2:
            return iter(sf)
        lazylist = sf[...]
        it = lazylist.iter__hardwork(to_iter_pairs=True)
        for prime, tail in it:
            if not prime < begin:
                break
            lazylist = tail # del lazylist to free memory
        return iter(lazylist)
    def __bool__(sf, /):
        return True
    __len__ = ...
    def __contains__(sf, x, /):
        'using is_prime__using_A014233_/is_prime__tribool_'
        check_type_is(int, x)
        #r = is_prime__tribool_(x, case=Case4is_prime__tribool_.II_prime_basis_gtN)
        r = is_prime__tribool_(x, case=None)
        if r is ...:
            raise Bool5TriboolFail__probably_prime(x)
        return r

class GlobalControl4PrimeGenerator__Eratosthenes_sieve(_IBaseGlobalControl4PrimeGenerator):
    'using Eratosthenes_sieve'
    #@override
    def _mk_new_lazy_seq_(sf, /):
        it = raw_iter_all_strict_sorted_primes_(to_cache_only_busy_primes_plus_next=True, may_primes=None)
        lazy_seq = LazySeq(it)
        return lazy_seq

class GlobalControl4PrimeGenerator__Miller_Rabin_primality_test(_IBaseGlobalControl4PrimeGenerator):
    'using Miller_Rabin_primality_test; not inf long, halt between [2**81..<2**82]'
    #@override
    def _mk_new_lazy_seq_(sf, /):
        it = prime_filter__using_primality_test_(_count(2))
        lazy_seq = LazySeq(it)
        return lazy_seq



prime_gen__Eratosthenes_sieve = GlobalControl4PrimeGenerator__Eratosthenes_sieve()
prime_gen__Miller_Rabin_primality_test = GlobalControl4PrimeGenerator__Miller_Rabin_primality_test()
prime_gen = prime_gen__Eratosthenes_sieve



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

prime_basis4A014233 = prime_gen[:len(A014233)]
assert prime_basis4A014233[11] == 37
assert len(prime_basis4A014233) == len(A014233)
check_type_is(tuple, A014233)
check_type_is(tuple, prime_basis4A014233)
prime_basis_set4A014233 = frozenset(prime_basis4A014233)
if 0:
    #move to below
    assert not any(map(is_prime__using_A014233_, A014233))





class OverflowError__Miller_Rabin_primality_test__A014233(Error):pass

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
        [[n >= is_prime__using_A014233_.upperbound > A014233[-1] > 2**81][is_strong_pseudoprime__basis_(prime_basis4A014233, n) is True]]

        ######################
        [is_strong_pseudoprime__basis_(prime_basis4A014233, n) is True] ==>> [@[p :<- prime_basis4A014233] -> [n%p =!= 0]]
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
    [is_strong_pseudoprime_(b;n) =[def]= [[n >= 3][n%2==1][(e,t) :=> [[e,t :: pint][t%2==1][t*2**e == n-1]]][[b**t %n == +1]or[?[s :<- [0..<e]] -> [(b**t)**(2**s) %n == -1]]]]]

    [[is_strong_pseudoprime_(b;n)] -> [gcd(n,b) == 1]]

primality_test_of_Miller_Rabin
  probabilistic primality test
    return probably_prime | composite
  --> deterministic algorithm

    #]]]'''#'''
    #see:is_strong_pseudoprime__basis_
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
                return _kw__is_strong_pseudoprime__basis_(basis, n)
    else:
        for i1, max1 in enumerate(A014233, 1):
            if n < max1:
                basis = prime_basis4A014233[:i1]
                return _kw__is_strong_pseudoprime__basis_(basis, n, to_find_sqrt_neg1=to_find_sqrt_neg1)
        if n == max1:
            if to_find_sqrt_neg1:
                bool_or_with_sqrts = _kw__is_strong_pseudoprime__basis_(prime_basis4A014233, n, to_find_sqrt_neg1=to_find_sqrt_neg1)
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
    #if not _kw__is_strong_pseudoprime__basis_(prime_basis4A014233, n):
        #return False
    bool_or_with_sqrts = _kw__is_strong_pseudoprime__basis_(prime_basis4A014233, n, to_find_sqrt_neg1=to_find_sqrt_neg1)
    if not _bool__5bool_or_with_sqrts_(bool_or_with_sqrts):
        return bool_or_with_sqrts
    # [[n >= is_prime__using_A014233_.upperbound > A014233[-1] > 2**81][is_strong_pseudoprime__basis_(prime_basis4A014233, n) is True]]
        #see:_find_upperbound4is_prime__using_A014233_()

    upperbound = is_prime__using_A014233_.upperbound #max1+2
    raise OverflowError__Miller_Rabin_primality_test__A014233(f'[{upperbound} == upperbound <= n == {n}]')
if 1:
    #see below:_find_upperbound4is_prime__using_A014233_
    is_prime__using_A014233_.upperbound = A014233[-1]+2
        #only for first raise in _find_upperbound4is_prime__using_A014233_

def is_strong_pseudoprime_(base, n, /, *, to_find_sqrt_neg1=False):
    'base/int{>=2,%n=!=0} -> n{>=3,odd} -> [n is base-SPRP]'
    return _kw__is_strong_pseudoprime__basis_([base], n, to_find_sqrt_neg1=to_find_sqrt_neg1)
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
    for k, p in enumerate(iter(prime_gen)):
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
def is_strong_pseudoprime__basis__with_trial_division_(xfilter4continuous_bases4div, bases4SPRP, n, /):
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
    return is_strong_pseudoprime__basis_(bases, n)

def is_strong_pseudoprime__basis_(basis, n, /, *, to_find_sqrt_neg1=False):
    'basis/[base/int{>=2,%n=!=0}] -> n{>=3,odd} -> [n is basis-SPRP] /(bool if not to_find_sqrt_neg1 or not found sqrt_neg1 else (bool, [sqrt_neg1]/[int%n <= n//2]{len=1/(False|True),2/False}))'
    #see:is_prime__using_A014233_
    return _kw__is_strong_pseudoprime__basis_(basis, n, to_find_sqrt_neg1=to_find_sqrt_neg1)
def _kw__is_strong_pseudoprime__basis_(basis, n, /, *, to_find_sqrt_neg1):
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

    #return all(_is_strong_pseudoprime_(base, n, n_neg1, e_neg1, odd) for base in basis)
    #if not to_find_sqrt_neg1:
    #    return all(_is_strong_pseudoprime_(base, n, n_neg1, e_neg1, odd, False) for base in basis)
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

        r = all(put(_is_strong_pseudoprime_(base, n, n_neg1, e_neg1, odd, True)) for base in basis)
        #bug:return sqrts or r
        #   may be found one sqrt then found not pseudoprime
        #   hence len(sqrts)==1 donot repr True
        if to_find_sqrt_neg1 and sqrts:
            if len(sqrts)==2:
                assert r is False
            return (r, sqrts)
        return r
def _is_strong_pseudoprime_(base, n, n_neg1, e_neg1, odd, to_find_sqrt_neg1, /):
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

if __name__ == "__main__":
    with timer(prefix='apply is_prime__using_A014233_ on A014233', _to_show_=_to_show_):
        assert not any(map(is_prime__using_A014233_, A014233))
        #assert not any(len(_sqrts__5bool_or_with_sqrts_(bool_or_with_sqrts)) == 2 for bool_or_with_sqrts in (ls := [is_prime__using_A014233_(n, to_find_sqrt_neg1=True) for n in A014233])), ls
        #   SyntaxError: assignment expression cannot be used in a comprehension iterable expression
        assert (__ := [is_prime__using_A014233_(n, to_find_sqrt_neg1=True) for n in A014233]) == [False, (False, [483061]), False, False, False, False, (False, [27393523843088, 36156112808384]), (False, [27393523843088, 36156112808384]), False, False, False, (False, [107889940756980366727205, 103782637039805229854323]), (False, [806966215798523717614900, 1560865212556530034242163])], __

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




class IsPrimeError(Error):pass
def iter_until_found_min_prime_witness4odd_composite_(odd_composite, /):
    'odd_composite/int{odd,>=9} -> Iter (is_pseudoprime, prime_idx, prime_base){if not is_pseudoprime then prime_base is min_prime_witness) | ^IsPrimeError # [[is_pseudoprime == is_strong_pseudoprime_(prime_base, odd_composite)][prime_gen[prime_idx] == prime_base][not is_strong_pseudoprime_(min_prime_witness, odd_composite)]]'
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
    for i, p in enumerate(prime_gen):
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
        is_pseudoprime = _is_strong_pseudoprime_(base, n, n_neg1, e_neg1, odd, False)
        yield (is_pseudoprime, i, p)
        if not is_pseudoprime:
            return
        if r == 0:raise logic-err
def find_min_prime_witness4odd_composite_(odd_composite, /, *, with_prime_idx=False):
    'odd_composite/int{odd,>=9} -> min_prime_witness/int{prime} if not with_prime_idx else (prime_idx, min_prime_witness) | ^IsPrimeError # [[not is_strong_pseudoprime_(min_prime_witness, odd_composite)][prime_gen[prime_idx] == min_prime_witness]]'
    #NOTE: may have [min_witness_base < min_prime_witness]
    for (is_pseudoprime, i, p) in iter_until_found_min_prime_witness4odd_composite_(odd_composite):
        pass
    assert not is_pseudoprime
    min_prime_witness = base = p
    if with_prime_idx:
        prime_idx = i
        return (prime_idx, min_prime_witness)
    return min_prime_witness

def __():
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
        # @20250130: ++[case :: (___ | [basis/uint] | None)] for kw:case@next_pseudoprime__ge_/prev_may_pseudoprime__lt_/...
    bit_length = auto()
    ERH = auto()
    II_prime_basis_gtN = auto()
        # def____II_prime_basis_gtN:here
        # impl____II_prime_basis_gtN:goto
        # II_prime_basis_gtN___vs___A014233:goto
def detect_strong_pseudoprime__not_waste_too_much_time_(n, /):
    'n/int -> (0|1|-1) # [0=>not prime][1=>prime][-1=>strong_pseudoprime] #[case:=Case4is_prime__tribool_.II_prime_basis_gtN]'
    #r = is_prime__tribool_(n, case=Case4is_prime__tribool_.II_prime_basis_gtN)
    r = is_prime__tribool_(n, case=None)
        #=> case=Case4is_prime__tribool_.II_prime_basis_gtN
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
        [delegate := mk_tribool_delegate5PRP_test_(is_strong_pseudoprime__basis__with_trial_division_, xfilter4continuous_bases4div, bases4SPRP)]
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

        [[n >= is_prime__using_A014233_.upperbound > A014233[-1] > 2**81][is_strong_pseudoprime__basis_(prime_basis4A014233, n) is True][is_strong_pseudoprime__basis_(basis, n) is True]]
]]


[[
pseudoprime
strong pseudoprime

probable-prime (PRP)
strong probable-prime (SPRP)
  b-SPRP
Extended Riemann Hypothesis (ERH)

[n,b :: int][n =!= 0][b%n =!= 0]:
    [is_strong_pseudoprime_(b;n) =[def]= [[n >= 3][n%2==1][(e,t) :=> [[e,t :: pint][t%2==1][t*2**e == n-1]]][[b**t %n == +1]or[?[s :<- [0..<e]] -> [(b**t)**(2**s) %n == -1]]]]]

    [[is_strong_pseudoprime_(b;n)] -> [gcd(n,b) == 1]]
[[Extended Riemann Hypothesis (ERH)] -> @[n :: int] -> [n > 0] -> [n%2==1] -> [[is_prime_(n)] <-> [@[b :<- [2..<min(n, 2*(log n)**2)]] -> [is_strong_pseudoprime_(b;n)]]]]
  # what is the base of log?
==>>:
!! [2 < e ~= 2.718281828459045 < 10]
[[Extended Riemann Hypothesis (ERH)] -> @[n :: int] -> [n > 0] -> [n%2==1] -> [[is_prime_(n)] <-> [@[b :<- [2..<min(n, 2*(ceil_log2 n)**2)]] -> [is_strong_pseudoprime_(b;n)]]]]
==>>:
!! [[is_strong_pseudoprime_(b;n)] -> [gcd(n,b) == 1]]
[[Extended Riemann Hypothesis (ERH)] -> @[n :: int] -> [n > 0] -> [n%2==1] -> [[is_prime_(n)] <-> [@[b :<- [2..<min(1+floor_sqrt(n), 2*(ceil_log2 n)**2)]] -> [is_strong_pseudoprime_(b;n)]]]]
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
#   !! there are many funcs depends on is_prime__tribool_():next_pseudoprime__ge_,prev_may_pseudoprime__lt_,iter_pseudoprimes__between_,...
#   to override it by [case:=delegate]
######################
    #]]]'''#'''
    #def is_prime__tribool_(n, /, *, case=Case4is_prime__tribool_.II_prime_basis_gtN, skip_check=False):
    #def is_prime__tribool_(n, /, *, case:Case4is_prime__tribool_, skip_check=False):
    #def is_prime__tribool_(n, /, *, case:[Case4is_prime__tribool_,tuple], skip_check=False, skip_A014233=False, params4is_strong_pseudoprime__basis__with_trial_division_=None):
    #def is_prime__tribool_(n, /, *, case:[Case4is_prime__tribool_,tuple], skip_check=False, skip_A014233=False, delegate=None):
    #
    # xxx is_prime__using_A014233_.upperbound
    #   since trial_division...
    if 0b0001:params = dict(locals())
    ######################
    ##delegate used in:view script/搜索冫伪素数牜临近幂方.py
    #   !! there are many funcs depends on is_prime__tribool_():next_pseudoprime__ge_,prev_may_pseudoprime__lt_,iter_pseudoprimes__between_,...
    #   to override it by [case:=delegate]
    ######################
    #if not delegate is None:
    if callable(case):
        delegate = case
        # [delegate => ignore all other kwds]
        return delegate(n)
    ######################
    ######################
    #.if params4is_strong_pseudoprime__basis__with_trial_division_:
    #.    # use is_strong_pseudoprime__basis__with_trial_division_ instead
    #.    #   since just required whether_SPRP
    #.    (xfilter4continuous_bases4div, bases4SPRP) = params4is_strong_pseudoprime__basis__with_trial_division_
    #.    whether_SPRP = is_strong_pseudoprime__basis__with_trial_division_(xfilter4continuous_bases4div, bases4SPRP, n)
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
        # [[n >= is_prime__using_A014233_.upperbound > A014233[-1] > 2**81][is_strong_pseudoprime__basis_(prime_basis4A014233, n) is True]]
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
            prime_basis = prime_gen[L:sz]
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
        ps = prime_gen.iter__lt_(end)
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
        if not _kw__is_strong_pseudoprime__basis_(basis, n, to_find_sqrt_neg1=False):
            return False
        # [is_strong_pseudoprime__basis_(basis, n) is True]
    # [is_strong_pseudoprime__basis_(chain(*basis_ls), n) is True]
    # !! [is_strong_pseudoprime__basis_(prime_basis4A014233, n) is True]
    # [is_strong_pseudoprime__basis_(chain(prime_basis4A014233, *basis_ls), n) is True]
        # hence the above "exclude" prime_basis4A014233 is ok

    # postcondition:
    # [[n >= is_prime__using_A014233_.upperbound > A014233[-1] > 2**81][is_strong_pseudoprime__basis_(chain(prime_basis4A014233, *basis_ls), n) is True]]
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
    for p in iter(prime_gen):
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


if 0:
    #bug: prime_gen.iter__lt_(end) --> range(2, end)
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
    for p in prime_gen.iter__lt_(max_p+1):
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
        # [:next_pseudoprime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
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


def prev_may_pseudoprime__lt_(end, /, **kwds):
    # @20250130: ++kw:case@prev_may_pseudoprime__lt_
    'using Miller_Rabin_primality_test: end -> (may pseudoprime){[[pseudoprime < end][next pseudoprime >= end]]} #see:prev_may_prime__le_pow2_81__lt_'
    # [:next_pseudoprime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    kwds.setdefault('case', None)
    for n in reversed(range(3, end|1, 2)):
        r = is_prime__tribool_(n, **kwds)
        if not r is False:
            pseudoprime = n
            return pseudoprime
            break
    else:
        assert end <= 3, (end, kwds)
        if 2 < end:
            return 2
    return None

def next_pseudoprime__ge_(begin, /, **kwds):
    # @20250130: ++kw:case@next_pseudoprime__ge_
    'using Miller_Rabin_primality_test: begin -> (pseudoprime){[[prev pseudoprime < begin][pseudoprime >= begin]]} #see:next_may_prime__le_pow2_81__ge_' \
    r'''

!! II_prime_basis_gtN___vs___A014233:goto
=> [II_prime_basis_gtN `better_than` A014233[:13]]
=> [II_prime_basis_gtN `better_than` __le_pow2_81]
=> [next_pseudoprime__ge_ `better_than` next_may_prime__le_pow2_81__ge_]
=> [[n <= 2**81] -> [next_pseudoprime__ge_(n) == next_may_prime__le_pow2_81__ge_(n)]]
    [:next_pseudoprime__ge___vs__next_may_prime__le_pow2_81__ge_]:here
'''#'''
    kwds.setdefault('case', None)
    begin = max(2, begin)
    if begin == 2:
        return 2
    for n in _count(begin|1, 2):
        r = is_prime__tribool_(n, **kwds)
        if not r is False:
            break
    pseudoprime = n
    return pseudoprime
def next_may_prime__le_pow2_81__ge_(begin, /, *, is_prime_and_may_upperbound=default4is_prime_and_may_upperbound):
    'using Miller_Rabin_primality_test: begin -> (may prime){[[prev prime < begin][prime >= begin]]} #see:next_pseudoprime__ge_'
    # [:next_pseudoprime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    it = raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_(begin, is_prime_and_may_upperbound=is_prime_and_may_upperbound)
    return _next__may_head_(it)
def _next__may_head_(it, /):
    for head in it:
        return head
    return None
def prev_may_prime__le_pow2_81__lt_(end, /, *, is_prime_and_may_upperbound=default4is_prime_and_may_upperbound):
    'using Miller_Rabin_primality_test: end -> (may prime){[[prime < end][next prime >= end]]} #see:prev_may_pseudoprime__lt_'
    # [:next_pseudoprime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
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
def iter_pseudoprimes__ge_lt_(begin, may_end, /, *, reverse=False, **kwds):
    # @20250130: ++kw:case@next_pseudoprime__ge___vs__next_may_prime__le_pow2_81__ge_&prev_may_pseudoprime__lt_
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
    odd_primes = _iter_pseudoprimes__inside_(odds, **kwds)
    primess = (even_primes, odd_primes)
    if reverse:
        primess = reversed(primess)
    primess
    return chain(*primess)
def _iter_pseudoprimes__inside_(uints, /, **kwds):
    kwds.setdefault('case', None)
    for n in uints:
        r = is_prime__tribool_(n, **kwds)
        if not r is False:
            pseudoprime = n
            yield pseudoprime
    return
def iter_pseudoprimes__inside_(ints, /, **kwds):
    it = filter(2 .__le__, ints)
    return _iter_pseudoprimes__inside_(it, **kwds)
iter_pseudoprimes__inside_
iter_pseudoprimes__ge_lt_
iter_pseudoprimes__between_ = iter_pseudoprimes__ge_lt_
def iter_pseudoprimes__ge_(begin, /, **kwds):
    # @20250130: ++kw:case@next_pseudoprime__ge___vs__next_may_prime__le_pow2_81__ge_&prev_may_pseudoprime__lt_
    # [:next_pseudoprime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    return _iter_xs_ge_(next_pseudoprime__ge_, begin, **kwds)
def reversed_iter_pseudoprimes__lt_(end, /, **kwds):
    # @20250130: ++kw:case@next_pseudoprime__ge___vs__next_may_prime__le_pow2_81__ge_&prev_may_pseudoprime__lt_
    # [:next_pseudoprime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    return _reversed_iter_xs_lt_(prev_may_pseudoprime__lt_, end, **kwds)
def iter_primes__le_pow2_81__ge_(begin, /):
    # [:next_pseudoprime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    return _iter_xs_ge_(next_may_prime__le_pow2_81__ge_, begin)
iter_primes__le_pow2_81__ge_ = raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_
def reversed_iter_primes__le_pow2_81__lt_(end, /):
    # [:next_pseudoprime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    return raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_(end, reverse=True)
    return _reversed_iter_xs_lt_(prev_may_prime__le_pow2_81__lt_, end)
#bug:reversed_iter_primes__le_pow2_81__lt_ = raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_

def pairwise_diff_(xs, /):
    xs = iter(xs)
    for a, b in pairwise(xs):
        yield b-a
def iter_pairwise_diff_pseudoprimes__ge_(begin, /):
    # [:next_pseudoprime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
    return pairwise_diff_(iter_pseudoprimes__ge_(begin))
def iter_pairwise_diff_primes__le_pow2_81__ge_(begin, /):
    # [:next_pseudoprime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
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










#class StableReprDict(dict):
#    def __repr__(sf, /):
#        return stable_repr(dict(sf))




class GlobalControl4MinPrimeFactorGenerator__Eratosthenes_sieve(_IBaseGlobalControl4LazySeq):
    'using Eratosthenes_sieve'
    #see:GlobalControl4PrimeGenerator__Eratosthenes_sieve
    #@override
    def _mk_new_lazy_seq_(sf, /):
        it = raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_(to_cache_only_busy_primes_plus_next=True, may_primes=None)
        it = map(snd, it)
        it = chain([None, None], it)
        lazy_seq = LazySeq(it)
        return lazy_seq
    def __bool__(sf, /):
        return True
    def get_or_mk_lazy_min_prime_factor_seq_(sf, /):
        '-> LazySeq<may min_prime_factor> # get if weak ref exist else mk new lazy_seq (not store as strong ref)'
        lazy_seq = sf.get_or_mk_lazy_seq_()
        return lazy_seq
min_prime_factor_gen__Eratosthenes_sieve = GlobalControl4MinPrimeFactorGenerator__Eratosthenes_sieve()
min_prime_factor_gen = min_prime_factor_gen__Eratosthenes_sieve


class GlobalControl4AllPrimeFactorsGenerator__Eratosthenes_sieve(_IBaseGlobalControl4LazySeq):
    'using Eratosthenes_sieve'
    #see:GlobalControl4MinPrimeFactorGenerator__Eratosthenes_sieve
    #@override
    def _mk_new_lazy_seq_(sf, /):
        it = raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_(to_cache_only_busy_primes_plus_next=True, may_primes=None, to_export_all_prime_factors=True)
        it = map(snd, it)
        it = chain([None, ()], it)
        lazy_seq = LazySeq(it)
        return lazy_seq
    def __bool__(sf, /):
        return True
    def get_or_mk_lazy_all_prime_factors_seq_(sf, /):
        '-> LazySeq<may all_prime_factors> # get if weak ref exist else mk new lazy_seq (not store as strong ref)'
        lazy_seq = sf.get_or_mk_lazy_seq_()
        return lazy_seq
all_prime_factors_gen__Eratosthenes_sieve = GlobalControl4AllPrimeFactorsGenerator__Eratosthenes_sieve()
all_prime_factors_gen = all_prime_factors_gen__Eratosthenes_sieve

def tabulate_may_min_prime_factor4uint_lt_(sz, /):
    '-> uint2may_min_prime_factor/[may prime]/[None,None,prime...]'
    return min_prime_factor_gen[:sz]
def tabulate_may_factorization4uint_lt_(sz, uint2may_min_prime_factor=None, /):
    '-> uint2may_factorization/[may p2e/{prime:exp}]/[None,p2e...]'
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
    return (*u2f,)
def tabulate_may_all_prime_factors4uint_lt_(sz, /):
    '-> uint2may_all_prime_factors/[may [prime]]/[None,[prime]...]'
    return all_prime_factors_gen[:sz]

#class


if __name__ == "__main__":
    pass




__all__


from seed.math.prime_gens import detect_strong_pseudoprime__not_waste_too_much_time_

from seed.math.prime_gens import all_prime_factors_gen, tabulate_may_all_prime_factors4uint_lt_

from seed.math.prime_gens import min_prime_factor_gen, tabulate_may_min_prime_factor4uint_lt_, tabulate_may_factorization4uint_lt_



from seed.math.prime_gens import prime_gen__Eratosthenes_sieve, prime_gen__Miller_Rabin_primality_test

from seed.math.prime_gens import prime_gen, prime_filter__using_primality_test_, raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_

from seed.math.prime_gens import is_strong_pseudoprime__basis_, is_prime__using_A014233_, is_prime__le_pow2_81_, is_prime__tribool_, Case4is_prime__tribool_

from seed.math.prime_gens import is_prime__le_pow2_81_, next_pseudoprime__ge_, prev_may_pseudoprime__lt_, next_may_prime__le_pow2_81__ge_, prev_may_prime__le_pow2_81__lt_, raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_, raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_

from seed.math.prime_gens import iter_pseudoprimes__ge_, reversed_iter_pseudoprimes__lt_, iter_primes__le_pow2_81__ge_, reversed_iter_primes__le_pow2_81__lt_
from seed.math.prime_gens import iter_pairwise_diff_pseudoprimes__ge_, iter_pairwise_diff_primes__le_pow2_81__ge_

#######
from seed.math.prime_gens import iter_pseudoprimes__inside_, iter_pseudoprimes__ge_lt_# iter_pseudoprimes__between_
from seed.math.prime_gens import prev_may_pseudoprime__lt_, next_pseudoprime__ge_, reversed_iter_pseudoprimes__lt_, iter_pseudoprimes__ge_
from seed.math.prime_gens import prev_may_prime__le_pow2_81__lt_, next_may_prime__le_pow2_81__ge_, reversed_iter_primes__le_pow2_81__lt_, iter_primes__le_pow2_81__ge_
#######

from seed.math.prime_gens import is_strong_pseudoprime__basis__with_trial_division_, continuous_trial_division_, iter_continuous_prime_bases_, callable5xfilter4continuous_bases, mk_initial_state4filter4continuous_bases_, filter4continuous_bases4II_prime_basis_gtN, filter4continuous_bases4empty, mk_filter4continuous_bases4fixed_size
    # @20250130
from seed.math.prime_gens import mk_tribool_delegate5PRP_test_, is_strong_pseudoprime__basis__with_trial_division_
    # @20250131


from seed.math.prime_gens import *
