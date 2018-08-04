
__all__ = '''
    test_SuffixTree
    '''.split()


from .SuffixTree import SuffixTree
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


def test_SuffixTree():
    for i, array in enumerate(gen_arrays()):
        print(i, array)
        try:
            r = test_SuffixTree1(array)
        except:
            raise Exception(array)
        if not r:
            raise Exception(array)

def test_SuffixTree1(array):
    st = SuffixTree.from_uint_array(array, testing=True)
    return True


test_SuffixTree()


