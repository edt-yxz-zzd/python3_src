

__all__ = '''
    ArrayTV
    ArrayGe
    ArrayGe0
    ArrayGe1
    ArrayGe2
    ArrayJust
    '''
from .TypeVerifier import TypeVerifier
from itertools import islice
from .IntRange import UIntRange

class ArrayTV(TypeVerifier):
    def __init__(self, type_verifier, min_len, may_max_len):
        assert isinstance(type_verifier, TypeVerifier)
        self.size_range = UIntRange(min_len, may_max_len)
        self.type_verifier = type_verifier
        elem_type_name = type_verifier.get_TypeName()
        elem_type_spec = type_verifier.get_TypeSpec()
        self.type_name = '[{}]{{{}<=len(.)<={}}}'.format(
                elem_type_name, min_len, may_max_len)
        self.type_spec = '[{}]{}'.format(
                elem_type_spec, self.size_range.range_spec)

        if may_max_len is None:
            lens = (min_len, min_len+1, min_len+2)
        else:
            lens = {min_len, may_max_len, (may_max_len+min_len)//2}
            lens = tuple(sorted(lens))
        self.__lens = lens

        rng = self.size_range
        singleton = (
            # []
            rng.may_max == 0 or
            # [a]*L
            (rng.is_singleton_range() and type_verifier.is_singletonTV()) or
            # []
            (rng.min == 0 and type_verifier.is_emptyTV())
            )
        empty = rng.min != 0 and type_verifier.is_emptyTV()
        self.__case = self._singleton_empty2case(singleton, empty)

    def case_num_instances(self):
        return self.__case

    def __repr__(self):
        a = self.type_verifier
        rng = self.size_range
        return '{!r}[{}, {}]'.format(a, *rng.get_args())
    def get_construct_info(self):
        a = self.type_verifier
        rng = self.size_range
        return self.make_args_kwargs(a, *rng.get_args())
    def get_TypeSpec(self):
        return self.type_spec
    def get_TypeName(self):
        return self.type_name
    def has_instance(self, obj):
        return type(obj) == tuple and \
            self.size_range.valid(len(obj)) and \
            all(map(self.type_verifier.has_instance, obj))
    def iter_examples(self):
        if self.size_range.min == 0: yield ()
        it = self.type_verifier.iter_examples()
        ls = list(islice(it, 0, 2))
        L = len(ls)
        if L == 0: return
        for n in self.__lens:
            for x in ls:
                yield (x,) * n
        if L == 2:
            for n in self.__lens:
                yield ((ls[1], ls[0]) * (n+1)//2)[:n]



    def untypechecked_equal(self, lhs, rhs):
        f = self.type_verifier.untypechecked_equal
        return len(lhs) == len(rhs) and all(map(f, lhs, rhs))
    def __eq__(self, other):
        return type(other) == __class__ and \
                self.size_range == other.size_range and \
                self.type_verifier == other.type_verifier
    def __hash__(self):
        return hash((__class__, self.type_verifier, self.size_range))

def ArrayJust(type_verifier, len):
    return ArrayTV(type_verifier, len, len)
def ArrayGe(type_verifier, min_len):
    return ArrayTV(type_verifier, min_len, None)
def ArrayGe0(type_verifier):
    return ArrayGe(type_verifier, 0)
def ArrayGe1(type_verifier):
    return ArrayGe(type_verifier, 1)
def ArrayGe2(type_verifier):
    return ArrayGe(type_verifier, 2)

