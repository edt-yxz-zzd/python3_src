


__all__ = '''
    UInt2UInt1s_by_digits__LE
    UInt1s2UInt_by_1add1_2gcd_cf_3sub1_4LE_5add_head0s
    UInt2UInt_by_0LE_1add1_2gcd_cf_3sub1_4LE_5add_head0s
    UInt1s2UInt1s_to_UInt2UInt_by_0LE_HERE_1add1_2gcd_cf_3sub1_4LE_5add_head0s

    aUInt1s2UInt_by_1add1_2gcd_cf_3sub1_4LE_5add_head0s__R5
    aUInt2UInt_by_0LE_1add1_2gcd_cf_3sub1_4LE_5add_head0s__R6R7
    '''.split()

from .UInt2Digits import UInt2UInt1s_by_digits__LE
from .pint1s_2_uint_pint_by_gcd_cf import pint1s_2_uint_pint_by_gcd_cf
from .UInt2UIntLLs import UInt2UIntLLs_by_1digits_LE_2add_headMINs

from ..Bijection import Bijection
from ..NumberTVs import PInt, UInt, IntGeLeTV
from ..SeqBJ import Array2Tuple
from .XInt2YInt_by_add_or_mirror import aUInt2PInt_by_add1



'''
1) UInt <-> UInt1s # UInt2UInt1s_by_digits__LE

2) UInt1s
    <-> PInt1s       # fmap (+1)
    <-> (UInt, PInt) # pint1s_2_uint_pint_by_gcd_cf
    <-> (UInt, UInt) # fmap (-1)
    <-> [UInt]{2}    # Array2Tuple^-1
    <-> UInt         # UInt2UIntLLs_by_1digits_LE_2add_headMINs^-1
'''

# UInt2UInt1s_by_digits__LE
def UInt1s2UInt_by_1add1_2gcd_cf_3sub1_4LE_5add_head0s(small_radix):
    return  +( aUInt2PInt_by_add1[1,None]
            >> pint1s_2_uint_pint_by_gcd_cf
            >> +(UInt.idBJ * ~aUInt2PInt_by_add1)
            >> ~Array2Tuple(UInt, 2)
            >> ~UInt2UIntLLs_by_1digits_LE_2add_headMINs(2, small_radix)
            )

aUInt1s2UInt_by_1add1_2gcd_cf_3sub1_4LE_5add_head0s__R5 \
    = UInt1s2UInt_by_1add1_2gcd_cf_3sub1_4LE_5add_head0s(5)


def UInt2UInt_by_0LE_1add1_2gcd_cf_3sub1_4LE_5add_head0s(
    small_radix0, small_radix5):
    return +(UInt2UInt1s_by_digits__LE(small_radix0)
            >> UInt1s2UInt_by_1add1_2gcd_cf_3sub1_4LE_5add_head0s(small_radix5)
            )
def UInt1s2UInt1s_to_UInt2UInt_by_0LE_HERE_1add1_2gcd_cf_3sub1_4LE_5add_head0s(
    aUInt1s2UInt1s, small_radix0, small_radix5):
    return +(UInt2UInt1s_by_digits__LE(small_radix0)
            >> aUInt1s2UInt1s
            >> UInt1s2UInt_by_1add1_2gcd_cf_3sub1_4LE_5add_head0s(small_radix5)
            )

aUInt2UInt_by_0LE_1add1_2gcd_cf_3sub1_4LE_5add_head0s__R6R7 \
    = UInt2UInt_by_0LE_1add1_2gcd_cf_3sub1_4LE_5add_head0s(6,7)



