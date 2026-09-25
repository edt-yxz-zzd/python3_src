#__all__:goto
r'''[[[
e ../../python3_src/seed/math/pseudo_random.py
pseudo-random number generator

seed.math.pseudo_random
py -m nn_ns.app.debug_cmd   seed.math.pseudo_random -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.pseudo_random:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/factor_pint/factor_pint__elliptic_curve_method.py
view ../../python3_src/pari_gp_script/polynomial7primitive7finite_field.gp.out.txt
]]


'#'; __doc__ = r'#'
#>>> f = lambda rn,sz:f'{rn.getrandbits(sz):0>{sz}b}'
>>> f = lambda rn,sz:uint2sized_binstr_(sz, rn.getrandbits(sz))

>>> PseudoRandom7linear__M127__mid126.exps4binary_primitive_polynomial
(127, 126, 0)
>>> PseudoRandom7linear__M127__mid001.exps4binary_primitive_polynomial
(127, 1, 0)
>>> PseudoRandom7linear__M127.deg4binary_primitive_polynomial
127
>>> bin(PseudoRandom7linear__M127.mul_order4binary_primitive_polynomial)
'0b1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
>>> bin(PseudoRandom7linear__M127__mid126.feedback_mask4binary_primitive_polynomial)
'0b1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001'
>>> bin(PseudoRandom7linear__M127__mid001.feedback_mask4binary_primitive_polynomial)
'0b1100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

>>> rn = PseudoRandom7linear__M127(1, assumption7independent=False)
>>> rn
PseudoRandom7linear__M127__mid126(1, assumption7independent = False)
>>> bin(rn.getrandbits(32))
'0b11111111111111111111111111111111'
>>> rn.random()
0.9999999999999998
>>> rn.random()
0.9996744791666665
>>> rn.random()
0.6666666666666665
>>> rn.random()
0.5999999999999999
>>> rn.random()
0.6000651041666665
>>> f(PseudoRandom7linear__M127(1, assumption7independent=False), 67)
'1111111111111111111111111111111111111111111111111111111111111111111'
>>> f(PseudoRandom7linear__M127(1, assumption7independent=False), 130)
'1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111010'


>>> rn = PseudoRandom7linear__M127(1, assumption7independent=True)
>>> rn
PseudoRandom7linear__M127__mid126(1, assumption7independent = True)
>>> bin(rn.getrandbits(32))
'0b0'
>>> rn.random()
1.5522028107284314e-10
>>> rn.random()
0.6669921874999241
>>> rn.random()
0.6666666666666665
>>> rn.random()
0.2857157389322915
>>> rn.random()
0.9332682291666665


>>> bin(PseudoRandom7linear__M127(1, assumption7independent=True).getrandbits(64))
'0b0'
>>> bin(PseudoRandom7linear__M127(1, assumption7independent=True).getrandbits(67))
'0b101'
>>> bin(PseudoRandom7linear__M127(1, assumption7independent=True).getrandbits(128))
'0b1010101010101010101010101010101010101010101010101010101010101011'
>>> f(PseudoRandom7linear__M127(1, assumption7independent=True), 67)
'0000000000000000000000000000000000000000000000000000000000000000101'
>>> f(PseudoRandom7linear__M127(1, assumption7independent=True), 128)
'00000000000000000000000000000000000000000000000000000000000000001010101010101010101010101010101010101010101010101010101010101011'
>>> f(PseudoRandom7linear__M127(1, assumption7independent=True), 512)
'00000000000000000000000000000000000000000000000000000000000000001010101010101010101010101010101010101010101010101010101010101011111111111111111111111111111111101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010010010010010010010010010010010010010010010010010101010101010101010101010101010101010101010101011101110111011101110111011101110101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010001010001010001010001010001010001010'





###################################
!!!!!!!!!!!!!!!!bug!!!!!!!!!!!!!!!!
###################################
>>> f(PseudoRandom7linear__M127__mid001(1, assumption7independent=True), 512)
'00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
>>> f(PseudoRandom7linear__M127__mid001(1, assumption7independent=False), 512)
'10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010001000'






###########################
_uniform_next_b_u_() => M5.period only 16! # [2 ~= (-1+2**5)/16]
    0110110000100
>>> f(PseudoRandom7linear__M5(1, assumption7independent=True), 128)
'01101100001001110110110000100111011011000010011101101100001001110110110000100111011011000010011101101100001001110110110000100111'

_uniform_next_b_u_() => M6.period only 32! # [2 ~= (-1+2**6)/32]
    11111
>>> f(_PseudoRandom7linear__M6(1, assumption7independent=True), 128)
'01000100010110100011111011001110010001000101101000111110110011100100010001011010001111101100111001000100010110100011111011001110'


_uniform_next_b_u_() => M7.period only 64! # [2 ~= (-1+2**7)/64]
    11111111
>>> f(PseudoRandom7linear__M7(1, assumption7independent=True), 128)
'00001011101010010100110001000100010011110001101011001100111111110000101110101001010011000100010001001111000110101100110011111111'


###########################
_raw_next_b_u_() => M5.period == 31 == (-1+2**5)
    0000
>>> f(PseudoRandom7linear__M5(1, assumption7independent=False), 128)
'10010110011111000110111010100001001011001111100011011101010000100101100111110001101110101000010010110011111000110111010100001001'
>>> PseudoRandom7linear__M5.exps4binary_primitive_polynomial
(5, 2, 0)
>>> PseudoRandom7linear__M5.deg4binary_primitive_polynomial
5
>>> PseudoRandom7linear__M5.mul_order4binary_primitive_polynomial
31
>>> PseudoRandom7linear__M5.feedback_mask4binary_primitive_polynomial
20


###########################

>>> _count_period_(+5, assumption7independent=False)
31
>>> _count_period_(+7, assumption7independent=False)
127
>>> _count_period_(13, assumption7independent=False)
8191
>>> _count_period_(17, assumption7independent=False) #doctest: +SKIP
131071
>>> _count_period_(19, assumption7independent=False) #doctest: +SKIP
524287


###########################

>>> _count_period_(+5, assumption7independent=True)
16
>>> _count_period_(+7, assumption7independent=True)
64
>>> _count_period_(13, assumption7independent=True)
4096
>>> _count_period_(17, assumption7independent=True) #doctest: +SKIP
65536
>>> _count_period_(19, assumption7independent=True) #doctest: +SKIP
262144


###########################
>>> PseudoRandom7linear(8, 1, assumption7independent=False)
PseudoRandom7linear((8, 4, 3, 2, 0), 1, assumption7independent = False)
>>> f(PseudoRandom7linear(8, 1, assumption7independent=False), 512)
'10001110001001011100000011001001001101110010000010101101101011001011000011111011011110101110100010000110110001111001110011000101101001000101001010100111011101100111101111110100110011010100011000001110101010111110010100001001111111100001011110001101000000010001110001001011100000011001001001101110010000010101101101011001011000011111011011110101110100010000110110001111001110011000101101001000101001010100111011101100111101111110100110011010100011000001110101010111110010100001001111111100001011110001101000000010'

>>> PseudoRandom7linear(8, 1, assumption7independent=True)
PseudoRandom7linear((8, 4, 3, 2, 0), 1, assumption7independent = True)
>>> f(PseudoRandom7linear(8, 1, assumption7independent=True), 512)
'00011011000100001000001010111001110001110101111000000110101101111001010100111101101101101111100100100011100100101000111110010100000110110001000010000010101110011100011101011110000001101011011110010101001111011011011011111001001000111001001010001111100101000001101100010000100000101011100111000111010111100000011010110111100101010011110110110110111110010010001110010010100011111001010000011011000100001000001010111001110001110101111000000110101101111001010100111101101101101111100100100011100100101000111110010100'































[[
py_adhoc_call   seed.math.pseudo_random   @_test_M127__mid001_ +assumption7independent =256
py_adhoc_call   seed.math.pseudo_random   @_test_M127__mid001_ +assumption7independent =2
    000'
py_adhoc_call   seed.math.pseudo_random   @_test_M127__mid001_ +assumption7independent =2 =5
    000'
py_adhoc_call   seed.math.pseudo_random   @_test_M127__mid001_ +assumption7independent =2 =127605887595351923798765477786913079298
    '11'
        # "5"后继，错位1，
py_adhoc_call   seed.math.pseudo_random   @_test_M127__mid001_ +assumption7independent =130 =127605887595351923798765477786913079298
    '1101110101111101110101111101011111010101011111111101110101111101011111010101011111111101011111010101011111111101010101111111110101'
        # 所以是 初始状态 非法？大概有一半非法？
        #   但M5版并无此现象
]]

[[
py_adhoc_call   seed.math.pseudo_random   @_count_period_ +assumption7independent =5 =2
py_adhoc_call   seed.math.pseudo_random   @_count_period_ +assumption7independent =5
    16
py_adhoc_call   seed.math.pseudo_random   @_count_period_ +assumption7independent =7
    64
py_adhoc_call   seed.math.pseudo_random   @_count_period_ +assumption7independent =13
    4096
py_adhoc_call   seed.math.pseudo_random   @_count_period_ +assumption7independent =17
    65536
py_adhoc_call   seed.math.pseudo_random   @_count_period_ +assumption7independent =19
    262144


py_adhoc_call   seed.math.pseudo_random   @_count_period_ -assumption7independent =5
    31
py_adhoc_call   seed.math.pseudo_random   @_count_period_ -assumption7independent =7
    127
py_adhoc_call   seed.math.pseudo_random   @_count_period_ -assumption7independent =13
    8191
py_adhoc_call   seed.math.pseudo_random   @_count_period_ -assumption7independent =17
    131071
py_adhoc_call   seed.math.pseudo_random   @_count_period_ -assumption7independent =19
    524287

]]

py_adhoc_call   seed.math.pseudo_random   @f
from seed.math.pseudo_random import *
]]]'''#'''
__all__ = r'''
IPseudoRandom7linear
    PseudoRandom7linear
    PseudoRandom7linear__M5
    PseudoRandom7linear__M7
    PseudoRandom7linear__M13
    PseudoRandom7linear__M17
    PseudoRandom7linear__M19
    PseudoRandom7linear__M31
    PseudoRandom7linear__M61
    PseudoRandom7linear__M89
    PseudoRandom7linear__M107
    PseudoRandom7linear__M127__mid126
        PseudoRandom7linear__M127
    PseudoRandom7linear__M127__mid001
    PseudoRandom7linear__M521
    PseudoRandom7linear__M607
    PseudoRandom7linear__M1279
    PseudoRandom7linear__M2203
    PseudoRandom7linear__M2281



uint5bits_
uint2sized_binstr_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from random import Random
from abc import abstractmethod
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge, check_int_ge_le
    from seed.helper.repr_input import repr_helper
    from seed.types.CachedProperty import CachedProperty# mk_cached_propertyT_
    from seed.debug.print_err import print_err
    from seed.tiny_.containers import mk_immutable_seq
#.    from itertools import islice
with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
    from seed.math.polynomial.binary_primitive_polynomial import deg2neg_or_list4exps4binary_primitive_polynomial

#.#################################
___end_mark_of_excluded_global_names__0___ = ...


_debug = False
#_zpow1024 = 1<<1024
_inv_zpow32 = 0.5**32 # == 2.0**-32
_inv_zpow52 = 0.5**52 # == 2.0**-52
def uint5bits_(bits, /):
    'big_endian'
    return int(''.join('01'[bool(b)] for b in bits), 2)
    return int(''.join(map(str, bits)), 2)
def uint2sized_binstr_(sz, u, /):
    return f'{u:0>{sz}b}'

def _4mask(es, /):
    deg = es[0]
    bits = [0]*deg
    for ez in es[1:]:
        #bug:bits[deg-1-ez] = 1
        bits[ez] = 1
    bits
    return uint5bits_(bits)
def _raw_next_b_u_(mask, u, /):
    b = u&1
    u >>= 1
    if b:
        u ^= mask
    if _debug:print_err('_raw_next_b_u_() ->', (b, u))
    return (b, u)
def _uniform_next_b_u_(mask, u, /):
    while 1:
        (b0, u) = _raw_next_b_u_(mask, u)
        (b1, u) = _raw_next_b_u_(mask, u)
        if not b0 == b1:
            return (b1, u)
class IPseudoRandom7linear(Random):
    '[st :: 1+uint%mul_order][period{assumption7independent;deg} == (2**(-1+deg) if assumption7independent else (-1+2**deg))]'


    #def __new__(cls, may_int_or_state=None, /):
    #    self = super(__class__, cls).__new__(cls)
    def __init__(self, may_int_or_state=None, /, *, assumption7independent:bool):
        self.seed(may_int_or_state)
        self._assumption7independent = bool(assumption7independent)
    @property
    def assumption7independent(self, /):
        return self._assumption7independent
    def __repr__(self, /):
        return repr_helper(self, self.getstate(), assumption7independent=self.assumption7independent)
        if self.assumption7independent:
            return repr_helper(self, self.getstate(), assumption7independent=True)
        return repr_helper(self, self.getstate())
    def __init_subclass__(cls, /, **kwargs):
        super().__init_subclass__(**kwargs)
        es = cls.exps4binary_primitive_polynomial
        if hasattr(type(es), '__len__'):
            deg = es[0]
            check_int_ge(2, deg)
            mul_order = -1+(1<<deg)
            mask = _4mask(es)
            cls.deg4binary_primitive_polynomial = deg
            cls.mul_order4binary_primitive_polynomial = mul_order
            cls.feedback_mask4binary_primitive_polynomial = mask
    @property
    @abstractmethod
    def exps4binary_primitive_polynomial(self, /):
        '-> [uint]{strictly-descending}{len<=1+deg}{len>=3}{len%2==1}{.[-1]==0}{.[0]==deg}'
    #@property
    @CachedProperty
    def deg4binary_primitive_polynomial(self, /):
        '-> int{>=2}'
        #bug:return -1+len(self.exps4binary_primitive_polynomial)
        deg = self.exps4binary_primitive_polynomial[0]
        check_int_ge(2, deg)
        return deg
    @CachedProperty
    def mul_order4binary_primitive_polynomial(self, /):
        '-> mul_order/int{>=1}{==-1+2**deg4binary_primitive_polynomial}{???is_prime_(mul_order)#Mersenne_prime???}'
        deg = self.deg4binary_primitive_polynomial
        return -1+(1<<deg)
    @CachedProperty
    def feedback_mask4binary_primitive_polynomial(self, /):
        '-> uint # bitwise-little_endian'
        return _4mask(self.exps4binary_primitive_polynomial)

    ###########################
    # py_help random:Random
    ###########################
    #@override
    def getrandbits(self, k, /):
        'getrandbits(k) -> x.  Generates an int with k random bits.'
        mask = self.feedback_mask4binary_primitive_polynomial
        _next_b_u_ = _uniform_next_b_u_ if self.assumption7independent else _raw_next_b_u_
        u = self.getstate()
        bits = []
        for _ in range(k):
            (b, u) = _next_b_u_(mask, u)
            bits.append(b)
        u, bits
        self.setstate(u)
        return uint5bits_(bits)
    #@override
    def random(self, /):
        '-> float{>=0.0}{<1.0}'
        # float: exp
        r'''
        >>> math.ulp(0.0)
        5e-324
        >>> 3e-324
        5e-324
        >>> 2e-324
        0.0
        >>> 1e+308
        1e+308
        >>> 2e+308
        inf

        >>> 0.5**1075
        0.0
        >>> 0.5**1074
        5e-324
        >>> (0.5**1074).hex()
        '0x0.0000000000001p-1022'

        >>> 2.0**1024
        Traceback (most recent call last):
            ...
        OverflowError: (34, 'Math result not representable')
        >>> 2.0**1023
        8.98846567431158e+307
        >>> (2.0**1023).hex()
        '0x1.0000000000000p+1023'

        >>> 13*4
        52
        >>> 1074-52
        1022
        >>> 1075//32
        33
        >>> 32*34
        1088

        '''#'''
        #fail:return self.getrandbits(1024)/_zpow1024
        u52 = self.getrandbits(52)
        f52 = float(u52)*_inv_zpow52
        #while f52:
        if not f52:return f52
        for _ in range(34):
            # [0 < f52]
            u32 = self.getrandbits(32)
            if not u32:
                f52 *= _inv_zpow32 # 0.5**32
                if not f52:return f52
                # [0 < f52]
                continue
            # [0 < u32]
            #s32 = f'{u32:0>32b}'
            s32 = uint2sized_binstr_(32, u32)
            # ["1" in s32]
            for b in map(int, s32):
                # [0 < f52]
                if b:return f52
                f52 *= 0.5
                if not f52:return f52
                # [0 < f52]
            # !! ["1" in s32]
            raise 000
        # !! [1075 < 1088 == 32*34]
        raise 000
        return f52

    #@override
    def seed(self, may_int_or_state=None, /):
        #seed(self, a=None, version=2)
        'may (int|st) -> None'
        match may_int_or_state:
            case None:
                rn = Random()
                while not (u := rn.getrandbits(self.deg4binary_primitive_polynomial)):pass
                u
                # [1 <= u < 2**deg4binary_primitive_polynomial]
            case int() as j:
                # !! ???[(self.mul_order4binary_primitive_polynomial) is Mersenne_prime]???
                #bug:u = 1+ j%(self.mul_order4binary_primitive_polynomial)
                #   since: u --> 1+u
                M = (self.mul_order4binary_primitive_polynomial)
                u = j%M
                if u == 0:
                    u = M
                    # u --> u
                # [1 <= u <= mul_order4binary_primitive_polynomial]
                # [1 <= u < 2**deg4binary_primitive_polynomial]
            case bad_seed:
                raise TypeError(bad_seed)
        # [1 <= u < 2**deg4binary_primitive_polynomial]
        u
        self.setstate(u)
    #@override
    def setstate(self, state, /):
        'st -> None'
        check_int_ge_le(1, self.mul_order4binary_primitive_polynomial, state)
        self._st = state
        # [1 <= u < 2**deg4binary_primitive_polynomial]
    #@override
    def getstate(self, /):
        '-> st'
        return self._st

r'''[[[
view ../../python3_src/nn_ns/math_nn/numbers/Mersenne_exponents.py
    3:5
    4:7
    5:13
    6:17
    7:19
    8:31
    9:61
    10:89
    11:107
    12:127
    13:521
    14:607
    15:1279
    16:2203
    17:2281
    18:3217

view ../../python3_src/pari_gp_script/polynomial7primitive7finite_field.gp.out.txt
    [5,2,0]%=%[5,3,2,1,0]
    [6,1,0]%=%[6,4,3,1,0]
    [7,1,0]%=%[7,3,2,1,0]
    [13,4,3,1,0]%=%%empty@deg:13
    [17,3,0]%=%[17,3,2,1,0]
    [19,5,2,1,0]%=%%empty@deg:19
    [31,3,0]%=%[31,3,2,1,0]
    [61,5,2,1,0]%=%%empty@deg:61
    [89,6,5,3,0]%=%%[89,38,0]
    [107,7,5,3,2,1,0]%<[107,9,7,4,0]%%empty@deg:107
    [127,1,0]%=%[127,7,3,1,0]
    [521,9,6,5,3,1,0]%<[521,9,7,2,0]%%[521,32,0]
    [607,9,7,6,3,1,0]%<[607,12,9,7,0]%%[607,105,0]
    [1279,11,9,8,5,3,2,1,0]%<[1279,16,8,3,0]%%[1279,216,0]
    [2203,11,10,6,4,1,0]%<[2203,14,6,5,0]%%empty@deg:2203
    [2281,9,8,7,6,2,0]%<[2281,20,18,4,0]%%[2281,715,0]


#]]]'''#'''


def exps4binary_primitive_polynomial5or_deg_(deg_or_exps4binary_primitive_polynomial, /):
    match deg_or_exps4binary_primitive_polynomial:
        case int() as deg:
            check_int_ge(2, deg)
            match deg2neg_or_list4exps4binary_primitive_polynomial[deg]:
                case int() as neg_deg:
                    assert neg_deg == -deg
                    raise NotImplementedError('unknown factorization of (-1+2**deg) : ', deg)
                case ess:
                    es = ess[0]
            es
        case es:
            pass
    es
    es = mk_immutable_seq(es)
    return es
class PseudoRandom7linear(IPseudoRandom7linear):
    def __init__(self, deg_or_exps4binary_primitive_polynomial, may_int_or_state=None, /, *, assumption7independent:bool):
        self._es = exps4binary_primitive_polynomial5or_deg_(deg_or_exps4binary_primitive_polynomial)
        super().__init__(may_int_or_state, assumption7independent=assumption7independent)
    @property
    #@override
    def exps4binary_primitive_polynomial(self, /):
        return self._es
    def __repr__(self, /):
        return repr_helper(self, self.exps4binary_primitive_polynomial, self.getstate(), assumption7independent=self.assumption7independent)

class PseudoRandom7linear__M5(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (5,2,0)


class _PseudoRandom7linear__M6(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (6,1,0)


class PseudoRandom7linear__M7(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (7,6,0) # <<== (7,1,0)

class PseudoRandom7linear__M13(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (13,4,3,1,0)

class PseudoRandom7linear__M17(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (17,3,0)

class PseudoRandom7linear__M19(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (19,5,2,1,0)

class PseudoRandom7linear__M31(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (31,3,0)

class PseudoRandom7linear__M61(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (61,5,2,1,0)

class PseudoRandom7linear__M89(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (89,6,5,3,0) # [89,38,0]

class PseudoRandom7linear__M107(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (107,7,5,3,2,1,0) # [107,9,7,4,0]

class PseudoRandom7linear__M127__mid126(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (127,126,0)
class PseudoRandom7linear__M127__mid001(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (127,1,0)
PseudoRandom7linear__M127__mid126
PseudoRandom7linear__M127__mid001
PseudoRandom7linear__M127 = PseudoRandom7linear__M127__mid126

class PseudoRandom7linear__M521(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (521,9,7,2,0) # [521,32,0]

class PseudoRandom7linear__M607(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (607,9,7,6,3,1,0) # [607,12,9,7,0]%%[607,105,0]

class PseudoRandom7linear__M1279(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (1279,11,9,8,5,3,2,1,0) # [1279,16,8,3,0]%%[1279,216,0]

class PseudoRandom7linear__M2203(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (2203,14,6,5,0) # [2203,11,10,6,4,1,0]

class PseudoRandom7linear__M2281(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (2281,9,8,7,6,2,0) # [2281,20,18,4,0]%%[2281,715,0]






def _test_M127__mid001_(sz=256, m=1, /, *args, **kwds):
    global _debug
    _debug = True
    try:
        rn = PseudoRandom7linear__M127__mid001(m, *args, **kwds)
        u = rn.getrandbits(sz)
        return uint2sized_binstr_(sz, u)
    finally:
        _debug = False


def _count_period_(deg, /, *args, **kwds):
    check_int_ge_le(5, 20, deg)
    T = globals()[f'PseudoRandom7linear__M{deg}']
    rn = T(*args, **kwds)
    rn.getrandbits(1)
    u0 = rn.getstate()
    sz = 0
    for sz in range(1, 1+2**deg):
        rn.getrandbits(1)
        u1 = rn.getstate()
        if u1 == u0:break
    else:
        raise 000
    return sz



__all__
from seed.math.pseudo_random import *
