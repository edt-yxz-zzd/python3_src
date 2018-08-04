
__all__ = ['aPInt_URational_2_UInt_PInt_by_mulGCD']

from ..Bijection import Bijection
from ..NumberTVs import URational, PInt, UInt
from ..TupleTV import PairTV
from .import_cf import ND2Fraction, Fraction2ND

class PInt_URational_2_UInt_PInt_by_mulGCD(Bijection):
    InputType = PairTV(PInt, URational)
    OutputType = PairTV(UInt, PInt)
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        gcd, fr = input
        n, d = Fraction2ND(fr)
        return gcd*n, gcd*d
    def untypechecked_backward(self, output):
        u, p = nd = output
        fr = ND2Fraction(nd)
        n, d = Fraction2ND(fr)
        gcd = p // d
        return gcd, fr
    def get_construct_info(self):
        return 'aPInt_URational_2_UInt_PInt_by_mulGCD'
aPInt_URational_2_UInt_PInt_by_mulGCD = PInt_URational_2_UInt_PInt_by_mulGCD()

