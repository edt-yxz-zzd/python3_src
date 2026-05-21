#__all__:goto
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/short/target_uint2short_addition_chain.py

seed.math.power.addition_chain.short.target_uint2short_addition_chain
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.short.target_uint2short_addition_chain -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.short.target_uint2short_addition_chain:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.power.addition_chain.short.target_uint2short_addition_chain   @f
]]]'''#'''
__all__ = r'''
靶值讠欤未必最短辻加链牜尽量短扌
    靶值讠加链牜尽量短扌
        target_uint2short_addition_chain_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from functools import lru_cache #cache #cached_property
    from seed.tiny_.check import check_type_is, check_int_ge

    from seed.math.power.addition_chain.data.get_target_uint2may_optimal_addition_chain7arbitrary_recur_shortest_stem_ import 靶值讠婪溟链牜递归最短牜任意扌
    from seed.math.power.addition_chain.shortest.upper_bound4len_optimal_addition_chain import 实证估计冫上界纟最小显链长巛靶值牜次优牜精研综合扌
    #.def 实证估计冫上界纟最小显链长巛靶值牜次优牜精研综合扌(靶值, /, *, 欤排除窗式拆分牜定窗式=False, 欤排除窗式拆分牜滑窗式=False):
    #.    '靶值 -> (上界纟最小显链长{靶值}, 加链{靶值}{显链长==上界纟最小显链长{靶值}})'
    from seed.math.power.addition_chain.shortest.may_optimal_addition_chain5target_uint7generally_solved_small_step_cases import 构造冫鬽最短加链巛靶值纟已知阳爻模板扌
    from seed.math.power.addition_chain.data.get_target_uint2may_len_optimal_addition_chain_ import 靶值讠最小显链长扌
    from seed.math.power.addition_chain.shortest.lower_bound4len_optimal_addition_chain import 估计冫下界纟最小显链长巛靶值牜精研综合扌
    #def 估计冫下界纟最小显链长巛靶值牜精研综合扌(靶值, /, *, 鬽上界纟最小显链长, 鬽上界纟总小步数=None, 欤排除数据验证部分=False):
    #    '靶值 -> 下界纟最小显链长{靶值}'
    from seed.math.power.addition_chain.common.properties import 显链长纟

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def target_uint2short_addition_chain_(u, /):
    return 靶值讠加链牜尽量短扌(u)

def 靶值讠加链牜尽量短扌(靶值, /):
    '靶值 -> 短加链{靶值}{尽量短}'
    (欤未必最短, 短加链) = 靶值讠欤未必最短辻加链牜尽量短扌(靶值)
    return 短加链
#lru_cache(maxsize=128, typed=False)
@lru_cache()
def 靶值讠欤未必最短辻加链牜尽量短扌(靶值, /):
    '靶值 -> (欤未必最短/bool, 短加链{靶值}{尽量短})'
    check_int_ge(1, 靶值)
    # [靶值 > 0]
    (欤未必最短, 短加链) = _靶值讠欤未必最短辻加链牜尽量短扌(靶值)
    check_type_is(bool, 欤未必最短)
    check_type_is(tuple, 短加链)
    return (欤未必最短, 短加链)

def _靶值讠欤未必最短辻加链牜尽量短扌(靶值, /):
    # [靶值 > 0]
    ###########################
    # 查表
    try:
        最短加链 = 靶值讠婪溟链牜递归最短牜任意扌(靶值)
    except LookupError:
        #except IndexError:
        pass
    else:
        欤最短 = True
        欤未必最短 = not 欤最短
        return (欤未必最短, 最短加链)

    ###########################
    # 匹配模板
    if not None is (最短加链:=构造冫鬽最短加链巛靶值纟已知阳爻模板扌(靶值)):
        欤最短 = True
        欤未必最短 = not 欤最短
        return (欤未必最短, 最短加链)

    ###########################
    # 随机优化
    (_, 短加链) = 实证估计冫上界纟最小显链长巛靶值牜次优牜精研综合扌(靶值)
    显链长 = 显链长纟(短加链)
    try:
        #查表
        最小显链长 = 靶值讠最小显链长扌(靶值)
    except LookupError:
        #except IndexError:
        #下界
        下界纟最小显链长 = 估计冫下界纟最小显链长巛靶值牜精研综合扌(靶值, 鬽上界纟最小显链长=显链长)
        assert (显链长 >= 下界纟最小显链长)
        欤未必最短 = (显链长 > 下界纟最小显链长)
    else:
        assert (显链长 >= 最小显链长)
        欤最短 = (显链长 == 最小显链长)
        欤未必最短 = not 欤最短
    欤未必最短
    return (欤未必最短, 短加链)



__all__
from seed.math.power.addition_chain.short.target_uint2short_addition_chain import 靶值讠欤未必最短辻加链牜尽量短扌, 靶值讠加链牜尽量短扌
from seed.math.power.addition_chain.short.target_uint2short_addition_chain import target_uint2short_addition_chain_
from seed.math.power.addition_chain.short.target_uint2short_addition_chain import *
