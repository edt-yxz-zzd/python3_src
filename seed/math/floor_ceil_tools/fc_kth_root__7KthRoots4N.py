#__all__:goto
r'''[[[
e ../../python3_src/seed/math/floor_ceil_tools/fc_kth_root__7KthRoots4N.py

seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N
py -m nn_ns.app.debug_cmd   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N:__doc__ -ht # -ff -df
#######

[[
move_from:
view ../../python3_src/seed/math/primality_test/reproduceable7probable_primes.py

come_from:
view ../../python3_src/seed/math/BinaryQuadraticForm__7class_number.py
]]


'#'; __doc__ = r'#'

>>> list_all_floor_kth_root_until_diff_lt_(0, 2**16)
[(1, 65536), (2, 256), (3, 40), (4, 16), (5, 9), (6, 6), (7, 4), (8, 4), (9, 3), (10, 3), (11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (17, 1)]

>>> list_all_floor_kth_root_until_diff_lt_(1, 2**16)
[(1, 65536), (2, 256), (3, 40), (4, 16), (5, 9), (6, 6), (7, 4)]

>>> list_all_floor_kth_root_until_diff_lt_(1, 2**256)   #doctest: +ELLIPSIS
[..., (40, 84), (41, 75), (42, 68), (43, 61), (44, 56), (45, 51), (46, 47), (47, 43), (48, 40), (49, 37), (50, 34), (51, 32), (52, 30), (53, 28), (54, 26), (55, 25), (56, 23), (57, 22), (58, 21), (59, 20), (60, 19), (61, 18), (62, 17), (63, 16)]

>>> #see:_ns2ks_(): [n:=2**256]->[估值:k==25] 实际k应当是26
>>> list_all_floor_kth_root_until_diff_lt_(4, 2**256)   #doctest: +ELLIPSIS
[..., (19, 11375), (20, 7131), (21, 4674), (22, 3183), (23, 2241), (24, 1625), (25, 1209), (26, 920), (27, 714), ..., (40, 84), (41, 75), (42, 68), (43, 61), (44, 56), (45, 51), (46, 47), (47, 43)]
>>> list_all_floor_kth_root_until_diff_lt_(..., 2**256)   #doctest: +ELLIPSIS
[..., (43, 61), (44, 56), (45, 51)]





>>> KthRoots4N(200)
KthRoots4N(200)
>>> KthRoots4N(200).validate()
>>> u = 1<<120
>>> for n in [-1+u, u, 1+u]:KthRoots4N(n).validate()





estimate_k4N_where_diff_kth_root4N_kppth_root4N_lt1:goto
estimate_k4N_where_diff_kth_root4N_kppth_root4N_ltB:goto
estimate_k4N_where_diff_kth_root4N_kppth_root4N_lt_given_bound:goto
py_adhoc_call__7list_all_floor_kth_root_until_diff_lt_:goto
py_adhoc_call__7_ns2ks_:goto

py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @f
from seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N import *
]]]'''#'''
__all__ = r'''
KthRoots4N
    list_all_floor_kth_root_until_diff_lt_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_int_ge
    from seed.helper.repr_input import repr_helper
    from seed.math.floor_ceil_tools.fc_log import floor_log_, floor_log2, ceil_log2
    from seed.math.floor_ceil_tools.fc_kth_root import floor_sqrt, ceil_sqrt, floor_kth_root_, ceil_kth_root_
    from bisect import bisect_right, bisect_left
    from itertools import pairwise
from weakref import WeakValueDictionary
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


r'''[[[
%s/seed\.math\.primality_test\.reproduceable7probable_primes/seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N

[[
py_adhoc_call__7list_all_floor_kth_root_until_diff_lt_:here

py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =0 ='2**16'
py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =1 ='2**16'
py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =1 ='2**256'
py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =4 ='2**256'
py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =... ='2**256'
py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =4 ='2**2048'
[..., (256, 256), (257, 250), (258, 245), (259, 240), (260, 235), (261, 230), (262, 225), (263, 220), (264, 216), (265, 212), (266, 207), (267, 203), (268, 199), (269, 195)]
py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =... ='2**2048'
[..., (244, 336), (245, 328), (246, 320)]

py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =4 ='(2**10)**(2**10)'
[..., (1024, 1024), (1025, 1017), (1026, 1010), (1027, 1003), (1028, 996), (1029, 990), (1030, 983), (1031, 976), (1032, 970), (1033, 963), (1034, 957), (1035, 951), (1036, 944), (1037, 938), (1038, 932), (1039, 926), (1040, 920), (1041, 914), (1042, 908), (1043, 902), (1044, 896), (1045, 890), (1046, 885), (1047, 879), (1048, 873), (1049, 868), (1050, 862), (1051, 856), (1052, 851), (1053, 846), (1054, 840), (1055, 835), (1056, 830), (1057, 824), (1058, 819), (1059, 814), (1060, 809), (1061, 804), (1062, 799), (1063, 794), (1064, 789), (1065, 784), (1066, 779), (1067, 774), (1068, 769), (1069, 764), (1070, 760), (1071, 755), (1072, 750), (1073, 746), (1074, 741), (1075, 737), (1076, 732), (1077, 728), (1078, 723), (1079, 719), (1080, 714), (1081, 710), (1082, 706), (1083, 701), (1084, 697), (1085, 693), (1086, 689), (1087, 685), (1088, 681), (1089, 677), (1090, 673), (1091, 669), (1092, 665), (1093, 661), (1094, 657), (1095, 653), (1096, 649), (1097, 645), (1098, 641)]

py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =4 ='(2**12)**(2**12)'
    ^ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =4 ='2**2048' --min_k='2**8'
py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =4 ='(2**12)**(2**12)' --min_k='2**12'
[(4096, 4096), (4097, 4087), (4098, 4079), (4099, 4071), (4100, 4062), (4101, 4054), ..., (4400, 2305), (4401, 2301), (4402, 2297), (4403, 2293), (4404, 2289), (4405, 2285), (4406, 2281), (4407, 2277), (4408, 2273), (4409, 2269), (4410, 2265), (4411, 2261), (4412, 2257), (4413, 2253), (4414, 2249), (4415, 2245), (4416, 2241), (4417, 2237), (4418, 2233)]
py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =12 ='(2**12)**(2**12)' --min_k='2**12'
[(4096, 4096)]
py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =12 ='(2**12)**(2**12)' --min_k='2**11'
[(2048, 16777216), (2049, 16641555), (2050, 16507123), (2051, 16373905), (2052, 16241892), ..., (3947, 5606), (3948, 5594), (3949, 5582), (3950, 5570), (3951, 5558), (3952, 5546), (3953, 5533), (3954, 5521), (3955, 5509), (3956, 5497), (3957, 5485)]
py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ ='2**12' ='(2**12)**(2**12)' --min_k='2**11'
[(2048, 16777216), (2049, 16641555), (2050, 16507123), (2051, 16373905), (2052, 16241892), ..., (2499, 833410), (2500, 828877), (2501, 824373), (2502, 819897), (2503, 815449), (2504, 811028), (2505, 806635), (2506, 802269), (2507, 797930), (2508, 793618), (2509, 789333), (2510, 785074), (2511, 780842), (2512, 776635), (2513, 772455), (2514, 768301), (2515, 764172), (2516, 760069)]
py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ ='12*2**12' ='(2**12)**(2**12)' --min_k='2**11'
[(2048, 16777216), (2049, 16641555), (2050, 16507123), (2051, 16373905), (2052, 16241892), ..., (2150, 7620188), (2151, 7564257), (2152, 7508788), (2153, 7453776), (2154, 7399218), (2155, 7345110), (2156, 7291446), (2157, 7238224), (2158, 7185439), (2159, 7133088), (2160, 7081166), (2161, 7029669), (2162, 6978594), (2163, 6927937), (2164, 6877694), (2165, 6827861), (2166, 6778434)]

py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =16 ='(2**16)**(2**16)' --min_k='2**16'
[(65536, 65536)]
py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =16 ='(2**16)**(2**16)' --min_k='2**16-1024'
[(64512, 78150)]
py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =16 ='(2**16)**(2**16)' --min_k='2**16-1024-512'
[(64000, 85521)]
py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list_all_floor_kth_root_until_diff_lt_ =16 ='(2**16)**(2**16)' --min_k='2**16-1024-512-64'
[(63936, 86499), (63937, 86483)]

]]
[[
py_adhoc_call__7_ns2ks_:here

py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list._ns2ks_ '=[31,32,33, 63,64,65, 127,128,129]'
    [1, 2, 2, 2, 2, 2, 2, 2, 2]
py_adhoc_call   seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N   @list._ns2ks_ '=[n for e in range(5,257) for u in [1<<e] for n in [u-1,u]]'
    # 256 => 25
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]

]]


#]]]'''#'''

__all__
r'''[[[

[[
@20260813
estimate_k4N_where_diff_kth_root4N_kppth_root4N_lt1:here
[N**/k - N**/(1+k) < 1] ~= [k > (lnN/lnlnN)]

estimate_k4N_where_diff_kth_root4N_kppth_root4N_ltB:here
[N**/k - N**/(1+k) < B] ~= [k > lnN/(lnB+lnlnN)]

<<==:
[floor_kth_root_(k;N) == floor_kth_root_(1+k;N)]
~=:
[N**/k - N**/(1+k) < 1]
[exp(lnN/k) -exp(lnN/(1+k)) < 1]
[exp(lnN/(k*(1+k))) < 1+exp(-lnN/(1+k))]
[N == exp(lnN) < (1+exp(-lnN/(1+k)))**(k*(1+k)) ~=??? 1+(k*(1+k))*exp(-lnN/(1+k)) ~=??? 1+(k*(1+k))/N**/(1+k)]

[f(x) := exp(lnN/x)]
[Df(x) == exp(lnN/x)*lnN*(-1/x**2)]

!! [exp(lnN/k) -exp(lnN/(1+k)) < 1]
[f(k) -f(1+k) < 1]
[(f(1+k) -f(k))/((1+k) -(k)) > -1]
~=:
[Df(k) > -1]
[exp(lnN/k)*lnN*(-1/k**2) > -1]
[exp(lnN/k)*lnN < (k**2)]
[exp(lnN/2/k)*sqrt(lnN) < k]
[N**(1/2/k)*sqrt(lnN) < k]
[N**/2 < (k/sqrt(lnN))**k]

!! [exp(lnN/2/k)*sqrt(lnN) < k]
[(lnN/2/k) + lnlnN/2 < lnK]
[(lnN/2) < k*(lnK -lnlnN/2)]
[(lbN/2) < k*(lbK -lblnN/2)]
~= [(lbN/2) < k*(lbK -lblbN/2)]

!! [(lnN/2) < k*(lnK -lnlnN/2)]
[(lnlnN -ln2) < lnK + ln(lnK -lnlnN/2)]
~= [lnlnN < lnK + lnlnK]
~= [lnlnN -lnlnlnN < lnK]
~= [(lnN/2) < k*(lnlnN -lnlnlnN -lnlnN/2)]
~= [k > (lnN/(lnlnN -2*lnlnlnN))]
~= [k > (lnN/lnlnN)]


[N**/k - N**/(1+k) < B]
[(f(1+k) -f(k))/((1+k) -(k)) > -B]
~=:
[Df(k) > -B]
[exp(lnN/k)*lnN < (B*k**2)]
[(lnN/k) +lnlnN < (lnB + 2*lnK)]
[lnN < k*(2*lnK +lnB -lnlnN)]
[B:=lnN] => [lnN < 2*k*lnK]
[lnlnN < lnK +ln(2*lnK +lnB -lnlnN)]
~= [lnlnN < lnK +ln(2*lnK +lnB -(lnK +ln(2*lnK +lnB -lnlnN)))]
~= [lnlnN < lnK +lnlnKB]
~= [lnN < k*lnKB]
~= [k > lnN/lnKB == lnN/(lnB+lnK) ~= lnN/(lnB+lnlnN -lnlnKB) ~= lnN/(lnB+lnlnN)]
~= [k > lnN/(lnB+lnlnN)]



taylor('x*log('x), 'x)
    *** log: domain error in log: series valuation != 0
taylor((1+'x)*log(1+'x), 'x)
    x+1/2*x^2-1/6*x^3+1/12*x^4-1/20*x^5+1/30*x^6-1/42*x^7+1/56*x^8-1/72*x^9+1/90*x^10-1/110*x^11+1/132*x^12-1/156*x^13+1/182*x^14-1/210*x^15+O(x^16)
taylor((1+'x)*(log(1+'x) -'C), 'x)
    -C+(-C+1)*x+1/2*x^2-1/6*x^3+1/12*x^4-1/20*x^5+1/30*x^6-1/42*x^7+1/56*x^8-1/72*x^9+1/90*x^10-1/110*x^11+1/132*x^12-1/156*x^13+1/182*x^14-1/210*x^15+O(x^16)
    useless
serreverse(taylor((1+'x)*(log(1+'x) -'C), 'x))
    *** serreverse: domain error in serreverse: valuation != 1
serreverse(taylor((1+'x)*(log(1+'x) -0), 'x))
    x-1/2*x^2+2/3*x^3-9/8*x^4+32/15*x^5-625/144*x^6+324/35*x^7-117649/5760*x^8+131072/2835*x^9-4782969/44800*x^10+1562500/6237*x^11-25937424601/43545600*x^12+35831808/25025*x^13-23298085122481/6706022400*x^14+110730297608/13030875*x^15+O(x^16)


!! [Df(k) > -1]
=> [N**/2 < (k/sqrt(lnN))**k]
=> [(lnN/2) < k*(lnK -lnlnN/2)]
=> ~= [k > (lnN/(lnlnN -2*lnlnlnN))]
=> ~= [k > (lnN/lnlnN)]
sqrtnint(2^64, 20)
    9
    sqrtnint <==> (flip . floor_kth_root_)
{search_(N)= for(k=2,logint(N,2), if(sqrtnint(N,k) == sqrtnint(N,1+k),return(k))) }
{search_until_diff_lt_(min4diff,N)= for(k=2,1+logint(N,2), if(sqrtnint(N,k) -sqrtnint(N,1+k) < min4diff,return(k))) }
{search_until_le1_(min4k,max4k,k2ratio_)= for(neg4k=-max4k,-min4k,my(k=-neg4k,r=k2ratio_(k));if(r<=1,return([k,r;k+1,k2ratio_(k+1);max4k,k2ratio_(max4k)]))) }

search_(2^64)
    23
search_until_le1_(15,23,(k,N=2^64)->(k/sqrt(log(N)))^k /sqrt(N))
    [20,0.827
    ;21,6.9
    ;23,557.465
    ]
    ######################
    23 vs 21
    ######################
search_until_le1_(15,23,(k,N=2^64)->(k*(log(k)-log(log(N))/2)/(log(N)/2)))
    [20,0.99
    ;21,1.087
    ;23,1.285
    ]
    ######################
!! [N**/k - N**/(1+k) < 1] ~= [k > (lnN/lnlnN)] #estimate_k4N_where_diff_kth_root4N_kppth_root4N_lt1:goto
search_until_le1_(10,23,(k,N=2^64)->(k/(log(N)/(log(log(N)) -0*log(log(log(N)))))))
    [11,0.94
    ;12,1.0258563
    ;23,1.9662
    ]
search_until_le1_(10,23,(k,N=2^64)->(k/(log(N)/(log(log(N)) -1*log(log(log(N)))))))
    [18,0.9979
    ;19,1.053
    ;23,1.275
    ]
search_until_le1_(10,26,(k,N=2^64)->(k/(log(N)/(log(log(N)) -1.5*log(log(log(N)))))))
    [24,0.969968979
    ;25,1.01
    ;26,1.05
    ]
search_until_le1_(10,41,(k,N=2^64)->(k/(log(N)/(log(log(N)) -2*log(log(log(N)))))))
    [39,0.990255
    ;40,1.015646
    ;41,1.041
    ]
    [(lnN/lnlnN) == (log(2^64)/log(log(2^64))) ~= 11.7]
    [(lnN/(lnlnN -2*lnlnlnN)) == (log(2^64)/(log(log(2^64)) -2*log(log(log(2^64))))) ~= 39.38]
    [(lnN/(lnlnN -1.5*lnlnlnN)) == (log(2^64)/(log(log(2^64)) -1.5*log(log(log(2^64))))) ~= 24.7]
    [(lnN/(lnlnN -lnlnlnN)) == (log(2^64)/(log(log(2^64)) -log(log(log(2^64))))) ~= 18.0]
    ######################

search_(2^6400)
    872
search_until_le1_(850,872,(k,N=2^6400)->(k/sqrt(log(N)))^k /sqrt(N))
    [865,0.7818
    ;866,27.6156
    ;872,54956499704.98
    ]
    ######################
    872 vs 866
    ######################
search_until_le1_(850,872,(k,N=2^6400)->(k*(log(k)-log(log(N))/2)/(log(N)/2)))
    [865,0.999889
    ;866,1.001496
    ;872,1.01114924
    ]
    ######################
!! [N**/k - N**/(1+k) < 1] ~= [k > (lnN/lnlnN)] #estimate_k4N_where_diff_kth_root4N_kppth_root4N_lt1:goto
search_until_le1_(500,872,(k,N=2^6400)->(k/(log(N)/(log(log(N)) -0*log(log(log(N)))))))
    [528,0.9994949
    ;529,1.00138789
    ;872,1.65
    ]
search_until_le1_(500,872,(k,N=2^6400)->(k/(log(N)/(log(log(N)) -1*log(log(log(N)))))))
    [707,0.9992
    ;708,1.0006
    ;872,1.232398
    ]
search_until_le1_(500,872,(k,N=2^6400)->(k/(log(N)/(log(log(N)) -1.5*log(log(log(N)))))))
    [852,0.999787
    ;853,1.00096
    ;872,1.0232565
    ]
search_until_le1_(500,1073,(k,N=2^6400)->(k/(log(N)/(log(log(N)) -2*log(log(log(N)))))))
    [1071,0.9999
    ;1072,1.0008
    ;1073,1.00177
    ]

    [(lnN/lnlnN) == (log(2^6400)/log(log(2^6400))) ~= 528.3]
    [(lnN/(lnlnN -2*lnlnlnN)) == (log(2^6400)/(log(log(2^6400)) -2*log(log(log(2^6400))))) ~= 1071.1]
    [(lnN/(lnlnN -1.5*lnlnlnN)) == (log(2^6400)/(log(log(2^6400)) -1.5*log(log(log(2^6400))))) ~= 852.18]
    [(lnN/(lnlnN -lnlnlnN)) == (log(2^6400)/(log(log(2^6400)) -log(log(log(2^6400))))) ~= 707.56]
    ######################










search_until_diff_lt_(256,2^64)
    8
!! [N**/k - N**/(1+k) < B] ~= [k > lnN/(lnB+lnlnN)] # estimate_k4N_where_diff_kth_root4N_kppth_root4N_ltB:goto
search_until_le1_(2,8,(k,N=2^64,B=256)->(k/(log(N)/(log(log(N)) +log(B)))))
    [4,0.84
    ;5,1.05
    ;8,1.68
    ]
    ######################
    8 vs 5
    ######################
search_until_diff_lt_(256,2^6400)
    469
search_until_le1_(200,469,(k,N=2^6400,B=256)->(k/(log(N)/(log(log(N)) +log(B)))))
    [318,0.999
    ;319,1.0026
    ;469,1.474
    ]
    ######################
    469 vs 319
    ######################
search_until_diff_lt_(2^12,2^6400)
    377
search_until_le1_(200,377,(k,N=2^6400,B=2^12)->(k/(log(N)/(log(log(N)) +log(B)))))
    [265,0.9985
    ;266,1.00228
    ;377,1.42
    ]
    ######################
    377 vs 266
    ######################
search_until_diff_lt_(2^128,2^6400)
    50
search_until_le1_(2,50,(k,N=2^6400,B=2^128)->(k/(log(N)/(log(log(N)) +log(B)))))
    [45,0.985
    ;46,1.007
    ;50,1.09
    ]
    ######################
    50 vs 46
    ######################

]]




[[
before:@20260813
estimate_k4N_where_diff_kth_root4N_kppth_root4N_lt_given_bound:here
[n>=1][k>=1][diff>=1][n**/k -n**/(1+k) < diff]:
    [x:=n**/(1+k)]
    [x**(1+k) == n]
    [(x+diff)**k > n]
    [(x+diff)**k > x**(1+k)]
    [(1+diff/x)**k > x]
    [k*ln_(1+diff/x) > ln_(x)]
    [z:=diff/x]
    [k*ln_(1+z) > ln_(diff/z)]
    [k*ln_(1+z) > ln_(diff) -ln_(z)]
    [k*(z -z**2/2 +z**3/3 ...) > ln_(diff) -ln_(z)]
    [k*sum[-(-z)**j/j | [j:<-[1..]]] > ln_(diff) -ln_(z)]
    ~~=>:
        [k*z ~>~ ln_(diff) -ln_(z)]
        [k*z +ln_(z) ~>~ ln_(diff)]
        [k*z ~>~ ln_(diff)]
        [z ~>~ ln_(diff)/k]
        [diff/x ~>~ ln_(diff)/k]
        [k*diff/ln_(diff) ~>~ x]
        [x ~<~ k*diff/ln_(diff)]

    [k*ln_(1+diff/x) > ln_(x)]
    ~~=>:
        [k*(diff/x) ~>~ ln_(x)]
        [k*diff ~>~ x*ln_(x)]
        [x*ln_(x) ~<~ k*diff]

        [n**/(1+k)*ln_(n**/(1+k)) ~<~ k*diff]
        [n**/(1+k)/(1+k)/k ~<~ diff/ln_(n)]
        [diff:=floor_log2(n)]:
            [n**/(1+k)/(1+k)/k ~<~ 1/ln2]
            [n**/(1+k)/(1+k)/k ~<~ 1]
                [n**/k ~<~ k**2]
                [n**/2 ~<~ k**k]
            [n**/(1+k) ~<~ (1+k)**2]
            [log2(n) ~<~ 2*(1+k)*log2(1+k)]
                _n2k_:goto

        [n:=2**256][diff:=4][k:=47][x~=43-4=39]:
            !! [x ~<~ k*diff/ln_(diff)]
            [39 ~= x ~<~ k*diff/ln_(diff) ~= 135.61333384356257] #bad
            !! [x*ln_(x) ~<~ k*diff]
            [142.8789041990562 ~= x*ln_(x) ~<~ k*diff == 188]

        [n:=2**2048][diff:=4][k:=269][x~=195-4=191]:
            !! [x*ln_(x) ~<~ k*diff]
            [1003.1842247569064 ~= x*ln_(x) ~<~ k*diff == 1076]


]]

#]]]'''#'''

__all__
class KthRoots4N:
    _n2sf = WeakValueDictionary()
    def __new__(cls, n, /):
        assert cls is __class__
        try:
            return cls._n2sf[n]
        except KeyError:
            pass
        check_int_ge(1, n)
        sf = super(__class__, cls).__new__(cls)
        sf._n = n
        rs = _n2rs_(n)
        # [rs:has no dup]
        sf._rs = tuple(rs)
        return sf
    @property
    def the_N(sf, /):
        return sf._n
    @property
    def _kth_roots4N_(sf, /):
        return sf._rs
    def __repr__(sf, /):
        return repr_helper(sf, sf.the_N)
    def __call__(sf, u, /):
        'u -> max_exp/floor_log_(u; n)'
        assert u >= 2
        n = sf.the_N
        # [u**max_exp <= n]
        # [u <= n**/max_exp]
        # [u <= floor_kth_root_(max_exp;n)]
        if u > n:
            return 0
        # [u <= n]
        rs = sf._kth_roots4N_
        if not (rs and u >= rs[-1][1]):
            return floor_log_(u, n)
        # [rs[-1][-1] <= u <= n]
        if 0:
            # !! [rs:has no dup]
            j = bisect_right(rs, -u, key=lambda k_rt:-k_rt[1])
            assert 0 < j <= len(rs)
            assert j == len(rs) or u > rs[j][1]
            assert u <= rs[j-1][1]
            max_exp = rs[j-1][0]
        else:
            # allow [rs:has dup]
            j = bisect_left(rs, -u, key=lambda k_rt:-k_rt[1])
            assert 0 <= j < len(rs)
            assert u >= rs[j][1]
            assert not j == 0 or u == rs[j][1]
            assert j == 0 or u < rs[j-1][1]
            max_exp = rs[j][0] if u == rs[j][1] else rs[j-1][0]
        return max_exp
    def validate(sf, /):
        rs = sf._kth_roots4N_
        n = sf.the_N
        assert sf(1+n) == 0
        assert sf(n) == 1
        prev_rt = 1+n
        for k, rt in rs:
            if rt >= 1:
                assert sf(rt+1) < k
                assert sf(rt+1) == floor_log_(rt+1, n)
            if rt >= 2:
                assert sf(rt) == k
                assert sf(rt) == floor_log_(rt, n)
            if rt >= 3:
                assert sf(rt-1) >= k
                assert sf(rt-1) == floor_log_(rt-1, n)




def _n2rs_(n):
    rs = list_all_floor_kth_root_until_diff_lt_(..., n, one_more=True)
    #if len(rs) > 1 and rs[-2][-1] == rs[-1][-1]:
    for (k, rt6k), (k1, rt6k1) in pairwise(rs):
        if rt6k == rt6k1:
            del rs[k-1:]
            # [rs:has no dup]
            assert not rs or rs[-1][0] == k-1
            break
    else:
        # [rs:has no dup]
        if len(rs) > 2:
            rs.pop() # one_more
    # [rs:has no dup]
    return rs
def _ns2ks_(ns, /):
    for n in ns:
        yield _n2k_(n)
def _n2k_(n, /):
    # min k :=> [floor_log2(n) <= 2*(1+k)*ceil_log2(1+k)]
        # min k :=> [log2(n) <= 2*(1+k)*log2(1+k)]
        #   see:list_all_floor_kth_root_until_diff_lt_
    assert n >= 1
    if n < 31:
        k = 1
        return k
    lb_n = floor_log2(n)
    u = 2*(1+lb_n)
    assert u >= 2
    k1 = max(1,-(u//-floor_log2(u)))
    lb_k1 = ceil_log2(k1)
    assert lb_n <= 2*k1*lb_k1, (n, k1, lb_n, 2*k1*lb_k1)
    for e in reversed(range(1+lb_k1)):
        if lb_n > (e << (1+e)):
            break
    else:
        raise
    assert lb_n > (e << (1+e))
    assert lb_n <= ((1+e) << (2+e))
    x0 = k1 = lb_n // (1+e)
    lb_k1 = ceil_log2(k1)
    while not lb_n <= 2*k1*lb_k1:
        k1 += 1
        lb_k1 = ceil_log2(k1)
    assert k1 -x0 < 3, (n, lb_n, e, k1, x0)
    y0 = k = k1-1
    lb_k = ceil_log2(k)
    while not lb_n > 2*k*lb_k:
        k -= 1
        lb_k = ceil_log2(k)
    assert k -y0 < 3, (n, lb_n, e, k, y0)
    k1 = 1+k
    assert lb_n <= 2*k1*ceil_log2(k1)
    assert lb_n > 2*k*ceil_log2(k)
    return k


def list_all_floor_kth_root_until_diff_lt_(emay_min_diff, n, /, *, min_k=1, one_more=False):
    if not (b_auto:=emay_min_diff is ...):
        min_diff = emay_min_diff
        assert min_diff >= 0
    assert n >= 1
    assert min_k >= 1
    if min_k == 1:
        k = 1
        777;rt = n
    else:
        assert min_k >= 2
        k = min_k
        777;rt = floor_kth_root_(k, n)
    ls = [(k, rt)]
    b_stop = False
    for k in range(1+k, 2+floor_log2(n)):
        rt = floor_kth_root_(k, n)
        diff = ls[-1][-1] -rt
        if b_auto:
            if diff < floor_log2(rt):
                b_stop = True
        elif diff < min_diff:
            b_stop = True
        if b_stop:break
        ls.append((k, rt))
    else:
        #if one_more: raise Exception(emay_min_diff, n, min_k, one_more)
        pass
    ls
    if b_stop and one_more:
        ls.append((k, rt))
    ls
    return ls




__all__
from seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N import KthRoots4N, list_all_floor_kth_root_until_diff_lt_
from seed.math.floor_ceil_tools.fc_kth_root__7KthRoots4N import *
