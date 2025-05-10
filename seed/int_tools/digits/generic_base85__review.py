#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/digits/generic_base85__review.py
view others/数学/编程/generic_base85_encode.txt
  摘要冫极简情形

seed.int_tools.digits.generic_base85__review
py -m nn_ns.app.debug_cmd   seed.int_tools.digits.generic_base85__review -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.digits.generic_base85__review:__doc__ -ht # -ff -df

TODO: ++新增情形:[规模纟靶符集 > 规模纟源符集]
TODO: 根据表达式最终输出的整数来自适应精度的浮点数表达式(含:整数预测)(最终结果:取整:floor/ceil)(表达式运算:log,pow,mul,div,add,sub,floor,ceil)



[[
copy from:view others/数学/编程/generic_base85_encode.txt
[理论最小长度纟靶串(规模纟靶符集,规模纟源符集;长度纟源串) == ceil_log_(规模纟靶符集;规模纟源符集**长度纟源串) == ceil(长度纟源串*log_(规模纟靶符集;规模纟源符集))]

[码长纟起步牜靶 == 2]:
  #摘要冫极简情形:here
  [规模纟源符集 >= 3]
  [1 <= 码长纟截断牜源 <= floor_log_(规模纟源符集/(规模纟源符集-1);(规模纟源符集-1))]
  [2 <= 规模纟靶符集 == ceil_kth_root_(1+码长纟截断牜源;规模纟源符集**码长纟截断牜源)]
  [理论最小长度纟靶串(规模纟靶符集,规模纟源符集;码长纟截断牜源+1) -理论最小长度纟靶串(规模纟靶符集,规模纟源符集;码长纟截断牜源) >= 理论最小长度纟靶串(规模纟靶符集,规模纟源符集;1)] # == 码长纟起步牜靶
    #唯一性约束:无此，则 同一 规模纟靶符集 对应多个 码长纟截断牜源/码长纟截断牜靶
  [[码长牜源 :<- [码长纟起步牜源..=码长纟截断牜源]] -> [码长牜靶 := 理论最小长度纟靶串(规模纟靶符集,规模纟源符集;码长牜源)] -> [码长牜靶 == (1+码长牜源)]]
  [码长纟起步牜靶==1+码长纟起步牜源]
  [码长纟截断牜靶==1+码长纟截断牜源]
  [码长纟起步牜源 === 1]



]]



+brief:(码长纟截断牜源, 规模纟靶符集)
[[
===
py_adhoc_call   seed.int_tools.digits.generic_base85__review   ,枚举冫可行配置纟非完美编码巛规模纟源符集乊极简情形扌 +brief  '=2**8'
(1, 16)
(2, 41)
(3, 64)
(4, 85)
(5, 102)
(6, 116)
(7, 128)
(8, 139)
(9, 148)
(10, 155)
(11, 162)
(12, 168)
(13, 173)
(14, 177)
(15, 182)
(16, 185)
(17, 189)
(18, 192)
(19, 195)
(20, 197)
(21, 199)
(22, 202)
(23, 204)
(24, 206)
(25, 207)
(26, 209)
(27, 211)
(28, 212)
(29, 213)
(30, 215)
(31, 216)
(32, 217)
(33, 218)
(34, 219)
(35, 220)
(36, 221)
(37, 222)
(39, 223)
(40, 224)
(41, 225)
(43, 226)
(45, 227)
(46, 228)
(48, 229)
(50, 230)
(52, 231)
(55, 232)
(57, 233)
(60, 234)
(63, 235)
(67, 236)
(70, 237)
(75, 238)
(79, 239)
(84, 240)
(90, 241)
(97, 242)
(105, 243)
(114, 244)
(125, 245)
(138, 246)
(153, 247)
(173, 248)
(199, 249)
(232, 250)
(280, 251)
(351, 252)
(469, 253)
(706, 254)
(1415, 255)

===
注意:[206,207,209,...]跳过208,210,214
注意:[215..=255]
===
]]




from seed.int_tools.digits.generic_base85__review import *
]]]'''#'''
__all__ = r'''
理论最小长度纟靶串
乸配置纟非完美编码
枚举冫可行配置纟非完美编码巛规模纟源符集乊极简情形扌

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#from itertools import islice
from collections import namedtuple
from math import log, floor, ceil
from seed.math.floor_ceil import floor_log_, ceil_kth_root_, ceil_log_

from seed.tiny_.check import check_type_is, check_int_ge

#from seed.abc.abc__ver1 import abstractmethod, override, ABC
#from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...
乸配置纟非完美编码 = namedtuple('乸配置纟非完美编码', r'''
规模纟源符集
规模纟靶符集

码长纟起步牜源
码长纟起步牜靶

码长纟截断牜源
码长纟截断牜靶
'''#'''
)

def _ceil_log4pow_(base, base4y, e4y, /):
    #return ceil_log_(base, base4y**e4y)
    e = ceil(e4y*log(base4y,  base))
    if not base**(e-1) < base4y**e4y <= base**e:raise NotImplementedError(base, base4y, e4y)
    return e
def 理论最小长度纟靶串(规模纟靶符集,规模纟源符集,长度纟源串):
    #return ceil_log_(规模纟靶符集,规模纟源符集**长度纟源串)
    #return ceil(长度纟源串*log_(规模纟靶符集,规模纟源符集))
    return _ceil_log4pow_(规模纟靶符集,规模纟源符集,长度纟源串)
def _floor_log4ND_(N4base, D4base, y, /):
    check_int_ge(1, D4base)
    check_int_ge(1+D4base, N4base)
    check_int_ge(1, y)
    if not y.bit_length() < 2**12:raise NotImplementedError(N4base, D4base, y)
    e = floor(log(y, base:=N4base/D4base))
    if not e < 2**12:raise NotImplementedError(N4base, D4base, y, e)
    if not N4base**e <= y * D4base**e:raise NotImplementedError(N4base, D4base, y, e)
    if not y * D4base**(e+1) < N4base**(e+1):raise NotImplementedError(N4base, D4base, y, e)
    return e

def _ceil_kth_root_(k, x, /):
    check_int_ge(2, k)
    check_int_ge(2, x)
    return ceil_kth_root_(k, x)
    r = ceil(x**(1.0/k))
        # OverflowError: int too large to convert to float
    if not r**(k-1) < x:raise NotImplementedError(k, x)
    if not x <= r**k:raise NotImplementedError(k, x)
    return r

def 枚举冫可行配置纟非完美编码巛规模纟源符集乊极简情形扌(规模纟源符集, *, brief=False):
    '规模纟源符集/uint{>=3} -> Iter (乸配置纟非完美编码 if not brief else (码长纟截断牜源, 规模纟靶符集)) #非完美编码.极简情形:[码长纟起步牜靶 == 2]'
    check_type_is(bool, brief)
    check_int_ge(3, 规模纟源符集)
    码长纟起步牜源 = 1
        # !! 恒定关系
    码长纟起步牜靶 = 2
        # !! 极简情形
    assert 码长纟起步牜靶 == 1+码长纟起步牜源

    # [1 <= 码长纟截断牜源 <= floor_log_(规模纟源符集/(规模纟源符集-1);(规模纟源符集-1))]
    上限牜近似值 = _floor_log4ND_(规模纟源符集, (规模纟源符集-1), (规模纟源符集-1))
        #.上限牜近似值 = floor(log((规模纟源符集-1), base:=规模纟源符集/(规模纟源符集-1)))
        #.if not 上限牜近似值 < 2**12:raise NotImplementedError
        #.if not 规模纟源符集**上限牜近似值 <= (规模纟源符集-1)**(上限牜近似值+1):raise NotImplementedError
        #.if not (规模纟源符集-1)**(上限牜近似值+2) < 规模纟源符集**(上限牜近似值+1):raise NotImplementedError

    幂方值 = 1
    for 码长纟截断牜源 in range(1, 1+上限牜近似值):
        幂方值 *= 规模纟源符集
        # [幂方值 == 规模纟源符集**码长纟截断牜源]
        码长纟截断牜源
        码长纟截断牜靶 = 1+码长纟截断牜源
        # [2 <= 规模纟靶符集 == ceil_kth_root_(1+码长纟截断牜源;规模纟源符集**码长纟截断牜源)]
        规模纟靶符集 = _ceil_kth_root_(码长纟截断牜靶, 幂方值)
        assert 规模纟靶符集 >= 2
        # [理论最小长度纟靶串(规模纟靶符集,规模纟源符集;码长纟截断牜源+1) -理论最小长度纟靶串(规模纟靶符集,规模纟源符集;码长纟截断牜源) >= 理论最小长度纟靶串(规模纟靶符集,规模纟源符集;1)] # == 码长纟起步牜靶
        if not 理论最小长度纟靶串(规模纟靶符集,规模纟源符集,码长纟截断牜源+1) -理论最小长度纟靶串(规模纟靶符集,规模纟源符集,码长纟截断牜源) >= 码长纟起步牜靶:continue
        yield (乸配置纟非完美编码
(规模纟源符集
=规模纟源符集
,规模纟靶符集
=规模纟靶符集
#
,码长纟起步牜源
=码长纟起步牜源
,码长纟起步牜靶
=码长纟起步牜靶
#
,码长纟截断牜源
=码长纟截断牜源
,码长纟截断牜靶
=码长纟截断牜靶
) if not brief else (码长纟截断牜源, 规模纟靶符集))

__all__
from seed.int_tools.digits.generic_base85__review import *
