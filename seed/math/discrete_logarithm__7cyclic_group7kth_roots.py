#__all__:goto
# [formula__kth_roots4unity7cyclic_group_]:goto
# [criterion__has_kth_roots7cyclic_group_]:goto
# [formula__kth_roots7cyclic_group7convert_to_strict_]:goto
# [formula__kth_roots7cyclic_group7strict_]:goto
#   [formula__kth_roots7cyclic_group7strict__7semi_tight_order4base_]:goto
# [formula__calc_partial_discrete_logarithm_]:goto
# [formula__calc_mul_order7cyclic_group_]:goto
r'''[[[
e ../../python3_src/seed/math/discrete_logarithm__7cyclic_group7kth_roots.py
see also:
    view ../../python3_src/seed/math/discrete_logarithm.py
    view ../../python3_src/seed/math/sqrts_mod_.py
    view ../../python3_src/seed/math/factor_pint/perfect_power/lift_neg_kth_root_mod_coprime_power_.py
    view ../../python3_src/seed/math/factor_pint/perfect_power/detect_perfect_power.py
    view ../../python3_src/seed/math/floor_ceil_tools/fc_perfect.py



seed.math.discrete_logarithm__7cyclic_group7kth_roots
py -m nn_ns.app.debug_cmd   seed.math.discrete_logarithm__7cyclic_group7kth_roots -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.discrete_logarithm__7cyclic_group7kth_roots:__doc__ -ht # -ff -df
#######

[[
to impl kth_roots_of() @cyclic_group

view ../../python3_src/seed/math/discrete_logarithm.py
view ../../python3_src/seed/algo/baby_steps_giant_steps_method.py
]]


'#'; __doc__ = r'#'
>>> M = 1+360*5557
>>> M == 1 +2**3 *3**2 *5 *5557
True
>>> M
2000521

>>> ops = GroupOps7discrete_logarithm7kth_root__7uint_mod(M)
>>> ops
GroupOps7discrete_logarithm7kth_root__7uint_mod(2000521)

znprimroot(2000521) -> Mod(7,2000521)
Mod(7,2000521)^333333 -> Mod(1046135,2000521)
Mod(7,2000521)^-1 -> Mod(1143155,2000521)



    mul_order_of__7cyclic_group7baby_steps_giant_steps_method_
    mul_order_of__7cyclic_group7slack_order4base_is_prime_power_
    mul_order_of__7cyclic_group7factorization4slack_order4base_

def mul_order_of__7cyclic_group7baby_steps_giant_steps_method_(sf, max4tight_order4base, pt7base, /):
>>> ops.mul_order_of__7cyclic_group7baby_steps_giant_steps_method_(2000520, 7)
2000520
>>> ops.mul_order_of__7cyclic_group7baby_steps_giant_steps_method_(2000520, 49)
1000260


def mul_order_of__7cyclic_group7slack_order4base_is_prime_power_(sf, p, ep, slack_order4base, pt7base, /, *, to_log_p_mul_order=False):
>>> def test1(M, g, p, ep, /):
...     tight_order4base = p**ep
...     pt7base = ops.pow_(g, perfect_div(M-1, tight_order4base))
...     for e in range(1, 1+tight_order4base):
...         pt7tgt = ops.pow_(pt7base, e)
...         _o = ops.mul_order_of__7cyclic_group7slack_order4base_is_prime_power_(p, ep, tight_order4base, pt7tgt)
...         _log_p_o = ops.mul_order_of__7cyclic_group7slack_order4base_is_prime_power_(p, ep, tight_order4base, pt7tgt, to_log_p_mul_order=True)
...         o = tight_order4base//gcd(e,tight_order4base)
...         assert o == _o, (tight_order4base, e, _o, o)
...         assert p**_log_p_o == _o, (tight_order4base, e, _o, o)
...         print(e, _o, _log_p_o, sep=':')
>>> test1(M:=2000521, g:=7, p:=2, ep:=3)
1:8:3
2:4:2
3:8:3
4:2:1
5:8:3
6:4:2
7:8:3
8:1:0
>>> test1(M:=2000521, g:=7, p:=3, ep:=2)
1:9:2
2:9:2
3:3:1
4:9:2
5:9:2
6:3:1
7:9:2
8:9:2
9:1:0
>>> test1(M:=2000521, g:=7, p:=5, ep:=1)
1:5:1
2:5:1
3:5:1
4:5:1
5:1:0




def mul_order_of__7cyclic_group7factorization4slack_order4base_(sf, factorization4slack_order4base, slack_order4base, pt7base, /, *, to_factorization4mul_order=False):
>>> pt7base = 7
>>> tight_order4base = M-1
>>> factorization4tight_order4base = {2:3, 3:2, 5:1, 5557:1}
>>> part0_4exp = 100003
>>> 1 == gcd(tight_order4base, part0_4exp)
True
>>> pt7radix = ops.pow_(pt7base, part0_4exp)
>>> from seed.math.all_factors_of_ import sorted_all_factors5factorization_, iter_unsorted_all_factors5factorization_
>>> ts = [(part4exp, p2e4part4exp, ops.pow_(pt7radix, part4exp)) for part4exp, p2e4part4exp in iter_unsorted_all_factors5factorization_(factorization4tight_order4base, with_factorization=True)]
>>> len(ts)
48
>>> len(ts) == (1+3)*(1+2)*(1+1)*(1+1) == 4*3*2*2 == 48
True
>>> ts == (
... [(1, {}, 195131)
... , (5557, {5557: 1}, 544845)
... , (5, {5: 1}, 1034882)
... , (27785, {5: 1, 5557: 1}, 1706828)
... , (3, {3: 1}, 72141)
... , (16671, {3: 1, 5557: 1}, 383399)
... , (15, {3: 1, 5: 1}, 387277)
... , (83355, {3: 1, 5: 1, 5557: 1}, 494535)
... , (9, {3: 2}, 1114546)
... , (50013, {3: 2, 5557: 1}, 343793)
... , (45, {3: 2, 5: 1}, 1657483)
... , (250065, {3: 2, 5: 1, 5557: 1}, 527215)
... , (2, {2: 1}, 190968)
... , (11114, {2: 1, 5557: 1}, 763356)
... , (10, {2: 1, 5: 1}, 1836574)
... , (55570, {2: 1, 5: 1, 5557: 1}, 1114813)
... , (6, {2: 1, 3: 1}, 968760)
... , (33342, {2: 1, 3: 1, 5557: 1}, 511163)
... , (30, {2: 1, 3: 1, 5: 1}, 414317)
... , (166710, {2: 1, 3: 1, 5: 1, 5557: 1}, 1173975)
... , (18, {2: 1, 3: 2}, 1274292)
... , (100026, {2: 1, 3: 2, 5557: 1}, 845648)
... , (90, {2: 1, 3: 2, 5: 1}, 423182)
... , (500130, {2: 1, 3: 2, 5: 1, 5557: 1}, 1267964)
... , (4, {2: 2}, 1279715)
... , (22228, {2: 2, 5557: 1}, 625856)
... , (20, {2: 2, 5: 1}, 1619174)
... , (111140, {2: 2, 5: 1, 5557: 1}, 357887)
... , (12, {2: 2, 3: 1}, 1523475)
... , (66684, {2: 2, 3: 1, 5557: 1}, 1565280)
... , (60, {2: 2, 3: 1, 5: 1}, 1871563)
... , (333420, {2: 2, 3: 1, 5: 1, 5557: 1}, 368616)
... , (36, {2: 2, 3: 2}, 1206606)
... , (200052, {2: 2, 3: 2, 5557: 1}, 299597)
... , (180, {2: 2, 3: 2, 5: 1}, 366246)
... , (1000260, {2: 2, 3: 2, 5: 1, 5557: 1}, 2000520)
... , (8, {2: 3}, 1979684)
... , (44456, {2: 3, 5557: 1}, 1723020)
... , (40, {2: 3, 5: 1}, 1661356)
... , (222280, {2: 3, 5: 1, 5557: 1}, 1748265)
... , (24, {2: 3, 3: 1}, 1619240)
... , (133368, {2: 3, 3: 1, 5557: 1}, 1393549)
... , (120, {2: 3, 3: 1, 5: 1}, 1835212)
... , (666840, {2: 3, 3: 1, 5: 1, 5557: 1}, 368615)
... , (72, {2: 3, 3: 2}, 876797)
... , (400104, {2: 3, 3: 2, 5557: 1}, 986702)
... , (360, {2: 3, 3: 2, 5: 1}, 1199466)
... , (2000520, {2: 3, 3: 2, 5: 1, 5557: 1}, 1)
... ])
True
>>> for (part4exp, p2e4part4exp, pt7tgt) in ts:
...     tight_order4tgt = ops.mul_order_of__7cyclic_group7factorization4slack_order4base_(factorization4tight_order4base, tight_order4base, pt7tgt)
...     assert tight_order4tgt*part4exp == tight_order4base
...     p2e4tight_order4tgt = ops.mul_order_of__7cyclic_group7factorization4slack_order4base_(factorization4tight_order4base, tight_order4base, pt7tgt, to_factorization4mul_order=True)
...     assert II__p2e_(p2e4tight_order4tgt) == tight_order4tgt
...     print(pt7tgt, part4exp, tight_order4tgt, sorted(p2e4tight_order4tgt.items()), sep=':')
195131:1:2000520:[(2, 3), (3, 2), (5, 1), (5557, 1)]
544845:5557:360:[(2, 3), (3, 2), (5, 1)]
1034882:5:400104:[(2, 3), (3, 2), (5557, 1)]
1706828:27785:72:[(2, 3), (3, 2)]
72141:3:666840:[(2, 3), (3, 1), (5, 1), (5557, 1)]
383399:16671:120:[(2, 3), (3, 1), (5, 1)]
387277:15:133368:[(2, 3), (3, 1), (5557, 1)]
494535:83355:24:[(2, 3), (3, 1)]
1114546:9:222280:[(2, 3), (5, 1), (5557, 1)]
343793:50013:40:[(2, 3), (5, 1)]
1657483:45:44456:[(2, 3), (5557, 1)]
527215:250065:8:[(2, 3)]
190968:2:1000260:[(2, 2), (3, 2), (5, 1), (5557, 1)]
763356:11114:180:[(2, 2), (3, 2), (5, 1)]
1836574:10:200052:[(2, 2), (3, 2), (5557, 1)]
1114813:55570:36:[(2, 2), (3, 2)]
968760:6:333420:[(2, 2), (3, 1), (5, 1), (5557, 1)]
511163:33342:60:[(2, 2), (3, 1), (5, 1)]
414317:30:66684:[(2, 2), (3, 1), (5557, 1)]
1173975:166710:12:[(2, 2), (3, 1)]
1274292:18:111140:[(2, 2), (5, 1), (5557, 1)]
845648:100026:20:[(2, 2), (5, 1)]
423182:90:22228:[(2, 2), (5557, 1)]
1267964:500130:4:[(2, 2)]
1279715:4:500130:[(2, 1), (3, 2), (5, 1), (5557, 1)]
625856:22228:90:[(2, 1), (3, 2), (5, 1)]
1619174:20:100026:[(2, 1), (3, 2), (5557, 1)]
357887:111140:18:[(2, 1), (3, 2)]
1523475:12:166710:[(2, 1), (3, 1), (5, 1), (5557, 1)]
1565280:66684:30:[(2, 1), (3, 1), (5, 1)]
1871563:60:33342:[(2, 1), (3, 1), (5557, 1)]
368616:333420:6:[(2, 1), (3, 1)]
1206606:36:55570:[(2, 1), (5, 1), (5557, 1)]
299597:200052:10:[(2, 1), (5, 1)]
366246:180:11114:[(2, 1), (5557, 1)]
2000520:1000260:2:[(2, 1)]
1979684:8:250065:[(3, 2), (5, 1), (5557, 1)]
1723020:44456:45:[(3, 2), (5, 1)]
1661356:40:50013:[(3, 2), (5557, 1)]
1748265:222280:9:[(3, 2)]
1619240:24:83355:[(3, 1), (5, 1), (5557, 1)]
1393549:133368:15:[(3, 1), (5, 1)]
1835212:120:16671:[(3, 1), (5557, 1)]
368615:666840:3:[(3, 1)]
876797:72:27785:[(5, 1), (5557, 1)]
986702:400104:5:[(5, 1)]
1199466:360:5557:[(5557, 1)]
1:2000520:1:[]













    discrete_logarithm__7cyclic_group7baby_steps_giant_steps_method_
    discrete_logarithm__7cyclic_group7tight_order4base_is_prime_
    discrete_logarithm__7cyclic_group7tight_order4base_is_prime_power_
    discrete_logarithm__7cyclic_group7factorization4tight_order4base_
    partial_discrete_logarithm__7cyclic_group7factorization4part4tight_order4base_

def discrete_logarithm__7cyclic_group7baby_steps_giant_steps_method_(sf, max4exp, pt7base, pt7tgt, /, *, max4exp__vs__tight_order4base:bool):
>>> for (part4exp, p2e4part4exp, pt7tgt) in ts:
...     exp0 = part0_4exp*part4exp%tight_order4base
...     exp0 = exp0 if not 0 == exp0 else tight_order4base
...     if 0b001:
...         exp1 = ops.discrete_logarithm__7cyclic_group7baby_steps_giant_steps_method_(max4exp:=part4exp*part0_4exp, pt7base, pt7tgt, max4exp__vs__tight_order4base=False)
...         assert exp1 == exp0, (1, exp0, exp1)
...     if 0:
...         exp2 = ops.discrete_logarithm__7cyclic_group7baby_steps_giant_steps_method_(max4exp:=tight_order4base, pt7base, pt7tgt, max4exp__vs__tight_order4base=True) #doctest: +SKIP
...         assert exp2 == exp0, (2, exp0, exp2) #doctest: +SKIP
...     if part4exp == tight_order4base:
...         exp2 = ops.discrete_logarithm__7cyclic_group7baby_steps_giant_steps_method_(max4exp:=tight_order4base, pt7base, pt7tgt, max4exp__vs__tight_order4base=True)
...         assert exp2 == exp0, (2, exp0, exp2)
...     #print(pt7tgt, exp, sep=':')




def discrete_logarithm__7cyclic_group7tight_order4base_is_prime_(sf, tight_order4base, pt7base, pt7tgt, /):
>>> ls4p_pt = [(p, ops.pow_(pt7base, tight_order4base//p)) for p in factorization4tight_order4base]
>>> for p, pt in ls4p_pt:
...     pt7tgt = ops.pow_(pt, part0_4exp)
...     exp0 = part0_4exp%p
...     exp0 = exp0 if not 0 == exp0 else p
...     exp1 = ops.discrete_logarithm__7cyclic_group7tight_order4base_is_prime_(p, pt, pt7tgt)
...     assert exp1 == exp0, (1, exp0, exp1, p)






def discrete_logarithm__7cyclic_group7tight_order4base_is_prime_power_(sf, p, ep, tight_order4base, pt7base, pt7tgt, /):
>>> ls4p_e_pt = [(p, ep, ops.pow_(pt7base, tight_order4base//p**ep)) for p, ep in factorization4tight_order4base.items() if ep >= 2]
>>> for p, ep, pt in ls4p_e_pt:
...     pw = p**ep
...     for exp0 in range(1, 1+pw):
...         pt7tgt = ops.pow_(pt, exp0)
...         exp1 = ops.discrete_logarithm__7cyclic_group7tight_order4base_is_prime_power_(p, ep, pw, pt, pt7tgt)
...         assert exp1 == exp0, (1, exp0, exp1, p, ep)







def discrete_logarithm__7cyclic_group7factorization4tight_order4base_(sf, factorization4tight_order4base, tight_order4base, pt7base, pt7tgt, /):
>>> for (part4exp, p2e4part4exp, pt7tgt) in ts:
...     exp0 = part0_4exp*part4exp%tight_order4base
...     exp0 = exp0 if not 0 == exp0 else tight_order4base
...     if 0b001:
...         exp1 = ops.discrete_logarithm__7cyclic_group7factorization4tight_order4base_(factorization4tight_order4base, tight_order4base, pt7base, pt7tgt)
...         assert exp1 == exp0, (1, exp0, exp1, part4exp, p2e4part4exp)
...     #print(pt7tgt, exp, sep=':')










def partial_discrete_logarithm__7cyclic_group7factorization4part4tight_order4base_(sf, factorization4t, t, tight_order4base, pt7base, pt7tgt, /):
>>> ls4t_p2e4t = [(t, complete_factor_pint_via_trial_division(factorization4tight_order4base, t)) for t in iter_unsorted_all_factors5factorization_({p**ep:1 for p, ep in factorization4tight_order4base.items()})]
>>> ls4t_p2e4t == [(1, {}), (5557, {5557: 1}), (9, {3: 2}), (50013, {3: 2, 5557: 1}), (8, {2: 3}), (44456, {2: 3, 5557: 1}), (72, {2: 3, 3: 2}), (400104, {2: 3, 3: 2, 5557: 1}), (5, {5: 1}), (27785, {5: 1, 5557: 1}), (45, {3: 2, 5: 1}), (250065, {3: 2, 5: 1, 5557: 1}), (40, {2: 3, 5: 1}), (222280, {2: 3, 5: 1, 5557: 1}), (360, {2: 3, 3: 2, 5: 1}), (2000520, {2: 3, 3: 2, 5: 1, 5557: 1})]
True
>>> for (part4exp, p2e4part4exp, pt7tgt) in ts:
...     exp0 = part0_4exp*part4exp%tight_order4base
...     exp0 = exp0 if not 0 == exp0 else tight_order4base
...     if 0b001:
...         for t, factorization4t in ls4t_p2e4t:
...             _exp6t = exp0%t
...             _exp6t = _exp6t if not 0 == _exp6t else t
...             exp6t = ops.partial_discrete_logarithm__7cyclic_group7factorization4part4tight_order4base_(factorization4t, t, tight_order4base, pt7base, pt7tgt)
...             assert exp6t == _exp6t, (1, exp6t, _exp6t, part4exp, p2e4part4exp, t, factorization4t)
...     #print(pt7tgt, exp, sep=':')





    repr_kth_roots4unity7cyclic_group_
    repr_kth_roots7cyclic_group_
    repr_kth_roots7cyclic_group__7slack_order4base_pow_
    repr_kth_roots7cyclic_group__7low_level_

def repr_kth_roots4unity7cyclic_group_(sf, k, tight_order4base, pt7base, /, *, validate=False):
>>> for (part4exp, p2e4part4exp, pt7tgt) in ts:
...     k = part0_4exp*part4exp
...     if 0b001:
...         (pt7root, sz, pows_repr) = ops.repr_kth_roots4unity7cyclic_group_(k, tight_order4base, pt7base, validate=True)
...         assert sz == part4exp, (1, k, sz, part4exp, p2e4part4exp)
...     #print(pt7tgt, exp, sep=':')






def repr_kth_roots7cyclic_group_(sf, factorization4gcd_k_tight_order4base, gcd_k_tight_order4base, k, tight_order4base, pt7base, pt7tgt, /):
>>> for (part4exp, p2e4part4exp, _0_pt7tgt) in ts:
...     a = perfect_div(tight_order4base, part4exp)
...     k = part0_4exp*a
...     gcd_k_tight_order4base = a
...     factorization4gcd_k_tight_order4base = complete_factor_pint_via_trial_division(factorization4tight_order4base, gcd_k_tight_order4base)
...     if 0b001:
...         #_1_pt7tgt = ops.pow_(pt7base, k)
...         _1_pt7tgt = ops.pow_(pt7radix, a)
...         for b in iter_unsorted_all_factors5factorization_(p2e4part4exp):
...             pt7tgt = ops.pow_(_1_pt7tgt, b)
...             (pt7root, ((pt7tgt, e4tgt), (pt7base_pow, e4base_pow))) = ops.repr_kth_roots7cyclic_group_(factorization4gcd_k_tight_order4base, gcd_k_tight_order4base, k, tight_order4base, pt7base, pt7tgt)
...             assert ops.eq_(pt7tgt, ops.pow_(pt7root, k))
...     #print(pt7tgt, exp, sep=':')






def repr_kth_roots7cyclic_group__7slack_order4base_pow_(sf, factorization4gcd_k_slack_order4base_pow, gcd_k_slack_order4base_pow, k, slack_order4base_pow, pt7base_pow, pt7tgt, /):
>>> ds = 101*569
>>> p2e4ds = {101:1, 569:1}
>>> de = 379*29663
>>> slack_order4base_pow = ds*tight_order4base**2
>>> pt7base_pow = ops.pow_(pt7base, de)
>>> for (part4exp, p2e4part4exp, _0_pt7tgt) in ts:
...     a = perfect_div(tight_order4base, part4exp)
...     k = part0_4exp*a
...     #gcd_k_tight_order4base = a
...     #factorization4gcd_k_tight_order4base = complete_factor_pint_via_trial_division(factorization4tight_order4base, gcd_k_tight_order4base)
...     #(factorization4gcd_k_tight_order4base, gcd_k_tight_order4base, k, tight_order4base, pt7base)
...     gcd_k_slack_order4base_pow = gcd(k, slack_order4base_pow)
...     factorization4gcd_k_slack_order4base_pow = complete_factor_pint_via_trial_division(factorization4tight_order4base, gcd_k_slack_order4base_pow)
...     if 0b001:
...         #_1_pt7tgt = ops.pow_(pt7base, k)
...         _1_pt7tgt = ops.pow_(pt7radix, a)
...         for b in iter_unsorted_all_factors5factorization_(p2e4part4exp):
...             pt7tgt = ops.pow_(_1_pt7tgt, b)
...             (pt7root, ((_pt7tgt, e4tgt), (_pt7base_pow, e4base_pow))) = ops.repr_kth_roots7cyclic_group__7slack_order4base_pow_(factorization4gcd_k_slack_order4base_pow, gcd_k_slack_order4base_pow, k, slack_order4base_pow, pt7base_pow, pt7tgt)
...             assert ops.eq_(pt7tgt, ops.pow_(pt7root, k))
...             assert ops.eq_(pt7tgt, _pt7tgt)
...             assert ops.eq_(pt7base_pow, _pt7base_pow)
...             assert ops.eq_(pt7root, ops.mul_(ops.pow_(pt7tgt, e4tgt), ops.pow_(pt7base_pow, e4base_pow)))
...     #print(pt7tgt, exp, sep=':')






def repr_kth_roots7cyclic_group__7low_level_(sf, factorization4t, gcd_k_t, u2, v2, s, t, u, v, k, tight_order4base, pt7base_pow, pt7tgt, /):
    neednot test: used by repr_kth_roots7cyclic_group_






















py_adhoc_call   seed.math.discrete_logarithm__7cyclic_group7kth_roots   @f
]]]'''#'''
__all__ = r'''
IGroupOps7discrete_logarithm7kth_root
    IGroupOps7discrete_logarithm7kth_root__7uint_mod
        GroupOps7discrete_logarithm7kth_root__7uint_mod

IGroupOps7discrete_logarithm7kth_root
    mul_order_of__7cyclic_group7baby_steps_giant_steps_method_
    mul_order_of__7cyclic_group7slack_order4base_is_prime_power_
    mul_order_of__7cyclic_group7factorization4slack_order4base_

    discrete_logarithm__7cyclic_group7baby_steps_giant_steps_method_
    discrete_logarithm__7cyclic_group7tight_order4base_is_prime_
    discrete_logarithm__7cyclic_group7tight_order4base_is_prime_power_
    discrete_logarithm__7cyclic_group7factorization4tight_order4base_
    partial_discrete_logarithm__7cyclic_group7factorization4part4tight_order4base_


    repr_kth_roots4unity7cyclic_group_
    repr_kth_roots7cyclic_group_
    repr_kth_roots7cyclic_group__7slack_order4base_pow_
    repr_kth_roots7cyclic_group__7low_level_


NoKthRootError
PowsRepr

decompose_coprime_part_
    noncoprime_part_
    coprime_part_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge, check_uint_lt
    from seed.types.attr.class2method_decorator import mk_instance_method_decorator_
    #def mk_instance_method_decorator_(klass, /, *, name=''):
    from seed.algo.baby_steps_giant_steps_method import search_mul_order__7baby_steps_giant_steps_method_
    #def search_mul_order__7baby_steps_giant_steps_method_(sz4giant_step, mul_, pow_, base, /, *, key=None, hash_vs_sort=False, _debug=False, tmay_target=()):
    #   'sz4giant_step/uint{>0} -> mul_/(R->R->R) -> pow_/(R->int->R) -> base/R -> may mul_order4base/int{=!=0} # [base**mul_order4base == (one if not tmay_target else tmay_target[0])][0 =!= mul_order4base][mul_order4base == mul_order_(base)][0 < mul_order4base < sz4giant_step*(1+sz4giant_step)] # DL:discrete_logarithm'
    from seed.algo.baby_steps_giant_steps_method import calc_min4sz4giant_step5max4order4base_
    #def calc_min4sz4giant_step5max4order4base_(max4order4base, /):
    #   'max4order4base/uint{>0} -> min4sz4giant_step/uint{>0} # [0 < mul_order4base < sz4giant_step*(1+sz4giant_step)]'
    from seed.math.II import II__p2e_
    from seed.math.floor_ceil_tools.fc_perfect import perfect_div
    from seed.math.Chinese_Remainder_Theorem__ver2 import apply_CRT__pairs
    from seed.math.semi_factor_pint_via_trial_division import complete_factor_pint_via_trial_division
    from seed.helper.repr_input import repr_helper
    from seed.math.gcd import gcd
    from seed.math.gcd import noncoprime_part_of_to_, coprime_part_of_to_
    #def noncoprime_part_of_to_(u7whole, u7mask, /):
    #def coprime_part_of_to_(u7whole, u7mask, /):

    # [noncoprime_part_of_to_(a, b) == noncoprime_part_(b;a)]
    # [coprime_part_of_to_(a, b) == coprime_part_(b;a)]

    from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple_, mk_namedtuple__check6make_
    #def mk_namedtuple_(__module__, nm, nms_or_str, /, *args, **kwds):
    #def mk_namedtuple__check6make_(__module__, nm, nms_or_str, /, *args, **kwds):
    #    def _check6make_(sf, /):

    #from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import mk_named_pseudo_tuple_
    #def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
    from seed.iters.apply_commutative_operations_except_one import iter_apply_commutative_operations_except_one_
    #def iter_apply_commutative_operations_except_one_(apply_, commutative_operation_keys, x0, /):
    #   :: (k->x->x) -> [k] -> x -> (iter x)


#.#################################
___end_mark_of_excluded_global_names__0___ = ...
r'''[[[
@20260831
[[[
===
[G::FiniteGroup][base :: G]:
    [G.one == base**0 == base/base]
    [mul_order_of_(base) =[def]= min{e | [e:<-[1..]][base**e == G.one]}]
    [cyclic_group7generated_by(base) =[def]= {base**e | [e:<-[1..]]}]
    [mul_order_of_(base) == len(cyclic_group7generated_by(base))]
[G::FiniteGroup][base :: G][e::int]:
    [is_slack_order_of_(base, e) =[def]= [e > 0][0 == e%mul_order_of_(base)]]
    #slack_order4base
    [is_tight_order_of_(base, e) =[def]= [e == mul_order_of_(base)]]
    #tight_order4base

[G::FiniteGroup][base :: G][slack_order4base::uint{>0}][base**slack_order4base == base**0][power :<- cyclic_group7generated_by(base)]:
    [discrete_logarithm_(base, slack_order4base;power) =[def]= min{exp | [[exp:<-[1..=slack_order4base]][base**exp==power]]}]

[G::FiniteGroup][base :: G][slack_order4base::uint{>0}][base**slack_order4base == base**0]:
    [mul_order_of_(base) == discrete_logarithm_(base, slack_order4base; base**0)]
      #tight_order4base

[M,N::uint{>0}][M%N==0][r::int]:
    [mods6mod_(M,N;r) =[def]= {u%M | [u::int][u =[%N]= r]}]
    [@[u:<-mods6mod_(M,N;r)] -> [u =[%N]= r]]
    [@[u:<-mods6mod_(M,N;r)] -> [0 <= u//N < (M///N)]]
    [len(mods6mod_(M,N;r)) == (M///N)]
    [mods6mod_(M,N;r) == {(r%N+d*N)%M | [d:<-[0..<(M///N)]]}]
[a,b::int{>0}]:
  [noncoprime_part_(a; b) =[def]= max{u | [u:<-[1..=b]][0 == b%u][?[e:<-[1..]] -> [0 == a**e%u]]}]
  [0 == b%noncoprime_part_(a; b)]
  [coprime_part_(a; b) =[def]= b///noncoprime_part_(a; b)]
  [b == coprime_part_(a; b)*noncoprime_part_(a; b)]
  [1 == gcd(coprime_part_(a; b), noncoprime_part_(a; b))]

  [decompose_coprime_part_(a; b) =[def]= (coprime_part_(a; b), noncoprime_part_(a; b))]



  [noncoprime_part_(a; b) == max{u | [u:<-[1..=b]][0 == b%u][[e:=b] -> [0 == a**e%u]]}]
  [noncoprime_part_(a; b) == max{u | [u:<-[1..=b]][0 == b%u][[e:=b.bit_length()] -> [0 == a**e%u]]}]
  [noncoprime_part_(a; b) == gcd(b,pow(a,b.bit_length(),b))]





[G::FiniteGroup][base :: G][k::int{=!=0}][power :<- cyclic_group7generated_by(base)][tight_order4base := mul_order_of_(base)]:
    # G.one**/k =[def]=
    [kth_roots4unity7cyclic_group_(base, tight_order4base;k) =[def]= let [g:=gcd(k,tight_order4base)] in base .**: mods6mod_(tight_order4base,(tight_order4base///g);0)]
        # [formula__kth_roots4unity7cyclic_group_]:here

    #power**/k =[def]=
    [kth_roots7cyclic_group_(base, tight_order4base;k;power) =[def]= let [exp:=discrete_logarithm_(base, tight_order4base;power)][g:=gcd(k,tight_order4base)] in if 0=!=exp%g then {} else let [rt:=base**((exp///g) * (k///g)**-1%(tight_order4base///g))] in rt .*: kth_roots4unity7cyclic_group_(base, tight_order4base;k)]

    #len(G.one**/k)
    [len(kth_roots4unity7cyclic_group_(base, tight_order4base;k)) == (tight_order4base///gcd(k,tight_order4base))]
    #len(power**/k)
    [len(kth_roots7cyclic_group_(base, tight_order4base;k;power)) <- {0, (tight_order4base///gcd(k,tight_order4base))}]

    #power**/k ==
    [kth_roots7cyclic_group_(base, tight_order4base;k;power) == let [h := noncoprime_part_(k; coprime_part_(tight_order4power;tight_order4base///tight_order4power))] in kth_roots7cyclic_group_(base**h, tight_order4base///h;k;power) :>*: kth_roots4unity7cyclic_group_(base, tight_order4base;k)]
        #ver1


    #power**/k ==
    [kth_roots7cyclic_group_(base, tight_order4base;k;power) == let [h := coprime_part_(tight_order4power;tight_order4base///tight_order4power)] in kth_roots7cyclic_group_(base**h, tight_order4base///h;k;power) :>*: kth_roots4unity7cyclic_group_(base, tight_order4base;k)]
        #ver2
        #==>>:
    [kth_roots7cyclic_group_(base, tight_order4base;k;power) == let [h := coprime_part_(tight_order4power;tight_order4base///tight_order4power)][bh:=base**h][obsh:=tight_order4base///h][eh:=discrete_logarithm_(bh, obsh;power)][gh:=gcd(k,obsh)] in if 0=!=eh%gh then {} else let [rt:=bh**((eh///gh) * (k///gh)**-1%(obsh///gh))] in rt .*: kth_roots4unity7cyclic_group_(base, tight_order4base;k)]
        #ver2
        # [formula__kth_roots7cyclic_group7convert_to_strict_]:here
        # [obsh == noncoprime_part_(tight_order4power;obsh)]
        # [all_prime_factors_of(obsh) == all_prime_factors_of(tight_order4power)]


[G::FiniteGroup][base :: G][k::int{=!=0}][power :<- cyclic_group7generated_by(base)][tight_order4base := mul_order_of_(base)][tight_order4power := mul_order_of_(power)][exp:=discrete_logarithm_(base, tight_order4base;power)]:
    [tight_order4base == noncoprime_part_(tight_order4power;tight_order4base)]:
        <==> [all_prime_factors_of(tight_order4base) == all_prime_factors_of(tight_order4power)]

    !! [power**tight_order4power == G.one]
    !! [base**exp == power]
    [base**(exp*tight_order4power) == G.one]
    !! [base**tight_order4base == G.one]
    [0 == (exp*tight_order4power)%tight_order4base]
    !! [0 == tight_order4base%tight_order4power]
    [0 == exp%(tight_order4base///tight_order4power)]
    !! tight
    [1 == gcd(tight_order4base, exp///(tight_order4base///tight_order4power))]
    [(tight_order4base///tight_order4power) == gcd(exp, tight_order4base)]
    [(tight_order4base///tight_order4power) == noncoprime_part_(tight_order4base; exp)]

    [0 == exp%gcd(k,tight_order4base)]:
        <==> [0 == gcd(exp, tight_order4base)%gcd(k,tight_order4base)]
        <==> [0 == (tight_order4base///tight_order4power)%gcd(k,tight_order4base)]
        <==> [0 == (tight_order4base///gcd(k,tight_order4base))%tight_order4power]
        <==> [G.one == power**(tight_order4base///gcd(k,tight_order4base))]
            # [criterion__has_kth_roots7cyclic_group_]:here
        <==> [0 == tight_order4base%(tight_order4power*gcd(k,tight_order4base))]
        ==>> [[p::prime][0 == gcd(k,tight_order4base)%p][0 == tight_order4power%p] -> [0 == tight_order4base%(p*gcd(k,tight_order4base))][gde_(p;tight_order4base) > gde_(p;k)]]
        ==>> [[p::prime][0 == gcd(k,tight_order4base)%p][gde_(p;tight_order4base) < gde_(p;k)][t:=noncoprime_part_(k;tight_order4base)] -> [0 =!= tight_order4power%p][gde_(p;t) == gde_(p;tight_order4base)]]

[G::FiniteGroup][base :: G][k::int{=!=0}][power :<- cyclic_group7generated_by(base)][tight_order4base := mul_order_of_(base)][tight_order4power := mul_order_of_(power)][exp:=discrete_logarithm_(base, tight_order4base;power)][tight_order4base == noncoprime_part_(tight_order4power;tight_order4base)][0 == exp%gcd(k,tight_order4base)]:
    !! [0 == exp%gcd(k,tight_order4base)]
    [G.one == power**(tight_order4base///gcd(k,tight_order4base))]
    [0 == tight_order4base%(tight_order4power*gcd(k,tight_order4base))]

    !! [tight_order4base == noncoprime_part_(tight_order4power;tight_order4base)]
    [all_prime_factors_of(tight_order4base) == all_prime_factors_of(tight_order4power)]
    [tight_order4base =[:prime_factors:]= tight_order4power]


    [g7kpw:=gcd(k,tight_order4power)]
    [0 == tight_order4power%g7kpw]
    [0 == tight_order4base%g7kpw]

    [k9pw := noncoprime_part_(g7kpw; k)]
    [k9pw =[:prime_factors:]= g7kpw]
    [0 == k9pw%g7kpw]
    [pw9k := noncoprime_part_(g7kpw; tight_order4power)]
    [pw9k =[:prime_factors:]= g7kpw =[:prime_factors:]= k9pw]
    [0 == pw9k%g7kpw]
    [bs9kpw := noncoprime_part_(g7kpw; tight_order4base)]
    !! [tight_order4base =[:prime_factors:]= tight_order4power]
    [bs9kpw =[:prime_factors:]= g7kpw =[:prime_factors:]= k9pw =[:prime_factors:]= pw9k]
    [0 == bs9kpw%pw9k]
    [0 == bs9kpw%g7kpw]
    [t:=bs9kpw]
    [s:=tight_order4base///t]

    !! [tight_order4base =[:prime_factors:]= tight_order4power]
    [bs9kpw == noncoprime_part_(k; tight_order4base)]
    [(s,t) == decompose_coprime_part_(k; tight_order4base)]

    [g7kbs9pw := noncoprime_part_(tight_order4power; gcd(k,tight_order4base))]
    [g7kbs9pw == gcd(k9pw,bs9kpw)]
    !! [0 == k9pw%g7kpw]
    !! [0 == bs9kpw%g7kpw]
    [0 == g7kbs9pw%g7kpw]

    !! [tight_order4base =[:prime_factors:]= tight_order4power]
    [g7kbs9pw == gcd(k,tight_order4base)]

    !! [pw9k := noncoprime_part_(g7kpw; tight_order4power)]
    !! [bs9kpw := noncoprime_part_(g7kpw; tight_order4base)]
    !! [0 == bs9kpw%pw9k]
    !! [0 == tight_order4base%tight_order4power]
    [(bs9kpw///pw9k) == noncoprime_part_(g7kpw; tight_order4base///tight_order4power)]
    !! [g7kpw:=gcd(k,tight_order4power)]
    !! [tight_order4base =[:prime_factors:]= tight_order4power]
    [(bs9kpw///pw9k) == noncoprime_part_(k; tight_order4base///tight_order4power)]
    !! [g7kbs9pw == gcd(k,tight_order4base)]
    [0 == (bs9kpw///pw9k)%g7kbs9pw]:
        <==> [0 == noncoprime_part_(k; tight_order4base///tight_order4power)%gcd(k,tight_order4base)]
        <==> [0 == (tight_order4base///tight_order4power)%gcd(k,tight_order4base)]
        <==> [0 == tight_order4base%(tight_order4power*gcd(k,tight_order4base))]
        <==> [0 == exp%gcd(k,tight_order4base)]
        <==> [0 < len(kth_roots7cyclic_group_(base, tight_order4base;k;power))]
    !! [0 == exp%gcd(k,tight_order4base)]
    [0 == (bs9kpw///pw9k)%g7kbs9pw]
    [0 < len(kth_roots7cyclic_group_(base, tight_order4base;k;power))]

    !! [0 == (tight_order4base///tight_order4power)%gcd(k,tight_order4base)]
    !! [tight_order4base =[:prime_factors:]= tight_order4power]
    [gcd(k,tight_order4base) == gcd(k,tight_order4base///tight_order4power)]
    [gcd(k,tight_order4base) == noncoprime_part_(gcd(k,tight_order4base);k)]
    [gcd(k,tight_order4base) == noncoprime_part_(tight_order4base;k)]
    [1 == gcd(gcd(k,tight_order4base), k///gcd(k,tight_order4base))]
    [kg := k///gcd(k,tight_order4base)]
    !! [g7kbs9pw == gcd(k,tight_order4base)]
    [k == kg*g7kbs9pw]
    [1 == gcd(kg, g7kbs9pw)]


    !! [0 == exp%gcd(k,tight_order4base)]
    !! [g7kbs9pw == gcd(k,tight_order4base)]
    [0 == exp%g7kbs9pw]

    !! [t:=bs9kpw]
    !! [bs9kpw == noncoprime_part_(k; tight_order4base)]
    !! [g7kbs9pw == gcd(k,tight_order4base)]
    [0 == t%g7kbs9pw]
    [0 == gcd(exp,t)%g7kbs9pw]
    [0 == (exp%t)%g7kbs9pw]
    [exp6s := (exp%s)]
    [exp6t := (exp%t)]
    [0 == exp6t%g7kbs9pw]

    !! [(s,t) == decompose_coprime_part_(k; tight_order4base)]
    [s*t == tight_order4base]
    [1 == gcd(s,t)]
    !! [tight_order4base > 0]
    [s > 0]
    [t > 0]
    [v:=t**-1%s]
    [t*v%s == t*t**-1%s == 1]
    [0 == (1-t*v)%s]
    [u := (1-t*v)///s]
    [1 == s*u+t*v]
    [u == (t**-1%s *t -1)///-s]

    !! [1 == s*u+t*v]
    [exp =[%(s*t)]= exp6s*t*v + exp6t*s*u]
    !! [0 == exp%g7kbs9pw]
    !! [0 == t%g7kbs9pw]
    !! [0 == exp6t%g7kbs9pw]
    [(exp///g7kbs9pw) =[%(s*(t///g7kbs9pw))]= exp6s*(t///g7kbs9pw)*v + (exp6t///g7kbs9pw)*s*u]
    [exg := (exp///g7kbs9pw)]
    [tg := (t///g7kbs9pw)]
    [etg := (exp6t///g7kbs9pw)]
    [exg =[%(s*tg)]= exp6s*tg*v + etg*s*u]

    [mods_(s*t, exp/k)
    !! [0 == exp6t%g7kbs9pw]
    !! [g7kbs9pw == gcd(k,tight_order4base)]
    !! [k == kg*g7kbs9pw]
    == mods6mod_(s*t,s*tg; exg/kg)
    !! [1 == gcd(kg, g7kbs9pw)]
    == mods6mod_(s*t,s*tg; exg*kg**-1%(s*tg))
    !! [exg =[%(s*tg)]= exp6s*tg*v + etg*s*u]
    == mods6mod_(s*t,s*tg; (exp6s*tg*v + etg*s*u)*kg**-1%(s*tg))
    ]
    [mods_(s*t, exp/k) == mods6mod_(s*t,s*tg; (exp6s*tg*v + etg*s*u)*kg**-1%(s*tg))]


    !! [power == base**exp]
    [power**s
    == base**(s*exp%(s*t))
    == base**(exp%t*s%(s*t))
    == base**(exp6t*s)
    ]
    [power**s == base**(exp6t*s)]
    [power**t == base**(exp6s*t)]
    [power**tg
    == base**(tg*exp%(s*t))
    !! [0 == exp%g7kbs9pw]
    == base**(t*exg%(s*t))
    == base**(exg%s *t%(s*t))
    == base**((exp///g7kbs9pw)%s *t%(s*t))
    == base**((exp*g7kbs9pw**-1)%s *t%(s*t))
    == base**((g7kbs9pw**-1%s)*exp6s*t)
    ]
    [power**tg == base**((g7kbs9pw**-1%s)*exp6s*t)]
    [g6s := g7kbs9pw%s]
    [ig6s := g7kbs9pw**-1%s]
    [power**tg == base**(ig6s*exp6s*t)]

    [r::int][1==gcd(r,tight_order4base)][radix:=base**r]:
        !! [radix:=base**r]
        !! [1==gcd(r,tight_order4base)]
        !! [tight_order4base := mul_order_of_(base)]
        [mul_order_of_(radix) == tight_order4base]
        [kth_roots7cyclic_group_(base, tight_order4base;k;power) == kth_roots7cyclic_group_(radix, tight_order4base;k;power)]

        [ir := r**-1%(s*t)]
        !! [radix:=base**r]
        [base == radix**ir]
        !! [power == base**exp]
        [power == radix**(exp*ir)]

        !! [power**tg == base**(ig6s*exp6s*t)]
        [power**tg == radix**(ir*ig6s*exp6s*t)]


        [kth_roots7cyclic_group_(base, tight_order4base;k;power)
        == base .**: mods_(s*t, exp/k)
        !! [mods_(s*t, exp/k) == mods6mod_(s*t,s*tg; (exp6s*tg*v + etg*s*u)*kg**-1%(s*tg))]
        == base .**: mods6mod_(s*t,s*tg; (exp6s*tg*v + etg*s*u)*kg**-1%(s*tg))
        == radix .**: mods6mod_(s*t,s*tg; (ir*exp6s*tg*v + ir*etg*s*u)*kg**-1%(s*tg))
        !! [(ir*ig6s*exp6s*t) =[%(s*tg)]= ir*(ig6s*exp6s*g7kbs9pw%s)*tg == ir*exp6s*tg]
        == radix .**: mods6mod_(s*t,s*tg; ((ir*ig6s*exp6s*t)*v + ir*etg*s*u)*kg**-1%(s*tg))
        !! [power**tg == radix**(ir*ig6s*exp6s*t)]
        == (power**(tg*v*kg**-1%(s*tg))) .*: (radix .**: mods6mod_(s*t,s*tg; (ir*etg*s*u)*kg**-1%(s*tg)))
        ]
        [kth_roots7cyclic_group_(base, tight_order4base;k;power) == (power**(tg*v*kg**-1%(s*tg))) .*: (radix .**: mods6mod_(s*t,s*tg; (ir*etg*s*u)*kg**-1%(s*tg)))]
    ==>>:
    [kth_roots7cyclic_group_(base, tight_order4base;k;power) == (power**(tg*v*kg**-1%(s*tg))) .*: (base .**: mods6mod_(s*t,s*tg; (etg*s*u)*kg**-1%(s*tg)))]
    [kth_roots7cyclic_group_(base, tight_order4base;k;power) == ((power**tg)**(v*kg**-1%s)) .*: ((base**s) .**: mods6mod_(t,tg; etg*u*kg**-1%tg))]
    ==>>:
        # [formula__kth_roots7cyclic_group7strict_]:goto
[G::FiniteGroup][base :: G][k::int{=!=0}][power :<- cyclic_group7generated_by(base)][tight_order4base := mul_order_of_(base)][tight_order4power := mul_order_of_(power)][exp:=discrete_logarithm_(base, tight_order4base;power)][#NOT_REQUIRED:[tight_order4base == noncoprime_part_(tight_order4power;tight_order4base)]#][0 == exp%gcd(k,tight_order4base)]:
    # s,t,u,v,tg,kg,etg
    [(s,t) := decompose_coprime_part_(k; tight_order4base)]
    [v := t**-1%s]
    [u := (1-t*v)///s]
    [exp6t := (exp%t)]
    [g7kbs9pw := gcd(k,tight_order4base)]
    [kg := k///g7kbs9pw]
    [tg := (t///g7kbs9pw)]
    [etg := (exp6t///g7kbs9pw)]
    [kth_roots7cyclic_group_(base, tight_order4base;k;power) == ((power**tg)**(v*kg**-1%s)) .*: ((base**s) .**: mods6mod_(t,tg; etg*u*kg**-1%tg))]
        # [formula__kth_roots7cyclic_group7strict_]:here
        # neednot to calc exp,exp6s
        # only need exp6t,tight_order4power
        # ??? ok if tight_order4base --> semi_tight_order4base where[1==gcd(k,ds)][semi_tight_order4base:=ds*tight_order4base] ???
        #       Yes! <<==: [formula__kth_roots7cyclic_group7strict__7semi_tight_order4base_]:goto
        #
        # neednot: [formula__kth_roots7cyclic_group7convert_to_strict_]:goto
        #       <<==:
        # ??? does it hold if remove precondition: [tight_order4base == noncoprime_part_(tight_order4power;tight_order4base)] ???
        #       Yes! <<==:
    [remove precondition: [tight_order4base == noncoprime_part_(tight_order4power;tight_order4base)]]:
        [kth_roots7cyclic_group_(base, tight_order4base;k;power)**k
        == ((power**tg)**(v*kg**-1%s *k)) .*: ((base**s) .**: (k .*: mods6mod_(t,tg; etg*u*kg**-1%tg)))
        == ((power**tg)**(v*kg**-1%s *kg*g)) .*: ((base**s) .**: (kg*g .*: mods6mod_(t,tg; etg*u*kg**-1%tg)))
        == ((power**t)**(v%s)) .*: ((base**s) .**: (kg .*: mods6mod_(t*g7kbs9pw,t; exp6t*u*kg**-1%t)))
        == ((power**t)**(v%s)) .*: ((base**s) .**: (kg .*: mods6mod_(t*g7kbs9pw,t; exp6t*u*kg**-1%t) %t))
        == ((power**t)**(v%s)) .*: ((base**s) .**: (kg .*: mods_(t; exp6t*u*kg**-1%t)))
        == ((power**t)**(v%s)) * ((base**s)**(exp6t*u %t))
        !! [power**t == base**(exp6s*t)]
        == ((base**(exp6s*t))**(v%s)) * ((base**s)**(exp6t*u %t))
        == (base**(exp6s*v%s *t + exp6t*u%t *s))
        == base**((exp6s*v*t + exp6t*u*s) %(s*t))
        !! [exp =[%(s*t)]= exp6s*t*v + exp6t*s*u]
        == base**(exp %(s*t))
        == power
        ]
        ok!
    [try:tight_order4base-->semi_tight_order4base][[ds::int][1==gcd(k,ds)][semi_tight_order4base:=ds*tight_order4base]]:
        [sc := s*ds]
        [(sc,t) == decompose_coprime_part_(k;semi_tight_order4base)]
        [vc := t**-1%sc]
        [uc := (1-t*vc)///sc]
        same:[exp6t := (exp%t)]
        same:[g7kbs9pw == gcd(k,tight_order4base) == gcd(k,semi_tight_order4base)]
        same:[kg := k///g7kbs9pw]
        same:[tg := (t///g7kbs9pw)]
        same:[etg := (exp6t///g7kbs9pw)]
        s,u,v --> sc,uc,vc
        [kth_roots7cyclic_group_(base, tight_order4base;k;power)**k
        == ((power**tg)**(v*kg**-1%s *k)) .*: ((base**s) .**: (k .*: mods6mod_(t,tg; etg*u*kg**-1%tg)))

        =?= ((power**tg)**(vc*kg**-1%sc *k)) .*: ((base**sc) .**: (k .*: mods6mod_(t,tg; etg*uc*kg**-1%tg)))
        == ((power**tg)**(vc*kg**-1%(s*ds) *k)) .*: ((base**(s*ds)) .**: (k .*: mods6mod_(t,tg; etg*uc*kg**-1%tg)))
        == ((power**t)**(vc*kg**-1%(s*ds) *kg %s)) .*: ((base**(s*ds)) .**: (k .*: mods6mod_(t,tg; etg*uc*kg**-1%tg)))
        == ((power**t)**(v*kg**-1%s *kg %s)) .*: ((base**(s*ds)) .**: (k .*: mods6mod_(t,tg; etg*uc*kg**-1%tg)))
        == ((power**t)**(v*kg**-1%s *kg %s)) .*: ((base**s) .**: (k .*: mods6mod_(t,tg; ds*etg*uc*kg**-1%tg)))
        == ((power**t)**(v*kg**-1%s *kg %s)) .*: ((base**s) .**: (kg .*: mods_(t; ds*uc*exp6t*kg**-1%t)))
        !! [uc := (1-t*vc)///sc]
        => [ds*uc == (1-t*vc)///s]
        => [s*ds*uc =[%t]= 1]
        !! [s*u =[%t]= 1]
        !! [1==gcd(s,t)]
        => [ds*uc =[%t]= s**-1%t =[%t]= u]
        == ((power**t)**(v*kg**-1%s *kg %s)) .*: ((base**s) .**: (kg .*: mods_(t; u*exp6t*kg**-1%t)))
        ...same above
        ]
        ok!
    [[ds::int][1==gcd(k,ds)][semi_tight_order4base:=ds*tight_order4base]]
        [sc := s*ds]
        [(sc,t) == decompose_coprime_part_(k;semi_tight_order4base)]
        [vc := t**-1%sc]
        [uc := (1-t*vc)///sc]
        [kth_roots7cyclic_group_(base, semi_tight_order4base;k;power) == ((power**tg)**(vc*kg**-1%sc *k)) .*: ((base**sc) .**: (k .*: mods6mod_(t,tg; etg*uc*kg**-1%tg)))]
            # [formula__kth_roots7cyclic_group7strict__7semi_tight_order4base_]:here

    !! [power**s == base**(exp6t*s)]
    [power**s == (base**s)**exp6t]
    [exp6t == discrete_logarithm_((base**s), (tight_order4base///s);(power**s))]
        # [formula__calc_partial_discrete_logarithm_]:here
    [tight_order4power{base,tight_order4base;power} == if power==G.one then 1 else let [?p:=>[p::prime][0==tight_order4base%p]][ep:=gde_(p;tight_order4base)][_e:=(tight_order4base///p**ep)][_b:=base**_e][_pw:=power**_e][e:=min{e | [e:<-[0..=ep]][G.one==_pw**(p**e)]}][_pe:=p**_e] in (p**e * tight_order4power{base**_pe,tight_order4base///_pe;power**_pe})]
        # [formula__calc_mul_order7cyclic_group_]:here

===
]]]
#]]]'''#'''
__all__

# \(def \)\@<!\<\w*(sf,.*)
#   to avoid: call f(sf, ...) instead of sf.f(...)
# \(^@_method_\)\@<!\ndef
#   to avoid: method lossing
def decompose_coprime_part_(u7mask, u7whole, /):
    # [decompose_coprime_part_(a; b) =[def]= (coprime_part_(a; b), noncoprime_part_(a; b))]
    t = noncoprime_part_(u7mask, u7whole)
    s = perfect_div(u7whole, t)
    return (s, t)

def noncoprime_part_(u7mask, u7whole, /):
    # [noncoprime_part_of_to_(a, b) == noncoprime_part_(b;a)]
    return noncoprime_part_of_to_(u7whole, u7mask)
def coprime_part_(u7mask, u7whole, /):
    # [coprime_part_of_to_(a, b) == coprime_part_(b;a)]
    return coprime_part_of_to_(u7whole, u7mask)

class NoKthRootError(Exception):pass



class IGroupOps7discrete_logarithm7kth_root(ABC):
    __slots__ = ()
    @abstractmethod
    def mul_(sf, pt6lhs, pt6rhs, /):
        'pt/G -> pt/G -> pt/G'
    @abstractmethod
    def pow_(sf, pt, e, /):
        'pt/G -> e/int -> pt/G'
    @abstractmethod
    def eq_(sf, pt6lhs, pt6rhs, /):
        'pt/G -> pt/G -> bool'
    @property
    @abstractmethod
    def one(sf, /):
        '-> pt/G # [one == pow_(one,0)]'
    @abstractmethod
    def eq_one_(sf, pt, /):
        'pt/G -> bool'
        return sf.eq_(pt, sf.one)
    @property
    @abstractmethod
    def hash_vs_sort(sf, /):
        '-> bool'
    @abstractmethod
    def key_func(sf, pt, /):
        'pt/G -> (Hashable if not hash_vs_sort else Ord)'

class IGroupOps7discrete_logarithm7kth_root__7uint_mod(IGroupOps7discrete_logarithm7kth_root):
    '[pt :: uint%modulus]'
    __slots__ = ()
    @property
    @abstractmethod
    def modulus(sf, /):
        '-> int{>=2} # <<== [G.one:=1]'
    @override
    def mul_(sf, pt6lhs, pt6rhs, /):
        'pt/G -> pt/G -> pt/G'
        return (pt6lhs*pt6rhs)%sf.modulus
    @override
    def pow_(sf, pt, e, /):
        'pt/G -> e/int -> pt/G'
        return pow(pt, e, sf.modulus)
    @override
    def eq_(sf, pt6lhs, pt6rhs, /):
        'pt/G -> pt/G -> bool'
        return 0 == (pt6lhs-pt6rhs)%sf.modulus
    @override
    def eq_one_(sf, pt, /):
        'pt/G -> bool'
        return 0 == (pt-1)%sf.modulus
    #@override
    one = 1
    #@override
    hash_vs_sort = False
    @override
    def key_func(sf, pt, /):
        'pt/G -> (Hashable if not hash_vs_sort else Ord)'
        return pt%sf.modulus

_GroupOps7discrete_logarithm7kth_root__7uint_mod = mk_namedtuple__check6make_(__name__, '_GroupOps7discrete_logarithm7kth_root__7uint_mod', 'modulus')
class GroupOps7discrete_logarithm7kth_root__7uint_mod(_GroupOps7discrete_logarithm7kth_root__7uint_mod, IGroupOps7discrete_logarithm7kth_root__7uint_mod):
    ___no_slots_ok___ = True
    def _check6make_(sf, /):
        check_int_ge(2, sf.modulus)










_method_ = mk_instance_method_decorator_(IGroupOps7discrete_logarithm7kth_root)

#@_method_
#def mul_order_of__7cyclic_group7tight_order4base_is_prime_power_(sf, p, ep, tight_order4base, pt7base, pt7tgt, /, *, to_log_p_mul_order=False):
#    '[tight_order4base == mul_order_of_(pt7base)][?[e:<-[1..=tight_order4base]] -> [pt7tgt == pt7base**e]] => p/prime -> ep/uint -> tight_order4base/int{>0}{==p**ep} -> pt7base/G -> pt7tgt/G -> tight_order4tgt/int{>0}{==mul_order_of_(pt7tgt)}'
@_method_
def mul_order_of__7cyclic_group7slack_order4base_is_prime_power_(sf, p, ep, slack_order4base, pt7base, /, *, to_log_p_mul_order=False):
    '[0 == slack_order4base%mul_order_of_(pt7base)] => p/prime -> ep/uint -> slack_order4base/int{>0}{==p**ep} -> pt7base/G -> tight_order4base/int{>0}{==mul_order_of_(pt7base)}'
    check_int_ge(2, p)
    check_int_ge(0, ep)
    check_int_ge(1, slack_order4base)
    assert (lbP:=p.bit_length())*ep >= slack_order4base.bit_length() >= (lbP-1)*ep
    assert slack_order4base == p**ep
    eq_one_ = sf.eq_one_
    eq_ = sf.eq_
    pow_ = sf.pow_
    if eq_one_(pt7base):
        return 1 if not to_log_p_mul_order else 0
    # [pt7base =!= G.one]
    # [1 < mul_order_of_(pt7base)]

    B = pt7base
    e = 0
    # [B == pt7base**(p**e)]
    # [B =!= G.one]
    for e in range(1, 1+ep):
        # [B == pt7base**(p**(e-1))]
        # [B =!= G.one]
        B = pow_(B, p)
        # [B == pt7base**(p**e)]
        if eq_one_(B):
            return p**e if not to_log_p_mul_order else e
        # [B =!= G.one]
    assert e == ep
    raise ValueError('[pt7base**(p**ep) =!= G.one]', p, ep, pt7base)


def _pow_except1_(eq_one_, pow_, j2pe, pt0, /):
    def apply_(pe, pt, /):
        '(p, ep) -> pt -> pt**(p**e)'
        (p, ep) = pe
        for _ in range(ep):
            if eq_one_(pt): break
            pt = pow_(pt, p)
        return pt

    commutative_operation_keys = j2pe
    x0 = pt0
    pts = iter_apply_commutative_operations_except_one_(apply_, commutative_operation_keys, x0)
    return pts
@_method_
def mul_order_of__7cyclic_group7factorization4slack_order4base_(sf, factorization4slack_order4base, slack_order4base, pt7base, /, *, to_factorization4mul_order=False):
    '[0 == slack_order4base%mul_order_of_(pt7base)] => factorization4slack_order4base/{p/prime:ep/uint{>0}} -> slack_order4base/int{>0}{==II__p2e_(factorization4slack_order4base)} -> pt7base/G -> tight_order4base/int{>0}{==mul_order_of_(pt7base)}'
    check_int_ge(1, slack_order4base)
    assert slack_order4base == II__p2e_(factorization4slack_order4base)

    eq_one_ = sf.eq_one_
    eq_ = sf.eq_
    pow_ = sf.pow_
    if eq_one_(pt7base):
        return 1 if not to_factorization4mul_order else {}
    # [pt7base =!= G.one]
    # [1 < mul_order_of_(pt7base)]

    ##################
    #new:
    ##################
    j2pe = sorted(factorization4slack_order4base.items())
    pts = _pow_except1_(eq_one_, pow_, j2pe, pt7base)
    j2pe, pts
    p2e4tight_order4base = {}
    for (p, ep), pt in zip(j2pe, pts):
        # [pt == pt7base**(slack_order4base///p**ep)]
        e = sf.mul_order_of__7cyclic_group7slack_order4base_is_prime_power_(p, ep, p**ep, pt, to_log_p_mul_order=True)
        if not 0 == e:
            p2e4tight_order4base[p] = e
    p2e4tight_order4base
    tight_order4base = II__p2e_(p2e4tight_order4base)
    return tight_order4base if not to_factorization4mul_order else p2e4tight_order4base

    ##################
    #old:
    ##################
    #.p2e4tight_order4base = {}
    #.p2e4c = {}
    #.c = 1
    #.# [c == II__p2e_(p2e4c)]
    #.B = pt7base
    #.o4B = slack_order4base
    #.# [B == pt7base**c]
    #.# [0 == o4B%mul_order_of_(B)]
    #.# [o4B == slack_order4base///c]
    #.it = iter(sorted(factorization4slack_order4base.items()))
    #.for p, ep in it:
    #.    # [c == II__p2e_(p2e4c)]
    #.    # [B == pt7base**c]
    #.    # [o4B == slack_order4base///c]
    #.    t = p**ep
    #.    s = perfect_div(o4B, t)
    #.    e = sf.mul_order_of__7cyclic_group7slack_order4base_is_prime_power_(p, ep, t, pow_(B, s), to_log_p_mul_order=True)
    #.    if not 0 == e:
    #.        p2e4tight_order4base[p] = e
    #.    ########################
    #.    p2e4c[p] = ep
    #.    c *= t
    #.    B = pow_(B, t)
    #.    o4B = s
    #.    # [c == II__p2e_(p2e4c)]
    #.    # [B == pt7base**c]
    #.    # [o4B == slack_order4base///c]
    #.    ########################
    #.    if eq_one_(B):
    #.        break
    #.    ########################
    #.else:
    #.    assert c == slack_order4base
    #.    assert p2e4c == factorization4slack_order4base
    #.    assert eq_one_(B)

    #.p2e4tight_order4base
    #.tight_order4base = II__p2e_(p2e4tight_order4base)
    #.return tight_order4base if not to_factorization4mul_order else p2e4tight_order4base


@_method_
def mul_order_of__7cyclic_group7baby_steps_giant_steps_method_(sf, max4tight_order4base, pt7base, /):
    '[?[e:<-[1..=max4tight_order4base]] -> [G.one == pt7base**e]] => max4tight_order4base/int{>0} -> pt7base/G -> tight_order4base/int{>0} # [G.one == pt7base**tight_order4base][@[e:<-[1..<tight_order4base]] -> [G.one =!= pt7base**e]]'
    return sf.discrete_logarithm__7cyclic_group7baby_steps_giant_steps_method_(max4exp:=max4tight_order4base, pt7base, pt7tgt:=sf.one, max4exp__vs__tight_order4base=False)
@_method_
def discrete_logarithm__7cyclic_group7baby_steps_giant_steps_method_(sf, max4exp, pt7base, pt7tgt, /, *, max4exp__vs__tight_order4base:bool):
    '[[max4exp__vs__tight_order4base is True] -> [max4exp==mul_order_of_(pt7base)]][?[e:<-[1..=max4exp]] -> [pt7tgt == pt7base**e]] => max4exp/int{>0} -> pt7base/G -> pt7tgt/G -> exp/int{>0} # [pt7tgt == pt7base**exp][@[e:<-[1..<exp]] -> [pt7tgt =!= pt7base**e]]'
    eq_one_ = sf.eq_one_
    eq_ = sf.eq_
    if max4exp__vs__tight_order4base:
        tight_order4base = max4exp
        if eq_one_(pt7tgt):
            return tight_order4base
    if eq_(pt7tgt, pt7base):
        return 1
    sz4giant_step = calc_min4sz4giant_step5max4order4base_(max4exp)
    mul_ = sf.mul_
    pow_ = sf.pow_
    key = sf.key_func
    hash_vs_sort = sf.hash_vs_sort
    return search_mul_order__7baby_steps_giant_steps_method_(sz4giant_step, mul_, pow_, pt7base, key=key, hash_vs_sort=hash_vs_sort, tmay_target=[pt7tgt])

@_method_
def discrete_logarithm__7cyclic_group7tight_order4base_is_prime_(sf, tight_order4base, pt7base, pt7tgt, /):
    '[tight_order4base == mul_order_of_(pt7base)][?[e:<-[1..=tight_order4base]] -> [pt7tgt == pt7base**e]] => tight_order4base/prime -> pt7base/G -> pt7tgt/G -> exp/int{>0} # [pt7tgt == pt7base**exp][@[e:<-[1..<exp]] -> [pt7tgt =!= pt7base**e]]'
    eq_one_ = sf.eq_one_
    if eq_one_(pt7tgt):
        return tight_order4base
    return sf.discrete_logarithm__7cyclic_group7baby_steps_giant_steps_method_(max4exp:=tight_order4base, pt7base, pt7tgt, max4exp__vs__tight_order4base=True)

@_method_
def discrete_logarithm__7cyclic_group7tight_order4base_is_prime_power_(sf, p, ep, tight_order4base, pt7base, pt7tgt, /):
    '[tight_order4base == mul_order_of_(pt7base)][?[e:<-[1..=tight_order4base]] -> [pt7tgt == pt7base**e]] => p/prime -> ep/uint -> tight_order4base/int{>0}{==p**ep} -> pt7base/G -> pt7tgt/G -> exp/int{>0} # [pt7tgt == pt7base**exp][@[e:<-[1..<exp]] -> [pt7tgt =!= pt7base**e]]'
    check_int_ge(2, p)
    check_int_ge(0, ep)
    check_int_ge(1, tight_order4base)
    assert (lbP:=p.bit_length())*ep >= tight_order4base.bit_length() >= (lbP-1)*ep
    assert tight_order4base == p**ep
    eq_one_ = sf.eq_one_
    eq_ = sf.eq_
    if eq_one_(pt7tgt):
        return tight_order4base
    if eq_(pt7tgt, pt7base):
        return 1
    # [pt7tgt =!= G.one]
    # [1 < mul_order_of_(pt7tgt)]
    # !! [0 == tight_order4base%mul_order_of_(pt7tgt)]
    # [1 < tight_order4base]
    # [pt7base =!= G.one]


    mul_ = sf.mul_
    pow_ = sf.pow_
    ########################
    e2pw = [pt7tgt]
        # ~ {e:pt7tgt**(p**e)}
    for e in range(1, 1+ep):
        if eq_one_(e2pw[-1]):break
        e2pw.append(pow_(e2pw[-1], p))
    if not eq_one_(e2pw[-1]):raise ValueError('[pt7tgt**(p**ep) =!= G.one]', p, ep, pt7tgt)
    assert 1 <= len(e2pw) <= 1+ep
    ########################
    e2pw7p = [1]
    for e in range(1, 1+ep):
        e2pw7p.append(e2pw7p[-1] * p)
    assert len(e2pw7p) == 1+ep
    ########################
    ########################
    L = len(e2pw)
    # [pt7tgt**(p**(-1+L)) == G.one]
    # [mul_order_of_(pt7tgt) == (p**(-1+L))]
    # [0 == exp%p**(ep+1-L)]
    # [gde_(p;exp) == (ep+1-L)]

    ep0 = (ep+1-L)
    exp0 = e2pw7p[ep0] # == p**ep0
    # [exp0 == p**ep0 == p**(ep+1-L)]
    # [0 == exp%exp0]
    ########################
    B = pow_(pt7base, exp0)
    e2pw7b = [B]
    for e in range(1+ep0, 1+ep):
        if eq_one_(e2pw7b[-1]):raise ValueError('[pt7base**(p**(e-1)) == G.one][1<=e<=ep]', p, ep, e-1, pt7base)
        e2pw7b.append(pow_(e2pw7b[-1], p))
    if not eq_one_(e2pw7b[-1]):raise ValueError('[pt7base**(p**ep) =!= G.one]', p, ep, pt7base)
    assert 1 <= len(e2pw7b) == L <= 1+ep

    ########################
    # !! [pt7base =!= G.one]
    assert L >= 2
    B2 = e2pw7b[-2]
    ########################
    it = zip(reversed(range(L)), reversed(e2pw))
    for e, pw in it:
        # [0 <= e <= L-1]
        # [0 <= L-1-e]
        assert (L-1-e) >= 0
        assert e == L-1, (e, L, e2pw)
        _exp = 0
        patch = sf.one
        ##################
        # [_exp == (exp///exp0)%p**(L-1-e)]
        # [patch == B**-_exp]
        ##################
        assert 0 <= _exp < e2pw7p[(L-1-e)]
        break
    for e, pw in it:
        # [pw == pt7tgt**(p**e)]
        # [0 <= e <= L-2]
        # [0 <= L-2-e]
        assert (L-2-e) >= 0
        ##################
        # [_exp == (exp///exp0)%p**(L-1-old_e)]
        # [patch == B**-_exp]
        ##################
        # !! [e == -1+old_e]
        # [_exp == (exp///exp0)%p**(L-2-e)]
        assert 0 <= _exp < e2pw7p[(L-2-e)]
        # !! [pt7tgt == pt7base**exp == B**(exp///exp0)]
        # [pw == pt7tgt**(p**e) == B**(exp///exp0 * p**e %p**(ep-ep0))]
        # [pw == (B**(p**e))**((exp///exp0) %p**(ep-ep0-e))]
        # !! [ep0 == (ep+1-L)]
        # [pw == e2pw7b[e]**((exp///exp0) %p**(L-1-e))]
        # !! [_exp == (exp///exp0)%p**(L-2-e)]
        # [pw == e2pw7b[e]**((exp///exp0) //p**(L-2-e) %p *p**(L-2-e) + _exp)]
        _pw = mul_(pw, pow_(patch, e2pw7p[e]))
        # !! [patch == B**-_exp]
        # [pow_(patch, p**e) == e2pw7b[e]**-exp]
        # [_pw == e2pw7b[e]**((exp///exp0) //p**(L-2-e) %p *p**(L-2-e))]
        # [_pw == e2pw7b[L-2]**((exp///exp0) //p**(L-2-e) %p)]
        digit = sf.discrete_logarithm__7cyclic_group7tight_order4base_is_prime_(p, B2, _pw)
        assert 1 <= digit <= p
        digit %= p # fixed bug
        assert 0 <= digit < p
        # [digit == ((exp///exp0) //p**(L-2-e) %p)]
        ##################
        # !! [0 <= L-2-e]
        _exp7new = _exp + digit*e2pw7p[(L-2-e)] if not 0==digit else _exp
        # [_exp7new == _exp + digit*p**(L-2-e)]
        # !! [_exp == (exp///exp0)%p**(L-2-e)]
        # [_exp7new == (exp///exp0)%p**(L-2-e) + digit*p**(L-2-e)]
        # [_exp7new == (exp///exp0)%p**(L-1-e)]
        patch7new = mul_(patch, pow_(e2pw7b[(L-2-e)], -digit)) if not 0==digit else patch
        # !! [patch == B**-_exp]
        # [patch7new == B**-_exp * (B**(p**(L-2-e)))**-digit]
        # [patch7new == B**-_exp * B**(p**(L-2-e)*-digit)]
        # [patch7new == B**-(_exp +p**(L-2-e)*digit)]
        # [patch7new == B**-_exp7new]
        ##################
        # [_exp7new == (exp///exp0)%p**(L-1-e)]
        # [patch7new == B**-_exp7new]
        _exp = _exp7new
        patch = patch7new
        # [_exp == (exp///exp0)%p**(L-1-e)]
        # [patch == B**-_exp]
        ##################
        assert 0 <= _exp < e2pw7p[(L-1-e)]
            # fixed bug: 『digit %= p』
    if 1:
        ##################
        # [_exp == (exp///exp0)%p**(L-1-e)]
        # [patch == B**-_exp]
        ##################
        assert e == 0
        # [_exp == (exp///exp0)%p**(L-1)]
        assert 0 <= _exp < e2pw7p[(L-1)]
        # !! [exp0 == p**ep0 == p**(ep+1-L)]
        # [_exp*exp0 == exp%p**(L-1+ep0) == exp%p**(L-1+(ep+1-L))]
        # [_exp*exp0 == exp%p**ep]
        # !! [1 <= exp <= p**ep]
        # [exp == p**ep if _exp==0 else _exp*exp0]
        exp = e2pw7p[ep] if _exp==0 else _exp*exp0
        assert 1 <= exp <= e2pw7p[ep] == tight_order4base, (1, exp, e2pw7p[ep], tight_order4base)
        # !! [patch == B**-_exp]
        # [patch == (pt7base**exp0)**-_exp == pt7base**-exp == pt7tgt**-1]
        # [patch*pt7tgt == G.one]
        assert eq_one_(mul_(patch, pt7tgt))
        assert eq_(pt7tgt, pow_(pt7base, exp))
    exp
    ########################
    return exp
    ########################

@_method_
def discrete_logarithm__7cyclic_group7factorization4tight_order4base_(sf, factorization4tight_order4base, tight_order4base, pt7base, pt7tgt, /):
    '[tight_order4base == mul_order_of_(pt7base)][?[e:<-[1..=tight_order4base]] -> [pt7tgt == pt7base**e]] => factorization4tight_order4base/{p/prime:ep/uint{>0}} -> tight_order4base/int{>0}{==II__p2e_(factorization4tight_order4base)} -> pt7base/G -> pt7tgt/G -> exp/int{>0} # [pt7tgt == pt7base**exp][@[e:<-[1..<exp]] -> [pt7tgt =!= pt7base**e]]'
    check_int_ge(1, tight_order4base)
    assert tight_order4base == II__p2e_(factorization4tight_order4base)

    eq_one_ = sf.eq_one_
    eq_ = sf.eq_
    if eq_one_(pt7tgt):
        return tight_order4base
    if eq_(pt7tgt, pt7base):
        return 1
    # [pt7tgt =!= G.one]
    pow_ = sf.pow_

    ##################
    #new:
    ##################
    j2pe = sorted(factorization4tight_order4base.items())
    pts7B = _pow_except1_(eq_one_, pow_, j2pe, pt7base)
    pts7T = _pow_except1_(eq_one_, pow_, j2pe, pt7tgt)

    t_exp6t_pairs = []
    for (p, ep), pt7B, pt7T in zip(j2pe, pts7B, pts7T):
        # [pt == pt7base**(slack_order4base///p**ep)]
        t = p**ep
        exp6t = sf.discrete_logarithm__7cyclic_group7tight_order4base_is_prime_power_(p, ep, t, pt7B, pt7T)
        assert 1 <= exp6t <= t
        t_exp6t_pairs.append((t, exp6t%t))
    t_exp6t_pairs
    exp = apply_CRT__pairs(t_exp6t_pairs, extended=False)
    if exp == 0:
        exp = tight_order4base
        # [pt7tgt == G.one]
        # !! [pt7tgt =!= G.one]
        raise 000
    assert 1 <= exp <= tight_order4base
    assert eq_(pt7tgt, pow_(pt7base, exp))
    return exp

    ##################
    #old:
    ##################
    #.t_exp6t_pairs = []
    #.p2e4c = {}
    #.c = 1
    #.# [c == II__p2e_(p2e4c)]
    #.T = pt7tgt
    #.B = pt7base
    #.o4B = tight_order4base
    #.# [T == pt7tgt**c]
    #.# [B == pt7base**c]
    #.# [o4B == mul_order_of_(B)]
    #.# [o4B == tight_order4base///c]
    #.it = iter(sorted(factorization4tight_order4base.items()))
    #.for p, ep in it:
    #.    # [c == II__p2e_(p2e4c)]
    #.    # [T == pt7tgt**c]
    #.    # [B == pt7base**c]
    #.    # [o4B == tight_order4base///c]
    #.    t = p**ep
    #.    s = perfect_div(o4B, t)
    #.    # !! [exp6t == discrete_logarithm_((base**s), (tight_order4base///s);(power**s))] # [formula__calc_partial_discrete_logarithm_]:goto
    #.    exp6t = sf.discrete_logarithm__7cyclic_group7tight_order4base_is_prime_power_(p, ep, t, pow_(B, s), pow_(T, s))
    #.    assert 1 <= exp6t <= t
    #.    t_exp6t_pairs.append((t, exp6t%t))
    #.    ########################
    #.    p2e4c[p] = ep
    #.    c *= t
    #.    T = pow_(T, t)
    #.    B = pow_(B, t)
    #.    o4B = s
    #.    # [c == II__p2e_(p2e4c)]
    #.    # [T == pt7tgt**c]
    #.    # [B == pt7base**c]
    #.    # [o4B == tight_order4base///c]
    #.    ########################
    #.    if eq_one_(T):
    #.        t_exp6t_pairs.extend((p**ep,0) for p, ep in it)
    #.        break
    #.    if eq_(T, B):
    #.        #t_exp6t_pairs.extend((p**ep,1) for p, ep in it)
    #.        #t_exp6t_pairs.append((II__p2e_(dict(it)), 1))
    #.        t_exp6t_pairs.append((o4B, 1))
    #.        break
    #.    ########################
    #.else:
    #.    assert c == tight_order4base
    #.    assert p2e4c == factorization4tight_order4base
    #.    assert eq_one_(T)
    #.    assert eq_one_(B)

    #.t_exp6t_pairs
    #.exp = apply_CRT__pairs(t_exp6t_pairs, extended=False)
    #.if exp == 0:
    #.    exp = tight_order4base
    #.    # [pt7tgt == G.one]
    #.    # !! [pt7tgt =!= G.one]
    #.    raise 000
    #.assert 1 <= exp <= tight_order4base
    #.assert eq_(pt7tgt, pow_(pt7base, exp))
    #.return exp

@_method_
def partial_discrete_logarithm__7cyclic_group7factorization4part4tight_order4base_(sf, factorization4t, t, tight_order4base, pt7base, pt7tgt, /):
    '[tight_order4base == mul_order_of_(pt7base)][?[e:<-[1..=tight_order4base]] -> [pt7tgt == pt7base**e]] => factorization4t/{p/prime:ep/uint{>0}} -> t/uint{>0}{==II__p2e_(factorization4t)} -> tight_order4base/int{>0}{[0==tight_order4base%t][1==gcd(t,tight_order4base///t)]} -> pt7base/G -> pt7tgt/G -> exp6t/int{>0}{==exp%t if not 0==exp%t else t} # [pt7tgt == pt7base**exp][@[e:<-[1..<exp]] -> [pt7tgt =!= pt7base**e]]'
    check_int_ge(1, t)
    check_int_ge(1, tight_order4base)
    assert t == II__p2e_(factorization4t)
    s = perfect_div(tight_order4base, t)
    #assert 1 == gcd(s, t)
    assert all(not 0 == s%p for p in factorization4t)

    #.p2e4t = complete_factor_pint_via_trial_division(sorted(factorization4tight_order4base), t)

    pow_ = sf.pow_
    # !! [exp6t == discrete_logarithm_((base**s), (tight_order4base///s);(power**s))] # [formula__calc_partial_discrete_logarithm_]:goto
    exp6t = sf.discrete_logarithm__7cyclic_group7factorization4tight_order4base_(factorization4t, t, pow_(pt7base, s), pow_(pt7tgt, s))
    assert 1 <= exp6t <= t
    #exp6t %= t
    return exp6t



class PowsRepr:
    '[modulus,tight_order4base::int{>0}][0==tight_order4base%modulus][residue::uint%modulus] => [es := {residue%modulus +d*modulus | [sz:=tight_order4base///modulus][d:<-[0..<sz]]}][PowsRepr(pt7base, tight_order4base, modulus, residue) ~ pt7base .**: es]'
    def __init__(sf, pt7base, tight_order4base, modulus, residue, /):
        check_int_ge(1, tight_order4base)
        check_int_ge(1, modulus)
        check_uint_lt(modulus, residue)
        sz = perfect_div(tight_order4base, modulus)
        es = range(residue%modulus, tight_order4base, modulus)
        assert len(es) == sz
        sf._b = pt7base
        sf._es = es
    @property
    def base(sf, /):
        return sf._b
    @property
    def exps(sf, /):
        return sf._es
    @property
    def tight_order4base(sf, /):
        return sf.exps.stop
    @property
    def modulus(sf, /):
        return sf.exps.step
    @property
    def residue(sf, /):
        return sf.exps.start
    @property
    def args(sf, /):
        return (sf.base, sf.tight_order4base, sf.modulus, sf.residue)
    def __len__(sf, /):
        return len(sf.exps)
    def __repr__(sf, /):
        return repr_helper(sf, *sf.args)

NoKthRootError

@_method_
def repr_kth_roots4unity7cyclic_group_(sf, k, tight_order4base, pt7base, /, *, validate=False):
    '[tight_order4base == mul_order_of_(pt7base)] => k/int{=!=0} -> tight_order4base/int{>0} -> pt7base/G -> (pt7root/G, sz/int{>0}{==gcd(k, tight_order4base)}, PowsRepr(pt7base, tight_order4base, modulus:=tight_order4base///sz, residue:=0)) # [pt7root**k == G.one][mul_order_of_(pt7root) == gcd(k, tight_order4base)]'
    check_type_is(int, k)
    assert not k == 0
    check_int_ge(1, tight_order4base)
    eq_one_ = sf.eq_one_
    pow_ = sf.pow_
    # !! [kth_roots4unity7cyclic_group_(base, tight_order4base;k) =[def]= let [g:=gcd(k,tight_order4base)] in base .**: mods6mod_(tight_order4base,(tight_order4base///g);0)] # [formula__kth_roots4unity7cyclic_group_]:goto
    sz = g = gcd(k, tight_order4base)
    modulus = step = perfect_div(tight_order4base, sz)
    pt7root = pow_(pt7base, step)
    if validate:
        assert eq_one_(pow_(pt7root, k))
        assert eq_one_(pow_(pt7root, g))
        assert sz == (_sz:=sf.mul_order_of__7cyclic_group7baby_steps_giant_steps_method_(max4tight_order4pt7root:=g, pt7root)), (sz, _sz)
    pows_repr = PowsRepr(pt7base, tight_order4base, modulus, residue:=0)
    return (pt7root, sz, pows_repr)

@_method_
def repr_kth_roots7cyclic_group_(sf, factorization4gcd_k_tight_order4base, gcd_k_tight_order4base, k, tight_order4base, pt7base, pt7tgt, /):
    '[tight_order4base == mul_order_of_(pt7base)][?[e:<-[1..=tight_order4base]] -> [pt7tgt == pt7base**e]] => factorization4gcd_k_tight_order4base/{prime:int{>0}} -> gcd_k_tight_order4base/int{>0}{==gcd(k, tight_order4base)}{==II__p2e_(factorization4gcd_k_tight_order4base)} -> k/int{=!=0} -> tight_order4base/int{>0} -> pt7base/G -> pt7tgt/G -> ((pt7root/G, ((pt7tgt, e4tgt/uint), (pt7base_pow, e4base_pow/uint))) if [G.one == pt7tgt**(tight_order4base///gcd_k_tight_order4base)] else ^NoKthRootError) # [pt7root**k == pt7tgt][pt7root == (pt7tgt**e4tgt * pt7base_pow**e4base_pow)]'

    if 0:
        r'''[[[
        exp = sf.discrete_logarithm__7cyclic_group7factorization4tight_order4base_(factorization4tight_order4base, tight_order4base, pt7base, pt7tgt)
        if not 0==exp%gcd_k_tight_order4base:
            raise NoKthRootError(k, tight_order4base, pt7base, pt7tgt, exp, gcd_k_tight_order4base)
        g = gcd_k_tight_order4base
        eg = perfect_div(exp, g)
        kg = perfect_div(k, g)
        og = perfect_div(tight_order4base, g)
        return pow_(pt7base, eg*pow(kg, -1, og) %og)
        #]]]'''#'''

    check_int_ge(1, tight_order4base)
    check_type_is(int, k)
    assert not k == 0
    check_int_ge(1, gcd_k_tight_order4base)
    assert gcd_k_tight_order4base == II__p2e_(factorization4gcd_k_tight_order4base)

    ######################
    pow_ = sf.pow_
    (s, t) = decompose_coprime_part_(k, tight_order4base)
    gcd_k_t = gcd_k_tight_order4base
    factorization4t = complete_factor_pint_via_trial_division(sorted(factorization4gcd_k_tight_order4base), t)
    # [v := t**-1%s]
    # [u := (1-t*v)///s]
    v = pow(t, -1, s)
    u = perfect_div(1-t*v, s)
    assert 1 == s*u + t*v

    s2 = perfect_div(k, gcd_k_t)
    t2 = perfect_div(tight_order4base, gcd_k_t)
    v2 = pow(t2, -1, s2)
    u2 = perfect_div(1-t2*v2, s2)
    assert 1 == s2*u2 + t2*v2

    pt7base_pow = pow_(pt7base, s)

    return sf.repr_kth_roots7cyclic_group__7low_level_(factorization4t, gcd_k_t, u2, v2, s, t, u, v, k, tight_order4base, pt7base_pow, pt7tgt)
        # ^NoKthRootError

@_method_
def repr_kth_roots7cyclic_group__7slack_order4base_pow_(sf, factorization4gcd_k_slack_order4base_pow, gcd_k_slack_order4base_pow, k, slack_order4base_pow, pt7base_pow, pt7tgt, /):
    # pseudo_base --> base_pow
    r'''[[[
    [precondition:
        [pt7tgt,pt7base_pow <- cyclic_group7generated_by(pt7base)]
        [G.one == pt7base_pow**slack_order4base_pow]
            # ==>> [0 == slack_order4base_pow%mul_order_of_(pt7base_pow)]
        [(pt7tgt**coprime_part_(k;slack_order4base_pow)) <- cyclic_group7generated_by(pt7base_pow)]
    ]
    => factorization4gcd_k_slack_order4base_pow/{prime:int{>0}}
    -> gcd_k_slack_order4base_pow/int{>0}{==gcd(k,slack_order4base_pow)}{==II__p2e_(factorization4gcd_k_slack_order4base_pow)}
    -> k/int{=!=0}
    -> slack_order4base_pow/int{>0}
    -> pt7base_pow/G
    -> pt7tgt/G
    -> ((pt7root/G, ((pt7tgt, e4tgt/uint), (pt7base_pow, e4base_pow/uint))) | ^NoKthRootError)

    #]]]'''#'''
    check_int_ge(1, slack_order4base_pow)
    check_type_is(int, k)
    assert not k == 0
    check_int_ge(1, gcd_k_slack_order4base_pow)
    assert gcd_k_slack_order4base_pow == II__p2e_(factorization4gcd_k_slack_order4base_pow)
    #assert 0 == k%gcd_k_slack_order4base_pow
    #assert 0 == slack_order4base_pow%gcd_k_slack_order4base_pow
    kg = perfect_div(k, gcd_k_slack_order4base_pow)
    og = perfect_div(slack_order4base_pow, gcd_k_slack_order4base_pow)
    #assert 1 == gcd(kg, og)
    ikg6og = pow(kg, -1, og)
    # [1 == gcd(kg, og)]

    ######################
    pow_ = sf.pow_

    (_s, _t) = decompose_coprime_part_(k, slack_order4base_pow)
    _pt7base_pow = pow_(pt7base_pow, _s)
    # [_pt7base_pow == pt7base_pow**_s]
    # !! [is_slack_order_of_(pt7base_pow, _s*_t)]
    # [is_slack_order_of_(_pt7base_pow, _t)]
    _p2e4t = complete_factor_pint_via_trial_division(factorization4gcd_k_slack_order4base_pow, _t)
    p2e4t = sf.mul_order_of__7cyclic_group7factorization4slack_order4base_(_p2e4t, _t, _pt7base_pow, to_factorization4mul_order=True)
    t = II__p2e_(p2e4t)
    # [t == mul_order_of_(_pt7base_pow)]
    factorization4t = p2e4t
    semi_tight_order4base = _s*t
    gcd_k_t = gcd(k, t)
    s = _s

    # [v := t**-1%s]
    # [u := (1-t*v)///s]
    v = pow(t, -1, s)
    u = perfect_div(1-t*v, s)
    assert 1 == s*u + t*v

    s2 = perfect_div(k, gcd_k_t)
    t2 = perfect_div(semi_tight_order4base, gcd_k_t)
    v2 = pow(t2, -1, s2)
    u2 = perfect_div(1-t2*v2, s2)
    assert 1 == s2*u2 + t2*v2


    # !! [(pt7tgt**coprime_part_(k;slack_order4base_pow)) <- cyclic_group7generated_by(pt7base_pow)]
    # [(pt7tgt**_s) <- cyclic_group7generated_by(pt7base_pow)]
    # [(pt7tgt**_s) <- cyclic_group7generated_by(pt7base_pow**_s)]
    # [(pt7tgt**_s) <- cyclic_group7generated_by(_pt7base_pow)]
    _pt7base_pow
    (pt7root, ((the__pt7tgt, e4tgt), (_the__pt7base_pow, _e4base_pow))) = sf.repr_kth_roots7cyclic_group__7low_level_(factorization4t, gcd_k_t, u2, v2, s, t, u, v, k, semi_tight_order4base, _pt7base_pow, pt7tgt)
    assert pt7tgt is the__pt7tgt
    assert _pt7base_pow is _the__pt7base_pow
    # !! [_pt7base_pow == pt7base_pow**_s]
    e4base_pow = _s*_e4base_pow
    return (pt7root, ((pt7tgt, e4tgt), (pt7base_pow, e4base_pow)))


@_method_
def repr_kth_roots7cyclic_group__7low_level_(sf, factorization4t, gcd_k_t, u2, v2, s, t, u, v, k, semi_tight_order4base, pt7base_pow, pt7tgt, /):
    r'''[[[
    [precondition:
        [0 == semi_tight_order4base%mul_order_of_(pt7base)]
        [1 == gcd(k, semi_tight_order4base///mul_order_of_(pt7base))]

        [pt7tgt,pt7base_pow <- cyclic_group7generated_by(pt7base)]

        [@[p:<-factorization4t] -> [0 == gcd_k_t%p]]
            # <==> [gcd_k_t =[:prime_factors:]= t]
        [0 == k%gcd_k_t][0 == t%gcd_k_t][1 == (k///gcd_k_t)*u2 + (semi_tight_order4base///gcd_k_t)*v2]
            # <==> [1 == gcd((k///gcd_k_t), (semi_tight_order4base///gcd_k_t))][1 == gcd((k///gcd_k_t), (t///gcd_k_t))]
            # <==> [gcd(k, semi_tight_order4base) == gcd_k_t == gcd(k, t)]
        [1 == s*u + t*v]
        [(s,t) := decompose_coprime_part_(k; semi_tight_order4base)]
            # ==>> [1==gcd(s,t)][s*t == semi_tight_order4base]
            # ==>> [1==gcd(s,k)][0 == k**t%t][@[p::prime][0==t%p] -> [0==k%p]]
            # ==>> [t =[:prime_factors:]= gcd(k,t) == gcd(k,semi_tight_order4base)]

        # s: slack_part{semi_tight_order4base}
        # t: tight_part{semi_tight_order4base}
        #    # so called "semi_tight_order4base"
        [t == mul_order_of_(pt7base_pow)]
            # <==> [?[r:<-[1..=semi_tight_order4base]] -> [1==gcd(r,semi_tight_order4base)][pt7base_pow == pt7base**(r*s)]]
            # ==>> [(pt7tgt**s) <- cyclic_group7generated_by(pt7base_pow)]
    ]
    => factorization4t/{prime:int{>0}}
    -> gcd_k_t/int{>0}{==gcd(k, t)}{==gcd(k, semi_tight_order4base)}
    -> u2/int
    -> v2/int
    -> s/int{>0}
    -> t/int{>0}{==II__p2e_(factorization4t)}
    -> u/int
    -> v/int
    -> k/int{=!=0}
    -> semi_tight_order4base/int{>0}
    -> pt7base_pow/G
    -> pt7tgt/G
    -> ((pt7root/G, ((pt7tgt, e4tgt/uint), (pt7base_pow, e4base_pow/uint))) if [G.one == (pt7tgt**s)**(t///gcd_k_t)] else ^NoKthRootError)
        # [G.one == (pt7tgt**s)**(t///gcd_k_t)] <==> [G.one == pt7tgt**(semi_tight_order4base///gcd_k_t)] <==> [0 == discrete_logarithm_(pt7base_pow;pt7tgt**s)%gcd_k_t]

    postcondition:
        [pt7root == (pt7tgt**e4tgt * pt7base_pow**e4base_pow)]
        [pt7root**k == pt7tgt]
            # see:repr_kth_roots4unity7cyclic_group_()
            #   [(pt7root*any_kth_root4unity{k})**k == pt7tgt]

    #]]]'''#'''
    # factorization4t, gcd_k_t, s, t, k, semi_tight_order4base, pt7base_pow, pt7tgt
    check_int_ge(1, gcd_k_t)
    check_type_is(int, k)
    assert not k == 0
    check_int_ge(1, s)
    check_int_ge(1, t)
    check_type_is(int, u)
    check_type_is(int, v)
    check_type_is(int, u2)
    check_type_is(int, v2)
    check_int_ge(1, semi_tight_order4base)
    assert s*t == semi_tight_order4base
    assert 1 == s*u + t*v
    # [1 == gcd(s,t)]

    assert t == II__p2e_(factorization4t)
    assert 0 == k%gcd_k_t
    assert 0 == t%gcd_k_t
    g7kbs9pw = gcd_k_t
    kg = perfect_div(k, g7kbs9pw)
    tg = perfect_div(t, g7kbs9pw)
    assert 1 == kg*u2 + (s*tg)*v2
    # [1 == kg*u2 + (s*tg)*v2]
    # [1 == gcd(k///gcd_k_t, s*t///gcd_k_t)]
    # [1 == gcd(k///gcd_k_t, semi_tight_order4base///gcd_k_t)]
    # [1 == gcd(k///gcd_k_t, t///gcd_k_t)]
    # [gcd_k_t == gcd(k, semi_tight_order4base)]
    # [gcd_k_t == gcd(k, t)]
    # [1 == gcd(k///gcd_k_t, s)]
    # !! [1 == gcd(s,t)]
    # [1 == gcd(gcd_k_t, s)]
    # [1 == gcd(k, s)]
    assert all(0 == gcd_k_t%p for p in factorization4t)
    # [gcd_k_t =[:prime_factors:]= t]
    # [t == noncoprime_part_(k;semi_tight_order4base)]
    # [s == coprime_part_(k;semi_tight_order4base)]

    eq_one_ = sf.eq_one_
    eq_ = sf.eq_
    mul_ = sf.mul_
    pow_ = sf.pow_


    # !! [criterion__has_kth_roots7cyclic_group_]:goto
    pt7tgt_pow = pow_(pt7tgt, s)
    if not eq_one_(pow_(pt7tgt_pow, perfect_div(t, gcd_k_t))):raise NoKthRootError(k, semi_tight_order4base, pt7base_pow, pt7tgt, (s, t, u, v), gcd_k_t)


    #exp6t = sf.partial_discrete_logarithm__7cyclic_group7factorization4part4tight_order4base_(factorization4t, t, semi_tight_order4base, pt7base, pt7tgt)

    # !! [exp6t == discrete_logarithm_((base**s), (tight_order4base///s);(power**s))] # [formula__calc_partial_discrete_logarithm_]:goto
    exp6t = sf.discrete_logarithm__7cyclic_group7factorization4tight_order4base_(factorization4t, t, pt7base_pow, pow_(pt7tgt, s))
        # !! [t == mul_order_of_(pt7base_pow)]
        # [?[r:<-[1..=semi_tight_order4base]] -> [1==gcd(r,semi_tight_order4base)][pt7base_pow == pt7base**(r*s)]]
        # [(pt7tgt**s) <- cyclic_group7generated_by(pt7base_pow)]
    assert 1 <= exp6t <= t

    ##################
    # neednot: [formula__kth_roots7cyclic_group7convert_to_strict_]:goto
    ##################
    #old:
    # !! [formula__kth_roots7cyclic_group7strict_]:goto
    #   [kth_roots7cyclic_group_(base, tight_order4base;k;power) == ((power**tg)**(v*kg**-1%s)) .*: ((base**s) .**: mods6mod_(t,tg; etg*u*kg**-1%tg))]
    ###########################
    #new:
    #   tight_order4base --> semi_tight_order4base
    # !! [formula__kth_roots7cyclic_group7strict__7semi_tight_order4base_]:goto
    #   [kth_roots7cyclic_group_(base, semi_tight_order4base;k;power) == ((power**tg)**(vc*kg**-1%sc *k)) .*: ((base**sc) .**: (k .*: mods6mod_(t,tg; etg*uc*kg**-1%tg)))]
    ###########################

    # [1 == s*u + t*v]
    # [exp6t := (exp%t)]
    # [g7kbs9pw := gcd(k,semi_tight_order4base)]
    etg = perfect_div(exp6t, g7kbs9pw)

    # !! [1 == kg*u2 + (s*tg)*v2]
    # [1 =[%(s*tg)]= kg*u2]
    # [kg**-1%(s*tg) == u2%(s*tg)]
    # [kg**-1%s == u2%s]
    # [kg**-1%tg == u2%tg]
    ikg6s_tg = u2%(s*tg)
    ikg6s = ikg6s_tg%s
    ikg6tg = ikg6s_tg%tg
    #ikg6s = pow(kg, -1, s)
    #ikg6tg = pow(kg, -1, tg)
    assert 0 == (1-kg%s*ikg6s)%s
    assert 0 == (1-kg%tg*ikg6tg)%tg
    e4tgt = (v*ikg6s%s) *tg
    e4base_pow = (etg*u*ikg6tg%tg)
    pt7root = mul_(pow_(pt7tgt, e4tgt), pow_(pt7base_pow, e4base_pow))
    ##################
    assert e4tgt >= 0
    assert e4base_pow >= 0
    assert eq_(pt7tgt, pow_(pt7root, k))
    return (pt7root, ((pt7tgt, e4tgt), (pt7base_pow, e4base_pow)))
    ##################




























__all__
from seed.math.discrete_logarithm__7cyclic_group7kth_roots import IGroupOps7discrete_logarithm7kth_root, IGroupOps7discrete_logarithm7kth_root__7uint_mod, GroupOps7discrete_logarithm7kth_root__7uint_mod

from seed.math.discrete_logarithm__7cyclic_group7kth_roots import NoKthRootError, PowsRepr

from seed.math.discrete_logarithm__7cyclic_group7kth_roots import decompose_coprime_part_, noncoprime_part_, coprime_part_

from seed.math.discrete_logarithm__7cyclic_group7kth_roots import (IGroupOps7discrete_logarithm7kth_root
,   mul_order_of__7cyclic_group7baby_steps_giant_steps_method_
,   mul_order_of__7cyclic_group7slack_order4base_is_prime_power_
,   mul_order_of__7cyclic_group7factorization4slack_order4base_
#
,   discrete_logarithm__7cyclic_group7baby_steps_giant_steps_method_
,   discrete_logarithm__7cyclic_group7tight_order4base_is_prime_
,   discrete_logarithm__7cyclic_group7tight_order4base_is_prime_power_
,   discrete_logarithm__7cyclic_group7factorization4tight_order4base_
,   partial_discrete_logarithm__7cyclic_group7factorization4part4tight_order4base_
#
,   repr_kth_roots4unity7cyclic_group_
,   repr_kth_roots7cyclic_group_
,   repr_kth_roots7cyclic_group__7slack_order4base_pow_
,   repr_kth_roots7cyclic_group__7low_level_
#
)



from seed.math.discrete_logarithm__7cyclic_group7kth_roots import *
