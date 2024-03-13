#__all__:goto
r'''[[[
e ../../python3_src/seed/math/generate_partition4additive_semigroup__total_ordering__increasing.py
    view ../../python3_src/seed/math/iter_sorted_products_of_uints.py
    view ../../python3_src/seed/for_libs/for_heapq.py
vs:
    view ../../python3_src/seed/math/cut_uint_into_uints.py



seed.math.generate_partition4additive_semigroup__total_ordering__increasing
py -m nn_ns.app.debug_cmd   seed.math.generate_partition4additive_semigroup__total_ordering__increasing -x
py -m nn_ns.app.doctest_cmd seed.math.generate_partition4additive_semigroup__total_ordering__increasing:__doc__ -ff -v


[[
source:
view ../../python3_src/seed/math/iter_sorted_products_of_uints.py

source:
view ../../python3_src/script/finger_tree_ops.py
    concat(*finger_trees)
    <<==:
    big_node_seq5node_seq(node_seq):
        '[Node<k>] -> [Node<k+1>]'
        [len(node_seq) >= 2]
        (q,r) = divmod(len(node_seq),3)
        [[r==1] -> [q >= 1]]
        case r of
            0 -> 3*q+2*0
            1 -> 3*(q-1)+2*2
            2 -> 3*q+2*1
    ######################
    (2,3)-finger_tree:
        Tree<k> =[def]= (Digits<k>,Tree<k+1>,Digits<k>) | Seed<k>
        Seed<k> =[def]= [Node<k>]{len<-{0,1}}
        Digits<k> =[def]= [Node<k>]{len<-{1,2}}
        Node<0> =[def]= Value
        Node<k+1> =[def]= [Node<k>]{len<-{2,3}}
    ######################

]]

[[
partition 分拆
    分拆vs拆分
generate_partition4additive_semigroup__total_ordering__increasing
additive semigroup total ordering
    generate/span via sorted generators#maybe infinite
        e.g. G = (coprimes, mul)
        e.g. G = (set<pint>, add)
            finger_tree
                view ../../python3_src/script/finger_tree_ops.py
            concat finger_trees --> cut nodes into node groups
            ###
            generate until a continuous section of len=min_generator since exists partition: %min_generator into this continuous section

    add-operation:
        commutative
        associative
        strict monotone increasing
            [a < a+b] # [a == a+0] but [not$ 0 <- G]
            [[b < c] -> [a+b < a+c]]
    分拆-->tmay 极大前驱
        [分拆 :: {生成元:重复次数}]
        [重复次数 :: 正整数]
        [分拆基元数 := sum(分拆.values())]
        [分拆基元数 >= 1]
        [all_delta_set = {min_generator} \-/ {generators[i+1]-generators[i] | [i :<- [0..]]}]
        [all_delta_set<partition> = {min_generator} \-/ {generators[i+1]-generators[i] | [[i :<- [0..]][generators[i] == min(map fst partition)][partition[generators[i]] == 1]]}]
        [len(all_delta_set<partition>) <- {1,2}]
            至少一个后继
            至多两个后继
            [partition+++{2:1} <- successors_of_(partition)]
            [(generators[i],1) == min(partition.items())]:
                [partition---{generators[i]:1}+++{generators[i+1]:1} <- successors_of_(partition)]

        [『孤粒轰击积聚自堵塞』枚举法 ==>> [任意元素有一两个后继][除开最小生成元，其他元素有且只有一个前驱][枚举生成的元素可能重复，但每个分拆都唯一]]
            # 互素素数+乘法 ==>> 枚举生成的元素唯一
            # 多个正整数+加法 ==>> 枚举生成的元素重复
        ############
        e.g. G = ({2,3,4,5}, add)
            [7/{2:1,5:1} --> 5/{5:1} --> 4/{4:1} ...]
            [7/{3:1,4:1} --> 6/{2:1,4:1} --> 4/{4:1} ...]
            [7/{2:2,3:1} --> 5/{2:1,3:1} --> 3/{3:1} ...]
            [4/{4:1} --> 3/{3:1} --> 2/{2:1} --> Nothing]
            ############
            [9/{4:1,5:1} --> 8/{3:1,5:1} --> 7/{2:1,5:1} ...]
            [9/{2:2,5:1} --> 7/{2:1,5:1} ...]
            [9/{2:1,3:1,4:1} --> 7/{3:1,4:1} ...]
            [9/{2:3,3:1} --> 7/{2:2,3:1} ...]
            [9/{3:3} --> 8/{2:1,3:2} --> 6/{3:2} --> 5/{2:1,3:1} ...]
            ############
            2/{2:1}:
            --4/{2:2}:--6/{2:3}:--8/{2:4}:...
            --3/{3:1}:
            ----5/{2:1,3:1}:
            ------7/{2:2,3:1}:--9/{2:3,3:1}:--11/{2:4,3:1}:...
            ------6/{3:2}:--8/{2:1,3:2}:
            ----------9/{3:3}:
            ------------....
            ----------10/{2:2,3:2}:
            ------------....
            ----4/{4:1}:
            ------6/{2:1,4:1}:
            --------....
            ------5/{5:1}:
            --------....
            ############
        ######################
        #过气:
        # * [分拆基元数 == 1]:
        #     [分拆 == {生成元:1}]
        #     [分拆 ~ 生成元]
        #     * 最小生成元 没有极大前驱
        #     * 非最小生成元 的 极大前驱 为 小于它的极大生成元
        # * [分拆基元数 > 1]:
        #     [分拆 的 极大前驱 == 分拆{其中最小生成元 的 重复次数 减一}]
        #         e.g. G = ({2,3,4,5}, add)
        #             [7/{2:1,5:1} --> 5/{5:1} --> 4/{4:1}]
        #             [7/{3:1,4:1} --> 4/{4:1}]
        #             [4/{4:1} --> 3/{3:1} --> 2/{2:1} --> Nothing]
    分拆: 其中最小生成元g + 相应极大前驱的分拆囗囗生成元大于等于囗(g)
        #并非 极大前驱 的所有分拆都有效，只有那些 [最小生成元 >= g] 才有用。
    最优分拆择取策略『取大优先』: 首要 分拆基元数 越少越好; 次要 分拆基元数 相同下 为尽可能符合 贪婪算法 分拆中最大生成元 越大越好 相应重复次数 越大越好 相同 则 依次考虑 其余生成元 及 相应重复次数。
        收集器...
]]

[[
antisymmetric,transitive:
view ../lots/NOTE/Types and Programming Languages (2002)(Benjamin C. Pierce)/preordered set.u8

irreflexive:
view ../lots/NOTE/The Art of Multiprocessor Programming/linearizability.txt
]]




py_adhoc_call   seed.math.generate_partition4additive_semigroup__total_ordering__increasing   ,30:generate4additive_semigroup__total_ordering__increasing_ =[3,7]
py_adhoc_call   seed.math.generate_partition4additive_semigroup__total_ordering__increasing   ,4:generate4additive_semigroup__total_ordering__increasing_ =[3,7]

py_adhoc_call   seed.math.generate_partition4additive_semigroup__total_ordering__increasing   ,30:generate4additive_semigroup__total_ordering__increasing_ =[3,7] --__add__:__mul__ +to_ensure_single_jpartition_per_element
py_adhoc_call   seed.math.generate_partition4additive_semigroup__total_ordering__increasing   ,30:generate4additive_semigroup__total_ordering__increasing_ =[3,7] --__add__:__add__ +to_export_all_partitions

>>> from seed.iters.apply_may_args4islice_ import list_islice_, show_islice_, stable_show_islice_, stable_list_islice_
>>> show_islice_(30, generate4additive_semigroup__total_ordering__increasing_([3,7]))
(3, ((0, 1),), 3)
(6, ((0, 2),), 6)
(7, ((1, 1),), 7)
(9, ((0, 3),), 9)
(10, ((1, 1), (0, 1)), 10)
(12, ((0, 4),), 12)
(13, ((1, 1), (0, 2)), 13)
(14, ((1, 2),), 14)
(15, ((0, 5),), 15)
(16, ((1, 1), (0, 3)), 16)
(17, ((1, 2), (0, 1)), 17)
(18, ((0, 6),), 18)
(19, ((1, 1), (0, 4)), 19)
(20, ((1, 2), (0, 2)), 20)
(21, ((1, 3),), 21)
(22, ((1, 1), (0, 5)), 22)
(23, ((1, 2), (0, 3)), 23)
(24, ((1, 3), (0, 1)), 24)
(25, ((1, 1), (0, 6)), 25)
(26, ((1, 2), (0, 4)), 26)
(27, ((1, 3), (0, 2)), 27)
(28, ((1, 4),), 28)
(29, ((1, 2), (0, 5)), 29)
(30, ((1, 3), (0, 3)), 30)
(31, ((1, 4), (0, 1)), 31)
(32, ((1, 2), (0, 6)), 32)
(33, ((1, 3), (0, 4)), 33)
(34, ((1, 4), (0, 2)), 34)
(35, ((1, 5),), 35)
(36, ((1, 3), (0, 5)), 36)
>>> show_islice_(30, generate4additive_semigroup__total_ordering__increasing_([3,7], __add__='__mul__'))
(3, ((0, 1),), 3)
(7, ((1, 1),), 7)
(9, ((0, 2),), 9)
(21, ((1, 1), (0, 1)), 21)
(27, ((0, 3),), 27)
(49, ((1, 2),), 49)
(63, ((1, 1), (0, 2)), 63)
(81, ((0, 4),), 81)
(147, ((1, 2), (0, 1)), 147)
(189, ((1, 1), (0, 3)), 189)
(243, ((0, 5),), 243)
(343, ((1, 3),), 343)
(441, ((1, 2), (0, 2)), 441)
(567, ((1, 1), (0, 4)), 567)
(729, ((0, 6),), 729)
(1029, ((1, 3), (0, 1)), 1029)
(1323, ((1, 2), (0, 3)), 1323)
(1701, ((1, 1), (0, 5)), 1701)
(2187, ((0, 7),), 2187)
(2401, ((1, 4),), 2401)
(3087, ((1, 3), (0, 2)), 3087)
(3969, ((1, 2), (0, 4)), 3969)
(5103, ((1, 1), (0, 6)), 5103)
(6561, ((0, 8),), 6561)
(7203, ((1, 4), (0, 1)), 7203)
(9261, ((1, 3), (0, 3)), 9261)
(11907, ((1, 2), (0, 5)), 11907)
(15309, ((1, 1), (0, 7)), 15309)
(16807, ((1, 5),), 16807)
(19683, ((0, 9),), 19683)
>>> list_islice_(30, iter_strict_sorted_elements4additive_semigroup__total_ordering__increasing_([3,7]))
[3, 6, 7, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
>>> list_islice_(30, iter_strict_sorted_elements4additive_semigroup__total_ordering__increasing_([3,7], __add__='__mul__', to_ensure_single_jpartition_per_element=True))
[3, 7, 9, 21, 27, 49, 63, 81, 147, 189, 243, 343, 441, 567, 729, 1029, 1323, 1701, 2187, 2401, 3087, 3969, 5103, 6561, 7203, 9261, 11907, 15309, 16807, 19683]

>>> list_islice_(30, iter_strict_sorted_elements4additive_semigroup__total_ordering__increasing_([3,27], __add__='__add__'))
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90]
>>> 3*30
90
>>> list_islice_(10, iter_strict_sorted_elements4additive_semigroup__total_ordering__increasing_([3,27], __add__='__mul__'))
[3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]
>>> 3**10
59049
>>> show_islice_(30, generate4additive_semigroup__total_ordering__increasing_([3,27]))
(3, ((0, 1),), 3)
(6, ((0, 2),), 6)
(9, ((0, 3),), 9)
(12, ((0, 4),), 12)
(15, ((0, 5),), 15)
(18, ((0, 6),), 18)
(21, ((0, 7),), 21)
(24, ((0, 8),), 24)
(27, ((1, 1),), 27)
(30, ((1, 1), (0, 1)), 30)
(33, ((1, 1), (0, 2)), 33)
(36, ((1, 1), (0, 3)), 36)
(39, ((1, 1), (0, 4)), 39)
(42, ((1, 1), (0, 5)), 42)
(45, ((1, 1), (0, 6)), 45)
(48, ((1, 1), (0, 7)), 48)
(51, ((1, 1), (0, 8)), 51)
(54, ((1, 2),), 54)
(57, ((1, 2), (0, 1)), 57)
(60, ((1, 2), (0, 2)), 60)
(63, ((1, 2), (0, 3)), 63)
(66, ((1, 2), (0, 4)), 66)
(69, ((1, 2), (0, 5)), 69)
(72, ((1, 2), (0, 6)), 72)
(75, ((1, 2), (0, 7)), 75)
(78, ((1, 2), (0, 8)), 78)
(81, ((1, 3),), 81)
(84, ((1, 3), (0, 1)), 84)
(87, ((1, 3), (0, 2)), 87)
(90, ((1, 3), (0, 3)), 90)
>>> show_islice_(30, generate4additive_semigroup__total_ordering__increasing_([3,27], to_export_all_partitions=True))
(3, (((0, 1),),), 3)
(6, (((0, 2),),), 6)
(9, (((0, 3),),), 9)
(12, (((0, 4),),), 12)
(15, (((0, 5),),), 15)
(18, (((0, 6),),), 18)
(21, (((0, 7),),), 21)
(24, (((0, 8),),), 24)
(27, (((1, 1),), ((0, 9),)), 27)
(30, (((1, 1), (0, 1)), ((0, 10),)), 30)
(33, (((1, 1), (0, 2)), ((0, 11),)), 33)
(36, (((1, 1), (0, 3)), ((0, 12),)), 36)
(39, (((1, 1), (0, 4)), ((0, 13),)), 39)
(42, (((1, 1), (0, 5)), ((0, 14),)), 42)
(45, (((1, 1), (0, 6)), ((0, 15),)), 45)
(48, (((1, 1), (0, 7)), ((0, 16),)), 48)
(51, (((1, 1), (0, 8)), ((0, 17),)), 51)
(54, (((1, 2),), ((1, 1), (0, 9)), ((0, 18),)), 54)
(57, (((1, 2), (0, 1)), ((1, 1), (0, 10)), ((0, 19),)), 57)
(60, (((1, 2), (0, 2)), ((1, 1), (0, 11)), ((0, 20),)), 60)
(63, (((1, 2), (0, 3)), ((1, 1), (0, 12)), ((0, 21),)), 63)
(66, (((1, 2), (0, 4)), ((1, 1), (0, 13)), ((0, 22),)), 66)
(69, (((1, 2), (0, 5)), ((1, 1), (0, 14)), ((0, 23),)), 69)
(72, (((1, 2), (0, 6)), ((1, 1), (0, 15)), ((0, 24),)), 72)
(75, (((1, 2), (0, 7)), ((1, 1), (0, 16)), ((0, 25),)), 75)
(78, (((1, 2), (0, 8)), ((1, 1), (0, 17)), ((0, 26),)), 78)
(81, (((1, 3),), ((1, 2), (0, 9)), ((1, 1), (0, 18)), ((0, 27),)), 81)
(84, (((1, 3), (0, 1)), ((1, 2), (0, 10)), ((1, 1), (0, 19)), ((0, 28),)), 84)
(87, (((1, 3), (0, 2)), ((1, 2), (0, 11)), ((1, 1), (0, 20)), ((0, 29),)), 87)
(90, (((1, 3), (0, 3)), ((1, 2), (0, 12)), ((1, 1), (0, 21)), ((0, 30),)), 90)
>>> show_islice_(10, generate4additive_semigroup__total_ordering__increasing_([3,27], to_ensure_single_jpartition_per_element=True))
Traceback (most recent call last):
    ...
seed.math.generate_partition4additive_semigroup__total_ordering__increasing.ValildFail__not_unique_jpartition_per_element: (27, [(27, ((((1, 1),), 27), ())), (27, ((((0, 9),), 27), ((((0, 8),), 24), ((((0, 7),), 21), ((((0, 6),), 18), ((((0, 5),), 15), ((((0, 4),), 12), ((((0, 3),), 9), ((((0, 2),), 6), ((((0, 1),), 3), ()))))))))))])




>>> search_max_miss_ex__pint_additive_generators_([])
Traceback (most recent call last):
    ...
seed.math.generate_partition4additive_semigroup__total_ordering__increasing.Error__generators_gcd_not_eq1: []
>>> search_max_miss_ex__pint_additive_generators_([4,6])
Traceback (most recent call last):
    ...
seed.math.generate_partition4additive_semigroup__total_ordering__increasing.Error__generators_gcd_not_eq1: [4, 6]
>>> search_max_miss_ex__pint_additive_generators_([-3,4,6])
Traceback (most recent call last):
    ...
TypeError
>>> search_max_miss_ex__pint_additive_generators_([3,4,6], uint_count__vs__pint_count=True)
(5, (6, 9), (3, 4, 6), ((0, 0, 1), (1, 1, 0), (0, 2, 0)))
>>> search_max_miss_ex__pint_additive_generators_([1], uint_count__vs__pint_count=True)
(0, (1, 2), (1,), ((1,),))
>>> search_max_miss_ex__pint_additive_generators_([7,11], uint_count__vs__pint_count=True)
(59, (60, 67), (7, 11), ((7, 1), (4, 3), (1, 5), (9, 0), (6, 2), (3, 4), (0, 6)))

>>> search_max_miss_ex__pint_additive_generators_([3,4,6], uint_count__vs__pint_count=False)
(5, (6, 9), (3, 4, 6), (((2, 1),), ((1, 1), (0, 1)), ((1, 2),)))
>>> search_max_miss_ex__pint_additive_generators_([1], uint_count__vs__pint_count=False)
(0, (1, 2), (1,), (((0, 1),),))
>>> search_max_miss_ex__pint_additive_generators_([7,11], uint_count__vs__pint_count=False)
(59, (60, 67), (7, 11), (((1, 1), (0, 7)), ((1, 3), (0, 4)), ((1, 5), (0, 1)), ((0, 9),), ((1, 2), (0, 6)), ((1, 4), (0, 3)), ((1, 6),)))

>>> search_max_miss_ex__pint_additive_generators_([3,4,6], may_max_begin=6)
(5, (6, 9), (3, 4, 6), (((2, 1),), ((1, 1), (0, 1)), ((1, 2),)))
>>> search_max_miss_ex__pint_additive_generators_([3,4,6], may_max_begin=5)
False






>>> max_miss_ex_7_11 = search_max_miss_ex__pint_additive_generators_([7,11])
>>> partition_pint4max_miss_ex__pint_additive_generators_(max_miss_ex_7_11, 59)
Traceback (most recent call last):
    ...
TypeError
>>> partition_pint4max_miss_ex__pint_additive_generators_(max_miss_ex_7_11, 60)
((1, 1), (0, 7))
>>> partition_pint4max_miss_ex__pint_additive_generators_(max_miss_ex_7_11, 70)
((0, 10),)
>>> partition_pint4max_miss_ex__pint_additive_generators_(max_miss_ex_7_11, 71)
((1, 2), (0, 7))
>>> partition_pint4max_miss_ex__pint_additive_generators_(max_miss_ex_7_11, 78)
((1, 2), (0, 8))

>>> max_miss_ex_3_4_6 = search_max_miss_ex__pint_additive_generators_([3,4,6])
>>> partition_pint4max_miss_ex__pint_additive_generators_(max_miss_ex_3_4_6, 6)
((2, 1),)
>>> partition_pint4max_miss_ex__pint_additive_generators_(max_miss_ex_3_4_6, 17)
((2, 1), (1, 2), (0, 1))


#]]]'''
__all__ = r'''
iter_strict_sorted_elements4additive_semigroup__total_ordering__increasing_
    generate4additive_semigroup__total_ordering__increasing_
ValildFail__not_unique_jpartition_per_element



search_max_miss_ex__pint_additive_generators_
    Error__generators_gcd_not_eq1
    partition_pint4max_miss_ex__pint_additive_generators_

'''.split()#'''
__all__



from seed.iters.ensure_sorted import ensure_strict_sorted
#def ensure_strict_sorted(iterable, /, *, key=None, __lt__=None, reverse=False, on_error=None, __le__=None, with_key=False):

from seed.tiny import check_type_is, fst, snd, at
######################
from seed.for_libs.for_heapq import heappushs_, heappops_, heapify, heappush, heappop, heappushpop, heappoppush, heapreplace
from seed.for_libs.for_heapq import Heap, std____key__le__reverse_
#class Heap:
#    def __init__(sf, heap, /, *, item5obj_, item2val_, key, __le__, reverse, obj_vs_item, applied__heapify):
######################
#  seed.types.Heap (py.heapq) donot support kwd:__le__ ==>> using seed.for_libs.for_heapq instead
#  #from seed.types.Heap import Heap, HeapWithKey
#  #class Heap(IHeap):
#  #    def __init__(self, iterable, *
#  #            , sorted=False, copy=False, are_heap_items=True
#  #            , obj2item=None, item2obj=None):
#  #class HeapWithKey(IHeap):
#  #    def __init__(self, obj2key, iterable, *
#  #            , sorted=False, copy=True, are_heap_items=False):


from itertools import pairwise
import operator #__le__
from seed.tiny import ifNonef, ifNone, echo
from seed.tiny import check_type_is
from seed.tiny_.check import check_callable



def __():
  def default_partition_collector(j2k_g, k4x, x, /):
    # partition_collector
    may_ls = []
    def partition_collector4x(may_jpartition4x, /):
        nonlocal may_ls
        if may_ls is None:
            raise 000
        ls = may_ls
        if may_jpartition4x is None:

            may_ls = None
            info4x = ls
            return info4x
        jpartition4x = may_jpartition4x
        ls.append(jpartition4x)
        return None
    return partition_collector4x

class ValildFail__not_unique_jpartition_per_element(Exception):pass

def iter_strict_sorted_elements4additive_semigroup__total_ordering__increasing_(strict_sorted_generators, /, *, __add__=None, key=None, __le__=None, reverse=False, on_error=None, to_export_all_partitions=False, j2k_g=None, to_ensure_single_jpartition_per_element=False):
    'strict-sorted-Iter g -> Iter x'
    kwds = {**locals()}
    del kwds['strict_sorted_generators']
    it = generate4additive_semigroup__total_ordering__increasing_(strict_sorted_generators, **kwds)
    return map(at[-1], it)
def generate4additive_semigroup__total_ordering__increasing_(strict_sorted_generators, /, *, __add__=None, key=None, __le__=None, reverse=False, on_error=None, to_export_all_partitions=False, j2k_g=None, to_ensure_single_jpartition_per_element=False):#, partition_collector=None
    r'''[[[
    :: strict-sorted-Iter g -> Iter (k4x, jpartition4x, x)
    :: +to_export_all_partitions => strict-sorted-Iter g -> Iter (k4x, [jpartition4x], x)
        [g :: x]
        [k4x =[def]= k<x> :: k]
        [jpartition4x =[def]= jpartition<x> :: reversed_sorted[(j4g/uint, count/pint)]]
            #NOTE: remove [count==0]

    precondition:
        #xxx partition_collector :: j2k_g -> k4x -> x -> partition_collector4x/((jpartition4x -> None) +++ (None -> info4x))
            [j2k_g :: [(k4g, g)]]
            [(k4g, g) == j2k_g[j4g]]

        to_export_all_partitions :: bool
        j2k_g :: [(k4g, g)]
        strict_sorted_generators :: Iter<x>
            [[not$ reverse] -> [all(not __le__(key(b),key(a)) for a,b in parwise(strict_sorted_generators))]]
            [[reverse] -> [all(not __le__(key(b),key(a)) for b,a in parwise(strict_sorted_generators))]]

        key :: x -> k

        __le__ :: k -> k -> bool
            ######################
            [__le__ :: total_order]
            ######################
            [@[a :: k] -> [__le__(a,a)]]
                #reflexive
            [@[a,b :: k] -> [not$ __eq__(a,b)] -> [__le__(a,b)] -> [not$ __le__(b,a)]]
                #antisymmetric
                #   [eqv<__le__> === __eq__]
                [@[a,b :: k] -> [__le__(a,b)] -> [__le__(b,a)] -> [__eq__(a,b)]]
            [@[a,b,c :: k] -> [__le__(a,b)] -> [__le__(b,c)] -> [__le__(a,c)]]
                #transitive
            [@[a,b :: k] -> [not$ __le__(a,b)] -> [__le__(b,a)]]
                #total

        __add__<G> :: x -> x -> x
            [@[x,y :<- G] -> [__add__(x,y) <- G]]
                #closure
            [@[x,y :<- G] -> [__add__(x,y) == __add__(y,x)]]
                #commutative
            [@[x,y,z :<- G] -> [__add__(x,__add__(y,z)) == __add__(__add__(x,y),z)]]
                #associative
            [@[x,y :<- G] -> [not$ __le__(__add__(x,y), x)]]
                #strict_monotone_increasing__gtZERO
                #   [not$ x+y <= x]
                #   [x < x+y]
                #   [x+0 < x+y]
                #   [0 < y]
                #   [not$ 0 <- G]
            [@[x,y,z :<- G] -> [not$ __le__(z,y)] -> [not$ __le__(__add__(x,z),__add__(x,y))]]
                #strict_monotone_increasing__gtRHS
                #   [[y < z] -> [x+y < x+z]]
                #   !! [[a < b] -> [y < z] -> [a+y < a+z == z+a < z+b == b+z]]
                #   [[a < b] -> [y < z] -> [a+y < b+z]]
                #
                #   [x+y < x+z]:
                #       [z <= y]:
                #           [x+z <= x+y]
                #           !! [x+y <= x+z]
                #           _L
                #       [y < z]
                #   [[x+y < x+z] -> [y < z]]
                #       # [:backward_cancel]:here
                #
            ######################
            #does (-) well-defined??? [(x-a) < (y-b) < (z-c)]
            ???[[x+b < y+a] -> [y+c < z+b] -> [x+c < z+a]]???
            proof:
            [x+b < y+a][y+c < z+b]:
                [x+b + y+c < y+a + z+b]
                [x+c + y+b < y+b + z+a]
                !! [:backward_cancel]:goto
                [x+c < z+a]
            [[x+b < y+a] -> [y+c < z+b] -> [x+c < z+a]]
                # [(-) well-defined: compact total_order __le__, but not satisfy closure and other property, e.g. [(x-x) == 0 !<- G][(x-(x+y)) == -y !<- G]]
                # although (generators[i+1]-generators[i]) is not min, it is simplest protocol/『孤粒轰击积聚自堵塞』枚举法
                #


    #]]]'''#'''
    if type(__add__) is str:
        str4add = __add__
        if str4add.isidentifier():
            nm4add = __add__
            __add__ = getattr(operator, nm4add)
    __add__ = ifNone(__add__, operator.__add__)
    check_callable(__add__)
    #partition_collector = ifNone(partition_collector, default_partition_collector)
    #check_callable(partition_collector)
    check_type_is(bool, to_export_all_partitions)
    check_type_is(bool, to_ensure_single_jpartition_per_element)
    j2k_g = ifNone(j2k_g, [])
    if not len(j2k_g) == 0: raise TypeError
    j2k_g[:0]

    k5x_, le4k_, reverse = std____key__le__reverse_(key, __le__, reverse)
    iter_keyed_gs = ensure_strict_sorted(strict_sorted_generators, key=k5x_, __le__=le4k_, reverse=reverse, on_error=on_error, with_key=True)

    def kk5item_(item, /):
        k4x, lnkls__jp_x = item
        ((jpartition4x, x), lnkls__jp_x_) = lnkls__jp_x
        kk4x = k4x, jpartition4x
        return kk4x
    def le4kk_(lhs_kk, rhs_kk, /):
        k4x, jpartition4x = lhs_kk
        k4y, jpartition4y = rhs_kk
        if not le4k_(k4y, k4x):
            # [k4x < k4y]
            return True
        if not le4k_(k4x, k4y):
            # [k4y < k4x]
            return False
        # [k4x == k4y]

        # strategy to choose jpartition4x『取大优先』排序策略，与『reverse』无关，下面排除『reverse』的干扰。
        if reverse:
            return jpartition4x <= jpartition4y
        else:
            return jpartition4x >= jpartition4y
        #
    #j2k_g = [] #now, come from input
        # :: [(k4g, g)]
    ls = []
        # ###xxx :: [(k4x, jpartition4x, x)]
        # :: [(k4x, nonempty lnkls__jp_x)]
        # lnkls__jp_x :: lnkls<(jpartition4x, x)>
        # if x is not g: lnkls__jp_x<x> --> lnkls__jp_x<x_>
        # jpartition4x :: reversed_sorted[(j4g,count/pint)]
        # jpartition4x_ = jpartition4x[:-1]
        # x_ ~ jpartition4x_
        # lnkls__jp_x_ ~ (jpartition4x_, x_)
        #
    hp = Heap(ls, item5obj_=None, item2val_=None, key=kk5item_, __le__=le4kk_, reverse=reverse, obj_vs_item=False, applied__heapify=False)
    def try_add_next_g_(lnkls__jp_x_, min_j4g4x, /):
        nonlocal no_more_new_g
        next_j4min_g4x = min_j4g4x +1
        if next_j4min_g4x == len(j2k_g):
            assert not lnkls__jp_x_
            if no_more_new_g:
                return
            if not feed_new_g_():
                no_more_new_g = True
            return
        assert next_j4min_g4x < len(j2k_g)
        assert lnkls__jp_x_
        inc_at_(next_j4min_g4x, lnkls__jp_x_)
    def inc_at_(j4g, lnkls__jp_x, /):
        assert lnkls__jp_x
        if 0b00:print(f'inc_at_({j4g}, {lnkls__jp_x})')
        ((jpartition4x, x), lnkls__jp_x_) = lnkls__jp_x
        (min_j4g4x, count) = jpartition4x[-1]
        if j4g == min_j4g4x:
            if 0b00:print(f'inc_at_:({j4g} == {min_j4g4x})')
            if 0:
                #bug: gs=[3,7]
                #   inc_at_(0, ((((0, 2),), 6), ((((0, 1),), 3), ())))
                #   ({0:2},6) --> ({0:1},3) instead of ({0:2},6) --> ()
                #       ==>> (((0, 1), (0, 3)), 9) wrong!
                if lnkls__jp_x_:
                    (jp_, x_), _ = lnkls__jp_x_
                else:
                    jp_ = ()
            jp_ = jpartition4x[:-1]
            _jp = (*jp_, (j4g, count+1))
        elif j4g < min_j4g4x:
            if 0b00:print(f'inc_at_:({j4g} < {min_j4g4x})')
            _jp = (*jpartition4x, (j4g, 1))
        else:
            raise 000
        k4g, g = j2k_g[j4g]
        _x = __add__(x, g)
        add_(_jp, _x, lnkls__jp_x)
    def add_(jpartition4x, x, lnkls__jp_x_, /):
        if 0b00:print(f'add_({jpartition4x}, {x}, {lnkls__jp_x_})')
        lnkls__jp_x = (jpartition4x, x), lnkls__jp_x_
        k4x = k5x_(x)
        item = (k4x, lnkls__jp_x)
        hp.heappush(item)
    def add__g8x_(j4g, /):
        k4g, g = j2k_g[j4g]
        jpartition4x = ((j4g, 1),)
        x = g
        lnkls__jp_x_ = ()
        add_(jpartition4x, x, lnkls__jp_x_)

    def feed_new_g_():
        for k_g in iter_keyed_gs:
            break
        else:
            return False
        j4g = len(j2k_g)
        j2k_g.append(k_g)
        add__g8x_(j4g)
        return True
    if not feed_new_g_():
        return
    no_more_new_g = False
    def main():
      while 1:
        # (k4x, jpartition4x, x) = ls[0]
        (k4x, ((jpartition4x, x), lnkls__jp_x_)) = ls[0]
        #if partition_collector is default_partition_collector:
        if not to_export_all_partitions:
            #yield x
            yield (k4x, jpartition4x, x)
                # output unique x per eqvs<x>
        #bug:eqvs = hp.heappop_eqvs_()
            # jpartition4x make diff order!!
            # gs==[3,7]:
            #   (21, ((1, 3),), 21)
            #   (21, ((0, 7),), 21)
            #
        eqvs = [hp.heappop()]
        while ls:
            (_k4x, _) = ls[0]
            if not le4k_(_k4x, k4x):
                break

            eqvs.append(hp.heappop())
            if to_ensure_single_jpartition_per_element: raise ValildFail__not_unique_jpartition_per_element(x, eqvs)
        eqvs
        #xxx: assert len(eqvs) == 1
            # 3+4==2+5 if gs==[2,3,4,5]
            #
        ls4jpartition4x = tuple(jpartition4x for k4x, ((jpartition4x, x), lnkls__jp_x_) in eqvs)
        if 1:
            # to_ensure_jpartition_unique
            #   !! [『孤粒轰击积聚自堵塞』枚举法 ==>> [任意元素有一两个后继][除开最小生成元，其他元素有且只有一个前驱][枚举生成的元素可能重复，但每个分拆都唯一]]
            #   ==>> [jpA =!= jpB]
            #   !! 『取大优先』排序策略
            #   ==>> [jpA >= jpB]
            #   ==>> [jpA > jpB]
            #
            if not all(jpA > jpB for jpA, jpB in pairwise(ls4jpartition4x)): raise 000
        #if to_ensure_single_jpartition_per_element and len(eqvs) >= 2: raise ValildFail__not_unique_jpartition_per_element(k4x, x, ls4jpartition4x)
        if to_export_all_partitions:
            yield (k4x, ls4jpartition4x, x)
                # output unique x per eqvs<x>


        for k4x, lnkls__jp_x in eqvs:
            # next x = x + min_delta
            # min_delta <- {min_g, [count<min_g4x>==1]:-min_g4x+next_g4min_g4x}
            inc_at_(0, lnkls__jp_x)

            ((jpartition4x, x), lnkls__jp_x_) = lnkls__jp_x
            (min_j4g4x, count) = jpartition4x[-1]
            if count == 1:
                try_add_next_g_(lnkls__jp_x_, min_j4g4x)
            ######
      else:
        return
    return main()


class Error__generators_gcd_not_eq1(Exception):pass
def search_max_miss_ex__pint_additive_generators_(pint_additive_generators, /, *, uint_count__vs__pint_count=False, may_max_begin=None):
    r'''[[[
    :: may_max_begin/(may int)
    -> pint_additive_generators/(SizedContainer<pint>)
    ->:
    | -> ^Error__generators_gcd_not_eq1 iff [not gcd(strict_sorted_generators)==1]
    | -> False iff [not may_max_begin is None][max_miss >= max_begin]
    | -> (max_miss, (begin, end), j2generator, offset2jpartition) iff uint_count__vs__pint_count is False
    | -> (max_miss, (begin, end), j2generator, offset2j2count) iff uint_count__vs__pint_count is True
        + max_miss :: uint # 0!!
        + (begin, end) :: (pint, pint)
            [begin == max_miss +1]
            [end == begin +min_g]
        + j2generator/strict_sorted_generators :: unique-sorted[pint]
        ########################
        + offset2j2count :: [[count/uint]]{len=min_g}
            [count may be 0]
            [[offset :<- [0..<min_g]] -> [begin+offset == sum[j2generator[j]*offset2j2count[offset][j] | [j :<- [0..<len(j2generator)]]]]]
            # O(num_gs**2) too big!!!
        ########################
        + offset2jpartition :: [[(j4g, count/pint)]]{len=min_g}
            [count =!= 0]
            [min_g == min(strict_sorted_generators)]
            [j4g :: idx<strict_sorted_generators>]
            [offset2jpartition ::jpartitions<[begin..<end]>]

    ===
    how?
        min_g
        u%min_g
        * [gcd(generators) =!= 1]:
            ^Error__generators_gcd_not_eq1
        * [gcd(generators) == 1]:
            [must occur continuous range of length min_g]
            [(begin, end) :=> [[begin + min_g == end][[begin..<end] |<| span<generators>][not$ (begin-1) <- span<generators>]]]
            [max_miss := begin-1]
            @[u > max_miss]:
                [(q,r) := (u-(max_miss+1))/%min_g]
                [0 <= r < min_g]
                [u == q*min_g +r +(max_miss+1)]
                [u - q*min_g  == (begin+r) <- [begin..<end]]
    ===
    #]]]'''#'''
    len(pint_additive_generators)
        #MUST BE finite to check gcd==1
        #   !! infinite generators may not coprime
    from math import gcd
    from collections import deque

    check_type_is(bool, uint_count__vs__pint_count)
    if not may_max_begin is None:
        max_begin = may_max_begin
        check_type_is(int, max_begin)

    gs = sorted({*pint_additive_generators})
    for g in gs:
        check_type_is(int, g)

    if not gcd(*gs) == 1:
        raise Error__generators_gcd_not_eq1(gs)
    assert gs
    min_g = gs[0]
    if not min_g > 0: raise TypeError


    if may_max_begin is None:
        def is_ok_(x, /):
            return True
    else:
        max_end = max_begin +min_g
        def is_ok_(x, /):
            #bug:return x < max_begin
            #x is last
            return x < max_end
    is_ok_

    dq = deque([], min_g)
    it = generate4additive_semigroup__total_ordering__increasing_(gs)

    prev = -1
    for (k4x, jpartition4x, x) in it:
        if not is_ok_(x):
            return False
        prev += 1
        if not prev == x:
            #miss
            prev = x
            dq.clear()
        else:
            #continuous
            pass
        dq.append(jpartition4x)
        if len(dq) == min_g:
            last = x
            max_miss = last -min_g
            break
    ######################
    max_miss
    begin = max_miss +1
    end = begin +min_g
    strict_sorted_generators = tuple(gs)
    j2generator = strict_sorted_generators
    offset2jpartition = tuple(dq)
    assert max_miss >= 0
    assert all(count > 0 for jpartition in offset2jpartition for j, count in jpartition)
    assert all(begin+offset==sum(j2generator[j]*c for j, c in jpartition) for offset, jpartition in enumerate(offset2jpartition))

    if uint_count__vs__pint_count is False:
        return (max_miss, (begin, end), j2generator, offset2jpartition)
    ######################
    num_gs = len(j2generator)
    offset2j2count = tuple(_simplify_jpartition_(num_gs, jpartition) for jpartition in offset2jpartition)

    assert all(begin+offset==sum(map(int.__mul__, j2generator, j2count)) for offset, j2count in enumerate(offset2j2count))

    return (max_miss, (begin, end), j2generator, offset2j2count)
#simplified_jpartition
def _simplify_jpartition_(num_gs, jpartition, /):
    #patch zero count
    j2count = [0]*num_gs
    for j, count in jpartition:
        j2count[j] = count
    j2count = tuple(j2count)
    return j2count

def partition_pint4max_miss_ex__pint_additive_generators_(max_miss_ex, pint, /):
    r'''
    -> jpartition/[(j4g,count)]

precondition:
    #search_max_miss_ex__pint_additive_generators_():goto
    [max_miss_ex :: result of search_max_miss_ex__pint_additive_generators_<uint_count__vs__pint_count=False>]
    [(max_miss, (begin, end), j2generator, offset2jpartition) == max_miss_ex]
    [pint > max_miss >= 0]
postcondition:
    [pint == sum(j2generator[j]*c for j, c in jpartition)]

    '''#'''
    check_type_is(int, pint)
    (max_miss, (begin, end), j2generator, offset2jpartition) = max_miss_ex
    if not pint > max_miss: raise TypeError
    min_g = j2generator[0] #strict_sorted_generators
    if 0:
        #取消 <<== 取大优先
        q, r = divmod(pint -begin, min_g)
        jpartition = offset2jpartition[r]
        jpartition, q, min_g
    r = pint -begin
    jpartition = []
    for j in reversed(range(len(j2generator))):
        if r < min_g:
            break
        g = j2generator[j]
        q, r = divmod(r, g)
        if q > 0:
            jpartition.append((j,q))
    assert 0 <= r < min_g
    _jpartition = offset2jpartition[r]
    #merge:jpartition,_jpartition
    d = dict(_jpartition)
    _jpartition = None
    for j, count in jpartition:
        if j in d:
            d[j] += count
        else:
            d[j] = count
    jpartition = sorted(d.items(), reverse=True)
    d = None
    jpartition = tuple(jpartition)
    assert pint == sum(j2generator[j]*c for j, c in jpartition)
    return jpartition



__all__


from seed.math.generate_partition4additive_semigroup__total_ordering__increasing import iter_strict_sorted_elements4additive_semigroup__total_ordering__increasing_

from seed.math.generate_partition4additive_semigroup__total_ordering__increasing import generate4additive_semigroup__total_ordering__increasing_


from seed.math.generate_partition4additive_semigroup__total_ordering__increasing import search_max_miss_ex__pint_additive_generators_, partition_pint4max_miss_ex__pint_additive_generators_

from seed.math.generate_partition4additive_semigroup__total_ordering__increasing import *
