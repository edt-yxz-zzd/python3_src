
from fractions import Fraction
from abc import ABCMeta, abstractmethod

class TypeVerifier(metaclass=ABCMeta):
    # immutable and hashable

    '''
    def __str__(self):
        return self.get_TypeName()
    def __repr__(self):
        return '<{!s}>'.format(self.get_TypeName())
    '''

    # () -> str
    @abstractmethod
    def get_TypeName(self):pass
    # (obj) -> bool
    @abstractmethod
    def has_instance(self, obj):pass
    # () -> Iter obj
    @abstractmethod
    def iter_examples(self):pass
    # (lhs, rhs) -> bool or TypeError
    def typechecked_equal(self, lhs, rhs):
        assert self.has_instance(lhs), TypeError
        assert self.has_instance(rhs), TypeError
        return self.untypechecked_equal(lhs, rhs)
    # (lhs, rhs) -> bool
    # compare Instance
    def untypechecked_equal(self, lhs, rhs):
        # to be overrided
        return lhs == rhs

    # compare Type
    def __eq__(self, other):
        # to be overrided
        return self is other
    def __ne__(self, other):
        return not (self == other)


'''
class Bijection:
    def get_InputType(self):
    def get_OutputType(self):
    def untypechecked_forward(self, input):
    def untypechecked_backward(self, output):
'''
class IsBijectionOf:
    def __init__(InputType, OutputType):
        self.InputType = InputType
        self.OutputType = OutputType
    def __call__(self, obj):
        return isinstance(obj, Bijection) and \
            obj.get_InputType() == self.InputType and \
            obj.get_OutputType() == self.OutputType
class Bijection(metaclass=ABCMeta):
    # we may have dynamic chained bijection, so I/O is not depended on cls
    # return an instance of TypeVerifier
    @abstractmethod
    def get_InputType(self):pass
    @abstractmethod
    def get_OutputType(self):pass
    @abstractmethod
    def untypechecked_forward(self, input):pass
    @abstractmethod
    def untypechecked_backward(self, output):pass
    # def chain(self, other):pass
    def test(self):
        I = self.get_InputType()
        O = self.get_OutputType()
        inputs = I.iter_examples()
        outputs = O.iter_examples()
        for i, o in zip(inputs, outputs):
            o2 = self.untypechecked_forward(i)
            i2 = self.untypechecked_backward(o2)
            assert I.untypechecked_equal(i, i2)
            i2 = self.untypechecked_backward(o)
            o2 = self.untypechecked_forward(i2)
            assert O.untypechecked_equal(o, o2)
    def typechecked_forward(self, input):
        assert self.get_InputType().has_instance(input)
        output = self.untypechecked_forward(input)
        assert self.get_OutputType().has_instance(output)
        return output
    def typechecked_backward(self, output):
        assert self.get_OutputType().has_instance(output)
        input = self.untypechecked_backward(output)
        assert self.get_InputType().has_instance(input)
        return input

class AnyHashable(TypeVerifier):
    def get_TypeName(self):
        return 'AnyHashable'
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
Any = AnyHashable()
class IdBijection(Bijection):
    def __init__(self, io_type = Any):
        self.io_type = io_type
    def get_InputType(self):
        return self.io_type
    def get_OutputType(self):
        return self.io_type
    def untypechecked_forward(self, input):
        return input
    def untypechecked_backward(self, output):
        return output
id_bijection = IdBijection()
def id_of(io_type):
    return IdBijection(io_type)

def chainable(b0, b1):
    return b0.get_OutputType() == b1.get_InputType()
class ChainedBijection(Bijection):
    def __init__(self, *bijections):
        assert len(bijections) > 1, TypeError
        assert all(isinstance(b, Bijection) for b in bijections), TypeError
        assert all(map(chainable, bijections, bijections[1:])), TypeError
        self.bijections = bijections
    def get_InputType(self):
        return self.bijections[0].get_InputType()
    def get_OutputType(self):
        return self.bijections[-1].get_OutputType()
    def untypechecked_forward(self, input):
        for b in self.bijections:
            input = b.untypechecked_forward(input)
        return input
    def untypechecked_backward(self, output):
        # bug: for b in self.bijections: # forgot "reversed"
        for b in reversed(self.bijections):
            output = b.untypechecked_backward(output)
        return output

def chain_bijections(*bijections):
    L = len(bijections)
    if L > 1: return ChainedBijection(*bijections)
    if L == 0: return id_bijection
    bijection, = bijections
    return bijection


def all_of_Type(objs, Type):
    return all(isinstance(obj, Type) for obj in objs)
def all_TypeVerifiers(objs):
    return all_of_Type(objs, TypeVerifier)
def all_Bijections(objs):
    return all_of_Type(objs, Bijection)
class TupleBijection(Bijection):
    def __init__(self, *bijections):
        assert all_Bijections(bijections)
        self.bijections = bijections
        self.InputType = Tuple(b.get_InputType() for b in bijections)
        self.OutputType = Tuple(b.get_OutputType() for b in bijections)
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return tuple(b.untypechecked_forward(i)
                    for b, i in zip(self.bijections, input))
    def untypechecked_backward(self, output):
        return tuple(b.untypechecked_backward(o)
                    for b, o in zip(self.bijections, output))
def tuple_bijection(bijections):
    return TupleBijection(*bijections)
def pair_bijection(b0, b1):
    return TupleBijection(b0, b1)


##################################
'''
class (TypeVerifier):
    def get_TypeName(self):
    def has_instance(self, obj):
    def iter_examples(self):
    def untypechecked_equal(self, lhs, rhs):
    def __eq__(self, other):
'''

class BoolTV(TypeVerifier):
    def get_TypeName(self):
        return 'Bool'
    def has_instance(self, obj):
        return type(obj) == bool
    def iter_examples(self):
        yield False
        yield True
Bool = BoolTV()
class IntTV(TypeVerifier):
    def get_TypeName(self):
        return 'Int'
    def has_instance(self, obj):
        return type(obj) == int
    def iter_examples(self):
        return iter((0,1,-1,2,-2))
    def __eq__(self, other):
        return type(other) == IntTV
        assert isinstance(other, IntTV), TypeError
Int = IntTV()
class RationalTV(TypeVerifier):
    def get_TypeName(self):
        return 'Rational'
    def has_instance(self, obj):
        return type(obj) == Fraction
    def iter_examples(self):
        return iter((Fraction(0),Fraction(1),Fraction(-1)
                    ,Fraction(1,2),Fraction(-3,2)))
    def __eq__(self, other):
        return type(other) == RationalTV
Rational = RationalTV()


class IntGeTV(TypeVerifier):
    def __init__(self, min):
        assert isinstance(min, int), TypeError
        self.min = min
        self.type_name = 'Int{{.>={min}}}'.format(min=min)
    def get_TypeName(self):
        return self.type_name
    def has_instance(self, obj):
        return type(obj) == int and obj >= self.min
    def iter_examples(self):
        return range(self.min, self.min+3)
    def __eq__(self, other):
        return type(other) == IntGeTV and self.min == other.min
UInt = IntGeTV(0)
PInt = IntGeTV(1)
class IntGeLtTV(TypeVerifier):
    def __init__(self, min, max):
        assert isinstance(min, int), TypeError
        assert isinstance(max, int), TypeError
        assert min < max, ValueError
        self.min = min
        self.max = max
        self.type_name = 'Int{{{min}<=.<{max}}}'.format(min=min, max=max)
    def get_TypeName(self):
        return self.type_name
    def has_instance(self, obj):
        return type(obj) == int and self.min <= obj < self.max
    def iter_examples(self):
        #return range(self.min, self.max)
        m = self.min
        yield m
        M = self.max - 1
        if M == m: return
        yield M
        mid = (M+m)//2
        if m < mid < M:
            yield mid
    def __eq__(self, other):
        return type(other) == IntGeLtTV and \
                self.min == other.min and \
                self.max == other.max

class RationalGeTV(TypeVerifier):
    def __init__(self, min):
        assert isinstance(min, Fraction), TypeError
        self.min = min
        self.type_name = 'Rational{{.>={min}}}'.format(min=min)
    def get_TypeName(self):
        return self.type_name
    def has_instance(self, obj):
        return type(obj) == Fraction and obj >= self.min
    def iter_examples(self):
        m = self.min
        return iter((m, m + Fraction(1, 2), m + Fraction(30, 7)))
    def __eq__(self, other):
        return type(other) == RationalGeTV and self.min == other.min
URational = RationalGeTV(Fraction(0))
class RationalGtTV(TypeVerifier):
    def __init__(self, min):
        assert isinstance(min, Fraction), TypeError
        self.min = min
        self.type_name = 'Rational{{.>{min}}}'.format(min=min)
    def get_TypeName(self):
        return self.type_name
    def has_instance(self, obj):
        return type(obj) == Fraction and obj > self.min
    def iter_examples(self):
        m = self.min
        return iter((m + Fraction(1, 9999), m + Fraction(1, 2), m + Fraction(30, 7)))
    def __eq__(self, other):
        return type(other) == RationalGtTV and self.min == other.min
PRational = RationalGtTV(Fraction(0))

def list_TypeNames(type_verifiers, sep = ', '):
    return sep.join(t.get_TypeName() for t in type_verifiers)
class TupleTV(TypeVerifier):
    def __init__(self, *type_verifiers):
        assert all_TypeVerifiers(type_verifiers)
        self.type_verifiers = type_verifiers
        L = len(type_verifiers)
        names = list_TypeNames(type_verifiers)
        self.type_name = '({},)'.format(names) if L == 1 else \
                         '({})'.format(names) # str(type_verifiers)
    def get_TypeName(self):
        return self.type_name
    def has_instance(self, obj):
        if type(obj) != tuple: return False
        if len(obj) != len(self.type_verifiers): return False
        return all(t.has_instance(x) for x, t in zip(obj, self.type_verifiers))
    def iter_examples(self):
        # product or zip ?? product is too much
        return zip(*(t.iter_examples() for t in self.type_verifiers))
    def untypechecked_equal(self, lhs, rhs):
        return all(t.untypechecked_equal(a,b)
                    for t, a, b in zip(self.type_verifiers, lhs, rhs))
    def __eq__(self, other):
        return type(other) == TupleTV and \
                self.type_verifiers == other.type_verifiers

def Pair(a, b):
    return TupleTV(a, b)
def Tuple(type_verifiers):
    return TupleTV(*type_verifiers)

class ArrayTV(TypeVerifier):
    def __init__(self, type_verifier, min_len = 0):
        assert isinstance(type_verifier, TypeVerifier)
        assert isinstance(min_len, int)
        assert min_len >= 0
        self.type_verifier = type_verifier
        self.min_len = min_len
        self.type_name = '[{}]{{len(.)>={}}}'.format(type_verifier.get_TypeName(), min_len)
    def get_TypeName(self):
        return self.type_name
    def has_instance(self, obj):
        return type(obj) == tuple and \
            all(map(self.type_verifier.has_instance, obj))
    def iter_examples(self):
        if self.min_len == 0: yield ()
        it = self.type_verifier.iter_examples()
        ls = list(islice(it, 0, 2))
        if self.min_len <= 1:
            for x in ls:
                yield (x,)
        if self.min_len <= 2:
            for x, y in product(ls, ls):
                yield (x, y)
        for x in ls:
            # only one
            L = max(self.min_len, 3)
            for n in range(L, L+2):
                yield (x,) * n
            break

    def untypechecked_equal(self, lhs, rhs):
        f = self.type_verifier.untypechecked_equal
        return len(lhs) == len(rhs) and all(f(a,b) for a, b in zip(lhs, rhs))
    def __eq__(self, other):
        return type(other) == ArrayTV and \
                self.min_len == other.min_len and \
                self.type_verifier == other.type_verifier

def Array(type_verifier, min_len = 0):
    return ArrayTV(type_verifier, min_len)
def Array0(type_verifier):
    return Array(type_verifier, 0)
def Array1(type_verifier):
    return Array(type_verifier, 1)
def Array2(type_verifier):
    return Array(type_verifier, 2)
PInts = Array0(PInt)
PInt1s = Array1(PInt)




class UnionTV(TypeVerifier):
    # should have no overlaps, i.e. UnionTV(Int, UInt) is Error!
    def __init__(self, *type_verifiers):
        assert all_TypeVerifiers(type_verifiers)
        self.type_verifiers = type_verifiers
        names = list_TypeNames(type_verifiers)
        self.type_name = 'Union({})'.format(names)
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
        return which_Types
    def has_instance(self, obj):
        s = sum(t.has_instance(obj) for t in self.type_verifiers)
        if s > 1:
            raise TypeError('This UnionTV is wrong for overlaps between types')
        return 1 == s
    def iter_examples(self):
        for t in self.type_verifiers:
            for a in t.iter_examples():
                yield a
                break
    def untypechecked_equal(self, lhs, rhs):
        t0 = self.which_Type(lhs)
        t1 = self.which_Type(rhs)
        if t0 is not t1: return False
        return t0.untypechecked_equal(lhs, rhs)
    def __eq__(self, other):
        return type(other) == UnionTV and \
            self.type_verifiers == other.type_verifiers
'''
class NamedTupleTV(TypeVerifier):
    def __init__(self, **kwargs):
        self.
    def get_TypeName(self):
        return ''
    def has_instance(self, obj):
    def iter_examples(self):
    def untypechecked_equal(self, lhs, rhs):
    def __eq__(self, other):
class NamedUnionTV(TypeVerifier):
    def get_TypeName(self):
        return ''
    def has_instance(self, obj):
    def iter_examples(self):
    def untypechecked_equal(self, lhs, rhs):
    def __eq__(self, other):
'''





'''
[PInt]
    <-[append 1]-> [PInt]{len(.)>=1, .[-1]=1}
    <-[continued fraction]-> Rational{.>=1}
    <-[-1]-> Rational{.>=0}
    <-> (UInt, PInt){gcd(.)==1}
[PInt]{len(.)>=1}
    <-[head]-> (PInt, [PInt])
    <-[see above]-> (PInt, (UInt, PInt){gcd(.)==1})
    <-[mul]-> (UInt, PInt)

'''
from nn_ns.math_nn.continued_fraction.continued_fraction import\
      finite_continued_fraction2ND as CF2ND \
    , ND2continued_fraction as _ND2CF \
    , ND2Fraction, Fraction2ND
def ND2CF(ND):
    # assume to append 1 after cf
    # -2 == [-2] == [-3] ++ [1] ==>> [-3]
    # 2 == [2] == [1] ++ [1] ==>> [1]
    # 2/3 == [0,1,2] == [0,1,1] ++ [1] ==>> [0,1,1]
    # 1 == [1] == [] ++ [1] ==>> []
    *cf, = _ND2CF(ND)
    assert len(cf) == 1 or cf[-1] > 1
    if cf[-1] == 1:
        cf = cf[:-1]
    else:
        cf[-1] -= 1
    return cf

class PInts2URational_by_cf(Bijection):
    def get_InputType(self):
        return PInts
    def get_OutputType(self):
        return URational
    def untypechecked_forward(self, input):
        cf = input + (1,)
        nd = CF2ND(cf)
        fr = ND2Fraction(nd) - 1
        return fr
    def untypechecked_backward(self, output):
        fr = output + 1
        nd = Fraction2ND(fr)
        cf = ND2CF(nd)
        pints = tuple(cf)
        return pints

class ArrayHead(Bijection):
    def __init__(self, type_verifier, input_min):
        assert input_min >= 1
        self.type_verifier = type_verifier
        self.input_min = input_min
        self.InputType = Array(type_verifier, input_min)
        self.OutputType = Pair(type_verifier, Array(type_verifier, input_min-1))
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        return (input[0], input[1:])
    def untypechecked_backward(self, output):
        head, tail = output
        return (head,) + tail
class PInt_URational_2_UInt_PInt_by_mulGCD(Bijection):
    InputType = Pair(PInt, URational)
    OutputType = Pair(UInt, PInt)
    def get_InputType(self):
        return self.InputType
    def get_OutputType(self):
        return self.OutputType
    def untypechecked_forward(self, input):
        gcd, fr = input
        n, d = Fraction2ND(fr)
        return gcd*n, gcd*d
    def untypechecked_backward(self, output):
        u, p = nd = output
        fr = ND2Fraction(nd)
        n, d = Fraction2ND(fr)
        gcd = p // d
        return gcd, fr

pint1s_2_uint_pint = chain_bijections(
                      ArrayHead(PInt, 1)
                    , pair_bijection(id_of(PInt), PInts2URational_by_cf())
                    , PInt_URational_2_UInt_PInt_by_mulGCD()
                    )

class UInt2PInt_by_add1(Bijection):
    def get_InputType(self):
        return UInt
    def get_OutputType(self):
        return PInt
    def untypechecked_forward(self, input):
        return input + 1
    def untypechecked_backward(self, output):
        return output - 1
UInt2PInt_by_add1().test()

examples = {
    'PInt0s':
        ((), (1,), (2,), (100,)
        ,(1,1), (2,1), (1,2), (2,2), (3,2)*5
        ),
    'PInt1s':
        ((1,), (2,), (100,)
        ,(1,1), (2,1), (1,2), (2,2), (3,2)*5
        ),
    '(UInt, PInt)':
        ((0,1), (1,1), (0, 2), (2,1), (1,2), (0,3)
        )
    }

def test_IO_by_name(input_name, output_name, bijection):
    print('test_IO_by_name:', input_name, '->', output_name)
    inputs = examples[input_name]
    outputs = examples[output_name]
    test_IO(inputs, outputs, bijection)
def test_IO(inputs, outputs, bijection):
    test_I(inputs, bijection)
    test_O(outputs, bijection)
def test_I(inputs, bijection):
    eqI = bijection.get_InputType().untypechecked_equal
    for i in inputs:
        o = bijection.typechecked_forward(i)
        i_ = bijection.typechecked_backward(o)
        print(i, o)
        assert eqI(i, i_)
def test_O(outputs, bijection):
    eqO = bijection.get_OutputType().untypechecked_equal
    for o in outputs:
        i = bijection.typechecked_backward(o)
        o_ = bijection.typechecked_forward(i)
        print(i, o)
        assert eqO(o, o_)

#est_IO_by_name('PInt1s', '(UInt, PInt)', pint1s_2_uint_pint)


'''
class Bijection:
    def get_InputType(self):
    def get_OutputType(self):
    def untypechecked_forward(self, input):
    def untypechecked_backward(self, output):
'''


