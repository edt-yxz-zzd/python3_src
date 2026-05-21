#__all__:goto
#@20260510:++优化冫复用小对象
#.e ../../python3_src/seed/math/__CMDS__.txt
#%s/seed[.]math[.]prime_gens[.]OverflowError__Miller_Rabin_primality_test__A014233/seed.math.primality_test.strong_probable_prime.OverflowError__Miller_Rabin_primality_test__A014233/g
r'''[[[
e ../../python3_src/seed/math/prime_gens.py
view ../../python3_src/seed/math/prime_gens.py.note.txt

[[
psp vs prp
[pseudoprime <: composite_number]
<<==:
@20250225
  /sdcard/0my_files/book/math/factorint/snd/The new book of prime number records(3ed)(1996)(Ribenboim).djvu
  [pg20/567]
PSP(a) - pseudoprime in base a
EPSP(a) - Euler pseudoprime in base a
SPSP(a) - strong pseudoprime in base a
LPSP(P,Q) - Lucas pseudoprime with parameters (P,Q)
ELPSP(P,Q) - Euler-Lucas pseudoprime with parameters (P, Q)
SLPSP(P,Q) - strong Lucas pseudoprime with parameters (P, Q)
SPSP
]]

[[
命名有误丶尚未订正
警告:见view others/数学/primality_test/proof_primality_via_GFsqN_test.txt
  看来我确实搞错了:应该是[pseudoprime =!= PRP][pseudoprime <: odd_composite <: composite][odd_prime <: SPRP <: PRP][SPRP == strong_probable_prime =!= strong_pseudoprime]
      #而非一直以为的『odd_prime <: SPRP == strong_pseudoprime』
[n <- [2..]][n%2==1]:
    [is_strong_probable_prime__base_(b;n) =[def]= [gcd(b,n)== 1][(ez,odd) :=> [2**ez*(2*hf+1) == n-1]][[b**(1+2*hf)%n==1]or[?[e :<- [0..<ez]] -> [b**(2**e*(1+2*hf)%n == n-1]]]]
    [is_strong_pseudoprime__base_(b;n) =[def]= [not is_prime(n)][is_strong_probable_prime__base_(b;n)]]

]]


e ../../python3_src/seed/math/prime_gens.py
    view ../../python3_src/seed/math/is_prime__le_pow2_64.py
        # replaced since 2**64 < A014233[-1]

e ../../python3_src/seed/math/factor_pint_by_trial_division_.py
e ../../python3_src/seed/math/factor_pint_into_strong_probable_primes_by_quadratic_sieve_.py

[[
!mv ../../python3_src/seed/math/lazy_prime_seq_by_Eratosthenes_sieve.py ../../python3_src/seed/math/prime_gens.py
.+1,$s/\<lazy_prime_seq_by_Eratosthenes_sieve\>/prime_gens/g
]]
[[
#@20250419之前:
rename:
    to match:
        next_may_prime__le_pow2_81__ge_
        raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_
.+1,$s/\<prev_may_prime__lt_\>/prev_may_prime__le_pow2_81__lt_/g
.+1,$s/\<raw_iter_all_strict_sorted_primes__using_primality_test__lt_\>/raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_/g
]]
[[
后续:_helper4renaming_pseudoprime_()

@20250419
:.+1,1475s/pseudoprime/probable_prime/g
    #替换48次/46行

]]
#重命名后:
__all__

seed.math.prime_gens
py -m seed.math.prime_gens
py -m nn_ns.app.debug_cmd   seed.math.prime_gens -x
py -m nn_ns.app.doctest_cmd seed.math.prime_gens:__doc__ -ht #  -ff -v -df
py -m nn_ns.app.doctest_cmd seed.math.prime_gens:__doc__ -ff
py -m nn_ns.app.doctest_cmd seed.math.prime_gens:_doc4tmp_test -ht






from seed.math.prime_gens import hold_all_weakrefs4caches_
000;    __ws = hold_all_weakrefs4caches_()
from seed.math.prime_gens import detect_strong_probable_prime__not_waste_too_much_time_

from seed.math.prime_gens import all_prime_factors_gen, tabulate_may_all_prime_factors4uint_lt_, tabulate_may_all_prime_factor_lflnkls4uint_lt_, extract_prime_factorization5uint2may_all_prime_factor_lflnkls_

from seed.math.prime_gens import min_prime_factor_gen, tabulate_may_min_prime_factor4uint_lt_, tabulate_may_factorization4uint_lt_



from seed.math.prime_gens import prime_gen__Eratosthenes_sieve, prime_gen__Miller_Rabin_primality_test

from seed.math.prime_gens import prime_gen, prime_filter__using_primality_test_, raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_

from seed.math.prime_gens import is_strong_probable_prime__basis_, is_prime__using_A014233_, is_prime__le_pow2_81_, is_prime__tribool_, Case4is_prime__tribool_







>>> list_islice_(9, reversed_iter_probable_primes__lt_(7))
[5, 3, 2]


py_adhoc_call   seed.math.prime_gens   @raw_list_all_strict_sorted_ints__ge2__with_min_prime_factor__sized_ =200 -to_cache_only_busy_primes_plus_next --may_primes=None

py_adhoc_call   seed.math.prime_gens   @_find_mismatch4diff_cases4is_prime__tribool_
... ...
2**521-1
    # choke here:
    # _find_mismatch4diff_cases4is_prime__tribool_:
    #   r1 = is_prime__tribool_(mn, case=C.ERH)
    # _is_strong_probable_prime_:
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




>>> ps_lt200 = raw_list_all_strict_sorted_primes__lt_(200, to_cache_only_busy_primes_plus_next=False, may_primes=None)
>>> ps_lt200
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
>>> ps_lt200 == list_all_strict_sorted_primes__lt_(200, _mk=list)
True
>>> tuple(ps_lt200) == list_all_strict_sorted_primes__lt_(200)
True
>>> sieve4uint2is_prime__lt_(20)
(False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True)
>>> sieve4uint2is_prime__lt_(20, _mk=list)
[False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]






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


######################
#@20250419
#新增这两行测试移至此处，以避免影响以上测试:
>>> __ws = hold_all_weakrefs4caches_()
>>> __ws.index(prime_gen.get_or_mk_lazy_prime_seq_())
4

######################


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
>>> min_prime_factor_gen[:20]
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



>>> tbl = TabulateMinPrimeFactor(2**9)
>>> len(tbl)
512
>>> rt = [*tabulate_may_min_prime_factor4uint_lt_(len(tbl))]
>>> rn = [*tbl.iter7naive_()]
>>> rf = [*tbl.iter7fancy_()]
>>> ri = [*tbl]
>>> rf == ri
True
>>> rn == rt
True
>>> rf == rt
True
>>> ri == rt
True
>>> rt
[None, None, 2, 3, 2, 5, 2, 7, 2, 3, 2, 11, 2, 13, 2, 3, 2, 17, 2, 19, 2, 3, 2, 23, 2, 5, 2, 3, 2, 29, 2, 31, 2, 3, 2, 5, 2, 37, 2, 3, 2, 41, 2, 43, 2, 3, 2, 47, 2, 7, 2, 3, 2, 53, 2, 5, 2, 3, 2, 59, 2, 61, 2, 3, 2, 5, 2, 67, 2, 3, 2, 71, 2, 73, 2, 3, 2, 7, 2, 79, 2, 3, 2, 83, 2, 5, 2, 3, 2, 89, 2, 7, 2, 3, 2, 5, 2, 97, 2, 3, 2, 101, 2, 103, 2, 3, 2, 107, 2, 109, 2, 3, 2, 113, 2, 5, 2, 3, 2, 7, 2, 11, 2, 3, 2, 5, 2, 127, 2, 3, 2, 131, 2, 7, 2, 3, 2, 137, 2, 139, 2, 3, 2, 11, 2, 5, 2, 3, 2, 149, 2, 151, 2, 3, 2, 5, 2, 157, 2, 3, 2, 7, 2, 163, 2, 3, 2, 167, 2, 13, 2, 3, 2, 173, 2, 5, 2, 3, 2, 179, 2, 181, 2, 3, 2, 5, 2, 11, 2, 3, 2, 191, 2, 193, 2, 3, 2, 197, 2, 199, 2, 3, 2, 7, 2, 5, 2, 3, 2, 11, 2, 211, 2, 3, 2, 5, 2, 7, 2, 3, 2, 13, 2, 223, 2, 3, 2, 227, 2, 229, 2, 3, 2, 233, 2, 5, 2, 3, 2, 239, 2, 241, 2, 3, 2, 5, 2, 13, 2, 3, 2, 251, 2, 11, 2, 3, 2, 257, 2, 7, 2, 3, 2, 263, 2, 5, 2, 3, 2, 269, 2, 271, 2, 3, 2, 5, 2, 277, 2, 3, 2, 281, 2, 283, 2, 3, 2, 7, 2, 17, 2, 3, 2, 293, 2, 5, 2, 3, 2, 13, 2, 7, 2, 3, 2, 5, 2, 307, 2, 3, 2, 311, 2, 313, 2, 3, 2, 317, 2, 11, 2, 3, 2, 17, 2, 5, 2, 3, 2, 7, 2, 331, 2, 3, 2, 5, 2, 337, 2, 3, 2, 11, 2, 7, 2, 3, 2, 347, 2, 349, 2, 3, 2, 353, 2, 5, 2, 3, 2, 359, 2, 19, 2, 3, 2, 5, 2, 367, 2, 3, 2, 7, 2, 373, 2, 3, 2, 13, 2, 379, 2, 3, 2, 383, 2, 5, 2, 3, 2, 389, 2, 17, 2, 3, 2, 5, 2, 397, 2, 3, 2, 401, 2, 13, 2, 3, 2, 11, 2, 409, 2, 3, 2, 7, 2, 5, 2, 3, 2, 419, 2, 421, 2, 3, 2, 5, 2, 7, 2, 3, 2, 431, 2, 433, 2, 3, 2, 19, 2, 439, 2, 3, 2, 443, 2, 5, 2, 3, 2, 449, 2, 11, 2, 3, 2, 5, 2, 457, 2, 3, 2, 461, 2, 463, 2, 3, 2, 467, 2, 7, 2, 3, 2, 11, 2, 5, 2, 3, 2, 479, 2, 13, 2, 3, 2, 5, 2, 487, 2, 3, 2, 491, 2, 17, 2, 3, 2, 7, 2, 499, 2, 3, 2, 503, 2, 5, 2, 3, 2, 509, 2, 7]

>>> tbl[0]
>>> tbl[1]
>>> tbl[2]
2
>>> tbl[3]
3
>>> tbl[4]
2
>>> tbl[6]
2
>>> tbl[9]
3
>>> tbl[15]
3
>>> tbl.extract_prime_factors_at_(2**3*3**2*5)
(2, 3, 5)
>>> tbl.extract_prime_factorization_at_(2**3*3**2*5) == {2:3, 3:2, 5:1}
True



>>> all_prime_factors_gen.get_or_mk_lazy_all_prime_factors_seq_()
LazySeq(LazyList([<...>]))
>>> all_prime_factors_gen.get_or_mk_lazy_all_prime_factors_seq_()[:20]
(None, (), (2,), (3,), (2,), (5,), (2, 3), (7,), (2,), (3,), (2, 5), (11,), (2, 3), (13,), (2, 7), (3, 5), (2,), (17,), (2, 3), (19,))
>>> all_prime_factors_gen[:20]
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
>>> uint2may_all_prime_factor_lflnkls = tabulate_may_all_prime_factor_lflnkls4uint_lt_(20)
>>> uint2may_all_prime_factor_lflnkls
(None, (), (2, ()), (3, ()), (2, ()), (5, ()), (2, (3, ())), (7, ()), (2, ()), (3, ()), (2, (5, ())), (11, ()), (2, (3, ())), (13, ()), (2, (7, ())), (3, (5, ())), (2, ()), (17, ()), (2, (3, ())), (19, ()))
>>> extract_prime_factorization5uint2may_all_prime_factor_lflnkls_(uint2may_all_prime_factor_lflnkls, 12) == {2:2,3:1}
True


    is_prime__le_pow2_81_
    raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_
    raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_
    next_probable_prime__ge_
    prev_may_probable_prime__lt_
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
seed.math.primality_test.strong_probable_prime.OverflowError__Miller_Rabin_primality_test__A014233: [3317044064679887385962123 == upperbound <= n == 3317044064679887385962123]
>>> pp = next_probable_prime__ge_(2**82) -2**82
>>> pp
9
>>> mm =  2**82 -prev_may_probable_prime__lt_(2**82)
>>> mm
57
>>> is_prime__le_pow2_81_(2**82+pp)
Traceback (most recent call last):
    ...
seed.math.primality_test.strong_probable_prime.OverflowError__Miller_Rabin_primality_test__A014233: [3317044064679887385962123 == upperbound <= n == 4835703278458516698824713]
>>> is_prime__le_pow2_81_(2**82-mm)
Traceback (most recent call last):
    ...
seed.math.primality_test.strong_probable_prime.OverflowError__Miller_Rabin_primality_test__A014233: [3317044064679887385962123 == upperbound <= n == 4835703278458516698824647]
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
seed.math.primality_test.strong_probable_prime.OverflowError__Miller_Rabin_primality_test__A014233: [3317044064679887385962123 == upperbound < end == 4835703278458516698824704]
>>> 2**81 -prev_may_prime__le_pow2_81__lt_(2**81)
51
>>> prev_may_prime__le_pow2_81__lt_(2) is None
True
>>> prev_may_prime__le_pow2_81__lt_(1) is None
True






>>> [*map(detect_strong_probable_prime__not_waste_too_much_time_, range(-1, 20))]
[0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1]
>>> [*map(calc_len_prime_basis4II_prime_basis_gtN_, [is_prime__le_pow2_81_.upperbound, 2**607-1, 2**1279-1])]
[19, 87, 158]
>>> detect_strong_probable_prime__not_waste_too_much_time_(is_prime__le_pow2_81_.upperbound)
-1
>>> detect_strong_probable_prime__not_waste_too_much_time_(2**607-1)
-1
>>> detect_strong_probable_prime__not_waste_too_much_time_(2**1279-1)
-1




    iter_probable_primes__ge_
    reversed_iter_probable_primes__lt_
    iter_primes__le_pow2_81__ge_
    reversed_iter_primes__le_pow2_81__lt_

>>> list_islice_(9, iter_probable_primes__ge_(-4))
[2, 3, 5, 7, 11, 13, 17, 19, 23]
>>> list_islice_(9, iter_probable_primes__ge_(0))
[2, 3, 5, 7, 11, 13, 17, 19, 23]
>>> list_islice_(9, iter_probable_primes__ge_(7))
[7, 11, 13, 17, 19, 23, 29, 31, 37]

>>> list_islice_(9, iter_primes__le_pow2_81__ge_(-4))
[2, 3, 5, 7, 11, 13, 17, 19, 23]
>>> list_islice_(9, iter_primes__le_pow2_81__ge_(0))
[2, 3, 5, 7, 11, 13, 17, 19, 23]
>>> list_islice_(9, iter_primes__le_pow2_81__ge_(7))
[7, 11, 13, 17, 19, 23, 29, 31, 37]

>>> list_islice_(9, reversed_iter_probable_primes__lt_(-4))
[]
>>> list_islice_(9, reversed_iter_probable_primes__lt_(0))
[]
>>> list_islice_(9, reversed_iter_probable_primes__lt_(7))
[5, 3, 2]

>>> list_islice_(9, reversed_iter_primes__le_pow2_81__lt_(-4))
[]
>>> list_islice_(9, reversed_iter_primes__le_pow2_81__lt_(0))
[]
>>> list_islice_(9, reversed_iter_primes__le_pow2_81__lt_(7))
[5, 3, 2]

#>>> for a, b in zip(iter_probable_primes__ge_(0), iter_primes__le_pow2_81__ge_(0)):
#...     if not a == b:break
#>>> (a, b)
[:next_probable_prime__ge___vs__next_may_prime__le_pow2_81__ge_]:goto
>>> A014233[12] == (3317044064679887385961981)
True
>>> next_probable_prime__ge_(3317044064679887385961981)
3317044064679887385962123
>>> next_probable_prime__ge_(3317044064679887385961980)
3317044064679887385962123
>>> next_probable_prime__ge_(3317044064679887385961981) -3317044064679887385961981
142

    iter_pairwise_diff_probable_primes__ge_
    iter_pairwise_diff_primes__le_pow2_81__ge_
>>> list_islice_(9, iter_pairwise_diff_probable_primes__ge_(0))
[1, 2, 2, 4, 2, 4, 2, 4, 6]
>>> list_islice_(9, iter_pairwise_diff_primes__le_pow2_81__ge_(0))
[1, 2, 2, 4, 2, 4, 2, 4, 6]



    iter_probable_primes__inside_
    iter_probable_primes__ge_lt_   iter_probable_primes__between_
>>> iter_probable_primes__between_ is iter_probable_primes__ge_lt_
True
>>> [*iter_probable_primes__inside_(range(-5, 11))]
[2, 3, 5, 7]
>>> [*iter_probable_primes__between_(-5, 11)]
[2, 3, 5, 7]
>>> [*iter_probable_primes__between_(-5, 11, reverse=True)]
[7, 5, 3, 2]
>>> [*iter_probable_primes__between_(-5, 11, case=[], reverse=True)] # see:is_prime__tribool_() since < 2**81
[7, 5, 3, 2]
>>> [*iter_probable_primes__between_(-5, 11, case=[], reverse=True, skip_A014233=True)] # see:is_prime__tribool_() since skip_A014233 # 由于打补丁，之前相当于skip_check=True
[7, 5, 3, 2]
>>> [*iter_probable_primes__between_(-5, 11, case=[], reverse=True, skip_A014233=True, skip_check=True)] # see:is_prime__tribool_() since skip_A014233
[9, 7, 5, 3, 2]

>>> [*map((2**100).__rsub__, islice(iter_probable_primes__between_(2**100, 2**100+8000, case=[], reverse=True, skip_A014233=True), 9))] # see:is_prime__tribool_() since skip_A014233 # 由于打补丁，之前相当于skip_check=True
[7995, 7987, 7983, 7981, 7977, 7965, 7947, 7945, 7911]
>>> [*map((2**100).__rsub__, islice(iter_probable_primes__between_(2**100, 2**100+8000, case=[], reverse=True, skip_A014233=True, skip_check=True), 9))] # see:is_prime__tribool_() since skip_A014233
[7999, 7997, 7995, 7993, 7991, 7989, 7987, 7985, 7983]
>>> [*map((2**100).__rsub__, islice(iter_probable_primes__between_(2**100, 2**100+8000, case=[], reverse=True), 9))]
[7737, 7717, 7713, 7701, 7623, 7557, 7531, 7491, 7477]
>>> [*map((2**100).__rsub__, islice(iter_probable_primes__between_(2**100, 2**100+8000, case=None, reverse=True), 9))]
[7737, 7717, 7713, 7701, 7623, 7557, 7531, 7491, 7477]


is_strong_probable_prime__basis__with_trial_division_
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

>>> [(n, is_strong_probable_prime__basis__with_trial_division_(None, [], n)) for n in range(-2, 20)]
[(-2, False), (-1, False), (0, False), (1, False), (2, True), (3, True), (4, False), (5, True), (6, False), (7, True), (8, False), (9, False), (10, False), (11, True), (12, False), (13, True), (14, False), (15, False), (16, False), (17, True), (18, False), (19, True)]
>>> [(n, r) for n in range(-2, 2**16) for r in [is_strong_probable_prime__basis__with_trial_division_(None, [2], n)] if not r is is_prime__le_pow2_81_(n)]
[(2047, True), (3277, True), (4033, True), (4681, True), (8321, True), (42799, True), (49141, True), (65281, True)]

xfilter4continuous_bases:=False
    filter4continuous_bases4empty
>>> [(n, [*iter_continuous_prime_bases_(False, n)]) for n in range(-2, 20)]
[(-2, []), (-1, []), (0, []), (1, []), (2, []), (3, []), (4, []), (5, []), (6, []), (7, []), (8, []), (9, []), (10, []), (11, []), (12, []), (13, []), (14, []), (15, []), (16, []), (17, []), (18, []), (19, [])]
>>> [(n, continuous_trial_division_(False, n)) for n in range(-2, 20)]
[(-2, 1), (-1, 1), (0, 1), (1, 1), (2, -1), (3, -1), (4, 2), (5, -1), (6, 2), (7, -1), (8, 2), (9, 0), (10, 2), (11, 0), (12, 2), (13, 0), (14, 2), (15, 0), (16, 2), (17, 0), (18, 2), (19, 0)]
>>> [(n, r) for n in range(-2, 2**12) for r in [is_strong_probable_prime__basis__with_trial_division_(False, [2], n)] if not r is is_prime__le_pow2_81_(n)]
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
    [delegate := mk_tribool_delegate5PRP_test_(is_strong_probable_prime__basis__with_trial_division_, xfilter4continuous_bases4div, bases4SPRP)]
>>> delegate = mk_tribool_delegate5PRP_test_(is_strong_probable_prime__basis__with_trial_division_, xfilter4continuous_bases4div:=None, bases4SPRP:=[2,3,5,7])
>>> [(n, is_prime__tribool_(n, case=delegate)) for n in range(-2, 20)]
[(-2, False), (-1, False), (0, False), (1, False), (2, Ellipsis), (3, Ellipsis), (4, False), (5, Ellipsis), (6, False), (7, Ellipsis), (8, False), (9, False), (10, False), (11, Ellipsis), (12, False), (13, Ellipsis), (14, False), (15, False), (16, False), (17, Ellipsis), (18, False), (19, Ellipsis)]
>>> bool(...)
True



    iter_primes__ge_lt_
        iter_primes__between_
>>> iter_primes__between_ is iter_primes__ge_lt_
True

>>> is_prime__using_A014233_.upperbound - 2**81
899192425450629036549771
>>> bin(is_prime__using_A014233_.upperbound - 2**81)
'0b10111110011010010101000110101101110001011011001000100100000100001010011010001011'

>>> [*islice(iter_primes__ge_lt_(is_prime__using_A014233_.upperbound -500, None), 99)]
[3317044064679887385961657, 3317044064679887385961753, 3317044064679887385961763, 3317044064679887385961783, 3317044064679887385961801, 3317044064679887385961813]
>>> [*islice(iter_primes__ge_lt_(is_prime__using_A014233_.upperbound -500, 3317044064679887385961753), 99)]
[3317044064679887385961657]
>>> [*islice(iter_primes__ge_lt_(is_prime__using_A014233_.upperbound -500, 3317044064679887385961753+1), 99)]
[3317044064679887385961657, 3317044064679887385961753]



















######################
[[
check_args4core_sieve_interval__ge_le
    core_sieve4primes__ge_le
    core_sieve4offsetted_uint2is_prime__ge_le
    core_sieve4prime_factorization__ge_le
    core_sieve4pairs8prime_factorization__ge_le
    core_sieve4prime_factors__ge_le
>>> min_u = 10
>>> max1_u = calc_min_end5begin6args4sieve_interval_(min_u)
>>> max1_u
14
>>> max_u = -1+max1_u
>>> core_sieve4primes__ge_le(min_u, max_u)
(11, 13)
>>> core_sieve4offsetted_uint2is_prime__ge_le(min_u, max_u)
[False, True, False, True]
>>> core_sieve4prime_factorization__ge_le(min_u, max_u)
[{2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}]
>>> core_sieve4pairs8prime_factorization__ge_le(min_u, max_u)
[((2, 1), (5, 1)), ((11, 1),), ((2, 2), (3, 1)), ((13, 1),)]
>>> core_sieve4prime_factors__ge_le(min_u, max_u)
[(2, 5), (11,), (2, 3), (13,)]


>>> core_sieve4primes__ge_le(min_u, ...)
(11, 13)
>>> core_sieve4offsetted_uint2is_prime__ge_le(min_u, ...)
[False, True, False, True]
>>> core_sieve4prime_factorization__ge_le(min_u, ...)
[{2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}]
>>> core_sieve4pairs8prime_factorization__ge_le(min_u, ...)
[((2, 1), (5, 1)), ((11, 1),), ((2, 2), (3, 1)), ((13, 1),)]
>>> core_sieve4prime_factors__ge_le(min_u, ...)
[(2, 5), (11,), (2, 3), (13,)]



>>> tabulate_may_all_prime_factors4uint_lt_(1+max_u, _mk=list)[min_u:]
[(2, 5), (11,), (2, 3), (13,)]




>>> min_u = 2**32
>>> max1_u = calc_min_end5begin6args4sieve_interval_(min_u)
>>> max1_u -min_u
65537
>>> max1_u
4295032833
>>> max_u = -1+max1_u

#>>> core_sieve4prime_factors__ge_le(min_u, max_u) == tabulate_may_all_prime_factors4uint_lt_(1+max_u, _mk=list)[min_u:]
    手机内存不足

>>> _u2ps = core_sieve4prime_factors__ge_le(min_u, max_u, _validate=True)
>>> len(_u2ps)
65537
>>> _u2ps[:30]
[(2,), (641, 6700417), (2, 3, 715827883), (7, 613566757), (2, 5, 13, 41, 61, 1321), (3, 47, 3384529), (2, 83, 1277, 20261), (11, 6323, 61751), (2, 3, 59, 3033169), (5, 9629, 89209), (2, 7, 43826197), (3, 23, 53, 1174451), (2, 1073741827), (19, 29, 7794859), (2, 3, 5, 131, 364289), (4294967311,), (2, 17, 15790321), (3, 7, 13, 15732481), (2, 11, 4219, 46273), (5, 26053, 32971), (2, 3, 149, 2402107), (3209, 1338413), (2, 2147483659), (3, 11393, 41887), (2, 5, 7, 1901, 8069), (733, 5859437), (2, 3, 2539, 281933), (31, 43, 3222031), (2, 1073741831), (3, 5, 11, 79, 65899)]







]]

######################
[[
new ver: tabulate_may_factorization4uint_lt_<<==:
    tabulate_may_prime_factorization4uint_lt_
    tabulate_may_pairs8prime_factorization4uint_lt_

def tabulate_may_prime_factorization4uint_lt_(sz, /, *, _mk=tuple, dict_vs_pairs=False, _validate=False):
>>> tabulate_may_prime_factorization4uint_lt_(50, _validate=True) == \
... (None
... ,{}
... ,{2: 1}
... ,{3: 1}
... ,{2: 2}
... ,{5: 1}
... ,{2: 1, 3: 1}
... ,{7: 1}
... ,{2: 3}
... ,{3: 2}
... ,{2: 1, 5: 1}
... ,{11: 1}
... ,{2: 2, 3: 1}
... ,{13: 1}
... ,{2: 1, 7: 1}
... ,{3: 1, 5: 1}
... ,{2: 4}
... ,{17: 1}
... ,{2: 1, 3: 2}
... ,{19: 1}
... ,{2: 2, 5: 1}
... ,{3: 1, 7: 1}
... ,{2: 1, 11: 1}
... ,{23: 1}
... ,{2: 3, 3: 1}
... ,{5: 2}
... ,{2: 1, 13: 1}
... ,{3: 3}
... ,{2: 2, 7: 1}
... ,{29: 1}
... ,{2: 1, 3: 1, 5: 1}
... ,{31: 1}
... ,{2: 5}
... ,{3: 1, 11: 1}
... ,{2: 1, 17: 1}
... ,{5: 1, 7: 1}
... ,{2: 2, 3: 2}
... ,{37: 1}
... ,{2: 1, 19: 1}
... ,{3: 1, 13: 1}
... ,{2: 3, 5: 1}
... ,{41: 1}
... ,{2: 1, 3: 1, 7: 1}
... ,{43: 1}
... ,{2: 2, 11: 1}
... ,{3: 2, 5: 1}
... ,{2: 1, 23: 1}
... ,{47: 1}
... ,{2: 4, 3: 1}
... ,{7: 2}
... )
True
>>> tabulate_may_pairs8prime_factorization4uint_lt_(50, _validate=True) == \
... (None
... ,()
... ,((2, 1),)
... ,((3, 1),)
... ,((2, 2),)
... ,((5, 1),)
... ,((2, 1), (3, 1))
... ,((7, 1),)
... ,((2, 3),)
... ,((3, 2),)
... ,((2, 1), (5, 1))
... ,((11, 1),)
... ,((2, 2), (3, 1))
... ,((13, 1),)
... ,((2, 1), (7, 1))
... ,((3, 1), (5, 1))
... ,((2, 4),)
... ,((17, 1),)
... ,((2, 1), (3, 2))
... ,((19, 1),)
... ,((2, 2), (5, 1))
... ,((3, 1), (7, 1))
... ,((2, 1), (11, 1))
... ,((23, 1),)
... ,((2, 3), (3, 1))
... ,((5, 2),)
... ,((2, 1), (13, 1))
... ,((3, 3),)
... ,((2, 2), (7, 1))
... ,((29, 1),)
... ,((2, 1), (3, 1), (5, 1))
... ,((31, 1),)
... ,((2, 5),)
... ,((3, 1), (11, 1))
... ,((2, 1), (17, 1))
... ,((5, 1), (7, 1))
... ,((2, 2), (3, 2))
... ,((37, 1),)
... ,((2, 1), (19, 1))
... ,((3, 1), (13, 1))
... ,((2, 3), (5, 1))
... ,((41, 1),)
... ,((2, 1), (3, 1), (7, 1))
... ,((43, 1),)
... ,((2, 2), (11, 1))
... ,((3, 2), (5, 1))
... ,((2, 1), (23, 1))
... ,((47, 1),)
... ,((2, 4), (3, 1))
... ,((7, 2),)
... )
True

]]




######################

[[
######################
check_args4sieve_interval__ge_lt
    calc_min_end5begin6args4sieve_interval_
        test4calc_min_end5begin6args4sieve_interval_
        iter_min_ends5begin6args4sieve_interval_
    sieve_interval4primes__ge_lt
    sieve_interval4offsetted_uint2is_prime__ge_lt
    sieve_interval4prime_factorization__ge_lt
    sieve_interval4prime_factors__ge_lt

>>> calc_min_end5begin6args4sieve_interval_(9900)
10000
>>> prime_gen[1219:1230]
(9887, 9901, 9907, 9923, 9929, 9931, 9941, 9949, 9967, 9973, 10007)
>>> sieve_interval4primes__ge_lt(9900, 10001)#, _validate=True
[9901, 9907, 9923, 9929, 9931, 9941, 9949, 9967, 9973]
>>> sieve_interval4offsetted_uint2is_prime__ge_lt(9900, 10001) == \
... [False, True, False, False, False, False, False, True, False, False
... , False, False, False, False, False, False, False, False, False, False
... , False, False, False, True, False, False, False, False, False, True
... , False, True, False, False, False, False, False, False, False, False
... , False, True, False, False, False, False, False, False, False, True
... , False, False, False, False, False, False, False, False, False, False
... , False, False, False, False, False, False, False, True, False, False
... , False, False, False, True, False, False, False, False, False, False
... , False, False, False, False, False, False, False, False, False, False
... , False, False, False, False, False, False, False, False, False, False
... , False]
True
>>> sieve_interval4prime_factorization__ge_lt(9900, 10001, _validate=True) == \
... [{2: 2, 3: 2, 5: 2, 11: 1}
... ,{9901: 1}
... ,{2: 1, 4951: 1}
... ,{3: 1, 3301: 1}
... ,{2: 4, 619: 1}
... ,{5: 1, 7: 1, 283: 1}
... ,{2: 1, 3: 1, 13: 1, 127: 1}
... ,{9907: 1}
... ,{2: 2, 2477: 1}
... ,{3: 3, 367: 1}
... ,{2: 1, 5: 1, 991: 1}
... ,{11: 1, 17: 1, 53: 1}
... ,{2: 3, 3: 1, 7: 1, 59: 1}
... ,{23: 1, 431: 1}
... ,{2: 1, 4957: 1}
... ,{3: 1, 5: 1, 661: 1}
... ,{2: 2, 37: 1, 67: 1}
... ,{47: 1, 211: 1}
... ,{2: 1, 3: 2, 19: 1, 29: 1}
... ,{7: 1, 13: 1, 109: 1}
... ,{2: 6, 5: 1, 31: 1}
... ,{3: 1, 3307: 1}
... ,{2: 1, 11: 2, 41: 1}
... ,{9923: 1}
... ,{2: 2, 3: 1, 827: 1}
... ,{5: 2, 397: 1}
... ,{2: 1, 7: 1, 709: 1}
... ,{3: 2, 1103: 1}
... ,{2: 3, 17: 1, 73: 1}
... ,{9929: 1}
... ,{2: 1, 3: 1, 5: 1, 331: 1}
... ,{9931: 1}
... ,{2: 2, 13: 1, 191: 1}
... ,{3: 1, 7: 1, 11: 1, 43: 1}
... ,{2: 1, 4967: 1}
... ,{5: 1, 1987: 1}
... ,{2: 4, 3: 3, 23: 1}
... ,{19: 1, 523: 1}
... ,{2: 1, 4969: 1}
... ,{3: 1, 3313: 1}
... ,{2: 2, 5: 1, 7: 1, 71: 1}
... ,{9941: 1}
... ,{2: 1, 3: 1, 1657: 1}
... ,{61: 1, 163: 1}
... ,{2: 3, 11: 1, 113: 1}
... ,{3: 2, 5: 1, 13: 1, 17: 1}
... ,{2: 1, 4973: 1}
... ,{7: 3, 29: 1}
... ,{2: 2, 3: 1, 829: 1}
... ,{9949: 1}
... ,{2: 1, 5: 2, 199: 1}
... ,{3: 1, 31: 1, 107: 1}
... ,{2: 5, 311: 1}
... ,{37: 1, 269: 1}
... ,{2: 1, 3: 2, 7: 1, 79: 1}
... ,{5: 1, 11: 1, 181: 1}
... ,{2: 2, 19: 1, 131: 1}
... ,{3: 1, 3319: 1}
... ,{2: 1, 13: 1, 383: 1}
... ,{23: 1, 433: 1}
... ,{2: 3, 3: 1, 5: 1, 83: 1}
... ,{7: 1, 1423: 1}
... ,{2: 1, 17: 1, 293: 1}
... ,{3: 5, 41: 1}
... ,{2: 2, 47: 1, 53: 1}
... ,{5: 1, 1993: 1}
... ,{2: 1, 3: 1, 11: 1, 151: 1}
... ,{9967: 1}
... ,{2: 4, 7: 1, 89: 1}
... ,{3: 1, 3323: 1}
... ,{2: 1, 5: 1, 997: 1}
... ,{13: 2, 59: 1}
... ,{2: 2, 3: 2, 277: 1}
... ,{9973: 1}
... ,{2: 1, 4987: 1}
... ,{3: 1, 5: 2, 7: 1, 19: 1}
... ,{2: 3, 29: 1, 43: 1}
... ,{11: 1, 907: 1}
... ,{2: 1, 3: 1, 1663: 1}
... ,{17: 1, 587: 1}
... ,{2: 2, 5: 1, 499: 1}
... ,{3: 2, 1109: 1}
... ,{2: 1, 7: 1, 23: 1, 31: 1}
... ,{67: 1, 149: 1}
... ,{2: 8, 3: 1, 13: 1}
... ,{5: 1, 1997: 1}
... ,{2: 1, 4993: 1}
... ,{3: 1, 3329: 1}
... ,{2: 2, 11: 1, 227: 1}
... ,{7: 1, 1427: 1}
... ,{2: 1, 3: 3, 5: 1, 37: 1}
... ,{97: 1, 103: 1}
... ,{2: 3, 1249: 1}
... ,{3: 1, 3331: 1}
... ,{2: 1, 19: 1, 263: 1}
... ,{5: 1, 1999: 1}
... ,{2: 2, 3: 1, 7: 2, 17: 1}
... ,{13: 1, 769: 1}
... ,{2: 1, 4999: 1}
... ,{3: 2, 11: 1, 101: 1}
... ,{2: 4, 5: 4}
... ]
True
>>> sieve_interval4prime_factors__ge_lt(9900, 10001, _validate=True) == \
... [(2, 3, 5, 11)
... ,(9901,)
... ,(2, 4951)
... ,(3, 3301)
... ,(2, 619)
... ,(5, 7, 283)
... ,(2, 3, 13, 127)
... ,(9907,)
... ,(2, 2477)
... ,(3, 367)
... ,(2, 5, 991)
... ,(11, 17, 53)
... ,(2, 3, 7, 59)
... ,(23, 431)
... ,(2, 4957)
... ,(3, 5, 661)
... ,(2, 37, 67)
... ,(47, 211)
... ,(2, 3, 19, 29)
... ,(7, 13, 109)
... ,(2, 5, 31)
... ,(3, 3307)
... ,(2, 11, 41)
... ,(9923,)
... ,(2, 3, 827)
... ,(5, 397)
... ,(2, 7, 709)
... ,(3, 1103)
... ,(2, 17, 73)
... ,(9929,)
... ,(2, 3, 5, 331)
... ,(9931,)
... ,(2, 13, 191)
... ,(3, 7, 11, 43)
... ,(2, 4967)
... ,(5, 1987)
... ,(2, 3, 23)
... ,(19, 523)
... ,(2, 4969)
... ,(3, 3313)
... ,(2, 5, 7, 71)
... ,(9941,)
... ,(2, 3, 1657)
... ,(61, 163)
... ,(2, 11, 113)
... ,(3, 5, 13, 17)
... ,(2, 4973)
... ,(7, 29)
... ,(2, 3, 829)
... ,(9949,)
... ,(2, 5, 199)
... ,(3, 31, 107)
... ,(2, 311)
... ,(37, 269)
... ,(2, 3, 7, 79)
... ,(5, 11, 181)
... ,(2, 19, 131)
... ,(3, 3319)
... ,(2, 13, 383)
... ,(23, 433)
... ,(2, 3, 5, 83)
... ,(7, 1423)
... ,(2, 17, 293)
... ,(3, 41)
... ,(2, 47, 53)
... ,(5, 1993)
... ,(2, 3, 11, 151)
... ,(9967,)
... ,(2, 7, 89)
... ,(3, 3323)
... ,(2, 5, 997)
... ,(13, 59)
... ,(2, 3, 277)
... ,(9973,)
... ,(2, 4987)
... ,(3, 5, 7, 19)
... ,(2, 29, 43)
... ,(11, 907)
... ,(2, 3, 1663)
... ,(17, 587)
... ,(2, 5, 499)
... ,(3, 1109)
... ,(2, 7, 23, 31)
... ,(67, 149)
... ,(2, 3, 13)
... ,(5, 1997)
... ,(2, 4993)
... ,(3, 3329)
... ,(2, 11, 227)
... ,(7, 1427)
... ,(2, 3, 5, 37)
... ,(97, 103)
... ,(2, 1249)
... ,(3, 3331)
... ,(2, 19, 263)
... ,(5, 1999)
... ,(2, 3, 7, 17)
... ,(13, 769)
... ,(2, 4999)
... ,(3, 11, 101)
... ,(2, 5)
... ]
True

>>> sieve_interval4primes__ge_lt(9, 14)
[11, 13]
>>> sieve_interval4primes__ge_lt(10, 14)
[11, 13]
>>> sieve_interval4primes__ge_lt(10, 13)
Traceback (most recent call last):
    ...
TypeError: (10, 13)






]]




















######################
[[
py_adhoc_call { -lineno }  seed.math.prime_gens   ,iter_find_best_wheel_paramss4sieve_lt_  ='[2**ez for ez in range(1+60)]'
0:(1, (0, 1, 1, ()))
1:(2, (0, 1, 2, ()))
2:(4, (0, 1, 4, ()))
3:(8, (1, 2, 7, (2,)))
4:(16, (1, 2, 11, (2,)))
5:(32, (2, 6, 19, (2, 3)))
6:(64, (2, 6, 30, (2, 3)))
7:(128, (2, 6, 51, (2, 3)))
8:(256, (2, 6, 94, (2, 3)))
9:(512, (3, 30, 175, (2, 3, 5)))
10:(1024, (3, 30, 312, (2, 3, 5)))
11:(2048, (3, 30, 585, (2, 3, 5)))
12:(4096, (3, 30, 1131, (2, 3, 5)))
13:(8192, (4, 210, 2131, (2, 3, 5, 7)))
14:(16384, (4, 210, 4003, (2, 3, 5, 7)))
15:(32768, (4, 210, 7748, (2, 3, 5, 7)))
16:(65536, (4, 210, 15238, (2, 3, 5, 7)))
17:(131072, (5, 2310, 30026, (2, 3, 5, 7, 11)))
18:(262144, (5, 2310, 57262, (2, 3, 5, 7, 11)))
19:(524288, (5, 2310, 111733, (2, 3, 5, 7, 11)))
20:(1048576, (5, 2310, 220676, (2, 3, 5, 7, 11)))
21:(2097152, (6, 30030, 438041, (2, 3, 5, 7, 11, 13)))
22:(4194304, (6, 30030, 840292, (2, 3, 5, 7, 11, 13)))
23:(8388608, (6, 30030, 1644794, (2, 3, 5, 7, 11, 13)))
24:(16777216, (6, 30030, 3253798, (2, 3, 5, 7, 11, 13)))
25:(33554432, (6, 30030, 6471805, (2, 3, 5, 7, 11, 13)))
26:(67108864, (7, 510510, 12717522, (2, 3, 5, 7, 11, 13, 17)))
27:(134217728, (7, 510510, 24832374, (2, 3, 5, 7, 11, 13, 17)))
28:(268435456, (7, 510510, 49062077, (2, 3, 5, 7, 11, 13, 17)))
29:(536870912, (7, 510510, 97521484, (2, 3, 5, 7, 11, 13, 17)))
30:(1073741824, (7, 510510, 194440297, (2, 3, 5, 7, 11, 13, 17)))
31:(2147483648, (8, 9699690, 378629862, (2, 3, 5, 7, 11, 13, 17, 19)))
32:(4294967296, (8, 9699690, 745901154, (2, 3, 5, 7, 11, 13, 17, 19)))
33:(8589934592, (8, 9699690, 1480443737, (2, 3, 5, 7, 11, 13, 17, 19)))
34:(17179869184, (8, 9699690, 2949528903, (2, 3, 5, 7, 11, 13, 17, 19)))
35:(34359738368, (9, 223092870, 5880435823, (2, 3, 5, 7, 11, 13, 17, 19, 23)))
36:(68719476736, (9, 223092870, 11501283416, (2, 3, 5, 7, 11, 13, 17, 19, 23)))
37:(137438953472, (9, 223092870, 22742978601, (2, 3, 5, 7, 11, 13, 17, 19, 23)))
38:(274877906944, (9, 223092870, 45226368971, (2, 3, 5, 7, 11, 13, 17, 19, 23)))
39:(549755813888, (9, 223092870, 90193149711, (2, 3, 5, 7, 11, 13, 17, 19, 23)))
40:(1099511627776, (9, 223092870, 180126711191, (2, 3, 5, 7, 11, 13, 17, 19, 23)))
41:(2199023255552, (10, 6469693230, 354821180062, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)))
42:(4398046511104, (10, 6469693230, 702150796813, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)))
43:(8796093022208, (10, 6469693230, 1396810030315, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)))
44:(17592186044416, (10, 6469693230, 2786128497319, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)))
45:(35184372088832, (10, 6469693230, 5564765431327, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)))
46:(70368744177664, (11, 200560490130, 10987230530628, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)))
47:(140737488355328, (11, 200560490130, 21743244468725, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)))
48:(281474976710656, (11, 200560490130, 43255272344919, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)))
49:(562949953421312, (11, 200560490130, 86279328097308, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)))
50:(1125899906842624, (11, 200560490130, 172327439602085, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)))
51:(2251799813685248, (12, 7420738134810, 343414305299262, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)))
52:(4503599627370496, (12, 7420738134810, 678304252777313, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)))
53:(9007199254740992, (12, 7420738134810, 1348084147733415, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)))
54:(18014398509481984, (12, 7420738134810, 2687643937645619, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)))
55:(36028797018963968, (12, 7420738134810, 5366763517470028, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)))
56:(72057594037927936, (12, 7420738134810, 10725002677118846, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)))
57:(144115188075855872, (13, 304250263527210, 21258596649612743, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)))
58:(288230376151711744, (13, 304250263527210, 42168798248242275, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)))
59:(576460752303423488, (13, 304250263527210, 83989201445501340, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)))
60:(1152921504606846976, (13, 304250263527210, 167630007840019470, (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41)))

]]
[[
test:calc_min_end5begin6args4sieve_interval_
py_adhoc_call  seed.math.prime_gens   @test4calc_min_end5begin6args4sieve_interval_ ='range(1,1+2**20)'
    ok
py_adhoc_call  seed.math.prime_gens   @list.20:iter_min_ends5begin6args4sieve_interval_ =1
[2, 4, 7, 10, 14, 19, 24, 30, 36, 43, 50, 58, 67, 76, 86, 96, 107, 118, 130, 142]
py_adhoc_call  seed.math.prime_gens   @list.20:iter_min_ends5begin6args4sieve_interval_ =1 +with_begin
[(1, 2), (2, 4), (4, 7), (7, 10), (10, 14), (14, 19), (19, 24), (24, 30), (30, 36), (36, 43), (43, 50), (50, 58), (58, 67), (67, 76), (76, 86), (86, 96), (96, 107), (107, 118), (118, 130), (130, 142)]

]]
[[
test:_mk_offsetted_u2num_bits7remain_
py_adhoc_call  seed.math.prime_gens   @_test4mk_offsetted_u2num_bits7remain_
    ok
]]



#]]]'''
_doc4tmp_test = r'''
>>> 

'''#'''
#重命名前:
#.__all__ = r'''
#.hold_all_weakrefs4caches_
#.
#.prime_gen
#.prime_gen__Miller_Rabin_primality_test
#.
#.is_strong_pseudoprime__basis_
#.    is_strong_pseudoprime__basis__with_trial_division_
#.    is_prime__le_pow2_81_
#.        prime_filter__using_primality_test_
#.            raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_
#.                prev_may_prime__le_pow2_81__lt_
#.                    reversed_iter_primes__le_pow2_81__lt_
#.            raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_
#.                next_may_prime__le_pow2_81__ge_
#.                    iter_primes__le_pow2_81__ge_
#.                        iter_pairwise_diff_primes__le_pow2_81__ge_
#.            iter_primes__ge_lt_         iter_primes__between_
#.        is_prime__tribool_
#.            Case4is_prime__tribool_
#.            detect_strong_pseudoprime__not_waste_too_much_time_
#.            next_pseudoprime__ge_
#.            prev_may_pseudoprime__lt_
#.                reversed_iter_pseudoprimes__lt_
#.                iter_pseudoprimes__ge_
#.                    iter_pairwise_diff_pseudoprimes__ge_
#.            iter_pseudoprimes__inside_
#.            iter_pseudoprimes__ge_lt_   iter_pseudoprimes__between_
#.
#.
#.
#.min_prime_factor_gen
#.    tabulate_may_min_prime_factor4uint_lt_
#.    tabulate_may_factorization4uint_lt_
#.
#.all_prime_factors_gen
#.    tabulate_may_all_prime_factors4uint_lt_
#.
#.
#.
#.
#.
#.
#.
#.
#.
#.
#.
#.
#.raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_
#.    raw_list_all_strict_sorted_ints__ge2__with_min_prime_factor__sized_
#.    raw_iter_all_strict_sorted_primes_
#.        raw_iter_all_strict_sorted_primes__lt_
#.            raw_list_all_strict_sorted_primes__lt_
#.
#.
#.    GlobalControl4PrimeGenerator__Eratosthenes_sieve
#.        prime_gen__Eratosthenes_sieve
#.            prime_gen
#.    GlobalControl4PrimeGenerator__Miller_Rabin_primality_test
#.        prime_gen__Miller_Rabin_primality_test
#.
#.Error
#.    Bool5TriboolFail__probably_prime
#.    OverflowError__Miller_Rabin_primality_test__A014233
#.    IsPrimeError
#.
#.
#.A014233         n2upperbound4Miller_Rabin_primality_test_using_first_n_plus1_primes_as_basis
#.    prime_basis4A014233
#.        prime_basis_set4A014233
#.
#.
#.is_strong_pseudoprime__basis_
#.    is_strong_pseudoprime_
#.        iter_until_found_min_prime_witness4odd_composite_
#.            find_min_prime_witness4odd_composite_
#.
#.    is_prime__using_A014233_        is_prime__le_pow2_81_
#.        default4is_prime_and_may_upperbound
#.            prime_filter__using_primality_test_
#.                raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_
#.                    prev_may_prime__le_pow2_81__lt_
#.                raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_
#.                    next_may_prime__le_pow2_81__ge_
#.
#.        is_prime__tribool_
#.            mk_tribool_delegate5PRP_test_
#.                is_strong_pseudoprime__basis__with_trial_division_
#.            Case4is_prime__tribool_
#.            detect_strong_pseudoprime__not_waste_too_much_time_
#.            iter_prime_basis4II_prime_basis_gtN_
#.                calc_len_prime_basis4II_prime_basis_gtN_
#.            next_pseudoprime__ge_
#.            prev_may_pseudoprime__lt_
#.
#.
#.
#.GlobalControl4MinPrimeFactorGenerator__Eratosthenes_sieve
#.    min_prime_factor_gen__Eratosthenes_sieve
#.        min_prime_factor_gen
#.        tabulate_may_min_prime_factor4uint_lt_
#.        tabulate_may_factorization4uint_lt_
#.
#.GlobalControl4AllPrimeFactorsGenerator__Eratosthenes_sieve
#.    all_prime_factors_gen__Eratosthenes_sieve
#.        all_prime_factors_gen
#.        tabulate_may_all_prime_factors4uint_lt_
#.
#.
#.
#.mk_tribool_delegate5PRP_test_
#.is_strong_pseudoprime__basis__with_trial_division_
#.    continuous_trial_division_
#.        iter_continuous_prime_bases_
#.    callable5xfilter4continuous_bases
#.    mk_initial_state4filter4continuous_bases_
#.        filter4continuous_bases4II_prime_basis_gtN
#.        filter4continuous_bases4empty
#.        mk_filter4continuous_bases4fixed_size
#.
#.
#.
#.pairwise_diff_
#.'''.split()#'''

r'''[[[
后续:_helper4renaming_pseudoprime_()

@20250419
:.+1,.+130s/pseudoprime/probable_prime/g
    #替换18次/17行

#]]]'''#'''
#重命名后:
__all__ = r'''
hold_all_weakrefs4caches_

prime_gen
prime_gen__Miller_Rabin_primality_test

is_strong_probable_prime__basis_
    is_strong_probable_prime__basis__with_trial_division_
    is_prime__le_pow2_81_
        prime_filter__using_primality_test_
            raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_
                prev_may_prime__le_pow2_81__lt_
                    reversed_iter_primes__le_pow2_81__lt_
            raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_
                next_may_prime__le_pow2_81__ge_
                    iter_primes__le_pow2_81__ge_
                        iter_pairwise_diff_primes__le_pow2_81__ge_
            iter_primes__ge_lt_         iter_primes__between_
        is_prime__tribool_
            Case4is_prime__tribool_
            detect_strong_probable_prime__not_waste_too_much_time_
            next_probable_prime__ge_
            prev_may_probable_prime__lt_
                reversed_iter_probable_primes__lt_
                iter_probable_primes__ge_
                    iter_pairwise_diff_probable_primes__ge_
            iter_probable_primes__inside_
            iter_probable_primes__ge_lt_   iter_probable_primes__between_



min_prime_factor_gen
    tabulate_may_min_prime_factor4uint_lt_
    tabulate_may_factorization4uint_lt_
        tabulate_may_prime_factorization4uint_lt_
            tabulate_may_pairs8prime_factorization4uint_lt_

all_prime_factors_gen
    tabulate_may_all_prime_factors4uint_lt_
        tabulate_may_all_prime_factor_lflnkls4uint_lt_
        extract_prime_factorization5uint2may_all_prime_factor_lflnkls_












raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_
    raw_list_all_strict_sorted_ints__ge2__with_min_prime_factor__sized_
    raw_iter_all_strict_sorted_primes_
        raw_iter_all_strict_sorted_primes__lt_
            raw_list_all_strict_sorted_primes__lt_
                    list_all_strict_sorted_primes__lt_


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


is_strong_probable_prime__basis_
    is_strong_probable_prime_
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
                is_strong_probable_prime__basis__with_trial_division_
            Case4is_prime__tribool_
            detect_strong_probable_prime__not_waste_too_much_time_
            iter_prime_basis4II_prime_basis_gtN_
                calc_len_prime_basis4II_prime_basis_gtN_
            next_probable_prime__ge_
            prev_may_probable_prime__lt_



GlobalControl4MinPrimeFactorGenerator__Eratosthenes_sieve
    min_prime_factor_gen__Eratosthenes_sieve
        min_prime_factor_gen
        tabulate_may_min_prime_factor4uint_lt_
        tabulate_may_factorization4uint_lt_
            tabulate_may_prime_factorization4uint_lt_
                tabulate_may_pairs8prime_factorization4uint_lt_

GlobalControl4AllPrimeFactorsGenerator__Eratosthenes_sieve
    all_prime_factors_gen__Eratosthenes_sieve
        all_prime_factors_gen
        tabulate_may_all_prime_factors4uint_lt_
            tabulate_may_all_prime_factor_lflnkls4uint_lt_
            extract_prime_factorization5uint2may_all_prime_factor_lflnkls_



mk_tribool_delegate5PRP_test_
is_strong_probable_prime__basis__with_trial_division_
    continuous_trial_division_
        iter_continuous_prime_bases_
    callable5xfilter4continuous_bases
    mk_initial_state4filter4continuous_bases_
        filter4continuous_bases4II_prime_basis_gtN
        filter4continuous_bases4empty
        mk_filter4continuous_bases4fixed_size



pairwise_diff_








is_strong_pseudoprime_
is_strong_pseudoprime__basis__with_trial_division_
is_strong_pseudoprime__basis_
detect_strong_pseudoprime__not_waste_too_much_time_
prev_may_pseudoprime__lt_
next_pseudoprime__ge_
iter_pseudoprimes__ge_lt_
iter_pseudoprimes__inside_
iter_pseudoprimes__between_
iter_pseudoprimes__ge_
reversed_iter_pseudoprimes__lt_
iter_pairwise_diff_pseudoprimes__ge_



TabulateMinPrimeFactor
    find_best_wheel_params4sieve_lt_
    iter_find_best_wheel_paramss4sieve_lt_


list_all_strict_sorted_primes__lt_
    sieve4uint2is_prime__lt_

check_args4core_sieve_interval__ge_le
    core_sieve4primes__ge_le
    core_sieve4offsetted_uint2is_prime__ge_le
    core_sieve4prime_factorization__ge_le
    core_sieve4pairs8prime_factorization__ge_le
    core_sieve4prime_factors__ge_le

check_args4sieve_interval__ge_lt
    calc_min_end5begin6args4sieve_interval_
        test4calc_min_end5begin6args4sieve_interval_
        iter_min_ends5begin6args4sieve_interval_
    sieve_interval4primes__ge_lt
    sieve_interval4offsetted_uint2is_prime__ge_lt
    sieve_interval4prime_factorization__ge_lt
    sieve_interval4prime_factors__ge_lt


to_std_args4core_sieve_interval__ge_le
to_std_args4sieve_interval__ge_lt


check_offsetted_uint2may_prime_factors_
    check_offsetted_uint2prime_factors_
    check_uint2may_prime_factors_

check_offsetted_uint2may_pairs8prime_factorization_
    check_offsetted_uint2pairs8prime_factorization_
    check_uint2may_pairs8prime_factorization_

check_offsetted_uint2may_prime_factorization_
    check_offsetted_uint2prime_factorization_
    check_uint2may_prime_factorization_


tabulate_may_factorization4uint_lt_
tabulate_may_prime_factorization4uint_lt_
    tabulate_may_pairs8prime_factorization4uint_lt_







iter_all_strict_sorted_primes_


iter_primes__inside_
    PrimalityUndeterminedError




'''.split()#'''
__all__

___begin_mark_of_excluded_global_names__0___ = ...

from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__, 'ref:_ref,count:_count'):
    #from operator import __index__
    from weakref import ref as _ref
    from itertools import count as _count
    from itertools import islice, chain

    from seed.iters.apply_may_args4islice_ import list_islice_, show_islice_, stable_show_islice_, stable_list_islice_

    from seed.debug.print_err import print_err
    from seed.tiny_.funcs import snd
    from seed.tiny_.check import check_type_is, check_int_ge



    from seed.types.LazySeq import LazySeq





___end_mark_of_excluded_global_names__0___ = ...





__all__


def __():
  class Error(Exception):
    pass
    r'''[[[
    def __repr__(sf, /):
        return repr_helper(sf, *sf.args)
    #]]]'''#'''

if 1:from seed.math.prime_sieve.sieve_lt import _iter__lt_

from seed.math.prime_sieve.sieve_lt import list_all_strict_sorted_primes__lt_, sieve4uint2is_prime__lt_
from seed.math.prime_sieve.sieve_lt import iter_all_strict_sorted_primes_
from seed.math.prime_sieve.sieve_lt import raw_list_all_strict_sorted_primes__lt_, raw_iter_all_strict_sorted_primes__lt_, raw_iter_all_strict_sorted_primes_, raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_, raw_list_all_strict_sorted_ints__ge2__with_min_prime_factor__sized_

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


class Bool5TriboolFail__probably_prime(PrimalityUndeterminedError):pass








44444; is_strong_pseudoprime_ = is_strong_probable_prime_  # backward_compatible_for_renaming_pseudoprime_as_probable_prime
44444; is_strong_pseudoprime__basis__with_trial_division_ = is_strong_probable_prime__basis__with_trial_division_  # backward_compatible_for_renaming_pseudoprime_as_probable_prime
44444; is_strong_pseudoprime__basis_ = is_strong_probable_prime__basis_  # backward_compatible_for_renaming_pseudoprime_as_probable_prime
44444; detect_strong_pseudoprime__not_waste_too_much_time_ = detect_strong_probable_prime__not_waste_too_much_time_  # backward_compatible_for_renaming_pseudoprime_as_probable_prime
44444; prev_may_pseudoprime__lt_ = prev_may_probable_prime__lt_  # backward_compatible_for_renaming_pseudoprime_as_probable_prime
44444; next_pseudoprime__ge_ = next_probable_prime__ge_  # backward_compatible_for_renaming_pseudoprime_as_probable_prime
44444; iter_pseudoprimes__ge_lt_ = iter_probable_primes__ge_lt_  # backward_compatible_for_renaming_pseudoprime_as_probable_prime
44444; iter_pseudoprimes__inside_ = iter_probable_primes__inside_  # backward_compatible_for_renaming_pseudoprime_as_probable_prime
44444; iter_pseudoprimes__between_ = iter_probable_primes__between_  # backward_compatible_for_renaming_pseudoprime_as_probable_prime
44444; iter_pseudoprimes__ge_ = iter_probable_primes__ge_  # backward_compatible_for_renaming_pseudoprime_as_probable_prime
44444; reversed_iter_pseudoprimes__lt_ = reversed_iter_probable_primes__lt_  # backward_compatible_for_renaming_pseudoprime_as_probable_prime
44444; iter_pairwise_diff_pseudoprimes__ge_ = iter_pairwise_diff_probable_primes__ge_  # backward_compatible_for_renaming_pseudoprime_as_probable_prime

#44444; _kw__is_strong_pseudoprime__basis_ = _kw__is_strong_probable_prime__basis_  # backward_compatible_for_renaming_pseudoprime_as_probable_prime
#44444; _is_strong_pseudoprime_ = _is_strong_probable_prime_  # backward_compatible_for_renaming_pseudoprime_as_probable_prime
#44444; _iter_pseudoprimes__inside_ = _iter_probable_primes__inside_  # backward_compatible_for_renaming_pseudoprime_as_probable_prime

#_kw__is_strong_pseudoprime__basis_
#_is_strong_pseudoprime_
#_iter_pseudoprimes__inside_

is_strong_pseudoprime_
is_strong_pseudoprime__basis_
is_strong_pseudoprime__basis__with_trial_division_
detect_strong_pseudoprime__not_waste_too_much_time_
prev_may_pseudoprime__lt_
next_pseudoprime__ge_
iter_pseudoprimes__ge_lt_
iter_pseudoprimes__inside_
iter_pseudoprimes__between_
iter_pseudoprimes__ge_
reversed_iter_pseudoprimes__lt_
iter_pairwise_diff_pseudoprimes__ge_


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
        def u2ps_(u, /):
            #优化冫复用小对象
            #assert sf() is lazy_seq, (sf(), lazy_seq)
            ps4u = lazy_seq[u]
            #print_err(u, ps4u, sep=':')
            return ps4u

        it = raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_(to_cache_only_busy_primes_plus_next=True, may_primes=None, to_export_all_prime_factors=True, may_uint2all_prime_factors_=u2ps_)
            #bug:why fail to pass u2ps_? bug@LazySeq fixed
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




from seed.math.prime_sieve.sieve_lt import tabulate_may_min_prime_factor4uint_lt_
from seed.math.prime_sieve.sieve_lt import TabulateMinPrimeFactor, iter_find_best_wheel_paramss4sieve_lt_, find_best_wheel_params4sieve_lt_

from seed.math.prime_sieve.sieve_lt import tabulate_may_all_prime_factors4uint_lt_, tabulate_may_all_prime_factor_lflnkls4uint_lt_, extract_prime_factorization5uint2may_all_prime_factor_lflnkls_

from seed.math.prime_sieve.sieve_lt import tabulate_may_pairs8prime_factorization4uint_lt_, tabulate_may_prime_factorization4uint_lt_#deprecated: tabulate_may_factorization4uint_lt_
if 1: from seed.math.prime_sieve.sieve_lt import tabulate_may_factorization4uint_lt_#deprecated





from seed.math.prime_sieve.sieve_ge_le import calc_min_end5begin6args4sieve_interval_, test4calc_min_end5begin6args4sieve_interval_, iter_min_ends5begin6args4sieve_interval_
from seed.math.prime_sieve.sieve_ge_le import check_args4core_sieve_interval__ge_le, check_args4sieve_interval__ge_lt
from seed.math.prime_sieve.sieve_ge_le import to_std_args4core_sieve_interval__ge_le, to_std_args4sieve_interval__ge_lt

from seed.math.prime_sieve.sieve_ge_le import sieve_interval4primes__ge_lt, sieve_interval4offsetted_uint2is_prime__ge_lt, sieve_interval4prime_factorization__ge_lt, sieve_interval4prime_factors__ge_lt

from seed.math.prime_sieve.sieve_ge_le import core_sieve4primes__ge_le, core_sieve4offsetted_uint2is_prime__ge_le, core_sieve4prime_factorization__ge_le, core_sieve4pairs8prime_factorization__ge_le, core_sieve4prime_factors__ge_le





from seed.math.prime_sieve.sieve_lt import check_offsetted_uint2may_prime_factors_, check_offsetted_uint2prime_factors_, check_uint2may_prime_factors_

from seed.math.prime_sieve.sieve_lt import check_offsetted_uint2may_pairs8prime_factorization_, check_offsetted_uint2pairs8prime_factorization_, check_uint2may_pairs8prime_factorization_

from seed.math.prime_sieve.sieve_lt import check_offsetted_uint2may_prime_factorization_, check_offsetted_uint2prime_factorization_, check_uint2may_prime_factorization_





#class

























######################
#@20250419
def _filter4globals_(is_ok_, /):
    nms = []
    xs = []
    for nm, x in sorted(globals().items()):
        if not is_ok_(nm, x):
            continue
        nms.append(nm)
        xs.append(x)
    nms = tuple(nms)
    xs = tuple(xs)
    return (nms, xs)
_IBaseGlobalControl4LazySeq.get_or_mk_lazy_seq_
def _prepare4hold_all_weakrefs4caches_():
    'all:instance:_IBaseGlobalControl4LazySeq'
    def is_ok_(nm, x, /):
        return isinstance(x, _IBaseGlobalControl4LazySeq)
    (nms, xs) = _filter4globals_(is_ok_)
    for x in xs:
        x.get_or_mk_lazy_seq_()
    return (nms, xs)
_data4hold_all_weakrefs4caches_ = _prepare4hold_all_weakrefs4caches_()
assert (__:='\n'.join(_data4hold_all_weakrefs4caches_[0])) == (r'''
all_prime_factors_gen
all_prime_factors_gen__Eratosthenes_sieve
min_prime_factor_gen
min_prime_factor_gen__Eratosthenes_sieve
prime_gen
prime_gen__Eratosthenes_sieve
prime_gen__Miller_Rabin_primality_test
'''.strip()), __
('all_prime_factors_gen', 'all_prime_factors_gen__Eratosthenes_sieve', 'min_prime_factor_gen', 'min_prime_factor_gen__Eratosthenes_sieve', 'prime_gen', 'prime_gen__Eratosthenes_sieve', 'prime_gen__Miller_Rabin_primality_test')
assert (__:=len(_data4hold_all_weakrefs4caches_[0])) == 7, __
#@20250419
def hold_all_weakrefs4caches_():
    '-> tuple<weakref<lazy_seq>> # to replace 『lazy_prime_seq = prime_gen.get_or_mk_lazy_prime_seq_()』' \
    ' # all:instance:_IBaseGlobalControl4LazySeq.get_or_mk_lazy_seq_'
    (nms, xs) = _data4hold_all_weakrefs4caches_
    ws = tuple(x.get_or_mk_lazy_seq_() for x in xs)
    return ws
hold_all_weakrefs4caches_()

def _helper4renaming_probable_prime_():
    r'''[[[
    'helper:rename:pseudoprime --> probable_prime'

@20250419
:%s/^def \(\w*\)pseudoprime\(\w*\)\((.*):\)$/def \1probable_prime\2\3\r44444; \1pseudoprime\2 = \1probable_prime\2  # backward_compatible_for_renaming_pseudoprime_as_probable_prime
    只替换了15个 #预期:16个
        缺失:iter_pseudoprimes__between_

@20250419
:%s/^\(\w*\)pseudoprime\(\w*\) = \(\w*\)pseudoprime\(\w*\)$/\1probable_prime\2 = \3probable_prime\4\r44444; \0  # backward_compatible_for_renaming_pseudoprime_as_probable_prime

    #]]]'''#'''
    def is_ok_(nm, x, /):
        return 'pseudo' in nm
    (nms, xs) = _filter4globals_(is_ok_)
    def is_ok_(nm, x, /):
        return 'pseudoprime' in nm
    (_nms, _xs) = _filter4globals_(is_ok_)
    assert _nms == nms, set(nms)^set(_nms)
    return (nms, xs)
44444; _helper4renaming_pseudoprime_ = _helper4renaming_probable_prime_  # backward_compatible_for_renaming_pseudoprime_as_probable_prime
_data4renaming_pseudoprime_ = _helper4renaming_pseudoprime_()
assert (__:='\n'.join(_data4renaming_pseudoprime_[0])) == (r'''
_helper4renaming_pseudoprime_
detect_strong_pseudoprime__not_waste_too_much_time_
is_strong_pseudoprime_
is_strong_pseudoprime__basis_
is_strong_pseudoprime__basis__with_trial_division_
iter_pairwise_diff_pseudoprimes__ge_
iter_pseudoprimes__between_
iter_pseudoprimes__ge_
iter_pseudoprimes__ge_lt_
iter_pseudoprimes__inside_
next_pseudoprime__ge_
prev_may_pseudoprime__lt_
reversed_iter_pseudoprimes__lt_
'''.strip()), __
#_is_strong_pseudoprime_
#_iter_pseudoprimes__inside_
#_kw__is_strong_pseudoprime__basis_
('_helper4renaming_pseudoprime_', '_is_strong_pseudoprime_', '_iter_pseudoprimes__inside_', '_kw__is_strong_pseudoprime__basis_', 'detect_strong_pseudoprime__not_waste_too_much_time_', 'is_strong_pseudoprime_', 'is_strong_pseudoprime__basis_', 'is_strong_pseudoprime__basis__with_trial_division_', 'iter_pairwise_diff_pseudoprimes__ge_', 'iter_pseudoprimes__between_', 'iter_pseudoprimes__ge_', 'iter_pseudoprimes__ge_lt_', 'iter_pseudoprimes__inside_', 'next_pseudoprime__ge_', 'prev_may_pseudoprime__lt_', 'reversed_iter_pseudoprimes__lt_')
assert (__:=len(_data4renaming_pseudoprime_[0])) == 16-3, __
######################
























if __name__ == "__main__":
    pass




#重命名前:
#.__all__
#.
#.
#.from seed.math.prime_gens import hold_all_weakrefs4caches_
#.from seed.math.prime_gens import detect_strong_pseudoprime__not_waste_too_much_time_
#.
#.from seed.math.prime_gens import all_prime_factors_gen, tabulate_may_all_prime_factors4uint_lt_
#.
#.from seed.math.prime_gens import min_prime_factor_gen, tabulate_may_min_prime_factor4uint_lt_, tabulate_may_factorization4uint_lt_
#.
#.
#.
#.from seed.math.prime_gens import prime_gen__Eratosthenes_sieve, prime_gen__Miller_Rabin_primality_test
#.
#.from seed.math.prime_gens import prime_gen, prime_filter__using_primality_test_, raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_
#.
#.from seed.math.prime_gens import is_strong_pseudoprime__basis_, is_prime__using_A014233_, is_prime__le_pow2_81_, is_prime__tribool_, Case4is_prime__tribool_
#.
#.from seed.math.prime_gens import is_prime__le_pow2_81_, next_pseudoprime__ge_, prev_may_pseudoprime__lt_, next_may_prime__le_pow2_81__ge_, prev_may_prime__le_pow2_81__lt_, raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_, raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_
#.
#.from seed.math.prime_gens import iter_pseudoprimes__ge_, reversed_iter_pseudoprimes__lt_, iter_primes__le_pow2_81__ge_, reversed_iter_primes__le_pow2_81__lt_
#.from seed.math.prime_gens import iter_pairwise_diff_pseudoprimes__ge_, iter_pairwise_diff_primes__le_pow2_81__ge_
#.
#.#######
#.from seed.math.prime_gens import iter_pseudoprimes__inside_, iter_pseudoprimes__ge_lt_# iter_pseudoprimes__between_
#.from seed.math.prime_gens import prev_may_pseudoprime__lt_, next_pseudoprime__ge_, reversed_iter_pseudoprimes__lt_, iter_pseudoprimes__ge_
#.from seed.math.prime_gens import prev_may_prime__le_pow2_81__lt_, next_may_prime__le_pow2_81__ge_, reversed_iter_primes__le_pow2_81__lt_, iter_primes__le_pow2_81__ge_
#.#######
#.
#.from seed.math.prime_gens import is_strong_pseudoprime__basis__with_trial_division_, continuous_trial_division_, iter_continuous_prime_bases_, callable5xfilter4continuous_bases, mk_initial_state4filter4continuous_bases_, filter4continuous_bases4II_prime_basis_gtN, filter4continuous_bases4empty, mk_filter4continuous_bases4fixed_size
#.    # @20250130
#.from seed.math.prime_gens import mk_tribool_delegate5PRP_test_, is_strong_pseudoprime__basis__with_trial_division_
#.    # @20250131
#.
#.


r'''[[[
后续:_helper4renaming_pseudoprime_()

@20250419
:.+1,$s/pseudoprime/probable_prime/g
    #替换16次/9行
#]]]'''#'''

#重命名后:
__all__

from seed.math.prime_gens import hold_all_weakrefs4caches_
#000;    __ws = hold_all_weakrefs4caches_()
from seed.math.prime_gens import detect_strong_probable_prime__not_waste_too_much_time_

from seed.math.prime_gens import all_prime_factors_gen, tabulate_may_all_prime_factors4uint_lt_, tabulate_may_all_prime_factor_lflnkls4uint_lt_, extract_prime_factorization5uint2may_all_prime_factor_lflnkls_

from seed.math.prime_gens import min_prime_factor_gen, tabulate_may_min_prime_factor4uint_lt_, TabulateMinPrimeFactor, tabulate_may_prime_factorization4uint_lt_, tabulate_may_pairs8prime_factorization4uint_lt_
if 1:from seed.math.prime_gens import tabulate_may_factorization4uint_lt_#deprecated



from seed.math.prime_gens import prime_gen__Eratosthenes_sieve, prime_gen__Miller_Rabin_primality_test

from seed.math.prime_gens import prime_gen, prime_filter__using_primality_test_, raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_

from seed.math.prime_gens import is_strong_probable_prime__basis_, is_prime__using_A014233_, is_prime__le_pow2_81_, is_prime__tribool_, Case4is_prime__tribool_

from seed.math.prime_gens import is_prime__le_pow2_81_, next_probable_prime__ge_, prev_may_probable_prime__lt_, next_may_prime__le_pow2_81__ge_, prev_may_prime__le_pow2_81__lt_, raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__ge_, raw_iter_all_strict_sorted_primes__using_primality_test__le_pow2_81__lt_

from seed.math.prime_gens import iter_probable_primes__ge_, reversed_iter_probable_primes__lt_, iter_primes__le_pow2_81__ge_, reversed_iter_primes__le_pow2_81__lt_
from seed.math.prime_gens import iter_pairwise_diff_probable_primes__ge_, iter_pairwise_diff_primes__le_pow2_81__ge_

#######
from seed.math.prime_gens import iter_probable_primes__inside_, iter_probable_primes__ge_lt_# iter_probable_primes__between_
from seed.math.prime_gens import prev_may_probable_prime__lt_, next_probable_prime__ge_, reversed_iter_probable_primes__lt_, iter_probable_primes__ge_
from seed.math.prime_gens import prev_may_prime__le_pow2_81__lt_, next_may_prime__le_pow2_81__ge_, reversed_iter_primes__le_pow2_81__lt_, iter_primes__le_pow2_81__ge_
#######

from seed.math.prime_gens import is_strong_probable_prime__basis__with_trial_division_, continuous_trial_division_, iter_continuous_prime_bases_, callable5xfilter4continuous_bases, mk_initial_state4filter4continuous_bases_, filter4continuous_bases4II_prime_basis_gtN, filter4continuous_bases4empty, mk_filter4continuous_bases4fixed_size
    # @20250130
from seed.math.prime_gens import mk_tribool_delegate5PRP_test_, is_strong_probable_prime__basis__with_trial_division_
    # @20250131

from seed.math.prime_gens import sieve4uint2is_prime__lt_, list_all_strict_sorted_primes__lt_
    # @20260511
    #vs:raw_list_all_strict_sorted_primes__lt_
    #vs:tabulate_may_min_prime_factor4uint_lt_


# @20260511
from seed.math.prime_gens import (
check_args4core_sieve_interval__ge_le
,   core_sieve4primes__ge_le
,   core_sieve4offsetted_uint2is_prime__ge_le
,   core_sieve4prime_factorization__ge_le
,   core_sieve4pairs8prime_factorization__ge_le
,   core_sieve4prime_factors__ge_le
)

# @20260511
from seed.math.prime_gens import (
check_args4sieve_interval__ge_lt
,   calc_min_end5begin6args4sieve_interval_
,       test4calc_min_end5begin6args4sieve_interval_
,       iter_min_ends5begin6args4sieve_interval_
,   sieve_interval4primes__ge_lt
,   sieve_interval4offsetted_uint2is_prime__ge_lt
,   sieve_interval4prime_factorization__ge_lt
,   sieve_interval4prime_factors__ge_lt
)

r'''[[[
TODO:
e ../../python3_src/seed/math/primality_test/Jacobi_sums_test/selection_of_auxiliary_numbers.py
    TODO:list_best_Ts_le__ver3_ using:
        sieve_interval4prime_factorization__ge_lt
        or:
        sieve_interval4prime_factors__ge_lt

]]]'''#'''

from seed.math.prime_gens import *
