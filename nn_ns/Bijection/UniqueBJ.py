

__all__ = '''
    SingletonTV_BJ
    EmptyTV_BJ
    '''.split()
from .Bijection import Bijection

class SingletonTV_BJ(Bijection):
    def __init__(self, InputTV, OutputTV):
        assert InputTV.is_singletonTV()
        assert OutputTV.is_singletonTV()
        self.InputTV = InputTV
        self.OutputTV = OutputTV
        try:
            self.input = next(InputTV.iter_examples())
            self.output = next(OutputTV.iter_examples())
        except:
            print(InputTV)
            print(OutputTV)
            raise

    def is_idBJ(self):
        return self.get_InputType() == self.get_OutputType()
    def get_InputType(self):
        return self.InputTV
    def get_OutputType(self):
        return self.OutputTV
    def untypechecked_forward(self, input):
        assert input == self.input
        return self.output
    def untypechecked_backward(self, output):
        assert output == self.output
        return self.input
    def get_construct_info(self):
        return self.make_args_kwargs(self.InputTV, self.OutputTV)



class EmptyTV_BJ(Bijection):
    def __init__(self, InputTV, OutputTV):
        assert InputTV.is_emptyTV()
        assert OutputTV.is_emptyTV()
        self.InputTV = InputTV
        self.OutputTV = OutputTV
    def is_idBJ(self):
        return self.get_InputType() == self.get_OutputType()
    def get_InputType(self):
        return self.InputTV
    def get_OutputType(self):
        return self.OutputTV
    def untypechecked_forward(self, input):
        raise TypeError('InputTV is not emptyTV')
    def untypechecked_backward(self, output):
        raise TypeError('OutputTV is not emptyTV')
    def get_construct_info(self):
        return self.make_args_kwargs(self.InputTV, self.OutputTV)


