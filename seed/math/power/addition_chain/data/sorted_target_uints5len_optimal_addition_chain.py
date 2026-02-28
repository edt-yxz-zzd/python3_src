#__all__:goto
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/data/sorted_target_uints5len_optimal_addition_chain.py

seed.math.power.addition_chain.data.sorted_target_uints5len_optimal_addition_chain
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.data.sorted_target_uints5len_optimal_addition_chain -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.data.sorted_target_uints5len_optimal_addition_chain:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> len(最小显链长讠靶值列表)
22
>>> 最小显链长讠靶值列表.最大靶值牜可用
100000
>>> 最小显链长讠靶值列表.最小靶值牜溢出
100001
>>> 最小显链长讠靶值列表[:3]
((1,), (2,), (3, 4))
>>> 最小显链长讠靶值列表[:6]
((1,), (2,), (3, 4), (5, 6, 8), (7, 9, 10, 12, 16), (11, 13, 14, 15, 17, 18, 20, 24, 32))
>>> 最小显链长讠靶值列表.截取乊扌(最小显链长:=5, 1, 100001)
(11, 13, 14, 15, 17, 18, 20, 24, 32)
>>> 最小显链长讠靶值列表.截取乊扌(最小显链长:=5, 1, 11)
()
>>> 最小显链长讠靶值列表.截取乊扌(最小显链长:=5, 1, 12)
(11,)
>>> 最小显链长讠靶值列表.截取乊扌(最小显链长:=5, 1, 13)
(11,)
>>> 最小显链长讠靶值列表.截取乊扌(最小显链长:=5, 1, 14)
(11, 13)
>>> 最小显链长讠靶值列表.截取乊扌(最小显链长:=5, 16, 19)
(17, 18)
>>> 最小显链长讠靶值列表.截取乊扌(最小显链长:=5, 17, 19)
(17, 18)
>>> 最小显链长讠靶值列表.截取乊扌(最小显链长:=5, 17, 18)
(17,)
>>> 最小显链长讠靶值列表.截取乊扌(最小显链长:=5, 17, 17)
()

py_adhoc_call   seed.math.power.addition_chain.data.sorted_target_uints5len_optimal_addition_chain   @f
]]]'''#'''
__all__ = r'''
乸最小显链长讠靶值列表
    最小显链长讠靶值列表
        sorted_target_uints5len_optimal_addition_chain

'''.split()#'''
#.max_target_uint4known_data4len_optimal_addition_chain
#.    最大靶值纟丮最小显链长讠靶值列表厈
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
from bisect import bisect_left #bisect_right
___end_mark_of_excluded_global_names__0___ = ...

def _import():
    from seed.math.power.addition_chain.data.target_uint2may_len_optimal_addition_chain import target_uint2may_len_optimal_addition_chain, 靶值讠最小显链长
    return 靶值讠最小显链长

def _归组制表冫最小显链长讠靶值列表扌(靶值序列=None, 靶值讠最小显链长=None, /):
    if 靶值讠最小显链长 is None:
        靶值讠最小显链长 = _import()
    if 靶值序列 is None:
        靶值序列 = range(1, len(靶值讠最小显链长))
    最小显链长讠靶值列表 = []
    for 靶值 in 靶值序列:
        最小显链长 = 靶值讠最小显链长[靶值]
        最小显链长讠靶值列表.extend([] for _ in range(len(最小显链长讠靶值列表), 1+最小显链长))
        最小显链长讠靶值列表[最小显链长].append(靶值)
    最小显链长讠靶值列表 = tuple(map(tuple, 最小显链长讠靶值列表))
    return 最小显链长讠靶值列表

class 乸最小显链长讠靶值列表:
    def __init__(sf, 鬽丮靶值讠最小显链长厈=None, /):
        靶值讠最小显链长 = _import() if 鬽丮靶值讠最小显链长厈 is None else 鬽丮靶值讠最小显链长厈
        if not type(靶值讠最小显链长) is tuple:
            靶值讠最小显链长 = tuple(靶值讠最小显链长)
            鬽丮靶值讠最小显链长厈 = 靶值讠最小显链长
        最小显链长讠靶值列表 = _归组制表冫最小显链长讠靶值列表扌(靶值序列:=None, 靶值讠最小显链长)
        sf._靶值讠最小显链长 = 靶值讠最小显链长
        sf._最大靶值牜可用 = -1+len(靶值讠最小显链长)
        sf._最小靶值牜溢出 = len(靶值讠最小显链长)
        sf._最小显链长讠靶值列表 = 最小显链长讠靶值列表
    def __len__(sf, /):
        return len(sf.最小显链长讠靶值列表)
    def __repr__(sf, /):
        return f'乸最小显链长讠靶值列表({sf.靶值讠最小显链长})'
    @property
    def 最小显链长讠靶值列表(sf, /):
        return sf._最小显链长讠靶值列表
    @property
    def 最小靶值牜溢出(sf, /):
        return sf._最小靶值牜溢出
    @property
    def 最大靶值牜可用(sf, /):
        return sf._最大靶值牜可用
    @property
    def 靶值讠最小显链长(sf, /):
        return sf._靶值讠最小显链长
    def __getitem__(sf, k, /):
        return sf.最小显链长讠靶值列表[k]
    def 定位乊扌(sf, 最小显链长, 靶值左闭边界列表, /):
        'uint -> strict_sorted[pint] -> exindices/[uint]'
        assert 最小显链长 >= 0
        靶值左闭边界列表 = list(靶值左闭边界列表)
        assert 靶值左闭边界列表 == sorted(靶值左闭边界列表)
        if 靶值左闭边界列表:
            assert 靶值左闭边界列表[0] >= 1
            assert 靶值左闭边界列表[-1] <= sf.最小靶值牜溢出
            assert all(map(int.__lt__, 靶值左闭边界列表, 靶值左闭边界列表[1:]))
        靶值列表 = sf.最小显链长讠靶值列表[最小显链长]
        起址列表 = []
        起址 = 0
        for 靶值左闭边界 in 靶值左闭边界列表:
            起址 = bisect_left(靶值列表, 靶值左闭边界, 起址)
            起址列表.append(起址)
            #bug:起址 += 1
            #   !! 可能[讫址==起址]
        起址列表 = tuple(起址列表)
        return 起址列表
    def 截取乊扌(sf, 最小显链长, 靶值左闭边界, 靶值右开边界, /):
        'uint -> uint -> uint -> exindices/[uint]'
        if not 靶值右开边界 <= sf.最小靶值牜溢出:raise ValueError(靶值右开边界)
            #.靶值右开边界 = min(sf.最小靶值牜溢出, 靶值右开边界)
        靶值左闭边界 = max(1, 靶值左闭边界)
        if not 靶值左闭边界 < 靶值右开边界:
            return ()
        # strict_sorted[靶值左闭边界, 靶值右开边界]
        (起址, 讫址) = sf.定位乊扌(最小显链长, [靶值左闭边界, 靶值右开边界])
        靶值列表 = sf.最小显链长讠靶值列表[最小显链长]
        return 靶值列表[起址:讫址]


#.max_target_uint4known_data4len_optimal_addition_chain = \
#.最大靶值纟丮最小显链长讠靶值列表厈 = -1+len(_import())
#.sorted_target_uints5len_optimal_addition_chain = \
#.最小显链长讠靶值列表 = _归组制表冫最小显链长讠靶值列表扌()
#.
#.assert 最大靶值纟丮最小显链长讠靶值列表厈 == 10**5

sorted_target_uints5len_optimal_addition_chain = \
最小显链长讠靶值列表 = 乸最小显链长讠靶值列表()
assert 最小显链长讠靶值列表.最大靶值牜可用 == 10**5


__all__
#.from seed.math.power.addition_chain.data.sorted_target_uints5len_optimal_addition_chain import sorted_target_uints5len_optimal_addition_chain, max_target_uint4known_data4len_optimal_addition_chain, 最小显链长讠靶值列表, 最大靶值纟丮最小显链长讠靶值列表厈
from seed.math.power.addition_chain.data.sorted_target_uints5len_optimal_addition_chain import sorted_target_uints5len_optimal_addition_chain, 最小显链长讠靶值列表 # .最大靶值牜可用 .最小靶值牜溢出
from seed.math.power.addition_chain.data.sorted_target_uints5len_optimal_addition_chain import *
