
__all__ = '''
    Bytes
    Str
    '''.split()
from .TypeVerifier import TypeVerifier
# from .utils import all_TypeVerifiers
from .IntRange import UIntRange

class SetTV(TypeVerifier):
    def __init__(self, type_verifier, min_len = 0, max_len = None):
        assert isinstance(type_verifier, TypeVerifier), TypeError
        self.size_range = UIntRange(min_len, max_len)

        self.type_verifier = type_verifier
        elem_type_name = self.type_verifier.get_TypeName()
        elem_type_spec = type_verifier.get_TypeSpec()
        self.type_name = 'Set({}){{{}<=len(.)<={}}}'.format(
            elem_type_name, *self.size_range.get_args())
        self.type_spec = '{open}{elem}{close}{rng}'.format(
            elem = elem_type_spec, rng = self.size_range.range_spec
            , open = '{{', close = '}}')


    def get_construct_info(self):
        return self.make_args_kwargs(
            self.type_verifier, *self.size_range.get_args())
    def get_TypeSpec(self):
        return self.type_spec
    def get_TypeName(self):
        return self.type_name
    def has_instance(self, obj):
        return type(obj) == frozenset and \
            self.size_range.valid(len(obj)) and \
            all(map(self.type_verifier.has_instance, obj))
    def iter_examples(self):
        raise NotImplementedError
    def __hash__(self):
        return hash((__class__, self.type_verifier, self.size_range))
    def __eq__(self, other):
        return type(other) == __class__ and \
            self.type_verifier == other.type_verifier and \
            self.size_range == other.size_range

