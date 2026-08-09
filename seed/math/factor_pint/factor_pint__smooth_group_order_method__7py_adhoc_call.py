#TODO:goto
#发现冫平方因子使得群规模包含素幂的环乘阶:goto
#发现冫四次因子使得群规模直接包含该素因子:goto
#goto:分解M199失败
#================================
r'''[[[
e ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method__7py_adhoc_call.py
view ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method.py

call7Qfb:here
call7Pmm_Qpp:goto

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
[[
再来分解M199:仍旧失败
++kw:imay_sz4giant_step, info8qfbclassno4D
===
[case4ks4D:=4] #chunk_sieve
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**199)'  =... ='2**12' --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=4 --imay_sz4giant_step='2**12'
    # 五秒每试@[min_num_fwd_giant_steps:=0]
    # 六秒每试@[min_num_fwd_giant_steps:=-sz4giant_step]
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**199)'  =... ='2**16' --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=4 --imay_sz4giant_step='2**16'
    # 五十秒每试@[min_num_fwd_giant_steps:=-sz4giant_step]
    15:((601100, 17, (3, 3)), (1, 0, 1, []))
    22:((601100, 23, (3, 3)), (1, 0, 1, ()))
    23:((601100, 29, (3, 3)), (1, 0, 1, []))
    total::duration: 1174.609374532476 *(unit: 0:00:01)
    ^C KeyboardInterrupt
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**199)'  =... ='2**8' --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=4 --imay_sz4giant_step='2**12'
    # 五秒每试
    288:((601100, 353, (3, 3)), (1, 0, 1, ()))
    407:((601100, 499, (29, 29)), (1, 0, 1, []))
    431:((601100, 533, (3, 3)), (1, 0, 1, []))
    ^C KeyboardInterrupt
===
M67
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='(-1+2**67)'  =... ='2**10' --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=4 --imay_sz4giant_step='2**12'
    3:((901111, 1, (47, 47), (2,), 193707721), (189920844962875, 0, 189920844962875, (5, 5, 5, 13, 149, 784391719)))
    total::duration: 3.7947811540216208 *(unit: 0:00:01)
===
CYC2_125
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='((-1+2**125)//(-1+2**25))'  =... ='2**10' --case4xprimes=2  +stop_if_found_exps7key --case4ks4D=4 --imay_sz4giant_step='2**12'
    17:((301110, 17, (11, 11), (7,)), (1226943705622131377516, 2, 306735926405532844379, (2, 2, 23, 293, 751, 60607902211511)))
    total::duration: 23.27026430889964 *(unit: 0:00:01)
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='((-1+2**125)//(-1+2**25))'  ='[(17,1+11)]' ='2**10' --case4xprimes=2 --case4ks4D=4 --imay_sz4giant_step='2**12' --exp4pt0='23*293*751*60607902211511'  -stop_if_found_exps7key
    8:((901111, 17, (53, 53), (), 269089806001), (84, 2, 21, (2, 2, 3, 7)))
    total::duration: 2.8339372305199504 *(unit: 0:00:01)
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='((-1+2**125)//(-1+2**25))'  ='[(17,1+53)]' ='2**10' --case4xprimes=2 --case4ks4D=4 --imay_sz4giant_step='2**12' --exp4pt0='3*7*23*293*751*60607902211511'  -stop_if_found_exps7key
    14:((901111, 17, (197, 197), (), 269089806001), (4, 2, 1, (2, 2)))
    total::duration: 2.994131077080965 *(unit: 0:00:01)

py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='((-1+2**125)//(-1+2**25))'  =17 =1+197 ='2**10' --case4xprimes=2  --imay_sz4giant_step='2**12' --exp4pt0='3*7*23*293*751*60607902211511'
    #意外:本意是使用iter_trials4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_
    #   但是 结果不错
    5:((901111, 969, (5, 5), (2, 2, 11, 19, 109, 137, 360470772823213), 269089806001), (4500112802275717213444, 2, 1125028200568929303361, (2, 2, 11, 19, 109, 137, 360470772823213)))
    total::duration: 15.08856061566621 *(unit: 0:00:01)

iter_trials4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_
py_adhoc_call7rest { +lineno +to_show_StopIteration_value  }  seed.math.factor_pint.factor_pint__smooth_group_order_method   ,iter_trials4factor_pint__smooth_group_order_method7ambiguous_BinaryQuadraticForm_ ='((-1+2**125)//(-1+2**25))'  =17 =1+197 ='2**10' --case4xprimes=2  --imay_sz4giant_step='2**12' --exp4pt0='3*7*23*293*751*60607902211511'
    4:((901111, 17, (277, 277), (), 269089806001), (4, 2, 1, (2, 2)))
    total::duration: 3.0814969995990396 *(unit: 0:00:01)

===
]]



#]]]'''#'''
#================================
r'''[[[

call7Pmm_Qpp:here
call7Qfb:goto

[[[
===


[[
def factor_pint__smooth_group_order_method7Pmm_(n, u0, bound4stage1, bound4stage2=None, /, *, more_info=False, detect_once6stage1=False, bound4pow4stage1=1, case4xprimes=2, max_size7dense=2049, max_size7physical=65537):
===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='17*31' =5  =2 =2 --bound4pow4stage1=16
    17
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='17*31' =5  =2 =2 --bound4pow4stage1=8
    0


===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='7*5' =2  =2 =3 --bound4pow4stage1=2 # +more_info +_debug7list_all
    7
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='7*5' =2  =2 =2 --bound4pow4stage1=2
    0



===
[M67 == -1+2**67 == 193707721*761838257287]
[193707721 == 1+2**3 * 3**3 *5 *67 *2677]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='-1+2**67' =5  =67 =2677 --bound4pow4stage1=1
    193707721
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='-1+2**67' =5  =67 =-1+2677 --bound4pow4stage1=1
    0
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='-1+2**67' =5  =-1+67 =2677 --bound4pow4stage1=1
    0



===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='13*37' =2  =4 =4
    13
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='13*37' =6  =4 =4
    37
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='13*37' =10  =4 =4
    (3,) # <<== [2,2,3]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Pmm_   ='13*37' =10  =2 =4
    (1, 2) # <<== [2]++[3]

===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   ,_iter_search_exceptional4factor_pint__smooth_group_order_method7Pmm_  ='13*37' ='range(13*37)'   =4 =4
    (1, (0,))
    (10, (3,))
    (11, (3,))
    (23, (3,))
    (29, (3,))
    (31, (2,))
    (45, (3,))
    (48, (3,))
    (63, (3,))
    (82, (3,))
    (84, (3,))
    (85, (3,))
    (88, (3,))
    (97, (3,))
    (100, (3,))
    (101, (3,))
    (119, (3,))
    (121, (3,))
    (134, (3,))
    (137, (3,))
    (140, (3,))
    (158, (3,))
    (159, (3,))
    (162, (3,))
    (171, (3,))
    (175, (3,))
    (193, (3,))
    (199, (3,))
    (211, (3,))
    (212, (3,))
    (214, (3,))
    (216, (2,))
    (230, (3,))
    (232, (3,))
    (236, (3,))
    (245, (3,))
    (249, (3,))
    (251, (3,))
    (265, (2,))
    (267, (3,))
    (269, (3,))
    (270, (3,))
    (282, (3,))
    (288, (3,))
    (306, (3,))
    (310, (3,))
    (319, (3,))
    (322, (3,))
    (323, (3,))
    (341, (3,))
    (344, (3,))
    (347, (3,))
    (360, (3,))
    (362, (3,))
    (380, (3,))
    (381, (3,))
    (384, (3,))
    (393, (3,))
    (396, (3,))
    (397, (3,))
    (399, (3,))
    (418, (3,))
    (433, (3,))
    (436, (3,))
    (450, (2,))
    (452, (3,))
    (458, (3,))
    (470, (3,))
    (471, (3,))
    (480, (1,))

===
]]
[[
===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =3   =2 =2 --bound4pow4stage1=4
    7
    # [D==B**2-4==5]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =3   =2 =2 --bound4pow4stage1=2
    0
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =5   =2 =2 +more_info
    (99001, 7, 'from:gcd(D,n) or gcd(B-2,n)')
    # [D==B**2-4==21]

py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =6   =2 =2 --bound4pow4stage1=32
    0
    # [D==B**2-4==32]
    # [Jacobi_symbol(7;32) == Jacobi_symbol(7;4) == +1]
    # [Jacobi_symbol(31;32) == Jacobi_symbol(31;1) == +1]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =6   =2 =2 --bound4pow4stage1=2
    0
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =6   =2 =3 --bound4pow4stage1=2
    7
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =6   =5 =5
    7
    #???31???

py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =8   =2 =2 --bound4pow4stage1=4
    31
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =8   =2 =2 --bound4pow4stage1=2
    0

py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =9   =2 =2 +more_info
    (99001, 7, 'from:gcd(D,n) or gcd(B-2,n)')

py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =12   =2 =2 +more_info
    (99001, 7, 'from:gcd(D,n) or gcd(B-2,n)')
    # [D==B**2-4==140]

py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =20   =2 =2 --bound4pow4stage1=16
    31
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =20   =2 =2 --bound4pow4stage1=8
    0
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =22   =2 =2 --bound4pow4stage1=16
    31
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='7*31' =22   =2 =2 --bound4pow4stage1=8
    0






===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =3   =4 =4
    23
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =6   =4 =4
    11
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =16   =4 =4
    (3,) # <<== [2,2,3]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =16   =3 =3
    0
    #???old:(2,) # <<== [2,3]
    #bug_fixed_1:goto
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =16   =2 =3
    0
    #???old:(1, 2) # <<== [2]++[3]
    #bug_fixed_1:goto

===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   ,_iter_search_exceptional4factor_pint__smooth_group_order_method7Qpp_  ='11*23' ='range(11*23)'   =4 =4
    (0, (2,))
    (1, (3,))
    (2, -1)
    (16, (3,))
    (39, (3,))
    (45, (3,))
    (76, (3,))
    (93, (3,))
    (116, (3,))
    (122, (3,))
    (131, (3,))
    (137, (3,))
    (160, (3,))
    (177, (3,))
    (208, (3,))
    (214, (3,))
    (237, (3,))
    (251, -1)
    (252, (3,))

===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =45   =4 =4
    (3,) # <<== [2,2,3]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =45   =3 =3
    (2,) # <<== [2,3]
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='11*23' =45   =2 =3
    (1, 2) # <<== [2]++[3]





===
[M67 == -1+2**67 == 193707721*761838257287]
[193707721 == -1+2*13*7450297]
    #7450297:23bit
[761838257287 == -1+2**3 *67927 *1401943]
    #1401943:21bit

? default('output,0)
? factorint(-1+2^53)~
[6361,69431,20394401;1,1,1]

? factorint(-1+20394401)~
[2,5,13,37,53;5,2,1,1,1]
? factorint(1+20394401)~
[2,3,7,277,1753;1,1,1,1,1]

? factorint(-1+69431)~
[2,5,53,131;1,1,1,1]
? factorint(1+69431)~
[2,3,11,263;3,1,1,1]

? factorint(-1+6361)~
[2,3,5,53;3,1,1,1]
? factorint(1+6361)~
[2,3181;1,1]


? factorint(1+2^54)~
[5,13,37,109,246241,279073;1,1,1,1,1,1]

? factorint(1+246241)~
[2,123121;1,1]
? factorint(-1+246241)~
[2,3,5,19;5,4,1,1]

? factorint(1+279073)~
[2,139537;1,1]
? factorint(-1+279073)~
[2,3,17,19;5,3,1,1]

===
? nextprime(2^54)
18014398509482143
iter_next_probable_primes ='2**54' | more

? factorint(1+18014398509482143)~
[2,7,11,179,3517,11613247;5,1,1,1,1,1]
? factorint(1+18014398509482147)~
[2,3,173,1721,5042101063;2,1,1,1,1]
? factorint(1+18014398509482171)~
[2,3,7,59,2683,2551369;2,3,1,2,1,1]
? factorint(1+18014398509482329)~
[2,5,1801439850948233;1,1,1]
? factorint(1+18014398509482357)~
[2,3,419,2161,3847,861941;1,1,1,1,1,1]
? factorint(1+18014398509482387)~
[2,3,13,103,13841173861;2,5,1,1,1]
? factorint(1+18014398509482399)~
[2,3,5,2663,3541,795997;5,1,2,1,1,1]
? factorint(1+18014398509482461)~
[2,40751,221030140481;1,1,1]
? factorint(1+18014398509482471)~
[2,3,1063033,706092791;3,1,1,1]
? factorint(1+18014398509482483)~
[2,3,29,229,521,10429,41603;2,1,1,1,1,1,1]
? factorint(1+18014398509482537)~
[2,3,131,22919082073133;1,1,1,1]
? factorint(1+18014398509482579)~
[2,3,5,269,1116133736647;2,1,1,1,1]
? factorint(1+18014398509482603)~
[2,3,166799986198913;2,3,1]
? factorint(1+18014398509482677)~
[2,283,1873,129281,131441;1,1,1,1,1]
? factorint(1+18014398509482693)~
[2,3,11,90981810653953;1,2,1,1]
? factorint(1+18014398509482723)~
[2,3,19,8011951,9861583;2,1,1,1,1]
? factorint(1+18014398509482839)~
[2,5,67,173,383,2153,47119;3,1,1,1,1,1,1]
? factorint(1+18014398509482863)~
[2,1125899906842679;4,1]


/,\d\{,5};
? factorint(1+18014398509482483)~
[2,3,29,229,521,10429,41603;2,1,1,1,1,1,1]
? factorint(1+18014398509482839)~
[2,5,67,173,383,2153,47119;3,1,1,1,1,1,1]

? factorint(-1+18014398509482483)~
[2,223,40391028048167;1,1,1]
? factorint(-1+18014398509482839)~
[2,3,17,19,293,36591421;1,2,3,1,1,1]

? 18014398509482483*18014398509482839
324518553658451118278737859609237
===
echo 333 | sed 's/[0-9]\+/a\0b/'
echo 333 | sed 's/[0-9]\+/factorint(1+\0)~/'
===
iter_next_probable_primes ='2**64' | sed 's/[0-9]\+/factorint(1+\0)~/' | more
default('output,0)
? factorint(1+18446744073709551629)~
[2,3,5,614891469123651721;1,1,1,1]
? factorint(1+18446744073709551653)~
[2,3,53,6689,257687,11218057;1,2,1,1,1,1]
? factorint(1+18446744073709551667)~
[2,4999,922521708027083;2,1,1]
? factorint(1+18446744073709551697)~
[2,7,8446117,156003590371;1,1,1,1]
? factorint(1+18446744073709551709)~
[2,5,11,431,389089729460231;1,1,1,1,1]
? factorint(1+18446744073709551757)~
[2,211,577,75758515912957;1,1,1,1]
? factorint(1+18446744073709551923)~
[2,3,15139,33846988414231;2,2,1,1]
? factorint(1+18446744073709551947)~
[2,3,1537228672809129329;2,1,1]
? factorint(1+18446744073709552009)~
[2,5,41,3259,4493,3072664103;1,1,1,1,1,1]
? factorint(1+18446744073709552109)~
[2,3,5,149,31034449,132974437;1,1,1,1,1,1]
? factorint(1+18446744073709552157)~
[2,3,31,11019560378560067;1,3,1,1]
? factorint(1+18446744073709552213)~
[2,10303,2224231,402481699;1,1,1,1]
? factorint(1+18446744073709552253)~
[2,3,23,134008211,997491553;1,1,1,1,1]
? factorint(1+18446744073709552267)~
[2,276091,2328281,7174177;2,1,1,1]
? factorint(1+18446744073709552333)~
[2,9223372036854776167;1,1]
? factorint(1+18446744073709552357)~
[2,281,4591,414809,17235661;1,1,1,1,1]
? factorint(1+18446744073709552361)~
[2,3,3074457345618258727;1,1,1]
? factorint(1+18446744073709552373)~
[2,3,163,698581537291129;1,4,1,1]

? factorint(1+18446744073709552421)~
[2,3,109,239,178127,662543381;1,1,1,1,1,1]
? factorint(1+18446744073709552423)~
[2,787,2929914878289319;3,1,1]
? factorint(1+18446744073709552501)~
[2,11,41,53,1760449,5346013;1,1,2,1,1,1]
? factorint(1+18446744073709552541)~
[2,3,340117,9039410983921;1,1,1,1]
? factorint(1+18446744073709552577)~
[2,3,29,47,3011,749138057891;1,1,1,1,1,1]
? factorint(1+18446744073709552597)~
[2,9223372036854776299;1,1]
? factorint(1+18446744073709552613)~
[2,3,13,59,389,106213,97016551;1,1,1,1,1,1,1]
? factorint(1+18446744073709552621)~
[2,7,23,97,383,2953,522191617;1,1,1,1,1,1,1]
? factorint(1+18446744073709552697)~
[2,3,61,622233828297563;1,5,1,1]
? factorint(1+18446744073709552729)~
[2,5,131,443,31786645656281;1,1,1,1,1]
? factorint(1+18446744073709552859)~
[2,3,5,7,47,2417,14319641971;2,4,1,1,1,1,1]
? factorint(1+18446744073709552901)~
[2,3,7,31,1567,5147,17713,99173;1,1,1,1,1,1,1,1]
? factorint(1+18446744073709552957)~
[2,7,17,3767,4007,26141,196429;1,1,1,1,1,1,1]
? factorint(1+18446744073709552969)~
[2,5,1844674407370955297;1,1,1]
? factorint(1+18446744073709553023)~
[2,19,211,35947914211987;7,1,1,1]
? factorint(1+18446744073709553029)~
[2,5,11,13,12899821030566121;1,1,1,1,1]
? factorint(1+18446744073709553033)~
[2,3,3074457345618258839;1,1,1]
? factorint(1+18446744073709553099)~
[2,3,5,19,29,6367,7457,123707;2,1,2,2,1,1,1,1]


/,\d\{,5};
? factorint(1+18446744073709552901)~
[2,3,7,31,1567,5147,17713,99173;1,1,1,1,1,1,1,1]

? factorint(-1+18446744073709552901)~
[2,5,13,103,239,257,9181,244297;2,2,1,1,1,1,1,1]


? 18014398509482483*18446744073709552901
332306998946238196299746630821333183

===
324518553658451118278737859609237
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='18014398509482483*18014398509482839' =3  =10429 =47119
    18014398509482483
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='18014398509482483*18014398509482839' =4  =10429 =47119
    18014398509482839

===
332306998946238196299746630821333183
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='18014398509482483*18446744073709552901' =3  =17713 =99173
    18014398509482483
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   @factor_pint__smooth_group_order_method7Qpp_  ='18014398509482483*18446744073709552901' =4  =17713 =99173
    18446744073709552901

py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   ,_iter_search_exceptional4factor_pint__smooth_group_order_method7Qpp_  ='18014398509482483*18446744073709552901' ='range(7,21)'  =17713 =99173
    <NONE>
    #十分稀罕，必须 mul_order4pt0{@p},mul_order4pt0{@q} 的 最大素因子 恰好相同

===
]]
[[
===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   ,stable_repr._iter_search_mul_order4X_4factor_pint__smooth_group_order_method7Qpp_  ='11*23' ='range(11*23)'
    (0, 4, {2: 2})
    (1, 3, {3: 1})
    (2, 506, {2: 1, 11: 1, 23: 1})
    (3, 120, {2: 3, 3: 1, 5: 1})
    (4, 110, {2: 1, 5: 1, 11: 1})
    (5, 24, {2: 3, 3: 1})
    (6, 132, {2: 2, 3: 1, 11: 1})
    (7, 60, {2: 2, 3: 1, 5: 1})
    (8, 120, {2: 3, 3: 1, 5: 1})
    (9, 11, {11: 1})
    (10, 66, {2: 1, 3: 1, 11: 1})
    (11, 44, {2: 2, 11: 1})
    (12, 33, {3: 1, 11: 1})
    (13, 22, {2: 1, 11: 1})
    (14, 110, {2: 1, 5: 1, 11: 1})
    (15, 120, {2: 3, 3: 1, 5: 1})
    (16, 12, {2: 2, 3: 1})
    (17, 132, {2: 2, 3: 1, 11: 1})
    (18, 40, {2: 3, 5: 1})
    (19, 55, {5: 1, 11: 1})
    (20, 264, {2: 3, 3: 1, 11: 1})
    (21, 138, {2: 1, 3: 1, 23: 1})
    (22, 12, {2: 2, 3: 1})
    (23, 12, {2: 2, 3: 1})
    (24, 66, {2: 1, 3: 1, 11: 1})
    (25, 230, {2: 1, 5: 1, 23: 1})
    (26, 120, {2: 3, 3: 1, 5: 1})
    (27, 132, {2: 2, 3: 1, 11: 1})
    (28, 24, {2: 3, 3: 1})
    (29, 110, {2: 1, 5: 1, 11: 1})
    (30, 60, {2: 2, 3: 1, 5: 1})
    (31, 264, {2: 3, 3: 1, 11: 1})
    (32, 66, {2: 1, 3: 1, 11: 1})
    (33, 44, {2: 2, 11: 1})
    (34, 66, {2: 1, 3: 1, 11: 1})
    (35, 22, {2: 1, 11: 1})
    (36, 110, {2: 1, 5: 1, 11: 1})
    (37, 110, {2: 1, 5: 1, 11: 1})
    (38, 24, {2: 3, 3: 1})
    (39, 12, {2: 2, 3: 1})
    (40, 110, {2: 1, 5: 1, 11: 1})
    (41, 40, {2: 3, 5: 1})
    (42, 11, {11: 1})
    (43, 24, {2: 3, 3: 1})
    (44, 92, {2: 2, 23: 1})
    (45, 6, {2: 1, 3: 1})
    (46, 44, {2: 2, 11: 1})
    (47, 30, {2: 1, 3: 1, 5: 1})
    (48, 230, {2: 1, 5: 1, 23: 1})
    (49, 24, {2: 3, 3: 1})
    (50, 132, {2: 2, 3: 1, 11: 1})
    (51, 40, {2: 3, 5: 1})
    (52, 110, {2: 1, 5: 1, 11: 1})
    (53, 132, {2: 2, 3: 1, 11: 1})
    (54, 24, {2: 3, 3: 1})
    (55, 44, {2: 2, 11: 1})
    (56, 66, {2: 1, 3: 1, 11: 1})
    (57, 22, {2: 1, 11: 1})
    (58, 110, {2: 1, 5: 1, 11: 1})
    (59, 55, {5: 1, 11: 1})
    (60, 132, {2: 2, 3: 1, 11: 1})
    (61, 24, {2: 3, 3: 1})
    (62, 60, {2: 2, 3: 1, 5: 1})
    (63, 55, {5: 1, 11: 1})
    (64, 88, {2: 3, 11: 1})
    (65, 66, {2: 1, 3: 1, 11: 1})
    (66, 24, {2: 3, 3: 1})
    (67, 69, {3: 1, 23: 1})
    (68, 66, {2: 1, 3: 1, 11: 1})
    (69, 20, {2: 2, 5: 1})
    (70, 15, {3: 1, 5: 1})
    (71, 276, {2: 2, 3: 1, 23: 1})
    (72, 24, {2: 3, 3: 1})
    (73, 110, {2: 1, 5: 1, 11: 1})
    (74, 40, {2: 3, 5: 1})
    (75, 22, {2: 1, 11: 1})
    (76, 12, {2: 2, 3: 1})
    (77, 24, {2: 3, 3: 1})
    (78, 33, {3: 1, 11: 1})
    (79, 22, {2: 1, 11: 1})
    (80, 110, {2: 1, 5: 1, 11: 1})
    (81, 55, {5: 1, 11: 1})
    (82, 132, {2: 2, 3: 1, 11: 1})
    (83, 132, {2: 2, 3: 1, 11: 1})
    (84, 120, {2: 3, 3: 1, 5: 1})
    (85, 60, {2: 2, 3: 1, 5: 1})
    (86, 11, {11: 1})
    (87, 24, {2: 3, 3: 1})
    (88, 44, {2: 2, 11: 1})
    (89, 24, {2: 3, 3: 1})
    (90, 506, {2: 1, 11: 1, 23: 1})
    (91, 30, {2: 1, 3: 1, 5: 1})
    (92, 20, {2: 2, 5: 1})
    (93, 12, {2: 2, 3: 1})
    (94, 276, {2: 2, 3: 1, 23: 1})
    (95, 120, {2: 3, 3: 1, 5: 1})
    (96, 110, {2: 1, 5: 1, 11: 1})
    (97, 88, {2: 3, 11: 1})
    (98, 66, {2: 1, 3: 1, 11: 1})
    (99, 12, {2: 2, 3: 1})
    (100, 24, {2: 3, 3: 1})
    (101, 22, {2: 1, 11: 1})
    (102, 110, {2: 1, 5: 1, 11: 1})
    (103, 110, {2: 1, 5: 1, 11: 1})
    (104, 132, {2: 2, 3: 1, 11: 1})
    (105, 132, {2: 2, 3: 1, 11: 1})
    (106, 110, {2: 1, 5: 1, 11: 1})
    (107, 120, {2: 3, 3: 1, 5: 1})
    (108, 132, {2: 2, 3: 1, 11: 1})
    (109, 66, {2: 1, 3: 1, 11: 1})
    (110, 8, {2: 3})
    (111, 33, {3: 1, 11: 1})
    (112, 264, {2: 3, 3: 1, 11: 1})
    (113, 230, {2: 1, 5: 1, 23: 1})
    (114, 30, {2: 1, 3: 1, 5: 1})
    (115, 12, {2: 2, 3: 1})
    (116, 12, {2: 2, 3: 1})
    (117, 230, {2: 1, 5: 1, 23: 1})
    (118, 120, {2: 3, 3: 1, 5: 1})
    (119, 22, {2: 1, 11: 1})
    (120, 24, {2: 3, 3: 1})
    (121, 44, {2: 2, 11: 1})
    (122, 12, {2: 2, 3: 1})
    (123, 264, {2: 3, 3: 1, 11: 1})
    (124, 110, {2: 1, 5: 1, 11: 1})
    (125, 110, {2: 1, 5: 1, 11: 1})
    (126, 132, {2: 2, 3: 1, 11: 1})
    (127, 132, {2: 2, 3: 1, 11: 1})
    (128, 110, {2: 1, 5: 1, 11: 1})
    (129, 110, {2: 1, 5: 1, 11: 1})
    (130, 264, {2: 3, 3: 1, 11: 1})
    (131, 12, {2: 2, 3: 1})
    (132, 44, {2: 2, 11: 1})
    (133, 24, {2: 3, 3: 1})
    (134, 22, {2: 1, 11: 1})
    (135, 120, {2: 3, 3: 1, 5: 1})
    (136, 115, {5: 1, 23: 1})
    (137, 12, {2: 2, 3: 1})
    (138, 12, {2: 2, 3: 1})
    (139, 30, {2: 1, 3: 1, 5: 1})
    (140, 230, {2: 1, 5: 1, 23: 1})
    (141, 264, {2: 3, 3: 1, 11: 1})
    (142, 66, {2: 1, 3: 1, 11: 1})
    (143, 8, {2: 3})
    (144, 66, {2: 1, 3: 1, 11: 1})
    (145, 132, {2: 2, 3: 1, 11: 1})
    (146, 120, {2: 3, 3: 1, 5: 1})
    (147, 55, {5: 1, 11: 1})
    (148, 132, {2: 2, 3: 1, 11: 1})
    (149, 132, {2: 2, 3: 1, 11: 1})
    (150, 110, {2: 1, 5: 1, 11: 1})
    (151, 55, {5: 1, 11: 1})
    (152, 22, {2: 1, 11: 1})
    (153, 24, {2: 3, 3: 1})
    (154, 12, {2: 2, 3: 1})
    (155, 33, {3: 1, 11: 1})
    (156, 88, {2: 3, 11: 1})
    (157, 110, {2: 1, 5: 1, 11: 1})
    (158, 120, {2: 3, 3: 1, 5: 1})
    (159, 276, {2: 2, 3: 1, 23: 1})
    (160, 12, {2: 2, 3: 1})
    (161, 20, {2: 2, 5: 1})
    (162, 15, {3: 1, 5: 1})
    (163, 506, {2: 1, 11: 1, 23: 1})
    (164, 24, {2: 3, 3: 1})
    (165, 44, {2: 2, 11: 1})
    (166, 24, {2: 3, 3: 1})
    (167, 22, {2: 1, 11: 1})
    (168, 60, {2: 2, 3: 1, 5: 1})
    (169, 120, {2: 3, 3: 1, 5: 1})
    (170, 132, {2: 2, 3: 1, 11: 1})
    (171, 132, {2: 2, 3: 1, 11: 1})
    (172, 110, {2: 1, 5: 1, 11: 1})
    (173, 55, {5: 1, 11: 1})
    (174, 11, {11: 1})
    (175, 66, {2: 1, 3: 1, 11: 1})
    (176, 24, {2: 3, 3: 1})
    (177, 12, {2: 2, 3: 1})
    (178, 22, {2: 1, 11: 1})
    (179, 40, {2: 3, 5: 1})
    (180, 55, {5: 1, 11: 1})
    (181, 24, {2: 3, 3: 1})
    (182, 276, {2: 2, 3: 1, 23: 1})
    (183, 30, {2: 1, 3: 1, 5: 1})
    (184, 20, {2: 2, 5: 1})
    (185, 33, {3: 1, 11: 1})
    (186, 138, {2: 1, 3: 1, 23: 1})
    (187, 24, {2: 3, 3: 1})
    (188, 66, {2: 1, 3: 1, 11: 1})
    (189, 88, {2: 3, 11: 1})
    (190, 110, {2: 1, 5: 1, 11: 1})
    (191, 60, {2: 2, 3: 1, 5: 1})
    (192, 24, {2: 3, 3: 1})
    (193, 132, {2: 2, 3: 1, 11: 1})
    (194, 110, {2: 1, 5: 1, 11: 1})
    (195, 110, {2: 1, 5: 1, 11: 1})
    (196, 11, {11: 1})
    (197, 66, {2: 1, 3: 1, 11: 1})
    (198, 44, {2: 2, 11: 1})
    (199, 24, {2: 3, 3: 1})
    (200, 132, {2: 2, 3: 1, 11: 1})
    (201, 110, {2: 1, 5: 1, 11: 1})
    (202, 40, {2: 3, 5: 1})
    (203, 132, {2: 2, 3: 1, 11: 1})
    (204, 24, {2: 3, 3: 1})
    (205, 230, {2: 1, 5: 1, 23: 1})
    (206, 30, {2: 1, 3: 1, 5: 1})
    (207, 44, {2: 2, 11: 1})
    (208, 6, {2: 1, 3: 1})
    (209, 92, {2: 2, 23: 1})
    (210, 24, {2: 3, 3: 1})
    (211, 22, {2: 1, 11: 1})
    (212, 40, {2: 3, 5: 1})
    (213, 110, {2: 1, 5: 1, 11: 1})
    (214, 12, {2: 2, 3: 1})
    (215, 24, {2: 3, 3: 1})
    (216, 110, {2: 1, 5: 1, 11: 1})
    (217, 110, {2: 1, 5: 1, 11: 1})
    (218, 22, {2: 1, 11: 1})
    (219, 66, {2: 1, 3: 1, 11: 1})
    (220, 44, {2: 2, 11: 1})
    (221, 66, {2: 1, 3: 1, 11: 1})
    (222, 264, {2: 3, 3: 1, 11: 1})
    (223, 60, {2: 2, 3: 1, 5: 1})
    (224, 55, {5: 1, 11: 1})
    (225, 24, {2: 3, 3: 1})
    (226, 132, {2: 2, 3: 1, 11: 1})
    (227, 120, {2: 3, 3: 1, 5: 1})
    (228, 115, {5: 1, 23: 1})
    (229, 66, {2: 1, 3: 1, 11: 1})
    (230, 12, {2: 2, 3: 1})
    (231, 12, {2: 2, 3: 1})
    (232, 138, {2: 1, 3: 1, 23: 1})
    (233, 264, {2: 3, 3: 1, 11: 1})
    (234, 110, {2: 1, 5: 1, 11: 1})
    (235, 40, {2: 3, 5: 1})
    (236, 132, {2: 2, 3: 1, 11: 1})
    (237, 12, {2: 2, 3: 1})
    (238, 120, {2: 3, 3: 1, 5: 1})
    (239, 55, {5: 1, 11: 1})
    (240, 22, {2: 1, 11: 1})
    (241, 66, {2: 1, 3: 1, 11: 1})
    (242, 44, {2: 2, 11: 1})
    (243, 33, {3: 1, 11: 1})
    (244, 22, {2: 1, 11: 1})
    (245, 120, {2: 3, 3: 1, 5: 1})
    (246, 60, {2: 2, 3: 1, 5: 1})
    (247, 132, {2: 2, 3: 1, 11: 1})
    (248, 24, {2: 3, 3: 1})
    (249, 110, {2: 1, 5: 1, 11: 1})
    (250, 120, {2: 3, 3: 1, 5: 1})
    (251, 253, {11: 1, 23: 1})
    (252, 6, {2: 1, 3: 1})

===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   ,stable_repr._iter_search_mul_order4X_4factor_pint__smooth_group_order_method7Qpp_  ='11*23' ='range(11*23)' | grep '[0-9][0-9]:' -v | lineno1
    1:(0, 4, {2: 2})
    2:(1, 3, {3: 1})
    3:(3, 120, {2: 3, 3: 1, 5: 1})
    4:(5, 24, {2: 3, 3: 1})
    5:(7, 60, {2: 2, 3: 1, 5: 1})
    6:(8, 120, {2: 3, 3: 1, 5: 1})
    7:(15, 120, {2: 3, 3: 1, 5: 1})
    8:(16, 12, {2: 2, 3: 1})
    9:(18, 40, {2: 3, 5: 1})
    10:(22, 12, {2: 2, 3: 1})
    11:(23, 12, {2: 2, 3: 1})
    12:(26, 120, {2: 3, 3: 1, 5: 1})
    13:(28, 24, {2: 3, 3: 1})
    14:(30, 60, {2: 2, 3: 1, 5: 1})
    15:(38, 24, {2: 3, 3: 1})
    16:(39, 12, {2: 2, 3: 1})
    17:(41, 40, {2: 3, 5: 1})
    18:(43, 24, {2: 3, 3: 1})
    19:(45, 6, {2: 1, 3: 1})
    20:(47, 30, {2: 1, 3: 1, 5: 1})
    21:(49, 24, {2: 3, 3: 1})
    22:(51, 40, {2: 3, 5: 1})
    23:(54, 24, {2: 3, 3: 1})
    24:(61, 24, {2: 3, 3: 1})
    25:(62, 60, {2: 2, 3: 1, 5: 1})
    26:(66, 24, {2: 3, 3: 1})
    27:(69, 20, {2: 2, 5: 1})
    28:(70, 15, {3: 1, 5: 1})
    29:(72, 24, {2: 3, 3: 1})
    30:(74, 40, {2: 3, 5: 1})
    31:(76, 12, {2: 2, 3: 1})
    32:(77, 24, {2: 3, 3: 1})
    33:(84, 120, {2: 3, 3: 1, 5: 1})
    34:(85, 60, {2: 2, 3: 1, 5: 1})
    35:(87, 24, {2: 3, 3: 1})
    36:(89, 24, {2: 3, 3: 1})
    37:(91, 30, {2: 1, 3: 1, 5: 1})
    38:(92, 20, {2: 2, 5: 1})
    39:(93, 12, {2: 2, 3: 1})
    40:(95, 120, {2: 3, 3: 1, 5: 1})
    41:(99, 12, {2: 2, 3: 1})
    42:(100, 24, {2: 3, 3: 1})
    43:(107, 120, {2: 3, 3: 1, 5: 1})
    44:(110, 8, {2: 3})
    45:(114, 30, {2: 1, 3: 1, 5: 1})
    46:(115, 12, {2: 2, 3: 1})
    47:(116, 12, {2: 2, 3: 1})
    48:(118, 120, {2: 3, 3: 1, 5: 1})
    49:(120, 24, {2: 3, 3: 1})
    50:(122, 12, {2: 2, 3: 1})
    51:(131, 12, {2: 2, 3: 1})
    52:(133, 24, {2: 3, 3: 1})
    53:(135, 120, {2: 3, 3: 1, 5: 1})
    54:(137, 12, {2: 2, 3: 1})
    55:(138, 12, {2: 2, 3: 1})
    56:(139, 30, {2: 1, 3: 1, 5: 1})
    57:(143, 8, {2: 3})
    58:(146, 120, {2: 3, 3: 1, 5: 1})
    59:(153, 24, {2: 3, 3: 1})
    60:(154, 12, {2: 2, 3: 1})
    61:(158, 120, {2: 3, 3: 1, 5: 1})
    62:(160, 12, {2: 2, 3: 1})
    63:(161, 20, {2: 2, 5: 1})
    64:(162, 15, {3: 1, 5: 1})
    65:(164, 24, {2: 3, 3: 1})
    66:(166, 24, {2: 3, 3: 1})
    67:(168, 60, {2: 2, 3: 1, 5: 1})
    68:(169, 120, {2: 3, 3: 1, 5: 1})
    69:(176, 24, {2: 3, 3: 1})
    70:(177, 12, {2: 2, 3: 1})
    71:(179, 40, {2: 3, 5: 1})
    72:(181, 24, {2: 3, 3: 1})
    73:(183, 30, {2: 1, 3: 1, 5: 1})
    74:(184, 20, {2: 2, 5: 1})
    75:(187, 24, {2: 3, 3: 1})
    76:(191, 60, {2: 2, 3: 1, 5: 1})
    77:(192, 24, {2: 3, 3: 1})
    78:(199, 24, {2: 3, 3: 1})
    79:(202, 40, {2: 3, 5: 1})
    80:(204, 24, {2: 3, 3: 1})
    81:(206, 30, {2: 1, 3: 1, 5: 1})
    82:(208, 6, {2: 1, 3: 1})
    83:(210, 24, {2: 3, 3: 1})
    84:(212, 40, {2: 3, 5: 1})
    85:(214, 12, {2: 2, 3: 1})
    86:(215, 24, {2: 3, 3: 1})
    87:(223, 60, {2: 2, 3: 1, 5: 1})
    88:(225, 24, {2: 3, 3: 1})
    89:(227, 120, {2: 3, 3: 1, 5: 1})
    90:(230, 12, {2: 2, 3: 1})
    91:(231, 12, {2: 2, 3: 1})
    92:(235, 40, {2: 3, 5: 1})
    93:(237, 12, {2: 2, 3: 1})
    94:(238, 120, {2: 3, 3: 1, 5: 1})
    95:(245, 120, {2: 3, 3: 1, 5: 1})
    96:(246, 60, {2: 2, 3: 1, 5: 1})
    97:(248, 24, {2: 3, 3: 1})
    98:(250, 120, {2: 3, 3: 1, 5: 1})
    99:(252, 6, {2: 1, 3: 1})

===
py_adhoc_call   seed.math.factor_pint.factor_pint__smooth_group_order_method   ,stable_repr._iter_search_mul_order4X_4factor_pint__smooth_group_order_method7Qpp_  ='11*23' ='range(11*23)' | grep '[0-9][0-9]:\|[4-9]:' -v | lineno1
    # [55 == 253/4.6]
    1:(0, 4, {2: 2})
    2:(1, 3, {3: 1})
    3:(5, 24, {2: 3, 3: 1})
    4:(16, 12, {2: 2, 3: 1})
    5:(22, 12, {2: 2, 3: 1})
    6:(23, 12, {2: 2, 3: 1})
    7:(28, 24, {2: 3, 3: 1})
    8:(38, 24, {2: 3, 3: 1})
    9:(39, 12, {2: 2, 3: 1})
    10:(43, 24, {2: 3, 3: 1})
    11:(45, 6, {2: 1, 3: 1})
    12:(49, 24, {2: 3, 3: 1})
    13:(54, 24, {2: 3, 3: 1})
    14:(61, 24, {2: 3, 3: 1})
    15:(66, 24, {2: 3, 3: 1})
    16:(72, 24, {2: 3, 3: 1})
    17:(76, 12, {2: 2, 3: 1})
    18:(77, 24, {2: 3, 3: 1})
    19:(87, 24, {2: 3, 3: 1})
    20:(89, 24, {2: 3, 3: 1})
    21:(93, 12, {2: 2, 3: 1})
    22:(99, 12, {2: 2, 3: 1})
    23:(100, 24, {2: 3, 3: 1})
    24:(110, 8, {2: 3})
    25:(115, 12, {2: 2, 3: 1})
    26:(116, 12, {2: 2, 3: 1})
    27:(120, 24, {2: 3, 3: 1})
    28:(122, 12, {2: 2, 3: 1})
    29:(131, 12, {2: 2, 3: 1})
    30:(133, 24, {2: 3, 3: 1})
    31:(137, 12, {2: 2, 3: 1})
    32:(138, 12, {2: 2, 3: 1})
    33:(143, 8, {2: 3})
    34:(153, 24, {2: 3, 3: 1})
    35:(154, 12, {2: 2, 3: 1})
    36:(160, 12, {2: 2, 3: 1})
    37:(164, 24, {2: 3, 3: 1})
    38:(166, 24, {2: 3, 3: 1})
    39:(176, 24, {2: 3, 3: 1})
    40:(177, 12, {2: 2, 3: 1})
    41:(181, 24, {2: 3, 3: 1})
    42:(187, 24, {2: 3, 3: 1})
    43:(192, 24, {2: 3, 3: 1})
    44:(199, 24, {2: 3, 3: 1})
    45:(204, 24, {2: 3, 3: 1})
    46:(208, 6, {2: 1, 3: 1})
    47:(210, 24, {2: 3, 3: 1})
    48:(214, 12, {2: 2, 3: 1})
    49:(215, 24, {2: 3, 3: 1})
    50:(225, 24, {2: 3, 3: 1})
    51:(230, 12, {2: 2, 3: 1})
    52:(231, 12, {2: 2, 3: 1})
    53:(237, 12, {2: 2, 3: 1})
    54:(248, 24, {2: 3, 3: 1})
    55:(252, 6, {2: 1, 3: 1})

===
]]

===
]]]

#]]]'''#'''
#================================
