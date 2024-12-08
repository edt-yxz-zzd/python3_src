#__all__:goto
r'''[[[
e ../../python3_src/seed/math/iter_sorted_products_of_uints.py
see:
    view ../../python3_src/seed/math/generate_partition4additive_semigroup__total_ordering__increasing.py

!mv ../../python3_src/seed/math/iter_sorted_products_of_pairwise_coprime_uints.py ../../python3_src/seed/math/iter_sorted_products_of_uints.py
from seed.math.iter_sorted_products_of_uints import iter_sorted_products_of_uints, iter_sorted_products_of_strict_sorted_pairwise_coprime_uints, iter_sorted_products_of_strict_sorted_pairwise_coprime_uints__with_ifactor_exp_pairs
from seed.math.iter_sorted_products_of_uints import iter_unsorted_products_of_strict_sorted_pairwise_coprime_uints_lt_, iter_approximate_num_pints_lt__generated_by_, approximate_num_pints_lt__generated_by_, iter_unsorted_primes_lt__prime_eq_one_plus_product_generated_by_strict_sorted_pairwise_coprime_uints_


py -m nn_ns.app.debug_cmd   seed.math.iter_sorted_products_of_uints -x
py -m nn_ns.app.doctest_cmd seed.math.iter_sorted_products_of_uints:__doc__ -ff -v
py_adhoc_call   seed.math.iter_sorted_products_of_uints   @f

py -m seed.math.iter_sorted_products_of_uints _NOP_
py -m seed.math.iter_sorted_products_of_uints print_sorted_products_of_strict_sorted_pairwise_coprime_uints =[] =3
[1]
py -m seed.math.iter_sorted_products_of_uints print_sorted_products_of_strict_sorted_pairwise_coprime_uints =[2] =5
[1, 2, 4, 8, 16]
py -m seed.math.iter_sorted_products_of_uints print_sorted_products_of_strict_sorted_pairwise_coprime_uints =[2,3] =15
[1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48]
py -m seed.math.iter_sorted_products_of_uints print_sorted_products_of_strict_sorted_pairwise_coprime_uints =[2,3,5] =25
[1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36, 40, 45, 48, 50, 54]

f({2,3}) -> [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, ...]
[[
可能的用处:
    给定 素数集ps，搜索 (q:=II p**e<p> {p<-ps} + 1) 型 素数
        phi(q)=(q-1) is ps-smooth

]]
[[
发现新用处:
view others/数学/ECC-椭圆曲线整数分解.txt


/sdcard/0my_files/book/math/factorint/snd/Lenstra Elliptic Curve Factorization(2016)(Thomas Browning).pdf

[Hasse_interval(p) =[def]= [p+1-2*floor_sqrt(p)..=p+1+2*floor_sqrt(p)]]
[group_order_(ECC(a,b;GF(p))) <- Hasse_interval(p)]

the order of ECC(a,b;GF(p)) for various curves is known to vary randomly.  Thus, it is quite likely that eventually the chosen curve will happen to have an order which is the product of small primes.

那么，若 只选 {2,3}，(2**i*3**j)型的整数的最大间隙的增长速度是多少？
[Hasse_interval(101) == [82..=122]]



py -m seed.math.iter_sorted_products_of_uints print_sorted_products_of_strict_sorted_pairwise_coprime_uints =[2,3] =100
[1
, 2
, 3
, 4
, 6
, 8
, 9
, 12
, 16
, 18
, 24
, 27
, 32
, 36
, 48
, 54
, 64
, 72
, 81
, 96
, 108
, 128
, 144
, 162
, 192
, 216
, 243
, 256
, 288
, 324
, 384
, 432
, 486
, 512
, 576
, 648
, 729
, 768
, 864
, 972
, 1024
, 1152
, 1296
, 1458
, 1536
, 1728
, 1944
, 2048
, 2187
, 2304
, 2592
, 2916
, 3072
, 3456
, 3888
, 4096
, 4374
, 4608
, 5184
, 5832
, 6144
, 6561
, 6912
, 7776
, 8192
, 8748
, 9216
, 10368
, 11664
, 12288
, 13122
, 13824
, 15552
, 16384
, 17496
, 18432
, 19683
, 20736
, 23328
, 24576
, 26244
, 27648
, 31104
, 32768
, 34992
, 36864
, 39366
, 41472
, 46656
, 49152
, 52488
, 55296
, 59049
, 62208
, 65536
, 69984
, 73728
, 78732
, 82944
, 93312
]






py -m seed.math.iter_sorted_products_of_uints print_max_gaps_between_sorted_products_of_strict_sorted_pairwise_coprime_uints =[2,3] =100
[(0, 1, 1, 2)
, (3, 2, 4, 6)
, (6, 3, 9, 12)
, (7, 4, 12, 16)
, (9, 6, 18, 24)
, (13, 12, 36, 48)
, (18, 15, 81, 96)
, (20, 20, 108, 128)
, (23, 30, 162, 192)
, (27, 32, 256, 288)
, (28, 36, 288, 324)
, (29, 60, 324, 384)
, (33, 64, 512, 576)
, (34, 72, 576, 648)
, (35, 81, 648, 729)
, (37, 96, 768, 864)
, (38, 108, 864, 972)
, (40, 128, 1024, 1152)
, (41, 144, 1152, 1296)
, (42, 162, 1296, 1458)
, (44, 192, 1536, 1728)
, (45, 216, 1728, 1944)
, (49, 288, 2304, 2592)
, (50, 324, 2592, 2916)
, (52, 384, 3072, 3456)
, (53, 432, 3456, 3888)
, (57, 576, 4608, 5184)
, (58, 648, 5184, 5832)
, (62, 864, 6912, 7776)
, (66, 1152, 9216, 10368)
, (67, 1296, 10368, 11664)
, (71, 1728, 13824, 15552)
, (77, 2592, 20736, 23328)
, (81, 3456, 27648, 31104)
, (87, 5184, 41472, 46656)
, (98, 10368, 82944, 93312)
, (109, 11259, 165888, 177147)
, (112, 13344, 196608, 209952)
, (114, 15012, 221184, 236196)
, (117, 17792, 262144, 279936)
, (119, 20016, 294912, 314928)
, (121, 22518, 331776, 354294)
, (124, 26688, 393216, 419904)
, (126, 30024, 442368, 472392)
, (132, 40032, 589824, 629856)
, (134, 45036, 663552, 708588)
, (137, 53376, 786432, 839808)
, (139, 60048, 884736, 944784)
, (145, 80064, 1179648, 1259712)
, (147, 90072, 1327104, 1417176)
, (153, 120096, 1769472, 1889568)
, (159, 160128, 2359296, 2519424)
, (161, 180144, 2654208, 2834352)
, (167, 240192, 3538944, 3779136)
, (174, 255879, 4782969, 5038848)
, (175, 269568, 5038848, 5308416)
, (176, 360288, 5308416, 5668704)
, (182, 480384, 7077888, 7558272)
, (189, 511758, 9565938, 10077696)
, (190, 539136, 10077696, 10616832)
, (191, 720576, 10616832, 11337408)
, (198, 767637, 14348907, 15116544)
, (199, 808704, 15116544, 15925248)
, (200, 851968, 15925248, 16777216)
, (202, 909792, 17006112, 17915904)
, (203, 958464, 17915904, 18874368)
, (205, 1023516, 19131876, 20155392)
, (206, 1078272, 20155392, 21233664)
, (207, 1441152, 21233664, 22674816)
, (214, 1535274, 28697814, 30233088)
, (215, 1617408, 30233088, 31850496)
, (216, 1703936, 31850496, 33554432)
, (218, 1819584, 34012224, 35831808)
, (219, 1916928, 35831808, 37748736)
, (221, 2047032, 38263752, 40310784)
, (222, 2156544, 40310784, 42467328)
, (224, 2302911, 43046721, 45349632)
, (225, 2426112, 45349632, 47775744)
, (226, 2555904, 47775744, 50331648)
, (228, 2729376, 51018336, 53747712)
, (229, 2875392, 53747712, 56623104)
, (231, 3070548, 57395628, 60466176)
, (232, 3234816, 60466176, 63700992)
, (233, 3407872, 63700992, 67108864)
, (235, 3639168, 68024448, 71663616)
, (236, 3833856, 71663616, 75497472)
, (238, 4094064, 76527504, 80621568)
, (239, 4313088, 80621568, 84934656)
, (241, 4605822, 86093442, 90699264)
, (242, 4852224, 90699264, 95551488)
, (243, 5111808, 95551488, 100663296)
, (245, 5458752, 102036672, 107495424)
, (246, 5750784, 107495424, 113246208)
, (248, 6141096, 114791256, 120932352)
, (249, 6469632, 120932352, 127401984)
, (253, 7278336, 136048896, 143327232)
, (254, 7667712, 143327232, 150994944)
, (256, 8188128, 153055008, 161243136)
, (257, 8626176, 161243136, 169869312)
, (259, 9211644, 172186884, 181398528)
]
==>>
, (49, 288, 2304, 2592)

py_adhoc_call   seed.math.prime_gens   @next_may_prime__le_pow2_81__ge_  ='(2304+2592)//2 -5'
2447

>>> 49**2 < 2447 < 50**2
True
>>> 2447+1+2*49
2546
>>> 2447+1-2*49
2350

[floor_sqrt(2447) == 49]
[Hasse_interval(2447) == [2447+1-2*49..=2447+1+2*49] == [2350..=2546]]
只选{2,3}在[p==2447]不行

]]

发现相关:
[[[
https://mathworld.wolfram.com/SmoothNumber.html
===

Smooth Number
An integer is k-smooth if it has no prime factors >k. The following table gives the first few k-smooth numbers for small k. Berndt (1994, p. 52) called the 7-smooth numbers "highly composite numbers."

k	OEIS	k-smooth numbers
2	A000079	1, 2, 4, 8, 16, 32, 64, 128, 256, 512, ...
3	A003586	1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, ...
5	A051037	1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, ...
7	A002473	1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, ...
11	A051038	1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, ...
The probability that a random positive integer <=n is k-smooth is psi(n,k)/n, where psi(n,k) is the number of k-smooth numbers <=n. This fact is important in application of Kraitchik's extension of Fermat's factorization method because it is related to the number of random numbers which must be examined to find a suitable subset whose product is a square.

Since about pi(k) k-smooth numbers must be found (where pi(k) is the prime counting function), the number of random numbers which must be examined is about pi(k)n/psi(n,k). But because it takes about pi(k) steps to determine if a number is k-smooth using trial division, the expected number of steps needed to find a subset of numbers whose product is a square is ∼[pi(k)]^2n/psi(n,k) (Pomerance 1996). Canfield et al. (1983) showed that this function is minimized when

 k∼exp(1/2sqrt(lnnlnlnn)) 	
(1)
and that the minimum value is about

 exp(2sqrt(lnnlnlnn)). 	
(2)
In the continued fraction factorization algorithm, n can be taken as 2sqrt(n), but in Fermat's factorization method, it is n^(1/2+epsilon). k is an estimate for the largest prime in the factor base (Pomerance 1996).

The curiosity

 11859210 approx 11859211->
7×13×19^4 approx 2×3^4×5×11^4->
91×19^4 approx 10×33^4->
9.1 approx (33^4)/(19^4)->
9.1^(1/4) approx 33/19 	
(3)
involves the largest consecutive 19-smooth numbers, 11859210 and 11859211.
]]]


[[[
离散对数 很容易求的素数:若(p-1)可分解为 小素数
===
view others/数学/整数分解/sqrts_mod_.txt
view script/discrete_logarithm.py
===
py -m seed.math.iter_sorted_products_of_uints print_sorted_products_of_strict_sorted_pairwise_coprime_uints =[] =3
py_adhoc_call   seed.math.iter_sorted_products_of_uints   ,iter_unsorted_products_of_strict_sorted_pairwise_coprime_uints_lt_  =100  ='[2,3,5]'
1
2
4
8
16
32
64
3
6
12
24
48
96
9
18
36
72
27
54
81
5
10
20
40
80
15
30
60
45
90
25
50
75
py_adhoc_call   seed.math.iter_sorted_products_of_uints   ,iter_unsorted_products_of_strict_sorted_pairwise_coprime_uints_lt_  =100  ='[5,3,2]'  +coprime_factors_is_unsorted_but_finite
1
5
25
3
15
75
9
45
27
81
2
10
50
6
30
18
90
54
4
20
12
60
36
8
40
24
72
16
80
48
32
96
64

]]]
[[[
e others/数学/整数分解/ECC-椭圆曲线整数分解.txt
e ../../python3_src/seed/math/iter_sorted_products_of_uints.py
===
  approximate_num_pints_lt__generated_by_(prime_bases; N)
    近似估计 由prime_bases生成的小于N的正整数数量
    等价于 数格子:
      平面: [sum log2(p)*x {(p,x) :<- zip(prime_bases,vars)} == log2(N)]与 所有 坐标平面 所围锥体。
      [@[x :<- vars] -> [x >= 0]][sum log2(p)*x {(p,x) :<- zip(prime_bases,vars)} <= log2(N)]

    volumn(lens) = II sz {sz :<- lens} / factorial(len(lens))
    volumn(prime_bases; N) = II (log2(N)/log2(p)) {p :<- prime_bases} / factorial(L)
      会减少，显然不行
    [L := len(prime_bases)]
    [approximate_num_pints_lt__generated_by_(prime_bases; N) =[def]= sum (sum volumn({prime_bases[j] | [j :<- js]}; N) {js :<- iter_combinations_(k; L)}) /factorial(k) {k :<- [0..=L]}]
    [approximate_num_pints_lt__generated_by_(prime_bases; N) == sum (sum II (log2(N)/log2(prime_bases[j])) {j :<- js} {js :<- iter_combinations_(k; L)}) /factorial(k) {k :<- [0..=L]}]
    表达为 L+1 的 数组，可用于 递推 计算
    [array4approximate_num_pints_lt__generated_by_(prime_bases; N) =[def]= [((sum II (log2(N)/log2(prime_bases[j])) {j :<- js} {js :<- iter_combinations_(k; L)}) /factorial(k)) | [k :<- [0..=L]]]]
    [array4approximate_num_pints_lt__generated_by_(prime_bases++[pL]; N) == let [ls := array4approximate_num_pints_lt__generated_by_(prime_bases; N)] in ([0+ls[0]]++[(ls[k-1]*(log2(N)/log2(pL))/k + ls[k]) | [k :<- [1..=L]]]++[(ls[(L+1)-1]*(log2(N)/log2(pL))/(L+1) + 0)])]
===


>>> f = lambda gs, N, /: (ls := [*iter_unsorted_products_of_strict_sorted_pairwise_coprime_uints_lt_(N, gs)], *map(ls.index, gs), len(ls))[1:]


>>> _print_ex_arrays4approximate_num_pints_lt__generated_by_([2,3,5,7], 2**20)
0:1.0:(1.0,)%
1:21.0:(1.0, 20.0)%
2:159.80454578572062:(1.0, 32.61859507142915, 126.18595071429148)%
3:671.2009256983828:(1.0, 41.23212623289701, 266.66659325982, 362.30220620566575)%
4:2103.7271624623922:(1.0, 48.35626997505745, 413.53839029885137, 995.5592534107293, 645.273248777754)%
>>> f([2,3,5,7], 2**20)
(1, 20, 142, 510, 1285)
>>> _print_ex_arrays4approximate_num_pints_lt__generated_by_([2,3,5,7], 2**80)
0:1.0:(1.0,)%
1:81.0:(1.0, 80.0)%
2:2150.4495917143804:(1.0, 130.4743802857166, 2018.9752114286637)%
3:27619.935194251317:(1.0, 164.92850493158804, 4266.66549215712, 23187.34119716261)%
4:235716.78323007358:(1.0, 193.4250799002298, 6616.614244781622, 63715.792218286675, 165189.95168710503)%
>>> f([2,3,5,7], 2**80) #doctest: +SKIP
(1, 80, 2084, 25378, 199186)

>>> [*iter_approximate_num_pints_lt__generated_by_([2,3,5,7], 2**80)]
[1.0, 81.0, 2150.4495917143804, 27619.935194251317, 235716.78323007358]

>>> iter_unsorted_products_of_strict_sorted_pairwise_coprime_uints_lt_(2**80, [2,3,5,7,11,13,17,19]) #doctest: +SKIP
<<<...too many to enumerate...>>>
>>> [*iter_approximate_num_pints_lt__generated_by_([2,3,5,7,11,13,17,19], 2**80)]
[1.0, 81.0, 2150.4495917143804, 27619.935194251317, 235716.78323007358, 1421349.4458287342, 7167370.210745273, 30346393.18970447, 115542533.5714829]

>>> from seed.math.prime_gens import is_strong_pseudoprime__basis_, is_prime__using_A014233_, is_prime__le_pow2_81_, is_prime__tribool_, Case4is_prime__tribool_
>>> max1 = is_prime__using_A014233_.upperbound
>>> ls = [*filter(is_prime__using_A014233_, map(1 .__add__, iter_unsorted_products_of_strict_sorted_pairwise_coprime_uints_lt_(max1, [2,3,5,7])))] ; len(ls) #doctest: +SKIP
18724
>>> ls = [*filter(is_prime__using_A014233_, map(1 .__add__, iter_unsorted_products_of_strict_sorted_pairwise_coprime_uints_lt_(max1, [2,3,5])))] ; len(ls) #doctest: +SKIP
2297


py_adhoc_call   seed.math.iter_sorted_products_of_uints   ,iter_unsorted_primes_lt__prime_eq_one_plus_product_generated_by_strict_sorted_pairwise_coprime_uints_  ='[2,3,5]' > /sdcard/0my_files/tmp/out4py/seed.math.iter_sorted_products_of_uints..iter_unsorted_primes_lt__prime_eq_one_plus_product_generated_by_strict_sorted_pairwise_coprime_uints_.2-3-5.out.txt
view /sdcard/0my_files/tmp/out4py/seed.math.iter_sorted_products_of_uints..iter_unsorted_primes_lt__prime_eq_one_plus_product_generated_by_strict_sorted_pairwise_coprime_uints_.2-3-5.out.txt
du -h /sdcard/0my_files/tmp/out4py/seed.math.iter_sorted_products_of_uints..iter_unsorted_primes_lt__prime_eq_one_plus_product_generated_by_strict_sorted_pairwise_coprime_uints_.2-3-5.out.txt
44K
du -h ../../python3_src/seed/math/iter_sorted_products_of_uints.py
32K

!mkdir ../../python3_src/seed/math/_output_/
cp -t ../../python3_src/seed/math/_output_/ /sdcard/0my_files/tmp/out4py/seed.math.iter_sorted_products_of_uints..iter_unsorted_primes_lt__prime_eq_one_plus_product_generated_by_strict_sorted_pairwise_coprime_uints_.2-3-5.out.txt
view ../../python3_src/seed/math/_output_/seed.math.iter_sorted_products_of_uints..iter_unsorted_primes_lt__prime_eq_one_plus_product_generated_by_strict_sorted_pairwise_coprime_uints_.2-3-5.out.txt

>>> from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_
>>> txt = read_under_pkg_('seed.math', '_output_/seed.math.iter_sorted_products_of_uints..iter_unsorted_primes_lt__prime_eq_one_plus_product_generated_by_strict_sorted_pairwise_coprime_uints_.2-3-5.out.txt', xencoding='u8')
Traceback (most recent call last):
    ...
ValueError: '_output_/seed.math.iter_sorted_products_of_uints..iter_unsorted_primes_lt__prime_eq_one_plus_product_generated_by_strict_sorted_pairwise_coprime_uints_.2-3-5.out.txt' must be only a file name
>>> txt = read_under_pkg_('seed.math._output_', 'seed.math.iter_sorted_products_of_uints..iter_unsorted_primes_lt__prime_eq_one_plus_product_generated_by_strict_sorted_pairwise_coprime_uints_.2-3-5.out.txt', xencoding='u8') #doctest: +SKIP
>>> primes = sorted(map(int, txt.split())) #doctest: +SKIP
>>> for p in primes[-200:]:p #doctest: +SKIP
250157725494998535000001
252101350959004475617537
252428641478023053312001
253899891671040000000001
257363915118311250000001
272405031328125000000001
281250000000000000000001
281792804290560000000001
284993413919539200000001
289678573608398437500001
289910292480000000000001
297203348275200000000001
299512499409958993920001
301748514175415039062501
306700799395798009774081
311236235751857377305601
314928000000000000000001
323108661091869508239361
324000000000000000000001
327147519355517877092353
332416317995750522880001
334731302496000000000001
335276126861572265625001
341992096703447040000001
345427999563645871718401
363907686783100177612801
370604037770368200000001
385175539364659200000001
389045294689821721632001
390625000000000000000001
394419752309411020800001
396718580736000000000001
405457305908203125000001
415051741658464911360001
415188281250000000000001
424673280000000000000001
425152800000000000000001
436196692474023836123137
436689224139720213135361
443146905982625054796451
453859079503531380572161
456504342950707200000001
464380231680000000000001
469654673817600000000001
473303702771293224960001
475525357240320000000001
479219999055934390272001
480926385989222400000001
491275377157185239777281
499187499016598323200001
503316480000000000000001
504202701918008951235073
504287866115034867302401
507799783342080000000001
510591464441472803143681
510759433740234375000001
518727059586428962176001
521421432495117187500001
521838526464000000000001
532466665617704878080001
534966026895360000000001
540609741210937500000001
545861530174650266419201
547367362976074218750001
547805211540848640000001
550376570880000000000001
560319851238927630336001
578415690713088000000001
581130733500000000000001
582252298852960284180481
583666511707216281600001
590862541310166739728601
592966460432589120000001
607197655482971258880001
611529523200000000000001
615093750000000000000001
624688945970135040000001
630359832643793584128001
630567202148437500000001
637729200000000000000001
643730163574218750000001
645488468627244630147073
649983722677862400000001
665051346015930175781251
667953313873920000000001
673903123672407736320001
675425858836496044500001
675762176513671875000001
684209203720092773437501
687194767360000000000001
698491930961608886718751
698702758623552341016577
699840000000000000000001
703687441776640000000001
711914062500000000000001
714093445324800000000001
718255453697204589843751
729823150634765625000001
747093134985236840448001
747936715490438676480001
750473176484995605000001
753145430616000000000001
756304052877013426852609
756431799172552300953601
774840978000000000000001
782132148742675781250001
783641640960000000000001
802449040343040000000001
819716834902011199488001
826497043200000000000001
834941642342400000000001
861906544436645507812501
949218750000000000000001
992916339191015625000001
1007769600000000000000001
1088391168000000000000001
1115771008320000000000001
1125000000000000000000001
1138495604030571110400001
1147912560000000000000001
1149208725915527343750001
1162261467000000000000001
1207959552000000000000001
1225822640976562500000001
1230187500000000000000001
1231576566696166992187501
1244160000000000000000001
1260719665287587168256001
1267054080963134765625001
1314732507698036736000001
1345210031250000000000001
1351524353027343750000001
1357868313789367675781251
1361577238510594141716481
1381711998254583486873601
1405550128432803840000001
1407137205909366759375001
1415577600000000000000001
1440908498851191561600001
1455630747132400710451201
1473826131471555719331841
1479074071160291328000001
1556444031219243417600001
1579460446107205632000001
1594323000000000000000001
1624959306694656000000001
1632586752000000000000001
1669883284684800000000001
1689405441284179687500001
1729382256910270464000001
1793023523964568417075201
1830143396396880000000001
1865311197643687707279361
1867732837463092101120001
1877117156982421875000001
1932735283200000000000001
1959104102400000000000001
1968300000000000000000001
1974325557634007040000001
1979120929996800000000001
2044671995971986731827201
2046980738154938499072001
2079947912569159680000001
2099520000000000000000001
2109375000000000000000001
2113446032179200000000001
2118221523607500000000001
2164168736951500800000001
2179240250625000000000001
2189469451904296875000001
2240900897413373116600321
2241279404955710521344001
2267481600000000000000001
2288818359375000000000001
2360784484517792254525441
2394184845657348632812501
2440191195195840000000001
2453606395166384078192641
2531250000000000000000001
2552526178459920315627553
2555839994964983414784001
2593635297932144810880001
2597002484341800960000001
2602870608208896000000001
2654208000000000000000001
2665339502805909504000001
2729307650873251332096001
2802520898437500000000001
2814274411818733518750001
2821109907456000000000001
2839822216627759349760001
2919292602539062500000001
3123444729850675200000001
3128528594970703125000001
3166593487994880000000001
3167635202407836914062501
3173748645888000000000001
3242044122415181013600001
3242591731706757120000001
3294258113514384000000001
>>> 250157725494998535000001 .bit_length() # primes[-200]
78
>>> 3294258113514384000000001 .bit_length() # primes[-1]
82


]]]



#]]]'''
__all__ = r'''
    iter_sorted_products_of_uints
    iter_sorted_products_of_strict_sorted_pairwise_coprime_uints
    iter_sorted_products_of_strict_sorted_pairwise_coprime_uints__with_ifactor_exp_pairs


    iter_find_max_gaps_between_sorted_ints
    iter_find_max_gaps_between_sorted_products_of_strict_sorted_pairwise_coprime_uints

    print_sorted_products_of_strict_sorted_pairwise_coprime_uints
    print_max_gaps_between_sorted_products_of_strict_sorted_pairwise_coprime_uints

    iter_unsorted_products_of_strict_sorted_pairwise_coprime_uints_lt_
    iter_approximate_num_pints_lt__generated_by_
        approximate_num_pints_lt__generated_by_
    iter_unsorted_primes_lt__prime_eq_one_plus_product_generated_by_strict_sorted_pairwise_coprime_uints_
    '''.split()#'''
    #iter_sorted_products_of_pairwise_coprime_uints

__all__
from seed.math.II import II
from seed.math.gcd import gcd
from seed.math.lcm import lcm_many
from seed.math.are_pairwise_coprime import are_pairwise_coprime
from seed.tiny_.check import check_int_ge
from seed.tiny import fst

import heapq
from itertools import islice, pairwise

def iter_find_max_gaps_between_sorted_ints(sorted_ints, /):
    sorted_ints = iter(sorted_ints)
    max_gap = -1
    for idx, (i, j) in enumerate(pairwise(sorted_ints)):
        gap = j-i
        assert gap >= 0
        if gap > max_gap:
            max_gap = gap
            yield (idx, gap, i, j)

def iter_find_max_gaps_between_sorted_products_of_strict_sorted_pairwise_coprime_uints(sorted_coprime_factors, /, *, finite_seq_vs_infinite_seq, turnoff__verify_factors_are_pairwise_coprime):
    it = iter_sorted_products_of_strict_sorted_pairwise_coprime_uints(sorted_coprime_factors, finite_seq_vs_infinite_seq=finite_seq_vs_infinite_seq, turnoff__verify_factors_are_pairwise_coprime=turnoff__verify_factors_are_pairwise_coprime)
    it = iter_find_max_gaps_between_sorted_ints(it)
    return it

def iter_sorted_products_of_strict_sorted_pairwise_coprime_uints(sorted_coprime_factors, /, *, finite_seq_vs_infinite_seq, turnoff__verify_factors_are_pairwise_coprime):
    return map(fst, iter_sorted_products_of_strict_sorted_pairwise_coprime_uints__with_ifactor_exp_pairs(sorted_coprime_factors, finite_seq_vs_infinite_seq=finite_seq_vs_infinite_seq, turnoff__verify_factors_are_pairwise_coprime=turnoff__verify_factors_are_pairwise_coprime))
def iter_sorted_products_of_strict_sorted_pairwise_coprime_uints__with_ifactor_exp_pairs(sorted_coprime_factors, /, *, finite_seq_vs_infinite_seq, turnoff__verify_factors_are_pairwise_coprime):
    #def iter_sorted_products_of_pairwise_coprime_uints(us, /):
    #pairwise_coprime ==>> outs all diff 但还是不能自动避免重复(不同路径相乘:2*3==3*2)

    turnoff__verify_factors_are_pairwise_coprime = bool(turnoff__verify_factors_are_pairwise_coprime)
    finite_seq_vs_infinite_seq = bool(finite_seq_vs_infinite_seq)
    if not finite_seq_vs_infinite_seq:
        L = len(sorted_coprime_factors)
        xL = L
    else:
        xL = float('inf')


    if 0:
        #may be infinite seq such as PRIMES
        if not turnoff__verify_factors_are_pairwise_coprime:
            if not are_pairwise_coprime(sorted_coprime_factors): raise ValueError

    tmay_min_unused_idx4factors_and_prev_factor_and_may_II_prev_factors = [(0, 1, (None if turnoff__verify_factors_are_pairwise_coprime else 1))]
    _coprime_factors = sorted_coprime_factors
    del sorted_coprime_factors
    def get_(i, /):
        if not i >= 0: raise IndexError
        if not finite_seq_vs_infinite_seq:
            if not i < L: raise IndexError

        [(min_unused_idx4factors, prev_factor, may_II_prev_factors)] = tmay_min_unused_idx4factors_and_prev_factor_and_may_II_prev_factors
        factor = _coprime_factors[i]
        if i == min_unused_idx4factors:
            #strict_sorted
            check_int_ge(prev_factor+1, factor)

            #pairwise_coprime
            if not turnoff__verify_factors_are_pairwise_coprime:
                II_prev_factors = may_II_prev_factors
                if not 1==gcd(factor, II_prev_factors): raise ValueError
                may_II_prev_factors = factor*II_prev_factors

            tmay_min_unused_idx4factors_and_prev_factor_and_may_II_prev_factors[0] = (1+min_unused_idx4factors, factor, may_II_prev_factors)
        else:
            if not i < min_unused_idx4factors: raise logic-err
        return factor

    if 0:
        ies = ifactor_exp_pairs = ()
            # [exp >= 1]
            # [0 <= ifactor < xL]
        product5ies = 1
        if xL == 0:
            yield product5ies
            return

    heap = []
    def init_heap(heap, /):
        ies = ifactor_exp_pairs = ()
            # [exp >= 1]
            # [0 <= ifactor < xL]
        product5ies = 1
        heap_item = mk_item(product5ies, ies)
        put(heap_item)
    def mk_item(product5ies, ies, /):
        heap_item = (product5ies, ies)
        return heap_item
    def put(heap_item, /):
        heapq.heappush(heap, heap_item)

    def iter_new_items(old_heap_item, /, *, _ver_=2):
        #ver3:dec(ies) == if e0 >=2 then [(i0,e0-1),*_ies] elif len(ies) == 1 and i0 >=1 then [(i0-1,1)] else [*_ies]
        #   ver3 ==>> inc()不使用除法;但 扇出系数 太大，不好
        #ver2:dec(ies) == (if i0 >= 1 then [(i0-1,1)] else [])++(if e0 >=2 then [(i0,e0-1)] else [])++_ies
        #ver1:dec(ies) == if e0 >=2 then [(i0,e0-1),*_ies] elif i0 >= 1 then [(i0-1,1),*_ies] else [*_ies]
        #==>> inc(ies) := inv<dec>(ies)
        #ver1:inc(ies) == if xL == 0 then [] else (if len(ies)==0 or i0>=1 then [[(0,1),*ies]] else [])++(if len(ies)>=1 then [[(i0,e0+1),*_ies]] else [])++(if (len(ies)>=1 and e0==1 and i0+1 < (if len(_ies)>=1 then _ies[0][0] else xL)) then [[(i0+1,1),*_ies]] else [])
        #ver2:inc(ies) == if xL == 0 then [] else (if len(ies)==0 or i0>=1 then [[(0,1),*ies]] else [])++(if len(ies)>=1 and i0==0 then [[(i0,e0+1),*_ies]] else [])++(if (len(ies)>=1 and e0==1 and i0+1 < (if len(_ies)>=1 then _ies[0][0] else xL)) then [[(i0+1,1),*_ies]] else [])++(if (len(ies)>=2 and e0==1 and i0+1 == _ies[0][0]) then [[(i0+1,1+_ies[0][1]),*_ies[1:]]] else [])
        #ver3:inc(ies) == if xL == 0 then [] else (if len(ies)==0 then [[(0,1)]] else [])++(if (len(ies)==1 and e0==1 and i0+1 < xL) then [[(i0+1,1)]] else [])++(if len(ies)>=1 then [[(i0,e0+1),*_ies]] else [])++(if (len(ies)>=1 and i0 >= 1) then [[(i_,1),*ies] for i_ in range(i0)] else [])
        (old_product5ies, old_ies) = old_heap_item

        if _ver_==3:
            #ver3:
            if xL == 0:
                return;yield
            #sz = 1+(old_ies[-1][0] if old_ies else -1)
            len_ies = len(old_ies)
            if not len_ies == 0:
                [(i0,e0), *_ies] = old_ies
                if len_ies==1 and e0 == 1 and 1+i0 < xL:
                    ies = ((1+i0,1),)
                    product5ies = get_(1+i0)
                    yield mk_item(product5ies, ies)
                if 1:
                    ies = ((i0,1+e0), *_ies)
                    product5ies = old_product5ies*get_(i0)
                    yield mk_item(product5ies, ies)
                for i_ in range(i0):
                    ies = (((i_,1),*old_ies))
                    product5ies = old_product5ies*get_(i_)
                    yield mk_item(product5ies, ies)

            else:
                    ies = ((0,1),)
                    product5ies = get_(0)
                    yield mk_item(product5ies, ies)
            return
        if _ver_==2:
            #ver2:
            if xL == 0:
                return;yield
            #sz = 1+(old_ies[-1][0] if old_ies else -1)
            len_ies = len(old_ies)
            if not len_ies == 0:
                [(i0,e0), *_ies] = old_ies

                if i0 == 0:
                    ies = ((0,1+e0), *_ies)
                else:
                    ies = ((0,1), *old_ies)
                product5ies = old_product5ies*get_(0)
                yield mk_item(product5ies, ies)

                if e0 == 1 and 1+i0 < xL:
                    if len_ies >= 2 and 1+i0==_ies[0][0]:
                        [(i1,e1), *_1ies] = _ies
                        ies = ((i1,1+e1), *_1ies)
                    else:
                        i1 = 1+i0
                        ies = ((i1,1), *_ies)
                    product5ies = old_product5ies//get_(i0) *get_(i1)
                    yield mk_item(product5ies, ies)
            else:
                    ies = ((0,1),)
                    product5ies = get_(0)
                    yield mk_item(product5ies, ies)
            return
    #end-def iter_new_items(old_product5ies, old_ies, /):



    init_heap(heap)
    while heap:
        #(old_product5ies, old_ies)
        old_heap_item = heapq.heappop(heap)
        yield old_heap_item
        for new_heap_item in iter_new_items(old_heap_item):
            put(new_heap_item)
#if __name__ == "__main__":
def print_sorted_products_of_strict_sorted_pairwise_coprime_uints(sorted_coprime_factors, sz, /):
    it = iter_sorted_products_of_strict_sorted_pairwise_coprime_uints(sorted_coprime_factors, finite_seq_vs_infinite_seq=False, turnoff__verify_factors_are_pairwise_coprime=False)
    it = islice(it, sz)
    print([*it])
def print_max_gaps_between_sorted_products_of_strict_sorted_pairwise_coprime_uints(sorted_coprime_factors, sz, /):
    it = iter_find_max_gaps_between_sorted_products_of_strict_sorted_pairwise_coprime_uints(sorted_coprime_factors, finite_seq_vs_infinite_seq=False, turnoff__verify_factors_are_pairwise_coprime=False)
    it = islice(it, sz)
    print([*it])


def __():
  def iter_sorted_products_of_pairwise_coprime_uints(us, /):
    us = sorted(us)
    if not all(type(u) is int for u in us): raise TypeError
    if not all(u >= 2 for u in us): raise ValueError
    del us[:us.count(1)]


    if 0:
        M = II(us)
        if not all(gcd(u, M//u) ==1 for u in us): raise ValueError
    else:
        if not lcm_many(us) == II(us): raise ValueError('not pairwise coprime')

    return iter_sorted_products_of_uints(us)


def iter_sorted_products_of_uints(us, /):
    us = {*us}
    if not all(type(u) is int for u in us): raise TypeError
    if not all(u >= 0 for u in us): raise ValueError
    if 0 in us:
        yield 0
        us.remove(0)
    us.discard(1)
        # [u >= 2]

    outs = []
    o = 1
    yield o; outs.append(o)

    if not us: return

    heap = []
    def init_heap(heap, us):
        for u in us:
            put(u, 0)
    def mk_item(u, idx, /):
        o = u*outs[idx]
        heap_item = (o, (u, idx))
        return heap_item
    def put(u, idx, /):
        heap_item = mk_item(u, idx)
        heapq.heappush(heap, heap_item)
    def get():
        prev_o = outs[-1]
        while 1:
            (o, (u, idx)) = old_heap_item = heap[0]
            if not o == prev_o:
                #避免重复
                #来源1:不同路径相乘:2*3==3*2
                #来源2:不互素相乘: 6*35==10*21
                outs.append(o)
                    #必须在mk_item使用outs[idx+1]之前 加入！
            ###
            new_heap_item = mk_item(u, idx+1)
            old_heap_item = heapq.heappushpop(heap, new_heap_item)
            if not o == prev_o:
                break

        return o
    init_heap(heap, us)
    while 1:
        yield get()
assert [*iter_sorted_products_of_uints([])] == [1]
#print([*islice(iter_sorted_products_of_uints([2,3]), 13)])
#print([*islice(iter_sorted_products_of_uints([2,3,5]), 19)])
assert [*islice(iter_sorted_products_of_uints([2,3]), 13)] == [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32]
assert [*islice(iter_sorted_products_of_uints([2,3,5]), 19)] == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32]




def iter_unsorted_products_of_strict_sorted_pairwise_coprime_uints_lt_(max1, sorted_coprime_factors, /, *, coprime_factors_is_unsorted_but_finite=False):
    coprime_factors = iter(sorted_coprime_factors)
    is_unsorted = bool(coprime_factors_is_unsorted_but_finite)
    sorted_coprime_factors = None #release memory if using LazyList
    def _():
        lsls = [[]]
        def put(n, /):
            lsls[-1].append(n)
            return n
        def iter_lsls():
            #return iter(lsls)
            i = 0
            while i < len(lsls):
                ls = lsls[i]
                if not ls:
                    break
                if lsls[-1]:
                    lsls.append([])
                yield ls
                i += 1
        return put, iter_lsls

    def main():
        check_int_ge(0, max1)
        if max1 < 2:
            return

        put, iter_lsls = _()
        yield put(1)
        if max1 < 3:
            return
        prev_ft = 1
        for ft in coprime_factors:
            if is_unsorted:
                check_int_ge(2, ft)
            else:
                check_int_ge(prev_ft+1, ft)
                prev_ft = ft
            if not ft < max1:
                if is_unsorted:
                    continue
                else:
                    break
            maxpp4lhs = (max1-1)//ft +1
            for ls in iter_lsls():
                for lhs in ls:
                    if not lhs < maxpp4lhs:
                        break
                    yield put(lhs*ft)

    return main()
#assert (r := [*iter_unsorted_products_of_strict_sorted_pairwise_coprime_uints_lt_(100, [2,3,5])) == [], r
#assert (r := [*iter_unsorted_products_of_strict_sorted_pairwise_coprime_uints_lt_(100, [5,3,2], coprime_factors_is_unsorted_but_finite=True)) == [], r
def approximate_num_pints_lt__generated_by_(coprime_bases, N, /):
    '-> total_estimate/float'
    for x in iter_approximate_num_pints_lt__generated_by_(coprime_bases, N): pass
    return x
def iter_approximate_num_pints_lt__generated_by_(coprime_bases, N, /):
    '-> Iter total_estimate/float'
    #len(coprime_bases)
    #may inf long:if not len({*coprime_bases}) == len(coprime_bases):raise ValueError(coprime_bases)
    coprime_bases = iter(coprime_bases) #release memory if using LazyList
    arrays = _iter_arrays4approximate_num_pints_lt__generated_by_(coprime_bases, N)
    for L, array in enumerate(arrays):
        total_estimate = sum(array)
        yield total_estimate

def _print_ex_arrays4approximate_num_pints_lt__generated_by_(gs, N, /):
    arrays = _iter_arrays4approximate_num_pints_lt__generated_by_(gs, N)
    for L, array in enumerate(arrays):
        total = sum(array)
        print(f'{L}:{total}:{array}%')
def _iter_arrays4approximate_num_pints_lt__generated_by_(coprime_bases, N, /):
    r'''[[[
    [L := len(prime_bases)]
    [approximate_num_pints_lt__generated_by_(prime_bases; N) == sum (sum II (log2(N)/log2(prime_bases[j])) {j :<- js} {js :<- iter_combinations_(k; L)}) /factorial(k) {k :<- [0..=L]}]
    [array4approximate_num_pints_lt__generated_by_(prime_bases++[pL]; N) == let [ls := array4approximate_num_pints_lt__generated_by_(prime_bases; N)] in ([0+ls[0]]++[(ls[k-1]*(log2(N)/log2(pL))/k + ls[k]) | [k :<- [1..=L]]]++[(ls[(L+1)-1]*(log2(N)/log2(pL))/(L+1) + 0)])]
    #]]]'''#'''
    from math import log2 as lb_, log as ln_

    gs = iter(coprime_bases)
    coprime_bases = None

    check_int_ge(1, N)
    ln_N = ln_(N)
    ls = (1.0,)
    yield ls
    for L, g in enumerate(gs):
        # L is num of prev gs before g
        check_int_ge(2, g)
        assert len(ls) == L+1
        ln_g = ln_(g)
        log_g_N = ln_N/ln_g
        _ls = (1.0, *(ls[k-1]*log_g_N/k + ls[k] for k in range(1,L+1)), ls[L]*log_g_N/(L+1))
        ls = _ls
        assert len(ls) == L+2
        yield ls

def iter_unsorted_primes_lt__prime_eq_one_plus_product_generated_by_strict_sorted_pairwise_coprime_uints_(coprime_bases, may_max1=None, /, *, coprime_factors_is_unsorted_but_finite=False):
    from seed.math.prime_gens import is_strong_pseudoprime__basis_, is_prime__using_A014233_, is_prime__le_pow2_81_, is_prime__tribool_, Case4is_prime__tribool_
    max1 = is_prime__using_A014233_.upperbound
    if not may_max1 is None:
        if may_max1 > max1: raise ValueError(may_max1)
        max1 = may_max1
    return filter(is_prime__using_A014233_, map(1 .__add__, iter_unsorted_products_of_strict_sorted_pairwise_coprime_uints_lt_(max1, coprime_bases, coprime_factors_is_unsorted_but_finite=coprime_factors_is_unsorted_but_finite)))

__all__
if __name__ == "__main__":
    def _NOP_():pass #nop:no-op:无操作:用于 adhoc_argparser__main
    from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main, adhoc_argparse, AdhocArgParserError
    adhoc_argparser__main(globals(), None)
        #main()




from seed.math.iter_sorted_products_of_uints import iter_sorted_products_of_uints, iter_sorted_products_of_strict_sorted_pairwise_coprime_uints, iter_sorted_products_of_strict_sorted_pairwise_coprime_uints__with_ifactor_exp_pairs
from seed.math.iter_sorted_products_of_uints import iter_unsorted_products_of_strict_sorted_pairwise_coprime_uints_lt_, iter_approximate_num_pints_lt__generated_by_, approximate_num_pints_lt__generated_by_, iter_unsorted_primes_lt__prime_eq_one_plus_product_generated_by_strict_sorted_pairwise_coprime_uints_

from seed.math.iter_sorted_products_of_uints import *
