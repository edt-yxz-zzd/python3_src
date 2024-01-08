bug@_detect_primality__Nmm._call_g_
contains bug since output  composite least partial_pseudo_primitive_root
    see:
        view ../../python3_src/seed/math/primality_proving__plain.py
#__all__:goto
r'''[[[
e ../../python3_src/seed/math/primality_proving.py



seed.math.primality_proving
py -m seed.math.primality_proving
py -m nn_ns.app.debug_cmd   seed.math.primality_proving -x
py -m nn_ns.app.doctest_cmd seed.math.primality_proving:__doc__ -ff -v


[[
TODO:
    validate_primality__Nmm_ ++eR/ft_ex
TODO:
    iter_odd_primes__one_prime_per_bit_length_ certificate only g2
TODO:
    bug:may_ft4m
        _ex_check_setting4validate_primality__Nmm__partial_factorization_
    find prime/composite example for N**/3 ~ N**/2
TODO:
    is_composite_ex__Nmm_ ++fts/Bs
===
DONE:
    merge (g2, gs) into single ggg
    merge_partial_pseudo_primitive_roots_into_single_one
]]


[[
copy from:
    view others/数学/prime/primality_test.txt
===
# using complete factorization
# without gcd
[[[m :: pint][m%2==1][m>=3]
  [e2 :: pint][L :: uint][ps :: [pint]{len=L}][es :: [pint]{len=L}]
  # ps neednot be a set /distinguish
  [@[p :<- ps] -> [is_prime_(p)]]
  [e := 2**e2 * II ps[i]**es[i] {i :<- [0..<L]}]
  [g2 :: int][g2**(e///2) %m == m-1]
  [gs :: [int]{len=L}][@[i :<- [0..<L]] -> [gs[i]**(e///2///ps[i]) %m =!= m-1]][@[i :<- [0..<L]] -> [gs[i]**(e///2) %m == m-1]]
  ] -> [
  [phi(m) %e == 0]
  [[e == m-1] -> [is_prime_(m)]]
  ]
]

# using partial factorization
# using gcd
[[[m :: pint][m%2==1][m>=3]
  [e2 :: pint][L :: uint][fts :: [pint]{len=L}][es :: [pint]{len=L}]
  # fts neednot be pairwise-coprime
  [@[ft :<- fts] -> [[ft%2==1][ft>=3]]]
  [Bs :: [pint]{len=L}][@[i :<- [0..<L]] -> @[p4ft :<- all_prime_factors_of_(fts[i])] -> [p4ft >= Bs[i]]]
  [e5ft := 2**e2 * II fts[i]**es[i] {i :<- [0..<L]}]
  [e5B := 2**e2 * II Bs[i]**es[i] {i :<- [0..<L]}]
  [g2 :: int][g2**(e5ft///2) %m == m-1]
  [gs :: [int]{len=L}][@[i :<- [0..<L]] -> [gcd(gs[i]**(e5ft///2///fts[i]) %m +1, m) == 1]][@[i :<- [0..<L]] -> [gs[i]**(e5ft///2) %m == m-1]]

  ###
  [js := [i | [i :<- [0..<L]][fts[i] == Bs[i]]]]
  [ej := 2**e2 * II fts[j]**es[j] {j :<- js}]

  ] -> [
  ###
  [@[q4m :<- all_prime_factors_of_(m)] -> [(q4m-1) >= e5B]]
  [[(e5B+1)**2 > m] -> [is_prime_(m)]]

  ###
  [[e5ft == e5B] <==> [fts == Bs] <==> [@[ft :<- fts] -> [is_prime_(ft)]]]
  [[e5ft == e5B] -> [phi(m) %e5ft == 0]]
  [[e5ft == e5B] -> @[q4m :<- all_prime_factors_of_(m)] -> [(q4m-1) %e5ft == 0]]

  ###
  [e5ft %ej == 0]
  [e5B %ej == 0]
  [@[j :<- js] -> [is_prime_(fts[j])]]
  [[phi(m) %ej == 0][phi(m) ///ej >= e5B///ej][phi(m) >= e5B]]
  [@[q4m :<- all_prime_factors_of_(m)] -> [[(q4m-1) %ej == 0][(q4m-1) ///ej >= e5B///ej][(q4m-1) >= e5B]]]

  ###
  [[[e5ft==m-1][eF := ej][eR := e5ft///ej][gcd(eF,eR)==1]
    [u := if [e5ft%3 == 1] then 3 else 1]
    [(q,r) := eR /% (2*u*eF)]
    # [kB :: pint][[q4m :<- all_prime_factors_of_(m)] -> [(q4m-1)///eF >= kB]]
      # !! [(q4m-1) >= e5B]
      # !! [(q4m-1)///eF >= e5B///eF]
      # e.g. [kB := e5B///eF] #but select best to max rhs=(kB*eF +1) * (((2*u*eF) +r -kB)*eF +1)
    [kB := min(e5B///eF, (((2*u*eF) +r-1)///2))]
    [m < (kB*eF +1) * (((2*u*eF) +r -kB)*eF +1)]
    ] -> [
      [[is_prime_(m)] <-> [not$ [[r >= 2*kB][q >= ceil_(kB**2 /(2*u)) >= 1][sqrt(r**2 -8*u*q) %1 == 0]]]]
      [[[r >= 2*kB][q >= ceil_(kB**2 /(2*u)) >= 1][sqrt(r**2 -8*u*q) %1 == 0]] -> [
        [(s+t) == r]
        [(s-t) == sqrt(r**2 -8*u*q)]
        [m == (1+s*eF)*(1+t*eF)]
        ]]
      ]
    ]
  ]
]
]]
[[
copy from:
    view others/数学/prime/primality_test.txt
===
Miller's Test [Miller76]: If the extended Riemann hypothesis is true, then if n is an x-SPRP for all integers x with 1 < x < 2*(log n)**2 == 2*ln(n)**2, then n is prime.
    #require ERH
    2*ln(n)**2
heuristically we should be able to replace the bound in Miller's test with a bound near: (log 2)^-1 log n log log n.
  #heuristically
  #not exact
  ln(n)*lnln(n)/ln(2)
  log2(n)*lnln(n)


===
Note that there is no finite set of bases that will work in Miller's test.  In fact, if for n composite we let W(n) denote the least witness for n (the least x which shows n is composite), then there are infinitely many composite n with:
    [W(n) > (log n)**(1/(3 log log log n))]

===
Pocklington's Theorem (1914):  Let [n-1 = q**k *R] where q is a prime which does not divide R.  If there is an integer x such that [x**(n-1) %n == 1][gcd(x**((n-1)///q) %n -1,n) == 1], then each prime factor p of n has the form q**k*r+1.
    # [:Pocklington_Theorem_1914]:here
]]
[[
move from:
    #doc4Case4is_prime__Nmm_:here
===
view ../../python3_src/nn_ns/math_nn/numbers/b002233-least_positive_prime_primitive_root_of_n_th_prime__except_0th__fst_10000.txt
    [[least_positive_prime_primitive_root_of_(PRIMES[3417-1]) == 107][107 == PRIMES[27]][31771 == PRIMES[3416]][floor_log2(31771)==14][(31771-1)==II__p2e_({2: 1, 3: 2, 5: 1, 353: 1})]]
    ==>> [prime_bases<N> |>=| PRIMES[:1+2*floor_log2(N)]]
    ==>> [num_prime_bases<N> >= (1+2*floor_log2(N))]
===
view ../../python3_src/nn_ns/math_nn/numbers/b001918-least_positive_primitive_root_of_n_th_prime__fst_10000.txt
    [least_positive_primitive_root_of_(PRIMES[43-1]) == 19]
        43 19
        80 21
        326 23
        775 31
        3894 37
        5629 38
        7103 44

]]



from seed.math.primality_proving import *


[[[
old_version:
===
py_adhoc_call   seed.math.primality_proving   @test_many4is_prime_ex__Nmm_ =10_00
py_adhoc_call   seed.math.primality_proving   @test_many4is_prime_ex__Nmm_ =16_00_00
py_adhoc_call   seed.math.primality_proving   @test_many4is_prime_ex__Nmm_ =20_00_00
    pass test!
    setting:
        using_prime_base_as_primitive_root_candidate_only
        one_plus_2floor_log2_P
        partial_primitive_roots__vs__primitive_root=False
        [2 <= N < 20_00_00]
]]]




[[[
nontrivial_factor from result of is_composite_ex__Nmm_
===
>>> from seed.math.prime_gens import A014233
>>> for N in A014233:
...     try:
...         (N, is_composite_ex__Nmm_(N))
...     except Exception as e:
...         (N, e)
(2047, (True, (1, 23)))
(1373653, (True, (0, 5)))
(25326001, (True, (0, 7)))
(3215031751, (True, (1, 151)))
(2152302898747, (True, (1, 318246769)))
(3474749660383, (True, (1, 22055881)))
(341550071728321, (True, (1, 10670053)))
(341550071728321, (True, (1, 10670053)))
(3825123056546413051, (True, (1, 747451)))
(3825123056546413051, (True, (1, 747451)))
(3825123056546413051, (True, (1, 747451)))
(318665857834031151167461, (True, (1, 798330580441)))
(3317044064679887385961981, (True, (1, 2575672364521)))

]]]


[[[
py_adhoc_call   seed.math.primality_proving   ,200:iter_odd_primes__one_prime_per_bit_length_
===
(2, 3)
(3, 5)
(4, 13)
(5, 17)
(6, 41)
(7, 97)
(8, 241)
(9, 449)
(10, 641)
(11, 1217)
(12, 2113)
(13, None)
(14, None)
(15, None)
(16, None)
(17, 114689)
(18, None)
(19, None)
(20, 974849)
(21, None)
(22, 2424833)
(23, None)
(24, 13631489)
(25, 26017793)
(26, 63766529)
(27, None)
(28, 167772161)
... #choke
]]]



#py_adhoc_call   seed.math.primality_proving   ,200:iter_odd_primes__one_prime_per_bit_length_   %seed.math.primality_proving:N2num_prime_bases__heuristically@f   --case4prime_bases=f
[[[
py_adhoc_call   seed.math.primality_proving   ,200:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases=...
    #without +using_nonprime_gs4detect_primality
        #now the bug fixed
        #[:detect_ERH_counterexample]:goto
===
(2, 3)
(3, 5)
(4, 13)
(5, 17)
(6, 41)
(7, 97)
(8, 193)
(9, 257)
(10, 769)
(11, 1153)
(12, 3329)
(13, 7681)
???ERH???: 12289
(14, 13313)
???ERH???: 18433
(15, 19457)
???ERH???: 40961
???ERH???: 61441
???ERH???: 59393
(16, 37889)
???ERH???: 65537
(17, 114689)
???ERH???: 163841
???ERH???: 147457
???ERH???: 188417
???ERH???: 151553
???ERH???: 176129
???ERH???: 184321
???ERH???: 249857
(18, 133121)
???ERH???: 270337
???ERH???: 286721
???ERH???: 319489
???ERH???: 417793
???ERH???: 307201
???ERH???: 331777
???ERH???: 380929
???ERH???: 430081
???ERH???: 471041
???ERH???: 495617
???ERH???: 520193
(19, 301057)
???ERH???: 786433
???ERH???: 557057
???ERH???: 638977
???ERH???: 737281
???ERH???: 1032193
???ERH???: 778241
???ERH???: 925697
(20, 974849)
???ERH???: 1179649
???ERH???: 1376257
???ERH???: 1769473
???ERH???: 1146881
???ERH???: 1097729
???ERH???: 1130497
???ERH???: 1196033
???ERH???: 1589249
???ERH???: 1720321
???ERH???: 1785857
^CTraceback (most recent call last):
    ...
KeyboardInterrupt
]]]

[[[
#below after bug fixed:
    #bug:for case4prime_bases in _all_cases4prime_bases:
py_adhoc_call   seed.math.primality_proving   ,400:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing >> ~/my_tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt
    NOTE: 『:ERH』『+timing』

view /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt

===[output_after_bug_fixed:begin]
(2, 3)
(3, 5)
(4, 13)
(5, 17)
(6, 41)
(7, 97)
(8, 193)
(9, 257)
(10, 769)
(11, 1153)
(12, 3329)
(13, 7681)
(14, 12289)
(15, 18433)
(16, 40961)
(17, 65537)
(18, 163841)
(19, 270337)
(20, 786433)
(21, 1179649)
(22, 2752513)
(23, 7340033)
(24, 13631489)
(25, 23068673)
(26, 36175873)
(27, 104857601)
(28, 167772161)
(29, 469762049)
(30, 754974721)
(31, 2013265921)
(32, 3221225473)
(33, 7918845953)
(34, 12348030977)
(35, 24159191041)
(36, 52613349377)
(37, 77309411329)
(38, 206158430209)
(39, 313532612609)
(40, 850403524609)
(41, 2061584302081)
(42, 2748779069441)
(43, 6597069766657)
(44, 17317308137473)
(45, 29686813949953)
(46, 39582418599937)
(47, 79164837199873)
(48, 263882790666241)
(49, 474989023199233)
(50, 1108307720798209)
(51, 1337006139375617)
(52, 4222124650659841)
(53, 7881299347898369)
(54, 12947848928690177)
(55, 31525197391593473)
(56, 38280596832649217)
(57, 112589990684262401)
(58, 180143985094819841)
(59, 459367161991790593)
(60, 882705526964617217)
(61, 1945555039024054273)
(62, 4179340454199820289)
(63, 6269010681299730433)
(64, 15564440312192434177)
(65, 35740566642812256257)
(66, 51881467707308113921)
(67, 83010348331692982273)
(68, 221360928884514619393)
(69, 332041393326771929089)
(70, 691752902764108185601)
(71, 1328165573307087716353)
(72, 2434970217729660813313)
(73, 9149585060559937601537)
(74, 13576803638250229989377)
(75, 32613843522318487257089)
(76, 46043073207979040833537)
(77, 92086146415958081667073)
(78, 188894659314785808547841)
(79, 368344585663832326668289)
(80, 1095589024025757689577473)
(81, 1265594217409064917270529)
(82, 4533471823554859405148161)
(83, 7555786372591432341913601)
(84, 10955890240257576895774721)
(85, 21760664753063325144711169)
(86, 62864142619960717084721153)
(87, 150511264542021332250918913)
===[output_after_bug_fixed:end]
]]]

[[[
py_adhoc_call   seed.math.primality_proving   ,200:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases=...  +using_nonprime_gs4detect_primality
py_adhoc_call   seed.math.primality_proving   ,200:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases=...  +using_nonprime_gs4detect_primality =137
py_adhoc_call   seed.math.primality_proving   ,200:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases=...  +using_nonprime_gs4detect_primality =245
py_adhoc_call   seed.math.primality_proving   ,200:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases=...  +using_nonprime_gs4detect_primality =262
py_adhoc_call   seed.math.primality_proving   ,200:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases=...  +using_nonprime_gs4detect_primality =281
===below output [2..=286] with bug from above cmd:
    #bug:for case4prime_bases in _all_cases4prime_bases:
    #   ==>> [is_last===False]
    #   ==>> [tribool===True]
    #   ==>> [using_nonprime_gs4detect_primality===False]
but since setting 『--case4prime_bases=...』『all_cases4prime_bases is _all_cases4prime_bases』
==>> hence output are correct
===
vs:
    (23, None) # found bug <<== rerun with 『--case4prime_bases:ERH』
    (23, 7340033)
    (23,7<<20 ^1)
py_adhoc_call   seed.math.prime_gens @is_prime__le_pow2_81_ =7340033
True
echo $[7<<20 ^1]
7340033
===
===============================
===============================
===============================
===
#below cmd after bug fixed:
    #bug:for case4prime_bases in _all_cases4prime_bases:
===
NOTE: 『:ERH』『+timing』
py_adhoc_call   seed.math.primality_proving   ,1:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing  =286
286...: ... ...
(286, 122388140210220931467926100129881691118471630860284789838864181813550969967928135385089)
286...:duration: 117.654149882 *(unit: 0:00:01)
117.6 seconds ~ 2 minutes
上面是 『先素数后合数』方案
下面是 『一配比一』方案
287...:duration: 0.839426231 *(unit: 0:00:01)
===
py_adhoc_call   seed.math.primality_proving   ,30:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing  =287 > /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt
py_adhoc_call   seed.math.primality_proving   ,300:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing  =317 > /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt
py_adhoc_call   seed.math.primality_proving   ,200:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing  =503 > /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt
===
NOTE:『:ERH』『+timing』
NOTE:『+output_as_OddInt__ge3__repr_by_lshift_odd_plus1』
py_adhoc_call   seed.math.primality_proving   ,150:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing +output_as_OddInt__ge3__repr_by_lshift_odd_plus1 =552 > /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt
===
NOTE:『:ERH』『+timing』
NOTE:『+output_as_OddInt__ge3__repr_by_lshift_odd_plus1』
NOTE:『+with_certificate』『+output_composite』
py_adhoc_call   seed.math.primality_proving   ,50:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing +output_as_OddInt__ge3__repr_by_lshift_odd_plus1 +with_certificate
py_adhoc_call   seed.math.primality_proving   ,50:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing +output_as_OddInt__ge3__repr_by_lshift_odd_plus1 +with_certificate +output_composite
py_adhoc_call   seed.math.primality_proving   ,1025:iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing +output_as_OddInt__ge3__repr_by_lshift_odd_plus1 +with_certificate +output_composite > /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt
    ...只到[num_bits==80](!刚刚好1025行!)，因为 合数 占用了 900多个坑

py_adhoc_call   seed.math.primality_proving   ,iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing +output_as_OddInt__ge3__repr_by_lshift_odd_plus1 +with_certificate +output_composite --end=1026 > /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt
    cellphone kill Termux:halt at:48688row:(535, 533<<525^1, 139)

should continue@(535, 533<<525^1, 139)
try continue@(12, 7<<9^1, 3)

py_adhoc_call   seed.math.primality_proving   ,iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing +output_as_OddInt__ge3__repr_by_lshift_odd_plus1 +with_certificate +output_composite --end=13 =12 --begin_odd4first_num_bits=9
12...: ... ...
(12, 9<<8^1, 5)
(12, 11<<8^1, 3)
(12, 13<<8^1, [3, 2])
12...:duration: 0.00326738400000004 *(unit: 0:00:01)

py_adhoc_call   seed.math.primality_proving   ,iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing +output_as_OddInt__ge3__repr_by_lshift_odd_plus1 +with_certificate +output_composite --end=13 =12
    ok

continue@(535, 533<<525^1, 139)
py_adhoc_call   seed.math.primality_proving   ,iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing +output_as_OddInt__ge3__repr_by_lshift_odd_plus1 +with_certificate +output_composite --end=536 =535 --begin_odd4first_num_bits=535   >> /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt
    48858row:(535, 873<<525^1, [10, 2])

py_adhoc_call   seed.math.primality_proving   ,iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing +output_as_OddInt__ge3__repr_by_lshift_odd_plus1 +with_certificate +output_composite --end=1026 =536   >> /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt
56501row:(577, 275<<568^1, 3)
1.1 MB

py_adhoc_call   seed.math.primality_proving   ,iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing +output_as_OddInt__ge3__repr_by_lshift_odd_plus1 +with_certificate +output_composite --end=1026 =577 --begin_odd4first_num_bits=277   >> /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt
62243row:(607, 257<<598^1, 3)
1.2 MB

py_adhoc_call   seed.math.primality_proving   @continue4iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing +output_as_OddInt__ge3__repr_by_lshift_odd_plus1 +with_certificate +output_composite --end=608   :/sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt
    ok
    begin_odd4first_num_bits『2+』
py_adhoc_call   seed.math.primality_proving   @continue4iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing +output_as_OddInt__ge3__repr_by_lshift_odd_plus1 +with_certificate +output_composite --end=609   :/sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt
    ok
    begin『1+』
py_adhoc_call   seed.math.primality_proving   @continue4iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing +output_as_OddInt__ge3__repr_by_lshift_odd_plus1 +with_certificate +output_composite    :/sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt  --end=1026
74726row:(670, 665<<660^1, 3)
86221row:(718, 35<<712^1, 3)
py_adhoc_call   seed.math.primality_proving   @continue4iter_odd_primes__one_prime_per_bit_length_     --case4prime_bases:ERH  +using_nonprime_gs4detect_primality  +timing +output_as_OddInt__ge3__repr_by_lshift_odd_plus1 +with_certificate +output_composite    :/sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt  --end=719
86222row:(718, 37<<712^1, [6, 2])
    1.7 MB

validate_output5iter_odd_primes__one_prime_per_bit_length_
py_adhoc_call   seed.math.primality_proving   @validate_output5iter_odd_primes__one_prime_per_bit_length_   +to_validate_continuity  +to_validate_certificate  +had_output_composite    :/sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt
py_adhoc_call   seed.math.primality_proving   @validate_output5iter_odd_primes__one_prime_per_bit_length_   +to_validate_continuity  +to_validate_certificate  +had_output_composite    :../../python3_src/seed/math/_output_/seed.math.primality_proving..continue4iter_odd_primes__one_prime_per_bit_length_.end-719.txt
py_adhoc_call   seed.math.primality_proving   @validate_output5iter_odd_primes__one_prime_per_bit_length_   +to_validate_continuity  -to_validate_certificate  +had_output_composite    :../../python3_src/seed/math/_output_/seed.math.primality_proving..continue4iter_odd_primes__one_prime_per_bit_length_.end-719.txt
    『-to_validate_certificate』

filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_
py_adhoc_call   seed.math.primality_proving   ,filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_   +output_as_OddInt__ge3__repr_by_lshift_odd_plus1     :../../python3_src/seed/math/_output_/seed.math.primality_proving..continue4iter_odd_primes__one_prime_per_bit_length_.end-719.txt  >  ../../python3_src/seed/math/_output_/seed.math.primality_proving..filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_.end-719.txt
    20 KB
py_adhoc_call   seed.math.primality_proving   @validate_output5iter_odd_primes__one_prime_per_bit_length_   +to_validate_continuity  +to_validate_certificate  -had_output_composite    :../../python3_src/seed/math/_output_/seed.math.primality_proving..filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_.end-719.txt
    『-had_output_composite』
===
view /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt
!du -h /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt
!cp /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt  /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt.bak
view /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt.bak
!cp /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt.bak  /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt
!cp /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt  /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt.bak2
!cp /sdcard/0my_files/tmp/out4py/seed.math.primality_proving..iter_odd_primes__one_prime_per_bit_length_.out.txt  ../../python3_src/seed/math/_output_/seed.math.primality_proving..continue4iter_odd_primes__one_prime_per_bit_length_.end-719.txt
view ../../python3_src/seed/math/_output_/seed.math.primality_proving..continue4iter_odd_primes__one_prime_per_bit_length_.end-719.txt
!mv ../../python3_src/seed/math/_output_/seed.math.primality_proving..continue4iter_odd_primes__one_prime_per_bit_length_.end-719.prime_only.txt   ../../python3_src/seed/math/_output_/seed.math.primality_proving..filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_.end-719.txt
!du -h ../../python3_src/seed/math/_output_/seed.math.primality_proving..filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_.end-719.txt
===
view ../../python3_src/seed/math/_output_/seed.math.primality_proving..filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_.end-719.txt
    # output5iter_odd_primes__one_prime_per_bit_length_,output5reformat_output5iter_odd_primes__one_prime_per_bit_length_ are deprecated by output5filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_
===[output5filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_:begin]
(2, 1<<1^1, [2])
(3, 1<<2^1, [2])
(4, 3<<2^1, [2, 2])
(5, 1<<4^1, [3])
(6, 5<<3^1, [3, 2])
(7, 3<<5^1, [5, 2])
(8, 3<<6^1, [5, 2])
(9, 1<<8^1, [3])
(10, 3<<8^1, [7, 2])
(11, 9<<7^1, [5, 2])
(12, 13<<8^1, [3, 2])
(13, 15<<9^1, [13, 2])
(14, 3<<12^1, [22, 2])
(15, 9<<11^1, [10, 2])
(16, 5<<13^1, [6, 2])
(17, 1<<16^1, [6])
(18, 5<<15^1, [6, 2])
(19, 33<<13^1, [10, 2])
(20, 3<<18^1, [10, 2])
(21, 9<<17^1, [38, 2])
(22, 21<<17^1, [10, 2])
(23, 7<<20^1, [6, 2])
(24, 13<<20^1, [3, 5])
(25, 11<<21^1, [6, 2])
(26, 69<<19^1, [10, 2])
(27, 25<<22^1, [6, 2])
(28, 5<<25^1, [3, 3])
(29, 7<<26^1, [6, 2])
(30, 45<<24^1, [22, 2])
(31, 15<<27^1, [22, 2])
(32, 3<<30^1, [10, 2])
(33, 59<<27^1, [6, 2])
(34, 23<<29^1, [6, 2])
(35, 45<<29^1, [14, 2])
(36, 49<<30^1, [6, 2])
(37, 9<<33^1, [14, 2])
(38, 3<<36^1, [22, 2])
(39, 73<<32^1, [6, 2])
(40, 99<<33^1, [26, 2])
(41, 15<<37^1, [14, 2])
(42, 5<<39^1, [3, 3])
(43, 3<<41^1, [5, 5])
(44, 63<<38^1, [10, 2])
(45, 27<<40^1, [10, 2])
(46, 9<<42^1, [10, 2])
(47, 9<<43^1, [10, 2])
(48, 15<<44^1, [14, 2])
(49, 27<<44^1, [10, 2])
(50, 63<<44^1, [22, 2])
(51, 19<<46^1, [6, 2])
(52, 15<<48^1, [22, 2])
(53, 7<<50^1, [6, 2])
(54, 23<<49^1, [6, 2])
(55, 7<<52^1, [6, 2])
(56, 17<<51^1, [6, 2])
(57, 25<<52^1, [6, 2])
(58, 5<<55^1, [6, 2])
(59, 51<<53^1, [10, 2])
(60, 49<<54^1, [6, 2])
(61, 27<<56^1, [10, 2])
(62, 29<<57^1, [3, 3])
(63, 87<<56^1, [10, 2])
(64, 27<<59^1, [10, 2])
(65, 31<<60^1, [6, 2])
(66, 45<<60^1, [22, 2])
(67, 9<<63^1, [10, 2])
(68, 3<<66^1, [10, 2])
(69, 9<<65^1, [38, 2])
(70, 75<<63^1, [14, 2])
(71, 9<<67^1, [5, 7])
(72, 33<<66^1, [10, 2])
(73, 31<<68^1, [6, 2])
(74, 23<<69^1, [6, 2])
(75, 221<<67^1, [6, 2])
(76, 39<<70^1, [10, 2])
(77, 39<<71^1, [10, 2])
(78, 5<<75^1, [3, 3])
(79, 39<<73^1, [34, 2])
(80, 29<<75^1, [6, 2])
(81, 67<<74^1, [6, 2])
(82, 15<<78^1, [22, 2])
(83, 25<<78^1, [6, 2])
(84, 145<<76^1, [6, 2])
(85, 9<<81^1, [14, 2])
(86, 13<<82^1, [6, 2])
(87, 249<<79^1, [10, 2])
(88, 5<<85^1, [6, 2])
(89, 51<<83^1, [22, 2])
(90, 37<<84^1, [6, 2])
(91, 53<<85^1, [6, 2])
(92, 65<<85^1, [6, 2])
(93, 87<<86^1, [14, 2])
(94, 61<<88^1, [6, 2])
(95, 7<<92^1, [6, 2])
(96, 57<<90^1, [46, 2])
(97, 27<<92^1, [10, 2])
(98, 29<<93^1, [6, 2])
(99, 33<<93^1, [10, 2])
(100, 43<<94^1, [6, 2])
(101, 85<<94^1, [6, 2])
(102, 57<<96^1, [10, 2])
(103, 121<<96^1, [6, 2])
(104, 43<<98^1, [6, 2])
(105, 131<<97^1, [6, 2])
(106, 315<<97^1, [22, 2])
(107, 219<<99^1, [10, 2])
(108, 29<<103^1, [6, 2])
(109, 67<<102^1, [6, 2])
(110, 43<<104^1, [6, 2])
(111, 53<<105^1, [6, 2])
(112, 37<<106^1, [6, 2])
(113, 231<<105^1, [10, 2])
(114, 105<<107^1, [22, 2])
(115, 93<<108^1, [14, 2])
(116, 15<<112^1, [14, 2])
(117, 73<<110^1, [6, 2])
(118, 95<<111^1, [6, 2])
(119, 129<<111^1, [10, 2])
(120, 153<<112^1, [14, 2])
(121, 115<<114^1, [6, 2])
(122, 163<<114^1, [6, 2])
(123, 7<<120^1, [3, 3])
(124, 33<<118^1, [10, 2])
(125, 51<<119^1, [22, 2])
(126, 71<<119^1, [6, 2])
(127, 177<<119^1, [10, 2])
(128, 81<<121^1, [10, 2])
(129, 11<<125^1, [6, 2])
(130, 5<<127^1, [3, 7])
(131, 11<<127^1, [6, 2])
(132, 81<<125^1, [10, 2])
(133, 21<<128^1, [10, 2])
(134, 21<<129^1, [10, 2])
(135, 111<<128^1, [10, 2])
(136, 65<<129^1, [6, 2])
(137, 295<<128^1, [6, 2])
(138, 9<<134^1, [10, 2])
(139, 53<<133^1, [6, 2])
(140, 247<<132^1, [6, 2])
(141, 67<<134^1, [6, 2])
(142, 147<<134^1, [22, 2])
(143, 225<<135^1, [22, 2])
(144, 111<<137^1, [10, 2])
(145, 31<<140^1, [6, 2])
(146, 219<<138^1, [10, 2])
(147, 355<<138^1, [6, 2])
(148, 29<<143^1, [6, 2])
(149, 141<<141^1, [10, 2])
(150, 43<<144^1, [6, 2])
(151, 249<<143^1, [10, 2])
(152, 17<<147^1, [3, 3])
(153, 35<<147^1, [6, 2])
(154, 175<<146^1, [6, 2])
(155, 81<<148^1, [10, 2])
(156, 163<<148^1, [6, 2])
(157, 191<<149^1, [6, 2])
(158, 65<<151^1, [6, 2])
(159, 63<<153^1, [10, 2])
(160, 315<<151^1, [26, 2])
(161, 131<<153^1, [6, 2])
(162, 105<<155^1, [22, 2])
(163, 117<<156^1, [10, 2])
(164, 43<<158^1, [6, 2])
(165, 183<<157^1, [10, 2])
(166, 9<<162^1, [10, 2])
(167, 225<<159^1, [26, 2])
(168, 141<<160^1, [10, 2])
(169, 99<<162^1, [10, 2])
(170, 75<<163^1, [22, 2])
(171, 93<<164^1, [26, 2])
(172, 15<<168^1, [22, 2])
(173, 131<<165^1, [6, 2])
(174, 61<<168^1, [6, 2])
(175, 91<<168^1, [6, 2])
(176, 165<<168^1, [14, 2])
(177, 7<<174^1, [6, 2])
(178, 177<<170^1, [22, 2])
(179, 207<<171^1, [10, 2])
(180, 27<<175^1, [10, 2])
(181, 51<<175^1, [14, 2])
(182, 95<<175^1, [6, 2])
(183, 7<<180^1, [6, 2])
(184, 347<<175^1, [6, 2])
(185, 333<<176^1, [14, 2])
(186, 299<<177^1, [6, 2])
(187, 127<<180^1, [6, 2])
(188, 83<<181^1, [6, 2])
(189, 25<<184^1, [6, 2])
(190, 29<<185^1, [6, 2])
(191, 3<<189^1, [10, 2])
(192, 13<<188^1, [6, 2])
(193, 7<<190^1, [6, 2])
(194, 187<<186^1, [6, 2])
(195, 45<<189^1, [22, 2])
(196, 57<<190^1, [14, 2])
(197, 617<<187^1, [6, 2])
(198, 159<<190^1, [10, 2])
(199, 149<<191^1, [6, 2])
(200, 111<<193^1, [10, 2])
(201, 183<<193^1, [10, 2])
(202, 163<<194^1, [6, 2])
(203, 3<<201^1, [10, 2])
(204, 261<<195^1, [14, 2])
(205, 203<<197^1, [6, 2])
(206, 45<<200^1, [14, 2])
(207, 85<<200^1, [6, 2])
(208, 181<<200^1, [6, 2])
(209, 191<<201^1, [6, 2])
(210, 9<<206^1, [10, 2])
(211, 3<<209^1, [5, 7])
(212, 65<<205^1, [6, 2])
(213, 11<<209^1, [6, 2])
(214, 21<<209^1, [10, 2])
(215, 9<<211^1, [10, 2])
(216, 275<<207^1, [6, 2])
(217, 261<<208^1, [10, 2])
(218, 99<<211^1, [10, 2])
(219, 73<<212^1, [6, 2])
(220, 27<<215^1, [10, 2])
(221, 31<<216^1, [6, 2])
(222, 105<<215^1, [22, 2])
(223, 505<<214^1, [6, 2])
(224, 183<<216^1, [26, 2])
(225, 615<<215^1, [22, 2])
(226, 55<<220^1, [6, 2])
(227, 279<<218^1, [10, 2])
(228, 381<<219^1, [22, 2])
(229, 75<<222^1, [14, 2])
(230, 395<<221^1, [6, 2])
(231, 245<<223^1, [6, 2])
(232, 351<<223^1, [14, 2])
(233, 15<<229^1, [14, 3])
(234, 63<<228^1, [34, 2])
(235, 115<<228^1, [6, 2])
(236, 29<<231^1, [3, 3])
(237, 25<<232^1, [6, 2])
(238, 195<<230^1, [34, 2])
(239, 207<<231^1, [10, 2])
(240, 83<<233^1, [6, 2])
(241, 285<<232^1, [22, 2])
(242, 37<<236^1, [6, 2])
(243, 67<<236^1, [6, 2])
(244, 95<<237^1, [6, 2])
(245, 67<<238^1, [6, 2])
(246, 65<<239^1, [6, 2])
(247, 533<<237^1, [6, 2])
(248, 17<<243^1, [6, 2])
(249, 291<<240^1, [10, 2])
(250, 29<<245^1, [6, 2])
(251, 35<<245^1, [6, 2])
(252, 177<<244^1, [10, 2])
(253, 203<<245^1, [6, 2])
(254, 75<<247^1, [26, 2])
(255, 167<<247^1, [6, 2])
(256, 207<<248^1, [10, 2])
(257, 39<<251^1, [10, 2])
(258, 43<<252^1, [6, 2])
(259, 313<<250^1, [6, 2])
(260, 37<<254^1, [6, 2])
(261, 135<<253^1, [14, 2])
(262, 633<<252^1, [34, 2])
(263, 51<<257^1, [10, 2])
(264, 65<<257^1, [6, 2])
(265, 239<<257^1, [6, 2])
(266, 147<<258^1, [22, 2])
(267, 91<<260^1, [6, 2])
(268, 55<<262^1, [6, 2])
(269, 51<<263^1, [22, 2])
(270, 159<<262^1, [10, 2])
(271, 121<<264^1, [6, 2])
(272, 17<<267^1, [6, 2])
(273, 25<<268^1, [6, 2])
(274, 81<<267^1, [14, 2])
(275, 123<<268^1, [22, 2])
(276, 175<<268^1, [6, 2])
(277, 99<<270^1, [10, 2])
(278, 3<<276^1, [22, 2])
(279, 177<<271^1, [10, 3])
(280, 27<<275^1, [10, 2])
(281, 21<<276^1, [10, 3])
(282, 261<<273^1, [10, 2])
(283, 147<<275^1, [10, 2])
(284, 81<<277^1, [10, 2])
(285, 297<<276^1, [10, 2])
(286, 63<<280^1, [26, 2])
(287, 231<<279^1, [34, 2])
(288, 125<<281^1, [6, 2])
(289, 357<<280^1, [10, 2])
(290, 135<<282^1, [14, 2])
(291, 325<<282^1, [6, 2])
(292, 37<<286^1, [6, 2])
(293, 7<<290^1, [3, 3])
(294, 77<<287^1, [6, 2])
(295, 33<<289^1, [10, 2])
(296, 37<<290^1, [6, 2])
(297, 59<<291^1, [6, 2])
(298, 107<<291^1, [6, 2])
(299, 141<<291^1, [22, 2])
(300, 287<<291^1, [6, 2])
(301, 15<<297^1, [22, 2])
(302, 177<<294^1, [14, 2])
(303, 81<<296^1, [10, 2])
(304, 207<<296^1, [10, 2])
(305, 93<<298^1, [10, 2])
(306, 71<<299^1, [6, 2])
(307, 177<<299^1, [10, 2])
(308, 389<<299^1, [6, 2])
(309, 267<<300^1, [10, 2])
(310, 107<<303^1, [6, 2])
(311, 141<<303^1, [22, 2])
(312, 13<<308^1, [6, 2])
(313, 239<<305^1, [6, 2])
(314, 65<<307^1, [6, 2])
(315, 231<<307^1, [26, 2])
(316, 285<<307^1, [34, 2])
(317, 957<<307^1, [10, 2])
(318, 21<<313^1, [10, 2])
(319, 75<<312^1, [14, 2])
(320, 13<<316^1, [6, 2])
(321, 153<<313^1, [10, 2])
(322, 207<<314^1, [14, 2])
(323, 7<<320^1, [3, 5])
(324, 559<<314^1, [6, 2])
(325, 109<<318^1, [6, 2])
(326, 99<<319^1, [10, 2])
(327, 51<<321^1, [10, 2])
(328, 177<<320^1, [10, 2])
(329, 457<<320^1, [6, 2])
(330, 625<<320^1, [6, 2])
(331, 81<<324^1, [10, 2])
(332, 63<<326^1, [10, 2])
(333, 35<<327^1, [6, 2])
(334, 561<<324^1, [10, 2])
(335, 469<<326^1, [6, 2])
(336, 297<<327^1, [10, 2])
(337, 261<<328^1, [10, 2])
(338, 125<<331^1, [6, 2])
(339, 45<<333^1, [26, 2])
(340, 63<<334^1, [10, 2])
(341, 143<<333^1, [6, 2])
(342, 177<<334^1, [14, 2])
(343, 15<<339^1, [38, 2])
(344, 133<<336^1, [6, 2])
(345, 25<<340^1, [6, 2])
(346, 23<<341^1, [6, 2])
(347, 159<<339^1, [10, 2])
(348, 559<<338^1, [6, 2])
(349, 67<<342^1, [6, 2])
(350, 55<<344^1, [6, 2])
(351, 81<<344^1, [10, 2])
(352, 17<<347^1, [6, 2])
(353, 301<<344^1, [6, 2])
(354, 423<<345^1, [10, 2])
(355, 3<<353^1, [10, 2])
(356, 201<<348^1, [10, 2])
(357, 941<<347^1, [6, 2])
(358, 65<<351^1, [6, 2])
(359, 161<<351^1, [6, 2])
(360, 165<<352^1, [26, 2])
(361, 35<<355^1, [6, 2])
(362, 55<<356^1, [6, 2])
(363, 231<<355^1, [26, 2])
(364, 253<<356^1, [6, 2])
(365, 265<<356^1, [6, 2])
(366, 261<<357^1, [10, 2])
(367, 189<<359^1, [10, 2])
(368, 281<<359^1, [6, 2])
(369, 131<<361^1, [6, 2])
(370, 9<<366^1, [10, 2])
(371, 19<<366^1, [6, 2])
(372, 113<<365^1, [6, 2])
(373, 195<<365^1, [46, 2])
(374, 993<<364^1, [14, 2])
(375, 555<<365^1, [22, 2])
(376, 39<<370^1, [10, 2])
(377, 171<<369^1, [10, 2])
(378, 45<<372^1, [26, 2])
(379, 197<<371^1, [6, 2])
(380, 83<<373^1, [6, 2])
(381, 39<<375^1, [10, 2])
(382, 195<<374^1, [22, 2])
(383, 725<<373^1, [6, 2])
(384, 285<<375^1, [14, 2])
(385, 41<<379^1, [6, 2])
(386, 23<<381^1, [6, 2])
(387, 159<<379^1, [10, 2])
(388, 211<<380^1, [6, 2])
(389, 67<<382^1, [6, 2])
(390, 235<<382^1, [6, 2])
(391, 735<<381^1, [22, 2])
(392, 485<<383^1, [6, 2])
(393, 7<<390^1, [6, 2])
(394, 23<<389^1, [6, 2])
(395, 39<<389^1, [14, 2])
(396, 29<<391^1, [6, 2])
(397, 183<<389^1, [10, 2])
(398, 55<<392^1, [6, 2])
(399, 105<<392^1, [58, 2])
(400, 347<<391^1, [6, 2])
(401, 143<<393^1, [6, 2])
(402, 21<<397^1, [10, 2])
(403, 81<<396^1, [10, 2])
(404, 57<<398^1, [14, 2])
(405, 93<<398^1, [10, 2])
(406, 1095<<395^1, [14, 2])
(407, 97<<400^1, [6, 2])
(408, 613<<398^1, [6, 2])
(409, 585<<399^1, [14, 2])
(410, 3<<408^1, [22, 2])
(411, 465<<402^1, [22, 2])
(412, 27<<407^1, [10, 2])
(413, 39<<407^1, [10, 2])
(414, 169<<406^1, [6, 2])
(415, 861<<405^1, [10, 2])
(416, 63<<410^1, [10, 2])
(417, 99<<410^1, [10, 2])
(418, 33<<412^1, [38, 2])
(419, 403<<410^1, [6, 2])
(420, 105<<413^1, [26, 2])
(421, 31<<416^1, [6, 2])
(422, 129<<414^1, [10, 2])
(423, 327<<414^1, [14, 2])
(424, 71<<417^1, [6, 2])
(425, 291<<416^1, [10, 2])
(426, 877<<416^1, [6, 2])
(427, 179<<419^1, [6, 2])
(428, 81<<421^1, [10, 2])
(429, 1059<<418^1, [10, 2])
(430, 393<<421^1, [10, 2])
(431, 933<<421^1, [10, 2])
(432, 843<<422^1, [10, 2])
(433, 765<<423^1, [14, 2])
(434, 565<<424^1, [6, 2])
(435, 7<<432^1, [6, 2])
(436, 1505<<425^1, [6, 2])
(437, 75<<430^1, [22, 2])
(438, 225<<430^1, [14, 2])
(439, 953<<429^1, [6, 2])
(440, 3<<438^1, [10, 2])
(441, 105<<434^1, [26, 2])
(442, 193<<434^1, [6, 2])
(443, 81<<436^1, [10, 2])
(444, 745<<434^1, [6, 2])
(445, 155<<437^1, [6, 2])
(446, 419<<437^1, [6, 2])
(447, 177<<439^1, [10, 2])
(448, 223<<440^1, [6, 2])
(449, 45<<443^1, [14, 2])
(450, 177<<442^1, [14, 2])
(451, 683<<441^1, [6, 2])
(452, 261<<443^1, [22, 2])
(453, 25<<448^1, [6, 2])
(454, 81<<447^1, [14, 2])
(455, 155<<447^1, [6, 2])
(456, 955<<446^1, [6, 2])
(457, 333<<448^1, [22, 2])
(458, 1181<<447^1, [6, 2])
(459, 33<<453^1, [10, 2])
(460, 27<<455^1, [10, 3])
(461, 67<<454^1, [6, 2])
(462, 57<<456^1, [10, 2])
(463, 115<<456^1, [6, 2])
(464, 449<<455^1, [6, 2])
(465, 611<<455^1, [6, 2])
(466, 585<<456^1, [14, 2])
(467, 135<<459^1, [14, 2])
(468, 669<<458^1, [10, 2])
(469, 313<<460^1, [6, 2])
(470, 45<<464^1, [14, 2])
(471, 539<<461^1, [6, 2])
(472, 183<<464^1, [14, 2])
(473, 131<<465^1, [6, 2])
(474, 323<<465^1, [6, 2])
(475, 137<<467^1, [6, 2])
(476, 17<<471^1, [6, 2])
(477, 67<<470^1, [6, 2])
(478, 293<<469^1, [6, 2])
(479, 551<<469^1, [6, 2])
(480, 595<<470^1, [6, 2])
(481, 445<<472^1, [6, 2])
(482, 249<<474^1, [10, 2])
(483, 123<<476^1, [14, 2])
(484, 459<<475^1, [10, 2])
(485, 447<<476^1, [10, 2])
(486, 65<<479^1, [6, 2])
(487, 819<<477^1, [34, 2])
(488, 261<<479^1, [26, 2])
(489, 115<<482^1, [6, 2])
(490, 77<<483^1, [6, 2])
(491, 53<<485^1, [6, 2])
(492, 181<<484^1, [6, 2])
(493, 669<<483^1, [10, 2])
(494, 253<<486^1, [6, 2])
(495, 283<<486^1, [6, 2])
(496, 141<<488^1, [10, 2])
(497, 105<<490^1, [22, 2])
(498, 125<<491^1, [6, 2])
(499, 873<<489^1, [10, 2])
(500, 1101<<489^1, [10, 2])
(501, 239<<493^1, [6, 2])
(502, 299<<493^1, [6, 2])
(503, 433<<494^1, [6, 2])
(504, 1451<<493^1, [6, 2])
(505, 185<<497^1, [6, 2])
(506, 625<<496^1, [6, 2])
(507, 295<<498^1, [6, 2])
(508, 57<<502^1, [14, 2])
(509, 629<<499^1, [6, 2])
(510, 711<<500^1, [10, 2])
(511, 127<<504^1, [6, 2])
(512, 2401<<500^1, [6, 2])
(513, 519<<503^1, [10, 2])
(514, 745<<504^1, [6, 2])
(515, 755<<505^1, [6, 2])
(516, 113<<509^1, [6, 2])
(517, 267<<508^1, [10, 2])
(518, 249<<510^1, [10, 2])
(519, 783<<509^1, [10, 2])
(520, 101<<513^1, [6, 2])
(521, 15<<517^1, [14, 2])
(522, 69<<515^1, [10, 2])
(523, 921<<513^1, [10, 2])
(524, 39<<518^1, [10, 2])
(525, 87<<518^1, [14, 2])
(526, 15<<522^1, [22, 2])
(527, 417<<518^1, [14, 2])
(528, 371<<519^1, [6, 2])
(529, 233<<521^1, [6, 2])
(530, 169<<522^1, [6, 2])
(531, 33<<525^1, [10, 2])
(532, 823<<522^1, [6, 2])
(533, 367<<524^1, [6, 2])
(534, 189<<526^1, [10, 2])
(535, 873<<525^1, [10, 2])
(536, 3<<534^1, [10, 2])
(537, 131<<529^1, [6, 2])
(538, 813<<528^1, [26, 2])
(539, 277<<530^1, [6, 2])
(540, 95<<533^1, [6, 2])
(541, 959<<531^1, [6, 2])
(542, 169<<534^1, [6, 2])
(543, 141<<535^1, [14, 2])
(544, 163<<536^1, [6, 2])
(545, 79<<538^1, [6, 2])
(546, 81<<539^1, [14, 2])
(547, 385<<538^1, [6, 2])
(548, 193<<540^1, [6, 2])
(549, 465<<540^1, [26, 2])
(550, 1229<<539^1, [6, 2])
(551, 545<<541^1, [6, 2])
(552, 151<<544^1, [6, 2])
(553, 255<<545^1, [14, 2])
(554, 1457<<543^1, [6, 2])
(555, 225<<547^1, [14, 3])
(556, 435<<547^1, [14, 2])
(557, 677<<547^1, [6, 2])
(558, 637<<548^1, [6, 2])
(559, 25<<554^1, [6, 2])
(560, 65<<553^1, [6, 2])
(561, 645<<551^1, [14, 2])
(562, 441<<553^1, [10, 2])
(563, 141<<555^1, [26, 2])
(564, 141<<556^1, [10, 2])
(565, 127<<558^1, [3, 3])
(566, 77<<559^1, [6, 2])
(567, 393<<558^1, [10, 2])
(568, 151<<560^1, [6, 2])
(569, 363<<560^1, [26, 2])
(570, 145<<562^1, [6, 2])
(571, 319<<562^1, [6, 2])
(572, 507<<563^1, [10, 2])
(573, 731<<563^1, [6, 2])
(574, 107<<567^1, [6, 2])
(575, 741<<565^1, [10, 2])
(576, 285<<567^1, [14, 2])
(577, 361<<568^1, [6, 2])
(578, 345<<569^1, [34, 2])
(579, 337<<570^1, [6, 2])
(580, 627<<570^1, [14, 2])
(581, 705<<571^1, [26, 2])
(582, 765<<572^1, [38, 2])
(583, 171<<575^1, [14, 2])
(584, 81<<577^1, [10, 2])
(585, 327<<576^1, [10, 2])
(586, 1061<<575^1, [6, 2])
(587, 319<<578^1, [6, 2])
(588, 125<<581^1, [6, 2])
(589, 47<<583^1, [6, 2])
(590, 363<<581^1, [10, 2])
(591, 427<<582^1, [6, 2])
(592, 567<<582^1, [26, 2])
(593, 215<<585^1, [6, 2])
(594, 531<<584^1, [10, 2])
(595, 519<<585^1, [22, 2])
(596, 89<<589^1, [6, 2])
(597, 161<<589^1, [6, 2])
(598, 555<<588^1, [14, 2])
(599, 81<<592^1, [10, 2])
(600, 49<<594^1, [6, 2])
(601, 233<<593^1, [6, 2])
(602, 961<<592^1, [6, 2])
(603, 245<<595^1, [6, 2])
(604, 183<<596^1, [14, 2])
(605, 67<<598^1, [6, 2])
(606, 955<<596^1, [6, 2])
(607, 659<<597^1, [6, 2])
(608, 133<<600^1, [6, 2])
(609, 87<<602^1, [14, 2])
(610, 1469<<599^1, [6, 2])
(611, 319<<602^1, [6, 2])
(612, 207<<604^1, [10, 2])
(613, 701<<603^1, [6, 2])
(614, 263<<605^1, [6, 2])
(615, 581<<605^1, [6, 2])
(616, 347<<607^1, [6, 2])
(617, 189<<609^1, [22, 2])
(618, 305<<609^1, [6, 2])
(619, 7<<616^1, [6, 2])
(620, 275<<611^1, [6, 2])
(621, 267<<612^1, [10, 2])
(622, 655<<612^1, [6, 2])
(623, 103<<616^1, [6, 2])
(624, 401<<615^1, [6, 2])
(625, 265<<616^1, [6, 2])
(626, 783<<616^1, [14, 2])
(627, 611<<617^1, [6, 2])
(628, 95<<621^1, [6, 2])
(629, 103<<622^1, [6, 2])
(630, 345<<621^1, [14, 2])
(631, 85<<624^1, [6, 2])
(632, 63<<626^1, [10, 2])
(633, 231<<625^1, [10, 2])
(634, 345<<625^1, [14, 2])
(635, 621<<625^1, [10, 2])
(636, 449<<627^1, [6, 2])
(637, 947<<627^1, [6, 2])
(638, 99<<631^1, [10, 2])
(639, 725<<629^1, [6, 2])
(640, 101<<633^1, [6, 2])
(641, 179<<633^1, [6, 2])
(642, 865<<632^1, [6, 2])
(643, 621<<633^1, [10, 2])
(644, 145<<636^1, [6, 2])
(645, 203<<637^1, [6, 2])
(646, 955<<636^1, [6, 2])
(647, 405<<638^1, [22, 2])
(648, 141<<640^1, [10, 2])
(649, 221<<641^1, [6, 2])
(650, 117<<643^1, [10, 2])
(651, 1063<<640^1, [6, 2])
(652, 619<<642^1, [6, 2])
(653, 1065<<642^1, [26, 2])
(654, 23<<649^1, [6, 2])
(655, 237<<647^1, [10, 2])
(656, 275<<647^1, [6, 2])
(657, 155<<649^1, [6, 2])
(658, 15<<654^1, [22, 2])
(659, 97<<652^1, [6, 2])
(660, 1029<<649^1, [26, 2])
(661, 471<<652^1, [10, 2])
(662, 77<<655^1, [6, 2])
(663, 735<<653^1, [22, 2])
(664, 387<<655^1, [10, 2])
(665, 183<<657^1, [10, 2])
(666, 1247<<655^1, [6, 2])
(667, 9<<663^1, [10, 2])
(668, 95<<661^1, [6, 2])
(669, 25<<664^1, [6, 2])
(670, 667<<660^1, [6, 2])
(671, 357<<662^1, [22, 2])
(672, 495<<663^1, [14, 2])
(673, 179<<665^1, [6, 2])
(674, 77<<667^1, [6, 2])
(675, 375<<666^1, [14, 2])
(676, 525<<666^1, [22, 2])
(677, 747<<667^1, [10, 2])
(678, 393<<669^1, [10, 2])
(679, 1953<<668^1, [22, 2])
(680, 113<<673^1, [6, 2])
(681, 515<<671^1, [6, 2])
(682, 75<<675^1, [14, 2])
(683, 111<<676^1, [10, 2])
(684, 165<<676^1, [26, 2])
(685, 155<<677^1, [6, 2])
(686, 255<<678^1, [22, 2])
(687, 423<<678^1, [10, 2])
(688, 347<<679^1, [6, 2])
(689, 381<<680^1, [10, 2])
(690, 567<<680^1, [10, 2])
(691, 1171<<680^1, [6, 2])
(692, 1235<<681^1, [6, 2])
(693, 93<<686^1, [10, 2])
(694, 633<<684^1, [34, 2])
(695, 357<<686^1, [22, 2])
(696, 1311<<685^1, [10, 2])
(697, 617<<687^1, [6, 2])
(698, 159<<690^1, [10, 2])
(699, 63<<693^1, [10, 2])
(700, 595<<690^1, [6, 2])
(701, 51<<695^1, [26, 2])
(702, 1601<<691^1, [6, 2])
(703, 91<<696^1, [6, 2])
(704, 381<<695^1, [14, 2])
(705, 231<<697^1, [10, 2])
(706, 607<<696^1, [6, 2])
(707, 1555<<696^1, [6, 2])
(708, 223<<700^1, [6, 2])
(709, 447<<700^1, [10, 2])
(710, 531<<700^1, [10, 2])
(711, 357<<702^1, [22, 2])
(712, 71<<705^1, [6, 2])
(713, 837<<703^1, [10, 2])
(714, 455<<705^1, [6, 2])
(715, 185<<707^1, [6, 2])
(716, 193<<708^1, [6, 2])
(717, 647<<707^1, [6, 2])
(718, 37<<712^1, [6, 2])
===[output5filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_:end]
===
===[output5iter_odd_primes__one_prime_per_bit_length_:begin]
(2, 3)
(3, 5)
(4, 13)
(5, 17)
(6, 41)
(7, 97)
(8, 193)
(9, 257)
(10, 769)
(11, 1153)
(12, 3329)
(13, 7681)
(14, 12289)
(15, 18433)
(16, 40961)
(17, 65537)
(18, 163841)
(19, 270337)
(20, 786433)
(21, 1179649)
(22, 2752513)
(23, 7340033)
(24, 13631489)
(25, 23068673)
(26, 36175873)
(27, 104857601)
(28, 167772161)
(29, 469762049)
(30, 754974721)
(31, 2013265921)
(32, 3221225473)
(33, 7918845953)
(34, 12348030977)
(35, 24159191041)
(36, 52613349377)
(37, 77309411329)
(38, 206158430209)
(39, 313532612609)
(40, 850403524609)
(41, 2061584302081)
(42, 2748779069441)
(43, 6597069766657)
(44, 17317308137473)
(45, 29686813949953)
(46, 39582418599937)
(47, 79164837199873)
(48, 263882790666241)
(49, 474989023199233)
(50, 1108307720798209)
(51, 1337006139375617)
(52, 4222124650659841)
(53, 7881299347898369)
(54, 12947848928690177)
(55, 31525197391593473)
(56, 38280596832649217)
(57, 112589990684262401)
(58, 180143985094819841)
(59, 459367161991790593)
(60, 882705526964617217)
(61, 1945555039024054273)
(62, 4179340454199820289)
(63, 6269010681299730433)
(64, 15564440312192434177)
(65, 35740566642812256257)
(66, 51881467707308113921)
(67, 83010348331692982273)
(68, 221360928884514619393)
(69, 332041393326771929089)
(70, 691752902764108185601)
(71, 1328165573307087716353)
(72, 2434970217729660813313)
(73, 9149585060559937601537)
(74, 13576803638250229989377)
(75, 32613843522318487257089)
(76, 46043073207979040833537)
(77, 92086146415958081667073)
(78, 188894659314785808547841)
(79, 368344585663832326668289)
(80, 1095589024025757689577473)
(81, 1265594217409064917270529)
(82, 4533471823554859405148161)
(83, 7555786372591432341913601)
(84, 10955890240257576895774721)
(85, 21760664753063325144711169)
(86, 62864142619960717084721153)
(87, 150511264542021332250918913)
(88, 193428131138340667952988161)
(89, 493241734402768703280119809)
(90, 715684085211860471426056193)
(91, 2050338190066411080301674497)
(92, 2514565704798428683388846081)
(93, 6731298963614255244763987969)
(94, 18878585599102049192211644417)
(95, 34662321099990647697175478273)
(96, 70562582239266675669250080769)
(97, 133697524242821069689105416193)
(98, 287202089114208223776596819969)
(99, 326816170371340392573368795137)
(100, 851702747028341629130597466113)
(101, 1683598453428117173862808944641)
(102, 4516005263313067242832005169153)
(103, 9586607664225984848818817990657)
(104, 13627243952453466066089559457793)
(105, 20757778578737256449508514988033)
(106, 49913742383986532683932688711681)
(107, 138807740724991119463889000988673)
(108, 294094939252949221147235143647233)
(109, 339730360861165479601116459040769)
(110, 872143612957021828229731805298689)
(111, 2149935417987077064938408636317697)
(112, 3001796621340447222744193190330369)
(113, 9370473236887071735863630094139393)
(114, 17037224067067403156115691080253441)
(115, 30180225490233685590833509913591809)
(116, 77884452878022414427957444938301441)
(117, 94759417668260604220681558008266753)
(118, 246634100780404312355198575637954561)
(119, 334903147375496382040217013234696193)
(120, 794421419355828627165165938370674689)
(121, 2388456554926020709124028311441244161)
(122, 3385377551764707613801883606651502593)
(123, 9304595970494411110326649421962412033)
(124, 10966130965225555951456408247312842753)
(125, 33895313892515354759047080037148786689)
(126, 47187593850364513488085150639952232449)
(127, 117636677626965054751986924834810494977)
(128, 215334935317156371410416743765415821313)
(129, 467888254516290387262140085218681290753)
(130, 850705917302346158658436518579420528641)
(131, 1871553018065161549048560340874725163009)
(132, 3445358965074501942566667900246653140993)
(133, 7145929705339707732730866756067132440577)
(134, 14291859410679415465461733512134264881153)
(135, 37771342728224169444434581424926271471617)
(136, 44236707699722000250238698966129867489281)
(137, 100383298241676846721695509192371622379521)
(138, 196002643346460554954903773880698489798657)
(139, 577118894297911634033883334204278886629377)
(140, 1344795914071548807607256448570347971674113)
(141, 1459130789356984131330950316667422090723329)
(142, 3201376507992189064263428306718075333378049)
(143, 9800132167323027747745188694034924489932801)
(144, 19338927476850774755550505689562250993467393)
(145, 43207693822153082336725454153256200417837057)
(146, 76310362476221976062442535964218612028276737)
(147, 123699446023099550238205937293596380228485121)
(148, 323360805378694035552267914953401241836716033)
(149, 393050634124102232869567034555427371542904833)
(150, 958932043536816795086035885723879544757157889)
(151, 2776442777217062581121196924944721007494561793)
(152, 3032901347000164747248857685080177164813336577)
(153, 6244208655588574479630001116341541221674516481)
(154, 15610521638971436199075002790853853054186291201)
(155, 28901765777295687591430290881352276511750619137)
(156, 58160343477767865153125153255066926807596924929)
(157, 136302154653419168641066310082426785524552302593)
(158, 185542200051774784537577176028434367729757061121)
(159, 719332837123803780053376128602545548736904298497)
(160, 899166046404754725066720160753181935921130373121)
(161, 1495755581955845955349083695983070902929118461953)
(162, 4795552247492025200355840857350303658246028656641)
(163, 10687230722982227589364445339237819581234006720513)
(164, 15711142601307206370689611951700042461301274836993)
(165, 33431849953944404253909290548384974074629456920577)
(166, 52614058943912505055332653977786188707613571547137)
(167, 164418934199726578297914543680581839711292411084801)
(168, 206071730863657311466719561412995905771486488559617)
(169, 578754648383037555608659193755648075783749287018497)
(170, 876900982398541750922210899629769811793559525785601)
(171, 2174714436348383542287083031081829133248027623948289)
(172, 5612166287350667205902149757630526795478780965027841)
(173, 6126614863691145033109846818746658418397669220155393)
(174, 22822809568559379970668742347697475634947042591113217)
(175, 34047142143260714382473041862958529225904604521168897)
(176, 61733829160857339264923647333935794750266590615306241)
(177, 167616699782206593882944206094565066958299591488831489)
(178, 264894248762951492118581468560160864746598461549314049)
(179, 619583158123513659531597333242410158220857418539073537)
(180, 1293043112605593724239855304158073373678311134342414337)
(181, 2442414768255010368008615574520805261392365475980115969)
(182, 4549596136945607548251342736852480388868131768982568961)
(183, 10727468786061222008508429190052164285331173855285215233)
(184, 16617998521264482307823325575661165209865702356178436097)
(185, 31895063444271311864583097502565809884065007980446220289)
(186, 57277020839862596081143220139742805737750374691612131329)
(187, 194626933689967885011510072448089266319579868517317476353)
(188, 254394259783737550487485606506951324480710694282477961217)
(189, 612998216346355543343338810860123673447495648873440870401)
(190, 1422155861923544860556546041195486922398189905386382819329)
(191, 2353913150770005286438421033702874906038383291674012942337)
(192, 5100145160001678120616578906356228963083163798627028041729)
(193, 10984928036926691336712631490613416228179122027812060397569)
(194, 18340906633082957856832697220934900309549069814293350842369)
(195, 35308697261550079296576315505543123590575749375110194135041)
(196, 89448699729260200884659999280709246429458565083612491808769)
(197, 121030367835424438477708814816222818085473540913572165451777)
(198, 249514793981620560362472629572504740040068628917445371887617)
(199, 467644079286307716905766312028971147999625480612570571210753)
(200, 1393516585255843129571545251952101944374722908671015661862913)
(201, 2297419235151525159563898928894005908293462092673836631719937)
(202, 4092670331472115858020934703931398503298735749790550502408193)
(203, 9641628265553941653251772554046975615133217962696757011808257)
(204, 13106588423487389434889128315657607476821718168040904062926849)
(205, 40776052873071878241877288093157001039000900967238368195772417)
(206, 72312211991654562399388294155352317113499134720225677588561921)
(207, 136589733762014173421066777848998821214387254471537391000616961)
(208, 290855786010877239873095138713750431056518741874685503189549057)
(209, 613850332906934285257029519274324114163481543625026863085125633)
(210, 925596313493178398712170165188509659052788924418888673133592577)
(211, 2468256835981809063232453773836025757474103798450369795022913537)
(212, 3342431132058699773127281152069618213246182227068209097426862081)
(213, 9050275065266633231852330504065427777405047260984689248417349633)
(214, 17277797851872663442627176416852180302318726589152588565160394753)
(215, 29619082031781708758789445286032309089689245581404437540274962433)
(216, 56564219157916457699077065650408923608781545381154307802608435201)
(217, 107369172365208694250611739161867120450123515232591086083496738817)
(218, 325809902349598796346683898146355399986581701395448812943024586753)
(219, 480487330737792164309251001306746347454958872765005320097793835009)
(220, 1421715937525522020421893373729550836305083787907413001933198196737)
(221, 3264681041725272787635458858193783401885747957417022448883640303617)
(222, 5528895312599252301640696453392697696741992508528828340851326320641)
(223, 13295676823155344820612150995063392080260505794319325295856760913921)
(224, 19272149375345965165718999066111689114357802458300487359538908889089)
(225, 32383529688081334909609793512728657938060241835668851710700625592321)
(226, 92674816668330324294167864361629980440627683952483217903793660231681)
(227, 117528517502109820354876518894976202467886926467012808159811050930177)
(228, 320991865005762305055254148379827477707992250780873691103139859529729)
(229, 505499000009074496150006532881618075130696457922635734020692692172801)
(230, 1331147366690562839861683869921594264510834005862940766254490756055041)
(231, 3302593466725953374846709348159904757520550191761220128935192255528961)
(232, 4731470640084937283964061147771945183223318846155870470433683598737409)
(233, 12940774400232307101440167241769422723345829322819474790929732919623681)
(234, 27175626240487844913024351207715787719026241577920897060952439131209729)
(235, 49606301867557177222187307760116120439492345737474653365230642858557441)
(236, 100075322028463174917803960003016869060541080096470605049856601245089793)
(237, 172543658669764094685868896556925636311277724304259663879063105594982401)
(238, 336460134406039984637444348286004990806991562393306344564173055910215681)
(239, 714330746892823351999497231745672134328689778619635008459321257163227137)
(240, 1145689893567233588714169473137986225106884089380284168156979021150683137)
(241, 1966997708835310679418905420748952253948566057068560168221319403782799361)
(242, 4085833837300013762161375470467999067851056511524868840656214340489183233)
(243, 7398672083759484380130058284360971285027588818166654387134225967912845313)
(244, 20981308894243313913801657821322157375451371275397975127694073640349859841)
(245, 29594688335037937520520233137443885140110355272666617548536903871651381249)
(246, 57422529605297490711457168774144851764393226648457616138952201542010142721)
(247, 117716185690859855958487195986996946117006114629338113084852013161120792577)
(248, 240291200809860268823328460101036918152537809975084178304538443375796289537)
(249, 514152495850509839908739572716189288105797813990805116813387404576152354817)
(250, 1639634076114340657853300080689428382687905056300574393136850554799551152129)
(251, 1978868712551790449133293200832068737726781964500693233096198945447734149121)
(252, 5003710887452384421379898522103945236823434395951752889400388762060699205633)
(253, 11477438532800384604973100564825998678815335394104020751957953883596858064897)
(254, 16961731821872489563999656007132017751943845410005941997967419532409149849601)
(255, 37768122856702743429172567375880626194328295779613230848807454158831040331777)
(256, 93628759656736142393278101159368737990730026663232799828780155818898507169793)
(257, 141121608757979113172477137979338387696172793811249437423088930509644126748673)
(258, 311191239825287275200847022210848752355663083788909015856042257021266535907329)
(259, 566295686426249518243401848558114299344898518755398383505472246788700149645313)
(260, 1071076825445174807668031611330363147642747358157175217364982652073196449169409)
(261, 1953991505879710797772760372021608445023930991232684518165846730133534062673921)
(262, 4581024530451321981445027094406215354444993768334404814811040667313063191379969)
(263, 11810793102206251933204240470886166601033538435895337532024673568807139223273473)
(264, 15052971600851105405064228051129428020925098006533273325129485921028706853191681)
(265, 55348618655437141412466930834152819953863052670176189610860725155782475967889409)
(266, 68085748471541922909059739185108489817722750983396651655201059396652920228282369)
(267, 168593281929532380536719354172649593834361097673172661241450242315521516755746817)
(268, 407588154115353007890969867230581435643510346023054785418890695707854216332574721)
(269, 755890758541200123725071390136714662466146459897301602049579108403656910289502209)
(270, 1178300300078929604630258343448408150314875363957558379665520374864524007215988737)
(271, 3586775756215106469440534831629116633662891045002882111686238122229117103726657537)
(272, 4031417378886400659867047414062478199819447786118941877597755244819503521544011777)
(273, 11857109937901178411373668864889641764174846429761593757640456602410304475129446401)
(274, 19208518099399909026425343561121219657963251216213781887377539695904693249709703169)
(275, 58336980894473797783958450815257037479740244434427041287591046483858698017636876289)
(276, 82999769565308248879615682054227492349223925008331156303483196216872131325906124801)
(277, 187816621416354666036158914819851925544529567447423645121024832582179222886050430977)
(278, 364250417292324200797399107529409794995451282322276160234714826826044553475976593409)
(279, 671586706882722745220204604507349309522863301781696670432755461960519645471331844097)
(280, 1639126877815458903588295983882344077479530770450242721056216720717200490641894670337)
(281, 2549752921046269405581793752705868564968158976255933121643003787782311874331836153857)
(282, 3961223288054025683671715294382331520575532695254753242552523741733234519051245453313)
(283, 8924135223661942919536278134470539977388556416895765925750513257238091560161426538497)
(284, 19669522533785506843059551806588128929754369245402912652674600648606405887702736044033)
(285, 36060791311940095878942511645411569704549676949905339863236767855778410794121682747393)
(286, 122388140210220931467926100129881691118471630860284789838864181813550969967928135385089)
(287, 224378257052071707691197850238116433717197989910522114704584333324843444941201581539329)
(288, 485667223056432267729865476705879726660601709763034880312953102434726071301302124544001)
(289, 693532794524585278318247900735996249671339241541613809086897030276788829818259433848833)
(290, 1049041201801893698296509429684700209586899693088155341475978701259008314010812589015041)
(291, 2525469559893447792195300478870574578635128890767781377627356132660575570766771047628801)
(292, 4600239936790526439937285795358092770929219394875466386324291786261725347365933723680769)
(293, 13925050619474025980350702948110983522812772222325736088332991353008465916350934514925569)
(294, 19146944601776785722982216553652602343867561805697887121457863110386640634982534958022657)
(295, 32823333603045918382255228377690175446630105952624949351070622474948526802827202785181697)
(296, 73603838988648423038996572725729484334867510318007462181188668580187605557854939578892289)
(297, 234736567585419295097340421125299436527415303176348122631898997093571282589915753251602433)
(298, 425708690366777365685007204413678639125990465082529646129037164220544529442728569456295937)
(299, 560980610670239332351271175909613907633314538099408225272843365935483912630137647601287169)
(300, 1141854150796870130388757641745100648870647322230710359243305290946694205140776630223896577)
(301, 3819442455627161411753335665767584051971503238123630469942763342539464937056256324093870081)
(302, 5633677622050063082336170107007186476657967276232354943165575930245710782157978078038458369)
(303, 10312494630193335811734006297572476940323058742933802268845461024856555330051892075053449217)
(304, 26354152943827413741098016093796329958603372343053050242605067063522308065688168636247703553)
(305, 47361086449776801505741362255518042244446640152733017827290265447489365219497578418763988993)
(306, 72314777159874256062529821938532924717327127975140736897582985952080536141598453069510606849)
(307, 180277683905602018634757443424229967253054952839435358181298429767862745029055298497230667777)
(308, 396203497397057543779212686395624052324510602568024600748729317399427162803968989352670789633)
(309, 543888605681307785033674998805303969000742061108804978919849499977619807036810900550967099393)
(310, 1743702795742320089845789509278427705860056944978041430544536224647350392597416220492988153857)
(311, 2297776581305300305310806736525778565666056348055176090717566426871742106133043804574872240129)
(312, 6779255729241169695101387251026410519979286814120235842117075415451380965612384558178346467329)
(313, 15579251147006149587781072624954924175721630274757080444865202156662308180589999128890623131649)
(314, 16948139323102924237753468127566026299948217035300589605292688538628452414030961395445866168321)
(315, 60231079748258084598785402114888493465969817463914403058809400806510346271402339728430693613569)
(316, 74311072416682052427072898713174115315157567000933354423206403592447829815366523041570336276481)
(317, 249528758957069207623539523047395187216160672350502526957924660484114291695809693160641444970497)
(318, 350435373080774310392933248668442143802006210699138345069436513783332923760886340238142217388033)
(319, 625777451929954125701666515479360971075011090534175616195422346041665935287297036139539673907201)
(320, 1735489466685739441945955136262761093114697424414780375581971306355553527196770446893656695635969)
(321, 2553172003874212832862799383155792761986045249379436514077323171849997015972171907449321869541377)
(322, 6908583069306693547746398330892145120668122439497298802797462700299991925571759278980517999935489)
(323, 14951909251446370576765151943186864802218931656496569389629291254755538080464483850160734608556033)
(324, 18656511766871699000919017714824681750982997312458889037506191543322200417365282304106809478086657)
(325, 58205646728844799745264341493120295122923698234218787981056883813155487527522454988125716869021697)
(326, 105731358278085049078553574455392829672833873856654312112378559587199876426141707226136623303360513)
(327, 217870677663932828404292214029294315689475861280378582534598243997866412029625336102342132867530753)
(328, 378069705358001084583918841992010724284678700457127540280626364584532891463173377354064289387773953)
(329, 976146075415855907654524919719485316373435966716990315865798014774754414681752731360493673730015233)
(330, 1334991897450568801496888566355970071626690326472907981216901004888887328612900343764351304335360001)
(331, 2768239198553499466783948131195739540525105060974221989851365923737596764611710152829758864669802497)
(332, 8612299728833109452216727519275634126078104634142023968426471762739189934347542697692583134528274433)
(333, 9569221920925677169129697243639593473420116260157804409362746403043544371497269664102870149475860481)
(334, 19172619634426088899577714834577899780673875792673315263044645471812244258607029577006107692342706177)
(335, 64113786870202037033168971532385276271914778943057289542730400900391747289031706749489230001488265217)
(336, 81201683157569317692329145181741693188736415121910511702306733762969505095276831149672926696980873217)
(337, 142718109792091528065305770319424794089294305365782111476781532068249433197759278990334234800754262017)
(338, 546812681195752981093125556779405341338292357723303109106442651602488249799843980805878294255763456001)
(339, 787410260921884292774100801762343691527140995121556477113277418307583079711775332360464743728299376641)
(340, 2204748730581276019767482244934562336275994786340358135917176771261232623192970930609301282439238254593)
(341, 2502214829151765641482142547822558841964025828941835027271081573732986231084086056167699074514373574657)
(342, 6194294052585489769822926307197103706680175828289577619957782357352986893732632614568989317329288429569)
(343, 16798085566333531579180817104263332085912341229259871511749918257228439033851207090356581199537053368321)
(344, 18617878169352997500258738957225193061886178195763024258856159401761519929185087858478544162820234149889)
(345, 55993618554445105263936057014211106953041137430866238372499727524094796779504023634521937331790177894401)
(346, 103028258140178993685642344906148436793595692872793878605399498644334426074287403487520364690493927325697)
(347, 178059707003135434739316661305191320110670817030154638024549133526621453758822795157779760715092765704193)
(348, 313004327719348138425402558709440087867499958238542272502273476859689913997427492116977629684707094429697)
(349, 600251590903651528429394531192343066536600993258886075353197079058296221476283133362075168196790707027969)
(350, 1970975373116467705290549206900230964747048037566491590711990408848136846638541631935172194079014261882881)
(351, 2902709185862434256882445195616703784445652564416105797230385874849074265049488585213617231280002822045697)
(352, 4873684558978901962172994402516934749192700601982597387942376283697211111688030217148789425359017083928577)
(353, 10786610678328305078044642023217627643433844714682072160078347510241621651603655112954306007596059869577217)
(354, 30317184830118757794105538709774461748654593450568216104406252470645886768294658556675557748924473919143937)
(355, 55043966783761716278659701487250086579117559740038746969702132145286149026123635393680445274643016477310977)
(356, 115248305453501093458443749988929868775027390705706126467813839179192874523446361605518432293783815749369857)
(357, 269772774705832161553222807809907976411195956850919067179633887232886803299908025549235932309578533880987649)
(358, 298154820078709296509406716389271302303553448591876546085886549120299973891503025049102411904316339252101121)
(359, 738506554348803026738684328287271994936493926512186521843503606282589166100492108198545974101460471070588929)
(360, 1513709086553447197663141790899377380925732892851065541666808633995369098218399973326212245052682953126051841)
(361, 2568718449908880093004119402738337373692152787868474858586099500113353621219102985038420779483340768941178881)
(362, 8073115128285051720870089551463346031603908761872349555556312714641968523831466524406465306947642416672276481)
(363, 16953541769398608613827188058073026666368208399931934066668256700748133900046079701253577144590049075011780609)
(364, 37136329590111237916002411936731391745377980304612807955559038487353055209624746012269740411959155116692471809)
(365, 38897736527191612836919522384323394515909742216294047858589506716002211978460702344867514660747731643966423041)
(366, 76621201762996309059894304470252120518131643158133935781825367946238319444364100468003179822303078936416878593)
(367, 221937274072127240035555916396592349087002000871836227781838996809793752873330497907319555347360642436517855233)
(368, 329970232879723568518472023848901852346283398121618941834374381500275368028602486306649709273060002775986864129)
(369, 615318156686744305707043916358806301172428827813979806125310234541438764580027412187489137576809400194366963713)
(370, 1352760527677727939264340823750658127768393148171192245527399599602552398466014463435090623069626772946394546177)
(371, 2855827780652981205113608405695833825288829979472516962780065821383166174539363867251857982035878742886832930817)
(372, 8492329979310180952048361837990242690990468096852484652477564153060467834814424131564735578159323630163476873217)
(373, 14654905716508719342030358923965463050824259105187915993213495662360984316715156687213481749920956706919274250241)
(374, 37313644555110662324708067721788986690944844337055386105797438955703736991020898949751249686337205153771382898689)
(375, 41710116270063278127317175398978625606192122068611760903761487654412032286035445955915294211313492165847165173761)
(376, 93791396585655803788994297113378963525275258273202662356566372239110299626977002798166283199494122924283355201537)
(377, 205619600207014646768179805210100035420795758522021221320164739139587964566834198442133774706583269487851971018753)
(378, 432883368856872940564589063600210600885885807414781518568767871872816767509124628299228999382280567342846254776321)
(379, 947533596275599658791378283658238759716883378452355101756080786210498924436639464166090143092325241850452357677057)
(380, 1596858649560909069638261879058554661045712089574527379609232594019724075700326406614933642165746092864721739841537)
(381, 3001324690740985721247817507628126832808808264742485195410123911651529588063264089541321062383811933577067366449153)
(382, 7503311726852464303119543769070317082022020661856212988525309779128823970158160223853302655959529833942668416122881)
(383, 13948464107610350307081203160451230472989653794476293376104742538124095841960682467419601091206818281047268209459201)
(384, 21932757355414895655272512555744003778218214242348930274150905508222716220462314500494269302035548745370876908666881)
(385, 50483820439130426490732520128309005187758415940283853543308750924189831019730801095874528639071298164783492112580609)
(386, 113280767814634127735302240287912889689604250402588159170351343537206450093054480507816015482794132467319055472132097)
(387, 195778718288335068586011480497588581093989954500125188131368082852345930052126765225464635453959424590257932826836993)
(388, 519613956714952194611929841320643907054489061629263077933568119268490455861619464938025636236294825013137406622171137)
(389, 659983603789607526805673921677405531235085632780296231688133914521115839672578277741188959769322336983511018837639169)
(390, 2314867864038175653721393605883437311048434682139844991741962237499436154075461123420588142474488793897389394430525441)
(391, 3620059319293742777628136809200694518341701045474012912617749456515075687756306224923685712167551624499108946609438721)
(392, 9554986502625661208977667224284826347731836773087870816977461150529587529588073573267959566809592042895607287649402881)
(393, 17652098775984726687101009964864338984675723193168520107240835445102083353630750353913591282188442207081369339657453569)
(394, 28999876560546336700237373513705699760538688103062568747609943945524851223821947010000899963595297911633678200865816577)
(395, 49173703733100310056924242044979230028739514609540877441599470168498660770828518843045004286096374719726671731902906369)
(396, 146260247001016306835979796851733094444455992171967738031424065116560119215797645789569756338132806858674203100018900993)
(397, 230738148286086070267106058826441002442546953167845655687505206175262946693887665340441943188606065992563613511236714497)
(398, 554780247245234267308888884610022082375522728928153489084711971131779762542680725408712868868779612222557322103519969281)
(399, 1059125926559083601226060597891860339080543391590111206434450126706125001217845021234815476931306532424882160379447214081)
(400, 1750079507219057188692585845087978750766421699436993279203591399842977978202820106516576049976968413102067188817467539457)
(401, 2884857285675218190006222199972114828352718190426398143240502249885254765221939772125306918117653983557298074938303840257)
(402, 6778405929978135047846787826507906170115477706176711721180480810919200007794208135902819052360361807519245826428462170113)
(403, 13072640007814974735133090808265247613794135576197944033705212992487028586460258547812579600980697771644259808112034185217)
(404, 36797060762738447402596848201042919209198307547816435057836895830704228613739987023472446284241964097961620200611651780609)
(405, 60037309665520624709500120749070026078165659683279446673312830039570057211891557775139254463763204580884748748366379220993)
(406, 88361363015786403302288484166978062574719620098374992079674124856625285815888784628733176932554716419447311665942453288961)
(407, 250478238174430133196624159684292151809981461904434680744573957584442819335633595879075599268173369649282607681356506857473)
(408, 395729793816818741364769613109461569741027412751078503341298546389854248074080913076993150390181122667552161104823553359873)
(409, 755308089340420762474356357810880973241438944402547877502967861788139429439926049429171265834440315695001677802028641812481)
(410, 1983167906370745796855745924098313119485214048892843657853946385823217373708934037475567631319145854542773636075070074912769)
(411, 4802984773241649976760009659925602086253252774662355733865026403165604576951324622011140357101056366470779899869310337679361)
(412, 8924255578668356085850856658442409037683463220017796460342758736204478181690203168640054340936156345442481362337815337107457)
(413, 12890591391409847679562348506639035276653891317803483776050651507850912929108071243591189603574448054528028634487955486932993)
(414, 27929614681388003305718421764384576432750097855240881514776411600343644679734154361114244141077970784810728708057236888354817)
(415, 71146148641050505462199885027026983161532054004030766225510326591407923281808008594435988773574357531722004194193138937495553)
(416, 166586104135142646935882657624258302036757980106998867259731496409150259391550459147947681030808251781592985430305886292672513)
(417, 261778163640938445184958461980977331772048254453855362836720922928664693329579292946774927334127252799646119961909249888485377)
(418, 349037551521251260246611282641303109029397672605140483782294563904886257772772390595699903112169670399528159949212333184647169)
(419, 1065622221689880741510487476548826916203388348938421325486853857982342135472933889470205007228821039174317033784337653586460673)
(420, 2221148055135235292478435434990110693823439734759984896796419952122003458554006121972635747077443357087906472404078483902300161)
(421, 5246140168319412881282399884548070972078219564004535756242972839297684359251366840468701574049580500550483858630585371502575617)
(422, 5457678078332292432947012783118557704823309062553105746414060453785494212446986471132762121390289391701713046478592846159937537)
(423, 13834579314842322678865683566509832321528853205076477357189129987502764398993523845429559796082361481290388885259688842591469569)
(424, 24030706577463117069100025277607292839842167035117550883435553005815199323022390043437278177904530034779635739533649121076314113)
(425, 49246025450998359627521882787209311383056835262107093711829196652762133823940250018593295420917029860006154931016140100233854977)
(426, 148414997665036293447892409637053491693954792181676705104035070324647393002046732873904880014241358031702398194162044219605123073)
(427, 242337829710754814386980536602349601032774529537241780739997971157234967820901848888747763033516105702848157598677362967473815553)
(428, 438645010202707038331741306475761289020217584190314731618767277401922511586436866144995950965693956691188843921628299449505677313)
(429, 716859669451646224681040190675665439926559292681393982691781707976290030509315804394368382828194290333285471779327730118868074497)
(430, 2128240605057578593387337449937952920801796426997452957113278271838957371030489980184980354685404012094286613101233601032786804737)
(431, 5052540673075625515598946159776361514269913654932884501238393454518440781606735754484953361123363723368878905912088930696157986817)
(432, 9130314656811902057127356082939920164050454900553958487768415181477053759688056250869915720100740876312893714220559418171192246273)
(433, 16571033718768932559199116022417648696319330958300778750042319368517072659932059387699847036481771697222689659261513534759103365121)
(434, 24477474643410318682215687719388160819399796056052130702676890047613453732971538703399774053888107212891031784268640907552662487041)
(435, 77634751435382816068195597156006343696220238110522864104773428257209396618557517445119283370915908186726953906919300011211276419073)
(436, 130402121551619573864547292097979405427244931201268873300986617775781408382733330083598796287085314532392930390528511737581440860161)
(437, 207950227059061114468381063810731277757732780653186243137785968546096598085421921727998080457810468357304340822105267887173061836801)
(438, 623850681177183343405143191432193833273198341959558729413357905638289794256265765183994241373431405071913022466315803661519185510401)
(439, 1321177109248568280589114358744179384687462266416576598068733520162867053169380609378547804508622508963406912023108801976506186203137)
(440, 2129410325084785812156222093421888284239183673888627129730928317912029164394720478494700343887979195978796450018357943164652153208833)
(441, 4658085086122968964091735829360380621773214286631371846286405695432563797113451046707157002254954491203617234415158000672676585144321)
(442, 8562004015445076286378143000633842476211717688760521584126440944937950598503771923947440966049583017164744059448814229807872199360513)
(443, 14373519694322304232054499130597745918614489798748233125683766145906196859664363229839227321243859572856876037623916116361402034159617)
(444, 33050222753920113126174697074985557744962329938479733576032116600926285989043057426636494920761343770920903234659930576201371961262081)
(445, 55009766731356966814035737413398780676178911575456200851382314879394086746863612361113092217106129229452241625474246865086847291228161)
(446, 148703821035087542548909509523961865182702993226555794559543160867523369980231313414879907348177213852519285426281996364331542032416769)
(447, 251270418360004725834434207023782817540223673518858001308249541513619441398577016462374640578781545125497981102166237293428954078642177)
(448, 633144669991876314814450035777441449847117279036218466573329353192510004880030222272424235582692480937695477805458428434289906887426049)
(449, 1022116956040697189834986604842506376434808163466541022270845592597773998909465829677456165066230014069822296008811812719033033540239361)
(450, 2010163346880037806675473656190262540321789388150864010465996332108955531188616131698997124630252361003983848817329898347431632629137409)
(451, 3878366005421089892540532506152399195027633198042486212283264109690442451417584231498347559667972775609381267633435933817219788377686017)
(452, 5928278345036043701042922308086536983321887348105937929170904437067089193674901812129245757384134081604969316851108513770391594533388289)
(453, 18170968107390172263733095197200113358841034017182951507037254979515982202834948083154776267844089139019063040156654448338365040715366401)
(454, 29436968333972079067247614219464183641322475107836381441400353066815891168592615894710737553907424405210882125053780206308151365958893569)
(455, 56330001132909534017572595111320351412407205453267149671815490436499544828788339057779806430316676330959095424485628789848931626217635841)
(456, 173532745425576145118651059133261082576931874864097186892205785054377630037073754194128113357911051277632052033496049981631386138831749121)
(457, 242037295190437094552924828026705509939762573108876914073736236327152882941761508467621619887683267331733919694886637251867022342328680449)
(458, 429198266696555868869375708557866677535825223485861314596219962616167499630961473724115815446477385463630269008500178069752182261696954369)
(459, 767541692856160876420085941129732788277445276885807871657253650334755088247748207032457749553734325232165222816217083897812539319817076737)
(460, 2511954631165617413738463080060943670726184542535371216332830128368289379719903223015316271266766882577995274671255910938295583228492251137)
(461, 3116684449779562346675500488223763443308414154627219842487029974086581267430250295222707225460618169124549692647669370978996371783499644929)
(462, 10606030664921495746895733004701762165288334735149345135627504986443888492150702497175779812015237948662646715278636068406136906964745060353)
(463, 21398132043262666857772092904222853491371201658634643694687071463878020642058434862723064533013199370108848636088476278363258671946415472641)
(464, 41772875162717119213650737886939396598372476281421543560497804727309701166453205449402852066621419639908143641755329778196100624799741509633)
(465, 56844602949710823696081516367305058622729583536633770858494785497519437444772624787494749694222020935376115289782865243825874124170695016449)
(466, 108851367350510087928666733469307559064801330176532752707755972229292539787862472997330371754893231578379795235754422807326141939901330882561)
(467, 200956370493249393099077046404875493658094763402829697306626410269463150377592257841225301701341350606239621973700472875063646658279380090881)
(468, 497925229111051274012157570536524834286168135987011361104196549889892028157811927762147136437768013168793730001502282790435480053292241780737)
(469, 931842132805734222814979489255200437259017199186454744547763946879140238047205580804496584185479151700044469300270340887332168948762162495489)
(470, 2143534618594660193056821828318671932353010809630183437937348376207606937360984083639736551480974406466555967719471710667345564354980054302721)
(471, 3209347665062560677937852681843789365384091184418524647356196596599722608993251169671716670134014458570760185002209033471386831075928470192129)
(472, 8717040782284951451764408768495932524902243959162745980945216729910934878601335273468261976022629252963994268725851623380538628376918887497729)
(473, 12480134890484466012908607089322045472810862936069068016435228323697622613079507331413577255289228766538614745388924182107656396911217205051393)
(474, 30771630302492232993660153357641379295556555178246633353500601134002535145226571511805995827926877035053225669928416113135671879407047001767937)
(475, 52206976488438834924228371640828098619086663274548467732874084896078604518836412348203361342736621099718785347123133219809127522956847544795137)
(476, 103651807334710679557592095520476224995558922705672870243370445925061171015500030355557038578280006854916128572390454275825421067476368848060417)
(477, 204255032100753397951725599996232561020660230037649479597229996381738189942308883347715340727787072331746488657357659896479506221203432730001409)
(478, 446617346309856310446683588051463734172040652246502220313346186118278280993257483737914886815235911889565083407505927982600711364273177536495617)
(479, 839884497668023300532841832820329411361073035453319875060251701539833900434419363616351886126945349662629218285105004499703044237933518165901313)
(480, 1813906628357436892257861671608333937422281147349275229258982803688570492771250531222248175119900119961032250016832949826944868680836454841057281)
(481, 5426476972228970870956292059601402367414555365179344383329393933723790717870295706849750843215835652992667907613382606204977926473762839692574721)
(482, 12145552953573157275219026722164037658303139648805903383811407546042461921345650615780565932231398450293701653894222642202602280377230985019785217)
(483, 23998441980554190278746028704034965975442348221736965722229769127120045242176948204674853167300594528291169532995813413508756313034528693292105729)
(484, 44777580768595013568879785264845729198081454608850679945136032639626425878696013113600640665816962961323767543272676247156581901149791342362099713)
(485, 87213850124453032964223372607346583666851460610702631527127697559533822953277202012111051754336306944277664888204297527141577820540116470744481793)
(486, 101456827885269747519901909968277904936829439636611562402922601187824581511642382653909948349563489062694375261445715244102059209576869272454430721)
(487, 319589007838599704687691016400075400551012734855326421569206193741647431761673505359816337301124990547487282073554003018921486510167138208231456769)
(488, 407388185816236986195298438488008202900192057617778735187119983231111011915979413425699946449785702236357414511343564287855960826147121232470867969)
(489, 1436004333145356426435534725704856500644355145625886729395212201427670999857092185255340807409206306733520388315847046531906068812472611240893480961)
(490, 1922997106994651214531063893552590444341136455881622228929240687129228991112975621994108559487111054234453389570786479703595953018441583748674748417)
(491, 5294485541335922824423188901729210054549622449959791071857130203524630469038322491724039150795682383087066475181905632430679766752072931879468138497)
(492, 9040583801715113502081105577481009621447940221157756452888118555075076555622041235868406474471872748478858792527593579905217337567218874247016349697)
(493, 16707598241291190422354308373853026068366497259542925599398208047914989546163385598883878263595809029647393735361768245736437565835550902959265021953)
(494, 50547352526716546210530822344810948822681301126031212874711469490254019194969644920987996420804061997019917668717816037923093622199035915679450529793)
(495, 56541109743323251294783489026013828129718609559947957484361050852734732933503594911618984138685966581646785376470916753882353735503269423467527667713)
(496, 112682635672206055583950133606614130972301398557634798661412129614637418284438259823862569096179806190985112905758293460034090130119589946415850192897)
(497, 335650404129975484718149334147361241194089272299337698140376556298919969357901199475335312201386656739104591634173640093718566345037076436132319723521)
(498, 799167628880894011233688890827050574271641124522232614619944181664095165137859998750798362384253944616915694367080095461234681773897801038410285056001)
(499, 1395346680026040943614020803384030302678285403415818145126422541185510158330703557818893940722907387301134802364921846675315754377225560613064357707777)
(500, 1759767118795728612736582937601165364546153756197956217393117088024337553633567717249257993970127186046448358996310370205638769266122957886579447693313)
(501, 6112034025681077397915252637045282792029511320346035036613333101366999822974353270446105875514774168430171230519428570087522846206770382341761860108289)
(502, 7646435873132393899483935307433219894631062279428721656683625930162062540039044468047638731292541742094649363704222353373093435212654160335509607415809)
(503, 22146533331547334839307986542599225514215718842760110216347893162275405216300376285382124218392445313223967722300523605421735501318255862376425819471873)
(504, 37106951344197670729602642578881612264580840693816304762033248243027266707681115461997069562225679156452629520852262992456048744125622697815466355720193)
(505, 75697157807598280744055011739138230395009847314745873256801112887223094041858099081675620885036533634114254570449826642088149057623599714358222200504321)
(506, 127866820620943041797390222532328091883462579923557218339191069066255226422057599800127737981480631138706511098732815273797549083823648166145645608960001)
(507, 241412557332340462913472740141035437475977350895676028224392738397089867484844748422641169309035431589877892954407555236929772670259047737682978909716481)
(508, 746333058600320346363007250876692606705394386497818772002190431925918505580265798513385581050306147830402163981083696190101534492461869616158904290377729)
(509, 1029481346183336618119148159652279933372133923480543876292495135266234078969270147510788444036496857423953862158117642332398827183680956115271821926858753)
(510, 2327380722214156869579377874444422997226032494736619065322620162716351129243723608522005035643717855734280432414695210487553469404124514460916583116046337)
(511, 6651529715244960279866801463953681477304216637559507652230048059971343874294298695522804827606237247330601742147202064290729465301239118684363568061612033)
(512, 7859410849558636629901668462083065564472157552549398559549382574798817245167623606274731491674495881319278928590271730493130632966670828721041794742091777)
(513, 13591117803984781044294763621228191680003497775170805005934625760335147522672208751875337423337154060490481512497629414830270049178516151957420046551089153)
(514, 39018816046122011090557221186184981894422373188833332290640833107705914853143720694208579500524777553238569274800516046429869698026953885195676048865361921)
(515, 79085117086770787579518663075354795517554071832400445313916319453202592521136937245979805430593844436765422288521851315582688918148591096168417226559324161)
(516, 189385287010439184031483103099657576550646042215867556460345305392569916924788851047326474461607510916121699996884115468309273594718745300493375292210937857)
(517, 223742794830917089099141542157560057252311917131135564490761931592106937251852315175381277350660200949577406633486985973622017919424358385981111517789028353)
(518, 834636043638926669448483056138313921435590522331876487763291699871679810872078299305916675060889738373704483172108756665646179205043673979165494650628734977)
(519, 1312289201143131691120807696699397189727042929690480501844693576304267654443448410354483446933085672985161868120002322227311161280219270533507193396470480897)
(520, 2708377201848404614113953049637580917750831895759663462300159411631796334074856489313978608229714492393386435353670182272458284328013207129179597099228987393)
(521, 6435747806372446607795531999138806141190095593884348821307309492986446734435302548864899663120113645291215291929513304409801863749734353574288151522920366081)
(522, 7401109977328313598964861799009627062368609932967001144503405916934413744600597931194634612588130692084897585718940300071272143312194506610431374251358420993)
(523, 24697182206954263857415354046695168566816991841531188601766800179335489343395473531269052457223436113805038682779507305672614652139605581841330781469206904833)
(524, 33465888593136722360536766395521791934188497088198613870798009363529523019063573254097478248224590955514319518033469182930969691498618638586298387919185903617)
(525, 74654674553920380650428171190010151237805108889058446327164790118642782119449509566832836092193318285378097386382354331153701619496918501461742557665876246529)
(526, 205943929803918291449457023972441796518083059004299162281833903775566295501929681563676789219843636649318889341744425741113659639991499314377220848733451714561)
(527, 357827578034308031393431579152117621450169315019969794464686407810046438434602821716888421269478318678191570231280939725184983624485230058730421224674372354049)
(528, 636709982977114051064571299114799220901740124088291576721336485839459130260132598834367406671349909974144232881559849582943064386973718713616241124000921550849)
(529, 1599497854810432063590782886185964619623778424933390160388909985990231561731653860144556396274118911309710040554215039922649423203933978008329748591829808316417)
(530, 2320301609124146083663882470089510907437069131448437228375328649204713595988407745617425158543571639582326153250320530016547231943904225608650021562396889317377)
(531, 3624613164548961929510443621914975618718261838475665256160276706449966800833962395520711490269248005028012452414701893043600409663850387933039086937708750176257)
(532, 11299456948574983590860208715287973235625490504035880703863286853819404079872541861793733168528754197492629728550377492329102792247533595715496850567175384072193)
(533, 20155045930143470123186860746102970485903062041220744681982144716168754786455518169031835104982030573413341970245387799196990156767168066233717347062713807798273)
(534, 41518296248469927556210536032844266178045544695266711116017715001154165173189023803237240706720477148502688091295676229408513783422286261778447723104663865655297)
(535, 95887493716704356498867190361568900458819472272401689958421865597903667185698459736047913060759197223922874877516204625062519928380042080774034027170295118299137)
(536, 168709267295369864355395194038224319707613641936321873741278333972943909275180795136964025728895907143122034148757033567120309977081036238337819319282443644567553)
(537, 230217854330140127401633025197993602934347782225605890209452726567246376198423793363982160109222539955718609098824702055132922989558497366898482612770834556649473)
(538, 714378303703831769379876524755606103761926515074112934123225445416684365837093679408082046445793606809157363348643064010775062559202512821711703680086597307465729)
(539, 973593063350363592217593098928919511646020392007524146381960385635530476442189171936229898477170130805100072066785381210256788826071813292074498988359101865525249)
(540, 2671230065510022852293757238938551728703882663991763000903573621238278563523695923001930407374185196432765540688653031479404907970449740440348805888638691038986241)
(541, 6741341139010820829867666295110713441650061775705528204911913428335550374787432605681187528083798956260584614527416466286182386167529739690248696966327643964178433)
(542, 9503955390972502358687262597486636676862235162412798887425346147142506889168518126048973449394469435729207923713312890947777462042231708093030488319577658643972097)
(543, 15858671125764767249407148239593086052515682342014256131680163393456727471866994742874618418516215271453471209983161155309309137845617406403755016012549702589349889)
(544, 36666147425527050519905888837640752149788031514160620559771157916786476282472626143100181591746710485771855421663195295254147368352278542465419398724051085419347969)
(545, 71082837953782502848406508421438513370141214469170282802991938047267033774609508351040842840441475542968750388009630142946690603676809935086334539857669588911128577)
(546, 145764806943199562803061447649025812227378186632982098912464480552623537613756206998336918229766063771657437504526077001991947820198015309923875891860031308906364929)
(547, 346416362179826121476411465091820603132966678109247580748758179091111493711704566014566132829999596000543910118781108924487036486273061076053655668926617616845373441)
(548, 694632289877469521505947145586715599009481235065815928150756660411267722455677727177259881934440748343947788601815626207023356278968319871982914743925581299232800769)
(549, 1673595931570069054405520324859185251499527328008312987513481073011603580009793487758683135230647398859770578755669772985833474972643879484311167647281840954110115841)
(550, 2211666021397435341789660730378428681820343103357222216832331439495979354658103437048840401288672745374901119667438872042569183592880997727116586062913314551184228353)
(551, 3923052828841667245810789578702176180934375887159271304063858859317522370345537422918203478282592827434731034072430220547437608000391029328815425237714422881677475841)
^CTraceback (most recent call last):
    ...
KeyboardInterrupt
===[output5iter_odd_primes__one_prime_per_bit_length_:end]
e ../../python3_src/seed/math/_output_/seed.math.primality_proving..doc8out.txt
    view ../../python3_src/seed/math/_output_/seed.math.iter_sorted_products_of_uints..iter_unsorted_primes_lt__prime_eq_one_plus_product_generated_by_strict_sorted_pairwise_coprime_uints_.2-3-5.out.txt
===
]]]
[[[
py_adhoc_call   seed.math.primality_proving   @reformat_output5iter_odd_primes__one_prime_per_bit_length_ +postscript
===[output5reformat_output5iter_odd_primes__one_prime_per_bit_length_:begin]
(2,1<<1 ^1)
(3,1<<2 ^1)
(4,3<<2 ^1)
(5,1<<4 ^1)
(6,5<<3 ^1)
(7,3<<5 ^1)
(8,3<<6 ^1)
(9,1<<8 ^1)
(10,3<<8 ^1)
(11,9<<7 ^1)
(12,13<<8 ^1)
(13,15<<9 ^1)
(14,3<<12 ^1)
(15,9<<11 ^1)
(16,5<<13 ^1)
(17,1<<16 ^1)
(18,5<<15 ^1)
(19,33<<13 ^1)
(20,3<<18 ^1)
(21,9<<17 ^1)
(22,21<<17 ^1)
(23,7<<20 ^1)
(24,13<<20 ^1)
(25,11<<21 ^1)
(26,69<<19 ^1)
(27,25<<22 ^1)
(28,5<<25 ^1)
(29,7<<26 ^1)
(30,45<<24 ^1)
(31,15<<27 ^1)
(32,3<<30 ^1)
(33,59<<27 ^1)
(34,23<<29 ^1)
(35,45<<29 ^1)
(36,49<<30 ^1)
(37,9<<33 ^1)
(38,3<<36 ^1)
(39,73<<32 ^1)
(40,99<<33 ^1)
(41,15<<37 ^1)
(42,5<<39 ^1)
(43,3<<41 ^1)
(44,63<<38 ^1)
(45,27<<40 ^1)
(46,9<<42 ^1)
(47,9<<43 ^1)
(48,15<<44 ^1)
(49,27<<44 ^1)
(50,63<<44 ^1)
(51,19<<46 ^1)
(52,15<<48 ^1)
(53,7<<50 ^1)
(54,23<<49 ^1)
(55,7<<52 ^1)
(56,17<<51 ^1)
(57,25<<52 ^1)
(58,5<<55 ^1)
(59,51<<53 ^1)
(60,49<<54 ^1)
(61,27<<56 ^1)
(62,29<<57 ^1)
(63,87<<56 ^1)
(64,27<<59 ^1)
(65,31<<60 ^1)
(66,45<<60 ^1)
(67,9<<63 ^1)
(68,3<<66 ^1)
(69,9<<65 ^1)
(70,75<<63 ^1)
(71,9<<67 ^1)
(72,33<<66 ^1)
(73,31<<68 ^1)
(74,23<<69 ^1)
(75,221<<67 ^1)
(76,39<<70 ^1)
(77,39<<71 ^1)
(78,5<<75 ^1)
(79,39<<73 ^1)
(80,29<<75 ^1)
(81,67<<74 ^1)
(82,15<<78 ^1)
(83,25<<78 ^1)
(84,145<<76 ^1)
(85,9<<81 ^1)
(86,13<<82 ^1)
(87,249<<79 ^1)
(88,5<<85 ^1)
(89,51<<83 ^1)
(90,37<<84 ^1)
(91,53<<85 ^1)
(92,65<<85 ^1)
(93,87<<86 ^1)
(94,61<<88 ^1)
(95,7<<92 ^1)
(96,57<<90 ^1)
(97,27<<92 ^1)
(98,29<<93 ^1)
(99,33<<93 ^1)
(100,43<<94 ^1)
(101,85<<94 ^1)
(102,57<<96 ^1)
(103,121<<96 ^1)
(104,43<<98 ^1)
(105,131<<97 ^1)
(106,315<<97 ^1)
(107,219<<99 ^1)
(108,29<<103 ^1)
(109,67<<102 ^1)
(110,43<<104 ^1)
(111,53<<105 ^1)
(112,37<<106 ^1)
(113,231<<105 ^1)
(114,105<<107 ^1)
(115,93<<108 ^1)
(116,15<<112 ^1)
(117,73<<110 ^1)
(118,95<<111 ^1)
(119,129<<111 ^1)
(120,153<<112 ^1)
(121,115<<114 ^1)
(122,163<<114 ^1)
(123,7<<120 ^1)
(124,33<<118 ^1)
(125,51<<119 ^1)
(126,71<<119 ^1)
(127,177<<119 ^1)
(128,81<<121 ^1)
(129,11<<125 ^1)
(130,5<<127 ^1)
(131,11<<127 ^1)
(132,81<<125 ^1)
(133,21<<128 ^1)
(134,21<<129 ^1)
(135,111<<128 ^1)
(136,65<<129 ^1)
(137,295<<128 ^1)
(138,9<<134 ^1)
(139,53<<133 ^1)
(140,247<<132 ^1)
(141,67<<134 ^1)
(142,147<<134 ^1)
(143,225<<135 ^1)
(144,111<<137 ^1)
(145,31<<140 ^1)
(146,219<<138 ^1)
(147,355<<138 ^1)
(148,29<<143 ^1)
(149,141<<141 ^1)
(150,43<<144 ^1)
(151,249<<143 ^1)
(152,17<<147 ^1)
(153,35<<147 ^1)
(154,175<<146 ^1)
(155,81<<148 ^1)
(156,163<<148 ^1)
(157,191<<149 ^1)
(158,65<<151 ^1)
(159,63<<153 ^1)
(160,315<<151 ^1)
(161,131<<153 ^1)
(162,105<<155 ^1)
(163,117<<156 ^1)
(164,43<<158 ^1)
(165,183<<157 ^1)
(166,9<<162 ^1)
(167,225<<159 ^1)
(168,141<<160 ^1)
(169,99<<162 ^1)
(170,75<<163 ^1)
(171,93<<164 ^1)
(172,15<<168 ^1)
(173,131<<165 ^1)
(174,61<<168 ^1)
(175,91<<168 ^1)
(176,165<<168 ^1)
(177,7<<174 ^1)
(178,177<<170 ^1)
(179,207<<171 ^1)
(180,27<<175 ^1)
(181,51<<175 ^1)
(182,95<<175 ^1)
(183,7<<180 ^1)
(184,347<<175 ^1)
(185,333<<176 ^1)
(186,299<<177 ^1)
(187,127<<180 ^1)
(188,83<<181 ^1)
(189,25<<184 ^1)
(190,29<<185 ^1)
(191,3<<189 ^1)
(192,13<<188 ^1)
(193,7<<190 ^1)
(194,187<<186 ^1)
(195,45<<189 ^1)
(196,57<<190 ^1)
(197,617<<187 ^1)
(198,159<<190 ^1)
(199,149<<191 ^1)
(200,111<<193 ^1)
(201,183<<193 ^1)
(202,163<<194 ^1)
(203,3<<201 ^1)
(204,261<<195 ^1)
(205,203<<197 ^1)
(206,45<<200 ^1)
(207,85<<200 ^1)
(208,181<<200 ^1)
(209,191<<201 ^1)
(210,9<<206 ^1)
(211,3<<209 ^1)
(212,65<<205 ^1)
(213,11<<209 ^1)
(214,21<<209 ^1)
(215,9<<211 ^1)
(216,275<<207 ^1)
(217,261<<208 ^1)
(218,99<<211 ^1)
(219,73<<212 ^1)
(220,27<<215 ^1)
(221,31<<216 ^1)
(222,105<<215 ^1)
(223,505<<214 ^1)
(224,183<<216 ^1)
(225,615<<215 ^1)
(226,55<<220 ^1)
(227,279<<218 ^1)
(228,381<<219 ^1)
(229,75<<222 ^1)
(230,395<<221 ^1)
(231,245<<223 ^1)
(232,351<<223 ^1)
(233,15<<229 ^1)
(234,63<<228 ^1)
(235,115<<228 ^1)
(236,29<<231 ^1)
(237,25<<232 ^1)
(238,195<<230 ^1)
(239,207<<231 ^1)
(240,83<<233 ^1)
(241,285<<232 ^1)
(242,37<<236 ^1)
(243,67<<236 ^1)
(244,95<<237 ^1)
(245,67<<238 ^1)
(246,65<<239 ^1)
(247,533<<237 ^1)
(248,17<<243 ^1)
(249,291<<240 ^1)
(250,29<<245 ^1)
(251,35<<245 ^1)
(252,177<<244 ^1)
(253,203<<245 ^1)
(254,75<<247 ^1)
(255,167<<247 ^1)
(256,207<<248 ^1)
(257,39<<251 ^1)
(258,43<<252 ^1)
(259,313<<250 ^1)
(260,37<<254 ^1)
(261,135<<253 ^1)
(262,633<<252 ^1)
(263,51<<257 ^1)
(264,65<<257 ^1)
(265,239<<257 ^1)
(266,147<<258 ^1)
(267,91<<260 ^1)
(268,55<<262 ^1)
(269,51<<263 ^1)
(270,159<<262 ^1)
(271,121<<264 ^1)
(272,17<<267 ^1)
(273,25<<268 ^1)
(274,81<<267 ^1)
(275,123<<268 ^1)
(276,175<<268 ^1)
(277,99<<270 ^1)
(278,3<<276 ^1)
(279,177<<271 ^1)
(280,27<<275 ^1)
(281,21<<276 ^1)
(282,261<<273 ^1)
(283,147<<275 ^1)
(284,81<<277 ^1)
(285,297<<276 ^1)
(286,63<<280 ^1)
(287,231<<279 ^1)
(288,125<<281 ^1)
(289,357<<280 ^1)
(290,135<<282 ^1)
(291,325<<282 ^1)
(292,37<<286 ^1)
(293,7<<290 ^1)
(294,77<<287 ^1)
(295,33<<289 ^1)
(296,37<<290 ^1)
(297,59<<291 ^1)
(298,107<<291 ^1)
(299,141<<291 ^1)
(300,287<<291 ^1)
(301,15<<297 ^1)
(302,177<<294 ^1)
(303,81<<296 ^1)
(304,207<<296 ^1)
(305,93<<298 ^1)
(306,71<<299 ^1)
(307,177<<299 ^1)
(308,389<<299 ^1)
(309,267<<300 ^1)
(310,107<<303 ^1)
(311,141<<303 ^1)
(312,13<<308 ^1)
(313,239<<305 ^1)
(314,65<<307 ^1)
(315,231<<307 ^1)
(316,285<<307 ^1)
(317,957<<307 ^1)
(318,21<<313 ^1)
(319,75<<312 ^1)
(320,13<<316 ^1)
(321,153<<313 ^1)
(322,207<<314 ^1)
(323,7<<320 ^1)
(324,559<<314 ^1)
(325,109<<318 ^1)
(326,99<<319 ^1)
(327,51<<321 ^1)
(328,177<<320 ^1)
(329,457<<320 ^1)
(330,625<<320 ^1)
(331,81<<324 ^1)
(332,63<<326 ^1)
(333,35<<327 ^1)
(334,561<<324 ^1)
(335,469<<326 ^1)
(336,297<<327 ^1)
(337,261<<328 ^1)
(338,125<<331 ^1)
(339,45<<333 ^1)
(340,63<<334 ^1)
(341,143<<333 ^1)
(342,177<<334 ^1)
(343,15<<339 ^1)
(344,133<<336 ^1)
(345,25<<340 ^1)
(346,23<<341 ^1)
(347,159<<339 ^1)
(348,559<<338 ^1)
(349,67<<342 ^1)
(350,55<<344 ^1)
(351,81<<344 ^1)
(352,17<<347 ^1)
(353,301<<344 ^1)
(354,423<<345 ^1)
(355,3<<353 ^1)
(356,201<<348 ^1)
(357,941<<347 ^1)
(358,65<<351 ^1)
(359,161<<351 ^1)
(360,165<<352 ^1)
(361,35<<355 ^1)
(362,55<<356 ^1)
(363,231<<355 ^1)
(364,253<<356 ^1)
(365,265<<356 ^1)
(366,261<<357 ^1)
(367,189<<359 ^1)
(368,281<<359 ^1)
(369,131<<361 ^1)
(370,9<<366 ^1)
(371,19<<366 ^1)
(372,113<<365 ^1)
(373,195<<365 ^1)
(374,993<<364 ^1)
(375,555<<365 ^1)
(376,39<<370 ^1)
(377,171<<369 ^1)
(378,45<<372 ^1)
(379,197<<371 ^1)
(380,83<<373 ^1)
(381,39<<375 ^1)
(382,195<<374 ^1)
(383,725<<373 ^1)
(384,285<<375 ^1)
(385,41<<379 ^1)
(386,23<<381 ^1)
(387,159<<379 ^1)
(388,211<<380 ^1)
(389,67<<382 ^1)
(390,235<<382 ^1)
(391,735<<381 ^1)
(392,485<<383 ^1)
(393,7<<390 ^1)
(394,23<<389 ^1)
(395,39<<389 ^1)
(396,29<<391 ^1)
(397,183<<389 ^1)
(398,55<<392 ^1)
(399,105<<392 ^1)
(400,347<<391 ^1)
(401,143<<393 ^1)
(402,21<<397 ^1)
(403,81<<396 ^1)
(404,57<<398 ^1)
(405,93<<398 ^1)
(406,1095<<395 ^1)
(407,97<<400 ^1)
(408,613<<398 ^1)
(409,585<<399 ^1)
(410,3<<408 ^1)
(411,465<<402 ^1)
(412,27<<407 ^1)
(413,39<<407 ^1)
(414,169<<406 ^1)
(415,861<<405 ^1)
(416,63<<410 ^1)
(417,99<<410 ^1)
(418,33<<412 ^1)
(419,403<<410 ^1)
(420,105<<413 ^1)
(421,31<<416 ^1)
(422,129<<414 ^1)
(423,327<<414 ^1)
(424,71<<417 ^1)
(425,291<<416 ^1)
(426,877<<416 ^1)
(427,179<<419 ^1)
(428,81<<421 ^1)
(429,1059<<418 ^1)
(430,393<<421 ^1)
(431,933<<421 ^1)
(432,843<<422 ^1)
(433,765<<423 ^1)
(434,565<<424 ^1)
(435,7<<432 ^1)
(436,1505<<425 ^1)
(437,75<<430 ^1)
(438,225<<430 ^1)
(439,953<<429 ^1)
(440,3<<438 ^1)
(441,105<<434 ^1)
(442,193<<434 ^1)
(443,81<<436 ^1)
(444,745<<434 ^1)
(445,155<<437 ^1)
(446,419<<437 ^1)
(447,177<<439 ^1)
(448,223<<440 ^1)
(449,45<<443 ^1)
(450,177<<442 ^1)
(451,683<<441 ^1)
(452,261<<443 ^1)
(453,25<<448 ^1)
(454,81<<447 ^1)
(455,155<<447 ^1)
(456,955<<446 ^1)
(457,333<<448 ^1)
(458,1181<<447 ^1)
(459,33<<453 ^1)
(460,27<<455 ^1)
(461,67<<454 ^1)
(462,57<<456 ^1)
(463,115<<456 ^1)
(464,449<<455 ^1)
(465,611<<455 ^1)
(466,585<<456 ^1)
(467,135<<459 ^1)
(468,669<<458 ^1)
(469,313<<460 ^1)
(470,45<<464 ^1)
(471,539<<461 ^1)
(472,183<<464 ^1)
(473,131<<465 ^1)
(474,323<<465 ^1)
(475,137<<467 ^1)
(476,17<<471 ^1)
(477,67<<470 ^1)
(478,293<<469 ^1)
(479,551<<469 ^1)
(480,595<<470 ^1)
(481,445<<472 ^1)
(482,249<<474 ^1)
(483,123<<476 ^1)
(484,459<<475 ^1)
(485,447<<476 ^1)
(486,65<<479 ^1)
(487,819<<477 ^1)
(488,261<<479 ^1)
(489,115<<482 ^1)
(490,77<<483 ^1)
(491,53<<485 ^1)
(492,181<<484 ^1)
(493,669<<483 ^1)
(494,253<<486 ^1)
(495,283<<486 ^1)
(496,141<<488 ^1)
(497,105<<490 ^1)
(498,125<<491 ^1)
(499,873<<489 ^1)
(500,1101<<489 ^1)
(501,239<<493 ^1)
(502,299<<493 ^1)
(503,433<<494 ^1)
(504,1451<<493 ^1)
(505,185<<497 ^1)
(506,625<<496 ^1)
(507,295<<498 ^1)
(508,57<<502 ^1)
(509,629<<499 ^1)
(510,711<<500 ^1)
(511,127<<504 ^1)
(512,2401<<500 ^1)
(513,519<<503 ^1)
(514,745<<504 ^1)
(515,755<<505 ^1)
(516,113<<509 ^1)
(517,267<<508 ^1)
(518,249<<510 ^1)
(519,783<<509 ^1)
(520,101<<513 ^1)
(521,15<<517 ^1)
(522,69<<515 ^1)
(523,921<<513 ^1)
(524,39<<518 ^1)
(525,87<<518 ^1)
(526,15<<522 ^1)
(527,417<<518 ^1)
(528,371<<519 ^1)
(529,233<<521 ^1)
(530,169<<522 ^1)
(531,33<<525 ^1)
(532,823<<522 ^1)
(533,367<<524 ^1)
(534,189<<526 ^1)
(535,873<<525 ^1)
(536,3<<534 ^1)
(537,131<<529 ^1)
(538,813<<528 ^1)
(539,277<<530 ^1)
(540,95<<533 ^1)
(541,959<<531 ^1)
(542,169<<534 ^1)
(543,141<<535 ^1)
(544,163<<536 ^1)
(545,79<<538 ^1)
(546,81<<539 ^1)
(547,385<<538 ^1)
(548,193<<540 ^1)
(549,465<<540 ^1)
(550,1229<<539 ^1)
(551,545<<541 ^1)
---postscript:
(12,13<<8 ^1)
(13,15<<9 ^1)
(19,33<<13 ^1)
(26,69<<19 ^1)
(75,221<<67 ^1)
(106,315<<97 ^1)
(197,617<<187 ^1)
(436,1505<<425 ^1)
(512,2401<<500 ^1)
===[output5reformat_output5iter_odd_primes__one_prime_per_bit_length_:end]
(197,617<<187 ^1)
    [is_prime_ 197]
    [is_prime_ 617]
    [187==11*17]
===
]]]
[[[
py_adhoc_call   seed.math.primality_proving   @test4merge_partial_pseudo_primitive_roots_into_single_one
py_adhoc_call   seed.math.primality_proving   @test4merge_partial_pseudo_primitive_roots_into_single_one 109
py_adhoc_call   seed.math.primality_proving   @test4merge_partial_pseudo_primitive_roots_into_single_one =109
py_adhoc_call   seed.math.primality_proving   @test4merge_partial_pseudo_primitive_roots_into_single_one =125
py_adhoc_call   seed.math.primality_proving   @test4merge_partial_pseudo_primitive_roots_into_single_one =148
===[output5test4merge_partial_pseudo_primitive_roots_into_single_one:begin]
(2, 3, 2)
(3, 5, 2)
(4, 13, 2)
(5, 17, 3)
(6, 41, 11)
(7, 97, 10)
(8, 193, 78)
(9, 257, 3)
(10, 769, 755)
(11, 1153, 866)
(12, 3329, 2953)
(13, 7681, 6497)
(14, 12289, 9186)
(15, 18433, 16542)
(16, 40961, 32168)
(17, 65537, 6)
(18, 163841, 32757)
(19, 270337, 8620)
(20, 786433, 17933)
(21, 1179649, 217718)
(22, 2752513, 1418044)
(23, 7340033, 6262937)
(24, 13631489, 3880477)
(25, 23068673, 7529398)
(26, 36175873, 7023606)
(27, 104857601, 20080126)
(28, 167772161, 3)
(29, 469762049, 15745258)
(30, 754974721, 491510594)
(31, 2013265921, 652092105)
(32, 3221225473, 3172072973)
(33, 7918845953, 7400254634)
(34, 12348030977, 2461381352)
(35, 24159191041, 14453154916)
(36, 52613349377, 8807680913)
(37, 77309411329, 19932170834)
(38, 206158430209, 4186958644)
(39, 313532612609, 26248221663)
(40, 850403524609, 490857377982)
(41, 2061584302081, 785361059982)
(42, 2748779069441, 3)
(43, 6597069766657, 5)
(44, 17317308137473, 17112340408519)
(45, 29686813949953, 3595570523970)
(46, 39582418599937, 32954208611848)
(47, 79164837199873, 77036364097355)
(48, 263882790666241, 120463176856900)
(49, 474989023199233, 393597830171371)
(50, 1108307720798209, 735606654856382)
(51, 1337006139375617, 1086434322414604)
(52, 4222124650659841, 1561448461719384)
(53, 7881299347898369, 4401128866676326)
(54, 12947848928690177, 11031226835064719)
(55, 31525197391593473, 30072326117196523)
(56, 38280596832649217, 6233618657302977)
(57, 112589990684262401, 96818690048144943)
(58, 180143985094819841, 17186879953728393)
(59, 459367161991790593, 64028395532430434)
(60, 882705526964617217, 126100304683978181)
(61, 1945555039024054273, 794613454146180503)
(62, 4179340454199820289, 3)
(63, 6269010681299730433, 3655957478606009507)
(64, 15564440312192434177, 10501964674862354950)
(65, 35740566642812256257, 11384496769234765745)
(66, 51881467707308113921, 39065856179572450097)
(67, 83010348331692982273, 14154022620613157831)
(68, 221360928884514619393, 221360915999612730893)
(69, 332041393326771929089, 264382038260359363609)
(70, 691752902764108185601, 202444913137815112394)
(71, 1328165573307087716353, 1147335646366363202745)
(72, 2434970217729660813313, 2244530950151457744138)
(73, 9149585060559937601537, 8371514034428409145990)
(74, 13576803638250229989377, 7411046877568233527297)
(75, 32613843522318487257089, 24878842032039334565684)
(76, 46043073207979040833537, 31934091310364510121555)
(77, 92086146415958081667073, 12798546600981985174260)
(78, 188894659314785808547841, 3)
(79, 368344585663832326668289, 89793482840266970898520)
(80, 1095589024025757689577473, 27524823421191418570762)
(81, 1265594217409064917270529, 380421411015022890012097)
(82, 4533471823554859405148161, 4269240114449969049482820)
(83, 7555786372591432341913601, 3225934774230391894354393)
(84, 10955890240257576895774721, 2477326998927972674546178)
(85, 21760664753063325144711169, 20140980928145493792858247)
(86, 62864142619960717084721153, 52275448873202408919439905)
(87, 150511264542021332250918913, 121851823657314786282388010)
(88, 193428131138340667952988161, 44746884680582066421044303)
(89, 493241734402768703280119809, 431819599019279317384729300)
(90, 715684085211860471426056193, 694278793144440611361124387)
(91, 2050338190066411080301674497, 561360483028155517250571141)
(92, 2514565704798428683388846081, 2135747439375332625672456692)
(93, 6731298963614255244763987969, 6553839529388436022481279178)
(94, 18878585599102049192211644417, 14471104062766270883691733223)
(95, 34662321099990647697175478273, 33407226322703699564302845271)
(96, 70562582239266675669250080769, 34618023713629230877271718333)
(97, 133697524242821069689105416193, 71385889259790514476200232111)
(98, 287202089114208223776596819969, 175196363348994280375236798157)
(99, 326816170371340392573368795137, 27346927845056055049520485430)
(100, 851702747028341629130597466113, 54284957068636988423846508455)
(101, 1683598453428117173862808944641, 430087084664396922931924124369)
(102, 4516005263313067242832005169153, 3587078419201335011159427343384)
(103, 9586607664225984848818817990657, 5005014312554320313620145779128)
(104, 13627243952453466066089559457793, 1795105763180443563347941784215)
(105, 20757778578737256449508514988033, 19156305571214245376410479504769)
(106, 49913742383986532683932688711681, 44014345014181549788531990378186)
(107, 138807740724991119463889000988673, 2372636976631827430449142733461)
(108, 294094939252949221147235143647233, 229551015370752446347462974383096)
(109, 339730360861165479601116459040769, 315614856048733740640109854496786)
(110, 872143612957021828229731805298689, 472304828783555527312076301851837)
(111, 2149935417987077064938408636317697, 1588394988655895437289824677356205)
(112, 3001796621340447222744193190330369, 2357930801742169792529824335799140)
(113, 9370473236887071735863630094139393, 2961771685846481242506034429521215)
(114, 17037224067067403156115691080253441, 17009241519428472753937545386168830)
(115, 30180225490233685590833509913591809, 8915643999228293541106948712495768)
(116, 77884452878022414427957444938301441, 20841748977298780978422209212685820)
(117, 94759417668260604220681558008266753, 85209161240180011299418895207390301)
(118, 246634100780404312355198575637954561, 230236592918389136478968251606899801)
(119, 334903147375496382040217013234696193, 243208786268397646552479931670860761)
(120, 794421419355828627165165938370674689, 490772649480856431106708300698607065)
(121, 2388456554926020709124028311441244161, 633283466359918165885339532160208762)
(122, 3385377551764707613801883606651502593, 1000946712926454646953777632462880480)
(123, 9304595970494411110326649421962412033, 3)
(124, 10966130965225555951456408247312842753, 8855244759217522690616013549165728388)
(125, 33895313892515354759047080037148786689, 27541227106729583936072878481355545607)
(126, 47187593850364513488085150639952232449, 24824221529113997706185631481228989482)
(127, 117636677626965054751986924834810494977, 112982158743197284273383337157096022248)
(128, 215334935317156371410416743765415821313, 111041993993932988296743437413827575557)
(129, 467888254516290387262140085218681290753, 185206520226120738854529003438975339097)
(130, 850705917302346158658436518579420528641, 787785953932212754306254620773304287043)
(131, 1871553018065161549048560340874725163009, 773839690699239915176358262818570156128)
(132, 3445358965074501942566667900246653140993, 2872341836178646996822303508822225848316)
(133, 7145929705339707732730866756067132440577, 2820408113353335737738327720824395666603)
(134, 14291859410679415465461733512134264881153, 2842291043359633565273216556401790537758)
(135, 37771342728224169444434581424926271471617, 3657741094744798462394338919569996310970)
(136, 44236707699722000250238698966129867489281, 17728887098242275817324374230716808627227)
(137, 100383298241676846721695509192371622379521, 2013689901423399526235694434498570679728)
(138, 196002643346460554954903773880698489798657, 53749199486622520327319333567839037112711)
(139, 577118894297911634033883334204278886629377, 285357238752713524881588017117605340904026)
(140, 1344795914071548807607256448570347971674113, 1062858728229816005859750867147961243860929)
(141, 1459130789356984131330950316667422090723329, 1055541611738664320798904809165982783848225)
(142, 3201376507992189064263428306718075333378049, 581890665453611800777969132192353631071282)
(143, 9800132167323027747745188694034924489932801, 803052663992603066560171319900065652811688)
(144, 19338927476850774755550505689562250993467393, 16359207357713706806773739488891185035683435)
(145, 43207693822153082336725454153256200417837057, 25535743006280913431506243371517937576163259)
(146, 76310362476221976062442535964218612028276737, 65186389755697194599246156616731372822055754)
(147, 123699446023099550238205937293596380228485121, 120236323524414640073803394804867361215283376)
^CTraceback (most recent call last):
    ...
KeyboardInterrupt
===[output5test4merge_partial_pseudo_primitive_roots_into_single_one:end]
]]]
[[[
py_adhoc_call   seed.math.primality_proving   @test4try_optimize_reduce_pseudo_primitive_root_   --level=8
py_adhoc_call   seed.math.primality_proving   @test4try_optimize_reduce_pseudo_primitive_root_   --level=8 +verbose
效果一般
===
===
]]]




#]]]'''
if 0:
    __all__ = r'''
Error
    ValidateFail
        ValidateFail__order_mod_
        ValidateFail__order_mod__proper_factor
        ValidateFail__order_mod__not_order
        ValidateFail__order_mod__not_corresponding_partial_primitive_root
    PrimalityFail
        PrimalityFail__is_prime_ex__Nmm_____assume_case


    validate_order_mod_
    validate_primality__Pmm_
    Case4is_prime__Nmm____how_to_find_primitive_root
    Case4is_prime__Nmm____how_many_prime_bases_to_be_test
    ResultCase4is_prime__Nmm_
    default_case4num
    default_case4root
    is_prime__Nmm_
    is_prime_ex__Nmm_
    test_many4is_prime_ex__Nmm_
    test_one4is_prime_ex__Nmm_
'''.split()#'''
__all__ = r'''
    iter_pow_IIs_except_one_
    iter_pow_II1_except_one_
    validate_primality__Nmm__complete_factorization_
    validate_primality__Nmm_
    N2num_prime_bases__ERH
    N2num_prime_bases__heuristically
    N2num_prime_bases__tiny__one_plus_2floor_log2_P
    iter_detect_primality__Nmm_
    Error
    ValidateFail
    ValidateFail__order_mod_
    ValidateFail__order_mod__proper_factor
    ValidateFail__order_mod__not_order
    ValidateFail__nonprime
    ValidateFail__nonprime__nontrivial_factor
    ValidateFail__bad_setting
    ValidateFail__bad_setting__eF_eR_not_coprime
    ValidateFail__bad_setting__cannot_conform_primality

    DetectPrimalityFail
    DetectPrimalityFail__bad_setting
    DetectPrimalityFail__bad_setting__cannot_conform_primality
    DetectPrimalityFail__bad_setting__too_few_num_prime_bases



    is_composite_ex__Nmm_
        is_composite__Nmm_
        validate_result5is_composite_ex__Nmm_

    test_many4is_composite_ex__Nmm_
        test_one4is_composite_ex__Nmm_

    continue4iter_odd_primes__one_prime_per_bit_length_
    iter_odd_primes__one_prime_per_bit_length_
        iter_odd_primes__Pocklington_Theorem_1914__factor_2s__bit_length_
            iter_odd_uints__Pocklington_Theorem_1914__factor_2s__bit_length_

    OddInt__ge3__repr_by_lshift_odd_plus1
        output5reformat_output5iter_odd_primes__one_prime_per_bit_length_

    validate_output5iter_odd_primes__one_prime_per_bit_length_
        validate_primality_certificate4two_dominanted_odd_int_
    filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_
        output5filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_

    merge_partial_pseudo_primitive_roots_into_single_one
        test4merge_partial_pseudo_primitive_roots_into_single_one
            output5iter_odd_primes__one_prime_per_bit_length_
                reformat_output5iter_odd_primes__one_prime_per_bit_length_

    try_optimize_reduce_pseudo_primitive_root_
        test4try_optimize_reduce_pseudo_primitive_root_
            output5test4merge_partial_pseudo_primitive_roots_into_single_one
'''.split()#'''
__all__

def __():
    #API
    ...


from seed.for_libs.for_time import (
Timer__print_err
    ,timer__print_err__thread_wide
    ,timer__print_err__process_wide
    ,timer__print_err__system_wide__highest_resolution
    ,timer__print_err__system_wide__monotonic
)

timer = timer__print_err__thread_wide

if 1:
    from seed.iters.apply_commutative_operations_except_one import iter_apply_commutative_operations_except_one_
    #def iter_apply_commutative_operations_except_one_(apply_, commutative_operation_keys, x0, /):
    from seed.math.II import II, II_mod, II__p2e_, II__ft2e_, II__ft_e_pairs_
    from seed.math.gcd import gcd
    from seed.math.floor_ceil import floor_log2
    from seed.mapping_tools.dict_op import inv__k2v_to_v2ks

    #from seed.seq_tools.split_tuples import split_tuples, unzip_pairs
    #from seed.iters.difference_of_two_sorted_iterables import difference_of_two_sorted_iterables
    from seed.seq_tools.remove_strict_sorted_indices import lsls2lsls_pair__via_idc_ #ls2ls_pair__via_idc_
    from seed.seq_tools.remove_strict_sorted_indices import iter_complement_idc_, iter_values__via_idc_
    from seed.seq_tools.remove_strict_sorted_indices import list_rngs__via_idc_, list_values__via_idc_, list_idc4reserve_, list_complement_idc_
    from seed.seq_tools.remove_strict_sorted_indices import iter_ints_in_gaps_
    from seed.math.floor_ceil import floor_sqrt #perfect_div, perfect_kth_root_

    from seed.math.prime_gens import prime_gen
    #from seed.math.prime_gens import is_prime__le_pow2_81_ #is_strong_pseudoprime__basis_, is_prime__using_A014233_, is_prime__le_pow2_81_, is_prime__tribool_, Case4is_prime__tribool_
    from seed.tiny import print_err
    from seed.tiny import check_type_is
    from seed.tiny_.check import check_int_ge, check_uint_lt, check_int_ge_lt # check_int_ge_le
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
    from seed.math.prime_gens import tabulate_may_factorization4uint_lt_# min_prime_factor_gen, tabulate_may_min_prime_factor4uint_lt_
    #def tabulate_may_factorization4uint_lt_(sz, uint2may_min_prime_factor=None, /):
    #    '-> uint2may_factorization/[may p2e/{prime:exp}]/[None,p2e...]'
    from seed.math.are_pairwise_coprime import are_pairwise_coprime

    from itertools import count as count_
    from itertools import islice
    from fractions import Fraction
    if 0:
        # using builtin eval since f'{odd}<<{e2}^1'
        from ast import literal_eval
        eval = literal_eval

    from enum import Enum, auto


def __():
    from seed.mapping_tools.dict_op import inv__k2v_to_v2k, inv__k2v_to_v2ks, inv__k2vs_to_v2k, inv__k2vs_to_v2ks
    from seed.math.prime_gens import is_strong_pseudoprime_
    #def is_strong_pseudoprime_(base, n, /, *, to_find_sqrt_neg1=False):
    #    'base/int{>=2,%n=!=0} -> n{>=3,odd} -> [n is base-SPRP]'


_int_pow_ = int.__pow__
def _int_pow(base, exp, modulus, /):
    assert modulus > 1
    if base+1 == modulus:
        return 1 if exp&1==0 else base
    return _int_pow_(base, exp, modulus)
class _pow_ne_:
    def __init__(sf, modulus, ne, Err, /):
        sf.modulus = modulus
        sf.ne = ne
        sf.Err = Err
    def __call__(sf, base, exp, /):
        x = _int_pow(base, exp, sf.modulus)
        if x == sf.ne:
            raise sf.Err
        return x

def __():
  def _pow_(modulus, base, exp, /):
    return _int_pow(base, exp, modulus)
    assert exp >= 0
    if exp >= 2:
        if not -modulus < (base<<1) < modulus:
            base %= modulus
            base -= modulus
        if abs(base) < 2:
            if base == -1 and (exp&1 == 0):
                base = 1
            return base
    return _int_pow(base, exp, modulus)

def _mk_x_(_pow_, ft_e_pairs, g, /):
    x = g
    for ft, e in ft_e_pairs:
        for _ in range(e):
            x = _pow_(x, ft)
    return x
def _mk_x1_(_pow_, fts, es, g, /):
    ft_e_pairs = zip(fts, es)
    x1 = _mk_x_(_pow_, ft_e_pairs, g)
    return x1
def _mk_x0_(_pow_, fts, es, g, /):
    ft_e_pairs = zip(fts, es)
    ft_emm_pairs = [(ft, e-1) for ft, e in ft_e_pairs if e >= 1]
    x0 = _mk_x_(_pow_, ft_emm_pairs, g)
    return x0
def iter_pow_IIs_except_one_(_pow_, fts, es, g, /):
    x0 = _mk_x0_(_pow_, fts, es, g)
    return iter_pow_II1_except_one_(_pow_, fts, x0)
def iter_pow_II1_except_one_(_pow_, fts, x0, /):
    def apply_(ft, x, /):
        x = _pow_(x, ft)
        return x
    return iter_apply_commutative_operations_except_one_(apply_, fts, x0)

def validate_primality__Nmm__complete_factorization_(e2, ps, es, g2, gs, /):
    r'''
    [@[p :<- ps] -> [is_prime_(p)]]
    '''#'''
    # not using gcd
    assert len(ps) ==  len(es) ==  len(gs)
    assert all(p&1 == 1 for p in ps)
    assert all(p >= 3 for p in ps)
    assert all(e >= 1 for e in es)
    L = len(ps)
    assert e2 >= 0
    assert e2 >= 1 or L==0

    p_e_pairs = [*zip(ps, es)]
    Nmm = II__ft_e_pairs_(p_e_pairs) << e2
    assert Nmm >= 1
    N = Nmm+1
    assert N >= 2
    if N <= 3: return
    assert e2 >= 1
    assert e2 >= 2 or L >= 1
    #_es[0] -= 1
    # if e2==0: del _es[0], ...
    #_pow_ = _pow_ne_(N, Nmm, ValidateFail__order_mod__proper_factor)
    #   Nmm: too tedious to handle [e2==1]
    #to check:xxx since too tedious to handle [e2==1]
        #[g2 :: int][g2**(e///2) %m == m-1]
        #[gs :: [int]{len=L}][@[i :<- [0..<L]] -> [gs[i]**(e///2///ps[i]) %m =!= m-1]][@[i :<- [0..<L]] -> [gs[i]**(e///2) %m == m-1]]
    #to check:
        #[g2 :: int][g2**(e///2) %m =!= 1][g2**e %m == 1]
        #[gs :: [int]{len=L}][@[i :<- [0..<L]] -> [gs[i]**(e///ps[i]) %m =!= 1]][@[i :<- [0..<L]] -> [gs[i]**e %m == 1]]

    #_pow_ = _pow_ne_(modulus, modulus-1, ValidateFail__order_mod__proper_factor)
    _main_loop4validate__Nmm_(e2, ps, es, g2, gs, N, using_gcd=False)
    return
def _main_loop4validate__Nmm_(e2, fts, es, g2, gs, N, /, *, using_gcd):
    _fts = [2, *fts]
    _es = [e2, *es]
    _gs = [g2, *gs]
    _main_loop4validate__Nmm__ver2_(_fts, _es, _gs, 1, N, using_gcd=using_gcd)
    return
def _main_loop4validate__Nmm__ver2_(_fts, _es, _gs, remain_ft, N, /, *, using_gcd):
    if not using_gcd:
        assert remain_ft == 1
        #assert fts == Bs
    remain_ft = None

    g2js = inv__k2v_to_v2ks(_gs, True, set_vs_list=True)
    _pow_ = _pow_ne_(N, 1, ValidateFail__order_mod__proper_factor)

    g_js_pairs = sorted(g2js.items(), key=lambda kv:kv[1][0])
    assert g_js_pairs[0][1][0] == 0
    #####e2,g2...
        #assert g_js_pairs[0][0] == g2
        #assert _es[0] == e2
        #assert _fts[0] == 2
    for g, js in g_js_pairs:
        #ks = difference_of_two_sorted_iterables(range(L), js)
        ([selected_fts, selected_es], [unselected_fts, unselected_es]) = lsls2lsls_pair__via_idc_(js, [_fts, _es])
        g0 = _mk_x1_(_pow_, unselected_fts, unselected_es, g)
        it = iter_pow_IIs_except_one_(_pow_, selected_fts, selected_es, g0)
        for i, x in enumerate(it):
            #assert not x == 1
            #   valid via _pow_/_pow_ne_
            if i==0:
                j = js[i]
                _ft = _fts[j]
                #_e = _es[j]
                if not _int_pow(x, _ft, N) == 1:
                    raise ValidateFail__order_mod__not_order
            #####
            if using_gcd:
                if not (ft4m := gcd(x-1, N)) == 1:
                    if not 1 < ft4m < N: raise 000
                    assert N %ft4m == 0
                    raise ValidateFail__nonprime__nontrivial_factor(ft4m)
    return
def validate_primality__Nmm__ver2_(fts, es, Bs, gs, remain_ft, /):
    . 
    r'''
    [Bs :: [pint]{len=L}][@[i :<- [0..<L]] -> @[p4ft :<- all_prime_factors_of_(fts[i])] -> [p4ft >= Bs[i]]]
    [N-1 == remain_ft*II__ft_e_pairs_(zip(fts, es))]

    remain_ft distinguish from fts: without g
    '''#'''
    fts = [*fts]
    es = [*es]
    Bs = [*Bs]
    gs = [*gs]
    assert len(fts) ==  len(es) ==  len(Bs) ==  len(gs)
    using_gcd = True

    case, payload = _ex_check_setting4validate_primality__Nmm__partial_factorization__ver2_(fts, es, Bs, remain_ft, detect_complete_factorization__vs__try_reduce_len=False)
    C = _ResultCase4ex_check_setting_ver2
    if case is C.square_case__basic:
        N = payload
        pass
    elif case is C.square_case__len_reduced:
        (js, fts, es, Bs, remain_ft, N) = payload
        gs = list_values__via_idc_(js, gs)
        pass
    elif case is C.complete_factorization:
        N = payload
        using_gcd = False
        pass
    elif case is C.cubic_case:
        (j2, e2, fts, es, Bs, must_be_composite, N) = payload
        g2 = gs[j2]
        gs = _without_idx_(j2, gs)
        validate_primality__Nmm_(e2, fts, es, Bs, g2, gs)
        return
    elif case is C.N_eq_2:
        return
    else:
        raise 000
    #square_case__basic | square_case__len_reduced | complete_factorization
    (fts, es, Bs, gs, remain_ft, N), using_gcd
    _main_loop4validate__Nmm__ver2_(fts, es, gs, remain_ft, N, using_gcd=using_gcd)
    return
class _ResultCase4ex_check_setting_ver2(Enum):
    N_eq_2 = auto()
    complete_factorization = auto()
    square_case__len_reduced = auto()
    square_case__basic = auto()
    cubic_case = auto()
def _without_idx_(idx, ls, /):
    ls = [*ls]
    del ls[idx]
    return ls
def _ex_check_setting4validate_primality__Nmm__partial_factorization__ver2_(fts, es, Bs, remain_ft, /, *, detect_complete_factorization__vs__try_reduce_len):
    r'''
    -> (case/_ResultCase4ex_check_setting_ver2, payload) | ^ValidateFail__bad_setting | ^ValidateFail__bad_setting__eF_eR_not_coprime | ^ValidateFail__bad_setting__cannot_conform_primality | ^ValidateFail__nonprime__nontrivial_factor
        * -> (N_eq_2, 2)
        * -> (complete_factorization, N)
        * -> (square_case__len_reduced, (js, fts, es, Bs, remain_ft, N))
        * -> (square_case__basic, N)
        * -> (cubic_case, (j2, e2, fts, es, Bs, must_be_composite, N))

    [Bs :: [pint]{len=L}][@[i :<- [0..<L]] -> @[p4ft :<- all_prime_factors_of_(fts[i])] -> [p4ft >= Bs[i]]]
    #neednot [are_pairwise_coprime(fts)]

    see:_ex_check_setting4validate_primality__Nmm__partial_factorization_
    '''#'''

    check_type_is(bool, detect_complete_factorization__vs__try_reduce_len)
    assert len(fts) ==  len(es) ==  len(Bs)
    fts = [*fts]
    es = [*es]
    Bs = [*Bs]
    assert all(ft >= 2 for ft in fts)
    assert all(B >= 2 for B in Bs)
    assert all(ft >= B for ft, B in zip(fts, Bs))
    assert all(e >= 1 for e in es)
    assert remain_ft >= 1
    L = len(fts)
    if L == 0:
        if remain_ft == 1:
            N = 2
            return _ResultCase4ex_check_setting_ver2.N_eq_2, N
        raise ValidateFail__bad_setting

    pows5ft = [*map(_int_pow_, fts, es)]
    Nmm = remain_ft * II(pows4ft)
    N = Nmm + 1
    assert N >= 3
    if N&1 == 0: raise ValidateFail__nonprime__nontrivial_factor(2)
    # [N >= 3][N%2 == 1]


    if detect_complete_factorization__vs__try_reduce_len is False:
        is_complete_factorization = (remain_ft==1 and fts==Bs)
        using_gcd = not is_complete_factorization
        if not using_gcd:
            #N = 1+II__ft_e_pairs_(zip(fts, es))
            return _ResultCase4ex_check_setting_ver2.complete_factorization, N



    fsqrtN = floor_sqrt(N)
    pows5B = [*map(_int_pow_, Bs, es)]
    e5B = II(pows4B)
    if e5B+1 > fsqrtN:
        js = sorted(range(L), reverse=True, key=lambda j:(pows4B[j], -pows4ft[j]))
            #key=pows4B.__getitem__

        for k, e5B4k in enumerate(accumulate(js, lambda i,j: pows4B[i]*pows4B[j]), 1):
            if e5B4k+1 > fsqrtN:
                break
        else:
            raise 000
        if k < L:
            js = js[:k]
            js.sort()
            cs = list_complement_idc_(L, js)
            _fts = list_values__via_idc_(cs, fts)
            _es = list_values__via_idc_(cs, es)
            remain_ft *= II(map(_int_pow_, _fts, _es))

            fts = list_values__via_idc_(js, fts)
            es = list_values__via_idc_(js, es)
            Bs = list_values__via_idc_(js, Bs)
            return _ResultCase4ex_check_setting_ver2.square_case__len_reduced, (js, fts, es, Bs, remain_ft, N)
        return _ResultCase4ex_check_setting_ver2.square_case__basic, N

    if not remain_ft == 1: raise ValidateFail__bad_setting
    if not 2 in fts: raise ValidateFail__bad_setting
    j2 = fts.index(2)
    e2 = es[j2]
    assert Bs[j2] == 2
    assert fts[j2] == 2

    fts = _without_idx_(j2, fts)
    es = _without_idx_(j2, es)
    Bs = _without_idx_(j2, Bs)
    if not all(ft&1 == 1 for ft in fts): raise ValidateFail__bad_setting
    if not all(B >= 3 for B in Bs): raise ValidateFail__bad_setting


    e2, fts, es, Bs
    js = [i for i in range(L) if fts[i] == Bs[i]]
    (must_be_composite, _N) = _ex_check_setting4validate_primality__Nmm__partial_factorization_(e2, fts, es, Bs, js)
        # raise: ^ValidateFail__bad_setting__eF_eR_not_coprime | ^ValidateFail__bad_setting__cannot_conform_primality | ^ValidateFail__nonprime__nontrivial_factor
    assert N == _N
    return _ResultCase4ex_check_setting_ver2.cubic_case, (j2, e2, fts, es, Bs, must_be_composite, N)



def validate_primality__Nmm_(e2, fts, es, Bs, g2, gs, /):
    r'''
    [@[ft :<- fts] -> [[ft%2==1][ft>=3]]]
    [Bs :: [pint]{len=L}][@[i :<- [0..<L]] -> @[p4ft :<- all_prime_factors_of_(fts[i])] -> [p4ft >= Bs[i]]]
    '''#'''
    assert len(fts) ==  len(es) ==  len(Bs) ==  len(gs)
    L = len(fts)
    assert all(ft&1 == 1 for ft in fts)
    assert all(ft >= 3 for ft in fts)
    assert all(B >= 3 for B in Bs)
    assert all(ft >= B for ft, B in zip(fts, Bs))
    assert all(e >= 1 for e in es)
    assert e2 >= 0
    assert e2 >= 1 or L==0
    if e2 == 0:
        if not L == 0:
            raise ValidateFail__nonprime__nontrivial_factor(2)
        N = 2
        if not g2&1 == 1: raise ValidateFail__bad_setting
        return

    assert e2 >= 1

    js = [i for i in range(L) if fts[i] == Bs[i]]
    if len(js) == L:
        ps = fts
        validate_primality__Nmm__complete_factorization_(e2, ps, es, g2, gs)
    else:
        _validate_primality__Nmm__partial_factorization_(e2, fts, es, Bs, g2, gs, js)
    return

def _ex_check_setting4validate_primality__Nmm__partial_factorization_(e2, fts, es, Bs, js, /):
    r'''
    -> (must_be_composite, N) | ^ValidateFail__bad_setting__eF_eR_not_coprime | ^ValidateFail__bad_setting__cannot_conform_primality | ^ValidateFail__nonprime__nontrivial_factor

    [@[ft :<- fts] -> [[ft%2==1][ft>=3]]]
    [Bs :: [pint]{len=L}][@[i :<- [0..<L]] -> @[p4ft :<- all_prime_factors_of_(fts[i])] -> [p4ft >= Bs[i]]]
    '''#'''

    # using gcd
    assert e2 >= 1
    L = len(fts)
    assert L >= 1

    js
    cs = list_complement_idc_(L, js)

    #js:
    ps = list_values__via_idc_(js, fts)
    es4p = list_values__via_idc_(js, es)

    #cs:
    fts4np = list_values__via_idc_(cs, fts)
    Bs4np = list_values__via_idc_(cs, Bs)
    es4np = list_values__via_idc_(cs, es)

    ej = II__ft_e_pairs_(zip(ps, es4p)) << e2
    eR = II__ft_e_pairs_(zip(fts4np, es4np))
    e5ft = ej * eR
    e5B = ej * II__ft_e_pairs_(zip(Bs4np, es4np))
    # [e5ft := 2**e2 * II fts[i]**es[i] {i :<- [0..<L]}]
    # [e5B := 2**e2 * II Bs[i]**es[i] {i :<- [0..<L]}]
    # [ej := 2**e2 * II fts[j]**es[j] {j :<- js}]
    111; js=None # del js

    Nmm = e5ft
    N = Nmm+1
    assert N >= 7

    must_be_composite = False
    if N < (e5B+1)**2:
        pass
    else:
        # [N >= (e5B+1)**2]
        m = N
        eF = ej
        eR
        # [m >= (e5B+1)**2]
        # !! [e5B >= ej == eF]
        # [m >= (eF+1)**2]
        # !! [m == 1+eF*eR]
        # [1+eF*eR >= (eF+1)**2]
        # [eR >= eF+2]
        #assert m == 1+eF*eR
        if not gcd(eF,eR)==1: raise ValidateFail__bad_setting__eF_eR_not_coprime
        # [gcd(eF,eR) == 1]
        # !! [eF%2 == 0]
        # [eR%2 == 1]
        # !! [eR >= eF+2]
        # [eR >= eF+3]

        #u = if e5ft%3 == 1 then 3 else 1
        u = 3 if m%3 == 2 else 1
        _2_u_eF = (2*u*eF)
        (q, r) = divmod(eR, _2_u_eF)
        assert eR&1 == 1
        assert r&1 == 1
        # [r <= eR]

        #bug:e5B//eF:kB = min(e5B, ((_2_u_eF +r-1)>>1))
        kB = min(e5B//eF, ((_2_u_eF +r-1)>>1))
            # select kB to max rhs => [m < rhs]
            #   => (2*u*eF+r)/2 but r is odd
        assert kB >= 1
        if not m < (kB*eF +1) * ((_2_u_eF +r -kB)*eF +1): raise ValidateFail__bad_setting__cannot_conform_primality
        # [m < (kB*eF +1) * ((_2_u_eF +r -kB)*eF +1)]

        # [gcd...to check:ok] => [[is_prime_(m)] <-> [not$ [[r >= 2*kB][q >= ceil_(kB**2 /(2*u)) >= 1][sqrt(r**2 -8*u*q) %1 == 0]]]]
        if r >= 2*kB and 2*u*q >= kB**2 and (sq := r**2 -8*u*q) >= 0 and (sqrt := floor_sqrt(sq))**2 == sq:
            # [(s+t) == r]
            # [(s-t) == sqrt(r**2 -8*u*q)]
            # [m == (1+s*eF)*(1+t*eF)]
            assert q > 0
            r, sqrt
            assert r&1 == 1
            assert sqrt&1 == 1
            assert 0 <= sqrt < r
            s = (r+sqrt)//2
            t = (r-sqrt)//2
            assert 0 < t <= s < t+s == r < _2_u_eF
            assert 0 < t <= (r-1)//2 <= (_2_u_eF-2)//2 == u*eF -1
            assert kB <= (r-1)//2

            ft4m = (1+t*eF)
            # !! [r <= eR]
            assert 0 < t < r <= eR
            assert 3 <= 1+t*eF < 1+eR*eF == m
            assert 3 <= ftm < m
            #not check gcd yet:
                #assert m == (1+s*eF)*(1+t*eF)

                #assert 1 < ft4m < m
                #assert m %ft4m == 0
            #if 1 < ft4m < m and m %ft4m == 0:
            assert 1 < ft4m < m
            if m %ft4m == 0:
                raise ValidateFail__nonprime__nontrivial_factor(ft4m)
            # [gcd ... to check:must fail]
            # [any (g2,gs) must cause failure]
            # [is_composite_(N)]
            must_be_composite = True
    return (must_be_composite, N)
    #return (may_ft4m, N)

def _validate_primality__Nmm__partial_factorization_(e2, fts, es, Bs, g2, gs, js, /):
    # [@[ft :<- fts] -> [[ft%2==1][ft>=3]]]
    # [Bs :: [pint]{len=L}][@[i :<- [0..<L]] -> @[p4ft :<- all_prime_factors_of_(fts[i])] -> [p4ft >= Bs[i]]]
    (must_be_composite, N) = _ex_check_setting4validate_primality__Nmm__partial_factorization_(e2, fts, es, Bs, js)


    ######################
    ######################
    ######################
    # check ... gcd
    #to check:
        # [g2 :: int][g2**(e5ft///2) %m == m-1]
        # [gs :: [int]{len=L}][@[i :<- [0..<L]] -> [gcd(gs[i]**(e5ft///2///fts[i]) %m +1, m) == 1]][@[i :<- [0..<L]] -> [gs[i]**(e5ft///2) %m == m-1]]
    #to check:
        # [g2 :: int][gcd(g2**(e5ft///2) %m -1, m) == 1][g2**e5ft %m == 1]
        # [gs :: [int]{len=L}][@[i :<- [0..<L]] -> [gcd(gs[i]**(e5ft///fts[i]) %m -1, m) == 1]][@[i :<- [0..<L]] -> [gs[i]**e5ft %m == 1]]
    _main_loop4validate__Nmm_(e2, fts, es, g2, gs, N, using_gcd=True)
    # [is_prime_(N)]

    if must_be_composite:
        # [is_composite_(N)]
        # _L
        raise 000
    return






class _detect_compositeness__Nmm:
    def __init__(sf, e2, fts, es, N, max1_len_rootss, /):
        assert e2 >= 1
        assert N >= 3
        assert N&1 == 1
        max1_len_rootss = max(2, min(1+e2, max1_len_rootss))
        assert 2 <= max1_len_rootss <= 1+e2
        sf.args = (e2, fts, es, N, max1_len_rootss)
        sf.rootss = [[1], [N-1]] # ++[set<root>]
            # [len(rootss[i]) == 2**max(0,i-1)]
            # [0 <= i < max(2, min(1+e2, max1_len_rootss))]
    #def __call__(sf, gs, /):
    def iter_call_gs(sf, gs, /):
        'gs/[int{abs<-[1..<N]}] -> Iter ((unknown/..., (x0__but2, g_is_g2)) | (is_composite/True, <0:witness4composite|1:nontrivial_factor>)) # primality_test_of_Miller_Rabin'
        for g in gs:
            r = sf.call_g(g)
            yield r
            (case, payload) = r
            if not case is ...:
                break
        return
    def call_g(sf, g, /):
        'g/int{abs<-[1..<N]} -> ((unknown/..., (x0__but2, g_is_g2)) | (is_composite/True, <0:witness4composite|1:nontrivial_factor>)) # primality_test_of_Miller_Rabin'
        try:
            r = sf._call_g_(g)
        except _ToReturn as exc:
            [r] = exc.args
        return r
    def _call_g_(sf, g, /):
        (e2, fts, es, N, max1_len_rootss) = sf.args
        rootss = sf.rootss
        assert 0 < abs(g) < N
        if N%g == 0:
            # since now using direct_case4prime_bases
            #   SHOULD detect prime factor here
            ft4m = g
            return (True, (1, ft4m))

        L = len(fts)
        Nmm = rootss[1][0]

        _pow_ = _pow_ne_(N, 1, _ToReturn((..., (1,False))))
            # (x0__but2, g_is_g2)
        x0__but2 = _mk_x0_(_pow_, fts, es, g)
        _pow_ = _pow_ne_(N, 1, _ToReturn((..., (x0__but2,False))))
        x1__but2 = _mk_x1_(_pow_, fts, [1]*L, x0__but2)
        _pow_ = None

        xs = []
        x = x1__but2
        if x == 1:
            pass
        #to simplify witness4composite____validate_result5is_composite_ex__Nmm_
            # ==>> sqrt_mod_(N; +1) besides {+1,-1} will be used to find out nontrivial_factor
        #elif x == Nmm:
        #    xs.append(Nmm)
        #    pass
        else:
            #to simplify witness4composite____validate_result5is_composite_ex__Nmm_
                #for _ in range(e2-1):
            for _ in range(e2):
                xs.append(x)
                x = _int_pow(x, 2, N)
                #to simplify witness4composite____validate_result5is_composite_ex__Nmm_
                #if x == Nmm:
                #    xs.append(Nmm)
                    # [xs[-1] == Nmm]
                #    break
                if x == 1:
                    # [xs[-1] =!= Nmm]
                    break
            else:
                if 0:
                    #to simplify witness4composite____validate_result5is_composite_ex__Nmm_
                    assert not x == Nmm
                    # [1 =!= x =!= Nmm][0 <= x < N]
                    # [1 =!= x < Nmm]
                #####
                # [x =!= 1][0 <= x < N]

                # [1 =!= x < N]
                if x == 0:
                    ft4m = gcd(g, N)
                    if ft4m == N: raise ValueError
                    assert 1 < ft4m < N
                    assert N %ft4m == 0
                    return (True, (1,ft4m))
                # [1 < x < N]
                assert 2 <= x < N
                #assert 2 <= abs(g) < N
                assert 1 <= abs(g) < N
                witness4composite = g
                return (True, (0,witness4composite))
            pass
        #
        xs.append(1)
        xs.reverse() # [1,...]
        del xs[max1_len_rootss:]
        r = sf._update_roots(xs)
        if not r is ...:
            return r
        if 0:
            #bug:
            g_is_g2 = len(xs) > 1 and (xs[1]==Nmm)
            if not len(xs) == 1:
                assert g_is_g2
        else:
            g_is_g2 = len(xs) == 1+e2 and (xs[1]==Nmm)

        return (..., (x0__but2, g_is_g2))
    def _update_roots(sf, xs, /):
        '-> emay result'
        def f(N, xx, x, rts, /):
            assert x not in rts
            for y in rts:
                yy = _int_pow(y, 2, N)
                if yy == xx:
                    break
            else:
                raise 000
            ft4m = gcd(x+y, N)
            assert 1 < ft4m < N
            assert N %ft4m == 0
            return (True, (1,ft4m))

        (e2, fts, es, N, max1_len_rootss) = sf.args
        rootss = sf.rootss
        assert xs, xs
        assert xs[0] == 1
        begin = min(len(xs), len(rootss))
        end = min(len(xs), max1_len_rootss)
        for i in reversed(range(0, begin)):
            if xs[i] in rootss[i]:
                if not i == begin-1:
                    assert not xs[i+1] in rootss[i+1]
                    return f(N, xs[i], xs[i+1], rootss[i+1])

                break

        # extend rootss
        for i in range(begin, end):
            x = xs[i]
            rs = {rt*x %N for rs_ in rootss for rt in rs_}
            rootss.append(rs)
        return ...

class _detect_primality__Nmm:
    def __init__(sf, e2, fts, es, N, using_gcd, /):
        '[using_gcd is True] <==> [fts are all prime]'
        assert e2 >= 1
        assert N >= 3
        assert N&1 == 1
        _fts = [2, *fts]
        _es = [e2, *es]
        L = len(_fts)
        j2g = [None]*L
        js = [*range(L)]
        sf.args = (e2, fts, es, N, using_gcd, _fts, _es)
        sf._set_new_state(js, j2g)
    def _set_new_state(sf, js, j2g, /):
        sf.state = js, j2g
        (e2, fts, es, N, using_gcd, _fts, _es) = sf.args

        L = len(_fts)
        cs = list_complement_idc_(L, js)
        fts4known_g = list_values__via_idc_(cs, _fts)
        es4known_g = list_values__via_idc_(cs, _es)

        fts4unknown_g = list_values__via_idc_(js, _fts)
        es4unknown_g = list_values__via_idc_(js, _es)

        sf.state_ex = (cs, fts4known_g, es4known_g, fts4unknown_g, es4unknown_g)

    #def __call__(sf, gs, /):
    def iter_call_gs(sf, gs, may_exss, /):
        'gs/[int{abs<-[1..<N]}] -> Iter ((is_prime/False, (delta_js, j2g)) | (unknown/..., (delta_js, j2may_g)) | (is_composite/True, <0:witness4composite|1:nontrivial_factor>))'
        for g, may_exs in zip(gs, may_exss):
            r = sf.call_g(g, may_exs)
            yield r
            (case, payload) = r
            if not case is ...:
                break
        return

    def call_g(sf, g, may_exs, /):
        'g/int{abs<-[1..<N]} -> ((is_prime/False, (delta_js, j2g)) | (unknown/..., (delta_js, j2may_g)) | (is_composite/True, <0:witness4composite|1:nontrivial_factor>))'
        try:
            r = sf._call_g_(g, may_exs)
        except _ToReturn as exc:
            [r] = exc.args
        (case, payload) = r
        if case is ...:
            (delta_js, j2g) = payload
            js, j2g = sf.state
            if delta_js:
                for j in delta_js:
                    j2g[j] = g
                js = [j for j in js if j2g[j] is None]
                sf._set_new_state(js, j2g)
            if not js:
                case = False
                r = case, (delta_js, j2g)
                # [N is prime]
            pass
        return r

bug@_detect_primality__Nmm._call_g_
contains bug since output  composite least partial_pseudo_primitive_root
    def _call_g_(sf, g, may_exs, /):
        'g/int{abs<-[1..<N]} -> ((unknown/..., (delta_js, j2may_g)) | (is_composite/True, <0:witness4composite|1:nontrivial_factor>))'
        (e2, fts, es, N, using_gcd, _fts, _es) = sf.args
        js, j2g = sf.state
        assert 0 < abs(g) < N

        delta_js = []
        if not js:
            return (..., (delta_js, j2g))

        (cs, fts4known_g, es4known_g, fts4unknown_g, es4unknown_g) = sf.state_ex
        _pow_ = _pow_ne_(N, 1, _ToReturn((..., (delta_js, j2g))))
        if not may_exs is None:
            (x0__but2, g_is_g2) = may_exs
            #if x0__but2 == 1:
            if fts4unknown_g == [2]:
                if g_is_g2:
                    assert not x0__but2 == 1
                    assert js == [0]
                    #bug:delta_js.append(2)
                    delta_js.append(0)
                    pass
                return (..., (delta_js, j2g))
        else:
            x0__but2 = _mk_x0_(_pow_, fts, es, g)
        x0__but2
        x0 = _mk_x0_(_pow_, [2], [e2], x0__but2)

        x04unknown_g = _mk_x1_(_pow_, fts4known_g, [1]*len(fts4known_g), x0)

        _pow_ = _pow_ne_(N, None, None)
        it = iter_pow_II1_except_one_(_pow_, fts4unknown_g, x04unknown_g)
        for i, x in enumerate(it):
            #may have [x == 1]
            if x == 1:
                continue

            if i==0:
                j = js[i]
                _ft = _fts[j]
                #_e = _es[j]
                if not _int_pow(x, _ft, N) == 1:
                    # [1 =!= x < N]
                    if x == 0:
                        ft4m = gcd(g, N)
                        if ft4m == N: raise ValueError
                        assert 1 < ft4m < N
                        assert N %ft4m == 0
                        return (True, (1,ft4m))
                    # [1 < x < N]
                    assert 2 <= x < N
                    #assert 2 <= abs(g) < N
                    assert 1 <= abs(g) < N
                    witness4composite = g
                    return (True, (0,witness4composite))
                pass
            #####
            if using_gcd:
                if not (ft4m := gcd(x-1, N)) == 1:
                    if not 1 < ft4m < N: raise 000
                    assert N %ft4m == 0
                    return (True, (1,ft4m))
            #####
            j = js[i]
            delta_js.append(j)
        return (..., (delta_js, j2g))

#_detect_compositeness__Nmm(e2, fts, es, N, max1_len_rootss)
#_detect_primality__Nmm(e2, fts, es, N, using_gcd)
validate_primality__Nmm_
def N2num_prime_bases__ERH(N, /):
    '-> 2*floor_log2(N)**2 # >= # ERH => 2*ln(n)**2'
    #NOTE:原文上限用于 [2..<2*ln(n)**2] 并非 素数；这里 用作 PRIMES[:num_prime_bases]
    return 2*floor_log2(N)**2
def N2num_prime_bases__heuristically(N, /):
    '-> floor_log2(N)*max(1, floor_log2(floor_log2(N))) # ~= log2(n)*lnln(n)'
    #NOTE:原文上限用于 [2..<log2(n)*lnln(n)] 并非 素数；这里 用作 PRIMES[:num_prime_bases]
    flbN = floor_log2(N)
    flb_flbN = floor_log2(flbN)
    return flbN*max(1, flb_flbN)
def N2num_prime_bases__tiny__one_plus_2floor_log2_P(N, /):
    '-> (1+2*floor_log2(N)) #one_plus_2floor_log2_P'
    flbN = floor_log2(N)
    return 1+2*flbN
assert floor_log2(3) == 1
assert floor_log2(1) == 0
assert N2num_prime_bases__ERH(3) == 2
assert N2num_prime_bases__heuristically(3) == 1
assert N2num_prime_bases__tiny__one_plus_2floor_log2_P(3) == 3

assert floor_log2(5) == 2
assert floor_log2(2) == 1
assert N2num_prime_bases__ERH(5) == 8
assert N2num_prime_bases__heuristically(5) == 2
assert N2num_prime_bases__tiny__one_plus_2floor_log2_P(5) == 5

assert N2num_prime_bases__heuristically(7) == 2

assert floor_log2(16) == 4
assert floor_log2(4) == 2
assert floor_log2(256-1) == 7
assert floor_log2(8-1) == 2
assert floor_log2(256) == 8
assert floor_log2(8) == 3
assert N2num_prime_bases__ERH(256) == 128
assert N2num_prime_bases__heuristically(256) == 24
assert N2num_prime_bases__tiny__one_plus_2floor_log2_P(256) == 17

assert prime_gen.get_or_mk_lazy_prime_seq_() is prime_gen() is prime_gen.get_or_mk_lazy_prime_seq_() is prime_gen()
def iter_detect_primality__Nmm_(e2, fts, es, Bs, case4prime_bases, N2max1_len_rootss=None, /, *, using_nonprime_gs4detect_primality, reject_early_if_cannot_conform_primality):
    r'''
    -> Iter ((is_prime/False, (delta_js, j2g)) | (unknown/..., (delta_js, j2may_g)) | (is_composite/True, <0:witness4composite|1:nontrivial_factor>))

    [@[ft :<- fts] -> [[ft%2==1][ft>=3]]]
    [Bs :: [pint]{len=L}][@[i :<- [0..<L]] -> @[p4ft :<- all_prime_factors_of_(fts[i])] -> [p4ft >= Bs[i]]]


    '''#'''
    for r in _iter_detect_primality__Nmm_(e2, fts, es, Bs, case4prime_bases, N2max1_len_rootss, using_nonprime_gs4detect_primality=using_nonprime_gs4detect_primality, reject_early_if_cannot_conform_primality=reject_early_if_cannot_conform_primality):
        yield r
        (case, payload) = r
        if not case is ...:
            return
def _iter_detect_primality__Nmm_(e2, fts, es, Bs, case4prime_bases, N2max1_len_rootss, /, *, using_nonprime_gs4detect_primality, reject_early_if_cannot_conform_primality):
    assert len(fts) ==  len(es) ==  len(Bs)
    L = len(fts)
    assert all(ft&1 == 1 for ft in fts)
    assert all(ft >= 3 for ft in fts)
    assert all(B >= 3 for B in Bs)
    assert all(ft >= B for ft, B in zip(fts, Bs))
    assert e2 >= 0
    assert e2 >= 1 or L==0
    if e2 == 0:
        if not L == 0:
            is_composite = True
            ft4m = 2
            yield (is_composite, (1,ft4m))
            return
        N = 2
        is_composite = False
        #j2g = [1]
        j2g = [] #e2==0
        yield (is_composite, ([], j2g))
        return

    assert e2 >= 1


    js = [i for i in range(L) if fts[i] == Bs[i]]
    using_gcd = len(js) < L

    N = None
    must_be_composite = False
    cannot_conform_primality = False
    if using_gcd:
        assert L > 0
        try:
            (must_be_composite, N) = _ex_check_setting4validate_primality__Nmm__partial_factorization_(e2, fts, es, Bs, js)
        except ValidateFail__bad_setting__cannot_conform_primality:
            cannot_conform_primality = True
            pass
        except ValidateFail__bad_setting__eF_eR_not_coprime:
            raise DetectPrimalityFail__bad_setting
        except ValidateFail__nonprime__nontrivial_factor as exc:
            [ft4m] = exc.args
            is_composite = True
            yield (is_composite, (1,ft4m))
            return
        else:
            pass
    else:
        pass
    cannot_conform_primality
    must_be_composite
    assert not (cannot_conform_primality and must_be_composite)
    if cannot_conform_primality and reject_early_if_cannot_conform_primality:
        raise DetectPrimalityFail__bad_setting__cannot_conform_primality

    if N is None:
        N = 1 +(II__ft_e_pairs_(zip(fts, es)) << e2)

    assert N >= 3
    num_prime_bases = _calc_num_prime_bases(case4prime_bases, N)
    if N2max1_len_rootss is None:
        # total num roots <= 2**(max1_len_rootss-1)
        if 1:
            max1_len_rootss = 3+floor_log2(num_prime_bases)
            ######################
            #!!!!!!not bug!!!!!!!
            # space = O(2**max1_len_rootss) = O(8*num_prime_bases) # ~= O(floor_log2(N)**2)
            ######################
            #??????????????????????
            #???#bug:space&time-consuming
            #???# space = O(2**max1_len_rootss)
            #???# 这个费时又导致手机死机的bug 是 对照 seed/math/primality_proving__plain.py 的 输出(耗时极少！) 发现的: 存在大量 witness4composite=2 @out@primality_proving__plain 对应于 nontrivial_factor=成千上万的大因子 @out@primality_proving(this-module)，估计是 max1_len_rootss 提前于『witness4composite=2』发现的因子，只能是 因为max1_len_rootss 大很多！
            #??????????????????????
        else:
            max1_len_rootss = 3+floor_log2(1+floor_log2(num_prime_bases))
    else:
        max1_len_rootss = N2max1_len_rootss(N)
    max1_len_rootss = max(3, max1_len_rootss)

    lazy_prime_seq = prime_gen.get_or_mk_lazy_prime_seq_()
        # hold weakref
    #gs = _list_prime_bases4N(num_prime_bases, N)
    #   why using iter_gs_()?
    #       since floor_log2(N)**2 is too big...

    def iter_gs_():
        gs = _iter_prime_bases4N(num_prime_bases, N)
        return gs

    def iter_gaps_():
        if not using_nonprime_gs4detect_primality:
            gaps = ''
        else:
            gs = iter_gs_()
            gaps = iter_ints_in_gaps_(gs)
        return iter(gaps)

    N, max1_len_rootss, using_gcd
    dc = _detect_compositeness__Nmm(e2, fts, es, N, max1_len_rootss)
    #if cannot_conform_primality:
    if cannot_conform_primality or must_be_composite:
        # _detect_compositeness__Nmm only
        #   since cannot conform primality
        for r in dc.iter_call_gs(iter_gs_()):
            is_composite = r[0]
            if is_composite is ...:
                pass
            elif is_composite is True:
                yield r
                return
            else:
                raise 000
        if must_be_composite:
            assert not cannot_conform_primality
            raise DetectPrimalityFail__bad_setting__too_few_num_prime_bases
        assert cannot_conform_primality
        raise DetectPrimalityFail__bad_setting__cannot_conform_primality
        pass
    else:
        dc
        dp = _detect_primality__Nmm(e2, fts, es, N, using_gcd)
        gaps = iter_gaps_()

        #####
        #sfs = dc, dp
        for g in iter_gs_():
            r = dc.call_g(g)
            (case, payload) = r
            if not case is ...:
                assert case is True
                yield r
                return
            may_exs = (x0__but2, g_is_g2) = payload

            # dc MUST BE before dp
            r = dp.call_g(g, may_exs)
            yield r
                # will stop by outer func if not case==...

bug@_detect_primality__Nmm._call_g_
contains bug since output  composite least partial_pseudo_primitive_root
            #一对一 的 配比方案
            #   一素数g用于检测合数/素数，配比 一合数g用于检测素数
            #   见__doc__:(23, None) #伪output5iter_odd_primes__one_prime_per_bit_length_
            #       即:即使是2*lbN**2个素数 也无法替代 [2..<2*lbN**2]个正整数
            #
            ##这一改动，效果惊人！
            #   原先『先用完所有素数g再用合数g』两百多比特的素数 需要 两分钟 # 见__doc__:286 117.6秒
            #   一对一 之后 两百多比特的素数，平均1秒；三百多比特的素数，平均2秒
            #   可见，素数g用作本原根 相当糟糕
            for g in gaps:
                r = dp.call_g(g, None)
                yield r
                    # will stop by outer func if not case==...
                break

        for g in gaps:
            r = dp.call_g(g, None)
            yield r
                # will stop by outer func if not case==...

        raise DetectPrimalityFail__bad_setting__too_few_num_prime_bases
        pass
    raise 000
#end-def iter_detect_primality__Nmm_(e2, fts, es, Bs, case4prime_bases, N2max1_len_rootss=None, /, *, using_nonprime_gs4detect_primality, reject_early_if_cannot_conform_primality):
def _iter_detect_primality__Nmm__ver2_(fts, es, Bs, remain_ft, case4prime_bases, N2max1_len_rootss, /, *, using_nonprime_gs4detect_primality, reject_early_if_cannot_conform_primality, try_reduce_len):
    .TODO
    #neednot [are_pairwise_coprime(fts)]
    try:
        case, payload = _ex_check_setting4validate_primality__Nmm__partial_factorization__ver2_(fts, es, Bs, remain_ft, detect_complete_factorization__vs__try_reduce_len=False)
    except ValidateFail__nonprime__nontrivial_factor:


_nm2N2num_prime_bases = (dict(
    N2num_prime_bases__ERH=N2num_prime_bases__ERH
        ,ERH=N2num_prime_bases__ERH
        ,lbN_lbN_2=N2num_prime_bases__ERH
    ,N2num_prime_bases__heuristically=N2num_prime_bases__heuristically
        ,lbN_lblbN=N2num_prime_bases__heuristically
    ,N2num_prime_bases__tiny__one_plus_2floor_log2_P=N2num_prime_bases__tiny__one_plus_2floor_log2_P
        ,one_plus_2floor_log2_P=N2num_prime_bases__tiny__one_plus_2floor_log2_P
        ,plus1_2lbN=N2num_prime_bases__tiny__one_plus_2floor_log2_P
        ,lbN_2__plus1=N2num_prime_bases__tiny__one_plus_2floor_log2_P
        ,tiny=N2num_prime_bases__tiny__one_plus_2floor_log2_P
    ))
#def _calc_num_prime_bases(N2num_prime_bases, N, /):
def _calc_num_prime_bases(case4prime_bases, N, /):
    assert N >= 3
    if callable(case4prime_bases):
        N2num_prime_bases = case4prime_bases
    elif type(case4prime_bases) is int:
        num_prime_bases = case4prime_bases
        assert num_prime_bases > 0
        N2num_prime_bases = lambda N:num_prime_bases
    elif type(case4prime_bases) is str:
        nm = case4prime_bases
        N2num_prime_bases = _nm2N2num_prime_bases[nm]
    else:
        raise 000
        N2num_prime_bases = ...
    num_prime_bases = N2num_prime_bases(N)
    num_prime_bases = max(1, num_prime_bases)
    return num_prime_bases
def _list_prime_bases4N(num_prime_bases, N, /):
    return [*_iter_prime_bases4N(num_prime_bases, N)]
def _iter_prime_bases4N(num_prime_bases, N, /):
    assert N >= 3
    halfN = N // 2
    prime_bases = islice(iter(prime_gen.get_or_mk_lazy_prime_seq_()), num_prime_bases)
    #for i, g in enumerate(prime_bases):
    for g in prime_bases:
        yield g
        if g > halfN:
            #Note: [N==3][g==2 > 1==N//2]
            break
    return
def validate_result5is_composite_ex__Nmm_(N, r, /):
    check_int_ge(2, N)

    case, payload = r
    if case is ...:
        (e2, fts, es, Bs, prime_bases, may__j2may_g) = payload
        cannot_conform_primality = may__j2may_g is None
        pass
    elif case is False:
        if not (N==2) is (payload is None): raise ValidateFail
        if (payload is None):
            return
        (e2, fts, es, Bs, g2, gs) = payload
        try:
            validate_primality__Nmm_(e2, fts, es, Bs, g2, gs)
        except ValidateFail as exc:
            if exc.args:
                raise
            raise type(exc)(N, r)
    elif case is True:
        _01, _x = payload
        check_uint_lt(2, _01)
        if not (N&1 == 1): raise ValidateFail(N, r)
        if _01 == 0:
            witness4composite = _x
            check_int_ge_lt(1, N, abs(witness4composite))
            if not (pw := _int_pow(witness4composite, N-1, N)) > 1: raise ValidateFail(N, r, pw)
                #goto:simplify:witness4composite____validate_result5is_composite_ex__Nmm_
                    # sqrt_mod_(N; +1) besides {+1,-1} will be used to find out nontrivial_factor
        elif _01 == 1:
            nontrivial_factor = _x
            check_int_ge_lt(2, N, nontrivial_factor)
            if not N %nontrivial_factor == 0: raise ValidateFail(N, r)
        else:
            raise 000
        return r
    else:
        raise 000
    pass



assert (1, 1) == factor_pint_out_power_of_base_(2, 2)
_all_cases4prime_bases = [N2num_prime_bases__tiny__one_plus_2floor_log2_P, N2num_prime_bases__heuristically, N2num_prime_bases__ERH]
def is_composite_ex__Nmm_(N, /, *, case4prime_bases=N2num_prime_bases__tiny__one_plus_2floor_log2_P, using_nonprime_gs4detect_primality=False, tribool=False, validate=True, direct_case4prime_bases=N2num_prime_bases__tiny__one_plus_2floor_log2_P, reject_early_if_cannot_conform_primality=False):
    r'''[[[
    -> ((True, ((1,nontrivial_factor<N>) | (0,witness4composite))) | (False, may (e2, fts, es, Bs, g2, gs)) | ((..., (e2, fts, es, Bs, prime_bases, may__j2may_g)) if tribool else ^DetectPrimalityFail))

    ===
    emay case4prime_bases
        allow [case4prime_bases := ...]

    ===
    direct_case4prime_bases:
        why?
            since floor_log2(N)**2 is too big...

    ===

    #]]]'''#'''
    lazy_prime_seq = prime_gen.get_or_mk_lazy_prime_seq_()
        # hold weakref
    original_case4prime_bases = case4prime_bases
    original_tribool = tribool
    original_using_nonprime_gs4detect_primality = using_nonprime_gs4detect_primality

    if original_case4prime_bases is ...:
        all_cases4prime_bases = _all_cases4prime_bases
    else:
        all_cases4prime_bases = [original_case4prime_bases]

    #bug:for case4prime_bases in _all_cases4prime_bases:
    #   ==>> [is_last===False]
    #   ==>> [tribool===True]
    #   ==>> [using_nonprime_gs4detect_primality===False]
    for case4prime_bases in all_cases4prime_bases:
        is_last = case4prime_bases is all_cases4prime_bases[-1]
        tribool = original_tribool if is_last else True
        using_nonprime_gs4detect_primality = original_using_nonprime_gs4detect_primality if is_last else False
        r = _is_composite_ex__Nmm_(N, case4prime_bases=case4prime_bases, using_nonprime_gs4detect_primality=using_nonprime_gs4detect_primality, tribool=tribool, direct_case4prime_bases=direct_case4prime_bases, reject_early_if_cannot_conform_primality=reject_early_if_cannot_conform_primality)
        case, payload = r
        if not case is ...:
            break
        (e2, fts, es, Bs, prime_bases, may__j2may_g) = payload
        cannot_conform_primality = may__j2may_g is None
        if cannot_conform_primality:
            if original_tribool:
                break
            raise DetectPrimalityFail__bad_setting__cannot_conform_primality
        if (case4prime_bases is N2num_prime_bases__ERH or _calc_num_prime_bases(case4prime_bases, N) >= N2num_prime_bases__ERH(N)) and (using_nonprime_gs4detect_primality is True):
            #[:detect_ERH_counterexample]:here
            print_err(f'???ERH???:counterexample: {N}')
        pass

    else:
        assert is_last
    r
    if validate:
        validate_result5is_composite_ex__Nmm_(N, r)
    return r
def _is_composite_ex__Nmm_(N, /, *, case4prime_bases, using_nonprime_gs4detect_primality, tribool, direct_case4prime_bases, reject_early_if_cannot_conform_primality):
    check_int_ge(2, N)
    if N == 2:
        return (False, None)

    assert N >= 3
    if N&1 == 0:
        ft4m = 2
        return (True, (1,ft4m))
    assert N&1 == 1
    # [N >= 1][N&1 == 1]

    num_prime_bases = _calc_num_prime_bases(case4prime_bases, N)
    num_direct_prime_bases = _calc_num_prime_bases(direct_case4prime_bases, N)

    prime_bases = _list_prime_bases4N(num_direct_prime_bases, N)
    for p in prime_bases:
        if p**2 > N:
            #return (False, None)
            break
        if N%p == 0:
            assert 1 < p < N
            return (True, (1,p))
    else:
        pass


    Nmm = N-1
    eR = Nmm
    eF = 1
    fts = []
    es = []
    p = ...
    assert prime_bases
    assert prime_bases[0] == 2
    for p in prime_bases:
        (e4p, eR) = factor_pint_out_power_of_base_(p, eR)
        B4eR = 3 if p==2 else p+2
        if e4p:
            eF *= p**e4p
            fts.append(p)
            es.append(e4p)
            if eF > eR:
                e5B = eF*B4eR
                # [if below check pass] => [[(e5B+1)**2 > m] -> [is_prime_(m)]]
                if (sq := (e5B+1)**2) > N:
                    break
                elif sq == N:
                    return (True, (1,(e5B+1)))
    B4eR
    eF, eR
    fts, es
    assert eR == 1 or eR >= B4eR, ((eR, B4eR), (N, Nmm, eR, eF, fts, es))
    assert B4eR&1 == 1
    assert fts
    assert fts[0] == 2
    e2 = es[0]
    del fts[0]
    del es[0]
    Bs = [*fts]
    if eR == 1:
        pass
    else:
        fts.append(eR)
        es.append(1)
        Bs.append(B4eR)
    e2, fts, es, Bs
    #if 0b01:print((N, prime_bases, eR, eF, e2, fts, es, Bs))

    #validate_primality__Nmm_(e2, fts, es, Bs, g2, gs)
    #iter_detect_primality__Nmm_(e2, fts, es, Bs, case4prime_bases, N2max1_len_rootss=None, /, *, using_nonprime_gs4detect_primality, reject_early_if_cannot_conform_primality):
    it = iter_detect_primality__Nmm_(e2, fts, es, Bs, num_prime_bases, using_nonprime_gs4detect_primality=using_nonprime_gs4detect_primality, reject_early_if_cannot_conform_primality=reject_early_if_cannot_conform_primality)
    if tribool:
        tmay_cannot_conform_primality = []
        tmay_exc_type = []
        def f(it, /):
            try:
                yield from it
            except DetectPrimalityFail__bad_setting__cannot_conform_primality:
                T = DetectPrimalityFail__bad_setting__cannot_conform_primality
                r = True
            except DetectPrimalityFail__bad_setting__too_few_num_prime_bases:
                T = DetectPrimalityFail__bad_setting__too_few_num_prime_bases
                r = False
            except DetectPrimalityFail__bad_setting:
                raise 000
            else:
                return
            tmay_cannot_conform_primality.append(r)
            tmay_exc_type.append(T)
            return
            #
        it = f(it)
    r = None
    for r in it:
        pass
    assert (r is None) is (tribool and tmay_cannot_conform_primality == [True])
    if r is None:
        assert tribool
        [cannot_conform_primality] = tmay_cannot_conform_primality
        assert cannot_conform_primality
        may__j2may_g = None
        return (..., (e2, fts, es, Bs, prime_bases, may__j2may_g))

    case, payload = r
    if case is ...:
        (delta_js, j2may_g) = payload
        assert tribool
        [cannot_conform_primality] = tmay_cannot_conform_primality
        assert not cannot_conform_primality
        may__j2may_g = j2may_g
        return (..., (e2, fts, es, Bs, prime_bases, may__j2may_g))
        raise DetectPrimalityFail__bad_setting
    elif case is False:
        (delta_js, j2g) = payload
        [g2, *gs] = j2g
        return (False, (e2, fts, es, Bs, g2, gs))
    elif case is True:
        return r
    else:
        raise 000
    pass
#end-def is_composite_ex__Nmm_(N, /, *, case4prime_bases=N2num_prime_bases__tiny__one_plus_2floor_log2_P, using_nonprime_gs4detect_primality=False, tribool=False, validate=True):
def is_composite__Nmm_(N, /, *, tribool=False, quadbool=False, **kwds):
    '-> ((is_composite/bool | ^DetectPrimalityFail) if not tribool else (emay bool) if not quadbool else (bool|type-DetectPrimalityFail__bad_setting__cannot_conform_primality|type-DetectPrimalityFail__bad_setting__too_few_num_prime_bases))'
    if quadbool:
        tribool = quadbool = True

    r = is_composite_ex__Nmm_(N, tribool=tribool, **kwds)
    case, payload = r
    if quadbool:
        if case is ...:
            (e2, fts, es, Bs, prime_bases, may__j2may_g) = payload
            case = DetectPrimalityFail__bad_setting__cannot_conform_primality if may__j2may_g is None else DetectPrimalityFail__bad_setting__too_few_num_prime_bases
    return case


def test_many4is_composite_ex__Nmm_(max1, /, **kwds4is_composite_ex__Nmm_):
    lazy_prime_seq = prime_gen.get_or_mk_lazy_prime_seq_()
        # hold weakref
    u2p2e4N = tabulate_may_factorization4uint_lt_(max1)
    for u, p2e4N in enumerate(u2p2e4N):
        if u < 2:
            pass
        else:
            N = u
            factorization4Nmm = prev_p2e4N
            is_prime = len(p2e4N) == 1 and [*p2e4N.values()] == [1] # == N in p2e4N
            is_composite = not is_prime
            test_one4is_composite_ex__Nmm_(N, is_composite, factorization4Nmm, **kwds4is_composite_ex__Nmm_)
        prev_p2e4N = p2e4N

def test_one4is_composite_ex__Nmm_(N, is_composite:bool, factorization4Nmm, /, **kwds4is_composite_ex__Nmm_):
    r = is_composite_ex__Nmm_(N, tribool=True, validate=True, **kwds4is_composite_ex__Nmm_)
    case, payload = r
    if case is ...:
        pass
    else:
        assert case is is_composite #:: bool


def _as_odd_e2_(odd_N_ge3, /):
    if not odd_N_ge3 >= 3: raise ValueError(odd_N_ge3)
    if not odd_N_ge3&1 == 1: raise ValueError(odd_N_ge3)
    (e2, odd) = factor_pint_out_power_of_base_(2, odd_N_ge3-1)
    return (odd, e2)

class OddInt__ge3__repr_by_lshift_odd_plus1(int):
    __slots__ = ()
    def __new__(cls, /, *args, **kwargs):
        sf = super(__class__, cls).__new__(cls, *args, **kwargs)
        u = int(sf)
        if not u >= 3: raise ValueError(u)
        if not u&1 == 1: raise ValueError(u)
        return sf
    def __repr__(sf, /):
        (odd, e2) = _as_odd_e2_(int(sf))
        s = f'{odd}<<{e2}^1'
        assert eval(s) == int(sf)
        return s


def continue4iter_odd_primes__one_prime_per_bit_length_(iopath, /, end=None, *, with_certificate=False, output_composite=False, output_as_OddInt__ge3__repr_by_lshift_odd_plus1=False, timing=True, **kwds4is_composite_ex__Nmm_):
    'see:iter_odd_primes__one_prime_per_bit_length_'
    output_composite = bool(output_composite)
    with_certificate = bool(with_certificate)
    if output_composite:
        with_certificate = True

    with open(iopath, 'r+t', encoding='ascii') as iofile:
        line = None
        for line in iofile:
            assert line.startswith('(')
            assert line.endswith(')\n')
            if not output_as_OddInt__ge3__repr_by_lshift_odd_plus1:
                if '^' in line:
                    output_as_OddInt__ge3__repr_by_lshift_odd_plus1 = True
            if not with_certificate:
                if line.count(',')==2:
                    with_certificate = True
            #####
            if with_certificate and not output_composite:
                # ([
                if line.count(',')==2 and not line.endswith('])\n'):
                    output_composite = True
            pass
        if line is None:
            begin = 2
            begin_odd4first_num_bits = 1
            #default:
            with_certificate
            output_composite
            output_as_OddInt__ge3__repr_by_lshift_odd_plus1
        else:
            t = eval(line)
            if len(t) == 2:
                num_bits, may_p = t
                if may_p is None:
                    raise NotImplementedError
                p = may_p

                begin = 1 + num_bits
                begin_odd4first_num_bits = 1
                with_certificate = False
                output_composite = False
            elif len(t) == 3:
                num_bits, N, certificate = t
                with_certificate = True
                if type(certificate) is int:
                    # composite
                    assert output_composite
                    (odd, e2) = _as_odd_e2_(N)
                    begin = num_bits
                    begin_odd4first_num_bits = 2 + odd
                elif type(certificate) is list:
                    # prime
                    begin = 1 + num_bits
                    begin_odd4first_num_bits = 1
                else:
                    raise 000
            else:
                raise 000
            begin
            begin_odd4first_num_bits
        begin
        begin_odd4first_num_bits
        with_certificate
        output_composite
        output_as_OddInt__ge3__repr_by_lshift_odd_plus1

        it = iter_odd_primes__one_prime_per_bit_length_(begin, end=end, timing=timing, output_as_OddInt__ge3__repr_by_lshift_odd_plus1=output_as_OddInt__ge3__repr_by_lshift_odd_plus1, with_certificate=with_certificate, output_composite=output_composite, begin_odd4first_num_bits=begin_odd4first_num_bits, **kwds4is_composite_ex__Nmm_)
        for t in it:
            print(t, file=iofile, flush=True)
    return
def _read_and_eval_per_line_(ipath, /):
    with open(ipath, 'rt', encoding='ascii') as ifile:
        yield from _eval_per_line_(ifile)
def _eval_per_line_(ifile, /):
    return map(eval, ifile)

def filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_(ipath, /, *, output_as_OddInt__ge3__repr_by_lshift_odd_plus1):
    # had_output_composite = True
    def iter_():
        return _read_and_eval_per_line_(ipath)
    for (num_bits, N, certificate) in iter_():
        if output_as_OddInt__ge3__repr_by_lshift_odd_plus1:
            N = OddInt__ge3__repr_by_lshift_odd_plus1(N)

        if type(certificate) is list:
            yield (num_bits, N, certificate)
def validate_output5iter_odd_primes__one_prime_per_bit_length_(ipath, /, *, to_validate_continuity, to_validate_certificate, had_output_composite):
    assert to_validate_continuity or to_validate_certificate

    def iter_():
        return _read_and_eval_per_line_(ipath)
    #####
    if to_validate_continuity:
        if had_output_composite:
            _num_bits = 2
            it = iter_odd_uints__Pocklington_Theorem_1914__factor_2s__bit_length_(_num_bits, 1)
            Nothing = object()
            for (num_bits, may_N, *tmay_certificate) in iter_():
                assert num_bits == _num_bits
                if may_N is None:
                    assert not tmay_certificate
                    assert next(it, Nothing) is Nothing
                    _num_bits += 1
                else:
                    (N, [certificate]) = may_N, tmay_certificate
                    (e2, odd, _N) = next(it)
                    assert N == _N
                    if type(certificate) is list:
                        _num_bits += 1

                if not num_bits == _num_bits:
                    it = iter_odd_uints__Pocklington_Theorem_1914__factor_2s__bit_length_(_num_bits, 1)
        else:
            for i, (num_bits, may_p, *tmay_certificate) in enumerate(iter_(), 2):
                #assert may_p is None or ... ...
                assert num_bits == i
    #####
    if to_validate_certificate:
        for (num_bits, N, certificate) in iter_():
            if not N.bit_length() == num_bits: raise TypeError
            validate_primality_certificate4two_dominanted_odd_int_(N, certificate)
    #####
    return
def validate_primality_certificate4two_dominanted_odd_int_(N, certificate, /):
    'primality_certificate4two_dominanted_odd_int:see:iter_odd_primes__Pocklington_Theorem_1914__factor_2s__bit_length_'
    if not type(certificate) in (int, list):raise TypeError

    check_int_ge(3, N)
    if not N&1 == 1:raise TypeError
    (odd, e2) = _as_odd_e2_(N)
    if not 1 <= odd < (1<<e2): raise TypeError
    #[N is two_dominanted_odd_int]

    if type(certificate) is list:
        partial_pseudo_primitive_roots = certificate
        if not 1 <= len(partial_pseudo_primitive_roots) <= 2:raise TypeError
        (odd, e2) = _as_odd_e2_(N)
        e2
        [g2, *gs] = partial_pseudo_primitive_roots
        if odd == 1:
            fts = []
            es = []
            Bs = []
            assert gs == []
        else:
            fts = [odd]
            es = [1]
            Bs = [3]
            assert len(gs) == 1
        payload = (e2, fts, es, Bs, g2, gs)
        is_composite = False
        #validate_primality__Nmm_(e2, fts, es, Bs, g2, gs)
    elif type(certificate) is int:
        is_composite = True
        if certificate < 0:
            witness4composite = -certificate
            payload = (0, witness4composite)
        else:
            nontrivial_factor = certificate
            payload = (1, nontrivial_factor)
        payload
    else:
        raise 000
    payload
    case = is_composite
    r = case, payload
    validate_result5is_composite_ex__Nmm_(N, r)
    return

def iter_odd_primes__one_prime_per_bit_length_(begin=2, /, end=None, *, timing=False, output_as_OddInt__ge3__repr_by_lshift_odd_plus1=False, with_certificate=False, output_composite=False, begin_odd4first_num_bits=1, **kwds4is_composite_ex__Nmm_):
    r'''
    + -> Iter (num_bits, None) if no prime@num_bits, no matter with_certificate,output_composite

    * -> Iter (num_bits, prime)
    * -> Iter (num_bits, prime, certificate) if with_certificate
    * -> Iter (num_bits, prime/composite, certificate) if output_composite
    ===
    primality_certificate4two_dominanted_odd_int
    certificate:see:iter_odd_primes__Pocklington_Theorem_1914__factor_2s__bit_length_
    '''#'''
    output_composite = bool(output_composite)
    with_certificate = bool(with_certificate)
    if output_composite:
        with_certificate = True


    _to_show_ = timing
    _show_hint_on_enter_=True

    lazy_prime_seq = prime_gen.get_or_mk_lazy_prime_seq_()
        # hold weakref
    begin = max(2, begin)
    ns = count_(begin) if end is None else range(begin, end)
    for num_bits in ns:
        if num_bits == begin:
            begin_odd = begin_odd4first_num_bits
        else:
            begin_odd = 1
        it = iter_odd_primes__Pocklington_Theorem_1914__factor_2s__bit_length_(num_bits, begin_odd, output_as_OddInt__ge3__repr_by_lshift_odd_plus1=output_as_OddInt__ge3__repr_by_lshift_odd_plus1, with_certificate=with_certificate, output_composite=output_composite, **kwds4is_composite_ex__Nmm_)
        with timer(prefix=f'{num_bits}...', _to_show_=_to_show_, _show_hint_on_enter_=_show_hint_on_enter_):
            for x in it:
                if type(x) is int:
                    N = x
                    t = (N,)
                    is_prime = True
                else:
                    N, certificate = x
                    t = x
                    is_prime = bool([int, list].index(type(certificate)))
                assert N.bit_length() == num_bits, (num_bits, N.bit_length())
                #yield (num_bits, N)
                #may_t = t
                yield (num_bits, *t)
                if is_prime:
                    break
            else:
                # no prime @num_bits

                #yield (num_bits, None)
                #may_t = None
                yield (num_bits, None)
            #yield (num_bits, may_t)
        #yield (num_bits, may_p)

def iter_odd_primes__Pocklington_Theorem_1914__factor_2s__bit_length_(num_bits, begin_odd=1, /, *, output_as_OddInt__ge3__repr_by_lshift_odd_plus1=False, with_certificate=False, output_composite=False, **kwds4is_composite_ex__Nmm_):
    r'''
    * -> Iter prime
    * -> Iter (prime, certificate) if with_certificate
    * -> Iter (prime/composite, certificate) if output_composite

    [N == (odd<<e2) +1]

    primality_certificate4two_dominanted_odd_int
    certificate:
        * [is_prime_(N)]:
            [certificate is partial_pseudo_primitive_roots]
            * [odd > 1]:
                gs = [g2, g4odd]
                ===hidden:
                fts = [2, odd]
                es = [e2, 1]
                Bs = [2, 3]
            * [odd == 1]:
                gs = [g2]
                ===hidden:
                fts = [2]
                es = [e2]
                Bs = [2]
        * [is_composite_(N)]:
            * [certificate is nontrivial_factor]
            * [certificate is (-witness4composite)]

    '''#'''
    output_composite = bool(output_composite)
    with_certificate = bool(with_certificate)
    if output_composite:
        with_certificate = True

    def mk_certificate4prime_(e2, odd, payload, /):
        if payload is None:
            # ==>> [N==2] _L
            raise 000
        (_e2, fts, es, Bs, g2, gs) = payload
        assert _e2 == e2
        fts = [2, *fts]
        es = [e2, *es]
        Bs = [2, *Bs]
        gs = [g2, *gs]
        if odd == 1:
            assert fts == [2]
            assert es == [e2]
            assert Bs == [2]
            assert gs == [g2]
        else:
            assert fts == [2, odd]
            assert es == [e2, 1]
            assert Bs == [2, 3]
            #assert gs == [g2, _]
            assert len(gs) == 2
        certificate = partial_pseudo_primitive_roots = gs
        return certificate
    def mk_certificate4composite_(payload, /):
        _01, _x = payload
        if _01 == 0:
            witness4composite = _x
            assert 1 < witness4composite < N
            certificate = -witness4composite
            assert certificate < 0
        elif _01 == 1:
            nontrivial_factor = _x
            assert 1 < nontrivial_factor < N
            certificate = nontrivial_factor
            assert certificate > 0
        else:
            raise 000
        return certificate
    ######################
    it = iter_odd_uints__Pocklington_Theorem_1914__factor_2s__bit_length_(num_bits, begin_odd)
    for (e2, odd, N) in it:
        if 0:
            case = is_composite__Nmm_(N, quadbool=True, **kwds4is_composite_ex__Nmm_)
            if case is DetectPrimalityFail__bad_setting__cannot_conform_primality:
                raise 000 #since 2**e2 > odd
        case, payload = is_composite_ex__Nmm_(N, reject_early_if_cannot_conform_primality=True, **kwds4is_composite_ex__Nmm_)
            # 『, quadbool=False』
            # TypeError: is_composite_ex__Nmm_() got an unexpected keyword argument 'quadbool'

        if output_as_OddInt__ge3__repr_by_lshift_odd_plus1:
            N = OddInt__ge3__repr_by_lshift_odd_plus1(N)

        if case is ...:
            (e2, fts, es, Bs, prime_bases, may__j2may_g) = payload
            cannot_conform_primality = may__j2may_g is None
            if cannot_conform_primality:
                raise 000 #since 2**e2 > odd
            if output_composite:
                raise DetectPrimalityFail__bad_setting__too_few_num_prime_bases
        elif case is False:
            # prime
            if not with_certificate:
                yield N
            else:
                certificate = mk_certificate4prime_(e2, odd, payload)
                yield N, certificate
        elif case is True:
            # composite
            if output_composite:
                certificate = mk_certificate4composite_(payload)
                yield N, certificate
        else:
            raise 000
    return
def iter_odd_uints__Pocklington_Theorem_1914__factor_2s__bit_length_(num_bits, begin_odd=1, /):
    assert begin_odd >= 1
    assert num_bits >= 2

    lazy_prime_seq = prime_gen.get_or_mk_lazy_prime_seq_()
        # hold weakref
    half = num_bits//2
    if not num_bits >= 2:raise ValueError
    if not 1 <= begin_odd < (1<<half):raise ValueError
    if not begin_odd&1 == 1:raise ValueError
    k0 = 1+floor_log2(begin_odd)
    #prev_end = 0 # if begin_odd==1
    prev_end = begin_odd ^ 1
    if begin_odd == 1:
        assert k0 == 1
        assert prev_end == 0
    assert prev_end&1 == 0
    for k in range(k0, half+1):
        begin = prev_end ^ 1
        end = 1<<k
        prev_end = end
        e2 = num_bits -k
        for odd in range(begin, end, 2):
            assert odd < (1<<e2)
            Nmm = odd << e2
            N = Nmm ^ 1
            yield (e2, odd, N)
    return

def _parse_data5doc(__doc__, begin_str, end_str, stop_prefix, /):
    s = __doc__
    _, _s = s.split(begin_str)
    _s_, _ = _s.split(end_str)
    lines = _s_.strip().split('\n')
    for i, line in enumerate(lines):
        if line.startswith(stop_prefix):
            del lines[i:]
            break
    lines
    return [*map(eval, lines)]
output5filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_ = _parse_data5doc(__doc__
    ,'===[output5filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_:begin]'
    ,'===[output5filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_:end]'
    ,'^'
    )
output5iter_odd_primes__one_prime_per_bit_length_ = _parse_data5doc(__doc__
    ,'===[output5iter_odd_primes__one_prime_per_bit_length_:begin]'
    ,'===[output5iter_odd_primes__one_prime_per_bit_length_:end]'
    ,'^'
    )
assert (__:=output5iter_odd_primes__one_prime_per_bit_length_) == [(num_bits, p) for num_bits, p, gs in output5filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_[:len(__)]]
_output_after_bug_fixed = _parse_data5doc(__doc__
    ,'===[output_after_bug_fixed:begin]'
    ,'===[output_after_bug_fixed:end]'
    ,'^'
    )
assert (__:=_output_after_bug_fixed) == output5iter_odd_primes__one_prime_per_bit_length_[:len(__)]

output5reformat_output5iter_odd_primes__one_prime_per_bit_length_ = _parse_data5doc(__doc__
    ,'===[output5reformat_output5iter_odd_primes__one_prime_per_bit_length_:begin]'
    ,'===[output5reformat_output5iter_odd_primes__one_prime_per_bit_length_:end]'
    ,'-'
    )
assert (__:=output5reformat_output5iter_odd_primes__one_prime_per_bit_length_) == output5iter_odd_primes__one_prime_per_bit_length_[:len(__)]
# output5iter_odd_primes__one_prime_per_bit_length_,output5reformat_output5iter_odd_primes__one_prime_per_bit_length_ are deprecated by output5filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_

def reformat_output5iter_odd_primes__one_prime_per_bit_length_(*, postscript=False):
    num_bits__prime__pairs = output5iter_odd_primes__one_prime_per_bit_length_
    if postscript:
        appendix = []
        prev_ratio = Fraction(1)
    for num_bits, p in num_bits__prime__pairs:
        (odd, e2) = _as_odd_e2_(p)
        s = f'({num_bits},{odd}<<{e2} ^1)'
        assert eval(s) == (num_bits, p)
        print(s)
        if postscript:
            ratio = Fraction(odd, num_bits)
            if prev_ratio < ratio:
                prev_ratio = ratio
                appendix.append(s)
    if postscript:
        print('---postscript:')
        for s in appendix:
            print(s)
def test4merge_partial_pseudo_primitive_roots_into_single_one(num_bits4begin=2):
    'partial_pseudo_primitive_roots since some fts are not prime'
    lazy_prime_seq = prime_gen.get_or_mk_lazy_prime_seq_()
        # hold weakref
    num_bits__prime__pairs = output5iter_odd_primes__one_prime_per_bit_length_
    for num_bits, p in num_bits__prime__pairs:
        if num_bits < num_bits4begin:
            continue

        print(f'({num_bits}, {p}', flush=True, end='')
        r = is_composite_ex__Nmm_(p, case4prime_bases=..., using_nonprime_gs4detect_primality=True, tribool=True, validate=True)
        case, payload = r
        # (False, may (e2, fts, es, Bs, g2, gs))
        # [p is old prime]
        if not case is False: raise 000
        if payload is None: raise 000
        print(f', ', flush=True, end='')
        (e2, fts, es, Bs, g2, gs) = payload
        ggg = merge_partial_pseudo_primitive_roots_into_single_one(p, fts, es, gs, e2_g2 = (e2, g2))
        print(f'{ggg}', flush=True, end='')

        r4ggg = case, (e2, fts, es, Bs, ggg, [ggg]*len(gs))
        validate_result5is_composite_ex__Nmm_(p, r4ggg)
        print(f')', flush=True)

output5test4merge_partial_pseudo_primitive_roots_into_single_one = _parse_data5doc(__doc__
    ,'===[output5test4merge_partial_pseudo_primitive_roots_into_single_one:begin]'
    ,'===[output5test4merge_partial_pseudo_primitive_roots_into_single_one:end]'
    ,'^'
    )
def test4try_optimize_reduce_pseudo_primitive_root_(**kwds):
    triples = output5test4merge_partial_pseudo_primitive_roots_into_single_one
    for (num_bits, p, ggg) in triples:
        ggg = try_optimize_reduce_pseudo_primitive_root_(p, p-1, ggg, **kwds)
        print((num_bits, p, ggg))


#optimize
#minimize
def try_optimize_reduce_pseudo_primitive_root_(modulus, exp, ggg, /, *, level, basic_guarantee=8, verbose=False):
    '[level==0] => [no optimize]'
    assert basic_guarantee > 0
    if level is None or level < 0:
        level = 0
    if level == 0:
        #no optimize
        return ggg
    total = min(exp, level*(basic_guarantee + floor_log2(exp)))
    s = range(2, exp) if exp&1==1 else range(3, exp, 2)
    coprimes = (t for t in s if gcd(t, exp)==1)
    coprimes = islice(coprimes, total)
    mmm = ggg
    prev_e = 0
    prev_hhh = 1
    delta_e2pow = {}
    for e in coprimes:
        if 0:
            hhh = pow(ggg, e, modulus)
        else:
            #hhh = pow(ggg, e-prev_e, modulus) *prev_hhh %modulus
            delta_e = e-prev_e
            if not delta_e in delta_e2pow:
                delta_e2pow[delta_e] = pow(ggg, delta_e, modulus)
            hhh = delta_e2pow[delta_e] *prev_hhh %modulus
            prev_e = e
            prev_hhh = hhh
        #
        if hhh < mmm:
            if verbose:
                print(f'{ggg}**{e} => {hhh}')
            mmm = hhh
        ###ggg = hhh
            #since now using cache
    return mmm
def merge_partial_pseudo_primitive_roots_into_single_one(modulus, fts, es, gs, /, *, e2_g2=None, level4optimize=0): #, try_optimize=False
    r'''
    [are_pairwise_coprime(fts)]
    [level4optimize==0] => [no optimize]

[[[modulus :: pint]
    [L :: uint][fts :: [int{>1}]{len=L}][es :: [pint]{len=L}][gs :: [int]{len=L}]
    [are_pairwise_coprime(fts)]
    [e5ft := II__ft_e_pairs_(zip(fts, es))]
    [@[i :<- [0..<L]] -> [(gs[i]**e5ft -1) %modulus == 0]]
    [@[i :<- [0..<L]] -> [(gs[i]**(e5ft///fts[i]) -1) %modulus =!= 0]]

    ###
    [ggg := II gs[i]**(e5ft///fts[i]**es[i]) {i :<- [0..<L]} %modulus]
    ###
    [g2js := inv__k2v_to_v2ks(dict(enumerate(gs)))]
    [hhh := II g**(e5ft///II fts[j]**es[j] {j :<- js}) {(g,js) :<- g2js.items()} %modulus]
  ] -> [
    ###
    [(ggg**e5ft -1) %modulus == 0]
    [@[i :<- [0..<L]] -> [(ggg**(e5ft///fts[i]) -1) %modulus =!= 0]]
    ###
    [(hhh**e5ft -1) %modulus == 0]
    [@[i :<- [0..<L]] -> [(hhh**(e5ft///fts[i]) -1) %modulus =!= 0]]
  ]
]
    '''#'''
    try_optimize = level4optimize > 0
    assert modulus > 0
    assert len(fts) ==  len(es) ==  len(gs)
    assert all(ft >= 2 for ft in fts)
    assert all(e >= 1 for e in es)
    if not e2_g2 is None:
        e2, g2 = e2_g2
        assert e2 >= 1
        #assert g2
        fts = [2, *fts]
        es = [e2, *es]
        gs = [g2, *gs]
    L = len(fts)
    if not are_pairwise_coprime(fts): raise ValueError

    if modulus == 1:
        assert L == 0
        hhh = 0
        return hhh
    N = modulus
    assert N >= 2
        # for _pow_ne_
    if L==0:
        assert [*gs] == [1]
        hhh = 1
        return hhh
    assert L > 0
        # for try_optimize, level4optimize


    g2js = inv__k2v_to_v2ks(gs, True, set_vs_list=True)
    _pow_ = _pow_ne_(N, 1, ValidateFail__order_mod__proper_factor)

    g_js_pairs = sorted(g2js.items(), key=lambda kv:kv[1][0])
    # [hhh := II g**(e5ft///II fts[j]**es[j] {j :<- js}) {(g,js) :<- g2js.items()} %modulus]
    #concave凹
    #convex凸
    convex_es4g = [II(fts[j]**es[j] for j in js) for g, js in g_js_pairs]
    apply_ = int.__mul__
    concave_es4g = iter_apply_commutative_operations_except_one_(apply_, convex_es4g, 1)
    pows = [_pow_(g, concave_e) for (g, js), concave_e in zip(g_js_pairs, concave_es4g)]
    hhh = II_mod(N, pows)
    if try_optimize:
        assert L > 0
        e5ft = concave_es4g[0]*convex_es4g[0]
        hhh = try_optimize_reduce_pseudo_primitive_root_(modulus, e5ft, hhh, level=level4optimize)
    return hhh



class _ToReturn(BaseException):pass
class Error(Exception):pass
class ValidateFail(Error):pass
class ValidateFail__order_mod_(ValidateFail):pass
class ValidateFail__order_mod__proper_factor(ValidateFail__order_mod_):pass
class ValidateFail__order_mod__not_order(ValidateFail__order_mod_):pass

class ValidateFail__nonprime(ValidateFail):pass
class ValidateFail__nonprime__nontrivial_factor(ValidateFail__nonprime):pass
class ValidateFail__bad_setting(ValidateFail):pass
class ValidateFail__bad_setting__eF_eR_not_coprime(ValidateFail):pass
class ValidateFail__bad_setting__cannot_conform_primality(ValidateFail__bad_setting):pass

class DetectPrimalityFail(Error):pass
class DetectPrimalityFail__bad_setting(DetectPrimalityFail):pass
class DetectPrimalityFail__bad_setting__cannot_conform_primality(DetectPrimalityFail__bad_setting):pass
class DetectPrimalityFail__bad_setting__too_few_num_prime_bases(DetectPrimalityFail__bad_setting):pass

is_composite_ex__Nmm_(5)




r"""[[[
old_version:
===
class ValidateFail__order_mod__not_corresponding_partial_primitive_root(ValidateFail__order_mod_):pass
class PrimalityFail(Error):pass
class PrimalityFail__is_prime_ex__Nmm_____assume_case(PrimalityFail):pass


def _eval_x0_(base, pe_pairs, M, /):
    '-> x0 | ^ValidateFail__order_mod__proper_factor'
    x = base
    for p, e in pe_pairs:
        for _ in range(e-1):
            x = pow(x, p, M)
            #if x in bads:
            if x == 1:
                raise ValidateFail__order_mod__proper_factor
            #if x > halfM: x -= M
    x0 = x
    return x0

def _II__factorization_(factorization, /, *, factorization_is_pe_pairs):
    if factorization_is_pe_pairs:
        pe_pairs = (factorization)
        m = II(p**e for p, e in pe_pairs)
    else:
        p2e = (factorization)
        m = II__p2e_(p2e)
    return m
def _mk_sorted_pe_pairs_(factorization, /, *, factorization_is_pe_pairs):
    if factorization_is_pe_pairs:
        pe_pairs = (factorization)
    else:
        p2e = (factorization)
        pe_pairs = (p2e.items())
    pe_pairs = sorted(pe_pairs)
    return pe_pairs

#def validate_order_mod_(M, factorization4phiM, primitive_root_mod_M, /):
def validate_order_mod_(modulus, factorization4order4base, base, /, *, factorization_is_pe_pairs=False, to_collect_info=False):
    '-> (None if not to_collect_info else xs4good) | ^ValidateFail__order_mod__proper_factor | ^ValidateFail__order_mod__not_order'
    assert not modulus == 0
    M = abs(modulus)
    B = base
    #Mmm = M-1
    #halfM = M//2
    #bads = (1, Mmm)
    pe_pairs = _mk_sorted_pe_pairs_(factorization4order4base, factorization_is_pe_pairs=factorization_is_pe_pairs)
    x0 = _eval_x0_(base, pe_pairs, M)
        # ^ValidateFail__order_mod__proper_factor
    def apply_(pe, x, /):
        p, e = pe
        x = pow(x, p, M)
        if x == 1:
            if not to_collect_info:
                raise ValidateFail__order_mod__proper_factor
        return x


    if to_collect_info:
        bad_idc = []
        good_idc = []
        xs4good = []

    for i, x in enumerate(iter_apply_commutative_operations_except_one_(apply_, pe_pairs, x0)):
        if i == 0:
            p0, e0 = pe_pairs[0]
            if not 1==pow(x, p0, M):
                raise ValidateFail__order_mod__not_order
        if not to_collect_info:
            if x == 1:
                raise ValidateFail__order_mod__proper_factor
        else:
            if x == 1:
                bad_idc.append(i)
            else:
                good_idc.append(i)
                xs4good.append(x)

    if to_collect_info:
        if bad_idc:
            raise ValidateFail__order_mod__proper_factor((bad_idc, good_idc, xs4good))

    if not pe_pairs:
        #if not base == 1:
        if not (base%M == 1):
            raise ValidateFail__order_mod__not_order

    if to_collect_info:
        return xs4good

#end-def validate_order_mod_(modulus, factorization4order4base, base, /):


def validate_primality__Pmm_(factorization4Pmm, primitive_root_mod_P, /, *, factorization_is_pe_pairs=False, using_p2partial_primitive_root=False):
    Pmm = _II__factorization_(factorization4Pmm, factorization_is_pe_pairs=factorization_is_pe_pairs)
    P = Pmm +1
    if not using_p2partial_primitive_root:
        modulus = P
        order4base = Pmm
        factorization4order4base = factorization4Pmm
        base = primitive_root_mod_P
        validate_order_mod_(modulus, factorization4order4base, base, factorization_is_pe_pairs=factorization_is_pe_pairs)
    else:
        p2partial_primitive_root = primitive_root_mod_P
        pe_pairs = _mk_sorted_pe_pairs_(factorization4Pmm, factorization_is_pe_pairs=factorization_is_pe_pairs)
        if not len(p2partial_primitive_root) == len(pe_pairs): raise ValueError

        if not p2partial_primitive_root.keys() == dict(pe_pairs).keys(): raise ValueError
        p2i = {p:i for i, (p,e) in enumerate(pe_pairs)}

        partial_primitive_root2ps = inv__k2v_to_v2ks(p2partial_primitive_root)
        for base, ps in partial_primitive_root2ps.items():
            js = [p2i[p] for p in ps]
            try:
                xs4good = validate_order_mod_(P, pe_pairs, base, factorization_is_pe_pairs=True, to_collect_info=True)
            except ValidateFail__order_mod__proper_factor as exc:
                [(bad_idc, good_idc, xs4good)] = exc.args
                if not {*js} <= {*good_idc}: raise ValidateFail__order_mod__not_corresponding_partial_primitive_root


class Case4is_prime__Nmm_(Enum):
    '#doc4Case4is_prime__Nmm_:goto'
    #assume__exists_prime_primitive_root_mod_P_lt_log2_P = auto()
    #assume__exist_prime_primitive_roots_of_P__and__prime_index_of_the_min_one_le_2floor_log2_P = auto()
del Case4is_prime__Nmm_
class Case4is_prime__Nmm____how_to_find_primitive_root(Enum):
    using_prime_base_as_primitive_root_candidate_only = auto()
    using_arbitrary_int_ge2_as_primitive_root_candidate = auto()
class Case4is_prime__Nmm____how_many_prime_bases_to_be_test(Enum):
    #using_1plus_2floor_log2_P_as_num_bases_to_be_test = auto()
    one_plus_2floor_log2_P = auto()
    one_plus_square_floor_log2_P = auto()
class ResultCase4is_prime__Nmm_(Enum):
    # is_prime =:
    # True:
    two = auto()
    primitive_root = auto()
    p2partial_primitive_root = auto()
    # True & [unfactored_part4Nmm > 1]:
    factored_part4Nmm_ge_sqrtN = auto()
    factored_part4Nmm_ge_cubic_rootN = auto()
    # False:
    factors = auto()
    witness4composite = auto()


default_case4num=Case4is_prime__Nmm____how_many_prime_bases_to_be_test.one_plus_2floor_log2_P
default_case4root=Case4is_prime__Nmm____how_to_find_primitive_root.using_prime_base_as_primitive_root_candidate_only
def is_prime__Nmm_(factorization4Nmm, /, *, tribool=False, **kwds4is_prime_ex__Nmm_):
    r = is_prime_ex__Nmm_(factorization4Nmm, raise__vs__emay=tribool, **kwds4is_prime_ex__Nmm_)
    if r is ...:
        return ...
    (is_prime, result_case, payload4result_case) = r
    return is_prime

def is_prime_ex__Nmm_(factorization4Nmm, /, *, factorization_is_pe_pairs=False, partial_primitive_roots__vs__primitive_root=False, case4num=default_case4num, case4root=default_case4root, raise__vs__emay=False, odd_coprime_nonprime_factor2prime_factor_lowbound4Nmm=None):
    '-> (is_prime/bool, result_case/ResultCase4is_prime__Nmm_, payload4result_case) | (... if raise__vs__emay else ^PrimalityFail__is_prime_ex__Nmm_____assume_case)'
    # view others/数学/整数分解/factorint.txt
    #       F1,R1,B1 ==>> odd_coprime_nonprime_factor2prime_factor_lowbound4Nmm
    #
    check_type_is(bool, partial_primitive_roots__vs__primitive_root)
    check_type_is(bool, raise__vs__emay)

    to_collect_partials = partial_primitive_roots__vs__primitive_root is False

    pe_pairs = _mk_sorted_pe_pairs_(factorization4Nmm, factorization_is_pe_pairs=factorization_is_pe_pairs)
    if not all(e >= 1 for p, e in pe_pairs): raise ValueError
    if not all(p >= 2 for p, e in pe_pairs): raise ValueError

    js4unfactored = set()
    if odd_coprime_nonprime_factor2prime_factor_lowbound4Nmm:
        if 2 in odd_coprime_nonprime_factor2prime_factor_lowbound4Nmm: raise ValueError
        p2i = {p:i for i, (p,e) in enumerate(pe_pairs)}
        for unfactored, min_p4unfactored in odd_coprime_nonprime_factor2prime_factor_lowbound4Nmm.items():
            if not unfactored in p2i: raise ValueError
            if not (unfactored&1 == 1): raise ValueError
            js4unfactored.add(p2i[unfactored])
        R1_2_B1 = odd_coprime_nonprime_factor2prime_factor_lowbound4Nmm
    else:
        js4unfactored
        pass
    true_pe_pairs = []
    false_pe_pairs = []
    for i, pe in enumerate(pe_pairs):
        if i in js4unfactored:
            false_pe_pairs.append(pe)
        else:
            true_pe_pairs.append(pe)

    #Nmm = _II__factorization_(factorization4Nmm, factorization_is_pe_pairs=factorization_is_pe_pairs)
    if 1:
        factored_part4Nmm = _II__factorization_(true_pe_pairs, factorization_is_pe_pairs=True)
            # F1
        unfactored_part4Nmm = _II__factorization_(false_pe_pairs, factorization_is_pe_pairs=True)
            # R1
        assert unfactored_part4Nmm&1 == 1
    Nmm = factored_part4Nmm * unfactored_part4Nmm
    assert Nmm >= 1
    N = Nmm +1
    assert N >= 2
    #if not factorization4Nmm.get(2,1-len(factorization4Nmm)) >= 1: raise ValueError
    if N == 2:
        return (True, ResultCase4is_prime__Nmm_.two, None)
    if not (N&1 == 1):
        return (False, ResultCase4is_prime__Nmm_.factors, [2])
    if not factorization4Nmm.get(2,-1) >= 1: raise 000


    if case4num is Case4is_prime__Nmm____how_many_prime_bases_to_be_test.one_plus_2floor_log2_P:
        max1_prime_index4base = 1+ 2*floor_log2(N)
    elif case4num is Case4is_prime__Nmm____how_many_prime_bases_to_be_test.one_plus_square_floor_log2_P:
        max1_prime_index4base = 1+ floor_log2(N)**2
    else:
        raise 000
    if case4root is Case4is_prime__Nmm____how_to_find_primitive_root.using_prime_base_as_primitive_root_candidate_only:
        def iter_candidate_primitive_root_between_(a, b, /):
            return;yield
    elif case4root is Case4is_prime__Nmm____how_to_find_primitive_root.using_arbitrary_int_ge2_as_primitive_root_candidate:
        def iter_candidate_primitive_root_between_(a, b, /):
            return iter(range(max(2,a), b))
    else:
        raise 000

    M = modulus = N

    PRIMES = prime_gen.get_or_mk_lazy_prime_seq_()
    primes = PRIMES[:max1_prime_index4base]
    halfN = N//2
    for i, base in enumerate(primes):
        if base > halfN:
            max1_prime_index4base = max(1,i)
            #max1_prime_index4base = i+1
                # 『+1』<<== [N=3][base == 2 > 3//2]
            primes = primes[:max1_prime_index4base]
            break
    for i, base in enumerate(primes):
        if base**2 > N:
            # [is_prime_(N)]
            break
        if N%base == 0:
            if N == base:
                raise 000
            assert 1 < base < N
            factors = [base]
            return (False, ResultCase4is_prime__Nmm_.factors, factors)




    assert unfactored_part4Nmm&1 == 1
    assert factored_part4Nmm&1 == 0
    if unfactored_part4Nmm == 1:
        #ok
        # [factorization4Nmm is complete]
        pass
    elif factored_part4Nmm > unfactored_part4Nmm:
        #ok
        # [1+F1 > sqrt_(N)]
        result_case = ResultCase4is_prime__Nmm_.factored_part4Nmm_ge_sqrtN
        pass
    elif factored_part4Nmm**2 > unfactored_part4Nmm:
        #ok
        # [1+F1 > cubic_root_(N)]
        result_case = ResultCase4is_prime__Nmm_.factored_part4Nmm_ge_cubic_rootN
        pass
    else:
        raise PrimalityFail__is_prime_ex__Nmm_____unfactored_part4Nmm_too_big







    odd_pe_pairs = pe_pairs[1:]
    #odd_p1_pairs = [(odd_p, 1) for odd_p, e in odd_pe_pairs]
    p1_pairs = [(p, 1) for p, e in pe_pairs]
    p2, e2 = pe_pairs[0]
    assert p2 == 2
    assert e2 >= 1
    if to_collect_partials:
        p2rt = {}

    def _test_order_mod_(pe_pairs4B, B, base, /):
        '-> ... | result'
        #assert (B is base) is (pe_pairs4B is pe_pairs)
        assert (B == base) is (pe_pairs4B == pe_pairs)
        try:
            may_xs4good = validate_order_mod_(M, pe_pairs4B, B, factorization_is_pe_pairs=True, to_collect_info=to_collect_partials ....)
        except ValidateFail__order_mod__proper_factor as exc:
            if to_collect_partials ....:
                [(bad_idc, good_idc, xs4good)] = exc.args
                assert bad_idc
                assert 0 < len(bad_idc) < len(pe_pairs4B)
                # [len(bad_idc) < len(pe_pairs4B)] <<== [not$ [x0==1]]
                # [0 < len(bad_idc)] <<== [raise ValidateFail__order_mod__proper_factor]
                assert len(bad_idc) +len(good_idc) == len(pe_pairs4B)
                if js4unfactored:
                    ds = []
                for good_i, x4i in zip(good_idc, xs4good):
                    if good_i in js4unfactored:
                        d = gcd(x4i-1, M)
                        if not d == 1:
                            assert 1 < d < M
                            ds.append(d)
                    p, e = pe_pairs4B[good_i]
                    p2rt.setdefault(p, base)
                        # base not B
                if js4unfactored:
                    if ds:
                        return (False, ResultCase4is_prime__Nmm_.factors, ds)
                if len(p2rt) == len(pe_pairs):
                    # pe_pairs not pe_pairs4B
                    if js4unfactored:
                        return (True, result_case, (ResultCase4is_prime__Nmm_.p2partial_primitive_root, p2rt))
                    return (True, ResultCase4is_prime__Nmm_.p2partial_primitive_root, p2rt)
            return ...
        except ValidateFail__order_mod__not_order:
            raise 000 # since pass primality_test_of_Miller_Rabin
            return (False, ResultCase4is_prime__Nmm_.witness4composite, base)
        if to_collect_partials ....:
            xs4good = may_xs4good
            if js4unfactored:
        return (True, ResultCase4is_prime__Nmm_.primitive_root, base)

    k = min(e2, 1+floor_log2(len(primes)))
    xss = [set() for _ in range(k)]
        # for primitive (2**k)-th-root of 1 mod N
    #xss[0] = {1,Nmm}
    xss[0] = {1,-1}
    def _add_xs_(xs, /):
        for i, x in enumerate(reversed(xs), 1):
            if i == len(xss):
                break
            s = xss[i]
            if s:
                if not x in s:
                    break
            else:
                for s_ in xss[:i]:
                    assert s_
                    for y in s_:
                        xy = x*y%M
                        s.add(xy)
                assert len(s) == (1<<i), (len(s), i, 1<<i, x, xs, xss, M)
        else:
            i = len(xss)
        if i == len(xss):
            return ...

        i, x, s
        x2 = pow(x, 2, M)
        for y in s:
            y2 = pow(y, 2, M)
            if y2 == x2:
                break
        else:
            raise 000
        x,y,x2
        # [x**2 =[%N]= y**2]
        # [(x**2-y**2)%N == 0]
        ds = [x+y, x-y]
        ds = [gcd(d, M) for d in ds]
        ds = [d for d in ds if 1 < d < M]
        if not ds:
            raise 000
        return (False, ResultCase4is_prime__Nmm_.factors, ds)




    for base in primes:
        ######################
        # is N composite?
        #   using primality_test_of_Miller_Rabin
        ######################
        try:
            x0__but2 = _eval_x0_(base, odd_pe_pairs, M)
                # ^ValidateFail__order_mod__proper_factor
        except ValidateFail__order_mod__proper_factor:
            x0__but2 = 1
        x = x0__but2
        if not x == 1:
            for odd_p, _ in odd_pe_pairs:
                x = pow(x, odd_p, M)
                if x == Nmm:
                    break
        # [is_prime_(N)] -> [2**e2 %order_mod_(N;x) == 0]

        xs = [] # for primitive (2**k)-th-root of 1 mod N
        if x == 1:
            #ok
            pass
        elif x == Nmm:
            #ok
            pass
        else:
            for _ in range(e2-1):
                xs.append(x)
                x = pow(x, 2, M)
                if x == Nmm:
                    #ok
                    break
            else:
                return (False, ResultCase4is_prime__Nmm_.witness4composite, base)
        xs
        x
        r = _add_xs_(xs)
        if not r is ...:
            return r
        if x == 1:
            if not to_collect_partials:
                continue

        ######################
        # is "base" a primitive_root_mod_N
        ######################
        x0 = pow(x0__but2, 1<<(e2-1), M)
        if not x0 == 1:
            p1_pairs
            r = _test_order_mod_(p1_pairs, x0, base)
            if r is ...:
                continue
            return r


    ######################
    ######################
    ######################
    prev = 2
    for base in primes:
        ######################
        # try:non-prime primitive_root_candidate
        ######################
        for b in iter_candidate_primitive_root_between_(prev+1, base):
            r = _test_order_mod_(pe_pairs, b, b)
            if r is ...:
                continue
            return r
        prev = base

    if raise__vs__emay is True:
        return ...
    raise PrimalityFail__is_prime_ex__Nmm_____assume_case((case4num, case4root, partial_primitive_roots__vs__primitive_root), tuple(pe_pairs))

#end-def is_prime_ex__Nmm_(factorization4Nmm, /, *, factorization_is_pe_pairs=False, partial_primitive_roots__vs__primitive_root=False, case4num=default_case4num, case4root=default_case4root, raise__vs__emay=False):

def test_many4is_prime_ex__Nmm_(max1, /, **kwds4is_prime_ex__Nmm_):
    u2m = tabulate_may_factorization4uint_lt_(max1)
    for u, m in enumerate(u2m):
        if u < 2:
            pass
        else:
            N = u
            factorization4Nmm = prev_m
            is_prime = N in m
            test_one4is_prime_ex__Nmm_(is_prime, factorization4Nmm, factorization_is_pe_pairs=False, **kwds4is_prime_ex__Nmm_)
        prev_m = m
def test_one4is_prime_ex__Nmm_(result, factorization4Nmm, /, *, factorization_is_pe_pairs=False, **kwds4is_prime_ex__Nmm_):
    N = 1+ II__p2e_(factorization4Nmm)
    r = is_prime_ex__Nmm_(factorization4Nmm, factorization_is_pe_pairs=factorization_is_pe_pairs, **kwds4is_prime_ex__Nmm_)
    if r is ...:
        assert kwds4is_prime_ex__Nmm_['raise__vs__emay'] is True
        pass
    else:
        (is_prime, result_case, payload4result_case) = r
        RC = ResultCase4is_prime__Nmm_
        if result_case is RC.two:
            assert is_prime is True
            assert payload4result_case is None
        elif result_case is RC.primitive_root:
            assert is_prime is True
            primitive_root = payload4result_case
            validate_primality__Pmm_(factorization4Nmm, primitive_root, factorization_is_pe_pairs=factorization_is_pe_pairs, using_p2partial_primitive_root=False)
        elif result_case is RC.p2partial_primitive_root:
            assert is_prime is True
            p2partial_primitive_root = payload4result_case
            validate_primality__Pmm_(factorization4Nmm, p2partial_primitive_root, factorization_is_pe_pairs=factorization_is_pe_pairs, using_p2partial_primitive_root=True)
        elif result_case is RC.factors:
            assert is_prime is False
            factors = payload4result_case
            assert factors
            for ft in factors:
                assert 1 < ft < N
                assert N%ft == 0
        elif result_case is RC.witness4composite:
            assert is_prime is False
            witness4composite = payload4result_case
            assert 2 <= witness4composite < N
            assert N&1 == 1
            assert not is_strong_pseudoprime_(witness4composite, N)
        else:
            raise 000
        pass
    if r is ...:
        assert result is None or result is ...
    else:
        assert result is None or result is is_prime
    return
#]]]"""



r"""[[[
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
class IPrimalityProver4SpecialFormPrime(ABC):
    r'''[[[
    prime in special form:
        e.g. [[(n-1) == F*R][F has been completely factorized]]
    args:
        e.g. provide some witnesses (assume enough to determine primality/compositeness)
        e.g. the factorization of F
    state:
        e.g. 

    #]]]'''#'''
    __slots__ = ()
    #raise NotImplementedError
    #___no_slots_ok___ = True
    def is_prime_(sf, /, *args):
        ...
    def iter_states4is_prime_(sf, /, *args):
        ...
    @abstractmethod
    def __repr__(sf, /):
        #return repr_helper(sf, *args, **kwargs)
        #return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
        ...
#]]]"""

def __():
    from seed.tiny import ifNonef, ifNone, echo
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.helper.repr_input import repr_helper

if __name__ == "__main__":
    pass
__all__


from seed.math.primality_proving import *

