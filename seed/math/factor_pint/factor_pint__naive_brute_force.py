#__all__:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/factor_pint__naive_brute_force.py

seed.math.factor_pint.factor_pint__naive_brute_force
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.factor_pint__naive_brute_force -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.factor_pint__naive_brute_force:__doc__ -ht # -ff -df

[[
for tiny uint such as < 1024
without any fancy config...
]]

>>> from seed.math.II import II, II__ft_e_pairs_, II__p2e_
>>> for n in range(1, 500):
...     assert II__p2e_(p2e:=factor_pint__naive_brute_force_(n)) == n, (n, p2e)
>>> for n in range(1, 500):
...     assert II__ft_e_pairs_(pe_it:=iter_factor_pint__naive_brute_force_(n)) == n, (n, pe_it)

>>> for n in range(1, 500):
...     assert II__ft_e_pairs_(pe_it:=_ver1__iter_factor_pint__naive_brute_force_(n)) == n, (n, pe_it)
>>> for n in range(1, 500):
...     assert II__ft_e_pairs_(pe_it:=_ver2__iter_factor_pint__naive_brute_force_(n)) == n, (n, pe_it)
>>> for n in range(1, 500):
...     assert II__ft_e_pairs_(pe_it:=_ver3__iter_factor_pint__naive_brute_force_(n)) == n, (n, pe_it)

>>> for n in range(1, 500):
...     assert II(ps:=_ver3__flatten_iter_factor_pint__naive_brute_force_(n)) == n, (n, ps)

>>> for n in range(1, 500):
...     assert II(ps:=flatten_iter_factor_pint__naive_brute_force_(n)) == n, (n, ps)
>>> for n in range(1, 500):
...     assert II(ps:=flatten_list_factor_pint__naive_brute_force_(n)) == n, (n, ps)


>>> [flatten_list_factor_pint__naive_brute_force_(24) for n in [1, 2, 8, 3, 9, 24, 2100]]
[[2, 2, 2, 3], [2, 2, 2, 3], [2, 2, 2, 3], [2, 2, 2, 3], [2, 2, 2, 3], [2, 2, 2, 3], [2, 2, 2, 3]]
>>> [factor_pint__naive_brute_force_(24) for n in [1, 2, 8, 3, 9, 24, 2100]]
[{2: 3, 3: 1}, {2: 3, 3: 1}, {2: 3, 3: 1}, {2: 3, 3: 1}, {2: 3, 3: 1}, {2: 3, 3: 1}, {2: 3, 3: 1}]





py_adhoc_call   seed.math.factor_pint.factor_pint__naive_brute_force   @factor_pint__naive_brute_force_ =18
py_adhoc_call   seed.math.factor_pint.factor_pint__naive_brute_force   ,iter_factor_pint__naive_brute_force_ =240


py_adhoc_call   seed.math.factor_pint.factor_pint__naive_brute_force   @flatten_list_factor_pint__naive_brute_force_ =2100
py_adhoc_call   seed.math.factor_pint.factor_pint__naive_brute_force   ,flatten_iter_factor_pint__naive_brute_force_ =3600



]]]'''#'''
__all__ = r'''
factor_pint__naive_brute_force_
    iter_factor_pint__naive_brute_force_
flatten_list_factor_pint__naive_brute_force_
    flatten_iter_factor_pint__naive_brute_force_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge
from seed.iters.generator_iterator2result_ import generator_iterator2result_
from math import isqrt
from itertools import repeat, groupby # islice
___end_mark_of_excluded_global_names__0___ = ...


def factor_pint__naive_brute_force_(n, /):
    'n/int{>=1} -> {p:e}'
    return dict(iter_factor_pint__naive_brute_force_(n))
def iter_factor_pint__naive_brute_force_(n, /):
    'n/int{>=1} -> Iter (p,e)'
    return _ver3__iter_factor_pint__naive_brute_force_(n)
    return _ver2__iter_factor_pint__naive_brute_force_(n)
    return _ver1__iter_factor_pint__naive_brute_force_(n)
def flatten_list_factor_pint__naive_brute_force_(n, /):
    'n/int{>=1} -> [p]'
    return [*_ver3__flatten_iter_factor_pint__naive_brute_force_(n)]
def flatten_iter_factor_pint__naive_brute_force_(n, /):
    'n/int{>=1} -> Iter p'
    return _ver3__flatten_iter_factor_pint__naive_brute_force_(n)
def _ver3__flatten_iter_factor_pint__naive_brute_force_(n, /):
    'n/int{>=1} -> Iter p'
    m = _init0(n)
    if m:
        (n, ez) = m
        yield from repeat(2, ez)
    n
    # [n%2 =!= 0]
    # [n >= 1]
    if n == 1: return
    # [n > 1]
    # [@[d:<-[2..<3]] -> [n%d =!= 0]]
    for p in range(3, 1+isqrt(n), 2):
        # [@[d:<-[2..<p]] -> [n%d =!= 0]]
        # [3 <= p <= isqrt(n)]
        # [p%2 == 1]
        # [n >= 9]
        # [n >= isqrt(n)**2 >= 3*isqrt(n)]
        # [n/2 > n/3 >= isqrt(n)]
        # => [min(n/2,isqrt(n) == isqrt(n)]
        #
        # [3 <= p <= isqrt(n) < n/2]
        # [n/p <= n/3 < n]
        # [n/p >= n/isqrt(n) >= isqrt(n)]
        # [isqrt(n) <= n/p <= n/3]
        if n%p == 0:
            q = n//p
            # !! [isqrt(n) <= n/p <= n/3]
            # [q >= isqrt(n)]
            # [q >= 1]
            n = q
            777; ep = 1
            # [n >= 1]
            # [ep == 1]
            m, (p, ep) = yield from _body0(n, p, ep)
            if not m: return
            (n, q, r) = m
            # [[n > 1][n == q*p+r][r>0]]
        # [[n > 1][n == q*p+r][r>0]]
        # [n%p =!= 0]
        # !! [@[d:<-[2..<p]] -> [n%d =!= 0]]
        # [@[d:<-[2..<(p+1)]] -> [n%d =!= 0]]
        # !! [p%2 == 1]
        # !! [n%2 == 1]
        # [@[d:<-[2..<(p+2)]] -> [n%d =!= 0]]
        # !! [n > 1]
        # [n >= (p+3)**2 > p+2]
    # [n > 1]
    # [@[d:<-[2..<=isqrt(n)]] -> [n%d =!= 0]]
    # [is_prime(n)]
    yield n
    return

def _init(n, /):
    m = _init0(n)
    if m:
        (n, ez) = m
        yield (2, ez)
    n
    # [n%2 =!= 0]
    # [n >= 1]
    return n
def _init0(n, /):
    check_int_ge(1, n)
    # [n >= 1]
    if (n >> 21):raise ValueError(f'too big:{n}')
    if n&1 == 1:
        # [n%2 == 1]
        # [n >= 1]
        return None
    m = n^(n-1)
    # 0bxxx1000 ^ 0bxxx0111
    # => 0b0001111
    ez = m.bit_length() - 1
    n >>= ez
    # [n%2 == 1]
    # [n%2 =!= 0]
    # [n >= 1]
    return (n, ez)
def _body(n, p, ep, /):
    it = _body0(n, p, ep)
    m, (p, ep) = generator_iterator2result_(it)
    yield (p, ep)
    return m
def _body0(n, p, ep, /):
    # [n >= 1]
    # [ep == 1]
    yield p
    while n > 1:
        # [n > 1]
        # [ep >= 1]
        q, r = divmod(n, p)
        # [n == q*p+r]
        if r:
            # [[n > 1][n == q*p+r][r>0]]
            # [ep >= 1]
            break
        # [r==0]
        # [q >= 1]
        n = q
        777; ep += 1
        yield p
        # [n >= 1]
        # [q,r invalid]
    else:
        # [n==1]
        # [q,r invalid]
        # [ep >= 1]
        return None, (p, ep)
    # [[n > 1][n == q*p+r][r>0]]
    return (n, q, r), (p, ep)
def _ver3__iter_factor_pint__naive_brute_force_(n, /):
    'n/int{>=1} -> Iter (p,e)'
    ps = _ver3__flatten_iter_factor_pint__naive_brute_force_(n)
    for p, it in groupby(ps):
        ls = [*it]
        ep = len(ls)
        yield (p,ep)
def _ver2__iter_factor_pint__naive_brute_force_(n, /):
    'n/int{>=1} -> Iter (p,e)'
    n = yield from _init(n)
    # [n%2 =!= 0]
    # [n >= 1]
    if n == 1: return
    # [n > 1]
    # [@[d:<-[2..<3]] -> [n%d =!= 0]]
    for p in range(3, 1+isqrt(n), 2):
        # [@[d:<-[2..<p]] -> [n%d =!= 0]]
        # [3 <= p <= isqrt(n)]
        # [p%2 == 1]
        # [n >= 9]
        # [n >= isqrt(n)**2 >= 3*isqrt(n)]
        # [n/2 > n/3 >= isqrt(n)]
        # => [min(n/2,isqrt(n) == isqrt(n)]
        #
        # [3 <= p <= isqrt(n) < n/2]
        # [n/p <= n/3 < n]
        # [n/p >= n/isqrt(n) >= isqrt(n)]
        # [isqrt(n) <= n/p <= n/3]
        if n%p == 0:
            q = n//p
            # !! [isqrt(n) <= n/p <= n/3]
            # [q >= isqrt(n)]
            # [q >= 1]
            n = q
            777; ep = 1
            # [n >= 1]
            # [ep == 1]
            m = yield from _body(n, p, ep)
            if not m: return
            (n, q, r) = m
            # [[n > 1][n == q*p+r][r>0]]
        # [[n > 1][n == q*p+r][r>0]]
        # [n%p =!= 0]
        # !! [@[d:<-[2..<p]] -> [n%d =!= 0]]
        # [@[d:<-[2..<(p+1)]] -> [n%d =!= 0]]
        # !! [p%2 == 1]
        # !! [n%2 == 1]
        # [@[d:<-[2..<(p+2)]] -> [n%d =!= 0]]
        # !! [n > 1]
        # [n >= (p+3)**2 > p+2]
    # [n > 1]
    # [@[d:<-[2..<=isqrt(n)]] -> [n%d =!= 0]]
    # [is_prime(n)]
    yield (n, 1)
    return
def _ver1__iter_factor_pint__naive_brute_force_(n, /):
    'n/int{>=1} -> Iter (p,e)'
    n = yield from _init(n)
    # [n%2 =!= 0]
    # [n >= 1]
    # [@[d:<-[2..<3]] -> [n%d =!= 0]]
    for p in range(3, 1+n, 2):
        # [@[d:<-[2..<p]] -> [n%d =!= 0]]
        # [3 <= p <= n]
        # [p%2 == 1]
        q, r = divmod(n, p)
            # will test ?[q <= p]?
        # [n == q*p+r]
        # !! [3 <= p <= n]
        # [q >= 1]
        #xxx:if r:continue
            #<<== will test ?[q <= p]?
        if r == 0:
            # [q >= 1]
            n = q
            777; ep = 1
            # [n >= 1]
            # [ep == 1]
            m = yield from _body(n, p, ep)
            if not m: return
            (n, q, r) = m
            # [[n > 1][n == q*p+r][r>0]]
        # [[n > 1][n == q*p+r][r>0]]
        # [n%p =!= 0]
        if q <= p:
            # [n == q*p+r <= p*p+(p-1) < (p+1)**2]
            # [n%p =!= 0]
            # [n > 1]
            # [is_prime(n)]
            yield (n, 1)
            return
        # [p < q < q*p+r == n]

        # !! [n%p =!= 0]
        # !! [@[d:<-[2..<p]] -> [n%d =!= 0]]
        # [@[d:<-[2..<(p+1)]] -> [n%d =!= 0]]
        # !! [p%2 == 1]
        # !! [n%2 == 1]
        # [@[d:<-[2..<(p+2)]] -> [n%d =!= 0]]



__all__
from seed.math.factor_pint.factor_pint__naive_brute_force import factor_pint__naive_brute_force_, iter_factor_pint__naive_brute_force_
from seed.math.factor_pint.factor_pint__naive_brute_force import flatten_list_factor_pint__naive_brute_force_, flatten_iter_factor_pint__naive_brute_force_
from seed.math.factor_pint.factor_pint__naive_brute_force import *
