


__all__ = '''
    ChoiceOfTuple2UnionBJ
    '''.split()

from .ChoiceTV import ChoiceTV
from .UnionTV import UnionTV
from .TupleTV import TupleTV
from .Bijection import Bijection


class ChoiceOfTuple2UnionBJ(Bijection):
    # TupleTV with different length
    def __init__(self, InputTV, OutputTV):
        assert isinstance(InputTV, ChoiceTV), TypeError
        assert isinstance(OutputTV, UnionTV), TypeError
        key2tupleTVs = InputTV.ChoiceType
        tupleTVs = OutputTV.type_verifiers
        if len(key2tupleTVs) != len(tupleTVs): raise TypeError
        if frozenset(key2tupleTVs.values()) != tupleTVs: raise TypeError
        if not all(isinstance(t, TupleTV) for t in tupleTVs): raise TypeError
        if len(tupleTVs) != len(set(map(lambda tv: len(tv.type_verifiers), tupleTVs))): raise TypeError
        len2key = {len(tv.type_verifiers): key
                    for key, tv in key2tupleTVs.items()}
        assert len(len2key) == len(key2tupleTVs)

        self.InputTV = InputTV
        self.OutputTV = OutputTV
        self.len2key = len2key
    def get_InputType(self):
        return self.InputTV
    def get_OutputType(self):
        return self.OutputTV
    def untypechecked_forward(self, input):
        tag, tpl = input
        return tpl
    def untypechecked_backward(self, output):
        tag = self.len2key[len(output)]
        return tag, output
    def get_construct_info(self):
        return self.make_args_kwargs(self.InputTV, self.OutputTV)




