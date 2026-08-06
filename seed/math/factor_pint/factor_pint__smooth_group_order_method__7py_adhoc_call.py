#TODO:goto
#发现冫平方因子使得群规模包含素幂的环乘阶:goto
#发现冫四次因子使得群规模直接包含该素因子:goto
#goto:分解M199失败
r'''[[[
e ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method__7py_adhoc_call.py
view ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method.py


[[
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   ,_iter_test4factor7bqf
    1
    4
    14
    20
    32
    44
    60
    72
    (901111, 35, (83, 83), (2, 13, 17, 37, 59, 1993), 193707721)


===
def iter_trials4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, k4D, min_A, bound4stage1, bound4stage2=None, may_reproduceable4exps6stage1=None, may_reproduceable4exps6stage2=None, /, *, scale4bound4stage2=100, used_As7reduced=None, quiet=False):

py_adhoc_call { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_trials4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**67)'  =35 =1 =1024 ='2**16'
    1:((701110, 35, (3, 3), (2, 2, 13, 17, 37, 59, 1993)), (1, 0, 1, []))
    2:((701110, 35, (13, 13), (2,)), (3846035596, 2, 961508899, [2, 2, 13, 17, 37, 59, 1993]))
    3:((701110, 35, (19, 19), ()), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    4:((701110, 35, (31, 31), ()), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    5:((701110, 35, (43, 43), ()), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    6:((701110, 35, (59, 59), ()), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    7:((701110, 35, (71, 71), ()), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    8:((901111, 35, (83, 83), (), 193707721), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    9:((901111, 35, (83, 83), (), 193707721), (7692071192, 3, 961508899, (2, 2, 2, 13, 17, 37, 59, 1993)))

===
py_adhoc_call { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   @trials4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**67)'  =35 =1 =1024 ='2**16'
    ((901111, 35, (83, 83), (), 193707721), (7692071192, 3, 961508899, (2, 2, 2, 13, 17, 37, 59, 1993)))

===
def iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_(n, emay_signed_prev_k4D__or__k4D__min_A__pairs, bound4stage1, bound4stage2=None, may_reproduceable4exps6stage1=None, may_reproduceable4exps6stage2=None, /, *, scale4bound4stage2=100, quiet_level=0):

py_adhoc_call { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**67)'  =... =1024 ='2**16'
    1:((301110, 1, (11, 11), (5, 5, 5, 13, 149, 11953)), (1, 0, 1, []))
    2:((901111, 1, (47, 47), (2,), 193707721), (2894120125, 0, 2894120125, [5, 5, 5, 13, 149, 11953]))
    3:((901111, 1, (47, 47), (2,), 193707721), (5788240250, 1, 2894120125, (2, 5, 5, 5, 13, 149, 11953)))
    4:((901111, 1, (47, 47), (2,), 193707721), (5788240250, 1, 2894120125, (2, 5, 5, 5, 13, 149, 11953)))
py_adhoc_call { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**67)'  =... =1024 ='2**16'  --quiet_level=1
    1:((901111, 1, (47, 47), (2,), 193707721), (5788240250, 1, 2894120125, (2, 5, 5, 5, 13, 149, 11953)))
    2:((901111, 1, (47, 47), (2,), 193707721), (5788240250, 1, 2894120125, (2, 5, 5, 5, 13, 149, 11953)))
py_adhoc_call { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**67)'  =... =1024 ='2**16'  --quiet_level=2
    1:((901111, 1, (47, 47), (2,), 193707721), (5788240250, 1, 2894120125, (2, 5, 5, 5, 13, 149, 11953)))
    2:((901111, 1, (47, 47), (2,), 193707721), (5788240250, 1, 2894120125, (2, 5, 5, 5, 13, 149, 11953)))
py_adhoc_call { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**67)'  =... =1024 ='2**16'  --quiet_level=3
    1:((901111, 1, (47, 47), (2,), 193707721), (5788240250, 1, 2894120125, (2, 5, 5, 5, 13, 149, 11953)))

===
signed_prev_k4D:
py_adhoc_call { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**67)'  =1 =1024 ='2**16'
    1:((201100, 3, (5, 5)), (1, 0, 1, []))
    2:((201100, 3, (5, 5)), (1, 0, 1, ()))
    3:((201100, 15, (11, 11)), (1, 0, 1, []))
    4:((201100, 15, (11, 11)), (1, 0, 1, ()))
    5:((201100, 5, (3, 3)), (1, 0, 1, []))
    6:((201100, 5, (3, 3)), (1, 0, 1, ()))
    7:((701110, 35, (3, 3), (2, 2, 13, 17, 37, 59, 1993)), (1, 0, 1, []))
    8:((701110, 35, (13, 13), (2,)), (3846035596, 2, 961508899, [2, 2, 13, 17, 37, 59, 1993]))
    9:((701110, 35, (19, 19), ()), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    10:((701110, 35, (31, 31), ()), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    11:((701110, 35, (43, 43), ()), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    12:((701110, 35, (59, 59), ()), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    13:((701110, 35, (71, 71), ()), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    14:((901111, 35, (83, 83), (), 193707721), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    15:((901111, 35, (83, 83), (), 193707721), (7692071192, 3, 961508899, (2, 2, 2, 13, 17, 37, 59, 1993)))
    16:((901111, 35, (83, 83), (), 193707721), (7692071192, 3, 961508899, (2, 2, 2, 13, 17, 37, 59, 1993)))

===
signed_prev_k4D:
py_adhoc_call { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**67)'  =35 =1024 ='2**16'
    1:((201100, 105, (13, 13)), (1, 0, 1, []))
    2:((201100, 105, (13, 13)), (1, 0, 1, ()))
    3:((201100, 21, (23, 23)), (1, 0, 1, []))
    4:((201100, 21, (23, 23)), (1, 0, 1, ()))
    5:((201100, 7, (5, 5)), (1, 0, 1, []))
    6:((201100, 7, (5, 5)), (1, 0, 1, ()))
    7:((201100, 77, (3, 3)), (1, 0, 1, []))
    8:((201100, 77, (3, 3)), (1, 0, 1, ()))
    9:((701110, 231, (13, 13), (2, 2, 3, 353, 35753)), (1, 0, 1, []))
    10:((301110, 231, (31, 31), (13,)), (151449708, 2, 37862427, [2, 2, 3, 353, 35753]))
    11:((701110, 231, (37, 37), ()), (1968846204, 2, 492211551, [2, 2, 3, 353, 35753, 13]))
    12:((701110, 231, (43, 43), ()), (1968846204, 2, 492211551, [2, 2, 3, 353, 35753, 13]))
    13:((701110, 231, (61, 61), ()), (1968846204, 2, 492211551, [2, 2, 3, 353, 35753, 13]))
    14:((701110, 231, (67, 67), ()), (1968846204, 2, 492211551, [2, 2, 3, 353, 35753, 13]))
    15:((901111, 231, (79, 79), (), 193707721), (1968846204, 2, 492211551, [2, 2, 3, 353, 35753, 13]))
    16:((901111, 231, (79, 79), (), 193707721), (1968846204, 2, 492211551, (2, 2, 3, 13, 353, 35753)))
    17:((901111, 231, (79, 79), (), 193707721), (1968846204, 2, 492211551, (2, 2, 3, 13, 353, 35753)))



===
signed_prev_k4D:
py_adhoc_call { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**67)'  =-35 =1024 ='2**16'
    1:((701110, 35, (3, 3), (2, 2, 13, 17, 37, 59, 1993)), (1, 0, 1, []))
    2:((701110, 35, (13, 13), (2,)), (3846035596, 2, 961508899, [2, 2, 13, 17, 37, 59, 1993]))
    3:((701110, 35, (19, 19), ()), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    4:((701110, 35, (31, 31), ()), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    5:((701110, 35, (43, 43), ()), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    6:((701110, 35, (59, 59), ()), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    7:((701110, 35, (71, 71), ()), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    8:((901111, 35, (83, 83), (), 193707721), (7692071192, 3, 961508899, [2, 2, 13, 17, 37, 59, 1993, 2]))
    9:((901111, 35, (83, 83), (), 193707721), (7692071192, 3, 961508899, (2, 2, 2, 13, 17, 37, 59, 1993)))
    10:((901111, 35, (83, 83), (), 193707721), (7692071192, 3, 961508899, (2, 2, 2, 13, 17, 37, 59, 1993)))



++kw:stop_if_found_exps7key
py_adhoc_call { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**67)'  =-35 =1024 ='2**16'  +stop_if_found_exps7key
    1:((701110, 35, (3, 3), (2, 2, 13, 17, 37, 59, 1993)), (1, 0, 1, []))
    2:((701110, 35, (13, 13), (2,)), (3846035596, 2, 961508899, [2, 2, 13, 17, 37, 59, 1993]))
    3:((701110, 35, (13, 13), (2,)), (3846035596, 2, 961508899, (2, 2, 13, 17, 37, 59, 1993)))



===
M67-->M1207:
py_adhoc_call { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**1207)'  =... =1024 ='2**16'
    1:((201100, 1, (11, 11)), (1, 0, 1, []))
    2:((201100, 1, (11, 11)), (1, 0, 1, ()))
    3:((201100, 3, (5, 5)), (1, 0, 1, []))
    4:((201100, 3, (5, 5)), (1, 0, 1, ()))
    5:((201100, 15, (11, 11)), (1, 0, 1, []))
    ... ...
    ... ...
    31:((201100, 11, (3, 3)), (1, 0, 1, []))
    32:((201100, 11, (3, 3)), (1, 0, 1, ()))
    33:((201100, 143, (3, 3)), (1, 0, 1, []))
    34:((201100, 143, (3, 3)), (1, 0, 1, ()))
    ^C KeyboardInterrupt
===
py_adhoc_call { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**1207)'  =... ='2**20'
    ^C KeyboardInterrupt
        ?why so slow?
===
py_adhoc_call { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**1207)'  =... ='2**12'  --case4xprimes=2
    ... ...
    ... ...
    50:((201100, 91, (11, 11)), (1, 0, 1, ()))
    51:((201100, 273, (5, 5)), (1, 0, 1, []))
    52:((201100, 273, (5, 5)), (1, 0, 1, ()))
    53:((201100, 1365, (11, 11)), (1, 0, 1, []))
    54:((201100, 1365, (11, 11)), (1, 0, 1, ()))
    ^C KeyboardInterrupt
py_adhoc_call { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**1207)'  =1365 ='2**12'  --case4xprimes=2
    TODO
===
]]
[[
view ../../python3_src/seed/math/factor_pint/database4factors4cyclotomic_numbers__7py_adhoc_call.py
    iter_collect_missing_orders7flatten_
    (3, 227, {227: 1}, 1012732682774617818194689795139806022588388002941405805166033661866962725148373553742636400886744464424956493)
CYC3_227=(-1+3**227)//2
===
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+3**227)//2'  =... ='2**12' ='2**16'  --case4xprimes=2
    ... ...
    540:((201100, 110055, (13, 13)), (1, 0, 1, ()))
    ^C KeyboardInterrupt

py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+3**227)//2'  =110055 ='2**12' ='2**16'  --case4xprimes=2
    # 三秒每试
    ... ...
    250:((201100, 636405, (13, 13)), (1, 0, 1, ()))
    ... ...
    440:((201100, 87087, (5, 5)), (1, 0, 1, ()))
    ^C KeyboardInterrupt

++kw:stop_if_found_exps7key
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+3**227)//2'  =87087 ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key
    ... ...
    392:((201100, 14325749295, (37, 37)), (1, 0, 1, ()))
    ... ...
    400:((201100, 220396143, (5, 5)), (1, 0, 1, ()))
    ^C KeyboardInterrupt

===
++kw:to_sorted_ks4D --> kw:case4ks4D
===
]]
[[
分解M199失败
成功分解:M67,M103,M109,CYC2_125
<<==:
view ../../python3_src/seed/math/factor_pint/DATA4TESTING.py
M67 --> M103,M109;M199,CYC2_125
===
2:103:2550183799
2:109:745988807
2:125:269089806001
2:199:164504919713

$ cyclotomic_number 2 125
CYC2_125 = 1267650638007162390353805312001
[CYC2_125 == ((-1+2^125)/(-1+2^25))]
[CYC2_125 == ((-1+2**125)//(-1+2**25))]

k4D{M103}:[4524261 == 3 *7 *17 *19 *23 *29]
    [4524261%8 == 5]
k4D{M109}:[4365515 == 5 *7 *11 *17 *23 *29]
    [4365515%8 == 3]



===
M103
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**103)'  =... ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key
    ... ...
    262:((201100, 6555, (7, 7)), (1, 0, 1, ()))
    20260804-19:57:47.280300+0800
    ... ...
    458:((201100, 10465, (11, 11)), (1, 0, 1, ()))
    20260804-20:06:55.035309+0800
    ... ...
    655:((901111, 4524261, (13, 13), (), 2550183799), (12651611289815906, 1, 6325805644907953, (2, 29, 1301, 2549, 3187, 20639)))
    20260804-20:16:05.046019+0800
    耗时:半小时
[4524261 == 3 *7 *17 *19 *23 *29]
===
M109
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**109)'  =... ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key
    20260804-20:44:03.201437+0800
    1:((201100, 1, (5, 5)), (1, 0, 1, []))
    20260804-20:44:06.037812+0800
    0:duration: 2.837321924045682 *(unit: 0:00:01)
    ... ...
    619:((901111, 4365515, (3, 3), (2, 3, 293, 563, 1201, 1693, 64663), 745988807), (130131693215396286, 1, 65065846607698143, (2, 3, 293, 563, 1201, 1693, 64663)))
    20260804-21:12:06.254811+0800
    耗时:半小时
[4365515 == 5 *7 *11 *17 *23 *29]
===
M199
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**199)'  =... ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key
    ... ...
    1134:((201100, 3530373, (5, 5)), (1, 0, 1, ()))
    20260804-22:26:27.355239+0800
    ... ...
    20260804-23:03:20.105976+0800
    1745:((201100, 13560547, (5, 5)), (1, 0, 1, []))
    20260804-23:03:22.356902+0800
    1744:duration: 2.2511495389044285 *(unit: 0:00:01)
    ... ...
    20260804-23:56:06.557673+0800
    2663:((201100, 715320815, (3, 3)), (1, 0, 1, []))
    20260804-23:56:08.829560+0800
    2662:duration: 2.272137539461255 *(unit: 0:00:01)
    ^C KeyboardInterrupt
        total::duration: 8878.291142683476 *(unit: 0:00:01)
    耗时:2.5小时?失败
===
M199
+to_sorted_ks4D --> kw:case4ks4D
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**199)'  =... ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=1 # +to_sorted_ks4D
    20260804-23:59:50.355936+0800
    1:((201100, 1, (13, 13)), (1, 0, 1, []))
    20260804-23:59:53.587040+0800
    ... ...
    20260805-01:41:24.606437+0800
    1795:((201100, 2215, (7, 7)), (1, 0, 1, []))
    20260805-01:41:26.873294+0800
    1794:duration: 2.2670876160264015 *(unit: 0:00:01)
    ^C KeyboardInterrupt
        total::duration: 6054.805520976894 *(unit: 0:00:01)
    耗时:1.5小时?失败
===
e ../../python3_src/seed/math/primality_test/SPRP_2357.py
++val@kw:case4xprimes:=2357
    但是 还是不如 [case4xprimes:=2]...5seq
===
M199
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**199)'  =2215 ='2**14' ='2**20'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=1 # +to_sorted_ks4D
    # 廿秒每试
    20260805-08:34:04.016349+0800
    ... ...
    20260805-09:16:35.498775+0800
    101:((201100, 2341, (7, 7)), (1, 0, 1, []))
    20260805-09:16:54.975264+0800
    100:duration: 19.476751615293324 *(unit: 0:00:01)
    ^C KeyboardInterrupt
        total::duration: 2559.671655151993 *(unit: 0:00:01)
    耗时:一小时?失败
===
DONE: kw:to_sorted_ks4D --> case4ks4D
M67
[case4ks4D:=2] #partial_squarefree
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='((-1+2**67))'  =... ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    0: ... ...
    20260805-11:47:34.892057+0800
    1:((301110, 1, (11, 11), (5, 5, 5, 13, 149, 11953)), (1, 0, 1, []))
    20260805-11:47:37.712346+0800
    0:duration: 2.821299691684544 *(unit: 0:00:01)
    1: ... ...
    20260805-11:47:37.712819+0800
    2:((901111, 1, (47, 47), (2,), 193707721), (2894120125, 0, 2894120125, [5, 5, 5, 13, 149, 11953]))
    20260805-11:47:37.735791+0800
    1:duration: 0.023305539041757584 *(unit: 0:00:01)
    2: ... ...
    20260805-11:47:37.736248+0800
    3:((901111, 1, (47, 47), (2,), 193707721), (2894120125, 0, 2894120125, (5, 5, 5, 13, 149, 11953)))
    20260805-11:47:37.736481+0800
    2:duration: 0.0004834616556763649 *(unit: 0:00:01)
    20260805-11:47:37.736627+0800
    total::duration: 2.9520923076197505 *(unit: 0:00:01)

===
TODO:尝试证明:『此方案无效:[D:=n2D_(k * n**2)]』

发现冫平方因子使得群规模包含素幂的环乘阶:here
    大概:
        sqrt(D)
        sqrt(u**2*k)
        u*sqrt(k)
        u**(p-1)%p == 1
<<==:
M67**2
    如果平方因子真的无效，那么群规模必定很小，就是不知道能否分开平方因子的不同素幂
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='((-1+2**67)**2)'  =... ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    0: ... ...
    20260805-22:23:30.162045+0800
    1:((201100, 1, (5, 5)), (1, 0, 1, []))
    20260805-22:23:32.721239+0800
    0:duration: 2.5596316922456026 *(unit: 0:00:01)
    1: ... ...
    20260805-22:23:32.721756+0800
    2:((201100, 1, (5, 5)), (1, 0, 1, ()))
    20260805-22:23:32.721959+0800
    1:duration: 0.00046223122626543045 *(unit: 0:00:01)
    2: ... ...
    20260805-22:23:32.722225+0800
    3:((701110, 3, (7, 7), (2, 3, 3, 3, 5, 29, 67, 2551, 2677, 8539)), (1, 0, 1, []))
    20260805-22:23:39.018648+0800
    2:duration: 6.296726461499929 *(unit: 0:00:01)
    3: ... ...
    20260805-22:23:39.019126+0800
    4:((901111, 3, (13, 13), (2,), 37522681175013841), (30591615221319330, 1, 15295807610659665, [2, 3, 3, 3, 5, 29, 67, 2551, 2677, 8539]))
    20260805-22:23:39.027321+0800
    3:duration: 0.008504538796842098 *(unit: 0:00:01)
    4: ... ...
    20260805-22:23:39.027761+0800
    5:((901111, 3, (13, 13), (2,), 37522681175013841), (30591615221319330, 1, 15295807610659665, (2, 3, 3, 3, 5, 29, 67, 2551, 2677, 8539)))
    20260805-22:23:39.028013+0800
    4:duration: 0.0005116919055581093 *(unit: 0:00:01)
    20260805-22:23:39.028204+0800
    total::duration: 8.890867384150624 *(unit: 0:00:01)

[37522681175013841 == 193707721**2]
2551, 2677, 8539
    这么说，[群规模{3*M67**2}%(P-1) == 0]
    [4*30591615221319330%(-1+193707721) == 0]
    [4*30591615221319330%(-1+761838257287) == 0]
    [(-1+193707721)*(-1+761838257287) == 8*9*67*30591615221319330]
view ../../python3_src/seed/math/factor_pint/DATA4TESTING.py
    M67 == -1+2**67
    [-1+2**67 == 147573952589676412927 == 193707721*761838257287]
    [193707721 == +1+2**3 * 3**3 *5 *67 *2677 == -1+2*13*7450297]
        #7450297:23bit
    [761838257287 == +1+2 *3**2 *29 *67 *2551 *8539 == -1+2**3 *67927 *1401943]
        #1401943:21bit

py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='((-1+2**67)**2)'  =3 ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    3:((901111, 5, (3, 3), (2, 3, 3, 3, 5, 29, 67, 2551, 2677, 8539), 37522681175013841), (30591615221319330, 1, 15295807610659665, (2, 3, 3, 3, 5, 29, 67, 2551, 2677, 8539)))
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='((-1+2**67)**2)'  =13 ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    ...失败:k<-{15,17,19,21,23,29,31}
    成功:33
    17:((301110, 33, (19, 19), (5,)), (6118323044263866, 1, 3059161522131933, (2, 3, 3, 3, 29, 67, 2551, 2677, 8539)))
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='((-1+2**67)**2)'  =33 ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    ...35,37,!39!
    7:((301110, 39, (11, 11), (3, 5)), (4078882029509244, 2, 1019720507377311, (2, 2, 3, 3, 29, 67, 2551, 2677, 8539)))
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='((-1+2**67)**2)'  =39 ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    13:((901111, 55, (7, 7), (2, 2, 2, 3, 3, 3, 5, 29, 67, 2551, 2677, 8539), 37522681175013841), (122366460885277320, 3, 15295807610659665, (2, 2, 2, 3, 3, 3, 5, 29, 67, 2551, 2677, 8539)))

[1019==+1+2*509]
[10007==+1+2*5003]
[100003==+1+2*3*7*2381]
[10000600009 == 100003**2]
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(100003**2 * 10007**4)'  =... ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    3:((901111, 1, (5, 5), (2, 2, 2, 3, 3, 139, 1087, 10007), 10000600009), (108863110872, 3, 13607888859, (2, 2, 2, 3, 3, 139, 1087, 10007)))
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(100003**2 * 10007**4)'  =1 ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    3:((901111, 3, (7, 7), (2, 2, 2, 3, 3, 7, 139, 2381, 10007), 10000600009), (1669200983352, 3, 208650122919, (2, 2, 2, 3, 3, 7, 139, 2381, 10007)))
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(100003**2 * 10007**4)'  =3 ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    7:((901111, 11, (3, 3), (2, 2, 3, 23, 139, 1087, 10007), 10000600009), (417308591676, 2, 104327147919, (2, 2, 3, 23, 139, 1087, 10007)))

py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(10007**2 * 1019**4)'  =... ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    3:((901111, 1, (5, 5), (2, 2, 2, 3, 3, 5, 17, 139, 1019), 100140049), (866842920, 3, 108355365, (2, 2, 2, 3, 3, 5, 17, 139, 1019)))
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(10007**2 * 1019**4)'  =1 ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    3:((901111, 3, (7, 7), (2, 2, 2, 3, 3, 17, 139, 1019), 100140049), (173368584, 3, 21671073, (2, 2, 2, 3, 3, 17, 139, 1019)))
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(10007**2 * 1019**4)'  =3 ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    3:((901111, 5, (3, 3), (2, 2, 5, 17, 1019, 5003), 100140049), (1733339380, 2, 433334845, (2, 2, 5, 17, 1019, 5003)))
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(10007**2 * 1019**2)'  =3 ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    3:((901111, 5, (3, 3), (2, 2, 5, 17, 5003), 1038361), (1701020, 2, 425255, (2, 2, 5, 17, 5003)))
发现冫四次因子使得群规模直接包含该素因子:here
    => 四次方方案:D{k*n**4} [pt0 **= n]
        ++kw:exp4pt0
    view ../../python3_src/seed/math/BinaryQuadraticForm.py
        实证:四次方因子=>群规模包含((P+(P%4-2))*P) ~= phi_(sqrt(P**4))
        实证:[0 == ((4*qfbclassno(-4*k*p^2))%(p+(p%4-2)*Jacobi_symbol(p,k)))]
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(10007 * 1019)**4'  =3 ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    7:((901111, 11, (5, 5), (2, 2, 2, 3), 1078193566321), (361437379185, 0, 361437379185, (3, 5, 17, 139, 1019, 10007)))
    四次方:对得上!!!
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(10007 * 1019)**3'  =... ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    3:((901111, 1, (23, 23), (2, 3, 83, 1019, 10007), 1058089859), (5078172234, 1, 2539086117, (2, 3, 83, 1019, 10007)))
    三次方:也对得上!!!
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(10007 * 1019)**2'  =... ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    3:((901111, 1, (5, 5), (2, 2, 2, 3, 3, 5, 17, 139), 1038361), (850680, 3, 106335, (2, 2, 2, 3, 3, 5, 17, 139)))
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(10007 * 1019)**2'  =1 ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    3:((901111, 3, (7, 7), (2, 2, 2, 3, 3, 17, 139), 1038361), (170136, 3, 21267, (2, 2, 2, 3, 3, 17, 139)))
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(10007 * 1019)**2'  =3 ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    3:((901111, 5, (3, 3), (2, 2, 5, 17, 5003), 1038361), (1701020, 2, 425255, (2, 2, 5, 17, 5003)))
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(10007 * 1019)**4'  =... ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2 --exp4pt0='10007*1019'
    3:((901111, 1, (5, 5), (2, 2, 2, 3, 3, 5, 17, 139), 1078193566321), (850680, 3, 106335, (2, 2, 2, 3, 3, 5, 17, 139)))
    四次方:对得上!!!
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='((-1+2**67)**4)'  =... ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2 --exp4pt0='(-1+2**67)'
    5:((901111, 3, (13, 13), (2,), 1407951602561738083485286541573281), (30591615221319330, 1, 15295807610659665, (2, 3, 3, 3, 5, 29, 67, 2551, 2677, 8539)))
    !!!四次方:对不上???
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='((-1+2**67)**4)'  =... ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2 --exp4pt0='1'
    ... ...
    18:((201100, 19, (5, 5)), (1, 0, 1, ()))
    KeyboardInterrupt
    全部失败:看来确实是包含((P-1)*P) == phi_(sqrt(P**4))
===
===
M199
[case4ks4D:=2] #partial_squarefree
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**199)'  =... ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    813:((201100, 1005, (13, 13)), (1, 0, 1, []))
    20260805-12:45:05.627542+0800
    812:duration: 2.2158618457615376 *(unit: 0:00:01)
    ... ...
    1299:((201100, 1599, (7, 7)), (1, 0, 1, []))
    20260805-13:31:09.638372+0800
    ... ...
    ^C KeyboardInterrupt
    耗时:一小时?失败
TODO:随机k4D起始值99999
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**199)'  =99999 ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    TODO

内建k4D有限序列:
[case4ks4D:=3] #builtin_data6zpow64
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**199)'  =... ='2**16' ='2**17'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=3
    20260805-21:51:05.382946+0800
    ... ...
    20260805-22:10:55.383969+0800
    55:((201100, 145, (7, 7)), (1, 0, 1, []))
    20260805-22:11:12.939073+0800
    54:duration: 17.555374385789037 *(unit: 0:00:01)
    ... ...
    20260805-22:14:05.137867+0800
    63:((201100, 247, (5, 5)), (1, 0, 1, []))
    20260805-22:14:22.245269+0800
    62:duration: 17.10760246310383 *(unit: 0:00:01)
    ... ...
    ... ...
    151:((201100, 16385, (3, 3)), (1, 0, 1, []))
    20260806-07:35:02.196596+0800
    150:duration: 17.39295130968094 *(unit: 0:00:01)
    ... ...
    20260806-07:50:38.434421+0800
    191:((201100, 117651, (11, 11)), (1, 0, 1, []))
    20260806-07:53:58.595360+0800
    190:duration: 26.677333309315145 *(unit: 0:00:01)
    ... ...
    20260806-08:50:46.243496+0800
    295:((201100, 14348909, (3, 3)), (1, 0, 1, []))
    20260806-08:51:03.953670+0800
    294:duration: 17.710454463027418 *(unit: 0:00:01)
    ... ...
    327:((201100, 60466177, (5, 5)), (1, 0, 1, []))
    ... ...
    367:((201100, 387420491, (3, 3)), (1, 0, 1, []))
    20260806-09:34:03.149058+0800
    ... ...
    20260806-10:37:50.827581+0800
    463:((201100, 34359738369, (7, 7)), (1, 0, 1, []))
    20260806-10:38:08.784071+0800
    462:duration: 17.95671746134758 *(unit: 0:00:01)
    ... ...
    549:((201100, 2821109907455, (3, 3)), (1, 0, 1, []))
    ... ...
    636:((201100, 106993205379077, (3, 3)), (1, 0, 1, ()))
    ... ...
    ... ...
    20260806-18:54:20.639415+0800
    884:((201100, 18446744073709551617, (3, 3)), (1, 0, 1, ()))
    20260806-18:54:20.639526+0800
    883:duration: 0.0003092307597398758 *(unit: 0:00:01)
    884: ... ...
    20260806-18:54:20.639715+0800
    885:None
    20260806-18:54:20.639983+0800
    884:duration: 0.0004096152260899544 *(unit: 0:00:01)
    20260806-18:54:20.640092+0800
    total::duration: 45928.721918737516 *(unit: 0:00:01)
    失败@builtin_data6zpow64 #442内建squarefree
TODO


===
CYC2_125
[case4ks4D:=2] #partial_squarefree
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='((-1+2**125)//(-1+2**25))'  =... ='2**12' ='2**16'  --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=2
    20260805-11:49:04.333533+0800
    1:((201100, 1, (5, 5)), (1, 0, 1, []))
    20260805-11:49:07.133400+0800
    0:duration: 2.800836537964642 *(unit: 0:00:01)
    ... ...
    ... ...
    20260805-11:52:56.241607+0800
    113:((501110, 137, (7, 7), ()), (3496424734760400, 4, 218526545922525, (2, 2, 2, 2, 3, 3, 5, 5, 17, 17, 47, 2153, 33211)))
    20260805-11:52:56.241824+0800
    112:duration: 0.0004276921972632408 *(unit: 0:00:01)
    20260805-11:52:56.241939+0800
    total::duration: 232.00228116754442 *(unit: 0:00:01)
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='((-1+2**125)//(-1+2**25))'  ='[(137,7)]' ='2**12' ='2**16'  --case4xprimes=2
    54:((901111, 137, (701, 701), (), 269089806001), (3496424734760400, 4, 218526545922525, (2, 2, 2, 2, 3, 3, 5, 5, 17, 17, 47, 2153, 33211)))
    total::duration: 8.431474693119526 *(unit: 0:00:01)
===
]]



#]]]'''#'''
