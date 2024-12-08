#__all__:goto
r'''[[[
e ../../python3_src/seed/math/floor_ceil__tiny.py

seed.math.floor_ceil__tiny
py -m nn_ns.app.debug_cmd   seed.math.floor_ceil__tiny -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.floor_ceil__tiny:__doc__ -ht # -ff -df

>>> fractional_fixed_point_part_of_(5/4)
0.25
>>> fractional_fixed_point_part_of_(-5/4)
0.75
>>> fractional_fixed_point_part_of_neg_(5/4)
0.75
>>> fractional_fixed_point_part_of_neg_(-5/4)
0.25


>>> fractional_fixed_point_part_of_(5)
0
>>> fractional_fixed_point_part_of_(-5)
0
>>> fractional_fixed_point_part_of_neg_(5)
0
>>> fractional_fixed_point_part_of_neg_(-5)
0



>>> from seed.math.continued_fraction.continued_fraction_ops____using_LazyList import ContinuedFraction
>>> cf_5_3 = ContinuedFraction([1,1,1,1])
>>> fractional_fixed_point_part_of_(cf_5_3)
ContinuedFraction(LazyList([0, 1, 1, <...>]))
>>> fractional_fixed_point_part_of_(-cf_5_3)
ContinuedFraction(LazyList([0, 2, <...>]))
>>> fractional_fixed_point_part_of_neg_(cf_5_3)
ContinuedFraction(LazyList([0, 2, <...>]))
>>> fractional_fixed_point_part_of_neg_(-cf_5_3)
ContinuedFraction(LazyList([0, 1, 1, <...>]))

>>> 1 - fractional_fixed_point_part_of_(cf_5_3)
ContinuedFraction(LazyList([0, 2, 1, <...>]))
>>> 1 - fractional_fixed_point_part_of_(-cf_5_3)
ContinuedFraction(LazyList([0, 1, 1, 1, <...>]))
>>> 1 - fractional_fixed_point_part_of_neg_(cf_5_3)
ContinuedFraction(LazyList([0, 1, 1, 1, <...>]))
>>> 1 - fractional_fixed_point_part_of_neg_(-cf_5_3)
ContinuedFraction(LazyList([0, 2, 1, <...>]))


>>> 1 == fractional_fixed_point_part_of_(cf_5_3) + fractional_fixed_point_part_of_neg_(cf_5_3)
True
>>> 1 == fractional_fixed_point_part_of_(-cf_5_3) + fractional_fixed_point_part_of_neg_(-cf_5_3)
True



>>> 1 == cf_5_3.fractional_fixed_point_part_of_() + cf_5_3.fractional_fixed_point_part_of_neg_()
True


>>> 1 == fractional_fixed_point_part_of_(7/4) + fractional_fixed_point_part_of_neg_(7/4)
True
>>> 0 == fractional_fixed_point_part_of_(7) + fractional_fixed_point_part_of_neg_(7)
True





py_adhoc_call   seed.math.floor_ceil__tiny   @f
#]]]'''
__all__ = r'''
floor_
ceil_
fractional_fixed_point_part_of_
fractional_fixed_point_part_of_neg_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...

from math import floor as floor_, ceil as ceil_

def fractional_fixed_point_part_of_(x, /):
    'x -> (x -floor_(x)) #see:seed.math.continued_fraction.continued_fraction_ops____using_LazyList.ContinuedFraction'
    return (x -floor_(x))
def fractional_fixed_point_part_of_neg_(x, /):
    'x -> (ceil_(x) -x)/(-x -floor_(-x)) #see:seed.math.continued_fraction.continued_fraction_ops____using_LazyList.ContinuedFraction'
    return (ceil_(x) -x)



__all__
from seed.math.floor_ceil__tiny import floor_, ceil_
from seed.math.floor_ceil__tiny import fractional_fixed_point_part_of_, fractional_fixed_point_part_of_neg_
from seed.math.floor_ceil__tiny import *
