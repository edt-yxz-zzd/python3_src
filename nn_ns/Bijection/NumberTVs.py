

__all__ = '''
    Bool Int Rational
    IntGeTV IntGeLeTV   is_IntGeTV
    RationalGeTV RationalGtTV

    UInt PInt
    URational PRational
    Digit BijectiveDigit BiDigit
    PIntRadixReprLE UIntRadixReprLE

    '''.split()
from .TypeVerifier import TypeVerifier
from .IntRange import IntRange, UIntRange
from fractions import Fraction


class BoolTV(TypeVerifier):
    def get_construct_info(self):
        return 'Bool'
    def get_TypeSpec(self):
        return 'Bool'
    def get_TypeName(self):
        return 'Bool'
    def has_instance(self, obj):
        return type(obj) == bool
    def iter_examples(self):
        yield False
        yield True
    def __hash__(self):
        return id(__class__)
    def __eq__(self, other):
        return type(other) == __class__
Bool = BoolTV()

class RationalTV(TypeVerifier):
    def get_construct_info(self):
        return 'Rational'
    def get_TypeSpec(self):
        return 'Rational'
    def get_TypeName(self):
        return 'Rational'
    def has_instance(self, obj):
        return type(obj) == Fraction
    def iter_examples(self):
        return iter((Fraction(0),Fraction(1),Fraction(-1)
                    ,Fraction(1,2),Fraction(-3,2)))
    def __eq__(self, other):
        return type(other) == __class__
    def __hash__(self):
        return id(__class__)
Rational = RationalTV()



class IntGeLeTV(TypeVerifier):
    # non-empty
    def __init__(self, may_min, may_max):
        self.int_range = IntRange(may_min, may_max)
        self.type_name = 'Int{{{min}<=.<={max}}}'.format(min=may_min, max=may_max)
        self.type_spec = 'Int{}'.format(self.int_range.range_spec)

    def case_num_instances(self):
        return self._singleton_empty2case(
            self.int_range.is_singleton_range(), False)
    def get_construct_info(self):
        return self.make_args_kwargs(*self.int_range.get_args())
    def get_TypeSpec(self):
        return self.type_spec
    def get_TypeName(self):
        return self.type_name
    def has_instance(self, obj):
        return type(obj) == int and self.int_range.valid(obj)
    def iter_examples(self):
        #return range(self.min, self.max)
        m = self.int_range.may_min
        M = self.int_range.may_max
        outputs = {m, M}
        outputs.discard(None)
        L = len(outputs)
        if L == 2:
            mid = (M+m)//2
            outputs.update([m+1,mid,M-1])
        elif L == 1:
            if m is None:
                outputs.update(range(M, M-4, -1))
            elif M is None:
                outputs.update(range(m, m+3))
        outputs.update([1000, -1000])
        outputs.update(range(-2,3))
        return filter(self.has_instance, outputs)
    def __eq__(self, other):
        return type(other) == __class__ and \
                self.int_range == other.int_range
    def __hash__(self):
        return hash((__class__, self.int_range))
Int = IntGeLeTV(None, None)
def IntGeTV(min):
    assert type(min) is int
    return IntGeLeTV(min, None)
def is_IntGeTV(XInt):
    return (isinstance(XInt, IntGeLeTV) and
            XInt.int_range.may_max is None and
            XInt.int_range.may_min is not None
            )
UInt = IntGeTV(0)
PInt = IntGeTV(1)
assert is_IntGeTV(UInt)
assert is_IntGeTV(PInt)
assert not is_IntGeTV(Int)


def Digit(radix):
    assert radix >= 2
    return IntGeLeTV(0, radix-1)
def BijectiveDigit(radix):
    assert radix >= 1
    return IntGeLeTV(1, radix)
BiDigit = BijectiveDigit
def PIntRadixReprLE(big_radix):
    'PIntRadixReprLE = ([Digit(R)], BiDigit(R-1))'
    R = big_radix
    fst = Digit(R)
    snd = BiDigit(R-1)
    return +(fst[0,None] * snd)
def UIntRadixReprLE(big_radix):
    'UIntRadixReprLE = () | ([Digit(R)], BiDigit(R-1))'
    T = TypeVerifier
    alter = T.TupleTV()
    return +(alter + PIntRadixReprLE(big_radix))
    return T.UnionTV(alter, PIntRadixReprLE(big_radix))


class RationalGeTV(TypeVerifier):
    def __init__(self, min):
        assert isinstance(min, Fraction), TypeError
        self.min = min
        self.type_name = 'Rational{{.>={min}}}'.format(min=min)
    def get_construct_info(self):
        return self.make_args_kwargs(self.min)
    def get_TypeSpec(self):
        return self.type_name
    def get_TypeName(self):
        return self.type_name
    def has_instance(self, obj):
        return type(obj) == Fraction and obj >= self.min
    def iter_examples(self):
        m = self.min
        return iter((m, m + Fraction(1, 2), m + Fraction(30, 7)))
    def __eq__(self, other):
        return type(other) == __class__ and self.min == other.min
    def __hash__(self):
        return hash((__class__, self.min))
URational = RationalGeTV(Fraction(0))
class RationalGtTV(TypeVerifier):
    def __init__(self, min):
        assert isinstance(min, Fraction), TypeError
        self.min = min
        self.type_name = 'Rational{{.>{min}}}'.format(min=min)
    def get_construct_info(self):
        return self.make_args_kwargs(self.min)
    def get_TypeSpec(self):
        return self.type_name
    def get_TypeName(self):
        return self.type_name
    def has_instance(self, obj):
        return type(obj) == Fraction and obj > self.min
    def iter_examples(self):
        m = self.min
        return iter((m + Fraction(1, 9999), m + Fraction(1, 2), m + Fraction(30, 7)))
    def __eq__(self, other):
        return type(other) == __class__ and self.min == other.min
    def __hash__(self):
        return hash((__class__, self.min))
PRational = RationalGtTV(Fraction(0))


