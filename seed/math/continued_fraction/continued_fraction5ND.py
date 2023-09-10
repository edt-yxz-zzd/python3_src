#__all__:goto
r'''[[[
e ../../python3_src/seed/math/continued_fraction/continued_fraction5ND.py


seed.math.continued_fraction.continued_fraction5ND
py -m nn_ns.app.debug_cmd   seed.math.continued_fraction.continued_fraction5ND -x
py -m nn_ns.app.doctest_cmd seed.math.continued_fraction.continued_fraction5ND:__doc__ -ff -v
py_adhoc_call   seed.math.continued_fraction.continued_fraction5ND   @f


#]]]'''
__all__ = r'''
iter_continued_fraction_digits_ex5ND_
    continued_fraction_digits_ex5ND_
    iter_continued_fraction_digits5ND_



'''.split()#'''
__all__

from seed.tiny import check_type_is, fst
from seed.tiny_.check import check_uint, check_int_ge

def iter_continued_fraction_digits5ND_(N, D, /):
    '-> Iter cf_digit'
    check_int_ge(1, D)
    it = iter_continued_fraction_digits_ex5ND_(N, D)
    return map(fst, it)
def continued_fraction_digits_ex5ND_(N, D, /):
    '-> (cf_digits, gcd_of_ND)/([int;pint*], uint)'
    it = iter_continued_fraction_digits_ex5ND_(N, D)
    cf_digits = []
    try:
        while 1:
            (q, N, D) = next(it)
            cf_digits.append(q)
    except StopIteration as e:
        gcd_of_ND = e.value
        check_uint(gcd_of_ND)
    assert D == 0
    assert gcd_of_ND == abs(N)
    return (cf_digits, gcd_of_ND)

def iter_continued_fraction_digits_ex5ND_(N, D, /):
    '-> Iter (cf_digit, next_N, next_D) with StopIteration(gcd_of_ND)'
    check_type_is(int, N)
    check_type_is(int, D)
    while D:
        q,r = divmod(N, D)
        q # 0 if 0 <= N < D
        #yield q
        N, D = D, r
        yield q, N, D # (q, next_N, next_D)
    gcd_of_ND = abs(N)
    return gcd_of_ND



if __name__ == "__main__":
    pass
__all__

from seed.math.continued_fraction.continued_fraction5ND import iter_continued_fraction_digits_ex5ND_, continued_fraction_digits_ex5ND_, iter_continued_fraction_digits5ND_

from seed.math.continued_fraction.continued_fraction5ND import *
