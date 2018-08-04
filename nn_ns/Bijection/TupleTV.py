

__all__ = 'TupleTV tupleTV PairTV'.split()
from .TypeVerifier import TypeVerifier
from .utils import all_TypeVerifiers
#from .import_fold import foldl0
#import operator


def list_TypeNames(type_verifiers, sep = ', '):
    return sep.join(t.get_TypeName() for t in type_verifiers)
def list_TypeSpecs(type_verifiers, sep = ', '):
    return sep.join(t.get_TypeSpec() for t in type_verifiers)
class TupleTV(TypeVerifier):
    def __init__(self, *type_verifiers):
        assert all_TypeVerifiers(type_verifiers)
        self.type_verifiers = type_verifiers
        L = len(type_verifiers)
        names = list_TypeNames(type_verifiers)
        specs = list_TypeSpecs(type_verifiers)
        fmt = '({},)' if L == 1 else '({})'
        self.type_name = fmt.format(names)
        self.type_spec = fmt.format(specs)

        singleton = all(t.is_singletonTV() for t in type_verifiers)
        empty = any(t.is_emptyTV() for t in type_verifiers)
        self.__case = self._singleton_empty2case(singleton, empty)
        # 0 * inf == NaN
        # case = foldl0(operator.mul, 1
        #             , (t.case_num_instances() for t in type_verifiers))
        # self.__case = self._singleton_empty2case(case == 1, case == 0)

    def case_num_instances(self):
        return self.__case
    def __repr__(self):
        # +(x * y * z)
        ts = self.type_verifiers
        L = len(ts)
        if L >= 2:
            s = ' * '.join(map(repr, ts))
            return '(+({}))'.format(s)
        if L == 1:
            return '(+({!r} * ...))'.format(ts[0])
        return super().__repr__()
    def get_construct_info(self):
        ts = self.type_verifiers
        return self.make_name_args_kwargs('TupleTV', *ts)
        return self.make_args_kwargs(*self.type_verifiers)
    def get_TypeSpec(self):
        return self.type_spec
    def get_TypeName(self):
        return self.type_name
    def has_instance(self, obj):
        if type(obj) != tuple: return False
        if len(obj) != len(self.type_verifiers): return False
        return all(t.has_instance(x) for x, t in zip(obj, self.type_verifiers))
    def iter_examples(self):
        # product or zip ?? product is too much
        # bug: return zip(*(t.iter_examples() for t in self.type_verifiers))
        if not self.type_verifiers: return iter([()])
        return zip(*(t.iter_examples() for t in self.type_verifiers))
    def untypechecked_equal(self, lhs, rhs):
        return all(t.untypechecked_equal(a,b)
                    for t, a, b in zip(self.type_verifiers, lhs, rhs))
    def __eq__(self, other):
        return type(other) == __class__ and \
                self.type_verifiers == other.type_verifiers
    def __hash__(self):
        return hash((__class__, self.type_verifiers))

def PairTV(a, b):
    return TupleTV(a, b)
def tupleTV(type_verifiers):
    return TupleTV(*type_verifiers)


