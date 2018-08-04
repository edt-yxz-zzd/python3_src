

from .ArrayTV import ArrayGe0, ArrayGe1, ArrayTV
from .NumberTVs import PInt, UInt, BiDigit, Digit
from .SetTV import SetTV

PInts = ArrayGe0(PInt)
PInt1s = ArrayGe1(PInt)
PIntSet = SetTV(PInt)
UInts = ArrayGe0(UInt)


def BiDigits(radix):
    return ArrayGe0(BiDigit(radix))
def Digits(radix):
    return ArrayGe0(Digit(radix))


