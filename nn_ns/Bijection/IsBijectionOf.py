
__all__ = ['IsBijectionOf']
from .Bijection import Bijection
from .TypeVerifier import TypeVerifier

class IsBijectionOf:
    def __init__(InputType, OutputType):
        assert isinstance(InputType, TypeVerifier)
        assert isinstance(OutputType, TypeVerifier)
        self.InputType = InputType
        self.OutputType = OutputType
    def __call__(self, obj):
        return isinstance(obj, Bijection) and \
            obj.get_InputType() == self.InputType and \
            obj.get_OutputType() == self.OutputType



