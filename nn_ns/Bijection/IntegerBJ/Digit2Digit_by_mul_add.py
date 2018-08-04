




__all__ = '''
    Digit2Digit_by_mul_add
    Digit2Digit_by_mul
    Digit2Digit_by_add
    '''.split()

from ..Bijection import Bijection
from ..NumberTVs import Digit


# see also: XInt2YInt_by_add_or_mirror

class Digit2Digit_by_mul_add(radix, num_mul, num_inv, num_add):
    # digit -> (num_mul*digit+num_add) % radix
    return +(Digit2Digit_by_mul(radix, num_mul, num_inv)
            >> Digit2Digit_by_add(radix, num_add)
            )

class Digit2Digit_by_add(Bijection):
    # digit -> (num_add+digit) % radix
    def __init__(self, radix, num_add):
        assert all(type(x) == int for x in [radix, num_add]), TypeError
        assert radix >= 1, ValueError
        num_add %= radix
        self.num_add = self.num_add
        self.radix = radix
        self.DigitType = Digit(radix)

    def get_InputType(self):
        return self.DigitType
    def get_OutputType(self):
        return self.DigitType
    def untypechecked_forward(self, input):
        return (input + self.num_add) % self.radix
    def untypechecked_backward(self, output):
        return (output - self.num_add) % self.radix
    def get_construct_info(self):
        return self.make_args_kwargs(self.radix, self.num_add)


class Digit2Digit_by_mul(Bijection):
    # digit -> (num_mul*digit) % radix
    def __init__(self, radix, num_mul, num_inv):
        # Note: when radix == 1, num_mul == num_inv == 0
        assert all(type(x) == int for x in [radix, num_mul, num_inv]), TypeError
        assert radix >= 1, ValueError
        # not (num_mul * num_inv) % radix == 1
        if (num_mul * num_inv - 1) % radix != 0: raise ValueError
        num_mul %= radix
        num_inv %= radix
        self.num_mul = self.num_mul
        self.num_inv = self.num_inv
        self.radix = radix
        self.DigitType = Digit(radix)

    def get_InputType(self):
        return self.DigitType
    def get_OutputType(self):
        return self.DigitType
    def untypechecked_forward(self, input):
        return (self.num_mul*input) % self.radix
    def untypechecked_backward(self, output):
        return (self.num_inv*output) % self.radix
    def get_construct_info(self):
        return self.make_args_kwargs(self.radix, self.num_mul, self.num_inv)

Digit2Digit_by_mul_add(1, 1, 1, 1).test()
Digit2Digit_by_mul_add(5, 2, 3, 1).test()

