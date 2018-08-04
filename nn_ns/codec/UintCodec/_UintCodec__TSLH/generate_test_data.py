
from .codec import *
from itertools import chain
from pprint import pprint
import os.path

case__uint_bytes_pairs__pairs = []
for case in cases_TSLH:
    if case == TINY_CASE:
        rng = range(0x80)
    else:
        rng1 = range(1000)
        rng2 = (1<<i for i in range(1000))
        rng = chain(rng1, rng2)

    Encoder, Decoder = uint_case2Encoder_Decoder(case)
    decode = Decoder().decode
    encode = Encoder().encode
    ls = [(u, encode(u)) for u in rng]
    for u, bs in ls:
        assert u == decode(bs)
    case__uint_bytes_pairs__pairs.append((case, ls))


fname = 'test_data.txt'
folder = os.path.dirname(__file__)
path = os.path.join(folder, fname)
with open(path, 'w') as fout:
    pprint(case__uint_bytes_pairs__pairs, stream=fout)











