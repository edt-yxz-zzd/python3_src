#__all__:goto
#TODO:goto

# ??DONE:
#   实现:补丁:更多失败信息:
#       1. ctx{FoundTrivialFactor} verbose print_err;
#       2. stage1结束，stage2起始ctx 即使还未实现stage2，方便未来断点重启
#
#   DONE:实现: [X:Z] 省略Y，且齐次无需inv6N_()
#   DONE:实现:第二阶段:额外一个大素数

# [choose_B1__6ECM]:goto
# [:???is_perfect_power_ok__6ECM???]:goto
# [:inspect_why_almost_fail6prime_square6nonstrict]:goto
#   fail:try1_factor_pint__elliptic_curve_method7inversionless_@(**2)@{-strict}@{p_small} #but sometime succ rarely
#   fixed by:
#   #   # patch0001:goto
#   #   # patch0002:goto
#   #   # patch0003:goto


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
[[
Theorem 7.3.1 (Hasse).
[p::prime][p>3][k::int{>0}][a,b::FF(p**k)][FF(p**k).0 =!= (4*a**3+27*b**2)][EC{FF(p**k);a,b} := ({O}\-/{(x,y) | [x,y::FF(p**k)][y**2 == (x**3 +a*x +b)]})]:
    # FF(p**k) not ZZ%(p**k)
    [i::int]:
        [quadratic_character{FF(p**k);x} =[def]= if FF(p**k).0 == x then 0 elif is_square_(FF(p**k);x) then +1 else -1]

    [len(EC{FF(p**k);a,b}) == 1 +sum{1+quadratic_character{FF(p**k);(x**3 +a*x +b)} | [x::FF(p**k)]}]
    <==>:
    [len(EC{FF(p**k);a,b}) == 1+p**k +sum{quadratic_character{FF(p**k);(x**3 +a*x +b)} | [x::FF(p**k)]}]

    #Theorem 7.3.1 (Hasse).
    [abs(len(EC{FF(p**k);a,b}) -(1+p**k)) <= floor_sqrt(4*p**k)]
        # [k==1] => every len in this interval is actually order of some EC%p
    <==>:
    [(1+p**k) -floor_sqrt(4*p**k) <= len(EC{FF(p**k);a,b}) <= (1+p**k) +floor_sqrt(4*p**k)]
    [k:=1]:
        [(1+p) -floor_sqrt(4*p) <= len(EC{FF(p);a,b}) <= (1+p) +floor_sqrt(4*p)]

]]
[[
Chapter 7 ELLIPTIC CURVE ARITHMETIC
7.4 Elliptic curve method
7.4.1 Basic ECM algorithm
Algorithm 7.4.2 (Lenstra elliptic curve method (ECM)).
    # xxx:elliptic curve works over ZZ%p**k
    # elliptic curve works over FF(p**k)
    # [P+(-P) == O] must receive special treatment => partial-O crash

page338 [347/604]
[B2:=B1][n::composite{>3}][not$is_prime_(n)][#???not$is_prime_power_(n)???#][1==gcd(n,6)][p:=min{p | [p::prime][n%p==0]}]:
    ##################
    # [:???is_perfect_power_ok__6ECM???]:goto
    ##################
    # [[p-->+oo] -> [small_o(1) --> 0]]
    [TIME{ECM7stage1_only(n)} == O(exp((1+small_o(1))*sqrt(2*lnPlnlnP)))] where [B1 := (exp((1+small_o(1))*sqrt(1/2*lnPlnlnP)))]
        # [choose_B1__6ECM]:here
        # best via min (B1/prob(succ|B1))
        [TIME7per_trial{ECM7stage1_only(n)} ~= B]
        [num_trials7heuristic_expected{n} == 1/prob(succ|B1) == TIME{ECM7stage1_only(n)}/B1 == O(L_(p)**(sqrt2-1/sqrt2+small_o(1))) == O(L_(p)**(1/sqrt2+small_o(1)))]
        [num_trials7heuristic_expected{n} ~= B1]
        [TIME{ECM7stage1_only(n)} ~= B1**2]
    ##################
    [L_(p) =[def]= (exp(sqrt(lnPlnlnP)))]
    [TIME{ECM7stage1_only(n)} == O(L_(p)**(sqrt2+small_o(1)))] where [B1 := (L_(p)**(1/sqrt2+small_o(1)))]
        # the heuristic expected complexity of ECM to give a nontrivial factorization of n with least prime factor p is L_(p)**(√2+o(1)) arithmetic steps with integers the size of n.
        # (Note that the error expression “o(1)” tends to 0 as p tends to infinity.)
    ##################

B1_from_p_:goto
    batch_iter__7B1_from_p_:goto
TODO:iter_B1s_from_n_:goto
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
...       try:
...         k_pt = ops.mul7h_(k, pt_0)
...       except (Incapable__add7h__X6diff_eq0,FoundNonTrivialFactor) as exc:
...         print(k, repr(exc), sep=':')
...       else:
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
seed.math.factor_pint.factor_pint__elliptic_curve_method.FoundNonTrivialFactor: (35, 7, ((35, 16, 1), (Pt4EC7h(-7, 14), Pt4EC7h(8, 1), Pt4EC7h(0, -14))))
>>> #before_patch_123: seed.math.factor_pint.factor_pint__elliptic_curve_method.Incapable__add7h__X6diff_eq0: ((35, 16, 1), (Pt4EC7h(-7, 14), Pt4EC7h(8, 1), Pt4EC7h(0, -14)))

>>> n = 35
>>> show_diffs_(ops, pt_0, 60)
6:FoundNonTrivialFactor(35, 7, ((35, 16, 1), (Pt4EC7h(-7, 14), Pt4EC7h(8, 1), Pt4EC7h(0, -14))))
>>> #before_patch_123: 6:Incapable__add7h__X6diff_eq0((35, 16, 1), (Pt4EC7h(-7, 14), Pt4EC7h(8, 1), Pt4EC7h(0, -14)))

>>> show_diffs_(ops, pt_0, 60, same_also=True)
0:True:Pt4EC7h(0, 0):Pt4EC7h(0, 0)
1:True:Pt4EC7h(8, 1):Pt4EC7h(8, 1)
2:True:Pt4EC7h(14, 16):Pt4EC7h(14, 16)
3:True:Pt4EC7h(11, -17):Pt4EC7h(11, -17)
4:True:Pt4EC7h(-5, -14):Pt4EC7h(0, -14)
5:True:Pt4EC7h(1, 8):Pt4EC7h(-7, 14)
6:FoundNonTrivialFactor(35, 7, ((35, 16, 1), (Pt4EC7h(-7, 14), Pt4EC7h(8, 1), Pt4EC7h(0, -14))))
>>> #before_patch_123: 6:Incapable__add7h__X6diff_eq0((35, 16, 1), (Pt4EC7h(-7, 14), Pt4EC7h(8, 1), Pt4EC7h(0, -14)))


>>> show_muls_(ops, pt_0, 60)
0:Pt4EC7h(0, 0)
1:Pt4EC7h(8, 1)
2:Pt4EC7h(14, 16)
3:Pt4EC7h(11, -17)
4:Pt4EC7h(-5, -14)
5:Pt4EC7h(1, 8)
6:Pt4EC7h(14, 1)
7:Pt4EC7h(-6, 8)
8:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(-5, -14)))
9:Pt4EC7h(4, -17)
10:Pt4EC7h(14, 16)
11:Pt4EC7h(1, 8)
12:Pt4EC7h(15, -14)
13:Pt4EC7h(-6, -13)
14:Pt4EC7h(14, 16)
15:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(-5, -14)))
16:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(-5, -14)))
17:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(-5, -14)))
18:Pt4EC7h(14, 1)
19:Pt4EC7h(-6, -13)
20:Pt4EC7h(-5, -14)
21:Pt4EC7h(11, -17)
22:Pt4EC7h(14, 16)
23:Pt4EC7h(-6, 8)
24:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(15, -14)))
25:Pt4EC7h(-6, 8)
26:Pt4EC7h(14, 16)
27:Pt4EC7h(11, -17)
28:Pt4EC7h(-5, -14)
29:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(-5, -14)))
30:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(-5, -14)))
31:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(-5, -14)))
32:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(-5, -14)))
33:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(-5, -14)))
34:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(-5, -14)))
35:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(-5, -14)))
36:Pt4EC7h(15, -14)
37:Pt4EC7h(1, 8)
38:Pt4EC7h(14, 16)
39:Pt4EC7h(4, -17)
40:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(-5, -14)))
41:Pt4EC7h(-6, 8)
42:Pt4EC7h(14, 1)
43:Pt4EC7h(1, 8)
44:Pt4EC7h(-5, -14)
45:Pt4EC7h(4, -3)
46:Pt4EC7h(14, 16)
47:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(15, -14)))
48:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(15, -14)))
49:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(15, -14)))
50:Pt4EC7h(14, 16)
51:Pt4EC7h(4, -3)
52:Pt4EC7h(-5, -14)
53:Pt4EC7h(1, 8)
54:Pt4EC7h(14, 1)
55:Pt4EC7h(-6, 8)
56:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(-5, -14)))
57:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(-5, -14)))
58:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(-5, -14)))
59:FoundNonTrivialFactor(35, 7, ((35, 16, 1), Pt4EC7h(-5, -14)))

#before_patch_123:
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
20:FoundNonTrivialFactor(4087, 61, ((4087, 724, -1984), (Pt4EC7h(2013, -1891), Pt4EC7h(-694, -156), Pt4EC7h(0, -1159))))
>>> #before_patch_123: 20:Incapable__add7h__X6diff_eq0((4087, 724, -1984), (Pt4EC7h(2013, -1891), Pt4EC7h(-694, -156), Pt4EC7h(0, -1159)))

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
20:FoundNonTrivialFactor(4087, 61, ((4087, 724, -1984), (Pt4EC7h(2013, -1891), Pt4EC7h(-694, -156), Pt4EC7h(0, -1159))))
>>> #before_patch_123: 20:Incapable__add7h__X6diff_eq0((4087, 724, -1984), (Pt4EC7h(2013, -1891), Pt4EC7h(-694, -156), Pt4EC7h(0, -1159)))
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
20:FoundNonTrivialFactor(4087, 61, ((4087, 724, -1984), (Pt4EC7h(2013, -1891), Pt4EC7h(-694, -156), Pt4EC7h(0, -1159))))
>>> #before_patch_123:20:FoundNonTrivialFactor(4087, 61, (4087, 724, -1984))



>>> default_B1=10000
>>> settings4EPC = ((4087, 724, -1984), (-694, -156))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(settings4EPC)
(61, ((4087, 724, -1984), (-694, -156)), 1, (5, 7))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(settings4EPC, default_B1)
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
(None, ((4087, ((4087, 724, -1984), (-694, -156)), (Ops4EllipticPseudocurve7DropY(4087, 724, -1984, detect6Incapable = True, strict = False), Pt4EC7h(-694, -156)), (2, 10, 4)), (2, 10, Pt4EC7h(-98, 1564), Pt4EC7h(-98, 1564))))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(settings4EPC, 3, 5)
(61, ((4087, 724, -1984), (-694, -156)), 2, (3, 0, 5))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(settings4EPC, 3, 4)
(None, ((4087, ((4087, 724, -1984), (-694, -156)), (Ops4EllipticPseudocurve7DropY(4087, 724, -1984, detect6Incapable = True, strict = False), Pt4EC7h(-694, -156)), (4, 4, 2)), (4, 4, Pt4EC7h(-1906, 1655), Pt4EC7h(-1906, 1655))))








>>> try1_factor_pint__elliptic_curve_method7inversionless_(35, default_B1) #doctest: +SKIP
(7, ((35, -3, 1), (-8, 1)), 1, (13, 3))
(5, ((35, 10, 1), (-10, 1)), 1, (13, 3))
(5, ((35, -16, 1), (-3, 1)), 1, (13, 3))
(None, (35, ((35, 5, 1), (-7, 1)), (Ops4EllipticPseudocurve7DropY(35, 5, 1, detect6Incapable = True, strict = False), Pt4EC7h(-7, 1)), (10000, 1000000, 996)))
(None, (35, ((35, 5, 1), (15, 1)), (Ops4EllipticPseudocurve7DropY(35, 5, 1, detect6Incapable = True, strict = False), Pt4EC7h(15, 1)), (10000, 1000000, 996)))

>>> try1_factor_pint__elliptic_curve_method7inversionless_(((35, -3, 1), (-8, 1)))
(7, ((35, -3, 1), (-8, 1)), 1, (2, 3))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(((35, -3, 1), (-8, 1)), default_B1)
(7, ((35, -3, 1), (-8, 1)), 1, (13, 3))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(((35, -16, 1), (-3, 1)))
(7, ((35, -16, 1), (-3, 1)), 1, (2, 3))
>>> #before_patch_123:(None, ((35, ((35, -16, 1), (-3, 1)), (Ops4EllipticPseudocurve7DropY(35, -16, 1, detect6Incapable = True, strict = False), Pt4EC7h(-3, 1)), (4, 400, 20)), '@stage1...', (Pt4EC7h(15, 4), 3)))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(((35, -16, 1), (-3, 1)), default_B1)
(5, ((35, -16, 1), (-3, 1)), 1, (13, 3))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(((35, 5, 1), (15, 1)))
(7, ((35, 5, 1), (15, 1)), 1, (0, 2))
>>> #before_patch_123:(None, ((35, ((35, 5, 1), (15, 1)), (Ops4EllipticPseudocurve7DropY(35, 5, 1, detect6Incapable = True, strict = False), Pt4EC7h(15, 1)), (4, 400, 20)), '@stage1...', (Pt4EC7h(15, 1), 2)))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(((35, 5, 1), (15, 1)), default_B1)
(7, ((35, 5, 1), (15, 1)), 1, (0, 2))
>>> #before_patch_123:(None, ((35, ((35, 5, 1), (15, 1)), (Ops4EllipticPseudocurve7DropY(35, 5, 1, detect6Incapable = True, strict = False), Pt4EC7h(15, 1)), (10000, 1000000, 996)), '@stage1...', (Pt4EC7h(15, 1), 2)))













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






# [:???is_perfect_power_ok__6ECM???]:goto
# [:inspect_why_almost_fail6prime_square6nonstrict]:goto
    ok:try1_factor_pint__elliptic_curve_method_
    ok:try1_factor_pint__elliptic_curve_method7inversionless_@(**e{>2})
    ok:try1_factor_pint__elliptic_curve_method7inversionless_@(**2)@{+strict}
    half_ok:try1_factor_pint__elliptic_curve_method7inversionless_@(**2)@{-strict}@{p_big_enough}
    fail:try1_factor_pint__elliptic_curve_method7inversionless_@(**2)@{-strict}@{p_small} #but sometime succ rarely
>>> try1_factor_pint__elliptic_curve_method7inversionless_(257**2, detect_square_at_first=False) # all fails #doctest: +SKIP
(None, (66049, ((66049, -25786, 1), (-17962, 1)), (Ops4EllipticPseudocurve7DropY(66049, -25786, 1, detect6Incapable = True, strict = False), Pt4EC7h(-17962, 1)), (10000, 1000000, 996)))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(257**3, detect_square_at_first=False) #doctest: +SKIP
(66049, ((16974593, 3458899, 1), (4418285, 1)), 1, (99, 227))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(257**4, detect_square_at_first=False) #doctest: +SKIP
(66049, ((4362470401, -118380204, 1), (563157099, 1)), 1, (131, 419))


>>> try1_factor_pint__elliptic_curve_method7inversionless_(257**2)
(257, None)
>>> try1_factor_pint__elliptic_curve_method7inversionless_(257**2, detect_square_at_first=True)
(257, None)
>>> try1_factor_pint__elliptic_curve_method7inversionless_(257**4, detect_square_at_first=True)
(66049, None)
>>> try1_factor_pint__elliptic_curve_method7inversionless_(257**3, detect_square_at_first=True) #doctest: +SKIP
(66049, ((16974593, 1817534, 1), (6329146, 1)), 1, (13, 3))


+strict
>>> try1_factor_pint__elliptic_curve_method7inversionless_(11**2, detect_square_at_first=False, strict=True) #doctest: +SKIP
(11, FoundNonTrivialFactor(121, 11, (121, -49, -14)))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(257**2, detect_square_at_first=False, strict=True) #doctest: +SKIP
(257, ((66049, -25936, -6915), (-15962, -26192)), 2, (13, 9, 53))
>>> try1_factor_pint__elliptic_curve_method7inversionless_(10007**2, detect_square_at_first=False, strict=True) #doctest: +SKIP
(10007, ((100140049, 47924418, 37626515), (38054523, 12458095)), 2, (31, 108, 659))

p_big_enough
>>> try1_factor_pint__elliptic_curve_method7inversionless_(10007**2, detect_square_at_first=False, strict=False) #doctest: +SKIP
(10007, ((100140049, 19640702, 1), (37248481, 1)), 2, (31, 108, 659))


-7inversionless
>>> try1_factor_pint__elliptic_curve_method_(11**2, detect_square_at_first=False) #doctest: +SKIP
(11, ((121, -38, 19), (5, -14)), 2, (3, 0, 5))
>>> try1_factor_pint__elliptic_curve_method_(((121, -38, 19), (5, -14)), detect_square_at_first=False)
(11, ((121, -38, 19), (5, -14)), 2, (3, 0, 5))










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
B1_from_p_
    batch_iter__7B1_from_p_
    max_B1_from_n_
        batch_iter__7max_B1_from_n_

try1_factor_pint__elliptic_curve_method7inversionless_
    prepare4criteria4ECM7inversionless_



try1_factor_pint__elliptic_curve_method_
    prepare4factor_pint__elliptic_curve_method_
    default__B1_from_n_
    default__dup_exps_from_B1_may_B1pw_
    default__delta_exps_from_B1_B2_
    default__asc_exps_from_B1_B2_          iter_deltas5asc_ints_



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


iter_error_pairs4add_table4EPC6square_modulus_
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
        # [:???is_perfect_power_ok__6ECM???]:goto
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
    from itertools import repeat, cycle, islice, product

#.#################################
___end_mark_of_excluded_global_names__0___ = ...
#e script/整数分解牜凑平方牜凑整除幂.py


__all__
r'''[[[[[[[[[
[[[
===
[[
# [:???is_perfect_power_ok__6ECM???]:goto
is_prime_square_ <: is_prime_power_ <: is_perfect_power_
is_perfect_square_ <: is_perfect_power_

++kw:detect_square_at_first
    <<==:
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ -detect_square_at_first ='257**2'
    (None, (66049, ((66049, -25786, 1), (-17962, 1)), (Ops4EllipticPseudocurve7DropY(66049, -25786, 1, detect6Incapable = True, strict = False), Pt4EC7h(-17962, 1)), (10000, 1000000, 996)))
    ...
    ...all fail...
    ...

py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ -detect_square_at_first ='257**3'
    (66049, ((16974593, 3458899, 1), (4418285, 1)), 1, (99, 227))

py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ -detect_square_at_first ='257**4'
    (66049, ((4362470401, -118380204, 1), (563157099, 1)), 1, (131, 419))

py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ -detect_square_at_first ='67**2'
    (None, (4489, ((4489, -26, 1), (1227, 1)), (Ops4EllipticPseudocurve7DropY(4489, -26, 1, detect6Incapable = True, strict = False), Pt4EC7h(1227, 1)), (10000, 1000000, 996)))
    ...
    ...all fail...
    ...

py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ -detect_square_at_first ='67**3'
    (4489, ((300763, -33496, 1), (11712, 1)), 1, (14, 3))

py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ -detect_square_at_first ='67**4'
    (4489, ((20151121, 9722493, 1), (2337337, 1)), 1, (99, 227))

+detect_square_at_first
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ +detect_square_at_first ='67**2'
    (67, None)
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ +detect_square_at_first ='67**4'
    (4489, None)
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ +detect_square_at_first ='67**3'
    (4489, ((300763, 126846, 1), (92612, 1)), 1, (75, 97))

]]
[[
# [:???is_perfect_power_ok__6ECM???]:goto
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   ,iter_error_pairs4add_table4EPC6square_modulus_ =5
    (Ops4EllipticPseudocurve(25, 6, -9), Pt4EC(-1, -3))
    ...320 行
py_adhoc_call { +lineno +to_show_StopIteration_value }  seed.math.factor_pint.factor_pint__elliptic_curve_method   ,iter_error_pairs4add_table4EPC6square_modulus_ ='((25, 6, -9), (-1, -3))'
    320:(True, (Pt4EC(-1, -3), Pt4EC(-6, -8)))
    321:(Ops4EllipticPseudocurve(25, 6, -9), Pt4EC(-1, -3))

py_adhoc_call { +lineno +to_show_StopIteration_value }  seed.math.factor_pint.factor_pint__elliptic_curve_method   ,iter_error_pairs4add_table4EPC6square_modulus_ =7
    #########
    ...
    336:(True, (Pt4EC(-5, -19), Pt4EC(-12, -5)))
    337:(Ops4EllipticPseudocurve(49, -6, 15), Pt4EC(?, ?))
    #########
    ...
    714:(True, (Pt4EC(-2, -16), Pt4EC(-9, -2)))
    715:(Ops4EllipticPseudocurve(49, 17, 4), Pt4EC(-5, 23))
    #########
    ...
    672:(True, (Pt4EC(-2, -3), Pt4EC(-9, -10)))
    673:((Ops4EllipticPseudocurve(49, 10, -12), Pt4EC(7, -3)), (2577, 672, 0))
    #########
    ...
    462:(True, (Pt4EC(-2, -6), Pt4EC(-9, -20)))
    463:((Ops4EllipticPseudocurve(49, 13, 21), Pt4EC(-23, 1)), (50, 2500), (2038, 462, 0))
    #########
    ...
    336:(True, (Pt4EC(-5, -2), Pt4EC(-12, -16)))
    337:((Ops4EllipticPseudocurve(49, -13, 15), Pt4EC(-5, 2)), (29, 841), (505, 336, 0))
    #########
    ...
    336:(True, (Pt4EC(-3, -2), Pt4EC(-10, -9)))
    337:((Ops4EllipticPseudocurve(49, 11, 15), Pt4EC(11, -12)), (29, 841), (505, 336, 0))
    #########
py_adhoc_call { +lineno +to_show_StopIteration_value }  seed.math.factor_pint.factor_pint__elliptic_curve_method   ,iter_error_pairs4add_table4EPC6square_modulus_ =11
    #########
    ...
    1870:(True, (Pt4EC(-4, -19), Pt4EC(-15, -3)))
    1871:((Ops4EllipticPseudocurve(121, -49, -13), Pt4EC(-54, -7)), (100, 10000), (8130, 1870, 0))
    #########
    ...
    2750:(True, (Pt4EC(-2, -57), Pt4EC(-13, -57)))
    2751:((Ops4EllipticPseudocurve(121, -23, -56), Pt4EC(47, -21)), (144, 20736), (17986, 2750, 0))
    #########


xy6EPC
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method_ -detect_square_at_first ='11**2'
    (11, ((121, -38, 19), (5, -14)), 2, (3, 0, 5))
    (11, ((121, -24, 54), (38, 13)), 1, (2, 3))

# [:inspect_why_almost_fail6prime_square6nonstrict]:here
XZ6EPC
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ -detect_square_at_first ='((121, -24, 54), (38, 13))'
    (11, ((121, -24, 54), (38, 13)), 2, (3, 2, 11))
    ???why???
    竟然可能成功=>mk_ex5n__7random_() : try_fix__bug__almost_fail6prime_square_7turnoff_detect_square_at_first:goto#fail...

XZ6EPC
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ -detect_square_at_first ='11**2'
    (None, (121, ((121, 18, 1), (-40, 1)), (Ops4EllipticPseudocurve7DropY(121, 18, 1, detect6Incapable = True, strict = False), Pt4EC7h(-40, 1)), (4, 400, 20)))
    (None, ((121, ((121, -45, 1), (-21, 1)), (Ops4EllipticPseudocurve7DropY(121, -45, 1, detect6Incapable = True, strict = False), Pt4EC7h(-21, 1)), (4, 400, 20)), '@stage1...'))
    (None, ((121, ((121, -55, 1), (-36, 1)), (Ops4EllipticPseudocurve7DropY(121, -55, 1, detect6Incapable = True, strict = False), Pt4EC7h(-36, 1)), (4, 400, 20)), '@stage1...'))
    (None, ((121, ((121, -5, 1), (-48, 1)), (Ops4EllipticPseudocurve7DropY(121, -5, 1, detect6Incapable = True, strict = False), Pt4EC7h(-48, 1)), (4, 400, 20)), '@stage1...', (Pt4EC7h(-10, -4), 3)))
    #########
    # try_fix__bug__almost_fail6prime_square_7turnoff_detect_square_at_first:  .1:之后, .2:之前:
    #竟然成功一次:
    (11, ((121, -32, 1), (-44, 1)), 1, (2, 3))
    #########
    # try_fix__bug__almost_fail6prime_square_7turnoff_detect_square_at_first:  .1:之后, .2:之后:
    (11, ((121, 19, 1), (-11, 1)), 1, (2, 3))
    (None, ((121, ((121, 1, 1), (58, 1)), (Ops4EllipticPseudocurve7DropY(121, 1, 1, detect6Incapable = True, strict = False), Pt4EC7h(58, 1)), (4, 400, 20)), '@stage2.begin...', (3, 5, Pt4EC7h(0, 35), Pt4EC7h(0, 0))))
    (None, ((121, ((121, -57, 1), (2, 1)), (Ops4EllipticPseudocurve7DropY(121, -57, 1, detect6Incapable = True, strict = False), Pt4EC7h(2, 1)), (4, 400, 20)), '@stage1...', (Pt4EC7h(-30, 24), 3)))
    # after:++『if cache[-1].eq_zero_()...』#detect6cache:goto
    (None, ((121, ((121, -55, 1), (34, 1)), (Ops4EllipticPseudocurve7DropY(121, -55, 1, detect6Incapable = True, strict = False), Pt4EC7h(34, 1)), (4, 400, 20)), '@stage1...', (Pt4EC7h(0, -47), 2)))
    (None, ((121, ((121, 56, 1), (-27, 1)), (Ops4EllipticPseudocurve7DropY(121, 56, 1, detect6Incapable = True, strict = False), Pt4EC7h(-27, 1)), (4, 400, 20)), '@stage2.begin:@init-cache...:[2*j<*>pt1 == O]', (4, Pt4EC7h(-21, -21), Pt4EC7h(0, 23))))

py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ -detect_square_at_first ='((121, 1, 1), (58, 1))'
    # after:++『if pt8small_step.eq_zero_()...』
    # after:++『if cache[-1].eq_zero_()...』#detect6cache:goto
    (None, ((121, ((121, 1, 1), (58, 1)), (Ops4EllipticPseudocurve7DropY(121, 1, 1, detect6Incapable = True, strict = False), Pt4EC7h(58, 1)), (4, 400, 20)), '@stage2.begin:@init-cache.begin...:[2<*>pt1 == O]', (2, Pt4EC7h(0, 35))))
    # after:++『if _pt.X == 0:...』#detect_X6stage1:goto
    (None, ((121, ((121, 1, 1), (58, 1)), (Ops4EllipticPseudocurve7DropY(121, 1, 1, detect6Incapable = True, strict = False), Pt4EC7h(58, 1)), (4, 400, 20)), '@stage1:...[X==0]', (Pt4EC7h(20, 13), 2, Pt4EC7h(0, 35))))
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ -detect_square_at_first ='((121, 56, 1), (-27, 1))'
    # after:++『if cache[-1].eq_zero_()...』#detect6cache:goto
    (None, ((121, ((121, 56, 1), (-27, 1)), (Ops4EllipticPseudocurve7DropY(121, 56, 1, detect6Incapable = True, strict = False), Pt4EC7h(-27, 1)), (4, 400, 20)), '@stage2.begin:@init-cache...:[2*j<*>pt1 == O]', (4, Pt4EC7h(-21, -21), Pt4EC7h(0, 23))))

XZ6EPC,+strict
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ -detect_square_at_first +strict ='11**2'
    (11, FoundNonTrivialFactor(121, 11, (121, -49, -14)))

py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ -detect_square_at_first +strict ='257**2'
    (257, ((66049, -25936, -6915), (-15962, -26192)), 2, (13, 9, 53))

py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ -detect_square_at_first +strict ='10007**2'
(10007, ((100140049, 47924418, 37626515), (38054523, 12458095)), 2, (31, 108, 659))



XZ6EPC,-strict,p_big_enough
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ -detect_square_at_first -strict ='10007**2'
    (10007, ((100140049, 44102985, 1), (26001311, 1)), 2, (31, 194, 1277))
    (None, ((100140049, ((100140049, 44887264, 1), (-46589411, 1)), (Ops4EllipticPseudocurve7DropY(100140049, 44887264, 1, detect6Incapable = True, strict = False), Pt4EC7h(-46589411, 1)), (32, 3200, 58)), '@stage2.begin:@init-cache...:[2*j<*>pt1 == O]', (50, Pt4EC7h(30794043, -7332337), Pt4EC7h(34634457, -19479392))))
    (10007, ((100140049, 23804839, 1), (15222891, 1)), 2, (31, 42, 251))
    (None, ((100140049, ((100140049, 20881417, 1), (-35257327, 1)), (Ops4EllipticPseudocurve7DropY(100140049, 20881417, 1, detect6Incapable = True, strict = False), Pt4EC7h(-35257327, 1)), (32, 3200, 58)), '@stage1...', (Pt4EC7h(18938411, -24529588), 31)))
    (10007, ((100140049, 19640702, 1), (37248481, 1)), 2, (31, 108, 659))
    half_ok
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @try1_factor_pint__elliptic_curve_method7inversionless_ -detect_square_at_first -strict ='55555559**2'
    (None, ((3086420135802481, ((3086420135802481, 6679540342757, 1), (575078109688372, 1)), (Ops4EllipticPseudocurve7DropY(3086420135802481, 6679540342757, 1, detect6Incapable = True, strict = False), Pt4EC7h(575078109688372, 1)), (256, 25600, 160)), (256, 25600, Pt4EC7h(1386745087006760, 321760178702510), Pt4EC7h(1386745087006760, 321760178702510))))
    (55555559, ((3086420135802481, -781829452349751, 1), (88854043241671, 1)), 2, (251, 1040, 8783))
    (None, ((3086420135802481, ((3086420135802481, 1314248336871218, 1), (871949769330518, 1)), (Ops4EllipticPseudocurve7DropY(3086420135802481, 1314248336871218, 1, detect6Incapable = True, strict = False), Pt4EC7h(871949769330518, 1)), (256, 25600, 160)), (256, 25600, Pt4EC7h(924553739202990, 576598827605744), Pt4EC7h(924553739202990, 576598827605744))))
    (None, ((3086420135802481, ((3086420135802481, 1098765936218349, 1), (-524732384086169, 1)), (Ops4EllipticPseudocurve7DropY(3086420135802481, 1098765936218349, 1, detect6Incapable = True, strict = False), Pt4EC7h(-524732384086169, 1)), (256, 25600, 160)), (256, 25600, Pt4EC7h(-930800569541153, -924913444529554), Pt4EC7h(-930800569541153, -924913444529554))))
    (55555559, ((3086420135802481, 305146434596480, 1), (1037237117303743, 1)), 2, (251, 86, 811))
    (None, ((3086420135802481, ((3086420135802481, 1076358357128684, 1), (-1441767787492636, 1)), (Ops4EllipticPseudocurve7DropY(3086420135802481, 1076358357128684, 1, detect6Incapable = True, strict = False), Pt4EC7h(-1441767787492636, 1)), (256, 25600, 160)), (256, 25600, Pt4EC7h(-1165141384675086, 794824401768530), Pt4EC7h(-1165141384675086, 794824401768530))))
    (None, ((3086420135802481, ((3086420135802481, 914545166712481, 1), (-1286084457219141, 1)), (Ops4EllipticPseudocurve7DropY(3086420135802481, 914545166712481, 1, detect6Incapable = True, strict = False), Pt4EC7h(-1286084457219141, 1)), (256, 25600, 160)), (256, 25600, Pt4EC7h(1367475516347820, 176489216910736), Pt4EC7h(1367475516347820, 176489216910736))))
    (None, ((3086420135802481, ((3086420135802481, -1192174267143316, 1), (160462262489171, 1)), (Ops4EllipticPseudocurve7DropY(3086420135802481, -1192174267143316, 1, detect6Incapable = True, strict = False), Pt4EC7h(160462262489171, 1)), (256, 25600, 160)), (256, 25600, Pt4EC7h(730852734770698, -1478343191605623), Pt4EC7h(730852734770698, -1478343191605623))))
    (55555559, ((3086420135802481, 957409698687769, 1), (1161290665971497, 1)), 2, (251, 2704, 24971))
    (None, ((3086420135802481, ((3086420135802481, 269862868064953, 1), (-1189137358966096, 1)), (Ops4EllipticPseudocurve7DropY(3086420135802481, 269862868064953, 1, detect6Incapable = True, strict = False), Pt4EC7h(-1189137358966096, 1)), (256, 25600, 160)), (256, 25600, Pt4EC7h(909430932820371, 563923072786449), Pt4EC7h(909430932820371, 563923072786449))))
    (None, ((3086420135802481, ((3086420135802481, 1202423080168366, 1), (-1088847347504767, 1)), (Ops4EllipticPseudocurve7DropY(3086420135802481, 1202423080168366, 1, detect6Incapable = True, strict = False), Pt4EC7h(-1088847347504767, 1)), (256, 25600, 160)), (256, 25600, Pt4EC7h(-354953312193422, 661795627729877), Pt4EC7h(-354953312193422, 661795627729877))))
    (None, ((3086420135802481, ((3086420135802481, -542732720085494, 1), (-293675450238730, 1)), (Ops4EllipticPseudocurve7DropY(3086420135802481, -542732720085494, 1, detect6Incapable = True, strict = False), Pt4EC7h(-293675450238730, 1)), (256, 25600, 160)), '@stage1...', (Pt4EC7h(-1098866084984775, -606147096852929), 229)))
    (55555559, ((3086420135802481, 1119471487987115, 1), (-1385011322393185, 1)), 2, (251, 416, 3343))
    (None, ((3086420135802481, ((3086420135802481, 166270660776580, 1), (619103611537477, 1)), (Ops4EllipticPseudocurve7DropY(3086420135802481, 166270660776580, 1, detect6Incapable = True, strict = False), Pt4EC7h(619103611537477, 1)), (256, 25600, 160)), '@stage1...', (Pt4EC7h(328946463770891, 947120775579169), 79)))
    (None, ((3086420135802481, ((3086420135802481, -1349609412034606, 1), (-361683877800516, 1)), (Ops4EllipticPseudocurve7DropY(3086420135802481, -1349609412034606, 1, detect6Incapable = True, strict = False), Pt4EC7h(-361683877800516, 1)), (256, 25600, 160)), (256, 25600, Pt4EC7h(583378581498287, 641875017414280), Pt4EC7h(583378581498287, 641875017414280))))
    (55555559, ((3086420135802481, 736616997974826, 1), (574005424832666, 1)), 2, (251, 416, 3343))
    # succ ratio:5/16

_count_succ_ratio_
    -> (total, c7fail, c7ok)
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @_count_succ_ratio_ =100 :7inversionless -detect_square_at_first -strict ='10007**2'
    (100, 22, 78)
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @_count_succ_ratio_ =100 :7inversionless -detect_square_at_first -strict ='55555559**2'
    (100, 66, 34)
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @_count_succ_ratio_ =100 :7inversionless -detect_square_at_first -strict ='44444444444444461**2'
    (100, 100, 0)
    # too big
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @max_B1_from_n_ ='44444444444444461**2'
    4096
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @_count_succ_ratio_ =20 :7inversionless -detect_square_at_first -strict ='44444444444444461**2' =10000
    (20, 19, 1)
    (20, 17, 3)
#########################
#above:before_patch_123:
#########################
#below:after_patch_123:
#########################
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @_count_succ_ratio_ =20 :7inversionless -detect_square_at_first -strict ='44444444444444461**2' =10000
    (20, 20, 0)
    fail
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @_count_succ_ratio_ =20 :7inversionless -detect_square_at_first -strict ='44444444444444461**2'
    (20, 20, 0)
    fail
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @_count_succ_ratio_ =20 :7inversionless -detect_square_at_first -strict ='55555559**2'
    (20, 12, 8)
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @_count_succ_ratio_ =20 :7inversionless -detect_square_at_first -strict ='257**2'
    (20, 3, 17)
py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @_count_succ_ratio_ =20 :7inversionless -detect_square_at_first -strict ='11**2'
    (20, 12, 8)
]]
[[
# [choose_B1__6ECM]:goto
py_adhoc_call { --lineno=2 }  seed.math.factor_pint.factor_pint__elliptic_curve_method   ,batch_iter__7B1_from_p_ ='[1+(1<<ez) for ez in range(2,1+100)]'
2:(5, 2)
3:(9, 4)
4:(17, 4)
5:(33, 8)
6:(65, 8)
7:(129, 16)
...
11:(2049, 16)
12:(4097, 32)
...
14:(16385, 32)
15:(32769, 64)
...
18:(262145, 64)
19:(524289, 128)
...
24:(16777217, 128)
25:(33554433, 256)
...
30:(1073741825, 256)
31:(2147483649, 512)
...
32:(4294967297, 512)
33:(8589934593, 1024)
...
39:(549755813889, 1024)
40:(1099511627777, 2048)
...
46:(70368744177665, 2048)
47:(140737488355329, 4096)
...
55:(36028797018963969, 4096)
56:(72057594037927937, 8192)
...
62:(4611686018427387905, 8192)
63:(9223372036854775809, 16384)
64:(18446744073709551617, 32768)
...
72:(4722366482869645213697, 32768)
73:(9444732965739290427393, 65536)
...
81:(2417851639229258349412353, 65536)
82:(4835703278458516698824705, 131072)
...
91:(2475880078570760549798248449, 131072)
92:(4951760157141521099596496897, 262144)
...
100:(1267650600228229401496703205377, 262144)

py_adhoc_call { --lineno=3 }  seed.math.factor_pint.factor_pint__elliptic_curve_method   ,batch_iter__7max_B1_from_n_ +only_B1 ='[1+(1<<ez) for ez in range(3,1+100)]'
3:2
4:2
5:4
...
8:4
9:8
...
12:8
13:16
...
22:16
23:32
...
28:32
29:64
...
36:64
37:128
...
48:128
49:256
...
60:256
61:512
...
64:512
65:1024
...
78:1024
79:2048
...
92:2048
93:4096
...
100:4096

]]
===
]]]
#]]]]]]]]]'''#'''
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
    def mul_X_Z_mod_(sf, n, /):
        return (sf.X * sf.Z)%n

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
        default__dup_exps_from_B1_may_B1pw_
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
            # <<== [B:=0][X1==0]
        [_addh((X1:Z1),(X2:Z2),(Xn:Zn)) =[def]= _doubleh((X1:Z1)) =[def]= (0:0)]

    [P1=!=O][P2=!=O][P1=!=-P2][P1==+P2]:
        [Zn == 0]
        [X1*Z2 == X2*Z1]
        [P1=!=-P1]
        [0 =!= (X1**3 +C*X1**2*Z1 +A*X1*Z1**2 +B*Z1**3)]
            # [B:=0] ==>> [X1=!=0]
        [Xp := ((X1**2 -A*Z1**2)**2 -4*B*(2*X1 +C*Z1)*Z1**3)]
            # [B:=0][A:=1][Xp==0] ==>> [0 == (X1**2 -Z1**2)**2 %n][1 < gcd(n, X1-Z1) <= n]
            # fix: [:inspect_why_almost_fail6prime_square6nonstrict]:goto
            # patch0003:goto
        [Zp := 4*Z1*(X1**3 +C*X1**2*Z1 +A*X1*Z1**2 +B*Z1**3)]
            # [Zp =?= 0]
            # !! [Z1 =!= 0]
            # [Zp == 0] => [1 <= gcd(n, Z1) < n]
            # fix: [:inspect_why_almost_fail6prime_square6nonstrict]:goto
            # patch0003:goto
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
        #old:raise Incapable__add7h__X6diff_eq0#[Xp:=???/Xn]
        !! [Xn == 0]
        [xn == Xn/Zn == 0]
        [0 == xp*xn == ((X1*X2 -A*Z1*Z2)**2 -4*B*(X1*Z2 +X2*Z1 +C*Z1*Z2)*Z1*Z2)/(X1*Z2 -X2*Z1)**2]
            # [B:=0][A:=1][Xn==0] ==>> [0 == (X1*X2 -Z1*Z2)**2 %n][1 < gcd(n, (X1*X2 -Z1*Z2)) <= n] # ??what about:(X1*Z2 -X2*Z1)
            # fix: [:inspect_why_almost_fail6prime_square6nonstrict]:goto
            # patch0001:goto


    [P1=!=O][P2=!=O][P1=!=-P2][P1=!=+P2][Xn =!= 0]:
        [Zn =!= 0]
        [X1*Z2 =!= X2*Z1]
        [Xp := Zn * ((X1*X2 -A*Z1*Z2)**2 -4*B*(X1*Z2 +X2*Z1 +C*Z1*Z2)*Z1*Z2)]
            # [B:=0][A:=1][Xp==0] ==>> [0 == Zn*(X1*X2 -Z1*Z2)**2 %n][1 < gcd(n, (X1*X2 -Z1*Z2)) <= n]
            # fix: [:inspect_why_almost_fail6prime_square6nonstrict]:goto
            # patch0002:goto
        [Zp := Xn * (X1*Z2 -X2*Z1)**2]
            # !! [X1*Z2 =!= X2*Z1]
            # [B:=0][A:=1][Zp==0] ==>> [0 == Xn*(X1*Z2 -X2*Z1)**2 %n][1 < gcd(n, (X1*Z2 -X2*Z1)) < n]
            # fix: [:inspect_why_almost_fail6prime_square6nonstrict]:goto
            # patch0002:goto
        [_addh((X1:Z1),(X2:Z2),(Xn:Zn)) =[def]= (Xp:Zp)]

        !! [P1-P2 =[repr]= (Xn:Zn) =[repr]= P2-P1]
        [_addh((X2:Z2),(X1:Z1),(Xn:Zn)) == (Xp:Zp)]

    #add7h_:goto
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
    def __contains__(sf, pt, /):
        match pt:
            case sf.zero:
                return True
            case Pt4EC(x=x, y=y):
                (n, a, b) = sf.params4elliptic_pseudocurve
                return 0 == (pow(y, 2, n) -(pow(x, 3, n) +a*x +b)) %n
            case _:
                raise TypeError(pt)
        raise 000

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
        'Pt4EC -> Pt4EC -> Pt4EC | ^FoundNonTrivialFactor | ^FoundTrivialFactor'
        return sf.add_(pt, pt)
    def sub_(sf, pt6lhs, pt6rhs, /):
        'Pt4EC -> Pt4EC -> Pt4EC | ^FoundNonTrivialFactor | ^FoundTrivialFactor'
        return sf.add_(pt6lhs, sf.neg_(pt6rhs))
    def add_(sf, pt6lhs, pt6rhs, /):
        'Pt4EC -> Pt4EC -> Pt4EC | ^FoundNonTrivialFactor | ^FoundTrivialFactor'
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
                        # ^FoundNonTrivialFactor
                        # ^FoundTrivialFactor
                else:
                    slope = hrem6N_((yL-yR)*sf.inv6N_(xL-xR))
                        # ^FoundNonTrivialFactor
                        # ^FoundTrivialFactor
                slope
                # !! [C==0]
                _x = hrem6N_(slope**2 -(xL+xR))
                _y = hrem6N_(-(yL+slope*(_x-xL)))
                pt = sf.mk_point_(_x, _y)
                return pt
        raise TypeError(type(pt6lhs), type(pt6rhs))
    def inv6N_(sf, x, /):
        'x -> x**-1%n | ^FoundNonTrivialFactor | ^FoundTrivialFactor'
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
        '-> (ops4EPC, pt6EPC)|^FoundNonTrivialFactor|TypeError'
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
                d = _d6strict%n
                # [0 <= d < n]
                #bug:if d in b'\0\1\5':raise TypeError(d)#ParamError__ops4EPC7DropY
                #   ^ValueError: byte must be in range(0, 256)
                if d < 6 and d in b'\0\1\5':raise TypeError(d)#ParamError__ops4EPC7DropY
                # [d !<- {0,1,5}]
                # !! [0 <= d < n]
                # [d%n !<- {0,1,5}%n]
            elif 0:
                # !! [n >= 10]
                # [n-6 >= 4 > 0]
                d = 6+random_uint_mod_(-6+n) # randrange(6, n)
                # [0 <= d-6 < n-6]
                # [6 <= d < n]
                # [d !<- {0,1,5}]
                # [d%n !<- {0,1,5}%n]
            else:
                ############
                #since found succ at [detect_square_at_first:=False][n:=11**2]
                #   why:(11, ((121, -24, 54), (38, 13)), 2, (3, 2, 11))
                # try_fix__bug__almost_fail6prime_square_7turnoff_detect_square_at_first:here.1
                ############
                # !! [n >= 10]
                # [n-3 >= 7 > 0]
                d = 2+random_uint_mod_(-3+n) # randrange(2, n-1)
                # [0 <= d-2 < n-3]
                # [2 <= d < n-1]
                if d >= 5:
                    # [5 <= d < n-1]
                    d += 1
                    # [6 <= d < n]
                else:
                    # [2 <= d < 5]
                    pass
                # [d =!= 5][2 <= d < n]
                # [d%n !<- {0,1,5}%n]
            # [d%n !<- {0,1,5}%n]
            d
            d = hrem6N_(d)
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
            # [1 <= x0 < n] # to avoid Incapable__add7h__X6diff_eq0
            if 0:
                # !! [n >= 10]
                # [n-5 >= 5 > 0]
                C = 3+random_uint_mod_(-5+n) # randrange(3, -2+n)
                # [0 <= C-3 < -5+n]
                # [3 <= C < -2+n]
                # [3 <= C <= -3+n]
                # [C%n !<- {-2,+2}%n]
            else:
                ############
                #since found succ at [detect_square_at_first:=False][n:=11**2]
                #   why:(11, ((121, -24, 54), (38, 13)), 2, (3, 2, 11))
                # try_fix__bug__almost_fail6prime_square_7turnoff_detect_square_at_first:here.2
                ############
                # !! [n >= 10]
                # [n-2 >= 8 > 0]
                C = 0+random_uint_mod_(-2+n) # randrange(0, -2+n)
                # [0 <= C < -2+n]
                if C >= 2:
                    # [2 <= C < -2+n]
                    C += 1
                    # [3 <= C < -1+n]
                # [C=!=2][0 <= C < -1+n]
                if C >= n-2:
                    # [n-2 <= C < -1+n]
                    C += 1
                    # [n-1 <= C < n]
                # [C=!=2][C=!=n-2][0 <= C < n]
                # [C%n !<- {-2,+2}%n]
            # [C%n !<- {-2,+2}%n]
            # [(4-C**2)%n =!= 0]or[1 < gcd(n,C+2) < n] # => "not strict"
            N4C, D4C = C, 1
            X0, Z0 = x0, 1
            # [1 <= X0 < n] # to avoid Incapable__add7h__X6diff_eq0
            # (X0,Z0) maybe on EC or twist_EC # => "not strict"
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
        '[pt7sum == pt6lhs <+> pt6rhs] => pt6lhs/Pt4EC7h -> pt6rhs/Pt4EC7h -> pt7sum/Pt4EC7h -> (pt6lhs<+>-pt6rhs)/Pt4EC7h|^Incapable__add7h__X6diff_eq0|^FoundNonTrivialFactor'
        #old:'[pt7sum == pt6lhs <+> pt6rhs] => pt6lhs/Pt4EC7h -> pt6rhs/Pt4EC7h -> pt7sum/Pt4EC7h -> (pt6lhs<+>-pt6rhs)/Pt4EC7h|^Incapable__add7h__X6diff_eq0|^FoundNonTrivialFactor if detect6Incapable'
        return sf.add7h_(pt6lhs, sf.neg_(pt6rhs), pt7sum)
    def add7h_(sf, pt6lhs, pt6rhs, pt7diff, /):
        '[pt7diff == pt6lhs <+> -pt6rhs] => pt6lhs/Pt4EC7h -> pt6rhs/Pt4EC7h -> pt7diff/Pt4EC7h -> (pt6lhs<+>pt6rhs)/Pt4EC7h|^Incapable__add7h__X6diff_eq0|^FoundNonTrivialFactor'
        #old:'[pt7diff == pt6lhs <+> -pt6rhs] => pt6lhs/Pt4EC7h -> pt6rhs/Pt4EC7h -> pt7diff/Pt4EC7h -> (pt6lhs<+>pt6rhs)/Pt4EC7h|^Incapable__add7h__X6diff_eq0|^FoundNonTrivialFactor if detect6Incapable'
        # precondition:[pt7diff == pt6lhs - pt6rhs]
        args4EPC = (n, N4C, D4C) = sf._args
        ctx = (args4EPC, (pt6lhs, pt6rhs, pt7diff))
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
        # [X1*Z2 =!= X2*Z1]

        # [0 =!= pt7diff.Z]
        # [pt7diff =!= O]
        # [pt6lhs =!= O]
        # [pt6rhs =!= O]
        # [pt6lhs =!= +/-pt6rhs]

        if 0 == pt7diff.X:
            # [0 == pt7diff.X]
            # [0 =!= pt7diff.Z]
            ##################
            if 1:
                # patch0001:here
                # [B:=0][A:=1][Xn==0] ==>> [0 == (X1*X2 -Z1*Z2)**2 %n][1 < gcd(n, (X1*X2 -Z1*Z2)) <= n] # ??what about:(X1*Z2 -X2*Z1)
                (X1, Z1) = pt6lhs
                (X2, Z2) = pt6rhs
                _detect_u_(n, ctx, (X1*X2 -Z1*Z2))
                    # ^FoundNonTrivialFactor
                _detect_u_(n, ctx, (X1*Z2 -X2*Z1))
                    # ^FoundNonTrivialFactor
            ##################
            if sf._detect6Incapable:
                ft = gcd(n, pt7diff.Z)
                if 1 < ft < n:
                    raise FoundNonTrivialFactor(n, ft, ctx)
            if 0 == pt7diff.X: raise Incapable__add7h__X6diff_eq0(ctx)
            raise 000
            ##################
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
            # [Xp =?= 0]
            # [Zp =?= 0]
            ##################
            if 1:
                # patch0002:here
                # [B:=0][A:=1][Xp==0] ==>> [0 == Zn*(X1*X2 -Z1*Z2)**2 %n][1 < gcd(n, (X1*X2 -Z1*Z2)) <= n]
                # [B:=0][A:=1][Zp==0] ==>> [0 == Xn*(X1*Z2 -X2*Z1)**2 %n][1 < gcd(n, (X1*Z2 -X2*Z1)) < n]
                if Zp == 0:
                    #_detect_u_(n, ctx, (X1*Z2 -X2*Z1))
                    _detect_u_(n, ctx, xzxz)
                        # ^FoundNonTrivialFactor
                    # !! [X1*Z2 =!= X2*Z1]
                    raise Exception(sf, ctx)
                # [Zp =!= 0]
                if Xp == 0:
                    #_detect_u_(n, ctx, (X1*X2 -Z1*Z2))
                    _detect_u_(n, ctx, xxzz)
                        # ^FoundNonTrivialFactor
                    pass
                # [Xp =?= 0]
                # [Zp =!= 0]
            ##################
            # [Xp =?= 0]
            # [Zp =!= 0]
            ##################
        return sf.mk_point_(Xp, Zp)
    def double7h_(sf, pt, /):
        'pt/Pt4EC7h -> (pt<+>pt)/Pt4EC7h|^FoundNonTrivialFactor'
        #old:'pt/Pt4EC7h -> (pt<+>pt)/Pt4EC7h'
        if pt.eq_zero_():
            return pt7h_O
        # [pt =!= O]
        args4EPC = (n, N4C, D4C) = sf._args
        ctx = (args4EPC, pt)

        # [:define__doubleh]:goto
        # setup:precondition:[P1=!=O][P2=!=O][P1=?=-P2][P1==+P2]:
        (X1, Z1) = P1 = P2 = pt
        # [P1 =!= O]
        # [Z1 =!= 0]
        if X1 == 0:
            # [x1 == X1/Z1 == 0]
            # !! [B:=0]
            # [y1 == 0]
            # [P1 == -P1]
            # [2*P1 == O]
            return pt7h_O
        # [X1 =!= 0]
        # [Z1 =!= 0]
        X1X1 = pow(X1, 2, n)
        Z1Z1 = pow(Z1, 2, n)


        # [0 =?= (X1**3 +C*X1**2*Z1 +A*X1*Z1**2 +B*Z1**3)]
        # !! [B:=0][A:=1]
        # part4Zp = ((X1 +C*Z1)%n *X1X1 +X1*Z1Z1) %n
        # Zp = part4Zp*Z1*4 %n if part4Zp else 0
        # Xp = pow(X1X1 -Z1Z1, 2, n) if Zp else 0
        if X1 == 0:
            D4C_X1 = 0
            D4C_part4Zp = 0
        else:
            D4C_X1 = D4C*X1 %n
            D4C_part4Zp = ((D4C_X1 +N4C*Z1)%n *X1X1 +D4C_X1*Z1Z1) %n

        Zp = D4C_part4Zp*Z1*4 %n if D4C_part4Zp else 0
        Xp = D4C*pow(X1X1 -Z1Z1, 2, n) %n if Zp else 0
        ##################
        if 1:
            # patch0003:here
            # [B:=0] ==>> [X1=!=0]
            # [B:=0][A:=1][Xp==0] ==>> [0 == (X1**2 -Z1**2)**2 %n][1 < gcd(n, X1-Z1) <= n]
            # [Zp =?= 0]
            # !! [Z1 =!= 0]
            # [Zp == 0] => [1 <= gcd(n, Z1) < n]
            if Zp == 0 != D4C_part4Zp:
                _detect_u_(n, ctx, Z1)
                    # ^FoundNonTrivialFactor
                raise Exception(sf, pt)
            # [Zp =?= 0]
            # [Zp == 0] <==> [0 == D4C_part4Zp]
            if Xp == 0:
                _detect_u_(n, ctx, X1-Z1)
                    # ^FoundNonTrivialFactor
                pass
        return sf.mk_point_(Xp, Zp)

    def mul7h_(sf, k, pt, /, *, _old_ver=False):
        # vs:_old_ver__mul7h_
        # vs:bi_mul7h_
        'k/int -> pt/Pt4EC7h -> (k<*>pt)/Pt4EC7h|^Incapable__add7h__X6diff_eq0|^FoundNonTrivialFactor'
        #old:'k/int -> pt/Pt4EC7h -> (k<*>pt)/Pt4EC7h|^Incapable__add7h__X6diff_eq0|^FoundNonTrivialFactor if detect6Incapable'
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
                # ^FoundNonTrivialFactor
                # ^Incapable__add7h__X6diff_eq0
        pt7O
        for _ in range(ez4k):
            pt7O = sf.double7h_(pt7O)
                # ^FoundNonTrivialFactor
        return pt7O

    def bi_mul7h_(sf, k, pt, /, *, only1=False):
        # vs:_old_ver__mul7h_
        # vs:mul7h_
        'k/int -> pt/Pt4EC7h -> (k<*>pt, (k+1)<*>pt)/(Pt4EC7h,Pt4EC7h)|^Incapable__add7h__X6diff_eq0|^FoundNonTrivialFactor'
        #old:'k/int -> pt/Pt4EC7h -> (k<*>pt, (k+1)<*>pt)/(Pt4EC7h,Pt4EC7h)|^Incapable__add7h__X6diff_eq0|^FoundNonTrivialFactor if detect6Incapable'
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












def _mk_ops7force_(M, /):
    j = 0
    while 1:
        j += 1
        try:
            (ops, pt0) = Ops4EllipticPseudocurve.mk_ex5n__7random_(M)
        except FoundNonTrivialFactor as exc:
            print('!!!', j, repr(exc), sep=':')
            continue
        else:
            break
        pass
    return (ops, pt0)

def _setup7force_(p_or_settings4EPC, /):
    match p_or_settings4EPC:
        case ((n, a, b) as args4EPC, xy6EPC):
            M = pp = n
            check_int_ge(5, pp)
            ops = Ops4EllipticPseudocurve(*args4EPC)
            pt0 = ops.mk_point_(*xy6EPC)
            pass
        case p:
            check_int_ge(5, p)
            M = pp = p**2
            (ops, pt0) = _mk_ops7force_(M)
            pass
    M
    r = (M, ops, pt0)
    assert pt0 in ops, r
    return r
def iter_error_pairs4add_table4EPC6square_modulus_(p_or_settings4EPC, /):
    # [:???is_perfect_power_ok__6ECM???]:goto
    (M, ops, pt0) = _setup7force_(p_or_settings4EPC)
    print((ops, pt0))
    pts = [ops.zero]
    for x, y in product(range(M), repeat=2):
        pt = ops.mk_point_(x, y)
        if pt in ops:
            pts.append(pt)
    pts
    sz = len(pts)
    #xxx:assert ops.mul_(len(pts), pts[1]).eq_zero_()
    c0 = c1 = c2 = 0
    for ptA, ptB in product(pts, repeat=2):
        try:
            ptC = ops.add_(ptA, ptB)
        except FoundNonTrivialFactor:
            yield (True, (ptA, ptB))
            c1 += 1
            pass
        except FoundTrivialFactor:
            yield (False, (ptA, ptB))
            c2 += 1
            pass
        else:
            c0 += 1
            pass
        pass
    szsz = sz**2
    r = ((ops, pt0), (sz, szsz), (c0, c1, c2))
    assert szsz == c0+c1+c2, r
    return r






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
        # [:???is_perfect_power_ok__6ECM???]:goto
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



















def _xs5or_B_(xs_or_B, may__xs5B_, default__xs5B_, extra_args7pre, extra_args7post, /):
    match xs_or_B:
        case int() as B:
            xs5B_ = ifNone(may__xs5B_, default__xs5B_)
            xs = xs5B_(*extra_args7pre, B, *extra_args7post)
        case xs:
            pass
    iter(xs)#check iterable
    return xs
def default__dup_exps_from_B1_may_B1pw_(B1, may_B1pw, /):
    # may_max4exp_pow6stage1 --> may_B1pw
    B1pw = ifNone(may_B1pw, B1) # eg: (p+1+floor_sqrt(4*p)) or (floor_sqrt(n)+1+floor_sqrt(4*floor_sqrt(n)))
        # [p is B1-smooth] => [max4exp_pow:=(p+1+floor_sqrt(4*p))]
        # but ... but in practice the cost of doing so is too high for the meager benefit it may provide.
    assert 2 <= B1 <= B1pw
    ps = iter_primes__ge_lt_(2, 1+B1)
    for p in ps:
        ep = floor_log_(p, B1pw)
        yield from repeat(p, ep)
def default__delta_exps_from_B1_B2_(B1, B2, /):
    # B1 --> (B1|B1_at_stage2)
    #   eg: using prev (pt0, B1, pt1, B2) to resume stage2 begin at bigger position: [pt0{curr}:=pt1{prev}][B1{curr}:=2][B1_at_stage2{curr}:=B2{prev}]
    ps = iter_primes__ge_lt_(1+B1, 1+B2)
    _p = 0
    for p in ps:
        yield p - _p
        _p = p
def default__asc_exps_from_B1_B2_(B1, B2, /):
    ps = iter_primes__ge_lt_(1+B1, 1+B2)
    return ps
def iter_deltas5asc_ints_(j0, asc_js, /):
    for j in asc_js:
        d = j-j0
        if not d > 0:raise TypeError(j0, j)
        yield d
        j0 = j

def prepare4factor_pint__elliptic_curve_method_(n_or_settings4EPC, /, *, random_uint_mod_=None, result6fail=None, drop_Y=False, to_raise=False, detect_square_at_first=True, **kwds4mk):
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
    if detect_square_at_first:
        # [:???is_perfect_power_ok__6ECM???]:goto
        #(rt, e) = factor_pint_as_perfect_power_(n)
        rt = isqrt(n)
        if rt**2 == n:
            assert 1 < rt < n
            assert 0 == n%rt
            return (+1, rt, None)
        # [not#is_perfect_square_(n)]

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


# [choose_B1__6ECM]:goto
def batch_iter__7B1_from_p_(ps, /, only_B1=False):
    for p in ps:
        B1 = B1_from_p_(p)
        yield (p, B1) if not only_B1 else B1
def batch_iter__7max_B1_from_n_(ns, /, only_B1=False):
    for n in ns:
        B1 = max_B1_from_n_(n)
        yield (n, B1) if not only_B1 else B1
def B1_from_p_(p, /):
    'p/prime{>3}{#min prime factor for some "n"#} -> B1{#ECM#} # assume [B2:=B1] i.e. ECM7stage1_only'
    check_int_ge(5, p)
    approx_lnP = p.bit_length()
    approx_lnlnP = approx_lnP.bit_length()
    B1 = 1 << isqrt(approx_lnP*approx_lnlnP//2)
    return B1
def max_B1_from_n_(n, /):
    n = max(8, n)
    check_int_ge(8, n)
    # [n >= 8]
    # [n.bit_length() >= 4]
    # [n.bit_length()//2 >= 2]
    approx_sqrtN = 1<<(n.bit_length()//2)
    # [approx_sqrtN >= 4]
    max4min_p4n = 1+approx_sqrtN
    # [max4min_p4n >= 5]
    return B1_from_p_(max4min_p4n)

#DONE:B1_or_dup_exps4stage1 --> (B1_or_dup_exps4stage1|B1_from_n_)
#   howto impl B1_from_n_ # vs B1_from_p_
#       B1_from_n_ --> max_B1_from_n_,iter_B1s_from_n_
#DONE:delta_exps_from_B1_B2_ --> asc_exps_from_B1_B2_
#   B2_or_delta_exps4stage2-->B2_or_asc_exps4stage2
def try1_factor_pint__elliptic_curve_method_(n_or_settings4EPC, may_B1_or_dup_exps4stage1=None, may_B2_or_asc_exps4stage2=None, /, *, random_uint_mod_=None, result6fail=None, detect_square_at_first=False, dup_exps_from_B1_may_B1pw_=None, asc_exps_from_B1_B2_=None, may_B1_at_stage2=None, may_B1pw_at_stage1=None, B1_from_n_=None, default_scale4B2=100):
    # detect_square_at_first=True-->False
    '-> (((result6fail|ft), may_exc_or_ctx) | (ft, settings4EPC, stage, ((j4exp, zmay_q1{==max_exp6stage1}) if stage==1 else (max_exp6stage1, j4delta, zmay_q2{==max_exp6stage2}))))'
    #TODO:++kw:drop_Y/inversionless#Ops4EllipticPseudocurve7DropY
    #vs:try1_factor_pint__elliptic_curve_method7inversionless_
    ###########################
    match prepare4factor_pint__elliptic_curve_method_(n_or_settings4EPC, random_uint_mod_=random_uint_mod_, result6fail=result6fail, detect_square_at_first=detect_square_at_first, drop_Y=False):
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
        B1_or_dup_exps4stage1 = ifNonef(may_B1_or_dup_exps4stage1, lambda:ifNone(B1_from_n_, default__B1_from_n_)(n))
        may_B1pw = may_B1pw_at_stage1
        dup_exps4stage1 = _xs5or_B_(B1_or_dup_exps4stage1, dup_exps_from_B1_may_B1pw_, default__dup_exps_from_B1_may_B1pw_, [], [may_B1pw])
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
        #old:delta_exps4stage2 = _xs5or_B_(B2_or_delta_exps4stage2, delta_exps_from_B1_B2_, default__delta_exps_from_B1_B2_, B1)
        B2_or_asc_exps4stage2 = ifNonef(may_B2_or_asc_exps4stage2, lambda:B1*default_scale4B2)
        B1_at_stage2 = ifNone(may_B1_at_stage2, B1)
        asc_exps4stage2 = _xs5or_B_(B2_or_asc_exps4stage2, asc_exps_from_B1_B2_, default__asc_exps_from_B1_B2_, [B1_at_stage2], [])
        delta_exps4stage2 = iter_deltas5asc_ints_(0, asc_exps4stage2)
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
    return (result6fail, (ctx, (B1, B2, pt1, pt2)))
    return (result6fail, ctx)
#end-def try1_factor_pint__elliptic_curve_method_(n_or_settings4EPC, B1_or_dup_exps4stage1, may_B2_or_asc_exps4stage2, /, *, random_uint_mod_=None, result6fail=None, detect_square_at_first=True, dup_exps_from_B1_may_B1pw_=None, asc_exps_from_B1_B2_=None):
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
def default__B1_from_n_(n, /):
    return min(10000, max_B1_from_n_(n))
def prepare4criteria4ECM7inversionless_(n, may_B1, may_B2, may_max4big_step, /, *, B1_from_n_=None, default_scale4B2=100, default_max4big_step=1<<16):
    # default_B1=10000 --> B1_from_n_=None
    #B1 = ifNone(may_B1, default_B1)
    B1 = ifNonef(may_B1, lambda:ifNone(B1_from_n_, default__B1_from_n_)(n))
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
def try1_factor_pint__elliptic_curve_method7inversionless_(n_or_settings4EPC, may_B1=None, may_B2=None, may_max4big_step=None, /, *, random_uint_mod_=None, result6fail=None, detect_square_at_first=True, dup_exps_from_B1_may_B1pw_=None, asc_exps_from_B1_B2_=None, default_scale4B2=100, default_max4big_step=1<<16, imay_period4detect=0, may_B1_at_stage2=None, may_B1pw_at_stage1=None, B1_from_n_=None, strict=False):
    # default_B1=10000 --> B1_from_n_=None
    # default:strict=False instead True
    '-> (((result6fail|ft), may_exc_or_ctx) | (ft, settings4EPC, stage, ((j4exp, zmay_q1{==max_exp6stage1}) if stage==1 else (max_exp6stage1, j4delta, zmay_q2{==max_exp6stage2}))))'
    #TODO:++kw:drop_Y/inversionless#Ops4EllipticPseudocurve7DropY
    #vs:try1_factor_pint__elliptic_curve_method_
    ###########################
    match prepare4factor_pint__elliptic_curve_method_(n_or_settings4EPC, random_uint_mod_=random_uint_mod_, result6fail=result6fail, detect_square_at_first=detect_square_at_first, drop_Y=True, strict=strict, detect6Incapable=True):
        # default:strict=False instead True
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
    (B1, B2, big_step) = prepare4criteria4ECM7inversionless_(n, may_B1, may_B2, may_max4big_step, B1_from_n_=B1_from_n_, default_scale4B2=default_scale4B2, default_max4big_step=default_max4big_step)
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
    mk_iter4detect_ = _4imay_period4detect(n, imay_period4detect)
    pt0 = pt6EPC
    zmay_q1 = 0
    zmay_q2 = 0
    try:
        #########
        mul7h_ = ops4EPC.mul7h_
        may_B1pw = may_B1pw_at_stage1
        dup_exps4stage1 = _xs5or_B_(B1, dup_exps_from_B1_may_B1pw_, default__dup_exps_from_B1_may_B1pw_, [], [may_B1pw])
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
                _detect_pt_(n, ctx, _pt7pre)
                    # ^FoundNonTrivialFactor
                return (result6fail, (ctx, '@stage1...', (_pt7pre, exp)))
            if _pt.X == 0:
                # detect_X6stage1:here
                # [_pt.x == 0]
                # !! [B:=0]
                # [g? * _pt.y**2 == (...)*_pt.x == 0]
                # [_pt.y == 0]
                _detect_pt_(n, ctx, _pt7pre)
                    # ^FoundNonTrivialFactor
                return (result6fail, (ctx, '@stage1:...[X==0]', (_pt7pre, exp, _pt)))
            if next(iter4detect):
                _detect_pt_(n, ctx, _pt7pre)
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
        _detect_pt_(n, ctx, pt1)
            # ^FoundNonTrivialFactor
        # [not pt1.eq_partial_zero_mod_()]
        #########
        #max4delta6cache = D

        add7h_ = ops4EPC.add7h_
        #old:delta_exps4stage2 = _xs5or_B_(B2, delta_exps_from_B1_B2_, default__delta_exps_from_B1_B2_, B1)
        B1_at_stage2 = ifNone(may_B1_at_stage2, B1)
        asc_exps4stage2 = _xs5or_B_(B2, asc_exps_from_B1_B2_, default__asc_exps_from_B1_B2_, [B1_at_stage2], [])
        delta_exps4stage2 = iter_deltas5asc_ints_(0, asc_exps4stage2)
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
            ##################
            #detect6cache:here
            z_pt1 = ops4EPC.double7h_(pt1)
                # ^FoundNonTrivialFactor
            if z_pt1.eq_zero_():
                # [2<*>pt1 == O]
                # !! [pt1 =!= O]
                # [2 == order_(EC;pt1)]
                # [pt1.?y? == 0]
                return (result6fail, (ctx, '@stage2.begin:@init-cache.begin...:[2<*>pt1 == O]', (2, pt1)))
            # [z_pt1 =!= O]
            cache = [pt7h_O, z_pt1]
            for j in range(2, 1+D):
                # [cache[-1] is cache[j-1] =!= O]
                cache.append(add7h_(cache[-1], z_pt1, cache[-2]))
                    # ^Incapable__add7h__X6diff_eq0
                    # ^FoundNonTrivialFactor
                # [cache[-1] is cache[j] == 2*j<*>pt1]
                if cache[-1].eq_zero_():
                    # [O == 2*j<*>pt1]
                    # [0 == 2*j%order_(EC;pt1)]
                    _detect_pt_(n, ctx, cache[-2])
                        # ^FoundNonTrivialFactor
                    return (result6fail, (ctx, '@stage2.begin:@init-cache...:[2*j<*>pt1 == O]', (2*j, pt1, cache[-2])))
                # [cache[-1] is cache[j] == O]
            cache
            # [[j:<-[0..=D]] -> [cache[j] == 2*j<*>pt1]]
            # [[j:<-[1..=D]] -> [O =!= cache[j] == 2*j<*>pt1]]
            #end-detect6cache
            ##################
            j2XZ6cache = [pt.mul_X_Z_mod_(n) for pt in cache]
            777;cache[0] = None
            777;j2XZ6cache[0] = None
            ##################

            pt8big_step = cache[D]
            # !! [2*D == big_step]
            # [pt8big_step == big_step<*>pt1]

            k4ref = q-2
            # !! [2 <= big_step]
            # [(q-k4ref) == 2 <= big_step]
            # [0 == (q-k4ref)%2][2 <= (q-k4ref) <= big_step]

            pt7ref = mul7h_(k4ref, pt1)
                # ^FoundNonTrivialFactor
            pt7ref7pre = mul7h_(k4ref-big_step, pt1)
                # ^FoundNonTrivialFactor
            777;XZ4ref = pt7ref.mul_X_Z_mod_(n)
            # [pt7ref == k4ref<*>pt1]
            # [pt7ref7pre == (k4ref-big_step)<*>pt1]
            # [0 == (q-k4ref)%2][2 <= (q-k4ref) <= big_step]
            j4small_step = (q-k4ref)>>1
            pt8small_step = cache[j4small_step]
            777;XZ4small_step = j2XZ6cache[j4small_step]
            diff = _diff7h7mod_(n, pt7ref, pt8small_step, XZ4ref, XZ4small_step)
            #diff = pt7ref.diff7h7mod_(n, pt8small_step)
            IIdiffs = diff
            if 0 == IIdiffs:
                assert diff == 0, ctx
                if 0 and not detect_square_at_first:
                    _detect_pt_(n, ctx, pt7ref)
                        # ^FoundNonTrivialFactor
                if 0 and pt8small_step.eq_zero_() and not detect_square_at_first:
                    _detect_pt_(n, ctx, pt7ref)
                        # ^FoundNonTrivialFactor
                return (result6fail, (ctx, '@stage2.begin...', (k4ref, q, pt7ref, pt8small_step)))
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
                777;XZ4ref = pt7ref.mul_X_Z_mod_(n)
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
            j4small_step = (q-k4ref)>>1
            pt8small_step = cache[j4small_step]
            777;XZ4small_step = j2XZ6cache[j4small_step]
            diff = _diff7h7mod_(n, pt7ref, pt8small_step, XZ4ref, XZ4small_step)
            #diff = pt7ref.diff7h7mod_(n, pt8small_step)
            IIdiffs7pre = IIdiffs
            # !! [0 =!= IIdiffs %n]
            # [0 =!= IIdiffs7pre %n]
            IIdiffs = diff*IIdiffs %n
            if 0 == IIdiffs:
                # !! MAYBE:[0 == diff%n]
                #_detect_u_(n, ctx, diff)
                    # ^FoundNonTrivialFactor
                # !! [0 =!= IIdiffs7pre %n]
                _detect_u_(n, ctx, IIdiffs7pre)
                    # ^FoundNonTrivialFactor
                assert diff == 0, ctx
                if 0 and not detect_square_at_first:
                    _detect_pt_(n, ctx, pt7ref)
                        # ^FoundNonTrivialFactor
                return (result6fail, (ctx, '@stage2...', (k4ref, q, pt7ref, pt8small_step)))
            # [0 =!= IIdiffs %n]
            if next(iter4detect):
                _detect_u_(n, ctx, IIdiffs)
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
        _detect_u_(n, ctx, IIdiffs)
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
    return (result6fail, (ctx, (B1, B2, pt1, pt2)))
    return (result6fail, ctx)
#end-def try1_factor_pint__elliptic_curve_method7inversionless_(n_or_settings4EPC, may_B1=None, may_B2=None, may_max4big_step=None, /, *, random_uint_mod_=None, result6fail=None, detect_square_at_first=True, dup_exps_from_B1_may_B1pw_=None, asc_exps_from_B1_B2_=None, default_B1=10000, default_scale4B2=100, default_max4big_step=1<<16, imay_period4detect=0):
def _diff7h7mod_(n, pt7ref, pt8small_step, XZ4ref, XZ4small_step, /):
    '-> (pt7ref.X*pt8small_step.Z -pt8small_step.X*pt7ref.Z)%n'
    #diff = pt7ref.diff7h7mod_(n, pt8small_step)
    (Xr, Zr) = pt7ref
    (Xm, Zm) = pt8small_step
    diff = ((Xr-Xm)*(Zr+Zm) -XZ4ref +XZ4small_step) %n
    return diff

###########################
#########
def _detect_pt_(n, ctx, pt1, /):
    '-> None|^FoundNonTrivialFactor'
    # [pt1 =!= O]
    ft = gcd(n, pt1.Z)
    if 1 < ft < n:
        raise FoundNonTrivialFactor(n, ft, ctx)
    # !! [pt1 =!= O]
    # [ft =!= n]
    assert ft == 1, ctx# settings4EPC
    # [not pt1.eq_partial_zero_mod_()]
#########
def _detect_u_(n, ctx, u, /):
    '-> None|^FoundNonTrivialFactor'
    ft = gcd(n, u)
    if 1 < ft < n:
        raise FoundNonTrivialFactor(n, ft, ctx)
#########

###########################




def _count_succ_ratio_(total, tag:'7inversionless', /, *args, **kwds):
    match tag:
        case '7inversionless':
            f = try1_factor_pint__elliptic_curve_method7inversionless_
        case 'no:7inversionless':
            f = try1_factor_pint__elliptic_curve_method_
        case _:
            raise TypeError('should be: "7inversionless","no:7inversionless"', tag)
    f
    g = lambda:f(*args, **kwds)

    c7fail = c7ok = 0
    for j in range(total):
        r = g()
        match r:
            case (None, *_):
                c7fail += 1
            case (int() as ft, *_):
                c7ok += 1
            case bad:
                raise Exception(bad)

    c7fail, c7ok
    assert c7fail+c7ok == total
    return (total, c7fail, c7ok)














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
#def try1_factor_pint__elliptic_curve_method_(n_or_settings4EPC, may_B1_or_dup_exps4stage1=None, may_B2_or_asc_exps4stage2=None, /, *, random_uint_mod_=None, result6fail=None, detect_square_at_first=False, dup_exps_from_B1_may_B1pw_=None, asc_exps_from_B1_B2_=None, may_B1_at_stage2=None, may_B1pw_at_stage1=None, B1_from_n_=None, default_scale4B2=100):
#   '-> (((result6fail|ft), may_exc_or_ctx) | (ft, settings4EPC, stage, ((j4exp, zmay_q1{==max_exp6stage1}) if stage==1 else (max_exp6stage1, j4delta, zmay_q2{==max_exp6stage2}))))'
#def prepare4factor_pint__elliptic_curve_method_(n_or_settings4EPC, /, *, random_uint_mod_=None, result6fail=None, drop_Y=False, to_raise=False, detect_square_at_first=True, **kwds4mk):
#   '-> ((-1, result6fail, may_exc)|(+1, non_trivial_factor, may_exc)|(0, (n{[1 == gcd(n, 6)][n >= 25]}, settings4EPC, (ops4EPC/T, pt)))) | ^FoundFactor if to_raise | ^ParamError__ops4EPC7DropY if to_raise and drop_Y # [T := Ops4EllipticPseudocurve if not drop_Y else Ops4EllipticPseudocurve7DropY]'
#   not$drop_Y => [settings4EPC == (args4EPC, xy6EPC) :: ((n,a,b),(x,y))]
#   drop_Y => [settings4EPC == (args4EPC, XZ6EPC) :: ((n,N4C,D4C),(X,Z))]



from seed.math.factor_pint.factor_pint__elliptic_curve_method import try1_factor_pint__elliptic_curve_method7inversionless_
#def try1_factor_pint__elliptic_curve_method7inversionless_(n_or_settings4EPC, may_B1=None, may_B2=None, may_max4big_step=None, /, *, random_uint_mod_=None, result6fail=None, detect_square_at_first=True, dup_exps_from_B1_may_B1pw_=None, asc_exps_from_B1_B2_=None, default_scale4B2=100, default_max4big_step=1<<16, imay_period4detect=0, may_B1_at_stage2=None, may_B1pw_at_stage1=None, B1_from_n_=None, strict=False):
#   '-> (((result6fail|ft), may_exc_or_ctx) | (ft, settings4EPC, stage, ((j4exp, zmay_q1{==max_exp6stage1}) if stage==1 else (max_exp6stage1, j4delta, zmay_q2{==max_exp6stage2}))))'
#   [settings4EPC == (args4EPC, XZ6EPC) :: ((n,N4C,D4C),(X,Z))]

from seed.math.factor_pint.factor_pint__elliptic_curve_method import B1_from_p_

from seed.math.factor_pint.factor_pint__elliptic_curve_method import *
