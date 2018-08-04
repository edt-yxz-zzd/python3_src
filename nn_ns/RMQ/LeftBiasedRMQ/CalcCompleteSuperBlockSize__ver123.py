
__all__ = '''
    CalcCompleteSuperBlockSize_Ver1
    CalcCompleteSuperBlockSize_Ver2
    '''.split()

# complete_super_block_size
from .common_methods import floor_log2
from .CalcCompleteSuperBlockSizeBase import CalcCompleteSuperBlockSizeBase
from itertools import count
from math import ceil, floor, log, log2

class CalcCompleteSuperBlockSize_Ver1(CalcCompleteSuperBlockSizeBase):
    @classmethod
    def get_version(cls):
        return 1
    @classmethod
    def get_min_array_length__at_least__from123xxx(cls):
        min_array_length__at_least__from1234__ver1 = max(
            cls.min_array_length__at_least1
            ,cls.min_array_length__at_least2
            ,cls.min_array_length__at_least3
            ,cls.min_array_length__at_least4
            #, 65880
            )
        return min_array_length__at_least__from1234__ver1
    @classmethod
    def delta_x__upper_bound_at_least2__p_ge(cls, min_array_length):
        '''
delta_x__upper_bound_at_least2__p_ge__ver1(min_array_length)
    # donot care whether min_array_length == 2**power
    = 2*log<log2(min_array_length)>(1+1/log2(min_array_length))
'''
        min_b = log2(min_array_length)
        return -2 + 2*log(1+min_b, min_b)



    @classmethod
    def calc_complete_super_block_size(cls, array_length):
        '''
    # calc:
    def complete_super_block_size__ver1_int(p) # use int operation only
        # require: min_array_length >= min_array_length__at_least4 == 36
            ## black era
            #| p < min_array_length__at_least3   = p # may <= log2(p)**2
            #| p < min_array_length__at_least4   = p # may < ceil_log2(p)**2
        | p < min_array_length  = undefined # use other method to do RMQ
        | p == 2**power         = log2(p)**2 + 1 = ceil_log2(p)**2 + 1
        | p >= min_array_length = ceil_log2(p)**2 = (floor_log2(p)+1)**2
'''
        assert array_length >= 1
        p = array_length
        if p < cls.min_array_length__at_least4:
            return p
        pseudo_power = floor_log2(p)
        if (1 << pseudo_power) == p:
            # p == 2**power
            power = pseudo_power
            return power**2 + 1
        # p != 2**power
        # ceil_log2_p = floor_log2_p + 1 = pseudo_power + 1
        ceil_log2_p = pseudo_power + 1
        return ceil_log2_p**2

class CalcCompleteSuperBlockSize_Ver2(CalcCompleteSuperBlockSizeBase):
    @classmethod
    def get_version(cls):
        return 2
    @classmethod
    def get_min_array_length__at_least__from123xxx(cls):
        min_array_length__at_least__from123__ver2 = max(
            cls.min_array_length__at_least1
            ,cls.min_array_length__at_least2
            ,cls.min_array_length__at_least3
            #, 65880
            )
        return min_array_length__at_least__from123__ver2
    @classmethod
    def delta_x__upper_bound_at_least2__p_ge(cls, min_array_length):
        '''
delta_x__upper_bound_at_least2__p_ge__ver2(min_array_length)
    # donot care whether min_array_length == 2**power
    = log<log2(min_array_length)>(1+1/log2(min_array_length)**2)
'''
        lp = log2(min_array_length)
        return log(1+1/lp**2, lp)


    @classmethod
    def calc_complete_super_block_size(cls, array_length):
        '''
    # rewrite complete_super_block_size__ver3_float
    # calc:
    def complete_super_block_size__ver3_float(p) # use float operation
        # black era
        | p < min_array_length__at_least3   = p # may <= log2(p)**2

        # using ver1 definition
        # p >= min_array_length__at_least3
        #   log2(p)**2 <= ceil(log2(p)**2) <= s_ <= p
        #
        #   delta_x(p) <= MOST(p)
        #   delta_x(p) <= LEAST(p)
        #   [p < min_array_length] or [delta_x(p) <= MOST(min_array_length)]
        #
        #   white era: p < min_array_length
        #       LEAST(p) >= MOST(p)
        #   golden era: p >= min_array_length
        #       [LEAST(p) <= LEAST(min_array_length) < MOST(min_array_length) <= MOST(p)]
        #       NOTE: MOST(min_array_length) is the constant
        #
        | p == 2**power         = log2(p)**2 + 1    = floor(log2(p)**2)+1
        | p >= min_array_length = ceil(log2(p)**2)  = floor(log2(p)**2)+1
'''
        assert array_length >= 1
        p = array_length
        if p < cls.min_array_length__at_least3:
            return p
        return floor(log2(p)**2)+1


def calc_complete_super_block_size(*, print=print, begin=17, size=100):
    assert begin > 0
    assert size >= 0
    C1 = CalcCompleteSuperBlockSize_Ver1
    C2 = CalcCompleteSuperBlockSize_Ver2
    print(f'calc_complete_super_block_size(begin={begin})')
    print('array_length, complete_super_block_size__ver1, ...ver2')
    for p in range(begin, begin+size):
        s1 = C1.calc_complete_super_block_size(p)
        s2 = C2.calc_complete_super_block_size(p)
        print(p, s1, s2)
    '''
calc_complete_super_block_size(begin=17)
17 17 17
18 18 18
19 19 19
20 20 19
21 21 20
22 22 20
23 23 21
24 24 22
25 25 22
26 26 23
27 27 23
28 28 24
29 29 24
30 30 25
31 31 25
32 32 26
33 33 26
34 34 26
35 35 27
36 36 27
37 36 28
38 36 28
39 36 28
40 36 29
41 36 29
42 36 30
43 36 30
44 36 30
45 36 31
46 36 31
47 36 31
48 36 32
49 36 32
50 36 32
51 36 33
52 36 33
53 36 33
54 36 34
55 36 34
56 36 34
57 36 35
58 36 35
59 36 35
60 36 35
61 36 36
62 36 36
63 36 36
64 37 37
65 49 37
66 49 37
67 49 37
68 49 38
69 49 38
70 49 38
71 49 38
'''



def calc_min_array_length_and_delta_x__upper_bound():
    CalcCompleteSuperBlockSize_Ver1.calc_min_array_length_and_delta_x__upper_bound()
    print('\n'*3)
    CalcCompleteSuperBlockSize_Ver2.calc_min_array_length_and_delta_x__upper_bound()

    '''
calc_min_array_length_and_delta_x__upper_bound(ver = 1)
array_length p, at_least, at_most
36 0.21526934279162502 0.18127101772032317
37 0.21278473726672908 0.18780536858289398
38 0.21041509779171141 0.19418097879084595
39 0.20815189339169127 0.2004050919669922
40 0.20598744524062695 0.20648448825713883

40 0.20598744524062695

        40 0.20598744524062695 0.20648448825713883 0.0024129772371868086
        41 0.20391482108681735 0.2124255206178578 0.04173654217815281
        42 0.20192774514319645 0.21823414798199892 0.08075365189285333
        43 0.20002052084693656 0.22391596555153903 0.1194649659116136
        44 0.19818796438101316 0.22947623246032745 0.15787168598776824
        45 0.19642534723731186 0.2349198970371229 0.1959754702803389
        46 0.19472834640945047 0.24025161988442179 0.23377836003008334
        47 0.19309300105098703 0.24547579497244065 0.2712827168066114
        48 0.191515674634279 0.2505965689312828 0.30849116872457305
        49 0.1899930218070538 0.2556178587083662 0.3454065642892783
        50 0.18852195927556759 0.26054336774303444 0.3820319327479047
        51 0.18709964015107783 0.2653766007960505 0.41837045000068507
        52 0.1857234312850813 0.2701208775585755 0.45442540927399744
        53 0.18439089319198088 0.2747793451531786 0.49020019588000285
        54 0.18309976221856994 0.27935498962847216 0.5256982654898283
        55 0.18184793467026772 0.28385064653902825 0.5609231254328788
        56 0.18063345264626252 0.2882690106932375 0.595878318606684
        57 0.17945449137114444 0.29261264514368523 0.630567409642087
        58 0.17830934784039565 0.29688398948732386 0.6649939730196543
        59 0.17719643062227908 0.3010853675361673 0.6991615828762161




calc_min_array_length_and_delta_x__upper_bound(ver = 2)
array_length p, at_least, at_most
17 0.041288477572514574 0.012333370161017765
18 0.039160433215079095 0.024214373792442956
19 0.03728921674321343 0.03565778879914383
20 0.03563021895229108 0.04668235020234146

20 0.03563021895229108

        20 0.03563021895229108 0.04668235020234146 0.3101898213100853
        21 0.034148612268654475 0.05730857109781917 0.6782108346588236
        22 0.03281681271119002 0.06755744272390407 1.0586229174190351
        23 0.03161269156904039 0.07744966761386474 1.4499548684337396
        24 0.030518291049978646 0.08700521986990184 1.85092044398609
        25 0.029518885933210004 0.09624310759131793 2.2603909174986967
        26 0.028602287328081337 0.10518126042353337 2.677372344982628
        27 0.02775831877368218 0.11383649413800345 3.1009866291301647
        28 0.026978416947785334 0.12222452193580224 3.530455666555916
        29 0.02625532376633781 0.13035999325696324 3.965088010992231
        30 0.025582846391400273 0.13825654788029906 4.404267600448646
        31 0.024955668308818058 0.14592687756606715 4.847444186237403
        32 0.024369199240475363 0.15338279036696534 5.294125172246462
        33 0.023819454891947728 0.16063527459096072 5.74386862838176
        34 0.023302959841262565 0.16769456060442822 6.1962772860935615
        35 0.022816668536462883 0.17457017944530362 6.650993358926451
        36 0.02235790058182313 0.18127101772032317 7.107694059060968
        37 0.021924287386106914 0.18780536858289398 7.566087703352373
        38 0.021513727911514745 0.19418097879084595 8.025910320587204
        39 0.02112435176191722 0.2004050919669922 8.486922686464661
'''


if '__main__' == __name__:
    calc_complete_super_block_size()
    print('\n'*3)
    calc_min_array_length_and_delta_x__upper_bound()

