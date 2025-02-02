#__all__:goto
r'''[[[
e ../../python3_src/seed/algo/rho_method.py
vs:
    view ../../python3_src/seed/math/RhoDetector.py
        OO
    view ../../python3_src/seed/algo/rho_method.py
        functional
re-export:
    view ../../python3_src/seed/math/sprp_factor_pint__via_rho_method_.py
    from seed.math.sprp_factor_pint__via_rho_method_ import try_factor1_pint__via_rho_method_, sprp_factor_pint__via_rho_method_

seed.algo.rho_method
py -m nn_ns.app.debug_cmd   seed.algo.rho_method -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.algo.rho_method:__doc__ -ht # -ff -df

[[
rho_method:
    ver1: f(2*k) ~ f(k)
    ver2: f(k) ~ f(2**floor_log2(k))
    ver2_1: f(k) ~ f(-1+2**floor_log2(k))
]]


>>> [(x, (x**2+1)%77) for x in range(77)] == (
... [(0, 1), (1, 2), (2, 5), (3, 10), (4, 17), (5, 26), (6, 37), (7, 50), (8, 65), (9, 5), (10, 24), (11, 45), (12, 68), (13, 16), (14, 43), (15, 72)
... , (16, 26), (17, 59), (18, 17), (19, 54), (20, 16), (21, 57), (22, 23), (23, 68), (24, 38), (25, 10), (26, 61), (27, 37), (28, 15), (29, 72), (30, 54), (31, 38)
... , (32, 24), (33, 12), (34, 2), (35, 71), (36, 65), (37, 61), (38, 59), (39, 59), (40, 61), (41, 65), (42, 71), (43, 2), (44, 12), (45, 24), (46, 38), (47, 54)
... , (48, 72), (49, 15), (50, 37), (51, 61), (52, 10), (53, 38), (54, 68), (55, 23), (56, 57), (57, 16), (58, 54), (59, 17), (60, 59), (61, 26), (62, 72), (63, 43)
... , (64, 16), (65, 68), (66, 45), (67, 24), (68, 5), (69, 65), (70, 50), (71, 37), (72, 26), (73, 17), (74, 10), (75, 5), (76, 2)
... ])
True

>>> f = lambda j, x:(x**2+1)%77
>>> test_ = lambda x,y:gcd(x-y,77)
>>> stop_ = 1 .__ne__ # lambda r:not r==1
>>> rho_method_(0, f, test_, stop_)
(7, (3, 5), (4, 26))
>>> rho_method__brute_force_(0, f, test_, stop_)
(7, (3, 5), (4, 26))
>>> rho_method_(0, f, test_, stop_, listing=True)
(7, (3, 5), (4, 26), [(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 5, 5), (4, 26, 26)])
>>> rho_method__brute_force_(0, f, test_, stop_, listing=True)
(7, (3, 5), (4, 26), [(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 5, 5), (4, 26, 26)])
>>> rho_method_(0, f, test_, stop_, to_split_header_cycle=True)
(7, (3, 5), (4, 26), [(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 5, 5), (4, 26, 26)], (3, 1), ([(0, 0, 0), (1, 1, 1), (2, 2, 2)], [(3, 5, 5)]))
>>> rho_method__brute_force_(0, f, test_, stop_, to_split_header_cycle=True)
(7, (3, 5), (4, 26), [(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 5, 5), (4, 26, 26)], (3, 1), ([(0, 0, 0), (1, 1, 1), (2, 2, 2)], [(3, 5, 5)]))


# gcd => not period actually:
>>> rho_method_(0, f, to_split_header_cycle=True)
(True, (7, 61), (9, 61), [(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 5, 5), (4, 26, 26), (5, 61, 61), (6, 26, 26), (7, 61, 61), (8, 26, 26), (9, 61, 61)], (4, 2), ([(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 5, 5)], [(4, 26, 26), (5, 61, 61)]))
>>> rho_method_(0, f, to_reduce_list=True)
(True, (7, 61), (9, 61), (4, 2), ([0, 1, 2, 5], [26, 61]))







# true period:
>>> g = lambda j, x:(x*2+1)%13
>>> rho_method_(0, g, to_split_header_cycle=True)
(True, (15, 7), (27, 7), [(0, 0, 0), (1, 1, 1), (2, 3, 3), (3, 7, 7), (4, 2, 2), (5, 5, 5), (6, 11, 11), (7, 10, 10), (8, 8, 8), (9, 4, 4), (10, 9, 9), (11, 6, 6), (12, 0, 0), (13, 1, 1), (14, 3, 3), (15, 7, 7), (16, 2, 2), (17, 5, 5), (18, 11, 11), (19, 10, 10), (20, 8, 8), (21, 4, 4), (22, 9, 9), (23, 6, 6), (24, 0, 0), (25, 1, 1), (26, 3, 3), (27, 7, 7)], (0, 12), ([], [(0, 0, 0), (1, 1, 1), (2, 3, 3), (3, 7, 7), (4, 2, 2), (5, 5, 5), (6, 11, 11), (7, 10, 10), (8, 8, 8), (9, 4, 4), (10, 9, 9), (11, 6, 6)]))

>>> rho_method_(0, g, to_reduce_list=True)
(True, (15, 7), (27, 7), (0, 12), ([], [0, 1, 3, 7, 2, 5, 11, 10, 8, 4, 9, 6]))
>>> rho_method_(12, g, to_reduce_list=True)
(True, (0, 12), (1, 12), (0, 1), ([], [12]))
>>> rho_method_(12, g, listing=True)
(True, (0, 12), (1, 12), [(0, 12, 12), (1, 12, 12)])













>>> try_factor1_pint__via_rho_method_(0)
Traceback (most recent call last):
    ...
TypeError: 0
>>> try_factor1_pint__via_rho_method_(1)
-1
>>> try_factor1_pint__via_rho_method_(2)
-1
>>> try_factor1_pint__via_rho_method_(3)
-1
>>> try_factor1_pint__via_rho_method_(4)  # !!! fail ?!
-1
>>> try_factor1_pint__via_rho_method_(31)
-1
>>> try_factor1_pint__via_rho_method_(2**37-1)
223
>>> try_factor1_pint__via_rho_method_(2**37-1, to_output_statistics=True)
(223, 1, 23)

below output before: patch001__seed_definition
(223, 1, 21)

>>> try_factor1_pint__via_rho_method_(31, to_output_statistics=True)
(-1, 8, 62)

below output before: patch001__seed_definition
(-1, 2, 12)

>>> for n in range(1, 40):(n, try_factor1_pint__via_rho_method_(n, to_output_statistics=True))
(1, (-1, 0, 0))
(2, (-1, 2, 6))
(3, (-1, 2, 6))
(4, (-1, 2, 6))
(5, (-1, 2, 7))
(6, (2, 1, 2))
(7, (-1, 2, 12))
(8, (4, 1, 2))
(9, (3, 1, 4))
(10, (2, 1, 2))
(11, (-1, 6, 46))
(12, (4, 1, 2))
(13, (-1, 8, 62))
(14, (2, 1, 2))
(15, (5, 2, 6))
(16, (4, 1, 2))
(17, (-1, 8, 60))
(18, (2, 1, 2))
(19, (-1, 8, 60))
(20, (4, 1, 2))
(21, (3, 1, 4))
(22, (2, 1, 2))
(23, (-1, 8, 58))
(24, (4, 1, 2))
(25, (5, 1, 4))
(26, (2, 1, 2))
(27, (3, 1, 4))
(28, (4, 1, 2))
(29, (-1, 8, 71))
(30, (2, 1, 2))
(31, (-1, 8, 62))
(32, (4, 1, 2))
(33, (3, 1, 4))
(34, (2, 1, 2))
(35, (5, 1, 4))
(36, (4, 1, 2))
(37, (-1, 8, 72))
(38, (2, 1, 2))
(39, (3, 1, 4))

below output before: patch001__seed_definition
(1, (-1, 0, 0))
(2, (-1, 2, 8))
(3, (-1, 2, 7))
(4, (-1, 2, 8))
(5, (-1, 2, 14))
(6, (3, 1, 2))
(7, (-1, 2, 5))
(8, (-1, 2, 8))
(9, (3, 1, 2))
(10, (2, 1, 4))
(11, (-1, 2, 15))
(12, (3, 1, 2))
(13, (-1, 2, 11))
(14, (7, 1, 3))
(15, (3, 1, 2))
(16, (-1, 2, 8))
(17, (-1, 2, 18))
(18, (3, 1, 2))
(19, (-1, 2, 14))
(20, (4, 1, 4))
(21, (3, 1, 2))
(22, (2, 1, 4))
(23, (-1, 2, 15))
(24, (3, 1, 2))
(25, (-1, 2, 14))
(26, (2, 1, 4))
(27, (3, 1, 2))
(28, (7, 1, 3))
(29, (-1, 2, 18))
(30, (3, 1, 2))
(31, (-1, 2, 12))
(32, (16, 2, 8))
(33, (3, 1, 2))
(34, (2, 1, 4))
(35, (7, 1, 3))
(36, (3, 1, 2))
(37, (-1, 2, 10))
(38, (2, 1, 4))
(39, (3, 1, 2))










>>> sprp_factor_pint__via_rho_method_(2**37-1)
({223: 1, 616318177: 1}, {})
>>> sprp_factor_pint__via_rho_method_(2**37-1, to_output_statistics=True)
({223: 1, 616318177: 1}, {}, 23)

below output before: patch001__seed_definition
({223: 1, 616318177: 1}, {}, 21)


>>> for n in range(1, 10):
...     sprp_factor_pint__via_rho_method_(n)
...     sprp_factor_pint__via_rho_method_(n, to_output_statistics=True)
({}, {})
({}, {}, 0)
({2: 1}, {})
({2: 1}, {}, 0)
({3: 1}, {})
({3: 1}, {}, 0)
({2: 2}, {})
({2: 2}, {}, 0)
({5: 1}, {})
({5: 1}, {}, 0)
({2: 1, 3: 1}, {})
({2: 1, 3: 1}, {}, 2)
({7: 1}, {})
({7: 1}, {}, 0)
({2: 3}, {})
({2: 3}, {}, 0)
({3: 2}, {})
({3: 2}, {}, 0)












:[why_required__factor_pint_as_pefect_power_]:here
required:factor_pint_as_pefect_power_()
>>> def show_fails(N, /):
...  for n in range(1, N):
...     if _x_is_SPRP_(n):continue
...     (imay_proper_factor, jseed, _total_steps) = try_factor1_pint__via_rho_method_(n, to_output_statistics=True)
...     if imay_proper_factor == -1:
...         print(n, (imay_proper_factor, jseed, _total_steps), sep=':')
>>> show_fails(2**8)
1:(-1, 0, 0)
4:(-1, 2, 6)

below output before: patch001__seed_definition
>>> show_fails(2**16) #doctest: +SKIP
1:(-1, 0, 0)
4:(-1, 2, 8)
8:(-1, 2, 8)
16:(-1, 2, 8)
25:(-1, 2, 14)
>>> show_fails(2**8) #doctest: +SKIP
1:(-1, 0, 0)
4:(-1, 2, 8)
8:(-1, 2, 8)
16:(-1, 2, 8)
25:(-1, 2, 14)















view ../../python3_src/nn_ns/math_nn/factor_Mersenne_number_into_prime2exp.py.cached.txt
>37
: {223: 1, 616318177: 1}
.
>41
: {13367: 1, 164511353: 1}
.
>59
: {179951: 1, 3203431780337: 1}
.
>67
: {193707721: 1, 761838257287: 1}
.
>101
: {7432339208719: 1, 341117531003194129: 1}
.


below output before&after: patch001__seed_definition
py_adhoc_call   seed.algo.rho_method   @try_factor1_pint__via_rho_method_ +to_output_statistics  =2**16+1
(-1, 64, 4135)
    [log2(4135) ~= 12.0]
(-1, 64, 4128)

py_adhoc_call   seed.algo.rho_method   @try_factor1_pint__via_rho_method_ +to_output_statistics  =2**16-1
(3, 1, 5)
(17, 1, 2)

py_adhoc_call   seed.algo.rho_method   @try_factor1_pint__via_rho_method_ +to_output_statistics  =2**31-1
(-1, 860, 740460)
    [log2(740460) ~= 19.5]
(-1, 860, 740460)

py_adhoc_call   seed.algo.rho_method   @try_factor1_pint__via_rho_method_ +to_output_statistics  =2**37-1
(223, 1, 21)
(223, 1, 23)

py_adhoc_call   seed.algo.rho_method   @try_factor1_pint__via_rho_method_ +to_output_statistics  =2**41-1
(13367, 1, 476)
(13367, 1, 240)

py_adhoc_call   seed.algo.rho_method   @try_factor1_pint__via_rho_method_ +to_output_statistics  =2**59-1
(179951, 1, 1098)
(179951, 1, 106)

py_adhoc_call   seed.algo.rho_method   @try_factor1_pint__via_rho_method_ +to_output_statistics  =2**67-1
(193707721, 1, 31997)
    [log2(31997) ~= 15.0]
    [log2(193707721) ~= 27.5]
(193707721, 1, 26418)

py_adhoc_call   seed.algo.rho_method   @try_factor1_pint__via_rho_method_ +to_output_statistics  =2**101-1
(7432339208719, 1, 4842513)
    [log2(4842513) ~= 22.2]
    [log2(7432339208719) ~= 42.8]
(7432339208719, 1, 5065574)





py_adhoc_call   seed.algo.rho_method   @sprp_factor_pint__via_rho_method_ +to_output_statistics  =2**31-1
({2147483647: 1}, {}, 0)

py_adhoc_call   seed.algo.rho_method   @sprp_factor_pint__via_rho_method_ +to_output_statistics  =2**41-1
({13367: 1, 164511353: 1}, {}, 476)
({13367: 1, 164511353: 1}, {}, 240)









]]]'''#'''
__all__ = r'''
rho_method_
try_factor1_pint__via_rho_method_
sprp_factor_pint__via_rho_method_


rho_method_
rho_method__brute_force_
    postprocess4rho_method_
    preprocess4rho_method_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from operator import __eq__
from itertools import islice
from math import isqrt, gcd
#from seed.math.gcd import gcd

from seed.helper.ifNone import ifNone
#from seed.tiny_.types5py import curry1
from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...

def _key_(j, xj, /):
    return xj

def _reduce_list(ls, /):
    return [xi for (i, xi, ki) in ls]
def postprocess4rho_method_(result_tpl, test_, stop_, to_reduce_list, /):
    '#for:[listing:=True][to_split_header_cycle:=True]'
    assert len(result_tpl) in (3, 4)
    assert (len(result_tpl) == 4) is (type(result_tpl[-1]) is list)
    if len(result_tpl) == 3:
        return result_tpl
    (r, (i, xi), (j, xj), ls) = result_tpl
    period = j - i
    # [stop_(r[i,j])]
    for i_ in reversed(range(i)):
        # [stop_(r[i_+1,j_+1])]
        j_ = i_ + period
        (_i_, xi_, ki_) = ls[i_]
        (_j_, xj_, kj_) = ls[j_]
        r_ = test_(kj_, ki_)
        if not stop_(r_):
            # [stop_(r[i_+1,j_+1])]
            # [not stop_(r[i_,j_])]
            sz4header = 1+i_
            break
        # [stop_(r[i_,j_])]
    else:
        # [stop_(r[i_:=0,j_])]
        sz4header = 0
        #bug:assert i == 0
        #   !! period may be >= 2 # cause i+=1
    sz4header
    period
    header = ls[:sz4header]
    cycle = ls[sz4header:sz4header+period]
    if to_reduce_list:
        _header = _reduce_list(header)
        _cycle = _reduce_list(cycle)
        return (r, (i, xi), (j, xj), (sz4header, period), (_header, _cycle))
        #._ls = _reduce_list(ls)
        #.return (r, (i, xi), (j, xj), _ls, (sz4header, period), (_header, _cycle))

    return (*result_tpl, (sz4header, period), (header, cycle))

def _tail4rho_method_(tpl, ls, test_, stop_, listing, to_split_header_cycle, to_reduce_list, /):
    if listing:
        tpl = (*tpl, ls)
    if to_split_header_cycle:
        tpl = postprocess4rho_method_(tpl, test_, stop_, to_reduce_list)
    return tpl
def preprocess4rho_method_(key, listing, to_split_header_cycle, to_reduce_list, /):
    check_type_is(bool, listing)
    check_type_is(bool, to_split_header_cycle)
    check_type_is(bool, to_reduce_list)
    if to_reduce_list:
        to_split_header_cycle = True
    if to_split_header_cycle:
        listing = True
    key = ifNone(key, _key_)
        #key = ifNone(key, echo)
    return (key, listing, to_split_header_cycle, to_reduce_list)
def rho_method__brute_force_(x0, f, test_=__eq__, stop_=bool, /, *, key=None, listing=False, to_split_header_cycle=False, to_reduce_list=False):
    'O(max_j**2) => x[0] -> (j->x[j]->x[j+1]) -> (k->k->r) -> (r->whether_stop/bool) -> (kw:key/(j->x[j]->k)) -> (r{stop_(r)}, (i, x[i]), (j, x[j]), ?list4all?/[(i, xi, ki)], ?(sz4header, period)?, ?(header, cycle)?)  # stop iff found result or detect bad seed/state'
    (key, listing, to_split_header_cycle, to_reduce_list) = preprocess4rho_method_(key, listing, to_split_header_cycle, to_reduce_list)

    j, xj = 0, x0
    777; kj = key(j, xj)
    777; del x0
    ls = []
        # :: [(i, xi, ki)]
    while 1:
        for (i, xi, ki) in ls:
            r = test_(kj, ki)
            if stop_(r):
                ls.append((j, xj, kj))
                tpl = (r, (i, xi), (j, xj))
                return _tail4rho_method_(tpl, ls, test_, stop_, listing, to_split_header_cycle, to_reduce_list)
        ls.append((j, xj, kj))
        j += 1
        777; xj = f(j, xj)
        777; kj = key(j, xj)
    raise 000

def rho_method_(x0, f, test_=__eq__, stop_=bool, /, *, key=None, listing=False, to_split_header_cycle=False, to_reduce_list=False):
    'O(max_j) => x[0] -> (j->x[j]->x[j+1]) -> (k->k->r) -> (r->whether_stop/bool) -> (kw:key/(j->x[j]->k)) -> (r{stop_(r)}, (i, x[i]), (j, x[j]), ?list4all?/[(i, xi, ki)], ?(sz4header, period)?, ?(header, cycle)?)  # stop iff found result or detect bad seed/state'
    # [case4stop == (-1/bad|0/continue|+1/ok)]
    #   eg:gcd => (modulus/bad | 1/continue | proper_factor/[2..<modulus]/ok)
    (key, listing, to_split_header_cycle, to_reduce_list) = preprocess4rho_method_(key, listing, to_split_header_cycle, to_reduce_list)

    if listing: ls = []
            # :: [(i, xi, ki)]
    else:ls = None # !! _tail4rho_method_

    j, xj = 0, x0
    777; kj = key(j, xj)
    777; del x0
    if listing: ls.append((j, xj, kj))
    # [j == 0 == 2**0 - 1]
    while 1:
        # [j == 2**? - 1]
        i, xi, ki = j, xj, kj
        j += 1 # == 2**?
        # [i == 2**? - 1]
        # [j == 2**?]
        for j in range(j, j<<1):
            # [j <- [2**? ..= 2**(?+1)-1]]
            # [(j-i) <- [1 ..= 2**?]]
            # => [detect period for all lengths]
            777; xj = f(j, xj)
            777; kj = key(j, xj)
            if listing: ls.append((j, xj, kj))
            # ki, kj
            r = test_(kj, ki)
            if stop_(r):
                tpl = (r, (i, xi), (j, xj))
                return _tail4rho_method_(tpl, ls, test_, stop_, listing, to_split_header_cycle, to_reduce_list)
        # [j == 2**(?+1)-1]
    raise 000



def _lazy_imports():
    'lazy_import'
    global _lazy_imports
    from seed.math.semi_factor_pint_via_trial_division import semi_factor_pint_via_trial_division
    from seed.math.merge_coprimess_into_smaller_coprimes import merge_coprimess_into_smaller_coprimes
    from seed.math.factor_pint_as_pefect_power_ import factor_pint_as_pefect_power_
    _4lazy_imports = (factor_pint_as_pefect_power_, merge_coprimess_into_smaller_coprimes, semi_factor_pint_via_trial_division)
    def f():
        return _4lazy_imports
    if f is _lazy_imports:raise 000
    _lazy_imports = f
    if not f is _lazy_imports:raise 000
    return _lazy_imports()
def _x_is_SPRP_(n, /):
    'used in doctest'
    return _is_SPRP_(n)
def _is_SPRP_(n, /):
    "lazy_import"
    global _is_SPRP_
    from seed.math.prime_gens import detect_strong_pseudoprime__not_waste_too_much_time_ as f
    if f is _is_SPRP_:raise 000
    _is_SPRP_ = f
    if not f is _is_SPRP_:raise 000
    return _is_SPRP_(n)
#.def _seeds4factor(n, /):
#.    return range(isqrt(n), n)
#.    x = 2
#.    while 1:
#.        x = (x+2)%n
#.    return
#.def _f4factor(n, x, /):
#.    return (x**2+1)%n
#.    return pow(x, 2, n)+1
def _f4factor(n, a, x, /):
    r'''
    :: n -> a -> x -> (x**2+a)%n
        [x0 <- [0..=n-1]]
        [a <- [1..=n-3]]
        [seed := (a, x0)]
    '''#'''
    # patch001__seed_definition
    return (x**2+a)%n
def sprp_factor_pint__via_rho_method_(n, f_=None, /, *, seeds=None, max_num_seeds=None, max_num_tries_per_seed=None, to_output_statistics=False):
    'n/int{>=1} -> may (n -> (*params) -> uint%n -> uint%n) -> (kw:seeds/may (Iter params_x0/(*params, x0))) -> (success_part, failure_part)/(sprp2exp, non_sprp2exp)/({sprp:exp}, {non_sprp:exp}) if not to_output_statistics else (sprp2exp, non_sprp2exp, total_steps) # [SPRP == strong probable-prime]'

    check_type_is(bool, to_output_statistics)
    check_int_ge(1, n)
    #if n < 4:
    if n == 1:
        return ({}, {}, 0) if to_output_statistics else ({}, {})
    # [n >= 2]

    (factor_pint_as_pefect_power_, merge_coprimess_into_smaller_coprimes, semi_factor_pint_via_trial_division) = _lazy_imports()

    ls4sprp4succ = []
        # [sprp-factor]{pairwise-coprime}
    ls4non_sprp4todo = []
        # [(non-sprp)-(non-pefect_power)-factor]{pairwise-coprime}
        # a todo_list
    ls4non_sprp4fail = []
    def put(factor):
        # [factor >= 2]
        if _is_SPRP_(factor):
            ls4sprp4succ.append(factor)
            return
        (factor, exp) = factor_pint_as_pefect_power_(factor)
            # :[why_required__factor_pint_as_pefect_power_]:goto
            # try_factor1_pint__via_rho_method_ fail at: 4,8,16, 25...
        if exp > 1 and _is_SPRP_(factor):
            ls4sprp4succ.append(factor)
            return
        ls4non_sprp4todo.append(factor)
        return
    #end-put
    kwds = dict(to_detect_SPRP=False, seeds=seeds, max_num_seeds=max_num_seeds, max_num_tries_per_seed=max_num_tries_per_seed, to_output_statistics=True)

    # [n >= 2]
    put(n)
    total_steps = 0
    while ls4non_sprp4todo:
        u = ls4non_sprp4todo.pop()
        # [u >= 2]
        (imay_proper_factor, jseed, _total_steps) = try_factor1_pint__via_rho_method_(u, f_, **kwds)
        total_steps += _total_steps
        if imay_proper_factor == -1:
            ls4non_sprp4fail.append(u)
            continue
        factor = imay_proper_factor
        factors = merge_coprimess_into_smaller_coprimes([[factor], [u//factor]])
        for _ in map(put, factors):pass
    assert not ls4non_sprp4todo
    777; ls4non_sprp4fail
    777; ls4sprp4succ
    unfactored_part = n
    (sprp2exp, unfactored_part) = semi_factor_pint_via_trial_division(ls4sprp4succ, unfactored_part)
    (non_sprp2exp, unfactored_part) = semi_factor_pint_via_trial_division(ls4non_sprp4fail, unfactored_part)
    if not unfactored_part==1:raise Exception(n, sprp2exp, non_sprp2exp, unfactored_part, total_steps)
    if to_output_statistics:
        return (sprp2exp, non_sprp2exp, total_steps)
    return (sprp2exp, non_sprp2exp)
def try_factor1_pint__via_rho_method_(n, f_=None, /, *, to_detect_SPRP=False, seeds=None, max_num_seeds=None, max_num_tries_per_seed=None, to_output_statistics=False):
    'n/int{>=1}/[not is_prime(n)] -> may (n -> (*params) -> uint%n -> uint%n) -> (kw:seeds/may (Iter params_x0/(*params, x0))) -> imay proper_factor if not to_output_statistics else (imay_proper_factor, jseed, total_steps) # [SPRP == strong probable-prime]'
    check_type_is(bool, to_detect_SPRP)
    check_type_is(bool, to_output_statistics)
    check_int_ge(1, n)
    if to_detect_SPRP:
        if not _is_SPRP_(n):raise ValueError('is composite integer')
    if n == 1:
        return (-1, 0, 0) if to_output_statistics else -1
    # [n >= 2]


    w = 0 if max_num_tries_per_seed and max_num_seeds and seeds else (2 if n < 16 else isqrt(isqrt(n)))
    # [w >= 2]or[w == 0]

    max_num_tries_per_seed = ifNone(max_num_tries_per_seed, 4*w)
    max_num_seeds = ifNone(max_num_seeds, 4*w)
    #seeds = ifNone(seeds, _seeds4factor(n))

    w2 = w*w
    seeds = ifNone(seeds, ((a, max(n-1,w+w2)) for a in range(w,max(n-3,w2))))
        # patch001__seed_definition
    seeds = islice(seeds, max_num_seeds)

    check_int_ge(0, max_num_seeds)
    check_int_ge(1, max_num_tries_per_seed)

    f_ = ifNone(f_, _f4factor)
    #f = curry1(f_, n)

    max_j = max_num_tries_per_seed
    test_ = lambda x,y:gcd(x-y,n)
    stop_ = 1 .__ne__
    #stop_ = lambda r:not r==1
    num_js = 0
    def key_(j, xj, /):
        nonlocal num_js
        if j > max_j:
            return 0
        num_js += 1
        return xj

    jseed = 0
    for jseed, seed in enumerate(seeds, 1):
        params_x0 = seed
        (*params, x0) = params_x0
        def f(j, xj, /, *, f_=f_, n=n, params=params):
            # patch001__seed_definition
            return f_(n, *params, xj)
        tpl = rho_method_(x0, f, test_, stop_, key=key_)
        (r, (i, xi), (j, xj)) = tpl
        _gcd = r
        if 1 < _gcd < n:
            proper_factor = _gcd
            #success
            imay_proper_factor = proper_factor
            break
        assert _gcd == n or _gcd == 0
        #bad seed or hit max_j
    else:
        #failure
        imay_proper_factor = -1
    imay_proper_factor
    total_steps = num_js
    if to_output_statistics:
        return (imay_proper_factor, jseed, total_steps)

    return imay_proper_factor



__all__
from seed.algo.rho_method import rho_method_
from seed.algo.rho_method import try_factor1_pint__via_rho_method_, sprp_factor_pint__via_rho_method_
from seed.algo.rho_method import *
