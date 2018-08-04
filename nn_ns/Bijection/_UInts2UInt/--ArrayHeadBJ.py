

# use 'SeqBJ.SplitHead'

__all__ = ['ArrayHeadBJ']
from .Bijection import Bijection
from .ArrayTV import ArrayTV
from .TupleTV import Pair

class ArrayHeadBJ(Bijection):
    def __init__(self, type_verifier, input_min, input_max=None):
        assert input_min >= 1
        self.type_verifier = type_verifier
        self.input_min = input_min
        self.InputType = ArrayTV(type_verifier, input_min, input_max)
        output_min = input_min - 1
        output_max = None if input_max is None else input_max - 1
        self.OutputType = Pair(type_verifier
                             , ArrayTV(type_verifier, output_min, output_max))
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return (input[0], input[1:])
    def untypechecked_backward(self, output):
        head, tail = output
        return (head,) + tail

