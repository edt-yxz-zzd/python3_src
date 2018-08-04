

__all__ = '''
    UInt2UIntLLs_by_1digits_LE_2add_headMINs
    aUInt2UIntLLs_by_1digits_LE_2add_headMINs__L4R3
    '''.split()
from .UInt2Digits import UInt2UInt1Ms_by_digits__LE
from .UIntLLs2UInt0Ls import XIntNLMs2XIntNMs_by_remove_shortest_array_suffix_headMINs
from ..abbr import UInt

def UInt2UIntLLs_by_1digits_LE_2add_headMINs(lenO, small_radix):
    '''UInt <-> UInt[L]

UInt
    <-> UInt[1..L]  # UInt2UInt1Ms_by_digits__LE
    <-> UInt[L..L]  # XIntNLMs2XIntNMs_by_remove_shortest_array_suffix_headMINs^-1
'''
    L = lenO
    b1 = UInt2UInt1Ms_by_digits__LE(L, small_radix)
    b2 = ~XIntNLMs2XIntNMs_by_remove_shortest_array_suffix_headMINs(UInt, L, 1, L)
    return UInt2UIntLLs__more(b1, b2)
def UInt2UIntLLs__more(aUInt2UIntNLs, aUIntNLs2UIntLLs):
    return +(aUInt2UIntNLs >> aUIntNLs2UIntLLs)


aUInt2UIntLLs_by_1digits_LE_2add_headMINs__L4R3 = UInt2UIntLLs_by_1digits_LE_2add_headMINs(4, 3)

