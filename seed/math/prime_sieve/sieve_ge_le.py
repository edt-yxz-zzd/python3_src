#__all__:goto
r'''[[[
e ../../python3_src/seed/math/prime_sieve/sieve_ge_le.py

seed.math.prime_sieve.sieve_ge_le
py -m nn_ns.app.debug_cmd   seed.math.prime_sieve.sieve_ge_le -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.prime_sieve.sieve_ge_le:__doc__ -ht # -ff -df
#######

[[
move_from:
e ../../python3_src/seed/math/prime_gens.py
]]


'#'; __doc__ = r'#'
>>> [*map(calc_best_end5begin6args4sieve_interval_, range(40))]
[9, 9, 9, 9, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81]
>>> [*enumerate(map(calc_best_end5begin6args4sieve_interval_, range(40)))]  #doctest: +SKIP
>>> calc_best_end5begin6args4sieve_interval_(10**8)
100040004
>>> calc_best_end5begin6args4sieve_interval_(calc_best_end5begin6args4sieve_interval_(10**8))
100100025


>>> [*map(calc_best_begin5end6args4sieve_interval_, range(40))]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
>>> [*enumerate(map(calc_best_begin5end6args4sieve_interval_, range(40)))]  #doctest: +SKIP
>>> calc_best_begin5end6args4sieve_interval_(10**8)
99920016
>>> calc_best_begin5end6args4sieve_interval_(calc_best_begin5end6args4sieve_interval_(10**8))
99860049


[[
py_adhoc_call   seed.math.prime_sieve.sieve_ge_le   @list.20:iter_best_ends5begin6args4sieve_interval_ =0
    [9, 36, 81, 144, 225, 324, 441, 576, 729, 900, 1089, 1296, 1521, 1764, 2025, 2304, 2601, 2916, 3249, 3600]
    #ver2:[12, 39, 84, 147, 228, 327, 444, 579, 732, 903, 1092, 1299, 1524, 1767, 2028, 2307, 2604, 2919, 3252, 3603]
py_adhoc_call   seed.math.prime_sieve.sieve_ge_le   @list.iter_best_begins5end6args4sieve_interval_ =3603
    [3249, 2916, 2601, 2304, 2025, 1764, 1521, 1296, 1089, 900, 729, 576, 441, 324, 225, 144, 81, 36, 9, 0]
]]


>>> from itertools import islice

check_args4core_sieve_interval__ge_le
check_args4sieve_interval__ge_lt

to_std_args4core_sieve_interval__ge_le
to_std_args4sieve_interval__ge_lt

>>> to_std_args4core_sieve_interval__ge_le(10, ...)
(10, 13)
>>> to_std_args4core_sieve_interval__ge_le('!!!', '...') # ok:[not emay_max_u is ...]
('!!!', '...')
>>> to_std_args4core_sieve_interval__ge_le(0, ...) # ok:[min_u < 10]
(0, 1)

>>> to_std_args4sieve_interval__ge_lt(10, ...)
(10, 14)
>>> to_std_args4sieve_interval__ge_lt(-1, '...') # ok:[not emay_max1_u is ...]
(0, '...')
>>> to_std_args4sieve_interval__ge_lt(-1, ...) # ok:[min_u < 10]
(0, 2)

>>> check_args4core_sieve_interval__ge_le(10, 13)
>>> check_args4core_sieve_interval__ge_le(10, 99)
>>> check_args4core_sieve_interval__ge_le(10, 12)
Traceback (most recent call last):
    ...
TypeError: (10, 12)
>>> check_args4core_sieve_interval__ge_le(10, 100)
Traceback (most recent call last):
    ...
TypeError: 100
>>> check_args4core_sieve_interval__ge_le(9, 20)
Traceback (most recent call last):
    ...
TypeError: 9
>>> check_args4core_sieve_interval__ge_le(2, 3) # [2 < 10]
Traceback (most recent call last):
    ...
TypeError: 2

>>> check_args4sieve_interval__ge_lt(10, 14)
>>> check_args4sieve_interval__ge_lt(10, 10000)
>>> check_args4sieve_interval__ge_lt(10, 13)
Traceback (most recent call last):
    ...
TypeError: (10, 13)
>>> check_args4sieve_interval__ge_lt(0, 1)
>>> check_args4sieve_interval__ge_lt(0, 0)
>>> check_args4sieve_interval__ge_lt(0, -1)
Traceback (most recent call last):
    ...
TypeError: -1
>>> check_args4sieve_interval__ge_lt(1, 1)
Traceback (most recent call last):
    ...
TypeError: (1, 1)
>>> check_args4sieve_interval__ge_lt(1, 2)
>>> check_args4sieve_interval__ge_lt(2, 4)
>>> check_args4sieve_interval__ge_lt(2, 3) # !!!!!!!not assume prime ...!!!!!!!
Traceback (most recent call last):
    ...
TypeError: (2, 3)


calc_min_end5begin6args4sieve_interval_
    test4calc_min_end5begin6args4sieve_interval_
    iter_min_ends5begin6args4sieve_interval_
>>> calc_min_end5begin6args4sieve_interval_(10)
14
>>> calc_min_end5begin6args4sieve_interval_(1)
2
>>> calc_min_end5begin6args4sieve_interval_(0)
2
>>> calc_min_end5begin6args4sieve_interval_(-1)
2
>>> calc_min_end5begin6args4sieve_interval_(-999)
2
>>> test4calc_min_end5begin6args4sieve_interval_([-1])
Traceback (most recent call last):
    ...
AssertionError: (-1, 1)
>>> test4calc_min_end5begin6args4sieve_interval_([9])
>>> test4calc_min_end5begin6args4sieve_interval_([10, 10000])
>>> [*islice(iter_min_ends5begin6args4sieve_interval_(10), 10)]
[14, 19, 24, 30, 36, 43, 50, 58, 67, 76]


iter_best_interval5big_interval6args4sieve_interval_
    calc_best_begin5end6args4sieve_interval_
        iter_best_begins5end6args4sieve_interval_
    calc_best_end5begin6args4sieve_interval_
        iter_best_ends5begin6args4sieve_interval_
>>> calc_best_end5begin6args4sieve_interval_(10)
36
>>> calc_best_end5begin6args4sieve_interval_(0)
9
>>> calc_best_end5begin6args4sieve_interval_(-999)
9

>>> calc_best_begin5end6args4sieve_interval_(50)
36
>>> calc_best_begin5end6args4sieve_interval_(49)
9
>>> calc_best_begin5end6args4sieve_interval_(36)
9
>>> calc_best_begin5end6args4sieve_interval_(17)
9
>>> calc_best_begin5end6args4sieve_interval_(16)
0
>>> calc_best_begin5end6args4sieve_interval_(10)
0
>>> calc_best_begin5end6args4sieve_interval_(0)
0
>>> calc_best_begin5end6args4sieve_interval_(-999)
0

def iter_best_interval5big_interval6args4sieve_interval_(min_u7whole, may_max1_u7whole, /, *, reverse=False, validate=True):
>>> [*islice(iter_best_ends5begin6args4sieve_interval_(0), 10)]
[9, 36, 81, 144, 225, 324, 441, 576, 729, 900]
>>> [*islice(iter_best_begins5end6args4sieve_interval_(10000), 10)]
[9216, 8649, 8100, 7569, 7056, 6561, 6084, 5625, 5184, 4761]
>>> [*iter_best_interval5big_interval6args4sieve_interval_(0, 10000)]
[(0, 9), (9, 36), (36, 81), (81, 144), (144, 225), (225, 324), (324, 441), (441, 576), (576, 729), (729, 900), (900, 1089), (1089, 1296), (1296, 1521), (1521, 1764), (1764, 2025), (2025, 2304), (2304, 2601), (2601, 2916), (2916, 3249), (3249, 3600), (3600, 3969), (3969, 4356), (4356, 4761), (4761, 5184), (5184, 5625), (5625, 6084), (6084, 6561), (6561, 7056), (7056, 7569), (7569, 8100), (8100, 8649), (8649, 9216), (9216, 10000)]
>>> [*iter_best_interval5big_interval6args4sieve_interval_(0, 10000, reverse=True)]
[(9216, 10000), (8649, 9216), (8100, 8649), (7569, 8100), (7056, 7569), (6561, 7056), (6084, 6561), (5625, 6084), (5184, 5625), (4761, 5184), (4356, 4761), (3969, 4356), (3600, 3969), (3249, 3600), (2916, 3249), (2601, 2916), (2304, 2601), (2025, 2304), (1764, 2025), (1521, 1764), (1296, 1521), (1089, 1296), (900, 1089), (729, 900), (576, 729), (441, 576), (324, 441), (225, 324), (144, 225), (81, 144), (36, 81), (9, 36), (0, 9)]
>>> [*islice(iter_best_interval5big_interval6args4sieve_interval_(0, None), 9)]
[(0, 9), (9, 36), (36, 81), (81, 144), (144, 225), (225, 324), (324, 441), (441, 576), (576, 729)]
>>> [*islice(iter_best_interval5big_interval6args4sieve_interval_(0, None, reverse=True), 9)]
Traceback (most recent call last):
    ...
TypeError: reverse and None is may_max1_u7whole








core_sieve4primes__ge_le
core_sieve4offsetted_uint2is_prime__ge_le
core_sieve4prime_factorization__ge_le
core_sieve4pairs8prime_factorization__ge_le
core_sieve4prime_factors__ge_le


>>> core_sieve4primes__ge_le(10, ...)
(11, 13)
>>> core_sieve4primes__ge_le(10, 13)
(11, 13)
>>> core_sieve4primes__ge_le(10, 99)
(11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
>>> core_sieve4primes__ge_le(10, ..., _mk=list)
[11, 13]

>>> core_sieve4offsetted_uint2is_prime__ge_le(10, ...)
[False, True, False, True]
>>> core_sieve4offsetted_uint2is_prime__ge_le(10, 13)
[False, True, False, True]
>>> core_sieve4offsetted_uint2is_prime__ge_le(10, 99)
[False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False]

>>> core_sieve4prime_factors__ge_le(10, ...)
[(2, 5), (11,), (2, 3), (13,)]
>>> core_sieve4prime_factors__ge_le(10, 13)
[(2, 5), (11,), (2, 3), (13,)]
>>> core_sieve4prime_factors__ge_le(10, 99)
[(2, 5), (11,), (2, 3), (13,), (2, 7), (3, 5), (2,), (17,), (2, 3), (19,), (2, 5), (3, 7), (2, 11), (23,), (2, 3), (5,), (2, 13), (3,), (2, 7), (29,), (2, 3, 5), (31,), (2,), (3, 11), (2, 17), (5, 7), (2, 3), (37,), (2, 19), (3, 13), (2, 5), (41,), (2, 3, 7), (43,), (2, 11), (3, 5), (2, 23), (47,), (2, 3), (7,), (2, 5), (3, 17), (2, 13), (53,), (2, 3), (5, 11), (2, 7), (3, 19), (2, 29), (59,), (2, 3, 5), (61,), (2, 31), (3, 7), (2,), (5, 13), (2, 3, 11), (67,), (2, 17), (3, 23), (2, 5, 7), (71,), (2, 3), (73,), (2, 37), (3, 5), (2, 19), (7, 11), (2, 3, 13), (79,), (2, 5), (3,), (2, 41), (83,), (2, 3, 7), (5, 17), (2, 43), (3, 29), (2, 11), (89,), (2, 3, 5), (7, 13), (2, 23), (3, 31), (2, 47), (5, 19), (2, 3), (97,), (2, 7), (3, 11)]


>>> core_sieve4pairs8prime_factorization__ge_le(10, ...)
[((2, 1), (5, 1)), ((11, 1),), ((2, 2), (3, 1)), ((13, 1),)]
>>> core_sieve4pairs8prime_factorization__ge_le(10, 13)
[((2, 1), (5, 1)), ((11, 1),), ((2, 2), (3, 1)), ((13, 1),)]
>>> core_sieve4pairs8prime_factorization__ge_le(10, 99)
[((2, 1), (5, 1)), ((11, 1),), ((2, 2), (3, 1)), ((13, 1),), ((2, 1), (7, 1)), ((3, 1), (5, 1)), ((2, 4),), ((17, 1),), ((2, 1), (3, 2)), ((19, 1),), ((2, 2), (5, 1)), ((3, 1), (7, 1)), ((2, 1), (11, 1)), ((23, 1),), ((2, 3), (3, 1)), ((5, 2),), ((2, 1), (13, 1)), ((3, 3),), ((2, 2), (7, 1)), ((29, 1),), ((2, 1), (3, 1), (5, 1)), ((31, 1),), ((2, 5),), ((3, 1), (11, 1)), ((2, 1), (17, 1)), ((5, 1), (7, 1)), ((2, 2), (3, 2)), ((37, 1),), ((2, 1), (19, 1)), ((3, 1), (13, 1)), ((2, 3), (5, 1)), ((41, 1),), ((2, 1), (3, 1), (7, 1)), ((43, 1),), ((2, 2), (11, 1)), ((3, 2), (5, 1)), ((2, 1), (23, 1)), ((47, 1),), ((2, 4), (3, 1)), ((7, 2),), ((2, 1), (5, 2)), ((3, 1), (17, 1)), ((2, 2), (13, 1)), ((53, 1),), ((2, 1), (3, 3)), ((5, 1), (11, 1)), ((2, 3), (7, 1)), ((3, 1), (19, 1)), ((2, 1), (29, 1)), ((59, 1),), ((2, 2), (3, 1), (5, 1)), ((61, 1),), ((2, 1), (31, 1)), ((3, 2), (7, 1)), ((2, 6),), ((5, 1), (13, 1)), ((2, 1), (3, 1), (11, 1)), ((67, 1),), ((2, 2), (17, 1)), ((3, 1), (23, 1)), ((2, 1), (5, 1), (7, 1)), ((71, 1),), ((2, 3), (3, 2)), ((73, 1),), ((2, 1), (37, 1)), ((3, 1), (5, 2)), ((2, 2), (19, 1)), ((7, 1), (11, 1)), ((2, 1), (3, 1), (13, 1)), ((79, 1),), ((2, 4), (5, 1)), ((3, 4),), ((2, 1), (41, 1)), ((83, 1),), ((2, 2), (3, 1), (7, 1)), ((5, 1), (17, 1)), ((2, 1), (43, 1)), ((3, 1), (29, 1)), ((2, 3), (11, 1)), ((89, 1),), ((2, 1), (3, 2), (5, 1)), ((7, 1), (13, 1)), ((2, 2), (23, 1)), ((3, 1), (31, 1)), ((2, 1), (47, 1)), ((5, 1), (19, 1)), ((2, 5), (3, 1)), ((97, 1),), ((2, 1), (7, 2)), ((3, 2), (11, 1))]

>>> core_sieve4prime_factorization__ge_le(10, ...)
[{2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}]
>>> core_sieve4prime_factorization__ge_le(10, 13)
[{2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}]
>>> core_sieve4prime_factorization__ge_le(10, 99)
[{2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}, {2: 1, 7: 1}, {3: 1, 5: 1}, {2: 4}, {17: 1}, {2: 1, 3: 2}, {19: 1}, {2: 2, 5: 1}, {3: 1, 7: 1}, {2: 1, 11: 1}, {23: 1}, {2: 3, 3: 1}, {5: 2}, {2: 1, 13: 1}, {3: 3}, {2: 2, 7: 1}, {29: 1}, {2: 1, 3: 1, 5: 1}, {31: 1}, {2: 5}, {3: 1, 11: 1}, {2: 1, 17: 1}, {5: 1, 7: 1}, {2: 2, 3: 2}, {37: 1}, {2: 1, 19: 1}, {3: 1, 13: 1}, {2: 3, 5: 1}, {41: 1}, {2: 1, 3: 1, 7: 1}, {43: 1}, {2: 2, 11: 1}, {3: 2, 5: 1}, {2: 1, 23: 1}, {47: 1}, {2: 4, 3: 1}, {7: 2}, {2: 1, 5: 2}, {3: 1, 17: 1}, {2: 2, 13: 1}, {53: 1}, {2: 1, 3: 3}, {5: 1, 11: 1}, {2: 3, 7: 1}, {3: 1, 19: 1}, {2: 1, 29: 1}, {59: 1}, {2: 2, 3: 1, 5: 1}, {61: 1}, {2: 1, 31: 1}, {3: 2, 7: 1}, {2: 6}, {5: 1, 13: 1}, {2: 1, 3: 1, 11: 1}, {67: 1}, {2: 2, 17: 1}, {3: 1, 23: 1}, {2: 1, 5: 1, 7: 1}, {71: 1}, {2: 3, 3: 2}, {73: 1}, {2: 1, 37: 1}, {3: 1, 5: 2}, {2: 2, 19: 1}, {7: 1, 11: 1}, {2: 1, 3: 1, 13: 1}, {79: 1}, {2: 4, 5: 1}, {3: 4}, {2: 1, 41: 1}, {83: 1}, {2: 2, 3: 1, 7: 1}, {5: 1, 17: 1}, {2: 1, 43: 1}, {3: 1, 29: 1}, {2: 3, 11: 1}, {89: 1}, {2: 1, 3: 2, 5: 1}, {7: 1, 13: 1}, {2: 2, 23: 1}, {3: 1, 31: 1}, {2: 1, 47: 1}, {5: 1, 19: 1}, {2: 5, 3: 1}, {97: 1}, {2: 1, 7: 2}, {3: 2, 11: 1}]





sieve_interval4primes__ge_lt
sieve_interval4offsetted_uint2is_prime__ge_lt
sieve_interval4prime_factorization__ge_lt
sieve_interval4prime_factors__ge_lt

>>> sieve_interval4primes__ge_lt(0, 20)
[2, 3, 5, 7, 11, 13, 17, 19]
>>> sieve_interval4primes__ge_lt(9, 12)
Traceback (most recent call last):
    ...
TypeError: (9, 12)
>>> sieve_interval4primes__ge_lt(9, 13)
[11]
>>> sieve_interval4primes__ge_lt(10, 14)
[11, 13]


>>> sieve_interval4offsetted_uint2is_prime__ge_lt(0, 20)
[False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]
>>> sieve_interval4offsetted_uint2is_prime__ge_lt(10, 20)
[False, True, False, True, False, False, False, True, False, True]

>>> sieve_interval4prime_factors__ge_lt(0, 20)
[None, (), (2,), (3,), (2,), (5,), (2, 3), (7,), (2,), (3,), (2, 5), (11,), (2, 3), (13,), (2, 7), (3, 5), (2,), (17,), (2, 3), (19,)]
>>> sieve_interval4prime_factors__ge_lt(10, 20)
[(2, 5), (11,), (2, 3), (13,), (2, 7), (3, 5), (2,), (17,), (2, 3), (19,)]

>>> sieve_interval4prime_factorization__ge_lt(0, 20)
[None, {}, {2: 1}, {3: 1}, {2: 2}, {5: 1}, {2: 1, 3: 1}, {7: 1}, {2: 3}, {3: 2}, {2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}, {2: 1, 7: 1}, {3: 1, 5: 1}, {2: 4}, {17: 1}, {2: 1, 3: 2}, {19: 1}]
>>> sieve_interval4prime_factorization__ge_lt(10, 20)
[{2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}, {2: 1, 7: 1}, {3: 1, 5: 1}, {2: 4}, {17: 1}, {2: 1, 3: 2}, {19: 1}]









iter_sieve4prime_chunks_ge_lt_
    iter_sieve4prime_chunks_ge_
    reverse_iter_sieve4prime_chunks_lt_
    iter_sieve4primes_ge_lt_
        iter_sieve4primes_ge_
        reverse_iter_sieve4primes_lt_
def iter_sieve4prime_chunks_ge_lt_(min_u7whole, may_max1_u7whole, /, *, with_interval=False, reverse=False):
def iter_sieve4primes_ge_lt_(min_u7whole, may_max1_u7whole, /, *, reverse=False):
>>> [*iter_sieve4prime_chunks_ge_lt_(0, 100)]
[[2, 3, 5, 7], [11, 13, 17, 19, 23, 29, 31], [37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]]
>>> [*iter_sieve4prime_chunks_ge_lt_(0, 100, with_interval=True)]
[((0, 9), [2, 3, 5, 7]), ((9, 36), [11, 13, 17, 19, 23, 29, 31]), ((36, 100), [37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])]
>>> [*iter_sieve4prime_chunks_ge_lt_(0, 100, reverse=True)]
[[37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97], [11, 13, 17, 19, 23, 29, 31], [2, 3, 5, 7]]
>>> [*islice(iter_sieve4prime_chunks_ge_lt_(0, None), 3)]
[[2, 3, 5, 7], [11, 13, 17, 19, 23, 29, 31], [37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]]
>>> [*islice(iter_sieve4prime_chunks_ge_lt_(0, None, with_interval=True), 3)]
[((0, 9), [2, 3, 5, 7]), ((9, 36), [11, 13, 17, 19, 23, 29, 31]), ((36, 81), [37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79])]
>>> [*islice(iter_sieve4prime_chunks_ge_lt_(0, None, reverse=True), 3)]
Traceback (most recent call last):
    ...
TypeError: reverse and None is may_max1_u7whole

>>> [*islice(iter_sieve4prime_chunks_ge_(14, with_interval=True), 2)]
[((14, 36), [17, 19, 23, 29, 31]), ((36, 81), [37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79])]
>>> [*reverse_iter_sieve4prime_chunks_lt_(42, with_interval=True)]
[((9, 42), [11, 13, 17, 19, 23, 29, 31, 37, 41]), ((0, 9), [2, 3, 5, 7])]
>>> [*islice(iter_sieve4primes_ge_lt_(0, None), 16)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
>>> [*iter_sieve4primes_ge_lt_(0, 42)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
>>> [*iter_sieve4primes_ge_lt_(0, 42, reverse=True)]
[41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]
>>> [*islice(iter_sieve4primes_ge_(244), 16)]
[251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347]
>>> [*islice(reverse_iter_sieve4primes_lt_(244), 16)]
[241, 239, 233, 229, 227, 223, 211, 199, 197, 193, 191, 181, 179, 173, 167, 163]
>>> [*reverse_iter_sieve4primes_lt_(42)]
[41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]

>>> [*iter_sieve4primes_ge_lt_(2, 3)]
[2]

Traceback (most recent call last):
    ...
TypeError: (2, 3)



iter_sieve4prime_factors_chunks_ge_lt_
    iter_sieve4prime_factors_chunks_ge_
    reverse_iter_sieve4prime_factors_chunks_lt_
    iter_sieve4prime_factorss_ge_lt_
        iter_sieve4prime_factorss_ge_
        reverse_iter_sieve4prime_factorss_lt_
def iter_sieve4prime_factors_chunks_ge_lt_(min_u7whole, may_max1_u7whole, /, *, with_interval=False, reverse=False):
>>> [*iter_sieve4prime_factors_chunks_ge_lt_(0, 100)]
[[None, (), (2,), (3,), (2,), (5,), (2, 3), (7,), (2,)], [(3,), (2, 5), (11,), (2, 3), (13,), (2, 7), (3, 5), (2,), (17,), (2, 3), (19,), (2, 5), (3, 7), (2, 11), (23,), (2, 3), (5,), (2, 13), (3,), (2, 7), (29,), (2, 3, 5), (31,), (2,), (3, 11), (2, 17), (5, 7)], [(2, 3), (37,), (2, 19), (3, 13), (2, 5), (41,), (2, 3, 7), (43,), (2, 11), (3, 5), (2, 23), (47,), (2, 3), (7,), (2, 5), (3, 17), (2, 13), (53,), (2, 3), (5, 11), (2, 7), (3, 19), (2, 29), (59,), (2, 3, 5), (61,), (2, 31), (3, 7), (2,), (5, 13), (2, 3, 11), (67,), (2, 17), (3, 23), (2, 5, 7), (71,), (2, 3), (73,), (2, 37), (3, 5), (2, 19), (7, 11), (2, 3, 13), (79,), (2, 5), (3,), (2, 41), (83,), (2, 3, 7), (5, 17), (2, 43), (3, 29), (2, 11), (89,), (2, 3, 5), (7, 13), (2, 23), (3, 31), (2, 47), (5, 19), (2, 3), (97,), (2, 7), (3, 11)]]
>>> [*iter_sieve4prime_factors_chunks_ge_lt_(0, 100, with_interval=True)]
[((0, 9), [None, (), (2,), (3,), (2,), (5,), (2, 3), (7,), (2,)]), ((9, 36), [(3,), (2, 5), (11,), (2, 3), (13,), (2, 7), (3, 5), (2,), (17,), (2, 3), (19,), (2, 5), (3, 7), (2, 11), (23,), (2, 3), (5,), (2, 13), (3,), (2, 7), (29,), (2, 3, 5), (31,), (2,), (3, 11), (2, 17), (5, 7)]), ((36, 100), [(2, 3), (37,), (2, 19), (3, 13), (2, 5), (41,), (2, 3, 7), (43,), (2, 11), (3, 5), (2, 23), (47,), (2, 3), (7,), (2, 5), (3, 17), (2, 13), (53,), (2, 3), (5, 11), (2, 7), (3, 19), (2, 29), (59,), (2, 3, 5), (61,), (2, 31), (3, 7), (2,), (5, 13), (2, 3, 11), (67,), (2, 17), (3, 23), (2, 5, 7), (71,), (2, 3), (73,), (2, 37), (3, 5), (2, 19), (7, 11), (2, 3, 13), (79,), (2, 5), (3,), (2, 41), (83,), (2, 3, 7), (5, 17), (2, 43), (3, 29), (2, 11), (89,), (2, 3, 5), (7, 13), (2, 23), (3, 31), (2, 47), (5, 19), (2, 3), (97,), (2, 7), (3, 11)])]
>>> [*iter_sieve4prime_factors_chunks_ge_lt_(0, 100, reverse=True)]
[[(2, 3), (37,), (2, 19), (3, 13), (2, 5), (41,), (2, 3, 7), (43,), (2, 11), (3, 5), (2, 23), (47,), (2, 3), (7,), (2, 5), (3, 17), (2, 13), (53,), (2, 3), (5, 11), (2, 7), (3, 19), (2, 29), (59,), (2, 3, 5), (61,), (2, 31), (3, 7), (2,), (5, 13), (2, 3, 11), (67,), (2, 17), (3, 23), (2, 5, 7), (71,), (2, 3), (73,), (2, 37), (3, 5), (2, 19), (7, 11), (2, 3, 13), (79,), (2, 5), (3,), (2, 41), (83,), (2, 3, 7), (5, 17), (2, 43), (3, 29), (2, 11), (89,), (2, 3, 5), (7, 13), (2, 23), (3, 31), (2, 47), (5, 19), (2, 3), (97,), (2, 7), (3, 11)], [(3,), (2, 5), (11,), (2, 3), (13,), (2, 7), (3, 5), (2,), (17,), (2, 3), (19,), (2, 5), (3, 7), (2, 11), (23,), (2, 3), (5,), (2, 13), (3,), (2, 7), (29,), (2, 3, 5), (31,), (2,), (3, 11), (2, 17), (5, 7)], [None, (), (2,), (3,), (2,), (5,), (2, 3), (7,), (2,)]]
>>> [*islice(iter_sieve4prime_factors_chunks_ge_lt_(0, None), 3)]
[[None, (), (2,), (3,), (2,), (5,), (2, 3), (7,), (2,)], [(3,), (2, 5), (11,), (2, 3), (13,), (2, 7), (3, 5), (2,), (17,), (2, 3), (19,), (2, 5), (3, 7), (2, 11), (23,), (2, 3), (5,), (2, 13), (3,), (2, 7), (29,), (2, 3, 5), (31,), (2,), (3, 11), (2, 17), (5, 7)], [(2, 3), (37,), (2, 19), (3, 13), (2, 5), (41,), (2, 3, 7), (43,), (2, 11), (3, 5), (2, 23), (47,), (2, 3), (7,), (2, 5), (3, 17), (2, 13), (53,), (2, 3), (5, 11), (2, 7), (3, 19), (2, 29), (59,), (2, 3, 5), (61,), (2, 31), (3, 7), (2,), (5, 13), (2, 3, 11), (67,), (2, 17), (3, 23), (2, 5, 7), (71,), (2, 3), (73,), (2, 37), (3, 5), (2, 19), (7, 11), (2, 3, 13), (79,), (2, 5)]]
>>> [*islice(iter_sieve4prime_factors_chunks_ge_lt_(0, None, with_interval=True), 3)]
[((0, 9), [None, (), (2,), (3,), (2,), (5,), (2, 3), (7,), (2,)]), ((9, 36), [(3,), (2, 5), (11,), (2, 3), (13,), (2, 7), (3, 5), (2,), (17,), (2, 3), (19,), (2, 5), (3, 7), (2, 11), (23,), (2, 3), (5,), (2, 13), (3,), (2, 7), (29,), (2, 3, 5), (31,), (2,), (3, 11), (2, 17), (5, 7)]), ((36, 81), [(2, 3), (37,), (2, 19), (3, 13), (2, 5), (41,), (2, 3, 7), (43,), (2, 11), (3, 5), (2, 23), (47,), (2, 3), (7,), (2, 5), (3, 17), (2, 13), (53,), (2, 3), (5, 11), (2, 7), (3, 19), (2, 29), (59,), (2, 3, 5), (61,), (2, 31), (3, 7), (2,), (5, 13), (2, 3, 11), (67,), (2, 17), (3, 23), (2, 5, 7), (71,), (2, 3), (73,), (2, 37), (3, 5), (2, 19), (7, 11), (2, 3, 13), (79,), (2, 5)])]
>>> [*islice(iter_sieve4prime_factors_chunks_ge_lt_(0, None, reverse=True), 3)]
Traceback (most recent call last):
    ...
TypeError: reverse and None is may_max1_u7whole

>>> [*islice(iter_sieve4prime_factors_chunks_ge_(14, with_interval=True), 2)]
[((14, 36), [(2, 7), (3, 5), (2,), (17,), (2, 3), (19,), (2, 5), (3, 7), (2, 11), (23,), (2, 3), (5,), (2, 13), (3,), (2, 7), (29,), (2, 3, 5), (31,), (2,), (3, 11), (2, 17), (5, 7)]), ((36, 81), [(2, 3), (37,), (2, 19), (3, 13), (2, 5), (41,), (2, 3, 7), (43,), (2, 11), (3, 5), (2, 23), (47,), (2, 3), (7,), (2, 5), (3, 17), (2, 13), (53,), (2, 3), (5, 11), (2, 7), (3, 19), (2, 29), (59,), (2, 3, 5), (61,), (2, 31), (3, 7), (2,), (5, 13), (2, 3, 11), (67,), (2, 17), (3, 23), (2, 5, 7), (71,), (2, 3), (73,), (2, 37), (3, 5), (2, 19), (7, 11), (2, 3, 13), (79,), (2, 5)])]
>>> [*reverse_iter_sieve4prime_factors_chunks_lt_(42, with_interval=True)]
[((9, 42), [(3,), (2, 5), (11,), (2, 3), (13,), (2, 7), (3, 5), (2,), (17,), (2, 3), (19,), (2, 5), (3, 7), (2, 11), (23,), (2, 3), (5,), (2, 13), (3,), (2, 7), (29,), (2, 3, 5), (31,), (2,), (3, 11), (2, 17), (5, 7), (2, 3), (37,), (2, 19), (3, 13), (2, 5), (41,)]), ((0, 9), [None, (), (2,), (3,), (2,), (5,), (2, 3), (7,), (2,)])]
>>> [*islice(iter_sieve4prime_factorss_ge_lt_(0, None), 16)]
[None, (), (2,), (3,), (2,), (5,), (2, 3), (7,), (2,), (3,), (2, 5), (11,), (2, 3), (13,), (2, 7), (3, 5)]
>>> [*iter_sieve4prime_factorss_ge_lt_(0, 42)]
[None, (), (2,), (3,), (2,), (5,), (2, 3), (7,), (2,), (3,), (2, 5), (11,), (2, 3), (13,), (2, 7), (3, 5), (2,), (17,), (2, 3), (19,), (2, 5), (3, 7), (2, 11), (23,), (2, 3), (5,), (2, 13), (3,), (2, 7), (29,), (2, 3, 5), (31,), (2,), (3, 11), (2, 17), (5, 7), (2, 3), (37,), (2, 19), (3, 13), (2, 5), (41,)]
>>> [*iter_sieve4prime_factorss_ge_lt_(0, 42, reverse=True)]
[(41,), (2, 5), (3, 13), (2, 19), (37,), (2, 3), (5, 7), (2, 17), (3, 11), (2,), (31,), (2, 3, 5), (29,), (2, 7), (3,), (2, 13), (5,), (2, 3), (23,), (2, 11), (3, 7), (2, 5), (19,), (2, 3), (17,), (2,), (3, 5), (2, 7), (13,), (2, 3), (11,), (2, 5), (3,), (2,), (7,), (2, 3), (5,), (2,), (3,), (2,), (), None]
>>> [*islice(iter_sieve4prime_factorss_ge_(244), 16)]
[(2, 61), (5, 7), (2, 3, 41), (13, 19), (2, 31), (3, 83), (2, 5), (251,), (2, 3, 7), (11, 23), (2, 127), (3, 5, 17), (2,), (257,), (2, 3, 43), (7, 37)]
>>> [*islice(reverse_iter_sieve4prime_factorss_lt_(244), 16)]
[(3,), (2, 11), (241,), (2, 3, 5), (239,), (2, 7, 17), (3, 79), (2, 59), (5, 47), (2, 3, 13), (233,), (2, 29), (3, 7, 11), (2, 5, 23), (229,), (2, 3, 19)]
>>> [*reverse_iter_sieve4prime_factorss_lt_(42)]
[(41,), (2, 5), (3, 13), (2, 19), (37,), (2, 3), (5, 7), (2, 17), (3, 11), (2,), (31,), (2, 3, 5), (29,), (2, 7), (3,), (2, 13), (5,), (2, 3), (23,), (2, 11), (3, 7), (2, 5), (19,), (2, 3), (17,), (2,), (3, 5), (2, 7), (13,), (2, 3), (11,), (2, 5), (3,), (2,), (7,), (2, 3), (5,), (2,), (3,), (2,), (), None]


iter_sieve4prime_factorization_chunks_ge_lt_
    iter_sieve4prime_factorization_chunks_ge_
    reverse_iter_sieve4prime_factorization_chunks_lt_
    iter_sieve4prime_factorizations_ge_lt_
        iter_sieve4prime_factorizations_ge_
        reverse_iter_sieve4prime_factorizations_lt_
def iter_sieve4prime_factorization_chunks_ge_lt_(min_u7whole, may_max1_u7whole, /, *, with_interval=False, reverse=False):
>>> [*iter_sieve4prime_factorization_chunks_ge_lt_(0, 100)]
[[None, {}, {2: 1}, {3: 1}, {2: 2}, {5: 1}, {2: 1, 3: 1}, {7: 1}, {2: 3}], [{3: 2}, {2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}, {2: 1, 7: 1}, {3: 1, 5: 1}, {2: 4}, {17: 1}, {2: 1, 3: 2}, {19: 1}, {2: 2, 5: 1}, {3: 1, 7: 1}, {2: 1, 11: 1}, {23: 1}, {2: 3, 3: 1}, {5: 2}, {2: 1, 13: 1}, {3: 3}, {2: 2, 7: 1}, {29: 1}, {2: 1, 3: 1, 5: 1}, {31: 1}, {2: 5}, {3: 1, 11: 1}, {2: 1, 17: 1}, {5: 1, 7: 1}], [{2: 2, 3: 2}, {37: 1}, {2: 1, 19: 1}, {3: 1, 13: 1}, {2: 3, 5: 1}, {41: 1}, {2: 1, 3: 1, 7: 1}, {43: 1}, {2: 2, 11: 1}, {3: 2, 5: 1}, {2: 1, 23: 1}, {47: 1}, {2: 4, 3: 1}, {7: 2}, {2: 1, 5: 2}, {3: 1, 17: 1}, {2: 2, 13: 1}, {53: 1}, {2: 1, 3: 3}, {5: 1, 11: 1}, {2: 3, 7: 1}, {3: 1, 19: 1}, {2: 1, 29: 1}, {59: 1}, {2: 2, 3: 1, 5: 1}, {61: 1}, {2: 1, 31: 1}, {3: 2, 7: 1}, {2: 6}, {5: 1, 13: 1}, {2: 1, 3: 1, 11: 1}, {67: 1}, {2: 2, 17: 1}, {3: 1, 23: 1}, {2: 1, 5: 1, 7: 1}, {71: 1}, {2: 3, 3: 2}, {73: 1}, {2: 1, 37: 1}, {3: 1, 5: 2}, {2: 2, 19: 1}, {7: 1, 11: 1}, {2: 1, 3: 1, 13: 1}, {79: 1}, {2: 4, 5: 1}, {3: 4}, {2: 1, 41: 1}, {83: 1}, {2: 2, 3: 1, 7: 1}, {5: 1, 17: 1}, {2: 1, 43: 1}, {3: 1, 29: 1}, {2: 3, 11: 1}, {89: 1}, {2: 1, 3: 2, 5: 1}, {7: 1, 13: 1}, {2: 2, 23: 1}, {3: 1, 31: 1}, {2: 1, 47: 1}, {5: 1, 19: 1}, {2: 5, 3: 1}, {97: 1}, {2: 1, 7: 2}, {3: 2, 11: 1}]]
>>> [*iter_sieve4prime_factorization_chunks_ge_lt_(0, 100, with_interval=True)]
[((0, 9), [None, {}, {2: 1}, {3: 1}, {2: 2}, {5: 1}, {2: 1, 3: 1}, {7: 1}, {2: 3}]), ((9, 36), [{3: 2}, {2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}, {2: 1, 7: 1}, {3: 1, 5: 1}, {2: 4}, {17: 1}, {2: 1, 3: 2}, {19: 1}, {2: 2, 5: 1}, {3: 1, 7: 1}, {2: 1, 11: 1}, {23: 1}, {2: 3, 3: 1}, {5: 2}, {2: 1, 13: 1}, {3: 3}, {2: 2, 7: 1}, {29: 1}, {2: 1, 3: 1, 5: 1}, {31: 1}, {2: 5}, {3: 1, 11: 1}, {2: 1, 17: 1}, {5: 1, 7: 1}]), ((36, 100), [{2: 2, 3: 2}, {37: 1}, {2: 1, 19: 1}, {3: 1, 13: 1}, {2: 3, 5: 1}, {41: 1}, {2: 1, 3: 1, 7: 1}, {43: 1}, {2: 2, 11: 1}, {3: 2, 5: 1}, {2: 1, 23: 1}, {47: 1}, {2: 4, 3: 1}, {7: 2}, {2: 1, 5: 2}, {3: 1, 17: 1}, {2: 2, 13: 1}, {53: 1}, {2: 1, 3: 3}, {5: 1, 11: 1}, {2: 3, 7: 1}, {3: 1, 19: 1}, {2: 1, 29: 1}, {59: 1}, {2: 2, 3: 1, 5: 1}, {61: 1}, {2: 1, 31: 1}, {3: 2, 7: 1}, {2: 6}, {5: 1, 13: 1}, {2: 1, 3: 1, 11: 1}, {67: 1}, {2: 2, 17: 1}, {3: 1, 23: 1}, {2: 1, 5: 1, 7: 1}, {71: 1}, {2: 3, 3: 2}, {73: 1}, {2: 1, 37: 1}, {3: 1, 5: 2}, {2: 2, 19: 1}, {7: 1, 11: 1}, {2: 1, 3: 1, 13: 1}, {79: 1}, {2: 4, 5: 1}, {3: 4}, {2: 1, 41: 1}, {83: 1}, {2: 2, 3: 1, 7: 1}, {5: 1, 17: 1}, {2: 1, 43: 1}, {3: 1, 29: 1}, {2: 3, 11: 1}, {89: 1}, {2: 1, 3: 2, 5: 1}, {7: 1, 13: 1}, {2: 2, 23: 1}, {3: 1, 31: 1}, {2: 1, 47: 1}, {5: 1, 19: 1}, {2: 5, 3: 1}, {97: 1}, {2: 1, 7: 2}, {3: 2, 11: 1}])]
>>> [*iter_sieve4prime_factorization_chunks_ge_lt_(0, 100, reverse=True)]
[[{2: 2, 3: 2}, {37: 1}, {2: 1, 19: 1}, {3: 1, 13: 1}, {2: 3, 5: 1}, {41: 1}, {2: 1, 3: 1, 7: 1}, {43: 1}, {2: 2, 11: 1}, {3: 2, 5: 1}, {2: 1, 23: 1}, {47: 1}, {2: 4, 3: 1}, {7: 2}, {2: 1, 5: 2}, {3: 1, 17: 1}, {2: 2, 13: 1}, {53: 1}, {2: 1, 3: 3}, {5: 1, 11: 1}, {2: 3, 7: 1}, {3: 1, 19: 1}, {2: 1, 29: 1}, {59: 1}, {2: 2, 3: 1, 5: 1}, {61: 1}, {2: 1, 31: 1}, {3: 2, 7: 1}, {2: 6}, {5: 1, 13: 1}, {2: 1, 3: 1, 11: 1}, {67: 1}, {2: 2, 17: 1}, {3: 1, 23: 1}, {2: 1, 5: 1, 7: 1}, {71: 1}, {2: 3, 3: 2}, {73: 1}, {2: 1, 37: 1}, {3: 1, 5: 2}, {2: 2, 19: 1}, {7: 1, 11: 1}, {2: 1, 3: 1, 13: 1}, {79: 1}, {2: 4, 5: 1}, {3: 4}, {2: 1, 41: 1}, {83: 1}, {2: 2, 3: 1, 7: 1}, {5: 1, 17: 1}, {2: 1, 43: 1}, {3: 1, 29: 1}, {2: 3, 11: 1}, {89: 1}, {2: 1, 3: 2, 5: 1}, {7: 1, 13: 1}, {2: 2, 23: 1}, {3: 1, 31: 1}, {2: 1, 47: 1}, {5: 1, 19: 1}, {2: 5, 3: 1}, {97: 1}, {2: 1, 7: 2}, {3: 2, 11: 1}], [{3: 2}, {2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}, {2: 1, 7: 1}, {3: 1, 5: 1}, {2: 4}, {17: 1}, {2: 1, 3: 2}, {19: 1}, {2: 2, 5: 1}, {3: 1, 7: 1}, {2: 1, 11: 1}, {23: 1}, {2: 3, 3: 1}, {5: 2}, {2: 1, 13: 1}, {3: 3}, {2: 2, 7: 1}, {29: 1}, {2: 1, 3: 1, 5: 1}, {31: 1}, {2: 5}, {3: 1, 11: 1}, {2: 1, 17: 1}, {5: 1, 7: 1}], [None, {}, {2: 1}, {3: 1}, {2: 2}, {5: 1}, {2: 1, 3: 1}, {7: 1}, {2: 3}]]
>>> [*islice(iter_sieve4prime_factorization_chunks_ge_lt_(0, None), 3)]
[[None, {}, {2: 1}, {3: 1}, {2: 2}, {5: 1}, {2: 1, 3: 1}, {7: 1}, {2: 3}], [{3: 2}, {2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}, {2: 1, 7: 1}, {3: 1, 5: 1}, {2: 4}, {17: 1}, {2: 1, 3: 2}, {19: 1}, {2: 2, 5: 1}, {3: 1, 7: 1}, {2: 1, 11: 1}, {23: 1}, {2: 3, 3: 1}, {5: 2}, {2: 1, 13: 1}, {3: 3}, {2: 2, 7: 1}, {29: 1}, {2: 1, 3: 1, 5: 1}, {31: 1}, {2: 5}, {3: 1, 11: 1}, {2: 1, 17: 1}, {5: 1, 7: 1}], [{2: 2, 3: 2}, {37: 1}, {2: 1, 19: 1}, {3: 1, 13: 1}, {2: 3, 5: 1}, {41: 1}, {2: 1, 3: 1, 7: 1}, {43: 1}, {2: 2, 11: 1}, {3: 2, 5: 1}, {2: 1, 23: 1}, {47: 1}, {2: 4, 3: 1}, {7: 2}, {2: 1, 5: 2}, {3: 1, 17: 1}, {2: 2, 13: 1}, {53: 1}, {2: 1, 3: 3}, {5: 1, 11: 1}, {2: 3, 7: 1}, {3: 1, 19: 1}, {2: 1, 29: 1}, {59: 1}, {2: 2, 3: 1, 5: 1}, {61: 1}, {2: 1, 31: 1}, {3: 2, 7: 1}, {2: 6}, {5: 1, 13: 1}, {2: 1, 3: 1, 11: 1}, {67: 1}, {2: 2, 17: 1}, {3: 1, 23: 1}, {2: 1, 5: 1, 7: 1}, {71: 1}, {2: 3, 3: 2}, {73: 1}, {2: 1, 37: 1}, {3: 1, 5: 2}, {2: 2, 19: 1}, {7: 1, 11: 1}, {2: 1, 3: 1, 13: 1}, {79: 1}, {2: 4, 5: 1}]]
>>> [*islice(iter_sieve4prime_factorization_chunks_ge_lt_(0, None, with_interval=True), 3)]
[((0, 9), [None, {}, {2: 1}, {3: 1}, {2: 2}, {5: 1}, {2: 1, 3: 1}, {7: 1}, {2: 3}]), ((9, 36), [{3: 2}, {2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}, {2: 1, 7: 1}, {3: 1, 5: 1}, {2: 4}, {17: 1}, {2: 1, 3: 2}, {19: 1}, {2: 2, 5: 1}, {3: 1, 7: 1}, {2: 1, 11: 1}, {23: 1}, {2: 3, 3: 1}, {5: 2}, {2: 1, 13: 1}, {3: 3}, {2: 2, 7: 1}, {29: 1}, {2: 1, 3: 1, 5: 1}, {31: 1}, {2: 5}, {3: 1, 11: 1}, {2: 1, 17: 1}, {5: 1, 7: 1}]), ((36, 81), [{2: 2, 3: 2}, {37: 1}, {2: 1, 19: 1}, {3: 1, 13: 1}, {2: 3, 5: 1}, {41: 1}, {2: 1, 3: 1, 7: 1}, {43: 1}, {2: 2, 11: 1}, {3: 2, 5: 1}, {2: 1, 23: 1}, {47: 1}, {2: 4, 3: 1}, {7: 2}, {2: 1, 5: 2}, {3: 1, 17: 1}, {2: 2, 13: 1}, {53: 1}, {2: 1, 3: 3}, {5: 1, 11: 1}, {2: 3, 7: 1}, {3: 1, 19: 1}, {2: 1, 29: 1}, {59: 1}, {2: 2, 3: 1, 5: 1}, {61: 1}, {2: 1, 31: 1}, {3: 2, 7: 1}, {2: 6}, {5: 1, 13: 1}, {2: 1, 3: 1, 11: 1}, {67: 1}, {2: 2, 17: 1}, {3: 1, 23: 1}, {2: 1, 5: 1, 7: 1}, {71: 1}, {2: 3, 3: 2}, {73: 1}, {2: 1, 37: 1}, {3: 1, 5: 2}, {2: 2, 19: 1}, {7: 1, 11: 1}, {2: 1, 3: 1, 13: 1}, {79: 1}, {2: 4, 5: 1}])]
>>> [*islice(iter_sieve4prime_factorization_chunks_ge_lt_(0, None, reverse=True), 3)]
Traceback (most recent call last):
    ...
TypeError: reverse and None is may_max1_u7whole

>>> [*islice(iter_sieve4prime_factorization_chunks_ge_(14, with_interval=True), 2)]
[((14, 36), [{2: 1, 7: 1}, {3: 1, 5: 1}, {2: 4}, {17: 1}, {2: 1, 3: 2}, {19: 1}, {2: 2, 5: 1}, {3: 1, 7: 1}, {2: 1, 11: 1}, {23: 1}, {2: 3, 3: 1}, {5: 2}, {2: 1, 13: 1}, {3: 3}, {2: 2, 7: 1}, {29: 1}, {2: 1, 3: 1, 5: 1}, {31: 1}, {2: 5}, {3: 1, 11: 1}, {2: 1, 17: 1}, {5: 1, 7: 1}]), ((36, 81), [{2: 2, 3: 2}, {37: 1}, {2: 1, 19: 1}, {3: 1, 13: 1}, {2: 3, 5: 1}, {41: 1}, {2: 1, 3: 1, 7: 1}, {43: 1}, {2: 2, 11: 1}, {3: 2, 5: 1}, {2: 1, 23: 1}, {47: 1}, {2: 4, 3: 1}, {7: 2}, {2: 1, 5: 2}, {3: 1, 17: 1}, {2: 2, 13: 1}, {53: 1}, {2: 1, 3: 3}, {5: 1, 11: 1}, {2: 3, 7: 1}, {3: 1, 19: 1}, {2: 1, 29: 1}, {59: 1}, {2: 2, 3: 1, 5: 1}, {61: 1}, {2: 1, 31: 1}, {3: 2, 7: 1}, {2: 6}, {5: 1, 13: 1}, {2: 1, 3: 1, 11: 1}, {67: 1}, {2: 2, 17: 1}, {3: 1, 23: 1}, {2: 1, 5: 1, 7: 1}, {71: 1}, {2: 3, 3: 2}, {73: 1}, {2: 1, 37: 1}, {3: 1, 5: 2}, {2: 2, 19: 1}, {7: 1, 11: 1}, {2: 1, 3: 1, 13: 1}, {79: 1}, {2: 4, 5: 1}])]
>>> [*reverse_iter_sieve4prime_factorization_chunks_lt_(42, with_interval=True)]
[((9, 42), [{3: 2}, {2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}, {2: 1, 7: 1}, {3: 1, 5: 1}, {2: 4}, {17: 1}, {2: 1, 3: 2}, {19: 1}, {2: 2, 5: 1}, {3: 1, 7: 1}, {2: 1, 11: 1}, {23: 1}, {2: 3, 3: 1}, {5: 2}, {2: 1, 13: 1}, {3: 3}, {2: 2, 7: 1}, {29: 1}, {2: 1, 3: 1, 5: 1}, {31: 1}, {2: 5}, {3: 1, 11: 1}, {2: 1, 17: 1}, {5: 1, 7: 1}, {2: 2, 3: 2}, {37: 1}, {2: 1, 19: 1}, {3: 1, 13: 1}, {2: 3, 5: 1}, {41: 1}]), ((0, 9), [None, {}, {2: 1}, {3: 1}, {2: 2}, {5: 1}, {2: 1, 3: 1}, {7: 1}, {2: 3}])]
>>> [*islice(iter_sieve4prime_factorizations_ge_lt_(0, None), 16)]
[None, {}, {2: 1}, {3: 1}, {2: 2}, {5: 1}, {2: 1, 3: 1}, {7: 1}, {2: 3}, {3: 2}, {2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}, {2: 1, 7: 1}, {3: 1, 5: 1}]
>>> [*iter_sieve4prime_factorizations_ge_lt_(0, 42)]
[None, {}, {2: 1}, {3: 1}, {2: 2}, {5: 1}, {2: 1, 3: 1}, {7: 1}, {2: 3}, {3: 2}, {2: 1, 5: 1}, {11: 1}, {2: 2, 3: 1}, {13: 1}, {2: 1, 7: 1}, {3: 1, 5: 1}, {2: 4}, {17: 1}, {2: 1, 3: 2}, {19: 1}, {2: 2, 5: 1}, {3: 1, 7: 1}, {2: 1, 11: 1}, {23: 1}, {2: 3, 3: 1}, {5: 2}, {2: 1, 13: 1}, {3: 3}, {2: 2, 7: 1}, {29: 1}, {2: 1, 3: 1, 5: 1}, {31: 1}, {2: 5}, {3: 1, 11: 1}, {2: 1, 17: 1}, {5: 1, 7: 1}, {2: 2, 3: 2}, {37: 1}, {2: 1, 19: 1}, {3: 1, 13: 1}, {2: 3, 5: 1}, {41: 1}]
>>> [*iter_sieve4prime_factorizations_ge_lt_(0, 42, reverse=True)]
[{41: 1}, {2: 3, 5: 1}, {3: 1, 13: 1}, {2: 1, 19: 1}, {37: 1}, {2: 2, 3: 2}, {5: 1, 7: 1}, {2: 1, 17: 1}, {3: 1, 11: 1}, {2: 5}, {31: 1}, {2: 1, 3: 1, 5: 1}, {29: 1}, {2: 2, 7: 1}, {3: 3}, {2: 1, 13: 1}, {5: 2}, {2: 3, 3: 1}, {23: 1}, {2: 1, 11: 1}, {3: 1, 7: 1}, {2: 2, 5: 1}, {19: 1}, {2: 1, 3: 2}, {17: 1}, {2: 4}, {3: 1, 5: 1}, {2: 1, 7: 1}, {13: 1}, {2: 2, 3: 1}, {11: 1}, {2: 1, 5: 1}, {3: 2}, {2: 3}, {7: 1}, {2: 1, 3: 1}, {5: 1}, {2: 2}, {3: 1}, {2: 1}, {}, None]
>>> [*islice(iter_sieve4prime_factorizations_ge_(244), 16)]
[{2: 2, 61: 1}, {5: 1, 7: 2}, {2: 1, 3: 1, 41: 1}, {13: 1, 19: 1}, {2: 3, 31: 1}, {3: 1, 83: 1}, {2: 1, 5: 3}, {251: 1}, {2: 2, 3: 2, 7: 1}, {11: 1, 23: 1}, {2: 1, 127: 1}, {3: 1, 5: 1, 17: 1}, {2: 8}, {257: 1}, {2: 1, 3: 1, 43: 1}, {7: 1, 37: 1}]
>>> [*islice(reverse_iter_sieve4prime_factorizations_lt_(244), 16)]
[{3: 5}, {2: 1, 11: 2}, {241: 1}, {2: 4, 3: 1, 5: 1}, {239: 1}, {2: 1, 7: 1, 17: 1}, {3: 1, 79: 1}, {2: 2, 59: 1}, {5: 1, 47: 1}, {2: 1, 3: 2, 13: 1}, {233: 1}, {2: 3, 29: 1}, {3: 1, 7: 1, 11: 1}, {2: 1, 5: 1, 23: 1}, {229: 1}, {2: 2, 3: 1, 19: 1}]
>>> [*reverse_iter_sieve4prime_factorizations_lt_(42)]
[{41: 1}, {2: 3, 5: 1}, {3: 1, 13: 1}, {2: 1, 19: 1}, {37: 1}, {2: 2, 3: 2}, {5: 1, 7: 1}, {2: 1, 17: 1}, {3: 1, 11: 1}, {2: 5}, {31: 1}, {2: 1, 3: 1, 5: 1}, {29: 1}, {2: 2, 7: 1}, {3: 3}, {2: 1, 13: 1}, {5: 2}, {2: 3, 3: 1}, {23: 1}, {2: 1, 11: 1}, {3: 1, 7: 1}, {2: 2, 5: 1}, {19: 1}, {2: 1, 3: 2}, {17: 1}, {2: 4}, {3: 1, 5: 1}, {2: 1, 7: 1}, {13: 1}, {2: 2, 3: 1}, {11: 1}, {2: 1, 5: 1}, {3: 2}, {2: 3}, {7: 1}, {2: 1, 3: 1}, {5: 1}, {2: 2}, {3: 1}, {2: 1}, {}, None]







>>> [*iter_sieve4primes_ge_lt_(0, 9, with_uint=True)]
Traceback (most recent call last):
    ...
TypeError: iter_sieve4primes_ge_lt_() got an unexpected keyword argument 'with_uint'
>>> [*iter_sieve4prime_factorss_ge_lt_(0, 9, with_uint=True)]
[(0, None), (1, ()), (2, (2,)), (3, (3,)), (4, (2,)), (5, (5,)), (6, (2, 3)), (7, (7,)), (8, (2,))]
>>> [*iter_sieve4prime_factorizations_ge_lt_(0, 9, with_uint=True)]
[(0, None), (1, {}), (2, {2: 1}), (3, {3: 1}), (4, {2: 2}), (5, {5: 1}), (6, {2: 1, 3: 1}), (7, {7: 1}), (8, {2: 3})]
>>> [*islice(iter_sieve4prime_factorizations_ge_(0, with_uint=True), 4)]
[(0, None), (1, {}), (2, {2: 1}), (3, {3: 1})]
>>> [*reverse_iter_sieve4prime_factorizations_lt_(9, with_uint=True)]
[(8, {2: 3}), (7, {7: 1}), (6, {2: 1, 3: 1}), (5, {5: 1}), (4, {2: 2}), (3, {3: 1}), (2, {2: 1}), (1, {}), (0, None)]


>>> iter_primes_ is iter_primes__new_ver_
True
>>> [*islice(iter_primes_(), 20)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]





py_adhoc_call   seed.math.prime_sieve.sieve_ge_le   @f
]]]'''#'''
__all__ = r'''
iter_primes_        iter_primes__new_ver_


iter_best_interval5big_interval6args4sieve_interval_
    calc_best_begin5end6args4sieve_interval_
        iter_best_begins5end6args4sieve_interval_
    calc_best_end5begin6args4sieve_interval_
        iter_best_ends5begin6args4sieve_interval_

calc_min_end5begin6args4sieve_interval_
    test4calc_min_end5begin6args4sieve_interval_
    iter_min_ends5begin6args4sieve_interval_

check_args4core_sieve_interval__ge_le
check_args4sieve_interval__ge_lt

to_std_args4core_sieve_interval__ge_le
to_std_args4sieve_interval__ge_lt



iter_sieve4prime_chunks_ge_lt_
    iter_sieve4prime_chunks_ge_
    reverse_iter_sieve4prime_chunks_lt_
    iter_sieve4primes_ge_lt_
        iter_sieve4primes_ge_
        reverse_iter_sieve4primes_lt_

iter_sieve4prime_factors_chunks_ge_lt_
    iter_sieve4prime_factors_chunks_ge_
    reverse_iter_sieve4prime_factors_chunks_lt_
    iter_sieve4prime_factorss_ge_lt_
        iter_sieve4prime_factorss_ge_
        reverse_iter_sieve4prime_factorss_lt_

iter_sieve4prime_factorization_chunks_ge_lt_
    iter_sieve4prime_factorization_chunks_ge_
    reverse_iter_sieve4prime_factorization_chunks_lt_
    iter_sieve4prime_factorizations_ge_lt_
        iter_sieve4prime_factorizations_ge_
        reverse_iter_sieve4prime_factorizations_lt_



sieve_interval4primes__ge_lt
sieve_interval4offsetted_uint2is_prime__ge_lt
sieve_interval4prime_factorization__ge_lt
sieve_interval4prime_factors__ge_lt


core_sieve4primes__ge_le
core_sieve4offsetted_uint2is_prime__ge_le
core_sieve4prime_factorization__ge_le
core_sieve4pairs8prime_factorization__ge_le
core_sieve4prime_factors__ge_le









'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__, 'repeat:_repeat'):
    from itertools import repeat as _repeat, pairwise
    from seed.iters.chains import chains

    from seed.tiny_.check import check_int_ge_lt, check_int_ge
    from seed.math.II import II
    #from math import isqrt as floor_sqrt
    from seed.math.floor_ceil_tools.fc_kth_root import floor_sqrt, ceil_sqrt
    from seed.math.floor_ceil_tools.fc_log import floor_log2
    from seed.math.floor_ceil_tools.fc_div import floor_div_, ceil_div_


    from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
    from seed.math.prime_sieve.sieve_lt import list_all_strict_sorted_primes__lt_, sieve4uint2is_prime__lt_
    from seed.math.prime_sieve.sieve_lt import tabulate_may_all_prime_factors4uint_lt_
    from seed.math.prime_sieve.sieve_lt import tabulate_may_prime_factorization4uint_lt_#deprecated: tabulate_may_factorization4uint_lt_
    from seed.math.prime_sieve.sieve_lt import check_offsetted_uint2pairs8prime_factorization_, check_offsetted_uint2prime_factors_

    #from seed.math.is_prime__via_complete_factorization_Nmm_ import is_prime__via_complete_factorization_Nmm_
    #def is_prime__via_complete_factorization_Nmm_(p2e4Nmm_or_ps4Nmm, N, /):
#.#################################
___end_mark_of_excluded_global_names__0___ = ...





def _test4mk_offsetted_u2num_bits7remain_():
    for min_u in range(10):
        for max1_u in range(min_u, 20):
            _mk_offsetted_u2num_bits7remain_(min_u, max1_u, _validate=True)
def _mk_offsetted_u2num_bits7remain_(min_u, max1_u, /, *, _validate=False):
    #_u2num_bits7remain = [u.bit_length() for u in range(min_u, max1_u)]
    assert 0 <= min_u <= max1_u
    n0 = min_u.bit_length()
    nt = max1_u.bit_length()
    if not n0 < nt:
        _u2num_bits7remain = [n0]*(max1_u -min_u)
    else:
        _u2num_bits7remain = []
        def iter_ez_end_pairs_():
            for ez in range(n0, nt):
                end = 1<<ez
                yield (ez, end)
            else:
                ez = nt
                end = max1_u
                yield (ez, end)
        begin = min_u
        for (ez, end) in iter_ez_end_pairs_():
            _u2num_bits7remain.extend(_repeat(ez, end-begin))
            begin = end
        _u2num_bits7remain
    _u2num_bits7remain
    if _validate:
        assert _u2num_bits7remain == [u.bit_length() for u in range(min_u, max1_u)]
    return _u2num_bits7remain
r'''[[[


[[
copy_to:
    view ../lots/NOTE/math-book/prime/The_new_book_of_prime_number_records-note.txt
===
[product_of_the_coprime_rates_of_prime_numbers_le_(x):=sum[(1-1/p) | [p::prime][p <= x]]]
    # [(1-1/p) == (p-1)/p == phi(p)/p]
[sum_of_the_inverses_of_positive_integers_le_(x):=sum[1/n | [n:<-[1..]][n <= x]]]
[sum_of_the_inverses_of_prime_numbers_le_(x):=sum[1/p | [p::prime][p <= x]]]
    #sum of the reciprocals of all of the primes between ...
[sum_of_the_inverses_of_4k1_prime_numbers_le_(x):=sum[1/p | [p::prime][p%4==1][p <= x]]]

[sum_of_the_inverses_of_prime_powers_le_(x):=sum[1/p**e | [p::prime][e::uint][e>=1][p**e <= x]]]

==>>:
[sum_of_the_inverses_of_prime_numbers_le_(x) == lnln(x) +C +O(1/ln(x))] where [C~=0.2615...]
    page228[253/567]@'/sdcard/0my_files/book/math/factorint/snd/The new book of prime number records(3ed)(1996)(Ribenboim).djvu'
    I. The Growth of pi(x)
        A. History Unfolding
            Erdos and Selberg

[the_Euler_constant =[def]= limit{sum_of_the_inverses_of_positive_integers_le_(n) -ln(n) | n-->+oo}]
    ~= 0.577215665....
    page222[247/567]@'/sdcard/0my_files/book/math/factorint/snd/The new book of prime number records(3ed)(1996)(Ribenboim).djvu'

or:
[sum[N/p | [p::prime][p <= N]] == N*lnln(N) +O(N)]
    page121[134/604]@'Prime numbers-A Computational Perspective(2ed)(2005)(Pomerance).pdf'
        3.2.1 Sieving to recognize primes
            formula_3_1

[limit{sum[1/p | [p::prime][sqrt(N) < p <= N]] | N-->+oo} == ln(2) ~= 0.6931471805599453]
[sum_of_the_inverses_of_prime_numbers_le_(sqrt(x)) == lnln(x) +O(1)]
[1/2+2*sum_of_the_inverses_of_4k1_prime_numbers_le_(x) == lnln(x) +O(1)]
    page125[138/604]@'Prime numbers-A Computational Perspective(2ed)(2005)(Pomerance).pdf'

[sum_of_the_inverses_of_prime_numbers_le_(x) == lnln(x) +B +o(1)] where [B:=the_Mertens_constant=the_Euler_constant+sum[(ln(1-1/p)+1/p) | [p::prime]]]
    formula_1_21
    <<==:
[[x-->+oo] => [product_of_the_coprime_rates_of_prime_numbers_le_(x) ~ 1/e**the_Euler_constant/ln(x)]]
    #<==>:
    [limit{(product_of_the_coprime_rates_of_prime_numbers_le_(x) * ln(x)) | [x-->+oo]} == 1/e**the_Euler_constant]
    page35[49/604]@'Prime numbers-A Computational Perspective(2ed)(2005)(Pomerance).pdf'
    Theorem__1_4_2 (Mertens)
    the Mertens Theorem 1.4.2
    the_Mertens_Theorem__1_4_2
        用于分析:轮子互素占比@Algorithm__3_2_2(Fancy Eratosthenes sieve)
    !! [轮子最大素数{轮子规模:=M} ~ (ln(M))]
    !! [下一个轮子规模{轮子规模:=M} == 轮子规模{筛子规模:=M} * 下一个素数{轮子最大素数{轮子规模:=M}}]
    => [下一个轮子规模{轮子规模:=M} ~ 轮子规模{筛子规模:=M} * (ln(M))]
    !! [轮子规模{筛子规模:=N} <= N/ln(N) < 下一个轮子规模{筛子规模:=N}]
    => [轮子最大素数{筛子规模:=N} ~ (ln(轮子规模{筛子规模:=N})) ~ ln(N/ln(N)) ~ ln(N)]
    => [轮子规模{筛子规模:=N} ~ (N/ln(N))]
    => [轮子互素占比{筛子规模:=N} ~ product_of_the_coprime_rates_of_prime_numbers_le_(轮子最大素数{筛子规模:=N}) ~ 1/e**the_Euler_constant/ln(轮子最大素数{筛子规模:=N}) ~ 1/e**the_Euler_constant/ln(ln(N/ln(N))) == O(1/lnln(N))]
    => [N*轮子互素占比{筛子规模:=N} == O(N/lnln(N))]

[轮子最大素数{轮子规模:=M} ~ (ln(M))]
    <<==:
    view ../../python3_src/seed/math/prime_gens.py.note.txt
        [@[x::real] -> [x > 0] -> [II{p | [p::prime][p <= x]} == e**((1+o(1))*x)]]


===
TODO:改版:TabulateMinPrimeFactor --> TabulatePrimes
Algorithm__3_2_2
Algorithm 3.2.2 (Fancy Eratosthenes sieve)
    page126[139/604]@'Prime numbers-A Computational Perspective(2ed)(2005)(Pomerance).pdf'
    优点:改进原筛效率:O(N*lnln(N)) --> O(N/lnln(N))


==>>:
我:[sum_of_the_inverses_of_prime_powers_le_(x) == O(lnln(x))]
    #用于 _sieve_p_,_sieve_p_0_
    <<==:
我:[sum_of_the_inverses_of_prime_powers_le_(x) <= 2*lnln(x) +O(1)]
    [[proof:
    [f(p;x) := sum[1/p**e | [e::uint][e>=1][p**e <= x]]]
    [p::prime][p <= x]:
        [p >= 2]
        [f(p;x)
        :> [ep:=floor_log_(p;x)]
        !! [p <= x]
        => [ep >= 1]
        == sum[1/p**e | [e:<-[1..=ep]]]
        == 1/p*(1-1/p**ep)/(1-1/p)
        !! [ep >= 1]
        < 1/p*(1-0)/(1-1/p)
        == 1/p *p/(p-1)
        == 1/p *(1 +1/(p-1))
        !! [p >= 2]
        <= 1/p *(1 +1/(2-1))
        == 2/p
        ]
        [f(p;x) < 2/p]
    [@[p::prime][p <= x] -> [f(p;x) < 2/p]]

    [sum_of_the_inverses_of_prime_powers_le_(x)
    == sum[1/p**e | [p::prime][e::uint][e>=1][p**e <= x]]
    == sum[sum[1/p**e | [e::uint][e>=1][p**e <= x]] | [p::prime]]
    == sum[sum[1/p**e | [e::uint][e>=1][p**e <= x]] | [p::prime][p <= x]]
    == sum[f(p;x) | [p::prime][p <= x]]
    !! [@[p::prime][p <= x] -> [f(p;x) < 2/p]]
    < sum[2/p | [p::prime][p <= x]]
    == 2 *sum[1/p | [p::prime][p <= x]]
    == 2 *sum_of_the_inverses_of_prime_numbers_le_(x)
    !! [sum_of_the_inverses_of_prime_numbers_le_(x) == lnln(x) +C +O(1/ln(x))] where [C~=0.2615...]
    == 2*lnln(x) +O(1)
    ]
    [sum_of_the_inverses_of_prime_powers_le_(x) <= 2*lnln(x) +O(1)]
    ok
    ]]

]]

==>>:
core_sieve4primes__ge_le(min_u, max_u)
[TIME(prepare primes between [0..=floor_sqrt(max_u)])
    ~= (sum[sqrt(max_u)/p | p <= sqrt(max_u)])
    ~= sqrt(max_u)*(sum_of_the_inverses_of_prime_numbers_le_(sqrt(max_u)))
    == O(sqrt(max_u)*lnln(sqrt(max_u)))
    == O(sqrt(max_u)*lnln(max_u))
]
[TIME(sieve between [min_u..=max_u] with primes between [0..=floor_sqrt(max_u)])
    ~= (sum[(max_u+1-min_u)/p | p <= sqrt(max_u)])
    == O((max_u+1-min_u)*lnln(sqrt(max_u)))
    == O((max_u+1-min_u)*lnln(max_u))
]
[sqrt(max_u) <= (max_u+1-min_u)]:
    # => 平均耗时极小
    [sqrt(min_u) <= sqrt(max_u) <= (max_u+1-min_u)]
    [min_u <= max_u <= (max_u+1-min_u)**2]
    [min_u <= (max_u+1-min_u)**2]

    [max_u <= (max_u+1-min_u)**2]
    [m := 1+max_u]
    [n := min_u]
    [-1+m <= (m-n)**2]
    [-1+m <= m**2-2*n*m+n**2]
    [m**2-(1+2*n)*m+(1+n**2) >= 0]
    [4*n-3>=0]:
        [n >= 3/4]
        [D:=sqrt((1+2*n)**2-4*(1+n**2))]
        [D==sqrt(4*n-3)]
        [m >= ((1+2*n)+D)/2]
        [m >= n +(1+sqrt(4*n-3))/2]
        [1+max_u
        == m
        >= n +ceil((1+sqrt(4*n-3))/2)
        >= n +ceil((1+ceil_sqrt(4*n-3))/2)
        ]
        [min max_u == -1+min_u +ceil((1+ceil_sqrt(4*min_u-3))/2)]
        [min max_u == min_u +ceil((-1+ceil_sqrt(4*min_u-3))/2)]
        [min max_u == min_u +((ceil_sqrt(4*min_u-3))//2)]

[floor_sqrt(max_u) < min_u]:
    # otherwise two tables touched
    [sqrt(max_u) < min_u]
    [max_u < min_u**2]

[max_u < 10*min_u]:
    # otherwise the saved time for [0..<min_u] is negligible
[[max_u < 10*min_u] -> [max_u < min_u**2]]:
    [min_u >= 10]

[min_u <= max_u < 10*min_u][min_u <= max_u <= (max_u+1-min_u)**2]:
    [sqrt(min_u) <= (max_u+1-min_u)]
    [min_u+sqrt(min_u)-1 <= max_u < 10*min_u]
    [min_u+sqrt(min_u)-1 < 10*min_u]
    [sqrt(min_u) <= 9*min_u]
    [min_u <= 81*min_u**2]
    [1 <= 81*min_u]
    [min_u > 0]

[min_u >= 10][min_u <= max_u < 10*min_u][min_u <= max_u <= (max_u+1-min_u)**2]:
    [min_u <= (10*min_u-min_u)**2]
    [min_u <= 81*min_u**2]
    ok

[min_u >= 10][min_u <= max_u < 10*min_u][min_u <= max_u <= (max_u+1-min_u)**2]:
    [O(min_u) == O(max_u)]
    bug:[O(max_u+1-min_u) == O(max_u)]
    [O(sqrt(max_u)) == O(sqrt(min_u)) <= O(max_u+1-min_u) <= O(max_u)]
    [TIME(core_sieve4primes__ge_le(min_u, max_u))
    == TIME(prepare primes between [0..=floor_sqrt(max_u)])
    +  TIME(sieve between [min_u..=max_u] with primes between [0..=floor_sqrt(max_u)])
    == O(sqrt(max_u)*lnln(max_u))
    +  O((max_u+1-min_u)*lnln(max_u))
    !! [sqrt(max_u) <= (max_u+1-min_u)]
    == (max_u+1-min_u)*O(lnln(max_u))
        # 平均耗时极小
    [(max_u+1-min_u) == O(min_u)]:
        !! [O(min_u) == O(max_u)]
        ... == O(max_u*lnln(max_u))
            # 从耗时上看，并没有好处，不如直接 list_all_strict_sorted_primes__lt_(1+max_u)
    [(max_u+1-min_u) == O(sqrt(max_u))]:
        ... == sqrt(max_u)*O(lnln(max_u))
        # 更省时
    ]
    [SPACE(core_sieve4primes__ge_le(min_u, max_u))
    ~= sqrt(max_u) +(max_u+1-min_u)
        # 最小可以是 ~2*sqrt(max_u)
    ]
    为了节省时间、空间，应当有:
        [(max_u+1-min_u) == O(sqrt(max_u))]
        而非:
        [(max_u+1-min_u) == O(min_u)]

assume:[min_u >= 10][min_u <= max_u < 10*min_u][min_u <= max_u <= (max_u+1-min_u)**2]


[lnlnN :<- [1,2,3,...]] => N=???:
>>> from math import ceil, isqrt as floor_sqrt, e as E
>>> E
2.718281828459045
>>> E**E**1
15.154262241479259
>>> E**E**2
1618.1779919126518
>>> E**E**3
528491311.4854919
>>> E**E**4
5.1484355626345056e+23
>>> E**E**5
2.8511235679460374e+64
>>> E**E**6
1.6102705667791347e+175
>>> E**E**7
Traceback (most recent call last):
    ...
OverflowError: (34, 'Math result not representable')

==>>:通常情况:[lnln(max_u) <= 3]
!! 应当有:[开销工作量/有效工作量 < 1/2] #这样累积开销不超过有效工作1
最佳:[(max_u+1-min_u) ~= 2*lnln(max_u)*sqrt(max_u)]
!! 通常情况:[lnln(max_u) <= 3]
=>:[(max_u+1-min_u) ~= 6*sqrt(max_u)]
=>:[sqrt(max_u) ~= 3+sqrt(min_u)]
=>:区间边界序列:可考虑:(map (\n->n**2+3) [3,6,9..])  # 边界值:3*(3*k**2+1):是合数，避免误解

DONE:区间边界序列=>迭代输出一块一块的数据
    chunk by chunk
    iter_sieve4prime_chunks_ge_
        iter_sieve4primes_ge_

    calc_min_end5begin6args4sieve_interval_ --> calc_best_end5begin6args4sieve_interval_
[calc_best_end5begin6args4sieve_interval_(min_u) ~= (3+(3+sqrt(-3+min_u))**2)]
ver1:[calc_best_end5begin6args4sieve_interval_(min_u) := (3+(3+3*ceil_div_(3;floor_sqrt(max(0,-3+min_u))))**2)]
ver2:[calc_best_end5begin6args4sieve_interval_(min_u) := (3+(3+3*ceil_div_(3;-1+floor_sqrt(max(0,-3+min_u))))**2)]
ver3:[calc_best_end5begin6args4sieve_interval_(min_u) := ((3+3*ceil_div_(3;-1+floor_sqrt(max(0,min_u))))**2)]
    ver3:[calc_best_begin5end6args4sieve_interval_(max1_u) := (max(0,-3+3*floor_div_(3;+1+ceil_sqrt(max(0,max1_u))))**2)]

#]]]'''#'''
__all__
def test4calc_min_end5begin6args4sieve_interval_(iterable8min_us, /):
    for min_u in iterable8min_us:
        min_max1_u = calc_min_end5begin6args4sieve_interval_(min_u, validate=False)
        _check_output4calc_min_end5begin6args4sieve_interval_(min_u, min_max1_u)
def _check_output4calc_min_end5begin6args4sieve_interval_(min_u, min_max1_u, /):
    min_max_u = -1+min_max1_u
    assert not ((-1+min_max_u)+1-min_u)**2 >= (-1+min_max_u) or min_max_u == min_u, (min_u, min_max_u)
    assert ((0+min_max_u)+1-min_u)**2 >= (0+min_max_u), (min_u, min_max_u)
    assert min_u <= min_max_u < 10*min_u, (min_u, min_max_u)
def iter_min_ends5begin6args4sieve_interval_(min_u, /, *, with_begin=False, validate=True):
    'begin[0]/min_u/uint -> Iter min_end[k]/begin[1+k]/min_max1_u/uint # [min_u[k] >= 1][min_max1_u[k] == min{1+max_u | [max_u:<-[min_u[k]..<10*min_u[k]]][(max_u+1-min_u[k])**2 >= max_u]}]'
    while 1:
        max1_u = calc_min_end5begin6args4sieve_interval_(min_u, validate=validate)
        yield max1_u if not with_begin else (min_u, max1_u)
        min_u = max1_u
def calc_min_end5begin6args4sieve_interval_(min_u, /, *, validate=True):
    'begin/min_u/uint -> min_end/min_max1_u/uint # [min_u >= 1][min_max1_u == min{1+max_u | [max_u:<-[min_u..<10*min_u]][(max_u+1-min_u)**2 >= max_u]}]'
    min_u = max(1, min_u)
    #check_int_ge(10, min_u)
    check_int_ge(1, min_u)
    min_max_u = min_u +((ceil_sqrt(4*min_u-3))//2)
    min_max1_u = 1+min_max_u
    if validate:
        _check_output4calc_min_end5begin6args4sieve_interval_(min_u, min_max1_u)
    return min_max1_u
def iter_best_begins5end6args4sieve_interval_(max1_u, /, *, with_end=False, validate=True):
    'end[0]/max1_u/uint -> Iter best_begin[k]/end[1+k]/best_min_u/uint # [max1_u[k] >= 0][best_min_u[k]  ~= ((-3+sqrt(max1_u))**2)]'
    while max1_u > 0:
        min_u = calc_best_begin5end6args4sieve_interval_(max1_u, validate=validate)
        yield min_u if not with_end else (min_u, max1_u)
        max1_u = min_u
def calc_best_begin5end6args4sieve_interval_(max1_u, /, *, validate=True):
    'end/max1_u/uint -> best_begin/best_min_u/uint # [max1_u >= 0][best_min_u ~= ((-3+sqrt(max1_u))**2)]'
    max1_u = max(0, max1_u)
    # ver3:[calc_best_begin5end6args4sieve_interval_(max1_u) := (max(0,-3+3*floor_div_(3;+1+ceil_sqrt(max(0,max1_u))))**2)]
    best_min_u = (max(0,-3+3*floor_div_(3,+1+ceil_sqrt(max(0,max1_u))))**2)
    #########
    if validate:
        check_args4sieve_interval__ge_lt(best_min_u, max1_u)
    return best_min_u
def iter_best_ends5begin6args4sieve_interval_(min_u, /, *, with_begin=False, validate=True):
    'begin[0]/min_u/uint -> Iter best_end[k]/begin[1+k]/best_max1_u/uint # [min_u[k] >= 0][best_max1_u[k]  ~= ((3+sqrt(min_u))**2)]'
    while 1:
        max1_u = calc_best_end5begin6args4sieve_interval_(min_u, validate=validate)
        yield max1_u if not with_begin else (min_u, max1_u)
        min_u = max1_u
def calc_best_end5begin6args4sieve_interval_(min_u, /, *, validate=True):
    'begin/min_u/uint -> best_end/best_max1_u/uint # [min_u >= 0][best_max1_u ~= ((3+sqrt(min_u))**2)]'
    min_u = max(0, min_u)
    #########
    # ver2:[calc_best_end5begin6args4sieve_interval_(min_u) := (3+(3+3*ceil_div_(3;-1+floor_sqrt(max(0,-3+min_u))))**2)]
    #.best_max1_u = (3+(3+3*ceil_div_(3,-1+floor_sqrt(max(0,-3+min_u))))**2)
    #########
    #ver3:[calc_best_end5begin6args4sieve_interval_(min_u) := ((3+3*ceil_div_(3;-1+floor_sqrt(max(0,min_u))))**2)]
    best_max1_u = ((3+3*ceil_div_(3,-1+floor_sqrt(max(0,min_u))))**2)
    #########
    if validate:
        check_args4sieve_interval__ge_lt(min_u, best_max1_u)
    return best_max1_u
def iter_best_interval5big_interval6args4sieve_interval_(min_u7whole, may_max1_u7whole, /, *, reverse=False, validate=True):
    'min_u7whole/begin[0]/uint -> may max1_u7whole/end[-1]/uint -> Iter (begin[k], end[k]) #[begin[k]  ~= ((3+sqrt(end[k]))**2)]'
    if None is may_max1_u7whole:
        if reverse:raise TypeError('reverse and None is may_max1_u7whole')
        yield from iter_best_ends5begin6args4sieve_interval_(min_u7whole, with_begin=True, validate=validate)
        return
    max1_u7whole = may_max1_u7whole
    check_int_ge(0, min_u7whole)
    check_int_ge(0, max1_u7whole)
    if not min_u7whole < max1_u7whole:
        return
    if reverse and min_u7whole == 0:
        yield from iter_best_begins5end6args4sieve_interval_(max1_u7whole, with_end=True, validate=validate)
        return

    max1_u7first = calc_best_end5begin6args4sieve_interval_(min_u7whole)
    min_u7last = calc_best_begin5end6args4sieve_interval_(max1_u7whole)

    if not max1_u7first <= min_u7last:
        interval7whole = (min_u7whole, max1_u7whole)
        if validate:
            check_args4sieve_interval__ge_lt(*interval7whole)
        yield interval7whole
        return

    if reverse:
        for begin, end in iter_best_begins5end6args4sieve_interval_(max1_u7whole, with_end=True, validate=validate):
            yield (begin, end)
            if begin <= max1_u7first:
                if not begin == max1_u7first:raise 000
                yield (min_u7whole, max1_u7first)
                return
        raise 000
    else:
        for begin, end in iter_best_ends5begin6args4sieve_interval_(min_u7whole, with_begin=True, validate=validate):
            yield (begin, end)
            if end >= min_u7last:
                if not end == min_u7last:raise 000
                yield (min_u7last, max1_u7whole)
                return
        raise 000
    raise 000

def check_args4core_sieve_interval__ge_le(min_u, max_u, /):
    'min_u -> max_u -> None if [[min_u >= 10][min_u <= max_u < 10*min_u][(max_u+1-min_u)**2 >= max_u >= min_u]] else ^TypeError'
    check_int_ge(10, min_u)
    check_int_ge_lt(min_u, 10*min_u, max_u)
    if not (max_u-min_u+1)**2 >= max_u >= min_u:raise TypeError(min_u, max_u)
def check_args4sieve_interval__ge_lt(min_u, max1_u, /):
    'min_u -> max1_u -> None if [0 == min_u <= max1_u] or [[1 <= min_u < max1_u][(max1_u-min_u)**2 >= -1+max1_u]] else ^TypeError'
    check_int_ge(0, min_u)
    check_int_ge(min_u, max1_u)
    if min_u == 0:
        return
    if not (max1_u-min_u)**2 >= -1+max1_u >= min_u:raise TypeError(min_u, max1_u)
def to_std_args4sieve_interval__ge_lt(min_u, emay_max1_u, /):
    min_u = max(0, min_u)
    if emay_max1_u is ...:
        max1_u = calc_min_end5begin6args4sieve_interval_(min_u)
    else:
        max1_u = emay_max1_u
    return (min_u, max1_u)
def to_std_args4core_sieve_interval__ge_le(min_u, emay_max_u, /):
    if emay_max_u is ...:
        max_u = -1+calc_min_end5begin6args4sieve_interval_(min_u)
    else:
        max_u = emay_max_u
    return (min_u, max_u)
#def iter_primes__old_ver_=iter_all_strict_sorted_primes_(*, size=None, end=None, may_primes=None):
def iter_primes__new_ver_():
    '-> Iter prime'
    return iter_sieve4primes_ge_(0)
iter_primes_ = iter_primes__new_ver_
def iter_sieve4primes_ge_(min_u, /):
    'min_u/uint -> Iter prime{>=min_u}'
    return iter_sieve4primes_ge_lt_(min_u, None, reverse=False)
def reverse_iter_sieve4primes_lt_(max1_u, /):
    'max1_u/uint -> Iter prime{<max1_u}'
    return iter_sieve4primes_ge_lt_(0, max1_u, reverse=True)
def iter_sieve4primes_ge_lt_(min_u7whole, may_max1_u7whole, /, *, reverse=False):
    'min_u7whole/uint -> may max1_u7whole/uint -> Iter prime{>=min_u}'
    it = iter_sieve4prime_chunks_ge_lt_(min_u7whole, may_max1_u7whole, reverse=reverse)
    if reverse:
        it = map(reversed, it)
    return chains(it)

def iter_sieve4prime_chunks_ge_(min_u, /, *, with_interval=False):
    'min_u/uint -> Iter [prime{>=min_u}]'
    return iter_sieve4prime_chunks_ge_lt_(min_u, None, with_interval=with_interval, reverse=False)
def reverse_iter_sieve4prime_chunks_lt_(max1_u, /, *, with_interval=False):
    'max1_u/uint -> Iter [prime{<max1_u}]'
    check_int_ge(0, max1_u)
    return iter_sieve4prime_chunks_ge_lt_(0, max1_u, with_interval=with_interval, reverse=True)
def iter_sieve4prime_chunks_ge_lt_(min_u7whole, may_max1_u7whole, /, *, with_interval=False, reverse=False):
    'min_u7whole/uint -> may max1_u7whole/uint -> Iter [prime{>=min_u}]'
    check_int_ge(0, min_u7whole)
    if 1:
        # !! [fail:check_args4sieve_interval__ge_lt(2,3)]
        if min_u7whole <= 2:
            min_u7whole = 0
    for begin, end in iter_best_interval5big_interval6args4sieve_interval_(min_u7whole, may_max1_u7whole, reverse=reverse):
        chunk = sieve_interval4primes__ge_lt(begin, end)
        yield chunk if not with_interval else ((begin, end), chunk)




def _chain_chunks(it, min_u7whole, may_max1_u7whole, reverse, with_uint, /):
    if reverse:
        it = map(reversed, it)
    it = chains(it)
    if with_uint:
        if reverse:
            it = _with_uint7reversed(may_max1_u7whole, it)
        else:
            #bug:it = enumerate(it, max(1, min_u7whole))
            it = enumerate(it, max(0, min_u7whole))
    return it
def _with_uint7reversed(max1, it, /):
    for x in it:
        max1 -= 1
        yield (max1, x)

def iter_sieve4prime_factorss_ge_(min_u, /, *, with_uint=False):
    'min_u/uint -> Iter prime_factors/[prime]'
    return iter_sieve4prime_factorss_ge_lt_(min_u, None, reverse=False, with_uint=with_uint)
def reverse_iter_sieve4prime_factorss_lt_(max1_u, /, *, with_uint=False):
    'max1_u/uint -> Iter prime_factors/[prime]'
    return iter_sieve4prime_factorss_ge_lt_(0, max1_u, reverse=True, with_uint=with_uint)
def iter_sieve4prime_factorss_ge_lt_(min_u7whole, may_max1_u7whole, /, *, reverse=False, with_uint=False):
    'min_u7whole/uint -> may max1_u7whole/uint -> Iter prime_factors/[prime]'
    it = iter_sieve4prime_factors_chunks_ge_lt_(min_u7whole, may_max1_u7whole, reverse=reverse)
    return _chain_chunks(it, min_u7whole, may_max1_u7whole, reverse, with_uint)

def iter_sieve4prime_factors_chunks_ge_(min_u, /, *, with_interval=False):
    'min_u/uint -> Iter [prime_factors/[prime]]'
    return iter_sieve4prime_factors_chunks_ge_lt_(min_u, None, with_interval=with_interval, reverse=False)
def reverse_iter_sieve4prime_factors_chunks_lt_(max1_u, /, *, with_interval=False):
    'max1_u/uint -> Iter [prime_factors/[prime]]'
    check_int_ge(0, max1_u)
    return iter_sieve4prime_factors_chunks_ge_lt_(0, max1_u, with_interval=with_interval, reverse=True)
def iter_sieve4prime_factors_chunks_ge_lt_(min_u7whole, may_max1_u7whole, /, *, with_interval=False, reverse=False):
    'min_u7whole/uint -> may max1_u7whole/uint -> Iter [prime_factors/[prime]]'
    for begin, end in iter_best_interval5big_interval6args4sieve_interval_(min_u7whole, may_max1_u7whole, reverse=reverse):
        chunk = sieve_interval4prime_factors__ge_lt(begin, end)
        yield chunk if not with_interval else ((begin, end), chunk)



def iter_sieve4prime_factorizations_ge_(min_u, /, *, with_uint=False, Pmm_only=False):
    'min_u/uint -> Iter prime_factorization/{prime:exp}'
    return iter_sieve4prime_factorizations_ge_lt_(min_u, None, reverse=False, with_uint=with_uint, Pmm_only=Pmm_only)
def reverse_iter_sieve4prime_factorizations_lt_(max1_u, /, *, with_uint=False, Pmm_only=False):
    'max1_u/uint -> Iter prime_factorization/{prime:exp}'
    return iter_sieve4prime_factorizations_ge_lt_(0, max1_u, reverse=True, with_uint=with_uint, Pmm_only=Pmm_only)
def iter_sieve4prime_factorizations_ge_lt_(min_u7whole, may_max1_u7whole, /, *, reverse=False, with_uint=False, Pmm_only=False):
    'min_u7whole/uint -> may max1_u7whole/uint -> Iter prime_factorization/{prime:exp}'
    if Pmm_only:
        old_with_uint = with_uint
        with_uint = True
        if not None is may_max1_u7whole:
            may_max1_u7whole += 1
    it = iter_sieve4prime_factorization_chunks_ge_lt_(min_u7whole, may_max1_u7whole, reverse=reverse)
    it = _chain_chunks(it, min_u7whole, may_max1_u7whole, reverse, with_uint)
    if Pmm_only:
        it = _filter4pmm_(it, old_with_uint, reverse)
    return it
def _filter4pmm_(it, old_with_uint, reverse, /):
    f = reversed if reverse else iter

    for ab in pairwise(it):
        a, b = f(ab)
        (Nmm, p2e4Nmm) = a
        (N, p2e4N) = b
        if len(p2e4N) == 1 and 1 in p2e4N.values():
            yield (Nmm, p2e4Nmm) if old_with_uint else p2e4Nmm

    return
    r'''[[[
    for (Nmm, p2e4Nmm) in it:
        N = 1+Nmm
        if is_prime__via_complete_factorization_Nmm_(p2e4Nmm, N):
            yield (Nmm, p2e4Nmm) if old_with_uint else p2e4Nmm
    #]]]'''#'''



def iter_sieve4prime_factorization_chunks_ge_(min_u, /, *, with_interval=False):
    'min_u/uint -> Iter [prime_factorization/{prime:exp}]'
    return iter_sieve4prime_factorization_chunks_ge_lt_(min_u, None, with_interval=with_interval, reverse=False)
def reverse_iter_sieve4prime_factorization_chunks_lt_(max1_u, /, *, with_interval=False):
    'max1_u/uint -> Iter [prime_factorization/{prime:exp}]'
    check_int_ge(0, max1_u)
    return iter_sieve4prime_factorization_chunks_ge_lt_(0, max1_u, with_interval=with_interval, reverse=True)
def iter_sieve4prime_factorization_chunks_ge_lt_(min_u7whole, may_max1_u7whole, /, *, with_interval=False, reverse=False):
    'min_u7whole/uint -> may max1_u7whole/uint -> Iter [prime_factorization/{prime:exp}]'
    for begin, end in iter_best_interval5big_interval6args4sieve_interval_(min_u7whole, may_max1_u7whole, reverse=reverse):
        chunk = sieve_interval4prime_factorization__ge_lt(begin, end)
        yield chunk if not with_interval else ((begin, end), chunk)




def sieve_interval4primes__ge_lt(min_u, emay_max1_u, /):
    'min_u -> emay max1_u -> primes/[uint]{len<=max1_u-min_u} # [[0 == min_u <= max1_u] or [[1 <= min_u < max1_u][(max1_u-min_u)**2 >= -1+max1_u]]]'
    (min_u, max1_u) = to_std_args4sieve_interval__ge_lt(min_u, emay_max1_u)
    if 1:
        # !! [fail:check_args4sieve_interval__ge_lt(2,3)]
        min_u = 0 if min_u <= 2 else min_u
        777;check_args4sieve_interval__ge_lt(min_u, max1_u)
    if min_u >= 10 and max1_u <= 10*min_u:
        ps = core_sieve4primes__ge_le(min_u, max_u:=-1+max1_u, _mk=list)
    else:
        ps = list_all_strict_sorted_primes__lt_(max1_u, _mk=list)
        for j, p in enumerate(ps):
            if p >= min_u:
                ps = ps[j:]
                break
        else:
            ps = []
        ps
    ps
    return ps
def sieve_interval4offsetted_uint2is_prime__ge_lt(min_u, emay_max1_u, /):
    'min_u -> emay max1_u -> [is_prime/bool]{len==max1_u-min_u} # [[0 == min_u <= max1_u] or [[1 <= min_u < max1_u][(max1_u-min_u)**2 >= -1+max1_u]]]'
    (min_u, max1_u) = to_std_args4sieve_interval__ge_lt(min_u, emay_max1_u)
    check_args4sieve_interval__ge_lt(min_u, max1_u)
    if min_u >= 10 and max1_u <= 10*min_u:
        _u2b = core_sieve4offsetted_uint2is_prime__ge_le(min_u, max_u:=-1+max1_u)
    else:
        _u2b = sieve4uint2is_prime__lt_(max1_u, _mk=list)
        777;del _u2b[:min_u]
    return _u2b
def sieve_interval4prime_factorization__ge_lt(min_u, emay_max1_u, /, *, _validate=False):
    'min_u -> emay max1_u -> [{prime:exp}]{len==max1_u-min_u} # [[0 == min_u <= max1_u] or [[1 <= min_u < max1_u][(max1_u-min_u)**2 >= -1+max1_u]]]'
    (min_u, max1_u) = to_std_args4sieve_interval__ge_lt(min_u, emay_max1_u)
    check_args4sieve_interval__ge_lt(min_u, max1_u)
    if min_u >= 10 and max1_u <= 10*min_u:
        _u2p2e = core_sieve4prime_factorization__ge_le(min_u, max_u:=-1+max1_u, _validate=_validate)
            #core_sieve4pairs8prime_factorization__ge_le
    else:
        _u2p2e = tabulate_may_prime_factorization4uint_lt_(max1_u, _mk=list)
        777;del _u2p2e[:min_u]
    return _u2p2e
def sieve_interval4prime_factors__ge_lt(min_u, emay_max1_u, /, *, _validate=False):
    'min_u -> emay max1_u -> [[prime]]{len==max1_u-min_u} # [[0 == min_u <= max1_u] or [[1 <= min_u < max1_u][(max1_u-min_u)**2 >= -1+max1_u]]]'
    (min_u, max1_u) = to_std_args4sieve_interval__ge_lt(min_u, emay_max1_u)
    check_args4sieve_interval__ge_lt(min_u, max1_u)
    if min_u >= 10 and max1_u <= 10*min_u:
        _u2ps = core_sieve4prime_factors__ge_le(min_u, max_u:=-1+max1_u, _validate=_validate)
    else:
        _u2ps = tabulate_may_all_prime_factors4uint_lt_(max1_u, _mk=list)
            # tabulate_may_all_prime_factor_lflnkls4uint_lt_
        777;del _u2ps[:min_u]
    return _u2ps


def core_sieve4primes__ge_le(min_u, emay_max_u, /, *, _mk=tuple):
    'min_u -> emay max_u -> primes/[uint] # [primes==[p | [p::prime][min_u<=p<=max_u]]] # [min_u >= 10][min_u <= max_u < 10*min_u][(max_u+1-min_u)**2 >= max_u >= min_u]'
    (min_u, max_u) = to_std_args4core_sieve_interval__ge_le(min_u, emay_max_u)
    offsetted_u2b = core_sieve4offsetted_uint2is_prime__ge_le(min_u, max_u)
    return _mk(u for u, b in enumerate(offsetted_u2b, min_u) if b)
def core_sieve4offsetted_uint2is_prime__ge_le(min_u, emay_max_u, /):
    'min_u -> emay max_u -> offsetted_uint2is_prime/[is_prime/bool]{len==(max_u+1-min_u)} # [offsetted_uint2is_prime == [is_prime_(u) | [u:<-[min_u..=max_u]]]] # [min_u >= 10][min_u <= max_u < 10*min_u][(max_u+1-min_u)**2 >= max_u >= min_u]'
    #sieve4uint2is_prime__lt_
    (min_u, max_u) = to_std_args4core_sieve_interval__ge_le(min_u, emay_max_u)
    check_args4core_sieve_interval__ge_le(min_u, max_u)
    #floor_sqrt
    floor_sqrt4max_u = floor_sqrt(max_u)
    ps = list_all_strict_sorted_primes__lt_(1+floor_sqrt4max_u)
    max1_u = 1+max_u
    len_interval = max1_u-min_u
    _u2b = offsetted_u2b = [True]*len_interval
    neg0 = -min_u
    # [neg0 == -min_u]
    for p in ps:
        # [p <= floor_sqrt(max_u)]
        # !! [max_u < 10*min_u <= min_u**2]
        # [floor_sqrt(max_u) < min_u]
        # [p < min_u]

        #.u0 = min_u +neg0%p
        #.for u in range(u0, max1_u, p):
        #.    _u = u -min_u
        _u0 = neg0%p
        # [_u0 == (-min_u)%p]
        # [u0 := min_u+_u0]
        # [u0%p == (min_u+_u0)%p == 0]
        # !! [p < min_u]
        # [p < min_u <= u0]
        # [u0 > p]
        for _u in range(_u0, len_interval, p):
            # [_u >= _u0]
            # [_u%p == _u0%p]
            # [u := min_u+_u]
            # [u >= u0 > p]
            # [u%p == u0%p == 0]
            # [is_composite(u)]
            _u2b[_u] = False
    return offsetted_u2b

def core_sieve4prime_factorization__ge_le(min_u, emay_max_u, /, *, _validate=False):
    'min_u -> emay max_u -> prime_factorizations/[{prime:exp}] # [prime_factorizations==[prime_factorization4u | [u:<-[min_u..=max_u]][prime_factorization4u:={p: gde_(p;u) | [p::prime][u%p==0]}]]] # [min_u >= 10][min_u <= max_u < 10*min_u][(max_u+1-min_u)**2 >= max_u >= min_u]'
    #tabulate_may_prime_factorization4uint_lt_
    (min_u, max_u) = to_std_args4core_sieve_interval__ge_le(min_u, emay_max_u)
    _u2pes = offsetted_u2pe_pairs = core_sieve4pairs8prime_factorization__ge_le(min_u, max_u, _validate=_validate)
    _u2p2e = offsetted_u2p2e = _u2pes
    for _u in range(len(_u2pes)):
        _u2p2e[_u] = dict(_u2pes[_u])
    return offsetted_u2p2e
def core_sieve4pairs8prime_factorization__ge_le(min_u, emay_max_u, /, *, _with_exp=True, _validate=False):
    'min_u -> emay max_u -> prime_factor_gde_pairss/[[(uint,uint)]] # [prime_factor_gde_pairss==[prime_factor_gde_pairs4u | [u:<-[min_u..=max_u]][prime_factor_gde_pairs4u:=[(p, gde_(p;u)) | [p::prime][u%p==0]]]]] # [min_u >= 10][min_u <= max_u < 10*min_u][(max_u+1-min_u)**2 >= max_u >= min_u]'
    #old:core_sieve4prime_factor_gde_pairs__ge_le
    (min_u, max_u) = to_std_args4core_sieve_interval__ge_le(min_u, emay_max_u)
    offsetted_u2pe_pairs = core_sieve4prime_factors__ge_le(min_u, max_u, _with_exp=_with_exp, _validate=_validate)
    return offsetted_u2pe_pairs
def core_sieve4prime_factors__ge_le(min_u, emay_max_u, /, *, _with_exp=False, _validate=False):
    'min_u -> emay max_u -> prime_factorss/[[uint]] # [prime_factorss==[prime_factors4u | [u:<-[min_u..=max_u]][prime_factors4u:=[p | [p::prime][u%p==0]]]]] # [min_u >= 10][min_u <= max_u < 10*min_u][(max_u+1-min_u)**2 >= max_u >= min_u]'
    # tabulate_may_all_prime_factors4uint_lt_
    # tabulate_may_all_prime_factor_lflnkls4uint_lt_
    (min_u, max_u) = to_std_args4core_sieve_interval__ge_le(min_u, emay_max_u)
    check_args4core_sieve_interval__ge_le(min_u, max_u)
    #floor_sqrt
    floor_sqrt4max_u = floor_sqrt(max_u)
    ps = list_all_strict_sorted_primes__lt_(1+floor_sqrt4max_u)
    max1_u = 1+max_u
    len_interval = max1_u-min_u
    if _with_exp:
        _u2pes = offsetted_u2pe_pairs = [[] for _ in range(len_interval)]
    else:
        _u2ps = offsetted_u2ps = [[] for _ in range(len_interval)]
    _u2num_bits7remain = _mk_offsetted_u2num_bits7remain_(min_u, max1_u)
    # 不变量:[@[u:<-[min_u..=max_u]] -> [_u:=u-min_u] -> [(u///II[p**e | [(p,e):<-_u2pes[_u]]]) < 2**_u2num_bits7remain[_u]]]
    # 充分条件牜完全分解:[@[u:<-[min_u..=max_u]] -> [_u:=u-min_u] -> [2**_u2num_bits7remain[_u] <= floor_sqrt4max_u] -> [u == II[p**e | [(p,e):<-_u2pes[_u]]]]]
    # <==>充分条件牜完全分解:[@[u:<-[min_u..=max_u]] -> [_u:=u-min_u] -> [_u2num_bits7remain[_u] <= floor_log2(floor_sqrt4max_u)] -> [u == II[p**e | [(p,e):<-_u2pes[_u]]]]]
    #   若未必完全分解，则可能存在一个素因子q [u%q==0][q > ps[-1]]
    #



    #########
    max1_e4p = _u2num_bits7remain[-1] # == max_u.bit_length()
    neg0 = -min_u
    # [neg0 == -min_u]
    #########
    #params = (neg0, len_interval, _u2num_bits7remain, _with_exp, _u2pes, _u2ps)
    #########
    if _with_exp:
        def on_prime_power_(_u, pe, /):
            (p, e) = pe
            if e == 1:
                _u2pes[_u].append(None)
            _u2pes[_u][-1] = pe
        on_prime_power_
    else:
        def on_prime_power_(_u, pe, /):
            (p, e) = pe
            if e == 1:
                _u2ps[_u].append(p)
        on_prime_power_
    on_prime_power_
    #########
    _sieve_p_ = _mk_sieve_p_(neg0, len_interval, _u2num_bits7remain, on_prime_power_)
    #########
    for p in ps:
        # [p <= floor_sqrt(max_u)]
        # !! [max_u < 10*min_u <= min_u**2]
        # [floor_sqrt(max_u) < min_u]
        # [p < min_u]
        _sieve_p_(big:=False, p, max1_e4p)
    #########
    #_u2pes or _u2ps
    _u2num_bits7remain
    #########
    if _with_exp:
        def on_maybe_big_prime_q_(_u, /):
            u = min_u +_u
            v = II(p**e for p, e in _u2pes[_u])
            if not u == v:
                q = u//v
                assert u == q*v
                _1_or_q = q
            else:
                _1_or_q = 1
            _1_or_q
            return _1_or_q
        on_maybe_big_prime_q_
    else:
        def on_maybe_big_prime_q_(_u, /):
            u = min_u +_u
            (p2e, _1_or_q) = semi_factor_pint_via_trial_division(_u2ps[_u], u)
            return _1_or_q
        on_maybe_big_prime_q_
    on_maybe_big_prime_q_
    #########
    floor_log2_floor_sqrt4max_u = -1+floor_sqrt4max_u.bit_length() # == floor_log2(floor_sqrt4max_u)
    max1_e4q = 2 # at most 1
    #.for _u, num_bits7remain in enumerate(_u2num_bits7remain):
    #.    if num_bits7remain <= floor_log2_floor_sqrt4max_u:
    for _u in range(len_interval):
        if _u2num_bits7remain[_u] <= floor_log2_floor_sqrt4max_u:
            # !! 充分条件牜完全分解:[@[u:<-[min_u..=max_u]] -> [_u:=u-min_u] -> [_u2num_bits7remain[_u] <= floor_log2(floor_sqrt4max_u)] -> [u == II[p**e | [(p,e):<-_u2pes[_u]]]]]
            pass
        else:
            #.u = min_u +_u
            #.if _with_exp:
            #.    v = II(p**e for p, e in _u2pes[_u])
            #.    if not u == v:
            #.        q = u//v
            #.        assert u == q*v
            #.        #_u2pes[_u].append((q, 1))
            #.        _1_or_q = q
            #.    else:
            #.        _1_or_q = 1
            #.    _1_or_q
            #.else:
            #.    (p2e, _1_or_q) = semi_factor_pint_via_trial_division(_u2ps[_u], u)
            _1_or_q = on_maybe_big_prime_q_(_u)
            _1_or_q
            if not 1 == (q:=_1_or_q):
                assert q > floor_sqrt4max_u
                _sieve_p_(big:=True, q, max1_e4q)
                    # !! at most one more bigger prime q be appended
                    # => keep sorted order
                #assert _u2num_bits7remain[_u] <= floor_log2_floor_sqrt4max_u

    #########
    #_u2pes or _u2ps
    #########
    lss = _u2pes if _with_exp else _u2ps
    for _u in range(len_interval):
        lss[_u] = tuple(lss[_u])
    #########
    lss
    assert len(lss) == max_u+1-min_u
    if _validate:
        if _with_exp:
            check_offsetted_uint2pairs8prime_factorization_(min_u, _u2pes)
        else:
            check_offsetted_uint2prime_factors_(min_u, _u2ps)
    #########
    if _with_exp:
        return offsetted_u2pe_pairs
    return offsetted_u2ps
    #########
#end-def core_sieve4prime_factors__ge_le(min_u, max_u, /, *, _with_exp=False, _validate=False):
def _mk_sieve_p_(neg0, len_interval, _u2num_bits7remain, on_prime_power_, /):
    # [neg0 == -min_u]
    # from:core_sieve4prime_factors__ge_le
    # used in:tabulate_may_prime_factorization4uint_lt_#tabulate_may_factorization4uint_lt_
    # xxx:used in:tabulate_may_all_prime_factors4uint_lt_
    #########
    #.def _sieve_p_(params, big, p, max1_e, /):
    #.    (neg0, len_interval, _u2num_bits7remain, _with_exp, _u2pes, _u2ps) = params
    def _sieve_p_(big, p, max1_e, /):
        'offsetted:min_u#vs:_sieve_p_0_'

        # [not big] => [p < floor_sqrt(max_u) < min_u]
        # [big] => [p > floor_sqrt(max_u)]
        # [neg0 == -min_u]
        pw = 1 # p powers
        floor_log2_pw = 0 # == floor_log2(pw)
        for e in range(1, max1_e):
            pe = (p, e)
            pw *= p
            delta = (tmp:=-1+pw.bit_length()) -floor_log2_pw
            777; floor_log2_pw = tmp
            # [pw == p**e]
            # [floor_log2_pw == floor_log2(pw)]
            # [pw >= 2**floor_log2_pw]

            _u0 = neg0%pw
            if not _u0 < len_interval:
                break
            # [_u0 == (-min_u)%pw]
            # [u0 := min_u+_u0]
            # [u0%pw == (min_u+_u0)%pw == 0]
            # [u0%pw == 0]
            # !! [u0 >= min_u > 0]
            # [u0 >= pw >= p]
            # [not big]:
            #   !! [p < min_u]
            #   [p < min_u <= u0]
            #   [u0 > p]
            for _u in range(_u0, len_interval, pw):
                # [_u >= _u0]
                # [_u%pw == _u0%pw]
                # [u := min_u+_u]
                # [u >= u0 >= pw]
                # [u%pw == u0%pw == 0]
                # [not big]:
                #   !! [u0 > p]
                #   [is_composite(u)]
                # [is_prime_(u)] => [big]
                #########
                #.if _with_exp:
                #.    if e == 1:
                #.        _u2pes[_u].append(None)
                #.    _u2pes[_u][-1] = pe
                #.else:
                #.    if e == 1:
                #.        _u2ps[_u].append(p)
                on_prime_power_(_u, pe)
                #########
                _u2num_bits7remain[_u] -= delta
                # [_u2num_bits7remain[_u] == u.bit_length() -sum[-1+(p**e).bit_length() | [(p,e):<-_u2pes[_u]]]]
                # [_u2num_bits7remain[_u] == u.bit_length() -sum[floor_log2(pw) | [(p,e):<-_u2pes[_u]][pw:=p**e]]]
                # [2**_u2num_bits7remain[_u] == 2**u.bit_length() /II[2**floor_log2(pw) | [(p,e):<-_u2pes[_u]][pw:=p**e]]]
                # [2**_u2num_bits7remain[_u] > u /// II[pw | [(p,e):<-_u2pes[_u]][pw:=p**e]]]
                #   不变量
    #end-def _sieve_p_(big, p, max1_e, /):
    return _sieve_p_
    #########


__all__
from seed.math.prime_sieve.sieve_ge_le import calc_best_begin5end6args4sieve_interval_, iter_best_begins5end6args4sieve_interval_, calc_best_end5begin6args4sieve_interval_, iter_best_ends5begin6args4sieve_interval_, iter_best_interval5big_interval6args4sieve_interval_

from seed.math.prime_sieve.sieve_ge_le import calc_min_end5begin6args4sieve_interval_, test4calc_min_end5begin6args4sieve_interval_, iter_min_ends5begin6args4sieve_interval_
from seed.math.prime_sieve.sieve_ge_le import check_args4core_sieve_interval__ge_le, check_args4sieve_interval__ge_lt
from seed.math.prime_sieve.sieve_ge_le import to_std_args4core_sieve_interval__ge_le, to_std_args4sieve_interval__ge_lt

from seed.math.prime_sieve.sieve_ge_le import iter_primes_#===iter_primes__new_ver_
from seed.math.prime_sieve.sieve_ge_le import (
iter_sieve4prime_chunks_ge_lt_
,   iter_sieve4prime_chunks_ge_
,   reverse_iter_sieve4prime_chunks_lt_
,   iter_sieve4primes_ge_lt_
,       iter_sieve4primes_ge_
,       reverse_iter_sieve4primes_lt_
)
from seed.math.prime_sieve.sieve_ge_le import (
iter_sieve4prime_factors_chunks_ge_lt_
,   iter_sieve4prime_factors_chunks_ge_
,   reverse_iter_sieve4prime_factors_chunks_lt_
,   iter_sieve4prime_factorss_ge_lt_
,       iter_sieve4prime_factorss_ge_
,       reverse_iter_sieve4prime_factorss_lt_
)
from seed.math.prime_sieve.sieve_ge_le import (
iter_sieve4prime_factorization_chunks_ge_lt_
,   iter_sieve4prime_factorization_chunks_ge_
,   reverse_iter_sieve4prime_factorization_chunks_lt_
,   iter_sieve4prime_factorizations_ge_lt_
,       iter_sieve4prime_factorizations_ge_
,       reverse_iter_sieve4prime_factorizations_lt_
)


from seed.math.prime_sieve.sieve_ge_le import sieve_interval4primes__ge_lt, sieve_interval4offsetted_uint2is_prime__ge_lt, sieve_interval4prime_factorization__ge_lt, sieve_interval4prime_factors__ge_lt

from seed.math.prime_sieve.sieve_ge_le import core_sieve4primes__ge_le, core_sieve4offsetted_uint2is_prime__ge_le, core_sieve4prime_factorization__ge_le, core_sieve4pairs8prime_factorization__ge_le, core_sieve4prime_factors__ge_le

from seed.math.prime_sieve.sieve_ge_le import *
