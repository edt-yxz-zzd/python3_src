

__all__ = '''
    aUInt2PInt_by_add1
    XInt2YInt_by_add
    XInt2YInt_by_mirror
    '''.split()

from ..Bijection import Bijection
from ..NumberTVs import PInt, UInt, IntGeLeTV

'''
class UInt2PInt_by_add1(Bijection):
    def get_InputType(self):
        return UInt
    def get_OutputType(self):
        return PInt
    def untypechecked_forward(self, input):
        return input + 1
    def untypechecked_backward(self, output):
        return output - 1
    def get_construct_info(self):
        return 'aUInt2PInt_by_add1'
aUInt2PInt_by_add1 = UInt2PInt_by_add1()
aUInt2PInt_by_add1.test()
'''


class XInt2YInt_by_add(Bijection):
    def __init__(self, InputType, offset):
        if not isinstance(InputType, IntGeLeTV): raise TypeError
        if type(offset) is not int: raise TypeError
        rngI = InputType.int_range
        rngO = rngI.shift_range(offset)

        self.InputType = InputType
        self.OutputType = IntGeLeTV(*rngO.get_args())
        self.offset = offset
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return input + self.offset
    def untypechecked_backward(self, output):
        return output - self.offset
    def get_construct_info(self):
        return self.make_args_kwargs(self.InputType, self.offset)
aUInt2PInt_by_add1 = XInt2YInt_by_add(UInt, 1)
aUInt2PInt_by_add1.test()


class XInt2YInt_by_mirror(Bijection):
    def __init__(self, InputType, center):
        if not isinstance(InputType, IntGeLeTV): raise TypeError
        if type(center) is not int: raise TypeError
        rngI = InputType.int_range
        rngO = rngI.mirror_range(center)

        self.InputType = InputType
        self.OutputType = IntGeLeTV(*rngO.get_args())
        self.center = center
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return self.center - input
    def untypechecked_backward(self, output):
        return self.center - output
    def get_construct_info(self):
        return self.make_args_kwargs(self.InputType, self.center)
for center in range(-1, 4):
    XInt2YInt_by_mirror(UInt, center).test()

