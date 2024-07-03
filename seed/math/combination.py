#__all__:goto
r'''[[[
e ../../python3_src/seed/math/combination.py



seed.math.combination
py -m nn_ns.app.debug_cmd   seed.math.combination -x
py -m nn_ns.app.doctest_cmd seed.math.combination:__doc__
py_adhoc_call   seed.math.combination   @f

[[
===
py_help math > /sdcard/0my_files/tmp/out4py/py_help.math.out.txt
py_help itertools > /sdcard/0my_files/tmp/out4py/py_help.itertools.out.txt
py_help functools > /sdcard/0my_files/tmp/out4py/py_help.functools.out.txt
===
view /sdcard/0my_files/tmp/out4py/py_help.math.out.txt
view /sdcard/0my_files/tmp/out4py/py_help.itertools.out.txt
view /sdcard/0my_files/tmp/out4py/py_help.functools.out.txt

\<\(comb\|factorial\|perm\|prod\|combinations\|combinations_with_replacement\|permutations\|product\)\>

===
comb(n, k, /)
    Number of ways to choose k items from n items without repetition and without order.

    Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates to zero when k > n.

    Also called the binomial coefficient because it is equivalent to the coefficient of k-th term in polynomial expansion of the expression (1 + x)**n.

    Raises TypeError if either of the arguments are not integers.
    Raises ValueError if either of the arguments are negative.

factorial(x, /)
    Find x!.

    Raise a ValueError if x is negative or non-integral.

perm(n, k=None, /)
    Number of ways to choose k items from n items without repetition and with order.

    Evaluates to n! / (n - k)! when k <= n and evaluates to zero when k > n.

    If k is not specified or is None, then k defaults to n and the function returns n!.

    Raises TypeError if either of the arguments are not integers.
    Raises ValueError if either of the arguments are negative.

prod(iterable, /, *, start=1)
    Calculate the product of all the elements in the input iterable.

    The default start value for the product is 1.

    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may reject non-numeric types.

===
Combinatoric generators:
    product(p, q, ... [repeat=1]) --> cartesian product
    permutations(p[, r])
    combinations(p, r)
    combinations_with_replacement(p, r)

===
combinations(iterable, r)

    Return successive r-length combinations of elements in the iterable.

    combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)

combinations_with_replacement(iterable, r)

    Return successive r-length combinations of elements in the iterable allowing individual elements to have successive repeats.

    combinations_with_replacement('ABC', 2) --> ('A','A'), ('A','B'), ('A','C'), ('B','B'), ('B','C'), ('C','C')

permutations(iterable, r=None)

    Return successive r-length permutations of elements in the iterable.

    permutations(range(3), 2) --> (0,1), (0,2), (1,0), (1,2), (2,0), (2,1)

product(*iterables, repeat=1) --> product object

    Cartesian product of input iterables.
    Equivalent to nested for-loops.

    For example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).
    The leftmost iterators are in the outermost for-loop, so the output tuples cycle in a manner similar to an odometer (with the rightmost element changing on every iteration).

    To compute the product of an iterable with itself, specify the number of repetitions with the optional repeat keyword argument. For example, product(A, repeat=4) means the same as product(A, A, A, A).

    product('ab', range(3)) --> ('a',0) ('a',1) ('a',2) ('b',0) ('b',1) ('b',2)
    product((0,1), (0,1), (0,1)) --> (0,0,0) (0,0,1) (0,1,0) (0,1,1) (1,0,0) ...

===
reduce(function, iterable[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence or iterable, from left to right, so as to reduce the iterable to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).
    If initial is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty.

===
accumulate(iterable, func=None, *, initial=None)

    Return series of accumulated sums (or other binary function results).

===
]]

#]]]'''#'''
__all__ = r'''
comb
    C
    num_combinations_
    choose_
    binomial_coefficient_
    组合数扌
    二项式系数扌
perm
    P
    num_permutations_
    排列数扌
factorial
    阶乘扌
    置换数扌
prod
    foldl__mul_
    reduce__mul_
    II
    积扌
sum
    和扌
reduce
    泛累积扌
accumulate
    枚举冫前缀累计值扌

combinations
    枚举冫组合牜无重复扌
combinations_with_replacement
    枚举冫组合牜带重复扌
permutations
    枚举冫排列扌
product
    枚举冫正交外直积元组扌

iter_partitions_of_sum_
'''.split()#'''
__all__

from itertools import pairwise
from seed.tiny_.check import check_int_ge
######################
######################
######################

from itertools import accumulate
from functools import reduce
from math import comb, factorial, perm, prod
from itertools import combinations, combinations_with_replacement, permutations, product

P = perm
C = comb
choose_ = C
binomial_coefficient_ = C

num_permutations_ = P
num_combinations_ = C

foldl__mul_ = prod
reduce__mul_ = prod
II = prod

阶乘扌 = factorial
置换数扌 = factorial

排列数扌 = P
组合数扌 = C
二项式系数扌 = C

和扌 = sum = sum
积扌 = prod
枚举冫前缀累计值扌 = accumulate
泛累积扌 = reduce

枚举冫组合牜无重复扌 = combinations
枚举冫组合牜带重复扌 = combinations_with_replacement
枚举冫排列扌 = permutations
枚举冫正交外直积元组扌 = product
    #direct product:直积
    #exterior product:外积
    #outer product:外积
#枚举冫笛卡儿积扌 = product
    #Cartesian product:笛卡儿积

######################
##news:
######################
def iter_partitions_of_sum_(M, L, /):
    'M/the_sum/uint -> L/num_parts/pint -> parts/[uint] #[position matters] #used in: "(x+y+z)**n"'
    check_int_ge(0, M)
    check_int_ge(1, L)
    for js in combinations_with_replacement(range(1+M), L-1):
        js = (0, *js, M)
        ns = tuple(j-i for i,j in pairwise(js))
        assert len(ns) == L
        assert sum(ns) == M
        yield ns
枚举冫整数拆分牜位次相关扌=iter_partitions_of_sum_


__all__
######################
from seed.math.combination import P, C
from seed.math.combination import num_permutations_, num_combinations_
from seed.math.combination import 排列数扌, 组合数扌
from seed.math.combination import perm, comb


######################
from seed.math.combination import comb, C, num_combinations_, choose_, binomial_coefficient_,组合数扌,二项式系数扌
from seed.math.combination import perm, P, num_permutations_,排列数扌
from seed.math.combination import factorial,阶乘扌,置换数扌


######################
from seed.math.combination import prod, sum
from seed.math.combination import 积扌,和扌
from seed.math.combination import reduce, accumulate
from seed.math.combination import 泛累积扌,枚举冫前缀累计值扌

######################
from seed.math.combination import prod, foldl__mul_, reduce__mul_, II,积扌
from seed.math.combination import sum,和扌
from seed.math.combination import reduce,泛累积扌
from seed.math.combination import accumulate,枚举冫前缀累计值扌

######################
from seed.math.combination import combinations, combinations_with_replacement, permutations, product
from seed.math.combination import 枚举冫组合牜无重复扌,枚举冫组合牜带重复扌,枚举冫排列扌,枚举冫正交外直积元组扌
######################
from seed.math.combination import combinations,枚举冫组合牜无重复扌
from seed.math.combination import combinations_with_replacement,枚举冫组合牜带重复扌
from seed.math.combination import permutations,枚举冫排列扌
from seed.math.combination import product,枚举冫正交外直积元组扌
######################
from seed.math.combination import iter_partitions_of_sum_, 枚举冫整数拆分牜位次相关扌
######################
from seed.math.combination import *
