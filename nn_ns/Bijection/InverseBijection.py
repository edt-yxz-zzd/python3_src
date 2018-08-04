

__all__ = '''
    inverse_bijection
    is_inverse_bijection_of
'''.split()

from .Bijection import Bijection
from .IdBijection import is_IdBijection

class InverseBijection(Bijection):
    def __init__(self, bijection):
        assert isinstance(bijection, Bijection), TypeError
        assert not isinstance(bijection, InverseBijection), TypeError
        assert not bijection.is_idBJ(), TypeError
        if bijection.is_idBJ(): raise TypeError
        if isinstance(bijection, InverseBijection): raise TypeError
        self.bijection = bijection
    def get_InputType(self):
        return self.bijection.get_OutputType()
    def get_OutputType(self):
        return self.bijection.get_InputType()
    def untypechecked_forward(self, input):
        return self.bijection.untypechecked_backward(input)
    def untypechecked_backward(self, output):
        return self.bijection.untypechecked_forward(output)
    def get_construct_info(self):
        return self.make_args_kwargs(self.bijection)
    def __repr__(self):
        return '(~{!r})'.format(self.bijection)

def inverse_bijection(bijection):
    if type(bijection) == InverseBijection:
        return bijection.bijection
    if is_IdBijection(bijection):
        return bijection
    if bijection.is_idBJ():
        return bijection.get_InputType().idBJ
    return InverseBijection(bijection)

def is_inverse_bijection_of(bijection0, bijection1):
    from .ChainedBijection import ChainedBijection
    assert isinstance(bijection0, Bijection)
    assert isinstance(bijection1, Bijection)
    if isinstance(bijection0, ChainedBijection) \
        and isinstance(bijection1, ChainedBijection):
        return all(map(__is_inverse_bijection_of
            , bijection0.bijections, reversed(bijection1.bijections)))
    return __is_inverse_bijection_of(bijection0, bijection1)

def __is_inverse_bijection_of(bijection0, bijection1):
    # inverse_bijection will do some simplification
    return ~bijection0 == ~~bijection1



