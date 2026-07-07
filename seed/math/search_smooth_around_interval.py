#__all__:goto
#DONE:min/max:缩减范围
#   new_version:prune using best_n
r'''[[[
e ../../python3_src/seed/math/search_smooth_around_interval.py
see:
    view ../../python3_src/seed/math/iter_sorted_products_of_uints.py

seed.math.search_smooth_around_interval
py -m nn_ns.app.debug_cmd   seed.math.search_smooth_around_interval -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.search_smooth_around_interval:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> search_max_smooth_integer_le_(15, [2])
(8, (3,))
>>> search_max_smooth_integer_le_(15, [3])
(9, (2,))
>>> search_max_smooth_integer_le_(15, [2,3])
(12, (2, 1))
>>> search_max_smooth_integer_le_(15, [2,3,5])
(15, (0, 1, 1))

>>> search_min_smooth_integer_ge_(10, [2])
(16, (4,))
>>> search_min_smooth_integer_ge_(10, [3])
(27, (3,))
>>> search_min_smooth_integer_ge_(10, [2,3])
(12, (2, 1))
>>> search_min_smooth_integer_ge_(10, [2,3,5])
(10, (1, 0, 1))

>>> search_smooth_integer_around_interval_(10, 15, [2,3,5])
((10, (1, 0, 1)), (15, (0, 1, 1)))
>>> search_smooth_integer_around_interval_(10, 15, [2,3])
((9, (0, 2)), (16, (4, 0)))
>>> search_smooth_integer_around_interval_(10, 15, [3])
((9, (2,)), (27, (3,)))
>>> search_smooth_integer_around_interval_(10, 15, [2])
((8, (3,)), (16, (4,)))





>>> search_smooth_integer_around_interval_(103, 140, [2,3,5])
((100, (2, 0, 2)), (144, (4, 2, 0)))
>>> search_smooth_integer_around_interval_(108, 108, [2,3,5])
((108, (2, 3, 0)), (108, (2, 3, 0)))
>>> search_smooth_integer_around_interval_(105, 105, [2,3,5])
((100, (2, 0, 2)), (108, (2, 3, 0)))


>>> search_smooth_integer_around_interval_(103, 140, [2,3,5], tuple_vs_dict=True)
((100, {2: 2, 0: 2}), (144, {1: 2, 0: 4}))




>>> from seed.math.iter_sorted_products_of_uints import print_sorted_products_of_strict_sorted_pairwise_coprime_uints
>>> rs = sorted_search_smooth_integer_inside_interval_(1, 30, [2,3,5])
>>> rs
[(1, (0, 0, 0)), (2, (1, 0, 0)), (3, (0, 1, 0)), (4, (2, 0, 0)), (5, (0, 0, 1)), (6, (1, 1, 0)), (8, (3, 0, 0)), (9, (0, 2, 0)), (10, (1, 0, 1)), (12, (2, 1, 0)), (15, (0, 1, 1)), (16, (4, 0, 0)), (18, (1, 2, 0)), (20, (2, 0, 1)), (24, (3, 1, 0)), (25, (0, 0, 2)), (27, (0, 3, 0)), (30, (1, 1, 1))]
>>> print_sorted_products_of_strict_sorted_pairwise_coprime_uints([2,3,5], len(rs))
[1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30]
>>> [u for u, _ in rs]
[1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30]
>>> sorted_search_smooth_integer_inside_interval_(103, 140, [2,3,5])
[(108, (2, 3, 0)), (120, (3, 1, 1)), (125, (0, 0, 3)), (128, (7, 0, 0)), (135, (0, 3, 1))]
>>> sorted_search_smooth_integer_inside_interval_(100, 108, [2,3,5])
[(100, (2, 0, 2)), (108, (2, 3, 0))]
>>> sorted_search_smooth_integer_inside_interval_(108, 108, [2,3,5])
[(108, (2, 3, 0))]
>>> sorted_search_smooth_integer_inside_interval_(101, 107, [2,3,5])
[]


>>> sorted_search_smooth_integer_inside_interval_(100, 108, [2,3,5], tuple_vs_dict=True)
[(100, {2: 2, 0: 2}), (108, {1: 3, 0: 2})]





[[
??? O(5**len(us)) ???
??? O(exp(len(us))) ???

py_adhoc_call { +to_show_total_timedelta }  seed.math.search_smooth_around_interval   ,search_smooth_integer_around_interval_  =... =123456789987654321111111111111111111 ='[2]'
    (83076749736557242056487941267521536, (116,))
    (166153499473114484112975882535043072, (117,))
    total::duration: 0.13099516 *(unit: 0:00:01)
    #有效位数:0

py_adhoc_call { +to_show_total_timedelta }  seed.math.search_smooth_around_interval   ,search_smooth_integer_around_interval_  =... =123456789987654321111111111111111111 ='[2,3]'
    (123194829669983853169202804520124416, (50, 42))
    (124615124604835863084731911901282304, (115, 1))
    total::duration: 0.15572084500000005 *(unit: 0:00:01)
    #有效位数:2

py_adhoc_call { +to_show_total_timedelta }  seed.math.search_smooth_around_interval   ,search_smooth_integer_around_interval_  =... =123456789987654321111111111111111111 ='[2,3,5]'
    (123395347352125440000000000000000000, (36, 23, 19))
    (123473197721091960600568887744921600, (20, 58, 2))
    total::duration: 0.24410169999999998 *(unit: 0:00:01)
    #有效位数:3

py_adhoc_call { +to_show_total_timedelta }  seed.math.search_smooth_around_interval   ,search_smooth_integer_around_interval_  =... =123456789987654321111111111111111111 ='[2,3,5,7]'
    (123456713654528522617038603093540864, (28, 24, 0, 18))
    (123461727978533333961277440000000000, (31, 11, 10, 16))
    total::duration: 0.32001285299999993 *(unit: 0:00:01)
    #有效位数:4

py_adhoc_call { +to_show_total_timedelta }  seed.math.search_smooth_around_interval   ,search_smooth_integer_around_interval_  =... =123456789987654321111111111111111111 ='[2,3,5,7,11]'
    (123456713654528522617038603093540864, (28, 24, 0, 18, 0))
    (123457166543881325206790749760990625, (0, 14, 5, 11, 15))
    total::duration: 1.604873392 *(unit: 0:00:01)
    #有效位数:5

py_adhoc_call { +to_show_total_timedelta }  seed.math.search_smooth_around_interval   ,search_smooth_integer_around_interval_  =... =123456789987654321111111111111111111 ='[2,3,5,7,11,13]'
    (123456777359893931324758907520000000, (13, 21, 7, 13, 4, 1))
    (123456809172330832859781120000000000, (20, 16, 10, 4, 1, 9))
    total::duration: 6.830119028 *(unit: 0:00:01)
    #有效位数:6


py_adhoc_call { +to_show_total_timedelta }  seed.math.search_smooth_around_interval   ,search_smooth_integer_around_interval_  =... =123456789987654321111111111111111111 ='[2,3,5,7,11,13,17]'
    (123456777359893931324758907520000000, (13, 21, 7, 13, 4, 1, 0))
    (123456801281492250000000000000000000, (19, 17, 21, 0, 3, 2, 1))
    total::duration: 27.874380458999998 *(unit: 0:00:01)
    #有效位数:6

py_adhoc_call { +to_show_total_timedelta }  seed.math.search_smooth_around_interval   ,search_smooth_integer_around_interval_  =... =123456789987654321111111111111111111 ='[2,3,5,7,11,13,17,19]'
    (123456789255034555678853439117468750, (1, 2, 6, 16, 0, 1, 7, 5))
    (123456790782696783380522400000000000, (14, 2, 11, 9, 8, 0, 2, 3))
    total::duration: 96.891551854 *(unit: 0:00:01)
    #有效位数:7

py_adhoc_call { +to_show_total_timedelta }  seed.math.search_smooth_around_interval   ,search_smooth_integer_around_interval_  =... =123456789987654321111111111111111111 ='[2,3,5,7,11,13,17,19,23]'
    (123456789969753323793951490669056000, (12, 8, 3, 9, 0, 1, 4, 4, 5))
    (123456790684472096046715203043196928, (23, 14, 0, 2, 0, 1, 1, 3, 10))
    total::duration: 333.11480527699996 *(unit: 0:00:01)
    #有效位数:7

py_adhoc_call { +to_show_total_timedelta }  seed.math.search_smooth_around_interval   ,search_smooth_integer_around_interval_  =... =123456789987654321111111111111111111 ='[2,3,5,7,11,13,17,19,23,29]'
    (123456789969753323793951490669056000, (12, 8, 3, 9, 0, 1, 4, 4, 5, 0))
    (123456790042656754949009703483525000, (3, 2, 5, 9, 3, 6, 1, 0, 6, 2))
    total::duration: 715.27626465 *(unit: 0:00:01)
    #有效位数:7


]]



py_adhoc_call   seed.math.search_smooth_around_interval   @f
]]]'''#'''
__all__ = r'''
search_smooth_integer_around_interval_
    search_max_smooth_integer_le_
    search_min_smooth_integer_ge_

sorted_search_smooth_integer_inside_interval_
    disordered_search_smooth_integer_inside_interval_
        disordered_iter_search_smooth_integer_inside_interval_

check_smooth_bases_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.iters.is_sorted import is_strict_sorted
    from seed.tiny_.check import check_type_is, check_int_ge, check_all_
    from seed.math.floor_ceil_tools.fc_div import floor_div, ceil_div
    from seed.math.floor_ceil_tools.fc_log import ceil_log_, floor_log_
    from seed.iters.flatten_recur import flatten_recur
    # def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):

    from seed.iters.flatten_recur__7iter import flatten_recur__7iter_
    #def flatten_recur__7iter_(g, /, dat6init=None, next6init_=None, *, explain6exit_=None, explain6halfway_=None, send_=None, throw_=None, BaseException=None):
with mk_ctx4lazy_import4funcs_(__name__, arbitrary_ok=True):
    #from seed.iters.flatten_recur__7iter import Case4FlattenRecur7Iter6halfway, Case4FlattenRecur7Iter6exit
    from seed.iters.flatten_recur__7iter import Case6halfway, Case6exit
        #Case6halfway:subcall, yield1, yields
        #Case6exit:tailcall, return1
#.#################################
___end_mark_of_excluded_global_names__0___ = ...


def check_smooth_bases_(us, /, *, smooth_bases_checked=False):
    if smooth_bases_checked:
        return
    us[:0] #seq
    if not len(us) > 0:raise TypeError
    check_all_([check_int_ge, 2], us)
    if not is_strict_sorted(us):raise TypeError
def search_max_smooth_integer_le_(upperbound, us, /, *, tuple_vs_dict=False, smooth_bases_checked=False):
    'upperbound/uint{>=1} -> us/strict_sorted[uint{>=2}] -> (m/uint{>=1}{<=upperbound}, j2e4m/[uint]{len==len{us}})'
    # new_version:prune using best_n
    check_int_ge(1, upperbound)
    check_smooth_bases_(us, smooth_bases_checked=smooth_bases_checked)
    sz = len(us)
    assert sz > 0
    j2u = us
    (_mk, j2e4n) = _init_j2e_(sz, tuple_vs_dict)
    best_j2e4n = _mk(j2e4n)
    best_n = 1
    def set_best_(n, /):
        nonlocal best_n, best_j2e4n
        best_j2e4n = _mk(j2e4n)
        best_n = n
    def recur_(j, n, m, M, /, *, j2e4n=j2e4n):
        # [n ~ j2e4n]
        # [j >= 0]
        # [M >= m >= 1]
        # [1 <= best_n <= n*m <= n*M <= upperbound]

        old_ej = j2e4n[j]
        uj = j2u[j]
        into = j > 0
        b_new_best = False
        if not into:
            _ej = floor_log_(uj, M)
            pw = uj**_ej
            if not pw < m:
                M = floor_div(M, pw)
                assert 1 <= M < uj
                n *= pw
                j2e4n[j] += _ej
                if n > best_n:
                    set_best_(n)
                    b_new_best = True
                elif n < best_n:
                    raise 000
        else:
            while 1:
                # [1 <= best_n <= n*m <= n*M <= upperbound]
                if (yield recur_(j-1, n, m, M)):
                    # prune using best_n here
                    b_new_best = True
                    m = ceil_div(best_n, n)
                    if m > M: break
                    # [1 <= best_n <= n*m <= n*M <= upperbound]
                m = ceil_div(m, uj)
                M = floor_div(M, uj)
                if m > M: break
                n *= uj
                j2e4n[j] += 1
                # [1 <= best_n <= n*m <= n*M <= upperbound]
        j2e4n[j] = old_ej
        return b_new_best
    flatten_recur(recur_(sz-1, 1, best_n, upperbound))
    return (best_n, best_j2e4n)
def search_min_smooth_integer_ge_(lowerbound, us, /, *, tuple_vs_dict=False, smooth_bases_checked=False):
    'lowerbound/uint{>=1} -> us/strict_sorted[uint{>=2}] -> (M/uint{>=lowerbound}, j2e4M/[uint]{len==len{us}})'
    # new_version:prune using best_n
    check_int_ge(1, lowerbound)
    check_smooth_bases_(us, smooth_bases_checked=smooth_bases_checked)
    sz = len(us)
    assert sz > 0
    j2u = us
    (_mk, j2e4n) = _init_j2e_(sz, tuple_vs_dict)
    best_j2e4n = None
    best_n = (1+lowerbound)*us[0]
    def set_best_(n, /):
        nonlocal best_n, best_j2e4n
        best_j2e4n = _mk(j2e4n)
        best_n = n
    def recur_(j, n, m, M, /, *, j2e4n=j2e4n):
        # [n ~ j2e4n]
        # [j >= 0]
        # [M >= m >= 1]
        # [1 <= lowerbound <= n*m <= n*M <= best_n]

        old_ej = j2e4n[j]
        uj = j2u[j]
        into = j > 0
        b_new_best = False
        if not into:
            _ej = ceil_log_(uj, m)
            pw = uj**_ej
            if not pw > M:
                m = ceil_div(m, pw)
                assert 1 == m
                n *= pw
                j2e4n[j] += _ej
                if n < best_n:
                    set_best_(n)
                    b_new_best = True
                elif n > best_n:
                    raise 000
        else:
            while 1:
                # [1 <= lowerbound <= n*m <= n*M <= best_n]
                if (yield recur_(j-1, n, m, M)):
                    # prune using best_n here
                    b_new_best = True
                    M = floor_div(best_n, n)
                    if m > M: break
                    # [1 <= lowerbound <= n*m <= n*M <= best_n]
                m = ceil_div(m, uj)
                M = floor_div(M, uj)
                if m > M: break
                n *= uj
                j2e4n[j] += 1
                # [1 <= lowerbound <= n*m <= n*M <= best_n]
        j2e4n[j] = old_ej
        return b_new_best
    flatten_recur(recur_(sz-1, 1, lowerbound, best_n))
    if best_j2e4n is None:raise 000
    return (best_n, best_j2e4n)

r'''[[[
def search_max_smooth_integer_le_(min4interval, us, /, *, tuple_vs_dict=False, smooth_bases_checked=False):
    'min4interval/uint{>=1} -> us/strict_sorted[uint{>=2}] -> (m/uint{>=1}{<=min4interval}, j2e4m/[uint]{len==len{us}})'
    check_int_ge(1, min4interval)
    check_smooth_bases_(us, smooth_bases_checked=smooth_bases_checked)
    sz = len(us)
    j2u = us
    #j2e = [0]*sz
    #best_j2e = (0,)*sz
    (_mk, j2e) = _init_j2e_(sz, tuple_vs_dict)
    best_j2e = _mk(j2e)
    best_u = 1
    def set_best_(m, /):
        nonlocal best_u, best_j2e
        best_j2e = _mk(j2e)
        best_u = m
    def recur_(j, m, /, *, j2e=j2e, min4interval=min4interval):
        # [m ~ j2e]
        # [1 <= m <= min4interval]
        if j == -1:
            return
        old_ej = j2e[j]
        uj = j2u[j]
        into = j > 0
        while 1:
            #if into:recur_(j-1, m)
            if into:yield recur_(j-1, m)
            m *= uj
            if m > min4interval:
                break
            j2e[j] += 1
            if m > best_u:
                set_best_(m)
        j2e[j] = old_ej
    #recur_(sz-1, 1)
    flatten_recur(recur_(sz-1, 1))
    return (best_u, best_j2e)
#]]]'''#'''


r'''[[[
def search_min_smooth_integer_ge_(max4interval, us, /, *, tuple_vs_dict=False, smooth_bases_checked=False):
    'max4interval/uint{>=1} -> us/strict_sorted[uint{>=2}] -> (M/uint{>=max4interval}, j2e4M/[uint]{len==len{us}})'
    check_int_ge(1, max4interval)
    check_smooth_bases_(us, smooth_bases_checked=smooth_bases_checked)
    sz = len(us)
    j2u = us
    #j2e = [0]*sz
    (_mk, j2e) = _init_j2e_(sz, tuple_vs_dict)
    best_j2e = None
    best_u = (1+max4interval)*us[0]
    def set_best_(M, /):
        nonlocal best_u, best_j2e
        best_j2e = _mk(j2e)
        best_u = M
    def recur_(j, M, /, *, j2e=j2e, max4interval=max4interval):
        # [M ~ j2e]
        # [1 <= M <= max4interval]
        if j == -1:
            return
        old_ej = j2e[j]
        uj = j2u[j]
        into = j > 0
        while 1:
            #if into:recur_(j-1, M)
            if into:yield recur_(j-1, M)
            M *= uj
            j2e[j] += 1
            if M >= max4interval:
                if M < best_u:
                    set_best_(M)
                break
        j2e[j] = old_ej
    #recur_(sz-1, 1)
    flatten_recur(recur_(sz-1, 1))
    if best_j2e is None:raise 000
    return (best_u, best_j2e)
#]]]'''#'''

def search_smooth_integer_around_interval_(emay_min4interval, max4interval, us, /, *, tuple_vs_dict=False, smooth_bases_checked=False):
    'emay min4interval/uint{>=1} -> max4interval/uint{>=1} -> us/strict_sorted[uint{>=2}] -> ((m/uint{>=1}{<=min4interval}, j2e4m/[uint]{len==len{us}}), (M/uint{>=max4interval}, j2e4M/[uint]{len==len{us}}))'
    min4interval = max4interval if ... is emay_min4interval else emay_min4interval
    check_int_ge(1, min4interval)
    check_int_ge(min4interval, max4interval)
    check_smooth_bases_(us, smooth_bases_checked=smooth_bases_checked)
    777;smooth_bases_checked = True
    (m, j2e4m) = search_max_smooth_integer_le_(min4interval, us, tuple_vs_dict=tuple_vs_dict, smooth_bases_checked=smooth_bases_checked)
    (M, j2e4M) = search_min_smooth_integer_ge_(max4interval, us, tuple_vs_dict=tuple_vs_dict, smooth_bases_checked=smooth_bases_checked)
    return ((m, j2e4m), (M, j2e4M))


class _Counter(dict):
    def __missing__(sf, k, /):
        return 0
    def __setitem__(sf, k, v, /):
        if v == 0:
            sf.pop(k, 0)
        else:
            dict.__setitem__(sf, k, v)
def _init_j2e_(sz, tuple_vs_dict):
    if not tuple_vs_dict:
        _mk = tuple
        j2e4n = [0]*sz
    else:
        _mk = dict
        j2e4n = _Counter()
    return (_mk, j2e4n)

def sorted_search_smooth_integer_inside_interval_(min4interval, max4interval, us, /, *, tuple_vs_dict=False, smooth_bases_checked=False):
    'min4interval/uint{>=1} -> max4interval/uint{>=1} -> us/strict_sorted[uint{>=2}] -> sorted-[(n/uint{>=min4interval}{<=max4interval}, j2e4n/[uint]{len==len{us}})]'
    # vs:prime_sieve
    #   prime_sieve: save time, but consume space
    return disordered_search_smooth_integer_inside_interval_(min4interval, max4interval, us, tuple_vs_dict=tuple_vs_dict, smooth_bases_checked=smooth_bases_checked, to_sorted=True)
def disordered_search_smooth_integer_inside_interval_(min4interval, max4interval, us, /, *, tuple_vs_dict=False, smooth_bases_checked=False, to_sorted=False):
    'min4interval/uint{>=1} -> max4interval/uint{>=1} -> us/strict_sorted[uint{>=2}] -> unsorted-[(n/uint{>=min4interval}{<=max4interval}, j2e4n/[uint]{len==len{us}})]'
    n_j2e4n_pairs = list(disordered_iter_search_smooth_integer_inside_interval_(min4interval, max4interval, us, tuple_vs_dict=tuple_vs_dict, smooth_bases_checked=smooth_bases_checked))
    if to_sorted:
        n_j2e4n_pairs.sort()
    return n_j2e4n_pairs
def disordered_iter_search_smooth_integer_inside_interval_(min4interval, max4interval, us, /, *, tuple_vs_dict=False, smooth_bases_checked=False):
    'min4interval/uint{>=1} -> max4interval/uint{>=1} -> us/strict_sorted[uint{>=2}] -> unsorted-Iter (n/uint{>=min4interval}{<=max4interval}, j2e4n/[uint]{len==len{us}})'
    check_int_ge(1, min4interval)
    check_int_ge(1, max4interval)
    # ok:[min4interval > max4interval]
    check_smooth_bases_(us, smooth_bases_checked=smooth_bases_checked)
    sz = len(us)
    j2u = us
    (_mk, j2e4n) = _init_j2e_(sz, tuple_vs_dict)
    _res = (Case6exit.return1, None)
    yield1 = Case6halfway.yield1
    subcall = Case6halfway.subcall
    def recur_(j, n, m, M, /, *, j2e4n=j2e4n, _res=_res):
        # [n ~ j2e4n]
        if j == -1 or m > M:
            #return
            return _res
        old_ej = j2e4n[j]
        uj = j2u[j]
        into = j > 0
        if not into:
            _ej = ceil_log_(uj, m)
            _n = uj**_ej
            m = 1 #  == ceil_div(m, _n)
            M = floor_div(M, _n)
            if M == 0:
                # <==> [1==m > M]
                pass
            else:
                # <==> [1==m <= M]
                j2e4n[j] += _ej
                n *= _n
                n0 = n
                # [m*n0 <= n <= M*n0]
                #assert m*n0 <= n <= M*n0
                _max4e = floor_log_(uj, M)
                for e in range(1+_max4e):
                    if not e == 0:
                        j2e4n[j] += 1
                        n *= uj
                    out = (n, _mk(j2e4n))
                    #yield out
                    #yield (yield1, out)
                    yield (1, out)
                    # [m*n0 <= n <= M*n0]
                #assert m*n0 <= n <= M*n0
        else:
            while 1:
                g = recur_(j-1, n, m, M)
                #yield from g
                #yield (0, g)
                #yield (subcall, g)
                yield (-2, g)
                m = ceil_div(m, uj)
                M = floor_div(M, uj)
                if m > M:
                    break
                j2e4n[j] += 1
                n *= uj
        j2e4n[j] = old_ej
        #return
        return _res
    #########
    #########
    #########
    return flatten_recur__7iter_(recur_(sz-1, 1, min4interval, max4interval))
    #########
    def main():
        it = recur_(sz-1, 1, min4interval, max4interval)
        ls = [it]
        while ls:
            for x in ls[-1]:
                if x[0] == 0:
                    break
                yield x
            else:
                ls.pop()
                continue
            it = x[1]
            ls.append(it)
    return main()
    #########
    #bug:without main() to shadow 'yield'
    def main():
        yield from recur_(sz-1, 1, min4interval, max4interval)
        return
    return main()
    #########



__all__
from seed.math.search_smooth_around_interval import check_smooth_bases_

from seed.math.search_smooth_around_interval import search_smooth_integer_around_interval_, search_max_smooth_integer_le_, search_min_smooth_integer_ge_
#def search_smooth_integer_around_interval_(min4interval, max4interval, us, /, *, tuple_vs_dict=False, smooth_bases_checked=False):

from seed.math.search_smooth_around_interval import sorted_search_smooth_integer_inside_interval_, disordered_search_smooth_integer_inside_interval_, disordered_iter_search_smooth_integer_inside_interval_
#def sorted_search_smooth_integer_inside_interval_(min4interval, max4interval, us, /, *, tuple_vs_dict=False, smooth_bases_checked=False):

from seed.math.search_smooth_around_interval import *
