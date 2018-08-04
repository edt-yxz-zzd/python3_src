
'''
[PInt]
    <-[append 1]-> [PInt]{len(.)>=1, .[-1]=1}
    <-[continued fraction]-> Rational{.>=1}
    <-[-1]-> Rational{.>=0}
    <-> (UInt, PInt){gcd(.)==1}
'''

__all__ = ['aPInts2URational_by_cf']
from ..Bijection import Bijection
from ..NumberTVs import URational
from ..abbr import PInts
from .import_cf import CF2ND, _ND2CF, ND2Fraction, Fraction2ND

def ND2CF(ND):
    # assume to append 1 after cf
    # -2 == [-2] == [-3] ++ [1] ==>> [-3]
    # 2 == [2] == [1] ++ [1] ==>> [1]
    # 2/3 == [0,1,2] == [0,1,1] ++ [1] ==>> [0,1,1]
    # 1 == [1] == [] ++ [1] ==>> []
    *cf, = _ND2CF(ND)
    assert len(cf) == 1 or cf[-1] > 1
    if cf[-1] == 1:
        cf = cf[:-1]
    else:
        cf[-1] -= 1
    return cf

class PInts2URational_by_cf(Bijection):
    def get_InputType(self):
        return PInts
    def get_OutputType(self):
        return URational
    def untypechecked_forward(self, input):
        cf = input + (1,)
        nd = CF2ND(cf)
        fr = ND2Fraction(nd) - 1
        return fr
    def untypechecked_backward(self, output):
        fr = output + 1
        nd = Fraction2ND(fr)
        cf = ND2CF(nd)
        pints = tuple(cf)
        return pints
    def get_construct_info(self):
        return 'aPInts2URational_by_cf'
aPInts2URational_by_cf = PInts2URational_by_cf()

