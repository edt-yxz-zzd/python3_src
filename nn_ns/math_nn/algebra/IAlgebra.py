
'''
ISet is type
IPureFunction is object
IOperation
    when arity == 0:
        IOperation is a typed object
        operation_equal
    function where arity > 0
INamedRef
    typed named tuple
IRelation
    descript the relationship of the attributes
    may use INamedRef to offer attribute names
    may use IOperation as type of attribute values, to distinguish values.
'''


__all__ = '''
    IAlgebra
    ISet
    ISet_eq
    '''.split()

from abc import ABCMeta, abstractmethod
#from .IAlgebra import IAlgebra, ISet



class IAlgebra(metaclass=ABCMeta):pass
class ISet(metaclass=ABCMeta):
    # object -> bool
    @abstractmethod
    def is_element(self, x):pass
    def __set_equal__(self, other):
        return False
    def __element_equal__(self, x, y):
        return False
    def __is_subset_of__(self, other):
        return False

    '''
    no_elements = 0
    single_element = 1
    unknown_num_elements = float('inf')
    def num_elements(self):
        return unknown_num_elements
    '''
    def are_elements(self, *xs):
        return all(map(self.is_element, xs))
    def set_equal(self, other):
        return self is other or self.__set_equal__(other)
    def __contains__(self, x):
        return self.is_element(x)
    ''' hash make thing harder
    def __eq__(self, other):
        return self.set_equal(other)
    def __ne__(self, other):
        return not (self == other)
    '''
    def element_equal(self, x, y):
        assert self.is_element(x)
        assert self.is_element(y)
        return x is y or self.__element_equal__(x, y)
    def is_subset_of(self, other):
        assert isinstance(other, __class__)
        return x is y or self.__is_subset_of__(x, y)


'''
class ISet_element_equal(ISet):
    # [are_elements(x, y)]: S -> S -> bool
    @abstractmethod
class ISet_is_subset_of(ISet):
    @abstractmethod
'''

class SetExcluded(ISet):
    def __init__(self, set, *IsTheElements):
        if not isinstance(set, ISet): raise TypeError
        if not all(isinstance(e, IIsTheElement) for e in IsTheElements): raise TypeError
        # if not all(set.set_equal(e.get_IO_Set()) for e in IsTheElements): raise TypeError
        if not all(set.is_element(e()) for e in IsTheElements): raise TypeError
        self.__IsTheElements = IsTheElements
        self.__set = set
    def is_element(self, obj):
        return (self.__set.is_element(obj)
            and not any(e.is_the_element(obj) for e in self.__IsTheElements)
            )
    def __iter_excluded_elements(self):
        return (e() for e in self.__IsTheElements)
    def __not_any_excluded_in(self, other):
        return not any(other.is_element(e)
                    for e in self.__iter_excluded_elements())
    def __set_equal__(self, other):
        return (isinstance(other, __class__)
            and self.__set.set_equal(other.__set)
            and self.__not_any_excluded_in(other)
            and other.__not_any_excluded_in(self)
            )

    def __is_subset_of__(self, other):
        if self.__set.is_subset_of(other): return True
        return (isinstance(other, __class__)
            and self.__set.is_subset_of(other.__set)
            and other.__not_any_excluded_in(self)
            )










class IPureFunction(metaclass=ABCMeta):
    # total
    # untyped

    @abstractmethod
    # InputSets -> OutputSet
    def apply(self, *xs):pass
    @abstractmethod
    # return UInt
    def get_arity(self):pass
    def __function_equal__(self, other):
        return False


    def __call__(self, *xs):
        assert len(xs) == self.get_arity()
        return self.apply(*xs)

    def function_equal(self, other):
        assert isinstance(other, __class__)
        return self is other or\
            (   isinstance(other, __class__)
            and self.get_arity() == other.get_arity()
            and self.__function_equal__(other)
            )

class _Callable2PureFunction_(IPureFunction):
    def __init__(self, func, arity):
        assert isinstance(arity, int), TypeError
        assert arity >= 0
        assert callable(func)
        self.__func = func
        self.__arity = arity
    def get_arity(self):
        return self.__arity
    def apply(self, *xs):
        return self.func(*xs)



class IOperationBase(metaclass=ABCMeta):
    # return a IPureFunction
    @abstractmethod
    def get_underlying_function(self):pass

    # return an ISet object
    @abstractmethod
    def get_OutputSet(self):pass

    # return a tuple of ISet objects
    @abstractmethod
    def get_InputSets(self):pass




    def is_closure_operation(self):
        T = self.get_OutputSet()
        return all(map(T.set_equal, self.get_InputSets()))
    def is_restricted_operation_of(self, other):
        assert isinstance(other, __class__)
        return (self.underlying_function_equal(other)
            and self.get_OutputSet().is_subset_of(other.get_OutputSet())
            and all(a.is_subset_of(b) for a,b in zip(
                        self.get_InputSets(), other.get_InputSets()))
            )

    def underlying_function_equal(self, other):
        assert isinstance(other, __class__)
        return self.get_underlying_function().function_equal(
                other.get_underlying_function())
    def operation_equal(self, other):
        assert isinstance(other, __class__)
        return self is other or\
            (   isinstance(other, __class__)
            and self.get_arity() == other.get_arity()
            and self.__operation_equal__(other)
            )
    def __operation_equal__(self, other):
        return (self.get_underlying_function()
                    .function_equal(other.get_underlying_function())
            and self.get_OutputSet().set_equal(other.get_OutputSet())
            and all(a.set_equal(b) for a,b in zip(self.get_InputSets(), other.get_InputSets()))
            )


    # InputSets -> OutputSet
    def apply(self, *xs):
        assert len(xs) == self.get_arity()
        return self.get_underlying_function()(*xs)
    def __call__(self, *xs):
        return self.apply(*xs)
    def get_OperationType(self):
        return self.get_OutputSet(), self.get_InputSets()

    # return UInt
    def get_arity(self):
        return len(self.get_InputSets())

    def is_nullary_operation(self):
        return self.get_arity() == 0
    def is_unary_operation(self):
        return self.get_arity() == 1
    def is_binary_operation(self):
        return self.get_arity() == 2
    def is_ternary_operation(self):
        return self.get_arity() == 3
    '''
Binary means 2-ary.
Ternary means 3-ary.
Quaternary means 4-ary.
Quinary means 5-ary.
Senary means 6-ary.
Septenary means 7-ary.
Octonary means 8-ary (alternatively octary).
Novenary means 9-ary (alternatively nonary, from ordinal).
Denary means 10-ary (alternatively decenary)
Polyadic, multary and multiary mean 2 or more operands (or parameters).
n-ary means n operands (or parameters), but is often used as a synonym of "polyadic".
    '''

class IOperation(IOperationBase):
    # total
    # typed
    def __init__(self, pure_function, OutputSet, *InputSets):
        if not isinstance(pure_function, IPureFunction): raise TypeError
        if not isinstance(OutputSet, ISet): raise TypeError
        if not all(isinstance(i, ISet) for i in InputSets): raise TypeError
        self.__pure_function = pure_function
        self.__OutputSet = OutputSet
        self.__InputSets = InputSets

    def get_underlying_function(self):
        return self.__pure_function
    def get_OutputSet(self):
        return self.__OutputSet
    def get_InputSets(self):
        return self.__InputSets


class IClosureOperation(IOperation):
    def __init__(self, pure_function, IO_Set):
        arity = pure_function.get_arity()
        if not isinstance(arity, int): raise TypeError
        if not arity >= 0: raise TypeError
        super().__init__(pure_function, IO_Set, (IO_Set,)*arity)
    # return an ISet object
    def get_IO_Set(self):
        return self.get_OutputSet()
    def is_IO_Set(self, set):
        assert isinstance(set, ISet)
        return set.set_equal(self.get_IO_Set())

class IClosureOperation_FixedArity(IClosureOperation):
    @classmethod
    @abstractmethod
    def __arity__(cls):pass
    def __init__(self, pure_function, IO_Set):
        arity = type(self).__arity__()
        if not isinstance(arity, int): raise TypeError
        if not pure_function.get_arity() == arity: raise TypeError
        super().__init__(pure_function, IO_Set)
class IClosureBinaryOperation(IClosureOperation):
    @classmethod
    def __arity__(cls):
        return 2
class IClosureUnaryOperation(IClosureOperation):
    @classmethod
    def __arity__(cls):
        return 1
class INullaryOperation(IClosureOperation):
    @classmethod
    def __arity__(cls):
        return 0

class IIdempotentCBinaryOperation(IClosureBinaryOperation):
    # [apply(x,x) == x]
    pass
class ICommutativeCBinaryOperation(IClosureBinaryOperation):
    # [apply(x,y) == apply(y,x)]
    pass
class IAssociativeCBinaryOperation(IClosureBinaryOperation):
    # [apply(x,apply(y,z)) == apply(apply(x,y),z)]
    pass


'''
closure
idempotent
commutative
associative
distributive
associativity
commutativity
idempotency
division
identity
divisibility
invertibility
inverse
abelian
group
monoid
magma
quasigroup
semigroup
semilattice


absorbing
distributive property
semiring

'''

class IIsTheElement(INullaryOperation):
    # [is_the_element(x)] <==> [x == apply()]
    @abstractmethod
    # obj -> bool # is_the_element(apply()) == True
    def is_the_element(self, obj):pass
class SetExcluded(ISet):
    def __init__(self, set, *IsTheElements):
        if not isinstance(set, ISet): raise TypeError
        if not all(isinstance(e, IIsTheElement) for e in IsTheElements): raise TypeError
        # if not all(set.set_equal(e.get_IO_Set()) for e in IsTheElements): raise TypeError
        if not all(set.is_element(e()) for e in IsTheElements): raise TypeError
        self.__IsTheElements = IsTheElements
        self.__set = set
    def is_element(self, obj):
        return (self.__set.is_element(obj)
            and not any(e.is_the_element(obj) for e in self.__IsTheElements)
            )
    def __iter_excluded_elements(self):
        return (e() for e in self.__IsTheElements)
    def __set_equal__(self, other):
        f = lambda self, other:\
            not any(other.is_element(e)
                    for e in self.__iter_excluded_elements())
        return (isinstance(other, __class__)
            and self.__set.set_equal(other.__set)
            and f(self, other)
            and f(other, self)
            )

class NullaryPureFunction(IPureFunction):
    def __init__(self, element):
        self.__element = element
    def apply(self):
        return self.__element
    def get_arity(self):
        return 0
    def __function_equal__(self, other):
        return self() is other()


class NullaryOperation(INullaryOperation):
    def __init__(self, element, Set):
        if not isinstance(Set, ISet): raise TypeError
        if not Set.is_element(element): raise TypeError
        super().__init__(NullaryPureFunction(element), Set)















class IRelation(metaclass=ABCMeta):pass
class INamedRef(metaclass=ABCMeta):pass




class IReferToAdd(INamedRef):
    @property
    def add(self):
        add = self.__get_add_operation__()
        assert isinstance(add, IClosureBinaryOperation)
        return add
    @abstractmethod
    # return IClosureBinaryOperation
    def __get_add_operation__(self):pass

class IReferToMul(INamedRef):
    @property
    def mul(self):
        mul = self.__get_mul_operation__()
        assert isinstance(mul, IClosureBinaryOperation)
        return mul
    @abstractmethod
    # return IClosureBinaryOperation
    def __get_mul_operation__(self):pass

class IReferToElement(INamedRef):
    @abstractmethod
    # return INullaryOperation
    def __get_the_element_nullary__(self):pass

    @property
    def the_element_nullary(self):
        nullary = self.__get_the_element_nullary__()
        assert isinstance(nullary, INullaryOperation)
        if __debug__: element = nullary()
        assert nullary.get_IO_Set().is_element(element)
        return nullary
    @property
    def the_element(self):
        return self.the_element_nullary()

class ITheMulElement(IReferToElement, IReferToMul, IRelation):
    # [mul.get_IO_Set() == the_element_nullary.get_IO_Set()]
    pass




class ITheLeftAbsorbing(ITheMulElement):
    # [the_element == mul the_element x]
    pass
class ITheRightAbsorbing(ITheMulElement):
    # [mul x the_element == the_element]
    pass
class ITheAbsorbing(ITheRightAbsorbing, ITheLeftAbsorbing):
    # [mul x the_element == the_element == mul the_element x]
    pass

def iszero_nullary2nonzero_set(iszero_nullary):
    assert isinstance(iszero_nullary, IIsTheElement)
    set = iszero_nullary.get_IO_Set()
    return SetExcluded(set, iszero_nullary)
def mul_absorbing2nonzero_set(mul_absorbing):
    assert isinstance(mul_absorbing, ITheAbsorbing)
    mul = mul_absorbing.mul
    absorbing_nullary = mul_absorbing.the_element_nullary
    assert absorbing_nullary.get_IO_Set().set_equal(mul.get_IO_Set())
    if not isinstance(the_element_nullary, IIsTheElement): raise TypeError
    return nullary_op2nonzero_set(absorbing_nullary)


class ITheLeftIdentity(ITheMulElement):
    # [mul the_element x == x]
    pass
class ITheRightIdentity(ITheMulElement):
    # [mul x the_element == x]
    # e.g. (x - 0) == x
    pass
class ITheIdentity(ITheRightIdentity, ITheLeftIdentity):
    # [mul x the_element == x == mul the_element x]
    pass
class IReferToIdentity(IReferToMul):
    # [self.mul is get_identity_nullary().mul]
    # [mul x identity == x == mul identity x]
    @abstractmethod
    def __get_TheIdentity_object__(self):pass
    def get_TheIdentity_object(self):
        obj = self.__get_TheIdentity_object__()
        assert isinstance(obj, ITheIdentity)
        return obj

    # return a nullary operation
    def get_identity_nullary(self):
        return self.get_TheIdentity_object().the_element_nullary
    @property
    def identity(self):
        return self.get_identity_nullary()()

    def __get_mul_operation__(self):
        return self.get_TheIdentity_object().mul




def is_identity_of(mul_identity, mul):
    return (isinstance(mul_identity, ITheIdentity) and
            isinstance(mul, IClosureBinaryOperation) and
            mul.operation_equal(mul_identity.mul)
            )
def is_absorbing_of(mul_absorbing, mul):
    return (isinstance(mul_absorbing, ITheAbsorbing) and
            isinstance(mul, IClosureBinaryOperation) and
            mul.operation_equal(mul_absorbing.mul)
            )




class TheSubsetMulIdentity(ITheIdentity):
    def __init__(self, subset_mul, mul_identity):
        assert isinstance(subset_mul, IOperation), TypeError
        assert isinstance(mul_identity, ITheIdentity), TypeError
        mul = mul_identity.mul
        assert isinstance(mul, IOperation)
        if not subset_mul.is_closure_operation(): raise TypeError
        if not subset_mul.is_restricted_operation_of(mul): raise ValueError
        subset = subset_mul.get_IO_Set()
        if not subset.is_element(mul_identity.identity): raise ValueError
        self.__identity_nullary = NullaryOperation(mul_identity.identity, subset)
        self.__subset_mul = subset_mul
    def __get_mul_operation__(self):
        return self.__subset_mul
    def __get_the_element_nullary__(self):
        return self.__identity_nullary



