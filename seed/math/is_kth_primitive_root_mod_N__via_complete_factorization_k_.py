#__all__:goto
r'''[[[
e ../../python3_src/seed/math/is_kth_primitive_root_mod_N__via_complete_factorization_k_.py
copy from:
    view ../../python3_src/seed/math/find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_.py

seed.math.is_kth_primitive_root_mod_N__via_complete_factorization_k_
py -m nn_ns.app.debug_cmd   seed.math.is_kth_primitive_root_mod_N__via_complete_factorization_k_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.is_kth_primitive_root_mod_N__via_complete_factorization_k_:__doc__ -ht # -ff -df

[[
]]



>>> def f(factorization_of_k, N, /):
...     ver2bs = [[is_kth_primitive_root_mod_N__via_complete_factorization_k_(None, factorization_of_k, N, r, _ver=_ver) for r in range(N)] for _ver in range(3)]
...     ok = (ver2bs[0] == ver2bs[1] == ver2bs[2])
...     roots = [r for r, b in enumerate(ver2bs[2]) if b]
...     return (ok, len(roots), roots)
...     return (ver2bs[0] == ver2bs[1], ver2bs[0] == ver2bs[2], ver2bs[2] == ver2bs[1])
...     assert ver2bs[0] == ver2bs[1], (ver2bs[0], ver2bs[1])
...     assert ver2bs[0] == ver2bs[2], (ver2bs[0], ver2bs[2])
...     return ver2bs[2]
>>> f({2:3,3:2,5:1}, 297)
(True, 0, [])
>>> f({2:1}, 297)
(True, 3, [109, 188, 296])
>>> f({3:1}, 297)
(True, 2, [100, 199])
>>> f({5:1}, 297)
(True, 4, [82, 136, 163, 190])
>>> f({2:3}, 297)
(True, 0, [])
>>> f({3:2}, 297)
(True, 6, [34, 67, 133, 166, 232, 265])


>>> 1+360*5
1801
>>> 27*41
1107
>>> f({2:3,3:2,5:1}, 1107)
(True, 192, [7, 11, 13, 22, 29, 34, 47, 52, 56, 58, 65, 67, 70, 76, 88, 94, 95, 97, 101, 104, 106, 110, 112, 130, 140, 142, 149, 151, 157, 158, 175, 176, 193, 194, 211, 212, 218, 220, 227, 229, 239, 257, 259, 263, 265, 268, 272, 274, 275, 281, 293, 299, 302, 304, 311, 313, 317, 322, 335, 340, 347, 356, 358, 362, 376, 380, 382, 391, 398, 403, 416, 421, 425, 427, 434, 436, 439, 445, 457, 463, 464, 466, 470, 473, 475, 479, 481, 499, 509, 511, 518, 520, 526, 527, 544, 545, 562, 563, 580, 581, 587, 589, 596, 598, 608, 626, 628, 632, 634, 637, 641, 643, 644, 650, 662, 668, 671, 673, 680, 682, 686, 691, 704, 709, 716, 725, 727, 731, 745, 749, 751, 760, 767, 772, 785, 790, 794, 796, 803, 805, 808, 814, 826, 832, 833, 835, 839, 842, 844, 848, 850, 868, 878, 880, 887, 889, 895, 896, 913, 914, 931, 932, 949, 950, 956, 958, 965, 967, 977, 995, 997, 1001, 1003, 1006, 1010, 1012, 1013, 1019, 1031, 1037, 1040, 1042, 1049, 1051, 1055, 1060, 1073, 1078, 1085, 1094, 1096, 1100])


>>> f({2:3,3:2,5:1}, 1801)
(True, 96, [22, 26, 95, 97, 118, 123, 133, 152, 173, 174, 188, 195, 205, 264, 269, 273, 275, 276, 287, 290, 312, 325, 326, 334, 337, 374, 385, 391, 406, 442, 455, 496, 498, 539, 549, 557, 573, 613, 637, 661, 684, 704, 711, 762, 797, 822, 832, 837, 964, 969, 979, 1004, 1039, 1090, 1097, 1117, 1140, 1164, 1188, 1228, 1244, 1252, 1262, 1303, 1305, 1346, 1359, 1395, 1410, 1416, 1427, 1464, 1467, 1475, 1476, 1489, 1511, 1514, 1525, 1526, 1528, 1532, 1537, 1596, 1606, 1613, 1627, 1628, 1649, 1668, 1678, 1683, 1704, 1706, 1775, 1779])



>>> f({2:1}, 1107)
(True, 3, [163, 944, 1106])
>>> f({3:1}, 1107)
(True, 2, [370, 739])
>>> f({5:1}, 1107)
(True, 4, [379, 406, 838, 1000])
>>> f({2:3}, 1107)
(True, 8, [55, 109, 161, 325, 782, 946, 998, 1052])
>>> f({3:2}, 1107)
(True, 6, [124, 247, 493, 616, 862, 985])


>>> f({2:1}, 1801)
(True, 1, [1800])
>>> f({3:1}, 1801)
(True, 2, [73, 1727])
>>> f({5:1}, 1801)
(True, 4, [32, 350, 394, 1024])
>>> f({2:3}, 1801)
(True, 4, [464, 524, 1277, 1337])
>>> f({3:2}, 1801)
(True, 6, [144, 150, 888, 925, 1507, 1789])





py_adhoc_call   seed.math.is_kth_primitive_root_mod_N__via_complete_factorization_k_   @is_kth_primitive_root_mod_N__via_complete_factorization_k_
]]]'''#'''
__all__ = r'''
is_kth_primitive_root_mod_N__via_complete_factorization_k_
    check_kth_primitive_root_mod_N__via_complete_factorization_k_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.math.II import II, II__p2e_
from seed.tiny_.check import check_type_is, check_int_ge, check_uint_lt
from seed.iters.apply_commutative_operations_except_one import iter_apply_commutative_operations_except_one_
#def iter_apply_commutative_operations_except_one_(apply_, commutative_operation_keys, x0, /):
    # :: (k->x->x) -> [k] -> x -> (iter x)
    # :: apply_/(k->x->x) -> keys/[k] -> x0/x -> xs/(iter x){xs[i] == (II<mul=(.)> (apply_ keys[j]) {j :<- [0..<len(keys)] | [j=!=i]})(x0)}

___end_mark_of_excluded_global_names__0___ = ...

def check_kth_primitive_root_mod_N__via_complete_factorization_k_(may_k, factorization_of_k, N, r, /, *, _ver=2):
    'may k/int{>=1} -> factorization{k} -> N/int{>=2} -> r/uint%N -> None if [k==min_order_mod_(N;r)] else ^ValueError'
    if not is_kth_primitive_root_mod_N__via_complete_factorization_k_(may_k, factorization_of_k, N, r, _ver=_ver):raise ValueError(may_k, factorization_of_k, N, r)

def _k5factorization_of_k_ex_(factorization_of_k, may_k, /):
    k = II__p2e_(factorization_of_k) if may_k is None else may_k
    return k
def is_kth_primitive_root_mod_N__via_complete_factorization_k_(may_k, factorization_of_k, N, r, /, *, _ver=2):
    'may k/int{>=1} -> factorization{k} -> N/int{>=2} -> r/uint%N -> bool/[k==min_order_mod_(N;r)]'
    check_int_ge(2, N)
    check_uint_lt(N, r)
    # [0 <= r < N]
    for q, e in factorization_of_k.items():
        check_int_ge(2, q)
        check_int_ge(1, e)
    k = _k5factorization_of_k_ex_(factorization_of_k, may_k)
    check_int_ge(1, k)

    if k == 1:
        return r==1
    # [k >= 2]
    assert factorization_of_k
    # [len(qs) >= 1]
    if r <= 1:
        return False
    # [2 <= r < N]
    II_q = II(q for q in factorization_of_k)
    e0 = k//II_q
    _k = e0 * II_q
    assert _k == k
    #II_qmm = II(q-1 for q in factorization_of_k)
    #phi_k = e0 * II_qmm
    q_e_pairs = sorted(factorization_of_k.items())
    assert q_e_pairs
        # !! [k >= 2]
    # [len(qs) >= 1]

    (k, q_e_pairs, N, r)
    # [2 <= r < N]
    # [k >= 2]
    # [len(qs) >= 1]
    f = _fs[_ver]
    return f(k, q_e_pairs, N, r)
def _is_kth_primitive_root_mod_N__via_complete_factorization_k__naive_(k, q_e_pairs, N, r, /):
    # [2 <= r < N]
    # [k >= 2]
    # [len(qs) >= 1]
    return pow(r, k, N) == 1 and all(pow(r, k//q, N) != 1 for q, _ in q_e_pairs)
_is_kth_primitive_root_mod_N__via_complete_factorization_k__ver0_ = _is_kth_primitive_root_mod_N__via_complete_factorization_k__naive_
def _is_kth_primitive_root_mod_N__via_complete_factorization_k__ver1_(k, q_e_pairs, N, r, /):
    # [2 <= r < N]
    # [k >= 2]
    # [len(qs) >= 1]
    if 1:
        g = r
        # !! [2 <= r < N]
        # [2 <= g < N]
        #base0 = pow(g, e0, N)
        base0 = g
        # [base0 =!= 1]
        for q, e in q_e_pairs:
            for _ in range(e-1):
                base0 = pow(base0, q, N)
                if base0 == 1:
                    return False
        assert not base0 == 1
        # [base0 == pow(g, k///II(qs), N)]
        # [base0 =!= 1]
        # [base0 == pow(g, k///II(qs[0:]), N)]
        ls = [base0]
        # [ls[0] == pow(g, k///II(qs[0:]), N)]
        for j, (q, _) in enumerate(q_e_pairs):
            # [ls[j] == pow(g, k///II(qs[j:]), N)]
            if ls[-1] == 1:
                return False
            ls.append(pow(ls[-1], q, N))
            # [ls[j+1] == pow(g, k///II(qs[j+1:]), N)]
        else:
            # [@[j:<-[0..<len(ls)]] -> [ls[j] == pow(g, k///II(qs[j:]), N)]]
            assert len(ls) == 1+len(q_e_pairs)
            # [len(ls)==1+len(qs)]
            # [@[j:<-[0..=len(qs)]] -> [ls[j] == pow(g, k///II(qs[j:]), N)]]
            # [ls[-1] == pow(g,k,N)]
            if not ls[-1] == 1:
                # [pow(g,k,N) =!= 1]
                return False
            # [pow(g,k,N) == 1]

        for i in range(len(q_e_pairs)):
            # [0 <= i < len(qs) == len(ls)-1]
            # [0 <= i <= len(qs)-1 == len(ls)-2]
            #base1 = pow(g, k//q, N)
            base1 = ls[i]
            # [base1 == ls[i] == pow(g, k///II(qs[i:]), N) =!= ls[-1] == 1]
            # [base1 =!= 1]
            assert not base1 == 1
            for q, _ in q_e_pairs[i+1:]:
                base1 = pow(base1, q, N)
                if base1 == 1:
                    return False
            # [base1 == pow(g, k///qs[i], N)]
            # [base1 =!= 1]
    return True
def _is_kth_primitive_root_mod_N__via_complete_factorization_k__ver2_(k, q_e_pairs, N, r, /):
    # [2 <= r < N]
    # [k >= 2]
    # [len(qs) >= 1]
    if 1:
        g = r
        # !! [2 <= r < N]
        # [2 <= g < N]
        #base0 = pow(g, e0, N)
        base0 = g
        # [base0 =!= 1]
        for q, e in q_e_pairs:
            for _ in range(e-1):
                base0 = pow(base0, q, N)
                if base0 == 1:
                    return False
        assert not base0 == 1
        # [base0 == pow(g, k///II(qs), N)]
        # [base0 =!= 1]
        # [base0 == pow(g, k///II(qs[0:]), N)]
        def apply_(q, gg, /):
            return pow(gg, q, N)
        qs = [q for q, _ in q_e_pairs]
        commutative_operation_keys = qs
        return all(gg != 1 and (j>0 or apply_(qs[0], gg)==1) for j, gg in enumerate(iter_apply_commutative_operations_except_one_(apply_, commutative_operation_keys, base0)))
_fs = (
[_is_kth_primitive_root_mod_N__via_complete_factorization_k__ver0_
,_is_kth_primitive_root_mod_N__via_complete_factorization_k__ver1_
,_is_kth_primitive_root_mod_N__via_complete_factorization_k__ver2_
])
#end-is_kth_primitive_root_mod_N__via_complete_factorization_k_



__all__
from seed.math.is_kth_primitive_root_mod_N__via_complete_factorization_k_ import check_kth_primitive_root_mod_N__via_complete_factorization_k_
#def check_kth_primitive_root_mod_N__via_complete_factorization_k_(may_k, factorization_of_k, N, r, /, *, _ver=2):
#    'may k/int{>=1} -> factorization{k} -> N/int{>=2} -> r/uint%N -> None if [k==min_order_mod_(N;r)] else ^ValueError'

from seed.math.is_kth_primitive_root_mod_N__via_complete_factorization_k_ import is_kth_primitive_root_mod_N__via_complete_factorization_k_
#def is_kth_primitive_root_mod_N__via_complete_factorization_k_(may_k, factorization_of_k, N, r, /, *, _ver=2):
#   'may k/int{>=1} -> factorization{k} -> N/int{>=2} -> r/uint%N -> bool/[k==min_order_mod_(N;r)]'

if 1:from seed.math.is_kth_primitive_root_mod_N__via_complete_factorization_k_ import _is_kth_primitive_root_mod_N__via_complete_factorization_k__ver2_
#def _is_kth_primitive_root_mod_N__via_complete_factorization_k__ver2_(k, q_e_pairs, N, r, /):
    # [2 <= r < N]
    # [k >= 2]
    # [len(qs) >= 1]
from seed.math.is_kth_primitive_root_mod_N__via_complete_factorization_k_ import *
