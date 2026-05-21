#__all__:goto
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/shortest/lower_bound4len_optimal_addition_chain.py

seed.math.power.addition_chain.shortest.lower_bound4len_optimal_addition_chain
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.shortest.lower_bound4len_optimal_addition_chain -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.shortest.lower_bound4len_optimal_addition_chain:__doc__ -ht # -ff -df
#######

[[
view ../../python3_src/seed/math/power/addition_chain/common/README-formula.txt
===
  下界牜猜想牜一九六九:[ℓ(n) >= λ(n) + log2(v(n))]
    即:猜想:[ℓ(n) >= λ(n) + ceil_log2(v(n))]
    猜想牜显链长下界:[显链长>=首爻位纟靶值+ceil_log2(阳爻数纟靶值)]
        成立于:[靶值<-[1..=2**64]]
        成立于:[阳爻数{靶值}<-[1..=16]]
        成立于:[总小步数{靶值}<-[1..=5]]
        即:[[n:<-[1..]] -> [[n<-[1..=2**64]]or[ν(n)<-[1..=16]]or[s(n)<-[1..=5]]] -> [ℓ(n) >= λ(n) + ceil_log2(v(n))]]

  ===
  下界牜一九七四:[ℓ(n) >= log2(n)+log2(v(n))-2.123164629...]
    => [ℓ(n) >= ceil(log2(n)+log2(v(n))-2.123164629...) >= ceil(log2(n*v(n))-2.13) == ceil_log2(n*v(n)/2**2.13) >= ceil_log2(n*v(n)*_fr)]
    where:
      _fr = Fraction(*nextafter(1/2**2.13, -1.0).as_integer_ratio())
      assert _fr == Fraction(514441372341571, 2251799813685248)
      assert (1/_fr)**100 > 2**213
    不采用更精细版<<==数据太大，无法校验

===
]]


'#'; __doc__ = r'#'

>>> from math import nextafter
>>> _fr == Fraction(*nextafter(__fl:=1/2**2.13, -1.0).as_integer_ratio())
True
>>> _fr == Fraction(514441372341571, 2251799813685248)
True
>>> (1/_fr)**100 > 2**213
True

>>> __fr = Fraction(*(__fl).as_integer_ratio())
>>> (1/__fr)**100 > 2**213
False



py_adhoc_call   seed.math.power.addition_chain.shortest.lower_bound4len_optimal_addition_chain   @f
]]]'''#'''
__all__ = r'''
估计冫下界纟最小显链长巛靶值牜精研综合扌

估计冫下界纟最小显链长巛靶值牜平凡扌
估计冫下界纟最小显链长巛靶值牜一九七四扌
估计冫下界纟最小显链长巛靶值牜数据验证部纟一九六九扌
    欤已知成立冫下界纟最小显链长乊靶值牜猜想牜一九六九扌
    估计冫下界纟最小显链长巛靶值牜猜想牜一九六九扌

'''.split()#'''
#更名:估计冫下界纟显链长纟最短加链牜猜想牜一九六九牜已经数据实测验证部分扌 --> 估计冫下界纟显链长纟最短加链牜数据验证部纟一九六九扌 --> 估计冫下界纟最小显链长巛靶值牜数据验证部纟一九六九扌
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.tiny_.check import check_type_is, check_int_ge
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from fractions import Fraction
    from seed.math.floor_ceil_tools.fc_log import floor_log2, ceil_log2
    from seed.math.power.addition_chain.common.properties import 显链长纟, 阳爻数纟, 首爻位纟

    #from seed.debug.print_err import print_err
    #from math import log2, nextafter
    #from math import ceil
    #from bisect import bisect_right

#.#################################
___end_mark_of_excluded_global_names__0___ = ...


__all__

_fr = Fraction(514441372341571, 2251799813685248)



#估计冫下上界纟显链长纟最短加链扌(靶值, /):
#class 匴乸估值器纟下界纟显链长纟最短加链
def 估计冫下界纟最小显链长巛靶值牜平凡扌(靶值, /):
    check_int_ge(1, 靶值)
    # 阳爻数==1 <=> 必 +0 => 唯一
    # 阳爻数==2 <=> 必 +1
    # 阳爻数==3 => 必 +2
    # 阳爻数>=4 => 必 >= +2
    return 首爻位纟(靶值) +min(3, 阳爻数纟(靶值)) -1
def 估计冫下界纟最小显链长巛靶值牜猜想牜一九六九扌(靶值, /):
    check_int_ge(1, 靶值)
    #下界牜猜想牜一九六九:[ℓ(n) >= λ(n) + log2(v(n))]
    return 首爻位纟(靶值) +ceil_log2(阳爻数纟(靶值))
def 估计冫下界纟最小显链长巛靶值牜数据验证部纟一九六九扌(靶值, /, *, 鬽上界纟最小显链长, 鬽上界纟总小步数=None):
    if 欤已知成立冫下界纟最小显链长乊靶值牜猜想牜一九六九扌(靶值, 鬽上界纟最小显链长=鬽上界纟最小显链长, 鬽上界纟总小步数=鬽上界纟总小步数):
        return 估计冫下界纟最小显链长巛靶值牜猜想牜一九六九扌(靶值)
    return 估计冫下界纟最小显链长巛靶值牜平凡扌(靶值)
def 欤已知成立冫下界纟最小显链长乊靶值牜猜想牜一九六九扌(靶值, /, *, 鬽上界纟最小显链长, 鬽上界纟总小步数=None):
    check_int_ge(1, 靶值)
    #成立于:[靶值<-[1..=2**64]]
    #成立于:[阳爻数{靶值}<-[1..=16]]
    #成立于:[总小步数{靶值}<-[1..=5]]
    #即:[[n:<-[1..]] -> [[n<-[1..=2**64]]or[ν(n)<-[1..=16]]or[s(n)<-[1..=5]]] -> [ℓ(n) >= λ(n) + ceil_log2(v(n))]]
    if 靶值 <= 0x1_0000_0000_0000_0000:
        return True
    if 阳爻数纟(靶值) <= 16:
        return True

    if not 鬽上界纟总小步数 is None:
        上界纟总小步数 = 鬽上界纟总小步数
        check_int_ge(0, 上界纟总小步数)
        if 上界纟总小步数 <= 5:
            return True
        pass

    if not 鬽上界纟最小显链长 is None:
        上界纟最小显链长 = 鬽上界纟最小显链长
        首爻位纟靶值 = 首爻位纟(靶值)
        check_int_ge(首爻位纟靶值, 上界纟最小显链长)
        上界纟总小步数 = 上界纟最小显链长 -首爻位纟靶值
        check_int_ge(0, 上界纟总小步数)
        if 上界纟总小步数 <= 5:
            return True
        pass

    return False
def 估计冫下界纟最小显链长巛靶值牜一九七四扌(靶值, /):
    check_int_ge(1, 靶值)
    #下界牜一九七四:[ℓ(n) >= log2(n)+log2(v(n))-2.123164629...]
    #   => [ℓ(n) >= ceil(log2(n)+log2(v(n))-2.123164629...) >= ceil(log2(n*v(n))-2.13) == ceil_log2(n*v(n)/2**2.13) >= ceil_log2(n*v(n)*_fr)]
    return ceil_log2(靶值*阳爻数纟(靶值)*_fr)








def 估计冫下界纟最小显链长巛靶值牜精研综合扌(靶值, /, *, 鬽上界纟最小显链长, 鬽上界纟总小步数=None, 欤排除数据验证部分=False):
    '靶值 -> 下界纟最小显链长{靶值}'
    check_int_ge(1, 靶值)
    if 阳爻数纟(靶值) <= 3:
        return 估计冫下界纟最小显链长巛靶值牜平凡扌(靶值)

    if not 欤排除数据验证部分:
        #估计冫下界纟最小显链长巛靶值牜数据验证部纟一九六九扌
        if 欤已知成立冫下界纟最小显链长乊靶值牜猜想牜一九六九扌(靶值, 鬽上界纟最小显链长=鬽上界纟最小显链长, 鬽上界纟总小步数=鬽上界纟总小步数):
            return 估计冫下界纟最小显链长巛靶值牜猜想牜一九六九扌(靶值)


    return max(估计冫下界纟最小显链长巛靶值牜平凡扌(靶值), 估计冫下界纟最小显链长巛靶值牜一九七四扌(靶值))







__all__
from seed.math.power.addition_chain.shortest.lower_bound4len_optimal_addition_chain import 估计冫下界纟最小显链长巛靶值牜精研综合扌

from seed.math.power.addition_chain.shortest.lower_bound4len_optimal_addition_chain import 估计冫下界纟最小显链长巛靶值牜平凡扌, 估计冫下界纟最小显链长巛靶值牜一九七四扌, 估计冫下界纟最小显链长巛靶值牜数据验证部纟一九六九扌, 估计冫下界纟最小显链长巛靶值牜精研综合扌
from seed.math.power.addition_chain.shortest.lower_bound4len_optimal_addition_chain import 估计冫下界纟最小显链长巛靶值牜数据验证部纟一九六九扌, 欤已知成立冫下界纟最小显链长乊靶值牜猜想牜一九六九扌, 估计冫下界纟最小显链长巛靶值牜猜想牜一九六九扌
from seed.math.power.addition_chain.shortest.lower_bound4len_optimal_addition_chain import *
