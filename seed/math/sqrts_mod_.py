#__all__:goto
#API:goto
r'''[[[
e ../../python3_src/seed/math/sqrts_mod_.py
!mv ../../python3_src/seed/math/sqrt_mod_.py ../../python3_src/seed/math/sqrts_mod_.py



seed.math.sqrts_mod_
py -m seed.math.sqrts_mod_
py -m nn_ns.app.debug_cmd   seed.math.sqrts_mod_ -x
py -m nn_ns.app.doctest_cmd seed.math.sqrts_mod_:__doc__ -ff -v

from seed.math.sqrts_mod_ import iter_sqrts_mod_prime_power_,  iter_sqrts_mod_prime_
from seed.math.sqrts_mod_ import iter_sqrts_mod_prime_power__coprime__5one_sqrt_
from seed.math.sqrts_mod_ import upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime_, iter_degrade_sqrts_mod_prime_power__coprime__5one_sqrt_
from seed.math.sqrts_mod_ import is_square_residual_mod_prime_power_, is_square_residual_mod_prime_
from seed.math.inv_mod_ import inv_mod_power__coprime_, inv_mod__coprime_, upgrade__inv_mod_power__coprime_


py_adhoc_call   seed.math.sqrts_mod_   @_test4iter_sqrts_mod_prime_power_


[[[
我的开平方算法
===

中国剩余定理，分解 xx 关于base的离散对数
xx =[%p]= base**(inv_mod_(2**e;odd)*odd * e4two_power + inv_mod_(odd;2**e)*2**e * e4odd)

y := xx**(inv_mod_(2**e;odd)*odd) %p
    # e4odd vanish

h := xx**(inv_mod_(odd;2**e)*2**e) %p
    # e4two_power vanish

e4y := discrete_logarithm__coprime_(p, base, order_of_base, factorization_of_order_of_base, y)
    # e4y == e4two_power

xx**(inv_mod_(2**e;odd)*odd) =[%p]= y =[%p]= base**e4y

h**((odd+1)///2)**2 =[%p]= h
h**((odd+1)///2) <- sqrts_(h)
    # !! [[(p-1)%q == 0] -> [p == q**s *t +1] -> [t%q =!= 0] -> [xq**t %p == 1] -> [a_kth_root_mod_(p;q;xq) ==  xq**(inv_mod_(t;q))]]
    # [[p == 2**s *t +1] -> [t%2 =!= 0] -> [xx**t %p == 1] -> [a_sqrt_mod_(p;xx) ==  xx**(inv_mod_(t;2)) == xx**((t+1)///2)]]


xx =[%p]= y * h =[%p]= base**e4y * h
sqrt(xx) =[%p]= sqrt(base**(e4y) * sqrt(h)
sqrt(xx) =[%p]= base**(e4y///2) * h**((odd+1)///2)
sqrt(xx) =[%p]= base**(e4y///2) * xx**(inv_mod_(odd;2**e)*2**e*(odd+1)///2)


]]]

[[[
发现 模运算囗开平方 的 本质都是求 部分离散对数
===
Shanks-Tonelli Algorithm

Atkin-Muller-Armand Square Root Algorithm
    # A Complete Generalization of Atkin’s Square Root Algorithm
e**(3/2):
    # On Shanks Algorithm for Modular Square Roots(2011)(Puchta).pdf
===
from seed.math.discrete_logarithm import discrete_logarithm__coprime_
    #def discrete_logarithm__coprime_(modulus, base, order_of_base, factorization_of_order_of_base, y, /)
    TIME = O(sum((p + ep**(3/2) *log2(p)) for p,ep in factorization_of_order_of_base.items())) *time_per_mul_mod<modulus>
    SPACE = O(max((p + ep + ep**(1/2) *log2(p)) for p,ep in factorization_of_order_of_base.items())) *space_per_word<modulus>


[[p==1+odd*2**e] -> [O(Shanks-Tonelli Algorithm) == O(log2(p)+e**2)*time_per_mul_mod]]
[[p==1+odd*2**e] -> [O(sqrts_mod_ base on discrete_logarithm__coprime_<order_of_base=2**e> Algorithm) == O(log2(p)+e**(3/2))*time_per_mul_mod]]
]]]

[[

===
Shanks-Tonelli Algorithm
    used in factorint::Quadratic Sieve Method
    /sdcard/0my_files/book/math/factorint/202308/The Quadratic Sieve Factoring Algorithm.pdf
    等差数列
        arithmetic series
        arithmetic progression
    [Q(x) =[def]= x**2-N]
    [x <- [floor_sqrtN-M..=floor_sqrtN+M]]
    [MM := [floor_sqrtN-M..=floor_sqrtN+M]]
    [Q(x)%p == 0]:
        [N =[%p]= x**2]
        [Legendre_symbol(N/p) == +1 == N**((p-1)///2) %p]
        [sqrts<%p>(N) =[def]= {x%p, p-x%p}]
    [Q(x) =[%p]= Q(y)]:
        [(x**2-y**2)%p == 0]
        [[x =[%p]= y]or[x =[%p]= -y]]
    [Q(x)%p == 0]:
        [x%p <- sqrts<%p>(N)]
    [prime include -1]
    generate primes, eval sqrts<%p>(N) (if not exist, discard the prime)
    [x__p_1 == {x | [x :<- MM][Q(x)%p == 0]} == MM /-\ [(rNp+i*p) | [rNp :<- sqrts<%p>(N)][i :: int]]]
    [x__p_k == {x | [x :<- MM][Q(x)%p**k == 0]} == MM /-\ [(rNp_k+i*p**k) | [rNp_k :<- sqrts<%p**k>(N)][i :: int]]]
        sqrts<%p**k>(N) <<== Shanks-Tonelli Algorithm
]]


>>> list_sqrts_mod_prime_(2, 0)
[0]
>>> list_sqrts_mod_prime_(2, 2)
[0]
>>> list_sqrts_mod_prime_(2, -1)
[1]
>>> list_sqrts_mod_prime_(2, 1)
[1]
>>> list_sqrts_mod_prime_(2, 3)
[1]
>>> list_sqrts_mod_prime_(2, -3)
[1]

>>> for p in [3, 7, 5, 13, 17, 41]:
...     for xx in range(999, 999+p):
...         (p, xx%p, list_sqrts_mod_prime_(p, xx))
(3, 0, [0])
(3, 1, [1, 2])
(3, 2, [])
(7, 5, [])
(7, 6, [])
(7, 0, [0])
(7, 1, [1, 6])
(7, 2, [3, 4])
(7, 3, [])
(7, 4, [2, 5])
(5, 4, [2, 3])
(5, 0, [0])
(5, 1, [1, 4])
(5, 2, [])
(5, 3, [])
(13, 11, [])
(13, 12, [5, 8])
(13, 0, [0])
(13, 1, [1, 12])
(13, 2, [])
(13, 3, [4, 9])
(13, 4, [2, 11])
(13, 5, [])
(13, 6, [])
(13, 7, [])
(13, 8, [])
(13, 9, [3, 10])
(13, 10, [6, 7])
(17, 13, [8, 9])
(17, 14, [])
(17, 15, [7, 10])
(17, 16, [4, 13])
(17, 0, [0])
(17, 1, [1, 16])
(17, 2, [6, 11])
(17, 3, [])
(17, 4, [2, 15])
(17, 5, [])
(17, 6, [])
(17, 7, [])
(17, 8, [5, 12])
(17, 9, [3, 14])
(17, 10, [])
(17, 11, [])
(17, 12, [])
(41, 15, [])
(41, 16, [4, 37])
(41, 17, [])
(41, 18, [10, 31])
(41, 19, [])
(41, 20, [15, 26])
(41, 21, [12, 29])
(41, 22, [])
(41, 23, [8, 33])
(41, 24, [])
(41, 25, [5, 36])
(41, 26, [])
(41, 27, [])
(41, 28, [])
(41, 29, [])
(41, 30, [])
(41, 31, [20, 21])
(41, 32, [14, 27])
(41, 33, [19, 22])
(41, 34, [])
(41, 35, [])
(41, 36, [6, 35])
(41, 37, [18, 23])
(41, 38, [])
(41, 39, [11, 30])
(41, 40, [9, 32])
(41, 0, [0])
(41, 1, [1, 40])
(41, 2, [17, 24])
(41, 3, [])
(41, 4, [2, 39])
(41, 5, [13, 28])
(41, 6, [])
(41, 7, [])
(41, 8, [7, 34])
(41, 9, [3, 38])
(41, 10, [16, 25])
(41, 11, [])
(41, 12, [])
(41, 13, [])
(41, 14, [])


>>> list_sqrts_mod_prime_power_(3, 1, 991)
[1, 2]
>>> list_sqrts_mod_prime_power_(3, 2, 991)
[1, 8]
>>> list_sqrts_mod_prime_power_(3, 3, 991)
[10, 17]
>>> list_sqrts_mod_prime_power_(3, 4, 991)
[10, 71]

>>> list_sqrts_mod_prime_power_(3, 1, 9)
[0]
>>> list_sqrts_mod_prime_power_(3, 2, 9)
[0, 3, 6]
>>> list_sqrts_mod_prime_power_(3, 3, 9)
[3, 6, 12, 15, 21, 24]
>>> list_sqrts_mod_prime_power_(3, 4, 9)
[3, 24, 30, 51, 57, 78]

>>> list_sqrts_mod_M__by_enumerate_(3**1, 9)
[0]
>>> list_sqrts_mod_M__by_enumerate_(3**2, 9)
[0, 3, 6]
>>> list_sqrts_mod_M__by_enumerate_(3**3, 9)
[3, 6, 12, 15, 21, 24]
>>> list_sqrts_mod_M__by_enumerate_(3**4, 9)
[3, 24, 30, 51, 57, 78]




>>> tabulate_sqrts_mod_M_(6)
[[0], [1, 5], [], [3], [2, 4], []]










_may_output4debug_

>>> from seed.math.sqrts_mod_ import iter_sqrts_mod_prime_
>>> import sys
>>> del sys.modules['seed.math.sqrts_mod_']
>>> from seed.math.sqrts_mod_ import iter_sqrts_mod_prime_

>>> [*iter_sqrts_mod_prime_(2, 0, _may_output4debug_=None)]
[0]
>>> [*iter_sqrts_mod_prime_(2, 0, _may_output4debug_=print)]
('{{{begin:', ('iter_sqrts_mod_prime_', (2, 0)))
('[sqrts_mod__prime_(2;xx) == {xx%2}]', ('iter_sqrts_mod_prime_', (2, 0)))
('}}}end:', ('iter_sqrts_mod_prime_', (2, 0)))
[0]
>>> [*iter_sqrts_mod_prime_(2, 1, _may_output4debug_=print)]
('{{{begin:', ('iter_sqrts_mod_prime_', (2, 1)))
('[sqrts_mod__prime_(2;xx) == {xx%2}]', ('iter_sqrts_mod_prime_', (2, 1)))
('}}}end:', ('iter_sqrts_mod_prime_', (2, 1)))
[1]
>>> [*iter_sqrts_mod_prime_(7, 0, _may_output4debug_=print)]
('{{{begin:', ('iter_sqrts_mod_prime_', (7, 0)))
('[[[p=!=2][xx%p==0]] -> [sqrts_mod__prime_(p;xx) == {0}]]', ('iter_sqrts_mod_prime_', (7, 0)))
('}}}end:', ('iter_sqrts_mod_prime_', (7, 0)))
[0]
>>> [*iter_sqrts_mod_prime_(7, 1, _may_output4debug_=print)]
('{{{begin:', ('iter_sqrts_mod_prime_', (7, 1)))
('[[[p=!=2][xx%p =!= 0][(x_p@floor_sqrt_(xx%p))**2 == xx%p]] -> [sqrts_mod__prime_(p;xx) == {x_p, p-x_p}]]', ('iter_sqrts_mod_prime_', (7, 1)))
('}}}end:', ('iter_sqrts_mod_prime_', (7, 1)))
[1, 6]
>>> [*iter_sqrts_mod_prime_(7, 2, _may_output4debug_=print)]
('{{{begin:', ('iter_sqrts_mod_prime_', (7, 2)))
('[[[p=!=2][xx%p =!= 0][p%4 == 3][x_p := (xx**((odd+1)///2)) %p]] -> [sqrts_mod__prime_(p;xx) == {x_p, p-x_p}]]', ('iter_sqrts_mod_prime_', (7, 2)))
('}}}end:', ('iter_sqrts_mod_prime_', (7, 2)))
[3, 4]
>>> [*iter_sqrts_mod_prime_(7, 3, _may_output4debug_=print)]
('{{{begin:', ('iter_sqrts_mod_prime_', (7, 3)))
('[[[p=!=2][xx%p =!= 0][Jacobi_symbol(p, xx%p) =!= 1]] -> [sqrts_mod__prime_(p;xx) == {}]]', ('iter_sqrts_mod_prime_', (7, 3)))
('}}}end:', ('iter_sqrts_mod_prime_', (7, 3)))
[]
>>>
>>> [*iter_sqrts_mod_prime_(7, 4, _may_output4debug_=print)]
('{{{begin:', ('iter_sqrts_mod_prime_', (7, 4)))
('[[[p=!=2][xx%p =!= 0][(x_p@floor_sqrt_(xx%p))**2 == xx%p]] -> [sqrts_mod__prime_(p;xx) == {x_p, p-x_p}]]', ('iter_sqrts_mod_prime_', (7, 4)))
('}}}end:', ('iter_sqrts_mod_prime_', (7, 4)))
[2, 5]
>>> [*iter_sqrts_mod_prime_(7, 5, _may_output4debug_=print)]
('{{{begin:', ('iter_sqrts_mod_prime_', (7, 5)))
('[[[p=!=2][xx%p =!= 0][Jacobi_symbol(p, xx%p) =!= 1]] -> [sqrts_mod__prime_(p;xx) == {}]]', ('iter_sqrts_mod_prime_', (7, 5)))
('}}}end:', ('iter_sqrts_mod_prime_', (7, 5)))
[]
>>> [*iter_sqrts_mod_prime_(7, 6, _may_output4debug_=print)]
('{{{begin:', ('iter_sqrts_mod_prime_', (7, 6)))
('[[[p=!=2][xx%p =!= 0][Jacobi_symbol(p, xx%p) =!= 1]] -> [sqrts_mod__prime_(p;xx) == {}]]', ('iter_sqrts_mod_prime_', (7, 6)))
('}}}end:', ('iter_sqrts_mod_prime_', (7, 6)))
[]
>>> is_square_residual_mod_prime_(17, 9)
True
>>> is_square_residual_mod_prime_(41, 21)
True
>>> [*iter_sqrts_mod_prime_(17, 15, _may_output4debug_=print)]
('{{{begin:', ('iter_sqrts_mod_prime_', (17, 15)))
('}}}end:', ('iter_sqrts_mod_prime_', (17, 15)))
[7, 10]

>>> from seed.math.sqrts_mod_ import iter_sqrts_mod_prime_power_
>>> [*iter_sqrts_mod_prime_power_(2, 11, 5*2**6, _may_output4debug_=print)]
('{{{begin:', ('iter_sqrts_mod_prime_power_', (2, 11, 320)))
('[[yy%p =!= 0] -> [0 < 2*e < k] -> [sqrts_mod__prime_power_(p**k;yy*p**(2*e)) == ((p**e .*: sqrts_mod__prime_power__coprime_(p**(k-2*e);yy)) *+* (p**(k-e) .*: range(p**e)))]]', ('iter_sqrts_mod_prime_power_', (2, 11, 320)))
('{{{begin:', ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 5, 1)))
('[[[xx%p =!= 0][k>=3][p == 2][xx%8 =!= 1]] -> [sqrts_mod__prime_power__coprime_(p**k;xx) == {}]]', ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 5, 1)))
('}}}end:', ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 5, 1)))
('}}}end:', ('iter_sqrts_mod_prime_power_', (2, 11, 320)))
[]
>>> [*iter_sqrts_mod_prime_power_(2, 11, 17*2**6, _may_output4debug_=print)]
('{{{begin:', ('iter_sqrts_mod_prime_power_', (2, 11, 1088)))
('[[yy%p =!= 0] -> [0 < 2*e < k] -> [sqrts_mod__prime_power_(p**k;yy*p**(2*e)) == ((p**e .*: sqrts_mod__prime_power__coprime_(p**(k-2*e);yy)) *+* (p**(k-e) .*: range(p**e)))]]', ('iter_sqrts_mod_prime_power_', (2, 11, 1088)))
('{{{begin:', ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2]]: x_p@x%p = ???', 1), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2]]: ks<half_down> = ???', [1, 2, 3, 5]), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2]]: pks<half_down> = ???', {0: 1, 1: 2, 2: 4, 3: 8, 5: 32, 4: 16}), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2]]: (q@p**k, xx_q@xx%q) = ???', (32, 17)), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2]]: xx_ds<little-endian radix-p digits of xx%q> = ???', [1, 0, 0, 0, 1]), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2]]: (i, ij@(i+j), j, x_0_i@x%p**i, implicit:xx_0_i@(xx%p**i), xx_i_ij@(xx%p**(i+j)//p**i)) = ???', (1, 2, 1, 1, Ellipsis, 0)), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2]]: (i, ij, j, x_0_i, xx_i_ij) : lhs@((xx_i_ij -(x_0_i**2 //p**i % p**j)) % p**j) = ???', 0), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2][p==2][lhs is even]]: (i, ij, j, x_0_i, xx_i_ij, lhs) : x_i_ij@(lhs///2 *inv_mod_(2**(j-1), x_0_i) %2**(j-1)) = ???', 0), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2]]: (i, ij, j, x_0_i, xx_i_ij, lhs, x_i_ij) : x_0_ij@(x_0_i + x_i_ij*p**i) = ???', 1), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2]]: (i, ij@(i+j), j, x_0_i@x%p**i, implicit:xx_0_i@(xx%p**i), xx_i_ij@(xx%p**(i+j)//p**i)) = ???', (2, 3, 1, 1, Ellipsis, 0)), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2]]: (i, ij, j, x_0_i, xx_i_ij) : lhs@((xx_i_ij -(x_0_i**2 //p**i % p**j)) % p**j) = ???', 0), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2][p==2][lhs is even]]: (i, ij, j, x_0_i, xx_i_ij, lhs) : x_i_ij@(lhs///2 *inv_mod_(2**(j-1), x_0_i) %2**(j-1)) = ???', 0), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2]]: (i, ij, j, x_0_i, xx_i_ij, lhs, x_i_ij) : x_0_ij@(x_0_i + x_i_ij*p**i) = ???', 1), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2]]: (i, ij@(i+j), j, x_0_i@x%p**i, implicit:xx_0_i@(xx%p**i), xx_i_ij@(xx%p**(i+j)//p**i)) = ???', (3, 5, 2, 1, Ellipsis, 2)), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2]]: (i, ij, j, x_0_i, xx_i_ij) : lhs@((xx_i_ij -(x_0_i**2 //p**i % p**j)) % p**j) = ???', 2), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2][p==2][lhs is even]]: (i, ij, j, x_0_i, xx_i_ij, lhs) : x_i_ij@(lhs///2 *inv_mod_(2**(j-1), x_0_i) %2**(j-1)) = ???', 1), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2]]: (i, ij, j, x_0_i, xx_i_ij, lhs, x_i_ij) : x_0_ij@(x_0_i + x_i_ij*p**i) = ???', 9), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
(('[[xx%p =!= 0][k>=2]]: x_q@(x%p**k) = ???', 9), ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
('[[[xx%p =!= 0][k>=4][p==2][found one x_q]] -> [sqrts_mod__prime_power__coprime_(p**k;xx) == {x_q, q-x_q, x_q .^. (q///2), (q-x_q) .^. (q///2)}]]', ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
('}}}end:', ('_iter_sqrts_mod_prime_power__coprime_', (2, 5, 17, 1)))
('}}}end:', ('iter_sqrts_mod_prime_power_', (2, 11, 1088)))
[56, 72, 184, 200, 312, 328, 440, 456, 568, 584, 696, 712, 824, 840, 952, 968, 1080, 1096, 1208, 1224, 1336, 1352, 1464, 1480, 1592, 1608, 1720, 1736, 1848, 1864, 1976, 1992]



(2,3,5,7,13,17,19,31,61,89,107,127,521,607,1279,2203,2281,3217,4253,4423,9689,9941,11213,19937,21701,23209,44497,86243,110503,132049,216091,756839,859433,1257787,1398269,2976221,3021377,6972593,13466917,20996011,24036583,25964951,30402457,32582657,37156667,42643801,43112609,57885161       #unstable: ,74207281,77232917,82589933)

py_adhoc_call   seed.math.prime_gens   @next_may_prime__le_pow2_81__ge_  ='2**72'
4722366482869645213711
py_adhoc_call   seed.math.prime_gens   @next_may_prime__le_pow2_81__ge_  ='2**50'
1125899906842679

>>> selective_test4iter_sqrts_mod_prime_power_(2, 8) #doctest: +SKIP
>>> selective_test4iter_sqrts_mod_prime_power_(2, 89) #doctest: +SKIP
>>> selective_test4iter_sqrts_mod_prime_power_(3, 61) #doctest: +SKIP
>>> selective_test4iter_sqrts_mod_prime_power_(5, 67) #doctest: +SKIP
>>> selective_test4iter_sqrts_mod_prime_power_(7, 63) #doctest: +SKIP
>>> selective_test4iter_sqrts_mod_prime_power_(17, 87) #doctest: +SKIP
>>> selective_test4iter_sqrts_mod_prime_power_(2**89-1, 43) #doctest: +SKIP
>>> selective_test4iter_sqrts_mod_prime_power_(1125899906842679, 79) #doctest: +SKIP
>>> selective_test4iter_sqrts_mod_prime_power_(4722366482869645213711, 53) #doctest: +SKIP

py_adhoc_call   seed.math.sqrts_mod_   @selective_tests4iter_sqrts_mod_prime_power_  '%:print'  --output_=print  ='[(2, 8), (2, 89), (3, 61), (5, 67), (7, 63), (17, 87), (2**89-1, 43), (1125899906842679, 79), (4722366482869645213711, 53)]'

py_adhoc_call   seed.math.sqrts_mod_   @selective_tests4iter_sqrts_mod_prime_power_  '%:print' --output_=print  ='[(89, 2), (61, 3), (67, 5), (47, 7), (43, 17)]'



upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime_
    upgrade__sqrt_mod_odd_prime_power__coprime_
    upgrade_or_after_flip_MSB__sqrt_mod_2_power__coprime_

iter_degrade_sqrts_mod_prime_power__coprime__5one_sqrt_
    iter_sqrts_mod_prime_power__coprime__5one_sqrt_

x_0_ij = upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime_(p, i, j, x_0_i, xx_i_ij, p_i, p_j)
xs__p_j = iter_sqrts_mod_prime_power__coprime__5one_sqrt_(p, j, p_j, w__p_j)
>>> upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime_(2, 4, 3, 0b1001, 0b100, 1<<4, 1<<3)
33
>>> 33 %2**(4-1) == 0b1001 %2**(4-1)
True
>>> 33**2 //2**4 %2**3 == 0b100
True
>>> 33**2 %2**4 == 0b1001**2 %2**4
True
>>> upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime_(3, 4, 3, 1+3*19, 23, 3**4, 3**3)
1516
>>> 1516 %3**4 == (1+3*19)
True
>>> 1516**2 //3**4 %3**3 == 23
True
>>> 1516**2 %3**4 == (1+3*19)**2 %3**4
True
>>> upgrade__sqrt_mod_odd_prime_power__coprime_(3, 4, 3, 1+3*19, 23, 3**4, 3**3)
1516
>>> upgrade_or_after_flip_MSB__sqrt_mod_2_power__coprime_(4, 3, 0b1001, 0b100, 1<<4, 1<<3)
33

upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime__ex_(p, i, j, x_0_i, xx_i_ij, p_i, p_j, /, *, may_inv_x_0_i) -> (may_inv_x_0_i, x_0_i, x_i_ij, x_0_ij)
[i>=3] is not bug
    [i==2==j][x_0_i==3] not is_square_residual_mod_prime_
>>> upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime__ex_(2, 2, 2, 3, 2, 4, 4, may_inv_x_0_i=None)
(None, 3, 0, 3)
>>> upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime__ex_(2, 2, 2, 3, 0, 4, 4, may_inv_x_0_i=None)
(None, 3, 1, 7)
>>> upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime__ex_(2, 2, 2, 3, 1, 4, 4, may_inv_x_0_i=None) # assert i >= 3 AssertionError
Traceback (most recent call last):
    ...
seed.math.sqrts_mod_.Error__not_square_residual_mod: (2, 2, 2, 3, 1)
>>> upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime__ex_(2, 2, 2, 3, 3, 4, 4, may_inv_x_0_i=None) # assert i >= 3 AssertionError
Traceback (most recent call last):
    ...
seed.math.sqrts_mod_.Error__not_square_residual_mod: (2, 2, 2, 3, 3)
>>> _test_p_eq2_and_i_ge_3___4upgrade_sqrt_mod_()

py_adhoc_call   seed.math.sqrts_mod_   @_test_p_eq2_and_i_ge_3___4upgrade_sqrt_mod_

>>> [*iter_sqrts_mod_prime_power__coprime__5one_sqrt_(2, 1, 2**1, 1)]
[1]
>>> [*iter_sqrts_mod_prime_power__coprime__5one_sqrt_(2, 2, 2**2, 1)]
[1, 3]
>>> [*iter_sqrts_mod_prime_power__coprime__5one_sqrt_(2, 2, 2**2, 3)]
[1, 3]
>>> [*iter_sqrts_mod_prime_power__coprime__5one_sqrt_(2, 3, 2**3, 1)]
[1, 3, 5, 7]
>>> [*iter_sqrts_mod_prime_power__coprime__5one_sqrt_(2, 3, 2**3, 3)]
[1, 3, 5, 7]
>>> [*iter_sqrts_mod_prime_power__coprime__5one_sqrt_(2, 3, 2**3, 5)]
[1, 3, 5, 7]
>>> [*iter_sqrts_mod_prime_power__coprime__5one_sqrt_(2, 3, 2**3, 7)]
[1, 3, 5, 7]
>>> f = lambda p,k,/:(lambda q,/:(lambda ls,/:all([*iter_sqrts_mod_prime_power__coprime__5one_sqrt_(p, k, q, x_q)] == ls[x_q**2%q] for x_q in range(q) if x_q%p))(tabulate_sqrts_mod_M_(q)))(p**k)
>>> all(f(2, k) for k in range(1,10))
True
>>> all(f(3, k) for k in range(1,6))
True
>>> all(f(5, k) for k in range(1,5))
True
>>> all(f(7, k) for k in range(1,4))
True
>>> all(f(17, k) for k in range(1,3))
True



is_square_residual_mod_prime_
is_square_residual_mod_prime_power_

>>> f = lambda p,/:([is_square_residual_mod_prime_(p, xx) for xx in range(p)] == [*map(bool, tabulate_sqrts_mod_M_(p))])
>>> f(2)
True
>>> f(3)
True
>>> f(5)
True
>>> f(7)
True
>>> f(17)
True

>>> f = lambda p,k,/:([is_square_residual_mod_prime_power_(p, k, xx) for xx in range(q:=p**k)] == [*map(bool, tabulate_sqrts_mod_M_(q))])
Traceback (most recent call last):
    ...
SyntaxError: assignment expression cannot be used in a comprehension iterable expression
>>> f = lambda p,k,/:(lambda q,/:([is_square_residual_mod_prime_power_(p, k, xx) for xx in range(q)] == [*map(bool, tabulate_sqrts_mod_M_(q))]))(p**k)
>>> all(f(2, k) for k in range(1,10))
True
>>> all(f(3, k) for k in range(1,6))
True
>>> all(f(5, k) for k in range(1,5))
True
>>> all(f(7, k) for k in range(1,4))
True
>>> all(f(17, k) for k in range(1,3))
True


inv_mod_ can upgrade too!!!
upgrade__inv_mod_power__coprime_
inv_mod_power__coprime_
inv_mod__coprime_

def upgrade__inv_mod_power__coprime_(m, i, j, x_0_i, x_i_ij, inv_x_0_i, m_i, m_j, /):
def inv_mod_power__coprime_(m, k, x, /):
def inv_mod__coprime_(M, x, /):
>>> inv_mod__coprime_(15, 2)
8
>>> inv_mod__coprime_(15, 7)
13
>>> inv_mod_power__coprime_(15, 2, (2+6*15))
203
>>> (2+6*15)*203 %15**2
1
>>> inv_mod_power__coprime_(15, 3, (7+5*15 + 9*15**2))
1243
>>> (7+5*15 + 9*15**2)*1243 %15**3
1
>>> inv_mod_power__coprime_(15, 3, (7+5*15 + 9*15**2), may___known__k__inv=(3,1243))
1243
>>> inv_mod_power__coprime_(15, 3, (7+5*15 + 9*15**2), may___known__k__inv=(2,1243%15**2))
1243
>>> inv_mod_power__coprime_(15, 3, (7+5*15 + 9*15**2), may___known__k__inv=(1,1243%15**1))
1243
>>> [*iter_sqrts_mod_prime_power_(2, 11, 17)]
[279, 745, 1303, 1769]
>>> [*iter_sqrts_mod_prime_power_(2, 11, 17, may___known__k__sqrt__may_inv_sqrt=(11,1303, None))]
[279, 745, 1303, 1769]
>>> [*iter_sqrts_mod_prime_power_(2, 11, 17, may___known__k__sqrt__may_inv_sqrt=(10,1303%2**10, None))]
[279, 745, 1303, 1769]
>>> [*iter_sqrts_mod_prime_power_(2, 11, 17, may___known__k__sqrt__may_inv_sqrt=(4,1303%2**4, 7))]
[279, 745, 1303, 1769]
>>> [*iter_sqrts_mod_prime_power_(2, 11, 17, may___known__k__sqrt__may_inv_sqrt=(1,1303%2**1, 1))]
[279, 745, 1303, 1769]



>>> upgrade__inv_mod_power__coprime_(15, 1, 1, (2), (10), 8, 15**1, 15**1)
(12, 188)
>>> divmod(188, 15**1)
(12, 8)
>>> ((2) + (10)*15**1) *(8 + 12*15**1) %15**(1+1)
1
>>> upgrade__inv_mod_power__coprime_(15, 1, 1, (2), (0), 8, 15**1, 15**1)
(7, 113)
>>> divmod(113, 15**1)
(7, 8)
>>> ((2) + (0)*15**1) *(8 + 7*15**1) %15**(1+1)
1
>>> upgrade__inv_mod_power__coprime_(15, 2, 2, (2+6*15), (0+10*15), 203, 15**2, 15**2)
(101, 22928)
>>> divmod(22928, 15**2)
(101, 203)
>>> ((2+6*15) + (0+10*15)*15**2) *(203 + 101*15**2) %15**(2+2)
1
>>> upgrade__inv_mod_power__coprime_(15, 2, 1, (2+6*15), (3), 203, 15**2, 15**1)
(14, 3353)
>>> divmod(3353, 15**2)
(14, 203)
>>> ((2+6*15) + (3)*15**2) *(203 + 14*15**2) %15**(2+1)
1

>>> upgrade__inv_mod_power__coprime_(15, 3, 1, (7+5*15 + 9*15**2), (12), 1243, 15**3, 15**1)
(4, 14743)
>>> divmod(14743, 15**3)
(4, 1243)
>>> ((7+5*15 + 9*15**2) + (12)*15**3) *(1243 + 4*15**3) %15**(3+1)
1
>>> upgrade__inv_mod_power__coprime_(15, 3, 2, (7+5*15 + 9*15**2), (12+7*15), 1243, 15**3, 15**2)
(124, 419743)
>>> divmod(419743, 15**3)
(124, 1243)
>>> ((7+5*15 + 9*15**2) + (12+7*15)*15**3) *(1243 + 124*15**3) %15**(3+2)
1
>>> upgrade__inv_mod_power__coprime_(15, 3, 3, (7+5*15 + 9*15**2), (12+7*15+5*15**2), 1243, 15**3, 15**3)
(574, 1938493)
>>> divmod(1938493, 15**3)
(574, 1243)
>>> ((7+5*15 + 9*15**2) + (12+7*15+5*15**2)*15**3) *(1243 + 574*15**3) %15**(3+3)
1


#>>> _find_arbitrary_one_primitive_root_mod_prime_(188894659314785808547841, {2:75, 5:1})
3
>>> pow(3, 3001, 188894659314785808547841)
110337350542512389496789
>>> pow(9, 3001, 188894659314785808547841)
29635960599175890200997
>>> [*iter_sqrts_mod_prime_(188894659314785808547841, 29635960599175890200997)]
[78557308772273419051052, 110337350542512389496789]
>>> pow(78557308772273419051052, 2, 188894659314785808547841)
29635960599175890200997




#]]]'''
__all__ = r'''
iter_sqrts_mod_prime_
    list_sqrts_mod_prime_
iter_sqrts_mod_prime_power_
    list_sqrts_mod_prime_power_

find_arbitrary_one_square_nonresidual_mod_odd_prime_

iter_sqrts_mod_M__by_enumerate_
    list_sqrts_mod_M__by_enumerate_

tabulate_sqrts_mod_M_
    complete_test4iter_sqrts_mod_prime_power_
selective_tests4iter_sqrts_mod_prime_power_
    selective_test4iter_sqrts_mod_prime_power_

upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime__ex_
    upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime_
        upgrade__sqrt_mod_odd_prime_power__coprime_
        upgrade_or_after_flip_MSB__sqrt_mod_2_power__coprime_

iter_degrade_sqrts_mod_prime_power__coprime__5one_sqrt_
    iter_sqrts_mod_prime_power__coprime__5one_sqrt_

is_square_residual_mod_prime_power_
    is_square_residual_mod_prime_

inv_mod_power__coprime_
    inv_mod__coprime_
    upgrade__inv_mod_power__coprime_


default_upperbound4apply_floor_sqrt

Error
    Error__not_prime_number
    Error__not_coprime
    Error__not_square_residual_mod
    Error__not_inv_mod
    Error__not_flip_MSB
    Error__not_p_eq2_and_i_ge3
    Error__not_sqrt_mod

'''.split()#'''
__all__
def __():
    # API:here
    #inv_mod_ = inv_mod__coprime_
    def inv_mod__coprime_(M, x, /):
        '[M=!=0] ==>> [0 <= inv_mod_(M, x) < abs(M)][(inv_mod_(M, x)*x-1)%M == 0]'
        # !! gcd ~ log2(M) steps
        # O(log2(M)**3)

    def inv_mod_power__coprime_(m, k, x, /):
        'm -> k -> x -> inv_x/uint%m**k # [[m >= 2][k >= 1][gcd(m,x)==1][x*inv_x %m**k == 1]]'
        # O((k**3 + log2(m))*log2(m)**2)

    def upgrade__inv_mod_power__coprime_(m, i, j, x_0_i, x_i_ij, inv_x_0_i, m_i, m_j, /):
        'm -> i -> j -> x_0_i -> x_i_ij -> inv_x_0_i -> m_i -> m_j -> (inv_x_i_ij, inv_x_0_ij) # [[m >= 2][1 <= j <= i][m_i == m**i][m_j == m**j][0 < *_0_i < m**i][0 <= *_i_ij < m**j][0 <= *_0_ij < m**(i+j)]]'
        # O(i**2 * log2(p)**2)






    def is_square_residual_mod_prime_power_(p, k, xx, /):
        'p/prime -> k/int{>=1} -> xx/int -> [?x -> [x**2%p**k == xx%p**k]]/bool'
    def is_square_residual_mod_prime_(p, xx, /):
        'p/prime -> xx/int -> [?x -> [x**2%p == xx%p]]/bool'

    def iter_sqrts_mod_prime_(p, xx, /, *, _may_output4debug_=None, upperbound4apply_floor_sqrt=default_upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime=None):
        'p/prime -> xx/int -> Iter x{x**2 =[%p]= xx} #output is strict sorted # [[upperbound4apply_floor_sqrt == Ellipsis] <-> [upperbound4apply_floor_sqrt == +oo]]'
        # O((log2(p)+log2(p///odd4p)**(3/2))*log2(p)**2 +find_arbitrary_one_square_nonresidual_mod_odd_prime_)
    def iter_sqrts_mod_prime_power_(p, k, xx, /, *, _may_output4debug_=None, upperbound4apply_floor_sqrt=default_upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime=None):
        'p/prime -> k/int{>=1} -> xx/int -> Iter x{x**2 =[%p**k]= xx} # output is strict sorted # [[upperbound4apply_floor_sqrt == Ellipsis] <-> [upperbound4apply_floor_sqrt == +oo]]'
        # O((k**3 + log2(p) + log2(p///odd4p)**(3/2))*log2(p)**2 +find_arbitrary_one_square_nonresidual_mod_odd_prime_ + num_sqrts)





    def upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime_(p, i, j, x_0_i, xx_i_ij, p_i, p_j, /, *, may_inv_x_0_i=None, validate=False):
        'p -> i -> j -> x_0_i -> xx_i_ij -> p_i -> p_j -> x_0_ij # [[p is prime][xx%p =!= 0][i+j <= k][xx%p**k == x**2%p**k][1 <= j <= i][p_i == p**i][p_j == p**j][xx_i_ij == (xx%p**(i+j)//p**i)][xx%p**(i+j) == x_0_ij**2%p**(i+j)][[p%2==1] -> [[x_0_i == x%p**i][x_0_ij == x%p**(i+j)]]][[p==2] -> [[0 <= x_0_i < 2**i][x_0_i%2**(i-1) == x%2**(i-1)][0 <= x_0_ij < 2**(i+j)][x_0_ij%2**(i+j-1) == x%2**(i+j-1)]]]]'
        #   [may_inv_x_0_i is None]:
        #       O((i**3 + log2(p))*log2(p)**2)
        #   [not$ may_inv_x_0_i is None]:
        #       O(i**2 * log2(p)**2)






    def upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime__ex_(p, i, j, x_0_i, xx_i_ij, p_i, p_j, /, *, may_inv_x_0_i, validate=False):
        'p -> i -> j -> x_0_i -> xx_i_ij -> p_i -> p_j -> (_may_inv_x_0_i, _x_0_i, x_i_ij, x_0_ij) # [[p is prime][xx%p =!= 0][i+j <= k][xx%p**k == x**2%p**k][1 <= j <= i][p_i == p**i][p_j == p**j][xx_i_ij == (xx%p**(i+j)//p**i)][xx%p**(i+j) == x_0_ij**2%p**(i+j)][[p%2==1] -> [[x_0_i == x%p**i][x_0_ij == x%p**(i+j)]]][[p==2] -> [[0 <= x_0_i < 2**i][x_0_i%2**(i-1) == x%2**(i-1)][0 <= x_0_ij < 2**(i+j)][x_0_ij%2**(i+j-1) == x%2**(i+j-1)]]]] #[[p==2] -> [i>=2] -> [(may_inv_x_0_i, x_0_i) may be changed]]'
        #   [may_inv_x_0_i is None]:
        #       O((i**3 + log2(p))*log2(p)**2)
        #   [not$ may_inv_x_0_i is None]:
        #       O(i**2 * log2(p)**2)





    def iter_degrade_sqrts_mod_prime_power__coprime__5one_sqrt_(p, i, j, p_i, p_j, x__p_i, /):
        'p -> i -> j -> p_i -> p_j -> x__p_i/(int%p_i) -> xs__p_j/Iter w__p_j/(int%p_j) # [[p is prime][x__p_i%p =!= 0][1 <= j <= i][p_i == p**i][0 <= x__p_i < p_i][0 <= w__p_j < p_j][w__p_j**2%p_j == x__p_i**2%p_j]]'

    def iter_sqrts_mod_prime_power__coprime__5one_sqrt_(p, k, q, x_q, /):
        'p -> k -> q -> x_q/(int%q) -> xs_q/Iter w_q/(int%q) # [[p is prime][x_q%p =!= 0][k >= 1][q == p**k][0 <= x_q < q][0 <= w_q < q][w_q**2%q == x_q**2%q]] #used in degrade all sqrts; see:upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime_'

__all__
from seed.math.discrete_logarithm import discrete_logarithm__coprime_
    #def discrete_logarithm__coprime_(modulus, base, order_of_base, factorization_of_order_of_base, y, /)
    #sqrts_mod__prime_

from seed.for_libs.for_time import (
Timer__print_err
    ,timer__print_err__thread_wide
    ,timer__print_err__process_wide
    ,timer__print_err__system_wide__highest_resolution
    ,timer__print_err__system_wide__monotonic
)

timer = timer__print_err__thread_wide
_to_show_ = False
_to_show_ = True
_to_show_ = __name__ == "__main__"

with timer(prefix='basic...', _to_show_=_to_show_):
    from math import isqrt as floor_sqrt_
    from itertools import pairwise, islice, count as _count

    from seed.math.Jacobi_symbol import Jacobi_symbol
        #def Jacobi_symbol(M, x, /):
        #    'M/int{%2==1} -> x/int -> Jacobi_symbol(x::/M)/(-1|0|+1)'
    from seed.tiny import print_err
    from seed.tiny import null_iter
    from seed.tiny import check_callable
    from seed.tiny import check_type_is
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_2_powers
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
    #def factor_pint_out_power_of_base_(base, n, /):
    #    'base/int{>=2} -> n/pint -> (exp/uint, unfactored_part) #[n == base**exp * unfactored_part][unfactored_part%base =!= 0]'

with timer(prefix='prime_gens', _to_show_=_to_show_):
    from seed.math.prime_gens import prime_gen
    from seed.math.prime_gens import detect_strong_pseudoprime__not_waste_too_much_time_
    #def detect_strong_pseudoprime__not_waste_too_much_time_(n, /):
    #    'n/int -> (0|1|-1) # [0=>not prime][1=>prime][-1=>strong_pseudoprime]'
with timer(prefix='inv_mod_(<-- seed.math.continued_fraction.continued_fraction_fold)', _to_show_=_to_show_):
    from seed.math.inv_mod_ import inv_mod_ as inv_mod__coprime_
    #from seed.math.sqrts_mod_ import inv_mod__coprime_
    #from seed.math.continued_fraction.continued_fraction_fold import inv_mod_ as inv_mod__coprime_
with timer(prefix='radix_repr2uint', _to_show_=_to_show_):
    from seed.int_tools.digits.radix_repr2uint import radix_repr2uint, IRadixRepr2Uint, RadixRepr2Uint
    #def radix_repr2uint(radix_or_an_IRadixRepr2Uint, digits, /,*, is_big_endian:bool, _merge_ver:'0|1|2'=0, input_is_an_IRadixRepr2Uint_not_radix=False):
with timer(prefix='uint2radix_repr', _to_show_=_to_show_):
    from seed.int_tools.digits.uint2radix_repr import uint2radix_repr, IUint2RadixRepr__little_endian__plain, IUint2RadixRepr, Uint2RadixRepr
    #def uint2radix_repr(radix_or_an_IUint2RadixRepr, uint, /,*, is_big_endian:bool, _split_ver:'0|1'=1, min_len=0, imay_max_len=-1, input_is_an_IUint2RadixRepr_not_radix=False):
with timer(prefix='sqrts_mod_', _to_show_=_to_show_):
    if __name__ == "__main__":
        from seed.math.sqrts_mod_ import *

def _dummy1_(_, /):pass



def _test4iter_sqrts_mod_prime_power_():
    p_k__ls = (
    [(2, 1)
    ,(2, 2)
    ,(2, 3)
    ,(2, 4)
    ,(2, 5)
    ,(2, 6)
    ,(2, 7)
    ,(2, 8)
    ,(3, 1)
    ,(3, 2)
    ,(3, 3)
    ,(3, 4)
    ,(3, 5)
    ,(5, 1)
    ,(5, 2)
    ,(5, 3)
    ,(5, 4)
    ,(7, 1)
    ,(7, 2)
    ,(7, 3)
    ,(7, 4)
    ,(17, 1)
    ,(17, 2)
    ,(17, 3)
    ])
    print(f'{__name__}._test4iter_sqrts_mod_prime_power_:begin')
    for p, k in p_k__ls:
        print((p, k))
        complete_test4iter_sqrts_mod_prime_power_(p, k)
    print(f'{__name__}._test4iter_sqrts_mod_prime_power_:end')

def _check_(in_out, /):
    ((p, k, xx), xs_q) = in_out
    if xx%p == 0: raise ValueError(in_out)
    if not len(xs_q) == ((1 if k==1 else (2 if k==2 else 4)) if p == 2 else 2): raise ValueError(in_out)
    q = p**k
    xx_q = xx%q
    if not all(0 < x_q < w_q < q for x_q, w_q in pairwise(xs_q)): raise ValueError(in_out)
    if not all(pow(x_q, 2, q) == xx_q for x_q in xs_q): raise ValueError(in_out)
        #ValueError: ((2, 89, 1856910058928125295021882761), [96299660218406426371046467, 213185349602938642353734589, 405784670039751495095827523, 522670359424283711078515645])

_dummy_output_ = _dummy1_
def selective_tests4iter_sqrts_mod_prime_power_(p_k_pairs, /, *, sz4outer=9, sz4inner=9, output_:print=_dummy1_, check_=_check_):
    for p, k in p_k_pairs:
        selective_test4iter_sqrts_mod_prime_power_(p, k, sz4outer=sz4outer, sz4inner=sz4inner, output_=output_, check_=check_)
def selective_test4iter_sqrts_mod_prime_power_(p, k, /, *, sz4outer=9, sz4inner=9, output_:print=_dummy1_, check_=_check_):
    def main():
        for xx in _iter_xxs__f2_outer_(sz4outer, sz4inner):
            in_out = ((p, k, xx), list_sqrts_mod_prime_power_(p, k, xx))
            output_(in_out)
            check_(in_out)
    def _iter_xxs__f2_outer_(sz4outer, sz4inner, /):
        q = p**k
        #for t in range(1, 1+sz4outer):
        for t in islice(filter(p.__rmod__, _count(2)), sz4outer):
            if t >= q:
                break
            tq = t*q
            floor_sqrt_tq = floor_sqrt_(tq)
            yield from _iter_xxs__f2_inner_(q, sz4inner, floor_sqrt_tq)
        floor_sqrt_q = floor_sqrt_(q)
        #for inv_t in range(2, 2+sz4outer):
        for inv_t in islice(filter(p.__rmod__, _count(2)), sz4outer):
            tq = q//inv_t
            if tq <= floor_sqrt_q:
                break
            yield from _iter_xxs__f2_inner_(q, sz4inner, tq)
    def _iter_xxs__f2_inner_(q, sz4inner, floor_sqrt_xx, /):
        f2 = floor_sqrt_xx**2
        if not floor_sqrt_xx%p == 0:
            yield f2 +7*q
        step0 = 2*floor_sqrt_xx+1
        acc = f2
        for step in range(step0, step0 +2*sz4inner, 2):
            acc += step
            if not acc%p == 0:
                yield acc
    main()
    return
def complete_test4iter_sqrts_mod_prime_power_(p, k, /):
    q = p**k
    xx2xs__q = tabulate_sqrts_mod_M_(q)

    for xx in range(3*q, 4*q):
        #r0 = list_sqrts_mod_M__by_enumerate_(q, xx)
        r1 = list_sqrts_mod_prime_power_(p, k, xx)
        xx_q = xx%q
        r0 = xx2xs__q[xx_q]
        if not r0 == r1:
            raise Exception((p,k,q), (xx,xx%q), (r0, r1))
            r'''[[[
raise Exception((p,k,q), (xx,xx%q), (r0, r1))
Exception: ((2, 2, 4), (13, 1), ([1, 3], []))
            #]]]'''#'''

def tabulate_sqrts_mod_M_(M, /):
    'O(M*log2(M)**2) : M/int{>=1} -> xx2xs__M/[int%M]{len=M}{[[xx_M :<- [0..<M]][x_M :<- xx2xs__M[xx_M]][x_M**2%M==xx_M]]} #output is strict sorted'
    check_type_is(int, M)
    if not M >= 1: raise ValueError(M)
    xx2xs__M = [[] for i in range(M)]
    for x_M in range(M):
        xx_M = x_M**2%M
        xx2xs__M[xx_M].append(x_M)
    return xx2xs__M

def list_sqrts_mod_M__by_enumerate_(M, xx, /):
    'O(M*log2(M)**2) : M/int{>=1} -> xx/int -> [x{x**2 =[%M]= xx}] #output is strict sorted'
    return [*iter_sqrts_mod_M__by_enumerate_(M, xx)]

def iter_sqrts_mod_M__by_enumerate_(M, xx, /):
    'O(M*log2(M)**2) : M/int{>=1} -> xx/int -> Iter x{x**2 =[%M]= xx} #output is strict sorted'
    check_type_is(int, M)
    check_type_is(int, xx)
    if not M >= 1: raise ValueError(M)
    xx_M = xx%M
    return (x_M for x_M in range(M) if x_M**2%M == xx_M)


default_upperbound4apply_floor_sqrt = 1<<32

def list_sqrts_mod_prime_(p, xx, /, *, upperbound4apply_floor_sqrt=default_upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime=None):
    'p/prime -> xx/int -> [x{x**2 =[%p]= xx}] #[O((log2(p)+log2(p///odd4p)**(3/2))*log2(p)**2 +find_arbitrary_one_square_nonresidual_mod_odd_prime_)]'
    return [*iter_sqrts_mod_prime_(p, xx, upperbound4apply_floor_sqrt=upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime=may_arbitrary_one_square_nonresidual_mod_odd_prime)]

#iter_sqrts_mod_prime_power_
def iter_sqrts_mod_prime_(p, xx, /, *, _may_output4debug_=None, upperbound4apply_floor_sqrt=default_upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime=None):
    r'''[[[
    'p/prime -> xx/int -> Iter x{x**2 =[%p]= xx} #output is strict sorted # [[upperbound4apply_floor_sqrt == Ellipsis] <-> [upperbound4apply_floor_sqrt == +oo]]'

    O((log2(p)+log2(p///odd4p)**(3/2))*log2(p)**2 +find_arbitrary_one_square_nonresidual_mod_odd_prime_)
    #]]]'''#'''
    check_type_is(int, p)
    check_type_is(int, xx)
    xx0 = xx
    output4debug_ = _5may_output4debug_(_may_output4debug_)
    fnm_params = ('iter_sqrts_mod_prime_', (p, xx0))
    999;    output4debug_((_begin, fnm_params))
    yield from _body4iter_sqrts_mod_prime_(fnm_params, output4debug_, p, xx, upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime)
    999;    output4debug_((_end, fnm_params))
    return
def _body4iter_sqrts_mod_prime_(fnm_params, output4debug_, p, xx, upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime, /):
    if p == 2:
        999;    output4debug_(('[sqrts_mod__prime_(2;xx) == {xx%2}]', fnm_params))
        yield xx&1
        return
    yield from _iter_sqrts_mod_odd_prime_(fnm_params, output4debug_, p, xx, upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime)
def is_square_residual_mod_prime_power_(p, k, xx, /):
    'p/prime -> k/int{>=1} -> xx/int -> [?x -> [x**2%p**k == xx%p**k]]/bool'
    check_type_is(int, p)
    check_type_is(int, k)
    check_type_is(int, xx)
    if not p >= 2: raise ValueError(p)
    if not p == 2:
        if not p&1 ==1: raise ValueError(p)
    if not k >= 1: raise ValueError(p)
    # [k >= 1]

    #bug::if k == 1 or (p&1):
    #   miss[xx%p =!= 0]
    if k == 1:
        return is_square_residual_mod_prime_(p, xx)
    # [k >= 2]

    xx_p = xx%p
    if xx_p == 0:
        q = p**k
        xx_q = xx%q
        # [0 <= xx_q < q]
        if xx_q == 0:
            return True
        # [0 < xx_q < q]
        (ee, yy_h) = factor_pint_out_power_of_base_(p, xx_q)
        if ee&1 == 1:
            return False
        #e = ee>>1
        p, k, xx, xx_p = p, k-ee, yy_h, yy_h%p
            # conversion witb same result
        yy_h = ee = xx_q = q = None
    # [k >= 2][xx%p =!= 0]

    if p == 2:
        # [p == 2][k >= 2][xx%p =!= 0]
        if 0:
            k = min(k, 3)
            # [p == 2][2 <= k <= 3][xx%p =!= 0]
        if k == 2:
            # [k == 2][xx%2 =!= 0]
            # [[xx%2 =!= 0] -> [is_square_residual_mod_prime_(2, 2, xx)] <-> [xx%4 == 1]]
            return (xx&3) == 1
        # [k >= 3][xx%2 =!= 0]
        # [[k >= 3] -> [xx%2 =!= 0] -> [is_square_residual_mod_prime_(2, k, xx)] <-> [xx%8 == 1]]
        return (xx&7) == 1
    else:
        # [p =!= 2][k >= 2][xx%p =!= 0]
        if 0:
            k = 1
            # [p =!= 2][k == 1][xx%p =!= 0]
        # [[k >= 1] -> [xx%p =!= 0] -> [is_square_residual_mod_prime_(p, k, xx)] <-> [is_square_residual_mod_prime_(p, xx_p)]]
        return is_square_residual_mod_prime_(p, xx_p)
    raise 000

def is_square_residual_mod_prime_(p, xx, /):
    'p/prime -> xx/int -> [?x -> [x**2%p == xx%p]]/bool'
    check_type_is(int, p)
    check_type_is(int, xx)
    if not p >= 2: raise ValueError(p)
    if not p == 2:
        if not p&1 ==1: raise ValueError(p)

    if p == 2:
        return True
    # [p is odd prime]
    return not Jacobi_symbol(p, xx) == -1
        # 0, +1 OK
    ######################
    #########deprecated:
    #if upperbound4apply_floor_sqrt
    xx_p = xx%p
    w_p = floor_sqrt_(xx_p)
    if w_p**2 == xx_p:
        x_p = w_p
        return True

    return not Jacobi_symbol(p, xx_p) == -1
        # 0, +1 OK
    if xx_p == 0:
        return True
    # [xx%p =!= 0]

    # !! [p is odd prime]
    # !! [xx%p =!= 0]
    # !! [x%p =!= 0]
    # [pow(x, (p-1), p) == +1]
    # [pow(x**2, (p-1)//2, p) == +1]
    # [pow(xx, (p-1)//2, p) == +1]
    return pow(xx_p, (p-1)//2, p) == +1

def find_arbitrary_one_square_nonresidual_mod_odd_prime_(p, /):
    'p/prime{>2} -> square_nonresidual/int # [[-p < square_nonresidual < p][@[x :<- [0..<p]] -> [x**2%p =!= square_nonresidual%p]][-1 == Jacobi_symbol(p, z)]]'
    check_type_is(int, p)
    if not p >= 3: raise ValueError(p)
    if not p&1 ==1: raise ValueError(p)

    if p&3 == 3:
        # [p == 4*k+3]
        z = -1
        # [not$ is_square_residual_mod(p;z)]
    elif 1 < (p&7) < 7:
        # [p == 8*k+/-3]
        z = 2
        # [not$ is_square_residual_mod(p;z)]
    else:
        assert p&7 == 1
        # [p == 8*k+1]
        #
        # [[p,q :: odd_prime] -> [p=!=q] -> [(p:/q)(q:/p)==(-1)^((p-1)(q-1)/4)]]
        #
        # [[p,q :: odd_prime] -> [q < p == 8*k+1] -> [(q:/p) == (p:/q)]]
        for q in prime_gen.iter__ge_(3):
            #if q == p: raise logic-err
            if p < q**2: raise logic-err
            if -1 == Jacobi_symbol(q, p%q):
                break
        z = q
        # [not$ is_square_residual_mod(p;z)]
    # [not$ is_square_residual_mod(p;z)]
    # [z**(odd*2**(e-1))%p == -1]
    assert -1 == Jacobi_symbol(p, z)
    return z


def _iter_sqrts_mod_odd_prime_(fnm_params, output4debug_, p, xx, upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime, /):
    r'''[[[
    'p/odd_prime -> xx/int -> Iter x{x**2 =[%p]= xx} #[using discrete_logarithm__coprime_ + Chinese_Remainder_Theorem on exp/index] #output is strict sorted'
    O((log2(p)+log2(p///odd4p)**(3/2))*log2(p)**2)

    [[p==1+odd*2**e] -> [O(sqrts_mod_ base on discrete_logarithm__coprime_<order_of_base=2**e> Algorithm) == O(log2(p)+e**(3/2))*time_per_mul_mod]]
    #]]]'''#'''
    'old-ver: p/odd_prime -> xx/int -> Iter x{x**2 =[%p]= xx} #[Shanks-Tonelli Algorithm] #output is strict sorted'

    check_type_is(int, p)
    check_type_is(int, xx)
    if not p >= 3: raise ValueError(p)
    if not p&1 ==1: raise ValueError(p)
    # [p%2 == 1]

    xx0 = xx
    xx_p = xx0%p
    if xx_p == 0:
        # [xx%p == 0]
        999;    output4debug_(('[[[p=!=2][xx%p==0]] -> [sqrts_mod__prime_(p;xx) == {0}]]', fnm_params))
        yield 0
        return
    # [p%2 == 1][xx%p =!= 0]

    if upperbound4apply_floor_sqrt is ... or xx_p < upperbound4apply_floor_sqrt:
        #apply_floor_sqrt
        w_p = floor_sqrt_(xx_p)
        if w_p**2 == xx_p:
            x_p = w_p
            999;    output4debug_(('[[[p=!=2][xx%p =!= 0][(x_p@floor_sqrt_(xx%p))**2 == xx%p]] -> [sqrts_mod__prime_(p;xx) == {x_p, p-x_p}]]', fnm_params))
            yield x_p
            yield p -x_p
            return
        #end-if w_p**2 == xx_p:
    #end-if xx_p < upperbound4apply_floor_sqrt:

    # [p%2 == 1][xx%p =!= 0]
    if not Jacobi_symbol(p, xx_p) == 1:
        # [not$ is_square_residual_mod(p;xx)]
        999;    output4debug_(('[[[p=!=2][xx%p =!= 0][Jacobi_symbol(p, xx%p) =!= 1]] -> [sqrts_mod__prime_(p;xx) == {}]]', fnm_params))
        return
    # [is_square_residual_mod(p;xx)]

    #999;    output4debug_(('[[[p=!=2][xx%p =!= 0][Jacobi_symbol(p, xx%p) == 1]] -> [sqrts_mod__prime_(p;xx) == {...apply [Shanks-Tonelli Algorithm]...}]]', fnm_params))




    # [p%2 == 1][xx%p =!= 0][Jacobi_symbol(p, xx%p) == 1]
    e, odd = factor_pint_out_2_powers(p-1)
    # [p-1 == odd*2**e][odd%2==1]
    # !! [is_square_residual_mod(p;xx)]
    # [xx**(odd*2**(e-1))%p == 1]
    assert e >= 1
    if e == 1:
        # [e == 1]
        # [p%4 == 3]
        # !! [xx**(odd*2**(e-1))%p == 1]
        # !! [e == 1]
        # [xx**odd %p == 1]
        # [xx**(odd+1) %p == xx]
        # [(xx**((odd+1)///2))**2 %p == xx]
        # [(xx**((odd+1)///2)) %p <- sqrts_mod__prime_(p; xx)]
        x_p = pow(xx_p, (odd+1)//2, p)
        assert xx_p == pow(x_p, 2, p)
        999;    output4debug_(('[[[p=!=2][xx%p =!= 0][p%4 == 3][x_p := (xx**((odd+1)///2)) %p]] -> [sqrts_mod__prime_(p;xx) == {x_p, p-x_p}]]', fnm_params))
        w_p = p -x_p
        if w_p < x_p:
            x_p, w_p = w_p, x_p
        yield x_p
        yield w_p
        return
    # [e >= 2]
    # [p%4 == 1]

    r'''[[[
  [p%8==5][s==2]:
    # Atkin’s Algorithm
    # let [x := xx*c*(a_sqrt_mod_(p;-1) -1) %p]
    # let [x**2 %p == xx**2 *c**2 *(-2*a_sqrt_mod_(p;-1)) %p == xx * (xx *c**2 *(-2)*a_sqrt_mod_(p;-1)) %p]
    # let [b == a_sqrt_mod_(p;-1) == (2*xx *c**2) == (2*xx)**(2*e+1)] to determine c
    # -> [c == (2*xx)**e %p]
    # ...
    [c := (2*xx)**((p-5)///8) %p]
    [b := 2*xx*c**2 %p]
    [x := xx*c*(b-1) %p]
    [x %p <- sqrts_mod_(p;xx)]
    #]]]'''#'''
    if e == 2:
        # [e == 2]
        # [p%8 == 5]
        c = pow(2*xx_p, (p-5)//8, p)
        c_xx_p = c*xx_p %p
        b = 2*c_xx_p*c %p
        x_p = c_xx_p*(b-1) %p
        assert xx_p == pow(x_p, 2, p)

        999;    output4debug_(('[[[p=!=2][xx%p =!= 0][p%8 == 5][c := (2*xx)**((p-5)///8) %p][b := 2*xx*c**2 %p][x := xx*c*(b-1) %p]] -> [sqrts_mod__prime_(p;xx) == {x_p, p-x_p}]]', fnm_params))
        w_p = p -x_p
        if w_p < x_p:
            x_p, w_p = w_p, x_p
        yield x_p
        yield w_p
        return
    # [e >= 3]
    # [p%8 == 1]

    # [((2*xx)**t) **2 %p == -1] ==>> [b == (2*xx)**t %p][c == (2*xx)**e %p][x := xx *c*(b-1) %p]
    #
    # !! [[(p-1)%q == 0] -> [p == q**s *t +1] -> [t%q =!= 0] -> [xq**t %p == 1] -> [a_kth_root_mod_(p;q;xq) ==  xq**(inv_mod_(t;q))]]
    # [[p == 2**s *t +1] -> [t%2 =!= 0] -> [xx**t %p == 1] -> [a_sqrt_mod_(p;xx) ==  xx**(inv_mod_(t;2)) == xx**((t+1)///2)]]

    if may_arbitrary_one_square_nonresidual_mod_odd_prime is None:
        z = find_arbitrary_one_square_nonresidual_mod_odd_prime_(p)
        # [Jacobi_symbol(p, z) == -1]
    else:
        z = may_arbitrary_one_square_nonresidual_mod_odd_prime
        if not Jacobi_symbol(p, z) == -1: raise ValueError(z)
        # [Jacobi_symbol(p, z) == -1]
    # [Jacobi_symbol(p, z) == -1]


    #我的开平方算法:goto
    discrete_logarithm__coprime_
    base = pow(z, odd, p)
    order_of_base = 1<<e
    factorization_of_order_of_base = {2:e}
    #fail:y = pow(xx_p, odd, p)
    _2_e = (1<<e)
    y = pow(xx_p, inv_mod__coprime_(_2_e, odd)*odd, p)
    e4y = discrete_logarithm__coprime_(p, base, order_of_base, factorization_of_order_of_base, y)
    assert e4y%2 == 0
    x_p = pow(base, e4y//2, p) * pow(xx, (inv_mod__coprime_(odd, _2_e)*_2_e*((odd+1)//2))%(p-1), p) %p
    assert xx_p == pow(x_p, 2, p)
    w_p = p -x_p
    if w_p < x_p:
        x_p, w_p = w_p, x_p
    yield x_p
    yield w_p
    return




    999;    output4debug_((('[[[p=!=2][xx%p =!= 0][Jacobi_symbol(p, xx%p) == 1]]: {...apply [Shanks-Tonelli Algorithm]...} : (e,odd,z) = ??? :=> [[p-1 == odd*2**e][odd%2==1][Jacobi_symbol(p, z) == -1]]]', (e,odd,z)), fnm_params))




    # [p%2 == 1][xx%p =!= 0][Jacobi_symbol(p, xx%p) == 1][p-1 == odd*2**e][odd%2==1][Jacobi_symbol(p, z) == -1]
    e, odd, z
    [a := pow(xx_p, (odd+1)//2, p)]
      # (first guess of square root)

    [b := pow(xx_p, odd, p)]
    # !! [xx**(odd*2**(e-1))%p == 1]
    # [b**(2**(e-1)) %p == 1]
    # [a**2 =[%p]= xx**(odd+1) =[%p]= xx*b]
    # [a**2 =[%p]= xx*b]

    [g := pow(z, odd, p)]
    # !! [z**(odd*2**(e-1))%p == -1]
    # [g**(2**(e-1))%p == -1]

    [r := e]
      # (exponent r will decrease after each updation)

    a, b, g, r
    999;    output4debug_((('[[[p=!=2][xx%p =!= 0][Jacobi_symbol(p, xx%p) == 1]]: {...apply [Shanks-Tonelli Algorithm]...} : (e,odd,z) : init (a,b,g,r) = ??? :=> [[a**2 =[%p]= xx*b][b**(2**(r-1)) %p == 1][g**(2**(r-1)) %p == -1][r==e]]]', (a,b,g,r)), fnm_params))

    # !! [r == e]
    # !! [b**(2**(e-1)) %p == 1]
    # [b**(2**(r-1)) %p == 1]
    # !! [g**(2**(e-1))%p == -1]
    # [g**(2**(r-1))%p == -1]
    # !! [a**2 =[%p]= xx*b]
    while 1:
        ######################
        # [a**2 =[%p]= xx*b]
        # [b**(2**(r-1)) %p == 1]
        # [g**(2**(r-1)) %p == -1]
        ######################
        #let m :=> [m <- [0..<r]][b**(2**m) %p == 1]
        b2 = b
        for m in range(r):
            if b2 == 1:
                break
            b2 = pow(b2, 2, p)
        else:
            raise logic-err

        # [0 <= m < r]
        # [b**(2**m) %p == 1]
        # [[m > 0] -> [b**(2**(m-1)) %p == -1]]

        if m==0:
            # !! [b**(2**m) %p == 1]
            # [b**(2**0) %p == 1]
            # [b %p == 1]
            # [a**2 =[%p]= xx*b =[%p]= 1]
            # [(a**2-xx)%p == 0]
            assert xx_p == pow(a, 2, p)
            x_p = a
            999;    output4debug_((('[[[p=!=2][xx%p =!= 0][Jacobi_symbol(p, xx%p) == 1]]: {...apply [Shanks-Tonelli Algorithm]...} : (e,odd,z) : found x_p@(x%p) = ???]', x_p), fnm_params))
            break
        # [0 < m < r]
        # [b**(2**(m-1)) %p == -1]

        ######################
        #to update a,b, but keep:
        # [a**2 =[%p]= xx*b]
        # [b**(2**(r-1)) %p == 1]
        # [g**(2**(r-1)) %p == -1]
        ######################
        r'''[[[
        [rr := m]:
            [0 < rr < r]
            !! [g**(2**(r-1)) %p == -1]
            [(g**(2**(r-rr)))**(2**(rr-1)) %p == -1]
            [(g**(2**(r-m)))**(2**(rr-1)) %p == -1]
            !! [gg**(2**(rr-1)) %p == -1]
            [gg := (g**(2**(r-m))) %p]
        [aa := a*K %p]:
            !! [a**2 =[%p]= xx*b]
            [aa**2 =[%p]= xx*bb]
            [bb := b*K**2]
            !! [b**(2**(r-1)) %p == 1]
            [bb**(2**(rr-1)) %p == 1]
            !! [rr := m]
            [bb**(2**(m-1)) %p == 1]
                <==> [(b*K**2)**(2**(m-1)) %p == 1]
                !! [b**(2**(m-1)) %p == -1]
                <==> [K**(2**m) %p == -1 %p]
                !! [g**(2**(r-1)) %p == -1]
                <<== [K == g**(2**(r-1-m)) %p]
        ==>>:
        [rr := m]
        [gg := (g**(2**(r-m))) %p]
        [aa := a*K %p]:
        [bb := b*K**2]
        [K := g**(2**(r-1-m)) %p]

        ==>>:
        [K := g**(2**(r-1-m)) %p]
        [r := m]
        [g := K**2 %p]
        [a := a*K %p]
        # [b := b*K**2 %p]
        [b := b*g %p]
        #]]]'''#'''
        [K := pow(g, 1<<(r-1-m), p)]
        # !! [0 <= m < r]
        # [rr < r] # ==>> loop will stop
        [r := m]
        [g := pow(K, 2, p)]
        [a := a*K %p]
        [b := b*g %p]
        999;    output4debug_((('[[[p=!=2][xx%p =!= 0][Jacobi_symbol(p, xx%p) == 1]]: {...apply [Shanks-Tonelli Algorithm]...} : (e,odd,z) : update&dec-r (a,b,g,r) = ??? :=> [[a**2 =[%p]= xx*b][b**(2**(r-1)) %p == 1][g**(2**(r-1)) %p == -1][r < r<old>]]]', (a,b,g,r)), fnm_params))
    #end-while 1:
    x_p

    999;    output4debug_(('[[[p=!=2][xx%p =!= 0][Jacobi_symbol(p, xx%p) == 1][found one x_p]] -> [sqrts_mod__prime_(p;xx) == {x_p, p-x_p}]]', fnm_params))


    w_p = p -x_p
    if w_p < x_p:
        x_p, w_p = w_p, x_p
    yield x_p
    yield w_p
    return

def list_sqrts_mod_prime_power_(p, k, xx, /, *, upperbound4apply_floor_sqrt=default_upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime=None):
    'p/prime -> k/int{>=1} -> xx/int -> [x{x**2 =[%p**k]= xx}] # output is strict sorted'
    return [*iter_sqrts_mod_prime_power_(p, k, xx, upperbound4apply_floor_sqrt=upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime=may_arbitrary_one_square_nonresidual_mod_odd_prime)]

_dummy_output4debug_ = _dummy1_
def _5may_output4debug_(_may_output4debug_, /):
    if _may_output4debug_ is None:
        output4debug_ = _dummy_output4debug_
    #elif _may_output4debug_ is True:
    #    output4debug_ = print_err
    else:
        output4debug_ = _may_output4debug_
    check_callable(output4debug_)
    return output4debug_

_begin = '{{{begin:'
_end = '}}}end:'
def iter_sqrts_mod_prime_power_(p, k, xx, /, *, _may_output4debug_=None, upperbound4apply_floor_sqrt=default_upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime=None, may___known__k__sqrt__may_inv_sqrt=None):
    r'''[[[
    'p/prime -> k/int{>=1} -> xx/int -> Iter x{x**2 =[%p**k]= xx} # output is strict sorted # [[upperbound4apply_floor_sqrt == Ellipsis] <-> [upperbound4apply_floor_sqrt == +oo]]'


    O((k**3 + log2(p) + log2(p///odd4p)**(3/2))*log2(p)**2 +find_arbitrary_one_square_nonresidual_mod_odd_prime_ + num_sqrts)


    ######################
    ######################
    [gcd(p, xx) == 1]:
        O((k**3 + log2(p) + log2(p///odd4p)**(3/2))*log2(p)**2 +find_arbitrary_one_square_nonresidual_mod_odd_prime_)
    [gcd(p, xx) =!= 1]:
        above + O(num_sqrts)

    #]]]'''#'''
    check_type_is(int, p)
    check_type_is(int, k)
    check_type_is(int, xx)
    if not p >= 2: raise ValueError(p)
    # [p >= 2]
    if not p == 2:
        if not p&1 ==1: raise ValueError(p)
    # [[p == 2]or[p%2 == 1]]
    if not k >= 1: raise ValueError(k)
    if not may___known__k__sqrt__may_inv_sqrt is None:
        knowns = may___known__k__sqrt__may_inv_sqrt
        check_type_is(tuple, knowns)
        if not len(knowns) == 3: raise ValueError
        kt, x_0_kt, may__inv_x_0_kt = may___known__k__sqrt__may_inv_sqrt
        check_type_is(int, kt)
        check_type_is(int, x_0_kt)
        if not may__inv_x_0_kt is None:
            inv_x_0_kt = may__inv_x_0_kt
            check_type_is(int, inv_x_0_kt)
        if not kt >= 1: raise ValueError(kt)

    xx0 = xx
    output4debug_ = _5may_output4debug_(_may_output4debug_)
    fnm_params = ('iter_sqrts_mod_prime_power_', (p, k, xx0))
    999;    output4debug_((_begin, fnm_params))
    yield from _body4iter_sqrts_mod_prime_power_(fnm_params, output4debug_, p, k, xx, upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime, may___known__k__sqrt__may_inv_sqrt)
    999;    output4debug_((_end, fnm_params))
    return

def _body4iter_sqrts_mod_prime_power_(fnm_params, output4debug_, p, k, xx, upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime, may___known__k__sqrt__may_inv_sqrt, /):
    # [k >= 1]
    xx0 = xx
    xx_p = xx0%p
    if xx_p == 0:
        q = p**k
        xx_q = xx0%q
        if xx_q == 0:
            999;    output4debug_(('[sqrts_mod__prime_power_(p**k;0) == range(0, p**k, p**((k+1)//2))]', fnm_params))
            x_q = p**((k+1)//2)
            yield from range(0, q, x_q)
            return
        # [xx_q > 0]
        #bug:(exp, yy_q) = factor_pint_out_power_of_base_(p, xx_q)
        #   yy_q --> yy_h
        (ee, yy_h) = factor_pint_out_power_of_base_(p, xx_q)
        # [xx_q == p**ee *yy_h]
        # [yy_h%p =!= 0]
        #
        # !! [xx_q > 0]
        # !! [xx_q == xx_q%p**k]
        # !! [xx%p == 0]
        # [1 <= ee < k]
        assert 1 <= ee < k
        # let (y_hh,e) :=> [(y_hh*p**e)**2 %q == yy_h *p**ee][(y_hh*p**e) == y_hh *p**e %q]
        # [2*e == ee]
        if ee&1 == 1:
            999;    output4debug_(('[[yy%p =!= 0] -> [0 < 2*e+1 < k] -> [sqrts_mod__prime_power_(p**k;yy*p**(2*e+1)) == {}]]', fnm_params))
            return
        # [2 <= ee < k]
        e = ee>>1
        # [1 <= e < (k+1)//2 < k]
        p_e = p**e
        assert p <= p_e < q
        if 0:
            r'''[[[
            #bug:
            #   [y_q**2%q == yy_q]
            #   [(y_q*p**e)**2%q == yy_q*p**(2*e)]
            for y_q in _iter_sqrts_mod_prime_power__coprime_(p, k, yy_q, yy_q%p):
                yield (p_e*y_q) %q
            #]]]'''#'''
        # !! [xx_q := xx0%p**k]
        # [xx_q := xx_q%p**k]
        # [p**ee *yy_h == p**ee *yy_h %p**k]
        # [yy_h == yy_h %p**(k-ee)]
        #
        # !! [(y_hh*p**e) == y_hh *p**e %q]
        # [y_hh == y_hh %p**(k-e)]
        #
        #
        # !! [yy_h == yy_h %p**(k-ee)]
        # !! [(y_hh*p**e)**2 %q == yy_h *p**ee]
        # [y_hh**2 %p**(k-ee) == yy_h]
        # let y_h :=> [y_h**2 %p**(k-ee) == yy_h][y_h == y_h %p**(k-ee)]
        #
        # [y_hh == y_hh %p**(k-e)]
        # [y_h == y_h %p**(k-ee)]
        # [y_h == y_hh %p**(k-ee)]
        #
        # [h := (yhh -y_h)///p**(k-ee)]
        # [(h, y_h) == divmos(yhh, p**(k-ee))]
        # [y_hh == y_h + h*p**(k-ee)][h == h%p**e]
        #
        # [(y_hh)**2 %p**(k-ee) == (y_hh %p**(k-ee))**2 %p**(k-ee) == y_h**2 %p**(k-2*e) == yy_h]
        #
        r'''[[[
        if 0:
            step = p**(k-2*e)
            p_k_neg_e = step*p_e
            #unordered! deprecated
            # !! let y_h :=> [y_h**2 %p**(k-ee) == yy_h][y_h == y_h %p**(k-ee)]
            for y_h in _iter_sqrts_mod_prime_power__coprime_(p, k-ee, yy_h, yy_h%p):
                #for h in range(p_e):
                #    h_step = h*step
                #for h_step in range(0, p_k_neg_e, step):
                #    y_hh = y_h + h_step
                #for y_hh in range(y_h, y_h+p_k_neg_e, step):
                yield from range(y_h, y_h+p_k_neg_e, step)
                    #y_hh are unordered!!
        #]]]'''#'''

        999;    output4debug_(('[[yy%p =!= 0] -> [0 < 2*e < k] -> [sqrts_mod__prime_power_(p**k;yy*p**(2*e)) == ((p**e .*: sqrts_mod__prime_power__coprime_(p**(k-2*e);yy)) *+* (p**(k-e) .*: range(p**e)))]]', fnm_params))
        # !! let y_h :=> [y_h**2 %p**(k-ee) == yy_h][y_h == y_h %p**(k-ee)]
        y_h__ls = [y_h for y_h in _iter_sqrts_mod_prime_power__coprime_(output4debug_, p, k-ee, yy_h, yy_h%p, upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime, may___known__k__sqrt__may_inv_sqrt)]
        assert len(y_h__ls) <= 4
        # !! [y_hh == y_h + h*p**(k-ee)][h == h%p**e]
        # [y_hh <- {y_h + h*p**(k-ee) | [y_h :<- y_h__ls][h :<- [0..<p**e]]}]
        #
        # !! [xx_q == p**ee *yy_h]
        # !! let (y_hh,e) :=> [(y_hh*p**e)**2 %q == yy_h *p**ee][(y_hh*p**e) == y_hh *p**e %q]
        # !! [y_hh == y_hh %p**(k-e)]
        # [(y_hh*p**e)**2 %q == yy_h *p**ee == xx_q][y_hh == y_hh %p**(k-e)]
        # [x_q <- {y_hh*p**e | [y_hh <- {y_h + h*p**(k-ee) | [y_h :<- y_h__ls][h :<- [0..<p**e]]}]}]
        # [x_q <- {(y_h + h*p**(k-ee))*p**e | [y_h :<- y_h__ls][h :<- [0..<p**e]]}]
        # [x_q <- {(y_h*p**e + h*p**(k-e)) | [y_h :<- y_h__ls][h :<- [0..<p**e]]}]
        #   for [p==2][2*(k-e-1) >= k]:
        #       # [2*(k-e-1) >= k] <==> [k >= ee+2]
        #       [x_q <- {(y_h*p**e + h*p**(k-e-1)) | [y_h :<- y_h__ls][h :<- [0..<p**e]]}]
        #       but no improvement at all, since MSB of sqrts_mod_(2**i; _) is arbitrary already.
        #
        p_k_neg_e = p**(k-e)
        y_h_p_e__ls = [y_h*p_e for y_h in y_h__ls]
        # [x_q <- {(y_h_p_e + h*p_k_neg_e) | [y_h_p_e :<- y_h_p_e__ls][h :<- [0..<p**e]]}]
        # [x_q <- {(y_h_p_e + h_p_k_neg_e) | [y_h_p_e :<- y_h_p_e__ls][h_p_k_neg_e :<- [0,p_k_neg_e..<p**k]]}]
        #
        for h_p_k_neg_e in range(0, q, p_k_neg_e):
            for y_h_p_e in y_h_p_e__ls:
                x_q = y_h_p_e + h_p_k_neg_e
                yield x_q
                    #x_q are sorted!!
        return
    # [xx%p =!= 0]

    999;    output4debug_(('[[xx%p =!= 0] -> [sqrts_mod__prime_power_(p**k;xx) == sqrts_mod__prime_power__coprime_(p**k;xx)]]', fnm_params))

    # [p >= 2]
    # [[p == 2]or[p%2 == 1]]
    # [k >= 1]
    # [xx%p =!= 0]
    yield from _iter_sqrts_mod_prime_power__coprime_(output4debug_, p, k, xx0, xx_p, upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime, may___known__k__sqrt__may_inv_sqrt)
    return


def _decompose__greedy_(k, /):
    #greedy
    assert k >= 1
    ks = [1]
    for _ in range(k.bit_length()-1):
        ks.append(ks[-1] << 1)
    t = k -ks[-1]
    assert 0 <= t < ks[-1]
    if not t == 0:
        ks.append(k)
    return ks
#def _decompose__half_down_(k, /):
def _decompose__half_down_(k0, k, /):
    #half_down
    assert k >= k0 >= 1
    # [k >= k0 >= 1]
    k_ = k
    ks = [k_]
    # [k_ >= k0 >= 1]
    #while not k_ == 1:
    while k_ > k0:
        # [k_ > k0 >= 1]
        # [k_ >= 2]
        # [k_ > (k_+1)//2 >= 1]
        #   ==>> loop halt
        k_ = (k_+1)//2
        ks.append(k_)
        # [k_ >= 1]
        # may have:[k_ <= k0]
    if k_ < k0:
        ks[-1] = k0
    ks.reverse()
    assert ks[0] == k0
    assert ks[-1] == k
    return ks
def _prepare_p_pows__half_down_(p, ks, /):
    # !! [O(_prepare_p_pows__half_down__p_gt2_(p;ks<i0,k>) == O(k**2 *log2(p)**2)]
    # [O(_prepare_p_pows__half_down_(p;ks<i0,k>) == O(k**2 *log2(p)**2)]
    if p == 2:
        pks = _prepare_p_pows__half_down__p_eq2_(ks)
    else:
        pks = _prepare_p_pows__half_down__p_gt2_(p, ks)
    return pks
def _prepare_p_pows__half_down__p_gt2_(p, ks, /):
    '{i,i-1}'
    # [O(_prepare_p_pows__half_down__p_gt2_(p;ks<i0,k>) == O(sum (2**i*log2(p))**2 {i :<- [1..=log2(k)]}) <= O((sum 2**i {i :<- [1..=log2(k)]} *log2(p))**2) == O((2**log2(k) *log2(p))**2) == O((k *log2(p))**2)]
    # [O(_prepare_p_pows__half_down__p_gt2_(p;ks<i0,k>) == O(k**2 *log2(p)**2)]
    pks = {}
    if not ks[0] == 1:
        k0, k1 = ks[:2]
        i = k0
        ij = k1
        j = ij - i
        #es = {i, j, ij, ij-1}
        es = {i-1,j}
        min_e = min(es)
        pks[min_e] = p**min_e
        for e in es:
            if e > min_e:
                pks[e] = p**(e-min_e) * pks[min_e]
        pks[i] = pks[i-1]*p
        if j > 1:
            assert not (ij-1) in pks
            pks[ij-1] = pks[i-1]*pks[j]
        pks[ij] = pks[ij-1]*p
        ######################
        pks[i]
        pks[j]
        pks[ij]
        pks[ij-1]
        ks = ks[2:]
        pre_i = ij
        pre_i_neg1 = ij-1
    for i in ks:
        if i >= 4:
            i_neg1 = i-1
            if not i_neg1 in pks:
                if i&1:
                    # [i is odd]
                    # [i == 2*pre_i -1]
                    # [i-1 == 2*pre_i_neg1]
                    pks[i_neg1] = pks[pre_i_neg1]**2
                else:
                    # [i is even]
                    # [i == 2*pre_i]
                    # [i-1 == pre_i +pre_i_neg1]
                    pks[i_neg1] = pks[pre_i_neg1]*pks[pre_i]
            #end-if not i_neg1 in pks:

            pks[i] = pks[i_neg1]*p
            #next round
            pre_i_neg1 = i_neg1
            pre_i = i
        elif i == 1:
            pks[1] = p
        elif i == 2:
            pks[2] = p**2
            #next round
            pre_i_neg1 = 1
            pre_i = 2
        elif i == 3:
            pks[3] = p*pks[2]
            #next round
            pre_i_neg1 = 2
            pre_i = 3
        else:
            raise ValueError((ks, i))
    return pks
def _prepare_p_pows__half_down__p_eq2_(ks, /):
    '{i,i-1,i-2} i>=3'
    pks = {0:1}
        #x_i_ij___MSB0 = lhs//2 *inv_mod__coprime_(pks[j-1], x_0_i) %pks[j-1]
        #   KeyError: 0
        #
    if not ks[0] == 1:
        k0, k1 = ks[:2]
        i = k0
        ij = k1
        j = ij - i
        es = {j-1,j}
        for e in es:
            pks[e] = 1 << e
        ######################
        pks[j]
        pks[j-1]
    for i in ks:
        for j in [i,i-1,i-2]:
            if j >= 0 and not j in pks:
                pks[j] = 1<<j
        r'''[[[
        if i >= 4:
            i_neg1 = i-1
            i_neg2 = i-2
            if not i_neg2 in pks:
                pks[i_neg2] = 1<<i_neg2
            if not i_neg1 in pks:
                pks[i_neg1] = 1<<i_neg1
            if not i in pks:
                pks[i] = 1<<i
        elif i == 1:
            pks[1] = 2
        elif i == 2:
            pks[2] = 4
        elif i == 3:
            pks[3] = 8
        else:
            raise ValueError((ks, i))
        #]]]'''#'''
    return pks

def _iter_sqrts_mod_prime_power__coprime_(output4debug_, p, k, xx0, xx_p, upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime, may___known__k__sqrt__may_inv_sqrt, /):
    r'''[[[

decompose k:
    k = i + j where i >= j
    [ks :: [pint]]
    [1 == k[0] <= ks[-1] == k]
    [k[a] < k[a+1] <= 2*k[a]]
    target: min len(ks)
    greedy:
        33 => [1,2,4,8,16,32,33]
            7
        31 => [1,2,4,8,16,31]
            6
    half_down:
        33 => [1,2,3,5,9,17,33]
            7
        31 => [1,2,4,8,16,31]
            6
    [len(ks) >= ceil_log2(k)]
    [min len(ks) == ceil_log2(k)]
        <<== greedy
        <<== half_down
    [half_down vs greedy]:
        half_down better since handle less digits


copy from:
view others/数学/二次互反律.txt
    平方根提升:
[[
平方根提升:
  # 允许[x%p==0]非互素
@[p,i,j::int][is_prime p][1<=j<=i][
  [x :<- [0..<p**i]]
  [u :<- [0..<p**j]]
  [xj := x + u*p**i]
  ]:
  [xj <- [0..<p**(i+j)]]
  [u == (xj-x)///p**i]

  [high_digits := (xj**2%p**(i+j) - x**2%p**i)]
  [high_digits <- [0..<p**(i+j)]]
  !![1<=j<=i]
  [high_digits
    == (x**2 + 2*x*u*p**i + (u*p**i)**2)%p**(i+j) - x**2%p**i
    == (x**2 + 2*x*u*p**i)%p**(i+j) - x**2%p**i
    == (x**2 //p**i + 2*x*u)*p**i %p**(i+j)
    == (x**2 //p**i + 2*x*u)%p**j *p**i
    ]
  [(p**i) \\\ high_digits]
  [k := high_digits ///p**i %p**j]
  [k <- [0..<p**j]]
  [xj**2%p**(i+j) == x**2%p**i + k*p**i]
      # 固定x: k%p**j的数量 决定 xj**2%p**(i+j)的数量
  [k == (x**2 //p**i + 2*x*u)%p**j]
  [2*x*u%p**j == (k - x**2 //p**i)%p**j]

  ##已知:xx_ij, x
  #     前置条件:[xx_ij%p**i == x**2%p**i]
  #     后置条件:[xx_ij==xj**2%p**(i+j)] #xj为输出
  ##==>>已知:x**2%p**i
  ##==>>已知:high_digits
  ##==>>已知:k
  ##求xj # 即 提升x为xj
  ##<==>求u
  [e := max_power_of_base_as_factor_of_(p;2*x)]
  [e>=0] # [x==0] ==>> [e==+oo]
  [k := xx_ij //p**i %p**j]
  * [2*x%p =!= 0]:
    [e==0]
    [u == u%p**j == inv_mod_(p**j;2*x)*(k - x**2 //p**i)%p**j]
          # (u,xj) 唯一
    [p**min(e,j)==p**e==p**0==1]
  * [2*x%p == 0]:
    [e>=1]
    [2*x%p**j==0] <==> [e>=j]
    * [e>=j]:
      [k == (x**2 //p**i + 2*x*u)%p**j == (x**2 //p**i)%p**j]
          # k与u无关
      !![k := xx_ij //p**i %p**j]
      [xx_ij //p**i %p**j == (x**2 //p**i)%p**j]
      !![xx_ij%p**i == x**2%p**i]
      [xx_ij %p**(i+j) == (x**2)%p**(i+j)]
      * [xx_ij %p**(i+j) == (x**2)%p**(i+j)]:
        [u <- [0..<p**j]]
            # (u,xj) 共有p**j对
        [p**min(e,j)==p**j]
      * [xx_ij %p**(i+j) =!= (x**2)%p**(i+j)]:
        [u <- {}]
            # (u,xj) 共有0对无解
    * [e<j]:
      [x2_pe := 2*x///p**e]
      [x2_pe <- [0..<2*p**(i-e)]]
      [x2_pe%p =!= 0]
      [2*x == x2_pe*p**e]
      [k == (x**2 //p**i + 2*x*u)%p**j
        == (x**2 //p**i + x2_pe*p**e*u)%p**j
        ]
      [x2_pe*p**e*u =[%p**j]= (k - x**2 //p**i)]
      * [p**e \\\ (k - x**2 //p**i)]:
        [x2_pe*u =[%p**(j-e)]= (k - x**2 //p**i) ///p**e]
        [u =[%p**(j-e)]= (k - x**2 //p**i) ///p**e *inv_mod_(p**(j-e);x2_pe)]
        [u0 := (k - x**2 //p**i) ///p**e *inv_mod_(p**(j-e);x2_pe) %p**(j-e)]
        [u0 <- [0..<p**(j-e)]]
        [u%p**(j-e) == u0]
        !![u :<- [0..<p**j]]
        [u <- {u0+v*p**(j-e) | [v :<- [0..<p**e]]}]
            # (u,xj) 共有p**e对
        [p**min(e,j)==p**e]
      * [not$ p**e \\\ (k - x**2 //p**i)]:
        [u <- {}]
            # (u,xj) 共有0对无解
  综上:[(u,xj)共有p**min(e,j)对 if [p**(min(e,j)+i) \\\ (xx_ij - x**2)] else 0对无解]
  统一解形式:
    [mej := min(e,j)]
    [x2_p_mej := x///p**mej] #注意:x2_pe在[x==0]未定义
    [xj <- {x+(u0+v*p**(j-mej))*p**i | [u0 :<- (if [p**(mej+i) \\\ (xx_ij - x**2)] then {(xx_ij - x**2) ///p**(mej+i) *inv_mod_(p**(j-mej);x2_p_mej) %p**(j-mej)} else {})][v :<- [0..<p**mej]]}]

  #####
  #最快提升:
  [j==i]:
    !![x :<- [0..<p**i]]
    * [x==0]:
      [e == +oo > i]
    * [x=!=0][p==2]:
      [e <- [1..=i]]
    * [x=!=0][p=!=2]:
      [e <- [0..<i]]
      [e < i]
    #####
    [mej == j]
      <==> [e >= j]
      <==> [e >= i]
      <==> [[x==0]or[p==2][x==2**(i-1)]]
    #####实例:
        # xx_ij = 1
        # p = 2
        # i = j = 5
        # e = 1
        # mej = 1
        # k = 0
        # 2**5: x <- {1,17,15,31}
        # 过滤:[xx_ij =[%p**(i+mej)==2**6]= x**2]
        # {x:x**2%2**6} = {1:1,17:33,15:33,31:1}
        ##只有[x<-{1,31}]合格
        # {x:may u0<x>} == {1:0,17:/,15:/,31:-15*15%2**4==15}
        # {x:{xj}} == {1:{1+(0+0*16)*32=1,1+(0+1*16)*32=513},17:{},15:{},31:{31+(15+0*16)*32=511,31+(15+1*16)*32=1023}}
        # {xj} == {1,2**9-1,2**9+1,2**10-1}


]]
    #]]]'''#'''
    p, k, xx0, xx_p

    fnm_params = ('_iter_sqrts_mod_prime_power__coprime_', (p, k, xx0, xx_p))
    999;    output4debug_((_begin, fnm_params))
    xs_q = _body4iter_sqrts_mod_prime_power__coprime_(fnm_params, output4debug_, p, k, xx0, xx_p, upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime, may___known__k__sqrt__may_inv_sqrt)
    yield from xs_q # ==>> begin~end correctly placed
    999;    output4debug_((_end, fnm_params))
    return
    return xs_q

def _body4iter_sqrts_mod_prime_power__coprime_(fnm_params, output4debug_, p, k, xx0, xx_p, upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime, may___known__k__sqrt__may_inv_sqrt, /):
    r'''[[[
    ######################
    '...+O((log2(p)+log2(p///odd4p)**(3/2))*log2(p)**2 +find_arbitrary_one_square_nonresidual_mod_odd_prime_)'
        #find x_p

    '...+O(k**2 * log2(p)**2)'
        #build pks

    '...+O((i0**3 + log2(p))*log2(p)**2)'
        #calc inv_x_0_i

    [t :<- [0..=log2(k/i0)]][i := i0*2**t]:
        '...+O(i**2 * log2(p)**2)'
            # upgrade (x_0_i,inv_x_0_i) -> (x_0_ij,inv_x_0_ij)
    ######################
            total4upgrade == O(k**3 * log2(p)**2)

    ######################
    total = O((k**3 + log2(p) + log2(p///odd4p)**(3/2))*log2(p)**2 +find_arbitrary_one_square_nonresidual_mod_odd_prime_)
    #]]]'''#'''
    validate = False
    p, k, xx0, xx_p
    # [p >= 2]
    # [[p == 2]or[p%2 == 1]]
    # [k >= 1]
    # [xx%p =!= 0]

    if not may___known__k__sqrt__may_inv_sqrt is None:
        knowns = may___known__k__sqrt__may_inv_sqrt
        kt, x_0_kt, may__inv_x_0_kt = may___known__k__sqrt__may_inv_sqrt
        if not may__inv_x_0_kt is None:
            inv_x_0_kt = may__inv_x_0_kt

    if not may___known__k__sqrt__may_inv_sqrt is None:
        if k <= kt:
            q = p**k
            x_q = x_0_kt %q
            xs_q = _iter_sqrts_mod_prime_power__coprime__5one_sqrt_(fnm_params, output4debug_, p, k, q, x_q, {k:q, k-1:1<<(k-1)} if p==2 else {k:q})
            #yield from xs_q
            return xs_q
        # [1 <= kt < k]
    # [[not$ may___known__k__sqrt__may_inv_sqrt is None] -> [1 <= kt < k]]


    if k == 1:
        999;    output4debug_(('[[[xx%p =!= 0][k==1]] -> [sqrts_mod__prime_power__coprime_(p**k;xx) == sqrts_mod__prime_(p;xx)]]', fnm_params))
        # !! [[not$ may___known__k__sqrt__may_inv_sqrt is None] -> [1 <= kt < k]]
        if not may___known__k__sqrt__may_inv_sqrt is None: raise 000

        xs_p = iter_sqrts_mod_prime_(p, xx_p, _may_output4debug_=output4debug_, upperbound4apply_floor_sqrt=upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime=may_arbitrary_one_square_nonresidual_mod_odd_prime)
        xs_q = xs_p
        #yield from xs_q
        return xs_q
    # [k >= 2]
    # [[not$ may___known__k__sqrt__may_inv_sqrt is None] -> [1 <= kt < k]]

    # now:is_square_residual_mod_prime_, is_square_residual_mod_prime_power_
    if not p == 2:
        # [p%2 == 1]
        if not Jacobi_symbol(p, xx_p) == 1:
            # [not$ is_square_residual_mod(p;xx)]
            999;    output4debug_(('[[[xx%p =!= 0][k>=2][p%2 == 1][Jacobi_symbol(p, xx%p) =!= 1]] -> [sqrts_mod__prime_power__coprime_(p**k;xx) == {}]]', fnm_params))
            return null_iter
        # [is_square_residual_mod(p;xx)]
        # [is_square_residual_mod(q;xx)]
    else:
        # [p == 2]

        # !! [xx%p =!= 0]
        # [xx is odd]
        # [k >= 2]
        if k == 2:
            # [k == 2]
            if not xx0&3 == 1:
                # [k == 2][xx%4 =!= 1]
                # [not$ is_square_residual_mod(4;xx)]
                999;    output4debug_(('[[[xx%p =!= 0][k==2][p == 2][xx%4 =!= 1]] -> [sqrts_mod__prime_power__coprime_(p**k;xx) == {}]]', fnm_params))
                return null_iter
            # [k == 2][xx%4 == 1]
            # [is_square_residual_mod(4;xx)]
        else:
            # [k >= 3]
            if not xx0&7 == 1:
                # [k >= 3][xx%8 =!= 1]
                # [not$ is_square_residual_mod(8;xx)]
                # !! [k >= 3]
                # [not$ is_square_residual_mod(q;xx)]
                999;    output4debug_(('[[[xx%p =!= 0][k>=3][p == 2][xx%8 =!= 1]] -> [sqrts_mod__prime_power__coprime_(p**k;xx) == {}]]', fnm_params))
                return null_iter
            # [k >= 3][xx%8 == 1]
            # [is_square_residual_mod(8;xx)]
            # [is_square_residual_mod(q;xx)]
            pass
        # [is_square_residual_mod(q;xx)]
        # [[[k == 2][xx%4 == 1]] or [[k >= 3][xx%8 == 1]]]
        # [k >= 2]
        if k < 4:
            pks = ...
            q = 1 << k
            x_q = 1
            xs_q = _iter_sqrts_mod_prime_power__coprime__5one_sqrt_(fnm_params, output4debug_, p, k, q, x_q, pks)
            #yield from xs_q
            return xs_q
        # [k >= 4][xx%8 == 1]
            #below floor_sqrt_, required [k >= 3]
        pass

    #q = p**k
    #xx_q = xx0%q
    # [k >= 2]
    # [is_square_residual_mod(q;xx)]
    #
    # [[p==2] -> [xx%8 == 1]]
    # [[p==2] -> [k >= 4]]


    # [k >= 2]
    # [[not$ may___known__k__sqrt__may_inv_sqrt is None] -> [1 <= kt < k]]
    if not may___known__k__sqrt__may_inv_sqrt is None:
        # [1 <= kt < k]
        x_0_kt
        i = kt
        x_0_i = x_0_kt
        # [1 <= i < k]
    else:
        # [k >= 2]
        if p == 2:
            # [p == 2]
            # [k >= 4][xx%8 == 1]
            #it = iter(range(1, 8, 2))
            x_p = 1
        else:
            # [p >= 3]
            # [k >= 2]
            it = iter_sqrts_mod_prime_(p, xx_p, _may_output4debug_=output4debug_, upperbound4apply_floor_sqrt=upperbound4apply_floor_sqrt, may_arbitrary_one_square_nonresidual_mod_odd_prime=may_arbitrary_one_square_nonresidual_mod_odd_prime)
            '...+O((log2(p)+log2(p///odd4p)**(3/2))*log2(p)**2 +find_arbitrary_one_square_nonresidual_mod_odd_prime_)'
            [x_p, _] = it
        x_p
        999;    output4debug_((('[[xx%p =!= 0][k>=2]]: x_p@x%p = ???', x_p), fnm_params))
        x_0_1 = x_p

        i = 1
        x_0_i = x_0_1
        # !! [k >= 2]
        # [1 <= i < k]
    # [1 <= i < k]
    i, x_0_i






    # [1 <= i < k]
    ks = _decompose__half_down_(i, k)
    assert ks[0] == i
    assert ks[-1] == k
    assert 1 <= i < k
    assert len(ks) >= 2

    #ks = _decompose__greedy_(k)
    999;    output4debug_((('[[xx%p =!= 0][k>=2]]: ks<half_down> = ???', ks), fnm_params))

    r'''[[[
    see:_upgrade__sqrt_mod_prime_power__coprime_:requirements<pks>

    which p**i are required using greedy?
        !! greedy
        [j == i] except last j
    which p**i are required using half_down?
    !! half_down
        [j <- {i,i-1}]
        [p >= 3]:
            pks[i]
            pks[i-1]
            pks[k]
        [p == 2]:
            pks[i]
            [i >= 1]:
                pks[i-1] #maybe pks[j-1] --> pks[0]
            [i >= 2]:
                pks[i-2] #maybe pks[j-1] --> pks[0]
            pks[k]
            pks[k-1]
    <<==
    :
    pks[i]
    pks[j]
    pks[i+j]
    pks[k]
    [p == 2]:
        [i >= 3]:
            pks[i-1]
            pks[i-2]
        pks[j-1] # pks[0] if j==1
        pks[k-1]
    <<==
    common:
        [lhs :=  (xx_i_ij -(x_0_i**2 //pks[i] % pks[j])) % pks[j]]
        #next round:
        x_0_i = x_0_ij
        w_q = q -x_q
    * [p >= 3]:
        no extra
    * [p == 2]:
        yield pks[k-1] -x_q
        [_x_0_i := x_0_i + pks[i-1]]
        [_lhs := lhs -(pks[i-2] +x_0_i) %pks[j]]
        x_i_ij___MSB0 = lhs//2 *inv_mod__coprime_(pks[j-1], x_0_i) %pks[j-1]
    #]]]'''#'''
    if 0:
        pks = [1]
        for _ in range(k):
            pks.append(pks[-1]*p)
    pks = _prepare_p_pows__half_down_(p, ks)
    # !! [O(_prepare_p_pows__half_down_(p;k) == O(k**2 *log2(p)**2)]
    '...+O(k**2 * log2(p)**2)'
    999;    output4debug_((('[[xx%p =!= 0][k>=2]]: pks<half_down> = ???', pks), fnm_params))


    q = pks[k]
    xx_q = xx0%q
    999;    output4debug_((('[[xx%p =!= 0][k>=2]]: (q@p**k, xx_q@xx%q) = ???', (q, xx_q)), fnm_params))


    if upperbound4apply_floor_sqrt is ... or xx_q < upperbound4apply_floor_sqrt:
        #apply_floor_sqrt
        w_q = floor_sqrt_(xx_q)
        if w_q**2 == xx_q:
            x_q = w_q
            999;    output4debug_((('[[xx%p =!= 0][k>=2][(x_q@floor_sqrt_(xx_q))**2 == xx_q]]: x_q = ???', x_q), fnm_params))
            if p == 2:
                # [p == 2]
                # [k >= 4][xx%8 == 1]
                999;    output4debug_(('[[[xx%p =!= 0][k>=2][(x_q@floor_sqrt_(xx_q))**2 == xx_q][p==2][k >= 4]] -> [sqrts_mod__prime_power__coprime_(p**k;xx) == {x_q, q///2-x_q, q///2+x_q, q-x_q}]]', fnm_params))
                #yield x_q
                #yield pks[k-1] -x_q
                #yield pks[k-1] +x_q
                #yield q -x_q
            else:
                999;    output4debug_(('[[[xx%p =!= 0][k>=2][(x_q@floor_sqrt_(xx_q))**2 == xx_q][p=!=2]] -> [sqrts_mod__prime_power__coprime_(p**k;xx) == {x_q, q-x_q}]]', fnm_params))
                #yield x_q
                #yield q -x_q
            xs_q = _iter_sqrts_mod_prime_power__coprime__5one_sqrt_(fnm_params, output4debug_, p, k, q, x_q, pks)
            #yield from xs_q
            return xs_q
        #end-if w_q**2 == xx_q:
    #end-if xx_q < upperbound4apply_floor_sqrt:




    #uint2radix_repr(p, xx_q)
    #xx_ds = [*uint2radix_repr(p, xx0, is_big_endian=True, imay_max_len=k)]
    xx_ds = [*uint2radix_repr(p, xx_q, is_big_endian=True, imay_max_len=k)]
    xx_ds.reverse()
    if len(xx_ds) < k:
        xx_ds += [0]*(k-len(xx_ds))
    assert len(xx_ds) == k
    999;    output4debug_((('[[xx%p =!= 0][k>=2]]: xx_ds<little-endian radix-p digits of xx%q> = ???', xx_ds), fnm_params))



    ######################
    #x_p # [x_p**2 %p == xx%p]
    i, x_0_i # [x_0_i**2 %p**i == xx%p**i]
    ks # == _decompose__half_down_(i, k)
    pks # [pks[i] == p**i]
    q # == p**k
    xx_q # == xx%p**k
    xx_ds #  xx%p**k --> little-endian radix-p number
    ######################

    if not (may___known__k__sqrt__may_inv_sqrt is None or may__inv_x_0_kt is None):
        assert i == kt
        # !! [x_0_i == x_0_kt]
        inv_x_0_i = inv_x_0_kt
    elif 1:
        inv_x_0_i = inv_mod_power__coprime_(p, i, x_0_i)
        '...+O((i0**3 + log2(p))*log2(p)**2)'
    else:
        inv_x_0_i = inv_mod__coprime_(pks[i], x_0_i)
        # !! gcd ~ log2(p**i) steps
        # ...+O(log2(p**i)**3)
        '...+O(i0**3 * log2(p)**3)'
            # but normally [i0==1] here
    inv_x_0_i

    #i = 1 | kt # = ks[0]
    #implicit: xx_0_i = xx_q%p**i
        # xx_ds[0:i]
    x_0_i
        # sqrts_mod_$ xx_ds[0:i]
    inv_x_0_i
        # inv_mod_$ sqrts_mod_$ xx_ds[0:i]


    for i, ij in pairwise(ks):
        # [i >= ks[0] == (1|kt) >= 1]
        # [x_0_i**2 %p**i == xx %p**i]
        # [x_0_i*inv_x_0_i %p**i == 1]
        j = ij - i
        assert 1 <= j <= i
        xx_i_ij = radix_repr2uint(p, xx_ds[i:ij], is_big_endian=False)
            # xx_ds[0:i+j]
        #(xx_0_i, xx_i_ij, x_0_i) --> x_i_ij
        #   implicit:xx_0_i
        (inv_x_0_i, x_0_i, x_i_ij, x_0_ij) = _upgrade__sqrt_mod_prime_power__coprime_(fnm_params, output4debug_, p, i, j, x_0_i, xx_i_ij, pks, inv_x_0_i, validate) # -> (_may_inv_x_0_i, _x_0_i, x_i_ij, x_0_ij)
        # !! [not$ may_inv_x_0_i is None]:
        '...+O(i**2 * log2(p)**2)'
            # xxx '...+O(i**3 * log2(p)**3)'
        if ij == k:
            inv_x_0_ij = ...
        else:
            p_i = pks[i]
            p_j = pks[j]
            (inv_x_i_ij, inv_x_0_ij) = _upgrade__inv_mod_power__coprime_(fnm_params, output4debug_, p, i, j, x_0_i, x_i_ij, inv_x_0_i, p_i, p_j)
            '...+O(i**2 * log2(p)**2)'
        inv_x_0_ij
        x_0_ij
        ######################
        #next round:
        x_0_i = x_0_ij
        inv_x_0_i = inv_x_0_ij
    x_0_k = x_0_i


    x_q = x_0_k
    999;    output4debug_((('[[xx%p =!= 0][k>=2]]: x_q@(x%p**k) = ???', x_q), fnm_params))


    xs_q = _iter_sqrts_mod_prime_power__coprime__5one_sqrt_(fnm_params, output4debug_, p, k, q, x_q, pks)
    '...+O(k * log2(p))'
    #yield from xs_q
    return xs_q

def _iter_sqrts_mod_prime_power__coprime__5one_sqrt_(fnm_params, output4debug_, p, k, q, x_q, may_pks, /):
    # [k >= 1]
    if k == 1:
        #call from another place
        assert fnm_params is ...
        assert output4debug_ is _dummy_output4debug_
            #==>> not call output4debug_()
        if p == 2:
            xs_q = [x_q]
            return iter(xs_q)
        # [[k == 1][p=!=2]]
        pass
    else:
        # [k >= 2]
        pass
    # [[k >= 2]or[[k >= 1][p=!=2]]]

    if p == 2:
        # [k >= 2][p==2]
        # [[[k == 2][xx%4 == 1]] or [[k >= 3][xx%8 == 1]]]
        if k < 4:
            # [2 <= k < 4]
            # [[[k == 2][xx%4 == 1]] or [[k >= 3][xx%8 == 1]]]
            if k == 2:
                # [k == 2][xx%4 == 1]
                999;    output4debug_(('[[[xx%p =!= 0][k==2][p == 2][xx%4 == 1]] -> [sqrts_mod__prime_power__coprime_(p**k;xx) == {1,3}]]', fnm_params))
                xs_q = [1, 3]
            elif k == 3:
                # [k == 3][xx%8 == 1]
                999;    output4debug_(('[[[xx%p =!= 0][k==3][p == 2][xx%8 == 1]] -> [sqrts_mod__prime_power__coprime_(p**k;xx) == {1,3,5,7}]]', fnm_params))
                xs_q = [1, 3, 5, 7]
            else:
                raise 000
            return iter(xs_q)
        # [k >= 4][p==2][xx%8 == 1]
        pass
    else:
        # [k >= 1][p=!=2]
        pass
    # [[k >= 4]or[[p=!=2][k >= 1]]]
    assert k >= 4 or (p > 2 and k >= 1)

    w_q = q -x_q
    if w_q < x_q:
        x_q, w_q = w_q, x_q
    # [[k >= 4]or[[p=!=2][k >= 1]]]
    if p==2:
        # [p==2][k >= 4]
        # !! [k >= 4]
        # 4 solutions

        #s_q = x_q ^ pks[k-1]
        if may_pks is None:
            p__k_neg1 = 1 << (k-1)
        else:
            pks = may_pks
            p__k_neg1 = pks[k-1]
        p__k_neg1

        s_q = x_q ^ p__k_neg1
        #m_q = q -s_q
        m_q = w_q ^ p__k_neg1
        if m_q < x_q:
            x_q, m_q, s_q, w_q = m_q, x_q, w_q, s_q
        xs_q = [x_q, m_q, s_q, w_q]

        999;    output4debug_(('[[[xx%p =!= 0][k>=4][p==2][found one x_q]] -> [sqrts_mod__prime_power__coprime_(p**k;xx) == {x_q, q-x_q, x_q .^. (q///2), (q-x_q) .^. (q///2)}]]', fnm_params))
    else:
        # [p=!=2][k >= 1]
        # 2 solutions
        xs_q = [x_q, w_q]
        if fnm_params is ...:
            #call from another place
            #==>> not call output4debug_()
            #assert k >= 1
            pass
        else:
            assert k >= 2
            999;    output4debug_(('[[[xx%p =!= 0][k>=2][p=!=2][found one x_q]] -> [sqrts_mod__prime_power__coprime_(p**k;xx) == {x_q, q-x_q}]]', fnm_params))
    xs_q

    assert len(xs_q) == (4 if p==2 else 2)
    #xs_q.sort()

    return iter(xs_q)
    #yield from xs_q
    return

def inv_mod_power__coprime_(m, k, x, /, *, may___known__k__inv=None):
    'm -> k -> x -> inv_x/uint%m**k # [[m >= 2][k >= 1][gcd(m,x)==1][x*inv_x %m**k == 1]] #[O((k**3 + log2(m))*log2(m)**2)]'
    m, k, x
    check_type_is(int, m)
    check_type_is(int, k)
    check_type_is(int, x)

    if not m >= 2: raise ValueError(m)
    if not k >= 1: raise ValueError((i, j))
    if not may___known__k__inv is None:
        knowns = may___known__k__inv
        check_type_is(tuple, knowns)
        if not len(knowns) == 2: raise ValueError
        kt, inv_x_0_kt = may___known__k__inv
        check_type_is(int, kt)
        check_type_is(int, inv_x_0_kt)
        if not kt >= 1: raise ValueError(kt)


    if not may___known__k__inv is None:
        if k <= kt:
            if k == kt:
                inv_x_M = inv_x_0_kt
            else:
                M = m**k
                inv_x_M = inv_x_0_kt %M
            return inv_x_M
        # [1 <= kt < k]
    # [[not$ may___known__k__inv is None] -> [1 <= kt < k]]



    x0 = x

    if not may___known__k__inv is None:
        # [1 <= kt < k]
        i = kt
        inv_x_0_i = inv_x_0_kt
    else:
        x_m = x0 %m
        inv_x_m = inv_mod__coprime_(m, x_m)
        # !! gcd ~ log2(m) steps
        # ...+O(log2(m)**3)
        '...+O(log2(m)**3)'
        x_0_1 = x_m
        inv_x_0_1 = inv_x_m

        i = 1
        #x_0_i = x_0_1
        inv_x_0_i = inv_x_0_1
    #i, x_0_i, inv_x_0_i
    i, inv_x_0_i


    if k == 1:
        # !! [[not$ may___known__k__inv is None] -> [1 <= kt < k]]
        if not may___known__k__inv is None:
            raise 000
        return inv_x_m


    ks = _decompose__half_down_(i, k)
    #ks = _decompose__greedy_(k)
    mks = _prepare_p_pows__half_down_(m, ks)
    # !! [O(_prepare_p_pows__half_down_(m;k) == O(k**2 *log2(m)**2)]
    '...+O(k**2 * log2(m)**2)'
    M = mks[k]
    x_M = x0 %M
    if x_M == 1 or x_M +1 == M:
        return x_M

    x_ds = [*uint2radix_repr(m, x_M, is_big_endian=True, imay_max_len=k)]
    x_ds.reverse()
    if len(x_ds) < k:
        x_ds += [0]*(k-len(x_ds))
    assert len(x_ds) == k


    if not may___known__k__inv is None:
        #x_0_i = x_M %pks[i]
        x_0_i = radix_repr2uint(m, x_ds[0:i], is_big_endian=False)
    else:
        x_0_i = x_0_1
    x_0_i

    ######################
    #x_m # [x_m == x%m]
    #inv_x_m # [inv_x_m*x_m %m == 1]
    i, x_0_i, inv_x_0_i # [x_0_i == x%m**i][inv_x_0_i*x_0_i %m**i == 1]
    ks # == _decompose__half_down_(i, k)
    mks # [mks[i] == m**i]
    M # == m**k
    x_M # == x%m**k
    x_ds #  x%m**k --> little-endian radix-m number
    ######################
    fnm_params = ...
    output4debug_ = _5may_output4debug_(None)


    #i = (1|kt) # = ks[0]
    x_0_i
        # x_ds[0:i]
    inv_x_0_i
        # inv_mod_$ x_ds[0:i]
    for i, ij in pairwise(ks):
        # [i >= ks[0] == 1]
        # [inv_x_0_i == inv_mod_(m**i, x_0_i)]
        j = ij - i
        assert 1 <= j <= i
        x_i_ij = radix_repr2uint(m, x_ds[i:ij], is_big_endian=False)
            # x_ds[0:i+j]
        #(x_0_i, x_i_ij, inv_x_0_i) --> inv_x_i_ij
        m_i = mks[i]
        m_j = mks[j]
        (inv_x_i_ij, inv_x_0_ij) = _upgrade__inv_mod_power__coprime_(fnm_params, output4debug_, m, i, j, x_0_i, x_i_ij, inv_x_0_i, m_i, m_j)
        '...+O(i**2 * log2(m)**2)'
        x_0_ij = x_0_i + x_i_ij*m_i

        inv_x_0_ij
        x_0_ij
        ######################
        #next round:
        x_0_i = x_0_ij
        inv_x_0_i = inv_x_0_ij
    '...+O(k**3 * log2(m)**2)'
    inv_x_0_k = inv_x_0_i


    inv_x_M = inv_x_0_k
    return inv_x_M
#end-def inv_mod_power__coprime_(m, k, x, /):


def upgrade__inv_mod_power__coprime_(m, i, j, x_0_i, x_i_ij, inv_x_0_i, m_i, m_j, /):
    r'''[[[
    'm -> i -> j -> x_0_i -> x_i_ij -> inv_x_0_i -> m_i -> m_j -> (inv_x_i_ij, inv_x_0_ij) # [[m >= 2][1 <= j <= i][m_i == m**i][m_j == m**j][0 < *_0_i < m**i][0 <= *_i_ij < m**j][0 <= *_0_ij < m**(i+j)]]'


    O(i**2 * log2(p)**2)

    ######################
    [inv_x_0_i =[def]= inv_mod_(m**i; x_0_i)]
    [inv_x_0_ij =[def]= inv_mod_(m**(i+j); x_0_ij)]
    ######################
    known:  i, j, x_0_i, x_i_ij, inv_x_0_i
    unknown: inv_x_i_ij
    ######################
    constraints:
    [m >= 2]
    [gcd(m, x_0_i) == 1]

    [1 <= j <= i]
    [x_0_i*inv_x_0_i %m**i == 1]
    [x_0_ij*inv_x_0_ij %m**(i+j) == 1]
    [m_i == m**i]
    [m_j == m**j]
    [0 < x_0_i < m**i]
    [0 < inv_x_0_i < m**i]
    [0 <= x_i_ij < m**j]
    [0 <= inv_x_i_ij < m**j]

    [x_0_ij == x_0_i + x_i_ij*m**i]
    [inv_x_0_ij == inv_x_0_i + inv_x_i_ij*m**i]
    [0 <= x_0_ij < m**(i+j)]
    [0 <= inv_x_0_ij < m**(i+j)]
    ######################

    #]]]'''#'''
    m, i, j, x_0_i, x_i_ij, inv_x_0_i, m_i, m_j
    check_type_is(int, m)
    check_type_is(int, i)
    check_type_is(int, j)
    check_type_is(int, x_0_i)
    check_type_is(int, x_i_ij)
    check_type_is(int, inv_x_0_i)
    check_type_is(int, m_i)
    check_type_is(int, m_j)

    if not m >= 2: raise ValueError(m)
    if not 1 <= j <= i: raise ValueError((i, j))

    if not 0 < x_0_i < m_i: raise ValueError((x_0_i, m_i))
    if not 0 <= x_i_ij < m_j: raise ValueError((x_i_ij, m_j))
        # 『0 <=』
    if not 0 < inv_x_0_i < m_i: raise ValueError((inv_x_0_i, m_i))


    fnm_params = ...
    output4debug_ = _5may_output4debug_(None)

    (inv_x_i_ij, inv_x_0_ij) = _upgrade__inv_mod_power__coprime_(fnm_params, output4debug_, m, i, j, x_0_i, x_i_ij, inv_x_0_i, m_i, m_j)

    return (inv_x_i_ij, inv_x_0_ij)
def _upgrade__inv_mod_power__coprime_(fnm_params, output4debug_, p, i, j, x_0_i, x_i_ij, inv_x_0_i, p_i, p_j, /):
    r'''[[[
    -> (inv_x_i_ij, inv_x_0_ij)

    O(i**2 * log2(p)**2)
    ######################
    [inv_x_i_ij == (inv_x_0_i %p**j)*(p**j - ((x_0_i*inv_x_0_i -1) ///p**i %p**j + (inv_x_0_i %p**j)*x_i_ij %p**j)) %p**j]
    <<==:
    ######################


    ######################
    [inv_x_0_i =[def]= inv_mod_(p**i; x_0_i)]
    [inv_x_0_ij =[def]= inv_mod_(p**(i+j); x_0_ij)]
    ######################
    known:  i, j, x_0_i, x_i_ij, inv_x_0_i
    unknown: inv_x_i_ij
    ######################
    constraints:
    [1 <= j <= i]
    [x_0_i*inv_x_0_i %p**i == 1]
    [x_0_ij*inv_x_0_ij %p**(i+j) == 1]
    [p_i == p**i]
    [p_j == p**j]
    [0 < x_0_i < p**i]
    [0 < inv_x_0_i < p**i]
    [0 <= x_i_ij < p**j]
    [0 <= inv_x_i_ij < p**j]

    [x_0_ij == x_0_i + x_i_ij*p**i]
    [inv_x_0_ij == inv_x_0_i + inv_x_i_ij*p**i]
    [0 <= x_0_ij < p**(i+j)]
    [0 <= inv_x_0_ij < p**(i+j)]
    ######################
    !! [x_0_ij*inv_x_0_ij %p**(i+j) == 1]
    !! [x_0_ij == x_0_i + x_i_ij*p**i]
    !! [inv_x_0_ij == inv_x_0_i + inv_x_i_ij*p**i]
    [(x_0_i + x_i_ij*p**i)*(inv_x_0_i + inv_x_i_ij*p**i) %p**(i+j) == 1]
    [1
    == (x_0_i + x_i_ij*p**i)*(inv_x_0_i + inv_x_i_ij*p**i) %p**(i+j)
    !! [1 <= j <= i]
    == (x_0_i*inv_x_0_i + inv_x_0_i*x_i_ij*p**i + x_0_i*inv_x_i_ij*p**i) %p**(i+j)
    == ((x_0_i*inv_x_0_i) %p**(i+j) + (inv_x_0_i*x_i_ij*p**i + x_0_i*inv_x_i_ij*p**i) %p**(i+j)) %p**(i+j)
    == ((x_0_i*inv_x_0_i) %p**(i+j) + (inv_x_0_i*x_i_ij + x_0_i*inv_x_i_ij) %p**j *p**i) %p**(i+j)
    ]
    !! [x_0_i*inv_x_0_i %p**i == 1]
    [0
    == ((x_0_i*inv_x_0_i -1) %p**(i+j) + (inv_x_0_i*x_i_ij + x_0_i*inv_x_i_ij) %p**j *p**i) %p**(i+j) ///p**i
    == ((x_0_i*inv_x_0_i -1) ///p**i %p**j + inv_x_0_i*x_i_ij %p**j + x_0_i*inv_x_i_ij %p**j) %p**j
    ]
    [x_0_i*inv_x_i_ij %p**j == p**j - ((x_0_i*inv_x_0_i -1) ///p**i %p**j + inv_x_0_i*x_i_ij %p**j) %p**j]
    [(x_0_i %p**j)*inv_x_i_ij %p**j == p**j - ((x_0_i*inv_x_0_i -1) ///p**i %p**j + (inv_x_0_i %p**j)*x_i_ij %p**j) %p**j]
    ==>>:
    [inv_x_i_ij == (inv_x_0_i %p**j)*(p**j - ((x_0_i*inv_x_0_i -1) ///p**i %p**j + (inv_x_0_i %p**j)*x_i_ij %p**j)) %p**j]
    ######################
    #]]]'''#'''

    inv_x_0_j = (inv_x_0_i %p_j)

    [inv_x_i_ij := inv_x_0_j*(p_j - ((x_0_i*inv_x_0_i -1) //p_i %p_j + inv_x_0_j*x_i_ij %p_j)) %p_j]
    '...+O(i**2 * log2(p)**2)'

    inv_x_0_ij = inv_x_0_i + inv_x_i_ij*p_i
    return (inv_x_i_ij, inv_x_0_ij)
#end-def _upgrade__inv_mod_power__coprime_(fnm_params, output4debug_, p, i, j, x_0_i, x_i_ij, inv_x_0_i, p_i, p_j, /):










#def upgrade__sqrt_mod_prime_power__coprime_
def _upgrade__sqrt_mod_prime_power__coprime_(fnm_params, output4debug_, p, i, j, x_0_i, xx_i_ij, pks, may_inv_x_0_i, validate, /):
    r'''[[[
    [xx%p=!=0][1 <= j <= i][is_square_residual_mod(p**(i+j);xx)]:
    -> (_may_inv_x_0_i, _x_0_i, x_i_ij, x_0_ij)

    [may_inv_x_0_i is None]:
        #xxx O(i**3 * log2(p)**3)
        O((i**3 + log2(p))*log2(p)**2)
    [not$ may_inv_x_0_i is None]:
        O(i**2 * log2(p)**2)

    [1 <= j <= i]
    requirements<pks>:
        * [p=!=2]:
            pks[i]
            pks[j]
        * [p==2]:
            pks[i]
            [i >= 3]:
                pks[i-1]
                pks[i-2]
            pks[j]
            pks[j-1] # pks[0] if j==1

    #]]]'''#'''
    #(xx_0_i, xx_i_ij, x_0_i) --> x_i_ij
    #   implicit:xx_0_i
    ij = i+j
    999;    output4debug_((('[[xx%p =!= 0][k>=2]]: (i, ij@(i+j), j, x_0_i@x%p**i, implicit:xx_0_i@(xx%p**i), xx_i_ij@(xx%p**(i+j)//p**i)) = ???', (i, ij, j, x_0_i, ..., xx_i_ij)), fnm_params))
    r'''[[[
    ######################
    known: xx_0_i/implicit, xx_i_ij
    known: x_0_i
    unknown: x_i_ij
    ######################
    #constraints:
    [0 < j <= i < i+j == ij <= 2*i]
    [xx_0_i == x_0_i**2%p**i]
    [(xx_0_i+xx_i_ij*p**i) == (x_0_i+x_i_ij*p**i)**2%p**ij]
    ######################
    [(xx_0_i+xx_i_ij*p**i) == (x_0_i**2+2*x_0_i*x_i_ij*p**i)%p**ij]
    [(xx_0_i+xx_i_ij*p**i) //p**i == (x_0_i**2+2*x_0_i*x_i_ij*p**i)%p**ij //p**i]
    [xx_i_ij == (x_0_i**2 //p**i+2*x_0_i*x_i_ij)%p**j]
    [xx_i_ij -(x_0_i**2 //p**i) =[%p**j]= 2*x_0_i*x_i_ij]
    [lhs := xx_i_ij -(x_0_i**2 //p**i) %p**j]
    solve:[lhs =[%p**j]= 2*x_0_i*x_i_ij]
    !! [xx%p =!= 0]
    [x_0_i%p =!= 0]
    * [p%2 == 1]:
        !! [2%p =!= 0]
        !! [x_0_i%p =!= 0]
        [(2*x_0_i)%p =!= 0]
        [x_i_ij == lhs *inv_mod_(p**j;2*x_0_i) %p**j]
    * [p == 2]:
        [[:proof: [[lhs%2 == 1] -> [i >= 3]]
        [[lhs%2 == 1] -> [x_0_i <-!- sqrts_mod_(2**(i+j);xx) %2**i]]
            #cannot upgrade from x_0_i
        #but:
        !! [1 <= j <= i]
        * [i==1][j==1]:
            !! [xx%p=!=0][is_square_residual_mod(p**(i+j);xx)]
            [xx%4==1]
            [xx_0_i == 1][xx_i_ij == 0]
            [x_0_i == 1]
            [x_0_i <- {1} == {1,3}%2 == sqrts_mod_(4;1) %2**1]
            [x_0_i <- sqrts_mod_(2**(i+j);xx) %2**i]
        * [i==2][j==1]:
            !! [xx%p=!=0][is_square_residual_mod(p**(i+j);xx)]
            [xx%8==1]
            [xx_0_i == 1][xx_i_ij == 0]
            [x_0_i <- {1,3}]
            [x_0_i <- {1,3} == {1,3,5,7}%4 == sqrts_mod_(8;1) %2**2]
            [x_0_i <- sqrts_mod_(2**(i+j);xx) %2**i]
        * [i==2][j==2]:
            !! [xx%p=!=0][is_square_residual_mod(p**(i+j);xx)]
            [xx%8==1]
            [xx%16 <- {1,9}]
            [xx_0_i == 1][xx_i_ij <- {0,2}]
            [x_0_i <- {1,3}]
            * [xx%16 == 1]:
                [x_0_i <- {1,3} == {1,7,9,15}%4 == sqrts_mod_(16;1) %2**2]
            * [xx%16 == 9]:
                [x_0_i <- {1,3} == {3,5,11,13}%4 == sqrts_mod_(16;9) %2**2]
            [x_0_i <- sqrts_mod_(2**(i+j);xx) %2**i]
        [[i < 3] -> [x_0_i <- sqrts_mod_(2**(i+j);xx) %2**i]]
        !! [[lhs%2 == 1] -> [x_0_i <-!- sqrts_mod_(2**(i+j);xx) %2**i]]
        [[lhs%2 == 1] -> [i >= 3]]
        DONE
        ]]

        * [lhs%2 == 1]:
            !! [[lhs%2 == 1] -> [i >= 3]]
            [i >= 3]
            no solution!
            but change (x_0_i += 2**(i-1)) ==>> [lhs%2 == 0]
            !! [lhs := xx_i_ij -(x_0_i**2 //p**i) %p**j]
            [_lhs := xx_i_ij -((x_0_i+2**(i-1))**2 //p**i) %p**j]
            [_lhs
            == xx_i_ij -((x_0_i**2 +2**(2*i-2) +2*x_0_i*2**(i-1)) //p**i) %p**j
            !! [i >= 3]
            [2*i-2>=i+1]
            [i-2>=1]
            == xx_i_ij -((x_0_i**2 +2**(2*i-2) +2*x_0_i*2**(i-1)) //p**i) %p**j
            == lhs -((2**(2*i-2) +2*x_0_i*2**(i-1)) //p**i) %p**j
            == lhs -(2**(i-2) +x_0_i) %p**j
            =[%2]= lhs%2 -(2**(i-2) +x_0_i) %p**j %2
            !! [j >= 1]
            =[%2]= lhs%2 -(2**(i-2) +x_0_i) %2
            !! [x_0_i%2==1]
            =[%2]= lhs%2 +1 -(2**(i-2)) %2
            !! [i-2>=1]
            =[%2]= lhs%2 +1
            !! [lhs%2 == 1]
            =[%2]= 0
            ]
            assert [i >= 3]
            [_x_0_i := x_0_i + 2**(i-1)]
            [_lhs == lhs -(2**(i-2) +x_0_i) %p**j]
            [_lhs =[%2]= lhs%2 +1 =[%2]= 0]
        * [lhs%2 == 0]:
            [lhs///2 =[%p**(j-1)]= x_0_i*x_i_ij]
            [x_i_ij =[%p**(j-1)]= lhs///2 *inv_mod_(p**(j-1);x_0_i) %p**(j-1)]
            [x_i_ij //p**(j-1) <- {0,1}]
            two solution!

    ===
    {1,3,5,7}**2 %8 == 1
    {1,7,9,15}**2 %16 == 1
    {1,15,17,31}**2 %32 == 1
    ===
    {1,15,17,31}%8 = {1,7} #{3,5} dropped
    {1,15,17,31}%16 = {1,15} #7,9} dropped
    ===
    {1,7,9,15} %8 == {1,7} #{3,5} dropped
    ===
    1 --> {1,9}
        9 --> {}
        1 --> {1,17}
            17 --> {}
            1 --> {1,33}
    ===
    * [p > 2]:
        2 solutions
        {x_q, q-x_q}
    * [p == 2]:
        * [k==1]:
            1 solution
            {1}
        * [k==2]:
            2 solutions
            {1,3}
        * [k>=3]:
            4 solutions
            {x_q, q///2-x_q, q///2+x_q, q-x_q}
            proof:
            * [([+-]x_q +k*q///2) are solutions]
            [([+-]x_q +k*q///2)**2
            == x_q**2 +2*k*q///2 +(k*q///2)**2
            !! [k>=3]
            [q///2 % 2 == 0]
            [(q///2)**2 % q == 0]
            =[%q]= x_q**2
            =[%q]= xx_q
            =[%q]= xx
            ]
            * ==>>
            * [solutions must be ([+-]x_q +t*q///2)]
            [w_q**2 =[%q]= x_p**2]:
                [(w_q-x_q)*(w_q+x_q) %q == 0]
                !! [x_q**2 =[%q]= xx]
                !! [xx%2 =!= 0]
                [x_q is odd]
                [w_q is odd]
                [u,n <- {0,1}][u =!= n]
                * [{x_q,w_q} == {0byyyuuuaaa1, 0bzzznnnaaa1}]:
                    [x_q-w_q == 0bxxxxxx0000]
                    [x_q+w_q == 0bxxxxxxxxx10]
                    ==>>:
                    [(x_q-w_q)%2**(k-1)==0]
                    [w_q == x_q + +t*q///2]
                * [{x_q,w_q} == {0byyyuuu1, 0bzzznnn1}]:
                    [x_q-w_q == 0bxxxxxxxxx10]
                    [x_q+w_q == 0bxxxxxx0000]
                    ==>>:
                    [(x_q+w_q)%2**(k-1)==0]
                    [w_q == -x_q + +t*q///2]



    ######################
    # upgrade-ver of inv_mod_
    ######################
    * [p=!=2]:
        x_i_ij = lhs *inv_mod_(pks[j], x_0_i<<1) % pks[j]
        ###########
        inv_mod_(p**j; 2*x_0_i)
        <--
        inv_mod_(p**i; 2*x_0_i)
        --> inv_mod_(p**(i+j); 2*x_0_ij)
    * [p==2]:
        x_i_ij___MSB0 = lhs//2 *inv_mod_(pks[j-1], x_0_i) %pks[j-1]
        ###########
        inv_mod_(2**(j-1); x_0_i)
        <--
        inv_mod_(2**i; x_0_i)
        --> inv_mod_(2**(i+j); x_0_ij)
    ######################
    [inv_x_0_i =[def]= inv_mod_(p**i; x_0_i)]
    [inv_x_0_ij =[def]= inv_mod_(p**(i+j); x_0_ij)]
    ######################
    known:  i, j, x_0_i, x_0_ij, inv_x_0_i
        <==> known:  i, j, x_0_i, x_i_ij, inv_x_0_i
    unknown: inv_x_0_ij
        <==> unknown: inv_x_i_ij
    ######################
    see:_upgrade__inv_mod_power__coprime_
    ######################
    #]]]'''#'''
    x_0_i
    [lhs :=  (xx_i_ij -(x_0_i**2 //pks[i] % pks[j])) % pks[j]]
    '...+O(i**2 * log2(p)**2)'
    999;    output4debug_((('[[xx%p =!= 0][k>=2]]: (i, ij, j, x_0_i, xx_i_ij) : lhs@((xx_i_ij -(x_0_i**2 //p**i % p**j)) % p**j) = ???', lhs), fnm_params))

    x_0_i__changed = False
    saved = may_inv_x_0_i, x_0_i

    p_i = pks[i]
    p_j = pks[j]
    if not p == 2:
        # [p=!=2]
        #x_i_ij = lhs *inv_mod__coprime_(pks[j], x_0_i<<1) % pks[j]
        if may_inv_x_0_i is None:
            x_0_j = x_0_i %p_j
            if 0:
                inv_double_x_0_j = inv_mod__coprime_(pks[j], x_0_j<<1)
                # !! gcd ~ log2(p**j) steps
                '...+O(i**3 * log2(p)**3)'
            else:
                inv_double_x_0_j = inv_mod_power__coprime_(p, j, x_0_j<<1)
                '...+O((i**3 + log2(p))*log2(p)**2)'
        else:
            inv_x_0_i = may_inv_x_0_i
            inv_x_0_j = inv_x_0_i %p_j
            '...+O(i**2 * log2(p)**2)'
            # [2 * (p_i+1)///2 %p_i == 1]
            # [inv_mod_(p_i;2) == (p_i+1)///2]
            # [inv_mod_(p_i;2*t) == inv_mod_(p_i;2) *inv_mod_(p_i;t) %p_i == (p_i+1)///2 * inv_t %p_i]
            # [[inv_t==2*s] -> [(p_i+1)///2 * inv_t %p_i == s %p_i]]
            # [[inv_t==2*s+1] -> [(p_i+1)///2 * inv_t %p_i == ((p_i+1)///2 +s) %p_i]]
            s = inv_x_0_j >> 1
            if inv_x_0_j&1:
                inv_double_x_0_j = ((p_j+1)//2 +s) %p_j
                '...+O(i**2 * log2(p)**2)'
            else:
                inv_double_x_0_j = s
            inv_double_x_0_j
        inv_double_x_0_j
        x_i_ij = lhs *inv_double_x_0_j % p_j
        '...+O(i**2 * log2(p)**2)'
        999;    output4debug_((('[[xx%p =!= 0][k>=2][p=!=2]]: (i, ij, j, x_0_i, xx_i_ij, lhs) : x_i_ij@(lhs *inv_mod_(p**j; 2*x_0_i) % p**j) = ???', x_i_ij), fnm_params))
    else:
        # [p==2]
        if lhs&1:
            # no solution
            # solve:see above _lhs
            # assert [i >= 3]
            # [_x_0_i := x_0_i + 2**(i-1)]
            # [_lhs == lhs -(2**(i-2) +x_0_i) %p**j]
            # [_lhs =[%2]= lhs%2 +1 =[%2]= 0]
            if not i >= 3:
                # check constraints<input>
                _check4upgrade_sqrt_mod_(p, i, j, x_0_i, xx_i_ij, p_i, p_j, may_inv_x_0_i=may_inv_x_0_i, strict=True)
                raise Exception(('not i >= 3: logic-err?', (p, i, j, x_0_i, xx_i_ij, p_i, p_j, may_inv_x_0_i)))
            assert i >= 3
            [_x_0_i := x_0_i + pks[i-1]]
            [_lhs := lhs -(pks[i-2] +x_0_i) %pks[j]]
            '...+O(i**2 * log2(p)**2)'
            assert _lhs&1 == 0
            ######################
            x_0_i__changed = True
            x_0_i = _x_0_i
            lhs = _lhs
            999;    output4debug_((('[[xx%p =!= 0][k>=2][p==2][lhs is odd][i>=3]]: (i, ij, j, x_0_i, xx_i_ij, lhs) : reset (x_0_i@(x_0_i<old> + 2**(i-1)), lhs@(lhs<old> -(2**(i-2) +x_0_i<old>) %2**j)) = ???', (x_0_i, lhs)), fnm_params))
        assert lhs&1 == 0
        # two solution
        # pick arbitrary one
        if 0:
            x_i_ij___MSB0 = lhs//2 *inv_mod__coprime_(pks[j-1], x_0_i) %pks[j-1]
            if not i==1:
                x_i_ij___MSB1 = x_i_ij___MSB0 | pks[j-1]
        p_jmm = pks[j-1]
        if may_inv_x_0_i is None:
            x_0_jmm = x_0_i %p_jmm
            inv_x_0_jmm = inv_mod__coprime_(p_jmm, x_0_jmm)
        else:
            inv_x_0_i = may_inv_x_0_i
            inv_x_0_jmm = inv_x_0_i %p_jmm
        inv_x_0_jmm
        # !! [j-1 < j <= i]
        # [no matter MSB changed or not, inv_x_0_jmm is correct]
        x_i_ij___MSB0 = lhs//2 *inv_x_0_jmm %p_jmm
        #x_i_ij___MSB0 = lhs//2 *inv_mod__coprime_(pks[j-1], x_0_i) %pks[j-1]
        x_i_ij = x_i_ij___MSB0
        999;    output4debug_((('[[xx%p =!= 0][k>=2][p==2][lhs is even]]: (i, ij, j, x_0_i, xx_i_ij, lhs) : x_i_ij@(lhs///2 *inv_mod_(2**(j-1), x_0_i) %2**(j-1)) = ???', x_i_ij), fnm_params))
        if x_0_i__changed and x_0_i > p_i:
            x_0_i ^= p_i
            x_i_ij += 1
                # x_i_ij is x_i_ij___MSB0, this "+" cannot overflow
            assert 0 < x_0_i < p_i
            assert 0 < x_i_ij <= p_jmm < p_j
            # [0 < x_0_i < p**i]
            # [0 < x_i_ij < p**j]
            #   『0 <』vs below 『0 <=』

            # now x_i_ij may become MSB1
            if x_i_ij == p_jmm:
                x_i_ij = 0
            assert 0 <= x_i_ij < p_jmm

        if x_0_i__changed:
            999;    output4debug_((('[[xx%p =!= 0][k>=2][p==2][x_0_i__changed]]: (i, ij, j) : (x_0_i, x_i_ij) = ???', (x_0_i, x_i_ij)), fnm_params))
        # [0 < x_0_i < p**i]
        # [0 <= x_i_ij < p**j]
    x_0_i
    x_i_ij
    assert 0 < x_0_i < p_i
    assert 0 <= x_i_ij < p_j
    # [0 < x_0_i < p**i]
    # [0 <= x_i_ij < p**j]

    x_0_ij = x_0_i + x_i_ij*pks[i]
    '...+O(i**2 * log2(p)**2)'
    999;    output4debug_((('[[xx%p =!= 0][k>=2]]: (i, ij, j, x_0_i, xx_i_ij, lhs, x_i_ij) : x_0_ij@(x_0_i + x_i_ij*p**i) = ???', x_0_ij), fnm_params))

    if x_0_i__changed:
        if may_inv_x_0_i is None:
            _may_inv_x_0_i = may_inv_x_0_i
        else:
            inv_x_0_i = may_inv_x_0_i
            _inv_x_0_i = inv_x_0_i ^ pks[i-1]
            _may_inv_x_0_i = _inv_x_0_i
        _may_inv_x_0_i
        may_inv_x_0_i = _may_inv_x_0_i
    may_inv_x_0_i #may be updated
    _may_inv_x_0_i, _x_0_i = may_inv_x_0_i, x_0_i
    may_inv_x_0_i, x_0_i = saved



    may_inv_x_0_i, x_0_i
    _may_inv_x_0_i, _x_0_i
    x_i_ij, x_0_ij

    if validate:
        _validate4upgrade_sqrt_mod_(p, i, j, x_0_i, xx_i_ij, p_i, p_j, may_inv_x_0_i, _may_inv_x_0_i, _x_0_i, x_i_ij, x_0_ij)
    #xxx:return (x_i_ij, x_0_ij)
    return (_may_inv_x_0_i, _x_0_i, x_i_ij, x_0_ij)
        #why return (may_inv_x_0_i, x_0_i, ...)? <<== since x_0_i/may_inv_x_0_i may be changed
#end-def _upgrade__sqrt_mod_prime_power__coprime_(fnm_params, output4debug_, p, i, j, x_0_i, xx_i_ij, pks, may_inv_x_0_i, validate, /):




def upgrade__sqrt_mod_odd_prime_power__coprime_(p, i, j, x_0_i, xx_i_ij, p_i, p_j, /, *, may_inv_x_0_i=None, validate=False):
    'p -> i -> j -> x_0_i -> xx_i_ij -> p_i -> p_j -> x_0_ij # [[p is prime][p%2 == 1][xx%p =!= 0][i+j <= k][xx%p**k == x**2%p**k][1 <= j <= i][p_i == p**i][p_j == p**j][x_0_i == x%p**i][xx_i_ij == (xx%p**(i+j)//p**i)][x_0_ij == x%p**(i+j)][xx%p**(i+j) == x_0_ij**2%p**(i+j)]]'
    check_type_is(int, p)
    if not p >= 3: raise ValueError(p)
    if not (p&1) == 1: raise ValueError(p)
    x_0_ij = upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime_(p, i, j, x_0_i, xx_i_ij, p_i, p_j, may_inv_x_0_i=may_inv_x_0_i, validate=validate)
    return x_0_ij






def upgrade_or_after_flip_MSB__sqrt_mod_2_power__coprime_(i, j, x_0_i, xx_i_ij, p_i, p_j, /, *, may_inv_x_0_i=None, validate=False):
    'i -> j -> x_0_i -> xx_i_ij -> p_i -> p_j -> x_0_ij # [[p == 2][xx%p =!= 0][i+j <= k][xx%p**k == x**2%p**k][1 <= j <= i][p_i == p**i][p_j == p**j][0 <= x_0_i < 2**i][x_0_i%2**(i-1) == x%2**(i-1)][xx_i_ij == (xx%p**(i+j)//p**i)][0 <= x_0_ij < 2**(i+j)][x_0_ij%2**(i+j-1) == x%2**(i+j-1)]][xx%p**(i+j) == x_0_ij**2%p**(i+j)]'
    x_0_ij = upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime_(2, i, j, x_0_i, xx_i_ij, p_i, p_j, may_inv_x_0_i=may_inv_x_0_i, validate=validate)
    return x_0_ij








def upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime_(p, i, j, x_0_i, xx_i_ij, p_i, p_j, /, *, may_inv_x_0_i=None, validate=False):
    r'''[[[
    'p -> i -> j -> x_0_i -> xx_i_ij -> p_i -> p_j -> x_0_ij # [[p is prime][xx%p =!= 0][i+j <= k][xx%p**k == x**2%p**k][1 <= j <= i][p_i == p**i][p_j == p**j][xx_i_ij == (xx%p**(i+j)//p**i)][xx%p**(i+j) == x_0_ij**2%p**(i+j)][[p%2==1] -> [[x_0_i == x%p**i][x_0_ij == x%p**(i+j)]]][[p==2] -> [[0 <= x_0_i < 2**i][x_0_i%2**(i-1) == x%2**(i-1)][0 <= x_0_ij < 2**(i+j)][x_0_ij%2**(i+j-1) == x%2**(i+j-1)]]]]'


    [may_inv_x_0_i is None]:
        O((i**3 + log2(p))*log2(p)**2)
    [not$ may_inv_x_0_i is None]:
        O(i**2 * log2(p)**2)


    #]]]'''#'''

    (_may_inv_x_0_i, _x_0_i, x_i_ij, x_0_ij) = upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime__ex_(p, i, j, x_0_i, xx_i_ij, p_i, p_j, may_inv_x_0_i=may_inv_x_0_i, validate=validate)
    return x_0_ij






class Error(Exception):pass
class Error__not_prime_number(Error):pass
class Error__not_coprime(Error):pass
class Error__not_square_residual_mod(Error):pass
class Error__not_inv_mod(Error):pass
class Error__not_flip_MSB(Error):pass
class Error__not_p_eq2_and_i_ge3(Error):pass
class Error__not_sqrt_mod(Error):pass

def _validate4upgrade_sqrt_mod_(p, i, j, x_0_i, xx_i_ij, p_i, p_j, may_inv_x_0_i, _may_inv_x_0_i, _x_0_i, x_i_ij, x_0_ij, /):
    _check4upgrade_sqrt_mod_(p, i, j, x_0_i, xx_i_ij, p_i, p_j, may_inv_x_0_i=may_inv_x_0_i, strict=True)
    if not _may_inv_x_0_i is None:
        _inv_x_0_i = _may_inv_x_0_i
        check_type_is(int, _inv_x_0_i)
    check_type_is(int, _x_0_i)
    check_type_is(int, x_i_ij)
    check_type_is(int, x_0_ij)

    if not 0 < _x_0_i < p_i: raise ValueError((_x_0_i, p_i))
    if not 0 <= x_i_ij < p_j: raise ValueError((x_i_ij, p_j))
        # "0 <= ..."
    if not x_0_ij == _x_0_i + x_i_ij*p_i: raise ValueError((x_0_ij, _x_0_i, x_i_ij, p_i))

    if not (_may_inv_x_0_i is None) is (may_inv_x_0_i is None): raise ValueError((_may_inv_x_0_i, may_inv_x_0_i))

    if not _may_inv_x_0_i is None:
        inv_x_0_i = may_inv_x_0_i
        if not (_x_0_i is x_0_i) is (_inv_x_0_i is inv_x_0_i): raise ValueError((x_i_ij, p_j))

        if not 1 == inv_x_0_i*x_0_i %p_i: raise Error__not_inv_mod((p, i, x_0_i, inv_x_0_i, p_i))

        if not (_inv_x_0_i is inv_x_0_i):
            if not 1 == _inv_x_0_i*_x_0_i %p_i: raise Error__not_inv_mod((p, i, _x_0_i, _inv_x_0_i, p_i))


    if not ((_x_0_i is x_0_i) or (p==2 and i>=3)):raise Error__not_p_eq2_and_i_ge3((p, i, j, x_0_i, xx_i_ij, _x_0_i))

    if not ((_x_0_i is x_0_i) or (_x_0_i^x_0_i == 1 << (i-1))):raise Error__not_flip_MSB((p, i, x_0_i, _x_0_i))

    if not ((_may_inv_x_0_i is may_inv_x_0_i) or (_inv_x_0_i^inv_x_0_i == 1 << (i-1))):raise Error__not_flip_MSB((p, i, inv_x_0_i, _inv_x_0_i))

    xx_0_i = x_0_i**2%p_i
    xx_0_ij = xx_0_i + xx_i_ij*p_i

    if not ((_x_0_i is x_0_i) or (_x_0_i**2%p_i == xx_0_i)):raise Error__not_sqrt_mod((p, i, x_0_i, _x_0_i))
    if not x_0_ij**2 %(p_i*p_j) == xx_0_ij: raise Error__not_sqrt_mod((p, i, j, x_0_i, xx_i_ij, x_i_ij, x_0_ij))
    return

def _check4upgrade_sqrt_mod_(p, i, j, x_0_i, xx_i_ij, p_i, p_j, /, *, may_inv_x_0_i, strict):
    check_type_is(int, p)
    check_type_is(int, i)
    check_type_is(int, j)
    check_type_is(int, x_0_i)
    check_type_is(int, xx_i_ij)
    check_type_is(int, p_i)
    check_type_is(int, p_j)
    if not may_inv_x_0_i is None:
        inv_x_0_i = may_inv_x_0_i
        check_type_is(int, inv_x_0_i)
    if not p >= 2: raise ValueError(p)
    if not p == 2:
        if not (p&1): raise ValueError(p)
    if not 1 <= j <= i: raise ValueError((i, j))

    if not 0 < x_0_i < p_i: raise ValueError((x_0_i, p_i))
    if not 0 <= xx_i_ij < p_j: raise ValueError((xx_i_ij, p_j))
        # "0 <= ..."

    if not may_inv_x_0_i is None:
        if not 0 < inv_x_0_i < p_i: raise ValueError((inv_x_0_i, p_i))

    if not strict:
        return
    if not p_i == p**i: raise ValueError((p, i, p_i))
    if not p_j == p**j: raise ValueError((p, j, p_j))

    if 0 == detect_strong_pseudoprime__not_waste_too_much_time_(p): raise Error__not_prime_number(p)

    if 0 == x_0_i%p: raise Error__not_coprime((p, x_0_i))

    xx_0_i = x_0_i**2%p_i
    xx_0_ij = xx_0_i + xx_i_ij*p_i
    if not is_square_residual_mod_prime_power_(p, i+j, xx_0_ij): raise Error__not_square_residual_mod((p, i, j, x_0_i, xx_i_ij))

    if not may_inv_x_0_i is None:
        if not 1 == inv_x_0_i*x_0_i %p_i: raise Error__not_inv_mod((p, i, x_0_i, inv_x_0_i, p_i))
    return

def _test_p_eq2_and_i_ge_3___4upgrade_sqrt_mod_():
    p = 2
    for i in range(1, 5):
        p_i = 1<<i
        for j in range(1, i+1):
            # [1 <= j <= i]
            p_j = 1<<j
            #q = p**(i+j)
            q = 1 <<(i+j)
            xx2sqrts = tabulate_sqrts_mod_M_(q)
            for xx in range(1, q, 2):
                # [xx%2==1]
                # coprime xx,2
                xs_q = xx2sqrts[xx]
                if not xs_q:
                    continue
                # [is_square_residual_mod(q;xx)]
                for x_q in xs_q:
                    x_0_i = x_q%p_i
                    xx_i_ij = xx//p_i
                    (_may_inv_x_0_i, _x_0_i, x_i_ij, x_0_ij) = upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime__ex_(p, i, j, x_0_i, xx_i_ij, p_i, p_j, may_inv_x_0_i=None, validate=True)
                    if not _x_0_i is x_0_i:raise 000
                        #can upgrade from x_0_i
                    if not x_0_ij == x_q & (q//2 -1):raise 000
                    #bug:if not x_0_ij == min(x_q, q-x_q):raise 000
                    if not x_0_ij == min(x_q, x_q^(q//2)):raise 000

                    _2_x_0_i = x_0_i^(1 << (i-1))
                        #flip MSB

                    if i==1:
                        assert _2_x_0_i==0
                        continue
                    assert not _2_x_0_i==0
                    (_3_may_inv_x_0_i, _3_x_0_i, _3_x_i_ij, _3_x_0_ij) = upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime__ex_(p, i, j, _2_x_0_i, xx_i_ij, p_i, p_j, may_inv_x_0_i=None, validate=True)
                    if i >= 3:
                        #cannot upgrade from _2_x_0_i, switch back to x_0_i
                        if _3_x_0_i == _2_x_0_i:raise 000
                        if not _3_x_0_i == x_0_i:raise 000
                        if not _3_x_0_ij == x_0_ij:raise Exception(i,j,x_0_ij, _3_x_0_ij) #000
                        if not _3_x_i_ij == x_i_ij:raise 000
                    else:
                        assert i == 2
                        if not _3_x_0_i is _2_x_0_i:raise 000
                            #can upgrade from _2_x_0_i
                        if _3_x_0_i == x_0_i:raise 000
                        if _3_x_0_ij == x_0_ij:raise 000
                        if j==1:
                            if not _3_x_i_ij == x_i_ij == 0:raise 000
                            if not _3_x_0_ij == _2_x_0_i:raise 000
                        else:
                            assert j==2
                            #xx=1 => 1-->1,3-->7
                            #xx=9 => 1-->5,3-->3
                            if not {x_i_ij, _3_x_i_ij} == {0,1}:raise 000



def upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime__ex_(p, i, j, x_0_i, xx_i_ij, p_i, p_j, /, *, may_inv_x_0_i, validate=False):
    r'''[[[
    'p -> i -> j -> x_0_i -> xx_i_ij -> p_i -> p_j -> (_may_inv_x_0_i, _x_0_i, x_i_ij, x_0_ij) # [[p is prime][xx%p =!= 0][i+j <= k][xx%p**k == x**2%p**k][1 <= j <= i][p_i == p**i][p_j == p**j][xx_i_ij == (xx%p**(i+j)//p**i)][xx%p**(i+j) == x_0_ij**2%p**(i+j)][[p%2==1] -> [[x_0_i == x%p**i][x_0_ij == x%p**(i+j)]]][[p==2] -> [[0 <= x_0_i < 2**i][x_0_i%2**(i-1) == x%2**(i-1)][0 <= x_0_ij < 2**(i+j)][x_0_ij%2**(i+j-1) == x%2**(i+j-1)]]]] #[[p==2] -> [i>=2] -> [(may_inv_x_0_i, x_0_i) may be changed]]'



# upgrade vs degrade
#   2**k is not easy to handle
#   upgrade one sqrt may need to flip MSB first
#   degrade all sqrts may need to regenerate all sqrts from one, see:iter_sqrts_mod_prime_power__coprime__5one_sqrt_
#       degrade one sqrt is easy
#       degrade all sqrts via degrade one by one will reduce the size: 4->2 @[k>=4], hence wrong
#

    [may_inv_x_0_i is None]:
        O((i**3 + log2(p))*log2(p)**2)
    [not$ may_inv_x_0_i is None]:
        O(i**2 * log2(p)**2)


    #]]]'''#'''
    _check4upgrade_sqrt_mod_(p, i, j, x_0_i, xx_i_ij, p_i, p_j, may_inv_x_0_i=may_inv_x_0_i, strict=False)

    fnm_params = ...
    output4debug_ = _5may_output4debug_(None)


    if not p == 2:
        pks = {i:p_i, j:p_j}
    else:
        es = {i, i-1, i-2, j, j-1}
            # >>> {1, 1}
            # {1}
        pks = {i:p_i, j:p_j}
            # >>> {1:3,1:4}
            # {1: 4}
        for e in es:
            if e >= 0 and not e in pks:
                p_e = 1<<e
                pks[e] = p_e
        pks
    pks
    (_may_inv_x_0_i, _x_0_i, x_i_ij, x_0_ij) = _upgrade__sqrt_mod_prime_power__coprime_(fnm_params, output4debug_, p, i, j, x_0_i, xx_i_ij, pks, may_inv_x_0_i, validate)

    return (_may_inv_x_0_i, _x_0_i, x_i_ij, x_0_ij)




def iter_degrade_sqrts_mod_prime_power__coprime__5one_sqrt_(p, i, j, p_i, p_j, x__p_i, /):
    'p -> i -> j -> p_i -> p_j -> x__p_i/(int%p_i) -> xs__p_j/Iter w__p_j/(int%p_j) # [[p is prime][x__p_i%p =!= 0][1 <= j <= i][p_i == p**i][0 <= x__p_i < p_i][0 <= w__p_j < p_j][w__p_j**2%p_j == x__p_i**2%p_j]]'
    check_type_is(int, p)
    check_type_is(int, i)
    check_type_is(int, j)
    check_type_is(int, p_i)
    check_type_is(int, p_j)
    check_type_is(int, x__p_i)
    if not p >= 2: raise ValueError(p)
    if not p == 2:
        if not (p&1): raise ValueError(p)
    if not 1 <= j <= i: raise ValueError((i, j))

    if not 0 <= x__p_i < p_i: raise ValueError((x__p_i, p_i))
    if j == i:
        w__p_j = x__p_i
    else:
        w__p_j = x__p_i%p_j
    w__p_j
    xs__p_j = iter_sqrts_mod_prime_power__coprime__5one_sqrt_(p, j, p_j, w__p_j)
    return xs__p_j




def iter_sqrts_mod_prime_power__coprime__5one_sqrt_(p, k, q, x_q, /):
    'p -> k -> q -> x_q/(int%q) -> xs_q/Iter w_q/(int%q) # [[p is prime][x_q%p =!= 0][k >= 1][q == p**k][0 <= x_q < q][0 <= w_q < q][w_q**2%q == x_q**2%q]] #used in degrade all sqrts; see:upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime_'
    fnm_params = ...
    output4debug_ = _5may_output4debug_(None)

    may_pks = None
    xs_q = _iter_sqrts_mod_prime_power__coprime__5one_sqrt_(fnm_params, output4debug_, p, k, q, x_q, may_pks)
    return xs_q
    return iter(xs_q)



def __():
    #ValueError: ((2, 89, 1856910058928125295021882761), [96299660218406426371046467, 213185349602938642353734589, 405784670039751495095827523, 522670359424283711078515645])
        #after:inv_mod__coprime_ --> _upgrade__inv_mod_power__coprime_
        #bug fixed:see:_upgrade__sqrt_mod_prime_power__coprime_: (may_inv_x_0_i, x_0_i, x_i_ij) may change ==>> now return (_may_inv_x_0_i, _x_0_i, x_i_ij, x_0_ij)
    (p, k, xx) = (2, 89, 1856910058928125295021882761)
    in_out = ((p, k, xx), list_sqrts_mod_prime_power_(p, k, xx))
    _check_(in_out)
if 0b0:__()

if __name__ == "__main__":
    pass
__all__

if 0:
    with timer(prefix='inv_mod_', _to_show_=_to_show_):
        from seed.math.inv_mod_ import inv_mod_ as inv_mod__coprime_

if 1:
    # export to seed.math.inv_mod_
    #from seed.math.sqrts_mod_ import _upgrade__inv_mod_power__coprime_
    from seed.math.sqrts_mod_ import upgrade__inv_mod_power__coprime_
    from seed.math.sqrts_mod_ import inv_mod_power__coprime_
    from seed.math.sqrts_mod_ import inv_mod__coprime_

from seed.math.sqrts_mod_ import iter_sqrts_mod_prime_power_
from seed.math.sqrts_mod_ import iter_sqrts_mod_prime_
######################



######################
from seed.math.sqrts_mod_ import iter_sqrts_mod_prime_power_,  iter_sqrts_mod_prime_
from seed.math.sqrts_mod_ import iter_sqrts_mod_prime_power__coprime__5one_sqrt_
from seed.math.sqrts_mod_ import upgrade_or_maybe_after_flip_MSB_if_p_eq2__sqrt_mod_prime_power__coprime_, iter_degrade_sqrts_mod_prime_power__coprime__5one_sqrt_
from seed.math.sqrts_mod_ import is_square_residual_mod_prime_power_, is_square_residual_mod_prime_
#from seed.math.inv_mod_ import inv_mod_power__coprime_, inv_mod__coprime_, upgrade__inv_mod_power__coprime_
######################
from seed.math.sqrts_mod_ import *

