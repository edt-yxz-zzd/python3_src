

__all__ = '''
    UInt2UIntRadixReprLE
    PInt2PIntRadixReprLE
    '''.split()

from ..Bijection import Bijection
from ..NumberTVs import UIntRadixReprLE, UInt, IntGeLeTV, PInt, PIntRadixReprLE
from .SplitIntBJ import SplitIntBJ
from ..ArbitraryRadixNumber import \
    arbitrary_radix_repr_maypairLE2number \
    , number2arbitrary_radix_repr_maypairLE
from ..UniqueBJ import SingletonTV_BJ
from ..ChoiceOfTuple2UnionBJ import ChoiceOfTuple2UnionBJ


def UInt2UIntRadixReprLE(radix):
    '''\
UInt
    <-> <left=0, right=PInt>    # SplitIntBJ
    <-> <left=(), right=PInt>   # SingletonTV_BJ
    <-> <left=(), right=PIntRadixReprLE(R)>   # PInt2PIntRadixReprLE
    <-> UIntRadixReprLE(R)      # ChoiceOfTuple2UnionBJ
'''
    b1 = SplitIntBJ(UInt, 0)

    emptyTpl = UInt.TupleTV()
    rightBJ = PInt2PIntRadixReprLE(radix)
    b2 = +(SingletonTV_BJ(IntGeLeTV(0,0), emptyTpl) / rightBJ)

    OutputType = UIntRadixReprLE(radix)
    b3 = ChoiceOfTuple2UnionBJ(b2.get_OutputType(), OutputType)
    return +(b1 >> b2 >> b3)
class PInt2PIntRadixReprLE(Bijection):
    'Int{1..} <-> ([Int{0..R-1}], Int{1..R-1})'
    def __init__(self, radix):
        assert radix >= 1, TypeError
        self.radix = radix
        self.OutputType = PIntRadixReprLE(radix)

    def get_InputType(self):
        return PInt
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        tailLE, head = number2arbitrary_radix_repr_maypairLE(input, self.radix, 0, divmod, tuple)
        return tailLE, head
    def untypechecked_backward(self, output):
        tailLE, head = output
        return arbitrary_radix_repr_maypairLE2number(output, self.radix, 0)

    def get_construct_info(self):
        return self.make_args_kwargs(self.radix)




