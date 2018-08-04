

__all__ = 'RecordBijection record_bijection'.split()
from .Bijection import Bijection
from .RecordTV import RecordTV
from .IdBijection import id_of
from .utils import all_Bijections, are_strs\
    , dict_value_map, dict_value_map_with_key
from .import_FrozenDict import FrozenDict

# see also: IdBijection.id_of
# see also: RecordKeyBijection & Str2StrBJ
class RecordBijection(Bijection):
    def __init__(self, iterable_or_mapping=(), **kwargs):
        key2bijection = FrozenDict(iterable_or_mapping, **kwargs)
        assert are_strs(key2bijection)
        assert all_Bijections(key2bijection.values())
        self.key2bijection = key2bijection
        self.InputType = dict_value_map(lambda bj: bj.get_InputType()
                                      , key2bijection.items()
                                      , RecordTV)
        self.OutputType = dict_value_map(lambda bj: bj.get_OutputType()
                                      , key2bijection.items()
                                      , RecordTV)

    def is_idBJ(self):
        return all(b.is_idBJ() for b in self.key2bijection.values())
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        k2bj = self.key2bijection
        def kv2v(key, val):
            return k2bj[key].untypechecked_forward(val)
        return dict_value_map_with_key(kv2v, input)
    def untypechecked_backward(self, output):
        k2bj = self.key2bijection
        def kv2v(key, val):
            return k2bj[key].untypechecked_backward(val)
        return dict_value_map_with_key(kv2v, output)

    def get_construct_info(self):
        ls = tuple(sorted(self.key2bijection.items()))
        return self.make_args_kwargs(ls)
def record_bijection(**key2bijection):
    return RecordBijection(**key2bijection)


