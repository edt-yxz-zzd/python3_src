

__all__ = ['ArrayBijection']
from .Bijection import Bijection
from .ArrayTV import ArrayTV
from .IntRange import UIntRange

class ArrayBijection(Bijection):
    '(a<->b) -> ([a]<->[b])'
    def __init__(self, a2b, min_len=0, max_len=None):
        assert isinstance(a2b, Bijection)
        a = a2b.get_InputType()
        b = a2b.get_OutputType()
        self.InputType = ArrayTV(a, min_len, max_len)
        self.OutputType = ArrayTV(b, min_len, max_len)
        self.bijection = a2b
        self.size_range = UIntRange(min_len, max_len)

    def is_idBJ(self):
        return self.bijection.is_idBJ()
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return tuple(map(self.bijection.untypechecked_forward, input))
    def untypechecked_backward(self, output):
        return tuple(map(self.bijection.untypechecked_backward, output))

    def get_construct_info(self):
        return self.make_args_kwargs(self.bijection, *self.size_range.get_args())
    def __repr__(self):
        return '{!r}[{},{}]'.format(self.bijection, *self.size_range.get_args())
