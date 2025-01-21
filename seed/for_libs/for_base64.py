r'''[[[
e ../../python3_src/seed/for_libs/for_base64.py

view ../../python3_src/seed/int_tools/digits/generic_base85.py
view ../../python3_src/seed/text/base64.py
    std=_mk_half_table('AZaz09++//==')
    urlsafe=_mk_half_table('AZaz09--__==')


py -m seed.for_libs.for_base64

#]]]'''#'''

__all__ = r'''
iter_find_best_parameters4IWordBasedRadixDigitsCodec
WordBasedRadixDigitsCodec__oradix_lt_iradix
    PaddingProtocol
DigitOrder
DecodeError






a85_alphabet
b85_alphabet


impl__base64__xx85encode_
impl__base64__xx85decode_

    impl__base64__xx85codec__mod
        impl__base64__a85encode
        impl__base64__a85decode

        impl__base64__b85encode
        impl__base64__b85decode


'''.split()#'''
__all__


######################
from seed.int_tools.digits.generic_base85 import iter_find_best_parameters4IWordBasedRadixDigitsCodec
from seed.int_tools.digits.generic_base85 import WordBasedRadixDigitsCodec__oradix_lt_iradix, PaddingProtocol, DigitOrder
from seed.int_tools.digits.generic_base85 import DecodeError


from seed.int_tools.digits.generic_base85 import a85_alphabet, b85_alphabet

from seed.int_tools.digits.generic_base85 import impl__base64__xx85encode_, impl__base64__xx85decode_

from seed.int_tools.digits.generic_base85 import impl__base64__xx85codec__mod
from seed.int_tools.digits.generic_base85 import impl__base64__a85encode, impl__base64__a85decode
from seed.int_tools.digits.generic_base85 import impl__base64__b85encode, impl__base64__b85decode
######################


######################
def __():
    # seed.text.base64
    #######
    from seed.text.base64 import uint__to__radix64_digits_, uint__from__radix64_digits_, uint__to__radix64_digits__b64__str_, uint__from__radix64_digits__b64__str_
    #######
    from seed.text.base64 import \
(uint__to__radix64_digits_
,uint__from__radix64_digits_
,   uint__to__radix64_digits__b64__bytes_
,   uint__from__radix64_digits__b64__bytes_
,
,   uint__to__radix64_digits__b64__str_
,   uint__from__radix64_digits__b64__str_
)

    #######
    from seed.text.base64 import \
(b64_cfg_case2b64_alphabet_and_pad_byte
,b64_cfg_case2table_pair

,b64encode__bs2bs__altchars
,b64decode__bs2bs__altchars
,   b64encode__bs2bs__std
,   b64decode__bs2bs__std
,   b64encode__bs2bs__urlsafe
,   b64decode__bs2bs__urlsafe
,       b64encode__bs2bs_
,       b64decode__bs2bs_
,           b64encode__uint2bs_
,           b64decode__uint5bs_
,               b64encode__uint2str_
,               b64decode__uint5str_
,
,           uint__to__radix64_digits__b64__bytes_
,           uint__from__radix64_digits__b64__bytes_
,               uint__to__radix64_digits__b64__str_
,               uint__from__radix64_digits__b64__str_
,
,               uint__to__radix64_digits_
,               uint__from__radix64_digits_
)
    #######
#end-def __():


######################


from seed.for_libs.for_base64 import *
