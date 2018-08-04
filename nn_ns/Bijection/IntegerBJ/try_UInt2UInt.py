


from .UInt2UInt1s import \
    UInt2UInt_by_0LE_1add1_2gcd_cf_3sub1_4LE_5add_head0s
    #UInt2UInt_by_0LE_1add1_2gcd_cf_3sub1_4LE_5add_head0s__R6R7\
from itertools import count

M = 1000
def try_UInt2UInt(aUInt2UInt, M=M):
    print('print(i, i2o, o2i)')
    for i in range(M+1):
        i2o = aUInt2UInt.typechecked_forward(i)
        o2i = aUInt2UInt.typechecked_backward(i)
        print(i, i2o, o2i)

def apply_UInt2UInt1s_many_times(aUInt2UInt, M=M):
    for i in range(M+1):
        o = i
        print(i)
        for idx in count(1):
            o = aUInt2UInt.typechecked_forward(o)
            print(f'\t{i}[{idx}] = {o}')
            if o == i: break


def try_UInt2UInt_by_0LE_1add1_2gcd_cf_3sub1_4LE_5add_head0s(r1, r2, M=M):
    aUInt2UInt = UInt2UInt_by_0LE_1add1_2gcd_cf_3sub1_4LE_5add_head0s(r1, r2)
    try_UInt2UInt(aUInt2UInt, M)

if 0:
    try_UInt2UInt_by_0LE_1add1_2gcd_cf_3sub1_4LE_5add_head0s(2,2)
    try_UInt2UInt_by_0LE_1add1_2gcd_cf_3sub1_4LE_5add_head0s(20000,20000)


apply_UInt2UInt1s_many_times(UInt2UInt_by_0LE_1add1_2gcd_cf_3sub1_4LE_5add_head0s(2,2), M=M)

