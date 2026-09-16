#__all__:goto
#TODO:goto
#   实现:补丁:更多失败信息:
#       1. ctx{FoundTrivialFactor} verbose print_err;
#       2. stage1结束，stage2起始ctx 即使还未实现stage2，方便未来断点重启
#
#   DONE:实现: [X:Z] 省略Y，且齐次无需inv6N_()
#   DONE:实现:第二阶段:额外一个大素数

# formula4edgecase4addh_:goto
# formula4main4addh_:goto
# formula4doubleh_:goto
# [:define__addh]:goto
# [:define__doubleh]:goto
# [:define__mulh]:goto
# [:define__ECM7inversionless]:goto
# [examples__ECM]:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/factor_pint__elliptic_curve_method.py
ECM

seed.math.factor_pint.factor_pint__elliptic_curve_method
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.factor_pint__elliptic_curve_method -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.factor_pint__elliptic_curve_method:__doc__ -ht # -ff -df
#######

[[
TODO:
e ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method.py
]]


'#'; __doc__ = r'#'
>>> for u in range(1, 35):print(u, try_factor_pint__elliptic_curve_method_(u), sep=':')
1:None
2:None
3:None
4:2
5:None
6:2
7:None
8:2
9:3
10:2
11:None
12:2
13:None
14:2
15:3
16:2
17:None
18:2
19:None
20:2
21:3
22:2
23:None
24:2
25:5
26:2
27:3
28:2
29:None
30:2
31:None
32:2
33:3
34:2

>>> s = set()
>>> while len(s) < 3:s.add(try_factor_pint__elliptic_curve_method_(35))
>>> s == {None, 5, 7}
True


>>> try_factor_pint__elliptic_curve_method_(31, with_ctx=True)
>>> try_factor_pint__elliptic_curve_method_(31, with_ctx=True, result6fail='fail')
'fail'
>>> try_factor_pint__elliptic_curve_method_(34, with_ctx=True)
2
>>> for _ in range(9):try_factor_pint__elliptic_curve_method_(35, with_ctx=True, result6fail=False)   #doctest: +SKIP
(5, ((0, 10000), (0, 2), (Ops4EllipticPseudocurve(35, 5, 8), Pt4EC(-17, 15)), (Ops4EllipticPseudocurve(35, 5, 8), 30)))
False
(7, ((0, 10000), (0, 2), (Ops4EllipticPseudocurve(35, 7, 6), Pt4EC(-12, 7)), (Ops4EllipticPseudocurve(35, 7, 6), 14)))
(5, ((0, 10000), (-1, None), (None, pt_O), (35, 12, 8)))
(5, ((0, 10000), (0, 2), (Ops4EllipticPseudocurve(35, -9, 5), Pt4EC(-5, -10)), (Ops4EllipticPseudocurve(35, -9, 5), -20)))
(7, ((0, 10000), (-1, None), (None, pt_O), (35, 29, 16)))
False
(7, ((0, 10000), (-1, None), (None, pt_O), (35, 16, -12)))
False




>>> for _ in range(9):try_factor_pint__elliptic_curve_method_((-1+2**67), with_ctx=True, result6fail=False)   #doctest: +SKIP
False
False
False
False
False
False
False
(193707721, ((0, 10000), (92, 181), (Ops4EllipticPseudocurve(147573952589676412927, -65329900703389147398, 61110624153339716918), Pt4EC(34206251627092302792, 62573895624016379251)), (Ops4EllipticPseudocurve(147573952589676412927, -65329900703389147398, 61110624153339716918), 5240554684677003330)))
(193707721, ((0, 10000), (155, 571), (Ops4EllipticPseudocurve(147573952589676412927, -43218562940503950175, -48142509726347098493), Pt4EC(-15492791477142507109, -38181994672106652297)), (Ops4EllipticPseudocurve(147573952589676412927, -43218562940503950175, -48142509726347098493), 84961549451557299714)))















def ex1_try_factor_pint__elliptic_curve_method_(n, B1, /, *, random_uint_mod_=None):
>>> ex1_try_factor_pint__elliptic_curve_method_(n:=(-1+2**67), B1:=1_00_00, random_uint_mod_=None)   #doctest: +SKIP
(193707721, ((147573952589676412927, 8977067194192764477, 45441361906832129093), (-48615346920337614352, 38730586238887869137)), 10000)
>>> ex1_try_factor_pint__elliptic_curve_method_(n:=(-1+2**67), B1:=1_00_00, settings4EPC=((147573952589676412927, 8977067194192764477, 45441361906832129093), (-48615346920337614352, 38730586238887869137)))
(193707721, ((147573952589676412927, 8977067194192764477, 45441361906832129093), (-48615346920337614352, 38730586238887869137)), 10000)









try1_factor_pint__elliptic_curve_method_
#ft@stage2
>>> try1_factor_pint__elliptic_curve_method_(n:=(-1+2**67), B1:=1_00, B2:=1_00_00) #doctest: +SKIP
(193707721, ((147573952589676412927, 31894543639004476236, 49298064024460420879), (-32188269198793461178, 38620417464689350048)), 2, (97, 218, 1549))
>>> try1_factor_pint__elliptic_curve_method_(settings4EPC:=((147573952589676412927, 31894543639004476236, 49298064024460420879), (-32188269198793461178, 38620417464689350048)), B1:=1_00, B2:=1_00_00)
(193707721, ((147573952589676412927, 31894543639004476236, 49298064024460420879), (-32188269198793461178, 38620417464689350048)), 2, (97, 218, 1549))


#ft@stage1
>>> try1_factor_pint__elliptic_curve_method_(n:=(-1+2**67), B1:=1_00_00, B2:=0) #doctest: +SKIP
(193707721, ((147573952589676412927, -17560380949213629436, 23162115318173030126), (71001320234957843534, 24622508313107188569)), 1, (1196, 9241))
>>> try1_factor_pint__elliptic_curve_method_(settings4EPC:=((147573952589676412927, -17560380949213629436, 23162115318173030126), (71001320234957843534, 24622508313107188569)), B1:=1_00_00, B2:=0)
(193707721, ((147573952589676412927, -17560380949213629436, 23162115318173030126), (71001320234957843534, 24622508313107188569)), 1, (1196, 9241))



















>>> def show_muls_(ops, pt_0, end4k, /):
...     for k in range(end4k):
...         k_pt = ops.mul7h_(k, pt_0)
...         print(k, k_pt, sep=':')

>>> def show_diffs_(ops, pt_0, end4k, /, *, same_also=False):
...     n = ops.params4elliptic_pseudocurve7drop_Y[0]
...     _k_pt = pt7h_O
...     _kmm_pt = pt_0 # ~ -pt_0
...     for k in range(end4k):
...         k_pt = ops.mul7h_(k, pt_0)
...         if not _k_pt.eq7h7mod_(n, k_pt):print(k, False, k_pt, _k_pt, sep=':')
...         elif same_also:print(k, True, k_pt, _k_pt, sep=':') # diff-repr by ratio
...         try:
...             (_k_pt, _kmm_pt) = (ops.add7h_(_k_pt, pt_0, _kmm_pt), _k_pt)
...         except (Incapable__add7h__X6diff_eq0,FoundNonTrivialFactor) as exc:
...             print(1+k, repr(exc), sep=':')
...             break



>>> Ops4EllipticPseudocurve7DropY.mk_ex5n__7random_(35) #doctest: +SKIP
seed.math.factor_pint.factor_pint__elliptic_curve_method.FoundNonTrivialFactor: (35, 5, (35, 12, -1))
seed.math.factor_pint.factor_pint__elliptic_curve_method.FoundNonTrivialFactor: (35, 7, (35, -13, -14))

>>> Ops4EllipticPseudocurve7DropY.mk_ex5n__7random_(35, strict=False) #doctest: +SKIP
(Ops4EllipticPseudocurve7DropY(35, 16, 1, strict = False), Pt4EC7h(8, 1))

>>> (ops, pt_0) = (Ops4EllipticPseudocurve7DropY(35, 16, 1), Pt4EC7h(8, 1))
Traceback (most recent call last):
    ...
seed.math.factor_pint.factor_pint__elliptic_curve_method.FoundNonTrivialFactor: (35, 7, (35, 16, 1))

>>> (ops, pt_0) = (Ops4EllipticPseudocurve7DropY(35, 16, 1, strict=False), Pt4EC7h(8, 1))
>>> (ops, pt_0)
(Ops4EllipticPseudocurve7DropY(35, 16, 1, strict = False), Pt4EC7h(8, 1))

>>> _2_0 = ops.double7h_(pt_0); _2_0
Pt4EC7h(14, 16)
>>> ops.add7h_(pt_0, pt_0, pt7h_O)
Pt4EC7h(14, 16)
>>> ops.add7h_(pt_0, pt7h_O, pt_0)
Pt4EC7h(8, 1)
>>> ops.add7h_(pt7h_O, pt_0, pt_0)
Pt4EC7h(8, 1)
>>> _3_0 = ops.add7h_(_2_0, pt_0, pt_0); _3_0
Pt4EC7h(11, -17)
>>> ops.add7h_(pt_0, _2_0, pt_0)
Pt4EC7h(11, -17)
>>> _4_0 = ops.add7h_(_3_0, pt_0, _2_0);_4_0
Pt4EC7h(0, -14)
>>> _a4_0 = ops.double7h_(_2_0); _a4_0 # =!= _4_0 !!!!!!!!!!!!!!!!!!!
Pt4EC7h(-5, -14)
>>> _5_0 = ops.add7h_(_4_0, pt_0, _3_0);_5_0
Pt4EC7h(-7, 14)
>>> _6_0 = ops.add7h_(_5_0, pt_0, _4_0);_6_0
Traceback (most recent call last):
    ...
seed.math.factor_pint.factor_pint__elliptic_curve_method.Incapable__add7h__X6diff_eq0: ((35, 16, 1), (Pt4EC7h(-7, 14), Pt4EC7h(8, 1), Pt4EC7h(0, -14)))

>>> n = 35
>>> show_diffs_(ops, pt_0, 60)
6:Incapable__add7h__X6diff_eq0((35, 16, 1), (Pt4EC7h(-7, 14), Pt4EC7h(8, 1), Pt4EC7h(0, -14)))

>>> show_diffs_(ops, pt_0, 60, same_also=True)
0:True:Pt4EC7h(0, 0):Pt4EC7h(0, 0)
1:True:Pt4EC7h(8, 1):Pt4EC7h(8, 1)
2:True:Pt4EC7h(14, 16):Pt4EC7h(14, 16)
3:True:Pt4EC7h(11, -17):Pt4EC7h(11, -17)
4:True:Pt4EC7h(-5, -14):Pt4EC7h(0, -14)
5:True:Pt4EC7h(1, 8):Pt4EC7h(-7, 14)
6:Incapable__add7h__X6diff_eq0((35, 16, 1), (Pt4EC7h(-7, 14), Pt4EC7h(8, 1), Pt4EC7h(0, -14)))


>>> show_muls_(ops, pt_0, 60)
0:Pt4EC7h(0, 0)
1:Pt4EC7h(8, 1)
2:Pt4EC7h(14, 16)
3:Pt4EC7h(11, -17)
4:Pt4EC7h(-5, -14)
5:Pt4EC7h(1, 8)
6:Pt4EC7h(14, 1)
7:Pt4EC7h(-6, 8)
8:Pt4EC7h(0, 0)
9:Pt4EC7h(4, -17)
10:Pt4EC7h(14, 16)
11:Pt4EC7h(1, 8)
12:Pt4EC7h(15, -14)
13:Pt4EC7h(-6, -13)
14:Pt4EC7h(14, 16)
15:Pt4EC7h(-6, 8)
16:Pt4EC7h(0, 0)
17:Pt4EC7h(4, -17)
18:Pt4EC7h(14, 1)
19:Pt4EC7h(-6, -13)
20:Pt4EC7h(-5, -14)
21:Pt4EC7h(11, -17)
22:Pt4EC7h(14, 16)
23:Pt4EC7h(-6, 8)
24:Pt4EC7h(0, 0)
25:Pt4EC7h(-6, 8)
26:Pt4EC7h(14, 16)
27:Pt4EC7h(11, -17)
28:Pt4EC7h(-5, -14)
29:Pt4EC7h(4, -3)
30:Pt4EC7h(14, 16)
31:Pt4EC7h(-6, 8)
32:Pt4EC7h(0, 0)
33:Pt4EC7h(4, -17)
34:Pt4EC7h(14, 1)
35:Pt4EC7h(9, 2)
36:Pt4EC7h(15, -14)
37:Pt4EC7h(1, 8)
38:Pt4EC7h(14, 16)
39:Pt4EC7h(4, -17)
40:Pt4EC7h(0, 0)
41:Pt4EC7h(-6, 8)
42:Pt4EC7h(14, 1)
43:Pt4EC7h(1, 8)
44:Pt4EC7h(-5, -14)
45:Pt4EC7h(4, -3)
46:Pt4EC7h(14, 16)
47:Pt4EC7h(-6, 8)
48:Pt4EC7h(0, 0)
49:Pt4EC7h(-6, 8)
50:Pt4EC7h(14, 16)
51:Pt4EC7h(4, -3)
52:Pt4EC7h(-5, -14)
53:Pt4EC7h(1, 8)
54:Pt4EC7h(14, 1)
55:Pt4EC7h(-6, 8)
56:Pt4EC7h(0, 0)
57:Pt4EC7h(-6, 8)
58:Pt4EC7h(14, 1)
59:Pt4EC7h(1, 8)





>>> Ops4EllipticPseudocurve7DropY.mk_ex5n__7random_(61*67) #doctest: +SKIP
(Ops4EllipticPseudocurve7DropY(4087, 724, -1984), Pt4EC7h(-694, -156))
>>> (ops, pt_0) = (Ops4EllipticPseudocurve7DropY(4087, 724, -1984), Pt4EC7h(-694, -156))
>>> (ops, pt_0)
(Ops4EllipticPseudocurve7DropY(4087, 724, -1984), Pt4EC7h(-694, -156))
>>> n = 4087
>>> show_diffs_(ops, pt_0, 60)
20:Incapable__add7h__X6diff_eq0((4087, 724, -1984), (Pt4EC7h(2013, -1891), Pt4EC7h(-694, -156), Pt4EC7h(0, -1159)))

>>> show_diffs_(ops, pt_0, 60, same_also=True)
0:True:Pt4EC7h(0, 0):Pt4EC7h(0, 0)
1:True:Pt4EC7h(-694, -156):Pt4EC7h(-694, -156)
2:True:Pt4EC7h(-98, 1564):Pt4EC7h(-98, 1564)
3:True:Pt4EC7h(1695, 11):Pt4EC7h(1695, 11)
4:True:Pt4EC7h(419, -1272):Pt4EC7h(-271, -816)
5:True:Pt4EC7h(113, 1861):Pt4EC7h(2030, 1785)
6:True:Pt4EC7h(265, 163):Pt4EC7h(-1180, 508)
7:True:Pt4EC7h(1285, -6):Pt4EC7h(195, 1812)
8:True:Pt4EC7h(-1928, -1927):Pt4EC7h(1953, -1374)
9:True:Pt4EC7h(-2016, 1066):Pt4EC7h(130, -1277)
10:True:Pt4EC7h(-1319, 585):Pt4EC7h(1241, -1638)
11:True:Pt4EC7h(-1886, -181):Pt4EC7h(1852, 1790)
12:True:Pt4EC7h(-51, -168):Pt4EC7h(-597, 1880)
13:True:Pt4EC7h(-754, -600):Pt4EC7h(-892, -16)
14:True:Pt4EC7h(-112, -2038):Pt4EC7h(-714, -1753)
15:True:Pt4EC7h(535, -1220):Pt4EC7h(745, 1586)
16:True:Pt4EC7h(-1680, 601):Pt4EC7h(-1803, 1061)
17:True:Pt4EC7h(615, 275):Pt4EC7h(1403, 1159)
18:True:Pt4EC7h(67, -1638):Pt4EC7h(0, -1159)
19:True:Pt4EC7h(-1245, -1413):Pt4EC7h(2013, -1891)
20:Incapable__add7h__X6diff_eq0((4087, 724, -1984), (Pt4EC7h(2013, -1891), Pt4EC7h(-694, -156), Pt4EC7h(0, -1159)))
>>> gcd(n, 1159)
61


>>> show_muls_(ops, pt_0, 30)
0:Pt4EC7h(0, 0)
1:Pt4EC7h(-694, -156)
2:Pt4EC7h(-98, 1564)
3:Pt4EC7h(1695, 11)
4:Pt4EC7h(419, -1272)
5:Pt4EC7h(113, 1861)
6:Pt4EC7h(265, 163)
7:Pt4EC7h(1285, -6)
8:Pt4EC7h(-1928, -1927)
9:Pt4EC7h(-2016, 1066)
10:Pt4EC7h(-1319, 585)
11:Pt4EC7h(-1886, -181)
12:Pt4EC7h(-51, -168)
13:Pt4EC7h(-754, -600)
14:Pt4EC7h(-112, -2038)
15:Pt4EC7h(535, -1220)
16:Pt4EC7h(-1680, 601)
17:Pt4EC7h(615, 275)
18:Pt4EC7h(67, -1638)
19:Pt4EC7h(-1245, -1413)
20:Pt4EC7h(-526, -1001)
21:Pt4EC7h(1001, -994)
22:Pt4EC7h(-1851, -1585)
23:Pt4EC7h(-607, -1560)
24:Pt4EC7h(627, 954)
25:Pt4EC7h(432, 342)
26:Pt4EC7h(1466, 562)
27:Pt4EC7h(876, 1680)
28:Pt4EC7h(-1047, 853)
29:Pt4EC7h(-890, 1249)








++kw:imay_period4detect
>>> [*islice(_4imay_period4detect(9, -1)(), 0, 17)]
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
>>> [*islice(_4imay_period4detect(9, 0)(), 0, 17)] # auto # 9=>16
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False]
>>> [*islice(_4imay_period4detect(9, 1)(), 0, 17)]
[True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
>>> [*islice(_4imay_period4detect(9, 2)(), 0, 17)]
[False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False]
>>> [*islice(_4imay_period4detect(9, 3)(), 0, 17)]
[False, False, True, False, False, True, False, False, True, False, False, True, False, False, True, False, False]







>>> (ops, pt_0) = (Ops4EllipticPseudocurve7DropY(4087, 724, -1984, detect6Incapable=True), Pt4EC7h(-694, -156))
>>> show_diffs_(ops, pt_0, 60)
20:FoundNonTrivialFactor(4087, 61, (4087, 724, -1984))




>>> settings4EPC = ((4087, 724, -1984), (-694, -156))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(settings4EPC)
(67, ((4087, 724, -1984), (-694, -156)), 1, (21, 5))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(settings4EPC, 9, imay_period4detect=1)
(67, ((4087, 724, -1984), (-694, -156)), 1, (5, 5))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(settings4EPC, 8, imay_period4detect=1)
(61, ((4087, 724, -1984), (-694, -156)), 1, (5, 7))

>>> try1_factor_pint__elliptic_curve_method7inversionless_(settings4EPC, 10, 20)
(67, ((4087, 724, -1984), (-694, -156)), 1, (5, 5))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(settings4EPC, 3, 10)
(61, ((4087, 724, -1984), (-694, -156)), 2, (3, 1, 7))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(settings4EPC, 2, 10)
(None, (4087, ((4087, 724, -1984), (-694, -156)), (Ops4EllipticPseudocurve7DropY(4087, 724, -1984, detect6Incapable = True, strict = False), Pt4EC7h(-694, -156)), (2, 10, 4)))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(settings4EPC, 3, 5)
(61, ((4087, 724, -1984), (-694, -156)), 2, (3, 0, 5))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(settings4EPC, 3, 4)
(None, (4087, ((4087, 724, -1984), (-694, -156)), (Ops4EllipticPseudocurve7DropY(4087, 724, -1984, detect6Incapable = True, strict = False), Pt4EC7h(-694, -156)), (4, 4, 2)))







>>> try1_factor_pint__elliptic_curve_method7inversionless_(35) #doctest: +SKIP
(7, ((35, -3, 1), (-8, 1)), 1, (13, 3))
(5, ((35, 10, 1), (-10, 1)), 1, (13, 3))
(5, ((35, -16, 1), (-3, 1)), 1, (13, 3))
(None, (35, ((35, 5, 1), (-7, 1)), (Ops4EllipticPseudocurve7DropY(35, 5, 1, detect6Incapable = True, strict = False), Pt4EC7h(-7, 1)), (10000, 1000000, 996)))
(None, (35, ((35, 5, 1), (15, 1)), (Ops4EllipticPseudocurve7DropY(35, 5, 1, detect6Incapable = True, strict = False), Pt4EC7h(15, 1)), (10000, 1000000, 996)))

>>> try1_factor_pint__elliptic_curve_method7inversionless_(((35, -3, 1), (-8, 1)))
(7, ((35, -3, 1), (-8, 1)), 1, (13, 3))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(((35, -16, 1), (-3, 1)))
(5, ((35, -16, 1), (-3, 1)), 1, (13, 3))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(((35, 5, 1), (15, 1)))
(None, (35, ((35, 5, 1), (15, 1)), (Ops4EllipticPseudocurve7DropY(35, 5, 1, detect6Incapable = True, strict = False), Pt4EC7h(15, 1)), (10000, 1000000, 996)))






>>> M677 = -1+2**677
>>> M677 == (1943118631 * 531132717139346021081 * 978146583988637765536217 * 53625112691923843508117942311516428173021903300344567 * 11583306121194302925666610180475654822154587629577979400456857120235319057709961541850271218784399)
True
>>> n = M677
>>> d = 8689346476060549
>>> p53_6M677 = 53625112691923843508117942311516428173021903300344567
>>> order4EC_6d_6p53_6M677 = (2**4 * 3**9 * 3079 * 152077 * 172259 * 1067063 * 3682177 * 3815423 * 8867563 * 15880351)
>>> B1 = 11000000 # = 11*10**6
>>> B2 = 100*B1

>>> (ops, pt_0) = Ops4EllipticPseudocurve7DropY.mk_ex5n__7random_(n, strict=True, _d6strict=d)
>>> (ops, pt_0)
(Ops4EllipticPseudocurve7DropY(627057063764139831929324851379409869378845668175598843037877190478889006888518431438644711527536922839520331484815861906173161536477065546885468336421475511783984145060592245840032548652210559519683510271, -97503043140353293616716817776289974619720666565578128279768174236064446902549981253020389277636140137436330940980987543036725248, 59845263566661426996686823339816783683161195519714360280201674769083690967660287554949519535161429195284222362624), Pt4EC7h(430449974945880598783931876255267955898481599517755304563988950914481375606025154356242953187136, 41989559385379681935948478478770327184783721545536))

>>> pt7expected_partial_O = ops.mul7h_(order4EC_6d_6p53_6M677, pt_0)
>>> pt7expected_partial_O.eq_partial_zero_mod_(n)
True
>>> p53_6M677 == gcd(n, pt7expected_partial_O.Z)
True

>>> ops.mul7h_(order4EC_6d_6p53_6M677, Pt4EC7h(1, 1)).eq_partial_zero_mod_(n)
True
>>> ops.mul7h_(order4EC_6d_6p53_6M677, Pt4EC7h(3, 1)).eq_partial_zero_mod_(n)
True

>>> ops.mul7h_(order4EC_6d_6p53_6M677, Pt4EC7h(2, 1)).eq_partial_zero_mod_(n) # pt @twist_EC
False
>>> ops.mul7h_(order4EC_6d_6p53_6M677, Pt4EC7h(4, 1)).eq_partial_zero_mod_(n) # pt @twist_EC
False

# EC or twist_EC: [g? *y**2 == rhs{x}]
# [Jacobi_symbol(p;rhs{x}) -> (0|-1|+1)]
# %p => [len(EC)+len(twist_EC) == 2+2*p] # 『2+』for two pt7h_O
>>> ops.mul7h_(2+2*p53_6M677-order4EC_6d_6p53_6M677, Pt4EC7h(2, 1)).eq_partial_zero_mod_(n) # pt @twist_EC
True
>>> ops.mul7h_(2+2*p53_6M677-order4EC_6d_6p53_6M677, Pt4EC7h(4, 1)).eq_partial_zero_mod_(n) # pt @twist_EC
True













[[
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   ,iter_prepare4Ops4EllipticPseudocurve7DropY_  =35
    ... ...
    FoundNonTrivialFactor(35, 5, (35, 17, -16))
    FoundNonTrivialFactor(35, 7, (35, -6, 7))
    ... ...
    ^KeyboardInterrupt

py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   ,iter_prepare4Ops4EllipticPseudocurve7DropY_  =35 -strict
    (Ops4EllipticPseudocurve7DropY(35, 16, 1, strict = False), Pt4EC7h(8, 1))

py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   ,iter_prepare4Ops4EllipticPseudocurve7DropY_  =143 +strict
    ... ...
    FoundNonTrivialFactor(143, 11, (143, -2, -66))
    FoundNonTrivialFactor(143, 13, (143, -2, -12))
    ... ...
    ^KeyboardInterrupt

py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   ,iter_prepare4Ops4EllipticPseudocurve7DropY_  ='61*67' +strict
    (Ops4EllipticPseudocurve7DropY(4087, 724, -1984), Pt4EC7h(-694, -156))

]]

py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @f

]]]'''#'''
__all__ = r'''
try1_factor_pint__elliptic_curve_method7inversionless_
    prepare4criteria4ECM7inversionless_



try1_factor_pint__elliptic_curve_method_
    default__dup_exps_from_B1_
    default__delta_exps_from_B1_B2_
    prepare4factor_pint__elliptic_curve_method_




try_factor_pint__elliptic_curve_method_
    default__ks5n_and_B_or_ks_
        default__ks5n_and_B_
    ex1_try_factor_pint__elliptic_curve_method_



Ops4EllipticPseudocurve
    Pt4EC
    ZeroPt4EC
        pt_O


Ops4EllipticPseudocurve7DropY
    Pt4EC7h
        pt7h_O
    iter_prepare4Ops4EllipticPseudocurve7DropY_


FoundFactor
    FoundNonTrivialFactor
    FoundTrivialFactor
Incapable__add7h__X6diff_eq0
ParamError__ops4EPC7DropY



to_even_ge_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    #low_level_API:iter_sieve4primes_ge_lt_ --> high_level_API:iter_primes__ge_lt_
    from seed.math.prime_sieve.primes_ge_lt import iter_primes__ge_lt_# iter_filter4primes_ge_lt_
    #from seed.math.prime_sieve.sieve_ge_le import iter_sieve4primes_ge_lt_
    from seed.math.floor_ceil_tools.fc_log import ceil_log_, floor_log_
    from seed.math.factor_pint.perfect_power.detect_perfect_power import factor_pint_as_perfect_power_
    from seed.math.inv_mod__py_ import inv_mod__py_
    from seed.math.hrem_ import hrem_, mk_hrem_
    from seed.math.gcd import gcd, are_coprime
    from seed.math.II import II_mod
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
    from seed.tiny_.check import check_type_is, check_int_ge, check_callable
    from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple_, mk_namedtuple__check6make_
    #def mk_namedtuple_(__module__, nm, nms_or_str, /, *args, **kwds):
    #def mk_namedtuple__check6make_(__module__, nm, nms_or_str, /, *args, **kwds):
    #    def _check6make_(sf, /):

    #from seed.tiny_.singleton import mk_SingletonClass
    #def mk_SingletonClass(module_qname, type_qname, /, *bases, **kw):

    from random import randrange
    from seed.helper.ifNone import ifNone, ifNonef
    from seed.helper.repr_input import repr_helper


    from math import isqrt
    from itertools import repeat, cycle, islice

#.#################################
___end_mark_of_excluded_global_names__0___ = ...
#e script/整数分解牜凑平方牜凑整除幂.py


__all__
#class NotImplementedError__add7h__X6diff_eq0(NotImplementedError):pass
class Incapable__add7h__X6diff_eq0(BaseException):pass
class ParamError__ops4EPC7DropY(BaseException):pass

class FoundFactor(BaseException):
    def __init__(sf, n, ft, ctx=None, /):
        check_int_ge(1, ft)
        check_int_ge(ft, n)
        if not n%ft == 0:raise ValueError(n, ft, ctx)
        sf._n = n
        sf._ft = ft
        sf._ctx = ctx
        super().__init__(n, ft, ctx)
        assert ft == sf.factor
        assert ft == sf.args[1]
    @property
    def N(sf, /):
        return sf._n
    @property
    def factor(sf, /):
        return sf._ft
    @property
    def ctx(sf, /):
        return sf._ctx

class FoundNonTrivialFactor(FoundFactor):pass
class FoundTrivialFactor(FoundFactor):pass

_Pt4EC7h = mk_namedtuple_(__name__, '_Pt4EC7h', 'X Z')
class Pt4EC7h(_Pt4EC7h):
    # Ops4EllipticPseudocurve7DropY
    def __new__(cls, X, Z, /):
        if Z == 0:
            X = 0
        sf = super(__class__, cls).__new__(cls, X, Z)
        return sf
    def diff7h_(sf, ot, /):
        '-> sf.Z*ot.Z*(sf.X/sf.Z - ot.X/ot.Z)'
        return (sf.X*ot.Z - ot.X*sf.Z)
    def diff7h7mod_(sf, n, ot, /):
        '-> sf.Z*ot.Z*(sf.X/sf.Z - ot.X/ot.Z) %n'
        return sf.diff7h_(ot) %n
    def eq7h7mod_(sf, n, ot, /):
        #bug:return sf == ot or 0 == sf.diff7h7mod_(n, ot)
        #   !! diff7h7mod_()->0 @pt7h_O
        if sf == ot:return True
        if sf.eq_zero_():
            return ot.eq_zero_()
        if ot.eq_zero_():
            return False
            return sf.eq_zero_()
        return 0 == sf.diff7h7mod_(n, ot)
    def partial_eq7h7mod_(sf, n, ot, /):
        #bug:return not 1 == gcd(n, sf.diff7h7mod_(n, ot))
        #   !! diff7h7mod_()->0 @pt7h_O
        if sf == ot:return True
        if sf.eq_zero_():
            return ot.eq_partial_zero_mod_()
        if ot.eq_zero_():
            return sf.eq_partial_zero_mod_()
        return not 1 == gcd(n, sf.diff7h7mod_(n, ot))
    def eq_zero_(sf, /):
        return 0 == sf.Z
    def eq_partial_zero_mod_(sf, n, /):
        return not 1 == gcd(n, sf.Z)
pt7h_O = Pt4EC7h(0, 0)


Pt4EC = mk_namedtuple_(__name__, 'Pt4EC', 'x y')
    # Ops4EllipticPseudocurve
class ZeroPt4EC:
    # Ops4EllipticPseudocurve
    def __new__(cls, /):
        try:
            return pt_O
        except NameError:
            pass
        sf = super(__class__, cls).__new__(cls)
        return sf
    def __repr__(sf, /):
        return 'pt_O'
    def __reduce__(sf, /):
        return 'seed.math.factor_pint.factor_pint__elliptic_curve_method.pt_O'
pt_O = ZeroPt4EC()
assert pt_O is ZeroPt4EC()

r'''[[[
[Y**2 =[%n]= X**3+a*X+b]
[gcd(n,(4*a**3+27*b**2)) == 1]

[Y**2 =[%n]= X**3+C*X**2+A*X+B]
[g=!=0][h=!=0]:
    [twist_EC{g,EC} := [g*Y**2 =[%n]= X**3+C*X**2+A*X+B]]
    [twist_EC{g,EC} ~=~ twist_EC{g*h**2,EC}]
    [Y:=_Y/g**2][X:=_X/g]
    [_Y**2 =[%n]= _X**3+g*C*_X**2+g**2*A*_X+g**3*B]
[Y**2*Z =[%n]= X**3+C*X**2*Z+A*X*Z**2+B*Z**3]
    [O == (0,1,0)]
        #the point at infinity
[gcd(n,(4*A**3+27*B**2-18*A*B*C-A**2*C**2+4*B*C**3)) == 1]
[-O == O]
[-P == (P.x,-P.y)]
[O+P == P]
[-P+P == O]
[[Q =!= -P] -> [P+Q == R] -> [slope:=if P.x == Q.x then (3*P.x**2+2*C*P.x+A)/(2*P.y) else (P.y-Q.y)/(P.x-Q.x)] -> [R.x==slope**2-C-P.x-Q.x][R.y==-(P.y+slope*(R.x-P.x))]]
    #注意:负号:斜率+镜像 得 -R.y
    #B? 无用？
    # [g==1]
    [Q =!= -P][P.x==Q.x]:
        [P==Q]
        [slope**2 == (3*x**2+2*C*x+A)**2/(4*y**2) ==  (3*x**2+2*C*x+A)**2/4/(x**3+C*x**2+A*x+B)] #无y
    [Q =!= -P][P.x=!=Q.x]:
        [P=!=Q]
        [slope**2 == dy**2/dx**2 == ???y似乎不可避免...]
        [y1**2 -y2**2 == (x1**3 -x2**3) +a*(x1-x2) == fff(x1,x2)]
        [slope == (y1-y2)/(x1-x2) == (x1**2 +x1*x2 +x2**2 +a)/(y1+y2)]
        其实是要求提供更多参数:
            [addh_(P,Q,P-Q) := ...]
        [slope{P+Q}*slope{P-Q} == (yP**2 -yQ**2)/(xP-xQ)**2]
        [slope{P+Q}**2 == fff(x1,x2)**2/(xP-xQ)**4 /slope{P-Q}**2]
        [x{P+Q}==slope{P+Q}**2-C-xP-xQ]
        [x{P-Q}==slope{P-Q}**2-C-xP-xQ]
        [slope{P+Q}**2 == x{P+Q}+C+xP+xQ]
        [slope{P-Q}**2 == x{P-Q}+C+xP+xQ]

    ##################
    [g*Y**2 =[%n]= X**3+C*X**2+A*X+B][Q =!= -P][P.x=!=Q.x]:
        [P=!=Q]
        [Y:=_Y/g**2][X:=_X/g]
        [_Y**2 =[%n]= _X**3+g*C*_X**2+g**2*A*_X+g**3*B]
        ==>>:
        [_slope{P+Q} == ((_yP-_yQ)/(_xP-_xQ))]
        [_slope{P-Q} == ((_yP+_yQ)/(_xP-_xQ))]
        [_x{P+Q} == _slope{P+Q}**2-g*C-_xP-_xQ]
        [_x{P-Q} == _slope{P-Q}**2-g*C-_xP-_xQ]
        ==>>:
        [_slope{P+Q}/g == ((_yP/g**2-_yQ/g**2)/(_xP/g-_xQ/g)) == ((yP-yQ)/(xP-xQ)) == slope{P+Q}]
        [_slope{P-Q}/g == ((_yP/g**2+_yQ/g**2)/(_xP/g-_xQ/g)) == ((yP+yQ)/(xP-xQ)) == slope{P-Q}]
        [x{P+Q} == _x{P+Q}/g == g*(_slope{P+Q}/g)**2-C-_xP/g-_xQ/g == g*slope{P+Q}**2-C-xP-xQ]]
        [x{P-Q} == _x{P-Q}/g == g*(_slope{P-Q}/g)**2-C-_xP/g-_xQ/g == g*slope{P-Q}**2-C-xP-xQ]]
        ==>>:
        [x{P+Q} == g*slope{P+Q}**2-C-xP-xQ]]
        [x{P-Q} == g*slope{P-Q}**2-C-xP-xQ]]
        [slope{P+Q} == ((yP-yQ)/(xP-xQ))]
        [slope{P-Q} == ((yP+yQ)/(xP-xQ))]
        ==>>:

        [x{P+Q} +x{P-Q}
        == g*slope{P+Q}**2 +g*slope{P-Q}**2 -2*C -2*(xP+xQ)
        == 2*(g*yP**2+g*yQ**2)/(xP-xQ)**2 -2*C -2*(xP+xQ)
        == 2*((xP**3+C*xP**2+A*xP+B)+(xQ**3+C*xQ**2+A*xQ+B) -C*(xP-xQ)**2 -(xP+xQ)*(xP-xQ)**2)/(xP-xQ)**2
        == 2*(A*(xP+xQ)+2*B +2*C*xP*xQ +xP*xQ*(xP+xQ))/(xP-xQ)**2
        == 2*(((xP*xQ)+A)*(xP+xQ)+2*(C*(xP*xQ)+B))/(xP-xQ)**2
            # == 2*((M+A)*H+2*(C*M+B))/S**2
        ]
        [x{P+Q} +x{P-Q} == 2*(A*(xP+xQ)+2*B +2*C*xP*xQ +xP*xQ*(xP+xQ))/(xP-xQ)**2]
            #formula4edgecase4addh_:here

        [x{P+Q} * x{P-Q}
        == (g*slope{P+Q}**2 -C -(xP+xQ))*(g*slope{P-Q}**2 -C -(xP+xQ))
        == (g*slope{P+Q}*slope{P-Q})**2 -(C +(xP+xQ))*(g*slope{P+Q}**2+g*slope{P-Q}**2) +(C +(xP+xQ))**2
        == ((g*yP**2-g*yQ**2)/(xP-xQ)**2)**2 -(C +(xP+xQ))*2*(g*yP**2+g*yQ**2)/(xP-xQ)**2 +(C +(xP+xQ))**2
        # (g,yP,yQ)都消失！
        == (((xP**3+C*xP**2+A*xP+B)-(xQ**3+C*xQ**2+A*xQ+B))/(xP-xQ)**2)**2 -(C +(xP+xQ))*2*((xP**3+C*xP**2+A*xP+B)+(xQ**3+C*xQ**2+A*xQ+B))/(xP-xQ)**2 +(C +(xP+xQ))**2
        == (((xP+xQ)**2-xP*xQ+C*(xP+xQ)+A)/(xP-xQ))**2 -(C +(xP+xQ))*2*((xP+xQ)**3-3*xP*xQ*(xP+xQ)+C*(xP+xQ)**2-2*C*xP*xQ+A*(xP+xQ)+2*B)/(xP-xQ)**2 +(C +(xP+xQ))**2
        :> [S:=(xP-xQ)][H:=(xP+xQ)][M:=(xP*xQ)]
        == ((H**2-M+C*H+A)/S)**2 -(C+H)*2*(H**3-3*M*H+C*H**2-2*C*M+A*H+2*B)/S**2 +(C+H)**2
        !! [S**2 == (H**2-4*M)]
        == ((H**2-M+C*H+A)**2 -(C+H)*2*(H**3-3*M*H+C*H**2-2*C*M+A*H+2*B) +(C+H)**2*(H**2-4*M))/S**2
        !! PARI_GP:[((H^2-M+C*H+A)^2 -(C+H)*2*(H^3-3*M*H+C*H^2-2*C*M+A*H+2*B) +(C+H)^2*(H^2-4*M)) == (-4*B*H + (M^2 - 2*A*M + (-4*B*C + A^2)))]
        == (-4*B*H + M**2 -2*A*M -4*B*C +A**2)/S**2
        == ((M-A)**2 -4*B*(H+C))/S**2
        == (((xP*xQ)-A)**2 -4*B*((xP+xQ)+C))/(xP-xQ)**2
        ]
        [x{P+Q} * x{P-Q} == (((xP*xQ)-A)**2 -4*B*((xP+xQ)+C))/(xP-xQ)**2]
        [[B==0] -> [x{P+Q} * x{P-Q} == (((xP*xQ)-A)**2)/(xP-xQ)**2]]
    ##################
    [g*Y**2 =[%n]= X**3+C*X**2+A*X+B][Q =!= -P][P.x==Q.x]:
        [P==Q] # => doubleh_()
        !! [Q =!= -P]
        [2*P == P+P == P+Q =!= P+(-P) == O]
        [2*P =!= O]
        [P.y==0]:
            [-P == P == Q]
            !! [Q =!= -P]
            _L
        [P.y=!=0]
        [yP=!=0]
        [Y:=_Y/g**2][X:=_X/g]
        [_Y**2 =[%n]= _X**3+g*C*_X**2+g**2*A*_X+g**3*B]
        [_yP == g*yP =!=0]
        ==>>:
        [P-Q == O]
        [_slope{P+Q} == ((3*_xP**2+2*g*C*_xP+g**2*A)/(2*_yP))]
        [_x{P+Q} == _slope{P+Q}**2-g*C-_xP-_xQ]
        ==>>:
        [_slope{P+Q} == ((3*(_xP/g)**2+2*C*_xP/g+A)/(2*_yP/g**2)) == ((3*xP**2+2*C*xP+A)/(2*yP)) == slope{P+Q}]
        [x{P+Q} == _x{P+Q}/g == _slope{P+Q}**2/g -C-_xP/g-_xQ/g == slope{P+Q}**2/g -C-xP-xQ]
        ==>>:
        [slope{P+Q} == ((3*xP**2+2*C*xP+A)/(2*yP))]
        [x{P+Q} == slope{P+Q}**2/g -C-2*xP]
        ==>>:
        [x{P+Q}
        == slope{P+Q}**2/g -C-2*xP
        == ((3*xP**2+2*C*xP+A)/(2*yP))**2/g -C-2*xP
        == ((3*xP**2+2*C*xP+A)**2/(4*g*yP**2)) -C-2*xP
        # (g,yP,yQ)都消失！
        == ((3*xP**2+2*C*xP+A)**2/4/(xP**3+C*xP**2+A*xP+B)) -C-2*xP
        == ((3*xP**2+2*C*xP+A)**2 -(C+2*xP)*4*(xP**3+C*xP**2+A*xP+B))/4/(xP**3+C*xP**2+A*xP+B)
        !! PARI_GP:[((3*xP^2+2*C*xP+A)^2 -(C+2*xP)*4*(xP^3+C*xP^2+A*xP+B))== (-4*B*C + (A^2 - 2*xP^2*A + (-8*xP*B + xP^4)))]
        == (-4*B*C -8*xP*B +A**2 -2*xP**2*A +xP**4)/4/(xP**3+C*xP**2+A*xP+B)
        == ((xP**2+A)**2 -4*B*(2*xP+C))/4/(xP**3+C*xP**2+A*xP+B)
        ]
        [x{P+Q} == ((xP**2+A)**2 -4*B*(2*xP+C))/4/(xP**3+C*xP**2+A*xP+B)]
        [P-Q == O]
        [[B==0] -> [x{P+Q} == ((xP**2+A)**2)/4/(xP**3+C*xP**2+A*xP+B)]]
    ##################
    综上:
    ##################
    [g*Y**2 =[%n]= X**3+C*X**2+A*X+B][Q =!= -P][P.x=!=Q.x]:
        [P=!=Q]
        [x{P+Q} * x{P-Q} == (((xP*xQ)-A)**2 -4*B*((xP+xQ)+C))/(xP-xQ)**2]
        [[B==0] -> [x{P+Q} * x{P-Q} == (((xP*xQ)-A)**2)/(xP-xQ)**2]]
    [g*Y**2 =[%n]= X**3+C*X**2+A*X+B][Q =!= -P][P.x==Q.x]:
        [P==Q] # => doubleh_()
        [2*P =!= O]
        [P-Q == O]
        [x{P+Q} == ((xP**2+A)**2 -4*B*(2*xP+C))/4/(xP**3+C*xP**2+A*xP+B)]
        [[B==0] -> [x{P+Q} == ((xP**2+A)**2)/4/(xP**3+C*xP**2+A*xP+B)]]
    ##################
    [g*(Y/Z)**2 =[%n]= (X/Z)**3+C*(X/Z)**2+A*(X/Z)+B]
    [g*Y**2*Z =[%n]= X**3+C*X**2*Z+A*X*Z**2+B*Z**3]
    [g*Y**2*Z =[%n]= X**3+C*X**2*Z+A*X*Z**2+B*Z**3][Q =!= -P][xP/zP=!=xQ/zQ]:
        [P=!=Q][xPzQ=!=xQzP]
        [x{P+Q}/z{P+Q} * x{P-Q}/z{P-Q} == (((xP/zP*xQ/zQ)-A)**2 -4*B*((xP/zP+xQ/zQ)+C))/(xP/zP-xQ/zQ)**2]
        [x{P+Q} / z{P+Q} == z{P-Q}*(((xP*xQ)-A*(zP*zQ))**2 -4*B*((xP*zQ+xQ*zP)+C*(zP*zQ))*(zP*zQ)) / (x{P-Q}*(xP*zQ-xQ*zP)**2)]
        #formula4main4addh_:here
        [x{P+Q} / z{P+Q} == z{P-Q}*((xPxQ-A*zPzQ)**2 -4*B*((xPzQ+xQzP)+C*zPzQ)*zPzQ) / (x{P-Q}*(xPzQ-xQzP)**2)]
        [[B==0] -> [x{P+Q} / z{P+Q} == z{P-Q}*((xPxQ-A*zPzQ)**2) / (x{P-Q}*(xPzQ-xQzP)**2)]]
            # better:[A:=1]
        前提:[x{P-Q}*z{P-Q} =!= 0]

    [g*Y**2*Z =[%n]= X**3+C*X**2*Z+A*X*Z**2+B*Z**3][Q =!= -P][xP/zP==xQ/zQ]:
        [P==Q][xPzQ==xQzP] # => doubleh_()
        [2*P =!= O]
        [P-Q == O]
        [x{P+Q}/z{P+Q} == (((xP/zP)**2+A)**2 -4*B*(2*xP/zP+C))/4/((xP/zP)**3+C*(xP/zP)**2+A*xP/zP+B)]
        [x{P+Q} / z{P+Q} == ((xPxP+A*zPzP)**2 -4*B*(2*xPzP+C*zPzP)*zPzP) / (4*((xPxP*xPzP)+C*xPzP**2+A*(xPzP*zPzP)+B*zPzP**2))]
        #formula4doubleh_:here
        [x{P+Q} / z{P+Q} == ((xPxP+A*zPzP)**2 -4*B*(2*xPzP+C*zPzP)*zPzP) / (4*((xPxP+C*xPzP+A*zPzP)*xPzP+B*zPzP**2))]
        [[B==0] -> [x{P+Q} / z{P+Q} == ((xPxP+A*zPzP)**2) / (4*((xPxP+C*xPzP+A*zPzP)*xPzP))]]
            # [A_zPzP:=A*zPzP]
            # better:[A:=1]
        无前提
    ##################
    def doubleh_(P) -> (2*P):
        #formula4doubleh_:goto
        ... ...
    def addh_(P, Q, P-Q) -> (P+Q):
        #the “h” in the function name emphasizing the homogeneous nature of each [X : Z] pair.
        # (P-Q)用以校准方向，类似super(__class__, cls)
        #   实际上 可通过 一元二次方程 得到函数:[[xP/zP =!= xQ/zQ] => (xP/zP, xQ/zQ) -> {x{P-Q},x{P+Q}}]
        #   (x{P-Q} + x{P+Q})见:formula4edgecase4addh_:goto
        #   (x{P-Q} * x{P+Q})见:formula4main4addh_:goto
        # eg: [(2+2*k)*P := addh_((1+k)*P, (1+k)*P, O) == doubleh_((1+2*k)*P)]
        # eg: [(1+2*k)*P := addh_((1+k)*P, (0+k)*P, P)]
        # eg: [(0+2*k)*P := addh_((0+k)*P, (0+k)*P, O) == doubleh_((2*k)*P)]
        [(xP / zP) := P]
        [(xQ / zQ) := Q]
        [(x{P-Q} / z{P-Q}) := P-Q]
        if zP==0:
            # [P == O]
            return Q
        if zQ==0:
            # [Q == O]
            return P
        if z{P-Q}==0:
            # [P-Q == O]
            # [P == Q]
            # [xPzQ==xQzP]
            return doubleh_(P)
        # [P =!= O]
        # [Q =!= O]
        # [P =!= Q]
        # [xPzQ=!=xQzP]
        if xPzQ == -xQzP:
            # [xPzQ==-xQzP]
            # [P == -Q]
            # [P+Q == O]
            return O
        # [P =!= -Q]
        if x{P-Q}==0:
            ???undefined???
            #低效:formula4edgecase4addh_:goto
            #分解整数时用不上，因为[P-Q===pt6init][pt6init=!=O][另需初始化指派:[pt6init.x =!= 0]]
            raise 000
        # now: 符合前提:[x{P-Q}*z{P-Q} =!= 0]
        #formula4main4addh_:goto
        ... ...
    ##################


3 points on the curve are collinear if and only if they sum to 0.
    This interpretation is generalized to allow for a double intersection at a point of tangency
        (unless it is an inflection point, in which case it is a triple intersection).
    Finally, the geometrical interpretation takes the view that vertical lines intersect the curve at the point at infinity.

[@[p::prime{>3}] -> @[k::uint{>=1}] -> ?[d1,d2::uint{>=1}] -> [EC{FF{p**k}} ~=~ ZZ%d1 * ZZ%d2][gcd(d2, -1+p**k)%d1 == 0]]
    # [d1==1] => cyclic group

[@[p::prime{>3}] -> @[k::uint{>=1}] -> [(len(EC{FF{p**k}}) -(1+p**k))**2 <= 4*p**k]]
    [@[p::prime{>3}] -> @[k::uint{>=1}] -> [abs(len(EC{FF{p**k}}) -(1+p**k)) <= 2*p**(k/2)]]
    当[k%2==1]时，等号不成立:
    [@[p::prime{>3}] -> [(len(EC{ZZ%p}) -(1+p))**2 < 4*p]]
    [@[p::prime{>3}] -> [abs(len(EC{ZZ%p}) -(1+p)) < 2*sqrt(p)]]
    [@[p::prime{>3}] -> [abs(len(EC{ZZ%p}) -(1+p)) <= 2*floor_sqrt(p)]]
    [@[p::prime{>3}] -> [(1+p) -2*floor_sqrt(p) <= len(EC{ZZ%p}) <= (1+p) +2*floor_sqrt(p)]]
        强:只要在此范围内，必然存在某相应曲线#但分布应当是不均匀的
        [m:=len(EC{ZZ%p})]
        What the Deuring theorem actually says is that the number of curves—up to isomorphism—of order m is the so-called Kronecker class number of ((p+1−m)**2−4*m).

affine coordinates:(x,y)|O
    generally involving an inversion for a curve operation.
projective coordinates:(X,Y,Z)
    avoid inversions.
    (X,Y,0) ~ (0,1,0) # vs:O
    (X,Y,Z) ~ (X/Z,Y/Z,1) # vs:(x,y)
modified projective coordinates:(X,Y,Z)
    avoid inversions.
    has a lower operation count than projective coordinates.
    (X,Y,0) ~ (0,1,0) # vs:O
    (X,Y,Z) ~ (X/Z**2,Y/Z**3,1) # vs:(x,y)
    [(Y/Z**3)**2 =[%n]= (X/Z**2)**3 +a*(X/Z**2) +b]
    [Y**2 =[%n]= X**3 +a*X*Z**4 +b*Z**6]
    [O:=[0,1,0]]
    [double_([_,_,0]) == O]
    [double_([_,0,_]) == O]
        ???why???即便(ZZ%p)而非(ZZ%n)，也可能有3个不同根x。
            !! [[P.Y==0] -> [P == -P]]
            !! [[P == -P] -> [2*P == O]]
            [[P.Y==0] -> [2*P == O]]
    [double_([X,Y{=!=0},Z{=!=0}]) == let [M:=3*X**2+a*Z**4][S:=4*X*Y**2][_X:=M**2-2*S][_Y:=M*(S-_X)][_Z:=2*Y*Z] in [_X,_Y,_Z]]
        #原文bug:『[_Y:=M*(S-X2)]』
        #fixed:通过观察:以Z为单位: X:2,Y:3,Z:1,M:4,S:8,_X:8,_Y:12,_Z:4 => 『X2』应当是『_X』或『X**4』
    [add_(O,P) == P]
    [add_(P,O) == P]
    [add_(P{=!=O},Q{=!=O}) == let [[(xP,yP,zP):=P][(xQ,yQ,zQ):=Q][uP:=xQ*zP**2][uQ:=xP*zQ**2][sP:=yQ*zP**3][sQ:=yP*zQ**3][du:=uP-uQ][ds:=sP-sQ][u2:=uP+uQ][s2:=sP+sQ]] in if [du==0==ds] then double_(P) elif [du==0=!=ds] then (if [s2==0] then O else ^gcd) else let [tmp:=u2*du**2][_X:=ds**2-tmp][_Y:=2**-1 *((tmp-2*_X)*ds -s2*du**3)][_Z:=zP*zQ*du] in (_X,_Y,_Z)]
        #以Z为单位: X:2,Y:3,Z:1,u:4,s:6,tmp:12,_X:12,_Y:18,_Z:6
Montgomery coordinates:(X,Z)
    (X,0) ~ (0,1,0) # vs:O
    (X,Z) ~ (X/Z,?,1) # vs:(x,y)
    !! 使用了特别的形式:[g*Y**2 == X**3+C*X**2+X]
    which are the same as the projective coordinates [X,Y,Z], but with "Y" dropped.
    One can recover the x coordinate of the affine point when Z =!= 0 as x = X/Z.
        There are generally two possibilities for y, and this is left ambiguous.
    This option tends to work well in elliptic multiplication and when y-coordinates are not needed at any stage
        #{见上面:addh_()}:y似乎不可避免，而且:如何区分 2*P vs P+(-P) 如何区分P+Q vs P-Q
        ####？P+Q vs P-Q:加减法得到同样的X坐标值？非是，而是增添参数(P-Q)以甄别: #formula4main4addh_:goto
        , as sometimes happens in certain factorization and cryptography work, or when the elliptic algebra must be carried out in higher domains where coordinates themselves can be polynomials.

Theorem 7.4.3 (ECM curve construction)
    [d !<- {0,1,5}]
    [u:=d**2-5]
    [v:=d*4]
    [C(d):=-2 +(v-u)**3*(3*u+v)/(4*u**3*v)]
    [EC{d;ZZ%p} := [Y**2 =[%p]= X**3+C(d)*X**2+X]]
    [len(EC{d;ZZ%p})%12 == 0]
    [?[pt :: point{x==(u/v)**3}] -> [pt <- (EC{d;ZZ%p} | EC{d;ZZ%p}.twist)]]
        What is more, we do not even care whether an initial point is on E or its twist, again because y-coordinate ignorance is allowed.
        初始点:[X/Z == u**3/v**3] 忽略Y值，不在意用的是(EC{d;ZZ%p} | EC{d;ZZ%p}.twist)

stage1:第一阶段:
    [P1:=II(ks{B1})*P0]
        default__ks5n_and_B_()
        default__dup_exps_from_B1_
stage2:第二阶段:
    前提:P1幸存，没有^FoundNonTrivialFactor
    经验:占比{第二阶段耗时/总耗时} <- [1/4 ~ 1/2]
        [B2 := 100*B1]
    [P{k,P1} =[def]= k*P1]
    [q1 := next_prime_(1+B1)]
    [P{q1,P1} := q1*P1]
    for q1,q2 in pairwise(primes_ge_lt(q1,1+B2)):
        [dq := (q2-q1)]
        [P{dq,P1} := cached(dq*P1)]
        [P{q2,P1} := P{q1,P1} +P{dq,P1}]
            但只需检测:gcd(n,(P{q1,P1}.X*P{dq,P1}.Z -P{q1,P1}.Z*P{dq,P1}.X))
            [X1*Zd -Z1*Xd == (X1-Xd)*(Z1+Zd) -X1*Z1 +Xd*Zd]
            少量{q1}+大量{dq}足以覆盖全部可能素数:检测累积gcd(n,II(...{q1}))

vs:discriminant/判别式:
    view others/app/termux/help/gp-example-polynomial-discriminant.txt
    ===
    [EC{(y**2 === x**3 +a*x +b)}]:
        required:[gcd(n,(4*a**3+27*b**2)) == 1]
        Ops4EllipticPseudocurve

    [EC{(g*y**2 === x**3 +C*x**2 +A*x +B)}]:
        required:[gcd(n,(4*A**3+27*B**2-18*A*B*C-A**2*C**2+4*B*C**3)) == 1]

    [EC{(g*y**2 === x**3 +C*x**2 +A*x)}][B:=0]:
        required:[gcd(n,(4*A**3-A**2*C**2)) == 1]

    [EC{(g*y**2 === x**3 +C*x**2 +A*x)}][B:=0][A:=1]:
        required:[gcd(n,(4-C**2)) == 1]
        Ops4EllipticPseudocurve7DropY

Theorem 7.2.6 (Generalized Montgomery identities).
[EC{(g*y**2 === x**3 +C*x**2 +A*x +B)}][P1==(x1,y1)][P1==(x2,y2)][P1+P2==(xp,yp)][P1-P2==(xn,yn)]:
    #一致前提:[P1=!=-P2]
    [P1=!=O][P2=!=O][x1=!=x2]:
        # [P1=!=P2]
        # [P1=!=-P2]
        [xp*xn == ((x1*x2-A)**2 -4*B*(x1+x2+C))/(x1-x2)**2]

    [P1=!=O][P2=!=O][x1==x2][2*P1=!=0][???我:[P1==P2]???]:
        # [2*P1=!=0] <==> [P1=!=-P1] <==> [0 == y1] <==> [0 == (x1**3 +C*x1**2 +A*x1 +B)]
        # [P1==P2] # => [xn不存在]#[O.X不存在]
        # [P1=!=-P2]
        [xp == ((x1*x2-A)**2 -4*B*(x1+x2+C))/(4*(x1**3 +C*x1**2 +A*x1 +B))]
            # lhs: xp*xn --> xp
            # rhs: 只有分母改变:分母非零 即是 前置条件
            #   分子简化@[B:=0]
# 简化:[B:=0][A:=1]
[EC{(g*y**2 === x**3 +C*x**2 +A*x +B)}][(x,y)==(X/Z,Y/Z)]:
    [EC{(g*Y**2*Z === X**3 +C*X**2*Z +A*X*Z**2 +B*Z**3)}]
[EC{(g*Y**2*Z === X**3 +C*X**2*Z +A*X*Z**2 +B*Z**3)}][P1==(X1,Y1,Z1)][P1==(X2,Y2,Z2)][P1+P2==(Xp,Yp,Zp)][P1-P2==(Xn,Yn,Zn)]:
    # [:define__addh]:here
    # h - homogeneous
    [P1==O]:
        [_addh((0:0),(X2:Z2),(X2:Z2)) =[def]= (X2:Z2)]

    [P2==O]:
        [_addh((X1:Z1),(0:0),(X1:Z1)) =[def]= (X1:Z1)]

    [P1=!=O][P2=!=O][P1==-P2][P1==+P2]:
        [2*P1==O]
        [P1==-P1]
        [Zn == 0]
        [X1*Z2 == X2*Z1]
        [P1.y == (-P1).y == -(P1.y)]
        [P1.y == 0]
        [0 == (X1**3 +C*X1**2*Z1 +A*X1*Z1**2 +B*Z1**3)]
        [_addh((X1:Z1),(X2:Z2),(Xn:Zn)) =[def]= (0:0)]

    [P1=!=O][P2=!=O][P1=!=-P2][P1==+P2]:
        [Zn == 0]
        [X1*Z2 == X2*Z1]
        [P1=!=-P1]
        [0 =!= (X1**3 +C*X1**2*Z1 +A*X1*Z1**2 +B*Z1**3)]
        [Xp := ((X1**2 -A*Z1**2)**2 -4*B*(2*X1 +C*Z1)*Z1**3)]
        [Zp := 4*Z1*(X1**3 +C*X1**2*Z1 +A*X1*Z1**2 +B*Z1**3)]
        [_addh((X1:Z1),(X1:Z1),(0:0)) =[def]= _doubleh((X1:Z1)) =[def]= (Xp:Zp)]

    above=>[P1=!=O][P2=!=O][P1=?=-P2][P1==+P2]:
        [Zn == 0]
        [X1*Z2 == X2*Z1]
        [0 =?= (X1**3 +C*X1**2*Z1 +A*X1*Z1**2 +B*Z1**3)]
        [Zp := 4*Z1*(X1**3 +C*X1**2*Z1 +A*X1*Z1**2 +B*Z1**3)]
        [Xp := ((X1**2 -A*Z1**2)**2 -4*B*(2*X1 +C*Z1)*Z1**3) if Zp =!= 0 else 0]
        [_addh((X1:Z1),(X1:Z1),(0:0)) =[def]= _doubleh((X1:Z1)) =[def]= (Xp:Zp)]
            # [:define__doubleh]:here

    [P1=!=O][P2=!=O][P1==-P2][P1=!=+P2]:
        [Zn =!= 0]
        [X1*Z2 == X2*Z1]
        [_addh((X1:Z1),(X2:Z2),(Xn:Zn)) =[def]= (0:0)]

    below:[P1=!=O][P2=!=O][P1=!=-P2][P1=!=+P2]:
        [Zn =!= 0]
        [X1*Z2 =!= X2*Z1]

    [P1=!=O][P2=!=O][P1=!=-P2][P1=!=+P2][Xn == 0]:
        [Zn =!= 0]
        [X1*Z2 =!= X2*Z1]
        raise Incapable__add7h__X6diff_eq0#[Xp:=???/Xn]

    [P1=!=O][P2=!=O][P1=!=-P2][P1=!=+P2][Xn =!= 0]:
        [Zn =!= 0]
        [X1*Z2 =!= X2*Z1]
        [Xp := Zn * ((X1*X2 -A*Z1*Z2)**2 -4*B*(X1*Z2 +X2*Z1 +C*Z1*Z2)*Z1*Z2)]
        [Zp := Xn * (X1*Z2 -X2*Z1)**2]
        [_addh((X1:Z1),(X2:Z2),(Xn:Zn)) =[def]= (Xp:Zp)]
        !! [P1-P2 =[repr]= (Xn:Zn) =[repr]= P2-P1]
        [_addh((X2:Z2),(X1:Z1),(Xn:Zn)) == (Xp:Zp)]

    def _addh(P1,P2,P1-P2):
    def _doubleh(P1)
    # formula4edgecase4addh_:goto
    # formula4main4addh_:goto
    # formula4doubleh_:goto
Algorithm 7.2.7 (Elliptic multiplication: Montgomery method).
    (X:Z)表达:
        [Z=!=0] => [x:=X/Z] # y至多2值
        [Z==0] => [(X:Z) == O]
        [O := (0:0)] # 或者:(X:0)
    output:
        [Q == (Q.X:Q.Z)]
    postcondition:
        [Q == mul_(k,P)]
    input:
        [EC{d;ZZ%M}]
        [k :: int{>=0}]
        [P == (P.X:P.Z)]
    precondition:
        [k >= 0]
        [P.X*P.Z %M =!= 0]
    def mul_(k, P):
    def mulh_(k, P):
        # [:define__mulh]:here
        if k == 0:
            return O # (0:0)
        if k == 1:
            return P # (X:Z)
        if k == 2:
            return _doubleh(P)
        UV := P
        TW := _doubleh(P)
        # [TW == UV + P]
        bits := radux_repr{big_endian;k}
        #原文应当有病蛊:『for j in [1..=len-1]:...;if bits[len-1]:...』简单地说 拆出最后一步:应当改为『len-2』
        for j, bit in enumerate(bits[1:], 1):
            # [TW == UV + P]
            # [k_ := int(bits[:j], base=2)]
            # [UV == k_*P]
            # [TW == (1+k_)*P]
            # [_k := int(bits[:1+j], base=2)]
            if bit == 1:
                # [_k == 1+2*k_]
                # !! [TW == UV + P]
                # [P == TW-UV]
                UV := _addh(TW,UV,P)
                TW := _doubleh(TW) # can omitted@final step
                # [UV == (1+2*k_)*P]
                # [TW == 2*(1+k_)*P]
                # !! [_k == 1+2*k_]
                # [UV == _k*P]
                # [TW == (1+_k)*P]
                # [TW == UV + P]
            else:
                # [_k == 0+2*k_]
                # !! [TW == UV + P]
                # [-P == UV-TW]
                # !! [P =[repr]= (X:Z) =[repr]= -P]
                TW := _addh(UV,TW,-P) # can omitted@final step
                    # <==> TW := _addh(TW,UV,P)
                UV := _doubleh(UV)
                # [UV == 2*k_*P]
                # [TW == (1+2*k_)*P]
                # !! [_k == 0+2*k_]
                # [UV == _k*P]
                # [TW == (1+_k)*P]
                # [TW == UV + P]
            # [UV == _k*P]
            # [TW == (1+_k)*P]
            # [TW == UV + P]
        # [UV == k*P]
        # [TW == (1+k)*P]
        # [TW == UV + P]
        return UV
Algorithm 7.4.4 (Inversionless ECM)
    # Inversionless => C 保留 分数形式！
    output:
        may non_trivial_factor{n}
    input:n,B1,B2,D
        [n > 0][1 == gcd(n,6)]
        [0 == B1%2][B1>=2]
        [0 == B2%2][B2>=B1]
        [D > 0]
        default:
        # choose_criteria:
        [B1:=10000]     # stage-one limit
        [B2:=100*B1]    # stage-two limit
        [D:=100]        # cache size
            # or:1+floor_sqrt(B2-B1)

    def ECM7inversionless_(n, B1, B2, D):
# [:define__ECM7inversionless]:here
def ECM7inversionless_(n, B1, B2, D):
    # choose_random_curve:
    # 简化:[B:=0][A:=1] => 只需 选择C
    # 选C:
    d = randrange(6, n)
    u = (d**2-5) %n
    v = 4*d %n
    C = Fraction(((v-u)**3 * (v+3*u) -2*(4*v*u**3))%n, (4*v*u**3) %n)
    # [y**2 == x**3 +C*x**2 +x]

    pt_0 = (u**3%n : v**3%n)

    #stage1:
    pt = pt_0
    for p in primes_ge_le(2, B1):
        for _ in range(floor_log_(p;B1)):
            pt = mulh_(p, pt)
    pt_1 = pt
    ft = gcd(n, pt_1.Z)
    if ft == n:...failure:goto choose_random_curve
    if 1 < ft < n:...ok:return ft
    assert 1 == ft

    #stage2:
    _2_1 = _doubleh(pt_1) # 2*pt_1
    _4_1 = _doubleh(_2_1) # 4*pt_1
    j2zjpt1 = [_2_1,_4_1]
        # ~ {j:(2+2*j)*pt_1}
    while len(j2zjpt1) < D:
        j2zjpt1.append(_addh(j2zjpt1[-1], j2zjpt1[-2], _2_1))
    j2zjpt1
    j2XZ = [X*Z%n for (X:Z) in j2zjpt1]

    # 由于 正负不定，所以 [(X1*Z2-X2*Z1) =?= partial0] 实际上 同时检验 [%p:X1/Z1=?=X2/Z2]即[%p:x1=?=x2]即[%p:P1=?=P2][%p:P1=?=-P2]即[P1+P2=?=partial_O][P1-P2=?=partial_O]
    #

    jpivot7fst = -1+B1 # fst_pivot_position
    # !! [0 == B1%2][B1>=2]
    # [1 == jpivot7fst%2]
    # [jpivot7fst >= 1]
    pt7pivot7prev = mulh_(jpivot7fst-4*D,pt_1)
    pt7pivot = mulh_(jpivot7fst-2*D,pt_1)
    pt7big_step = j2zjpt1[-1] # == (2*D)*pt_1
    # [jpivot7fst >= 1]
    IIdiffs = 1
    for jpivot in range(jpivot7fst, B2, 2*D):
        # [1 == jpivot%2]
        # [jpivot >= 1]
        (pt7pivot7prev, pt7pivot) = (pt7pivot, _addh(pt7pivot, pt7pivot7prev, pt7big_step))
        # [pt7pivot == mulh_(jpivot,pt_1)]
        XZ7pivot = pt7pivot.X*pt7pivot.Z %n
        for p in primes_ge_le(2+jpivot, jpivot+2*D):
            # !! [1 == jpivot%2]
            # !! [jpivot >= 1]
            # [p >= 3]
            # [1 == p%2]
            # [0 == (p-jpivot)%2]
            j = (p-2-jpivot)///2
            # [0 <= j < D]
            # [p == 2*j+2+jpivot == 2*(1+j) +jpivot]
            XZ7small_step = j2XZ[j]
            pt7small_step = j2zjpt1[j] # == 2*(1+j)*pt_1
            # [p*pt_1 == pt7small_step + pt7pivot]
            # [p*pt_1 =?= partial_O]
            # <==> [[q::prime] -> [0==n%q][%q:pt7pivot =?= -pt7small_step]]
            # <==> [[q::prime] -> [0==n%q][%q:pt7pivot.x =?= (-pt7small_step).x]]
            # !! [(-pt7small_step).x == pt7small_step.x] # 正负无y无法体现
            # <==> [[q::prime] -> [0==n%q][%q:pt7pivot.X/pt7pivot.Z =?= pt7small_step.X/pt7small_step.Z]]
            # <==> [[q::prime] -> [0==n%q][%q:pt7pivot.X*pt7small_step.Z =?= pt7small_step.X*pt7pivot.Z]]
            # <==> [[q::prime] -> [0==n%q][%q:0 =?= (pt7pivot.X*pt7small_step.Z -pt7small_step.X*pt7pivot.Z)]]
            # !! [(pt7pivot.X*pt7small_step.Z -pt7small_step.X*pt7pivot.Z) == (pt7pivot.X*pt7small_step.Z -pt7small_step.X*pt7pivot.Z)+(pt7pivot.X*pt7pivot.Z -pt7small_step.X*pt7small_step.Z) == (pt7pivot.X-pt7small_step.X)*(pt7pivot.Z+pt7small_step.Z)]
            # <==> [[q::prime] -> [0==n%q][%q:0 =?= (pt7pivot.X-pt7small_step.X)*(pt7pivot.Z+pt7small_step.Z) -(pt7pivot.X*pt7pivot.Z -pt7small_step.X*pt7small_step.Z)]]
            # <==> [[q::prime] -> [0==n%q][%q:0 =?= ((pt7pivot.X-pt7small_step.X)*(pt7pivot.Z+pt7small_step.Z) -(XZ7pivot -XZ7small_step))]]
            diff = ((pt7pivot.X-pt7small_step.X)*(pt7pivot.Z+pt7small_step.Z) -(XZ7pivot -XZ7small_step)) %n
            IIdiffs = IIdiffs*diff %n
        IIdiffs
    IIdiffs
    ft = gcd(n, IIdiffs)
    if ft == n:...failure:goto choose_random_curve
    if 1 < ft < n:...ok:return ft
    assert 1 == ft
    ...failure:goto choose_random_curve

end-def ECM7inversionless_(n, B1, B2, D):

# [examples__ECM]:here
实例一:
    # 原文bug: M667-->M677
    [n := M677 = -1+2**677]
    [d := 8689346476060549]
    [B1 := 11000000 = 11*10**6]
    [B2 := 100*B1]
    [M677 == (1943118631 * 531132717139346021081 * 978146583988637765536217 * 53625112691923843508117942311516428173021903300344567 * 11583306121194302925666610180475654822154587629577979400456857120235319057709961541850271218784399)]
    [p53{M677} := 53625112691923843508117942311516428173021903300344567]
    [len(EC{d;ZZ%p53{M677}}) == (2**4 * 3**9 * 3079 * 152077 * 172259 * 1067063 * 3682177 * 3815423 * 8867563 * 15880351)]
    [[8867563 < B1 < 15880351 < B2] -> [p53{M677} 发现于 第二阶段]]
实例二:
    [n := F15 = 1+2**2**15]
    [d := 253301772]
    [B1 :=  = 10**7]
    [B2 := 50*B1]
    [p33{F15} := 168768817029516972383024127016961]
    [len(EC{d;ZZ%p33{F15}}) == (2**5 * 3 * 1889 * 5701 * 9883 * 11777 * 5909317 * 91704181)]
    [[5909317 < B1 < 91704181 < B2] -> [p33{F15} 发现于 第二阶段]]

    [p27{F16} := 188981757975021318420037633]
        原文bug:F15因子33位188...633
        到底是F15还是F16?
        view others/数学/prime/Fermat_primes.txt
            F15= 1214251009 · 2327042503868417 · 168768817029516972383024127016961 · C
            F16= 825753601 · 188981757975021318420037633 · C


#]]]'''#'''
#elliptic pseudocurve
class Ops4EllipticPseudocurve:
    #vs:Ops4EllipticPseudocurve7DropY
    'ops4elliptic_pseudocurve #[Y**2 =[%n]= X**3+a*X+b][n :: uint{>=2}][gcd(n,6) == 1][a,b::int][gcd(n,(4*a**3+27*b**2)) == 1]'
    def __init__(sf, n, a, b, /):
        '-> None|^FoundNonTrivialFactor|^FoundTrivialFactor'
        check_int_ge(10, n)
        check_type_is(int, a)
        check_type_is(int, b)
        # [n >= 10]
        if not 1 == (g:=gcd(n, 6)):
            # !! [n >= 10]
            raise FoundNonTrivialFactor(n, g)
        hrem6N_ = mk_hrem_(n)
        a = hrem6N_(a)
        b = hrem6N_(b)
        if not 1 == (g:=gcd(n, discriminant:=(4*a**3+27*b**2))):
            ctx = (n, a, b)
            if 1 < g < n:
                raise FoundNonTrivialFactor(n, g, ctx)
            assert g == n, (n, g)
            raise FoundTrivialFactor(n, g, ctx)
        sf._hrem6N_ = hrem6N_
        sf._n = n
        sf._a = a
        sf._b = b
        sf._args = (n, a, b)
    @classmethod
    def mk_ex5n__7random_(cls, n, may_random_uint_mod_=None, /):
        '-> (ops4EPC, pt6EPC)|^FoundNonTrivialFactor'
        check_int_ge(10, n)
        # [n >= 10]
        if not 1 == (g:=gcd(n, 6)):
            # !! [n >= 10]
            raise FoundNonTrivialFactor(n, g)

        random_uint_mod_ = ifNone(may_random_uint_mod_, randrange)
        check_callable(random_uint_mod_)
        hrem6N_ = mk_hrem_(n)
        while 1:
            x = random_uint_mod_(n)
            y = random_uint_mod_(n)
            a = random_uint_mod_(n)
            yy = hrem6N_(y**2)
            xx = hrem6N_(x**2)
            xxx = hrem6N_(x*xx)
            ax = hrem6N_(x*a)
            b = hrem6N_(yy -xxx -ax)
            if not 1 == (g:=gcd(n, discriminant:=(4*a**3+27*b**2))):
                ctx = (n, a, b)
                if 1 < g < n:
                    raise FoundNonTrivialFactor(n, g, ctx)
                assert g == n, (n, g)
                continue
            break
        sf = cls(n, a, b)
            # no: ^FoundFactor
        pt = sf.mk_point_(x, y)
        return (sf, pt)
    @property
    def params4elliptic_pseudocurve(sf, /):
        '-> (n, a, b)'
        return sf._args
    def __repr__(sf, /):
        nab = (n, a, b) = sf._args
        return f'Ops4EllipticPseudocurve{nab}'
    def __eq__(sf, ot, /):
        if not isinstance(ot, __class__):return NotImplemented
        return sf is ot or sf._args == ot._args
    def mk_point_(sf, x, y, /):
        'int -> int -> pt'
        hrem6N_ = sf._hrem6N_
        x = hrem6N_(x)
        y = hrem6N_(y)
        pt = Pt4EC(x, y)
        return pt

    @property
    def zero(sf, /):
        return pt_O
    def eq_zero_(sf, pt, /):
        return pt is pt_O
    def eq_(sf, pt6lhs, pt6rhs, /):
        match (pt6lhs, pt6rhs):
            case (sf.zero, sf.zero):
                return True
            case (Pt4EC(), Pt4EC()):
                return pt6lhs == pt6rhs
        raise TypeError(type(pt6lhs), type(pt6rhs))
    def neg_(sf, pt, /):
        match pt:
            case sf.zero:
                return pt
            case Pt4EC(x=x, y=y):
                # !! hrem6N_ && [n :: odd]
                return Pt4EC(x, -y)
        raise TypeError(type(pt))
    def double_(sf, pt, /):
        return sf.add_(pt, pt)
    def sub_(sf, pt6lhs, pt6rhs, /):
        return sf.add_(pt6lhs, sf.neg_(pt6rhs))
    def add_(sf, pt6lhs, pt6rhs, /):
        match (pt6lhs, pt6rhs):
            case (sf.zero, pt):
                return pt
            case (pt, sf.zero):
                return pt
            case (Pt4EC(x=xL, y=yL), Pt4EC(x=xR, y=yR)):
                # (n, a, b) = sf._args
                a = sf._a
                hrem6N_ = sf._hrem6N_
                # [[Q =!= -P] -> [P+Q == R] -> [slope:=if P.x == Q.x then (3*P.x**2+2*C*P.x+A)/(2*P.y) else (P.y-Q.y)/(P.x-Q.x)] -> [R.x==slope**2-C-P.x-Q.x][R.y==-(P.y+slope*(R.x-P.x))]]
                if xL == xR:
                    if yL == -yR:
                        # [pt6lhs == -pt6rhs]
                        return sf.zero
                    #assert yL == yR, (sf, pt6lhs, pt6rhs)
                    if not yL == yR:
                        ctx = (sf, pt6lhs, pt6rhs)
                        n = sf._n
                        ft = gcd(n, yL-yR)
                        if 1 < ft < n:
                            raise FoundNonTrivialFactor(n, ft, ctx)
                        assert ft == n, (n, ft)
                        raise ValueError('non-std point:should use .mk_point_():', ctx)
                    # [pt6lhs == pt6rhs]
                    # double_()
                    # !! [C==0]
                    slope = hrem6N_(hrem6N_(3*xL**2 +a) *sf.inv6N_(yL<<1))
                else:
                    slope = hrem6N_((yL-yR)*sf.inv6N_(xL-xR))
                slope
                # !! [C==0]
                _x = hrem6N_(slope**2 -(xL+xR))
                _y = hrem6N_(-(yL+slope*(_x-xL)))
                pt = sf.mk_point_(_x, _y)
                return pt
        raise TypeError(type(pt6lhs), type(pt6rhs))
    def inv6N_(sf, x, /):
        n = sf._n
        try:
            r = inv_mod__py_(n, x)
        except ValueError:
            ctx = (sf, x)
            ft = gcd(n, x)
            if 1 < ft < n:
                raise FoundNonTrivialFactor(n, ft, ctx)
            assert ft == n, (n, ft)
            raise FoundTrivialFactor(n, ft, ctx)
        hrem6N_ = sf._hrem6N_
        return hrem6N_(r)
    def mul_(sf, k, pt, /):
        out = sf.zero
        if k < 0:
            ot = sf.neg_(pt)
            k = -k
        for b in map(int, f'{k:b}'):
            out = sf.double_(out)
            if b:
                out = sf.add_(out, pt)
        return out

#end-class Ops4EllipticPseudocurve:

# [:define__addh]:goto
# [:define__doubleh]:goto
# [:define__mulh]:goto
# [:define__ECM7inversionless]:goto
# [examples__ECM]:goto
class Ops4EllipticPseudocurve7DropY:
    #vs:Ops4EllipticPseudocurve
    #
    # 7Montgomery --> 7DropY
    # inversionless
    'ops4elliptic_pseudocurve7drop_Y # [g*Y**2*Z =[%n]= X**3+C*X**2*Z+X*Z**2][n :: uint{>=2}][gcd(n,6) == 1][C::pseudo-Fraction%n][gcd(n,(4-C**2)) == 1][C==pseudo-Fraction(N4C, D4C)]'
    def __init__(sf, n, N4C, D4C, /, *, strict=True, detect6Incapable=False):
        '-> None|^FoundNonTrivialFactor|^FoundTrivialFactor|^ParamError__ops4EPC7DropY'
        strict = bool(strict)
        detect6Incapable = bool(detect6Incapable)
        check_int_ge(10, n)
        #check_type_is(int, C)
        check_type_is(int, N4C)
        check_type_is(int, D4C)
        # [n >= 10]
        if not 1 == (g:=gcd(n, 6)):
            # !! [n >= 10]
            raise FoundNonTrivialFactor(n, g)
        # [gcd(n,6) == 1]
        hrem6N_ = mk_hrem_(n)
        ##################
        N4C = hrem6N_(N4C)
        D4C = hrem6N_(D4C)
        ctx = (n, N4C, D4C)
        # !! required:[gcd(n,(4-C**2)) == 1]
        # forbid: [C =[%n]= +/-2]
        # <==>:
        # forbid: [N4C =[%n]= +/-2*D4C]
        # forbid: [D4C =[%n]= 0]
        if D4C == 0:raise ParamError__ops4EPC7DropY('[C == +/-oo]', ctx)
        zD4C = hrem6N_(2*D4C)
        if N4C == zD4C:raise ParamError__ops4EPC7DropY('[C =[%n]= +2]', ctx)
        if N4C == hrem6N_(-zD4C):raise ParamError__ops4EPC7DropY('[C =[%n]= -2]', ctx)
        # [D4C%n =!= 0]
        # [not$[N4C =[%n]= +2*D4C]]
        # [not$[N4C =[%n]= -2*D4C]]
        # ==>>:
        # [not$[C =[%n]= +/-2]]

        # !! required:[gcd(n,(4-C**2)) == 1]
        # required:[gcd(n,D4C*(4*D4C**2-N4C**2)) == 1]
        us = [D4C, hrem6N_(zD4C+N4C), hrem6N_(zD4C-N4C)]
        assert all(us)
        IIus = II_mod(n, us)
        if strict:
            g = gcd(n, IIus)
        else:
            g = 1 if IIus else n
        g
        if g == n:
            for u in us:
                g = gcd(n, u)
                if 1 < g < n:
                    break
            else:
                raise Exception(ctx)
            g
            assert 1 < g < n
        g
        if 1 < g < n:
            raise FoundNonTrivialFactor(n, g, ctx)
        assert 1 == g, ctx
        # strict => [gcd(n,D4C*(4*D4C**2-N4C**2)) == 1]
        # strict => [gcd(n,(4-C**2)) == 1]
        # [0 =!= D4C*(4*D4C**2-N4C**2) %n]


        sf._hrem6N_ = hrem6N_
        sf._n = n
        sf._N4C = N4C
        sf._D4C = D4C
        sf._args = (n, N4C, D4C)
        sf._strict = strict
        sf._detect6Incapable = detect6Incapable
        return

        ##################
        C = hrem6N_(C)
        if not 1 == (g:=gcd(n, discriminant:=(4-C**2))):
            ctx = (n, C)
            if 1 < g < n:
                raise FoundNonTrivialFactor(n, g, ctx)
            assert g == n, (n, g)
            # !! [n >= 10]
            # !! [C := hrem6N_(C)]
            if not abs(C) == 2:
                ft = gcd(n, C+2)
                if 1 < ft < n:
                    raise FoundNonTrivialFactor(n, ft, ctx)
                raise Exception(ctx)
            # [abs(C) == 2]
            raise FoundTrivialFactor(n, g, ctx)
        sf._hrem6N_ = hrem6N_
        sf._n = n
        sf._C = C
        sf._args = (n, C)
    @classmethod
    def mk_ex5n__7random_(cls, n, may_random_uint_mod_=None, /, *, strict=True, detect6Incapable=False, _d6strict=None):
        '-> (ops4EPC, pt6EPC)|^FoundNonTrivialFactor'
        strict = bool(strict)
        detect6Incapable = bool(detect6Incapable)
        check_int_ge(10, n)
        # [n >= 10]
        if not 1 == (g:=gcd(n, 6)):
            # !! [n >= 10]
            raise FoundNonTrivialFactor(n, g)
        # [gcd(n,6) == 1]

        random_uint_mod_ = ifNone(may_random_uint_mod_, randrange)
        check_callable(random_uint_mod_)
        hrem6N_ = mk_hrem_(n)
        b_init = True
        while strict:
            if not _d6strict is None:
                if b_init:
                    b_init = False
                else:
                    raise Exception(n, _d6strict)
                d = hrem6N_(_d6strict)
            else:
                d = 6+random_uint_mod_(-6+n) # randrange(6, n)
            d
            u = hrem6N_(d**2-5)
            v = hrem6N_(4*d)

            # [d:=6][n:=31] => [u==0]
            # [d:=29][n:=11*19=209] => [u==0]
            if u == 0:continue
            if v == 0:raise 000
            # [u%n =!= 0]
            # [v%n =!= 0]

            ctx = (n, None, d, u, v)
            (u3, v3) = (pow(u,3,n), pow(v,3,n))

            if u3 == 0:
                ft = gcd(n, u)
            elif v3 == 0:
                ft = gcd(n, v)
            else:
                ft = 0
            if ft:
                if 1 < ft < n:
                    raise FoundNonTrivialFactor(n, ft, ctx)
                raise Exception(ctx)
            # [u**3%n =!= 0]
            # [v**3%n =!= 0]
            # [u%n =!= 0]
            # [v%n =!= 0]

            # C = Fraction(((v-u)**3 * (v+3*u) -2*(4*v*u**3))%n, (4*v*u**3) %n)
            D4C = hrem6N_(4*v*u3)
            if D4C == 0:
                # !! [u**3%n =!= 0]
                # !! [v%n =!= 0]
                # !! [gcd(n,6) == 1]
                ft = gcd(n, v)
                if 1 < ft < n:
                    raise FoundNonTrivialFactor(n, ft, ctx)
                raise Exception(ctx)
            D4C
            # [D4C%n =!= 0]

            part4N4C = hrem6N_(pow(v-u,3,n) * (v+3*u))
            if part4N4C == 0:
                # !! [N4C =[%n]= (part4N4C -2*D4C)]
                # [N4C =[%n]= (-2*D4C)]
                # [C =[%n]= -2]
                # forbid
                continue
            part4N4C
            # [part4N4C%n =!= 0]
            zD4C = hrem6N_(2*D4C)
            N4C = hrem6N_(part4N4C -zD4C)
            # !! [part4N4C%n =!= 0]
            # [not$[N4C =[%n]= -2*D4C]]
            if N4C == zD4C:continue
            # [not$[N4C =[%n]= +2*D4C]]
            # [not$[N4C =[%n]= -2*D4C]]
            # [D4C%n =!= 0]
            # ==>>:
            # [not$[C =[%n]= +/-2]]

            if D4C == 0:raise 000
            if N4C == zD4C:raise 000
            if N4C == hrem6N_(-zD4C):raise 000

            # C = Fraction(N4C%n, D4C %n)
            X0, Z0 = XZ4pt_0 = (u3, v3)

            # !! [u**3%n =!= 0]
            # !! [v**3%n =!= 0]
            # [X0%n =!= 0]
            # [Z0%n =!= 0]
            # [pt_0 =!= O]

            # [g?*y**2 == x**3 +C*x**2 +x]
            # [g*Y**2*Z =[%n]= X**3+C*X**2*Z+X*Z**2]
            # !! [g? unknown]
            # !! [Y0 unknown]
            # no test:__contains__

            # [Y0 := 1 %n]
            # [g? := Z0**-1 * (X0**3 + C*X0**2*Z0 +X0*Z0**2) %n]

 
            break
        # strict => n, N4C, D4C, X0, Z0
        while not strict:
            # !! [g? can be square_nonresidual]
            # => [x0 can be arbitrary nonzero]
            x0 = 1+random_uint_mod_(-1+n) # randrange(1, n)
            # !! [(4-C**2)%n =!= 0]
            C = 3+random_uint_mod_(-5+n) # randrange(3, -2+n)
            N4C, D4C = C, 1
            X0, Z0 = x0, 1
            break
        n, N4C, D4C, X0, Z0
        sf = cls(n, N4C, D4C, strict=strict, detect6Incapable=detect6Incapable)
            # no: ^ParamError__ops4EPC7DropY
            # no: ^FoundTrivialFactor
            # ^FoundNonTrivialFactor
            # n
        pt_0 = sf.mk_point_(X0, Z0)
        return (sf, pt_0)
    @property
    def params4elliptic_pseudocurve7drop_Y(sf, /):
        '-> (n, N4C, D4C)'
        return sf._args
    def __repr__(sf, /):
        args = (n, N4C, D4C) = sf._args
        strict = sf._strict
        detect6Incapable = sf._detect6Incapable
        #bug:kwds = dict(strict=strict) if strict else {}
        #kwds = dict(strict=strict) if not strict else {}
        kwds = {}
        if not strict:
            kwds.update(strict=strict)
        if detect6Incapable:
            kwds.update(detect6Incapable=detect6Incapable)
        return repr_helper(sf, *args, **kwds)
        return f'Ops4EllipticPseudocurve7DropY{args}'
    def __eq__(sf, ot, /):
        if not isinstance(ot, __class__):return NotImplemented
        return sf is ot or sf._args == ot._args
    def mk_point_(sf, X, Z, /):
        'int -> int -> pt'
        hrem6N_ = sf._hrem6N_
        Z = hrem6N_(Z)
        X = hrem6N_(X) if Z else 0
        pt = Pt4EC7h(X, Z)
        return pt

    @property
    def zero(sf, /):
        return pt7h_O
    def eq_zero_(sf, pt, /):
        return pt.eq_zero_()
    def eq_(sf, pt6lhs, pt6rhs, /):
        match (pt6lhs, pt6rhs):
            case (Pt4EC7h(), Pt4EC7h()):
                return pt6lhs == pt6rhs
        raise TypeError(type(pt6lhs), type(pt6rhs))
    def neg_(sf, pt, /):
        # !! 7DropY
        # [pt =[repr]= -pt]
        return pt
    def sub7h_(sf, pt6lhs, pt6rhs, pt7sum, /):
        '[pt7sum == pt6lhs <+> pt6rhs] => pt6lhs/Pt4EC7h -> pt6rhs/Pt4EC7h -> pt7sum/Pt4EC7h -> (pt6lhs<+>-pt6rhs)/Pt4EC7h|^Incapable__add7h__X6diff_eq0|^FoundNonTrivialFactor if detect6Incapable'
        # [pt7sum == pt6lhs - (-pt6rhs)] => pt6lhs -> pt6rhs -> pt7sum -> (pt6lhs+(-pt6rhs))|^Incapable__add7h__X6diff_eq0|^FoundNonTrivialFactor if detect6Incapable
        return sf.add7h_(pt6lhs, sf.neg_(pt6rhs), pt7sum)
    def add7h_(sf, pt6lhs, pt6rhs, pt7diff, /):
        '[pt7diff == pt6lhs <+> -pt6rhs] => pt6lhs/Pt4EC7h -> pt6rhs/Pt4EC7h -> pt7diff/Pt4EC7h -> (pt6lhs<+>pt6rhs)/Pt4EC7h|^Incapable__add7h__X6diff_eq0|^FoundNonTrivialFactor if detect6Incapable'
        # precondition:[pt7diff == pt6lhs - pt6rhs]
        ctx = (n, N4C, D4C) = sf._args
        if pt7diff.eq_zero_():
            # [0 == pt7diff.Z]
            #assert pt6lhs.eq7h7mod_(n, pt6rhs)
            return sf.double7h_(pt6lhs)
        # [0 =!= pt7diff.Z]
        # [pt7diff =!= O]
        # !! [pt7diff == pt6lhs - pt6rhs]
        # [pt6lhs =!= +pt6rhs]

        if pt6lhs.eq_zero_():
            #assert pt6rhs.eq7h7mod_(n, pt7diff) # == -pt7diff
            return pt6rhs
        # [pt6lhs =!= O]

        if pt6rhs.eq_zero_():
            #assert pt6lhs.eq7h7mod_(n, pt7diff) # == +pt7diff
            return pt6lhs
        # [pt6rhs =!= O]

        # [pt6lhs =!= +pt6rhs]
        if pt6lhs.eq7h7mod_(n, pt6rhs):
            # [pt6lhs =[repr:ratio]= pt6rhs]
            # [pt6lhs == +/-pt6rhs]
            # !! [pt6lhs =!= +pt6rhs]
            # [pt6lhs == -pt6rhs]
            # [pt6lhs +pt6rhs == O]
            return pt7h_O
        # [pt6lhs =!= +/-pt6rhs]

        # [0 =!= pt7diff.Z]
        # [pt7diff =!= O]
        # [pt6lhs =!= O]
        # [pt6rhs =!= O]
        # [pt6lhs =!= +/-pt6rhs]

        if 0 == pt7diff.X:
            # [0 == pt7diff.X]
            # [0 =!= pt7diff.Z]
            if sf._detect6Incapable:
                ft = gcd(n, pt7diff.Z)
                if 1 < ft < n:
                    raise FoundNonTrivialFactor(n, ft, ctx)
            if 0 == pt7diff.X: raise Incapable__add7h__X6diff_eq0(ctx, (pt6lhs, pt6rhs, pt7diff))
            raise 000
        # [0 =!= pt7diff.X]

        # [:define__addh]:goto
        # setup:precondition:[P1=!=O][P2=!=O][P1=!=-P2][P1=!=+P2][Xn =!= 0]
        (X1, Z1) = P1 = pt6lhs
        (X2, Z2) = P2 = pt6rhs
        (Xn, Zn) = pt7diff
        # [Xn =!= 0]
        # [Zn =!= 0]

        # !! [B:=0][A:=1]
        if 0:
            Xp = (Zn * pow((X1*X2 -Z1*Z2) %n, 2, n)) %n
            Zp = (Xn * pow((X1*Z2 -X2*Z1) %n, 2, n)) %n
        else:
            xxzz = (X1*X2 -Z1*Z2) %n
            #xzxz = (X1*Z2 -X2*Z1) %n
            xzxz = ((X1-Z1)*(X2+Z2) -xxzz) %n
            Xp = (Zn * pow(xxzz, 2, n)) %n
            Zp = (Xn * pow(xzxz, 2, n)) %n
        return sf.mk_point_(Xp, Zp)
    def double7h_(sf, pt, /):
        'pt/Pt4EC7h -> (pt<+>pt)/Pt4EC7h'
        if pt.eq_zero_():
            return pt7h_O
        # [pt =!= O]
        ctx = (n, N4C, D4C) = sf._args

        # [:define__doubleh]:goto
        # setup:precondition:[P1=!=O][P2=!=O][P1=?=-P2][P1==+P2]:
        (X1, Z1) = P1 = P2 = pt
        # [P1 =!= O]
        # [Z1 =!= 0]
        X1X1 = pow(X1, 2, n)
        Z1Z1 = pow(Z1, 2, n)


        # [0 =?= (X1**3 +C*X1**2*Z1 +A*X1*Z1**2 +B*Z1**3)]
        # !! [B:=0][A:=1]
        # part4Zp = ((X1 +C*Z1)%n *X1X1 +X1*Z1Z1) %n
        # Zp = part4Zp*Z1*4 %n if part4Zp else 0
        # Xp = pow(X1X1 -Z1Z1, 2, n) if Zp else 0
        D4C_X1= D4C*X1 %n
        D4C_part4Zp = ((D4C_X1 +N4C*Z1)%n *X1X1 +D4C_X1*Z1Z1) %n
        Zp = D4C_part4Zp*Z1*4 %n if D4C_part4Zp else 0
        Xp = D4C*pow(X1X1 -Z1Z1, 2, n) %n if Zp else 0
        return sf.mk_point_(Xp, Zp)

    def mul7h_(sf, k, pt, /, *, _old_ver=False):
        # vs:_old_ver__mul7h_
        # vs:bi_mul7h_
        'k/int -> pt/Pt4EC7h -> (k<*>pt)/Pt4EC7h|^Incapable__add7h__X6diff_eq0|^FoundNonTrivialFactor if detect6Incapable'
        if _old_ver:
            return sf._old_ver__mul7h_(k, pt)

        # [:define__mulh]:goto
        check_type_is(int, k)
        # !! [pt =[repr]= -pt]
        k = abs(k)
        # [k >= 0]
        if 0 == k:
            return pt7h_O
        # [k >= 1]
        # if 1 == k.bit_count():
        (ez4k, odd4k) = factor_pint_out_power_of_base_(2, k)
        777;k = None
        if odd4k == 1:
            pt7O = pt
        else:
            # (pt7O, pt7OaddI) = sf.bi_mul7h_(odd4k, pt)
            pt7O = sf.bi_mul7h_(odd4k, pt, only1=True)
        pt7O
        for _ in range(ez4k):
            pt7O = sf.double7h_(pt7O)
        return pt7O

    def bi_mul7h_(sf, k, pt, /, *, only1=False):
        # vs:_old_ver__mul7h_
        # vs:mul7h_
        'k/int -> pt/Pt4EC7h -> (k<*>pt, (k+1)<*>pt)/(Pt4EC7h,Pt4EC7h)|^Incapable__add7h__X6diff_eq0|^FoundNonTrivialFactor if detect6Incapable'
        # [:define__mulh]:goto
        only1 = bool(only1)
        check_type_is(int, k)
        # !! [pt =[repr]= -pt]
        k = abs(k)
        # [k >= 0]

        # !! [pt =[repr]= -pt]
        #neg_pt7I = pt # ~= -pt
        pt7I = pt

        _k = 0
        pt7O = pt7h_O
        pt7OaddI = pt7I if k or not only1 else None
        # [pt7O == _k<*>pt7I]
        # [pt7OaddI == (1+_k)<*>pt7I]

        sbits = f'{k:b}'
        L = len(sbits)
        for not_last, b in enumerate(map(int, sbits), 1-L):
            # [pt7O == _k<*>pt7I]
            # [pt7OaddI == (1+_k)<*>pt7I]
            # [b <- {0,1}]
            if b == 1:
                # [b == 1]
                pt7O = sf.add7h_(pt7OaddI, pt7O, pt7I)
                pt7OaddI = sf.double7h_(pt7OaddI) if not_last or not only1 else None
                # [pt7O == (1+2*_k)<*>pt7I]
                # [pt7OaddI == (2+2*_k)<*>pt7I]
            else:
                # [b == 0]
                pt7OaddI = sf.add7h_(pt7OaddI, pt7O, pt7I) if not_last or not only1 else None
                pt7O = sf.double7h_(pt7O)
                # [pt7O == (0+2*_k)<*>pt7I]
                # [pt7OaddI == (1+2*_k)<*>pt7I]
            # [pt7O == (b+2*_k)<*>pt7I]
            # [pt7OaddI == (1+b+2*_k)<*>pt7I]
            _k = b+2*_k
            # [pt7O == _k<*>pt7I]
            # [pt7OaddI == (1+_k)<*>pt7I]
        # [pt7O == _k<*>pt7I]
        # [pt7OaddI == (1+_k)<*>pt7I]
        _k, pt7O, pt7OaddI
        assert _k == k
        # [_k == k]
        # [pt7O == k<*>pt7I]
        # [pt7OaddI == (1+k)<*>pt7I]
        assert only1 is (pt7OaddI is None)
        both = (pt7O, pt7OaddI)
        return both if not only1 else pt7O

    def _old_ver__mul7h_(sf, k, pt, /):
        # vs:mul7h_
        # vs:bi_mul7h_
        'k/int -> pt/Pt4EC7h -> (k<*>pt)/Pt4EC7h|^Incapable__add7h__X6diff_eq0|^FoundNonTrivialFactor if detect6Incapable'
        # [:define__mulh]:goto
        check_type_is(int, k)
        # !! [pt =[repr]= -pt]
        k = abs(k)
        # [k >= 0]
        match k:
            case 0:
                return pt7h_O
            case 1:
                return pt
            case 2:
                return sf.double7h_(pt)
        k
        # [k >= 3]
        sbits = f'{k:b}'
        assert sbits[0] == '1'
        pt7I = pt
        pt7O = pt7I
        pt7OaddI = sf.double7h_(pt7I)
        # [pt7OaddI == pt7O +pt7I]
        # [pt7O == 1<*>pt7I]

        # [k_{j} =[def]= int(sbits[:j],2)]
        # [pt7O == k_{1}<*>pt7I]
        j = 0
        # [pt7O == k_{1+j}<*>pt7I]
        # [pt7OaddI == pt7O +pt7I == (1+k_{1+j})<*>pt7I]
        for j, sbit in enumerate(sbits[1:], 1+j):
            # [pt7O == k_{j}<*>pt7I]
            # [pt7OaddI == pt7O +pt7I == (1+k_{j})<*>pt7I]
            if sbit == '1':
                # [k_{1+j} == 1+2*k_{j}]
                pt7O = sf.add7h_(pt7OaddI, pt7O, pt7I)
                    # ^Incapable__add7h__X6diff_eq0
                    # ^FoundNonTrivialFactor
                pt7OaddI = sf.double7h_(pt7OaddI)
                # [pt7O == k_{1+j}<*>pt7I]
                # [pt7OaddI == pt7O +pt7I == (1+k_{1+j})<*>pt7I]
            else:
                # [k_{1+j} == 0+2*k_{j}]
                pt7OaddI = sf.add7h_(pt7OaddI, pt7O, pt7I)
                    # ^Incapable__add7h__X6diff_eq0
                    # ^FoundNonTrivialFactor
                pt7O = sf.double7h_(pt7O)
                # [pt7O == k_{1+j}<*>pt7I]
                # [pt7OaddI == pt7O +pt7I == (1+k_{1+j})<*>pt7I]
            # [pt7O == k_{1+j}<*>pt7I]
            # [pt7OaddI == pt7O +pt7I == (1+k_{1+j})<*>pt7I]
        # [pt7O == k_{1+j}<*>pt7I]
        # [pt7OaddI == pt7O +pt7I == (1+k_{1+j})<*>pt7I]
        assert 1+j == len(sbits)
        # [1+j == len(sbits)]
        # [k_{1+j} == k]
        # [pt7O == k<*>pt7I]
        # [pt7OaddI == pt7O +pt7I == (1+k)<*>pt7I]
        return pt7O

#end-class Ops4EllipticPseudocurve7DropY:
def iter_prepare4Ops4EllipticPseudocurve7DropY_(n, /, *args, **kwds):
    f = lambda:Ops4EllipticPseudocurve7DropY.mk_ex5n__7random_(n, *args, **kwds)
    while 1:
        try:
            r = f()
        except FoundFactor as exc:
            yield exc
            continue
        else:
            yield r
            return
            break








def default__ks5n_and_B_(n, B, /):
    ps = iter_primes__ge_lt_(2, 1+B)
    for p in ps:
        ep = floor_log_(p, B)
        yield from repeat(p, ep)
def default__ks5n_and_B_or_ks_(n, B_or_ks, /):
    match B_or_ks:
        case int() as B:
            check_int_ge(2, B)
            ks = default__ks5n_and_B_(n, B)
            ks = iter(ks)
        case ks:
            ks = iter(ks)
        #case _: raise TypeError(type(B_or_ks))
    return ks
def ex1_try_factor_pint__elliptic_curve_method_(n, B1, /, *, random_uint_mod_=None, settings4EPC=None):
    'n/uint{>=1} -> B1/uint{>=2} -> may (ft/non_trivial_factor{n}, settings4EPC{n}, B1) # [B1 is smooth bound] # [settings4EPC == (args4EPC, xy6EPC) :: ((n,a,b),(x,y))]'
    check_int_ge(1, n)
    check_int_ge(2, B1)
    m = try_factor_pint__elliptic_curve_method_(n, Bs_or_kss:=[B1], random_uint_mod_=random_uint_mod_, with_ctx=True, settings4EPC=settings4EPC)
    match m:
        case None:
            return None
        case (ft, ((j4ks, B_or_ks), (j4k, k), (ops4EPC, pt), ctx6exc) as ctx):
            assert j4ks == 0
            assert B_or_ks is B1
            (_n, a, b) = ops4EPC.params4elliptic_pseudocurve
            assert _n == n
            args4EPC = (n, a, b)
            (x, y) = pt # Pt4EC
            xy6EPC = (x, y)
            settings4EPC = (args4EPC, xy6EPC)
            return (ft, settings4EPC, B1)

def try_factor_pint__elliptic_curve_method_(n, Bs_or_kss=None, ks5n_and_B_or_ks_=None, /, *, random_uint_mod_=None, with_ctx=False, result6fail=None, settings4EPC=None):
    #this is old_version:only B1
    #   #new_version:both B1,B2:try1_factor_pint__elliptic_curve_method_:goto
    'n/uint{>=1} -> Iter (B/uint{>=2}|ks/(Iter k/uint{>=2})) -> may (n -> (B|ks) -> ks) -> may non_trivial_factor{n} # [ks are multiplier => II(ks)*pt] # [B is smooth bound => ks:=chains(repeat(p,floor_log_(p,B)) for p in primes_lt(1+B))] # [[p::prime][n%p==0][1==gcd(n,[1..<p])] -> [best:B1:=exp((1/sqrt2+o(1))*sqrt(ln(p)*lnln(p)))]]'
    check_int_ge(1, n)
    if n < 4:
        return result6fail#None
    if n&1 == 0:
        return 2
    if n%3 == 0:
        return 3
    # [1 == gcd(n, 6)]
    (rt, e) = factor_pint_as_perfect_power_(n)
    if 1 < rt < n:
        return rt
    # [not$is_perfect_power_(n)]
    # [1 == gcd(n, 6)]

    # [n::prime]or[n>=35]
    if n < 35:
        return result6fail#None
    # [n >= 35]

    Bs_or_kss = ifNone(Bs_or_kss, [1_00_00])
    ks5n_and_B_or_ks_ = ifNone(ks5n_and_B_or_ks_, default__ks5n_and_B_or_ks_)
    check_callable(ks5n_and_B_or_ks_)
    random_uint_mod_ = ifNone(random_uint_mod_, randrange)
    check_callable(random_uint_mod_)

    if not None is settings4EPC:
        (args4EPC, xy6EPC) = settings4EPC
        g_ops4EPC = Ops4EllipticPseudocurve(*args4EPC)
        g_pt6EPC = g_ops4EPC.mk_point_(*xy6EPC)

    try:
        #########
        #for:ctx:
        (j4ks, B_or_ks) = (-1, None)
        (j4k, k) = (-1, None)
        (ops4EPC, pt) = (None, pt_O)
        #########
        for (j4ks, B_or_ks) in enumerate(Bs_or_kss):
            ks = ks5n_and_B_or_ks_(n, B_or_ks)
            (ops4EPC, pt) = Ops4EllipticPseudocurve.mk_ex5n__7random_(n, random_uint_mod_) if None is settings4EPC else (g_ops4EPC, g_pt6EPC)
                # ^FoundNonTrivialFactor
            _pt = pt
            mul_ = ops4EPC.mul_
            for (j4k, k) in enumerate(ks):
                try:
                    _pt = mul_(k, _pt)
                except FoundTrivialFactor:
                    'from:inv6N_()'
                    break
            #########
            #for:ctx:
            (j4k, k) = (-1, None)
            (ops4EPC, pt) = (None, pt_O)
            #########
    except FoundNonTrivialFactor as exc:
        if not exc.N == n:
            raise
        ft = exc.factor
        ctx = ((j4ks, B_or_ks), (j4k, k), (ops4EPC, pt), exc.ctx)
        return ft if not with_ctx else (ft, ctx)
    return result6fail#None



















def _xs5or_B_(xs_or_B, may__xs5B_, default__xs5B_, /, *extra_args):
    match xs_or_B:
        case int() as B:
            xs5B_ = ifNone(may__xs5B_, default__xs5B_)
            xs = xs5B_(*extra_args, B)
        case xs:
            pass
    iter(xs)#check iterable
    return xs
def default__dup_exps_from_B1_(B1, /):
    ps = iter_primes__ge_lt_(2, 1+B1)
    for p in ps:
        ep = floor_log_(p, B1)
        yield from repeat(p, ep)
def default__delta_exps_from_B1_B2_(B1, B2, /):
    ps = iter_primes__ge_lt_(1+B1, 1+B2)
    _p = 0
    for p in ps:
        yield p - _p
        _p = p

def prepare4factor_pint__elliptic_curve_method_(n_or_settings4EPC, /, *, random_uint_mod_=None, result6fail=None, drop_Y=False, to_raise=False, **kwds4mk):
    '-> ((-1, result6fail, may_exc)|(+1, non_trivial_factor, may_exc)|(0, (n{[1 == gcd(n, 6)][n >= 25]}, settings4EPC, (ops4EPC/T, pt)))) | ^FoundFactor if to_raise | ^ParamError__ops4EPC7DropY if to_raise and drop_Y # [T := Ops4EllipticPseudocurve if not drop_Y else Ops4EllipticPseudocurve7DropY]'
    #'-> ((True, (result6fail|non_trivial_factor))|(False, (n{[1 == gcd(n, 6)][n >= 25]}, settings4EPC, (ops4EPC/T, pt)))) | ^FoundFactor | ^ParamError__ops4EPC7DropY if drop_Y # [T := Ops4EllipticPseudocurve if not drop_Y else Ops4EllipticPseudocurve7DropY]'
    match n_or_settings4EPC:
        case int() as n:
            may_settings4EPC = None
            pass
        case ((int() as n, int(), int()) as args4EPC, (int(), int()) as xx6EPC) as settings4EPC:
            # (n,a,b)|(n,N4C,D4C)
            # (x,y)|(X,Z)
            # xy6EPC|XZ6EPC
            may_settings4EPC = settings4EPC
            pass
        case _:
            raise TypeError(n_or_settings4EPC)
    may_settings4EPC
    n
    check_int_ge(1, n)
    # [n >= 1]
    if n < 4:
        # [n :: prime]or[n==1]
        return (-1, result6fail, None)
    if n&1 == 0:
        return (+1, 2, None)
    if n%3 == 0:
        return (+1, 3, None)
    # [1 == gcd(n, 6)]
    if n < 25:
        # [n :: prime]
        return (-1, result6fail, None)
    # [n >= 25]
    # [1 == gcd(n, 6)]

    T = Ops4EllipticPseudocurve if not drop_Y else Ops4EllipticPseudocurve7DropY
    try:
        if not None is may_settings4EPC:
            # (args4EPC, xx6EPC) = settings4EPC
            settings4EPC
            (args4EPC, xx6EPC)
            ops4EPC = T(*args4EPC, **kwds4mk)
                # ^FoundTrivialFactor
                # ^FoundNonTrivialFactor
                # ^ParamError__ops4EPC7DropY
            pt6EPC = ops4EPC.mk_point_(*xx6EPC)
        else:
            (ops4EPC, pt6EPC) = T.mk_ex5n__7random_(n, random_uint_mod_, **kwds4mk)
                # ^FoundNonTrivialFactor

            args4EPC = ops4EPC.params4elliptic_pseudocurve if not drop_Y else ops4EPC.params4elliptic_pseudocurve7drop_Y
            xx6EPC = tuple(pt6EPC)
            settings4EPC = (args4EPC, xx6EPC)
        (args4EPC, xx6EPC)
        settings4EPC
        (ops4EPC, pt6EPC)
    except FoundNonTrivialFactor as exc:
        if not exc.N == n:
            if to_raise: raise
            return (-1, result6fail, exc)
            raise
        ft = exc.factor
        return (+1, ft, exc)
    except (FoundTrivialFactor, ParamError__ops4EPC7DropY) as exc:
        if to_raise: raise
        return (-1, result6fail, exc)
    (args4EPC, xx6EPC)
    settings4EPC
    (ops4EPC, pt6EPC)
    assert not None is settings4EPC

    # [n >= 25]
    # [1 == gcd(n, 6)]
    return (0, (n, settings4EPC, (ops4EPC, pt6EPC)))


def try1_factor_pint__elliptic_curve_method_(n_or_settings4EPC, B1_or_dup_exps4stage1, B2_or_delta_exps4stage2, /, *, random_uint_mod_=None, result6fail=None, dup_exps_from_B1_=None, delta_exps_from_B1_B2_=None):
    '-> (((result6fail|ft), may_exc_or_ctx) | (ft, settings4EPC, stage, ((j4exp, zmay_q1{==max_exp6stage1}) if stage==1 else (max_exp6stage1, j4delta, zmay_q2{==max_exp6stage2}))))'
    #TODO:++kw:drop_Y/inversionless#Ops4EllipticPseudocurve7DropY
    #vs:try1_factor_pint__elliptic_curve_method7inversionless_
    ###########################
    match prepare4factor_pint__elliptic_curve_method_(n_or_settings4EPC, random_uint_mod_=random_uint_mod_, result6fail=result6fail, drop_Y=False):
        case (-1, _, may_exc):
            return (result6fail, may_exc)
        #case (+1, ft):
        case (1, ft, may_exc):
            return (ft, may_exc)
        case (0, (n, settings4EPC, (ops4EPC, pt6EPC))):
            pass
        case _:
            raise 000
    (n, settings4EPC, (ops4EPC, pt6EPC))
    # [1 == gcd(n, 6)]
    ###########################
    ctx = (n, settings4EPC, (ops4EPC, pt6EPC))
    ###########################

    B1 = None
    pt0 = pt6EPC
    zmay_q1 = 0
    zmay_q2 = 0
    try:
        #########
        mul_ = ops4EPC.mul_
        dup_exps4stage1 = _xs5or_B_(B1_or_dup_exps4stage1, dup_exps_from_B1_, default__dup_exps_from_B1_)
        stage = 1
        max_exp6stage1 = 0 # zmay_q1
        j4exp = -1
        _pt = pt0
        for (j4exp, exp) in enumerate(dup_exps4stage1, 1+j4exp):
            assert exp > 0
            max_exp6stage1 = max(max_exp6stage1, abs(exp))
            _pt = mul_(exp, _pt)
                # ^FoundTrivialFactor
                # ^FoundNonTrivialFactor
        j4exp
        max_exp6stage1
        _pt
        #########
        zmay_q1 = max_exp6stage1
        imay_j4exp6stage1 = j4exp
        B1 = max_exp6stage1
        pt1 = _pt
        cache = {}
        max4delta6cache = 10+3*n.bit_length()

        add_ = ops4EPC.add_
        delta_exps4stage2 = _xs5or_B_(B2_or_delta_exps4stage2, delta_exps_from_B1_B2_, default__delta_exps_from_B1_B2_, B1)
        stage = 2
        max_exp6stage2 = 0 # zmay_q2
        _pt = pt1
        #for (j4exp, delta) in enumerate(delta_exps4stage2, 1+j4exp):
        j4delta = -1
        for (j4delta, delta) in enumerate(delta_exps4stage2, 1+j4delta):
            assert delta > 0
            max_exp6stage2 += delta
            _pt = add_(_pt, _cached_mul_(max4delta6cache, cache, mul_, delta, pt1))
                # ^FoundTrivialFactor
                # ^FoundNonTrivialFactor
        j4delta
        max_exp6stage2
        _pt
        #########
        zmay_q2 = max_exp6stage2
        imay_j4exp6stage2 = j4delta
        B2 = max_exp6stage2
        pt2 = _pt
    except FoundTrivialFactor as exc:
        if not exc.N == n:
            raise
        'from:inv6N_()'
        stage
        j4exp
        return (result6fail, exc)
    except FoundNonTrivialFactor as exc:
        if not exc.N == n:
            raise
        ft = exc.factor
        stage
        if stage == 1:
            zmay_q1 = max_exp6stage1
            _ctx = (stage, n, settings4EPC, (_pt, j4exp, exp, max_exp6stage1))
        else:
            zmay_q2 = max_exp6stage2
            _ctx = (stage, n, settings4EPC, (j4exp, exp, max_exp6stage1, pt1), (_pt, j4delta, delta, max_exp6stage2))
        _ctx
        ctx = (_ctx, exc.ctx)
        #return ft if not with_ctx else (ft, ctx)
        return (ft, settings4EPC, stage, ((j4exp, zmay_q1) if stage==1 else (max_exp6stage1, j4delta, zmay_q2)))

    imay_j4exp6stage1
    imay_j4exp6stage2
    B1, B2
    pt1, pt2
    return (result6fail, ctx)
def _cached_mul_(max4delta6cache, cache, mul_, delta, pt1, /):
    if not delta in cache:
        pt7mul = mul_(delta, pt1)
        if delta <= max4delta6cache:
            cache[delta] = pt7mul
    else:
        pt7mul = cache[delta]
    pt7mul
    return pt7mul



















def to_even_ge_(low, u, /):
    check_type_is(int, u)
    u = max(low, u)
    if u&1:
        u += 1
    assert 0 == u&1
    assert low <= u
    return u
#def default__B1_from_n_(n, /):
def prepare4criteria4ECM7inversionless_(n, may_B1, may_B2, may_max4big_step, /, *, default_B1=10000, default_scale4B2=100, default_max4big_step=1<<16):
    B1 = ifNone(may_B1, default_B1)
    B1 = to_even_ge_(2, B1)

    B2 = ifNonef(may_B2, lambda:B1*default_scale4B2)
    B2 = to_even_ge_(B1, B2)

    max4big_step = ifNone(may_max4big_step, default_max4big_step)
    max4big_step = to_even_ge_(2, max4big_step)

    # approx_num_primes6stage2 = (B2-B1) //B2.bit_length()
    #1+floor_sqrt(B2-B1)
    big_step = to_even_ge_(2, 1+isqrt(B2-B1))
    big_step = min(max4big_step, big_step)



    assert 2 <= B1 <= B2
    assert 2 <= big_step

    assert 0 == B1&1
    assert 0 == B2&1
    assert 0 == big_step&1

    # [2 <= B1 <= B2]
    # [2 <= big_step]
    # [0 == B1%2]
    # [0 == B2%2]
    # [0 == big_step%2]
    return (B1, B2, big_step)

def _4imay_period4detect(n, imay_period4detect, /):
    check_int_ge(-1, imay_period4detect)
    match imay_period4detect:
        case -1:
            mk_iter4detect_ = lambda:repeat(False)
            return mk_iter4detect_
        case 1:
            mk_iter4detect_ = lambda:repeat(True)
            return mk_iter4detect_
        case 0:
            # auto
            period4detect = 4*n.bit_length()
        case period4detect:
            pass

    period4detect
    js = range(period4detect)[::-1]
    mk_iter4detect_ = lambda:(not j for j in cycle(js))
    return mk_iter4detect_

#baby_steps_giant_steps
#max4giant_step-->max4big_step
#big_step
def try1_factor_pint__elliptic_curve_method7inversionless_(n_or_settings4EPC, may_B1=None, may_B2=None, may_max4big_step=None, /, *, random_uint_mod_=None, result6fail=None, dup_exps_from_B1_=None, delta_exps_from_B1_B2_=None, default_B1=10000, default_scale4B2=100, default_max4big_step=1<<16, imay_period4detect=0):
    '-> (((result6fail|ft), may_exc_or_ctx) | (ft, settings4EPC, stage, ((j4exp, zmay_q1{==max_exp6stage1}) if stage==1 else (max_exp6stage1, j4delta, zmay_q2{==max_exp6stage2}))))'
    #TODO:++kw:drop_Y/inversionless#Ops4EllipticPseudocurve7DropY
    #vs:try1_factor_pint__elliptic_curve_method_
    ###########################
    match prepare4factor_pint__elliptic_curve_method_(n_or_settings4EPC, random_uint_mod_=random_uint_mod_, result6fail=result6fail, drop_Y=True, strict=False, detect6Incapable=True):
        case (-1, _, may_exc):
            return (result6fail, may_exc)
        #case (+1, ft):
        case (1, ft, may_exc):
            return (ft, may_exc)
        case (0, (n, settings4EPC, (ops4EPC, pt6EPC))):
            pass
        case _:
            raise 000
    (n, settings4EPC, (ops4EPC, pt6EPC))
    # [1 == gcd(n, 6)]
    ###########################
    (B1, B2, big_step) = prepare4criteria4ECM7inversionless_(n, may_B1, may_B2, may_max4big_step, default_B1=default_B1, default_scale4B2=default_scale4B2, default_max4big_step=default_max4big_step)
    # [2 <= B1 <= B2]
    # [2 <= big_step]
    # [0 == B1%2]
    # [0 == B2%2]
    # [0 == big_step%2]
    D = big_step>>1
    # [2*D == big_step]
    ###########################
    ctx = (n, settings4EPC, (ops4EPC, pt6EPC), (B1, B2, big_step))
    ###########################
    if 1:
        #########
        def _detect_pt_(pt1, /):
            '-> None|^FoundNonTrivialFactor'
            # [pt1 =!= O]
            ft = gcd(n, pt1.Z)
            if 1 < ft < n:
                raise FoundNonTrivialFactor(n, ft)
            # !! [pt1 =!= O]
            # [ft =!= n]
            assert ft == 1, settings4EPC
            # [not pt1.eq_partial_zero_mod_()]
        #########
        def _detect_u_(u, /):
            '-> None|^FoundNonTrivialFactor'
            ft = gcd(n, u)
            if 1 < ft < n:
                raise FoundNonTrivialFactor(n, ft)

    ###########################
    mk_iter4detect_ = _4imay_period4detect(n, imay_period4detect)
    pt0 = pt6EPC
    zmay_q1 = 0
    zmay_q2 = 0
    try:
        #########
        mul7h_ = ops4EPC.mul7h_
        dup_exps4stage1 = _xs5or_B_(B1, dup_exps_from_B1_, default__dup_exps_from_B1_)
        stage = 1
        zmay_q1 = 0
        j4exp = -1
        _pt = pt0
        iter4detect = mk_iter4detect_()
        for (j4exp, exp) in enumerate(dup_exps4stage1, 1+j4exp):
            assert exp > 0
            zmay_q1 = max(zmay_q1, exp)
            _pt7pre = _pt
            _pt = mul7h_(exp, _pt)
                # ^Incapable__add7h__X6diff_eq0
                # ^FoundNonTrivialFactor
            if _pt.eq_zero_():
                _detect_pt_(_pt7pre)
                    # ^FoundNonTrivialFactor
                return (result6fail, ctx)
            if next(iter4detect):
                _detect_pt_(_pt7pre)
                    # ^FoundNonTrivialFactor
        j4exp
        zmay_q1
        _pt
        #########
        zmay_q1
        imay_j4exp6stage1 = j4exp
        pt1 = _pt
        assert not pt1.eq_zero_()
        # [pt1 =!= O]
        _detect_pt_(pt1)
            # ^FoundNonTrivialFactor
        # [not pt1.eq_partial_zero_mod_()]
        #########
        max4delta6cache = D

        add7h_ = ops4EPC.add7h_
        delta_exps4stage2 = _xs5or_B_(B2, delta_exps_from_B1_B2_, default__delta_exps_from_B1_B2_, B1)
        stage = 2
        zmay_q2 = 0
        #_pt = pt1
        j4delta = -1
        iter4detect = mk_iter4detect_()
        it = enumerate(delta_exps4stage2, 1+j4delta)
        for (j4delta, delta) in it:
            assert delta >= 3
            assert delta&1 == 1#head
            zmay_q2 += delta

            q = zmay_q2
            cache = [pt7h_O, ops4EPC.double7h_(pt1)]
            for _ in range(2, 1+D):
                cache.append(add7h_(cache[-1], cache[1], cache[-2]))
            cache
            # [[j:<-[0..=D]] -> [cache[j] == 2*j<*>pt1]]

            pt8big_step = cache[D]
            # !! [2*D == big_step]
            # [pt8big_step == big_step<*>pt1]

            k4ref = q-2
            # !! [2 <= big_step]
            # [(q-k4ref) == 2 <= big_step]
            # [0 == (q-k4ref)%2][2 <= (q-k4ref) <= big_step]

            pt7ref = mul7h_(k4ref, pt1)
            pt7ref7pre = mul7h_(k4ref-big_step, pt1)
            # [pt7ref == k4ref<*>pt1]
            # [pt7ref7pre == (k4ref-big_step)<*>pt1]
            # [0 == (q-k4ref)%2][2 <= (q-k4ref) <= big_step]
            IIdiffs = pt7ref.diff7h7mod_(n, cache[(q-k4ref)>>1])
            if 0 == IIdiffs: return (result6fail, ctx)
            # [0 =!= IIdiffs %n]
            break
        else:
            IIdiffs = 1
        IIdiffs
        for (j4delta, delta) in it:
            # [pt7ref == k4ref<*>pt1]
            # [pt7ref7pre == (k4ref-big_step)<*>pt1]
            # [0 == (q-k4ref)%2][2 <= (q-k4ref) <= big_step]
            assert delta >= 2
            assert delta&1 == 0#not-head
            # [0 == delta%2]
            zmay_q2 += delta
            new_q = zmay_q2
            # [new_q -q == delta]
            # !! [0 == delta%2]
            # [0 == (new_q -q)%2]

            # !! [0 == (q-k4ref)%2][2 <= (q-k4ref) <= big_step]
            # [0 == (new_q-k4ref)%2][2+delta <= (new_q-k4ref) <= big_step+delta]
            while not (new_q-k4ref) <= big_step:
                # [(new_q-k4ref) > big_step]
                # [(new_q-(k4ref+big_step)) > 0]
                # !! [2 <= big_step]
                # => will stop
                k4ref += big_step
                (pt7ref, pt7ref7pre) = (add7h_(pt7ref, pt8big_step, pt7ref7pre), pt7ref)
                    # ^Incapable__add7h__X6diff_eq0
                    # ^FoundNonTrivialFactor
                # [pt7ref == k4ref<*>pt1]
                # [pt7ref7pre == (k4ref-big_step)<*>pt1]
                # [(new_q-k4ref) > 0]
                # !! [0 == big_step%2]
                # [0 == (new_q-k4ref)%2]
                # [(new_q-k4ref) >= 2]
            # [2 <= (new_q-k4ref) <= big_step]
            # [0 == (new_q-k4ref)%2][2 <= (new_q-k4ref) <= big_step]
            q = new_q
            # [pt7ref == k4ref<*>pt1]
            # [pt7ref7pre == (k4ref-big_step)<*>pt1]
            # [0 == (q-k4ref)%2][2 <= (q-k4ref) <= big_step]
            diff = pt7ref.diff7h7mod_(n, cache[(q-k4ref)>>1])
            IIdiffs7pre = IIdiffs
            # !! [0 =!= IIdiffs %n]
            # [0 =!= IIdiffs7pre %n]
            IIdiffs = diff*IIdiffs %n
            if 0 == IIdiffs:
                # !! MAYBE:[0 == diff%n]
                #_detect_u_(diff)
                    # ^FoundNonTrivialFactor
                # !! [0 =!= IIdiffs7pre %n]
                _detect_u_(IIdiffs7pre)
                    # ^FoundNonTrivialFactor
                return (result6fail, ctx)
            # [0 =!= IIdiffs %n]
            if next(iter4detect):
                _detect_u_(IIdiffs)
                    # ^FoundNonTrivialFactor
        j4delta
        zmay_q2
        _pt
        IIdiffs
        # [0 =!= IIdiffs %n]
        assert not 0 == IIdiffs
        #########
        zmay_q2
        imay_j4exp6stage2 = j4delta
        pt2 = _pt
        IIdiffs
        # [0 =!= IIdiffs %n]
        #########
        _detect_u_(IIdiffs)
            # ^FoundNonTrivialFactor
        #########
    except Incapable__add7h__X6diff_eq0:
        stage
        j4exp
        return (result6fail, exc)
    except FoundNonTrivialFactor as exc:
        if not exc.N == n:
            raise
        ft = exc.factor
        stage
        if stage == 1:
            zmay_q1
            _ctx = (stage, n, settings4EPC, (_pt, j4exp, exp, zmay_q1))
        else:
            zmay_q1
            zmay_q2
            _ctx = (stage, n, settings4EPC, (j4exp, exp, zmay_q1, pt1), (_pt, j4delta, delta, zmay_q2))
        _ctx
        ctx = (_ctx, exc.ctx)
        #return ft if not with_ctx else (ft, ctx)
        return (ft, settings4EPC, stage, ((j4exp, zmay_q1) if stage==1 else (zmay_q1, j4delta, zmay_q2)))

    imay_j4exp6stage1
    imay_j4exp6stage2
    B1, B2, D
    pt1, pt2
    return (result6fail, ctx)






















__all__
from seed.math.factor_pint.factor_pint__elliptic_curve_method import FoundFactor, FoundNonTrivialFactor, FoundTrivialFactor
from seed.math.factor_pint.factor_pint__elliptic_curve_method import Incapable__add7h__X6diff_eq0, ParamError__ops4EPC7DropY


####################################
#old_version:only B1
####################################
from seed.math.factor_pint.factor_pint__elliptic_curve_method import try_factor_pint__elliptic_curve_method_, ex1_try_factor_pint__elliptic_curve_method_
#def try_factor_pint__elliptic_curve_method_(n, Bs_or_kss=None, ks5n_and_B_or_ks_=None, /, *, random_uint_mod_=None, with_ctx=False, result6fail=None):
#def ex1_try_factor_pint__elliptic_curve_method_(n, B1, /, *, random_uint_mod_=None, settings4EPC=None):
#   'n/uint{>=1} -> B1/uint{>=2} -> may (ft/non_trivial_factor{n}, settings4EPC{n}, B1) # [B1 is smooth bound] # [settings4EPC == (args4EPC, xy6EPC) :: ((n,a,b),(x,y))]'


####################################
#new_version:both B1,B2
####################################
from seed.math.factor_pint.factor_pint__elliptic_curve_method import try1_factor_pint__elliptic_curve_method_
#def try1_factor_pint__elliptic_curve_method_(n_or_settings4EPC, B1_or_dup_exps4stage1, B2_or_delta_exps4stage2, /, *, random_uint_mod_=None, result6fail=None, dup_exps_from_B1_=None, delta_exps_from_B1_B2_=None):
#   '-> (((result6fail|ft), may_exc_or_ctx) | (ft, settings4EPC, stage, ((j4exp, zmay_q1{==max_exp6stage1}) if stage==1 else (max_exp6stage1, j4delta, zmay_q2{==max_exp6stage2}))))'
#def prepare4factor_pint__elliptic_curve_method_(n_or_settings4EPC, /, *, random_uint_mod_=None, result6fail=None, drop_Y=False):
#   '-> ((-1, result6fail, may_exc)|(+1, non_trivial_factor, may_exc)|(0, (n{[1 == gcd(n, 6)][n >= 25]}, settings4EPC, (ops4EPC/T, pt)))) | ^FoundFactor if to_raise | ^ParamError__ops4EPC7DropY if to_raise and drop_Y # [T := Ops4EllipticPseudocurve if not drop_Y else Ops4EllipticPseudocurve7DropY]'
#   not$drop_Y => [settings4EPC == (args4EPC, xy6EPC) :: ((n,a,b),(x,y))]
#   drop_Y => [settings4EPC == (args4EPC, XZ6EPC) :: ((n,N4C,D4C),(X,Z))]



from seed.math.factor_pint.factor_pint__elliptic_curve_method import try1_factor_pint__elliptic_curve_method7inversionless_
#def try1_factor_pint__elliptic_curve_method7inversionless_(n_or_settings4EPC, may_B1=None, may_B2=None, may_max4big_step=None, /, *, random_uint_mod_=None, result6fail=None, dup_exps_from_B1_=None, delta_exps_from_B1_B2_=None, default_B1=10000, default_scale4B2=100, default_max4big_step=1<<16):
#   '-> (((result6fail|ft), may_exc_or_ctx) | (ft, settings4EPC, stage, ((j4exp, zmay_q1{==max_exp6stage1}) if stage==1 else (max_exp6stage1, j4delta, zmay_q2{==max_exp6stage2}))))'
#   [settings4EPC == (args4EPC, XZ6EPC) :: ((n,N4C,D4C),(X,Z))]

from seed.math.factor_pint.factor_pint__elliptic_curve_method import *
