
import sympy
from sympy import Integer, Rational, Number
from fractions import Fraction

#__all__ = ()

#assert hash(2) != hash(Integer(2))
#assert hash(Fraction(1,2)) != hash(Rational(1,2))


# Rational.__mro__
#    (<class 'sympy.core.numbers.Rational'>,
#         <class 'sympy.core.numbers.Number'>,
#         <class 'sympy.core.expr.AtomicExpr'>, <class 'sympy.core.basic.Atom'>, <class 'sympy.core.expr.Expr'>, <class 'sympy.core.basic.Basic'>, <class 'sympy.core.evalf.EvalfMixin'>, <class 'object'>)
# type(Rational(1,2)).__mro__
#    (<class 'sympy.core.numbers.Half'>, <class 'sympy.core.numbers.RationalConstant'>,
#         <class 'sympy.core.numbers.Rational'>
#         ......)

# type(Integer(1)).__mro__
#    (<class 'sympy.core.numbers.One'>, <class 'sympy.core.numbers.IntegerConstant'>,
#          <class 'sympy.core.numbers.Integer'>,
#          <class 'sympy.core.numbers.Rational'>,
#          .......)

assert type(Rational(1,2)).__hash__ is Rational.__hash__
assert type(Integer(1)).__hash__ is Integer.__hash__
org_rational_hash = Rational.__hash__
org_integer_hash = Integer.__hash__
org_number_hash = Number.__hash__


def sympy_rational2stdpy_fraction(sympy_rational):
    assert sympy_rational.is_rational
    return Fraction(*map(int,sympy.fraction(sympy_rational)))

Integer.__hash__ = lambda x: hash(int(x))
Rational.__hash__ = lambda x: hash(sympy_rational2stdpy_fraction(x))




