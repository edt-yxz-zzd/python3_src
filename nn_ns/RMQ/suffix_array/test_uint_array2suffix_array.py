
__all__ = '''
    test_uint_array2suffix_array
    '''.split()


from .suffix_array_definition import suffix_array_definition
from .lcp_array_definition import lcp_array_definition
from nn_ns.Bijection.IntegerBJ.UInt2Digits import UInt2Digits__LE
def gen_arrays():
    yield []
    for i in range(2**16):
        bs = bin(i)[2:]
        yield list(map(int, bs))

    aUInt2Digits__LE_R3 = UInt2Digits__LE(3)
    uint2digits__LE_R3 = aUInt2Digits__LE_R3.typechecked_forward
    for i in range(2**16):
        ds = uint2digits__LE_R3(i)
        yield ds

    aUInt2Digits__LE_R4 = UInt2Digits__LE(4)
    uint2digits__LE_R4 = aUInt2Digits__LE_R4.typechecked_forward
    for i in range(2**16):
        ds = uint2digits__LE_R4(i)
        yield ds


def test_uint_array2suffix_array(uint_array2suffix_array):
    for i, array in enumerate(gen_arrays()):
        print(i, array)
        try:
            r = test_uint_array2suffix_array1(uint_array2suffix_array, array)
        except:
            raise Exception(array)
        if not r:
            raise Exception(array)

def test_uint_array2suffix_array1(uint_array2suffix_array, array):
    SA, LCP = uint_array2suffix_array(None, array, LCP=True)
    SA_def = suffix_array_definition(array)
    LCP_def = lcp_array_definition(array, SA)
    r = SA == SA_def and LCP == LCP_def
    if not r:
        print(SA)
        print(SA_def)
        print(LCP)
        print(LCP_def)
    return r

