__all__ = ['CalcCompleteNormalBlockSizeBase']

from abc import ABC, abstractmethod
from itertools import count
from math import *
from .CalcCompleteSuperBlockSizeBase import CalcCompleteSuperBlockSizeBase
from .common_methods import floor_log2, ceil_log2

class CalcCompleteNormalBlockSizeBase(CalcCompleteSuperBlockSizeBase):
    '''to calc min_array_length, delta_y__upper_bound, complete_normal_block_size

1) min_array_length = calc_min_array_length()
2) delta_y__upper_bound = calc_delta_y__upper_bound(min_array_length)
3) complete_normal_block_size = calc_complete_normal_block_size(array_length)
see:
    .calc_min_array_length_and_delta_y__upper_bound
    .calc_complete_normal_block_size

see: "rmq - 2.1.2. complete_normal_block_size.txt"
    :: complete_normal_block_size__ver2

see: "rmq - 2.1.1. complete_super_block_size.txt"
    :: min_array_length
'''

    min_array_length__at_least5 = 5
    @classmethod
    def calc_complete_normal_block_size(cls, array_length):
        '''

def complete_normal_block_size__ver2(p) # use int operation only
    # black era
    | p < min_array_length__at_least5  = 1 # may >= log2(p)/2
    # white era: s < log2(p)/2
    | p == 2**(2*half_power)= log2(p)/2 - 1 = floor_log2(p)//2-1
    | otherwise             = floor_log2(p)//2
    #   p == 2**(2*half_power)-1 ==>> half_power-1
    #   p == 2**(2*half_power)   ==>> half_power-1 # seems useless
    #   p == 2**(2*half_power)+1 ==>> half_power
'''
        assert array_length >= 1
        p = array_length
        if p < cls.min_array_length__at_least5:
            return 1
        pseudo_power = floor_log2(p)
        if not (pseudo_power & 1):
            # even
            ceil_power = ceil_log2(p)
            if ceil_power == pseudo_power:
                # p == 2**(2*half_power)
                power = pseudo_power
                return power//2 -1
            else:
                pass
        return pseudo_power//2
        raise NotImplementedError
    @classmethod
    def calc_delta_y__upper_bound(cls, min_array_length):
        '''
def delta_y__upper_bound(min_array_length):
    # "?" a small number
    = ? + max {delta_y(p) | p <- [min_array_length..]}
    = delta_y__upper_bound__at_least__p_ge(min_array_length)
'''
        return cls.delta_y__upper_bound__at_least__p_ge(min_array_length)
    @classmethod
    def delta_y__upper_bound__at_least__p_ge(cls, min_array_length):
        '''
==>> delta_y__upper_bound__at_least__p_ge(min_array_length)
    # = ? + max {delta_y(p) | p <- [min_array_length..]}
    # min_array_length >= min_array_length__at_least5
    = max(delta_y__upper_bound__at_least1(min_array_length)
        , delta_y__upper_bound__at_least2(min_array_length)
        )
    = delta_y__upper_bound__at_least2(min_array_length)
    = 4/(log2(min_array_length)-2)
'''
        return 4/(log2(min_array_length)-2)

    @classmethod
    def calc_min_array_length_and_delta_y__upper_bound(cls, *, print=print, begin=0, N=20):
        print(f'calc_min_array_length_and_delta_y__upper_bound()')
        ver = cls.get_version()
        print(f'# super block size ver={ver}')
        min_array_length = cls.calc_min_array_length(print=print, begin=begin)
        delta_y__upper_bound = cls.calc_delta_y__upper_bound(min_array_length)

        print()
        print(min_array_length, delta_y__upper_bound)
        print()

        for p in range(min_array_length, min_array_length+N):
            at_least = cls.delta_y__upper_bound__at_least__p_ge(p)
            print('\t', end='')
            print(p, at_least)
        return min_array_length

'''

calc_complete_normal_block_size(begin=1)
array_length, complete_normal_block_size__ver1, ...ver2
1 1 1
2 1 1
3 1 1
4 1 1
5 1 1
6 1 1
7 1 1
8 1 1
9 1 1
10 1 1
11 1 1
12 1 1
13 1 1
14 1 1
15 1 1
16 1 1
17 2 2
18 2 2
19 2 2
20 2 2
21 2 2
22 2 2
23 2 2
24 2 2
25 2 2
26 2 2
27 2 2
28 2 2
29 2 2
30 2 2
31 2 2
32 2 2
33 2 2
34 2 2
35 2 2
36 2 2
37 2 2
38 2 2
39 2 2
40 2 2
41 2 2
42 2 2
43 2 2
44 2 2
45 2 2
46 2 2
47 2 2
48 2 2
49 2 2
50 2 2
51 2 2
52 2 2
53 2 2
54 2 2
55 2 2
56 2 2
57 2 2
58 2 2
59 2 2
60 2 2
61 2 2
62 2 2
63 2 2
64 2 2
65 3 3
66 3 3
67 3 3
68 3 3
69 3 3
70 3 3
71 3 3
72 3 3
73 3 3
74 3 3
75 3 3
76 3 3
77 3 3
78 3 3
79 3 3
80 3 3
81 3 3
82 3 3
83 3 3
84 3 3
85 3 3
86 3 3
87 3 3
88 3 3
89 3 3
90 3 3
91 3 3
92 3 3
93 3 3
94 3 3
95 3 3
96 3 3
97 3 3
98 3 3
99 3 3
100 3 3




calc_min_array_length_and_delta_y__upper_bound()
# super block size ver=1
array_length p, at_least, at_most
36 0.21526934279162502 0.18127101772032317
37 0.21278473726672908 0.18780536858289398
38 0.21041509779171141 0.19418097879084595
39 0.20815189339169127 0.2004050919669922
40 0.20598744524062695 0.20648448825713883

40 1.2041199826559246

        40 1.2041199826559246
        41 1.191344168161289
        42 1.1791349397732558
        43 1.1674521049520548
        44 1.1562593052715515
        45 1.145523562891132
        46 1.1352148904672978
        47 1.125305954333409
        48 1.1157717826045195
        49 1.1065895113302244
        50 1.0977381630001413
        51 1.0891984526641596
        52 1.0809526177092788
        53 1.0729842679727137
        54 1.0652782533951561
        55 1.0578205468507365
        56 1.0505981401487743
        57 1.043598951500745
        58 1.0368117429950512
        59 1.0302260468310234




calc_min_array_length_and_delta_y__upper_bound()
# super block size ver=2
array_length p, at_least, at_most
17 0.041288477572514574 0.012333370161017765
18 0.039160433215079095 0.024214373792442956
19 0.03728921674321343 0.03565778879914383
20 0.03563021895229108 0.04668235020234146

20 1.722706232293572

        20 1.722706232293572
        21 1.6720189227037687
        22 1.6263920369602667
        23 1.5850611435947763
        24 1.5474112289381665
        25 1.5129415947320604
        26 1.4812402488115854
        27 1.4519649157574384
        28 1.424828748432089
        29 1.39958943282667
        30 1.3760407791207752
        31 1.3540061592847121
        32 1.3333333333333333
        33 1.3138903319268407
        34 1.2955621510832849
        35 1.278248077383902
        36 1.261859507142915
        37 1.246318155869552
        38 1.2315545785561688
        39 1.217506939343707
'''
