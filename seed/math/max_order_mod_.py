#__all__:goto
#TODO:goto
#bug:因为逻辑出错，一者取伪本原根纟各素幂模分量，一者取最大模秩纟整模(各素幂模分量投影不一定是相应伪本原根)

#copy to others/数学/本原根.txt
# [:规律纟伪本原根纟模二幂]:goto
# [:规律纟伪本原根纟模奇素幂]:goto

# [all_primitive_roots_modZpow_(2**1) == {1}]
# [all_primitive_roots_modZpow_(2**2) == {1}]
# [all_pseudo_primitive_roots_modZpow_(2**3) == {3, 5, 7}]
# [all_pseudo_primitive_roots_modZpow_(2**4) == {3, 5, 11, 13}]
# [[ez>=4] -> [all_pseudo_primitive_roots_modZpow_(2**ez) == {(g+16*k) | [[g:<-[3, 5, 11, 13]][k:<-[0..<2**(ez-4)]]]}]]
# [[ez>=4] -> [len(all_pseudo_primitive_roots_modZpow_(2**ez)) == 2**(ez-2)]]

# [[is_prime_(p)] -> [p%2==1] -> [g4p:<-all_primitive_roots_modPpow_(p**1)] -> [(p-1) == len({k | [[k:<-[0..<p]][(g4p+k*p) <- all_primitive_roots_modPpow_(p**2)]]})]]
# [[ep:<-[2..]] -> [is_prime_(p)] -> [p%2==1] -> [all_primitive_roots_modPpow_(p**ep) == {(g+k*p**2) | [[g:<-all_primitive_roots_modPpow_(p**2)][k:<-[0..<p**(ep-2)]]]}]]
# [[ep:<-[2..]] -> [is_prime_(p)] -> [p%2==1] -> [len(all_primitive_roots_modPpow_(p**ep)) == phi_(p-1)*(p-1)*p**(ep-2)]]
# [[is_prime_(p)] -> [p%2==1] -> [len(all_primitive_roots_modPpow_(p**2)) == phi_(p-1)*(p-1)]]
# [[is_prime_(p)] -> [p%2==1] -> [len(all_primitive_roots_modPpow_(p**1)) == phi_(p-1)]]
r'''[[[
e ../../python3_src/seed/math/max_order_mod_.py
./script/.枚举冫泛化二三五七型素数.py.swp
./seed/math/.max_order_mod_.py.swp
./seed/math/.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_.py.swp


seed.math.max_order_mod_
py -m nn_ns.app.debug_cmd   seed.math.max_order_mod_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.max_order_mod_:__doc__ -ht # -ff -df

[[
grep 'def order_mod_' -r ../../python3_src/seed/math/ -l
    <None>

grep 'max_order_mod_' -r ../../python3_src/seed/math/ -l
    view ../../python3_src/seed/math/primality_proving__plain.py
    view ../../python3_src/seed/math/prime_pint/iter_primes_where_phiP_divs_.py

===
view ../../python3_src/seed/math/prime_pint/iter_primes_where_phiP_divs_.py
[L:<-[0..]][ps::[prime]{len=L}][es::[int{>0}]{len=L}][N:=II[ps[i]**es[i] | [i:<-[0..<L]]]]:
    [max_order_mod_(N) == lcm[(ps[i]-1)*ps[i]**(es[i]-(if ps[i]==2 and es[i]>=3 then 2 else 1)) | [i:<-[0..<L]]]]
===
view ../../python3_src/seed/math/primality_proving__plain.py
[modulus :<- [2..]][g :<- [1..<modulus]][gcd(g, modulus) == 1]:
    [order_mod_(modulus; g) =[def]= min{e | [[e :<- [1..<modulus]][g**e %modulus == 1]]}]
[modulus :<- [2..]]:
    [max_order_mod_(modulus) =[def]= max{order_mod_(modulus; g) | [[g :<- [1..<modulus]][gcd(g, modulus) == 1]]}]
[modulus :<- [2..]]:
    [all_partial_orders_mod_(modulus) =[def]= [((p4M-1) *p4M**(gde_(p4M;modulus)-1 -[p4M==2][modulus%8==0])) | [p4M :<- all_prime_factors_of_(modulus)]]]
    ######################
    [core_order_mod_(modulus) =[def]= gcd(all_partial_orders_mod_(modulus))]
    ######################
    [max_order_mod_(modulus) == lcm(all_partial_orders_mod_(modulus))]
    ######################



]]



>>> [(n, num_coprimes_lt_(n)) for n in range(1, 32)]
[(1, 1), (2, 1), (3, 2), (4, 2), (5, 4), (6, 2), (7, 6), (8, 4), (9, 6), (10, 4), (11, 10), (12, 4), (13, 12), (14, 6), (15, 8), (16, 8), (17, 16), (18, 6), (19, 18), (20, 8), (21, 12), (22, 10), (23, 22), (24, 8), (25, 20), (26, 12), (27, 18), (28, 12), (29, 28), (30, 8), (31, 30)]

>>> def g(max4M, f, /):
...   for M in range(2, 1+max4M):
...     ls = [(M, u, f(M, u)) for u in range(1, M) if are_coprime(M, u)]
...     yield ls
...     yield (M, max(e for _,_,e in ls))
>>> def gg(max4M, /):
...     ls0 = [*g(max4M, order_mod__naive_brute_force_)]
...     ls1 = [*g(max4M, order_mod__fancy_)]
...     assert ls0 == ls1
...     for x in ls1:print(x)
>>> gg(31)
[(2, 1, 1)]
(2, 1)
[(3, 1, 1), (3, 2, 2)]
(3, 2)
[(4, 1, 1), (4, 3, 2)]
(4, 2)
[(5, 1, 1), (5, 2, 4), (5, 3, 4), (5, 4, 2)]
(5, 4)
[(6, 1, 1), (6, 5, 2)]
(6, 2)
[(7, 1, 1), (7, 2, 3), (7, 3, 6), (7, 4, 3), (7, 5, 6), (7, 6, 2)]
(7, 6)
[(8, 1, 1), (8, 3, 2), (8, 5, 2), (8, 7, 2)]
(8, 2)
[(9, 1, 1), (9, 2, 6), (9, 4, 3), (9, 5, 6), (9, 7, 3), (9, 8, 2)]
(9, 6)
[(10, 1, 1), (10, 3, 4), (10, 7, 4), (10, 9, 2)]
(10, 4)
[(11, 1, 1), (11, 2, 10), (11, 3, 5), (11, 4, 5), (11, 5, 5), (11, 6, 10), (11, 7, 10), (11, 8, 10), (11, 9, 5), (11, 10, 2)]
(11, 10)
[(12, 1, 1), (12, 5, 2), (12, 7, 2), (12, 11, 2)]
(12, 2)
[(13, 1, 1), (13, 2, 12), (13, 3, 3), (13, 4, 6), (13, 5, 4), (13, 6, 12), (13, 7, 12), (13, 8, 4), (13, 9, 3), (13, 10, 6), (13, 11, 12), (13, 12, 2)]
(13, 12)
[(14, 1, 1), (14, 3, 6), (14, 5, 6), (14, 9, 3), (14, 11, 3), (14, 13, 2)]
(14, 6)
[(15, 1, 1), (15, 2, 4), (15, 4, 2), (15, 7, 4), (15, 8, 4), (15, 11, 2), (15, 13, 4), (15, 14, 2)]
(15, 4)
[(16, 1, 1), (16, 3, 4), (16, 5, 4), (16, 7, 2), (16, 9, 2), (16, 11, 4), (16, 13, 4), (16, 15, 2)]
(16, 4)
[(17, 1, 1), (17, 2, 8), (17, 3, 16), (17, 4, 4), (17, 5, 16), (17, 6, 16), (17, 7, 16), (17, 8, 8), (17, 9, 8), (17, 10, 16), (17, 11, 16), (17, 12, 16), (17, 13, 4), (17, 14, 16), (17, 15, 8), (17, 16, 2)]
(17, 16)
[(18, 1, 1), (18, 5, 6), (18, 7, 3), (18, 11, 6), (18, 13, 3), (18, 17, 2)]
(18, 6)
[(19, 1, 1), (19, 2, 18), (19, 3, 18), (19, 4, 9), (19, 5, 9), (19, 6, 9), (19, 7, 3), (19, 8, 6), (19, 9, 9), (19, 10, 18), (19, 11, 3), (19, 12, 6), (19, 13, 18), (19, 14, 18), (19, 15, 18), (19, 16, 9), (19, 17, 9), (19, 18, 2)]
(19, 18)
[(20, 1, 1), (20, 3, 4), (20, 7, 4), (20, 9, 2), (20, 11, 2), (20, 13, 4), (20, 17, 4), (20, 19, 2)]
(20, 4)
[(21, 1, 1), (21, 2, 6), (21, 4, 3), (21, 5, 6), (21, 8, 2), (21, 10, 6), (21, 11, 6), (21, 13, 2), (21, 16, 3), (21, 17, 6), (21, 19, 6), (21, 20, 2)]
(21, 6)
[(22, 1, 1), (22, 3, 5), (22, 5, 5), (22, 7, 10), (22, 9, 5), (22, 13, 10), (22, 15, 5), (22, 17, 10), (22, 19, 10), (22, 21, 2)]
(22, 10)
[(23, 1, 1), (23, 2, 11), (23, 3, 11), (23, 4, 11), (23, 5, 22), (23, 6, 11), (23, 7, 22), (23, 8, 11), (23, 9, 11), (23, 10, 22), (23, 11, 22), (23, 12, 11), (23, 13, 11), (23, 14, 22), (23, 15, 22), (23, 16, 11), (23, 17, 22), (23, 18, 11), (23, 19, 22), (23, 20, 22), (23, 21, 22), (23, 22, 2)]
(23, 22)
[(24, 1, 1), (24, 5, 2), (24, 7, 2), (24, 11, 2), (24, 13, 2), (24, 17, 2), (24, 19, 2), (24, 23, 2)]
(24, 2)
[(25, 1, 1), (25, 2, 20), (25, 3, 20), (25, 4, 10), (25, 6, 5), (25, 7, 4), (25, 8, 20), (25, 9, 10), (25, 11, 5), (25, 12, 20), (25, 13, 20), (25, 14, 10), (25, 16, 5), (25, 17, 20), (25, 18, 4), (25, 19, 10), (25, 21, 5), (25, 22, 20), (25, 23, 20), (25, 24, 2)]
(25, 20)
[(26, 1, 1), (26, 3, 3), (26, 5, 4), (26, 7, 12), (26, 9, 3), (26, 11, 12), (26, 15, 12), (26, 17, 6), (26, 19, 12), (26, 21, 4), (26, 23, 6), (26, 25, 2)]
(26, 12)
[(27, 1, 1), (27, 2, 18), (27, 4, 9), (27, 5, 18), (27, 7, 9), (27, 8, 6), (27, 10, 3), (27, 11, 18), (27, 13, 9), (27, 14, 18), (27, 16, 9), (27, 17, 6), (27, 19, 3), (27, 20, 18), (27, 22, 9), (27, 23, 18), (27, 25, 9), (27, 26, 2)]
(27, 18)
[(28, 1, 1), (28, 3, 6), (28, 5, 6), (28, 9, 3), (28, 11, 6), (28, 13, 2), (28, 15, 2), (28, 17, 6), (28, 19, 6), (28, 23, 6), (28, 25, 3), (28, 27, 2)]
(28, 6)
[(29, 1, 1), (29, 2, 28), (29, 3, 28), (29, 4, 14), (29, 5, 14), (29, 6, 14), (29, 7, 7), (29, 8, 28), (29, 9, 14), (29, 10, 28), (29, 11, 28), (29, 12, 4), (29, 13, 14), (29, 14, 28), (29, 15, 28), (29, 16, 7), (29, 17, 4), (29, 18, 28), (29, 19, 28), (29, 20, 7), (29, 21, 28), (29, 22, 14), (29, 23, 7), (29, 24, 7), (29, 25, 7), (29, 26, 28), (29, 27, 28), (29, 28, 2)]
(29, 28)
[(30, 1, 1), (30, 7, 4), (30, 11, 2), (30, 13, 4), (30, 17, 4), (30, 19, 2), (30, 23, 4), (30, 29, 2)]
(30, 4)
[(31, 1, 1), (31, 2, 5), (31, 3, 30), (31, 4, 5), (31, 5, 3), (31, 6, 6), (31, 7, 15), (31, 8, 5), (31, 9, 15), (31, 10, 15), (31, 11, 30), (31, 12, 30), (31, 13, 30), (31, 14, 15), (31, 15, 10), (31, 16, 5), (31, 17, 30), (31, 18, 15), (31, 19, 15), (31, 20, 15), (31, 21, 30), (31, 22, 30), (31, 23, 10), (31, 24, 30), (31, 25, 3), (31, 26, 6), (31, 27, 10), (31, 28, 15), (31, 29, 10), (31, 30, 2)]
(31, 30)
>>> [(M, max_order_mod_(M)) for M in range(2, 32)]
[(2, 1), (3, 2), (4, 2), (5, 4), (6, 2), (7, 6), (8, 2), (9, 6), (10, 4), (11, 10), (12, 2), (13, 12), (14, 6), (15, 4), (16, 4), (17, 16), (18, 6), (19, 18), (20, 4), (21, 6), (22, 10), (23, 22), (24, 2), (25, 20), (26, 12), (27, 18), (28, 6), (29, 28), (30, 4), (31, 30)]








>>> def g2(max_ez4M, f, /):
...   szs4gss = []
...   prev_gs = []
...   for ez4M in range(1, 1+max_ez4M):
...     M = 1<<ez4M
...     ls = [(M, u, f(M, u)) for u in range(1, M) if are_coprime(M, u)]
...     yield ls
...     max_order_modM = max(e for _,_,e in ls)
...     gs = [u for _,u,e in ls if e==max_order_modM]
...     yield (M, max_order_modM, len(gs), gs)
...     szs4gss.append(len(gs))
...     ######################
...     # [:规律纟伪本原根纟模二幂]:here
...     # [all_primitive_roots_modZpow_(2**1) == {1}]
...     # [all_primitive_roots_modZpow_(2**2) == {1}]
...     # [all_pseudo_primitive_roots_modZpow_(2**3) == {3, 5, 7}]
...     # [all_pseudo_primitive_roots_modZpow_(2**4) == {3, 5, 11, 13}]
...     # [[ez>=4] -> [all_pseudo_primitive_roots_modZpow_(2**ez) == {(g+16*k) | [[g:<-[3, 5, 11, 13]][k:<-[0..<2**(ez-4)]]]}]]
...     # [[ez>=4] -> [len(all_pseudo_primitive_roots_modZpow_(2**ez)) == 2**(ez-2)]]
...     ######################
...     if ez4M>=4:
...         assert len(gs) == M>>2
...     if ez4M>=5:
...         prev_M = M>>1
...         assert gs == prev_gs+[g+prev_M for g in prev_gs]
...     ######################
...     prev_gs = gs
...   yield szs4gss
>>> def gg2(max_ez4M, /):
...     ls0 = [*g2(max_ez4M, order_mod__naive_brute_force_)]
...     ls1 = [*g2(max_ez4M, order_mod__fancy_)]
...     assert ls0 == ls1
...     for x in ls1:print(x)
>>> gg2(8)
[(2, 1, 1)]
(2, 1, 1, [1])
[(4, 1, 1), (4, 3, 2)]
(4, 2, 1, [3])
[(8, 1, 1), (8, 3, 2), (8, 5, 2), (8, 7, 2)]
(8, 2, 3, [3, 5, 7])
[(16, 1, 1), (16, 3, 4), (16, 5, 4), (16, 7, 2), (16, 9, 2), (16, 11, 4), (16, 13, 4), (16, 15, 2)]
(16, 4, 4, [3, 5, 11, 13])
[(32, 1, 1), (32, 3, 8), (32, 5, 8), (32, 7, 4), (32, 9, 4), (32, 11, 8), (32, 13, 8), (32, 15, 2), (32, 17, 2), (32, 19, 8), (32, 21, 8), (32, 23, 4), (32, 25, 4), (32, 27, 8), (32, 29, 8), (32, 31, 2)]
(32, 8, 8, [3, 5, 11, 13, 19, 21, 27, 29])
[(64, 1, 1), (64, 3, 16), (64, 5, 16), (64, 7, 8), (64, 9, 8), (64, 11, 16), (64, 13, 16), (64, 15, 4), (64, 17, 4), (64, 19, 16), (64, 21, 16), (64, 23, 8), (64, 25, 8), (64, 27, 16), (64, 29, 16), (64, 31, 2), (64, 33, 2), (64, 35, 16), (64, 37, 16), (64, 39, 8), (64, 41, 8), (64, 43, 16), (64, 45, 16), (64, 47, 4), (64, 49, 4), (64, 51, 16), (64, 53, 16), (64, 55, 8), (64, 57, 8), (64, 59, 16), (64, 61, 16), (64, 63, 2)]
(64, 16, 16, [3, 5, 11, 13, 19, 21, 27, 29, 35, 37, 43, 45, 51, 53, 59, 61])
[(128, 1, 1), (128, 3, 32), (128, 5, 32), (128, 7, 16), (128, 9, 16), (128, 11, 32), (128, 13, 32), (128, 15, 8), (128, 17, 8), (128, 19, 32), (128, 21, 32), (128, 23, 16), (128, 25, 16), (128, 27, 32), (128, 29, 32), (128, 31, 4), (128, 33, 4), (128, 35, 32), (128, 37, 32), (128, 39, 16), (128, 41, 16), (128, 43, 32), (128, 45, 32), (128, 47, 8), (128, 49, 8), (128, 51, 32), (128, 53, 32), (128, 55, 16), (128, 57, 16), (128, 59, 32), (128, 61, 32), (128, 63, 2), (128, 65, 2), (128, 67, 32), (128, 69, 32), (128, 71, 16), (128, 73, 16), (128, 75, 32), (128, 77, 32), (128, 79, 8), (128, 81, 8), (128, 83, 32), (128, 85, 32), (128, 87, 16), (128, 89, 16), (128, 91, 32), (128, 93, 32), (128, 95, 4), (128, 97, 4), (128, 99, 32), (128, 101, 32), (128, 103, 16), (128, 105, 16), (128, 107, 32), (128, 109, 32), (128, 111, 8), (128, 113, 8), (128, 115, 32), (128, 117, 32), (128, 119, 16), (128, 121, 16), (128, 123, 32), (128, 125, 32), (128, 127, 2)]
(128, 32, 32, [3, 5, 11, 13, 19, 21, 27, 29, 35, 37, 43, 45, 51, 53, 59, 61, 67, 69, 75, 77, 83, 85, 91, 93, 99, 101, 107, 109, 115, 117, 123, 125])
[(256, 1, 1), (256, 3, 64), (256, 5, 64), (256, 7, 32), (256, 9, 32), (256, 11, 64), (256, 13, 64), (256, 15, 16), (256, 17, 16), (256, 19, 64), (256, 21, 64), (256, 23, 32), (256, 25, 32), (256, 27, 64), (256, 29, 64), (256, 31, 8), (256, 33, 8), (256, 35, 64), (256, 37, 64), (256, 39, 32), (256, 41, 32), (256, 43, 64), (256, 45, 64), (256, 47, 16), (256, 49, 16), (256, 51, 64), (256, 53, 64), (256, 55, 32), (256, 57, 32), (256, 59, 64), (256, 61, 64), (256, 63, 4), (256, 65, 4), (256, 67, 64), (256, 69, 64), (256, 71, 32), (256, 73, 32), (256, 75, 64), (256, 77, 64), (256, 79, 16), (256, 81, 16), (256, 83, 64), (256, 85, 64), (256, 87, 32), (256, 89, 32), (256, 91, 64), (256, 93, 64), (256, 95, 8), (256, 97, 8), (256, 99, 64), (256, 101, 64), (256, 103, 32), (256, 105, 32), (256, 107, 64), (256, 109, 64), (256, 111, 16), (256, 113, 16), (256, 115, 64), (256, 117, 64), (256, 119, 32), (256, 121, 32), (256, 123, 64), (256, 125, 64), (256, 127, 2), (256, 129, 2), (256, 131, 64), (256, 133, 64), (256, 135, 32), (256, 137, 32), (256, 139, 64), (256, 141, 64), (256, 143, 16), (256, 145, 16), (256, 147, 64), (256, 149, 64), (256, 151, 32), (256, 153, 32), (256, 155, 64), (256, 157, 64), (256, 159, 8), (256, 161, 8), (256, 163, 64), (256, 165, 64), (256, 167, 32), (256, 169, 32), (256, 171, 64), (256, 173, 64), (256, 175, 16), (256, 177, 16), (256, 179, 64), (256, 181, 64), (256, 183, 32), (256, 185, 32), (256, 187, 64), (256, 189, 64), (256, 191, 4), (256, 193, 4), (256, 195, 64), (256, 197, 64), (256, 199, 32), (256, 201, 32), (256, 203, 64), (256, 205, 64), (256, 207, 16), (256, 209, 16), (256, 211, 64), (256, 213, 64), (256, 215, 32), (256, 217, 32), (256, 219, 64), (256, 221, 64), (256, 223, 8), (256, 225, 8), (256, 227, 64), (256, 229, 64), (256, 231, 32), (256, 233, 32), (256, 235, 64), (256, 237, 64), (256, 239, 16), (256, 241, 16), (256, 243, 64), (256, 245, 64), (256, 247, 32), (256, 249, 32), (256, 251, 64), (256, 253, 64), (256, 255, 2)]
(256, 64, 64, [3, 5, 11, 13, 19, 21, 27, 29, 35, 37, 43, 45, 51, 53, 59, 61, 67, 69, 75, 77, 83, 85, 91, 93, 99, 101, 107, 109, 115, 117, 123, 125, 131, 133, 139, 141, 147, 149, 155, 157, 163, 165, 171, 173, 179, 181, 187, 189, 195, 197, 203, 205, 211, 213, 219, 221, 227, 229, 235, 237, 243, 245, 251, 253])
[1, 1, 3, 4, 8, 16, 32, 64]



>>> from itertools import chain
>>> def gp_(p, max_ep4M, f, /):
...   szs4gss = []
...   prev_gs = []
...   for ep4M in range(1, 1+max_ep4M):
...     M = p**ep4M
...     #ls = [(M, u, f(M, u)) for u in range(1, M) if are_coprime(M, u)]
...     ls = [(M, u, f(M, u)) for u in range(1, M) if u%p]
...     #yield ls
...     max_order_modM = max(e for _,_,e in ls)
...     gs = [u for _,u,e in ls if e==max_order_modM]
...     yield (M, max_order_modM, len(gs), gs)
...     szs4gss.append(len(gs))
...     ######################
...     # [:规律纟伪本原根纟模奇素幂]:here
...     # [[is_prime_(p)] -> [p%2==1] -> [g4p:<-all_primitive_roots_modPpow_(p**1)] -> [(p-1) == len({k | [[k:<-[0..<p]][(g4p+k*p) <- all_primitive_roots_modPpow_(p**2)]]})]]
...     # [[ep:<-[2..]] -> [is_prime_(p)] -> [p%2==1] -> [all_primitive_roots_modPpow_(p**ep) == {(g+k*p**2) | [[g:<-all_primitive_roots_modPpow_(p**2)][k:<-[0..<p**(ep-2)]]]}]]
...     # [[ep:<-[2..]] -> [is_prime_(p)] -> [p%2==1] -> [len(all_primitive_roots_modPpow_(p**ep)) == phi_(p-1)*(p-1)*p**(ep-2)]]
...     # [[is_prime_(p)] -> [p%2==1] -> [len(all_primitive_roots_modPpow_(p**2)) == phi_(p-1)*(p-1)]]
...     # [[is_prime_(p)] -> [p%2==1] -> [len(all_primitive_roots_modPpow_(p**1)) == phi_(p-1)]]
...     ######################
...     if ep4M==2:
...         assert len(gs) == len(prev_gs)*(p-1)#phi_phiM#多个副本中只有一个无效:见下面:『non_primitive_root』
...     if ep4M>=3:
...         assert len(gs) == len(prev_gs)*p#phi_phiM#所有副本均有效
...         prev_M = M//p
...         assert gs == list(chain.from_iterable((g+offset for g in prev_gs) for offset in range(0, M, prev_M)))
...     ######################
...     prev_gs = gs
...   yield szs4gss
>>> def ggp_(p, max_ep4M, /):
...     ls0 = [*gp_(p, max_ep4M, order_mod__naive_brute_force_)]
...     ls1 = [*gp_(p, max_ep4M, order_mod__fancy_)]
...     assert ls0 == ls1
...     for x in ls1:print(x)
>>> ggp_(3, 4)
(3, 2, 1, [2])
(9, 6, 2, [2, 5])
(27, 18, 6, [2, 5, 11, 14, 20, 23])
(81, 54, 18, [2, 5, 11, 14, 20, 23, 29, 32, 38, 41, 47, 50, 56, 59, 65, 68, 74, 77])
[1, 2, 6, 18]

>>> ggp_(5, 4)
(5, 4, 2, [2, 3])
(25, 20, 8, [2, 3, 8, 12, 13, 17, 22, 23])
(125, 100, 40, [2, 3, 8, 12, 13, 17, 22, 23, 27, 28, 33, 37, 38, 42, 47, 48, 52, 53, 58, 62, 63, 67, 72, 73, 77, 78, 83, 87, 88, 92, 97, 98, 102, 103, 108, 112, 113, 117, 122, 123])
(625, 500, 200, [2, 3, 8, 12, 13, 17, 22, 23, 27, 28, 33, 37, 38, 42, 47, 48, 52, 53, 58, 62, 63, 67, 72, 73, 77, 78, 83, 87, 88, 92, 97, 98, 102, 103, 108, 112, 113, 117, 122, 123, 127, 128, 133, 137, 138, 142, 147, 148, 152, 153, 158, 162, 163, 167, 172, 173, 177, 178, 183, 187, 188, 192, 197, 198, 202, 203, 208, 212, 213, 217, 222, 223, 227, 228, 233, 237, 238, 242, 247, 248, 252, 253, 258, 262, 263, 267, 272, 273, 277, 278, 283, 287, 288, 292, 297, 298, 302, 303, 308, 312, 313, 317, 322, 323, 327, 328, 333, 337, 338, 342, 347, 348, 352, 353, 358, 362, 363, 367, 372, 373, 377, 378, 383, 387, 388, 392, 397, 398, 402, 403, 408, 412, 413, 417, 422, 423, 427, 428, 433, 437, 438, 442, 447, 448, 452, 453, 458, 462, 463, 467, 472, 473, 477, 478, 483, 487, 488, 492, 497, 498, 502, 503, 508, 512, 513, 517, 522, 523, 527, 528, 533, 537, 538, 542, 547, 548, 552, 553, 558, 562, 563, 567, 572, 573, 577, 578, 583, 587, 588, 592, 597, 598, 602, 603, 608, 612, 613, 617, 622, 623])
[2, 8, 40, 200]

>>> ggp_(7, 4)
(7, 6, 2, [3, 5])
(49, 42, 12, [3, 5, 10, 12, 17, 24, 26, 33, 38, 40, 45, 47])
(343, 294, 84, [3, 5, 10, 12, 17, 24, 26, 33, 38, 40, 45, 47, 52, 54, 59, 61, 66, 73, 75, 82, 87, 89, 94, 96, 101, 103, 108, 110, 115, 122, 124, 131, 136, 138, 143, 145, 150, 152, 157, 159, 164, 171, 173, 180, 185, 187, 192, 194, 199, 201, 206, 208, 213, 220, 222, 229, 234, 236, 241, 243, 248, 250, 255, 257, 262, 269, 271, 278, 283, 285, 290, 292, 297, 299, 304, 306, 311, 318, 320, 327, 332, 334, 339, 341])
(2401, 2058, 588, [3, 5, 10, 12, 17, 24, 26, 33, 38, 40, 45, 47, 52, 54, 59, 61, 66, 73, 75, 82, 87, 89, 94, 96, 101, 103, 108, 110, 115, 122, 124, 131, 136, 138, 143, 145, 150, 152, 157, 159, 164, 171, 173, 180, 185, 187, 192, 194, 199, 201, 206, 208, 213, 220, 222, 229, 234, 236, 241, 243, 248, 250, 255, 257, 262, 269, 271, 278, 283, 285, 290, 292, 297, 299, 304, 306, 311, 318, 320, 327, 332, 334, 339, 341, 346, 348, 353, 355, 360, 367, 369, 376, 381, 383, 388, 390, 395, 397, 402, 404, 409, 416, 418, 425, 430, 432, 437, 439, 444, 446, 451, 453, 458, 465, 467, 474, 479, 481, 486, 488, 493, 495, 500, 502, 507, 514, 516, 523, 528, 530, 535, 537, 542, 544, 549, 551, 556, 563, 565, 572, 577, 579, 584, 586, 591, 593, 598, 600, 605, 612, 614, 621, 626, 628, 633, 635, 640, 642, 647, 649, 654, 661, 663, 670, 675, 677, 682, 684, 689, 691, 696, 698, 703, 710, 712, 719, 724, 726, 731, 733, 738, 740, 745, 747, 752, 759, 761, 768, 773, 775, 780, 782, 787, 789, 794, 796, 801, 808, 810, 817, 822, 824, 829, 831, 836, 838, 843, 845, 850, 857, 859, 866, 871, 873, 878, 880, 885, 887, 892, 894, 899, 906, 908, 915, 920, 922, 927, 929, 934, 936, 941, 943, 948, 955, 957, 964, 969, 971, 976, 978, 983, 985, 990, 992, 997, 1004, 1006, 1013, 1018, 1020, 1025, 1027, 1032, 1034, 1039, 1041, 1046, 1053, 1055, 1062, 1067, 1069, 1074, 1076, 1081, 1083, 1088, 1090, 1095, 1102, 1104, 1111, 1116, 1118, 1123, 1125, 1130, 1132, 1137, 1139, 1144, 1151, 1153, 1160, 1165, 1167, 1172, 1174, 1179, 1181, 1186, 1188, 1193, 1200, 1202, 1209, 1214, 1216, 1221, 1223, 1228, 1230, 1235, 1237, 1242, 1249, 1251, 1258, 1263, 1265, 1270, 1272, 1277, 1279, 1284, 1286, 1291, 1298, 1300, 1307, 1312, 1314, 1319, 1321, 1326, 1328, 1333, 1335, 1340, 1347, 1349, 1356, 1361, 1363, 1368, 1370, 1375, 1377, 1382, 1384, 1389, 1396, 1398, 1405, 1410, 1412, 1417, 1419, 1424, 1426, 1431, 1433, 1438, 1445, 1447, 1454, 1459, 1461, 1466, 1468, 1473, 1475, 1480, 1482, 1487, 1494, 1496, 1503, 1508, 1510, 1515, 1517, 1522, 1524, 1529, 1531, 1536, 1543, 1545, 1552, 1557, 1559, 1564, 1566, 1571, 1573, 1578, 1580, 1585, 1592, 1594, 1601, 1606, 1608, 1613, 1615, 1620, 1622, 1627, 1629, 1634, 1641, 1643, 1650, 1655, 1657, 1662, 1664, 1669, 1671, 1676, 1678, 1683, 1690, 1692, 1699, 1704, 1706, 1711, 1713, 1718, 1720, 1725, 1727, 1732, 1739, 1741, 1748, 1753, 1755, 1760, 1762, 1767, 1769, 1774, 1776, 1781, 1788, 1790, 1797, 1802, 1804, 1809, 1811, 1816, 1818, 1823, 1825, 1830, 1837, 1839, 1846, 1851, 1853, 1858, 1860, 1865, 1867, 1872, 1874, 1879, 1886, 1888, 1895, 1900, 1902, 1907, 1909, 1914, 1916, 1921, 1923, 1928, 1935, 1937, 1944, 1949, 1951, 1956, 1958, 1963, 1965, 1970, 1972, 1977, 1984, 1986, 1993, 1998, 2000, 2005, 2007, 2012, 2014, 2019, 2021, 2026, 2033, 2035, 2042, 2047, 2049, 2054, 2056, 2061, 2063, 2068, 2070, 2075, 2082, 2084, 2091, 2096, 2098, 2103, 2105, 2110, 2112, 2117, 2119, 2124, 2131, 2133, 2140, 2145, 2147, 2152, 2154, 2159, 2161, 2166, 2168, 2173, 2180, 2182, 2189, 2194, 2196, 2201, 2203, 2208, 2210, 2215, 2217, 2222, 2229, 2231, 2238, 2243, 2245, 2250, 2252, 2257, 2259, 2264, 2266, 2271, 2278, 2280, 2287, 2292, 2294, 2299, 2301, 2306, 2308, 2313, 2315, 2320, 2327, 2329, 2336, 2341, 2343, 2348, 2350, 2355, 2357, 2362, 2364, 2369, 2376, 2378, 2385, 2390, 2392, 2397, 2399])
[2, 12, 84, 588]



==>>:
big_endian-radix_repr:
(3, 2, 1, [2])
(9, 6, 2, [2, 5])
    2~[0,2]
    5~[1,2]
    non_primitive_root:[2,2]

(5, 4, 2, [2, 3])
(25, 20, 8, [2, 3, 8, 12, 13, 17, 22, 23])
    2~[0,2]
    12~[2,2]
    17~[3,2]
    22~[4,2]
    non_primitive_root:[1,2]

    3~[0,3]
    8~[1,3]
    13~[2,3]
    23~[4,3]
    non_primitive_root:[3,3]

(7, 6, 2, [3, 5])
(49, 42, 12, [3, 5, 10, 12, 17, 24, 26, 33, 38, 40, 45, 47])
    3~[0,3]
    10~[1,3]
    17~[2,3]
    24~[3,3]
    38~[5,3]
    45~[6,3]
    non_primitive_root:[4,3]

    5~[0,5]
    12~[1,5]
    26~[3,5]
    33~[4,5]
    40~[5,5]
    47~[6,5]
    non_primitive_root:[2,5]
==>>:
# [:规律纟伪本原根纟模奇素幂]:goto








not:[3, 19, 35, 51, 5, 21, 37, 53, 11, 27, 43, 59, 13, 29, 45, 61]
    !! list_sorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_
>>> list(iter_unsorted_pseudo_primitive_roots_mod_(2**6))
[3, 5, 11, 13, 19, 21, 27, 29, 35, 37, 43, 45, 51, 53, 59, 61]
>>> sorted(iter_unsorted_pseudo_primitive_roots_mod_(64))
[3, 5, 11, 13, 19, 21, 27, 29, 35, 37, 43, 45, 51, 53, 59, 61]

>>> list(iter_unsorted_pseudo_primitive_roots_mod_(3**4))
[2, 5, 11, 14, 20, 23, 29, 32, 38, 41, 47, 50, 56, 59, 65, 68, 74, 77]
>>> list(iter_unsorted_pseudo_primitive_roots_mod_(5**3))
[2, 3, 8, 12, 13, 17, 22, 23, 27, 28, 33, 37, 38, 42, 47, 48, 52, 53, 58, 62, 63, 67, 72, 73, 77, 78, 83, 87, 88, 92, 97, 98, 102, 103, 108, 112, 113, 117, 122, 123]

>>> list(iter_unsorted_pseudo_primitive_roots_mod_(2**4 * 3**2))
[83, 131, 101, 5, 11, 59, 29, 77]
>>> sorted(iter_unsorted_pseudo_primitive_roots_mod_(2**4 * 3**2))
[5, 11, 29, 59, 77, 83, 101, 131]

>>> list(iter_unsorted_pseudo_primitive_roots_mod_(2**5 * 3**3))
[515, 707, 227, 419, 803, 131, 677, 5, 389, 581, 101, 293, 299, 491, 11, 203, 587, 779, 461, 653, 173, 365, 749, 77, 83, 275, 659, 851, 371, 563, 245, 437, 821, 149, 533, 725, 731, 59, 443, 635, 155, 347, 29, 221, 605, 797, 317, 509]
>>> (_a := sorted(iter_unsorted_pseudo_primitive_roots_mod_(2**5 * 3**3)))
[5, 11, 29, 59, 77, 83, 101, 131, 149, 155, 173, 203, 221, 227, 245, 275, 293, 299, 317, 347, 365, 371, 389, 419, 437, 443, 461, 491, 509, 515, 533, 563, 581, 587, 605, 635, 653, 659, 677, 707, 725, 731, 749, 779, 797, 803, 821, 851]
>>> len(_a)
48
>>> len(_a) == 48 == 2**3 * 2*3
True


>>> (_b := list(iter_sorted_pseudo_primitive_roots_mod__naive_brute_force_(2**5 * 3**3)))
[5, 11, 13, 29, 43, 59, 61, 67, 77, 83, 85, 101, 115, 131, 133, 139, 149, 155, 157, 173, 187, 203, 205, 211, 221, 227, 229, 245, 259, 275, 277, 283, 293, 299, 301, 317, 331, 347, 349, 355, 365, 371, 373, 389, 403, 419, 421, 427, 437, 443, 445, 461, 475, 491, 493, 499, 509, 515, 517, 533, 547, 563, 565, 571, 581, 587, 589, 605, 619, 635, 637, 643, 653, 659, 661, 677, 691, 707, 709, 715, 725, 731, 733, 749, 763, 779, 781, 787, 797, 803, 805, 821, 835, 851, 853, 859]
>>> len(_b)
96
>>> len(_b) == 96 == 2**3 * 2**2*3
True

>>> _b == _a
#bug:因为逻辑出错，一者取伪本原根纟各素幂模分量，一者取最大模秩纟整模(各素幂模分量投影不一定是相应伪本原根)
True



















py_adhoc_call   seed.math.max_order_mod_   @f

]]]'''#'''
__all__ = r'''
max_order_mod_

order_mod__naive_brute_force_
order_mod__fancy_
    order_mod_

num_coprimes_lt_
    phi_



iter_sorted_pseudo_primitive_roots_mod__naive_brute_force_
iter_unsorted_pseudo_primitive_roots_mod_
    full_api4iter_unsorted_pseudo_primitive_roots_mod_
    min_api4iter_pseudo_primitive_roots_mod_
        prepare4min_api4iter_pseudo_primitive_roots_mod_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...



from seed.math.semi_factor_pint_via_trial_division import complete_factor_pint_via_trial_division
from seed.math.Chinese_Remainder_Theorem import mk_CRT


if 1:from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import _iter_coprimes4prime_bases_
from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import iter_unsorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_, list_sorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_
#def iter_unsorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_(exp4Ppow, factorization_of_pmm, may_p=None, may_arbitrary_one_primitive_root_modP=None, may_arbitrary_one_primitive_root_modPP=None, /):
#    'exp4Ppow/int{>=1} -> factorization{p-1} -> may p -> may arbitrary_one_primitive_root%p -> may arbitrary_one_primitive_root%p**2{== 2 not exp4Ppow} -> unsorted (Iter primitive_root%p**exp4Ppow)'



from seed.iters.apply_commutative_operations_except_one import iter_apply_commutative_operations_except_one_
#def iter_apply_commutative_operations_except_one_(apply_, commutative_operation_keys, x0, /):
    # :: (k->x->x) -> [k] -> x -> (iter x)
from seed.math.II import II, II__ft_e_pairs_, II__p2e_
from seed.math.gcd import gcd, gcd_many, are_coprime
from seed.math.lcm import lcm_many, lcm
from seed.math.prepare_p2e4N import prepare_p2e4psphiM_ex_
from seed.math.prepare_p2e4N import prepare_p2e4N_
#def prepare_p2e4N_(N, may_p2e4N_or_ps4N_or_factor_pint_func, /):
from seed.tiny_.check import check_type_is, check_int_ge

from itertools import product
___end_mark_of_excluded_global_names__0___ = ...

from seed.math.prepare_p2e4N import num_coprimes_lt_, phi_


#.def iter_pows_mod_(modulus, coprime4M, /):
#.    ######################
#.    check_int_ge(2, modulus)
#.    check_type_is(int, coprime4M)
#.    if not are_coprime(M:=modulus, u:=coprime4M%modulus):raise ValueError(modulus, coprime4M)
#.    M
#.    u
#.    ######################
#.    pw = u
#.    while not pw==1:
#.        yield pw
#.        pw = pw*u%M
#.    assert pw == 1
#.    yield pw
#.    return
#.
#.
#.def iter_order_kept_pows_mod_(modulus, coprime4M, psphiM_or_may_p2e4M_or_ps4M_or_factor_pint_func=None, may_p2e4psphiM_or_ps4psphiM_or_factor_pint_func=None, /):
#.    'modulus/int{>=2} -> coprime4M/int{gcd(modulus,coprime4M)==1} -> (psphiM|may_p2e4M_or_ps4M_or_factor_pint_func=None) -> (may_p2e4psphiM_or_ps4psphiM_or_factor_pint_func=None) -> Iter pw/(uint%modulus){[order_mod_(modulus;pw)==order_mod_(modulus;coprime4M)]} # [psphiM <- [k | [[k:<-[1..]][k%order_mod_(modulus;coprime4M)==0]]]]'
#.    (psphiM, p2e4psphiM) = prepare_p2e4psphiM_ex_(modulus, psphiM_or_may_p2e4M_or_ps4M_or_factor_pint_func, may_p2e4psphiM_or_ps4psphiM_or_factor_pint_func)
#.    ...






def iter_sorted_pseudo_primitive_roots_mod__naive_brute_force_(modulus, may_p2e4M_or_ps4M_or_factor_pint_func=None, psphiM_or_may_p2e4M_or_ps4M_or_factor_pint_func=None, may_p2e4psphiM_or_ps4psphiM_or_factor_pint_func=None, /):
    order_mod__naive_brute_force_
    order_mod__fancy_
    M = modulus
    p2e4M = prepare_p2e4N_(M, may_p2e4M_or_ps4M_or_factor_pint_func)
    max_order_modM = max_order_mod_(M, p2e4M)
    if not type(psphiM_or_may_p2e4M_or_ps4M_or_factor_pint_func) is int:
        psphiM_or_may_p2e4M_or_ps4M_or_factor_pint_func = p2e4M
    (psphiM, p2e4psphiM) = prepare_p2e4psphiM_ex_(modulus, psphiM_or_may_p2e4M_or_ps4M_or_factor_pint_func, may_p2e4psphiM_or_ps4psphiM_or_factor_pint_func)
    ps4M = sorted(p2e4M)
    iter_coprimes4M = _iter_coprimes4prime_bases_(ps4M, range(M))
    for coprime4M in iter_coprimes4M:
        order_modM_u = order_mod__fancy_(modulus, coprime4M, psphiM_or_may_p2e4M_or_ps4M_or_factor_pint_func, may_p2e4psphiM_or_ps4psphiM_or_factor_pint_func)
        #if 0b0001:assert order_modM_u == order_mod__naive_brute_force_(M, coprime4M)
        if max_order_modM == order_modM_u:
            yield coprime4M
def iter_unsorted_pseudo_primitive_roots_mod_(modulus, may_p2e4M_or_ps4M_or_factor_pint_func=None, may_q2e4O_or_qs4O_or_factor_pint_func=None, /, *, may_p4M2q2e4Pmm=None, may_j4P2p4M=None, may_j4P2primitive_roots_modPpow=None, may_j4P2Ppow4M=None, may_crt4M=None):
    #def iter_unsorted_pseudo_primitive_roots_mod_(modulus, p2e4M, max_order_modM, q2e4O, p4M2q2e4Pmm, j4P2p4M, j4P2primitive_roots_modPpow, j4P2Ppow4M, crt4M, /):
    'see:full_api4iter_unsorted_pseudo_primitive_roots_mod_,min_api4iter_pseudo_primitive_roots_mod_'
    return min_api4iter_pseudo_primitive_roots_mod_(modulus, may_p2e4M_or_ps4M_or_factor_pint_func, may_q2e4O_or_qs4O_or_factor_pint_func, may_p4M2q2e4Pmm, may_j4P2p4M, may_j4P2primitive_roots_modPpow, may_j4P2Ppow4M, may_crt4M)
def full_api4iter_unsorted_pseudo_primitive_roots_mod_(modulus, p2e4M, max_order_modM, q2e4O, p4M2q2e4Pmm, j4P2p4M, j4P2primitive_roots_modPpow, j4P2Ppow4M, crt4M, /):
    #bug:因为逻辑出错，一者取伪本原根纟各素幂模分量，一者取最大模秩纟整模(各素幂模分量投影不一定是相应伪本原根)
    r'''[[[
precondition:
    [modulus <- [2..]]
    [II__p2e_(p2e4M) == modulus]
    [max_order_modM == max_order_mod_(modulus)]
    [II__p2e_(q2e4O) == max_order_modM]
    [p4M2q2e4Pmm.keys() == p2e4M.keys()]
    [all(II__p2e_(q2e4Pmm) == p-1 for p, q2e4Pmm in p4M2q2e4Pmm.items())]
    [j4P2p4M == sorted(p2e4M.keys())]
    [j4P2primitive_roots_modPpow == [all_pseudo_primitive_roots_mod_prime_power_(p,p2e4M[p]) for p in j4P2p4M]]
    [j4P2Ppow4M == [p**p2e4M[p] for p in j4P2p4M]]
    [crt4M == mk_CRT(j4P2Ppow4M)]
        # [ordering is matter]

    'see:min_api4iter_pseudo_primitive_roots_mod_'

TODO:
    #提炼 极大值纟各素幂模分量 自 分解:q2e4O-->p4M2q2e4Pmm
    # [psphi4Ppow(p) =[def]=max_order_mod_(ppow(p))]
    # [ppow(p) =[def]= p**p2e4M[p]]
    [j4P2psphi4Ppow4M == [max_order_mod_(ppow) for ppow in j4P2Ppow4M]]
    [j4Q2q4O == sorted(q2e4O.keys())]
    [j4Q2Qpow4O == [q**q2e4O[q] for q in j4Q2q4O]]
    [j4Q2psphi4Qpow4O == [max_order_mod_(qpow) for qpow in j4Q2Qpow4O]]
    [j4Q2js4P4max_order == [[j4p for j4p,p in enumerate(j4P2p4M) if p4M2q2e4Pmm[p].get(q,0) == q2e4O[q]] for q in j4Q2q4O]]
    [radixs == radixs4j4Q2min_j4P4max_order == [map len j4Q2js4P4max_order]]
        #编码:变基数记数法
        # [(j4q,digits)=>([j4p:=j4Q2js4P4max_order[j4q][digits[j4q]]],[p:=j4P2p4M[j4p]],[q:=j4Q2q4O[j4q]]) 所指p相应素幂模分量耂伪本原根的模秩必须含偏极大因子q**q2e4O[q],而其居前的p_的对应模秩则必须不含该偏极大因子,而其居后的_p的对应模秩则随意含或不含该偏极大因子]
    #]]]'''#'''
    # arbitrary_one_pseudo_primitive_root_modM
    return _core_api4iter_pseudo_primitive_roots_mod_(j4P2primitive_roots_modPpow, crt4M)
def _core_api4iter_pseudo_primitive_roots_mod_(j4P2primitive_roots_modPpow, crt4M, /):
    for j4P2primitive_root_modP in product(*j4P2primitive_roots_modPpow):
        pseudo_primitive_root_modM = crt4M(j4P2primitive_root_modP)
        yield pseudo_primitive_root_modM
def min_api4iter_pseudo_primitive_roots_mod_(modulus, may_p2e4M_or_ps4M_or_factor_pint_func=None, may_q2e4O_or_qs4O_or_factor_pint_func=None, may_p4M2q2e4Pmm=None, may_j4P2p4M=None, may_j4P2primitive_roots_modPpow=None, may_j4P2Ppow4M=None, may_crt4M=None, /):
    'see:full_api4iter_unsorted_pseudo_primitive_roots_mod_'
    (modulus, p2e4M, max_order_modM, q2e4O, p4M2q2e4Pmm, j4P2p4M, j4P2primitive_roots_modPpow, j4P2Ppow4M, crt4M) = prepare4min_api4iter_pseudo_primitive_roots_mod_(modulus, may_p2e4M_or_ps4M_or_factor_pint_func, may_q2e4O_or_qs4O_or_factor_pint_func, may_p4M2q2e4Pmm, may_j4P2p4M, may_j4P2primitive_roots_modPpow, may_j4P2Ppow4M, may_crt4M)
    return _core_api4iter_pseudo_primitive_roots_mod_(j4P2primitive_roots_modPpow, crt4M)
def prepare4min_api4iter_pseudo_primitive_roots_mod_(modulus, may_p2e4M_or_ps4M_or_factor_pint_func, may_q2e4O_or_qs4O_or_factor_pint_func, may_p4M2q2e4Pmm, may_j4P2p4M, may_j4P2primitive_roots_modPpow, may_j4P2Ppow4M, may_crt4M, /):
    check_int_ge(2, modulus)
    p2e4M = prepare_p2e4N_(modulus, may_p2e4M_or_ps4M_or_factor_pint_func)
    max_order_modM = max_order_mod_(modulus, p2e4M)
    q2e4O = prepare_p2e4N_(max_order_modM, may_q2e4O_or_qs4O_or_factor_pint_func)
    if may_p4M2q2e4Pmm is None:
        _qs4O = sorted(q2e4O)
        p4M2q2e4Pmm = {p:complete_factor_pint_via_trial_division(_qs4O, p-1) for p in p2e4M}
    else:
        p4M2q2e4Pmm = may_p4M2q2e4Pmm
        assert p4M2q2e4Pmm.keys() == p2e4M.keys()
        assert all(II__p2e_(q2e4Pmm) == p-1 for p, q2e4Pmm in p4M2q2e4Pmm.items())
    p4M2q2e4Pmm

    j4P2p4M = sorted(p2e4M.keys()) if may_j4P2p4M is None else may_j4P2p4M
    j4P2primitive_roots_modPpow = [list_sorted_pseudo_primitive_roots_mod_prime_power__using_factorization_of_pmm_(p2e4M[p], p4M2q2e4Pmm[p], p) for p in j4P2p4M] if may_j4P2primitive_roots_modPpow is None else may_j4P2primitive_roots_modPpow
    j4P2Ppow4M = [p**p2e4M[p] for p in j4P2p4M] if may_j4P2Ppow4M is None else may_j4P2Ppow4M
    crt4M = mk_CRT(j4P2Ppow4M, extended=False) if may_crt4M is None else may_crt4M
    return (modulus, p2e4M, max_order_modM, q2e4O, p4M2q2e4Pmm, j4P2p4M, j4P2primitive_roots_modPpow, j4P2Ppow4M, crt4M)


#def order_mod_(modulus, coprime4M, psphiM_or_may_p2e4M_or_ps4M_or_factor_pint_func=None, may_p2e4psphiM_or_ps4psphiM_or_factor_pint_func=None, /):
def order_mod__fancy_(modulus, coprime4M, psphiM_or_may_p2e4M_or_ps4M_or_factor_pint_func=None, may_p2e4psphiM_or_ps4psphiM_or_factor_pint_func=None, /):
    'modulus/int{>=2} -> coprime4M/int{gcd(modulus,coprime4M)==1} -> (psphiM|may_p2e4M_or_ps4M_or_factor_pint_func=None) -> (may_p2e4psphiM_or_ps4psphiM_or_factor_pint_func=None) -> order_mod_(modulus;coprime4M) # [psphiM <- [k | [[k:<-[1..]][k%order_mod_(modulus;coprime4M)==0]]]]'
    ######################
    check_int_ge(2, modulus)
    check_type_is(int, coprime4M)
    if not are_coprime(M:=modulus, u:=coprime4M%modulus):raise ValueError(modulus, coprime4M)
    M
    u
    ######################



    ######################
    (psphiM, p2e4psphiM) = prepare_p2e4psphiM_ex_(modulus, psphiM_or_may_p2e4M_or_ps4M_or_factor_pint_func, may_p2e4psphiM_or_ps4psphiM_or_factor_pint_func)
    M
    u
    psphiM
    p2e4psphiM
    ######################


    ######################
    p_e_pairs4psphiM = sorted(p2e4psphiM.items())
    def apply_(pe, u, /):
        '(p,e) -> u -> u**p**e%M'
        (p, e) = pe
        for _ in range(e):
            u = pow(u, p, M)
        u
        return u
    it = iter_apply_commutative_operations_except_one_(apply_, p_e_pairs4psphiM, u)
        # :: (k->x->x) -> [k] -> x -> (iter x)
    p_e_pairs4out = []
    for (p, e), pw0 in zip(p_e_pairs4psphiM, it):
        pw = pw0
        ep = 0
        assert 0 == ep < e
        while not pw==1:
            if not ep < e:
                assert not pow(u, psphiM, M) == 1, (M, u, psphiM, (p,e), ep)
                raise ValueError(M, u, psphiM, (p,e), ep)
                #raise Exception(M, u, psphiM, (p,e), ep)
            pw = pow(pw, p, M)
            ep += 1
        ep
        assert 0 <= ep <= e
        if not ep == 0:
            p_e_pairs4out.append((p, ep))
        if ep == 0:
            assert pw0 == 1
        else:
            assert ep >= 1
            assert 1 < pw0 < M
        if __debug__ and not ep == 0:
            pw = apply_((p,ep-1), pw0)
            assert 1 < pw < M
            assert 1 == pow(pw, p, M)
            #assert pow(pw0, p**ep, M) == 1
            #assert apply_((p,ep), pw0) == 1
        p, ep
    p_e_pairs4out
    ######################

    order_modM_u = II__ft_e_pairs_(p_e_pairs4out)
    return order_modM_u
order_mod_ = order_mod__fancy_

def order_mod__naive_brute_force_(modulus, coprime4M, /):
    'modulus/int{>=2} -> coprime4M/int{gcd(modulus,u)==1} -> order_mod_(modulus;u)'
    check_int_ge(2, modulus)
    check_type_is(int, coprime4M)
    if not are_coprime(M:=modulus, u:=coprime4M%modulus):raise ValueError(modulus, coprime4M)
    M
    u

    pw = u
    e = 1
    while not pw==1:
        pw = pw*u%M
        e += 1
    e
    assert pow(u, e, M) == 1
    return e

def max_order_mod_(modulus, may_p2e4M_or_ps4M_or_factor_pint_func=None, /):
    'modulus/int{>=2} -> max_order_mod_(modulus)'
    check_int_ge(2, modulus)
        #ok:check_int_ge(1, modulus)
        #
    p2e4M = prepare_p2e4N_(modulus, may_p2e4M_or_ps4M_or_factor_pint_func)
    max_order_modM = lcm_many((p-1)*p**(e-(2 if p==2 and e>=3 else 1)) for p, e in p2e4M.items())
    return max_order_modM











__all__
from seed.math.max_order_mod_ import max_order_mod_
from seed.math.max_order_mod_ import order_mod__naive_brute_force_, order_mod__fancy_, order_mod_
from seed.math.max_order_mod_ import num_coprimes_lt_, phi_
from seed.math.max_order_mod_ import *
