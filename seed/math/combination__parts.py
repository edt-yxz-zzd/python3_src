#__all__:goto
r'''[[[
e ../../python3_src/seed/math/combination__parts.py

seed.math.combination__parts
py -m nn_ns.app.debug_cmd   seed.math.combination__parts -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.combination__parts:__doc__ -ht # -ff -df
#######

[[
源起:e script/对称多项式讠基表达.py
目标:
    + 排列组合的中间态:分成多个区间/零件
    + 采用树状遍历方式:允许用户根据前缀缓存中间运算值

vs:view ../../python3_src/seed/math/combination.py
    #combinations(iterable, r)
    #permutations(iterable, r=None)

[输入参数 =[def]= (候选数/总长, 入选数/选长, 拆分表纟入选数)]
[拆分表纟入选数=拆分表{入选数} =[def]= 有序排列大区]
[有序排列大区 =[def]= [无序组合中区]]
[无序组合中区 =[def]= (长度纟无序组合小区, 重复数)]
[拆分表纟入选数 :: [(长度纟无序组合小区, 重复数)]]

[入选数 :: uint%(1+候选数)]
    或:[入选数 > 候选数] => 空集
[候选数 :: uint]
[长度纟无序组合小区 :: uint]
[重复数 :: uint]

[入选数 == sum((长度纟无序组合小区*重复数) for (长度纟无序组合小区, 重复数) in 拆分表{入选数})]

]]
[[
泛化:
[输入参数 :: (候选数, 入选数, 规范拆分表牜零起)]
[规范泛型顶层拆分表纟入选数=规范拆分表牜零起 :: (0|规范拆分表牜一起)]
[规范拆分表牜一起 :: (-1|规范拆分表牜二起)]
[规范拆分表牜二起 :: (规范排列大区/([6.5]++[规范拟拆分表牜一起]{len>=2}) | 规范拟拆分表牜二起)]
[规范拟拆分表牜一起 :: (-1|规范拟拆分表牜二起)]
[规范拟拆分表牜二起 :: (排列小块/负长度牜排列型小区{<=-2} | 组合小块/长度牜组合型小区{>=2} | 规范组合大区/(4.5, 规范重复数{>=2}, 规范拆分表牜二起))]

[拆分表牜组合 :: (组合小块/长度牜组合型小区 | 规范组合大区/(规范重复数, 规范拆分表牜二起))]
[拆分表牜排列 :: (-1 | 排列小块/负长度牜排列型小区 | 规范排列大区/([6.5]++[规范拟拆分表牜一起]{len>=2}))]
[负长度牜排列型小区 <= -2]
    0 => 否则退化为 就地删除
    -1 => 否则退化为 -1
[长度牜组合型小区 >= 2]
    0 => 否则退化为 就地删除
    1 => 否则退化为 -1
[规范重复数 >= 2]
    0 => 否则退化为 就地删除
    1 => 否则退化为 就地解包
[规范组合大区.拆分表 =!= (0|-1)]
    0 => 否则退化为 就地删除
    -1 => 否则退化为 组合小块==+规范重复数
    <==>规范拆分表牜二起
[len(规范排列大区.body) >= 2]
    0 => 否则退化为 就地删除
    1 => 否则退化为 就地解包
[总入选数纟(规范排列大区) >= 2]
[规范排列大区.拆分表 =!= 0]
    否则退化为 就地删除
    ==>>『一起』@规范拟拆分表牜一起
[all(欤组合型拆分表扌(小区) or 欤组合型拆分表扌(后一小区) for 小区, 后一小区 in pairwise(规范排列大区.body))]
    #排列型小区不相邻:否则融合
    #   小区非全排列型:否则融合后 大区长度为一，本层应省去
    #       含至少一个组合型小区
[all(欤组合型拆分表扌(小区) or 欤排列小块扌(小区) for 小区 in pairwise(规范排列大区.body))]
    <==>[all(not 欤排列大区扌(小区) for 小区 in pairwise(规范排列大区.body))]
    #规范排列大区:子区间 不能是 规范排列大区:否则就地解包
    ==>>『拟』@规范拟拆分表牜一起 #不直接含 排列大区

长度约束:
[[入选数==0] <==> [拆分表 == 0]]
[[入选数>0] <==> [入选数 == 总长度纟(拆分表)]]

次序约束:
[组合小块:严序升列]
[规范组合大区.子区间.首位:严序升列]
    次序关系 形成 森林 =>:
        + 位置讠毝更小位置纟更小入选值
            [毝更小位置纟更小入选值 ~=~ 鬽父节点乊森林]
        + 位置讠数目纟更大入选值
            [数目纟更大入选值==数目纟后代乊森林]
        + 位置讠最大入选值{需:候选数}
            [最大入选值{位置} == 候选数-1 -数目纟更大入选值{位置}]



===
[未规范泛型拆分表纟入选数=未规范拆分表 :: (允负长度/int | 未规范排列大区/([6.5]++[未规范拟拆分表]) | 未规范组合大区/(4.5, 未规范重复数/uint, 未规范拆分表))]
    #注意:未规范时:排列大区 可以直接 包含 排列大区

]]



'#'; __doc__ = r'#'
>>> def show_leafs_(候选数, 入选数, 未规范泛型拆分表纟入选数, /, **kwds):
...     it = 排列组合牜泛型牜树状遍历扌(候选数, 入选数, 未规范泛型拆分表纟入选数, **kwds)
...     it = (x for c, x in it if c == 0)
...     for j, x in enumerate(it):
...         print(j, x, sep=':')
>>> def show_all_(候选数, 入选数, 未规范泛型拆分表纟入选数, /, **kwds):
...     it = 排列组合牜泛型牜树状遍历扌(候选数, 入选数, 未规范泛型拆分表纟入选数, **kwds)
...     for j, x in enumerate(it):
...         print(j, x, sep=':')

>>> show_leafs_(3, 2, 2)
0:SeqView([0, 1])
1:SeqView([0, 2])
2:SeqView([1, 2])

>>> show_leafs_(3, 2, -2)
0:SeqView([0, 1])
1:SeqView([0, 2])
2:SeqView([1, 0])
3:SeqView([1, 2])
4:SeqView([2, 0])
5:SeqView([2, 1])

>>> show_all_(3, 2, 2)
0:(1, SeqView([0]))
1:(1, SeqView([0, 1]))
2:(0, SeqView([0, 1]))
3:(-1, SeqView([0, 1]))
4:(1, SeqView([0, 2]))
5:(0, SeqView([0, 2]))
6:(-1, SeqView([0, 2]))
7:(-1, SeqView([0]))
8:(1, SeqView([1]))
9:(1, SeqView([1, 2]))
10:(0, SeqView([1, 2]))
11:(-1, SeqView([1, 2]))
12:(-1, SeqView([1]))

>>> show_all_(3, 2, -2)
0:(1, SeqView([0]))
1:(1, SeqView([0, 1]))
2:(0, SeqView([0, 1]))
3:(-1, SeqView([0, 1]))
4:(1, SeqView([0, 2]))
5:(0, SeqView([0, 2]))
6:(-1, SeqView([0, 2]))
7:(-1, SeqView([0]))
8:(1, SeqView([1]))
9:(1, SeqView([1, 0]))
10:(0, SeqView([1, 0]))
11:(-1, SeqView([1, 0]))
12:(1, SeqView([1, 2]))
13:(0, SeqView([1, 2]))
14:(-1, SeqView([1, 2]))
15:(-1, SeqView([1]))
16:(1, SeqView([2]))
17:(1, SeqView([2, 0]))
18:(0, SeqView([2, 0]))
19:(-1, SeqView([2, 0]))
20:(1, SeqView([2, 1]))
21:(0, SeqView([2, 1]))
22:(-1, SeqView([2, 1]))
23:(-1, SeqView([2]))

>>> show_all_(3, 2, -2, 鬽起始已入选名单=[2, 1])
0:(1, SeqView([2]))
1:(1, SeqView([2, 1]))
2:(0, SeqView([2, 1]))
3:(-1, SeqView([2, 1]))
4:(-1, SeqView([2]))


>>> show_all_(1, 2, 2) #nothing
>>> show_all_(2, 0, 0)
0:(0, SeqView([]))
>>> show_all_(2, 1, -1)
0:(1, SeqView([0]))
1:(0, SeqView([0]))
2:(-1, SeqView([0]))
3:(1, SeqView([1]))
4:(0, SeqView([1]))
5:(-1, SeqView([1]))
>>> show_all_(2, 2, -2)
0:(1, SeqView([0]))
1:(1, SeqView([0, 1]))
2:(0, SeqView([0, 1]))
3:(-1, SeqView([0, 1]))
4:(-1, SeqView([0]))
5:(1, SeqView([1]))
6:(1, SeqView([1, 0]))
7:(0, SeqView([1, 0]))
8:(-1, SeqView([1, 0]))
9:(-1, SeqView([1]))
>>> show_all_(2, 2, 2)
0:(1, SeqView([0]))
1:(1, SeqView([0, 1]))
2:(0, SeqView([0, 1]))
3:(-1, SeqView([0, 1]))
4:(-1, SeqView([0]))





>>> show_leafs_(6, 6, (4.5, 3, 2))
0:SeqView([0, 1, 2, 3, 4, 5])
1:SeqView([0, 1, 2, 4, 3, 5])
2:SeqView([0, 1, 2, 5, 3, 4])
3:SeqView([0, 2, 1, 3, 4, 5])
4:SeqView([0, 2, 1, 4, 3, 5])
5:SeqView([0, 2, 1, 5, 3, 4])
6:SeqView([0, 3, 1, 2, 4, 5])
7:SeqView([0, 3, 1, 4, 2, 5])
8:SeqView([0, 3, 1, 5, 2, 4])
9:SeqView([0, 4, 1, 2, 3, 5])
10:SeqView([0, 4, 1, 3, 2, 5])
11:SeqView([0, 4, 1, 5, 2, 3])
12:SeqView([0, 5, 1, 2, 3, 4])
13:SeqView([0, 5, 1, 3, 2, 4])
14:SeqView([0, 5, 1, 4, 2, 3])

>>> show_leafs_(5, 5, (6.5, 3, 2))
0:SeqView([0, 1, 2, 3, 4])
1:SeqView([0, 1, 3, 2, 4])
2:SeqView([0, 1, 4, 2, 3])
3:SeqView([0, 2, 3, 1, 4])
4:SeqView([0, 2, 4, 1, 3])
5:SeqView([0, 3, 4, 1, 2])
6:SeqView([1, 2, 3, 0, 4])
7:SeqView([1, 2, 4, 0, 3])
8:SeqView([1, 3, 4, 0, 2])
9:SeqView([2, 3, 4, 0, 1])

>>> 规范冫泛型拆分表纟入选数扌(0)
0
>>> 规范冫泛型拆分表纟入选数扌(1)
-1
>>> 规范冫泛型拆分表纟入选数扌(-1)
-1
>>> 规范冫泛型拆分表纟入选数扌(2)
2
>>> 规范冫泛型拆分表纟入选数扌(-2)
-2
>>> 规范冫泛型拆分表纟入选数扌((4.5, 0, 999))
0
>>> 规范冫泛型拆分表纟入选数扌((4.5, 1, 999))
999
>>> 规范冫泛型拆分表纟入选数扌((4.5, 2, 999))
(4.5, 2, 999)
>>> 规范冫泛型拆分表纟入选数扌((4.5, 2, 0))
0
>>> 规范冫泛型拆分表纟入选数扌((4.5, 2, 1))
2
>>> 规范冫泛型拆分表纟入选数扌((4.5, 2, 2))
(4.5, 2, 2)

>>> 规范冫泛型拆分表纟入选数扌((6.5,))
0
>>> 规范冫泛型拆分表纟入选数扌((6.5, 0))
0
>>> 规范冫泛型拆分表纟入选数扌((6.5, 0, 0))
0
>>> 规范冫泛型拆分表纟入选数扌((6.5, 0, 0, 2))
2
>>> 规范冫泛型拆分表纟入选数扌((6.5, 0, -2, 0, -1))
-3
>>> 规范冫泛型拆分表纟入选数扌((6.5, 2, -2, 0, -1))
(6.5, 2, -3)
>>> 规范冫泛型拆分表纟入选数扌((6.5, 0, -2, 2, -1))
(6.5, -2, 2, -1)
>>> 规范冫泛型拆分表纟入选数扌((6.5, 0, -2, (4.5, 1, 1), -1))
-4
>>> 规范冫泛型拆分表纟入选数扌((6.5, 0, -2, (4.5, 2, 2), -1))
(6.5, -2, (4.5, 2, 2), -1)
>>> 规范冫泛型拆分表纟入选数扌((6.5, 0, -2, (6.5, 2, 2), -1))
(6.5, -2, 2, 2, -1)
>>> 规范冫泛型拆分表纟入选数扌((6.5, 0, -2, (6.5, -2, 2), -1))
(6.5, -4, 2, -1)

py_adhoc_call   seed.math.combination__parts   @f
]]]'''#'''
__all__ = r'''
排列组合牜泛型牜树状遍历扌
    排列组合牜指定次序牜树状遍历扌
    LEAF
    ENTER
    EXIT
乸匴遍历器纟规范泛型顶层拆分表纟入选数
    检查冫规范泛型顶层拆分表纟入选数扌
    规范冫泛型拆分表纟入选数扌
    入选数巛规范泛型顶层拆分表扌
    求冫位置讠毝更小位置纟更小入选值扌
    求冫位置讠数目纟更大入选值扌
检查冫位置讠毝更小位置纟更小入选值扌
检查内容冫入选名单前缀扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import builtins
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from itertools import pairwise, repeat #combinations
    from seed.tiny_.check import check_type_is, check_int_ge, check_int_ge_lt
    from seed.types.view.View import SeqView#MapView
    from seed.data_funcs.finger_tree.ft23_7sized_ascend_set import AscendSet
        #view ../../python3_src/seed/data_funcs/finger_tree/ft23_7sized_ascend_set.py
    from seed.tiny_.containers import mk_tuple
___end_mark_of_excluded_global_names__0___ = ...



class 乸匴遍历器纟规范泛型顶层拆分表纟入选数:
    __slots__ = ()
    #########
    if 0:
        欤重复处理负载纟规范组合大区 = False
        欤重复处理负载纟规范组合大区 = True
    def 乊全处理纟零扌(sf, /):
        return
    def 乊全处理纟负一扌(sf, /):
        return
    def 乊全处理纟排列小块扌(sf, 排列小块, /):
        return
    def 乊全处理纟组合小块扌(sf, 组合小块, /):
        return
    def 乊预处理纟规范排列大区扌(sf, /):
        '-> 预处理快照'
    def 乊后处理纟规范排列大区扌(sf, 规范排列大区, 预处理快照, 处理结果纟负载, /):
        return
    def 乊预处理纟规范组合大区扌(sf, /):
        '-> 预处理快照'
    def 乊后处理纟规范组合大区扌(sf, 规范组合大区, 预处理快照, 处理结果纟负载, /):
        return

    #########
    def 乊零起扌(sf, 规范拆分表牜零起, /):
        match 规范拆分表牜零起:
            case int(0):
                return sf.乊全处理纟零扌()
            case 规范拆分表牜一起:
                return sf.乊一起扌(规范拆分表牜一起)
            #case
        raise 000
    def 乊一起扌(sf, 规范拆分表牜一起, /):
        match 规范拆分表牜一起:
            case int(-1):
                return sf.乊全处理纟负一扌()
            case 规范拆分表牜二起:
                return sf.乊二起扌(规范拆分表牜二起)
            #case
        raise 000
    def 乊拟一起扌(sf, 规范拟拆分表牜一起, /):
        match 规范拟拆分表牜一起:
            case int(-1):
                return sf.乊全处理纟负一扌()
            case 规范拟拆分表牜二起:
                return sf.乊拟二起扌(规范拟拆分表牜二起)
            #case
        raise 000
    def 乊二起扌(sf, 规范拆分表牜二起, /):
        match 规范拆分表牜二起:
            case tuple([float(6.5), *_]) as 规范排列大区:
                return sf.乊规范排列大区扌(规范排列大区)
            case 规范拟拆分表牜二起:
                return sf.乊拟二起扌(规范拟拆分表牜二起)
            #case
        raise 000
    def 乊拟二起扌(sf, 规范拟拆分表牜二起, /):
        match 规范拟拆分表牜二起:
            case int(-1 | 0 | 1): raise TypeError
            case int(组合小块) if 组合小块 >= 2:
                return sf.乊全处理纟组合小块扌(组合小块)
            case int(排列小块) if 排列小块 <= -2:
                return sf.乊全处理纟排列小块扌(排列小块)
            case tuple([float(4.5), 规范重复数, 规范拆分表牜二起]) as 规范组合大区:
                return sf.乊规范组合大区扌(规范组合大区)
            case 规范排列大区:
                return sf.乊规范排列大区扌(规范排列大区)
            #.case bad:
            #.    raise TypeError(type(bad))
            #case
        raise 000
    def 乊规范组合大区扌(sf, 规范组合大区, /):
        match 规范组合大区:
            case tuple([float(4.5), 规范重复数, 规范拆分表牜二起]) as 规范组合大区:
                pass
            case bad:
                check_type_is(tuple, 规范组合大区)
                if not len(规范组合大区) == 3:raise TypeError
                raise TypeError(bad)
        check_int_ge(2, 规范重复数)
        预处理快照 = sf.乊预处理纟规范组合大区扌()
        if not sf.欤重复处理负载纟规范组合大区:
            处理结果纟负载 = sf.乊二起扌(规范拆分表牜二起)
        else:
            处理结果纟负载 = tuple(map(sf.乊二起扌, repeat(规范拆分表牜二起, 规范重复数)))
        return sf.乊后处理纟规范组合大区扌(规范组合大区, 预处理快照, 处理结果纟负载)
    def 乊规范排列大区扌(sf, 规范排列大区, /):
        match 规范排列大区:
            case tuple([float(6.5), _, _, *_]):
                pass
            case bad:
                check_type_is(tuple, 规范排列大区)
                if not len(规范排列大区) >= 1+2:raise TypeError
                raise TypeError(bad)
        列表纟规范拟拆分表牜一起 = 规范排列大区[1:]
        for (a, b) in pairwise(列表纟规范拟拆分表牜一起):
            match (a, b):
                case (int(a), int(b)) if a < 2 and b < 2: raise TypeError
        预处理快照 = sf.乊预处理纟规范排列大区扌()
        处理结果纟负载 = tuple(map(sf.乊拟一起扌, 列表纟规范拟拆分表牜一起))
        return sf.乊后处理纟规范排列大区扌(规范排列大区, 预处理快照, 处理结果纟负载)
    #########
class _乸匴纟检查冫规范泛型顶层拆分表纟入选数(乸匴遍历器纟规范泛型顶层拆分表纟入选数):
    __slots__ = ()
    欤重复处理负载纟规范组合大区 = False
_匴纟检查冫规范泛型顶层拆分表纟入选数 = _乸匴纟检查冫规范泛型顶层拆分表纟入选数()

class _乸匴纟入选数巛规范泛型顶层拆分表(乸匴遍历器纟规范泛型顶层拆分表纟入选数):
    __slots__ = ()
    欤重复处理负载纟规范组合大区 = False
    def 乊全处理纟零扌(sf, /):
        return 0
    def 乊全处理纟负一扌(sf, /):
        return 1
    def 乊全处理纟排列小块扌(sf, 排列小块, /):
        return -排列小块
    def 乊全处理纟组合小块扌(sf, 组合小块, /):
        return +组合小块
    def 乊后处理纟规范排列大区扌(sf, 规范排列大区, 预处理快照, 处理结果纟负载, /):
        return sum(处理结果纟负载)
    def 乊后处理纟规范组合大区扌(sf, 规范组合大区, 预处理快照, 处理结果纟负载, /):
        (_, 规范重复数, _) = 规范组合大区
        return 规范重复数*处理结果纟负载
_匴纟入选数巛规范泛型顶层拆分表 = _乸匴纟入选数巛规范泛型顶层拆分表()



class _乸匴纟位置讠毝更小位置纟更小入选值(乸匴遍历器纟规范泛型顶层拆分表纟入选数):
    def __init__(sf, /):
        #sf.栈纟本层数据 = []
        sf.位置讠毝更小位置纟更小入选值 = []
        sf.当前位置 = 0
        assert sf.当前位置 == len(sf.位置讠毝更小位置纟更小入选值)
    #########
    欤重复处理负载纟规范组合大区 = True
    def 乊全处理纟零扌(sf, /):
        讫址 = 起址 = sf.当前位置
        assert sf.当前位置 == len(sf.位置讠毝更小位置纟更小入选值)
        return 起址
    def 乊全处理纟负一扌(sf, /):
        起址 = sf.当前位置
        sf.位置讠毝更小位置纟更小入选值 += [-1]
        sf.当前位置 = 讫址 = 起址+1
        assert sf.当前位置 == len(sf.位置讠毝更小位置纟更小入选值)
        return 起址
    def 乊全处理纟排列小块扌(sf, 排列小块, /):
        起址 = sf.当前位置
        sf.位置讠毝更小位置纟更小入选值 += [-1] * -排列小块
        sf.当前位置 = 讫址 = 起址 + -排列小块
        assert sf.当前位置 == len(sf.位置讠毝更小位置纟更小入选值)
        return 起址
    def 乊全处理纟组合小块扌(sf, 组合小块, /):
        起址 = sf.当前位置
        sf.位置讠毝更小位置纟更小入选值 += [-1]
        sf.位置讠毝更小位置纟更小入选值.extend(range(sf.当前位置, -1+组合小块+sf.当前位置))
        sf.当前位置 = 讫址 = 起址 + 组合小块
        assert sf.当前位置 == len(sf.位置讠毝更小位置纟更小入选值)
        return 起址
    def 乊预处理纟规范排列大区扌(sf, /):
        '-> 预处理快照'
        #sf.栈纟本层数据.append([sf.当前位置])
        预处理快照 = 起址 = sf.当前位置
        assert sf.当前位置 == len(sf.位置讠毝更小位置纟更小入选值)
        return 预处理快照
    def 乊后处理纟规范排列大区扌(sf, 规范排列大区, 预处理快照, 处理结果纟负载, /):
        起址 = 预处理快照
        #not:起址 = sf.当前位置
        讫址 = sf.当前位置
        列表纟起址纟子区间 = 处理结果纟负载
        ls = sf.位置讠毝更小位置纟更小入选值
        for j in 列表纟起址纟子区间:
            assert ls[j] == -1
        ...;pass#排列大区:子区间首位:随意
        assert sf.当前位置 == len(sf.位置讠毝更小位置纟更小入选值)
        return 起址
    def 乊预处理纟规范组合大区扌(sf, /):
        '-> 预处理快照'
        #sf.栈纟本层数据.append([sf.当前位置])
        预处理快照 = 起址 = sf.当前位置
        assert sf.当前位置 == len(sf.位置讠毝更小位置纟更小入选值)
        return 预处理快照
    def 乊后处理纟规范组合大区扌(sf, 规范组合大区, 预处理快照, 处理结果纟负载, /):
        起址 = 预处理快照
        #not:起址 = sf.当前位置
        讫址 = sf.当前位置
        列表纟起址纟子区间 = 处理结果纟负载
        ls = sf.位置讠毝更小位置纟更小入选值
        for j in 列表纟起址纟子区间:
            assert ls[j] == -1
        for i, j in pairwise(列表纟起址纟子区间):
            ls[j] = i#组合大区:子区间首位升列
        assert sf.当前位置 == len(sf.位置讠毝更小位置纟更小入选值)
        return 起址





def 检查冫规范泛型顶层拆分表纟入选数扌(规范泛型顶层拆分表纟入选数, /):
    _匴纟检查冫规范泛型顶层拆分表纟入选数.乊零起扌(规范泛型顶层拆分表纟入选数)
    return
def 入选数巛规范泛型顶层拆分表扌(规范泛型顶层拆分表纟入选数, /):
    '规范泛型顶层拆分表纟入选数/规范拆分表牜零起 -> 入选数'
    入选数 = _匴纟入选数巛规范泛型顶层拆分表.乊零起扌(规范泛型顶层拆分表纟入选数)
    return 入选数
def 求冫位置讠毝更小位置纟更小入选值扌(规范拆分表牜零起, /):
    匴 = _乸匴纟位置讠毝更小位置纟更小入选值()
    匴.乊零起扌(规范拆分表牜零起)
    return tuple(匴.位置讠毝更小位置纟更小入选值)
def 检查冫位置讠毝更小位置纟更小入选值扌(位置讠毝更小位置纟更小入选值, /):
    check_type_is(tuple, 位置讠毝更小位置纟更小入选值)
    for j, imay_i in enumerate(位置讠毝更小位置纟更小入选值):
        check_int_ge_lt(-1, j, imay_i)

def 检查内容冫入选名单前缀扌(候选数, 位置讠毝更小位置纟更小入选值, 位置讠数目纟更大入选值, 已入选名单, /):
    入选数 = len(位置讠毝更小位置纟更小入选值)
    if not 入选数 <= 候选数:raise TypeError
        # !! 空集=>不可能有 合法前缀/已入选名单:包括 空前缀！
    if not len(已入选名单) <= 入选数:raise TypeError
    if not 已入选名单:
        return

    #通行上下限:
    for 入选值 in 已入选名单:
        check_int_ge_lt(0, 候选数, 入选值)
    #无重复值:
    if not len(已入选名单) == len({*已入选名单}):raise TypeError
    #特色下限:
    for j, imay_i in enumerate(位置讠毝更小位置纟更小入选值[:len(已入选名单)]):
        if imay_i == -1:continue
        i = imay_i
        if not 已入选名单[i] > 已入选名单[j]:raise TypeError
    #特色上限:
    候选名单 = AscendSet(range(候选数), unordered_vs_ascend_vs_descend=1)
    for 当前位置, 入选值 in enumerate(已入选名单):
        (更小值集, 魊入选值, 更大值集) = 候选名单.partition_at_key_(入选值)
        if not 魊入选值: raise 000
        if not 位置讠数目纟更大入选值[当前位置] <= len(更大值集):raise TypeError
        候选名单 = 更小值集 + 更大值集
            #<==>候选名单 = 候选名单.iremove(入选值)
    #end-for_loop
    return

def 求冫位置讠数目纟更大入选值扌(位置讠毝更小位置纟更小入选值, /):
    入选数 = len(位置讠毝更小位置纟更小入选值)
    位置讠数目纟更大入选值 = [0]*入选数
    for j in reversed(range(入选数)):
        match 位置讠毝更小位置纟更小入选值[j]:
            case -1:
                continue
            case i:
                位置讠数目纟更大入选值[i] += 1 + 位置讠数目纟更大入选值[j]
    return tuple(位置讠数目纟更大入选值)






def 规范冫泛型拆分表纟入选数扌(未规范泛型拆分表纟入选数, /):
    '-> 规范拆分表牜零起'
    # [未规范泛型拆分表纟入选数=未规范拆分表 :: (允负长度/int | 未规范排列大区/([6.5]++[未规范拟拆分表]) | 未规范组合大区/(4.5, 未规范重复数/uint, 未规范拆分表))]
    #     #注意:未规范时:排列大区 可以直接 包含 排列大区
    def 乊未规范拆分表扌(未规范拆分表, /):
        match 未规范拆分表:
            case int(1):
                return -1
            case int(允负长度):
                return 允负长度
            case (float(4.5), int(未规范重复数), 未规范拆分表) as 未规范组合大区:
                return 乊未规范组合大区扌(未规范重复数, 未规范拆分表)
            case 未规范排列大区:
                return 乊未规范排列大区扌(未规范排列大区)
            #case
        raise 000
    def 乊未规范组合大区扌(未规范重复数, 未规范拆分表, /):
        规范拆分表 = 乊未规范拆分表扌(未规范拆分表)
        if 未规范重复数 < 0:raise TypeError()
        if 未规范重复数 == 0:
            return 0
        if 未规范重复数 == 1:
            return 规范拆分表
        规范重复数 = 未规范重复数
        check_int_ge(2, 规范重复数)

        match 规范拆分表:
            case int(-1):
                return +规范重复数
            case int(0):
                return 0
        规范拆分表牜二起 = 规范拆分表
        规范组合大区 = (4.5, 规范重复数, 规范拆分表牜二起)
        return 规范组合大区
    def 乊未规范排列大区扌(未规范排列大区, /):
        未规范排列大区 = mk_tuple(未规范排列大区)
        match 未规范排列大区:
            case (float(6.5), *列表纟规范拆分表牜零起):
                pass
            case bad:
                raise TypeError(bad)
            #case
        列表纟规范拆分表牜零起
        列表纟规范拆分表牜一起 = [*filter(bool, map(乊未规范拆分表扌, 列表纟规范拆分表牜零起))]
            #就地删除
        ls = []#reversed
        777;欤末位负数冃排列小块 = False
        while 列表纟规范拆分表牜一起:
            规范拆分表牜一起 = 列表纟规范拆分表牜一起.pop()
            match 规范拆分表牜一起:
                case int(0 | 1):
                    raise 000
                case int(组合小块) if 组合小块 >= 2:
                    ls.append(组合小块)
                    777;欤末位负数冃排列小块 = False
                case int(泛排列小块) if 泛排列小块 <= -1:
                    if 欤末位负数冃排列小块:
                        #融合
                        ls[-1] += 泛排列小块
                    else:
                        ls.append(泛排列小块)
                    777;欤末位负数冃排列小块 = True
                case (float(4.5), 规范重复数, 规范拆分表牜二起) as 规范组合大区:
                    ls.append(规范组合大区)
                    777;欤末位负数冃排列小块 = False
                case tuple([float(6.5), *_列表纟规范拟拆分表牜一起]) as 规范排列大区:
                    #就地解包
                    列表纟规范拆分表牜一起.extend(_列表纟规范拟拆分表牜一起)
                    pass;ls;欤末位负数冃排列小块
                case _:
                    raise 000
                #case
            pass
        #end-while 列表纟规范拆分表牜一起:
        match ls:
            case []:
                return 0
            case [规范拆分表牜一起]:
                return 规范拆分表牜一起
            #case
        assert len(ls) >= 2
        ls.append(6.5)
        ls.reverse()
        规范排列大区 = tuple(ls)
        return 规范排列大区
    def main():
        规范拆分表牜零起 = 乊未规范拆分表扌(未规范泛型拆分表纟入选数)
        检查冫规范泛型顶层拆分表纟入选数扌(规范拆分表牜零起)
        return 规范拆分表牜零起
    return main()


LEAF = 0
ENTER = +1
EXIT = -1
def 排列组合牜泛型牜树状遍历扌(候选数, 入选数, 未规范泛型拆分表纟入选数, /, *, 鬽起始已入选名单=None):
    '候选数/uint -> 入选数/uint -> 拆分表{入选数} -> Iter (单步况态, 已入选名单/SeqView[uint%候选数]{len<=入选数}) # [单步况态 :: (+1/ENTER|-1/EXIT|0/LEAF)]'
    check_int_ge(0, 候选数)
    位置讠毝更小位置纟更小入选值 = 预备冫参数纟排列组合牜泛型牜树状遍历扌(入选数, 未规范泛型拆分表纟入选数)
    return 排列组合牜指定次序牜树状遍历扌(候选数, 入选数, 位置讠毝更小位置纟更小入选值, 鬽起始已入选名单=鬽起始已入选名单)
def 预备冫参数纟排列组合牜泛型牜树状遍历扌(入选数, 未规范泛型拆分表纟入选数, /):
    '入选数 -> 未规范泛型拆分表纟入选数 -> 位置讠毝更小位置纟更小入选值'
    check_int_ge(0, 入选数)
    规范拆分表牜零起 = 规范冫泛型拆分表纟入选数扌(未规范泛型拆分表纟入选数)
    if not 入选数 == 入选数巛规范泛型顶层拆分表扌(规范拆分表牜零起):raise ValueError(入选数, 规范拆分表牜零起)
    位置讠毝更小位置纟更小入选值 = 求冫位置讠毝更小位置纟更小入选值扌(规范拆分表牜零起)
        # [毝更小位置纟更小入选值 ~=~ 鬽父节点乊森林]
    return 位置讠毝更小位置纟更小入选值


def 排列组合牜指定次序牜树状遍历扌(候选数, 入选数, 位置讠毝更小位置纟更小入选值, /, *, 鬽起始已入选名单=None):
    '候选数/uint -> 入选数/uint -> 位置讠毝更小位置纟更小入选值/次序表{入选数}/[imay uint%入选数]{len==入选数} -> Iter (单步况态, 已入选名单/SeqView[uint%候选数]{len<=入选数}) # [单步况态 :: (+1/ENTER|-1/EXIT|0/LEAF)] # [all(-1 <= imay_i < j for j, imay_i in enumerate(位置讠毝更小位置纟更小入选值))]'
    if 0:
        位置讠入选值 = ...
        位置讠数目纟更大入选值 = ...
    def _当前位置讠候选名单扌(候选名单, 当前位置, /):
        match 位置讠毝更小位置纟更小入选值[当前位置]:
            case -1:
                pass
            case 父位置:
                # [当前入选值 > 位置讠入选值[父位置]]
                (_, 候选名单) = 候选名单.split_at_key_(位置讠入选值[父位置])
            #case
        候选名单
        后代数目 = 位置讠数目纟更大入选值[当前位置]
        有效数量 = len(候选名单) -后代数目
        if not 有效数量 > 0:raise 000
        (候选名单, _) = 候选名单.split_at_(有效数量)
        return 候选名单
    def 当前位置讠趃候选名单扌(候选名单, 当前位置, /):
        候选名单 = _当前位置讠候选名单扌(候选名单, 当前位置)
        趃候选名单 = iter(候选名单)
        return 趃候选名单
    def 初始化扌(起始已入选名单, 已入选名单, 位置讠入选值, 位置讠保存候选名单, /):
        assert 起始已入选名单
        assert not 位置讠入选值
        位置讠趃候选名单 = []
        for 当前位置, 入选值 in enumerate(起始已入选名单):
            assert len(位置讠趃候选名单) == len(位置讠入选值)
            assert len(位置讠趃候选名单) == -1+len(位置讠保存候选名单)
            候选名单 = _当前位置讠候选名单扌(位置讠保存候选名单[-1], 当前位置)
            (落选名单, 魊入选值, 候选名单) = 候选名单.partition_at_key_(入选值)
            if not 魊入选值: raise 000
            趃候选名单 = iter(候选名单)
            位置讠趃候选名单.append(趃候选名单)
            位置讠入选值.append(入选值)
            777;yield (ENTER, 已入选名单)
            if 入选数 == len(位置讠入选值):
                yield (LEAF, 已入选名单)
                yield (EXIT, 已入选名单)
                777;位置讠入选值.pop()
                assert len(位置讠趃候选名单) == 1+len(位置讠入选值)
                assert len(位置讠趃候选名单) == len(位置讠保存候选名单)
                return 位置讠趃候选名单
                continue
            位置讠保存候选名单.append(位置讠保存候选名单[-1].iremove(入选值))
        位置讠趃候选名单.append(当前位置讠趃候选名单扌(位置讠保存候选名单[-1], len(位置讠入选值)))
        assert len(位置讠趃候选名单) == 1+len(位置讠入选值)
        assert len(位置讠趃候选名单) == len(位置讠保存候选名单)
        return 位置讠趃候选名单

    def main():
        nonlocal 位置讠入选值, 位置讠数目纟更大入选值
        check_int_ge(0, 候选数)
        check_int_ge(0, 入选数)
        检查冫位置讠毝更小位置纟更小入选值扌(位置讠毝更小位置纟更小入选值)
        if not 入选数 == len(位置讠毝更小位置纟更小入选值):raise ValueError(入选数, 位置讠毝更小位置纟更小入选值)
        match 鬽起始已入选名单:
            case None:
                起始已入选名单 = []
                    #已入选-前缀
            case 起始已入选名单:
                pass
            #case
        起始已入选名单 = mk_tuple(起始已入选名单)

        if not 入选数 <= 候选数:
            #空集
            if not None is 鬽起始已入选名单:raise TypeError
                # !! 空集=>不可能有 合法前缀/已入选名单:包括 空前缀！
            return
        位置讠入选值 = []
            #已入选-前缀
        已入选名单 = SeqView(位置讠入选值)
        if 入选数 == len(位置讠入选值):
            if 起始已入选名单:raise TypeError
            yield (LEAF, 已入选名单)
            return



        #位置讠毝更小位置纟更小入选值 = 求冫位置讠毝更小位置纟更小入选值扌(规范拆分表牜零起)
            # [毝更小位置纟更小入选值 ~=~ 鬽父节点乊森林]
        位置讠数目纟更大入选值 = 求冫位置讠数目纟更大入选值扌(位置讠毝更小位置纟更小入选值)
            # [数目纟更大入选值==数目纟后代乊森林]
        #位置讠最大入选值 = [(候选数-1 -数目纟更大入选值) for 位置,数目纟更大入选值 in enumerate(位置讠数目纟更大入选值)]
            # [最大入选值{位置} == 候选数-1 -数目纟更大入选值{位置}]

        if 起始已入选名单:
            检查内容冫入选名单前缀扌(候选数, 位置讠毝更小位置纟更小入选值, 位置讠数目纟更大入选值, 起始已入选名单)








        #.候选名单牜初始 = range(候选数)
        #.候选名单 = AscendSet(候选名单牜初始, unordered_vs_ascend_vs_descend=1)
        #.位置讠保存候选名单 = [候选名单]
        #.777;del 候选名单
        位置讠保存候选名单 = [AscendSet(range(候选数), unordered_vs_ascend_vs_descend=1)]
        if 起始已入选名单:
            位置讠趃候选名单 = yield from 初始化扌(起始已入选名单, 已入选名单, 位置讠入选值, 位置讠保存候选名单)
        else:
            位置讠趃候选名单 = [当前位置讠趃候选名单扌(位置讠保存候选名单[-1], len(位置讠入选值))]
        位置讠趃候选名单

        while 1:
            assert len(位置讠趃候选名单) == 1+len(位置讠入选值)
            assert len(位置讠趃候选名单) == len(位置讠保存候选名单)
            for 入选值 in 位置讠趃候选名单[-1]:
                break
            else:
                位置讠趃候选名单.pop()
                位置讠保存候选名单.pop()
                if not 位置讠入选值:break
                yield (EXIT, 已入选名单)
                777;位置讠入选值.pop()
                continue
            位置讠入选值.append(入选值)
            777;yield (ENTER, 已入选名单)
            if 入选数 == len(位置讠入选值):
                yield (LEAF, 已入选名单)
                yield (EXIT, 已入选名单)
                777;位置讠入选值.pop()
                continue
            位置讠保存候选名单.append(位置讠保存候选名单[-1].iremove(入选值))
            位置讠趃候选名单.append(当前位置讠趃候选名单扌(位置讠保存候选名单[-1], len(位置讠入选值)))
        #end-while 1:
    #end-def main():
    return main()
#end-def 排列组合牜指定次序牜树状遍历扌






































































































#.def 规范冫拆分表纟入选数扌(拆分表纟入选数, /):
#.    #拆分表纟入选数 = tuple((长度纟无序组合小区, 重复数) for (长度纟无序组合小区, 重复数) in 拆分表纟入选数)
#.    def __():
#.        for (长度纟无序组合小区, 重复数) in 拆分表纟入选数:
#.            check_int_ge(0, 长度纟无序组合小区)
#.            check_int_ge(0, 重复数)
#.            if 长度纟无序组合小区 == 0 or 重复数 == 0:
#.                continue
#.            yield (长度纟无序组合小区, 重复数)
#.    拆分表纟入选数 = tuple(__())
#.    return 拆分表纟入选数
#.def _预备冫排列组合牜三层扌(候选数, 入选数, 拆分表纟入选数, /):
#.    check_int_ge(0, 候选数)
#.    check_int_ge(0, 入选数)
#.    拆分表纟入选数 = 规范冫拆分表纟入选数扌(拆分表纟入选数)
#.    if not 入选数 == sum((长度纟无序组合小区*重复数) for (长度纟无序组合小区, 重复数) in 拆分表纟入选数):raise TypeError
#.    return 拆分表纟入选数
#.#.def 排列组合牜三层扌(候选数, 入选数, 拆分表纟入选数, /):
#.#.    '候选数/uint -> 入选数/uint -> 拆分表{入选数}/有序排列大区/[无序组合中区/(长度纟无序组合小区, 重复数)] -> Iter 入选名单/[uint%候选数]{len==入选数}'
#.#.    拆分表纟入选数 = _预备冫排列组合牜三层扌(候选数, 入选数, 拆分表纟入选数)
#.#.    if not 入选数 <= 候选数:
#.#.        #空集
#.#.        return
#.#.    if 入选数 == 0:
#.#.        yield ()
#.#.        return
#.#.    us = []
#.#.    js = [*range(候选数)]
#.#.    jss = []
#.#.    while 1:
#.#.        i = len(jss)
#.#.        combinations(js, 入选数)
#.#.
#.
#.
#.
#.
#.LEAF = 0
#.ENTER = +1
#.EXIT = -1
#.def 排列组合牜三层牜树状遍历扌(候选数, 入选数, 拆分表纟入选数, /):
#.    '候选数/uint -> 入选数/uint -> 拆分表{入选数}/有序排列大区/[无序组合中区/(长度纟无序组合小区, 重复数)] -> Iter (case, idx_seq_view/SeqView[uint%候选数]) # [case :: (+1/ENTER|-1/EXIT|0/LEAF)]'
#.    if not 入选数 <= 候选数:
#.        #空集
#.        return
#.    位置讠入选值 = i2u = us = []
#.        #已入选-前缀
#.    idx_seq_view = SeqView(us)
#.    if 入选数 == 0:
#.        yield (LEAF, idx_seq_view)
#.        return
#.    双向链表冃候选名单纟下一中区首位 = 
#.        #取:全局最小候选值
#.    双向链表冃候选名单纟下一小区首位
#.        #取:比当前小区首位更大的最小候选值
#.    位置讠毝更小位置纟更小入选值 = j2imay_i4small = _mk__j2imay_i4small(入选数, 拆分表纟入选数)
#.        # [毝更小位置纟更小入选值 ~=~ 鬽父节点乊森林]
#.    位置讠数目纟更大入选值 = i2num_biggers = _mk__i2num_biggers(入选数, 拆分表纟入选数)
#.        # [数目纟更大入选值==数目纟后代乊森林]
#.    位置讠最大入选值 = [(候选数-1 -数目纟更大入选值) for 位置,数目纟更大入选值 in enumerate(位置讠数目纟更大入选值)]
#.        # [最大入选值{位置} == 候选数-1 -数目纟更大入选值{位置}]
#.    TODO... ...
#.或者 两层
#.或者 泛化
#.    t2u = stk = [*range(候选数)[::-1]]
#.        # 候选区-降序
#.        # 不变式:[sorted([*i2u,*t2u]) == [*range(候选数)]]
#.        # 不变式:[u > v for u,v in pairwise(t2u)]
#.        #
#.    i2t = []
#.        # 入选项 于 候选区 应有的插入位
#.        # 不变式:[len(i2t) == len(i2u)]
#.        # 不变式:[[len(i2t) > 0] -> [i:=len(i2t)-1] -> [t:=i2t[-1]] -> [u:=i2u[-1]] -> [[0 <= t <= len(stk)][降序:[*stk[:t],u,*stk[t:]]][i2num_biggers[i] >= t]]]
#.        #   还剩t个更大的候选
#.
#.def _mk__i2num_biggers(入选数, 拆分表纟入选数, /):
#.    i2num_biggers = [0]*入选数
#.    i = 0
#.    for (长度纟无序组合小区, 重复数) in 拆分表纟入选数:
#.        _i = i+长度纟无序组合小区*重复数
#.            # 中区@us[i:_i]
#.        for j in range(i, _i, 长度纟无序组合小区):
#.            _j = j + 长度纟无序组合小区
#.                # 小区@us[j:_j]
#.            i2num_biggers[j] = _i -j-1
#.                #小区首位小于中区居后尾部
#.            for k in range(j+1, _j):
#.                i2num_biggers[k] = _j -k-1
#.                    #小区内部位小于小区居后尾部
#.        i = _i
#.    assert i == 入选数
#.    assert len(i2num_biggers) == 入选数
#.    return i2num_biggers
#.
#.
#.
#.def _mk__j2imay_i4small(入选数, 拆分表纟入选数, /):
#.    j2imay_i4small = [*range(-1, -1+入选数)] # [-1]*入选数
#.        #升序:小区内部位小于小区居后尾部
#.    i = 0
#.    for (长度纟无序组合小区, 重复数) in 拆分表纟入选数:
#.        _i = i+长度纟无序组合小区*重复数
#.            # 中区@us[i:_i]
#.        j2imay_i4small[i] = -1
#.            #中区首位随意
#.        for j in range(i, _i, 长度纟无序组合小区)[1:]:
#.            # 小区@us[j:j+长度纟无序组合小区]
#.            j2imay_i4small[j] = i
#.                #升序:小区首位大于前小区首位
#.        i = _i
#.    assert i == 入选数
#.    assert len(j2imay_i4small) == 入选数
#.    return j2imay_i4small
#.


__all__
from seed.math.combination__parts import 排列组合牜泛型牜树状遍历扌, LEAF, ENTER, EXIT, 排列组合牜指定次序牜树状遍历扌, 预备冫参数纟排列组合牜泛型牜树状遍历扌
#[(LEAF, ENTER, EXIT) == (0, +1, -1)]
#def 排列组合牜泛型牜树状遍历扌(候选数, 入选数, 未规范泛型拆分表纟入选数, /, *, 鬽起始已入选名单=None):
#    '候选数/uint -> 入选数/uint -> 拆分表{入选数} -> Iter (单步况态, 已入选名单/SeqView[uint%候选数]{len<=入选数}) # [单步况态 :: (+1/ENTER|-1/EXIT|0/LEAF)]'
#def 预备冫参数纟排列组合牜泛型牜树状遍历扌(入选数, 未规范泛型拆分表纟入选数, /):
#    '入选数 -> 未规范泛型拆分表纟入选数 -> 位置讠毝更小位置纟更小入选值'
#def 排列组合牜指定次序牜树状遍历扌(候选数, 入选数, 位置讠毝更小位置纟更小入选值, /, *, 鬽起始已入选名单=None):
#    '候选数/uint -> 入选数/uint -> 位置讠毝更小位置纟更小入选值/次序表{入选数}/[imay uint%入选数]{len==入选数} -> Iter (单步况态, 已入选名单/SeqView[uint%候选数]{len<=入选数}) # [单步况态 :: (+1/ENTER|-1/EXIT|0/LEAF)] # [all(-1 <= imay_i < j for j, imay_i in enumerate(位置讠毝更小位置纟更小入选值))]'
from seed.math.combination__parts import *
