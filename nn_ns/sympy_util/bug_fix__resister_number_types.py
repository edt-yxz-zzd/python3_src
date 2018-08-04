
'''
sympy bugs from fraction_division.py
bug:
    from sympy import Integer
    from numbers import Integral
    assert not issubclass(Integer, Integral)
    TODO::sympy abstract base class for Number int float complex....
    fixed by:
        import nn_ns.sympy_util.bug_fix__resister_number_types

'''

import numbers
import sympy


numbers.Number.register(sympy.Number)
#numbers.Complex.register(sympy.?????)
numbers.Real.register(sympy.Float)
numbers.Rational.register(sympy.Rational)
numbers.Integral.register(sympy.Integer)

sympy.Rational.numerator = property(lambda self: sympy.fraction(self)[0])
sympy.Rational.denominator = property(lambda self: sympy.fraction(self)[1])






