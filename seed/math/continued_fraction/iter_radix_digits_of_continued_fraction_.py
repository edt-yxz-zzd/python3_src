#__all__:goto
r'''[[[
e ../../python3_src/seed/math/continued_fraction/iter_radix_digits_of_continued_fraction_.py
注意:
    连分数 整数项的负号 不涉及 部分分数项
    浮点数 整数部分的负号 也是 小数部分的负号


py -m seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_
py -m nn_ns.app.debug_cmd   seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_ -x
py -m nn_ns.app.doctest_cmd seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_:__doc__ -ht



[[
py_adhoc_call   seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_   ,20:iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_ =10 '=[1]*100'  +to_chain_integer_part +using_LazyList
===
1
6
1
8
0
3
3
9
8
8
7
4
9
8
9
4
8
4
8
2
]]

[[
py_adhoc_call  { -lineno } seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_  ,iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_   %itertools:repeat   =10 '=repeat(1)'  +to_chain_integer_part +using_LazyList
... ...
98:3
99:7
100:4
101:8
102:4
103:7
104:5
RecursionError: maximum recursion depth exceeded
]]
[[
py_adhoc_call  { -lineno } seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_  ,iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_   %itertools:repeat   =10 '=repeat(1)'  +to_chain_integer_part -using_LazyList
... ...
38:2
39:0
40:3
41:0
42:9
RecursionError: maximum recursion depth exceeded
]]
[[
对照一下上面输出:一致！
py_adhoc_call  { -lineno } seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_  ,110:iter_radix_digits_of_continued_fraction__with_int__via_NDs_   %itertools:repeat   =10 '=repeat(1)'  +to_chain_integer_part
... ...
37:7
38:2
39:0
40:3
41:0
42:9
43:1
44:7
45:9
... ...
91:1
92:8
93:9
94:3
95:9
96:1
97:1
98:3
99:7
100:4
101:8
102:4
103:7
104:5
105:4
106:0
107:8
108:8
109:0
]]
[[
py_adhoc_call  { -lineno } seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_  ,iter_radix_digits_of_continued_fraction__with_int__via_NDs_   %itertools:repeat   =10 '=repeat(1)'  +to_chain_integer_part
... ...
9981:7
9982:2
9983:5
9984:0
9985:9
9986:2
9987:3
9988:1
9989:3
9990:2
9991:7
9992:9
9993:7
9994:7
9995:1
9996:1
9997:3
9998:8
9999:0
10000:3
10001:2
10002:9
10003:4
10004:3
10005:7
10006:6
10007:5
10008:4
10009:7
10010:5
10011:0
10012:9
10013:0
10014:1
10015:6
10016:5
10017:1
10018:6
10019:9
10020:4
10021:9
10022:6
^C KeyboardInterrupt
]]






######################
>>> import seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_ as mmm
>>> _save = mmm._debug__via_NDs

#begin:doctest
######################
>>> from seed.iters.apply_may_args4islice_ import list_islice_, show_islice_, stable_show_islice_, stable_list_islice_
>>> from seed.math.continued_fraction.continued_fraction5ND import iter_continued_fraction_digits5ND_
>>> from fractions import Fraction
>>> from decimal import Decimal

######################
>>> list_islice_(20, iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_(10, repeat(1), to_chain_integer_part=True, using_LazyList=True))
[1, 6, 1, 8, 0, 3, 3, 9, 8, 8, 7, 4, 9, 8, 9, 4, 8, 4, 8, 2]
>>> list_islice_(20, iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_(10, repeat(1), to_chain_integer_part=True, using_LazyList=False))
[1, 6, 1, 8, 0, 3, 3, 9, 8, 8, 7, 4, 9, 8, 9, 4, 8, 4, 8, 2]
>>> (i,it) = iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_(10, repeat(1), to_chain_integer_part=False, using_LazyList=False); i; list_islice_(20, it)
1
[6, 1, 8, 0, 3, 3, 9, 8, 8, 7, 4, 9, 8, 9, 4, 8, 4, 8, 2, 0]


######################
>>> list_islice_(20, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1), to_chain_integer_part=True))
[1, 6, 1, 8, 0, 3, 3, 9, 8, 8, 7, 4, 9, 8, 9, 4, 8, 4, 8, 2]
>>> (i,it) = iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1), to_chain_integer_part=False); i; list_islice_(20, it)
1
[6, 1, 8, 0, 3, 3, 9, 8, 8, 7, 4, 9, 8, 9, 4, 8, 4, 8, 2, 0]


######################
测试冫有理数:有限长小数:
######################
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 0), to_chain_integer_part=True))
Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.ContinuedFractionError__inf__no_cf0
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 1), to_chain_integer_part=True))
[1]
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 2), to_chain_integer_part=True))
[2]
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 3), to_chain_integer_part=True))
[1, 5]
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 5), to_chain_integer_part=True))
[1, 6]
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 6), to_chain_integer_part=True))
[1, 6, 2, 5]


######################
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_(10, repeat(1, 0), to_chain_integer_part=True, using_LazyList=True))
Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.ContinuedFractionError__inf__no_cf0
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_(10, repeat(1, 1), to_chain_integer_part=True, using_LazyList=True))
[1]
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_(10, repeat(1, 2), to_chain_integer_part=True, using_LazyList=True))
[2]
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_(10, repeat(1, 3), to_chain_integer_part=True, using_LazyList=True))
[1, 5]
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_(10, repeat(1, 5), to_chain_integer_part=True, using_LazyList=True))
[1, 6]
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_(10, repeat(1, 6), to_chain_integer_part=True, using_LazyList=True))
[1, 6, 2, 5]




######################
测试冫有理数:循环小数:
######################
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 4), to_chain_integer_part=True))
[1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
>>> list_islice_(31, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 7), to_chain_integer_part=True))
[1, 6, 1, 5, 3, 8, 4, 6, 1, 5, 3, 8, 4, 6, 1, 5, 3, 8, 4, 6, 1, 5, 3, 8, 4, 6, 1, 5, 3, 8, 4]
>>> list_islice_(31, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 8), to_chain_integer_part=True))
[1, 6, 1, 9, 0, 4, 7, 6, 1, 9, 0, 4, 7, 6, 1, 9, 0, 4, 7, 6, 1, 9, 0, 4, 7, 6, 1, 9, 0, 4, 7]

######################
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_(10, repeat(1, 4), to_chain_integer_part=True, using_LazyList=True))
[1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
>>> list_islice_(31, iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_(10, repeat(1, 7), to_chain_integer_part=True, using_LazyList=True))
[1, 6, 1, 5, 3, 8, 4, 6, 1, 5, 3, 8, 4, 6, 1, 5, 3, 8, 4, 6, 1, 5, 3, 8, 4, 6, 1, 5, 3, 8, 4]
>>> list_islice_(31, iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_(10, repeat(1, 8), to_chain_integer_part=True, using_LazyList=True))
[1, 6, 1, 9, 0, 4, 7, 6, 1, 9, 0, 4, 7, 6, 1, 9, 0, 4, 7, 6, 1, 9, 0, 4, 7, 6, 1, 9, 0, 4, 7]







######################
######################
_detail_=True
using_nested_intervals=False
######################
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 1), to_chain_integer_part=True, _detail_=True, using_nested_intervals=False))
[1]
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 2), to_chain_integer_part=True, _detail_=True, using_nested_intervals=False))
[2]

#>>> mmm._debug__via_NDs = True
>>> show_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 3), to_chain_integer_part=True, _detail_=True, using_nested_intervals=False))
1
(False, (0, (0, 1), (1, 1), 1), [])
(False, (0, (1, 1), (1, 2), 2), [])
(True, (0, (1, 2), 2, (1, 2)), [[5], []])

>>> mmm._debug__via_NDs = False
>>> show_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 5), to_chain_integer_part=True, _detail_=True, using_nested_intervals=False))
1
(False, (0, (0, 1), (1, 1), 1), [])
(False, (0, (1, 1), (1, 2), 2), [])
(False, (0, (1, 2), (2, 3), 3), [])
(False, (0, (2, 3), (3, 5), 4), [6])
(True, (1, (3, 5), 4, (0, 5)), [[], []])
>>> show_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 6), to_chain_integer_part=True, _detail_=True, using_nested_intervals=False))
1
(False, (0, (0, 1), (1, 1), 1), [])
(False, (0, (1, 1), (1, 2), 2), [])
(False, (0, (1, 2), (2, 3), 3), [])
(False, (0, (2, 3), (3, 5), 4), [6])
(False, (1, (3, 5), (5, 8), 5), [])
(True, (1, (5, 8), 5, (2, 8)), [[2, 5], []])

######################
>>> show_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 4), to_chain_integer_part=True, _detail_=True, using_nested_intervals=False))
1
(False, (0, (0, 1), (1, 1), 1), [])
(False, (0, (1, 1), (1, 2), 2), [])
(False, (0, (1, 2), (2, 3), 3), [])
(True, (0, (2, 3), 3, (2, 3)), [[], [6]])
>>> show_islice_(31, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 7), to_chain_integer_part=True, _detail_=True, using_nested_intervals=False))
1
(False, (0, (0, 1), (1, 1), 1), [])
(False, (0, (1, 1), (1, 2), 2), [])
(False, (0, (1, 2), (2, 3), 3), [])
(False, (0, (2, 3), (3, 5), 4), [6])
(False, (1, (3, 5), (5, 8), 5), [])
(False, (1, (5, 8), (8, 13), 6), [])
(True, (1, (8, 13), 6, (2, 13)), [[], [1, 5, 3, 8, 4, 6]])
>>> show_islice_(31, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 8), to_chain_integer_part=True, _detail_=True, using_nested_intervals=False))
1
(False, (0, (0, 1), (1, 1), 1), [])
(False, (0, (1, 1), (1, 2), 2), [])
(False, (0, (1, 2), (2, 3), 3), [])
(False, (0, (2, 3), (3, 5), 4), [6])
(False, (1, (3, 5), (5, 8), 5), [])
(False, (1, (5, 8), (8, 13), 6), [])
(False, (1, (8, 13), (13, 21), 7), [1])
(True, (2, (13, 21), 7, (19, 21)), [[], [9, 0, 4, 7, 6, 1]])

######################
>>> show_islice_(20, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1), to_chain_integer_part=True, _detail_=True, using_nested_intervals=False))
1
(False, (0, (0, 1), (1, 1), 1), [])
(False, (0, (1, 1), (1, 2), 2), [])
(False, (0, (1, 2), (2, 3), 3), [])
(False, (0, (2, 3), (3, 5), 4), [6])
(False, (1, (3, 5), (5, 8), 5), [])
(False, (1, (5, 8), (8, 13), 6), [])
(False, (1, (8, 13), (13, 21), 7), [1])
(False, (2, (13, 21), (21, 34), 8), [])
(False, (2, (21, 34), (34, 55), 9), [])
(False, (2, (34, 55), (55, 89), 10), [])
(False, (2, (55, 89), (89, 144), 11), [])
(False, (2, (89, 144), (144, 233), 12), [8, 0])
(False, (4, (144, 233), (233, 377), 13), [])
(False, (4, (233, 377), (377, 610), 14), [3])
(False, (5, (377, 610), (610, 987), 15), [])
(False, (5, (610, 987), (987, 1597), 16), [])
(False, (5, (987, 1597), (1597, 2584), 17), [])
(False, (5, (1597, 2584), (2584, 4181), 18), [])
(False, (5, (2584, 4181), (4181, 6765), 19), [3, 9])






######################
######################
_detail_=True
using_nested_intervals=True
######################
fgrep  '_detail_=True, using_nested_intervals=False' ../../python3_src/seed/math/continued_fraction/iter_radix_digits_of_continued_fraction_.py
######################
#>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 1), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
#>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 2), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
#>>> show_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 3), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
#>>> show_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 5), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
#>>> show_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 6), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
#>>> show_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 4), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
#>>> show_islice_(31, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 7), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
#>>> show_islice_(31, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 8), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
#>>> show_islice_(20, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
######################
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 1), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
[1]
>>> list_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 2), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
[2]
>>> show_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 3), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
1
(False, (0, ((0, 1), (1, 1)), ((0, 1), (1, 1)), 0), [])
(False, (0, ((0, 1), (1, 1)), ((1, 2), (1, 1)), 1), [])
(True, (0, ((1, 2), (1, 1)), ((1, 2), (1, 2)), 2), [[5], []])
>>> show_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 5), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
1
(False, (0, ((0, 1), (1, 1)), ((0, 1), (1, 1)), 0), [])
(False, (0, ((0, 1), (1, 1)), ((1, 2), (1, 1)), 1), [])
(False, (0, ((1, 2), (1, 1)), ((1, 2), (2, 3)), 2), [])
(False, (0, ((1, 2), (2, 3)), ((3, 5), (2, 3)), 3), [6])
(True, (1, ((3, 5), (2, 3)), ((3, 5), (3, 5)), 4), [[], []])
>>> show_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 6), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
1
(False, (0, ((0, 1), (1, 1)), ((0, 1), (1, 1)), 0), [])
(False, (0, ((0, 1), (1, 1)), ((1, 2), (1, 1)), 1), [])
(False, (0, ((1, 2), (1, 1)), ((1, 2), (2, 3)), 2), [])
(False, (0, ((1, 2), (2, 3)), ((3, 5), (2, 3)), 3), [6])
(False, (1, ((3, 5), (2, 3)), ((3, 5), (5, 8)), 4), [])
(True, (1, ((3, 5), (5, 8)), ((5, 8), (5, 8)), 5), [[2, 5], []])
>>> show_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 4), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
1
(False, (0, ((0, 1), (1, 1)), ((0, 1), (1, 1)), 0), [])
(False, (0, ((0, 1), (1, 1)), ((1, 2), (1, 1)), 1), [])
(False, (0, ((1, 2), (1, 1)), ((1, 2), (2, 3)), 2), [])
(True, (0, ((1, 2), (2, 3)), ((2, 3), (2, 3)), 3), [[], [6]])
>>> show_islice_(31, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 7), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
1
(False, (0, ((0, 1), (1, 1)), ((0, 1), (1, 1)), 0), [])
(False, (0, ((0, 1), (1, 1)), ((1, 2), (1, 1)), 1), [])
(False, (0, ((1, 2), (1, 1)), ((1, 2), (2, 3)), 2), [])
(False, (0, ((1, 2), (2, 3)), ((3, 5), (2, 3)), 3), [6])
(False, (1, ((3, 5), (2, 3)), ((3, 5), (5, 8)), 4), [])
(False, (1, ((3, 5), (5, 8)), ((8, 13), (5, 8)), 5), [])
(True, (1, ((8, 13), (5, 8)), ((8, 13), (8, 13)), 6), [[], [1, 5, 3, 8, 4, 6]])
>>> show_islice_(31, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 8), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
1
(False, (0, ((0, 1), (1, 1)), ((0, 1), (1, 1)), 0), [])
(False, (0, ((0, 1), (1, 1)), ((1, 2), (1, 1)), 1), [])
(False, (0, ((1, 2), (1, 1)), ((1, 2), (2, 3)), 2), [])
(False, (0, ((1, 2), (2, 3)), ((3, 5), (2, 3)), 3), [6])
(False, (1, ((3, 5), (2, 3)), ((3, 5), (5, 8)), 4), [])
(False, (1, ((3, 5), (5, 8)), ((8, 13), (5, 8)), 5), [])
(False, (1, ((8, 13), (5, 8)), ((8, 13), (13, 21)), 6), [1])
(True, (2, ((8, 13), (13, 21)), ((13, 21), (13, 21)), 7), [[], [9, 0, 4, 7, 6, 1]])
>>> show_islice_(20, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1), to_chain_integer_part=True, _detail_=True, using_nested_intervals=True))
1
(False, (0, ((0, 1), (1, 1)), ((0, 1), (1, 1)), 0), [])
(False, (0, ((0, 1), (1, 1)), ((1, 2), (1, 1)), 1), [])
(False, (0, ((1, 2), (1, 1)), ((1, 2), (2, 3)), 2), [])
(False, (0, ((1, 2), (2, 3)), ((3, 5), (2, 3)), 3), [6])
(False, (1, ((3, 5), (2, 3)), ((3, 5), (5, 8)), 4), [])
(False, (1, ((3, 5), (5, 8)), ((8, 13), (5, 8)), 5), [])
(False, (1, ((8, 13), (5, 8)), ((8, 13), (13, 21)), 6), [1])
(False, (2, ((8, 13), (13, 21)), ((21, 34), (13, 21)), 7), [])
(False, (2, ((21, 34), (13, 21)), ((21, 34), (34, 55)), 8), [])
(False, (2, ((21, 34), (34, 55)), ((55, 89), (34, 55)), 9), [])
(False, (2, ((55, 89), (34, 55)), ((55, 89), (89, 144)), 10), [])
(False, (2, ((55, 89), (89, 144)), ((144, 233), (89, 144)), 11), [8, 0])
(False, (4, ((144, 233), (89, 144)), ((144, 233), (233, 377)), 12), [])
(False, (4, ((144, 233), (233, 377)), ((377, 610), (233, 377)), 13), [3])
(False, (5, ((377, 610), (233, 377)), ((377, 610), (610, 987)), 14), [])
(False, (5, ((377, 610), (610, 987)), ((987, 1597), (610, 987)), 15), [])
(False, (5, ((987, 1597), (610, 987)), ((987, 1597), (1597, 2584)), 16), [])
(False, (5, ((987, 1597), (1597, 2584)), ((2584, 4181), (1597, 2584)), 17), [])
(False, (5, ((2584, 4181), (1597, 2584)), ((2584, 4181), (4181, 6765)), 18), [3, 9])








######################
######################
######################
def iter_fraction_part_radix_digits_of_ND__ge0_lt1_(radix, ND, /, *, _detail_=False):
######################
>>> [*iter_fraction_part_radix_digits_of_ND__ge0_lt1_(10, (0, 5))]
[]
>>> [*iter_fraction_part_radix_digits_of_ND__ge0_lt1_(10, (0, 5), _detail_=True)]
[[], []]

>>> [*iter_fraction_part_radix_digits_of_ND__ge0_lt1_(10, (2, 5))]
[4]
>>> [*iter_fraction_part_radix_digits_of_ND__ge0_lt1_(10, (2, 5), _detail_=True)]
[[4], []]

>>> [*iter_fraction_part_radix_digits_of_ND__ge0_lt1_(10, (1, 12500))]
[0, 0, 0, 0, 8]
>>> [*iter_fraction_part_radix_digits_of_ND__ge0_lt1_(10, (1, 12500), _detail_=True)]
[[0, 0, 0, 0, 8], []]

>>> [*iter_fraction_part_radix_digits_of_ND__ge0_lt1_(10, (5, 12500))]
[0, 0, 0, 4]
>>> [*iter_fraction_part_radix_digits_of_ND__ge0_lt1_(10, (5, 12500), _detail_=True)]
[[0, 0, 0, 4], []]

>>> [*iter_fraction_part_radix_digits_of_ND__ge0_lt1_(10, (20, 12500))]
[0, 0, 1, 6]
>>> [*iter_fraction_part_radix_digits_of_ND__ge0_lt1_(10, (20, 12500), _detail_=True)]
[[0, 0, 1, 6], []]

######################
>>> list_islice_(5, iter_fraction_part_radix_digits_of_ND__ge0_lt1_(10, (1, 3)))
[3, 3, 3, 3, 3]
>>> [*iter_fraction_part_radix_digits_of_ND__ge0_lt1_(10, (1, 3), _detail_=True)]
[[], [3]]

>>> list_islice_(20, iter_fraction_part_radix_digits_of_ND__ge0_lt1_(10, (3, 7)))
[4, 2, 8, 5, 7, 1, 4, 2, 8, 5, 7, 1, 4, 2, 8, 5, 7, 1, 4, 2]
>>> [*iter_fraction_part_radix_digits_of_ND__ge0_lt1_(10, (3, 7), _detail_=True)]
[[], [4, 2, 8, 5, 7, 1]]

>>> list_islice_(20, iter_fraction_part_radix_digits_of_ND__ge0_lt1_(10, (2,35)))
[0, 5, 7, 1, 4, 2, 8, 5, 7, 1, 4, 2, 8, 5, 7, 1, 4, 2, 8, 5]
>>> [*iter_fraction_part_radix_digits_of_ND__ge0_lt1_(10, (2, 35), _detail_=True)]
[[0], [5, 7, 1, 4, 2, 8]]






######################
######################
radix_repr5continued_fraction_
######################
#>>> mmm._debug__via_NDs = True
>>> radix_repr5continued_fraction_(10, [0], imay_max_num_digits_after_dot=-1)
'0'
>>> radix_repr5continued_fraction_(10, [0, 1], imay_max_num_digits_after_dot=-1)
'1'
>>> radix_repr5continued_fraction_(10, [0, 1, 1], imay_max_num_digits_after_dot=-1)
'0.5'
>>> radix_repr5continued_fraction_(10, [-567], imay_max_num_digits_after_dot=-1)
'-567'
>>> radix_repr5continued_fraction_(10, [-567, 1], imay_max_num_digits_after_dot=-1) # == -566 != -568
'-566'
>>> radix_repr5continued_fraction_(10, [-567, 1, 1], imay_max_num_digits_after_dot=-1) # == -566.5 != -567.5
'-566.5'
>>> [*iter_continued_fraction_digits5ND_(*Decimal('-566.5').as_integer_ratio())] # == cf[-567, 1, 1] == cf[-567, 2]
[-567, 2]
>>> radix_repr5continued_fraction_(10, [+567], imay_max_num_digits_after_dot=-1)
'567'
>>> radix_repr5continued_fraction_(10, [+567, 1], imay_max_num_digits_after_dot=-1)
'568'
>>> radix_repr5continued_fraction_(10, [+567, 1, 1], imay_max_num_digits_after_dot=-1)
'567.5'
>>> radix_repr5continued_fraction_(10, [+567]+[1]*20, imay_max_num_digits_after_dot=30)
'567.618033985017357938973140873378'
>>> radix_repr5continued_fraction_(10, [+567]+[1]*20, imay_max_num_digits_after_dot=3)
'567.618'
>>> radix_repr5continued_fraction_(10, repeat(1), imay_max_num_digits_after_dot=60)
'1.618033988749894848204586834365638117720309179805762862135448'

>>> gr = Decimal('1.618033988749894848204586834365638117720309179805762862135448')
>>> gr
Decimal('1.618033988749894848204586834365638117720309179805762862135448')
>>> gr.as_integer_ratio()
(202254248593736856025573354295704764715038647475720357766931, 125000000000000000000000000000000000000000000000000000000000)
>>> Fraction(gr)*10**60
Fraction(1618033988749894848204586834365638117720309179805762862135448, 1)
>>> gr*10**60
Decimal('1.618033988749894848204586834E+60')
>>> [*iter_continued_fraction_digits5ND_(*gr.as_integer_ratio())]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 17, 2, 15, 4, 3, 3, 1, 201, 1, 6, 1, 1, 19, 39, 8, 3, 4, 2, 119, 1, 2, 1, 1, 3, 4, 2, 4, 1, 1, 1, 2, 1, 1, 3, 2, 23, 2, 1, 48, 10, 1, 1, 6, 3, 1, 13, 1, 11]


>>> radix_repr5continued_fraction_(16, repeat(1), imay_max_num_digits_after_dot=60)
'1.9E3779B97F4A7C15F39CC0605CEDC8341082276BF3A27251F86C6A11D0C1'
>>> radix_repr5continued_fraction_(8, repeat(1), imay_max_num_digits_after_dot=60)
'1.474335715627751237012763471401402716671015010202116657635047'
>>> radix_repr5continued_fraction_(2, repeat(1), imay_max_num_digits_after_dot=60)
'1.100111100011011101111001101110010111111101001010011111000001'
>>> radix_repr5continued_fraction_(3, repeat(1), imay_max_num_digits_after_dot=60)
'1.121200112202121020010210010200102011221021200221110110010122'
>>> radix_repr5continued_fraction_(5, repeat(1), imay_max_num_digits_after_dot=60)
'1.302111342304120242231443114020402121110331330400402410223011'
>>> radix_repr5continued_fraction_(7, repeat(1), imay_max_num_digits_after_dot=60)
'1.421662036460160355141642042205102413441305131454206544260612'
>>> radix_repr5continued_fraction_(9, repeat(1), imay_max_num_digits_after_dot=60)
'1.550482536123120364837627413118462307016748680673830312448203'
>>> radix_repr5continued_fraction_(11, repeat(1), imay_max_num_digits_after_dot=60)
'1.68866AA0280681233206443625A00288521091655189588A182339047047'


>>> radix_repr5continued_fraction_(10, [-2], imay_max_num_digits_after_dot=15)
'-2'
>>> radix_repr5continued_fraction_(10, [-2,1], imay_max_num_digits_after_dot=15)
'-1'
>>> radix_repr5continued_fraction_(10, [-2,1,1], imay_max_num_digits_after_dot=15)
'-1.5'
>>> radix_repr5continued_fraction_(10, [-2,1,1,1], imay_max_num_digits_after_dot=15)
'-1.333333333333333'
>>> radix_repr5continued_fraction_(10, [-1], imay_max_num_digits_after_dot=15)
'-1'
>>> radix_repr5continued_fraction_(10, [-1,1], imay_max_num_digits_after_dot=15)
'0'
>>> radix_repr5continued_fraction_(10, [-1,1,1], imay_max_num_digits_after_dot=15)
'-0.5'
>>> radix_repr5continued_fraction_(10, [-1,1,1,1], imay_max_num_digits_after_dot=15)
'-0.333333333333333'
>>> radix_repr5continued_fraction_(10, [0,1,1,1], imay_max_num_digits_after_dot=15)
'0.666666666666666'
>>> radix_repr5continued_fraction_(10, chain([-1],repeat(1)), imay_max_num_digits_after_dot=60)
'-0.381966011250105151795413165634361882279690820194237137864551'
>>> gr = Decimal('-0.381966011250105151795413165634361882279690820194237137864551')
>>> [*iter_continued_fraction_digits5ND_(*gr.as_integer_ratio())]
[-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 7, 6, 1, 11, 1, 1, 5, 3, 2, 4, 1, 2, 24, 3, 1, 26, 1, 1, 2, 3, 6, 2, 4, 4, 1, 1, 5, 1, 1, 1, 1, 8, 1, 3, 1, 18, 9, 62, 1, 2, 24, 2, 1, 1, 1, 1, 4, 1, 10, 23, 1, 27, 1, 1, 4]
>>> radix_repr5continued_fraction_(16, chain([-1],repeat(1)), imay_max_num_digits_after_dot=60)
'-0.61C8864680B583EA0C633F9FA31237CBEF7DD8940C5D8DAE079395EE2F3E'
>>> [*iter_continued_fraction_digits5ND_(-0x61C8864680B583EA0C633F9FA31237CBEF7DD8940C5D8DAE079395EE2F3E, 16**60)]
[-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 23, 4, 2, 1, 1, 2, 1, 20, 8, 1, 29, 3, 1, 57, 1, 2, 2, 2, 447, 5, 3, 1, 9, 1, 1, 2, 3158, 10, 2, 15, 2, 4, 4, 1, 1, 5, 1, 1, 1, 1, 5, 44, 1, 2, 1, 3, 1, 7, 3, 11, 11, 1, 1, 1, 8, 1, 5]





















######################
:testing:
iter_fraction_part_radix_digits_of_limit_of_nested_intervals__ND_repr__ge0_lt1_
truncated_continued_fraction2truncated_radix_digits_with_int_
truncated_continued_fraction5truncated_radix_digits_with_int_
######################
>>> def str2decimal_radix_digits_with_int_(s, /):
...     s4i,_,s4fr = s.partition('.')
...     if s4i[0] == '-':
...         sign = -1
...         s4u = s4i[1:]
...     elif s4i[0] == '+':
...         sign = +1
...         s4u = s4i[1:]
...     elif s4i == '0' and s4fr == '0'*len(s4fr):
...         sign = 0
...         s4u = s4i
...     else:
...         sign = +1
...         s4u = s4i
...     sign, s4u
...     uint_part = int(s4u, 10)
...     integer_part = (sign, uint_part)
...     fraction_part = map(int, s4fr)
...     t_rd = [integer_part, *fraction_part]
...     return t_rd

>>> radix_repr5continued_fraction_(10, repeat(1), imay_max_num_digits_after_dot=60)
'1.618033988749894848204586834365638117720309179805762862135448'
>>> t_rd = str2decimal_radix_digits_with_int_('1.618033988749894848204586834365638117720309179805762862135448')
>>> t_rd
[(1, 1), 6, 1, 8, 0, 3, 3, 9, 8, 8, 7, 4, 9, 8, 9, 4, 8, 4, 8, 2, 0, 4, 5, 8, 6, 8, 3, 4, 3, 6, 5, 6, 3, 8, 1, 1, 7, 7, 2, 0, 3, 0, 9, 1, 7, 9, 8, 0, 5, 7, 6, 2, 8, 6, 2, 1, 3, 5, 4, 4, 8]
>>> t_cf = truncated_continued_fraction5truncated_radix_digits_with_int_(10, t_rd, raise_vs_return_empty=True)
>>> t_cf == [1]*143
True
>>> t_rd2 = truncated_continued_fraction2truncated_radix_digits_with_int_(10, t_cf, raise_vs_return_empty=True)
>>> t_rd2
[(1, 1), 6, 1, 8, 0, 3, 3, 9, 8, 8, 7, 4, 9, 8, 9, 4, 8, 4, 8, 2, 0, 4, 5, 8, 6, 8, 3, 4, 3, 6, 5, 6, 3, 8, 1, 1, 7, 7, 2, 0, 3, 0, 9, 1, 7, 9, 8, 0, 5, 7, 6, 2, 8, 6, 2, 1, 3, 5, 4]
>>> t_rd2 == t_rd[:len(t_rd2)]
True
>>> while t_rd:
...     t_cf = truncated_continued_fraction5truncated_radix_digits_with_int_(10, t_rd, raise_vs_return_empty=True)
...     assert t_cf == [1]*len(t_cf)
...     t_rd2 = truncated_continued_fraction2truncated_radix_digits_with_int_(10, t_cf, raise_vs_return_empty=True)
...     assert t_rd2 == t_rd[:len(t_rd2)]
...     print(len(t_rd), len(t_cf), len(t_rd2))
...     t_rd = t_rd2
61 143 59
59 139 58
58 136 57
57 134 56
56 132 55
55 130 54
54 126 52
52 123 51
51 120 50
50 117 49
49 115 48
48 113 46
46 107 44
44 103 42
42 99 40
40 94 38
38 88 36
36 83 34
34 78 32
32 74 31
31 72 30
30 69 29
29 67 28
28 64 27
27 62 26
26 60 24
24 55 23
23 53 22
22 50 21
21 48 19
19 44 18
18 41 17
17 38 15
15 34 13
13 29 11
11 24 10
10 21 8
8 17 6
6 12 5
5 10 3
3 5 2
2 2 0





>>> radix_repr5continued_fraction_(10, chain([-1], repeat(1)), imay_max_num_digits_after_dot=60)
'-0.381966011250105151795413165634361882279690820194237137864551'
>>> t_rd = str2decimal_radix_digits_with_int_('-0.381966011250105151795413165634361882279690820194237137864551')
>>> t_rd
[(-1, 0), 3, 8, 1, 9, 6, 6, 0, 1, 1, 2, 5, 0, 1, 0, 5, 1, 5, 1, 7, 9, 5, 4, 1, 3, 1, 6, 5, 6, 3, 4, 3, 6, 1, 8, 8, 2, 2, 7, 9, 6, 9, 0, 8, 2, 0, 1, 9, 4, 2, 3, 7, 1, 3, 7, 8, 6, 4, 5, 5, 1]
>>> t_cf = truncated_continued_fraction5truncated_radix_digits_with_int_(10, t_rd, raise_vs_return_empty=True)
>>> len(t_cf)
143
>>> t_cf == [-1]+[1]*142
True
>>> t_rd2 = truncated_continued_fraction2truncated_radix_digits_with_int_(10, t_cf, raise_vs_return_empty=True)
>>> t_rd2
[(-1, 0), 3, 8, 1, 9, 6, 6, 0, 1, 1, 2, 5, 0, 1, 0, 5, 1, 5, 1, 7, 9, 5, 4, 1, 3, 1, 6, 5, 6, 3, 4, 3, 6, 1, 8, 8, 2, 2, 7, 9, 6, 9, 0, 8, 2, 0, 1, 9, 4, 2, 3, 7, 1, 3, 7, 8, 6, 4, 5]
>>> t_rd2 == t_rd[:len(t_rd2)]
True
>>> while t_rd:
...     t_cf = truncated_continued_fraction5truncated_radix_digits_with_int_(10, t_rd, raise_vs_return_empty=True)
...     assert t_cf == [*islice(chain([-1], repeat(1)), len(t_cf))]
...     t_rd2 = truncated_continued_fraction2truncated_radix_digits_with_int_(10, t_cf, raise_vs_return_empty=True)
...     assert t_rd2 == t_rd[:len(t_rd2)]
...     print(len(t_rd), len(t_cf), len(t_rd2))
...     t_rd = t_rd2
61 143 59
59 139 58
58 136 57
57 134 56
56 132 55
55 130 54
54 126 52
52 123 51
51 120 50
50 117 49
49 115 48
48 113 46
46 107 44
44 103 42
42 99 40
40 94 38
38 88 36
36 83 34
34 78 32
32 74 31
31 72 30
30 69 29
29 67 28
28 64 27
27 62 26
26 60 24
24 55 23
23 53 22
22 50 21
21 48 19
19 44 18
18 41 17
17 38 15
15 34 13
13 29 11
11 24 10
10 21 8
8 17 6
6 12 5
5 10 3
3 5 1
1 1 0



######################
######################
######################
#end:doctest
>>> mmm._debug__via_NDs = _save

######################
#]]]'''
__all__ = r'''
radix_repr5continued_fraction_
iter_radix_digits_of_continued_fraction__with_int__via_NDs_












radix_repr5continued_fraction_
    mk_formatter4fixed_point_fractional
        alphabet_09AZ
        i2sign_digits_pair_
i5sign_digits_pair_



iter_radix_digits_of_continued_fraction__with_int__via_NDs_
    iter_fraction_part_radix_digits_of_limit_of_NDs__alter_side__ge0_lt1_
        数据错误
        iter_common_parts_of_
        iter_fraction_part_radix_digits_of_ND__ge0_lt1_


数据错误
    数据错误牜序列冫空
    数据错误牜区间套冫非嵌套
    数据错误牜渐近序列冫非左右互换夹逼





check_radix_
    check_ND_
    check_ND__ge0_lt1_
check_interval_
    check_interval_nested_in_
check_integer_part_
    check_sign_
    check_uint_part_



iter_fraction_part_radix_digits_of_limit_of_nested_intervals__ND_repr__ge0_lt1_
    cmp__ND_




Fail4REPR
RadixRepr_Empty
truncated_continued_fraction2truncated_radix_digits_with_int_
truncated_continued_fraction5truncated_radix_digits_with_int_
    i5sign_digits_pair_












iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_
'''.split()#'''
    #RecursionError:iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_
__all__

from seed.math.continued_fraction.continued_fraction_ops import cf_neg, cf_cmp_, cf_sub, cf_floor_ex_, CachedIterator# to_PeekableIterator
from seed.math.continued_fraction.continued_fraction_fold import iter_approximate_fraction_NDs5continued_fraction_, ContinuedFractionError__inf__no_cf0
from seed.tiny_.check import check_type_is, check_int_ge, check_int_ge_lt
from seed.tiny_.check import check_pair
from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
from seed.math.gcd import gcd_ex
from seed.tiny import null_iter
from seed.math.continued_fraction.continued_fraction_ops import ContinuedFraction as CF__original
from seed.math.continued_fraction.continued_fraction_ops____using_LazyList import ContinuedFraction as CF__using_LazyList
from seed.math.sign_of import sign_of
from seed.tiny import print_err
from seed.math.continued_fraction.continued_fraction_fold import calc_ND5finite_continued_fraction_
from seed.math.continued_fraction.continued_fraction5ND import iter_continued_fraction_digits5ND_

import math
from itertools import repeat, chain, islice
def check_radix_(radix, /):
    check_int_ge(2, radix)
def check_ND_(ND, /, *, ge0_le1=False):
    check_pair(ND)
    (N,D) = ND
    if not ge0_le1:
        check_type_is(int, N)
        check_int_ge(1, D)
    else:
        check_int_ge(0, N)
        check_int_ge(N, D)
def check_ND__ge0_lt1_(ND, /):
    '[0 <= N < D]'
    check_pair(ND)
    (N,D) = ND
    check_int_ge(0, N)
    check_int_ge(N+1, D)

def iter_fraction_part_radix_digits_of_ND__ge0_lt1_(radix, ND, /, *, _detail_=False):
    '-> fraction_part/radix_digits<radix>/Iter uint%radix if not _detail_ else iter[nonloop_digits, loop_digits]'
    if _detail_:
        nonloop_digits = []
    check_radix_(radix)
    check_ND__ge0_lt1_(ND)
    # [0 <= N < D]
    (N,D) = ND
    (N_g, g, D_g) = gcd_ex(N,D)
    # [gcd(N_g, D_g) == 1]
    # [0 <= N_g < D_g]
    # [[N_g==0] <-> [D_g==1]]
    (N,D) = N_g, D_g
    # [gcd(N, D) == 1]
    # [0 <= N < D]
    # [[N==0] <-> [D==1]]
    (e4D, _D) = factor_pint_out_power_of_base_(radix, D)
    # [gcd(N, _D) == 1]
    if N and e4D:
        q, r = divmod(N, _D)
        # [gcd(r, _D) == 1]
        # [0 <= r < _D]
        # [[r==0] <-> [_D==1]]
        #   eg: [(r,_D) == (0,1)]
        ######################
        # [N/D == (q*_D+r)/_D/radix**e4D == (q+r/_D)/radix**e4D]
        reversed_digits = []
        q_ = q
        for _ in range(e4D):
            q_, digit = divmod(q_, radix)
            reversed_digits.append(digit)
        digits = reversed(reversed_digits)
        if _detail_:
            nonloop_digits.extend(digits)
        else:
            yield from digits
        ######################
        D = _D
        N = r
        # [gcd(N, D) == 1]
        # [0 <= N < D]
        # [[N==0] <-> [D==1]]
        ######################
        (e4D, _D) = factor_pint_out_power_of_base_(radix, D)
    assert e4D == 0


    # [gcd(N, D) == 1]
    # [0 <= N < D]
    # [[N==0] <-> [D==1]]
    known_coprime_R_Dge2 = False
        # [[known_coprime_R_Dge2] -> [[D >=2][gcd(radix,D)==1]]]
    (radix_g, g) = (1, radix)
    # [gcd(radix_g, D) == 1]
    # [(radix_g*g) == radix]
    while N:
        # [gcd(radix_g, D) == 1]
        # [(radix_g*g) == radix]
        # [gcd(N, D) == 1]
        # [1 <= N < D]
        assert 1 <= N < D
        # [(new_digit, new_N~/D) := N*radix%/D]
        if not known_coprime_R_Dge2:
            #(radix_g, g, D_g) = gcd_ex(radix,D)
            # !! [gcd(radix_g, D) == 1]
            # !! [(old_radix_g*old_g) == radix]
            # [new_g == gcd(radix,D) == gcd(old_radix_g*old_g,D) == gcd(old_g,D)]
            # [g_g := old_g/new_g]
            # [new_radix_g := old_radix_g*g_g]
            # [new_radix_g*new_g == (old_radix_g*g_g)*(old_g/g_g) == old_radix_g*old_g == radix]
            # [new_radix_g*new_g == radix]
            (g_g, g, D_g) = gcd_ex(g,D)
            radix_g *= g_g
            # [gcd(radix_g, D_g) == 1]
            # [radix_g*g == radix]
            if g == 1 and D > 1:
                # [(radix_g, g, D_g) == (radix,1,D)]
                # [gcd(radix, D) == 1]
                # [D > 1]
                known_coprime_R_Dge2 = True
                    # [[known_coprime_R_Dge2] -> [[D >=2][gcd(radix,D)==1]]]
                if _detail_:
                    N0 = N
                    loop_digits = []
                    yield nonloop_digits
                assert (radix_g, g, D_g) == (radix,1,D)
        else:
            # [(radix_g, g, D_g) == (radix,1,D)]
            # [gcd(radix, D) == 1]
            # [radix_g*g == radix]
            # ==>>:
            # [gcd(radix_g, D_g) == 1]
            # [radix_g*g == radix]
            #
            pass
        # [radix_g*g == radix]
        # [gcd(radix_g, D_g) == 1]
        # !! [gcd(N, D) == 1]
        # [gcd(N, D_g) == 1]
        # [gcd(N*radix_g, D_g) == 1]
        #
        # [(new_digit, new_N~/D_g) := N*radix_g%/D_g]
        (digit, r) = divmod(N*radix_g, D_g)
        # [gcd(r, D_g) == 1]
        # [0 <= r < D_g]
        # [[r==0] <-> [D_g==1]]
        if _detail_:
            if not known_coprime_R_Dge2:
                nonloop_digits.append(digit)
            else:
                #yield (False, (N, D, r), digit)
                loop_digits.append(digit)
                if r == N0:
                    #yield (True, loop_digits)
                    yield loop_digits
                    break
        else:
            yield digit
        N = r
        D = D_g
        # [gcd(radix_g, D) == 1]
        # [(radix_g*g) == radix]
        # [gcd(N, D) == 1]
        # [0 <= N < D]
        # [[N==0] <-> [D==1]]
    # [[N==0] <-> [D==1]]
    assert N == 0 or (_detail_ and known_coprime_R_Dge2 and loop_digits and r==N0)

    if N == 0:
        assert D == 1
        assert not known_coprime_R_Dge2
        if _detail_:
            loop_digits = []
            yield nonloop_digits
            yield loop_digits

    return
def iter_common_parts_of_(lhs, rhs, /):
    for (a, b) in zip(lhs, rhs):
        if not a == b:break
        yield a

class 数据错误(Exception):pass
class 数据错误牜序列冫空(数据错误):pass
class 数据错误牜区间套冫非嵌套(数据错误):pass
class 数据错误牜渐近序列冫非左右互换夹逼(数据错误):pass
def cmp__ND_(prev_ND, ND, /):
    '-> -1|0|+1'
    if prev_ND == ND:
        return 0
    A,B = prev_ND
    C,D = ND
    rc = sign_of(A*D-C*B)
    return rc
def check_interval_(interval, /, *, ge0_le1=False):
    check_pair(interval)
    (lND, rND) = interval
    check_ND_(lND, ge0_le1=ge0_le1)
    check_ND_(rND, ge0_le1=ge0_le1)
    if +1 == cmp__ND_(lND, rND):raise TypeError
def check_interval_nested_in_(prev_interval, interval, /):
    (prev_lND, prev_rND) = prev_interval
    (lND, rND) = interval
    if +1 == cmp__ND_(prev_lND, lND):raise TypeError
    if +1 == cmp__ND_(rND, prev_rND):raise TypeError
def iter_fraction_part_radix_digits_of_limit_of_nested_intervals__ND_repr__ge0_lt1_(radix, ND_pairs8nested_intervals, /, *, _detail_=False):
    '-> fraction_part/radix_digits<radix>/Iter uint%radix |^数据错误牜区间套冫非嵌套'
    # 后置条件:『0.ddd』只输出小数点后的数字『ddd』，即不含整数『0.』
    #
    # 前置条件:区间套(ND_pairs8nested_intervals)前面区间包含后面区间，即嵌套
    # 前置条件:区间套夹逼极限存在#否则卡壳在某一位置造成死循环
    # 前置条件:[0<=区间套夹逼极限<1] # 但[0<=N/D<=1]即允许部分[N/D==1]
    # xxx:前置条件:[区间套非空] #即使是整数0,也该有[区间套~==~[((0,1),(0,1))]] |^数据错误牜序列冫空
    #
    ######################
    def adjust(st, ND, /):
        # [new_N/new_D := (N/D)*radix**num_yielded_digits -yielded_part]
        # [new_N := (N*radix**num_yielded_digits)%D]
        # [new_D := D]
        (num_yielded_digits) = st
        (N,D) = ND
        [new_N := (N*pow(radix,num_yielded_digits,D))%D]
        [new_D := D]
        adjusted_ND = (new_N, new_D)
        if 0b001:
            A,B = adjusted_ND
            if not 0 <= A <= B: raise 数据错误牜区间套冫非嵌套
        return adjusted_ND
    def f(st, prev_ND, ND, /):
        adjusted_prev_ND = adjust(st, prev_ND)
        adjusted_ND = adjust(st, ND)
        (num_yielded_digits) = st
        it0 = iter_fraction_part_radix_digits_of_ND__ge0_lt1_(radix, adjusted_prev_ND)
        is_exact = prev_ND == ND
        if is_exact:
            it = it0
            # ["it" may be infinite long]
            if _detail_:
                last_ND = prev_ND
                adjusted_last_ND = adjusted_prev_ND
                it = iter_fraction_part_radix_digits_of_ND__ge0_lt1_(radix, adjusted_last_ND, _detail_=_detail_)
                # ["it" is finite long]
                digits = [*it]
            else:

                digits = it
            digits
            # ["digits" may be infinite long]
            st
        else:
            it1 = iter_fraction_part_radix_digits_of_ND__ge0_lt1_(radix, adjusted_ND)
            it = iter_common_parts_of_(it0, it1)
            # ["it" is finite long]
            digits = [*it]
            num_yielded_digits += len(digits)
            st = num_yielded_digits
        return (st, digits, is_exact)
            # ["digits" may be infinite long]
    ######################
    def main():
        check_radix_(radix)
        prev_interval = ((0,1), (1,1))
        num_yielded_digits = 0
        st = num_yielded_digits
        it_ps = iter(ND_pairs8nested_intervals)
        for j4interval, interval in enumerate(it_ps):
            check_interval_(interval, ge0_le1=True)
            check_interval_nested_in_(prev_interval, interval)
                # ^数据错误牜区间套冫非嵌套
            if _detail_:
                _num_yielded_digits = st
            ######################
            (st, digits, is_exact) = f(st, *interval)
            # ["digits" may be infinite long]
            if 0b000:print_err(j4interval, interval, digits)
            ######################
            if _detail_:
                #yield '!!!'
                yield (is_exact, (_num_yielded_digits, prev_interval, interval, j4interval), digits)
            else:
                yield from digits
            if is_exact:
                (_j4interval, _interval) = (j4interval, interval)
                for _j4interval, _interval in enumerate(it_ps, j4interval+1):
                    if not interval == _interval:raise 000
                if _detail_ and not _j4interval == j4interval:
                    yield (..., (_num_yielded_digits, prev_interval, interval, j4interval, _j4interval, _interval))
                break
            prev_interval = interval
        return
        if 0b001:input('xxx')
        if 0b001:quit()
    ######################
    return main()
    ######################
_using_nested_intervals = True
def iter_fraction_part_radix_digits_of_limit_of_NDs__alter_side__ge0_lt1_(radix, NDs, /, *, _detail_=False, using_nested_intervals=_using_nested_intervals):
  ''\
    '-> fraction_part/radix_digits<radix>/Iter uint%radix |^数据错误牜序列冫空 |^数据错误牜区间套冫非嵌套 |^数据错误牜渐近序列冫非左右互换夹逼'
    # 后置条件:『0.ddd』只输出小数点后的数字『ddd』，即不含整数『0.』
    #
    # 前置条件:NDs左右互换夹逼#rc正负符号交替
    # 前置条件:NDs夹逼极限存在#否则卡壳在某一位置造成死循环
    # 前置条件:[0<=NDs夹逼极限<1] # 但[0<=N/D<=1]即允许部分[N/D==1]
    # 前置条件:[NDs非空] #即使是整数0,也该有[NDs~==~[0]]
    #
    #
######################
  def ask_(s, /):
    while 1:
        r = input(s)
        if not r:
            r = 'y'
        #
        if len(r) == 1:
            r = r.lower()
            if r in 'ny':break
    return bool('ny'.index(r))
######################
  def adjust(st, ND, j4ND, /):
    # [new_N/new_D := (N/D)*radix**num_yielded_digits -yielded_part]
    # [new_N := (N*radix**num_yielded_digits)%D]
    # [new_D := D]
    (num_yielded_digits) = st
    (N,D) = ND
    [new_N := (N*pow(radix,num_yielded_digits,D))%D]
    [new_D := D]
    adjusted_ND = (new_N, new_D)
    if 0b001:
        A,B = adjusted_ND
        if not 0 <= A <= B: raise 数据错误牜区间套冫非嵌套
    if 0b000:
        A,B = adjusted_ND
        #assert 1 <= A < B or 0 == A < B == 1, (A, B)
        if not 1 <= A < B:
            # (0,1), (1,1): 来源于截断: cf[:1], cf[:2] where cf:=[0;1,...]
            # 10:(3,5) => 3/5=0.6, adjusted_ND=(0,5)
            print_err('not in (0<..<1): adjusted_ND=', adjusted_ND, 'j4ND=', j4ND, 'ND=', ND)
            if not ask_('continue? (y/n):'): raise KeyboardInterrupt
    return adjusted_ND
######################
  def _obsolete__adjust(st, ND, j4ND, /):
    (yielded_part, num_yielded_digits) = st
    (N,D) = ND
    new_N = N*radix**num_yielded_digits -D*yielded_part
    raise 000
######################
  def f(st, prev_ND, ND, j4ND, /):
    adjusted_prev_ND = adjust(st, prev_ND, j4ND-1)
    adjusted_ND = adjust(st, ND, j4ND)
    (num_yielded_digits) = st
    it0 = iter_fraction_part_radix_digits_of_ND__ge0_lt1_(radix, adjusted_prev_ND)
    it1 = iter_fraction_part_radix_digits_of_ND__ge0_lt1_(radix, adjusted_ND)
    it = iter_common_parts_of_(it0, it1)
    digits = [*it]
    num_yielded_digits += len(digits)
    st = num_yielded_digits
    return (st, digits)
######################
  def _cmp_(prev_ND, ND, /):
    '-> -1|+1'
    A,B = prev_ND
    C,D = ND
    if 0:
        #bug:not adjusted_ND
        assert 1 <= A < B or 0 == A < B == 1, (A, B)
            #第一项 可能是 (0,1)
        assert 1 <= C < D, (C, D)
    rc = sign_of(A*D-C*B)
    return rc
######################
  def cmp(may_prev_rc, prev_ND, ND, /):
    '-> -1|+1|^数据错误牜渐近序列冫非左右互换夹逼'
    rc = _cmp_(prev_ND, ND)
    assert abs(rc) == 1
    if rc == may_prev_rc:
        raise 数据错误牜渐近序列冫非左右互换夹逼
    return rc

######################
  def main(NDs=NDs, /):
    check_radix_(radix)
    NDs = iter(NDs)
    for j4ND, ND in enumerate(NDs, 0):
        break
    else:
        raise 数据错误牜序列冫空
    if using_nested_intervals:
        return _2_main(ND, j4ND, NDs)
    return _1_main(ND, j4ND, NDs)
######################
  def iter_intervals_(ND, j4ND, NDs, /):
    prev_ND = ND
    (prev_ND, ND, j4ND)
    _rc = None
    for j4ND, ND in enumerate(NDs, j4ND+1):
        if _rc is None:
            _rc = cmp(_rc, prev_ND, ND)
        else:
            _rc = -_rc
        _rc
        if _rc == -1:
            interval = (prev_ND, ND)
        else:
            interval = (ND, prev_ND)
        interval
        yield interval
        prev_ND = ND
    else:
        last_ND = prev_ND
        yield (last_ND, last_ND)
    return
######################
  def _2_main(ND, j4ND, NDs, /):
    assert using_nested_intervals
    intervals = iter_intervals_(ND, j4ND, NDs)
    return iter_fraction_part_radix_digits_of_limit_of_nested_intervals__ND_repr__ge0_lt1_(radix, intervals, _detail_=_detail_)
######################
  def _1_main(ND, j4ND, NDs, /):
    assert not using_nested_intervals
    prev_ND = ND
    #st = (0, 0)
        # :: (common_prefix/uint, e4shift/uint)
        # :: (yielded_part/uint, num_yielded_digits/uint)
    st = 0
        # :: (num_yielded_digits/uint)
    _rc = None
    (prev_ND, ND, j4ND, st)
    for j4ND, ND in enumerate(NDs, j4ND+1):
        _rc = cmp(_rc, prev_ND, ND)
            #^数据错误牜渐近序列冫非左右互换夹逼
        if _detail_:
            _num_yielded_digits = st
        ######################
        (st, digits) = f(st, prev_ND, ND, j4ND)
        ######################
        if _detail_:
            yield (False, (_num_yielded_digits, prev_ND, ND, j4ND), digits)
        else:
            yield from digits
        prev_ND = ND
    else:
        # [fraction_part is rational]
        (prev_ND, ND, j4ND, st)
        assert prev_ND == ND #j4ND
        last_ND = prev_ND
        adjusted_last_ND = adjust(st, last_ND, j4ND)
        it = iter_fraction_part_radix_digits_of_ND__ge0_lt1_(radix, adjusted_last_ND, _detail_=_detail_)
        if _detail_:
            _num_yielded_digits = st
            yield (True, (_num_yielded_digits, last_ND, j4ND, adjusted_last_ND), [*it])
        else:
            yield from it
    return
######################
  return main()
######################


_debug__via_NDs = False
def iter_radix_digits_of_continued_fraction__with_int__via_NDs_(radix, cf_digits, /, *, to_chain_integer_part, _detail_=False, allow_neg_cf=False, using_nested_intervals=_using_nested_intervals):
    '-> ((integer_part/(uint if not allow_neg_cf else (sign/[-1..=+1], uint_part/uint)), fraction_part/radix_digits<radix>/Iter uint%radix) if not to_chain_integer_part else iter ([integer_part]++fraction_part)) | ^ContinuedFractionError__inf__no_cf0'
    ######################
    #if allow_neg_cf:raise NotImplementedError
    def f(cf_digits=cf_digits, /, *, using_LazyList=True):
        if not using_LazyList:
            #to fix:UnboundLocalError: local variable 'cf_cmp_' referenced before assignment
            from seed.math.continued_fraction.continued_fraction_ops import cf_neg, cf_cmp_, cf_sub, cf_floor_ex_
        else:
            from seed.math.continued_fraction.continued_fraction_ops____using_LazyList import cf_neg, cf_cmp_, cf_sub, cf_floor_ex_, cf_0
            from seed.types.LazyList import LazyList
            cf_digits = LazyList(iter(cf_digits))
        if not using_LazyList:
            #calc:sign:
            cf_digits = iter(cf_digits)
            cf_digits = CachedIterator(cf_digits)
            sign = cf_cmp_(cf_digits, cf_0:=[0])
                #^ContinuedFractionError__inf__no_cf0
            cf_digits = cf_digits.chain_detach()
        else:
            sign = cf_cmp_(cf_digits, cf_0.the_lazylist)#LazyList(iter([0]))
                #^ContinuedFractionError__inf__no_cf0
        sign
        is_neg = sign == -1
        if is_neg:
            # [cf < 0]
            cf_digits = cf_neg(cf_digits)
        # [new-cf := abs(old-cf)]
        # [cf >= 0]
        if not using_LazyList:
            # calc:floor_part+is_int:
            cf_digits = iter(cf_digits)
            cf_digits = CachedIterator(cf_digits)
            (is_int, cf0_x) = cf_floor_ex_(cf_digits)
                #^ContinuedFractionError__inf__no_cf0
            cf_digits = cf_digits.chain_detach()
            floor_part = cf0_x
        else:
            (is_int, floor_part) = cf_floor_ex_(cf_digits)
        is_int
        floor_part
        uint_part = floor_part

        if not allow_neg_cf:
            # [integer_part :: uint_part]
            #   兼容冫旧接口
            if is_neg:
                # [cf < 0]
                raise ValueError('cf < 0')
            else:
                # [cf >= 0]
                integer_part = uint_part
        else:
            # [integer_part :: (sign, uint_part)]
            #   新接口通过allow_neg_cf开启
            integer_part = (sign, uint_part)

        integer_part

        if is_int:
            fraction_part = null_iter
            return (integer_part, fraction_part)
        # [cf not int]

        # !! [new-cf := abs(old-cf)]
        # [cf >= 0]
        if not using_LazyList:
            # calc: frac_cf_digits
            #       [frac_cf := cf - floor_part]
            if 0:
                #发现:改用cf_sub()后_detail_结果不同，因为[..., x, 1] --> [..., x+1]
                frac_cf_digits = cf_sub(cf_digits, [floor_part], _optimize_on_int=False)
                    # !! [cf >= 0]
            elif 1:
                frac_cf_digits = cf_sub(cf_digits, [floor_part], _optimize_on_int=True)
            else:
                for cf0 in cf_digits:
                    assert cf0 == floor_part
                    break
                else:
                    # !! [cf not int]
                    # [cannot reach here]
                    raise 000
                _1_cf_digits = cf_digits
                frac_cf_digits = chain([0], _1_cf_digits)
            frac_cf_digits
        else:
            frac_cf_digits = cf_sub(cf_digits, LazyList(iter([floor_part])), _optimize_on_int=True)
            check_type_is(LazyList, frac_cf_digits)
            check_type_is(LazyList, cf_digits)
            frac_cf_digits = iter(frac_cf_digits)
                #del LazyList
        cf_digits = None
        frac_cf_digits
        # [0 <= frac_cf < 1]
        ######################
        assert cf_digits is None
        integer_part, frac_cf_digits
        NDs = iter_approximate_fraction_NDs5continued_fraction_(frac_cf_digits)
        fraction_part = iter_fraction_part_radix_digits_of_limit_of_NDs__alter_side__ge0_lt1_(radix, NDs, _detail_=_detail_, using_nested_intervals=using_nested_intervals)
        return (integer_part, fraction_part)

    (integer_part, fraction_part) = f()
    if to_chain_integer_part:
        it = chain([integer_part], fraction_part)
        return it
    return (integer_part, fraction_part)

    ######################
    raise 000#below for old-API
    ######################
    r'''[[[
    ######################
    #ver1-->ver2
    def _ver1_X_ver2(cf_digits, /, *, ver):
        assert ver in (1,2)
        #cf_digits = to_PeekableIterator(cf_digits)
        cf_digits = iter(cf_digits)
        cf_digits = CachedIterator(cf_digits)
        (is_int, cf0_x) = cf_floor_ex_(cf_digits)
            #^ContinuedFractionError__inf__no_cf0
        cf_digits = cf_digits.chain_detach()
        floor_part = cf0_x
        if is_int:
            integer_part = floor_part
            fraction_part = null_iter
            #return True, (integer_part, fraction_part)
            frac_cf_digits = [0] #含小数点前面的0
            cf_digits = None
        else:
            ######################
            #ver1:bug:
            if ver==1:
                #bug:when neg:
                (cf_digits, integer_part, frac_cf_digits) = _ver1__bug_when_neg(cf_digits, floor_part)
            ######################
            #ver2:
            elif ver==2:
                (cf_digits, integer_part, frac_cf_digits) = _ver2(cf_digits, floor_part)
            else:
                raise 000
            #return False, (cf_digits, integer_part, frac_cf_digits)
        return (cf_digits, is_int, integer_part, frac_cf_digits)
    ######################
    #ver1:
    def _ver1__bug_when_neg(cf_digits, floor_part, /):
        #发现bug:源自于:输入[-567, 1, 1] 输出错误结果: '-567.5' # 应该是 '-566.5'
        #   连分数 整数项的负号 不涉及 部分分数项
        #   浮点数 整数部分的负号 也是 小数部分的负号
        integer_part = floor_part
        for cf0 in cf_digits:
            assert cf0 == integer_part
            break
        else:
            # !! [cf not int]
            # [cannot reach here]
            raise 000
        _1_cf_digits = cf_digits
        cf_digits = None
        frac_cf_digits = chain([0], _1_cf_digits)
        return (cf_digits, integer_part, frac_cf_digits)
    ######################
    #ver2:
    def _ver2(cf_digits, floor_part, /):
        if floor_part < 0:
            # [cf < 0]
            #fixed for negative cf
            # [cf == -abs(cf) == -(abs(integer_part) + fraction_part) == -(-integer_part + fraction_part) == integer_part -fraction_part]
            # [cf == integer_part -fraction_part]
            # [fraction_part == integer_part -cf]
            integer_part = ceil_part = 1+floor_part
            frac_cf_digits = cf_sub([integer_part], cf_digits)
            cf_digits = None
            if _debug__via_NDs:raise 444
        else:
            # [cf > 0]
            # [cf == integer_part + fraction_part]
            if 1:
                #为了保持doctest中_detail_结果不变，仍旧使用旧方法_ver1__bug_when_neg():
                (cf_digits, integer_part, frac_cf_digits) = _ver1__bug_when_neg(cf_digits, floor_part)
            else:
                #发现:改用cf_sub()后_detail_结果不同，因为[..., x, 1] --> [..., x+1]
                if _debug__via_NDs:
                    cf_digits = _cf_digits = [*cf_digits]
                integer_part = floor_part
                frac_cf_digits = cf_sub(cf_digits, [integer_part])
                cf_digits = None
                if _debug__via_NDs:
                    frac_cf_digits = [*frac_cf_digits]
                    _cf_digits
                    print_err('cf_digits=', _cf_digits)
                    print_err('frac_cf_digits=', frac_cf_digits)
        return (cf_digits, integer_part, frac_cf_digits)
    ######################
    #ver3:
    def _ver3(cf_digits, /):
        cf_digits = iter(cf_digits)
        cf_digits = CachedIterator(cf_digits)
        r = cf_cmp_(cf_digits, cf_0:=[0])
            #^ContinuedFractionError__inf__no_cf0
        cf_digits = cf_digits.chain_detach()
        # [cf == cf_0 + [0;*_1_cf_digits]]
        if r == -1:
            # [cf < 0]
            # [cf == cf_0 + [0;*_1_cf_digits] < 0]
            # [cf_0 < 0]
            cf_digits = cf_neg(cf_digits)
            # [old_cf == -new_cf == -(new-cf_0 + [0;*new-_1_cf_digits])]
            # [old-integer_part - old-fraction_part == old_cf == - new-cf_0 - [0;*new-_1_cf_digits]]
            # [[0;*new-_1_cf_digits] =!= [0;1]]:
            #       [old-integer_part == - new-cf_0]
            #       [old-fraction_part == [0;*new-_1_cf_digits]]
            #
            #
            # [new-cf >= 0]
        # [cf >= 0]
        (cf_digits, is_int, integer_part, frac_cf_digits) = _ver1_X_ver2(cf_digits, ver=1) #<<==[cf >= 0]
        if r == -1:
            assert integer_part >= 0
            if is_int:
                assert integer_part > 0
                integer_part = -integer_part
            else:
                #bug:when[integer_part==0]无法自带负号！！比如:『-0.3』
                #   API大改动: [integer_part::int] --> [integer_part::(sign, uint_part)]
                integer_part = -integer_part
                raise 000
        return (cf_digits, is_int, integer_part, frac_cf_digits)
    ######################
    def main(cf_digits, /, *, ver):
        assert ver in (1,2,3)
        if ver==3:
            (cf_digits, is_int, integer_part, frac_cf_digits) = _ver3(cf_digits)
        else:
            (cf_digits, is_int, integer_part, frac_cf_digits) = _ver1_X_ver2(cf_digits, ver=ver)
        ######################
        assert cf_digits is None
        integer_part, frac_cf_digits
        NDs = iter_approximate_fraction_NDs5continued_fraction_(frac_cf_digits)
        fraction_part = iter_fraction_part_radix_digits_of_limit_of_NDs__alter_side__ge0_lt1_(radix, NDs, _detail_=_detail_, using_nested_intervals=using_nested_intervals)
        integer_part, fraction_part

        if to_chain_integer_part:
            return chain([integer_part], fraction_part)
        return (integer_part, fraction_part)
    ######################
    return main(cf_digits, ver=3)
    #]]]'''#'''

def iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_(radix, cf, /, *, to_chain_integer_part, using_LazyList, allow_neg_cf=False):
    '[#!!RecursionError!!use iter_radix_digits_of_continued_fraction__with_int__via_NDs_ instead#] -> ((integer_part/(uint if not allow_neg_cf else (sign/[-1..=+1], uint_part/uint)), fraction_part/radix_digits<radix>/Iter uint%radix) if not to_chain_integer_part else iter ([integer_part]++fraction_part)) | ^ContinuedFractionError__inf__no_cf0'
    #if allow_neg_cf:raise NotImplementedError

    mk_CF = CF__using_LazyList if using_LazyList else CF__original
    def f(cf = mk_CF(cf)):
        check_type_is(mk_CF, cf)
        #is_neg = cf < 0
        sign = sign_of(cf)
        is_neg = sign == -1

        if is_neg:
            cf = -cf
        # [new-cf := abs(old-cf)]
        floor_part = math.floor(cf)
        uint_part = floor_part

        if not allow_neg_cf:
            # [integer_part :: uint_part]
            #   兼容冫旧接口
            if is_neg:
                # [cf < 0]
                raise ValueError('cf < 0')
            else:
                # [cf >= 0]
                integer_part = uint_part
        else:
            # [integer_part :: (sign, uint_part)]
            #   新接口通过allow_neg_cf开启
            integer_part = (sign, uint_part)

        yield integer_part

        # !! [new-cf := abs(old-cf)]
        cf -= floor_part
        # [0 <= cf < 1]
        while not cf == 0:
            cf *= radix
            digit = math.floor(cf)
            yield digit
            cf -= digit
    cf = None
    it = f()
    if to_chain_integer_part:
        return it
    for integer_part in it:
        fraction_part = it
        break
    return (integer_part, fraction_part)






__all__
r'''[[[
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
class _(ABC):
    __slots__ = ()
    raise NotImplementedError
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        #return repr_helper(sf, *args, **kwargs)
        #return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
        ...
if __name__ == "__main__":
class IFormatter4float_radix_fraction(ABC):
    __slots__ = ()
    def __call__(sf, integer_part, fraction_part, /):
        'int -> (Iter digit) -> str'
    @property
    def imay_max_num_digits_after_dot(sf, /):
        '-> imay'
    @property
    def fixed_point__vs__float_point(sf, /):
        '-> bool'
        #fractional fixed point
    @property
    def to_remove_tailing_zeros(sf, /):
        '-> bool#tailing_zeros come from truncate'
    @property
    def radix(sf, /):
        '-> uint{>=2}'
    def on_integer_part_(sf, integer_part, /):
        'int -> str'
        digits = . .
        return sf.on_digits_(digits)
    def on_fraction_part_(sf, fraction_part, /):
        'Iter uint%radix -> str'
        return sf.on_digits_(fraction_part)
    def on_digits_(sf, digits, /):
        'Iter uint%radix -> str'
        return sf.join_digits_(map(sf.on_digit_, digits))
    def on_digit_(sf, digit, /):
        'uint%radix -> str'
    def join_digits_(sf, ss, /):
        'Iter str -> str'
        return ''.join(ss)
    def on_sign_(sf, sign, /):
        '(-1|0|+1) -> str'
        check_type_is(int, sign)
        if not -1 <= sign <= +1:raise 000
        return ('', '', '-')[sign]
#]]]'''#'''

def _mk_alphabet5hts_(hts__str, /):
    def __(s, /):
        assert len(s)&1 == 0
        for i in range(len(s))[::2]:
            yield s[i:i+2]
    return ''.join(map(_mk_alphabet5ht_, __(hts__str)))
def _mk_alphabet5ht_(ht, /):
    h, t = ht
    i = ord(h)
    j = ord(t)
    assert h <= t, ht
    return ''.join(map(chr, range(i,1+j)))
alphabet_09AZ = _mk_alphabet5hts_('09AZ')
def mk_formatter4fixed_point_fractional(radix, /, alphabet=alphabet_09AZ, *, imay_max_num_digits_after_dot, dot='.', signs=('', '', '-')):
    'radix/int{>=2} -> alphabet/str{len>=radix} -> formatter/((sign, uint_part) -> (Iter digit) -> str)'
    #TypeError: mk_formatter4fixed_point_fractional() missing 1 required keyword-only argument: 'imay_max_num_digits_after_dot'
    check_radix_(radix)
    check_type_is(str, alphabet)
    if not radix <= len(alphabet):raise 777


    check_int_ge(-1, imay_max_num_digits_after_dot)

    check_type_is(str, dot)
    if not dot:raise 777

    check_type_is(tuple, signs)
    if not len(signs) == 3:raise 777
    for k in range(3):
        check_type_is(str, signs[k])



    def _on_digit_(digit, /):
        check_type_is(int, digit)
        if not 0 <= digit < radix:raise 777
        return alphabet[digit]
    if 0b0000:
        kkk = 0
        def on_digit_(digit, /):
            nonlocal kkk
            kkk += 1
            print_err('kkk=', kkk)
            if kkk > 1000:raise 000
            return _on_digit_(digit)
    else:
        on_digit_ = _on_digit_
    on_digit_
    def on_digits_(digits, /):
        return ''.join(map(on_digit_, digits))
    def formatter4fixed_point_fractional(integer_part, fraction_part, /):
        '(sign, uint_part) -> (Iter digit) -> str'
        if 0:
            (sign, digits4i) = i2sign_digits_pair_(radix, integer_part)
        else:
            (sign, uint_part) = integer_part
            (_, digits4i) = i2sign_digits_pair_(radix, uint_part)
        (sign, digits4i)

        if not digits4i:
            digits4i = [0]

        if not -1 == imay_max_num_digits_after_dot:
            max_num_digits_after_dot = imay_max_num_digits_after_dot
            fraction_part = islice(fraction_part, max_num_digits_after_dot)
        digits4f = iter(fraction_part)
        s4s = signs[sign]
        s4i = on_digits_(digits4i)
        s4f = on_digits_(digits4f)
        if not s4f:
            return f'{s4s}{s4i}'
        return f'{s4s}{s4i}{dot}{s4f}'
    return formatter4fixed_point_fractional

def i5sign_digits_pair_(radix, signed_digits, /):
    'big_endian'
    (sign, digits) = signed_digits
    u = 0
    for d in digits:
        u = u*radix +d
    if sign == -1:
        i = -u
    else:
        i = +u
    return i
def i2sign_digits_pair_(radix, i, /):
    'big_endian'
    sign = sign_of(i)
    u = abs(i)
    digits = []
    while u:
        u, d = divmod(u, radix)
        digits.append(d)
    digits.reverse()
    return (sign, digits)


def radix_repr5continued_fraction_(radix, cf_digits, /, *, formatter=None, **kwds4mk_formatter):
    r'''[[[
    typing:
    formatter/((sign, uint_part) -> (Iter digit) -> str)
    kwds4mk_formatter:<<==see:mk_formatter4fixed_point_fractional()
    #]]]'''#'''
    if not formatter is None:
        if not callable(formatter):raise 777
        if kwds4mk_formatter:raise 777
    else:
        formatter = mk_formatter4fixed_point_fractional(radix, **kwds4mk_formatter)
    assert callable(formatter)

    (integer_part, fraction_part) = iter_radix_digits_of_continued_fraction__with_int__via_NDs_(radix, cf_digits, to_chain_integer_part=False, _detail_=False, allow_neg_cf=True)
    (sign, uint_part) = integer_part
    radix_repr = formatter(integer_part, fraction_part)
    check_type_is(str, radix_repr)
    return radix_repr

def __():
    #发现:改用cf_sub()后_detail_结果不同，因为[..., x, 1] --> [..., x+1]
    global _debug__via_NDs
    from seed.iters.apply_may_args4islice_ import list_islice_, show_islice_, stable_show_islice_, stable_list_islice_
    _debug__via_NDs = True
    try:
        show_islice_(11, iter_radix_digits_of_continued_fraction__with_int__via_NDs_(10, repeat(1, 3), to_chain_integer_part=True, _detail_=True))
            #cf_digits= [1, 1, 1]
            #frac_cf_digits= [0, 2]
        frac_NDs = [*iter_approximate_fraction_NDs5continued_fraction_(frac_cf_digits := [0,2])]
        assert frac_NDs == [(0, 1), (1, 2)], frac_NDs
        digits4f = [*iter_fraction_part_radix_digits_of_limit_of_NDs__alter_side__ge0_lt1_(10, frac_NDs)]
        assert digits4f == [5], digits4f
    finally:
        _debug__via_NDs = False
    quit()
#__()



class Fail4REPR(Exception):pass
class RadixRepr_Empty(Exception):pass
def check_sign_(sign, /):
    check_int_ge_lt(-1,2, sign)
def check_uint_part_(uint_part, /):
    check_int_ge(0, uint_part)
def check_integer_part_(integer_part, /):
    check_pair(integer_part)
    (sign, uint_part) = integer_part
    check_sign_(sign)
    check_uint_part_(uint_part)

def truncated_continued_fraction2truncated_radix_digits_with_int_(radix, truncated_continued_fraction, /, *, raise_vs_return_empty):
    r'''[[[
    radix -> truncated_continued_fraction -> truncated_radix_digits_with_int

    truncated_continued_fraction
        [int;pint...]{1<=len<+oo}
    truncated_radix_digits_with_int
        [integer_part/(sign,uint_part);digit<radix>...]{1<=len<+oo}

    『截断』于输入而言是区间，于输出而言是确保输出数字正确

    #]]]'''#'''
    #iter_fraction_part_radix_digits_of_limit_of_nested_intervals__ND_repr__ge0_lt1_
    check_type_is(bool, raise_vs_return_empty)
    t_cf = [*truncated_continued_fraction]
    if len(t_cf) == 0:
        if raise_vs_return_empty:
            return []
        raise ContinuedFractionError__inf__no_cf0
    cf0 = t_cf[0]
    assert type(cf0) is int, t_cf
    # [cf0 <= the_exact_value <= cf0+1]
    if len(t_cf) >= 2:
        cf1 = t_cf[1]
    if len(t_cf) == 1 or (len(t_cf) == 2 and cf1==1):
        # [cf[cf0;] == cf0]
        # [cf[cf0;1] == cf0+1]
        # [cf0 < cf[cf0;1,x,...] < cf0+1]
        # cf[cf0;],cf[cf0;1] cannot repr by "integer_part"!!
        #
        # except:cf[cf0;1]@[cf0 <= -2]
        #   [uint_part == -1-cf0]
        #   [sign == -1]
        ######################
        # bug:except:cf[cf0;1]@[cf0 < 0]
        #   [uint_part == -1-cf0]
        #   but [sign <- {0,-1}]
        if len(t_cf) == 1 or cf0 >= -1:
            if raise_vs_return_empty:
                return []
            raise Fail4REPR('cannot repr by integer_part')
        # [len(t_cf) >= 2]
        # [len(t_cf) == 2][cf1==1]
        # [len(t_cf) == 2][cf1==1][cf0 <= -2]
        [cf0, cf1] = t_cf
        assert cf1 == 1
        assert cf0 <= -2
        # [cf0 <= -2]
        # [t_cf <= -1]
        # !! [cf1 exists]
        # [the_exact_value =!= cf0]
        # !! [cf0 <= the_exact_value <= cf0+1]
        # [cf0 < the_exact_value <= cf0+1 <= -1]
        # [the_exact_value <= -1]
        # [sign == -1]
        # [uint_part == floor(abs(the_exact_value)) == abs(ceil(the_exact_value)) == -(cf0+1) == -1-cf0]
        integer_part = (-1, -1-cf0)
        t_rd = [integer_part]
        return t_rd
    assert len(t_cf) >= 2
    assert len(t_cf) > 2 or cf1 >= 2

    if cf0 > 0:
        integer_part = (+1, cf0)
        t_cf[0] = 0
    elif cf0 == 0:
        integer_part = (0, cf0)
    else:
        # !! [2 <= cf1 < +oo]
        integer_part = (-1, -1-cf0)
        t_cf[0] = -1
    fr_t_cf = t_cf
    t_cf = None
    integer_part

    ND0 = calc_ND5finite_continued_fraction_(fr_t_cf)
    fr_t_cf[-1] += 1
    ND1 = calc_ND5finite_continued_fraction_(fr_t_cf)
    fr_t_cf = None

    integer_part, ND0, ND1
    def neg__ND_(ND,/):
        (N,D) = ND
        return (-N,D)
    if cf0 < 0:
        ND0 = neg__ND_(ND0)
        ND1 = neg__ND_(ND1)
    integer_part, ND0, ND1

    it0 = iter_fraction_part_radix_digits_of_ND__ge0_lt1_(radix, ND0)
    it1 = iter_fraction_part_radix_digits_of_ND__ge0_lt1_(radix, ND1)
    it = iter_common_parts_of_(it0, it1)
    t_rd = [integer_part, *it]
    return t_rd

def truncated_continued_fraction5truncated_radix_digits_with_int_(radix, truncated_radix_digits_with_int, /, *, raise_vs_return_empty):
    r'''[[[
    radix -> truncated_radix_digits_with_int -> truncated_continued_fraction

    truncated_continued_fraction
        [int;pint...]{1<=len<+oo}
    truncated_radix_digits_with_int
        [integer_part/(sign,uint_part);digit<radix>...]{1<=len<+oo}

    『截断』于输入而言是区间，于输出而言是确保输出数字正确

    #]]]'''#'''
    #iter_continued_fraction_digits5ND_
    check_type_is(bool, raise_vs_return_empty)
    t_rd = [*truncated_radix_digits_with_int]
    if len(t_rd) == 0:
        if raise_vs_return_empty:
            return []
        raise RadixRepr_Empty
    integer_part = t_rd[0]
    check_integer_part_(integer_part)
    (sign, uint_part) = integer_part
    t_rd[0] = 0
    fr_t_rd = t_rd
    t_rd = None
    (sign, uint_part, fr_t_rd)

    if len(fr_t_rd) == 1 or not any(fr_t_rd):
        if sign == -1:
            if uint_part == 0:
                cf0 = -1
            elif raise_vs_return_empty:
                return []
            else:
                raise Fail4REPR('cannot repr by cf0')
        else:
            cf0 = uint_part
        cf0
        t_cf = [cf0]
        return t_cf


    assert len(fr_t_rd) >= 2
    assert any(fr_t_rd)
    # [the_exact_value not int]

    (sign, uint_part, fr_t_rd)
    if sign == -1:
        # !! [the_exact_value not int]
        cf0 = -1-uint_part
    else:
        cf0 = uint_part
    cf0

    N0 = i5sign_digits_pair_(radix, (+1, fr_t_rd))
        # [sign := +1] ==>> [N1 := N0+1]
    N1 = N0+1
    D = radix**(len(fr_t_rd)-1)
    if sign == -1:
        N0 = D-N0
        N1 = D-N1
    ND0 = (N0, D)
    ND1 = (N1, D)
    it0 = iter_continued_fraction_digits5ND_(*ND0)
    it1 = iter_continued_fraction_digits5ND_(*ND1)
    it = iter_common_parts_of_(it0, it1)
    for h in it:
        assert h == 0
        break
    else:
        raise 000
    t_cf = [cf0, *it]
    return t_cf

def __():
    #iter_fraction_part_radix_digits_of_limit_of_nested_intervals__ND_repr__ge0_lt1_
    assert [5] == (digits := [*iter_fraction_part_radix_digits_of_limit_of_NDs__alter_side__ge0_lt1_(10, iter_approximate_fraction_NDs5continued_fraction_([0,1,1]), _detail_=False, using_nested_intervals=True)]), digits
    assert [(False, (0, ((0, 1), (1, 1)), ((0, 1), (1, 1)), 0), []), (False, (0, ((0, 1), (1, 1)), ((1, 2), (1, 1)), 1), []), (False, (0, ((1, 2), (1, 1)), ((1, 2), (1, 2)), 2), [5]), (True, (0, ((1, 2), (1, 1)), ((1, 2), (1, 2)), 2, 2, ((1, 2), (1, 2))), [])] == (digits := [*iter_fraction_part_radix_digits_of_limit_of_NDs__alter_side__ge0_lt1_(10, iter_approximate_fraction_NDs5continued_fraction_([0,1,1]), _detail_=True, using_nested_intervals=True)]), digits
    quit()
#__()

__all__
#from seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_ import iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_
    #RecursionError
from seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_ import iter_radix_digits_of_continued_fraction__with_int__via_NDs_
from seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_ import radix_repr5continued_fraction_
if 1:
    from seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_ import mk_formatter4fixed_point_fractional
    from seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_ import iter_fraction_part_radix_digits_of_ND__ge0_lt1_
    from seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_ import iter_fraction_part_radix_digits_of_limit_of_NDs__alter_side__ge0_lt1_
    111;    from seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_ import 数据错误

from seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_ import *
