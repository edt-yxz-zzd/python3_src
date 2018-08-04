


from .IAlgebra import \
    ( ISet
    , IOperation
    , INullaryOperation
    , IRelation
    , INamedRef
    , IClosureBinaryOperation
    , ICommutativeCBinaryOperation
    , ITheIdentity
    , ITheAbsorbing
    , IIdempotentCBinaryOperation
    , IReferToAdd
    , IReferToMul
    , SetExcluded
    , IIsTheElement
    , TheSubsetMulIdentity
    )
from .is_group import \
    ( is_group
    , LeftInverse2RightDivision
    , RightInverse2LeftDivision
    , is_inv_of
    )



class ILeftDistributivity(IReferToAdd, IReferToMul, IRelation):
    # [mul.get_IO_Set() == add.get_IO_Set()]
    # [(x `mul` add a b) == (mul x a `add` x b)]
    pass
class IRightDistributivity(IReferToAdd, IReferToMul, IRelation):
    # [mul.get_IO_Set() == add.get_IO_Set()]
    # [(add a b `mul` y) == (mul a y `add` b y)]
    pass
class IDistributivity(IRightDistributivity, ILeftDistributivity):
    # [mul.get_IO_Set() == add.get_IO_Set()]
    # [(x `mul` add a b) == (mul x a `add` x b)]
    # [(add a b `mul` y) == (mul a y `add` b y)]
    pass



def is_semiring(set, add, mul, zero_nullary, one_nullary
        , add_identity_zero, mul_identity_one, mul_absorbing_zero
        , distributivity):
    assert isinstance(set, ISet)
    assert isinstance(add, IOperation)
    assert isinstance(mul, IOperation)
    assert isinstance(zero_nullary, IOperation)
    assert isinstance(one_nullary, IOperation)
    assert isinstance(add_identity_zero, INamedRef)
    assert isinstance(mul_identity_one, INamedRef)
    assert isinstance(mul_absorbing_zero, INamedRef)
    assert isinstance(distributivity, IRelation)

    if not (isinstance(set, ISet)
        and isinstance(add, IClosureBinaryOperation)
        and isinstance(mul, IClosureBinaryOperation)
        and isinstance(zero_nullary, INullaryOperation)
        and isinstance(one_nullary, INullaryOperation)
        and isinstance(add_identity_zero, ITheIdentity)
        and isinstance(mul_identity_one, ITheIdentity)
        and isinstance(mul_absorbing_zero, ITheAbsorbing)
        and isinstance(distributivity, IDistributivity)
        ):
        return False

    return (zero_nullary.operation_equal(add_identity_zero.the_element_nullary)
        and zero_nullary.operation_equal(mul_absorbing_zero.the_element_nullary)
        and one_nullary.operation_equal(mul_identity_one.the_element_nullary)
        and add.operation_equal(add_identity_zero.mul)
        and add.operation_equal(distributivity.add)
        and mul.operation_equal(mul_absorbing_zero.mul)
        and mul.operation_equal(mul_identity_one.mul)
        and mul.operation_equal(distributivity.mul)
        and is_monoid(set, add, add_identity_zero)
        and isinstance(add, ICommutativeCBinaryOperation)
        and is_monoid(set, mul, mul_identity_one)
        )


def is_commutative_semiring(set, add, mul, zero_nullary, one_nullary
        , add_identity_zero, mul_identity_one, mul_absorbing_zero
        , distributivity):
    return is_semiring(
                set, add, mul, zero_nullary, one_nullary
                , add_identity_zero, mul_identity_one, mul_absorbing_zero
                , distributivity)\
        and isinstance(mul, ICommutativeCBinaryOperation)

def is_idempotent_semiring(set, add, mul, zero_nullary, one_nullary
        , add_identity_zero, mul_identity_one, mul_absorbing_zero
        , distributivity):
    return is_semiring(
                set, add, mul, zero_nullary, one_nullary
                , add_identity_zero, mul_identity_one, mul_absorbing_zero
                , distributivity)\
        and isinstance(add, IIdempotentCBinaryOperation)



def is_ring(set, add, sub, neg, mul, zero_nullary, one_nullary
        , add_identity_zero, mul_identity_one, mul_absorbing_zero
        , distributivity):
    return is_semiring(
                set, add, mul, zero_nullary, one_nullary
                , add_identity_zero, mul_identity_one, mul_absorbing_zero
                , distributivity)\
        and is_abelian_group(set, add, sub, add_identity_zero, neg)

def is_commutative_ring(
        set, add, sub, neg, mul, zero_nullary, one_nullary
        , add_identity_zero, mul_identity_one, mul_absorbing_zero
        , distributivity):
    return is_ring(
                set, add, sub, neg, mul, zero_nullary, one_nullary
                , add_identity_zero, mul_identity_one, mul_absorbing_zero
                , distributivity)\
        and isinstance(mul, ICommutativeCBinaryOperation)


'''
is_abelian_group
is_monoid
    commutative rings > integral domains > integrally closed domains > GCD domains > unique factorization domains > principal ideal domains > Euclidean domains > fields > finite fields 
Field: a commutative ring which contains a multiplicative inverse for every nonzero element
zero ring v.s. nonzero ring
    zero ring <=> only one element <=> trivial ring
domain is a nonzero ring in which ab = 0 implies a = 0 or b = 0.
    "the zero-product property"
    Equivalently, a domain is a ring in which 0 is the only left zero divisor (or equivalently, the only right zero divisor).
integral domain = commutative domain
integrally closed domain A =
    iff:
        A is a integral domain
        let F = "fraction field of A"
        A.set == "integral closure of A in F"
    1) "monic polynomial over A" = {x^n + sum s[i]*x^i {0<=i<n} |n>0, s <- A^n}
    2) "integral closure of A in B" =
        requires:
            B is a commutative ring
            A is a subring of B
        {b in B.set | f <- "monic polynomial over A", f(b) == 0}
        remark:
            "integral closure of A in B" is a subring of B
                A.set <= "integral closure of A in B" <= B.set
            ZZ is the integral closure of ZZ in QQ
                Note: "monic"
                    x + z = 0 ==>> x = -z ==>> x in ZZ
                    if (x^n + ...) is irreducible and n > 1, then x not in QQ

    3) "fraction field F of integral domain D" =
        F.set = D.set * (D.set\\{0})
'''

def is_trivial_ring(set, add, sub, neg, mul, zero_eq_nullary, one_nullary
        , add_identity_zero, mul_identity_one, mul_absorbing_zero
        , distributivity)
    assert isinstance(zero_eq_nullary, IIsTheElement)
    return (is_ring(
                set, add, sub, neg, mul, zero_eq_nullary, one_nullary
                , add_identity_zero, mul_identity_one, mul_absorbing_zero
                , distributivity)
        and isinstance(zero_eq_nullary, IIsTheElement)
        and zero_eq_nullary.is_the_element(one_nullary())
        )

def is_nontrivial_ring(set, add, sub, neg, mul, zero_eq_nullary, one_nullary
        , add_identity_zero, mul_identity_one, mul_absorbing_zero
        , distributivity)
    assert isinstance(zero_eq_nullary, IIsTheElement)
    return (is_ring(
                set, add, sub, neg, mul, zero_eq_nullary, one_nullary
                , add_identity_zero, mul_identity_one, mul_absorbing_zero
                , distributivity)
        and isinstance(zero_eq_nullary, IIsTheElement)
        and not zero_eq_nullary.is_the_element(one_nullary())
        )


def is_nonzero_set_of(nonzero_set, set, zero_eq_nullary):
    assert isinstance(zero_eq_nullary, IIsTheElement)
    assert isinstance(nonzero_set, ISet)
    assert isinstance(set, ISet)
    assert isinstance(zero_eq_nullary, IOperation)

    return (isinstance(set, ISet)
        and isinstance(nonzero_set, SetExcluded)
        and isinstance(zero_eq_nullary, IIsTheElement)
        and SetExcluded(set, zero_eq_nullary).set_equal(nonzero_set)
        and zero_eq_nullary() in set
        and zero_eq_nullary() not in nonzero_set
        )


def is_nonzero_mul_of(nonzero_mul, mul, zero_eq_nullary, nonzero_set, set):
    assert isinstance(zero_eq_nullary, IIsTheElement)
    assert isinstance(nonzero_mul, IOperation)
    assert isinstance(mul, IOperation)
    assert isinstance(nonzero_set, ISet)
    assert isinstance(set, ISet)
    assert isinstance(zero_eq_nullary, IOperation)
    return (is_magma(set, mul) and is_magma(nonzero_set, nonzero_mul)
        and isinstance(nonzero_mul, IClosureBinaryOperation)
        and isinstance(mul, IClosureBinaryOperation)
        and mul.underlying_function_equal(nonzero_mul)

        and is_nonzero_set_of(nonzero_set, set, zero_eq_nullary)

        and mul.get_IO_Set().set_equal(set)
        and nonzero_mul.get_IO_Set().set_equal(nonzero_set)
        )

def is_domain(set, nonzero_set, add, sub, neg, mul, nonzero_mul
        , zero_eq_nullary, one_nullary
        , add_identity_zero, mul_identity_one, mul_absorbing_zero
        , distributivity)
    assert isinstance(zero_eq_nullary, IIsTheElement)
    return (is_nontrivial_ring(
                set, add, sub, neg, mul, zero_eq_nullary, one_nullary
                , add_identity_zero, mul_identity_one, mul_absorbing_zero
                , distributivity)
        and is_nonzero_mul_of(nonzero_mul, mul, zero_eq_nullary, nonzero_set, set)
        )

def is_integral_domain(set, nonzero_set, add, sub, neg, mul, nonzero_mul
        , zero_eq_nullary, one_nullary
        , add_identity_zero, mul_identity_one, mul_absorbing_zero
        , distributivity)

    return (is_domain(
                set, nonzero_set, add, sub, neg, mul, nonzero_mul
                , zero_eq_nullary, one_nullary
                , add_identity_zero, mul_identity_one, mul_absorbing_zero
                , distributivity)
        and is_commutative_ring(
                set, add, sub, neg, mul, zero_eq_nullary, one_nullary
                , add_identity_zero, mul_identity_one, mul_absorbing_zero
                , distributivity)
        )


def is_field(set, nonzero_set, add, sub, neg, mul, nonzero_mul, nonzero_inv
        , zero_eq_nullary, one_nullary
        , add_identity_zero, mul_identity_one, mul_absorbing_zero
        , distributivity):
    if not (is_commutative_ring(
                set, add, sub, neg, mul, zero_eq_nullary, one_nullary
                , add_identity_zero, mul_identity_one, mul_absorbing_zero
                , distributivity)
        and is_nonzero_mul_of(nonzero_mul, mul, zero_eq_nullary, nonzero_set, set)
        and is_inv_of(nonzero_inv, nonzero_mul)
        ):
        return False

    nonzero_mul_identity = TheSubsetMulIdentity(nonzero_mul, mul_identity_one)
    nonzero_left_div = RightInverse2LeftDivision(nonzero_inv)
    nonzero_right_div = LeftInverse2RightDivision(nonzero_inv)
    return is_group(
                nonzero_set, nonzero_mul, nonzero_left_div, nonzero_right_div
                , nonzero_mul_identity, nonzero_inv)








