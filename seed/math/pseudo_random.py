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
[[
# [:reason4_body4mk_uniform_random_float_]:here
        # NOTE:only [deg >= 1+1075][assumption7independent:=False] can product [num_zeros == 1075]
===

>>> import math
>>> math.nextafter(1.0, 0.0).hex()
'0x1.fffffffffffffp-1'
>>> math.nextafter(0.0, 1.0).hex()
'0x0.0000000000001p-1022'
>>> math.ulp(0.0).hex()
'0x0.0000000000001p-1022'
>>> math.nextafter(1.0, 0.0)
0.9999999999999999
>>> math.nextafter(0.0, 1.0)
5e-324
>>> math.ulp(0.0)
5e-324
>>> math.ulp(1.0)
2.220446049250313e-16
>>> 1.0-math.ulp(1.0)
0.9999999999999998
>>> (1.0-math.ulp(1.0)).hex()
'0x1.ffffffffffffep-1'

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


>>> _body4mk_uniform_random_float_(-1+_zpow52, 0000).hex()
'0x1.fffffffffffffp-1'
>>> _body4mk_uniform_random_float_(-1+_zpow52, 1073).hex()
'0x0.0000000000002p-1022'
>>> _body4mk_uniform_random_float_(-1+_zpow52, 1074).hex()
'0x0.0000000000001p-1022'
>>> _body4mk_uniform_random_float_(1, 0000).hex()
'0x1.0000000000001p-1'
>>> _body4mk_uniform_random_float_(1, 1073).hex()
'0x0.0000000000001p-1022'
>>> _body4mk_uniform_random_float_(1, 1074).hex()
'0x0.0000000000001p-1022'
>>> _body4mk_uniform_random_float_(0, 0000).hex()
'0x1.0000000000000p-1'
>>> _body4mk_uniform_random_float_(0, 1073).hex()
'0x0.0000000000001p-1022'
>>> _body4mk_uniform_random_float_(0, 1074).hex()
'0x0.0p+0'

why?
    !! rounding...
>>> float.fromhex('0x1.0000000000001p-1074').hex()
'0x0.0000000000001p-1022'
>>> float.fromhex('0x1.0000000000001p-1075').hex()
'0x0.0000000000001p-1022'
>>> float.fromhex('0x1.0000000000000p-1074').hex()
'0x0.0000000000001p-1022'
>>> float.fromhex('0x1.0000000000000p-1075').hex()
'0x0.0p+0'

now:1074-->1075
>>> _body4mk_uniform_random_float_(-1+_zpow52, 0000).hex()
'0x1.fffffffffffffp-1'
>>> _body4mk_uniform_random_float_(-1+_zpow52, 1074).hex()
'0x0.0000000000001p-1022'
>>> _body4mk_uniform_random_float_(-1+_zpow52, 1075).hex()
'0x0.0p+0'
>>> _body4mk_uniform_random_float_(1, 0000).hex()
'0x1.0000000000001p-1'
>>> _body4mk_uniform_random_float_(1, 1074).hex()
'0x0.0000000000001p-1022'
>>> _body4mk_uniform_random_float_(1, 1075).hex()
'0x0.0p+0'
>>> _body4mk_uniform_random_float_(0, 0000).hex()
'0x1.0000000000000p-1'
>>> _body4mk_uniform_random_float_(0, 1073).hex()
'0x0.0000000000001p-1022'
>>> _body4mk_uniform_random_float_(0, 1074).hex()
'0x0.0p+0'
>>> _body4mk_uniform_random_float_(0, 1075).hex()
'0x0.0p+0'


===
]]
























'#'; __doc__ = r'#'
>>> PseudoRandom7linear__M5 = gmk_type4pseudo_random7linear_(5)
>>> PseudoRandom7linear__M7 = gmk_type4pseudo_random7linear_(7)
>>> _PseudoRandom7linear__M6 = gmk_type4pseudo_random7linear_(6)

#>>> f = lambda rn,sz:f'{rn.getrandbits(sz):0>{sz}b}'
>>> f = lambda rn,sz:uint2sized_binstr_(sz, rn.getrandbits(sz))

>>> PseudoRandom7linear__M127__mid126.exps4binary_primitive_polynomial
(127, 126, 0)
>>> PseudoRandom7linear__M127__mid001.exps4binary_primitive_polynomial
(127, 1, 0)
>>> PseudoRandom7linear__M127__mid126.deg4binary_primitive_polynomial
127
>>> bin(PseudoRandom7linear__M127__mid126.mul_order4binary_primitive_polynomial)
'0b1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
>>> bin(PseudoRandom7linear__M127__mid126.feedback_mask4binary_primitive_polynomial)
'0b1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001'
>>> bin(PseudoRandom7linear__M127__mid001.feedback_mask4binary_primitive_polynomial)
'0b1100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

>>> rn = PseudoRandom7linear__M127__mid126(False, 1)
>>> rn
PseudoRandom7linear__M127__mid126(False, 1)
>>> bin(rn.getrandbits(32))
'0b11111111111111111111111111111111'
>>> rn.random()
0.9999999999999999

0.9999999999999998
>>> rn.random()
0.4999999999999621

0.9996744791666665
>>> rn.random()
0.3333333333333333

0.6666666666666665
>>> rn.random()
0.3333333333333333

0.5999999999999999
>>> rn.random()
0.6656249999999999

0.6000651041666665
>>> f(PseudoRandom7linear__M127__mid126(False, 1), 67)
'1111111111111111111111111111111111111111111111111111111111111111111'
>>> f(PseudoRandom7linear__M127__mid126(False, 1), 130)
'1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111010'


>>> rn = PseudoRandom7linear__M127__mid126(True, 1)
>>> rn
PseudoRandom7linear__M127__mid126(True, 1)
>>> bin(rn.getrandbits(32))
'0b0'
>>> rn.random()
0.5000000000776101

1.5522028107284314e-10
>>> rn.random()
0.6666666666667423

0.6669921874999241
>>> rn.random()
0.9999998410542805

0.6666666666666665
>>> rn.random()
0.3333333333333333

0.2857157389322915
>>> rn.random()
0.6662946428571428

0.9332682291666665


>>> bin(PseudoRandom7linear__M127__mid126(True, 1).getrandbits(64))
'0b0'
>>> bin(PseudoRandom7linear__M127__mid126(True, 1).getrandbits(67))
'0b101'
>>> bin(PseudoRandom7linear__M127__mid126(True, 1).getrandbits(128))
'0b1010101010101010101010101010101010101010101010101010101010101011'
>>> f(PseudoRandom7linear__M127__mid126(True, 1), 67)
'0000000000000000000000000000000000000000000000000000000000000000101'
>>> f(PseudoRandom7linear__M127__mid126(True, 1), 128)
'00000000000000000000000000000000000000000000000000000000000000001010101010101010101010101010101010101010101010101010101010101011'
>>> f(PseudoRandom7linear__M127__mid126(True, 1), 512)
'00000000000000000000000000000000000000000000000000000000000000001010101010101010101010101010101010101010101010101010101010101011111111111111111111111111111111101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010010010010010010010010010010010010010010010010010101010101010101010101010101010101010101010101011101110111011101110111011101110101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010001010001010001010001010001010001010'





###################################
!!!!!!!!!!!!!!!!bug!!!!!!!!!!!!!!!!
###################################
>>> f(PseudoRandom7linear__M127__mid001(True, 1), 512)
'00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
>>> f(PseudoRandom7linear__M127__mid001(False, 1), 512)
'10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010001000'






###########################
_uniform_next_b_u_() => M5.period only 16! # [2 ~= (-1+2**5)/16]
    0110110000100
>>> f(PseudoRandom7linear__M5(True, 1), 128)
'01101100001001110110110000100111011011000010011101101100001001110110110000100111011011000010011101101100001001110110110000100111'

_uniform_next_b_u_() => M6.period only 32! # [2 ~= (-1+2**6)/32]
    11111
>>> f(_PseudoRandom7linear__M6(True, 1), 128)
'01000100010110100011111011001110010001000101101000111110110011100100010001011010001111101100111001000100010110100011111011001110'


_uniform_next_b_u_() => M7.period only 64! # [2 ~= (-1+2**7)/64]
    11111111@(7,6,0)
    00000000@(7,1,0)
>>> f(PseudoRandom7linear__M7(True, 1), 128)
'00000000110011001010011100001101110111011100110101101010001011110000000011001100101001110000110111011101110011010110101000101111'

'00001011101010010100110001000100010011110001101011001100111111110000101110101001010011000100010001001111000110101100110011111111'


###########################
_raw_next_b_u_() => M5.period == 31 == (-1+2**5)
    0000
>>> f(PseudoRandom7linear__M5(False, 1), 128)
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

>>> _count_period_(+5, False, 1)
31
>>> _count_period_(+7, False, 1)
127
>>> _count_period_(13, False, 1)
8191
>>> _count_period_(17, False, 1) #doctest: +SKIP
131071
>>> _count_period_(19, False, 1) #doctest: +SKIP
524287


###########################

>>> _count_period_(+5, True, 1)
16
>>> _count_period_(+7, True, 1)
64
>>> _count_period_(13, True, 1)
4096
>>> _count_period_(17, True, 1) #doctest: +SKIP
65536
>>> _count_period_(19, True, 1) #doctest: +SKIP
262144


###########################
>>> PseudoRandom7linear(False, 8, 1)
PseudoRandom7linear(False, (8, 4, 3, 2, 0), 1)
>>> f(PseudoRandom7linear(False, 8, 1), 512)
'10001110001001011100000011001001001101110010000010101101101011001011000011111011011110101110100010000110110001111001110011000101101001000101001010100111011101100111101111110100110011010100011000001110101010111110010100001001111111100001011110001101000000010001110001001011100000011001001001101110010000010101101101011001011000011111011011110101110100010000110110001111001110011000101101001000101001010100111011101100111101111110100110011010100011000001110101010111110010100001001111111100001011110001101000000010'

>>> PseudoRandom7linear(True, 8, 1)
PseudoRandom7linear(True, (8, 4, 3, 2, 0), 1)
>>> f(PseudoRandom7linear(True, 8, 1), 512)
'00011011000100001000001010111001110001110101111000000110101101111001010100111101101101101111100100100011100100101000111110010100000110110001000010000010101110011100011101011110000001101011011110010101001111011011011011111001001000111001001010001111100101000001101100010000100000101011100111000111010111100000011010110111100101010011110110110110111110010010001110010010100011111001010000011011000100001000001010111001110001110101111000000110101101111001010100111101101101101111100100100011100100101000111110010100'










####################################
####################################
####################################
####################################
>>> import pickle

1000111000100101110000001
>>> bs = pickle.dumps(PseudoRandom7linear(False, 8, 1))
>>> rn = pickle.loads(bs); rn
PseudoRandom7linear(False, (8, 4, 3, 2, 0), 1)
>>> f(rn, 512)
'10001110001001011100000011001001001101110010000010101101101011001011000011111011011110101110100010000110110001111001110011000101101001000101001010100111011101100111101111110100110011010100011000001110101010111110010100001001111111100001011110001101000000010001110001001011100000011001001001101110010000010101101101011001011000011111011011110101110100010000110110001111001110011000101101001000101001010100111011101100111101111110100110011010100011000001110101010111110010100001001111111100001011110001101000000010'

00011011000100001000001
>>> bs = pickle.dumps(PseudoRandom7linear(True, 8, 1))
>>> rn = pickle.loads(bs); rn
PseudoRandom7linear(True, (8, 4, 3, 2, 0), 1)
>>> f(rn, 512)
'00011011000100001000001010111001110001110101111000000110101101111001010100111101101101101111100100100011100100101000111110010100000110110001000010000010101110011100011101011110000001101011011110010101001111011011011011111001001000111001001010001111100101000001101100010000100000101011100111000111010111100000011010110111100101010011110110110110111110010010001110010010100011111001010000011011000100001000001010111001110001110101111000000110101101111001010100111101101101101111100100100011100100101000111110010100'


1000001100001
>>> bs = pickle.dumps(PseudoRandom7linear__M7(False, 1))
>>> rn = pickle.loads(bs); rn
mk_pseudo_random7linear_(7, -2, 1)

PseudoRandom7linear__M7(False, 1)
>>> f(rn, 512)
'10000011000010100011110010001011001110101001111101000011100010010011011010110111101100011010010111011100110010101011111110000001000001100001010001111001000101100111010100111110100001110001001001101101011011110110001101001011101110011001010101111111000000100000110000101000111100100010110011101010011111010000111000100100110110101101111011000110100101110111001100101010111111100000010000011000010100011110010001011001110101001111101000011100010010011011010110111101100011010010111011100110010101011111110000001000'

1111111010101001100
'11111110101010011001110111010010110001101111011010110110010010001110000101111100101011100110100010011110001010000110000010000001111111010101001100111011101001011000110111101101011011001001000111000010111110010101110011010001001111000101000011000001000000111111101010100110011101110100101100011011110110101101100100100011100001011111001010111001101000100111100010100001100000100000011111110101010011001110111010010110001101111011010110110010010001110000101111100101011100110100010011110001010000110000010000001111'

0000000011
>>> bs = pickle.dumps(PseudoRandom7linear__M7(True, 1))
>>> rn = pickle.loads(bs); rn
mk_pseudo_random7linear_(7, -2, 1, True)

PseudoRandom7linear__M7(True, 1)
>>> f(rn, 512)
'00000000110011001010011100001101110111011100110101101010001011110000000011001100101001110000110111011101110011010110101000101111000000001100110010100111000011011101110111001101011010100010111100000000110011001010011100001101110111011100110101101010001011110000000011001100101001110000110111011101110011010110101000101111000000001100110010100111000011011101110111001101011010100010111100000000110011001010011100001101110111011100110101101010001011110000000011001100101001110000110111011101110011010110101000101111'

0000101110101
'00001011101010010100110001000100010011110001101011001100111111110000101110101001010011000100010001001111000110101100110011111111000010111010100101001100010001000100111100011010110011001111111100001011101010010100110001000100010011110001101011001100111111110000101110101001010011000100010001001111000110101100110011111111000010111010100101001100010001000100111100011010110011001111111100001011101010010100110001000100010011110001101011001100111111110000101110101001010011000100010001001111000110101100110011111111'








####################################
>>> rn = PseudoRandom7linear__M127__mid001(False, b''); rn
PseudoRandom7linear__M127__mid001(False, 35199964725636440966184698525911177504)
>>> st0 = rn.getstate(); st0
(False, 35199964725636440966184698525911177504)
>>> for _ in range(7):rn.random()
0.5089915896808731
0.31811563523731956
0.2724104055073005
0.5439813667935123
0.03387603851627118
0.3224167492528913
0.8866519487150192
>>> st1 = rn.getstate(); st1
(False, 112626106645686747929903848387755394785)
>>> rn.setstate(st0);
>>> rn
PseudoRandom7linear__M127__mid001(False, 35199964725636440966184698525911177504)
>>> rn.getstate() == st0
True
>>> for _ in range(7):rn.random()
0.5089915896808731
0.31811563523731956
0.2724104055073005
0.5439813667935123
0.03387603851627118
0.3224167492528913
0.8866519487150192
>>> rn.getstate() == st1
True

>>> rn.setstate(st0);
>>> #rn = PseudoRandom7linear__M127__mid001(False, b'')
>>> f(rn, 512)
'00000100100110101000101110101111001111001001111100011010001011100000000011010111001101100001100100000010001000101101111001011000000110110101111100111001111000101000101101000010010111001110010000000010111100101011010001010110000011001100111011000101110100000101101111000010100101000100111100111011100011011100101001011000000011100010111110111001111101000010101010100110100111001110000111011000100011110111100110100010100110010010110010111101110100000010010011100001100101000011100011111111110101110100101001000100'


####################################
>>> rn = PseudoRandom7linear(False, (127,1,0), b''); rn
PseudoRandom7linear(False, (127, 1, 0), 35199964725636440966184698525911177504)
>>> st0 = rn.getstate(); st0
(False, (127, 1, 0), 35199964725636440966184698525911177504)
>>> for _ in range(7):rn.random()
0.5089915896808731
0.31811563523731956
0.2724104055073005
0.5439813667935123
0.03387603851627118
0.3224167492528913
0.8866519487150192
>>> st1 = rn.getstate(); st1
(False, (127, 1, 0), 112626106645686747929903848387755394785)
>>> rn.setstate(st0);
>>> rn
PseudoRandom7linear(False, (127, 1, 0), 35199964725636440966184698525911177504)
>>> rn.getstate() == st0
True
>>> for _ in range(7):rn.random()
0.5089915896808731
0.31811563523731956
0.2724104055073005
0.5439813667935123
0.03387603851627118
0.3224167492528913
0.8866519487150192
>>> rn.getstate() == st1
True

>>> rn.setstate(st0);
>>> #rn = PseudoRandom7linear(False, (127,1,0), b'')
>>> f(rn, 512)
'00000100100110101000101110101111001111001001111100011010001011100000000011010111001101100001100100000010001000101101111001011000000110110101111100111001111000101000101101000010010111001110010000000010111100101011010001010110000011001100111011000101110100000101101111000010100101000100111100111011100011011100101001011000000011100010111110111001111101000010101010100110100111001110000111011000100011110111100110100010100110010010110010111101110100000010010011100001100101000011100011111111110101110100101001000100'


####################################

#>>> gmk_type4pseudo_random7linear_(127) is PseudoRandom7linear__M127
True
>>> T127 = gmk_type4pseudo_random7linear_(127)
>>> T127 is gmk_type4pseudo_random7linear_(127)
True
>>> T127
<class 'seed.math.pseudo_random.PseudoRandom7linear__M127_1_0'>
>>> T127.exps4binary_primitive_polynomial
(127, 1, 0)

####################################
>>> T8 = gmk_type4pseudo_random7linear_(8)
>>> __name__
'seed.math.pseudo_random'
>>> T8
<class 'seed.math.pseudo_random.PseudoRandom7linear__M8_4_3_2_0'>
>>> T8.__module__
'seed.math.pseudo_random'
>>> T8.__name__
'PseudoRandom7linear__M8_4_3_2_0'
>>> T8.__qualname__ #bug:'seed.math.pseudo_random.PseudoRandom7linear__M8_4_3_2_0'
'PseudoRandom7linear__M8_4_3_2_0'
>>> T8 is gmk_type4pseudo_random7linear_(8)
True
>>> rn = mk_pseudo_random7linear_(8, -1, b''); rn
mk_pseudo_random7linear_(8, -2, 245)
>>> T8 is type(rn)
True
>>> bs = pickle.dumps(rn)
>>> rn = pickle.loads(bs); rn
mk_pseudo_random7linear_(8, -2, 245)
>>> T8 is type(rn)
True
>>> f(rn, 512)
'10100010000110110001111001110011000101101001000101001010100111011101100111101111110100110011010100011000001110101010111110010100001001111111100001011110001101000000010001110001001011100000011001001001101110010000010101101101011001011000011111011011110101110100010000110110001111001110011000101101001000101001010100111011101100111101111110100110011010100011000001110101010111110010100001001111111100001011110001101000000010001110001001011100000011001001001101110010000010101101101011001011000011111011011110101110'
>>> _count_period_(rn)
255
>>> rn.mul_order4binary_primitive_polynomial # default [assumption7independent:=False]@mk_pseudo_random7linear_()
255


>>> rn = mk_pseudo_random7linear_(8, -1, b'', True); rn
mk_pseudo_random7linear_(8, -2, 245, True)
>>> T8 is type(rn)
True
>>> bs = pickle.dumps(rn)
>>> rn = pickle.loads(bs); rn
mk_pseudo_random7linear_(8, -2, 245, True)
>>> T8 is type(rn)
True
>>> f(rn, 512)
'00010101110011100011101011110000001101011011110010101001111011011011011111001001000111001001010001111100101000001101100010000100000101011100111000111010111100000011010110111100101010011110110110110111110010010001110010010100011111001010000011011000100001000001010111001110001110101111000000110101101111001010100111101101101101111100100100011100100101000111110010100000110110001000010000010101110011100011101011110000001101011011110010101001111011011011011111001001000111001001010001111100101000001101100010000100'
>>> _count_period_(rn)
128


####################################

test:imay_version@mk_pseudo_random7linear_
>>> rn = mk_pseudo_random7linear_(8, -1, b''); rn
mk_pseudo_random7linear_(8, -2, 245)
>>> rn = mk_pseudo_random7linear_(8, -1, 1); rn
mk_pseudo_random7linear_(8, -2, 1)
>>> rn = mk_pseudo_random7linear_(8, -2, 1); rn
mk_pseudo_random7linear_(8, -2, 1)
>>> rn = mk_pseudo_random7linear_(8, 'int8state', 1); rn
mk_pseudo_random7linear_(8, -2, 1)
>>> rn = mk_pseudo_random7linear_(8, '', 1); rn
mk_pseudo_random7linear_(8, -2, 1)
>>> rn = mk_pseudo_random7linear_(8, 'auto', 1); rn
mk_pseudo_random7linear_(8, -2, 1)
>>> rn = mk_pseudo_random7linear_(8, 'obj8seed', 1); rn
mk_pseudo_random7linear_(8, -2, 34)
>>> rn = mk_pseudo_random7linear_(8, '', b''); rn
mk_pseudo_random7linear_(8, -2, 245)
>>> rn = mk_pseudo_random7linear_(8, 'auto', b''); rn
mk_pseudo_random7linear_(8, -2, 245)
>>> rn = mk_pseudo_random7linear_(8, 'obj8seed', b''); rn
mk_pseudo_random7linear_(8, -2, 245)


>>> "deprecate"; rn = mk_pseudo_random7linear_(8, +0, 1); rn #doctest: +SKIP
mk_pseudo_random7linear_(8, -2, 34)
>>> rn = mk_pseudo_random7linear_(8, +1, 1); rn
mk_pseudo_random7linear_(8, -2, 34)
>>> rn = mk_pseudo_random7linear_(8, +2, 1); rn
mk_pseudo_random7linear_(8, -2, 34)
>>> "deprecate"; rn = mk_pseudo_random7linear_(8, +3, 1); rn #doctest: +SKIP
mk_pseudo_random7linear_(8, -2, 34)

>>> "deprecate"; rn = mk_pseudo_random7linear_(8, +0, b''); rn #doctest: +SKIP
mk_pseudo_random7linear_(8, -2, 216)
>>> rn = mk_pseudo_random7linear_(8, +1, b''); rn
mk_pseudo_random7linear_(8, -2, 216)
>>> rn = mk_pseudo_random7linear_(8, +2, b''); rn
mk_pseudo_random7linear_(8, -2, 245)
>>> "deprecate"; rn = mk_pseudo_random7linear_(8, +3, b''); rn #doctest: +SKIP
mk_pseudo_random7linear_(8, -2, 216)

# (None, int, float, str, bytes, bytearray)
[version:=+1] => (str, bytes) --[bytes.decode('latin-1')]-> str --> int@otherwise
[version:=+2] => (str, bytes, bytearray) --[str.encode()]-> bytes --> int@otherwise
    # [encoding:=???]
    #   this must be bug!
    e ../lots/NOTE/Python/python-bug/random-bug.txt
    patch__7ver2_str_without_explicit_encoding:goto
[otherwise] => (None, int, float, str, bytes, bytearray) --> super().seed()

bytes=>{{0,3},{1},{2}}
>>> "deprecate"; rn = mk_pseudo_random7linear_(8, +0, b'aaa'); rn # ???using unstable hash()??? #doctest: +SKIP
mk_pseudo_random7linear_(8, -2, 229)
>>> rn = mk_pseudo_random7linear_(8, +1, b'aaa'); rn
mk_pseudo_random7linear_(8, -2, 239)
>>> rn = mk_pseudo_random7linear_(8, +2, b'aaa'); rn
mk_pseudo_random7linear_(8, -2, 200)
>>> "deprecate"; rn = mk_pseudo_random7linear_(8, +3, b'aaa'); rn #doctest: +SKIP
mk_pseudo_random7linear_(8, -2, 229)

str=>{{0,3},{1},{2}} #same as bytes
>>> "deprecate"; rn = mk_pseudo_random7linear_(8, +0, 'aaa'); rn # ???using unstable hash()??? #doctest: +SKIP
mk_pseudo_random7linear_(8, -2, 229)
>>> rn = mk_pseudo_random7linear_(8, +1, 'aaa'); rn
mk_pseudo_random7linear_(8, -2, 239)
>>> rn = mk_pseudo_random7linear_(8, +2, 'aaa'); rn
mk_pseudo_random7linear_(8, -2, 200)
>>> "deprecate"; rn = mk_pseudo_random7linear_(8, +3, 'aaa'); rn #doctest: +SKIP
mk_pseudo_random7linear_(8, -2, 229)

>>> "deprecate"; rn = mk_pseudo_random7linear_(8, +0, b'aaabbbbzzzklhfy76905432wchjkkj8i'); rn # ???using unstable hash()??? #doctest: +SKIP
mk_pseudo_random7linear_(8, -2, 238)
>>> "deprecate"; rn = mk_pseudo_random7linear_(8, +3, b'aaabbbbzzzklhfy76905432wchjkkj8i'); rn #doctest: +SKIP
mk_pseudo_random7linear_(8, -2, 238)
>>> "deprecate"; rn = mk_pseudo_random7linear_(8, +0, 'aaabbbbzzzklhfy76905432wchjkkj8i'); rn # ???using unstable hash()??? #doctest: +SKIP
mk_pseudo_random7linear_(8, -2, 238)
>>> "deprecate"; rn = mk_pseudo_random7linear_(8, +3, 'aaabbbbzzzklhfy76905432wchjkkj8i'); rn #doctest: +SKIP
mk_pseudo_random7linear_(8, -2, 238)


float=>same
>>> "deprecate"; rn = mk_pseudo_random7linear_(8, +0, 245677378/2**18); rn #doctest: +SKIP
mk_pseudo_random7linear_(8, -2, 228)
>>> rn = mk_pseudo_random7linear_(8, +1, 245677378/2**18); rn
mk_pseudo_random7linear_(8, -2, 228)
>>> rn = mk_pseudo_random7linear_(8, +2, 245677378/2**18); rn
mk_pseudo_random7linear_(8, -2, 228)
>>> "deprecate"; rn = mk_pseudo_random7linear_(8, +3, 245677378/2**18); rn #doctest: +SKIP
mk_pseudo_random7linear_(8, -2, 228)

int=>same
>>> "deprecate"; rn = mk_pseudo_random7linear_(8, +0, 245677378); rn #doctest: +SKIP
mk_pseudo_random7linear_(8, -2, 129)
>>> rn = mk_pseudo_random7linear_(8, +1, 245677378); rn
mk_pseudo_random7linear_(8, -2, 129)
>>> rn = mk_pseudo_random7linear_(8, +2, 245677378); rn
mk_pseudo_random7linear_(8, -2, 129)
>>> "deprecate"; rn = mk_pseudo_random7linear_(8, +3, 245677378); rn #doctest: +SKIP
mk_pseudo_random7linear_(8, -2, 129)


####################################




















[[
py_adhoc_call   seed.math.pseudo_random   @_test_M127__mid001_ =256 =True =1
py_adhoc_call   seed.math.pseudo_random   @_test_M127__mid001_ =2 =True =1
    '00'
py_adhoc_call   seed.math.pseudo_random   @_test_M127__mid001_ =2 =True =5
    '00'
py_adhoc_call   seed.math.pseudo_random   @_test_M127__mid001_ =2 =True =127605887595351923798765477786913079298
    '11'
        # "5"后继，错位1，
py_adhoc_call   seed.math.pseudo_random   @_test_M127__mid001_ =130 =True =127605887595351923798765477786913079298
    '1101110101111101110101111101011111010101011111111101110101111101011111010101011111111101011111010101011111111101010101111111110101'
        # 所以是 初始状态 非法？大概有一半非法？
        #   但M5版并无此现象
]]

[[
py_adhoc_call   seed.math.pseudo_random   @_count_period_ =5 =True =1
    16
py_adhoc_call   seed.math.pseudo_random   @_count_period_ =7 =True =1
    64
py_adhoc_call   seed.math.pseudo_random   @_count_period_ =13 =True =1
    4096
py_adhoc_call   seed.math.pseudo_random   @_count_period_ =17 =True =1
    65536
py_adhoc_call   seed.math.pseudo_random   @_count_period_ =19 =True =1
    262144


py_adhoc_call   seed.math.pseudo_random   @_count_period_ =5 =False =1
    31
py_adhoc_call   seed.math.pseudo_random   @_count_period_ =7 =False =1
    127
py_adhoc_call   seed.math.pseudo_random   @_count_period_ =13 =False =1
    8191
py_adhoc_call   seed.math.pseudo_random   @_count_period_ =17 =False =1
    131071
py_adhoc_call   seed.math.pseudo_random   @_count_period_ =19 =False =1
    524287

]]

py_adhoc_call   seed.math.pseudo_random   @_test__7DeprecationWarning_
py_adhoc_call   seed.math.pseudo_random   @f
from seed.math.pseudo_random import *
]]]'''#'''
__all__ = r'''
mk_pseudo_random7linear_
    gmk_type4pseudo_random7linear_




IPseudoRandom7linear
    PseudoRandom7linear
    PseudoRandom7linear__M127__mid126
    PseudoRandom7linear__M127__mid001

exps4binary_primitive_polynomial5or_deg_
uint5bits_
uint2sized_binstr_
'''.split()#'''
r'''[[[
    PseudoRandom7linear__M5
    PseudoRandom7linear__M7
    PseudoRandom7linear__M13
    PseudoRandom7linear__M17
    PseudoRandom7linear__M19
    PseudoRandom7linear__M31
    PseudoRandom7linear__M61
    PseudoRandom7linear__M89
    PseudoRandom7linear__M107
    PseudoRandom7linear__M521
    PseudoRandom7linear__M607
    PseudoRandom7linear__M1279
    PseudoRandom7linear__M2203
    PseudoRandom7linear__M2281
#]]]'''#'''

__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from random import Random
from abc import abstractmethod
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_int_ge, check_int_ge_le
    from seed.helper.repr_input import repr_helper, repr_helper__str
    from seed.types.CachedProperty import CachedProperty# mk_cached_propertyT_
    from seed.debug.print_err import print_err
    from seed.tiny_.containers import mk_immutable_seq, mk_tuple
    #???not???bug:from warnings import warn
    from warnings import warn
    from weakref import WeakValueDictionary
#.    from itertools import islice
with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
    from seed.math.polynomial.binary_primitive_polynomial import sparse_deg2list4exps4binary_primitive_polynomial

#.#################################
___end_mark_of_excluded_global_names__0___ = ...


_debug = False
if 0:
    #_zpow1024 = 1<<1024
    _inv_zpow32 = 0.5**32 # == 2.0**-32
    _inv_zpow52 = 0.5**52 # == 2.0**-52
if 1:
    _zpow52 = 1<<52
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
def _iter4getrandbits(self, u, /):
    mask = self.feedback_mask4binary_primitive_polynomial
    _next_b_u_ = _uniform_next_b_u_ if self.assumption7independent else _raw_next_b_u_
    while 1:
        (b, u) = bu = _next_b_u_(mask, u)
        yield bu
def _count_zero_randbits(self, max4num_zeros, /):
    u = self._get_uint_state_()
    it = _iter4getrandbits(self, u)
    num_zeros = 0
    for _ in range(max4num_zeros):
        (b, u) = next(it)
        if b:break
        num_zeros += 1
    u, num_zeros
    self._set_uint_state_(u)
    return num_zeros

def _mk_uniform_random_float_(self, /):
    '-> float{>=0.0}{<1.0}'
    u52 = self.getrandbits(52)
    # [0 <= u52 < 2**52]
    #       NOTE:only [deg >= 1+52][assumption7independent:=False] can product [u52 == 0]
    num_zeros = _count_zero_randbits(self, 1075)
    # [0 <= num_zeros <= 1075]
    #       NOTE:only [deg >= 1+1075][assumption7independent:=False] can product [num_zeros == 1075]
    return _body4mk_uniform_random_float_(u52, num_zeros)

def _body4mk_uniform_random_float_(u52, num_zeros, /):
    assert 0 <= u52 < _zpow52
    assert 0 <= num_zeros <= 1075
    # [0 <= u52 < 2**52]
    # [0 <= num_zeros <= 1075]

    if 0:
        u53 = _zpow52 ^ u52
        # [2**52 <= u53 < 2**53]
        f53 = float(u53)
        # [2**52 <= f53 < 2**53]
        f7uniform = f53*0.5**(53+num_zeros)
        #   bug: since [0.5**(53+num_zeros) may become 0.0]
    else:
        s7hex = f'0x1.{u52:0>13x}p-{1+num_zeros}'

        f7uniform = float.fromhex(s7hex)
    f7uniform
    # [2**-(1+num_zeros) <= f7uniform < 2**-num_zeros]
    # [[num_zeros:=0] -> [[2**-1 <= f7uniform < 2**-0]]]
    # [[num_zeros:=0] -> [[0.5 <= f7uniform < 1.0]]]

    # [[num_zeros:=1073] -> [[2**-(1+1073) <= f7uniform < 2**-1073]]]

    # [[num_zeros:=1074] -> [[2**-(1+1074) <= f7uniform < 2**-1074]]]
    # !! [:reason4_body4mk_uniform_random_float_]:goto
    # !! [0.5**1075 --> 0.0]
    # !! [0.5**1074 --> 5e-324 == math.ulp(0.0)]
    # expected:
    #       [[num_zeros:=1074] -> [[0.0 <= f7uniform < 5e-324 == math.ulp(0.0)]]]
    #       [[num_zeros:=1074] -> [[0.0 == f7uniform)]]]
    # actually:
    #       !! rounding
    #       [[num_zeros:=1074][u52:=0] <-> [[0.0 == f7uniform)]]]
    # ==>> using 1075 instead of 1074

    # !! [0 <= num_zeros <= 1075]
    # !! [[num_zeros:=1074][u52:=0] <-> [[0.0 == f7uniform)]]]
    # !! [[num_zeros:=1075] -> [[0.0 == f7uniform)]]]
    # !! [[num_zeros:=0] -> [[0.5 <= f7uniform < 1.0]]]
    # [0.0 <= f7uniform < 1.0]
    return f7uniform
def _old__mk_uniform_random_float_(self, /):
    # float: exp
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

def _test__7DeprecationWarning_():
    DeprecationWarning#ignored by default
        #Base category for warnings about deprecated features when those warnings are intended for other Python developers (ignored by default, unless triggered by code in __main__).
    UserWarning
    PseudoRandom7linear__M127__mid001(True, '')
    #warn('[assumption7independent:=True]', UserWarning)
    #warn('[assumption7independent:=True]', DeprecationWarning)
class IPseudoRandom7linear(Random):
    '[ust :: 1+uint%mul_order][period{assumption7independent;deg} == (2**(-1+deg) if assumption7independent else (-1+2**deg))]'
    __slots__ = ('_ust', '_settings')


    #@override
    def _set_uint_state_(self, u, /):
        'ust -> None'
        check_int_ge_le(1, self.mul_order4binary_primitive_polynomial, u)
        self._ust = u
        # [1 <= u < 2**deg4binary_primitive_polynomial]
    def _get_uint_state_(self, /):
        '-> ust'
        return self._ust
    def _get_settings_(self, /):
        '-> settings'
        return self._settings
    def _set_settings_(self, settings, /):
        if not None is (_settings:=getattr(self, '_settings', None)):
            if not _settings == settings:raise TypeError('incompatible settings:', _settings, settings)
        else:
            assumption7independent = settings[0]
            check_type_is(bool, assumption7independent)
            self._settings = settings
    #@override
    def setstate(self, state, /):
        'st -> None'
        settings = state[:-1]
        ust = state[-1]
        self._set_settings_(settings)
        self._set_uint_state_(ust)
    #@override
    def getstate(self, /):
        '-> st/(*settings, ust)'
        settings = self._get_settings_()
        ust = self._get_uint_state_()
        state = (*settings, ust)
        return state
    def __setstate__(self, state, /):
        #pickle
        raise 000
    def __getstate__(self, /):
        #pickle
        raise 000
        return None
    def __reduce__(self, /):
        #pickle
        #__repr__
        return (type(self), self._args4repr)
    @property
    def _args4repr(self, /):
        _args4repr = (*self._get_settings_(), self._get_uint_state_())
        return _args4repr



    #def __new__(cls, may_int_or_state=None, /):
    #    self = super(__class__, cls).__new__(cls)
    def __init__(self, assumption7independent:bool=None, int_or_may_seed=1, /, *extra_settings, version=-1):
        #def __init__(self, int_or_may_seed=None, /, *, assumption7independent:bool):
        #self._assumption7independent = bool(assumption7independent)
        if not None is assumption7independent:
            check_type_is(bool, assumption7independent)
            if assumption7independent:
                warn('[assumption7independent:=True]', UserWarning)
                #warn('[assumption7independent:=True]', DeprecationWarning)
            self._set_settings_((assumption7independent, *extra_settings))
            self.seed(int_or_may_seed, version=version)
        else:
            pass
            #pickle
            #leave undefined...
    @property
    def assumption7independent(self, /):
        #return self._assumption7independent
        return self._get_settings_()[0]
    def __repr__(self, /):
        return repr_helper(self, *self._args4repr)
        return repr_helper(self, *self._get_settings_(), self._get_uint_state_())
        #.return repr_helper(self, self._get_uint_state_(), assumption7independent=self.assumption7independent)
        #.if self.assumption7independent:
        #.    return repr_helper(self, self._get_uint_state_(), assumption7independent=True)
        #.return repr_helper(self, self._get_uint_state_())
    def __init_subclass__(cls, /, **kwargs):
        super().__init_subclass__(**kwargs)
        es = cls.exps4binary_primitive_polynomial
        _b_static7exps = hasattr(type(es), '__len__')
        if _b_static7exps:
            deg = es[0]
            check_int_ge(2, deg)
            mul_order = -1+(1<<deg)
            mask = _4mask(es)
            cls.deg4binary_primitive_polynomial = deg
            cls.mul_order4binary_primitive_polynomial = mul_order
            cls.feedback_mask4binary_primitive_polynomial = mask
        cls._b_static7exps = _b_static7exps

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
    #   less /data/data/com.termux/files/usr/lib/python3.11/random.py
    ###########################
    #@override
    #def seed(self, may_int_or_state=None, /):
    #   'may (int|ust) -> None'
    def seed(self, int_or_may_seed=None, /, version=2):
        #see:imay_version
        match version:
            case '' | 'auto':
                version = -1
            case 'obj8seed':
                version = +2
            case 'int8state':
                version = -2
            case 0:
                raise ValueError('[version:=0]')
        version
        check_int_ge_le(-2, 2, version)
        match (version, int_or_may_seed):
            case (-1, int() as j8st):
                version = -2
                pass
            case (-1, may_seed):
                version = +2
        version
        match (version, int_or_may_seed):
            #case (int(), may_seed) if version >= 0:
            case (int(1|2), may_seed) if version > 0:
                # None, int, float, str, bytes, bytearray
                if version == +2 and isinstance(may_seed, str):
                    #patch__7ver2_str_without_explicit_encoding:here
                    may_seed = may_seed.encode('u8')
                if not (version in (1,2) or (may_seed is None or isinstance(may_seed, int))):raise Exception('unintended unstable/non-reproductable random')
                rn = Random(0)
                rn.seed(may_seed, version=version)
                while not (u := rn.getrandbits(self.deg4binary_primitive_polynomial)):pass
                u
                # [0 =!= u]
                # [1 <= u < 2**deg4binary_primitive_polynomial]
            case (-2, int() as j8st):
                # !! ???[(self.mul_order4binary_primitive_polynomial) is Mersenne_prime]???
                #bug:u = 1+ j8st%(self.mul_order4binary_primitive_polynomial)
                #   since: u --> 1+u
                M = (self.mul_order4binary_primitive_polynomial)
                if not 1 <= j8st <= M:
                    u = j8st%M
                    if u == 0:
                        u = M
                    # u --> u
                else:
                    u = j8st
                u
                assert 1 <= u <= M
                # [1 <= u <= mul_order4binary_primitive_polynomial]
                # [1 <= u < 2**deg4binary_primitive_polynomial]
            case bad_seed:
                raise TypeError(bad_seed)
        # [1 <= u < 2**deg4binary_primitive_polynomial]
        u
        self._set_uint_state_(u)

    #@override
    def getrandbits(self, k, /):
        'getrandbits(k) -> x.  Generates an int with k random bits.'
        u = self._get_uint_state_()
        bits = []
        it = _iter4getrandbits(self, u)
        for _ in range(k):
            (b, u) = next(it)
            bits.append(b)
        u, bits
        self._set_uint_state_(u)
        return uint5bits_(bits)
    #@override
    def random(self, /):
        '-> float{>=0.0}{<1.0}'
        return _mk_uniform_random_float_(self)

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
    zmay_deg = 0
    match deg_or_exps4binary_primitive_polynomial:
        case int() as deg:
            check_int_ge(2, deg)
            if deg in _deg2T:
                es = _deg2T[deg].exps4binary_primitive_polynomial
            elif not deg in sparse_deg2list4exps4binary_primitive_polynomial:
                raise NotImplementedError('unknown factorization of (-1+2**deg) : ', deg)
            else:
                ess = sparse_deg2list4exps4binary_primitive_polynomial[deg]
                es = ess[0]
            es
            r'''[[[
            match deg2neg_or_list4exps4binary_primitive_polynomial[deg]:
                case int() as neg_deg:
                    assert neg_deg == -deg
                    raise NotImplementedError('unknown factorization of (-1+2**deg) : ', deg)
                case ess:
                    es = ess[0]
            #]]]'''#'''
            es
        case es:
            es = mk_tuple(es)
            deg = es[0]
            pass
    es
    es = mk_tuple(es)
    assert es[-1] == 0
    assert es[0] == deg
    assert deg >= 2
    assert len(es) >= 3
    assert len(es)&1 == 1
    return es
class PseudoRandom7linear(IPseudoRandom7linear):
    def __init__(self, assumption7independent:bool=None, deg_or_exps4binary_primitive_polynomial=None, int_or_may_seed=1, /):
        #def __init__(self, deg_or_exps4binary_primitive_polynomial, may_int_or_state=None, /, *, assumption7independent:bool):
        if not None is assumption7independent:
            check_type_is(bool, assumption7independent)
            es = exps4binary_primitive_polynomial5or_deg_(deg_or_exps4binary_primitive_polynomial)
            super().__init__(assumption7independent, int_or_may_seed, es)
            #super().__init__(int_or_may_seed, assumption7independent=assumption7independent)
        else:
            pass
            #pickle
            #leave undefined...
    @property
    #@override
    def exps4binary_primitive_polynomial(self, /):
        #return self._es
        return self._get_settings_()[1]

class PseudoRandom7linear__M127__mid126(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (127,126,0)
class PseudoRandom7linear__M127__mid001(IPseudoRandom7linear):
    #@override
    exps4binary_primitive_polynomial = (127,1,0)
PseudoRandom7linear__M127__mid126
PseudoRandom7linear__M127__mid001
#PseudoRandom7linear__M127 = PseudoRandom7linear__M127__mid126

r'''[[[
####################################
####################################
## !! mk_pseudo_random7linear_()
####################################
####################################



####################
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



####################
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



####################
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

####################

#]]]'''#'''






def _test_M127__mid001_(sz, /, *args, **kwds):
    global _debug
    _debug = True
    try:
        rn = PseudoRandom7linear__M127__mid001(*args, **kwds)
        u = rn.getrandbits(sz)
        return uint2sized_binstr_(sz, u)
    finally:
        _debug = False


def _count_period_(deg_or_exps_or_rn_or_T, /, *args, **kwds):
    match deg_or_exps_or_rn_or_T:
        case (int()|tuple()) as deg_or_exps:
            #T = globals()[f'PseudoRandom7linear__M{deg}']
            T = gmk_type4pseudo_random7linear_(deg_or_exps)
            rn = T(*args, **kwds)
        case type() as T if issubclass(T, IPseudoRandom7linear):
            rn = T(*args, **kwds)
        case IPseudoRandom7linear() as rn:
            rn
        case _:
            raise TypeError(deg_or_exps_or_rn_or_T)
    rn
    deg = rn.deg4binary_primitive_polynomial
    check_int_ge_le(5, 20, deg)

    rn.getrandbits(1)
    u0 = rn._get_uint_state_()
    sz = 0
    for sz in range(1, 1+2**deg):
        rn.getrandbits(1)
        u1 = rn._get_uint_state_()
        if u1 == u0:break
    else:
        raise 000
    return sz

def __():
    prefix = 'PseudoRandom7linear__M'
    for nm, T in globals().items():
        if not nm.startswith(prefix):continue
        if not nm[len(prefix):].isdigit():continue
        if not isinstance(T, type):continue
        if not issubclass(T, IPseudoRandom7linear):continue
        deg = int(nm[len(prefix):])
        yield (deg, T)
_deg2T = dict(__())
exps4binary_primitive_polynomial5or_deg_

_exps2T = WeakValueDictionary()
def mk_pseudo_random7linear_(deg_or_exps, imay_version, int_or_may_seed, /, assumption7independent=False):
    '[imay_version == (-2|-1|1|2|"obj8seed"|"int8state"|""|"auto")]'
    T = gmk_type4pseudo_random7linear_(deg_or_exps)
    rn = T(assumption7independent, int_or_may_seed, version=imay_version)
    #rn.seed(int_or_may_seed, version=imay_version)
    return rn
def gmk_type4pseudo_random7linear_(deg_or_exps, /):
    exps = exps4binary_primitive_polynomial5or_deg_(deg_or_exps)
    deg = exps[0]
    if not None is (T:=_deg2T.get(deg)) and exps == T.exps4binary_primitive_polynomial:
        return T
    if not None is (T:=_exps2T.get(exps)):
        return T


    check_type_is(tuple, exps)
    if not 1 == len(exps)&1:raise TypeError(exps)
    check_int_ge(2, deg)
    check_int_ge_le(0,0, exps[-1])
    u = 0
    for e in reversed(exps):
        check_int_ge(u, e)
        u = 1+e


    s = '_'.join(map(str, exps))
    nm = f'PseudoRandom7linear__M{s}'
    qnm = f'{__name__}.{nm}'
    #bug:T = type(nm, (_IPseudoRandom7linear__7repr4mk,), dict(exps4binary_primitive_polynomial=exps, __module__=__name__, __qualname__=qnm))
        # bug: , __qualname__=qnm
        #   qnm for nested type only
    T = type(nm, (_IPseudoRandom7linear__7repr4mk,), dict(exps4binary_primitive_polynomial=exps))
    assert T.__name__ == nm, (T.__name__, nm)
    assert T.__module__ == __name__, (T.__module__, __name__)
    assert T.__qualname__ == nm, (T.__qualname__, nm)
    #bug:assert T.__qualname__ == qnm, (T.__qualname__, qnm)
    assert int is type(T.mul_order4binary_primitive_polynomial) # __init_subclass__
    _T = _exps2T.setdefault(exps, T)
    if not _T is T:raise 000
    return T

class _IPseudoRandom7linear__7repr4mk(IPseudoRandom7linear):
    @property
    def _args4mk(self, /):
        exps = self.exps4binary_primitive_polynomial
        deg = exps[0]
        deg_or_exps = deg if exps == exps4binary_primitive_polynomial5or_deg_(deg) else exps
        tm = (True,) if self.assumption7independent else ()
        return (deg_or_exps, -2, self._get_uint_state_(), *tm)
    def __repr__(self, /):
        return repr_helper__str(mk_pseudo_random7linear_.__name__, *self._args4mk)
    def __reduce__(self, /):
        return (mk_pseudo_random7linear_, self._args4mk)


__all__
from seed.math.pseudo_random import mk_pseudo_random7linear_, gmk_type4pseudo_random7linear_
from seed.math.pseudo_random import *
