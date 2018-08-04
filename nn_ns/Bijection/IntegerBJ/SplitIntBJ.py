

__all__ = 'SplitIntBJ'.split()
from ..Bijection import Bijection
from ..NumberTVs import IntGeLeTV
from ..ChoiceTV import make_choice

class SplitIntBJ(Bijection):
    'Int{min..max} <-> <left=Int{min..mid}, right=Int{mid+1..max}>'
    def __init__(self, InputType, left_max):
        assert isinstance(InputType, IntGeLeTV), TypeError
        assert type(left_max) is int
        rng = InputType.int_range
        m, M = rng.get_args()
        left = IntGeLeTV(m, left_max)
        right = IntGeLeTV(left_max+1, M)

        self.left_max = left_max
        self.InputType = InputType
        self.OutputType = InputType.EitherTV(left, right)
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        if input <= self.left_max:
            return make_choice(left = input)
        return make_choice(right = input)
    def untypechecked_backward(self, output):
        tag, i = output
        return i
    def get_construct_info(self):
        return self.make_args_kwargs(self.InputType, self.left_max)


