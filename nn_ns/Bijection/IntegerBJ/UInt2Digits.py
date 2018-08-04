


'''
let UInts[m..M] = UInts{m<=len(.)<=M}
UInt <-> Digits
    # via little/big-endian offseted digits
    # bijective numeration
    # https://en.wikipedia.org/wiki/Bijective_numeration
Digits <-> UInt1s
    # split all 0s
Digits <-> UInts[1..M]
    # split first (M-1) 0s


'''
__all__ = '''
    UInt2BiDigits__little_endian
    BiDigit2Digit_by_sub1
    BiDigits2Digits_by_sub1
    UInt2Digits__LE
    aUInt2Digits__LE_R3

    Digits2BiDigits1s_by_split0__radix_down
    Digits2BiDigits1Ms_mayDigits_by_split0__radix_down
    aDigits2BiDigits1s_by_split0__radix_down__R3
    aDigits2BiDigits1Ms_mayDigits_by_split0__radix_down__R3_M3

    UInt2UInt1s_by_digits__LE
    UInt2UInt1s_by_digits__more
    aUInt2UInt1s_by_digits__LE_R2

    UInt2UInt1Ms_by_digits__LE
    UInt2UInt1Ms_by_digits__more
    aUInt2UInt1Ms_by_digits__LE_M4_R2
    '''.split()

from ..abbr import UInt, Digit, BiDigit, BiDigits, Digits
from ..ArrayTV import ArrayTV, ArrayJust
from ..ChoiceTV import ChoiceTV, make_choice

from ..Bijection import Bijection
from ..TupleBijection import TupleBijection, pair_bijection
from ..InverseBijection import inverse_bijection
from ..SeqBJ import SplitArrayLast, ArrayUnion2Choices
from ..ChoiceBijection import choice_bijection
from ..BijectiveNumeration import \
    bidigits2uint__little_endian, uint2bidigits__little_endian

from .import_split_seq import split_seq2seq1s, join
from itertools import chain

class UInt2BiDigits__little_endian(Bijection):
    def __init__(self, radix):
        self.OutputType = BiDigits(radix)
        self.radix = radix
    def get_InputType(self):
        return UInt
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return uint2bidigits__little_endian(self.radix, input)
    def untypechecked_backward(self, output):
        return bidigits2uint__little_endian(self.radix, output)
    def get_construct_info(self):
        return self.make_args_kwargs(self.radix)


class BiDigit2Digit_by_sub1(Bijection):
    def __init__(self, radix):
        self.InputType = BiDigit(radix)
        self.OutputType = Digit(radix)
        self.radix = radix
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return input - 1
    def untypechecked_backward(self, output):
        return output + 1
    def get_construct_info(self):
        return self.make_args_kwargs(self.radix)

def BiDigits2Digits_by_sub1(radix, min_len=0, max_len=None):
    return BiDigit2Digit_by_sub1(radix)[min_len, max_len]
def UInt2Digits__LE(radix):
    return +(UInt2BiDigits__little_endian(radix)
            >> BiDigits2Digits_by_sub1(radix))

aUInt2Digits__LE_R3 = UInt2Digits__LE(3)



##########################################

class Digits2BiDigits1s_by_split0__radix_down(Bijection):
    # Digit.radix == BiDigit.radix + 1
    def __init__(self, digit_radix):
        self.digit_radix = digit_radix
        self.InputType = Digits(digit_radix)
        self.OutputType = BiDigits(digit_radix-1)[1,None]
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return split_seq2seq1s(input, 0, tuple)
    def untypechecked_backward(self, output):
        return join((0,), output, tuple)
    def get_construct_info(self):
        return self.make_args_kwargs(self.digit_radix)
aDigits2BiDigits1s_by_split0__radix_down__R3 \
    = Digits2BiDigits1s_by_split0__radix_down(3)


class Digits2BiDigits1Ms_mayDigits_by_split0__radix_down(Bijection):
    # Digit.radix == BiDigit.radix + 1
    '''
Error: Digits(R) <-> ([BiDigits(R-1)]{0..M}, Digits(R))
    M = 3:
        [1,0,2] -> [1], [2]; []
        [1,0,2,0,3] -> [1], [2], [3]; []    # the same!
        [1,0,2,0,3,0] -> [1], [2], [3]; []  # the same!
        [1,0,2,0,3,0,4] -> [1], [2], [3]; [4]
ShouldBe: Digits(R) <-> <left=[BiDigits(R-1)]{1..M}  # begin from 1 not 0!!
                          ,right=([BiDigits(R-1)]{M}, Digits(R)))>
    M = 3:
        [1,0,2] -> <left=[[1], [2]]>
        [1,0,2,0,3] -> <left=([1], [2], [3])>
        [1,0,2,0,3,0] -> <right=([1], [2], [3]; [])>
        [1,0,2,0,3,0,4] -> <right=([1], [2], [3]; [4])>
    '''
    def __init__(self, digit_radix, max_len):
        assert type(max_len) is int and max_len >= 1
        left = ArrayTV(BiDigits(digit_radix-1), 1, max_len)
        right_fst = ArrayJust(BiDigits(digit_radix-1), max_len)
        right_snd = Digits(digit_radix)

        self.InputType = right_snd
        self.OutputType = ChoiceTV(left=left, right=+(right_fst * right_snd))
        self.left_max_lenO = max_len
        self.digit_radix = digit_radix
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        # bug:
        #   bidigits0Ms = split_seq2seq1s(input, 0, tuple, self.left_max_lenO)
        #   remain_digits = input[sum(map(len, bidigits0Ms)):]
        bidigits0Ms_digits = split_seq2seq1s(input, 0, tuple, self.left_max_lenO)
        assert len(bidigits0Ms_digits) >= 1
        if len(bidigits0Ms_digits) <= self.left_max_lenO:
            bidigits0Ms = bidigits0Ms_digits
            return make_choice(left = bidigits0Ms)

        assert len(bidigits0Ms_digits) == self.left_max_lenO+1
        bidigits0Ms = bidigits0Ms_digits[:-1]
        remain_digits = bidigits0Ms_digits[-1]
        r = make_choice(right = (bidigits0Ms, remain_digits))
        return r
    def untypechecked_backward(self, output):
        tag, data = output
        if tag == 'left':
            ss = bidigits0Ms = data
        else:
            bidigits0Ms, remain_digits = data
            ss = chain(bidigits0Ms, [remain_digits])
        r = join((0,), ss, tuple)
        return r
    def get_construct_info(self):
        return self.make_args_kwargs(self.digit_radix, self.left_max_lenO)
aDigits2BiDigits1Ms_mayDigits_by_split0__radix_down__R3_M3 \
    = Digits2BiDigits1Ms_mayDigits_by_split0__radix_down(3,3)




##################################
def UInt2UInt1s_by_digits__LE(small_radix):
    big_radix = small_radix+1
    uint2digits = UInt2Digits__LE(big_radix)
    # digits2uint = inverse_bijection(UInt2Digits__LE(small_radix))
    bidigits2uint = inverse_bijection(UInt2BiDigits__little_endian(small_radix))
    return UInt2UInt1s_by_digits__more(small_radix, uint2digits, bidigits2uint)
def UInt2UInt1s_by_digits__more(
    small_radix, uint2digits:'big_radix', bidigits2uint:'small_radix'):
    'UInt<->Digits(radix+1)<->BiDigits1s(radix)<->UInt1s'
    assert small_radix > 0

    big_radix = small_radix+1
    digits2bidigits1s = Digits2BiDigits1s_by_split0__radix_down(big_radix)
    bidigits1s_2_uint1s = bidigits2uint[1,None]
    return +(uint2digits >> digits2bidigits1s >> bidigits1s_2_uint1s)
aUInt2UInt1s_by_digits__LE_R2 = UInt2UInt1s_by_digits__LE(2)


##################################
def UInt2UInt1Ms_by_digits__LE(max_len, small_radix):
    big_radix = small_radix+1
    uint2digits = UInt2Digits__LE(big_radix)
    bidigits2uint = inverse_bijection(UInt2BiDigits__little_endian(small_radix))
    return UInt2UInt1Ms_by_digits__more(max_len, small_radix, uint2digits, bidigits2uint)
def UInt2UInt1Ms_by_digits__more(
    max_len
    , small_radix
    , uint2digits:'big_radix'
    , bidigits2uint:'small_radix'):
    '''UInt
    <-> Digits(radix+1)
    <-> <[BiDigits(radix)]{1..M-1} | ([BiDigits(radix)]{M-1}, Digits(radix+1))>
    <-> <[UInt]{1..M-1}            | ([UInt]{M-1}, UInt)>
    <-> <[UInt]{1..M-1}            | [UInt]{M}>
    <-> [UInt]{1..M}
    '''
    if max_len is None:
        return UInt2UInt1s_by_digits__more(small_radix, uint2digits, bidigits2uint)
    assert max_len >= 2
    assert small_radix >= 1

    M = max_len
    big_radix = small_radix+1

    b1 = uint2digits
    b2 = Digits2BiDigits1Ms_mayDigits_by_split0__radix_down(big_radix, M-1)

    b3_left_elem = bidigits2uint
    b3_left = b3_left_elem[1, M-1]

    b3_right_b1_fst_elem = bidigits2uint
    b3_right_b1_fst = b3_right_b1_fst_elem[M-1, M-1]
    digits2uint__big = inverse_bijection(uint2digits)
    b3_right_b1_snd = digits2uint__big
    b3_right_b1 = pair_bijection(b3_right_b1_fst, b3_right_b1_snd)
    b3_right_b2_OutputType = ArrayJust(UInt, M)
    b3_right_b2 = inverse_bijection(SplitArrayLast(b3_right_b2_OutputType))
    #from ..utils import print_IO_of_BJs
    #print_IO_of_BJs(b3_right_b1, b3_right_b2)
    b3_right = +(b3_right_b1 >> b3_right_b2)

    b3 = choice_bijection(left = b3_left, right = b3_right)

    OutputType = ArrayTV(UInt, 1, M)
    b4 = inverse_bijection(ArrayUnion2Choices(OutputType, M-1))
    return +(b1 >> b2 >> b3 >> b4)

aUInt2UInt1Ms_by_digits__LE_M4_R2 = UInt2UInt1Ms_by_digits__LE(4, 2)



#rint('\n'.join(sorted(globals().keys())))
#rint('\n'.join(globals().keys()))

