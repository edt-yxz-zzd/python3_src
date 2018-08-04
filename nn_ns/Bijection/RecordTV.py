

__all__ = 'RecordTV make_record'.split()
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




class RecordTV(TypeVerifier):
    def __init__(self, iterable_or_mapping=(), **kwargs):
        RecordType = FrozenDict(iterable_or_mapping, **kwargs)
        assert are_strs(RecordType, str), TypeError
        assert all_TypeVerifiers(RecordType.values()), TypeError

        self.RecordType = RecordType
        self.RecordKeys = frozenset(RecordType)
        self.type_name = ('{[' + list_record_type(
                                sorted(RecordType), RecordType
                                , val2str=lambda v:v.get_TypeName())
                        + ']}')
        self.type_spec = ('{[' + list_record_type(
                                sorted(RecordType), RecordType
                                , val2str=lambda v:v.get_TypeSpec())
                        + ']}')

        self.__case = self.TupleTV(*RecordType.values()).case_num_instances()
    def case_num_instances(self):
        return self.__case
    def get_construct_info(self):
        ls = tuple(sorted(self.RecordType.items()))
        return self.make_args_kwargs(ls)
    def get_TypeSpec(self):
        return self.type_spec
    def get_TypeName(self):
        return self.type_name
    def has_instance(self, obj):
        return (type(obj) == FrozenDict and
            len(obj) == len(self.RecordType) and
            are_strs(obj, str) and
            frozenset(obj) == self.RecordKeys and
            all(tv.has_instance(obj[key])
                for key, tv in self.RecordType.items()
                )
            )
    def iter_examples(self):
        if len(self.RecordType) == 0:
            yield FrozenDict()
            return
        def iter_item(key_tv):
            key, tv = key_tv
            for x in tv.iter_examples():
                yield key, x
        for pairs in zip(*map(iter_item, self.RecordType.items())):
            yield FrozenDict(pairs)


    def __hash__(self):
        return hash((__class__, self.RecordType))
    def __eq__(self, other):
        return type(other) == __class__ and \
                self.RecordType == other.RecordType

def make_record(**key2val):
    return FrozenDict(key2val)

