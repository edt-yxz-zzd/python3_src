
r'''
forward input: pintI=23, odd_int_K=3, int_A=5
output: pintO=26
impl:
    23 == 0b10111 == 0b10000 + 0b111 == 16 + 7
    16 | ((7*3+5)&(16-1)) == 16 + (7*3+5)%16 == 16 + 10 == 26

backward input: pintO=26, odd_int_K=3, int_A=5
output: pintI=23
impl:
    26 == 0b11010 == 0b10000 + 0b1010 == 16 + 10
    (11*3)%16 == 1
    16 | (((10-5)*11)&(16-1)) == 16 + ((10-5)*11)%16 == 16 + 7 == 23

'''

__all__ = '''
    UInt2UInt_by_mod
    '''.split()

from ..abbr import UInt
from ..Bijection import Bijection
#from nn_ns.math_nn.integer.mod import invmod as invmod_2pow
from nn_ns.math_nn.integer.inv_mod_pow import InvModPow

assert 23 == 0b10111 == 0b10000 + 0b111 == 16 + 7
assert 16 | ((7*3+5)&(16-1)) == 16 + (7*3+5)%16 == 16 + 10 == 26
assert 26 == 0b11010 == 0b10000 + 0b1010 == 16 + 10
assert (11*3)%16 == 1
assert 16 | (((10-5)*11)&(16-1)) == 16 + ((10-5)*11)%16 == 16 + 7 == 23


_inv_mod_2pow = InvModPow(2)
def invmod_2pow(digit, modulus):
    L = modulus.bit_length() - 1
    assert modulus == 1<<L
    return _inv_mod_2pow(digit, L)

def split_MSB(pint):
    # pint -> (modulus, digit)
    # pint -> (radix, digit)
    assert pint > 0
    L = pint.bit_length()
    assert L > 0
    modulus = 1 << (L-1)
    mask = modulus-1
    digit = pint & mask
    assert digit + modulus == digit | modulus == pint
    assert 0 <= digit < modulus
    return modulus, digit
assert split_MSB(1) == (1, 0)
assert split_MSB(2) == (2, 0)
assert split_MSB(3) == (2, 1)
assert split_MSB(4) == (4, 0)
assert split_MSB(5) == (4, 1)
assert split_MSB(7) == (4, 3)


def _inv_without_verify(digitI, modulus):
    # modulus == 2**x >= 2
    assert modulus >= 2

    odd = digitI & 1
    if not odd: digitI -= 1
    digitO = invmod_2pow(digitI, modulus)
    if not odd: digitO += 1
    digitO %= modulus
    if digitO & 1 != odd: raise logic-error
    return digitO
def _inv_with_verify(digitI, modulus):
    digitI %= modulus # to let the below "if digitI != ..." happy
    digitO = _inv_without_verify(digitI, modulus)
    if digitI != _inv_without_verify(digitO, modulus):
        print(digitI, modulus, digitO)
        raise logic-error
    return digitO

def forward_uint2uint_by_mod(odd_int_K, int_A, uint, *, inv:bool=False):
    if uint < 2: return uint
    pintI = uint
    modulus, digitI = split_MSB(pintI)
    if abs(odd_int_K) > modulus:
        odd_int_K %= modulus
    if abs(int_A) > modulus:
        int_A %= modulus

    if inv:
        digitI = _inv_with_verify(digitI, modulus)

    digitO = digitI * odd_int_K + int_A
    digitO %= modulus
    pintO = modulus | digitO
    return pintO
def backward_uint2uint_by_mod(odd_int_K, int_A, uint, *, inv:bool=False):
    if uint < 2: return uint
    pintO = uint
    modulus, digitO = split_MSB(pintO)
    if abs(odd_int_K) > modulus:
        odd_int_K %= modulus
    if abs(int_A) > modulus:
        int_A %= modulus
    inv_K = invmod_2pow(odd_int_K, modulus)

    digitI = (digitO - int_A) * inv_K
    if inv:
        digitI = _inv_with_verify(digitI, modulus)
    digitI %= modulus

    pintI = modulus | digitI
    return pintI

class UInt2UInt_by_mod(Bijection):
    def __init__(self, odd_int_K, int_A, *, inv:bool):
        if type(odd_int_K) is not int: raise TypeError
        if type(int_A) is not int: raise TypeError
        if not (odd_int_K & 1): raise ValueError

        self.odd_int_K = odd_int_K
        self.int_A = int_A
        self.inv = bool(inv)

    def get_InputType(self):
        return UInt
    def get_OutputType(self):
        return UInt
    def untypechecked_forward(self, input):
        return forward_uint2uint_by_mod(self.odd_int_K, self.int_A, input, inv=self.inv)
    def untypechecked_backward(self, output):
        return backward_uint2uint_by_mod(self.odd_int_K, self.int_A, output, inv=self.inv)
    def get_construct_info(self):
        return self.make_args_kwargs(self.odd_int_K, self.int_A, inv=self.inv)


def _t(inv):
    from ..test_IO_by_name import test_IO_by_name
    aUInt2UInt_by_mod = UInt2UInt_by_mod(-5, -3, inv=inv)
    aUInt2UInt_by_mod.test()
    test_IO_by_name('UInt', 'UInt', aUInt2UInt_by_mod)

    backward = aUInt2UInt_by_mod.untypechecked_backward
    forward = aUInt2UInt_by_mod.untypechecked_forward
    for n in [23425,64354, 224, 0, 1, 2, 3, 3342, 3, 4]:
        assert backward(forward(n)) == n
        assert forward(backward(n)) == n
if __name__ == '__main__':
    _t(inv=True)
    _t(inv=False)
del _t



