#__all__:goto
#TODO:goto
#TODO:new魖基类:提前排除冫最短加链牜加一型丶因数分解型#加二型？
#   更小靶值讠最小显链长:靶值讠最小显链长:view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length__ver3.py
#目前焦点:最短加链暨递归婪溟链
#   view ../../python3_src/seed/math/power/addition_chain/shortest/mixed_recursive_greedy_zpow_addition_chain__doc__py_adhoc_call.py
#   view ../../python3_src/seed/math/power/addition_chain/shortest/rewrite3.py
#   [环节列表=[def]=[(主干值, 内点址引, 内点溟次, 增量纟内点溟次, 显链长)]]
#########
##obsolete:目前焦点:贪溟链/贪婪型二幂环要链{贪婪型:加数必含前一劫的二幂倍，类似加星链;二幂环:倍环只考虑二幂;要点:非末劫则出度大于一，介点直接融入到汇劫}
#   倍环只考虑二幂<<==因为发现搜索失败时，倍环的内部状态即所有加链都得重走一遍，搜索效率并没有提高，只是最终表达上更简洁;二幂倍环 结构固定
#   贪婪型<<==因为发现12509,5784689都如此
#       view ../../python3_src/seed/math/power/addition_chain/shortest/rewrite.py
#k个不相等的正整数相交至多进几位？或者说 小步数下限是多少？[k>=2][sum[2**e-j | [j:<-[1..=k]]] == k*2**e -k*(1+k)/2 < k*2**e][大步数==floor_log2(左式) -floor_log2(2**e-1) <= e+floor_log2(k-1) -(e-1) == 1+floor_log2(k-1)][(k-1)>=小步数==(k-1)-大步数>=(k-2)-floor_log2(k-1)]
#   若是有k次2个不相等的正整数相加，则至多进几位？增长速率小于等于黄金比率:f[]=[0,1,1,2,  3,5,8,...];[f[j]==(((1+sqrt5)/2)**j-((1-sqrt5)/2)**j)/sqrt5][k>=小步数>=k-(floor_log2(f[2+k]) -floor_log2(f[2])) >=k-log2(f[2+k])>=k-(2+k)*log2((1+sqrt5)/2) >= k*(2-log2(1+sqrt5)) +2 -2*log2(1+sqrt5) ~= k*0.30575808636938273 -1.3884838272612345][log2(1+sqrt5) ~= 1.6942419136306173][小步数<=k<=...~=小步数*3.2705594539596636+4.541118907919327]
# [汇值未必升序]:标溟链/溟要链/溟隘链/[([(j, [ez]{ez严序递降})]{j严序递降}, u/汇值)]{条目依词典序严序递升}{融后互斥}{出度大于一}
#   [抹去指数][汇值未知][汇值未必升序]:模板链/溟模链/溟母链/[[(j, num_ezs)]{j严序递降}]{首j松序递升}
#       文本表达{溟母链}:[j:num_ezs,...;... ...]
#       文本表达{溟隘链}:[j:ez:ez...,...@u;... ...]
#   e ../../python3_src/seed/math/power/addition_chain/shortest/rewrite2.py
#########
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/shortest/search7contracted_chain.py
view ../../python3_src/seed/math/power/addition_chain/shortest/rewrite.py
    虚匏链#contracted_chain#也许该叫『空心链』
view ../../python3_src/seed/math/power/addition_chain/common/README-defs.txt
    #[:猜想:根据剩余链长辻虚匏融介链耂前缀链耂义务出度求最大靶值乊排除冫加一型丶因数分解型]:goto


seed.math.power.addition_chain.shortest.search7contracted_chain
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.shortest.search7contracted_chain -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.shortest.search7contracted_chain:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.math.power.addition_chain.shortest.search7contracted_chain:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.math.power.addition_chain.shortest.search7contracted_chain:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
come_from:
e ../../python3_src/seed/math/power/addition_chain/shortest/search.py
正打算编写时:乸匴前缀无效判定器纟最短加链牜提前排除乘环殿后牜强制乘环次序牜强制可交换步次序
    仔细想想，还是很慢，因为 失败的话 乘环的所有中间态 都得遍历一遍，考虑一开始就用 倍数 替代 乘环，也就是 直接 搜索 虚匏链(类似 骨架，只是 保留值 而非 倍数)。
        =>本模块

]]
[[
记录信息:
前缀纟虚匏链:
    [1,...,a,...,b,...,c]
址引讠构型纟下一位:
    --[...,+,...,*,...,+]
    『*』: [us[tk] == 倍数*us[tk-1]]
    『+』: [us[tk] == us[jk] + us[ik]]
        在 排除乘环殿后 的情形下:靶值 构型 必是 『+』
址引讠构料纟下一位:
    --[...,(jk,ik),...,倍数,...,(jk,ik)]

倍数 的 次序:
    匏腰邻接位倍数降序？不需要，因为 要求 乘环匏腰 出度>=2
    同位倍数降序？不对，得按 (倍数增长速率,倍数) 降序 排次。
        [倍数增长速率{倍数}=[def]=倍数**/(靶值讠最小显链长[倍数])]
        [[倍数]{同等增速}]{增速降序}
    但是 同时还得 限制 倍数，上界纟倍数...麻烦...

增长速率
增长率
growth_rate
e ../../python3_src/seed/math/power/addition_chain/data/pairs7DECS_of__growth_rate7len_optimal_addition_chain__target_uints7DECS.py
from seed.math.power.addition_chain.data.pairs7DECS_of__growth_rate7len_optimal_addition_chain__target_uints7DECS import pairs7DECS_of__growth_rate7len_optimal_addition_chain__target_uints7DECS, 降序列表纟丮最小显链长增长速率辻靶值列表厈

e ../../python3_src/seed/math/power/addition_chain/data/sorted_target_uints5len_optimal_addition_chain.py
from seed.math.power.addition_chain.data.sorted_target_uints5len_optimal_addition_chain import sorted_target_uints5len_optimal_addition_chain, 最小显链长讠靶值列表 # .最大靶值牜可用 .最小靶值牜溢出

e ../../python3_src/seed/math/power/addition_chain/shortest/rewrite.py
    ++虚匏融介链

直接搜索:虚匏融介链

]]



'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.power.addition_chain.shortest.search7contracted_chain   @蛮力搜索冫最短加链牜极简扌  --靶值=15
    (1, 2, 4, 5, 10, 15)


py_adhoc_call   '' @str   %%:P  ='P.nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3().取冫靶值讠最小显链长扌()[12509]'
    =>『'17'』
py_adhoc_call   '' @str   %%:P  ='P.nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3().取冫靶值讠最小显链长扌()'
    =>『'P.nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3().取冫靶值讠最小显链长扌()'』

from seed.math.power.addition_chain.shortest.search7contracted_chain import *
]]]'''#'''
__all__ = r'''
魖匴蛮力搜索器纟最短加链
    乸匴蛮力搜索器纟最短加链牜极简
        匴蛮力搜索器纟最短加链牜极简
            蛮力搜索冫最短加链牜极简扌
    魖匴蛮力搜索器纟加工链纟虚匏融介链纟最短加链牜复杂参数


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
null_iter = iter('')
#.from functools import cached_property
#from seed.math.power.addition_chain.data.pairs7DECS_of__growth_rate7len_optimal_addition_chain__target_uints7DECS import pairs7DECS_of__growth_rate7len_optimal_addition_chain__target_uints7DECS, 降序列表纟丮最小显链长增长速率辻靶值列表厈
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_int_ge_le, check_pair
from seed.math.power.addition_chain.shortest.search7iterative_deepening import 魖匴渐深树搜索
#see:dot_#from seed.func_tools.dot2 import dot
#.
#.from abc import update_abstractmethods
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from collections import namedtuple
    from seed.math.power.addition_chain.common.check import 检查冫严序加链乊靶值扌, 检查冫严序加链扌, 检查冫严序加链内容扌
    from seed.math.power.addition_chain.common.check import 检查冫松序加链乊靶值扌, 检查冫松序加链扌, 检查冫松序加链内容扌
    from seed.math.power.addition_chain.short.binary import 构造冫加链巛靶值牜二进制拆分扌
    from seed.math.power.addition_chain.common.properties import 显链长纟, 阳爻数纟, 首爻位纟
    from seed.helper.ifNone import ifNone,ifNonef
    from seed.tiny_.funcs import echo,fst,snd
    from seed.tiny_.containers import mk_tuple
    from itertools import groupby
    from seed.iters.PeekableIterator import echo_or_mk_IPeekableIterator
        #is_empty#not hp
        #head#hp[0]
        #read1()#_heappop
    from seed.for_libs.for_heapq import merge_ex
        #def merge_ex(*sorted_iterable_exs, key4stable:[False,callable]=False, key4le=None, __le__=None, reverse=False, unique:[bool,callable]=False, obj2value_:[None,callable]=None):
    from seed.debug.print_err import print_err
    from seed.types.Either import mk_Left,mk_Right #Either,Cased

    from seed.data_funcs.lnkls import mk_empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable #rglnkls_ops, empty_rglnkls

    from seed.data_funcs.lnkls import rglnkls2list



    from seed.math.power.addition_chain.shortest.upper_bound4len_optimal_addition_chain import 实证估计冫上界纟最小显链长巛靶值牜次优牜精研综合扌, 估计冫上界纟最小显链长巛靶值牜速算牜精研综合扌
    #def 实证估计冫上界纟最小显链长巛靶值牜次优牜精研综合扌(靶值, /, *, 欤排除窗式拆分牜定窗式=False, 欤排除窗式拆分牜滑窗式=False):
    #    '靶值 -> (上界纟最小显链长{靶值}, 加链{靶值}{显链长==上界纟最小显链长{靶值}})'

    from seed.math.power.addition_chain.shortest.lower_bound4len_optimal_addition_chain import 估计冫下界纟最小显链长巛靶值牜精研综合扌
    #def 估计冫下界纟最小显链长巛靶值牜精研综合扌(靶值, /, *, 鬽上界纟最小显链长, 鬽上界纟总小步数=None, 欤排除数据验证部分=False):

    from seed.math.factor_pint_by_trial_division_ import factor_pint_by_trial_division_
    from seed.math.all_factors_of_ import 有序列表冫所有因数巛因数分解扌, 无序枚举冫所有因数巛因数分解扌
    from seed.math.power.addition_chain.shortest.rewrite import 缩写冫最短加链讠虚匏链扌, 简化冫虚匏链讠虚匏融介链纟最短加链扌
    #.def 缩写冫最短加链讠虚匏链扌(更小靶值讠最小显链长, 最短加链, /, *, 更小靶值讠最短加链=None):
    #.def 简化冫虚匏链讠虚匏融介链纟最短加链扌(虚匏链纟最短加链, /, *, _欤检查=True):
    from seed.math.power.addition_chain.shortest.rewrite import 另构冫最短加链巛虚匏链扌, 另构冫虚匏链巛虚匏融介链纟最短加链扌
    #.def 另构冫最短加链巛虚匏链扌(更小靶值讠最短加链, 虚匏链纟最短加链, /):
    #.def 另构冫虚匏链巛虚匏融介链纟最短加链扌(虚匏融介链纟最短加链, /, *, _欤检查=True):

with mk_ctx4lazy_import4funcs_(__name__, 'DynamicStackedMapping:mk_DynamicStackedMapping_'):
    from seed.types.mapping.DynamicStackedMapping import DynamicStackedMapping as mk_DynamicStackedMapping_
    # >>> p1 = d.env_tell()
    # >>> d.env_pop_until(p1)


#.#################################


#.from functools import cached_property
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
#see:dot_#from seed.func_tools.dot2 import dot
#.
#.from abc import update_abstractmethods
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
#.
#.#################################
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import8lazy_objs__ver2_
#.with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
#.    from __.seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset
#.#################################
#.from seed.helper.lazy_import__func import force_lazy_imported_func_ # lazy_import4func_, lazy_import4funcs_
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
#.with mk_ctx4lazy_import4funcs_(__name__):
#.    from seed.helper.repr_input import repr_helper
#.    from seed.tiny_.map_ import map_, cmap_, call_, prepare4call_, dots_
#.    from seed.tiny_.types5py import mk_MapView,curry1,kwargs2Attrs #,MapView
#.    from seed.tiny_.containers import mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_,mk_tuple__split_first_if_str,mk_tuple__split_first_if_str__sep_ #xxx:null_tuple
#.    from seed.debug.print_err import print_err
#.    from seed.debug.expectError import expectError
#.    from seed.helper.ifNone import ifNone,ifNonef
#.    from seed.tiny_.funcs import echo,fst,snd
#.    from seed.types.Either import mk_Left,mk_Right #Either,Cased
#.    from seed.iters.flatten_recur import flatten_recur
#.    # def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):
#.    from seed.func_tools.dot_ import dot_
#.    from seed.iters.PeekableIterator import echo_or_mk_PeekableIterator
#.    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import mk_named_pseudo_tuple_
#.    #def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
#.    #    def _check6make_(sf, /):
#.    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import collect_tuple_subclasses_with_cached_property
#.    #assert not (__:=collect_tuple_subclasses_with_cached_property(globals(), to_print_err=True)), __
#.#################################
#.:s/\v^from +([_[:alnum:].]+) +import +([^# ]( *[^# ])*).*/lazy_import4funcs_('\1', '\2', __name__)\rif 0:\0



#.#################################
#.from seed.types.LazyList import ToConcatLazyList, decorator4protocol4ToConcatLazyList_
#.from seed.types.LazyList import LazyList, LazyListError
#.from seed.types.LazyList import to_LazyList, to_LazyListIter
#.
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)

__all__





r'''[[[
根据对称性(对偶融介图:有向无环图 反转方向)，隐节点『1』参与加法构成的最高位 距离L0 对照 构成末节点的最低位 距离Lt => 要求:[Lt<=L0]
    或者:融介图 [末节点的入度 >= 隐节点的出度]
    注意:融介图里 次大点 出度为2或3！
    注意:融介图里 隐节点 参与 末点的构造，则 [显链长纟(靶值)==1+显链长纟(靶值-1)]
已知:更小靶值讠最小显链长:
    * 因数分解型:
        [显链长纟(靶值)==显链长纟(k)+显链长纟(靶值///k)]
    * 加一型:
        [显链长纟(靶值)==1+显链长纟(靶值-1)]
    * 加二型:
        [显链长纟(靶值)==1+显链长纟(靶值-2)]
    * 乘二三加一二型:
        [显链长纟(靶值)==2+显链长纟((靶值-1)///2)]
        [显链长纟(靶值)==2+显链长纟((靶值-2)///2)]
        [显链长纟(靶值)==3+显链长纟((靶值-1)///3)]
        [显链长纟(靶值)==3+显链长纟((靶值-2)///3)]
    * 辗转相除型:
        [显链长纟(靶值)==1+显链长纟(d)+显链长纟((靶值-r)///d)]
            ???是否存在最短加链{d}含r???

模板:考虑隐节点出边的最高位:
    * [隐节点参与末节点的构造]:
        加一型
        [显链长纟(靶值)==1+显链长纟(靶值-1)]
    * [隐节点不参与末节点的构造]:
        [隐节点出边的最高位落在中途]
        [j:=隐节点出边的最高位]
        [0<j<显链长]
        [n:=[j的跨越边的数量]]
        * [n==0]:
            因数分解型
        * [n==1]:
            连锁...
        * [n>=2]:
            交织...
    ...应该按 融介图 的 节点数 分类
    * [融介图共1节点]:
        * [1]
    * [融介图共2节点]:
        * [1,2]
        * [1,3]
    * [融介图共3节点]:
        [1,N,T]
        * [1,(N=1*N),(T=N*M)]
            #因数分解型
        * [1,(N=1*N),(T=N*M+1)]
            #加一型
    * [融介图共4节点]:
        [1,N,M,T]
        * [1,(N=1*N),(M=N*a+1),(T=M*b+N)]
            唯一有效种型，但 仍是星链构型
            [a>=1][N,b>=2][T==N*a*b+b+N]
                # [k>=1][x,y>=2]
                # k*x*y+x+y >= (x+1)*(y+1)-1
                # [T==(k*x+1)*(k*y+1)/k -1/k]
                # [1+k*T==(k*x+1)*(k*y+1)]
        ===以下3种:因数分解型:
        ?#* [1,(N=1*N),(M=N*a),(T=M*b)]
        ?#* [1,(N=1*N),(M=N*a+1),(T=M*b)]
        ?#* [1,(N=1*N),(M=N*a),(T=M*b+N)]
        ===以下4种:加一型:
        ?#* [1,(N=1*N),(M=N*a),(T=M*b+1)]
        ?#* [1,(N=1*N),(M=N*a+1),(T=M*b+1)]
        ?#* [1,(N=1*N),(M=N*a),(T=M*b+N+1)]
        ?#* [1,(N=1*N),(M=N*a+1),(T=M*b+N+1)]


e others/数学/exponential-20260102.txt
e others/数学/the_function-pow_u_u.txt
#]]]'''#'''





class 魖匴蛮力搜索器纟最短加链(魖匴渐深树搜索):
    '快照链vs搜索链vs重启链vs环节列表'
    __slots__ = ()
    @abstractmethod
    def 规范冫参数纟渐深搜索扌(sf, /, *args, **kwds):
        '-> (std_args, std_kwds)'
        return (args, kwds)

    @abstractmethod
    def 乊搜索起始牜批量树深扌(sf, /, *std_args, **std_kwds):
        '-> 状态牜跨深{内含:靶值}{内含:下上界纟树深}{内含:重启信息牜本次起始}'
    @abstractmethod
    def 抽取冫重启信息牜本次起始巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 重启信息牜本次起始'
    @abstractmethod
    def 求取冫鬽搜索链牜无需搜索巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 鬽搜索链'
    @abstractmethod
    def 取冫下上界纟树深巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 下上界纟树深/(下界纟树深, 上界纟树深)'
    @abstractmethod
    def 取冫鬽丮假想树深辻起始链厈牜重启巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 鬽 (假想树深牜重启, 起始链牜重启)'
    @abstractmethod
    def 取冫起始链巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 起始链牜跨深'
    @abstractmethod
    def 欤搜索链内容前缀扌(sf, 搜索链冃前缀, 搜索链冃全链, /):
        '搜索链冃前缀 -> 搜索链冃全链 -> 欤前缀/bool'
    @abstractmethod
    def 乊搜索起始牜指定树深扌(sf, 状态牜跨深, 假想树深, /):
        '状态牜跨深 -> 假想树深 -> 状态牜定深{内含:搜索链}{内含:假想树深}{内含:靶值}'
        #匴.构造冫状态牜定深巛状态牜跨深扌
    @abstractmethod
    def 求取冫鬽搜索链牜无需搜索巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 鬽搜索链'
        #eg:无需搜索:因数分解型、加一型
    @abstractmethod
    def 检查冫中靶搜索链扌(sf, 状态牜跨深, 搜索链, /):
        '状态牜跨深 -> 搜索链 -> None|^Exception'
    @abstractmethod
    def 快照冫搜索链扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 快照链{内含:搜索链}'
    @abstractmethod
    def 构造冫重启链巛快照链扌(sf, 快照链, /):
        '快照链{内含:搜索链} -> 重启链'
    @abstractmethod
    def 欤搜索链中靶扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 欤成功/bool'
    @abstractmethod
    def 欤搜索链可回溯扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 欤可回溯/欤可减位/bool'
    @abstractmethod
    def 欤搜索链可能有效扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链}{内含:假想树深}{内含:靶值} -> 欤有效/欤可增位/bool #[未超长{假想树深}][未中靶][未判定必然无法中靶]'
    @abstractmethod
    def 减位冫搜索链扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 状态牜定深'
        #匴.出栈冫搜索链扌
    @abstractmethod
    def 增位冫搜索链牜自动扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 状态牜定深 #[以候选名单中下一个候选者作为末位环节]'
        #匴.入栈冫搜索链扌
    @abstractmethod
    def 增位冫搜索链牜指定扌(sf, 环节冃末位, 状态牜定深, /):
        '环节冃末位 -> 状态牜定深{内含:搜索链} -> 状态牜定深|^Exception{末位环节不在候选名单上}'
    @abstractmethod
    def 拆分冫环节列表巛重启链扌(sf, 重启链, /):
        '重启链 -> 环节列表/[环节]'



    ################
    ################
    ################
    ################
    @override
    def 规范冫参数纟渐深搜索扌(sf, /, *args, 靶值, 下界纟最小显链长=None, 上界纟最小显链长=None, 鬽丮假想最小显链长辻起始链厈牜重启=None, **kwds):
        #def 规范冫参数纟渐深搜索扌(sf, /, *args, 靶值, 丮假想树深辻起始链厈牜重启=None, 下界纟树深=None, 上界纟树深=None, **kwds):
            #树深-->最小显链长
        '-> (std_args, std_kwds)'
        check_int_ge(1, 靶值)
        if 上界纟最小显链长 is None:
            (上界纟最小显链长, 加链冃证据) = 实证估计冫上界纟最小显链长巛靶值牜次优牜精研综合扌(靶值)
        check_int_ge(0, 上界纟最小显链长)
        if 下界纟最小显链长 is None:
            下界纟最小显链长 = 估计冫下界纟最小显链长巛靶值牜精研综合扌(靶值, 鬽上界纟最小显链长=上界纟最小显链长)
        check_int_ge(0, 下界纟最小显链长)
        check_int_ge(下界纟最小显链长, 上界纟最小显链长)
        if not 鬽丮假想最小显链长辻起始链厈牜重启 is None:
            丮假想最小显链长辻起始链厈牜重启 = 鬽丮假想最小显链长辻起始链厈牜重启
            check_pair(丮假想最小显链长辻起始链厈牜重启)
            (假想最小显链长牜重启, 起始链牜重启) = 丮假想最小显链长辻起始链厈牜重启
            check_int_ge_le(下界纟最小显链长, 上界纟最小显链长, 假想最小显链长牜重启)
            下界纟最小显链长 = 假想最小显链长牜重启
        kwds.update(靶值=靶值, 下界纟最小显链长=下界纟最小显链长, 上界纟最小显链长=上界纟最小显链长, 鬽丮假想最小显链长辻起始链厈牜重启=鬽丮假想最小显链长辻起始链厈牜重启)
        return (args, kwds)


    @override
    def 求取冫鬽搜索链牜无需搜索巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 鬽搜索链'
        匴 = sf
        靶值 = 匴.取冫靶值巛状态牜跨深扌(状态牜跨深)
        阳爻数纟靶值 = 阳爻数纟(靶值)
        if not 阳爻数纟靶值 >= 4:
            最短加链 = 构造冫加链巛靶值牜二进制拆分扌(靶值)
            搜索链 = 匴.搜索链巛状态牜跨深辻最短加链扌(状态牜跨深, 最短加链)#if 下界纟最小显链长 <= 显链长纟(最短加链) <= 上界纟最小显链长 else None
            鬽搜索链 = 搜索链
        else:
            鬽搜索链 = None
        return 鬽搜索链

    ################
    @abstractmethod
    def 取冫靶值巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深{内含:靶值} -> 靶值'
    @abstractmethod
    def 搜索链巛状态牜跨深辻最短加链扌(sf, 状态牜跨深, 最短加链, /):
        '状态牜跨深{内含:靶值} -> 最短加链{靶值} -> 搜索链'
    ################
    ################
    ################
#end-class 魖匴蛮力搜索器纟最短加链(魖匴渐深树搜索):

_起始加链 = (1,)
class 乸匴蛮力搜索器纟最短加链牜极简(魖匴蛮力搜索器纟最短加链):
    r'''[[[
    [树深 =[def]= 显链长] #假想最小显链长{靶值}
    [搜索链 =[def]= 严序加链]
    [快照链 =[def]= rglnkls(严序加链)]
    [重启链 =[def]= 搜索链{冻结}]
    [环节列表 =[def]= 重启链]
    [状态牜跨深 =[def]= (靶值, 下上界纟最小显链长, 丮假想最小显链长辻起始链厈牜重启)]
    [状态牜定深 =[def]= (靶值, 假想最小显链长, 址引讠下限, 候选名单栈, 搜索链, 快照链)]
        [(len(搜索链) -len(候选名单栈)) <- {0,1}]
    #]]]'''#'''
    __slots__ = ()

    @override
    def 乊搜索起始牜批量树深扌(sf, /, *, 靶值, 下界纟最小显链长, 上界纟最小显链长, 鬽丮假想最小显链长辻起始链厈牜重启):
        #def 乊搜索起始牜批量树深扌(sf, /, *std_args, **std_kwds):
        '-> 状态牜跨深{内含:靶值}{内含:下上界纟树深}{内含:重启信息牜本次起始}'
        下上界纟最小显链长 = (下界纟最小显链长, 上界纟最小显链长)
        状态牜跨深 = (靶值, 下上界纟最小显链长, 鬽丮假想最小显链长辻起始链厈牜重启)
        return 状态牜跨深
    @override
    def 抽取冫重启信息牜本次起始巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 重启信息牜本次起始'
        (靶值, 下上界纟最小显链长, 鬽丮假想最小显链长辻起始链厈牜重启) = 状态牜跨深
        重启信息牜本次起始 = 鬽丮假想最小显链长辻起始链厈牜重启
        return 重启信息牜本次起始
    @override
    def 取冫下上界纟树深巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 下上界纟树深/(下界纟树深, 上界纟树深)'
        (靶值, 下上界纟最小显链长, 鬽丮假想最小显链长辻起始链厈牜重启) = 状态牜跨深
        return 下上界纟最小显链长
    @override
    def 取冫鬽丮假想树深辻起始链厈牜重启巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 鬽 (假想树深牜重启, 起始链牜重启)'
        (靶值, 下上界纟最小显链长, 鬽丮假想最小显链长辻起始链厈牜重启) = 状态牜跨深
        return 鬽丮假想最小显链长辻起始链厈牜重启
    @override
    def 取冫起始链巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 起始链牜跨深'
        return _起始加链
    @override
    def 欤搜索链内容前缀扌(sf, 搜索链冃前缀, 搜索链冃全链, /):
        '搜索链冃前缀 -> 搜索链冃全链 -> 欤前缀/bool'
        L = len(搜索链冃前缀)
        return mk_tuple(搜索链冃前缀[:L]) == mk_tuple(搜索链冃全链[:L])
    @override
    def 乊搜索起始牜指定树深扌(sf, 状态牜跨深, 假想树深, /):
        '状态牜跨深 -> 假想树深 -> 状态牜定深{内含:搜索链}{内含:假想树深}{内含:靶值}'
        #匴.构造冫状态牜定深巛状态牜跨深扌
        (靶值, 下上界纟最小显链长, 鬽丮假想最小显链长辻起始链厈牜重启) = 状态牜跨深
        假想最小显链长 = 假想树深
        址引讠下限 = [None]*(1+假想最小显链长)
        址引讠下限[-1] = 靶值
        for j in reversed(range(假想最小显链长)):
            址引讠下限[j] = (1+址引讠下限[1+j])//2
        址引讠下限 = tuple(址引讠下限)
        候选名单栈 = []
        搜索链 = [1]
        快照链 = ((), 1)
        状态牜定深 = (靶值, 假想最小显链长, 址引讠下限, 候选名单栈, 搜索链, 快照链)
        # [(len(搜索链) -len(候选名单栈)) <- {0,1}]
        return 状态牜定深
    @override
    def 求取冫鬽搜索链牜无需搜索巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 鬽搜索链'
        #eg:无需搜索:因数分解型、加一型
        return None
    @override
    def 检查冫中靶搜索链扌(sf, 状态牜跨深, 搜索链, /):
        '状态牜跨深 -> 搜索链 -> None|^Exception'
        靶值 = 状态牜跨深[0]
        检查冫严序加链乊靶值扌(靶值, 加链:=搜索链)
    @override
    def 快照冫搜索链扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 快照链{内含:搜索链}'
        快照链 = 状态牜定深[-1]
        return 快照链
    @override
    def 构造冫重启链巛快照链扌(sf, 快照链, /):
        '快照链{内含:搜索链} -> 重启链'
        加链 = tuple(rglnkls2list(快照链))
        重启链 = 搜索链 = 加链
        return 重启链
    @override
    def 欤搜索链中靶扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 欤成功/bool'
        靶值 = 状态牜定深[0]
        快照链 = 状态牜定深[-1]
        return 靶值 == 快照链[-1]
    @override
    def 欤搜索链可回溯扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 欤可回溯/欤可减位/bool'
        搜索链 = 状态牜定深[-2]
        return len(搜索链) > 1
    @override
    def 欤搜索链可能有效扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链}{内含:假想树深}{内含:靶值} -> 欤有效/欤可增位/bool #[未超长{假想树深}][未中靶][未判定必然无法中靶]'
        匴 = sf
        (靶值, 假想最小显链长, 址引讠下限, 候选名单栈, 搜索链, 快照链) = 状态牜定深
        j = len(搜索链)-1
        if not len(候选名单栈) == j:
            assert len(候选名单栈) == 1+j
            return not 候选名单栈[j].is_empty()
        if not j <= 假想最小显链长:
            return False
        if not 址引讠下限[j] <= 搜索链[j] <= 靶值:
            return False
        if 搜索链[j] == 靶值:
            #中靶
            return True
        if not j < 假想最小显链长:
            #全链#即:非前缀
            return False
        #前缀
        if len(候选名单栈) == j:
            it = 枚举冫候选者牜严序加链扌(严序加链:=搜索链, 最大址引=j, 上限=靶值, 下限=址引讠下限[1+j])
            it = echo_or_mk_IPeekableIterator(it)
            候选名单栈.append(it)
        assert len(候选名单栈) == len(搜索链)
        return not 候选名单栈[j].is_empty()
    @override
    def 减位冫搜索链扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 状态牜定深'
        #匴.出栈冫搜索链扌
        (靶值, 假想最小显链长, 址引讠下限, 候选名单栈, 搜索链, 快照链) = 状态牜定深
        if len(候选名单栈) == len(搜索链):
            候选名单栈.pop()
        搜索链.pop()
        (快照链, _) = 快照链
        assert len(候选名单栈) == len(搜索链)
        状态牜定深 = (靶值, 假想最小显链长, 址引讠下限, 候选名单栈, 搜索链, 快照链)
        return 状态牜定深
    @override
    def 增位冫搜索链牜自动扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 状态牜定深 #[以候选名单中下一个候选者作为末位环节]'
        #匴.入栈冫搜索链扌
        (靶值, 假想最小显链长, 址引讠下限, 候选名单栈, 搜索链, 快照链) = 状态牜定深
        assert len(候选名单栈) == len(搜索链)
        x = 候选名单栈[-1].read1()
        搜索链.append(x)
        快照链 = (快照链, x)
        状态牜定深 = (靶值, 假想最小显链长, 址引讠下限, 候选名单栈, 搜索链, 快照链)
        return 状态牜定深
    @override
    def 增位冫搜索链牜指定扌(sf, 环节冃末位, 状态牜定深, /):
        '环节冃末位 -> 状态牜定深{内含:搜索链} -> 状态牜定深|^Exception{末位环节不在候选名单上}'
        匴 = sf
        (靶值, 假想最小显链长, 址引讠下限, 候选名单栈, 搜索链, 快照链) = 状态牜定深
        if not 匴.欤搜索链可能有效扌(状态牜定深):
            raise Exception('末位环节不在候选名单上', 环节冃末位)
        assert len(候选名单栈) == len(搜索链)
        if not len(候选名单栈) == len(搜索链):raise Exception('已然中靶？', 搜索链, 环节冃末位)
        #.if not len(候选名单栈) == len(搜索链):
        #.    j = len(搜索链)-1
        #.    it = 枚举冫候选者牜严序加链扌(严序加链:=搜索链, 最大址引=j, 上限=靶值, 下限=址引讠下限[1+j])
        #.    it = echo_or_mk_IPeekableIterator(it)
        #.    候选名单栈.append(it)
        #.assert len(候选名单栈) == len(搜索链)
        it = 候选名单栈[-1]
        u = 环节冃末位
        while 1:
            if it.is_empty():
                raise Exception('末位环节不在候选名单上', 环节冃末位)
            if it.head == u:
                break
            it.read1()
        状态牜定深 = 匴.增位冫搜索链牜自动扌(状态牜定深)
        return 状态牜定深

    @override
    def 拆分冫环节列表巛重启链扌(sf, 重启链, /):
        '重启链 -> 环节列表/[环节]'
        环节列表 = us = 重启链
        return 环节列表
    ################
    @override
    def 取冫靶值巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深{内含:靶值} -> 靶值'
        靶值 = 状态牜跨深[0]
        return 靶值
    @override
    def 搜索链巛状态牜跨深辻最短加链扌(sf, 状态牜跨深, 最短加链, /):
        '状态牜跨深{内含:靶值} -> 最短加链{靶值} -> 搜索链'
        搜索链 = 加链 = 最短加链
        return 搜索链
    ################
    ################
#end-class 乸匴蛮力搜索器纟最短加链牜极简(魖匴蛮力搜索器纟最短加链):


匴蛮力搜索器纟最短加链牜极简 = 乸匴蛮力搜索器纟最短加链牜极简()

def 蛮力搜索冫最短加链牜极简扌(*, 靶值, 下界纟最小显链长=None, 上界纟最小显链长=None, 鬽丮假想最小显链长辻起始链厈牜重启=None):
    鬽最短加链 = 鬽搜索链 = 匴蛮力搜索器纟最短加链牜极简.渐深搜索扌(**locals())
    return 鬽最短加链

def 枚举冫候选者牜严序加链扌(严序加链, /, *, 最大址引, 上限, 下限):
    '-> 候选名单/(Iter 候选者/uint)'
    if not 下限 <= 上限:
        return
    for j in reversed(range(1+最大址引)):
        v = 严序加链[j]
        m = 上限 -v
        n = 下限 -v
        if not v >= n: break
        if not m >= 1: continue
        for i in reversed(range(1+j)):
            u = 严序加链[i]
            if u <= m:
                break
        else:
            continue
        # [u <= m]
        i
        for i in reversed(range(1+i)):
            u = 严序加链[i]
            if not u >= n:
                break
            # [n <= u <= m]
            # [下限==v+n <= v+u <= v+m==上限]
            yield (v+u)
    return
#end-def 枚举冫候选者牜严序加链扌(严序加链, /, *, 最大址引, 上限, 下限):















__all__

r'''[[[
TODO:
[搜索链=[def]=加工链纟虚匏融介链纟最短加链]
    虚匏融介链=:
        [[1], ..., [u, -倍数, 址差...], ..., [u, 址差, 址差, 址差...], ...]
        view ../../python3_src/seed/math/power/addition_chain/shortest/rewrite.py
    实际使用的是 前缀纟加工链 更准确地说，是 前缀纟虚匏融介链的在线工作形态:
        加工链=虚匏融介链的在线工作形态=:
        [[0, (None, 1)], ..., [倍数or1, (址引, u), (址引, u)...], ...]
            * [0, (None, 1)]
            * [1, (址引, u), (址引, u), (址引, u)...]
            * [倍数{>=2}, (址引, u), (址引, u)...]
                首个 (址引, u)==(当前址引-1, 倍数*加工链[当前址引-1][-1][-1])

    @override
    def 规范冫参数纟渐深搜索扌(sf, /, *args, **kwds):
        '-> (std_args, std_kwds)'
        #eg:[None=>下上界纟最小显链长纟(靶值)]
        #eg:[None=>因数分解纟(靶值)]
        #eg:[None=>更小靶值讠最小显链长{靶值}]
#]]]'''#'''
def _TODO(): TODO-\
    r'''[[[
    加工链 相关 代码 移至:
mv to:
    view ../../python3_src/seed/math/power/addition_chain/shortest/rewrite.py
or:
    e ../../python3_src/seed/math/power/addition_chain/shortest/rewrite7processing.py
    ===
    加工链=虚匏融介链的在线工作形态=:
        [[0, (None, 1)], ..., [倍数or1, (址引, u), (址引, u)...], ...]
            * [0, (None, 1)]
            * [1, (址引, u), (址引, u), (址引, u)...]
            * [倍数{>=2}, (址引, u), (址引, u)...]
    ===
    虚匏融介链=:
        [[1], ..., [u, -倍数, 址差...], ..., [u, 址差, 址差, 址差...], ...]
        view ../../python3_src/seed/math/power/addition_chain/shortest/rewrite.py
    ===
    #]]]'''#'''
def 加工链巛最短加链扌(更小靶值讠最小显链长, 最短加链, /, *, to_immutable:bool):
    虚匏融介链 = 虚匏融介链巛最短加链扌(更小靶值讠最小显链长, 最短加链)
    加工链纟虚匏融介链纟最短加链 = 加工链巛虚匏融介链扌(虚匏融介链, to_immutable=to_immutable)
    return 加工链纟虚匏融介链纟最短加链
def 加工链讠最短加链扌(更小靶值讠最短加链, 加工链纟虚匏融介链纟最短加链, /):
    虚匏融介链纟最短加链 = 加工链讠虚匏融介链扌(加工链纟虚匏融介链纟最短加链, to_immutable=True)
    最短加链 = 虚匏融介链讠最短加链扌(更小靶值讠最短加链, 虚匏融介链纟最短加链)
    return 最短加链

def 虚匏融介链巛最短加链扌(更小靶值讠最小显链长, 最短加链, /):
    虚匏链纟最短加链 = 缩写冫最短加链讠虚匏链扌(更小靶值讠最小显链长, 最短加链)
    虚匏融介链纟最短加链 = 简化冫虚匏链讠虚匏融介链纟最短加链扌(虚匏链纟最短加链)
    return 虚匏融介链纟最短加链
def 虚匏融介链讠最短加链扌(更小靶值讠最短加链, 虚匏融介链纟最短加链, /):
    虚匏链纟最短加链 = 另构冫虚匏链巛虚匏融介链纟最短加链扌(虚匏融介链纟最短加链)
    最短加链 = 另构冫最短加链巛虚匏链扌(更小靶值讠最短加链, 虚匏链纟最短加链)
    return 最短加链

def 加工链巛虚匏融介链扌(虚匏融介链, /, *, to_immutable:bool):
    assert len(虚匏融介链) >= 1
    def fill_(址引, v, ls, 址差列表, /):
        for 址差 in 址差列表:
            assert 址差 >= 0
            址引 -= 址差
            assert 址引 >= 0
            v += 加工链[址引][-1][-1]
            ls.append((址引, v))
        return v
    加工链 = []
    for j, x in enumerate(虚匏融介链):
        assert (j == 0) is (len(x) == 1), (j, x)
        match x:
            case [1]:
                ls = [0, (None, 1)]
            case [u, 址差甲, 址差乙, *址差列表] if 址差甲 >= 0:
                址引 = j #len(加工链)
                v = 0
                ls = [1]
                v = fill_(址引, v, ls, [址差甲, 址差乙, *址差列表])
                assert u == v
            #case [u, -倍数, *址差列表] if 倍数 >= 2:
                #SyntaxError: invalid syntax
                #   『-倍数』
            case [u, 负倍数, *址差列表] if (倍数:=-负倍数) >= 2:
                址引 = j-1
                v += 倍数*加工链[址引][-1][-1]
                ls = [倍数, (址引, v)]
                v = fill_(址引, v, ls, 址差列表)
                assert u == v
            case _:
                raise Exception('格式错误:虚匏融介链', 虚匏融介链, j, x)
            #case
        ls
        加工链.append(ls)
    加工链
    if to_immutable:
        加工链 = tuple_map_tuple_(加工链)
    return 加工链
def tuple_map_tuple_(x, /):
    return tuple(map(mk_tuple, x))
    return tuple(map(tuple, x))
def 加工链讠虚匏融介链扌(加工链, /, *, to_immutable:bool):
    assert len(加工链) >= 1
    def fill_(址引, v, ls, ku_pairs, /):
        for k, u in ku_pairs:
            assert 0 <= k <= 址引
            v += 虚匏融介链[k][0]
            assert u == v
            址差 = 址引 -k
            assert 址差 >= 0
            ls.append(址差)
            址引 = k
        return v
    虚匏融介链 = []
    for j, x in enumerate(加工链):
        assert len(x) >= 2, (j, x)
        assert (j == 0) is (x[0] == 0), (j, x)
        match x:
            case [0, (None, 1)]:
                ls = [1]
            case [1, *ku_pairs]:
                u = ku_pairs[-1][-1]
                ls = [u]
                址引 = j
                v = 0
                v = fill_(址引, v, ls, ku_pairs)
                assert v == u
            case [倍数, *ku_pairs] if 倍数 >= 2:
                u = ku_pairs[-1][-1]
                址引 = j-1
                v = 虚匏融介链[址引][0]
                ls = [u, -倍数, (址引, v)]
                v = fill_(址引, v, ls, ku_pairs)
                assert v == u
            case _:
                raise Exception('格式错误:加工链{虚匏融介链}', 加工链, j, x)
            #case
        虚匏融介链.append(ls)
    虚匏融介链
    if to_immutable:
        虚匏融介链 = tuple_map_tuple_(虚匏融介链)
    return 虚匏融介链
def 检查冫加工链纟虚匏融介链乊靶值扌(靶值, 加工链纟虚匏融介链, /):
    #最短加链 = 加工链讠最短加链扌(更小靶值讠最短加链, 加工链纟虚匏融介链)
    虚匏融介链 = 加工链讠虚匏融介链扌(加工链纟虚匏融介链, to_immutable=True)
    if not 虚匏融介链[-1][0] == 靶值 == 加工链纟虚匏融介链[-1][-1]:raise TypeError
def 欤加工链内容前缀扌(加工链冃前缀, 加工链冃全链, /):
    L = len(加工链冃前缀)
    if not L <= len(加工链冃全链):
        return False
    L1 = L-1
    if not tuple_map_tuple_(加工链冃前缀[:L1]) == tuple_map_tuple_(加工链冃全链[:L1]):
        return False
    N = len(加工链冃前缀[L1])
    if not tuple(加工链冃前缀[L1]) == tuple(加工链冃全链[L1][:N]):
        return False
    return True

def 构造冫鬽丮显链长辻加一型加工链厈扌(更小靶值讠最小显链长, 靶值, /):
    '-> 鬽(显链长,加一型加工链)'
    check_int_ge(1, 靶值)
    if 靶值 == 1:
        return None
    # [靶值 >= 2]

    #加一型
    假想最小显链长 = 1+更小靶值讠最小显链长[靶值-1]
    #虚匏融介链=:
    #   [[1], ..., [u, -倍数, 址差...], ..., [u, 址差, 址差, 址差...], ...]
    #加工链=虚匏融介链的在线工作形态=:
    #   [[0, (None, 1)], ..., [倍数or1, (址引, u), (址引, u)...], ...]
    加工链 = [[0, (None, 1)], [靶值-1, (0, 靶值)]]
        #_起始加工链
    加工链 = tuple_map_tuple_(加工链)
    鬽丮显链长辻加一型加工链厈 = (假想最小显链长, 加工链)
    return 鬽丮显链长辻加一型加工链厈

def 构造冫鬽丮显链长辻最短因数分解型加工链厈扌(因数分解纟靶值, 更小靶值讠最小显链长, 靶值, /):
    '-> 鬽 (显链长,最短因数分解型加工链)'
    check_int_ge(1, 靶值)
    #因数分解型
    假想最小显链长 = 靶值+1
    uv = None
    for u in 有序列表冫所有因数巛因数分解扌(因数分解纟靶值):
        v = 靶值//u
        assert u*v == 靶值
        if not 2 <= u <= v:
            if not u <= v: break
            assert u == 1
            continue
        # [2 <= u <= v]
        显链长 = 更小靶值讠最小显链长[u]+更小靶值讠最小显链长[v]
        if 显链长 < 假想最小显链长:
            假想最小显链长 = 显链长
            uv = (u, v)
    if uv:
        (u, v) = uv
        加工链 = [[0, (None, 1)], [u, (0, u)], [v, (1, 靶值)]]
        加工链 = tuple_map_tuple_(加工链)
        鬽丮显链长辻最短因数分解型加工链厈 = (假想最小显链长, 加工链)
    else:
        # @[靶值 是 (1|素数)]
        鬽丮显链长辻最短因数分解型加工链厈 = None
    return 鬽丮显链长辻最短因数分解型加工链厈



class 魖匴蛮力搜索器纟加工链纟虚匏融介链纟最短加链牜复杂参数(魖匴蛮力搜索器纟最短加链):
    r'''[[[
    [搜索链 =[def]= 加工链纟虚匏融介链纟最短加链]
    ===
    加工链=虚匏融介链的在线工作形态=:
        [[0, (None, 1)], ..., [倍数or1, (址引, u), (址引, u)...], ...]
            * [0, (None, 1)]
            * [1, (址引, u), (址引, u), (址引, u)...]
            * [倍数{>=2}, (址引, u), (址引, u)...]
    ===
    虚匏融介链=:
        [[1], ..., [u, -倍数, 址差...], ..., [u, 址差, 址差, 址差...], ...]
        view ../../python3_src/seed/math/power/addition_chain/shortest/rewrite.py
    ===
    ===
    [状态牜跨深 =[def]= ???]
    [状态牜定深 =[def]= ???]
    ===
    #]]]'''#'''
    __slots__ = ()
    ################
    @override
    def 规范冫参数纟渐深搜索扌(sf, /, *args, **kwds):
        (args, kwds) = super().规范冫参数纟渐深搜索扌(*args, **kwds)
        def f(*, 靶值, 因数分解纟靶值=NotImplemented, 更小靶值讠最小显链长=NotImplemented, 鬽丮显链长辻加一型加工链厈=NotImplemented, 鬽丮显链长辻最短因数分解型加工链厈=NotImplemented, **kwds):
            #############
            if NotImplemented is 因数分解纟靶值:
                if 靶值 > 2**32:raise NotImplementedError
                因数分解纟靶值 = p2e = factor_pint_by_trial_division_(靶值)
            #############
            if NotImplemented is 更小靶值讠最小显链长:
                from seed.math.power.addition_chain.data.target_uint2may_len_optimal_addition_chain import 靶值讠最小显链长
                更小靶值讠最小显链长 = 靶值讠最小显链长[:靶值]
            #############
            if NotImplemented is 鬽丮显链长辻加一型加工链厈:
                鬽丮显链长辻加一型加工链厈 = 构造冫鬽丮显链长辻加一型加工链厈扌(更小靶值讠最小显链长, 靶值)
            #############
            if NotImplemented is 鬽丮显链长辻最短因数分解型加工链厈:
                鬽丮显链长辻最短因数分解型加工链厈 = 构造冫鬽丮显链长辻最短因数分解型加工链厈扌(因数分解纟靶值, 更小靶值讠最小显链长, 靶值)
            #############
            #############
            kwds.update(靶值=靶值, 因数分解纟靶值=因数分解纟靶值, 更小靶值讠最小显链长=更小靶值讠最小显链长, 鬽丮显链长辻加一型加工链厈=鬽丮显链长辻加一型加工链厈, 鬽丮显链长辻最短因数分解型加工链厈=鬽丮显链长辻最短因数分解型加工链厈)
            return kwds
        kwds = f(**kwds)
        return (args, kwds)

    #求取冫鬽搜索链牜无需搜索巛状态牜跨深扌<<==:
    @override
    def 搜索链巛状态牜跨深辻最短加链扌(sf, 状态牜跨深, 最短加链, /):
        '状态牜跨深{内含:靶值} -> 最短加链{靶值} -> 搜索链'
        匴 = sf
        更小靶值讠最小显链长 = 匴.取冫更小靶值讠最小显链长巛状态牜跨深扌(状态牜跨深)
        搜索链 = 加工链 = 加工链巛最短加链扌(更小靶值讠最小显链长, 最短加链, to_immutable=True)
        return 搜索链
    @override
    def 求取冫鬽搜索链牜无需搜索巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 鬽搜索链'
        #eg:无需搜索:因数分解型、加一型
        匴 = sf
        靶值 = 匴.取冫靶值巛状态牜定深扌(状态牜定深)
        假想最小显链长 = 匴.取冫假想最小显链长巛状态牜定深扌(状态牜定深)
        因数分解纟靶值 = 匴.取冫因数分解纟靶值巛状态牜定深扌(状态牜定深)
        更小靶值讠最小显链长 = 匴.取冫更小靶值讠最小显链长巛状态牜定深扌(状态牜定深)
        鬽丮显链长辻加一型加工链厈 = 匴.取冫鬽丮显链长辻加一型加工链厈巛状态牜定深扌(状态牜定深)
        鬽丮显链长辻最短因数分解型加工链厈 = 匴.取冫鬽丮显链长辻最短因数分解型加工链厈巛状态牜定深扌(状态牜定深)

        assert 阳爻数纟(靶值) >= 4
        assert 靶值 >= 15

        #加一型
        # !! [靶值 >= 2]
        (显链长, 加一型加工链) = 鬽丮显链长辻加一型加工链厈
        if 显链长 <= 假想最小显链长:
            if 显链长 < 假想最小显链长:raise Exception('[显链长 < 假想最小显链长]', 显链长, 假想最小显链长)
            搜索链 = 加一型加工链
            return 搜索链

        #因数分解型
        if 鬽丮显链长辻最短因数分解型加工链厈:
            (显链长,最短因数分解型加工链) = 鬽丮显链长辻最短因数分解型加工链厈
            if 显链长 <= 假想最小显链长:
                if 显链长 < 假想最小显链长:raise Exception('[显链长 < 假想最小显链长]', 显链长, 假想最小显链长)
                搜索链 = 最短因数分解型加工链
                return 搜索链

        return None


    ################
    @override
    def 取冫起始链巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 起始链牜跨深'
        # !! [搜索链 =[def]= 加工链]
        return _起始加工链
    @override
    def 欤搜索链内容前缀扌(sf, 搜索链冃前缀, 搜索链冃全链, /):
        '搜索链冃前缀 -> 搜索链冃全链 -> 欤前缀/bool'
        # !! [搜索链 =[def]= 加工链]
        return 欤加工链内容前缀扌(搜索链冃前缀, 搜索链冃全链)
    @override
    def 检查冫中靶搜索链扌(sf, 状态牜跨深, 搜索链, /):
        '状态牜跨深 -> 搜索链 -> None|^Exception'
        匴 = sf
        # !! [搜索链 =[def]= 加工链]
        加工链 = 搜索链
        靶值 = 匴.取冫靶值巛状态牜跨深扌(状态牜跨深)
        检查冫加工链纟虚匏融介链乊靶值扌(靶值, 加工链)




    ################
    ################
    @abstractmethod
    def 取冫靶值巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 靶值'
    @abstractmethod
    def 取冫假想最小显链长巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 假想最小显链长'
    @abstractmethod
    def 取冫因数分解纟靶值巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 因数分解纟靶值'
    @abstractmethod
    def 取冫更小靶值讠最小显链长巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 更小靶值讠最小显链长'
    @abstractmethod
    def 取冫更小靶值讠最小显链长巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 更小靶值讠最小显链长'

    @abstractmethod
    def 取冫鬽丮显链长辻加一型加工链厈巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 鬽丮显链长辻加一型加工链厈'
    @abstractmethod
    def 取冫鬽丮显链长辻最短因数分解型加工链厈巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 鬽丮显链长辻最短因数分解型加工链厈'
    ################
#end-class 魖匴蛮力搜索器纟加工链纟虚匏融介链纟最短加链牜复杂参数(魖匴蛮力搜索器纟最短加链):

#状态牜共通
乸状态牜共通牜加工链 = namedtuple('乸状态牜共通牜加工链', '靶值 因数分解纟靶值 更小靶值讠最小显链长 鬽丮显链长辻加一型加工链厈 鬽丮显链长辻最短因数分解型加工链厈')
            #平坦址引讠下限
            #   但是考虑到 义务出度，不太可能是 静态数据
#状态牜跨深
乸状态牜跨深牜加工链 = namedtuple('乸状态牜跨深牜加工链', '状态牜共通 下上界纟最小显链长 鬽丮假想最小显链长辻起始链厈牜重启')
    #乊搜索起始牜批量树深扌
#状态牜定深
乸状态牜定深牜加工链 = namedtuple('乸状态牜定深牜加工链', '状态牜共通 假想最小显链长 候选名单栈 搜索链 环节列表 快照链')
    #乊搜索起始牜指定树深扌
_起始加工链 = ((0, (None, 1)),)
_起始环节链纟加工链 = ((), (-1, (None, 1)))
class 囗暂停冫乸匴蛮力搜索器纟加工链纟虚匏融介链纟最短加链(魖匴蛮力搜索器纟加工链纟虚匏融介链纟最短加链牜复杂参数):
    '暂停:因为发现搜索效率 并没有提高多少;现在转向:贪婪型二幂环要链'
    r'''[[[
    ===
    [状态牜跨深 =[def]= ???乸状态牜跨深牜加工链]
    [状态牜定深 =[def]= ???乸状态牜定深牜加工链]
    [快照链 =[def]= rglnkls(环节列表) :: rglnkls{环节}]
    [环节列表 :: [环节]]
        [(len(环节列表) -len(候选名单栈)) <- {0,1}]
    [环节 =[def]= (况态纟环节牜加工链, 负载纟环节牜加工链) = ((-1,(None,1))|(0,(址引,u))|(1,(址引,u),(址引,u))|(倍数{>=2},(址引,u)))]
    [况态纟环节牜加工链 <- [-1..]]
    ===
    #]]]'''#'''
    __slots__ = ()
    ################
    @override
    def 乊搜索起始牜批量树深扌(sf, /, *, 靶值, 下界纟最小显链长, 上界纟最小显链长, 鬽丮假想最小显链长辻起始链厈牜重启, 因数分解纟靶值, 更小靶值讠最小显链长, 鬽丮显链长辻加一型加工链厈, 鬽丮显链长辻最短因数分解型加工链厈):
        #def 乊搜索起始牜批量树深扌(sf, /, *std_args, **std_kwds):
        '-> 状态牜跨深{内含:靶值}{内含:下上界纟树深}{内含:重启信息牜本次起始}'
        状态牜共通 = 乸状态牜共通牜加工链(靶值, 因数分解纟靶值, 更小靶值讠最小显链长, 鬽丮显链长辻加一型加工链厈, 鬽丮显链长辻最短因数分解型加工链厈)
        下上界纟最小显链长 = (下界纟最小显链长, 上界纟最小显链长)
        状态牜跨深 = 乸状态牜跨深牜加工链(状态牜共通, 下上界纟最小显链长, 鬽丮假想最小显链长辻起始链厈牜重启)
        return 状态牜跨深
    @override
    def 抽取冫重启信息牜本次起始巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 重启信息牜本次起始'
        #.return sf.取冫鬽丮假想树深辻起始链厈牜重启巛状态牜跨深扌(状态牜跨深)
        return 状态牜跨深.鬽丮假想最小显链长辻起始链厈牜重启
    @override
    def 取冫下上界纟树深巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 下上界纟树深/(下界纟树深, 上界纟树深)'
        return 状态牜跨深.下上界纟最小显链长
    @override
    def 取冫鬽丮假想树深辻起始链厈牜重启巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 鬽 (假想树深牜重启, 起始链牜重启)'
        return 状态牜跨深.鬽丮假想最小显链长辻起始链厈牜重启
    @override
    def 乊搜索起始牜指定树深扌(sf, 状态牜跨深, 假想树深, /):
        '状态牜跨深 -> 假想树深 -> 状态牜定深{内含:搜索链}{内含:假想树深}{内含:靶值}'
        #匴.构造冫状态牜定深巛状态牜跨深扌
        状态牜共通 = 状态牜跨深.状态牜共通
        假想最小显链长 = 假想树深
        候选名单栈 = []
        搜索链 = 加工链 = [*_起始加工链]
        #显链长 = 0
        环节列表 = [_起始环节链纟加工链[-1]]
        快照链 = 环节链 = _起始环节链纟加工链#((), (-1, (None, 1)))
        状态牜定深 = 乸状态牜定深牜加工链(状态牜共通, 假想最小显链长, 候选名单栈, 搜索链, 环节列表, 快照链) #, ???
        # [(len(环节列表) -len(候选名单栈)) <- {0,1}]
        return 状态牜定深
    @override
    def 快照冫搜索链扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 快照链{内含:搜索链}'
        return 状态牜定深.快照链
    @override
    def 构造冫重启链巛快照链扌(sf, 快照链, /):
        '快照链{内含:搜索链} -> 重启链'
        环节链 = 快照链
        环节列表 = rglnkls2list(环节链)
        加工链 = 加工链巛环节列表扌(环节列表)
        重启链 = 搜索链 = 加工链
        return 重启链
    @override
    def 欤搜索链中靶扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 欤成功/bool'
        匴 = sf
        环节链 =  状态牜定深.快照链
        环节 = 环节链[-1]
        靶值 = 匴.取冫靶值巛状态牜定深扌(状态牜定深)
        return 环节[-1][-1] == 靶值
    @override
    def 欤搜索链可回溯扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 欤可回溯/欤可减位/bool'
        搜索链 =  状态牜定深.搜索链
        return len(搜索链) > 1
    @override
    def 欤搜索链可能有效扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链}{内含:假想树深}{内含:靶值} -> 欤有效/欤可增位/bool #[未超长{假想树深}][未中靶][未判定必然无法中靶]'
        匴 = sf
        match 状态牜定深:
            case 乸状态牜定深牜加工链(乸状态牜共通牜加工链(靶值, 因数分解纟靶值, 更小靶值讠最小显链长, 鬽丮显链长辻加一型加工链厈, 鬽丮显链长辻最短因数分解型加工链厈) as 状态牜共通, 假想最小显链长, 候选名单栈, 搜索链, 环节列表, 快照链):
                加工链 = 搜索链
                pass
            case _:
                raise TypeError(type(状态牜定深))
        j = len(环节列表)-1
        if not len(候选名单栈) == j:
            assert len(候选名单栈) == 1+j
            return not 候选名单栈[j].is_empty()
        if not j <= 假想最小显链长:
            # [超长]
            return False
        # [j <= 假想最小显链长]
        # [未超长]
        末值 = 环节列表[j][-1][-1]
        if not 末值 <= 靶值:
            #已然不可能中靶
            return False
        if 末值 == 靶值:
            #中靶
            return True
        # [未超长][未中靶]
        if not j < 假想最小显链长:
            # [未中靶][截止]
            return False
        # [j < 假想最小显链长]
        # [未中靶][未截止]
        剩余链长 = 假想最小显链长 -j
        assert 剩余链长 > 0
        下限牜当前位 = 靶值 >> 剩余链长
        if not 下限牜当前位 <= 末值:
            return False
        # [未中靶][未截止][可行]
        #前缀
        if len(候选名单栈) == j:
            #.it = 匴.枚举冫候选者牜加工链扌(加工链, 状态牜定深=状态牜定深, 最大址引纟环节列表=j, 最大址引纟加工链=len(加工链)-1, 剩余链长=剩余链长, 上限=靶值, 下限牜当前位牜尾附型=下限牜当前位牜尾附型, 下限牜开山型=下限牜后一位牜开山型)
            it = 匴.枚举冫候选者牜加工链扌(状态牜定深)
            it = echo_or_mk_IPeekableIterator(it)
            候选名单栈.append(it)
        assert len(候选名单栈) == len(环节列表)
        return not 候选名单栈[j].is_empty()

    @override
    def 减位冫搜索链扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 状态牜定深'
        #匴.出栈冫搜索链扌
        TODO
    @override
    def 增位冫搜索链牜自动扌(sf, 状态牜定深, /):
        '状态牜定深{内含:搜索链} -> 状态牜定深 #[以候选名单中下一个候选者作为末位环节]'
        #匴.入栈冫搜索链扌
        TODO
    @override
    def 增位冫搜索链牜指定扌(sf, 环节冃末位, 状态牜定深, /):
        '环节冃末位 -> 状态牜定深{内含:搜索链} -> 状态牜定深|^Exception{末位环节不在候选名单上}'
        匴 = sf
        候选名单栈 = 状态牜定深.候选名单栈
        环节列表 = 状态牜定深.环节列表
        if not 匴.欤搜索链可能有效扌(状态牜定深):
            raise Exception('末位环节不在候选名单上', 环节冃末位)
        if not len(候选名单栈) == len(环节列表):raise Exception('已然中靶？', 环节列表, 环节冃末位)
        it = 候选名单栈[-1]
        u = 环节冃末位
        while 1:
            if it.is_empty():
                raise Exception('末位环节不在候选名单上', 环节冃末位)
            if it.head == u:
                break
            it.read1()
        状态牜定深 = 匴.增位冫搜索链牜自动扌(状态牜定深)
        return 状态牜定深


    @override
    def 拆分冫环节列表巛重启链扌(sf, 重启链, /):
        '重启链 -> 环节列表/[环节]'
        加工链 = 搜索链 = 重启链
        环节列表 = 加工链讠环节列表扌(加工链)
        return 环节列表



    ################
    ################
    @override
    def 取冫靶值巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深{内含:靶值} -> 靶值'
        return 状态牜跨深.状态牜共通.靶值
    ################
    @override
    def 取冫靶值巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 靶值'
        return 状态牜定深.状态牜共通.靶值
    @override
    def 取冫假想最小显链长巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 假想最小显链长'
        return 状态牜定深.假想最小显链长
    @override
    def 取冫因数分解纟靶值巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 因数分解纟靶值'
        return 状态牜定深.状态牜共通.因数分解纟靶值
    @override
    def 取冫更小靶值讠最小显链长巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 更小靶值讠最小显链长'
        return 状态牜定深.状态牜共通.更小靶值讠最小显链长
    @override
    def 取冫更小靶值讠最小显链长巛状态牜跨深扌(sf, 状态牜跨深, /):
        '状态牜跨深 -> 更小靶值讠最小显链长'
        return 状态牜跨深.状态牜共通.更小靶值讠最小显链长

    ################
    @override
    def 取冫鬽丮显链长辻加一型加工链厈巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 鬽丮显链长辻加一型加工链厈'
        return 状态牜定深.状态牜共通.鬽丮显链长辻最短因数分解型加工链厈
    @override
    def 取冫鬽丮显链长辻最短因数分解型加工链厈巛状态牜定深扌(sf, 状态牜定深, /):
        '状态牜定深 -> 鬽丮显链长辻最短因数分解型加工链厈'
        return 状态牜定深.状态牜共通.鬽丮显链长辻最短因数分解型加工链厈
    ################
    ################
    #def 枚举冫候选者牜严序加链扌(严序加链, /, *, 最大址引, 上限, 下限):
    #def 枚举冫候选者牜加工链扌(sf, 加工链, /, *, 状态牜定深, 最大址引纟环节列表, 最大址引纟加工链, 剩余链长, 上限, 下限牜当前位牜尾附型, 下限牜开山型):
    def 枚举冫候选者牜加工链扌(sf, 状态牜定深, /):
        '-> 候选名单/(Iter 候选者/环节)'
        #assert 加工链 is 状态牜定深.搜索链
        义务出度表 = 状态牜定深.义务出度表
        匴 = sf
        #...先枚举:尾附型环节...
        #...再枚举:开山型环节...
        yield from 匴.枚举冫候选者牜加工链牜尾附型扌(状态牜定深)
        yield from 匴.枚举冫候选者牜加工链牜开山型扌(状态牜定深)
        return

    def 枚举冫候选者牜加工链牜尾附型扌(sf, 状态牜定深, /):
        '-> 候选名单/(Iter 候选者/环节)'
        #...#...先枚举:尾附型环节...
        #...j = len(环节列表)-1
        #...剩余链长 = 假想最小显链长 -j
        #...末值 = 加工链[-1][-1][-1]
        #...if j > 0:
        #...    #bug:次末值 = 环节列表[j-1][-1][-1]
        #...    次末值 = 加工链[-2][-1][-1]
        #...    # !! [已排除:因数分解型]
        #...    下限牜当前位牜尾附型 = 1+((靶值 -次末值-1)>>(剩余链长-1))
        #...    # [下限牜当前位牜尾附型 == ceil((靶值 -次末值)/2**(剩余链长-1))]
        #...else:
        #...    下限牜当前位牜尾附型 = 2
        #...下限牜当前位牜尾附型
        #...if not 下限牜当前位牜尾附型 <= 上限:
        #...    return
        #...下限牜追加数 = 下限牜当前位牜尾附型 -末值

    def 枚举冫候选者牜加工链牜开山型扌(sf, 状态牜定深, /):
        '-> 候选名单/(Iter 候选者/环节)'
        #...#...再枚举:开山型环节...
        #...j = len(环节列表)-1
        #...剩余链长 = 假想最小显链长 -j
        #...末值 = 加工链[-1][-1][-1]
        #...# !! [已排除:因数分解型]
        #...下限牜后一位牜开山型 = 1+((靶值 -末值-1)>>(剩余链长-1))
        #...# [下限牜后一位牜开山型 == ceil((靶值 -末值)/2**(剩余链长-1))]

        #...下限牜后一位牜开山型
        #...if not 下限牜开山型 <= 上限:
        #...    return
        #...for j in reversed(range(1+最大址引)):
        #...    融介节 = 加工链[j]
        #...    v = 融介节[-1][-1]
        #...    m = 上限 -v
        #...    n = 下限牜开山型 -v
        #...    if not v >= n: break
        #...    if not m >= 1: continue
        #...    for i in reversed(range(1+j)):
        #...        u = 严序加链[i]
        #...        if u <= m:
        #...            break
        #...    else:
        #...        continue
        #...    # [u <= m]
        #...    i
        #...    for i in reversed(range(1+i)):
        #...        u = 严序加链[i]
        #...        if not u >= n:
        #...            break
        #...        # [n <= u <= m]
        #...        # [下限牜开山型==v+n <= v+u <= v+m==上限]
        #...        yield (v+u)
        #...return

#:        TODO
#:        ++义务出度表::{u:剩余义务出度{>=1}{<=2}}
#:        his
#:view ../../python3_src/seed/math/power/addition_chain/common/README-defs.txt
#:    #[:猜想:根据剩余链长辻虚匏融介链耂前缀链耂义务出度求最大靶值乊排除冫加一型丶因数分解型]:goto
#:mk_DynamicStackedMapping_()
#:>>> p1 = d.env_tell()
#:>>> d.env_pop_until(p1)
#:    ################
'暂停:因为发现搜索效率 并没有提高多少;现在转向:贪婪型二幂环要链'
#end-class 乸匴蛮力搜索器纟加工链纟虚匏融介链纟最短加链(魖匴蛮力搜索器纟加工链纟虚匏融介链纟最短加链牜复杂参数):




__all__
#.class 魖匴前缀无效判定器纟加工链纟虚匏融介链纟最短加链(ABC):
#.    r'''[[[
#.    '匴前缀无效判定器{加工链纟虚匏融介链纟最短加链}'
#.
#.    加工链纟虚匏融介链纟最短加链
#.    虚匏融介链:
#.        [[1], ..., [u, -倍数, 址差...], ..., [u, 址差, 址差, 址差...], ...]
#.        view ../../python3_src/seed/math/power/addition_chain/shortest/rewrite.py
#.    实际使用的是 前缀纟加工链 更准确地说，是 前缀纟虚匏融介链的在线工作形态:
#.        加工链=虚匏融介链的在线工作形态=:
#.        [[0, (None, 1)], ..., [倍数or1, (址引, u), (址引, u)...], ...]
#.            * [0, (None, 1)]
#.            * [1, (址引, u), (址引, u), (址引, u)...]
#.            * [倍数{>=2}, (址引, u), (址引, u)...]
#.                首个 (址引, u)==(当前址引-1, 倍数*加工链[当前址引-1][-1][-1])
#.    #]]]'''#'''
#.    #额外参数:, 鬽因数分解纟靶值, 更小靶值讠最短加链, 更小靶值讠最小显链长
#.    __slots__ = ()
#.    @abstractmethod
#.    def 乊搜索起始纟批量处理扌(sf, 靶值, /, *, 欤显示冗杂调试信息, **额外参数):
#.        '靶值{>=15}{log2(靶值)%1=!=1}{阳爻数{靶值}>=4} -> 状态纟批次 | ^Exception # 做些针对 靶值 的冗长计算，比如:因数分解，异常出现时 分解结果 通过 保存冫状态纟批次讠部分具名参数扌 /保存冫状态纟无效判定讠额外具名参数扌 输出到 标准错误输出文件'
#.    @abstractmethod
#.    def 保存冫状态纟批次讠部分具名参数扌(sf, 状态纟批次, /):
#.        '状态纟批次{靶值} -> 部分具名参数{可读性数据}/kwds{.乊搜索起始纟批量处理扌.额外参数}'
#.    #下面 难以使用:异常出现时，b_goback多次...
#.    #.@abstractmethod
#.    #.def 保存冫状态纟无效判定讠额外具名参数扌(sf, 状态纟无效判定, /):
#.    #.    '状态纟无效判定{靶值,假想最小显链长} -> 额外具名参数{可读性数据}/kwds{.乊搜索起始纟批量处理扌.额外参数}'
#.    @abstractmethod
#.    def 乊搜索起始乊假想显链长扌(sf, 状态纟批次, 假想最小显链长, /):
#.        '状态纟批次{靶值} -> 假想最小显链长 -> Either 最短加链{靶值} 状态纟无效判定 | ^Exception # 起始:[前缀纟加工链 == [(0, (None, 1))]/[1]]'
#.    @abstractmethod
#.    def 欤加工链前缀无效扌(sf, 状态纟无效判定, /):
#.        '状态纟无效判定 -> 欤加工链前缀无效/bool'
#.    #@abstractmethod
#.    def 求取冫鬽下上界纟后一位扌(sf, 状态纟无效判定, /):
#.        '[0 <= 当前显链长 < 假想最小显链长][not 欤加工链前缀无效] => 状态纟无效判定 -> 后几位/uint{>=1} -> 鬽 (下界纟后一位, 上界纟后一位)'
#.        return sf.求取冫鬽下上界纟后几位扌(状态纟无效判定, 1)
#.    @abstractmethod
#.    def 求取冫鬽下上界纟后几位扌(sf, 状态纟无效判定, 后几位, /):
#.        '[0 <= 当前显链长 < 假想最小显链长][not 欤加工链前缀无效] => 状态纟无效判定 -> 后几位/uint{>=1} -> 鬽 (下界纟后几位, 上界纟后几位)'
#.    @abstractmethod
#.    def 乊加链前缀增位牜另起一行牜倍增扌(sf, 状态纟无效判定, 值纟后一位, 倍数, /):
#.        '[0 <= 当前显链长 < 假想最小显链长][not 欤加工链前缀无效][下界纟后一位<=值纟后一位<=上界纟后一位] => 状态纟无效判定 -> 值{后一位} -> 倍数 -> 状态纟无效判定'
#.    @abstractmethod
#.    def 乊加链前缀增位牜另起一行牜降序加俩扌(sf, 状态纟无效判定, 值纟后一位, 址引纟大加数, 址引纟小加数, /):
#.        '[0 <= 当前显链长 < 假想最小显链长][not 欤加工链前缀无效][下界纟后一位<=值纟后一位<=上界纟后一位] => 状态纟无效判定 -> 值{后一位} -> 址引纟大加数 -> 址引纟小加数 -> 状态纟无效判定'
#.    @abstractmethod
#.    def 乊加链前缀增位牜行尾降序追加扌(sf, 状态纟无效判定, 值纟后一位, 址引纟加数, /):
#.        '[0 <= 当前显链长 < 假想最小显链长][not 欤加工链前缀无效][下界纟后一位<=值纟后一位<=上界纟后一位] => 状态纟无效判定 -> 值{后一位} -> 址引纟加数{后一位} -> 状态纟无效判定'
#.    @abstractmethod
#.    def 乊加链前缀减位扌(sf, 状态纟无效判定, /):
#.        '[0 < 当前显链长 <= 假想最小显链长] => 状态纟无效判定 -> 状态纟无效判定'
#.
#.
#.
#.必要前缀纟加工链 = ((0, (None, 1)),)
#.def 冻结冫加工链扌(加工链, /):
#.    assert 加工链
#.    return tuple(map(tuple, 加工链))
#.def 靶值巛加工链扌(加工链, /):
#.    assert 加工链
#.    return 加工链[-1][-1][-1]
#.def 显链长巛加工链扌(加工链, /):
#.    assert 加工链
#.    return sum(map(len, 加工链)) -len(加工链) -1
#.___begin_mark_of_excluded_global_names__99___ = ...
#.def 规范输入扌(sf, 匴前缀无效判定器纟加工链纟虚匏融介链纟最短加链, 靶值, 鬽丮前缀纟加工链辻欤回溯中厈, 彧下界纟最小显链长, 彧上界纟最小显链长, 欤显示冗杂调试信息):
#.    鬽加工链 = None
#.    while 1:
#.        ######################
#.        #规范输入阶段:
#.        ######################
#.        check_type_le(魖匴前缀无效判定器纟加工链纟虚匏融介链纟最短加链, 匴前缀无效判定器纟加工链纟虚匏融介链纟最短加链)
#.        check_int_ge(1, 靶值)
#.        check_type_is(bool, 欤显示冗杂调试信息)
#.        ######################
#.        if 彧上界纟最小显链长 is ...:
#.            (上界纟最小显链长, 加链冃证据) = 实证估计冫上界纟最小显链长巛靶值牜次优牜精研综合扌(靶值)
#.        else:
#.            上界纟最小显链长 = 彧上界纟最小显链长
#.        上界纟最小显链长
#.        check_int_ge(0, 上界纟最小显链长)
#.        ######################
#.        if 彧下界纟最小显链长 is ...:
#.            下界纟最小显链长 = 估计冫下界纟最小显链长巛靶值牜精研综合扌(靶值, 鬽上界纟最小显链长=上界纟最小显链长)
#.        else:
#.            下界纟最小显链长 = 彧下界纟最小显链长
#.        下界纟最小显链长
#.        check_int_ge(0, 下界纟最小显链长)
#.        ######################
#.        ######################
#.        verbose = 欤显示冗杂调试信息
#.        ######################
#.        sf.罓乊测试扌(靶值=靶值, case4starting=-1, 假想最小显链长=-1)
#.        if not 下界纟最小显链长 <= 上界纟最小显链长:
#.            return None
#.        # [下界纟最小显链长 <= 上界纟最小显链长]
#.        前缀纟加工链 = [] if None is 鬽前缀纟加工链 else [*map(list, 鬽前缀纟加工链)]
#.        if not 前缀纟加工链:
#.            前缀纟加工链.append(必要前缀纟加工链)
#.        if not type(前缀纟加工链[0]) is tuple:
#.            前缀纟加工链[0] = tuple(前缀纟加工链[0])
#.        if not 前缀纟加工链[0] == 必要前缀纟加工链:raise ValueError(前缀纟加工链)
#.        # [1 <= len(前缀纟加工链)]
#.        # [0 <= 显链长巛加工链扌(前缀纟加工链)]
#.        if not 显链长巛加工链扌(前缀纟加工链) <= 上界纟最小显链长:raise Exception
#.        # [0 <= 显链长巛加工链扌(前缀纟加工链) <= 上界纟最小显链长]
#.        if not 显链长巛加工链扌(前缀纟加工链) <= 下界纟最小显链长: raise Exception('输入应当是: [前缀纟加工链 := 前缀纟加工链{乊前次搜索异常退出}][下界纟最小显链长 := 假想最小显链长{乊前次搜索异常退出}]')
#.        # [显链长巛加工链扌(前缀纟加工链) <= 下界纟最小显链长]
#.        # !! [下界纟最小显链长 <= 上界纟最小显链长]
#.        # 下界纟最小显链长 = max(下界纟最小显链长, 显链长巛加工链扌(前缀纟加工链))
#.        # [0 <= 显链长巛加工链扌(前缀纟加工链) <= 下界纟最小显链长 <= 上界纟最小显链长]
#.        检查冫严序加链内容扌(前缀纟加工链)
#.        检查冫严序加工链内容扌(前缀纟加工链)
#.        # [前缀纟加工链 <- 乸严序加工链]
#.        if 靶值巛加工链扌(前缀纟加工链) > 靶值: raise Exception
#.        if 靶值巛加工链扌(前缀纟加工链) == 靶值:
#.            # !! [0 <= 显链长巛加工链扌(前缀纟加工链) <= 下界纟最小显链长 <= 上界纟最小显链长]
#.            # !! [前缀纟加工链 <- 乸严序加工链]
#.            return 冻结冫加工链扌(前缀纟加工链)
#.            raise Exception
#.        # [靶值巛加工链扌(前缀纟加工链) < 靶值]
#.        阳爻数纟靶值 = 阳爻数纟(靶值)
#.        if not 阳爻数纟靶值 >= 4:
#.            最短加链 = 构造冫加链巛靶值牜二进制拆分扌(靶值)
#.            return 加工链巛最短加链扌(更小靶值讠最小显链长, 最短加链, to_immutable=True) if 下界纟最小显链长 <= 显链长纟(最短加链) <= 上界纟最小显链长 else None
#.        # [阳爻数{靶值} >= 4]
#.        # [靶值 >= 15]
#.        assert 靶值 >= 15
#.        首爻位纟靶值 = 首爻位纟(靶值)
#.        下界纟最小显链长 = max(下界纟最小显链长, 首爻位纟靶值+2)
#.        if not 下界纟最小显链长 <= 上界纟最小显链长:
#.            return None
#.        # [下界纟最小显链长 <= 上界纟最小显链长]
#.        ######################
#.
#.
#.
#.    return (鬽加工链, 匴前缀无效判定器纟加工链纟虚匏融介链纟最短加链, 靶值, 前缀纟加工链, 欤回溯中, 下界纟最小显链长, 上界纟最小显链长)
#.def 直达前缀扌(sf, 匴, 靶值, 前缀纟加工链, 链, st):
#.    stk = []
#.    for u in 前缀纟加工链[1:]:
#.        # [len(链) == 1+len(stk)]
#.        # [len(链) < len(前缀纟加工链)]
#.        # [链 == 前缀纟加工链[:len(链)]]
#.        # [st <~~ 链[-1]]
#.        hp = _4mk_heap4next(sf, 匴, 靶值, 链, st, 上界=u, **kwds4hp)
#.        if not (hp and hp.head.u == u):
#.            # [hp !<- stk]
#.            # [not hp]or[hp[0] !<- 链]
#.            break # (链, stk, st, hp{next})
#.        # [hp[0].u == u]
#.        stk.append(hp)
#.        链.append(u)
#.        # [len(链) <= len(前缀纟加工链)]
#.        # [链 == 前缀纟加工链[:len(链)]]
#.        777;st = 匴.乊加链前缀增位扌(st, u, hp.head.ji_ls)
#.        # [st <~~ 链[-1]]
#.        # [stk[-1][0].u == 链[-1]]
#.        # [len(链) == 1+len(stk)]
#.        # [stk[j-1][0].u == 链[j]]
#.    else:
#.        hp = _4mk_heap4next(sf, 匴, 靶值, 链, st, 上界=None, **kwds4hp)
#.        # [hp !<- stk]
#.        # [hp[0] !<- 链]
#.    ########
#.    # (链, stk, st, hp{next})
#.    ########
#.    # [st <~~ 链[-1]]
#.    ########
#.    # [hp !<- stk]
#.    # [not hp]or[hp[0] !<- 链]
#.    ########
#.    # [1 <= len(链) <= len(前缀纟加工链) <= 1+假想最小显链长]
#.    # [链 == 前缀纟加工链[:len(链)]]
#.    # !! [前缀纟加工链[-1] < 靶值]
#.    # [链[-1] < 靶值]
#.    # [1 <= len(链) <= 1+假想最小显链长]
#.    # [len(链) == 1+len(stk)]
#.    # [[j:<-[1..<len(链)]] -> [链[j] == stk[j-1].u]]
#.    ########
#.    assert len(链) == 1+len(stk)
#.    return (stk, st, hp)
#.
#.class 乸就地现场:
#.    __slots__ = '''
#.    链
#.    stk
#.    st
#.    b_goback
#.    '''.split()#'''
#.
#.冻结冫加工链扌
#.解冻冫加工链扌
#.
#.def 蛮力搜索冫加工链纟虚匏融介链纟最短加链扌(sf, 匴前缀无效判定器纟加工链纟虚匏融介链纟最短加链, 靶值, 鬽丮前缀纟加工链辻欤回溯中厈, /, *, 彧下界纟最小显链长, 彧上界纟最小显链长, 欤显示冗杂调试信息=False, **额外参数):
#.    '-> 鬽 加工链{虚匏融介链{最短加链{靶值}}}'
#.    if 1:
#.        (鬽加工链, 匴前缀无效判定器纟加工链纟虚匏融介链纟最短加链, 靶值, 前缀纟加工链, 欤回溯中, 下界纟最小显链长, 上界纟最小显链长) = 规范输入扌(sf, 匴前缀无效判定器纟加工链纟虚匏融介链纟最短加链, 靶值, 鬽丮前缀纟加工链辻欤回溯中厈, 彧下界纟最小显链长, 彧上界纟最小显链长, 欤显示冗杂调试信息)
#.        if not None is 鬽加工链:
#.            return 鬽加工链
#.
#.        匴 = 匴前缀无效判定器纟加工链纟虚匏融介链纟最短加链
#.        状态纟批次 = 匴.乊搜索起始纟批量处理扌(靶值, 欤显示冗杂调试信息=verbose, **额外参数)
#.        备份纟前缀纟加工链 = 冻结冫加工链扌(前缀纟加工链)
#.    try:
#.        前缀纟加工链 = 备份纟前缀纟加工链
#.        for 假想最小显链长 in range(下界纟最小显链长, 1+上界纟最小显链长):
#.            前缀纟加工链
#.            链 = 解冻冫加工链扌(必要前缀纟加工链)
#.            777;链屮状态 = 匴.乊搜索起始乊假想显链长扌(状态纟批次, 假想最小显链长)
#.            if 链屮状态.is_left:
#.                加工链 = 链屮状态.left
#.                鬽加工链 = 加工链
#.                break
#.            st = 链屮状态.right
#.            (stk, st, hp) = 直达前缀扌(sf, 匴, 靶值, 前缀纟加工链, 链, st)
#.            就地现场 = 构造冫就地现场扌(链, stk, st, hp)
#.            if 搜索扌(sf, 匴, 靶值, 假想最小显链长, 就地现场, verbose=verbose):
#.                # found
#.                加工链 = 冻结冫加工链扌(链)
#.                鬽加工链 = 加工链
#.                break
#.            assert 链 == [*必要前缀纟加工链]
#.            assert not stk
#.            ########下一轮:
#.            前缀纟加工链 = 必要前缀纟加工链
#.        else:
#.            鬽加工链 = None
#.        #ens-for 假想最小显链长 in range(下界纟最小显链长, 1+上界纟最小显链长):
#.        ######################
#.        #收尾阶段:
#.        ######################
#.        if not 鬽加工链 is None:
#.            加工链 = 鬽加工链
#.            检查冫严序加工链乊靶值扌(靶值, 加工链)
#.            assert 下界纟最小显链长 <= 显链长巛加工链扌(加工链) <= 上界纟最小显链长
#.        return 鬽加工链
#.    except BaseException as exc:
#.        raise 乊中断扌(exc, dict(locals()))
#.
#.    raise 000
#.
#.
#.
#.
#.直达前缀扌(sf, 匴, 靶值, 前缀纟加工链, 链, st)
#.    return (stk, st, hp)
#.构造冫就地现场扌(链, stk, st, hp)
#.    return 乸就地现场
#.搜索扌(sf, 匴, 靶值, 假想最小显链长, 就地现场, verbose)
#.    return b_found
#.检查冫严序加工链乊靶值扌(靶值, 加工链)
#.乊中断扌(exc, locals)
#.    raise
#.
#.
#.
#.
#.
#.
#.
#.
#.
#.def 蛮力搜索冫加工链纟虚匏融介链纟最短加链扌(sf, 匴前缀无效判定器纟加工链纟虚匏融介链纟最短加链, 靶值, 鬽前缀纟加工链, /, *, 彧下界纟最小显链长, 彧上界纟最小显链长, 欤显示冗杂调试信息=False, **额外参数):
#.    ...
#.        ######################
#.        #主工作循环:
#.        ######################
#.
#.        ######################
#.        # [阳爻数{靶值} >= 4]
#.        # [前缀纟加工链 <- 乸严序加工链]
#.        # [靶值巛加工链扌(前缀纟加工链) < 靶值]
#.        # [0 <= 显链长巛加工链扌(前缀纟加工链) <= 下界纟最小显链长 <= 上界纟最小显链长]
#.        ######################
#.        匴 = 匴前缀无效判定器纟加工链纟虚匏融介链纟最短加链
#.        备份纟前缀纟加工链 = 前缀纟加工链 = 冻结冫加工链扌(前缀纟加工链)
#.        # [0 <= 显链长巛加工链扌(前缀纟加工链) <= 下界纟最小显链长 <= 上界纟最小显链长]
#.        # [靶值巛加工链扌(前缀纟加工链) < 靶值]
#.        状态纟批次 = 匴.乊搜索起始纟批量处理扌(靶值, 欤显示冗杂调试信息=verbose, **额外参数)
#.        case4starting = 0o00_00
#.        sf.罓乊测试扌(靶值=靶值, case4starting=case4starting, 假想最小显链长=-1)
#.    try:
#.        for 假想最小显链长 in range(下界纟最小显链长, 1+上界纟最小显链长):
#.            sf.罓乊测试扌(靶值=靶值, case4starting=case4starting, 假想最小显链长=假想最小显链长)
#.            assert case4starting in (0, 3)
#.            # [下界纟最小显链长 <= 假想最小显链长 <= 上界纟最小显链长]
#.            # [0 <= 显链长巛加工链扌(前缀纟加工链) <= 下界纟最小显链长]
#.
#.            if not 假想最小显链长 == 下界纟最小显链长:
#.                # [0 <= 显链长巛加工链扌(前缀纟加工链) <= 下界纟最小显链长]
#.                前缀纟加工链 = 必要前缀纟加工链#((0, (None, 1)),)
#.                # [0 <= 显链长巛加工链扌(前缀纟加工链) <= 下界纟最小显链长]
#.            # [0 <= 显链长巛加工链扌(前缀纟加工链) <= 下界纟最小显链长]
#.            # !! [下界纟最小显链长 <= 假想最小显链长 <= 上界纟最小显链长]
#.            # [0 <= 显链长巛加工链扌(前缀纟加工链) <= 假想最小显链长]
#.            case4starting = 0o00_01
#.            sf.罓乊测试扌(靶值=靶值, case4starting=case4starting, 假想最小显链长=假想最小显链长)
#.            # [阳爻数{靶值} >= 4]
#.            # [靶值 >= 15]
#.            链 = [*必要前缀纟加工链]
#.            777;either_us_st = 匴.乊搜索起始乊假想显链长扌(状态纟批次, 假想最小显链长)
#.            if either_us_st.is_left:
#.                加工链 = either_us_st.left
#.                鬽加工链 = 加工链
#.                break
#.            st = either_us_st.right
#.            ...TODO:修改:
#.            # [st <~~ 链[-1]]
#.            # [len(链) == 1 <= len(前缀纟加工链) <= 1+假想最小显链长]
#.            # [链 == 前缀纟加工链[:len(链)]]
#.            欤强制降序乊可交换步 = 匴.欤强制降序乊可交换步扌(状态纟批次)
#.            kwds4hp = dict(假想最小显链长=假想最小显链长, 欤强制降序乊可交换步=欤强制降序乊可交换步, verbose=verbose)
#.            stk = []
#.                # :: [heap{-u:[(j,i)]}]
#.                #   heap_item.u
#.            # [len(链) == 1+len(stk)]
#.            # [len(链) == 1 <= len(前缀纟加工链)]
#.            # [链 == 前缀纟加工链[:len(链)]]
#.            # [st <~~ 链[-1]]
#.            for u in 前缀纟加工链[1:]:
#.                # [len(链) == 1+len(stk)]
#.                # [len(链) < len(前缀纟加工链)]
#.                # [链 == 前缀纟加工链[:len(链)]]
#.                # [st <~~ 链[-1]]
#.                hp = _4mk_heap4next(sf, 匴, 靶值, 链, st, 上界=u, **kwds4hp)
#.                if not (hp and hp.head.u == u):
#.                    # [hp !<- stk]
#.                    # [not hp]or[hp[0] !<- 链]
#.                    break # (链, stk, st, hp{next})
#.                # [hp[0].u == u]
#.                stk.append(hp)
#.                链.append(u)
#.                # [len(链) <= len(前缀纟加工链)]
#.                # [链 == 前缀纟加工链[:len(链)]]
#.                777;st = 匴.乊加链前缀增位扌(st, u, hp.head.ji_ls)
#.                # [st <~~ 链[-1]]
#.                # [stk[-1][0].u == 链[-1]]
#.                # [len(链) == 1+len(stk)]
#.                # [stk[j-1][0].u == 链[j]]
#.            else:
#.                hp = _4mk_heap4next(sf, 匴, 靶值, 链, st, 上界=None, **kwds4hp)
#.                # [hp !<- stk]
#.                # [hp[0] !<- 链]
#.            ########
#.            # (链, stk, st, hp{next})
#.            ########
#.            # [st <~~ 链[-1]]
#.            ########
#.            # [hp !<- stk]
#.            # [not hp]or[hp[0] !<- 链]
#.            ########
#.            # [1 <= len(链) <= len(前缀纟加工链) <= 1+假想最小显链长]
#.            # [链 == 前缀纟加工链[:len(链)]]
#.            # !! [前缀纟加工链[-1] < 靶值]
#.            # [链[-1] < 靶值]
#.            # [1 <= len(链) <= 1+假想最小显链长]
#.            # [len(链) == 1+len(stk)]
#.            # [[j:<-[1..<len(链)]] -> [链[j] == stk[j-1].u]]
#.            ########
#.            assert len(链) == 1+len(stk)
#.            # _深入链乊回溯前 = [*链]
#.            #_深入链乊回溯前 = [len(链), rglnkls5iterable(链)]
#.            _深入链乊回溯前 = []
#.                #用于 异常时输出环境
#.            case4starting = 0o00_02
#.            sf.罓乊测试扌(靶值=靶值, case4starting=case4starting, 假想最小显链长=假想最小显链长)
#.            if verbose:print_err(f'into: 靶值={靶值}, 假想最小显链长={假想最小显链长}, 链={链}')
#.            if _4search(sf, 匴, 靶值, 假想最小显链长, 链, stk, st, hp, _深入链乊回溯前, verbose=verbose, kwds4hp=kwds4hp):
#.                # found
#.                加工链 = 冻结冫加工链扌(链)
#.                鬽加工链 = 加工链
#.                break
#.            assert 链 == [1]
#.            assert not stk
#.            case4starting = 0o00_03
#.        else:
#.            鬽加工链 = None
#.        ######################
#.        #收尾阶段:
#.        ######################
#.        case4starting = 0o00_04
#.        sf.罓乊测试扌(靶值=靶值, case4starting=case4starting, 假想最小显链长=-1)
#.        if not 鬽加工链 is None:
#.            检查冫严序加工链乊靶值扌(靶值, 加工链)
#.            assert 下界纟最小显链长 <= 显链长巛加工链扌(加工链) <= 上界纟最小显链长
#.        return 鬽加工链
#.    except BaseException as e:
#.        ######################
#.        #输出中断现场:
#.        ######################
#.        if 0:0
#.        参数牜本次运行= dict(靶值=靶值, 前缀纟加工链=备份纟前缀纟加工链, 彧下界纟最小显链长=下界纟最小显链长, 彧上界纟最小显链长=上界纟最小显链长, **额外参数)
#.        _4print_err(参数牜本次运行=参数牜本次运行)
#.        if case4starting == 0o00_00:
#.            raise _4raise(e, 参数牜本次运行=参数牜本次运行)
#.        if case4starting == 0o00_04:
#.            _4print_err(鬽加工链牜待检查=鬽加工链)
#.            raise _4raise(e, 参数牜本次运行=参数牜本次运行, 鬽加工链牜待检查=鬽加工链)
#.        if case4starting == 0o00_03:
#.            if not 假想最小显链长 == 下界纟最小显链长:
#.                前缀纟加工链 = (1,)
#.            case4starting = 0o00_01
#.        ######
#.        assert case4starting in (1, 2)
#.        ######
#.        if not case4starting == 0o00_02:
#.            #尚无:链、_深入链乊回溯前
#.            链 = None
#.            深入链乊回溯前 = None
#.        else:
#.            链
#.            深入链乊回溯前 = rglnkls2list(_深入链乊回溯前[1])
#.        ######
#.        if case4starting == 0o00_01:
#.            #尚无:链、_深入链乊回溯前
#.            新前缀 = 前缀纟加工链
#.        elif case4starting == 0o00_02:
#.            #已有:链、_深入链乊回溯前
#.            if 深入链乊回溯前[:len(链)] == 链:
#.                # [b_goback]
#.                # [b_goback ing...]
#.                新前缀 = 深入链乊回溯前
#.            else:
#.                # [not b_goback]
#.                新前缀 = 链
#.            新前缀
#.        else:
#.            raise 000
#.        新前缀
#.        中断现场 = dict(鬽深入链乊回溯前=深入链乊回溯前, 鬽链=链, 假想最小显链长=假想最小显链长, 新前缀牜假想显链长=新前缀,     参数牜本次运行=参数牜本次运行)
#.        _4print_err(中断现场=中断现场)
#.        部分具名参数 = 匴.保存冫状态纟批次讠部分具名参数扌(状态纟批次)
#.        参数牜下一次运行 = dict(参数牜本次运行)
#.        777;参数牜下一次运行.update(前缀纟加工链=新前缀, 彧下界纟最小显链长=假想最小显链长, **部分具名参数)
#.        _4print_err(参数牜下一次运行=参数牜下一次运行)
#.        raise _4raise(e, 参数牜本次运行=参数牜本次运行, 中断现场=中断现场)
#.    if 1:
#.        raise 000
#.#end-def 蛮力搜索冫加工链纟虚匏融介链纟最短加链扌(sf, 匴前缀无效判定器纟加工链纟虚匏融介链纟最短加链, 靶值, 鬽前缀纟加工链, /, *, 下界纟最小显链长, 上界纟最小显链长, **额外参数):
#.def _4print_err(**kwds):
#.    print_err(kwds)
#.def _4raise(exc, /, **kwds):
#.    #bug:class ERR(type(exc), BaseException):
#.    #   class ERR(BaseException, BaseException):
#.    #       ^TypeError: duplicate base class BaseException
#.    bases = [type(exc), BaseException]
#.    if bases[0] is bases[1]:
#.        bases.pop()
#.    class ERR(*bases):
#.        def __init__(sf, /, *args):
#.            BaseException.__init__(sf, *args)
#.
#.    raise ERR('蛮力搜索冫加工链纟虚匏融介链纟最短加链扌', (exc, kwds)) from exc
#.___end_mark_of_excluded_global_names__99___ = ...
#.
#.class 魖匴蛮力搜索器纟最短加链(ABC):
#.    '匴蛮力搜索器{最短加链}'
#.    __slots__ = ()
#.    #.@property
#.    #.@abstractmethod
#.    #.def 匴前缀无效判定器纟加工链纟虚匏融介链纟最短加链(sf, /):
#.    #.    '-> 魖匴前缀无效判定器纟加工链纟虚匏融介链纟最短加链'
#.    #
#.    def 罓乊测试扌(sf, /, *, 靶值, case4starting, 假想最小显链长):
#.        return
#.
#.    ######################
#.    蛮力搜索冫加工链纟虚匏融介链纟最短加链扌 = 蛮力搜索冫加工链纟虚匏融介链纟最短加链扌
#.    ######################
#.def _4pop(_链, /):
#.    (_链[1], u) = rglnkls_ipop_right(_链[1])
#.    _链[0] -= 1
#.    #if 0b0001:print_err('_4pop:', u, '#', _链[0])
#.def _4push(_链, u, /):
#.    #if 0b0001:print_err('_4push:', u, '#', _链[0])
#.    (_链[1], _None) = rglnkls_ipush_right(_链[1], u)
#.    _链[0] += 1
#.def _4search(sf, 匴, 靶值, 假想最小显链长, 链, stk, st, hp, _深入链乊回溯前, /, *, verbose, kwds4hp):
#.    '-> b_found'
#.    ########
#.    # (链, stk, st, hp{next})
#.    ########
#.    # [st <~~ 链[-1]]
#.    ########
#.    # [hp !<- stk]
#.    # [not hp]or[hp[0] !<- 链]
#.    ########
#.    # [链[-1] < 靶值]
#.    # [1 <= len(链) <= 1+假想最小显链长]
#.    # [len(链) == 1+len(stk)]
#.    # [[j:<-[1..<len(链)]] -> [链[j] == stk[j-1].u]]
#.    ########
#.    链长上界 = 1+假想最小显链长
#.    assert 1 <= len(链) <= 链长上界
#.    assert len(链) == 1+len(stk)
#.    ########
#.    b_goback = False
#.    stk.append(hp); del hp
#.    # [len(链) == len(stk) >= 1]
#.    # [[j:<-[1..<len(链)]] -> [链[j] == stk[j-1].u]]
#.    # [not stk[-1]]or[not stk[-1] !<- 链]
#.    # [st <~~ 链[-1]]
#.    # [not b_goback]
#.    # [1 <= len(链) <= 链长上界]
#.    # [链[-1] < 靶值]
#.    ########
#.    _链 = [len(链), rglnkls5iterable(链)]
#.    _深入链乊回溯前[:] = _链
#.    while 1:
#.        if verbose:print_err(f'loop: b_goback={b_goback}, 链={链}')
#.        assert stk
#.        # [1 <= len(链) <= 链长上界]
#.        # [链[-1] < 靶值]
#.        # [len(链) == len(stk) >= 1]
#.        # [[j:<-[1..<len(链)]] -> [链[j] == stk[j-1].u]]
#.        # [not stk[-1]]or[not stk[-1] !<- 链]
#.        # [st <~~ 链[-1]]
#.        assert 链[-1] < 靶值
#.        hp = stk[-1]
#.        if b_goback:
#.            #回溯
#.            # [not stk[-1] !<- 链]
#.            assert hp
#.            _heappop(hp)
#.            # [not stk[-1]]or[not stk[-1] !<- 链]
#.            b_goback = False
#.            # [len(链) == len(stk) >= 1]
#.            # [[j:<-[1..<len(链)]] -> [链[j] == stk[j-1].u]]
#.            # [st <~~ 链[-1]]
#.            continue
#.        #深入
#.        assert not b_goback
#.        # [链[-1] < 靶值]
#.        # [1 <= len(链) <= 链长上界]
#.        if len(链) == 链长上界 or hp.is_empty():
#.            if _深入链乊回溯前[0] > len(链):
#.                if verbose:print_err('_深入链乊回溯前: 回溯中...', 链, (靶值, 假想最小显链长))
#.                sf.罓乊测试扌(靶值=靶值, case4starting=209, 假想最小显链长=假想最小显链长)
#.                    #0o00_0209:『SyntaxError: invalid digit '9' in octal literal』
#.            else:
#.                if verbose:print_err('_深入链乊回溯前: 回溯起始', 链)
#.                _深入链乊回溯前[:] = _链
#.            stk.pop()
#.            # [len(链) -1 == len(stk) >= 0]
#.            if not stk:
#.                return (b_found:=False)
#.                break
#.            # [len(链) -1 == len(stk) >= 1]
#.            st = 匴.乊加链前缀减位扌(st)
#.            777;链.pop();_4pop(_链)
#.            # [st <~~ 链[-1]]
#.            # [len(链) == len(stk) >= 1]
#.            # [not stk[-1] !<- 链]
#.            # [[j:<-[1..<len(链)]] -> [链[j] == stk[j-1].u]]
#.            b_goback = True
#.            continue
#.        # [1 <= len(链) < 链长上界]
#.        # [len(hp) > 0]
#.        # [not stk[-1] !<- 链]
#.        u = hp.head.u
#.        if not u > 链[-1]:raise 000-_4mk_heap4next-_4next_bounds
#.            # !! [下界纟后一位 = max(下界纟后一位, 1+链[-1])]
#.            # => [hp[0].u >= 1+链[-1]]
#.            # => [链:严序]
#.        if not u <= 靶值:raise 000-_4mk_heap4next-_4next_bounds
#.            # !! [上界纟后一位 := min(上界纟后一位, 靶值)]
#.            # => [hp[0].u <= 靶值]
#.        # [u <= 靶值]
#.        # [1 <= len(链) < 链长上界]
#.        链.append(u);_4push(_链, u)
#.        # [1 <= len(链) <= 链长上界]
#.        777;st = 匴.乊加链前缀增位扌(st, u, hp.head.ji_ls)
#.        # [st <~~ 链[-1]]
#.        if u == 靶值:
#.            return (b_found:=True)
#.        # [u < 靶值]
#.        # [链[-1] < 靶值]
#.        hp = _4mk_heap4next(sf, 匴, 靶值, 链, st, 上界=None, **kwds4hp)
#.        stk.append(hp)
#.        # [not stk[-1]]or[not stk[-1] !<- 链]
#.        # [len(链) == len(stk) >= 1]
#.        # [[j:<-[1..<len(链)]] -> [链[j] == stk[j-1].u]]
#.        # [链[-1] < 靶值]
#.        # [1 <= len(链) <= 链长上界]
#.        _深入链乊回溯前[:] = _链
#.        sf.罓乊测试扌(靶值=靶值, case4starting=206, 假想最小显链长=假想最小显链长)
#.    raise 000
#.
#._U_JIs_Pair = namedtuple('_U_JIs_Pair', 'u  ji_ls')
#.def _4mk_heap4next(sf, 匴, 靶值, 假想最小显链长, 链, st, /, *, 上界:None, verbose, **_kwds4hp):
#.    #kwds4hp
#.    args_ = [sf, 匴, 靶值, 链, st]
#.    (下界纟后一位, 上界纟后一位) = _4next_bounds(*args_, 1)
#.    上界 = min(上界纟后一位, ifNone(上界, 上界纟后一位))
#.    下界 = 下界纟后一位
#.    if not 下界 <= 上界:
#.        if verbose: print_err(f'mk-empty-hp: hp=[], 下界={下界}, 上界={上界}')
#.        return echo_or_mk_IPeekableIterator(null_iter) #_4mk_empty_heap_()
#.    def u_objs2u_ji_ls_(u_objs, /):
#.        u, [*objs] = u_objs
#.        #objs.sort(reverse=True)
#.        assert objs[0][0] == u
#.        assert objs[-1][0] == u
#.        assert objs[0] >= objs[-1]
#.        ji_ls = tuple((j, i) for _u, (j, i) in objs)
#.        assert ji_ls[0] >= ji_ls[-1]
#.            #ji_ls降序
#.        return _U_JIs_Pair(u, ji_ls)
#.
#.    it = echo_or_mk_IPeekableIterator(map(u_objs2u_ji_ls_, groupby(merge_ex(_4iter_next(链, 下界, args_, **_kwds4hp), reverse=True), key=fst)))
#.        # :: PeekableIterator{(u, ji_ls)}
#.    while (not it.is_empty()) and it.head.u > 上界:
#.        #it.read1()
#.        next(it)
#.    hp = it
#.    if verbose:
#.        hp = list(hp)
#.        print_err(f'mk: hp={hp}, 下界={下界}, 上界={上界}')
#.        hp = echo_or_mk_IPeekableIterator(iter(hp))
#.    return hp
#.def _heappop(hp, /):
#.    #it.read1()
#.    next(hp)
#.def _4iter_next(链, 下界, args_, /, *, 假想最小显链长, 欤强制降序乊可交换步):
#.    #_kwds4hp
#.
#.    #########
#.    # [:补丁牜下界纟非星步]:here
#.    #########
#.    剩余长度 = 假想最小显链长 -len(链)
#.    if 剩余长度 >= 3:
#.        (下界纟后三位, 上界纟后三位) = _4next_bounds(*args_, 3)
#.            #@后一位非星步
#.        #[[[前缀纟加工链[k] == 前缀纟加工链[j]+前缀纟加工链[i]]] -> [0 <= i <= j < k < 假想最小显链长] -> [前缀纟加工链[k]*2+前缀纟加工链[k-1] >= 下界乊[k+2]]]
#.        #   #前缀纟加工链[k-1] 义务出度为1
#.        #   #前缀纟加工链[k] 后续极大化=>等效义务出度为2 #因为 加法降序
#.        #     # 由于 加法降序 所以 [[前缀纟加工链[k+1] == 前缀纟加工链[k]+前缀纟加工链[k-1]] -> [前缀纟加工链[k]义务出度>=2]]
#.        #     #     => 还不如 [前缀纟加工链[k+1]==2*前缀纟加工链[k]][前缀纟加工链[k+2]==2*前缀纟加工链[k]+前缀纟加工链[k-1]]
#.        #
#.        欤可行冫非星步 = 下界纟后三位 <= 上界纟后三位
#.        下界纟后一位牜非星步 = (下界纟后三位 -链[-1]   +1) //2
#.            #ceil(.../2)
#.            # !! [uk*2+链[-1] >= 下界纟后三位]
#.            #   where uk 是 值纟后一位
#.    else:
#.        欤可行冫非星步 = False
#.    欤可行冫非星步
#.    #########
#.    def _is_ok(欤星步, uk, /):
#.        if not uk >= 下界:
#.            return
#.        #if 欤强制降序乊可交换步 and not 欤星步 and not uk*2+链[-1] >= 下界纟后三位:
#.        if 欤强制降序乊可交换步 and not 欤星步 and not uk >= 下界纟后一位牜非星步:
#.            #补丁牜下界纟非星步
#.            return
#.    #########
#.    def _iter(欤星步, j, /):
#.        if j < 0:
#.            return
#.        if 欤强制降序乊可交换步 and not 欤星步 and not 欤可行冫非星步:
#.            #补丁牜下界纟非星步
#.            return
#.        uj = 链[j]
#.        uk = uj*2
#.        if not _is_ok(欤星步, uk):
#.            return
#.        obj = (uk, (j, j))
#.        yield (obj, [_iter(False, j-1)])
#.        for i in reversed(range(j)):
#.            ui = 链[i]
#.            uk = uj +ui
#.            if not _is_ok(欤星步, uk):
#.                return
#.            obj = (uk, (j, i))
#.            yield (obj, None)
#.    def main():
#.        k = len(链)
#.        return _iter(True, k-1)
#.    return main()
#.
#.
#.def _4next_bounds(sf, 匴, 靶值, 链, st, 后几位, /):
#.    ok = False
#.    while 1:
#.        if 匴.欤加工链前缀无效扌(st):
#.            break
#.        鬽 = 匴.求取冫鬽下上界纟后几位扌(st, 后几位)
#.        if None is 鬽:
#.            break
#.        (下界纟后一位, 上界纟后一位) = 鬽
#.        下界纟后一位 = max(下界纟后一位, 后几位+链[-1])
#.            # => [hp[0].u >= 1+链[-1]]
#.            # => [链:严序]
#.        上界纟后一位 = min(上界纟后一位, 靶值)
#.            # => [hp[0].u <= 靶值]
#.            # => [链[-1] <= 靶值]
#.        if not 下界纟后一位 <= 上界纟后一位:
#.            break
#.        ok = True
#.        break
#.    if not ok:
#.        return (靶值, 0)
#.        return (靶值+1, 0)
#.    return (下界纟后一位, 上界纟后一位)
#.
#.
#.
#.
#.
#.class 乸匴蛮力搜索器纟最短加链(魖匴蛮力搜索器纟最短加链):
#.    ___no_slots_ok___ = True
#.    def __init__(sf, /, *, _毝靶值=-1, _imay_case4starting=-1, _毝假想显链长=-1):
#.        sf._毝靶值 = _毝靶值
#.        sf._imay_case4starting = _imay_case4starting
#.        sf._毝假想显链长 = _毝假想显链长
#.    @override
#.    def 罓乊测试扌(sf, /, *, 靶值, case4starting, 假想最小显链长):
#.        if sf._毝靶值 == 靶值 and sf._imay_case4starting == case4starting and sf._毝假想显链长 == 假想最小显链长:
#.            raise BaseException('debugging', 靶值, case4starting, 假想最小显链长)
#.匴蛮力搜索器纟最短加链 = 乸匴蛮力搜索器纟最短加链()
#.























__all__
from seed.math.power.addition_chain.shortest.search7contracted_chain import *
