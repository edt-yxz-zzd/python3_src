

from .codec import *

Decoder = TinyCaseDecoder
Encoder = TinyCaseEncoder
decode = Decoder().decode
encode = Encoder().encode
for i in range(0x80):
    assert i == decode(encode(i))





def test_non_tiny_case_codec(Encoder, Decoder):
    for uint_case in cases_TSLH:
        if uint_case != TINY_CASE:
            Encoder, Decoder = uint_case2Encoder_Decoder(uint_case)
            _test_non_tiny_case_codec(Encoder, Decoder, range(1000))
            _test_non_tiny_case_codec(Encoder, Decoder, [1<<i for i in range(1000)])
def _test_non_tiny_case_codec(Encoder, Decoder, rng):
    decode = Decoder().decode
    encode = Encoder().encode
    for i in rng:
        try:
            assert i == decode(encode(i))
        except:
            print(Encoder, Decoder)
            print(i, bin(i), i.bit_length())
            print(encode(i))
            print(decode(encode(i)))
            raise

test_non_tiny_case_codec(Encoder, Decoder)










