#__all__:goto
r'''[[[
e ../../python3_src/seed/text/unicode/constant.py
[[
view ../lots/NOTE/unicode/cjk/汉字区.txt
===
中选方案:
  所选用稳定汉字区 := [一-龥] #一yi1 #龥yu4
  <<==:
  ######################
  [gb2312 < [一-龠] < [一-龥]]
  ######################
  统合码牜最初版:V1_1:只含两个汉字区:[一-龥][豈-鶴]
      ######################
      # Age=V1_1
      4E00..9FA5
      F900..FA2D
  ######################


]]

region
range vs interval
    范围:左闭右开区间
    区间:闭区间


seed.text.unicode.constant
py -m nn_ns.app.debug_cmd   seed.text.unicode.constant -x
py -m nn_ns.app.doctest_cmd seed.text.unicode.constant:__doc__ -ht


>>> chr(CHAR_ORD_UPPER)
Traceback (most recent call last):
    ...
ValueError: chr() arg not in range(0x110000)
>>> chr(CHAR_ORD_UPPER-1)
'\U0010ffff'
>>> chr(MAX_CHAR_ORD)
'\U0010ffff'
>>> chr(MAX_CHAR_ORD+1)
Traceback (most recent call last):
    ...
ValueError: chr() arg not in range(0x110000)
>>> (MAX_CHAR_ORD+1) == CHAR_ORD_UPPER
True
>>> hex(CHAR_ORD_UPPER)
'0x110000'







>>> def hx5u(u, /):
...     return hex(u)[2:].upper()
>>> def f4blk(ublk, /):
...     urng = range(*ublk)
...     i = urng[0]
...     j = urng[-1]
...     return (len(urng), chr(i)+chr(j), hx5u(i), hx5u(j))

>>> CJK_IDEOGRAPH_RANGES4UNICODE_V1_1
((19968, 40870), (63744, 64046))
>>> ublk, cblk = CJK_IDEOGRAPH_RANGES4UNICODE_V1_1
>>> f4blk(ublk)
(20902, '一龥', '4E00', '9FA5')
>>> f4blk(cblk)
(302, '豈鶴', 'F900', 'FA2D')


>>> f4blk(CJK_UNIFIED_IDEOGRAPH_RANGE4UNICODE_V1_1)
(20902, '一龥', '4E00', '9FA5')
>>> f4blk(CJK_COMPATIBILITY_IDEOGRAPH_RANGE4UNICODE_V1_1)
(302, '豈鶴', 'F900', 'FA2D')





>>> def g4intv(intv, /):
...     i,j = intv
...     return (j+1-i, chr(i)+chr(j), hx5u(i), hx5u(j))

>>> CJK_IDEOGRAPH_INTERVALS4UNICODE_V1_1
((19968, 40869), (63744, 64045))
>>> uintv, cintv = CJK_IDEOGRAPH_INTERVALS4UNICODE_V1_1
>>> g4intv(uintv)
(20902, '一龥', '4E00', '9FA5')
>>> g4intv(cintv)
(302, '豈鶴', 'F900', 'FA2D')


>>> g4intv(CJK_UNIFIED_IDEOGRAPH_INTERVAL4UNICODE_V1_1)
(20902, '一龥', '4E00', '9FA5')
>>> g4intv(CJK_COMPATIBILITY_IDEOGRAPH_INTERVAL4UNICODE_V1_1)
(302, '豈鶴', 'F900', 'FA2D')


>>> brief_repr4cjk_ideograph_intervals4unicode_v1_1
'一龥豈鶴'
>>> brief_repr4cjk_unified_ideograph_interval4unicode_v1_1
'一龥'
>>> brief_repr4cjk_compatibility_ideograph_interval4unicode_v1_1
'豈鶴'



#]]]'''
__all__ = r'''
CHAR_ORD_UPPER
    MAX_CHAR_ORD

CJK_IDEOGRAPH_RANGES4UNICODE_V1_1
    CJK_UNIFIED_IDEOGRAPH_RANGE4UNICODE_V1_1
    CJK_COMPATIBILITY_IDEOGRAPH_RANGE4UNICODE_V1_1

CJK_IDEOGRAPH_INTERVALS4UNICODE_V1_1
    CJK_UNIFIED_IDEOGRAPH_INTERVAL4UNICODE_V1_1
    CJK_COMPATIBILITY_IDEOGRAPH_INTERVAL4UNICODE_V1_1

brief_repr4cjk_ideograph_intervals4unicode_v1_1
    brief_repr4cjk_unified_ideograph_interval4unicode_v1_1
    brief_repr4cjk_compatibility_ideograph_interval4unicode_v1_1

'''.split()#'''
__all__



CHAR_ORD_UPPER = 0x110000
MAX_CHAR_ORD = CHAR_ORD_UPPER-1

chr(MAX_CHAR_ORD)

try:
    chr(CHAR_ORD_UPPER)
except ValueError:
    #ValueError: chr() arg not in range(0x110000)
    pass
else:
    raise 000


def _rng5hzhz(hzhz, /):
    i, j = map(ord, hzhz)
    return (i, j+1)
def _rngs5hzhzs(hzhzs, /):
    return tuple(_rng5hzhz(hzhzs[k:k+2]) for k in range(len(hzhzs))[::2])

CJK_IDEOGRAPH_RANGES4UNICODE_V1_1 = ((0x4E00, 0x9FA6), (0xF900, 0xFA2E))

(CJK_UNIFIED_IDEOGRAPH_RANGE4UNICODE_V1_1
,CJK_COMPATIBILITY_IDEOGRAPH_RANGE4UNICODE_V1_1
) = CJK_IDEOGRAPH_RANGES4UNICODE_V1_1




assert CJK_IDEOGRAPH_RANGES4UNICODE_V1_1 == _rngs5hzhzs('一龥豈鶴')
assert CJK_UNIFIED_IDEOGRAPH_RANGE4UNICODE_V1_1 == _rng5hzhz('一龥')
assert CJK_COMPATIBILITY_IDEOGRAPH_RANGE4UNICODE_V1_1 == _rng5hzhz('豈鶴')





def _intv5hzhz(hzhz, /):
    i, j = map(ord, hzhz)
    return (i, j)
def _intvs5hzhzs(hzhzs, /):
    return tuple(_intv5hzhz(hzhzs[k:k+2]) for k in range(len(hzhzs))[::2])


CJK_IDEOGRAPH_INTERVALS4UNICODE_V1_1 = ((0x4E00, 0x9FA5), (0xF900, 0xFA2D))
(CJK_UNIFIED_IDEOGRAPH_INTERVAL4UNICODE_V1_1
,CJK_COMPATIBILITY_IDEOGRAPH_INTERVAL4UNICODE_V1_1
) = CJK_IDEOGRAPH_INTERVALS4UNICODE_V1_1

assert CJK_IDEOGRAPH_INTERVALS4UNICODE_V1_1 == _intvs5hzhzs('一龥豈鶴')
assert CJK_UNIFIED_IDEOGRAPH_INTERVAL4UNICODE_V1_1 == _intv5hzhz('一龥')
assert CJK_COMPATIBILITY_IDEOGRAPH_INTERVAL4UNICODE_V1_1 == _intv5hzhz('豈鶴')





brief_repr4cjk_ideograph_intervals4unicode_v1_1 = '一龥豈鶴'
brief_repr4cjk_unified_ideograph_interval4unicode_v1_1 = '一龥'
brief_repr4cjk_compatibility_ideograph_interval4unicode_v1_1 = '豈鶴'

assert CJK_IDEOGRAPH_INTERVALS4UNICODE_V1_1 == _intvs5hzhzs(brief_repr4cjk_ideograph_intervals4unicode_v1_1)
assert CJK_UNIFIED_IDEOGRAPH_INTERVAL4UNICODE_V1_1 == _intv5hzhz(brief_repr4cjk_unified_ideograph_interval4unicode_v1_1)
assert CJK_COMPATIBILITY_IDEOGRAPH_INTERVAL4UNICODE_V1_1 == _intv5hzhz(brief_repr4cjk_compatibility_ideograph_interval4unicode_v1_1)





__all__
from seed.text.unicode.constant import CHAR_ORD_UPPER, MAX_CHAR_ORD
from seed.text.unicode.constant import CJK_IDEOGRAPH_RANGES4UNICODE_V1_1
from seed.text.unicode.constant import CJK_UNIFIED_IDEOGRAPH_RANGE4UNICODE_V1_1, CJK_COMPATIBILITY_IDEOGRAPH_RANGE4UNICODE_V1_1
from seed.text.unicode.constant import *
