#__all__:goto
r'''[[[
e ../../python3_src/seed/math/binary_float/binary_float_ops____using_LazyList.py
see:
    view ../../python3_src/seed/types/LazyList.py
    view ../../python3_src/seed/math/continued_fraction/continued_fraction_ops____using_LazyList.py
    view ../../python3_src/seed/math/binary_float/binary_float_ops____using_LazyList.py
    view ../../python3_src/seed/math/binary_float/py_float_repr.py
e ../../python3_src/seed/math/binary_float/py_float_repr.py
e ../../python3_src/seed/math/binary_float/FloatNumberError.py


perturbation n. 微扰
  perturb vt. 扰乱
precision n. 精度
accuracy n. 精确度/准确度
mantissa n. 尾数，定点小数部分
significand n. 有效位数
exponent n. 指数/幂
radix/base n. 基数/根数/底




news:
    ++bf_is_power_of_2_
    ++.is_power_of_2_
    ++.__lshift__
    ++.__rshift__
        update bf_truediv/.__truediv__ if rhs.is_power_of_2_











doctest____begin:goto
doctest____end:goto


[[
===
bf_cmp_
bf_neg
    bf_lshift_
    bf_rshift_
bf_sub__p_p
bf_add__p_p
bf_truediv
bf_floor_ex_

bf_sub
bf_add
bf_inv
bf_mul

===
bf_add(lhs, rhs)
    | rhs == 0 = lhs
    | lhs == 0 = rhs
    | lhs < 0 && rhs < 0 = bf_neg(bf_add__p_p(bf_neg(lhs), bf_neg(rhs)))
    | lhs > 0 && rhs < 0 = bf_sub__p_p(lhs, bf_neg(rhs))
    | lhs < 0 && rhs > 0 = bf_neg(bf_sub__p_p(bf_neg(lhs), rhs))
    | lhs > 0 && rhs > 0 = bf_add__p_p(lhs, rhs)
bf_sub(lhs, rhs)
    = bf_add(lhs, bf_neg(rhs))
bf_inv(rhs)
    = bf_truediv(1, rhs)
bf_mul(lhs, rhs)
    = bf_truediv(lhs, bf_inv(rhs))

===
]]



seed.math.binary_float.binary_float_ops____using_LazyList
py -m nn_ns.app.debug_cmd   seed.math.binary_float.binary_float_ops____using_LazyList -x
py -m nn_ns.app.doctest_cmd seed.math.binary_float.binary_float_ops____using_LazyList:__doc__ -ff -v
py_adhoc_call   seed.math.binary_float.binary_float_ops____using_LazyList   @f

from seed.math.binary_float.binary_float_ops____using_LazyList import BinaryFloat




doctest____begin:here

    bf_to_bin_float_repr_
        bf_to_hex_float_repr_


    mk_binary_float_digits5float_
    mk_binary_float_digits5int_
        iter_binary_float_digits5int_
            gde2_

    positive_bf_digits2flatten_
        positive_bf_digits5flatten_

    bf_std_











def positive_bf_digits5flatten_(flatten_bf_digits, /, *, to_neg=False):

%s/mk\[\]/mk[()]/g
>>> class MkLazyList:
...     def __call__(sf, flatten_bf_digits=None, /, *, to_neg=False):
...         if flatten_bf_digits is None: return _bf_0
...         return positive_bf_digits5flatten_(flatten_bf_digits, to_neg=to_neg)
...     def __getitem__(sf, xs, /):
...         check_type_is(tuple, xs)
...         if xs and type(xs[0]) is slice:
...             xs0 = xs[0]
...             xs = ((xs0.start, xs0.stop), *xs[1:])
...         if xs:
...             check_type_is(tuple, xs[0])
...         it = iter(xs)
...         return LazyList(it)
>>> mk = MkLazyList()
>>> from itertools import islice
>>> list_ = lambda sz, it, /: list(islice(it, sz))

>>> list(bf_neg(mk[()]))
[]
>>> list(bf_neg(mk[(+1, 999),]))
[(-1, 999)]
>>> list(bf_neg(mk[(-1, 999),]))
[(1, 999)]
>>> list(bf_neg(mk[(+1, -999),]))
[(-1, -999)]
>>> list(bf_neg(mk[(-1, -999),]))
[(1, -999)]
>>> list(bf_neg(mk[(+1, 999), 1]))
[(-1, 999), 1]
>>> list(bf_neg(mk[(-1, 999), 1]))
[(1, 999), 1]
>>> list(bf_neg(mk[(+1, 999), 0]))
[(-1, 999), 0]
>>> list(bf_neg(mk[(-1, 999), 0]))
[(1, 999), 0]


>>> list(bf_inv(mk[()]))
Traceback (most recent call last):
    ...
seed.math.binary_float.binary_float_ops____using_LazyList.FloatNumberError__div0
>>> list(bf_inv(mk[(+1, 999),]))
[(1, -999)]
>>> list(bf_inv(mk[(-1, 999),]))
[(-1, -999)]
>>> list(bf_inv(mk[(+1, -999),]))
[(1, 999)]
>>> list(bf_inv(mk[(-1, -999),]))
[(-1, 999)]

>>> list(bf_inv(mk[(+1, 999), 0]))
[(1, -999)]
>>> list(bf_inv(mk[(-1, 999), 0]))
[(-1, -999)]
>>> list_(6, bf_inv(mk[(+1, 1), 1]))
[(1, -2), 0, 1, 0, 1, 0]
>>> list_(6, bf_inv(mk[(+1, 999), 1]))
[(1, -1000), 0, 1, 0, 1, 0]
>>> list_(6, bf_inv(mk[(-1, 999), 1]))
[(-1, -1000), 0, 1, 0, 1, 0]

>>> list(bf_inv(mk[()]))
Traceback (most recent call last):
    ...
seed.math.binary_float.binary_float_ops____using_LazyList.FloatNumberError__div0






>>> from seed.tiny import echo
>>> echo(bf_floor_(mk[()]))
0
>>> echo(bf_floor_(mk[+1:2, 0, 1, 0, 1]))
5
>>> echo(bf_floor_(mk[-1:2, 0, 1, 0, 1]))
-6
>>> echo(bf_floor_(mk[-1:2, 0, 1]))
-5






>>> list(bf_add(mk[()], mk[()]))
[]
>>> list(bf_add(mk[()], mk[+1:-2,]))
[(1, -2)]
>>> list(bf_add(mk[-1:-2,], mk[+1:-2,]))
[]


+0b0.0111001
-0b0.10011
(+) -->:
-0b0.0010011
>>> list(bf_add(mk[+1:-2, 1,1,0,0, 1], mk[-1:-1,0,0,1,1]))
[(-1, -3), 0, 0, 1, 1]


>>> _bf_A = mk[+1:-2, 1,1,0,0, 1]
>>> _bf_B = mk[-1:-1,0,0,1,1]
>>> _bf_0 = mk[()]
>>> _bf_4 = mk[+1:+2,]
>>> _bf_neg8th = mk[-1:-3,]
>>> _bf_3 = mk[+1:+1, 1]
>>> _bf_neg5div4 = mk[-1:+0, 0, 1]


TODO:

>>> list(bf_mul(_bf_0, _bf_0))
[]
>>> list(bf_mul(_bf_0, _bf_A))
[]
>>> list(bf_mul(_bf_B, _bf_0))
[]
>>> ert
>>> list(bf_mul(mk[()], mk[0])) # ??? [+oo*0 == +oo]
[]
>>> list(bf_mul(mk[0], mk[()]))
[]
>>> list(bf_mul(mk[0, 1], mk[0]))
[0]
>>> list(bf_mul(mk[0, 1], mk[1]))
[1]
>>> list(bf_mul(mk[-2, 1,3,4,2], mk[0,4,2,2,1]))
[-1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 10]
>>> list(iter_approximate_fractions5continued_fraction_([-1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 10]))[-1]
Fraction(-329, 1178)
>>> Fraction(-47, 38) * Fraction(7, 31)
Fraction(-329, 1178)



>>> echo(bf_cmp_(mk[()], mk[()]))
0
>>> echo(bf_cmp_(mk[()], mk[0]))
1
>>> echo(bf_cmp_(mk[0], mk[()]))
-1
>>> echo(bf_cmp_(mk[0], mk[0]))
0
>>> echo(bf_cmp_(mk[0], mk[1]))
-1
>>> echo(bf_cmp_(mk[1], mk[0]))
1
>>> echo(bf_cmp_(mk[0, 1], mk[1]))
0
>>> echo(bf_cmp_(mk[1], mk[0, 1]))
0
>>> echo(bf_cmp_(mk[1, 1], mk[1, 1]))
0
>>> echo(bf_cmp_(mk[1, 1], mk[1, 2]))
1
>>> echo(bf_cmp_(mk[1, 2], mk[1, 1]))
-1
>>> echo(bf_cmp_(mk[1, 1, 1], mk[1, 1]))
-1
>>> echo(bf_cmp_(mk[1, 1], mk[1, 1, 1]))
1
>>> echo(bf_cmp_(mk[1, 1, 1], mk[1, 2]))
0
>>> echo(bf_cmp_(mk[1, 2], mk[1, 1, 1]))
0
>>> echo(bf_cmp_(mk[1, 1, 2], mk[1, 1]))
-1
>>> echo(bf_cmp_(mk[1, 1], mk[1, 1, 2]))
1
>>> echo(bf_cmp_(mk[1, 1, 2], mk[1, 1, 1]))
1
>>> echo(bf_cmp_(mk[1, 1, 1], mk[1, 1, 2]))
-1
>>> echo(bf_cmp_(mk[1, 1, 2], mk[1, 1, 1, 1]))
0
>>> echo(bf_cmp_(mk[1, 1, 1, 1], mk[1, 1, 2]))
0
>>> echo(bf_cmp_(mk[1, 1, 2], mk[1, 1, 1, 1, 2]))
1
>>> echo(bf_cmp_(mk[1, 1, 1, 1, 2], mk[1, 1, 2]))
-1



>>> list(iter_approximate_fractions5continued_fraction_([4,2,3,5]))[-1]
Fraction(164, 37)
>>> list(iter_approximate_fractions5continued_fraction_([1,7,2,3]))[-1]
Fraction(59, 52)
>>> Fraction(164, 37) / Fraction(59, 52)
Fraction(8528, 2183)
>>> list(iter_approximate_fractions5continued_fraction_([3, 1, 9, 1, 2, 2, 1, 9, 2]))[-1]
Fraction(8528, 2183)
>>> divmod(Fraction(164, 37), Fraction(59, 52))
(3, Fraction(1979, 1924))
>>> list(iter_approximate_fractions5continued_fraction_([1, 34, 1, 54]))[-1]
Fraction(1979, 1924)
>>> list(bf_truediv(mk[4,2,3,5], mk[1,7,2,3]))
[3, 1, 9, 1, 2, 2, 1, 9, 2]
>>> len(bf_divmod(mk[4,2,3,5], mk[1,7,2,3]))
2
>>> echo(bf_divmod(mk[4,2,3,5], mk[1,7,2,3])[0])
3
>>> list(bf_divmod(mk[4,2,3,5], mk[1,7,2,3])[1])
[1, 34, 1, 54]


>>> echo(bf_lt_(mk[1], mk[1]))
False
>>> echo(bf_lt_(mk[1], mk[2]))
True
>>> echo(bf_lt_(mk[2], mk[1]))
False

>>> echo(bf_gt_(mk[1], mk[1]))
False
>>> echo(bf_gt_(mk[1], mk[2]))
False
>>> echo(bf_gt_(mk[2], mk[1]))
True

>>> echo(bf_le_(mk[1], mk[1]))
True
>>> echo(bf_le_(mk[1], mk[2]))
True
>>> echo(bf_le_(mk[2], mk[1]))
False

>>> echo(bf_ge_(mk[1], mk[1]))
True
>>> echo(bf_ge_(mk[1], mk[2]))
False
>>> echo(bf_ge_(mk[2], mk[1]))
True

>>> echo(bf_eq_(mk[1], mk[1]))
True
>>> echo(bf_eq_(mk[1], mk[2]))
False
>>> echo(bf_eq_(mk[2], mk[1]))
False

>>> echo(bf_ne_(mk[1], mk[1]))
False
>>> echo(bf_ne_(mk[1], mk[2]))
True
>>> echo(bf_ne_(mk[2], mk[1]))
True


>>> 0**0 #ZeroDivisionError
1
>>> 0**-2 #ZeroDivisionError
Traceback (most recent call last):
    ...
ZeroDivisionError: 0.0 cannot be raised to a negative power











decorator4protocol4ToConcatLazyList_
ContinuedFraction
is_int
math.floor
math.ceil
abs + - inv_
+ * - / % // divmod pow
== !=
> < >= <=


>>> bf_0
ContinuedFraction(LazyList([<...>]))
>>> bool(bf_0)
Traceback (most recent call last):
    ...
TypeError: 'ellipsis' object is not callable
>>> len(bf_0)
Traceback (most recent call last):
    ...
TypeError: 'ellipsis' object is not callable
>>> 0 in bf_0
Traceback (most recent call last):
    ...
TypeError: 'ellipsis' object is not callable

>>> bf_0 == bf_0
True
>>> bf_0 != bf_0
False
>>> bf_0 < bf_0
False
>>> bf_0 <= bf_0
True
>>> bf_0 > bf_0
False
>>> bf_0 >= bf_0
True

>>> bf_0 == bf_1
False
>>> bf_0 != bf_1
True
>>> bf_0 < bf_1
True
>>> bf_0 <= bf_1
True
>>> bf_0 > bf_1
False
>>> bf_0 >= bf_1
False

>>> bf_21_over_13 = ContinuedFraction(Fraction(21, 13))
>>> bfs = [bf_e, bf_golden_ratio_phi, bf_sqrt2, bf_pi__prefix2001, bf_0, bf_1, bf_neg1, bf_21_over_13]
>>> bfs.sort()
>>> bfs
[ContinuedFraction(LazyList([-1])), ContinuedFraction(LazyList([0])), ContinuedFraction(LazyList([1])), ContinuedFraction(LazyList([1, 2, 2, <...>])), ContinuedFraction(LazyList([1, 1, 1, 1, 1, 2])), ContinuedFraction(LazyList([1, 1, 1, 1, 1, 1, 1, 1, <...>])), ContinuedFraction(LazyList([2, 1, <...>])), ContinuedFraction(LazyList([3, 7, <...>]))]
>>> [bf.is_int() for bf in bfs]
[True, True, True, False, False, False, False, False]
>>> import math
>>> [math.floor(bf) for bf in bfs]
[-1, 0, 1, 1, 1, 1, 2, 3]
>>> [math.ceil(bf) for bf in bfs]
[-1, 0, 1, 2, 2, 2, 3, 4]
>>> bfs # bf_e: [2,1,...] --> [2,1,2,...]
[ContinuedFraction(LazyList([-1])), ContinuedFraction(LazyList([0])), ContinuedFraction(LazyList([1])), ContinuedFraction(LazyList([1, 2, 2, <...>])), ContinuedFraction(LazyList([1, 1, 1, 1, 1, 2])), ContinuedFraction(LazyList([1, 1, 1, 1, 1, 1, 1, 1, <...>])), ContinuedFraction(LazyList([2, 1, 2, <...>])), ContinuedFraction(LazyList([3, 7, <...>]))]
>>> [abs(bf) for bf in bfs]
[ContinuedFraction(LazyList([1])), ContinuedFraction(LazyList([0])), ContinuedFraction(LazyList([1])), ContinuedFraction(LazyList([1, 2, 2, <...>])), ContinuedFraction(LazyList([1, 1, 1, 1, 1, 2])), ContinuedFraction(LazyList([1, 1, 1, 1, 1, 1, 1, 1, <...>])), ContinuedFraction(LazyList([2, 1, 2, <...>])), ContinuedFraction(LazyList([3, 7, <...>]))]
>>> [+bf for bf in bfs]
[ContinuedFraction(LazyList([-1])), ContinuedFraction(LazyList([0])), ContinuedFraction(LazyList([1])), ContinuedFraction(LazyList([1, 2, 2, <...>])), ContinuedFraction(LazyList([1, 1, 1, 1, 1, 2])), ContinuedFraction(LazyList([1, 1, 1, 1, 1, 1, 1, 1, <...>])), ContinuedFraction(LazyList([2, 1, 2, <...>])), ContinuedFraction(LazyList([3, 7, <...>]))]
>>> [-bf for bf in bfs]
[ContinuedFraction(LazyList([1])), ContinuedFraction(LazyList([0])), ContinuedFraction(LazyList([-1])), ContinuedFraction(LazyList([-2, 1, 1, 2, <...>])), ContinuedFraction(LazyList([-2, 2, 1, 1, 2])), ContinuedFraction(LazyList([-2, 2, 1, 1, 1, 1, 1, <...>])), ContinuedFraction(LazyList([-3, 3, <...>])), ContinuedFraction(LazyList([-4, 1, 6, <...>]))]
>>> [bf.inv_() for bf in bfs if not bf == bf_0]
[ContinuedFraction(LazyList([-1])), ContinuedFraction(LazyList([0, 1])), ContinuedFraction(LazyList([0, 1, 2, 2, <...>])), ContinuedFraction(LazyList([0, 1, 1, 1, 1, 1, 2])), ContinuedFraction(LazyList([0, 1, 1, 1, 1, 1, 1, 1, 1, <...>])), ContinuedFraction(LazyList([0, 2, 1, 2, <...>])), ContinuedFraction(LazyList([0, 3, 7, <...>]))]
>>> bf_0.inv_()
ContinuedFraction(LazyList())

>>> fr_pi__apprx0_9 = [*islice(bf_pi__prefix2001.iter_approximate_fractions_(), 9)]
>>> fr_pi__apprx0_9
[Fraction(3, 1), Fraction(22, 7), Fraction(333, 106), Fraction(355, 113), Fraction(103993, 33102), Fraction(104348, 33215), Fraction(208341, 66317), Fraction(312689, 99532), Fraction(833719, 265381)]
>>> bf_355_over_113 = ContinuedFraction(Fraction(355, 113))
>>> bf_355_over_113.to_Fraction_or_dead_loop_()
Fraction(355, 113)
>>> bf_355_over_113
ContinuedFraction(LazyList([3, 7, 16]))
>>> bf_21_over_13
ContinuedFraction(LazyList([1, 1, 1, 1, 1, 2]))
>>> sum_ = bf_355_over_113 + bf_21_over_13
>>> product_ = bf_355_over_113 * bf_21_over_13
>>> sum_
ContinuedFraction(LazyList([<...>]))
>>> product_
ContinuedFraction(LazyList([<...>]))
>>> sum_.to_Fraction_or_dead_loop_()
Fraction(6988, 1469)
>>> product_.to_Fraction_or_dead_loop_()
Fraction(7455, 1469)
>>> sum_
ContinuedFraction(LazyList([4, 1, 3, 8, 1, 2, 2, 2, 2]))
>>> product_
ContinuedFraction(LazyList([5, 13, 2, 1, 4, 1, 1, 3]))
>>> bf_355_over_113.to_Fraction_or_dead_loop_() + bf_21_over_13.to_Fraction_or_dead_loop_()
Fraction(6988, 1469)
>>> bf_355_over_113.to_Fraction_or_dead_loop_() * bf_21_over_13.to_Fraction_or_dead_loop_()
Fraction(7455, 1469)


>>> diff_ = bf_355_over_113 - bf_21_over_13
>>> ratio_ = bf_355_over_113 / bf_21_over_13
>>> rem_ = bf_355_over_113 % bf_21_over_13
>>> quo_ = bf_355_over_113 // bf_21_over_13
>>> diff_
ContinuedFraction(LazyList([<...>]))
>>> ratio_
ContinuedFraction(LazyList([<...>]))
>>> rem_
ContinuedFraction(LazyList([<...>]))
>>> quo_
1
>>> diff_.to_Fraction_or_dead_loop_()
Fraction(2242, 1469)
>>> ratio_.to_Fraction_or_dead_loop_()
Fraction(4615, 2373)
>>> rem_.to_Fraction_or_dead_loop_()
Fraction(2242, 1469)
>>> diff_
ContinuedFraction(LazyList([1, 1, 1, 9, 25, 1, 2]))
>>> ratio_
ContinuedFraction(LazyList([1, 1, 17, 8, 1, 2, 1, 3]))
>>> rem_
ContinuedFraction(LazyList([1, 1, 1, 9, 25, 1, 2]))
>>> bf_355_over_113.to_Fraction_or_dead_loop_() - bf_21_over_13.to_Fraction_or_dead_loop_()
Fraction(2242, 1469)
>>> bf_355_over_113.to_Fraction_or_dead_loop_() / bf_21_over_13.to_Fraction_or_dead_loop_()
Fraction(4615, 2373)
>>> bf_355_over_113.to_Fraction_or_dead_loop_() % bf_21_over_13.to_Fraction_or_dead_loop_()
Fraction(2242, 1469)
>>> bf_355_over_113.to_Fraction_or_dead_loop_() // bf_21_over_13.to_Fraction_or_dead_loop_()
1

>>> (quo_, rem_) == divmod(bf_355_over_113, bf_21_over_13)
True

#>>> for exp in range(-10, 11):(exp, pow(bf_21_over_13.to_Fraction_or_dead_loop_(), exp))
>>> for exp in range(-10, 11):(exp, pow(bf_21_over_13, exp).to_Fraction_or_dead_loop_())
(-10, Fraction(137858491849, 16679880978201))
(-9, Fraction(10604499373, 794280046581))
(-8, Fraction(815730721, 37822859361))
(-7, Fraction(62748517, 1801088541))
(-6, Fraction(4826809, 85766121))
(-5, Fraction(371293, 4084101))
(-4, Fraction(28561, 194481))
(-3, Fraction(2197, 9261))
(-2, Fraction(169, 441))
(-1, Fraction(13, 21))
(0, Fraction(1, 1))
(1, Fraction(21, 13))
(2, Fraction(441, 169))
(3, Fraction(9261, 2197))
(4, Fraction(194481, 28561))
(5, Fraction(4084101, 371293))
(6, Fraction(85766121, 4826809))
(7, Fraction(1801088541, 62748517))
(8, Fraction(37822859361, 815730721))
(9, Fraction(794280046581, 10604499373))
(10, Fraction(16679880978201, 137858491849))

#>>> all(pow(bf_21_over_13, exp).to_Fraction_or_dead_loop_() == pow(bf_21_over_13.to_Fraction_or_dead_loop_(), exp) for exp in range(-40, 41))
>>> all(pow(bf_21_over_13, exp).to_Fraction_or_dead_loop_() == pow(bf_21_over_13.to_Fraction_or_dead_loop_(), exp) for exp in range(-10, 11))
True

doctest____end:here




#]]]'''
__all__ = r'''
    FloatNumberError__div0



    bf_to_signed_uint_exp_repr_
        bf_to_bin_float_repr_
        bf_to_hex_float_repr_


    mk_binary_float_digits5signed_uint_exp_repr_
        mk_binary_float_digits5float_
    mk_binary_float_digits5int_
        iter_binary_float_digits5int_
            gde2_

    positive_bf_digits2flatten_
        positive_bf_digits5flatten_

    bf_std_
        bf_eq_zero_
        bf_sign_of_
        bf_cmp_zero_
        bf_lt_zero_
        bf_is_neg_

    bf_cmp_
        bf_ge_
        bf_le_
        bf_gt_
        bf_lt_
        bf_ne_
        bf_eq_

    bf_neg
    bf_rshift_
    bf_lshift_

    bf_add__p_p
    bf_sub__p_p
        bf_add
            bf_sub
        bf_truediv__p_p
            bf_truediv
                bf_inv
                    bf_mul
                        bf_divmod
    bf_floor_ex_
        bf_is_int_
        bf_is_power_of_2_
        bf_floor_
        bf_ceil_

    BinaryFloat
        bf_0
        bf_1
        bf_neg1
'''.split()#'''
    #ZeroDivisionError = FloatNumberError__div0
    #chain__strict_
    #chain__lazy_
    #bf_unpack_or_raise
    #_old_ver_______bf_add__p_p
    #_truediv_bits__p_p__output_leading0s__input_aligned_
    #_sub_bits__p_gt_p__output_leading0s__input_aligned_
    #_add_bits__p_p__output_carry_bit__input_aligned_
    #
__all__
from math import floor
from itertools import repeat
from fractions import Fraction


from seed.math.PowSeq import PowSeq
from seed.math.divs import is_even


from seed.tiny import print_err
from seed.tiny import check_type_is
from seed.tiny_.check import check_pair, check_uint_lt, check_int_ge, check_int_ge_le # , check_int_ge_lt
from seed.tiny import is_iterator, is_iterable
from seed.types.LazySeq import LazySeq
from seed.types.LazyList import decorator4protocol4ToConcatLazyList_, ToConcatLazyList
from seed.types.LazyList import LazyList, LazyListError
from seed.types.LazyList import null_lazylist


#from seed.math.continued_fraction.continued_fraction_fold import ContinuedFractionError__inf__no_cf0
from seed.math.continued_fraction.continued_fraction_ops____using_LazyList import ContinuedFraction


from seed.math.binary_float.FloatNumberError import FloatNumberError
#class FloatNumberError(Exception):pass
from seed.math.binary_float.py_float_repr import float2signed_uint_exp_repr_, hex_float_repr5bin_
from seed.math.binary_float.py_float_repr import hex_float_repr__pos0, bin_float_repr__pos0, hex_float_repr__neg0, bin_float_repr__neg0
from seed.math.binary_float.py_float_repr import check_hex_float_repr, check_bin_float_repr
    #check_hex_mantissa,
    #heck_bin_mantissa,

from seed.math.binary_float.py_float_repr import (
check_signed_uint_exp_repr
,   signed_uint_exp_repr2bin_float_repr_
,   signed_uint_exp_repr5bin_float_repr_
,   signed_uint_exp_repr2hex_float_repr_
,   signed_uint_exp_repr5hex_float_repr_
#
,signed_uint_exp_repr__pos0
,signed_uint_exp_repr__neg0
,   hex_float_repr__pos0
,   hex_float_repr__neg0
#
,   bin_float_repr__pos0
,   bin_float_repr__neg0
#
,check_pint8bits
,   pint8bits2bin_mantissa_
,   pint8bits5bin_mantissa_
,   pint8bits2hex_mantissa_
,   pint8bits5hex_mantissa_
,       hex_mantissa5bin_
,       hex_mantissa2bin_
#
,signed_uint_exp_repr__pos0
,signed_uint_exp_repr__neg0
,   hex_float_repr__pos0
,   hex_float_repr__neg0
#
,   bin_float_repr__pos0
,   bin_float_repr__neg0
)





__all__

'bf_digits :: LazyList<int>{empty/0 or (fst (sign/(-1|+1), exp4msb/int); msb must be 1 and omitted; others (0|1)); allow tailing 0s since islice()}'
'bits :: LazyList<(0|1)>'
'flatten_bf_digits :: LazyList<int>{nonempty/positive_real_only (fst max_exp4msb; msb maybe 0, cannot omit; others (0|1))}'

chain__strict_ = LazyList.concat_initial_seq_
chain__lazy_ = LazyList.concat_initial_iterator_

class FloatNumberError__div0(FloatNumberError):pass
ZeroDivisionError = FloatNumberError__div0

def gde2_(n, /):
    check_type_is(int, n)
    if n == 0: raise ValueError('gde2_(0) == +oo')
    s = bin(n)
    i = s.rindex('1')
    gde2 = len(s) -i-1
    assert gde2 >= 0
    n_ = n >> gde2
        # [@k. [-1 >> k === -1]]
    assert n_&1 #odd
    assert n == n_ << gde2
    return gde2


    #def iter__le(sf, may_max_sz, /, *, relax, to_iter_pairs=False):
def bf_to_signed_uint_exp_repr_(may_max_sz, bf_digits, /, *, relax=False):
    signed_uint_exp_repr = _bf_to_signed_uint_exp_repr_(relax, may_max_sz, bf_digits)
    check_signed_uint_exp_repr(signed_uint_exp_repr)
    return signed_uint_exp_repr
def _bf_to_signed_uint_exp_repr_(relax, may_max_sz, bf_digits, /):
    (sign0, exp4msb, mantissa_bits) = bf_std_(bf_digits)
    if sign0 == 0:
        return signed_uint_exp_repr__pos0
    sign = sign0

    bin_mantissa = ''.join(map(str, mantissa_bits.iter__le(may_max_sz, relax=relax)))
    if '1' in bin_mantissa:
        #removr tailing_0s
        i = bin_mantissa.rindex('1')
        bin_mantissa = bin_mantissa[:i+1]
    else:
        bin_mantissa = '0'
    bin_mantissa
    pint8bits = pint8bits5bin_mantissa_(bin_mantissa)
    return (sign, pint8bits, exp4msb)


def bf_to_bin_float_repr_(may_max_sz, bf_digits, /, *, relax=False):
    return signed_uint_exp_repr2bin_float_repr_(bf_to_signed_uint_exp_repr_(may_max_sz, bf_digits, relax=relax))

def bf_to_hex_float_repr_(may_max_sz, bf_digits, /, *, relax=False):
    return signed_uint_exp_repr2hex_float_repr_(bf_to_signed_uint_exp_repr_(may_max_sz, bf_digits, relax=relax))



def mk_binary_float_digits5float_(real, /):
    return mk_binary_float_digits5signed_uint_exp_repr_(float2signed_uint_exp_repr_(real))
def mk_binary_float_digits5signed_uint_exp_repr_(signed_uint_exp_repr, /):
    check_signed_uint_exp_repr(signed_uint_exp_repr)
    (sign, uint8bits, exp4msb) = signed_uint_exp_repr
    if uint8bits == 0:
        # sign may be -1 !!
        return _bf_0
    pint8bits = uint8bits
    assert pint8bits & 1
    bin_mantissa = pint8bits2bin_mantissa_(pint8bits)
    mantissa_bits = LazyList(map(int, bin_mantissa))
    bf_digits = chain__strict_([(sign, exp4msb)], mantissa_bits)

    return bf_digits

def mk_binary_float_digits5int_(n, /):
    return LazyList(iter_binary_float_digits5int_(n))
def iter_binary_float_digits5int_(n, /):
    'n/int -> (null_iter if n==0 else (sign, exp4msb):Iter (0|1))'
    check_type_is(int, n)
    if n == 0:
        return
    if n < 0:
        sign = -1
        n = -n
    else:
        sign = +1

    s = bin(n)
    assert s[:3] == '0b1'
    exp4msb = len(s) -3
    bf0 = (sign, exp4msb)
    yield bf0
    i = s.rindex('1')
    #gde2 = len(s) -i-1
    yield from map(int, s[3:i+1])

def _check_bf0(bf0, /):
    check_pair(bf0)
    (sign, exp4msb) = bf0
    check_type_is(int, sign)
    check_type_is(int, exp4msb)
    if not abs(sign) == 1: raise TypeError

r'''[[[
def iter_binary_float_digits5ND_(N, D, /):
    check_type_is(int, N)
    check_type_is(int, D)
    if D == 0:
        raise FloatNumberError__div0
    # (N,D) = Fraction(N,D).as_integer_ratio()
    if N == 0:
        return
    gde2_N = gde2_(N)
    gde2_D = gde2_(D)
    gde2 = min(gde2_N, gde2_D)
    if gde2:
        N >>= gde2
        D >>= gde2
        gde2_N -= gde2
        gde2_D -= gde2
    if gde2_D:

    while N&1 == 0 == D&1:
#]]]'''#'''
__all__



def positive_bf_digits2flatten_(exp4msb__OUT, exp4msb__IN, mantissa_bits__IN, /, *, without_exp4msb=False):
    #mantissa_bits === _1_bf_digits
    #if not exp4msb__IN <= exp4msb__OUT: raise TypeError
    check_type_is(int, exp4msb__IN)
    check_int_ge(exp4msb__IN, exp4msb__OUT)
    whole_bits = chain__strict_([1], mantissa_bits__IN)
    aligned_whole_bits__OUT = chain__lazy_(repeat(0, exp4msb__OUT -exp4msb__IN), whole_bits)
        # pad leading 0s
    if without_exp4msb:
        return aligned_whole_bits__OUT
    flatten_bf_digits__OUT = chain__strict_([exp4msb__OUT], aligned_whole_bits__OUT)
    return flatten_bf_digits__OUT
def positive_bf_digits5flatten_(flatten_bf_digits, /, *, to_neg=False):
    exp4msb__OUT, aligned_whole_bits__OUT = flatten_bf_digits.unpack_or_raise()
    1;      flatten_bf_digits = None
    bits = aligned_whole_bits__OUT
    1;      aligned_whole_bits__OUT = None
    num_0s = 0
    while 1:
        msb, bits = bits.unpack_or_raise()
            # "positive" must contain bit '1'
        if msb == 1:
            break
        num_0s += 1
    mantissa_bits__IN = bits
    exp4msb__IN = exp4msb__OUT -num_0s
    sign = -1 if to_neg else +1
    bf_digits = chain__strict_([(sign, exp4msb__IN)], mantissa_bits__IN)
    return bf_digits

def __():
    def bf_unpack_or_raise(bf_digits, /):
        'bf_digits :: LazyList<int>{fst int; others pint}'
        m = bf_digits.may_unpack()
        if m is None:
            raise FloatNumberError__div0
        return m


def bf_std_(bf_digits, /):
    '-> (sign0, exp4msb, _1_bf_digits)'
    m = bf_digits.may_unpack()
    if m is None:
        (sign0, exp4msb) = (0, 0)
        _1_bf_digits = bf_digits
    else:
        bf0, _1_bf_digits = m
        (sign, exp4msb) = bf0
        sign0 = sign
    return (sign0, exp4msb, _1_bf_digits)

def bf_eq_zero_(bf_digits, /):
    return bf_digits.is_empty__hardwork()
def bf_sign_of_(bf_digitsL, /):
    (sign0L, exp4msbL, _1_bf_digitsL) = bf_std_(bf_digitsL)
    return sign0L
bf_cmp_zero_ = bf_sign_of_
def bf_lt_zero_(bf_digitsL, /):
    return bf_cmp_zero_(bf_digitsL) == -1
bf_is_neg_ = bf_lt_zero_



def bf_ge_(lhs, rhs, /):
    return not bf_lt_(lhs, rhs)
def bf_le_(lhs, rhs, /):
    return not bf_gt_(lhs, rhs)
def bf_gt_(lhs, rhs, /):
    return bf_lt_(rhs, lhs)
def bf_lt_(lhs, rhs, /):
    return bf_cmp_(lhs, rhs, detect_lt_or_gt_only=-1) == -1
def _result_with_flip_(to_flip, r, /):
    return -r if to_flip else r
def bf_cmp_(lhs, rhs, /, *, detect_lt_or_gt_only):
    '[detect_lt_or_gt_only <- {-1,0,+1}]; -1: detect_lt_only, result +2 repr (0|+1); +1: detect_gt_only, result -2 repr (0|+1); 0: normal cmp'
    '-> [-1,0,+1]'
    return _bf_cmp_(False, lhs, rhs, detect_lt_or_gt_only=detect_lt_or_gt_only)
#def _bf_cmp_(to_flip, bf_digitsL, bf_digitsR, /, *, detect_lt_only):
def _bf_cmp_(to_flip, bf_digitsL, bf_digitsR, /, *, detect_lt_or_gt_only):
    '[detect_lt_or_gt_only <- {-1,0,+1}]; -1: detect_lt_only, result +2 repr (0|+1); +1: detect_gt_only, result -2 repr (0|+1); 0: normal cmp'
    (sign0L, exp4msbL, _1_bf_digitsL) = bf_std_(bf_digitsL)
    (sign0R, exp4msbR, _1_bf_digitsR) = bf_std_(bf_digitsR)
    if not sign0L == sign0R:
        r = -1 if sign0L < sign0R else +1
        return _result_with_flip_(to_flip, r)

    if sign0R == 0:
        return 0
    if sign0R < 0:
        to_flip = not to_flip
    if not exp4msbL == exp4msbR:
        r = -1 if exp4msbL < exp4msbR else +1
        return _result_with_flip_(to_flip, r)
    r'''[[[
    if detect_lt_only:
        detect_lt_or_gt_only = -1 if not to_flip else +1
    else:
        detect_lt_or_gt_only = 0
    #]]]'''#'''
    if to_flip:
        detect_lt_or_gt_only = -detect_lt_or_gt_only
    r = _bf_cmp__p_p(_1_bf_digitsL, _1_bf_digitsR, detect_lt_or_gt_only=detect_lt_or_gt_only)
    return _result_with_flip_(to_flip, r)

def _bf_eq0__p(bits, /):
    return not any(bits)
def _bf_cmp__p_p(bitsL, bitsR, /, *, detect_lt_or_gt_only):
    '[detect_lt_or_gt_only <- {-1,0,+1}]; -1: detect_lt_only, result +2 repr (0|+1); +1: detect_gt_only, result -2 repr (0|+1); 0: normal cmp'
    #used in:bf_cmp_/_bf_cmp_
    #used in:_truediv_bits__p_p__output_leading0s__input_aligned_
    check_int_ge_le(-1,+1, detect_lt_or_gt_only)
    while 1:
        nullL = bitsL.is_empty__hardwork()
        nullR = bitsR.is_empty__hardwork()
        if nullL and nullR:
            return 0 # eq
        elif nullL and not nullR:
            # 0, -1
            # not +1
            if detect_lt_or_gt_only == +1:
                return -2
            if _bf_eq0__p(bitsR):
                return 0 # eq
            # [0 < not 0]
            return -1
        elif not nullL and nullR:
            # 0, +1
            # not -1
            if detect_lt_or_gt_only == -1:
                return +2
            if _bf_eq0__p(bitsL):
                return 0 # eq
            # [not 0 > 0]
            return +1
        # [nonempty bitsL, bitsR]
        bf0L, bitsL = bitsL.may_unpack()
        bf0R, bitsR = bitsR.may_unpack()
        if not bf0L == bf0R:
            return -1 if bf0L < bf0R else +1
        #continue
def bf_ne_(lhs, rhs, /):
    return not bf_eq_(lhs, rhs)
def bf_eq_(lhs, rhs, /):
    return bf_cmp_(lhs, rhs, detect_lt_or_gt_only=0) == 0



_bf_1 = mk_binary_float_digits5int_(1)
_bf_0 = null_lazylist
def bf_inv(bf_digits, /):
    return bf_truediv(_bf_1, bf_digits)
def bf_neg(bf_digits, /):
    (sign0, exp4msb, _1_bf_digits) = bf_std_(bf_digits)
    if sign0 == 0:
        # [-0 == 0]
        return bf_digits
    sign = sign0
    sign = -sign
    return chain__strict_([(sign, exp4msb)], _1_bf_digits)
def bf_rshift_(k, bf_digits, /):
    return bf_lshift_(-k, bf_digits)
def bf_lshift_(k, bf_digits, /):
    check_type_is(int, k)
    (sign0, exp4msb, _1_bf_digits) = bf_std_(bf_digits)
    if sign0 == 0:
        zero = bf_digits
        return zero
    sign = sign0
    exp4msb += k
    return chain__strict_([(sign, exp4msb)], _1_bf_digits)



bf_mul__use__bf_truediv = True
def bf_mul(lhs, rhs, /):
    if bf_eq_zero_(rhs):
        return _bf_0
    if bf_eq_zero_(lhs):
        return _bf_0
    if bf_is_power_of_2_(lhs, neg_ok=True):
        lhs, rhs = rhs, lhs
    if bf_is_power_of_2_(rhs, neg_ok=True):
        (sign0, exp4msb, mantissa_bits) = bf_std_(rhs)
        r = bf_lshift_(exp4msb, lhs)
        if sign0 == -1:
            r = bf_neg(r)
        return r
    if bf_mul__use__bf_truediv:
        _bf_mul = _bf_mul__using_truediv
    else:
        _bf_mul = _bf_mul__plain
    return _bf_mul(lhs, rhs)

def _bf_mul__using_truediv(lhs, rhs, /):
    'input non-zero&&non-power-of-2'
    return bf_truediv(lhs, bf_inv(rhs))
def bf_sub(lhs, rhs, /):
    return bf_add(lhs, bf_neg(rhs))
def bf_add(lhs, rhs, /):
    (sign0L, exp4msbL, _1_bf_digitsL) = bf_std_(lhs)
    (sign0R, exp4msbR, _1_bf_digitsR) = bf_std_(rhs)
    if sign0R == 0:
        return lhs
    if sign0L == 0:
        return rhs
    if sign0L > 0 and sign0R > 0:
        return bf_add__p_p(exp4msbL, _1_bf_digitsL, exp4msbR, _1_bf_digitsR)
    if sign0L > 0 and sign0R < 0:
        return bf_sub__p_p(exp4msbL, _1_bf_digitsL, exp4msbR, _1_bf_digitsR)
    if sign0L < 0 and sign0R > 0:
        return bf_neg(bf_sub__p_p(exp4msbL, _1_bf_digitsL, exp4msbR, _1_bf_digitsR))
    if sign0L < 0 and sign0R < 0:
        return bf_neg(bf_add__p_p(exp4msbL, _1_bf_digitsL, exp4msbR, _1_bf_digitsR))

@decorator4protocol4ToConcatLazyList_
def _add_bits__p_p__output_carry_bit__input_aligned_(bitsL, bitsR, /):
    'should output carry bit (0|1);  input aligned'
    #see:_sub_bits__p_gt_p__output_leading0s__input_aligned_
    # L: _ ???
    # R: _ ???
    # O: ? ???
    num_1s = 0 # after carry bit
    # L: _ ppp ???
    # R: _ qqq ???
    # O: ? ??? ???
    while 1:
        nullL = bitsL.is_empty__hardwork()
        nullR = bitsR.is_empty__hardwork()
        if nullL or nullR:
            carry = 0
            yield carry
            yield from repeat(1, num_1s)
            if not nullR:
                # L: _ ppp <eof>
                # R: _ qqq ddd
                # O: 0 111 ddd
                raise ToConcatLazyList(bitsR)
            elif not nullL:
                # L: _ ppp ddd
                # R: _ qqq <eof>
                # O: 0 111 ddd
                raise ToConcatLazyList(bitsL)
            else:
                # L: _ ppp <eof>
                # R: _ qqq <eof>
                # O: 0 111 <eof>
                return
        # [nonempty bitsL, bitsR]
        bf0L, bitsL = bitsL.may_unpack()
        bf0R, bitsR = bitsR.may_unpack()
        if not bf0L == bf0R:
            # L: _ ppp p??
            # R: _ qqq q??
            # O: ? ??? ???
            num_1s += 1
            # L: _ ppp ???
            # R: _ qqq ???
            # O: ? ??? ???
            continue
        # [bf0L == bf0R]
        if bf0R == 1:
            # L: _ ppp 1??
            # R: _ qqq 1??
            # O: 1 000 ???
            carry = 1
            yield carry
            yield from repeat(0, num_1s)
            # L: _ ???
            # R: _ ???
            # O: ? ???
        else:
            # L: _ ppp 0??
            # R: _ qqq 0??
            # O: 0 111 ???
            carry = 0
            yield carry
            yield from repeat(1, num_1s)
            # L: _ ???
            # R: _ ???
            # O: ? ???
        # L: _ ???
        # R: _ ???
        # O: ? ???
        num_1s = 0
        # L: _ ppp ???
        # R: _ qqq ???
        # O: ? ??? ???
    return
##xxx @decorator4protocol4ToConcatLazyList_
def bf_add__p_p(exp4msbL, _1_bf_digitsL, exp4msbR, _1_bf_digitsR, /):
    #see:bf_sub__p_p
    #see:_old_ver_______bf_add__p_p
    exp4msb__OUT = max(exp4msbL, exp4msbR)
    aligned_bitsL = positive_bf_digits2flatten_(exp4msb__OUT, exp4msbL, _1_bf_digitsL, without_exp4msb=True)
    aligned_bitsR = positive_bf_digits2flatten_(exp4msb__OUT, exp4msbR, _1_bf_digitsR, without_exp4msb=True)
    aligned_whole_bits__OUT = _add_bits__p_p__output_carry_bit__input_aligned_(aligned_bitsL, aligned_bitsR)
    flatten_bf_digits__OUT = chain__strict_([1+exp4msb__OUT], aligned_whole_bits__OUT)
        # 『1+』to contains carry bit (which may be 0)
    bf_digits = positive_bf_digits5flatten_(flatten_bf_digits__OUT)
    return bf_digits

    #old-ver:
@decorator4protocol4ToConcatLazyList_
def _old_ver_______bf_add__p_p(exp4msbL, _1_bf_digitsL, exp4msbR, _1_bf_digitsR, /):
    if exp4msbR == exp4msbL:
        yield (+1, exp4msbR+1)
        raise ToConcatLazyList(_add_bits__p_p__output_carry_bit__input_aligned_(_1_bf_digitsL, _1_bf_digitsR))
    if exp4msbR < exp4msbL:
        #swap
        exp4msbL, _1_bf_digitsL, exp4msbR, _1_bf_digitsR = exp4msbR, _1_bf_digitsR, exp4msbL, _1_bf_digitsL
    # [exp4msbL < exp4msbR]
    max_sz = exp4msbR -exp4msbL -1
    (num_1s, bitsR) = _search_next_0_(max_sz, _1_bf_digitsR)
    1;  _1_bf_digitsR = None #free memory
    # R: 1_ 1{num_1s}  ++ bitsR
    #   * R: 1_ 1{num_1s==max_sz}  ++ bitsR[?, ...]
    #   * R: 1_ 1{num_1s <max_sz}  ++ bitsR[0, ...]
    if num_1s == max_sz:
        # L:                        1_ ++ _1_bf_digitsL
        # R: 1_ 1{max_sz}  ++ bitsR[?, ...]

        carry, tail = _add_bits__p_p__output_carry_bit__input_aligned_(chain__strict_([1],_1_bf_digitsL), bitsR).unpack_or_raise()
        if carry:
            # L+R: 1_ 0{max_sz+1}  ++ push_carry_fwd((1:_1_bf_digitsL)+bitsR)
            yield (+1, exp4msbR+1)
            yield from repeat(0, max_sz+1)
        else:
            # L+R: 1_ 1{max_sz}  ++ push_carry_fwd((1:_1_bf_digitsL)+bitsR)
            yield (+1, exp4msbR)
            yield from repeat(1, max_sz)
        raise ToConcatLazyList(tail)
    assert num_1s < max_sz
        # L:                       1_ ++ _1_bf_digitsL
        # R: 1_ 1...1 ++ bitsR[0,?..?,...]
        #
        # R: 1_ 1{num_1s <=max_sz-2}  ++ bitsR[0, ...]
    yield (+1, exp4msbR)
    yield from repeat(1, num_1s)
    exp4headR = exp4msbR -1-num_1s
    1;      exp4msbR = None
    # !! [max_sz := exp4msbR -exp4msbL -1]
    # !! [num_1s < max_sz]
    # [exp4headR > exp4msbL]
    # carry bit has been outputted for bitsR
    assert exp4headR >= exp4msbL
    ###
    exp4msbL, _1_bf_digitsL, exp4headR, bitsR # no carry bit since:
    #assert bitsR.extract_head_or_raise() == 0
    #assert bitsR.extract_prefix__le(1, relax=True) == (0,)
    while 1:
        # [exp4msbL < exp4headR]
        #assert bitsR.extract_prefix__le(1, relax=True) == (0,)
        bitsR = bitsR.get_tail_or_raise()
            # carry waiting
        exp4headR -= 1
        # [exp4msbL <= exp4headR]
        max_sz = exp4headR -exp4msbL
        if max_sz == 0:
            num_1s = 0
        else:
            (num_1s, bitsR) = _search_next_0_(max_sz, bitsR)
        if num_1s == max_sz:
            # L:                    1_ ++ _1_bf_digitsL
            # R: 0// 1...1 ++ bitsR[?,...]
            #
            # R: 0// 1{num_1s==max_sz}  ++ bitsR[?, ...]
            carry, tail = _add_bits__p_p__output_carry_bit__input_aligned_(chain__strict_([1],_1_bf_digitsL), bitsR).unpack_or_raise()
            if carry:
                # L+R: 1 0{max_sz}  ++ push_carry_fwd((1:_1_bf_digitsL)+bitsR)
                yield 1
                yield from repeat(0, max_sz)
            else:
                # L+R: 0 1{max_sz}  ++ push_carry_fwd((1:_1_bf_digitsL)+bitsR)
                yield 0
                yield from repeat(1, max_sz)
            raise ToConcatLazyList(tail)
        assert num_1s < max_sz
            # L:                         1_ ++ _1_bf_digitsL
            # R: 0// 1...1 ++ bitsR[0,..,?,...]
            #
        # !! [max_sz := exp4headR -exp4msbL]
        # !! [num_1s < max_sz]
        exp4headR -= num_1s
        # [exp4msbL < exp4headR]
        yield 0
        yield from repeat(1, num_1s)
        #assert bitsR.extract_prefix__le(1, relax=True) == (0,)
    return
def _search_next_0_(may_max_sz, bits, /):
    #used in:_old_ver_______bf_add__p_p
    (num_1s, bits) = _search_next_0_ex_(0, may_max_sz, bits)
    return (num_1s, bits)
def _search_next_1_(may_max_sz, bits, /):
    #used in:_truediv_bits__p_p__output_leading0s__input_aligned_
    (num_0s, bits) = _search_next_0_ex_(1, may_max_sz, bits)
    return (num_0s, bits)
def _search_next_0_ex_(_0, may_max_sz, bits, /):
    ps = bits.iter__le(may_max_sz, relax=False, to_iter_pairs=True)
    num_1s = -1
    for num_1s, (_01, _1_bits) in enumerate(ps):
        if _01 == _0:
            break
        bits = _1_bits
    else:
        num_1s += 1
    num_1s, bits
    assert num_1s == may_max_sz or bits.extract_prefix__le(1, relax=True) == (_0,)
    return (num_1s, bits)



def bf_sub__p_p(exp4msbL, _1_bf_digitsL, exp4msbR, _1_bf_digitsR, /):
    #see:bf_add__p_p
    bf_digitsL = chain__strict_([(+1, exp4msbL)], _1_bf_digitsL)
    bf_digitsR = chain__strict_([(+1, exp4msbR)], _1_bf_digitsR)
    r = bf_cmp_(bf_digitsL, bf_digitsR, detect_lt_or_gt_only=0)
    if r == 0:
        # eq
        return _bf_0
    if r == -1:
        #swap
        # [lhs < rhs]
        exp4msbL, _1_bf_digitsL, exp4msbR, _1_bf_digitsR = exp4msbR, _1_bf_digitsR, exp4msbL, _1_bf_digitsL
        # [lhs > rhs]
    elif r == +1:
        # [lhs > rhs]
        pass
    else:
        raise logic-err
    # [lhs > rhs]

    bf_digits = _bf_sub__p_gt_p(exp4msbL, _1_bf_digitsL, exp4msbR, _1_bf_digitsR, to_neg=(r == -1))
    return bf_digits
def _bf_sub__p_gt_p(exp4msbL, _1_bf_digitsL, exp4msbR, _1_bf_digitsR, /, *, to_neg):
    # [lhs > rhs]
    assert exp4msbL >= exp4msbR
    exp4msb__OUT = exp4msbL
    aligned_bitsL = positive_bf_digits2flatten_(exp4msb__OUT, exp4msbL, _1_bf_digitsL, without_exp4msb=True)
    aligned_bitsR = positive_bf_digits2flatten_(exp4msb__OUT, exp4msbR, _1_bf_digitsR, without_exp4msb=True)
    aligned_whole_bits__OUT = _sub_bits__p_gt_p__output_leading0s__input_aligned_(aligned_bitsL, aligned_bitsR)
    flatten_bf_digits__OUT = chain__strict_([exp4msb__OUT], aligned_whole_bits__OUT)
    bf_digits = positive_bf_digits5flatten_(flatten_bf_digits__OUT, to_neg=to_neg)
    return bf_digits
@decorator4protocol4ToConcatLazyList_
def _sub_bits__p_gt_p__output_leading0s__input_aligned_(bitsL, bitsR, /):
    'should output all leading 0s generated by subtract; [lhs > rhs];  input aligned'
    '-> aligned_whole_bits__OUT'
    #see:_add_bits__p_p__output_carry_bit__input_aligned_
    #################################
    #################################
    ##### output_leading_0s__until_NOT_EQ_BIT #####
    ##### loop4output_diff__between_NOT_EQ_BIT #####
    ##### loop4output_flip__before_MAYBE_LAST_1_at_bitsR__after_bitsL_empty #####
    ##### output_diff_on_LAST_1_at_bitsR__after_bitsL_empty #####
    #################################
    #################################

    #print_err(_sub_bits__p_gt_p__output_leading0s__input_aligned_)
    #assert bitsL.extract_head_or_raise() == 1
    ##### output_leading_0s__until_NOT_EQ_BIT #####
    while 1:
        # prev prefixes are eq
            # L: bbb !
            # R: bbb !
            # O: 000 !  # leading 0s
        nullL = bitsL.is_empty__hardwork()
        nullR = bitsR.is_empty__hardwork()
        #print_err(bitsL, bitsR)
        if nullL or nullR:
            raise logic-err-'p gt p'
        # [nonempty bitsL, bitsR]
        bf0L, bitsL = bitsL.may_unpack()
        bf0R, bitsR = bitsR.may_unpack()
        if not bf0L == bf0R:
            if not bf0L == 1:
                raise logic-err-'p gt p'
            # L: bbb ! 1
            # R: bbb ! 0
            # O: 000 ! ? # leading 0s
            # [bf0L == 1][bf0R == 0]
            # NOT_EQ_BIT
            # L: 1
            # R: 0
            # O: ?
            break
        else:
            # L: bbb ! b
            # R: bbb ! b
            # O: 000 ! 0  # leading 0s
            yield 0 # leading 0
            # L: bbb !
            # R: bbb !
            # O: 000 !  # leading 0s
    #end-while
    # NOT_EQ_BIT
    # L: 1
    # R: 0
    # O: ?

    ##### loop4output_diff__between_NOT_EQ_BIT #####
    num_EQs = 0 # after NOT-EQ bit
        # NOT_EQ_BIT
        # L: 1 bbb
        # R: 0 bbb
        # O: ? ???
    while 1:
        nullL = bitsL.is_empty__hardwork()
        nullR = bitsR.is_empty__hardwork()
        #print_err(bitsL, bitsR)
        if nullR:
            # L: 1 bbb ddd
            # R: 0 bbb <eof>
            # O: 1 000 ddd
            NOT_EQ_BIT = 1
            yield NOT_EQ_BIT
            yield from repeat(0, num_EQs)
            # L: ddd
            # O: ddd
            raise ToConcatLazyList(bitsL)
        if nullL:
            # L: 1 bbb <eof>
            # R: 0 bbb ddd
            if _bf_eq0__p(bitsR):
                # L: 1 bbb <eof>
                # R: 0 bbb 000 <eof>
                # O: 1 <eof>
                NOT_EQ_BIT = 1
                yield NOT_EQ_BIT
                return
            #borrow
            # L: 1 bbb <eof>
            # R: 0 bbb ppp 100 <eof>
            # O: 0 111 qqq 1 <eof>
            NOT_EQ_BIT = 0
            yield NOT_EQ_BIT
            yield from repeat(1, num_EQs)
            # [empty bitsL][nonempty bitsR]
            # R: ppp 100 <eof>
            # O: qqq 1 <eof>
            bitsR
            break
        # [nonempty bitsL, bitsR]
        bf0L, bitsL = bitsL.unpack_or_raise()
        bf0R, bitsR = bitsR.unpack_or_raise()
        if bf0L == bf0R:
            # L: 1 bbb b
            # R: 0 bbb b
            num_EQs += 1
            continue
        # [bf0L =!= bf0R]
        if bf0L == 1:
            # [bf0L == 1][bf0R == 0]
            # L: 1 bbb 1
            # R: 0 bbb 0
            # O: 1 000 ?
            NOT_EQ_BIT = 1
            yield NOT_EQ_BIT
            yield from repeat(0, num_EQs)
            # L: 1
            # R: 0
            # O: ?
        else:
            # [bf0L == 0][bf0R == 1]
            # borrow
            # L: 1 bbb 0
            # R: 0 bbb 1
            # O: 0 111 ?
            NOT_EQ_BIT = 0
            yield NOT_EQ_BIT
            yield from repeat(1, num_EQs)
            # L: 1
            # R: 0
            # O: ?
        # L: 1
        # R: 0
        # O: ?
        # new NOT_EQ_BIT here
        num_EQs = 0
    #end-while
    # [empty bitsL][nonempty bitsR]
    # R: ppp 100 <eof>
    # O: qqq 1 <eof>

    ##### loop4output_flip__before_MAYBE_LAST_1_at_bitsR__after_bitsL_empty #####
    bitsR
    # R: 00(1 ppp)? 100 <eof>
    # O: 11(0 qqq)? 1 <eof>
    while 1:
        # !! [bitsR contains '1']
        bf0R, bitsR = bitsR.unpack_or_raise()
        #print_err(bitsL, bitsR)
        if bf0R == 1:
            # new MAYBE_LAST_1
            break
        # [bf0R == 0]
        yield 1 # flip 0/bf0R
    # R: (1 ppp)? 100 <eof>
    # O: (0 qqq)? 1 <eof>
    num_0s = 0
    # R: (100 ppp)? 100 <eof>
    # O: (011 qqq)? 1 <eof>
    while not bitsR.is_empty__hardwork():
        #print_err(bitsL, bitsR)
        # R: (100 ppp)? 100 <eof>
        # O: (011 qqq)? 1 <eof>
        bf0R, bitsR = bitsR.unpack_or_raise()
        if bf0R == 1:
            # new MAYBE_LAST_1
            # R: 100 (1 ppp)? 100 <eof>
            # O: 011 (0 qqq)? 1 <eof>
            yield 0
                # flip prev MAYBE_LAST_1
            yield from repeat(1, num_0s)
                # flip 0s following prev MAYBE_LAST_1
            # R: (1 ppp)? 100 <eof>
            # O: (0 qqq)? 1 <eof>
            num_0s = 0
            # R: (100 ppp)? 100 <eof>
            # O: (011 qqq)? 1 <eof>
        else:
            # R: (100 0pp)? 100 <eof>
            # O: (011 1qq)? 1 <eof>
            num_0s += 1
            # R: (100 ppp)? 100 <eof>
            # O: (011 qqq)? 1 <eof>
        # R: (100 ppp)? 100 <eof>
        # O: (011 qqq)? 1 <eof>
    #end-while
    # R: 100 <eof>
    # O: 1 <eof>
    ##### output_diff_on_LAST_1_at_bitsR__after_bitsL_empty #####
    yield 1
    return

def bf_truediv(lhs, rhs, /):
    #if bf_eq_zero_(rhs): raise ZeroDivisionError
    #if bf_is_neg_(lhs):
    if bf_is_power_of_2_(rhs, neg_ok=True):
        (sign0, exp4msb, mantissa_bits) = bf_std_(rhs)
        #bug:r = bf_lshift_(exp4msb, lhs)
        r = bf_lshift_(-exp4msb, lhs)
        if sign0 == -1:
            r = bf_neg(r)
        return r

    (sign0L, exp4msbL, _1_bf_digitsL) = bf_std_(lhs)
    (sign0R, exp4msbR, _1_bf_digitsR) = bf_std_(rhs)
    if sign0R == 0:
        # [rhs == 0]
        # [lhs/0 --> ^ZeroDivisionError]
        raise ZeroDivisionError
    # [rhs =!= 0]
    if sign0L == 0:
        # [rhs =!= 0]
        # [0/rhs == 0]
        return lhs
    # [lhs =!= 0][rhs =!= 0]
    bf_digits = bf_truediv__p_p(exp4msbL, _1_bf_digitsL, exp4msbR, _1_bf_digitsR)
    if not sign0L == sign0R:
        bf_digits = bf_neg(bf_digits)
    return bf_digits


def bf_truediv__p_p(exp4msbL, _1_bf_digitsL, exp4msbR, _1_bf_digitsR, /):
    # chain__strict_([1], L/R)
    aligned_bitsL = positive_bf_digits2flatten_(exp4msbL, exp4msbL, _1_bf_digitsL, without_exp4msb=True)
    aligned_bitsR = positive_bf_digits2flatten_(exp4msbR, exp4msbR, _1_bf_digitsR, without_exp4msb=True)


    aligned_whole_bits__OUT = _truediv_bits__p_p__output_leading0s__input_aligned_(aligned_bitsL, aligned_bitsR)
    exp4msb__OUT = exp4msbL -exp4msbR
    flatten_bf_digits__OUT = chain__strict_([exp4msb__OUT], aligned_whole_bits__OUT)
    bf_digits = positive_bf_digits5flatten_(flatten_bf_digits__OUT)
    return bf_digits

@decorator4protocol4ToConcatLazyList_
def _truediv_bits__p_p__output_leading0s__input_aligned_(bitsL, bitsR, /):
    'should output all leading 0s (at most 1) generated by try-div;  input aligned'
    '-> aligned_whole_bits__OUT'
    #see:_sub_bits__p_gt_p__output_leading0s__input_aligned_
    #see:_bf_cmp__p_p
    assert bitsL.extract_head_or_raise() == 1
    assert bitsR.extract_head_or_raise() == 1
    rshifted_bitR = chain__strict_([0], bitsR)
    aligned = True
    while 1:
        # [bitsL.head == '1']
        # [bitsR.head == '1']
        # [rshifted_bitR.head == '0']
        #bug: LT = -1 == _bf_cmp__p_p(bitsL, bitsR, detect_lt_or_gt_only=-1)
        #   since below require p_gt_p
        if not aligned:
            # L: 1   xxx
            # R: _   1 yyy
            # Q: 0 ! 1 zzz
            # [L < R]
            r_cmp = -1
            #yield 0
                #the quo bit has been yielded
            yield 1
            # L: 1 xxx
            # R: _ 1 yyy
            # Q: 0 1 ! zzz
            bitsD = rshifted_bitR
            # [D < L < R]

            # L: 1 xxx
            # D: 0 1 yyy
            # Q: 0 1 ! zzz
            # [L > D]
            # [p_gt_p]
        else:
            # L: 1 xxx
            # R: 1 yyy
            # [L <?> R]
            r_cmp = _bf_cmp__p_p(bitsL, bitsR, detect_lt_or_gt_only=0)

            if r_cmp == 0:
                #EQ
                # [L == R]
                # L: 1 xxx <eof>
                # R: 1 xxx <eof>
                # Q: 1 <eof>
                yield 1
                return
            LT = r_cmp == -1
            if LT:
                #LT
                # [L < R]
                # L: 1 xxx
                # R: _ 1 yyy
                # Q: 0 1 zzz
                yield 0
                aligned = False
                # L: 1   xxx
                # R: _   1 yyy
                # Q: 0 ! 1 zzz
                # [L < R]
                continue
            else:
                #GT
                # [L > R]
                # L: 1 xxx
                # R: 1 yyy
                # Q: 1 zzz
                yield 1
                # L: 1   xxx
                # R: 1   yyy
                # Q: 1 ! zzz
                bitsD = bitsR
                # L: 1   xxx
                # D: 1   yyy
                # Q: 1 ! zzz
                # [L > D]
                # [p_gt_p]
            # [L > D]
            # [p_gt_p]
        # [L > D]
        # [p_gt_p]

        if not aligned:
            # L: 1 xxx
            # D: 0 1 yyy
            # Q: 0 1 ! zzz
            # [L > D]
            pass
        else:
            #GT
            # L: 1   xxx
            # D: 1   yyy
            # Q: 1 ! zzz
            # [L > D]
            pass
        # [L > D]
        # [p_gt_p]
        #print_err(_truediv_bits__p_p__output_leading0s__input_aligned_, bitsL)
        bitsL = _sub_bits__p_gt_p__output_leading0s__input_aligned_(bitsL, bitsD)
        # [L > 0]
        (num_0s, bitsL) = _search_next_1_(None, bitsL)
        assert bitsL.extract_head_or_raise() == 1
        # [bitsL.head == '1']
        if not num_0s > 0:
            raise logic-err
        if not aligned:
            # [old_L > D]
            # old_L: 1 xxx
            # D: 0 1 yyy
            # Q: 0 1 ! zzz
            # L: 0 0{num_0s-1} 1 uuu
            # [L > 0]
            if num_0s == 1:
                # L: 0 1 uuu
                # !! [old_L < R]
                # [L == old_L*2-R < R]
                # [L < R]
                # Q: 0 1 ! zzz
                # L: 0 1   uuu
                # R: _ _   1 yyy
                #xxx yield 0 # output 1 already
                aligned = False
                # L: 1   uuu
                # R: _   1 yyy
                # Q: 1 ! 1 zzz
                # [L < R]
                continue
            else:
                # L: 0 0   0{num_0s-2} 1 uuu
                # Q: 0 1 ! 0{num_0s-2} vvv
                yield from repeat(0, num_0s -2)
                aligned = True
                # L: 0 0 0{num_0s-2}   1 uuu
                # Q: 0 1 0{num_0s-2} ! vvv
        else:
            #GT
            # [old_L > D]
            # old_L: 1   xxx
            # D: 1   yyy
            # Q: 1 ! zzz
            # L: 0 0{num_0s-1} 1 uuu
            # [L > D]

            # L: 0   0{num_0s-1} 1 uuu
            # Q: 1 ! 0{num_0s-1} vvv
            yield from repeat(0, num_0s -1)
            aligned = True
            # L: 0 0 0{num_0s-1}   1 uuu
            # Q: 0 1 0{num_0s-1} ! vvv


        # [bitsL.head == '1']
    return


bf_lshift_
bf_rshift_
bf_sign_of_
bf_add
bf_sub
bf_truediv
bf_add__p_p
bf_sub__p_p
bf_truediv__p_p

def bf_is_power_of_2_(bf_digits, /, *, neg_ok):
    if not neg_ok:
        if bf_is_neg_(bf_digits):
            return False
    _le2 = bf_digits.extract_prefix__le(2, relax=False)
    only_msb = len(_le2) == 1
    return only_msb
def bf_is_int_(bf_digits, /):
    (is_int, the_floor, bf_digits4mantissa) = bf_floor_ex_(bf_digits)
    return is_int
def bf_floor_(bf_digits, /):
    (is_int, the_floor, bf_digits4mantissa) = bf_floor_ex_(bf_digits)
    return the_floor
def bf_ceil_(bf_digits, /):
    (is_int, the_floor, bf_digits4mantissa) = bf_floor_ex_(bf_digits)
    return the_floor if is_int else the_floor+1
def bf_floor_ex_(bf_digits, /):
    '-> (is_int, the_floor, bf_digits4mantissa)'
    #(sign0, exp4msb, _1_bf_digits) = bf_std_(bf_digits)
    (sign0, exp4msb, mantissa_bits) = bf_std_(bf_digits)
    if sign0 == 0:
        zero = bf_digits
        is_int = True
        the_floor = 0
        bf_digits4mantissa = zero
    elif exp4msb < 0:
        is_int = False
        the_floor = 0
        bf_digits4mantissa = bf_digits
    else:
        prefix, mantissa_bits = mantissa_bits.extract_prefix_with_tail__le(exp4msb, relax=False)
        bits4floor__without_tailing_0s = (1, *prefix)#(, *repeat(0, exp4msb-len(prefix)))
        num_tailing_0s = exp4msb -len(prefix)
            # tuple<(0|1)>    not    LazyList<(0|1)>
        1;      prefix = None
        is_int = _bf_eq0__p(mantissa_bits)
            #   non-std form from slice may cause last item be 0 / tailing_0s
        the_floor = int(''.join(map(str, bits4floor__without_tailing_0s)), 2) << num_tailing_0s
        zero = _bf_0 #null_lazylist
        bf_digits4mantissa = zero if is_int else positive_bf_digits5flatten_(chain__strict_([-1], mantissa_bits))
    if sign0 == -1:
        if is_int:
            bf_digits4mantissa # zero ok
            the_floor = -the_floor
        else:
            bf_digits4mantissa = bf_sub(_bf_1, bf_digits4mantissa)
            the_floor = -1-the_floor
    return (is_int, the_floor, bf_digits4mantissa)




def bf_divmod(lhs, rhs, /):
    (is_int, the_floor, bf_digits4mantissa) = bf_floor_ex_(bf_truediv(lhs, rhs))
    iq = the_floor
    r = bf_mul(bf_digits4mantissa, rhs)
    return (iq,r)

    #old:
    iq = bf_floor_(bf_truediv(lhs, rhs))
        #useless:(is_int, the_floor, bf_digits4mantissa) = bf_floor_ex_(bf_digits)
    bf8q = mk_binary_float_digits5int_(iq)
    r = bf_sub(lhs, bf_mul(bf8q, rhs))
    return (iq,r)


def _bf_mul__plain(lhs, rhs, /):
    'input non-zero&&non-power-of-2'
    #see:bf_truediv__p_p
    (sign0L, exp4msbL, _1_bf_digitsL) = bf_std_(lhs)
    (sign0R, exp4msbR, _1_bf_digitsR) = bf_std_(rhs)
    assert sign0L
    assert sign0R
    sign = sign0L * sign0R
    exp4msb__OUT = 1+exp4msbL+exp4msbR
        # "1+" for carry bit (0|1)

    # chain__strict_([1], L/R)
    aligned_bitsL = positive_bf_digits2flatten_(exp4msbL, exp4msbL, _1_bf_digitsL, without_exp4msb=True)
    aligned_bitsR = positive_bf_digits2flatten_(exp4msbR, exp4msbR, _1_bf_digitsR, without_exp4msb=True)


    aligned_whole_bits__OUT = _mul_bits__p_p__output_carry_bit__input_aligned_(aligned_bitsL, aligned_bitsR)
    flatten_bf_digits__OUT = chain__strict_([exp4msb__OUT], aligned_whole_bits__OUT)
    bf_digits = positive_bf_digits5flatten_(flatten_bf_digits__OUT, to_neg=(sign==-1))
    return bf_digits


def _mul_bits__p_p__output_carry_bit__input_aligned_(bitsL, bitsR, /):
    'as if [1 <= (1.xxx * 1.yyy) < 4] so carry bit (0|1)'
    #see:_add_bits__p_p__output_carry_bit__input_aligned_
    #see:_sub_bits__p_gt_p__output_leading0s__input_aligned_
    r'''[[[
    x = 1.11111... = 2
    x*x =:
        % 11111....
        %  11111....
        %   11111....
        %    11111....
        %     11111....
        %      11111....
        %       ...
        %       ...
        =:
        % 12345...
        = 1*2**0 + 2*2**-1 + 3*2**-2 + ...
        = sum~ (i+1)*2**-i ~{i :<- [0..]}
        = 2*2
        = 4
    [sum_tail_(k) =[def]= sum~ (i+1)*2**-i ~{i :<- [k..]}]
    [sum_tail_(0) == 4]
    [sum_tail_(k)
    == sum~ (i+1)*2**-i ~{i :<- [k..]}
    == sum~ ((i+k)+1)*2**-(i+k) ~{i :<- [0..]}
    == 2**-k * sum~ ((i+1)+k)*2**-i ~{i :<- [0..]}
    == 2**-k * (sum_tail_(0) + k * sum~ 2**-i ~{i :<- [0..]})
    == 2**-k * (4 + k * 2)
    == (k+2)*2**(1-k)
    ]
    #[[begin-verify: diff and at0
    [sum_tail_(k) == (k+2)*2**(1-k)]
    [sum_tail_(k) - sum_tail_(k+1)
    !! sum_tail_.def
    == (k+1)*2**-k
    ]
    [sum_tail_(k) - sum_tail_(k+1)
    !! [sum_tail_(k) == (k+2)*2**(1-k)]
    == (k+2)*2**(1-k) - ((k+1)+2)*2**(1-(k+1))
    == (2*k+4)*2**-k - (k+3)*2**-k
    == (k+1)*2**-k
    #ok
    ]
    [sum_tail_(0)
    !! [sum_tail_(k) == (k+2)*2**(1-k)]
    == (0+2)*2**(1-0)
    == 4
    #ok
    ]
    #]]end-verify: diff and at0

    #########################
    [sum_tail_(k) =[def]= sum~ (i+1)*2**-i ~{i :<- [k..]}]
    [sum_tail_(k) == (k+2)*2**(1-k)]
    #########################
    [sum_tail_(0) == 4]     # 2/(1/2)
    [sum_tail_(1) == 3]     # 3/1
    [sum_tail_(2) == 2]     # 4/2
    [sum_tail_(3) == 5/4]   # 5/4
    [sum_tail_(4) == 3/4]   # 6/8

    #]]]'''#'''
    _iter4mul(bitsL, bitsR)

def _iter4mul(bitsL, bitsR, /):
    '-> Iter (pint, ...) #to be sum/flatten to binary'
    assert bitsL.extract_prefix__le(1, relax=False) == (1,)
    assert bitsR.extract_prefix__le(1, relax=False) == (1,)
    num_1sL = 0
    num_1sR = 0
    lsL = []
    lsR = []
        #=> should use BinaryFloat(which is LazySeq)
        #   i.e. mul should def directly by BinaryFloat
    while 1:
        nullL = bitsL.is_empty__hardwork()
        nullR = bitsR.is_empty__hardwork()
        #print_err(bitsL, bitsR)
        if nullL or nullR:
            if nullL:
            . todo
            raise logic-err-'p gt p'
        # [nonempty bitsL, bitsR]
        bf0L, bitsL = bitsL.may_unpack()
        bf0R, bitsR = bitsR.may_unpack()
        num_1sL += bf0L
        num_1sR += bf0R

        lsL.append(bf0L)
        lsR.append(bf0R)
        # [len(lsL) == len(lsR)]
        u = sum(map(int.__mul__, lsL, reversed(lsR)))
        yield (u, num_1sL, num_1sR, len(lsL))


r'''[[[
TODO:
def pow__bf__int_(bf_digits, e, /):
    bin
bf_log_(lhs, rhs, /):
#]]]'''#'''

__all__


def _iter_continued_fraction_digits5bf_(sf, /):
    if sf == 0:
        yield 0     # [cf0 :: int]
        return
    # [sf =!= 0]
    if 1:
        #i = floor(sf)
        (is_int, i, mantissa4sf) = sf.floor_ex_()
        1;      sf = None
        # [i <= sf < i+1]
        # [0 <= mantissa4sf < 1]
        yield i     # [cf0 :: int]
    # [i <= sf < i+1]
    # [0 <= mantissa4sf < 1]
    while 1:
        # [i <= sf < i+1]
        # [0 <= mantissa4sf < 1]
        #sf -= i
        sf = mantissa4sf
        1;      mantissa4sf = None
        # [0 <= sf < 1]
        if is_int:
        #if sf == 0:
            assert sf == 0
            break
        # [0 < sf < 1]
        sf = sf.inv_()
        # [1 < sf]
        #i = floor(sf)
        (is_int, i, mantissa4sf) = sf.floor_ex_()
        1;      sf = None
        # [1 <= i <= sf < i+1]
        # [0 <= mantissa4sf < 1]
        yield i     # >= 1
        # [i <= sf < i+1]
        # [0 <= mantissa4sf < 1]
    return
class BinaryFloat(LazySeq):
    r'''[[[
    __bool__ is forbidden
        sf == bf_0
        len(sf.the_lazylist) > 0
    __len__ is forbidden
    __contains__ is forbidden


    bf([])
        === 0
    bf([bf0; tail0...])
        [bf0 :: (sign/(-1|+1), exp4msb/int)]
        [tail0 :: [(0|1)]]


    #]]]'''#'''
    @property
    def _bf_digits(sf, /):
        return sf.the_lazylist
    def __new__(cls, bf_digits__or__int__or__Fraction, /):
        if is_iterable(bf_digits__or__int__or__Fraction):
            bf_digits = bf_digits__or__int__or__Fraction
        elif type(bf_digits__or__int__or__Fraction) is int:
            i = bf_digits__or__int__or__Fraction
            bf_digits = iter_binary_float_digits5int_(i)
        else:
            rational = bf_digits__or__int__or__Fraction
            fr = Fraction(rational)
            #bf_digits = iter_binary_float_digits5ND_(*fr.as_integer_ratio())
            N, D = fr.as_integer_ratio()
            if D == 1:
                sf = cls(N)
            else:
                sf = cls(N)/cls(D)
            bf_digits = sf
        bf_digits

        if isinstance(bf_digits, __class__):
            sf = bf_digits
        else:
            sf = super(__class__, cls).__new__(cls, bf_digits)
        return sf
    if 0:
        #@override
        def _check_on_no_more_extend_(sf, _init_seq, _tails, /):
            super()._check_on_no_more_extend_(_init_seq, _tails)
            #ok: == 0

    #@override
    def _check_post__extend_more_(sf, _init_seq, begin4init_seq, _tails, begin4tails, /):
        super()._check_post__extend_more_(_init_seq, begin4init_seq, _tails, begin4tails)
        for i, u in enumerate(_init_seq[begin4init_seq:], begin4init_seq):
            if i == 0:
                bf0 = u
                _check_bf0(bf0)
            else:
                check_uint_lt(2, u)

    def __iter__(sf, /):
        it = super(__class__, sf).__iter__()
        #it = iter(sf._bf_digits)
        del sf # to free memory as soon as possible: _bf_digits,_ls,_tmay_tail
        return __class__._iter(it)
    def _iter(it, /):
        'detect again besides ._check_on_no_more_extend_() since .__iter__() bypass .extend_more_()'
        if not is_iterator(it): raise logic-err
        for bf0 in it:
            break
        else:
            return
        _check_bf0(bf0)
        yield bf0
        del bf0
        if 0:
            yield from it
        else:
            for u in it:
                check_uint_lt(2, u)
                yield u

    def iter_continued_fraction_digits_(sf, /):
        return _iter_continued_fraction_digits5bf_(sf)
    def to_ContinuedFraction_(sf, /):
        return ContinuedFraction(sf.iter_continued_fraction_digits_())
    def iter_approximate_fractions_(sf, /):
        return sf.to_ContinuedFraction_().iter_approximate_fractions_()
    def is_int(sf, /):
        return bf_is_int_(sf._bf_digits)
    def floor_ex_(sf, /):
        '-> (is_int, the_floor, mantissa4sf)'
        (is_int, the_floor, bf_digits4mantissa) = bf_floor_ex_(sf._bf_digits)
        mantissa4sf = __class__(bf_digits4mantissa)
        return (is_int, the_floor, mantissa4sf)
    def __floor__(sf, /):
        return bf_floor_(sf._bf_digits)
    def __ceil__(sf, /):
        return bf_ceil_(sf._bf_digits)
    def _cmp_(sf, ot, /, *, detect_lt_or_gt_only):
        ot = __class__(ot)
        return bf_cmp_(sf._bf_digits, ot._bf_digits, detect_lt_or_gt_only=detect_lt_or_gt_only)
    def __eq__(sf, ot, /):
        return sf._cmp_(ot, detect_lt_or_gt_only=0) == 0
    def __lt__(sf, ot, /):
        return sf._cmp_(ot, detect_lt_or_gt_only=-1) == -1
    def __gt__(sf, ot, /):
        return sf._cmp_(ot, detect_lt_or_gt_only=+1) == +1

    def __ne__(sf, ot, /):
        return not sf == ot
    def __le__(sf, ot, /):
        return not sf > ot
    def __ge__(sf, ot, /):
        return not sf < ot

    def __abs__(sf, /):
        if sf < bf_0:
        #if bf_is_neg_(sf._bf_digits):
            return -sf
        return sf
    def __pos__(sf, /):
        return sf
    def __neg__(sf, /):
        return __class__(bf_neg(sf._bf_digits))
    def inv_(sf, /):
        return __class__(bf_inv(sf._bf_digits))
    def __add__(sf, ot, /):
        ot = __class__(ot)
        if ot == bf_0:
            return sf
        if sf == bf_0:
            return ot
        return __class__(bf_add(sf._bf_digits, ot._bf_digits))
    def __mul__(sf, ot, /):
        ot = __class__(ot)
        if ot == bf_1:
            return sf
        if sf == bf_1:
            return ot
        if sf == bf_0:
            return sf
        if ot == bf_0:
            return ot
        if ot == bf_neg1:
            return -sf
        if sf == bf_neg1:
            return -ot
        return __class__(bf_mul(sf._bf_digits, ot._bf_digits))

    def __sub__(sf, ot, /):
        ot = __class__(ot)
        if sf._bf_digits is ot._bf_digits:
            return bf_0
        return sf + (-ot)
    def __truediv__(sf, ot, /):
        ot = __class__(ot)
        if ot == bf_0:
            raise ZeroDivisionError
        if sf._bf_digits is ot._bf_digits:
            return bf_1
        #xxx return sf * ot.inv_()
        if sf == bf_0:
            return bf_0
        if ot == bf_1:
            return sf
        if ot == bf_neg1:
            return -sf
        if sf == bf_1:
            return ot.inv_()
        if sf == bf_neg1:
            return -ot.inv_()
        if ot.is_power_of_2_(neg_ok=True):
            (sign0, exp4msb, mantissa_bits) = bf_std_(ot._bf_digits)
            #bug:sf <<= exp4msb
            sf <<= -exp4msb
            if sign0 == -1:
                return -sf
            return sf
        return __class__(bf_truediv(sf._bf_digits, ot._bf_digits))
    def is_power_of_2_(sf, /, *, neg_ok):
        return bf_is_power_of_2_(sf._bf_digits, neg_ok=neg_ok)
    def __rshift__(sf, ot, /):
        check_type_is(int, ot)
        return sf << -ot
    def __lshift__(sf, ot, /):
        check_type_is(int, ot)
        k = ot
        if k == 0:
            return sf
        return __class__(bf_lshift_(k, sf._bf_digits))


    def __divmod__(sf, ot, /):
        ot = __class__(ot)
        if ot == bf_0:
            raise ZeroDivisionError
        if sf._bf_digits is ot._bf_digits:
            return (bf_1, bf_0)
        iq, r = bf_divmod(sf._bf_digits, ot._bf_digits)
        return iq, __class__(r)
    def __mod__(sf, ot, /):
        #ot = __class__(ot)
        iq, r = divmod(sf, ot)
        return r
    def __floordiv__(sf, ot, /):
        #ot = __class__(ot)
        iq, r = divmod(sf, ot)
        return iq
    def __pow__(sf, e, /):
        check_type_is(int, e)
        #return __class__(pow__bf__int_(sf, e))
        if sf.is_power_of_2_(neg_ok=True):
            if sf == bf_1:
                return sf
            if sf == bf_neg1:
                return bf_1 if is_even(e) else bf_neg1
            (sign0, exp4msb, mantissa_bits) = bf_std_(sf._bf_digits)
            exp4msb *= e
            sign = sign0
            if sign == -1:
                sign = +1 if is_even(e) else -1
            return __class__(chain__strict_([(sign, exp4msb)], null_lazylist))

        if sf == bf_0:
            if e == 0:
                return bf_1
                raise ZeroDivisionError('0**0')
            if e < 0:
                raise ZeroDivisionError('0**0')
            return sf
        if e == 2:
            return sf*sf

        if bf_mul__use__bf_truediv:
            inv_sf = sf.inv_()
        if e < 5:
            if e < 0:
                return (sf**(-e)).inv_()
            elif e < 2:
                if e == 0:
                    return bf_1
                elif e == 1:
                    return sf
                else:
                    raise 000
            elif e == 2:
                if bf_mul__use__bf_truediv:
                    return sf/inv_sf
                return sf*sf
            elif e == 3:
                if bf_mul__use__bf_truediv:
                    return sf/inv_sf/inv_sf
                return sf*sf*sf
            elif e == 4:
                sf_2 = (sf*sf)
                return sf_2*sf_2
            else:
                raise 000
        pows = PowSeq(sf, None, bf_1)
        return pows.get_pow_(e)


#end-class BinaryFloat:

bf_0 = BinaryFloat(0)
bf_1 = BinaryFloat(1)
bf_neg1 = BinaryFloat(-1)

def __():
    from seed.tiny import ifNonef, ifNone, echo
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.helper.repr_input import repr_helper

def __():
    from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
    from seed.helper.repr_input import repr_helper
    class _(ABC):
        __slots__ = ()
        raise NotImplementedError
        ___no_slots_ok___ = True
        def __repr__(sf, /):
            #return repr_helper(sf, *args, **kwargs)
            #return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
            ...
if __name__ == "__main__":
    pass
__all__


from seed.math.binary_float.binary_float_ops____using_LazyList import BinaryFloat
from seed.math.binary_float.binary_float_ops____using_LazyList import *
