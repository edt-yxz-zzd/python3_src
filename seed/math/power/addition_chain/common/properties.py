#__all__:goto
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/common/properties.py

seed.math.power.addition_chain.common.properties
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.common.properties -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.common.properties:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> 显链长纟([1])
0
>>> 显链长纟([1, 2])
1
>>> 显链长纟([1, 2, 3])
2

>>> 阳爻数纟(1)
1
>>> 阳爻数纟(2)
1
>>> 阳爻数纟(3)
2
>>> 阳爻数纟(4)
1
>>> 阳爻数纟(5)
2
>>> 阳爻数纟(6)
2
>>> 阳爻数纟(7)
3

>>> 首爻位纟(1)
0
>>> 首爻位纟(2)
1
>>> 首爻位纟(3)
1
>>> 首爻位纟(4)
2
>>> 首爻位纟(7)
2

>>> 小步数纟(1, 0)
0
>>> 小步数纟(2, 1)
0
>>> 小步数纟(4, 2)
0
>>> 小步数纟(8, 3)
0
>>> 小步数纟(3, 2)
1
>>> 小步数纟(5, 3)
1
>>> 小步数纟(9, 4)
1

py_adhoc_call   seed.math.power.addition_chain.common.properties   @f
]]]'''#'''
__all__ = r'''
显链长纟
阳爻数纟
首爻位纟
小步数纟

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...


def 显链长纟(加链, /):
    return -1+len(加链)
def 阳爻数纟(靶值, /):
    return 靶值.bit_count()
def 首爻位纟(靶值, /):
    #return floor_log2(靶值)
    return -1+靶值.bit_length()
def 小步数纟(靶值, 显链长, /):
    return 显链长 -首爻位纟(靶值)



__all__
from seed.math.power.addition_chain.common.properties import 显链长纟, 阳爻数纟, 首爻位纟, 小步数纟
from seed.math.power.addition_chain.common.properties import *
