#__all__:goto
r'''[[[
e ../../python3_src/seed/math/primality_test/SPRP_2357.py

seed.math.primality_test.SPRP_2357
py -m nn_ns.app.debug_cmd   seed.math.primality_test.SPRP_2357 -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.primality_test.SPRP_2357:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/primality_test/reproduceable7probable_primes.py
]]


'#'; __doc__ = r'#'
>>> for n in range(-21, 22):print(n, detect_noncoprime_to_2357_(n), is_SPRP_2357_(n), sep=':')
-21:1:False
-20:1:False
-19:0:False
-18:1:False
-17:0:False
-16:1:False
-15:1:False
-14:1:False
-13:0:False
-12:1:False
-11:0:False
-10:1:False
-9:1:False
-8:1:False
-7:1:False
-6:1:False
-5:1:False
-4:1:False
-3:1:False
-2:1:False
-1:0:False
0:1:False
1:0:False
2:-1:True
3:-1:True
4:1:False
5:-1:True
6:1:False
7:-1:True
8:1:False
9:1:False
10:1:False
11:0:True
12:1:False
13:0:True
14:1:False
15:1:False
16:1:False
17:0:True
18:1:False
19:0:True
20:1:False
21:1:False

>>> [*filter4coprimes_to_2357_(range(-20, 200))]
[-19, -17, -13, -11, -1, 1, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 121, 127, 131, 137, 139, 143, 149, 151, 157, 163, 167, 169, 173, 179, 181, 187, 191, 193, 197, 199]
>>> [*filter4coprimes_to_2357_(range(-20, 200), neg_ok=False)]
[1, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 121, 127, 131, 137, 139, 143, 149, 151, 157, 163, 167, 169, 173, 179, 181, 187, 191, 193, 197, 199]
>>> [*filter4coprimes_to_2357_(range(-20, 200), in_2357_ok=True)]
[-19, -17, -13, -11, -1, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 121, 127, 131, 137, 139, 143, 149, 151, 157, 163, 167, 169, 173, 179, 181, 187, 191, 193, 197, 199]
>>> [*filter4coprimes_to_2357_(range(-20, 200), in_2357_ok=True, neg_ok=False)]
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 121, 127, 131, 137, 139, 143, 149, 151, 157, 163, 167, 169, 173, 179, 181, 187, 191, 193, 197, 199]

>>> _basis = (2,3,5,7)
>>> def show6diff_(n, /):
...     basis = _basis if n >= 9 else [base for base in _basis if base < n-1]
...     a = n == 2 or n > 2 and 1 == n&1 and is_strong_probable_prime__basis_(basis, n)
...     b = is_SPRP_2357_(n)
...     if not a is b:
...         print(n, a, b, sep=':')

>>> for n in range(-30, 3000):show6diff_(n)
>>> for n in range(2047-50, 2047+50):show6diff_(n)
>>> for n in range(1373653-50, 1373653+50):show6diff_(n)
>>> for n in range(25326001-50, 25326001+50):show6diff_(n)
>>> for n in range(3215031751-50, 3215031751+50):show6diff_(n)

>>> [*filter_SPRP_2357_(range(-200, 1+200))]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
>>> [*filter_SPRP_2357_(range(2047-50, 2047+50))]
[1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089]
>>> [*filter_SPRP_2357_(range(1373653-50, 1373653+50))]
[1373611, 1373627, 1373639, 1373677, 1373683, 1373689]
>>> [*filter_SPRP_2357_(range(25326001-50, 25326001+50))]
[25325969, 25325981, 25326023, 25326047]
>>> [*filter_SPRP_2357_(range(3215031751-50, 3215031751+50))]
[3215031733, 3215031749, 3215031751, 3215031767, 3215031773, 3215031791]




>>> next(iter_xprimes7SPRP_2357__ge_lt_(reverse=True))
Traceback (most recent call last):
    ...
TypeError: [reverse:=True][may_max1_u:=None]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(), 0, 20)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(-20), 0, 20)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+20), 0, 20)]
[23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+2, None), 0, 20)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+2, 2), 0, 20)]
[]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+2, 3), 0, 20)]
[2]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+2, 4), 0, 20)]
[2, 3]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+2, 5), 0, 20)]
[2, 3]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+2, 6), 0, 20)]
[2, 3, 5]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+3, 6), 0, 20)]
[3, 5]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+3, 6, reverse=True), 0, 20)]
[5, 3]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+2, 6, reverse=True), 0, 20)]
[5, 3, 2]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+1, 30), 0, 20)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+2, 30), 0, 20)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+3, 30), 0, 20)]
[3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> [*islice(iter_xprimes7SPRP_2357__ge_lt_(+4, 30), 0, 20)]
[5, 7, 11, 13, 17, 19, 23, 29]








next_SPRP_2357__ge_
prev_may_SPRP_2357__lt_
>>> next_SPRP_2357__ge_(-3)
2
>>> next_SPRP_2357__ge_(1)
2
>>> next_SPRP_2357__ge_(2)
2
>>> next_SPRP_2357__ge_(3)
3
>>> next_SPRP_2357__ge_(4)
5
>>> next_SPRP_2357__ge_(5)
5

>>> prev_may_SPRP_2357__lt_(-3)
>>> prev_may_SPRP_2357__lt_(1)
>>> prev_may_SPRP_2357__lt_(2)
>>> prev_may_SPRP_2357__lt_(3)
2
>>> prev_may_SPRP_2357__lt_(4)
3
>>> prev_may_SPRP_2357__lt_(5)
3
>>> prev_may_SPRP_2357__lt_(6)
5
>>> prev_may_SPRP_2357__lt_(7)
5
>>> prev_may_SPRP_2357__lt_(8)
7
















py_adhoc_call   seed.math.primality_test.SPRP_2357   @f
]]]'''#'''
__all__ = r'''
is_SPRP_2357_
    filter_SPRP_2357_
        iter_xprimes7SPRP_2357__ge_lt_
            next_SPRP_2357__ge_
            prev_may_SPRP_2357__lt_
detect_noncoprime_to_2357_
    filter4coprimes_to_2357_






II_2357
bs_2357
II_357
bs_357
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.primality_test.strong_probable_prime import is_strong_probable_prime__basis_
    from seed.tiny_.check import check_type_is, check_int_ge
    from itertools import count, islice
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

#A014233_7fst_four = (2047, 1373653, 25326001, 3215031751)
II_2357 = 210 # == 2*3*5*7
bs_2357 = b'\2\3\5\7'
II_357 = 105 # == 3*5*7
bs_357 = b'\3\5\7'
def detect_noncoprime_to_2357_(n, /):
    'int -> (-1/in_2357|0/coprime|+1/noncoprime)'
    #assert n >= 0
    if n&1 == 0:
        return -1 if n == 2 else +1
    u = n % II_357
    if u in bs_357:
        return -1 if n == u else +1
    return +1 if any(u%d == 0 for d in bs_357) else 0

    #.u = n % II_2357
    #.if u in bs_2357:
    #.    return -1 if n == u else +1
    #.return +1 if any(u%d == 0 for d in bs_2357) else 0

def filter4coprimes_to_2357_(ns, /, in_2357_ok=False, neg_ok=True):
    for n in ns:
        match detect_noncoprime_to_2357_(n):
            case 0:
                # coprime
                if neg_ok or n > 0:
                    yield n
            case 1:
                # noncoprime and not in_2357
                pass
            case -1:
                # in_2357
                if in_2357_ok:
                    yield n
                pass
            case _:
                raise 000

def filter_SPRP_2357_(ns, /):
    'Iter int -> Iter uint{is_SPRP_2357_}'
    return filter(is_SPRP_2357_, ns)
def is_SPRP_2357_(n, /):
    'n/int -> bool{== [n>=2][[is_prime_(n)]or[1==gcd(n,210)][7 < n-1][is_strong_probable_prime__basis_([2,3,5,7],n)]]}'
    if 1:
        'int -> bool'
        check_type_is(int, n)
        if n < 2:
            return False
        # [2 <= n]
    else:
        'pint -> bool'
        check_int_ge(1, n)
        # [1 <= n]
    # [1 <= n]
    ######################
    match detect_noncoprime_to_2357_(n):
        case 0:
            # coprime
            # [1 == gcd(n, 210)]
            pass
        case 1:
            # noncoprime and not in_2357
            return False
        case -1:
            # in_2357
            # [is_prime_(n)]
            return True
        case _:
            raise 000
    # [1 <= n]
    # [1 == gcd(n, 210)]
    ######################
    if n < 121:
        # [1 <= n < 11**2]
        # [1 <= sqrt(n) < 11]
        # [[is_composite_(n)] -> [min_prime_factor{n} <= 7]]
        # !! [1 == gcd(n, 210)]
        # [not$is_composite_(n)]
        # [[n==1]or[is_prime_(n)]]
        # [[n=!=1] -> [is_prime_(n)]]
        return not n == 1
    # [121 <= n]
    # [1 == gcd(n, 210)]
    ######################
    # [n%2 =!= 0]
    # [n%3 =!= 0]
    # [n%5 =!= 0]
    # [n%7 =!= 0]
    # [max(bs_2357) == 7 < n-1]
    # ==>> precondition{is_strong_probable_prime__basis_}
    ######################
    #A014233_7fst_three = (2047, 1373653, 25326001)
    if n < 1373653:
        if n < 2047:
            basis = b'\2'
        else:
            basis = b'\2\3'
    else:
        if n < 25326001:
            basis = b'\2\3\5'
        else:
            basis = b'\2\3\5\7'
    basis
    ######################
    return is_strong_probable_prime__basis_(basis, n)
    ######################

def iter_xprimes7SPRP_2357__ge_lt_(min_u=2, may_max1_u=None, /, *, reverse=False):
    check_type_is(int, min_u)
    min_u = max(2, min_u)
    #bug:odd_min_u = max(3, min_u)
    odd_min_u = 1|min_u
    match may_max1_u:
        case None:
            # +oo
            odd_us = count(odd_min_u, 2)
            if reverse:raise TypeError('[reverse:=True][may_max1_u:=None]')
            # [[reverse] -> [odd_us :: reversed]]
            pass
        case int(max1_u):
            #check_type_is(int, max1_u)
            #max1_u = max(min_u, max1_u)
            #max1_u = max(2, max1_u)
            if not min_u < max1_u: return
            # [min_u < max1_u]
            777;may_max1_u = max1_u
            odd_us = range(odd_min_u, max1_u, 2)
            if reverse:
                odd_us = odd_us[::-1]
            # [[reverse] -> [odd_us :: reversed]]
            pass
        case _:
            raise TypeError(may_max1_u)
    # [[reverse] -> [odd_us :: reversed]]
    # [[not None is may_max1_u] -> [min_u < max1_u]]
    even_ps = (2,) if min_u == 2 else ()
    odd_sprps = filter_SPRP_2357_(odd_us)
    # [[reverse] -> [odd_sprps :: reversed]]
    if reverse:
        # [odd_sprps :: reversed]
        yield from odd_sprps
        yield from even_ps
    else:
        yield from even_ps
        yield from odd_sprps

def next_SPRP_2357__ge_(min_u, /):
    #vs:next_probable_prime__ge_
    check_type_is(int, min_u)
    if min_u < 3:
        return 2
    odd_min_u = 1|min_u
    odd_us = count(odd_min_u, 2)
    return next(filter_SPRP_2357_(odd_us))
def prev_may_SPRP_2357__lt_(max1_u, /):
    #vs:prev_may_probable_prime__lt_
    check_type_is(int, max1_u)
    if max1_u <= 3:
        return 2 if 2 < max1_u else None
    # [3 < max1_u]
    odd_us = range(3, max1_u, 2)[::-1]
    return next(filter_SPRP_2357_(odd_us))

__all__
from seed.math.primality_test.SPRP_2357 import is_SPRP_2357_, filter_SPRP_2357_, iter_xprimes7SPRP_2357__ge_lt_, next_SPRP_2357__ge_, prev_may_SPRP_2357__lt_, detect_noncoprime_to_2357_, filter4coprimes_to_2357_
from seed.math.primality_test.SPRP_2357 import *
