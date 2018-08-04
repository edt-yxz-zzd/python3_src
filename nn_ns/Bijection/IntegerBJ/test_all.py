

# edit 'test_data.py' and this file to test all bijections defined.

from ..test_IO_by_name import test_IO_by_name
from .pint1s_2_uint_pint_by_gcd_cf import pint1s_2_uint_pint_by_gcd_cf
from .XInt2YInt_by_add_or_mirror import aUInt2PInt_by_add1
from .PIntSet2PInts_by_sorted_sub import aPIntSet2PInts_by_sorted_sub
from .PInts2URational_by_cf import aPInts2URational_by_cf
from .UInt2Digits import aUInt2Digits__LE_R3\
    , aUInt2UInt1s_by_digits__LE_R2, aUInt2UInt1Ms_by_digits__LE_M4_R2\
    , aDigits2BiDigits1s_by_split0__radix_down__R3\
    , aDigits2BiDigits1Ms_mayDigits_by_split0__radix_down__R3_M3
from .UIntLLs2UInt0Ls import \
    aUIntLLs2UInt0Ls_by_remove_head0s__L3\
    , aUIntNLNLs2UIntNNLs__L3N1\
    , aUIntNLMs2UIntNMs__L3N1M5
from .UInt2UIntLLs import aUInt2UIntLLs_by_1digits_LE_2add_headMINs__L4R3
from .UInt2UInt1s import \
    aUInt1s2UInt_by_1add1_2gcd_cf_3sub1_4LE_5add_head0s__R5\
    , aUInt2UInt_by_0LE_1add1_2gcd_cf_3sub1_4LE_5add_head0s__R6R7
from .UInt2UIntRadixReprLE import UInt2UIntRadixReprLE
from .UInt2UIntLLs_by_digit_channels import \
    UIntRadixReprLE2BiDigitChannels_UIntRadixReprLE_by_endBy0 \
    , UIntRadixReprLE2BiDigitChunks_UIntRadixReprLE_by_split0
from .UInt2UInt_by_mod import UInt2UInt_by_mod


test_IO_by_name('PInt1s', '(UInt, PInt)', pint1s_2_uint_pint_by_gcd_cf)

aUInt2PInt_by_add1.test()
test_IO_by_name('UInt', 'PInt', aUInt2PInt_by_add1)

test_IO_by_name('PIntSet', 'PInt0s', aPIntSet2PInts_by_sorted_sub)

aPInts2URational_by_cf.test()
test_IO_by_name('PInt0s', 'URational', aPInts2URational_by_cf)

test_IO_by_name('UInt', 'Digits_radix3', aUInt2Digits__LE_R3)
#rint(aUInt2UInt1s_by_digits__LE_R2.get_InputType().get_TypeName())
#rint(aUInt2UInt1s_by_digits__LE_R2.get_OutputType().get_TypeName())
test_IO_by_name('UInt', 'UInt1s', aUInt2UInt1s_by_digits__LE_R2)
test_IO_by_name('UInt', 'UInt1_4s', aUInt2UInt1Ms_by_digits__LE_M4_R2)

test_IO_by_name('Digits_radix3', 'BiDigits1s_radix2', aDigits2BiDigits1s_by_split0__radix_down__R3)
test_IO_by_name('Digits_radix3', 'BiDigits1Ms_mayDigits__R3_M3', aDigits2BiDigits1Ms_mayDigits_by_split0__radix_down__R3_M3)


test_IO_by_name('UInt3_3s', 'UInt0_3s', aUIntLLs2UInt0Ls_by_remove_head0s__L3)
test_IO_by_name('UInt4_4s', 'UInt1_4s', aUIntNLNLs2UIntNNLs__L3N1)
test_IO_by_name('UInt4_5s', 'UInt1_5s', aUIntNLMs2UIntNMs__L3N1M5)
test_IO_by_name('UInt', 'UInt4_4s', aUInt2UIntLLs_by_1digits_LE_2add_headMINs__L4R3)
test_IO_by_name('UInt1s', 'UInt', aUInt1s2UInt_by_1add1_2gcd_cf_3sub1_4LE_5add_head0s__R5)
test_IO_by_name('UInt', 'UInt', aUInt2UInt_by_0LE_1add1_2gcd_cf_3sub1_4LE_5add_head0s__R6R7)
#test_IO_by_name('UInt__many', 'UInt__many', aUInt2UInt_by_0LE_1add1_2gcd_cf_3sub1_4LE_5add_head0s__R6R7)
test_IO_by_name('UInt', 'UIntRadixReprLE__R300', UInt2UIntRadixReprLE(300))
test_IO_by_name('UIntRadixReprLE__R300', 'BiDigitChannels_UIntRadixReprLE_pair__R300N3', UIntRadixReprLE2BiDigitChannels_UIntRadixReprLE_by_endBy0(300,3))
test_IO_by_name('UIntRadixReprLE__R300', 'BiDigitChannels_UIntRadixReprLE_pair__R300N3', UIntRadixReprLE2BiDigitChunks_UIntRadixReprLE_by_split0(300,3))


for inv in [False, True]:
    aUInt2UInt_by_mod = UInt2UInt_by_mod(-5, -3, inv=inv)
    aUInt2UInt_by_mod.test()
    test_IO_by_name('UInt', 'UInt', aUInt2UInt_by_mod)
#test_IO_by_name('', '', )
#test_IO_by_name('', '', )
#test_IO_by_name('', '', )
#test_IO_by_name('', '', )
#test_IO_by_name('', '', )
#test_IO_by_name('', '', )
#test_IO_by_name('', '', )
#test_IO_by_name('', '', )
