

__all__ = '''
    ChoiceBijection
    choice_bijection
    make_eitherBJ
    '''.split()
from .Bijection import Bijection
from .ChoiceTV import ChoiceTV
from .IdBijection import id_of
from .utils import all_Bijections, are_strs\
    , dict_value_map, dict_value_map_with_key
from .import_FrozenDict import FrozenDict
from .import_is_valid_python_id import is_valid_python_id

# see also: IdBijection.id_of
# see also: ChoiceKeyBijection & Str2StrBJ
class ChoiceBijection(Bijection):
    def __init__(self, iterable_or_mapping=(), **kwargs):
        key2bijection = FrozenDict(iterable_or_mapping, **kwargs)
        assert are_strs(key2bijection), TypeError
        assert all_Bijections(key2bijection.values()), TypeError
        self.key2bijection = key2bijection
        self.InputType = dict_value_map(lambda bj: bj.get_InputType()
                                      , key2bijection
                                      , ChoiceTV)
        self.OutputType = dict_value_map(lambda bj: bj.get_OutputType()
                                      , key2bijection
                                      , ChoiceTV)

    def is_idBJ(self):
        return all(b.is_idBJ() for b in self.key2bijection.values())
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        k2bj = self.key2bijection
        key, val = input
        return key, k2bj[key].untypechecked_forward(val)
    def untypechecked_backward(self, output):
        k2bj = self.key2bijection
        key, val = output
        return key, k2bj[key].untypechecked_backward(val)

    def __repr__(self):
        # to +(x | y | z) ?? if keys = '0' '1' ...
        # to +(x / y) ?? if keys = 'left' 'right'
        # to choiceBJ(tag=bj, tag2=bj2) ?? if keys are is_valid_python_id
        k2b = self.key2bijection
        if _is_eitherBJ(self):
            return '+({!r} / {!r})'.format(k2b['left'], k2b['right'])
        if _is_num_choiceBJ(self):
            keys = _len2keys(len(k2b))
            s = ' | '.join(repr(k2b[k]) for k in keys)
            return '+({})'.format(s)
        if _is_kwargs_choiceBJ(self):
            s = list_record(k2b, repr)
            return 'ChoiceBJ({})'.format(s)
        return super().__repr__()

    def get_construct_info(self):
        k2b = self.key2bijection
        pairs = sorted(k2b.items())
        return self.make_name_args_kwargs('ChoiceBJ', tuple(pairs))

def choice_bijection(**key2bijection):
    return ChoiceBijection(**key2bijection)

def make_eitherBJ(leftBJ, rightBJ):
    return ChoiceBijection(left=leftBJ, right=rightBJ)
def _is_eitherBJ(bj):
    return bj.key2bijection.keys() == set(('left', 'right'))
def _len2keys(L):
    return list(map(str, range(L)))
def _is_num_choiceBJ(bj):
    def f(keys):
        return sorted(keys) == len2keys(len(keys))
    return f(bj.key2bijection.keys())
def _is_kwargs_choiceBJ(bj):
    return all(map(is_valid_python_id, bj.key2bijection.keys()))

def list_record(k2v, v2str):
    # key is str or <
    ls = sorted(k2v.items())
    return ', '.join('{} = {}'.format(k, v2str(v)) for k,v in ls)




