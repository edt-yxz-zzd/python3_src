#__all__:goto
#doctest_end:goto
r'''[[[
e ../../python3_src/seed/math/primality_test/SPRP_2357.py
see also:
    view ../../python3_src/seed/math/factor_pint/perfect_power/detect_perfect_power.py
        detect_nonperfect_square__via_II8357_()

seed.math.primality_test.SPRP_2357
py -m nn_ns.app.debug_cmd   seed.math.primality_test.SPRP_2357 -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.primality_test.SPRP_2357:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/primality_test/reproduceable7probable_primes.py
]]


'#'; __doc__ = r'#'
>>> for n in range(-21, 22):print(n, detect_noncoprime_to_2357_(n), is_SPRP_2357_(n), sep=':')
-21:1:False
-20:1:False
-19:0:False
-18:1:False
-17:0:False
-16:1:False
-15:1:False
-14:1:False
-13:0:False
-12:1:False
-11:0:False
-10:1:False
-9:1:False
-8:1:False
-7:1:False
-6:1:False
-5:1:False
-4:1:False
-3:1:False
-2:1:False
-1:0:False
0:1:False
1:0:False
2:-1:True
3:-1:True
4:1:False
5:-1:True
6:1:False
7:-1:True
8:1:False
9:1:False
10:1:False
11:0:True
12:1:False
13:0:True
14:1:False
15:1:False
16:1:False
17:0:True
18:1:False
19:0:True
20:1:False
21:1:False

>>> [*filter4coprimes_to_2357_(range(-20, 200))]
[-19, -17, -13, -11, -1, 1, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 121, 127, 131, 137, 139, 143, 149, 151, 157, 163, 167, 169, 173, 179, 181, 187, 191, 193, 197, 199]
>>> [*filter4coprimes_to_2357_(range(-20, 200), neg_ok=False)]
[1, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 121, 127, 131, 137, 139, 143, 149, 151, 157, 163, 167, 169, 173, 179, 181, 187, 191, 193, 197, 199]
>>> [*filter4coprimes_to_2357_(range(-20, 200), in_2357_ok=True)]
[-19, -17, -13, -11, -1, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 121, 127, 131, 137, 139, 143, 149, 151, 157, 163, 167, 169, 173, 179, 181, 187, 191, 193, 197, 199]
>>> [*filter4coprimes_to_2357_(range(-20, 200), in_2357_ok=True, neg_ok=False)]
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 121, 127, 131, 137, 139, 143, 149, 151, 157, 163, 167, 169, 173, 179, 181, 187, 191, 193, 197, 199]

>>> _basis = (2,3,5,7)
>>> def show6diff_(n, /):
...     basis = _basis if n >= 9 else [base for base in _basis if base < n-1]
...     a = n == 2 or n > 2 and 1 == n&1 and is_strong_probable_prime__basis_(basis, n)
...     b = is_SPRP_2357_(n)
...     if not a is b:
...         print(n, a, b, sep=':')

>>> for n in range(-30, 3000):show6diff_(n)
>>> for n in range(2047-50, 2047+50):show6diff_(n)
>>> for n in range(1373653-50, 1373653+50):show6diff_(n)
>>> for n in range(25326001-50, 25326001+50):show6diff_(n)
>>> for n in range(3215031751-50, 3215031751+50):show6diff_(n)

>>> [*filter_SPRP_2357_(range(-200, 1+200))]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
>>> [*filter_SPRP_2357_(range(2047-50, 2047+50))]
[1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089]
>>> [*filter_SPRP_2357_(range(1373653-50, 1373653+50))]
[1373611, 1373627, 1373639, 1373677, 1373683, 1373689]
>>> [*filter_SPRP_2357_(range(25326001-50, 25326001+50))]
[25325969, 25325981, 25326023, 25326047]
>>> [*filter_SPRP_2357_(range(3215031751-50, 3215031751+50))]
[3215031733, 3215031749, 3215031751, 3215031767, 3215031773, 3215031791]




>>> next(iter_xprimes7SPRP_2357__ge_lt_(reverse=True))
Traceback (most recent call last):
    ...
TypeError: [reverse:=True][may_max1_u:=None]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(), 0, 20)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(-20), 0, 20)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+20), 0, 20)]
[23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+2, None), 0, 20)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+2, 2), 0, 20)]
[]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+2, 3), 0, 20)]
[2]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+2, 4), 0, 20)]
[2, 3]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+2, 5), 0, 20)]
[2, 3]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+2, 6), 0, 20)]
[2, 3, 5]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+3, 6), 0, 20)]
[3, 5]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+3, 6, reverse=True), 0, 20)]
[5, 3]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+2, 6, reverse=True), 0, 20)]
[5, 3, 2]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+1, 30), 0, 20)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+2, 30), 0, 20)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+3, 30), 0, 20)]
[3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+4, 30), 0, 20)]
[5, 7, 11, 13, 17, 19, 23, 29]








next_SPRP_2357__ge_
prev_may_SPRP_2357__lt_
>>> next_SPRP_2357__ge_(-3)
2
>>> next_SPRP_2357__ge_(1)
2
>>> next_SPRP_2357__ge_(2)
2
>>> next_SPRP_2357__ge_(3)
3
>>> next_SPRP_2357__ge_(4)
5
>>> next_SPRP_2357__ge_(5)
5

>>> prev_may_SPRP_2357__lt_(-3)
>>> prev_may_SPRP_2357__lt_(1)
>>> prev_may_SPRP_2357__lt_(2)
>>> prev_may_SPRP_2357__lt_(3)
2
>>> prev_may_SPRP_2357__lt_(4)
3
>>> prev_may_SPRP_2357__lt_(5)
3
>>> prev_may_SPRP_2357__lt_(6)
5
>>> prev_may_SPRP_2357__lt_(7)
5
>>> prev_may_SPRP_2357__lt_(8)
7














prepare4iter_xprimes7SPRP_2357__ge_lt_
    iter_2357__ge_lt_
    iter_coprimes7SPRP_2357__ge_lt_

>>> [*iter_2357__ge_lt_(-20, 20)]
[2, 3, 5, 7]
>>> [*iter_2357__ge_lt_(10, 20)]
[]
>>> [*iter_2357__ge_lt_(3, 3)]
[]
>>> [*iter_2357__ge_lt_(3, 5)]
[3]
>>> [*iter_2357__ge_lt_(6, 12)]
[7]

>>> [*iter_coprimes7SPRP_2357__ge_lt_(-20, 20)]
[-19, -17, -13, -11, -1, 1, 11, 13, 17, 19]
>>> [*iter_coprimes7SPRP_2357__ge_lt_(10, 20)]
[11, 13, 17, 19]
>>> [*iter_coprimes7SPRP_2357__ge_lt_(3, 3)]
[]
>>> [*iter_coprimes7SPRP_2357__ge_lt_(3, 5)]
[]
>>> [*iter_coprimes7SPRP_2357__ge_lt_(6, 12)]
[11]

>>> [*prepare4iter_xprimes7SPRP_2357__ge_lt_(-20, 20)]
[2, 3, 5, 7, 11, 13, 17, 19]
>>> [*prepare4iter_xprimes7SPRP_2357__ge_lt_(10, 20)]
[11, 13, 17, 19]
>>> [*prepare4iter_xprimes7SPRP_2357__ge_lt_(3, 3)]
[]
>>> [*prepare4iter_xprimes7SPRP_2357__ge_lt_(3, 5)]
[3]
>>> [*prepare4iter_xprimes7SPRP_2357__ge_lt_(6, 12)]
[7, 11]


.+1,.+22s/..$/, reverse=True\0
>>> [*iter_2357__ge_lt_(-20, 20, reverse=True)]
[7, 5, 3, 2]
>>> [*iter_2357__ge_lt_(10, 20, reverse=True)]
[]
>>> [*iter_2357__ge_lt_(3, 3, reverse=True)]
[]
>>> [*iter_2357__ge_lt_(3, 5, reverse=True)]
[3]
>>> [*iter_2357__ge_lt_(6, 12, reverse=True)]
[7]

>>> [*iter_coprimes7SPRP_2357__ge_lt_(-20, 20, reverse=True)]
[19, 17, 13, 11, 1, -1, -11, -13, -17, -19]
>>> [*iter_coprimes7SPRP_2357__ge_lt_(10, 20, reverse=True)]
[19, 17, 13, 11]
>>> [*iter_coprimes7SPRP_2357__ge_lt_(3, 3, reverse=True)]
[]
>>> [*iter_coprimes7SPRP_2357__ge_lt_(3, 5, reverse=True)]
[]
>>> [*iter_coprimes7SPRP_2357__ge_lt_(6, 12, reverse=True)]
[11]

>>> [*prepare4iter_xprimes7SPRP_2357__ge_lt_(-20, 20, reverse=True)]
[19, 17, 13, 11, 7, 5, 3, 2]
>>> [*prepare4iter_xprimes7SPRP_2357__ge_lt_(10, 20, reverse=True)]
[19, 17, 13, 11]
>>> [*prepare4iter_xprimes7SPRP_2357__ge_lt_(3, 3, reverse=True)]
[]
>>> [*prepare4iter_xprimes7SPRP_2357__ge_lt_(3, 5, reverse=True)]
[3]
>>> [*prepare4iter_xprimes7SPRP_2357__ge_lt_(6, 12, reverse=True)]
[11, 7]











>>> [*iter_Sophie_Germain_xprimes7SPRP_2357__ge_lt_(2, 1000)]
[2, 3, 5, 11, 23, 29, 41, 53, 83, 89, 113, 131, 173, 179, 191, 233, 239, 251, 281, 293, 359, 419, 431, 443, 491, 509, 593, 641, 653, 659, 683, 719, 743, 761, 809, 911, 953]


>>> [*iter_Sophie_Germain_xprimes7SPRP_2357__ge_lt_(-1000, 2)]
[]

>>> [*iter_Sophie_Germain_xprimes7SPRP_2357__ge_lt_(2, 100, reverse=True)]
[89, 83, 53, 41, 29, 23, 11, 5, 3, 2]










iter_Sophie_Germain_xprime_chains7SPRP_2357__len_eq__head_ge_lt_
    iter_Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_
        iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_
        mk_Sophie_Germain_xprime_chain5head7SPRP_2357_
            iter_Sophie_Germain_xprime_chain5head7SPRP_2357_



>>> [*iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_(2, 2, 100, reverse=True)]
[89, 83, 53, 41, 29, 23, 11, 5, 3, 2]

>>> [*iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_(3, 2, 1000)]
[2, 5, 11, 41, 89, 179, 359, 509, 719]

>>> [*iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_(4, 2, 1000)]
[2, 5, 89, 179, 359, 509]

>>> [*iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_(5, 2, 1000)]
[2, 89, 179]

>>> [*iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_(6, 2, 1000)]
[89]


>>> [*islice(iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_(6, 2, None, num_primes4neg_one6IIprimes_only=16, num_primes4trial_division=32), 0, 3)]  #doctest: +SKIP
[8612271732450058740707639, 10145102801424692494583189, 11572344996933230503533539]


>>> [*islice(iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_(6, 2, None, num_primes4neg_one6IIprimes_only=8, num_primes4trial_division=32), 0, 3)]  #doctest: +SKIP
[41485574129, 83252439269, 366725879519]

>>> [*islice(iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_(6, 2, None, num_primes4neg_one6IIprimes_only=4, num_primes4trial_division=16), 0, 3)]  #doctest: +SKIP
[63419, 810809, 1122659]

>>> [*islice(iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_(4, 2, None, num_primes4neg_one6IIprimes_only=4, num_primes4trial_division=16), 0, 3)]
[11549, 55229, 63419]



>>> mk_Sophie_Germain_xprime_chain5head7SPRP_2357_(-1)
()
>>> mk_Sophie_Germain_xprime_chain5head7SPRP_2357_(7)
(7,)
>>> mk_Sophie_Germain_xprime_chain5head7SPRP_2357_(7, min4len4chain=2)
Traceback (most recent call last):
    ...
seed.math.primality_test.SPRP_2357.Error__Sophie_Germain_xprime_chain__too_short: (7, 2, 1)
>>> mk_Sophie_Germain_xprime_chain5head7SPRP_2357_(2)
(2, 5, 11, 23, 47)
>>> mk_Sophie_Germain_xprime_chain5head7SPRP_2357_(89)
(89, 179, 359, 719, 1439, 2879)
>>> mk_Sophie_Germain_xprime_chain5head7SPRP_2357_(11549)
(11549, 23099, 46199, 92399)


>>> [*iter_Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_(2, 2, 100, reverse=True)]
[(89, 179, 359, 719, 1439, 2879), (83, 167), (53, 107), (41, 83, 167), (29, 59), (23, 47), (11, 23, 47), (5, 11, 23, 47), (3, 7), (2, 5, 11, 23, 47)]

>>> [*iter_Sophie_Germain_xprime_chains7SPRP_2357__len_eq__head_ge_lt_(2, 2, 100)]
[(2, 5), (3, 7), (5, 11), (11, 23), (23, 47), (29, 59), (41, 83), (53, 107), (83, 167), (89, 179)]











#doctest_end:here

[[
py_adhoc_call   seed.math.primality_test.SPRP_2357   @bytes.filter4coprimes_to_2357_ '=range(210)' -in_2357_ok
py_adhoc_call   seed.math.primality_test.SPRP_2357   @_mk_coprimes6wheel_2357
    b'\x01\x0b\r\x11\x13\x17\x1d\x1f%)+/5;=CGIOSYaegkmqy\x7f\x83\x89\x8b\x8f\x95\x97\x9d\xa3\xa7\xa9\xad\xb3\xb5\xbb\xbf\xc1\xc5\xc7\xd1'
]]

[[
py_adhoc_call   seed.math.primality_test.SPRP_2357   @test4iter_coprimes7SPRP_2357__ge_lt_
    ok!
]]



py_adhoc_call   seed.math.primality_test.SPRP_2357   @f
]]]'''#'''
__all__ = r'''
is_SPRP_2357_
    filter_SPRP_2357_
        iter_xprimes7SPRP_2357__ge_lt_
            next_SPRP_2357__ge_
            prev_may_SPRP_2357__lt_
detect_noncoprime_to_2357_
    filter4coprimes_to_2357_



iter_xprimes7SPRP_2357__ge_lt_
    prepare4iter_xprimes7SPRP_2357__ge_lt_
        iter_2357__ge_lt_
        iter_coprimes7SPRP_2357__ge_lt_
iter_Sophie_Germain_xprimes7SPRP_2357__ge_lt_

iter_Sophie_Germain_xprime_chains7SPRP_2357__len_eq__head_ge_lt_
    iter_Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_
        iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_
        mk_Sophie_Germain_xprime_chain5head7SPRP_2357_
            iter_Sophie_Germain_xprime_chain5head7SPRP_2357_
                Error__Sophie_Germain_xprime_chain__too_short







II_2357
bs_2357
II_357
bs_357


coprimes6wheel_2357
    fwd_gaps6wheel_2357
    u2whether_coprime6wheel_2357
    u2idx4coprime6wheel_2357
    u2fwd_gap6wheel_2357
    u2bwd_gap6wheel_2357

test4iter_coprimes7SPRP_2357__ge_lt_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.primality_test.strong_probable_prime import is_strong_probable_prime__basis_
    from seed.tiny_.check import check_type_is, check_int_ge, check_may_
    from itertools import count, islice, pairwise, chain, cycle, product#accumulate
    from seed.seq_tools.iter_seq_range import seq_islice
    #def seq_islice(seq, begin ,end, step=None, *, reverse=False):
    from seed.tiny_.count_ import iter_ints__ge_lt_ # count_, iter_ints__from_to_



####################################
###iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_
####################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.prime_sieve.PrimeList import PrimeList
    from seed.math.II import II
    from bisect import bisect_left, bisect_right
    from seed.math.primality_test.strong_probable_prime import is_strong_probable_prime_
    from seed.tiny_.types5py import curry1
    from seed.debug.print_err import print_err
    from seed.excepts.repack_exception_ import repack_exception_, repack_exception7new_subclass_
with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
    from seed.math.primality_test.strong_probable_prime import A014233
####################################

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

r'''[[[
[[
py_adhoc_call   seed.math.primality_test.SPRP_2357   ,iter_xprimes7SPRP_2357__ge_lt_ ='2**32' | more
py_adhoc_call   seed.math.primality_test.SPRP_2357   ,iter_xprimes7SPRP_2357__ge_lt_ ='2**32' | head -n 50
4294967311
4294967357
4294967371
4294967377
4294967387
4294967389
4294967459
4294967477
4294967497
4294967513
4294967539
4294967543
4294967549
4294967561
4294967563
4294967569
4294967597
4294967627
4294967639
4294967653
4294967681
4294967687
4294967701
4294967723
4294967759
4294967779
4294967783
4294967791
4294967797
4294967821
4294967857
4294967861
4294967867
4294967891
4294967969
4294967977
4294967983
4294968001
4294968017
4294968019
4294968023
4294968059
4294968101
4294968127
4294968143
4294968149
4294968173
4294968187
4294968199
4294968211


[(4294968211-2**32)/50 == 18.3]
]]
[[
(1+2*Sophie_Germain_prime):hard modulus for discrete_logarithm
    view ../../python3_src/seed/math/discrete_logarithm__7cyclic_group7kth_roots.py
==>>:
Sophie_Germain_SPRP_2357

py_adhoc_call   seed.math.primality_test.SPRP_2357   ,iter_Sophie_Germain_xprimes7SPRP_2357__ge_lt_ ='2**32' | more
py_adhoc_call   seed.math.primality_test.SPRP_2357   ,iter_Sophie_Germain_xprimes7SPRP_2357__ge_lt_ ='2**32' | head -n 50
4294967681
4294967861
4294968101
4294968239
4294968329
4294968371
4294968521
4294968869
4294968929
4294971221
4294971269
4294971431
4294971491
4294971563
4294972151
4294972481
4294972613
4294972859
4294973069
4294973549
4294973603
4294973999
4294974083
4294974581
4294974641
4294974731
4294974923
4294975043
4294975673
4294976051
4294976069
4294976321
4294976519
4294976579
4294976981
4294977023
4294977083
4294977161
4294977233
4294977311
4294978283
4294978553
4294978679
4294979009
4294979081
4294979159
4294979471
4294979519
4294979693
4294979891


[(4294979891-2**32)/50 == 251.9]
    vs:[(4294968211-2**32)/50 == 18.3]
    [18**2 == 324 ~= 251]
]]
[[
py_adhoc_call   seed.math.primality_test.SPRP_2357   ,9:iter_Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_  =4 --num_primes4neg_one6IIprimes_only=16
    (37803423833540451886799, 75606847667080903773599, 151213695334161807547199, 302427390668323615094399)
    (139090528380647110907639, 278181056761294221815279, 556362113522588443630559, 1112724227045176887261119)
    (166758723927781458883409, 333517447855562917766819, 667034895711125835533639, 1334069791422251671067279)
    (257454351969801353366999, 514908703939602706733999, 1029817407879205413467999, 2059634815758410826935999)
    (343457141191105881409469, 686914282382211762818939, 1373828564764423525637879, 2747657129528847051275759)
    (363564651971532139007879, 727129303943064278015759, 1454258607886128556031519, 2908517215772257112063039)
    (392992662076434749399069, 785985324152869498798139, 1571970648305738997596279, 3143941296611477995192559)
    (499819923564663716024009, 999639847129327432048019, 1999279694258654864096039, 3998559388517309728192079)
    (610623062387109868106009, 1221246124774219736212019, 2442492249548439472424039, 4884984499096878944848079)

]]
[[
py_adhoc_call   seed.math.primality_test.SPRP_2357   ,9:iter_Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_  =9 --num_primes4neg_one6IIprimes_only=16
    ^KeyboardInterrupt
    ++print_err
    ++repack_exception_

]]
[[
py_adhoc_call   seed.math.primality_test.SPRP_2357   ,9:iter_Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_  =9 --num_primes4neg_one6IIprimes_only=8
    ^KeyboardInterrupt: (KeyboardInterrupt(), ('iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_()@', 7618379018249))
]]
[[
py_adhoc_call   seed.math.primality_test.SPRP_2357   ,9:iter_Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_  =7 --num_primes4neg_one6IIprimes_only=8
    (2503218397679, 5006436795359, 10012873590719, 20025747181439, 40051494362879, 80102988725759, 160205977451519)
    (4248299325269, 8496598650539, 16993197301079, 33986394602159, 67972789204319, 135945578408639, 271891156817279)
    (5449741727429, 10899483454859, 21798966909719, 43597933819439, 87195867638879, 174391735277759, 348783470555519, 697566941111039)
    (7370988424799, 14741976849599, 29483953699199, 58967907398399, 117935814796799, 235871629593599, 471743259187199)
    (7688304083459, 15376608166919, 30753216333839, 61506432667679, 123012865335359, 246025730670719, 492051461341439)
    (10899483454859, 21798966909719, 43597933819439, 87195867638879, 174391735277759, 348783470555519, 697566941111039)
    (11047044838829, 22094089677659, 44188179355319, 88376358710639, 176752717421279, 353505434842559, 707010869685119)
    (13442189290529, 26884378581059, 53768757162119, 107537514324239, 215075028648479, 430150057296959, 860300114593919)
    (17825993285099, 35651986570199, 71303973140399, 142607946280799, 285215892561599, 570431785123199, 1140863570246399)
==>>:
    [sz==8]:(5449741727429, 10899483454859, 21798966909719, 43597933819439, 87195867638879, 174391735277759, 348783470555519, 697566941111039)
]]



#]]]'''#'''









__all__
#A014233_7fst_four = (2047, 1373653, 25326001, 3215031751)
II_2357 = 210 # == 2*3*5*7
bs_2357 = b'\2\3\5\7'
II_357 = 105 # == 3*5*7
bs_357 = b'\3\5\7'
def detect_noncoprime_to_2357_(n, /):
    'int -> (-1/in_2357|0/coprime|+1/noncoprime)'
    #assert n >= 0
    if n&1 == 0:
        return -1 if n == 2 else +1
    # [1 == n%2]
    #new:
    if 8 > n > 2:
        # !! [1 == n%2]
        # [n <- {3,5,7}]
        return -1
    u = n % II_2357
    return 0 if u2whether_coprime6wheel_2357[u] else +1

    #old:
    u = n % II_357
    if u in bs_357:
        return -1 if n == u else +1
    return +1 if any(u%d == 0 for d in bs_357) else 0

    #.u = n % II_2357
    #.if u in bs_2357:
    #.    return -1 if n == u else +1
    #.return +1 if any(u%d == 0 for d in bs_2357) else 0

def filter4coprimes_to_2357_(ns, /, *, in_2357_ok=False, neg_ok=True):
    for n in ns:
        match detect_noncoprime_to_2357_(n):
            case 0:
                # coprime
                if neg_ok or n > 0:
                    yield n
            case 1:
                # noncoprime and not in_2357
                pass
            case -1:
                # in_2357
                if in_2357_ok:
                    yield n
                pass
            case _:
                raise 000

def filter_SPRP_2357_(ns, /):
    'Iter int -> Iter uint{is_SPRP_2357_}'
    return filter(is_SPRP_2357_, ns)
def is_SPRP_2357_(n, /):
    'n/int -> bool{== [n>=2][[is_prime_(n)]or[1==gcd(n,210)][7 < n-1][is_strong_probable_prime__basis_([2,3,5,7],n)]]}'
    if 1:
        'int -> bool'
        check_type_is(int, n)
        if n < 2:
            return False
        # [2 <= n]
    else:
        'pint -> bool'
        check_int_ge(1, n)
        # [1 <= n]
    # [1 <= n]
    ######################
    match detect_noncoprime_to_2357_(n):
        case 0:
            # coprime
            # [1 == gcd(n, 210)]
            pass
        case 1:
            # noncoprime and not in_2357
            return False
        case -1:
            # in_2357
            # [is_prime_(n)]
            return True
        case _:
            raise 000
    # [1 <= n]
    # [1 == gcd(n, 210)]
    ######################
    if n < 121:
        # [1 <= n < 11**2]
        # [1 <= sqrt(n) < 11]
        # [[is_composite_(n)] -> [min_prime_factor{n} <= 7]]
        # !! [1 == gcd(n, 210)]
        # [not$is_composite_(n)]
        # [[n==1]or[is_prime_(n)]]
        # [[n=!=1] -> [is_prime_(n)]]
        return not n == 1
    # [121 <= n]
    # [1 == gcd(n, 210)]
    ######################
    # [n%2 =!= 0]
    # [n%3 =!= 0]
    # [n%5 =!= 0]
    # [n%7 =!= 0]
    # [max(bs_2357) == 7 < n-1]
    # ==>> precondition{is_strong_probable_prime__basis_}
    ######################
    #A014233_7fst_three = (2047, 1373653, 25326001)
    if n < 1373653:
        if n < 2047:
            basis = b'\2'
        else:
            basis = b'\2\3'
    else:
        if n < 25326001:
            basis = b'\2\3\5'
        else:
            basis = b'\2\3\5\7'
    basis
    ######################
    return is_strong_probable_prime__basis_(basis, n)
    ######################



















__all__
####################################
#prepare_data:begin
####################################
#wheel_2357
def _mk_coprimes6wheel_2357():
    return bytes(filter4coprimes_to_2357_(range(II_2357), in_2357_ok=False))
def _mk_fwd_gaps6wheel_2357(coprimes6wheel_2357, /):
    return bytes(chain((b-a for a, b in pairwise(coprimes6wheel_2357)), [2]))
def _mk_bwd_gaps6wheel_2357(fwd_gaps6wheel_2357, /):
    return fwd_gaps6wheel_2357[-1:] + fwd_gaps6wheel_2357[:-1]
def _mk_u2whether_coprime6wheel_2357(coprimes6wheel_2357, /):
    ls = [False]*II_2357
    for u in coprimes6wheel_2357:
        ls[u] = True
    return bytes(ls)
def _mk_u2idx4coprime6wheel_2357(coprimes6wheel_2357, /):
    #xxx:accumulate(u2whether_coprime6wheel_2357)
    ls = [255]*II_2357
    for j, u in enumerate(coprimes6wheel_2357):
        ls[u] = j
    return bytes(ls)
def _mk_u2fwd_gap6wheel_2357(coprimes6wheel_2357, /):
    ls = [None]*II_2357
    for a, b in pairwise(coprimes6wheel_2357):
        for u in range(a, b):
            ls[u] = b-u
    ls[-1] = 2
    ls[0] = 1
    return bytes(ls)
def _mk_u2bwd_gap6wheel_2357(coprimes6wheel_2357, /):
    ls = [None]*II_2357
    for a, b in pairwise(coprimes6wheel_2357):
        for u in range(1+a, 1+b):
            ls[u] = u-a
    ls[1] = 2
    ls[0] = 1
    return bytes(ls)
def _mk_u2next_coprime6wheel_2357(coprimes6wheel_2357, /):
    ls = [None]*II_2357
    for a, b in pairwise(coprimes6wheel_2357):
        for u in range(a, b):
            ls[u] = b
    ls[-1] = ls[0] = 1
    return bytes(ls)
def _mk_u2prev_coprime6wheel_2357(coprimes6wheel_2357, /):
    ls = [None]*II_2357
    for a, b in pairwise(coprimes6wheel_2357):
        for u in range(1+a, 1+b):
            ls[u] = a
    ls[1] = ls[0] = II_2357-1
    return bytes(ls)

if 0b0000:
    coprimes6wheel_2357 = _mk_coprimes6wheel_2357()
    assert len(coprimes6wheel_2357) == 1*2*4*6 == 48
    fwd_gaps6wheel_2357 = _mk_fwd_gaps6wheel_2357(coprimes6wheel_2357)
    #bwd_gaps6wheel_2357 = _mk_bwd_gaps6wheel_2357(fwd_gaps6wheel_2357)
    u2whether_coprime6wheel_2357 = _mk_u2whether_coprime6wheel_2357(coprimes6wheel_2357)
    u2idx4coprime6wheel_2357 = _mk_u2idx4coprime6wheel_2357(coprimes6wheel_2357)
    u2fwd_gap6wheel_2357 = _mk_u2fwd_gap6wheel_2357(coprimes6wheel_2357)
    u2bwd_gap6wheel_2357 = _mk_u2bwd_gap6wheel_2357(coprimes6wheel_2357)
    #u2next_coprime6wheel_2357 = _mk_u2next_coprime6wheel_2357(coprimes6wheel_2357)
    #u2prev_coprime6wheel_2357 = _mk_u2prev_coprime6wheel_2357(coprimes6wheel_2357)
if 0b0000:
    # .,.+6s/\w\+/print('\0 = ', \0)
    print('coprimes6wheel_2357 = ', coprimes6wheel_2357)
    print('fwd_gaps6wheel_2357 = ', fwd_gaps6wheel_2357)
    print('u2whether_coprime6wheel_2357 = ', u2whether_coprime6wheel_2357)
    print('u2idx4coprime6wheel_2357 = ', u2idx4coprime6wheel_2357)
    print('u2fwd_gap6wheel_2357 = ', u2fwd_gap6wheel_2357)
    print('u2bwd_gap6wheel_2357 = ', u2bwd_gap6wheel_2357)

if 0b0001:
    coprimes6wheel_2357 =  b'\x01\x0b\r\x11\x13\x17\x1d\x1f%)+/5;=CGIOSYaegkmqy\x7f\x83\x89\x8b\x8f\x95\x97\x9d\xa3\xa7\xa9\xad\xb3\xb5\xbb\xbf\xc1\xc5\xc7\xd1'
    fwd_gaps6wheel_2357 =  b'\n\x02\x04\x02\x04\x06\x02\x06\x04\x02\x04\x06\x06\x02\x06\x04\x02\x06\x04\x06\x08\x04\x02\x04\x02\x04\x08\x06\x04\x06\x02\x04\x06\x02\x06\x06\x04\x02\x04\x06\x02\x06\x04\x02\x04\x02\n\x02'
    u2whether_coprime6wheel_2357 =  b'\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x01\x00\x00\x00\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x01\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
    u2idx4coprime6wheel_2357 =  b'\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\xff\x02\xff\xff\xff\x03\xff\x04\xff\xff\xff\x05\xff\xff\xff\xff\xff\x06\xff\x07\xff\xff\xff\xff\xff\x08\xff\xff\xff\t\xff\n\xff\xff\xff\x0b\xff\xff\xff\xff\xff\x0c\xff\xff\xff\xff\xff\r\xff\x0e\xff\xff\xff\xff\xff\x0f\xff\xff\xff\x10\xff\x11\xff\xff\xff\xff\xff\x12\xff\xff\xff\x13\xff\xff\xff\xff\xff\x14\xff\xff\xff\xff\xff\xff\xff\x15\xff\xff\xff\x16\xff\x17\xff\xff\xff\x18\xff\x19\xff\xff\xff\x1a\xff\xff\xff\xff\xff\xff\xff\x1b\xff\xff\xff\xff\xff\x1c\xff\xff\xff\x1d\xff\xff\xff\xff\xff\x1e\xff\x1f\xff\xff\xff \xff\xff\xff\xff\xff!\xff"\xff\xff\xff\xff\xff#\xff\xff\xff\xff\xff$\xff\xff\xff%\xff&\xff\xff\xff\'\xff\xff\xff\xff\xff(\xff)\xff\xff\xff\xff\xff*\xff\xff\xff+\xff,\xff\xff\xff-\xff.\xff\xff\xff\xff\xff\xff\xff\xff\xff/'
    u2fwd_gap6wheel_2357 =  b'\x01\n\t\x08\x07\x06\x05\x04\x03\x02\x01\x02\x01\x04\x03\x02\x01\x02\x01\x04\x03\x02\x01\x06\x05\x04\x03\x02\x01\x02\x01\x06\x05\x04\x03\x02\x01\x04\x03\x02\x01\x02\x01\x04\x03\x02\x01\x06\x05\x04\x03\x02\x01\x06\x05\x04\x03\x02\x01\x02\x01\x06\x05\x04\x03\x02\x01\x04\x03\x02\x01\x02\x01\x06\x05\x04\x03\x02\x01\x04\x03\x02\x01\x06\x05\x04\x03\x02\x01\x08\x07\x06\x05\x04\x03\x02\x01\x04\x03\x02\x01\x02\x01\x04\x03\x02\x01\x02\x01\x04\x03\x02\x01\x08\x07\x06\x05\x04\x03\x02\x01\x06\x05\x04\x03\x02\x01\x04\x03\x02\x01\x06\x05\x04\x03\x02\x01\x02\x01\x04\x03\x02\x01\x06\x05\x04\x03\x02\x01\x02\x01\x06\x05\x04\x03\x02\x01\x06\x05\x04\x03\x02\x01\x04\x03\x02\x01\x02\x01\x04\x03\x02\x01\x06\x05\x04\x03\x02\x01\x02\x01\x06\x05\x04\x03\x02\x01\x04\x03\x02\x01\x02\x01\x04\x03\x02\x01\x02\x01\n\t\x08\x07\x06\x05\x04\x03\x02\x01\x02'
    u2bwd_gap6wheel_2357 =  b'\x01\x02\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x01\x02\x01\x02\x03\x04\x01\x02\x01\x02\x03\x04\x01\x02\x03\x04\x05\x06\x01\x02\x01\x02\x03\x04\x05\x06\x01\x02\x03\x04\x01\x02\x01\x02\x03\x04\x01\x02\x03\x04\x05\x06\x01\x02\x03\x04\x05\x06\x01\x02\x01\x02\x03\x04\x05\x06\x01\x02\x03\x04\x01\x02\x01\x02\x03\x04\x05\x06\x01\x02\x03\x04\x01\x02\x03\x04\x05\x06\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x01\x02\x01\x02\x03\x04\x01\x02\x01\x02\x03\x04\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x01\x02\x03\x04\x01\x02\x03\x04\x05\x06\x01\x02\x01\x02\x03\x04\x01\x02\x03\x04\x05\x06\x01\x02\x01\x02\x03\x04\x05\x06\x01\x02\x03\x04\x05\x06\x01\x02\x03\x04\x01\x02\x01\x02\x03\x04\x01\x02\x03\x04\x05\x06\x01\x02\x01\x02\x03\x04\x05\x06\x01\x02\x03\x04\x01\x02\x01\x02\x03\x04\x01\x02\x01\x02\x03\x04\x05\x06\x07\x08\t\n'

####################################
#prepare_data:end
####################################
__all__



def test4iter_coprimes7SPRP_2357__ge_lt_():
    ns = range(-1-II_2357, +2+II_2357)
    for reverse, min_u, max1_u in product([False, True], ns, ns):
        ns0 = [*iter_coprimes7SPRP_2357__ge_lt_(min_u, max1_u, reverse=reverse, native=False)]
        ns1 = [*iter_coprimes7SPRP_2357__ge_lt_(min_u, max1_u, reverse=reverse, native=True)]
        assert ns0 == ns1, (reverse, min_u, max1_u)

def iter_coprimes7SPRP_2357__ge_lt_(may_min_u, may_max1_u, /, *, reverse=False, native=False):
    '-> Iter i/coprime_2357/int{[1==gcd(i,2*3*5*7)]}'
    #see:filter4coprimes_to_2357_
    #see:prepare4iter_xprimes7SPRP_2357__ge_lt_
    ###########################
    if native:
        ws = iter_ints__ge_lt_(may_min_u, may_max1_u, reverse=reverse)
        return filter4coprimes_to_2357_(ws, in_2357_ok=False, neg_ok=True)
    ###########################
    check_may_([check_type_is, int], may_min_u)
    check_may_([check_type_is, int], may_max1_u)

    if reverse:
        #if may_max1_u is None:raise TypeError('reverse and may_max1_u is None')
        if may_max1_u is None:raise TypeError('[reverse:=True][may_max1_u:=None]')
        min_n = 1-may_max1_u
        may_max1_n = None if may_min_u is None else 1-may_min_u
        it = _iter_coprimes7SPRP_2357__ge_lt_(min_n, may_max1_n)
        it = map(int.__neg__, it)
    else:
        #if may_min_u is None:raise TypeError('not reverse and may_min_u is None')
        if may_min_u is None:raise TypeError('[reverse:=False][may_min_u:=None]')
        min_u = may_min_u
        it = _iter_coprimes7SPRP_2357__ge_lt_(min_u, may_max1_u)
    it
    return it
def _iter_coprimes7SPRP_2357__ge_lt_(min_u, may_max1_u, /):
    if not may_max1_u is None:
        max1_u = may_max1_u
        if not min_u < max1_u:
            return

    min_u6wheel = min_u%II_2357
    if not u2whether_coprime6wheel_2357[min_u6wheel]:
        min_u += u2fwd_gap6wheel_2357[min_u6wheel]
        min_u6wheel += u2fwd_gap6wheel_2357[min_u6wheel]
        min_u6wheel %= II_2357
    min_u6wheel
    min_u
    #777;min_u6wheel = None
    # [1==gcd(min_u, II_2357)]

    if not may_max1_u is None:
        max_u6wheel = (max1_u-1)%II_2357
        if not u2whether_coprime6wheel_2357[max_u6wheel]:
            max1_u -= u2bwd_gap6wheel_2357[max_u6wheel]
            #max_u6wheel -= u2bwd_gap6wheel_2357[max_u6wheel]
            #max_u6wheel %= II_2357
        max1_u
        777;max_u6wheel = None
        # [1==gcd(-1+max1_u, II_2357)]

        if not min_u < max1_u:
            return
        # [min_u < max1_u]

        max_u = -1+max1_u
        # [1==gcd(max_u, II_2357)]
        # [min_u <= max_u]
        may_max_u = max_u
    else:
        may_max_u = None
    may_max_u

    # [not may_max_u is None] => [min_u <= max_u]
    # [not may_max_u is None] => [1==gcd(max_u, II_2357)]
    # [1==gcd(min_u, II_2357)]

    min_u6wheel
    min_u
    j4min_u = u2idx4coprime6wheel_2357[min_u6wheel]
    gaps = seq_islice(fwd_gaps6wheel_2357, j4min_u, None)
    777;gaps = chain(gaps, cycle(fwd_gaps6wheel_2357))

    u = min_u
    # [1==gcd(u, II_2357)]
    # [not may_max_u is None] => [u <= max_u]
    for gap in gaps:
        # [1==gcd(u, II_2357)]
        # [not may_max_u is None] => [u <= max_u]
        yield u
        if may_max_u == u:
            break
        # [not may_max_u is None] => [u < max_u]
        u += gap
        # [not may_max_u is None] => [u <= max_u]
    return
#_null_iter = iter('')
def iter_2357__ge_lt_(min_u=2, may_max1_u=None, /, *, reverse=False):
    '-> Iter u/uint{[u <- {2,3,5,7}]}'
    check_may_([check_type_is, int], may_max1_u)
    check_type_is(int, min_u)
    min_u = max(2, min_u)
    # [min_u >= 2]
    max1_u = may_max1_u if not may_max1_u is None else 8
    max1_u = min(8, max1_u)
    # [max1_u <= 8]
    if not min_u < max1_u:
        return
    # [2 <= min_u < max1_u <= 8]
    us = bs_2357
    if reverse:
        us = reversed(us)
    us
    for u in us:
        if min_u <= u < max1_u:
            yield u
    return

def prepare4iter_xprimes7SPRP_2357__ge_lt_(min_u=2, may_max1_u=None, /, *, reverse=False, native=False):
    '-> Iter u/uint{[u >= 2][[u <- {2,3,5,7}]or[1==gcd(u,2*3*5*7)]]}' \
    '  # vs:iter_coprimes7SPRP_2357__ge_lt_():this func include 2357'
    check_type_is(int, min_u)
    min_u = max(2, min_u)
    # [min_u >= 2]
    us7in2357 = iter_2357__ge_lt_(min_u, may_max1_u, reverse=reverse)

    # !! [min_u >= 2]
    us7gt2357 = iter_coprimes7SPRP_2357__ge_lt_(min_u, may_max1_u, reverse=reverse, native=native)
        # required:[min_u >= 2]

    uss = [us7in2357, us7gt2357]
    if reverse:
        uss = reversed(uss)
    uss
    return chain(*uss)

def iter_xprimes7SPRP_2357__ge_lt_(min_u=2, may_max1_u=None, /, *, reverse=False, native=False):
    '-> Iter SPRP_2357'
    #new:
    us = prepare4iter_xprimes7SPRP_2357__ge_lt_(min_u, may_max1_u, reverse=reverse, native=native)
    return filter_SPRP_2357_(us)
def __():
    #old:
  def iter_xprimes7SPRP_2357__ge_lt_(min_u=2, may_max1_u=None, /, *, reverse=False):
    check_type_is(int, min_u)
    min_u = max(2, min_u)
    #bug:odd_min_u = max(3, min_u)
    odd_min_u = 1|min_u
    match may_max1_u:
        case None:
            # +oo
            odd_us = count(odd_min_u, 2)
            if reverse:raise TypeError('[reverse:=True][may_max1_u:=None]')
            # [[reverse] -> [odd_us :: reversed]]
            pass
        case int(max1_u):
            #check_type_is(int, max1_u)
            #max1_u = max(min_u, max1_u)
            #max1_u = max(2, max1_u)
            if not min_u < max1_u: return
            # [min_u < max1_u]
            777;may_max1_u = max1_u
            odd_us = range(odd_min_u, max1_u, 2)
            if reverse:
                odd_us = odd_us[::-1]
            # [[reverse] -> [odd_us :: reversed]]
            pass
        case _:
            raise TypeError(may_max1_u)
    # [[reverse] -> [odd_us :: reversed]]
    # [[not None is may_max1_u] -> [min_u < max1_u]]
    even_ps = (2,) if min_u == 2 else ()
    odd_sprps = filter_SPRP_2357_(odd_us)
    # [[reverse] -> [odd_sprps :: reversed]]
    if reverse:
        # [odd_sprps :: reversed]
        yield from odd_sprps
        yield from even_ps
    else:
        yield from even_ps
        yield from odd_sprps

def next_SPRP_2357__ge_(min_u, /):
    #vs:next_probable_prime__ge_
    check_type_is(int, min_u)
    if min_u < 3:
        return 2
    odd_min_u = 1|min_u
    odd_us = count(odd_min_u, 2)
    return next(filter_SPRP_2357_(odd_us))
def prev_may_SPRP_2357__lt_(max1_u, /):
    #vs:prev_may_probable_prime__lt_
    check_type_is(int, max1_u)
    if max1_u <= 3:
        return 2 if 2 < max1_u else None
    # [3 < max1_u]
    odd_us = range(3, max1_u, 2)[::-1]
    return next(filter_SPRP_2357_(odd_us))






r'''[[[
Sophie_Germain_prime:
https://oeis.org/A005384
A005384 Sophie Germain primes p: 2p+1 is also prime.
==>>:
    Sophie_Germain_SPRP_2357
    Sophie_Germain_xprimes7SPRP_2357

is there infinite long Sophie_Germain_prime_chain???
[p::odd_prime][0 == ((a+1)*2**k -1) %p]:
    [1 =[%p]= (a+1)*2**k]
    [a+1 =[%p]= 2**-k]
[p::odd_prime][is_primitive_root_mod_(p;2)]:
    [@[a::int][a%p =!= p-1] -> ?[k:<-[0..=p-2]] -> [0 == ((a+1)*2**k -1) %p]]
==>>:
[Sophie_Germain_prime_chain must be finite long]

??? [Sophie_Germain_prime_chain can be arbitrary long] ???



view ../../python3_src/nn_ns/math_nn/numbers/_patch_prime_..b001918.b002233.out.txt
0 2 1 1
1 3 2 2
2 5 2 2
3 7 3 3
4 11 2 2
5 13 2 2
6 17 3 3
7 19 2 2
8 23 5 5
9 29 2 2
10 31 3 3
11 37 2 2
12 41 6 7
13 43 3 3
14 47 5 5
15 53 2 2
16 59 2 2
17 61 2 2
18 67 2 2
19 71 7 7
20 73 5 5
21 79 3 3
22 83 2 2
23 89 3 3
24 97 5 5
25 101 2 2
26 103 5 5
27 107 2 2
28 109 6 11
29 113 3 3
30 127 3 3
31 131 2 2
32 137 3 3
33 139 2 2
34 149 2 2
35 151 6 7
36 157 5 5
37 163 2 2
38 167 5 5
39 173 2 2
40 179 2 2
41 181 2 2
42 191 19 19
43 193 5 5
44 197 2 2
45 199 3 3
46 211 2 2
47 223 3 3
48 227 2 2
49 229 6 7
50 233 3 3
51 239 7 7
52 241 7 7
53 251 6 11
54 257 3 3

grep -e ' 2 2' ../../python3_src/nn_ns/math_nn/numbers/_patch_prime_..b001918.b002233.out.txt | head -n 25
1 3 2 2
2 5 2 2
4 11 2 2
5 13 2 2
7 19 2 2
9 29 2 2
11 37 2 2
15 53 2 2
16 59 2 2
17 61 2 2
18 67 2 2
22 83 2 2
25 101 2 2
27 107 2 2
31 131 2 2
33 139 2 2
34 149 2 2
37 163 2 2
39 173 2 2
40 179 2 2
41 181 2 2
44 197 2 2
46 211 2 2
48 227 2 2
56 269 2 2


#]]]'''#'''
def iter_Sophie_Germain_xprimes7SPRP_2357__ge_lt_(min_u=2, may_max1_u=None, /, *, reverse=False):
    '-> Iter u/Sophie_Germain_SPRP_2357/uint{>=2}{[is_SPRP_2357_(u)][is_SPRP_2357_(1+2*u)]}'
    if 0:
        it = iter_xprimes7SPRP_2357__ge_lt_(min_u, may_max1_u, reverse=reverse)
    else:
        us = prepare4iter_xprimes7SPRP_2357__ge_lt_(min_u, may_max1_u, reverse=reverse)
        def is_ok_(u, /):
            # [u >= 2]
            w = (1^(u<<1))
            # [w >= 5]
            # [1 == w%2]
            if w < 9:
                # [9 > w >= 5]
                # !! [1 == w%2]
                # [w <- {5,7}]
                return True
            # [w >= 9]
            return not +1 == detect_noncoprime_to_2357_(w)
        us = filter(is_ok_, us)
        it = filter_SPRP_2357_(us)
    it# :: Iter SPRP_2357
    #new:
    it = filter(lambda u:is_SPRP_2357_(1^(u<<1)), it)
    return it
    #old:
    it = (1^(u<<1) for u in it)
    it = filter_SPRP_2357_(it)
    it = ((u>>1) for u in it)
    return it

def iter_Sophie_Germain_xprime_chains7SPRP_2357__len_eq__head_ge_lt_(len4chain, min_u=2, may_max1_u=None, /, *, reverse=False, num_primes4neg_one6IIprimes_only=0, num_primes4trial_division=0, to_trunc=True):
    return iter_Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_(len4chain, min_u, may_max1_u, reverse=reverse, num_primes4neg_one6IIprimes_only=num_primes4neg_one6IIprimes_only, num_primes4trial_division=num_primes4trial_division, to_trunc=to_trunc)
def iter_Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_(min4len4chain, min_u=2, may_max1_u=None, /, *, reverse=False, num_primes4neg_one6IIprimes_only=0, num_primes4trial_division=0, to_trunc=False):
    heads = iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_(min4len4chain, min_u, may_max1_u, reverse=reverse, num_primes4neg_one6IIprimes_only=num_primes4neg_one6IIprimes_only, num_primes4trial_division=num_primes4trial_division)
    for head_u in heads:
        yield mk_Sophie_Germain_xprime_chain5head7SPRP_2357_(head_u, to_trunc=to_trunc, min4len4chain=min4len4chain, _neednot_check6min4len4chain=True)
    return
def iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_(min4len4chain, min_u=2, may_max1_u=None, /, *, reverse=False, num_primes4neg_one6IIprimes_only=0, num_primes4trial_division=0):
    'min4len4chain{>=2} -> Iter u/Sophie_Germain_SPRP_2357/uint{>=2}{[@[k:<-[0..<min4len4chain]] -> [is_SPRP_2357_(-1+2**k*(1+u))]]}'
    # [PRIMES[:20] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]]
    check_int_ge(2, min4len4chain)
    check_int_ge(0, num_primes4neg_one6IIprimes_only)
    check_int_ge(0, num_primes4trial_division)
    len4chain = min4len4chain

    check_may_([check_type_is, int], may_max1_u)
    check_type_is(int, min_u)
    min_u = max(2, min_u)
    # [min_u >= 2]

    #.if may_max1_u is None:
    #.else:
    #.    max1_u = may_max1_u

    ps = PrimeList()
    if 0 < num_primes4neg_one6IIprimes_only:
        ps7step = ps[:num_primes4neg_one6IIprimes_only]
        IIps7step = II(ps7step)
        min_u = -1+(1 +min_u//IIps7step)*IIps7step
        # [min_u{new} =[%IIps7step]= -1]
        # [min_u{new} >= min_u{old}]
        if reverse and not None is may_max1_u:
            max1_u = may_max1_u
            max1_u = max1_u//IIps7step *IIps7step
            may_max1_u = max1_u
        may_max1_u
        us = iter_ints__ge_lt_(min_u, may_max1_u, step=IIps7step, reverse=reverse)
        # [[u :<- us] -> [u =[%IIps7step]= -1]]
    else:
        ps7step = ()
        us = prepare4iter_xprimes7SPRP_2357__ge_lt_(min_u, may_max1_u, reverse=reverse)
    ps7step
    us

    if num_primes4neg_one6IIprimes_only < num_primes4trial_division:
        ps7td = ps[num_primes4neg_one6IIprimes_only:num_primes4trial_division]
    else:
        ps7td = ()
    ps7td
    #IIps7td = II(ps7td)
    j2bad_residues6p7td = [*map(curry1(_list_bad_residues6p__7len4chain_, len4chain), ps7td)]

    #ps7using = ps7step + ps7td
        # ^TypeError: unsupported operand type(s) for +: 'SeqSliceView' and 'SeqSliceView'
    ps7using = ps[:max(num_primes4neg_one6IIprimes_only, num_primes4trial_division)]
    IIps7using = II(ps7using)
    u = None
    try:
     for u in us:
        if u <= 7:
            match u:
                case 2:
                    # [longest_uchain{2} == [2,5,11,23,47]] # 95
                    max4len4chain = 5
                case 5:
                    max4len4chain = 4
                case 3:
                    # [longest_uchain{3} == [3,7]] # 15
                    max4len4chain = 2
                case 7:
                    max4len4chain = 1
                case _:
                    raise 000
            max4len4chain
            if len4chain <= max4len4chain:
                yield u
            continue
        if not u >= 8: raise 000

        if not 1 == u&1: raise 000
        if not u >= 9: raise 000
        # [1 == u%2]
        # [u >= 9]
        j2u6p = []
        u6wheel = u%IIps7using
        bad = False
        for p, bad_residues6p in zip(ps7td, j2bad_residues6p7td):
            u6p = u6wheel%p
            if _in_sorted_list_(bad_residues6p, u6p) and u > p:
                bad = True
                break
        bad
        if bad:continue
        # [[u>max(ps7td, default=0)] -> [1 == gcd(IIps7td, II(uchain))]]

        # !! [[num_primes4neg_one6IIprimes_only>0] -> [u =[%IIps7step]= -1]]
        # [[num_primes4neg_one6IIprimes_only>0] -> @[v:<-uchain] -> [v =[%IIps7step]= -1]]
        # [1 == gcd(IIps7step, II(uchain))]
        # !! [[u>max(ps7td, default=0)] -> [1 == gcd(IIps7td, II(uchain))]]
        # [[u>max(ps7using, default=0)] -> [1 == gcd(IIps7using, II(uchain))]]
        #   almost pass trial_division

        uchain = [u]
        for _ in range(-1+len4chain):
            uchain.append(1^(uchain[-1]<<1))
        assert len(uchain) == len4chain
        # !! [1 == u%2]
        # !! [u >= 5]
        # [@[v:<-uchain] -> [[1 == v%2][v >= 5]]]
        bad = False
        for j4p, p in enumerate(bs_2357):
            # [@[v:<-uchain] -> [is_SPRP_(bs_2357[:bs_2357.index(p)];v)]]
            min_SPSP6prev_ps = 0 if 0==j4p else A014233[-1+j4p]
            xidx = bisect_left(uchain, min_SPSP6prev_ps)
            if xidx == len4chain:
                # [uchain[-1] < min_SPSP6prev_ps]
                break
            # [uchain[xidx] >= min_SPSP6prev_ps]
            # [min(uchain[:xidx], default=-1) < min_SPSP6prev_ps <= uchain[xidx]]
            for v in seq_islice(uchain, xidx, None):
                #if v < min_SPSP6prev_ps:continue
                assert v >= min_SPSP6prev_ps
                # [v >= min_SPSP6prev_ps]
                # !! [[j2p>0] -> [min_SPSP6prev_ps >= 2+p]]
                # [[j2p>0] -> [v >= min_SPSP6prev_ps >= 2+p]]
                # !! [v >= 5]
                # [[j2p==0] -> [v >= 5 > 2+p==4]]
                # [v >= 2+p]
                assert v > 1+p
                # [1 < p < v-1]

                # !! [[1 == v%2][v >= 5]]
                # !! [1 < p < v-1]
                if not is_strong_probable_prime_(p, v):
                    bad = True
                    break
            bad
            if bad:break
            # [@[v:<-uchain] -> [is_SPRP_([p];v)]]
            # [@[v:<-uchain] -> [is_SPRP_(bs_2357[:1+bs_2357.index(p)];v)]]
        bad
        if bad:continue
        # [@[v:<-uchain] -> [is_SPRP_2357_(v)]]
        yield u
    except BaseException as exc:
        #KeyboardInterrupt
        #?ExceptionGroup?
        args = (exc, 'iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_()@', u)
        raise repack_exception_(*args)
        try:
            _exc = type(exc)(args)
        except:
            ok = False
        else:
            ok = True
        ok
        if ok:
            raise _exc
        else:
            print_err(args)
            raise
        raise 000
    return


def _in_sorted_list_(ls, x, /):
    j = bisect_right(ls, x)
    return 0 < j and ls[-1+j] == x
def _list_bad_residues6p__7len4chain_(len4chain, p, /):
    # [@[k:<-[0..<len4chain]] -> [0 =!= (-1+2**k*(1+u))%p]]
    # [@[k:<-[0..<len4chain]] -> [1 =!= (2**k*(1+u))%p]]
    # [@[k:<-[0..<len4chain]] -> [2**-k%p =!= (1+u)%p]]
    # [@[k:<-[0..<len4chain]] -> [u%p =!= (-1+2**-k%p)]]
    if p == 2:
        return [0]
    assert p&1
    # [1 == p%2]
    inv2 = pow(2,-1,p)
    inv_zpow6p = 1
    bad_residues6p = []
    for k in range(len4chain):
        # [inv_zpow6p == 2**-k%p]
        # [0 < inv_zpow6p < p]
        # [0 <= -1+inv_zpow6p < p-1]
        bad_residues6p.append(-1+inv_zpow6p)
        inv_zpow6p = inv_zpow6p*inv2 %p
        # [inv_zpow6p == 2**-(1+k)%p]
        if inv_zpow6p == 1:
            # [1 == 2**-(1+k)%p]
            # [1+k == order_mod_(p;2)]
            assert (-1+p)%(1+k) == 0
            break
    bad_residues6p.sort()
    assert bad_residues6p[0] == 0
    assert bad_residues6p[1] > 0
    assert bad_residues6p[-1] < p-1
    return bad_residues6p
#quadratic_nonresidue


class Error__Sophie_Germain_xprime_chain__too_short(Exception):pass
def mk_Sophie_Germain_xprime_chain5head7SPRP_2357_(head_u, /, *, min4len4chain=0, to_trunc=False, _neednot_check6min4len4chain=False):
    '-> ([Sophie_Germain_SPRP_2357]|^Error__Sophie_Germain_xprime_chain__too_short) # [next{Sophie_Germain_SPRP_2357} == 1+2*prev{Sophie_Germain_SPRP_2357}]'
    return tuple(iter_Sophie_Germain_xprime_chain5head7SPRP_2357_(head_u, min4len4chain=min4len4chain, to_trunc=to_trunc, _neednot_check6min4len4chain=_neednot_check6min4len4chain))
def iter_Sophie_Germain_xprime_chain5head7SPRP_2357_(head_u, /, *, min4len4chain=0, to_trunc=False, _neednot_check6min4len4chain=False):
    '-> Iter (Sophie_Germain_SPRP_2357|^Error__Sophie_Germain_xprime_chain__too_short) # [next{Sophie_Germain_SPRP_2357} == 1+2*prev{Sophie_Germain_SPRP_2357}]'
    check_int_ge(0, min4len4chain)
    check_type_is(int, head_u)
    u = head_u
    js = range(min4len4chain) if to_trunc else count()
    777;js = iter(js)
    if _neednot_check6min4len4chain:
        for j in islice(js, 0, min4len4chain):
            yield u
            u = 1^(u<<1)
        js, u
    js, u
    for j in js:
        if not is_SPRP_2357_(u):
            if not min4len4chain <= j:raise Error__Sophie_Germain_xprime_chain__too_short(head_u, min4len4chain, j)
            break
        yield u
        u = 1^(u<<1)
    return

__all__
from seed.math.primality_test.SPRP_2357 import is_SPRP_2357_, filter_SPRP_2357_, iter_xprimes7SPRP_2357__ge_lt_, next_SPRP_2357__ge_, prev_may_SPRP_2357__lt_, detect_noncoprime_to_2357_, filter4coprimes_to_2357_
from seed.math.primality_test.SPRP_2357 import iter_xprimes7SPRP_2357__ge_lt_, prepare4iter_xprimes7SPRP_2357__ge_lt_, iter_2357__ge_lt_, iter_coprimes7SPRP_2357__ge_lt_

from seed.math.primality_test.SPRP_2357 import iter_Sophie_Germain_xprimes7SPRP_2357__ge_lt_
from seed.math.primality_test.SPRP_2357 import iter_Sophie_Germain_xprime_chains7SPRP_2357__len_eq__head_ge_lt_, iter_Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_, iter_heads4Sophie_Germain_xprime_chains7SPRP_2357__len_ge__head_ge_lt_, mk_Sophie_Germain_xprime_chain5head7SPRP_2357_, iter_Sophie_Germain_xprime_chain5head7SPRP_2357_, Error__Sophie_Germain_xprime_chain__too_short



from seed.math.primality_test.SPRP_2357 import *
