

__all__ = 'UnionTV unionTV'.split()

from .TypeVerifier import TypeVerifier
from .utils import all_TypeVerifiers
from itertools import islice


def list_TypeNames(type_verifiers, sep = ', '):
    return sep.join(t.get_TypeName() for t in type_verifiers)
def list_TypeSpecs(type_verifiers, sep = ', '):
    return sep.join(t.get_TypeSpec() for t in type_verifiers)
class UnionTV(TypeVerifier):
    # should have no overlaps, i.e. UnionTV(Int, UInt) is Error!
    def __init__(self, *type_verifiers):
        assert all_TypeVerifiers(type_verifiers)
        self.type_verifiers = frozenset(type_verifiers)
        if len(self.type_verifiers) != len(type_verifiers): raise TypeError
        ls = sorted(type_verifiers, key=repr)
        names = list_TypeNames(ls)
        specs = list_TypeSpecs(ls)
        # unionTV not UnionTV
        fmt = 'unionTV([{}])' if len(ls) <= 1 else 'unionTV({{{}}})'
        self.type_name = fmt.format(names)
        self.type_spec = fmt.format(specs)

        case = sum(t.case_num_instances() for t in type_verifiers)
        self.__case = self._singleton_empty2case(case == 1, case == 0)

    def case_num_instances(self):
        return self.__case

    def __repr__(self):
        # +(x + y + z)
        bs = list(self.type_verifiers)
        bs.sort(key = repr)
        L = len(bs)
        if L >= 2:
            s = ' + '.join(map(repr, bs))
            return '(+({}))'.format(s)
        if L == 1:
            return '(+({!r} + ...))'.format(bs[0])
        return super().__repr__()
    def get_construct_info(self):
        bs = list(self.type_verifiers)
        bs.sort(key = repr)
        return self.make_name_args_kwargs('UnionTV', *bs)
        return self.make_args_kwargs(*self.type_verifiers)
    def get_TypeSpec(self):
        return self.type_spec
    def get_TypeName(self):
        return self.type_name
    def which_Type(self, obj):
        types = self.which_Types(obj)
        L = len(types)
        if L == 1:
            t, = types
            return t
        if L == 0:
            raise TypeError
        raise TypeError
    def which_Types(self, obj):
        types = tuple(t for t in self.type_verifiers if t.has_instance(obj))
        return types
    def has_instance(self, obj):
        s = sum(bool(t.has_instance(obj)) for t in self.type_verifiers)
        if s > 1:
            raise TypeError('This UnionTV is wrong for overlaps between types')
        return 1 == s
    def iter_examples(self):
        for t in self.type_verifiers:
            it = islice(t.iter_examples(), 0, 2)
            for a in it:
                yield a
    def untypechecked_equal(self, lhs, rhs):
        t0 = self.which_Type(lhs)
        t1 = self.which_Type(rhs)
        if t0 is not t1: return False
        return t0.untypechecked_equal(lhs, rhs)
    def __eq__(self, other):
        return type(other) == __class__ and \
            self.type_verifiers == other.type_verifiers
    def __hash__(self):
        return hash((__class__, self.type_verifiers))


def unionTV(type_verifiers):
    return UnionTV(*type_verifiers)
