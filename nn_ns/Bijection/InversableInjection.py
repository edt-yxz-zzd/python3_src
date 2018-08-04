

'''
allow to add some random salt
so, each time the output can be different

example:
    input -> (input, random_salt)
    input -> (output, decode_method, args)
        # decode_method can be program(i.e. lambda/SKIBC)
        #   e.g.
        #       to count steps of '3x+1' or 'Goodstein seq'
        #       to find sum of factors of a number
        #       to decode any times until unzipable

input
    <-[zip]->                input'
    <-[encrypt]->            input''
    -[add salt|waste time]-> input_salt
    <-[zip]->                input_salt'
    <-[encrypt random times but no unzippable middle output]->  output

'''

from abc import ABCMeta, abstractmethod

class InversableInjection(metaclass=ABCMeta):
    '''
    inverse . forward == id
    inverse :: Output -> Maybe Input
        # Maybe Input - represent Input or error/undefined/None...
    '''
    @abstractmethod
    def get_InputType(self):pass
    @abstractmethod
    def get_OutputType(self):pass
    @abstractmethod
    def untypechecked_forward(self, input):pass
    @abstractmethod
    def untypechecked_inverse(self, output):pass
    # def chain(self, other):pass
    def test(self):
        I = self.get_InputType()
        O = self.get_OutputType()
        inputs = I.iter_examples()
        for i in inputs:
            o2 = self.untypechecked_forward(i)
            i2 = self.untypechecked_inverse(o2)
            assert I.untypechecked_equal(i, i2)
    def typechecked_forward(self, input):
        assert self.get_InputType().has_instance(input)
        output = self.untypechecked_forward(input)
        assert self.get_OutputType().has_instance(output)
        return output
    def typechecked_inverse(self, output):
        assert self.get_OutputType().has_instance(output)
        input = self.untypechecked_backward(output)
        assert self.get_InputType().has_instance(input)
        return input


