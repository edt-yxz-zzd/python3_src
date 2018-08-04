

__all__ = 'ChoiceTV make_eitherTV make_choice is_choice'.split()
from .TypeVerifier import TypeVerifier
from .utils import all_TypeVerifiers, are_strs
from .import_FrozenDict import FrozenDict


def show_record_type_item(rt, key, eq, val2str):
    val = rt[key]
    return '{}{}{}'.format(key, eq, val2str(val))
def list_record_type(sorted_keys, rt
    , sep = ', ', eq = '=', val2str=lambda v: v.get_TypeName()):
    return sep.join(show_record_type_item(rt, key, eq, val2str)
                    for key in sorted_keys)

class ChoiceTV(TypeVerifier):
    def __init__(self, iterable_or_mapping=(), **kwargs):
        ChoiceType = FrozenDict(iterable_or_mapping, **kwargs)
        assert are_strs(ChoiceType), TypeError
        assert all_TypeVerifiers(ChoiceType.values()), TypeError

        self.ChoiceType = ChoiceType
        self.ChoiceKeys = frozenset(ChoiceType)
        self.type_name = ('{<' + list_record_type(
                                sorted(ChoiceType), ChoiceType
                                , val2str=lambda v:v.get_TypeName())
                        + '>}')
        self.type_spec = ('{<' + list_record_type(
                                sorted(ChoiceType), ChoiceType
                                , val2str=lambda v:v.get_TypeSpec())
                        + '>}')



        case = sum(t.case_num_instances() for t in ChoiceType.values())
        self.__case = self._singleton_empty2case(case == 1, case == 0)

    def case_num_instances(self):
        return self.__case


    def is_singletonTV(self):
        return self.__is_singletonTV
    def is_emptyTV(self):
        return self.__is_emptyTV



    def get_construct_info(self):
        return self.make_args_kwargs(sorted(self.ChoiceType.items()))
    def get_TypeSpec(self):
        return self.type_spec
    def get_TypeName(self):
        return self.type_name
    def has_instance(self, obj):
        if not is_choice(obj): return False
        tag, val = obj
        return (tag in self.ChoiceKeys and
            self.ChoiceType[tag].has_instance(val)
            )
    def iter_examples(self):
        if len(self.ChoiceType) == 0:
            return
        def iter_item(key_tv):
            key, tv = key_tv
            for x in tv.iter_examples():
                yield key, x
        for pairs in zip(*map(iter_item, self.ChoiceType.items())):
            yield from pairs


    def __hash__(self):
        return hash((__class__, self.ChoiceType))
    def __eq__(self, other):
        return type(other) == __class__ and \
                self.ChoiceType == other.ChoiceType
def make_eitherTV(lhs, rhs):
    return ChoiceTV(left=lhs, right=rhs)

def make_choice(**kwargs):
    assert len(kwargs) == 1, TypeError
    key_val, = kwargs.items()
    return key_val
def is_choice(obj):
    return type(obj) == tuple and len(obj) == 2 and \
        type(obj[0]) == str
