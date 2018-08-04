
__all__ = 'TheNone'.split()
from .TypeVerifier import TypeVerifier

class NoneTV(TypeVerifier):
    def case_num_instances(self):
        return 1
    def get_construct_info(self):
        return 'TheNone'
    def get_TypeSpec(self):
        return 'TheNone'
    def get_TypeName(self):
        return 'None'
    def has_instance(self, obj):
        return obj is None
    def untypechecked_equal(self, lhs, rhs):
        return lhs is rhs
    def iter_examples(self):
        yield None

    def __eq__(self, other):
        return isinstance(other, __class__)
    def __hash__(self):
        return id(__class__)
TheNone = NoneTV()

