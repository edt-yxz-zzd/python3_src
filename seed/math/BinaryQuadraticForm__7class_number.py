#__all__:goto
#end__py_adhoc_call:goto
#   主要命令牜数据校验牜群规模纟平方根纟负数纟四倍数牜前两万个牜天然版:goto
#   主要命令牜数据校验牜群规模纟平方根纟负数纟无平方因子牜前一万个牜天然版:goto
#   主要命令牜数据校验牜群规模纟平方根纟负数纟四倍数牜前两万个牜花哨版:goto
#   主要命令牜数据校验牜群规模纟平方根纟负数纟无平方因子牜前一万个牜花哨版:goto
#SECTION:goto
#   群规模计算牜蛮力枚举:goto
#   群规模计算牜大小步碰撞:goto
#   群规模计算牜蛮力牜拆分成泛子型牜参数互素:goto
#   扩伪群规模计算牜蛮力牜拆分成泛子型牜参数互素:goto
#   群规模计算牜蛮力牜后缩放牜拆分成泛子型牜参数互素:goto
#   群规模计算牜蛮力牜先缩放牜拆分成泛子型牜参数互素:goto
#       这是 蛮力计算的主用定理 <<== [k:=(1|2)][1==gcd(Dt,k*A)]
#       {发现难以兼容}:++简化条件:分离出:[C==A]

#TODO:h(D):排除[1==gcd(A,B,C)]; 增加[C==A>0>B>-A]，最后 计算 [C==A...]
# 定理牜枚举二次型牜无需互素牜首部中部受限则尾部自动大于等于绝对值纟中部:goto
# 定理牜枚举二次型牜无需互素牜首部受限则首部自动大于等于丮保证尾部大于等于首部的下界纟绝对值纟中部厈:goto
r'''[[[
e ../../python3_src/seed/math/BinaryQuadraticForm__7class_number.py
view ../../python3_src/seed/math/BinaryQuadraticForm.py
    [h(D) == 1/Pi * w5D_(D) * Dirichlet_L_function(1,Kronecker_symbol{D}) * sqrt(-D)] # 群规模公式牜无限求和牜负判别值:goto

    [h(Df) == 1/Df * w5D_(Df) * sum[Kronecker_symbol(u;Df)*u | [u:<-[1..=-Df]]]] # 群规模公式牜有限求和牜基础负判别值:goto
TODO:
    nonprimitive --> imprimitive

seed.math.BinaryQuadraticForm__7class_number
py -m nn_ns.app.debug_cmd   seed.math.BinaryQuadraticForm__7class_number -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.BinaryQuadraticForm__7class_number:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method.py
    iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_
        mk__approximate_qfbclassno5D_

view ../../python3_src/seed/math/factor_pint/smooth_group_order_method.py
    IOps6stage3_4smooth_group_order_method
        default_search_mul_order_
        default_search_multiple_of_mul_order_
]]


'#'; __doc__ = r'#'
>>>




py_adhoc_call   seed.math.BinaryQuadraticForm__7class_number   @f
from seed.math.BinaryQuadraticForm__7class_number import *
]]]'''#'''
#SECTION
r'''[[[
py_adhoc_call{校验}
[[
view ../../python3_src/nn_ns/math_nn/numbers/b000924-class_number_of_QQ(sqrt(n_th_neg_squarefree))__fst_10000.txt
view ../../python3_src/nn_ns/math_nn/numbers/b000003-class_number_of_the_quadratic_order_of_discriminant_(-4n)__fst_20000.txt

view ../../python3_src/nn_ns/math_nn/numbers/_patch__neg_squarefree__Df_..b000924.out.txt
view ../../python3_src/nn_ns/math_nn/numbers/_patch_D_..b000003.out.txt
===
py_adhoc_call { +lineno }  seed.math.BinaryQuadraticForm__7class_number   ,iter_class_numbers5neg_discriminants__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_ =100 | grep ':[^0]' | sed 's/.*/-\0/'
===
-3:1
-4:1
-7:1
-8:1
-11:1
-12:1
-15:2
-16:1
-19:1
-20:2
-23:3
-24:2
-27:1
-28:1
-31:3
-32:2
-35:2
-36:2
-39:4
-40:2
-43:1
-44:3
-47:5
-48:2
-51:2
-52:2
-55:4
-56:4
-59:3
-60:2
-63:4
-64:2
-67:1
-68:4
-71:7
-72:2
-75:2
-76:3
-79:5
-80:4
-83:3
-84:4
-87:6
-88:2
-91:2
-92:3
-95:8
-96:4
-99:2
-100:2
===
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   ,iter_class_numbers5neg_discriminants__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_ =100 +to_mul_four +with_D | sed 's/(\([^,]*\), \([^,]*\))/\1:\2/'
    1,1,1,1,2,2,1,2,2,2,3,2,2,4,2,2,4,2,3,4,4,2,3,4,2,6,3,2,6,4,3,4,4,4,6,4,2,6,4,4,8,4,3,6,4,4,5,4,4,6,6,4,6,6,4,8,4,2,9,4,6,8,4,4,8,8,3,8,8,4,7,4,4,10,6,6,8,4,5,8,6,4,9,8,4,10,6,4,12,8,6,6,4,8,8,8,4,8,6,4
<<==:
-4:1
-8:1
-12:1
-16:1
-20:2
-24:2
-28:1
-32:2
-36:2
-40:2
-44:3
-48:2
-52:2
-56:4
-60:2
-64:2
-68:4
-72:2
-76:3
-80:4
-84:4
-88:2
-92:3
-96:4
-100:2
-104:6
-108:3
-112:2
-116:6
-120:4
-124:3
-128:4
-132:4
-136:4
-140:6
-144:4
-148:2
-152:6
-156:4
-160:4
-164:8
-168:4
-172:3
-176:6
-180:4
-184:4
-188:5
-192:4
-196:4
-200:6
-204:6
-208:4
-212:6
-216:6
-220:4
-224:8
-228:4
-232:2
-236:9
-240:4
-244:6
-248:8
-252:4
-256:4
-260:8
-264:8
-268:3
-272:8
-276:8
-280:4
-284:7
-288:4
-292:4
-296:10
-300:6
-304:6
-308:8
-312:4
-316:5
-320:8
-324:6
-328:4
-332:9
-336:8
-340:4
-344:10
-348:6
-352:4
-356:12
-360:8
-364:6
-368:6
-372:4
-376:8
-380:8
-384:8
-388:4
-392:8
-396:6
-400:4
===
vs:
    view ../../python3_src/nn_ns/math_nn/numbers/b000003-class_number_of_the_quadratic_order_of_discriminant_(-4n)__fst_20000.txt
tail -n 5 '../../python3_src/nn_ns/math_nn/numbers/b000003-class_number_of_the_quadratic_order_of_discriminant_(-4n)__fst_20000.txt'
    19996 66
    19997 150
    19998 104
    19999 52
    20000 120
py_adhoc_call { +lineno } seed.math.BinaryQuadraticForm__7class_number   ,iter_class_numbers5neg_discriminants__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_ =100 +to_mul_four -with_D | sed 's/:/ /' | diff   -   '../../python3_src/nn_ns/math_nn/numbers/b000003-class_number_of_the_quadratic_order_of_discriminant_(-4n)__fst_20000.txt' | head -n 3
    100a101,20000
    > 101 14
    > 102 4
py_adhoc_call { +lineno } seed.math.BinaryQuadraticForm__7class_number   ,iter_class_numbers5neg_discriminants__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_ =1000 +to_mul_four -with_D | sed 's/:/ /' | diff   -   '../../python3_src/nn_ns/math_nn/numbers/b000003-class_number_of_the_quadratic_order_of_discriminant_(-4n)__fst_20000.txt' | head -n 3
    1000a1001,20000
    > 1001 40
    > 1002 16
py_adhoc_call { +lineno } seed.math.BinaryQuadraticForm__7class_number   ,iter_class_numbers5neg_discriminants__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_ =5000 +to_mul_four -with_D | sed 's/:/ /' | diff   -   '../../python3_src/nn_ns/math_nn/numbers/b000003-class_number_of_the_quadratic_order_of_discriminant_(-4n)__fst_20000.txt' | head -n 3
    5000a5001,20000
    > 5001 76
    > 5002 32

===
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @list.iter_class_numbers5neg_discriminants__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_ =100 +both7nonprimitive +validate6both
    [(0, 0), (0, 0), (1, 1), (1, 1), (0, 0), (0, 0), (1, 1), (1, 1), (0, 0), (0, 0), (1, 1), (1, 2), (0, 0), (0, 0), (2, 2), (1, 2), (0, 0), (0, 0), (1, 1), (2, 2), (0, 0), (0, 0), (3, 3), (2, 2), (0, 0), (0, 0), (1, 2), (1, 2), (0, 0), (0, 0), (3, 3), (2, 3), (0, 0), (0, 0), (2, 2), (2, 3), (0, 0), (0, 0), (4, 4), (2, 2), (0, 0), (0, 0), (1, 1), (3, 4), (0, 0), (0, 0), (5, 5), (2, 4), (0, 0), (0, 0), (2, 2), (2, 2), (0, 0), (0, 0), (4, 4), (4, 4), (0, 0), (0, 0), (3, 3), (2, 4), (0, 0), (0, 0), (4, 5), (2, 4), (0, 0), (0, 0), (1, 1), (4, 4), (0, 0), (0, 0), (7, 7), (2, 3), (0, 0), (0, 0), (2, 3), (3, 4), (0, 0), (0, 0), (5, 5), (4, 6), (0, 0), (0, 0), (3, 3), (4, 4), (0, 0), (0, 0), (6, 6), (2, 2), (0, 0), (0, 0), (2, 2), (3, 6), (0, 0), (0, 0), (8, 8), (4, 6), (0, 0), (0, 0), (2, 3), (2, 3)]
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @list.iter_class_numbers5neg_discriminants__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_ =100 +both7nonprimitive +validate6both +to_mul_four
    [(1, 1), (1, 1), (1, 2), (1, 2), (2, 2), (2, 2), (1, 2), (2, 3), (2, 3), (2, 2), (3, 4), (2, 4), (2, 2), (4, 4), (2, 4), (2, 4), (4, 4), (2, 3), (3, 4), (4, 6), (4, 4), (2, 2), (3, 6), (4, 6), (2, 3), (6, 6), (3, 6), (2, 4), (6, 6), (4, 4), (3, 6), (4, 7), (4, 4), (4, 4), (6, 8), (4, 8), (2, 2), (6, 6), (4, 8), (4, 6), (8, 8), (4, 4), (3, 4), (6, 10), (4, 6), (4, 4), (5, 10), (4, 8), (4, 5), (6, 7), (6, 8), (4, 6), (6, 6), (6, 8), (4, 8), (8, 12), (4, 4), (2, 2), (9, 12), (4, 8), (6, 6), (8, 8), (4, 10), (4, 8), (8, 8), (8, 8), (3, 4), (8, 12), (8, 8), (4, 4), (7, 14), (4, 9), (4, 4), (10, 10), (6, 10), (6, 10), (8, 8), (4, 4), (5, 10), (8, 14), (6, 9), (4, 4), (9, 12), (8, 12), (4, 4), (10, 10), (6, 12), (4, 6), (12, 12), (8, 10), (6, 8), (6, 12), (4, 4), (8, 8), (8, 16), (8, 14), (4, 4), (8, 9), (6, 12), (4, 8)]
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   ,iter_class_numbers5neg_discriminants__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_ =5000 +both7nonprimitive +validate6both +to_mul_four
    ... ...
    (60, 111)

py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   ,iter_class_numbers5neg_discriminants__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_ =100 +both7nonprimitive +validate6both +to_mul_four --_path4validate:'../../python3_src/nn_ns/math_nn/numbers/b000003-class_number_of_the_quadratic_order_of_discriminant_(-4n)__fst_20000.txt' --_regex8selector4line4path:'\d+ (?P<num_BQFs7primitive>\d+)'
    ... ...
    (4, 8)
    ^Exception: ('Ds shorter than lines@_path4validate', '101 14')

#主要命令牜数据校验牜群规模纟平方根纟负数纟四倍数牜前两万个牜天然版:here
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   ,iter_class_numbers5neg_discriminants__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_ =20000 +with_D +both7nonprimitive +validate6both +to_mul_four --_path4validate:'../../python3_src/nn_ns/math_nn/numbers/b000003-class_number_of_the_quadratic_order_of_discriminant_(-4n)__fst_20000.txt' --_regex8selector4line4path:'\d+ (?P<num_BQFs7primitive>\d+)'
    ... ...
    (-79992, (104, 156))
    (-79996, (52, 104))
    (-80000, (120, 259))
    ok!
        # here:已校验@(-4 .* range(1,1+20000))

===
#主要命令牜数据校验牜群规模纟平方根纟负数纟无平方因子牜前一万个牜天然版:here
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   ,iter_class_numbers5neg_discriminants__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_ =10000 +with_D +both7nonprimitive  --case6num_Ds:squarefree_radicand_only -to_mul_four --_path4validate:'../../python3_src/nn_ns/math_nn/numbers/b000924-class_number_of_QQ(sqrt(n_th_neg_squarefree))__fst_10000.txt' --_regex8selector4line4path:'\d+ (?P<num_BQFs7primitive>\d+)'
    ... ...
    (-65748, (60, 60))
    (-65752, (38, 38))
    (-16439, (156, 156))
    (-65764, (112, 112))
    (-65768, (146, 146))
    (-65780, (112, 112))
    (-65784, (100, 100))
    ok!
        # 1th..=10000th squarefree radicand
===
]]
[[
===
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @_decompose_squarefree_part_ex7except_four6Df_ =-12 ='{2:2,3:1}'
    ((2, {2: 1}), (-3, {3: 1}))
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7CRT_ =-3 +verbose
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7CRT_ =-12
    ValueError: -12
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @class_number5neg_discriminant__7brute_force7count_primitive_binary_quadratic_forms7ratio7CRT_ =-12 +both7nonprimitive
    (1, 2)
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   ,iter_class_numbers5neg_discriminants__7brute_force7count_primitive_binary_quadratic_forms7ratio7CRT_ =12 +with_D +both7nonprimitive
    (-1, (0, 0))
    (-2, (0, 0))
    (-3, (1, 1))
    (-4, (1, 1))
    (-5, (0, 0))
    (-6, (0, 0))
    (-7, (1, 1))
    (-8, (1, 1))
    (-9, (0, 0))
    (-10, (0, 0))
    (-11, (1, 1))
    (-12, (1, 2))
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7CRT_ =-20 +verbose
    # Qfb(1,0,5)
    # Qfb(2,2,3)
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7CRT_ =-52 +verbose
    ValueError@sqrt_of_odd_mod_zpow_
        『if not y&3 == 1:raise ValueError』
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7CRT_ =-15 +verbose
    # Qfb(1,1,4)
    # Qfb(2,1,2)
    bug:include:Qfb(2,-1,2) @_count_num_Bs6A_
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @_count_num_bad_Bs6A__7CeqA_ =-15 ='{3:1,5:1}'
    1
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7CRT_ =-19 +verbose
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @_count_num_bad_Bs6A__7CeqA_ =-84 ='{2:2,3:1,7:1}'
    1
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7CRT_ =-84 +verbose
    # Qfb(1,0,21)
    # Qfb(2,2,11)
    # Qfb(3,0,7)
    # Qfb(5,4,5)
bug:
    qfbprimeform(-84,4)
        Qfb(4,0,5)
    qfbprimeform(-84,4).disc
        -84
    Qfb(4,0,5).disc
        -80
    e ../lots/NOTE/pari-gp/pari-gp-bug/qfbprimeform-bug.txt

py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7CRT_ =-71 +verbose
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   ,iter_ABCs6Qfb5neg_discriminant__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_ =-71
    (1, 1, 18)
    (2, 1, 9)
    (2, -1, 9)
    (3, 1, 6)
    (3, -1, 6)
    (4, 3, 5)
    (4, -3, 5)
py_adhoc_call   seed.math.factor_pint.perfect_power.lift_neg_kth_root_mod_coprime_power_   @sqrt_mod_coprime_power_  =2 =2+3 =-199 =1
    21
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7CRT_ =-199 +verbose
<<==:
#主要命令牜数据校验牜群规模纟平方根纟负数纟四倍数牜前两万个牜花哨版:here
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   ,iter_class_numbers5neg_discriminants__7brute_force7count_primitive_binary_quadratic_forms7ratio7CRT_ =20000 +with_D +both7nonprimitive  +to_mul_four --_path4validate:'../../python3_src/nn_ns/math_nn/numbers/b000003-class_number_of_the_quadratic_order_of_discriminant_(-4n)__fst_20000.txt' --_regex8selector4line4path:'\d+ (?P<num_BQFs7primitive>\d+)'
    ... ...
    (-79988, (150, 150))
    (-79992, (104, 156))
    (-79996, (52, 104))
    (-80000, (120, 259))
    ok!
    ##############################
    ##############################
    #fixed bugs:
    Exception: ('validate fail@_path4validate', (-12, (0, 0)), '3 1', 0, '1')
        fix_bug_6neg4Deq3:goto
    Exception: ('validate fail@_path4validate', (-20, (3, 3)), '5 2', 3, '2')
        fix_bug_6neg4Deq20:goto
    ValueError@[D==Df==-52]
        sqrt_of_odd_mod_zpow_:『if not y&3 == 1:raise ValueError』
        fix_bug_6neg4Deq52:goto
    AssertionError@[D==-60][Df==-15]
        fix_bug_6neg4Deq15:goto
    Exception: ('validate fail@_path4validate', (-60, (3, 6)), '15 2', 3, '2')
        fix_bug_6neg4Deq15__another:goto
    ValueError@[D==-76][Df==-19]
        sqrt_of_odd_mod_zpow_:『if not y&7 == 1:raise ValueError』
        fix_bug_6neg4Deq19:goto
    Exception: ('validate fail@_path4validate', (-84, (5, 5)), '21 4', 5, '4')
        fix_bug_6neg4Deq84:goto
    Exception: ('validate fail@_path4validate', (-284, (9, 18)), '71 7', 9, '7')
        fix_bug_6neg4Deq71:goto
    AssertionError@[D==-796][Df==-199]
        fix_bug_6neg4Deq199:goto
===
view ../../python3_src/nn_ns/math_nn/numbers/b000924-class_number_of_QQ(sqrt(n_th_neg_squarefree))__fst_10000.txt
    ... ...
    9993 20
    9994 60
    9995 38
    9996 156
    9997 112
    9998 146
    9999 112
    10000 100

#主要命令牜数据校验牜群规模纟平方根纟负数纟无平方因子牜前一万个牜花哨版:here
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   ,iter_class_numbers5neg_discriminants__7brute_force7count_primitive_binary_quadratic_forms7ratio7CRT_ =10000 +with_D +both7nonprimitive  --case6num_Ds:squarefree_radicand_only -to_mul_four --_path4validate:'../../python3_src/nn_ns/math_nn/numbers/b000924-class_number_of_QQ(sqrt(n_th_neg_squarefree))__fst_10000.txt' --_regex8selector4line4path:'\d+ (?P<num_BQFs7primitive>\d+)'
    ... ...
    (-65720, (104, 104))
    (-16431, (114, 114))
    (-65732, (104, 104))
    (-16435, (20, 20))
    (-65748, (60, 60))
    (-65752, (38, 38))
    (-16439, (156, 156))
    (-65764, (112, 112))
    (-65768, (146, 146))
    (-65780, (112, 112))
    (-65784, (100, 100))
    ok!
        # 1th..=10000th squarefree radicand
===
]]
[[
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7sum_over_Df_ =-12
    ValueError: (-12, {2: 2, 3: 1})
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7sum_over_Df_ =-12 +_not_fundamental_ok
    seed.math.floor_ceil_tools.fc_perfect.NotPerfectError__div
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7sum_over_Df_ =-3
    1
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   @class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7sum_over_Df_ =-199
    9
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   ,iter_class_numbers5neg_discriminants__7brute_force7count_primitive_binary_quadratic_forms7ratio7sum_over_Df_ =10000 +with_D +both7nonprimitive  --case6num_Ds:squarefree_radicand_only -to_mul_four --_path4validate:'../../python3_src/nn_ns/math_nn/numbers/b000924-class_number_of_QQ(sqrt(n_th_neg_squarefree))__fst_10000.txt' --_regex8selector4line4path:'\d+ (?P<num_BQFs7primitive>\d+)'
    ... ...
    (-6159, (80, 80))
    ... ...
    (-34212, (76, 76))
    (-34216, (64, 64))
    (-8555, (32, 32))
    (-34228, (40, 40))
    ... ...
    (-42820, (48, 48))
    (-42824, (140, 140))
    (-10707, (12, 12))
    (-42836, (190, 190))
    (-10711, (65, 65))
    (-42852, (60, 60))
    ^C KeyboardInterrupt
        #slow...
        @6514 -10713 -42852 60
]]
[[
+squarefree_radicand_only6num_Ds --> --case6num_Ds:squarefree_radicand_only
++case6num_Ds:negative_fundamental_discriminant
++case6num_Ds:negative_discriminant

===
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   ,iter_class_numbers5neg_discriminants__7brute_force7count_primitive_binary_quadratic_forms7ratio7sum_over_Df_ =1000 +with_D  --case6num_Ds:negative_fundamental_discriminant | head
    (-3, 1)
    (-4, 1)
    (-7, 1)
    (-8, 1)
    (-11, 1)
    (-15, 2)
    (-19, 1)
    (-20, 2)
    (-23, 3)
    (-24, 2)
    Exception ignored in: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
    BrokenPipeError: [Errno 32] Broken pipe
===
py_adhoc_call  seed.math.BinaryQuadraticForm__7class_number   ,iter_class_numbers5neg_discriminants__7brute_force7count_primitive_binary_quadratic_forms7ratio7sum_over_Df_ =10 +with_D  --case6num_Ds:negative_discriminant
    (-3, 1)
    (-4, 1)
    (-7, 1)
    (-8, 1)
    (-11, 1)
    (-12, 1)
    (-15, 2)
    (-16, 1)
    (-19, 1)
    (-20, 2)

]]



end__py_adhoc_call:here
]]]'''#'''
#SECTION
r'''[[[
#TODO:h(D):排除[1==gcd(A,B,C)]; 增加[C==A>0>B>-A]，最后 计算 [C==A...]

[is_negative_fundamental_discriminant_(Df)]
[D == Df*rtm**2]
[h(D) == h(Df)*ratio4class_number7Duu_(Df,rtm)]
or:
[h(D) == h({[D==B**2-4*A*C][1==gcd(A,B,C)][[C==A>=B>=0]or[C>A>=B>-A]]};D)]
[h({[D==B**2-4*A*C][1==gcd(A,B,C)][[C==A>=B>=0]or[C>A>=B>-A]]};D) == h({[D==B**2-4*A*C][[C==A>=B>=0]or[C>A>=B>-A]]};D)*ratio4class_number7Duu_(Df,rtm)/ratio4pseudo_class_number7Duu_(Df,rtm)]
[h({[D==B**2-4*A*C][[C==A>=B>=0]or[C>A>=B>-A]]};D) == h({[D==B**2-4*A*C][C>=A>=B>-A]};D) -h({[D==B**2-4*A*C][C==A>0>B>-A]};D)]
[h({[D==B**2-4*A*C][C==A>0>B>-A]};D) == h({[D==B**2-4*A*C][C==A>B>0]};D) == h({[D==(B-2*A)*(B+2*A)][A>B>0]};D)]
==>>:
[h(D) == ratio4class_number7Duu_(Df,rtm)/ratio4pseudo_class_number7Duu_(Df,rtm)  *(h({[D==B**2-4*A*C][C>=A>=B>-A]};D) -h({[D==(B-2*A)*(B+2*A)][A>B>0]};D))]

[slack_min4A7noncoprime_ok{D} := 1]
    !! [4*A*C == B**2+(-D) > 0]
    !! [C>=A>=0]
    => [A > 0]
[slack_max4A7noncoprime_ok{D} := floor_sqrt((-D)//3)]
    !! [-D == 4*A*C-B**2 >= 4*A*A-A**2 == 3*A**2]
    => [A <= sqrt(-D/3)]

[slack_max4abs4B7noncoprime_ok{D} := floor_sqrt((-D)//3)]
    !! [abs(B) <= A <= slack_max4A7noncoprime_ok{D} == floor_sqrt((-D)//3)]
[slack_max4abs4B6A7noncoprime_ok{D,A} := A]
    !! [abs(B) <= A]
[slack_min4abs4B6A7noncoprime_ok{D,A} := ceil_sqrt(max(0,4*A**2-(-D)))]
    !! [B**2 == 4*A*C-(-D) >= 4*A*A-(-D)]
    => [abs(B) >= sqrt(max(0,4*A**2-(-D)))]

[1 <= A < slack_min4abs4B6A7noncoprime_ok{D,A}]:
    <==> [A**2 < (4*A**2-(-D))]
    <==> [3*A**2 > (-D)]
    <==> [A > sqrt((-D)/3)]
    <==> [A > slack_max4A7noncoprime_ok{D}]
[[slack_max4A7noncoprime_ok{D}>=A>=1] -> [A >= slack_min4abs4B6A7noncoprime_ok{D,A}]]
    # 定理牜枚举二次型牜无需互素牜首部受限则首部自动大于等于丮保证尾部大于等于首部的下界纟绝对值纟中部厈:here

[without:[C>=A][C>=B][C>=0]][D==B**2-4*A*C][D < 0][A > 0][abs(B) <= A <= slack_max4A7noncoprime_ok{D}]:
    [C < abs(B)]:
        [B**2+(-D)
        !! [D==B**2-4*A*C]
        == 4*A*C
        !! [A > 0]
        !! [C < abs(B)]
        < 4*A*abs(B)
        !! [A <= slack_max4A7noncoprime_ok{D}]
        <= 4*slack_max4A7noncoprime_ok{D}*abs(B)
        <= 4*sqrt((-D)/3)*abs(B)
        ]
        [abs(B)**2 -4*sqrt((-D)/3)*abs(B) +(-D) < 0]
        [(-4*sqrt((-D)/3))**2 -4*(-D) == 4/3*(-D) > 0]
        [[abs(B) > (4*sqrt((-D)/3) -sqrt(4/3*(-D)))/2 == sqrt((-D)/3)][abs(B) < (4*sqrt((-D)/3) +sqrt(4/3*(-D)))/2 == sqrt((-D)*3)]]
        [sqrt((-D)/3) < abs(B) < sqrt((-D)*3)]
        !! [abs(B) <= slack_max4A7noncoprime_ok{D}]
        [abs(B) <= sqrt((-D)/3)]
        !! [sqrt((-D)/3) < abs(B)]
        _L
    [C >= abs(B)]
[[without:[C>=A][C>=B][C>=0]][D==B**2-4*A*C][D < 0][A > 0][abs(B) <= A <= slack_max4A7noncoprime_ok{D}] -> [C >= abs(B)]]
    # 自动成立:[C >= abs(B)]
    # 定理牜枚举二次型牜无需互素牜首部中部受限则尾部自动大于等于绝对值纟中部:here


[slack_min4C7noncoprime_ok{D} := ceil_sqrt((-D)/4)]
    !! [-D == 4*A*C-B**2 <= 4*C*C-0**2 == 4*C**2]
    => [C >= sqrt(-D)/2]
[slack_max4C7noncoprime_ok{D} := ((-D+1)//4)]
    !! [C == (-D+B**2)/(4*A) <= (-D+A**2)/(4*A) == ((-D)/A +A)/4]
        # 最大值@[A <- {1,slack_max4A7noncoprime_ok{D}}]
        # !! 最小值@[A == sqrt(D) > slack_max4A7noncoprime_ok{D}]
        # => 最大值@[A == 1]
    => [C <= (-D+1)/4]
        # [[0>D>-15] -> [qfbclassno(D) == 1]]
        # [[0>D>-23] -> [qfbclassno(D) == 1+[D==-15]+[D==-20]]]
        # [qfbclassno(-15) == 2] # Qfb(1,1,4),Qfb(2,1,2)
        # [qfbclassno(-20) == 2] # Qfb(1,0,5),Qfb(2,2,3)

[slack_min4C7noncoprime_ok{D} < slack_min4abs4B6A7noncoprime_ok{D,A}]:
    <==> [ceil_sqrt((-D)/4) < ceil_sqrt(max(0,4*A**2-(-D)))]
    ==>>:
    [sqrt((-D)/4) < sqrt(max(0,4*A**2-(-D)))]
    [(-D)/4 < 4*A**2-(-D)]
    [5*(-D) < 16*A**2]
    [A > sqrt((-D)*5/16)]
    !! [sqrt((-D)/3) > sqrt((-D)*5/16)]
    确实有可能
    #无用

[slack_min4C7noncoprime_ok{D} <= slack_max4A7noncoprime_ok{D}]
[slack_min4C7noncoprime_ok{D} < slack_max4A7noncoprime_ok{D}]:
    <<== [ceil_sqrt((-D)/4) < floor_sqrt((-D)//3)]
    <<== [2+sqrt((-D)/4) <= sqrt((-D)/3)]
    <<== [4 +4*sqrt((-D)/4) +((-D)/4) <= ((-D)/3)]
    <<== [4 +2*sqrt(-D) <= ((-D)/12)]
    <<== [sqrt(-D)**2 -24*sqrt(-D) -48 >= 0]

    <<== [(sqrt(-D)-(12-8*sqrt(3)))*(sqrt(-D)-(12+8*sqrt(3))) >= 0]
    <<== [sqrt(-D) >= (12+8*sqrt(3)) == 2*sqrt(3)*(2*sqrt(3)+4) == 2*sqrt(3)*(1+sqrt(3))**2]
    <<== [(-D) >= 12*(1+sqrt(3))**4 ~= 668.55375505322444035726969756912749445]
    <<== [(-D) >= 669]

!! MAYBE:[slack_min4C7noncoprime_ok{D} < slack_max4A7noncoprime_ok{D}]
=> MAYBE:[tight_min4C7noncoprime_ok{D} < tight_max4A7noncoprime_ok{D}]

[h({[D==B**2-4*A*C][C>=A>=B>-A]};D)
== h({[D==B**2-4*A*C][min(C,slack_max4A7noncoprime_ok{D})>=A>=B>-A]};D)
!! 定理牜枚举二次型牜无需互素牜首部中部受限则尾部自动大于等于绝对值纟中部
== h({[D==B**2-4*A*C][slack_max4A7noncoprime_ok{D}>=A>=B>-A]};D)
    -h({[D==B**2-4*A*C][slack_max4A7noncoprime_ok{D}>=A>C>=abs(B)]};D)
        # == -h({[D==B**2-4*A*C][slack_max4A7noncoprime_ok{D}>=A>C>=B>=-C]};D)
        #   『B>=-C』
]
[h({[D==B**2-4*A*C][slack_max4A7noncoprime_ok{D}>=A>C>=abs(B)]};D)
== h({[D==B**2-4*A*C][slack_max4A7noncoprime_ok{D}>=C>A>=abs(B)]};D)
        #   『B>=-A』not『B>-A』
]
[h({[D==B**2-4*A*C][slack_max4A7noncoprime_ok{D}>=A>C>=abs(B)]};D)
== h({[D==B**2-4*A*C][slack_max4A7noncoprime_ok{D}>=A>=1][min(A,slack_min4abs4B6A7noncoprime_ok{D,A}) > abs(B)]};D)
!! [[slack_max4A7noncoprime_ok{D}>=A>=1] -> [A >= slack_min4abs4B6A7noncoprime_ok{D,A}]] # 定理牜枚举二次型牜无需互素牜首部受限则首部自动大于等于丮保证尾部大于等于首部的下界纟绝对值纟中部厈:goto
== h({[D==B**2-4*A*C][slack_max4A7noncoprime_ok{D}>=A>=slack_min4C7noncoprime_ok{D}][slack_min4abs4B6A7noncoprime_ok{D,A} > abs(B)]};D)
]
==>>:
[h({[D==B**2-4*A*C][C>=A>=B>-A]};D) == h({[D==B**2-4*A*C][slack_max4A7noncoprime_ok{D}>=A>=B>-A]};D) -h({[D==B**2-4*A*C][slack_max4A7noncoprime_ok{D}>=A>=slack_min4C7noncoprime_ok{D}][slack_min4abs4B6A7noncoprime_ok{D,A} > abs(B)]};D)]

!! [h(D) == ratio4class_number7Duu_(Df,rtm)/ratio4pseudo_class_number7Duu_(Df,rtm)  *(h({[D==B**2-4*A*C][C>=A>=B>-A]};D) -h({[D==(B-2*A)*(B+2*A)][A>B>0]};D))]
[h(D) == ratio4class_number7Duu_(Df,rtm)/ratio4pseudo_class_number7Duu_(Df,rtm)  *(h({[D==B**2-4*A*C][slack_max4A7noncoprime_ok{D}>=A>=B>-A]};D) -h({[D==B**2-4*A*C][slack_max4A7noncoprime_ok{D}>=A>=slack_min4C7noncoprime_ok{D}][slack_min4abs4B6A7noncoprime_ok{D,A} > abs(B)]};D) -h({[D==(B-2*A)*(B+2*A)][A>B>0]};D))]

==>>:
h(D)
    --> ???*h(Df) or ???*(h({[D==B**2-4*A*C][slack_max4A7noncoprime_ok{D}>=A>=B>-A]};D) -h({[D==B**2-4*A*C][slack_max4A7noncoprime_ok{D}>=A>=slack_min4C7noncoprime_ok{D}][slack_min4abs4B6A7noncoprime_ok{D,A} > abs(B)]};D) -h({[D==(B-2*A)*(B+2*A)][A>B>0]};D))
        # 自动成立:[A >= slack_min4abs4B6A7noncoprime_ok{D,A}]
    --> ???*(h({[Df==B**2-4*A*C][slack_max4A7noncoprime_ok{Df}>=A>=B>-A]};Df) -h({[Df==B**2-4*A*C][slack_max4A7noncoprime_ok{Df}>=A>=slack_min4C7noncoprime_ok{Df}][slack_min4abs4B6A7noncoprime_ok{Df,A} > abs(B)]};Df) -h({[Df==(B-2*A)*(B+2*A)][A>B>0]};Df))
        # 自动成立:Df => [1==gcd(A,B,C)]
        #   但是 [C>=A] 无法自动成立
[h({[Df==(B-2*A)*(B+2*A)][A>B>0]};Df) == h({[-Df==(2*A-B)*(2*A+B)][A>B>0][gcd((2*A-B),(2*A+B)) == 1+[Df%4==0]]};Df)]
TODO

#]]]'''#'''
#SECTION
r'''[[[
[[
Qfb:蛮力枚举列出class_group{D}所有等价类
CRT_le(max;moduli,remainders)
view ../../python3_src/seed/math/BinaryQuadraticForm__7class_number.py
#群规模计算牜蛮力枚举:here
    #三种解形态:简化版:goto
    #重要约束纟幂次:简化版:goto
    #bug:降级纟解结构:goto
[C >= A >= max(1,abs(B))][gcd(A,B,C) == 1]:
    [D==B**2-4*A*C <= A**2-4*A**2 == -3*A**2]
    [-D >= 3*A**2]
    [1 <= A <= sqrt(-D/3)]

    !! [gcd(A,B,C) == 1]
    [(-D + [D==-3]) > 3*A**2]
    [3*A**2 <= (-1-D + [D==-3])]
    [3*A**2 <= (-D -[D=!=-3])]

    [1 <= A < sqrt((-D + [D==-3])/3)]
    [max4A := floor_sqrt((-D -[D=!=-3])/3)]
    [1 <= A < max(2,sqrt((-D)/3))]
    蛮力枚举 素因子{A{D}}
        [D =[%(4*A*C)]= B**2]
        [D =[%(4*A)]= B**2]
        [Jacobi_symbol(素因子{4*A{D}};D) == +1|0]

    [B**2 == D+4*A*C >= D+4*A**2]
    [abs(B) >= sqrt(max(0,D+4*A**2))]
    [min4abs4B := sqrt(max(0,D+4*A**2))]
    [A >= abs(B) >= sqrt(max(0,D+4*A**2))]
    蛮力枚举 B{D,A{D}}
        sqrts_mod_(2*A; D)
        howto:CRT_le(max;moduli,remainders)
    xxx:solve:[B**2 =[%(2*A)]= D][0 <= B <= A]
    xxx:solve:[B**2 =[%(2*A)]= D][[min4abs4B <= B <= 2*A-max(1,min4abs4B)]]
    solve:[(B%(2*A)) :=> [B**2 =[%(4*A)]= D][min4abs4B <= B <= 2*A-max(1,min4abs4B)][1==gcd(A,B,(-D+B**2)///(4*A))]]
        !! 二幂模开平方耂特色冫最高爻位任意:%(4*A) --> %(2*A)
        !! primitive
        很麻烦，改为:
            pseudo_class_number7not_necessary_primitive:goto
            is_negative_fundamental_discriminant_:goto
            群规模公式牜负判别值牜不完全去平方因子化牜须留底:goto
            群规模计算牜蛮力牜先缩放牜拆分成泛子型牜参数互素:goto
    [p:=2][A%p =!= 0]:
        bug{有不少失误}:eg:『solve:...』
        !! [B**2 =[%(2*A)]= D]
        [B**2 =[%2]= D]
        [B =[%2]= D]
        [B =[%p]= D]
    [p::prime][A%p == 0]:
        [e4p4A := gde_(p;A)]
        [e4p4B := gde_(p;B)]
        [e4p4D := gde_(p;D)]

        [e4p4two := [p==2]*1]
        [two9pw := (2///p**e4p4two)]
        solve:[B**2 =[%(2*A)]= D]
            --> solve:[B**2 =[%(2*p**e4p4A)]= D]
            --> solve:[B**2 =[%(two9pw*p**(e4p4two+e4p4A))]= D]
            --> solve:[B**2 =[%two9pw]= D] and [B**2 =[%p**(e4p4two+e4p4A)]= D]

        !! [A%p == 0]
        [e4p4A > 0]

        !! [B**2 =[%(2*A)]= D]
        [B**2 =[%A]= D]
        [B**2 =[%p]= D]
        [Jacobi_symbol(p;B) <- {0,+1}]
        * [Jacobi_symbol(p;B) == +1]:
            [B%p =!= 0]
            [D%p =!= 0]
            [e4p4B == 0]
            [e4p4D == 0]

            * [p>2]:
                [(B%p) has 2 solution]
                [(B%p**e4p4A) has 2 solution]
            * [p==2]:
                * [e4p4A==1]:
                    [(B%p**(1+e4p4A)) has 2 solution]
                * [e4p4A>1]:
                    [(B%p**(1+e4p4A)) has 4 solution]
        * [Jacobi_symbol(p;B) == 0]:
            [B%p == 0]
            [D%p == 0]
            [e4p4B > 0]
            [e4p4D > 0]
            [gcd(A,B)%p == 0]

            !! primitive
            [1 == gcd(A,B,C)]
            !! [gcd(A,B)%p == 0]
            [C%p =!= 0]
            [gde_(p;4*A*C) == gde_(p;4*A) == gde_(p;4) + gde_(p;A) == [p==2]*2 + e4p4A]
            [e4p4four := [p==2]*2]
            [gde_(p;4*A*C) == e4p4four + e4p4A]
            * [e4p4four + e4p4A > e4p4D]:
                [e4p4two + e4p4A >= e4p4D]
                !! [B**2 =[%p**(e4p4four+e4p4A)]= D]
                !! [e4p4four + e4p4A > e4p4D]
                [2*e4p4B == e4p4D < (e4p4four+e4p4A)]
                [e4p4D%2 == 0]
                !! [e4p4A > 0]
                [e4p4B == e4p4D///2 < (e4p4four+e4p4A)/2 == (e4p4two+e4p4A/2) < (e4p4two+e4p4A)]
                [e4p4B == e4p4D///2 < (e4p4two+e4p4A)]

                [D9pw:=(D///p**e4p4D)]
                [B9pw:=(B///p**e4p4B)]
                [A9pw:=(A///p**e4p4A)]
                [four9pw:=(4///p**e4p4four)]
                [D9pw == B9pw**2 -C*four9pw*A9pw*p**(e4p4four+e4p4A -e4p4D)]
                !! [e4p4four + e4p4A > e4p4D]
                [B9pw**2 =[%p**(e4p4four+e4p4A-e4p4D)]= D9pw]
                !! [e4p4two + e4p4A >= e4p4D]
                [B9pw**2 =[%p**(e4p4two+e4p4A-e4p4D)]= D9pw]

                solve:[B**2 =[%p**(e4p4two+e4p4A)]= D]
                    --> solve:[B9pw**2 =[%p**(e4p4two+e4p4A-e4p4D)]= D9pw]
                [ft4B:=p**(e4p4D///2)]
                [B%p**(e4p4two+e4p4A) solution is ft4B*((B9pw%p**(e4p4two+e4p4A-e4p4D)) + p**(e4p4two+e4p4A-e4p4D)*(all_uints%ft4B))]
            * [e4p4four + e4p4A <= e4p4D]:
                [e4p4two + e4p4A <= e4p4D]

                !! [B**2 =[%p**(e4p4four+e4p4A)]= D]
                !! [e4p4four + e4p4A <= e4p4D]
                [B**2 =[%p**(e4p4four+e4p4A)]= 0]
                [2*e4p4B >= (e4p4four+e4p4A)]
                !! [D==(B**2-4*A*C)]
                [min(e4p4D, 2*e4p4B) <= (e4p4four+e4p4A)]
                !! [2*e4p4B >= (e4p4four+e4p4A)]
                !! [e4p4four + e4p4A <= e4p4D]
                [min(e4p4D, 2*e4p4B) >= (e4p4four+e4p4A)]
                !! [min(e4p4D, 2*e4p4B) <= (e4p4four+e4p4A)]
                [min(e4p4D, 2*e4p4B) == (e4p4four+e4p4A)]
                [[e4p4D == (e4p4four+e4p4A) <= 2*e4p4B]or[e4p4D > (e4p4four+e4p4A) == 2*e4p4B]]

                !! [2*e4p4B >= (e4p4four+e4p4A)]
                [e4p4B >= (e4p4four/2+e4p4A/2) == (e4p4two+e4p4A/2)]
                [e4p4B >= (e4p4two+ceil(e4p4A/2))]
                !! [e4p4A > 0]
                [e4p4A > (e4p4A/2)]
                [e4p4A >= ceil(e4p4A/2)]
                [e4p4two+e4p4A >= (e4p4two+ceil(e4p4A/2))]
                [(e4p4A-ceil(e4p4A/2)) >= 0]

                !! [[e4p4D == (e4p4four+e4p4A) <= 2*e4p4B]or[e4p4D > (e4p4four+e4p4A) == 2*e4p4B]]
                * [e4p4D == (e4p4four+e4p4A) <= 2*e4p4B]:
                    !! [e4p4B >= (e4p4two+ceil(e4p4A/2))]
                    solve:[B**2 =[%p**(e4p4two+e4p4A)]= D]
                    [ft4B:=p**(e4p4two+ceil(e4p4A/2))]
                    [B%p**(e4p4two+e4p4A) solution is ft4B*(all_uints%p**(e4p4A-ceil(e4p4A/2)))]
                    [ft4B:=p**(e4p4two+e4p4A-(e4p4A//2))]
                    [B%p**(e4p4two+e4p4A) solution is ft4B*(all_uints%p**floor(e4p4A/2))]

                * [e4p4D > (e4p4four+e4p4A) == 2*e4p4B]:
                    [e4p4A%2 == 0]
                    !! [e4p4B >= (e4p4two+ceil(e4p4A/2))]
                    [e4p4B == (e4p4two+(e4p4A///2))]
                    solve:[B**2 =[%p**(e4p4two+e4p4A)]= D]
                    [ft4B:=p**(e4p4two+(e4p4A///2))]
                    [B%p**(e4p4two+e4p4A) solution is ft4B*(all_coprimes%p**(e4p4A///2))]
            ==>>:
            #三类:见下面:简化版
            solve:[B**2 =[%p**(e4p4two+e4p4A)]= D]
            * [e4p4four+e4p4A > e4p4D == 2*e4p4B]:
                [D9pw:=(D///p**e4p4D)]
                [B9pw:=(B///p**e4p4B)]
                --> solve:[B9pw**2 =[%p**(e4p4two+e4p4A-e4p4D)]= D9pw]
                [ft4B:=p**(e4p4D///2)]
                [B%p**(e4p4two+e4p4A) solution is ft4B*((B9pw%p**(e4p4two+e4p4A-e4p4D)) + p**(e4p4two+e4p4A-e4p4D)*(all_uints%ft4B))]

            * [e4p4D == (e4p4four+e4p4A) <= 2*e4p4B]:
                [ft4B:=p**(e4p4two+e4p4A-(e4p4A//2))]
                [B%p**(e4p4two+e4p4A) solution is ft4B*(all_uints%p**floor(e4p4A/2))]

            * [e4p4D > (e4p4four+e4p4A) == 2*e4p4B]:
                [ft4B:=p**(e4p4two+(e4p4A///2))]
                [B%p**(e4p4two+e4p4A) solution is ft4B*(all_coprimes%p**(e4p4A///2))]
                    #NOTE:all_coprimes vs all_uints

            #重要约束:见下面:简化版
            [[e4p4four+e4p4A < e4p4D] -> [e4p4A%2 == 0]]
            [[e4p4four+e4p4A > e4p4D] -> [e4p4D%2 == 0]]
                # <==> [[e4p4D%2 == 1] -> [e4p4four+e4p4A <= e4p4D]]
    ==>>:
    [p::prime][A%p == 0][D%p == 0]:
        # 简化版
        [e4p4A := gde_(p;A)]
        [e4p4B := gde_(p;B)]
        [e4p4D := gde_(p;D)]

        [e4p4ZZA := gde_(p;4*A)]
        [e4p4ZA := gde_(p;2*A)]
        [e4p4A <= e4p4ZA <= e4p4ZZA]

        [D9pw:=(D///p**e4p4D)]
        [B9pw:=(B///p**e4p4B)]
        ==>>:
        #三种解形态:简化版:here
        solve:[B**2 =[%p**e4p4ZA]= D]
        * [e4p4ZZA > e4p4D == 2*e4p4B]:
            --> solve:[B9pw**2 =[%p**(e4p4ZA-e4p4D)]= D9pw]
            [ft4B:=p**(e4p4D///2)]
            [B%p**e4p4ZA solution is ft4B*((B9pw%p**(e4p4ZA-e4p4D)) + p**(e4p4ZA-e4p4D)*(all_uints%ft4B))]

        * [e4p4D == e4p4ZZA <= 2*e4p4B]:
            [ft4B:=p**(e4p4two+e4p4A-(e4p4A//2))]
            [B%p**e4p4ZA solution is ft4B*(all_uints%p**floor(e4p4A/2))]

        * [e4p4D > e4p4ZZA == 2*e4p4B]:
            [ft4B:=p**(e4p4two+(e4p4A///2))]
            [B%p**e4p4ZA solution is ft4B*(all_coprimes%p**(e4p4A///2))]
                #NOTE:all_coprimes vs all_uints

        #重要约束纟幂次:简化版:here
        [[e4p4ZZA < e4p4D] -> [e4p4A%2 == 0]]
        [[e4p4ZZA > e4p4D] -> [e4p4D%2 == 0]]
            # <==> [[e4p4D%2 == 1] -> [e4p4ZZA <= e4p4D]]

        solve:[B**2 =[%(2*A)]= D][[min4abs4B <= B <= 2*A-max(1,min4abs4B)]]
            #bug:降级纟解结构:here
            bug{missing:all_coprimes}:解形态: ft4B*(B9pw%M0 + M0*(all_uints%M2)) where [ft4B*M0*M2 == modulus7old]
                #########:尝试一:
                ...尝试兼容:all_uints,all_coprimes --> all_coprimes9ps{ps}%M2 # ps are partial prime factors of M2
                解形态: ft4B*(B9pw%M0 + M0*(all_coprimes9ps{ps}%M2)) where [ft4B*M0*M2 == modulus7old]
                不太行:???最后修正:[min4abs4B..=max]排除ps
                #########:尝试二:
                not_necessary_primitive
                    pseudo_class_number7not_necessary_primitive:goto
                #########:尝试三:
                发现对称性:[1 <= A <= max4A][-A < B <= A] => [C >= abs(B)][C <?> A]
                => [h(D)==(sum[num_Bs6ZA{A} | [1 <= A <= max4A{D}]] -sum[num_Bs6ZA{A} | [1 <= A <= max4A{D}][A==C]])///2 +h7CeqA(D)]
                #########:尝试四:
                先枚举B，再枚举(A,C)
                #########
            ft4B => [modulus7new := modulus7old///ft4B][min4abs4B7new := ceil(min4abs4B7old/ft4B)][max4abs4B7new := (max4abs4B7old//ft4B)][num_Bs7old := num_Bs7new]
            (all_uints%M) => [modulus7new := modulus7old///M][(qa,ra):=(min4abs4B7old/%M)][(qb,rb):=(max4abs4B7old/%M)]:
                [qa <= qb]
                [num_whole_wheel := qb-qa]
                * [qa == qb]:
                    <==> [num_whole_wheel == 0]
                    [min4abs4B7new := ra]
                    [max4abs4B7new := rb]
                    [num_Bs7old := num_Bs7new]
                * [qa < qb]:
                    <==> [num_whole_wheel > 0]
                    * [rb+1 <= ra-1]:
                        [min4abs4B7new := rb+1]
                        [max4abs4B7new := ra-1]
                        [num_Bs7old := (-num_Bs7new) + total_Bs7new7unbound*num_whole_wheel]
                            #exclude num_Bs7new
                    * [rb+1 > ra-1]:
                        [ra <= rb+1]
                        * [ra <= rb]:
                            [min4abs4B7new := ra]
                            [max4abs4B7new := rb]
                        * [ra == rb+1]:
                            [num_Bs7new := 0]
                        [num_Bs7old := (+num_Bs7new) + total_Bs7new7unbound*num_whole_wheel]
                            #include num_Bs7new


    ###########################
    只考虑[is_squarefree_(gcd(A,D))][k*A <= C]
        %s/class_number7nonprimitive/pseudo_class_number7not_necessary_primitive/g
    ###########################
    [class_number{D} == len{Qfb(A,B,C) | [[A,B,C::int][D==B**2-4*A*C][[C==A>=B>=0]or[C>A>=B>-A]][1==gcd(A,B,C)]]}]
    [pseudo_class_number7not_necessary_primitive{D} == len{Qfb(A,B,C) | [[A,B,C::int][D==B**2-4*A*C][[C==A>=B>=0]or[C>A>=B>-A]]]}]

    [k::int{>0}]:
        [class_number7squarefree_gcdAD_{D,k} == len{Qfb(A,B,C) | [[A,B,C::int][is_squarefree_(gcd(D,A))][D==B**2-4*A*C][[C==k**2*A>=k*B>=0]or[C>k**2*A>=k*B>-k**2*A]][1==gcd(k**2*A,k*B,C)]]}]
        [pseudo_class_number7not_necessary_primitive7squarefree_gcdAD_{D,k} == len{Qfb(A,B,C) | [[A,B,C::int][is_squarefree_(gcd(D,A))][D==B**2-4*A*C][[C==k**2*A>=k*B>=0]or[C>k**2*A>=k*B>-k**2*A]]]}]

    [k,t::int{>0}][Dt::int{<0}][t*Dt%4 < 2]:
        # [D == t*Dt]
        [tclass_number7coprimeAD_{Dt,k,t} == len{Qfb(t*A,t*B,C) | [[A,B,C::int][is_squarefree_(t)][1==gcd(Dt,A)][t*Dt==(t*B)**2-4*(t*A)*C][Dt==t*B**2-4*A*C][[C==k**2*t*A>=k*t*B>=0]or[C>k**2*t*A>=k*t*B>-k**2*t*A]][1==gcd(A,t*B)][1==gcd(k**2*t*A,k*t*B,C)]]}]
            # 不可或缺的前提:[is_squarefree_(t)] => [B7big%t == 0]
            # NOTE: [Dt==t*B**2-4*A*C] # 『t*』 => 不同于 原型，称为 泛子型
            # => [1==gcd(A,t*B)]
            # => [t**-1*Dt =[%A]= B**2]
            # => [(B%A) <- sqrts_mod_(A;Dt*pow(t,-1,A))]
            #
            # !! [[C==k**2*t*A>=k*t*B>=0]or[C>k**2*t*A>=k*t*B>-k**2*t*A]]
            # [1==gcd(Dt,A)][[A==C/(k**2*t)][k*A>=B>=0]or[1<=A<C/(k**2*t)][k*A>=B>-k*A]]
            #   主要求(k*t*B%(2*k**2*t*A))
            #   即求(B%(2*k*A))
            #   虽然:[1==gcd(Dt,A)]但没有:[1=?=gcd(Dt,k)]
            #
            # !! [1==gcd(A,t*B)][1==gcd(k**2*t*A,k*t*B,C)]
            # [1==gcd(Dt,A)][1==gcd(A,t*B)][1==gcd(k*t,C)]
            # [gcd(Dt,t) == gcd(4,t)]
            # 不容易保证:[1==gcd(k*t,C)]
            #   => pseudo_class_number7not_necessary_primitive
            #   => tpseudo_class_number7not_necessary_primitive7coprimeAD_
        [tpseudo_class_number7not_necessary_primitive7coprimeAD_{Dt,k,t} == len{Qfb(t*A,t*B,C) | [[A,B,C::int][is_squarefree_(t)][1==gcd(Dt,A)][t*Dt==(t*B)**2-4*(t*A)*C][Dt==t*B**2-4*A*C][[C==k**2*t*A>=k*t*B>=0]or[C>k**2*t*A>=k*t*B>-k**2*t*A]][1==gcd(A,t*B)]]}]
            #泛子型:主要计算模块
            #注释:见上面:tclass_number7coprimeAD_
            # !! [1==gcd(Dt,A)]
            # !! [1==gcd(A,t*B)]
            # !! [Dt==t*B**2-4*A*C]
            # [gcd(Dt,t) == gcd(t*B**2-4*A*C,t) == gcd(4*A*C,t) == gcd(4*C,t)]
            # [gcd(Dt,t) == gcd(4*C,t)]

        ==>>:
        [class_number7squarefree_gcdAD_{D,k} == sum[tclass_number7coprimeAD_{D///t,k,t} | [t::int{>0}][is_squarefree_(t)][0 == D%t]]]
        [pseudo_class_number7not_necessary_primitive7squarefree_gcdAD_{D,k} == sum[tpseudo_class_number7not_necessary_primitive7coprimeAD_{D///t,k,t} | [t::int{>0}][is_squarefree_(t)][0 == D%t]]]

    [n::int{>0}]:
        [decompose_squarefree_part_ex_(n) =[def]= ?(k,t) :=> [k::int{>0}][t::int{>0}][n == k**2*t][is_squarefree_(t)]]

    [t::int{>0}][Dft::int{<0}][t*Dft%4 < 2][2 >= decompose_squarefree_part_ex_(t*Dft)[0]]:
        # [Df == t*Dft]
        # [k == 1]
        [tpseudo_class_number7not_necessary_primitive7CgtA7coprimeAD_{Dft,t} == len{Qfb(t*A,t*B,C) | [[A,B,C::int][is_squarefree_(t)][1==gcd(Dft,A)][t*Dft==(t*B)**2-4*(t*A)*C][Dft==t*B**2-4*A*C][C>t*A>=t*B>-t*A][1==gcd(A,t*B)]]}]
        [tpseudo_class_number7not_necessary_primitive7CeqA7coprimeAD_{Dft,t} == len{Qfb(t*A,t*B,C) | [[A,B,C::int][is_squarefree_(t)][1==gcd(Dft,A)][t*Dft==(t*B)**2-4*(t*A)*C][Dft==t*B**2-4*A*C][C==t*A>=t*B>=0][1==gcd(A,t*B)]]}]

        ==>>:
        [tpseudo_class_number7not_necessary_primitive7coprimeAD_{Dft,1,t} == tpseudo_class_number7not_necessary_primitive7CeqA7coprimeAD_{Dft,t} + tpseudo_class_number7not_necessary_primitive7CgtA7coprimeAD_{Dft,t}]

    [k::int{>0}]:
        [class_number7A_{D,k} == len{Qfb(A,B,C) | [[A,B,C::int][0 == gcd(D,A)%k**2][is_squarefree_(gcd(D,A)///k**2)][D==B**2-4*A*C][[C==A>=B>=0]or[C>A>=B>-A]][1==gcd(A,B,C)]]}]
        [pseudo_class_number7not_necessary_primitive7A_{D,k} == len{Qfb(A,B,C) | [[A,B,C::int][0 == gcd(D,A)%k**2][is_squarefree_(gcd(D,A)///k**2)][D==B**2-4*A*C][[C==A>=B>=0]or[C>A>=B>-A]]]}]
        [class_number7ABC_{D,k} == len{Qfb(A,B,C) | [[A,B,C::int][0 == D%k**2][2 > (D///k**2)%4][0 == gcd(A,C)%k][D==B**2-4*A*C][[C==A>=B>=0]or[C>A>=B>-A]][k==gcd(A,B,C)]]}]
        [pseudo_class_number7not_necessary_primitive7ABC_{D,k} == len{Qfb(A,B,C) | [[A,B,C::int][0 == D%k**2][2 > (D///k**2)%4][0 == gcd(A,C)%k][D==B**2-4*A*C][[C==A>=B>=0]or[C>A>=B>-A]][0==gcd(A,B,C)%k]]}]

        ==>>:
        [class_number7A_{D,k} == [0 == D%k**2][2 > (D///k**2)%4]*class_number7squarefree_gcdAD_{D///k**2,k}]
        [pseudo_class_number7not_necessary_primitive7A_{D,k} == [0 == D%k**2][2 > (D///k**2)%4]*pseudo_class_number7not_necessary_primitive7squarefree_gcdAD_{D///k**2,k}]

        bug:[class_number7ABC_{D,k} == [0 == D%k**2]*class_number{D///k**2}]
        [class_number7ABC_{D,k} == [0 == D%k**2][2 > (D///k**2)%4]*class_number{D///k**2}]
        [class_number7ABC_{D,1} == class_number{D}]
        bug:[pseudo_class_number7not_necessary_primitive7ABC_{D,k} == [0 == D%k**2]*pseudo_class_number7not_necessary_primitive{D///k**2}]
        [pseudo_class_number7not_necessary_primitive7ABC_{D,k} == [0 == D%k**2][2 > (D///k**2)%4]*pseudo_class_number7not_necessary_primitive{D///k**2}]
        [pseudo_class_number7not_necessary_primitive7ABC_{D,1} == pseudo_class_number7not_necessary_primitive{D}]

    ==>>:
    [pseudo_class_number7not_necessary_primitive{D} == sum[class_number7ABC_{D,k} | [k::int{>0}][0 == D%k**2][2 > (D///k**2)%4]]]
    !! [class_number7ABC_{D,k} == [0 == D%k**2][2 > (D///k**2)%4]*class_number{D///k**2}]
    [pseudo_class_number7not_necessary_primitive{D} == sum[class_number{D///k**2} | [k::int{>0}][0 == D%k**2][2 > (D///k**2)%4]]]


    [class_number{D} == sum[class_number7A_{D,k} | [k::int{>0}][0 == D%k**2][2 > (D///k**2)%4]]]
    !! [class_number7A_{D,k} == [0 == D%k**2][2 > (D///k**2)%4]*class_number7squarefree_gcdAD_{D///k**2,k}]
    [class_number{D} == sum[class_number7squarefree_gcdAD_{D///k**2,k} | [k::int{>0}][0 == D%k**2][2 > (D///k**2)%4]]]
    !! [class_number7squarefree_gcdAD_{D,k} == sum[tclass_number7coprimeAD_{D///t,k,t} | [t::int{>0}][is_squarefree_(t)][0 == D%t]]]
    [class_number{D} == sum[sum[tclass_number7coprimeAD_{D///k**2///t,k,t} | [t::int{>0}][is_squarefree_(t)][0 == D///k**2%t]] | [k::int{>0}][0 == D%k**2][2 > (D///k**2)%4]]]
    [class_number{D} == sum[tclass_number7coprimeAD_{D///(k**2*t),k,t} | [k::int{>0}][t::int{>0}][is_squarefree_(t)][0 == D%(k**2*t)][2 > (D///k**2)%4]]]
    [class_number{D} == sum[tclass_number7coprimeAD_{D///ft4D,k,t} | [ft4D::int{>0}][0 == D%ft4D][(k,t) := decompose_squarefree_part_ex_(ft4D)]]]
        # 群规模计算牜蛮力牜拆分成泛子型牜参数互素:here

    [pseudo_class_number7not_necessary_primitive{D} == sum[pseudo_class_number7not_necessary_primitive7A_{D,k} | [k::int{>0}][0 == D%k**2][2 > (D///k**2)%4]]]
    !! [pseudo_class_number7not_necessary_primitive7A_{D,k} == [0 == D%k**2][2 > (D///k**2)%4]*pseudo_class_number7not_necessary_primitive7squarefree_gcdAD_{D///k**2,k}]
    [pseudo_class_number7not_necessary_primitive{D} == sum[pseudo_class_number7not_necessary_primitive7squarefree_gcdAD_{D///k**2,k} | [k::int{>0}][0 == D%k**2][2 > (D///k**2)%4]]]
    !! [pseudo_class_number7not_necessary_primitive7squarefree_gcdAD_{D,k} == sum[tpseudo_class_number7not_necessary_primitive7coprimeAD_{D///t,k,t} | [t::int{>0}][is_squarefree_(t)][0 == D%t]]]
    [pseudo_class_number7not_necessary_primitive{D} == sum[sum[tpseudo_class_number7not_necessary_primitive7coprimeAD_{D///k**2///t,k,t} | [t::int{>0}][is_squarefree_(t)][0 == D///k**2%t]] | [k::int{>0}][0 == D%k**2][2 > (D///k**2)%4]]]
    [pseudo_class_number7not_necessary_primitive{D} == sum[tpseudo_class_number7not_necessary_primitive7coprimeAD_{D///(k**2*t),k,t} | [k::int{>0}][t::int{>0}][is_squarefree_(t)][0 == D%(k**2*t)][2 > (D///k**2)%4]]]
    [pseudo_class_number7not_necessary_primitive{D} == sum[tpseudo_class_number7not_necessary_primitive7coprimeAD_{D///ft4D,k,t} | [ft4D::int{>0}][0 == D%ft4D][(k,t) := decompose_squarefree_part_ex_(ft4D)]]]
        # 扩伪群规模计算牜蛮力牜拆分成泛子型牜参数互素:here
        #   bug{不是群}:就 分解整数牜探测群规模 而言，扩伪群规模 应该也可以...
        #   goto:fail:证明:[扩伪群规模%群规模 == 0]


    [rtm::uint{>0}][is_negative_fundamental_discriminant_(Df)]:
        !! [pseudo_class_number7not_necessary_primitive{D} == sum[class_number{D///k**2} | [k::int{>0}][0 == D%k**2][2 > (D///k**2)%4]]]
        #   rhs必含Df
        [pseudo_class_number7not_necessary_primitive{Df*rtm**2} == sum[class_number{Df*u**2} | [u::int{>0}][0 == rtm%u]]]
        !! [[u::uint{>0}] -> [h(D*u**2) == h(D)*ratio4class_number7Duu_(D,u)]] # 群规模公式牜负判别值牜完全去平方因子化牜无须留底:goto
        [pseudo_class_number7not_necessary_primitive{Df*rtm**2} == sum[class_number{Df}*ratio4class_number7Duu_(Df,u) | [u::int{>0}][0 == rtm%u]]]
        [pseudo_class_number7not_necessary_primitive{Df*rtm**2} %class_number{Df} == 0]
        [pseudo_class_number7not_necessary_primitive{Df*rtm**2}*w5D_(Df)/class_number{Df}
        == sum[w5D_(Df)*ratio4class_number7Duu_(Df,u) | [u::int{>0}][0 == rtm%u]]
        == (ratio4class_number7Duu_(Df,1)*w5D_(Df) -hratio4class_number7Duu_(Df,1)) +sum[hratio4class_number7Duu_(Df,u) | [u::int{>0}][0 == rtm%u]]
        == (w5D_(Df) -1) +sum[hratio4class_number7Duu_(Df,u) | [u::int{>0}][0 == rtm%u]]
        !! [hratio4class_number7Duu_(D,u) =[def]= (II[p**(-1+gde_(p;u))*(p-Kronecker_symbol(p;D)) | [p::prime][u%p==0]])]
        == (w5D_(Df) -1) +II[(1 + (p-Kronecker_symbol(p;Df))*sum[p**j | [j:<-[0..=-1+e4p]]]) | [p::prime][rtm%p==0][e4p:=gde_(p;rtm)]]
        == (w5D_(Df) -1 +II[(1 + (p-Kronecker_symbol(p;Df))*(-1+p**e4p)///(-1+p)) | [p::prime][rtm%p==0][e4p:=gde_(p;rtm)]])
        ]

        [hratio4pseudo_class_number7Duu_(Df,rtm) =[def]= II[(1 + (p-Kronecker_symbol(p;Df))*(-1+p**e4p)///(-1+p)) | [p::prime][rtm%p==0][e4p:=gde_(p;rtm)]]]

        [pseudo_class_number7not_necessary_primitive{Df*rtm**2}/class_number{Df}
        == (w5D_(Df) -1 +hratio4pseudo_class_number7Duu_(Df,rtm)) / w5D_(Df)
        !! [pseudo_class_number7not_necessary_primitive{D*rtm**2} %class_number{D} == 0]
        == (1 +(-1 +hratio4pseudo_class_number7Duu_(Df,rtm)) /// w5D_(Df))
        ]

        [ratio4pseudo_class_number7Duu_(Df,rtm) =[def]= (1 +(-1 +hratio4pseudo_class_number7Duu_(Df,rtm)) /// w5D_(Df))]
        [pseudo_class_number7not_necessary_primitive{Df*rtm**2} == class_number{Df}*ratio4pseudo_class_number7Duu_(Df,rtm)]
            #已证明:猜想推论冫扩伪群规模公式牜负判别值牜完全去平方因子化牜无须留底:here
            #扩伪群规模公式牜负判别值牜完全去平方因子化牜无须留底:here


        !! [[u::uint{>0}] -> [h(D*u**2) == h(D)*ratio4class_number7Duu_(D,u)]] # 群规模公式牜负判别值牜完全去平方因子化牜无须留底:goto
        [class_number{Df*rtm**2} == class_number{Df}*ratio4class_number7Duu_(Df,rtm)]
        !! [pseudo_class_number7not_necessary_primitive{Df*rtm**2} == class_number{Df}*ratio4pseudo_class_number7Duu_(Df,rtm)] #扩伪群规模公式牜负判别值牜完全去平方因子化牜无须留底:goto
        [pseudo_class_number7not_necessary_primitive{Df*rtm**2}*ratio4class_number7Duu_(Df,rtm) == class_number{Df*rtm**2}*ratio4pseudo_class_number7Duu_(Df,rtm)]
            # 已证明:猜想校验用定理牜扩伪群规模倍率:here
            # 定理牜扩伪群规模倍率:here
            #   已校验@(-4 .* range(1,1+20000))
            #       @_validate7both_()@view ../../python3_src/seed/math/BinaryQuadraticForm__7class_number.py


    #bug:[(rtm,_Df) := decompose_squarefree_part_ex_(D///4 if D%4==0 else D)][Df := 4*_Df if D%4==0 else _Df]:
        # !! see:[is_negative_fundamental_discriminant_(Df)]
    [(_rtm,_Df) := decompose_squarefree_part_ex_(D)][(rtm,Df) := (_rtm,_Df) if _Df%4 < 2 else (_rtm///2,4*_Df)]:
        # Df : negative fundamental discriminant
        # rtm : max sqrt
        [D == rtm**2*Df]

        !! [[u>=2][D%u == 0] -> [h(D*u**2) == h(D)*(u///w5D_(D))]] # 群规模公式牜负判别值牜不完全去平方因子化牜须留底:goto
        bug{注意前提}:[class_number{D} == class_number{Df}*(rtm///w5D_(Df))]
            =>下面都有bug:
            xxxxxxxxxxxxxxxxx:TODO
        !! [pseudo_class_number7not_necessary_primitive{D} == sum[class_number{D///k**2} | [k::int{>0}][0 == D%k**2][2 > (D///k**2)%4]]]
        [pseudo_class_number7not_necessary_primitive{D} == sum[class_number{Df}*(rtm///k///w5D_(Df)) | [k::int{>0}][0 == rtm%k]]]
        [pseudo_class_number7not_necessary_primitive{D}*w5D_(Df)/class_number{Df} == sum[(rtm///k) | [k::int{>0}][0 == rtm%k]] == sum[k | [k::int{>0}][0 == rtm%k]]]
        !! [class_number{D} == class_number{Df}*(rtm///w5D_(Df))]
        [pseudo_class_number7not_necessary_primitive{D}/class_number{D}
        == (1/rtm)*sum[k | [k::int{>0}][0 == rtm%k]]
            # 未必是整数
        == (1/rtm)*II[(p**(1+gde_(p;rtm)) -1)///(p-1) | [p::prime][0 == rtm%p]]
        == II[((p**(1+e4p) -1)///(p-1))/p**e4p | [p::prime][0 == rtm%p][e4p:=gde_(p;rtm)]]
        == II[1+((p**e4p -1)///(p-1))/p**e4p | [p::prime][0 == rtm%p][e4p:=gde_(p;rtm)]]
        == II[p/(p-1) -1/(p-1)/p**e4p | [p::prime][0 == rtm%p][e4p:=gde_(p;rtm)]]
        == II[(p -1/p**e4p)/(p-1) | [p::prime][0 == rtm%p][e4p:=gde_(p;rtm)]]
        ]
        [pseudo_class_number7not_necessary_primitive{D}/class_number{D} == II[(p -1/p**e4p)/(p-1) | [p::prime][0 == rtm%p][e4p:=gde_(p;rtm)]]]
            #here:fail:证明:[扩伪群规模%群规模 == 0]
            #   rhs未必是整数
            #   根本原因是:集合扩大后 非群
        [class_number{D} == pseudo_class_number7not_necessary_primitive{D}*rtm /// II[(p**(1+gde_(p;rtm)) -1)///(p-1) | [p::prime][0 == rtm%p]]]
        !! [pseudo_class_number7not_necessary_primitive{D} == sum[tpseudo_class_number7not_necessary_primitive7coprimeAD_{D///ft4D,k,t} | [ft4D::int{>0}][0 == D%ft4D][(k,t) := decompose_squarefree_part_ex_(ft4D)]]]
        [class_number{D} == rtm*sum[tpseudo_class_number7not_necessary_primitive7coprimeAD_{D///ft4D,k,t} | [ft4D::int{>0}][0 == D%ft4D][(k,t) := decompose_squarefree_part_ex_(ft4D)]] /// II[(p**(1+gde_(p;rtm)) -1)///(p-1) | [p::prime][0 == rtm%p]]]
            # 群规模计算牜蛮力牜后缩放牜拆分成泛子型牜参数互素:here
            #   虽然:[1==gcd(Dt,A)]但没有:[1=?=gcd(Dt,k)]，依然麻烦
        ==>>:
        #改为：先缩放:
        # [D:=Df][(rtm,Df):=(1,Df)][(k,t):=(1,ft4Df)][Dt:=Df///ft4Df]
        #   [D%4==0] => ++[D:=Df][(rtm,Df):=(1,Df)][(k,t):=(2,ft4Df///4)][Dt:=Df///ft4Df]
        #   不论哪种，都有:[1==gcd(k**2,Dt)]
        #   不论哪种，都有:[2>=gcd(k**2,t*Dt)]
        #       等号<==>[D%16==8]
        [class_number{Df} == sum[([ft4Df%4=!=0]*tpseudo_class_number7not_necessary_primitive7coprimeAD_{Df///ft4Df,1,ft4Df} +[ft4Df%4==0]*tpseudo_class_number7not_necessary_primitive7coprimeAD_{Df///ft4Df,2,ft4Df///4}) | [ft4Df::int{>0}][0 == Df%ft4Df]]]
        !! [class_number{D} == class_number{Df}*(rtm///w5D_(Df))]
        [class_number{D} == (rtm///w5D_(Df))*sum[([ft4Df%4=!=0]*tpseudo_class_number7not_necessary_primitive7coprimeAD_{Df///ft4Df,1,ft4Df} +[ft4Df%4==0]*tpseudo_class_number7not_necessary_primitive7coprimeAD_{Df///ft4Df,2,ft4Df///4}) | [ft4Df::int{>0}][0 == Df%ft4Df]]]
            # 群规模计算牜蛮力牜先缩放牜拆分成泛子型牜参数互素:here
            #   [1==gcd(Dt,A)][1==gcd(Dt,k)] => 容易处理
            #   这是 蛮力计算的主用定理 <<== [k:=(1|2)][1==gcd(Dt,k*A)]
            #   {发现难以兼容}:见下面:class_number7CeqA:『简化条件:分离出:[C==A]』

        !! [tpseudo_class_number7not_necessary_primitive7coprimeAD_{Dft,1,t} == tpseudo_class_number7not_necessary_primitive7CeqA7coprimeAD_{Dft,t} + tpseudo_class_number7not_necessary_primitive7CgtA7coprimeAD_{Dft,t}]
        [class_number{D} == (rtm///w5D_(Df))*(sum[([ft4Df%4=!=0]*(tpseudo_class_number7not_necessary_primitive7CeqA7coprimeAD_{Df///ft4Df,ft4Df} +tpseudo_class_number7not_necessary_primitive7CgtA7coprimeAD_{Df///ft4Df,ft4Df}) +[ft4Df%4==0]*tpseudo_class_number7not_necessary_primitive7coprimeAD_{Df///ft4Df,2,ft4Df///4}) | [ft4Df::int{>0}][0 == Df%ft4Df]])]
            #??无用


    ######################
    简化条件:分离出:[C==A]
    ######################
    [class_number7CeqA{D} == len{Qfb(A,B,A) | [[A,B::int][D==B**2-4*A**2][A>=B>=0][1==gcd(A,B)]]}]
    [pseudo_class_number7not_necessary_primitive7CeqA{D} == len{Qfb(A,B,A) | [[A,B::int][D==B**2-4*A**2][A>=B>=0]]}]

    [pseudo_class_number7not_necessary_primitive7CeqA{D} == sum[class_number7CeqA{D///k**2} | [k::int{>0}][0 == D%k**2][2 > (D///k**2)%4]]]

    [[A,B::int][D==B**2-4*A**2][A>=B>=0][1==gcd(A,B)]][u,v :: int{>0}][0 < u <= v][u*v == -D == (2*A-B)*(2*A+B)][u==(2*A-B)][v==(2*A+B)]:
        [gcd(u,v)
        == gcd((2*A-B), (2*A+B))
        == gcd((4*A), (2*A+B))
        <- gcd((4*A), 2*(2*A+B)) ./ {1,2}
        == gcd((4*A), (2*B)) ./ {1,2}
        == 2*gcd((2*A), B) ./ {1,2}
        !! [1==gcd(A,B)]
        == 2*gcd(2, B) ./ {1,2}
        ]
        [2*gcd(2,B)%gcd(u,v) == 0]
        [2*gcd(2,B)///gcd(u,v) <= 2]
        [gcd(u,v) <- {1,2,4}]

        [v+u == 4*A]
        [v-u == 2*B]

        [A == (v+u)/4]
        [B == (v-u)/2]
        [gcd(A,B)
        == gcd((v+u)/4,(v-u)/2)
        == gcd((v+u)/4,v)
        ]
        [gcd(A,B) == gcd((v+u)/4,v)]
        [0 == gcd((v+u),v)%gcd((v+u)/4,v)]
        [0 == gcd(u,v)%gcd(A,B)]


        !! [A == (v+u)/4]
        !! [B == (v-u)/2]
        !! [A>=B>=0]
        [(v+u)/4 >= (v-u)/2 >= 0]
        [v >= u][6*u >= 2*v]
        [u <= v <= 3*u]
        [-D == u*v <= v**2 <= 3*u*v == 3*-D]
        [sqrt(-D) <= v <= sqrt(3*-D)]
        [v/3 <= u <= v <= 3*u]
        [u*v/3 <= u**2 <= u*v]
        [sqrt(-D/3) <= u <= sqrt(-D)]
        [sqrt(-D/3) <= u <= sqrt(-D) <= v <= sqrt(3*-D)]

        !! [v+u == 4*A]
        !! [v-u == 2*B]
        [(v+u)%4 == 0]
        [(v-u)%2 == 0]
        [v%2 == u%2]
        [v%4 == (-u)%4]
        [(u%4, v%4) <- {(0,0),(2,2),(1,3),(3,1)}]

        * [D%4 == 0]:
            [u*v%4 == 0]
            [(u%4, v%4) <- {(0,0),(2,2)}]
            [gde_(2;D) <-!- {0,1,3}]
            [[gde_(2;D) == 2]or[gde_(2;D) >= 4]]
            [D%16 =!= 8]
            [[D%16 == 8] -> [0==class_number7CeqA{D}]]
            * [gde_(2;D) == 2]:
                [D%8 == 4]
                [(u%4, v%4) == (2,2)]
                !! [gcd(u,v) <- {1,2,4}]
                [gcd(u,v) == 2]
                [gcd(u/2,v/2) == 1]

                !! [0 == gcd(u,v)%gcd(A,B)]
                [0 == 2%gcd(A,B)]
                * [gcd(A,B) == 2]:
                    !! [gcd(A,B) == gcd((v+u)/4,v)]
                    !! [v%2 == 0]
                    [(v+u)/4 %2 == 0]
                    [(v+u) %8 == 0]
                * [gcd(A,B) == 1]:
                    !! [gcd(A,B) == gcd((v+u)/4,v)]
                    !! [v%2 == 0]
                    [(v+u)/4 %2 == 1]
                    [(v+u) %8 == 4]
                !! [gcd(A,B) == 1]
                [(v+u) %8 == 4]
                !! [u%4 == v%4 == 2]
                [u%8 == v%8 <- {2,6}]
                [u/2%4 == v/2%4 <- {1,3}]
                [(-D)/4%4 == u*v/4%4 == 3]
                [D/4%4 == 1]
                [D%16 == 4]
                [[D%8 == 4][D%16 =!= 4] -> [0==class_number7CeqA{D}]]
                [[D%16 == 12] -> [0==class_number7CeqA{D}]]

                search:(u/2,v/2):
                    # for:class_number7CeqA{D}
                    [u%4 == v%4 == 2]
                    [u/2%4 == v/2%4 <- {1,3}]
                    [gcd(u/2,v/2) == 1]
                    [sqrt(-D/3)/2 <= u/2 <= sqrt(-D)/2 <= v/2 <= sqrt(3*-D)/2]
                    [u/2*v/2 == -D/4]
            * [gde_(2;D) >= 4]:
                [D%16 == 0]
                [(u%4, v%4) == (0,0)]
                [gcd(u,v)%4 == 0]
                !! [gcd(u,v) <- {1,2,4}]
                [gcd(u,v) == 4]
                [gcd(u/4,v/4) == 1]
                !! [0 == gcd(u,v)%gcd(A,B)]
                [0 == 4%gcd(A,B)]
                * [gcd(A,B) == 4]:
                    !! [gcd(A,B) == gcd((v+u)/4,v)]
                    !! [v%4 == 0]
                    [(v+u)/4 %4 == 0]
                    [(v+u) %16 == 0]
                * [gcd(A,B) == 2]:
                    !! [gcd(A,B) == gcd((v+u)/4,v)]
                    !! [v%4 == 0]
                    [(v+u)/4 %4 == 2]
                    [(v+u) %16 == 8]
                * [gcd(A,B) == 1]:
                    !! [gcd(A,B) == gcd((v+u)/4,v)]
                    !! [v%4 == 0]
                    [(v+u)/4 %2 == 1]
                    [(v+u) %8 == 4]
                !! [gcd(A,B) == 1]
                [(v+u) %8 == 4]
                !! [u%4 == v%4 == 0]
                [{u%8,v%8} == {0,4}]
                [{u/4%2,v/4%2} == {0,1}]
                [(-D)/16%2 == u*v/16%2 == 0]
                [D%32 == 0]
                [[D%16 == 0][D%32 =!= 0] -> [0==class_number7CeqA{D}]]
                [[D%32 == 16] -> [0==class_number7CeqA{D}]]

                search:(u/4,v/4):
                    # for:class_number7CeqA{D}
                    [u%4 == v%4 == 0]
                    [{u/4%2,v/4%2} == {0,1}]
                    [gcd(u/4,v/4) == 1]
                    [sqrt(-D/3)/4 <= u/4 <= sqrt(-D)/4 <= v/4 <= sqrt(3*-D)/4]
                    [u/4*v/4 == -D/16]
        * [D%4 == 1]:
            [u*v%4 == 3]
            [(u%4, v%4) <- {(1,3),(3,1)}]
            !! [gcd(u,v) <- {1,2,4}]
            [gcd(u,v) == 1]
            !! [0 == gcd(u,v)%gcd(A,B)]
            [0 == 1%gcd(A,B)]
            [gcd(A,B) == 1]

            search:(u,v):
                # for:class_number7CeqA{D}
                [{u%4,v%4} == {1,3}]
                [gcd(u,v) == 1]
                [sqrt(-D/3) <= u <= sqrt(-D) <= v <= sqrt(3*-D)]
                [u*v == -D]
    #简化条件:分离出:[C==A]
    ==>>:
        * [D%16 == 4]:
            search:(u/2,v/2):
                # for:class_number7CeqA{D}
                [u%4 == v%4 == 2]
                [u/2%4 == v/2%4 <- {1,3}]
                [gcd(u/2,v/2) == 1]
                [sqrt(-D/3)/2 <= u/2 <= sqrt(-D)/2 <= v/2 <= sqrt(3*-D)/2]
                [u/2*v/2 == -D/4]
        * [D%32 == 0]:
            search:(u/4,v/4):
                # for:class_number7CeqA{D}
                [u%4 == v%4 == 0]
                [{u/4%2,v/4%2} == {0,1}]
                [gcd(u/4,v/4) == 1]
                [sqrt(-D/3)/4 <= u/4 <= sqrt(-D)/4 <= v/4 <= sqrt(3*-D)/4]
                [u/4*v/4 == -D/16]
        * [D%4 == 1]:
            search:(u,v):
                # for:class_number7CeqA{D}
                [{u%4,v%4} == {1,3}]
                [gcd(u,v) == 1]
                [sqrt(-D/3) <= u <= sqrt(-D) <= v <= sqrt(3*-D)]
                [u*v == -D]
    ==>>:
        [[0==class_number7CeqA{D}] >= ([D%16 == 8] +[D%16 == 12] +[D%32 == 16])]
            #『>=』:因为u,v的其他约束:范围约束+互素分量约束 可能导致空集
        [[0=!=class_number7CeqA{D}] <= ([D%16 == 4] +[D%32 == 0] +[D%4 == 1])]
            # [D%4==0] => D%32:+0,+4,+20
            # [D%4==0] => D%32:+0,+4,-8,-12,-16,+20,-24,-28

    !! vs: [[u>=2][D%u == 0] -> [h(D*u**2) == h(D)*(u///w5D_(D))]] # 群规模公式牜负判别值牜不完全去平方因子化牜须留底:goto
    ??? [class_number7CeqA{D*u**2} == class_number7CeqA{D}*(u///w5D_(D))]
        #不太行:这样一来，就无用
        #pseudo_class_number7not_necessary_primitive7CeqA倒是有可能


    ######################
    简化条件:分离出:[C>A]
    ######################
    [class_number7CgtA{D} == len{Qfb(A,B,C) | [[A,B,C::int][D==B**2-4*A*C][C>A>=B>-A][1==gcd(A,B,C)]]}]
    [pseudo_class_number7not_necessary_primitive7CgtA{D} == len{Qfb(A,B,C) | [[A,B,C::int][D==B**2-4*A*C][C>A>=B>-A]]}]

    [pseudo_class_number7not_necessary_primitive7CgtA{D} == sum[class_number7CgtA{D///k**2} | [k::int{>0}][0 == D%k**2][2 > (D///k**2)%4]]]


    [(rtm,_Df) := decompose_squarefree_part_ex_(D///4 if D%4==0 else D)][Df := 4*_Df if D%4==0 else _Df]:
        # Df : negative fundamental discriminant
        # rtm : max sqrt
        [D == rtm**2*Df]
        !! [[u>=2][D%u == 0] -> [h(D*u**2) == h(D)*(u///w5D_(D))]] # 群规模公式牜负判别值牜不完全去平方因子化牜须留底:goto
        bug{注意前提}:[class_number{D} == class_number{Df}*(rtm///w5D_(Df))]
        [class_number{Df} == class_number7CeqA{Df} + class_number7CgtA{Df}]
        [class_number7CgtA{Df} == ...]

    ######################
    暂不考虑:[C>=A]
    发现对称性:[1 <= A <= max4A][-A < B <= A] => [C >= abs(B)][C <?> A]
    => [h(D)==(sum[num_Bs6ZA{A} | [1 <= A <= max4A{D}]] -sum[num_Bs6ZA{A} | [1 <= A <= max4A{D}][A==C]])///2 +h7CeqA(D)]
    ######:
    [D<0][max4A := floor_sqrt((-D -[D=!=-3])/3)][1 <= A <= max4A][0 <= B <= A][D==B**2-4*A*C][C >= 1]:
        #暂不考虑:[C>=A]
        * [D == -3]:
            [max4A == floor_sqrt((3 -0)/3) == 1]
            [A==1]
            [0 <= B <= 1]
            [B%2 == D%1 == 1]
            [B==1]
            [-3 == B**2-4*C]
            [4*C == 3+B**2 == 4]
            [C==1]
            [C>=B]
        * [D =!= -3]:
            [max4A == floor_sqrt((-D -1)/3)]
            [A <= sqrt((-D-1)/3)]
            [1+3*A**2 <= (-D)]
            [(-D)-3*A**2 >= 1]
            [B**2 -4*A*C -D == 0]
            [B**2 -4*A*B -D == 4*A*(C-B)]
            [C < B]:
                [C-B < 0]
                [B**2 -4*A*B -D < 0]
                [f(B) := (B**2 -4*A*B -D)]
                [f(B) < 0]
                [f(B) decrease for B in interval(-oo,2*A)]
                !! [0 <= B <= A]
                [f(B) decrease]
                !! [(-D)-3*A**2 >= 1]
                [0 > f(B) >= f(A) == (A**2 -4*A*A -D) == -D -3*A**2 >= 1]
                [0 > 1]
                _L
            [C>=B]
            [0 <= B <= min(A,C)]
        ==>>:
        [C>=B]
    [[D<0][max4A := floor_sqrt((-D -[D=!=-3])/3)][1 <= A <= max4A][0 <= B <= A][D==B**2-4*A*C][C >= 1] -> [0 <= B <= min(A,C)]]
        #bug:对称性:避免CRT_le
        #   不太对:[max4A >= A > C] => [C < max4A] #[C > max4A]并未被重复计算...
        # CRT_le来自C俩个阈值之一:[C>=A]vs[C>max4A] # 自动有[C>=B]
    ######################




    ######################
    先枚举B，再枚举(A,C)
    ######:
    [B%2 == D%2]
    [0 <= abs4B <= max4A]
    [A*C == (B**2 + -D)///4]
    [p2e4AC := factor((B**2 + -D)///4)]
        #缺点:查表法 占空O(D)
    [abs4B <= A <= C]
    [1==gcd(abs4B, A, C)]
    ...
    ######################
    doing
]]
#]]]'''#'''


__all__ = r'''
iter_class_numbers5neg_discriminants_
    iter_class_numbers5neg_discriminants__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_
    iter_class_numbers5neg_discriminants__7brute_force7count_primitive_binary_quadratic_forms7ratio7CRT_
    iter_class_numbers5neg_discriminants__7brute_force7count_primitive_binary_quadratic_forms7ratio7sum_over_Df_






class_number5neg_discriminant__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_
    iter_class_numbers5neg_discriminants__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_
        iter_ABCs6Qfb5neg_discriminant__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_






class_number5neg_discriminant__7brute_force7count_primitive_binary_quadratic_forms7ratio_
    class_number5neg_discriminant__7brute_force7count_primitive_binary_quadratic_forms7ratio7CRT_
        iter_class_numbers5neg_discriminants__7brute_force7count_primitive_binary_quadratic_forms7ratio7CRT_
        class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7CRT_
    class_number5neg_discriminant__7brute_force7count_primitive_binary_quadratic_forms7ratio7sum_over_Df_
        iter_class_numbers5neg_discriminants__7brute_force7count_primitive_binary_quadratic_forms7ratio7sum_over_Df_
        class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7sum_over_Df_






w5D_
    hratio4class_number7Duu_
    ratio4class_number7Duu_

    hratio4pseudo_class_number7Duu_
    ratio4pseudo_class_number7Duu_

is_negative_discriminant_
    is_negative_fundamental_discriminant_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
    from seed._lazy_ import fst, snd, echo# print_err, ifNone
import re
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from math import gcd
    from seed.math.floor_ceil_tools.fc_kth_root import floor_sqrt, ceil_sqrt
    from seed.math.BinaryQuadraticForm import check_discriminant7Qfb_
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.math.prepare_p2e4N import prepare_p2e4N_
    #def prepare_p2e4N_(N, may_p2e4N_or_ps4N_or_factor_pint_func, /):
    from seed.math.II import II, II__p2e_# II_mod, II__ft2e_, II__ft_e_pairs_, factorial_mod_
    from seed.math.Kronecker_symbol import Kronecker_symbol
    from seed.math.floor_ceil_tools.fc_perfect import perfect_div
    from seed.iters.is_sorted import is_strict_sorted
    from seed.math.prime_sieve.sieve_lt import list_primes__lt_
    from seed.math.sqrts_mod_ import list_sqrts_mod_prime_
    from seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N import KthRoots4N
    from itertools import product, chain, islice, count
    from seed.math.Chinese_Remainder_Theorem__ver2 import get_CRT_type_
    #CRT = get_CRT_type_(extended=False, ver='long_term')
    #u = CRT(us)(rs)

    from seed.math.factor_pint.perfect_power.lift_neg_kth_root_mod_coprime_power_ import sqrt_mod_coprime_power_, iter_degrade_sqrts_mod_prime_power__coprime__5one_sqrt_
    #def sqrt_mod_coprime_power_(M, j, y, x1, /):
    #    '[[M%2==1]or[log2(M)%1 == 0]] => M -> j -> y -> x1 -> xj # [gcd(M,y) == 1][x1**2 =[%M**1]= y][xj**2 =[%M**j]= y][[M%2==1] -> [xj =[%M]= x1]][[log2(M)%1 == 0] -> [xj =[%(max(2,M)///2)]= x1]]!!!!!!NOTE!!!!!!'
    #def iter_degrade_sqrts_mod_prime_power__coprime__5one_sqrt_(p, i, j, p_i, p_j, x__p_i, /):
    #    'p -> i -> j -> p_i -> p_j -> x__p_i/(int%p_i) -> xs__p_j/Iter w__p_j/(int%p_j) # [[p is prime][x__p_i%p =!= 0][1 <= j <= i][p_i == p**i][0 <= x__p_i < p_i][0 <= w__p_j < p_j][w__p_j**2%p_j == x__p_i**2%p_j]]'

    from seed.tiny_.types5py import curry1
    #from seed.iters.flatten_recur import flatten_recur

    from seed.debug.show_name_value_pairs_ import errshow_name_value_pairs_, show_name_value_pairs_, iter_name_value_pairs_, parse_xnms_
    from seed.math.iter_unsorted_squarefree_uints import iter_unsorted_squarefree_uints_

    from seed.math.iter_sorted_squarefree_uints import iter_sorted_squarefree_uints_
    #def iter_sorted_squarefree_uints_(may_primes=None, /, *, may_prime2ok_=None, more=False, to_seq6more=False, may_squarefree7resume=None, new_resume=False, neg_resume_ok=False):
    from seed.math.iter_sorted_squarefree_uints import iter_reversed_sorted_negative_fundamental_discriminants_



#.#################################
___end_mark_of_excluded_global_names__0___ = ...


__all__
def iter_class_numbers5neg_discriminants__7brute_force7count_primitive_binary_quadratic_forms7ratio7sum_over_Df_(Ds__or__num_Ds, may_p2e4neg4D_or_ps4D_or_factor_pint_func=None, /, *, case6num_Ds='', with_D=False, to_mul_four=False, nonprimitive_ok=False, both7nonprimitive=False, _path4validate=None, _regex8selector4line4path=None):
    '(Ds/Iter D/int{<0} | num_Ds/uint{>=0}) -> Iter class_number{D}/uint{>=0} # [TIME:O(Df*ln(Df)**3)]'
    class_number5neg_discriminant__7brute_force7count_primitive_binary_quadratic_forms7ratio7sum_over_Df_
    tag = '_7brute_force7count_primitive_binary_quadratic_forms7ratio7sum_over_Df_'
    kwds = {}
    return iter_class_numbers5neg_discriminants_(tag, Ds__or__num_Ds, may_p2e4neg4D_or_ps4D_or_factor_pint_func, case6num_Ds=case6num_Ds, with_D=with_D, to_mul_four=to_mul_four, nonprimitive_ok=nonprimitive_ok, both7nonprimitive=both7nonprimitive, _path4validate=_path4validate, _regex8selector4line4path=_regex8selector4line4path, **kwds)
def iter_class_numbers5neg_discriminants__7brute_force7count_primitive_binary_quadratic_forms7ratio7CRT_(Ds__or__num_Ds, may_p2e4neg4D_or_ps4D_or_factor_pint_func=None, /, *, case6num_Ds='', with_D=False, to_mul_four=False, nonprimitive_ok=False, both7nonprimitive=False, _path4validate=None, _regex8selector4line4path=None):
    '(Ds/Iter D/int{<0} | num_Ds/uint{>=0}) -> Iter class_number{D}/uint{>=0} # [TIME:O(Df**(1/2+err))*len(Ds)]'
    class_number5neg_discriminant__7brute_force7count_primitive_binary_quadratic_forms7ratio7CRT_
    tag = '_7brute_force7count_primitive_binary_quadratic_forms7ratio7CRT_'
    kwds = {}
    return iter_class_numbers5neg_discriminants_(tag, Ds__or__num_Ds, may_p2e4neg4D_or_ps4D_or_factor_pint_func, case6num_Ds=case6num_Ds, with_D=with_D, to_mul_four=to_mul_four, nonprimitive_ok=nonprimitive_ok, both7nonprimitive=both7nonprimitive, _path4validate=_path4validate, _regex8selector4line4path=_regex8selector4line4path, **kwds)
def iter_class_numbers5neg_discriminants__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_(Ds__or__num_Ds, may_p2e4neg4D_or_ps4D_or_factor_pint_func=None, /, *, case6num_Ds='', with_D=False, to_mul_four=False, nonprimitive_ok=False, both7nonprimitive=False, validate6both=False, _path4validate=None, _regex8selector4line4path=None):
    '(Ds/Iter D/int{<0} | num_Ds/uint{>=0}) -> Iter class_number{D}/uint{>=0} # [TIME:O(D)*len(Ds)]'
    class_number5neg_discriminant__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_
    tag = '_7brute_force7enumerate_primitive_binary_quadratic_forms7naive_'
    kwds = dict(validate6both=validate6both)
    return iter_class_numbers5neg_discriminants_(tag, Ds__or__num_Ds, may_p2e4neg4D_or_ps4D_or_factor_pint_func, case6num_Ds=case6num_Ds, with_D=with_D, to_mul_four=to_mul_four, nonprimitive_ok=nonprimitive_ok, both7nonprimitive=both7nonprimitive, _path4validate=_path4validate, _regex8selector4line4path=_regex8selector4line4path, **kwds)
def iter_class_numbers5neg_discriminants_(tag, Ds__or__num_Ds, may_p2e4neg4D_or_ps4D_or_factor_pint_func=None, /, *, case6num_Ds='', with_D=False, to_mul_four=False, nonprimitive_ok=False, both7nonprimitive=False, _path4validate=None, _regex8selector4line4path=None, **kwds):
    'tag/str -> (Ds/Iter D/int{<0} | num_Ds/uint{>=0}) -> Iter class_number{D}/uint{>=0} # [[tag:="_7brute_force7enumerate_primitive_binary_quadratic_forms7naive_"] => [TIME:O(D)*len(Ds)]]   # [[tag:="_7brute_force7count_primitive_binary_quadratic_forms7ratio7CRT_"] => [TIME:O(Df**(1/2+err))*len(Ds)]]'
    match Ds__or__num_Ds:
        case int() as num_Ds:
            check_int_ge(0, num_Ds)
            match case6num_Ds:
                case '' | 'negative_even_discriminant':
                    Ds = (-neg4D for neg4D in range(1, 1+num_Ds))
                case 'squarefree_radicand_only':
                    us = iter_sorted_squarefree_uints_()
                    Ds = (-u*4 if not (-u)&3 < 2 else -u for u in us)
                    Ds = islice(Ds, 0, num_Ds)
                case 'negative_fundamental_discriminant':
                    Ds = iter_reversed_sorted_negative_fundamental_discriminants_()
                    Ds = islice(Ds, 0, num_Ds)
                case 'negative_discriminant':
                    Ds = (-u for u in count(1))
                    Ds = filter(is_negative_discriminant_, Ds)
                    Ds = islice(Ds, 0, num_Ds)
                case _:
                    raise Exception('unknown:', case6num_Ds)
            Ds
        case Ds:
            Ds = iter(Ds)
    Ds
    if to_mul_four:
        Ds = map((4).__mul__, Ds)
    Ds
    #f = class_number5neg_discriminant__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_
    #f = class_number5neg_discriminant__7brute_force7count_primitive_binary_quadratic_forms7ratio7CRT_
    #f = class_number5neg_discriminant__7brute_force7count_primitive_binary_quadratic_forms7ratio7sum_over_Df_
    nm = f'class_number5neg_discriminant_{tag!s}'
    f = globals()[nm]
    777;kwds = dict(nonprimitive_ok=nonprimitive_ok, both7nonprimitive=both7nonprimitive, **kwds)
        #777;kwds = dict(nonprimitive_ok=nonprimitive_ok, both7nonprimitive=both7nonprimitive, validate6both=validate6both)
    777;m = may_p2e4neg4D_or_ps4D_or_factor_pint_func
    g = lambda D, /:f(D, m, **kwds)
    h = lambda D, /:(D, g(D))

    it = map((g if not with_D else h), Ds)
    if _path4validate:
        assert _regex8selector4line4path
        rgx = re.compile(_regex8selector4line4path)
        get7dropD_ = echo if not with_D else snd
        assert bool(both7nonprimitive) >= bool(nonprimitive_ok)
        assert not (nonprimitive_ok and not both7nonprimitive)
        get7num_ = echo if not both7nonprimitive else fst
        def _iter_cmp(it, /, *, _path4validate=_path4validate, rgx=rgx):
            with open(_path4validate) as ifile:
                for line in ifile:
                    line = line.strip()
                    if not line:continue
                    m = next(it, None)
                    if m is None:
                        raise Exception('Ds shorter than lines@_path4validate', line)
                    r = m
                    num_BQFs7primitive = get7num_(get7dropD_(r))
                    m = rgx.fullmatch(line)
                    if m is None:
                        raise Exception('_regex8selector4line4path not fullmatch line@_path4validate', rgx, line)
                    s8num_BQFs7primitive = m['num_BQFs7primitive']
                    if not num_BQFs7primitive == int(s8num_BQFs7primitive):
                        raise Exception('validate fail@_path4validate', r, line, num_BQFs7primitive, s8num_BQFs7primitive)
                    yield r
                else:
                    m = next(it, None)
                    if not m is None:
                        raise Exception('Ds longer than lines@_path4validate', m)
        it = _iter_cmp(it)
    return it
def class_number5neg_discriminant__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_(D, may_p2e4neg4D_or_ps4D_or_factor_pint_func=None, /, *, nonprimitive_ok=False, both7nonprimitive=False, validate6both=False):
    'D/int{<0} -> class_number{D}/uint{>=0} # [TIME:O(D)]'
    #7not_necessary_primitive
    #def class_number5neg_discriminant__7enumerate_primitive_binary_quadratic_forms__7brute_force_(D, /):
    it = iter_ABCs6Qfb5neg_discriminant__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_(D, may_p2e4neg4D_or_ps4D_or_factor_pint_func, quiet=True, nonprimitive_ok=nonprimitive_ok, both7nonprimitive=both7nonprimitive, validate6both=validate6both)
    try:
        next(it)
    except StopIteration as exc:
        num_BQFs7total = exc.value
    else:
        raise 000
    return num_BQFs7total
def iter_ABCs6Qfb5neg_discriminant__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_(D, may_p2e4neg4D_or_ps4D_or_factor_pint_func=None, /, *, quiet=False, nonprimitive_ok=False, both7nonprimitive=False, validate6both=False):
    'D/int{<0} -> GI{yield (A,B,C);return class_number{D}/uint{>=0}} # [TIME:O(D)]'
    quiet = bool(quiet)
    both7nonprimitive = bool(both7nonprimitive)
    validate6both = both7nonprimitive and bool(validate6both)
    nonprimitive_ok = both7nonprimitive or bool(nonprimitive_ok)
    check_type_is(int, D)

    if not D < 0:raise ValueError(D)
    if not D%4 < 2:return 0 if not both7nonprimitive else (0,0)
    check_discriminant7Qfb_(D)
    # [[D < 0][D%4 < 2]]


    # primitive => [1 <= A < max(2,sqrt((-D)/3))]
    # nonprimitive_ok => [1 <= A <= max(1,sqrt((-D)/3))]
    #max4A = max(1, floor_sqrt((-1-D)//3)) if not nonprimitive_ok else max(1, floor_sqrt((-D)//3))
    max4A = max(1, floor_sqrt((-(not nonprimitive_ok)-D)//3))
    min4A = 1
    max4A7all_Bs = floor_sqrt((-D)//4)
    if both7nonprimitive:
        num_BQFs7primitive = 0
        num_BQFs7include_nonprimitive = 0
    else:
        num_BQFs7total = 0
    for A in range(min4A, 1+max4A):
        # !! [A >= abs(B) >= sqrt(max(0,D+4*A**2))]
        min4abs4B = ceil_sqrt(max(0,D+4*A**2)) if A > max4A7all_Bs else 0
        max4abs4B = A
        # !! [B%2 == D%2]
        if not min4abs4B&1 == D&1:
            min4abs4B += 1
        if not max4abs4B&1 == D&1:
            max4abs4B -= 1

        ZZA = A<<2
        # [ZZA == 4*A]

        #D6ZZA = D%ZZA
        # for_loop{A}:O(D**/2)
        #   for_loop{B}:O(A)==O(D**/2)
        # TIME:O(D)
        BB = (min4abs4B-2)**2
        for B in range(min4abs4B, 1+max4abs4B, 2):
            # [BB == (B-2)**2]
            BB += (B-1)<<2
            # [BB == B**2]
            (q, r) = divmod(BB-D, ZZA)
            # !! [ZZA == 4*A]
            # [B**2-D == 4*A*q + r]
            if not r==0:continue
            # [r == 0]
            C = q
            # [B**2-D == 4*A*C + 0]
            assert C >= A >= B >= 0
            # [C >= A >= B >= 0]
            if not (nonprimitive_ok or 1==gcd(A, B, C)):continue
            num_Bs6A = 1 + (C > A > B > 0)
                # [C == A >= B >= 0]*1
                # [C > A == B > 0]*1
                # [C > A > B == 0]*1
                # [C > A > B > 0 > -B > -A]*2
            num_Bs6A
            if both7nonprimitive:
                assert nonprimitive_ok
                if 1==gcd(A, B, C):
                    num_BQFs7primitive += num_Bs6A
                num_BQFs7include_nonprimitive += num_Bs6A
            else:
                num_BQFs7total += num_Bs6A
            if not quiet:
                yield (A, B, C)
                if num_Bs6A == 2:
                    yield (A, -B, C)
    if both7nonprimitive:
        assert 0 < num_BQFs7primitive <= num_BQFs7include_nonprimitive, (D, num_BQFs7primitive, num_BQFs7include_nonprimitive)
        if validate6both:
            p2e4neg4D = prepare_p2e4N_(-D, may_p2e4neg4D_or_ps4D_or_factor_pint_func)
            _validate7both_(D, p2e4neg4D, num_BQFs7primitive, num_BQFs7include_nonprimitive)
        return (num_BQFs7primitive, num_BQFs7include_nonprimitive)
    else:
        num_BQFs7total
        assert num_BQFs7total > 0, D
        return num_BQFs7total
    raise 000
r'''[[[
_validate7both_
[w5D_(D) := (6+max(-5,D))]
[D<0][D%4<2][u>0]:
    [hratio4class_number7Duu_(D,u) =[def]= (II[p**(-1+gde_(p;u))*(p-Kronecker_symbol(p;D)) | [p::prime][u%p==0]])]
    [ratio4class_number7Duu_(D,u) =[def]= (hratio4class_number7Duu_(D,u)///(1 if u == 1 else w5D_(D)))]
[rtm::uint{>0}][is_negative_fundamental_discriminant_(Df)]:
    [hratio4pseudo_class_number7Duu_(Df,rtm) =[def]= II[(1 + (p-Kronecker_symbol(p;Df))*(-1+p**e4p)///(-1+p)) | [p::prime][rtm%p==0][e4p:=gde_(p;rtm)]]]
    [ratio4pseudo_class_number7Duu_(Df,rtm) =[def]= (1 +(-1 +hratio4pseudo_class_number7Duu_(Df,rtm)) /// w5D_(Df))]

    [pseudo_class_number7not_necessary_primitive{Df*rtm**2}*ratio4class_number7Duu_(Df,rtm) == class_number{Df*rtm**2}*ratio4pseudo_class_number7Duu_(Df,rtm)] # 已证明:猜想校验用定理牜扩伪群规模倍率
#]]]'''#'''
def w5D_(D, /):
    return (6+max(-5,D))
def hratio4class_number7Duu_(D, u, p2e4u, /):
    return II((p-Kronecker_symbol(p,D))*p**(-1+e4p) for p, e4p in p2e4u.items())
def ratio4class_number7Duu_(D, u, p2e4u, /):
    r = hratio4class_number7Duu_(D, u, p2e4u)
    if u >= 2:
        r = perfect_div(r, w5D_(D))
    return r
def hratio4pseudo_class_number7Duu_(Df, rtm, p2e4rtm, /):
    return II((1 + (p-Kronecker_symbol(p,Df))*perfect_div((-1+p**e4p),(-1+p))) for p, e4p in p2e4rtm.items())
def ratio4pseudo_class_number7Duu_(Df, rtm, p2e4rtm, /):
    h = hratio4pseudo_class_number7Duu_(Df, rtm, p2e4rtm)
    return 1+perfect_div(-1+h, w5D_(Df))


def _validate7both_(D, p2e4neg4D, num_BQFs7primitive, num_BQFs7include_nonprimitive, /):
    ####################new:
    # now:check:已证明:猜想校验用定理牜扩伪群规模倍率
    #   已校验@(-4 .* range(1,1+20000))
    ((rtm, p2e4rtm), (Df, p2e4neg4Df)) = _decompose_squarefree_part_ex7except_four6Df_(D, p2e4neg4D)
    r4h = ratio4class_number7Duu_(Df,rtm, p2e4rtm)
    r4psh = ratio4pseudo_class_number7Duu_(Df,rtm, p2e4rtm)
    assert num_BQFs7include_nonprimitive*r4h == num_BQFs7primitive*r4psh, (D, p2e4neg4D, (num_BQFs7primitive, num_BQFs7include_nonprimitive), (Df, rtm, p2e4rtm, r4h, r4psh), (num_BQFs7include_nonprimitive*r4h, num_BQFs7primitive*r4psh, num_BQFs7include_nonprimitive*r4h -num_BQFs7primitive*r4psh))
    return
    ####################old:
    # bug:check: [class_number{D} == pseudo_class_number7not_necessary_primitive{D}*rtm /// II[(p**(1+gde_(p;rtm)) -1)///(p-1) | [p::prime][0 == rtm%p]]]
    ((rtm, p2e4rtm), (Df, p2e4neg4Df)) = _decompose_squarefree_part_ex7except_four6Df_(D, p2e4neg4D)
    sum4divisors4rtm = II((-1+p**(1+e))//(-1+p) for p, e in p2e4rtm.items())
    assert sum4divisors4rtm*num_BQFs7primitive == rtm*num_BQFs7include_nonprimitive, (D, p2e4neg4D, (num_BQFs7primitive, num_BQFs7include_nonprimitive), (Df, rtm, sum4divisors4rtm), (sum4divisors4rtm*num_BQFs7primitive, rtm*num_BQFs7include_nonprimitive, sum4divisors4rtm*num_BQFs7primitive -rtm*num_BQFs7include_nonprimitive))
        # AssertionError: (-12, {2: 2, 3: 1}, (1, 1), (-3, 2, 3), (3, 2, 1)) => fix:max4A@nonprimitive_ok
        # AssertionError: (-12, {2: 2, 3: 1}, (1, 2), (-3, 2, 3), (3, 4, -1))
    return
def _decompose_squarefree_part_ex7except_four6Df_(D, p2e4neg4D, /):
    # [(_rtm,_Df) := decompose_squarefree_part_ex_(D)][(rtm,Df) := (_rtm,_Df) if _Df%4 < 2 else (_rtm///2,4*_Df)]:
        # Df : negative fundamental discriminant
        # rtm : max sqrt
    assert D < 0
    assert D&3 < 2
    ((rtm, p2e4rtm), (neg4Df, p2e4neg4Df)) = _decompose_squarefree_part_ex_(-D, p2e4neg4D)
    Df = -neg4Df
    if not Df%4 < 2:
        assert rtm&1 == 0, (D, rtm, Df)
        if Df&1 == 1:
            p2e4neg4Df[2] = 2
        else:
            p2e4neg4Df[2] += 2

        rtm //= 2
        Df *= 4

        if rtm&1 == 1:
            del p2e4rtm[2]
        else:
            p2e4rtm[2] -= 1

    return ((rtm, p2e4rtm), (Df, p2e4neg4Df))

def _decompose_squarefree_part_ex_(N, p2e4N, /):
    assert N > 0
    p2e4rtm = {} # sqrt max
    p2e4sqf = {} # squarefree
    for p, e in p2e4N.items():
        (e4rtm, e4sqf) = divmod(e, 2)
        if e4rtm:
            p2e4rtm[p] = e4rtm
        if e4sqf:
            p2e4sqf[p] = e4sqf
    rtm = II__p2e_(p2e4rtm)
    sqf = II__p2e_(p2e4sqf)
    return ((rtm, p2e4rtm), (sqf, p2e4sqf))

__all__




def is_negative_discriminant_(D, /):
    check_type_is(int, D)
    return D < 0 and D&3 < 2
def is_negative_fundamental_discriminant_(Df, p2e4neg4Df, /):
    #bug:return is_negative_discriminant_(Df) and all(e4p in (2, 3) if p==2 else e4p == 1 for p, e4p in p2e4neg4Df.items())
    return is_negative_discriminant_(Df) and (Df&3 == 1 or Df&15 in (8,12)) and all(e4p in (2, 3) if p==2 else e4p == 1 for p, e4p in p2e4neg4Df.items())
    return is_negative_discriminant_(Df) and not (Df&3 == 0 and is_negative_discriminant_(Df>>2)) and all(e4p in (2, 3) if p==2 else e4p == 1 for p, e4p in p2e4neg4Df.items())


def class_number5neg_discriminant__7brute_force7count_primitive_binary_quadratic_forms7ratio7CRT_(D, may_p2e4neg4D_or_ps4D_or_factor_pint_func=None, /, *, nonprimitive_ok=False, both7nonprimitive=False):
    'D/int{<0} -> class_number{D}/uint{>=0} # [Df==D///rtm**2][TIME:O(Df**(1/2+err))]'
    class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7CRT_
    return class_number5neg_discriminant__7brute_force7count_primitive_binary_quadratic_forms7ratio_(tag:='CRT', D, may_p2e4neg4D_or_ps4D_or_factor_pint_func, nonprimitive_ok=nonprimitive_ok, both7nonprimitive=both7nonprimitive)
def class_number5neg_discriminant__7brute_force7count_primitive_binary_quadratic_forms7ratio7sum_over_Df_(D, may_p2e4neg4D_or_ps4D_or_factor_pint_func=None, /, *, nonprimitive_ok=False, both7nonprimitive=False):
    'D/int{<0} -> class_number{D}/uint{>=0} # [Df==D///rtm**2][TIME:O(Df*ln(Df)**3)]'
    class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7sum_over_Df_
    return class_number5neg_discriminant__7brute_force7count_primitive_binary_quadratic_forms7ratio_(tag:='sum_over_Df', D, may_p2e4neg4D_or_ps4D_or_factor_pint_func, nonprimitive_ok=nonprimitive_ok, both7nonprimitive=both7nonprimitive)

def class_number5neg_discriminant__7brute_force7count_primitive_binary_quadratic_forms7ratio_(tag, D, may_p2e4neg4D_or_ps4D_or_factor_pint_func=None, /, *, nonprimitive_ok=False, both7nonprimitive=False):
    'tag/str -> D/int{<0} -> class_number{D}/uint{>=0} # [Df==D///rtm**2]'
    nm = f'class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7{tag!s}_'
    f = globals()[nm]
    both7nonprimitive = bool(both7nonprimitive)
    nonprimitive_ok = both7nonprimitive or bool(nonprimitive_ok)
    check_type_is(int, D)

    if not D < 0:raise ValueError(D)
    if not D%4 < 2:return 0 if not both7nonprimitive else (0,0)
    check_discriminant7Qfb_(D)
    # [[D < 0][D%4 < 2]]

    p2e4neg4D = prepare_p2e4N_(-D, may_p2e4neg4D_or_ps4D_or_factor_pint_func)
    ((rtm, p2e4rtm), (Df, p2e4neg4Df)) = _decompose_squarefree_part_ex7except_four6Df_(D, p2e4neg4D)
    r4h = ratio4class_number7Duu_(Df,rtm, p2e4rtm)
    r4psh = ratio4pseudo_class_number7Duu_(Df,rtm, p2e4rtm)
    num_BQFs7Df = f(Df, p2e4neg4Df)
    num_BQFs7include_nonprimitive = num_BQFs7Df*r4psh
    num_BQFs7primitive = num_BQFs7Df*r4h
    num_BQFs7total = num_BQFs7primitive if not nonprimitive_ok else num_BQFs7include_nonprimitive
    return num_BQFs7total if not both7nonprimitive else (num_BQFs7primitive, num_BQFs7include_nonprimitive)


def class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7sum_over_Df_(Df, may_p2e4neg4Df_or_ps4Df_or_factor_pint_func=None, /, *, _not_fundamental_ok=False):
    'Df/int{<0}/is_negative_fundamental_discriminant_(Df) -> class_number{Df}/uint{>0} # [TIME:O(Df*ln(Df)**3)]'
    ''
    check_discriminant7Qfb_(Df)
    p2e4neg4Df = prepare_p2e4N_(-Df, may_p2e4neg4Df_or_ps4Df_or_factor_pint_func)
    p2e4neg4Df
    if not _not_fundamental_ok:
        if not is_negative_fundamental_discriminant_(Df, p2e4neg4Df):raise ValueError(Df, p2e4neg4Df)
    ##############################
    # [h(Df) == 1/Df * w5D_(Df) * sum[Kronecker_symbol(u;Df)*u | [u:<-[1..=-Df]]]] # 群规模公式牜有限求和牜基础负判别值:goto
    return perfect_div(w5D_(Df) * sum(Kronecker_symbol(u, Df) * u for u in range(1, 1-Df)), Df)

def class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7CRT_(Df, may_p2e4neg4Df_or_ps4Df_or_factor_pint_func=None, /, *, verbose=False):
    'Df/int{<0}/is_negative_fundamental_discriminant_(Df) -> class_number{Df}/uint{>0} # [TIME:O(Df**(1/2+err))]'
    check_discriminant7Qfb_(Df)
    p2e4neg4Df = prepare_p2e4N_(-Df, may_p2e4neg4Df_or_ps4Df_or_factor_pint_func)
    p2e4neg4Df
    if not is_negative_fundamental_discriminant_(Df, p2e4neg4Df):raise ValueError(Df, p2e4neg4Df)
    ##############################
    slack_max4A7noncoprime_ok = floor_sqrt((-Df)//3)
    (j2p4A, j2sqrts4D6p4A, j2max4e4p4A) = _prepare7p4A_sqrts4D_max4e4p_(Df, p2e4neg4Df, slack_max4A7noncoprime_ok)
    if verbose:
        #print_err()
        xnms = parse_xnms_('(slack_max4A7noncoprime_ok, (j2p4A, j2sqrts4D6p4A, j2max4e4p4A))')
        errshow_name_value_pairs_(xnms, (slack_max4A7noncoprime_ok, (j2p4A, j2sqrts4D6p4A, j2max4e4p4A)))
    ##############################
    (j2e2pow4p4ZA, j2e2sqrts6pow4p4ZA_4D6pow4p4ZZA) = _prepare7lookup_table4solution6prime_power_(Df, j2p4A, j2sqrts4D6p4A, j2max4e4p4A)
    if verbose:
        xnms = parse_xnms_('(j2e2pow4p4ZA, j2e2sqrts6pow4p4ZA_4D6pow4p4ZZA)')
        errshow_name_value_pairs_(xnms, (j2e2pow4p4ZA, j2e2sqrts6pow4p4ZA_4D6pow4p4ZZA))
    ##############################
    #bug:num_BQFs7include_nonprimitive = 0
        #bug:include:Qfb(2,-1,2) @[D==-60][Df==-15] @_count_num_Bs6A_
    num_BQFs7include_nonprimitive = -_count_num_bad_Bs6A__7CeqA_(Df, p2e4neg4Df)
        #fix_bug_6neg4Deq15__another:here
        # [C >= A >= B > -A]
        #   to exclude:[C == A >= 0 > B > -A]
    it = _iter_unsorted__A__j4p4A_e4p4A_pairs__pairs4Df__A_lt_(1+slack_max4A7noncoprime_ok, j2p4A, j2max4e4p4A)
    for (A, j4p4A_e4p4A_pairs) in it:
        slack_min4abs4B6A7noncoprime_ok = ceil_sqrt(max(0,4*A**2-(-Df)))
        #slack_min4C7noncoprime_ok
        ZZA = A << 2
        ZA = A << 1
        (moduli4CRT, remainderss4CRT) = _prepare7moduli_remainderss4CRT_(Df, j2p4A, j2max4e4p4A, j2e2pow4p4ZA, j2e2sqrts6pow4p4ZA_4D6pow4p4ZZA, A, j4p4A_e4p4A_pairs, verbose=verbose)
        num_Bs6A = _count_num_Bs6A_(A, slack_min4abs4B6A7noncoprime_ok, moduli4CRT, remainderss4CRT)
        num_BQFs7include_nonprimitive += num_Bs6A
        if verbose:
            xnms = parse_xnms_('((A, j4p4A_e4p4A_pairs), slack_min4abs4B6A7noncoprime_ok, (moduli4CRT, remainderss4CRT), num_Bs6A, num_BQFs7include_nonprimitive)')
            errshow_name_value_pairs_(xnms, ((A, j4p4A_e4p4A_pairs), slack_min4abs4B6A7noncoprime_ok, (moduli4CRT, remainderss4CRT), num_Bs6A, num_BQFs7include_nonprimitive))
        num_BQFs7include_nonprimitive
    num_BQFs7include_nonprimitive


    ##############################
    # !! [is_negative_fundamental_discriminant_(Df)]
    #_decompose_squarefree_part_ex7except_four6Df_()
    #D = Df
    777;rtm = 1
    777;p2e4rtm = {}
    r4h = ratio4class_number7Duu_(Df,rtm, p2e4rtm)
    r4psh = ratio4pseudo_class_number7Duu_(Df,rtm, p2e4rtm)
    assert r4h == 1
    assert r4psh == 1
    num_BQFs7primitive = r4h*perfect_div(num_BQFs7include_nonprimitive, r4psh)
    assert num_BQFs7primitive == num_BQFs7include_nonprimitive
    ##############################
    if verbose:
        xnms = parse_xnms_('[num_BQFs7primitive]')
        errshow_name_value_pairs_(xnms, [num_BQFs7primitive])

    ##############################
    return num_BQFs7primitive
    ##############################

def _prepare7p4A_sqrts4D_max4e4p_(Df, p2e4neg4Df, slack_max4A7noncoprime_ok, /):
    floor_log7max4A_ = KthRoots4N(slack_max4A7noncoprime_ok)
    j2p4A = []
    j2sqrts4D6p4A = []
    j2max4e4p4A = []
    #ps4A = list_primes__lt_(1+slack_max4A7noncoprime_ok)
    ps4ZA = list_primes__lt_(1+max(2,slack_max4A7noncoprime_ok))
    # to solve: [B**2 =[%(4*A)]= Df]
    for p in ps4ZA:
        # to solve: [B**2 =[%(4*p)]= Df]
        sqrts4D6p4A = list_sqrts_mod_prime_(p, Df)
        if not sqrts4D6p4A:continue
        assert is_strict_sorted(sqrts4D6p4A)
        j2p4A.append(p)
        j2sqrts4D6p4A.append(sqrts4D6p4A)
        if 0 == sqrts4D6p4A[0]:
            match p2e4neg4Df[p]:
                #e4p6neg4Df
                case 1:
                    # to solve: [B**2 =[%p**e]= p*(Df///p)]
                    assert p > 2
                    max4e4p4A = 1
                case 2:
                    # to solve: [B**2 =[%(4*2**e)]= 4*(Df///4)]
                    assert p == 2
                    #bug:max4e4p4A = floor_log7max4A_(p)
                    # [Df == 4*odd4Df]
                    # [odd4Df&4 =!= 1]
                    # [odd4Df%4 == 3]
                    # [ez4B == 1]
                    # [odd4B**2 =[%4]= odd4Df] has no solutions
                    # [max4e4p4A>=2][odd4Df%4 == 3] => [odd4B**2 =[%(2**max4e4p4A)]= odd4Df] has no solutions
                    # [max4e4p4A>=2][odd4Df%4 == 3] => [B**2 =[%(4*2**max4e4p4A)]= 4*odd4Df] has no solutions
                    max4e4p4A = 1
                        # fix_bug_6neg4Deq52:here
                    # [max4e4p4A == 1]
                    # [max4e4p4A==1][odd4Df%4 == 3][B**2 =[%(4*2**max4e4p4A)]= 4*odd4Df] =>  [B**2 =[%8]= 4][B%8 <- {2,6}][B%4 == 2]
                case 3:
                    # to solve: [B**2 =[%(4*2**e)]= 8*(Df///8)]
                    assert p == 2
                    max4e4p4A = 1#not 3
                case e4p6neg4Df:
                    raise Exception('bug:is_negative_fundamental_discriminant_()', Df, p2e4neg4Df, p, e4p6neg4Df)
            max4e4p4A
        else:
            # MAYBE:[p==2]

            #max4e4p4A = floor_log7max4A_(p)
                #later:^ValueError@sqrt_of_odd_mod_zpow_:『if not y&7 == 1:raise ValueError』
            if p==2 and not Df&7 == 1:
                #fix_bug_6neg4Deq19:here
                # [Df%8 =!= 1]
                # !! [Df%4 == 1]
                # [Df%8 == 5]
                assert Df&7 == 5
                # [max4e4p4ZZA < 3]
                # [max4e4p4A < 1]
                max4e4p4A = 0 # min(0, max4e4p4A)
            else:
                max4e4p4A = floor_log7max4A_(p) if not (p==2 > slack_max4A7noncoprime_ok) else 0
            max4e4p4A
        max4e4p4A
        j2max4e4p4A.append(max4e4p4A)
    j2p4A
    j2sqrts4D6p4A
    j2max4e4p4A
    assert j2p4A
    assert j2p4A[0] == 2
    assert all(max4e4p4A > 0 or p4A == 2 for p4A, max4e4p4A in zip(j2p4A, j2max4e4p4A))
        # fix_bug_6neg4Deq3.part1:here
    return (j2p4A, j2sqrts4D6p4A, j2max4e4p4A)

def _list_pows_(p4A, max4e4p4A, /):
    max4e4p4ZA = max4e4p4A +(p4A==2)
    ls = [1]
    for e in range(1, 1+max4e4p4ZA):
        ls.append(ls[-1]*p4A)
    return ls
def _prepare7lookup_table4solution6prime_power_(Df, j2p4A, j2sqrts4D6p4A, j2max4e4p4A, /):
    #预先准备好 结果乊素幂模分量...
    j2e2pow4p4ZA = [*map(_list_pows_, j2p4A, j2max4e4p4A)]
    j2e2sqrts6pow4p4ZA_4D6pow4p4ZZA = [*map(curry1(_list_sqrtss_, Df), j2p4A, j2sqrts4D6p4A, j2max4e4p4A, j2e2pow4p4ZA)]
    return (j2e2pow4p4ZA, j2e2sqrts6pow4p4ZA_4D6pow4p4ZZA)
def _list_sqrtss_(Df, p4A, sqrts4D6p4A, max4e4p4A, e2pow4p4ZA, /):
    max4e4p4ZA = max4e4p4A +(p4A==2)
    assert len(e2pow4p4ZA) == 1+max4e4p4ZA
    max4e4p4ZZA = max4e4p4A + 2*(p4A==2)
    if 0 == (B6p4A:=min(sqrts4D6p4A)):
        # [Df%p == 0]
        if p4A == 2:
            ez4Df = 2 +(Df&7 == 0)
            odd4Df = Df >> ez4Df
            max4e4p4ZZA
            if ez4Df < max4e4p4ZZA:
                # [ez4Df < max4e4p4ZZA]
                assert ez4Df == 2
                assert odd4Df&3 == 3
                # [max4e4p4A>=2][odd4Df%4 == 3] => [odd4B**2 =[%(2**max4e4p4A)]= odd4Df] has no solutions
                assert max4e4p4A == 1
                    # fix_bug_6neg4Deq52:goto
                # [max4e4p4A == 1]
                assert max4e4p4ZZA == 3
                if 0:
                    ##obsolete:
                    assert ez4Df == 2
                    # [max4e4p4ZZA >= 3]
                    # [max4e4p4A >= 1]
                    ez4B = 1
                    # [(2*odd4B)**2 == B**2 =[%(4*2**max4e4p4A)]= Df == 4*odd4Df]
                    # [odd4B**2 =[%(2**max4e4p4A)]= odd4Df]
                    # get: [??? =[%2**max(0,-1+max4e4p4A)]= odd4B]
                    # !! [max4e4p4A >= 1]
                    # get: [??? =[%2**(-1+max4e4p4A)]= odd4B]
                    odd4B6zpow7emm = sqrt_mod_coprime_power_(p4A, max4e4p4A, odd4Df, odd4Df&1)
                        # ^ValueError <<== [odd4Df%4 == 3]
                        # fix_bug_6neg4Deq52:goto
                    # [odd4B6zpow7emm =[%2**(-1+max4e4p4A)]= odd4B]
                    B6max4pow4p4A = 2*odd4B6zpow7emm
                    # [B6max4pow4p4A == 2*odd4B6zpow7emm =[%2**(max4e4p4A)]= 2*odd4B == B]
                    B6max4pow4p4A # not:B6max4pow4p4ZA
                    B6max4pow4p4ZA = B6max4pow4p4A
                        # one of 1/2 solutions
                        # bug:one of 1/2/4 solutions
                        #   fix_bug_6neg4Deq71:goto
                else:
                    # [max4e4p4A == 1]
                    # [max4e4p4ZA == 2]
                    # [ez4B == 1]
                    # [max4e4p4A==1][odd4Df%4 == 3][B**2 =[%(4*2**max4e4p4A)]= 4*odd4Df] =>  [B**2 =[%8]= 4][B%8 <- {2,6}][B%4 == 2]
                        # fix_bug_6neg4Deq52:goto
                    B6max4pow4p4ZA = 2
                        # the only solution
                B6max4pow4p4ZA
            else:
                # [ez4Df >= max4e4p4ZZA]
                # [2 <= max4e4p4ZZA <= 3]
                # [0 <= max4e4p4A <= 1]
                # [0 <= max4e4p4A <= [ez4Df==3]]
                assert max4e4p4A == 0 or max4e4p4A == 1 and ez4Df == 3
                # [Df%(4*2**max4e4p4A) == 0]
                # [B**2 =[%(4*2**max4e4p4A)]= 0]
                # [2*ez4B >= 2+max4e4p4A]
                # [ez4B >= 1+ceil(max4e4p4A/2)]
                # !! [0 <= max4e4p4A <= 1]
                # [ez4B >= 1+max4e4p4A]
                if 0:
                    min4ez4B = 1+max4e4p4A
                    ft4B = 1<<min4ez4B
                # [B%2**(1+max4e4p4A) <- ft4B*(all_uints%2**(max4e4p4A+1-min4ez4B))]
                # [B6max4pow4p4ZA <- ft4B*(all_uints%2**0)]
                B6max4pow4p4ZA = 0
                    # the only solution
            B6max4pow4p4ZA
        else:
            assert max4e4p4A == 1
            assert len(sqrts4D6p4A) == 1 # [0]
            B6max4pow4p4ZA = 0
                # the only solution
        B6max4pow4p4ZA
    else:
        # [Df%p =!= 0]
        B6max4pow4p4ZZA = sqrt_mod_coprime_power_(p4A, max4e4p4ZZA, Df, B6p4A)
            # Df%ZZA --> B%ZA
            # one of 1/2 solutions
            # bug:one of 1/2/4 solutions
            #   fix_bug_6neg4Deq71:goto
            # ^ValueError <<== sqrt_of_odd_mod_zpow_:『if not y&7 == 1:raise ValueError』
            #   fix_bug_6neg4Deq19:goto
        if p4A == 2:
            # fix_bug_6neg4Deq199:here
            pw = e2pow4p4ZA[max4e4p4ZA]
            B6max4pow4p4ZA = B6max4pow4p4ZZA -pw if B6max4pow4p4ZZA > pw else B6max4pow4p4ZZA
            assert B6max4pow4p4ZA < pw
        else:
            B6max4pow4p4ZA = B6max4pow4p4ZZA
        B6max4pow4p4ZZA
    B6max4pow4p4ZA
        # one of 1/2 solutions
        # bug:one of 1/2/4 solutions
        #   fix_bug_6neg4Deq71:goto
    assert 0 <= B6max4pow4p4ZA < e2pow4p4ZA[max4e4p4ZA], (Df, p4A, sqrts4D6p4A, max4e4p4A, B6max4pow4p4ZA, e2pow4p4ZA[max4e4p4ZA])
        # AssertionError: (-199, 2, [1], 3, 21, 16)
        #       @[D==-796][Df==-199]

    #e2Bs6pow4p4ZA = [[B6max4pow4p4ZA%pw] for pw in e2pow4p4ZA]
    e2Bs6pow4p4ZA = [[] for _ in range(0, 1+max4e4p4ZA)]
    _B6pow4p4ZA = B6max4pow4p4ZA
    for e4p4ZA in range(0, 1+max4e4p4ZA)[::-1]:
        _B6pow4p4ZA %= e2pow4p4ZA[e4p4ZA]
        e2Bs6pow4p4ZA[e4p4ZA].append(_B6pow4p4ZA)
    e2Bs6pow4p4ZA
        # init: one of 1/2 solutions
        # bug:init: one of 1/2/4 solutions
        #   fix_bug_6neg4Deq71:goto
    if p4A == 2:
        # 1 solution --> 1/2 solutions
        # bug:1 solution --> 1/2/4 solutions
        #   fix_bug_6neg4Deq71:goto
        assert B6p4A == 1 or B6max4pow4p4ZA in (0,2)
            # fix_bug_6neg4Deq52:goto

        for e4p4ZA in range(0, 1+max4e4p4ZA):
            pw = e2pow4p4ZA[e4p4ZA]
            [B0] = Bs = e2Bs6pow4p4ZA[e4p4ZA]
            if B0 == 0:continue
            if B6p4A == 0:
                # the only solution
                # fix_bug_6neg4Deq52:goto
                # fix_bug_6neg4Deq20:here
                #   fix bug: @[D==-20][Df==-20]
                continue
            hf = pw>>1 # MSB
            # MAYBE:[hf == 0]
            if B0 == hf:
                #if B0 == hf and B6p4A == 1:
                # fix_bug_6neg4Deq15:here
                continue
            if 1:
                # fix_bug_6neg4Deq71:here
                # !! B%(4*A) --> B%(2*A)
                # 1 solution --> 2 solutions
                B1 = pw -B0
                assert not B0 == B1
                Bs[:] = sorted([B0, B1])
            else:
                # bug:1 solution --> 2/4 solutions
                B3 = pw -B0
                B2 = hf ^ B0
                B1 = hf ^ B3
                #xxx:assert B0 < B1 < B2 < B3
                #xxx:Bs[:] = (B0, B1, B2, B3)
                Bs[:] = sorted({B0, B1, B2, B3})
                #assert len(Bs) == 4, (pw, B0, Bs)
                    # AssertionError: (4, 1, [1, 3])
                    #   @[D==-60][Df==-15]
    else:
        # 1 solution --> 1/2 solutions
        for e4p4ZA in range(0, 1+max4e4p4ZA):
            pw = e2pow4p4ZA[e4p4ZA]
            [B0] = Bs = e2Bs6pow4p4ZA[e4p4ZA]
            if B0 == 0:continue
            B1 = pw -B0
            assert not B0 == B1
            Bs[:] = sorted([B0, B1])

    e2Bs6pow4p4ZA

    e2sqrts6pow4p4ZA_4D6pow4p4ZZA = e2Bs6pow4p4ZA
    return e2sqrts6pow4p4ZA_4D6pow4p4ZZA


def _prepare7moduli_remainderss4CRT_(Df, j2p4A, j2max4e4p4A, j2e2pow4p4ZA, j2e2sqrts6pow4p4ZA_4D6pow4p4ZZA, A, j4p4A_e4p4A_pairs, /, *, verbose):
    ######################
    if not 'move to _prepare7p4A_sqrts4D_max4e4p_()' and A&1 == 1:
        # fix_bug_6neg4Deq3:here
        # fix bug: @[D==-12][Df==-3][A%2==1]
        # [A%2==1]
        if not j2p4A:
            assert -Df < 12, Df
            assert Df in (-3, -4, -7, -8, -11), Df
            j2p4A = [2]
            j2max4e4p4A = [0]
            j2e2pow4p4ZA = [[1, 2]]
            j2e2sqrts6pow4p4ZA_4D6pow4p4ZZA = [[[0], [Df&1]]]
        else:
            assert not -Df < 12, Df
            #assert not Df in (-3, -4, -7, -8, -11), Df
        assert j2p4A[0] == 2
        j4p4A_e4p4A_pairs = chain([(0, 0)], j4p4A_e4p4A_pairs)
    if A&1 == 1:
        # fix_bug_6neg4Deq3.part2:here
        j4p4A_e4p4A_pairs = chain([(0, 0)], j4p4A_e4p4A_pairs)
    ######################
    ZZA = A << 2
    ZA = A << 1
    moduli4CRT = []
    remainderss4CRT = []
    for j4p4A, e4p4A in j4p4A_e4p4A_pairs:
        p4A = j2p4A[j4p4A]
        #sqrts4D6p4A = j2sqrts4D6p4A[j4p4A]
        max4e4p4A = j2max4e4p4A[j4p4A]
        assert 1 <= e4p4A <= max4e4p4A or (p4A, e4p4A) == (2, 0)
        # to solve: [B**2 =[%(4*p4A**e4p4A)]= Df]
        e4p4ZZA = e4p4A +2*(p4A == 2)
        # to solve: [B**2 =[%p4A**e4p4ZZA]= Df]
        e4p4ZA = e4p4A +(p4A == 2)
        # to get: B%p**e4p4ZA
        pow4p4ZA = j2e2pow4p4ZA[j4p4A][e4p4ZA]
        ##################
        if 0b000 and verbose:
            xnms = parse_xnms_('(j2e2sqrts6pow4p4ZA_4D6pow4p4ZZA, j4p4A, e4p4ZA)')
            errshow_name_value_pairs_(xnms, (j2e2sqrts6pow4p4ZA_4D6pow4p4ZZA, j4p4A, e4p4ZA))
        ##################
        sqrts6pow4p4ZA_4D6pow4p4ZZA = j2e2sqrts6pow4p4ZA_4D6pow4p4ZZA[j4p4A][e4p4ZA]
        moduli4CRT.append(pow4p4ZA)
        remainderss4CRT.append(sqrts6pow4p4ZA_4D6pow4p4ZZA)
    moduli4CRT
    remainderss4CRT
    return (moduli4CRT, remainderss4CRT)

def _count_num_Bs6A_(A, slack_min4abs4B6A7noncoprime_ok, moduli4CRT, remainderss4CRT, /):
    '# [C >= A >= B > -A] to exclude:[C == A >= 0 > B > -A]'
    ZZA = A << 2
    ZA = A << 1
    #xxx:if A <= slack_min4C7noncoprime_ok:
    if 0 == slack_min4abs4B6A7noncoprime_ok:
        # [C >= A] for all B
        num_Bs6A = II(map(len, remainderss4CRT))
    else:
        CRT = get_CRT_type_(extended=False, ver='long_term')
        apply_CRT_ = CRT(moduli4CRT)
        Bs6A = []
        for remainders4CRT in product(*remainderss4CRT):
            sqrt6p4ZA_4D6ZZA = apply_CRT_(remainders4CRT)
                #TODO:递归:修剪
            # [0 <= sqrt6p4ZA_4D6ZZA < 2*A]
            B6A = sqrt6p4ZA_4D6ZZA -ZA*(sqrt6p4ZA_4D6ZZA > A)
            # [A >= B6A > -A]
            if abs(B6A) >= slack_min4abs4B6A7noncoprime_ok:
                # [C >= A]
                Bs6A.append(sqrt6p4ZA_4D6ZZA)
                # [C >= A >= B > -A]
                #   to exclude:[C == A >= 0 > B > -A]
        Bs6A
        num_Bs6A = len(Bs6A)
    num_Bs6A
    return num_Bs6A
def _count_num_bad_Bs6A__7CeqA_(Df, p2e4neg4Df, /):
    '[C == A >= 0 > B > -A][nonprimitive_ok:=True]'
    '<==> [C == A > B > 0][nonprimitive_ok:=True]'
    #fix_bug_6neg4Deq15__another:goto

    # [-D == 4*A**2 -B**2]
    # [-D == (2*A-B)*(2*A+B)]
    # [(2*A-B) =[%2]= (2*A+B)]
    # [(2*A-B)+(2*A+B) =[%4]= 0]

    if 0:
        #bug:@[D==Df==84]
        if Df&3 == 0: return 0
    if Df&15 == 8:
        #fix_bug_6neg4Deq84:here
        # [Df%16 == 8]
        assert Df&15 == 8
        # [{(2*A-B),(2*A+B)}%4 == {0,2}]
        # [(2*A-B)+(2*A+B) =[%4]= 2]
        # _L
        return 0
    if Df&15 == 12:
        # [Df///4 %4 == 3]
        squarefree = -(Df >> 2)
        p2e4squarefree = dict(p2e4neg4Df)
        777;del p2e4squarefree[2]
        # [squarefree == -Df///4]
        # [squarefree%4 == 1]
        # @u,v :=> [u*v == squarefree]
        # [u%4 == v%4 <- {1,3}]
        # [-Df == (2*u)*(2*v)]
        k = 2
        # [-Df == (k*u)*(k*v)]

    else:
        # [Df%4 == 1]
        assert Df&3 == 1
        # [is_squarefree_(-Df)]
        squarefree = -Df
        p2e4squarefree = p2e4neg4Df
        # [squarefree == -Df]
        # [squarefree%4 == 3]
        # @u,v :=> [u*v == squarefree]
        # [{u,v}%4 == {1,3}]
        # [-Df == (1*u)*(1*v)]
        k = 1
        # [-Df == (k*u)*(k*v)]
    k, squarefree, p2e4squarefree
    # [-Df == (k*u)*(k*v)]

    assert not p2e4squarefree or 1 == max(p2e4squarefree.values())
    ps = sorted(p2e4squarefree)
    it = iter_unsorted_squarefree_uints_(ps)
    sz = 0
    for u in it:
        v = perfect_div(squarefree, u)
        if not u < v:continue
        # [u < v]
        B = perfect_div((u-v)*k, 2)
        # [B < 0]
        A = perfect_div((u+v)*k, 4)
        # [A > 0]
        if A > -B:
            # [C == A > -B > 0 > B]
            # [C == A > -B > 0 > B > -A]
            # [C == A > 0 > B > -A]
            sz += 1
    return sz


def _iter_unsorted__A__j4p4A_e4p4A_pairs__pairs4Df__A_lt_(max1_A, j2p4A, j2max4e4p4A, /):
    assert max1_A >= 2
    # [max1_A >= 2]
    j4p4A_e4p4A_pairs = []
    def recur(j, A, /):
        # precondition:[A < max1_A]
        if j == len(j2p4A):
            yield (A, tuple(j4p4A_e4p4A_pairs))
            return
        p4A = j2p4A[j]
        max4e4p4A = j2max4e4p4A[j]
        jpp = 1+j
        if 1:
            e4p4A = 0
            yield from recur(jpp, A)

        j4p4A_e4p4A_pairs.append(...)
        for e4p4A in range(1, 1+max4e4p4A):
            A *= p4A
            777;j4p4A_e4p4A_pairs[-1] = (j, e4p4A)
            if not A < max1_A: break
            # [A < max1_A]
            yield from recur(jpp, A)
        j4p4A_e4p4A_pairs.pop()
    # !! [max1_A >= 2]
    # [1 < max1_A]
    return recur(0, 1)



























































































































































































__all__
if 1:from seed.math.BinaryQuadraticForm__7class_number import w5D_, hratio4class_number7Duu_, ratio4class_number7Duu_, hratio4pseudo_class_number7Duu_, ratio4pseudo_class_number7Duu_
    #internal
if 1:from seed.math.BinaryQuadraticForm__7class_number import is_negative_discriminant_, is_negative_fundamental_discriminant_
    #internal


if 1:from seed.math.BinaryQuadraticForm__7class_number import iter_class_numbers5neg_discriminants_, iter_class_numbers5neg_discriminants__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_, iter_class_numbers5neg_discriminants__7brute_force7count_primitive_binary_quadratic_forms7ratio7CRT_, iter_class_numbers5neg_discriminants__7brute_force7count_primitive_binary_quadratic_forms7ratio7sum_over_Df_
    #mainly for py_adhoc_call






from seed.math.BinaryQuadraticForm__7class_number import class_number5neg_discriminant__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_, iter_ABCs6Qfb5neg_discriminant__7brute_force7enumerate_primitive_binary_quadratic_forms7naive_



from seed.math.BinaryQuadraticForm__7class_number import class_number5neg_discriminant__7brute_force7count_primitive_binary_quadratic_forms7ratio7CRT_, class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7CRT_


from seed.math.BinaryQuadraticForm__7class_number import class_number5neg_discriminant__7brute_force7count_primitive_binary_quadratic_forms7ratio7sum_over_Df_, class_number5neg_fundamental_discriminant__7brute_force7count_primitive_binary_quadratic_forms7sum_over_Df_



from seed.math.BinaryQuadraticForm__7class_number import *
