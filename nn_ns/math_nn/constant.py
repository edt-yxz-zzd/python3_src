
from fractions import Fraction as Int

#from sympy import Integer as Int
# sympy bug:
#   hash(2) != hash(Integer(2))

one = Int(1)
zero = Int(0)
two = Int(2)
half = one/2
three = Int(3)

del Int

