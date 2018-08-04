
__all__ = 'Any'.split()
from .TypeVerifier import TypeVerifier

class AnyHashableTV(TypeVerifier):
    def get_construct_info(self):
        return 'Any'
    def get_TypeSpec(self):
        return 'Any'
    def get_TypeName(self):
        return 'Any'
    def has_instance(self, obj):
        try:
            hash(obj)
        except:
            return False
        return True
    def untypechecked_equal(self, lhs, rhs):
        return lhs is rhs
    def iter_examples(self):
        return iter([ False,True,0,1,-1,0.0,0.1,0j, 1+1j
                    , '','a',',)', b'', b'a,)', (), (1,False)
                    , frozenset(), frozenset([1,False])
                    ])

    def __eq__(self, other):
        return isinstance(other, __class__)
    def __hash__(self):
        return id(__class__)
Any = AnyHashableTV()

