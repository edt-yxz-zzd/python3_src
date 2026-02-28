#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/int_repr7human7lex_order7alnum.py
    整数耂文本表达牜极简牜词典序牜字母数字
mv -iv ../../python3_src/seed/int_tools/int_repr7human7alnum7lex_order.py  ../../python3_src/seed/int_tools/int_repr7human7lex_order7alnum.py

seed.int_tools.int_repr7human7lex_order7alnum
py -m seed.int_tools.int_repr7human7lex_order7alnum
py -m nn_ns.app.debug_cmd   seed.int_tools.int_repr7human7lex_order7alnum -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.int_repr7human7lex_order7alnum:__doc__ -ht # -ff -df
#######
[[
old:e ../../python3_src/seed/int_tools/step_decoder/easy_int_lex_order_alnum_repr.py
.+1,$s/seed\.int_tools\.step_decoder\.easy_int_lex_order_alnum_repr/seed.int_tools.int_repr7human7lex_order7alnum
]]

#######
[[
源起:保存数据->文件太大->分裂文件
分裂文件:自动化命名:
view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py
view script/对称多项式讠基表达.py
]]
[[
版本一:
整数耂文本表达牜极简牜词典序牜字母数字
    编码效率低:基于十进制
    但考虑到用于 自动化命名，可读性 才是 首要目标
[字母表 =[def]= regex'[0-9][A-Y]']
    10+25 == 35
[字母表牜头胞 =[def]= regex'[WXY]']
    3
[字母表牜体胞 =[def]= regex'[0-9][A-V]']
    32==22+10
    [字母表牜躯胞 =[def]= regex'[0-9]']
        10
    [字母表牜颈胞 =[def]= regex'[A-V]']
        22==5+17
    [字母表牜颈胞牜保留{正整数} =[def]= regex'[R-V]']
        5
    [字母表牜颈胞牜实用{正整数} =[def]= regex'[A-Q]']
        #负整数:取反:[F-V]
        17
        [ABCD.EFGH.IJKL.MNOP.Q]
        [ABCDEFGHIJKLMNOPQ]

W = -
X = 0
Y = +
考虑负整数编码:
    取反冫正整数编码
考虑正整数编码:
    bug:Y[1-9] # !! 两个独立取反区间 比较=>负数时 次序有误:[ok:Y0<YB10][bad:W0<WU89]
    fixed:YA[1-9]
    YB[1-9][0-9]
    YC[1-9][0-9]{2}
    ...
    YP[1-9][0-9]{15}
    YQ[B-P][A-P][1-9][0-9]{...}
    YQQ[B-P][A-P][A-P][1-9][0-9]{...}
    YQQQ[B-P][A-P]{3}[1-9][0-9]{...}
    ...
    YQ{n}[B-P][A-P]{n}[1-9][0-9]{...}

[0123456789]
[OIZEASGLBP]...既非升序亦非降序

]]
[[
版本二:
    版本一:[1-9]需要3字节
    考虑改用5头胞,或更多
[字母表 =[def]= regex'[0-9][A-Y]']
    10+25 == 35
[字母表牜头胞 =[def]= regex'[UVWXY]']
    5
[字母表牜体胞 =[def]= regex'[0-9][A-T]']
    30==20+10
    [字母表牜躯胞 =[def]= regex'[0-9]']
        10
    [字母表牜颈胞 =[def]= regex'[A-T]']
        20==3+17
    [字母表牜颈胞牜保留{正整数} =[def]= regex'[R-T]']
        3
    [字母表牜颈胞牜实用{正整数} =[def]= regex'[A-Q]']
        #负整数:取反:[D-T]
        17
        [ABCD.EFGH.IJKL.MNOP.Q]
        [ABCDEFGHIJKLMNOPQ]

U = -[A-T]+[0-9]+
V = -[1-9]
W = 0
X = +[1-9]
Y = +[A-T]+[0-9]+

e ../../python3_src/seed/int_tools/int_repr7lex_order7base.py
e ../../python3_src/seed/types/WordSeq.py
]]




'#'; __doc__ = r'#'
>>> 匴整数耂文本表达牜极简牜词典序牜字母数字牜头胞集规模三.列表纟字母表牜头胞辻多种体胞
('WXY', 'ABCDEFGHIJKLMNOPQRSTUV', '0123456789')

>>> 匴整数耂文本表达牜极简牜词典序牜字母数字牜头胞集规模三.符型相关信息
(35, (32, 10, 0), (3, 22, 10), (9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 34, 33, 32))

>>> from seed.types.FrozenDict import FrozenDict
>>> 匴整数耂文本表达牜极简牜词典序牜字母数字牜头胞集规模三.总字母表相关信息 == ('0123456789ABCDEFGHIJKLMNOPQRSTUVWXY', FrozenDict({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34}), FrozenDict({'W': 'Y', 'X': 'X', 'Y': 'W', 'A': 'V', 'B': 'U', 'C': 'T', 'D': 'S', 'E': 'R', 'F': 'Q', 'G': 'P', 'H': 'O', 'I': 'N', 'J': 'M', 'K': 'L', 'L': 'K', 'M': 'J', 'N': 'I', 'O': 'H', 'P': 'G', 'Q': 'F', 'R': 'E', 'S': 'D', 'T': 'C', 'U': 'B', 'V': 'A', '0': '9', '1': '8', '2': '7', '3': '6', '4': '5', '5': '4', '6': '3', '7': '2', '8': '1', '9': '0'}))
True





#>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌 = 详解读冫整数巛文本表达牜极简牜词典序牜字母数字牜头胞三扌
#>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌 = 表述冫整数讠文本表达牜极简牜词典序牜字母数字牜头胞三扌
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌 = _匴三.表述冫数据讠字符串表达扌
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌 = _匴三.详解读冫数据巛字符串表达扌
>>> decode_int5txt7human7lex_order7alnum_ = decode_int5txt7human7lex_order7alnum7headW_
>>> encode_int2txt7human7lex_order7alnum_ = encode_int2txt7human7lex_order7alnum7headW_

>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('X', 欤校验=True)
(0, 1)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('YA1', 欤校验=True)
(1, 3)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('YA9', 欤校验=True)
(9, 3)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('YB10', 欤校验=True)
(10, 4)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('YB99', 欤校验=True)
(99, 4)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('YP1000000000000000', 欤校验=True)
(1000000000000000, 18)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('YP9999999999999999', 欤校验=True)
(9999999999999999, 18)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('YQBA10000000000000000', 欤校验=True)
(10000000000000000, 21)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('YQBA99999999999999999', 欤校验=True)
(99999999999999999, 21)



>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('X', 欤校验=True)
(0, 1)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('WV8', 欤校验=True)
(-1, 3)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('WV0', 欤校验=True)
(-9, 3)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('WU89', 欤校验=True)
(-10, 4)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('WU00', 欤校验=True)
(-99, 4)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('WG8999999999999999', 欤校验=True)
(-1000000000000000, 18)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('WG0000000000000000', 欤校验=True)
(-9999999999999999, 18)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('WFUV89999999999999999', 欤校验=True)
(-10000000000000000, 21)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('WFUV00000000000000000', 欤校验=True)
(-99999999999999999, 21)


>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(0, 欤校验=True)
'X'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(1, 欤校验=True)
'YA1'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(9, 欤校验=True)
'YA9'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(10, 欤校验=True)
'YB10'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(99, 欤校验=True)
'YB99'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(1000000000000000, 欤校验=True)
'YP1000000000000000'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(9999999999999999, 欤校验=True)
'YP9999999999999999'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(10000000000000000, 欤校验=True)
'YQBA10000000000000000'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(99999999999999999, 欤校验=True)
'YQBA99999999999999999'



>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(0, 欤校验=True)
'X'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(-1, 欤校验=True)
'WV8'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(-9, 欤校验=True)
'WV0'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(-10, 欤校验=True)
'WU89'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(-99, 欤校验=True)
'WU00'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(-1000000000000000, 欤校验=True)
'WG8999999999999999'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(-9999999999999999, 欤校验=True)
'WG0000000000000000'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(-10000000000000000, 欤校验=True)
'WFUV89999999999999999'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(-99999999999999999, 欤校验=True)
'WFUV00000000000000000'


>>> us = [1, 9, 10, 99, 100, 999, 1000000000000000, 9999999999999999, 10000000000000000, 99999999999999999]
>>> ints = [*map(int.__neg__, reversed(us)), 0, *us]
>>> len(ints) == len(set(ints))
True
>>> ints == sorted(ints)
True

>>> ss = [*map(encode_int2txt7human7lex_order7alnum_, ints)]
>>> len(ss) == len(set(ss))
True
>>> ss == sorted(ss)
True

>>> _ints = [*map(decode_int5txt7human7lex_order7alnum_, ss)]
>>> _ints == ints
True


>>> for i, s in zip(ints, ss):
...     print(s, i, sep=':')
WFUV00000000000000000:-99999999999999999
WFUV89999999999999999:-10000000000000000
WG0000000000000000:-9999999999999999
WG8999999999999999:-1000000000000000
WT000:-999
WT899:-100
WU00:-99
WU89:-10
WV0:-9
WV8:-1
X:0
YA1:1
YA9:9
YB10:10
YB99:99
YC100:100
YC999:999
YP1000000000000000:1000000000000000
YP9999999999999999:9999999999999999
YQBA10000000000000000:10000000000000000
YQBA99999999999999999:99999999999999999







>>> 匴整数耂文本表达牜极简牜词典序牜字母数字牜头胞集规模五.列表纟字母表牜头胞辻多种体胞
('UVWXY', 'ABCDEFGHIJKLMNOPQRST', '0123456789')

>>> 匴整数耂文本表达牜极简牜词典序牜字母数字牜头胞集规模五.符型相关信息
(35, (30, 10, 0), (5, 20, 10), (9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 34, 33, 32, 31, 30))

>>> from seed.types.FrozenDict import FrozenDict
>>> 匴整数耂文本表达牜极简牜词典序牜字母数字牜头胞集规模五.总字母表相关信息 == ('0123456789ABCDEFGHIJKLMNOPQRSTUVWXY', FrozenDict({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34}), FrozenDict({'U': 'Y', 'V': 'X', 'W': 'W', 'X': 'V', 'Y': 'U', 'A': 'T', 'B': 'S', 'C': 'R', 'D': 'Q', 'E': 'P', 'F': 'O', 'G': 'N', 'H': 'M', 'I': 'L', 'J': 'K', 'K': 'J', 'L': 'I', 'M': 'H', 'N': 'G', 'O': 'F', 'P': 'E', 'Q': 'D', 'R': 'C', 'S': 'B', 'T': 'A', '0': '9', '1': '8', '2': '7', '3': '6', '4': '5', '5': '4', '6': '3', '7': '2', '8': '1', '9': '0'}))
True





#>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌 = 详解读冫整数巛文本表达牜极简牜词典序牜字母数字牜头胞五扌
#>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌 = 表述冫整数讠文本表达牜极简牜词典序牜字母数字牜头胞五扌
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌 = _匴五.表述冫数据讠字符串表达扌
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌 = _匴五.详解读冫数据巛字符串表达扌
>>> decode_int5txt7human7lex_order7alnum_ = decode_int5txt7human7lex_order7alnum7headU_
>>> encode_int2txt7human7lex_order7alnum_ = encode_int2txt7human7lex_order7alnum7headU_

>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('W', 欤校验=True)
(0, 1)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('X1', 欤校验=True)
(1, 2)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('X9', 欤校验=True)
(9, 2)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('YB10', 欤校验=True)
(10, 4)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('YB99', 欤校验=True)
(99, 4)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('YP1000000000000000', 欤校验=True)
(1000000000000000, 18)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('YP9999999999999999', 欤校验=True)
(9999999999999999, 18)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('YQBA10000000000000000', 欤校验=True)
(10000000000000000, 21)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('YQBA99999999999999999', 欤校验=True)
(99999999999999999, 21)



>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('W', 欤校验=True)
(0, 1)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('V8', 欤校验=True)
(-1, 2)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('V0', 欤校验=True)
(-9, 2)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('US89', 欤校验=True)
(-10, 4)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('US00', 欤校验=True)
(-99, 4)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('UE8999999999999999', 欤校验=True)
(-1000000000000000, 18)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('UE0000000000000000', 欤校验=True)
(-9999999999999999, 18)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('UDST89999999999999999', 欤校验=True)
(-10000000000000000, 21)
>>> 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌('UDST00000000000000000', 欤校验=True)
(-99999999999999999, 21)


>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(0, 欤校验=True)
'W'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(1, 欤校验=True)
'X1'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(9, 欤校验=True)
'X9'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(10, 欤校验=True)
'YB10'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(99, 欤校验=True)
'YB99'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(1000000000000000, 欤校验=True)
'YP1000000000000000'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(9999999999999999, 欤校验=True)
'YP9999999999999999'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(10000000000000000, 欤校验=True)
'YQBA10000000000000000'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(99999999999999999, 欤校验=True)
'YQBA99999999999999999'



>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(0, 欤校验=True)
'W'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(-1, 欤校验=True)
'V8'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(-9, 欤校验=True)
'V0'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(-10, 欤校验=True)
'US89'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(-99, 欤校验=True)
'US00'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(-1000000000000000, 欤校验=True)
'UE8999999999999999'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(-9999999999999999, 欤校验=True)
'UE0000000000000000'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(-10000000000000000, 欤校验=True)
'UDST89999999999999999'
>>> 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(-99999999999999999, 欤校验=True)
'UDST00000000000000000'


>>> us = [1, 9, 10, 99, 100, 999, 1000000000000000, 9999999999999999, 10000000000000000, 99999999999999999]
>>> ints = [*map(int.__neg__, reversed(us)), 0, *us]
>>> len(ints) == len(set(ints))
True
>>> ints == sorted(ints)
True

>>> ss = [*map(encode_int2txt7human7lex_order7alnum_, ints)]
>>> len(ss) == len(set(ss))
True
>>> ss == sorted(ss)
True

>>> _ints = [*map(decode_int5txt7human7lex_order7alnum_, ss)]
>>> _ints == ints
True


>>> for i, s in zip(ints, ss):
...     print(s, i, sep=':')
UDST00000000000000000:-99999999999999999
UDST89999999999999999:-10000000000000000
UE0000000000000000:-9999999999999999
UE8999999999999999:-1000000000000000
UR000:-999
UR899:-100
US00:-99
US89:-10
V0:-9
V8:-1
W:0
X1:1
X9:9
YB10:10
YB99:99
YC100:100
YC999:999
YP1000000000000000:1000000000000000
YP9999999999999999:9999999999999999
YQBA10000000000000000:10000000000000000
YQBA99999999999999999:99999999999999999










[[
py -m seed.int_tools.int_repr7human7lex_order7alnum encode 0 1 -1 999 -999 +11 -11 +7777 -7777
    W
    X1
    V8
    YC999
    UR000
    YB11
    US88
    YD7777
    UQ2222

py -m seed.int_tools.int_repr7human7lex_order7alnum decode W X1 V8 YC999 UR000 YB11 US88 YD7777 UQ2222
    0
    1
    -1
    999
    -999
    11
    -11
    7777
    -7777

py -m seed.int_tools.int_repr7human7lex_order7alnum xdecode  aaaUQ22220000bbb --begin 3 --end -3
    (-7777, 9)

py -m seed.int_tools.int_repr7human7lex_order7alnum xdecode  aaaUQ22220000bbb --begin 3 --end 8
    ^EOFError: (4, 3, b'\x07\x07\x07')
py -m seed.int_tools.int_repr7human7lex_order7alnum xdecode  aaaUQ22220000bbb --begin 3 --end 9
    (-7777, 9)

py -m seed.int_tools.int_repr7human7lex_order7alnum xdecode  aaaUQ22220000bbb --begin 3 --end 9 --strict
    -7777

py -m seed.int_tools.int_repr7human7lex_order7alnum xdecode  aaaUQ22220000bbb --begin 3 --end 10 --strict
    ^seed.int_tools.int_repr7lex_order7base.FormatError: ('0', 9, 10)

]]
[[
e ../../python3_src/nn_ns/app/int_repr7human.py
e ../../python3_src/bash_script/app/int_repr7human
int_repr7human encode 7777
    YD7777
]]

py_adhoc_call   seed.int_tools.int_repr7human7lex_order7alnum   @f
]]]'''#'''
#:__all__ = r'''
#:表述冫整数讠文本表达牜极简牜词典序牜字母数字扌
#:详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌
#:    详解读冫整数巛趃文本表达牜极简牜词典序牜字母数字扌
#:        详解读冫自然数巛趃文本表达牜极简牜词典序牜字母数字扌
#:解读冫整数巛文本表达牜极简牜词典序牜字母数字扌
#:    解读冫整数巛趃文本表达牜极简牜词典序牜字母数字扌
#:        解读冫自然数巛趃文本表达牜极简牜词典序牜字母数字扌
#:
#:encode_int2txt7human7lex_order7alnum_
#:xdecode_int5txt7human7lex_order7alnum_
#:    xdecode_int5iter_chars7human7lex_order7alnum_
#:        xdecode_uint5iter_chars7human7lex_order7alnum_
#:decode_int5txt7human7lex_order7alnum_
#:    decode_int5iter_chars7human7lex_order7alnum_
#:        decode_uint5iter_chars7human7lex_order7alnum_
#:
#:FormatError
#:'''.split()#'''
__all__ = r'''
乸匴整数耂文本表达牜极简牜词典序牜字母数字牜头胞集规模三
    匴整数耂文本表达牜极简牜词典序牜字母数字牜头胞集规模三
        表述冫整数讠文本表达牜极简牜词典序牜字母数字牜头胞三扌
        解读冫整数巛文本表达牜极简牜词典序牜字母数字牜头胞三扌
        详解读冫整数巛文本表达牜极简牜词典序牜字母数字牜头胞三扌
        详解读冫整数巛趃文本表达牜极简牜词典序牜字母数字牜头胞三扌
            encode_int2txt7human7lex_order7alnum7headW_
            decode_int5txt7human7lex_order7alnum7headW_
            xdecode_int5txt7human7lex_order7alnum7headW_
            xdecode_int5iter_chars7human7lex_order7alnum7headW_

乸匴整数耂文本表达牜极简牜词典序牜字母数字牜头胞集规模五
    匴整数耂文本表达牜极简牜词典序牜字母数字牜头胞集规模五
        表述冫整数讠文本表达牜极简牜词典序牜字母数字牜头胞五扌
        解读冫整数巛文本表达牜极简牜词典序牜字母数字牜头胞五扌
        详解读冫整数巛文本表达牜极简牜词典序牜字母数字牜头胞五扌
        详解读冫整数巛趃文本表达牜极简牜词典序牜字母数字牜头胞五扌
            encode_int2txt7human7lex_order7alnum7headU_
            decode_int5txt7human7lex_order7alnum7headU_
            xdecode_int5txt7human7lex_order7alnum7headU_
            xdecode_int5iter_chars7human7lex_order7alnum7headU_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import islice, chain
from seed.tiny_.check import check_type_is, check_int_ge, check_int_ge_le
#from seed.helper.repr_input import repr_helper
#from seed.int_tools.digits.uint25radix_repr import uint2radix_repr_, uint5radix_repr_
    #digits = uint2radix_repr_(radix, u, is_big_endian=)
    #u = uint5radix_repr_(radix, digits, is_big_endian=)
from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.int_tools.int_repr7lex_order7base import FormatError
from seed.int_tools.int_repr7lex_order7base import 魖数据字符串表达牜词典序牜前置长度
from seed.int_tools.int_repr7lex_order7base import 魖整数位元串表达牜词典序牜前置长度牜整数零编码为单胞


___end_mark_of_excluded_global_names__0___ = ...

###########################
###########################
###########################
FormatError = FormatError

class 乸匴整数耂文本表达牜极简牜词典序牜字母数字牜头胞集规模三(魖整数位元串表达牜词典序牜前置长度牜整数零编码为单胞, 魖数据字符串表达牜词典序牜前置长度):
    ___no_slots_ok___ = True
    #@override
    列表纟字母表牜头胞辻多种体胞 = (
    ('WXY'
    ,'ABCDEFGHIJKLMNOPQRSTUV'
    ,'0123456789'
    ))

    @override
    def 罓解读冫正整数巛定型定长前取器扌(sf, 删负偏移后头胞纟正整数编码, 定型定长前取器, /):
        assert 删负偏移后头胞纟正整数编码 == 1
        return _罓解读冫正整数巛定型定长前取器扌(sf, 定型定长前取器)
    @override
    def 罓表述冫正整数讠趃序列纟带符型位元串扌(sf, 正整数, /):
        #bug:头胞串 = bytes([1]) #删负偏移后
        头胞串 = bytes([2])
        yield (0, 头胞串)
        yield from _罓表述冫正整数讠趃序列纟带符型位元串扌(sf, 正整数)
_匴三 = 匴整数耂文本表达牜极简牜词典序牜字母数字牜头胞集规模三 = 乸匴整数耂文本表达牜极简牜词典序牜字母数字牜头胞集规模三()

表述冫整数讠文本表达牜极简牜词典序牜字母数字牜头胞三扌 = _匴三.encode_dat2txt7lex_order_
解读冫整数巛文本表达牜极简牜词典序牜字母数字牜头胞三扌 = _匴三.decode_dat5txt7lex_order_
详解读冫整数巛文本表达牜极简牜词典序牜字母数字牜头胞三扌 = _匴三.xdecode_dat5txt7lex_order_
详解读冫整数巛趃文本表达牜极简牜词典序牜字母数字牜头胞三扌 = _匴三.xdecode_dat5iter_chars7lex_order_
encode_int2txt7human7lex_order7alnum7headW_ = 表述冫整数讠文本表达牜极简牜词典序牜字母数字牜头胞三扌
decode_int5txt7human7lex_order7alnum7headW_ = 解读冫整数巛文本表达牜极简牜词典序牜字母数字牜头胞三扌
xdecode_int5txt7human7lex_order7alnum7headW_ = 详解读冫整数巛文本表达牜极简牜词典序牜字母数字牜头胞三扌
xdecode_int5iter_chars7human7lex_order7alnum7headW_ = 详解读冫整数巛趃文本表达牜极简牜词典序牜字母数字牜头胞三扌

class 乸匴整数耂文本表达牜极简牜词典序牜字母数字牜头胞集规模五(魖整数位元串表达牜词典序牜前置长度牜整数零编码为单胞, 魖数据字符串表达牜词典序牜前置长度):
    ___no_slots_ok___ = True
    #@override
    列表纟字母表牜头胞辻多种体胞 = (
    ('UVWXY'
    ,'ABCDEFGHIJKLMNOPQRST'
    ,'0123456789'
    ))

    @override
    def 罓解读冫正整数巛定型定长前取器扌(sf, 删负偏移后头胞纟正整数编码, 定型定长前取器, /):
        if 删负偏移后头胞纟正整数编码 == 1:
            [体胞] = 定型定长前取器.读取冫位元串牜子表扌(符型:=2, 数目:=1)
            正整数 = 体胞
            return 正整数
        assert 删负偏移后头胞纟正整数编码 == 2
        return _罓解读冫正整数巛定型定长前取器扌(sf, 定型定长前取器)
    @override
    def 罓表述冫正整数讠趃序列纟带符型位元串扌(sf, 正整数, /):
        assert 正整数 >= 1
        if 正整数 <= 9:
            #bug:头胞串 = bytes([1]) #删负偏移后
            头胞串 = bytes([3])
            yield (0, 头胞串)
            体胞串 = bytes([正整数])
            yield (2, 体胞串)
            return
        #bug:头胞串 = bytes([2]) #删负偏移后
        头胞串 = bytes([4])
        yield (0, 头胞串)
        yield from _罓表述冫正整数讠趃序列纟带符型位元串扌(sf, 正整数)
_匴五 = 匴整数耂文本表达牜极简牜词典序牜字母数字牜头胞集规模五 = 乸匴整数耂文本表达牜极简牜词典序牜字母数字牜头胞集规模五()

表述冫整数讠文本表达牜极简牜词典序牜字母数字牜头胞五扌 = _匴五.encode_dat2txt7lex_order_
解读冫整数巛文本表达牜极简牜词典序牜字母数字牜头胞五扌 = _匴五.decode_dat5txt7lex_order_
详解读冫整数巛文本表达牜极简牜词典序牜字母数字牜头胞五扌 = _匴五.xdecode_dat5txt7lex_order_
详解读冫整数巛趃文本表达牜极简牜词典序牜字母数字牜头胞五扌 = _匴五.xdecode_dat5iter_chars7lex_order_
encode_int2txt7human7lex_order7alnum7headU_ = 表述冫整数讠文本表达牜极简牜词典序牜字母数字牜头胞五扌
decode_int5txt7human7lex_order7alnum7headU_ = 解读冫整数巛文本表达牜极简牜词典序牜字母数字牜头胞五扌
xdecode_int5txt7human7lex_order7alnum7headU_ = 详解读冫整数巛文本表达牜极简牜词典序牜字母数字牜头胞五扌
xdecode_int5iter_chars7human7lex_order7alnum7headU_ = 详解读冫整数巛趃文本表达牜极简牜词典序牜字母数字牜头胞五扌





def _罓解读冫正整数巛定型定长前取器扌(sf, 定型定长前取器, /):
    num_Qs = 0
    while 1:
        [颈胞] = 定型定长前取器.读取冫位元串牜子表扌(符型:=1, 数目:=1)
        if not 颈胞 == 16:
            # not Q
            break
        num_Qs += 1
    num_Qs, 颈胞
    if 颈胞 > 16:raise FormatError#NotImplementedError
    #assert 0 <= 颈胞 < 16
    _颈胞串 = 定型定长前取器.读取冫位元串牜子表扌(符型:=1, 数目:=num_Qs)
    颈胞串 = bytes([颈胞]) + _颈胞串
    体胞数 = 1+_uint5base16_(颈胞串)
    体胞串 = 定型定长前取器.读取冫位元串牜子表扌(符型:=2, 数目:=体胞数)
    正整数 = _uint5base10_(体胞串)
    return 正整数
def _罓表述冫正整数讠趃序列纟带符型位元串扌(sf, 正整数, /):
    assert 正整数 >= 1
    体胞串 = _uint2base10_(正整数)
    体胞数 = len(体胞串)
    assert 体胞数 >= 1
    颈胞串 = _uint2base16_(-1+体胞数)
    颈胞数 = len(颈胞串)
    assert 颈胞数 >= 1
    num_Qs = -1+颈胞数
    Qs = bytes([16])*num_Qs
    yield (1, Qs)
    yield (1, 颈胞串)
    yield (2, 体胞串)


def _uint5base16_(us, /):
    s = ''.join(f'{u:X}' for u in us)
    u = int(s, 16)
    return u
def _uint2base16_(u, /):
    s = f'{u:X}'
    us = bytes(int(c, 16) for c in s)
    return us
def _uint5base10_(us, /):
    s = ''.join(map(str, us))
    u = int(s, 10)
    return u
def _uint2base10_(u, /):
    s = str(u)
    us = bytes(int(c, 10) for c in s)
    return us









###########################
def _main_(args=None, /):
    from seed.int_tools.int_repr7human7lex_order7alnum import encode_int2txt7human7lex_order7alnum7headU_, decode_int5txt7human7lex_order7alnum7headU_, xdecode_int5txt7human7lex_order7alnum7headU_, xdecode_int5iter_chars7human7lex_order7alnum7headU_
    import argparse
    parser = argparse.ArgumentParser(
        description='encode/decode int: [U-Y][A-T]*[0-9]*'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    action7subcmd = parser.add_subparsers(dest='subcmd', required=True)


    #######
    subparser7encode = action7subcmd.add_parser('encode', description='encode ints...')
    subparser7encode.add_argument('ints', nargs='*', type=int, help='ints to be encoded')

    #######
    subparser7decode = action7subcmd.add_parser('decode', description='strict decode strs as ints...')
    subparser7decode.add_argument('strs', nargs='*', type=str, help='strs to be encoded')


    #######
    subparser7xdecode = action7subcmd.add_parser('xdecode', description='nonstrict decode txt as int:output:(int, end)')
    subparser7xdecode.add_argument('txt', type=str, help='txt to be encoded')
    #subparser7xdecode.add_argument('--with_end', action='store_true', default=False, help='nonstrict mode:output:(int, end)')
    subparser7xdecode.add_argument('--strict', action='store_true', default=False, help='strict mode:output:int only')
    subparser7xdecode.add_argument('--begin', type=int, default=None, help='begin addr for txt')
    subparser7xdecode.add_argument('--end', type=int, default=None, help='end addr for txt')

    #######
    args = parser.parse_args(args)
    match args.subcmd:
        case 'encode':
            # encode_int2txt7human7lex_order7alnum7headU_(int, /, *, validate=True) -> str
            for i in args.ints:
                print(encode_int2txt7human7lex_order7alnum7headU_(i))
        case 'decode':
            # decode_int5txt7human7lex_order7alnum7headU_(txt, begin=None, end=None, /, *, validate=True) -> int
            for s in args.strs:
                print(decode_int5txt7human7lex_order7alnum7headU_(s))
        case 'xdecode':
            # xdecode_int5txt7human7lex_order7alnum7headU_(txt, begin=None, end=None, /, *, validate=True) -> (int, end)
            (s, j, k) = _args = (args.txt, args.begin, args.end)
            (j, k, _1) = slice(j, k).indices(len(s))
            if args.strict:
                print(decode_int5txt7human7lex_order7alnum7headU_(s, j, k))
            else:
                print(xdecode_int5txt7human7lex_order7alnum7headU_(s, j, k))
        case bad:
            raise Exception(bad)
if __name__ == '__main__':
    from seed.int_tools.int_repr7human7lex_order7alnum import *
    from seed.int_tools.int_repr7human7lex_order7alnum import encode_int2txt7human7lex_order7alnum7headU_, decode_int5txt7human7lex_order7alnum7headU_, xdecode_int5txt7human7lex_order7alnum7headU_, xdecode_int5iter_chars7human7lex_order7alnum7headU_
    if 1:from seed.int_tools.int_repr7human7lex_order7alnum import _main_
    _main_()

###########################









###########################
###########################
###########################
###########################
#:_字母表牜头胞 = 'WXY'
#:_字母表牜躯胞 = '0123456789'
#:_字母表牜颈胞 = 'ABCDEFGHIJKLMNOPQRSTUV'
#:_字母表牜颈胞牜实用 = 'ABCDEFGHIJKLMNOPQ'
#:_字母表牜十六进制牜自定义 = 'ABCDEFGHIJKLMNOP'
#:_字母表牜十六进制牜标准 = '0123456789ABCDEF'
#:assert len(_字母表牜颈胞) == 22
#:assert len(_字母表牜颈胞牜实用) == 17
#:assert len(_字母表牜十六进制牜自定义) == 16
#:assert len(_字母表牜十六进制牜标准) == 16
#:#_d2c16_ = _字母表牜十六进制牜自定义.__getitem__
#:_hex2c16_ = dict(zip(_字母表牜十六进制牜标准, _字母表牜十六进制牜自定义)).__getitem__
#:_hex5c16_ = dict(zip(_字母表牜十六进制牜自定义, _字母表牜十六进制牜标准)).__getitem__
#:def _表述冫自然数讠十六进制牜字母扌(u, /):
#:    check_int_ge(0, u)
#:    #.digits = uint2radix_repr_(radix:=16, u, is_big_endian=True)
#:    #.return ''.join(map(_d2c16_, digits))
#:    s = f'{u:X}'
#:    return ''.join(map(_hex2c16_, s))
#:def _解读冫自然数巛十六进制牜字母扌(s, /):
#:    s = ''.join(map(_hex5c16_, s))
#:    return int(s, 16)
#:
#:def __():
#:    #bug:ss = [_字母表牜头胞, _字母表牜躯胞, _字母表牜颈胞牜实用]
#:    ss = [_字母表牜头胞, _字母表牜躯胞, _字母表牜颈胞]
#:    d = {}
#:    for s in ss:
#:        for a, b in zip(s, reversed(s)):
#:            d[a] = b
#:    #bug:assert len(d) == sum(map(len, ss)) == 3+10+17 == 30
#:    assert len(d) == sum(map(len, ss)) == 3+10+22 == 35
#:    return d
#:_d = __()
#:_取反冫字符扌 = _d.__getitem__
###########################
#:class FormatError(Exception):pass
#:def 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(整数, /, *, 欤校验=True):
#:    '整数/int -> 文本/str'
#:    def iter4pos_(u, /):
#:        assert u > 0
#:        yield 'Y'
#:        s09 = str(u)
#:        len_s09 = len(s09)
#:        if not len_s09 == 1:
#:            sAP = _表述冫自然数讠十六进制牜字母扌(len_s09-1)
#:            sQ = 'Q'*(-1+len(sAP))
#:            yield sQ
#:            yield sAP
#:        else:
#:            #fixed:Y[1-9] --> YA[1-9]
#:            yield 'A'
#:        yield s09
#:    def on_pos_(u, /):
#:        return ''.join(iter4pos_(u))
#:    def on_neg_(n, /):
#:        assert n < 0
#:        s = on_pos_(-n)
#:        _s = ''.join(map(_取反冫字符扌, s))
#:        return _s
#:    def _main(i, /):
#:        if i < 0:
#:            return on_neg_(i)
#:        if i > 0:
#:            return on_pos_(i)
#:        return 'X'
#:    def main(欤校验, 整数, /):
#:        check_type_is(bool, 欤校验)
#:        check_type_is(int, 整数)
#:        s = _main(整数)
#:        if 欤校验:
#:            end = len(s)
#:            (_i, _end) = 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌(s, 0, end, 欤校验=False)
#:            if not _i == 整数:raise Exception((整数, end), (_i, _end), s)
#:            if not _end == end:raise Exception((整数, end), (_i, _end), s)
#:        return s
#:    return main(欤校验, 整数)
#:
#:def 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌(文本, 起址=None, 讫址=None, /, *, 欤校验=True):
#:    '文本/str -> 起址/uint -> 讫址/uint -> (整数/int, 讫址/uint)'
#:    #########
#:    check_type_is(bool, 欤校验)
#:    check_type_is(str, 文本)
#:    #########
#:    js = range(len(文本))[起址:讫址]
#:    if not js:raise FormatError('<EOF>')
#:    起址 = js[0]
#:    讫址 = 1+js[-1]
#:    #########
#:    check_int_ge(0, 起址)
#:    check_int_ge_le(起址, len(文本), 讫址)
#:    #########
#:    it = map(文本.__getitem__, range(起址, 讫址))
#:    (i, sz, _it) = 详解读冫整数巛趃文本表达牜极简牜词典序牜字母数字扌(it)
#:    _end = 起址+sz
#:    if 欤校验:
#:        s = 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌(i, 欤校验=False)
#:        if not s == (_s:=文本[起址:_end]):raise Exception(_s, i, s)
#:    return (i, _end)
#:
#:def _next(it, errmsg, /):
#:    for c in it:
#:        return c
#:    raise FormatError(errmsg)
#:def 详解读冫整数巛趃文本表达牜极简牜词典序牜字母数字扌(趃文本, /):
#:    '趃文本/(Iter char) -> (整数/int, 字符数牜消耗/uint, 趃文本/Iterator{char})'
#:    趃文本 = iter(趃文本)
#:    match _next(趃文本, '<EOF>'):
#:        case 'Y':
#:            sign = +1
#:            it = 趃文本
#:        case 'X':
#:            return (0, 1, 趃文本)
#:        case 'W':
#:            sign = -1
#:            it = map(_取反冫字符扌, 趃文本)
#:        case bad:
#:            raise FormatError('expected:[WXY]', bad)
#:        #case
#:    sign, it
#:    (u, _sz, _it) = 详解读冫自然数巛趃文本表达牜极简牜词典序牜字母数字扌(it, 欤允零=False)
#:    if u == 0:raise 000
#:    i = sign*u
#:    return (i, 1+_sz, 趃文本)
#:def 详解读冫自然数巛趃文本表达牜极简牜词典序牜字母数字扌(趃文本, /, *, 欤允零=True):
#:    '趃文本/(Iter char) -> (自然数/uint, 字符数牜消耗/uint, 趃文本/Iterator{char})'
#:    it = 趃文本 = iter(趃文本)
#:    num_Qs = 0
#:    c = _next(it, '<EOF>')
#:    while c == 'Q':
#:        num_Qs += 1
#:        c = _next(it, '<EOF>')
#:    num_Qs, c
#:    777;sz = 1+num_Qs
#:    #if 0 == num_Qs and c.isdigit():
#:    if 0 == num_Qs and c == 'A':
#:        #fixed:Y[1-9] --> YA[1-9]
#:        c = _next(it, '<EOF>')
#:        777;sz += 1
#:        if 欤允零:
#:            if not '0' <= c <= '9':raise FormatError('expected:[0-9]', c)
#:        else:
#:            if not '1' <= c <= '9':raise FormatError('expected:[1-9]', c)
#:        u = int(c)
#:    else:
#:        len_sAP = 1+num_Qs
#:        sAP = ''.join(chain(c, islice(it, 0, num_Qs)))
#:        777;sz += num_Qs
#:        if not len(sAP) == len_sAP:
#:            if not len(sAP) < len_sAP:raise 000
#:            raise FormatError('expected:[A-P]', '<EOF>')
#:        len_s09 = 1+_解读冫自然数巛十六进制牜字母扌(sAP)
#:        s09 = ''.join(islice(it, 0, len_s09))
#:        777;sz += len_s09
#:        if not s09.isdigit():raise FormatError('expected:[0-9]', s09)
#:        if not '1' <= s09[0] <= '9':raise FormatError('expected:[1-9]', s09[0])
#:        u = int(s09, 10)
#:    u, sz
#:    return (u, sz, it)
#:
#:
#:encode_int2txt7human7lex_order7alnum_ = 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌
#:xdecode_int5txt7human7lex_order7alnum_ = 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌
#:xdecode_int5iter_chars7human7lex_order7alnum_ = 详解读冫整数巛趃文本表达牜极简牜词典序牜字母数字扌
#:xdecode_uint5iter_chars7human7lex_order7alnum_ = 详解读冫自然数巛趃文本表达牜极简牜词典序牜字母数字扌
#:
#:def decode_int5txt7human7lex_order7alnum_(s, /):
#:    'str -> int'
#:    (i, end) = xdecode_int5txt7human7lex_order7alnum_(s)
#:    if not end == len(s):raise FormatError('extra tailing chars', s[:end], s[end:])
#:    return i
#:def decode_int5iter_chars7human7lex_order7alnum_(chars, /):
#:    'Iter char -> int'
#:    it = iter(chars)
#:    (i, sz, it) = xdecode_int5iter_chars7human7lex_order7alnum_(it)
#:    if (t:=''.join(it)): raise FormatError('extra tailing chars', t)
#:    return i
#:def decode_uint5iter_chars7human7lex_order7alnum_(chars, /):
#:    'Iter char -> uint'
#:    it = iter(chars)
#:    (u, sz, it) = xdecode_uint5iter_chars7human7lex_order7alnum_(it)
#:    if (t:=''.join(it)): raise FormatError('extra tailing chars', t)
#:    return u
#:
#:解读冫整数巛文本表达牜极简牜词典序牜字母数字扌 = decode_int5txt7human7lex_order7alnum_
#:解读冫整数巛趃文本表达牜极简牜词典序牜字母数字扌 = decode_int5iter_chars7human7lex_order7alnum_
#:解读冫自然数巛趃文本表达牜极简牜词典序牜字母数字扌 = decode_uint5iter_chars7human7lex_order7alnum_
#:
#:
#:
#:
#:
#:
#:
#:
#:
#:
#:
#:__all__
#:from seed.int_tools.int_repr7human7lex_order7alnum import FormatError
#:
#:from seed.int_tools.int_repr7human7lex_order7alnum import 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌, 详解读冫整数巛文本表达牜极简牜词典序牜字母数字扌, 详解读冫整数巛趃文本表达牜极简牜词典序牜字母数字扌, 详解读冫自然数巛趃文本表达牜极简牜词典序牜字母数字扌
#:
#:from seed.int_tools.int_repr7human7lex_order7alnum import 表述冫整数讠文本表达牜极简牜词典序牜字母数字扌, 解读冫整数巛文本表达牜极简牜词典序牜字母数字扌, 解读冫整数巛趃文本表达牜极简牜词典序牜字母数字扌, 解读冫自然数巛趃文本表达牜极简牜词典序牜字母数字扌
#:
#:from seed.int_tools.int_repr7human7lex_order7alnum import encode_int2txt7human7lex_order7alnum_, xdecode_int5txt7human7lex_order7alnum_, xdecode_int5iter_chars7human7lex_order7alnum_, xdecode_uint5iter_chars7human7lex_order7alnum_
#:from seed.int_tools.int_repr7human7lex_order7alnum import encode_int2txt7human7lex_order7alnum_, decode_int5txt7human7lex_order7alnum_, decode_int5iter_chars7human7lex_order7alnum_, decode_uint5iter_chars7human7lex_order7alnum_
###########################
###########################
###########################
###########################

__all__
from seed.int_tools.int_repr7human7lex_order7alnum import FormatError

from seed.int_tools.int_repr7human7lex_order7alnum import 表述冫整数讠文本表达牜极简牜词典序牜字母数字牜头胞五扌, 解读冫整数巛文本表达牜极简牜词典序牜字母数字牜头胞五扌, 详解读冫整数巛文本表达牜极简牜词典序牜字母数字牜头胞五扌, 详解读冫整数巛趃文本表达牜极简牜词典序牜字母数字牜头胞五扌
from seed.int_tools.int_repr7human7lex_order7alnum import encode_int2txt7human7lex_order7alnum7headU_, decode_int5txt7human7lex_order7alnum7headU_, xdecode_int5txt7human7lex_order7alnum7headU_, xdecode_int5iter_chars7human7lex_order7alnum7headU_
    # encode_int2txt7human7lex_order7alnum7headU_(int, /, *, validate=True) -> str
    # decode_int5txt7human7lex_order7alnum7headU_(txt, begin=None, end=None, /, *, validate=True) -> int
    # xdecode_int5txt7human7lex_order7alnum7headU_(txt, begin=None, end=None, /, *, validate=True) -> (int, end)
    # xdecode_int5iter_chars7human7lex_order7alnum7headU_(chars) -> (int, num_consumed_chars, iter_remain_chars)
if 1:from seed.int_tools.int_repr7human7lex_order7alnum import _main_

from seed.int_tools.int_repr7human7lex_order7alnum import *
