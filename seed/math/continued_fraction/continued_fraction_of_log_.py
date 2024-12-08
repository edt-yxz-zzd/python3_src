#__all__:goto
r'''[[[
e ../../python3_src/seed/math/continued_fraction/continued_fraction_of_log_.py
    view ../../python3_src/nn_ns/math_nn/continued_fraction/continued_fraction.py
    view ../../python3_src/seed/math/continued_fraction/continued_fraction_fold.py
    view ../../python3_src/seed/math/continued_fraction/continued_fraction_of_log_.py
    view ../../python3_src/seed/math/continued_fraction/iter_continued_fraction_of_log__truncated_.py



xxx:无用:TODO:拆解为 固定的连分数 之间 四则运算
    互素分解整数
    [log_(b; y)
    == log_(II<i>(d[i]^eb[i]); II<j>(d[j]^ey[j]))
    == sum<j>(ey[j]*log_(II<i>(d[i]^eb[i]); d[j]))
    == sum<j>(ey[j]/log_(d[j];II<i>(d[i]^eb[i])))
    == sum<j>(ey[j]/sum<i>(eb[i]*log_(d[j];d[i])))
    ]
    {log_(d[j];d[i]) | i,j} are fixed!!
    {log_(d[j];d[i]) | [i<j]} are fixed!!
    [log_(p^ebp*q^ebq;p^eyp*q*eyq)
    # !! == sum<j>(ey[j]/sum<i>(eb[i]*log_(d[j];d[i])))
    == eyp/(ebp*log_(p;p) + ebq*log_(p;q))  +  eyq/(ebp*log_(q;p) + ebq*log_(q;q))
    == eyp/(ebp + ebq*log_(p;q))  +  eyq/(ebp*log_(q;p) + ebq)
    == eyp/(ebp + ebq*log_(p;q))  +  eyq/(ebp/log_(p;q) + ebq)
    ]
    [log_(p^ebp*q^ebq;p^eyp*q*eyq)
    == f(ebp,ebq;eyp,eyq;log_(p;q))
    ]
    [log_(p;q)
    let [cf0 := floor_log_(p;q)
    == cf0 + log_(p;q/p^cf0)
    == cf0 + 1/log_(q/p^cf0;p)
    == cf0 + 1/log_(p^-cf0*q^1;p^1*q^0)
    !! [ebp = -cf0][ebq = 1][eyp = 1][eyq = 0]
    !! == cf0 + 1/(eyp/(ebp + ebq*log_(p;q))  +  eyq/(ebp/log_(p;q) + ebq))
    == cf0 + 1/(1/(-cf0 + 1*log_(p;q))  +  0/...)
    == cf0 + (-cf0 + log_(p;q))
    无用
    不能由旧项得出新项
    ]

DONE:互素分解整数+指数同步步进搜索
    from seed.math.merge_coprimess_into_smaller_coprimes import merge_coprimess_into_smaller_coprimes
    TmpFraction+PowSeq
    效果一般，因为『while not y_ <= pows[-1]:』
        只是 减少了『y/base**cf0』中Fraction(..., _normalize=True) 的gcd



seed.math.continued_fraction.continued_fraction_of_log_
py -m nn_ns.app.debug_cmd   seed.math.continued_fraction.continued_fraction_of_log_ -x
py -m nn_ns.app.doctest_cmd seed.math.continued_fraction.continued_fraction_of_log_:__doc__ -ff -v
from seed.math.continued_fraction.continued_fraction_of_log_ import continued_fraction_of_log_
from seed.math.continued_fraction.continued_fraction_of_log_ import floor_log__Fraction_





>>> from seed.math.continued_fraction.continued_fraction_fold import iter_continued_fraction_digits5ND_, iter_approximate_fractions5continued_fraction_
>>> from math import log
>>> from seed.iters.apply_may_args4islice_ import list_islice_, show_islice_, stable_show_islice_, stable_list_islice_

#>>> from itertools import islice
#>>> list_islice_ = lambda sz,it,/:[*islice(it, sz)]




e others/数学/编程/generic_base85_encode.txt
py -m nn_ns.app.doctest_cmd seed.math.continued_fraction.continued_fraction_of_log_:__doc__ -ff
NOTE:16,41,64,85
>>> iradix = 2**8
>>> for oradix in range(2, 96):
...     cf_digits = list_islice_(4, continued_fraction_of_log_(oradix, iradix))
...     frs = [*iter_approximate_fractions5continued_fraction_(cf_digits)]
...     print(oradix)
...     print('->', cf_digits)
...     print('->', frs)
2
-> [8]
-> [Fraction(8, 1)]
3
-> [5, 21, 12, 2]
-> [Fraction(5, 1), Fraction(106, 21), Fraction(1277, 253), Fraction(2660, 527)]
4
-> [4]
-> [Fraction(4, 1)]
5
-> [3, 2, 4, 12]
-> [Fraction(3, 1), Fraction(7, 2), Fraction(31, 9), Fraction(379, 110)]
6
-> [3, 10, 1, 1]
-> [Fraction(3, 1), Fraction(31, 10), Fraction(34, 11), Fraction(65, 21)]
7
-> [2, 1, 5, 1]
-> [Fraction(2, 1), Fraction(3, 1), Fraction(17, 6), Fraction(20, 7)]
8
-> [2, 1, 2]
-> [Fraction(2, 1), Fraction(3, 1), Fraction(8, 3)]
9
-> [2, 1, 1, 10]
-> [Fraction(2, 1), Fraction(3, 1), Fraction(5, 2), Fraction(53, 21)]
10
-> [2, 2, 2, 4]
-> [Fraction(2, 1), Fraction(5, 2), Fraction(12, 5), Fraction(53, 22)]
11
-> [2, 3, 5, 209]
-> [Fraction(2, 1), Fraction(7, 3), Fraction(37, 16), Fraction(7740, 3347)]
12
-> [2, 4, 3, 7]
-> [Fraction(2, 1), Fraction(9, 4), Fraction(29, 13), Fraction(212, 95)]
13
-> [2, 6, 5, 1]
-> [Fraction(2, 1), Fraction(13, 6), Fraction(67, 31), Fraction(80, 37)]
14
-> [2, 9, 1, 7]
-> [Fraction(2, 1), Fraction(19, 9), Fraction(21, 10), Fraction(166, 79)]
15
-> [2, 20, 1, 49]
-> [Fraction(2, 1), Fraction(41, 20), Fraction(43, 21), Fraction(2148, 1049)]
16
-> [2]
-> [Fraction(2, 1)]
17
-> [1, 1, 22, 2]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(45, 23), Fraction(92, 47)]
18
-> [1, 1, 11, 3]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(23, 12), Fraction(71, 37)]
19
-> [1, 1, 7, 1]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(15, 8), Fraction(17, 9)]
20
-> [1, 1, 5, 1]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(11, 6), Fraction(13, 7)]
21
-> [1, 1, 4, 1]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(9, 5), Fraction(11, 6)]
22
-> [1, 1, 3, 1]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(7, 4), Fraction(9, 5)]
23
-> [1, 1, 3, 3]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(7, 4), Fraction(23, 13)]
24
-> [1, 1, 2, 1]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(5, 3), Fraction(7, 4)]
25
-> [1, 1, 2, 1]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(5, 3), Fraction(7, 4)]
26
-> [1, 1, 2, 2]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(5, 3), Fraction(12, 7)]
27
-> [1, 1, 2, 6]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(5, 3), Fraction(32, 19)]
28
-> [1, 1, 1, 1]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(5, 3)]
29
-> [1, 1, 1, 1]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(5, 3)]
30
-> [1, 1, 1, 1]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(5, 3)]
31
-> [1, 1, 1, 1]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(5, 3)]
32
-> [1, 1, 1, 2]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(8, 5)]
33
-> [1, 1, 1, 2]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(8, 5)]
34
-> [1, 1, 1, 2]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(8, 5)]
35
-> [1, 1, 1, 3]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(11, 7)]
36
-> [1, 1, 1, 4]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(14, 9)]
37
-> [1, 1, 1, 6]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(20, 13)]
38
-> [1, 1, 1, 9]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(29, 19)]
39
-> [1, 1, 1, 17]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(53, 35)]
40
-> [1, 1, 1, 77]
-> [Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(233, 155)]
41
-> [1, 2, 36, 2]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(109, 73), Fraction(221, 148)]
42
-> [1, 2, 14, 1]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(43, 29), Fraction(46, 31)]
43
-> [1, 2, 9, 4]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(28, 19), Fraction(115, 78)]
44
-> [1, 2, 6, 1]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(19, 13), Fraction(22, 15)]
45
-> [1, 2, 5, 3]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(16, 11), Fraction(51, 35)]
46
-> [1, 2, 4, 2]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(13, 9), Fraction(29, 20)]
47
-> [1, 2, 3, 1]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(10, 7), Fraction(13, 9)]
48
-> [1, 2, 3, 5]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(10, 7), Fraction(53, 37)]
49
-> [1, 2, 2, 1]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(7, 5), Fraction(10, 7)]
50
-> [1, 2, 2, 1]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(7, 5), Fraction(10, 7)]
51
-> [1, 2, 2, 3]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(7, 5), Fraction(24, 17)]
52
-> [1, 2, 2, 11]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(7, 5), Fraction(80, 57)]
53
-> [1, 2, 1, 1]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(4, 3), Fraction(7, 5)]
54
-> [1, 2, 1, 1]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(4, 3), Fraction(7, 5)]
55
-> [1, 2, 1, 1]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(4, 3), Fraction(7, 5)]
56
-> [1, 2, 1, 1]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(4, 3), Fraction(7, 5)]
57
-> [1, 2, 1, 2]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(4, 3), Fraction(11, 8)]
58
-> [1, 2, 1, 2]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(4, 3), Fraction(11, 8)]
59
-> [1, 2, 1, 3]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(4, 3), Fraction(15, 11)]
60
-> [1, 2, 1, 4]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(4, 3), Fraction(19, 14)]
61
-> [1, 2, 1, 6]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(4, 3), Fraction(27, 20)]
62
-> [1, 2, 1, 10]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(4, 3), Fraction(43, 32)]
63
-> [1, 2, 1, 21]
-> [Fraction(1, 1), Fraction(3, 2), Fraction(4, 3), Fraction(87, 65)]
64
-> [1, 3]
-> [Fraction(1, 1), Fraction(4, 3)]
65
-> [1, 3, 22, 9]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(89, 67), Fraction(805, 606)]
66
-> [1, 3, 11, 78]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(45, 34), Fraction(3514, 2655)]
67
-> [1, 3, 7, 3]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(29, 22), Fraction(91, 69)]
68
-> [1, 3, 5, 2]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(21, 16), Fraction(46, 35)]
69
-> [1, 3, 4, 2]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(17, 13), Fraction(38, 29)]
70
-> [1, 3, 3, 1]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(13, 10), Fraction(17, 13)]
71
-> [1, 3, 3, 11]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(13, 10), Fraction(147, 113)]
72
-> [1, 3, 2, 1]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(9, 7), Fraction(13, 10)]
73
-> [1, 3, 2, 2]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(9, 7), Fraction(22, 17)]
74
-> [1, 3, 2, 7]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(9, 7), Fraction(67, 52)]
75
-> [1, 3, 1, 1]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(5, 4), Fraction(9, 7)]
76
-> [1, 3, 1, 1]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(5, 4), Fraction(9, 7)]
77
-> [1, 3, 1, 1]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(5, 4), Fraction(9, 7)]
78
-> [1, 3, 1, 1]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(5, 4), Fraction(9, 7)]
79
-> [1, 3, 1, 2]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(5, 4), Fraction(14, 11)]
80
-> [1, 3, 1, 3]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(5, 4), Fraction(19, 15)]
81
-> [1, 3, 1, 4]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(5, 4), Fraction(24, 19)]
82
-> [1, 3, 1, 6]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(5, 4), Fraction(34, 27)]
83
-> [1, 3, 1, 12]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(5, 4), Fraction(64, 51)]
84
-> [1, 3, 1, 40]
-> [Fraction(1, 1), Fraction(4, 3), Fraction(5, 4), Fraction(204, 163)]
85
-> [1, 4, 33, 1]
-> [Fraction(1, 1), Fraction(5, 4), Fraction(166, 133), Fraction(171, 137)]
86
-> [1, 4, 11, 1]
-> [Fraction(1, 1), Fraction(5, 4), Fraction(56, 45), Fraction(61, 49)]
87
-> [1, 4, 7, 3]
-> [Fraction(1, 1), Fraction(5, 4), Fraction(36, 29), Fraction(113, 91)]
88
-> [1, 4, 5, 5]
-> [Fraction(1, 1), Fraction(5, 4), Fraction(26, 21), Fraction(135, 109)]
89
-> [1, 4, 4, 39]
-> [Fraction(1, 1), Fraction(5, 4), Fraction(21, 17), Fraction(824, 667)]
90
-> [1, 4, 3, 3]
-> [Fraction(1, 1), Fraction(5, 4), Fraction(16, 13), Fraction(53, 43)]
91
-> [1, 4, 2, 1]
-> [Fraction(1, 1), Fraction(5, 4), Fraction(11, 9), Fraction(16, 13)]
92
-> [1, 4, 2, 2]
-> [Fraction(1, 1), Fraction(5, 4), Fraction(11, 9), Fraction(27, 22)]
93
-> [1, 4, 2, 10]
-> [Fraction(1, 1), Fraction(5, 4), Fraction(11, 9), Fraction(115, 94)]
94
-> [1, 4, 1, 1]
-> [Fraction(1, 1), Fraction(5, 4), Fraction(6, 5), Fraction(11, 9)]
95
-> [1, 4, 1, 1]
-> [Fraction(1, 1), Fraction(5, 4), Fraction(6, 5), Fraction(11, 9)]

>>> xxx # -ff
>>> list_islice_(7, continued_fraction_of_log_(85, 2**8))
[1, 4, 33, 1, 7, 37, 1]
>>> [*iter_approximate_fractions5continued_fraction_([1, 4, 33, 1, 7, 37, 1])]
[Fraction(1, 1), Fraction(5, 4), Fraction(166, 133), Fraction(171, 137), Fraction(1363, 1092), Fraction(50602, 40541), Fraction(51965, 41633)]
>>> xxx # -ff






>>> floor_log__Fraction_(2, 3, _guess_first=False, with_remain=True)
1
>>> _1 = TmpFraction((2, 3), None, None)
>>> _2 = _1._mk((1,0))
>>> _3 = _1._mk((0,1))
>>> _2 > _3
False
>>> _2**2
TmpFraction((2, 3), (PowSeq(2, [2], 1), PowSeq(3, [3], 1)), (2, 0))
>>> _3
TmpFraction((2, 3), (PowSeq(2, [2], 1), PowSeq(3, [3], 1)), (0, 1))
>>> _2**2 > _3
True
>>> floor_log_ex_(_2, _3, _guess_first=False, with_remain=True)
(1, False, TmpFraction((2, 3), (PowSeq(2, [2, 4], 1), PowSeq(3, [3], 1)), (-1, 1)))
>>> list_islice_(6, continued_fraction_of_log_(2, 3))
[1, 1, 1, 2, 2, 3]

>>> [*iter_approximate_fractions5continued_fraction_([1, 1, 1, 2, 2, 3])]
[Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(8, 5), Fraction(19, 12), Fraction(65, 41)]
>>> 65/41
1.5853658536585367
>>> log(3, 2)
1.5849625007211563
>>> list_islice_(8, iter_continued_fraction_digits5ND_(*Fraction.from_float(log(3, 2)).as_integer_ratio()))
[1, 1, 1, 2, 2, 3, 1, 5]
>>> [*iter_continued_fraction_digits5ND_(15849625007211563, 10000000000000000)]
[1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4, 1, 2, 3, 2, 1, 1, 1, 7, 3, 20, 1, 7, 3, 2, 2, 2, 2, 4]


#too slow
>>> for y in range(1,11):((2,y), list_islice_(12, continued_fraction_of_log_(2, y))) #doctest: +SKIP


>>> list_islice_(12, continued_fraction_of_log_(2, 1))
[0]
>>> list_islice_(12, continued_fraction_of_log_(2, 2))
[1]
>>> list_islice_(12, continued_fraction_of_log_(2, 4))
[2]
>>> list_islice_(7, continued_fraction_of_log_(2, 8))
[3]

>>> list_islice_(12, continued_fraction_of_log_(2, 5))
[2, 3, 9, 2, 2, 4, 6, 2, 1, 1, 3, 1]
>>> list_islice_(7, continued_fraction_of_log_(2, 7)) # len『12』run slow
[2, 1, 4, 5, 4, 5, 4]

>>> list_islice_(12, continued_fraction_of_log_(2, 3))
[1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2]
>>> list_islice_(12, continued_fraction_of_log_(2, 6))
[2, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2]
>>> list_islice_(7, continued_fraction_of_log_(2, 9))
[3, 5, 1, 7, 1, 2, 4]


validate equation: [base**e == y]
continued_fraction_of_log_(2, 3) =>:
>>> [*iter_approximate_fractions5continued_fraction_([1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2])]
[Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(8, 5), Fraction(19, 12), Fraction(65, 41), Fraction(84, 53), Fraction(485, 306), Fraction(1054, 665), Fraction(24727, 15601), Fraction(50508, 31867), Fraction(125743, 79335)]
>>> all((2**N < 3**D) for fr in [*iter_approximate_fractions5continued_fraction_([1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2])][::2] for N,D in [fr.as_integer_ratio()])
True
>>> all((2**N > 3**D) for fr in [*iter_approximate_fractions5continued_fraction_([1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2])][1::2] for N,D in [fr.as_integer_ratio()])
True

>>> [*iter_approximate_fractions5continued_fraction_of_log_(2,3, may_max1_denominator=79335+1)]
[Fraction(1, 1), Fraction(2, 1), Fraction(3, 2), Fraction(8, 5), Fraction(19, 12), Fraction(65, 41), Fraction(84, 53), Fraction(485, 306), Fraction(1054, 665), Fraction(24727, 15601), Fraction(50508, 31867), Fraction(125743, 79335)]
>>> [*iter_approximate_fractions_le5continued_fraction_of_log_(2,3, may_max1_denominator=79335+1)]
[Fraction(1, 1), Fraction(3, 2), Fraction(19, 12), Fraction(84, 53), Fraction(1054, 665), Fraction(50508, 31867)]
>>> [*iter_approximate_fractions_ge5continued_fraction_of_log_(2,3, may_max1_denominator=79335+1)]
[Fraction(2, 1), Fraction(8, 5), Fraction(65, 41), Fraction(485, 306), Fraction(24727, 15601), Fraction(125743, 79335)]



[[[
py_adhoc_call   seed.math.continued_fraction.continued_fraction_of_log_   ,main4continued_fraction_of_log_ =2 =7 --may_args4islice='[12]' -_debug -_guess_first -_express_fraction_by_coprime_factors
===
2
1
4
5
4
5
4
1
29
1
4  # wait seconds to compute "4"
...???... # too long to wait next output # +_guess_first ==>> [this cf_digit <= 8]
    # floor_log_result_is_big:goto
]]]

[[[
py_adhoc_call   seed.math.continued_fraction.continued_fraction_of_log_   ,main4continued_fraction_of_log_ =2 =7 --may_args4islice='[12]' -_debug -_guess_first +_express_fraction_by_coprime_factors
===
2
1
4
5
4
5
4
1
29
1
4
... ...
]]]
[[[
py_adhoc_call   seed.math.continued_fraction.continued_fraction_of_log_   ,main4continued_fraction_of_log_ =2 =7 --may_args4islice='[12]' -_debug -_guess_first -_express_fraction_by_coprime_factors +_using_continued_fraction_as_input4log
===
2
1
4
5
4
5
4
1
... ... #还不如前面的
]]]





[b**((A+B*z)/(C+D*z)) == y]
    <==> [b**(A+B*z) == y**(C+D*z)]
    <==> [b**(B*z)/y**(D*z) == y**C/b**A]
    <==> [(b**B/y**D)**z == y**C/b**A]
    <==> [z == log_((b**B/y**D); (y**C/b**A))]
    (b**B/y**D) --> 1
    (y**C/b**A) --> 1
    ?how?log1p(x) == log(1+x)
        [D ln(x) == ln(x)]
        [D ln(1+x) == ln(1+x)]
        ln(1+x) = sum x**i/i! {i>=1}
        [z == log_(1+p; 1+q)
        == ln(1+q)/ln(1+p)
        ]
    [y==f(x)]:
        # [x:=?]
        [Df(x0) ~= (f(x)-f(x0))/(x-x0)]
        [x ~= x0 + (f(x)-f(x0))/Df(x0)]
        [x ~= x0 + (y-f(x0))/Df(x0)]
        [1+q==(1+p)**x]
        [q == y==f(x) == (1+p)**x -1]
        [Df(x) = (1+p)**x *ln(1+p)]
    [a0 := floor(z)]
    * [b**B > y**D]:
        !! [(b**B/y**D)**z == y**C/b**A]
        [(b**B/y**D)**a0 <= (y**C/b**A) < (b**B/y**D)**(a0+1)]
    * [b**B < y**D]:
        !! [(y**D/b**B)**z == b**A/y**C]
        [(y**D/b**B)**a0 <= (b**A/y**C) < (y**D/b**B)**(a0+1)]
    =>:
    [n>d][(n/d)**x <= (m/b) < (n/d)**(x+1)]:
        # [x := ?]
        [m>b]
        [b*n**x <= m*d**x]
        [m*d*d**x < b*n*n**x]
        [b*d*n**x <= m*d*d**x < b*n*n**x]

#]]]'''
__all__ = r'''
floor_log__Fraction_
continued_fraction_of_log_
main4continued_fraction_of_log_

iter_approximate_fractions5continued_fraction_of_log_
iter_approximate_fractions_le5continued_fraction_of_log_
iter_approximate_fractions_ge5continued_fraction_of_log_

approximate_fraction_le5continued_fraction_of_log_


TmpFraction
floor_log_ex_

'''.split()#'''
__all__

#from functools import totalordering
from itertools import islice
from numbers import Rational
from fractions import Fraction

from seed.math.continued_fraction.continued_fraction_ops import ContinuedFraction
    #直接用连分数作为对数输入
from seed.math.merge_coprimess_into_smaller_coprimes import merge_coprimess_into_smaller_coprimes, semi_factor_coprimess_via_gcd
    #互素分解整数+指数同步步进搜索
from seed.math.II import II
from seed.math.sign_of import sign_of
from seed.helper.repr_input import repr_helper
from seed.math.PowSeq import PowSeq

from seed.math.continued_fraction.continued_fraction_fold import iter_approximate_fractions5continued_fraction_ #iter_continued_fraction_digits5ND_
from seed.math.continued_fraction.continued_fraction_fold import iter_approximate_fraction_NDs5continued_fraction__by_limit_denominator_, iter_approximate_fractions5continued_fraction__by_limit_denominator_, approximate_fraction5continued_fraction__by_limit_denominator_
    #def approximate_fraction5continued_fraction__by_limit_denominator_(max1_denominator, cf_digits, /, *, le_vs_any_vs_ge=0):

#from seed.math.floor_ceil import floor_log_, ceil_log_
    # int-version-floor_log_
from seed.math.gcd import gcd, gcd_many, are_coprime
from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
from seed.tiny import check_type_is, check_type_le
from seed.iters.apply_may_args4islice_ import apply_may_args4islice_

#@totalordering
class TmpFraction:
    def get_args(sf, /):
        return (sf.idx2factor, sf.idx2factor_pows, sf.idx2exp)
    def __repr__(sf, /):
        args = sf.get_args()
        return repr_helper(sf, *args)

    def __init__(sf, idx2factor, may_idx2factor_pows, may_idx2exp, /):
        check_type_is(tuple, idx2factor)
        if not may_idx2factor_pows is None:
            idx2factor_pows = may_idx2factor_pows
            check_type_is(tuple, idx2factor_pows)
            if not len(idx2factor_pows) == len(idx2factor): raise TypeError
        else:
            idx2factor_pows = tuple(map(PowSeq, idx2factor))

        if not may_idx2exp is None:
            idx2exp = may_idx2exp
            check_type_is(tuple, idx2exp)
            if not len(idx2exp) == len(idx2factor): raise TypeError
        else:
            idx2exp = (0,)*len(idx2factor)
                # <==> 1


        sf.idx2factor = idx2factor
        sf.idx2factor_pows = idx2factor_pows
        sf.idx2exp = idx2exp
    def is_int(sf, /):
        return not any(e < 0 for e in sf.idx2exp)
    def _mk(sf, idx2exp, /):
        return __class__(sf.idx2factor, sf.idx2factor_pows, idx2exp)
    def _from_uint(sf, u, /):
        check_type_is(int, u)
        if not u==1: raise NotImplementedError
        return __class__(sf.idx2factor, sf.idx2factor_pows, (0,)*len(sf.idx2factor))
    def __truediv__(sf, ot, /):
        if type(ot) is int:
            ot = sf._from_uint(ot)
        if type(ot) is type(sf):
            if not ot.idx2factor_pows is sf.idx2factor_pows: raise TypeError
            return sf._mk(tuple(map(int.__sub__, sf.idx2exp, ot.idx2exp)))
        raise NotImplementedError
    def __mul__(sf, ot, /):
        if type(ot) is int:
            ot = sf._from_uint(ot)
        if type(ot) is type(sf):
            if not ot.idx2factor_pows is sf.idx2factor_pows: raise TypeError
            return sf._mk(tuple(map(int.__add__, sf.idx2exp, ot.idx2exp)))
        raise NotImplementedError
    def __pow__(sf, e, /):
        check_type_is(int, e)
        return sf._mk(tuple(map(e.__mul__, sf.idx2exp)))
    def __eq__(sf, ot, /):
        if type(ot) is int:
            if ot == 1:
                return not any(sf.idx2exp)
            if ot == 0:
                return False
        elif type(ot) is type(sf):
            if not ot.idx2factor_pows is sf.idx2factor_pows: raise TypeError
            return ot.idx2exp == sf.idx2exp
        raise NotImplementedError
    @property
    def numerator(sf, /):
        try:
            return sf._N
        except AttributeError:
            sf._N = II(pows.get_pow_(e) for pows, e in zip(sf.idx2factor_pows, sf.idx2exp) if e > 0)
        return sf._N

        #return II(ft**e for ft, e in zip(sf.idx2factor, sf.idx2exp) if e > 0)
    @property
    def denominator(sf, /):
        try:
            return sf._D
        except AttributeError:
            sf._D = II(pows.get_pow_(-e) for pows, e in zip(sf.idx2factor_pows, sf.idx2exp) if e < 0)
        return sf._D

        #return II(ft**(-e) for ft, e in zip(sf.idx2factor, sf.idx2exp) if e < 0)
        #N:numerator
        #D:denominator
    def _cmp(sf, ot, /):
        #print(sf, ot)
        if type(ot) is int:
            if ot == 1:
                #print(sf.numerator, sf.denominator)
                return sign_of(sf.numerator - sf.denominator)
            if ot == 0:
                return +1
        elif type(ot) is type(sf):
            if not ot.idx2factor_pows is sf.idx2factor_pows: raise TypeError
            return (sf/ot)._cmp(1)
        elif type(ot) is Fraction:
            return sign_of(sf.numerator*ot.denominator - ot.numerator*sf.denominator)

        raise NotImplementedError
    if 0:
        def __eq__(sf, ot, /):
            return sf._cmp(ot) == 0
    def __lt__(sf, ot, /):
        return sf._cmp(ot) == -1
    def __gt__(sf, ot, /):
        return sf._cmp(ot) == +1

    def __ne__(sf, ot, /):
        return not sf == ot
    def __le__(sf, ot, /):
        return not sf > ot
    def __ge__(sf, ot, /):
        return not sf < ot


def _prepare(base, y, /):
    '-> ... if y==1 else (base, y)'
    if not y > 0: raise ValueError
    if not base > 0: raise ValueError
    if base == 1: raise ValueError
    # [base > 0][base=!=1][y > 0]
    if y == 1:
        # [base > 0][base=!=1][y == 1]
        return ...
    # [base > 0][base=!=1][y > 0][y =!= 1]
    had_inv_base = False
    had_inv_y = False
    if base < 1:
        base = 1/base
        had_inv_base = not had_inv_base
        # [log_(b;y) == -log_(1/b;y)]
    # [base > 1][y > 0][y =!= 1]
    if y < 1:
        y = 1/y
        had_inv_y = not had_inv_y
        # [log_(b;y) == -log_(b;1/y)]
    # [base > 1][y > 1]
    to_neg = had_inv_base^had_inv_y
    return (to_neg, had_inv_base, had_inv_y, base, y)
def floor_log__Fraction_(base, y, /, *, _guess_first, with_remain):
    'Fraction-version-floor_log_'
    base = Fraction(base)
    y = Fraction(y)
    (e, exact, y_remain) = floor_log_ex_(base, y, _guess_first=_guess_first, with_remain=with_remain)
    return e

def floor_log_ex_(base, y, /, *, _guess_first, with_remain):
    #'Fraction-or-???TmpFraction???-or-ContinuedFraction-version-floor_log_'
    r'''[[[
[[base > 0][base=!=1][y > 0]]:
    [floor_log_(base;y) =[def]= floor(log_(base;y))]

    [floor_log_ex_(base;y) =[def]= (e, exact, y_remain) where [[e := floor_log_(base;y)][exact := [y_remain==1]][y_remain := y/base**e]]]

    [(e, exact, y_remain) := floor_log_ex_(base;y)]:
        !! [[e := floor_log_(base;y)][exact := [y_remain==1]][y_remain := y/base**e]]
        * [base > 1]:
            [base**e <= y < base**(e+1)]
            [1 <= y/base**e < base]
            [1 <= y_remain < base]
        * [base < 1]:
            [base**e >= y > base**(e+1)]
            [1 >= y_remain > base]
        [[1 <= y_remain < base]xor[1 >= y_remain > base]]

[[base > 1][y > 1]]:
    [floor_log_ex__gt1_(base;y) =[def]= floor_log_ex_(base;y)]

floor_log_(base;y) = floor_log_ex_(base;y)[0]


[[reshape_output:here
[[base > 0][base=!=1][y > 0]]:
    floor_log_ex_(base;y) = (e, exact, y_remain) where:
    [exact := exact_]
    [to_neg := [base < 1]xor[y < 1]]
    [e := if to_neg then -[not exact_]-e_ else e_]
    [y_remainM := if [y < 1] then 1/y_remain_ else y_remain_]
    [y_remain := y_remainM * if to_negand [not exact_] then base else 1]
    <<==:
    * [base < 1][y < 1]:
        (e_, exact_, y_remain_) = floor_log_ex__gt1_(1/base;1/y)
        [exact := exact_]
        [e := e_]
        [y_remain := 1/y_remain_]
    * [base < 1][y > 1]
        (e_, exact_, y_remain_) = floor_log_ex__gt1_(1/base;y)
        [exact := exact_]
        [e := -[not exact_]-e_]
        [y_remain := y_remain_*base**[not exact_]]
    * [base > 1][y < 1]:
        (e_, exact_, y_remain_) = floor_log_ex__gt1_(base;1/y)
        [exact := exact_]
        [e == -[not exact_]-e_]
        [y_remain == 1/y_remain_ *base**[not exact_]]
    * [base > 1][y > 1]:
        (e_, exact_, y_remain_) = floor_log_ex__gt1_(base;y)
        [exact := exact_]
        [e := e_]
        [y_remain := y_remain_]
]] <<==:
[[
floor_log_ex_(base;y)
    | not [[base > 0][base=!=1][y > 0]] = _L
    | [base < 1][y < 1] = (e, exact, y_remain) where
        (e_, exact_, y_remain_) = floor_log_ex__gt1_(1/base;1/y)
        [exact := exact_]
        [e := e_]
        [y_remain := 1/y_remain_]
        ######
        [[proof:
        [[e := floor_log_(base;y)][exact := [y_remain==1]][y_remain := y/base**e]]
        [[e_ := floor_log_(1/base;1/y)][exact_ := [y_remain_==1]][y_remain_ := (1/y)/(1/base)**e_]]
        [e_
        == floor_log_(1/base;1/y)
        == floor(log_(1/base;1/y))
        == floor(log_(base;y))
        == floor_log_(base;y)
        == e
        ]
        [e == e_]
        [y_remain_
        == (1/y)/(1/base)**e_
        == (1/y)/(1/base)**e
        == 1/(y/base**e)
        == 1/y_remain
        ]
        [y_remain == 1/y_remain_]
        [exact_
        == [y_remain_==1]
        == [1/y_remain==1]
        == [y_remain==1]
        == exact
        ]
        [exact == exact_]
        ]]
    | [base < 1][y > 1] = (e, exact, y_remain) where
        (e_, exact_, y_remain_) = floor_log_ex__gt1_(1/base;y)
        [exact := exact_]
        [e := -[not exact_]-e_]
        [y_remain := y_remain_*base**[not exact_]]
        ######
        [[proof:
        [[e := floor_log_(base;y)][exact := [y_remain==1]][y_remain := y/base**e]]
        [[e_ := floor_log_(1/base;y)][exact_ := [y_remain_==1]][y_remain_ := y/(1/base)**e_]]
        [e_
        == floor_log_(1/base;y)
        == floor(log_(1/base;y))
        == floor(-log_(base;y))
        == -[not exact_]-floor_log_(base;y)
        == -[not exact_]-e
        ]
        [e == -[not exact_]-e_]
        [y_remain_
        == y/(1/base)**e_
        == y/(1/base)**(-[not exact_]-e_)
        == y/base**([not exact_]+e_)
        == y/base**e /base**[not exact_]
        == y_remain /base**[not exact_]
        ]
        [y_remain == y_remain_*base**[not exact_]]
        * [y_remain_==1]:
            [exact_ == [y_remain_==1] == 1]
            [y_remain == y_remain_*base**[not exact_] == y_remain_ == 1]
        * [y_remain_=!=1]:
            [exact_ == [y_remain_==1] == 0]
            [y_remain == y_remain_*base**[not exact_] == y_remain_*base]
            !! [[1 <= y_remain < base]xor[1 >= y_remain > base]]
            [[1 <= y_remain_ < 1/base]xor[1 >= y_remain_ > 1/base]]
            !! [base < 1]
            [1 <= y_remain_ < 1/base]
            !! [y_remain_=!=1]
            [1 < y_remain_ < 1/base]
            [y_remain_*base > 1]
            [y_remain == y_remain_*base > 1]
        [[y_remain==1] == [y_remain_==1]]
        [exact == exact_]
        ]]
    | [base > 1][y < 1] = (e, exact, y_remain) where
        (e_, exact_, y_remain_) = floor_log_ex__gt1_(base;1/y)
        [exact := exact_]
        [e := -[not exact_]-e_]
        [y_remain := 1/y_remain_ *base**[not exact_]]
        ######
        [[proof:
        [[e := floor_log_(base;y)][exact := [y_remain==1]][y_remain := y/base**e]]
        [[e_ := floor_log_(base;1/y)][exact_ := [y_remain_==1]][y_remain_ := (1/y)/base**e_]]
        [e_
        == floor_log_(base;1/y)
        == floor(log_(base;1/y))
        == floor(-log_(base;y))
        == -[not exact_]-floor_log_(base;y)
        == -[not exact_]-e
        ]
        [e == -[not exact_]-e_]
        [y_remain_
        == (1/y)/base**e_
        == (1/y)/base**(-[not exact_]-e)
        == 1/(y/base**e) *base**[not exact_]
        == 1/y_remain *base**[not exact_]
        ]
        [y_remain == 1/y_remain_ *base**[not exact_]]
        * [y_remain_==1]:
            [exact_ == [y_remain_==1] == 1]
            [y_remain == 1/y_remain_*base**[not exact_] == 1/y_remain_ == 1]
        * [y_remain_=!=1]:
            [exact_ == [y_remain_==1] == 0]
            [y_remain == 1/y_remain_*base**[not exact_] == 1/y_remain_*base]
            !! [[1 <= y_remain < base]xor[1 >= y_remain > base]]
            [[1 <= y_remain_ < base]xor[1 >= y_remain_ > base]]
            !! [base > 1]
            [1 <= y_remain_ < base]
            !! [y_remain_=!=1]
            [1 < y_remain_ < base]
            [1/y_remain_*base > 1]
            [y_remain == 1/y_remain_*base > 1]
        [[y_remain==1] == [y_remain_==1]]
        [exact == exact_]

        ]]
    | [base > 1][y > 1] = floor_log_ex__gt1_(base;y)
]]


    #]]]'''#'''
#def floor_log_ex_(base, y, /, *, _guess_first, with_remain):
    base0 = base
    y0 = y
    r = _prepare(base, y); del base, y
    if r is ...:
        # [base > 0][base=!=1][y == 1]
        e0 = 0
        exact0 = True
        y_remain0 = 1 if with_remain else None
        return e0, exact0, y_remain0
    (to_neg, had_inv_base, had_inv_y, base_, y_) = r; del r
    # [had_inv_base == [base_ == 1/base0] == [base_ is not base0]]
    # [had_inv_y == [y_ == 1/y0] == [y_ is not y0]]
    # [to_neg == had_inv_base xor had_inv_y]

    # [base_ > 1][y_ > 1]
    (e_, exact_, y_remain_) = _floor_log_ex__gt1_(base_, y_, _guess_first=_guess_first, with_remain=with_remain); del base_, y_
    #reshape_output:goto
    #
    # [exact := exact_]
    # [to_neg := [base < 1]xor[y < 1]]
    # [e := if to_neg then -[not exact_]-e_ else e_]
    # [y_remainM := if [y < 1] then 1/y_remain_ else y_remain_]
    # [y_remain := y_remainM * if to_negand [not exact_] then base else 1]
    exact0 = exact_
    e0 = e_ if not to_neg else -(not exact_)-e_
    y_remain0 = 1/y_remain_ if had_inv_y else y_remain_
    if to_neg and not exact_:
        y_remain0 *= base0

    assert (1 >= y0/base0**e0 == y_remain0 > base0) if had_inv_base else (1 <= y0/base0**e0 == y_remain0 < base0)
        # [[1 <= y_remain < base]xor[1 >= y_remain > base]]
    return e0, exact0, y_remain0
#end-def floor_log_ex_(base, y, /, *, _guess_first, with_exact, with_remain):


_near1 = 1+Fraction(1, 1<<4)
def _floor_log_ex__gt1_(base, y, /, *, _guess_first, with_remain):
    'Fraction-version-floor_log_'
    # [base > 1][y > 1]
    #   if not first round: [1 < base < y]
    if _guess_first:
        (e, exact, y_remain) = _floor_log_ex__gt1__impl__guess_first_(base, y, with_remain=with_remain)
    else:
        (e, exact, y_remain) = _floor_log_ex__gt1__impl_(base, y, with_remain=with_remain)
    assert 1 <= y/base**e == y_remain < base
        # [base**e <= y < base**(e+1)]
    return (e, exact, y_remain)
def _floor_log_ex__gt1__impl__guess_first_(base, y, /, *, with_remain):
    'Fraction-version-floor_log_ #guess a initial result at first'
    # [base > 1][y > 0][y =!= 1]
    #   if not first round: [1 < base < y]
    y0 = y; del y
    trans = base < _near1
    if trans:
        if y0 < base:
            e = 0
            exact = False
            y_remain = y0 if with_remain else None
            return (e, exact, y_remain)
        # [base == 1+p]
        p = base - 1
        # [y0 == base**x == (1+p)**x >= 1+x*p]
        # [x <= (y0-1)/p]
        # [x_ := floor((y0-1)/p)]
        # [x <= x_ == (y0-1)//p <= (y0-1)/p]
        # [e == floor(x) <= x <= x_ == (y0-1)//p <= (y0-1)/p]
        # [e <= x_]
        x_ = (y0-1)//p
        if 0b00:
            print(f'_floor_log_ex__gt1__impl__guess_first_:x_ = {x_}')
            if x_ > 100:
                # floor_log_result_is_big:here
                print(f'_floor_log_ex__gt1__impl__guess_first_:x_ is big:{x_}')

        # [[base**x_ <= y0] -> [x_ <= e]]
        # !! [e <= x_]
        # [[base**x_ <= y0] -> [e == x_]]
        y_ = base**x_ / y0
        if y_ <= 1:
            e = x_
            y_remain = 1/y_
            exact = y_remain == 1
            if not with_remain:
                y_remain = None
            return (e, exact, y_remain)
        # [y_ > 1]
    else:
        y_ = y0
        # [y_ > 1]
    # [y_ > 1]
    (e_, exact_, y_remain_) = _floor_log_ex__gt1__impl_(base, y_, with_remain=with_remain)
    if trans:
        exact = exact_
        # [e_ == floor_log_(base, base**x_/y0) == x_+floor_log_(base, 1/y0) == x_-ceil_log_(base, y0) == x_-(floor_log_(base, y0) +[not exact_]) == x_-e -[not exact]]
        # [e_ == x_-e -[not exact]]
        # [e == x_-e_ -[not exact]]
        e = x_-e_ -(not exact_)
        # [y_remain_ == (base**x_/y0)/base*e_ == 1/(y0/base**(x_-e_)) == 1/(y0/base**(e +[not exact])) == 1/(y0/base**e) *base**[not exact] == 1/y_remain *base**[not exact]]
        # [y_remain_ == 1/y_remain *base**[not exact]]
        # [y_remain == 1/y_remain_ *base**[not exact]]
        y_remain = (1 if exact else base)/y_remain_
    else:
        (e, exact, y_remain) = (e_, exact_, y_remain_)
    return (e, exact, y_remain)

def _floor_log_ex__gt1__impl_(base, y, /, *, with_remain):
    'Fraction-version-floor_log_'
    # [base > 1][y > 1]
    #   if not first round: [1 < base < y]
    y0 = y; del y
    if type(base) is ContinuedFraction:
        base_is_int = base.is_int()
        support_floordiv = True
    elif type(base) is TmpFraction:
        base_is_int = base.is_int()
        support_floordiv = False
    else:
        base_is_int = base.denominator == 1
        support_floordiv = True

    pows = [base]
        # [pows[i] == base**2**i]
    y_ = y0
    while not y_ <= pows[-1]:
        pows.append(pows[-1]**2)
    e = 0
    while pows:
        w = pows.pop()
            # [w == base**2**len(pows)]
        if y_ >= w:
            e += 1 << len(pows)
            if base_is_int and support_floordiv:
                y_ = y_//w
            else:
                y_ = y_/w
            assert y_ < w
        #assert y_ < w
    y_
    y0
    #assert 1 <= y0/base**e < base
        # [base**e <= y0 < base**(e+1)]
    def calc__y_remain(e, y_, /):
        if base_is_int:
            y_remain = y0/base**e
        else:
            y_remain = y_
        return y_remain

    if y_ == 1:
        y_remain = calc__y_remain(e, y_)
        exact = y_remain == 1
    else:
        exact = False
    exact

    if with_remain:
        if y_ == 1:
            y_remain # ok
        else:
            y_remain = calc__y_remain(e, y_)
    else:
        y_remain = None

    return (e, exact, y_remain)

def _2fr(x, /):
    (NNN, DDD) = x.as_integer_ratio()
    return Fraction(x)
def main4continued_fraction_of_log_(base, y, /, *, may_args4islice=None, _debug=False, _guess_first=False, _express_fraction_by_coprime_factors=False, _using_continued_fraction_as_input4log=False):
    it = continued_fraction_of_log_(base, y, _debug=_debug, _guess_first=_guess_first, _express_fraction_by_coprime_factors=_express_fraction_by_coprime_factors, _using_continued_fraction_as_input4log=_using_continued_fraction_as_input4log)
    if may_args4islice:
        it = apply_may_args4islice_(may_args4islice, it)
    return it
def continued_fraction_of_log_(base, y, /, *, _debug=False, _guess_first=False, _express_fraction_by_coprime_factors=False, _using_continued_fraction_as_input4log=False):
    r'''[[[
[continued_fraction_of_log_(b; y) =[def]= continued_fraction_of(log_(b; y))]
    [b**x == y]
    [x == log_(b; y)]
    [continued_fraction_of(x) == continued_fraction_of_log_(b; y)]

continued_fraction_of_log_ b y
    | y <= 0 = _L
    | b <= 0 = _L
    | b == 1 = _L
    | y == 1 = [0;] # ===0

    # [b > 0][b =!= 1][y > 0][y =!= 1]
    | b < 1 = continued_fraction_of_log_(1/b, 1/y)
        !! [[b**x == y] <-> [(1/b)**x == 1/y]]
    # [b > 1][y > 0][y =!= 1]
    | y < 1 = -continued_fraction_of_log_(b, 1/y)
        !! [[b**x == y] <-> [b**(-x) == 1/y]]

    # [b > 1][y > 1]
    | otherwise = cf0 : if _b == 1 then [] else continued_fraction_of_log_(_b; b) where
        cf0 = floor_log_(b;y)
        _b = (y/b**cf0)
        #####
        !! [cf0 := floor_log_(b;y)]
        !! [b > 1]
        [b**cf0 <= y < b**(cf0+1)]
        [1 <= y/b**cf0 < b]
        [b**x == y]:
            [b**(x-cf0) == y/b**cf0]
            !! [1 <= y/b**cf0 < b]
            [1 <= b**(x-cf0) < b]
            !! [b > 1]
            [0 <= (x-cf0) < 1.0]
            !! [1 <= y/b**cf0 < b]
            * [(y/b**cf0) == 1]:
                [(x-cf0) == 0.0]
                [x == cf0] #continued_fraction is finite.
                [x == cf([cf0;])]
                [x == cf([cf0; +oo, ...])]
            * [1 < (y/b**cf0) < b]:
                [0 <= (x-cf0) < 1]
                [1/(x-cf0) > 1.0]
                [b == (y/b**cf0) ** (1/(x-cf0))]
                [(1/(x-cf0)) == log_((y/b**cf0); b)]
                [x == cf([cf0; *recur~continued_fraction_of_log_((y/b**cf0); b)])]
                    #NOTE:  [1 < y/b**cf0 < b]


    #]]]'''#'''
    if _using_continued_fraction_as_input4log:
        if _express_fraction_by_coprime_factors and _using_continued_fraction_as_input4log: raise TypeError
        base = ContinuedFraction(base)
        y = ContinuedFraction(y)
    else:
        base = Fraction(base)
        y = Fraction(y)
        if _express_fraction_by_coprime_factors:
            def __(base, y, /):
                if not base > 0:raise TypeError
                if not y > 0:raise TypeError
                idx2factor, idx2exp__lsls = semi_factor_coprimess_via_gcd([base.as_integer_ratio(), y.as_integer_ratio()])
                T = TmpFraction
                _1 = T(idx2factor, None, None)
                [(N0, D0), (N1, D1)] = [[_1._mk(idx2exp) for idx2exp in idx2exp__ls] for idx2exp__ls in idx2exp__lsls]
                base = N0/D0
                y = N1/D1
                return base, y
            base, y = __(base, y)
    #end



    #_floor_log_ = floor_log__Fraction_
    _floor_log_ = floor_log_ex_
    if 1:
        # first_round:
        (cf0, exact, y_remain) = _floor_log_(base, y, _guess_first=_guess_first, with_remain=True)
        # [base**cf0 <= y < base**(cf0+1)] or [base**cf0 >= y > base**(cf0+1)]
        # [1 <= y/base**cf0 == y_remain < base] or [1 >= y/base**cf0 == y_remain > base]
        if _debug:
            yield cf0, (base, y)
        else:
            yield cf0
        # [1 <= y_remain < base] or [1 >= y_remain > base]
        if exact:
            # [1 == y_remain < base] or [1 == y_remain > base]
            pass # <==> yield +oo
            return
        # [1 < y_remain < base] or [1 > y_remain > base]
        _b = y_remain
        # [1 < _b < base] or [1 > _b > base]

        if base < 1:
            base = 1/base
            _b = 1/_b
        # [1 < _b < base]
        base, y = _b, base
        # [1 < base < y]
        # [base > 1][y > 1]
    # [base > 1][y > 1]




    # [base > 1][y > 1]
    _floor_log_ = _floor_log_ex__gt1_
    while 1:
        # [base > 1][y > 1]
        (cf0, exact, y_remain) = _floor_log_(base, y, _guess_first=_guess_first, with_remain=True)
        # [base**cf0 <= y < base**(cf0+1)]
        # [1 <= y/base**cf0 == y_remain < base]
        if _debug:
            yield cf0, (base, y)
        else:
            yield cf0
        if 0:
            _b = (y/base**cf0)
            # [1 <= _b < base]
            if _b == 1:
                pass # <==> yield +oo
                return
            # [1 < _b < base]
        else:
            # [1 <= y_remain < base]
            if exact:
                # [1 == y_remain < base]
                pass # <==> yield +oo
                return
            # [1 < y_remain < base]
            _b = y_remain
            # [1 < _b < base]

        # [1 < _b < base]
        base, y = _b, base
        # [1 < base < y]
        # [base > 1][y > 1]
    return


def iter_approximate_fractions5continued_fraction_of_log_(base, y, /, *, may_max1_denominator=None, le_vs_any_vs_ge=0):
    '[max1_denominator >= 2] => [fst is (cf0,1)]'
    cf_digits = continued_fraction_of_log_(base, y)
    #it = iter_approximate_fractions5continued_fraction_(cf_digits)
    it = iter_approximate_fractions5continued_fraction__by_limit_denominator_(may_max1_denominator, cf_digits, le_vs_any_vs_ge=le_vs_any_vs_ge)
    return it
def iter_approximate_fractions_le5continued_fraction_of_log_(base, y, /, *, may_max1_denominator=None):
    '[max1_denominator >= 2] => [fst is (cf0,1)]'
    return iter_approximate_fractions5continued_fraction_of_log_(base, y, may_max1_denominator=may_max1_denominator, le_vs_any_vs_ge=-1)
    #bug:when finite cf!
    it = iter_approximate_fractions5continued_fraction_of_log_(base, y, may_max1_denominator=may_max1_denominator)
    it = islice(it, 0, None, 2)
    return it
def iter_approximate_fractions_ge5continued_fraction_of_log_(base, y, /, *, may_max1_denominator=None):
    'output may be empty'
    return iter_approximate_fractions5continued_fraction_of_log_(base, y, may_max1_denominator=may_max1_denominator, le_vs_any_vs_ge=+1)
    #bug:when finite cf!
    it = iter_approximate_fractions5continued_fraction_of_log_(base, y, may_max1_denominator=may_max1_denominator)
    it = islice(it, 1, None, 2)
    return it

def approximate_fraction_le5continued_fraction_of_log_(max1_denominator, base, y, /):
    '->Fraction|^ContinuedFractionError__inf__no_cf0' '  #no 『ge』-version'
    check_int_ge(2, max1_denominator)
    cf_digits = continued_fraction_of_log_(base, y)
    return approximate_fraction5continued_fraction__by_limit_denominator_(max1_denominator, cf_digits, le_vs_any_vs_ge=-1)

    it = iter_approximate_fractions_le5continued_fraction_of_log_(base, y, may_max1_denominator=max1_denominator)
        # ^ContinuedFractionError__inf__no_cf0
    for fr in it:
        # at least (cf0, 1)
        pass
    return fr

__all__


from seed.math.continued_fraction.continued_fraction_of_log_ import continued_fraction_of_log_
from seed.math.continued_fraction.continued_fraction_of_log_ import floor_log__Fraction_

from seed.math.continued_fraction.continued_fraction_of_log_ import *
