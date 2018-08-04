

__all__ = 'UnionBijection union_bijection'.split()
from .Bijection import Bijection
from .UnionTV import UnionTV, unionTV
from .IdBijection import id_of
from .utils import all_Bijections
from .import_FrozenDict import FrozenDict

# see also: IdBijection.id_of
class UnionBijection(Bijection):
    # I/O should have no same instances
    def __init__(self, *disjoint_bijections):
        assert all_Bijections(disjoint_bijections), TypeError
        self.InputTV2BJ = FrozenDict(
            (b.get_InputType(), b) for b in disjoint_bijections}
        self.OutputTV2BJ = FrozenDict(
            (b.get_OutputType(), b) for b in disjoint_bijections}
        assert len(self.InputTV2BJ) == len(disjoint_bijections) == len(self.OutputTV2BJ), TypeError

        self.InputType = unionTV(self.InputTV2BJ)
        self.OutputType = unionTV(self.OutputTV2BJ)

    def is_idBJ(self):
        return all(b.is_idBJ() for b in self.InputTV2BJ.values())
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        I = self.get_InputType().which_Type(input)
        bj = self.InputTV2BJ[I]
        return bj.untypechecked_forward(input)
    def untypechecked_backward(self, output):
        O = self.get_OutputType().which_Type(output)
        bj = self.OutputTV2BJ[O]
        return bj.untypechecked_backward(output)
    def __repr__(self):
        # +(x + y + z)
        bs = list(self.InputTV2BJ.values())
        bs.sort(key = repr)
        if L >= 2:
            s = ' + '.join(map(repr, bs))
            return '(+({}))'.format(s)
        if L == 1:
            return '(+({!r} + ...))'.format(bs[0])
        return super().__repr__()
    def get_construct_info(self):
        bs = list(self.InputTV2BJ.values())
        bs.sort(key = repr)
        return self.make_name_args_kwargs('UnionBJ', *bs)
def union_bijection(disjoint_bijections):
    return UnionBijection(*disjoint_bijections)

