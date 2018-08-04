
# NOTE: 4**Fraction(1,3) -> float
# so, we can use Fraction instead of Rational !!!!!!
#bug: from ..math_nn.constant import * 


# sympy bug:
#   hash(2) != hash(Integer(2))



from sympy import Integer as Int

one = Int(1)
zero = Int(0)
two = Int(2)
half = one/2
three = Int(3)

del Int


