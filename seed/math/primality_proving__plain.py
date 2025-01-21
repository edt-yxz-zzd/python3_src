#__all__:goto
#doing:goto
r'''[[[
e ../../python3_src/seed/math/primality_proving__plain.py
view ../../python3_src/nn_ns/math_nn/numbers/_patch_prime_..b001918.b002233.out.txt
    索引纟素数:素数:最小正本原根:最小素本原根
    1 3 2 2
    3 7 3 3
    8 23 5 5
view ../../python3_src/nn_ns/math_nn/numbers/b001918-least_positive_primitive_root_of_n_th_prime__fst_10000.txt
    最小正本原根
    注意:第一列是:索引纟素数，不是:素数
view ../../python3_src/nn_ns/math_nn/numbers/b002233-least_positive_prime_primitive_root_of_n_th_prime__except_0th__fst_10000.txt
    最小素本原根
    最小『素』本原根

view script/search_prime_modulus4NTT4len_is_zpow.py
    ##vs:本模块.iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
    py_adhoc_call   script.search_prime_modulus4NTT4len_is_zpow   ,100:iter_ex_prime_moduli4NTT4len_is_zpow_  +only_zpow_dominance   --min0_log2_zpow=44  --may_max1_log2_zpow=None   --min0_prime_modulus='int(2**61.99)' --max1_prime_modulus='2**62'


seed.math.primality_proving__plain
py -m seed.math.primality_proving__plain
    #see:_debug__N_eq_645
py -m nn_ns.app.debug_cmd   seed.math.primality_proving__plain -x
py -m nn_ns.app.doctest_cmd seed.math.primality_proving__plain:__doc__ -ff -v
py_adhoc_call   seed.math.primality_proving__plain   @f
from seed.math.primality_proving__plain import *


[[buggy:from old version:
git mv seed/math/_output_/seed.math.primality_proving..filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_.end-719.txt seed/math/_output_/seed.math.primality_proving..filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_.end-719.buggy.txt
    view ../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_.10.out.txt
    view ../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
]]


view others/数学/prime/primality_test.txt
    view ../../python3_src/nn_ns/math_nn/numbers/_patch_prime_.py
    view ../../python3_src/nn_ns/math_nn/numbers/_patch_prime_..b001918.b002233.out.txt
    3,5,7,11,13,17,19,31,67,73,
    2,2,3, 2, 2, 3, 2, 3, 2, 5,
    # [2 == the_least_positive_primitive_root_mod_(11)]
    # [3 == the_least_positive_primitive_root_mod_(31)]
view ../../python3_src/seed/math/primality_proving-202310.py
    ...theorem: cubic_root_case...
    merge_partial_pseudo_primitive_roots_into_single_one
        #to extact out to this module???
    contains bug since output  composite least partial_pseudo_primitive_root
    but donot skip useless remain_ft, waste time ==>> try to write new version:
view ../../python3_src/seed/math/primality_proving.py
    too fancy
        ==>> this plain version
view ../../python3_src/seed/io/continue_io.py






[[
最小正本原根的上限估值未明确
===
view others/数学/prime/primitive_root.txt
https://mathworld.wolfram.com/PrimitiveRoot.html
===
Call the least primitive root g_p.
Kearnes (1984) showed that for any positive integer m, there exist infinitely many primes p such that [m < g_p < p-m]
Burgess (1962) proved that [g_p <= C*p^(1/4+epsilon)] for C and epsilon positive constants and p sufficiently large (Ribenboim 1996, p. 24).
]]
[[[
===
===
是幺元幂根囗,是本原幺元幂根囗,是伪浅偏本原幺元幂根囗,是伪深偏本原幺元幂根囗
是拟本原根囗,是伪浅偏拟本原根囗,是伪深偏拟本原根囗
===
===
===
(伪?[浅深]偏)?拟?本原根
    10
((伪?[浅深]偏)?本原)?幺元幂根
    6
===
拟:
    [max_order_mod_(N) == phi_(N)]
    -->
    [max_order_mod_(N) <= phi_(N)]
        <==>模各素幂的本原根之综合
        ==>>[最小拟本原根不一定是素数]
===
偏: (///?)
    *浅偏:
        [pow(g,order///q4order,N) =!= 1]
        <==>模某素幂的伪浅偏本原根
        ==>>[最小伪浅偏拟本原根若存在必是素数]
            # [(N,g)互素]==>>[pow(g,max_order_mod_(N),N) == 1]
            # [N==2]==>>[伪浅偏拟本原根不存在]
        ==>>[最小伪浅偏本原幺元幂根不一定是素数]
            # [MAYBE [[(N,g)互素][pow(g,e,N) =!= 1]]]
            # [N==17][e==4][g==4] # {4,13}
    *深偏:
        [gcd(N,-1+pow(g,order///q4order,N)) == 1]
        <==>模各素幂的伪深偏本原根之综合
            # 模各素幂的伪『深』偏本原根之综合
        ==>>[最小伪深偏某某本原某某根不一定是素数]
        !! [最小伪浅偏拟本原根若存在必是素数]
        ==>>[奇素数幂模的最小伪深偏拟本原根是素数]
            # 奇素数幂模 不一定行，甚至不一定存在！
            # [是伪浅偏拟本原根囗(9;2,?) ==>> {2,5,8}]
            # [是伪浅偏拟本原根囗(9;3,?) ==>> {2,4,5,7}]
            #
            # [是伪深偏拟本原根囗(9;2,?) ==>> {2,5,8}]
            # [是伪深偏拟本原根囗(9;3,?) ==>> {}]
            #
            # [not$ 是伪深偏拟本原根囗(9;3,2)]
            #
===
伪:
    q4order     #素因子
    -->
    ft4order    #任意正因数
===
===
===
伪[浅深]偏拟本原根
    [order := max_order_mod_(N)]
    [pow(g,order,N) == 1]
    本原根 要求 其幂 遍历所有互素剩余类
        模 必须是 p4N**k, 2*p4N**k, 2, 4
        [max_order_mod_(N) == phi_(N)]
    拟本原根 只要求 模运算根秩 最大
        [max_order_mod_(N) <= phi_(N)]
        max{order_mod_(g;N) | ...}
        lcm {phi_(p4N**k) | ...}
        <==>模各素幂的本原根之综合
    伪?[浅深]偏拟?本原根 只针对特定指数因数q4order/ft4order
        拟?[max_order_mod_(N) <= phi_(N)]
        伪?ft4order
        浅偏本原根/浅偏拟本原根/伪浅偏本原根/伪浅偏拟本原根<==>模某素幂的伪浅偏本原根
            [pow(g,order///q4order,N) =!= 1]
            [pow(g,order///ft4order,N) =!= 1]
        深偏本原根/深偏拟本原根/伪深偏本原根/伪深偏拟本原根<==>模各素幂的伪深偏本原根之综合
            [gcd(N,-1+pow(g,order///q4order,N)) == 1]
            [gcd(N,-1+pow(g,order///ft4order,N)) == 1]


===
伪[浅深]偏本原幺元幂根
    幺元幂根
        [pow(g,e,N) == 1]
    本原幺元幂根
        [pow(g,e,N) == 1]
        @q4e. [pow(g,e///q4e,N) =!= 1]
    偏本原幺元幂根 只针对特定指数因数q4e
        [pow(g,e,N) == 1]
        浅偏本原幺元幂根
            [pow(g,e///q4e,N) =!= 1]
        深偏本原幺元幂根
            [gcd(N, -1+pow(g,e///q4e,N)) == 1]
    伪偏本原幺元幂根 只针对特定指数因数ft4e
        [pow(g,e,N) == 1]
        伪浅偏本原幺元幂根
            [pow(g,e///ft4e,N) =!= 1]
        伪深偏本原幺元幂根
            [gcd(N, -1+pow(g,e///ft4e,N)) == 1]
===
[N,e,g,q4e,ft4e :: pint][q4e <- all_prime_factors_of_(e)][ft4e \\\ e]:
    [是幺元幂根囗(N,e;g) =[def]= [pow(g,e,N) == 1]]
    [是本原幺元幂根囗(N,e;g) =[def]= [e == order_mod_(N;g)]]
    [是本原幺元幂根囗(N,e;g) == [[pow(g,e,N) == 1][@[q4e :<- all_prime_factors_of_(e)] -> [pow(g,e///q4e,N) =!= 1]]]]

    [是浅偏本原幺元幂根囗(N,e;q4e,g) == [[pow(g,e,N) == 1][pow(g,e///q4e,N) =!= 1]]]
    [是深偏本原幺元幂根囗(N,e;q4e,g) == [[pow(g,e,N) == 1][gcd(N, -1+pow(g,e///q4e,N)) == 1]]]

    [是伪浅偏本原幺元幂根囗(N,e;ft4e,g) == [[pow(g,e,N) == 1][pow(g,e///ft4e,N) =!= 1]]]
    [是伪深偏本原幺元幂根囗(N,e;ft4e,g) == [[pow(g,e,N) == 1][gcd(N, -1+pow(g,e///ft4e,N)) == 1]]]

[N,g,order,q4order,ft4order :: pint][q4order <- all_prime_factors_of_(order)][ft4order \\\ order][order == max_order_mod_(N)]:
    [是伪深偏拟本原根囗(N;ft4order,g) == 是伪深偏本原幺元幂根囗(N,order;ft4order,g)]
    [是伪浅偏拟本原根囗(N;ft4order,g) == 是伪浅偏本原幺元幂根囗(N,order;ft4order,g)]

    [是深偏拟本原根囗(N;q4order,g) == 是深偏本原幺元幂根囗(N,order;q4order,g)]
    [是浅偏拟本原根囗(N;q4order,g) == 是浅偏本原幺元幂根囗(N,order;q4order,g)]

    [是拟本原根囗(N;g) == 是本原幺元幂根囗(N,order;g)]

    [order == max_order_mod_(N) == phi_(N)]:
        [是伪深偏本原根囗(N;ft4order,g) == 是伪深偏本原幺元幂根囗(N,order;ft4order,g)]
        [是伪浅偏本原根囗(N;ft4order,g) == 是伪浅偏本原幺元幂根囗(N,order;ft4order,g)]

        [是深偏本原根囗(N;q4order,g) == 是深偏本原幺元幂根囗(N,order;q4order,g)]
        [是浅偏本原根囗(N;q4order,g) == 是浅偏本原幺元幂根囗(N,order;q4order,g)]

        [是本原根囗(N;g) == 是本原幺元幂根囗(N,order;g)]


===
===
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

===
===
[not$ using_gcd][N=>Nmm=>q4Nmm=>g4q4Nmm]:
    [@[N :<- [2..]] -> [@[q4Nmm :<- all_prime_factors_of_(N-1)] -> ?[g4q4Nmm :<- [2..<N]] -> [[pow(g4q4Nmm, (N-1), N) == 1][pow(g4q4Nmm, (N-1)///q4Nmm, N) =!= 1]]] -> [is_prime_(N)]]
        # [:素性证明囗囗减一囗囗完全分解]:here
===
[using_gcd][N=>Nmm=>ft4Nmm=>e4ft4Nmm/g4ft4Nmm/B4ft4Nmm]:
    [@[N :<- [2..]] -> @[L :<- [0..]] -> @[j2ft4Nmm,j2e4ft4Nmm,j2g4ft4Nmm,j2B4ft4Nmm :: [pint]{len=L}] -> [@[j :<- [0..<L]] -> [j2B4ft4Nmm[j] <= min 2 all_prime_factors_of_(j2ft4Nmm[j])]] -> [fff_(j2x) := (II [j2x[j]**j2e4ft4Nmm[j] | [j :<- [0..<L]]])] -> [fff_(j2ft4Nmm) \\\ (N-1)] -> [@[j :<- [0..<L]] -> [[pow(j2g4ft4Nmm[j], (N-1), N) == 1][gcd(N, -1+pow(j2g4ft4Nmm[j], (N-1)///j2ft4Nmm[j], N)) == 1]]] -> [[@[p4N :<- all_prime_factors_of_(N)] -> [p4N >= (fff_(j2B4ft4Nmm) +1)]][N < (fff_(j2B4ft4Nmm) +1)**2] -> [is_prime_(N)]]]
        # [:素性证明囗囗减一囗囗部分分解囗囗平方根规模]:here
===
===
===
[not$ using_gcd][N/g=>order4g_N=>q4order4g_N]:
    [@[N :<- [2..]] -> @[g,order4g_N :: pint] -> [pow(g, order4g_N, N) == 1] -> [@[q4order4g_N :<- all_prime_factors_of_(order4g_N)] -> [pow(g, (order4g_N)///q4order4g_N, N) =!= 1]] -> [order4g_N == order_mod_(N;g)]]
        # [:模运算根秩证明囗囗完全分解]:here
===
[not$ using_gcd][N/order=>q4order=>g4q4order_N]:
    [@[N :<- [2..]] -> @[order :: pint] -> [@[q4order :<- all_prime_factors_of_(order)] -> ?[g4q4order_N :: int] -> [[pow(g4q4order_N, order, N) == 1][pow(g4q4order_N, (order)///q4order, N) =!= 1]]] -> [order \\\ max_order_mod_(N)]]
        # [:模运算总根秩的因数证明囗囗完全分解]:here

===
[not$ using_gcd][N/e=>q4e=>g4q4e_N]:
    [@[N :<- [2..]] -> @[e :: pint] -> @[q4e :<- all_prime_factors_of_(e)] -> @[g4q4e_N :: int] -> [[pow(g4q4e_N, e, N) == 1][pow(g4q4e_N, (e)///q4e, N) =!= 1]] -> [q4e**gde_(q4e;e) \\\ max_order_mod_(N)]]
        # [:模运算总根秩的素因子部分幂证明囗囗特定素因子]:here
===
[using_gcd][N/e=>q4e=>g4q4e_N]:
    [@[N :<- [2..]] -> @[e :: pint] -> @[q4e :<- all_prime_factors_of_(e)] -> @[g4q4e_N :: int] -> [[pow(g4q4e_N, e, N) == 1][gcd(N, -1+pow(g4q4e_N, (e)///q4e, N)) == 1]] -> [@[p4N :<- all_prime_factors_of_(N)] -> [q4e**gde_(q4e;e) \\\ (p4N-1)]]]
        # [:模运算总根秩的素因子部分幂整除模因数减一证明囗囗特定素因子]:here

===
===
[not$ using_gcd][N/e=>x4e]:
    #e.g. [e := Nmm///q4Nmm]
    [@[N :<- [2..]] -> @[e :<- [1..]] -> @[x4e :<- [1..<N]] -> [@[_x4e :<- [2..<x4e]] -> [pow(_x4e, e, N) == 1]] -> [[@[_x4e,_y4e :<- [1..<x4e]] -> [pow(_x4e*_y4e, e, N) == 1]][[pow(x4e, e, N) =!= 1] -> [is_prime_(x4e)]]]]
    [@[N :<- [2..]] -> @[e :<- [1..]] -> @[x4e :<- [1..<N]] -> [@[_x4e :<- [2..<x4e]] -> [pow(_x4e, e, N) == 1]] -> [[pow(x4e, e, N) =!= 1] -> [[not$ max_order_mod_(N) \\\ e]or[x4e =!= the_min_prime_factors_of_(N)]or[x4e == the_least_positive_partial_pseudo_primitive_root_mod_(N,max_order_mod_(N);max_order_mod_(N)///e,using_gcd=False)]]]]
        # ++互素 => [:最小伪浅偏拟本原根若存在必是素数]:here
        # => [奇素数幂模的最小伪深偏拟本原根是素数]:here
        # => [:只需枚举素数兼检测整除与否@素性证明囗囗减一囗囗完全分解]:here
        #
===
===
TODO:证明以上定理
===
===
===
the_least_positive_partial_pseudo_primitive_root_mod_
===
]]]


[[[
copy from:
  view ../../python3_src/seed/math/primality_proving__plain.py
copy to:
    view others/数学/prime/primitive_root.txt
===
给定素数p，p最小 的 平方非剩余 必定是 素数
给定素数p，p最小 的 本原根 不一定是 素数
    本原根 相当于 merge_partial_pseudo_primitive_roots_into_single_one，所以 最小者 不一定是 素数
===
但是，p最小的 ft-partial_pseudo_primitive_root<p> 必定是 素数
    [:素数模的前提下囗囗最小正偏伪本原根必是素数]:goto
    [:此前未发现模的非平凡因子的前提下囗囗最小正偏伪本原根必是素数]:goto
===
[[is_prime_(N)] -> [N%2 == 1] -> [[is_a_partial_pseudo_primitive_root_mod_(N,N-1,2; g, using_gcd=False)] <-> [is_a_quadratic_nonresidue_mod_(N; g)]]]
    [:关于二的偏伪本原根等价于与模互素的平方非剩余]:goto

TODO:
xxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxx
===definitions:
######################new-definitions:
# qualifier: partial + pseudo
    # partial: pass test for not-necessary-all factors
    # pseudo: [gcd(pseudo_order, max_order_mod_(modulus)) <= max_order_mod_(modulus) <= phi_(modulus)]
        # xxx pseudo: pass test for not-necessary-prime factor
        # pseudo <-- [max_order_mod_(modulus) =?= phi_(modulus)][primitive_root generate all coprime residue classes]
        # primitive_root second explain come from kth_root_of() e.g. kth-primitive_root of unity
        #   primitive n-th roots of unity
        #   partial_ft be prime, pass test for all prime factors
        #   partial_ft be prime, pass test for necessary-enough prime factors
        #   [pseudo_order \\\ max_order_mod_(modulus) \\\ phi_(modulus)]
        #
    #
#
[m :<- [1..]][x :: int]:
    [is_a_nontrivial_factor_of_(m; x) =[def]= [[2 <= x < m][m %x == 0]]]
[x,y :: int]:
    [are_coprime_(m, x) =[def]= [gcd(x,y) == 1]]

[@[modulus :<- [2..]] -> @[x :: int] -> [[x %modulus == 1] <-> [gcd(modulus, x-1) == 0]]]
[@[modulus :<- [2..]] -> @[x :: int] -> [[x %modulus =!= 1] <-> [1 <= gcd(modulus, x-1) < modulus]]]
[@[modulus :<- [2..]] -> @[x :: int] -> [1 == [gcd(modulus, x-1) == 0] + [gcd(modulus, x-1) == 1] + [2 <= gcd(modulus, x-1) < modulus]]]

[@[modulus :<- [2..]] -> @[x :: int] -> [1 == [x %modulus == 1] + [are_coprime_(modulus, x-1)] + [is_a_nontrivial_factor_of_(modulus; gcd(modulus, x-1))]]]
[@[modulus :<- [2..]] -> @[e :<- [1..]] -> @[x,y :: int] -> [x**e %modulus == 1] -> [y**e %modulus == 1] -> [(x*y)**e %modulus == 1]]
[@[modulus :<- [2..]] -> @[e :<- [1..]] -> [x := modulus] -> [0 == x**e %modulus =!= 1]]
[@[modulus :<- [2..]] -> @[e :<- [1..]] -> [x :<- all_prime_factors_of_(modulus)] -> [x**e %modulus =!= 1]]
    # existence
    # [:positive_non_unity_root_exists]:here
[@[modulus :<- [2..]] -> @[e :<- [1..]] -> [x := min{x | [x :<- [1..=the_min_prime_factors_of_(modulus)]][x**e %modulus =!= 1]}] -> [is_prime_(x)]]
    # [:min_positive_non_unity_root_is_prime]:here
        # primitive n-th roots of unity

[modulus :<- [2..]][e :<- [1..]][g :: int]:
    [is_non_unity_root_mod_(modulus, e; g) =[def]= [g**e %modulus =!= 1]]
    [is_unity_root_mod_(modulus, e; g) =[def]= [g**e %modulus == 1]]
    [[is_unity_root_mod_(modulus, e; g)] -> [gcd(g,modulus) == 1]]
        # [:unity_root_is_coprime]:here

[modulus :<- [2..]][pseudo_order :<- [1..<modulus]][partial_ft :<- [2..=pseudo_order]][pseudo_order %partial_ft == 0][using_gcd :: bool][g :: int]:
    [is_a_partial_pseudo_primitive_root_mod_(modulus, pseudo_order, partial_ft; g, *, using_gcd) =[def]= [[g**pseudo_order %modulus == 1][if using_gcd then [gcd(modulus, 1 - g**(pseudo_order///partial_ft) %modulus) == 1] else [g**(pseudo_order///partial_ft) %modulus =!= 1]]]]
    #bug?: [g**(pseudo_order///partial_ft) %modulus =!= 1] vs [gcd(modulus, 1 - g**(pseudo_order///partial_ft) %modulus) == 1]
    # ++using_gcd:
    #   is_a_partial_pseudo_primitive_root_mod_
    #   all_std_partial_pseudo_primitive_roots_mod_
    #   the_least_positive_partial_pseudo_primitive_root_mod_
    #   exists_a_partial_pseudo_primitive_root_mod_

    # drop qualifier 'pseudo'
    # xxx:unclear:pseudo:xxx [is_a_partial_primitive_root_mod_(modulus, pseudo_order, partial_ft; g, ?using_gcd?) =[def]= [[is_prime_(partial_ft)][is_a_partial_pseudo_primitive_root_mod_(modulus, pseudo_order, partial_ft; g, using_gcd=???)]]]
    ######################
    [[is_a_partial_pseudo_primitive_root_mod_(modulus, pseudo_order, partial_ft; g, using_gcd=True)] -> [is_a_partial_pseudo_primitive_root_mod_(modulus, pseudo_order, partial_ft; g, using_gcd=False)]]
    [[is_a_partial_pseudo_primitive_root_mod_(modulus, pseudo_order, partial_ft; g, using_gcd=False)] -> [is_non_unity_root_mod_(modulus, pseudo_order///partial_ft; g)]]
    ######################
    [[is_a_partial_pseudo_primitive_root_mod_(modulus, pseudo_order, partial_ft; g, using_gcd=using_gcd)] -> [is_non_unity_root_mod_(modulus, pseudo_order///partial_ft; g)]]
        # !! [:min_positive_non_unity_root_is_prime]:goto
        # ???existence??? => min_positive_partial_pseudo_primitive_root_is_prime
        # min_positive_partial_pseudo_primitive_root_is_prime_or_nonexists
    ######################

[modulus :<- [2..]][order :<- [1..<modulus]][g :: int]:
    # drop qualifier 'partial'
    [is_a_pseudo_primitive_root_mod_(modulus, order; g) =[def]= [@[p4order :<- all_prime_factors_of_(order] -> [is_a_partial_pseudo_primitive_root_mod_(modulus, order, p4order; g, using_gcd=False)]]]
        # =[def]= primitive n-th roots of unity

[modulus :<- [2..]][max_order_mod_(modulus) == phi_(modulus)][order :<- [1..<modulus]][g :: int]:
    # drop qualifier 'partial'_'pseudo'
        # [primitive_root generate all coprime residue classes]
        # [modulus is of form 2, 4, p**k, 2*p**k where p is odd prime]
    [is_a_primitive_root_mod_(modulus, order; g) =[def]= is_a_pseudo_primitive_root_mod_(modulus, order; g)]

[e,ft,n :: pint][e %ft == 0]:
    [_is_effective_ft_(n;e,ft) =[def]= [gcd(n,e///ft) < gcd(n,e)]]
        # [n := max_order_mod_(modulus)][e := pseudo_order][order := gcd(n,e)][partial_ft := gcd(n,e)///gcd(n,e///ft)]: [2 <= partial_ft <= order < modulus >= 3][?[g :<- [2..<modulus]] -> [is_a_pseudo_primitive_root_mod_(modulus, order; g)]]
    [[_is_effective_ft_(n;e,ft)] -> [ft >= 2]]
    [[_is_effective_ft_(n;e,ft)] <-> [[d := gcd(n,e)][gcd(d,e///ft) < d]]]
    TODO:_is_effective_ft_
xxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxx
[modulus :<- [2..]][pseudo_order :<- [1..<modulus]][partial_ft :<- [2..=pseudo_order]][pseudo_order %partial_ft == 0][using_gcd :: bool]:
    [all_std_partial_pseudo_primitive_roots_mod_(modulus, pseudo_order; partial_ft, *, using_gcd) =[def]= {g | [[g :<- [1..<modulus]][is_a_partial_pseudo_primitive_root_mod_(modulus, pseudo_order, partial_ft; g, using_gcd=using_gcd)]]}]
    [exists_a_partial_pseudo_primitive_root_mod_(modulus, pseudo_order; partial_ft, *, using_gcd) =[def]= [len(all_std_partial_pseudo_primitive_roots_mod_(modulus, pseudo_order; partial_ft, using_gcd=using_gcd)) > 0]]
    #bug: [[exists_a_partial_pseudo_primitive_root_mod_(modulus, pseudo_order; partial_ft, using_gcd=False)] <-> [gcd(partial_ft, max_order_mod_(modulus)) =!= 1]]
    #bug: [[exists_a_partial_pseudo_primitive_root_mod_(modulus, pseudo_order; partial_ft, using_gcd=True)] <-> [gcd(partial_ft, core_order_mod_(modulus)) =!= 1]]
    #_is_effective_ft_(n;e,ft)
    [[exists_a_partial_pseudo_primitive_root_mod_(modulus, pseudo_order; partial_ft, using_gcd=False)] <-> [_is_effective_ft_(max_order_mod_(modulus); pseudo_order, partial_ft)]]
    [[exists_a_partial_pseudo_primitive_root_mod_(modulus, pseudo_order; partial_ft, using_gcd=True)] <-> [_is_effective_ft_(core_order_mod_(modulus); pseudo_order, partial_ft)]]

[modulus :<- [2..]][pseudo_order :<- [1..<modulus]][partial_ft :<- [2..=pseudo_order]][pseudo_order %partial_ft == 0][using_gcd :: bool][exists_a_partial_pseudo_primitive_root_mod_(modulus, pseudo_order; partial_ft, using_gcd=using_gcd)]:
    # is_the_least_positive-partial_pseudo_primitive_root
    [the_least_positive_partial_pseudo_primitive_root_mod_(modulus, pseudo_order; partial_ft, *, using_gcd) =[def]= min(all_std_partial_pseudo_primitive_roots_mod_(modulus, pseudo_order; partial_ft, using_gcd=using_gcd))]

[modulus :<- [2..]][g :<- [1..<modulus]][gcd(g, modulus) == 1]:
    [order_mod_(modulus; g) =[def]= min{e | [[e :<- [1..<modulus]][g**e %modulus == 1]]}]

[modulus :<- [2..]]:
    [all_partial_orders_mod_(modulus) =[def]= [((p4M-1) *p4M**(gde_(p4M;modulus)-1 -[p4M==2][modulus%8==0])) | [p4M :<- all_prime_factors_of_(modulus)]]]
    ######################
    [core_order_mod_(modulus) =[def]= gcd(all_partial_orders_mod_(modulus))]
    ######################
    [max_order_mod_(modulus) =[def]= max{order_mod_(modulus; g) | [[g :<- [1..<modulus]][gcd(g, modulus) == 1]]}]
    ######################
    [max_order_mod_(modulus) == lcm(all_partial_orders_mod_(modulus))]
    ######################
    [@[g :<- [1..<modulus]] -> [gcd(g, modulus) == 1] -> [g**order_mod_(modulus) %modulus == 1]]
    [@[g :<- [1..<modulus]] -> [gcd(g, modulus) == 1] -> [max_order_mod_(modulus) %order_mod_(modulus;g) == 0]]
    [@[g :<- [1..<modulus]] -> [gcd(g, modulus) == 1] -> [g**max_order_mod_(modulus) %modulus == 1]]
    ######################
    [?[g :<- [1..<modulus]] -> [gcd(g, modulus) == 1] -> [max_order_mod_(modulus) == order_mod_(modulus;g)]]
        #g is pseudo_primitive_root
    ######################
    [@[pseudo_order :<- all_factors_of(max_order_mod_(modulus))] -> ?[g :<- [1..<modulus]] -> [gcd(g, modulus) == 1] -> [pseudo_order == order_mod_(modulus;g)]]
    ######################
    [max_order_mod_(modulus) == lcm{order_mod_(modulus;g) | [[g :<- [1..<modulus]][gcd(g, modulus)]]}]
    ######################
    [[max_order_mod_(modulus) %2 == 0] <-> [modulus >= 3]]
    [[modulus >= 3] -> [[is_a_partial_pseudo_primitive_root_mod_(modulus, max_order_mod_(modulus), 2; g, using_gcd=False)] <-> [[gcd(g,modulus) == 1][is_a_quadratic_nonresidue_mod_(modulus; g)]]]]
        # [:关于二的偏伪本原根等价于与模互素的平方非剩余]:here
        ######################
        # from: [[is_prime_(N)] -> [N%2 == 1] -> [[is_a_partial_pseudo_primitive_root_mod_(N,N-1,2; g, using_gcd=False)] <-> [is_a_quadratic_nonresidue_mod_(N; g)]]]
    ######################

# min_positive_partial_pseudo_primitive_root_is_prime_or_nonexists
[[[modulus :<- [2..]][pseudo_order :<- [1..<modulus]][partial_ft :<- [2..=pseudo_order]][pseudo_order %partial_ft == 0][using_gcd :: bool][exists_a_partial_pseudo_primitive_root_mod_(modulus, pseudo_order; partial_ft, using_gcd=using_gcd)]]
    -> [g4ft :<- [1..<modulus]]
    -> [[pseudo_order %max_order_mod_(modulus) == 0]or[[b :<- [2..<g4ft]] -> [is_prime_(b)] -> [modulus %b =!= 0] -> [b**pseudo_order %modulus == 1]]]
    #xxx -> [[using_gcd==False] -> [b :<- [2..<g4ft]] -> [is_prime_(b)] -> [modulus %b =!= 0] -> [b**(pseudo_order///ft) %modulus =!= 1]]
    -> [[using_gcd==True] -> [b :<- [2..<g4ft]] -> [is_prime_(b)] -> [modulus %b =!= 0] -> [gcd(modulus, b**(pseudo_order///ft) %modulus -1) == 1]]
    #xxx -> [[b :<- [2..<g4ft]] -> [is_prime_(b)] -> [modulus %b =!= 0] -> [b**(pseudo_order///ft) %modulus == 1]]
        # [:此前未发现模的非平凡因子的前提]:here
        # xxx [:此前未发现模的非平凡因子或合数证据的前提]:here
        # !! [:min_positive_non_unity_root_is_prime]:goto
        # !! [g4ft**(pseudo_order///partial_ft) %modulus =!= 1]
        # => [is_prime_(g4ft)]
        # => [is_prime_(b)]
        # !! [:unity_root_is_coprime]:goto
        # !! [g4ft**pseudo_order %modulus == 1]
        # => [gcd(g4ft,modulus) == 1]
        # => [modulus %g4ft =!= 0]
        # => [modulus %b =!= 0]
        # the conclusion ok: [b**pseudo_order %modulus == 1]
        #   instead of using_gcd: [gcd(modulus, b**pseudo_order %modulus -1) =!= 1]
        # since:
        #   * [gcd(modulus, b**pseudo_order %modulus -1) > 1] ==>> [found nontrivial_factor of modulus]
        #   * [gcd(modulus, b**pseudo_order %modulus -1) < 1] ==>> [b**pseudo_order %modulus == 1]
        #
        # [[gcd(modulus, b**pseudo_order %modulus -1) == 0] -> [gcd(modulus, b**pseudo_order %modulus -1) =!= 1]]
        # [[gcd(modulus, b**pseudo_order %modulus -1) == 0] <-> [b**pseudo_order %modulus == 1]]
        # [is_prime_(modulus)] ==>> [[gcd(modulus, b**pseudo_order %modulus -1) =!= 1] <-> [gcd(modulus, b**pseudo_order %modulus -1) == 0] <-> [b**pseudo_order %modulus == 1]]
        #   [:素数模的前提]:here
        # [[:素数模的前提] -> [:此前未发现模的非平凡因子的前提]]
        # 模为素数平方 都 不行:
        #   [modulus := 3**2][pseudo_order := 6][partial_ft := 3][b := 2]
xxxxxxxxxxxx doing 赫拉 海格 鬼畜 纵队
        #   [6 == phi(9)]
        #   [gcd(9, 2**(6///3)%9 -1) == 3]
        #       #发现模的非平凡因子
        #   1
        #   2 --> 4(4-1==3) --> 8 --> 7 --> 5 --> 1  #3:nontrivial_factor
        #   4 --> 7(7-1==6:3) --> 1
        #   5 --> 7(7-1==6:3) --> 8 --> 4 --> 2 --> 1
        #   7 --> 4(4-1==3) --> 1
        #   8 --> 1
        #   [6 == phi(9)]
        #   [2 == the_least_positive_partial_pseudo_primitive_root_mod_(9, phi(9); 3, using_gcd=False)]
        #   [2 == the_least_positive_partial_pseudo_primitive_root_mod_(9, phi(9); 2, using_gcd=False)]
        #   [2 == the_least_positive_pseudo_primitive_root_mod_(9, phi(9))]
        #   [2 == the_least_positive_primitive_root_mod_(9)]
        #
    #???xxx -> [g4ft == the_least_positive_partial_pseudo_primitive_root_mod_(modulus, pseudo_order; partial_ft, using_gcd=using_gcd???doing)]
    -> [g4ft == the_least_positive_partial_pseudo_primitive_root_mod_(modulus, pseudo_order; partial_ft, using_gcd=False)]
    -> [[is_prime_(g4ft)][modulus %g4ft =!= 0]]
    ]
    # [:此前未发现模的非平凡因子的前提下囗囗最小正偏伪本原根必是素数]:here
        # [:此前未发现模的非平凡因子的前提]:goto
    # => [:素数模的前提下囗囗最小正偏伪本原根必是素数]:here
        # [:素数模的前提]:goto
    ######################
    # from: [[0 < g4ft4Nmm < N] -> [[is_prime_(N)]or[[b :<- [2..<g4ft4Nmm]] -> [is_prime_(b)] -> [b**Nmm %N == 1]]] -> [g4ft4Nmm == the_least_positive_partial_pseudo_primitive_root_mod_(N, Nmm; ft4Nmm, using_gcd=using_gcd???doing)] -> [is_prime_(g4ft4Nmm)]]
    ######################
    [[proof:
    [pseudo_order %max_order_mod_(modulus) == 0]:
        !! [@[g :<- [1..<modulus]] -> [gcd(g, modulus) == 1] -> [g**max_order_mod_(modulus) %modulus == 1]]
        [@[g :<- [1..<modulus]] -> [gcd(g, modulus) == 1] -> [g**pseudo_order %modulus == 1]]
        !! [g4ft :<- [1..<modulus]]
        [[b :<- [2..<g4ft]] -> [is_prime_(b)] -> [modulus %b =!= 0] -> [b**pseudo_order %modulus == 1]]

    [[pseudo_order %max_order_mod_(modulus) == 0] -> [[b :<- [2..<g4ft]] -> [is_prime_(b)] -> [modulus %b =!= 0] -> [b**pseudo_order %modulus == 1]]]
    !! [[pseudo_order %max_order_mod_(modulus) == 0]or[[b :<- [2..<g4ft]] -> [is_prime_(b)] -> [modulus %b =!= 0] -> [b**pseudo_order %modulus == 1]]]
    [[b :<- [2..<g4ft]] -> [is_prime_(b)] -> [modulus %b =!= 0] -> [b**pseudo_order %modulus == 1]]
    [[b :<- [2..<g4ft]] -> [gcd(g, modulus) == 1] -> [b**pseudo_order %modulus == 1]]
    !! [g4ft == the_least_positive_partial_pseudo_primitive_root_mod_(modulus, pseudo_order; partial_ft, using_gcd=using_gcd???doing)]
    [[b :<- [2..<g4ft]] -> [gcd(g4ft, modulus) == 1] -> [b**(pseudo_order///partial_ft) %modulus == 1]]
        #bug: 
        ??? [gcd(modulus, 1 - b**(pseudo_order///partial_ft) %modulus) =!= 1]
        pseudo <-- [max_order_mod_(modulus) =?= phi_(modulus)][primitive_root generate all coprime residue classes]
        [gcd(modulus, 1 - b**(pseudo_order///partial_ft) %modulus) =!= 1] -> nontrivial_factor or 0/[b**(pseudo_order///partial_ft) %modulus == 1]
            not bug!



    [not$ is_prime_(g4ft)]:
        [(u,v) :=> [1 < u <= v < g4ft == u*v]]
        !! [g4ft == the_least_positive_partial_pseudo_primitive_root_mod_(modulus, pseudo_order; partial_ft, using_gcd=using_gcd???doing)]
        [gcd(g4ft, modulus) == 1]
        [gcd(u, modulus) == 1]
        [gcd(v, modulus) == 1]
        !! [[b :<- [2..<g4ft]] -> [gcd(g, modulus) == 1] -> [b**(pseudo_order///partial_ft) %modulus == 1]]
        [u**(pseudo_order///partial_ft) %modulus == 1]
        [v**(pseudo_order///partial_ft) %modulus == 1]
        [(u*v)**(pseudo_order///partial_ft) %modulus == 1]
        [g4ft**(pseudo_order///partial_ft) %modulus == 1]
        !! [g4ft == the_least_positive_partial_pseudo_primitive_root_mod_(modulus, pseudo_order; partial_ft, using_gcd=using_gcd???doing)]
        [g4ft**(pseudo_order///partial_ft) %modulus =!= 1]
        _L
    [is_prime_(g4ft)]
    :DONE
    ]]



######################old-definitions:
[g4q4Nmm is_a q4Nmm-partial_primitive_root<N>] =[def]=:
    [is_prime_(q4Nmm)]
    [g4q4Nmm is_a q4Nmm-partial_pseudo_primitive_root<N>]

[g4ft4Nmm is_a ft4Nmm-partial_pseudo_primitive_root<N>] =[def]=:
    #partial: ft4Nmm only (not all nontrivial factors of Nmm)
    #pseudo => not-require: [is_prime_(ft4Nmm)]
    #
    [N == Nmm +1]
    [Nmm %ft4Nmm == 0]
    [g4ft4Nmm**Nmm %N == 1]
    [g4ft4Nmm**(Nmm///ft4Nmm) %N =!= 1]

===
[[0 < g4ft4Nmm < N] -> [[is_prime_(N)]or[[b :<- [2..<g4ft4Nmm]] -> [is_prime_(b)] -> [b**Nmm %N == 1]]] -> [g4ft4Nmm is_the_least_positive ft4Nmm-partial_pseudo_primitive_root<N>] -> [is_prime_(g4ft4Nmm)]]
    [[proof:
    !! [[is_prime_(N)]or[[b :<- [2..<g4ft4Nmm]] -> [is_prime_(b)] -> [b**Nmm %N == 1]]]
    * [is_prime_(N)]:
        !! [is_prime_(N)]
        [[b :<- [1..<N]] -> [b**Nmm %N == 1]]
        !! [0 < g4ft4Nmm < N]
        [[b :<- [2..<g4ft4Nmm]] -> [b**Nmm %N == 1]]

    * [[b :<- [2..<g4ft4Nmm]] -> [is_prime_(b)] -> [b**Nmm %N == 1]]
        !! [[b :<- [2..<g4ft4Nmm]] -> [is_prime_(b)] -> [b**Nmm %N == 1]]
        [[b :<- [2..<g4ft4Nmm]] -> [b**Nmm %N == 1]]

    [[b :<- [2..<g4ft4Nmm]] -> [b**Nmm %N == 1]]

    !! [g4ft4Nmm is_the_least_positive ft4Nmm-partial_pseudo_primitive_root<N>]
    [[b :<- [2..<g4ft4Nmm]] -> [not$ b is_a ft4Nmm-partial_pseudo_primitive_root<N>]]
    !! [[b :<- [2..<g4ft4Nmm]] -> [b**Nmm %N == 1]]
    [[b :<- [2..<g4ft4Nmm]] -> [b**(Nmm///ft4Nmm) %N == 1]]


    [g4ft4Nmm == a*b][1 < a <= b < g4ft4Nmm]:
        !! [[b :<- [2..<g4ft4Nmm]] -> [b**(Nmm///ft4Nmm) %N == 1]]
        [a**(Nmm///ft4Nmm) %N == 1]
        [b**(Nmm///ft4Nmm) %N == 1]
        [(a*b)**(Nmm///ft4Nmm) %N == 1]
        [g4ft4Nmm**(Nmm///ft4Nmm) %N == 1]
        !! [g4ft4Nmm is_the_least_positive ft4Nmm-partial_pseudo_primitive_root<N>]
        [g4ft4Nmm**(Nmm///ft4Nmm) %N =!= 1]
        _L
    [is_prime_(g4ft4Nmm)]
    :DONE
    ]]

===
example for: [[g4ft4Nmm is_the_least_positive ft4Nmm-partial_pseudo_primitive_root<N>] -> [is_prime_(g4ft4Nmm)]]
    view ../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_.10.out.txt
    view ../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
        (14, 3, 12, 11)
        (15, 9, 11, 5)
        (16, 5, 13, 3)
        (17, 1, 16, 3)
        (18, 5, 15, 3)
        (19, 33, 13, 5)
        (20, 3, 18, 5)
    found bug@view ../../python3_src/seed/math/primality_proving-202310.py
        view ../../python3_src/seed/math/_output_/seed.math.primality_proving..filter_out_composites___output5iter_odd_primes__one_prime_per_bit_length_.end-719.txt
        (14, 3<<12^1, [22, 2])
        (15, 9<<11^1, [10, 2])
        (16, 5<<13^1, [6, 2])
        (17, 1<<16^1, [6])
        (18, 5<<15^1, [6, 2])
        (19, 33<<13^1, [10, 2])
        (20, 3<<18^1, [10, 2])
===
===
]]]
[[[
===
doing:[modulus :<- [2..]][pseudo_order :<- [1..<modulus]][L :<- [1..]][j2ft,j2e,j2prime_lowbound4ft :: [pint]{len=L}][partial_ft := II~ j2ft[j]**j2e[j] ~{j :<- [0..<L]}][partial_lowbound := II~ j2prime_lowbound4ft[j]**j2e[j] ~{j :<- [0..<L]}][pseudo_order %partial_ft == 0][j2g :: [int]{len=L}][][][][][][partial_ft :<- [2..=pseudo_order]][pseudo_order %partial_ft == 0][g :: int]:
    [@[j :<- [0..<L]] -> @[p4ft :<- all_prime_factors_of_(j2ft[j])] -> [p4ft >= %j2prime_lowbound4ft[j]]]
    [@[j :<- [0..<L]] -> [is_a_partial_pseudo_primitive_root_mod_(modulus, pseudo_order, j2ft[j]; j2g[j], using_gcd=???)]]
  # j2ft neednot be pairwise-coprime
]]]
bug!!!:[(e5B+1)**2 > m]
    [(e5B+1)**2 > m-1]
    [(e5B+1)**2 > phi(m)]
    [(e5B+1)**2 > max_order_mod_(m)]
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
TODO:
    定理 lowB 证明 复制
        e others/数学/prime/primality_test.txt
            最小正偏伪本原根 必是 素数
    实现 lowB:
        validate_prime_certificate__Nmm__partial_factorization__gt_sqrtN_
        Tester4prime_via_Nmm__sqrt_case
DONE:
    generalize: zpow --> radix pow

        RadixPowDominancePlusplusOddNumberRelated:goto
        iter_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_:goto

DONE:
    load output, mk validatable
        _iter_read_output4zpow:goto
        _mk_validatable4zpow:goto


DONE:
    extend primality_test_of_Miller_Rabin
        new_version_test6Tester4composite_via_even_Nmm:goto
]]


g - partial_pseudo_primitive_root
z - 2
    zpow == 2pow == 2**ez == 2**e2
    ez == e2
    gz == g2
[Nmm := N-1] # --N
[Npp := N+1] # ++N
zpow_dominance N primality certificate case:
    0:prime:gz
        # partial_pseudo_primitive_root<2>
        # [gcd(gz**(Nmm///2) %N -1, N) == 1][N < (2**ez4Nmm+1)**2]
    1:composite:witness4composite
        # [witness4composite**Nmm %N =!= 1]
        #   otherwise found more unity roots ==>> nontrivial_factor
    2:composite:nontrivial_factor
        # [2 <= nontrivial_factor < N][N %nontrivial_factor == 0]
    #see:iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_

[[[
===
[@[n >= 1] -> [2*ln(n)**2 < (1+floor_log2(n))**2]]
[@[n <- [2**48..]] -> [2*ln(n)**2 < 1+floor_log2(n)**2]]
    [@[n <- [2**48..]] -> [2*ln(n)**2 < floor_log2(n)**2]]
===
proof___floor_log2_ver___ERH:here
???[@[n >= 1] -> [2*ln(n)**2 < (1+floor_log2(n))**2]]???
    # ERH: [2..<2*ln(n)**2]
    !! [n >= 1]
    [0 <= ln(n) == (log2(n)/log2(math.e)) < log2(n)]
    [0 <= ln(n)**2 == (log2(n)/log2(math.e))**2 < log2(n)**2]
    !! [log2(math.e)**2 > 2]
    [2*ln(n)**2 == 2*(log2(n)/log2(math.e))**2 < log2(n)**2 <= ceil_log2(n)**2 < (1+floor_log2(n))**2]
    [2*ln(n)**2 < (1+floor_log2(n))**2]
===
???[@[n <- [2**48..]] -> [2*ln(n)**2 < 1+floor_log2(n)**2]]???
    !! [2*ln(2**48 -1)**2 > 1+floor_log2(2**48 -1)**2]
    !! [2*ln(2**49 -1)**2 < 1+floor_log2(2**49 -1)**2]
    !! [@[n >= 1] -> [2*ln(n)**2 < (1+floor_log2(n))**2]]
===
>>> from math import log as ln, log2, floor
>>> from math import e

######################
>>> log2(e)
1.4426950408889634
>>> log2(e)**2
2.0813689810056077
>>> log2(e)**2 > 2
True

######################
>>> lb = lambda n:floor(log2(n))
>>> f = lambda n:2*ln(n)**2
>>> g = lambda n:(1+lb(n))**2
>>> h = lambda n:1+lb(n)**2


######################
>>> [f(10**e) for e in range(9)]
[0.0, 10.603796220956799, 42.415184883827195, 95.43416598861116, 169.66073953530878, 265.0949055239199, 381.7366639544446, 519.586014826883, 678.6429581412351]
>>> [g(10**e) for e in range(9)]
[1, 16, 49, 100, 196, 289, 400, 576, 729]
>>> [h(10**e) for e in range(9)]
[1, 10, 37, 82, 170, 257, 362, 530, 677]

######################
>>> [h(2**e -1) for e in range(40, 50)]
[1522, 1601, 1682, 1765, 1850, 1937, 2026, 2117, 2210, 2402]
>>> [f(2**e -1) for e in range(40, 50)]
[1537.4496445381437, 1615.2830327929414, 1695.0382331033882, 1776.7152454694951, 1860.3140698912691, 1945.834706368712, 2033.2771549018266, 2122.6414154906133, 2213.9274881350716, 2307.1353728352033]
>>> f(2**48 -1) > h(2**48 -1)
True
>>> f(2**49 -1) < h(2**49 -1) # ==>> [@[n <- [2**48..]] -> [f(n) < h(n)]]
True
>>> f(2**48) < h(2**48)
True

    ==>> [@[n <- [2**48..]] -> [f(n) < h(n)]]
    ==>> [@[n <- [2**48..]] -> [2*ln(n)**2 < 1+floor_log2(n)**2]]


######################
>>> all(f(2**e -1) < -1+h(2**e -1) for e in range(49, 1000))
True
>>> all(f(2**e -1) >= -1+h(2**e -1) for e in range(1, 49))
True
>>> all(f(2**e -1) > -1+h(2**e -1) for e in range(2, 49))
True
>>> all(f(2**e -1) > h(2**e -1) for e in range(2, 49))
True

    ==>> [@[n <- [2**48..]] -> [2*ln(n)**2 < floor_log2(n)**2]]

######################
]]]


>>> from seed.iters.apply_may_args4islice_ import list_islice_, show_islice_, stable_show_islice_, stable_list_islice_

[[[
py_adhoc_call   seed.math.primality_proving__plain   ,4:iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ =5
===
py_adhoc_call   seed.math.primality_proving__plain   ,4:iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ =5
>>> show_islice_(4, iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(5))
(5, 1, 4, 3)
(6, 5, 3, 3)
(7, 3, 5, 5)
(8, 3, 6, 5)

===
]]]

[[[
py_adhoc_call   seed.math.primality_proving__plain   ,50:iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
===
>>> show_islice_(50, iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_())
(2, 1, 1, 2)
(3, 1, 2, 2)
(4, 3, 2, 2)
(5, 1, 4, 3)
(6, 5, 3, 3)
(7, 3, 5, 5)
(8, 3, 6, 5)
(9, 1, 8, 3)
(10, 3, 8, 7)
(11, 9, 7, 5)
(12, 13, 8, 3)
(13, 15, 9, 13)
(14, 3, 12, 11)
(15, 9, 11, 5)
(16, 5, 13, 3)
(17, 1, 16, 3)
(18, 5, 15, 3)
(19, 33, 13, 5)
(20, 3, 18, 5)
(21, 9, 17, 19)
(22, 21, 17, 5)
(23, 7, 20, 3)
(24, 13, 20, 3)
(25, 11, 21, 3)
(26, 69, 19, 5)
(27, 25, 22, 3)
(28, 5, 25, 3)
(29, 7, 26, 3)
(30, 45, 24, 11)
(31, 15, 27, 11)
(32, 3, 30, 5)
(33, 59, 27, 3)
(34, 23, 29, 3)
(35, 45, 29, 7)
(36, 49, 30, 3)
(37, 9, 33, 7)
(38, 3, 36, 11)
(39, 73, 32, 3)
(40, 99, 33, 13)
(41, 15, 37, 7)
(42, 5, 39, 3)
(43, 3, 41, 5)
(44, 63, 38, 5)
(45, 27, 40, 5)
(46, 9, 42, 5)
(47, 9, 43, 5)
(48, 15, 44, 7)
(49, 27, 44, 5)
(50, 63, 44, 11)
(51, 19, 46, 3)

===vs:bug:
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
===
]]]
[[[
py_adhoc_call   seed.math.primality_proving__plain   ,5:iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ =10
===
>>> show_islice_(5, iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(10))
(10, 1, 9, 2, 3)
(10, 3, 8, 0, 7)
(11, 1, 10, 2, 5)
(11, 3, 9, 2, 29)
(11, 5, 8, 2, 3)

===
py_adhoc_call   seed.math.primality_proving__plain   ,5:iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ =10 =3
===
>>> show_islice_(5, iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(10,3))
(10, 3, 8, 0, 7)
(11, 1, 10, 2, 5)
(11, 3, 9, 2, 29)
(11, 5, 8, 2, 3)
(11, 7, 8, 2, 11)

===
py_adhoc_call   seed.math.primality_proving__plain   ,5:iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ =10 =5
===
>>> show_islice_(5, iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(10,5))
(10, 5, 7, 0, 3)
(11, 1, 10, 2, 5)
(11, 3, 9, 2, 29)
(11, 5, 8, 2, 3)
(11, 7, 8, 2, 11)

===
]]]
[[[
py_adhoc_call   seed.math.primality_proving__plain   ,50:iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
===
>>> show_islice_(50, iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_())
(2, 1, 1, 0, 2)
(3, 1, 2, 0, 2)
(4, 1, 3, 2, 3)
(4, 3, 2, 0, 2)
(5, 1, 4, 0, 3)
(6, 1, 5, 2, 3)
(6, 3, 4, 2, 7)
(6, 5, 3, 0, 3)
(7, 1, 6, 2, 5)
(7, 3, 5, 0, 5)
(8, 1, 7, 2, 3)
(8, 3, 6, 0, 5)
(9, 1, 8, 0, 3)
(10, 1, 9, 2, 3)
(10, 3, 8, 0, 7)
(11, 1, 10, 2, 5)
(11, 3, 9, 2, 29)
(11, 5, 8, 2, 3)
(11, 7, 8, 2, 11)
(11, 9, 7, 0, 5)
(12, 1, 11, 2, 3)
(12, 3, 10, 2, 7)
(12, 5, 9, 2, 13)
(12, 7, 9, 2, 3)
(12, 9, 8, 2, 5)
(12, 11, 8, 2, 3)
(12, 13, 8, 0, 3)
(13, 1, 12, 2, 17)
(13, 3, 11, 2, 5)
(13, 5, 10, 2, 3)
(13, 7, 10, 1, 2)
(13, 9, 9, 2, 11)
(13, 11, 9, 1, 2)
(13, 13, 9, 2, 3)
(13, 15, 9, 0, 13)
(14, 1, 13, 2, 3)
(14, 3, 12, 0, 11)
(15, 1, 14, 2, 5)
(15, 3, 13, 2, 7)
(15, 5, 12, 2, 3)
(15, 7, 12, 1, 2)
(15, 9, 11, 0, 5)
(16, 1, 15, 2, 3)
(16, 3, 14, 2, 13)
(16, 5, 13, 0, 3)
(17, 1, 16, 0, 3)
(18, 1, 17, 2, 3)
(18, 3, 16, 2, 7)
(18, 5, 15, 0, 3)
(19, 1, 18, 2, 5)

===
]]]


[[[
iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
===create file:
py_adhoc_call   seed.math.primality_proving__plain   ,5:iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ :/sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
view /sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
===continue append to file
py_adhoc_call   seed.math.primality_proving__plain   ,3:iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ :/sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
view /sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
===
py_adhoc_call   seed.math.primality_proving__plain   @validate_output5iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ :/sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt +to_validate_continuity +to_validate_certificate
]]]
[[[
iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
===create file:
py_adhoc_call   seed.math.primality_proving__plain   ,5:iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ :/sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
view /sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
===continue append to file
py_adhoc_call   seed.math.primality_proving__plain   ,3:iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ :/sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
view /sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
===
validate_output5iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
py_adhoc_call   seed.math.primality_proving__plain   @validate_output5iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ :/sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt +to_validate_continuity +to_validate_certificate
===
]]]

[[[
view ../../python3_src/seed/math/_output_/seed.math.primality_proving..continue4iter_odd_primes__one_prime_per_bit_length_.end-719.txt
!cp ../../python3_src/seed/math/_output_/seed.math.primality_proving..continue4iter_odd_primes__one_prime_per_bit_length_.end-719.txt  ../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.reformat5-719.txt
e ../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.reformat5-719.txt
    reformat to: (num_bits4N, odd4Nmm, ez4Nmm, case, certificate)
    #补偿: ((((((
%s/<</, /
%s/\^1//
%s/, \(\d*\))/, 2, \1)
%s/, -\(\d*\))/, 1, \1)
%s/, \[\(\d*\)\D.*)/, 0, \1)
    #补偿: \]

original last line:86222row: (718, 37, 712, [6, 2])
now:(718, 37, 712, 0, 6)
view ../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.reformat5-719.txt
===
py_adhoc_call   seed.math.primality_proving__plain   @validate_output5iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ :../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.reformat5-719.txt +to_validate_continuity +to_validate_certificate
    ok!
===
!du -h ../../python3_src/seed/math/_output_/seed.math.primality_proving..continue4iter_odd_primes__one_prime_per_bit_length_.end-719.txt
    1.7MB
!du -h ../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.reformat5-719.txt
    1.8MB
===
===
===
===
py_adhoc_call   seed.math.primality_proving__plain   ,86222:iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ :/sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
===
===
view /sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
86222row:(718, 37, 712, 0, 3)
86252row:(719, 59, 713, 2, 11)

diff /sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt   ../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.reformat5-719.txt >  /sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out...diff-719.txt
view  /sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out...diff-719.txt
    xxx发现 bug: max1_len_rootss @ view ../../python3_src/seed/math/primality_proving-202310.py::_iter_detect_primality__Nmm_()
        该模块max1_len_rootss 角色类同于 本模块::Tester4composite_via_even_Nmm::max1_k
        xxx已订正！
        又发现不是bug，又改回去
        几百比特的N，floor_log2_N**2 几万 =>:
            * 只使用 floor_log2_N个素数 用作 试除
            * 2**max1_len_rootss依然上万 这可能是 导致该模块实现 费时的原因

!du -h /sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
    1.8MB
    curr:last_line:86252row:(719, 59, 713, 2, 11)
===
!mv /sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt ../../python3_src/seed/math/_output_/
view  ../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
===
py_adhoc_call   seed.math.primality_proving__plain   ,22:iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ :../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
===
===
!rm ../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
!rm ../../python3_src/seed/math/_output_/seed.math.primality_proving..continue4iter_odd_primes__one_prime_per_bit_length_.end-719.txt
!rm ../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.reformat5-719.txt
!ls ../../python3_src/seed/math/_output_/
!du -h ../../python3_src/seed/math/_output_/
    104KB
===
]]]
[[[
py_adhoc_call   seed.math.primality_proving__plain   ,2000:iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ :../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
===
view ../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
    (num_bits4N, odd4Nmm, ez4Nmm, gz)
(2, 1, 1, 2)
(3, 1, 2, 2)
(4, 3, 2, 2)
(5, 1, 4, 3)
(6, 5, 3, 3)
(7, 3, 5, 5)
... ...
... ...
(2095, 379, 2086, 3)
(2096, 733, 2086, 3)
(2097, 1593, 2086, 5)
(2098, 3127, 2086, 3)
(2099, 2657, 2087, 3)
(2100, 589, 2090, 3)
(2101, 1945, 2090, 3)
(2102, 775, 2092, 3)
===
extract seq of odd4Nmm
    to search in oeis
extract_odd4Nmm_seq_from_output5iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
iter_extract_odd4Nmm_seq_from_output5iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
===
py_adhoc_call   seed.math.primality_proving__plain   ,iter_extract_odd4Nmm_seq_from_output5iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ :../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
===
py_adhoc_call   seed.math.primality_proving__plain   @extract_odd4Nmm_seq_from_output5iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ :../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
(1, 1, 3, 1, 5, 3, 3, 1, 3, 9, 13, 15, 3, 9, 5, 1, 5, 33, 3, 9, 21, 7, 13, 11, 69, 25, 5, 7, 45, 15, 3, 59, 23, 45, 49, 9, 3, 73, 99, 15, 5, 3, 63, 27, 9, 9, 15, 27, 63, 19, 15, 7, 23, 7, 17, 25, 5, 51, 49, 27, 29, 87, 27, 31, 45, 9, 3, 9, 75, 9, 33, 31, 23, 221, 39, 39, 5, 39, 29, 67, 15, 25, 145, 9, 13, 249, 5, 51, 37, 53, 65, 87, 61, 7, 57, 27, 29, 33, 43, 85
    , ... ..., 2595, 1633, 1565, 1191, 3067, 471, 2403, 379, 733, 1593, 3127, 2657, 589, 1945, 775)
    #odd4Nmm__seq for num_bits4N <- [2..=2102]
===
]]]


[[[
after new_version_test6Tester4composite_via_even_Nmm:
===
py_adhoc_call   seed.math.primality_proving__plain   ,7:iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
py_adhoc_call   seed.math.primality_proving__plain   ,500:iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_ :/sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
===
diff /sdcard/0my_files/tmp/out4py/seed.math.primality_proving__plain..iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt  ../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_.out.txt
===
]]]


[[[
iter_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_
===
py_adhoc_call   seed.math.primality_proving__plain   ,7:iter_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_ =2 =2
    ok
>>> show_islice_(7, iter_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(2,2))
(2, 1, 1, 2)
(3, 1, 2, 2)
(4, 3, 2, 2)
(5, 1, 4, 3)
(6, 5, 3, 3)
(7, 3, 5, 5)
(8, 3, 6, 5)

===
py_adhoc_call   seed.math.primality_proving__plain   ,7:iter_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_ =3 =3
>>> show_islice_(7, iter_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(3,3))
(2, 2, 1, 2)
(3, 2, 2, 2)
(4, 4, 2, 2)
(5, 2, 4, 2)
(6, 2, 5, 2)
(7, 2, 6, 3)
(8, 4, 6, 3)

===
py_adhoc_call   seed.math.primality_proving__plain   ,7:iter_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_ =10 '=[2,5]'
>>> show_islice_(7, iter_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(10, [2,5]))
(2, 1, 1, (2, 2))
(3, 1, 2, (2, 2))
(4, 3, 3, (7, 2))
(5, 7, 4, (3, 2))
(6, 7, 5, (3, 3))
(7, 21, 5, (11, 2))
(8, 3, 7, (7, 2))

===
===
py_adhoc_call   seed.math.primality_proving__plain   ,7:iter_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_ =10 '=None'
    ok@[may_j2prime_factor4radix := None]
>>> show_islice_(7, iter_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(10,None))
(2, 1, 1, (2, 2))
(3, 1, 2, (2, 2))
(4, 3, 3, (7, 2))
(5, 7, 4, (3, 2))
(6, 7, 5, (3, 3))
(7, 21, 5, (11, 2))
(8, 3, 7, (7, 2))

===
===
iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_
validate_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_
iter_extract_significand4Nmm_seq_from_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_
extract_significand4Nmm_seq_from_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_
===
py_adhoc_call   seed.math.primality_proving__plain   ,100:iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_ =10 '=[2,5]'  :../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_.10.out.txt  +allow_create -output_composite
run twice:
... ...
(195, 235, 192, (3, 2))
(196, 39, 194, (11, 3))
(197, 429, 194, (7, 2))
(198, 103, 195, (3, 3))
(199, 72, 197, (11, 3))
(200, 117, 197, (7, 2))
(201, 24, 199, (7, 2))
===
py_adhoc_call   seed.math.primality_proving__plain   @validate_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_ =10 '=[2,5]'  :../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_.10.out.txt  +to_validate_continuity +to_validate_certificate -had_output_composite
    ok
py_adhoc_call   seed.math.primality_proving__plain   @validate_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_ =6 '=[2,3]'  :../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_.10.out.txt  +to_validate_continuity +to_validate_certificate -had_output_composite
    ValidateFail
===
py_adhoc_call   seed.math.primality_proving__plain   @extract_significand4Nmm_seq_from_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_ =10 '=[2,5]'  :../../python3_src/seed/math/_output_/seed.math.primality_proving__plain..iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_.10.out.txt  -had_output_composite
(1, 1, 3, 7, 7, 21, 3, 6, 6, 3, 22, 19, 4, 42, 6, 69, 13, 37, 15, 6, 96, 9, 28, 96, 61, 6, 9, 3, 51, 33, 63, 57, 112, 55, 49, 3, 16, 6, 12, 42, 24, 36, 72, 21, 6, 21, 24, 33, 61, 21, 85, 31, 49, 13, 93, 18, 9, 151, 16, 123, 19, 9, 42, 111, 6, 31, 3, 36, 16, 196, 115, 19, 99, 15, 141, 147, 42, 9, 16, 42, 3, 82, 88, 63, 16, 19, 264, 112, 78, 123, 226, 43, 63, 55, 16, 13, 94, 27, 72, 82, 321, 111, 22, 123, 84, 13, 88, 48, 124, 42, 115, 6, 55, 192, 39, 205, 34, 46, 45, 97, 37, 64, 85, 289, 234, 13, 79, 135, 48, 97, 238, 73, 78, 165, 115, 7, 94, 564, 39, 201, 234, 7, 502, 15, 511, 33, 3, 88, 109, 36, 16, 162, 51, 52, 205, 228, 279, 7, 231, 156, 229, 114, 213, 13, 115, 226, 171, 226, 19, 121, 208, 145, 361, 664, 244, 114, 69, 151, 16, 235, 49, 172, 355, 126, 42, 436, 258, 277, 82, 189, 16, 82, 15, 235, 39, 429, 103, 72, 117, 24)
===
===
===
]]]


#]]]'''
__all__ = r'''
Result
    Certificate
        CompositeCertificate
            CompositeCertificate__witness4composite
            CompositeCertificate__nontrivial_factor
        PrimeCertificate
            PrimeCertificate__complete_factorization
            PrimeCertificate__sqrt_case
            PrimeCertificate__TWO

Fail
    ValidateFail
    ERH__fail
    Fail__unknown_fine_upperbound4primitive_root
Error
    AlreadyFinish__partial_pseudo_primitive_roots
    ValueError__N_divs_g
    ValueError__not_complete_factorization
    ValueError__not_sqrt_case


validate_unity_primitive_root_certificate__complete_factorization4order_
validate_prime_certificate__Nmm__complete_factorization_
validate_prime_certificate__Nmm__partial_factorization__gt_sqrtN_

return_version____primality_test__Nmm__plain__sqrt_case_
    raise_version____primality_test__Nmm__plain__sqrt_case_
        Tester4composite_via_even_Nmm
        Tester4prime_via_Nmm__complete_factorization
        Tester4prime_via_Nmm__sqrt_case






iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
    iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
        iter_N_exss__zpow_dominance_Nmm_
            iter_N_exs__zpow_dominance_Nmm__fixed_bit_length_


iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
    iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
    iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
        validate_output5iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
        validate_output5iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_

extract_odd4Nmm_seq_from_output5iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
    iter_extract_odd4Nmm_seq_from_output5iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_







Error
    ValueError__miss_some_prime_factors
    ValueError__contain_useless_prime_factors

RadixPowDominancePlusplusOddNumberRelated
    iter_odd_N_exss__radix_pow_dominance_Nmm_
    iter_odd_N_exs__radix_pow_dominance_Nmm__fixed_num_digits4N__

    RadixPowDominancePlusplusOddPrimeRelated
        iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_
            iter_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_
            iter_until_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_
        iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_
            validate_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_
        iter_extract_significand4Nmm_seq_from_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_
            extract_significand4Nmm_seq_from_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_

'''.split()#'''
__all__

from itertools import count as count_
from itertools import islice, pairwise
from os import SEEK_SET, SEEK_END, SEEK_CUR

from seed.mapping_tools.dict_op import inv__k2v_to_v2ks
from seed.iters.apply_commutative_operations_except_one import iter_apply_commutative_operations_except_one_
#def iter_apply_commutative_operations_except_one_(apply_, commutative_operation_keys, x0, /):
from seed.math.II import II
from seed.math.gcd import gcd
from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
#def semi_factor_pint_via_trial_division(candidate_factors, pint, /):
 #   'Iter factor{>=2} -> pint -> (factor2exp/{factor:exp{>=1}}, unfactored_part{>=1})'
from seed.math.factor_pint_by_trial_division_ import factor_pint_by_trial_division_, factor_pint_by_trial_division_ex_

from seed.math.floor_ceil import floor_log2, floor_sqrt, floor_log_
from seed.tiny_.dict__add_fmap_filter import dict_add__new
from seed.math.prime_gens import prime_gen
from seed.tiny_.check import check_int_ge, check_int_ge_lt# check_uint_lt, check_int_ge_le
from seed.math.divs import is_odd
from seed.tiny import check_type_is
from seed.tiny import check_type_le
from seed.io.continue_io import LineContinueIO, IValidatableLineContinueIO
from seed.tiny import print_err, mk_fprint

#from seed.tiny import null_tuple
from seed.tiny import mk_tuple
from seed.helper.repr_input import repr_helper




class Result(BaseException):pass
class Certificate(Result):
    if 0:
        @property
        def N(sf, /):
            raise NotImplementedError
    def validate(sf, /):
        raise NotImplementedError
class CompositeCertificate(Certificate):pass
class PrimeCertificate(Certificate):pass

class CompositeCertificate__witness4composite(CompositeCertificate):
    def __init__(sf, N, witness4composite, /, *, validate=True):
        #assert -N < witness4composite < N
        assert N >= 4, (N, witness4composite)
        super().__init__(N, witness4composite)
        sf.N = N
        sf.witness4composite = witness4composite
        if validate:
            sf.validate()
    def validate(sf, /):
        if pow(sf.witness4composite, sf.N-1, sf.N) == 1: raise ValidateFail(sf.N, sf.witness4composite)
            #otherwise use CompositeCertificate__nontrivial_factor

class CompositeCertificate__nontrivial_factor(CompositeCertificate):
    def __init__(sf, N, nontrivial_factor, /, *, validate=True):
        super().__init__(N, nontrivial_factor)
        sf.N = N
        sf.nontrivial_factor = nontrivial_factor
        if validate:
            sf.validate()
    def validate(sf, /):
        if not 2 <= sf.nontrivial_factor < sf.N and sf.N %sf.nontrivial_factor == 0: raise ValidateFail(sf.N, sf.nontrivial_factor)


class PrimeCertificate__TWO(PrimeCertificate):
    N = 2
    def validate(sf, /):
        pass
class PrimeCertificate__complete_factorization(PrimeCertificate):
    def __init__(sf, N, j2prime_factor4Nmm, j2exp4Nmm, j2g, /, *, validate=True):
        super().__init__(N, j2prime_factor4Nmm, j2exp4Nmm, j2g)
        sf.N = N
        sf.j2prime_factor4Nmm = j2prime_factor4Nmm
        sf.j2exp4Nmm = j2exp4Nmm
        sf.j2g = j2g
        if validate:
            sf.validate()
    def validate(sf, /):
        validate_prime_certificate__Nmm__complete_factorization_(sf.N, sf.j2prime_factor4Nmm, sf.j2exp4Nmm, sf.j2g)


class PrimeCertificate__sqrt_case(PrimeCertificate):
    def __init__(sf, N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, j2g, /, *, validate=True):
        super().__init__(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, j2g)
        sf.N = N
        sf.j2prime_factor4ft4Nmm = j2prime_factor4ft4Nmm
        sf.j2exp4ft4Nmm = j2exp4ft4Nmm
        sf.j2g = j2g
        if validate:
            sf.validate()
    def validate(sf, /):
        validate_prime_certificate__Nmm__partial_factorization__gt_sqrtN_(sf.N, sf.j2prime_factor4ft4Nmm, sf.j2exp4ft4Nmm, sf.j2g)


class Fail(Exception):pass
class ValidateFail(Fail):pass
class ERH__fail(Fail):pass
class Fail__unknown_fine_upperbound4primitive_root(Fail):pass

class Error(Exception):pass
class AlreadyFinish__partial_pseudo_primitive_roots(Error):pass
class ValueError__N_divs_g(Error):pass
class ValueError__not_complete_factorization(Error):pass
class ValueError__not_sqrt_case(Error):pass


class ValueError__miss_some_prime_factors(Error):pass
class ValueError__contain_useless_prime_factors(Error):pass

#def validate_discrete_logarithm_certificate__complete_factorization4order_(M, g, order4gM, j2prime_factor4order, j2exp4order, /):
def validate_unity_primitive_root_certificate__complete_factorization4order_(M, g, order4gM, j2prime_factor4order, j2exp4order, /):
    # [unity==1]
    assert len(j2prime_factor4order) == len(j2exp4order)
    assert all(p >= 2 for p in j2prime_factor4order)
    assert all(e >= 1 for e in j2exp4order)
    assert order4gM == II(map(int.__pow__, j2prime_factor4order, j2exp4order))

    if not pow(g, order4gM, M) == 1: raise ValidateFail
    for p in j2prime_factor4order:
        if pow(g, (order4gM//p), M) == 1: raise ValidateFail
    return

def _j2g__to__g2js(j2g, /):
    g2js = inv__k2v_to_v2ks(j2g, True, set_vs_list=True)
    return g2js
def _index(seq, js, /):
    return [seq[j] for j in js]

def validate_prime_certificate__Nmm__complete_factorization_(N, j2prime_factor4Nmm, j2exp4Nmm, j2g, /):
    # not using gcd
    assert len(j2prime_factor4Nmm) == len(j2exp4Nmm) == len(j2g)
    assert all(p >= 2 for p in j2prime_factor4Nmm)
    assert all(e >= 1 for e in j2exp4Nmm)
    Nmm = N-1
    assert Nmm == II(map(int.__pow__, j2prime_factor4Nmm, j2exp4Nmm))

    _validate_prime_certificate__Nmm__impl_(N, j2prime_factor4Nmm, j2exp4Nmm, j2g, Nmm, using_gcd=False)
    return


def validate_prime_certificate__Nmm__partial_factorization__gt_sqrtN_(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, j2g, /):
    # using gcd
    # not-require: [gcd(ft4Nmm, Nmm///ft4Nmm) == 1]
    assert len(j2prime_factor4ft4Nmm) == len(j2exp4ft4Nmm) == len(j2g)
    assert all(p >= 2 for p in j2prime_factor4ft4Nmm)
    assert all(e >= 1 for e in j2exp4ft4Nmm)
    Nmm = N-1
    ft4Nmm = II(map(int.__pow__, j2prime_factor4ft4Nmm, j2exp4ft4Nmm))
    assert Nmm %ft4Nmm == 0
    #unfactored = Nmm //ft4Nmm
    if not N < (ft4Nmm+1)**2: raise ValidateFail

    _validate_prime_certificate__Nmm__impl_(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, j2g, Nmm, using_gcd=True)
    return

def _iter_pow_II__except_one(N, Nmm, Nmm__IIps, ps, g, /):
    def apply_(p, gg, /):
        if gg == Nmm:
            return Nmm if p&1 else 1
        gg = pow(gg, p, N)
        return gg
    g_IIps = pow(g, Nmm__IIps, N)
    it = iter_apply_commutative_operations_except_one_(apply_, ps, g_IIps)
    return it
def _validate_prime_certificate__Nmm__impl_(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, j2g, Nmm, /, *, using_gcd):
    g2js = _j2g__to__g2js(j2g)


    for g, js in sorted(g2js.items()):
        #if not pow(g, Nmm, N) == 1: raise ValidateFail
            # move below:see:known__g_is_root
        ps = _index(j2prime_factor4ft4Nmm, js)
        IIps = II(ps)
        Nmm__IIps = Nmm//IIps

        it = _iter_pow_II__except_one(N, Nmm, Nmm__IIps, ps, g)
        known__g_is_root = False
        for j, p, gg in zip(js, ps, it):
            #gg = pow(g, (Nmm//p), N)
            # [gg == g**(Nmm///p) %N]
            if using_gcd:
                if not gcd(gg-1, N) == 1: raise ValidateFail
                # [gcd(gg-1, N) == 1]
            else:
                if gg == 1: raise ValidateFail
                # [gg =!= 1]
            if not known__g_is_root:
                if not pow(gg, p, N) == 1: raise ValidateFail
                # [gg**p %N == 1]
                # !! [gg == g**(Nmm///p) %N]
                # [g**Nmm %N == 1]
                known__g_is_root = True
                # [known__g_is_root is True]
            # [known__g_is_root is True]
            # [g**Nmm %N == 1]
            # [gg =!= 1]
                # using_gcd => [gcd(gg-1, N) == 1]
            # [is_a_partial_pseudo_primitive_root_mod_(N, Nmm, p; g, using_gcd=using_gcd)]
    return


def _4min_witness4composite__may_be_composite(*, begin=9, end=2**16):
    '-> may (N, g, gg0, gg_ls, may_k4gg0) # [[2 <= g < min_prime_factor_of_(N)][not$ is_prime_(g)][[may_k4gg0 is None] <-> [g**(N-1) %N =!= 1]][1 =!= gg0 == g**odd4Nmm %N][[not% may_k4gg0 is None] -> [[k4gg0 > 0][gg0**(2**k4gg0) %N == 1][not$ gg0**(2**(k4gg0-1)) %N <- {1,N-1}]]]] #{enhanced:=False}'
    #   [:min_witness4composite__may_be_composite:primality_test_of_Miller_Rabin]:goto
    from seed.math.prime_gens import is_strong_pseudoprime__basis_, is_prime__using_A014233_, is_prime__le_pow2_81_, is_prime__tribool_, Case4is_prime__tribool_
    enhanced = False
    begin = max(9, begin)
    begin |= 1
    assert begin %2 == 1
    # [is_odd_(begin)]
    for N in range(begin, end, 2):
        # [is_odd_(N)]
        if is_prime__le_pow2_81_(N):
            continue
        # [not$ is_prime_(N)]
        Nmm = N -1
        (ez4Nmm, odd4Nmm) = factor_pint_out_power_of_base_(2, Nmm)
        tc = Tester4composite_via_even_Nmm(N, enhanced=enhanced)
        try:
            for g in range(2, N):
                if N %g == 0:
                    #[g is min_witness4composite]
                    assert is_prime__le_pow2_81_(g)
                    # [is_prime_(g)]
                    break
                if not gcd(g, N) == 1:
                    raise 000
                # [gcd(g, N) == 1]
                (gg0, k4gg0) = tc.test_(g)
                # [enhanced := False] ==>> [fixed: not skip Nmm:below『pow(gg0, 1<<(k4gg0-1), N) == N-1』]
                assert gg0 == pow(g, odd4Nmm, N)
                assert (k4gg0 == 0) if gg0 == 1 else (pow(gg0, 1<<(k4gg0-1), N) == N-1)
            else:#for-else
                raise 000
            # [g is min_witness4composite]
            # [is_prime_(g)]
            pass
        except (CompositeCertificate__nontrivial_factor, CompositeCertificate__witness4composite):
            #[g is min_witness4composite]
            # [gcd(g, N) == 1]
            # [g < min_prime_factor_of_(N)]
            ######################
            #(gg0, gg_ls, may_k4gg0) = _calc__gg0__gg_ls__may_k4gg0__5primality_test_of_Miller_Rabin_(N, Nmm, ez4Nmm, odd4Nmm, g)
            (gg0, gg_ls, may_k4gg0) = _validate_witness4composite__5primality_test_of_Miller_Rabin(N, Nmm, ez4Nmm, odd4Nmm, g, enhanced=enhanced)

            if is_prime__le_pow2_81_(g):
                # [min_witness4composite is prime]
                continue
            else:
                # [min_witness4composite is composite]
                # [(N,g) is counterexample of [min_witness4composite ALWAYS_BE prime]]
                # [gcd(g, N) == 1]
                # [g < min_prime_factor_of_(N)]
                return (N, g, gg0, gg_ls, may_k4gg0)
        else:#try-else
            # [g is min_witness4composite]
            # [is_prime_(g)]
            pass
    return None
class _Calc__gg0__gg_ls__may_k4gg0__5primality_test_of_Miller_Rabin:
    def __init__(sf, N, Nmm, ez4Nmm, odd4Nmm, g0, /):
        sf.args = (N, Nmm, ez4Nmm, odd4Nmm, g0)
        sf.check_precondition()
        sf._may_output = None
    def check_precondition(sf, /):
        (N, Nmm, ez4Nmm, odd4Nmm, g0) = sf.args
        cls = type(sf)
        cls.cls__check_precondition(N, Nmm, ez4Nmm, odd4Nmm, g0)
    def check_postcondition(sf, gg0, gg_ls, may_k4gg0, /):
        (N, Nmm, ez4Nmm, odd4Nmm, g0) = sf.args
        cls = type(sf)
        cls.cls__check_postcondition(N, Nmm, ez4Nmm, odd4Nmm, g0, gg0, gg_ls, may_k4gg0)
    def calc__gg0__gg_ls__may_k4gg0__5primality_test_of_Miller_Rabin_(sf, /, *, validate):
        '-> (gg0, gg_ls, may_k4gg0) #see:postcondition4gg0'
        if sf._may_output is None:
            (N, Nmm, ez4Nmm, odd4Nmm, g0) = sf.args
            cls = type(sf)
            (gg0, gg_ls, may_k4gg0) = cls.cls__calc__gg0__gg_ls__may_k4gg0__5primality_test_of_Miller_Rabin_(N, Nmm, ez4Nmm, odd4Nmm, g0)
            validated = False
            sf._may_output = (gg0, gg_ls, may_k4gg0, validated)
        (gg0, gg_ls, may_k4gg0, validated) = sf._may_output
        if validate and not validated:
            sf.check_postcondition(g0, gg0, gg_ls, may_k4gg0)
            validated = True
            sf._may_output = (gg0, gg_ls, may_k4gg0, validated)
        return (gg0, gg_ls, may_k4gg0)
    @classmethod
    def cls__check_postcondition4gg0_and_may_k4gg0(cls, N, Nmm, ez4Nmm, odd4Nmm, g0, gg0, may_k4gg0, /):
        ######################postcondition:
        if not may_k4gg0 is None:
            k4gg0 = may_k4gg0
        assert gg0 == pow(g0, odd4Nmm, N)
        assert (may_k4gg0 is None) is (not pow(gg0, 1<<ez4Nmm, N) == 1)
        assert (may_k4gg0 is None) or (0 <= k4gg0 <= ez4Nmm and (k4gg0==0) is (gg0==1))
        assert (may_k4gg0 is None) or (pow(gg0, 1<<k4gg0, N) == 1 and (k4gg0==0 or not pow(gg0, 1<<(k4gg0-1), N) == 1))
    @classmethod
    def cls__check_postcondition4gg_ls(cls, N, Nmm, ez4Nmm, odd4Nmm, g0, gg0, gg_ls, may_k4gg0, /):
        ######################postcondition:
        assert 1 <= len(gg_ls) <= 1+ez4Nmm
        assert gg_ls[0] == gg0
        assert gg_ls[-1] == 1 or len(gg_ls) == 1+ez4Nmm
        assert (gg_ls[-1] == 1) is (not may_k4gg0 is None)
        assert all(gg_gg == pow(gg, 2, N) for gg, gg_gg in pairwise(gg_ls))
    @classmethod
    def cls__check_postcondition(cls, N, Nmm, ez4Nmm, odd4Nmm, g0, gg0, gg_ls, may_k4gg0, /):
        cls.cls__check_postcondition4gg0_and_may_k4gg0(N, Nmm, ez4Nmm, odd4Nmm, g0, gg0, may_k4gg0)
        cls.cls__check_postcondition4gg_ls(N, Nmm, ez4Nmm, odd4Nmm, g0, gg0, gg_ls, may_k4gg0)
        ######################
        ##postcondition4gg0:
        # [1 <= len(gg_ls) <= 1+ez4Nmm]
        # [gg_ls[0] == gg0]
        # [[gg_ls[-1] =!= 1] -> [len(gg_ls) == 1+ez4Nmm]]
        # [[gg_ls[-1] =!= 1] <-> [may_k4gg0 is None]]
        # [@[i :<- [1..<len(gg_ls)]] -> [gg_ls[i] == gg_ls[i-1]**2 %N]]
        #
        # [gg0 == g0**odd4Nmm %N)]
        # [[may_k4gg0 is None] <-> [gg0**(2**ez4Nmm) %N =!= 1]]
        # [[not$ may_k4gg0 is None] -> [[0 <= k4gg0 <= ez4Nmm][[k4gg0==0] <-> [gg0==1]][gg0**(2**k4gg0) %N == 1][[k4gg0 =!= 0] -> [gg0**(2**(k4gg0-1)) %N =!= 1]]]]
        ######################
    @classmethod
    def cls__check_precondition(cls, N, Nmm, ez4Nmm, odd4Nmm, g0, /):
        ######################precondition:
        assert odd4Nmm >= 1
        assert odd4Nmm %2 == 1
            # [is_odd_(odd4Nmm)]
        assert ez4Nmm >= 1
            # [is_odd_(N)]
        assert N-1 == Nmm == (odd4Nmm<<ez4Nmm)
    @classmethod
    def cls__calc__gg0__gg_ls__may_k4gg0__5primality_test_of_Miller_Rabin_(cls, N, Nmm, ez4Nmm, odd4Nmm, g0, /):
        '-> (gg0, gg_ls, may_k4gg0) #see:postcondition4gg0'
        gg0 = pow(g0, odd4Nmm, N)
        gg_ls = [gg0]
        if gg0 == 1:
            # [gg0 == 1]
            k4gg0 = 0
            may_k4gg0 = k4gg0
            gg0, gg_ls, may_k4gg0
        else:
            # [gg0 =!= 1]
            gg = gg0
            # [gg =!= 1]
            for k4gg0 in range(ez4Nmm):
                # [gg =!= 1]
                assert not gg == Nmm
                gg = pow(gg, 2, N)
                gg_ls.append(gg)
                # [gg may be 1]
                if gg == 1:
                    k4gg0 += 1
                    may_k4gg0 = k4gg0
                    break
            else:
                may_k4gg0 = None
            gg0, gg_ls, may_k4gg0
        gg0, gg_ls, may_k4gg0
        gg_ls
        return (gg0, gg_ls, may_k4gg0)
def _calc__gg0__gg_ls__may_k4gg0__5primality_test_of_Miller_Rabin_(N, Nmm, ez4Nmm, odd4Nmm, g0, /):
    '-> (gg0, gg_ls, may_k4gg0) #see:postcondition4gg0'
    sf = _Calc__gg0__gg_ls__may_k4gg0__5primality_test_of_Miller_Rabin(N, Nmm, ez4Nmm, odd4Nmm, g0)
        #check_precondition
    (gg0, gg_ls, may_k4gg0) = sf.calc__gg0__gg_ls__may_k4gg0__5primality_test_of_Miller_Rabin_(validate=True)
        #check_postcondition
    return (gg0, gg_ls, may_k4gg0)
    ######################
def _validate_witness4composite__5primality_test_of_Miller_Rabin(N, Nmm, ez4Nmm, odd4Nmm, g0, /, *, enhanced):
    if enhanced: raise NotImplementedError
    #no (gg0, k4gg0): assert (k4gg0 == 0) if gg0 == 1 else ((pow(g0, odd4Nmm<<k4gg0, N) == 1) and (not pow(g0, odd4Nmm<<(k4gg0-1), N) == N-1))
    (gg0, gg_ls, may_k4gg0) = _calc__gg0__gg_ls__may_k4gg0__5primality_test_of_Miller_Rabin_(N, Nmm, ez4Nmm, odd4Nmm, g0)
    if not may_k4gg0 is None:
        k4gg0 = may_k4gg0

    if not enhanced:
        #validate: [g0 is min_witness4composite]
        # [enhanced := False] ==>> [fixed: skip Nmm:below『not pow(gg0, 1<<(k4gg0-1), N) == Nmm』]
        assert not gg0 == 1
        assert may_k4gg0 is None or k4gg0 >= 1
            #==>> assert not k4gg0 == 0
        assert (not pow(gg0, 1<<ez4Nmm, N) == 1) if may_k4gg0 is None else (pow(gg0, 1<<k4gg0, N) == 1 and not pow(gg0, 1<<(k4gg0-1), N) in [1, Nmm])
        assert (not pow(g0, N-1, N) == 1) if may_k4gg0 is None else (pow(g0, odd4Nmm<<k4gg0, N) == 1 and not pow(g0, odd4Nmm<<(k4gg0-1), N) in [1, Nmm])
    ######################
    if 0b00:
        if N == 645 and g0 == 2:
            print_err([(N, g0), k4gg0, pow(g0, odd4Nmm<<(k4gg0-1), N)])
                # --> [(645, 2), 2, 259]
            # [645 == 3*5*43]
            # [259 %3 == 1] # +1
            # [259 %5 == 4] # -1
            # [259%43 == 1] # +1
    return (gg0, gg_ls, may_k4gg0)
#end-def _validate_witness4composite__5primality_test_of_Miller_Rabin(N, Nmm, ez4Nmm, odd4Nmm, g0, /, *, enhanced):

def _test_g(N, g, /):
    ft = gcd(g, N)
    if 1 < ft < N:
        raise CompositeCertificate__nontrivial_factor(N, ft)
    elif ft == N:
        raise ValueError__N_divs_g((N, g))
    elif ft == 1:
        pass
    else:
        raise 000
    #assert ft == 1
class Tester4composite_via_even_Nmm:
    #primality_test_of_Miller_Rabin
    r'''[[[
######################
py_adhoc_call   seed.math.primality_proving__plain   @_4min_witness4composite__may_be_composite
    -->None # [..2**16]
py_adhoc_call   seed.math.primality_proving__plain   @_4min_witness4composite__may_be_composite   --begin='2**16'   --end='2**17'
    -->None
py_adhoc_call   seed.math.primality_proving__plain   @_4min_witness4composite__may_be_composite   --begin='2**17'   --end='2**18'
    -->None
py_adhoc_call   seed.math.primality_proving__plain   @_4min_witness4composite__may_be_composite   --begin='2**18'   --end='2**19'
    -->None
######################
[:min_witness4composite__may_be_composite:primality_test_of_Miller_Rabin]:here
[len({a,b,-a,-b}%N) == 4][a**2 %N == b**2 %N == Nmm] ==>> [gcd(a*b) %N == 1][a*b %N =!= Nmm][(a*b)**2 %N == 1]

[len({a,b,-a,-b}%N) == 4][a**2 %N == b**2 %N == Nmm]:
    !! [gcd(N,Nmm) == 1]
    !! [a**2 %N == b**2 %N == Nmm]
    [gcd(a*b) %N == 1]
    !! [a =!= b]
    !! [a**2 %N == b**2 %N == Nmm]
    [a*b %N =!= Nmm]
    [(a*b)**2 %N == 1]
    [(a*b) is witness4composite<%N>]
[len({a,b,-a,-b}%N) == 4][a**2 %N == b**2 %N == Nmm]:
    [gcd(a**2+1,b**2+1) %N == 0]
    [(a-b)*(a+b) %N == 0]
    [(a-b) %N =!= 0]
    [(a+b) %N =!= 0]

    [(a,b,N) := (8,18,65)]:
        [(a*b) %N == 14]

>>> [x for x in range(65) if pow(x,2,65)==1]
[1, 14, 51, 64]
>>> [x for x in range(65) if pow(x,2,65)==64]
[8, 18, 47, 57]
>>> [x for x in range(65) if pow(x,2,65)==14]
[12, 27, 38, 53]
>>> [x for x in range(65) if pow(x,2,65)==51]
[21, 31, 34, 44]
>>> 8**2 %65
64
>>> 18**2 %65
64
>>> 8*18 %65
14
>>> 14**2 %65
1

    #]]]'''#'''
    def __init__(sf, N, /, *, max1_k=None, enhanced=True):
        assert N >= 3
        assert N %2 == 1
        Nmm = N -1
        (ez4Nmm, odd4Nmm) = factor_pint_out_power_of_base_(2, Nmm)
        # !! [N %2 == 1]
        # [ez4Nmm >= 1]

        if max1_k is None:
            if not enhanced:
                # [max1_k := 2] turnoff enhanced__primality_test_of_Miller_Rabin
                max1_k = 2
                # !! [ez4Nmm >= 1]
                # [2 <= max1_k <= 1+ez4Nmm]
            else:
                max1_k = 1+min(ez4Nmm, floor_log2(1+floor_log2(N)))
                # !! [N >= 3]
                # [floor_log2(N) >= 1]
                # [floor_log2(1+floor_log2(N)) >= floor_log2(1+1) == 1]
                # !! [ez4Nmm >= 1]
                # [1 <= min(ez4Nmm, floor_log2(1+floor_log2(N))) <= ez4Nmm]
                # [2 <= max1_k <= 1+ez4Nmm]
            max1_k
            # [2 <= max1_k <= 1+ez4Nmm]
        else:
            check_int_ge(2, max1_k)
            # [max1_k >= 2]
            max1_k = min(1+ez4Nmm, max1_k)
            # !! [ez4Nmm >= 1]
            # [2 <= max1_k <= 1+ez4Nmm]
        # [2 <= max1_k <= 1+ez4Nmm]
        max1_k
            # sz ~ O(2**max1_k) ~ O(floor_log2(N))

        if 0b00:
            #限制max1_k看看是否提速
            upperbound = 9 #sz = 256
            max1_k = min(upperbound, max1_k)

        assert ez4Nmm >= 1
        assert 2 <= max1_k <= 1+ez4Nmm
        # [2 <= max1_k <= 1+ez4Nmm]
        # [ez4Nmm >= 1]

        k2roots = [[1], [Nmm]]
        sf._root2k = {1:0, Nmm:1}
        #sf._root2square_lnks = {1:null_tuple, Nmm:(1, null_tuple)}
        sf._data = (N, Nmm, ez4Nmm, odd4Nmm, max1_k, k2roots)
    def test_(sf, g0, /):
        '-> (gg0, k4gg0) | ^CompositeCertificate__witness4composite | ^CompositeCertificate__nontrivial_factor | ^ValueError__N_divs_g'
        ######################new api: return (gg0, k4gg0)
        ##postcondition:
        # [gg0 == g0**odd4Nmm %N]
        # [[gg0 == 1] <-> [k4gg0 == 0]]
        # [[gg0 =!= 1] <-> [1 <= k4gg0 <= ez4Nmm]]
        # [[1 <= k4gg0 <= ez4Nmm] -> [gg0**(2**(k4gg0-1)) %N == Nmm]]
        ######################old api: return None
        #'-> None | ^CompositeCertificate__witness4composite | ^CompositeCertificate__nontrivial_factor | ^ValueError__N_divs_g'
        (N, Nmm, ez4Nmm, odd4Nmm, max1_k, k2roots) = sf._data
        root2k = sf._root2k
        #root2square_lnks = sf._root2square_lnks

        _test_g(N, g0)
            # ^CompositeCertificate__nontrivial_factor
            # ^ValueError__N_divs_g
        # [gcd(g0, N) == 1]


        ######################new:
        #new_version_test6Tester4composite_via_even_Nmm:here
        #   enhanced__primality_test_of_Miller_Rabin
        #
        def _extend_roots(gg_ls, /):
            # [gg_ls[-1] in k2roots[-1]]
            if 0:
                gg = gg_ls[-1]
                k0 = root2k[gg]
                assert k0 == len(k2roots)-1
            else:
                k0 = len(k2roots)-1
            k0
            assert k0 >= 1

            dsz = max1_k -len(k2roots)
            ggs = gg_ls[-1-dsz:-1]
            assert len(ggs) <= dsz
            for gg in reversed(ggs):
                roots = {r*gg %N for rs in k2roots for r in rs}
                k = len(k2roots)
                if not len(roots) == 1<<(k-1): raise 000
                k2roots.append(roots)
                root2k.update((r, k) for r in roots)
                if not len(root2k) == 1<<(len(k2roots)-1): raise 000
            assert 2 <= len(ggs)+k0+1 <= len(k2roots) <= max1_k
            return
        def _raise_factor2(gg_ls, k, /):
            # [len(gg_ls) >= 2]
            # not$ [gg_ls[-2] in root2k]
            # [gg_ls[-1] in root2k]
            # [not$ gg_ls[-1] in k2roots[-1]]
            # [gg_ls[-1] in k2roots[root2k[gg_ls[-1]]]]
            # [k == root2k[gg_ls[-1]]]
            gg = gg_ls[-2]
            gg_gg = gg_ls[-1]
            #k = root2k[gg_gg]
            raise _raise_factor(N, k2roots, k, gg_gg, gg)
                # [k+1 < len(k2roots)]
                # [not$ gg in k2roots[k+1]]
                # [gg_gg in k2roots[k]]
                # [gg_gg == gg**2 %N]
            return
        gg = gg0 = pow(g0, odd4Nmm, N)
        may_k = root2k.get(gg)
        #if gg in root2k:
        if not may_k is None:
            # [gg in root2k]
            k = may_k
            #assert gg in k2roots[k]
            k4gg0 = k
            pass
            #return
        else:
            # [not$ gg in root2k]
            sz = len(k2roots)
            #last_roots = k2roots[-1]
            gg_ls = [gg]
            # [not$ gg_ls[-1] in root2k]
            for _ in range(ez4Nmm-(sz-1)):
                # [not$ gg_ls[-1] in root2k]
                gg = pow(gg, 2, N)
                gg_ls.append(gg)
                # [not$ gg_ls[-2] in root2k]
                # [MAYBE$ gg_ls[-1] in root2k]
                may_k = root2k.get(gg)
                if may_k is None:
                    # [not$ gg_ls[-1] in root2k]
                    continue
                # [gg_ls[-1] in root2k]
                k = may_k
                # [gg_ls[-1] in k2roots[k]]
                if k == sz-1:
                    #pass test@g0
                    # [N is g0-SPRP]
                    #
                    # [gg_ls[-1] in k2roots[-1]]
                    k4gg0 = k + len(gg_ls)-1
                    _extend_roots(gg_ls)
                    break
                    #return
                else:
                    #composite
                    #
                    # [not$ gg_ls[-1] in k2roots[-1]]
                    # [gg_ls[-1] in k2roots[k]]
                    # [not$ gg_ls[-2] in root2k]
                    raise _raise_factor2(gg_ls, k)
                # [gg_ls[-1] in root2k]
                #   ==>> cannot enter next round
                raise 000
            else:
                # [not$ gg_ls[-1] in root2k]
                if 1:
                    #see:_debug__N_eq_645
                    # bug fix: require more square to try to find nontrivial_factor
                    #
                    # [not$ gg_ls[-1] in root2k]
                    gg # 对标 [k==sz-1]
                    max_k4gg_gg = sz-1 -1
                    # [gg_gg =[def]= gg**2 %N]
                    # [@[k > max_k4gg_gg] -> [not$ gg_gg in k2roots[k]]]
                    for max_k4gg_gg in range(max_k4gg_gg+1)[::-1]:
                        # [not$ gg_ls[-1] in root2k]
                        # [@[k > max_k4gg_gg] -> [not$ gg_gg in k2roots[k]]]
                        gg = pow(gg, 2, N)
                        gg_ls.append(gg)
                        max_k4gg = max_k4gg_gg
                        # [@[k > max_k4gg] -> [not$ gg in k2roots[k]]]
                        # [not$ gg_ls[-2] in root2k]
                        # [MAYBE$ gg_ls[-1] in root2k]
                        may_k = root2k.get(gg)
                        if may_k is None:
                            # [not$ gg_ls[-1] in root2k]
                            continue
                        # [gg_ls[-1] in root2k]
                        k = may_k
                        # [gg_ls[-1] in k2roots[k]]
                        # !! [@[k > max_k4gg] -> [not$ gg in k2roots[k]]]
                        # [k <= max_k4gg]
                        assert 0 <= k <= max_k4gg < sz-1
                        # found nontrivial_factor!
                        #
                        # [k < sz-1]
                        # [gg_ls[-1] in k2roots[k]]
                        # [not$ gg_ls[-2] in root2k]
                        raise _raise_factor2(gg_ls, k)
                    else:#for-else
                        # witness4composite
                        # [g0**Nmm %N =!= 1]
                        pass
                    # witness4composite
                    pass
                # witness4composite
                # [g0**Nmm %N =!= 1]
                try:
                    raise CompositeCertificate__witness4composite(N, g0)
                except ValidateFail:
                    if 0b01:
                        #see:_debug__N_eq_645
                        if N == 645 and g0 == 2:
                            print_err([(N, g0), max1_k, sz, k2roots, gg_ls])
                                # --> [(645, 2), 2, 2, [[1], [644]], [257, 259]]
                            assert gg0 == 257
                    # call:_4min_witness4composite__may_be_composite():raise:
                    # ValidateFail: (645, 2)
                    #   but pass _validate_witness4composite__5primality_test_of_Miller_Rabin
                    enhanced = (max1_k > 2)
                    try:
                        _validate_witness4composite__5primality_test_of_Miller_Rabin(N, Nmm, ez4Nmm, odd4Nmm, g0, enhanced=enhanced)
                    except NotImplementedError:
                        # curr only support [enhanced==False]
                        pass
                    raise #re-raise the ValidateFail
            k4gg0
        k4gg0
        gg0
        if 0:
            assert gg0 == pow(g0, odd4Nmm, N)
            assert (k4gg0 == 0) if gg0 == 1 else (pow(gg0, 1<<(k4gg0-1), N) == N-1)
        ##postcondition:
        # [gg0 == g0**odd4Nmm %N]
        # [[gg0 == 1] <-> [k4gg0 == 0]]
        # [[gg0 =!= 1] <-> [1 <= k4gg0 <= ez4Nmm]]
        # [[1 <= k4gg0 <= ez4Nmm] -> [gg0**(2**(k4gg0-1)) %N == Nmm]]
        return (gg0, k4gg0)
        return None
        ######################old:
        gg = pow(g0, odd4Nmm, N)
        gg_ls = [gg]
        if gg == 1:
            pass
        elif gg == Nmm:
            pass
        else:
            for _ in range(ez4Nmm-1):
                gg = pow(gg, 2, N)
                gg_ls.append(gg)
                if gg == Nmm:
                    break
            else:
                raise CompositeCertificate__witness4composite(N, g0)

        if gg_ls[-1] == 1:
            pass
        else:
            gg_ls.append(1)
            assert 1 < 2 <= gg_ls[-2] == Nmm < N

        gg_ls.reverse()
        gg_ls = gg_ls[:max1_k]
        sz = min(len(k2roots), len(gg_ls))
        for k in reversed(range(sz)):
            gg = gg_ls[k]
            if gg in k2roots[k]:
                break
        else:
            raise 000
        k
        if k == sz-1:
            pass
        else:
            gg = gg_ls[k+1]
            gg_gg = gg_ls[k]
            raise _raise_factor(N, k2roots, k, gg_gg, gg)


        while len(k2roots) < len(gg_ls):
            gg = gg_ls[len(k2roots)]
            roots = {r*gg %N for rs in k2roots for r in rs}
            if not len(roots) == 1<<(len(k2roots)-1): raise 000
            k2roots.append(roots)
        assert 1 <= len(gg_ls) <= len(k2roots) <= max1_k
        assert gg_ls[-1] in k2roots[len(gg_ls) -1]
        return

def _raise_factor(N, k2roots, k, gg_gg, gg, /):
    # [k+1 < len(k2roots)]
    # [not$ gg in k2roots[k+1]]
    # [gg_gg in k2roots[k]]
    # [gg_gg == gg**2 %N]

    rs = k2roots[k+1]
    assert not gg in rs
    for r in rs:
        rr = pow(r, 2, N)
        if rr == gg_gg:
            break
    else:
        raise 000
    gg, r
    assert 1 < gg < N
    assert 1 < r < N
    assert len({gg, N-gg, r, N-r}) == 4
    assert pow(gg, 2, N) == pow(r, 2, N)
    # [gg**2 =[%N]= r**2]
    # [(gg-r)*(gg+r) =[%N]= 0]
    ft = gcd(gg-r, N)
    assert 1 < ft < N
    raise CompositeCertificate__nontrivial_factor(N, ft)

#end-class Tester4composite_via_even_Nmm:


class Tester4prime_via_Nmm__complete_factorization:
    #complete_factorization
    validate_prime_certificate__Nmm__complete_factorization_
    def __init__(sf, N, j2prime_factor4Nmm, j2exp4Nmm, /):
        # not using gcd
        sf._tester = Tester4prime_via_Nmm__sqrt_case(N, j2prime_factor4Nmm, j2exp4Nmm, complete_factorization__vs__using_gcd=False)
            # ^ValueError__not_complete_factorization
    def g2js_(sf, g, /):
        '-> (done, js4g) | ^AlreadyFinish__partial_pseudo_primitive_roots | ^ValueError__N_divs_g | ^CompositeCertificate__nontrivial_factor | ^CompositeCertificate__witness4composite'
        return sf._tester.g2js_(g)
    @property
    def j2g(sf, /):
        return sf._tester.j2g

#end-class Tester4prime_via_Nmm__complete_factorization:
class Tester4prime_via_Nmm__sqrt_case:
    #sqrt_case
    validate_prime_certificate__Nmm__partial_factorization__gt_sqrtN_
    # not-require: [gcd(ft4Nmm, Nmm///ft4Nmm) == 1]
    def __init__(sf, N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, /, *, complete_factorization__vs__using_gcd=True):
        # using gcd
            # ^ValueError__not_complete_factorization
            # ^ValueError__not_sqrt_case
        assert len(j2prime_factor4ft4Nmm) == len(j2exp4ft4Nmm)# == len(j2g)
        assert all(p >= 2 for p in j2prime_factor4ft4Nmm)
        assert all(e >= 1 for e in j2exp4ft4Nmm)
        Nmm = N-1
        ft4Nmm = II(map(int.__pow__, j2prime_factor4ft4Nmm, j2exp4ft4Nmm))
        assert Nmm %ft4Nmm == 0
        #unfactored = Nmm //ft4Nmm
        ######################
        using_gcd = complete_factorization__vs__using_gcd is True
        if not using_gcd:
            #complete_factorization
            if not Nmm == ft4Nmm: raise ValueError__not_complete_factorization
        ######################
        if not N < (ft4Nmm+1)**2: raise ValueError__not_sqrt_case
        ######################
        L = len(j2exp4ft4Nmm)
        js4todo = set(range(L))
        j2g = {}
        ######################
        sf._data = (N, Nmm, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, using_gcd, js4todo, j2g)
        sf._on_new_js4todo(js4todo, j2prime_factor4ft4Nmm, Nmm)
            #init _data2!

        return
    def __repr__(sf, /):
        'tmp-for-debug'
        #sf._data = (N, Nmm, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, using_gcd, js4todo, j2g)
        #sf._data2 = (js, ps, Nmm__IIps)
        s = repr_helper(sf, _data=sf._data, _data2=sf._data2)
        s = f'[<{s}>]'
        return s
    @property
    def j2g(sf, /):
        (N, Nmm, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, using_gcd, js4todo, j2g) = sf._data
        return j2g

    def _on_new_js4g(sf, g, js4g, /):
        (N, Nmm, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, using_gcd, js4todo, j2g) = sf._data
        if not len(js4g):
            return
        for j in js4g:
            dict_add__new(j2g, j, g)
                #update emplace!
            js4todo.remove(j)
                #update emplace!
        ######################
        sf._on_new_js4todo(js4todo, j2prime_factor4ft4Nmm, Nmm)
            #update _data2

    def _on_new_js4todo(sf, js4todo, j2prime_factor4ft4Nmm, Nmm, /):
        js = sorted(js4todo)
        ps = _index(j2prime_factor4ft4Nmm, js)
        IIps = II(ps)
        Nmm__IIps = Nmm//IIps
        sf._data2 = (js, ps, Nmm__IIps)
        #return (js, ps  Nmm__IIps)

    def g2js_(sf, g, /):
        '-> (done, js4g) | ^AlreadyFinish__partial_pseudo_primitive_roots | ^ValueError__N_divs_g | ^CompositeCertificate__nontrivial_factor | ^CompositeCertificate__witness4composite'
        (N, Nmm, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, using_gcd, js4todo, j2g) = sf._data
        (js, ps, Nmm__IIps) = sf._data2
        if not js4todo:
            raise AlreadyFinish__partial_pseudo_primitive_roots
            return js4g

        _test_g(N, g)
            # ^CompositeCertificate__nontrivial_factor
            # ^ValueError__N_divs_g
        # [gcd(g, N) == 1]


        js4g = []

        it = _iter_pow_II__except_one(N, Nmm, Nmm__IIps, ps, g)
        known__g_is_root = False
        for j, p, gg in zip(js, ps, it):
            #gg = pow(g, (Nmm//p), N)
            if gg == 1:
                # [g**(Nmm///p) %N == 1]
                    #each time skip has [g**(Nmm///p) %N == 1] not only [gcd(gg-1, N) =!= 1] since:
                    #   [gcd(gg-1, N) =!= 1] ==>> [[gcd(gg-1, N) == 0]or[2 <= gcd(gg-1, N) < N]]
                    #   [gcd(gg-1, N) =!= 1] ==>> [[gg %N == 1]or[gcd(gg-1, N) is a nontrivial_factor of N]]
                    # this condition will be used to proof the_least_positive_partial_pseudo_primitive_root_mod_{if not found nontrivial_factor} be prime
                    #   用作前提条件之于:[奇素数幂模的最小伪深偏拟本原根是素数] => [:只需枚举素数兼检测整除与否@素性证明囗囗减一囗囗完全分解]:goto
                # [g**Nmm %N == 1]
                # [known__g_is_root is True]
                known__g_is_root = True
                continue
                    #skip:js4g.append(j)
            #will have: [j not in js4todo]
            #will have: [@[j :<- js4todo] -> [pj := j2prime_factor4Nmm[j]] -> [g**(Nmm///pj)%Nmm == 1]]
            #
            # [gg =!= 1]
            # !! [gcd(g, N) == 1]
            # [2 <= gg < N]
            # [1 <= gcd(gg-1, N) < N]

            if using_gcd:
                if not (ft := gcd(gg-1, N)) == 1:
                    # [gcd(gg-1, N) =!= 1]
                    # !! [1 <= gcd(gg-1, N) < N]
                    # [2 <= gcd(gg-1, N) < N]
                    # [2 <= ft < N]
                    assert 1 < ft < N
                    raise CompositeCertificate__nontrivial_factor(N, ft)
                # [gcd(gg-1, N) == 1]
            else:
                # !! [gg =!= 1]
                pass

            if not known__g_is_root:
                if not pow(gg, p, N) == 1:
                    raise CompositeCertificate__witness4composite(N, g)
                # [g**Nmm %N == 1]
                # [known__g_is_root is True]
                known__g_is_root = True
            # [known__g_is_root is True]
            # [g**Nmm %N == 1]
            # [gg =!= 1]
            # [g**(Nmm///p) %N =!= 1]
                # using_gcd => [gcd(gg-1, N) == 1]
            # [is_a_partial_pseudo_primitive_root_mod_(N, Nmm, p; g, using_gcd=using_gcd)]
            js4g.append(j)
        js4g
        sf._on_new_js4g(g, js4g)
            # update js4todo...
        111; done = not js4todo
        # [@[j :<- js4todo] -> [pj := j2prime_factor4Nmm[j]] -> [g**(Nmm///pj)%Nmm == 1]]
        return (done, js4g)

#end-class Tester4prime_via_Nmm__sqrt_case:

def return_version____primality_test__Nmm__plain__sqrt_case_(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, /, *, complete_factorization__vs__using_gcd=True):
    '-> (case, payload)/((odd_prime_case/0, j2g) | (1, witness4composite) | (2, nontrivial_factor) | (even_prime_case/3, None)) | ^ERH__fail/Fail__unknown_fine_upperbound4primitive_root | ^ValueError__not_complete_factorization | ^ValueError__not_sqrt_case'
    # not-require: [gcd(ft4Nmm, Nmm///ft4Nmm) == 1]
    try:
        raise_version____primality_test__Nmm__plain__sqrt_case_(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, complete_factorization__vs__using_gcd=complete_factorization__vs__using_gcd)
    except (PrimeCertificate__sqrt_case, PrimeCertificate__complete_factorization) as exc:
        (_N, _j2prime_factor4ft4Nmm, _j2exp4ft4Nmm, j2g) = exc.args
        case = 0
        return (0, j2g)
        return (0, N, j2prime_factor4ft4Nmm, j2g)
    except CompositeCertificate__witness4composite as exc:
        (_N, witness4composite) = exc.args
        return (1, witness4composite)
    except CompositeCertificate__nontrivial_factor as exc:
        (_N, nontrivial_factor) = exc.args
        return (2, nontrivial_factor)
    except PrimeCertificate__TWO as exc:
        () = exc.args
        return (3, None)
    else:
        raise 000
    raise 000
#end-def return_version____primality_test__Nmm__plain__sqrt_case_(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, /, *, complete_factorization__vs__using_gcd=True):


_p2least_positive_primitive_root = {3:2,7:3,23:5}
def raise_version____primality_test__Nmm__plain__sqrt_case_(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, /, *, complete_factorization__vs__using_gcd=True):
    # not-require: [gcd(ft4Nmm, Nmm///ft4Nmm) == 1]
    #
    #old-name:def primality_test__Nmm__plain__sqrt_case_(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, /, *, complete_factorization__vs__using_gcd=True):
    '-> ^PrimeCertificate__TWO | ^PrimeCertificate__sqrt_case | ^PrimeCertificate__complete_factorization | ^CompositeCertificate__nontrivial_factor | ^CompositeCertificate__witness4composite | ^ERH__fail/Fail__unknown_fine_upperbound4primitive_root | ^ValueError__not_complete_factorization | ^ValueError__not_sqrt_case'
            # xxx ^AlreadyFinish__partial_pseudo_primitive_roots
            # xxx ^ValueError__N_divs_g
    check_int_ge(2, N)
    check_type_is(bool, complete_factorization__vs__using_gcd)

    if not is_odd(N):
        if N == 2:
            raise PrimeCertificate__TWO
        raise CompositeCertificate__nontrivial_factor(N, 2)
    # [N >= 3][N %2 == 1]



    tp = Tester4prime_via_Nmm__sqrt_case(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, complete_factorization__vs__using_gcd=complete_factorization__vs__using_gcd)
            # ^ValueError__not_complete_factorization
            # ^ValueError__not_sqrt_case
    tc = Tester4composite_via_even_Nmm(N)

    assert len(j2prime_factor4ft4Nmm)
        #=> assert len(tp.js4todo)
        #=> no ^AlreadyFinish__partial_pseudo_primitive_roots


    ######################
    lazy_prime_seq = prime_gen.get_or_mk_lazy_prime_seq_()
        # hold weakref

    ######################
    #trial_division
    max1_p4trial_division = (1+floor_sqrt(N))
    floor_log2_N = floor_log2(N)
    num_primes4trial_division = 1+floor_log2_N
    if 0b00:
        #限制num_primes4trial_division看看是否提速
        num_primes4trial_division = min(256, num_primes4trial_division)
        #没必要:pow(g, Nmm/ft, N) 运算量 大概就是 floor_log2_N次操作
    for p in islice(prime_gen, num_primes4trial_division):
        if not p < max1_p4trial_division:
            # [N is prime]
            break
        if N%p == 0:
            raise CompositeCertificate__nontrivial_factor(N, p)



    ######################
    max1_witness4composite5trial_division = max1_p4trial_division
    max1_witness4composite5ERH = (1+floor_log2_N)**2
        # ERH: [2..<2*ln(n)**2]
        #
        # !! [log2(math.e)**2 > 2]
        # !! [n >= 1]
        # [2*ln(n)**2 == 2*(log2(n)/log2(math.e))**2 < log2(n)**2 <= ceil_log2(n)**2 < (1+floor_log2(n))**2]
        # [2*ln(n)**2 < (1+floor_log2(n))**2]
        #     proof___floor_log2_ver___ERH:goto
        #
        # extra:[@[n <- [2**48..]] -> [2*ln(n)**2 < 1+floor_log2(n)**2]]
    max1_witness4composite = min(max1_witness4composite5ERH, max1_witness4composite5trial_division)

    _p2least_positive_primitive_root
    if N in _p2least_positive_primitive_root:
        max1_witness4composite = max(1+_p2least_positive_primitive_root[N], max1_witness4composite)

    #_p2least_positive_primitive_root = {3:2,7:3,23:5}
    #if N == 3:
    #    max1_witness4composite = max(3, max1_witness4composite)
    #    # max(3, ...) for [N==3][primitive_root==2]
    #elif N == 7:
    #    max1_witness4composite = max(4, max1_witness4composite)
    #    # max(4, ...) for [N==7][primitive_root==3]
            #<<==:
            #view ../../python3_src/nn_ns/math_nn/numbers/_patch_prime_..b001918.b002233.out.txt
            #   索引纟素数:素数:最小正本原根:最小素本原根
            #   1 3 2 2
            #   3 7 3 3
            #   8 23 5 5
            #
            #
            # Fail__unknown_fine_upperbound4primitive_root: (7, [2, 3], [1, 1], False, 3)
            # Fail__unknown_fine_upperbound4primitive_root: (23, (2, 11), (1, 1), False, 5)
            # Fail__unknown_fine_upperbound4primitive_root: (23, [2, 11], [1, 1], False, 5, [<Tester4prime_via_Nmm__sqrt_case(_data = (23, 22, [2, 11], [1, 1], False, {0}, {1: 2}), _data2 = ([0], [2], 11))>])
            #   why?
            #
            #
    assert 3 <= max1_witness4composite <= N
    # !! 最小正本原根的上限估值未明确
    if 1:
        #max1_partial_pseudo_primitive_root4prime = ???
        max1_partial_pseudo_primitive_root4prime = max1_witness4composite
            # 最小正本原根的上限估值未明确


    def f2(tp, /):
        j2g = tp.j2g
        assert len(j2g) == len(j2exp4ft4Nmm)
        j2g = tuple(j2g[j] for j in range(len(j2g)))
        T = PrimeCertificate__sqrt_case if complete_factorization__vs__using_gcd is True else PrimeCertificate__complete_factorization
        raise T(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, j2g)
        raise T(N, j2prime_factor4ft4Nmm, j2g)
    ######################new-version:
    #new-version vs old-version:
    #   new-version:both tc,tp try prime g
    #   old-version:tc try prime g; tp try g >= 2
    #######
    # !! [:素数模的前提下囗囗最小正偏伪本原根必是素数]:goto
    # [tp.g2js_(g) 只需测试 素数g(g一定最小)；tc.test_(g) 不太对(g不一定最小？不太肯定)，但 素数组合遍历效率高，已经足够作为 合数证据]
    #   [:min_witness4composite__may_be_composite:primality_test_of_Miller_Rabin]:goto
    #######
    # old-reason but ok:
    #   !! [[0 < g4ft4Nmm < N] -> [[is_prime_(N)]or[[b :<- [2..<g4ft4Nmm]] -> [is_prime_(b)] -> [b**Nmm %N == 1]]] -> [g4ft4Nmm is_the_least_positive ft4Nmm-partial_pseudo_primitive_root<N>] -> [is_prime_(g4ft4Nmm)]]
    #######
    max1_both = max(max1_witness4composite, max1_partial_pseudo_primitive_root4prime)
    for p in prime_gen:
        g = p
        if not g < max1_both:
            break
        ######################
        # for composite
        if g < max1_witness4composite:
            tc.test_(g)
                # ^CompositeCertificate__witness4composite
                # ^CompositeCertificate__nontrivial_factor
                # xxx ^ValueError__N_divs_g
                 #      [g == p < max1_witness4composite <= N]
        ######################
        # for prime
        if g < max1_partial_pseudo_primitive_root4prime:
            # [@[j :<- tp.js4todo] -> [pj := j2prime_factor4Nmm[j]] -> @[gp :<- PRIMES] -> [gp < g] -> [gp**(Nmm///pj)%Nmm == 1]]
                #==>> [@[j :<- tp.js4todo] -> [pj := j2prime_factor4Nmm[j]] -> @[g_ :<- [1..<g]] -> [g_**(Nmm///pj)%Nmm == 1]]
            (done, js4g) = tp.g2js_(g)
            # [@[j :<- new tp.js4todo] -> [pj := j2prime_factor4Nmm[j]] -> @[gp :<- PRIMES] -> [gp <= g] -> [gp**(Nmm///pj)%Nmm == 1]]
                 # xxx ^AlreadyFinish__partial_pseudo_primitive_roots
                 #      [N>=3]=>[init-js4todo =!= {}]
                 #      done=>raise
                 # xxx ^ValueError__N_divs_g
                 #      [g == j < max1_witness4composite <= N]
                 # xxx ^CompositeCertificate__nontrivial_factor
                 # xxx ^CompositeCertificate__witness4composite
            if done:
                raise f2(tp)
                    # ^PrimeCertificate__sqrt_case if complete_factorization__vs__using_gcd
                    # ^PrimeCertificate__complete_factorization
        ######################

    raise Fail__unknown_fine_upperbound4primitive_root(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, complete_factorization__vs__using_gcd, max1_partial_pseudo_primitive_root4prime, tp)
    raise ERH__fail(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, complete_factorization__vs__using_gcd)
    ######################old-version:
    def iter2(tp, /):
        #!!!!!!!wrong!!!!!!!
        #   partial_pseudo_primitive_root must be prime!!!
        for idx in range(2, max1_witness4composite):
        #for idx, p in zip(range(2, max1_witness4composite), prime_gen):
            #max1_partial_pseudo_primitive_root4prime = ???
            #g = p
            g = idx
                 # !!!idx not p/(prime_gen[idx-2])!!!
                 # idx is better than p here # via compare runing
                 #      although weird
                 #  ???why??? unknown yet
                 #  [a**(odd4Nmm*2**ea) =[%N]= -1]:
                 #      [(a**x) **(odd4Nmm*2**ea) =[%N]= (-1)**x] #!!! pass test
                 #  [a**(odd4Nmm*2**ea) =[%N]= -1][b**odd4Nmm =[%N]= 1]:
                 #      [(a**x * b**y) **(odd4Nmm*2**ea) =[%N]= (-1)**x] #!!! pass test
                 #  [a**(odd4Nmm*2**ea) =[%N]= -1][c**(odd4Nmm*2**ec) =[%N]= -1][ea > ec]:
                 #      [(a**x * c**y) **(odd4Nmm*2**ea) =[%N]= (-1)**x] #!!! can not conform pass test
                 #      [(a**(2*z+1) * c**y) **(odd4Nmm*2**ea) =[%N]= -1] #!!! pass test
                 #      [aa := a**(2**(ea-ec) %N]
                 #      [aa**(odd4Nmm*2**ec) =[%N]= -1]
                 #          # i.e. [eaa == ec]
                 #          # i.e. if [aa =!= c] then convert (a,c) to (aa,c) meeting below case:
                 #  [a**(odd4Nmm*2**ea) =[%N]= -1][c**(odd4Nmm*2**ec) =[%N]= -1][ea == ec][a =!= c][g := (a**x * c**y)]:
                 #      #!!! the only possible case to fail !!!
                 #      ...
                 #
            (done, js4g) = tp.g2js_(g)
                 # xxx ^AlreadyFinish__partial_pseudo_primitive_roots
                 #      [N>=3]=>[init-js4todo =!= {}]
                 #      done=>raise
                 # xxx ^ValueError__N_divs_g
                 #      [g == j < max1_witness4composite <= N]
                 # ^CompositeCertificate__nontrivial_factor
                 # ^CompositeCertificate__witness4composite
            if done:
                raise f2(tp)
                    # ^PrimeCertificate__sqrt_case if complete_factorization__vs__using_gcd
                    # ^PrimeCertificate__complete_factorization
            yield
    def iter1(tc, /):
        for p in prime_gen:
            if not p < max1_witness4composite:
                # curr j is unused!
                # assume [N is prime]
                break
            g = p
            tc.test_(g)
                # ^CompositeCertificate__witness4composite
                # ^CompositeCertificate__nontrivial_factor
                # xxx ^ValueError__N_divs_g
                 #      [g == p < max1_witness4composite <= N]
            yield
    it1 = iter1(tc)
    it2 = iter2(tp)
    for _ in zip(it1, it2):
        # it1 for composite
        # it2 for prime
        pass
    # assume [N is prime]
    for _ in it2:
        # it2 for prime
        pass
    raise ERH__fail(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, complete_factorization__vs__using_gcd)
#end-def raise_version____primality_test__Nmm__plain__sqrt_case_(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, /, *, complete_factorization__vs__using_gcd=True):
def __():
    assert (0, (2,)) == return_version____primality_test__Nmm__plain__sqrt_case_(3, [2], [1], complete_factorization__vs__using_gcd=False)
    assert (0, (3, 2)) == return_version____primality_test__Nmm__plain__sqrt_case_(7, [2,3], [1,1], complete_factorization__vs__using_gcd=False)
        # Fail__unknown_fine_upperbound4primitive_root: (7, [2, 3], [1, 1], False, 3)
    assert (0, (5, 2)) == return_version____primality_test__Nmm__plain__sqrt_case_(23, [2,11], [1,1], complete_factorization__vs__using_gcd=False)
        # Fail__unknown_fine_upperbound4primitive_root: (23, [2, 11], [1, 1], False, 5)
        # Fail__unknown_fine_upperbound4primitive_root: (23, [2, 11], [1, 1], False, 5, [<Tester4prime_via_Nmm__sqrt_case(_data = (23, 22, [2, 11], [1, 1], False, {0}, {1: 2}), _data2 = ([0], [2], 11))>])
        #
__()


#CompositeCertificate__nontrivial_factor
#CompositeCertificate__witness4composite
#nontrivial_factor
#witness4composite


class _ValidatableLineContinueIO4primality_certificate__not_output_composite(IValidatableLineContinueIO):
    #@override
    def iter_generate_continuity_infos(sf, /):
        return count_(2)
    #@override
    def validate_line_value_payload_(sf, line_value, /):
        (num_bits4N, odd4Nmm, ez4Nmm, gz) = line_value
        case = 0
            #prime
        Nmm = odd4Nmm << ez4Nmm
        N = Nmm +1
        assert N.bit_length() == num_bits4N
        PrimeCertificate__sqrt_case(N, (2,), (ez4Nmm,), (gz,), validate=True)
        return
    #@override
    def validate_line_value_continuity_info_(sf, line_value, continuity_info, /):
        (num_bits4N, odd4Nmm, ez4Nmm, gz) = line_value
        assert num_bits4N == continuity_info


class _ValidatableLineContinueIO4primality_certificate__output_composite(IValidatableLineContinueIO):
    #@override
    def iter_generate_continuity_infos(sf, /):
        return iter_N_exs__zpow_dominance_Nmm__fixed_bit_length_(2, 1)
    #@override
    def line_value2may_iter_regenerate_continuity_infos_(sf, line_value, /):
        (num_bits4N, odd4Nmm, ez4Nmm, case, certificate) = line_value
        if case == 0:
            #prime
            return iter_N_exs__zpow_dominance_Nmm__fixed_bit_length_(num_bits4N+1, 1)
        return None
    #@override
    def validate_line_value_payload_(sf, line_value, /):
        (num_bits4N, odd4Nmm, ez4Nmm, case, certificate) = line_value
        Nmm = odd4Nmm << ez4Nmm
        N = Nmm +1
        assert N.bit_length() == num_bits4N
        check_int_ge_lt(0, 3, case)
        if case == 0:
            #prime
            gz = certificate
            PrimeCertificate__sqrt_case(N, (2,), (ez4Nmm,), (gz,), validate=True)
        elif case == 1:
            witness4composite = certificate
            CompositeCertificate__witness4composite(N, witness4composite, validate=True)
        elif case == 2:
            nontrivial_factor = certificate
            CompositeCertificate__nontrivial_factor(N, nontrivial_factor, validate=True)
        else:
            raise 000
        return
    #@override
    def validate_line_value_continuity_info_(sf, line_value, continuity_info, /):
        (num_bits4N, odd4Nmm, ez4Nmm, case, certificate) = line_value
        assert (num_bits4N, odd4Nmm, ez4Nmm) == continuity_info

def validate_output5iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(ipath, /, *, to_validate_continuity=True, to_validate_certificate=True):
    _impl__validate_output5iter_continue4iter_xxx_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(ipath, to_validate_continuity=to_validate_continuity, to_validate_certificate=to_validate_certificate, had_output_composite=False)
def validate_output5iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(ipath, /, *, to_validate_continuity=True, to_validate_certificate=True):
    _impl__validate_output5iter_continue4iter_xxx_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(ipath, to_validate_continuity=to_validate_continuity, to_validate_certificate=to_validate_certificate, had_output_composite=True)
def _impl__validate_output5iter_continue4iter_xxx_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(ipath, /, *, to_validate_continuity, to_validate_certificate, had_output_composite):
    validatable = _mk_validatable4zpow(ipath, had_output_composite=had_output_composite)
    validatable.validate_whole_file_(to_validate_continuity=to_validate_continuity, to_validate_payload=to_validate_certificate)
    return
def _mk_validatable4zpow(ipath, /, *, had_output_composite):
    if had_output_composite:
        T = _ValidatableLineContinueIO4primality_certificate__output_composite
    else:
        T = _ValidatableLineContinueIO4primality_certificate__not_output_composite
    T
    validatable = T.from_path_(None, ipath, allow_create=False)
    return validatable
def _iter_read_output4zpow(ipath, /, *, had_output_composite):
    validatable = _mk_validatable4zpow(ipath, had_output_composite=had_output_composite)
    return validatable.iter_read_line_values_()

def extract_odd4Nmm_seq_from_output5iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(ipath, /):
    return tuple(iter_extract_odd4Nmm_seq_from_output5iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(ipath))
def iter_extract_odd4Nmm_seq_from_output5iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(ipath, /):
    return _impl__iter_extract_odd4Nmm_seq_from_output5iter_continue4iter_xxx_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(ipath, had_output_composite=False)
def _impl__iter_extract_odd4Nmm_seq_from_output5iter_continue4iter_xxx_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(ipath, /, *, had_output_composite):
    it = _iter_read_output4zpow(ipath, had_output_composite=had_output_composite)
    if had_output_composite:
        for (num_bits4N, odd4Nmm, ez4Nmm, case, certificate) in it:
            if case == 0:
                yield odd4Nmm
    else:
        for (num_bits4N, odd4Nmm, ez4Nmm, gz) in it:
            yield odd4Nmm


def iter_continue4iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(path, /, *, allow_create=True):
    return _impl__iter_continue4iter_xxx_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(path, allow_create=allow_create, output_composite=True)
def iter_continue4iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(path, /, *, allow_create=True):
    return _impl__iter_continue4iter_xxx_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(path, allow_create=allow_create, output_composite=False)
def _impl__iter_continue4iter_xxx_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(path, /, *, allow_create, output_composite):
    line_continue_io = LineContinueIO.from_path_(None, path, allow_create=allow_create)
    tm = line_continue_io.read_last_line_then_tmay_safe_eval_()

    if output_composite:
        f = iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
        if tm:
            [(num_bits4N, odd4Nmm, ez4Nmm, case, certificate)] = tm
    else:
        f = iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
        if tm:
            [(num_bits4N, odd4Nmm, ez4Nmm, gz)] = tm
            case = 0

    if tm:
        (num_bits4N, odd4Nmm, ez4Nmm, case, ...)
        if case == 0:
            #prime
            begin_num_bits4N = num_bits4N+1
            args = (begin_num_bits4N,)
        else:
            #composite
            begin_num_bits4N = num_bits4N
            begin_odd4Nmm = odd4Nmm +2
            args = (begin_num_bits4N, begin_odd4Nmm)
        args
    else:
        [] = tm
        args = ()
    f, args
    with line_continue_io.get_text_iofile_wrapper() as ofile:
        ofile.seek(0, SEEK_END)
        #   already at eof
        fprint = mk_fprint(ofile)
        for tpl in f(*args):
            fprint(tpl, flush=True)
            yield tpl

def iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(begin_num_bits4N=2, begin_odd4Nmm=1, /):#, *, output_composite=False
    '-> Iter (num_bits4N, odd4Nmm, ez4Nmm, gz)'
    #xxx '-> Iter ((num_bits4N, odd4Nmm, ez4Nmm, gz) if not output_composite else (num_bits4N, odd4Nmm, ez4Nmm, case, certificate))'
    it = iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(begin_num_bits4N, begin_odd4Nmm)
    for (num_bits4N, odd4Nmm, ez4Nmm, case, certificate) in it:
        #if output_composite:
        if case == 0:
            #prime
            gz = certificate
            yield (num_bits4N, odd4Nmm, ez4Nmm, gz)
    return
def iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_(begin_num_bits4N=2, begin_odd4Nmm=1, /):
    '-> Iter (num_bits4N, odd4Nmm, ez4Nmm, case, certificate) # (0,gz)|(1,witness4composite)|(2,nontrivial_factor)'
    lazy_prime_seq = prime_gen.get_or_mk_lazy_prime_seq_()
        # hold weakref

    j2prime_factor4ft4Nmm = (2,)
    for it in iter_N_exss__zpow_dominance_Nmm_(begin_num_bits4N, begin_odd4Nmm):
        for (num_bits4N, odd4Nmm, ez4Nmm) in it:
            Nmm = odd4Nmm << ez4Nmm
            N = Nmm +1
            j2exp4ft4Nmm = (ez4Nmm,)
            (case, payload) = return_version____primality_test__Nmm__plain__sqrt_case_(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, complete_factorization__vs__using_gcd=True)
            if case == 0:
                #odd_prime_case
                j2g = payload
                #gz = g2
                [gz] = j2g
                yield (num_bits4N, odd4Nmm, ez4Nmm, 0, gz)
                break
            elif case == 1:
                witness4composite = payload
                yield (num_bits4N, odd4Nmm, ez4Nmm, 1, witness4composite)
            elif case == 2:
                nontrivial_factor = payload
                yield (num_bits4N, odd4Nmm, ez4Nmm, 2, nontrivial_factor)
            elif case == 3:
                # even_prime_case
                # [N == 2]
                raise 000
            else:
                raise 000
        else:
            num_bits4N
            raise BaseException(num_bits4N) # No zpow_dominance-prime@num_bits4N???
    raise 000

def iter_N_exss__zpow_dominance_Nmm_(begin_num_bits4N=2, begin_odd4Nmm=1, /):
    '-> Iter (Iter (num_bits4N, odd4Nmm, ez4Nmm))'
    for num_bits4N in count_(begin_num_bits4N):
        it = iter_N_exs__zpow_dominance_Nmm__fixed_bit_length_(num_bits4N, begin_odd4Nmm)
        yield it
        begin_odd4Nmm = 1
    return
def iter_N_exs__zpow_dominance_Nmm__fixed_bit_length_(num_bits4N, begin_odd4Nmm=1, /):
    '-> Iter (num_bits4N, odd4Nmm, ez4Nmm)'
    assert num_bits4N >= 2
    assert begin_odd4Nmm&1 == 1
    #bug:assert 1 <= begin_odd4Nmm <= 1<<(num_bits4N-2)
        # ... <= 1 if num_bits4N==2
    assert 1 <= begin_odd4Nmm < 1<<(num_bits4N//2)
        # ... < 2 if num_bits4N==2

    for odd4Nmm in range(begin_odd4Nmm, (1<<(num_bits4N-1)) +1, 2):
        L = odd4Nmm.bit_length()
        ez4Nmm = num_bits4N -L
        if L <= ez4Nmm:
            yield (num_bits4N, odd4Nmm, ez4Nmm)
        else:
            break
    return


class RadixPowDominancePlusplusOddNumberRelated:
    r'''[[[
    # radix:e.g. 2, 10
    #
    # not-require: [gcd(significand4Nmm, radix) == 1]
    #
    [N%2 == 1]
    [Nmm%2 == 0]
    [Nmm == significand4Nmm *radix**num_tail_zeros4Nmm]
    [significand4Nmm %radix =!= 0]
    [1 <= significand4Nmm < radix**num_tail_zeros4Nmm]
          # [:radix_pow_dominance_Nmm]:here

    [radix**(num_digits4N-1) <= Nmm == N-1 < N < radix**num_digits4N]
    [num_digits4N == 1+floor_log_(radix; Nmm)]
    [num_digits4N == 1+num_tail_zeros4Nmm +floor_log_(radix;significand4Nmm)]
        # relation4convert
    !! [:radix_pow_dominance_Nmm]
    [0 <= floor_log_(radix;significand4Nmm) < num_tail_zeros4Nmm]
    [num_tail_zeros4Nmm >= 1]
    [2 <= 1+num_tail_zeros4Nmm <= num_digits4N <= 2*num_tail_zeros4Nmm]
    [num_digits4N >= 2]
        #bound
    [ceil(num_digits4N/2) <= num_tail_zeros4Nmm <= num_digits4N-1]
        #bound

    [floor_log_(radix;significand4Nmm) == num_digits4N -(1+num_tail_zeros4Nmm) <= num_digits4N -1 -ceil(num_digits4N/2) == num_digits4N//2 -1]
    [floor_log_(radix;significand4Nmm) < num_digits4N//2]
    [1 <= significand4Nmm < radix**(num_digits4N//2)]
        #bound

    ######################
    # relation4convert
    [num_digits4N == 1+num_tail_zeros4Nmm +floor_log_(radix;significand4Nmm)]
    ######################
    #bound
    [num_digits4N >= 2]
    [1 <= significand4Nmm < radix**(num_digits4N//2)]
        [floor_log_(radix;significand4Nmm) < num_digits4N//2]
    [ceil(num_digits4N/2) <= num_tail_zeros4Nmm <= num_digits4N-1]
    ######################
    #]]]'''#'''
    def __init__(sf, radix, /):
        check_int_ge(2, radix)
        sf.radix = radix
        #sf.radix_is_odd = (radix&1 == 1)
    def iter_odd_N_exs__radix_pow_dominance_Nmm__fixed_num_digits4N__(sf, num_digits4N, begin_significand4Nmm=1, /, **kwds):
        '-> Iter (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, Nmm)'
        radix = sf.radix
        return iter_odd_N_exs__radix_pow_dominance_Nmm__fixed_num_digits4N__(radix, num_digits4N, begin_significand4Nmm, **kwds)
    def iter_odd_N_exss__radix_pow_dominance_Nmm_(sf, begin_num_digits4N=2, begin_significand4Nmm=1, /, **kwds):
        '-> Iter (Iter (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, Nmm))'
        radix = sf.radix
        return iter_odd_N_exss__radix_pow_dominance_Nmm_(radix, begin_num_digits4N, begin_significand4Nmm, **kwds)
def iter_odd_N_exss__radix_pow_dominance_Nmm_(radix, begin_num_digits4N=2, begin_significand4Nmm=1, /, *, skip_begin=False, floor_log__radix__begin_significand4Nmm=None, next_pow_radix4begin_significand4Nmm=None, pow__radix__num_tail_zeros4Nmm4begin_significand4Nmm=None, floor_pow_radix4Nmm=None, begin_Nmm=None):
    '-> Iter (Iter (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, Nmm))'
    assert begin_num_digits4N >= 2
    S_lt_R = begin_significand4Nmm < radix

    if not floor_pow_radix4Nmm is None:
        background = floor_pow_radix4Nmm
    elif S_lt_R and not pow__radix__num_tail_zeros4Nmm4begin_significand4Nmm is None:
        background = pow__radix__num_tail_zeros4Nmm4begin_significand4Nmm
    else:
        background = radix**(begin_num_digits4N-1)
    background
    floor_pow_radix4Nmm = background

    for num_digits4N in count_(begin_num_digits4N):
        it = iter_odd_N_exs__radix_pow_dominance_Nmm__fixed_num_digits4N__(radix
        , num_digits4N, begin_significand4Nmm

        ,skip_begin
        =skip_begin
        ,floor_log__radix__begin_significand4Nmm
        =floor_log__radix__begin_significand4Nmm

        ,next_pow_radix4begin_significand4Nmm
        =next_pow_radix4begin_significand4Nmm

        ,pow__radix__num_tail_zeros4Nmm4begin_significand4Nmm
        =pow__radix__num_tail_zeros4Nmm4begin_significand4Nmm

        ,floor_pow_radix4Nmm
        =floor_pow_radix4Nmm

        ,begin_Nmm
        =begin_Nmm
        )
        yield it
        #update:
        #
        begin_significand4Nmm = 1
        #
        skip_begin = False
        floor_log__radix__begin_significand4Nmm = 0
        next_pow_radix4begin_significand4Nmm = radix
        background *= radix
        pow__radix__num_tail_zeros4Nmm4begin_significand4Nmm = background
        floor_pow_radix4Nmm = background
        if 0:
            #bug:since [begin_significand4Nmm==1]: 100 + 100 = 200 err # 100 + 10 == 110
            step = pow__radix__num_tail_zeros4Nmm4begin_significand4Nmm
            begin_Nmm = background +step
        else:
            begin_Nmm = background
    return
def iter_odd_N_exs__radix_pow_dominance_Nmm__fixed_num_digits4N__(radix, num_digits4N, begin_significand4Nmm=1, /, *, skip_begin=False, floor_log__radix__begin_significand4Nmm=None, next_pow_radix4begin_significand4Nmm=None, pow__radix__num_tail_zeros4Nmm4begin_significand4Nmm=None, floor_pow_radix4Nmm=None, begin_Nmm=None):
    '-> Iter (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, Nmm)'
    assert radix >= 2
    assert num_digits4N >= 2
    #(q, r) = divmod(begin_significand4Nmm, radix)
    r = begin_significand4Nmm %radix
    assert not r == 0

    #assert 1 <= begin_significand4Nmm < radix**(num_digits4N//2)
        # ... < radix if num_digits4N==2
    assert 1 <= begin_significand4Nmm
    S_lt_R = begin_significand4Nmm < radix
    if not floor_log__radix__begin_significand4Nmm is None:
        logR_S = floor_log__radix__begin_significand4Nmm
        assert logR_S >= 0
    elif S_lt_R:
        logR_S = 0
    else:
        logR_S = floor_log_(radix, begin_significand4Nmm)
    logR_S
    assert 0 <= logR_S < (num_digits4N//2)

    if not next_pow_radix4begin_significand4Nmm is None:
        endS = next_pow_radix4begin_significand4Nmm
    elif S_lt_R:
        endS = radix
    else:
        endS = radix**(1+logR_S)
    endS
    #assert 1 <= endS//radix <= begin_significand4Nmm < endS
    assert 1 <= begin_significand4Nmm < endS


    # !! [num_digits4N == 1+num_tail_zeros4Nmm +floor_log_(radix;significand4Nmm)]
    num_tail_zeros4Nmm4begin_significand4Nmm = num_digits4N -1 -logR_S

    if not pow__radix__num_tail_zeros4Nmm4begin_significand4Nmm is None:
        step = pow__radix__num_tail_zeros4Nmm4begin_significand4Nmm
    elif S_lt_R and not floor_pow_radix4Nmm is None:
        step = background = floor_pow_radix4Nmm
    else:
        step = radix**num_tail_zeros4Nmm4begin_significand4Nmm
    step
    assert step >= begin_significand4Nmm
        # !! [:radix_pow_dominance_Nmm]

    if not floor_pow_radix4Nmm is None:
        background = floor_pow_radix4Nmm
    elif S_lt_R:
        background = step
    else:
        background = radix**(num_digits4N-1)
    background

    if begin_Nmm is None:
        #begin_Nmm = begin_significand4Nmm * radix**num_tail_zeros4Nmm4begin_significand4Nmm
        begin_Nmm = begin_significand4Nmm * step
    begin_Nmm

    if S_lt_R:
        assert logR_S == 0
            #assert floor_log__radix__begin_significand4Nmm == 0
        assert endS == radix
            #assert next_pow_radix4begin_significand4Nmm == radix
        assert step == background
            #assert pow__radix__num_tail_zeros4Nmm4begin_significand4Nmm == floor_pow_radix4Nmm
        if begin_significand4Nmm == 1:
            assert begin_Nmm == background


    assert 2 <= 1+num_tail_zeros4Nmm4begin_significand4Nmm <= num_digits4N <= 2*num_tail_zeros4Nmm4begin_significand4Nmm

    min_num_tail_zeros4Nmm = (num_digits4N+1)//2
    assert min_num_tail_zeros4Nmm <= num_tail_zeros4Nmm4begin_significand4Nmm

    rg1 = range(logR_S, num_digits4N//2)
    rg2 = range(min_num_tail_zeros4Nmm, num_tail_zeros4Nmm4begin_significand4Nmm+1)[::-1]
    assert len(rg1) == len(rg2)

    d = (-r)%radix
    for logR_S, num_tail_zeros4Nmm in zip(rg1, rg2):
        assert num_digits4N == 1 +logR_S +num_tail_zeros4Nmm
        assert logR_S < num_tail_zeros4Nmm
        skip_begin
        begin_significand4Nmm
        endS
        step
        d
        begin_Nmm
        # [step == radix**num_tail_zeros4Nmm]
        assert endS <= step
            # [significand4Nmm < endS <= radix**num_tail_zeros4Nmm]
        for significand4Nmm, Nmm in zip(range(begin_significand4Nmm, endS), count_(begin_Nmm, step)):
            # [significand4Nmm < radix**num_tail_zeros4Nmm]
            #
            # [significand4Nmm %radix == (-d) %radix]
            # [(significand4Nmm +d) %radix == 0]
            if d==0:
                # [significand4Nmm %radix == 0]
                d = radix-1
                #skip:yield
            else:
                # [significand4Nmm %radix =!= 0]
                d -= 1
                if skip_begin:
                    skip_begin = False
                    #skip:yield
                elif Nmm&1 == 0:
                    # [Nmm%2 == 0]
                    # [N%2 == 1]
                    yield (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, Nmm)
                        # [N%2 == 1]
                        # [significand4Nmm %radix =!= 0]
                        # [significand4Nmm < radix**num_tail_zeros4Nmm]
            ##update for next round:
            pass
        ##update for next round:
        assert not skip_begin
        begin_significand4Nmm = endS +1
        endS *= radix
        step //= radix
        d = radix-1 # <<== r==1
        begin_Nmm = background +step

    return

def iter_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(radix, prime_or_may_j2prime_factor4radix, begin_num_digits4N=2, begin_significand4Nmm=1, /, **kwds):
    '-> Iter (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, certificate/(g|j2g))'
    sf = RadixPowDominancePlusplusOddPrimeRelated(radix, prime_or_may_j2prime_factor4radix)
    return sf.iter_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(begin_num_digits4N, begin_significand4Nmm, **kwds)
def iter_until_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(radix, prime_or_may_j2prime_factor4radix, begin_num_digits4N=2, begin_significand4Nmm=1, /, **kwds):
    '-> Iter (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, case, certificate) # (0,(g|j2g))|(1,witness4composite)|(2,nontrivial_factor)'
    sf = RadixPowDominancePlusplusOddPrimeRelated(radix, prime_or_may_j2prime_factor4radix)
    return sf.iter_until_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(begin_num_digits4N, begin_significand4Nmm, **kwds)


def iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(radix, prime_or_may_j2prime_factor4radix, /, *args, **kwds):
    sf = RadixPowDominancePlusplusOddPrimeRelated(radix, prime_or_may_j2prime_factor4radix)
    return sf.iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(*args, **kwds)

def iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(radix, prime_or_may_j2prime_factor4radix, /, *args, **kwds):
    sf = RadixPowDominancePlusplusOddPrimeRelated(radix, prime_or_may_j2prime_factor4radix)
    return sf.iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(*args, **kwds)

def validate_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(radix, prime_or_may_j2prime_factor4radix, /, *args, **kwds):
    sf = RadixPowDominancePlusplusOddPrimeRelated(radix, prime_or_may_j2prime_factor4radix)
    return sf.validate_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(*args, **kwds)

def iter_extract_significand4Nmm_seq_from_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(radix, prime_or_may_j2prime_factor4radix, /, *args, **kwds):
    sf = RadixPowDominancePlusplusOddPrimeRelated(radix, prime_or_may_j2prime_factor4radix)
    return sf.iter_extract_significand4Nmm_seq_from_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(*args, **kwds)

def extract_significand4Nmm_seq_from_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(radix, prime_or_may_j2prime_factor4radix, /, *args, **kwds):
    sf = RadixPowDominancePlusplusOddPrimeRelated(radix, prime_or_may_j2prime_factor4radix)
    return sf.extract_significand4Nmm_seq_from_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(*args, **kwds)


class RadixPowDominancePlusplusOddPrimeRelated(RadixPowDominancePlusplusOddNumberRelated):
    r'''[[[
    generalize: zpow --> radix pow
    [rpdpp_prime =[def]= radix pow dominance plusplus odd prime]
    [rpdppp =[abbr]= rpdpp_prime]

    significant digit
    significand

    # (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, case, certificate)
    # (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, g_or_j2g)
    #]]]'''#'''
    def __init__(sf, radix, prime_or_may_j2prime_factor4radix, /):
        super().__init__(radix)
        ######################
        turnon__fmt4single_prime = type(prime_or_may_j2prime_factor4radix) is int
        #p2e = None
        if turnon__fmt4single_prime:
            p = prime_or_may_j2prime_factor4radix
            j2prime_factor4radix = [p]
        else:
            may_j2prime_factor4radix = prime_or_may_j2prime_factor4radix
            if may_j2prime_factor4radix is None:
                p2e = factor_pint_by_trial_division_(radix)
                j2prime_factor4radix = sorted(p2e)
            else:
                j2prime_factor4radix = may_j2prime_factor4radix
            j2prime_factor4radix
        j2prime_factor4radix
        ######################
        check_int_ge(2, radix)
        j2prime_factor4radix[:0]
        j2prime_factor4radix = mk_tuple(j2prime_factor4radix)
        #if p2e is None:
        (p2e, unfactored_part) = semi_factor_pint_via_trial_division(j2prime_factor4radix, radix)
        if not unfactored_part == 1: raise ValueError__miss_some_prime_factors((radix, j2prime_factor4radix, unfactored_part))
        if not len(p2e) == len(j2prime_factor4radix): raise ValueError__contain_useless_prime_factors((radix, j2prime_factor4radix, {*j2prime_factor4radix}-{*p2e}))

        #sf.radix = radix
        #sf.radix_is_odd = (radix&1 == 1)
        sf.j2prime_factor4radix = j2prime_factor4radix
        sf._p2e4radix = p2e
        sf._j2exp4radix = tuple(p2e[p] for p in j2prime_factor4radix)
        sf.turnon__fmt4single_prime = turnon__fmt4single_prime

    r'''[[[ vivi:
    _impl__iter_continue4iter_xxx_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
    _mk_validatable4zpow
        _ValidatableLineContinueIO4primality_certificate__output_composite
        _ValidatableLineContinueIO4primality_certificate__not_output_composite
    _iter_read_output4zpow
    _impl__iter_extract_odd4Nmm_seq_from_output5iter_continue4iter_xxx_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
    _impl__validate_output5iter_continue4iter_xxx_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
    ==>>
    _GeneralizedValidatableLineContinueIO4primality_certificate__output_composite
    _GeneralizedValidatableLineContinueIO4primality_certificate__not_output_composite
    #]]]'''#'''
    def _mk_validatable4radix_pow(sf, ipath, /, *, had_output_composite):
        #see:_mk_validatable4zpow
        if had_output_composite:
            T = _GeneralizedValidatableLineContinueIO4primality_certificate__output_composite
        else:
            T = _GeneralizedValidatableLineContinueIO4primality_certificate__not_output_composite
        T
        validatable = T.from_path_(sf, None, ipath, allow_create=False)
        return validatable
    def _iter_read_output4radix_pow(sf, ipath, /, *, had_output_composite):
        #see:_iter_read_output4zpow
        validatable = sf._mk_validatable4radix_pow(ipath, had_output_composite=had_output_composite)
        return validatable.iter_read_line_values_()
    def iter_extract_significand4Nmm_seq_from_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(sf, ipath, /, *, had_output_composite):
        #see:_impl__iter_extract_odd4Nmm_seq_from_output5iter_continue4iter_xxx_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
        it = sf._iter_read_output4radix_pow(ipath, had_output_composite=had_output_composite)
        if had_output_composite:
            for (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, case, certificate) in it:
                if case == 0:
                    yield significand4Nmm
        else:
            for (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, g_or_j2g) in it:
                yield significand4Nmm
    def extract_significand4Nmm_seq_from_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(sf, ipath, /, *, had_output_composite):
        return tuple(sf.iter_extract_significand4Nmm_seq_from_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(ipath, had_output_composite=had_output_composite))
    def validate_output5iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(sf, ipath, /, *, to_validate_continuity, to_validate_certificate, had_output_composite):
        #see:_impl__validate_output5iter_continue4iter_xxx_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
        validatable = sf._mk_validatable4radix_pow(ipath, had_output_composite=had_output_composite)
        validatable.validate_whole_file_(to_validate_continuity=to_validate_continuity, to_validate_payload=to_validate_certificate)
        return





    def iter_continue4iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(sf, path, /, *, allow_create, output_composite):
        #see:iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_
        #see:_impl__iter_continue4iter_xxx_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
        line_continue_io = LineContinueIO.from_path_(None, path, allow_create=allow_create)
        skip_begin = False
        tm = line_continue_io.read_last_line_then_tmay_safe_eval_()

        if tm:
            if output_composite:
                [(num_digits4N, significand4Nmm, num_tail_zeros4Nmm, case, certificate)] = tm
            else:
                [(num_digits4N, significand4Nmm, num_tail_zeros4Nmm, g_or_j2g)] = tm
                case = 0
            (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, case, ...)
            if case == 0:
                #prime
                begin_num_digits4N = num_digits4N+1
                args = (begin_num_digits4N,)
            else:
                #composite
                begin_num_digits4N = num_digits4N
                begin_num_tail_zeros4Nmm = num_tail_zeros4Nmm
                args = (begin_num_digits4N, begin_num_tail_zeros4Nmm)
                skip_begin = True
            args
        else:
            [] = tm
            args = ()
        args
        f = sf.iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_
        with line_continue_io.get_text_iofile_wrapper() as ofile:
            ofile.seek(0, SEEK_END)
            #   already at eof
            fprint = mk_fprint(ofile)
            for tpl in f(*args, output_composite=output_composite, skip_begin=skip_begin):
                fprint(tpl, flush=True)
                yield tpl


    def iter_xxx_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(sf, begin_num_digits4N=2, begin_significand4Nmm=1, /, *, output_composite, **kwds):
        if output_composite:
            f = sf.iter_until_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_
        else:
            f = sf.iter_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_
        f
        return f(begin_num_digits4N, begin_significand4Nmm, **kwds)
    def iter_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(sf, begin_num_digits4N=2, begin_significand4Nmm=1, /, **kwds):
        '-> Iter (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, certificate/(g|j2g))'
        #see:iter_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
        it = sf.iter_until_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(begin_num_digits4N, begin_significand4Nmm, **kwds)
        for (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, case, certificate) in it:
            if case == 0:
                #prime
                g_or_j2g = certificate
                yield (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, g_or_j2g)
        return

    def iter_until_odd_prime_exs__radix_pow_dominance_Pmm__P_per_num_digits4N_(sf, begin_num_digits4N=2, begin_significand4Nmm=1, /, **kwds):
        '-> Iter (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, case, certificate) # (0,(g|j2g))|(1,witness4composite)|(2,nontrivial_factor)'
        #see:iter_until_odd_prime_exs__zpow_dominance_Pmm__P_per_bit_length_
        lazy_prime_seq = prime_gen.get_or_mk_lazy_prime_seq_()
            # hold weakref

        j2prime_factor4ft4Nmm = sf.j2prime_factor4radix
        _j2exp4radix = sf._j2exp4radix
        turnon__fmt4single_prime = sf.turnon__fmt4single_prime
        for it in sf.iter_odd_N_exss__radix_pow_dominance_Nmm_(begin_num_digits4N, begin_significand4Nmm, **kwds):
            for (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, Nmm) in it:
                N = Nmm +1
                j2exp4ft4Nmm = tuple(num_tail_zeros4Nmm*e for e in _j2exp4radix)
                    # not-require: [gcd(significand4Nmm, radix) == 1]
                (case, payload) = return_version____primality_test__Nmm__plain__sqrt_case_(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, complete_factorization__vs__using_gcd=True)
                if case == 0:
                    #odd_prime_case
                    j2g = payload
                    if turnon__fmt4single_prime:
                        [g] = j2g
                        g_or_j2g = g
                    else:
                        g_or_j2g = j2g
                    g_or_j2g
                    yield (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, 0, g_or_j2g)
                    break
                elif case == 1:
                    witness4composite = payload
                    yield (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, 1, witness4composite)
                elif case == 2:
                    nontrivial_factor = payload
                    yield (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, 2, nontrivial_factor)
                elif case == 3:
                    # even_prime_case
                    # [N == 2]
                    raise 000
                else:
                    raise 000
            else:
                num_digits4N
                raise BaseException(num_digits4N) # No radix_pow_dominance-prime@num_digits4N???
        raise 000


#end-class RadixPowDominancePlusplusOddNumberRelated:

class _IGeneralizedValidatableLineContinueIO4primality_certificate(IValidatableLineContinueIO):
    @classmethod
    def from_path_(cls, rpdpp_prime_related, may_setting, path, /, *, allow_create):
        binary_iofile = cls._open_(path, allow_create=allow_create)
        sf = validatable = cls(rpdpp_prime_related, may_setting, binary_iofile)
        return sf
    def __init__(sf, rpdpp_prime_related, may_setting, binary_iofile, /):
        check_type_le(RadixPowDominancePlusplusOddPrimeRelated, rpdpp_prime_related)
        sf.rpdpp_prime_related = rpdpp_prime_related
        super().__init__(may_setting, binary_iofile)
    def __repr__(sf, /):
        return repr_helper(sf, sf.rpdpp_prime_related, sf.setting, sf.binary_iofile)
class _GeneralizedValidatableLineContinueIO4primality_certificate__not_output_composite(_IGeneralizedValidatableLineContinueIO4primality_certificate):
    # (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, g_or_j2g)
    #@override
    def iter_generate_continuity_infos(sf, /):
        return count_(2)
    #@override
    def validate_line_value_payload_(sf, line_value, /):
        rpdpp_prime_related = sf.rpdpp_prime_related
        ######################
        (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, g_or_j2g) = line_value
        case = 0
            #prime
        certificate = g_or_j2g
        line_value4output_composite = (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, case, certificate)
        _validate_line_value_payload__output_composite_(rpdpp_prime_related, line_value4output_composite)

    #@override
    def validate_line_value_continuity_info_(sf, line_value, continuity_info, /):
        (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, g_or_j2g) = line_value
        assert num_digits4N == continuity_info

def _validate_line_value_payload__output_composite_(rpdpp_prime_related, line_value, /):
    ######################
    radix = rpdpp_prime_related.radix
    j2prime_factor4radix = rpdpp_prime_related.j2prime_factor4radix
    _j2exp4radix = rpdpp_prime_related._j2exp4radix
    ######################
    (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, case, certificate) = line_value
    ######################

    Nmm = significand4Nmm * radix**num_tail_zeros4Nmm
    N = Nmm +1
    if not (floor_pow_radix4Nmm := radix**(num_digits4N-1)) < N < (next_pow_radix4Nmm := floor_pow_radix4Nmm*radix): raise ValidateFail

    check_int_ge_lt(0, 3, case)
    if case == 0:
        #prime
        g_or_j2g = certificate
        if type(g_or_j2g) is int:
            g = g_or_j2g
            j2g = (g,)
        else:
            j2g = g_or_j2g
        j2g
        j2prime_factor4ft4Nmm = j2prime_factor4radix
        j2exp4ft4Nmm = tuple(num_tail_zeros4Nmm*e for e in _j2exp4radix)
        PrimeCertificate__sqrt_case(N, j2prime_factor4ft4Nmm, j2exp4ft4Nmm, j2g, validate=True)
    elif case == 1:
        witness4composite = certificate
        CompositeCertificate__witness4composite(N, witness4composite, validate=True)
    elif case == 2:
        nontrivial_factor = certificate
        CompositeCertificate__nontrivial_factor(N, nontrivial_factor, validate=True)
    else:
        raise 000
    return


class _GeneralizedValidatableLineContinueIO4primality_certificate__output_composite(_IGeneralizedValidatableLineContinueIO4primality_certificate):
    # (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, case, certificate)
    #@override
    def iter_generate_continuity_infos(sf, /):
        rpdpp_prime_related = sf.rpdpp_prime_related
        return rpdpp_prime_related.iter_odd_N_exs__radix_pow_dominance_Nmm__fixed_num_digits4N__(2, 1)
    #@override
    def line_value2may_iter_regenerate_continuity_infos_(sf, line_value, /):
        rpdpp_prime_related = sf.rpdpp_prime_related
        (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, case, certificate) = line_value
        if case == 0:
            #prime
            return rpdpp_prime_related.iter_odd_N_exs__radix_pow_dominance_Nmm__fixed_num_digits4N__(num_digits4N+1, 1)
        return None
    #@override
    def validate_line_value_payload_(sf, line_value, /):
        rpdpp_prime_related = sf.rpdpp_prime_related
        _validate_line_value_payload__output_composite_(rpdpp_prime_related, line_value)
    #@override
    def validate_line_value_continuity_info_(sf, line_value, continuity_info, /):
        (num_digits4N, significand4Nmm, num_tail_zeros4Nmm, case, certificate) = line_value
        assert (num_digits4N, significand4Nmm, num_tail_zeros4Nmm) == continuity_info[:-1]

def _debug__N_eq_645():
    N = 645
    g = 2
    tc = Tester4composite_via_even_Nmm(N, enhanced=False)
    try:
        tc.test_(g)
    except CompositeCertificate__nontrivial_factor:
        pass

if __name__ == "__main__":
    _debug__N_eq_645()
    pass
__all__


from seed.math.primality_proving__plain import *

