

__all__ = '''
    TupleBijection
    tuple_bijection
    pair_bijection
    mayBJs2TupleBJ
    '''.split()
from .Bijection import Bijection
from .TupleTV import tupleTV
from .IdBijection import id_of
from .utils import all_Bijections

# see also: IdBijection.id_of
class TupleBijection(Bijection):
    def __init__(self, *bijections):
        assert all_Bijections(bijections)
        self.bijections = bijections
        self.InputType = tupleTV(b.get_InputType() for b in bijections)
        self.OutputType = tupleTV(b.get_OutputType() for b in bijections)

    def is_idBJ(self):
        return all(b.is_idBJ() for b in self.bijections)
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return tuple(b.untypechecked_forward(i)
                    for b, i in zip(self.bijections, input))
    def untypechecked_backward(self, output):
        return tuple(b.untypechecked_backward(o)
                    for b, o in zip(self.bijections, output))

    def __repr__(self):
        # +(x * y * z)
        bs = self.bijections
        L = len(bs)
        if L >= 2:
            s = ' * '.join(map(repr, bs))
            return '(+({}))'.format(s)
        if L == 1:
            return '(+({!r} * ...))'.format(bs[0])
        return super().__repr__()
    def get_construct_info(self):
        bs = self.bijections
        return self.make_name_args_kwargs('TupleBJ', *bs)
def tuple_bijection(bijections):
    return TupleBijection(*bijections)
def pair_bijection(b0, b1):
    return TupleBijection(b0, b1)

def mayBJs2TupleBJ(InputTV, mayBJs):
    bs = list(mayBJs)
    assert isinstance(InputTV, TupleTV)
    if len(InputTV.type_verifiers) != len(bs): raise TypeError
    ts = InputTV.type_verifiers
    it = ((id_of(t) if b is None else e) for b, t in zip(bs, ts))
    return tuple_bijection(it)


