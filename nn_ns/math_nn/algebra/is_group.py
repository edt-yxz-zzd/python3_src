


from .IAlgebra import \
    ( IClosureBinaryOperation
    , IReferToMul
    , ICommutativeCBinaryOperation
    , IClosureUnaryOperation
    , IClosureOperation
    , IOperation
    , IAssociativeCBinaryOperation
    , ICommutativeCBinaryOperation
    , IIdempotentCBinaryOperation
    , ITheIdentity
    , IReferToIdentity
    , _Callable2PureFunction_
    )


class ILeftDivision(IClosureBinaryOperation, IReferToMul):
    # d\n ::= apply(n,d)
    # [d*q == n] ==>> [q == d\n]
    # [q == d\(d*q)]
    # [q == apply(mul(d,q),d)]
    def left_div(self, n, d):
        return self(n,d)
class IRightDivision(IClosureBinaryOperation, IReferToMul):
    # n/d ::= apply(n,d)
    # [q*d == n] ==>> [q == n/d]
    # [q == (q*d)/d]
    # [q == apply(mul(q,d),d)]
    def right_div(self, n, d):
        return self(n,d)
class IDivision(IRightDivision, ILeftDivision):
    # [n/d == d\n]
    # [(n/d)*d == d*(d\n)] ==>> [q*d == d*q] i.e. commutativity
    # mul -> return ICommutativeCBinaryOperation
    @property
    def mul(self):
        mul = super().mul
        assert isinstance(mul, ICommutativeCBinaryOperation)
        return mul
    def div(self, n, d):
        return self(n,d)



class ILeftInverse(IClosureUnaryOperation, IReferToIdentity):
    # [(apply x `mul` x) == mul.identity]
    def left_inverse_of(self, x):
        return self(x)
class IRightInverse(IClosureUnaryOperation, IReferToIdentity):
    # [(x `mul` apply x) == mul.identity]
    def right_inverse_of(self, x):
        return self(x)
class IInverse(IRightInverse, ILeftInverse):
    # [(x `mul` apply x) == mul.identity == apply x `mul` x]
    def inverse_of(self, x):
        return self(x)

def is_inv_of(inv, mul):
    return (isinstance(inv, IInverse)
        and isinstance(mul, IClosureBinaryOperation)
        and inv.mul.operation_equal(mul)
        )

class RightInverse2LeftDivision(ILeftDivision):
    # requires: IAssociativeCBinaryOperation
    # RightInverse ==>> Identity
    # [d\n == d\(1*n) == d\((d * right_inv d)*n)
    #   =[assoc]= d\(d*(right_inv d * n))
    #   =[cancel]= right_inv d * n
    #  ]
    def __init__(self, right_inv):
        if not isinstance(right_inv, IRightInverse): raise TypeError
        if not isinstance(right_inv.mul, IAssociativeCBinaryOperation): raise TypeError
        self.__right_inv = right_inv
        f = _Callable2PureFunction_(self.__left_div, 2)
        super().__init__(f, right_inv.mul.get_IO_set())
    def __left_div(self, n, d):
        right_inv = self.__right_inv
        mul = right_inv.mul
        return mul(right_inv(d), n)

class LeftInverse2RightDivision(IRightDivision):
    # requires: IAssociativeCBinaryOperation
    # LeftInverse ==>> Identity
    # [n/d == (n*1)/d == (n*(left_inv d * d))/d
    #   =[assoc]= ((n * left_inv d)*d))/d
    #   =[cancel]= n * left_inv d
    #  ]
    def __init__(self, left_inv):
        if not isinstance(left_inv, ILeftInverse): raise TypeError
        if not isinstance(left_inv.mul, IAssociativeCBinaryOperation): raise TypeError
        self.__left_inv = left_inv
        f = _Callable2PureFunction_(self.__right_div, 2)
        super().__init__(f, left_inv.mul.get_IO_set())
    def __right_div(self, n, d):
        left_inv = self.__left_inv
        mul = left_inv.mul
        return mul(n, left_inv(d))








def is_magma(set, mul):
    assert isinstance(set, ISet)
    assert isinstance(mul, IOperation)
    return (isinstance(set, ISet) and
            isinstance(mul, IClosureBinaryOperation) and
            mul.is_binary_operation() and
            mul.is_IO_Set(set)
            )
def is_semigroup(set, mul):
    return is_magma(set, mul) and isinstance(mul, IAssociativeCBinaryOperation)
def is_semilattice(set, mul):
    return (is_semigroup(set, mul) and
            isinstance(mul, ICommutativeCBinaryOperation) and
            isinstance(mul, IIdempotentCBinaryOperation)
            )
def is_quasigroup(set, mul, left_div, right_div):
    assert isinstance(mul, IOperation)
    assert isinstance(left_div, IOperation)
    assert isinstance(right_div, IOperation)
    if not is_magma(set, mul): return False
    return (all(map(isinstance
                    , [left_div, right_div]
                    , [ILeftDivision, IRightDivision]))
            and all(map(mul.operation_equal
                        , [left_div.mul, right_div.mul]))
            )
def is_commutative_quasigroup(set, mul, div):
    assert isinstance(div, IOperation)
    return (is_quasigroup(set, mul, div, div) and
            isinstance(div, IDivision) and
            isinstance(mul, ICommutativeCBinaryOperation)
            )

def is_loop(set, mul, left_div, right_div
        , mul_identity, left_inv, right_inv):
    assert isinstance(left_inv, IOperation)
    assert isinstance(right_inv, IOperation)
    return (is_quasigroup(set, mul, left_div, right_div)
            and all(map(isinstance
                    , [mul_identity, left_inv, right_inv]
                    , [ITheIdentity, ILeftInverse, IRightInverse]))
            and all(map(mul.operation_equal
                        , [mul_identity.mul, left_inv.mul, right_inv.mul]))
            and all(map(mul_identity.the_element_nullary.operation_equal
                        , [ left_inv.get_identity_nullary()
                          , right_inv.get_identity_nullary()]))
            )

def is_loop_inv(set, mul, left_div, right_div, mul_identity, inv):
    assert isinstance(inv, IOperation)
    return (is_loop(set, mul, left_div, right_div, mul_identity, inv, inv)
            and isinstance(inv, IInverse))

def is_monoid(set, mul, mul_identity):
    return (is_semigroup(set, mul)
        and isinstance(mul_identity, ITheIdentity)
        and mul.operation_equal(mul_identity.mul)
        )

def is_group(set, mul, left_div, right_div, mul_identity, inv):
    return is_loop_inv(set, mul, left_div, right_div, mul_identity, inv)\
        and is_monoid(set, mul, mul_identity)

def is_abelian_group(set, mul, div, mul_identity, inv):
    return (is_group(set, mul, div, div, mul_identity, inv) and
            is_commutative_quasigroup(set, mul, div)
            )


