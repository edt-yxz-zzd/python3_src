

__all__ = 'chainable ChainedBijection chain_bijections'.split()
from .Bijection import Bijection
from .IdBijection import id_bijection
from .InverseBijection import is_inverse_bijection_of

from .utils import all_Bijections
from itertools import chain

def chainable(b0, b1):
    return b0.get_OutputType() == b1.get_InputType()
class ChainedBijection(Bijection):
    def __init__(self, *bijections):
        assert len(bijections) > 1, TypeError
        assert all_Bijections(bijections), TypeError
        assert not any(b.is_idBJ() for b in bijections), TypeError
        assert not any(isinstance(b, ChainedBijection) for b in bijections), TypeError
        assert all(map(chainable, bijections, bijections[1:])), TypeError
        assert not any(map(is_inverse_bijection_of, bijections, bijections[1:])), TypeError
        self.bijections = bijections
    def get_InputType(self):
        return self.bijections[0].get_InputType()
    def get_OutputType(self):
        return self.bijections[-1].get_OutputType()
    def untypechecked_forward(self, input):
        for b in self.bijections:
            input = b.untypechecked_forward(input)
        return input
    def untypechecked_backward(self, output):
        # bug: for b in self.bijections: # forgot "reversed"
        for b in reversed(self.bijections):
            output = b.untypechecked_backward(output)
        return output

    def __repr__(self):
        # Note: b[...] ==>> +(...)[...] ==>> +((...)[...]) # Error!!
        # bug: '+({})' instead of '(+({}))'
        s = ' >> '.join(map(repr, self.bijections))
        return '(+({}))'.format(s)
    def get_construct_info(self):
        return self.make_args_kwargs(*self.bijections)
def chain_bijections(bijections):
    bijections = tuple(bijections)
    if not bijections: raise TypeError

    # save InputType
    b0 = bijections[0]

    # expand ChainedBijection
    bijections = chain.from_iterable(
                    b.bijections if isinstance(b, ChainedBijection) else [b]
                    for b in bijections)
    # remove idBJ
    bijections = (b for b in bijections if not b.is_idBJ())

    # remove adjacent inv bijection pair
    ls = []
    for b in bijections:
        if ls and is_inverse_bijection_of(b, ls[-1]):
            ls.pop()
        else:
            ls.append(b)
    if not ls:
        return b0.get_InputType().id_BJ
    del b0
    bijections = ls

    L = len(bijections)
    if L > 1: return ChainedBijection(*bijections)
    bijection, = bijections

    # inverse_bijection will do some simplification
    return ~~bijection


