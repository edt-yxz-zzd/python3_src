'''
[PInt]
    <-[append 1]-> [PInt]{len(.)>=1, .[-1]=1}
    <-[continued fraction]-> Rational{.>=1}
    <-[-1]-> Rational{.>=0}
    <-> (UInt, PInt){gcd(.)==1}
[PInt]{len(.)>=1}
    <-[head]-> (PInt, [PInt])
    <-[see above]-> (PInt, (UInt, PInt){gcd(.)==1})
    <-[mul]-> (UInt, PInt)

'''

__all__ = ['pint1s_2_uint_pint_by_gcd_cf']
from ..SeqBJ import SplitHead
from ..NumberTVs import PInt
from ..abbr import PInt1s
from .PInts2URational_by_cf import aPInts2URational_by_cf
from .PInt_URational_2_UInt_PInt_by_mulGCD import aPInt_URational_2_UInt_PInt_by_mulGCD
'''
from ..ChainedBijection import ChainedBijection
from ..TupleBijection import pair_bijection
from ..IdBijection import id_of
from ..ArrayHeadBJ import ArrayHeadBJ
pint1s_2_uint_pint = ChainedBijection(
                      ArrayHeadBJ(PInt, 1)
                    , pair_bijection(id_of(PInt), aPInts2URational_by_cf)
                    , aPInt_URational_2_UInt_PInt_by_mulGCD
                    )
'''
pint1s_2_uint_pint_by_gcd_cf = +( SplitHead(PInt1s) >>
                                +(PInt.idBJ * aPInts2URational_by_cf) >>
                                aPInt_URational_2_UInt_PInt_by_mulGCD
                                )

if __name__ == '__main__':
    print(pint1s_2_uint_pint_by_gcd_cf)
